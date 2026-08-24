# Supervisor report — remediation tasks

**Run:** `RUN_0001` · **Report date:** 2026-08-23

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **14** — 0 bug(s), 14 enhancement(s)
- Reported category revised after analysis: **3**

| Task_ID | Task_Name | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ISSUE_000034` | Manually re-running batch/dev runs to verify a guard | sameer-s-mansur | Code fix | ENHANCEMENT | ENHANCEMENT | yes | 6 | 06:00 | 01:30 | 07:30 | category MISSING_TEST confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000037` | Use Devin to build a repeatable integration verification harness for the lock-key / attach-form workflows, replacing the hand-run dev runs he re-does each time. | sameer-s-mansur | Code fix | ENHANCEMENT | ENHANCEMENT | yes | 6 | 06:00 | 01:30 | 07:30 | category MISSING_TEST confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000038` | Use Devin to write regression tests for Elaris filename pairing (63 files landed with no human review and 3 open Devin Review findings). | sameer-s-mansur | Code fix | BUG | ENHANCEMENT | no | 6 | 06:00 | 01:30 | 07:30 | reported as bug but category MISSING_TEST shows the capability does not exist yet, so it is an enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000041` | Mirroring every KB wizard change across backend and UI by hand | hitesh | Tooling / automation | ENHANCEMENT | ENHANCEMENT | yes | 7 | 05:45 | 01:30 | 07:15 | category AUTOMATION_OPPORTUNITY confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000043` | Use Devin to generate a KB guideline wizard regression suite (General / Specialty / Specialty-Payer / Client-Payer scopes) so a versioning reversal of this size | hitesh | Code fix | BUG | ENHANCEMENT | no | 6 | 06:00 | 01:30 | 07:30 | reported as bug but category MISSING_TEST shows the capability does not exist yet, so it is an enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000047` | Commit identity not linked to a GitHub account | hitesh | Process change | ENHANCEMENT | ENHANCEMENT | yes | 10 | 05:00 | 01:15 | 06:15 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000044` | Use Devin to carve the KB branches into landable PRs (schema/API, then UI, then wizard UX) instead of one 130-file backend branch plus one 226-file UI branch. | hitesh | Code fix | ENHANCEMENT | ENHANCEMENT | yes | 7 | 07:00 | 01:45 | 08:45 | category MECHANICAL_MIGRATION confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000035` | Self-merging integration PRs within minutes | sameer-s-mansur | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 01:00 | 05:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000036` | Non-conventional commit subjects | sameer-s-mansur | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 01:00 | 05:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000042` | Carrying 130/226-file branches for days, then replacing the PR | hitesh | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 01:00 | 05:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000039` | Integration changes landing with no independent review | sameer-s-mansur | Process change | ENHANCEMENT | ENHANCEMENT | yes | 6 | 03:00 | 00:45 | 03:45 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000040` | Re-plumbing `version_number` through KB create/read paths, one surface at a time | hitesh | Process change | BUG | ENHANCEMENT | no | 8 | 04:00 | 01:00 | 05:00 | reported as bug but category PROCESS_PRACTICE shows the capability does not exist yet, so it is an enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000045` | Use Devin for the paired backend/UI propagation of each KB contract change. | hitesh | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 01:00 | 05:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000046` | Very large, long-lived unmerged branches | hitesh | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 01:00 | 05:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |

## Corroborating signals (6)

6 support record(s) from the rating cards helped prioritise the tasks above. They are not tasks, and no individual rating is reproduced here.

## Out of pilot scope (27)

- `ISSUE_000007` CI has no successful runs in globalcodio-monorepo — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000008` Hand-writing `docs/review-logs/` gate + review logs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000009` Merging `origin/dev` into each feature branch by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000010` Composing the Architect+EM review skeleton (verdict, lenses, nit list) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000011` Use Devin to generate a regression suite for the AI Case Manager send-path defect class (#1210's "reviewed draft discarded on send", #1213's email header, #1215 — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000012` Use Devin to emit the review-log artifact from the existing `/check` + `/fix` output, replacing the hand-written `docs/review-logs/` commits. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000013` Use Devin to split feature branches over ~100 files into stacked, individually reviewable PRs before review starts (#1212 was 140 files). — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000014` Hand-written review/audit logs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000015` Very large single-PR diffs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000016` `dev → feat/qa-automation` promotion/sync PRs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000017` Post-merge QA audit of already-merged feature work — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000018` Filling (or not filling) the PR template by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000019` Use Devin for the recurring `dev → feat/qa-automation` sync plus its QA audit — mechanical, repeats every few days, and currently bypasses review entirely. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000020` Use Devin to finish landing #1208 (the notes-visibility feature it authored): #1209's remediation is merged into the branch, so the remaining work is bounded. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000021` Use Devin to generate the live authenticated API validation he explicitly skipped on #1214, as a repeatable harness rather than a per-run manual pass. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000022` Promotion/sync PR self-merged without independent review — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000023` Unfilled PR-template bodies — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000024` `/check` → `/fix` blocker clearing before review — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000025` Writing the standards/review log by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000026` Syncing `origin/dev` into the feature branch — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000027` Use Devin to generate regression tests for the email-header / platform-field contract so the case_number behavior cannot silently regress (this surface changed  — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000028` Use Devin for the pre-merge `/check`+`/fix` blocker pass on her branches, so her time goes to the domain decision rather than the standards sweep. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000029` Late-night test/doc top-ups on a long-lived shared branch — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000030` Merging without a recorded human review — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000031` Use Devin to build the portal access-control test matrix (roles × account statuses) — bounded, high-value on a security surface, and it removes the late-night m — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000032` Use Devin to split #1183-class branches (150 files, open 5 days) into stacked reviewable PRs. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000033` Merges without an independent human review record — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_AI` for a tier C or D task covers investigation and proposal only, because policy forbids the AI from making that change.
