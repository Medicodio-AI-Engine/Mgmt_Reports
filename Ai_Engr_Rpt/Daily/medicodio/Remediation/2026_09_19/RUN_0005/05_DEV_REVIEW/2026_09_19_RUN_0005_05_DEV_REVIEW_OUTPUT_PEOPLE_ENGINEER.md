# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-19 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_19_Employee_Rating_Cards.md, 2026_09_19_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Review-log / standards-log / atlas refresh commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — Review-log / standards-log / atlas refresh commits
- [RECOMMENDATION] `SOURCE_011:59` — Automate with Devin — generate the logs from the gate output in one bot commit

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Review-log / standards-log / atlas refresh commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` "Repair what the pre-push gate surfaced" (type errors, imports, JSX)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — "Repair what the pre-push gate surfaced" (type errors, imports, JSX)
- [RECOMMENDATION] `SOURCE_011:60` — Automate through scripts/tooling — run the gate locally before pushing (prek hook already exists)

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- "Repair what the pre-push gate surfaced" (type errors, imports, JSX) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Function-header relocation/restoration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Function-header relocation/restoration
- [RECOMMENDATION] `SOURCE_011:61` — Automate through scripts/tooling — lint rule instead of hand edits (recommended 09-17, not done)

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Function-header relocation/restoration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Reviewer pushes 20–44 fix commits to a peer's PR then merges it

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:62` — Reviewer pushes 20–44 fix commits to a peer's PR then merges it
- [RECOMMENDATION] `SOURCE_011:62` — Improve documentation/process — branch protection: approver may not have commits on the branch

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Reviewer pushes 20–44 fix commits to a peer's PR then merges it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:65` — Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three registry cache copies; per-case party cap; `buildBoundPartyOverlay(prefixes)` wire-or-remove) — each is a scoped fix with a stated acceptance test.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:66` — Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:67` — Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body.

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Reviewer remediates, then approves and merges (no independent approver)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:87` — Reviewer remediates, then approves and merges (no independent approver) — `#1391`: 44 own commits → `approved` → merge in 11 s
- [RECOMMENDATION] `SOURCE_011:87` — Branch protection on `dev`: approver ≠ committer; if she remediates, Saahil or anirudh approves
- [REPORT_OBSERVATION] `SOURCE_011:87` — previous evidence: `#1288` 09-06, `#1322` 09-11, `#1367` 09-14, `#1380` 09-16, `#1390` 09-17 (09-18 report: "do not approve #1391 if you push fixes to it")

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Reviewer remediates, then approves and merges (no independent approver) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Merge with own open pre-merge list

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:88` — Merge with own open pre-merge list — Closeout log: "Still open — author-side, before merge" ×4, merged 10 min later
- [RECOMMENDATION] `SOURCE_011:88` — Convert the list into PR checklist items that block merge
- [REPORT_OBSERVATION] `SOURCE_011:88` — previous evidence: `#1367` "pending 2 schema index decisions" (09-14); `#1380` (09-16)

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Merge with own open pre-merge list -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` QA verdict consumed after merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:89` — QA verdict consumed after merge — `#1391` BLOCK RELEASE / NOT READY 52 at +74 min
- [RECOMMENDATION] `SOURCE_011:89` — Run gate on PR head before approval (runner exists)
- [REPORT_OBSERVATION] `SOURCE_011:89` — previous evidence: `#1367`, `#1380`, `#1389`, `#1390` all NOT READY / KNOWN RISKS post-merge

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- QA verdict consumed after merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Header relocation / review-log commits by hand

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:90` — Header relocation / review-log commits by hand — 2 header + 7 log commits
- [RECOMMENDATION] `SOURCE_011:90` — Lint rule + bot commit
- [REPORT_OBSERVATION] `SOURCE_011:90` — previous evidence: 09-16, 09-17 (lint rule recommended)

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Header relocation / review-log commits by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Gate-surfaced repair commits after push

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:117` — Gate-surfaced repair commits after push
- [RECOMMENDATION] `SOURCE_011:117` — Automate through scripts/tooling — local gate before push

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Gate-surfaced repair commits after push -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Oversized single PR (>200 files)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Oversized single PR (>200 files)
- [RECOMMENDATION] `SOURCE_011:118` — Improve documentation/process — split by runtime; §5.2 size justification

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Oversized single PR (>200 files) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:121` — Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:122` — Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log.

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:123` — Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items).

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Oversized single PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:141` — Oversized single PR — `#1391` 284 files / 28k lines vs 800-line ceiling, no §5.2 justification
- [RECOMMENDATION] `SOURCE_011:141` — Split by runtime; justification in body
- [REPORT_OBSERVATION] `SOURCE_011:141` — previous evidence: `#1310` (09-09), `#1322` (09-11)

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Oversized single PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Author's own findings dispositioned by reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:142` — Author's own findings dispositioned by reviewer — 13 Devin findings + 11 decision items answered by reviewer, 0 by author
- [RECOMMENDATION] `SOURCE_011:142` — Author answers findings in-thread within the day
- [REPORT_OBSERVATION] `SOURCE_011:142` — previous evidence: `#1322` merged by Saijyoti after 16 of her commits (09-11)

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Author's own findings dispositioned by reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

