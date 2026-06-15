# PROJECT-detail.md — Skill 9: marketing-content-writer

## Executive Summary

`marketing-content-writer` is a professional-grade Claude Code harness skill that generates compliant, evidence-backed marketing content for three regulated and trend-sensitive industries: **healthcare, cosmetics, and fashion**. It combines world-renowned copywriting frameworks (AIDA, PAS, FAB, StoryBrand) with regulatory pre-screening (FDA, EU Cosmetics Regulation, FTC), peer-reviewed evidence sourcing, platform-specific formatting, brand voice scoring, and A/B variant generation. The result is content that a senior marketing manager would be proud to publish — not generic AI output.

---

## Problem Statement

### Domain Context
Marketing content in healthcare, cosmetics, and fashion occupies a uniquely constrained space:
- **Healthcare**: Claims about efficacy, treatment, or diagnosis are regulated by FDA (US), EMA (EU), and regional bodies. Violating these rules risks legal liability and brand damage.
- **Cosmetics**: Claims like "anti-aging," "heals acne," or "regenerates skin cells" cross a legal line in many jurisdictions. The EU Cosmetics Regulation (EC 1223/2009) and FDA's distinction between cosmetics and drugs are both nuanced and frequently misunderstood by marketers.
- **Fashion**: While less regulated for claims, fashion marketing must navigate fast-changing trends, sustainability/greenwashing standards (EU Green Claims Directive), and cultural sensitivity landmines.

### The Gap
Generic content tools: (a) have no compliance awareness, (b) produce unsupported health claims, (c) apply the same tone and format regardless of platform or industry, and (d) ignore current research and trend data. This skill fills that gap with a structured, evidence-first, compliance-first workflow.

---

## Target Users & Use Cases

| User | Trigger | Skill Response |
|------|---------|----------------|
| Healthcare brand marketing manager | "Write a social post about our new probiotic supplement for gut health" | Intake → compliance screen (supplement vs. drug claims) → evidence search → framework-based draft → Instagram-formatted Variant A + Variant B |
| Cosmetics startup founder | "Write a landing page for our vitamin C serum targeting 25-35 year old women" | Intake → EU/FDA cosmetic claim compliance → PubMed evidence on vitamin C efficacy → StoryBrand framework landing page → quality score |
| Fashion brand content strategist | "Create a TikTok script for our new sustainable denim collection" | Intake → EU Green Claims compliance check → trend research → AIDA TikTok script format → A/B hook variants |
| Medical clinic marketing team | "Write an email campaign for our new weight management program" | Intake → FDA advertising compliance for medical services → research on email persuasion → FAB email framework → 2 subject line + body variants |
| Cosmetics e-commerce manager | "Write product descriptions for 3 new skincare SKUs" | Brief intake → compliance check per SKU → ingredient evidence lookup → FAB product description × 3 |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    /marketing-content-writer (main.md)                  │
└────────────────────────┬────────────────────────────────────────────────┘
                         │
         ┌───────────────▼──────────────┐
         │  Stage 1: sub-brief-intake   │
         │  → industry, product,        │
         │    audience, platform,       │
         │    goals, tone, constraints  │
         └───────────────┬──────────────┘
                         │
         ┌───────────────▼──────────────────┐
         │  Stage 2: sub-compliance-checker  │
         │  → FDA / EU / FTC / regional      │
         │    constraint mapping             │
         │  → forbidden claims list          │
         │  → approved language guide        │
         └───────────────┬──────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 3: Knowledge Research          │
         │  → WebSearch: trend data,             │
         │    competitor content, search intent  │
         │  → SECOND-KNOWLEDGE-BRAIN lookup      │
         │  → PubMed / industry source fetch     │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 4: sub-framework-selector      │
         │  → match brief to AIDA/PAS/FAB/       │
         │    StoryBrand/4Ps/PASTOR framework    │
         │  → justify selection                  │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 5: sub-content-generator       │
         │  → Draft Variant A                    │
         │  → embed evidence citations           │
         │  → comply with constraint list        │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 6: sub-platform-adapter        │
         │  → reformat for target platform       │
         │  → apply word count, hashtags,        │
         │    CTA placement, visual cue notes    │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 7: sub-quality-reviewer        │
         │  → brand voice score (1-10)           │
         │  → compliance re-check                │
         │  → readability score (Flesch)         │
         │  → persuasion score (1-10)            │
         │  → improvement notes                  │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 8: sub-ab-variant-generator    │
         │  → Variant B: alternate angle or CTA  │
         │  → head-to-head comparison table      │
         └───────────────┬──────────────────────┘
                         │
         ┌───────────────▼──────────────────────┐
         │  Stage 9: Final Synthesis             │
         │  → structured deliverable             │
         │  → both variants + quality scores     │
         │  → compliance certification note      │
         │  → evidence citations                 │
         └───────────────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### sub-brief-intake.md
- **Purpose:** Parse the user's content request into a structured brief
- **Inputs:** Raw user message (product/service description, target audience, platform, goal, brand notes)
- **Outputs:** Structured JSON-like brief: `{industry, product, audience, platform, goal, tone, word_count_target, brand_constraints, compliance_jurisdiction}`
- **Tools:** Read (CLAUDE.md context), conversational clarification questions
- **Quality Gate:** All 8 brief fields populated before proceeding

### sub-compliance-checker.md
- **Purpose:** Screen the brief against relevant regulatory frameworks
- **Inputs:** Structured brief from sub-brief-intake
- **Outputs:** `{jurisdiction, forbidden_claims[], approved_language_guide[], disclosure_requirements[], risk_level: low/medium/high}`
- **Tools:** WebSearch (FDA guidance, EU regs), WebFetch (regulatory documents), SECOND-KNOWLEDGE-BRAIN
- **Quality Gate:** Risk level assessed; high-risk content flagged for human legal review

### sub-framework-selector.md
- **Purpose:** Select the optimal copywriting framework(s) for the brief
- **Inputs:** Structured brief, platform, goal
- **Outputs:** Primary framework + secondary framework + justification
- **Frameworks Available:** AIDA, PAS, FAB, StoryBrand (SB7), 4Ps, PASTOR, ACCA, Before-After-Bridge, QUEST, The Hook-Story-Offer
- **Quality Gate:** Framework justification references audience psychology and conversion goals

### sub-content-generator.md
- **Purpose:** Draft Variant A using selected framework and evidence
- **Inputs:** Brief, compliance constraints, framework selection, research findings
- **Outputs:** Full draft content piece with evidence citations inline
- **Tools:** WebSearch (supporting statistics), SECOND-KNOWLEDGE-BRAIN
- **Quality Gate:** Zero forbidden claims; all health/efficacy claims cited; word count within ±10% of target

### sub-platform-adapter.md
- **Purpose:** Reformat content for the specific target platform
- **Inputs:** Draft content, platform name
- **Outputs:** Platform-optimized version with formatting notes
- **Platforms:** Instagram post, Instagram Story, TikTok script, YouTube description, Blog post, Email (subject + body), Landing page, Product description, LinkedIn post, Print ad
- **Quality Gate:** Format matches platform conventions (character limits, hashtag count, CTA placement)

### sub-quality-reviewer.md
- **Purpose:** Score the content and generate improvement notes
- **Inputs:** Platform-adapted content draft, brief, compliance constraints
- **Outputs:** Quality scorecard + revision notes
- **Scoring Dimensions:**
  - Brand Voice Consistency: 1–10
  - Regulatory Compliance: Pass / Warn / Fail
  - Readability (Flesch-Kincaid grade): target 6–9 for consumer content
  - Persuasion Score: 1–10 (AIDA stage completion, emotional hook strength)
  - SEO Alignment (if applicable): keyword density, meta signals
- **Quality Gate:** Compliance = Pass; Brand Voice ≥ 7; Persuasion ≥ 7

### sub-ab-variant-generator.md
- **Purpose:** Generate a second content variant with a different angle, hook, or CTA
- **Inputs:** Variant A, brief, quality review notes
- **Outputs:** Variant B content + comparison table (A vs B: angle, hook, CTA, target sub-segment)
- **Quality Gate:** Variant B passes same compliance and quality gates as Variant A

---

## Skill File Format Specification

```yaml
---
name: marketing-content-writer
description: Generate compliant, evidence-backed marketing content for healthcare, cosmetics, and fashion with A/B variants and platform adaptation
---
```

Required sections in main.md:
- `## Role & Persona`
- `## Workflow (Harness Flow)` — numbered steps with sub-skill invocations
- `## Sub-skills Available`
- `## Tools`
- `## Output Format`
- `## Quality Gates`

---

## E2E Execution Flow

```
1. User invokes /marketing-content-writer
2. Harness presents intake prompt (or processes inline brief if provided)
3. sub-brief-intake → structured brief JSON
4. [GATE 1] All 8 brief fields populated?
   - No → ask clarifying questions
   - Yes → proceed
5. sub-compliance-checker → constraint map
6. [GATE 2] Risk level = High?
   - Yes → warn user, flag for legal review, offer to proceed with conservative language
   - No → proceed
7. Knowledge Research:
   a. WebSearch: "[industry] [product] [audience] marketing trends 2025"
   b. WebSearch: "[key ingredient/claim] clinical evidence"
   c. SECOND-KNOWLEDGE-BRAIN lookup for domain knowledge
8. sub-framework-selector → primary + secondary framework
9. sub-content-generator → Variant A draft
10. [GATE 3] Zero forbidden claims? All citations present? Word count OK?
    - No → revise draft
    - Yes → proceed
11. sub-platform-adapter → formatted Variant A
12. sub-quality-reviewer → scorecard
13. [GATE 4] Compliance = Pass AND Brand Voice ≥ 7 AND Persuasion ≥ 7?
    - No → revise per improvement notes, re-score
    - Yes → proceed
14. sub-ab-variant-generator → Variant B + comparison table
15. Final synthesis → structured deliverable
```

---

## SECOND-KNOWLEDGE-BRAIN Integration

- **Sources:** PubMed, FDA.gov, EFSA, Cosmetics Europe, Journal of Advertising Research, Journal of Consumer Psychology, Content Marketing Institute, Vogue Business, Business of Fashion, WWD
- **Crawl Config:** `tools/knowledge_updater.py` — weekly schedule
- **Append Format:** `## [YYYY-MM-DD] [Source] — [Title]` with relevance note and key finding summary
- **Knowledge Categories:**
  - Copywriting Frameworks
  - Regulatory Updates (FDA, EU, FTC, ASEAN)
  - Cosmetic Ingredient Research
  - Healthcare Advertising Rules
  - Fashion Trend Intelligence
  - Consumer Psychology Research
  - Platform Algorithm Changes

---

## Quality Gates Definition

| Gate | Condition | Action if Failed |
|------|-----------|-----------------|
| Gate 1 | All brief fields populated | Ask user for missing fields |
| Gate 2 | Compliance risk ≤ Medium | Warn user + offer conservative language track |
| Gate 3 | Zero forbidden claims + all citations present | Revise draft automatically |
| Gate 4 | Brand Voice ≥ 7, Persuasion ≥ 7, Compliance = Pass | Apply improvement notes and re-score |
| Gate 5 | Variant B passes Gates 3 & 4 | Regenerate with alternate angle |

---

## Test Scenarios

See `tests/test-scenarios.md` for 7 detailed scenario tests covering:
1. Healthcare supplement social post (FDA risk)
2. Cosmetics landing page (EU claims compliance)
3. Fashion TikTok script (sustainability/greenwashing)
4. Medical clinic email campaign
5. Skincare product descriptions (×3 SKUs)
6. Fashion brand Instagram story sequence
7. Healthcare blog post with high-risk claim attempt

---

## Key Design Decisions

1. **Compliance before content** — Regulatory screening always precedes content generation. This prevents generating illegal claims that then need to be removed, which degrades output quality.
2. **Evidence hierarchy enforced** — All health/efficacy claims must cite Systematic Review > RCT > Cohort Study tier evidence. Expert opinion and brand claims without backing are flagged.
3. **Platform-aware formatting** — Content is never generic. Every output specifies the platform (TikTok, Instagram, email, etc.) and is formatted accordingly with native conventions.
4. **A/B as default** — Two variants are always produced. This is non-negotiable — single-variant content cannot be tested and optimized.
5. **Brand voice scoring** — The quality reviewer scores brand voice consistency using submitted brand notes, ensuring content doesn't drift toward generic AI tone.
6. **Graceful degradation** — If WebSearch/WebFetch are unavailable, skill falls back to SECOND-KNOWLEDGE-BRAIN and signals the limitation explicitly. Content is still produced but marked as "research-limited."
7. **Conservative language track** — When compliance risk is High, the skill offers a conservative language alternative rather than refusing to generate content.
8. **Three-industry knowledge segmentation** — SECOND-KNOWLEDGE-BRAIN is segmented into Healthcare, Cosmetics, and Fashion knowledge zones so research queries are pre-scoped.
