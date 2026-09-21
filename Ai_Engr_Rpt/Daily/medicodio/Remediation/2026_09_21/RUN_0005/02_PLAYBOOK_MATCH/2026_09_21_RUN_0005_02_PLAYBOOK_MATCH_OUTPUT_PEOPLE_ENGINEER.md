# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-09-21 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_21_Employee_Rating_Cards.md, 2026_09_21_Mgmt_Activity_Report.md; dated by filename only, no stated review date

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000282` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000283` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000284` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000285` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000286` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000287` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000288` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000289` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000290` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000291` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000292` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000293` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000294` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000295` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000296` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000297` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000298` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000299` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000300` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000301` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000302` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000303` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |

## Escalated: no approved playbook matched

- `ISSUE_000284` Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a
- `ISSUE_000289` Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a

These need either human direction or a new approved playbook.
