# Plan — proposed actions and stop conditions

**Run:** `RUN_0005` · **Report date:** 2026-09-03 · **Stage:** `03_PLAN` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## `ISSUE_000282` Hand-written `docs(review)` logs

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

## `ISSUE_000283` Same-class date/timezone fixes across call sites

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

## `ISSUE_000284` Remediating another author's branch before approving it

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

## `ISSUE_000285` Ask Devin to enumerate every `formatDate`/`formatExpiryDate`/`parseDateValue` caller and generate a west-of-UTC regression test per caller; today's three separa

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

## `ISSUE_000286` Delegate the `docs/review-logs/` skeleton from gate output so the human writes only the judgement.

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

## `ISSUE_000287` Have Devin split `#1305` into stackable PRs (schema, service, UI) before a human reviews 105 files.

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

## `ISSUE_000288` Reviewer remediates then approves own remediation

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

## `ISSUE_000290` Very large single PR

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

## `ISSUE_000291` `dev → uat → main` promotion PRs with template-only bodies

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

## `ISSUE_000292` Content-sync decode/dependency fixes one per commit

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

## `ISSUE_000293` Remediating others' PRs (`#1257`) then approving

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

## `ISSUE_000294` Delegate the content-sync bundle-corpus test suite (non-mocked) — fourth report naming it.

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

## `ISSUE_000295` Delegate the `importSession` infinite-spinner fix from the NOT READY report; it is a scoped UI defect with a written reproduction.

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

## `ISSUE_000296` Have the promotion PR body generated from `git log dev..uat` plus the latest gate verdicts so the approver sees what is being promoted.

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

## `ISSUE_000297` Empty approvals incl. production

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

## `ISSUE_000298` Content-sync defects on mocked tests

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

## `ISSUE_000299` QA verdict ignored on promotion

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

## `ISSUE_000300` QA gates failing on environment before testing

- Repository: globalcodio-monorepo
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000301` Empty approvals on promotions

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

## `ISSUE_000302` Remediating another author's branch

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

## `ISSUE_000303` Pre-flight credential check that fails fast and pings the owner instead of running a full gate to "no verdict".

- Repository: globalcodio-monorepo
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000304` Emit a machine-readable verdict as a commit status on `dev` so `dev → uat` cannot merge with NOT READY outstanding.

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

## `ISSUE_000305` Delegate resolving the `#1282` verdict disagreement (hosted-dev vs Claude run) into a single recorded decision.

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

## `ISSUE_000306` Empty approvals incl. prod

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

## `ISSUE_000307` Gate cost with no verdict

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

## `ISSUE_000308` Feature PRs remediated by others before merge

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

## `ISSUE_000309` Devin docs PRs reviewed only by Devin

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

## `ISSUE_000310` Delegate the backend enforcement of the ISO-3166 rule (`persons.dto.ts`) plus a migration audit of non-canonical stored values — bounded, well specified by the 

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

## `ISSUE_000311` Ask Devin for the regression tests before opening the next validation PR rather than after the reviewer writes them.

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

## `ISSUE_000312` Devin-reviews-Devin loop

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

## `ISSUE_000313` Own PRs landed by others' remediation

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

## `ISSUE_000314` Post-merge fix-up PR for QA findings

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

## `ISSUE_000315` Delegate a BullMQ retry-path test that asserts a transient blob/Gemini failure is retried, not permanently failed.

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

## `ISSUE_000316` Delegate the hosted-dev manual verification checklist for the extraction UI once personas are restored.

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

## `ISSUE_000317` None with history

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

## `ISSUE_000318` Multi-day accumulation → single ≥ 100-file PR

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

## `ISSUE_000319` Manual QA routine comments

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

## `ISSUE_000320` Let Devin generate the tenancy/IDOR/RBAC probes for letter groups from the `#1306` body before human review.

- Repository: globalcodio-monorepo
- Autonomy tier: **D** (no execution)
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Read and document the current tenancy/authorization model from the code as it exists.
2. Identify the boundary the report claims may be violated.
3. Write read-only tests that assert cross-tenant access is denied.
4. Execute the tests and record results.
5. Produce a written finding with evidence and a proposed change for human decision.

**Stop conditions**

- HUMAN_OWNED_SURFACE: TENANT_ISOLATION semantics require a human decision
- OUT_OF_PILOT_SCOPE: widening the pilot is a human decision
- MISSING_CAPABILITY: security.read_tenancy_model: Engineering repositories are not checked out in the pilot.
- MISSING_CAPABILITY: test.write_isolation_test: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- NO_REPRODUCTION: playbook requires a verified reproduction first
- Any remediation would alter isolation or authorization semantics.
- The finding cannot be verified without production access.

## `ISSUE_000321` Split `#1306` (schema, platform admin, case-manager UI, AI drafting) with Devin doing the mechanical separation.

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

## `ISSUE_000322` One huge PR per feature

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

## `ISSUE_000323` Template-only PR body on large PRs

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

## `ISSUE_000324` Draft the `#1284` PR body (Why / schema / UI sections) from the diff so reviewers can start.

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

## `ISSUE_000325` Answer or triage the 17 open Devin findings.

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

## `ISSUE_000326` Unlanded feature branch

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

## `ISSUE_000327` Template-only body

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

## `ISSUE_000328` One-word promotion approval

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

## `ISSUE_000329` Regression test across every `MergeDataBuilder` token source so the next opt-in feature cannot miss the send path.

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

## `ISSUE_000330` One-word approval on promotion

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

## `ISSUE_000331` Empty approvals on every PR incl. prod

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

## `ISSUE_000332` Template-only PR bodies

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

## `ISSUE_000333` A PR-body generator invoked on open for `Dev_1.0` PRs.

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

## `ISSUE_000334` A Devin check that lists Devin Review findings still open at approval time in the approval dialog.

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

## `ISSUE_000335` Empty approvals

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

## `ISSUE_000336` Devin findings unanswered before promotion

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000337` One-word approvals

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

## `ISSUE_000338` Self-merge on `Dev_1.0`

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

## `ISSUE_000339` Analytics config contract test (BE default ↔ FE fail-closed).

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

## `ISSUE_000340` Extend `#528`'s pattern to the remaining untested components — Devin can enumerate components without specs.

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

## `ISSUE_000341` Self-merge

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

## `ISSUE_000342` One-word approvals

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

## `ISSUE_000343` Per-facility prompt/mapping edits shipped to prod same day

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

## `ISSUE_000344` Golden-file regression suite for Trinity/PPV parsing.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000345` PR body generation from commit messages (which are already descriptive).

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

## `ISSUE_000346` Template-only bodies

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

## `ISSUE_000347` Prompt changes to prod with 0 tests

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

## `ISSUE_000348` `okay` approvals on prod/feature merges

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

## `ISSUE_000349` Not a Devin task: a release checklist. Devin could generate the per-chart fixture set for the gate-threshold fix.

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

## `ISSUE_000350` `okay` approvals

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

## `ISSUE_000351` Per-chart fixtures for the gate-threshold logic; the bug class ("global instead of per chart") is testable.

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

## `ISSUE_000352` Template-only body

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

## `ISSUE_000353` None observed in-window

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

## `ISSUE_000354` Threshold-table test for every E/M band so the "14 minutes early, one unit high" class cannot recur.

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

## `ISSUE_000355` None with history

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
