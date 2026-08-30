# Playbook match and capability check

**Run:** `RUN_0005` · **Report date:** 2026-08-29 · **Stage:** `02_PLAYBOOK_MATCH` · **Status:** PARTIAL_SOURCE_DATA

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_MISMATCH: filename date and stated review date disagree; artifact excluded from automatic processing
- PARTIAL: missing DAILY_ENGINEERING_DETAIL; run continues in analysis-only mode with reduced confidence

| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |
| ----- | -------- | ----- | ------ | ---------- | -------------------- |
| `ISSUE_000002` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000049` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000003` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000282` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000283` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000284` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000285` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000286` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 77 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000287` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000288` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000289` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000290` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000291` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000292` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000293` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000294` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000295` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000296` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000297` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000298` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000299` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000300` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000301` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000302` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000303` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000304` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000305` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000306` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000307` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000308` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000309` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000310` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000311` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000312` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000313` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000314` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000315` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000316` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000317` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000318` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000319` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000320` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000321` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000322` | ORG_PB_REGRESSION_TEST_GENERATION | ORG | ORG_PLAYBOOK | 65 | test.write_regression_test, ci.run_targeted_tests |
| `ISSUE_000323` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000324` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000325` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000326` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000327` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000328` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000329` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000330` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000331` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000332` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000333` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000334` | ORG_PB_QA_VALIDATION | ORG | ORG_PLAYBOOK | 65 | qa.execute_cases, ci.run_targeted_tests |
| `ISSUE_000335` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000336` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000337` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000338` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000339` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000340` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000341` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000342` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000343` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000344` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000345` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000346` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000347` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000348` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000349` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000350` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000351` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000352` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000353` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000354` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000355` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000356` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000357` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000358` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000359` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000360` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000361` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000362` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000363` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000364` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000365` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000366` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000367` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000368` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000369` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000370` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000371` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000372` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000373` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000374` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000375` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000376` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000377` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000378` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 72 | none |
| `ISSUE_000379` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 84 | none |
| `ISSUE_000380` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000381` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000382` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000383` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000384` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000385` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000386` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000387` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000388` | — | — | NO_MATCH | 0 | none |
| `ISSUE_000389` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000390` | GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL | GENERAL | GENERAL_PLAYBOOK | 60 | none |
| `ISSUE_000391` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |
| `ISSUE_000392` | ORG_PB_MECHANICAL_MIGRATION | ORG | ORG_PLAYBOOK | 77 | repo.multi_file_edit, git.stacked_branches, ci.run_targeted_tests |

## Escalated: no approved playbook matched

- `ISSUE_000293` Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by noth
- `ISSUE_000343` Per-facility QA re-baseline after each merge or model change
- `ISSUE_000346` Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one
- `ISSUE_000347` Delegate the QA re-baseline harness so a model bump costs one run, not a day.
- `ISSUE_000350` A large feature branch that does not land
- `ISSUE_000359` Manual `Dev_1.0` sync merges
- `ISSUE_000361` Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open).
- `ISSUE_000364` Production-path changes with no tests
- `ISSUE_000375` Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return.
- `ISSUE_000387` Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable.
- `ISSUE_000388` Delegate the split of his three commits into a reviewable PR with a body describing the recall contract.

These need either human direction or a new approved playbook.
