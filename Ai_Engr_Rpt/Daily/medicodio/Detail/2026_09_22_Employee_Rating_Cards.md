# Employee Rating Cards — 2026-09-22

**Review window:** Monday 2026-09-21 03:00 UTC → Tuesday 2026-09-22 03:00 UTC. Comparison windows: previous working day 09-18, week 09-14→09-21, month 08-22→09-21.
**Companion report:** `2026_09_22_Mgmt_Activity_Report.md` (same directory) holds the evidence detail; this file only scores it.

## Scoring limitations (read before the numbers)

- **Devin session telemetry is unavailable (20th consecutive run).** `devin_session_search` returns HTTP 403 (`org.sessions.view`). Nobody's prompts, session count, ACU effort, tests-requested or correction cycles were observed. **Observable Devin Leverage** is scored only on GitHub-visible behaviour: how a member responded to Devin Review findings, Devin QA gate verdicts and Devin-authored PRs. A member who used Devin sessions heavily but left no GitHub trace will be under-scored; a member who ignored visible findings is scored on that.
- **Jira is not connected**; Sentry has no token. Coordination, support and incident work are invisible and therefore **NR**, not zero.
- **Volume is not scored.** Commit, PR, file and review counts appear only as evidence of *what* happened; scores follow closure, rigor, independence of review and follow-through.
- **Attribution is imperfect:** `Claude`/`Devin AI` tool identities appear as commit authors; three `Claude` commits were attributed to akanksh-rv by inference. Multiple identities per person were merged manually.
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
| jatinkushwaha-medicodio | Medicodio | **7.2** | Solid | 8 | 8 | 4 | 8 | 6 | 8 | Medium |
| Medicodio-Amit | Medicodio | **6.7** | Mixed | 8 | 6 | NR | 7 | 4 | 7 | Medium |
| afifashaikh007 | Medicodio | **6.4** | Mixed | 6 | 7 | NR | NR | 5 | 7 | Medium-Low |
| anirudh-medicodio | Global Codio | **6.4** | Mixed | 8 | 7 | 4 | 6 | 5 | 6 | Medium |
| akanksh-rv | Global Codio | **6.0** | Mixed | 5 | NR | 8 | 7 | 4 | 6 | Low |
| amit-pandey-medicodio | Medicodio | **5.7** | Mixed | 7 | 5 | 4 | 4 | 8 | 7 | Medium |
| ragha82 | Global Codio | **5.1** | Mixed | 5 | 6 | 3 | 5 | 5 | 6 | Medium |
| avinash-codio | Medicodio | **4.8** | Needs Support | 7 | 4 | NR | 3 | 4 | 5 | Medium |
| NandanDate-Medicodio | Medicodio | **3.8** | Needs Support | 6 | 3 | 2 | 3 | NR | 4 | Medium |
| Vishnu Sai Karthik | Medicodio | **NR** | — | 5 | 5 | NR | NR | NR | NR | Low (2 rated dims) |
| Pj-Vineeth-Kumar | Global Codio | **NR** | — | 5 | NR | NR | NR | NR | 6 | Low (2 rated dims) |
| svh-medicodio | Global Codio | **NR** | — | 5 | NR | 3 | NR | NR | NR | Low (2 rated dims) |
| sameer-s-mansur | Medicodio | **NR** | — | 5 | NR | NR | NR | NR | 6 | Low (2 rated dims) |
| ashwinsk-medicodio | Medicodio | **NR** | — | 4 | 4 | NR | NR | NR | NR | Low (2 rated dims) |
| Sumedh Kaulgud | Medicodio | **NR** | — | 5 | NR | NR | NR | NR | NR | Low (1 rated dim) |
| SaijyotiMeti, SaahilVishwakarma, Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; `#1391` verdicts unacknowledged day 4) |
| Hitesh Shanthakumar, karthikmed, Murali-Shetty19, shaheen-khan11, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; Murali `#435` day 14 no reviewer) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | 8 PRs reviewed; QA gate `#1400` 66/100 with evidence; correctly skipped docs-only `#1399` |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions).

## Cards

### jatinkushwaha-medicodio — Medicodio — 7.2 Solid (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#657` (RPA import trigger) and `#584` (cron parser) merged; `#660` opened with follow-up commit same day. Carried `#643`/`#644` work now in prod via `#659`. |
| Engineering Rigor | 8 | **Observed Fact:** 16 of 17 Devin Review findings on own PRs resolved before merge; PRs sized 10–12 files. Deduction: `#584` merged by author after peer approval. |
| Code Review Contribution | 4 | **Observed Fact:** five approvals, all 0 characters, including `#659`/`#585` prod promotions merged ≈3 min after opening with 9 open BUG findings. |
| Observable Devin Leverage | 8 | **Observed Fact:** best finding-closure rate on the team; **Inference:** Devin Review is being used as a pre-merge gate on his own work. Deduction for ignoring findings on promotions he merged. |
| Automation of Repetitive Work | 6 | **Observed Fact:** pg-notify cache invalidation removes manual cache resets (`#660`); no automation of the promotion ritual. |
| Consistency Across Windows | 8 | Week Improving (`#573`, `#643`, `#644`, `#657`, `#584`, `#660`); month Improving. |

**Recommendation:** apply the same finding-closure discipline to the promotions you merge for others.

### anirudh-medicodio — Global Codio — 6.4 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#1399` (governance overhaul, 644 files) and `#1400` (classification fix, 43 files) merged; both close carried items (review-rule drift; classification defects). Deduction: `#1401` DEV-FIX-LIST #9 not picked up; 6 Devin PRs closed without disposition. |
| Engineering Rigor | 7 | **Observed Fact:** specification-grade bodies, ADR + HLD, "close five real defects Devin found", four gate-suite root causes fixed before merge. Deduction: self-merge of `#1400` into `dev` after own review; `#1399` 644 files in one PR. |
| Code Review Contribution | 4 | **Observed Fact:** the day's only substantive review body (8,914 chars) is on his own PR; no review on any peer PR. |
| Observable Devin Leverage | 6 | **Observed Fact:** Devin findings on `#1400` dispositioned in a named commit (positive) vs `#1392`–`#1398` closed in 60 s without a note including a BLOCK RELEASE report (negative). |
| Automation of Repetitive Work | 5 | **Observed Fact:** `#1399` gates rule drift (positive); 3 hand-committed `docs(review)` logs duplicating Devin's PR output (negative). |
| Consistency Across Windows | 6 | Week Needs Attention (all merges via 0-char/self); month Consistent (largest GC contributor; same governance gap in 6 reports). |

**Recommendation:** enable branch protection on `dev` (no self-approval) — the single change that would lift Rigor and Review together.

### Medicodio-Amit — Medicodio — 6.7 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#462` (provider-documented E&M level, 28 files) merged to `uat` and promoted to prod via `#466` the same morning. |
| Engineering Rigor | 6 | **Observed Fact:** `#462` — PRD-quality body, 25 regression tests, all 6 findings dispositioned (carried from 09-17). `#466` — empty body, 19 commits, 2 BUG findings unanswered, merged 25 s after opening. Average of an excellent PR and a hollow one. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 7 | **Observed Fact:** `#462` disposition (fix with SHA / reasoned rejection) is the model; `#466` findings ignored. |
| Automation of Repetitive Work | 4 | **Observed Fact:** promotion body left empty for the second time (`#453`, `#466`); no tooling. |
| Consistency Across Windows | 7 | Week/month Improving on feature rigor; promotion habit unchanged. |

**Recommendation:** give promotion PRs a body and a findings checklist (Devin can draft it).

### amit-pandey-medicodio — Medicodio — 5.7 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#586` fix, `#7`/`#8` docs, deploy test→dev cutover merged; `#659`/`#585` promotions landed in prod. |
| Engineering Rigor | 5 | **Observed Fact:** promotions `#659` (6 BUG) / `#585` (3 BUG) opened with badge-only bodies and no finding response; `#7` body is accurate and explains the automation. |
| Code Review Contribution | 4 | **Observed Fact:** 0-char approvals on `#657`, `#584`. |
| Observable Devin Leverage | 4 | **Observed Fact:** 9 Devin findings on own promotions unanswered; automation investment is in Claude hooks, not Devin (not penalised in itself — scored on findings ignored). |
| Automation of Repetitive Work | 8 | **Observed Fact:** repo-structure regeneration now hook-driven end-to-end (`#7`); `crucible` pipeline added. Deduction: Dev_1.0 sync still manual (3 commits). |
| Consistency Across Windows | 7 | Week Improving (tooling), month Consistent; 0-char approvals persistent. |

**Recommendation:** extend the hook approach to the Dev_1.0 → application-2.0 sync and answer the 9 promotion findings.

### afifashaikh007 — Medicodio — 6.4 Mixed (Confidence: Medium-Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** 15 root-cause fixes on `feat/inpatient-engine`; nothing merged or in a PR (13th report of branch without PR). |
| Engineering Rigor | 7 | **Observed Fact:** stage-IO capture added, test programme tracked, own review error corrected in writing. Deduction: no CI/review on the branch. |
| Code Review Contribution | NR | None given. |
| Observable Devin Leverage | NR | No Devin artefacts possible without a PR. |
| Automation of Repetitive Work | 5 | **Observed Fact:** prompt-surface audit done by hand; capture tooling is a step toward a harness. |
| Consistency Across Windows | 7 | Week and month Improving (48 commits, all in last 10 days, quality rising). |

**Recommendation:** open a draft PR so Rigor and Devin dimensions can be earned.

### akanksh-rv — Global Codio — 6.0 Mixed (Confidence: Low)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** audit report delivered; `#1373` decision items still unfiled (day 8); no fix PR from `#1391` findings. |
| Engineering Rigor | NR | No product code in window (test commit is under `Claude` identity — attribution inferred, not scored). |
| Code Review Contribution | 8 | **Observed Fact:** 4,573-char evidence-first code audit on `#1391` with a stated verdict and relationship to the prior live gate. |
| Observable Devin Leverage | 7 | **Observed Fact:** built on Devin's `#1398` gate rather than duplicating it. |
| Automation of Repetitive Work | 4 | **Observed Fact:** 5th markdown audit report; none converted to specs. |
| Consistency Across Windows | 6 | Week Stable, month Consistent (substantive reviewer since 09-03). |

**Recommendation:** file `#1373`/`#1391` open items as issues; add a human Co-Authored-By to tool-identity commits.

### ragha82 — Global Codio — 5.1 Mixed (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#1316` QA rounds progressed (F-4/F-5/F-6 documented); `#1394` idle day 5; `#1362` failure untouched on first working day. |
| Engineering Rigor | 6 | **Observed Fact:** repro corrected when wrong; findings graded with severity. Deduction: 14 Devin findings on own `#1394` unanswered since 09-17. |
| Code Review Contribution | 3 | **Observed Fact:** 0-char approval + merge of 644-file `#1399`. |
| Observable Devin Leverage | 5 | **Observed Fact:** `#1362` Devin CI diagnosis not acted on; `#1394` findings ignored; F-6 finding parallels Devin's `#1398` but neither converted. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 7 markdown repro/report commits; no spec generated from them. |
| Consistency Across Windows | 6 | Week Stable, month Consistent. |

**Recommendation:** fix `#1362`'s prerequisite and hand F-6 to Devin as spec + fix.

### avinash-codio — Medicodio — 4.8 Needs Support (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** HCPCS module split (`#467`) merged to `uat` and promoted to prod (`#468`) same day; gynecology config `#465` merged. |
| Engineering Rigor | 4 | **Observed Fact:** `#467` body excellent; but 107 files in one PR, "some fixes and config chnages" commit, 8 Devin findings incl. 2 SEC unanswered, prod promotion 18 min after `uat`. |
| Code Review Contribution | NR | None given. |
| Observable Devin Leverage | 3 | **Observed Fact:** ~12 findings across 3 PRs, 0 dispositions, 3 SEC. |
| Automation of Repetitive Work | 4 | **Observed Fact:** manual same-day promotion for the 4th time this month. |
| Consistency Across Windows | 5 | Month Needs Attention (`#451`, `#458`, `#461`, `#468`). |

**Recommendation:** written disposition of the 2 SEC findings today; one-working-day UAT soak.

### NandanDate-Medicodio — Medicodio — 3.8 Needs Support (Confidence: Medium)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** all five engine PRs merged within minutes; Gastro Coding Atlas artifact source added. |
| Engineering Rigor | 3 | **Observed Fact:** merged two prod promotions (`#466` 25 s, `#468`) with unanswered BUG/SEC findings visible. |
| Code Review Contribution | 2 | **Observed Fact:** five approvals, all `okay`; 291 files, ~15 open findings. Repeat since `#449` (09-08). |
| Observable Devin Leverage | 3 | **Observed Fact:** Devin findings present on every PR merged; none referenced. |
| Automation of Repetitive Work | NR | No repetitive work of his own observed. |
| Consistency Across Windows | 4 | Week and month Needs Attention (5 reports with the same pattern). |

**Recommendation:** three-line approval template (findings / tests / rollback) before every merge.

### Two-dimension members (overall NR)

| Member | Rated | Evidence |
| --- | --- | --- |
| Vishnu Sai Karthik | Delivery 5, Rigor 5 | 30 rule fields + v6 prompt swap on the unreviewed inpatient branch; no output diff recorded; `#452` finding open since 09-15. |
| Pj-Vineeth-Kumar | Delivery 5, Consistency 6 | DOCX fidelity + focus-ring commits, no PR; prior branch-without-PR pattern resolved 09-16. |
| svh-medicodio | Delivery 5, Review 3 | 1 feature commit, no PR; 0-char approval on `#1400` that enabled a self-merge. |
| sameer-s-mansur | Delivery 5, Consistency 6 | 5 integration commits with explanatory messages, no PR. |
| ashwinsk-medicodio | Delivery 4, Rigor 4 | "imprving prompts" / "prompt improvemnt" — content unverifiable (Repeat: low-info messages). |
| Sumedh Kaulgud | Delivery 5 | 1 typed fix, no PR; repo has no Devin Review. |

### Members with no in-window events (overall NR)

SaijyotiMeti, SaahilVishwakarma, Amrutha-Beedikar (Global Codio); Hitesh Shanthakumar, karthikmed, Murali-Shetty19, shaheen-khan11, Shashvi1 (Medicodio). **Observed Fact:** no commits, PRs, reviews or comments. Carried, not scored: `#1391` verdicts (Saijyoti/Saahil) unacknowledged day 4; `#435` (Murali) unreviewed day 14. Saijyoti's latest rated card remains 09-19 (5.4 Mixed).

## How to read the spread

- **Observed Fact:** nine members earned a rated overall today (range 3.8–7.2), six had two or fewer rated dimensions, eight had no events. Of the 15 human review submissions, 14 were ≤10 characters — Code Review Contribution is the lowest-scoring dimension for every rated member except akanksh-rv.
- **Observed Fact:** the two highest scores (Jatin 7.2, Medicodio-Amit 6.7) and the two lowest (Nandan 3.8, avinash 4.8) are separated mainly by one behaviour: whether Devin Review findings were answered before merge. Volume did not drive the ranking — anirudh (18 commits, 6.4) and Nandan (6 commits, 5 merges, 3.8) differ for reasons unrelated to count.
- **Inference:** Medicodio's promotion ritual (open → `okay` → merge in seconds) is a shared habit that lowers three people's Rigor and Review scores at once; a template would raise all three without any change in how much they ship.
- **Inference:** Global Codio scores are held down by review independence (self-merge, 0-char approvals on 644/43-file PRs) rather than by code quality; the code-level evidence (`#1399`, `#1400` bodies, akanksh's audit) is strong.
- **Recommendation:** treat the gap between "Delivery" (mostly 5–8) and "Review" (mostly 2–4) as the team's single improvement lever; branch protection plus an approval template addresses it for both products.
- **Recommendation:** re-rate Vishnu, Vineeth, svh, sameer, ashwinsk and Sumedh once their branches become PRs — their NR is an evidence gap, not a judgement.
- **Limitation restated:** without Devin session telemetry, "Observable Devin Leverage" reflects only how visible Devin outputs were consumed. A member's actual Devin usage may be higher or lower than scored.

*MediCodio AI © 2026. All Rights Reserved · www.medicodio.ai*
