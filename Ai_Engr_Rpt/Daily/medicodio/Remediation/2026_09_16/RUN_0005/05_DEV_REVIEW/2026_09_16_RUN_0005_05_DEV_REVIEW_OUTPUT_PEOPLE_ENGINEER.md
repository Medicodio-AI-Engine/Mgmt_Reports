# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-16 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_16_Employee_Rating_Cards.md, 2026_09_16_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` `docs(review-logs)` commits recording gate runs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:48` — `docs(review-logs)` commits recording gate runs
- [RECOMMENDATION] `SOURCE_011:48` — Automate through scripts/tooling — emit the log from the gate runner

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- `docs(review-logs)` commits recording gate runs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Manual 42-gate run + hand-typed verdict table

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:49` — Manual 42-gate run + hand-typed verdict table
- [RECOMMENDATION] `SOURCE_011:49` — Automate with Devin — the gate run + table is mechanical; the decisions are not

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Manual 42-gate run + hand-typed verdict table -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Delegate the §4.4 data-correction script with explicit ACs (three counts on UAT/prod, idempotent, behind the schema-approval gate) — the missing artefact his ow

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:52` — Delegate the §4.4 data-correction script with explicit ACs (three counts on UAT/prod, idempotent, behind the schema-approval gate) — the missing artefact his own review named.

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Delegate the §4.4 data-correction script with explicit ACs (three counts on UAT/prod, idempotent, behind the schema-approval gate) — the missing artefact his ow -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Devin session to add a pre-push test run for the specs touched by a branch (he noted the hook "does not run tests, which is exactly where two of the four blocke

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:53` — Devin session to add a pre-push test run for the specs touched by a branch (he noted the hook "does not run tests, which is exactly where two of the four blockers lived").

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Devin session to add a pre-push test run for the specs touched by a branch (he noted the hook "does not run tests, which is exactly where two of the four blocke -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Merge over his own written blocker

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:72` — Merge over his own written blocker — `#1373` approved+merged 2 min after "REQUEST-DECISION on release readiness"; NOT READY gate after
- [RECOMMENDATION] `SOURCE_011:72` — Branch protection on `dev`: no self-merge on PRs the reviewer has committed to; NEEDS-DECISION rows must be closed in the PR before approve
- [REPORT_OBSERVATION] `SOURCE_011:72` — previous evidence: 09-11 report: `#1366` merged after his own blocker note; 09-15 report Immediate Attention named `#1373` explicitly

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Merge over his own written blocker -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Hand-written review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:73` — Hand-written review-log commits — 2 today
- [RECOMMENDATION] `SOURCE_011:73` — Script the log from the gate output
- [REPORT_OBSERVATION] `SOURCE_011:73` — previous evidence: 08-24 → 09-15 on every branch

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Hand-written review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Promotion PRs with bodies `uat update` / `main update`

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:101` — Promotion PRs with bodies `uat update` / `main update`
- [RECOMMENDATION] `SOURCE_011:101` — Automate with Devin — generate the release manifest + gate verdicts into the body

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Promotion PRs with bodies `uat update` / `main update` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Bulk-closing Devin QA/fix PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:102` — Bulk-closing Devin QA/fix PRs
- [RECOMMENDATION] `SOURCE_011:102` — Improve documentation/process — decide a retention rule; close with a one-line disposition

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Bulk-closing Devin QA/fix PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` `act()`/jest housekeeping

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:103` — `act()`/jest housekeeping
- [RECOMMENDATION] `SOURCE_011:103` — Automate with Devin — well-scoped, test-verifiable

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- `act()`/jest housekeeping -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Release-manifest generator for dev→uat→main PRs (commits, PRs, open QA findings) so an empty-body approval is at least approving something legible.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:106` — Release-manifest generator for dev→uat→main PRs (commits, PRs, open QA findings) so an empty-body approval is at least approving something legible.

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Release-manifest generator for dev→uat→main PRs (commits, PRs, open QA findings) so an empty-body approval is at least approving something legible. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` A `dev` CI job that builds every `Dockerfile.` (the hook added in `#1382` only catches undeclared imports).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:107` — A `dev` CI job that builds every `Dockerfile.` (the hook added in `#1382` only catches undeclared imports).

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- A `dev` CI job that builds every `Dockerfile.` (the hook added in `#1382` only catches undeclared imports). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Re-open or re-delegate the fixes from `#1369`/`#1371` with the QA findings as ACs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:108` — Re-open or re-delegate the fixes from `#1369`/`#1371` with the QA findings as ACs.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Re-open or re-delegate the fixes from `#1369`/`#1371` with the QA findings as ACs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Promotion PRs with no body, empty approvals

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:127` — Promotion PRs with no body, empty approvals — `#1375`/`#1377`/`#1378`/`#1383`/`#1384` today; `#1378` broke prod build
- [RECOMMENDATION] `SOURCE_011:127` — Manifest in body; require the QA gate verdicts of included PRs to be linked
- [REPORT_OBSERVATION] `SOURCE_011:127` — previous evidence: Every dev→uat→main this month (09-05, 09-10, 09-12 reports)

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Promotion PRs with no body, empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Remediate a peer's PR, then approve and merge it yourself

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:128` — Remediate a peer's PR, then approve and merge it yourself — `#1364`: 12 own commits → 10k review → self-approve → merge, 2 new Devin findings open
- [RECOMMENDATION] `SOURCE_011:128` — Same branch-protection rule as above
- [REPORT_OBSERVATION] `SOURCE_011:128` — previous evidence: Flagged 09-12/09-15 for SaijyotiMeti and akanksh; team-level Repeat Issue

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Remediate a peer's PR, then approve and merge it yourself -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Repointing deep links / agent tools after route retirements

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:154` — Repointing deep links / agent tools after route retirements
- [RECOMMENDATION] `SOURCE_011:154` — Automate through scripts/tooling — a route-reference grep in CI

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Repointing deep links / agent tools after route retirements -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Dark-mode token adjustments

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:155` — Dark-mode token adjustments
- [RECOMMENDATION] `SOURCE_011:155` — Improve documentation/process — token table in `frontend.mdc`

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Dark-mode token adjustments -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Split `#1380` into a reviewable stack; ask Devin to run `nx test`/`typecheck` per layer and report.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:158` — Split `#1380` into a reviewable stack; ask Devin to run `nx test`/`typecheck` per layer and report.

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Split `#1380` into a reviewable stack; ask Devin to run `nx test`/`typecheck` per layer and report. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Regression e2e for the retired `/hr/pipeline` links (every consumer that was repointed).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:159` — Regression e2e for the retired `/hr/pipeline` links (every consumer that was repointed).

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Regression e2e for the retired `/hr/pipeline` links (every consumer that was repointed). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Close or hand `#1365` to a reviewer — a Devin PR nobody owns is negative leverage.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:160` — Close or hand `#1365` to a reviewer — a Devin PR nobody owns is negative leverage.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Close or hand `#1365` to a reviewer — a Devin PR nobody owns is negative leverage. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Oversized PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:179` — Oversized PR — `#1380` 385 files
- [RECOMMENDATION] `SOURCE_011:179` — Stack it; agree a 100-file ceiling for HR work
- [REPORT_OBSERVATION] `SOURCE_011:179` — previous evidence: 09-05 → 09-12 reports: 300+-file PRs from him

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Oversized PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Devin PR with no reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:180` — Devin PR with no reviewer — still no reviewer
- [RECOMMENDATION] `SOURCE_011:180` — Own it or close it
- [REPORT_OBSERVATION] `SOURCE_011:180` — previous evidence: `#1365` since 09-11

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Devin PR with no reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` PRD add + reconcile commit with each feature branch

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:204` — PRD add + reconcile commit with each feature branch
- [RECOMMENDATION] `SOURCE_011:204` — Continue manually — this is the design record; keep it

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- PRD add + reconcile commit with each feature branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Fixture-type fixes after payload changes

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:205` — Fixture-type fixes after payload changes
- [RECOMMENDATION] `SOURCE_011:205` — Automate with Devin — typed fixture factories

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Fixture-type fixes after payload changes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` e2e + unit coverage for attach-to-step and `completeStepOnSatisfy` before the PR opens.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:208` — e2e + unit coverage for attach-to-step and `completeStepOnSatisfy` before the PR opens.

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- e2e + unit coverage for attach-to-step and `completeStepOnSatisfy` before the PR opens. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Delegate the `#1372` C-1..C-4 answers as an investigation with the four config keys as ACs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:209` — Delegate the `#1372` C-1..C-4 answers as an investigation with the four config keys as ACs.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Delegate the `#1372` C-1..C-4 answers as an investigation with the four config keys as ACs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` (none meeting the four-part test today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:226` — (none meeting the four-part test today) — no merge today
- [RECOMMENDATION] `SOURCE_011:226` — Watch the `questionnaire-chase-attachment` PR for the same sequence
- [REPORT_OBSERVATION] `SOURCE_011:226` — previous evidence: `#1367` remediate-then-approve (09-15)

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- (none meeting the four-part test today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Empty approvals on promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:251` — Empty approvals on promotion PRs
- [RECOMMENDATION] `SOURCE_011:251` — Improve documentation/process — approval must name the gate verdicts checked

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Empty approvals on promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Prod hotfix after promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:252` — Prod hotfix after promotion
- [RECOMMENDATION] `SOURCE_011:252` — Automate through scripts/tooling — Docker build of each app on `dev`

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Prod hotfix after promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` CI job building all `Dockerfile.` on `dev`/`uat` before promotion.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:255` — CI job building all `Dockerfile.` on `dev`/`uat` before promotion.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- CI job building all `Dockerfile.` on `dev`/`uat` before promotion. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Fix the red `formatDayLabel` spec (deterministic month abbreviations) — scoped, test-verifiable.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:256` — Fix the red `formatDayLabel` spec (deterministic month abbreviations) — scoped, test-verifiable.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Fix the red `formatDayLabel` spec (deterministic month abbreviations) — scoped, test-verifiable. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Empty approvals on 500+-file promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:273` — Empty approvals on 500+-file promotions — `#1375`, `#1378` today; `#1378` broke prod
- [RECOMMENDATION] `SOURCE_011:273` — Approval comment must list the QA verdicts of included PRs; block promotion with an open NOT READY
- [REPORT_OBSERVATION] `SOURCE_011:273` — previous evidence: 09-05, 09-10, 09-12 reports

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Empty approvals on 500+-file promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:294` — —
- [RECOMMENDATION] `SOURCE_011:294` — —
- [REPORT_OBSERVATION] `SOURCE_011:310` — — — —
- [RECOMMENDATION] `SOURCE_011:310` — —
- [REPORT_OBSERVATION] `SOURCE_011:310` — previous evidence: —

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` If `#1360` is still needed, re-scope it as a Devin task with the orphan-checklist audit count as the AC.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:297` — If `#1360` is still needed, re-scope it as a Devin task with the orphan-checklist audit count as the AC.

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- If `#1360` is still needed, re-scope it as a Devin task with the orphan-checklist audit count as the AC. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Fix-after-Devin-finding commits on validators/coercion

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:337` — Fix-after-Devin-finding commits on validators/coercion
- [RECOMMENDATION] `SOURCE_011:337` — Automate with Devin — zod schema tests for every route

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Fix-after-Devin-finding commits on validators/coercion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Open → approve → merge within 1–3 min

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:338` — Open → approve → merge within 1–3 min
- [RECOMMENDATION] `SOURCE_011:338` — Improve documentation/process — minimum soak for Devin Review to finish

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Open → approve → merge within 1–3 min -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Regression tests for batch-run creation (`retry_of`, null/zero coercion, import find-or-create bypass).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:341` — Regression tests for batch-run creation (`retry_of`, null/zero coercion, import find-or-create bypass).

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Regression tests for batch-run creation (`retry_of`, null/zero coercion, import find-or-create bypass). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Excel export snapshot tests (header dedupe).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:342` — Excel export snapshot tests (header dedupe).

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Excel export snapshot tests (header dedupe). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Merge within minutes of opening, empty approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:356` — Merge within minutes of opening, empty approval — 4 today; one reverted
- [RECOMMENDATION] `SOURCE_011:356` — Require nodejs test run in CI before merge to `Dev_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:356` — previous evidence: 09-0x/09-1x reports (amit approvals)

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Merge within minutes of opening, empty approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Empty approve + merge of Jatin's PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:377` — Empty approve + merge of Jatin's PRs
- [RECOMMENDATION] `SOURCE_011:377` — Improve documentation/process — one line naming what was checked

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Empty approve + merge of Jatin's PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Ask Devin Review for a per-PR "reviewer checklist" digest and paste the checked items into the approval.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:380` — Ask Devin Review for a per-PR "reviewer checklist" digest and paste the checked items into the approval.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Ask Devin Review for a per-PR "reviewer checklist" digest and paste the checked items into the approval. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:393` — Empty approvals — 4 today
- [RECOMMENDATION] `SOURCE_011:393` — Named checks in approval; CI test gate
- [REPORT_OBSERVATION] `SOURCE_011:393` — previous evidence: 08-2x → 09-12 reports

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Long-lived branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:414` — Long-lived branch without PR
- [RECOMMENDATION] `SOURCE_011:414` — Improve documentation/process — draft PR now

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Long-lived branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Test fixtures for inpatient charts (empty text, disputed body part).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:417` — Test fixtures for inpatient charts (empty text, disputed body part).

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Test fixtures for inpatient charts (empty text, disputed body part). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` `feat/inpatient-engine` without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:430` — `feat/inpatient-engine` without PR — 4 more commits, still no PR
- [RECOMMENDATION] `SOURCE_011:430` — Open a draft PR this week
- [REPORT_OBSERVATION] `SOURCE_011:430` — previous evidence: 9 prior reports

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- `feat/inpatient-engine` without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` PRs to `uat` with no human reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:451` — PRs to `uat` with no human reviewer
- [RECOMMENDATION] `SOURCE_011:451` — Improve documentation/process — assign a reviewer on open

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- PRs to `uat` with no human reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Unit tests for the scope-list validator and the guideline loader.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:454` — Unit tests for the scope-list validator and the guideline loader.

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Unit tests for the scope-list validator and the guideline loader. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` `uat`-targeted PR without reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:467` — `uat`-targeted PR without reviewer — `#452`
- [RECOMMENDATION] `SOURCE_011:467` — Reviewer on open
- [REPORT_OBSERVATION] `SOURCE_011:467` — previous evidence: `#435` (09-10 → )

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- `uat`-targeted PR without reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

