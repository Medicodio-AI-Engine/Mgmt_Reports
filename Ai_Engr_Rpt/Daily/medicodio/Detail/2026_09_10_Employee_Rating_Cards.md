# Employee Rating Cards — 2026-09-10

**Review window:** 2026-09-09 03:00 → 2026-09-10 03:00 UTC. Comparison windows: previous day 09-08, week 09-02 → 09-09, month 08-10 → 09-09. Companion to `2026_09_10_Mgmt_Activity_Report.md`; evidence cited there by PR/commit.

## Scoring limitations — read before the numbers

- **Devin session telemetry is missing.** `devin_session_search` returned HTTP 403 (`org.sessions.view`), as on every prior run. "Observable Devin Leverage" scores only what is visible on GitHub: `Co-Authored-By: Devin` trailers, PRs opened by `devin-ai-integration[bot]`, Devin Review findings and how they were dispositioned, and Devin QA-gate outcomes. A member who ran effective sessions that left no GitHub trace is under-scored here; a member whose work was architectural or investigative may correctly show little Devin use.
- **Jira and Sentry data unavailable** — Delivery is judged on merged/advanced GitHub work only; support, meetings and coordination are invisible except where written into a PR.
- **Volume is not productivity.** Commit, PR, file and line counts appear as context and never raise a score. Large single-day volume without independent review can lower Rigor.
- **One day is a small sample.** Consistency (10) uses week and month; the other five dimensions use the day with prior-report context. Never conclude from a single unusual day.
- **NR** = no in-window evidence for that dimension; excluded from the weighted average. Fewer than three rated dimensions → overall **NR**.
- Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**. Overall = Σ(score × weight) / Σ(weights of rated dimensions).
- Identity mapping by e-mail: `Akanksh RV`→akanksh-rv, `saijyoti`/`SaijyotiMeti`, `Sumedh Kaulgud`→sumedh-codio, `vineeth.kumar`→Pj-Vineeth-Kumar, `Vishnu Sai Karthik`→vishnu-saikarthik, `Amit Prakhar Pandey`→amit-pandey-medicodio, `sameer.mansur@`→sameer-s-mansur.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, abandoned without record, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anirudh-medicodio | Global Codio | **7.1** | Solid | 8.0 | 6.5 | 7.5 | 7.5 | 5.0 | 7.0 | High |
| saijyoti | Global Codio | **7.0** | Solid | 8.0 | 6.5 | 7.5 | 7.5 | 5.0 | 6.5 | High |
| akanksh-rv | Global Codio | **6.9** | Mixed | 7.5 | 7.0 | 8.0 | 6.0 | 5.5 | 6.5 | High |
| ragha82 | Global Codio | **6.8** | Mixed | 7.0 | 7.0 | NR | 7.0 | NR | 5.5 | Medium |
| Amrutha-Beedikar | Global Codio | **6.8** | Mixed | 6.5 | 7.5 | NR | 6.5 | 6.5 | 6.5 | Medium |
| sameer-s-mansur | Medicodio | **6.4** | Mixed | 7.5 | 6.5 | NR | 6.0 | 4.0 | 6.0 | High |
| amit-pandey-medicodio | Medicodio | **6.3** | Mixed | 8.0 | 7.5 | 3.0 | 6.0 | 4.5 | 6.5 | High |
| Pj-Vineeth-Kumar | Global Codio | **6.1** | Mixed | 7.0 | 5.5 | NR | 6.0 | 6.0 | 6.0 | Medium |
| jatinkushwaha-medicodio | Medicodio | **6.0** | Mixed | 7.5 | 6.5 | 3.0 | 6.5 | 4.5 | 6.0 | High |
| afifashaikh007 | Medicodio | **6.0** | Mixed | 6.0 | 6.5 | NR | NR | NR | 5.0 | Low (3 dimensions) |
| Hitesh Shanthakumar | Medicodio | **5.7** | Mixed | 6.0 | 5.5 | NR | NR | NR | 5.5 | Low (3 dimensions) |
| vishnu-saikarthik | Medicodio | **5.6** | Mixed | 6.0 | 5.5 | NR | NR | NR | 5.0 | Low (3 dimensions) |
| NandanDate-Medicodio | Medicodio | **5.4** | Mixed | 7.0 | 5.5 | 3.5 | 4.5 | NR | 5.0 | High |
| sumedh-codio | Medicodio | **4.6** | Needs Support | 7.0 | 3.5 | 2.5 | 3.5 | 6.0 | 4.5 | High |
| Murali-Shetty19 | Medicodio | **4.3** | Needs Support | 4.5 | 4.5 | NR | 3.5 | NR | 4.5 | Medium |
| avinash-codio | Medicodio | **3.9** | Needs Support | 5.0 | 4.0 | 2.5 | 3.0 | NR | 4.0 | Medium |
| svh-medicodio, SaahilVishwakarma, Medicodio-Amit, Shashvi1, ashwinsk-medicodio, shaheen-khan11, Karthik Khatavkar | — | NR | — | NR | NR | NR | NR | NR | NR | — (no in-window activity) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Movement vs 2026-09-09: anirudh 7.6→7.1, saijyoti 5.9→7.0, akanksh 5.9→6.9, Amrutha 6.0→6.8, Pj-Vineeth 7.1→6.1, jatin 6.4→6.0, amit 6.4→6.3, sameer 6.5→6.4, Nandan 6.5→5.4, sumedh 4.6→4.6, Murali 4.4→4.3, avinash 3.6→3.9, afifa 5.8→6.0, vishnu 5.6→5.6. ragha82 and Hitesh newly rated. Single-day moves of ≤ 0.5 are noise.

---

## anirudh-medicodio — Global Codio — 7.1 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | Merged `#1295` (89 files, svh's, open since 09-01), `#1312` (64 files, Saahil's), `#1339` (8) to `dev`; 6/6 deploys green; synced `#1323`. Against: `#1320` (137 files) still a draft. |
| Engineering Rigor | 6.5 | 5 targeted fixes on `#1312` (retracted a false RLS claim in docs). Against: `#1312` approved empty and merged at 17:29; Devin Review posted 17 new findings at 17:32; `#1339` merged 9 min after opening with 3 findings unanswered; QA gates 74/68/72 — all "known risks". |
| Code Review Contribution | 7.5 | 14,759-char Architect+EM review of `#1295` with 8 inline dispositions citing fixing commits — the longest review in the org today. Against: 2 of 3 approvals empty; reviewer, remediator and merger were the same person on all three. |
| Observable Devin Leverage | 7.5 | 2 Devin trailers in `#1295`; consumed 3 QA-gate verdicts. Against: 20 findings unanswered across `#1312`/`#1339`. Inference: post-merge gate is substituting for pre-merge disposition. |
| Automation of Repetitive Work | 5.0 | Gate/verdict logs still hand-written (`3944dc105c`, `37e8187cb4`). |
| Consistency Across Windows | 7.0 | Day Stable; week Improving; month Consistent (821 commits — context only). |

**Recommendation:** wait for the post-push Devin Review and disposition (or delegate) each finding before merging any PR > 50 files.

## saijyoti — Global Codio — 7.0 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | Own `#1338` merged; merged `#1342` (533 files) and `#1336` (110 files) after remediation; unblocked `#1337` with 8 fixes. |
| Engineering Rigor | 6.5 | 5 `test(` commits; 2 pre-existing test failures fixed; TDZ crash fixed. Against: 70 commits in one day, 65 on other authors' PRs; merged `#1336` 5 min after leaving a "[needs your decision]" thread open. |
| Code Review Contribution | 7.5 | Two Architect+EM reviews (8,068 / 8,305 chars), 7 inline "[was: verified Devin finding — fixed in …]" threads. Against: approved and merged PRs she had just pushed 45 and 20 commits to. |
| Observable Devin Leverage | 7.5 | 4 Devin trailers; the clearest finding dispositions in the org today. Against: 5 late findings on `#1336` at 00:24 → merged 01:29. |
| Automation of Repetitive Work | 5.0 | ≈ 25 mechanical hygiene commits (700-line splits, header backfills, primitive migrations) done by hand — Good Devin Candidate. |
| Consistency Across Windows | 6.5 | Day Improved; week Needs Attention (volume shape); month Consistent. |

**Recommendation:** delegate the hygiene sweep to Devin and use the time for one independent review where she has not pushed commits.

## akanksh-rv — Global Codio — 6.9 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#1336` merged (by saijyoti); `#1338` remediated and merged; `#1337` opened (68 files). Against: `#1337` still open with 5 findings. |
| Engineering Rigor | 7.0 | 5 `test(` commits; PRDs reconciled; data-driven ineligible-recipient rule replaces hard-coding. Against: 42 commits 00:16–04:44 UTC then a 68-file PR; findings on his PRs closed by a colleague. |
| Code Review Contribution | 8.0 | 11,339-char review of `#1338` with 7 evidence-linked threads plus an overflow comment for out-of-hunk notes — his first substantive written review in this dataset. Against: he wrote 24 of the fixes then approved. |
| Observable Devin Leverage | 6.0 | 0 trailers; `#1337` 5 findings open at window end; `#1336` findings dispositioned by saijyoti. |
| Automation of Repetitive Work | 5.5 | Review-log ledgers and header backfills still manual; PRD-delta commits repeat daily. |
| Consistency Across Windows | 6.5 | Day Improved; week Needs Attention; month Consistent. |

**Recommendation:** disposition `#1337`'s 5 findings himself (or via Devin) before anyone merges it.

## ragha82 — Global Codio — 6.8 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1339` opened and merged; `#1320` (anirudh's draft) advanced by 32 commits. Against: `#1320` still draft. |
| Engineering Rigor | 7.0 | Security-class fixes: cross-firm private-label leak, path-param validation, server-side pagination, 3 lost-update races; precise commit messages. Against: no `test(` commits; `#1339` merged with 3 findings unanswered. |
| Code Review Contribution | NR | No reviews or comments. |
| Observable Devin Leverage | 7.0 | Devin Review re-ran 8× on `#1320`; ≈ 20 findings resolved by his commits within the day. Inference: effective fix loop, no written dispositions. |
| Automation of Repetitive Work | NR | No evidence either way. |
| Consistency Across Windows | 5.5 | Day Improved; week Improving from a low base (2 commits on 09-08, 0 on 09-05–09-07); month Consistent. |

**Recommendation:** regression tests for the three lost-update races before `#1320` leaves draft.

## Amrutha-Beedikar — Global Codio — 6.8 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | Saahil's `#1322` moved from stale to remediated (13 commits). Against: own `#1323` idle 3rd day with 3 open findings; `#1322` not merged. |
| Engineering Rigor | 7.5 | First tests for `fill_pdf.py` "and fix the divergence they found"; pre-push pytest gate; 13 deferrals filed explicitly; single-writer refactor. Against: 3 new findings open at 15:44. |
| Code Review Contribution | NR | No reviews or comments. |
| Observable Devin Leverage | 6.5 | 9 findings resolved by commits within 20 min; 3 open; no written dispositions. |
| Automation of Repetitive Work | 6.5 | Pre-push gate for worker tests is automation in progress. |
| Consistency Across Windows | 6.5 | Day Improved; week Improving; month Consistent (low volume). |

**Recommendation:** close the 3 + 3 open findings on `#1322`/`#1323` and request independent review.

## sameer-s-mansur — Medicodio — 6.4 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#301`, `#302`, `#303` merged; `#304` opened the same day the Dev gap was found. |
| Engineering Rigor | 6.5 | RCA bodies on `#302`/`#304`; DB-sync divergence refusal; 4 "Review:" fix commits. Against: `#301`/`#303` badge-only bodies; no tests; second seed-vs-CHECK bug class in two days. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 6.0 | `#301` 2 findings fixed in 8 min; `#302` 1 and `#304` 2 unanswered. |
| Automation of Repetitive Work | 4.0 | Third manual UAT→Dev back-port (`#304`) after two recommendations for a drift script. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

**Recommendation:** CHECK-constraint validation test over seeds (Good Devin Candidate).

## amit-pandey-medicodio — Medicodio — 6.3 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | 4 PRs merged (`#629`, `#630`, `#561`, `#562`) plus 2 promotions merged. |
| Engineering Rigor | 7.5 | RCA-quality bodies on every fix; follow-up fix within `#561`. Against: 0 tests across 4 PRs (0 `test(` in app repos all week). |
| Code Review Contribution | 3.0 | 4 approvals, all empty, including `#558` with 5 open Devin findings. |
| Observable Devin Leverage | 6.0 | `#561` finding fixed in 17 min; 3 PRs "No Issues Found". Against: approved `#558` past 5 findings. |
| Automation of Repetitive Work | 4.5 | Promotion approvals repeated daily without a template. |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

**Recommendation:** ask Devin for unit tests on `emMethodForCode` priority and the canEdit lock.

## Pj-Vineeth-Kumar — Global Codio — 6.1 Mixed (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1342` opened after 4 days of recommendations and merged the same day. Against: `#1333` (Devin-authored, 19 trailers) closed unmerged with no comment. |
| Engineering Rigor | 5.5 | Rules charter → scoped rulebooks is a real process fix. Against: 533-file PR needed 45 fixes from the reviewer within 8 h; generic "Refactor code structure" commit. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 6.0 | Yesterday's model Devin PR abandoned without record; 0 trailers and 0 dispositions today. |
| Automation of Repetitive Work | 6.0 | Skills/rules refactor reduces repeated rule lookups. |
| Consistency Across Windows | 6.0 | Day Regressed; week Stable; month Consistent. |

**Recommendation:** comment `#1333`'s disposition so the Devin work is traceable.

## jatinkushwaha-medicodio — Medicodio — 6.0 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#559`, `#628` merged; 2 promotions merged; 2 prod promotions opened. |
| Engineering Rigor | 6.5 | `#559` written body + unit-test guard commit. Against: 4 promotion PRs badge-only; `#558` to UAT with 5 findings. |
| Code Review Contribution | 3.0 | 4 approvals: 3 empty, 1 "ok". |
| Observable Devin Leverage | 6.5 | `#559` 2 findings fixed in 8 min ("address Devin review"). Against: 10 findings carried on `#558`/`#557`/`#626`. |
| Automation of Repetitive Work | 4.5 | Promotion bodies still manual/badge-only (3rd recommendation). |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

**Recommendation:** disposition the 10 promotion findings before the prod merge.

## afifashaikh007 — Medicodio — 6.0 Mixed (Low confidence, 3 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | Guidelines chain wired; fix landed. Against: `feat/inpatient-engine` still has no PR (4th report). |
| Engineering Rigor | 6.5 | Timestamped real-profile test with recorded findings; fix commit explains the merged-condition bug. Against: no review path. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | Branch invisible to Devin Review; nothing to assess. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.0 | Day Stable; week Needs Attention; month Insufficient History. |

**Recommendation:** open the draft PR today.

## Hitesh Shanthakumar — Medicodio — 5.7 Mixed (Low confidence, 3 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | Inpatient chart pane, review page and PCS rail advanced; "never saved" bug fixed. Against: no PR. |
| Engineering Rigor | 5.5 | Clear bug-naming commits; no tests; no review. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.5 | Day Insufficient Data; week Stable; month Consistent (77 react commits — context). |

**Recommendation:** open a draft PR before the branch grows further.

## vishnu-saikarthik — Medicodio — 5.6 Mixed (Low confidence, 3 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | CDI Phase 2 sourcing and injury-merge fix landed on the shared branch; no PR (3rd report). |
| Engineering Rigor | 5.5 | Fix and feature separated; no tests; no review. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.0 | Day Stable; week Stable; month Insufficient History. |

**Recommendation:** co-open the `feat/inpatient-engine` draft PR.

## NandanDate-Medicodio — Medicodio — 5.4 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#438` merged to uat; `#439` promoted to prod. |
| Engineering Rigor | 5.5 | `#438` findings were dispositioned yesterday. Against: merged own PR after a 2-char approval; prod merge 1 min 39 s after opening with 4 findings unanswered. |
| Code Review Contribution | 3.5 | One approval, "okay ", on a prod PR with open findings. |
| Observable Devin Leverage | 4.5 | Yesterday 5 written dispositions (model); today 4 prod findings ignored. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.0 | Day Regressed; week Stable; month Consistent. |

**Recommendation:** disposition `#439`'s 4 findings post-hoc; no prod merge with open findings.

## sumedh-codio — Medicodio — 4.6 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | SIS export end-to-end; "both submits have now run for real". |
| Engineering Rigor | 3.5 | `#19`: 33 commits, +3,596/−1,832, empty body, self-merged 11 s after opening; no tests; no CI. 3rd such merge in 48 h. |
| Code Review Contribution | 2.5 | 3 empty approvals, incl. prod `#303` 46 s after opening and `#302` with 1 open finding. |
| Observable Devin Leverage | 3.5 | Repo has no Devin Review; approved past an open finding elsewhere. |
| Automation of Repetitive Work | 6.0 | The work itself automates SIS charge entry; selector reconnaissance still manual. |
| Consistency Across Windows | 4.5 | Day Regressed; week Needs Attention; month Needs Improvement. |

**Recommendation:** add a body to `#19`; enable required review on `main`.

## Murali-Shetty19 — Medicodio — 4.3 Needs Support (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4.5 | `#560` opened and closed unmerged within 72 min, no comment. |
| Engineering Rigor | 4.5 | Body, `.env.example` and docs included. Against: 1 finding unanswered; closed silently. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3.5 | 1 new + 13 prior findings unanswered. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.5 | Day Regressed; week Needs Attention; month Needs Improvement. |

**Recommendation:** one Devin session to disposition the 14 open findings, then re-open `#560`.

## avinash-codio — Medicodio — 3.9 Needs Support (Medium confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | `#439` prod promotion opened. Against: `#415` (30 files) closed unmerged after 8 days, no comment; `feat/checkpoint` no PR (3rd report). |
| Engineering Rigor | 4.0 | Badge-only prod body; `#415` fate undocumented. |
| Code Review Contribution | 2.5 | "ok" on `#438` (findings were already answered — acceptable outcome, no evidence of what was checked). |
| Observable Devin Leverage | 3.0 | 0 trailers; work kept off PRs. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.0 | Day Stable; week Needs Attention; month Needs Improvement. |

**Recommendation:** draft PR for `feat/checkpoint`; comment why `#415` closed.

## Not rated

- **svh-medicodio, SaahilVishwakarma, Medicodio-Amit, Shashvi1, ashwinsk-medicodio, shaheen-khan11, Karthik Khatavkar:** no commits, reviews or comments in window — NR, not a low score. Note (Observed Fact): svh's `#1295` and Saahil's `#1312`/`#1322` were remediated and merged by anirudh and Amrutha.
- **devin-ai-integration[bot]:** tool. 6 QA-gate PRs opened, 6 verdicts posted, 4 older QA PRs and `#1333` closed unmerged.

---

## How to read the spread

- **Observed Fact:** Two members score Solid, twelve Mixed, three Needs Support. The Solid/Mixed boundary (7.1 / 7.0 / 6.9) is within a single day's noise — anirudh, saijyoti and akanksh are the same tier. All three earned it through written, evidence-linked reviews; all three lost points for approving and merging PRs they had just remediated. Every Medicodio approval today (13/13) was ≤ 5 characters; every Global Codio approval was accompanied by an 8k–15k-char review from the same person.
- **Observed Fact:** Needs Support scores come from controls, not output. sumedh delivered the most functional RPA progress of the week and still scores 4.6 because an empty-body self-merge to `main` in 11 s (third in 48 h) is the single behaviour the rubric weights most heavily. avinash and Murali are low because work was abandoned or kept off PRs, not because of volume.
- **Inference:** Global Codio's rating rise (saijyoti +1.1, akanksh +1.0, Amrutha +0.8) reflects a real change in review writing quality, not a change in independence — five large PRs today had no approver who had not also pushed to them. Medicodio's fall (Nandan −1.1) is a single-day regression on a prod PR and should be watched, not concluded on.
- **Inference:** Devin leverage scores are Global-Codio-heavy (27 trailers vs 0) because that is where Devin Review is integrated and where findings are being answered in writing. Absent telemetry, Medicodio members who use Devin sessions without trailers are under-scored; the correction is the missing `org.sessions.view` permission, not a lower bar.
- **Recommendation:** treat the seven Repeat Patterns in the activity report as team fixes with owners (second approver > 50 files; disposition-before-prod; draft-PR-within-24 h; RPA branch protection; promotion body script; drift script; make `Mgmt_Reports` private). Re-rate on 09-11 for direction, not on the second decimal.
