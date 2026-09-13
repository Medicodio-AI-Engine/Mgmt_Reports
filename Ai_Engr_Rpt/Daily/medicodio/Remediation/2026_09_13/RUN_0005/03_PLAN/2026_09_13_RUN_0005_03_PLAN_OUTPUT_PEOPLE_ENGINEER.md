# Plan — proposed actions and stop conditions

**Run:** `RUN_0005` · **Report date:** 2026-09-13 · **Stage:** `03_PLAN` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## `ISSUE_000282` Hand-fixing another member's findings, then approving and merging

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000283` `docs(review-logs)` commits written by hand

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000284` Re-running the 37-gate matrix and transcribing results into prose

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000285` Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`, 

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Identify the defect class and the exact behavior that must not regress.
2. Locate the existing test suite and the closest existing tests for that surface.
3. Write the smallest test that fails against the current behavior when the defect is present.
4. Run the new test and record the pre-fix result.
5. Run the targeted suite for the touched module.
6. Run the broader suite for the package.
7. Record every command and its output as evidence.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: test.write_regression_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Test framework cannot be identified.
- CI or local test execution is unavailable in the target repository.
- The behavior under test touches authentication, authorization, tenancy, PHI, secrets, or billing.

## `ISSUE_000286` Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000287` Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch.

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000288` Reviewer remediates, approves, then merges

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000289` Merged over the approver's own written blocker

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000290` Post-merge QA-gate verdict unactioned in-window

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000291` Ad-hoc per-component timestamp formatting

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000292` Branch carried without a PR

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000293` Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Identify the defect class and the exact behavior that must not regress.
2. Locate the existing test suite and the closest existing tests for that surface.
3. Write the smallest test that fails against the current behavior when the defect is present.
4. Run the new test and record the pre-fix result.
5. Run the targeted suite for the touched module.
6. Run the broader suite for the package.
7. Record every command and its output as evidence.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: test.write_regression_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Test framework cannot be identified.
- CI or local test execution is unavailable in the target repository.
- The behavior under test touches authentication, authorization, tenancy, PHI, secrets, or billing.

## `ISSUE_000294` Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real).

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000295` Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work.

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000296` Work carried on a branch with no PR

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000297` Large single PR (73 files) awaiting a human reviewer

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000298` Author absent while another member remediates and merges his PR

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000299` Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR.

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000300` Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000301` Decision items on his PRs resolved without him

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000302` PR-description accuracy

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.
