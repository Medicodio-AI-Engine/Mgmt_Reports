# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-09-04 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000282` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000283` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000284` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000285` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 89 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000286` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000287` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000288` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000289` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000290` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000291` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000292` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000293` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000294` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000295` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000296` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000297` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000298` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000299` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000300` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000301` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000302` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000303` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000304` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000305` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000306` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000307` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000308` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000309` | ORG_PB_TENANT_ISOLATION_VALIDATION | ORG | ORG_PLAYBOOK | 89 | security.read_tenancy_model, test.write_isolation_test, qa.execute_cases |
| `ISSUE_000310` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000311` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000312` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000313` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000314` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000315` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000316` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000317` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000318` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000319` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000320` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000321` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000322` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000323` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000324` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000325` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000326` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000327` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000328` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000329` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000330` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000331` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000332` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000333` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000334` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000335` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000336` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000337` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000338` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000339` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000340` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000341` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000117` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000342` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000343` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000344` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000345` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000346` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000347` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000348` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000349` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000350` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000351` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000352` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000353` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000354` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000355` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000356` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000357` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000358` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000359` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000360` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000361` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000362` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000363` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000364` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000365` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000366` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000367` | — | — | NO_MATCH | 0 | none |

## Escalated: no approved playbook matched

- `ISSUE_000300` Delegate a persona-credential preflight that runs before every gate and posts one org-admin blocker instead of five identical no-verdict comments.
- `ISSUE_000335` Parallel nodejs + react commits for the same change
- `ISSUE_000338` Delegate a coder-performance dedupe regression test (the bug he fixed today).
- `ISSUE_000341` Promotion PRs with badge-only bodies
- `ISSUE_000342` Delegate the promotion-body generator for `#608`/`#536`.
- `ISSUE_000346` Badge-only promotion bodies
- `ISSUE_000347` KB dataset loader + page pairs (`kb-asc`, earlier `invoicing-billing-suite`)
- `ISSUE_000351` `okay` approval + merge + immediate prod promotion
- `ISSUE_000353` Badge-only body on a prod promotion
- `ISSUE_000356` Delegate answering the 14 open findings before the next promotion.
- `ISSUE_000357` Template/badge-only body on prod promotion
- `ISSUE_000359` Delegate the regression test over the 821 parents he counted.
- `ISSUE_000362` Template body on prod promotion
- `ISSUE_000366` Same-day `Dev → Uat → prod` promotion with badge bodies
- `ISSUE_000367` Delegate golden-file tests for the `others` parser and the Trinity/PPV parsers named 09-03.

These need either human direction or a new approved playbook.
