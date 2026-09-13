# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-13 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-fixing another member's findings, then approving and merging

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:54` — Hand-fixing another member's findings, then approving and merging
- [RECOMMENDATION] `SOURCE_011:54` — Improve documentation/process: reviewer posts findings, author (or Devin) remediates, a member who did not commit approves

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-fixing another member's findings, then approving and merging -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` `docs(review-logs)` commits written by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:55` — `docs(review-logs)` commits written by hand
- [RECOMMENDATION] `SOURCE_011:55` — Automate through scripts/tooling: generate the log from the reviews API at merge time

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- `docs(review-logs)` commits written by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Re-running the 37-gate matrix and transcribing results into prose

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:56` — Re-running the 37-gate matrix and transcribing results into prose
- [RECOMMENDATION] `SOURCE_011:56` — Automate through scripts/tooling: enable the `pull_request` trigger on `ci.yml` (disclosed as `workflow_dispatch`-only on 09-07) and let the check post the table

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Re-running the 37-gate matrix and transcribing results into prose -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`, 

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`, `accepted→Approved`) plus snapshot tests for both portals — bounded, PRD-specified, currently the top open decision on a merged PR.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`,  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is never swept before anyone designs the fix.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Reviewer remediates, approves, then merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:81` — Reviewer remediates, approves, then merges — `#1366`: 22 of the branch's final commits and all 31 remediations are his; his own approval is 8 characters
- [RECOMMENDATION] `SOURCE_011:81` — A member who has not committed to the branch approves; >25 % authorship disqualifies approval
- [REPORT_OBSERVATION] `SOURCE_011:81` — previous evidence: 09-04 (4 of 9 merges), 09-06, 09-07 (`#1288`), 09-10 (`#1350`), 09-11 (`#1316`, `#1331`, `#1337`, `#1349`)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Reviewer remediates, approves, then merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Merged over the approver's own written blocker

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:82` — Merged over the approver's own written blocker — Review says "this shouldn't merge until someone decides"; merged 16 min later with 2 unmet PRD criteria and 6 decision items, no written decision
- [RECOMMENDATION] `SOURCE_011:82` — Require a written decision or an explicit "ship with known risk" line before merge; convert NEEDS-DECISION rows into tracked issues
- [REPORT_OBSERVATION] `SOURCE_011:82` — previous evidence: 09-07 (`#1288`, "one blocker survives", merged 41 min later)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Merged over the approver's own written blocker -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Post-merge QA-gate verdict unactioned in-window

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:83` — Post-merge QA-gate verdict unactioned in-window — `#1366` → NOT READY, fix PR `#1371` open and unmerged at window close; `#1358` and `#1369` also still open
- [RECOMMENDATION] `SOURCE_011:83` — Make the QA gate a pre-merge check, or assign the fix PR an owner and an SLA on the same day
- [REPORT_OBSERVATION] `SOURCE_011:83` — previous evidence: 09-11 (`#1316` → fix PR `#1358`), 09-12 (`#1322` → `#1369`)

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Post-merge QA-gate verdict unactioned in-window -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Ad-hoc per-component timestamp formatting

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Ad-hoc per-component timestamp formatting
- [RECOMMENDATION] `SOURCE_011:114` — Automate with Devin (in progress and working): finish with a lint rule that fails on `toLocaleString`/`Intl.DateTimeFormat` outside `format-utils`

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Ad-hoc per-component timestamp formatting -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Branch carried without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:115` — Branch carried without a PR
- [RECOMMENDATION] `SOURCE_011:115` — Improve documentation/process: open a draft PR at first push so Devin Review and CI run

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Branch carried without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC selection), which is the missing evidence a reviewer needs for a 73-file diff.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:119` — Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real).

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:120` — Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Work carried on a branch with no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:139` — Work carried on a branch with no PR — Branch unchanged since 09-11 16:04, still no PR
- [RECOMMENDATION] `SOURCE_011:139` — Open a draft PR (or close the branch) before the next push
- [REPORT_OBSERVATION] `SOURCE_011:139` — previous evidence: Reported 09-11 and 09-12 for `feat/hr-portal-revamp`

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Work carried on a branch with no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Large single PR (73 files) awaiting a human reviewer

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:140` — Large single PR (73 files) awaiting a human reviewer — No human review event in 2 days; only Devin Review has looked at it
- [RECOMMENDATION] `SOURCE_011:140` — Split by layer (formatter/lib, migration, profile UI) or request a named reviewer
- [REPORT_OBSERVATION] `SOURCE_011:140` — previous evidence: `#1365` open since 09-11

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Large single PR (73 files) awaiting a human reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Author absent while another member remediates and merges his PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:166` — Author absent while another member remediates and merges his PR
- [RECOMMENDATION] `SOURCE_011:166` — Improve documentation/process: hold the merge for the author's written decision, or record an explicit hand-off in the PR

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Author absent while another member remediates and merges his PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:169` — Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR.

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:170` — Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migration.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Decision items on his PRs resolved without him

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:188` — Decision items on his PRs resolved without him — 2 unmet PRD acceptance criteria + 6 decision items answered by nobody; merged anyway
- [RECOMMENDATION] `SOURCE_011:188` — Reply in-thread with a decision (or "ship with known risk") before the PR is merged
- [REPORT_OBSERVATION] `SOURCE_011:188` — previous evidence: 09-11 (`#1322`), 09-12 report

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Decision items on his PRs resolved without him -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` PR-description accuracy

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:189` — PR-description accuracy — Same, uncorrected at merge
- [RECOMMENDATION] `SOURCE_011:189` — Fill the hygiene section from the diff (a Devin task), not from memory
- [REPORT_OBSERVATION] `SOURCE_011:189` — previous evidence: Reviewer's correction on `#1366`: "no new utility/route/component/hook/store/DTO/endpoint" was wrong — the branch adds ~25 exported surfaces, a DTO field and a query-key member

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- PR-description accuracy -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

