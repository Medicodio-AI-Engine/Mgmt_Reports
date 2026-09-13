# Employee Rating Cards — 2026-09-13

**Review window:** 2026-09-12 03:00 UTC → 2026-09-13 03:00 UTC (Saturday). Comparison windows: previous working day 09-11, week 09-06 → 09-13, month 08-14 → 09-13. Companion to `2026_09_13_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`Missing required permission 'org.sessions.view'`) for the **11th consecutive run**, and fetching a known session ID also returned 403. Prompt quality, ACU/effort, tests-requested and correction burden are unobservable. "Observable Devin Leverage" is scored only from GitHub-visible evidence: Devin-authored PRs, `Co-Authored-By: Devin` trailers, Devin Review findings and how humans dispositioned them, and Devin QA-gate verdict comments. Claude session/co-author markers are **not** counted as Devin usage.
- **Jira and production telemetry (Sentry) were not callable.** Ticket flow, incident load and support work are invisible; coordination-heavy days are under-observed, not under-performing.
- **Weekend window.** Only three actors produced any event, all between 03:06 and 05:05 UTC. Members with no activity are **NR**, not low-scored — a quiet Saturday is not a performance signal.
- **Volume is never scored.** Commit, PR, file and line counts appear only as context.
- **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average; fewer than three rated dimensions → overall **NR**. Confidence reflects how much of the member's work is visible in GitHub.
- **Identity merges (e-mail matched):** `Akanksh RV` = `akanksh-rv`, `Pj-Vineeth-Kumar` = `vineeth.kumar`, `saijyoti` = `SaijyotiMeti`. `devin-ai-integration[bot]` is a tool and is not rated. Two commits today carry placeholder/corrupt `Co-Authored-By: Devin` e-mails; attribution was resolved from the committing author, not the trailer.
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

Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pj-Vineeth-Kumar | Global Codio | **7.7** | Solid | 7.0 | 7.5 | NR | 9.0 | 8.0 | 7.5 | High |
| akanksh-rv | Global Codio | **6.7** | Mixed | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 6.5 | High |
| SaijyotiMeti | Global Codio | NR | — | 5.0 | NR | NR | 4.0 | NR | NR | Low (2 dimensions rated) |
| anirudh-medicodio, ragha82, Amrutha-Beedikar, svh-medicodio, SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, Saturday) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, shaheen-khan11, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, Saturday) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Weighted overall = Σ(score × weight) / Σ(weights of rated dimensions). Pj-Vineeth-Kumar: (7.0×25 + 7.5×25 + 9.0×15 + 8.0×10 + 7.5×10) / 85 = 7.7. akanksh-rv: (7.0×25 + 7.5×25 + 6.0×15 + 6.5×15 + 5.0×10 + 6.5×10) / 100 = 6.7.

Change vs 2026-09-12 cards: Pj-Vineeth-Kumar 7.3 → **7.7**; akanksh-rv 6.8 → **6.7**; SaijyotiMeti 6.6 → **NR** (no in-window activity, 2 dimensions rated). All other members move to NR for this window (no observed activity on a Saturday) — this is not a score change and must not be read as a decline.

## Cards

## Pj-Vineeth-Kumar — Global Codio — Overall 7.7 (Solid) — Confidence: High

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1365` rebased onto `dev` (12-commit series re-landed 03:25–03:26) and advanced with two targeted fixes (`0da6f05af`, `ae772edf9`). Against: PR still open on day 2 with no human review requested, and `feat/hr-portal-revamp` remains without a PR for the 3rd report. |
| Engineering Rigor | 7.5 | The validation fix ships with a new test file for the profile timezone card (Save disabled while `!isValidTimezone`, legacy + empty covered); the audit/security fix deletes five duplicated private `formatTimestamp` helpers rather than patching each. Against: a 73-file diff still lacks a regression suite for the migrated rendering sites. |
| Code Review Contribution | NR | No review events in-window. |
| Observable Devin Leverage | 9.0 | All four Devin Review findings (03:47) dispositioned by 03:59 — two fixed with SHAs named in-thread, two rejected with specific technical reasons (`localCalendarDay()` consumers are calendar-date inputs; RSC-hydration path unreachable because every consumer is a client component fed after mount). PR is Devin-driven with human ownership. |
| Automation of Repetitive Work | 8.0 | The whole series removes a real repetition: one shared formatter replacing ad-hoc rendering at 45 call sites plus five duplicated private helpers found and deleted today. Not yet locked in with a lint rule. |
| Consistency Across Windows | 7.5 | Day Stable (same disposition discipline as 09-11's 10 findings); week Improving (133 commits across both identities, two Devin-driven PRs with every finding answered); month Improving (316 commits; written dispositions now his default). |

Inference: he is the clearest example in the org of Devin used for leverage rather than volume — the human decisions (which helper survives, what is intentional) stay with him and are written down. Recommendation: attach a Devin-generated regression suite to `#1365` and request a named reviewer; a 73-file diff with no human reader is the only thing capping Delivery.

## akanksh-rv — Global Codio — Overall 6.7 (Mixed) — Confidence: High

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1366` (74 files) landed on `dev` with 31 findings remediated and 37 quality gates recorded. Against: merged 16 minutes after his own review said "this shouldn't merge until someone decides", with two unmet PRD acceptance criteria and six NEEDS-DECISION items unresolved and unwaived in writing; the post-merge QA gate then returned NOT READY and its fix PR `#1371` was left open at window close, alongside `#1358` and `#1369` from the two previous days. |
| Engineering Rigor | 7.5 | Found a guard test that was failing on the branch and proved a prior cycle's "gates green" record wrong; found a foreign-table read outside RLS and moved it behind a service; found and fixed two regressions his *own* earlier fixes had introduced (fail-soft de-escalation on a read failure; Retry reading merged worst-of delivery status); verified gates beyond exit codes (0 Nx-cache hits, every block `1 passed, 1 total`, 510 tests). Against: the two acceptance criteria he identified as unmet shipped anyway, and the QA gate found three product defects in exactly those surfaces. |
| Code Review Contribution | 6.0 | 11,203-character architect/EM review with 4 inline threads and a 10-row Stop-and-Check table — the most useful review artefact in the org this week, and it changed the code. Capped at 6 because it was not independent (the branch's final 22 remediation commits are his), his approval body was 8 characters, and he merged past his own written blocker. |
| Observable Devin Leverage | 6.5 | Each Devin Review comment individually verified against the code — three real (two of them his own regressions), one stale, PR-size ones advisory: the strongest disposition standard observed. Against: no delegation of an almost entirely mechanical 31-finding remediation; the post-merge NOT READY verdict and its three PRODUCT_FAILUREs went unanswered in-window. |
| Automation of Repetitive Work | 5.0 | Hand-written `docs(review-logs)` commit again (5th report: 09-04, 09-06, 09-07, 09-11, today) and a hand-transcribed 37-gate matrix while `ci.yml` remains `workflow_dispatch`-only. Repetition is visible in his own commit messages; no automation attempted. |
| Consistency Across Windows | 6.5 | Day Stable vs 09-11 (same depth, same lack of independence); week Stable (166 commits, three long-form reviews, all on branches he had committed to); month Consistent (631 commits; the two structural weaknesses unchanged since 08-26). |

Inference: with the author absent on a Saturday he chose to ship a feature he had personally repaired; that may have been the right call, but no written decision exists on the PR, and the QA gate's three confirmed defects landed on `dev` as a result. Recommendation: post the written decision and merge `#1371` before the next `dev → uat` promotion; delegate mechanical remediation to Devin so approval can stay independent.

## SaijyotiMeti — Global Codio — Overall NR — Confidence: Low (2 dimensions rated)

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | His `#1366` merged in-window — but the remediation (31 findings / 22 commits), the review, the approval and the merge were another member's, and the reviewer's two unmet PRD acceptance criteria were addressed to him and never answered. Rated because the outcome of his own PR is in-window evidence about follow-through. |
| Engineering Rigor | NR | No in-window work of his to assess. (Context, not scored: `#1366` carried a 12,372-character PRD-mapped body — the reason the review could be that specific — and the reviewer corrected its hygiene section as inaccurate: the branch adds ~25 exported surfaces, a DTO field and a query-key member.) |
| Code Review Contribution | NR | No review events in-window. |
| Observable Devin Leverage | 4.0 | Six Devin Review findings on his PR were closed by the reviewer's commits or left standing; the three PRODUCT_FAILUREs the post-merge gate found in his feature's surfaces were picked up by Devin's own fix PR, not by him. |
| Automation of Repetitive Work | NR | No in-window evidence. |
| Consistency Across Windows | NR | Week: 170 commits and substantial delivery, but on two PRs (`#1322`, `#1366`) closing decisions and the merge were another member's; month: 575 commits. Not scored on a weekend with two rated dimensions. |

Recommendation: reply in-thread with a decision on the two acceptance criteria and take ownership of `#1371`.

## Members not rated this window

**Global Codio:** anirudh-medicodio, ragha82, Amrutha-Beedikar, svh-medicodio, SaahilVishwakarma — no commits, reviews or comments in the window. Their open PRs (`#1363` 110 files, `#1362`, `#1364`) received no events.

**Medicodio:** amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, shaheen-khan11, Shashvi1 — zero activity across all five Medicodio repositories.

NR here means "no in-window evidence", not a judgement. Their most recent rated window is 2026-09-12.

## How to read the spread

- **Observed Fact.** Three people produced events in a 2-hour window; two are rated on three or more dimensions. Two scores moved: Vineeth up (every Devin finding dispositioned in 12 minutes, a real repetition removed), akanksh slightly down (same exceptional review depth, but a second occurrence of merging past his own written blocker, and a post-merge NOT READY verdict left open). 93 % of the week's human review bodies and 95 % of the month's are ≤10 characters; today's 11.2k-character review is the outlier, not the norm.
- **Inference.** The gap between the two top scores is about *timing and independence*, not skill. The org's two best Devin practices — write down every disposition (Vineeth) and verify every finding against code (akanksh) — already exist; what is missing is a rule that puts the verification before the merge and a second reader who did not write the diff.
- **Recommendation.** (1) Make the QA-gate verdict a pre-merge check and give each resulting fix PR a same-day owner — three consecutive NOT READY verdicts have now arrived post-merge with all three fix PRs still open. (2) Require a non-committer approval on `dev`. (3) A dimension is NR far too often for Medicodio members because Jira and session telemetry are unavailable — granting `org.sessions.view` and exposing a Jira tool would raise confidence more than any behavioural change.
