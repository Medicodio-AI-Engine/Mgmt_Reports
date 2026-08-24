# Intake — normalized findings

**Run:** `RUN_0001` · **Report date:** 2026-08-23 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_002 | EMPLOYEE_RATING_CARDS | `employee-rating-cards-2026-08-23.md` | yes |
| SOURCE_003 | DAILY_ENGINEERING_DETAIL | `mgmt-activity-report-2026-08-23.md` | yes |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000001` | Low automation-adoption signal for SaijyotiMeti | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000002` | Low automation-adoption signal for akanksh-rv | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000003` | Low automation-adoption signal for Amrutha-Beedikar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000004` | Low automation-adoption signal for sameer-s-mansur | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000005` | Low automation-adoption signal for anirudh-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000006` | Low automation-adoption signal for hitesh | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000007` | CI has no successful runs in globalcodio-monorepo | CI_FAILURE | globalcodio-monorepo | — | — | — | UNKNOWN |
| `ISSUE_000008` | Hand-writing `docs/review-logs/` gate + review logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000009` | Merging `origin/dev` into each feature branch by hand | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000010` | Composing the Architect+EM review skeleton (verdict, lenses, nit list) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000011` | Use Devin to generate a regression suite for the AI Case Manager send-path defect class (#1210's "reviewed draft discarded on send", #1213's email header, #1215 | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000012` | Use Devin to emit the review-log artifact from the existing `/check` + `/fix` output, replacing the hand-written `docs/review-logs/` commits. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000013` | Use Devin to split feature branches over ~100 files into stacked, individually reviewable PRs before review starts (#1212 was 140 files). | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000014` | Hand-written review/audit logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000015` | Very large single-PR diffs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000016` | `dev → feat/qa-automation` promotion/sync PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000017` | Post-merge QA audit of already-merged feature work | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000018` | Filling (or not filling) the PR template by hand | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000019` | Use Devin for the recurring `dev → feat/qa-automation` sync plus its QA audit — mechanical, repeats every few days, and currently bypasses review entirely. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000020` | Use Devin to finish landing #1208 (the notes-visibility feature it authored): #1209's remediation is merged into the branch, so the remaining work is bounded. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000021` | Use Devin to generate the live authenticated API validation he explicitly skipped on #1214, as a repeatable harness rather than a per-run manual pass. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000022` | Promotion/sync PR self-merged without independent review | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000023` | Unfilled PR-template bodies | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000024` | `/check` → `/fix` blocker clearing before review | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000025` | Writing the standards/review log by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000026` | Syncing `origin/dev` into the feature branch | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000027` | Use Devin to generate regression tests for the email-header / platform-field contract so the case_number behavior cannot silently regress (this surface changed  | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000028` | Use Devin for the pre-merge `/check`+`/fix` blocker pass on her branches, so her time goes to the domain decision rather than the standards sweep. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000029` | Late-night test/doc top-ups on a long-lived shared branch | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000030` | Merging without a recorded human review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000031` | Use Devin to build the portal access-control test matrix (roles × account statuses) — bounded, high-value on a security surface, and it removes the late-night m | SECURITY_TENANCY | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000032` | Use Devin to split #1183-class branches (150 files, open 5 days) into stacked reviewable PRs. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000033` | Merges without an independent human review record | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000034` | Manually re-running batch/dev runs to verify a guard | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000035` | Self-merging integration PRs within minutes | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000036` | Non-conventional commit subjects | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000037` | Use Devin to build a repeatable integration verification harness for the lock-key / attach-form workflows, replacing the hand-run dev runs he re-does each time. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000038` | Use Devin to write regression tests for Elaris filename pairing (63 files landed with no human review and 3 open Devin Review findings). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000039` | Integration changes landing with no independent review | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000040` | Re-plumbing `version_number` through KB create/read paths, one surface at a time | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000041` | Mirroring every KB wizard change across backend and UI by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000042` | Carrying 130/226-file branches for days, then replacing the PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000043` | Use Devin to generate a KB guideline wizard regression suite (General / Specialty / Specialty-Payer / Client-Payer scopes) so a versioning reversal of this size | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000044` | Use Devin to carve the KB branches into landable PRs (schema/API, then UI, then wizard UX) instead of one 130-file backend branch plus one 226-file UI branch. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000045` | Use Devin for the paired backend/UI propagation of each KB contract change. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000046` | Very large, long-lived unmerged branches | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000047` | Commit identity not linked to a GitHub account | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
