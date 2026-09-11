# Employee Rating Cards — 2026-09-11

**Review window:** 2026-09-10 03:00 UTC → 2026-09-11 03:00 UTC. Comparison windows: previous working day 09-09, week 09-03 → 09-10, month 08-11 → 09-10. Companion to `2026_09_11_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` and org session listing returned HTTP 403 (`org.sessions.view`), for the 9th consecutive run. Prompt quality, ACU/effort, tests-requested and correction burden are unobservable. "Observable Devin Leverage" is therefore scored only from what is visible in GitHub: `Co-Authored-By: Devin` trailers, Devin-authored PRs, Devin Review findings and how humans dispositioned them, and Devin QA-gate verdict comments.
- **Jira and Sentry were not callable.** Ticket flow, incident load and support work are invisible; members whose day was coordination-heavy are under-observed, not under-performing.
- **Volume is never scored.** Commit, PR, file and line counts appear only as context; a dimension is scored on the quality of what is observable (tests, PR bodies, finding dispositions, review substance, follow-through).
- **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average; fewer than three rated dimensions → overall NR. Confidence reflects how much of the member's work is visible in GitHub.
- **Identity merges (e-mail matched):** `saijyoti`=`SaijyotiMeti`, `Akanksh RV`=`akanksh-rv`, `Sumedh Kaulgud`=`sumedh-codio`, `Hitesh Shanthakumar`=`hitesh.ms`. `Claude <noreply@anthropic.com>` (4 commits) is unattributable and unrated. `devin-ai-integration[bot]` is a tool and is not rated.
- **Product boundaries.** Medicodio and Global Codio members are scored against the same rubric but never compared to each other's conventions.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, abandoned without record, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.**

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| akanksh-rv | Global Codio | **7.1** | Solid | 7.5 | 7.5 | 7.5 | 7.0 | 5.0 | 7.0 | High |
| Medicodio-Amit | Medicodio | **7.1** | Solid | 7.0 | 8.0 | NR | 6.0 | NR | 6.5 | Medium |
| saijyoti | Global Codio | **7.0** | Solid | 8.0 | 7.0 | 7.5 | 7.0 | 4.5 | 6.5 | High |
| anirudh-medicodio | Global Codio | **7.0** | Solid | 8.0 | 7.0 | 7.0 | 7.0 | 4.5 | 7.0 | High |
| Pj-Vineeth-Kumar | Global Codio | **6.8** | Mixed | 8.0 | 7.5 | 5.5 | 5.5 | 5.5 | 7.0 | High |
| ragha82 | Global Codio | **6.7** | Mixed | 7.0 | 7.5 | NR | 6.0 | 5.0 | 6.5 | Medium |
| Amrutha-Beedikar | Global Codio | **6.7** | Mixed | 6.5 | 7.5 | NR | 6.0 | NR | 6.0 | Medium |
| Hitesh Shanthakumar | Medicodio | **6.3** | Mixed | 6.0 | 6.5 | NR | 7.0 | 6.0 | 6.0 | Medium |
| afifashaikh007 | Medicodio | **6.0** | Mixed | 6.0 | 6.5 | NR | NR | 5.5 | 5.5 | Low |
| amit-pandey-medicodio | Medicodio | **5.9** | Mixed | 7.5 | 6.5 | 3.0 | 6.0 | 4.0 | 6.5 | High |
| jatinkushwaha-medicodio | Medicodio | **5.5** | Mixed | 7.5 | 6.5 | 3.0 | 4.0 | 4.0 | 6.0 | High |
| Vishnu Sai Karthik | Medicodio | **5.3** | Mixed | 5.5 | 5.0 | NR | NR | NR | 5.5 | Low |
| sameer-s-mansur | Medicodio | **5.3** | Mixed | 7.0 | 5.0 | NR | 3.5 | 3.5 | 6.0 | High |
| NandanDate-Medicodio | Medicodio | **4.6** | Needs Support | 6.5 | 4.5 | 3.0 | 3.0 | NR | 4.5 | High |
| sumedh-codio | Medicodio | **4.5** | Needs Support | 6.5 | 4.5 | 2.5 | 3.0 | 5.0 | 4.5 | High |
| avinash-codio | Medicodio | **4.2** | Needs Support | 6.0 | 4.5 | 2.5 | 2.5 | 4.0 | 4.0 | Medium |
| ashwinsk-medicodio | Medicodio | NR | — | 5.0 | 4.0 | NR | NR | NR | NR | Low (2 dimensions) |
| svh-medicodio | Global Codio | NR | — | 4.0 | NR | NR | NR | NR | 5.0 | Low (2 dimensions) |
| SaahilVishwakarma | Global Codio | NR | — | 3.5 | NR | NR | NR | NR | 4.5 | Low (2 dimensions) |
| Murali-Shetty19 | Medicodio | NR | — | 5.0 | NR | NR | NR | NR | NR | Low (1 dimension) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Change vs 2026-09-10 cards: akanksh 6.9→7.1, saijyoti 7.0→7.0, anirudh 7.1→7.0, Vineeth 6.1→6.8, ragha82 6.8→6.7, Amrutha 6.8→6.7, Hitesh 5.7→6.3, amit-pandey 6.3→5.9, Jatin 6.0→5.5, afifa 6.0→6.0, Vishnu 5.6→5.3, sameer 6.4→5.3, Nandan 5.4→4.6, sumedh 4.6→4.5, avinash 3.9→4.2; Medicodio-Amit NR→7.1 (first rated day this week).

## Cards

## akanksh-rv — Global Codio — 7.1 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | Own `#1337` (70 files) merged 03:48; remediated saijyoti's `#1350` (23 commits) to merge 20:42. Against: `#1355` PRD opened and closed in 74 s; QA gate NOT READY on `#1350` post-merge. |
| Engineering Rigor | 7.5 | Tests added for guard branches; refusal modelled as a type not a tag; transactional skip row; explicit self-correction commit ("correct my own overclaim"). Against: 25 commits between 18:27 and 20:40 on a PR merged at 20:42. |
| Code Review Contribution | 7.5 | 8,924-char Architect+EM review with 5 inline "[was: blocker — fixed in …]" threads. Against: he authored the fixes, then approved and merged. |
| Observable Devin Leverage | 7.0 | "All three Devin findings were verified as real (zero false positives)" and fixed. Against: 0 trailers; `#1355` closed before its 16 findings were read. |
| Automation of Repetitive Work | 5.0 | PRD-changelog and review-log commits (5 today) still manual. |
| Consistency Across Windows | 7.0 | Day Stable; week Stable; month Consistent; second consecutive substantive review. |

## Medicodio-Amit — Medicodio — 7.1 Solid (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#440` merged; `#444`, `#447` opened with full bodies and open at window end. |
| Engineering Rigor | 8.0 | 4,565- and 7,485-char PR bodies with per-commit rationale and rule tables; `#440` Devin "No Issues Found". Against: no `test(` commits visible. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 6.0 | Clean Devin Review on `#440`; 4 findings on `#447` unanswered (13 h, within normal turnaround). |
| Automation of Repetitive Work | NR | No evidence either way. |
| Consistency Across Windows | 6.5 | Day Improved; week Improving; month Consistent (55 commits, 19 days). |

## saijyoti — Global Codio — 7.0 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | Merged `#1337`, `#1331`, `#1316` (186 files combined) after remediation; own `#1350` opened and merged same day. |
| Engineering Rigor | 7.0 | 7 `(architect-review)` fixes with independent verification; 4 `test(` commits; gate failures fixed. Against: 35 commits on `#1316` in 3 h then merge; QA gate found 5 PRODUCT_FAILUREs 1 h later. |
| Code Review Contribution | 7.5 | Three reviews of 8.3k/6.5k/10.2k chars with hash-linked dispositions — the org's best. Against: approved `#1331` 5 min after posting 5 "needs your decision" blockers; reviewer = remediator = merger ×3. |
| Observable Devin Leverage | 7.0 | Every Devin finding dispositioned in writing; "Devin-flagged, independently verified". Against: QA gate consumed post-merge; `#1316` NOT READY, `#1350` NOT READY. |
| Automation of Repetitive Work | 4.5 | 12 hand-written review-log commits; 6 PRD-changelog commits. |
| Consistency Across Windows | 6.5 | Day Stable; week Needs Attention (merge-control shape); month Consistent. |

## anirudh-medicodio — Global Codio — 7.0 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | Closed own draft `#1320` (148 files, open since 09-07); remediated and merged `#1323`, `#1349`. |
| Engineering Rigor | 7.0 | Three tenancy/RLS fixes with pinned tests; ADR-0048; author approval obtained for migration scope. Against: 23 commits on a 123-file breaking PR merged 3 h after opening; 4 findings posted post-merge. |
| Code Review Contribution | 7.0 | 8,867 + 9,680-char reviews, blockers named with fixing commits. Against: REQUEST CHANGES → own 0-char APPROVE in 4 and 11 min; "[needs your decision]" on `#1323` unanswered. |
| Observable Devin Leverage | 7.0 | 20 of 36 findings resolved by his commits; QA verdicts 70/82/78 consumed. Against: gate is post-merge. |
| Automation of Repetitive Work | 4.5 | Header backfills, review-log and ADR reverse-documentation by hand (4 commits). |
| Consistency Across Windows | 7.0 | Day Stable; week Improving; month Consistent. |

## Pj-Vineeth-Kumar — Global Codio — 6.8 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#1349` opened and merged same day; HR-portal parity and WYSIWYG editor progressed. |
| Engineering Rigor | 7.5 | 30,083-char body ("one of the better ones in this repo" — reviewer); textbook migration pairing; `test(hr-analytics)` update. Against: 5 blockers found by reviewer incl. a cross-tenant read; editor code on a `docs/` branch. |
| Code Review Contribution | 5.5 | One approval ("approved!") on `#1320` (148 files) with no comments. |
| Observable Devin Leverage | 5.5 | 0 trailers today (19 on 09-09); 21 findings handled by reviewer. Inference: breaking migration correctly human-owned. |
| Automation of Repetitive Work | 5.5 | Retirement sweep done by hand; no automation. |
| Consistency Across Windows | 7.0 | Day Improved; week Improving; month Consistent. |

## ragha82 — Global Codio — 6.7 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | QA artifacts for three merged PRs landed on `feat/qa-automation`. Against: no PR of his own. |
| Engineering Rigor | 7.5 | Executable e2e suites (`#1312`, `#1342`); two findings publicly corrected (F-B "my probe", F-C reclassified). |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 6.0 | Works alongside Devin QA gates; Inference: duplicates digest/plan artifacts Devin already produces. |
| Automation of Repetitive Work | 5.0 | Digest + plan + report per PR written by hand, 3× today. |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

## Amrutha-Beedikar — Global Codio — 6.7 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | Own `#1323` merged (by anirudh); `#1322` (Saahil's) advanced 8 commits but still open, 4th day. |
| Engineering Rigor | 7.5 | 5 `test(` commits; debt filed explicitly. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 6.0 | 1 finding auto-resolved; no written dispositions. |
| Automation of Repetitive Work | NR | No evidence. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Insufficient History. |

## Hitesh Shanthakumar — Medicodio — 6.3 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 14 commits on a branch with no PR (5th report); Devin PR `#448` closed unmerged by intent, branch retained. |
| Engineering Rigor | 6.5 | Intent-stating conventional commits; seed answer keys aligned to spec. Against: 2,009 lines unreviewed; no tests. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 7.0 | Only Medicodio member with Devin-trailer commits today: 101-file prompt export + vetting reports, a well-fitted bulk task. |
| Automation of Repetitive Work | 6.0 | `feat(scripts): export assembled engine prompts to text files` — automation in progress. |
| Consistency Across Windows | 6.0 | Day Improved; week Improving; month Consistent. |

## afifashaikh007 — Medicodio — 6.0 Mixed (Low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 9 rule-scoped commits on `feat/inpatient-engine`; no PR (5th report). |
| Engineering Rigor | 6.5 | Guideline sections cited per commit; four section-number corrections. Against: no tests; no review. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No Devin Review possible without a PR. |
| Automation of Repetitive Work | 5.5 | "generate the code tables" — repetition acknowledged, partly scripted. |
| Consistency Across Windows | 5.5 | Day Improved; week Improving; month Insufficient History. |

## amit-pandey-medicodio — Medicodio — 5.9 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#632`, `#564`, `#566` merged; `#635` open; promotions `#631`/`#563` merged. |
| Engineering Rigor | 6.5 | Fix commits follow Devin findings within the hour; RVU edge case handled. Against: promotion PRs with empty bodies; no `test(` commits. |
| Code Review Contribution | 3.0 | 3 approvals, all 0-char, incl. `#305` (12 files, 8 findings). |
| Observable Devin Leverage | 6.0 | Findings on own PRs resolved by commits (bot marked resolved). Against: `#305` findings ignored at merge. |
| Automation of Repetitive Work | 4.0 | Daily "dev to uat" PRs by hand. |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

## jatinkushwaha-medicodio — Medicodio — 5.5 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#633`, `#567` merged; `#568`, `#634`, `#565` open; `#626`/`#557` prod PRs open 2nd day. |
| Engineering Rigor | 6.5 | `#633` 821-char body, Devin "No Issues". Against: promotion PRs empty; no tests. |
| Code Review Contribution | 3.0 | 6 approvals, all 0-char; `#307` prod approved 85 s after 6 findings. |
| Observable Devin Leverage | 4.0 | Merged `#307` to `release/prod_1.0` with 6 findings unanswered; `#566` approved before fix commits landed. |
| Automation of Repetitive Work | 4.0 | Daily "dev->uat" PRs by hand. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

## Vishnu Sai Karthik — Medicodio — 5.3 Mixed (Low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | 4 commits, no PR; dxex split progressed. |
| Engineering Rigor | 5.0 | Two described commits; two titled "config update"/"paramters updated" (Repeat Pattern). |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No PR, no Devin exposure. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.5 | Day Stable; week Stable; month Consistent. |

## sameer-s-mansur — Medicodio — 5.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | Teams alerting reached UAT and prod (`#305`, `#307`); `#304` back-port merged; `#306` open. |
| Engineering Rigor | 5.0 | 12-file / 2.4k-line feature with no test commits; same diff as three PRs. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 3.5 | 21 Devin findings across 4 PRs, 0 dispositions; 6 reached prod. |
| Automation of Repetitive Work | 3.5 | Manual triple-PR promotion and UAT→Dev back-port (Repeat Pattern ×3). |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

## NandanDate-Medicodio — Medicodio — 4.6 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | 5 engine PRs approved and merged incl. 2 prod promotions — fast turnaround. |
| Engineering Rigor | 4.5 | `#446` merged 22 s after opening, before Devin Review ran. |
| Code Review Contribution | 3.0 | 5 approvals, all "okay". |
| Observable Devin Leverage | 3.0 | `#443` merged 29 s after 4 findings; `#446` 3 findings post-merge. 09-09's written dispositions (`#438`) not repeated. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.5 | Day Regressed (from 09-09 dispositions); week Needs Attention; month Consistent. |

## sumedh-codio — Medicodio — 4.5 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | RPA `#20` shipped with docs. |
| Engineering Rigor | 4.5 | First RPA test commit this week (positive). Against: self-merge 11 s after opening, empty body (3rd: `#17`, `#19`, `#20`). |
| Code Review Contribution | 2.5 | `#304` approved 0-char 12 min after 5 new findings. |
| Observable Devin Leverage | 3.0 | No Devin Review on RPA repo; `#304` findings ignored. |
| Automation of Repetitive Work | 5.0 | Notification breakdown automated in RPA; own PR process not. |
| Consistency Across Windows | 4.5 | Day Stable; week Stable; month Consistent (pattern unchanged). |

## avinash-codio — Medicodio — 4.2 Needs Support (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | `#442`, `#445` merged to UAT and promoted to prod same hour; PC1/PC2 split landed. |
| Engineering Rigor | 4.5 | `#445` scoped title. Against: duplicate commits, "orhto cpt"; 28-file prod promotion 22 s after opening. |
| Code Review Contribution | 2.5 | `#441` prod approved "Okay" with 1 finding. |
| Observable Devin Leverage | 2.5 | 8 findings across `#441/#443/#446` reached prod unanswered (3rd consecutive report). |
| Automation of Repetitive Work | 4.0 | Per-client config files added by hand (2 days running). |
| Consistency Across Windows | 4.0 | Day Stable; week Stable; month Needs Improvement. |

## ashwinsk-medicodio — Medicodio — NR (2 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | 7 POC commits, no PR. |
| Engineering Rigor | 4.0 | One well-described commit; then "fixex" ×2, "kep thinking empty". |
| Others | NR | — |

## svh-medicodio — Global Codio — NR (2 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4.0 | Own `#1316`/`#1331` merged only after 41 reviewer commits; `#1334` closed unmerged; 0 commits or comments. |
| Consistency Across Windows | 5.0 | Week Needs Attention (absent since 09-08 while PRs remediated); month Consistent (240 commits). |
| Others | NR | — |

## SaahilVishwakarma — Global Codio — NR (2 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 3.5 | `#1322` (112 files) open 4th day, author inactive, advanced only by Amrutha. |
| Consistency Across Windows | 4.5 | Week Needs Attention; month Insufficient History. |
| Others | NR | — |

## Murali-Shetty19 — Medicodio — NR (1 dimension)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | 1 commit (Chatwoot routes) on `Supportcodio-BE`, no PR. |
| Others | NR | — |

## How to read the spread

- **Observed Fact:** The four Solid scores are the three Global Codio senior reviewers plus Medicodio-Amit, whose PR bodies are the most complete in Medicodio. All three Needs Support scores are Medicodio members whose day consisted mainly of approving/merging or self-merging with Devin findings unanswered. Medicodio's 16 human review events were all ≤10 chars; Global Codio produced 6 reviews over 6,000 chars.
- **Inference:** The Global Codio spread is compressed (6.7–7.1) because the same strength (deep review) and the same weakness (reviewer = remediator = merger, QA gate post-merge) apply to all three seniors. The Medicodio spread is wide because the difference between members is almost entirely whether they write PR bodies and answer Devin findings — not what they build.
- **Recommendation:** Do not rank individuals on these numbers; they move 0.5 on a single well-written approval. Use them to pick two habits per product: Global Codio — second approver + pre-merge QA gate; Medicodio — no prod merge before Devin Review completes + one disposition line per finding. Re-score after a week, not a day.
