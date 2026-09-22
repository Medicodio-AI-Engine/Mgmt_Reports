# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-22 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_22_Employee_Rating_Cards.md, 2026_09_22_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written `docs(review)` audit/architect/gate-result logs committed to the feature branch

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:67` — Hand-written `docs(review)` audit/architect/gate-result logs committed to the feature branch
- [RECOMMENDATION] `SOURCE_067:67` — Automate with Devin — Devin already writes the review log as a PR comment; make the PR comment the record and stop committing logs to the product repo

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs(review)` audit/architect/gate-result logs committed to the feature branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Bulk-closing Devin QA/report PRs without a note

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:68` — Bulk-closing Devin QA/report PRs without a note
- [RECOMMENDATION] `SOURCE_067:68` — Improve documentation/process — one-line close reason ("superseded by fix X" / "won't fix, pre-existing") so BLOCK RELEASE verdicts do not disappear silently

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Bulk-closing Devin QA/report PRs without a note -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Self-authored review + self-merge on own PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:69` — Self-authored review + self-merge on own PR
- [RECOMMENDATION] `SOURCE_067:69` — Improve documentation/process — branch protection requiring a non-author approval with a body

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Self-authored review + self-merge on own PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate the F-6/F-1 items Devin already documented (`#1398`, `#1401` DEV-FIX-LIST #9 "Unclassified" grouping in `apps/web`) as scoped Devin fix PRs instead of 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:72` — Delegate the F-6/F-1 items Devin already documented (`#1398`, `#1401` DEV-FIX-LIST #9 "Unclassified" grouping in `apps/web`) as scoped Devin fix PRs instead of closing the reports — Good Devin Candidate (bounded, reproduced, has evidence).

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate the F-6/F-1 items Devin already documented (`#1398`, `#1401` DEV-FIX-LIST #9 "Unclassified" grouping in `apps/web`) as scoped Devin fix PRs instead of  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Use Devin to generate the review log from the PR thread rather than committing it — Good Devin Candidate.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:73` — Use Devin to generate the review log from the PR thread rather than committing it — Good Devin Candidate.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Use Devin to generate the review log from the PR thread rather than committing it — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Keep architectural decisions (`ADR-0058`, strategy-chain design) human-owned — Primarily Human-Owned; no change recommended.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:74` — Keep architectural decisions (`ADR-0058`, strategy-chain design) human-owned — Primarily Human-Owned; no change recommended.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Keep architectural decisions (`ADR-0058`, strategy-chain design) human-owned — Primarily Human-Owned; no change recommended. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Author merges own PR into `dev` after self-review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:94` — Author merges own PR into `dev` after self-review — `#1400` 18:38 UTC merged by author, peer approval 0 chars
- [RECOMMENDATION] `SOURCE_067:94` — Enable "require 1 approval, dismiss stale, no self-approval" on `dev`; owner: anirudh (repo admin)
- [REPORT_OBSERVATION] `SOURCE_067:94` — previous evidence: `#1214` 08-24 (315 files, 9 min); `#1364` 09-15 (12 own commits then self-approve/merge); recorded 09-13, 09-16

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Author merges own PR into `dev` after self-review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Devin PRs closed without disposition

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:95` — Devin PRs closed without disposition — `#1392`–`#1398` closed 09:29–09:30 UTC, 0 comments
- [RECOMMENDATION] `SOURCE_067:95` — Add a one-line close reason; re-open `#1398` finding F-1 as an issue
- [REPORT_OBSERVATION] `SOURCE_067:95` — previous evidence: 12 closed 12:02–12:05 UTC on 09-16 incl. fix PRs `#1360/#1369/#1371` (fixes never landed) — reported 09-16, 09-17

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Devin PRs closed without disposition -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` 0-character approvals given/received

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:96` — 0-character approvals given/received — Received on `#1399` (ragha82) and `#1400` (svh)
- [RECOMMENDATION] `SOURCE_067:96` — Same branch-protection change + "approval must name what was checked" in the rulebook he just hardened
- [REPORT_OBSERVATION] `SOURCE_067:96` — previous evidence: 25/32 on 08-21; 14/15 today team-wide; anirudh gave `#1362` 09-15

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- 0-character approvals given/received -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Manual live A/B repro writing for each QA finding, committed as markdown

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:127` — Manual live A/B repro writing for each QA finding, committed as markdown
- [RECOMMENDATION] `SOURCE_067:127` — Automate with Devin — each repro guide is already a step list; have Devin convert F-1/F-5/F-6 to API specs in `e2e/` so the repro is a test, not a document

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Manual live A/B repro writing for each QA finding, committed as markdown -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Merging large PRs with a 0-char approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:128` — Merging large PRs with a 0-char approval
- [RECOMMENDATION] `SOURCE_067:128` — Improve documentation/process — approval body must list what was checked

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Merging large PRs with a 0-char approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Devin to write the org-scope/data_scope authorization regression suite for `/cases/:id/steps` and the `#1398` F-1 endpoint together — Good Devin Candidate (both

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:131` — Devin to write the org-scope/data_scope authorization regression suite for `/cases/:id/steps` and the `#1398` F-1 endpoint together — Good Devin Candidate (both reproduced, security-relevant but bounded; human reviews the fix).

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Devin to write the org-scope/data_scope authorization regression suite for `/cases/:id/steps` and the `#1398` F-1 endpoint together — Good Devin Candidate (both -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Devin to open the `#1362` `ACR_NAME` prerequisite fix and a `dry_run` dispatch test — Good Devin Candidate (Devin already diagnosed it).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:132` — Devin to open the `#1362` `ACR_NAME` prerequisite fix and a `dry_run` dispatch test — Good Devin Candidate (Devin already diagnosed it).

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Devin to open the `#1362` `ACR_NAME` prerequisite fix and a `dry_run` dispatch test — Good Devin Candidate (Devin already diagnosed it). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Triage of the 14 `#1394` findings — Possible Devin Candidate (Devin drafts dispositions; author decides).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:133` — Triage of the 14 `#1394` findings — Possible Devin Candidate (Devin drafts dispositions; author decides).

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Triage of the 14 `#1394` findings — Possible Devin Candidate (Devin drafts dispositions; author decides). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` 0-character approval on large PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:151` — 0-character approval on large PR — `#1399` (644 files) 13:05 UTC
- [RECOMMENDATION] `SOURCE_067:151` — Approval must state scope checked; for docs-only PRs say so explicitly
- [REPORT_OBSERVATION] `SOURCE_067:151` — previous evidence: `#1363` (205 files) 09-15, `#1378` (542 files) 09-15 — reported 09-16

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- 0-character approval on large PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Workflow shipped without its documented prerequisite

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:152` — Workflow shipped without its documented prerequisite — No fix in first working day after failure
- [RECOMMENDATION] `SOURCE_067:152` — Create the variable or dispatch `dry_run` today; owner ragha82
- [REPORT_OBSERVATION] `SOURCE_067:152` — previous evidence: `#1362` merged 09-15 with `ACR_NAME` uncreated → failed 09-20 — reported 09-21

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Workflow shipped without its documented prerequisite -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Long-lived feature branch without PR until very large

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:178` — Long-lived feature branch without PR until very large
- [RECOMMENDATION] `SOURCE_067:178` — Improve documentation/process — open a draft PR on day 1 so Devin Review runs incrementally

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Long-lived feature branch without PR until very large -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Devin to write component/render tests for DOCX export and toolbar — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:181` — Devin to write component/render tests for DOCX export and toolbar — Good Devin Candidate.

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Devin to write component/render tests for DOCX export and toolbar — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Open a draft PR now so Devin Review runs on each push — Good Devin Candidate (process).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:182` — Open a draft PR now so Devin Review runs on each push — Good Devin Candidate (process).

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Open a draft PR now so Devin Review runs on each push — Good Devin Candidate (process). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` (none confirmed today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:200` — (none confirmed today) — New branch, 2 commits, no PR — watch
- [RECOMMENDATION] `SOURCE_067:200` — Open draft PR by 09-23
- [REPORT_OBSERVATION] `SOURCE_067:200` — previous evidence: `feat/hr-portal-revamp` no PR for 5 reports (09-11→09-16)

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- (none confirmed today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Empty approval on a peer PR with open Devin findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:226` — Empty approval on a peer PR with open Devin findings
- [RECOMMENDATION] `SOURCE_067:226` — Improve documentation/process — name what was checked

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Empty approval on a peer PR with open Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Devin to generate API contract tests for the service-provider module before PR — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:229` — Devin to generate API contract tests for the service-provider module before PR — Good Devin Candidate.

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Devin to generate API contract tests for the service-provider module before PR — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` (none confirmed)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:247` — (none confirmed) — 0-char approval enabling self-merge — first recorded instance for this member
- [RECOMMENDATION] `SOURCE_067:247` — Approval body must state scope
- [REPORT_OBSERVATION] `SOURCE_067:247` — previous evidence: —

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- (none confirmed) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Post-merge audit reports as markdown

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:273` — Post-merge audit reports as markdown
- [RECOMMENDATION] `SOURCE_067:273` — Automate with Devin — Devin already runs the gate; humans should decide and file fixes

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Post-merge audit reports as markdown -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Devin to implement the `batchUpsertForceOverride` party-identity fix now that a pinning test exists — Good Devin Candidate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:276` — Devin to implement the `batchUpsertForceOverride` party-identity fix now that a pinning test exists — Good Devin Candidate.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Devin to implement the `batchUpsertForceOverride` party-identity fix now that a pinning test exists — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Decision items left open after merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:294` — Decision items left open after merge — Still not filed as issues
- [RECOMMENDATION] `SOURCE_067:294` — File as issues this week
- [REPORT_OBSERVATION] `SOURCE_067:294` — previous evidence: `#1373` 7 NEEDS-DECISION 09-14; 9 "your call" items 09-05

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Decision items left open after merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Reviewer remediates peer PR with 20–44 commits then approves/merges (Saijyoti)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:319` — Reviewer remediates peer PR with 20–44 commits then approves/merges (Saijyoti)
- [RECOMMENDATION] `SOURCE_067:319` — Improve documentation/process — push fixes as suggestions or a stacked PR; author merges

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Reviewer remediates peer PR with 20–44 commits then approves/merges (Saijyoti) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Devin to fix the `#1398` F-1 module-access bypass with regression test — Good Devin Candidate (Saahil/Saijyoti to review).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:322` — Devin to fix the `#1398` F-1 module-access bypass with regression test — Good Devin Candidate (Saahil/Saijyoti to review).

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Devin to fix the `#1398` F-1 module-access bypass with regression test — Good Devin Candidate (Saahil/Saijyoti to review). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Post-merge NOT READY verdict unacknowledged

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:340` — Post-merge NOT READY verdict unacknowledged — `#1391` verdicts unanswered day 4; report PR closed without note
- [RECOMMENDATION] `SOURCE_067:340` — Merger posts a disposition within 1 working day
- [REPORT_OBSERVATION] `SOURCE_067:340` — previous evidence: `#1316`, `#1322`, `#1366`, `#1367`, `#1380`, `#1391` (6 consecutive)

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Post-merge NOT READY verdict unacknowledged -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Manual prompt-surface audits (orphans, dead registry rows, spelling)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:368` — Manual prompt-surface audits (orphans, dead registry rows, spelling)
- [RECOMMENDATION] `SOURCE_067:368` — Automate through scripts/tooling — a registry-vs-prompt-file consistency check in CI

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Manual prompt-surface audits (orphans, dead registry rows, spelling) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Manual dx-vs-px consistency checks on empty/edge documents

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:369` — Manual dx-vs-px consistency checks on empty/edge documents
- [RECOMMENDATION] `SOURCE_067:369` — Automate with Devin — Devin to write a shared fixture suite covering empty-doc, unknown-approach, and escape-hatch cases

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Manual dx-vs-px consistency checks on empty/edge documents -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Devin to build the regression harness around `_stage_io.json` captures (golden per-stage outputs on a fixed chart set) — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:372` — Devin to build the regression harness around `_stage_io.json` captures (golden per-stage outputs on a fixed chart set) — Good Devin Candidate.

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Devin to build the regression harness around `_stage_io.json` captures (golden per-stage outputs on a fixed chart set) — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Devin to generate the prompt-registry lint — Good Devin Candidate.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:373` — Devin to generate the prompt-registry lint — Good Devin Candidate.

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Devin to generate the prompt-registry lint — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Clinical vocabulary decisions (approach taxonomy, CARE-STATUS rule) — Primarily Human-Owned.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:374` — Clinical vocabulary decisions (approach taxonomy, CARE-STATUS rule) — Primarily Human-Owned.

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Clinical vocabulary decisions (approach taxonomy, CARE-STATUS rule) — Primarily Human-Owned. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` `feat/inpatient-engine` without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:392` — `feat/inpatient-engine` without PR — 15 more commits, still no PR
- [RECOMMENDATION] `SOURCE_067:392` — Open a draft PR to `uat` so Devin Review and CI run
- [REPORT_OBSERVATION] `SOURCE_067:392` — previous evidence: reported 09-05 → 09-18 (12 reports; Hitesh then afifa/Vishnu)

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- `feat/inpatient-engine` without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Bulk prompt version swaps (15 prompts) without recorded output diff

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:417` — Bulk prompt version swaps (15 prompts) without recorded output diff
- [RECOMMENDATION] `SOURCE_067:417` — Automate with Devin — Devin to run v5 vs v6 on a fixed chart set and attach the diff to the PR

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Bulk prompt version swaps (15 prompts) without recorded output diff -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Prompt A/B diff harness — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:420` — Prompt A/B diff harness — Good Devin Candidate.

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Prompt A/B diff harness — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Branch without PR (shared)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:438` — Branch without PR (shared) — as above
- [RECOMMENDATION] `SOURCE_067:438` — as above
- [REPORT_OBSERVATION] `SOURCE_067:438` — previous evidence: as above

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Branch without PR (shared) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Prompt edits with contentless commit messages

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:463` — Prompt edits with contentless commit messages
- [RECOMMENDATION] `SOURCE_067:463` — Improve documentation/process — one line: which prompt, what changed, why

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Prompt edits with contentless commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Devin to summarise a prompt diff into a commit message — Good Devin Candidate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:466` — Devin to summarise a prompt diff into a commit message — Good Devin Candidate.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Devin to summarise a prompt diff into a commit message — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Low-information commit messages

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:484` — Low-information commit messages — "imprving prompts", "prompt improvemnt"
- [RECOMMENDATION] `SOURCE_067:484` — Adopt the `type(scope): what — why` convention already used by peers on the same branch
- [REPORT_OBSERVATION] `SOURCE_067:484` — previous evidence: "beautfied excel" ×2 09-12 (reported 09-13)

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Low-information commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Feature → `uat` → prod on the same day with the same reviewer and one-word approvals

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:511` — Feature → `uat` → prod on the same day with the same reviewer and one-word approvals
- [RECOMMENDATION] `SOURCE_067:511` — Improve documentation/process — a UAT soak of at least one working day, and findings answered before the promotion PR

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Feature → `uat` → prod on the same day with the same reviewer and one-word approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Devin to disposition the 8 `#467`/`#468` findings (fix or reasoned rejection) — Good Devin Candidate; the SEC items need human sign-off.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:514` — Devin to disposition the 8 `#467`/`#468` findings (fix or reasoned rejection) — Good Devin Candidate; the SEC items need human sign-off.

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Devin to disposition the 8 `#467`/`#468` findings (fix or reasoned rejection) — Good Devin Candidate; the SEC items need human sign-off. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Devin to add unit tests for the empty-slice guard described in the body — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:515` — Devin to add unit tests for the empty-slice guard described in the body — Good Devin Candidate.

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Devin to add unit tests for the empty-slice guard described in the body — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Prod promotion with unanswered Devin findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:533` — Prod promotion with unanswered Devin findings — `#468` 3 BUG + 1 SEC unanswered, merged 12:17 UTC
- [RECOMMENDATION] `SOURCE_067:533` — Block promotion PR until each finding has a written disposition
- [REPORT_OBSERVATION] `SOURCE_067:533` — previous evidence: `#451` (09-11), `#458` (09-17, 4 findings), `#461` (09-18, inert-fix finding) — reported each time

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Prod promotion with unanswered Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Promotion PR with empty body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:560` — Promotion PR with empty body
- [RECOMMENDATION] `SOURCE_067:560` — Automate with Devin — Devin drafts the promotion body from the constituent PR titles/risks

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Promotion PR with empty body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Promotion-body generation — Good Devin Candidate.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:563` — Promotion-body generation — Good Devin Candidate.

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Promotion-body generation — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Facility-scope billing rules — Primarily Human-Owned (correctly human).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 5 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:564` — Facility-scope billing rules — Primarily Human-Owned (correctly human).

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Facility-scope billing rules — Primarily Human-Owned (correctly human). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Prod promotion merged within seconds

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:582` — Prod promotion merged within seconds — `#466` 25 s
- [RECOMMENDATION] `SOURCE_067:582` — One-working-day UAT soak; findings answered first
- [REPORT_OBSERVATION] `SOURCE_067:582` — previous evidence: `#453` 28 s (09-17, later reverted `#454`) — reported 09-17

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Prod promotion merged within seconds -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` One-word approval + immediate merge as gatekeeper for `uat`/prod

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:608` — One-word approval + immediate merge as gatekeeper for `uat`/prod
- [RECOMMENDATION] `SOURCE_067:608` — Improve documentation/process — approval template: findings checked / tests seen / rollback path

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- One-word approval + immediate merge as gatekeeper for `uat`/prod -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Devin pre-merge summary comment listing open findings per PR so the gatekeeper has a checklist — Good Devin Candidate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:611` — Devin pre-merge summary comment listing open findings per PR so the gatekeeper has a checklist — Good Devin Candidate.

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Devin pre-merge summary comment listing open findings per PR so the gatekeeper has a checklist — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` One-word approval on prod promotion with open findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:629` — One-word approval on prod promotion with open findings — `#466`, `#468` today
- [RECOMMENDATION] `SOURCE_067:629` — Require written disposition before merging to `release/prod_3.0`
- [REPORT_OBSERVATION] `SOURCE_067:629` — previous evidence: `#449` (09-08), `#458` (09-17), `#461` (09-18) — reported each time

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- One-word approval on prod promotion with open findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Manual `apps/backend

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:658` — Manual `apps/backend
- [RECOMMENDATION] `SOURCE_067:658` — `#6` (321 files, 09-17), 3 sync commits today; ~6 this month

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Manual `apps/backend -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Regenerated `repo-structure.md` commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:659` — Regenerated `repo-structure.md` commits
- [RECOMMENDATION] `SOURCE_067:659` — Already automated by hook — Continue (verify the hook, drop the manual PR)

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Regenerated `repo-structure.md` commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Prod promotion PRs with badge-only bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:660` — Prod promotion PRs with badge-only bodies
- [RECOMMENDATION] `SOURCE_067:660` — Automate with Devin — generated changelog body

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Prod promotion PRs with badge-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` Scheduled Dev_1.0 → application-2.0 sync PR — Good Devin Candidate.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:663` — Scheduled Dev_1.0 → application-2.0 sync PR — Good Devin Candidate.

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- Scheduled Dev_1.0 → application-2.0 sync PR — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Disposition of the 9 promotion findings — Possible Devin Candidate (Devin drafts, human decides for prod).

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:664` — Disposition of the 9 promotion findings — Possible Devin Candidate (Devin drafts, human decides for prod).

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Disposition of the 9 promotion findings — Possible Devin Candidate (Devin drafts, human decides for prod). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` 0-char approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:683` — 0-char approvals — `#657`, `#584`
- [RECOMMENDATION] `SOURCE_067:683` — Name what was checked
- [REPORT_OBSERVATION] `SOURCE_067:683` — previous evidence: 4 on 09-15, `#626`/`#651` era — reported 09-16, 09-17

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- 0-char approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Prod promotion with unanswered Devin findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:684` — Prod promotion with unanswered Devin findings — `#659` 6 BUG, `#585` 3 BUG
- [RECOMMENDATION] `SOURCE_067:684` — Disposition before merge
- [REPORT_OBSERVATION] `SOURCE_067:684` — previous evidence: `#626` (09-11)

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Prod promotion with unanswered Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Instant 0-char approve + merge of promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:711` — Instant 0-char approve + merge of promotions
- [RECOMMENDATION] `SOURCE_067:711` — Improve documentation/process — approval template

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Instant 0-char approve + merge of promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Devin to write pg-notify reconnection/cache-invalidation integration tests for `#660` — Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:714` — Devin to write pg-notify reconnection/cache-invalidation integration tests for `#660` — Good Devin Candidate.

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Devin to write pg-notify reconnection/cache-invalidation integration tests for `#660` — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` 0-char approve + merge of peer prod promotions within minutes

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:732` — 0-char approve + merge of peer prod promotions within minutes — `#659`, `#585` at 04:35–04:36 UTC
- [RECOMMENDATION] `SOURCE_067:732` — Written disposition of the 9 findings before/after merge
- [REPORT_OBSERVATION] `SOURCE_067:732` — previous evidence: `#626` (09-11), `#644` (09-15) — reported 09-12, 09-16

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- 0-char approve + merge of peer prod promotions within minutes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Self-merge after peer approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:733` — Self-merge after peer approval — `#584` 07:09 UTC
- [RECOMMENDATION] `SOURCE_067:733` — Let the approver merge
- [REPORT_OBSERVATION] `SOURCE_067:733` — previous evidence: `#573` 09-15

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Self-merge after peer approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` Payer/back-port fixes landing without PR or via self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:758` — Payer/back-port fixes landing without PR or via self-merge
- [RECOMMENDATION] `SOURCE_067:758` — Improve documentation/process — PR with Devin Review

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- Payer/back-port fixes landing without PR or via self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Contract test for the RPA webhook payload — Good Devin Candidate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:761` — Contract test for the RPA webhook payload — Good Devin Candidate.

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Contract test for the RPA webhook payload — Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` (none confirmed today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:779` — (none confirmed today) — branch, no PR yet
- [RECOMMENDATION] `SOURCE_067:779` — Open PR
- [REPORT_OBSERVATION] `SOURCE_067:779` — previous evidence: self-merge `#310` 09-11

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- (none confirmed today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` Self-merged PRs without review in this repo

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:804` — Self-merged PRs without review in this repo
- [RECOMMENDATION] `SOURCE_067:804` — Improve documentation/process — enable Devin Review + one reviewer

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- Self-merged PRs without review in this repo -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Enable Devin Review on the repo — Good Devin Candidate (config).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:807` — Enable Devin Review on the repo — Good Devin Candidate (config).

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Enable Devin Review on the repo — Good Devin Candidate (config). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` (none new)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:825` — (none new) — no merge today
- [RECOMMENDATION] `SOURCE_067:825` — Enable review
- [REPORT_OBSERVATION] `SOURCE_067:825` — previous evidence: self-merges `#21`–`#24`

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- (none new) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000129` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:847` — —
- [RECOMMENDATION] `SOURCE_067:847` — —

### DECISION: ISSUE_000129_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` `#435` without reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_067:868` — `#435` without reviewer — day 14
- [RECOMMENDATION] `SOURCE_067:868` — Assign reviewer or close
- [REPORT_OBSERVATION] `SOURCE_067:868` — previous evidence: day 7 (09-15)

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- `#435` without reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

