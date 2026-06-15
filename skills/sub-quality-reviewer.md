---
name: sub-quality-reviewer
description: Score content across 5 quality dimensions — brand voice, compliance, readability, persuasion, and SEO — and generate actionable improvement notes
---

## Purpose

Evaluate the platform-adapted content draft against 5 quantitative quality dimensions. Produce a scored quality card and specific improvement notes. If any dimension falls below its pass threshold, provide targeted revision instructions before the content advances to the A/B variant stage.

## Inputs

- Platform-formatted content (from `sub-platform-adapter`)
- Structured brief (for brand tone, audience, goal comparison)
- Compliance constraint package (for re-check)

## Outputs

```json
{
  "brand_voice_score": 0-10,
  "compliance_status": "Pass | Warn | Fail",
  "readability_grade": 1-16,
  "persuasion_score": 0-10,
  "seo_score": 0-10,
  "overall_gate": "PASS | FAIL",
  "improvement_notes": ["string"],
  "revised_sections": {"section_name": "revised_text"}
}
```

## Scoring Dimensions

### Dimension 1 — Brand Voice Consistency (1–10)

Score based on alignment with the brief's specified tone and any brand constraints:

| Score | Criteria |
|-------|----------|
| 9–10 | Tone perfectly matches brief; vocabulary matches brand constraints; no off-brand phrases; sentence rhythm is consistent throughout |
| 7–8 | Tone largely matches; 1–2 phrases slightly off-register; vocabulary mostly on-brand |
| 5–6 | Tone drifts in ≥2 sections; some generic AI-sounding phrases present; register inconsistency |
| 3–4 | Tone significantly misaligned with brief; sounds like generic content |
| 1–2 | Tone entirely wrong for the brand; would require a full rewrite |

**Evaluation Signals:**
- **Formal vs. casual:** Count contractions (it's, you're = casual; it is, you are = formal)
- **Vocabulary register:** Are adjectives aspirational or clinical or playful — per brief tone?
- **Sentence length:** Premium/authoritative brands use longer, complex sentences; playful/Gen Z brands use very short punchy lines
- **Unique brand promise:** Is the brand's core differentiator present in the copy?
- **Off-brand phrases:** Generic phrases like "world-class," "best-in-class," "cutting-edge" without specificity signal drift

### Dimension 2 — Regulatory Compliance (Pass / Warn / Fail)

Re-run the forbidden claims check against the compliance package:

| Status | Criteria |
|--------|----------|
| Pass | Zero forbidden claims; all disclosures present; no borderline language |
| Warn | 1 borderline claim that should be softened; disclosure missing but not legally required |
| Fail | ≥1 forbidden claim present; required disclosure missing; risk level escalates |

**Check sequence:**
1. Scan every sentence against `forbidden_claims` list
2. Verify required disclosures are present (FDA disclaimer, FTC disclosure, etc.)
3. Verify any "clinically proven/tested" claims include: study design, n, result, and citation
4. Verify sustainability claims (fashion) reference a specific certification

### Dimension 3 — Readability (Flesch-Kincaid Grade Level)

Estimate the Flesch-Kincaid grade level by analyzing:
- Average words per sentence
- Average syllables per word

| Grade | Interpretation | Target For |
|-------|---------------|-----------|
| 4–6 | Very easy | Consumer social media, TikTok, Instagram |
| 6–8 | Easy | Consumer email, product descriptions, landing pages |
| 8–10 | Fairly easy | Healthcare consumer blog, cosmetics landing page |
| 10–12 | Standard | B2B content, professional healthcare communications |
| 12+ | Difficult | Medical/scientific content for professionals |

**Target:** Grade 6–9 for consumer-facing content. Grade 8–12 for professional/B2B.

**Readability killers to flag:**
- Sentences > 25 words
- Passive voice ("is known to," "was found to") — convert to active where possible
- Jargon without explanation (flag for audience appropriateness)
- Noun stacking: "evidence-based clinical efficacy optimization" — break up

### Dimension 4 — Persuasion Score (1–10)

Evaluate persuasion effectiveness across 6 sub-criteria:

| Sub-criteria | Weight | 1–10 Scoring Signal |
|-------------|--------|---------------------|
| Hook Strength | 20% | Does the opening create genuine curiosity or emotional resonance? Does it stop the scroll? |
| Problem Clarity | 15% | Is the audience's pain or desire stated with specific, vivid language? |
| Desire / Outcome | 20% | Is the desired transformation described with specific, credible detail? |
| Evidence & Proof | 20% | Are claims substantiated with citations, numbers, or social proof? |
| CTA Clarity | 15% | Is there one clear action? Is it compelling? Is it frictionless? |
| Emotional Resonance | 10% | Does the content connect to the audience's deeper identity/values? |

**Composite formula:** Weighted average of 6 sub-criteria.

**Common persuasion deficits:**
- Opening is generic ("Are you tired of X?") — too predictable; score -2 on Hook
- Benefits stated without specificity ("feel better" vs. "fall asleep in under 20 minutes") — score -2 on Desire
- CTA is passive ("learn more") for a conversion goal — score -2 on CTA Clarity
- No social proof for a trust-critical industry (healthcare, cosmetics) — score -2 on Evidence

### Dimension 5 — SEO Alignment (1–10, applicable for Blog/Landing Page only)

Only score this dimension if `platform` = Blog Post, Landing Page, or YouTube Description.

| Sub-criteria | Signal |
|-------------|--------|
| Primary keyword in H1/headline | Present / Absent |
| Primary keyword in first 100 words | Present / Absent |
| Secondary keywords / LSI terms | ≥3 natural mentions |
| Meta description (150–160 chars) | Present / Within length |
| Internal/external link opportunities | Noted in content |
| Readability alignment with search intent | Educational/informational/commercial |

Score 0–10 based on % criteria met.

---

## Step-by-Step Instructions

### Step 1 — Score All 5 Dimensions

Work through each dimension systematically. Calculate the score for each.

### Step 2 — Gate 4 Check

| Dimension | Pass Threshold |
|-----------|---------------|
| Brand Voice | ≥ 7 |
| Compliance | Pass |
| Readability | Grade 6–12 (within target range) |
| Persuasion | ≥ 7 |
| SEO | ≥ 6 (only if applicable) |

**If all dimensions pass → `overall_gate: PASS`**
**If any dimension fails → `overall_gate: FAIL` → generate improvement notes**

### Step 3 — Generate Improvement Notes

For each failed dimension, generate a specific, actionable instruction (not a general suggestion):

**Format for improvement notes:**
```
[Dimension]: [Score] → [Target]
Issue: [1 sentence describing the specific problem]
Fix: [Exact instruction — what to change and how]
Example: [Show the problem text] → [Show the improved version]
```

Example:
```
[Brand Voice]: 5/10 → 7/10
Issue: The opening paragraph uses passive voice and formal language inconsistent with the "conversational + playful" tone in the brief.
Fix: Rewrite first 2 sentences in second person, active voice, with a casual contraction.
Example: "Vitamin C has been shown to improve skin radiance" → "Your skin is literally begging for vitamin C — and here's what the science says."
```

### Step 4 — Apply Revisions (Auto-Revise)

For each improvement note, apply the revision to the content draft. Do not ask the user for permission to apply auto-revisions — this is an internal quality gate process.

After all revisions are applied, re-score the affected dimensions.

### Step 5 — Output Quality Scorecard

Present the final scored quality card (post-revision scores).

**Scorecard Template:**
```
QUALITY SCORECARD — Variant A
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brand Voice:     [score]/10  [PASS/FAIL]
Compliance:      [Pass/Warn/Fail]
Readability:     Grade [X]   [PASS/FAIL]
Persuasion:      [score]/10  [PASS/FAIL]
SEO Alignment:   [score]/10  [PASS/FAIL] (if applicable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gate 4 Status:   ✅ PASS / ❌ FAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Revisions applied: [n] sections revised]
```

## Quality Gate

- [ ] All 5 dimensions scored with numerical or categorical values
- [ ] Improvement notes generated for every dimension below pass threshold
- [ ] Auto-revisions applied before presenting final score
- [ ] Final Gate 4 status is PASS before advancing to `sub-ab-variant-generator`

## Tools

- Read: Brief (for brand tone comparison), SECOND-KNOWLEDGE-BRAIN.md (Brand Voice Dimensions)
- No WebSearch required
