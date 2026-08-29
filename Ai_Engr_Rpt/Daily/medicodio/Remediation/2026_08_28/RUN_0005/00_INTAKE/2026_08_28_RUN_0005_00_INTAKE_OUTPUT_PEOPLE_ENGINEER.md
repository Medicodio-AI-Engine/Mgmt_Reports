# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-08-28 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_08_28_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_08_28_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000001` | Low automation-adoption signal for SaijyotiMeti | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000049` | Low automation-adoption signal for Pj-Vineeth-Kumar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000130` | Low automation-adoption signal for svh-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000004` | Low automation-adoption signal for sameer-s-mansur | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000050` | Low automation-adoption signal for jatinkushwaha-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000282` | `docs(review-logs)` write-ups | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Backfilling function headers / doc comments | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Env-var documentation drift | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Use Devin to build a regression suite for the bundle signature/rollback engine, with the fail-open case he just fixed as the first test. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Use Devin to generate the env-var documentation drift check as a CI gate. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000287` | Use Devin to convert his `/check` finding list into a checked-in acceptance checklist for the next content-sync phase. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000288` | Substantive review recorded in a commit, empty approval on GitHub | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Hand-written review logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000290` | `docs(review-log)` write-ups | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Being the org's only substantive reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Hand-fixing the same validation defect on two layers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | Use Devin to turn her review template into a repository skill/checklist so `okay`-style approvals have an alternative that costs less than writing 5,000 charact | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Use Devin to generate the shared-error-code contract tests between API and web. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000295` | Use Devin to draft the review-log entries from the gate output. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Review quality concentrated in one person | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Manual QA passes on `feat/qa-automation` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Empty approvals | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Extend #1253's interaction matrix to the Document Checklist and file-number surfaces, which absorbed two hand-run QA cycles this week. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Use Devin to convert the `qa update` PR bodies into executable e2e specs. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Use Devin to wire the e2e suite into the gate so QA findings arrive before merge, not after. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Low-information approval | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Manual `dev` merges into feature branches | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000304` | Filter/label UI changes applied per surface | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | Use Devin to write regression tests for configurable file-number generation, including the collision → 409 path. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000306` | Use Devin to split #1239 into reviewable slices so it can land. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000307` | Use Devin to consolidate case-list filter behaviour into one tested component. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Devin PR opened, then left without a reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Post-merge QA hardening passes | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000310` | Same defect class fixed surface-by-surface (URL state, focus restore) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000311` | Hand-written review/gate logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000312` | Use Devin to generate an a11y + URL-state regression suite for the checklist surfaces. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000313` | Use Devin to extract a single tested URL-state hook and migrate the call sites. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Use Devin to run the pre-merge `/check` pass so the QA-fix PR becomes unnecessary. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Feature lands, then a separate QA-hardening PR follows | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Promotion fan-out (`Dev_1.0` → `release/prod_1.0` cherry-pick PRs) | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000317` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000318` | Facility-day state semantics corrected in 13 successive PRs | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000319` | Use Devin to generate a state-machine test suite for the facility-day states, seeded with the 13 defects fixed today — it would have caught most of them before  | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000320` | Use Devin to write the promotion script that opens the `Dev_1.0`→prod cherry-pick PR with a filled body. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000321` | Use Devin to answer the 5 open findings on #249 before it merges. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Empty-bodied approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Behaviour changes to a production dashboard with no tests | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Promotion fan-out | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000325` | One-word approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | `uat` → `release/prod_3.0` promotion PRs with template-only bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Journey/attribution logic verified by reading output | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000328` | Use Devin to build golden-file tests for `guidelines_journey` per-target attribution across the lanes he added (laterality, BMI/Z68, split, `excludes1`). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000329` | Use Devin to generate promotion PR bodies (included PRs, risk, rollback) from the diff. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000330` | Land #405 by adding acceptance criteria and requesting review. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000331` | One-word approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Promotion merged with an open Devin Review finding | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000333` | Promotion fan-out | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000334` | Batch/ledger invariants stated in prose then verified by hand | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000335` | Template-only PR bodies on promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000336` | Use Devin to convert his written batch/ledger invariants into a regression suite (cached re-run, dual writers, event-driven vs RPA warning, blank insurance cate | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000337` | Use Devin to script the three-stage promotion so the bodies are generated. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000338` | Use Devin to write fixtures for the gender-resolution precedence rules he just shipped. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Production batch-semantics changes with zero tests | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000341` | Promotion fan-out with template bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000342` | Same change authored twice across nodejs and react | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000343` | UI style tweaks committed individually | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | Manual `Dev_1.0` sync into the feature branch | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000345` | Use Devin to generate a regression suite for the encounter decrypt/patch path, asserting the age field and PHI masking. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000346` | Use Devin to table-drive the login error-message contract across API and UI. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Use Devin to produce the cross-repo API contract test so paired changes cannot drift. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | PHI-adjacent change with no tests | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000350` | Client-config routing edits per specialty | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000351` | Promotion PRs with template bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000352` | Draft Devin PRs left idle | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000353` | Use Devin to build KB-table-driven fixtures for the I.B.9 collapse redesign in #411, where 3 findings are currently open. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000354` | Use Devin to validate client-config routing changes against a schema so podiatry-style exclusions cannot regress. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000355` | Close out #393 or convert it into a scoped, reviewable PR. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000356` | Rich feature bodies, template-only promotion bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000357` | Devin draft opened then idle | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000358` | Same-minute `uat`→prod promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000359` | Trigger-field corrections | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000360` | Template-only PR bodies | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000361` | Use Devin to generate a routing-trigger fixture suite keyed on `type_of_service_id` / `type_of_visit_id`, so a field mismatch fails a test rather than a chart. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000362` | Use Devin to write the P039-vs-P036 lab-source contract test that pins the refactor he just made. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000363` | Use Devin to draft his promotion PR bodies. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000364` | Promotion to `release/prod_3.0` within a minute of merge | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000365` | Behaviour change to chart routing with no tests | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000366` | Approving three-stage promotion chains | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000367` | Empty approval bodies | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000368` | Use Devin to generate a promotion checklist comment (diff summary, findings status, migration presence) so his approval has something concrete to confirm. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000369` | Use Devin to script the `Dev_1.0`→`Uat_1.0`→prod chain into a single reviewed unit. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000370` | Empty approvals on production promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000371` | Guideline-rule gating fixes verified by reading the rule | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000372` | Use Devin to generate unit tests for the guideline-rule predicates (`match.present`, exclusion lanes) she has now corrected twice. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000373` | Use Devin to answer Devin Review findings before merge rather than leaving them open. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000374` | Merge with an open Devin Review finding | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000375` | Same-minute prod promotion with template body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000376` | Use Devin to write BMI/Z68 gating fixtures across client configurations. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000377` | Use Devin to generate the promotion body from the diff. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000378` | Promotion opened and merged within minutes on a template body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000379` | Work accumulating on a draft branch without reaching review | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000380` | Scope the ICD memory-manager agent as a Devin task with explicit acceptance criteria and requested tests. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000381` | Use Devin to split #393 into a reviewable first slice. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000382` | Work not reaching a reviewable state | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
