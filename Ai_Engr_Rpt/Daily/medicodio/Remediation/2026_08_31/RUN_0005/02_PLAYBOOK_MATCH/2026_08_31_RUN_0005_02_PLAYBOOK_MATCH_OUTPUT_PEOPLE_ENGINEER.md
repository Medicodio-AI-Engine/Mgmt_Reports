# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-08-31 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000282` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000283` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000284` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000285` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000286` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000287` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000288` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000289` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000290` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000291` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000292` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000293` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000294` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000295` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000296` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000297` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000298` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000299` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000300` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000301` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000302` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000303` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000304` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000305` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000306` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000307` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000308` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000309` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000310` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000311` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000312` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000313` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000314` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000315` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000316` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000317` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |

## Escalated: no approved playbook matched

- `ISSUE_000302` Commits landing under an unlinked author identity
- `ISSUE_000306` Delegate recall-precision tests for the episodic memory feature in #393 before it is marked ready.
- `ISSUE_000312` Split the two open PRs' remaining work into scoped follow-ups with acceptance criteria written from the bot findings.
- `ISSUE_000313` Commits landing under an unlinked email

These need either human direction or a new approved playbook.
