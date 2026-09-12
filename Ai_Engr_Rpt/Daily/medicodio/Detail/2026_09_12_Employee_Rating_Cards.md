# Employee Rating Cards — 2026-09-12

**Review window:** 2026-09-11 03:00 UTC → 2026-09-12 03:00 UTC. Comparison windows: previous working day 09-10, week 09-04 → 09-11, month 08-12 → 09-11. Companion to `2026_09_12_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` and org session listing returned HTTP 403 (`org.sessions.view`), for the 10th consecutive run. Prompt quality, ACU/effort, tests-requested and correction burden are unobservable. "Observable Devin Leverage" is scored only from GitHub-visible evidence: `Co-Authored-By: Devin` trailers, Devin-authored PRs, Devin Review findings and how humans dispositioned them, and Devin QA-gate verdict comments. Claude session markers on commits are **not** counted as Devin usage.
- **Jira and Sentry were not callable.** Ticket flow, incident load and support work are invisible; members whose day was coordination-heavy are under-observed, not under-performing.
- **Volume is never scored.** Commit, PR, file and line counts appear only as context; a dimension is scored on the quality of what is observable (tests, PR bodies, finding dispositions, review substance, follow-through).
- **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average; fewer than three rated dimensions → overall NR. Confidence reflects how much of the member's work is visible in GitHub.
- **Identity merges (e-mail matched):** `saijyoti`=`SaijyotiMeti`=`Saijyoti Meti`, `Akanksh RV`=`akanksh-rv`, `Pj-Vineeth-Kumar`=`vineeth.kumar`, `Amrutha-Beedikar`=`amrutha.b`, `Sumedh Kaulgud`=`sumedh-codio`. `Claude <noreply@anthropic.com>` (3 commits) is unattributable and unrated. `devin-ai-integration[bot]` is a tool and is not rated.
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
| Medicodio-Amit | Medicodio | **7.8** | Solid | 8.0 | 8.5 | NR | 8.5 | 5.0 | 7.5 | High |
| Pj-Vineeth-Kumar | Global Codio | **7.3** | Solid | 7.5 | 7.5 | 4.0 | 9.0 | 8.0 | 7.5 | High |
| anirudh-medicodio | Global Codio | **7.1** | Solid | 7.5 | 7.5 | NR | 7.0 | 5.0 | 7.5 | High |
| Amrutha-Beedikar | Global Codio | **7.1** | Solid | 7.0 | 7.5 | NR | 7.5 | 6.0 | 6.5 | Medium |
| akanksh-rv | Global Codio | **6.8** | Mixed | 7.0 | 7.5 | NR | 6.0 | 5.5 | 7.0 | High |
| saijyoti | Global Codio | **6.6** | Mixed | 7.5 | 7.0 | 6.5 | 6.0 | 4.5 | 6.5 | High |
| sameer-s-mansur | Medicodio | **6.3** | Mixed | 7.0 | 7.0 | NR | 5.5 | 3.5 | 6.5 | High |
| afifashaikh007 | Medicodio | **6.3** | Mixed | 6.0 | 7.0 | NR | NR | 5.5 | 6.0 | Low |
| amit-pandey-medicodio | Medicodio | **6.2** | Mixed | 7.5 | 7.0 | 3.5 | 6.5 | 4.0 | 6.5 | High |
| ragha82 | Global Codio | **6.1** | Mixed | 6.5 | 7.0 | 4.0 | 5.5 | NR | 6.5 | Medium |
| jatinkushwaha-medicodio | Medicodio | **5.5** | Mixed | 7.0 | 6.5 | 3.0 | 4.5 | 4.0 | 6.0 | High |
| NandanDate-Medicodio | Medicodio | **5.4** | Mixed | 7.0 | 6.5 | 3.0 | 3.5 | NR | 5.0 | High |
| Hitesh Shanthakumar | Medicodio | **5.3** | Mixed | 5.0 | 5.5 | NR | NR | 5.0 | 5.5 | Medium |
| Vishnu Sai Karthik | Medicodio | **5.3** | Mixed | 5.0 | 5.5 | NR | NR | NR | 5.5 | Low |
| ashwinsk-medicodio | Medicodio | **4.3** | Needs Support | 5.0 | 4.0 | NR | NR | 3.5 | 4.5 | Low |
| avinash-codio | Medicodio | **3.4** | Needs Support | 4.0 | 3.5 | 2.5 | 2.5 | NR | 4.5 | Medium |
| svh-medicodio | Global Codio | NR | — | 3.5 | NR | NR | NR | NR | 4.5 | Low (2 dimensions) |
| SaahilVishwakarma | Global Codio | NR | — | 3.5 | NR | NR | NR | NR | 4.5 | Low (2 dimensions) |
| Murali-Shetty19 | Medicodio | NR | — | 4.0 | NR | NR | NR | NR | NR | Low (1 dimension) |
| sumedh-codio | Medicodio | NR | — | NR | NR | NR | NR | NR | 5.5 | Low (1 dimension) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Change vs 2026-09-11 cards: Medicodio-Amit 7.1→7.8, Vineeth 6.8→7.3, anirudh 7.0→7.1, Amrutha 6.7→7.1, akanksh 7.1→6.8, saijyoti 7.0→6.6, amit-pandey 5.9→6.2, ragha82 6.7→6.1, sameer 5.3→6.3, afifa 6.0→6.3, Jatin 5.5→5.5, Nandan 4.6→5.4, Hitesh 6.3→5.3, Vishnu 5.3→5.3, avinash 4.2→3.4; ashwinsk NR→4.3 (3 dimensions rated today); sumedh 4.5→NR (no activity).

## Cards

## Medicodio-Amit — Medicodio — 7.8 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#447` (13 files, 7.5k body) and `#444` both merged after all findings dispositioned; yesterday's recommended action done. Against: opened `#449` prod promotion that merged in 21 s with 2 findings posted after. |
| Engineering Rigor | 8.5 | Four disposition rounds (4,106 / 3,758 / 2,393 / 1,325 chars): 6 fixed with hashes, 1 accepted with payload trace, 1 raised for confirmation; admits "a regression this PR introduced". Removed obsolete test runner. |
| Code Review Contribution | NR | No review events. |
| Observable Devin Leverage | 8.5 | Every Devin finding answered in writing with reason or fix — the standard for Medicodio. Against: `#449` findings unanswered. |
| Automation of Repetitive Work | 5.0 | E&M mapping tables edited by hand (4th day); no tooling started. |
| Consistency Across Windows | 7.5 | Day Improved; week Improving (4 long-form PRs merged); month Consistent. |

## Pj-Vineeth-Kumar — Global Codio — 7.3 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#1365` (67 files) delivered via Devin with all findings closed by 23:33; 19 HR-portal commits advanced. Against: HR branch still no PR after yesterday's recommendation. |
| Engineering Rigor | 7.5 | 9.7k body, PRD-linked, calendar-arithmetic fix for "tomorrow", auth-store sync. Against: ~7k HR lines unreviewed. |
| Code Review Contribution | 4.0 | One approval: `#1359` (1,331 files) 0-char, 70 s before merge. |
| Observable Devin Leverage | 9.0 | Best delegation of the day: bounded 130-call-site migration → Devin PR → 8 findings fixed with commit refs, 2 reasoned rejections, all before human review. Inference: prompt/spec quality high (session not visible). |
| Automation of Repetitive Work | 8.0 | The repetitive migration itself was automated via Devin. |
| Consistency Across Windows | 7.5 | Day Improved; week Improving (`#1349`, `#1365`); month Consistent — 97 Devin-trailer commits this month. |

## anirudh-medicodio — Global Codio — 7.1 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#1363` (110 files) opened as a PR from the first commit and advanced through 49 commits; dev→uat→main promotions completed. Against: 16 findings open; `#1361` body untouched template. |
| Engineering Rigor | 7.5 | Tests replaced "two vacuous assertions", debts filed, PRD r3, deployment note on `ALLOWED_ORIGINS`. Against: 110-file PR mixing 14 perf items with an auth-cookie change. |
| Code Review Contribution | NR | No review events today (yesterday's REQUEST-CHANGES-then-own-approve pattern did not occur). |
| Observable Devin Leverage | 7.0 | 5 of 21 findings resolved within 2 h, 2 Devin-trailer commits; later commits address session/KB-writer findings but no re-run confirmed before 03:00. |
| Automation of Repetitive Work | 5.0 | 9 header/PRD/review-log commits by hand; lockfile churn undone manually. |
| Consistency Across Windows | 7.5 | Day Improved; week Improving; month Consistent (active 24/30). |

## Amrutha-Beedikar — Global Codio — 7.1 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | Two own PRs opened with full bodies (`#1360` via Devin, `#1364`); neither reviewed by a human yet (19 h / 14 h). |
| Engineering Rigor | 7.5 | Added the test Devin omitted and sized the backlog; `#1364` root cause ("label as React key") in body; Devin "No Issues" on `#1364`. Against: 2 audit-SQL findings open. |
| Code Review Contribution | NR | No review events. |
| Observable Devin Leverage | 7.5 | Bounded bug delegated; Devin fixed its own race finding; she complemented with a test. |
| Automation of Repetitive Work | 6.0 | Delegated one repetitive fix class; label-as-key sweep not yet generalised. |
| Consistency Across Windows | 6.5 | Day Improved; week Stable; month Insufficient History. |

## akanksh-rv — Global Codio — 6.8 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1367` (109 files) opened and left open for review; 22 fixes landed on `#1366`. Against: 10 findings incl. 3 SEC unanswered at 03:00. |
| Engineering Rigor | 7.5 | Policy-seam test "which had no test at any tier"; query-shape test; "nine defects found by the first end-to-end run" fixed; 6.9k body. Against: 12.6k-line PR. |
| Code Review Contribution | NR | No review events (positive vs yesterday: did not approve the PR he remediated). |
| Observable Devin Leverage | 6.0 | 15 findings on `#1366` resolved by his commits; 10 on own `#1367` unanswered, 3 SEC. |
| Automation of Repetitive Work | 5.5 | PRD reconciliation + review-log commits still manual; removed an outdated punch list. |
| Consistency Across Windows | 7.0 | Day Stable; week Stable; month Consistent. |

## saijyoti — Global Codio — 6.6 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#1322` (open since 09-07) merged; `#1366` opened with a 12.4k body. Against: QA gate NOT READY 55 min after merge → `#1369`. |
| Engineering Rigor | 7.0 | 3 test commits, 5 tech-debt entries, boundary fix between form modules; self-corrected an overwritten review log. Against: merged 116 files 1 min after own approval without the gate. |
| Code Review Contribution | 6.5 | 6,297-char Architect+EM review with re-review after 510-commit sync. Against: she authored 16 of the commits under review, then approved and merged (Repeat Pattern). |
| Observable Devin Leverage | 6.0 | Findings dispositioned via review-log (Devin cited it when resolving 6). Against: 1 finding on the log unanswered at merge; gate not run pre-merge for the 2nd consecutive day. |
| Automation of Repetitive Work | 4.5 | 7 hand-written ledger commits incl. two restores of overwritten logs. |
| Consistency Across Windows | 6.5 | Day Stable; week Needs Attention; month Consistent. |

## amit-pandey-medicodio — Medicodio — 6.2 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#636`, `#638`, `#641`, `#569`, `#570`, `#572` merged; `#640` closed cleanly. Against: `#308` 9 findings 20 h unanswered. |
| Engineering Rigor | 7.0 | Root-cause bodies (`#638` Zod strip, `#636` lineage); 7 finding→fix cycles on `#569` before merge. Against: `#569` body template-only; one revert-and-redo. |
| Code Review Contribution | 3.5 | 9 approvals, 8 at 0 chars incl. `#626` prod (2 findings) and `#309` (4 findings); 1 specific inline comment on `#565`. |
| Observable Devin Leverage | 6.5 | First written false-positive rejection (`#570`, 1.6k chars, verified trace); findings fixed within the hour. Against: approves others' PRs with findings unread. |
| Automation of Repetitive Work | 4.0 | Same fix opened twice (Dev + UAT) ×2; daily promotion PRs by hand. |
| Consistency Across Windows | 6.5 | Day Improved; week Stable; month Consistent. |

## ragha82 — Global Codio — 6.1 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | `#1362` opened (3 well-scoped CI commits); open with 1 finding unanswered 17 h. |
| Engineering Rigor | 7.0 | Live-revision guard on image purge; redundant install removed. Against: PR body is the unfilled template. |
| Code Review Contribution | 4.0 | One approval: `#1361` uat→main (1,331 files) 0-char. |
| Observable Devin Leverage | 5.5 | Finding on `acr-purge.sh` unanswered; no delegation. |
| Automation of Repetitive Work | NR | No repetitive-work evidence today (QA-digest work paused). |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

## sameer-s-mansur — Medicodio — 6.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | Reliable file moves shipped UAT → prod → Dev in one day; `#314` (66 files) opened. Against: `#312` abandoned sync; self-merge to prod. |
| Engineering Rigor | 7.0 | Design doc, "settle the three open questions", QA report, PHI-safe retry logger, terminality carried explicitly; 11/18 findings fixed pre-merge. Against: 0 written dispositions; no unit tests for `http_retry.py`. |
| Code Review Contribution | NR | No review events. |
| Observable Devin Leverage | 5.5 | SEC findings answered by code within 40 min. Against: `#310` merged 3 min before 6 findings; 7 left on `#309`. |
| Automation of Repetitive Work | 3.5 | Triple promotion + back-port by hand for the 4th report. |
| Consistency Across Windows | 6.5 | Day Improved; week Stable; month Consistent. |

## afifashaikh007 — Medicodio — 6.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 11 rule-scoped commits; still no PR (6th report). |
| Engineering Rigor | 7.0 | Two `test(` commits ("three charts that exercise every rule added this week"); bug commits name the mechanism. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No Devin events possible without a PR. |
| Automation of Repetitive Work | 5.5 | Guideline → code transcription still manual; fixtures started. |
| Consistency Across Windows | 6.0 | Day Improved; week Improving; month Insufficient History. |

## jatinkushwaha-medicodio — Medicodio — 5.5 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#637`, `#639`, `#571` merged; prod promotions `#626`/`#557` completed. Against: `#637` merged 8 min after open with a migration finding open. |
| Engineering Rigor | 6.5 | 860-char body on `#637`; 2 of 6 `#639` findings fixed within 16 min. Against: 4 findings merged open; badge-only promotion bodies. |
| Code Review Contribution | 3.0 | 7 approvals ≤2 chars; `#311` approved before Devin posted; `#313` 1 min after. |
| Observable Devin Leverage | 4.5 | Partial fixes on `#639`; approvals precede or ignore findings. |
| Automation of Repetitive Work | 4.0 | 4 manual promotion PRs. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

## NandanDate-Medicodio — Medicodio — 5.4 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | Own `#450` opened and merged with test; 4 engine PRs merged; 4 stale PRs closed. Against: `#449` merged 21 s after open. |
| Engineering Rigor | 6.5 | `#450`: 2,525-char body with worked example + `test_hcpcs_units_merge.py`; Devin "No Issues". Against: closed 4 PRs without a captured reason. |
| Code Review Contribution | 3.0 | 4 "okay" approvals incl. two prod promotions; no evidence of reading `#447`'s four disposition rounds. |
| Observable Devin Leverage | 3.5 | `#449` merged before Devin ran; `#451` finding unanswered. Own PR clean. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.0 | Day Improved (own PR) / Stable (gate); week Needs Attention; month Consistent. |

## Hitesh Shanthakumar — Medicodio — 5.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | +8k lines wired in one commit on a shared branch; no PR (6th report); `#448` delegation not continued. |
| Engineering Rigor | 5.5 | Commit bodies state intent; guard narrowing described. Against: 49-file single commit, no tests visible. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No Devin events today. |
| Automation of Repetitive Work | 5.0 | Answer-key fixes still bundled into feature commits. |
| Consistency Across Windows | 5.5 | Day Regressed; week Stable; month Consistent. |

## Vishnu Sai Karthik — Medicodio — 5.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | 1 commit on POC branch; no PR. |
| Engineering Rigor | 5.5 | Commit described ("added better logging"); no tests. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.5 | Day Stable; week Stable; month Consistent; message-quality Repeat Pattern did not recur. |

## ashwinsk-medicodio — Medicodio — 4.3 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | 3 commits on POC branch; no PR, no README. |
| Engineering Rigor | 4.0 | "beautfied excel" ×2, 11 min apart; no tests. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | 3.5 | Repeated hand-formatting of the same output file. |
| Consistency Across Windows | 4.5 | Day Stable; week Insufficient Data; month Insufficient History; low-information messages now a Repeat Pattern (09-11 → today). |

Confidence Low: three rated dimensions on a POC branch; this score reflects commit hygiene, not the research itself.

## avinash-codio — Medicodio — 3.4 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4.0 | No code; opened `#451` prod promotion with empty body, merged in 4.5 min with 1 finding open. |
| Engineering Rigor | 3.5 | Badge-only prod PR body. |
| Code Review Contribution | 2.5 | `#450` approved "okay". |
| Observable Devin Leverage | 2.5 | `#451` finding unanswered — 4th consecutive report of prod promotion with open findings. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.5 | Day Regressed; week Stable; month Needs Improvement. |

Confidence Medium: one gate event and one approval is a thin day; the score is driven by the Repeat Pattern, not by absence of work.

## svh-medicodio — Global Codio — NR (2 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 3.5 | 0 activity; `#1358` (fixes to own `#1316`) and the 5 `#1331` legal-content decisions untouched. |
| Consistency Across Windows | 4.5 | Week Needs Attention (absent since 09-08); month Consistent (179 commits). |
| Others | NR | — |

## SaahilVishwakarma — Global Codio — NR (2 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 3.5 | `#1322` merged by others (24 colleague commits, 0 own since 09-07); `#1369` awaits his size-0 decision. |
| Consistency Across Windows | 4.5 | Week Needs Attention; month Insufficient History. |
| Others | NR | — |

## Murali-Shetty19 — Medicodio — NR (1 dimension)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4.0 | `#382` and `#434` closed unmerged (closer not captured); `#435` open; 0 commits. |
| Others | NR | — |

## sumedh-codio — Medicodio — NR (1 dimension)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Consistency Across Windows | 5.5 | 0 activity today; week Stable (90 commits); month Consistent. RPA self-merge pattern had no opportunity to recur. |
| Others | NR | — |

## How to read the spread

- **Observed Fact:** Four Solid scores today, and for the first time a Medicodio member (Medicodio-Amit) tops the grid — on the strength of four written disposition rounds, not output volume. The two biggest single-day rises (Vineeth +0.5, sameer +1.0) both came from visible rigor (a self-remediating Devin PR; a design doc + PHI-safe logging + 11 pre-merge fixes). The two biggest falls (Hitesh −1.0, avinash −0.8) came from one 8k-line unreviewed commit and one prod promotion with an open finding respectively.
- **Inference:** The Global Codio spread widened (6.1–7.3) because Devin delegation quality now separates members: those who delegated bounded tasks and let Devin close its own findings scored higher on Devin Leverage than the senior reviewers who remain in the remediate-approve-merge loop. The Medicodio spread is still governed by one habit — whether Devin findings get a written answer before a prod merge — which is why two members moved up ≥0.5 on a single well-written comment each.
- **Recommendation:** Do not rank individuals on these numbers; a 0.5 move is one good approval or one skipped gate. Use them to confirm two habits per product: Global Codio — pre-merge QA gate + second approver (the `#1365`/`#1360` delegation shape is the model to copy); Medicodio — "Devin check complete + one line per finding" before any `release/prod_*` merge (Medicodio-Amit's `#447` comments are the template). Re-score after a week, not a day.
