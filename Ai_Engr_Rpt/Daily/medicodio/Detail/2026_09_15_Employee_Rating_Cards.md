# Employee Rating Cards — 2026-09-15

**Review window:** 2026-09-14 03:00 UTC → 2026-09-15 03:00 UTC (Monday). Comparison windows: previous working day 09-11, week 09-07 → 09-14, month 08-15 → 09-14. Companion to `2026_09_15_Mgmt_Activity_Report.md`. Per the 09-14 cards, today's scores are compared against the **09-12 and 09-11 working-day cards**, not the weekend NR sets.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`Missing required permission 'org.sessions.view'`) for the **13th consecutive run**; no Jira or Sentry tools were callable. Prompt quality, ACU/effort, tests-requested and correction burden are unobservable. "Observable Devin Leverage" is scored only from GitHub-visible artefacts: Devin-authored PRs, `Co-Authored-By: Devin` trailers, Devin Review / Devin QA findings and the human dispositions of them. **Claude trailers are not counted as Devin usage** (63 of 67 commits today carry them).
- **Activity was confined to Global Codio.** Three humans and the Devin bot produced all 67 commits, all in `globalcodio-monorepo`. **All five Medicodio repositories had zero events** (commits on any branch, PRs, reviews, comments). Every Medicodio member is therefore **NR** today; NR means "no evidence", not a low score, and the cause of the silent Monday cannot be established from GitHub (Jira/calendar unavailable).
- **NR rules.** A dimension without in-window evidence is NR and excluded from the weighted average; fewer than three rated dimensions → overall **NR**.
- **Volume is never scored.** Commit, file and line counts appear only as context (e.g. "36 commits", "95 files").
- **Attribution.** Commits are placed by author date. akanksh-rv's 27 commits at 02:08–02:52 UTC on 09-15 fall inside this window. Identities merged by e-mail: `saijyoti` = SaijyotiMeti; `Akanksh RV` = akanksh-rv; `Amrutakb` = Amrutha-Beedikar.
- **Product boundaries.** Global Codio members are scored against the rubric only; nothing here compares them to Medicodio conventions.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, abandoned without record, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| akanksh-rv | Global Codio | **7.3** | Solid | 8 | 8 | 6 | 7 | 5 | 8 | Medium (GitHub only; large evidence base) |
| SaijyotiMeti | Global Codio | **6.5** | Mixed | 6 | 8 | 5 | 7 | 5 | 7 | Medium (GitHub only; large evidence base) |
| Amrutha-Beedikar | Global Codio | **6.3** | Mixed | 6 | 6 | NR | 7 | NR | 6 | Low (1 commit; 4 dimensions rated) |
| anirudh-medicodio, Pj-Vineeth-Kumar, ragha82, svh-medicodio, SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity in window) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (zero Medicodio events Monday) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Weighted averages: akanksh-rv = (8·25 + 8·25 + 6·15 + 7·15 + 5·10 + 8·10) / 100 = 7.25 → **7.3 (Solid)**. SaijyotiMeti = (6·25 + 8·25 + 5·15 + 7·15 + 5·10 + 7·10) / 100 = 6.50 → **6.5 (Mixed)**. Amrutha-Beedikar (Review and Automation NR; weights 25+25+15+10 = 75) = (6·25 + 6·25 + 7·15 + 6·10) / 75 = 6.33 → **6.3 (Mixed)**.

Change vs last rated working-day cards: akanksh-rv 6.8 (09-12) / 6.7 (09-13) → **7.3**; SaijyotiMeti 6.6 (09-12) → **6.5**; Amrutha-Beedikar 7.1 (09-12) → **6.3** (thin evidence, Low confidence — not a trend). All others NR today versus rated values on 09-12 (Medicodio-Amit 7.8, Pj-Vineeth-Kumar 7.3, anirudh 7.1, ashwinsk 4.3, avinash 3.4) — absence of evidence, not a change.

## Cards

## akanksh-rv — Global Codio — Overall 7.3 — Solid — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** his PR `#1367` (AI Case Manager inbox triage, opened 09-11) merged into `dev` at 18:08 by a non-author after a full review; Entity Status Phase 1+2 PRDs written and pushed (`docs/entity-status-phase-1-and-2-prds`, no PR yet); 27-commit review pass on `#1373` ended with 7 NEEDS-DECISION items written and **no merge**. **Inference:** the one loose end is the PRD branch without a PR. |
| Engineering Rigor | 8 | **Observed Fact:** `#1367` body (10.2k chars) quantifies defects and fixes (thinking tokens 5,859→ `thinkingLevel:'low'`, 29.7s→1.5s; 29/56 goals invisible to the candidate query), discloses "test suite had not been run" and the correction cycle; on `#1373` his pass fixed a tenant-scoping gap (`findCaseHasOrganization` by `firm_id`), restored structured logging, and replaced "three tests that proved nothing" with tests that fail on the wrong behaviour; final commit repairs his own typecheck breaks. **Inference:** rigour is high; his PR still shipped at 123 files and the pre-merge test suite was not run by him. |
| Code Review Contribution | 6 | **Observed Fact:** 27 review-pass commits on a peer's PR with the findings recorded in a commit body (`docs/review-logs` 19-row ledger) — **no GitHub review object**, so nothing is "requested" vs "done" in the PR timeline; no approval given (correct, given open items). **Inference:** substantive but not independent and not traceable as a review. |
| Observable Devin Leverage | 7 | **Observed Fact:** dispositioned all 12 Devin Review comments on `#1373` in writing (6 folded in, 3 refuted with evidence, 3 already disclosed); Devin marked 4 resolved at 02:17. 8 new findings at 02:56 unanswered at window end (4 min later — not a lapse). No Devin-authored work on his branches. **Inference:** strong as a Devin *reviewer-consumer*; no delegation of the mechanical work Devin could have done. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 5 of 28 commits are atlas regeneration / header sync / debt-ledger sync, recurring on every branch this month; no automation of them. |
| Consistency Across Windows | 8 | **Observed Fact:** 09-11 he merged `#1366` over his own written blocker; today he stopped at the decision items. Week 166 commits (3rd), month 629 (2nd), 31 PRs; PR-body quality consistent since 08-24. **Inference:** Improving on control (one day), Consistent on rigour. |

**Do:** open the PRD branch as a draft PR; post the 7 items as a Request-changes review. **Don't:** commit 27 fixes on a peer's PR without a review object. **Next improvement:** convert the NEEDS-DECISION list into a formal review addressed to the author.

## SaijyotiMeti — Global Codio — Overall 6.5 — Mixed — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** remediated and merged `#1367` (20 commits, 8 fixes, 4 test commits); opened `#1373` (95 files, PRD, size justification, standards audit). But: merged with her own "pending 2 schema decisions" unwritten; post-merge Devin QA `#1372` NOT READY 45/100 42 min later. **Inference:** high throughput, merge control below the rubric's 7 ("merged without controls" language applies to the open decisions, not the code). |
| Engineering Rigor | 8 | **Observed Fact:** every fix commit has a why-it-matters body; 4 test commits covering the fixes ("this branch shipped untested"); one further real bug found by running the gates (multi-attachment ordering); `#1373` opened with PRD + `§5.2` size justification + `/check` log. **Inference:** the 95-file size and the unrun index decision cost the top band. |
| Code Review Contribution | 5 | **Observed Fact:** 8,122-char architect/EM review with 7 SHA-linked inline comments — the most specific review in the org this window — followed 4 min later by an 8-char `approved` and 5 min later by her own merge, on a PR she had authored 20 commits to that day. **Inference:** substance 9, independence 1; the rubric's "independent review that changes outcomes" is not met because the review's outcomes were her own commits. |
| Observable Devin Leverage | 7 | **Observed Fact:** adjudicated 10 Devin Review claims in writing (6 real+fixed, 1 process gap, 3 false positives traced); 5 marked resolved by Devin. Post-merge QA NOT READY with C-1..C-4 configuration gaps unanswered at window end. No Devin authoring. **Inference:** excellent finding-disposition; gate still used after, not before, merge. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 3 hand-written `docs(review-logs)` commits + atlas regeneration; peer-remediation-then-approve repeated for the 6th report. No automation started. |
| Consistency Across Windows | 7 | **Observed Fact:** week 170 commits (2nd), 12 review events (6 substantive, all on PRs she remediated), 3 of the week's 4 post-merge NOT READY merges were hers; month 573 commits, most substantive reviewer in the org. Score 6.6 (09-12) → 6.5. **Inference:** Stable on review substance; the merge-control pattern is unchanged. |

**Do:** keep the SHA-linked review style; hand `#1373` to a non-contributor reviewer and the pre-merge QA gate. **Don't:** approve + merge a PR you remediated the same day; leave your own schema decisions open at merge. **Next improvement:** make `#1373` the first GC feature PR in five to be QA-gated before merge with an independent approval.

## Amrutha-Beedikar — Global Codio — Overall 6.3 — Mixed — Confidence: Low (4 of 6 dimensions; 1 commit)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** synced `dev` into Devin PR `#1360` and pushed `fix(audit): stop the orphan-checklist audit overstating the backlog`; `#1360` (4th day) and `#1364` (4th day) still open with no reviewer requested. **Inference:** progress without closure. |
| Engineering Rigor | 6 | **Observed Fact:** fix commit has a clear body (Claude trailer); no test added for the corrected count; the new Devin Review finding on the SQL header's exemption claim is unanswered. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 7 | **Observed Fact:** finishing a Devin-authored PR by hand — the only member this window consuming Devin output to closure; 1 finding resolved, 1 new unanswered. **Inference:** positive consumption; asking Devin to make the fix + test would have been the higher-leverage path. |
| Automation of Repetitive Work | NR | No repetitive-work evidence in window. |
| Consistency Across Windows | 6 | **Observed Fact:** 09-11 4 commits, today 1; week 27, month 45; 09-12 card 7.1. **Inference:** low, steady volume; today's drop is evidence thinness, not a regression. |

**Do:** answer the header finding, add the count test (Devin), request a reviewer on `#1360`/`#1364`. **Don't:** leave a Devin finding on your own commit unanswered. **Next improvement:** close out `#1360` today.

## Members not rated this window

**Global Codio:** anirudh-medicodio (`#1363` 110 files idle 4th day, `feat/document-catalog-samples` no PR), Pj-Vineeth-Kumar (`#1365` no human reviewer, `feat/hr-portal-revamp` no PR 5th report), ragha82 (`#1362` idle), svh-medicodio, SaahilVishwakarma (`#1369` fix to his feature still open) — no commits, PR events, reviews or comments in `globalcodio-monorepo`. Last rated (09-12): Vineeth 7.3, anirudh 7.1; others NR.

**Medicodio:** amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, Shashvi1 — zero events across all five Medicodio repositories on a working Monday (last pushes 09-10/09-11). Last rated (09-12): Medicodio-Amit 7.8, ashwinsk 4.3, avinash 3.4. Carried unowned: integration `#308` (9 findings), `#314` (18k-line promotion), engine `#435`, `feat/inpatient-engine` (9th report without a PR).

## How to read the spread

- **Observed Fact:** three people account for every rated dimension today; two of them (akanksh-rv 7.3, SaijyotiMeti 6.5) produced the org's only substantive review work, each on the other's PR, and each by committing directly to it — 20 and 27 commits respectively. The single approval in the organisation was SaijyotiMeti's on her own remediation, followed by her own merge and a NOT READY post-merge gate (4th consecutive). Medicodio contributed no events.
- **Inference:** the ~0.8-point gap between akanksh-rv and SaijyotiMeti is entirely the merge-control decision: same rigour band, same Devin-disposition band, but he stopped at his decision items and she merged over hers. Amrutha-Beedikar's 6.3 is a thin-evidence number and should not be trended against her 7.1. The Medicodio NRs say nothing about performance; they say Monday was silent and the reason is not visible in GitHub.
- **Recommendation:** managers should read today's cards as one signal — Global Codio's review process has substance but no independence, and branch protection (approver with zero commits on the PR, QA gate as a required check) would move both rated engineers into the Solid/Strong bands without changing how they work. Confirm the Medicodio non-working day, then use 09-16 as the next comparable Medicodio card set against 09-11/09-12. Grant `org.sessions.view` so Devin leverage can be scored from sessions rather than inferred from GitHub artefacts.
