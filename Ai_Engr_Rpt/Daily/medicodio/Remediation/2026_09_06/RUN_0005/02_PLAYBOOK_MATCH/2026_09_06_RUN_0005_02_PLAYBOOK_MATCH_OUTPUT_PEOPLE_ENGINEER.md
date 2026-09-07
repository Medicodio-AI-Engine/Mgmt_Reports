# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-09-06 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000282` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000283` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000284` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000285` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000286` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000287` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000288` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000289` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000290` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 89 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000291` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000292` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000293` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000294` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000295` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000296` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000297` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000298` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000299` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 89 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000300` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000301` | ORG_PB_TENANT_ISOLATION_VALIDATION | ORG | ORG_PLAYBOOK | 89 | security.read_tenancy_model, test.write_isolation_test, qa.execute_cases |

## Escalated: no approved playbook matched

- `ISSUE_000297` Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t

These need either human direction or a new approved playbook.
