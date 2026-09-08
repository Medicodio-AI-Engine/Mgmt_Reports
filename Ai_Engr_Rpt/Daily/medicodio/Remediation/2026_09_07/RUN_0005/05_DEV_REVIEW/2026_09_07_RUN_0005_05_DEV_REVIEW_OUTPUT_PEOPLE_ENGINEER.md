# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-07 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge)
- [RECOMMENDATION] `SOURCE_011:59` — Improve documentation/process — reviewer posts findings, author (or Devin on the author's behalf) fixes, a second person approves

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Recording review passes as `docs(review-logs)` commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Recording review passes as `docs(review-logs)` commits
- [RECOMMENDATION] `SOURCE_011:60` — Automate through scripts/tooling — generate the log from the PR review API

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Recording review passes as `docs(review-logs)` commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift)
- [RECOMMENDATION] `SOURCE_011:61` — Automate with Devin — a nightly "does `dev` pass its own gates" run that files the fix before it lands on someone's branch

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:62` — Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind)
- [RECOMMENDATION] `SOURCE_011:62` — Improve documentation/process — the Stop-and-Check table is already a checklist; have Devin pre-fill it on the PR

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:65` — Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number fallback; raw-token behaviour when field metadata is absent — Devin's 19:46 finding) using the `persons.service.spec.ts:50-64` recipe, and run the suite so the gate is green before anyone reviews.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:66` — Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inheriting failures.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:67` — Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the code references from the review, for anirudh-medicodio and Amrutha-Beedikar to decide.

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Approves and merges a branch he remediated

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:88` — Approves and merges a branch he remediated — `#1288`: 11 of 12 commits his; 12.2k review → own 0-char APPROVE → own merge, 41 min
- [RECOMMENDATION] `SOURCE_011:88` — Hand approval to a second reader when > 25 % of commits are the reviewer's; on a weekend, wait or leave the PR open
- [REPORT_OBSERVATION] `SOURCE_011:88` — previous evidence: 09-03 `#1257` (16 commits, 0-char approve); 09-04 `#1259` (15 of 19 commits, 11.9k review then merge)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Approves and merges a branch he remediated -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Own "needs decision" items left open at merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:89` — Own "needs decision" items left open at merge — 1 self-declared blocker + 6 decision items merged to `dev` without a written decision or waiver
- [RECOMMENDATION] `SOURCE_011:89` — Write the decision (or the explicit "ship with known risk, ADR-0045 owns it") on the PR before approving
- [REPORT_OBSERVATION] `SOURCE_011:89` — previous evidence: 09-04 `#1259`/`#1304` disclosed items; 09-06 (team) nine "your call" items

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Own "needs decision" items left open at merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` `#1278` `importSession` SEV-High finding without fix or waiver

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:90` — `#1278` `importSession` SEV-High finding without fix or waiver — No commit or waiver
- [RECOMMENDATION] `SOURCE_011:90` — Fix or waive in writing by tomorrow (owner unchanged)
- [REPORT_OBSERVATION] `SOURCE_011:90` — previous evidence: 09-03, 09-04, 09-05, 09-06

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- `#1278` `importSession` SEV-High finding without fix or waiver -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Large unreviewed branches

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:91` — Large unreviewed branches — `feat/document-catalog-samples` 84 files / +10.4k, no PR
- [RECOMMENDATION] `SOURCE_011:91` — Open a draft PR now; split at ≤ 60 files
- [REPORT_OBSERVATION] `SOURCE_011:91` — previous evidence: 09-04 `#1259` 526 commits behind `dev`; 6 open PRs ≥ 56 files

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Large unreviewed branches -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Insufficient data — one commit in the week

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Insufficient data — one commit in the week
- [RECOMMENDATION] `SOURCE_011:118` — —

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Insufficient data — one commit in the week -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:121` — Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:122` — Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio, applicant-settings) — each is the same bounded change she made in `#1288`.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Devin findings on own PR unanswered

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:140` — Devin findings on own PR unanswered — Closed by the reviewer's commits, not hers; 0 replies
- [RECOMMENDATION] `SOURCE_011:140` — Disposition every finding within one working day (fix / reject with reason / out of scope)
- [REPORT_OBSERVATION] `SOURCE_011:140` — previous evidence: 09-03 (6 unanswered after 13 h), 09-04, 09-05, 09-06

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Devin findings on own PR unanswered -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Open PR not progressed by its author

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:141` — Open PR not progressed by its author — `#1288` completed by someone else
- [RECOMMENDATION] `SOURCE_011:141` — Ask for help or hand the PR over explicitly rather than leaving it
- [REPORT_OBSERVATION] `SOURCE_011:141` — previous evidence: 09-05 "open PRs idle" (`#1288`)

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Open PR not progressed by its author -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

