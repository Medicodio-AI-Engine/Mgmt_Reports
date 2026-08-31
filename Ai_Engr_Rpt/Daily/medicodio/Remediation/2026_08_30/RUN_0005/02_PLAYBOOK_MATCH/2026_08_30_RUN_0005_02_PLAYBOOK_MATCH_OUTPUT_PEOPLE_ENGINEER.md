# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-08-30 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000002` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000282` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000283` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000284` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000285` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000286` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000287` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000288` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000289` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000290` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000291` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000292` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000293` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000294` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000295` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000296` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000297` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000298` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000299` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000300` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000301` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000302` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000303` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000304` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000305` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000306` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000307` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000308` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000309` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000310` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000311` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000312` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000313` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000314` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |

## Escalated: no approved playbook matched

- `ISSUE_000285` Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and o
- `ISSUE_000301` Hand-writing per-phase tests unevenly (3 of 8 commits)
- `ISSUE_000302` Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Revie

These need either human direction or a new approved playbook.
