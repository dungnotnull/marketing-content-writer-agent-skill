"""
knowledge_updater.py — Skill 9: marketing-content-writer

Crawl4ai + PubMed E-utilities pipeline that fetches latest papers and
industry updates, then appends scored, deduplicated entries to
SECOND-KNOWLEDGE-BRAIN.md.

Schedule : Weekly (Monday 06:00 UTC)
Run manually: python tools/knowledge_updater.py [--dry-run] [--category healthcare|cosmetics|fashion|copywriting]
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from xml.etree import ElementTree

try:
    import asyncio
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

    CRAWL4AI_AVAILABLE = True
except ImportError:
    CRAWL4AI_AVAILABLE = False

try:
    import requests

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    from urllib.parse import quote_plus

    URLENCODE_AVAILABLE = True
except ImportError:
    URLENCODE_AVAILABLE = False

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("knowledge_updater")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SKILL_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_BRAIN_PATH = SKILL_DIR / "SECOND-KNOWLEDGE-BRAIN.md"
DEDUP_CACHE_PATH = SKILL_DIR / "tools" / ".dedup_cache.json"
PUBMED_EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# ---------------------------------------------------------------------------
# Source definitions
# ---------------------------------------------------------------------------
SOURCES: Dict[str, List[Dict[str, Any]]] = {
    "healthcare": [
        {
            "name": "PubMed — Healthcare Marketing",
            "url": "https://pubmed.ncbi.nlm.nih.gov",
            "pubmed_query": "healthcare marketing communication consumer behavior",
            "type": "research",
            "relevance_keywords": [
                "healthcare marketing",
                "health communication",
                "consumer behavior",
                "medical advertising",
                "patient engagement",
            ],
            "max_entries": 5,
        },
        {
            "name": "FDA — Dietary Supplements Guidance",
            "url": "https://www.fda.gov/food/dietary-supplements",
            "type": "regulatory",
            "relevance_keywords": [
                "dietary supplement",
                "health claim",
                "structure function",
                "FDA",
                "warning letter",
            ],
            "max_entries": 3,
        },
        {
            "name": "FTC — Health Claims Enforcement",
            "url": "https://www.ftc.gov/news-events/topics/health-claims",
            "type": "regulatory",
            "relevance_keywords": [
                "health claim",
                "advertising",
                "endorsement",
                "supplement",
                "enforcement",
            ],
            "max_entries": 3,
        },
    ],
    "cosmetics": [
        {
            "name": "PubMed — Cosmetic Ingredients",
            "url": "https://pubmed.ncbi.nlm.nih.gov",
            "pubmed_query": "cosmetic ingredient efficacy clinical study dermatology",
            "type": "research",
            "relevance_keywords": [
                "cosmetic",
                "skin",
                "efficacy",
                "clinical",
                "ingredient",
                "dermatology",
                "topical",
            ],
            "max_entries": 5,
        },
        {
            "name": "Cosmetics Europe — Publications",
            "url": "https://www.cosmeticseurope.eu/publications-cosmeticseurope/",
            "type": "industry",
            "relevance_keywords": [
                "cosmetic",
                "regulation",
                "claim",
                "safety",
                "consumer",
            ],
            "max_entries": 3,
        },
        {
            "name": "EFSA — Health Claims Register",
            "url": "https://www.efsa.europa.eu/en/topics/topic/health-claims",
            "type": "regulatory",
            "relevance_keywords": [
                "health claim",
                "nutrition",
                "EU",
                "substantiation",
                "authorized",
            ],
            "max_entries": 3,
        },
    ],
    "fashion": [
        {
            "name": "Vogue Business — Sustainability",
            "url": "https://www.voguebusiness.com/sustainability",
            "type": "industry",
            "relevance_keywords": [
                "fashion",
                "sustainability",
                "marketing",
                "consumer",
                "trend",
                "brand",
            ],
            "max_entries": 5,
        },
        {
            "name": "Business of Fashion — Sustainability",
            "url": "https://www.businessoffashion.com/topics/sustainability/",
            "type": "industry",
            "relevance_keywords": [
                "fashion",
                "marketing",
                "brand",
                "consumer",
                "trend",
                "sustainability",
            ],
            "max_entries": 5,
        },
    ],
    "copywriting": [
        {
            "name": "Content Marketing Institute — Articles",
            "url": "https://contentmarketinginstitute.com/articles/",
            "type": "best_practices",
            "relevance_keywords": [
                "content marketing",
                "copywriting",
                "conversion",
                "email",
                "social media",
                "framework",
            ],
            "max_entries": 5,
        },
        {
            "name": "PubMed — Advertising Research",
            "url": "https://pubmed.ncbi.nlm.nih.gov",
            "pubmed_query": "advertising copywriting persuasion consumer digital marketing",
            "type": "research",
            "relevance_keywords": [
                "advertising",
                "copywriting",
                "persuasion",
                "consumer",
                "digital",
                "AIDA",
                "framework",
            ],
            "max_entries": 5,
        },
    ],
}

# ---------------------------------------------------------------------------
# Deduplication helpers
# ---------------------------------------------------------------------------

def load_dedup_cache() -> Set[str]:
    """Load previously seen entry hashes from disk."""
    if DEDUP_CACHE_PATH.exists():
        try:
            with open(DEDUP_CACHE_PATH, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                return set(data.get("hashes", []))
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Could not read dedup cache: %s — starting fresh", exc)
    return set()


def save_dedup_cache(cache: Set[str]) -> None:
    """Persist the dedup cache to disk."""
    DEDUP_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DEDUP_CACHE_PATH, "w", encoding="utf-8") as fh:
        json.dump(
            {
                "hashes": sorted(cache),
                "last_updated": datetime.now(timezone.utc).isoformat(),
            },
            fh,
            indent=2,
        )


def compute_hash(url: str, title: str) -> str:
    """Deterministic hash of a URL + title pair for deduplication."""
    key = f"{url.strip().lower()}|{title.strip().lower()}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_relevance(text: str, keywords: List[str]) -> float:
    """Return 0.0–1.0 based on keyword hit rate."""
    if not keywords:
        return 0.0
    text_lower = text.lower()
    hits = sum(1 for kw in keywords if kw.lower() in text_lower)
    return round(hits / len(keywords), 2)


def score_recency(date_str: str) -> float:
    """Return 0.0–1.0 based on how recent a date is (1.0 = today)."""
    try:
        for fmt in ("%Y-%m-%d", "%Y %b %d", "%d %b %Y", "%b %d, %Y"):
            try:
                pub_date = datetime.strptime(date_str.strip(), fmt)
                break
            except ValueError:
                continue
        else:
            return 0.5
    except Exception:
        return 0.5

    now = datetime.now(timezone.utc)
    age_days = max((now - pub_date.replace(tzinfo=timezone.utc)).days, 0)
    if age_days <= 30:
        return 1.0
    if age_days <= 90:
        return 0.8
    if age_days <= 365:
        return 0.5
    return 0.2


# ---------------------------------------------------------------------------
# PubMed E-utilities API
# ---------------------------------------------------------------------------

def fetch_pubmed_entries(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """Search PubMed via E-utilities and return structured article dicts."""
    if not REQUESTS_AVAILABLE:
        logger.warning("requests library not available — cannot query PubMed API")
        return []

    try:
        from urllib.parse import quote_plus as _qp
        encoded_query = _qp(query)
    except Exception:
        encoded_query = query.replace(" ", "+")

    search_url = (
        f"{PUBMED_EUTILS_BASE}/esearch.fcgi?db=pubmed"
        f"&term={encoded_query}&retmax={max_results}"
        f"&sort=date&retmode=json"
    )

    try:
        resp = requests.get(search_url, timeout=15)
        resp.raise_for_status()
        search_data = resp.json()
    except Exception as exc:
        logger.error("PubMed esearch failed: %s", exc)
        return []

    id_list = search_data.get("esearchresult", {}).get("idlist", [])
    if not id_list:
        logger.info("PubMed esearch returned 0 results for query: %s", query)
        return []

    fetch_url = (
        f"{PUBMED_EUTILS_BASE}/efetch.fcgi?db=pubmed"
        f"&id={','.join(id_list)}&rettype=abstract&retmode=xml"
    )

    try:
        fetch_resp = requests.get(fetch_url, timeout=20)
        fetch_resp.raise_for_status()
    except Exception as exc:
        logger.error("PubMed efetch failed: %s", exc)
        return []

    entries: List[Dict[str, Any]] = []
    try:
        raw_xml = fetch_resp.content
        # Strip XML processing instructions and clean encoding issues
        raw_xml = re.sub(rb'<\?xml[^>]*\?>', b'', raw_xml)
        raw_xml = re.sub(rb'&(?!(?:amp|lt|gt|apos|quot);)[^;]*;', b'&amp;', raw_xml)
        root = ElementTree.fromstring(raw_xml)
        for article in root.findall(".//PubmedArticle"):
            title_el = article.find(".//ArticleTitle")
            title = (title_el.text or "").strip() if title_el is not None and title_el.text else ""

            authors_list: List[str] = []
            for author in article.findall(".//Author"):
                last = author.find("LastName")
                fore = author.find("ForeName")
                name_parts = []
                if last is not None and last.text:
                    name_parts.append(last.text)
                if fore is not None and fore.text:
                    name_parts.append(fore.text[0])
                if name_parts:
                    authors_list.append(" ".join(name_parts))
            authors = ", ".join(authors_list[:6])
            if len(authors_list) > 6:
                authors += " et al."

            abstract_el = article.find(".//AbstractText")
            abstract = (abstract_el.text or "").strip()[:500] if abstract_el is not None and abstract_el.text else ""

            journal_el = article.find(".//Journal/Title")
            journal = (journal_el.text or "").strip() if journal_el is not None and journal_el.text else ""

            pub_date_el = article.find(".//PubDate")
            date_str = ""
            if pub_date_el is not None:
                year_el = pub_date_el.find("Year")
                medline_el = pub_date_el.find("MedlineDate")
                if year_el is not None and year_el.text:
                    date_str = year_el.text
                elif medline_el is not None and medline_el.text:
                    date_str = medline_el.text

            pmid_el = article.find(".//PMID")
            pmid = pmid_el.text if pmid_el is not None and pmid_el.text else ""

            doi = ""
            for aid in article.findall(".//ArticleId"):
                id_type = aid.get("IdType", "")
                if id_type == "doi" and aid.text:
                    doi = aid.text
                    break

            url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""
            pub_date = f"{date_str}-01-01" if len(date_str) == 4 else date_str

            entries.append({
                "title": title[:200],
                "authors": authors,
                "journal": journal,
                "date": pub_date,
                "doi": doi,
                "url": url or f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_query}",
                "pmid": pmid,
                "abstract": abstract,
                "type": "research",
                "source_name": "PubMed",
            })
    except ElementTree.ParseError as exc:
        logger.error("PubMed XML parse error: %s", exc)

    return entries
# ---------------------------------------------------------------------------
# Generic HTML crawl extraction
# ---------------------------------------------------------------------------

def extract_entries_from_html(html_content: str, source: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse raw HTML to extract structured entries from headings and meta tags."""
    entries: List[Dict[str, Any]] = []

    title_pattern = re.compile(
        r'<(?:h[123]|title)[^>]*>(.*?)</(?:h[123]|title)>',
        re.IGNORECASE | re.DOTALL,
    )
    raw_titles = title_pattern.findall(html_content)
    clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in raw_titles if len(t.strip()) > 15]

    meta_desc_pattern = re.compile(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
        re.IGNORECASE,
    )
    meta_descriptions = meta_desc_pattern.findall(html_content)

    date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')
    dates = date_pattern.findall(html_content)
    latest_date = dates[0] if dates else datetime.now(timezone.utc).strftime("%Y-%m-%d")

    max_entries = source.get("max_entries", 5)
    keywords = source.get("relevance_keywords", [])

    for i, title in enumerate(clean_titles[:max_entries]):
        relevance = score_relevance(title, keywords)
        if relevance < 0.1:
            continue

        description = meta_descriptions[i] if i < len(meta_descriptions) else ""
        entries.append({
            "title": title[:150],
            "authors": "",
            "journal": "",
            "date": latest_date,
            "doi": "",
            "url": source["url"],
            "pmid": "",
            "abstract": description[:400] if description else "",
            "type": source.get("type", "industry"),
            "source_name": source["name"],
        })

    return entries


# ---------------------------------------------------------------------------
# Entry formatting
# ---------------------------------------------------------------------------

def format_entry_for_knowledge_brain(entry: Dict[str, Any], today: str) -> str:
    """Render a single knowledge entry in the canonical Markdown format."""
    authors_line = f"- **Authors:** {entry['authors']}\n" if entry.get("authors") else ""
    doi_line = ""
    if entry.get("doi"):
        doi_line = f"- **DOI:** {entry['doi']}\n"
    elif entry.get("url"):
        doi_line = f"- **URL:** {entry['url']}\n"

    abstract_text = entry.get("abstract", "")
    key_finding = abstract_text[:300] if abstract_text else f"[See source for details — {entry.get('source_name', 'Unknown')}]"

    entry_type = entry.get("type", "unknown").replace("_", " ").title()

    return (
        f"\n### [{today}] {entry.get('source_name', 'Unknown')} — {entry['title']}\n"
        f"{authors_line}"
        f"{doi_line}"
        f"- **Type:** {entry_type}\n"
        f"- **Relevance:** Content from {entry.get('source_name', 'Unknown')} "
        f"relevant to marketing content writing in healthcare/cosmetics/fashion\n"
        f"- **Key Finding:** {key_finding}\n"
    )


# ---------------------------------------------------------------------------
# Append to SECOND-KNOWLEDGE-BRAIN.md
# ---------------------------------------------------------------------------

def append_to_knowledge_brain(new_entries: List[str], category: str = "Mixed") -> int:
    """Insert new entries into the knowledge brain file and update the log."""
    if not new_entries:
        return 0

    if not KNOWLEDGE_BRAIN_PATH.exists():
        logger.error("SECOND-KNOWLEDGE-BRAIN.md not found at %s", KNOWLEDGE_BRAIN_PATH)
        return 0

    with open(KNOWLEDGE_BRAIN_PATH, "r", encoding="utf-8") as fh:
        content = fh.read()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_log_row = f"| {today} | Automated crawl | {len(new_entries)} | {category} |"

    insert_before = "## Knowledge Update Log"
    if insert_before in content:
        insert_pos = content.index(insert_before)
        new_content = (
            content[:insert_pos]
            + "\n".join(new_entries)
            + "\n\n"
            + content[insert_pos:]
        )
    else:
        new_content = content + "\n\n" + "\n".join(new_entries)

    footer = "_Automated updates begin after tools/knowledge_updater.py is deployed (Phase 3)._"
    if footer in new_content:
        new_content = new_content.replace(
            footer,
            f"{footer}\n{new_log_row}",
        )

    with open(KNOWLEDGE_BRAIN_PATH, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    logger.info("Appended %d entries to SECOND-KNOWLEDGE-BRAIN.md", len(new_entries))
    return len(new_entries)


# ---------------------------------------------------------------------------
# Async crawl (crawl4ai)
# ---------------------------------------------------------------------------

async def crawl_source_async(
    source: Dict[str, Any],
    dedup_cache: Set[str],
    dry_run: bool = False,
) -> Tuple[List[str], Set[str], int]:
    """Crawl a single source via crawl4ai. Returns (entries, new_hashes, skipped_count)."""
    new_entries: List[str] = []
    new_hashes: Set[str] = set()
    skipped = 0

    if not CRAWL4AI_AVAILABLE:
        logger.warning("crawl4ai unavailable — skipping %s", source["name"])
        return new_entries, new_hashes, skipped

    try:
        browser_config = BrowserConfig(headless=True, verbose=False)
        run_config = CrawlerRunConfig(page_timeout=30000)

        async with AsyncWebCrawler(config=browser_config) as crawler:
            result = await crawler.arun(url=source["url"], config=run_config)

            if not result.success:
                logger.error("Crawl failed for %s: %s", source["name"], result.error_message)
                return new_entries, new_hashes, skipped

            raw_html = result.html or ""
            entries = extract_entries_from_html(raw_html, source)

            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

            for entry in entries:
                entry_hash = compute_hash(entry["url"], entry["title"])
                if entry_hash in dedup_cache:
                    skipped += 1
                    logger.debug("DUP skipped: %s", entry["title"][:60])
                    continue

                formatted = format_entry_for_knowledge_brain(entry, today)
                new_entries.append(formatted)
                new_hashes.add(entry_hash)
                logger.info("NEW: %s (relevance: N/A)", entry["title"][:60])

    except Exception as exc:
        logger.error("Crawl error for %s: %s", source["name"], exc)

    return new_entries, new_hashes, skipped


# ---------------------------------------------------------------------------
# Sync fallback (requests)
# ---------------------------------------------------------------------------

def crawl_source_sync(
    source: Dict[str, Any],
    dedup_cache: Set[str],
) -> Tuple[List[str], Set[str], int]:
    """Fallback crawler using requests when crawl4ai is unavailable."""
    if not REQUESTS_AVAILABLE:
        return [], set(), 0

    new_entries: List[str] = []
    new_hashes: Set[str] = set()
    skipped = 0

    try:
        headers = {"User-Agent": "Mozilla/5.0 (research bot; skill-knowledge-updater/1.0)"}
        response = requests.get(source["url"], headers=headers, timeout=15)
        response.raise_for_status()

        entries = extract_entries_from_html(response.text, source)
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        for entry in entries:
            entry_hash = compute_hash(entry["url"], entry["title"])
            if entry_hash in dedup_cache:
                skipped += 1
                continue
            formatted = format_entry_for_knowledge_brain(entry, today)
            new_entries.append(formatted)
            new_hashes.add(entry_hash)
            logger.info("NEW: %s", entry["title"][:60])

    except Exception as exc:
        logger.error("Requests fallback error for %s: %s", source["name"], exc)

    return new_entries, new_hashes, skipped
# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def run_updater(
    categories: Optional[List[str]] = None,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """
    Main entry point for the knowledge updater.

    Args:
        categories: List of category names to update. If None, updates all.
        dry_run: If True, prints what would be added without writing to file.

    Returns:
        Summary dict with counts and metadata.
    """
    print(f"\n{'=' * 60}")
    print(f"Marketing Content Writer — Knowledge Updater")
    print(f"Run time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Dry run: {dry_run}")
    print(f"Categories: {categories or 'ALL'}")
    print(f"crawl4ai: {'available' if CRAWL4AI_AVAILABLE else 'NOT available'}")
    print(f"requests: {'available' if REQUESTS_AVAILABLE else 'NOT available'}")
    print(f"{'=' * 60}\n")

    dedup_cache = load_dedup_cache()
    logger.info("Dedup cache loaded: %d known entries", len(dedup_cache))

    target_categories = categories or list(SOURCES.keys())
    all_new_entries: List[str] = []
    total_skipped = 0
    total_new_hashes: Set[str] = set()
    categories_processed: List[str] = []

    for category in target_categories:
        if category not in SOURCES:
            logger.warning("Unknown category: %s — skipping", category)
            continue

        categories_processed.append(category)
        logger.info("--- Category: %s ---", category.upper())

        for source in SOURCES[category]:
            logger.info("Crawling: %s", source["name"])

            # Prefer PubMed E-utilities API for PubMed sources
            pubmed_query = source.get("pubmed_query")
            if pubmed_query and REQUESTS_AVAILABLE:
                pm_entries = fetch_pubmed_entries(
                    pubmed_query, max_results=source.get("max_entries", 5)
                )
                today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                for entry in pm_entries:
                    url = entry.get("url", source["url"])
                    entry_hash = compute_hash(url, entry["title"])
                    if entry_hash in (dedup_cache | total_new_hashes):
                        total_skipped += 1
                        logger.debug("DUP skipped: %s", entry["title"][:60])
                        continue

                    relevance = score_relevance(
                        entry["title"] + " " + entry.get("abstract", ""),
                        source.get("relevance_keywords", []),
                    )
                    recency = score_recency(entry.get("date", ""))
                    entry["relevance_score"] = round((relevance + recency) / 2, 2)

                    if entry["relevance_score"] < 0.15:
                        total_skipped += 1
                        continue

                    formatted = format_entry_for_knowledge_brain(entry, today)
                    all_new_entries.append(formatted)
                    total_new_hashes.add(entry_hash)
                    logger.info(
                        "NEW: %s (score: %.2f)",
                        entry["title"][:60],
                        entry["relevance_score"],
                    )

            elif CRAWL4AI_AVAILABLE:
                entries, hashes, skipped = asyncio.run(
                    crawl_source_async(
                        source, dedup_cache | total_new_hashes, dry_run
                    )
                )
                all_new_entries.extend(entries)
                total_new_hashes.update(hashes)
                total_skipped += skipped

            else:
                entries, hashes, skipped = crawl_source_sync(
                    source, dedup_cache | total_new_hashes
                )
                all_new_entries.extend(entries)
                total_new_hashes.update(hashes)
                total_skipped += skipped

    print(f"\n{'=' * 60}")
    print(f"New entries found:    {len(all_new_entries)}")
    print(f"Duplicates skipped:   {total_skipped}")
    print(f"Categories processed: {', '.join(categories_processed)}")
    print(f"{'=' * 60}\n")

    if not dry_run and all_new_entries:
        written = append_to_knowledge_brain(all_new_entries, category=", ".join(categories_processed))
        save_dedup_cache(dedup_cache | total_new_hashes)
        print(f"[DONE] Appended {written} new entries to SECOND-KNOWLEDGE-BRAIN.md")
        print(f"[DONE] Dedup cache updated ({len(dedup_cache) + len(total_new_hashes)} total hashes)")
    elif dry_run:
        print("[DRY RUN] No changes written.")
        for entry in all_new_entries[:5]:
            print(f"  Preview: {entry[:200]}...")
    else:
        print("[INFO] No new entries to add.")

    return {
        "total_new": len(all_new_entries),
        "total_skipped": total_skipped,
        "categories_processed": categories_processed,
        "dry_run": dry_run,
        "dedup_cache_size": len(dedup_cache) + len(total_new_hashes),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest domain knowledge",
    )
    parser.add_argument(
        "--category",
        nargs="+",
        choices=list(SOURCES.keys()),
        help="Which categories to update (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be added without writing to file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable DEBUG-level logging output",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger("knowledge_updater").setLevel(logging.DEBUG)

    result = run_updater(
        categories=args.category,
        dry_run=args.dry_run,
    )

    print(f"\nSummary: {json.dumps(result, indent=2)}")
    sys.exit(0 if result["total_new"] >= 0 else 1)


if __name__ == "__main__":
    main()