---
name: sub-platform-adapter
description: Reformat content for the target platform — applies character limits, hashtag rules, CTA placement, visual cue notes, and platform-native language patterns
---

## Purpose

Transform the generic content draft into a platform-native piece. Every platform has unique conventions, reading patterns, and native language codes. This sub-skill ensures the content looks like it belongs on the platform, not like it was pasted from a document.

## Inputs

- Variant A draft (from `sub-content-generator`)
- `platform` field from the brief
- `goal` field from the brief (affects CTA placement)

## Outputs

- Platform-formatted content with:
  - Proper character count
  - Correct hashtag placement and quantity
  - CTA at optimal position
  - Visual cue notes (for image/video-first platforms)
  - Platform-native language annotations

## Platform Specifications & Formatting Rules

### Instagram Feed Post

| Element | Specification |
|---------|--------------|
| Caption length | Optimal: 138–150 chars visible (up to 2,200 chars total) |
| First line rule | Must hook without "see more" truncation (visible above the fold) |
| Hashtags | 3–5 focused hashtags; place at end or in first comment |
| CTA position | Second-to-last line before hashtags |
| Emoji usage | 1–3 emojis max if brand voice permits; line breaks between sections |
| Tagging | Tag relevant brand/partner if applicable |
| Visual cue note | Describe ideal image/graphic: [e.g., "close-up of product on minimalist background, warm tones"] |

**Formatting Template:**
```
[Hook line — must stand alone]

[Body — 2–4 short paragraphs, each ≤3 lines]

[Social proof / evidence line]

[CTA line]

[Hashtag block — 3-5 tags]
```

---

### Instagram Story

| Element | Specification |
|---------|--------------|
| On-screen text | Max 7–10 words per frame; large font |
| Frames | 3–5 frames for a complete story |
| CTA | "Link Sticker" or "Swipe Up" on final frame |
| Visual cue | Background image/video direction per frame |
| Tone | Casual, direct, first-person |

**Formatting Template:**
```
Frame 1: [Attention/Problem — 5 words max]
Frame 2: [Agitation/Story — 7 words max]
Frame 3: [Solution/Reveal — 7 words max]
Frame 4: [Evidence/Social proof — 1 sentence]
Frame 5: [CTA frame — "Shop Now" / "Learn More" / "Book Free Consult"]
Visual cues: [one sentence per frame describing the background or overlay]
```

---

### TikTok Script

| Element | Specification |
|---------|--------------|
| Video length | 15–60 seconds; script for 60s = ~200 words |
| First 3 seconds | CRITICAL — hook must prevent scroll. Question, bold statement, or visual surprise |
| Script structure | Hook (0–3s) → Story (3–30s) → Offer (30–50s) → CTA (50–60s) |
| Caption | 150–300 chars; include 1–3 relevant hashtags |
| On-screen text overlays | Note key moments for text overlay |
| CTA | "Comment [X] for [Y]" or "Follow for Part 2" or "Link in bio" |
| Tone | Conversational, direct-to-camera, energetic |

**Formatting Template:**
```
[HOOK — 0:00–0:03]
"[Opening line — question or bold statement]"
[Text overlay: "[3-word phrase]"]

[STORY — 0:03–0:30]
"[Relatable narrative — specific, sensory, first person or 'you' POV]"
[Note: cut/transition point at 0:15]

[OFFER — 0:30–0:50]
"[Introduce product naturally within story resolution]"
"[Evidence-backed benefit with approved language]"
[Text overlay: "[Key claim]"]

[CTA — 0:50–0:60]
"[Single action instruction]"
Caption: [150-char caption + 1-3 hashtags]
```

---

### Email (Subject + Body)

| Element | Specification |
|---------|--------------|
| Subject line | 7–9 words; A/B test with curiosity vs. benefit angle |
| Preview text | 40–90 chars; extend the subject line narrative |
| Body length | Healthcare/cosmetics: 150–250 words; fashion: 100–200 words |
| Paragraphs | Max 3 lines each; white space is required |
| CTA | Single button above the fold (within first scroll); text CTA at bottom |
| Tone | Personal, direct, conversational (even for professional brands) |
| Personalization | "[First name]" placeholder at opening |

**Formatting Template:**
```
Subject: [benefit or curiosity hook — 7-9 words]
Preview: [extend subject narrative — 40-90 chars]

Hi [First name],

[Opening hook — 1 sentence that mirrors the subject line]

[Problem/situation — 2–3 sentences]

[Solution/product reveal — 2–3 sentences; evidence claim if applicable]

[Social proof — 1 sentence with disclosure if needed]

[CTA Button: "[Action verb + outcome]"]

[Closing — 1 sentence]

[Sign-off]
[FDA disclaimer block if supplement content]
```

---

### Blog Post

| Element | Specification |
|---------|--------------|
| Length | 1,200–2,500 words; healthcare SEO = 1,500+ |
| Structure | H1 (title) → H2 sections → H3 subsections |
| Introduction | 150 words: hook → context → what reader will learn |
| Section length | Each H2 section: 200–350 words |
| Evidence integration | Inline citations (hyperlinked) for all health claims |
| Meta description | 150–160 chars; includes primary keyword |
| CTA | End of article + sidebar/inline offer if applicable |
| SEO | Primary keyword in H1, first 100 words, and 1–2 H2s |

---

### Landing Page

| Element | Specification |
|---------|--------------|
| Hero section | H1 (≤12 words) + subheading (≤25 words) + primary CTA button |
| Above the fold | Everything above scroll must communicate the core value proposition |
| Body sections | Feature/benefit sections; testimonials; social proof; FAQ |
| CTA | Primary (above fold) + secondary (bottom) |
| Word count | Hero: 50 words; full page: 600–1,000 words |
| Trust elements | Note where to place: certifications, media logos, clinical study references |

---

### Product Description (E-commerce)

| Element | Specification |
|---------|--------------|
| Short description | 75–100 words; scannable; top 3 benefits |
| Long description | 200–300 words; FAB structure |
| Bullet points | 3–5 bullets; each = one benefit (not feature alone) |
| Compliance | All ingredient claims must use approved language |
| SEO | Include primary product keyword naturally |

---

### LinkedIn Post

| Element | Specification |
|---------|--------------|
| Length | 150–300 chars (short) or 1,300–2,000 chars (long-form) |
| First line | Hook that works as standalone message; truncated after 2 lines |
| Tone | Professional but human; first-person perspective |
| Hashtags | 3–5 at end |
| CTA | Invite comment or share; link in first comment (not body) |

---

## Step-by-Step Instructions

### Step 1 — Identify the Target Platform

Read the `platform` field from the brief. Select the matching specification above.

### Step 2 — Reformat Content to Platform Template

Apply the formatting template for the target platform:
1. Restructure paragraphs to match platform reading pattern
2. Trim or expand to meet character/word count
3. Rewrite opening line as a platform-native hook if needed
4. Add visual cue notes in `[brackets]`
5. Add or remove hashtags per platform convention

### Step 3 — Optimize CTA Placement

- Above-the-fold platforms (email, landing page, Instagram Story): CTA in first visible area
- Discovery platforms (TikTok, Instagram Feed): CTA at the end after value delivery
- Search platforms (Blog, YouTube): CTA at end + one inline mid-content

### Step 4 — Add Platform-Native Language Patterns

| Platform | Native Language Pattern |
|----------|------------------------|
| TikTok | "POV: you..." / "The way that..." / Direct-to-camera second person |
| Instagram | "Drop a ❤️ if..." / "Save this for later" / "DM me [X]" |
| Email | "Quick question for you," / "[First name], this is for you" |
| LinkedIn | "Here's what I've learned:" / "Most people don't know this:" |
| Blog | "In this guide, you'll discover..." / "Here's the research:" |

### Step 5 — Output Platform-Formatted Content

Output:
1. The fully formatted content piece
2. A formatting notes block:
   ```
   [FORMAT NOTES]
   Platform: [name]
   Character count: [n]
   Hashtags: [list]
   Visual cues: [descriptions]
   CTA placement: [position]
   ```

## Quality Gate

- [ ] Character/word count matches platform specification (±5%)
- [ ] CTA is at the optimal position for the platform
- [ ] Hashtag count follows platform convention
- [ ] Visual cue notes are present for image/video-first platforms
- [ ] Platform-native language patterns are used (at least 1 native pattern per piece)

## Tools

- Read: SECOND-KNOWLEDGE-BRAIN.md (Platform Performance Benchmarks)
- No WebSearch required
