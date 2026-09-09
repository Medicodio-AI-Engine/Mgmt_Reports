# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-09 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_09_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_09_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Dev→UAT / UAT→prod promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000283` | CI-probe no-op PR to exercise the unit-test stage | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Same-morning "address Devin review" follow-up commits | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review foun | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000288` | Empty approvals on prod-path PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | CI-probe PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Prod promotions with badge-only body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000291` | Manual verification of add-on state edge cases | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000292` | Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000293` | Coder-performance dedupe golden fixtures (scope filter on/off). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Empty approvals on prod promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000295` | Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Two prod promotions per day | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000297` | Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Prod promotion with unanswered Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000300` | Selector / dialog timing fixes discovered by running the robot | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000301` | Self-merge of feature branch to `main` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000304` | Add `robocop`/dry-run lint as a GitHub Action. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Empty approvals on integration prod path | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Self-merge, no review (new) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | One-word approvals ("okay") | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Manual `client_configs` list edits that silently regress (`04d7512c`) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000309` | Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Ask Devin for an open-findings digest before merging others' PRs. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | One-word approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Ordering/routing logic verified by reading, not golden tests | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000313` | Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000314` | Golden tests for routing/assembly absent | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000129` | — | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000318` | Unanswered Devin findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | One-word approvals on PRs with open findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Checkpoint round-trip tests (write → resume → identical output). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Approves / merges with open findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Template/badge-only bodies | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Gate-by-gate fixes discovered by running charts | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000325` | Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Fixture generation for the principal-drop regression. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000327` | Long-running branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000328` | Large schema/field moves across 65 files by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000329` | Contract tests for `asserted_at` / `author_role` stamping. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000330` | Work on shared branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000331` | Finishing other people's large PRs to get them merged | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Green-gate matrix documented by hand in `docs/review` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000333` | Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000335` | Large PR finished and merged by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Hand-written `docs(review-logs)` and atlas regeneration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000337` | 40-commit single-day PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000338` | Disposition the 5 `#1336` findings via Devin with reasons before requesting review. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Split `#1336` with Devin's help into db-migration / api / web PRs. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000340` | Very large PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | `/check` audit logs written by hand into `docs/review` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000342` | Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction") | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000343` | Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | One regression test per QA finding in `#1334` (2 findings → verify 2 tests). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000345` | >50-file PRs open concurrently | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Devin findings unanswered | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Large UI feature commits (60–99 files) on a personal branch without PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Work without PR (`feat/mobbin-trails`) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000351` | Ownership-guard exemptions added case by case | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000352` | Regression tests for the ownership guard (guidance-only vs rule writes). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000353` | Draft PR for the branch. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000354` | — (branch without PR is new for her) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000355` | Re-syncing long-lived feature branch with `dev` | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000356` | Regression test for the remediation-card case (from 09-08). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000357` | — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
