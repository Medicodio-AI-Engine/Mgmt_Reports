# Dev review — decisions required

**Run:** `RUN_0004` · **Report date:** 2026-08-27 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000001` Low automation-adoption signal for SaijyotiMeti

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:31` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000001_ATTEMPT_01
<!-- Low automation-adoption signal for SaijyotiMeti -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000050` Low automation-adoption signal for jatinkushwaha-medicodio

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:37` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000050_ATTEMPT_01
<!-- Low automation-adoption signal for jatinkushwaha-medicodio -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000198` Low automation-adoption signal for amit-pandey-medicodio

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:39` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000198_ATTEMPT_01
<!-- Low automation-adoption signal for amit-pandey-medicodio -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000199` Hand-writing `/check` + `/fix` review-log markdown

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:65` — Hand-writing `/check` + `/fix` review-log markdown
- [RECOMMENDATION] `SOURCE_011:65` — Automate through scripts/tooling — generate the log from the gate output and the pushed fix commits

### DECISION: ISSUE_000199_ATTEMPT_01
<!-- Hand-writing `/check` + `/fix` review-log markdown -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000200` Backfilling tests that the original branch omitted

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:66` — Backfilling tests that the original branch omitted
- [RECOMMENDATION] `SOURCE_011:66` — Automate with Devin — a "write the missing service/repository tests for this diff" session per branch

### DECISION: ISSUE_000200_ATTEMPT_01
<!-- Backfilling tests that the original branch omitted -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000201` RBAC gate-parity sweeps (read paths missing a guard)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:67` — RBAC gate-parity sweeps (read paths missing a guard)
- [RECOMMENDATION] `SOURCE_011:67` — Automate through scripts/tooling — a lint rule that fails a controller method with no authz decorator

### DECISION: ISSUE_000201_ATTEMPT_01
<!-- RBAC gate-parity sweeps (read paths missing a guard) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000202` Delegate #1245 (idempotency keys on five note-creation endpoints) to Devin with the acceptance criteria already in the issue — it is bounded, repetitive across 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:70` — Delegate #1245 (idempotency keys on five note-creation endpoints) to Devin with the acceptance criteria already in the issue — it is bounded, repetitive across five endpoints, and she wrote the spec.

### DECISION: ISSUE_000202_ATTEMPT_01
<!-- Delegate #1245 (idempotency keys on five note-creation endpoints) to Devin with the acceptance criteria already in the issue — it is bounded, repetitive across  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000203` Delegate a repo-wide "controller methods without an authz decorator" audit; she has now found this class of gap on three separate branches.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:71` — Delegate a repo-wide "controller methods without an authz decorator" audit; she has now found this class of gap on three separate branches.

### DECISION: ISSUE_000203_ATTEMPT_01
<!-- Delegate a repo-wide "controller methods without an authz decorator" audit; she has now found this class of gap on three separate branches. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000204` Have Devin produce the review-log entry from the gate output at the end of each `/fix` cycle instead of writing it manually.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:72` — Have Devin produce the review-log entry from the gate output at the end of each `/fix` cycle instead of writing it manually.

### DECISION: ISSUE_000204_ATTEMPT_01
<!-- Have Devin produce the review-log entry from the gate output at the end of each `/fix` cycle instead of writing it manually. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000205` Review quality concentrated in one or two people

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:92` — Review quality concentrated in one or two people — Today 2 of 25 human review events were substantive, and both were hers
- [RECOMMENDATION] `SOURCE_011:92` — Not her defect to fix, but she is the natural owner of a 3-line review template the rest of the org can follow
- [REPORT_OBSERVATION] `SOURCE_011:92` — previous evidence: 08-25 report: "when akanksh-rv and SaijyotiMeti were both absent the substantive-review count went to zero"

### DECISION: ISSUE_000205_ATTEMPT_01
<!-- Review quality concentrated in one or two people -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000206` Post-hoc remediation of someone else's large branch

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 6 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:124` — Post-hoc remediation of someone else's large branch
- [RECOMMENDATION] `SOURCE_011:124` — Improve documentation/process — run the RBAC/audit/bounded-read gate before the PR is opened, not after 190 files exist

### DECISION: ISSUE_000206_ATTEMPT_01
<!-- Post-hoc remediation of someone else's large branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000207` Bounding unbounded list reads

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:125` — Bounding unbounded list reads
- [RECOMMENDATION] `SOURCE_011:125` — Automate through scripts/tooling — a lint/test rule that fails a list query with no `take`/pagination

### DECISION: ISSUE_000207_ATTEMPT_01
<!-- Bounding unbounded list reads -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000208` Regenerating architecture docs (`screen_index`, `module_map`, `data_flows`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:126` — Regenerating architecture docs (`screen_index`, `module_map`, `data_flows`)
- [RECOMMENDATION] `SOURCE_011:126` — Automate with Devin — a scheduled regeneration session per merge to `dev`

### DECISION: ISSUE_000208_ATTEMPT_01
<!-- Regenerating architecture docs (`screen_index`, `module_map`, `data_flows`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000209` Split #1244 into reviewable slices (schema + sync engine + admin surface) and let Devin do the mechanical split, so a second person can actually review it.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:129` — Split #1244 into reviewable slices (schema + sync engine + admin surface) and let Devin do the mechanical split, so a second person can actually review it.

### DECISION: ISSUE_000209_ATTEMPT_01
<!-- Split #1244 into reviewable slices (schema + sync engine + admin surface) and let Devin do the mechanical split, so a second person can actually review it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000210` Delegate the repo-wide unbounded-read audit — he has now fixed eight instances by hand in one day.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:130` — Delegate the repo-wide unbounded-read audit — he has now fixed eight instances by hand in one day.

### DECISION: ISSUE_000210_ATTEMPT_01
<!-- Delegate the repo-wide unbounded-read audit — he has now fixed eight instances by hand in one day. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000211` Delegate architecture-doc regeneration as a recurring session.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:131` — Delegate architecture-doc regeneration as a recurring session.

### DECISION: ISSUE_000211_ATTEMPT_01
<!-- Delegate architecture-doc regeneration as a recurring session. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000212` Very large PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:151` — Very large PRs — #1238 merged at 190 files; #1244 opened at 77 files
- [RECOMMENDATION] `SOURCE_011:151` — Treat >100 files as requiring two reviewers, or split by layer
- [REPORT_OBSERVATION] `SOURCE_011:151` — previous evidence: 08-25 report: #1238 at 171 files, #1239 at 155

### DECISION: ISSUE_000212_ATTEMPT_01
<!-- Very large PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000213` Review record kept off the PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:152` — Review record kept off the PR — GitHub shows an empty approval on #1238; the actual review is a `docs(review-logs)` commit
- [RECOMMENDATION] `SOURCE_011:152` — Paste the review-log verdict into the PR review body so the audit trail lives where the merge happened
- [REPORT_OBSERVATION] `SOURCE_011:152` — previous evidence: 08-23 and 08-25 reports note review logs committed into the repo

### DECISION: ISSUE_000213_ATTEMPT_01
<!-- Review record kept off the PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000214` Fixing the same class of Devin Review finding across create dialogs / read surfaces

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:183` — Fixing the same class of Devin Review finding across create dialogs / read surfaces
- [RECOMMENDATION] `SOURCE_011:183` — Improve documentation/process — put the recurring findings (org scoping, loading states, collision→409) into the session's acceptance criteria up front

### DECISION: ISSUE_000214_ATTEMPT_01
<!-- Fixing the same class of Devin Review finding across create dialogs / read surfaces -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000215` Re-stating firm-scoped settings reads per surface

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:184` — Re-stating firm-scoped settings reads per surface
- [RECOMMENDATION] `SOURCE_011:184` — Automate with Devin — one shared hook/helper, then a single migration session across surfaces

### DECISION: ISSUE_000215_ATTEMPT_01
<!-- Re-stating firm-scoped settings reads per surface -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000216` Ask Devin for the collision/scoping test matrix (manual vs generated, org vs firm scope, settings loading) before implementation — it would have pre-empted seve

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:187` — Ask Devin for the collision/scoping test matrix (manual vs generated, org vs firm scope, settings loading) before implementation — it would have pre-empted several of today's eight review cycles.

### DECISION: ISSUE_000216_ATTEMPT_01
<!-- Ask Devin for the collision/scoping test matrix (manual vs generated, org vs firm scope, settings loading) before implementation — it would have pre-empted seve -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000217` Open a Devin session to rebase and slice #1239 into reviewable parts so it can land.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:188` — Open a Devin session to rebase and slice #1239 into reviewable parts so it can land.

### DECISION: ISSUE_000217_ATTEMPT_01
<!-- Open a Devin session to rebase and slice #1239 into reviewable parts so it can land. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000218` Delegate the "read display settings under the caller's org scope" audit across the remaining portals.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:189` — Delegate the "read display settings under the caller's org scope" audit across the remaining portals.

### DECISION: ISSUE_000218_ATTEMPT_01
<!-- Delegate the "read display settings under the caller's org scope" audit across the remaining portals. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000219` Devin PR left open without a reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:209` — Devin PR left open without a reviewer — #1239 untouched and unreviewed for a second day while a new feature was started
- [RECOMMENDATION] `SOURCE_011:209` — Land or explicitly park #1239 before opening the next Devin feature; one open Devin PR per author at a time
- [REPORT_OBSERVATION] `SOURCE_011:209` — previous evidence: 08-25 report flagged #1239 as needing a named reviewer that day

### DECISION: ISSUE_000219_ATTEMPT_01
<!-- Devin PR left open without a reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000220` Many review cycles caused by unstated acceptance criteria

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:210` — Many review cycles caused by unstated acceptance criteria — 8 cycles on #1243
- [RECOMMENDATION] `SOURCE_011:210` — Write the acceptance criteria/test matrix into the session prompt
- [REPORT_OBSERVATION] `SOURCE_011:210` — previous evidence: 7 cycles on #1239 (08-25)

### DECISION: ISSUE_000220_ATTEMPT_01
<!-- Many review cycles caused by unstated acceptance criteria -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000221` Large feature branch remediated by a reviewer after the fact

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:238` — Large feature branch remediated by a reviewer after the fact
- [RECOMMENDATION] `SOURCE_011:238` — Automate with Devin — a pre-PR "run the RBAC/audit/bounded-read/test gate against this diff" session, owned by the author

### DECISION: ISSUE_000221_ATTEMPT_01
<!-- Large feature branch remediated by a reviewer after the fact -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000222` Run a Devin session against the diff before opening a PR of this size, with the repo's own gate rules as acceptance criteria.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:241` — Run a Devin session against the diff before opening a PR of this size, with the repo's own gate rules as acceptance criteria.

### DECISION: ISSUE_000222_ATTEMPT_01
<!-- Run a Devin session against the diff before opening a PR of this size, with the repo's own gate rules as acceptance criteria. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000223` Delegate the audit-row and authz-decorator coverage checks that anirudh had to add by hand.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:242` — Delegate the audit-row and authz-decorator coverage checks that anirudh had to add by hand.

### DECISION: ISSUE_000223_ATTEMPT_01
<!-- Delegate the audit-row and authz-decorator coverage checks that anirudh had to add by hand. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000224` Very large single PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:260` — Very large single PR — Merged at 190 files after 34 reviewer commits
- [RECOMMENDATION] `SOURCE_011:260` — Split by layer (schema / service / UI) or feature-flag increments
- [REPORT_OBSERVATION] `SOURCE_011:260` — previous evidence: 08-25 report: 171 files on day 2

### DECISION: ISSUE_000224_ATTEMPT_01
<!-- Very large single PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000225` QA defects filed as issues that no one picks up

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:289` — QA defects filed as issues that no one picks up
- [RECOMMENDATION] `SOURCE_011:289` — Automate with Devin — open a Devin session at triage from the issue body; the issues already contain reproduction steps

### DECISION: ISSUE_000225_ATTEMPT_01
<!-- QA defects filed as issues that no one picks up -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000226` Delegate #1242 (partial-success sheet state) to Devin directly from the issue — it is a bounded frontend state bug.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:292` — Delegate #1242 (partial-success sheet state) to Devin directly from the issue — it is a bounded frontend state bug.

### DECISION: ISSUE_000226_ATTEMPT_01
<!-- Delegate #1242 (partial-success sheet state) to Devin directly from the issue — it is a bounded frontend state bug. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000227` Delegate #1240 (pre-filled emails on new templates) the same way.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:293` — Delegate #1240 (pre-filled emails on new templates) the same way.

### DECISION: ISSUE_000227_ATTEMPT_01
<!-- Delegate #1240 (pre-filled emails on new templates) the same way. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000228` Use Devin to write the regression test for #1241 (questionnaire bundle import performance) before optimising it.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:294` — Use Devin to write the regression test for #1241 (questionnaire bundle import performance) before optimising it.

### DECISION: ISSUE_000228_ATTEMPT_01
<!-- Use Devin to write the regression test for #1241 (questionnaire bundle import performance) before optimising it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000229` QA issues filed but not delegated

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:312` — QA issues filed but not delegated — Both still open; #1242 added
- [RECOMMENDATION] `SOURCE_011:312` — Open a Devin session at the moment the issue is filed
- [REPORT_OBSERVATION] `SOURCE_011:312` — previous evidence: 08-25 report recommended delegating #1240/#1241 to Devin at triage — owner: SaahilVishwakarma

### DECISION: ISSUE_000229_ATTEMPT_01
<!-- QA issues filed but not delegated -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000230` Section/field rename fixes in chart-fetch (`emr_appointment_type` → `emr_visit_type`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:342` — Section/field rename fixes in chart-fetch (`emr_appointment_type` → `emr_visit_type`)
- [RECOMMENDATION] `SOURCE_011:342` — Automate with Devin — an alias map plus a test that fails when an EMR section key is renamed

### DECISION: ISSUE_000230_ATTEMPT_01
<!-- Section/field rename fixes in chart-fetch (`emr_appointment_type` → `emr_visit_type`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000231` UAT→prod promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:343` — UAT→prod promotion PRs
- [RECOMMENDATION] `SOURCE_011:343` — Automate through scripts/tooling — a promotion workflow that opens the PR with the diff summary

### DECISION: ISSUE_000231_ATTEMPT_01
<!-- UAT→prod promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000232` Delegate regression tests for the exclusion-validation lane — the fix changed lane wiring with no test commit.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:346` — Delegate regression tests for the exclusion-validation lane — the fix changed lane wiring with no test commit.

### DECISION: ISSUE_000232_ATTEMPT_01
<!-- Delegate regression tests for the exclusion-validation lane — the fix changed lane wiring with no test commit. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000233` Delegate an EMR section-alias test so the next rename fails in CI rather than in charts.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:347` — Delegate an EMR section-alias test so the next rename fails in CI rather than in charts.

### DECISION: ISSUE_000233_ATTEMPT_01
<!-- Delegate an EMR section-alias test so the next rename fails in CI rather than in charts. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000234` Devin Review findings unaddressed at merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:365` — Devin Review findings unaddressed at merge — 2 findings open on #397 at merge; the change then promoted to prod via #399
- [RECOMMENDATION] `SOURCE_011:365` — Read the findings before promoting; answer or explicitly dismiss with a reason
- [REPORT_OBSERVATION] `SOURCE_011:365` — previous evidence: Team-level pattern in the 08-22 to 08-25 reports

### DECISION: ISSUE_000234_ATTEMPT_01
<!-- Devin Review findings unaddressed at merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000235` Long-lived `feat/guideline` branch landed as one 223-file PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:394` — Long-lived `feat/guideline` branch landed as one 223-file PR
- [RECOMMENDATION] `SOURCE_011:394` — Improve documentation/process — open the draft PR at first push (this improved today; keep it)

### DECISION: ISSUE_000235_ATTEMPT_01
<!-- Long-lived `feat/guideline` branch landed as one 223-file PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000236` Non-descriptive commit messages ("Testing the ggl changes")

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:395` — Non-descriptive commit messages ("Testing the ggl changes")
- [RECOMMENDATION] `SOURCE_011:395` — Improve documentation/process — conventional-commit subjects naming the change

### DECISION: ISSUE_000236_ATTEMPT_01
<!-- Non-descriptive commit messages ("Testing the ggl changes") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000237` Delegate a regression test for the single-anchor `linking_removal` path — the bug was that a whole chart class was skipped, which is exactly what a test pins.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:398` — Delegate a regression test for the single-anchor `linking_removal` path — the bug was that a whole chart class was skipped, which is exactly what a test pins.

### DECISION: ISSUE_000237_ATTEMPT_01
<!-- Delegate a regression test for the single-anchor `linking_removal` path — the bug was that a whole chart class was skipped, which is exactly what a test pins. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000238` Delegate splitting the next guideline change into reviewable slices.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:399` — Delegate splitting the next guideline change into reviewable slices.

### DECISION: ISSUE_000238_ATTEMPT_01
<!-- Delegate splitting the next guideline change into reviewable slices. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000239` Delegate a diff summary for the prod promotion PR body so the reviewer has something to read.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:400` — Delegate a diff summary for the prod promotion PR body so the reviewer has something to read.

### DECISION: ISSUE_000239_ATTEMPT_01
<!-- Delegate a diff summary for the prod promotion PR body so the reviewer has something to read. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000240` Oversized change promoted straight to prod

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:418` — Oversized change promoted straight to prod — 223 files to `uat`, then to `release/prod_3.0` 11 minutes later, both approved `okay`, 3 findings open
- [RECOMMENDATION] `SOURCE_011:418` — Require a written risk/rollback note and one substantive approval on `release/prod_3.0`
- [REPORT_OBSERVATION] `SOURCE_011:418` — previous evidence: Prior reports flag hotfix/promotion pairs merged minutes apart

### DECISION: ISSUE_000240_ATTEMPT_01
<!-- Oversized change promoted straight to prod -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000241` Non-descriptive commit messages

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:419` — Non-descriptive commit messages — "Testing the ggl changes", "devin changes and vaccine acces"
- [RECOMMENDATION] `SOURCE_011:419` — Conventional-commit subjects; squash exploratory commits
- [REPORT_OBSERVATION] `SOURCE_011:419` — previous evidence: Prior reports (engine)

### DECISION: ISSUE_000241_ATTEMPT_01
<!-- Non-descriptive commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000242` Approving and merging promotion PRs with a one-word body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:448` — Approving and merging promotion PRs with a one-word body
- [RECOMMENDATION] `SOURCE_011:448` — Improve documentation/process — a 3-line review template (checked / not checked / verdict) required on `uat` and `release/prod_3.0`

### DECISION: ISSUE_000242_ATTEMPT_01
<!-- Approving and merging promotion PRs with a one-word body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000243` Manual UAT→prod promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:449` — Manual UAT→prod promotion PRs
- [RECOMMENDATION] `SOURCE_011:449` — Automate through scripts/tooling — a promotion workflow that opens the PR, lists the diff and links the gate run

### DECISION: ISSUE_000243_ATTEMPT_01
<!-- Manual UAT→prod promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000244` Low-information approvals as the review record

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:470` — Low-information approvals as the review record — 5 of 5 approvals today were "okay", including a 223-file prod promotion with 3 open Devin Review findings
- [RECOMMENDATION] `SOURCE_011:470` — Adopt the 3-line review template; block `release/prod_3.0` merges without it
- [REPORT_OBSERVATION] `SOURCE_011:470` — previous evidence: 08-20, 08-21, 08-22, 08-24, 08-25 reports (08-25: 9 of 9 human reviews thin)

### DECISION: ISSUE_000244_ATTEMPT_01
<!-- Low-information approvals as the review record -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000245` Prod promotion within minutes of UAT

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:471` — Prod promotion within minutes of UAT — #396 merged 11 min after #395; #399 merged 6 min after opening
- [RECOMMENDATION] `SOURCE_011:471` — Require a UAT soak window or a linked gate run before prod promotion
- [REPORT_OBSERVATION] `SOURCE_011:471` — previous evidence: Prior reports on hotfix/promotion pairs

### DECISION: ISSUE_000245_ATTEMPT_01
<!-- Prod promotion within minutes of UAT -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000246` Long-lived draft PR with slow trickle of commits

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:499` — Long-lived draft PR with slow trickle of commits
- [RECOMMENDATION] `SOURCE_011:499` — Improve documentation/process — state the remaining scope on the PR and set an exit criterion, or convert the remainder into a Devin session

### DECISION: ISSUE_000246_ATTEMPT_01
<!-- Long-lived draft PR with slow trickle of commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000247` Write the remaining scope of #393 as acceptance criteria and hand the mechanical parts (persistence, retrieval tests) to Devin.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:502` — Write the remaining scope of #393 as acceptance criteria and hand the mechanical parts (persistence, retrieval tests) to Devin.

### DECISION: ISSUE_000247_ATTEMPT_01
<!-- Write the remaining scope of #393 as acceptance criteria and hand the mechanical parts (persistence, retrieval tests) to Devin. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000248` Delegate a benchmark/test harness for recall quality so the draft can be evaluated rather than debated.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:503` — Delegate a benchmark/test harness for recall quality so the draft can be evaluated rather than debated.

### DECISION: ISSUE_000248_ATTEMPT_01
<!-- Delegate a benchmark/test harness for recall quality so the draft can be evaluated rather than debated. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000249` Removing PHI/sensitive columns from API responses one endpoint at a time

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: PHI
- Priority: 9 · Complexity: 9 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:549` — Removing PHI/sensitive columns from API responses one endpoint at a time
- [RECOMMENDATION] `SOURCE_011:549` — Automate through scripts/tooling — a response-schema allowlist test that fails when a PHI column appears in a payload

### DECISION: ISSUE_000249_ATTEMPT_01
<!-- Removing PHI/sensitive columns from API responses one endpoint at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000250` Syncing `Dev_1.0` into the feature branch by hand

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:550` — Syncing `Dev_1.0` into the feature branch by hand
- [RECOMMENDATION] `SOURCE_011:550` — Automate through scripts/tooling — scheduled auto-merge of the base branch into open feature branches

### DECISION: ISSUE_000250_ATTEMPT_01
<!-- Syncing `Dev_1.0` into the feature branch by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000251` `lgtm` approvals on prod promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:551` — `lgtm` approvals on prod promotions
- [RECOMMENDATION] `SOURCE_011:551` — Improve documentation/process — 3-line review template, mandatory on `release/prod_1.0`

### DECISION: ISSUE_000251_ATTEMPT_01
<!-- `lgtm` approvals on prod promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000252` Delegate a PHI-masking regression suite covering masked date formatting, dispatch-batch responses and grant-based unmasking — the three defects he fixed by hand

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: PHI
- Priority: 9 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:554` — Delegate a PHI-masking regression suite covering masked date formatting, dispatch-batch responses and grant-based unmasking — the three defects he fixed by hand today are one test class.

### DECISION: ISSUE_000252_ATTEMPT_01
<!-- Delegate a PHI-masking regression suite covering masked date formatting, dispatch-batch responses and grant-based unmasking — the three defects he fixed by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000253` Delegate the remaining "dialog dropdowns → portalled `AnchoredPanel`" migration across other dialogs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:555` — Delegate the remaining "dialog dropdowns → portalled `AnchoredPanel`" migration across other dialogs.

### DECISION: ISSUE_000253_ATTEMPT_01
<!-- Delegate the remaining "dialog dropdowns → portalled `AnchoredPanel`" migration across other dialogs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000254` Delegate the dashboards documentation sync that consumed three separate PRs on one branch.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:556` — Delegate the dashboards documentation sync that consumed three separate PRs on one branch.

### DECISION: ISSUE_000254_ATTEMPT_01
<!-- Delegate the dashboards documentation sync that consumed three separate PRs on one branch. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000255` `lgtm` as the review record on prod-path PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:575` — `lgtm` as the review record on prod-path PRs — #577 (46 files) and #501 (56 files), both `release/prod_1.0`, both `lgtm`
- [RECOMMENDATION] `SOURCE_011:575` — 3-line review template required on prod branches
- [REPORT_OBSERVATION] `SOURCE_011:575` — previous evidence: 08-20, 08-21, 08-22, 08-24, 08-25 reports

### DECISION: ISSUE_000255_ATTEMPT_01
<!-- `lgtm` as the review record on prod-path PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000256` Self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:576` — Self-merge — #502 self-merged (6 files, documentation)
- [RECOMMENDATION] `SOURCE_011:576` — One non-author approval on `Dev_1.0` too, or an explicit documented exception for docs-only PRs
- [REPORT_OBSERVATION] `SOURCE_011:576` — previous evidence: 08-25 report: 4 self-merges in integration

### DECISION: ISSUE_000256_ATTEMPT_01
<!-- Self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000257` No tests with behaviour changes

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:577` — No tests with behaviour changes — 6 behaviour commits today, 0 test commits
- [RECOMMENDATION] `SOURCE_011:577` — Delegate the regression suite to Devin
- [REPORT_OBSERVATION] `SOURCE_011:577` — previous evidence: Prior reports on the app repos

### DECISION: ISSUE_000257_ATTEMPT_01
<!-- No tests with behaviour changes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000258` Opening UAT→prod promotion PRs across two repos

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:608` — Opening UAT→prod promotion PRs across two repos
- [RECOMMENDATION] `SOURCE_011:608` — Automate through scripts/tooling — a release workflow that opens both promotion PRs with a diff summary and links the deploy run

### DECISION: ISSUE_000258_ATTEMPT_01
<!-- Opening UAT→prod promotion PRs across two repos -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000259` Approving with an empty body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:609` — Approving with an empty body
- [RECOMMENDATION] `SOURCE_011:609` — Improve documentation/process — 3-line review template

### DECISION: ISSUE_000259_ATTEMPT_01
<!-- Approving with an empty body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000260` Delegate generation of the promotion PR body: changed areas, migrations included, risk and rollback — today's promotions shipped 100+ files across two repos wit

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:612` — Delegate generation of the promotion PR body: changed areas, migrations included, risk and rollback — today's promotions shipped 100+ files across two repos with no written description.

### DECISION: ISSUE_000260_ATTEMPT_01
<!-- Delegate generation of the promotion PR body: changed areas, migrations included, risk and rollback — today's promotions shipped 100+ files across two repos wit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000261` Delegate tests for #248's new insurance-created flag before it merges (35 files, no test commits).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:613` — Delegate tests for #248's new insurance-created flag before it merges (35 files, no test commits).

### DECISION: ISSUE_000261_ATTEMPT_01
<!-- Delegate tests for #248's new insurance-created flag before it merges (35 files, no test commits). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000262` Delegate a "release notes from the diff" session for each promotion pair.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:614` — Delegate a "release notes from the diff" session for each promotion pair.

### DECISION: ISSUE_000262_ATTEMPT_01
<!-- Delegate a "release notes from the diff" session for each promotion pair. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000263` Empty approvals as the review record

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:633` — Empty approvals as the review record — 5 approvals today, every one empty
- [RECOMMENDATION] `SOURCE_011:633` — 3-line review template; enforce on `Dev_1.0` and `release/prod_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:633` — previous evidence: 08-22, 08-24, 08-25 reports

### DECISION: ISSUE_000263_ATTEMPT_01
<!-- Empty approvals as the review record -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000264` Promotion PRs with no written risk/rollback note

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:634` — Promotion PRs with no written risk/rollback note — #577 (46 files) and #501 (56 files) opened with no description
- [RECOMMENDATION] `SOURCE_011:634` — Generate the body from the diff (script or Devin)
- [REPORT_OBSERVATION] `SOURCE_011:634` — previous evidence: Prior reports on promotion fan-out

### DECISION: ISSUE_000264_ATTEMPT_01
<!-- Promotion PRs with no written risk/rollback note -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000265` Applying the same dropdown/portal pattern across dialogs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:662` — Applying the same dropdown/portal pattern across dialogs
- [RECOMMENDATION] `SOURCE_011:662` — Automate with Devin — one session to migrate the remaining dialogs to the shared portalled component

### DECISION: ISSUE_000265_ATTEMPT_01
<!-- Applying the same dropdown/portal pattern across dialogs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000266` Long-lived personal feature branches (`hitesh/...-20260825`, `hitesh/invoicing-billing-suite-20260807`)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 6 · Complexity: 9 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:663` — Long-lived personal feature branches (`hitesh/...-20260825`, `hitesh/invoicing-billing-suite-20260807`)
- [RECOMMENDATION] `SOURCE_011:663` — Improve documentation/process — draft PR at first push

### DECISION: ISSUE_000266_ATTEMPT_01
<!-- Long-lived personal feature branches (`hitesh/...-20260825`, `hitesh/invoicing-billing-suite-20260807`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000267` Delegate the remaining dialog→portalled-dropdown migration, using #499 as the reference diff.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:666` — Delegate the remaining dialog→portalled-dropdown migration, using #499 as the reference diff.

### DECISION: ISSUE_000267_ATTEMPT_01
<!-- Delegate the remaining dialog→portalled-dropdown migration, using #499 as the reference diff. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000268` Delegate component tests for the Prediction Trail redesign (38 files, no test commits observed).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:667` — Delegate component tests for the Prediction Trail redesign (38 files, no test commits observed).

### DECISION: ISSUE_000268_ATTEMPT_01
<!-- Delegate component tests for the Prediction Trail redesign (38 files, no test commits observed). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000269` Open a draft PR (or a Devin session) for the long-lived invoicing/billing branch.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 5 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:668` — Open a draft PR (or a Devin session) for the long-lived invoicing/billing branch.

### DECISION: ISSUE_000269_ATTEMPT_01
<!-- Open a draft PR (or a Devin session) for the long-lived invoicing/billing branch. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000270` Manual repetitive UI pattern migration

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:687` — Manual repetitive UI pattern migration — #499 applied the same dropdown fix across 15 files by hand
- [RECOMMENDATION] `SOURCE_011:687` — Delegate the next pattern migration to Devin with the reference diff
- [REPORT_OBSERVATION] `SOURCE_011:687` — previous evidence: 08-24/08-25 reports note repetitive frontend pattern work in this repo

### DECISION: ISSUE_000270_ATTEMPT_01
<!-- Manual repetitive UI pattern migration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000271` Promotion fan-out: the same change carried through `import_main` → `Uat_1.0` → `release/prod_1.0` as separate PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 3 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:717` — Promotion fan-out: the same change carried through `import_main` → `Uat_1.0` → `release/prod_1.0` as separate PRs
- [RECOMMENDATION] `SOURCE_011:717` — Automate through scripts/tooling — a promotion workflow (this is the single most-repeated manual task in the org)

### DECISION: ISSUE_000271_ATTEMPT_01
<!-- Promotion fan-out: the same change carried through `import_main` → `Uat_1.0` → `release/prod_1.0` as separate PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000272` Re-deciding batch-status semantics case by case

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: C
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:718` — Re-deciding batch-status semantics case by case
- [RECOMMENDATION] `SOURCE_011:718` — Automate with Devin — one pytest suite encoding the four invariants he settled today

### DECISION: ISSUE_000272_ATTEMPT_01
<!-- Re-deciding batch-status semantics case by case -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000273` Hotfix pairs (prod fix + backport)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:719` — Hotfix pairs (prod fix + backport)
- [RECOMMENDATION] `SOURCE_011:719` — Improve documentation/process — fix in UAT, promote once, unless a true incident

### DECISION: ISSUE_000273_ATTEMPT_01
<!-- Hotfix pairs (prod fix + backport) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000274` Delegate a pytest suite for the four batch-status invariants (failed-preprocess, never-run, re-run subset, max-wins counts) — they are now precisely specified i

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: C
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:722` — Delegate a pytest suite for the four batch-status invariants (failed-preprocess, never-run, re-run subset, max-wins counts) — they are now precisely specified in his commit bodies.

### DECISION: ISSUE_000274_ATTEMPT_01
<!-- Delegate a pytest suite for the four batch-status invariants (failed-preprocess, never-run, re-run subset, max-wins counts) — they are now precisely specified i -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000275` Delegate a promotion script/workflow that opens the `import_main`→UAT→prod chain with diff summaries.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:723` — Delegate a promotion script/workflow that opens the `import_main`→UAT→prod chain with diff summaries.

### DECISION: ISSUE_000275_ATTEMPT_01
<!-- Delegate a promotion script/workflow that opens the `import_main`→UAT→prod chain with diff summaries. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000276` Delegate a repo scan for other secret-bearing file patterns after the `.pem` fix.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: SECRETS
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:724` — Delegate a repo scan for other secret-bearing file patterns after the `.pem` fix.

### DECISION: ISSUE_000276_ATTEMPT_01
<!-- Delegate a repo scan for other secret-bearing file patterns after the `.pem` fix. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000277` Self-merge into `import_main`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:745` — Self-merge into `import_main` — #241 and #244 self-merged today
- [RECOMMENDATION] `SOURCE_011:745` — Enable one-non-author-approval branch protection on `import_main` (still not enabled)
- [REPORT_OBSERVATION] `SOURCE_011:745` — previous evidence: 08-23 and 08-25 reports (4 self-merges on 08-25)

### DECISION: ISSUE_000277_ATTEMPT_01
<!-- Self-merge into `import_main` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000278` Behaviour changes with no tests

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:746` — Behaviour changes with no tests — 6 batch-status behaviour changes, 0 test commits
- [RECOMMENDATION] `SOURCE_011:746` — Delegate the invariant suite to Devin
- [REPORT_OBSERVATION] `SOURCE_011:746` — previous evidence: 08-22 to 08-25 reports

### DECISION: ISSUE_000278_ATTEMPT_01
<!-- Behaviour changes with no tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000279` Manual promotion fan-out

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:747` — Manual promotion fan-out — 5 of 7 PRs today
- [RECOMMENDATION] `SOURCE_011:747` — Promotion workflow (team-level action)
- [REPORT_OBSERVATION] `SOURCE_011:747` — previous evidence: Flagged every day since 08-20

### DECISION: ISSUE_000279_ATTEMPT_01
<!-- Manual promotion fan-out -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000280` One-word approvals on promotion/hotfix PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:777` — One-word approvals on promotion/hotfix PRs
- [RECOMMENDATION] `SOURCE_011:777` — Improve documentation/process — 3-line review template; the value of an independent approver is lost if nothing is recorded

### DECISION: ISSUE_000280_ATTEMPT_01
<!-- One-word approvals on promotion/hotfix PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000281` Approvals with no content

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:798` — Approvals with no content — 5 approvals, "approve" or empty, including an 84-file prod promotion
- [RECOMMENDATION] `SOURCE_011:798` — 3-line review template
- [REPORT_OBSERVATION] `SOURCE_011:798` — previous evidence: Team-level pattern since 08-20

### DECISION: ISSUE_000281_ATTEMPT_01
<!-- Approvals with no content -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

