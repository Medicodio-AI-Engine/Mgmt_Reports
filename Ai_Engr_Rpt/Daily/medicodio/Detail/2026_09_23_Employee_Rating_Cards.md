# Employee Rating Cards — 2026-09-23

**Review window:** Tuesday 2026-09-22 03:00 UTC → Wednesday 2026-09-23 03:00 UTC. Comparison windows: previous working day 09-21, week 09-15→09-22, month 08-23→09-22.
**Companion report:** `2026_09_23_Mgmt_Activity_Report.md` (same directory) holds the evidence detail; this file only scores it.

## Scoring limitations (read before the numbers)

- **Devin session telemetry is unavailable (21st consecutive run).** `devin_session_search` returns HTTP 403 (`org.sessions.view`). Nobody's prompts, session count, ACU effort, tests-requested or correction cycles were observed. **Observable Devin Leverage** is scored only on GitHub-visible behaviour: how a member responded to Devin Review findings, Devin QA gate verdicts and Devin-authored PRs. A member who used Devin sessions heavily but left no GitHub trace will be under-scored; a member who ignored visible findings is scored on that.
- **Jira is not connected**; Sentry has no token. Coordination, support and incident work are invisible and therefore **NR**, not zero.
- **Volume is not scored.** Today's 227 commits (2.7× yesterday) appear only as evidence of *what* happened; scores follow closure, rigor, independence of review and follow-through. 70 of those commits were written by reviewers on branches they then approved.
- **Attribution is imperfect:** `Claude`/`Devin AI` tool identities appear as commit authors; four `Claude` commits were attributed to SaijyotiMeti by branch ownership and timing. Multiple identities per person were merged manually.
- **Branch-protection and Actions-variable settings could not be read** (403); statements about them are inferred from observed self-merges and unaddressed failures.
- **Rules:** a dimension with no in-window evidence is **NR** and excluded from the weighted average; a member with fewer than three rated dimensions gets **NR** overall. Bands: Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5. Confidence reflects evidence breadth, not performance.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; carried items closed | Work merged or materially advanced; minor loose ends | Progress without closure; carried items untouched | Stalled, abandoned without record, or merged without follow-through |
| Engineering Rigor | 25 | Tests + accurate PR body + findings addressed before merge; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge into prod paths |
| Code Review Contribution | 15 | Substantive, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings or >100 files |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reason/test | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin PRs closed without note |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Amrutha-Beedikar | Global Codio | **7.0** | Solid | 7 | 8 | 4 | 9 | 6 | 7 | Medium |
| Medicodio-Amit | Medicodio | **7.1** | Solid | 7 | 7 | NR | 8 | 5 | 8 | Medium |
| jatinkushwaha-medicodio | Medicodio | **7.0** | Solid | 8 | 8 | 3 | 8 | 6 | 8 | Medium |
| Pj-Vineeth-Kumar | Global Codio | **6.4** | Mixed | 8 | 6 | NR | 5 | 5 | 7 | Medium |
| svh-medicodio | Global Codio | **5.9** | Mixed | 7 | 5 | NR | 5 | 6 | 7 | Medium |
| afifashaikh007 | Medicodio | **6.0** | Mixed | 6 | 6 | NR | NR | 5 | 7 | Medium-Low |
| akanksh-rv | Global Codio | **5.9** | Mixed | 6 | 6 | NR | NR | 5 | 6 | Medium-Low |
| SaijyotiMeti | Global Codio | **5.7** | Mixed | 7 | 7 | 4 | 4 | 4 | 6 | Medium |
| amit-pandey-medicodio | Medicodio | **5.7** | Mixed | 6 | 6 | 3 | 6 | 7 | 6 | Medium |
| anirudh-medicodio | Global Codio | **5.3** | Mixed | 7 | 6 | 3 | 4 | 5 | 5 | Medium |
| ragha82 | Global Codio | **5.0** | Mixed | 5 | 6 | 3 | 5 | 5 | 6 | Medium |
| sameer-s-mansur | Medicodio | **4.8** | Needs Support | 7 | 4 | NR | 3 | 3 | 6 | Medium |
| avinash-codio | Medicodio | **4.2** | Needs Support | 5 | 4 | NR | 3 | 4 | 5 | Medium |
| sumedh-codio (Sumedh Kaulgud) | Medicodio | **3.7** | Needs Support | 6 | 2 | 2 | NR | NR | 5 | Medium |
| NandanDate-Medicodio | Medicodio | **2.9** | Needs Support | NR | 3 | 2 | 3 | NR | 4 | Medium-Low |
| SaahilVishwakarma | Global Codio | **NR** | — | 3 | NR | NR | 3 | NR | NR | Low (2 rated dims; `#1391` verdicts unacknowledged day 5) |
| Vishnu Sai Karthik, ashwinsk-medicodio, Hitesh Shanthakumar, karthikmed, Murali-Shetty19, shaheen-khan11, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; Murali `#435` day 15 no reviewer) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | 17 PRs reviewed; QA gates `#1405` 56 / `#1403` 48 with fix PRs `#1411`/`#1413` inside 90 min; `#1362` diagnosis still unactioned |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions).

## Cards

### Amrutha-Beedikar — Global Codio — 7.0 Solid (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1406` (party-portal checklist authoring gate, 6 files) opened with 5.3k body and regression spec; 2 fix commits on Devin's `#1402`. Open, no reviewer yet. |
| Engineering Rigor | 8 | **Observed Fact:** spec "targets the rule, not the leaf props"; scoped diff; accurate body. |
| Code Review Contribution | 4 | **Observed Fact:** approved `#1409` uat→main (1,709 files / 416 commits, blank template body) with `approved` and merged to production. |
| Observable Devin Leverage | 9 | **Observed Fact:** answered the Devin finding on `#1406` with a 1.1k reasoning comment and a test — the best consumption instance today. |
| Automation of Repetitive Work | 6 | **Inference:** the rule-level spec is reusable across party-portal gates; no automation of the promotion she approved. |
| Consistency Across Windows | 7 | Day Improved; week Stable; month Consistent (small, well-described PRs). |

**Recommendation:** apply the `#1406` standard to promotions — ask the opener for the filled template and QA verdicts before approving.

### Medicodio-Amit — Medicodio — 7.1 Solid (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#470` chart-flagging agent (20 files, +4,166) opened to `uat`; left open for review rather than fast-merged. |
| Engineering Rigor | 7 | **Observed Fact:** 2.6k body with clear boundaries; `address review findings` commit before review requested. Deduction: 19 findings still open. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 8 | **Observed Fact:** 10/29 Devin findings marked resolved via a linked commit, pre-merge. |
| Automation of Repetitive Work | 5 | No repetitive work addressed or introduced. |
| Consistency Across Windows | 8 | Day Improved (vs `#466` 25 s promotion); week/month Improving. |

**Recommendation:** disposition the remaining 19 findings in the PR body before asking for approval.

### jatinkushwaha-medicodio — Medicodio — 7.0 Solid (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#660` cache invalidation and `#661` payer insurance-category resolution merged; `classify-changes.sh` monorepo support merged (`#12`). |
| Engineering Rigor | 8 | **Observed Fact:** `pg-notify` finding resolved with `a1d183b` before merge; 2.2k body on `#661`. Deduction: `#10`→`#11`→`#12` re-opened twice without explanation. |
| Code Review Contribution | 3 | **Observed Fact:** merged `#9` (14 files) 41 s after opening and `#662` with 0-char approvals. |
| Observable Devin Leverage | 8 | **Observed Fact:** 18/19 findings on own PRs closed pre-merge over three days; one `#661` finding open. |
| Automation of Repetitive Work | 6 | **Observed Fact:** `classify-changes.sh` monorepo support is CI tooling; sync PRs still manual. |
| Consistency Across Windows | 8 | Day Stable; week/month Improving. |

**Recommendation:** check Devin's open findings on peers' PRs before approving them.

### Pj-Vineeth-Kumar — Global Codio — 6.4 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#1405` (165 files, 67 commits) opened and merged; carried branch-without-PR resolved; new template PRD branch started. |
| Engineering Rigor | 6 | **Observed Fact:** 19k body, incident log, 409 concurrency verified by QA gate. Deductions: 12/14 findings unresolved at merge; QA NOT READY 56 (F3 HIGH) reached production. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 5 | **Observed Fact:** 2 findings resolved, 12 open; Devin fix PR `#1411` unreviewed at window end. |
| Automation of Repetitive Work | 5 | Manual incident write-ups repeat; nothing automated. |
| Consistency Across Windows | 7 | Day Improved; week Improving; month Consistent. |

**Recommendation:** review and merge `#1411` today; F3 is live.

### svh-medicodio — Global Codio — 5.9 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1403` service-provider module (332 files) opened and merged same day; carried branch-without-PR resolved. |
| Engineering Rigor | 5 | **Observed Fact:** 11k body with CLEANUP entries and controller spec; **but** the reviewer found six exploitable cross-tenant blockers and wrote 40 remediation commits; QA gate NOT READY 48 (PF-1 500 + PII leak). |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5 | **Observed Fact:** 0/8 findings dispositioned on the PR; Devin fix PR `#1413` opened, unreviewed. |
| Automation of Repetitive Work | 6 | **Observed Fact:** migration consolidation; 5 typecheck/lint repair commits suggest pre-push gates not run. |
| Consistency Across Windows | 7 | Day/week Improving; month Insufficient Data. |

**Recommendation:** run `/review-security` before opening the next module PR; merge `#1413`.

### afifashaikh007 — Medicodio — 6.0 Mixed (Confidence: Medium-Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** 4 POA fixes + QA tracker on `feat/inpatient-engine`; no PR — 14th report. |
| Engineering Rigor | 6 | **Observed Fact:** each fix names its clinical case; POA wording moved to config. No CI/review possible without a PR. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | Devin Review cannot run on a branch without a PR. |
| Automation of Repetitive Work | 5 | Hand-maintained tracker sheets. |
| Consistency Across Windows | 7 | Day Stable; week/month Improving. |

**Recommendation:** open the draft PR.

### akanksh-rv — Global Codio — 5.9 Mixed (Confidence: Medium-Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1414` opened (267 files, 298 commits, 160 from `main`); carried `#1373` decision items still unfiled (day 9). |
| Engineering Rigor | 6 | **Observed Fact:** security/PII fixes with tests; 4 ADRs; honest body about stale gates. Deductions: PR not rebased; gate matrix not re-run. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | PR opened 00:46; no Devin interaction yet in window. |
| Automation of Repetitive Work | 5 | "close the N gate failures" pairs recur; nothing automated. |
| Consistency Across Windows | 6 | Day Improved; week Stable; month Consistent — same mega-PR shape as `#1373`. |

**Recommendation:** split `#1414` into sync + feature.

### SaijyotiMeti — Global Codio — 5.7 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** six cross-tenant blockers on `#1403` fixed and merged; `feat/step-visibility` started. |
| Engineering Rigor | 7 | **Observed Fact:** exploit-verified fixes at one seam each, atlas regenerated. Deductions: generic commit message; 4 `Claude` commits without human trailer; 5 review-log commits. |
| Code Review Contribution | 4 | **Observed Fact:** 9.1k "REQUEST CHANGES — 8 items need a human decision, one takes production down" then `approved` + merge 25 min later with no decisions recorded; approver = remediator (40 commits). Substantive text, non-independent outcome. |
| Observable Devin Leverage | 4 | **Observed Fact:** cites Devin's 8 findings in prose; none resolved on the PR; QA gate PF-1 found post-merge. |
| Automation of Repetitive Work | 4 | Reviewer-remediation ritual repeated (`#1391` 09-18 → `#1403`). |
| Consistency Across Windows | 6 | Day Improved (0 → 45); week Stable; month Consistent. |

**Recommendation:** record the 8 decisions on `#1403` before the next promotion.

### amit-pandey-medicodio — Medicodio — 5.7 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#662` merged, `#663` open; `#9` sync merged. Deduction: `Dev_1.0` deploy trigger failed 3/3 with no follow-up. |
| Engineering Rigor | 6 | **Observed Fact:** Devin finding resolved in 9 min with named commit; `#9` empty body. |
| Code Review Contribution | 3 | **Observed Fact:** 4 0-char approvals incl. `#315` to `release/prod_1.0` in 5 min with an open finding. |
| Observable Devin Leverage | 6 | Own findings closed; peers' ignored. |
| Automation of Repetitive Work | 7 | **Observed Fact:** Crucible plan-mode guard; generated repo-structure refresh. Deduction: 7th manual sync PR. |
| Consistency Across Windows | 6 | Day Stable; week Improving; month Consistent. |

**Recommendation:** diagnose the three failed deploy triggers.

### anirudh-medicodio — Global Codio — 5.3 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1404` env-manifest (83 files) opened with PRD + migration checklist; `#1405` landed and promoted to production. Deduction: `#1402` closed silently; `#1404` findings unanswered. |
| Engineering Rigor | 6 | **Observed Fact:** test-backed fixes on `#1405`; `#1408`/`#1409` bodies are the unfilled template; promotion before QA verdict. |
| Code Review Contribution | 3 | **Observed Fact:** 30 commits on `#1405` then own 0-char approve/merge; 0-char approve of `#1407` (1,571 files) in 116 s. |
| Observable Devin Leverage | 4 | **Observed Fact:** 2/14 findings consumed on `#1405`; QA gate rendered irrelevant by promotion timing; Devin PR closed without note (3rd day). |
| Automation of Repetitive Work | 5 | Review-log commits and template promotions recur. |
| Consistency Across Windows | 5 | Day Stable; week Needs Attention; month Consistent. |

**Recommendation:** gate `uat→main` on the QA verdict.

### ragha82 — Global Codio — 5.0 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** 15 e2e/QA commits and 11 observability commits; `#1394` day 6 no reviewer; `#1362` `ACR_NAME` unfixed day 2. |
| Engineering Rigor | 6 | **Observed Fact:** runnable repro scripts; self-corrections. `#1407` blank body. |
| Code Review Contribution | 3 | **Observed Fact:** approved `#1408` in 64 s, 0 chars. |
| Observable Devin Leverage | 5 | **Observed Fact:** 5/33 findings on `#1394` resolved across 6 re-reviews. |
| Automation of Repetitive Work | 5 | 5-document QA set per PR repeated for 3 PRs. |
| Consistency Across Windows | 6 | Day Stable; week Stable; month Consistent. |

**Recommendation:** fix `#1362` and request a `#1394` reviewer today.

### sameer-s-mansur — Medicodio — 4.8 Needs Support (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** zero-pad fix landed on prod, uat and dev. |
| Engineering Rigor | 4 | **Observed Fact:** prod merged first (5 min) with an open finding; 3 hand-copied PRs; `fix/teams-card-payer-name-limit` 6 commits without PR. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3 | 4 findings across 3 PRs, none answered. |
| Automation of Repetitive Work | 3 | Repeat of `#308/#310/#314` ladder copying. |
| Consistency Across Windows | 6 | Day Improved; week Stable; month Consistent. |

**Recommendation:** one source PR, Devin opens the ladder.

### avinash-codio — Medicodio — 4.2 Needs Support (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#469` README merged. |
| Engineering Rigor | 4 | **Observed Fact:** title "read me file updated" for +405/−342; 422-char body. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3 | 3 findings unanswered — third PR in two days. |
| Automation of Repetitive Work | 4 | Hand-rewritten README. |
| Consistency Across Windows | 5 | Day Regressed; week Stable; month Needs Improvement. |

**Recommendation:** answer findings before merge.

### sumedh-codio (Sumedh Kaulgud) — Medicodio — 3.7 Needs Support (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#25` retry-own-batch-run shipped. |
| Engineering Rigor | 2 | **Observed Fact:** empty body, no reviewer, self-merged 24 s after opening onto `main`; 5th such PR. |
| Code Review Contribution | 2 | **Observed Fact:** approved/merged `#316`/`#317` within 60–90 s, 0 chars. |
| Observable Devin Leverage | NR | Repo has no Devin Review. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | Day Regressed; week Stable; month Consistent. |

**Recommendation:** enable Devin Review + 1 approval on `rf-rpa-automation`.

### NandanDate-Medicodio — Medicodio — 2.9 Needs Support (Confidence: Medium-Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No authored work in window. |
| Engineering Rigor | 3 | **Observed Fact:** as `uat` gatekeeper, merged `#469` with 3 open findings. |
| Code Review Contribution | 2 | **Observed Fact:** `ok` (2 chars); 7th ≤5-char approval in 8 days. |
| Observable Devin Leverage | 3 | Findings on merged PRs unconsumed. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | Week Needs Attention; month Needs Improvement. |

**Recommendation:** three-line approval template.

### SaahilVishwakarma — Global Codio — NR (Confidence: Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 3 | **Observed Fact:** no events; `#1391` post-merge NOT READY 52 / `#1398` BLOCK RELEASE F-1 unacknowledged day 5. |
| Observable Devin Leverage | 3 | Verdicts unanswered. |
| Others | NR | — |

**Recommendation:** post a disposition on `#1391`; delegate F-1 to Devin.

### Members with no events — NR

Vishnu Sai Karthik, ashwinsk-medicodio, Hitesh Shanthakumar, karthikmed, Murali-Shetty19, shaheen-khan11, Shashvi1 (Medicodio): no commits, PRs, reviews or comments in the window. Not scored. Murali `#435` remains without a reviewer (day 15); Hitesh/Vishnu share `feat/inpatient-engine` (no PR).

## How to read the spread

- **Observed Fact:** the three Solid scores (Amrutha, Medicodio-Amit, Jatin) are the three people who answered Devin findings with commits or tests *before* asking for merge. The four Needs Support scores share one trait: findings ignored at merge and approvals of ≤2 characters or none. Nobody scored ≥8 overall; the top of the team is capped by the Code Review dimension, where 13 of 14 approvals today carried ≤10 characters.
- **Observed Fact:** the two highest-volume contributors (SaijyotiMeti 45, anirudh 34 commits) score Mixed, not because of volume but because both wrote the remediation and then approved it — 70 commits by reviewers on branches they merged. Volume moved the Delivery score, not the Review or Rigor scores.
- **Inference:** Global Codio's production risk today is a process artefact, not a skills gap: the QA gate, fix PRs and security remediation all happened — in the wrong order relative to the `uat→main` merge. One rule (QA verdict before promotion) would have moved anirudh, Vineeth and Amrutha up a band.
- **Inference:** Medicodio's spread is bimodal by habit, not by team: authors close findings, mergers don't look at them.
- **Recommendation:** management should act on the two structural items — branch protection that forbids approver = committer, and a QA-verdict prerequisite for production promotion — before any individual coaching; both would change 9 of 16 cards tomorrow.
- **Limitation:** with Devin session telemetry unavailable for 21 runs, the Devin column measures response to Devin, not use of Devin. Treat differences of ±1 as noise.
