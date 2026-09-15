# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-15 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:51` — Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results)
- [RECOMMENDATION] `SOURCE_011:51` — Automate through scripts/tooling: generate the ledger from the `/review-` skill outputs and the CI gate run; keep only the human decision text hand-written

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` "regenerate atlas (module_map, screen_index)" commit

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:52` — "regenerate atlas (module_map, screen_index)" commit
- [RECOMMENDATION] `SOURCE_011:52` — Automate through scripts/tooling: pre-commit/CI job regenerates the atlas; no human commit

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- "regenerate atlas (module_map, screen_index)" commit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Remediating a peer's PR before approving it

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:53` — Remediating a peer's PR before approving it
- [RECOMMENDATION] `SOURCE_011:53` — Improve documentation/process: reviewer requests changes → author (or Devin, via `/fix`) remediates → reviewer approves; the reviewer's own remediation should be reviewed by someone else

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Remediating a peer's PR before approving it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:56` — Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-14 QA gates could not exercise them, and the bug she fixed ("re-enqueue silently no-op'd") is a mocked-Prisma blind spot of the kind first named on 08-30. Good Devin Candidate.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1 -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:57` — Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets and the retry leg against seeded volumes and proposes the additive migration; she approves the shape. Possible Devin Candidate (schema approval stays human).

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:58` — Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Devin Candidate.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Reviewer remediates, then approves, then merges the same PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:78` — Reviewer remediates, then approves, then merges the same PR — `#1367`: 20 own commits → 8.1k review → 8-char approval 4 min later → own merge 5 min later
- [RECOMMENDATION] `SOURCE_011:78` — A second approver for any PR where the reviewer authored >0 commits; enforce via CODEOWNERS/branch protection on `dev`
- [REPORT_OBSERVATION] `SOURCE_011:78` — previous evidence: 09-07 `#1288` (anirudh), 09-11 `#1316/#1331/#1337`, 09-12 `#1322` (Saijyoti)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Reviewer remediates, then approves, then merges the same PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Merge with own "needs your decision" items open

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:79` — Merge with own "needs your decision" items open — `#1367`: "pending 2 schema decisions" + a nit, merged 9 min later with no written decision
- [RECOMMENDATION] `SOURCE_011:79` — Decision items become GitHub issues or a follow-up PR before merge; PR body states who owns each
- [REPORT_OBSERVATION] `SOURCE_011:79` — previous evidence: 09-07 `#1288` (6 items), 09-11 `#1331` (5), 09-13 `#1366` (6 + 2 acceptance criteria)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Merge with own "needs your decision" items open -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Post-merge Devin QA NOT READY

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:80` — Post-merge Devin QA NOT READY — 09-14 `#1367` (45/100)
- [RECOMMENDATION] `SOURCE_011:80` — Run the QA gate on the branch before approval (`ci.yml` still `workflow_dispatch`-only per the 09-07 disclosure)
- [REPORT_OBSERVATION] `SOURCE_011:80` — previous evidence: 09-11 `#1316` (55), 09-12 `#1322` (55), 09-13 `#1366`

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Post-merge Devin QA NOT READY -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Hand-written review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:81` — Hand-written review-log commits — 5 today
- [RECOMMENDATION] `SOURCE_011:81` — Generate from tooling
- [REPORT_OBSERVATION] `SOURCE_011:81` — previous evidence: 08-21 → 09-13 (every GC feature PR)

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Hand-written review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Atlas regeneration / function-header sync / debt-ledger sync commits

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:112` — Atlas regeneration / function-header sync / debt-ledger sync commits
- [RECOMMENDATION] `SOURCE_011:112` — Automate through scripts/tooling (CI job or pre-commit hook regenerates and fails if stale)

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Atlas regeneration / function-header sync / debt-ledger sync commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` `/review-all` ledger written into `docs/review-logs/` by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:113` — `/review-all` ledger written into `docs/review-logs/` by hand
- [RECOMMENDATION] `SOURCE_011:113` — Automate with Devin: Devin runs the review-skill fan-out on the PR and posts the ledger as a PR comment

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- `/review-all` ledger written into `docs/review-logs/` by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Review-pass commits on a peer's branch

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Review-pass commits on a peer's branch
- [RECOMMENDATION] `SOURCE_011:114` — Improve documentation/process: request changes with the list; let the author or Devin `/fix` implement

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Review-pass commits on a peer's branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:117` — Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surfaces are mapped in the atlas; a Good Devin Candidate for a first draft he then reviews.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before merge. Good Devin Candidate.

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Devin QA gate pre-merge on `#1373` (shared with Saijyoti).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:119` — Devin QA gate pre-merge on `#1373` (shared with Saijyoti).

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Devin QA gate pre-merge on `#1373` (shared with Saijyoti). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Review-pass as 20+ direct commits on a peer's PR instead of a review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:139` — Review-pass as 20+ direct commits on a peer's PR instead of a review — `#1373`: 27 commits, no review object
- [RECOMMENDATION] `SOURCE_011:139` — Post the findings as a "Request changes" review; commit only what the author delegates
- [REPORT_OBSERVATION] `SOURCE_011:139` — previous evidence: 09-11/09-12 `#1366` (22 commits, then 8-char approval)

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Review-pass as 20+ direct commits on a peer's PR instead of a review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Work on a branch without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:140` — Work on a branch without a PR — `docs/entity-status-phase-1-and-2-prds` (2 commits, no PR)
- [RECOMMENDATION] `SOURCE_011:140` — Draft PR at first push
- [REPORT_OBSERVATION] `SOURCE_011:140` — previous evidence: 09-06 `feat/ai-cm-draft-support-letter-skill`
- [REPORT_OBSERVATION] `SOURCE_011:264` — Feature branch with no PR
- [RECOMMENDATION] `SOURCE_011:264` — Draft PR at first push

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Work on a branch without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Sync/regeneration chores as human commits

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:141` — Sync/regeneration chores as human commits — 5 today
- [RECOMMENDATION] `SOURCE_011:141` — CI regeneration
- [REPORT_OBSERVATION] `SOURCE_011:141` — previous evidence: 09-13 (2), all month

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Sync/regeneration chores as human commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Hand-fixing Devin PRs after Devin Review findings

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:169` — Hand-fixing Devin PRs after Devin Review findings
- [RECOMMENDATION] `SOURCE_011:169` — Automate with Devin: reply to the finding with the instruction and let Devin push the fix

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Hand-fixing Devin PRs after Devin Review findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:172` — Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:173` — Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green.

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Small PRs left open without requesting review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:191` — Small PRs left open without requesting review — Both still open, no reviewer requested
- [RECOMMENDATION] `SOURCE_011:191` — Request a reviewer at open
- [REPORT_OBSERVATION] `SOURCE_011:191` — previous evidence: `#1360` open since 09-11, `#1364` since 09-11

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Small PRs left open without requesting review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Large PR opened without a named reviewer

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:216` — Large PR opened without a named reviewer
- [RECOMMENDATION] `SOURCE_011:216` — Improve documentation/process: reviewer assigned at open; split >60-file PRs

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Large PR opened without a named reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:219` — Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candidate.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Devin QA gate on `#1363` before merge — the PR touches performance/security paths.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:220` — Devin QA gate on `#1363` before merge — the PR touches performance/security paths.

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Devin QA gate on `#1363` before merge — the PR touches performance/security paths. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` >60-file PR without reviewer

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:238` — >60-file PR without reviewer — `#1363` idle day 4
- [RECOMMENDATION] `SOURCE_011:238` — Assign reviewer; split
- [REPORT_OBSERVATION] `SOURCE_011:238` — previous evidence: `#1288`

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- >60-file PR without reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Branch with large checkpoint, no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:239` — Branch with large checkpoint, no PR — Still no PR (last commit 09-10)
- [RECOMMENDATION] `SOURCE_011:239` — Draft PR
- [REPORT_OBSERVATION] `SOURCE_011:239` — previous evidence: `feat/document-catalog-samples` 09-07 report

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Branch with large checkpoint, no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:267` — Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` `feat/hr-portal-revamp` no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:285` — `feat/hr-portal-revamp` no PR — Still none (5th)
- [RECOMMENDATION] `SOURCE_011:285` — Draft PR today
- [REPORT_OBSERVATION] `SOURCE_011:285` — previous evidence: 09-11, 09-12, 09-13, 09-14 reports

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- `feat/hr-portal-revamp` no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Placeholder `Co-Authored-By` Devin e-mails

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:286` — Placeholder `Co-Authored-By` Devin e-mails — No new commits to check
- [RECOMMENDATION] `SOURCE_011:286` — Fix the trailer template
- [REPORT_OBSERVATION] `SOURCE_011:286` — previous evidence: 09-13 (`devin@example.com`)

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Placeholder `Co-Authored-By` Devin e-mails -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Findings/promotions carried without disposition

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:337` — Findings/promotions carried without disposition — `#308`, `#314`, `#435` unchanged through Monday
- [RECOMMENDATION] `SOURCE_011:337` — Tuesday-first triage with a named owner each
- [REPORT_OBSERVATION] `SOURCE_011:337` — previous evidence: 09-11 → 09-14

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Findings/promotions carried without disposition -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` `feat/inpatient-engine` no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:338` — `feat/inpatient-engine` no PR — 9th (last commit 09-11)
- [RECOMMENDATION] `SOURCE_011:338` — Draft PR
- [REPORT_OBSERVATION] `SOURCE_011:338` — previous evidence: 8 reports

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- `feat/inpatient-engine` no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Reviews ≤10 chars on production-bound PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:339` — Reviews ≤10 chars on production-bound PRs — No reviews today to re-confirm
- [RECOMMENDATION] `SOURCE_011:339` — Approval template naming what was checked
- [REPORT_OBSERVATION] `SOURCE_011:339` — previous evidence: 08-20 → 09-12 (every window)

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Reviews ≤10 chars on production-bound PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

