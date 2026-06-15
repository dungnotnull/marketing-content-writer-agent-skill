---
name: sub-content-generator
description: Generate evidence-backed Variant A content using the selected copywriting framework, compliance constraints, and research evidence
---

## Purpose

Draft the primary content piece (Variant A) by executing the selected copywriting framework structure, injecting evidence citations for all health/efficacy claims, and respecting all compliance constraints from `sub-compliance-checker`.

## Inputs

- Structured brief (from `sub-brief-intake`)
- Compliance constraint package (from `sub-compliance-checker`)
- Framework selection (from `sub-framework-selector`)
- Research findings: evidence citations, trend insights (from Stage 3 research)

## Outputs

- Full draft content (Variant A) with:
  - Inline evidence citation markers
  - Framework stage labels (internal, not visible in final output)
  - Word count
  - Compliance self-check result (Gate 3)

## Step-by-Step Instructions

### Step 1 — Load Framework Template

Based on the selected primary framework, apply the following template structure:

#### AIDA Template
```
[ATTENTION] — Opening line that stops the scroll / grabs attention
  → Strongest possible hook: statistic, question, bold statement, or visual metaphor
  → Must NOT be a forbidden claim

[INTEREST] — Build curiosity and relevance
  → Show the audience you understand their world
  → Introduce the product category (not yet the product)
  → Evidence point if available: "[statistic]% of [audience] experience [problem]"

[DESIRE] — Make them want the outcome
  → Describe the transformation / result / benefit
  → Use evidence-backed claim with approved language
  → Social proof (if available) with proper disclosure

[ACTION] — Clear, single CTA
  → Compliant CTA language
  → Platform-appropriate format (link in bio, swipe, shop now, etc.)
```

#### PAS Template
```
[PROBLEM] — State the specific pain point
  → Name the problem in the audience's own language
  → Be specific: not "tired" but "lying awake at 2am running through tomorrow's to-do list"

[AGITATE] — Deepen the emotional weight of the problem
  → Consequences of not solving it
  → Emotional cost (frustration, embarrassment, missed opportunity)
  → No exaggeration — stay truthful

[SOLUTION] — Present the product as the resolution
  → Use approved language for any efficacy claim
  → Cite supporting evidence [Tier X citation]
  → Bridge problem directly to product benefit

[CTA] — Action instruction
```

#### FAB Template
```
[FEATURE] — What the product has/does
  → State the feature factually
  → Technical accuracy required

[ADVANTAGE] — Why that feature is better / different
  → What makes this feature notable vs. alternatives?
  → Comparative claims require substantiation

[BENEFIT] — How the feature improves the customer's life
  → Translate the advantage into lived experience
  → Use sensory language where applicable
  → Evidence citation if claim is health/efficacy-related [Tier X]
```

#### StoryBrand (SB7) Template
```
[CHARACTER] — The hero (the customer, not the brand)
  → Name their identity, desire, and current frustration

[PROBLEM] — External problem + internal emotional problem + philosophical problem
  → External: the practical issue
  → Internal: how it makes them feel
  → Philosophical: why it's wrong/unfair

[GUIDE] — The brand appears as the guide (empathy + authority)
  → "We understand [internal problem]" → empathy
  → "[Brand credential]" → authority

[PLAN] — 3-step simple plan to solve the problem

[CTA] — Direct CTA + Transitional CTA (lower commitment)

[AVOID FAILURE] — What happens if they don't act
  → Compliance check: no fear-based health claims that cross the line

[SUCCESS] — Vision of success with the product
  → Use transformation language, not cure/treatment language
```

#### HSO Template (Hook–Story–Offer)
```
[HOOK] — Pattern interrupt in first 1–3 seconds/lines
  → Question, bold claim, shocking stat, relatable moment, strong visual descriptor
  → Must be truthful and compliant

[STORY] — Relatable narrative
  → First or third person; specific and sensory
  → The "before" state of your audience character

[OFFER] — The product introduction as the resolution to the story
  → Natural, not forced product placement
  → Evidence-backed claim with approved language
  → CTA integrated into the story's natural conclusion
```

### Step 2 — Inject Evidence Citations

For every health, efficacy, or performance claim in the draft:

1. Flag the claim: `[CLAIM: "X reduces Y"]`
2. Find the supporting evidence (from Stage 3 research)
3. Insert citation: `[Evidence: Tier 2 RCT — Smith et al., 2022, n=120, Journal of Dermatology, DOI: x.x/xxxxx]`
4. Verify the claim language matches what the evidence actually shows (no claim inflation)
5. Apply approved language guide from compliance package if raw claim language is borderline

### Step 3 — Calibrate Word Count

Target: within ±10% of `word_count_target` from the brief.

| If Over Target | Trim Priority |
|----------------|---------------|
| Remove adjective clusters | Keep the most specific adjective, remove generic ones |
| Shorten agitate/interest section | Keep one pain amplifier, remove redundant ones |
| Simplify CTA | One action, not three |

| If Under Target | Expand Priority |
|-----------------|----------------|
| Add evidence block | One supporting statistic or study finding |
| Deepen the audience empathy | Add a specific sensory detail to the problem statement |
| Add social proof sentence | With required disclosure |

### Step 4 — Apply Compliance Constraints

Before finalizing the draft, run through the forbidden claims list from `sub-compliance-checker`:

```
FOR EACH sentence in draft:
  CHECK if any word/phrase matches forbidden_claims list
  IF match found:
    REPLACE with approved_language_guide alternative
    LOG: "[claim removed/replaced: original → replacement]"
```

### Step 5 — Gate 3 Self-Check

Before passing to `sub-platform-adapter`, run Gate 3:

- [ ] Zero forbidden claims remaining in the draft?
- [ ] Every health/efficacy claim has a Tier 1–4 citation?
- [ ] Word count is within ±10% of target?
- [ ] All required disclosures are present (e.g., FDA disclaimer for supplement content)?

If any check fails, resolve it before proceeding.

### Step 6 — Output Variant A Draft

Output the complete draft with:
- Final content text (clean, no framework labels visible)
- Internal annotation block:
  ```
  [INTERNAL] Framework: [name] | Word Count: [n] | Gate 3: PASS | Claims Checked: [n]
  ```
- Evidence citation list (to be included in the final deliverable's "Evidence Base" table)

## Quality Gate

- [ ] Framework structure is fully executed (all stages present)
- [ ] No forbidden claim pattern present
- [ ] Every efficacy/health claim is cited at Tier 1–4
- [ ] Word count within ±10% of target
- [ ] All legally required disclosures are included in the draft

## Tools

- Read: SECOND-KNOWLEDGE-BRAIN.md (framework templates, regulatory language)
- WebSearch: (used in Stage 3, not in this sub-skill — evidence already compiled)
