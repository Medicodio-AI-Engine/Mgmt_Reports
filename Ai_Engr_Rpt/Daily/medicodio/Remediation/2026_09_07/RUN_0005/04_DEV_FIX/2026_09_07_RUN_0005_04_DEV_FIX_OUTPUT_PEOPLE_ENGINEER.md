# Dev fix — dry-run record

**Run:** `RUN_0005` · **Report date:** 2026-09-07 · **Stage:** `04_DEV_FIX` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## `ISSUE_000282` Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge)

- Attempt: `ISSUE_000282_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000282-attempt-01
- plan step: Enumerate every affected file and confirm the change is deterministic per file.
- plan step: Confirm the transformation is reversible and produces no behavior change.
- plan step: Apply the transformation in reviewable slices, each independently buildable.
- plan step: Run build, typecheck, and the affected test suites per slice.
- plan step: Record the file list, commands, and results for each slice.

## `ISSUE_000283` Recording review passes as `docs(review-logs)` commits

- Attempt: `ISSUE_000283_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000283-attempt-01
- plan step: Derive QA cases from the issue, the diff, and the acceptance criteria.
- plan step: State explicitly which cases can and cannot be executed with available access.
- plan step: Execute the executable cases and record inputs, outputs, and environment.
- plan step: Classify every failure as code defect, test defect, environment, data, or configuration.
- plan step: Report unexecuted cases as NOT_RUN rather than assuming a pass.

## `ISSUE_000284` Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift)

- Attempt: `ISSUE_000284_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000284-attempt-01
- plan step: Enumerate every affected file and confirm the change is deterministic per file.
- plan step: Confirm the transformation is reversible and produces no behavior change.
- plan step: Apply the transformation in reviewable slices, each independently buildable.
- plan step: Run build, typecheck, and the affected test suites per slice.
- plan step: Record the file list, commands, and results for each slice.

## `ISSUE_000285` Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind)

- Attempt: `ISSUE_000285_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000285-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000286` Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f

- Attempt: `ISSUE_000286_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000286-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000287` Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher

- Attempt: `ISSUE_000287_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000287-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000288` Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co

- Attempt: `ISSUE_000288_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000288-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000289` Approves and merges a branch he remediated

- Attempt: `ISSUE_000289_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000289-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000290` Own "needs decision" items left open at merge

- Attempt: `ISSUE_000290_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000290-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000291` `#1278` `importSession` SEV-High finding without fix or waiver

- Attempt: `ISSUE_000291_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000291-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000292` Large unreviewed branches

- Attempt: `ISSUE_000292_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000292-attempt-01
- plan step: Enumerate every affected file and confirm the change is deterministic per file.
- plan step: Confirm the transformation is reversible and produces no behavior change.
- plan step: Apply the transformation in reviewable slices, each independently buildable.
- plan step: Run build, typecheck, and the affected test suites per slice.
- plan step: Record the file list, commands, and results for each slice.

## `ISSUE_000293` Insufficient data — one commit in the week

- Attempt: `ISSUE_000293_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000293-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000294` Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`.

- Attempt: `ISSUE_000294_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000294-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000295` Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio

- Attempt: `ISSUE_000295_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000295-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000296` Devin findings on own PR unanswered

- Attempt: `ISSUE_000296_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000296-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.

## `ISSUE_000297` Open PR not progressed by its author

- Attempt: `ISSUE_000297_ATTEMPT_01`
- DRY RUN: no repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed.

**Why nothing was executed**

- DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change
- globalcodio-monorepo is not in remediation_repository_allowlist

**What would have been done**

- create working branch devin/issue_000297-attempt-01
- plan step: Restate the reported pattern with its evidence and frequency.
- plan step: Identify whether the remedy is process, tooling, or code.
- plan step: Describe the smallest concrete improvement and who owns it.
- plan step: Produce the proposal for human decision; make no repository change.
