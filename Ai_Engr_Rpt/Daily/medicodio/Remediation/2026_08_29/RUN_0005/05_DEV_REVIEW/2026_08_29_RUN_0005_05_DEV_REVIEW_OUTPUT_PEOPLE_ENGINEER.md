# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-08-29 · **Stage:** `05_DEV_REVIEW` · **Status:** PARTIAL_SOURCE_DATA

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_MISMATCH: filename date and stated review date disagree; artifact excluded from automatic processing
- PARTIAL: missing DAILY_ENGINEERING_DETAIL; run continues in analysis-only mode with reduced confidence

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000002` Low automation-adoption signal for akanksh-rv

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:36` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000002_ATTEMPT_01
<!-- Low automation-adoption signal for akanksh-rv -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000049` Low automation-adoption signal for Pj-Vineeth-Kumar

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:39` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000049_ATTEMPT_01
<!-- Low automation-adoption signal for Pj-Vineeth-Kumar -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000003` Low automation-adoption signal for Amrutha-Beedikar

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:43` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000003_ATTEMPT_01
<!-- Low automation-adoption signal for Amrutha-Beedikar -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000282` Hand-written `docs(review-logs)` evidence commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:84` — Hand-written `docs(review-logs)` evidence commits
- [RECOMMENDATION] `SOURCE_011:84` — Automate through scripts/tooling — emit the review log from the gate runner (his own 08-28 recommended improvement, still open)

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Hand-written `docs(review-logs)` evidence commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` pnpm-lock repair commits after dependency bumps

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:85` — pnpm-lock repair commits after dependency bumps
- [RECOMMENDATION] `SOURCE_011:85` — Automate through scripts/tooling — a lockfile-refresh job like the one `paperclip-ai` already runs

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- pnpm-lock repair commits after dependency bumps -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Manual `dev`-into-branch merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:86` — Manual `dev`-into-branch merges
- [RECOMMENDATION] `SOURCE_011:86` — Continue manually — but shorten by landing #1244 in slices

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Manual `dev`-into-branch merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` Have Devin build the content-sync preflight matrix as tests (three environments × transportable/untransportable × ambiguous natural key) so the pass he ran by h

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:89` — Have Devin build the content-sync preflight matrix as tests (three environments × transportable/untransportable × ambiguous natural key) so the pass he ran by hand becomes a gate on #1244.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- Have Devin build the content-sync preflight matrix as tests (three environments × transportable/untransportable × ambiguous natural key) so the pass he ran by h -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Delegate the bundle-integrity regression suite covering the signature-check-fails-open class he fixed on 08-27 and the audit-stamp gap he fixed today.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:90` — Delegate the bundle-integrity regression suite covering the signature-check-fails-open class he fixed on 08-27 and the audit-stamp gap he fixed today.

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Delegate the bundle-integrity regression suite covering the signature-check-fails-open class he fixed on 08-27 and the audit-stamp gap he fixed today. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Delegate the lockfile/dependency-bump chore lane entirely.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:91` — Delegate the lockfile/dependency-bump chore lane entirely.

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Delegate the lockfile/dependency-bump chore lane entirely. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` Substance recorded in commits, approval left empty

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:110` — Substance recorded in commits, approval left empty — Empty-body approval on #1254 (320 files, prod-bound)
- [RECOMMENDATION] `SOURCE_011:110` — Paste the three-line verdict (scope / findings status / rollback) into the GitHub approval; it is the only artefact the merge records
- [REPORT_OBSERVATION] `SOURCE_011:110` — previous evidence: 08-28: empty GitHub approval on #1251 while the audit lived in `docs(review-logs)`

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- Substance recorded in commits, approval left empty -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` A long-lived branch grows instead of landing

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:111` — A long-lived branch grows instead of landing — Still open, 108 commits
- [RECOMMENDATION] `SOURCE_011:111` — Land the sync engine and the operator surface as separate PRs this window
- [REPORT_OBSERVATION] `SOURCE_011:111` — previous evidence: 08-26 → 08-28: #1244 open three windows, 118 files

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- A long-lived branch grows instead of landing -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Repairing specs the branch's own contract changes falsified

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:145` — Repairing specs the branch's own contract changes falsified
- [RECOMMENDATION] `SOURCE_011:145` — Automate with Devin — delegate the contract-test realignment once the contract is settled

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Repairing specs the branch's own contract changes falsified -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Doc/PRD re-sync after each design correction

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:146` — Doc/PRD re-sync after each design correction
- [RECOMMENDATION] `SOURCE_011:146` — Improve documentation/process — one PRD update at the end of the pass, or generate the endpoint map from the route table

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Doc/PRD re-sync after each design correction -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Hand-written review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:147` — Hand-written review-log commits
- [RECOMMENDATION] `SOURCE_011:147` — Automate through scripts/tooling — same gate-runner output anirudh needs

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Hand-written review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by noth

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: AUTHORIZATION
- Priority: 8 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:150` — Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by nothing.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by noth -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` Delegate the endpoint-map and Atlas generation so docs stop needing five catch-up commits.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:151` — Delegate the endpoint-map and Atlas generation so docs stop needing five catch-up commits.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- Delegate the endpoint-map and Atlas generation so docs stop needing five catch-up commits. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Delegate the decomposition itself: have Devin carve #1260 into contract, API, and web PRs against the current diff.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:152` — Delegate the decomposition itself: have Devin carve #1260 into contract, API, and web PRs against the current diff.

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Delegate the decomposition itself: have Devin carve #1260 into contract, API, and web PRs against the current diff. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` Very large single PR (team-level pattern, flagged 08-27 and 08-28 for #1239)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:172` — Very large single PR (team-level pattern, flagged 08-27 and 08-28 for #1239) — #1260 at 152 files / 65 commits, opened 21:13 with 2 findings outstanding
- [RECOMMENDATION] `SOURCE_011:172` — Split before requesting review; a 152-file PR will be approved on trust, not on reading
- [REPORT_OBSERVATION] `SOURCE_011:172` — previous evidence: Team-level: #1239 at 169 files has had no reviewer for four windows

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- Very large single PR (team-level pattern, flagged 08-27 and 08-28 for #1239) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Hand-written review-log commits (`/check`, `/fix`, `/architect-review`, gate results)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:207` — Hand-written review-log commits (`/check`, `/fix`, `/architect-review`, gate results)
- [RECOMMENDATION] `SOURCE_011:207` — Automate through scripts/tooling — the gate runner should emit these

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Hand-written review-log commits (`/check`, `/fix`, `/architect-review`, gate results) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` Being the only substantive reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:208` — Being the only substantive reviewer
- [RECOMMENDATION] `SOURCE_011:208` — Improve documentation/process — publish her review template as the repo's approval standard for PRs over a size threshold (her own 08-28 improvement, still open)

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- Being the only substantive reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` Fixing the same defect on both API and web layers

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:209` — Fixing the same defect on both API and web layers
- [RECOMMENDATION] `SOURCE_011:209` — Automate with Devin — a shared-contract test would catch the divergence once

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- Fixing the same defect on both API and web layers -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Delegate a contract test for checklist grouping/ordering (platform vs firm-owned, `sort_order`, always-null fields) so the semantics she verified by reading are

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:212` — Delegate a contract test for checklist grouping/ordering (platform vs firm-owned, `sort_order`, always-null fields) so the semantics she verified by reading are pinned by data.

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Delegate a contract test for checklist grouping/ordering (platform vs firm-owned, `sort_order`, always-null fields) so the semantics she verified by reading are -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Delegate the conversion of her review template into a repo checklist plus a PR-size-triggered required-reviewer rule.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:213` — Delegate the conversion of her review template into a repo checklist plus a PR-size-triggered required-reviewer rule.

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Delegate the conversion of her review template into a repo checklist plus a PR-size-triggered required-reviewer rule. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` Delegate the mock/repository-layer realignment across the remaining API modules that still bypass the repository layer.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:214` — Delegate the mock/repository-layer realignment across the remaining API modules that still bypass the repository layer.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- Delegate the mock/repository-layer realignment across the remaining API modules that still bypass the repository layer. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Review quality depends on one person's availability

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:233` — Review quality depends on one person's availability — 1 of 15 human review events had content — hers
- [RECOMMENDATION] `SOURCE_011:233` — Publish the template and make a non-empty approval body a merge requirement on `dev`
- [REPORT_OBSERVATION] `SOURCE_011:233` — previous evidence: 08-27 and 08-28: sole substantive reviewer

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Review quality depends on one person's availability -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000304` Applying a cross-cutting rule surface-by-surface (URL state 08-28, read-only gates today)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:264` — Applying a cross-cutting rule surface-by-surface (URL state 08-28, read-only gates today)
- [RECOMMENDATION] `SOURCE_011:264` — Automate with Devin — he built the central policy today; delegate the per-service adoption and its tests

### DECISION: ISSUE_000304_ATTEMPT_01
<!-- Applying a cross-cutting rule surface-by-surface (URL state 08-28, read-only gates today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000305` Findings on his PRs closed by the reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:265` — Findings on his PRs closed by the reviewer
- [RECOMMENDATION] `SOURCE_011:265` — Improve documentation/process — answer findings before requesting review

### DECISION: ISSUE_000305_ATTEMPT_01
<!-- Findings on his PRs closed by the reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000306` Hand-written review-log commits

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:266` — Hand-written review-log commits
- [RECOMMENDATION] `SOURCE_011:266` — Automate through scripts/tooling

### DECISION: ISSUE_000306_ATTEMPT_01
<!-- Hand-written review-log commits -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000307` Delegate the read-only enforcement matrix tests — every mutating case/document endpoint × closed/archived/active — the only way a central policy stays central.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:269` — Delegate the read-only enforcement matrix tests — every mutating case/document endpoint × closed/archived/active — the only way a central policy stays central.

### DECISION: ISSUE_000307_ATTEMPT_01
<!-- Delegate the read-only enforcement matrix tests — every mutating case/document endpoint × closed/archived/active — the only way a central policy stays central. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000308` Delegate answering the three #1258 findings with commits before review.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:270` — Delegate answering the three #1258 findings with commits before review.

### DECISION: ISSUE_000308_ATTEMPT_01
<!-- Delegate answering the three #1258 findings with commits before review. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000309` Delegate the URL-state utility extraction still outstanding from 08-28.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:271` — Delegate the URL-state utility extraction still outstanding from 08-28.

### DECISION: ISSUE_000309_ATTEMPT_01
<!-- Delegate the URL-state utility extraction still outstanding from 08-28. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000310` Devin Review findings on his PRs left for the reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:290` — Devin Review findings on his PRs left for the reviewer — 3 findings on #1258 unanswered at window close; #1256's closed by her again
- [RECOMMENDATION] `SOURCE_011:290` — Treat the findings report as a pre-review checklist owned by the author
- [REPORT_OBSERVATION] `SOURCE_011:290` — previous evidence: 08-28: both findings on #1252 closed by SaijyotiMeti

### DECISION: ISSUE_000310_ATTEMPT_01
<!-- Devin Review findings on his PRs left for the reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000311` Cross-cutting behaviour changed surface-by-surface

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:291` — Cross-cutting behaviour changed surface-by-surface — Read-only gating added per service alongside the new central policy
- [RECOMMENDATION] `SOURCE_011:291` — Land the policy, then migrate surfaces onto it with a test per surface
- [REPORT_OBSERVATION] `SOURCE_011:291` — previous evidence: 08-28: URL-state races fixed in four separate places

### DECISION: ISSUE_000311_ATTEMPT_01
<!-- Cross-cutting behaviour changed surface-by-surface -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000312` Manual `qa update` cycles on the file-number / govt-notice surfaces

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:322` — Manual `qa update` cycles on the file-number / govt-notice surfaces
- [RECOMMENDATION] `SOURCE_011:322` — Automate with Devin — exactly what #1253 enables; now make it a gate

### DECISION: ISSUE_000312_ATTEMPT_01
<!-- Manual `qa update` cycles on the file-number / govt-notice surfaces -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000313` RCA written into `docs/audits` by hand

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:323` — RCA written into `docs/audits` by hand
- [RECOMMENDATION] `SOURCE_011:323` — Continue manually — RCAs are judgement work and the write-up is the value

### DECISION: ISSUE_000313_ATTEMPT_01
<!-- RCA written into `docs/audits` by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000314` Make the e2e matrix a required check on `dev` and delegate the first three journeys to Devin, converting his own QA cycle into a mechanism.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:326` — Make the e2e matrix a required check on `dev` and delegate the first three journeys to Devin, converting his own QA cycle into a mechanism.

### DECISION: ISSUE_000314_ATTEMPT_01
<!-- Make the e2e matrix a required check on `dev` and delegate the first three journeys to Devin, converting his own QA cycle into a mechanism. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000315` Delegate extraction allow-list fixtures (empty fields, display-only `doc.`, multi-questionnaire paths) — the regression class ADR-0028 describes.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:327` — Delegate extraction allow-list fixtures (empty fields, display-only `doc.`, multi-questionnaire paths) — the regression class ADR-0028 describes.

### DECISION: ISSUE_000315_ATTEMPT_01
<!-- Delegate extraction allow-list fixtures (empty fields, display-only `doc.`, multi-questionnaire paths) — the regression class ADR-0028 describes. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000316` Delegate closing out #1250, open since 08-27 with a finding history.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:328` — Delegate closing out #1250, open since 08-27 with a finding history.

### DECISION: ISSUE_000316_ATTEMPT_01
<!-- Delegate closing out #1250, open since 08-27 with a finding history. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000317` Devin-authored PR merged without independent human approval

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:347` — Devin-authored PR merged without independent human approval — #1253 merged with no human approval recorded
- [RECOMMENDATION] `SOURCE_011:347` — Require one non-author approval on any Devin-authored PR, including QA tooling
- [REPORT_OBSERVATION] `SOURCE_011:347` — previous evidence: 08-28: 17 Devin PRs merged on empty or absent approvals (team-level)

### DECISION: ISSUE_000317_ATTEMPT_01
<!-- Devin-authored PR merged without independent human approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000318` A branch left open across windows with an unanswered finding

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:348` — A branch left open across windows with an unanswered finding — #1250 still open at window close
- [RECOMMENDATION] `SOURCE_011:348` — Land or close #1250 this window
- [REPORT_OBSERVATION] `SOURCE_011:348` — previous evidence: 08-27/08-28: #1250

### DECISION: ISSUE_000318_ATTEMPT_01
<!-- A branch left open across windows with an unanswered finding -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000319` File Number behaviour changed per surface (generation 08-27, search + labels today)

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:378` — File Number behaviour changed per surface (generation 08-27, search + labels today)
- [RECOMMENDATION] `SOURCE_011:378` — Automate with Devin — one File Number module with tests covering generation, display and lookup

### DECISION: ISSUE_000319_ATTEMPT_01
<!-- File Number behaviour changed per surface (generation 08-27, search + labels today) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000320` Terminology/copy corrections after the feature ships

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:379` — Terminology/copy corrections after the feature ships
- [RECOMMENDATION] `SOURCE_011:379` — Improve documentation/process — a terminology glossary checked in review

### DECISION: ISSUE_000320_ATTEMPT_01
<!-- Terminology/copy corrections after the feature ships -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000321` #1239 kept alive by merges instead of landing

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:380` — #1239 kept alive by merges instead of landing
- [RECOMMENDATION] `SOURCE_011:380` — Continue manually — but as three PRs, not one

### DECISION: ISSUE_000321_ATTEMPT_01
<!-- #1239 kept alive by merges instead of landing -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000322` Delegate the File Number test suite — generation format, uniqueness/collision (the P2002 path), organisation vs individual lookup — before the third surface is 

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:383` — Delegate the File Number test suite — generation format, uniqueness/collision (the P2002 path), organisation vs individual lookup — before the third surface is added.

### DECISION: ISSUE_000322_ATTEMPT_01
<!-- Delegate the File Number test suite — generation format, uniqueness/collision (the P2002 path), organisation vs individual lookup — before the third surface is  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000323` Delegate the decomposition of #1239 into the reports-hub skeleton plus per-report PRs, and land the skeleton.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:384` — Delegate the decomposition of #1239 into the reports-hub skeleton plus per-report PRs, and land the skeleton.

### DECISION: ISSUE_000323_ATTEMPT_01
<!-- Delegate the decomposition of #1239 into the reports-hub skeleton plus per-report PRs, and land the skeleton. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000324` Delegate answering #1257's finding.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:385` — Delegate answering #1257's finding.

### DECISION: ISSUE_000324_ATTEMPT_01
<!-- Delegate answering #1257's finding. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000325` #1239 not decomposed

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:404` — #1239 not decomposed — No update since 08-27 21:14, 169 files, no reviewer
- [RECOMMENDATION] `SOURCE_011:404` — Split it this window and land the skeleton, or close it and re-open in slices
- [REPORT_OBSERVATION] `SOURCE_011:404` — previous evidence: 08-27 and 08-28 reports both recommended splitting it; open since 08-25

### DECISION: ISSUE_000325_ATTEMPT_01
<!-- #1239 not decomposed -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000326` Devin Review findings unanswered on his open PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:405` — Devin Review findings unanswered on his open PR — 1 finding on #1257, no commit after
- [RECOMMENDATION] `SOURCE_011:405` — Answer or explicitly dismiss before review
- [REPORT_OBSERVATION] `SOURCE_011:405` — previous evidence: 08-27: findings outstanding on #1239

### DECISION: ISSUE_000326_ATTEMPT_01
<!-- Devin Review findings unanswered on his open PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000327` `dev`→`uat`→`main` promotion PRs with template bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:435` — `dev`→`uat`→`main` promotion PRs with template bodies
- [RECOMMENDATION] `SOURCE_011:435` — Automate through scripts/tooling — generate the body from the commit range (PRs included, findings status, rollback point)

### DECISION: ISSUE_000327_ATTEMPT_01
<!-- `dev`→`uat`→`main` promotion PRs with template bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000328` Approving a promotion with "approved"

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:436` — Approving a promotion with "approved"
- [RECOMMENDATION] `SOURCE_011:436` — Improve documentation/process — a three-line release verdict template

### DECISION: ISSUE_000328_ATTEMPT_01
<!-- Approving a promotion with "approved" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000329` Closing and re-opening a promotion PR (#1255 → #1262)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:437` — Closing and re-opening a promotion PR (#1255 → #1262)
- [RECOMMENDATION] `SOURCE_011:437` — Improve documentation/process — record why a release PR was abandoned

### DECISION: ISSUE_000329_ATTEMPT_01
<!-- Closing and re-opening a promotion PR (#1255 → #1262) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000330` Delegate a release-note generator that renders the promotion PR body from the `uat..main` range, including unanswered Devin Review findings in the range — this 

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:440` — Delegate a release-note generator that renders the promotion PR body from the `uat..main` range, including unanswered Devin Review findings in the range — this turns the empty approval into a real gate.

### DECISION: ISSUE_000330_ATTEMPT_01
<!-- Delegate a release-note generator that renders the promotion PR body from the `uat..main` range, including unanswered Devin Review findings in the range — this  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000331` Delegate a post-deploy smoke suite against the five deployed services.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:441` — Delegate a post-deploy smoke suite against the five deployed services.

### DECISION: ISSUE_000331_ATTEMPT_01
<!-- Delegate a post-deploy smoke suite against the five deployed services. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000332` Delegate the rollback-point documentation for each prod train.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:442` — Delegate the rollback-point documentation for each prod train.

### DECISION: ISSUE_000332_ATTEMPT_01
<!-- Delegate the rollback-point documentation for each prod train. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000333` Promotion approved with a content-free body (team-level, flagged 08-20 onward)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:460` — Promotion approved with a content-free body (team-level, flagged 08-20 onward) — 8-character approval on #1262, 331 files, prod-bound
- [RECOMMENDATION] `SOURCE_011:460` — Adopt the three-line release verdict; block merge on an empty body
- [REPORT_OBSERVATION] `SOURCE_011:460` — previous evidence: 08-28: 42 of 43 human review events empty or one word

### DECISION: ISSUE_000333_ATTEMPT_01
<!-- Promotion approved with a content-free body (team-level, flagged 08-20 onward) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000334` Per-client column/header mapping fixes

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:493` — Per-client column/header mapping fixes
- [RECOMMENDATION] `SOURCE_011:493` — Automate with Devin — he built the table today; delegate one fixture per source format so the next client is data, not code

### DECISION: ISSUE_000334_ATTEMPT_01
<!-- Per-client column/header mapping fixes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000335` `Dev_1.0`→`Uat_1.0`→prod promotion PRs on a 448-character template

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:494` — `Dev_1.0`→`Uat_1.0`→prod promotion PRs on a 448-character template
- [RECOMMENDATION] `SOURCE_011:494` — Automate through scripts/tooling — generate the body from the commit range

### DECISION: ISSUE_000335_ATTEMPT_01
<!-- `Dev_1.0`→`Uat_1.0`→prod promotion PRs on a 448-character template -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000336` Self-merging his own fix PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:495` — Self-merging his own fix PRs
- [RECOMMENDATION] `SOURCE_011:495` — Improve documentation/process — a non-author approver on `Dev_1.0`

### DECISION: ISSUE_000336_ATTEMPT_01
<!-- Self-merging his own fix PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000337` Delegate the registration header-mapping fixture suite — one case per source format, asserting the zero-import guard he hit today — the single highest-value del

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:498` — Delegate the registration header-mapping fixture suite — one case per source format, asserting the zero-import guard he hit today — the single highest-value delegable suite in the Medicodio repos.

### DECISION: ISSUE_000337_ATTEMPT_01
<!-- Delegate the registration header-mapping fixture suite — one case per source format, asserting the zero-import guard he hit today — the single highest-value del -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000338` Delegate the payer-fallthrough regression cases (blank carrier, orphaned payer, HST claim parsing) he has now fixed by hand three windows running.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:499` — Delegate the payer-fallthrough regression cases (blank carrier, orphaned payer, HST claim parsing) he has now fixed by hand three windows running.

### DECISION: ISSUE_000338_ATTEMPT_01
<!-- Delegate the payer-fallthrough regression cases (blank carrier, orphaned payer, HST claim parsing) he has now fixed by hand three windows running. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000339` Delegate promotion-body generation so the 448-character template disappears.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:500` — Delegate promotion-body generation so the 448-character template disappears.

### DECISION: ISSUE_000339_ATTEMPT_01
<!-- Delegate promotion-body generation so the 448-character template disappears. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000340` Production behaviour changed with zero tests

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:520` — Production behaviour changed with zero tests — A registration-header refactor touching three normalisers plus Elaris, no tests; he introduced and fixed a silent zero-import inside the same window
- [RECOMMENDATION] `SOURCE_011:520` — Require a fixture for each source format; delegate the suite
- [REPORT_OBSERVATION] `SOURCE_011:520` — previous evidence: 08-27 and 08-28: four production batch-semantics changes, no tests

### DECISION: ISSUE_000340_ATTEMPT_01
<!-- Production behaviour changed with zero tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000341` Self-merge without an independent approver

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:521` — Self-merge without an independent approver — 5 PRs merged today with `human_approvals=[]`
- [RECOMMENDATION] `SOURCE_011:521` — Non-author approval required on `Dev_1.0`
- [REPORT_OBSERVATION] `SOURCE_011:521` — previous evidence: 08-28: #254 self-merged 7 minutes after opening

### DECISION: ISSUE_000341_ATTEMPT_01
<!-- Self-merge without an independent approver -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000342` Template-only promotion bodies

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:522` — Template-only promotion bodies — 6 promotion PRs at 448 characters
- [RECOMMENDATION] `SOURCE_011:522` — Generate the body from the range
- [REPORT_OBSERVATION] `SOURCE_011:522` — previous evidence: Flagged every day since 08-20

### DECISION: ISSUE_000342_ATTEMPT_01
<!-- Template-only promotion bodies -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000343` Per-facility QA re-baseline after each merge or model change

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 6 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:554` — Per-facility QA re-baseline after each merge or model change
- [RECOMMENDATION] `SOURCE_011:554` — Automate with Devin — a harness that runs the facility set and diffs against the recorded baseline

### DECISION: ISSUE_000343_ATTEMPT_01
<!-- Per-facility QA re-baseline after each merge or model change -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000344` Closing review findings by hand, one commit per batch

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:555` — Closing review findings by hand, one commit per batch
- [RECOMMENDATION] `SOURCE_011:555` — Automate with Devin — delegate the mechanical findings, keep the judgement ones

### DECISION: ISSUE_000344_ATTEMPT_01
<!-- Closing review findings by hand, one commit per batch -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000345` Empty-body approvals on other people's PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:556` — Empty-body approvals on other people's PRs
- [RECOMMENDATION] `SOURCE_011:556` — Improve documentation/process — three-line verdict template

### DECISION: ISSUE_000345_ATTEMPT_01
<!-- Empty-body approvals on other people's PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000346` Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:559` — Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one of these is a defect he fixed by hand today.

### DECISION: ISSUE_000346_ATTEMPT_01
<!-- Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000347` Delegate the QA re-baseline harness so a model bump costs one run, not a day.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:560` — Delegate the QA re-baseline harness so a model bump costs one run, not a day.

### DECISION: ISSUE_000347_ATTEMPT_01
<!-- Delegate the QA re-baseline harness so a model bump costs one run, not a day. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000348` Delegate the remaining mechanical findings on #249 so he can land it.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:561` — Delegate the remaining mechanical findings on #249 so he can land it.

### DECISION: ISSUE_000348_ATTEMPT_01
<!-- Delegate the remaining mechanical findings on #249 so he can land it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000349` Approvals with no content

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:580` — Approvals with no content — 3 approvals, all empty, including #591 which carried a 4-finding report
- [RECOMMENDATION] `SOURCE_011:580` — Paste a three-line verdict; do not approve over an open findings report
- [REPORT_OBSERVATION] `SOURCE_011:580` — previous evidence: 08-28: 20 approvals, every one empty

### DECISION: ISSUE_000349_ATTEMPT_01
<!-- Approvals with no content -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000350` A large feature branch that does not land

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:581` — A large feature branch that does not land — Third window open, 31 commits
- [RECOMMENDATION] `SOURCE_011:581` — Split the registry (schema+seed / renderer / facility scoping) and land the schema
- [REPORT_OBSERVATION] `SOURCE_011:581` — previous evidence: #249 open since 08-27, 55 files

### DECISION: ISSUE_000350_ATTEMPT_01
<!-- A large feature branch that does not land -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000351` Behaviour changes without automated tests

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:582` — Behaviour changes without automated tests — 15 findings closed and 4 facilities re-baselined, still no test commit
- [RECOMMENDATION] `SOURCE_011:582` — Delegate the seed/drift suite
- [REPORT_OBSERVATION] `SOURCE_011:582` — previous evidence: 08-27, 08-28

### DECISION: ISSUE_000351_ATTEMPT_01
<!-- Behaviour changes without automated tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000352` Approving and merging `Dev_1.0`→`Uat_1.0` promotions

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:612` — Approving and merging `Dev_1.0`→`Uat_1.0` promotions
- [RECOMMENDATION] `SOURCE_011:612` — Automate through scripts/tooling — auto-merge on green for pure promotions, so the human gate is reserved for prod and carries a written verdict

### DECISION: ISSUE_000352_ATTEMPT_01
<!-- Approving and merging `Dev_1.0`→`Uat_1.0` promotions -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000353` Reading a large promotion diff with no summary

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:613` — Reading a large promotion diff with no summary
- [RECOMMENDATION] `SOURCE_011:613` — Automate with Devin — generate the range summary and the open-findings list into the PR body

### DECISION: ISSUE_000353_ATTEMPT_01
<!-- Reading a large promotion diff with no summary -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000354` Delegate a promotion summariser that posts "PRs in range / open Devin Review findings / migrations touched / rollback point" as a comment, so his approval can c

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:616` — Delegate a promotion summariser that posts "PRs in range / open Devin Review findings / migrations touched / rollback point" as a comment, so his approval can cite it.

### DECISION: ISSUE_000354_ATTEMPT_01
<!-- Delegate a promotion summariser that posts "PRs in range / open Devin Review findings / migrations touched / rollback point" as a comment, so his approval can c -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000355` Delegate an auto-merge-on-green rule for `Dev_1.0`→`Uat_1.0` so his attention moves to `release/prod_1.0` only.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:617` — Delegate an auto-merge-on-green rule for `Dev_1.0`→`Uat_1.0` so his attention moves to `release/prod_1.0` only.

### DECISION: ISSUE_000355_ATTEMPT_01
<!-- Delegate an auto-merge-on-green rule for `Dev_1.0`→`Uat_1.0` so his attention moves to `release/prod_1.0` only. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000356` Approval with no recorded content

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:635` — Approval with no recorded content — 5 approvals, all empty, one over an open finding on a prod-bound sync
- [RECOMMENDATION] `SOURCE_011:635` — Adopt the three-line verdict (range checked / findings status / rollback); it is a two-minute change with the largest control payoff in this repo
- [REPORT_OBSERVATION] `SOURCE_011:635` — previous evidence: 08-28: 6 approvals, all empty

### DECISION: ISSUE_000356_ATTEMPT_01
<!-- Approval with no recorded content -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000357` Environment/tagging logic corrected right after shipping it

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:664` — Environment/tagging logic corrected right after shipping it
- [RECOMMENDATION] `SOURCE_011:664` — Improve documentation/process — one config seam for environment identity, asserted by a test

### DECISION: ISSUE_000357_ATTEMPT_01
<!-- Environment/tagging logic corrected right after shipping it -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000358` The same change authored twice across nodejs and react

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:665` — The same change authored twice across nodejs and react
- [RECOMMENDATION] `SOURCE_011:665` — Automate with Devin — shared contract or generated client

### DECISION: ISSUE_000358_ATTEMPT_01
<!-- The same change authored twice across nodejs and react -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000359` Manual `Dev_1.0` sync merges

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:666` — Manual `Dev_1.0` sync merges
- [RECOMMENDATION] `SOURCE_011:666` — Continue manually

### DECISION: ISSUE_000359_ATTEMPT_01
<!-- Manual `Dev_1.0` sync merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000360` Delegate metrics tests: label cardinality, environment tag correctness per env, and the Loki flush-serialization failure path (dropped batch, backpressure) — no

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:669` — Delegate metrics tests: label cardinality, environment tag correctness per env, and the Loki flush-serialization failure path (dropped batch, backpressure) — none of which is covered today.

### DECISION: ISSUE_000360_ATTEMPT_01
<!-- Delegate metrics tests: label cardinality, environment tag correctness per env, and the Loki flush-serialization failure path (dropped batch, backpressure) — no -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000361` Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open).

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:670` — Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open).

### DECISION: ISSUE_000361_ATTEMPT_01
<!-- Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000362` Delegate answering the #591/#592 findings.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:671` — Delegate answering the #591/#592 findings.

### DECISION: ISSUE_000362_ATTEMPT_01
<!-- Delegate answering the #591/#592 findings. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000363` Merging while a Devin Review report is open

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:689` — Merging while a Devin Review report is open — #591 merged 23 min after a 4-finding report (1 commit after); #592 merged with 1 finding and no commit
- [RECOMMENDATION] `SOURCE_011:689` — Treat the findings report as a merge blocker until answered
- [REPORT_OBSERVATION] `SOURCE_011:689` — previous evidence: 08-28: #511 self-merged, findings outstanding

### DECISION: ISSUE_000363_ATTEMPT_01
<!-- Merging while a Devin Review report is open -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000364` Production-path changes with no tests

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:690` — Production-path changes with no tests — Metrics, logging transport and env tagging — all untested
- [RECOMMENDATION] `SOURCE_011:690` — Delegate the metrics/transport test suite
- [REPORT_OBSERVATION] `SOURCE_011:690` — previous evidence: 08-27, 08-28 (decrypt refactor, age-preservation fix)

### DECISION: ISSUE_000364_ATTEMPT_01
<!-- Production-path changes with no tests -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000365` "okay" approvals on engine PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:718` — "okay" approvals on engine PRs
- [RECOMMENDATION] `SOURCE_011:718` — Improve documentation/process — three-line verdict; block merge on an open findings report

### DECISION: ISSUE_000365_ATTEMPT_01
<!-- "okay" approvals on engine PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000366` Merging config changes with no fixture evidence

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:719` — Merging config changes with no fixture evidence
- [RECOMMENDATION] `SOURCE_011:719` — Automate with Devin — a config-diff fixture run posted to the PR

### DECISION: ISSUE_000366_ATTEMPT_01
<!-- Merging config changes with no fixture evidence -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000367` Delegate the `guidelines_journey` golden-file suite (recommended 08-28, not started) — it protects the logic he rewrote on three consecutive days.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:722` — Delegate the `guidelines_journey` golden-file suite (recommended 08-28, not started) — it protects the logic he rewrote on three consecutive days.

### DECISION: ISSUE_000367_ATTEMPT_01
<!-- Delegate the `guidelines_journey` golden-file suite (recommended 08-28, not started) — it protects the logic he rewrote on three consecutive days. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000368` Delegate a config-change fixture runner so an ortho/BMI config PR arrives with before/after prediction evidence and the approval has something to cite.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:723` — Delegate a config-change fixture runner so an ortho/BMI config PR arrives with before/after prediction evidence and the approval has something to cite.

### DECISION: ISSUE_000368_ATTEMPT_01
<!-- Delegate a config-change fixture runner so an ortho/BMI config PR arrives with before/after prediction evidence and the approval has something to cite. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000369` Land or close draft #405.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:724` — Land or close draft #405.

### DECISION: ISSUE_000369_ATTEMPT_01
<!-- Land or close draft #405. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000370` Merge within seconds of a findings report

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:743` — Merge within seconds of a findings report — #412 merged 96 s after a 2-finding report; #413 merged 75 s after a 2-finding report
- [RECOMMENDATION] `SOURCE_011:743` — Make an unanswered Devin Review report a merge blocker in `nextgen-codio-engine`
- [REPORT_OBSERVATION] `SOURCE_011:743` — previous evidence: 08-28: #410 merged on a 439-character template body with a finding reported

### DECISION: ISSUE_000370_ATTEMPT_01
<!-- Merge within seconds of a findings report -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000371` Approvals of ≤ 5 characters

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:744` — Approvals of ≤ 5 characters — 2 approvals, "okay"
- [RECOMMENDATION] `SOURCE_011:744` — Three-line verdict template
- [REPORT_OBSERVATION] `SOURCE_011:744` — previous evidence: 08-27, 08-28 (8 approvals, all "okay")

### DECISION: ISSUE_000371_ATTEMPT_01
<!-- Approvals of ≤ 5 characters -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000372` BMI/E66-Z68 trigger data edited without a fixture

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:773` — BMI/E66-Z68 trigger data edited without a fixture
- [RECOMMENDATION] `SOURCE_011:773` — Automate with Devin — one fixture per trigger condition, run on the config diff

### DECISION: ISSUE_000372_ATTEMPT_01
<!-- BMI/E66-Z68 trigger data edited without a fixture -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000373` Config/data PRs on a template body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:774` — Config/data PRs on a template body
- [RECOMMENDATION] `SOURCE_011:774` — Improve documentation/process — state the trigger and the client scope in the body

### DECISION: ISSUE_000373_ATTEMPT_01
<!-- Config/data PRs on a template body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000374` Delegate the E66/Z68 gate fixtures (recommended 08-28, not started) — a handful of chart fixtures pinning each trigger.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:777` — Delegate the E66/Z68 gate fixtures (recommended 08-28, not started) — a handful of chart fixtures pinning each trigger.

### DECISION: ISSUE_000374_ATTEMPT_01
<!-- Delegate the E66/Z68 gate fixtures (recommended 08-28, not started) — a handful of chart fixtures pinning each trigger. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000375` Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:778` — Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return.

### DECISION: ISSUE_000375_ATTEMPT_01
<!-- Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000376` Delegate the body/evidence generation for data-only config PRs.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:779` — Delegate the body/evidence generation for data-only config PRs.

### DECISION: ISSUE_000376_ATTEMPT_01
<!-- Delegate the body/evidence generation for data-only config PRs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000377` Merge over an unanswered findings report, on a template body

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:797` — Merge over an unanswered findings report, on a template body — #413 merged 75 s after a 2-finding report
- [RECOMMENDATION] `SOURCE_011:797` — Answer or dismiss findings in the PR before merge; the engine repo needs the blocker rule
- [REPORT_OBSERVATION] `SOURCE_011:797` — previous evidence: 08-28: #400 merged and #401 promoted 32 s later with a finding reported

### DECISION: ISSUE_000377_ATTEMPT_01
<!-- Merge over an unanswered findings report, on a template body -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000378` Model/RAG config toggles shipped without evidence of effect

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:826` — Model/RAG config toggles shipped without evidence of effect
- [RECOMMENDATION] `SOURCE_011:826` — Automate with Devin — a routing/selection fixture run that posts before/after predictions on the config diff

### DECISION: ISSUE_000378_ATTEMPT_01
<!-- Model/RAG config toggles shipped without evidence of effect -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000379` Template-only PR bodies on prediction-affecting changes

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:827` — Template-only PR bodies on prediction-affecting changes
- [RECOMMENDATION] `SOURCE_011:827` — Improve documentation/process — name the specialty, the model, and the expected behaviour change

### DECISION: ISSUE_000379_ATTEMPT_01
<!-- Template-only PR bodies on prediction-affecting changes -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000380` Delegate the routing-trigger fixture suite (recommended 08-28, not started) — the change he ships most often is the one with no test at all.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:830` — Delegate the routing-trigger fixture suite (recommended 08-28, not started) — the change he ships most often is the one with no test at all.

### DECISION: ISSUE_000380_ATTEMPT_01
<!-- Delegate the routing-trigger fixture suite (recommended 08-28, not started) — the change he ships most often is the one with no test at all. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000381` Delegate a config-diff evidence job so a model switch arrives with measured output, not an assertion.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:831` — Delegate a config-diff evidence job so a model switch arrives with measured output, not an assertion.

### DECISION: ISSUE_000381_ATTEMPT_01
<!-- Delegate a config-diff evidence job so a model switch arrives with measured output, not an assertion. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000382` Delegate the answer to #412's two findings as a follow-up PR.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:832` — Delegate the answer to #412's two findings as a follow-up PR.

### DECISION: ISSUE_000382_ATTEMPT_01
<!-- Delegate the answer to #412's two findings as a follow-up PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000383` Merging (or promoting) while a Devin Review finding is unanswered

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:850` — Merging (or promoting) while a Devin Review finding is unanswered — #412 merged 96 s after a 2-finding report
- [RECOMMENDATION] `SOURCE_011:850` — Merge blocker on open findings in the engine repo; he is the most frequent case
- [REPORT_OBSERVATION] `SOURCE_011:850` — previous evidence: 08-27 and 08-28 both recorded this for him

### DECISION: ISSUE_000383_ATTEMPT_01
<!-- Merging (or promoting) while a Devin Review finding is unanswered -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000384` Prediction-affecting config with no fixture evidence

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:851` — Prediction-affecting config with no fixture evidence — #412 (model + RAG toggle)
- [RECOMMENDATION] `SOURCE_011:851` — Delegate the fixture suite; require the run output in the body
- [REPORT_OBSERVATION] `SOURCE_011:851` — previous evidence: 08-27, 08-28

### DECISION: ISSUE_000384_ATTEMPT_01
<!-- Prediction-affecting config with no fixture evidence -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000385` Work accumulating on someone else's draft branch instead of a PR of his own

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:879` — Work accumulating on someone else's draft branch instead of a PR of his own
- [RECOMMENDATION] `SOURCE_011:879` — Improve documentation/process — open a small PR per capability (recall, parameters, dedup)

### DECISION: ISSUE_000385_ATTEMPT_01
<!-- Work accumulating on someone else's draft branch instead of a PR of his own -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000386` Terse commit subjects ("added more paramters…") on pipeline-affecting code

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:880` — Terse commit subjects ("added more paramters…") on pipeline-affecting code
- [RECOMMENDATION] `SOURCE_011:880` — Improve documentation/process — state the behaviour and its scope

### DECISION: ISSUE_000386_ATTEMPT_01
<!-- Terse commit subjects ("added more paramters…") on pipeline-affecting code -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000387` Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:883` — Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable.

### DECISION: ISSUE_000387_ATTEMPT_01
<!-- Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000388` Delegate the split of his three commits into a reviewable PR with a body describing the recall contract.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:884` — Delegate the split of his three commits into a reviewable PR with a body describing the recall contract.

### DECISION: ISSUE_000388_ATTEMPT_01
<!-- Delegate the split of his three commits into a reviewable PR with a body describing the recall contract. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000389` Delegate a fixture proving DXEX1 and DXEX2 recall behave identically for the shared parameter set.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:885` — Delegate a fixture proving DXEX1 and DXEX2 recall behave identically for the shared parameter set.

### DECISION: ISSUE_000389_ATTEMPT_01
<!-- Delegate a fixture proving DXEX1 and DXEX2 recall behave identically for the shared parameter set. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000390` No reviewable PR of his own

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:903` — No reviewable PR of his own — 3 commits pushed to a fourth-window draft owned by someone else
- [RECOMMENDATION] `SOURCE_011:903` — Open a PR for the dedup commit alone this window
- [REPORT_OBSERVATION] `SOURCE_011:903` — previous evidence: 08-27 and 08-28 reports both recommended opening one, however small

### DECISION: ISSUE_000390_ATTEMPT_01
<!-- No reviewable PR of his own -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000391` Upstream sync + lockfile refresh + release

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:931` — Upstream sync + lockfile refresh + release
- [RECOMMENDATION] `SOURCE_011:931` — Continue manually — the automation exists; only the failure triage is manual

### DECISION: ISSUE_000391_ATTEMPT_01
<!-- Upstream sync + lockfile refresh + release -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000392` Delegate triage of the Docker/Release failure class so a red sync does not need a person watching it.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:934` — Delegate triage of the Docker/Release failure class so a red sync does not need a person watching it.

### DECISION: ISSUE_000392_ATTEMPT_01
<!-- Delegate triage of the Docker/Release failure class so a red sync does not need a person watching it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

