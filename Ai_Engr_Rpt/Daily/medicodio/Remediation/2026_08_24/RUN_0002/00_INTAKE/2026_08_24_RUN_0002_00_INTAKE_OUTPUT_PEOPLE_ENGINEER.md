# Intake — normalized findings

**Run:** `RUN_0002` · **Report date:** 2026-08-24 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_08_24_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_08_24_Mgmt_Activity_Report.md` | yes |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000048` | Low automation-adoption signal for Medicodio-Amit | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000001` | Low automation-adoption signal for SaijyotiMeti | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000049` | Low automation-adoption signal for Pj-Vineeth-Kumar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000005` | Low automation-adoption signal for anirudh-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000050` | Low automation-adoption signal for jatinkushwaha-medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000006` | Low automation-adoption signal for hitesh | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000051` | Low automation-adoption signal for NandanDate-Medicodio | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000052` | Low automation-adoption signal for shaheen-khan11 | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000053` | Low automation-adoption signal for ragha82 | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000003` | Low automation-adoption signal for Amrutha-Beedikar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000054` | Preparing review-remediation PRs per reviewed PR | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000055` | Transcribing Architect+EM review logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000056` | Delegate remediation-PR preparation to Devin sessions from his own written findings lists (already structured with file/line references). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000057` | Have Devin pre-run the audit checklist on incoming PRs so his Architect+EM pass starts from a triaged findings list. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000058` | — none newly recurring for this member — | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000059` | uat/main promotion PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000060` | 900+ file branch-sync PRs (#1217, self-merged in 4 min) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000061` | Devin-generated release-diff summaries attached to every promotion PR, so approvers have something real to review. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000062` | Delegate branch-sync PRs (like #1217) to Devin with the gate suite as acceptance criteria. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000063` | Production-branch merges approved without substantive review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000064` | Self-merged sync PRs without independent review | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000065` | Merging after 'approved' one-word confirmations (#1235) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000066` | Use Devin to generate regression tests around the system-actor/impersonation boundary she just fixed in #1231 — the review noted 4 items needing her decision, i | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000067` | Drive #1208 (Devin's notes-visibility PR, now 4 days open with runtime verification posted) to a merge/close decision. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000068` | Working through QA DEV-FIX-LISTs item by item | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000069` | Feed the next QA DEV-FIX-LIST directly to a Devin session as acceptance criteria; today's #1221 shows the list format is precise enough. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000070` | Use Devin to generate portal-access regression tests covering the enable/disable roster paths fixed in #1222. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000071` | Large multi-concern PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000072` | Closing QA follow-up lists from earlier PRs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000073` | Before requesting human review on #1238, run the Devin Review findings to ground and fix them — 4 findings at open means reviewers will re-discover known issues | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000074` | Delegate the next QA follow-up batch to Devin with the follow-up list as acceptance criteria. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000075` | Large feature PRs opened with known findings outstanding | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000076` | Long-lived large PRs accruing repeated automated findings | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000077` | Use Devin to triage and fix the accumulated Devin Review findings on his PRs daily, keeping the queue near zero. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000078` | Delegate the follow-up cleanup that #1178's "APPROVE WITH NITS" review enumerated. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000079` | Multi-day 75–100 file PRs | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000080` | Nightly qa-automation branch syncs (titled "qa update-DD-MM") | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000081` | Approving promotion PRs within a minute | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000082` | Automate the qa-automation branch sync as a scheduled job (script or Devin) with a generated changelog, removing the manual 454-file PR. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000083` | Use Devin to write smoke tests for the person-creation flow touched by #1235. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000084` | Unfilled PR template on large sync PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000085` | Sub-minute empty approvals on promotions | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000086` | Production promotion PRs assembled manually | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000087` | One-word approvals of 100+ file promotions | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000088` | Devin-generated release notes and risk summary for each production promotion — the PERM/questionnaire release shipped with zero recorded reviewable content. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000089` | Devin smoke-test run against the uat branch before each promotion approval. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000090` | Thin approvals on promotion PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000091` | Unreviewable production PRs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000092` | UAT→prod promotion pairs (same diff, two PRs) | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000093` | Devin-generated tests for the Co-Pilot escalation path (chart finished-but-not-clean states) — the feature shipped without visible new tests. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000094` | Automate the UAT→prod promotion pair creation. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000095` | Merges gated only by 'okay' approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000096` | 'okay' approvals as merge gate | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000097` | HCPCS/coding-rule data changes | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000098` | Devin-generated regression tests for HCPCS/ophthalmology rule changes — #392 shipped with a post-merge Devin Review finding and no visible tests. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000099` | Continue the Devin-trailer workflow he already uses; extend it to the rule-change PRs. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000100` | 'okay' approvals on every engine merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000101` | Self-merge after bare peer approval | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000102` | Direct config-change PRs to the prod release branch | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000103` | Devin validation pass on config PRs: diff each key against dev/uat values and flag unexplained production-only changes. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000104` | Prod-branch changes merged in minutes on bare approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000105` | Closing and re-opening near-identical PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000106` | Mega-PRs mixing KB, MCP, UI concerns | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000107` | Use Devin to split the next KB/MCP wave into scoped PRs (backend API, MCP domain, UI) — the mechanical separation is well-defined. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000108` | Delegate Devin Review finding resolution on his PRs before requesting merge. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000109` | Duplicate/re-opened PRs instead of updating in place | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000110` | 100–226 file PRs merged on empty approvals | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000111` | Empty-body approvals as sole merge gate | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000112` | Manual merge servicing of every app-team PR | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000113` | Use Devin as a structured pre-merge reviewer on the PRs where he is the only human gate — he merged 356 files of hitesh's work today with no recorded review con | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000114` | Resume the Devin-assisted development workflow observed on 08-21 for his own endpoint work. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000115` | Empty-body approvals on all merges | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000116` | dev→uat sync PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000117` | 'lgtm' approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000118` | Devin-generated tests for the impersonation/session-management path (#564/#490) — security-sensitive functionality merged with no visible new tests. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000119` | Automate the dev→uat sync PRs. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000120` | Manual dev→uat sync PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000121` | Manually porting the same fix across branches and repos | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000122` | Delegate branch/repo porting to Devin: one session per fix, opening the dev and prod PRs from a single source change. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000123` | Duplicate manual porting of fixes | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000124` | Failure-reason/migration doc updates | AUTOMATION_OPPORTUNITY | medicodio-nextgen-integration | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000125` | Devin-generated tests for the event-driven batch-run fan-out — 68 files of pipeline logic merged with an unresolved finding. | MISSING_TEST | medicodio-nextgen-integration | — | — | — | CODE_CHANGE |
| `ISSUE_000126` | Extend the Devin-assisted docs/migration workflow he used today to the failure-taxonomy updates he makes regularly. | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000127` | Self-merge with only a bare approval, findings pending | PROCESS_PRACTICE | medicodio-nextgen-integration | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000128` | Insufficient data | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000129` | — | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.
