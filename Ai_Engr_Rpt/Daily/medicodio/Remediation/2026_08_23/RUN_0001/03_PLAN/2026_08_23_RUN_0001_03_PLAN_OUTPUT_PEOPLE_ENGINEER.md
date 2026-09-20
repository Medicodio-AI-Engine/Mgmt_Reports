# Plan — proposed actions and stop conditions

**Run:** `RUN_0001` · **Report date:** 2026-08-23 · **Stage:** `03_PLAN` · **Status:** OK

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

## `ISSUE_000002` Low automation-adoption signal for akanksh-rv

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

## `ISSUE_000003` Low automation-adoption signal for Amrutha-Beedikar

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

## `ISSUE_000005` Low automation-adoption signal for anirudh-medicodio

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

## `ISSUE_000006` Low automation-adoption signal for hitesh

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

## `ISSUE_000007` CI has no successful runs in globalcodio-monorepo

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

- ENVIRONMENT_NOT_VERIFIED: confirm the failure is infrastructure, not a code defect
- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- The item requires an organizational policy decision.

## `ISSUE_000008` Hand-writing `docs/review-logs/` gate + review logs

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

## `ISSUE_000009` Merging `origin/dev` into each feature branch by hand

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

## `ISSUE_000010` Composing the Architect+EM review skeleton (verdict, lenses, nit list)

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

## `ISSUE_000011` Use Devin to generate a regression suite for the AI Case Manager send-path defect class (#1210's "reviewed draft discarded on send", #1213's email header, #1215

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

## `ISSUE_000012` Use Devin to emit the review-log artifact from the existing `/check` + `/fix` output, replacing the hand-written `docs/review-logs/` commits.

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

## `ISSUE_000013` Use Devin to split feature branches over ~100 files into stacked, individually reviewable PRs before review starts (#1212 was 140 files).

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

## `ISSUE_000014` Hand-written review/audit logs

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

## `ISSUE_000015` Very large single-PR diffs

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

## `ISSUE_000016` `dev → feat/qa-automation` promotion/sync PRs

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

## `ISSUE_000017` Post-merge QA audit of already-merged feature work

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

## `ISSUE_000018` Filling (or not filling) the PR template by hand

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

## `ISSUE_000019` Use Devin for the recurring `dev → feat/qa-automation` sync plus its QA audit — mechanical, repeats every few days, and currently bypasses review entirely.

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

## `ISSUE_000020` Use Devin to finish landing #1208 (the notes-visibility feature it authored): #1209's remediation is merged into the branch, so the remaining work is bounded.

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

## `ISSUE_000021` Use Devin to generate the live authenticated API validation he explicitly skipped on #1214, as a repeatable harness rather than a per-run manual pass.

- Repository: globalcodio-monorepo
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000022` Promotion/sync PR self-merged without independent review

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

## `ISSUE_000023` Unfilled PR-template bodies

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

## `ISSUE_000024` `/check` → `/fix` blocker clearing before review

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

## `ISSUE_000025` Writing the standards/review log by hand

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

## `ISSUE_000026` Syncing `origin/dev` into the feature branch

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

## `ISSUE_000027` Use Devin to generate regression tests for the email-header / platform-field contract so the case_number behavior cannot silently regress (this surface changed 

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

## `ISSUE_000028` Use Devin for the pre-merge `/check`+`/fix` blocker pass on her branches, so her time goes to the domain decision rather than the standards sweep.

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

## `ISSUE_000029` Late-night test/doc top-ups on a long-lived shared branch

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

## `ISSUE_000030` Merging without a recorded human review

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

## `ISSUE_000031` Use Devin to build the portal access-control test matrix (roles × account statuses) — bounded, high-value on a security surface, and it removes the late-night m

- Repository: globalcodio-monorepo
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000032` Use Devin to split #1183-class branches (150 files, open 5 days) into stacked reviewable PRs.

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

## `ISSUE_000033` Merges without an independent human review record

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

## `ISSUE_000034` Manually re-running batch/dev runs to verify a guard

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
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
- MISSING_CAPABILITY: test.write_regression_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Test framework cannot be identified.
- CI or local test execution is unavailable in the target repository.
- The behavior under test touches authentication, authorization, tenancy, PHI, secrets, or billing.

## `ISSUE_000035` Self-merging integration PRs within minutes

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- The item requires an organizational policy decision.

## `ISSUE_000036` Non-conventional commit subjects

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- The item requires an organizational policy decision.

## `ISSUE_000037` Use Devin to build a repeatable integration verification harness for the lock-key / attach-form workflows, replacing the hand-run dev runs he re-does each time.

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
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
- MISSING_CAPABILITY: test.write_regression_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Test framework cannot be identified.
- CI or local test execution is unavailable in the target repository.
- The behavior under test touches authentication, authorization, tenancy, PHI, secrets, or billing.

## `ISSUE_000038` Use Devin to write regression tests for Elaris filename pairing (63 files landed with no human review and 3 open Devin Review findings).

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
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
- MISSING_CAPABILITY: test.write_regression_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Test framework cannot be identified.
- CI or local test execution is unavailable in the target repository.
- The behavior under test touches authentication, authorization, tenancy, PHI, secrets, or billing.

## `ISSUE_000039` Integration changes landing with no independent review

- Repository: medicodio-nextgen-integration
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Restate the reported pattern with its evidence and frequency.
2. Identify whether the remedy is process, tooling, or code.
3. Describe the smallest concrete improvement and who owns it.
4. Produce the proposal for human decision; make no repository change.

**Stop conditions**

- The item requires an organizational policy decision.

## `ISSUE_000040` Re-plumbing `version_number` through KB create/read paths, one surface at a time

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

## `ISSUE_000041` Mirroring every KB wizard change across backend and UI by hand

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

## `ISSUE_000042` Carrying 130/226-file branches for days, then replacing the PR

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

## `ISSUE_000043` Use Devin to generate a KB guideline wizard regression suite (General / Specialty / Specialty-Payer / Client-Payer scopes) so a versioning reversal of this size

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000044` Use Devin to carve the KB branches into landable PRs (schema/API, then UI, then wizard UX) instead of one 130-file backend branch plus one 226-file UI branch.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000045` Use Devin for the paired backend/UI propagation of each KB contract change.

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

## `ISSUE_000046` Very large, long-lived unmerged branches

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

## `ISSUE_000047` Commit identity not linked to a GitHub account

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook
