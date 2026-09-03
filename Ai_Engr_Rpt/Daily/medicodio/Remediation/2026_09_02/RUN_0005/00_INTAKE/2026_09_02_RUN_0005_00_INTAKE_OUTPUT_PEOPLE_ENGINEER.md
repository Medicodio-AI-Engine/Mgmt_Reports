# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-02 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_02_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_02_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs(review)` log commits recording gate results | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Remediating a colleague's branch before reviewing it | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000284` | Delegate the `READ COMMITTED` transaction concern on `SupportLetterService` (left as `[needs your decision]`) as a scoped reproduction test. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Delegate review-log generation from gate output. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Delegate the `matchedLetters` search-parity fix (minor, clearly scoped, left unfixed). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Reviewer remediates then approves | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Hand-written review-log commits | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Long-lived branch merged from `dev` repeatedly before a PR exists | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Own the remaining `[needs your decision]` items on #1282 (transaction isolation, `matchedLetters` parity) as scoped Devin tasks. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Delegate the `DraftLetterAiSkill` reject/no-owner test matrix for the next skill. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000292` | Large feature accumulating without a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Bundle decode/reference defects fixed one at a time | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Merging `dev` into the feature branch | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000295` | Non-mocked content-sync integration suite (third report recommending it). | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000296` | Delegate a fixture generator that produces a bundle exercising every column type and every FK shape (`id` and non-`id`). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Delegate the worker/API internal-token contract test that today's "declare the internal token the async import made mandatory" fix implies was missing. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | Decode/reference defects discovered serially after the fact | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000299` | Hand-written review-log / runbook commits (5 today) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000300` | Delegate the OpenAPI DTO shape + catalog binding sweep — a mechanical pattern migration across API and web. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Delegate the deploy-runbook generation from the migration file. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Address round-N PRD review findings | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000304` | Devin docs PRs superseded and closed unmerged | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Keep using Devin for as-built documentation — it is a Good Devin Candidate — but merge it: none of the three docs PRs this window landed. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Ask Devin for a one-page decision list from the PRD rather than another review round. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Devin docs PRs closed unmerged / superseded | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Manually closing stale QA-gate PRs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000309` | Re-syncing `feat/qa-automation` with `dev` via giant PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000310` | Make the gate emit a machine-readable verdict and wire it to branch protection on `dev`. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000311` | Delegate an ACU-per-gate report so "122.5 ACU validated nothing" is caught after one run, not five. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Self-merge with no review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000313` | Mirroring a BE analytics config change into FE by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000314` | `Dev_1.0` → `release/prod_1.0` promotion PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000315` | Analytics config contract test (BE default ↔ FE fail-closed). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Delegate a compile/typecheck gate so a missing import cannot merge (`#525` was a self-inflicted fix 3 minutes after the break merged). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Regression tests for the prediction-trail stage rail (reverted once by hitesh on 08-31, re-touched today). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | Behaviour change with no tests | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Empty approve + immediate merge on `Dev_1.0` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Delegate a merge-readiness summary bot for `Dev_1.0` PRs so the approval has content. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Revive `#249` prompt registry (14 reviews, idle) as a Devin remediation task. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Content-free approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Stalled own PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000325` | Column-visibility migration edge cases fixed serially | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000326` | "Prod fix issue" promotion PR with template body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | `sanitizeVisibleColumns` / `autoEnabledColumns` state-machine tests. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000328` | Auto-generated promotion PR body from the `Dev_1.0` diff. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000329` | Template-only body on a production promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000330` | Per-facility onboarding | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000331` | Dev → Uat → prod promotion PRs with template bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000332` | PHI-in-logs regression test for the redactor and the LLM-payload gate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000333` | Run the `/onboard-facility` skill via Devin for the next facility and measure the delta. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Self-merge with zero review on `Dev_1.0` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000335` | Template-only bodies on promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000336` | Approve-and-merge promotions within seconds | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000337` | None — this is a release-gate role; the improvement is a checklist, not delegation. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Empty approvals on production promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000339` | `okay` approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Manual `uat` → `release/prod_3.0` promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | KB-table-driven add-on/base phrase fixtures. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | Delegate a diff-summary comment for engine promotions so the `okay` has something to attach to. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000343` | One-word approvals incl. production | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | Prod client-config seeding by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000345` | Client-config drift check that fails when config references a key the deployed code does not read. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Combination-code fixtures from the KB table. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Devin findings on #411 unanswered | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Promotion PRs with `---` body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000349` | Generated promotion body listing included PRs. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000350` | Template-only production promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
