---
name: sub-framework-selector
description: Select the optimal copywriting framework(s) based on content brief context — matches goal, platform, audience, and industry to AIDA, PAS, FAB, StoryBrand, or other frameworks
---

## Purpose

Choose the primary copywriting framework (and optional secondary framework) that best fits the content brief. The selection is evidence-based, drawing on audience psychology, platform behavior patterns, and industry-specific conversion research.

## Inputs

- Structured brief (goal, platform, audience, industry, tone, word_count_target)
- Knowledge from SECOND-KNOWLEDGE-BRAIN.md (framework reference)

## Outputs

```json
{
  "primary_framework": "AIDA | PAS | FAB | StoryBrand | PASTOR | BAB | ACCA | QUEST | HSO | 4Ps",
  "secondary_framework": "string | null",
  "primary_justification": "string",
  "secondary_justification": "string | null",
  "framework_structure": ["Stage 1", "Stage 2", "..."],
  "key_psychological_principle": "string"
}
```

## Framework Selection Matrix

Use this matrix as the primary decision tool. Match the brief's dominant characteristics to the recommended framework:

### By Goal

| Goal | Primary Framework | Why |
|------|------------------|-----|
| Conversion (direct sale) | PAS or 4Ps | Problem-agitate-solution drives urgency; 4Ps uses bold promise + proof |
| Awareness (new product/brand) | AIDA or HSO | AIDA builds staged engagement; HSO pattern-interrupts in social feeds |
| Education (inform + build trust) | ACCA or StoryBrand | ACCA builds comprehension before CTA; SB7 positions brand as guide |
| Engagement (social interaction, shares) | BAB or HSO | Before-After-Bridge is shareable transformation content; HSO drives comments |
| Retention (existing customers) | StoryBrand or PASTOR | Narrative deepens relationship; PASTOR uses transformation stories |
| E-commerce product page | FAB | Features → Advantages → Benefits maps naturally to product listings |

### By Platform

| Platform | Recommended Framework | Notes |
|----------|----------------------|-------|
| Instagram Feed | AIDA or HSO | First line must serve as hook; AIDA is scroll-stopper |
| Instagram Story | BAB | Short → transformation story → CTA fits 3-frame story arc |
| TikTok | HSO | Hook (first 3 seconds critical) → Story → Offer |
| Email | 4Ps or PAS | Subject line = Promise/Problem; body = Picture/Agitate; CTA = Push/Solution |
| Blog Post | ACCA or StoryBrand | Long-form allows education arc; SB7 builds brand narrative |
| Landing Page | StoryBrand or PAS | SB7 for brand narrative LPs; PAS for product/problem LPs |
| LinkedIn | ACCA | Professional audience responds to education + conviction flow |
| Product Description | FAB | Direct, functional, benefit-led |
| YouTube Description | AIDA | Attention (search query match) → interest → CTA |
| Print Ad | 4Ps | Space-constrained; bold promise + visual + push |

### By Industry

| Industry | Recommended Framework | Why |
|----------|-----------------------|-----|
| Healthcare (supplements) | PAS or ACCA | Pain-driven purchase; compliance requires education-first approach |
| Healthcare (services/clinics) | StoryBrand | Trust is the primary purchase driver; narrative builds trust |
| Cosmetics (skincare) | PAS or FAB | Problem-solution for actives; FAB for product listings |
| Cosmetics (luxury/prestige) | QUEST or StoryBrand | QUEST pre-qualifies premium buyer; SB7 builds aspirational brand |
| Fashion (mass market) | AIDA or BAB | Speed + aspiration; transformation content drives engagement |
| Fashion (sustainable) | StoryBrand or ACCA | Values-alignment requires narrative; education builds conviction |

### By Tone

| Tone | Best Frameworks |
|------|----------------|
| Empathetic | PAS, StoryBrand |
| Authoritative / Scientific | ACCA, FAB |
| Inspirational | BAB, StoryBrand, PASTOR |
| Playful / Conversational | HSO, AIDA |
| Direct / Performance | 4Ps, PAS |
| Premium / Selective | QUEST, StoryBrand |

## Step-by-Step Instructions

### Step 1 — Score the Brief Against the Matrix

For each dimension (goal, platform, industry, tone), identify the top 1–2 recommended frameworks. Tally the recommendations.

### Step 2 — Select Primary Framework

The framework with the most hits across the 4 dimensions is the primary. If there's a tie, prefer the framework that matches the **goal** dimension (highest weight).

### Step 3 — Select Secondary Framework (Optional)

If word_count_target > 300 words OR the brief has a dual goal (e.g., educate + convert), select a secondary framework that complements the primary:
- PAS + FAB: Problem-solution with benefit-led product description
- StoryBrand + AIDA: Narrative brand section + conversion hook section
- ACCA + 4Ps: Education body + direct-response CTA block

### Step 4 — Define the Framework Structure

Map the framework's stages to the specific content piece. Example for PAS + Healthcare brief:

```
Framework: PAS (Problem–Agitate–Solution)
Structure:
  1. Problem: [state the audience's pain point]
  2. Agitate: [deepen the pain — consequences, emotions, costs of inaction]
  3. Solution: [introduce the product as the resolution]
  4. CTA: [clear, compliant call-to-action]
```

### Step 5 — State the Key Psychological Principle

Every framework is grounded in a psychological mechanism. Name it:

| Framework | Psychological Principle |
|-----------|------------------------|
| AIDA | Sequential attention processing; progressive commitment |
| PAS | Loss aversion; pain amplification drives motivation |
| FAB | Rational decision-making; concrete benefit clarity |
| StoryBrand | Narrative transportation; trust via guide-hero dynamic |
| BAB | Social comparison + aspirational self-concept |
| 4Ps | Direct response; cognitive loading reduction |
| HSO | Pattern interrupt; curiosity gap; reciprocity |
| ACCA | Health literacy model; comprehension before compliance |
| QUEST | Self-selection; exclusivity principle |
| PASTOR | Transformation arc; identity shift motivation |

## Quality Gate

- [ ] Primary framework selected and justified with reference to at least 2 brief dimensions
- [ ] Framework structure is mapped to the specific content piece (not generic)
- [ ] Key psychological principle is named and cited
- [ ] If word count > 300 words, secondary framework is considered

## Tools

- Read: SECOND-KNOWLEDGE-BRAIN.md (Analytical Frameworks section)
- No WebSearch required for this sub-skill
