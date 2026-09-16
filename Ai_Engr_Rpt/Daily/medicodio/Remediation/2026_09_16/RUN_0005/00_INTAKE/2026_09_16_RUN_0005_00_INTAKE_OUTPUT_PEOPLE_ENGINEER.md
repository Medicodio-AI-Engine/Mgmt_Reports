# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-16 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_16_Employee_Rating_Cards.md, 2026_09_16_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_16_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_16_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | `docs(review-logs)` commits recording gate runs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Manual 42-gate run + hand-typed verdict table | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Delegate the §4.4 data-correction script with explicit ACs (three counts on UAT/prod, idempotent, behind the schema-approval gate) — the missing artefact his ow | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Devin session to add a pre-push test run for the specs touched by a branch (he noted the hook "does not run tests, which is exactly where two of the four blocke | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Merge over his own written blocker | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Hand-written review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Promotion PRs with bodies `uat update` / `main update` | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000289` | Bulk-closing Devin QA/fix PRs | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | `act()`/jest housekeeping | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Release-manifest generator for dev→uat→main PRs (commits, PRs, open QA findings) so an empty-body approval is at least approving something legible. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | A `dev` CI job that builds every `Dockerfile.` (the hook added in `#1382` only catches undeclared imports). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Re-open or re-delegate the fixes from `#1369`/`#1371` with the QA findings as ACs. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Promotion PRs with no body, empty approvals | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000295` | Remediate a peer's PR, then approve and merge it yourself | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Repointing deep links / agent tools after route retirements | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000297` | Dark-mode token adjustments | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Split `#1380` into a reviewable stack; ask Devin to run `nx test`/`typecheck` per layer and report. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000299` | Regression e2e for the retired `/hr/pipeline` links (every consumer that was repointed). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Close or hand `#1365` to a reviewer — a Devin PR nobody owns is negative leverage. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Oversized PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000302` | Devin PR with no reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | PRD add + reconcile commit with each feature branch | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000304` | Fixture-type fixes after payload changes | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | e2e + unit coverage for attach-to-step and `completeStepOnSatisfy` before the PR opens. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Delegate the `#1372` C-1..C-4 answers as an investigation with the four config keys as ACs. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | (none meeting the four-part test today) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Empty approvals on promotion PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Prod hotfix after promotion | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000310` | CI job building all `Dockerfile.` on `dev`/`uat` before promotion. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000311` | Fix the red `formatDayLabel` spec (deterministic month abbreviations) — scoped, test-verifiable. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Empty approvals on 500+-file promotions | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000313` | — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | If `#1360` is still needed, re-scope it as a Devin task with the orphan-checklist audit count as the AC. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Fix-after-Devin-finding commits on validators/coercion | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000316` | Open → approve → merge within 1–3 min | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Regression tests for batch-run creation (`retry_of`, null/zero coercion, import find-or-create bypass). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Excel export snapshot tests (header dedupe). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | Merge within minutes of opening, empty approval | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Empty approve + merge of Jatin's PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Ask Devin Review for a per-PR "reviewer checklist" digest and paste the checked items into the approval. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Long-lived branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Test fixtures for inpatient charts (empty text, disputed body part). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000325` | `feat/inpatient-engine` without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | PRs to `uat` with no human reviewer | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000327` | Unit tests for the scope-list validator and the guideline loader. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | `uat`-targeted PR without reviewer | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
