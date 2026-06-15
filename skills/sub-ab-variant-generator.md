---
name: sub-ab-variant-generator
description: Generate Variant B — a second content piece with a different angle, hook, or CTA — and produce an A/B comparison table for testing guidance
---

## Purpose

Every content deliverable from `marketing-content-writer` includes two testable variants. Variant B is not a minor edit of Variant A — it takes a meaningfully different approach: a different emotional angle, a different opening hook strategy, a different CTA mechanism, or a different sub-segment targeting. This sub-skill produces Variant B and a structured comparison table.

## Inputs

- Variant A (finalized, quality-reviewed content)
- Structured brief (audience, goal, platform, tone)
- Quality review notes from `sub-quality-reviewer` (to avoid Variant B repeating the same weaknesses)

## Outputs

- Variant B content (platform-formatted, Gate 3 + 4 compliant)
- A/B comparison table
- Recommended test metric and success definition

## Variant Divergence Strategies

Choose ONE primary divergence strategy for Variant B. The strategy must produce a meaningfully different piece, not a superficial variation.

### Strategy 1 — Angle Flip (Pain vs. Aspiration)

If Variant A leads with the problem/pain (PAS frame), Variant B leads with the aspirational outcome (BAB or StoryBrand).

| Variant A | Variant B |
|-----------|-----------|
| Leads with: "Are you struggling with..." | Leads with: "Imagine waking up to..." |
| Emotional register: empathetic-urgent | Emotional register: inspirational-aspirational |
| Psychological trigger: loss aversion | Psychological trigger: positive self-concept |

**Best for:** Healthcare supplements, cosmetics skin care, weight management content

### Strategy 2 — Hook Swap

Variant A uses one hook type; Variant B uses a structurally different hook type.

| Hook Type A | Hook Type B |
|-------------|-------------|
| Statistic opener | Question opener |
| Bold claim | Relatable story moment |
| Question | Counterintuitive statement |
| Fear-based hook | Humor or surprise |
| Identity affirmation | Social proof opener |

**Best for:** Instagram, TikTok, Email subject lines (highest impact on open/click rates)

### Strategy 3 — CTA Strategy Swap

Variant A uses a high-commitment CTA (buy now, book appointment); Variant B uses a low-commitment transitional CTA (learn more, take the quiz, download guide).

| Variant A CTA | Variant B CTA |
|---------------|---------------|
| "Shop Now" | "See how it works →" |
| "Book Your Consultation" | "Take our 2-minute skin quiz" |
| "Buy Now — 20% Off Today Only" | "Get our free ingredient guide" |

**Best for:** New audiences, high-consideration purchases, healthcare services

### Strategy 4 — Sub-Segment Targeting

Variant A targets the primary demographic; Variant B targets a secondary sub-segment with a different angle for the same product.

| Variant A Sub-Segment | Variant B Sub-Segment |
|-----------------------|----------------------|
| "Women 30–45 experiencing early aging signs" | "Women 25–30 looking to prevent aging before it starts" |
| "People with chronic sleep issues" | "Busy professionals who can't wind down" |
| "Sustainable fashion advocates" | "Fashion lovers discovering sustainable options for the first time" |

**Best for:** Broad audience products, platform remarketing, multi-campaign strategies

### Strategy 5 — Evidence Angle Swap

Variant A leads with scientific/clinical evidence; Variant B leads with social proof / community trust / transformation story.

| Variant A Evidence | Variant B Evidence |
|--------------------|-------------------|
| "In a 12-week clinical study (n=87)..." | "Over 12,000 customers have..." |
| "Dermatologist-formulated with 15% vitamin C" | "My skin literally transformed in 3 weeks" (with disclosure) |
| "Backed by peer-reviewed research" | "Our community's #1 rated product for 3 years running" |

**Best for:** Cosmetics, fashion, wellness products where peer social proof rivals scientific authority

---

## Step-by-Step Instructions

### Step 1 — Select Divergence Strategy

Based on the brief and Variant A, choose the strategy that:
1. Creates the most meaningful divergence from Variant A
2. Is appropriate for the platform (e.g., Strategy 5 works better on Instagram than LinkedIn)
3. Hasn't been tested recently if the user mentions prior testing

### Step 2 — Plan Variant B Structure

Before writing, state:
- Strategy: [name]
- Key difference from Variant A: [1 sentence]
- Target sub-segment (if Strategy 4): [describe]
- Opening hook type: [type]
- CTA type: [high-commitment / low-commitment / viral / engagement]

### Step 3 — Draft Variant B

Write Variant B using the same process as `sub-content-generator`:
1. Apply same framework structure OR alternate framework if Strategy 1 is used
2. Use same compliance constraints (same forbidden claims list)
3. Use same or different evidence citations (can use different citations for variety)
4. Apply same word count target
5. Apply same platform formatting (from `sub-platform-adapter` specs)

### Step 4 — Self-Check (Gates 3 & 4 for Variant B)

Run the same quality gates as Variant A:

**Gate 3:**
- [ ] Zero forbidden claims?
- [ ] All health/efficacy claims cited?
- [ ] Word count within ±10%?

**Gate 4:**
- [ ] Brand Voice ≥ 7?
- [ ] Compliance = Pass?
- [ ] Persuasion ≥ 7?

If any gate fails, revise Variant B before presenting.

### Step 5 — Produce A/B Comparison Table

```
A/B COMPARISON TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dimension               │ Variant A              │ Variant B
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Primary Angle           │ [angle A]              │ [angle B]
Opening Hook Type       │ [hook type A]          │ [hook type B]
Emotional Register      │ [empathetic/aspir/etc] │ [different register]
CTA Strategy            │ [high/low/viral/engage]│ [different CTA type]
Target Sub-Segment      │ [describe]             │ [describe]
Framework Used          │ [framework A]          │ [framework B or same]
Evidence Type           │ [clinical/social proof]│ [different type]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Scores
Brand Voice             │ [A score]/10           │ [B score]/10
Compliance              │ [Pass/Warn]            │ [Pass/Warn]
Persuasion              │ [A score]/10           │ [B score]/10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 6 — Recommend Test Metric and Hypothesis

Based on the divergence strategy, recommend:

| Strategy | Recommended Metric | Hypothesis |
|----------|-------------------|------------|
| Strategy 1 (Pain vs. Aspiration) | Engagement rate / CTR | Aspiration-led content may outperform pain-led for premium audiences |
| Strategy 2 (Hook Swap) | Scroll-stop rate / Open rate | [Hook type B] may better match [platform/audience] behavioral patterns |
| Strategy 3 (CTA Swap) | Conversion rate vs. lead magnet conversion | Low-commitment CTA may outperform for cold traffic |
| Strategy 4 (Sub-Segment) | Segment-specific CTR | [Sub-segment B] may have higher purchase intent for this product |
| Strategy 5 (Evidence Swap) | Trust signal click rate | Social proof may outperform clinical evidence for [platform] audience |

**Output format:**
```
RECOMMENDED A/B TEST
━━━━━━━━━━━━━━━━━━━━
Test Metric:     [specific metric name]
Platform KPI:    [platform-native metric, e.g., "TikTok completion rate"]
Test Duration:   [minimum 7 days / 500 impressions per variant]
Hypothesis:      [Variant B will [outperform/achieve X] because [reason]]
Success Definition: [Variant B achieves ≥[X]% improvement in [metric] vs. Variant A]
━━━━━━━━━━━━━━━━━━━━
```

## Quality Gate

- [ ] Variant B uses a meaningfully different divergence strategy (not just a word swap)
- [ ] Variant B passes Gates 3 and 4 independently
- [ ] A/B comparison table is complete with all 8 dimension rows
- [ ] Test metric, hypothesis, and success definition are stated

## Tools

- Read: Brief, Variant A, SECOND-KNOWLEDGE-BRAIN.md
- No WebSearch required
