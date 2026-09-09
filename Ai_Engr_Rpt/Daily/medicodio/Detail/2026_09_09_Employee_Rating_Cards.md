# Employee Rating Cards — 2026-09-09

**Review window:** 2026-09-08 03:00 → 2026-09-09 03:00 UTC. Comparison windows: previous day 09-07, week 09-01 → 09-08, month 08-09 → 09-08. Companion to `2026_09_09_Mgmt_Activity_Report.md`; evidence cited there by PR/commit.

## Scoring limitations — read before the numbers

- **Devin session telemetry is missing.** `devin_session_search` returned HTTP 403 (`org.sessions.view`), as on every prior run. "Observable Devin Leverage" scores only what is visible on GitHub: `Co-Authored-By: Devin` trailers, PRs opened by `devin-ai-integration[bot]`, Devin Review findings and how they were dispositioned, and Devin QA-gate outcomes. A member who ran effective sessions that left no GitHub trace is under-scored; a member who ignored findings is scored on that.
- **Jira and Sentry data unavailable** — Delivery is judged on merged/advanced GitHub work only; support, meetings and coordination are invisible except where written into a PR.
- **Volume is not productivity.** Commit, PR, file and line counts appear as context and never raise a score. Large single-day volume with unreviewed output can lower Rigor.
- **One day is a small sample.** Consistency (10) uses week and month; the other five dimensions use the day with prior-report context. Never conclude from a single unusual day.
- **NR** = no in-window evidence for that dimension; excluded from the weighted average. Fewer than three rated dimensions → overall **NR**.
- Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**. Overall = Σ(score × weight) / Σ(weights of rated dimensions).

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anirudh-medicodio | Global Codio | **7.6** | Solid | 8.0 | 7.5 | 8.0 | 8.5 | 5.0 | 7.5 | High |
| Shashvi1 | Medicodio | **7.5** | Solid | 7.5 | 8.0 | NR | 6.5 | NR | NR | Low (3 dimensions) |
| Pj-Vineeth-Kumar | Global Codio | **7.1** | Solid | 7.0 | 7.0 | NR | 9.0 | 5.0 | 6.5 | Medium |
| NandanDate-Medicodio | Medicodio | **6.5** | Mixed | 7.0 | 7.5 | 4.0 | 8.0 | 5.0 | 5.5 | High |
| sameer-s-mansur | Medicodio | **6.5** | Mixed | 7.5 | 7.0 | NR | 5.5 | 4.5 | 6.0 | High |
| jatinkushwaha-medicodio | Medicodio | **6.4** | Mixed | 8.0 | 7.0 | 3.0 | 7.0 | 4.5 | 6.5 | High |
| amit-pandey-medicodio | Medicodio | **6.4** | Mixed | 8.0 | 7.0 | 3.0 | 7.0 | 5.0 | 6.5 | High |
| svh-medicodio | Global Codio | **6.0** | Mixed | 6.0 | 7.0 | NR | 4.5 | 5.5 | 6.5 | High |
| Amrutha-Beedikar | Global Codio | **6.0** | Mixed | 5.5 | 6.5 | NR | 5.5 | NR | 6.5 | Medium |
| akanksh-rv | Global Codio | **5.9** | Mixed | 6.0 | 6.5 | NR | 5.0 | 5.5 | 6.0 | Medium |
| saijyoti | Global Codio | **5.9** | Mixed | 6.0 | 6.0 | NR | NR | 5.5 | 6.0 | Medium |
| afifashaikh007 | Medicodio | **5.8** | Mixed | 6.0 | 6.0 | NR | NR | 5.0 | 5.5 | Medium |
| Medicodio-Amit | Medicodio | **5.7** | Mixed | 6.5 | 6.0 | NR | 4.0 | 5.0 | 6.0 | Medium |
| vishnu-saikarthik | Medicodio | **5.6** | Mixed | 6.0 | 5.5 | NR | NR | NR | 5.0 | Medium |
| sumedh-codio | Medicodio | **4.6** | Needs Support | 6.5 | 3.5 | 2.5 | NR | 5.5 | 5.0 | Medium |
| Murali-Shetty19 | Medicodio | **4.4** | Needs Support | 5.5 | 4.5 | NR | 2.5 | NR | 4.5 | Medium |
| avinash-codio | Medicodio | **3.6** | Needs Support | 5.0 | 3.5 | 2.0 | 2.5 | NR | 4.0 | Medium |
| ragha82, SaahilVishwakarma, ashwinsk-medicodio, hitesh, shaheen-khan11, Karthik Khatavkar | — | NR | — | NR | NR | NR | NR | NR | NR | — (no in-window activity) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

---

## anirudh-medicodio — Global Codio — 7.6 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#1284` (183 files) merged to `dev`, deploy 1/1; `#1321` (Devin regression PR) merged into the feature branch; 9 `test(` commits closed the 80-failure gate matrix; `E2E_SUPERADMIN` fixed after six reports. Against: `#1320` (119 files) still a WIP draft. |
| Engineering Rigor | 7.5 | Gate matrix documented; RCA-quality fixes on document-catalog. Against: merged `#1284` 4 min after his own "conditional on 6 decisions (2 live bugs)" review; QA gate returned NOT READY post-merge. |
| Code Review Contribution | 8.0 | 11,439-char Architect+EM review with 4 "needs decision" threads — the only substantive human review in the org today. Against: reviewer, approver and merger were the same person. |
| Observable Devin Leverage | 8.5 | Merged Devin's `#1321`; unblocked and consumed two QA-gate verdicts (`#1332`, `#1335`). Inference: broadest Devin use in the org. |
| Automation of Repetitive Work | 5.0 | Gate matrix still hand-written into `docs/review`. |
| Consistency Across Windows | 7.5 | Day Improved; week Improving; month Consistent. |

**Recommendation:** make the Devin QA gate a pre-merge check for > 800-line PRs; require a second approver on them.

## Pj-Vineeth-Kumar — Global Codio — 7.1 Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1333` PRD + v1 implementation advanced through 6 review rounds in one day (open, 1 finding left). Against: `feat/mobbin-trails` +6,700 lines with no PR (3rd report). |
| Engineering Rigor | 7.0 | `#1333`: tests (`1de2d3ab`, `95051cbc`), safety hardening rounds, product decisions recorded in the PRD. Against: 99- and 60-file commits unreviewed on the other branch. |
| Code Review Contribution | NR | Reviewed no one else's PR. |
| Observable Devin Leverage | 9.0 | 19 Devin-trailer commits; PRD → decisions (§15 Q1/Q2/Q7) → implement → review loop with SHAs — the rubric's intended pattern. |
| Automation of Repetitive Work | 5.0 | The `.docx` conversion *is* automation of a manual ChatGPT-paste workflow (Inference from PR body), but his own repetitive no-PR habit is unaddressed. |
| Consistency Across Windows | 6.5 | Day Improved; week Improving; month Consistent — offset by the persistent no-PR pattern. |

**Recommendation:** open `feat/mobbin-trails` as a PR and run it through the `#1333` loop.

## Shashvi1 — Medicodio — 7.5 Solid (Low confidence, 3 dimensions)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#437` POS normalisation merged to uat same day with tests and guide. |
| Engineering Rigor | 8.0 | RCA body, tests, implementation guide, `sys.path` removed after review — model fix PR. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 6.5 | 3 findings resolved by follow-up commit within 20 min; 1 late finding unanswered; no written replies. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | NR | 2 commits this week, 6 active days in the month — insufficient. |

**Recommendation:** delegate the repo-wide sweep of the same defect class to Devin.

## NandanDate-Medicodio — Medicodio — 6.5 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#438` (35 files) opened with 2 regression fixes same day; merged `#436`, `#437` to uat. Open at window end. |
| Engineering Rigor | 7.5 | RCA from one chart in body; config regression (`04d7512c`) caught and fixed; guide updated. Against: no config-invariant test added. |
| Code Review Contribution | 4.0 | "okay" ×2; `#436` merged with 1 finding open. |
| Observable Devin Leverage | 8.0 | 5 written dispositions on `#438` with SHAs and owner confirmation → 5/5 resolved. First observed from him this month. |
| Automation of Repetitive Work | 5.0 | Manual config-bundle edits; repetition acknowledged in the fix message, not automated. |
| Consistency Across Windows | 5.5 | Day Improved; week Stable; month Needs Improvement (19 one-word approvals). |

**Recommendation:** apply the `#438` disposition standard to every PR you approve.

## jatinkushwaha-medicodio — Medicodio — 6.4 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#623`, `#554`, `#625`, `#556` merged; Dev→UAT promoted; probe PR closed. |
| Engineering Rigor | 7.0 | Descriptive bodies; 3 Devin rounds fixed within 43 min; −734 dead config. Against: no tests; `#556` merged with 4 findings open. |
| Code Review Contribution | 3.0 | 8 approvals, all 0-char, incl. prod `#298` merged 59 s after open. |
| Observable Devin Leverage | 7.0 | Findings fixed promptly ("address Devin review", "Devin round 2"); no written dispositions; 0 trailers. |
| Automation of Repetitive Work | 4.5 | Probe PR pattern persists (3rd report); promotions manual. |
| Consistency Across Windows | 6.5 | Day Improved; week Stable; month Consistent. |

**Recommendation:** `workflow_dispatch` for the unit-test job; one sentence per approval.

## amit-pandey-medicodio — Medicodio — 6.4 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#555`, `#624` merged; 3 prod promotions merged; Dev→UAT opened and merged. |
| Engineering Rigor | 7.0 | RCA bodies; findings fixed pre-merge. Against: no tests for the add-on state machine that produced 3 bugs. |
| Code Review Contribution | 3.0 | 8 approvals, 0-char; `#556` with 4 open findings; `#300` prod with 3, merged in 4 min. |
| Observable Devin Leverage | 7.0 | 2 Devin trailers closing his own findings; as reviewer, findings not used. |
| Automation of Repetitive Work | 5.0 | Promotions manual (daily). |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

**Recommendation:** paste the open-findings count into every prod approval; resolve or reject each.

## sameer-s-mansur — Medicodio — 6.5 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | 6 PRs opened, 6 merged incl. 2 prod; model move shipped to all envs. |
| Engineering Rigor | 7.0 | Log-evidenced RCAs; test per fix; error-code collision fixed in 30 min. Against: `#295` merged with 3 findings unread in 54 s. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5.5 | `#299` 5/5 findings resolved; `#295`, `#298`, `#300` findings (1+3+3) unanswered at merge. |
| Automation of Repetitive Work | 4.5 | Prompt ports between envs by hand again (`#295`/`#296`). |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent; the prod-findings pattern is on its 4th report. |

**Recommendation:** CI check for Dev/UAT prompt + assertion drift.

## svh-medicodio — Global Codio — 6.0 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | `#1334` (43 files) and `#1331` opened; `#1316` (97 files) idle 4th day; `#1295` (56) idle. |
| Engineering Rigor | 7.0 | ADR, explicit `revert(` with reason, DB docs, spec fixes. Against: three unrelated fixes on one branch; migration BUG finding unanswered. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4.5 | 21 Devin findings open across 3 PRs, none answered. |
| Automation of Repetitive Work | 5.5 | `/check` logs by hand; retention floor now enforced in schema (a form of automating a manual check — Inference). |
| Consistency Across Windows | 6.5 | Day Stable; week Stable; month Consistent. |

**Recommendation:** one Devin session to disposition all 21 findings.

## akanksh-rv — Global Codio — 5.9 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | `#1336` (88 files) opened after 42 commits; `#1305` (109 files) idle 5th day. |
| Engineering Rigor | 6.5 | PRD, 3 test commits, escalation notes. Against: 88-file PR; 5 findings open; 40 commits in 4 h with 3 "repair what my changes invalidated" fixes. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5.0 | 5 findings on `#1336` open at window end (PR 20 min old — Inference: not yet engaged). |
| Automation of Repetitive Work | 5.5 | Atlas regen ×2 and 4 review logs by hand. |
| Consistency Across Windows | 6.0 | Day Insufficient; week Needs Attention (very large PRs); month Consistent. |

**Recommendation:** close/split `#1305`, then split `#1336` by layer.

## Amrutha-Beedikar — Global Codio — 6.0 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | `#1323` synced with dev; not yet merged (3rd day). |
| Engineering Rigor | 6.5 | 5-file conflict resolution documented per file. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5.5 | 3 new findings unanswered today (disposition table 09-08 shows she can). |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6.5 | Day Stable; week Improving; month Consistent. |

**Recommendation:** disposition the 3 findings and request review.

## saijyoti — Global Codio — 5.9 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 8 commits advancing the questionnaire agent; no PR. |
| Engineering Rigor | 6.0 | PRD updated with code; −142 dead UI. Against: no tests observed; unreviewed. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No Devin artefacts (Claude trailers only). |
| Automation of Repetitive Work | 5.5 | Guard exemptions case by case. |
| Consistency Across Windows | 6.0 | Day Insufficient; week Stable; month Consistent. |

**Recommendation:** draft PR + Devin-written guard tests.

## afifashaikh007 — Medicodio — 5.8 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 7 commits, +3,500 lines on the inpatient branch; nothing reviewable. |
| Engineering Rigor | 6.0 | Tests bundled with gate changes; precise messages. Against: no PR, no review of any kind. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | Branch invisible to Devin. |
| Automation of Repetitive Work | 5.0 | Gate-by-gate manual discovery. |
| Consistency Across Windows | 5.5 | Day Stable; week Needs Attention (no PR, 3rd report); month Insufficient History. |

**Recommendation:** draft PR today.

## Medicodio-Amit — Medicodio — 5.7 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | `#436` merged to uat same day. `#393` (46 files) draft since 08-25. |
| Engineering Rigor | 6.0 | Guide in same PR. Against: no test; 1 finding unanswered. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4.0 | 1 finding, unanswered at merge (after 19 dispositions yesterday — small sample). |
| Automation of Repetitive Work | 5.0 | Golden tests still absent (3rd report). |
| Consistency Across Windows | 6.0 | Day Regressed; week Stable; month Consistent. |

**Recommendation:** Devin golden tests for the chart assembler.

## vishnu-saikarthik — Medicodio — 5.6 Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 2 large commits on the inpatient branch; no PR. |
| Engineering Rigor | 5.5 | 65-file field move unreviewed; defaults documented. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5.0 | Day Stable; week Stable; month Insufficient History. |

**Recommendation:** co-own the inpatient draft PR.

## sumedh-codio — Medicodio — 4.6 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | PCP export flow landed on `main` (13 commits); follow-ups shipped. |
| Engineering Rigor | 3.5 | `#17` +5,509 lines, 67 commits, **empty body**, self-merged 12 s after open; `#18` same. No CI, no review. Good commit messages do not offset this. |
| Code Review Contribution | 2.5 | 2 empty approvals; merged `#295` in 54 s with 3 findings. |
| Observable Devin Leverage | NR | Repo has no Devin Review. |
| Automation of Repetitive Work | 5.5 | The RPA work automates manual claim export (Inference), but his own selector-fix loop remains manual. |
| Consistency Across Windows | 5.0 | Day Regressed; week Stable; month Insufficient History. |

**Recommendation:** Devin Review + required reviewer on the RPA repo; PR bodies.

## Murali-Shetty19 — Medicodio — 4.4 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | `#434`, `#435` opened; `#382` (08-21) still open — 3 PRs, same topic, none merged. |
| Engineering Rigor | 4.5 | `#435` body good; `#434` badge-only on 30 files; 13 findings unanswered. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 2.5 | 13 findings ignored (2nd report). |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.5 | Day Regressed; week Needs Attention; month Insufficient History. |

**Recommendation:** disposition all 13 findings; close superseded PRs.

## avinash-codio — Medicodio — 3.6 Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | +2,957-line checkpoint commit, no PR; `#415` (30 files) idle since 09-01. |
| Engineering Rigor | 3.5 | No PR, no body, no tests observed. |
| Code Review Contribution | 2.0 | "Okay"/"okay" twice in one minute on `#435` with 7 findings open. |
| Observable Devin Leverage | 2.5 | Findings ignored as reviewer (3rd report); own work hidden from Devin. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4.0 | Day Stable (negative); week Needs Attention; month Insufficient History. |

**Recommendation:** draft PR for `feat/checkpoint`; approvals only with a written status.

---

## How to read the spread

**Observed Fact.** Eighteen members had in-window GitHub activity; six had none and are NR. The spread runs 3.6 → 7.6 with a median of 6.0. Only one human review body in 29 exceeded ten characters. Every Medicodio member who approves PRs scores ≤ 4.0 on Code Review Contribution; every Global Codio member except anirudh is NR there because they reviewed nothing. Observable Devin Leverage separates the top from the middle: the three highest Devin scores (vineeth 9.0, anirudh 8.5, Nandan 8.0) each come from written, SHA-linked dispositions or Devin-authored PRs; the three lowest (Murali, avinash 2.5; Medicodio-Amit 4.0) come from findings left open at approval or merge.

**Inference.** Delivery is not the differentiator — fourteen of seventeen score 6.0–8.0 there. Rigor and review practice are. The Medicodio app repos show a fast, effective "Devin finds → human fixes in under an hour" loop without any written record; the Global Codio repo shows the opposite — extensive written records and a growing pile (~42) of unanswered findings. The two "Needs Support" Medicodio scores reflect control gaps (self-merge without review; approvals with open findings), not low output — sumedh's and Murali's delivery scores are mid-range. Because Devin session data is missing, members who used Devin without leaving GitHub traces (possible for saijyoti, afifa, vishnu, all NR) may be under-represented.

**Recommendation.** Read the cards with the activity report's Repeat Patterns: the same three team-level controls — an approval template that names open findings, a draft-PR-within-24-hours norm, and a pre-merge Devin QA gate for > 800-line PRs — would move the largest number of scores. Treat today's two positives (Nandan's `#438` dispositions; vineeth's `#1333` loop) as the reference examples in tomorrow's stand-ups. Do not rank on Overall alone when confidence is Low or Medium; Shashvi1's 7.5 rests on one PR.
