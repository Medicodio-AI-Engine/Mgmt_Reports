# Brief — Controlled Remediation Workflow for Devin (as built, Version 1)

This is the original prompt-architect brief, updated to match what is actually
implemented in `remediation/` and what the pilot has already produced. Sections
marked **As built** state the implemented behaviour; **Deferred** marks contracts
that exist but are intentionally not executed yet.

## 1. Objective

Take recurring engineering activity reports, vulnerability findings, QA and review
findings, CI failures and defect reports, and progressively automate the
engineering remediation lifecycle — without granting autonomy up front.

Stages: discover and normalize → classify and prioritize → match a playbook →
decide permitted autonomy → plan → fix eligible low-risk work in Dev → generate
regression tests → human review → (later) QA → UAT → release → learning.

**As built.** Version 1 runs `00_INTAKE → 01_TRIAGE → 02_PLAYBOOK_MATCH → 03_PLAN
→ 04_DEV_FIX → 05_DEV_REVIEW` and stops. `06_QA`, `07_UAT`, `08_RELEASE` and
`09_LEARNING` exist as contracts only. The whole pilot is dry-run: no repository is
modified, no commit or PR is created in a target repository, no deployment happens,
and no external system is changed.

## 2. Core design principle

Every issue is a persistent object in a controlled state machine:

`DISCOVERED → TRIAGED → PLAYBOOK_MATCHED → PLANNED → DEV_FIXING → DEV_REVIEW →
QA_TESTING → UAT_TESTING → RELEASE_READY → CLOSED`, plus `BLOCKED`, `REJECTED`,
`ROLLED_BACK`.

Attempts and decisions are never overwritten: a retry opens a new attempt
(`ISSUE_000123_ATTEMPT_02`) and the rejected attempt stays immutable.

**As built.** Transitions are validated (`states.py`); promotion past `DEV_REVIEW`
is refused. Review decisions are attempt-scoped, so a rejection cannot leak onto a
successor attempt. Issue IDs are stable across runs through a registry.

## 3. Input sources

Daily engineering activity reports, vulnerability and scanner findings, GitHub PR
reviews, Devin Review findings, CI/CD failures, test failures, QA and UAT findings,
human-entered defects, code-quality findings, environment validation reports.

**As built.** The pilot ingests the management reports in
`Ai_Engr_Rpt/Daily/medicodio/Detail/`: the activity report and the employee rating
cards for the report date. Every source is normalized into one issue shape before
anything else happens. A date whose inputs are incomplete is reported as
`PARTIAL`/incomplete rather than analysed as if it were whole.

**Rating cards are corroborating evidence only.** They help prioritise; they are
never tasks, and no individual rating value or band is reproduced in any
human-readable artifact.

## 4. Issue normalization

Normalized fields: issue ID, run ID, source, source artifact, repository,
branch/ref, environment, product, component, title, description, category,
defect/vulnerability type, security scope, files, related PR/commit, evidence,
reproduction information, status, confidence, owner, detection timestamp.
Repeated findings are deduplicated.

**As built.** Plus, for the pilot: `repository_scope` (`IN_SCOPE`,
`OUT_OF_SCOPE`, `UNRESOLVED`), `remediable`
(`CODE_CHANGE` / `TOOLING_AUTOMATION` / `NON_CODE_PROCESS` / `UNKNOWN`), the
reported vs analysed category pair, and a read-only `code_review` record per
candidate repository (see §11).

### Repository scope (pilot restriction)

In scope: `Mgmt_Reports`, `medicodio-nextgen-app-nodejs`,
`medicodio-nextgen-app-react`, `medicodio-nextgen-integration`,
`medicodio-paperclip`, `nextgen-codio-engine` (prefixes `medicodio-`,
`nextgen-codio`). Explicitly excluded: `globalcodio-monorepo`, `paperclip-ai`,
`interview`. Out-of-scope findings are preserved with their evidence and listed
under "Out of pilot scope" — never silently dropped, never candidates for work.

## 5. Priority scoring (1–10, 10 = act now)

10 active exploitation / outage / PHI exposure / auth bypass / money integrity ·
9 critical security-control or tenant-isolation failure · 8 major customer-impacting
defect with no workaround · 7 high impact with workaround · 6 important regression ·
5 medium · 4 localized · 3 low · 2 cosmetic · 1 hygiene.

Priority is independent of complexity: `Priority 10, Complexity 2` is an excellent
fast-remediation candidate.

## 6. Complexity scoring (1–10, 10 = hardest)

Considers repositories affected, domain ambiguity, files touched, migrations,
security sensitivity, external dependencies, testability, reproduction difficulty,
environment dependencies, rollback difficulty, blast radius, cross-team
coordination, business-rule ambiguity. Autonomous pilot band: complexity 1–4.

## 7. Playbook and skill matching

No fix begins before playbooks and skills are evaluated. Lookup order: org
playbook → org skill → previously successful org pattern → approved general
playbook → no-match escalation. Org playbooks always beat generic guidance.

Each match records playbook ID and name, source (`ORG` / `GENERAL` / `NONE`),
confidence 0–100, why it matched, required / available / missing skills, acceptance
criteria, required tests, rollback guidance, prior success statistics, and human
approval requirements. Uncertain match ⇒ stop before any code change.

**As built.** Five starter playbooks (regression test generation, mechanical
migration, QA validation, tenant-isolation validation, process-improvement
proposal). Latest 08-23 run: match rate 0.894.

## 8. Autonomy classification

* **Tier A** — autonomous execution allowed (mechanical rename, import fix,
  formatting, test generation, deterministic codemod).
* **Tier B** — implement and test, human approval before merge/promotion.
* **Tier C** — investigation and proposal only until approved (authorization,
  tenant-isolation policy, sensitive domain rules, financial correctness).
* **Tier D** — human-owned: secrets, PHI scope, authn/authz policy, production
  access, billing semantics, destructive data operations, irreversible migrations,
  compliance decisions. Evidence and options only.

**As built.** Unverified security scope caps the tier at B rather than blocking
planning outright, and records `SECURITY_SCOPE_UNVERIFIED` so a reviewer sees why.
The 08-23 run classified everything at tier C or D, so nothing was eligible for
execution even if the pilot were not dry-run.

## 9. Dev remediation stage

Preconditions: reproducible issue or sufficient evidence, approved playbook,
acceptance criteria, permitted tier, rollback plan, test strategy. Then: branch →
reproduce → generate a regression test → prove it fails before the fix → fix →
targeted tests → broader tests → typecheck/build → record changed files and commit
SHA → PR → evidence.

**Never claim an issue is fixed because the code changed.** Where technically
possible there must be a failing-before / passing-after test.

**As built.** Dry run: this stage plans and records what would be done, and writes
nothing outside the artifact directory. Missing capabilities are named rather than
assumed — the 08-23 run reports targeted CI runs blocking 20 issues, stacked
branches 9, multi-file edit 9, QA execution 6, regression-test writing 5.

## 10. Human review stage

`APPROVE` → QA · `REVIEW / ASK QUESTION` → Q&A loop · `REJECT` → record reviewer,
reason, category, required correction, timestamp; return to `DEV_FIXING` with a new
attempt; never delete the rejected attempt.

**As built.** File-based: a `DECISION:` block committed into the run's
`05_DEV_REVIEW` artifact in `Mgmt_Reports` is the review record, so the audit trail
lives in git next to the reports.

## 11. Reading the target code (added during implementation)

Task descriptions must describe the work a person or Devin actually carried out —
not what this platform proposes to do. Two read-only readers provide that:

* `history.work_done()` — the checkout's own history for the report date: commit
  count, author, subjects, and a per-commit `--shortstat` against the version
  immediately before it. When the finding quotes commit subjects, the history is
  narrowed to those commits.
* `codebase.inspect()` — what the code looks like now: whether reported paths still
  exist, and a source-file count.

Both are opt-in via `repository_root` / `REPOSITORY_ROOT` and **only read**: the
only commands are fixed `git log`, `git diff --shortstat` and `git rev-parse`
queries with `-C <checkout>` (a non-whitelisted git subcommand raises). Nothing is
fetched, checked out, staged or committed; no file in a target repository is opened
for writing. An unconfigured or absent checkout reports "not inspected" rather than
guessing, and never blocks a run.

## 12. Supervisor report (added during implementation)

Every run writes `<date>_<run>_SUPERVISOR_REPORT.md` and `.csv`, generated from the
analysed issues, one row per in-scope task:

`Task_ID`, `Task_Name`, `Task_Description`, `Task_Owner`, `Task_Type`, `Category`,
`Revised_Category`, `Category_Match`, `Complexity` (1–10), `Time_Human`, `Time_AI`,
`Time_Human_AI`, `Comments`.

* `Category` is what the report claimed; `Revised_Category` is what analysis
  concluded; `Category_Match` says whether they agree. BUG = functionality existed
  and is broken; ENHANCEMENT = the capability does not exist yet.
* `Task_Description` leads with the work the repository history shows landed, then
  the current read-only code state, then the report's claim and its recommendation.
  This platform's own plan steps are excluded — they are proposed future work.
* Corroborating rating signals and out-of-scope findings are counted below the
  table, never listed as tasks.

### Effort estimates (recalibrated)

Deterministic `HH:MM` planning figures from complexity × remediability × autonomy
tier — planning estimates, not measurements.

| Column | Meaning |
| ------ | ------- |
| `Time_Human` | the task done by a person alone |
| `Time_AI` | Devin alone — writing the change is the part it does fastest, so this is a small fraction of the human figure (roughly an eighth for code and tooling work, a quarter for process/judgement work); at tier C/D it covers investigation and a written proposal only, because policy forbids the AI making the change |
| `Time_Human_AI` | elapsed time when the two collaborate — **not** the sum, and never longer than `Time_Human`: the person spends about half their solo time directing and reviewing work that arrives already drafted |

```text
human = minutes_per_point[remediability] * complexity
ai    = human * (0.08 if proposal_only else share[remediability])  # 0.12 code, 0.25 process
joint = min(ai + (0.5 * human if proposal_only else 30), human)
```

## 13. Deferred stages (contracts only)

**QA.** Promote to QA, generate cases from the issue, acceptance criteria, diff,
regression tests and playbook, execute where automation exists, record results and
a summary. QA must classify a failure (`CODE_DEFECT`, `TEST_DEFECT`, `ENVIRONMENT`,
`TEST_DATA`, `CONFIGURATION`, `EXPECTED_BEHAVIOR`, `UNKNOWN`) before returning it;
only a confirmed `CODE_DEFECT` goes back to Dev automatically.

**UAT.** A UAT failure goes `UAT_TESTING → QA_TESTING` first — QA reproduces and
verifies before any code change, so environment, configuration, data or
misunderstanding problems never cause code churn.

**Release.** Approvals, tests, QA and UAT passes, no blockers, rollback plan,
deployment procedure, PR/commit references and evidence, then `RELEASE_READY →
CLOSED`; a production problem records `ROLLED_BACK`.

**Learning.** Per issue: playbook used, category, priority, complexity, tier,
attempts, rejections, questions, time to fix/QA/UAT, first-pass results, rollback,
false positive, human intervention. Aggregated into playbook success rate,
autonomous-fix success rate, QA/UAT first-pass rates, average attempts, rejection
and false-positive rates, average remediation time, and the complexity range
successfully automated. Autonomy expands only on statistically meaningful success.

## 14. Pilot scope and tracking

Run discovery → triage → priority/complexity → playbook match → proposed fix →
regression test → dev fix → human review. No auto-promotion through QA/UAT. Focus
on complexity 1–4, tier A/B, well-defined issues, strong reproduction, existing
test frameworks, reversible changes.

Track: total and deduplicated findings, priority and complexity distribution,
complexity 1–4 count, auto-fix attempts and successes, human-approved and rejected
fixes, Q&A corrections, regression tests generated, failing-before/passing-after
rate, QA first-pass rate on manual promotion, false positives, average remediation
time, playbook match rate, org vs general playbook usage.

Success criteria: complete issue-to-evidence traceability, zero autonomous Tier-D
changes, no promotion with required tests missing, most fix attempts carry a
reproducible test, and a reviewer can understand the change from the
People_Engineer summary alone.

**As built, latest 08-23 run.** 47 issues normalized · 14 in-scope supervisor tasks
(0 bug, 14 enhancement; 3 reported categories revised) · 6 corroborating rating
signals · 27 out-of-pilot findings preserved · playbook match 0.894 · 0
guardrail-blocked · 47 awaiting a human decision · **0 commits, 0 PRs, 0
repositories modified, 0 executions**.

Note on findings that are not code defects: most 08-23 findings are process or
automation opportunities, and CI blackouts are environment/process signals. Neither
is treated as a code defect, so the pilot does not manufacture fake Tier-B work.

## 15. File architecture

`YYYY_MM_DD_<RUN_ID>_<STAGE>_<ARTIFACT>_<AUDIENCE>.<ext>` — the date prefix is
mandatory, the run ID is constant across one execution, issue IDs are stable
throughout.

**As built.** Artifacts live with the reports they came from:
`Ai_Engr_Rpt/Daily/medicodio/Remediation/<YYYY_MM_DD>/<RUN_ID>/`, containing
`PRE_STAGE`, the six stage folders, `audit.jsonl`, `<date>_<run>_METRICS.json`,
`<date>_<run>_SUMMARY.md` and the two supervisor report files. A stage's input
references the previous stage's machine output by relative path and SHA-256 instead
of copying every issue, so the daily directory stays reviewable in a diff. Source
report filenames are kebab-case as they exist in the repo
(`mgmt-activity-report-2026-08-23.md`), not the brief's underscore form.

## 16. Two outputs per stage

`OUTPUT_DEVIN_AI.json` — maximum machine context for the next stage: run and issue
IDs, attempt, stage, status, evidence, source references, repository, environment,
category, security classification, priority, complexity, confidence, playbook match
and score, required and missing skills, autonomy tier, stop conditions, proposed
action, implementation plan, changed files, commands, test cases and results,
pre-fix failure and post-fix success, full-suite result, commit SHA, PR number,
rollback plan, review result, comments, questions, answers, rejection history, next
state and next expected input file.

`OUTPUT_PEOPLE_ENGINEER.md` — deliberately short: what was found, why it matters,
priority, complexity, confidence, matched playbook, required skills, proposed fix,
files changed, tests generated, results, risks, rollback, and the approve /
ask / reject decision.

Every stage also writes `INPUT.json`, and every output names the next expected
state and input file. All artifacts are schema-validated on write.

## 17. Guardrails

The automation must never: silently make security-policy decisions; modify
PHI-access rules; change authz or tenant-isolation policy; alter billing or money
semantics; expose or modify secrets outside an approved mechanism; promote with
required tests missing; claim remediation without evidence; delete rejection
history; overwrite a previous attempt; treat an environment failure as a code
defect without verification; use a generic playbook where an org playbook
conflicts; or expand its own permissions on the strength of one successful run.

**As built.** Enforced in code and covered by adversarial CLI tests: a dry run
writes nothing and makes no network call even with writes forced on, nothing
promotes past `DEV_REVIEW`, the review lifecycle is attempt-scoped, no rating value
leaks into an artifact, and malformed input fails loudly instead of being guessed.

## 18. Observability

The run generates its own telemetry — session/run ID, input used, playbook
selected, skills invoked, commands executed, files changed, test commands and
outcomes, attempt count, questions and answers, approval or rejection with reasons,
correction loops, promotion history, environment results, final disposition — so
what happened can be reconstructed without Devin session-history permissions.

**As built.** `audit.jsonl` per run, plus `METRICS.json` and the human `SUMMARY.md`.

## 19. Implementation conventions

* Python 3.11, pytest; package under `remediation/`.
* One responsibility per function, at most ten statements, enforced by
  `remediation/tools/function_length.py` (run it like a linter).
* Checks before any change lands: `pytest remediation/tests`, `ruff check`,
  `ruff format --check`, `python remediation/tools/function_length.py`.
* Configuration in `remediation/config/config.yaml`, overridable by environment
  (`remediation/.env.example`); no secrets are needed for a dry run.
* Extending the playbook registry is documented in `remediation/README.md`.

## 20. Design philosophy

The goal is not "give Devin vulnerabilities and let it fix everything". It is a
controlled remediation system where Devin progressively earns autonomy based on
issue type, playbooks, complexity, evidence, testing, and measured historical
success:

evidence before action · playbook before fix · test before claiming remediation ·
human control for sensitive decisions · immutable history for every attempt · QA
verification before sending failures back to Dev · progressive autonomy based on
measured success.
