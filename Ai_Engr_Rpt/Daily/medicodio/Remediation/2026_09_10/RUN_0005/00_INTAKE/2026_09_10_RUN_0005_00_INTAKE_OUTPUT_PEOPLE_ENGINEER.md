# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-10 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_10_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_10_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs(review)` gate/verdict logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Remediating another author's week-old PR to mergeable | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000284` | Good Devin Candidate: open a Devin session on `dev` to disposition the 17 fresh `#1312` findings and 3 `#1339` findings, each with commit or reasoned rejection. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Possible Devin Candidate: run the QA gate on the PR branch before merge for PRs > 50 files (needs hosted-env wiring — human decision). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Approver = remediator = merger on large `dev` PRs | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | PRD "reconcile with what shipped" commits | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Hand-written review-log ledgers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000289` | Backfilling function-header comments | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000290` | Good Devin Candidate: disposition the 5 open `#1337` findings. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Good Devin Candidate: the header-backfill and "smaller findings" sweeps (`bbb568e932`). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Possible Devin Candidate: split `#1337` (api / web) — sizing judgement is his. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000293` | Devin findings on his PRs left for others to disposition | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | 700-line-cap file splits | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000295` | Function-header backfills | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Tab-row / badge / DataTable migrations to shared primitives | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000297` | Review-log ledgers ("19-pass ledger") | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Good Devin Candidate: hand the mechanical hygiene sweep (splits, headers, primitive migrations) to Devin per module — ≈ 25 of today's 70 commits. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000299` | Good Devin Candidate: codify the "verified Devin finding — fixed in" disposition as a PR-comment template for the team. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Reviewer remediates, approves and merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Path-param validation across routes | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000302` | RBAC audit-log corrections | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Good Devin Candidate: regression tests for the 3 lost-update races and the private-label leak. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000304` | Good Devin Candidate: path-param validation sweep across remaining document routes. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Generic "Refactor code structure" commits | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Hygiene fixes left for the reviewer (headers, splits, tokens) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000308` | Good Devin Candidate: pre-PR hygiene pass (700-line cap, headers, token violations) — exactly what a colleague did by hand. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Possible Devin Candidate: land the `#1333` DOCX conversion via a fresh scoped PR if the work is still wanted. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Oversized single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000311` | Atlas index regeneration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000312` | Good Devin Candidate: the 13 filed deferrals are pre-scoped Devin tasks. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000313` | Good Devin Candidate: extend `fill_pdf.py` tests to the mirrored fit algorithms she pinned. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Own PR `#1323` idle with open findings | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000315` | Dev→UAT→prod promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000316` | Good Devin Candidate: unit tests for `claimOwner` / filter pruning. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000317` | Good Devin Candidate: promotion-PR body script listing included PRs and open-finding counts. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | Promotion with unanswered Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000320` | Empty approvals on promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000321` | Good Devin Candidate: unit tests for `emMethodForCode` priority and canEdit gating — 4 PRs, 0 tests. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000322` | Possible Devin Candidate: open-findings digest before promotion approval. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000323` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | No tests in app repos | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000325` | UAT-only fixes ported back to Dev by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000326` | Seed values violating DB CHECK constraints | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000327` | Good Devin Candidate: seed-vs-CHECK validation test. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000328` | Good Devin Candidate: UAT↔Dev drift report script. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000329` | UAT→Dev drift ported manually | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000330` | Prod promotion merged < 1 min with badge body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000331` | Empty-body self-merge to `main` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Selector reconnaissance commits ("record the SIS … selectors") | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000333` | Good Devin Candidate: unit tests for the exact-code selection and note formatter libraries. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000334` | Good Devin Candidate: Robot dry-run + `robocop` CI (no CI exists). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000335` | Empty-body self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Empty approvals on integration prod PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000337` | uat→prod approvals within 2 min | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Possible Devin Candidate: open-findings digest on prod PRs (recommended 09-09). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000339` | One-word prod approval with open findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Badge-only prod PR bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | Good Devin Candidate: open a draft PR on `feat/checkpoint`. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | One-word approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000343` | `feat/checkpoint` without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | Real-profile runs recorded as test commits | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000345` | Good Devin Candidate: open the draft PR (4th recommendation). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Possible Devin Candidate: fixtures from the real-profile findings. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Long-running branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000129` | — | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Possible Devin Candidate: contract tests for CDI Phase 2 → coder handoff. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000349` | Shared branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Good Devin Candidate: regression test for the never-saved add/replace bug once a PR exists. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000351` | — | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000352` | PRs closed/left without dispositions | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000353` | Good Devin Candidate: one Devin session to disposition the 14 open findings. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000354` | Devin findings unanswered | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
