# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-03 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written `docs(review)` logs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:90` — Hand-written `docs(review)` logs
- [RECOMMENDATION] `SOURCE_011:90` — Automate with Devin — the gate runner already has the verdicts; generate the log skeleton

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs(review)` logs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Same-class date/timezone fixes across call sites

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:91` — Same-class date/timezone fixes across call sites
- [RECOMMENDATION] `SOURCE_011:91` — Automate with Devin — one codemod + regression matrix instead of per-view fixes

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Same-class date/timezone fixes across call sites -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Remediating another author's branch before approving it

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:92` — Remediating another author's branch before approving it
- [RECOMMENDATION] `SOURCE_011:92` — Improve documentation/process — return findings to the author; keep approval independent

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Remediating another author's branch before approving it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Ask Devin to enumerate every `formatDate`/`formatExpiryDate`/`parseDateValue` caller and generate a west-of-UTC regression test per caller; today's three separa

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:95` — Ask Devin to enumerate every `formatDate`/`formatExpiryDate`/`parseDateValue` caller and generate a west-of-UTC regression test per caller; today's three separate off-by-one fixes suggest more remain.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Ask Devin to enumerate every `formatDate`/`formatExpiryDate`/`parseDateValue` caller and generate a west-of-UTC regression test per caller; today's three separa -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the `docs/review-logs/` skeleton from gate output so the human writes only the judgement.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:96` — Delegate the `docs/review-logs/` skeleton from gate output so the human writes only the judgement.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the `docs/review-logs/` skeleton from gate output so the human writes only the judgement. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Have Devin split `#1305` into stackable PRs (schema, service, UI) before a human reviews 105 files.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:97` — Have Devin split `#1305` into stackable PRs (schema, service, UI) before a human reviews 105 files.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Have Devin split `#1305` into stackable PRs (schema, service, UI) before a human reviews 105 files. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Reviewer remediates then approves own remediation

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:116` — Reviewer remediates then approves own remediation — `#1285`: 30 commits, 8-char `approved`, merge 60 s later
- [RECOMMENDATION] `SOURCE_011:116` — Second approver required when the reviewer has ≥ 1 commit on the branch
- [REPORT_OBSERVATION] `SOURCE_011:116` — previous evidence: 08-31, 09-01 (`#1282`: 19 commits, 8-char approval, merge 12 s later)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Reviewer remediates then approves own remediation -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Hand-written review logs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:117` — Hand-written review logs — 5 today
- [RECOMMENDATION] `SOURCE_011:117` — Generate from gate output
- [REPORT_OBSERVATION] `SOURCE_011:117` — previous evidence: 08-31 (6), 09-01 (4)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Hand-written review logs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Very large single PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:118` — Very large single PR — `#1305` 105 files
- [RECOMMENDATION] `SOURCE_011:118` — Split before review
- [REPORT_OBSERVATION] `SOURCE_011:118` — previous evidence: — (first occurrence as author)

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Very large single PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` `dev → uat → main` promotion PRs with template-only bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:148` — `dev → uat → main` promotion PRs with template-only bodies
- [RECOMMENDATION] `SOURCE_011:148` — Automate through scripts/tooling — generate the body from the merge list and gate verdicts

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- `dev → uat → main` promotion PRs with template-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Content-sync decode/dependency fixes one per commit

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:149` — Content-sync decode/dependency fixes one per commit
- [RECOMMENDATION] `SOURCE_011:149` — Automate with Devin — bundle-corpus integration suite

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Content-sync decode/dependency fixes one per commit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Remediating others' PRs (`#1257`) then approving

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:150` — Remediating others' PRs (`#1257`) then approving
- [RECOMMENDATION] `SOURCE_011:150` — Improve documentation/process

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Remediating others' PRs (`#1257`) then approving -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Delegate the content-sync bundle-corpus test suite (non-mocked) — fourth report naming it.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:153` — Delegate the content-sync bundle-corpus test suite (non-mocked) — fourth report naming it.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Delegate the content-sync bundle-corpus test suite (non-mocked) — fourth report naming it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Delegate the `importSession` infinite-spinner fix from the NOT READY report; it is a scoped UI defect with a written reproduction.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:154` — Delegate the `importSession` infinite-spinner fix from the NOT READY report; it is a scoped UI defect with a written reproduction.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Delegate the `importSession` infinite-spinner fix from the NOT READY report; it is a scoped UI defect with a written reproduction. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Have the promotion PR body generated from `git log dev..uat` plus the latest gate verdicts so the approver sees what is being promoted.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:155` — Have the promotion PR body generated from `git log dev..uat` plus the latest gate verdicts so the approver sees what is being promoted.

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Have the promotion PR body generated from `git log dev..uat` plus the latest gate verdicts so the approver sees what is being promoted. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Empty approvals incl. production

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:174` — Empty approvals incl. production — 4/4 empty; `#1283` 98 files approved 0-char, merged 1 min later
- [RECOMMENDATION] `SOURCE_011:174` — Written verdict ≥ 2 sentences on anything ≥ 20 files
- [REPORT_OBSERVATION] `SOURCE_011:174` — previous evidence: 08-31, 09-01

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Empty approvals incl. production -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Content-sync defects on mocked tests

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:175` — Content-sync defects on mocked tests — `#1278` needed one more dependency fix before merge
- [RECOMMENDATION] `SOURCE_011:175` — Integration corpus
- [REPORT_OBSERVATION] `SOURCE_011:175` — previous evidence: 08-30 → 09-02

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Content-sync defects on mocked tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` QA verdict ignored on promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:176` — QA verdict ignored on promotion — `#1278` NOT READY → `main` in 3 h
- [RECOMMENDATION] `SOURCE_011:176` — Gate as required status
- [REPORT_OBSERVATION] `SOURCE_011:176` — previous evidence: new

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- QA verdict ignored on promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` QA gates failing on environment before testing

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: AUTHENTICATION
- Priority: 8 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:205` — QA gates failing on environment before testing
- [RECOMMENDATION] `SOURCE_011:205` — Automate through scripts/tooling — a 10-second persona login probe before the gate spends effort

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- QA gates failing on environment before testing -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Empty approvals on promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:206` — Empty approvals on promotions
- [RECOMMENDATION] `SOURCE_011:206` — Improve documentation/process
- [REPORT_OBSERVATION] `SOURCE_011:409` — Empty approvals on promotions
- [RECOMMENDATION] `SOURCE_011:409` — Improve documentation/process

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Empty approvals on promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Remediating another author's branch

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:207` — Remediating another author's branch
- [RECOMMENDATION] `SOURCE_011:207` — Improve documentation/process

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Remediating another author's branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Pre-flight credential check that fails fast and pings the owner instead of running a full gate to "no verdict".

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: SECRETS
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:210` — Pre-flight credential check that fails fast and pings the owner instead of running a full gate to "no verdict".

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Pre-flight credential check that fails fast and pings the owner instead of running a full gate to "no verdict". -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Emit a machine-readable verdict as a commit status on `dev` so `dev → uat` cannot merge with NOT READY outstanding.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:211` — Emit a machine-readable verdict as a commit status on `dev` so `dev → uat` cannot merge with NOT READY outstanding.

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Emit a machine-readable verdict as a commit status on `dev` so `dev → uat` cannot merge with NOT READY outstanding. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Delegate resolving the `#1282` verdict disagreement (hosted-dev vs Claude run) into a single recorded decision.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:212` — Delegate resolving the `#1282` verdict disagreement (hosted-dev vs Claude run) into a single recorded decision.

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Delegate resolving the `#1282` verdict disagreement (hosted-dev vs Claude run) into a single recorded decision. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Empty approvals incl. prod

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:231` — Empty approvals incl. prod — 5/5 empty, 3 prod-path
- [RECOMMENDATION] `SOURCE_011:231` — Written verdicts
- [REPORT_OBSERVATION] `SOURCE_011:231` — previous evidence: 09-01 (`#1250` self-merged 0 approvals), 08-31

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Empty approvals incl. prod -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Gate cost with no verdict

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:232` — Gate cost with no verdict — 4 of 6 gates no verdict
- [RECOMMENDATION] `SOURCE_011:232` — Pre-flight probe
- [REPORT_OBSERVATION] `SOURCE_011:232` — previous evidence: 09-01 "122.5 ACU validated nothing"

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Gate cost with no verdict -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Feature PRs remediated by others before merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:259` — Feature PRs remediated by others before merge
- [RECOMMENDATION] `SOURCE_011:259` — Improve documentation/process — run the standards gate locally before requesting review

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Feature PRs remediated by others before merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Devin docs PRs reviewed only by Devin

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:260` — Devin docs PRs reviewed only by Devin
- [RECOMMENDATION] `SOURCE_011:260` — Continue manually — human PRD reviewer at round 3

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Devin docs PRs reviewed only by Devin -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Delegate the backend enforcement of the ISO-3166 rule (`persons.dto.ts`) plus a migration audit of non-canonical stored values — bounded, well specified by the 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:263` — Delegate the backend enforcement of the ISO-3166 rule (`persons.dto.ts`) plus a migration audit of non-canonical stored values — bounded, well specified by the QA comment.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Delegate the backend enforcement of the ISO-3166 rule (`persons.dto.ts`) plus a migration audit of non-canonical stored values — bounded, well specified by the  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Ask Devin for the regression tests before opening the next validation PR rather than after the reviewer writes them.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:264` — Ask Devin for the regression tests before opening the next validation PR rather than after the reviewer writes them.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Ask Devin for the regression tests before opening the next validation PR rather than after the reviewer writes them. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Devin-reviews-Devin loop

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:282` — Devin-reviews-Devin loop — 29 more bot comments, 0 human
- [RECOMMENDATION] `SOURCE_011:282` — Human review at round 3
- [REPORT_OBSERVATION] `SOURCE_011:282` — previous evidence: 09-01 (`#1280` 15 rounds)

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Devin-reviews-Devin loop -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Own PRs landed by others' remediation

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:283` — Own PRs landed by others' remediation — `#1285` 30 remediation commits by reviewer
- [RECOMMENDATION] `SOURCE_011:283` — Local gate before review
- [REPORT_OBSERVATION] `SOURCE_011:283` — previous evidence: `#1257` earlier week

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Own PRs landed by others' remediation -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Post-merge fix-up PR for QA findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:309` — Post-merge fix-up PR for QA findings
- [RECOMMENDATION] `SOURCE_011:309` — Improve documentation/process — run the QA routine pre-merge on this branch class

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Post-merge fix-up PR for QA findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Delegate a BullMQ retry-path test that asserts a transient blob/Gemini failure is retried, not permanently failed.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:312` — Delegate a BullMQ retry-path test that asserts a transient blob/Gemini failure is retried, not permanently failed.

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Delegate a BullMQ retry-path test that asserts a transient blob/Gemini failure is retried, not permanently failed. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Delegate the hosted-dev manual verification checklist for the extraction UI once personas are restored.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:313` — Delegate the hosted-dev manual verification checklist for the extraction UI once personas are restored.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Delegate the hosted-dev manual verification checklist for the extraction UI once personas are restored. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` None with history

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:331` — None with history — —
- [RECOMMENDATION] `SOURCE_011:331` — —
- [REPORT_OBSERVATION] `SOURCE_011:331` — previous evidence: —

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- None with history -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Multi-day accumulation → single ≥ 100-file PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:358` — Multi-day accumulation → single ≥ 100-file PR
- [RECOMMENDATION] `SOURCE_011:358` — Improve documentation/process — open the PR at the first reviewable slice

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Multi-day accumulation → single ≥ 100-file PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Manual QA routine comments

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:359` — Manual QA routine comments
- [RECOMMENDATION] `SOURCE_011:359` — Automate with Devin — the Devin gate already does this; unify rather than run two

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Manual QA routine comments -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Let Devin generate the tenancy/IDOR/RBAC probes for letter groups from the `#1306` body before human review.

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: TENANT_ISOLATION
- Priority: 10 · Complexity: 10 · Tier: D
- Playbook: ORG_PB_TENANT_ISOLATION_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:362` — Let Devin generate the tenancy/IDOR/RBAC probes for letter groups from the `#1306` body before human review.

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Let Devin generate the tenancy/IDOR/RBAC probes for letter groups from the `#1306` body before human review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Split `#1306` (schema, platform admin, case-manager UI, AI drafting) with Devin doing the mechanical separation.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:363` — Split `#1306` (schema, platform admin, case-manager UI, AI drafting) with Devin doing the mechanical separation.

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Split `#1306` (schema, platform admin, case-manager UI, AI drafting) with Devin doing the mechanical separation. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` One huge PR per feature

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:381` — One huge PR per feature — `#1306` 145 files
- [RECOMMENDATION] `SOURCE_011:381` — Stack PRs
- [REPORT_OBSERVATION] `SOURCE_011:381` — previous evidence: 08-29, 08-30, 08-31, 09-01 (`#1282`)

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- One huge PR per feature -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Template-only PR body on large PRs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:408` — Template-only PR body on large PRs
- [RECOMMENDATION] `SOURCE_011:408` — Automate with Devin — draft the body from the diff

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Template-only PR body on large PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Draft the `#1284` PR body (Why / schema / UI sections) from the diff so reviewers can start.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:412` — Draft the `#1284` PR body (Why / schema / UI sections) from the diff so reviewers can start.

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Draft the `#1284` PR body (Why / schema / UI sections) from the diff so reviewers can start. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Answer or triage the 17 open Devin findings.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:413` — Answer or triage the 17 open Devin findings.

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Answer or triage the 17 open Devin findings. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Unlanded feature branch

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:431` — Unlanded feature branch — closed unmerged, re-opened as 113 files
- [RECOMMENDATION] `SOURCE_011:431` — Stack
- [REPORT_OBSERVATION] `SOURCE_011:431` — previous evidence: `#1258` 08-28 → 09-01

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Unlanded feature branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Template-only body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:432` — Template-only body — `#1284`, `#1295`
- [RECOMMENDATION] `SOURCE_011:432` — Body before review
- [REPORT_OBSERVATION] `SOURCE_011:432` — previous evidence: `#1258`

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Template-only body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` One-word promotion approval

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:458` — One-word promotion approval
- [RECOMMENDATION] `SOURCE_011:458` — Improve documentation/process

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- One-word promotion approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Regression test across every `MergeDataBuilder` token source so the next opt-in feature cannot miss the send path.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:461` — Regression test across every `MergeDataBuilder` token source so the next opt-in feature cannot miss the send path.

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Regression test across every `MergeDataBuilder` token source so the next opt-in feature cannot miss the send path. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` One-word approval on promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:479` — One-word approval on promotion — `#1286` 601 files
- [RECOMMENDATION] `SOURCE_011:479` — Cite gate verdict
- [REPORT_OBSERVATION] `SOURCE_011:479` — previous evidence: 08-31

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- One-word approval on promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Empty approvals on every PR incl. prod

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:506` — Empty approvals on every PR incl. prod
- [RECOMMENDATION] `SOURCE_011:506` — Automate through scripts/tooling — block empty approvals on `Uat_1.0`/`release/`

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Empty approvals on every PR incl. prod -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Template-only PR bodies

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 7 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:507` — Template-only PR bodies
- [RECOMMENDATION] `SOURCE_011:507` — Automate with Devin
- [REPORT_OBSERVATION] `SOURCE_011:609` — Template-only bodies
- [RECOMMENDATION] `SOURCE_011:609` — Automate with Devin
- [REPORT_OBSERVATION] `SOURCE_011:705` — Template-only bodies
- [RECOMMENDATION] `SOURCE_011:705` — Automate with Devin

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Template-only PR bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` A PR-body generator invoked on open for `Dev_1.0` PRs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:510` — A PR-body generator invoked on open for `Dev_1.0` PRs.

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- A PR-body generator invoked on open for `Dev_1.0` PRs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` A Devin check that lists Devin Review findings still open at approval time in the approval dialog.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:511` — A Devin check that lists Devin Review findings still open at approval time in the approval dialog.

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- A Devin check that lists Devin Review findings still open at approval time in the approval dialog. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:529` — Empty approvals — 7/7 today incl. `#281` prod
- [RECOMMENDATION] `SOURCE_011:529` — Written verdict ≥ 2 sentences
- [REPORT_OBSERVATION] `SOURCE_011:529` — previous evidence: 08-30, 08-31, 09-01, 09-02

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Devin findings unanswered before promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:530` — Devin findings unanswered before promotion — `#602` 8 findings
- [RECOMMENDATION] `SOURCE_011:530` — Answer or waive
- [REPORT_OBSERVATION] `SOURCE_011:530` — previous evidence: 09-01 (`#411`)

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Devin findings unanswered before promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` One-word approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:558` — One-word approvals
- [RECOMMENDATION] `SOURCE_011:558` — Improve documentation/process

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- One-word approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Self-merge on `Dev_1.0`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:559` — Self-merge on `Dev_1.0`
- [RECOMMENDATION] `SOURCE_011:559` — Improve documentation/process

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Self-merge on `Dev_1.0` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Analytics config contract test (BE default ↔ FE fail-closed).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:562` — Analytics config contract test (BE default ↔ FE fail-closed).

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Analytics config contract test (BE default ↔ FE fail-closed). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Extend `#528`'s pattern to the remaining untested components — Devin can enumerate components without specs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:563` — Extend `#528`'s pattern to the remaining untested components — Devin can enumerate components without specs.

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Extend `#528`'s pattern to the remaining untested components — Devin can enumerate components without specs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:581` — Self-merge — `#526`
- [RECOMMENDATION] `SOURCE_011:581` — Second approver
- [REPORT_OBSERVATION] `SOURCE_011:581` — previous evidence: 09-01

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` One-word approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:582` — One-word approvals — `lgtm` ×2 on 145 files
- [RECOMMENDATION] `SOURCE_011:582` — Written verdict
- [REPORT_OBSERVATION] `SOURCE_011:582` — previous evidence: 09-01

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- One-word approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Per-facility prompt/mapping edits shipped to prod same day

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:608` — Per-facility prompt/mapping edits shipped to prod same day
- [RECOMMENDATION] `SOURCE_011:608` — Automate with Devin — golden-file suite per facility

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Per-facility prompt/mapping edits shipped to prod same day -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Golden-file regression suite for Trinity/PPV parsing.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:612` — Golden-file regression suite for Trinity/PPV parsing.

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Golden-file regression suite for Trinity/PPV parsing. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` PR body generation from commit messages (which are already descriptive).

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:613` — PR body generation from commit messages (which are already descriptive).

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- PR body generation from commit messages (which are already descriptive). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Template-only bodies

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:631` — Template-only bodies — `#280/#281`
- [RECOMMENDATION] `SOURCE_011:631` — Generate body
- [REPORT_OBSERVATION] `SOURCE_011:631` — previous evidence: 09-01

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Template-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Prompt changes to prod with 0 tests

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:632` — Prompt changes to prod with 0 tests — today
- [RECOMMENDATION] `SOURCE_011:632` — Golden files
- [REPORT_OBSERVATION] `SOURCE_011:632` — previous evidence: 08-31, 09-01

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Prompt changes to prod with 0 tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` `okay` approvals on prod/feature merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:658` — `okay` approvals on prod/feature merges
- [RECOMMENDATION] `SOURCE_011:658` — Improve documentation/process — release checklist

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- `okay` approvals on prod/feature merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Not a Devin task: a release checklist. Devin could generate the per-chart fixture set for the gate-threshold fix.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:661` — Not a Devin task: a release checklist. Devin could generate the per-chart fixture set for the gate-threshold fix.

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Not a Devin task: a release checklist. Devin could generate the per-chart fixture set for the gate-threshold fix. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` `okay` approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:679` — `okay` approvals — `#420`; `#419` no review
- [RECOMMENDATION] `SOURCE_011:679` — Written verdict; require 1 approval on `release/`
- [REPORT_OBSERVATION] `SOURCE_011:679` — previous evidence: 08-31, 09-01

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- `okay` approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` Per-chart fixtures for the gate-threshold logic; the bug class ("global instead of per chart") is testable.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:708` — Per-chart fixtures for the gate-threshold logic; the bug class ("global instead of per chart") is testable.

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- Per-chart fixtures for the gate-threshold logic; the bug class ("global instead of per chart") is testable. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000352` Template-only body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:726` — Template-only body — `#420`
- [RECOMMENDATION] `SOURCE_011:726` — Body before review
- [REPORT_OBSERVATION] `SOURCE_011:726` — previous evidence: 09-01

### DECISION: ISSUE_000352_ATTEMPT_01
<!-- Template-only body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000353` None observed in-window

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:751` — None observed in-window
- [RECOMMENDATION] `SOURCE_011:751` — —

### DECISION: ISSUE_000353_ATTEMPT_01
<!-- None observed in-window -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000354` Threshold-table test for every E/M band so the "14 minutes early, one unit high" class cannot recur.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:754` — Threshold-table test for every E/M band so the "14 minutes early, one unit high" class cannot recur.

### DECISION: ISSUE_000354_ATTEMPT_01
<!-- Threshold-table test for every E/M band so the "14 minutes early, one unit high" class cannot recur. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000355` None with history

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:772` — None with history — —
- [RECOMMENDATION] `SOURCE_011:772` — —
- [REPORT_OBSERVATION] `SOURCE_011:772` — previous evidence: —

### DECISION: ISSUE_000355_ATTEMPT_01
<!-- None with history -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

