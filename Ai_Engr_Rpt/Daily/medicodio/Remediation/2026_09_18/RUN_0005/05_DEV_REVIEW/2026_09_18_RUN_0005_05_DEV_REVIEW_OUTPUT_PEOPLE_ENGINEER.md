# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-18 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_18_Employee_Rating_Cards.md, 2026_09_18_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` `docs(review-logs): close … with the real gate matrix`

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:69` — `docs(review-logs): close … with the real gate matrix`
- [RECOMMENDATION] `SOURCE_011:69` — Automate with Devin — generate gate matrix from CI + QA report JSON

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- `docs(review-logs): close … with the real gate matrix` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Filing CLEANUP-xxx items by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:70` — Filing CLEANUP-xxx items by hand
- [RECOMMENDATION] `SOURCE_011:70` — Automate through scripts/tooling — issue template + linter that opens the item

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Filing CLEANUP-xxx items by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Test-mock repair after schema/catalog change (12 commits)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:71` — Test-mock repair after schema/catalog change (12 commits)
- [RECOMMENDATION] `SOURCE_011:71` — Automate with Devin — "update all mocks that mirror `LIVE_CASE_PARTY`" is a bounded sweep

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Test-mock repair after schema/catalog change (12 commits) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate the review-log / gate-matrix closing commit: input = CI run URL + QA report path, output = the log section. Removes ~3 manual commits/day.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:74` — Delegate the review-log / gate-matrix closing commit: input = CI run URL + QA report path, output = the log section. Removes ~3 manual commits/day.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate the review-log / gate-matrix closing commit: input = CI run URL + QA report path, output = the log section. Removes ~3 manual commits/day. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Ask Devin for a mock-consistency sweep whenever a catalog constant changes (today's 12 fix commits are exactly this shape).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:75` — Ask Devin for a mock-consistency sweep whenever a catalog constant changes (today's 12 fix commits are exactly this shape).

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Ask Devin for a mock-consistency sweep whenever a catalog constant changes (today's 12 fix commits are exactly this shape). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Have Devin draft the pre-merge QA verdict summary into the PR body so the merge decision cites it.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:76` — Have Devin draft the pre-merge QA verdict summary into the PR body so the merge decision cites it.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Have Devin draft the pre-merge QA verdict summary into the PR body so the merge decision cites it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Merge before the Devin QA verdict

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:95` — Merge before the Devin QA verdict — `#1386` merged 09-17 03:03; QA NOT READY 55/100 at 16:07
- [RECOMMENDATION] `SOURCE_011:95` — QA verdict quoted in PR body as a merge precondition on >100-file PRs
- [REPORT_OBSERVATION] `SOURCE_011:95` — previous evidence: `#1363` 09-13, `#1373` 09-15, `#1380` 09-16 (all NOT READY after merge)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Merge before the Devin QA verdict -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Reviewer remediates, approves, merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:96` — Reviewer remediates, approves, merges — `#1389`: 12 own commits → empty approval → merge 12 s later
- [RECOMMENDATION] `SOURCE_011:96` — Branch-protection: approver must have no commits on the branch
- [REPORT_OBSERVATION] `SOURCE_011:96` — previous evidence: 09-06 `#1288`, 09-14 `#1367`

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Reviewer remediates, approves, merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Self-merge on a 7-s empty co-approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:97` — Self-merge on a 7-s empty co-approval — `#1386`: svh approval (0 chars) 03:02:52, merge 03:03:00
- [RECOMMENDATION] `SOURCE_011:97` — Second reviewer names the check performed
- [REPORT_OBSERVATION] `SOURCE_011:97` — previous evidence: `#1373` (09-15)

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Self-merge on a 7-s empty co-approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` `#1358` closed without disposition

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:98` — `#1358` closed without disposition — still no note; `#1388` (QA report) also closed unmerged
- [RECOMMENDATION] `SOURCE_011:98` — One-line disposition on every closed Devin PR
- [REPORT_OBSERVATION] `SOURCE_011:98` — previous evidence: 09-16, 09-17

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- `#1358` closed without disposition -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Function-header backfill (§4.2) — 25 files today, 21 files on `#1380` 09-16

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:129` — Function-header backfill (§4.2) — 25 files today, 21 files on `#1380` 09-16
- [RECOMMENDATION] `SOURCE_011:129` — Automate through scripts/tooling — a lint rule fails CI instead of a person backfilling

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Function-header backfill (§4.2) — 25 files today, 21 files on `#1380` 09-16 -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Timestamp-surface sweep ("close the surfaces the sweep missed")

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:130` — Timestamp-surface sweep ("close the surfaces the sweep missed")
- [RECOMMENDATION] `SOURCE_011:130` — Automate with Devin — grep-driven inventory + fixture test per surface

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Timestamp-surface sweep ("close the surfaces the sweep missed") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Remediating a colleague's PR end-to-end before approving

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:131` — Remediating a colleague's PR end-to-end before approving
- [RECOMMENDATION] `SOURCE_011:131` — Improve documentation/process — request changes and let the author fix, or take over authorship explicitly

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Remediating a colleague's PR end-to-end before approving -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Generate a timestamp-surface inventory test (every component that renders a date gets one fixture) so the "surfaces the sweep missed" class closes permanently.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:134` — Generate a timestamp-surface inventory test (every component that renders a date gets one fixture) so the "surfaces the sweep missed" class closes permanently.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Generate a timestamp-surface inventory test (every component that renders a date gets one fixture) so the "surfaces the sweep missed" class closes permanently. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Delegate the header-backfill as a lint autofix PR rather than 25-file manual commits.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:135` — Delegate the header-backfill as a lint autofix PR rather than 25-file manual commits.

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Delegate the header-backfill as a lint autofix PR rather than 25-file manual commits. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Use Devin to draft the "known risks" section for `#1390`'s follow-up so the 70/100 verdict has an owner list.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:136` — Use Devin to draft the "known risks" section for `#1390`'s follow-up so the 70/100 verdict has an owner list.

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Use Devin to draft the "known risks" section for `#1390`'s follow-up so the 70/100 verdict has an owner list. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Reviewer remediates, then approves and merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:155` — Reviewer remediates, then approves and merges — `#1390`: 20 commits → approval 20 s → merge
- [RECOMMENDATION] `SOURCE_011:155` — Approver-without-commits rule; if she must fix, Vineeth or anirudh approves
- [REPORT_OBSERVATION] `SOURCE_011:155` — previous evidence: 09-06, 09-14, 09-15, 09-16 (`#1380`)

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Reviewer remediates, then approves and merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` QA verdict after merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:156` — QA verdict after merge — `#1389` NOT READY 64/100 after merge
- [RECOMMENDATION] `SOURCE_011:156` — QA gate before merge
- [REPORT_OBSERVATION] `SOURCE_011:156` — previous evidence: `#1380` NOT READY (09-16)

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- QA verdict after merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` "repair the typecheck and lint failures the first gate run surfaced"

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:186` — "repair the typecheck and lint failures the first gate run surfaced"
- [RECOMMENDATION] `SOURCE_011:186` — Automate through scripts/tooling — pre-push hook running the gate

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- "repair the typecheck and lint failures the first gate run surfaced" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Standards-audit doc + gate history

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:187` — Standards-audit doc + gate history
- [RECOMMENDATION] `SOURCE_011:187` — Automate with Devin

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Standards-audit doc + gate history -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Split `#1391` by runtime (api / worker / scheduler / web) with Devin generating the per-runtime PR bodies from the audit doc.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:190` — Split `#1391` by runtime (api / worker / scheduler / web) with Devin generating the per-runtime PR bodies from the audit doc.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Split `#1391` by runtime (api / worker / scheduler / web) with Devin generating the per-runtime PR bodies from the audit doc. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Migration dry-run + rollback checklist for the path-registry split.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:191` — Migration dry-run + rollback checklist for the path-registry split.

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Migration dry-run + rollback checklist for the path-registry split. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` >200-file single PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:210` — >200-file single PR — `#1391` 262 files
- [RECOMMENDATION] `SOURCE_011:210` — Split by runtime before review
- [REPORT_OBSERVATION] `SOURCE_011:210` — previous evidence: `#1310` 09-09 (recorded in 09-10 report)

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- >200-file single PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Multi-day branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:238` — Multi-day branch without PR
- [RECOMMENDATION] `SOURCE_011:238` — Improve documentation/process — draft-PR-on-first-push

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Multi-day branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Phase-result ledger commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:239` — Phase-result ledger commits
- [RECOMMENDATION] `SOURCE_011:239` — Automate with Devin

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Phase-result ledger commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` DOCX-fidelity fixture tests: template → rendered → expected table/spacing attributes.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:242` — DOCX-fidelity fixture tests: template → rendered → expected table/spacing attributes.

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- DOCX-fidelity fixture tests: template → rendered → expected table/spacing attributes. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Open `feat/support-letter-word-fidelity` as a draft now; let Devin Review run on the 84-file move before more lands on top.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:243` — Open `feat/support-letter-word-fidelity` as a draft now; let Devin Review run on the 84-file move before more lands on top.

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Open `feat/support-letter-word-fidelity` as a draft now; let Devin Review run on the 84-file move before more lands on top. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:261` — Branch without PR — `feat/support-letter-word-fidelity`, 11 commits, 84-file move
- [RECOMMENDATION] `SOURCE_011:261` — Draft PR today
- [REPORT_OBSERVATION] `SOURCE_011:261` — previous evidence: 5 prior reports

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Feature finished by the reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:262` — Feature finished by the reviewer — Saijyoti 20 commits on his branch
- [RECOMMENDATION] `SOURCE_011:262` — Author addresses review; reviewer approves
- [REPORT_OBSERVATION] `SOURCE_011:262` — previous evidence: `#1365` closed; `#1390`

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Feature finished by the reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` "expose Prometheus metrics …" per service

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:288` — "expose Prometheus metrics …" per service
- [RECOMMENDATION] `SOURCE_011:288` — Automate with Devin — one template, six PRs, or one shared factory (which `8ae2a2e` starts)

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- "expose Prometheus metrics …" per service -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Generate metric-name + label-cardinality tests per service from the shared factory.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:291` — Generate metric-name + label-cardinality tests per service from the shared factory.

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Generate metric-name + label-cardinality tests per service from the shared factory. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Have Devin triage the 15 findings into "fix / accept with reason / out of scope" so the disposition is a review, not a rewrite.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:292` — Have Devin triage the 15 findings into "fix / accept with reason / out of scope" so the disposition is a review, not a rewrite.

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Have Devin triage the 15 findings into "fix / accept with reason / out of scope" so the disposition is a review, not a rewrite. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Findings left undispositioned

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:310` — Findings left undispositioned — still open; +15 on `#1394`
- [RECOMMENDATION] `SOURCE_011:310` — Owner + date per finding in-thread
- [REPORT_OBSERVATION] `SOURCE_011:310` — previous evidence: `#1382` red spec, `#1384` (09-16, 09-17 reports)

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Findings left undispositioned -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Empty approvals on >200-file PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:335` — Empty approvals on >200-file PRs
- [RECOMMENDATION] `SOURCE_011:335` — Improve documentation/process — approval names the check performed

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Empty approvals on >200-file PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Ask Devin for a "what changed since my last look" digest before approving a 250-file PR.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:338` — Ask Devin for a "what changed since my last look" digest before approving a 250-file PR.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Ask Devin for a "what changed since my last look" digest before approving a 250-file PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Empty co-approval enabling self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:356` — Empty co-approval enabling self-merge — `#1386` 7 s before merge
- [RECOMMENDATION] `SOURCE_011:356` — Approval text states which gate output was read
- [REPORT_OBSERVATION] `SOURCE_011:356` — previous evidence: `#1380` (09-16)

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Empty co-approval enabling self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:381` — —
- [RECOMMENDATION] `SOURCE_011:381` — —

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` `#1373` decision items 1–3 (in prod since 09-15) — Devin can draft the decision record from the thread.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:384` — `#1373` decision items 1–3 (in prod since 09-15) — Devin can draft the decision record from the thread.

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- `#1373` decision items 1–3 (in prod since 09-15) — Devin can draft the decision record from the thread. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` `#1373` decisions unrecorded

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:402` — `#1373` decisions unrecorded — still unrecorded
- [RECOMMENDATION] `SOURCE_011:402` — Record today
- [REPORT_OBSERVATION] `SOURCE_011:402` — previous evidence: 09-15, 09-16, 09-17

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- `#1373` decisions unrecorded -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Manual `Dev_1.0 → Dev_2.0` sync PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:431` — Manual `Dev_1.0 → Dev_2.0` sync PRs
- [RECOMMENDATION] `SOURCE_011:431` — Automate through scripts/tooling — scheduled sync PR with generated manifest

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Manual `Dev_1.0 → Dev_2.0` sync PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Hand-made `dev → uat` promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:432` — Hand-made `dev → uat` promotion PRs
- [RECOMMENDATION] `SOURCE_011:432` — Same manifest generator

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Hand-made `dev → uat` promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 4 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:433` — Empty approvals
- [RECOMMENDATION] `SOURCE_011:433` — Improve documentation/process
- [REPORT_OBSERVATION] `SOURCE_011:488` — Empty approvals
- [RECOMMENDATION] `SOURCE_011:488` — Improve documentation/process

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Scheduled `Dev_1.0 → Dev_2.0` sync PR whose body lists the ported commits and conflicts — replaces `#6`.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:436` — Scheduled `Dev_1.0 → Dev_2.0` sync PR whose body lists the ported commits and conflicts — replaces `#6`.

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Scheduled `Dev_1.0 → Dev_2.0` sync PR whose body lists the ported commits and conflicts — replaces `#6`. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Regression tests for the writeback cron under 2+ replicas (Devin can extend today's `withCronLock` spec).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:437` — Regression tests for the writeback cron under 2+ replicas (Devin can extend today's `withCronLock` spec).

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Regression tests for the writeback cron under 2+ replicas (Devin can extend today's `withCronLock` spec). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Promotion manifest: "PRs and Devin findings carried by this promotion" auto-generated.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:438` — Promotion manifest: "PRs and Devin findings carried by this promotion" auto-generated.

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Promotion manifest: "PRs and Devin findings carried by this promotion" auto-generated. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Empty approvals on prod-bound PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:457` — Empty approvals on prod-bound PRs — `#6`, `#652`, `#578` merged with 0-char approvals
- [RECOMMENDATION] `SOURCE_011:457` — Approval names the check; CI test gate
- [REPORT_OBSERVATION] `SOURCE_011:457` — previous evidence: every report since 08-21

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Empty approvals on prod-bound PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Hand-made sync/promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:458` — Hand-made sync/promotion PRs — `#5`, `#6`
- [RECOMMENDATION] `SOURCE_011:458` — Manifest generator (Team Opportunity 1)
- [REPORT_OBSERVATION] `SOURCE_011:458` — previous evidence: 09-11, 09-12, 09-16, 09-17

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Hand-made sync/promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Production `23505` fix (`#651` closed)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:459` — Production `23505` fix (`#651` closed) — no `release/prod_1.0` PR observed today
- [RECOMMENDATION] `SOURCE_011:459` — Confirm prod status in writing
- [REPORT_OBSERVATION] `SOURCE_011:459` — previous evidence: 09-16, 09-17

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Production `23505` fix (`#651` closed) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Three successive "enhance/improve error handling" refactors on the same file

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:487` — Three successive "enhance/improve error handling" refactors on the same file
- [RECOMMENDATION] `SOURCE_011:487` — Automate with Devin — one pass with tests instead of three iterations

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Three successive "enhance/improve error handling" refactors on the same file -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Regression tests for cron-expression edge cases (blank, nonzero seconds, day-constraint intersection) — the last three findings on `#584`/`#657` are exactly thi

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:491` — Regression tests for cron-expression edge cases (blank, nonzero seconds, day-constraint intersection) — the last three findings on `#584`/`#657` are exactly this.

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Regression tests for cron-expression edge cases (blank, nonzero seconds, day-constraint intersection) — the last three findings on `#584`/`#657` are exactly thi -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Multi-replica test harness for the import trigger (two workers, one lock).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:492` — Multi-replica test harness for the import trigger (two workers, one lock).

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Multi-replica test harness for the import trigger (two workers, one lock). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:510` — Empty approvals — 4 today, incl. `#6` (321 files)
- [RECOMMENDATION] `SOURCE_011:510` — One sentence naming the check
- [REPORT_OBSERVATION] `SOURCE_011:510` — previous evidence: 09-11 → 09-17

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Partial finding disposition on prod-path features

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:511` — Partial finding disposition on prod-path features — 26 open on `#657`/`#584`
- [RECOMMENDATION] `SOURCE_011:511` — Disposition before promotion
- [REPORT_OBSERVATION] `SOURCE_011:511` — previous evidence: `#646` RLS finding (09-16)

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Partial finding disposition on prod-path features -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Per-client ENM rule branches (DVG, McQueen)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:538` — Per-client ENM rule branches (DVG, McQueen)
- [RECOMMENDATION] `SOURCE_011:538` — Automate with Devin — client-config-driven rule + generated parity test

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Per-client ENM rule branches (DVG, McQueen) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Turn each "verified unreachable" disposition into an executable test so the argument cannot rot.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:541` — Turn each "verified unreachable" disposition into an executable test so the argument cannot rot.

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Turn each "verified unreachable" disposition into an executable test so the argument cannot rot. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` Generate the per-client parity fixtures for the E&M level rule.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:542` — Generate the per-client parity fixtures for the E&M level rule.

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- Generate the per-client parity fixtures for the E&M level rule. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:560` — — — —
- [RECOMMENDATION] `SOURCE_011:560` — —
- [REPORT_OBSERVATION] `SOURCE_011:560` — previous evidence: none in history

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Manual `client_configs` sync from prod DB

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:587` — Manual `client_configs` sync from prod DB
- [RECOMMENDATION] `SOURCE_011:587` — Automate through scripts/tooling — export script + generated diff PR

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Manual `client_configs` sync from prod DB -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` `uat → prod` template promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:588` — `uat → prod` template promotions
- [RECOMMENDATION] `SOURCE_011:588` — Manifest generator

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- `uat → prod` template promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Client-config diff report (what knob changed, which client, which gate) posted to the PR before merge.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:591` — Client-config diff report (what knob changed, which client, which gate) posted to the PR before merge.

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Client-config diff report (what knob changed, which client, which gate) posted to the PR before merge. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` A real parity guard test for the gynecology clone (the finding says the current one checks nothing).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:592` — A real parity guard test for the gynecology clone (the finding says the current one checks nothing).

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- A real parity guard test for the gynecology clone (the finding says the current one checks nothing). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Prod promotion on ≤4-char approval

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:610` — Prod promotion on ≤4-char approval — `#459` "okay" → self-merge in 1 min
- [RECOMMENDATION] `SOURCE_011:610` — Require CI test gate + named approval
- [REPORT_OBSERVATION] `SOURCE_011:610` — previous evidence: `#453`/`#458` 09-16 and earlier

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Prod promotion on ≤4-char approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Findings unanswered after merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:611` — Findings unanswered after merge — `#464` ×6, `#465` ×3
- [RECOMMENDATION] `SOURCE_011:611` — Disposition or revert
- [REPORT_OBSERVATION] `SOURCE_011:611` — previous evidence: `#458` ×4

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Findings unanswered after merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` `feat/log_prob` branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:612` — `feat/log_prob` branch without PR — unchanged
- [RECOMMENDATION] `SOURCE_011:612` — Draft PR
- [REPORT_OBSERVATION] `SOURCE_011:612` — previous evidence: 09-17

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- `feat/log_prob` branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Prompt files recovered/reverted by hand

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:639` — Prompt files recovered/reverted by hand
- [RECOMMENDATION] `SOURCE_011:639` — Improve documentation/process — prompts versioned via PR, never via stash

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Prompt files recovered/reverted by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` 4-char approvals on prod PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:640` — 4-char approvals on prod PRs
- [RECOMMENDATION] `SOURCE_011:640` — Approval names the check

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- 4-char approvals on prod PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` A prompt-diff check that fails CI when `dx/px` extraction prompts change without a changelog entry.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:643` — A prompt-diff check that fails CI when `dx/px` extraction prompts change without a changelog entry.

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- A prompt-diff check that fails CI when `dx/px` extraction prompts change without a changelog entry. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Have Devin reproduce the BMI finding (`Z68` inactive) on a fixture chart.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:644` — Have Devin reproduce the BMI finding (`Z68` inactive) on a fixture chart.

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Have Devin reproduce the BMI finding (`Z68` inactive) on a fixture chart. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` Merge-then-revert on prompt content

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:662` — Merge-then-revert on prompt content — 3× 31-file revert chain today
- [RECOMMENDATION] `SOURCE_011:662` — Prompt changes via PR with Devin Review
- [REPORT_OBSERVATION] `SOURCE_011:662` — previous evidence: `#453` (09-16)

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- Merge-then-revert on prompt content -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` Prod promotion with an open Devin finding

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:663` — Prod promotion with an open Devin finding — `#460`/`#461`
- [RECOMMENDATION] `SOURCE_011:663` — Answer before promotion
- [REPORT_OBSERVATION] `SOURCE_011:663` — previous evidence: `#458` ×4 (09-16)

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- Prod promotion with an open Devin finding -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000352` 0-minute merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:688` — 0-minute merges
- [RECOMMENDATION] `SOURCE_011:688` — Improve documentation/process — wait for Devin Review + CI

### DECISION: ISSUE_000352_ATTEMPT_01
<!-- 0-minute merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000353` A merge-queue rule: no merge until Devin Review has posted.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:691` — A merge-queue rule: no merge until Devin Review has posted.

### DECISION: ISSUE_000353_ATTEMPT_01
<!-- A merge-queue rule: no merge until Devin Review has posted. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000354` Merge before automated review posts

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:709` — Merge before automated review posts — `#464` merged 10:33, findings 10:34
- [RECOMMENDATION] `SOURCE_011:709` — Merge-queue wait
- [REPORT_OBSERVATION] `SOURCE_011:709` — previous evidence: `#453` (09-16)

### DECISION: ISSUE_000354_ATTEMPT_01
<!-- Merge before automated review posts -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000355` Prompt-variant runs via runner flags

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:734` — Prompt-variant runs via runner flags
- [RECOMMENDATION] `SOURCE_011:734` — Automate through scripts/tooling — eval matrix output committed with the promotion

### DECISION: ISSUE_000355_ATTEMPT_01
<!-- Prompt-variant runs via runner flags -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000356` Eval-report generator for prompt promotions (recall/precision per chart set) attached to the PR.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:737` — Eval-report generator for prompt promotions (recall/precision per chart set) attached to the PR.

### DECISION: ISSUE_000356_ATTEMPT_01
<!-- Eval-report generator for prompt promotions (recall/precision per chart set) attached to the PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000357` —

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:755` — — — live-prompt promotion without PR
- [RECOMMENDATION] `SOURCE_011:755` — Open PR
- [REPORT_OBSERVATION] `SOURCE_011:755` — previous evidence: none in history

### DECISION: ISSUE_000357_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000358` Self-merge to `main` 0 min after open

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:781` — Self-merge to `main` 0 min after open
- [RECOMMENDATION] `SOURCE_011:781` — Improve documentation/process — enable Devin Review; second approver

### DECISION: ISSUE_000358_ATTEMPT_01
<!-- Self-merge to `main` 0 min after open -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000359` Per-branch split skeletons (three endoscopy branches)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:782` — Per-branch split skeletons (three endoscopy branches)
- [RECOMMENDATION] `SOURCE_011:782` — Automate with Devin — table-driven steps

### DECISION: ISSUE_000359_ATTEMPT_01
<!-- Per-branch split skeletons (three endoscopy branches) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000360` Screenshot-diff replay harness for the split flow ("one stitched picture per split" is already captured — assert on it).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: C
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:785` — Screenshot-diff replay harness for the split flow ("one stitched picture per split" is already captured — assert on it).

### DECISION: ISSUE_000360_ATTEMPT_01
<!-- Screenshot-diff replay harness for the split flow ("one stitched picture per split" is already captured — assert on it). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000361` Table-driven test for the eleven splitting insurances.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:786` — Table-driven test for the eleven splitting insurances.

### DECISION: ISSUE_000361_ATTEMPT_01
<!-- Table-driven test for the eleven splitting insurances. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000362` Self-merge to `main`, no review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:804` — Self-merge to `main`, no review — `#23`, `#24`
- [RECOMMENDATION] `SOURCE_011:804` — Enable Devin Review on the repo
- [REPORT_OBSERVATION] `SOURCE_011:804` — previous evidence: 09-16

### DECISION: ISSUE_000362_ATTEMPT_01
<!-- Self-merge to `main`, no review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000363` Lockfile churn repair after merges

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:829` — Lockfile churn repair after merges
- [RECOMMENDATION] `SOURCE_011:829` — Automate through scripts/tooling — `npm ci` check in CI

### DECISION: ISSUE_000363_ATTEMPT_01
<!-- Lockfile churn repair after merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000364` Lockfile-drift CI check.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:832` — Lockfile-drift CI check.

### DECISION: ISSUE_000364_ATTEMPT_01
<!-- Lockfile-drift CI check. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000365` `hitesh/` branches under `karthikmed`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:850` — `hitesh/` branches under `karthikmed` — `#652`/`#578` merged
- [RECOMMENDATION] `SOURCE_011:850` — Clarify authorship in PR body
- [REPORT_OBSERVATION] `SOURCE_011:850` — previous evidence: 09-17

### DECISION: ISSUE_000365_ATTEMPT_01
<!-- `hitesh/` branches under `karthikmed` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000366` Same secret/doc fix applied to 3 repos by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: SECRETS
- Priority: 7 · Complexity: 9 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:876` — Same secret/doc fix applied to 3 repos by hand
- [RECOMMENDATION] `SOURCE_011:876` — Automate through scripts/tooling — shared env-example source

### DECISION: ISSUE_000366_ATTEMPT_01
<!-- Same secret/doc fix applied to 3 repos by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000367` Env-example consistency check across nodejs/react/2.0.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:879` — Env-example consistency check across nodejs/react/2.0.

### DECISION: ISSUE_000367_ATTEMPT_01
<!-- Env-example consistency check across nodejs/react/2.0. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000368` Devin-reviewed PR closed without disposition

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:897` — Devin-reviewed PR closed without disposition — `#581`
- [RECOMMENDATION] `SOURCE_011:897` — One-line note
- [REPORT_OBSERVATION] `SOURCE_011:897` — previous evidence: team pattern 09-15/16

### DECISION: ISSUE_000368_ATTEMPT_01
<!-- Devin-reviewed PR closed without disposition -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000369` Direct pushes without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:923` — Direct pushes without PR
- [RECOMMENDATION] `SOURCE_011:923` — Improve documentation/process

### DECISION: ISSUE_000369_ATTEMPT_01
<!-- Direct pushes without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000370` Retry/back-off tests for eCW PPV lookups (Good Devin Candidate).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: C
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:926` — Retry/back-off tests for eCW PPV lookups (Good Devin Candidate).

### DECISION: ISSUE_000370_ATTEMPT_01
<!-- Retry/back-off tests for eCW PPV lookups (Good Devin Candidate). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000371` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:938` — — — —
- [RECOMMENDATION] `SOURCE_011:938` — —
- [REPORT_OBSERVATION] `SOURCE_011:938` — previous evidence: none in history

### DECISION: ISSUE_000371_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

