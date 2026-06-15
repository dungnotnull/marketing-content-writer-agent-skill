---
name: sub-compliance-checker
description: Screen content brief against FDA, EU Cosmetics Regulation, FTC, and regional advertising guidelines — produces forbidden claims list, approved language guide, and risk level
---

## Purpose

Map the content brief to applicable regulatory frameworks and produce a compliance constraint package that all downstream content generation stages must respect. This sub-skill prevents illegal advertising claims before they are written, not after.

## Inputs

- Structured brief from `sub-brief-intake` (industry, product, goal, jurisdiction)
- Any product claims or key messages provided by the user

## Outputs

```json
{
  "jurisdiction": "US | EU | UK | ASEAN | global",
  "applicable_frameworks": ["FDA 21 CFR Part 202", "EC 1223/2009", ...],
  "forbidden_claims": ["string"],
  "approved_language_guide": [{"unsafe": "string", "safe_alternative": "string"}],
  "disclosure_requirements": ["string"],
  "risk_level": "Low | Medium | High",
  "risk_rationale": "string"
}
```

## Step-by-Step Instructions

### Step 1 — Select Regulatory Frameworks by Industry + Jurisdiction

Use this decision matrix:

| Industry | US | EU | UK | ASEAN |
|----------|----|----|----|-------|
| Healthcare (supplements) | FDA Structure/Function Claims, FTC | EFSA EC 1924/2006, EU Health Claims Register | MHRA, ASA BCAP | ASEAN cosmetics directive, country-specific food supplement regs |
| Healthcare (medical services) | FDA 21 CFR Part 202, FTC | EU MDR, national health advertising codes | NHS advertising code, ASA | Ministry of Health advertising rules |
| Cosmetics | FDA Cosmetic vs. Drug distinction, FTC | EC 1223/2009, EFSA (if health claim) | UK Cosmetics Regulation, ASA | ASEAN Cosmetic Directive (ACD) |
| Fashion | FTC Green Guides (sustainability claims) | EU Green Claims Directive, EU Textile Labeling Regulation | CMA Green Claims Code | Regional consumer protection laws |

### Step 2 — Build Forbidden Claims List

Based on the selected frameworks, identify specific claim types to prohibit. Apply these universal rules plus industry-specific rules:

**Universal Forbidden Patterns:**
- Any claim that the product "cures," "treats," "prevents," or "diagnoses" a disease (unless product is an approved drug/device)
- Unsubstantiated superlatives: "the most effective," "the best," "the only" — unless supported by comparative study
- False origin or ingredient claims
- Before/after claims without disclosure of typical results
- Celebrity/influencer endorsements without "#ad" or equivalent disclosure

**Healthcare-Specific Forbidden Patterns (US FDA):**
- "Clinically proven to cure/treat [disease name]"
- "[Product] is FDA approved" (unless it genuinely is)
- "Guaranteed results"
- Disease name in the same sentence as the product without approved claim language

**Cosmetics-Specific Forbidden Patterns (EU EC 1223/2009):**
- "Rebuilds/regenerates skin cells" (implies drug-like mechanism)
- "Heals/treats eczema/psoriasis/acne" (therapeutic claim)
- "Clinically proven" without stating the study design, n, and result
- "Anti-aging" presented as treating a disease rather than appearance improvement

**Fashion-Specific Forbidden Patterns (FTC Green Guides / EU Green Claims):**
- "100% eco-friendly" / "fully sustainable" without third-party certification
- "Carbon neutral" without referencing a verified offset standard
- "Biodegradable" without specifying under what conditions

### Step 3 — Build Approved Language Guide

For each forbidden claim pattern identified, provide a safe alternative:

| Unsafe Claim | Safe Alternative | Framework Reference |
|-------------|-----------------|---------------------|
| "Treats acne" | "Helps reduce the appearance of blemishes" | FDA Cosmetic/Drug distinction |
| "Cures insomnia" | "Supports healthy sleep patterns" | FDA Structure/Function |
| "Prevents heart disease" | "Supports cardiovascular health" | FDA Structure/Function |
| "100% sustainable" | "Made with 80% recycled materials (GRS certified)" | FTC Green Guides |
| "Rebuilds collagen" | "Visibly improves skin firmness in 4 weeks" | EU EC 1223/2009 |
| "Clinically proven" | "Shown in a 12-week study (n=48) to visibly reduce fine lines" | EU Art. 20 substantiation |
| "FDA approved" | "Formulated in an FDA-registered facility" | If not actually approved |
| "Best on the market" | "Rated #1 by [named publication] in [year]" | FTC substantiation |

### Step 4 — Identify Disclosure Requirements

Based on the content type and jurisdiction, list required disclosures:

| Content Type | Disclosure Required |
|-------------|---------------------|
| Influencer/sponsored content (US) | "#ad," "#sponsored," or clear "Advertisement" label (FTC) |
| Testimonials claiming typical results | "Results may vary" or "typical results are [X]" (FTC) |
| Clinical study reference | Study design, n size, and result must be stated |
| Supplement structure/function claim (US) | "These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease." |
| Before/after imagery | Conditions under which achieved must be disclosed |
| Paid partnership (EU) | Clear "Paid partnership" or equivalent per national advertising codes |

### Step 5 — Assign Risk Level

Score risk based on:
- **High:** Content involves disease treatment claims, prescription drug promotion, child-directed health content, or the brief explicitly asks for claims that are likely to be illegal
- **Medium:** Content involves health benefits, supplement claims, "clinically tested" language, sustainability certifications, or before/after comparisons
- **Low:** Pure awareness/lifestyle content, fashion trend posts without sustainability claims, beauty tips without product efficacy claims

### Step 6 — Research for Jurisdiction-Specific Updates

If `compliance_jurisdiction` is non-US, run:
```
WebSearch: "[jurisdiction] cosmetic/healthcare advertising regulations 2024 2025"
```
Fetch any recent enforcement actions or guideline updates that affect the brief's industry.

### Step 7 — Output Compliance Package

Return the full compliance output JSON. Pass to `sub-content-generator` as an input constraint set.

## Quality Gate

- [ ] `applicable_frameworks` lists at least 1 framework per industry/jurisdiction combination
- [ ] `forbidden_claims` list has at least 3 entries for healthcare/cosmetics briefs
- [ ] `approved_language_guide` provides a safe alternative for every forbidden claim
- [ ] `risk_level` is assigned with a one-sentence rationale
- [ ] `disclosure_requirements` is populated (or explicitly set to "none" if not applicable)

## Tools

- WebSearch: "[jurisdiction] [industry] advertising regulations [current year]"
- WebFetch: FDA.gov, FTC.gov, EFSA, EC regulations
- Read: SECOND-KNOWLEDGE-BRAIN.md (Regulatory Framework Reference section)
