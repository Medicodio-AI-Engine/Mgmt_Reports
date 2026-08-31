# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-08-30 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000002` Low automation-adoption signal for akanksh-rv

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:39` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000002_ATTEMPT_01
<!-- Low automation-adoption signal for akanksh-rv -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000282` Hand-writing the `/check` → `/fix` remediation commits after each gate run

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:87` — Hand-writing the `/check` → `/fix` remediation commits after each gate run
- [RECOMMENDATION] `SOURCE_011:87` — Automate with Devin — the gate output is a precise, bounded work list; delegate the mechanical fixes and keep the verification for herself

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-writing the `/check` → `/fix` remediation commits after each gate run -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Authoring the review-log markdown for each gate pass

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:88` — Authoring the review-log markdown for each gate pass
- [RECOMMENDATION] `SOURCE_011:88` — Automate through scripts/tooling — generate the log skeleton from the gate output; she writes only the verdict

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Authoring the review-log markdown for each gate pass -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Re-deriving whether a Devin finding is real

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:89` — Re-deriving whether a Devin finding is real
- [RECOMMENDATION] `SOURCE_011:89` — Improve documentation/process — publish her "verified real / verified dormant / rejected" labelling as the org's standard reply format

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Re-deriving whether a Devin finding is real -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and o

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:93` — Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and one wrong test all lived in that matrix.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and o -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the `data_flows.md` AI Case Manager entity section, the one gap her own review left open and recommended as a fast follow-up.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:94` — Delegate the `data_flows.md` AI Case Manager entity section, the one gap her own review left open and recommended as a fast follow-up.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the `data_flows.md` AI Case Manager entity section, the one gap her own review left open and recommended as a fast follow-up. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Delegate the `/fix` remediation pass on her next feature close-out and keep the review for herself, so verification and remediation are not done by the same han

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:95` — Delegate the `/fix` remediation pass on her next feature close-out and keep the review for herself, so verification and remediation are not done by the same hands in the same hour.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Delegate the `/fix` remediation pass on her next feature close-out and keep the review for herself, so verification and remediation are not done by the same han -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Approve-and-merge within seconds of the last automated report

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:119` — Approve-and-merge within seconds of the last automated report — Approved 06:56:38 and merged 06:56:58, 37 s after a new Devin Review finding posted at 06:56:21
- [RECOMMENDATION] `SOURCE_011:119` — Treat an unanswered findings report as a merge blocker regardless of who the author is; her own thread format already provides the reply mechanism
- [REPORT_OBSERVATION] `SOURCE_011:119` — previous evidence: 08-29 report: org-wide pattern of merging minutes after a findings report (Medicodio #412, #413)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Approve-and-merge within seconds of the last automated report -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Reviewer and remediator are the same person

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:120` — Reviewer and remediator are the same person — She wrote the 13 remediation commits and then the review that approved them
- [RECOMMENDATION] `SOURCE_011:120` — Have the remediation delegated (to Devin or another engineer) so the review is genuinely second-pair-of-eyes
- [REPORT_OBSERVATION] `SOURCE_011:120` — previous evidence: 08-28 (#1256, same shape)

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Reviewer and remediator are the same person -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Hand-fixing blockers found by his own audit pass on a Devin-authored branch

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:158` — Hand-fixing blockers found by his own audit pass on a Devin-authored branch
- [RECOMMENDATION] `SOURCE_011:158` — Automate with Devin — feed the audit findings back as a scoped follow-up session rather than fixing them in the reviewer's hands

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Hand-fixing blockers found by his own audit pass on a Devin-authored branch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Re-running and re-recording gate results across three review logs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:159` — Re-running and re-recording gate results across three review logs
- [RECOMMENDATION] `SOURCE_011:159` — Automate through scripts/tooling — write the gate log from the run output so a "real results" correction commit cannot be needed

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Re-running and re-recording gate results across three review logs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Discovering that a spec suite mocks the data layer and therefore cannot fail

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:160` — Discovering that a spec suite mocks the data layer and therefore cannot fail
- [RECOMMENDATION] `SOURCE_011:160` — Improve documentation/process — a repo rule that any spec covering a persistence path must have a non-mocked integration counterpart

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Discovering that a spec suite mocks the data layer and therefore cannot fail -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Delegate a non-mocked content-sync integration suite (export → bundle → import → rollback against a real schema). This is the highest-value delegable suite in G

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:164` — Delegate a non-mocked content-sync integration suite (export → bundle → import → rollback against a real schema). This is the highest-value delegable suite in Global Codio right now: six of the seven blockers were invisible to the existing specs.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Delegate a non-mocked content-sync integration suite (export → bundle → import → rollback against a real schema). This is the highest-value delegable suite in G -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Delegate the export/import round-trip fixtures for every registry table, including the JSON-expression natural key case that failed.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:165` — Delegate the export/import round-trip fixtures for every registry table, including the JSON-expression natural key case that failed.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Delegate the export/import round-trip fixtures for every registry table, including the JSON-expression natural key case that failed. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Delegate the six `[needs decision]` items as one scoped follow-up PR with his decisions written as acceptance criteria — they are currently merged and unresolve

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:166` — Delegate the six `[needs decision]` items as one scoped follow-up PR with his decisions written as acceptance criteria — they are currently merged and unresolved.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Delegate the six `[needs decision]` items as one scoped follow-up PR with his decisions written as acceptance criteria — they are currently merged and unresolve -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Reviewer-of-own-work

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:190` — Reviewer-of-own-work — He is #1244's principal contributor and the author of its only substantive review; the independent approval that followed was 8 characters
- [RECOMMENDATION] `SOURCE_011:190` — For PRs where the reviewer is also the main contributor, require a second named reviewer before merge
- [REPORT_OBSERVATION] `SOURCE_011:190` — previous evidence: 08-29 report noted he works inside #1244 and answers its findings

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Reviewer-of-own-work -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Very large PR instead of a reviewable series

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:191` — Very large PR instead of a reviewable series — #1244 merged at 125 files / 122 commits / +25,798
- [RECOMMENDATION] `SOURCE_011:191` — Size threshold that forces either a split or a named architect reviewer who is not a contributor
- [REPORT_OBSERVATION] `SOURCE_011:191` — previous evidence: 08-27, 08-28, 08-29 reports (#1239, #1244, #1260)

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Very large PR instead of a reviewable series -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Merge with `[needs decision]` items open

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:192` — Merge with `[needs decision]` items open — Six `[needs decision]` items raised 16:02:39; merged 16:09:12 with no intervening commit
- [RECOMMENDATION] `SOURCE_011:192` — Convert each to a tracked issue with an owner before the merge button, or hold the merge
- [REPORT_OBSERVATION] `SOURCE_011:192` — previous evidence: New this window at this severity

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Merge with `[needs decision]` items open -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Implementing near-identical subscriber + notification + repository-hook trios per AI skill

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:228` — Implementing near-identical subscriber + notification + repository-hook trios per AI skill
- [RECOMMENDATION] `SOURCE_011:228` — Automate with Devin — one worked example exists; the remaining skills are repetitive implementation across similar modules

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Implementing near-identical subscriber + notification + repository-hook trios per AI skill -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Accumulating many phases on one branch before opening a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:229` — Accumulating many phases on one branch before opening a PR
- [RECOMMENDATION] `SOURCE_011:229` — Improve documentation/process — open the PR at phase 1 as a draft and let it grow reviewably

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Accumulating many phases on one branch before opening a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Hand-writing per-phase tests unevenly (3 of 8 commits)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:230` — Hand-writing per-phase tests unevenly (3 of 8 commits)
- [RECOMMENDATION] `SOURCE_011:230` — Automate with Devin — delegate the permission/scope and subscriber-failure matrices

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Hand-writing per-phase tests unevenly (3 of 8 commits) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Revie

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:234` — Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Review Queue signpost depends on.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Revie -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Delegate the AI-skill registry contract test so any new skill provider must satisfy the same interface the `DraftStepStartedSubscriber` rewire assumes.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:235` — Delegate the AI-skill registry contract test so any new skill provider must satisfy the same interface the `DraftStepStartedSubscriber` rewire assumes.

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Delegate the AI-skill registry contract test so any new skill provider must satisfy the same interface the `DraftStepStartedSubscriber` rewire assumes. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Delegate phase-by-phase PR preparation: each numbered phase becomes its own small PR with the acceptance criteria you already write in the commit subject.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:236` — Delegate phase-by-phase PR preparation: each numbered phase becomes its own small PR with the acceptance criteria you already write in the commit subject.

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Delegate phase-by-phase PR preparation: each numbered phase becomes its own small PR with the acceptance criteria you already write in the commit subject. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` One very large PR instead of a reviewable series

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:259` — One very large PR instead of a reviewable series — #1260 merged at 161 files / 80 commits; the successor branch is accumulating the same way
- [RECOMMENDATION] `SOURCE_011:259` — Open the current branch as a draft PR now and split at phase boundaries
- [REPORT_OBSERVATION] `SOURCE_011:259` — previous evidence: 08-29 report flagged #1260 at 152 files as a team-level pattern with him named

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- One very large PR instead of a reviewable series -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Tests that encode current behaviour rather than intended behaviour

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:260` — Tests that encode current behaviour rather than intended behaviour — Corrected by the reviewer, not by the author
- [RECOMMENDATION] `SOURCE_011:260` — Write the assertion from the PRD acceptance criterion, not from the observed output
- [REPORT_OBSERVATION] `SOURCE_011:260` — previous evidence: New, but material: a #1260 test asserted the instance-filter bug as expected

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Tests that encode current behaviour rather than intended behaviour -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` No observable Devin leverage

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:261` — No observable Devin leverage — Unchanged this window
- [RECOMMENDATION] `SOURCE_011:261` — Delegate one bounded item (the subscriber test matrix) and report the outcome
- [REPORT_OBSERVATION] `SOURCE_011:261` — previous evidence: 08-29 report: "None observed — no Devin-trailer commits, no delegated sub-PRs"

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- No observable Devin leverage -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Signing off large merges with a one-word body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:294` — Signing off large merges with a one-word body
- [RECOMMENDATION] `SOURCE_011:294` — Improve documentation/process — a required approval template: what you checked, what you accepted, what remains open

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Signing off large merges with a one-word body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Manually judging whether a large PR is safe to merge

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:295` — Manually judging whether a large PR is safe to merge
- [RECOMMENDATION] `SOURCE_011:295` — Automate through scripts/tooling — a required status check that fails while an unanswered Devin Review finding or an unresolved `[needs decision]` comment exists

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Manually judging whether a large PR is safe to merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Assembling the release/promotion summary

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:296` — Assembling the release/promotion summary
- [RECOMMENDATION] `SOURCE_011:296` — Automate with Devin — generate the merge summary from the commit range

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Assembling the release/promotion summary -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Delegate a pre-merge gate check — a small CI job (Devin can write it in one scoped session) that blocks merge while any Devin Review finding or `[needs decision

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:300` — Delegate a pre-merge gate check — a small CI job (Devin can write it in one scoped session) that blocks merge while any Devin Review finding or `[needs decision]` review comment on the PR is unresolved. This directly addresses the one weak practice visible in her record.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Delegate a pre-merge gate check — a small CI job (Devin can write it in one scoped session) that blocks merge while any Devin Review finding or `[needs decision -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Delegate generation of the merge/promotion summary from the commit range so the approval body is substantive by construction.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:301` — Delegate generation of the merge/promotion summary from the commit range so the approval body is substantive by construction.

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Delegate generation of the merge/promotion summary from the commit range so the approval body is substantive by construction. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Approval without content on a very large PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:324` — Approval without content on a very large PR — 8-character `approved` on #1244 (125 files)
- [RECOMMENDATION] `SOURCE_011:324` — Require a non-empty approval body on `dev`/`uat`/`main`; adopt SaijyotiMeti's three-line verdict format
- [REPORT_OBSERVATION] `SOURCE_011:324` — previous evidence: 08-29 report: 8-character approval on the 331-file prod PR #1254; the pattern is documented every day since 08-26

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Approval without content on a very large PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Merge over an unresolved findings/decision set

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:325` — Merge over an unresolved findings/decision set — #1244 merged 6 m 22 s after six `[needs decision]` items, no intervening commit
- [RECOMMENDATION] `SOURCE_011:325` — Make unresolved findings a hard merge blocker; this is the highest-leverage single change available to the org
- [REPORT_OBSERVATION] `SOURCE_011:325` — previous evidence: 08-29 report: Medicodio #412 merged 96 s and #413 75 s after findings reports

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Merge over an unresolved findings/decision set -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

