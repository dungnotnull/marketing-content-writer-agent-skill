# CLAUDE.md — Skill 9: marketing-content-writer

## Skill Identity
- **Name:** marketing-content-writer
- **Tagline:** Evidence-backed marketing content for healthcare, cosmetics, and fashion — compliant, on-brand, and trend-aligned.
- **Current Phase: Phase 5 — Integration & Cross-Skill Wiring (COMPLETE)- **Cluster:** D — Content Creation

---

## Problem This Skill Solves

Marketing teams in healthcare, cosmetics, and fashion industries face a dual challenge: producing high-quality, persuasive content that drives conversion while remaining compliant with strict regulatory frameworks (FDA, EU Cosmetics Regulation, FTC guidelines). Generic AI content tools ignore compliance entirely, generate unsupported health claims, and produce copy that sounds identical across brands. This skill solves that by grounding every piece of content in:
1. Validated copywriting frameworks (AIDA, PAS, StoryBrand, FAB)
2. Regulatory compliance pre-screening for each industry and target market
3. Evidence-based claims linked to peer-reviewed research
4. Platform-specific format and tone adaptation
5. Brand voice consistency scoring
6. A/B variant generation for conversion optimization

---

## Harness Flow Summary

```
/marketing-content-writer invoked
  Stage 1: sub-brief-intake          → extract content brief, audience, goals, platform, industry
  Stage 2: sub-compliance-checker    → screen for regulatory constraints (FDA/EU/FTC/local)
  Stage 3: Knowledge Research        → WebSearch + SECOND-KNOWLEDGE-BRAIN for trend data & evidence
  Stage 4: sub-framework-selector    → select optimal copywriting framework(s) for brief
  Stage 5: sub-content-generator     → draft Variant A using selected framework + evidence
  Stage 6: sub-platform-adapter      → reformat/resize content for target platform
  Stage 7: sub-quality-reviewer      → brand voice scoring, compliance re-check, quality gate
  Stage 8: sub-ab-variant-generator  → generate Variant B (alternative angle/CTA)
  Stage 9: Main harness              → synthesize final deliverable with both variants
```

---

## Sub-Skills List

| File | Description |
|------|-------------|
| `skills/sub-brief-intake.md` | Intake and parse content brief: industry, product, audience, goals, platform, tone, constraints |
| `skills/sub-compliance-checker.md` | Screen content against FDA, EU Cosmetics Regulation, FTC, and regional advertising guidelines |
| `skills/sub-framework-selector.md` | Select optimal copywriting framework(s) based on brief context (AIDA, PAS, FAB, StoryBrand, etc.) |
| `skills/sub-content-generator.md` | Generate evidence-backed content draft using selected framework and research data |
| `skills/sub-platform-adapter.md` | Reformat content for target platform: Instagram, TikTok, blog, email, landing page, print |
| `skills/sub-quality-reviewer.md` | Score brand voice consistency, readability, compliance, persuasion, and generate improvement notes |
| `skills/sub-ab-variant-generator.md` | Generate an alternative content variant (different angle, CTA, or emotional hook) |

---

## Tools Required

- **WebSearch** — trend research, regulatory updates, competitor analysis
- **WebFetch** — authoritative source scraping (PubMed, FDA, EFSA, Vogue Business, WWD)
- **Read** — read SECOND-KNOWLEDGE-BRAIN.md, CLAUDE.md, sub-skill files
- **Write** — write final content output deliverable
- **Bash** — run `tools/knowledge_updater.py`

---

## Knowledge Sources

| Source | Type | Domain |
|--------|------|--------|
| PubMed / NCBI | Research papers | Healthcare marketing, cosmetic ingredients |
| FDA.gov | Regulatory | Healthcare advertising, cosmetic claims |
| EFSA / EMA | Regulatory | EU health claims, cosmetic regulations |
| FTC.gov | Regulatory | Endorsement guidelines, advertising standards |
| Cosmetics Europe | Industry | Cosmetic industry best practices |
| Journal of Consumer Psychology | Research | Consumer behavior, persuasion |
| Journal of Advertising Research | Research | Copywriting effectiveness |
| Vogue Business / WWD / Business of Fashion | Industry | Fashion marketing trends |
| Content Marketing Institute | Best practices | Content strategy frameworks |
| CopybloggerAcademy / Nielsen Norman Group | UX + Content | Content UX, readability |

---

## Supporting Python Tools

- `tools/knowledge_updater.py` — crawl4ai pipeline that fetches latest papers and updates `SECOND-KNOWLEDGE-BRAIN.md`

---

## Active Development Tasks

- [x] Phase 0: Research world-renowned copywriting frameworks and regulatory landscape
- [x] Phase 1: Implement sub-brief-intake.md
- [x] Phase 1: Implement sub-compliance-checker.md
- [x] Phase 1: Implement sub-framework-selector.md
- [x] Phase 1: Implement sub-content-generator.md
- [x] Phase 1: Implement sub-platform-adapter.md
- [x] Phase 1: Implement sub-quality-reviewer.md
- [x] Phase 1: Implement sub-ab-variant-generator.md
- [x] Phase 2: Build main harness (skills/main.md)
- [x] Phase 3: Build tools/knowledge_updater.py
- [x] Phase 4: Write tests/test-scenarios.md
- [x] Phase 5: Cross-skill wiring (share sub-quality-reviewer with Cluster B)

---

## Reference Files

- `PROJECT-detail.md` — Full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Phase-by-phase build roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — Self-improving knowledge base
