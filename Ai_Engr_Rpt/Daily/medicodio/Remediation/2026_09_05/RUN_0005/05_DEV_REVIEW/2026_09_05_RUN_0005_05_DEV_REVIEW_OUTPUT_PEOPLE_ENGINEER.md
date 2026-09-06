# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-05 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Fixing another author's PR to merge-readiness, then approving it

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:58` — Fixing another author's PR to merge-readiness, then approving it
- [RECOMMENDATION] `SOURCE_011:58` — Improve documentation/process — reviewer posts findings; author (or Devin, delegated by the author) fixes; a second person approves

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Fixing another author's PR to merge-readiness, then approving it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Backfilling "mandatory function headers" and `docs(headers)` commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — Backfilling "mandatory function headers" and `docs(headers)` commits
- [RECOMMENDATION] `SOURCE_011:59` — Automate through scripts/tooling — a lint rule/pre-commit that fails on a missing header removes the manual pass

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Backfilling "mandatory function headers" and `docs(headers)` commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`)
- [RECOMMENDATION] `SOURCE_011:60` — Automate with Devin — run the gate on the branch head and delegate "make the suite green without weakening assertions"

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` `docs(review-logs): record …` commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — `docs(review-logs): record …` commits
- [RECOMMENDATION] `SOURCE_011:61` — Automate through scripts/tooling — generate the log from the posted review + gate output

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- `docs(review-logs): record …` commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Merging `dev` into a 100+-file feature branch and repairing the merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:62` — Merging `dev` into a 100+-file feature branch and repairing the merge
- [RECOMMENDATION] `SOURCE_011:62` — Improve documentation/process — smaller, shorter-lived PRs

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Merging `dev` into a 100+-file feature branch and repairing the merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:65` — Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped query, `withRlsTx` for multi-table writes, `toErrorCode()` instead of `err.message`, bounded `findMany`) and run it against every open DVR PR."

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both 

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:66` — Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both sides" (the `816270755` class).

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:67` — Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — human decides the cut.

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` > 100-file feature PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:87` — > 100-file feature PRs — `#1317` 199 files, +25.6k, merged same day
- [RECOMMENDATION] `SOURCE_011:87` — Cap at 60 files; stack PRs; delegate the split to Devin
- [REPORT_OBSERVATION] `SOURCE_011:87` — previous evidence: 08-30 `#1260` (161), 09-02 `#1282` (89), 09-04 `#1306` (163)

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- > 100-file feature PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Remediate-then-approve (non-independent review)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:88` — Remediate-then-approve (non-independent review) — Today as reviewer: 25/25 in-window commits on `#1305`, 32/32 on `#1318`, then approved + merged both
- [RECOMMENDATION] `SOURCE_011:88` — Reviewer does not approve a PR on which they authored > 20 % of commits; a second approver required
- [REPORT_OBSERVATION] `SOURCE_011:88` — previous evidence: 09-03 `#1282`, 09-04 `#1306` (as author, reviewer fixed)

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Remediate-then-approve (non-independent review) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Approve with own open blockers/decisions

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:89` — Approve with own open blockers/decisions — `#1305` approved 4 m 39 s after "4 items need your decision"; `#1318` approved 17 min after 5 open items and "verify before sign-off"
- [RECOMMENDATION] `SOURCE_011:89` — Track as a watch item; open decisions should be filed as issues before approve
- [REPORT_OBSERVATION] `SOURCE_011:89` — previous evidence: — (first observation; not yet a Repeat Pattern)

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Approve with own open blockers/decisions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:121` — Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`)
- [RECOMMENDATION] `SOURCE_011:121` — Automate with Devin — "realign specs to the new interfaces without weakening assertions" after each fix wave

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Fixing the blocker in a PR she is reviewing

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:122` — Fixing the blocker in a PR she is reviewing
- [RECOMMENDATION] `SOURCE_011:122` — Improve documentation/process — post the fix direction (she did, in detail) and let the author or Devin implement

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Fixing the blocker in a PR she is reviewing -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Standards-audit log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:123` — Standards-audit log commits
- [RECOMMENDATION] `SOURCE_011:123` — Automate through scripts/tooling — generate from gate output

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Standards-audit log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:126` — Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is not green" — replaces hand-written gate claims.

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:127` — Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so the per-ref fan-out she flagged on `#1317` cannot recur."

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:128` — Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `DocumentTypeMultiSelect` collapse) once she has decided each" — decisions are hers; implementation is delegable.

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` 100+-file PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:148` — 100+-file PRs — `#1305` merged at 115 files; `#1318` 82
- [RECOMMENDATION] `SOURCE_011:148` — Cap at 60 files; ship PRD-2 features as stacked PRs
- [REPORT_OBSERVATION] `SOURCE_011:148` — previous evidence: 08-26 (`#1220` 130 files), 09-04/09-05 (`#1305` 109→115)

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- 100+-file PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Reviewer fixes the blocker, then approves

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:149` — Reviewer fixes the blocker, then approves — `#1317`: blocker fixed by her session (`6d3c61e46`) 16 min after her REQUEST CHANGES; approve 61 min later
- [RECOMMENDATION] `SOURCE_011:149` — Post fix direction; author or Devin implements; approve only what you did not write
- [REPORT_OBSERVATION] `SOURCE_011:149` — previous evidence: 09-03 `#1282` (14/46 commits), 09-04 `#1306` (20/81), `#1311` (16/22)

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Reviewer fixes the blocker, then approves -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` PR-body claims not matching verification

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: TENANT_ISOLATION
- Priority: 10 · Complexity: 10 · Tier: D
- Playbook: ORG_PB_TENANT_ISOLATION_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:150` — PR-body claims not matching verification — `#1305`: three claims disproved by reviewer ("Tests green — 39 gates", cross-tenant lookup "closed", `kb_rule_id` "added")
- [RECOMMENDATION] `SOURCE_011:150` — Watch item: paste raw gate output instead of a summary sentence
- [REPORT_OBSERVATION] `SOURCE_011:150` — previous evidence: — (first observation)

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- PR-body claims not matching verification -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

