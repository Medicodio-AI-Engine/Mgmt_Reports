# Plan — proposed actions and stop conditions

**Run:** `RUN_0005` · **Report date:** 2026-08-28 · **Stage:** `03_PLAN` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## `ISSUE_000001` Low automation-adoption signal for SaijyotiMeti

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- INSUFFICIENT_EVIDENCE: rating data cannot justify a change
- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000049` Low automation-adoption signal for Pj-Vineeth-Kumar

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- INSUFFICIENT_EVIDENCE: rating data cannot justify a change
- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000130` Low automation-adoption signal for svh-medicodio

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- INSUFFICIENT_EVIDENCE: rating data cannot justify a change
- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000004` Low automation-adoption signal for sameer-s-mansur

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- INSUFFICIENT_EVIDENCE: rating data cannot justify a change
- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000050` Low automation-adoption signal for jatinkushwaha-medicodio

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- INSUFFICIENT_EVIDENCE: rating data cannot justify a change
- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000282` `docs(review-logs)` write-ups

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

## `ISSUE_000283` Backfilling function headers / doc comments

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

## `ISSUE_000284` Env-var documentation drift

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

## `ISSUE_000285` Use Devin to build a regression suite for the bundle signature/rollback engine, with the fail-open case he just fixed as the first test.

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

## `ISSUE_000286` Use Devin to generate the env-var documentation drift check as a CI gate.

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

## `ISSUE_000287` Use Devin to convert his `/check` finding list into a checked-in acceptance checklist for the next content-sync phase.

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

## `ISSUE_000288` Substantive review recorded in a commit, empty approval on GitHub

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

## `ISSUE_000289` Hand-written review logs

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

## `ISSUE_000290` `docs(review-log)` write-ups

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

## `ISSUE_000291` Being the org's only substantive reviewer

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

## `ISSUE_000292` Hand-fixing the same validation defect on two layers

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

## `ISSUE_000293` Use Devin to turn her review template into a repository skill/checklist so `okay`-style approvals have an alternative that costs less than writing 5,000 charact

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

## `ISSUE_000294` Use Devin to generate the shared-error-code contract tests between API and web.

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

## `ISSUE_000295` Use Devin to draft the review-log entries from the gate output.

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

## `ISSUE_000296` Review quality concentrated in one person

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

## `ISSUE_000297` Manual QA passes on `feat/qa-automation`

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

## `ISSUE_000298` Empty approvals

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

## `ISSUE_000299` Extend #1253's interaction matrix to the Document Checklist and file-number surfaces, which absorbed two hand-run QA cycles this week.

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

## `ISSUE_000300` Use Devin to convert the `qa update` PR bodies into executable e2e specs.

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

## `ISSUE_000301` Use Devin to wire the e2e suite into the gate so QA findings arrive before merge, not after.

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

## `ISSUE_000302` Low-information approval

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

## `ISSUE_000303` Manual `dev` merges into feature branches

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

## `ISSUE_000304` Filter/label UI changes applied per surface

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

## `ISSUE_000305` Use Devin to write regression tests for configurable file-number generation, including the collision → 409 path.

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

## `ISSUE_000306` Use Devin to split #1239 into reviewable slices so it can land.

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

## `ISSUE_000307` Use Devin to consolidate case-list filter behaviour into one tested component.

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

## `ISSUE_000308` Devin PR opened, then left without a reviewer

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

## `ISSUE_000309` Post-merge QA hardening passes

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

## `ISSUE_000310` Same defect class fixed surface-by-surface (URL state, focus restore)

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

## `ISSUE_000311` Hand-written review/gate logs

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

## `ISSUE_000312` Use Devin to generate an a11y + URL-state regression suite for the checklist surfaces.

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

## `ISSUE_000313` Use Devin to extract a single tested URL-state hook and migrate the call sites.

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

## `ISSUE_000314` Use Devin to run the pre-merge `/check` pass so the QA-fix PR becomes unnecessary.

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

## `ISSUE_000315` Feature lands, then a separate QA-hardening PR follows

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

## `ISSUE_000316` Promotion fan-out (`Dev_1.0` → `release/prod_1.0` cherry-pick PRs)

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000317` Empty approvals

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000318` Facility-day state semantics corrected in 13 successive PRs

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000319` Use Devin to generate a state-machine test suite for the facility-day states, seeded with the 13 defects fixed today — it would have caught most of them before 

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000320` Use Devin to write the promotion script that opens the `Dev_1.0`→prod cherry-pick PR with a filled body.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000321` Use Devin to answer the 5 open findings on #249 before it merges.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000322` Empty-bodied approvals

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000323` Behaviour changes to a production dashboard with no tests

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000324` Promotion fan-out

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000325` One-word approvals

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000326` `uat` → `release/prod_3.0` promotion PRs with template-only bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000327` Journey/attribution logic verified by reading output

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000328` Use Devin to build golden-file tests for `guidelines_journey` per-target attribution across the lanes he added (laterality, BMI/Z68, split, `excludes1`).

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000329` Use Devin to generate promotion PR bodies (included PRs, risk, rollback) from the diff.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000330` Land #405 by adding acceptance criteria and requesting review.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000331` One-word approvals

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000332` Promotion merged with an open Devin Review finding

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000333` Promotion fan-out

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000334` Batch/ledger invariants stated in prose then verified by hand

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000335` Template-only PR bodies on promotions

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000336` Use Devin to convert his written batch/ledger invariants into a regression suite (cached re-run, dual writers, event-driven vs RPA warning, blank insurance cate

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000337` Use Devin to script the three-stage promotion so the bodies are generated.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000338` Use Devin to write fixtures for the gender-resolution precedence rules he just shipped.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000339` Production batch-semantics changes with zero tests

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000340` Self-merge

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000341` Promotion fan-out with template bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000342` Same change authored twice across nodejs and react

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000343` UI style tweaks committed individually

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000344` Manual `Dev_1.0` sync into the feature branch

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000345` Use Devin to generate a regression suite for the encounter decrypt/patch path, asserting the age field and PHI masking.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000346` Use Devin to table-drive the login error-message contract across API and UI.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000347` Use Devin to produce the cross-repo API contract test so paired changes cannot drift.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000348` Self-merge

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000349` PHI-adjacent change with no tests

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000350` Client-config routing edits per specialty

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000351` Promotion PRs with template bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000352` Draft Devin PRs left idle

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000353` Use Devin to build KB-table-driven fixtures for the I.B.9 collapse redesign in #411, where 3 findings are currently open.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000354` Use Devin to validate client-config routing changes against a schema so podiatry-style exclusions cannot regress.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000355` Close out #393 or convert it into a scoped, reviewable PR.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000356` Rich feature bodies, template-only promotion bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000357` Devin draft opened then idle

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000358` Same-minute `uat`→prod promotion

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000359` Trigger-field corrections

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000360` Template-only PR bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000361` Use Devin to generate a routing-trigger fixture suite keyed on `type_of_service_id` / `type_of_visit_id`, so a field mismatch fails a test rather than a chart.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000362` Use Devin to write the P039-vs-P036 lab-source contract test that pins the refactor he just made.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000363` Use Devin to draft his promotion PR bodies.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000364` Promotion to `release/prod_3.0` within a minute of merge

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000365` Behaviour change to chart routing with no tests

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000366` Approving three-stage promotion chains

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000367` Empty approval bodies

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000368` Use Devin to generate a promotion checklist comment (diff summary, findings status, migration presence) so his approval has something concrete to confirm.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000369` Use Devin to script the `Dev_1.0`→`Uat_1.0`→prod chain into a single reviewed unit.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000370` Empty approvals on production promotions

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000371` Guideline-rule gating fixes verified by reading the rule

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000372` Use Devin to generate unit tests for the guideline-rule predicates (`match.present`, exclusion lanes) she has now corrected twice.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000373` Use Devin to answer Devin Review findings before merge rather than leaving them open.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000374` Merge with an open Devin Review finding

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000375` Same-minute prod promotion with template body

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000376` Use Devin to write BMI/Z68 gating fixtures across client configurations.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000377` Use Devin to generate the promotion body from the diff.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000378` Promotion opened and merged within minutes on a template body

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000379` Work accumulating on a draft branch without reaching review

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000380` Scope the ICD memory-manager agent as a Devin task with explicit acceptance criteria and requested tests.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.

## `ISSUE_000381` Use Devin to split #393 into a reviewable first slice.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000382` Work not reaching a reviewable state

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- TARGET_UNRESOLVED: confirm the repository before any implementation
- The item requires an organizational policy decision.
