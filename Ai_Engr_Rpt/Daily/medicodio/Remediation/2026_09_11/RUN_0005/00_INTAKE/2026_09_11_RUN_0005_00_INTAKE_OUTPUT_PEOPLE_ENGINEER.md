# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-11 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_11_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_11_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | `docs(review-logs)` gate/verdict ledgers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | PRD changelog entry per fix commit | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Remediating other authors' PRs before merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Delegate the bounded `(architect-review)` fixes (predicate binding, deterministic lookups, hyphen splitting) to Devin with the review finding as the spec, keepi | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Generate `docs/review-logs/` from the gate run automatically. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000287` | Run the Devin QA gate against the PR branch before merge for PRs >50 files. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Repeat Pattern: reviewer remediates, approves and merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Repeat Pattern: approve/merge within minutes of leaving "needs your decision" items | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Function-header backfills / "docs(headers)" | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Review-log commits (standards, architect, PR-review, green-gate) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Re-pointing specs after signature changes | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Devin-generated regression tests for tenancy predicates (three tenancy/RLS bypass fixes today on `#1349` alone). | SECURITY_TENANCY | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Header/ADR backfill delegated to Devin from the diff. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Pre-merge QA gate on `#1349`-class breaking migrations. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Repeat Pattern: REQUEST CHANGES then own 0-char approve + merge minutes later | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Repeat Pattern: reviewer remediates, approves, merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | PRD/changelog reconciliation ("docs: reconcile the PRDs with what this branch actually shipped") | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000299` | Review-log ledgers (3 today) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000300` | Devin drafts the PRD-delta from the merged diff; human reviews. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Delegate metric/help-text/copy fixes (3 commits today) to Devin. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Repeat Pattern: remediator approves and merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Retiring pages/endpoints and their specs (4 `refactor: retire…` commits) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000304` | Merging `dev` into two feature branches | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Delegate the spec/route retirement sweep after the schema decision. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Use Devin to draft the ADR (anirudh reverse-documented ADR-0048 for him). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | None meeting the recurrence bar | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Change digest + test plan per merged PR | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000309` | Manual repro guides for findings | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Let Devin produce the digest/plan; ragha82 owns adversarial probing and verdict adjudication. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | Convert the `#1342` contrast matrix into an automated a11y check. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000312` | Repairing spec mocks so tests "reach the code they name" | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000313` | Devin to generate the missing `fill_pdf`/typography regression specs from the PR body's acceptance list. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000314` | Insufficient data | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Own the `#1358` fix review — the 5 failures are in surfaces this author built. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Repeat Pattern: own large PR remediated to merge by reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Devin could split `#1322` into font-control vs fill-fidelity PRs for reviewability. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Repeat Pattern: long-open PR advanced by others | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000319` | Dev→UAT promotion PRs titled "dev to uat" | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000320` | Reciprocal 0-char approvals with Jatin | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Devin-generated regression tests for RVU/PFS override paths (two RVU fixes in two days). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000322` | Devin to triage findings on promotion PRs before human approval. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000323` | Repeat Pattern: empty-body approvals on PRs with open Devin findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | "dev->uat" promotion PRs, empty body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000325` | Reciprocal 0-char approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Devin to write the release note for `#626`/`#557` from the 31/44 commits before prod promotion. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Devin regression tests for the kb-payers modal lifecycle (2 fixes in 2 days). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | Repeat Pattern: production promotion merged <2 min with open Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000329` | Repeat Pattern: empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Seed chart answer-key edits | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000331` | Long-running branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Devin maintains seed answer keys from the case-3 spec. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000333` | Draft-PR the inpatient branch so Devin Review runs on 2,009 added lines. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Repeat Pattern: inpatient work on a long-lived branch without a PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000335` | E&M mapping-table edits (MDM options, level rules) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Devin generates E&M level-selection test matrices from the rule tables in `#447`. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000337` | None meeting the recurrence bar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Per-client config additions | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000339` | UAT→prod promotion PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000340` | Devin validates client config files against schema before promotion. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | Devin regression tests for the routing escalation rule. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000342` | Repeat Pattern: prod promotion <2 min with open Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000343` | Repeat Pattern: low-information commit messages | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | "okay" approvals on promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000345` | Devin summarises each promotion's findings into a go/no-go note for him to sign. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000346` | Repeat Pattern: "okay" approvals on prod promotions with open findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000347` | Transcribing PCS guideline rules into code | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000348` | Devin builds test fixtures per PCS guideline (B3.11a/B3.4b etc.) from the rule text. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Draft PR so Devin Review covers +2,356 lines. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Repeat Pattern: inpatient engine branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000351` | Prompt/parameter config tuning commits | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000352` | Devin diff-summarises prompt changes into the commit body. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000128` | Insufficient data | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000353` | None specific — POC stage. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000354` | None meeting the recurrence bar (message quality first flagged today) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000355` | Same change opened as three PRs (Dev/UAT/prod) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000356` | UAT→Dev back-porting | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000357` | Devin writes the Teams-alert payload tests (12 files, 2.4k lines, no test commits). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000358` | Repeat Pattern: manual UAT→Dev back-port | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000359` | Repeat Pattern: prod promotion with un-dispositioned findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000360` | Self-merge of RPA PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000361` | Enable Devin Review on `medicodio-nextgen-rf-rpa-automation`. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000362` | Devin generates Robot Framework payload tests for notification fields. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000363` | Repeat Pattern: RPA self-merge, empty body | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000364` | Repeat Pattern: 0-char approvals on PRs with open findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000365` | Devin adds route tests for the support endpoints once a PR exists. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
