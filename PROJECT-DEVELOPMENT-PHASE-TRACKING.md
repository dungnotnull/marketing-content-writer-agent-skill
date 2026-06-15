# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — Skill 9: marketing-content-writer

## Overview

| Phase | Name | Timeline | Status |
|-------|------|----------|--------|
| 0 | Research & Skill Architecture | Week 1–2 | In Progress |
| 1 | Core Sub-Skills | Week 3–5 | Pending |
| 2 | Main Harness + Quality Gates | Week 6–8 | Pending |
| 3 | SECOND-KNOWLEDGE-BRAIN Pipeline | Week 9–10 | Pending |
| 4 | Testing & Validation | Week 11–12 | Pending |
| 5 | Integration & Cross-Skill Wiring | Week 13–14 | Pending |

---

## Phase 0: Research & Skill Architecture (Week 1–2)

### Goal
Establish the complete theoretical foundation: copywriting frameworks, regulatory landscape, platform conventions, and evidence hierarchy before writing a single line of skill code.

### Task List
- [x] Survey copywriting frameworks: AIDA, PAS, FAB, StoryBrand (SB7), PASTOR, Before-After-Bridge, QUEST, ACCA, Hook-Story-Offer, 4Ps
- [x] Map regulatory constraints by industry and jurisdiction:
  - FDA: 21 CFR Part 202 (prescription drug advertising), FDA cosmetic guidance
  - EU: EC 1223/2009 Cosmetics Regulation, EFSA health claims (EC 1924/2006)
  - FTC: Endorsement Guides 16 CFR Part 255, Green Guides 16 CFR Part 260
  - UK ASA / BCAP Code
  - ASEAN: regulatory overview for cosmetic claims
- [x] Identify 10 authoritative knowledge sources per industry for crawl pipeline
- [x] Define platform conventions: Instagram, TikTok, YouTube, Blog, Email, Landing Page, LinkedIn, Print
- [x] Design the harness stage sequence (confirmed in PROJECT-detail.md)
- [x] Define quality gate thresholds (Brand Voice ≥ 7, Persuasion ≥ 7, Compliance = Pass)
- [x] Write CLAUDE.md, PROJECT-detail.md, PROJECT-DEVELOPMENT-PHASE-TRACKING.md ← **DONE**

### Deliverables
- [x] CLAUDE.md
- [x] PROJECT-detail.md
- [x] PROJECT-DEVELOPMENT-PHASE-TRACKING.md (this file)
- [x] SECOND-KNOWLEDGE-BRAIN.md (seed version)

### Success Criteria
- All regulatory jurisdictions mapped with specific rule references
- All 10 copywriting frameworks documented with use-case fit guidance
- Harness architecture approved and locked

### Estimated Effort: 6–8 hours research + documentation

---

## Phase 1: Core Sub-Skills (Week 3–5)

### Goal
Implement all 7 sub-skill files — the modular building blocks of the harness.

### Task List
- [x] Write `skills/sub-brief-intake.md`
  - Intake prompt template (8 required fields)
  - Clarification question tree for missing fields
  - Output: structured brief JSON schema
- [x] Write `skills/sub-compliance-checker.md`
  - Regulatory decision tree: industry → jurisdiction → applicable rules
  - Forbidden claims list per industry
  - Approved language guide (claim softening patterns)
  - Risk level scoring: Low/Medium/High
  - Disclosure requirement templates
- [x] Write `skills/sub-framework-selector.md`
  - Framework selection matrix: goal × audience × platform × industry → framework
  - Justification template for each framework recommendation
  - Secondary framework pairing logic
- [x] Write `skills/sub-content-generator.md`
  - Framework execution templates (one per framework)
  - Evidence citation embed pattern
  - Compliance constraint injection
  - Word count calibration logic
- [x] Write `skills/sub-platform-adapter.md`
  - 10 platform format specs (character limits, hashtag rules, CTA placement, visual cue notes)
  - Content chunking / expansion logic
  - Native language pattern library per platform
- [x] Write `skills/sub-quality-reviewer.md`
  - Scoring rubrics for each of the 5 dimensions
  - Improvement note generation templates
  - Re-score trigger logic
- [x] Write `skills/sub-ab-variant-generator.md`
  - Variant divergence strategies: angle, hook, CTA, emotional register, sub-segment targeting
  - A/B comparison table template

### Deliverables
- [x] 7 sub-skill `.md` files in `skills/`

### Success Criteria
- Each sub-skill has: purpose, inputs, outputs, tools, step-by-step instructions, quality gate
- sub-compliance-checker covers all 3 industries × minimum 3 jurisdictions
- sub-platform-adapter covers minimum 8 platforms
- sub-quality-reviewer scoring rubrics are quantitative (not subjective)

### Estimated Effort: 12–16 hours

---

## Phase 2: Main Harness + Quality Gates (Week 6–8)

### Goal
Build the top-level orchestration harness (`skills/main.md`) that drives all sub-skills in the correct sequence with quality gate checks at each stage.

### Task List
- [x] Write `skills/main.md` — primary skill entry point
  - Role & Persona definition (senior marketing strategist + compliance specialist)
  - Full harness workflow (9 stages, numbered)
  - Sub-skill invocation instructions
  - Inter-stage quality gate logic
  - Error handling: missing brief data, compliance failure, quality gate fail
  - Graceful degradation instructions (offline mode)
  - Output format specification
- [x] Validate stage transitions:
  - Stage 1 → 2: brief is complete
  - Stage 2 → 3: compliance risk ≤ Medium OR user accepts High-risk track
  - Stage 5 → 7: draft passes Gate 3
  - Stage 7 → 8: passes Gate 4
- [x] Define final output template

### Deliverables
- [x] `skills/main.md`

### Success Criteria
- main.md can be invoked standalone and drives the full workflow end-to-end
- All 5 quality gates are embedded in harness flow
- Output template produces a professional, structured deliverable (not a chat reply)

### Estimated Effort: 8–10 hours

---

## Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline (Week 9–10)

### Goal
Build the automated knowledge crawl pipeline (`tools/knowledge_updater.py`) that keeps the skill's knowledge base current.

### Task List
- [x] Write `tools/knowledge_updater.py`
  - Sources: PubMed, FDA.gov, EFSA, Cosmetics Europe, FTC.gov, Vogue Business, Business of Fashion, Journal of Advertising Research, Content Marketing Institute
  - crawl4ai integration for each source
  - Parsing: title, authors, date, DOI/URL, abstract, key findings
  - Scoring: recency + domain keyword relevance
  - Deduplication: DOI/URL hash check
  - Append to SECOND-KNOWLEDGE-BRAIN.md with date-stamped format
  - Scheduled to run weekly
- [x] Seed SECOND-KNOWLEDGE-BRAIN.md with 30+ initial entries (5+ per knowledge category)
- [x] Test pipeline: run updater, verify new entries appended correctly, verify deduplication

### Deliverables
- [x] `tools/knowledge_updater.py`
- [x] Updated `SECOND-KNOWLEDGE-BRAIN.md` (seeded)

### Success Criteria
- Pipeline runs without errors on test execution
- Deduplication verified (re-running does not add duplicate entries)
- SECOND-KNOWLEDGE-BRAIN.md has ≥ 30 seeded entries across 3 industries

### Estimated Effort: 10–14 hours

---

## Phase 4: Testing & Validation (Week 11–12)

### Goal
Validate the full harness against real-world content brief scenarios and confirm quality gate behavior.

### Task List
- [x] Write `tests/test-scenarios.md` with ≥ 7 scenario tests ← **DONE in this session**
- [x] Execute Scenario 1 (healthcare supplement post): verify FDA compliance check triggers
- [x] Execute Scenario 2 (cosmetics landing page): verify EU Cosmetics Regulation check
- [x] Execute Scenario 3 (fashion TikTok): verify greenwashing flag
- [x] Execute Scenario 4 (medical clinic email): verify FTC endorsement check
- [x] Execute Scenario 5 (skincare SKU descriptions): verify parallel brief processing
- [x] Execute Scenario 6 (fashion brand Instagram story): verify multi-format platform adapter
- [x] Execute Scenario 7 (high-risk healthcare claim): verify Gate 2 blocks and offers conservative track
- [x] Quality check: verify all outputs include both A/B variants
- [x] Quality check: verify all outputs include evidence citations
- [x] Quality check: verify quality scorecard appears in every output
- [x] Edge case: brief with missing audience → verify clarification questions triggered
- [x] Edge case: WebSearch unavailable → verify graceful degradation message appears

### Deliverables
- [x] `tests/test-scenarios.md`
- [x] Validated test execution logs

### Success Criteria
- All 7 scenarios produce outputs that pass Gates 1–5
- High-risk scenario (Scenario 7) correctly blocks and reroutes
- Graceful degradation scenario produces valid output with explicit limitation note

### Estimated Effort: 8–10 hours

---

## Phase 5: Integration & Cross-Skill Wiring (Week 13–14)

### Goal
Connect shared sub-skills with other harnesses in the skill library and ensure Cluster D integrates cleanly with the cross-cutting design patterns.

### Task List
- [x] Verify `sub-quality-reviewer.md` is compatible with Cluster B quality reviewer pattern
- [x] Verify `sub-brief-intake.md` aligns with Cluster A intake patterns for reusability
- [x] Register skill in root `D:\Dungchan\skill\CLAUDE.md` cluster map
- [x] Update `progression.json` to mark folder 9 as completed
- [x] Final review: confirm all 8 required files present and complete
- [x] Documentation review: ensure all files are in English, follow Claude Skill standard

### Deliverables
- [x] Updated `D:\Dungchan\skill\progression.json`
- [x] Cross-skill compatibility verification notes

### Success Criteria
- Folder 9 passes all file presence checks (8 required files)
- Skill is invocable standalone without dependency on other cluster's files
- progression.json updated correctly

### Estimated Effort: 4–6 hours

---

## Milestone Summary

| Milestone | Target Date | Criteria |
|-----------|-------------|----------|
| M0: Architecture Locked | End Week 2 | All 3 planning docs complete, regulatory landscape mapped |
| M1: Sub-Skills Complete | End Week 5 | All 7 sub-skill files pass self-review |
| M2: Harness Functional | End Week 8 | main.md drives end-to-end flow in test |
| M3: Knowledge Pipeline Live | End Week 10 | Updater runs, SECOND-KNOWLEDGE-BRAIN.md seeded ≥ 30 entries |
| M4: Test Suite Passed | End Week 12 | All 7 scenarios pass Gates 1–5 |
| M5: Integration Complete | End Week 14 | Folder 9 fully integrated, progression.json updated |
