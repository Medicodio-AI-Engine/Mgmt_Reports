# Employee Rating Cards — Review Day 2026-08-21 (UTC)

Scale: 1 = low, 10 = high. Scores are derived only from activity observable in GitHub for 2026-08-21, with 2026-08-20, 2026-08-14 → 08-20 and 2026-07-22 → 08-20 as the comparison windows.

**Scoring limitations (read before using these numbers).**

1. Devin session telemetry was not retrievable (`devin_session_search` → HTTP 403, *Missing required permission 'org.sessions.view'*). The Devin dimension therefore rates only observable leverage — bot-authored PRs, `Co-Authored-By: Devin AI` commit trailers, and Devin Review follow-through. A low score means no leverage was visible, not that none occurred.
2. Jira was unavailable (no tool exposed), so nothing here is scored against planned scope.
3. Only one previous run of this report is retrievable (2026-08-20). Its card set is used as a qualitative reference for repeat behaviour, not as a numeric baseline — the two runs used different collection windows, so score-to-score deltas are not published.
4. These are ratings of one review day against its own comparison windows, **not performance appraisals**. Volume (commits, PRs, approvals) is never scored as productivity by itself.
5. NR = not rated: no evidence was observed for that dimension, so it is excluded from the weighted average instead of being scored low. Confidence flags how much data backed the card.
6. Review and PR-comment events were collected only for PRs updated 2026-08-20 → 08-21, so review depth on older PRs is undercounted — this is why several Review scores are NR rather than low.

## Rubric

| Dimension | Weight | 1-3 | 4-5 | 6-7 | 8-10 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25% | Work opened but stalls | Lands with gaps | Scoped work merged | Complete, merged, self-contained |
| Engineering Rigor (tests, docs, safety) | 25% | Risky changes with no test or description | Thin evidence on sensitive paths | Tests or docs where risk warrants | Tests + provenance on the risky surface |
| Code Review Contribution | 15% | Empty or one-word approvals | Volume without depth | Some substantive findings | Findings that change the outcome |
| Observable Devin Leverage | 15% | Clear candidates all hand-done | Adjacent AI use only | Partial or indirect leverage | Scoped session with reviewed, landed output |
| Automation of Repetitive Work | 10% | High-volume manual repetition | Repetition acknowledged, unaddressed | Some scripted or generated output | Repetition removed at the source |
| Consistency Across Windows | 10% | One-off spike or drop-off | Uneven | Steady with the week and month | Steady at depth across all windows |

Bands: **Solid** ≥ 7.0 · **Mixed** 5.0 – 6.9 · **Needs Support** < 5.0 · **Not rated** when no dimension could be scored.

## Summary Grid

| # | Member | Product | Overall (1-10) | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | akanksh-rv | Global Codio | 7.7 | Solid | 8 | 7 | 9 | 7 | 7 | 8 | High |
| 2 | SaijyotiMeti | Global Codio | 7.4 | Solid | 8 | 9 | 8 | 5 | 4 | 8 | High |
| 3 | ragha82 | Global Codio | 7.0 | Solid | 8 | 7 | NR | 4 | 9 | 7 | High |
| 4 | anirudh-medicodio | Global Codio | 6.7 | Mixed | 8 | 8 | 6 | 4 | 4 | 8 | High |
| 5 | shaheen-khan11 | Medicodio | 6.3 | Mixed | 8 | 6 | NR | 4 | NR | NR | Low |
| 6 | ashwinsk-medicodio | Medicodio | 6.1 | Mixed | 8 | 6 | NR | 4 | 4 | 7 | Medium |
| 7 | svh-medicodio | Global Codio | 6.0 | Mixed | 6 | NR | NR | NR | NR | NR | Low |
| 8 | amit-pandey-medicodio | Medicodio | 5.9 | Mixed | 8 | 4 | 3 | 8 | 5 | 7 | High |
| 9 | Medicodio-Amit | Medicodio | 5.9 | Mixed | 6 | 7 | NR | 4 | NR | NR | Low |
| 10 | sameer-s-mansur | Medicodio | 5.8 | Mixed | 8 | 5 | NR | 4 | 4 | 7 | Medium |
| 11 | jatinkushwaha-medicodio | Medicodio | 5.6 | Mixed | 8 | 5 | 4 | 4 | 3 | 8 | High |
| 12 | hiteshjrxmedicodio | Medicodio | 5.3 | Mixed | 5 | 7 | NR | 4 | 4 | NR | Medium |
| 13 | Shashvi1 | Medicodio | 5.0 | Mixed | 6 | 4 | NR | NR | NR | NR | Low |
| 14 | avinash-codio | Medicodio | 4.9 | Needs Support | 8 | 3 | 3 | 4 | 4 | 7 | High |
| 15 | vishnu-saikarthik | Medicodio | 4.8 | Needs Support | 7 | 3 | NR | 4 | NR | 5 | Medium |
| 16 | NandanDate-Medicodio | Medicodio | 4.6 | Needs Support | 6 | 4 | 3 | 4 | 4 | 6 | High |
| 17 | SaahilVishwakarma | Global Codio | 4.5 | Needs Support | 4 | 5 | NR | NR | NR | NR | Low |
| 18 | Murali-Shetty19 | Medicodio | 2.5 | Needs Support | 3 | 2 | NR | NR | NR | NR | Low |

## Cards

### akanksh-rv — 7.7 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #1195 (QA PERM wage classification, positions, recruitment) merged; 5 remediation PRs (#1201, #1203, #1205, #1206, #1207) merged the same day; #1209 opened for the Devin PR |
| Engineering Rigor (tests, docs, safety) | 7 | Remediation PR bodies separate behaviour-preserving edits from the two genuine correctness bugs found; no test commits of his own observed on the day |
| Code Review Contribution | 9 | The day's deepest reviewer: 5 review events + 15 comments, including a detailed architect/EM review of the Devin-authored #1208 |
| Observable Devin Leverage | 7 | No Devin session of his own, but the strongest observed human validation of Devin output on the day, with a remediation PR opened against it |
| Automation of Repetitive Work | 7 | The `/check` → `/fix` → `/pr-review` routine now produces the remediation PRs that used to be hand-written; still re-runs per red verdict rather than being prevented by lint |
| Consistency Across Windows | 8 | Steady feature + remediation mix through the week window |

### SaijyotiMeti — 7.4 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 36 commits closing out the AI paralegal Case Manager branch (merged as #1189) plus the #1193 payment-sweep fix; #1194 reviewed and approved |
| Engineering Rigor (tests, docs, safety) | 9 | RLS added to two request-path reads, mailbox addresses removed from `audit_logs`, proposal edits audited, P2002 race mapped to 409, four test commits, `/enums` ts-jest mapping fixed so type-checking actually runs |
| Code Review Contribution | 8 | 4 review events with substantive bodies, including the architect/EM approval of #1194 |
| Observable Devin Leverage | 5 | No Devin session or trailer of her own; 33 of 36 commits are Claude-assisted. The token/enum/catalog sweeps were Good Devin Candidates done by hand |
| Automation of Repetitive Work | 4 | 5 hand-written `docs(review-logs)` commits plus 3 branch-sync merges — mechanical gate output still typed manually |
| Consistency Across Windows | 8 | Largest sustained committer in `globalcodio-monorepo` across the week and month windows, with the same fix-plus-test shape |

### ragha82 — 7.0 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #1196 and #1199 merged (fixed-matrix CI gate, sharded tests, review-fix routine firing on PRs into `dev`, auto-merge on green); #1204 opened with the pnpm root cause |
| Engineering Rigor (tests, docs, safety) | 7 | Documented the gate-and-merge loop and the `/ship` command, cut api-test wall clock ~4x while fixing TS2307; deleted his own gate-manifest abstraction once `ci.yml` sufficed |
| Code Review Contribution | NR | No review events observed on PRs in the collection window |
| Observable Devin Leverage | 4 | No Devin artifact; CI gate design is defensibly human-owned, but the post-consolidation cleanup was delegable |
| Automation of Repetitive Work | 9 | Removed repetition at the source: gate bookkeeping became CI, merges became auto-merge-on-green, install failures now fail loudly instead of surfacing as `nx not found` |
| Consistency Across Windows | 7 | CI reliability work compounding across the week window |

### anirudh-medicodio — 6.7 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 16 commits; merged #1199 and #1175; opened #1202 (GC PERM case-manager parity) and carried it through two remediation rounds |
| Engineering Rigor (tests, docs, safety) | 8 | §2.36 firm-scoping invariant pinned in a spec, agency-header specs made falsifiable, ISO-2 leak dropped, comments no longer asserting guarantees the code does not give, function headers added |
| Code Review Contribution | 6 | Substance is real but lands off-PR: architect+EM review log with REQUEST CHANGES on two decisions and a 38-finding cycle-2 log, while all 3 GitHub approvals had empty bodies |
| Observable Devin Leverage | 4 | No Devin artifact; the enumerated QA fix-list items (empty states, pagination, humanizer) are textbook delegable work done by hand |
| Automation of Repetitive Work | 4 | 3 hand-written review-log commits and 2 branch-sync merges |
| Consistency Across Windows | 8 | Steady reviewer/implementer role across the week and month windows |

### shaheen-khan11 — 6.3 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #489 merged into `release/prod_1.0` — nginx `client_max_body_size` raised so bulk PDF upload stops failing at 30 files |
| Engineering Rigor (tests, docs, safety) | 6 | PR body diagnoses the 413 at the proxy layer and states the sizing rationale relative to the app limit; no automated boundary test |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | 4 | No Devin artifact; a production infra limit is defensibly human-owned, though the boundary test is delegable |
| Automation of Repetitive Work | NR | No repetition observed on the day |
| Consistency Across Windows | NR | Insufficient data for comparison |

### ashwinsk-medicodio — 6.1 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #379 merged (Z32 parameter-based prediction, `urine_hcg_result` extraction parameter, 3 specialty guidelines) and promoted to `release/prod_3.0` via #380 |
| Engineering Rigor (tests, docs, safety) | 6 | Docs shipped in the same branch as the guideline change; no fixture or regression test for a change that alters coded output |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | 4 | No Devin artifact; the guideline judgment is his, but generating the fixture set from his own doc is a clear delegation |
| Automation of Repetitive Work | 4 | Guideline + doc + promotion PR repeated per change, all manual |
| Consistency Across Windows | 7 | Steady engine guideline contributions across the week window |

### svh-medicodio — 6.0 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | #1175 (`fix/qa-dev-fix-lists`) merged on the review day after an architect+EM review round |
| Engineering Rigor (tests, docs, safety) | NR | No commits authored by this member observed on the review day |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | NR | No evidence observed |
| Automation of Repetitive Work | NR | No evidence observed |
| Consistency Across Windows | NR | Insufficient data for comparison |

### amit-pandey-medicodio — 5.9 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | The RPA Job Scheduler ops dashboard landed end-to-end (#555 backend, #484 frontend, both merged); workspace-module PRs #560, #561, #486 merged; prediction-trail description precedence shipped |
| Engineering Rigor (tests, docs, safety) | 4 | No tests observed on a new dashboard feature; both Devin PRs merged with Devin Review findings posted and no human approval recorded; a self-revert inside the session |
| Code Review Contribution | 3 | 6 approvals on the day, all with empty bodies |
| Observable Devin Leverage | 8 | The day's clearest Devin leverage: 17 `Co-Authored-By: Devin AI` commits across backend and frontend producing a merged, user-visible feature |
| Automation of Repetitive Work | 5 | Real delegation of feature work, offset by manual `Dev_1.0` sync merges, four same-titled `Refactor/workspace module` PRs and a manual UAT→prod promotion (#559) |
| Consistency Across Windows | 7 | The only member with sustained Devin-delivered work in the week window |

### Medicodio-Amit — 5.9 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | #384 opened (new E&M management-option schema: one `drugs[]` list per diagnosis with `drug_type`, `is_drug_mgmt`, `is_diet_mgmt`); still open at end of day |
| Engineering Rigor (tests, docs, safety) | 7 | PR body specifies the exact payload change and the gating flags — the clearest engine PR description on the review day; no consumer-migration checklist or test evidence |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | 4 | No Devin artifact; migrating downstream consumers to the unified shape is delegable |
| Automation of Repetitive Work | NR | No repetition observed on the day |
| Consistency Across Windows | NR | Insufficient data for comparison |

### sameer-s-mansur — 5.8 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #226 merged (Trinity ADDENDUM captured into `description_of_procedure`) and promoted to `release/prod_1.0` via #227 |
| Engineering Rigor (tests, docs, safety) | 5 | Client-scoped extraction change with a descriptive branch name but no fixture test; promotion PR carried no description |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | 4 | No Devin artifact; per-client extraction fixtures are a well-bounded delegation |
| Automation of Repetitive Work | 4 | OPS alert recipients still edited in code; per-client parser tweaks repeated manually |
| Consistency Across Windows | 7 | Steady integration-side contributions across the week window |

### jatinkushwaha-medicodio — 5.6 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | Import-batch sweep cron + batch-run handling (#556), ICD flag codes F060/F061 (#557, #558), MFA `SetupLoader` (#485) — all merged |
| Engineering Rigor (tests, docs, safety) | 5 | Good domain rationale in PR bodies and a new auth/authz context document, but a cron that silently ages batches to `import_failed` merged with no observed test; one duplicated commit |
| Code Review Contribution | 4 | 6 approvals with bodies `lgtm` / `okok` / `lgtm` |
| Observable Devin Leverage | 4 | No Devin artifact; the sweep job, the flag-code registry change and the cross-branch port are all Good Devin Candidates |
| Automation of Repetitive Work | 3 | The identical ICD flag-code change was hand-ported to a second branch as its own PR |
| Consistency Across Windows | 8 | Steady scoped backend delivery across the week and month windows |

### hiteshjrxmedicodio — 5.3 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | Two large paired PRs opened (#562 backend, #488 frontend) replacing the closed #545/#471; nothing merged on the day |
| Engineering Rigor (tests, docs, safety) | 7 | The rework addresses the objection that closed the earlier PRs — no migration now contains data; PR bodies state what they replace and the required merge order |
| Code Review Contribution | NR | Two PR comments observed, no review verdicts |
| Observable Devin Leverage | 4 | No Devin artifact; slicing the mega-PRs and verifying the no-data-in-migrations invariant are both delegable |
| Automation of Repetitive Work | 4 | The whole workstream is being resubmitted by hand rather than sliced |
| Consistency Across Windows | NR | Insufficient data for comparison |

### Shashvi1 — 5.0 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | #377 (linking removal after chain) merged on the review day |
| Engineering Rigor (tests, docs, safety) | 4 | A coding-behaviour change merged on two one-word approvals with Devin Review findings posted and no observed test |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | NR | No evidence observed |
| Automation of Repetitive Work | NR | No evidence observed |
| Consistency Across Windows | NR | Insufficient data for comparison |

### avinash-codio — 4.9 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | #385 merged (laterality module enabled for ophthalmology) and #378 promoted UAT → `release/prod_3.0` |
| Engineering Rigor (tests, docs, safety) | 3 | Both PRs carried no description beyond the review badge; no test on a change that alters coded output |
| Code Review Contribution | 3 | 1 approval with the body `ok`, on an engine change affecting coding behaviour |
| Observable Devin Leverage | 4 | No Devin artifact; a specialty × config matrix test is a one-off delegation that would cover every future enablement |
| Automation of Repetitive Work | 4 | Per-specialty config enablement and promotion PRs repeated manually |
| Consistency Across Windows | 7 | Steady engine config contributions across the week window |

### vishnu-saikarthik — 4.8 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | #381 merged (additional-code LLM update for the gastro E&M flow) |
| Engineering Rigor (tests, docs, safety) | 3 | An LLM behaviour change landed with the title "feat:Updated llm of additional code llm", no description and no recorded before/after evaluation |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | 4 | No Devin artifact; a prompt-regression harness is exactly the bounded, repeatable work Devin handles well |
| Automation of Repetitive Work | NR | No repetition observed on the day |
| Consistency Across Windows | 5 | Single change on the day; thin week-level signal |

### NandanDate-Medicodio — 4.6 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | Claim-line splitting and `.md` updates authored; 6 engine PRs promoted through merge commits; #383 opened and merged |
| Engineering Rigor (tests, docs, safety) | 4 | #383 shipped as "Feat/addressed seq" with no description; no test evidence on the guideline changes he gates |
| Code Review Contribution | 3 | 7 approvals, all with the single-word body "okay"; five of them on PRs where Devin Review had posted findings |
| Observable Devin Leverage | 4 | No Devin artifact; the engine regression suite that would replace his manual gate is the team's highest-value delegation |
| Automation of Repetitive Work | 4 | Six merge-only promotion commits in one day, all manual |
| Consistency Across Windows | 6 | Consistently available as the engine gate, at consistently one word of recorded review |

### SaahilVishwakarma — 4.5 / 10 (Needs Support)

**Product:** Global Codio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | #1200 (GC PERM case-manager parity) opened, remediated by #1201, then closed; the work continued as another member's #1202 on the same branch |
| Engineering Rigor (tests, docs, safety) | 5 | PR used the repository template; no test evidence observed and the review history did not carry over to the successor PR |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | NR | No evidence observed |
| Automation of Repetitive Work | NR | No evidence observed |
| Consistency Across Windows | NR | Insufficient data for comparison |

### Murali-Shetty19 — 2.5 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 3 | `nextgen-codio-engine#382` "Testing ortho" opened into `uat` and still open at end of day; no commits observed |
| Engineering Rigor (tests, docs, safety) | 2 | No description beyond the review badge, so neither the intent nor the coding impact can be determined from the PR record |
| Code Review Contribution | NR | No review events observed |
| Observable Devin Leverage | NR | No evidence observed |
| Automation of Repetitive Work | NR | No evidence observed |
| Consistency Across Windows | NR | Insufficient data for comparison |

## How to read the spread

**Observed Fact:** delivery again does not separate the cards — 33 of 37 same-day PRs merged and every day-active member landed something. The spread comes from rigor and review depth. Every score below 5 traces to the same three things: an empty PR body, a one-word approval, or a change to clinical-coding output merged without a test — and the three coincide most often in `nextgen-codio-engine`, where seven PRs affecting coded output merged on "okay"/"ok" approvals with Devin Review findings posted on five of them.

**Inference:** the two weakest team-wide dimensions remain structural rather than individual — Observable Devin Leverage (mean 4.6 across rated cards) and Automation of Repetitive Work (mean 4.7). Promotion PRs, cross-branch ports, review-log transcription and per-specialty config bumps are unowned process work, so no single engineer is positioned to remove them. Two members did remove repetition at the source on this day (ragha82 via CI gates and auto-merge, akanksh-rv via the remediation routine), which is why they top the grid despite neither running a Devin session. Devin leverage itself is real but concentrated in one person (amit-pandey-medicodio), and the same day's Devin PRs merged with no recorded human approval — leverage and control moved in opposite directions.

**Recommendation:** keep the Devin and Automation columns as team targets owned by the leads, and use the Rigor and Review columns for individual coaching — starting with a recorded pre-merge check on `nextgen-codio-engine`, where one-word approvals and open Devin Review findings coincide, and with a required human approval on AI-authored PRs now that auto-merge-on-green is live. Two runs of this card set now exist; the behaviours that repeated from 2026-08-20 (one-word approvals, merges without recorded approval, promotion-PR volume) are recorded as Repeat Patterns in the day's report, but the numeric scores are not yet a trend line.

---

*MediCodio AI © 2026. All Rights Reserved · www.medicodio.ai*
