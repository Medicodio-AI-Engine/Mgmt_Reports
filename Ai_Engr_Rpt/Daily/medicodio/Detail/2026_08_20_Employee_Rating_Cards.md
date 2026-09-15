# Employee Rating Cards — Review Day 2026-08-20 (UTC)

Scale: 1 = low, 10 = high. Scores are derived only from activity observable in GitHub for 2026-08-20, with 2026-08-19, 2026-08-13 -> 19 and 2026-07-21 -> 08-19 as the comparison windows.

**Scoring limitations (read before using these numbers).**

1. Devin session telemetry was not retrievable (`devin_session_search` -> HTTP 403, *Missing required permission 'org.sessions.view'*). The Devin dimension therefore rates only observable leverage — bot-authored PRs with session links, `Co-Authored-By: Devin` trailers, and Devin Review follow-through. A low score means no leverage was visible, not that none occurred.
2. No previous run of this report is retrievable through the session API, so no score reflects a trend against a prior rating. The 2026-08-19 card set supplied by management is used only as a format reference, not as a scoring baseline, because it was produced from a differently-scoped data pull.
3. These are ratings of one review day against its own comparison windows, not performance appraisals. Volume (commits, PRs, approvals) is never scored as productivity by itself.
4. NR = not rated: no evidence was observed for that dimension, so it is excluded from the weighted average instead of being scored low. Confidence flags how much data backed the card.
5. Review and PR-comment events were collected only for PRs updated 2026-08-19 -> 08-21, so review depth on older PRs is undercounted; month-level review counts were not available for this run, which is why several Review scores are NR rather than low.

## Rubric

| Dimension | Weight | 1-3 | 4-5 | 6-7 | 8-10 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25% | Work opened but stalls | Lands with gaps | Scoped work merged | Complete, merged, self-contained |
| Engineering Rigor (tests, docs, safety) | 25% | Risky changes with no test or description | Thin evidence on sensitive paths | Tests or docs where risk warrants | Tests + provenance on the risky surface |
| Code Review Contribution | 15% | Empty or one-word approvals | Volume without depth | Some substantive findings | Findings that change the outcome |
| Observable Devin Leverage | 15% | Clear candidates all hand-done | Adjacent AI use only | Partial or indirect leverage | Scoped session with reviewed, landed output |
| Automation of Repetitive Work | 10% | High-volume manual repetition | Repetition acknowledged, unaddressed | Some scripted or generated output | Repetition removed at the source |
| Consistency Across Windows | 10% | One-off spike or drop-off | Uneven | Steady with the week and month | Steady at depth across all windows |

## Summary Grid

| # | Member | Product | Overall (1-10) | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SaijyotiMeti | Global Codio | 7.8 | Solid | 8 | 9 | 9 | 6 | 5 | 8 | High |
| 2 | anirudh-medicodio | Global Codio | 6.8 | Mixed | 9 | 8 | 5 | 4 | 4 | 8 | High |
| 3 | akanksh-rv | Global Codio | 6.8 | Mixed | 8 | 7 | 7 | 5 | 4 | 8 | High |
| 4 | Medicodio-Amit | Medicodio | 6.6 | Mixed | 7 | 7 | NR | 7 | 4 | 7 | High |
| 5 | Shashvi1 | Medicodio | 6.5 | Mixed | 7 | 8 | NR | 5 | 4 | NR | Low |
| 6 | jatinkushwaha-medicodio | Medicodio | 5.7 | Mixed | 8 | 5 | 4 | 4 | 4 | 8 | High |
| 7 | sameer-s-mansur | Medicodio | 5.6 | Mixed | 7 | 4 | NR | 5 | 5 | 8 | High |
| 8 | vishnu-saikarthik | Medicodio | 5.6 | Mixed | 7 | 5 | NR | 4 | NR | 6 | Medium |
| 9 | ragha82 | Global Codio | 5.3 | Mixed | 6 | 5 | NR | 5 | 3 | 7 | Medium |
| 10 | amit-pandey-medicodio | Medicodio | 5.2 | Mixed | 7 | 4 | 3 | 7 | 2 | 7 | High |
| 11 | avinash-codio | Medicodio | 5.2 | Mixed | 8 | 3 | NR | 4 | 4 | 7 | High |
| 12 | ANANYANG8055 | Medicodio | 5.2 | Mixed | 7 | 5 | NR | 4 | 3 | NR | Low |
| 13 | Amrutha-Beedikar | Global Codio | 5.1 | Mixed | 6 | 5 | NR | 4 | 3 | 7 | Medium |
| 14 | NandanDate-Medicodio | Medicodio | 4.8 | Needs Support | 6 | 4 | 3 | 5 | 5 | 6 | High |
| 15 | shaheen-khan11 | Medicodio | 4.8 | Needs Support | 6 | 5 | 4 | 4 | 4 | 5 | Medium |
| 16 | sumedh-codio | Medicodio | NR | Not rated | NR | NR | 3 | NR | NR | NR | Low |

## Cards

### SaijyotiMeti — 7.8 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 24 commits closing out `fix/qa-codioops-rls-and-stale-reads` (merged as #1188) plus the #1194 remediation; 1 PR opened and merged on the day |
| Engineering Rigor (tests, docs, safety) | 9 | `data_scope` enforced on questionnaire lock/approve/revisions/lineage, partial unique index so a closed follow-up goal can re-open, 2 payments test commits, 9 review-log/doc commits |
| Code Review Contribution | 9 | The day's deepest review: architect + EM APPROVE verdict on #1194 grounded in the CodioOps PRD; 4 of 5 review events carried substantive bodies |
| Observable Devin Leverage | 6 | No Devin session of her own on the review day; Devin Review's finding on #1194 was verified and consumed, and she requested Devin PR #1176 inside the week window |
| Automation of Repetitive Work | 5 | Review-log, standards-audit and gate-ledger commits (9 on the day) are mechanical gate output still written by hand |
| Consistency Across Windows | 8 | 56 commits in the week / 368 in the month with the same fix-plus-test-plus-review-log shape |

### anirudh-medicodio — 6.8 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 9 | Largest delivery stream in the day's data: 55 commits, two feature branches landed (#1172 PERM wage classification, #1174 assignable HR contacts) |
| Engineering Rigor (tests, docs, safety) | 8 | Security-relevant fixes carried evidence: RLS applied on dev/UAT deploy paths, firm-scoped audit rows no longer written platform-global, PII scrubber made to reach the PII, 5 test commits; offset by ~5 commits repairing type/test breakage his own review pass introduced |
| Code Review Contribution | 5 | 3 approvals on the day, all with empty bodies — his review depth lands in commit-level remediation and review-log files, not in the PR conversation |
| Observable Devin Leverage | 4 | No Devin-authored PR or co-author trailer; 51 of 55 commits are Claude-assisted. The error-code/stable-code sweep and the DTO header refresh were Good Devin Candidates done by hand |
| Automation of Repetitive Work | 4 | 11 hand-written `docs(review-logs)` commits on the day (139 in the month) that are mechanical outputs of a gate run |
| Consistency Across Windows | 8 | 175 commits in the week / 606 in the month at the same mix — steady at high volume |

### akanksh-rv — 6.8 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #1176 CodioOps questionnaire agent merged, payment-sweep attempt stamping and the payment step-card fixes landed; 3 PRs opened, 2 merged |
| Engineering Rigor (tests, docs, safety) | 7 | Ships gate evidence with each change and added a sweep-pass test, but only 1 test commit against 12 on the day and 9 against 256 in the month |
| Code Review Contribution | 7 | Only human besides SaijyotiMeti to post substantive review content: two automated QA-validation verdict tables on ragha82's sync PRs #1191/#1192 |
| Observable Devin Leverage | 5 | No Devin session; Devin Review outcomes consumed on his branches. The per-sync QA validation report he writes by hand is a scoped, repeatable delegation |
| Automation of Repetitive Work | 4 | The QA validation report is regenerated per sync manually; 5 review-log commits on the day |
| Consistency Across Windows | 8 | 72 commits in the week / 256 in the month with a steady feature-plus-remediation mix |

### Medicodio-Amit — 6.6 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | Model pricing read from `t_kb_model_pricing` with tiered rates keyed on provider+model shipped and merged (#374) |
| Engineering Rigor (tests, docs, safety) | 7 | Right structural call (hardcoded `MODEL_PRICING` dict removed rather than extended) and the cost-tracking docs were corrected in the same day off a Devin Review finding; no test commit on the day |
| Code Review Contribution | NR | No review events observed on the review day |
| Observable Devin Leverage | 7 | Requested Devin PR #373 (PHI-safe Sentry monitoring on the engine) and landed a Devin-Review-driven docs fix with a `Co-Authored-By: Devin` trailer — but #373 was still an open draft at day end |
| Automation of Repetitive Work | 4 | The remaining hardcoded-table-to-DB-config modules and the UAT promotion are still hand-driven |
| Consistency Across Windows | 7 | 16 commits in the week / 80 in the month, stable |

### Shashvi1 — 6.5 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | `linking_removal` moved to run once after the whole chain for IM E&M, plus the client-config enable; PR #377 merged |
| Engineering Rigor (tests, docs, safety) | 8 | One of only two day-active members to ship a behaviour change with its own test (`test(linking): cover the deferred linking_removal phase`) and a non-empty PR body |
| Code Review Contribution | NR | No review events observed in any window |
| Observable Devin Leverage | 5 | No Devin session; enabling the same flag for the remaining specialties is a scoped repeatable candidate, and Devin Review's finding on #377 was merged unaddressed on an `okay` approval |
| Automation of Repetitive Work | 4 | The per-specialty config-flag enable repeats by hand across the engine's client configs |
| Consistency Across Windows | NR | Insufficient data for comparison — 5 commits in the month, no prior-day activity |

### jatinkushwaha-medicodio — 5.7 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 8 PRs opened and all 8 merged across react and nodejs: email-OTP login flow, MCP redirect-URI allowlist for the OAuth 2.1 PKCE flow, atomic OTP attempt increment, cursor-pagination duplicate-row fix, access-request expiry cron |
| Engineering Rigor (tests, docs, safety) | 5 | Auth, OTP and redirect-validation changes landed with zero test commits on the day; 5 of 8 PR bodies empty; #554 merged the same day Devin Review reported 3 potential issues |
| Code Review Contribution | 4 | 11 approvals on the day, all thin (`lgtm`, `Ok`, empty) |
| Observable Devin Leverage | 4 | No Devin evidence; the OTP/pagination regression suite and the `t_sys_report_types -> t_kb_report_types` rename sweep are both clearly scoped candidates |
| Automation of Repetitive Work | 4 | Paired react+nodejs changes and rename sweeps applied by hand across both repos |
| Consistency Across Windows | 8 | 41 commits in the week / 75 in the month with 19 and 35 PRs merged — steady |

### sameer-s-mansur — 5.6 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | Two client-integration changes merged: Valley Impression/Plan diagnosis-block split into pre/post-op plus impression, and the final Elaris registration-export format |
| Engineering Rigor (tests, docs, safety) | 4 | Both PRs had empty descriptions (19 of 31 in the month) and no tests, on parsers whose output feeds clinical coding; Devin Review reported no issues on either |
| Code Review Contribution | NR | No review events observed in any window |
| Observable Devin Leverage | 5 | No Devin evidence in 144 monthly commits; per-client parser/export variants from a reference client are the clearest untouched delegation in Medicodio |
| Automation of Repetitive Work | 5 | Client-by-client extraction and export work repeats per client (Valley, Elaris, Apex) with no shared contract tests |
| Consistency Across Windows | 8 | 30 commits in the week / 144 in the month with a consistent per-client feature mix |

### vishnu-saikarthik — 5.6 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | GGL-034 landed and merged (#372): all deduped CPT procedure phrases now sent to the laterality prompt |
| Engineering Rigor (tests, docs, safety) | 5 | Non-empty PR body, but no test for a prompt-input change that affects laterality assignment, and the PR merged with one open Devin Review finding on an `okay` approval |
| Code Review Contribution | NR | No review events observed in any window |
| Observable Devin Leverage | 4 | No Devin evidence in 13 monthly commits; laterality regression fixtures are an obvious bounded delegation |
| Automation of Repetitive Work | NR | Insufficient data for comparison |
| Consistency Across Windows | 6 | 6 commits in the week / 13 in the month — low but consistent volume on narrow, scoped changes |

### ragha82 — 5.3 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | Two `dev -> feat/qa-automation` QA sync PRs merged (#1191 questionnaire, #1192 enabling HR); no commits authored on the day |
| Engineering Rigor (tests, docs, safety) | 5 | Sync-and-validate work with no test or doc output; both PRs merged with the automated QA comment and Devin Review clean, but no human approval recorded |
| Code Review Contribution | NR | No review events observed on the review day |
| Observable Devin Leverage | 5 | Devin Review consumed on both syncs; no session-level or delegated work visible |
| Automation of Repetitive Work | 3 | The dev-to-QA sync-and-validate cycle ran 22 times in the month, entirely by hand |
| Consistency Across Windows | 7 | 7 commits in the week / 21 in the month, 22 PRs merged in the month at a constant rate |

### amit-pandey-medicodio — 5.2 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | 12 PRs opened, 11 merged; the two prompt-config correctness fixes (single section-action error banner, inherited sequence via fallback chain only) landed on both repos |
| Engineering Rigor (tests, docs, safety) | 4 | 12 of 12 PR bodies empty (51 of 90 in the month) and no tests with the prompt-config fixes — on a config-resolution path the PR body is the only provenance record |
| Code Review Contribution | 3 | 10 approvals on the day, every one with an empty body, including PRs where Devin Review had open findings |
| Observable Devin Leverage | 7 | Strongest observable delegation of the day: the two ops-dashboard Devin PRs (#484 react, #555 nodejs) landed under his authorship with `Co-Authored-By: Devin`, one carrying a browser-verified runtime test comment — capped because both merged with no second human approval |
| Automation of Repetitive Work | 2 | 8 of his 12 PRs on the day are `dev -> UAT` promotion pairs; ~35 such pairs a month, all hand-opened |
| Consistency Across Windows | 7 | 59 commits in the week / 185 in the month / 90 PRs in the month at an unchanged rate |

### avinash-codio — 5.2 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 5 PRs opened and all 5 merged: podiatry and Elaris copilot routing configs, G2210/KX modifier and NaN fixes, ortho config changes |
| Engineering Rigor (tests, docs, safety) | 3 | 4 of 5 PR bodies empty (45 of 66 in the month), commit subjects like `excel changes` and `config changes ortho`, no tests on billing-rule and modifier changes, and #375/#376 each merged with an open Devin Review finding |
| Code Review Contribution | NR | No review events observed on the review day |
| Observable Devin Leverage | 4 | No Devin evidence in 66 monthly commits; specialty config rollout plus a config-diff/consistency test is a textbook delegation |
| Automation of Repetitive Work | 4 | 66 PRs in the month, largely mechanical specialty-config rollouts, none generated or templated |
| Consistency Across Windows | 7 | 22 commits in the week / 66 in the month — consistent rate, and the documentation gap is consistent rather than worsening |

### ANANYANG8055 — 5.2 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | gastro_op / vital_gastro_op CPT modules bumped to gpt-5.4 with gpt-5.4 and gpt-5.5 pricing added; PR merged |
| Engineering Rigor (tests, docs, safety) | 5 | Config-and-pricing bump with a descriptive body but no test or verification note attached; 1 commit on the day |
| Code Review Contribution | NR | No review events observed in any window |
| Observable Devin Leverage | 4 | No Devin evidence; the model-version-and-pricing bump across the remaining specialty configs is a scoped repeatable candidate |
| Automation of Repetitive Work | 3 | Model bumps are applied module-by-module by hand and recur through the month |
| Consistency Across Windows | NR | Insufficient data for comparison — 14 commits in the month, no prior-day activity |

### Amrutha-Beedikar — 5.1 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | One production-update PR merged (follow-up agent, email logo, CodioOps payment) — release coordination rather than authored change; no commits on the day |
| Engineering Rigor (tests, docs, safety) | 5 | No test or doc output on the day; her month record is clean on PR descriptions (0 of 30 empty) |
| Code Review Contribution | NR | No review events observed on the review day |
| Observable Devin Leverage | 4 | No Devin evidence; assembling and describing the production-promotion PR is a bounded, repeatable delegation |
| Automation of Repetitive Work | 3 | 28 of 30 monthly PRs merged are promotion/release PRs, assembled by hand |
| Consistency Across Windows | 7 | 14 commits in the week / 49 in the month, steady |

### NandanDate-Medicodio — 4.8 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | Gatekeeper day: 7 merge commits integrating #357, #366, #367, #369, #370, #372, #375 into the engine; no PR of his own |
| Engineering Rigor (tests, docs, safety) | 4 | Four of the PRs he approved carried open Devin Review findings at merge time (#372, #375, #377 one each, #374 two new) — nothing recorded showing they were triaged |
| Code Review Contribution | 3 | 11 approvals on the day, every one the single word `okay` or empty |
| Observable Devin Leverage | 5 | Consumed Devin Review on every engine PR and landed 6 Devin co-authored commits inside the week window (PR #353), but no session on the review day |
| Automation of Repetitive Work | 5 | The specialty/config fix class recurs and is still merged per-instance with no checklist |
| Consistency Across Windows | 6 | 38 commits in the week / 124 in the month, all merge-integration shaped |

### shaheen-khan11 — 4.8 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | `multi-pdf-dropzone.tsx` moved out of `shared/` into the workspace feature; PR merged |
| Engineering Rigor (tests, docs, safety) | 5 | Structural cleanup in the right direction with a described PR, but no test and no note on which consumers were re-pointed; 4 of 8 monthly PRs empty-bodied |
| Code Review Contribution | 4 | 1 approval on the day with an empty body |
| Observable Devin Leverage | 4 | No Devin evidence; the remaining `shared/ -> feature` file migration is exactly the repetitive pattern migration Devin handles well |
| Automation of Repetitive Work | 4 | The migration is being applied one file at a time by hand |
| Consistency Across Windows | 5 | 10 commits in the week / 30 in the month; the day is a single commit, so the trend is thin |

### sumedh-codio — NR / 10 (Not rated)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No authored commits or PRs observed in any window |
| Engineering Rigor (tests, docs, safety) | NR | No evidence observed |
| Code Review Contribution | 3 | One approval on integration PR #225 with an empty body — the only observable activity |
| Observable Devin Leverage | NR | No evidence observed |
| Automation of Repetitive Work | NR | Insufficient data for comparison |
| Consistency Across Windows | NR | Insufficient data for comparison |

## How to read the spread

**Observed Fact:** delivery is not what separates the cards — every day-active member landed the work they opened, and 39 of the day's 42 PRs merged. The spread comes from rigor and review depth. No card reached 8 on the review day: the highest (7.8) belongs to the one member who attached tests, docs and a substantive review verdict to changes that carried risk; every dimension score below 5 traces to an empty PR body, a one-word approval, or a rule change merged untested — including four engine PRs merged the same day Devin Review flagged findings on them.

**Inference:** the two weakest team-wide dimensions, Automation of Repetitive Work (mean 3.9) and Observable Devin Leverage (mean 4.9), are structural rather than individual. Promotion PR pairs, dev-to-QA sync cycles, review-log commits, per-specialty config bumps and per-client parser variants are unowned process work, so no single engineer is positioned to remove them. Devin leverage on the review day is real but concentrated in two people (amit-pandey-medicodio, Medicodio-Amit).

**Recommendation:** treat the Devin and Automation columns as team targets owned by the leads, and use the Rigor and Review columns for individual coaching — starting with a recorded pre-merge check on `nextgen-codio-engine`, where one-word approvals and open Devin Review findings coincide. Re-score on the next run to turn these into trends; per the analysis rules none of these numbers is a Repeat Pattern yet.

