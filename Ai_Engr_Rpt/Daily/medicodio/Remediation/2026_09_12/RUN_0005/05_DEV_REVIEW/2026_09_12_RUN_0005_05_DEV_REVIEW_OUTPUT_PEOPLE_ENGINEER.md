# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-12 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Header / PRD-status / review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:55` — Header / PRD-status / review-log commits
- [RECOMMENDATION] `SOURCE_011:55` — Automate with Devin — generate from diff + gate output

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Header / PRD-status / review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` dev→uat→main promotion PRs with template body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:56` — dev→uat→main promotion PRs with template body
- [RECOMMENDATION] `SOURCE_011:56` — Automate through scripts/tooling — pipeline promotion with Devin Review as required check

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- dev→uat→main promotion PRs with template body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Lockfile churn undo (`fix(deps): restore the minimal lockfile`, `revert the package.json export-map re-sort`)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:57` — Lockfile churn undo (`fix(deps): restore the minimal lockfile`, `revert the package.json export-map re-sort`)
- [RECOMMENDATION] `SOURCE_011:57` — Improve documentation/process — lockfile-only commits, lint rule

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Lockfile churn undo (`fix(deps): restore the minimal lockfile`, `revert the package.json export-map re-sort`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Devin-generated regression tests for the cookie/CSRF auth path — five session-correctness defects were found and fixed in one commit at 16:42; each should be pi

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Devin-generated regression tests for the cookie/CSRF auth path — five session-correctness defects were found and fixed in one commit at 16:42; each should be pinned.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Devin-generated regression tests for the cookie/CSRF auth path — five session-correctness defects were found and fixed in one commit at 16:42; each should be pi -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the 16 still-open Devin findings on `#1363` as a bounded remediation batch, with anirudh reviewing rather than fixing.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Delegate the 16 still-open Devin findings on `#1363` as a bounded remediation batch, with anirudh reviewing rather than fixing.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the 16 still-open Devin findings on `#1363` as a bounded remediation batch, with anirudh reviewing rather than fixing. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Devin drafts the release note for `#1361` (647 commits to `main`) — currently the body is the untouched template.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:62` — Devin drafts the release note for `#1361` (647 commits to `main`) — currently the body is the untouched template.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Devin drafts the release note for `#1361` (647 commits to `main`) — currently the body is the untouched template. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` None recurring today — 09-11 Repeat Patterns (REQUEST CHANGES → own approve; remediate-approve-merge) did not occur

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:82` — None recurring today — 09-11 Repeat Patterns (REQUEST CHANGES → own approve; remediate-approve-merge) did not occur — No review-then-merge event today
- [RECOMMENDATION] `SOURCE_011:82` — Keep it that way; the next test is who approves `#1363`
- [REPORT_OBSERVATION] `SOURCE_011:82` — previous evidence: 09-11 `#1323`, `#1349`

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- None recurring today — 09-11 Repeat Patterns (REQUEST CHANGES → own approve; remediate-approve-merge) did not occur -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` `docs(review-logs)` / tech-debt ledgers

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:109` — `docs(review-logs)` / tech-debt ledgers
- [RECOMMENDATION] `SOURCE_011:109` — Automate with Devin — Devin already reads them (23:11 resolutions cite the log)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- `docs(review-logs)` / tech-debt ledgers -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Restoring review-log files overwritten by a merge (2 commits)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:110` — Restoring review-log files overwritten by a merge (2 commits)
- [RECOMMENDATION] `SOURCE_011:110` — Automate through scripts/tooling — one file per PR, never edited in place

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Restoring review-log files overwritten by a merge (2 commits) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Remediating other authors' PRs to merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:111` — Remediating other authors' PRs to merge
- [RECOMMENDATION] `SOURCE_011:111` — Improve documentation/process — hand-over recorded, second approver

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Remediating other authors' PRs to merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Run the Devin QA gate on the `#1366` branch before merge — two consecutive post-merge NOT READY verdicts (`#1316`, `#1322`) each produced a Devin fix PR that a 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Run the Devin QA gate on the `#1366` branch before merge — two consecutive post-merge NOT READY verdicts (`#1316`, `#1322`) each produced a Devin fix PR that a human then had to review.

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Run the Devin QA gate on the `#1366` branch before merge — two consecutive post-merge NOT READY verdicts (`#1316`, `#1322`) each produced a Devin fix PR that a  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Delegate the standards-audit fix list (header corrections, unused imports, stacking-context isolation) to Devin; keep herself on the Architect+EM review.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:115` — Delegate the standards-audit fix list (header corrections, unused imports, stacking-context isolation) to Devin; keep herself on the Architect+EM review.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Delegate the standards-audit fix list (header corrections, unused imports, stacking-context isolation) to Devin; keep herself on the Architect+EM review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Have Devin generate the review-log ledger from the gate run instead of hand-writing it.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:116` — Have Devin generate the review-log ledger from the gate run instead of hand-writing it.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Have Devin generate the review-log ledger from the gate run instead of hand-writing it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Repeat Pattern: reviewer remediates, approves and merges the same PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:136` — Repeat Pattern: reviewer remediates, approves and merges the same PR — `#1322` (16 own commits, 6.3k review, approve, merge)
- [RECOMMENDATION] `SOURCE_011:136` — Second approver on any PR she has pushed >5 commits to
- [REPORT_OBSERVATION] `SOURCE_011:136` — previous evidence: 09-11 `#1337`, `#1331`, `#1316`; 09-10 `#1342`, `#1336`

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Repeat Pattern: reviewer remediates, approves and merges the same PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Repeat Pattern: QA gate runs after merge and returns NOT READY

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:137` — Repeat Pattern: QA gate runs after merge and returns NOT READY — `#1322` 55/100, 2 PRODUCT_FAILUREs, fix PR `#1369`
- [RECOMMENDATION] `SOURCE_011:137` — Gate on branch before merge for PRs >50 files
- [REPORT_OBSERVATION] `SOURCE_011:137` — previous evidence: 09-11 `#1316` (5 PRODUCT_FAILUREs), `#1350`

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Repeat Pattern: QA gate runs after merge and returns NOT READY -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` PRD/changelog reconciliation ("reconcile the PRDs with what shipped")

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:164` — PRD/changelog reconciliation ("reconcile the PRDs with what shipped")
- [RECOMMENDATION] `SOURCE_011:164` — Automate with Devin

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- PRD/changelog reconciliation ("reconcile the PRDs with what shipped") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Review-log ledgers (2 today)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:165` — Review-log ledgers (2 today)
- [RECOMMENDATION] `SOURCE_011:165` — Automate with Devin

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Review-log ledgers (2 today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Merging `dev` into feature branch (2 today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:166` — Merging `dev` into feature branch (2 today)
- [RECOMMENDATION] `SOURCE_011:166` — Continue manually

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Merging `dev` into feature branch (2 today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Delegate the 3 SEC + 3 BUG findings on `#1367` to Devin with acceptance tests, then review the diff — the surface (reading client email, proposing actions) warr

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:169` — Delegate the 3 SEC + 3 BUG findings on `#1367` to Devin with acceptance tests, then review the diff — the surface (reading client email, proposing actions) warrants a written disposition per SEC finding.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Delegate the 3 SEC + 3 BUG findings on `#1367` to Devin with acceptance tests, then review the diff — the surface (reading client email, proposing actions) warr -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Devin writes the e2e regression pack from the "nine defects" list.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:170` — Devin writes the e2e regression pack from the "nine defects" list.

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Devin writes the e2e regression pack from the "nine defects" list. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Repeat Pattern: remediator on another author's PR (approve/merge half did not occur today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:189` — Repeat Pattern: remediator on another author's PR (approve/merge half did not occur today) — `#1366` 22 fixes; no approval yet
- [RECOMMENDATION] `SOURCE_011:189` — Do not be the approver on `#1366`
- [REPORT_OBSERVATION] `SOURCE_011:189` — previous evidence: 09-11 `#1350` (23 fixes → approve → merge); 09-10 `#1338`

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Repeat Pattern: remediator on another author's PR (approve/merge half did not occur today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Timestamp-display migration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:215` — Timestamp-display migration
- [RECOMMENDATION] `SOURCE_011:215` — Automate with Devin — done today

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Timestamp-display migration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Role/permission matrix moves between portals (3 `refactor(` commits)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 6 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:216` — Role/permission matrix moves between portals (3 `refactor(` commits)
- [RECOMMENDATION] `SOURCE_011:216` — Possible Devin Candidate after the schema decision

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Role/permission matrix moves between portals (3 `refactor(` commits) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Merging `dev` into `feat/hr-portal-revamp`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:217` — Merging `dev` into `feat/hr-portal-revamp`
- [RECOMMENDATION] `SOURCE_011:217` — Continue manually

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Merging `dev` into `feat/hr-portal-revamp` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Open `feat/hr-portal-revamp` as a draft PR so the same finding→fix loop that worked on `#1365` runs on ~7k lines of HR role/permission code (security-relevant).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:220` — Open `feat/hr-portal-revamp` as a draft PR so the same finding→fix loop that worked on `#1365` runs on ~7k lines of HR role/permission code (security-relevant).

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Open `feat/hr-portal-revamp` as a draft PR so the same finding→fix loop that worked on `#1365` runs on ~7k lines of HR role/permission code (security-relevant). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Devin generates permission-matrix tests for the HR implicit baseline ("let an employee through without one").

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:221` — Devin generates permission-matrix tests for the HR implicit baseline ("let an employee through without one").

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Devin generates permission-matrix tests for the HR implicit baseline ("let an employee through without one"). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Emerging (not yet Repeat): `feat/hr-portal-revamp` without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:240` — Emerging (not yet Repeat): `feat/hr-portal-revamp` without a PR — 19 more commits, no PR
- [RECOMMENDATION] `SOURCE_011:240` — Draft PR tomorrow; becomes a Repeat Pattern if absent on 09-13
- [REPORT_OBSERVATION] `SOURCE_011:240` — previous evidence: 09-11 report recommended a draft PR

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Emerging (not yet Repeat): `feat/hr-portal-revamp` without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Spec-mock repairs "so tests reach the code they name"

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:265` — Spec-mock repairs "so tests reach the code they name"
- [RECOMMENDATION] `SOURCE_011:265` — Automate with Devin

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Spec-mock repairs "so tests reach the code they name" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` React duplicate-key / label-as-key fixes

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:266` — React duplicate-key / label-as-key fixes
- [RECOMMENDATION] `SOURCE_011:266` — Automate with Devin — lint rule + sweep

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- React duplicate-key / label-as-key fixes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Devin sweeps `apps/web` for other components keyed by display label (the `#1364` body says "A label is …" not unique) — same shape as the timezone sweep.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:269` — Devin sweeps `apps/web` for other components keyed by display label (the `#1364` body says "A label is …" not unique) — same shape as the timezone sweep.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Devin sweeps `apps/web` for other components keyed by display label (the `#1364` body says "A label is …" not unique) — same shape as the timezone sweep. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Delegate the 2 open audit-SQL findings on `#1360`.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:270` — Delegate the 2 open audit-SQL findings on `#1360`.

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Delegate the 2 open audit-SQL findings on `#1360`. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` None meeting the recurrence bar

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:289` — None meeting the recurrence bar — —
- [RECOMMENDATION] `SOURCE_011:289` — —
- [REPORT_OBSERVATION] `SOURCE_011:289` — previous evidence: —
- [REPORT_OBSERVATION] `SOURCE_011:338` — None meeting the recurrence bar — —
- [RECOMMENDATION] `SOURCE_011:338` — —
- [REPORT_OBSERVATION] `SOURCE_011:338` — previous evidence: —

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- None meeting the recurrence bar -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Approving promotion PRs 0-char (`#1361` today)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:315` — Approving promotion PRs 0-char (`#1361` today)
- [RECOMMENDATION] `SOURCE_011:315` — Improve documentation/process — approval names what was checked

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Approving promotion PRs 0-char (`#1361` today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Change digest + test plan per merged PR

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:316` — Change digest + test plan per merged PR
- [RECOMMENDATION] `SOURCE_011:316` — Automate with Devin — Devin produced `#1368` today

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Change digest + test plan per merged PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Devin adds a dry-run test for `acr-purge.sh` (live-revision guard) before it runs against the registry.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:319` — Devin adds a dry-run test for `acr-purge.sh` (live-revision guard) before it runs against the registry.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Devin adds a dry-run test for `acr-purge.sh` (live-revision guard) before it runs against the registry. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Formalise the split observed today: Devin writes the QA digest (`#1368`), ragha82 adjudicates.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:320` — Formalise the split observed today: Devin writes the QA digest (`#1368`), ragha82 adjudicates.

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Formalise the split observed today: Devin writes the QA digest (`#1368`), ragha82 adjudicates. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Insufficient data

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:361` — Insufficient data
- [RECOMMENDATION] `SOURCE_011:361` — —
- [REPORT_OBSERVATION] `SOURCE_011:403` — Insufficient data
- [RECOMMENDATION] `SOURCE_011:403` — —

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Insufficient data -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Review `#1358` — the failures are in surfaces this author built.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:364` — Review `#1358` — the failures are in surfaces this author built.

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Review `#1358` — the failures are in surfaces this author built. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Repeat Pattern: absent from follow-up on own PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:382` — Repeat Pattern: absent from follow-up on own PRs — `#1358` untouched; `#1331` legal-content decisions still unposted
- [RECOMMENDATION] `SOURCE_011:382` — Post the 5 `#1331` decisions; review `#1358`
- [REPORT_OBSERVATION] `SOURCE_011:382` — previous evidence: 09-11 (`#1316`, `#1331` remediated by reviewer)

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Repeat Pattern: absent from follow-up on own PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Review `#1369` (2 fixes to his feature) — it needs "a human call" per Devin's own comment on the size-0 semantics.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:406` — Review `#1369` (2 fixes to his feature) — it needs "a human call" per Devin's own comment on the size-0 semantics.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Review `#1369` (2 fixes to his feature) — it needs "a human call" per Devin's own comment on the size-0 semantics. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Repeat Pattern: long-open PR advanced to merge by others

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:424` — Repeat Pattern: long-open PR advanced to merge by others — `#1322` merged with 24 colleague commits, 0 author commits since 09-07
- [RECOMMENDATION] `SOURCE_011:424` — Manager to confirm ownership/availability
- [REPORT_OBSERVATION] `SOURCE_011:424` — previous evidence: 09-10, 09-11 reports

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Repeat Pattern: long-open PR advanced to merge by others -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Same fix as two PRs (Dev + UAT): `#638`/`#641`, `#570`/`#572`

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:451` — Same fix as two PRs (Dev + UAT): `#638`/`#641`, `#570`/`#572`
- [RECOMMENDATION] `SOURCE_011:451` — Automate through scripts/tooling — cherry-pick bot or pipeline promotion

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Same fix as two PRs (Dev + UAT): `#638`/`#641`, `#570`/`#572` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` dev→uat promotion PRs "dev to uat"

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:452` — dev→uat promotion PRs "dev to uat"
- [RECOMMENDATION] `SOURCE_011:452` — Automate through scripts/tooling

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- dev→uat promotion PRs "dev to uat" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Reciprocal 0-char approvals with Jatin

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:453` — Reciprocal 0-char approvals with Jatin
- [RECOMMENDATION] `SOURCE_011:453` — Improve documentation/process — approval checklist

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Reciprocal 0-char approvals with Jatin -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Devin-generated regression tests for the provider-override marker lifecycle — 6 fix commits today on the same marker (hide/keep/clear/first-service leak).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:456` — Devin-generated regression tests for the provider-override marker lifecycle — 6 fix commits today on the same marker (hide/keep/clear/first-service leak).

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Devin-generated regression tests for the provider-override marker lifecycle — 6 fix commits today on the same marker (hide/keep/clear/first-service leak). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Devin triages the 9 findings on `#308` (prompt-registry sync script) into fix/no-fix before human review.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:457` — Devin triages the 9 findings on `#308` (prompt-registry sync script) into fix/no-fix before human review.

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Devin triages the 9 findings on `#308` (prompt-registry sync script) into fix/no-fix before human review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Devin drafts the release note for `#626` (37 files to prod) from its 43 commits.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:458` — Devin drafts the release note for `#626` (37 files to prod) from its 43 commits.

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Devin drafts the release note for `#626` (37 files to prod) from its 43 commits. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Repeat Pattern: empty-body approvals on PRs with open Devin findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:478` — Repeat Pattern: empty-body approvals on PRs with open Devin findings — `#626` (2 findings), `#309` (4 findings), 8 of 9 approvals 0-char
- [RECOMMENDATION] `SOURCE_011:478` — One line per finding before approving
- [REPORT_OBSERVATION] `SOURCE_011:478` — previous evidence: 09-08, 09-10, 09-11 (`#305`)

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Repeat Pattern: empty-body approvals on PRs with open Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Same removal as two PRs (Node `#639` + React `#571`)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:505` — Same removal as two PRs (Node `#639` + React `#571`)
- [RECOMMENDATION] `SOURCE_011:505` — Continue manually — different repos; but link them in the body

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Same removal as two PRs (Node `#639` + React `#571`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Reciprocal 0-char approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:506` — Reciprocal 0-char approvals
- [RECOMMENDATION] `SOURCE_011:506` — Improve documentation/process

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Reciprocal 0-char approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Promotion PRs with badge-only body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:507` — Promotion PRs with badge-only body
- [RECOMMENDATION] `SOURCE_011:507` — Automate through scripts/tooling

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Promotion PRs with badge-only body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Devin writes the migration safety note for `20260911_001_system_actor_users.sql` and `20260911_002_client_columns_cleanup.sql` — both got ANALYSIS/BUG findings 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:510` — Devin writes the migration safety note for `20260911_001_system_actor_users.sql` and `20260911_002_client_columns_cleanup.sql` — both got ANALYSIS/BUG findings that nobody answered.

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Devin writes the migration safety note for `20260911_001_system_actor_users.sql` and `20260911_002_client_columns_cleanup.sql` — both got ANALYSIS/BUG findings  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Devin drafts release notes for `#626`/`#557` (102 files to prod today, badge-only bodies).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:511` — Devin drafts release notes for `#626`/`#557` (102 files to prod today, badge-only bodies).

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Devin drafts release notes for `#626`/`#557` (102 files to prod today, badge-only bodies). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Repeat Pattern: merge/approve before or immediately after Devin posts findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:530` — Repeat Pattern: merge/approve before or immediately after Devin posts findings — `#311` approved before findings posted; `#313` 1 min
- [RECOMMENDATION] `SOURCE_011:530` — Wait for the Devin Review check before approving
- [REPORT_OBSERVATION] `SOURCE_011:530` — previous evidence: 09-11 `#307` (93 s), 09-10 `#439`, `#303`

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Repeat Pattern: merge/approve before or immediately after Devin posts findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Repeat Pattern: empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:531` — Repeat Pattern: empty approvals — 7/7 today
- [RECOMMENDATION] `SOURCE_011:531` — Approval checklist
- [REPORT_OBSERVATION] `SOURCE_011:531` — previous evidence: 09-08 → 09-11

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Repeat Pattern: empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` UAT → prod → Dev back-port of the same change (3 PRs + 1 abandoned sync)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:557` — UAT → prod → Dev back-port of the same change (3 PRs + 1 abandoned sync)
- [RECOMMENDATION] `SOURCE_011:557` — Automate through scripts/tooling — Dev-first, pipeline promotion

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- UAT → prod → Dev back-port of the same change (3 PRs + 1 abandoned sync) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Design-doc + QA-report per feature

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:558` — Design-doc + QA-report per feature
- [RECOMMENDATION] `SOURCE_011:558` — Continue manually — this is the good kind of repetition

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Design-doc + QA-report per feature -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Devin writes retry/timeout unit tests for `http_retry.py` — 3 BUG findings on it across `#309`/`#310`/`#312`, none answered.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:561` — Devin writes retry/timeout unit tests for `http_retry.py` — 3 BUG findings on it across `#309`/`#310`/`#312`, none answered.

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Devin writes retry/timeout unit tests for `http_retry.py` — 3 BUG findings on it across `#309`/`#310`/`#312`, none answered. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Devin drafts the `#314` body (66 files to UAT) from the 78 commits.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:562` — Devin drafts the `#314` body (66 files to UAT) from the 78 commits.

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Devin drafts the `#314` body (66 files to UAT) from the 78 commits. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Repeat Pattern: manual UAT→Dev back-port

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:581` — Repeat Pattern: manual UAT→Dev back-port — `#311`, `#312` (abandoned), `#313`
- [RECOMMENDATION] `SOURCE_011:581` — Dev-first branching
- [REPORT_OBSERVATION] `SOURCE_011:581` — previous evidence: 09-09, 09-10, 09-11 (`#304`)

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Repeat Pattern: manual UAT→Dev back-port -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Repeat Pattern: prod promotion before/with un-dispositioned findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:582` — Repeat Pattern: prod promotion before/with un-dispositioned findings — `#310` self-merged 3 min before 6 findings
- [RECOMMENDATION] `SOURCE_011:582` — Findings gate; no self-merge to `release/prod_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:582` — previous evidence: 09-10 `#303`, 09-11 `#307`

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Repeat Pattern: prod promotion before/with un-dispositioned findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` E&M mapping-table edits

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:608` — E&M mapping-table edits
- [RECOMMENDATION] `SOURCE_011:608` — Possible Devin Candidate — table edits with human rule review

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- E&M mapping-table edits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Deleting obsolete standalone test runners

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:609` — Deleting obsolete standalone test runners
- [RECOMMENDATION] `SOURCE_011:609` — Automate with Devin — sweep

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Deleting obsolete standalone test runners -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` Devin generates the E&M level-selection test matrix from the rank tables in `service_registry.py` (the max-code and rank-lookup bugs Devin found are exactly mat

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:612` — Devin generates the E&M level-selection test matrix from the rank tables in `service_registry.py` (the max-code and rank-lookup bugs Devin found are exactly matrix cases).

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- Devin generates the E&M level-selection test matrix from the rank tables in `service_registry.py` (the max-code and rank-lookup bugs Devin found are exactly mat -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` None meeting the recurrence bar

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:631` — None meeting the recurrence bar — —
- [RECOMMENDATION] `SOURCE_011:631` — —
- [REPORT_OBSERVATION] `SOURCE_011:631` — previous evidence: —
- [REPORT_OBSERVATION] `SOURCE_011:935` — None meeting the recurrence bar — —
- [RECOMMENDATION] `SOURCE_011:935` — —
- [REPORT_OBSERVATION] `SOURCE_011:935` — previous evidence: —

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- None meeting the recurrence bar -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` "okay" approvals on promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:656` — "okay" approvals on promotions
- [RECOMMENDATION] `SOURCE_011:656` — Improve documentation/process — go/no-go note

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- "okay" approvals on promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` Batch-closing stale engine PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:657` — Batch-closing stale engine PRs
- [RECOMMENDATION] `SOURCE_011:657` — Improve documentation/process — comment the reason on each

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- Batch-closing stale engine PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Devin summarises each `uat → release/prod_3.0` PR's findings into a go/no-go line for him to sign.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:660` — Devin summarises each `uat → release/prod_3.0` PR's findings into a go/no-go line for him to sign.

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Devin summarises each `uat → release/prod_3.0` PR's findings into a go/no-go line for him to sign. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` Repeat Pattern: "okay" approvals on prod promotions before/with open findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:678` — Repeat Pattern: "okay" approvals on prod promotions before/with open findings — `#449` (21 s, 2 findings after), `#451` (1 finding)
- [RECOMMENDATION] `SOURCE_011:678` — Wait for the Devin check; one line per finding
- [REPORT_OBSERVATION] `SOURCE_011:678` — previous evidence: 09-08, 09-09, 09-10, 09-11 (`#443`, `#446`)

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- Repeat Pattern: "okay" approvals on prod promotions before/with open findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` UAT→prod promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:699` — UAT→prod promotion PRs
- [RECOMMENDATION] `SOURCE_011:699` — Automate through scripts/tooling with a findings gate

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- UAT→prod promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000352` Devin validates client config files against schema before promotion (carried from 09-11).

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:702` — Devin validates client config files against schema before promotion (carried from 09-11).

### DECISION: ISSUE_000352_ATTEMPT_01
<!-- Devin validates client config files against schema before promotion (carried from 09-11). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000353` Repeat Pattern: prod promotion with open Devin findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:720` — Repeat Pattern: prod promotion with open Devin findings — `#451`
- [RECOMMENDATION] `SOURCE_011:720` — Wait for Devin Review; answer findings
- [REPORT_OBSERVATION] `SOURCE_011:720` — previous evidence: 09-08, 09-10, 09-11

### DECISION: ISSUE_000353_ATTEMPT_01
<!-- Repeat Pattern: prod promotion with open Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000354` PCS guideline rule → code + fixture

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:741` — PCS guideline rule → code + fixture
- [RECOMMENDATION] `SOURCE_011:741` — Automate through scripts/tooling — generate fixtures from the rule text

### DECISION: ISSUE_000354_ATTEMPT_01
<!-- PCS guideline rule → code + fixture -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000355` Diagnosing "X never saw Y" key mismatches (3 today)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:742` — Diagnosing "X never saw Y" key mismatches (3 today)
- [RECOMMENDATION] `SOURCE_011:742` — Automate with Devin — schema/contract test between extraction and PCS

### DECISION: ISSUE_000355_ATTEMPT_01
<!-- Diagnosing "X never saw Y" key mismatches (3 today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000356` Devin writes a contract test between the extraction output and PCS input — three of today's bugs were key-name/shape mismatches ("PCS never saw the approach", "

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:745` — Devin writes a contract test between the extraction output and PCS input — three of today's bugs were key-name/shape mismatches ("PCS never saw the approach", "extraction never saw DNR", "severity changed shape").

### DECISION: ISSUE_000356_ATTEMPT_01
<!-- Devin writes a contract test between the extraction output and PCS input — three of today's bugs were key-name/shape mismatches ("PCS never saw the approach", " -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000357` Draft PR so Devin Review covers the +4.4k lines added this week.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:746` — Draft PR so Devin Review covers the +4.4k lines added this week.

### DECISION: ISSUE_000357_ATTEMPT_01
<!-- Draft PR so Devin Review covers the +4.4k lines added this week. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000358` Repeat Pattern: inpatient engine branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:765` — Repeat Pattern: inpatient engine branch without PR — `feat/inpatient-engine`, 11 more commits (shared with Hitesh: 49-file, +8k commit today)
- [RECOMMENDATION] `SOURCE_011:765` — Draft PR this week
- [REPORT_OBSERVATION] `SOURCE_011:765` — previous evidence: 09-07 → 09-11 reports

### DECISION: ISSUE_000358_ATTEMPT_01
<!-- Repeat Pattern: inpatient engine branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000359` Answer-key / seed fixes bundled into feature commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:786` — Answer-key / seed fixes bundled into feature commits
- [RECOMMENDATION] `SOURCE_011:786` — Automate with Devin

### DECISION: ISSUE_000359_ATTEMPT_01
<!-- Answer-key / seed fixes bundled into feature commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000360` Long-running branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:787` — Long-running branch without PR
- [RECOMMENDATION] `SOURCE_011:787` — Improve documentation/process — draft PR

### DECISION: ISSUE_000360_ATTEMPT_01
<!-- Long-running branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000361` Devin maintains the answer keys from the case specs (carried).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:790` — Devin maintains the answer keys from the case specs (carried).

### DECISION: ISSUE_000361_ATTEMPT_01
<!-- Devin maintains the answer keys from the case specs (carried). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000362` Draft PR so a 49-file commit is not the first thing a reviewer sees at merge time.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:791` — Draft PR so a 49-file commit is not the first thing a reviewer sees at merge time.

### DECISION: ISSUE_000362_ATTEMPT_01
<!-- Draft PR so a 49-file commit is not the first thing a reviewer sees at merge time. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000363` Repeat Pattern: inpatient work on long-lived branches without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:809` — Repeat Pattern: inpatient work on long-lived branches without a PR — `feat/inpatient-engine` +8k in one commit
- [RECOMMENDATION] `SOURCE_011:809` — Draft PR today
- [REPORT_OBSERVATION] `SOURCE_011:809` — previous evidence: 09-07 → 09-11

### DECISION: ISSUE_000363_ATTEMPT_01
<!-- Repeat Pattern: inpatient work on long-lived branches without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000364` Insufficient data today

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:830` — Insufficient data today
- [RECOMMENDATION] `SOURCE_011:830` — —

### DECISION: ISSUE_000364_ATTEMPT_01
<!-- Insufficient data today -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000365` Devin diff-summarises prompt changes into commit bodies (carried).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:833` — Devin diff-summarises prompt changes into commit bodies (carried).

### DECISION: ISSUE_000365_ATTEMPT_01
<!-- Devin diff-summarises prompt changes into commit bodies (carried). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000366` Repeat Pattern: low-information commit messages (did not recur today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:851` — Repeat Pattern: low-information commit messages (did not recur today) — —
- [RECOMMENDATION] `SOURCE_011:851` — Keep it up
- [REPORT_OBSERVATION] `SOURCE_011:851` — previous evidence: 09-10, 09-11

### DECISION: ISSUE_000366_ATTEMPT_01
<!-- Repeat Pattern: low-information commit messages (did not recur today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000367` Excel formatting of POC output

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:872` — Excel formatting of POC output
- [RECOMMENDATION] `SOURCE_011:872` — Automate through scripts/tooling — one formatting function, tested once

### DECISION: ISSUE_000367_ATTEMPT_01
<!-- Excel formatting of POC output -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000368` Devin writes the Excel export formatter with a snapshot test so "beautify" commits stop.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:875` — Devin writes the Excel export formatter with a snapshot test so "beautify" commits stop.

### DECISION: ISSUE_000368_ATTEMPT_01
<!-- Devin writes the Excel export formatter with a snapshot test so "beautify" commits stop. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000369` Repeat Pattern: low-information / typo commit messages

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:893` — Repeat Pattern: low-information / typo commit messages — "beautfied excel" ×2
- [RECOMMENDATION] `SOURCE_011:893` — Conventional-commit hook on the POC branch
- [REPORT_OBSERVATION] `SOURCE_011:893` — previous evidence: 09-11 report ("fixex" ×2, "kep thinking empty")

### DECISION: ISSUE_000369_ATTEMPT_01
<!-- Repeat Pattern: low-information / typo commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000128` Insufficient data

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:914` — Insufficient data
- [RECOMMENDATION] `SOURCE_011:914` — —
- [REPORT_OBSERVATION] `SOURCE_011:956` — Insufficient data
- [RECOMMENDATION] `SOURCE_011:956` — —

### DECISION: ISSUE_000128_ATTEMPT_01
<!-- Insufficient data -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000370` Devin rebases `#435` and summarises what of `#382`/`#434` it supersedes.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:917` — Devin rebases `#435` and summarises what of `#382`/`#434` it supersedes.

### DECISION: ISSUE_000370_ATTEMPT_01
<!-- Devin rebases `#435` and summarises what of `#382`/`#434` it supersedes. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000371` Enable Devin Review on the RPA repository (carried; not observable as done).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:959` — Enable Devin Review on the RPA repository (carried; not observable as done).

### DECISION: ISSUE_000371_ATTEMPT_01
<!-- Enable Devin Review on the RPA repository (carried; not observable as done). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000372` Repeat Pattern: RPA self-merge (no occurrence today — no PRs)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:977` — Repeat Pattern: RPA self-merge (no occurrence today — no PRs) — —
- [RECOMMENDATION] `SOURCE_011:977` — Branch protection still recommended
- [REPORT_OBSERVATION] `SOURCE_011:977` — previous evidence: `#17`, `#19`, `#20`

### DECISION: ISSUE_000372_ATTEMPT_01
<!-- Repeat Pattern: RPA self-merge (no occurrence today — no PRs) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

