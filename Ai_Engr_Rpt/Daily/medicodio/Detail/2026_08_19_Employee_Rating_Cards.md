# Employee Rating Cards — Review Day 2026-08-19 (UTC)

**Scale:** 1 = low, 10 = high. Scores are derived only from activity observable in GitHub for 2026-08-19 with the 2026-08-18, 2026-08-12 → 18, and 2026-07-20 → 08-18 comparison windows.

> **Scoring limitations (read before using these numbers).**
> 1. Devin **session** telemetry was not retrievable (`devin_session_search` → HTTP 403, `Missing required permission 'org.sessions.view'`). The Devin dimension therefore rates only *observable* leverage — bot-authored PRs with session links, Devin Review follow-through, and co-author trailers. A low score means *no leverage was visible*, not that none occurred.
> 2. No previous run of this report exists, so no score reflects a trend against a prior rating.
> 3. These are ratings of one review day against its own comparison windows, not performance appraisals. Volume (commits, PRs, approvals) is never scored as productivity by itself.
> 4. `NR` = not rated: no evidence was observed for that dimension, so it is excluded from the weighted average instead of being scored low. **Confidence** flags how much data backed the card.

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
| 1 | SaijyotiMeti | Global Codio | **8.1** | Strong | 8 | 9 | 9 | 8 | 5 | 8 | High |
| 2 | anirudh-medicodio | Global Codio | **7.2** | Solid | 9 | 8 | 8 | 4 | 4 | 8 | High |
| 3 | Amrutha-Beedikar | Global Codio | **7.2** | Solid | 8 | 9 | 8 | 4 | 5 | 7 | High |
| 4 | akanksh-rv | Global Codio | **6.3** | Mixed | 8 | 7 | 5 | 4 | 4 | 8 | High |
| 5 | sameer-s-mansur | Medicodio | **6.2** | Mixed | 8 | 5 | NR | 4 | 6 | 8 | High |
| 6 | Medicodio-Amit | Medicodio | **6.1** | Mixed | 8 | 6 | 6 | 4 | 4 | 7 | High |
| 7 | jatinkushwaha-medicodio | Medicodio | **5.9** | Mixed | 8 | 6 | 4 | 4 | 4 | 8 | High |
| 8 | NandanDate-Medicodio | Medicodio | **5.7** | Mixed | 6 | 5 | 4 | 8 | 5 | 6 | High |
| 9 | ashwinsk-medicodio | Medicodio | **5.5** | Mixed | 7 | 5 | NR | 4 | NR | NR | Low |
| 10 | karthikmed | Medicodio | **5.5** | Mixed | 5 | 7 | NR | 4 | NR | NR | Low |
| 11 | hiteshjrxmedicodio | Medicodio | **5.4** | Mixed | 6 | 6 | NR | 4 | 4 | 6 | Medium |
| 12 | Pj-Vineeth-Kumar | Global Codio | **5.3** | Mixed | 5 | 6 | NR | 5 | 5 | 5 | Medium |
| 13 | ragha82 | Global Codio | **5.2** | Mixed | 6 | 6 | 3 | 5 | 3 | 7 | Medium |
| 14 | avinash-codio | Medicodio | **5.0** | Mixed | 8 | 3 | 3 | 5 | 4 | 7 | High |
| 15 | amit-pandey-medicodio | Medicodio | **4.8** | Needs Support | 7 | 4 | 3 | 5 | 2 | 7 | High |
| 16 | shaheen-khan11 | Medicodio | **4.8** | Needs Support | 7 | 4 | 5 | 3 | 4 | 5 | Medium |
| 17 | SaahilVishwakarma | Global Codio | **4.4** | Needs Support | 5 | 5 | 3 | 4 | NR | NR | Low |

## Cards

### SaijyotiMeti — 8.1 / 10 (Strong)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | 24 commits of security/tenancy and payments fixes on the follow-up-goal branch |
| Engineering Rigor (tests, docs, safety) | 9 | 18 test commits in the month; security- and money-path fixes reasoned through in review |
| Code Review Contribution | 9 | 4 substantive inline findings on #1173; 49 reviews / 63 inline comments in the month with no thin approvals |
| Observable Devin Leverage | 8 | Requested the session behind Devin PR #1176 and landed 3 Devin co-authored commits (08-18) — one of only two clean delegations visible in the data |
| Automation of Repetitive Work | 5 | Batching/N+1 and error-code centralization still done by hand |
| Consistency Across Windows | 8 | 369 commits / 20 merged PRs / 49 reviews across the month, consistent |

### anirudh-medicodio — 7.2 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 9 | 51 commits, promotion PR #1187 opened and merged; largest remediation stream in the day's data |
| Engineering Rigor (tests, docs, safety) | 8 | Tests land on the money/auth surfaces he touched (pay-link test); ADRs, RBAC analysis, tech-debt ledger filed same day; offset by 4 commits repairing his own preceding patches |
| Code Review Contribution | 8 | Deepest review of the day (architect/EM verdict on #1173); 108 reviews and 115 inline comments in the month; 2 of 3 day approvals had empty bodies |
| Observable Devin Leverage | 4 | No Devin-authored PR or co-author trailer; the 25-site error-code sweep and the import-repair commits were Good Devin Candidates done by hand |
| Automation of Repetitive Work | 4 | 7 hand-written docs(review-logs) process commits on the day (49 in the month) that are mechanical outputs of a gate run |
| Consistency Across Windows | 8 | 627 commits / 16 PRs / 108 reviews across the month with the same mix — stable at high volume |

### Amrutha-Beedikar — 7.2 / 10 (Solid)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | PR #1180 shipped end to end: {{file_number}} merge field plus firm-configurable identifier label |
| Engineering Rigor (tests, docs, safety) | 9 | Feature landed with both docs and a test — the only day-active member to do all three in one PR |
| Code Review Contribution | 8 | 13 approvals in the month, none empty or thin — one of two reviewers with no thin-approval instances |
| Observable Devin Leverage | 4 | No Devin evidence; the repeated 'rename a user-facing term across layers' migration is a clear candidate |
| Automation of Repetitive Work | 5 | Cross-layer term migrations still hand-applied |
| Consistency Across Windows | 7 | 45 commits / 30 merged PRs / 14 reviews in the month, steady |

### akanksh-rv — 6.3 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | QA-validation PR #1185 plus validation reports on #1184/#1186; 2 PRs merged; RLS for six tenant tables on day one |
| Engineering Rigor (tests, docs, safety) | 7 | Ships validation evidence with the change, but only 2 test commits against 254 commits in the month |
| Code Review Contribution | 5 | 2 commented reviews on the day; 6 reviews total in the month — low relative to output |
| Observable Devin Leverage | 4 | No Devin-authored PR; the per-sync QA validation report is a scoped, repeatable delegation left undone |
| Automation of Repetitive Work | 4 | Validation report generation repeated per sync by hand |
| Consistency Across Windows | 8 | 84 commits in the week, 254 in the month with a steady feature/fix mix |

### sameer-s-mansur — 6.2 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | Age extraction from PDFs, facility-id filter, and the report-types rename fix — 3 PRs merged |
| Engineering Rigor (tests, docs, safety) | 5 | 3 of 3 PRs had empty descriptions (19 in the month); 4 test commits against 162 commits |
| Code Review Contribution | NR | No reviews observed in any window |
| Observable Devin Leverage | 4 | No Devin evidence; extraction edge-case tests and the catalog-rename follow-through are scoped candidates |
| Automation of Repetitive Work | 6 | Wrote a chart raw-data dump script rather than repeating the extraction by hand — correct tooling instinct |
| Consistency Across Windows | 8 | 162 commits / 32 merged PRs in the month with a consistent feature/fix mix |

### Medicodio-Amit — 6.1 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | Model pricing sourced from t_kb_model_pricing, Gemini promo pricing, thinking-cap config; 4 PRs merged |
| Engineering Rigor (tests, docs, safety) | 6 | Moving hardcoded pricing into DB config is the right structural call; 1 test commit in the month |
| Code Review Contribution | 6 | 12 reviews in the month with 6 carrying comments — above the repo baseline |
| Observable Devin Leverage | 4 | No Devin evidence; the remaining 'hardcoded table -> DB config' modules are a repeatable delegation |
| Automation of Repetitive Work | 4 | UAT promotions still opened by hand |
| Consistency Across Windows | 7 | 81 commits / 17 merged PRs in the month, stable |

### jatinkushwaha-medicodio — 5.9 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | Patient-age handling landed across PHI and schema layers plus the t_sys_report_types -> t_kb_report_types rename; 3 PRs merged |
| Engineering Rigor (tests, docs, safety) | 6 | PHI-layer change with no test commits on the day; refactor commits are clean and scoped |
| Code Review Contribution | 4 | 5 approvals on the day at thin depth; 39 in the month |
| Observable Devin Leverage | 4 | No Devin evidence; the table/label rename sweep and the age-field regression tests are both scoped candidates |
| Automation of Repetitive Work | 4 | Rename sweeps applied by hand across layers |
| Consistency Across Windows | 8 | 42 commits / 16 merged PRs in the week against 67 / 32 in the month, steady |

### NandanDate-Medicodio — 5.7 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | 4 merge commits and 9 approvals on nextgen-codio-engine; no PR of his own on the day |
| Engineering Rigor (tests, docs, safety) | 5 | The two config risks Devin escalated on PR #353 (obgyn-only code_scope for operative_hcpcs_prediction, rag_query_field contradicting its own comment) plus the PHI-in-exception-message concern were still open on the review day |
| Code Review Contribution | 4 | 9 approvals on the day at thin depth; 51 approvals and 1 commented review in the month |
| Observable Devin Leverage | 8 | Requested the session behind PR #353 and landed 6 Devin-related fix commits on 08-18 — the strongest delegation in the data |
| Automation of Repetitive Work | 5 | The guideline/config fix class recurs and is still handled per-instance |
| Consistency Across Windows | 6 | Regressed against 08-18 (that day carried the session work), but the week trend is improving |

### ashwinsk-medicodio — 5.5 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | Provider-written ICD code attached to chapter routing (IM E&M), merged to UAT; 2 PRs merged |
| Engineering Rigor (tests, docs, safety) | 5 | 1 commit on the day with no test for a routing rule change |
| Code Review Contribution | NR | No reviews observed in any window |
| Observable Devin Leverage | 4 | The same S4.1 routing change for the other specialties is a scoped, repeatable candidate |
| Automation of Repetitive Work | NR | Insufficient data for comparison |
| Consistency Across Windows | NR | Insufficient data for comparison — 6 commits in the month |

### karthikmed — 5.5 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | Injury-selection matching with normalization functions (PR #367), not merged on the day |
| Engineering Rigor (tests, docs, safety) | 7 | Devin Review reported no issues on #367 — the cleanest review outcome among the day's PRs |
| Code Review Contribution | NR | No reviews observed in any window |
| Observable Devin Leverage | 4 | Normalization unit tests across the matcher inputs are an unclaimed candidate |
| Automation of Repetitive Work | NR | Insufficient data for comparison |
| Consistency Across Windows | NR | Insufficient data for comparison — 8 commits in the month |

### hiteshjrxmedicodio — 5.4 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | Paired feature PRs #545/#471 opened (KB reference endpoints, scoped PHI unmask, structured Ask-AI answers); both still open |
| Engineering Rigor (tests, docs, safety) | 6 | Scoped PHI unmask is handled deliberately; 1 test commit against 70 commits in the month |
| Code Review Contribution | NR | No reviews observed in any window |
| Observable Devin Leverage | 4 | No Devin evidence; the KB styling centralization half of the change is separable and delegable |
| Automation of Repetitive Work | 4 | Paired cross-repo feature work applied by hand |
| Consistency Across Windows | 6 | 70 commits / 22 merged PRs in the month; the week window is too thin to trend |

### Pj-Vineeth-Kumar — 5.3 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | 3 PRs opened (portal access control x2, person re-invite confirm), none merged on the day |
| Engineering Rigor (tests, docs, safety) | 6 | Refactor-heavy month (32 refactor, 6 test commits); no test or doc output on the day |
| Code Review Contribution | NR | No reviews observed in any window |
| Observable Devin Leverage | 5 | Work is partly blocked on a product decision on access-control vocabulary, so limited delegable surface today |
| Automation of Repetitive Work | 5 | The access-control vocabulary migration is repeated across layers by hand |
| Consistency Across Windows | 5 | Weekly output needs attention (3 PRs opened, 2 merged); monthly baseline exists but the day is unrepresentative |

### ragha82 — 5.2 / 10 (Mixed)

**Product:** Global Codio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | Two QA-sync PRs merged (#1186, #1184); no commits authored on the day |
| Engineering Rigor (tests, docs, safety) | 6 | Sync-and-validate work with no test or doc output; 3 Devin Review findings on #1186 were consumed |
| Code Review Contribution | 3 | 1 approval on the day with an empty body; 14 approvals in the month |
| Observable Devin Leverage | 5 | Devin Review findings acted on, but no session-level or delegated work visible |
| Automation of Repetitive Work | 3 | The dev -> feat/qa-automation sync-and-validate cycle ran 22 times in the month, entirely by hand |
| Consistency Across Windows | 7 | 23 commits / 22 merged PRs in the month at a constant rate |

### avinash-codio — 5.0 / 10 (Mixed)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | CMS-indicator-gated bilateral 50 -> RT/LT split and the vaccine-guideline count fix; 3 PRs merged |
| Engineering Rigor (tests, docs, safety) | 3 | 48 empty-body PRs in the month and 2 untested billing-rule changes on the day — for billing rules the PR body is the only provenance record |
| Code Review Contribution | 3 | 3 approvals in the whole month |
| Observable Devin Leverage | 5 | Landed 1 Devin-Review-driven fix on 08-18; guideline-rule regression tests remain undelegated |
| Automation of Repetitive Work | 4 | 69 merged PRs in the month, largely mechanical, with no generated descriptions |
| Consistency Across Windows | 7 | 80 commits / 71 PRs in the month — the documentation gap is consistent rather than worsening |

### amit-pandey-medicodio — 4.8 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** High

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | 5 PRs opened and all 5 merged, including the prompt-config sequence fix |
| Engineering Rigor (tests, docs, safety) | 4 | 4 of 5 PRs had empty bodies; no tests accompanied the config fix |
| Code Review Contribution | 3 | 8 approvals on the day, all with empty bodies; 111 approvals in the month at the same depth |
| Observable Devin Leverage | 5 | Correctly not a Devin case — promotion PRs belong in CI; but the promotion-body generator is a real delegable task |
| Automation of Repetitive Work | 2 | Roughly 35 hand-opened promotion PR pairs a month, all mechanical |
| Consistency Across Windows | 7 | 196 commits / 86 merged PRs / 111 approvals in the month, unchanged rate |

### shaheen-khan11 — 4.8 / 10 (Needs Support)

**Product:** Medicodio · **Confidence in this card:** Medium

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | Bulk-upload config reuse shipped as a paired change across nodejs (#544) and react (#470), both merged |
| Engineering Rigor (tests, docs, safety) | 4 | Both PRs had empty descriptions and no tests for a config-behaviour change |
| Code Review Contribution | 5 | 38 approvals in the month — high volume, depth not evidenced |
| Observable Devin Leverage | 3 | The paired cross-repo config change is the textbook Devin case and was done manually |
| Automation of Repetitive Work | 4 | Paired repo edits repeated by hand |
| Consistency Across Windows | 5 | 26 commits / 6 PRs in the month — too thin a monthly baseline to call a trend |

### SaahilVishwakarma — 4.4 / 10 (Needs Support)

**Product:** Global Codio · **Confidence in this card:** Low

| Dimension | Score (1-10) | Evidence observed |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | 1 PR opened (#1179, form-version party-role mismatch), not merged on the day |
| Engineering Rigor (tests, docs, safety) | 5 | Devin Review raised findings on #1179; 1 test commit against 67 in the month |
| Code Review Contribution | 3 | 1 approval in the whole month |
| Observable Devin Leverage | 4 | No Devin-authored PR; the party-role regression test is an unclaimed scoped candidate |
| Automation of Repetitive Work | NR | Insufficient data for comparison |
| Consistency Across Windows | NR | Insufficient data for comparison |

## How to read the spread

**Observed Fact:** the dimension that separates the cards is not delivery — almost everyone landed their scoped work — but rigor and review depth. Overall scores of 8+ belong to members who attached a test, a doc, or a substantive review finding to a risky change; scores below 5 on a dimension are almost always empty PR bodies, thin approvals, or untested rule changes.

**Inference:** the two lowest team-wide dimensions (Automation of Repetitive Work, Observable Devin Leverage) are structural rather than individual — promotion PRs, sync cycles, rename sweeps and review-log commits are unowned process work, so no individual is positioned to fix them alone.

**Recommendation:** treat the Devin and Automation columns as team targets owned by the leads, and use the Rigor and Review columns for individual coaching. Re-score on the next run to convert these into trends; per the analysis rules, none of these numbers can be called a Repeat Pattern yet.
