# Dev review — decisions required

**Run:** `RUN_0003` · **Report date:** 2026-08-25 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000130` Low automation-adoption signal for svh-medicodio

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 1 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_010:31` — [rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]

### DECISION: ISSUE_000130_ATTEMPT_01
<!-- Low automation-adoption signal for svh-medicodio -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000131` Building one more report against the same catalog/controller/service/repository shape

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:56` — Building one more report against the same catalog/controller/service/repository shape
- [RECOMMENDATION] `SOURCE_011:56` — Automate with Devin — the shape is now proven; each remaining report is a bounded delegation

### DECISION: ISSUE_000131_ATTEMPT_01
<!-- Building one more report against the same catalog/controller/service/repository shape -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000132` Fixing SQL type/cast defects found only at runtime

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:57` — Fixing SQL type/cast defects found only at runtime
- [RECOMMENDATION] `SOURCE_011:57` — Automate through scripts/tooling — add a query-compilation test per report so casts fail in CI, not in UAT

### DECISION: ISSUE_000132_ATTEMPT_01
<!-- Fixing SQL type/cast defects found only at runtime -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000133` Delegate a follow-on session to write the report-query regression suite (fixed fixtures per report, asserting org scoping and the restricted-visibility predicat

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:60` — Delegate a follow-on session to write the report-query regression suite (fixed fixtures per report, asserting org scoping and the restricted-visibility predicate) — the six cast/window defects fixed today are exactly what such a suite catches.

### DECISION: ISSUE_000133_ATTEMPT_01
<!-- Delegate a follow-on session to write the report-query regression suite (fixed fixtures per report, asserting org scoping and the restricted-visibility predicat -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000134` Delegate the remaining PRD reports one session per report, referencing #1239 as the pattern.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:61` — Delegate the remaining PRD reports one session per report, referencing #1239 as the pattern.

### DECISION: ISSUE_000134_ATTEMPT_01
<!-- Delegate the remaining PRD reports one session per report, referencing #1239 as the pattern. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000135` Have a Devin session pre-answer reviewer questions on #1239 (per-report authorization proof, pagination bounds) so the human review is a verdict rather than an 

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: AUTHORIZATION
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:62` — Have a Devin session pre-answer reviewer questions on #1239 (per-report authorization proof, pagination bounds) so the human review is a verdict rather than an investigation.

### DECISION: ISSUE_000135_ATTEMPT_01
<!-- Have a Devin session pre-answer reviewer questions on #1239 (per-report authorization proof, pagination bounds) so the human review is a verdict rather than an  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000136` Very large single PR

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:81` — Very large single PR — #1239 (155 files) open
- [RECOMMENDATION] `SOURCE_011:81` — Split the report slate into per-report PRs behind the catalog flag; #1239's own catalog design already makes this cheap
- [REPORT_OBSERVATION] `SOURCE_011:81` — previous evidence: #1183 (150 files) merged 08-24

### DECISION: ISSUE_000136_ATTEMPT_01
<!-- Very large single PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000137` Running the full quality gate by hand and transcribing the result into a standards log

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:108` — Running the full quality gate by hand and transcribing the result into a standards log
- [RECOMMENDATION] `SOURCE_011:108` — Automate through scripts/tooling — the repo's CI workflow already exists but is `workflow_dispatch`-only; dispatch it per branch and link the run instead of a hand-written log

### DECISION: ISSUE_000137_ATTEMPT_01
<!-- Running the full quality gate by hand and transcribing the result into a standards log -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000138` Splitting oversized services/components after the fact

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:109` — Splitting oversized services/components after the fact
- [RECOMMENDATION] `SOURCE_011:109` — Improve documentation/process — enforce the size limit at review time on first submission

### DECISION: ISSUE_000138_ATTEMPT_01
<!-- Splitting oversized services/components after the fact -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000139` Delegate the checklist-group regression suite (group CRUD, step-link audit, deadline sweep) to Devin — the audit-trail and TOCTOU fixes today are untested behav

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: D
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:112` — Delegate the checklist-group regression suite (group CRUD, step-link audit, deadline sweep) to Devin — the audit-trail and TOCTOU fixes today are untested behaviours.

### DECISION: ISSUE_000139_ATTEMPT_01
<!-- Delegate the checklist-group regression suite (group CRUD, step-link audit, deadline sweep) to Devin — the audit-trail and TOCTOU fixes today are untested behav -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000140` Have Devin answer the open Devin Review findings on #1238 explicitly so the thread shows resolution.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:113` — Have Devin answer the open Devin Review findings on #1238 explicitly so the thread shows resolution.

### DECISION: ISSUE_000140_ATTEMPT_01
<!-- Have Devin answer the open Devin Review findings on #1238 explicitly so the thread shows resolution. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000141` Single very large PR held open for days

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:132` — Single very large PR held open for days — 171 files on day 2, still open
- [RECOMMENDATION] `SOURCE_011:132` — Land the mechanical splits (service/component decomposition) as a separate PR so the feature diff shrinks to reviewable size
- [REPORT_OBSERVATION] `SOURCE_011:132` — previous evidence: #1238 opened 08-24 at 155 files

### DECISION: ISSUE_000141_ATTEMPT_01
<!-- Single very large PR held open for days -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000142` Manually filing UI defects with screenshots and no owner

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:156` — Manually filing UI defects with screenshots and no owner
- [RECOMMENDATION] `SOURCE_011:156` — Automate with Devin — attach each issue to a Devin session at filing time so a fix PR exists before triage

### DECISION: ISSUE_000142_ATTEMPT_01
<!-- Manually filing UI defects with screenshots and no owner -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000143` Delegate #1240 (email template pre-fill / cache) to Devin — clear reproduction, likely a stale-cache or default-props defect.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:159` — Delegate #1240 (email template pre-fill / cache) to Devin — clear reproduction, likely a stale-cache or default-props defect.

### DECISION: ISSUE_000143_ATTEMPT_01
<!-- Delegate #1240 (email template pre-fill / cache) to Devin — clear reproduction, likely a stale-cache or default-props defect. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000144` Delegate #1241 (questionnaire bundle import performance) as an investigation-first session: profile, then propose.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:160` — Delegate #1241 (questionnaire bundle import performance) as an investigation-first session: profile, then propose.

### DECISION: ISSUE_000144_ATTEMPT_01
<!-- Delegate #1241 (questionnaire bundle import performance) as an investigation-first session: profile, then propose. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000145` QA findings recorded but not converted into work

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:178` — QA findings recorded but not converted into work — #1240/#1241 filed with `good first issue` label, no assignee
- [RECOMMENDATION] `SOURCE_011:178` — Attach a Devin session at filing time; the label already says the work is bounded
- [REPORT_OBSERVATION] `SOURCE_011:178` — previous evidence: 08-24: Devin Review findings accumulated on his PRs for 5 days before merge

### DECISION: ISSUE_000145_ATTEMPT_01
<!-- QA findings recorded but not converted into work -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000146` fix → prod-hotfix → uat-sync fan-out of the same diff

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:204` — fix → prod-hotfix → uat-sync fan-out of the same diff
- [RECOMMENDATION] `SOURCE_011:204` — Automate through scripts/tooling — one script (or a GitHub Action) should cut the hotfix and sync PRs from a merged fix; hand-cutting them produced duplicate #232

### DECISION: ISSUE_000146_ATTEMPT_01
<!-- fix → prod-hotfix → uat-sync fan-out of the same diff -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000147` Valley KB document corrections one field at a time

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:205` — Valley KB document corrections one field at a time
- [RECOMMENDATION] `SOURCE_011:205` — Automate with Devin — a single session against the live KB diff would batch the field mappings with a test per mapping

### DECISION: ISSUE_000147_ATTEMPT_01
<!-- Valley KB document corrections one field at a time -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000148` Delegate a "promote this fix" automation (fix → prod hotfix → uat sync) to Devin — it is deterministic, repeated daily, and today produced a duplicate PR.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:208` — Delegate a "promote this fix" automation (fix → prod hotfix → uat sync) to Devin — it is deterministic, repeated daily, and today produced a duplicate PR.

### DECISION: ISSUE_000148_ATTEMPT_01
<!-- Delegate a "promote this fix" automation (fix → prod hotfix → uat sync) to Devin — it is deterministic, repeated daily, and today produced a duplicate PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000149` Delegate tests for the migration trigger in #241 (env-source matrix, post-run ordering) before it merges — 20 files of RPA orchestration currently ship with no 

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 4 · Tier: C
- Playbook: ORG_PB_REGRESSION_TEST_GENERATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:209` — Delegate tests for the migration trigger in #241 (env-source matrix, post-run ordering) before it merges — 20 files of RPA orchestration currently ship with no visible test.

### DECISION: ISSUE_000149_ATTEMPT_01
<!-- Delegate tests for the migration trigger in #241 (env-source matrix, post-run ordering) before it merges — 20 files of RPA orchestration currently ship with no  -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000150` Have Devin sweep the 15 open Devin Review findings on his merged PRs and raise one remediation PR.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:210` — Have Devin sweep the 15 open Devin Review findings on his merged PRs and raise one remediation PR.

### DECISION: ISSUE_000150_ATTEMPT_01
<!-- Have Devin sweep the 15 open Devin Review findings on his merged PRs and raise one remediation PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000151` Self-merge seconds after opening

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 4 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:229` — Self-merge seconds after opening — #231 (8 s), #234 (8 s), #237 (17 s), #239 (8 s)
- [RECOMMENDATION] `SOURCE_011:229` — Require one non-author approval on `import_main` and `release/prod_1.0`; branch protection makes this a one-time change
- [REPORT_OBSERVATION] `SOURCE_011:229` — previous evidence: int #228 (11 min) and #229 (8 s) on 08-23; #230 (60 min) on 08-24

### DECISION: ISSUE_000151_ATTEMPT_01
<!-- Self-merge seconds after opening -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000152` Devin Review findings unaddressed on merged PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:230` — Devin Review findings unaddressed on merged PRs — 15 findings across 8 PRs today
- [RECOMMENDATION] `SOURCE_011:230` — One weekly remediation PR from the accumulated findings, delegated to Devin
- [REPORT_OBSERVATION] `SOURCE_011:230` — previous evidence: Findings on #228/#229/#230

### DECISION: ISSUE_000152_ATTEMPT_01
<!-- Devin Review findings unaddressed on merged PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000153` Hand-cut prod/uat promotion PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: C
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:231` — Hand-cut prod/uat promotion PRs — Duplicate #232 opened and closed in 12 s
- [RECOMMENDATION] `SOURCE_011:231` — Script the promotion pair
- [REPORT_OBSERVATION] `SOURCE_011:231` — previous evidence: Promotion pairs on 08-23 and 08-24

### DECISION: ISSUE_000153_ATTEMPT_01
<!-- Hand-cut prod/uat promotion PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000154` Approving another member's promotion/hotfix PRs with `lgtm`

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:257` — Approving another member's promotion/hotfix PRs with `lgtm`
- [RECOMMENDATION] `SOURCE_011:257` — Improve documentation/process — a 3-line review template (what I checked / what I did not / verdict) turns these into evidence; today's two prod approvals had no check recorded

### DECISION: ISSUE_000154_ATTEMPT_01
<!-- Approving another member's promotion/hotfix PRs with `lgtm` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000155` dev → uat sync PRs

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:258` — dev → uat sync PRs
- [RECOMMENDATION] `SOURCE_011:258` — Automate through scripts/tooling

### DECISION: ISSUE_000155_ATTEMPT_01
<!-- dev → uat sync PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000156` Delegate the dev→uat sync PRs so his review time goes to the diffs that matter.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:261` — Delegate the dev→uat sync PRs so his review time goes to the diffs that matter.

### DECISION: ISSUE_000156_ATTEMPT_01
<!-- Delegate the dev→uat sync PRs so his review time goes to the diffs that matter. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000157` Delegate the #498 Devin Review finding and a font-token regression check — a 23-file CSS refactor with no visual test is a classic Devin task.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:262` — Delegate the #498 Devin Review finding and a font-token regression check — a 23-file CSS refactor with no visual test is a classic Devin task.

### DECISION: ISSUE_000157_ATTEMPT_01
<!-- Delegate the #498 Devin Review finding and a font-token regression check — a 23-file CSS refactor with no visual test is a classic Devin task. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000158` `lgtm` / one-word approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:280` — `lgtm` / one-word approvals — 6 today, incl. 2 prod-branch hotfixes
- [RECOMMENDATION] `SOURCE_011:280` — Adopt the 3-line review template; for prod approvals state the verification performed
- [REPORT_OBSERVATION] `SOURCE_011:280` — previous evidence: 08-21 and 08-24 reports flagged this for him

### DECISION: ISSUE_000158_ATTEMPT_01
<!-- `lgtm` / one-word approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000159` Unifying the same visual pattern across many panes/dialogs by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:306` — Unifying the same visual pattern across many panes/dialogs by hand
- [RECOMMENDATION] `SOURCE_011:306` — Automate with Devin — repetitive pattern migration across similar modules is the canonical delegation

### DECISION: ISSUE_000159_ATTEMPT_01
<!-- Unifying the same visual pattern across many panes/dialogs by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000160` Opening 30–40-file frontend PRs with no reviewer requested

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:307` — Opening 30–40-file frontend PRs with no reviewer requested
- [RECOMMENDATION] `SOURCE_011:307` — Improve documentation/process — request a reviewer at open time

### DECISION: ISSUE_000160_ATTEMPT_01
<!-- Opening 30–40-file frontend PRs with no reviewer requested -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000161` Delegate the remaining pane migrations to the shared `StageHeading` contract — the pattern is fixed after #500.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:310` — Delegate the remaining pane migrations to the shared `StageHeading` contract — the pattern is fixed after #500.

### DECISION: ISSUE_000161_ATTEMPT_01
<!-- Delegate the remaining pane migrations to the shared `StageHeading` contract — the pattern is fixed after #500. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000162` Delegate component tests for the KB dialog dropdown fix; the ResizeObserver polyfill he just added makes them possible.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:311` — Delegate component tests for the KB dialog dropdown fix; the ResizeObserver polyfill he just added makes them possible.

### DECISION: ISSUE_000162_ATTEMPT_01
<!-- Delegate component tests for the KB dialog dropdown fix; the ResizeObserver polyfill he just added makes them possible. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000163` Large frontend PRs opened without a requested reviewer

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:330` — Large frontend PRs opened without a requested reviewer — #499 (15 files), #500 (38 files)
- [RECOMMENDATION] `SOURCE_011:330` — Request a reviewer at open; split the redesign from the behaviour change
- [REPORT_OBSERVATION] `SOURCE_011:330` — previous evidence: #493/#496/#497 on 08-24

### DECISION: ISSUE_000163_ATTEMPT_01
<!-- Large frontend PRs opened without a requested reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000164` Devin Review findings left open on his PRs

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:331` — Devin Review findings left open on his PRs — 1 finding each on #499/#500
- [RECOMMENDATION] `SOURCE_011:331` — Clear findings before asking for review
- [REPORT_OBSERVATION] `SOURCE_011:331` — previous evidence: 08-24 report

### DECISION: ISSUE_000164_ATTEMPT_01
<!-- Devin Review findings left open on his PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000165` Empty-body approvals as the sole gate before `Dev_1.0`

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 9 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:355` — Empty-body approvals as the sole gate before `Dev_1.0`
- [RECOMMENDATION] `SOURCE_011:355` — Improve documentation/process — a one-line verdict is the minimum; he is frequently the only reviewer

### DECISION: ISSUE_000165_ATTEMPT_01
<!-- Empty-body approvals as the sole gate before `Dev_1.0` -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000166` Have Devin produce a pre-merge summary (risk, touched surfaces, missing tests) on PRs where he is the only reviewer, so the approval has evidence behind it.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 9 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:358` — Have Devin produce a pre-merge summary (risk, touched surfaces, missing tests) on PRs where he is the only reviewer, so the approval has evidence behind it.

### DECISION: ISSUE_000166_ATTEMPT_01
<!-- Have Devin produce a pre-merge summary (risk, touched surfaces, missing tests) on PRs where he is the only reviewer, so the approval has evidence behind it. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000167` Delegate the `Dev_1.0` promotion mechanics so his time goes to the diffs.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:359` — Delegate the `Dev_1.0` promotion mechanics so his time goes to the diffs.

### DECISION: ISSUE_000167_ATTEMPT_01
<!-- Delegate the `Dev_1.0` promotion mechanics so his time goes to the diffs. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000168` Empty-body approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 9 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:377` — Empty-body approvals — 2 of 2 today
- [RECOMMENDATION] `SOURCE_011:377` — One-line verdict minimum; escalate anything touching auth/data to a second reviewer
- [REPORT_OBSERVATION] `SOURCE_011:377` — previous evidence: 17 on 08-24 (flagged); flagged on 08-21

### DECISION: ISSUE_000168_ATTEMPT_01
<!-- Empty-body approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000169` Pushing feature work onto another member's long-lived branch with no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:401` — Pushing feature work onto another member's long-lived branch with no PR
- [RECOMMENDATION] `SOURCE_011:401` — Improve documentation/process — cut a PR per repo so the work is reviewable and attributable

### DECISION: ISSUE_000169_ATTEMPT_01
<!-- Pushing feature work onto another member's long-lived branch with no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000170` Delegate the invoicing state-matrix tests (billing states "that tell the truth" implies a state machine worth pinning).

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: BILLING
- Priority: 5 · Complexity: 10 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:404` — Delegate the invoicing state-matrix tests (billing states "that tell the truth" implies a state machine worth pinning).

### DECISION: ISSUE_000170_ATTEMPT_01
<!-- Delegate the invoicing state-matrix tests (billing states "that tell the truth" implies a state machine worth pinning). -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000171` Work living on a long-lived shared branch with no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:422` — Work living on a long-lived shared branch with no PR — 2 commits today, still no PR
- [RECOMMENDATION] `SOURCE_011:422` — Open a draft PR per repo now so review and CI have a target
- [REPORT_OBSERVATION] `SOURCE_011:422` — previous evidence: Branch open since 08-07 (08-22 report flagged the same shape for other members)

### DECISION: ISSUE_000171_ATTEMPT_01
<!-- Work living on a long-lived shared branch with no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000172` Large engine features arriving as a single squashed commit

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:445` — Large engine features arriving as a single squashed commit
- [RECOMMENDATION] `SOURCE_011:445` — Improve documentation/process — commit per stage so the gate/ceiling changes can be reviewed separately (repo rules make these invariants review-critical)

### DECISION: ISSUE_000172_ATTEMPT_01
<!-- Large engine features arriving as a single squashed commit -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000173` Delegate the agentic-memory recall test matrix (routing_override / belief / confusion_pair / confirmed_phrase injection) — bounded, high-value, currently untest

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:448` — Delegate the agentic-memory recall test matrix (routing_override / belief / confusion_pair / confirmed_phrase injection) — bounded, high-value, currently untested.

### DECISION: ISSUE_000173_ATTEMPT_01
<!-- Delegate the agentic-memory recall test matrix (routing_override / belief / confusion_pair / confirmed_phrase injection) — bounded, high-value, currently untest -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000174` Delegate the `Docs//IMPLEMENTATION_GUIDE.md` sync the repo mandates for behaviour changes.

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:449` — Delegate the `Docs//IMPLEMENTATION_GUIDE.md` sync the repo mandates for behaviour changes.

### DECISION: ISSUE_000174_ATTEMPT_01
<!-- Delegate the `Docs//IMPLEMENTATION_GUIDE.md` sync the repo mandates for behaviour changes. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000175` Draft PR with no reviewer requested

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:467` — Draft PR with no reviewer requested — #393 draft, no reviewer
- [RECOMMENDATION] `SOURCE_011:467` — Request a reviewer at draft time; state the acceptance criteria in the body
- [REPORT_OBSERVATION] `SOURCE_011:467` — previous evidence: engine #373 (Devin, draft since 08-20, 6th day) shows drafts stall here

### DECISION: ISSUE_000175_ATTEMPT_01
<!-- Draft PR with no reviewer requested -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000176` Hand-tuning client-config bundles per client

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:490` — Hand-tuning client-config bundles per client
- [RECOMMENDATION] `SOURCE_011:490` — Automate through scripts/tooling — a config-diff report per environment before promotion; the repo's rules put every tunable in bundles precisely so this is mechanical

### DECISION: ISSUE_000176_ATTEMPT_01
<!-- Hand-tuning client-config bundles per client -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000177` Delegate a config-bundle diff/validation tool (dev vs uat vs prod) — a tuning change that reaches `uat` on an `okay` approval currently has no automated check.

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:493` — Delegate a config-bundle diff/validation tool (dev vs uat vs prod) — a tuning change that reaches `uat` on an `okay` approval currently has no automated check.

### DECISION: ISSUE_000177_ATTEMPT_01
<!-- Delegate a config-bundle diff/validation tool (dev vs uat vs prod) — a tuning change that reaches `uat` on an `okay` approval currently has no automated check. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000178` Delegate a regression run over sample charts for the tuned specialties.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:494` — Delegate a regression run over sample charts for the tuned specialties.

### DECISION: ISSUE_000178_ATTEMPT_01
<!-- Delegate a regression run over sample charts for the tuned specialties. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000179` Client-config change to `uat` on a one-word approval

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:512` — Client-config change to `uat` on a one-word approval — #394 merged on `okay`
- [RECOMMENDATION] `SOURCE_011:512` — Require a stated verification (which charts/specialties were exercised) for config tuning
- [REPORT_OBSERVATION] `SOURCE_011:512` — previous evidence: Same pattern on 08-24 (`avinash-codio` config PR #386 to prod)

### DECISION: ISSUE_000179_ATTEMPT_01
<!-- Client-config change to `uat` on a one-word approval -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000180` `okay` approvals on engine PRs he merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:535` — `okay` approvals on engine PRs he merges
- [RECOMMENDATION] `SOURCE_011:535` — Improve documentation/process — one line on what was checked; for coding-behaviour changes name the specialty exercised

### DECISION: ISSUE_000180_ATTEMPT_01
<!-- `okay` approvals on engine PRs he merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000181` Have Devin run the engine's pytest gate on `uat` candidates before merge — the blueprint records 10 known-red tests, so a human eyeballing a diff cannot tell re

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:538` — Have Devin run the engine's pytest gate on `uat` candidates before merge — the blueprint records 10 known-red tests, so a human eyeballing a diff cannot tell regression from baseline.

### DECISION: ISSUE_000181_ATTEMPT_01
<!-- Have Devin run the engine's pytest gate on `uat` candidates before merge — the blueprint records 10 known-red tests, so a human eyeballing a diff cannot tell re -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000182` One-word `okay` approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:556` — One-word `okay` approvals — `okay` on #394
- [RECOMMENDATION] `SOURCE_011:556` — Replace with a two-line template: what was checked, what was not
- [REPORT_OBSERVATION] `SOURCE_011:556` — previous evidence: Flagged in the 08-20, 08-21 and 08-24 reports

### DECISION: ISSUE_000182_ATTEMPT_01
<!-- One-word `okay` approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000183` Renaming/rebinding rule files across specialties by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:581` — Renaming/rebinding rule files across specialties by hand
- [RECOMMENDATION] `SOURCE_011:581` — Automate with Devin — mechanical rename + registry rebind with a discovery test is a textbook delegation

### DECISION: ISSUE_000183_ATTEMPT_01
<!-- Renaming/rebinding rule files across specialties by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000184` Delegate a registry-discovery test that fails when a rule file's `RULE_NAME` has no registry row — the exact class of defect he just fixed four times by hand.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:584` — Delegate a registry-discovery test that fails when a rule file's `RULE_NAME` has no registry row — the exact class of defect he just fixed four times by hand.

### DECISION: ISSUE_000184_ATTEMPT_01
<!-- Delegate a registry-discovery test that fails when a rule file's `RULE_NAME` has no registry row — the exact class of defect he just fixed four times by hand. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000185` Delegate the remaining specialty-module discovery audit.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:585` — Delegate the remaining specialty-module discovery audit.

### DECISION: ISSUE_000185_ATTEMPT_01
<!-- Delegate the remaining specialty-module discovery audit. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000186` Non-descriptive commit messages

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:603` — Non-descriptive commit messages — "…was changes shown before u push"
- [RECOMMENDATION] `SOURCE_011:603` — Squash or amend before PR; the repo mandates `<type>(<scope>): <description>`
- [REPORT_OBSERVATION] `SOURCE_011:603` — previous evidence: 08-20 report flagged non-informative titles/bodies in this repo

### DECISION: ISSUE_000186_ATTEMPT_01
<!-- Non-descriptive commit messages -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000187` Config/rule changes reaching branches without a PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 7 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:604` — Config/rule changes reaching branches without a PR — `feat/guideline` has no PR
- [RECOMMENDATION] `SOURCE_011:604` — Open the PR while the branch is small
- [REPORT_OBSERVATION] `SOURCE_011:604` — previous evidence: #386 merged straight to prod on 08-24

### DECISION: ISSUE_000187_ATTEMPT_01
<!-- Config/rule changes reaching branches without a PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000188` Long-lived PR with a placeholder title accumulating review findings

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:628` — Long-lived PR with a placeholder title accumulating review findings
- [RECOMMENDATION] `SOURCE_011:628` — Improve documentation/process — retitle to the change it makes and answer the findings, or close it

### DECISION: ISSUE_000188_ATTEMPT_01
<!-- Long-lived PR with a placeholder title accumulating review findings -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000189` Delegate the #382 Devin Review findings as a single remediation session.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:631` — Delegate the #382 Devin Review findings as a single remediation session.

### DECISION: ISSUE_000189_ATTEMPT_01
<!-- Delegate the #382 Devin Review findings as a single remediation session. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000190` Delegate DXEX memory-consolidation tests — memory behaviour is cross-cutting and currently unpinned.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:632` — Delegate DXEX memory-consolidation tests — memory behaviour is cross-cutting and currently unpinned.

### DECISION: ISSUE_000190_ATTEMPT_01
<!-- Delegate DXEX memory-consolidation tests — memory behaviour is cross-cutting and currently unpinned. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000191` Non-informative PR titles ("UAT", "config changes ortho")

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:650` — Non-informative PR titles ("UAT", "config changes ortho") — #382 "Testing ortho", 5 days open, 3 new findings
- [RECOMMENDATION] `SOURCE_011:650` — Retitle, fill the body, answer the findings, or close
- [REPORT_OBSERVATION] `SOURCE_011:650` — previous evidence: 08-20 report, this repo

### DECISION: ISSUE_000191_ATTEMPT_01
<!-- Non-informative PR titles ("UAT", "config changes ortho") -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000192` Shared feature branch merged by hand between contributors

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 7 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:673` — Shared feature branch merged by hand between contributors
- [RECOMMENDATION] `SOURCE_011:673` — Improve documentation/process — split into per-member branches with PRs into a shared integration branch

### DECISION: ISSUE_000192_ATTEMPT_01
<!-- Shared feature branch merged by hand between contributors -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000193` Delegate schema-validation tests for the structured-output path through `call_llm` — the repo's single LLM entry point, and its JSON contract is an explicit inv

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:676` — Delegate schema-validation tests for the structured-output path through `call_llm` — the repo's single LLM entry point, and its JSON contract is an explicit invariant.

### DECISION: ISSUE_000193_ATTEMPT_01
<!-- Delegate schema-validation tests for the structured-output path through `call_llm` — the repo's single LLM entry point, and its JSON contract is an explicit inv -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000194` Work on a shared long-lived branch with no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:694` — Work on a shared long-lived branch with no PR — `phrase-semantical-matching`, 3 contributors, no PR
- [RECOMMENDATION] `SOURCE_011:694` — Open a PR for the branch so CI and review have a target
- [REPORT_OBSERVATION] `SOURCE_011:694` — previous evidence: 08-22 report flagged long-lived branches with no PR

### DECISION: ISSUE_000194_ATTEMPT_01
<!-- Work on a shared long-lived branch with no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000195` Agent behaviour changes described only as "handled better"

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:717` — Agent behaviour changes described only as "handled better"
- [RECOMMENDATION] `SOURCE_011:717` — Improve documentation/process — state the behaviour before/after in the commit body

### DECISION: ISSUE_000195_ATTEMPT_01
<!-- Agent behaviour changes described only as "handled better" -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000196` Delegate documentation + tests for the icd-memory agent's handling change so the behaviour is pinned and reviewable.

- Category: MISSING_TEST · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:720` — Delegate documentation + tests for the icd-memory agent's handling change so the behaviour is pinned and reviewable.

### DECISION: ISSUE_000196_ATTEMPT_01
<!-- Delegate documentation + tests for the icd-memory agent's handling change so the behaviour is pinned and reviewable. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000197` Vague commit messages / no PR

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_011:738` — Vague commit messages / no PR — "updated to handle in better way"
- [RECOMMENDATION] `SOURCE_011:738` — State what changed and why; open a PR
- [REPORT_OBSERVATION] `SOURCE_011:738` — previous evidence: 08-20 and 08-24 reports

### DECISION: ISSUE_000197_ATTEMPT_01
<!-- Vague commit messages / no PR -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:

