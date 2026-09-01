# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-08-31 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Re-checking whether an open PR has picked up a human reviewer

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:86` — Re-checking whether an open PR has picked up a human reviewer
- [RECOMMENDATION] `SOURCE_011:86` — Automate through scripts/tooling — a stale-PR reminder on the CI gates he already owns

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Re-checking whether an open PR has picked up a human reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` QA-driven field-level fixes shipped as one "qa update" PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:87` — QA-driven field-level fixes shipped as one "qa update" PR
- [RECOMMENDATION] `SOURCE_011:87` — Improve documentation/process — split by concern so each part is reviewable

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- QA-driven field-level fixes shipped as one "qa update" PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Delegate a test matrix for the extraction allow-list empty-field handling in #1259 — bounded, data-driven, exactly the shape Devin lands well.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:91` — Delegate a test matrix for the extraction allow-list empty-field handling in #1259 — bounded, data-driven, exactly the shape Devin lands well.

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Delegate a test matrix for the extraction allow-list empty-field handling in #1259 — bounded, data-driven, exactly the shape Devin lands well. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Delegate a stale-PR / unreviewed-PR report as a scheduled job, extending the CI automation he already built.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:92` — Delegate a stale-PR / unreviewed-PR report as a scheduled job, extending the CI automation he already built.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Delegate a stale-PR / unreviewed-PR report as a scheduled job, extending the CI automation he already built. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Open PR with bot review only and no human reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:114` — Open PR with bot review only and no human reviewer — Still open, unattended through the review window; #1259 now in the same state
- [RECOMMENDATION] `SOURCE_011:114` — Assign a named reviewer at open time; treat "bot-reviewed only" as not-reviewed
- [REPORT_OBSERVATION] `SOURCE_011:114` — previous evidence: 08-30 report listed #1250 as open since 08-27

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Open PR with bot review only and no human reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Enforcing a state-based guard surface by surface

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:145` — Enforcing a state-based guard surface by surface
- [RECOMMENDATION] `SOURCE_011:145` — Automate with Devin — one case per (case state × mutating surface); a generated matrix suite is cheaper than manual verification

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Enforcing a state-based guard surface by surface -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Delegate the closed/archived read-only enforcement matrix covering every mutating endpoint and UI control.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:149` — Delegate the closed/archived read-only enforcement matrix covering every mutating endpoint and UI control.

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Delegate the closed/archived read-only enforcement matrix covering every mutating endpoint and UI control. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Delegate backfill tests for the guard's negative cases (open cases must remain editable) to prevent an over-broad guard.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:150` — Delegate backfill tests for the guard's negative cases (open cases must remain editable) to prevent an over-broad guard.

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Delegate backfill tests for the guard's negative cases (open cases must remain editable) to prevent an over-broad guard. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` PR opened late on Friday with bot review only

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:172` — PR opened late on Friday with bot review only — Still open and unreviewed after the review window
- [RECOMMENDATION] `SOURCE_011:172` — Request a named reviewer at open time
- [REPORT_OBSERVATION] `SOURCE_011:172` — previous evidence: 08-30 report listed #1258 among the open, unreviewed set

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- PR opened late on Friday with bot review only -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` No observable Devin leverage

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:173` — No observable Devin leverage — Unchanged
- [RECOMMENDATION] `SOURCE_011:173` — Delegate the state-guard matrix suite as a first bounded session
- [REPORT_OBSERVATION] `SOURCE_011:173` — previous evidence: 0 Devin-trailer commits across week and month

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- No observable Devin leverage -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Lookup/searchability fixes on displayed identifiers

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:204` — Lookup/searchability fixes on displayed identifiers
- [RECOMMENDATION] `SOURCE_011:204` — Automate with Devin — generate a search-parity test per displayed identifier so the next identifier does not need a new manual fix

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Lookup/searchability fixes on displayed identifiers -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Delegate search-parity regression tests: for every identifier rendered in the UI, assert it is queryable through the shared search platform.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:208` — Delegate search-parity regression tests: for every identifier rendered in the UI, assert it is queryable through the shared search platform.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Delegate search-parity regression tests: for every identifier rendered in the UI, assert it is queryable through the shared search platform. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Delegate the PR-preparation pass (description, gates, screenshots) on his large PRs, which have previously landed with thin bodies.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:209` — Delegate the PR-preparation pass (description, gates, screenshots) on his large PRs, which have previously landed with thin bodies.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Delegate the PR-preparation pass (description, gates, screenshots) on his large PRs, which have previously landed with thin bodies. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Open PR with bot review only

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:231` — Open PR with bot review only — Unattended through the review window
- [RECOMMENDATION] `SOURCE_011:231` — Named reviewer at open time
- [REPORT_OBSERVATION] `SOURCE_011:231` — previous evidence: 08-30 report listed #1257 as open since 08-27/08-28

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Open PR with bot review only -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Accumulating a multi-phase feature on one branch before opening a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:262` — Accumulating a multi-phase feature on one branch before opening a PR
- [RECOMMENDATION] `SOURCE_011:262` — Improve documentation/process — open a draft PR at phase 1 so gates and Devin Review run continuously instead of at the end

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Accumulating a multi-phase feature on one branch before opening a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Writing subscriber/notification wiring per skill by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:263` — Writing subscriber/notification wiring per skill by hand
- [RECOMMENDATION] `SOURCE_011:263` — Automate with Devin — a registry-driven contract test per subscriber

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Writing subscriber/notification wiring per skill by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Delegate the subscriber/notification test matrix for the AI Case Manager skill registry — the phases most likely to hide a wiring bug.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:267` — Delegate the subscriber/notification test matrix for the AI Case Manager skill registry — the phases most likely to hide a wiring bug.

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Delegate the subscriber/notification test matrix for the AI Case Manager skill registry — the phases most likely to hide a wiring bug. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Delegate the AI-skill registry contract tests so a new skill cannot register incorrectly.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:268` — Delegate the AI-skill registry contract tests so a new skill cannot register incorrectly.

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Delegate the AI-skill registry contract tests so a new skill cannot register incorrectly. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Open the branch as a draft PR and let Devin Review run per phase, rather than one large review at the end.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:269` — Open the branch as a draft PR and let Devin Review run per phase, rather than one large review at the end.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Open the branch as a draft PR and let Devin Review run per phase, rather than one large review at the end. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Large feature landed as a single PR instead of a reviewable series

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 3 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:291` — Large feature landed as a single PR instead of a reviewable series — `feat/ai-cm-draft-support-letter-skill` at 12 phases with no PR yet, second day
- [RECOMMENDATION] `SOURCE_011:291` — Open a draft PR now and split by phase boundary
- [REPORT_OBSERVATION] `SOURCE_011:291` — previous evidence: 08-30 report: #1260, 161 files / 80 commits

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Large feature landed as a single PR instead of a reviewable series -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Commits landing under an unlinked author identity

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHENTICATION
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:292` — Commits landing under an unlinked author identity — Branch commits attributed to `claude`, not to his GitHub login
- [RECOMMENDATION] `SOURCE_011:292` — Link the identity so review attribution is correct
- [REPORT_OBSERVATION] `SOURCE_011:292` — previous evidence: 08-21 report recorded the same class of issue for other members' emails

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Commits landing under an unlinked author identity -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Leaving a draft PR open across days with no review surface

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:323` — Leaving a draft PR open across days with no review surface
- [RECOMMENDATION] `SOURCE_011:323` — Improve documentation/process — a draft is either work-in-progress with a stated finish date or should be marked ready

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Leaving a draft PR open across days with no review surface -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` KB-table-driven rule redesigns verified by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:324` — KB-table-driven rule redesigns verified by hand
- [RECOMMENDATION] `SOURCE_011:324` — Automate with Devin — generate per-row fixtures from the KB table so each rule row has a test

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- KB-table-driven rule redesigns verified by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Delegate per-row fixtures for the I.B.9 collapse rules, generated from the KB table.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:328` — Delegate per-row fixtures for the I.B.9 collapse rules, generated from the KB table.

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Delegate per-row fixtures for the I.B.9 collapse rules, generated from the KB table. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Delegate recall-precision tests for the episodic memory feature in #393 before it is marked ready.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:329` — Delegate recall-precision tests for the episodic memory feature in #393 before it is marked ready.

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Delegate recall-precision tests for the episodic memory feature in #393 before it is marked ready. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Devin/engine draft PRs left open for days

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:351` — Devin/engine draft PRs left open for days — #393 draft for 6 days, #405 (Devin-authored) draft since 08-27
- [RECOMMENDATION] `SOURCE_011:351` — Close, land, or state a finish date for each draft older than 48 hours
- [REPORT_OBSERVATION] `SOURCE_011:351` — previous evidence: 08-22/08-23 reports: engine #373 draft for 4 consecutive days

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Devin/engine draft PRs left open for days -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Re-running the same Devin Review cycle on one PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:382` — Re-running the same Devin Review cycle on one PR
- [RECOMMENDATION] `SOURCE_011:382` — Improve documentation/process — a bot pass is a gate, not a reviewer; require one human verdict before the third bot pass

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Re-running the same Devin Review cycle on one PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Prompt/flag registry plumbing per integration

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:383` — Prompt/flag registry plumbing per integration
- [RECOMMENDATION] `SOURCE_011:383` — Automate with Devin — registry contract tests so each new prompt or flag is validated by construction

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Prompt/flag registry plumbing per integration -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Delegate prompt-registry contract tests (every registered prompt resolves, has required variables, and fails loudly when missing).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:387` — Delegate prompt-registry contract tests (every registered prompt resolves, has required variables, and fails loudly when missing).

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Delegate prompt-registry contract tests (every registered prompt resolves, has required variables, and fails loudly when missing). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Delegate the insurance-created-flag propagation tests across the integration boundary in #248.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:388` — Delegate the insurance-created-flag propagation tests across the integration boundary in #248.

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Delegate the insurance-created-flag propagation tests across the integration boundary in #248. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Split the two open PRs' remaining work into scoped follow-ups with acceptance criteria written from the bot findings.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:389` — Split the two open PRs' remaining work into scoped follow-ups with acceptance criteria written from the bot findings.

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Split the two open PRs' remaining work into scoped follow-ups with acceptance criteria written from the bot findings. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` Commits landing under an unlinked email

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHENTICATION
- Priority: 5 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:411` — Commits landing under an unlinked email — Unchanged; his Devin work is still invisible under his login
- [RECOMMENDATION] `SOURCE_011:411` — Link the email to the GitHub account so his Devin leverage is attributed to him
- [REPORT_OBSERVATION] `SOURCE_011:411` — previous evidence: 08-21 report identified `amit.p@medicodio.ai` as a separate API identity

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- Commits landing under an unlinked email -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Bot-review-only PRs left open for days

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:412` — Bot-review-only PRs left open for days — Both still open through the review window
- [RECOMMENDATION] `SOURCE_011:412` — One human verdict required before the third bot pass
- [REPORT_OBSERVATION] `SOURCE_011:412` — previous evidence: 08-30 report listed #248/#249 as open

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Bot-review-only PRs left open for days -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` A long-lived exploratory PR with a non-descriptive title

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:443` — A long-lived exploratory PR with a non-descriptive title
- [RECOMMENDATION] `SOURCE_011:443` — Improve documentation/process — exploratory work belongs on a branch or a draft with a stated purpose, not an open PR

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- A long-lived exploratory PR with a non-descriptive title -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` If the ortho work is still wanted, delegate it as a scoped session with written acceptance criteria; otherwise close #382.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:447` — If the ortho work is still wanted, delegate it as a scoped session with written acceptance criteria; otherwise close #382.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- If the ortho work is still wanted, delegate it as a scoped session with written acceptance criteria; otherwise close #382. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Non-descriptive engine PR titles/bodies

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:469` — Non-descriptive engine PR titles/bodies — #382 "Testing ortho", 10 days open
- [RECOMMENDATION] `SOURCE_011:469` — Close it or restate it with a purpose and acceptance criteria
- [REPORT_OBSERVATION] `SOURCE_011:469` — previous evidence: 08-21 report, pattern (5)

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Non-descriptive engine PR titles/bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

