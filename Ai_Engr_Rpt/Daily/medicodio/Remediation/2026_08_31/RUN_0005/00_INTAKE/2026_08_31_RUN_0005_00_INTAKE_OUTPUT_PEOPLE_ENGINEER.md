# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-08-31 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_08_31_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_08_31_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Re-checking whether an open PR has picked up a human reviewer | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | QA-driven field-level fixes shipped as one "qa update" PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000284` | Delegate a test matrix for the extraction allow-list empty-field handling in #1259 — bounded, data-driven, exactly the shape Devin lands well. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000285` | Delegate a stale-PR / unreviewed-PR report as a scheduled job, extending the CI automation he already built. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Open PR with bot review only and no human reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Enforcing a state-based guard surface by surface | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Delegate the closed/archived read-only enforcement matrix covering every mutating endpoint and UI control. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Delegate backfill tests for the guard's negative cases (open cases must remain editable) to prevent an over-broad guard. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000290` | PR opened late on Friday with bot review only | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | No observable Devin leverage | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Lookup/searchability fixes on displayed identifiers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | Delegate search-parity regression tests: for every identifier rendered in the UI, assert it is queryable through the shared search platform. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Delegate the PR-preparation pass (description, gates, screenshots) on his large PRs, which have previously landed with thin bodies. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000295` | Open PR with bot review only | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Accumulating a multi-phase feature on one branch before opening a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Writing subscriber/notification wiring per skill by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Delegate the subscriber/notification test matrix for the AI Case Manager skill registry — the phases most likely to hide a wiring bug. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000299` | Delegate the AI-skill registry contract tests so a new skill cannot register incorrectly. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Open the branch as a draft PR and let Devin Review run per phase, rather than one large review at the end. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Large feature landed as a single PR instead of a reviewable series | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000302` | Commits landing under an unlinked author identity | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Leaving a draft PR open across days with no review surface | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000304` | KB-table-driven rule redesigns verified by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | Delegate per-row fixtures for the I.B.9 collapse rules, generated from the KB table. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000306` | Delegate recall-precision tests for the episodic memory feature in #393 before it is marked ready. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000307` | Devin/engine draft PRs left open for days | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Re-running the same Devin Review cycle on one PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Prompt/flag registry plumbing per integration | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000310` | Delegate prompt-registry contract tests (every registered prompt resolves, has required variables, and fails loudly when missing). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | Delegate the insurance-created-flag propagation tests across the integration boundary in #248. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Split the two open PRs' remaining work into scoped follow-ups with acceptance criteria written from the bot findings. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000313` | Commits landing under an unlinked email | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Bot-review-only PRs left open for days | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | A long-lived exploratory PR with a non-descriptive title | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000316` | If the ortho work is still wanted, delegate it as a scoped session with written acceptance criteria; otherwise close #382. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Non-descriptive engine PR titles/bodies | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
