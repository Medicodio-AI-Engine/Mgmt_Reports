# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-02 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written `docs(review)` log commits recording gate results

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:95` — Hand-written `docs(review)` log commits recording gate results
- [RECOMMENDATION] `SOURCE_011:95` — Automate with Devin — the gate runner already emits the pass/fail data; a Devin task can write the log

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs(review)` log commits recording gate results -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Remediating a colleague's branch before reviewing it

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:96` — Remediating a colleague's branch before reviewing it
- [RECOMMENDATION] `SOURCE_011:96` — Improve documentation/process — split remediation (author or Devin) from approval so the approval is independent

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Remediating a colleague's branch before reviewing it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Delegate the `READ COMMITTED` transaction concern on `SupportLetterService` (left as `[needs your decision]`) as a scoped reproduction test.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:99` — Delegate the `READ COMMITTED` transaction concern on `SupportLetterService` (left as `[needs your decision]`) as a scoped reproduction test.

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Delegate the `READ COMMITTED` transaction concern on `SupportLetterService` (left as `[needs your decision]`) as a scoped reproduction test. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate review-log generation from gate output.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:100` — Delegate review-log generation from gate output.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate review-log generation from gate output. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the `matchedLetters` search-parity fix (minor, clearly scoped, left unfixed).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:101` — Delegate the `matchedLetters` search-parity fix (minor, clearly scoped, left unfixed).

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the `matchedLetters` search-parity fix (minor, clearly scoped, left unfixed). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Reviewer remediates then approves

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:121` — Reviewer remediates then approves — 19 of #1282's day commits are hers; her `approved` (8 chars) 12 s before her own merge
- [RECOMMENDATION] `SOURCE_011:121` — Have akanksh-rv or Devin remediate; Saijyoti approves only
- [REPORT_OBSERVATION] `SOURCE_011:121` — previous evidence: 08-30 report: "Saijyoti remediated AND reviewed #1260"; 08-31: #1239

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Reviewer remediates then approves -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Hand-written review-log commits

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:122` — Hand-written review-log commits — 4 today
- [RECOMMENDATION] `SOURCE_011:122` — Delegate to Devin
- [REPORT_OBSERVATION] `SOURCE_011:122` — previous evidence: 08-31 card: "6 hand-written review-log commits"

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Hand-written review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Long-lived branch merged from `dev` repeatedly before a PR exists

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:149` — Long-lived branch merged from `dev` repeatedly before a PR exists
- [RECOMMENDATION] `SOURCE_011:149` — Improve documentation/process — open a draft PR on day one so Devin Review and the gate run incrementally

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Long-lived branch merged from `dev` repeatedly before a PR exists -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Own the remaining `[needs your decision]` items on #1282 (transaction isolation, `matchedLetters` parity) as scoped Devin tasks.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:152` — Own the remaining `[needs your decision]` items on #1282 (transaction isolation, `matchedLetters` parity) as scoped Devin tasks.

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Own the remaining `[needs your decision]` items on #1282 (transaction isolation, `matchedLetters` parity) as scoped Devin tasks. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Delegate the `DraftLetterAiSkill` reject/no-owner test matrix for the next skill.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:153` — Delegate the `DraftLetterAiSkill` reject/no-owner test matrix for the next skill.

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Delegate the `DraftLetterAiSkill` reject/no-owner test matrix for the next skill. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Large feature accumulating without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:171` — Large feature accumulating without a PR — Resolved — #1282 opened and merged today
- [RECOMMENDATION] `SOURCE_011:171` — Close the pattern; open the next feature as a draft PR from the first commit
- [REPORT_OBSERVATION] `SOURCE_011:171` — previous evidence: 08-29, 08-30, 08-31 reports (3rd flag yesterday)

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Large feature accumulating without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Bundle decode/reference defects fixed one at a time

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:200` — Bundle decode/reference defects fixed one at a time
- [RECOMMENDATION] `SOURCE_011:200` — Automate with Devin — a real-DB bundle-corpus integration suite covering Decimal/JSON/reference classes

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Bundle decode/reference defects fixed one at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Merging `dev` into the feature branch

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:201` — Merging `dev` into the feature branch
- [RECOMMENDATION] `SOURCE_011:201` — Automate through scripts/tooling — auto-rebase bot or shorter-lived PRs

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Merging `dev` into the feature branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Non-mocked content-sync integration suite (third report recommending it).

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:204` — Non-mocked content-sync integration suite (third report recommending it).

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Non-mocked content-sync integration suite (third report recommending it). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Delegate a fixture generator that produces a bundle exercising every column type and every FK shape (`id` and non-`id`).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:205` — Delegate a fixture generator that produces a bundle exercising every column type and every FK shape (`id` and non-`id`).

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Delegate a fixture generator that produces a bundle exercising every column type and every FK shape (`id` and non-`id`). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Delegate the worker/API internal-token contract test that today's "declare the internal token the async import made mandatory" fix implies was missing.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:206` — Delegate the worker/API internal-token contract test that today's "declare the internal token the async import made mandatory" fix implies was missing.

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Delegate the worker/API internal-token contract test that today's "declare the internal token the async import made mandatory" fix implies was missing. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Decode/reference defects discovered serially after the fact

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:225` — Decode/reference defects discovered serially after the fact — "third bundle-breaking decode bug", "seventh ref was missed"
- [RECOMMENDATION] `SOURCE_011:225` — Build the integration corpus before the next content-sync feature
- [REPORT_OBSERVATION] `SOURCE_011:225` — previous evidence: 08-30 report: "six tests could not fail at all"; 08-31: four decode PRs

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Decode/reference defects discovered serially after the fact -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Hand-written review-log / runbook commits (5 today)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:253` — Hand-written review-log / runbook commits (5 today)
- [RECOMMENDATION] `SOURCE_011:253` — Automate with Devin — same as Saijyoti's log commits

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Hand-written review-log / runbook commits (5 today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Delegate the OpenAPI DTO shape + catalog binding sweep — a mechanical pattern migration across API and web.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:256` — Delegate the OpenAPI DTO shape + catalog binding sweep — a mechanical pattern migration across API and web.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Delegate the OpenAPI DTO shape + catalog binding sweep — a mechanical pattern migration across API and web. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Delegate the deploy-runbook generation from the migration file.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:257` — Delegate the deploy-runbook generation from the migration file.

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Delegate the deploy-runbook generation from the migration file. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:275` — — — —
- [RECOMMENDATION] `SOURCE_011:275` — —
- [REPORT_OBSERVATION] `SOURCE_011:275` — previous evidence: No prior documented finding

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Address round-N PRD review findings

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:302` — Address round-N PRD review findings
- [RECOMMENDATION] `SOURCE_011:302` — Improve documentation/process — cap automated rounds at 3, then request a named human PRD owner

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Address round-N PRD review findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Devin docs PRs superseded and closed unmerged

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:303` — Devin docs PRs superseded and closed unmerged
- [RECOMMENDATION] `SOURCE_011:303` — Improve documentation/process — one docs PR per topic, updated in place

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Devin docs PRs superseded and closed unmerged -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Keep using Devin for as-built documentation — it is a Good Devin Candidate — but merge it: none of the three docs PRs this window landed.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:306` — Keep using Devin for as-built documentation — it is a Good Devin Candidate — but merge it: none of the three docs PRs this window landed.

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Keep using Devin for as-built documentation — it is a Good Devin Candidate — but merge it: none of the three docs PRs this window landed. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Ask Devin for a one-page decision list from the PRD rather than another review round.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:307` — Ask Devin for a one-page decision list from the PRD rather than another review round.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Ask Devin for a one-page decision list from the PRD rather than another review round. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Devin docs PRs closed unmerged / superseded

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:325` — Devin docs PRs closed unmerged / superseded — #1277, #1279 closed without merge
- [RECOMMENDATION] `SOURCE_011:325` — Update one PR in place
- [REPORT_OBSERVATION] `SOURCE_011:325` — previous evidence: Prior windows' docs PRs

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Devin docs PRs closed unmerged / superseded -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Manually closing stale QA-gate PRs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:352` — Manually closing stale QA-gate PRs
- [RECOMMENDATION] `SOURCE_011:352` — Automate through scripts/tooling — auto-close QA PRs once the target merge is superseded

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Manually closing stale QA-gate PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Re-syncing `feat/qa-automation` with `dev` via giant PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:353` — Re-syncing `feat/qa-automation` with `dev` via giant PRs
- [RECOMMENDATION] `SOURCE_011:353` — Improve documentation/process — rebase or merge the branch into `dev`

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Re-syncing `feat/qa-automation` with `dev` via giant PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Make the gate emit a machine-readable verdict and wire it to branch protection on `dev`.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:356` — Make the gate emit a machine-readable verdict and wire it to branch protection on `dev`.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Make the gate emit a machine-readable verdict and wire it to branch protection on `dev`. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Delegate an ACU-per-gate report so "122.5 ACU validated nothing" is caught after one run, not five.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:357` — Delegate an ACU-per-gate report so "122.5 ACU validated nothing" is caught after one run, not five.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Delegate an ACU-per-gate report so "122.5 ACU validated nothing" is caught after one run, not five. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Self-merge with no review

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:375` — Self-merge with no review — #1250 merged by author, 0 approvals, 1,224 files
- [RECOMMENDATION] `SOURCE_011:375` — Land `feat/qa-automation` into `dev` via a reviewed PR
- [REPORT_OBSERVATION] `SOURCE_011:375` — previous evidence: 08-28 report (#1250 flagged since 08-27)

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Self-merge with no review -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Mirroring a BE analytics config change into FE by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:404` — Mirroring a BE analytics config change into FE by hand
- [RECOMMENDATION] `SOURCE_011:404` — Automate with Devin — contract test + Devin task per BE change

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Mirroring a BE analytics config change into FE by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` `Dev_1.0` → `release/prod_1.0` promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:405` — `Dev_1.0` → `release/prod_1.0` promotion PRs
- [RECOMMENDATION] `SOURCE_011:405` — Automate through scripts/tooling — release PR generator with changelog

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- `Dev_1.0` → `release/prod_1.0` promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Analytics config contract test (BE default ↔ FE fail-closed).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:408` — Analytics config contract test (BE default ↔ FE fail-closed).

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Analytics config contract test (BE default ↔ FE fail-closed). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Delegate a compile/typecheck gate so a missing import cannot merge (`#525` was a self-inflicted fix 3 minutes after the break merged).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:409` — Delegate a compile/typecheck gate so a missing import cannot merge (`#525` was a self-inflicted fix 3 minutes after the break merged).

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Delegate a compile/typecheck gate so a missing import cannot merge (`#525` was a self-inflicted fix 3 minutes after the break merged). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Regression tests for the prediction-trail stage rail (reverted once by hitesh on 08-31, re-touched today).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:410` — Regression tests for the prediction-trail stage rail (reverted once by hitesh on 08-31, re-touched today).

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Regression tests for the prediction-trail stage rail (reverted once by hitesh on 08-31, re-touched today). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:428` — Self-merge — #524 (178 s after approval), #525 (97 s)
- [RECOMMENDATION] `SOURCE_011:428` — Let the approver merge
- [REPORT_OBSERVATION] `SOURCE_011:428` — previous evidence: 08-31 report (#516)

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Behaviour change with no tests

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:429` — Behaviour change with no tests — 21 commits, 0 tests; `#519` 22 files template-only body
- [RECOMMENDATION] `SOURCE_011:429` — One test per fix PR minimum
- [REPORT_OBSERVATION] `SOURCE_011:429` — previous evidence: 08-28, 08-31 reports

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Behaviour change with no tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Empty approve + immediate merge on `Dev_1.0`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:456` — Empty approve + immediate merge on `Dev_1.0`
- [RECOMMENDATION] `SOURCE_011:456` — Improve documentation/process — a two-line approval template (what was checked, what was run)

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Empty approve + immediate merge on `Dev_1.0` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Delegate a merge-readiness summary bot for `Dev_1.0` PRs so the approval has content.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:459` — Delegate a merge-readiness summary bot for `Dev_1.0` PRs so the approval has content.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Delegate a merge-readiness summary bot for `Dev_1.0` PRs so the approval has content. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Revive `#249` prompt registry (14 reviews, idle) as a Devin remediation task.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:460` — Revive `#249` prompt registry (14 reviews, idle) as a Devin remediation task.

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Revive `#249` prompt registry (14 reviews, idle) as a Devin remediation task. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Content-free approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:478` — Content-free approvals — 7/7 today, incl. `#519` (22 files) 6 s before merge
- [RECOMMENDATION] `SOURCE_011:478` — Approval template
- [REPORT_OBSERVATION] `SOURCE_011:478` — previous evidence: 08-28 (20/20), 08-31 (9/9)

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Content-free approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Stalled own PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:479` — Stalled own PRs — Still open, no commits
- [RECOMMENDATION] `SOURCE_011:479` — Close or finish
- [REPORT_OBSERVATION] `SOURCE_011:479` — previous evidence: #248/#249 flagged 08-28, 08-30

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Stalled own PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Column-visibility migration edge cases fixed serially

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:506` — Column-visibility migration edge cases fixed serially
- [RECOMMENDATION] `SOURCE_011:506` — Automate with Devin — regression matrix over `sanitizeVisibleColumns` states

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Column-visibility migration edge cases fixed serially -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` "Prod fix issue" promotion PR with template body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:507` — "Prod fix issue" promotion PR with template body
- [RECOMMENDATION] `SOURCE_011:507` — Improve documentation/process — promotion body must list included PRs

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- "Prod fix issue" promotion PR with template body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` `sanitizeVisibleColumns` / `autoEnabledColumns` state-machine tests.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:510` — `sanitizeVisibleColumns` / `autoEnabledColumns` state-machine tests.

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- `sanitizeVisibleColumns` / `autoEnabledColumns` state-machine tests. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Auto-generated promotion PR body from the `Dev_1.0` diff.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:511` — Auto-generated promotion PR body from the `Dev_1.0` diff.

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Auto-generated promotion PR body from the `Dev_1.0` diff. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Template-only body on a production promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:529` — Template-only body on a production promotion — #521 open with `---` body
- [RECOMMENDATION] `SOURCE_011:529` — Fill the body before it is approved
- [REPORT_OBSERVATION] `SOURCE_011:529` — previous evidence: 08-31 report (#517)

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Template-only body on a production promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Per-facility onboarding

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:560` — Per-facility onboarding
- [RECOMMENDATION] `SOURCE_011:560` — Automate with Devin — now possible via the new skill; Resolved in principle

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Per-facility onboarding -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Dev → Uat → prod promotion PRs with template bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:561` — Dev → Uat → prod promotion PRs with template bodies
- [RECOMMENDATION] `SOURCE_011:561` — Automate through scripts/tooling — generated promotion body

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Dev → Uat → prod promotion PRs with template bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` PHI-in-logs regression test for the redactor and the LLM-payload gate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: PHI
- Priority: 9 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:564` — PHI-in-logs regression test for the redactor and the LLM-payload gate.

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- PHI-in-logs regression test for the redactor and the LLM-payload gate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Run the `/onboard-facility` skill via Devin for the next facility and measure the delta.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:565` — Run the `/onboard-facility` skill via Devin for the next facility and measure the delta.

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Run the `/onboard-facility` skill via Devin for the next facility and measure the delta. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Self-merge with zero review on `Dev_1.0`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:584` — Self-merge with zero review on `Dev_1.0` — #270 (10 min), #272 (13 s), #273 (7 s)
- [RECOMMENDATION] `SOURCE_011:584` — Require one non-author approval on `Dev_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:584` — previous evidence: 08-31 report ("self-merged both PRs")

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Self-merge with zero review on `Dev_1.0` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Template-only bodies on promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:585` — Template-only bodies on promotions — #271, #274, #277, #279
- [RECOMMENDATION] `SOURCE_011:585` — Generated promotion body
- [REPORT_OBSERVATION] `SOURCE_011:585` — previous evidence: 08-31

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Template-only bodies on promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Approve-and-merge promotions within seconds

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:610` — Approve-and-merge promotions within seconds
- [RECOMMENDATION] `SOURCE_011:610` — Improve documentation/process — release checklist recorded in the approval

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Approve-and-merge promotions within seconds -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` None — this is a release-gate role; the improvement is a checklist, not delegation.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:613` — None — this is a release-gate role; the improvement is a checklist, not delegation.

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- None — this is a release-gate role; the improvement is a checklist, not delegation. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Empty approvals on production promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:631` — Empty approvals on production promotions — 6/6 empty; 2 production merges 7–8 s after approval
- [RECOMMENDATION] `SOURCE_011:631` — Approval must state what was verified on UAT
- [REPORT_OBSERVATION] `SOURCE_011:631` — previous evidence: 08-28 card ("sumedh 4.6")

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Empty approvals on production promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` `okay` approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:657` — `okay` approvals
- [RECOMMENDATION] `SOURCE_011:657` — Improve documentation/process

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- `okay` approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Manual `uat` → `release/prod_3.0` promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:658` — Manual `uat` → `release/prod_3.0` promotions
- [RECOMMENDATION] `SOURCE_011:658` — Automate through scripts/tooling

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Manual `uat` → `release/prod_3.0` promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` KB-table-driven add-on/base phrase fixtures.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:661` — KB-table-driven add-on/base phrase fixtures.

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- KB-table-driven add-on/base phrase fixtures. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Delegate a diff-summary comment for engine promotions so the `okay` has something to attach to.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:662` — Delegate a diff-summary comment for engine promotions so the `okay` has something to attach to.

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Delegate a diff-summary comment for engine promotions so the `okay` has something to attach to. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` One-word approvals incl. production

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:680` — One-word approvals incl. production — `okay` ×5; `#414` (33 files → prod) merged 14 s after
- [RECOMMENDATION] `SOURCE_011:680` — Approval template
- [REPORT_OBSERVATION] `SOURCE_011:680` — previous evidence: 08-28 card (5.6, review thin)

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- One-word approvals incl. production -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Prod client-config seeding by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:706` — Prod client-config seeding by hand
- [RECOMMENDATION] `SOURCE_011:706` — Automate through scripts/tooling — seed as a deploy step after code, with `--diff` gate

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Prod client-config seeding by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` Client-config drift check that fails when config references a key the deployed code does not read.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:709` — Client-config drift check that fails when config references a key the deployed code does not read.

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- Client-config drift check that fails when config references a key the deployed code does not read. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Combination-code fixtures from the KB table.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:710` — Combination-code fixtures from the KB table.

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Combination-code fixtures from the KB table. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Devin findings on #411 unanswered

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:728` — Devin findings on #411 unanswered — Merged today, still unanswered
- [RECOMMENDATION] `SOURCE_011:728` — Answer or dismiss each finding before merge
- [REPORT_OBSERVATION] `SOURCE_011:728` — previous evidence: 08-28, 08-31 reports

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Devin findings on #411 unanswered -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` Promotion PRs with `---` body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:753` — Promotion PRs with `---` body
- [RECOMMENDATION] `SOURCE_011:753` — Automate through scripts/tooling

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- Promotion PRs with `---` body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Generated promotion body listing included PRs.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:756` — Generated promotion body listing included PRs.

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Generated promotion body listing included PRs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` Template-only production promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:774` — Template-only production promotion — #414 (33 files, +4,480) → prod with `---`
- [RECOMMENDATION] `SOURCE_011:774` — Body lists PRs and UAT evidence
- [REPORT_OBSERVATION] `SOURCE_011:774` — previous evidence: 08-28 card (4.3)

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- Template-only production promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

