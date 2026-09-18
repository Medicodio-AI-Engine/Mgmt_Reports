# Plan — proposed actions and stop conditions

**Run:** `RUN_0005` · **Report date:** 2026-09-18 · **Stage:** `03_PLAN` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_18_Employee_Rating_Cards.md, 2026_09_18_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## `ISSUE_000282` `docs(review-logs): close … with the real gate matrix`

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

## `ISSUE_000283` Filing CLEANUP-xxx items by hand

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

## `ISSUE_000284` Test-mock repair after schema/catalog change (12 commits)

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

## `ISSUE_000285` Delegate the review-log / gate-matrix closing commit: input = CI run URL + QA report path, output = the log section. Removes ~3 manual commits/day.

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

## `ISSUE_000286` Ask Devin for a mock-consistency sweep whenever a catalog constant changes (today's 12 fix commits are exactly this shape).

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

## `ISSUE_000287` Have Devin draft the pre-merge QA verdict summary into the PR body so the merge decision cites it.

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

## `ISSUE_000288` Merge before the Devin QA verdict

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

## `ISSUE_000289` Reviewer remediates, approves, merges

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

## `ISSUE_000290` Self-merge on a 7-s empty co-approval

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

## `ISSUE_000291` `#1358` closed without disposition

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

## `ISSUE_000292` Function-header backfill (§4.2) — 25 files today, 21 files on `#1380` 09-16

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

## `ISSUE_000293` Timestamp-surface sweep ("close the surfaces the sweep missed")

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

## `ISSUE_000294` Remediating a colleague's PR end-to-end before approving

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

## `ISSUE_000295` Generate a timestamp-surface inventory test (every component that renders a date gets one fixture) so the "surfaces the sweep missed" class closes permanently.

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

## `ISSUE_000296` Delegate the header-backfill as a lint autofix PR rather than 25-file manual commits.

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

## `ISSUE_000297` Use Devin to draft the "known risks" section for `#1390`'s follow-up so the 70/100 verdict has an owner list.

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

## `ISSUE_000298` Reviewer remediates, then approves and merges

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

## `ISSUE_000299` QA verdict after merge

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

## `ISSUE_000300` "repair the typecheck and lint failures the first gate run surfaced"

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

## `ISSUE_000301` Standards-audit doc + gate history

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

## `ISSUE_000302` Split `#1391` by runtime (api / worker / scheduler / web) with Devin generating the per-runtime PR bodies from the audit doc.

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

## `ISSUE_000303` Migration dry-run + rollback checklist for the path-registry split.

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

## `ISSUE_000304` >200-file single PR

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

## `ISSUE_000305` Multi-day branch without PR

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

## `ISSUE_000306` Phase-result ledger commits

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

## `ISSUE_000307` DOCX-fidelity fixture tests: template → rendered → expected table/spacing attributes.

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

## `ISSUE_000308` Open `feat/support-letter-word-fidelity` as a draft now; let Devin Review run on the 84-file move before more lands on top.

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

## `ISSUE_000309` Branch without PR

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

## `ISSUE_000310` Feature finished by the reviewer

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

## `ISSUE_000311` "expose Prometheus metrics …" per service

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

## `ISSUE_000312` Generate metric-name + label-cardinality tests per service from the shared factory.

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

## `ISSUE_000313` Have Devin triage the 15 findings into "fix / accept with reason / out of scope" so the disposition is a review, not a rewrite.

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

## `ISSUE_000314` Findings left undispositioned

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

## `ISSUE_000315` Empty approvals on >200-file PRs

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

## `ISSUE_000316` Ask Devin for a "what changed since my last look" digest before approving a 250-file PR.

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

## `ISSUE_000317` Empty co-approval enabling self-merge

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

## `ISSUE_000318` —

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

## `ISSUE_000319` `#1373` decision items 1–3 (in prod since 09-15) — Devin can draft the decision record from the thread.

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

## `ISSUE_000320` `#1373` decisions unrecorded

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

## `ISSUE_000321` Manual `Dev_1.0 → Dev_2.0` sync PRs

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000322` Hand-made `dev → uat` promotion PRs

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000323` Empty approvals

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

## `ISSUE_000324` Scheduled `Dev_1.0 → Dev_2.0` sync PR whose body lists the ported commits and conflicts — replaces `#6`.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000325` Regression tests for the writeback cron under 2+ replicas (Devin can extend today's `withCronLock` spec).

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000326` Promotion manifest: "PRs and Devin findings carried by this promotion" auto-generated.

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000327` Empty approvals on prod-bound PRs

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

## `ISSUE_000328` Hand-made sync/promotion PRs

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000329` Production `23505` fix (`#651` closed)

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

## `ISSUE_000330` Three successive "enhance/improve error handling" refactors on the same file

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

## `ISSUE_000331` Regression tests for cron-expression edge cases (blank, nonzero seconds, day-constraint intersection) — the last three findings on `#584`/`#657` are exactly thi

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000332` Multi-replica test harness for the import trigger (two workers, one lock).

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000333` Empty approvals

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

## `ISSUE_000334` Partial finding disposition on prod-path features

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000335` Per-client ENM rule branches (DVG, McQueen)

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000336` Turn each "verified unreachable" disposition into an executable test so the argument cannot rot.

- Repository: nextgen-codio-engine
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

## `ISSUE_000337` Generate the per-client parity fixtures for the E&M level rule.

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000338` —

- Repository: nextgen-codio-engine
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

## `ISSUE_000339` Manual `client_configs` sync from prod DB

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000340` `uat → prod` template promotions

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000341` Client-config diff report (what knob changed, which client, which gate) posted to the PR before merge.

- Repository: nextgen-codio-engine
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

## `ISSUE_000342` A real parity guard test for the gynecology clone (the finding says the current one checks nothing).

- Repository: nextgen-codio-engine
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

## `ISSUE_000343` Prod promotion on ≤4-char approval

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000344` Findings unanswered after merge

- Repository: nextgen-codio-engine
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

## `ISSUE_000345` `feat/log_prob` branch without PR

- Repository: nextgen-codio-engine
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

## `ISSUE_000346` Prompt files recovered/reverted by hand

- Repository: nextgen-codio-engine
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

## `ISSUE_000347` 4-char approvals on prod PRs

- Repository: nextgen-codio-engine
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

## `ISSUE_000348` A prompt-diff check that fails CI when `dx/px` extraction prompts change without a changelog entry.

- Repository: nextgen-codio-engine
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

## `ISSUE_000349` Have Devin reproduce the BMI finding (`Z68` inactive) on a fixture chart.

- Repository: nextgen-codio-engine
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

## `ISSUE_000350` Merge-then-revert on prompt content

- Repository: nextgen-codio-engine
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

## `ISSUE_000351` Prod promotion with an open Devin finding

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000352` 0-minute merges

- Repository: nextgen-codio-engine
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

## `ISSUE_000353` A merge-queue rule: no merge until Devin Review has posted.

- Repository: nextgen-codio-engine
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

## `ISSUE_000354` Merge before automated review posts

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Derive QA cases from the issue, the diff, and the acceptance criteria.
2. State explicitly which cases can and cannot be executed with available access.
3. Execute the executable cases and record inputs, outputs, and environment.
4. Classify every failure as code defect, test defect, environment, data, or configuration.
5. Report unexecuted cases as NOT_RUN rather than assuming a pass.

**Stop conditions**

- MISSING_CAPABILITY: qa.execute_cases: No QA environment or credentials are provisioned for the pilot.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- Required test environment or credentials are unavailable.
- Validation would require production or PHI access.

## `ISSUE_000355` Prompt-variant runs via runner flags

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000356` Eval-report generator for prompt promotions (recall/precision per chart set) attached to the PR.

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000357` —

- Repository: nextgen-codio-engine
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000358` Self-merge to `main` 0 min after open

- Repository: medicodio-nextgen-rf-rpa-automation
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

## `ISSUE_000359` Per-branch split skeletons (three endoscopy branches)

- Repository: medicodio-nextgen-rf-rpa-automation
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000360` Screenshot-diff replay harness for the split flow ("one stitched picture per split" is already captured — assert on it).

- Repository: medicodio-nextgen-rf-rpa-automation
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

## `ISSUE_000361` Table-driven test for the eleven splitting insurances.

- Repository: medicodio-nextgen-rf-rpa-automation
- Autonomy tier: **C** (no execution)
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Steps**

1. Enumerate every affected file and confirm the change is deterministic per file.
2. Confirm the transformation is reversible and produces no behavior change.
3. Apply the transformation in reviewable slices, each independently buildable.
4. Run build, typecheck, and the affected test suites per slice.
5. Record the file list, commands, and results for each slice.

**Stop conditions**

- SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive
- MISSING_CAPABILITY: repo.multi_file_edit: Dry-run pilot performs no writes to engineering repositories.
- MISSING_CAPABILITY: git.stacked_branches: Dry-run pilot creates no branches, commits, or pull requests.
- MISSING_CAPABILITY: ci.run_targeted_tests: No engineering repository is checked out or allowlisted in the pilot.
- The transformation requires human judgment on any file.
- Any slice changes runtime behavior.
- The migration touches database schema, data, or irreversible infrastructure.

## `ISSUE_000362` Self-merge to `main`, no review

- Repository: medicodio-nextgen-rf-rpa-automation
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

## `ISSUE_000363` Lockfile churn repair after merges

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

## `ISSUE_000364` Lockfile-drift CI check.

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

## `ISSUE_000365` `hitesh/` branches under `karthikmed`

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

## `ISSUE_000366` Same secret/doc fix applied to 3 repos by hand

- Repository: unresolved
- Autonomy tier: **C** (no execution)
- Proposed action: PROPOSE: no approved playbook matched; request human direction.
- Rollback: Nothing to roll back: this issue is proposal-only, so no repository state is changed.

**Stop conditions**

- NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook

## `ISSUE_000367` Env-example consistency check across nodejs/react/2.0.

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

## `ISSUE_000368` Devin-reviewed PR closed without disposition

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

## `ISSUE_000369` Direct pushes without PR

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

## `ISSUE_000370` Retry/back-off tests for eCW PPV lookups (Good Devin Candidate).

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

## `ISSUE_000371` —

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
