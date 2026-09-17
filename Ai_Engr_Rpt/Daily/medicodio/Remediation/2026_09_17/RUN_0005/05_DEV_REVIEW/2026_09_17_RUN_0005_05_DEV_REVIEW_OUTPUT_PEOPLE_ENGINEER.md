# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-17 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_17_Employee_Rating_Cards.md, 2026_09_17_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written architect/PR review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:54` — Hand-written architect/PR review-log commits
- [RECOMMENDATION] `SOURCE_011:54` — Automate with Devin — generate the log from the review comment + commit list

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written architect/PR review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` "Repair N broken specs surfaced by the scoped gate"

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:55` — "Repair N broken specs surfaced by the scoped gate"
- [RECOMMENDATION] `SOURCE_011:55` — Automate with Devin — run the scoped gate on the branch before review and open a fix PR

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- "Repair N broken specs surfaced by the scoped gate" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` PRD/atlas/doc reconciliation after code lands

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:56` — PRD/atlas/doc reconciliation after code lands
- [RECOMMENDATION] `SOURCE_011:56` — Automate through scripts/tooling (doc-drift check in CI)

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- PRD/atlas/doc reconciliation after code lands -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate the `#1380` QA gate's two open items (locate the send-reminder durable record; refresh `E2E_FIRM2_`/`E2E_RBAC_`) as a scoped Devin session with the QA 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — Delegate the `#1380` QA gate's two open items (locate the send-reminder durable record; refresh `E2E_FIRM2_`/`E2E_RBAC_`) as a scoped Devin session with the QA report as acceptance criteria.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate the `#1380` QA gate's two open items (locate the send-reminder durable record; refresh `E2E_FIRM2_`/`E2E_RBAC_`) as a scoped Devin session with the QA  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Have Devin answer/triage the 9 `#1389` findings with tests before a human reviewer is asked.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Have Devin answer/triage the 9 `#1389` findings with tests before a human reviewer is asked.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Have Devin answer/triage the 9 `#1389` findings with tests before a human reviewer is asked. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Pre-review scoped test gate as a Devin check so spec repair is not done by the reviewer.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Pre-review scoped test gate as a Devin check so spec repair is not done by the reviewer.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Pre-review scoped test gate as a Devin check so spec repair is not done by the reviewer. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Reviewer remediates, then approves and merges the same PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:80` — Reviewer remediates, then approves and merges the same PR — `#1380`: 32 commits → APPROVE WITH NITS → `approved` → own merge, 6 min
- [RECOMMENDATION] `SOURCE_011:80` — Branch protection: an approver with commits on the branch cannot be the merging approver
- [REPORT_OBSERVATION] `SOURCE_011:80` — previous evidence: `#1260` (08-30), `#1367` (09-14: 20 commits → 8-char `approved` → own merge)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Reviewer remediates, then approves and merges the same PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Own `[needs decision]` left open at merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:81` — Own `[needs decision]` left open at merge — `#1380` decision #1 (`DROP COLUMN` bypasses safety hook)
- [RECOMMENDATION] `SOURCE_011:81` — Decision recorded in the PR before merge, or PR held
- [REPORT_OBSERVATION] `SOURCE_011:81` — previous evidence: `#1367` "pending 2 schema index decisions"

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Own `[needs decision]` left open at merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` `chore(atlas)` regeneration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:113` — `chore(atlas)` regeneration
- [RECOMMENDATION] `SOURCE_011:113` — Automate through scripts/tooling — CI job on `dev`

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- `chore(atlas)` regeneration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Review-log + standards-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Review-log + standards-log commits
- [RECOMMENDATION] `SOURCE_011:114` — Automate with Devin

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Review-log + standards-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Closing Devin fix/report PRs without a note

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:115` — Closing Devin fix/report PRs without a note
- [RECOMMENDATION] `SOURCE_011:115` — Improve documentation/process — one-line disposition required

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Closing Devin fix/report PRs without a note -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Run the `20260915000000_entity_status_phase1` migration + full Jest on a hosted dev clone and post the result on `#1386` before review.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Run the `20260915000000_entity_status_phase1` migration + full Jest on a hosted dev clone and post the result on `#1386` before review.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Run the `20260915000000_entity_status_phase1` migration + full Jest on a hosted dev clone and post the result on `#1386` before review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Regenerate the atlas on merge to `dev` (removes a daily manual commit for him, akanksh and Saijyoti).

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:119` — Regenerate the atlas on merge to `dev` (removes a daily manual commit for him, akanksh and Saijyoti).

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Regenerate the atlas on merge to `dev` (removes a daily manual commit for him, akanksh and Saijyoti). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Disposition sweep: for `#1358/#1360/#1369/#1371` produce a table of "fix lives in commit X / superseded / still open".

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:120` — Disposition sweep: for `#1358/#1360/#1369/#1371` produce a table of "fix lives in commit X / superseded / still open".

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Disposition sweep: for `#1358/#1360/#1369/#1371` produce a table of "fix lives in commit X / superseded / still open". -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Devin fix PRs for confirmed failures closed without disposition

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:139` — Devin fix PRs for confirmed failures closed without disposition — `#1358` (5 PRODUCT_FAILUREs from `#1316`) closed 10:17
- [RECOMMENDATION] `SOURCE_011:139` — Comment on each with where the fix lives
- [REPORT_OBSERVATION] `SOURCE_011:139` — previous evidence: `#1360/#1369/#1371` (09-15)

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Devin fix PRs for confirmed failures closed without disposition -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` >200-file feature PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:140` — >200-file feature PRs — `#1386` 234 files
- [RECOMMENDATION] `SOURCE_011:140` — Stack: schema → guard → API → web
- [REPORT_OBSERVATION] `SOURCE_011:140` — previous evidence: `#1250`, `#1363`

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- >200-file feature PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Post-merge findings left undispositioned

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:141` — Post-merge findings left undispositioned — still open
- [RECOMMENDATION] `SOURCE_011:141` — Owner + date in the QA thread
- [REPORT_OBSERVATION] `SOURCE_011:141` — previous evidence: `#1363` F-6/F-1 (09-15)

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Post-merge findings left undispositioned -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Doc sync after code change (`docs(architecture)`, `docs(ops)`, `docs(tracking)`)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:170` — Doc sync after code change (`docs(architecture)`, `docs(ops)`, `docs(tracking)`)
- [RECOMMENDATION] `SOURCE_011:170` — Automate through scripts/tooling

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Doc sync after code change (`docs(architecture)`, `docs(ops)`, `docs(tracking)`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Spec repairs left by refactors (`ModuleAccessGuard`, `@jest/globals` import)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:171` — Spec repairs left by refactors (`ModuleAccessGuard`, `@jest/globals` import)
- [RECOMMENDATION] `SOURCE_011:171` — Automate with Devin — pre-PR scoped gate

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Spec repairs left by refactors (`ModuleAccessGuard`, `@jest/globals` import) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Re-open the timezone work as a stack of Devin PRs (schema/selector → formatter → ~130 call sites) with per-stack tests, instead of one squash commit.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:174` — Re-open the timezone work as a stack of Devin PRs (schema/selector → formatter → ~130 call sites) with per-stack tests, instead of one squash commit.

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Re-open the timezone work as a stack of Devin PRs (schema/selector → formatter → ~130 call sites) with per-stack tests, instead of one squash commit. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Delegate the `E2E_FIRM2`/`E2E_RBAC` secret refresh + re-run of the cross-firm attacker probe from the `#1380` QA gate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:175` — Delegate the `E2E_FIRM2`/`E2E_RBAC` secret refresh + re-run of the cross-firm attacker probe from the `#1380` QA gate.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Delegate the `E2E_FIRM2`/`E2E_RBAC` secret refresh + re-run of the cross-firm attacker probe from the `#1380` QA gate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Regression tests for the retired `/hr/pipeline` and health-score routes (deep links, agent tool).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 2 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:176` — Regression tests for the retired `/hr/pipeline` and health-score routes (deep links, agent tool).

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Regression tests for the retired `/hr/pipeline` and health-score routes (deep links, agent tool). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Schema drop inside an oversized feature PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:195` — Schema drop inside an oversized feature PR — `immigration_health_scores` table + enum drop merged inside `#1380`
- [RECOMMENDATION] `SOURCE_011:195` — Schema-change PRs stand alone with their own reviewer
- [REPORT_OBSERVATION] `SOURCE_011:195` — previous evidence: 09-16 report: "split the schema drop out of `#1380`"

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Schema drop inside an oversized feature PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Devin PR on his branch never reviewed

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:196` — Devin PR on his branch never reviewed — closed unmerged, work re-pushed as one untraced commit
- [RECOMMENDATION] `SOURCE_011:196` — Review or explicitly reject Devin PRs within 2 days; never squash away authorship
- [REPORT_OBSERVATION] `SOURCE_011:196` — previous evidence: `#1365` unreviewed 09-11 → 09-15 (5 reports)

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Devin PR on his branch never reviewed -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Atlas regeneration commit

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:222` — Atlas regeneration commit
- [RECOMMENDATION] `SOURCE_011:222` — Automate through scripts/tooling

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Atlas regeneration commit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Delegate the `#1373` §4.4 correction script + UAT/prod counts.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:225` — Delegate the `#1373` §4.4 correction script + UAT/prod counts.

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Delegate the `#1373` §4.4 correction script + UAT/prod counts. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Atlas regeneration as CI.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:226` — Atlas regeneration as CI.

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Atlas regeneration as CI. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` `#1373` NEEDS-DECISION items open in production

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:244` — `#1373` NEEDS-DECISION items open in production — no comment 09-16
- [RECOMMENDATION] `SOURCE_011:244` — Post resolutions or name the decider today
- [REPORT_OBSERVATION] `SOURCE_011:244` — previous evidence: 09-15 (merge), 09-16 (promoted, flagged)

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- `#1373` NEEDS-DECISION items open in production -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` `dev -> uat` promotion PRs with badge-only bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:272` — `dev -> uat` promotion PRs with badge-only bodies
- [RECOMMENDATION] `SOURCE_011:272` — Automate with Devin — manifest of included PRs + open findings

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- `dev -> uat` promotion PRs with badge-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Empty approvals on peer PRs within 2 min

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:273` — Empty approvals on peer PRs within 2 min
- [RECOMMENDATION] `SOURCE_011:273` — Improve process — name the check performed

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Empty approvals on peer PRs within 2 min -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Regression tests for RLS `current_user_id` scoping (`setRlsOnConnection` callers) — the same class fixed twice this week.

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: TENANT_ISOLATION
- Priority: 10 · Complexity: 10 · Tier: D
- Playbook: ORG_PB_TENANT_ISOLATION_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:276` — Regression tests for RLS `current_user_id` scoping (`setRlsOnConnection` callers) — the same class fixed twice this week.

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Regression tests for RLS `current_user_id` scoping (`setRlsOnConnection` callers) — the same class fixed twice this week. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Promotion manifest generator that lists unresolved Devin findings on the included PRs (would have surfaced the `#646` RLS finding).

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: TENANT_ISOLATION
- Priority: 10 · Complexity: 10 · Tier: D
- Playbook: ORG_PB_TENANT_ISOLATION_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:277` — Promotion manifest generator that lists unresolved Devin findings on the included PRs (would have surfaced the `#646` RLS finding).

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Promotion manifest generator that lists unresolved Devin findings on the included PRs (would have surfaced the `#646` RLS finding). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` A nodejs test run as a required check on `Dev_1.0` (09-16 recommendation, still absent).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:278` — A nodejs test run as a required check on `Dev_1.0` (09-16 recommendation, still absent).

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- A nodejs test run as a required check on `Dev_1.0` (09-16 recommendation, still absent). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Promotion PRs with badge-only bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:297` — Promotion PRs with badge-only bodies — `#646/#653/#576/#579`
- [RECOMMENDATION] `SOURCE_011:297` — Manifest in body
- [REPORT_OBSERVATION] `SOURCE_011:297` — previous evidence: 09-11/09-12 `dev -> uat`

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Promotion PRs with badge-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Unanswered finding at promotion merge

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: TENANT_ISOLATION
- Priority: 10 · Complexity: 10 · Tier: D
- Playbook: ORG_PB_TENANT_ISOLATION_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:298` — Unanswered finding at promotion merge — `#646` RLS-migration BUG open at merge
- [RECOMMENDATION] `SOURCE_011:298` — Block promotion while a BUG finding is open
- [REPORT_OBSERVATION] `SOURCE_011:298` — previous evidence: `#642` revert (09-16, test gap)

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Unanswered finding at promotion merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Empty approvals 1–2 min after Devin Review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:326` — Empty approvals 1–2 min after Devin Review
- [RECOMMENDATION] `SOURCE_011:326` — Improve process — name checks; require test evidence

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Empty approvals 1–2 min after Devin Review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` `Dev_1.0 → Dev_2.0` app sync merges

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:327` — `Dev_1.0 → Dev_2.0` app sync merges
- [RECOMMENDATION] `SOURCE_011:327` — Automate through scripts/tooling (scheduled sync PR)

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- `Dev_1.0 → Dev_2.0` app sync merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Repo-structure doc regeneration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:328` — Repo-structure doc regeneration
- [RECOMMENDATION] `SOURCE_011:328` — Positive — already automated

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Repo-structure doc regeneration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` A pg-backed concurrency test for resolve vs heartbeat (`uq_enc_reviews_active_per_coder`) — would have made one PR of three.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:331` — A pg-backed concurrency test for resolve vs heartbeat (`uq_enc_reviews_active_per_coder`) — would have made one PR of three.

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- A pg-backed concurrency test for resolve vs heartbeat (`uq_enc_reviews_active_per_coder`) — would have made one PR of three. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Scheduled `Dev_1.0 → Dev_2.0` sync PR with conflict report.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:332` — Scheduled `Dev_1.0 → Dev_2.0` sync PR with conflict report.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Scheduled `Dev_1.0 → Dev_2.0` sync PR with conflict report. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` "What to check" digest per PR he approves.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:333` — "What to check" digest per PR he approves.

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- "What to check" digest per PR he approves. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Empty approvals on prod-bound PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:352` — Empty approvals on prod-bound PRs — 12 today
- [RECOMMENDATION] `SOURCE_011:352` — Approval must name the check or CI evidence
- [REPORT_OBSERVATION] `SOURCE_011:352` — previous evidence: 08-27 (20), 09-15 (4)

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Empty approvals on prod-bound PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Iterative "close N defects found in review" commits

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:379` — Iterative "close N defects found in review" commits
- [RECOMMENDATION] `SOURCE_011:379` — Continue manually — this is correct review response

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Iterative "close N defects found in review" commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Generate the PR bodies from his commit narrative (Why/What/Risk/Rollback).

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:382` — Generate the PR bodies from his commit narrative (Why/What/Risk/Rollback).

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Generate the PR bodies from his commit narrative (Why/What/Risk/Rollback). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Money-path property tests (invoice totals, fee recomputation) Devin Review probed three times.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 5 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:383` — Money-path property tests (invoice totals, fee recomputation) Devin Review probed three times.

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Money-path property tests (invoice totals, fee recomputation) Devin Review probed three times. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Split `#652` into schema → services → scripts stacks.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:384` — Split `#652` into schema → services → scripts stacks.

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Split `#652` into schema → services → scripts stacks. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:402` — — — badge-only bodies on 300-file PRs
- [RECOMMENDATION] `SOURCE_011:402` — Body before reviewer request
- [REPORT_OBSERVATION] `SOURCE_011:402` — previous evidence: none

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Long-lived branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:427` — Long-lived branch without PR
- [RECOMMENDATION] `SOURCE_011:427` — Improve documentation/process — draft PR on first push

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Long-lived branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Open a draft PR in `Dev_2.0` and let Devin Review run on the port.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:430` — Open a draft PR in `Dev_2.0` and let Devin Review run on the port.

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Open a draft PR in `Dev_2.0` and let Devin Review run on the port. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Inpatient chart fixture generation.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:431` — Inpatient chart fixture generation.

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Inpatient chart fixture generation. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:449` — Branch without PR — 11th; branch moved repos
- [RECOMMENDATION] `SOURCE_011:449` — Draft PR today
- [REPORT_OBSERVATION] `SOURCE_011:449` — previous evidence: 10 reports (09-05 → 09-16)

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` `UAT TO PROD` PRs with template bodies

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:474` — `UAT TO PROD` PRs with template bodies
- [RECOMMENDATION] `SOURCE_011:474` — Automate with Devin — manifest + open-findings list

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- `UAT TO PROD` PRs with template bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Unit tests for the stage-4 exclusion loader (the prod revert was a `TypeError` class Devin flagged).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:477` — Unit tests for the stage-4 exclusion loader (the prod revert was a `TypeError` class Devin flagged).

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Unit tests for the stage-4 exclusion loader (the prod revert was a `TypeError` class Devin flagged). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Pre-promotion check running the linking suite.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:478` — Pre-promotion check running the linking suite.

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Pre-promotion check running the linking suite. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` `uat`/prod PRs with no substantive human review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:496` — `uat`/prod PRs with no substantive human review — `#453`, `#455`, `#458`
- [RECOMMENDATION] `SOURCE_011:496` — Named reviewer; findings answered before prod
- [REPORT_OBSERVATION] `SOURCE_011:496` — previous evidence: `#435` (09-08), `#452` (09-15)

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- `uat`/prod PRs with no substantive human review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` One-word approvals on prod promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:522` — One-word approvals on prod promotions
- [RECOMMENDATION] `SOURCE_011:522` — Improve process

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- One-word approvals on prod promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Manual revert / revert-of-revert PRs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:523` — Manual revert / revert-of-revert PRs
- [RECOMMENDATION] `SOURCE_011:523` — Automate through scripts/tooling (rollback script with reason)

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Manual revert / revert-of-revert PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Rollback runbook + script.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:526` — Rollback runbook + script.

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Rollback runbook + script. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Consistency-POC evaluation harness (bounded, data-driven) once the POC design is fixed — Possible Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:527` — Consistency-POC evaluation harness (bounded, data-driven) once the POC design is fixed — Possible Devin Candidate.

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Consistency-POC evaluation harness (bounded, data-driven) once the POC design is fixed — Possible Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` One-word approvals on prod promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:545` — One-word approvals on prod promotions — `#453`, `#456`
- [RECOMMENDATION] `SOURCE_011:545` — Approval names the check
- [REPORT_OBSERVATION] `SOURCE_011:545` — previous evidence: 08-27, 09-06

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- One-word approvals on prod promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Self-merged PRs with empty bodies

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:570` — Self-merged PRs with empty bodies
- [RECOMMENDATION] `SOURCE_011:570` — Improve process — second approver

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Self-merged PRs with empty bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Enable Devin Review on the repo.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:573` — Enable Devin Review on the repo.

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Enable Devin Review on the repo. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` PR body generation from diff.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:574` — PR body generation from diff.

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- PR body generation from diff. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:592` — — — self-merge, empty body
- [RECOMMENDATION] `SOURCE_011:592` — Baseline recorded
- [REPORT_OBSERVATION] `SOURCE_011:592` — previous evidence: none (no history)

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` ragha82: delegate the `date-helpers` spec fix (one-line, confirmed by QA).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:617` — ragha82: delegate the `date-helpers` spec fix (one-line, confirmed by QA).

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- ragha82: delegate the `date-helpers` spec fix (one-line, confirmed by QA). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Post-merge QA finding unaddressed (ragha82)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:635` — Post-merge QA finding unaddressed (ragha82) — still red
- [RECOMMENDATION] `SOURCE_011:635` — Fix or delegate today
- [REPORT_OBSERVATION] `SOURCE_011:635` — previous evidence: `#1382` red spec (09-15/16)

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Post-merge QA finding unaddressed (ragha82) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

