---
name: sub-brief-intake
description: Parse and validate a content brief for marketing-content-writer — extracts all 8 required fields and asks targeted clarifying questions for any missing data
---

## Purpose

Extract a complete, structured content brief from the user's initial request. This sub-skill ensures all downstream stages have the information they need before any research, compliance checking, or content generation begins.

## Inputs

- Raw user request (natural language description of the content need)
- Any brand guidelines or style notes provided by the user
- Any prior context from the conversation

## Outputs

Structured brief JSON:
```json
{
  "industry": "healthcare | cosmetics | fashion | hybrid",
  "product_or_service": "string",
  "target_audience": {
    "demographics": "string",
    "psychographics": "string",
    "pain_points": ["string"],
    "desires": ["string"]
  },
  "platform": "Instagram | TikTok | Email | Blog | Landing Page | LinkedIn | YouTube | Print | Product Description",
  "goal": "awareness | engagement | conversion | retention | education",
  "tone": "professional | conversational | inspirational | authoritative | playful | empathetic",
  "word_count_target": "number",
  "compliance_jurisdiction": "US | EU | UK | ASEAN | global",
  "brand_constraints": ["string"],
  "additional_notes": "string"
}
```

## Step-by-Step Instructions

### Step 1 — Parse the Raw Request

Read the user's message and attempt to extract each of the 8 required fields:

| Field | Auto-Detection Signals |
|-------|----------------------|
| `industry` | Keywords: "supplement," "clinic," "serum," "skincare," "fashion," "clothing," "wellness," "medical," "beauty," "apparel" |
| `product_or_service` | Usually the noun being marketed — the product name or category |
| `target_audience` | Age ranges, gender mentions, lifestyle descriptors, pain points stated |
| `platform` | "Instagram," "TikTok," "email," "blog," "landing page," "product page," "LinkedIn" |
| `goal` | "sell," "convert" → conversion; "educate," "explain" → education; "reach," "awareness" → awareness |
| `tone` | Brand adjectives: "professional," "friendly," "bold," "scientific," "warm," "luxurious" |
| `word_count_target` | If stated explicitly; otherwise derive from platform default (see Platform Defaults table) |
| `compliance_jurisdiction` | Country/region mentions; if absent, default to "US" |

### Step 2 — Platform Defaults Table

If word_count_target is not stated, use these defaults:

| Platform | Default Word Count |
|----------|-------------------|
| Instagram Feed Post | 150 words (caption) |
| Instagram Story | 15 words (on-screen text) |
| TikTok Script | 200 words (60-second voiceover) |
| Email (subject + body) | Subject: 7–9 words; Body: 200 words |
| Blog Post | 1,500 words |
| Landing Page (hero section) | 300 words |
| Landing Page (full) | 800 words |
| LinkedIn Post | 150 words |
| YouTube Description | 200 words |
| Product Description (short) | 100 words |
| Product Description (long) | 250 words |
| Print Ad | 75 words |

### Step 3 — Identify Missing Fields

For each field not confidently detected, prepare a targeted clarifying question.

### Step 4 — Ask Clarifying Questions (if needed)

If any required fields are missing or ambiguous, present a numbered list of clarifying questions. Do not ask more than 4 questions at once. Example:

> To write the best content for you, I need a few details:
> 1. **Target audience:** Who is this for? (e.g., "women 25–35 interested in clean beauty" or "fitness enthusiasts with joint pain")
> 2. **Platform:** Where will this content be published? (Instagram, TikTok, email, blog, etc.)
> 3. **Goal:** What action do you want the reader to take? (buy, sign up, learn more, share)
> 4. **Compliance jurisdiction:** Is this for the US market, EU, or another region?

### Step 5 — Validate and Confirm

Once all 8 fields are populated, echo the structured brief back to the user in a clean summary and ask for confirmation:

> **Content Brief Summary:**
> - Industry: [value]
> - Product: [value]
> - Audience: [value]
> - Platform: [value]
> - Goal: [value]
> - Tone: [value]
> - Word Count: ~[value]
> - Jurisdiction: [value]
>
> Ready to proceed? Or would you like to adjust anything?

### Step 6 — Output Structured Brief

Once confirmed, output the structured brief JSON for use by subsequent stages.

## Quality Gate

- [ ] All 8 required fields are populated with non-null, specific values
- [ ] `industry` is one of: healthcare, cosmetics, fashion, hybrid
- [ ] `platform` is a recognized platform name
- [ ] `word_count_target` is a numeric value (derived or stated)
- [ ] `compliance_jurisdiction` is set (default: US)

**Do not pass to sub-compliance-checker until all gates pass.**

## Tools

- None (conversational only)
- Read: SECOND-KNOWLEDGE-BRAIN.md (Platform Defaults reference)
