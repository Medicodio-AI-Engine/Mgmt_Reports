# Intake — normalized findings

**Run:** `RUN_0003` · **Report date:** 2026-08-25 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_08_25_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_08_25_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000130` | Low automation-adoption signal for svh-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000131` | Building one more report against the same catalog/controller/service/repository shape | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000132` | Fixing SQL type/cast defects found only at runtime | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000133` | Delegate a follow-on session to write the report-query regression suite (fixed fixtures per report, asserting org scoping and the restricted-visibility predicat | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000134` | Delegate the remaining PRD reports one session per report, referencing #1239 as the pattern. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000135` | Have a Devin session pre-answer reviewer questions on #1239 (per-report authorization proof, pagination bounds) so the human review is a verdict rather than an  | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000136` | Very large single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000137` | Running the full quality gate by hand and transcribing the result into a standards log | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000138` | Splitting oversized services/components after the fact | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000139` | Delegate the checklist-group regression suite (group CRUD, step-link audit, deadline sweep) to Devin — the audit-trail and TOCTOU fixes today are untested behav | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000140` | Have Devin answer the open Devin Review findings on #1238 explicitly so the thread shows resolution. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000141` | Single very large PR held open for days | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000142` | Manually filing UI defects with screenshots and no owner | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000143` | Delegate #1240 (email template pre-fill / cache) to Devin — clear reproduction, likely a stale-cache or default-props defect. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000144` | Delegate #1241 (questionnaire bundle import performance) as an investigation-first session: profile, then propose. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000145` | QA findings recorded but not converted into work | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000146` | fix → prod-hotfix → uat-sync fan-out of the same diff | MECHANICAL_MIGRATION | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000147` | Valley KB document corrections one field at a time | AUTOMATION_OPPORTUNITY | medicodio-nextgen-integration | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000148` | Delegate a "promote this fix" automation (fix → prod hotfix → uat sync) to Devin — it is deterministic, repeated daily, and today produced a duplicate PR. | MECHANICAL_MIGRATION | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000149` | Delegate tests for the migration trigger in #241 (env-source matrix, post-run ordering) before it merges — 20 files of RPA orchestration currently ship with no  | MISSING_TEST | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000150` | Have Devin sweep the 15 open Devin Review findings on his merged PRs and raise one remediation PR. | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000151` | Self-merge seconds after opening | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000152` | Devin Review findings unaddressed on merged PRs | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000153` | Hand-cut prod/uat promotion PRs | MECHANICAL_MIGRATION | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000154` | Approving another member's promotion/hotfix PRs with `lgtm` | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000155` | dev → uat sync PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000156` | Delegate the dev→uat sync PRs so his review time goes to the diffs that matter. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000157` | Delegate the #498 Devin Review finding and a font-token regression check — a 23-file CSS refactor with no visual test is a classic Devin task. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000158` | `lgtm` / one-word approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000159` | Unifying the same visual pattern across many panes/dialogs by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000160` | Opening 30–40-file frontend PRs with no reviewer requested | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000161` | Delegate the remaining pane migrations to the shared `StageHeading` contract — the pattern is fixed after #500. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000162` | Delegate component tests for the KB dialog dropdown fix; the ResizeObserver polyfill he just added makes them possible. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000163` | Large frontend PRs opened without a requested reviewer | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000164` | Devin Review findings left open on his PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000165` | Empty-body approvals as the sole gate before `Dev_1.0` | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000166` | Have Devin produce a pre-merge summary (risk, touched surfaces, missing tests) on PRs where he is the only reviewer, so the approval has evidence behind it. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000167` | Delegate the `Dev_1.0` promotion mechanics so his time goes to the diffs. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000168` | Empty-body approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000169` | Pushing feature work onto another member's long-lived branch with no PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000170` | Delegate the invoicing state-matrix tests (billing states "that tell the truth" implies a state machine worth pinning). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000171` | Work living on a long-lived shared branch with no PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000172` | Large engine features arriving as a single squashed commit | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000173` | Delegate the agentic-memory recall test matrix (routing_override / belief / confusion_pair / confirmed_phrase injection) — bounded, high-value, currently untest | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000174` | Delegate the `Docs//IMPLEMENTATION_GUIDE.md` sync the repo mandates for behaviour changes. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000175` | Draft PR with no reviewer requested | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000176` | Hand-tuning client-config bundles per client | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000177` | Delegate a config-bundle diff/validation tool (dev vs uat vs prod) — a tuning change that reaches `uat` on an `okay` approval currently has no automated check. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000178` | Delegate a regression run over sample charts for the tuned specialties. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000179` | Client-config change to `uat` on a one-word approval | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000180` | `okay` approvals on engine PRs he merges | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000181` | Have Devin run the engine's pytest gate on `uat` candidates before merge — the blueprint records 10 known-red tests, so a human eyeballing a diff cannot tell re | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000182` | One-word `okay` approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000183` | Renaming/rebinding rule files across specialties by hand | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000184` | Delegate a registry-discovery test that fails when a rule file's `RULE_NAME` has no registry row — the exact class of defect he just fixed four times by hand. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000185` | Delegate the remaining specialty-module discovery audit. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000186` | Non-descriptive commit messages | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000187` | Config/rule changes reaching branches without a PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000188` | Long-lived PR with a placeholder title accumulating review findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000189` | Delegate the #382 Devin Review findings as a single remediation session. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000190` | Delegate DXEX memory-consolidation tests — memory behaviour is cross-cutting and currently unpinned. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000191` | Non-informative PR titles ("UAT", "config changes ortho") | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000192` | Shared feature branch merged by hand between contributors | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000193` | Delegate schema-validation tests for the structured-output path through `call_llm` — the repo's single LLM entry point, and its JSON contract is an explicit inv | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000194` | Work on a shared long-lived branch with no PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000195` | Agent behaviour changes described only as "handled better" | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000196` | Delegate documentation + tests for the icd-memory agent's handling change so the behaviour is pinned and reviewable. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000197` | Vague commit messages / no PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
