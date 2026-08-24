# Controlled engineering remediation platform (Version 1)

Turns the committed daily management reports in `Ai_Engr_Rpt/Daily/medicodio/Detail` into
normalized, prioritized, playbook-matched, autonomy-classified remediation proposals, and
stops at human review.

```
PRE_STAGE → 00_INTAKE → 01_TRIAGE → 02_PLAYBOOK_MATCH → 03_PLAN → 04_DEV_FIX → 05_DEV_REVIEW
```

`06_QA`, `07_UAT`, `08_RELEASE`, and `09_LEARNING` exist as schema-validated contracts only.
Their builders raise `StageDisabledError` until they are explicitly enabled, so Version 1 cannot
promote work into QA, UAT, or production.

## The pilot is dry-run only

`dry_run_mode: true` and an empty `remediation_repository_allowlist` mean the pilot:

- modifies no engineering repository,
- creates no branch, commit, or pull request,
- deploys nothing and changes no external system,
- records what it *would* have done, with the reasons execution was suppressed.

`--allow-writes` only turns off `dry_run_mode`; execution is still refused for every repository
that is not in the allowlist, and `config/config.yaml` ships with that list empty.

## Install and run

```bash
python3.11 -m venv .venv && .venv/bin/pip install -e remediation
cd remediation

../.venv/bin/python -m remediation validate                  # config, playbooks, skills, schemas
../.venv/bin/python -m remediation discover                  # source manifest only
../.venv/bin/python -m remediation --config config/config.yaml run \
    --repository-root ..                                     # full Version 1 flow, dry run
../.venv/bin/python -m remediation decisions                 # every DECISION block on file
```

`run` picks the latest date whose sources are complete unless `--report-date` is given. A
complete date needs both a detailed engineering report and an employee rating card report; a
date with only one of them runs as `PARTIAL` and is flagged `PARTIAL_SOURCE_DATA` and
analysis-only.

Artifacts land in `Ai_Engr_Rpt/Daily/medicodio/Remediation/<YYYY_MM_DD>/<RUN_ID>/`, one directory per
stage, named `YYYY_MM_DD_<RUN_ID>_<STAGE>_<ARTIFACT>_<AUDIENCE>.<ext>`. Each stage writes
`INPUT.json`, `OUTPUT_DEVIN_AI.json` (schema-validated), and `OUTPUT_PEOPLE_ENGINEER.md`.
`audit.jsonl` is append-only.

## Human review

Review is a `DECISION:` block committed into the `05_DEV_REVIEW` human artifact — one block per
attempt, keyed `DECISION: ISSUE_000123_ATTEMPT_01`:

```
### DECISION: ISSUE_000009_ATTEMPT_01
DECISION: APPROVE          # APPROVE | REVIEW (needs >= 1 question) | REJECT
REVIEWER: raj
COMMENTS:
QUESTIONS:
```

Commit the file and run again. The next run reads the block back:

- `APPROVE` records the approval and leaves the issue in `DEV_REVIEW`. Version 1 promotes nothing.
- `REVIEW` records the questions and keeps the attempt in `DEV_REVIEW`.
- `REJECT` preserves the rejected attempt and opens exactly one successor (`_ATTEMPT_02`) in
  `DEV_FIXING`. A decision applies to the attempt it names, so a stale rejection never travels
  to a later attempt.

Anything unparseable (missing outcome, `REVIEW` with no question, unrecognized value) stays
`PENDING` and is reported as malformed rather than guessed.

## What stops the platform

- **Autonomy tiers** — A autonomous, B implement-then-approve, C investigate/propose only,
  D human-owned. Missing capabilities, unverifiable security scope, environment signals, and
  complexity above `max_complexity_for_autonomy` all lower the tier; nothing raises it.
- **Guardrails** — security policy, PHI access, authentication, authorization, tenant isolation,
  billing/money semantics, secrets, destructive operations, irreversible migrations, compliance
  decisions, treating an environment failure as a code defect, treating an employee rating as a
  defect, preferring a general playbook over a conflicting org playbook, and premature
  promotion. Every violation records the rule, stop reason, evidence, required human action, and
  the state it forces (`BLOCKED` or human-owned).
- **Evidence rules** — an employee rating alone never proves a software defect (rating detail is
  redacted downstream, only the source locator survives), and a CI outage is an environment
  signal until someone shows it is a code defect.

## Supervisor report

Every run writes `<date>_<run>_SUPERVISOR_REPORT.md` and `.csv` next to the stage
folders, generated from the analysed issues (never hand-written), with one row per
in-scope task: `Task_ID`, `Task_Name`, `Task_Description`, `Task_Owner`,
`Task_Type`, `Category`, `Revised_Category`, `Category_Match`, `Complexity` (1-10),
`Time_Human`, `Time_AI`, `Time_Human_AI`, `Comments`. Corroborating signals and
out-of-scope findings are listed and counted below the table, never as tasks.

`Task_Description` says what was observed, what is proposed, what a read-only look
at the code found, and the first plan steps.

The three time columns are deterministic `HH:MM` planning estimates, not
measurements:

| Column | Meaning |
| ------ | ------- |
| `Time_Human` | how long the task takes a person working alone |
| `Time_AI` | how long Devin takes alone — for tier C/D that is investigation and a proposal only, because policy forbids the AI making the change |
| `Time_Human_AI` | elapsed time when the two collaborate (Devin drafts, a person directs and reviews) — **not** the sum of the other two, and never longer than `Time_Human` |

### Reading the target code

Set `repository_root` (or `REPOSITORY_ROOT`) to a directory holding local checkouts
of the target repositories and the description states what the code looks like
today. The inspection is read-only: paths are tested for existence and source files
counted, nothing is opened for writing, and no command or git operation runs. Unset,
or a repository with no checkout under that root, reports "not inspected" rather
than guessing — it never blocks a run.

## Layout

| Path | Contents |
| ---- | -------- |
| `src/remediation/` | pipeline, stages, state machine, scoring, playbooks, autonomy, guardrails, review |
| `schemas/` | pre-stage manifest, issue, stage output, future-stage contracts |
| `playbooks/org`, `playbooks/general` | approved playbooks; org playbooks win over general ones |
| `skills/registry.yaml` | capabilities available to the platform; dry run marks execution capabilities unavailable |
| `config/config.yaml`, `.env.example` | configuration; env vars override the file |
| `examples/` | manifest, `OUTPUT_DEVIN_AI.json`, and a `OUTPUT_PEOPLE_ENGINEER.md` with decisions filled in |
| `tests/` | unit and end-to-end tests |

## Tests

```bash
cd remediation
../.venv/bin/python -m pytest tests/
../.venv/bin/python -m ruff check . && ../.venv/bin/python -m ruff format --check .
```
