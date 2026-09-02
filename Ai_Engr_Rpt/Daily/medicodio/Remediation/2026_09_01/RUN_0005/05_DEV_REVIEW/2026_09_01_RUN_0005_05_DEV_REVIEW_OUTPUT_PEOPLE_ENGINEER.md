# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-01 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Hand-written `docs/review-logs/` entries recording gate results

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:93` — Hand-written `docs/review-logs/` entries recording gate results
- [RECOMMENDATION] `SOURCE_011:93` — Automate through scripts/tooling — the gate runner already emits the results; the log should be generated, not typed

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs/review-logs/` entries recording gate results -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Backfilling function headers to satisfy the standards audit

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:94` — Backfilling function headers to satisfy the standards audit
- [RECOMMENDATION] `SOURCE_011:94` — Automate with Devin — a bounded, mechanical pass with a clear acceptance criterion

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Backfilling function headers to satisfy the standards audit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Fixing tests left stale by someone else's merge into `dev`

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:95` — Fixing tests left stale by someone else's merge into `dev`
- [RECOMMENDATION] `SOURCE_011:95` — Improve documentation/process — the merging author should own the fallout, or CI should run the full suite pre-merge

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Fixing tests left stale by someone else's merge into `dev` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate the HR-reports persona/permission test matrix that the QA gate could not execute — 8 report views × org-scoping × role, as code-level integration tests

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:99` — Delegate the HR-reports persona/permission test matrix that the QA gate could not execute — 8 report views × org-scoping × role, as code-level integration tests that need no live personas.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate the HR-reports persona/permission test matrix that the QA gate could not execute — 8 report views × org-scoping × role, as code-level integration tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate review-log generation from the gate runner's output, removing ~6 commits per feature branch.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:100` — Delegate review-log generation from the gate runner's output, removing ~6 commits per feature branch.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate review-log generation from the gate runner's output, removing ~6 commits per feature branch. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Delegate the 2 documented "unresolvable without a decision" findings as a scoped investigation producing options, once the product decision exists.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:101` — Delegate the 2 documented "unresolvable without a decision" findings as a scoped investigation producing options, once the product decision exists.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Delegate the 2 documented "unresolvable without a decision" findings as a scoped investigation producing options, once the product decision exists. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Approving and merging a PR one drove

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:125` — Approving and merging a PR one drove — `#1239`: her `APPROVED` at 01:52:52, her merge at 01:53:10 (18 s). She is not the GitHub author, but she is the driver
- [RECOMMENDATION] `SOURCE_011:125` — Have a second Global Codio reviewer sign off on branches you drove, even when the PR author is the bot
- [REPORT_OBSERVATION] `SOURCE_011:125` — previous evidence: Self-merges flagged 08-23 (4), 08-25 (4), 08-27 (3), 08-28 (2)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Approving and merging a PR one drove -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Merging ahead of the post-merge QA gate

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:126` — Merging ahead of the post-merge QA gate — `#1239` merged 01:53; QA gate `#1276` completed 02:15 with "feature untested"
- [RECOMMENDATION] `SOURCE_011:126` — Run the gate pre-merge, or treat a "no verdict" gate as a blocker to the promotion that follows
- [REPORT_OBSERVATION] `SOURCE_011:126` — previous evidence: Named in the 08-28 and 08-31 reports

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Merging ahead of the post-merge QA gate -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Fixing one content-sync decode/type class at a time

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:167` — Fixing one content-sync decode/type class at a time
- [RECOMMENDATION] `SOURCE_011:167` — Automate with Devin — a corpus fixture covering every Prisma column type round-tripped through export→import would surface the remaining classes in one session

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Fixing one content-sync decode/type class at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Re-typing the same "scannability" UI polish across import/export surfaces

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:168` — Re-typing the same "scannability" UI polish across import/export surfaces
- [RECOMMENDATION] `SOURCE_011:168` — Continue manually — judgement-heavy UX work with no stable acceptance criterion

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Re-typing the same "scannability" UI polish across import/export surfaces -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Content-sync type-coverage corpus: delegate a fixture bundle exercising every column type in `schema.prisma` (enum, enum[], `@db.Date`, JSON, nullable) round-tr

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:172` — Content-sync type-coverage corpus: delegate a fixture bundle exercising every column type in `schema.prisma` (enum, enum[], `@db.Date`, JSON, nullable) round-tripped against a live DB. Acceptance criterion: the four defects fixed today all fail against the pre-fix commits.

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Content-sync type-coverage corpus: delegate a fixture bundle exercising every column type in `schema.prisma` (enum, enum[], `@db.Date`, JSON, nullable) round-tr -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Delegate the red spec on `dev` that `#1267` reported, as a bounded fix-with-repro session.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:173` — Delegate the red spec on `dev` that `#1267` reported, as a bounded fix-with-repro session.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Delegate the red spec on `dev` that `#1267` reported, as a bounded fix-with-repro session. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Merge minutes after a content-free approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:196` — Merge minutes after a content-free approval — `#1263` merged 0.5 min after an empty approval by svh-medicodio; `#1266` 0.8 min, `#1270` 0.1 min, `#1271` 0.1 min after empty approvals by ragha82
- [RECOMMENDATION] `SOURCE_011:196` — Ask your reviewer for a one-line verdict; a 27-file import-path change deserves more than a click
- [REPORT_OBSERVATION] `SOURCE_011:196` — previous evidence: Low-information approvals flagged from 08-20 onward

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Merge minutes after a content-free approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Merging while a QA gate reports NOT READY

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:197` — Merging while a QA gate reports NOT READY — `#1267` ("NOT READY") published 15:21; content-sync merges continued at 17:58 and 18:26
- [RECOMMENDATION] `SOURCE_011:197` — Treat a NOT READY gate as blocking for the subsystem it names until it is answered or superseded
- [REPORT_OBSERVATION] `SOURCE_011:197` — previous evidence: Merging with unanswered Devin findings flagged 08-23, 08-25, 08-27, 08-28

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Merging while a QA gate reports NOT READY -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Placeholder commit messages

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:198` — Placeholder commit messages — "Implement feature X to enhance user experience and optimize performance"
- [RECOMMENDATION] `SOURCE_011:198` — Squash or rewrite before merge; the message is the only durable record of intent
- [REPORT_OBSERVATION] `SOURCE_011:198` — previous evidence: Not previously flagged for this member

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Placeholder commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Hand-written standards-audit and remediation logs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:237` — Hand-written standards-audit and remediation logs
- [RECOMMENDATION] `SOURCE_011:237` — Automate through scripts/tooling — generate from the gate runner

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Hand-written standards-audit and remediation logs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Correcting specs that "never caught up with what this branch changed"

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:238` — Correcting specs that "never caught up with what this branch changed"
- [RECOMMENDATION] `SOURCE_011:238` — Improve documentation/process — a draft PR from phase 1 runs CI continuously instead of in a batch at the end

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Correcting specs that "never caught up with what this branch changed" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Open the draft PR, then delegate the subscriber/notification test matrix for the draft-letter skill — this is the third report to recommend it and the branch no

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:242` — Open the draft PR, then delegate the subscriber/notification test matrix for the draft-letter skill — this is the third report to recommend it and the branch now has seven recorded test failures to anchor acceptance criteria.

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Open the draft PR, then delegate the subscriber/notification test matrix for the draft-letter skill — this is the third report to recommend it and the branch no -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Delegate the seven test failures recorded in today's gate log as a single bounded fix session.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:243` — Delegate the seven test failures recorded in today's gate log as a single bounded fix session.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Delegate the seven test failures recorded in today's gate log as a single bounded fix session. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Large feature accumulating without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:265` — Large feature accumulating without a PR — Third day; 34 more authored commits; still no PR, so no CI, no Devin Review, no human reviewer
- [RECOMMENDATION] `SOURCE_011:265` — Open a draft PR today, before the next phase
- [REPORT_OBSERVATION] `SOURCE_011:265` — previous evidence: Named in the 08-30 report (12 phases, no PR) and again on 08-31 (second day)

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Large feature accumulating without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Content-free approval on a very large diff

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:266` — Content-free approval on a very large diff — "approved" (8 chars) on an 80-file, 6,950-line PR, merged 1 minute later
- [RECOMMENDATION] `SOURCE_011:266` — For diffs above ~20 files, record what you checked, even in three lines
- [REPORT_OBSERVATION] `SOURCE_011:266` — previous evidence: Low-information approvals flagged from 08-20 onward

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Content-free approval on a very large diff -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Merging other people's PRs on `dev` minutes after opening

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:304` — Merging other people's PRs on `dev` minutes after opening
- [RECOMMENDATION] `SOURCE_011:304` — Improve documentation/process — the bottleneck is a named reviewer, not a merger

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Merging other people's PRs on `dev` minutes after opening -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` QA gates re-running the same credential-free probes and reaching no verdict

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: SECRETS
- Priority: 8 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:305` — QA gates re-running the same credential-free probes and reaching no verdict
- [RECOMMENDATION] `SOURCE_011:305` — Automate through scripts/tooling — provision seeded QA personas in hosted-dev; without them the gate cannot ever produce a verdict

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- QA gates re-running the same credential-free probes and reaching no verdict -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Delegate a seeded QA persona fixture for hosted-dev (idempotent seed script + credential storage), which unblocks every gate the automation currently cannot com

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: SECRETS
- Priority: 7 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:309` — Delegate a seeded QA persona fixture for hosted-dev (idempotent seed script + credential storage), which unblocks every gate the automation currently cannot complete.

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Delegate a seeded QA persona fixture for hosted-dev (idempotent seed script + credential storage), which unblocks every gate the automation currently cannot com -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Have the QA automation emit a machine-readable verdict (`READY` / `NOT READY` / `NO VERDICT`) as a required status check, so a NOT READY result blocks the next 

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:310` — Have the QA automation emit a machine-readable verdict (`READY` / `NOT READY` / `NO VERDICT`) as a required status check, so a NOT READY result blocks the next merge instead of being a comment.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Have the QA automation emit a machine-readable verdict (`READY` / `NOT READY` / `NO VERDICT`) as a required status check, so a NOT READY result blocks the next  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Content-free approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:333` — Content-free approvals — 3 of 3 today, followed by merges 0.1–0.8 min later
- [RECOMMENDATION] `SOURCE_011:333` — One line stating what you verified
- [REPORT_OBSERVATION] `SOURCE_011:333` — previous evidence: Flagged from 08-20 onward; 08-28 recorded 42 of 43

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Content-free approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` QA gate output not consumed

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:334` — QA gate output not consumed — `#1267` NOT READY at 15:21; two further content-sync merges after it
- [RECOMMENDATION] `SOURCE_011:334` — Promote the verdict to a required check
- [REPORT_OBSERVATION] `SOURCE_011:334` — previous evidence: 08-28 report: "the org pays for review it does not consume"

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- QA gate output not consumed -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Manually re-checking read-only enforcement across case tabs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:369` — Manually re-checking read-only enforcement across case tabs
- [RECOMMENDATION] `SOURCE_011:369` — Automate with Devin — a surface × state matrix test for closed/archived cases

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Manually re-checking read-only enforcement across case tabs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Delegate the closed/archived-case read-only enforcement matrix (every tab × every mutating action) as tests, which is exactly the manual verification `#1258` ke

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:373` — Delegate the closed/archived-case read-only enforcement matrix (every tab × every mutating action) as tests, which is exactly the manual verification `#1258` keeps repeating.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Delegate the closed/archived-case read-only enforcement matrix (every tab × every mutating action) as tests, which is exactly the manual verification `#1258` ke -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` PR awaiting a human verdict for days

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:395` — PR awaiting a human verdict for days — Still open, now in its 4th day, updated today
- [RECOMMENDATION] `SOURCE_011:395` — Ask for a named reviewer and a date, or split it
- [REPORT_OBSERVATION] `SOURCE_011:395` — previous evidence: `#1258` flagged as carried-forward on 08-30 and 08-31

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- PR awaiting a human verdict for days -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Content-free approval on a large diff

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:396` — Content-free approval on a large diff — Empty approval on a 27-file import-path change
- [RECOMMENDATION] `SOURCE_011:396` — One line stating what you verified
- [REPORT_OBSERVATION] `SOURCE_011:396` — previous evidence: Org-wide pattern flagged from 08-20

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Content-free approval on a large diff -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Duplicating each change into a `-dev` and a `-prod` branch and PR by hand

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:432` — Duplicating each change into a `-dev` and a `-prod` branch and PR by hand
- [RECOMMENDATION] `SOURCE_011:432` — Automate through scripts/tooling — a promotion script or cherry-pick workflow

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Duplicating each change into a `-dev` and a `-prod` branch and PR by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Iterating access-control rules by successive small fixes

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 7 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:433` — Iterating access-control rules by successive small fixes
- [RECOMMENDATION] `SOURCE_011:433` — Automate with Devin — a decision-table test would settle the rules before the code moves

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Iterating access-control rules by successive small fixes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Delegate an approver-routing decision-table test suite: (requester role × affected client × peer availability × Support fallback) → expected approver. This is s

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:437` — Delegate an approver-routing decision-table test suite: (requester role × affected client × peer availability × Support fallback) → expected approver. This is security-relevant logic currently shipping with no tests.

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Delegate an approver-routing decision-table test suite: (requester role × affected client × peer availability × Support fallback) → expected approver. This is s -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Delegate the dev→prod promotion script that removes the manual six-PR fan-out.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:438` — Delegate the dev→prod promotion script that removes the manual six-PR fan-out.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Delegate the dev→prod promotion script that removes the manual six-PR fan-out. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Security-sensitive change with no tests

- Category: SECURITY_TENANCY · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 7 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:460` — Security-sensitive change with no tests — Break-glass approval routing changed three times today; no test commit
- [RECOMMENDATION] `SOURCE_011:460` — One delegated test session per access-control rule change
- [REPORT_OBSERVATION] `SOURCE_011:460` — previous evidence: 08-27 and 08-28: "zero tests in the Medicodio repositories"

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Security-sensitive change with no tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Manual dev/prod PR fan-out

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:461` — Manual dev/prod PR fan-out — 6 PRs for 3 changes; 2 prod PRs left open
- [RECOMMENDATION] `SOURCE_011:461` — Script the promotion
- [REPORT_OBSERVATION] `SOURCE_011:461` — previous evidence: Every report since 08-20

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Manual dev/prod PR fan-out -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` Self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:462` — Self-merge — `#516` self-merged after an empty approval
- [RECOMMENDATION] `SOURCE_011:462` — Require a non-author approver on `Dev_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:462` — previous evidence: Self-merges flagged 08-23, 08-25, 08-27, 08-28

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- Self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Clicking approve on every open Medicodio PR in a batch

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:497` — Clicking approve on every open Medicodio PR in a batch
- [RECOMMENDATION] `SOURCE_011:497` — Improve documentation/process — a one-line verdict requirement; batching approvals is not review

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Clicking approve on every open Medicodio PR in a batch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Hand-diagnosing PE-integration state-machine violations from production symptoms

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:498` — Hand-diagnosing PE-integration state-machine violations from production symptoms
- [RECOMMENDATION] `SOURCE_011:498` — Automate with Devin — a contract test over the status × coding_mode transition table

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Hand-diagnosing PE-integration state-machine violations from production symptoms -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Delegate a PE-integration status-transition contract test enumerating every `status` × `coding_mode` pair against `chk_ready_status_matches_coding_mode`. Accept

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:502` — Delegate a PE-integration status-transition contract test enumerating every `status` × `coding_mode` pair against `chk_ready_status_matches_coding_mode`. Acceptance criterion: the pre-fix code fails it.

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Delegate a PE-integration status-transition contract test enumerating every `status` × `coding_mode` pair against `chk_ready_status_matches_coding_mode`. Accept -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Delegate the prompt-registry contract tests behind `#249`, open for 5 days.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:503` — Delegate the prompt-registry contract tests behind `#249`, open for 5 days.

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Delegate the prompt-registry contract tests behind `#249`, open for 5 days. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Link `amit.p@medicodio.ai` to the GitHub account so delegation stops being invisible.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:504` — Link `amit.p@medicodio.ai` to the GitHub account so delegation stops being invisible.

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Link `amit.p@medicodio.ai` to the GitHub account so delegation stops being invisible. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Content-free approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:527` — Content-free approvals — 9 of 9 empty today
- [RECOMMENDATION] `SOURCE_011:527` — Require a one-line verdict; make it a merge gate for `release/prod_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:527` — previous evidence: Identified 08-20; restated 08-21, 08-22, 08-23, 08-25, 08-27, 08-28 (20 by him in one day)

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Content-free approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Approving and merging production promotions in seconds

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:528` — Approving and merging production promotions in seconds — `#597` approved 08:02:05, merged 08:02:13; `#517` approved 08:02:33, merged 08:02:39
- [RECOMMENDATION] `SOURCE_011:528` — No self-approval on `release/prod_1.0`; require a named second reviewer and a written verdict
- [REPORT_OBSERVATION] `SOURCE_011:528` — previous evidence: 08-28: "15 production-bound merges with essentially no recorded reasoning"

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Approving and merging production promotions in seconds -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Re-creating the same change as a `prod_fix_issue` branch and PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:564` — Re-creating the same change as a `prod_fix_issue` branch and PR
- [RECOMMENDATION] `SOURCE_011:564` — Automate through scripts/tooling — a promotion script that carries the original body and reviewers forward

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Re-creating the same change as a `prod_fix_issue` branch and PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Hand-fixing column-visibility edge cases one at a time

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:565` — Hand-fixing column-visibility edge cases one at a time
- [RECOMMENDATION] `SOURCE_011:565` — Automate with Devin — a column-state regression matrix (default / user-hidden / returning user / export)

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Hand-fixing column-visibility edge cases one at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Delegate the column-visibility and export regression matrix for the Chart Queue and History tables — the same class of edge case has now been fixed twice by han

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:569` — Delegate the column-visibility and export regression matrix for the Chart Queue and History tables — the same class of edge case has now been fixed twice by hand.

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Delegate the column-visibility and export regression matrix for the Chart Queue and History tables — the same class of edge case has now been fixed twice by han -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Delegate generation of promotion PR bodies from the underlying dev PR, so a production change never arrives with an empty body.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:570` — Delegate generation of promotion PR bodies from the underlying dev PR, so a production change never arrives with an empty body.

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Delegate generation of promotion PR bodies from the underlying dev PR, so a production change never arrives with an empty body. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Template-only body on a production promotion

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:593` — Template-only body on a production promotion — `#597` (447 chars) and `#517` (446 chars), both "Prod fix issue", both into `release/prod_1.0`
- [RECOMMENDATION] `SOURCE_011:593` — Carry the dev PR's body into the promotion; reject empty templates in CI
- [REPORT_OBSERVATION] `SOURCE_011:593` — previous evidence: 08-22 (`#1202`), 08-24 (`#1232`, `#1234`), 08-27, 08-28 (11 PRs with 439–448-character bodies)

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Template-only body on a production promotion -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Self-merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:594` — Self-merge — `#513` self-merged 21 min after an empty approval
- [RECOMMENDATION] `SOURCE_011:594` — Require a non-author merger
- [REPORT_OBSERVATION] `SOURCE_011:594` — previous evidence: Flagged 08-23, 08-25, 08-27, 08-28

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Self-merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Client onboarding: create config, seed KB chart-field mappings, add payer-header variants

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:628` — Client onboarding: create config, seed KB chart-field mappings, add payer-header variants
- [RECOMMENDATION] `SOURCE_011:628` — Automate with Devin — a scaffold generator taking a client profile and emitting config + mappings + a validation check; the steps are identical per client

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Client onboarding: create config, seed KB chart-field mappings, add payer-header variants -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Provider-specific payer-header variants added one at a time

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:629` — Provider-specific payer-header variants added one at a time
- [RECOMMENDATION] `SOURCE_011:629` — Automate through scripts/tooling — drive from a header-alias table rather than code changes

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Provider-specific payer-header variants added one at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Delegate a client-onboarding scaffold generator with the two clients onboarded today as the acceptance fixtures. This is the highest-value repetitive-work remov

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:633` — Delegate a client-onboarding scaffold generator with the two clients onboarded today as the acceptance fixtures. This is the highest-value repetitive-work removal in the Medicodio integration repo.

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Delegate a client-onboarding scaffold generator with the two clients onboarded today as the acceptance fixtures. This is the highest-value repetitive-work remov -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Delegate a KB mapping validation test that fails when a newly onboarded client is missing a required chart-field mapping.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:634` — Delegate a KB mapping validation test that fails when a newly onboarded client is missing a required chart-field mapping.

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Delegate a KB mapping validation test that fails when a newly onboarded client is missing a required chart-field mapping. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` Self-merge with no review at all

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:656` — Self-merge with no review at all — `#268` and `#269`, both self-merged, zero human and zero recorded response to bot review
- [RECOMMENDATION] `SOURCE_011:656` — Branch protection on `Dev_1.0` requiring a non-author approver
- [REPORT_OBSERVATION] `SOURCE_011:656` — previous evidence: 08-22 (two Elaris branches), 08-23, 08-25, 08-27, 08-28 (`#254`)

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- Self-merge with no review at all -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Template-only PR bodies

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:657` — Template-only PR bodies — Both PRs at 448 characters, badge only
- [RECOMMENDATION] `SOURCE_011:657` — Generate bodies from the diff
- [REPORT_OBSERVATION] `SOURCE_011:657` — previous evidence: 08-22 → 08-28

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Template-only PR bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Onboarding done by hand each time

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:658` — Onboarding done by hand each time — Two more clients onboarded the same manual way
- [RECOMMENDATION] `SOURCE_011:658` — Delegate the scaffold generator
- [REPORT_OBSERVATION] `SOURCE_011:658` — previous evidence: Recognised as repetitive on 08-22 and 08-27

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Onboarding done by hand each time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Reverting UI redesigns after they reach `Dev_1.0`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:691` — Reverting UI redesigns after they reach `Dev_1.0`
- [RECOMMENDATION] `SOURCE_011:691` — Improve documentation/process — agree the target design before implementation; a revert is an expensive review mechanism

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Reverting UI redesigns after they reach `Dev_1.0` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Delegate a visual-regression snapshot suite for the Prediction Trail stage rail so a UI change's effect is visible in the PR rather than after the fact.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:695` — Delegate a visual-regression snapshot suite for the Prediction Trail stage rail so a UI change's effect is visible in the PR rather than after the fact.

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Delegate a visual-regression snapshot suite for the Prediction Trail stage rail so a UI change's effect is visible in the PR rather than after the fact. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Commits under an unlinked author email

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:718` — Commits under an unlinked author email — Unchanged today
- [RECOMMENDATION] `SOURCE_011:718` — Link the email to the GitHub account so contribution and Devin attribution are accurate
- [REPORT_OBSERVATION] `SOURCE_011:718` — previous evidence: 08-23 report flagged `hitesh.ms@medicodio.ai`

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Commits under an unlinked author email -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Manually validating combination-code collapse against the KB table

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:753` — Manually validating combination-code collapse against the KB table
- [RECOMMENDATION] `SOURCE_011:753` — Automate with Devin — KB-table-driven fixtures asserting the collapse rule per row

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Manually validating combination-code collapse against the KB table -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Delegate KB-table-driven combination-code fixtures so the I.B.9 collapse rule is verified per row rather than by inspection.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:757` — Delegate KB-table-driven combination-code fixtures so the I.B.9 collapse rule is verified per row rather than by inspection.

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Delegate KB-table-driven combination-code fixtures so the I.B.9 collapse rule is verified per row rather than by inspection. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` Delegate a triage pass over the 8 unanswered Devin Review comments on `#411`, producing accept/reject decisions.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:758` — Delegate a triage pass over the 8 unanswered Devin Review comments on `#411`, producing accept/reject decisions.

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- Delegate a triage pass over the 8 unanswered Devin Review comments on `#411`, producing accept/reject decisions. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Long-lived PR with unanswered Devin findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:780` — Long-lived PR with unanswered Devin findings — `#411` in its 5th day, 8 unanswered Devin comments across two review runs
- [RECOMMENDATION] `SOURCE_011:780` — Answer or dismiss each finding with a reason, then request a human reviewer
- [REPORT_OBSERVATION] `SOURCE_011:780` — previous evidence: `#411` named as carried-forward on 08-30 and 08-31; `#393` draft since 08-25 flagged on 08-30

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Long-lived PR with unanswered Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Draft PR left open across many days

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:781` — Draft PR left open across many days — `#393` draft since 08-25, 7th day
- [RECOMMENDATION] `SOURCE_011:781` — Land it, split it, or close it with a stated decision
- [REPORT_OBSERVATION] `SOURCE_011:781` — previous evidence: 08-22/08-23 (`#373`, 7 days), 08-30, 08-31

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Draft PR left open across many days -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

