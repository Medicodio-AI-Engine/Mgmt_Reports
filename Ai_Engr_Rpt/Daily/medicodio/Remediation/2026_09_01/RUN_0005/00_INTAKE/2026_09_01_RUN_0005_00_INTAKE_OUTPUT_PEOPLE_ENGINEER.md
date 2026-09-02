# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-01 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_01_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_01_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs/review-logs/` entries recording gate results | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Backfilling function headers to satisfy the standards audit | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Fixing tests left stale by someone else's merge into `dev` | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000285` | Delegate the HR-reports persona/permission test matrix that the QA gate could not execute — 8 report views × org-scoping × role, as code-level integration tests | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate review-log generation from the gate runner's output, removing ~6 commits per feature branch. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Delegate the 2 documented "unresolvable without a decision" findings as a scoped investigation producing options, once the product decision exists. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Approving and merging a PR one drove | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Merging ahead of the post-merge QA gate | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000290` | Fixing one content-sync decode/type class at a time | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000291` | Re-typing the same "scannability" UI polish across import/export surfaces | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Content-sync type-coverage corpus: delegate a fixture bundle exercising every column type in `schema.prisma` (enum, enum[], `@db.Date`, JSON, nullable) round-tr | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000293` | Delegate the red spec on `dev` that `#1267` reported, as a bounded fix-with-repro session. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Merge minutes after a content-free approval | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Merging while a QA gate reports NOT READY | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000296` | Placeholder commit messages | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Hand-written standards-audit and remediation logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Correcting specs that "never caught up with what this branch changed" | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Open the draft PR, then delegate the subscriber/notification test matrix for the draft-letter skill — this is the third report to recommend it and the branch no | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000300` | Delegate the seven test failures recorded in today's gate log as a single bounded fix session. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Large feature accumulating without a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Content-free approval on a very large diff | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Merging other people's PRs on `dev` minutes after opening | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000304` | QA gates re-running the same credential-free probes and reaching no verdict | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | Delegate a seeded QA persona fixture for hosted-dev (idempotent seed script + credential storage), which unblocks every gate the automation currently cannot com | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000306` | Have the QA automation emit a machine-readable verdict (`READY` / `NOT READY` / `NO VERDICT`) as a required status check, so a NOT READY result blocks the next  | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000307` | Content-free approvals | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | QA gate output not consumed | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Manually re-checking read-only enforcement across case tabs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000310` | Delegate the closed/archived-case read-only enforcement matrix (every tab × every mutating action) as tests, which is exactly the manual verification `#1258` ke | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | PR awaiting a human verdict for days | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000312` | Content-free approval on a large diff | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000313` | Duplicating each change into a `-dev` and a `-prod` branch and PR by hand | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000314` | Iterating access-control rules by successive small fixes | SECURITY_TENANCY | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000315` | Delegate an approver-routing decision-table test suite: (requester role × affected client × peer availability × Support fallback) → expected approver. This is s | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000316` | Delegate the dev→prod promotion script that removes the manual six-PR fan-out. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000317` | Security-sensitive change with no tests | SECURITY_TENANCY | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Manual dev/prod PR fan-out | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000319` | Self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Clicking approve on every open Medicodio PR in a batch | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Hand-diagnosing PE-integration state-machine violations from production symptoms | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000322` | Delegate a PE-integration status-transition contract test enumerating every `status` × `coding_mode` pair against `chk_ready_status_matches_coding_mode`. Accept | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Delegate the prompt-registry contract tests behind `#249`, open for 5 days. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Link `amit.p@medicodio.ai` to the GitHub account so delegation stops being invisible. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000325` | Content-free approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Approving and merging production promotions in seconds | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Re-creating the same change as a `prod_fix_issue` branch and PR | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | Hand-fixing column-visibility edge cases one at a time | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000329` | Delegate the column-visibility and export regression matrix for the Chart Queue and History tables — the same class of edge case has now been fixed twice by han | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Delegate generation of promotion PR bodies from the underlying dev PR, so a production change never arrives with an empty body. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000331` | Template-only body on a production promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000332` | Self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000333` | Client onboarding: create config, seed KB chart-field mappings, add payer-header variants | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000334` | Provider-specific payer-header variants added one at a time | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000335` | Delegate a client-onboarding scaffold generator with the two clients onboarded today as the acceptance fixtures. This is the highest-value repetitive-work remov | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Delegate a KB mapping validation test that fails when a newly onboarded client is missing a required chart-field mapping. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000337` | Self-merge with no review at all | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Template-only PR bodies | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000339` | Onboarding done by hand each time | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Reverting UI redesigns after they reach `Dev_1.0` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000341` | Delegate a visual-regression snapshot suite for the Prediction Trail stage rail so a UI change's effect is visible in the PR rather than after the fact. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | Commits under an unlinked author email | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000343` | Manually validating combination-code collapse against the KB table | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000344` | Delegate KB-table-driven combination-code fixtures so the I.B.9 collapse rule is verified per row rather than by inspection. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000345` | Delegate a triage pass over the 8 unanswered Devin Review comments on `#411`, producing accept/reject decisions. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Long-lived PR with unanswered Devin findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Draft PR left open across many days | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
