<div align="center">

# 🎯 Marketing Content Writer

**Evidence-backed marketing content for healthcare, cosmetics & fashion — compliant, on-brand, and conversion-ready.**

[![Skill](https://img.shields.io/badge/Skill-9-blueviolet?style=flat-square)](./CLAUDE.md)
[![Cluster](https://img.shields.io/badge/Cluster-D%20Content%20Creation-ff6b6b?style=flat-square)](./PROJECT-detail.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](./tools/knowledge_updater.py)

*A [Claude Code Skill](https://docs.anthropic.com/en/docs/claude-code) that combines world-renowned copywriting frameworks with regulatory pre-screening, peer-reviewed evidence sourcing, platform-native formatting, and A/B variant generation.*

</div>

---

## ✨ Why This Skill?

Marketing teams in **healthcare**, **cosmetics**, and **fashion** face a brutal paradox: produce high-converting content that *also* complies with FDA, EU Cosmetics Regulation, FTC guidelines, and regional advertising codes. Generic AI tools ignore compliance entirely, generate unsupported health claims, and produce copy that sounds identical across brands.

**This skill solves that** by grounding every piece of content in:

| Pillar | What It Means |
|--------|---------------|
| 🏛️ **Copywriting Frameworks** | 10 world-class frameworks — AIDA, PAS, FAB, StoryBrand, PASTOR, BAB, ACCA, QUEST, HSO, 4Ps — each selected by goal × audience × platform × industry |
| ⚖️ **Regulatory Pre-Screening** | FDA, EU EC 1223/2009, FTC, UK ASA, ASEAN — compliance checked *before* content is written, not after |
| 📚 **Evidence-Based Claims** | Every health/efficacy claim cites Tier 1–4 research (systematic reviews, RCTs, cohort studies) |
| 📱 **Platform-Native Formatting** | Instagram, TikTok, Email, Blog, Landing Page, LinkedIn, YouTube, Print — each with character limits, hashtag rules, CTA placement |
| 🎨 **Brand Voice Scoring** | Quantitative 1–10 scoring across 5 dimensions — brand voice, compliance, readability, persuasion, SEO |
| 🧪 **A/B Variants** | Every deliverable includes two testable variants — not a word swap, but a meaningful divergence in angle, hook, or CTA strategy |

---

## 🏗️ Architecture

```
/marketing-content-writer invoked
  ┌─────────────────────────────────────────────────────────────────┐
  │  Stage 1: sub-brief-intake          → extract content brief      │
  │  Stage 2: sub-compliance-checker    → regulatory constraint map  │
  │  Stage 3: Knowledge Research        → WebSearch + SECOND-BRAIN    │
  │  Stage 4: sub-framework-selector    → select optimal framework   │
  │  Stage 5: sub-content-generator     → draft Variant A            │
  │  Stage 6: sub-platform-adapter      → reformat for platform      │
  │  Stage 7: sub-quality-reviewer       → 5-dimension quality gate  │
  │  Stage 8: sub-ab-variant-generator  → generate Variant B         │
  │  Stage 9: Final Synthesis            → structured deliverable     │
  └─────────────────────────────────────────────────────────────────┘
```

### Quality Gates

| Gate | Condition | Action if Failed |
|------|-----------|-----------------|
| **Gate 1** | All 8 brief fields populated | Ask user for missing fields |
| **Gate 2** | Compliance risk ≤ Medium | Warn user + offer conservative language |
| **Gate 3** | Zero forbidden claims + all citations | Auto-revise draft |
| **Gate 4** | Brand Voice ≥ 7, Persuasion ≥ 7, Compliance = Pass | Apply improvement notes, re-score |
| **Gate 5** | Variant B passes Gates 3 & 4 | Regenerate with alternate angle |

---

## 📁 Project Structure

```
marketing-content-writer-agent-skill/
├── CLAUDE.md                          # Skill identity, harness flow, tools
├── README.md                          # This file
├── PROJECT-detail.md                   # Full technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase-by-phase build roadmap
├── SECOND-KNOWLEDGE-BRAIN.md          # Self-improving domain knowledge base (39+ entries)
├── progression.json                    # Build completion status
├── cross-skill-compatibility.md       # Cross-skill wiring verification
│
├── skills/
│   ├── main.md                        # ⚡ Primary skill entry point (9-stage harness)
│   ├── sub-brief-intake.md            # Parse & validate content brief (8 required fields)
│   ├── sub-compliance-checker.md      # FDA / EU / FTC / ASEAN regulatory screening
│   ├── sub-framework-selector.md      # 10-framework selection matrix (goal × platform × industry)
│   ├── sub-content-generator.md       # Evidence-backed content draft (10 framework templates)
│   ├── sub-platform-adapter.md        # 10 platform format specs + native language patterns
│   ├── sub-quality-reviewer.md        # 5-dimension quantitative scoring + auto-revise
│   └── sub-ab-variant-generator.md    # 5 divergence strategies + A/B comparison table
│
├── tools/
│   ├── knowledge_updater.py           # 🕷️ Crawl4AI + PubMed E-utilities pipeline
│   └── .dedup_cache.json             # Deduplication cache (auto-generated)
│
└── tests/
    ├── test-scenarios.md             # 7 scenario tests across all 3 industries
    └── test-execution-log.md          # Validated execution results (all PASS)
```

---

## 🧠 Sub-Skills Deep Dive

### 1. `sub-brief-intake.md` — Content Brief Parser
Extracts 8 required fields from any user request: industry, product, audience, platform, goal, tone, word count, compliance jurisdiction. Includes auto-detection signals, platform default word counts, and a targeted clarification question tree for missing data.

### 2. `sub-compliance-checker.md` — Regulatory Gate
Decision matrix covering **3 industries × 4 jurisdictions** (US FDA, EU EC 1223/2009, UK ASA, ASEAN ACD). Produces forbidden claims list, approved language guide with safe alternatives, disclosure requirements, and risk level (Low/Medium/High). High-risk content triggers Gate 2 block with conservative language track option.

### 3. `sub-framework-selector.md` — Framework Intelligence
Selection matrix across **4 dimensions**: goal (awareness → 4Ps), platform (TikTok → HSO), industry (healthcare → PAS), tone (empathetic → StoryBrand). Includes secondary framework pairing logic and key psychological principle citation for each framework.

### 4. `sub-content-generator.md` — Draft Engine
Executes 10 framework templates (AIDA, PAS, FAB, StoryBrand, PASTOR, BAB, ACCA, QUEST, HSO, 4Ps) with evidence citation injection, compliance constraint enforcement, word count calibration (±10%), and Gate 3 self-check.

### 5. `sub-platform-adapter.md` — Platform Formatter
Complete format specifications for **10 platforms**: Instagram Feed, Instagram Story, TikTok Script, Email, Blog Post, Landing Page, Product Description, LinkedIn Post, YouTube Description, Print Ad. Each spec includes character limits, hashtag rules, CTA placement, visual cue notes, and platform-native language patterns.

### 6. `sub-quality-reviewer.md` — Quality Engine
Quantitative scoring across 5 dimensions:
- **Brand Voice Consistency** (1–10, threshold ≥ 7) — tone, vocabulary, rhythm, emotional register
- **Regulatory Compliance** (Pass/Warn/Fail) — re-run forbidden claims check
- **Readability** (Flesch-Kincaid Grade 6–12) — sentence length, passive voice, jargon
- **Persuasion Score** (1–10, threshold ≥ 7) — hook strength, problem clarity, CTA clarity, emotional resonance
- **SEO Alignment** (1–10, Blog/LP only) — keyword placement, meta description

Auto-revision loop: if any dimension fails, generates specific improvement notes with before/after examples and re-scores.

### 7. `sub-ab-variant-generator.md` — Variant Engine
5 meaningfully different divergence strategies:
1. **Angle Flip** — Pain (PAS) vs. Aspiration (BAB)
2. **Hook Swap** — Statistic vs. Question vs. Story vs. Counterintuitive
3. **CTA Strategy Swap** — High-commitment vs. Low-commitment
4. **Sub-Segment Targeting** — Primary vs. Secondary audience
5. **Evidence Angle Swap** — Clinical evidence vs. Social proof

Includes A/B comparison table and recommended test metric with hypothesis.

---

## ⚖️ Regulatory Coverage

### Healthcare (US)
| Framework | Scope | Key Rule |
|-----------|-------|---------|
| FDA 21 CFR Part 202 | Prescription drug advertising | Must include brief summary of risks |
| FDA Structure/Function Claims | Dietary supplements | May *not* claim to diagnose, treat, cure, or prevent disease |
| FTC Endorsement Guides 16 CFR Part 255 | Influencer marketing | Material connections must be disclosed |

### Cosmetics (EU)
| Framework | Scope | Key Rule |
|-----------|-------|---------|
| EC 1223/2009 Art. 20 | All cosmetic claims | Must be substantiated, truthful, not misleading |
| EFSA EC 1924/2006 | Health/nutrition claims | Must be on EU Register of Authorized Claims |
| UK ASA / BCAP Code | UK cosmetic advertising | Medical claims require medical authorization |

### Fashion (Sustainability)
| Framework | Scope | Key Rule |
|-----------|-------|---------|
| EU Green Claims Directive | Environmental claims | Must be verified by independent third party |
| FTC Green Guides 16 CFR Part 260 | US sustainability claims | Unqualified "eco-friendly" is deceptive |
| UK CMA Green Claims Code | UK environmental claims | Must be accurate, clear, not misleading |

### ASEAN
| Framework | Scope | Key Rule |
|-----------|-------|---------|
| ASEAN Cosmetic Directive (ACD) | 10 member states | Product notification required; claims must align with ASEAN guideline |

---

## 📚 Knowledge Base

`SECOND-KNOWLEDGE-BRAIN.md` is a self-improving domain knowledge base with **39+ seed entries** across 7 categories:

| Category | Entries | Highlights |
|----------|---------|-----------|
| Copywriting Frameworks | 5 | AIDA digital performance, PAS in healthcare, StoryBrand for LPs, FAB for e-commerce, HSO for short-form video |
| Regulatory Updates | 6 | FDA supplement guidance, EU EC 1223/2009 violations, FTC endorsement update, UK ASA adjudications, ASEAN claim guideline, EU Green Claims |
| Cosmetic Ingredient Research | 6 | Vitamin C, Retinol, Hyaluronic Acid, Niacinamide, Peptides, SPF — all with Tier-rated evidence |
| Healthcare Advertising Rules | 6 | FDA 21 CFR 202, Structure/Function decision framework, FTC substantiation, EMA 2001/83/EC, MHRA Blue Guide, Warning letter trends |
| Fashion Trend Intelligence | 6 | State of Fashion 2025, sustainability trust data, social commerce benchmarks, fashion tech, consumer trends, Google search data |
| Consumer Psychology Research | 5 | Prospect Theory, social proof meta-analysis, ELM, scarcity/urgency, regulatory focus theory |
| Platform Algorithm Changes | 5 | Instagram 2025, TikTok 2025, LinkedIn 2025, YouTube 2025, Email 2025 benchmarks |

Automated weekly updates via `tools/knowledge_updater.py` — crawl4AI + PubMed E-utilities with deduplication and relevance scoring.

---

## 🛠️ Knowledge Updater Pipeline

`tools/knowledge_updater.py` is a production-grade Python pipeline:

```bash
# Run all categories (weekly schedule)
python tools/knowledge_updater.py

# Run specific categories
python tools/knowledge_updater.py --category healthcare cosmetics

# Preview without writing
python tools/knowledge_updater.py --dry-run

# Verbose logging
python tools/knowledge_updater.py --verbose
```

**Features:**
- PubMed E-utilities API for structured research paper extraction (title, authors, DOI, abstract, journal)
- crawl4AI integration for web source crawling (FDA, FTC, EFSA, Vogue Business, etc.)
- `requests` fallback when crawl4AI is unavailable
- SHA-256 hash deduplication — re-running does not add duplicate entries
- Combined relevance + recency scoring (keyword hit rate × date freshness)
- Safe append to SECOND-KNOWLEDGE-BRAIN.md with atomic dedup cache

---

## 🧪 Test Coverage

7 comprehensive test scenarios across all 3 industries, multiple platforms, and compliance edge cases:

| # | Scenario | Industry | Platform | Key Test |
|---|----------|----------|----------|----------|
| 1 | Probiotic supplement post | Healthcare | Instagram Feed | FDA structure/function compliance |
| 2 | Vitamin C serum landing page | Cosmetics | Landing Page | EU EC 1223/2009 claim substantiation |
| 3 | Sustainable denim TikTok | Fashion | TikTok Script | Greenwashing detection + FTC Green Guides |
| 4 | Weight management clinic email | Healthcare | Email | FTC disclaimer requirements |
| 5 | Skincare product descriptions ×3 | Cosmetics | Product Description | Multi-SKU + dual jurisdiction (US+EU) + FDA Drug Facts |
| 6 | Luxury handbag Instagram story | Fashion | Instagram Story | Low-risk assessment, native CTA |
| 7 | Immune supplement blog (HIGH RISK) | Healthcare | Blog Post | Gate 2 block + conservative track reroute |

**All scenarios: ✅ PASS** — see [`tests/test-execution-log.md`](./tests/test-execution-log.md) for full validation details.

---

## 🚀 Quick Start

### As a Claude Code Skill

1. Clone this repository into your Claude Code skills directory
2. Invoke the skill in Claude Code:

```
/marketing-content-writer

"Write an Instagram post for our new probiotic supplement targeting adults 30-50 with digestive issues. Tone: empathetic and conversational. Goal: drive purchase via link in bio. US market."
```

The skill will automatically:
1. Parse your brief (Stage 1)
2. Check FDA compliance (Stage 2)
3. Research evidence (Stage 3)
4. Select the optimal framework — likely PAS (Stage 4)
5. Generate Variant A with citations (Stage 5)
6. Format for Instagram (Stage 6)
7. Score quality across 5 dimensions (Stage 7)
8. Generate Variant B with different angle (Stage 8)
9. Deliver structured output with both variants, quality scores, and compliance certification (Stage 9)

### Running the Knowledge Updater

```bash
pip install crawl4ai requests

# Full update
python tools/knowledge_updater.py

# Preview only
python tools/knowledge_updater.py --dry-run

# Specific industry
python tools/knowledge_updater.py --category healthcare cosmetics
```

---

## 📊 Output Format

Every deliverable follows this structured format:

```
════════════════════════════════════════════════════════════════
MARKETING CONTENT DELIVERABLE
Skill: marketing-content-writer | Date: 2026-06-15
════════════════════════════════════════════════════════════════

## CONTENT BRIEF SUMMARY
- Industry: healthcare | Product: GutBalance Pro | Platform: Instagram Feed

## COMPLIANCE CERTIFICATION
- Regulatory Frameworks: FDA Structure/Function, FTC | Risk: Medium | ✅ COMPLIANT

## COPYWRITING FRAMEWORK
- Primary: PAS — pain-driven purchase for health supplements

## EVIDENCE BASE
| Claim | Evidence | Tier | Citation |
| "supports healthy digestion" | RCT n=200 | Tier 2 | DOI:10.2196/32109 |

## VARIANT A — Pain Angle
[Platform-formatted content]

**Quality Scorecard:** Brand Voice 8/10 | Compliance Pass | Grade 7 | Persuasion 8/10

## VARIANT B — Aspiration Angle
[Platform-formatted content]

**Quality Scorecard:** Brand Voice 8/10 | Compliance Pass | Grade 6 | Persuasion 7/10

## A/B COMPARISON TABLE
| Dimension | Variant A | Variant B |
| Primary Angle | Pain-focused | Aspiration-focused |
| CTA Strategy | High-commitment | Low-commitment |
| Recommended Test Metric | CTR | Engagement rate |

## NEXT STEPS
1. A/B test both variants for 7 days minimum
2. Monitor compliance if any copy is modified
3. Run knowledge_updater.py before next campaign cycle
════════════════════════════════════════════════════════════════
```

---

## 🧭 Copywriting Frameworks

| Framework | Structure | Best For | Psychological Principle |
|-----------|-----------|----------|------------------------|
| **AIDA** | Attention → Interest → Desire → Action | General awareness, ads | Sequential attention processing |
| **PAS** | Problem → Agitate → Solution | Healthcare, supplements, pain-point content | Loss aversion |
| **FAB** | Feature → Advantage → Benefit | Product descriptions, e-commerce | Rational decision-making |
| **StoryBrand** | Character → Problem → Guide → Plan → CTA → Failure → Success | Landing pages, brand narrative | Narrative transportation |
| **PASTOR** | Problem → Amplify → Story → Transformation → Offer → Response | Long-form, email sequences | Transformation arc motivation |
| **BAB** | Before → After → Bridge | Social proof, transformation content | Social comparison + aspirational self |
| **ACCA** | Awareness → Comprehension → Conviction → Action | Educational health content | Health literacy model |
| **QUEST** | Qualify → Understand → Educate → Stimulate → Transition | Premium products, niche audiences | Self-selection + exclusivity |
| **HSO** | Hook → Story → Offer | TikTok, short-form video | Pattern interrupt + curiosity gap |
| **4Ps** | Promise → Picture → Proof → Push | Email, direct response | Cognitive loading reduction |

---

## 🔬 Evidence Hierarchy

Claims in this skill follow a strict evidence hierarchy:

| Tier | Type | Acceptable For |
|------|------|---------------|
| **1** | Systematic review / Meta-analysis | All health/efficacy claims (preferred) |
| **2** | Randomized Controlled Trial (RCT) | All health/efficacy claims |
| **3** | Cohort / observational study (n > 500) | Supporting evidence only |
| **4** | Expert consensus statement | Supporting evidence only |
| **5** | Industry survey / white paper | Trend data, benchmarks only |
| **6** | Anecdote / testimonial | Requires FTC disclosure; never as primary evidence |

---

## 📋 Development Phases

| Phase | Name | Status | Key Deliverable |
|-------|------|--------|----------------|
| 0 | Research & Architecture | ✅ Complete | 10 frameworks documented, 4 jurisdictions mapped, quality gates defined |
| 1 | Core Sub-Skills | ✅ Complete | 7 sub-skill files with purpose, I/O, tools, step-by-step, quality gates |
| 2 | Main Harness + Quality Gates | ✅ Complete | 9-stage orchestration with 5 embedded quality gates |
| 3 | Knowledge Pipeline | ✅ Complete | crawl4AI + PubMed pipeline, 39+ seed entries, deduplication verified |
| 4 | Testing & Validation | ✅ Complete | 7 scenarios validated, edge cases tested, all gates pass |
| 5 | Integration & Wiring | ✅ Complete | Cross-skill compatibility verified, progression.json updated |

---

## 📜 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

When contributing, please ensure:
- All content follows the compliance frameworks documented in `sub-compliance-checker.md`
- Any new evidence citations include Tier ratings
- New platform specs follow the existing format in `sub-platform-adapter.md`
- Run `python tools/knowledge_updater.py --dry-run` to verify pipeline health

---

<div align="center">

**Built with ❤️ for marketers who take compliance seriously.**

*Every claim cited. Every platform native. Every variant testable.*

</div>