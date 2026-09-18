# Employee Rating Cards — 2026-09-18

**Review window:** 2026-09-17 03:00 → 2026-09-18 03:00 UTC. Comparison: previous working day 09-16, week 09-10 → 09-17, month 08-18 → 09-17. Companion to `2026_09_18_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

1. **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (missing `org.sessions.view`). *Observable Devin Leverage* is therefore scored only from GitHub artefacts: how Devin Review findings were dispositioned, Devin QA verdicts, `devin-ai-integration[bot]` PRs/commits, and `Co-Authored-By: Claude` trailers. Prompt quality, scoping, tests requested, correction effort and session outcomes are **not** observed and are not scored. Where a member has no Devin-Review-bearing PR in window, the dimension is NR.
2. **No Jira, no Sentry.** Ticket flow and production error data are absent; delivery is judged from PRs/commits/merges only.
3. **Volume is not productivity.** Commit, PR, file and finding counts appear as evidence of *shape* (e.g. PR size, review latency), never as a score input on their own. 160 commits today, 111 with Claude trailers — a large share of the code in Global Codio and the engine is machine-drafted, which further decouples volume from effort.
4. **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average. Fewer than three rated dimensions → overall NR.
5. **Single-day caution.** Scores describe this window; trend labels lean on the 57 prior reports. No conclusion below rests on one unusual day alone unless stated.
6. **Identity mapping** is by observed pairing of commit author names to GitHub logins; `Medicodio-Amit` and `amit-pandey-medicodio` are different people.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; carried items closed | Work merged or materially advanced; minor loose ends | Progress without closure; carried items untouched | Stalled, abandoned without record, or merged without follow-through |
| Engineering Rigor | 25 | Tests + accurate PR body + findings addressed before merge; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge into prod paths |
| Code Review Contribution | 15 | Substantive, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings or >100 files |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reason/test | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin PRs closed without note |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.** Overall = weighted mean over rated dimensions only.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Medicodio-Amit | Medicodio | **7.6** | Solid | 7 | 8 | NR | 9 | 6 | NR | Medium (GitHub only; 4 dims; first active week) |
| anirudh-medicodio | Global Codio | **6.6** | Mixed | 7 | 7 | 6 | 7 | 5 | 7 | Medium (GitHub only; 6 dims) |
| amit-pandey-medicodio | Medicodio | **6.5** | Mixed | 8 | 7 | 2 | 8 | 5 | 7 | Medium (GitHub only; 6 dims) |
| SaijyotiMeti | Global Codio | **6.4** | Mixed | 7 | 7 | 5 | 7 | 4 | 6 | Medium (GitHub only; 6 dims) |
| SaahilVishwakarma | Global Codio | **6.2** | Mixed | 6 | 6 | NR | 6 | 5 | 7 | Medium (5 dims; PR <12 h old) |
| ragha82 | Global Codio | **6.1** | Mixed | 6 | 7 | NR | 5 | 7 | 5 | Medium (5 dims) |
| jatinkushwaha-medicodio | Medicodio | **6.0** | Mixed | 7 | 6 | 2 | 7 | 5 | 7 | Medium (6 dims) |
| Pj-Vineeth-Kumar | Global Codio | **5.9** | Mixed | 6 | 6 | NR | 5 | 5 | 7 | Medium (5 dims) |
| Sumedh Kaulgud | Medicodio | **5.4** | Mixed | 7 | 4 | NR | NR | 5 | NR | Low (3 dims; no Devin Review in repo) |
| avinash-codio | Medicodio | **4.1** | Needs Support | 5 | 3 | 3 | 3 | 5 | 5 | Medium (6 dims) |
| vishnu-saikarthik | Medicodio | **3.9** | Needs Support | 4 | 3 | 3 | 4 | NR | 5 | Medium (5 dims) |
| Karthik Khatavkar (karthikmed) | Medicodio | **4.6** | Needs Support | 5 | 4 | NR | 4 | 5 | NR | Low (4 dims; attribution unclear) |
| svh-medicodio | Global Codio | **NR** | — | NR | NR | 2 | NR | NR | 4 | — (2 dims) |
| NandanDate-Medicodio | Medicodio | **NR** | — | NR | 3 | 3 | NR | NR | NR | — (2 dims; merger of record) |
| ashwinsk-medicodio | Medicodio | **NR** | — | 6 | 5 | NR | NR | NR | NR | — (2 dims; no PR) |
| Murali-Shetty19 | Medicodio | **NR** | — | 5 | 4 | NR | 3 | NR | NR | — (3 dims → 4.0, but see card: low confidence) |
| sameer-s-mansur, shaheen-khan11 | Medicodio | NR | — | 6 | NR | NR | NR | NR | NR | — (1 dim; no PR) |
| akanksh-rv, Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events in window) |
| Hitesh Shanthakumar, afifashaikh007, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events in window) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

*Murali-Shetty19 has exactly three rated dimensions (4.0, Needs Support band) — shown as NR in the grid by judgement call because the three data points are one closed PR and three doc commits; the card carries the number with its caveat.*

## Cards

### Medicodio-Amit — Medicodio · Overall 7.6 · Solid

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#462` (26 files, provider-documented E&M level) advanced through two review rounds; `#463` risk-flag fix; neither merged yet. **Inference:** material progress, no closure. |
| Engineering Rigor | 8 | **Observed Fact:** 5,478-char PR body; fix commits named per review round; three long comments stating which findings were fixed and which were verified unreachable and why. |
| Code Review Contribution | NR | No reviews on others' PRs. |
| Observable Devin Leverage | 9 | **Observed Fact:** 16 Devin findings; 6 resolved with commits, remainder answered in writing. Best disposition behaviour observed in Medicodio this month. |
| Automation of Repetitive Work | 6 | **Observed Fact:** per-client rule branches (DVG, McQueen) hand-written; no generated parity fixtures. |
| Consistency Across Windows | NR | First active window since late August. |

**Recommendation:** encode the "unreachable" arguments as tests before merge; insist on a named reviewer rather than a 0-minute merge.

### anirudh-medicodio — Global Codio · Overall 6.6 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1386` (250 files) merged after 12 test/mocks fix commits; `#1393` audit opened; `#1358`/`#1388` still closed without note. |
| Engineering Rigor | 7 | **Observed Fact:** ADR, lifecycle catalog, specs run under jsdom; but Devin QA NOT READY 55/100 arrived 13 h after merge; self-merge 7 s after an empty co-approval. |
| Code Review Contribution | 6 | **Observed Fact:** 12,963-char architect/EM review on `#1389` (substantive); then 12 own commits on that branch, empty approval, merge 12 s later. **Inference:** the review changed the code — but the approval was not independent. |
| Observable Devin Leverage | 7 | **Observed Fact:** all 15 findings on `#1386` closed by commit before merge; QA gate consumed after merge (3rd consecutive PR). |
| Automation of Repetitive Work | 5 | **Observed Fact:** 3 review-log/CLEANUP commits by hand; 12 mock-repair commits by hand. |
| Consistency Across Windows | 7 | **Observed Fact:** 09-17 card 6.5 → 6.6; same PR-size and merge-ordering shape since 08-30. |

**Recommendation:** enable approver-without-commits and pre-merge QA verdict before reviewing `#1391`.

### amit-pandey-medicodio — Medicodio · Overall 6.5 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#658` fix + tests merged in 30 min; prediction-trail fixes; `Dev_2.0` ports landed. `#651`/prod `23505` status still unconfirmed (carried 3 days). |
| Engineering Rigor | 7 | **Observed Fact:** `test: cover withCronLock lifecycle` shipped with the fix — first test file with a fix this week; `#6` 321-file sync merged in 45 s with a generated body only. |
| Code Review Contribution | 2 | **Observed Fact:** merged `#652` (163 files) and `#578` (150 files) on 0-char approvals with open findings; own approvals empty. |
| Observable Devin Leverage | 8 | **Observed Fact:** both `#658` findings resolved with a linked commit before merge; findings on PRs he merged for others untouched. |
| Automation of Repetitive Work | 5 | **Observed Fact:** `#5`/`#6` hand-made sync PRs, following `#1`–`#3` 09-16 and `dev → uat` PRs 09-11/12/17. |
| Consistency Across Windows | 7 | **Observed Fact:** 09-17 card 5.7 → 6.5 on the strength of `#658`; review score unchanged at 2 for the 7th report. |

**Recommendation:** apply the `#658` rule to merges of others' PRs: no merge while findings are open.

### SaijyotiMeti — Global Codio · Overall 6.4 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1389` merged after independent review; `#1390` merged; `#1396` opened. Devin QA on `#1389` NOT READY 64/100 post-merge; Devin fix `134a868` landed 3 h later. |
| Engineering Rigor | 7 | **Observed Fact:** test commits alongside fixes; review-log ledger; 25-file header backfill by hand for the 2nd day. |
| Code Review Contribution | 5 | **Observed Fact:** 7,776-char changes-requested on `#1390` (specific); then 20 own commits, approval, merge 20 s later — 6th reviewer-remediates-merges instance since 09-06. |
| Observable Devin Leverage | 7 | **Observed Fact:** 3 findings on `#1396` answered in 2 min with reasons; `fix(web/meetings): three corrections from Devin's review of my own changes`. QA verdict after merge on `#1389`. |
| Automation of Repetitive Work | 4 | **Observed Fact:** header backfill (25 files) and surface sweep done manually two days running; no lint rule proposed. |
| Consistency Across Windows | 6 | **Observed Fact:** 09-17 card 6.1 → 6.4; same merge pattern as `#1380`, smaller PR. |

**Recommendation:** paste the hosted QA verdict into `#1396` before merging; hand approval of anything you fixed to someone else.

### SaahilVishwakarma — Global Codio · Overall 6.2 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1391` (262 files, 16 commits) opened with audit doc; not merged; 8 findings open. |
| Engineering Rigor | 6 | **Observed Fact:** 9 suites repaired in-PR, standards audit written; 4 "repair what the gate surfaced" commits imply gate not run before push; 217-file initial commit. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 6 | **Observed Fact:** all commits Claude-trailed; 8 Devin findings undispositioned at window end (<12 h). |
| Automation of Repetitive Work | 5 | **Observed Fact:** gate-failure repair repeated 4×; no pre-push hook. |
| Consistency Across Windows | 7 | **Observed Fact:** same oversized-PR shape as `#1310` (09-09); steady month (102 commits). |

**Recommendation:** disposition the 8 findings and propose a per-runtime split before review.

### ragha82 — Global Codio · Overall 6.1 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1394` (75 files) opened with runbook; `#1382` red spec (09-15) and `#1384` findings still open. |
| Engineering Rigor | 7 | **Observed Fact:** shared metrics factory, health probes, retention policy, runbook in the same PR; 15 findings unanswered. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 5 | **Observed Fact:** 15 + carried findings, none dispositioned. |
| Automation of Repetitive Work | 7 | **Observed Fact:** `feat(utils): add shared Prometheus metrics primitives` + `build the metrics registry from the shared factory` — the one anti-repetition change landed today. |
| Consistency Across Windows | 5 | **Observed Fact:** two silent days then a 75-file PR; carried items aging. |

**Recommendation:** close `#1382` first, then triage `#1394`.

### jatinkushwaha-medicodio — Medicodio · Overall 6.0 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#657` (RPA trigger + cron lock) and `#584` (cron builder) opened and iterated; neither merged; 3 successive "improve error handling" refactors on one file. |
| Engineering Rigor | 6 | **Observed Fact:** bodies ~800 chars; no test files; 26 findings open incl. replica duplication and prod gating. |
| Code Review Contribution | 2 | **Observed Fact:** 4 empty approvals incl. `#6` (321 files) within the minute it opened. |
| Observable Devin Leverage | 7 | **Observed Fact:** 14 of 40 findings resolved within ~20 min; the open set contains the production-risk items. |
| Automation of Repetitive Work | 5 | **Observed Fact:** cron-expression edge cases fixed one by one as findings arrive; no test table. |
| Consistency Across Windows | 7 | **Observed Fact:** 09-17 card 6.3 → 6.0; steady delivery, review score 2–3 for 7 reports. |

**Recommendation:** answer the six prod-risk findings on `#657`; one sentence per approval.

### Pj-Vineeth-Kumar — Global Codio · Overall 5.9 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** timezone work merged (via `#1390`, after reviewer's 20 fixes); support-letter branch 11 commits, no PR. |
| Engineering Rigor | 6 | **Observed Fact:** PRD first; 84-file move + 10 feature commits unreviewed; phase ledger maintained. |
| Code Review Contribution | NR | No reviews. |
| Observable Devin Leverage | 5 | **Observed Fact:** no Devin Review on the branch (no PR); `#1390` QA READY WITH KNOWN RISKS 70/100 achieved by the reviewer's remediation. |
| Automation of Repetitive Work | 5 | **Observed Fact:** ledger commits by hand. |
| Consistency Across Windows | 7 | **Observed Fact:** 09-17 card 5.9 → 5.9; branch-without-PR resumed 2 days after its 09-15 resolution. |

**Recommendation:** open the draft PR today.

### Sumedh Kaulgud — Medicodio · Overall 5.4 · Mixed (low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** 12 commits; `#23`/`#24` merged; endoscopy split flow end-to-end. |
| Engineering Rigor | 4 | **Observed Fact:** self-merge to `main` 0 min after open, no review, no tests; docs commits capture portal behaviour (positive). |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | Repo has no Devin Review. |
| Automation of Repetitive Work | 5 | **Observed Fact:** three split branches as "one skeleton with per-branch steps" — partial table-driving. |
| Consistency Across Windows | NR | Repo visible since 09-16. |

**Recommendation:** enable Devin Review and a second approver on the RPA repo.

### avinash-codio — Medicodio · Overall 4.1 · Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#459` prod promotion, `#464` config sync merged, `#465` open; `#458` ×4 findings from 09-16 still unanswered. |
| Engineering Rigor | 3 | **Observed Fact:** `#464` merged 1 min before 6 findings incl. "Named parity guard checks nothing"; `#459` self-merged 1 min after a 4-char approval; template bodies. |
| Code Review Contribution | 3 | **Observed Fact:** approvals ≤4 chars. |
| Observable Devin Leverage | 3 | **Observed Fact:** 13 findings across `#458`/`#464`/`#465`, 0 answered. |
| Automation of Repetitive Work | 5 | **Observed Fact:** manual `client_configs` sync from prod DB — 5th time this month; subjects now say what was synced. |
| Consistency Across Windows | 5 | **Observed Fact:** 09-17 card 4.2 → 4.1; same pattern since 09-11. |

**Recommendation:** freeze config promotions until `#464` findings are dispositioned; stop self-merging `uat → prod`.

### vishnu-saikarthik — Medicodio · Overall 3.9 · Needs Support

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | **Observed Fact:** `#460` BMI fix merged and promoted with the "fix remains inactive" finding unanswered; three 31-file revert/re-revert commits on a PR-less branch. |
| Engineering Rigor | 3 | **Observed Fact:** prompt files recovered from a stash, reverted, re-restored; no PR; `#458` ×4 still unanswered. |
| Code Review Contribution | 3 | **Observed Fact:** "okay" approval on prod promotion `#459`. |
| Observable Devin Leverage | 4 | **Observed Fact:** one finding on `#460` unanswered into prod. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | **Observed Fact:** 09-17 card 4.4 → 3.9; prompt incidents 09-07, 09-16, 09-17. |

**Recommendation:** answer the `#460` finding and verify on prod; manage prompts via PR.

### Karthik Khatavkar (karthikmed) — Medicodio · Overall 4.6 · Needs Support (low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#652`/`#578` (163/150 files) merged; lockfile repair commit. |
| Engineering Rigor | 4 | **Observed Fact:** badge/template bodies; Devin findings from 09-17 unanswered at merge; branches named `hitesh/` under his login. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | **Observed Fact:** findings carried into `Dev_1.0` without response. |
| Automation of Repetitive Work | 5 | **Observed Fact:** lockfile churn repaired by hand twice. |
| Consistency Across Windows | NR | Second window seen. |

**Recommendation:** clarify authorship and post dispositions in `#652`/`#578`.

### svh-medicodio — Global Codio · NR (2 dims)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Code Review Contribution | 2 | **Observed Fact:** 0-char approval on `#1386` (250 files) 7 s before the author merged; 4/4 approvals this week ≤10 chars on >200-file PRs. |
| Consistency Across Windows | 4 | **Observed Fact:** same on `#1380` 09-16. |

**Recommendation:** approvals cite the gate output read.

### NandanDate-Medicodio — Medicodio · NR (2 dims)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Engineering Rigor | 3 | **Observed Fact:** `#461` prod and `#464` merged in 0 min; `#464` findings arrived 1 min after merge. |
| Code Review Contribution | 3 | **Observed Fact:** merger of record without review text. |

**Recommendation:** ≥30 min open-to-merge on `uat`/`prod`.

### ashwinsk-medicodio — Medicodio · NR (2 dims)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** dxex chain + v3 prompt promoted to live OP call-1 (3 commits, 23 files). |
| Engineering Rigor | 5 | **Observed Fact:** no PR, no eval artefact in repo; commit body states the criterion. |

**Recommendation:** PR with eval numbers before `uat`.

### Murali-Shetty19 — Medicodio · 4.0 · Needs Support (3 dims, low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** Chatwoot secret/docs fixes across 3 repos; `#581` closed unmerged. |
| Engineering Rigor | 4 | **Observed Fact:** same fix applied by hand in three repos; `#581` closed with a security finding open. |
| Observable Devin Leverage | 3 | **Observed Fact:** 4 findings, 0 answered. |

**Recommendation:** one-line disposition on `#581` incl. the anonymous-session finding.

### sameer-s-mansur, shaheen-khan11 — Medicodio · NR (1 dim)

Delivery 6: **Observed Fact:** integration concurrency/logging (sameer, 3 commits) and eCW PPV resilience (shaheen, 1 commit) pushed without PR. Everything else NR. **Recommendation:** route through PRs.

### akanksh-rv, Amrutha-Beedikar, Hitesh Shanthakumar, afifashaikh007, Shashvi1 — NR

No events in window. akanksh: `#1373` decisions still unrecorded (carried). Hitesh: no pushes; `hitesh/` branches merged under karthikmed.

## How to read the spread

**Observed Fact.** Twelve members have an overall score; nine are in *Mixed*, one *Solid*, three *Needs Support*. The spread from 7.6 to 3.9 is driven almost entirely by two dimensions: how Devin Review findings were treated (answered before merge vs. ignored into `uat`/`prod`) and whether approvals carried any text. Every Medicodio human approval today was 0–4 characters; every Global Codio merge above 100 files was performed by someone with commits on the branch. Three post-merge Devin QA verdicts landed today, none READY. Devin session data was unavailable, so no score reflects prompt quality, scoping, or effort.

**Inference.** The top of the spread (Medicodio-Amit, anirudh, amit-pandey, Saijyoti) is not the people writing the most code — it is the people who leave a written trail when a finding is closed or declined. The bottom (avinash, Vishnu) is where automated findings reach production paths unanswered; both have been in *Needs Support* for consecutive reports, so this is a pattern, not a day. New or lightly evidenced members (Saahil's PR under 12 h old; Sumedh with no Devin Review in his repo; Murali with one closed PR) carry low confidence and should be re-read tomorrow rather than acted on today.

**Recommendation.** Two mechanical changes would move most of the middle band up without anyone working harder: (1) branch protection requiring an approver with no commits on the branch plus a QA verdict quoted in the body for >100-file PRs in `globalcodio-monorepo`; (2) a merge-queue minimum wait and a one-sentence approval rule on `uat`/`prod`/`Dev_1.0` in the Medicodio repos. Until session telemetry is granted (`org.sessions.view`), treat the Devin column as "finding disposition quality", not "Devin adoption".
