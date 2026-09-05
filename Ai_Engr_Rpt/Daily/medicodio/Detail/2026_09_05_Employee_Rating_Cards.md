# Employee Rating Cards — 2026-09-05

**Review window:** 2026-09-04 03:00 UTC → 2026-09-05 03:00 UTC. Companion to `2026_09_05_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **Devin session telemetry was unavailable** (`devin_session_search` → HTTP 403, `org.sessions.view` not granted). "Observable Devin Leverage" is scored **only** from GitHub artefacts: Devin Review findings and their resolution, Devin-authored PRs/commits, and commit messages that cite Devin findings. A member who used Devin sessions without leaving such artefacts will be under-scored; the dimension is marked NR when no artefact exists.
- Jira was not queryable; Sentry has no token. Delivery is judged from PR/commit outcomes only.
- **Volume is not productivity.** Commit, PR and finding counts are used as context and evidence of behaviour, never as the score.
- Scores reflect one 24-hour window plus historical consistency; a quiet day yields NR, not a low score.
- A dimension with no in-window evidence is **NR** and excluded from the weighted average. Fewer than three rated dimensions → **overall NR**.
- Confidence: **High** (multiple artefact types, history ≥ 2 weeks), **Medium** (single artefact type or short history), **Low** (one or two artefacts).

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Work stalled, closed unmerged without reason, or abandoned |
| Engineering Rigor | 25 | Tests + RCA + clear PR body + findings addressed | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed | Template body, no tests, findings ignored |
| Code Review Contribution | 15 | Substantive, specific review comments that change outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals, esp. on prod promotions |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; findings closed with tests/explanation | Findings closed with linked commits | Findings partially addressed | Findings ignored; Devin used where manual is faster |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ragha82 | Global Codio | **7.2** | Solid | 7.0 | 7.5 | NR | 8.0 | 7.0 | 6.0 | High |
| ashwinsk-medicodio | Medicodio | **6.7** | Mixed | 7.5 | 6.0 | NR | 6.5 | NR | 6.5 | Medium |
| amit-pandey-medicodio | Medicodio | **6.5** | Mixed | 8.0 | 6.5 | 3.5 | 8.0 | 6.0 | 6.0 | High |
| svh-medicodio | Global Codio | **6.6** | Mixed | 6.5 | 7.5 | NR | 6.0 | 5.5 | 6.5 | High |
| sameer-s-mansur | Medicodio | **6.3** | Mixed | 7.5 | 6.0 | NR | 4.5 | NR | 6.5 | Medium |
| SaijyotiMeti | Global Codio | **6.2** | Mixed | 5.5 | 6.5 | NR | NR | NR | 7.0 | Low |
| vishnu-saikarthik | Medicodio | **5.8** | Mixed | 6.5 | 6.0 | NR | 4.5 | NR | NR | Low |
| Medicodio-Amit | Medicodio | **5.8** | Mixed | 5.5 | 6.5 | NR | 5.0 | NR | 6.0 | Medium |
| jatinkushwaha-medicodio | Medicodio | **5.5** | Mixed | 6.0 | 5.0 | 3.5 | 6.5 | 6.5 | 5.5 | High |
| avinash-codio | Medicodio | **4.8** | Needs Support | 5.0 | 4.5 | NR | NR | NR | 5.0 | Low |
| nandanchouhan-medicodio | Medicodio | **3.2** | Needs Support | NR | NR | 3.0 | 3.0 | NR | 4.0 | Medium |
| afifashaikh007 | Medicodio | NR | — | 6.0 | 6.0 | NR | NR | NR | NR | Low |
| Pj-Vineeth | Global Codio | NR | — | 5.0 | NR | NR | NR | 4.0 | NR | Low |
| Karthik Khatavkar | Medicodio | NR | — | 5.5 | 5.5 | NR | NR | NR | NR | Low |
| sumedh-medicodio | Medicodio | NR | — | NR | NR | 3.0 | NR | NR | 4.0 | Low |
| Saahil Vishwakarma, anirudh-sachin, akanksh-p, Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — |
| hitesh-medicodio, shaheen-medicodio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions), rounded to one decimal.

## Cards

### ragha82 — Global Codio — 7.2 Solid (High confidence)
- **Delivery 7.0** — Observed Fact: 19 commits advancing #1314 (80 files); PR still open, 0 human reviews. Inference: substantial progress without closure.
- **Rigor 7.5** — Observed Fact: 2 test commits, PII-in-logs fix, size guard, remediation ledger documenting each finding→fix.
- **Review NR** — no reviews given.
- **Devin 8.0** — Observed Fact: 6 of 8 Devin Review findings resolved with linked commits — the most systematic response in the org today.
- **Automation 7.0** — Observed Fact: mailbox-flow e2e specs added to the QA automation suite.
- **Consistency 6.0** — 09-03 regressed (large PR, 0 tests), today improved; week stable.
- Recommendation: ask Devin to generate regression tests for the 6 resolved findings; request a human reviewer now.

### amit-pandey-medicodio — Medicodio — 6.5 Mixed (High confidence)
- **Delivery 8.0** — Observed Fact: ASC Payment Indicator shipped backend (#612) + frontend (#542) and promoted through UAT to prod in the same day; concurrency fix #616 merged.
- **Rigor 6.5** — Observed Fact: detailed bodies on #612/#616; no tests; prod promotions #608/#536 approved with empty reviews; #610 (UAT token→secrets) closed unmerged without explanation.
- **Review 3.5** — Observed Fact: 5 approvals, all 0 characters, two of them on 182- and 330-file prod promotions.
- **Devin 8.0** — Observed Fact: three fix commits cite the exact Devin finding and rationale (97ba735, e042080, f725bcc). Inference: highest-quality finding response in Medicodio to date.
- **Automation 6.0** — Observed Fact: moved toward secrets-based UAT token (#610) but closed unmerged; promotions still manual.
- **Consistency 6.0** — Improving on Devin leverage across the month; review depth unchanged (Repeat).
- Recommendation: delegate ASC PI regression tests to Devin; add a UAT-verification line to promotion approvals.

### ashwinsk-medicodio — Medicodio — 6.7 Mixed (Medium confidence)
- **Delivery 7.5** — Observed Fact: #428 (7th-character fix, configurable) merged; prod promotion #429 opened.
- **Rigor 6.0** — Observed Fact: 567-char explanatory body on #428; no tests; #429 has template body.
- **Review NR**.
- **Devin 6.5** — Observed Fact: 1 of 6 findings resolved via commit; 4 open on #429.
- **Automation NR**.
- **Consistency 6.5** — Stable across week/month; #429 not merged same-minute is a positive deviation.
- Recommendation: answer the 4 findings on #429 before merging.

### svh-medicodio — Global Codio — 6.6 Mixed (High confidence)
- **Delivery 6.5** — Observed Fact: #1316 opened (58 files); #1284 and #1295 still open — three concurrent large PRs, none reviewed.
- **Rigor 7.5** — Observed Fact: 13+3 bugs RCA'd in a doc, 18k-char body, additive migration, explicit scope notes; 0 test commits.
- **Review NR**.
- **Devin 6.0** — Observed Fact: 9 findings, 1 resolved on day of opening.
- **Automation 5.5** — Gemini auto-classify removes a manual picker (product automation); the bug-finding itself was manual demo-case building.
- **Consistency 6.5** — Stable strong documentation; PR-size pattern unchanged (Repeat).
- Recommendation: land #1284 before opening another; one regression test per RCA entry (Devin).

### sameer-s-mansur — Medicodio — 6.3 Mixed (Medium confidence)
- **Delivery 7.5** — Observed Fact: production parsing fault fixed and promoted same day (#285→#286).
- **Rigor 6.0** — Observed Fact: 2.3k RCA body naming two charts; test file included; 5 findings unanswered, self-merged 5 min after an empty approval.
- **Review NR**.
- **Devin 4.5** — Observed Fact: 10 findings across #285/#286, 0 addressed.
- **Automation NR**.
- **Consistency 6.5** — Consistent; same-day prod pattern repeats (08-27, 09-01).
- Recommendation: write a disposition for the 5 findings on #286.

### SaijyotiMeti — Global Codio — 6.2 Mixed (Low confidence)
- **Delivery 5.5** — Observed Fact: 7 commits on a follow-on branch; #1305 (109 files) idle, no review requested.
- **Rigor 6.5** — Inference from 09-03 ledger and today's scoped commits; no tests today.
- **Review / Devin / Automation NR**.
- **Consistency 7.0** — Active every day this week.
- Recommendation: get #1305 reviewed before stacking.

### vishnu-saikarthik — Medicodio — 5.8 Mixed (Low confidence)
- **Delivery 6.5** — #430 opened; a 93-file inpatient commit on the same branch.
- **Rigor 6.0** — "add tests" in commit; template body; findings unanswered.
- **Devin 4.5** — 6 findings, 0 answered.
- **Others NR**.
- Recommendation: split the inpatient commit out; fill the PR body.

### Medicodio-Amit — Medicodio — 5.8 Mixed (Medium confidence)
- **Delivery 5.5** — 1 commit on #425; #393 idle since 08-28.
- **Rigor 6.5** — substantive bodies; no tests today.
- **Devin 5.0** — 4 new findings unanswered (3 answered yesterday).
- **Consistency 6.0** — Stable.
- Recommendation: golden-file tests via Devin for Stage-0 routing.

### jatinkushwaha-medicodio — Medicodio — 5.5 Mixed (High confidence)
- **Delivery 6.0** — #544 merged; 5 no-op/CI-probe PRs (2 closed unmerged, 1 open).
- **Rigor 5.0** — CI probed via throwaway PRs; no tests on #544.
- **Review 3.5** — 8 approvals, all "lgtm"/empty, incl. prod #286 with 5 open findings.
- **Devin 6.5** — fixed 1 finding with an explanatory commit (e9c2524).
- **Automation 6.5** — Inference: building a CI change-impact stage (probe PRs suggest it).
- **Consistency 5.5** — Stable; review-depth Repeat.
- Recommendation: `workflow_dispatch` instead of probe PRs; one line of evidence per approval.

### avinash-codio — Medicodio — 4.8 Needs Support (Low confidence)
- **Delivery 5.0** — one 11-file commit; #415 idle since 09-02.
- **Rigor 4.5** — no body/tests context available.
- **Consistency 5.0** — low but steady cadence.
- **Others NR**. Low-confidence score; a single day of thin evidence.
- Recommendation: move #415 to review.

### nandanchouhan-medicodio — Medicodio — 3.2 Needs Support (Medium confidence)
- **Review 3.0** — "okay" approval on #428, merged one minute later with 6 open findings.
- **Devin 3.0** — merged with findings unaddressed.
- **Consistency 4.0** — one-word approvals on 08-29, 09-02, today (Repeat).
- **Others NR** (reviewer-only day).
- Recommendation: state what was checked; block merge on unanswered findings.

### afifashaikh007 — Medicodio — NR (Low confidence)
- Delivery 6.0, Rigor 6.0 (ARCHITECTURE.md + Phase 2 scaffolding, no PR). Two rated dimensions → overall NR. First observed day.
- Recommendation: open a draft PR so Devin Review can run.

### Pj-Vineeth — Global Codio — NR
- Delivery 5.0 (one branch-sync merge), Automation 4.0 (manual sync). Two rated dimensions → NR.

### Karthik Khatavkar — Medicodio — NR
- Delivery 5.5, Rigor 5.5 (merges and a fix on `hitesh` branch, no PR). Two rated dimensions → NR.

### sumedh-medicodio — Medicodio — NR
- Review 3.0 (empty approval on #285), Consistency 4.0 (Repeat). Two rated dimensions → NR.

### No observed activity — NR
Saahil Vishwakarma, anirudh-sachin, akanksh-p, Amrutha-Beedikar (Global Codio); hitesh-medicodio, shaheen-medicodio (Medicodio). No score is implied by a single quiet day.

## How to read the spread

- **Observed Fact:** the spread runs 3.2 → 7.2. Only one member is Solid; nobody is Strong. The two lowest scores are reviewer-only days scored almost entirely on review quality, which is the org's weakest, most-repeated pattern (17/17 human review events ≤ 4 characters). Global Codio had 0 human reviews, so no Global Codio member has a Review score.
- **Inference:** the ceiling is set by two structural habits, not by individual capability — empty approvals (Medicodio) and large unreviewed PRs (Global Codio). Devin leverage is bimodal: members who close findings with linked commits (ragha82, amit-pandey) score 8; members whose PRs carry 5–10 unanswered findings score ≤ 5. Because session telemetry is missing, Devin scores may under-count members who use Devin sessions without leaving review artefacts.
- **Recommendation:** treat the Review column as a team fix (one sentence of evidence per approval; finding disposition before prod) rather than individual feedback. Re-rate after `org.sessions.view` is granted; until then, do not use these scores for personnel decisions in isolation.
