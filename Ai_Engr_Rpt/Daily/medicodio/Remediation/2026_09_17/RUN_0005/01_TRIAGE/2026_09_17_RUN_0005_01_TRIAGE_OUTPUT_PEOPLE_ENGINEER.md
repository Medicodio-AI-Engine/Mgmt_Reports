# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-17 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_17_Employee_Rating_Cards.md, 2026_09_17_Mgmt_Activity_Report.md; dated by filename only, no stated review date

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written architect/PR review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | "Repair N broken specs surfaced by the scoped gate" | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | PRD/atlas/doc reconciliation after code lands | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Delegate the `#1380` QA gate's two open items (locate the send-reminder durable record; refresh `E2E_FIRM2_`/`E2E_RBAC_`) as a scoped Devin session with the QA  | PROCESS_PRACTICE | globalcodio-monorepo | 5 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Have Devin answer/triage the 9 `#1389` findings with tests before a human reviewer is asked. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Pre-review scoped test gate as a Devin check so spec repair is not done by the reviewer. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Reviewer remediates, then approves and merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Own `[needs decision]` left open at merge | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | `chore(atlas)` regeneration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Review-log + standards-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Closing Devin fix/report PRs without a note | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Run the `20260915000000_entity_status_phase1` migration + full Jest on a hosted dev clone and post the result on `#1386` before review. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Regenerate the atlas on merge to `dev` (removes a daily manual commit for him, akanksh and Saijyoti). | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000295` | Disposition sweep: for `#1358/#1360/#1369/#1371` produce a table of "fix lives in commit X / superseded / still open". | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Devin fix PRs for confirmed failures closed without disposition | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | >200-file feature PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000298` | Post-merge findings left undispositioned | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Doc sync after code change (`docs(architecture)`, `docs(ops)`, `docs(tracking)`) | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000300` | Spec repairs left by refactors (`ModuleAccessGuard`, `@jest/globals` import) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000301` | Re-open the timezone work as a stack of Devin PRs (schema/selector → formatter → ~130 call sites) with per-stack tests, instead of one squash commit. | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000302` | Delegate the `E2E_FIRM2`/`E2E_RBAC` secret refresh + re-run of the cross-firm attacker probe from the `#1380` QA gate. | PROCESS_PRACTICE | globalcodio-monorepo | 5 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Regression tests for the retired `/hr/pipeline` and health-score routes (deep links, agent tool). | MISSING_TEST | globalcodio-monorepo | 5 | 2 | — | CODE_CHANGE |
| `ISSUE_000304` | Schema drop inside an oversized feature PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Devin PR on his branch never reviewed | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Atlas regeneration commit | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000307` | Delegate the `#1373` §4.4 correction script + UAT/prod counts. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000308` | Atlas regeneration as CI. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000309` | `#1373` NEEDS-DECISION items open in production | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000310` | `dev -> uat` promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000311` | Empty approvals on peer PRs within 2 min | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Regression tests for RLS `current_user_id` scoping (`setRlsOnConnection` callers) — the same class fixed twice this week. | SECURITY_TENANCY | unresolved | 10 | 10 | — | CODE_CHANGE |
| `ISSUE_000313` | Promotion manifest generator that lists unresolved Devin findings on the included PRs (would have surfaced the `#646` RLS finding). | SECURITY_TENANCY | unresolved | 10 | 10 | — | CODE_CHANGE |
| `ISSUE_000314` | A nodejs test run as a required check on `Dev_1.0` (09-16 recommendation, still absent). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000316` | Unanswered finding at promotion merge | SECURITY_TENANCY | unresolved | 10 | 10 | — | CODE_CHANGE |
| `ISSUE_000317` | Empty approvals 1–2 min after Devin Review | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000318` | `Dev_1.0 → Dev_2.0` app sync merges | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000319` | Repo-structure doc regeneration | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000320` | A pg-backed concurrency test for resolve vs heartbeat (`uq_enc_reviews_active_per_coder`) — would have made one PR of three. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Scheduled `Dev_1.0 → Dev_2.0` sync PR with conflict report. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000322` | "What to check" digest per PR he approves. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Empty approvals on prod-bound PRs | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Iterative "close N defects found in review" commits | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000325` | Generate the PR bodies from his commit narrative (Why/What/Risk/Rollback). | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000326` | Money-path property tests (invoice totals, fee recomputation) Devin Review probed three times. | PROCESS_PRACTICE | unresolved | 5 | 10 | — | NON_CODE_PROCESS |
| `ISSUE_000327` | Split `#652` into schema → services → scripts stacks. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000328` | — | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000329` | Long-lived branch without PR | PROCESS_PRACTICE | unresolved | 3 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Open a draft PR in `Dev_2.0` and let Devin Review run on the port. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000331` | Inpatient chart fixture generation. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Branch without PR | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000333` | `UAT TO PROD` PRs with template bodies | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000334` | Unit tests for the stage-4 exclusion loader (the prod revert was a `TypeError` class Devin flagged). | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000335` | Pre-promotion check running the linking suite. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000336` | `uat`/prod PRs with no substantive human review | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000337` | One-word approvals on prod promotions | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000338` | Manual revert / revert-of-revert PRs | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000339` | Rollback runbook + script. | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000340` | Consistency-POC evaluation harness (bounded, data-driven) once the POC design is fixed — Possible Devin Candidate. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000341` | One-word approvals on prod promotions | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000342` | Self-merged PRs with empty bodies | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000343` | Enable Devin Review on the repo. | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000344` | PR body generation from diff. | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000345` | — | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000346` | ragha82: delegate the `date-helpers` spec fix (one-line, confirmed by QA). | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Post-merge QA finding unaddressed (ragha82) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Hand-written architect/PR review-log commits

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (16) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` "Repair N broken specs surfaced by the scoped gate"

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1367) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000284` PRD/atlas/doc reconciliation after code lands

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000285` Delegate the `#1380` QA gate's two open items (locate the send-reminder durable record; refresh `E2E_FIRM2_`/`E2E_RBAC_`) as a scoped Devin session with the QA 

- Priority: Priority 5/10 from base 3 adjusted by: security scope AUTHORIZATION (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.6

### `ISSUE_000286` Have Devin answer/triage the 9 `#1389` findings with tests before a human reviewer is asked.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000287` Pre-review scoped test gate as a Devin check so spec repair is not done by the reviewer.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Reviewer remediates, then approves and merges the same PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000289` Own `[needs decision]` left open at merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000290` `chore(atlas)` regeneration

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (15) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000291` Review-log + standards-log commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000292` Closing Devin fix/report PRs without a note

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (15) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000293` Run the `20260915000000_entity_status_phase1` migration + full Jest on a hosted dev clone and post the result on `#1386` before review.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000294` Regenerate the atlas on merge to `dev` (removes a daily manual commit for him, akanksh and Saijyoti).

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000295` Disposition sweep: for `#1358/#1360/#1369/#1371` produce a table of "fix lives in commit X / superseded / still open".

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000296` Devin fix PRs for confirmed failures closed without disposition

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000297` >200-file feature PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000298` Post-merge findings left undispositioned

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000299` Doc sync after code change (`docs(architecture)`, `docs(ops)`, `docs(tracking)`)

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (15) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000300` Spec repairs left by refactors (`ModuleAccessGuard`, `@jest/globals` import)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000301` Re-open the timezone work as a stack of Devin PRs (schema/selector → formatter → ~130 call sites) with per-stack tests, instead of one squash commit.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000302` Delegate the `E2E_FIRM2`/`E2E_RBAC` secret refresh + re-run of the cross-firm attacker probe from the `#1380` QA gate.

- Priority: Priority 5/10 from base 3 adjusted by: security scope AUTHORIZATION (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.6

### `ISSUE_000303` Regression tests for the retired `/hr/pipeline` and health-score routes (deep links, agent tool).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 2/10 from: category MISSING_TEST base 3; repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000304` Schema drop inside an oversized feature PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000305` Devin PR on his branch never reviewed

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000306` Atlas regeneration commit

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (15) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000307` Delegate the `#1373` §4.4 correction script + UAT/prod counts.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000308` Atlas regeneration as CI.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000309` `#1373` NEEDS-DECISION items open in production

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000310` `dev -> uat` promotion PRs with badge-only bodies

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (12) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000311` Empty approvals on peer PRs within 2 min

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000312` Regression tests for RLS `current_user_id` scoping (`setRlsOnConnection` callers) — the same class fixed twice this week.

- Priority: Priority 10/10 from base 3 adjusted by: category SECURITY_TENANCY (+4); security scope TENANT_ISOLATION (+4).
- Complexity: Complexity 10/10 from: category SECURITY_TENANCY base 9; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface TENANT_ISOLATION (+2).
- Confidence: 0.5

### `ISSUE_000313` Promotion manifest generator that lists unresolved Devin findings on the included PRs (would have surfaced the `#646` RLS finding).

- Priority: Priority 10/10 from base 3 adjusted by: category SECURITY_TENANCY (+4); security scope TENANT_ISOLATION (+4).
- Complexity: Complexity 10/10 from: category SECURITY_TENANCY base 9; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface TENANT_ISOLATION (+2).
- Confidence: 0.6

### `ISSUE_000314` A nodejs test run as a required check on `Dev_1.0` (09-16 recommendation, still absent).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000315` Promotion PRs with badge-only bodies

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000316` Unanswered finding at promotion merge

- Priority: Priority 10/10 from base 3 adjusted by: category SECURITY_TENANCY (+4); security scope TENANT_ISOLATION (+4).
- Complexity: Complexity 10/10 from: category SECURITY_TENANCY base 9; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface TENANT_ISOLATION (+2).
- Confidence: 0.65

### `ISSUE_000317` Empty approvals 1–2 min after Devin Review

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (27) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000318` `Dev_1.0 → Dev_2.0` app sync merges

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000319` Repo-structure doc regeneration

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000320` A pg-backed concurrency test for resolve vs heartbeat (`uq_enc_reviews_active_per_coder`) — would have made one PR of three.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000321` Scheduled `Dev_1.0 → Dev_2.0` sync PR with conflict report.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000322` "What to check" digest per PR he approves.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000323` Empty approvals on prod-bound PRs

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000324` Iterative "close N defects found in review" commits

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000325` Generate the PR bodies from his commit narrative (Why/What/Risk/Rollback).

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000326` Money-path property tests (invoice totals, fee recomputation) Devin Review probed three times.

- Priority: Priority 5/10 from base 3 adjusted by: security scope BILLING (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 10/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface BILLING (+2).
- Confidence: 0.5

### `ISSUE_000327` Split `#652` into schema → services → scripts stacks.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000328` —

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000329` Long-lived branch without PR

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (11) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000330` Open a draft PR in `Dev_2.0` and let Devin Review run on the port.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000331` Inpatient chart fixture generation.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000332` Branch without PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000333` `UAT TO PROD` PRs with template bodies

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (458) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000334` Unit tests for the stage-4 exclusion loader (the prod revert was a `TypeError` class Devin flagged).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000335` Pre-promotion check running the linking suite.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000336` `uat`/prod PRs with no substantive human review

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000337` One-word approvals on prod promotions

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (27) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000338` Manual revert / revert-of-revert PRs

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000339` Rollback runbook + script.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000340` Consistency-POC evaluation harness (bounded, data-driven) once the POC design is fixed — Possible Devin Candidate.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000341` One-word approvals on prod promotions

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000342` Self-merged PRs with empty bodies

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (20) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000343` Enable Devin Review on the repo.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000344` PR body generation from diff.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000345` —

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000346` ragha82: delegate the `date-helpers` spec fix (one-line, confirmed by QA).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000347` Post-merge QA finding unaddressed (ragha82)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.
