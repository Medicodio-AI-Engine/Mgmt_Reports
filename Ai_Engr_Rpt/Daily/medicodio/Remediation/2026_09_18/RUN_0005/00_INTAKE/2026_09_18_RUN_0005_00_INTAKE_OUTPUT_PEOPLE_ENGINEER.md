# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-18 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_18_Employee_Rating_Cards.md, 2026_09_18_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_18_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_18_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | `docs(review-logs): close … with the real gate matrix` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Filing CLEANUP-xxx items by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Test-mock repair after schema/catalog change (12 commits) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Delegate the review-log / gate-matrix closing commit: input = CI run URL + QA report path, output = the log section. Removes ~3 manual commits/day. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Ask Devin for a mock-consistency sweep whenever a catalog constant changes (today's 12 fix commits are exactly this shape). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Have Devin draft the pre-merge QA verdict summary into the PR body so the merge decision cites it. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Merge before the Devin QA verdict | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Reviewer remediates, approves, merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Self-merge on a 7-s empty co-approval | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | `#1358` closed without disposition | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Function-header backfill (§4.2) — 25 files today, 21 files on `#1380` 09-16 | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | Timestamp-surface sweep ("close the surfaces the sweep missed") | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Remediating a colleague's PR end-to-end before approving | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Generate a timestamp-surface inventory test (every component that renders a date gets one fixture) so the "surfaces the sweep missed" class closes permanently. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Delegate the header-backfill as a lint autofix PR rather than 25-file manual commits. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Use Devin to draft the "known risks" section for `#1390`'s follow-up so the 70/100 verdict has an owner list. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Reviewer remediates, then approves and merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | QA verdict after merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | "repair the typecheck and lint failures the first gate run surfaced" | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000301` | Standards-audit doc + gate history | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000302` | Split `#1391` by runtime (api / worker / scheduler / web) with Devin generating the per-runtime PR bodies from the audit doc. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000303` | Migration dry-run + rollback checklist for the path-registry split. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000304` | >200-file single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000305` | Multi-day branch without PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Phase-result ledger commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000307` | DOCX-fidelity fixture tests: template → rendered → expected table/spacing attributes. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Open `feat/support-letter-word-fidelity` as a draft now; let Devin Review run on the 84-file move before more lands on top. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Branch without PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Feature finished by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | "expose Prometheus metrics …" per service | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000312` | Generate metric-name + label-cardinality tests per service from the shared factory. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000313` | Have Devin triage the 15 findings into "fix / accept with reason / out of scope" so the disposition is a review, not a rewrite. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Findings left undispositioned | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Empty approvals on >200-file PRs | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Ask Devin for a "what changed since my last look" digest before approving a 250-file PR. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Empty co-approval enabling self-merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000318` | — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | `#1373` decision items 1–3 (in prod since 09-15) — Devin can draft the decision record from the thread. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | `#1373` decisions unrecorded | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Manual `Dev_1.0 → Dev_2.0` sync PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000322` | Hand-made `dev → uat` promotion PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000323` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Scheduled `Dev_1.0 → Dev_2.0` sync PR whose body lists the ported commits and conflicts — replaces `#6`. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000325` | Regression tests for the writeback cron under 2+ replicas (Devin can extend today's `withCronLock` spec). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000326` | Promotion manifest: "PRs and Devin findings carried by this promotion" auto-generated. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Empty approvals on prod-bound PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000328` | Hand-made sync/promotion PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000329` | Production `23505` fix (`#651` closed) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Three successive "enhance/improve error handling" refactors on the same file | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000331` | Regression tests for cron-expression edge cases (blank, nonzero seconds, day-constraint intersection) — the last three findings on `#584`/`#657` are exactly thi | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000332` | Multi-replica test harness for the import trigger (two workers, one lock). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000333` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Partial finding disposition on prod-path features | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000335` | Per-client ENM rule branches (DVG, McQueen) | AUTOMATION_OPPORTUNITY | nextgen-codio-engine | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000336` | Turn each "verified unreachable" disposition into an executable test so the argument cannot rot. | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000337` | Generate the per-client parity fixtures for the E&M level rule. | AUTOMATION_OPPORTUNITY | nextgen-codio-engine | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000338` | — | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Manual `client_configs` sync from prod DB | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000340` | `uat → prod` template promotions | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | Client-config diff report (what knob changed, which client, which gate) posted to the PR before merge. | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | A real parity guard test for the gynecology clone (the finding says the current one checks nothing). | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000343` | Prod promotion on ≤4-char approval | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000344` | Findings unanswered after merge | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000345` | `feat/log_prob` branch without PR | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Prompt files recovered/reverted by hand | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | 4-char approvals on prod PRs | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | A prompt-diff check that fails CI when `dx/px` extraction prompts change without a changelog entry. | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Have Devin reproduce the BMI finding (`Z68` inactive) on a fixture chart. | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Merge-then-revert on prompt content | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000351` | Prod promotion with an open Devin finding | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000352` | 0-minute merges | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000353` | A merge-queue rule: no merge until Devin Review has posted. | PROCESS_PRACTICE | nextgen-codio-engine | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000354` | Merge before automated review posts | AUTOMATION_OPPORTUNITY | nextgen-codio-engine | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000355` | Prompt-variant runs via runner flags | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000356` | Eval-report generator for prompt promotions (recall/precision per chart set) attached to the PR. | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000357` | — | MECHANICAL_MIGRATION | nextgen-codio-engine | — | — | — | CODE_CHANGE |
| `ISSUE_000358` | Self-merge to `main` 0 min after open | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000359` | Per-branch split skeletons (three endoscopy branches) | MECHANICAL_MIGRATION | medicodio-nextgen-rf-rpa-automation | — | — | — | CODE_CHANGE |
| `ISSUE_000360` | Screenshot-diff replay harness for the split flow ("one stitched picture per split" is already captured — assert on it). | MISSING_TEST | medicodio-nextgen-rf-rpa-automation | — | — | — | CODE_CHANGE |
| `ISSUE_000361` | Table-driven test for the eleven splitting insurances. | MECHANICAL_MIGRATION | medicodio-nextgen-rf-rpa-automation | — | — | — | CODE_CHANGE |
| `ISSUE_000362` | Self-merge to `main`, no review | PROCESS_PRACTICE | medicodio-nextgen-rf-rpa-automation | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000363` | Lockfile churn repair after merges | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000364` | Lockfile-drift CI check. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000365` | `hitesh/` branches under `karthikmed` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000366` | Same secret/doc fix applied to 3 repos by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000367` | Env-example consistency check across nodejs/react/2.0. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000368` | Devin-reviewed PR closed without disposition | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000369` | Direct pushes without PR | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000370` | Retry/back-off tests for eCW PPV lookups (Good Devin Candidate). | MISSING_TEST | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000371` | — | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
