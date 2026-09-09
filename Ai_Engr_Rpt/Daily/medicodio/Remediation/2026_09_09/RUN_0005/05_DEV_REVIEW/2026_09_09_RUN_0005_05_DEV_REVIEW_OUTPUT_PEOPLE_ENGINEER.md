# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-09 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Dev→UAT / UAT→prod promotion PRs with badge-only bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:58` — Dev→UAT / UAT→prod promotion PRs with badge-only bodies
- [RECOMMENDATION] `SOURCE_011:58` — Automate through scripts/tooling — generate the promotion body (included PRs + open-findings count) from `git log`; a human still merges

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Dev→UAT / UAT→prod promotion PRs with badge-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` CI-probe no-op PR to exercise the unit-test stage

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:59` — CI-probe no-op PR to exercise the unit-test stage
- [RECOMMENDATION] `SOURCE_011:59` — Automate through scripts/tooling — `workflow_dispatch` on the unit-test job (3rd recommendation)

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- CI-probe no-op PR to exercise the unit-test stage -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Same-morning "address Devin review" follow-up commits

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Same-morning "address Devin review" follow-up commits
- [RECOMMENDATION] `SOURCE_011:60` — Improve documentation/process — reply inline with SHA so the disposition is recorded; use Devin's auto-fix where scope is clear

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Same-morning "address Devin review" follow-up commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review foun

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:63` — Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review found in three rounds today.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review foun -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:64` — Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate).

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:65` — Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Empty approvals on prod-path PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:83` — Empty approvals on prod-path PRs — 8 approvals today, all 0-char incl. prod `#298` merged 1 min after open with 1 Devin finding
- [RECOMMENDATION] `SOURCE_011:83` — One sentence per approval naming what was checked; do not approve with open findings
- [REPORT_OBSERVATION] `SOURCE_011:83` — previous evidence: 09-04, 09-05, 09-07, 09-08 ("lgtm", "okok", empty)

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Empty approvals on prod-path PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` CI-probe PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:84` — CI-probe PRs — `#549` closed unmerged today
- [RECOMMENDATION] `SOURCE_011:84` — Add `workflow_dispatch` this week
- [REPORT_OBSERVATION] `SOURCE_011:84` — previous evidence: 09-05 recommendation; 09-07 `#549` opened

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- CI-probe PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Prod promotions with badge-only body

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:110` — Prod promotions with badge-only body
- [RECOMMENDATION] `SOURCE_011:110` — Automate through scripts/tooling — scripted promotion body listing included PRs + open findings

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Prod promotions with badge-only body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Manual verification of add-on state edge cases

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:111` — Manual verification of add-on state edge cases
- [RECOMMENDATION] `SOURCE_011:111` — Automate with Devin — unit tests for the add-on state machine

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Manual verification of add-on state edge cases -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases.

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Coder-performance dedupe golden fixtures (scope filter on/off).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:115` — Coder-performance dedupe golden fixtures (scope filter on/off).

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Coder-performance dedupe golden fixtures (scope filter on/off). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Empty approvals on prod promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:133` — Empty approvals on prod promotions — `#620`, `#551` (180 files), `#300` merged with 0-char approvals; `#300` with 3 open findings
- [RECOMMENDATION] `SOURCE_011:133` — Approval text must list the open-findings count and the smoke check done
- [REPORT_OBSERVATION] `SOURCE_011:133` — previous evidence: 09-04 → 09-08 (3–5 per day)

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Empty approvals on prod promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:158` — Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`)
- [RECOMMENDATION] `SOURCE_011:158` — Automate through scripts/tooling — prompt-registry diff check in CI that fails when Dev/UAT prompt text and its assertion diverge

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Two prod promotions per day

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:159` — Two prod promotions per day
- [RECOMMENDATION] `SOURCE_011:159` — Improve documentation/process — batch to one daily promotion with a findings checklist

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Two prod promotions per day -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:162` — Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand.

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:163` — A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests).

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Prod promotion with unanswered Devin findings

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:181` — Prod promotion with unanswered Devin findings — `#298` 1, `#300` 3 findings unanswered at merge
- [RECOMMENDATION] `SOURCE_011:181` — Resolve or reject findings on the UAT PR before raising the prod PR
- [REPORT_OBSERVATION] `SOURCE_011:181` — previous evidence: 09-05 (`#291` 4), 09-08 (`#291`, `#294`)

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Prod promotion with unanswered Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Selector / dialog timing fixes discovered by running the robot

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:207` — Selector / dialog timing fixes discovered by running the robot
- [RECOMMENDATION] `SOURCE_011:207` — Automate through scripts/tooling — record-and-assert harness on a captured page so selectors are verified without a full run

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Selector / dialog timing fixes discovered by running the robot -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Self-merge of feature branch to `main`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:208` — Self-merge of feature branch to `main`
- [RECOMMENDATION] `SOURCE_011:208` — Improve documentation/process — require one reviewer + Devin Review on the repo

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Self-merge of feature branch to `main` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:211` — Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:212` — Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate.

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Add `robocop`/dry-run lint as a GitHub Action.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:213` — Add `robocop`/dry-run lint as a GitHub Action.

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Add `robocop`/dry-run lint as a GitHub Action. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Empty approvals on integration prod path

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:231` — Empty approvals on integration prod path — `#295`, `#297` 0-char, `#295` merged in 54 s with 3 findings
- [RECOMMENDATION] `SOURCE_011:231` — Read the Devin report before approving
- [REPORT_OBSERVATION] `SOURCE_011:231` — previous evidence: 09-08 (5)

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Empty approvals on integration prod path -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Self-merge, no review (new)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:232` — Self-merge, no review (new) — `#17` +5,509 merged 12 s after open, empty body
- [RECOMMENDATION] `SOURCE_011:232` — Branch protection: 1 review required
- [REPORT_OBSERVATION] `SOURCE_011:232` — previous evidence: — (first report)

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Self-merge, no review (new) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` One-word approvals ("okay")

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:256` — One-word approvals ("okay")
- [RECOMMENDATION] `SOURCE_011:256` — Improve documentation/process — approval names what was checked

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- One-word approvals ("okay") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Manual `client_configs` list edits that silently regress (`04d7512c`)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:257` — Manual `client_configs` list edits that silently regress (`04d7512c`)
- [RECOMMENDATION] `SOURCE_011:257` — Automate with Devin — parametrised test asserting every specialty bundle declares `key_input_parameters`

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Manual `client_configs` list edits that silently regress (`04d7512c`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:260` — Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did.

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Ask Devin for an open-findings digest before merging others' PRs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:261` — Ask Devin for an open-findings digest before merging others' PRs.

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Ask Devin for an open-findings digest before merging others' PRs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` One-word approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:279` — One-word approvals — `#436` "okay" (1 finding open), `#437` "okay "
- [RECOMMENDATION] `SOURCE_011:279` — Apply the `#438` disposition standard to PRs you approve
- [REPORT_OBSERVATION] `SOURCE_011:279` — previous evidence: 08-27 → 09-08 (5 reports)

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- One-word approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Ordering/routing logic verified by reading, not golden tests

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:303` — Ordering/routing logic verified by reading, not golden tests
- [RECOMMENDATION] `SOURCE_011:303` — Automate with Devin — golden-file tests for assembler ordering

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Ordering/routing logic verified by reading, not golden tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:306` — Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists.

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Golden tests for routing/assembly absent

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:324` — Golden tests for routing/assembly absent — No test commit with `#436`
- [RECOMMENDATION] `SOURCE_011:324` — Delegate to Devin this week
- [REPORT_OBSERVATION] `SOURCE_011:324` — previous evidence: 09-05, 09-08 recommendations

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Golden tests for routing/assembly absent -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000129` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:347` — —
- [RECOMMENDATION] `SOURCE_011:347` — —
- [REPORT_OBSERVATION] `SOURCE_011:368` — — — —
- [RECOMMENDATION] `SOURCE_011:368` — —
- [REPORT_OBSERVATION] `SOURCE_011:368` — previous evidence: —

### DECISION: ISSUE_000129_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:350` — Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded.

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:392` — Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today)
- [RECOMMENDATION] `SOURCE_011:392` — Improve documentation/process — close superseded PRs; one PR per design

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:395` — Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation).

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` Unanswered Devin findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:413` — Unanswered Devin findings — `#434` 6, `#435` 7
- [RECOMMENDATION] `SOURCE_011:413` — Disposition each finding before requesting approval
- [REPORT_OBSERVATION] `SOURCE_011:413` — previous evidence: 09-08 (`#415`, 8)

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- Unanswered Devin findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` One-word approvals on PRs with open findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:437` — One-word approvals on PRs with open findings
- [RECOMMENDATION] `SOURCE_011:437` — Improve documentation/process

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- One-word approvals on PRs with open findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:440` — Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change.

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` Checkpoint round-trip tests (write → resume → identical output).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:441` — Checkpoint round-trip tests (write → resume → identical output).

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- Checkpoint round-trip tests (write → resume → identical output). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Approves / merges with open findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:459` — Approves / merges with open findings — `#435` ×2 with 7 findings open
- [RECOMMENDATION] `SOURCE_011:459` — Read the findings; approve only with a written status
- [REPORT_OBSERVATION] `SOURCE_011:459` — previous evidence: 09-05, 09-08 (`#431`, `#432`)

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Approves / merges with open findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Template/badge-only bodies

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:460` — Template/badge-only bodies — 2,957-line commit without any PR
- [RECOMMENDATION] `SOURCE_011:460` — Open a draft PR with a body
- [REPORT_OBSERVATION] `SOURCE_011:460` — previous evidence: 09-05, 09-08

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Template/badge-only bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Gate-by-gate fixes discovered by running charts

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:484` — Gate-by-gate fixes discovered by running charts
- [RECOMMENDATION] `SOURCE_011:484` — Automate with Devin — golden chart fixtures per gate

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Gate-by-gate fixes discovered by running charts -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:487` — Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation).

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Fixture generation for the principal-drop regression.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:488` — Fixture generation for the principal-drop regression.

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Fixture generation for the principal-drop regression. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` Long-running branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:506` — Long-running branch without PR — +3,500 lines today, still no PR
- [RECOMMENDATION] `SOURCE_011:506` — Draft PR today
- [REPORT_OBSERVATION] `SOURCE_011:506` — previous evidence: 09-05, 09-08

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- Long-running branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Large schema/field moves across 65 files by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:529` — Large schema/field moves across 65 files by hand
- [RECOMMENDATION] `SOURCE_011:529` — Automate with Devin — mechanical field migrations

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Large schema/field moves across 65 files by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Contract tests for `asserted_at` / `author_role` stamping.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:532` — Contract tests for `asserted_at` / `author_role` stamping.

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Contract tests for `asserted_at` / `author_role` stamping. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Work on shared branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:550` — Work on shared branch without PR — 65-file commit, no PR
- [RECOMMENDATION] `SOURCE_011:550` — Same draft PR as afifa
- [REPORT_OBSERVATION] `SOURCE_011:550` — previous evidence: 09-08 (`#430` findings unanswered)

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Work on shared branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Finishing other people's large PRs to get them merged

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:577` — Finishing other people's large PRs to get them merged
- [RECOMMENDATION] `SOURCE_011:577` — Improve documentation/process — PR size ceiling enforced (800 lines per `git_workflow.mdc §5.2` is already written)

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Finishing other people's large PRs to get them merged -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Green-gate matrix documented by hand in `docs/review`

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:578` — Green-gate matrix documented by hand in `docs/review`
- [RECOMMENDATION] `SOURCE_011:578` — Automate through scripts/tooling — CI emits the matrix

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Green-gate matrix documented by hand in `docs/review` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:581` — Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`).

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:582` — Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs.

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` Large PR finished and merged by the reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:600` — Large PR finished and merged by the reviewer — `#1284` 183 files: approved 07:42, reviewed 08:22, merged 08:26 by the same person
- [RECOMMENDATION] `SOURCE_011:600` — Second approver on >800-line PRs; merge after the QA gate, not before
- [REPORT_OBSERVATION] `SOURCE_011:600` — previous evidence: 09-07 (`#1314`), 09-08

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- Large PR finished and merged by the reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Hand-written `docs(review-logs)` and atlas regeneration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:626` — Hand-written `docs(review-logs)` and atlas regeneration
- [RECOMMENDATION] `SOURCE_011:626` — Automate through scripts/tooling — atlas regen in CI; review log from PR events

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Hand-written `docs(review-logs)` and atlas regeneration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` 40-commit single-day PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:627` — 40-commit single-day PRs
- [RECOMMENDATION] `SOURCE_011:627` — Improve documentation/process — split by layer (db / api / web)

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- 40-commit single-day PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Disposition the 5 `#1336` findings via Devin with reasons before requesting review.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:630` — Disposition the 5 `#1336` findings via Devin with reasons before requesting review.

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Disposition the 5 `#1336` findings via Devin with reasons before requesting review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Split `#1336` with Devin's help into db-migration / api / web PRs.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:631` — Split `#1336` with Devin's help into db-migration / api / web PRs.

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Split `#1336` with Devin's help into db-migration / api / web PRs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Very large PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:649` — Very large PRs — `#1336` 88 files
- [RECOMMENDATION] `SOURCE_011:649` — Split; enforce the 800-line ceiling
- [REPORT_OBSERVATION] `SOURCE_011:649` — previous evidence: 08-2x → 09-05 (`#1305` 109 files)

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Very large PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` `/check` audit logs written by hand into `docs/review`

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:674` — `/check` audit logs written by hand into `docs/review`
- [RECOMMENDATION] `SOURCE_011:674` — Automate through scripts/tooling

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- `/check` audit logs written by hand into `docs/review` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction")

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:675` — Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction")
- [RECOMMENDATION] `SOURCE_011:675` — Improve documentation/process — one PR per finding class

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:678` — Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value.

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` One regression test per QA finding in `#1334` (2 findings → verify 2 tests).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:679` — One regression test per QA finding in `#1334` (2 findings → verify 2 tests).

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- One regression test per QA finding in `#1334` (2 findings → verify 2 tests). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` >50-file PRs open concurrently

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:697` — >50-file PRs open concurrently — `#1316` 97, `#1295` 56, `#1334` 43
- [RECOMMENDATION] `SOURCE_011:697` — Finish `#1316` before opening more
- [REPORT_OBSERVATION] `SOURCE_011:697` — previous evidence: 09-04 → 09-08 (`#1284`, `#1295`, `#1316`)

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- >50-file PRs open concurrently -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Devin findings unanswered

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:698` — Devin findings unanswered — 21 across 3 PRs
- [RECOMMENDATION] `SOURCE_011:698` — Disposition via Devin this week
- [REPORT_OBSERVATION] `SOURCE_011:698` — previous evidence: 09-08 (`#1316` 6)

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Devin findings unanswered -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Large UI feature commits (60–99 files) on a personal branch without PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:722` — Large UI feature commits (60–99 files) on a personal branch without PR
- [RECOMMENDATION] `SOURCE_011:722` — Improve documentation/process — open the PR (3rd recommendation)

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Large UI feature commits (60–99 files) on a personal branch without PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:725` — Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines.

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:726` — Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature.

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` Work without PR (`feat/mobbin-trails`)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:744` — Work without PR (`feat/mobbin-trails`) — 5 commits, +6,700 lines today
- [RECOMMENDATION] `SOURCE_011:744` — Open the PR
- [REPORT_OBSERVATION] `SOURCE_011:744` — previous evidence: 09-05, 09-08

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- Work without PR (`feat/mobbin-trails`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` Ownership-guard exemptions added case by case

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:770` — Ownership-guard exemptions added case by case
- [RECOMMENDATION] `SOURCE_011:770` — Automate with Devin — table-driven guard tests

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- Ownership-guard exemptions added case by case -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000352` Regression tests for the ownership guard (guidance-only vs rule writes).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:773` — Regression tests for the ownership guard (guidance-only vs rule writes).

### DECISION: ISSUE_000352_ATTEMPT_01
<!-- Regression tests for the ownership guard (guidance-only vs rule writes). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000353` Draft PR for the branch.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:774` — Draft PR for the branch.

### DECISION: ISSUE_000353_ATTEMPT_01
<!-- Draft PR for the branch. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000354` — (branch without PR is new for her)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:792` — — (branch without PR is new for her) — 8 commits, no PR
- [RECOMMENDATION] `SOURCE_011:792` — Open a draft PR
- [REPORT_OBSERVATION] `SOURCE_011:792` — previous evidence: —

### DECISION: ISSUE_000354_ATTEMPT_01
<!-- — (branch without PR is new for her) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000355` Re-syncing long-lived feature branch with `dev`

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:815` — Re-syncing long-lived feature branch with `dev`
- [RECOMMENDATION] `SOURCE_011:815` — Improve documentation/process — merge smaller, sooner

### DECISION: ISSUE_000355_ATTEMPT_01
<!-- Re-syncing long-lived feature branch with `dev` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000356` Regression test for the remediation-card case (from 09-08).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:818` — Regression test for the remediation-card case (from 09-08).

### DECISION: ISSUE_000356_ATTEMPT_01
<!-- Regression test for the remediation-card case (from 09-08). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000357` —

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:836` — — — —
- [RECOMMENDATION] `SOURCE_011:836` — —
- [REPORT_OBSERVATION] `SOURCE_011:836` — previous evidence: —

### DECISION: ISSUE_000357_ATTEMPT_01
<!-- — -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

