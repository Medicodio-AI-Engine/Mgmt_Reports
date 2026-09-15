# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-15 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_15_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_15_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | "regenerate atlas (module_map, screen_index)" commit | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Remediating a peer's PR before approving it | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1 | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets  | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Reviewer remediates, then approves, then merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Merge with own "needs your decision" items open | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Post-merge Devin QA NOT READY | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Hand-written review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Atlas regeneration / function-header sync / debt-ledger sync commits | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000293` | `/review-all` ledger written into `docs/review-logs/` by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Review-pass commits on a peer's branch | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before  | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Devin QA gate pre-merge on `#1373` (shared with Saijyoti). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Review-pass as 20+ direct commits on a peer's PR instead of a review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Work on a branch without a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Sync/regeneration chores as human commits | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000301` | Hand-fixing Devin PRs after Devin Review findings | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000302` | Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000303` | Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000304` | Small PRs left open without requesting review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Large PR opened without a named reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000306` | Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Devin QA gate on `#1363` before merge — the PR touches performance/security paths. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | >60-file PR without reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Branch with large checkpoint, no PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | `feat/hr-portal-revamp` no PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Placeholder `Co-Authored-By` Devin e-mails | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000313` | Findings/promotions carried without disposition | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000314` | `feat/inpatient-engine` no PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Reviews ≤10 chars on production-bound PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
