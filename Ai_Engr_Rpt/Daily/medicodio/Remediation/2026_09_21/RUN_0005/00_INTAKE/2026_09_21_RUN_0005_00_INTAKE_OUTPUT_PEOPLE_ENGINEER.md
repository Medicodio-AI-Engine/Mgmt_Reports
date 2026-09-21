# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-21 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_21_Employee_Rating_Cards.md, 2026_09_21_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_064 | EMPLOYEE_RATING_CARDS | `2026_09_21_Employee_Rating_Cards.md` | no |
| SOURCE_065 | DAILY_ENGINEERING_DETAIL | `2026_09_21_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Workflow/infra change merged without a dry run of its own verification path | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000283` | Findings left undispositioned on open PRs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Findings undispositioned | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Infra change lands without exercising its own verification path | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | 0-char approvals followed by immediate merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Empty approvals | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Branch protection not enabled (as EM) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Carried: review-log / atlas / header-relocation commits by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | (Carried) Run the QA gate on the PR head before approval. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Reviewer remediates, approves, merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | QA verdict consumed after merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Carried: oversized single PR (`#1310`, `#1322`, `#1391`) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | (Carried) Devin drafts §12.4/§12.5 measurement PR. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | (Carried) One Devin PR per major #5–#11. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Author's findings dispositioned by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Manual upstream fork sync (`paperclip-ai`) | MECHANICAL_MIGRATION | paperclip-ai | — | — | — | CODE_CHANGE |
| `ISSUE_000302` | (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork. | PROCESS_PRACTICE | paperclip-ai | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Large invoicing PRs with badge-only bodies (`#652`/`#578`) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
