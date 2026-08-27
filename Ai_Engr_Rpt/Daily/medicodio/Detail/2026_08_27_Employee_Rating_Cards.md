# Employee Rating Cards — 2026-08-27 (review window 2026-08-26 03:00 → 2026-08-27 03:00 UTC)

Companion to `2026_08_27_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable** (`org.sessions.view` denied — HTTP 403, 8th consecutive run). "Observable Devin Leverage" is scored **only** from Git evidence: `Co-Authored-By: Devin AI` trailers, Devin-authored branches/PRs, and whether Devin Review findings were answered with pushed commits. Prompt quality, requested tests, correction burden and sessions that produced no commit are unobservable. A member who used Devin productively without a commit scores **NR**, not low.
- **Jira is not queryable** (installed at org level, no tool exposed). Coordination, requirement quality, support load and ticket hygiene are outside the evidence base and their absence is not held against anyone.
- **"Addressed findings" is an inference** — commits pushed after a finding was posted, not a verified fix.
- **Volume is not productivity.** Commit, PR and review counts are used only as evidence of *what kind* of work happened. Two 2-file fixes that landed and were promoted can outscore 35 commits of merge-day remediation, and the Rigor column reflects that.
- **Commit counting**: commits are attributed to the day they were written (default-branch history at collection time), not the day they landed. Comparisons to the 08-24/08-25 cards' raw figures are method-adjusted, not literal.
- **Members with no observed activity in the window are not scored** — absence is not a signal. Not scored today: akanksh-rv, ragha82, Amrutha-Beedikar, shaheen-khan11, Medicodio-Amit, Murali-Shetty19, karthikmed, vishnu-saikarthik, ANANYANG8055, SohamKakade, SaahilVishwakarma-as-committer.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| Delivery & Follow-Through | 25 | Work stalls or does not reach a reviewable state | Work progresses; landing is uneven | Meaningful work reaches a reviewable/landed state the same day | Substantial scoped delivery, closed out end to end |
| Engineering Rigor | 25 | No tests/docs; unsafe or unreviewable changes | Some care; gaps in tests, docs or risk handling | Tests/docs/risk handled proportionally to blast radius | Risk named, rollback stated, invariants defended, evidence attached |
| Code Review Contribution | 15 | Approvals with no content | One-line reviews on low-risk changes | Specific, evidenced review with a verdict | Architect-level review that changes the outcome |
| Observable Devin Leverage | 15 | Devin signal ignored or discarded | Devin Review consumed passively | Devin delegated on well-scoped work; findings closed | Devin used where leverage is highest, with acceptance criteria and review of output |
| Automation of Repetitive Work | 10 | Repeats manual work already flagged | Aware but manual | Automates or scripts a repeated task | Removes a class of repetitive work for the team |
| Consistency Across Windows | 10 | Erratic; no pattern | Sporadic contribution | Steady across day/week/month | Steady and improving across all windows |

Weighted average of rated dimensions only; **NR** dimensions are excluded and the remaining weights renormalized. Fewer than three rated dimensions → overall **NR**. Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**.

## Summary grid

| Member | Product | Overall | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| ------ | ------- | ------- | ---- | -------- | ----- | ------ | ----- | ---------- | ----------- | ---------- |
| SaijyotiMeti | Global Codio | 8.8 | Strong | 9.0 | 9.0 | 10.0 | 9.0 | 5.0 | 9.0 | High |
| anirudh-medicodio | Global Codio | 8.4 | Strong | 9.0 | 8.5 | 7.0 | 9.0 | 7.0 | 9.0 | High |
| Pj-Vineeth-Kumar | Global Codio | 7.6 | Solid | 7.5 | 7.5 | NR | 9.0 | 6.0 | 8.0 | Medium |
| sameer-s-mansur | Medicodio (integration) | 6.1 | Mixed | 8.5 | 6.0 | NR | 3.0 | 6.0 | 8.0 | High |
| Shashvi1 | Medicodio (engine) | 5.9 | Mixed | 8.0 | 7.0 | 3.0 | 4.0 | NR | 5.0 | Low |
| hiteshjrxmedicodio | Medicodio (app) | 5.9 | Mixed | 7.0 | 6.0 | NR | 3.0 | NR | 7.0 | Medium |
| jatinkushwaha-medicodio | Medicodio (app) | 5.5 | Mixed | 7.5 | 6.0 | 3.0 | 3.0 | 5.0 | 7.5 | High |
| avinash-codio | Medicodio (engine) | 4.9 | Needs Support | 7.0 | 4.0 | NR | 3.0 | NR | 5.0 | Medium |
| amit-pandey-medicodio | Medicodio (app + integration) | 4.7 | Needs Support | 6.5 | 5.0 | 2.0 | 3.5 | 4.0 | 6.0 | Medium |
| sumedh-codio | Medicodio (integration) | 4.7 | Needs Support | 5.0 | NR | 4.0 | NR | NR | 5.0 | Low |
| NandanDate-Medicodio | Medicodio (engine) | 4.6 | Needs Support | 6.0 | 4.0 | 2.0 | NR | NR | 6.5 | Medium |
| svh-medicodio | Global Codio | NR | — | 7.0 | NR | NR | NR | NR | 7.0 | Low |
| ashwinsk-medicodio | Medicodio (engine) | NR | — | 4.0 | NR | NR | NR | NR | 3.0 | Low |
| SaahilVishwakarma | Global Codio | NR | — | 4.0 | NR | NR | NR | NR | 5.0 | Low |

Dimension means across scored members: **Delivery 7.4** (11 raters), **Rigor 6.3** (10), **Review 4.4** (7), **Devin 5.2** (9), **Automation 5.5** (6), **Consistency 6.9** (11).
Against the 08-25 cards (Delivery 5.8, Rigor 5.3, Review 2.3, Devin 4.2, Automation 6.0, Consistency 5.5): every dimension improved except Automation, which fell because more members repeated manual work already flagged (promotion fan-out, hand-written review logs, hand-applied UI migrations).

## Cards

### SaijyotiMeti — Global Codio — **8.8 (Strong)** — confidence High
- **Delivery 9.0** — 34 commits closing her own `/check` findings on two Devin branches, then merged both: #1208 (43 files, open since 08-21) and #1243 (75 files, same-day). She converted the org's Devin backlog into shipped code.
- **Rigor 9.0** — 4 test commits (service/repository/helper coverage, `my_note` retirement assertions, settings-card save/cache/error states), deny-by-default for an unmodeled case-party role, audit coverage on the platform-admin `firm_config` write path, Swagger/design-doc backfill, and a tech-debt ticket (CLEANUP-103) plus issue #1245 filed instead of a TODO. Held below 10 because #1243 merged 4 minutes after a new Devin Review finding with no note on why it was acceptable.
- **Review 10.0** — the only two substantive human reviews in the org today: full "Architect + EM Review — APPROVE WITH NITS" write-ups on #1208 and #1243, each followed by pushed fixes. 23 of the other 25 human review events org-wide were one word or empty.
- **Devin 9.0** — 15 Devin Review findings consumed, 13 answered with pushed fixes; independent architect review rather than trust in the bot; merge only after a recorded green gate run. This is the reviewing half of the loop the last six reports asked for.
- **Automation 5.0** — aware but manual: 6 hand-written `docs(review-logs)` commits and a hand-written test backfill, both mechanical enough to script or delegate.
- **Consistency 9.0** — 191 commits in the week, 443 in the month; the only recurring source of architect-level review in the collected history.

### anirudh-medicodio — Global Codio — **8.4 (Strong)** — confidence High
- **Delivery 9.0** — 34 remediation commits on svh-medicodio's branch, then merged #1238 (190 files, Document Checklist Groups); in parallel ran a Devin session producing #1244 (77 files, opened for review).
- **Rigor 8.5** — closed a PII leak in a reminder CTA, retiered 12 checklist mutations off `documents:read`, added audit rows for four mutations that wrote none, bounded 8 unbounded list reads, mapped Prisma driver errors to contractual HTTP status, 3 test commits plus one gate-failing spec fixed, and cleaned up dead props/tombstones in the same PR. Below 9 because a 190-file PR merged with an **empty** GitHub approval.
- **Review 7.0** — the review genuinely changed the outcome (34 defects closed pre-merge), but the record lives in a `docs(review-logs)` commit while GitHub shows a content-free approval, so the audit trail is not where the merge happened.
- **Devin 9.0** — 37 `Co-Authored-By: Devin AI` commits, the largest single-day Devin authorship in the collected period; 12 of 13 Devin Review findings on #1244 answered with pushed fixes; scoping explicitly phased ("Phase 1").
- **Automation 7.0** — replaced literal branching with registries for origin, waive-state and audience, and deleted a single-consumer abstraction: removes per-case branching for everyone who extends checklists next.
- **Consistency 9.0** — 303 commits in the week, 817 in the month; first window in which he authored a Devin PR himself rather than only reviewing Devin output.

### Pj-Vineeth-Kumar — Global Codio — **7.6 (Solid)** — confidence Medium
- **Delivery 7.5** — #1243 (75 files) opened and merged the same day. Capped below 8 because #1239 (155 files, his best delegation of the month per the 08-25 report) went a second day with no commits and no reviewer while he started this feature.
- **Rigor 7.5** — three PRD commits before any code, revised twice to fold in reviewer decisions; manual file-number collisions mapped to 409; read-only field while settings load; org-scoped settings reads. No test commits of his own — SaijyotiMeti wrote them during review.
- **Review NR** — no review events in the window.
- **Devin 9.0** — 13 Devin-trailer commits; 8 Devin Review cycles, 11 of 12 findings answered with pushed fixes; PRD-anchored scoping, and he accepted the simpler design (drop the counter table) when review pushed back.
- **Automation 6.0** — the `firm_config`-only design avoids a counter table and its migration, but the same "read settings under the caller's org scope" concern was fixed surface-by-surface across four commits rather than once.
- **Consistency 8.0** — 46 commits in the week, 158 in the month; two PRD-anchored Devin features in two days, one now landed.

### sameer-s-mansur — Medicodio (integration) — **6.1 (Mixed)** — confidence High
- **Delivery 8.5** — 7 PRs in the window; six production-data correctness fixes plus a client document fix, carried through UAT and prod. Nothing stalled.
- **Rigor 6.0** — the reasoning is exemplary and written down (batch-count question settled on max-wins with the removal order pinned; `.pem` files permanently untracked), but six behaviour changes to production batch semantics shipped with **zero** tests, and two went in via self-merge.
- **Review NR** — no review events.
- **Devin 3.0** — no Devin evidence; the four invariants he specified by hand today are the most obviously delegable test suite in the org.
- **Automation 6.0** — closed the `.pem` tracking class permanently, but repeated the promotion fan-out (5 of 7 PRs) flagged every day since 08-20.
- **Consistency 8.0** — 76 commits in the week, 192 in the month; the steadiest contributor in the collected data, and self-merges dropped from 4 (08-25) to 2.

### Shashvi1 — Medicodio (engine) — **5.9 (Mixed)** — confidence Low
- **Delivery 8.0** — two 2-file fixes (exclusion-validation lane, EMR appointment-type alias) opened and merged the same day, then promoted to prod via #399. The cleanest delivery shape in the engine today.
- **Rigor 7.0** — small diffs, conventional-commit subjects that name the defect, Claude-assisted. No tests, and the specialty-table lane change is not pinned by anything.
- **Review 3.0** — two comment events on #397 with empty bodies.
- **Devin 4.0** — no delegation; 2 Devin Review findings on #397 were still open when it merged and was promoted toward prod.
- **Automation NR** — no automation evidence either way.
- **Consistency 5.0** — 5 commits in the week, 8 in the month; too little history to trend, hence Low confidence.

### hiteshjrxmedicodio — Medicodio (app frontend) — **5.9 (Mixed)** — confidence Medium
- **Delivery 7.0** — #500 (Prediction Trail redesign, 38 files) and #499 (KB dropdowns in dialogs, 15 files) both merged today; branch kept synced with `Dev_1.0`.
- **Rigor 6.0** — dated, scoped branch names and coherent PRs, but no test commits on a 38-file UI redesign.
- **Review NR** — no review events.
- **Devin 3.0** — the dialog-dropdown work is a repetitive pattern migration applied by hand across 15 files while the shared portalled component was being built in the other repo — leverage left on the table.
- **Automation NR**.
- **Consistency 7.0** — 80 commits in the week, 93 in the month; work now reaches `Dev_1.0` instead of sitting on personal branches.

### jatinkushwaha-medicodio — Medicodio (app) — **5.5 (Mixed)** — confidence High
- **Delivery 7.5** — 11 commits across both app repos; three PRs merged plus #502; PHI fixes, a portalled multi-select, and a batch-outcome index shipped the same day.
- **Rigor 6.0** — commit subjects state the security consequence and the performance fix ships with its migration, but six behaviour changes (including three on the PHI boundary) carry no tests, and #502 was self-merged.
- **Review 3.0** — approved #577 (46 files → prod) and #501 (56 files → prod) with `lgtm`.
- **Devin 3.0** — no Devin usage; the PHI masking/unmasking regression suite is the clearest available delegation.
- **Automation 5.0** — repeated the manual `Dev_1.0`→feature-branch sync in both repos and removed PHI columns endpoint-by-endpoint rather than adding a schema allowlist test.
- **Consistency 7.5** — 61 commits in the week, 124 in the month, with scope widening from dashboards to the PHI boundary.

### avinash-codio — Medicodio (engine) — **4.9 (Needs Support)** — confidence Medium
- **Delivery 7.0** — the long-lived `feat/guideline` branch flagged on 08-25 finally landed (#395, 223 files) and reached prod (#396). Real progress on the exact item the last report raised.
- **Rigor 4.0** — 223 files promoted to `release/prod_3.0` 11 minutes after reaching `uat`, approved "okay", with 3 Devin Review findings open; commit messages "Testing the ggl changes" and "devin changes and vaccine acces"; no tests for a fix whose defect was that an entire chart class was skipped. The single-anchor commit body, which explains the user-visible impact, is the counter-example and the reason this is 4 and not lower.
- **Review NR** — no review events.
- **Devin 3.0** — a commit message references "devin changes" but there is no Devin-authored commit, branch or session artefact to corroborate it, and 3 findings were left open on the prod promotion.
- **Automation NR**.
- **Consistency 5.0** — 19 commits in the week, 76 in the month, delivered as one large branch at a time.

### amit-pandey-medicodio — Medicodio (app + integration) — **4.7 (Needs Support)** — confidence Medium
- **Delivery 6.5** — opened both production promotions (#577, #501) and merged five PRs; opened integration #248 (35 files) which remains open.
- **Rigor 5.0** — two production promotions totalling 102 files opened with **no description**, no risk note and no rollback statement; #248 has no tests. He is, however, the reason the app repos avoid self-merges.
- **Review 2.0** — five approvals today, every one with an empty body, including the two he did not author.
- **Devin 3.5** — no delegation, but the one Devin Review finding on #248 was followed by pushed commits, so the signal was consumed passively.
- **Automation 4.0** — repeats the promotion fan-out and empty-approval pattern flagged since 08-20; nothing automated.
- **Consistency 6.0** — 52 commits in the week, 230 in the month, almost entirely merges and promotions.

### sumedh-codio — Medicodio (integration) — **4.7 (Needs Support)** — confidence Low
- **Delivery 5.0** — three sync commits on #243; his contribution in this window is gatekeeping, not authorship.
- **Rigor NR** — no authored behaviour change to assess.
- **Review 4.0** — five approvals on integration PRs including an 84-file prod promotion and a prod hotfix, bodies "approve" or empty. Scored above the empty-approval floor because his presence is *why* integration self-merges fell from four to two, but nothing was recorded about what he checked.
- **Devin NR**.
- **Automation NR**.
- **Consistency 5.0** — first window in which he appears as a reviewer in the collected data; Low confidence accordingly.

### NandanDate-Medicodio — Medicodio (engine) — **4.6 (Needs Support)** — confidence Medium
- **Delivery 6.0** — merged five engine PRs and kept the release path moving, including two promotions to `release/prod_3.0`.
- **Rigor 4.0** — approved and merged a 223-file prod promotion 11 minutes after it reached UAT, with 3 open Devin Review findings and no risk or rollback note; #399 merged 6 minutes after opening.
- **Review 2.0** — five approvals, every body the word "okay".
- **Devin NR** — no Devin evidence; his gap is review content, not delegation, so this is not scored against him.
- **Automation NR**.
- **Consistency 6.5** — 35 commits in the week, 132 in the month; reliably available as the non-author approver, which is why engine PRs are not self-merged.

### svh-medicodio — Global Codio — **NR** — confidence Low
- **Delivery 7.0** — no commits in the window, but his feature (#1238, Document Checklist Groups, 190 files) was merged today.
- **Rigor NR / Review NR / Devin NR / Automation NR** — no in-window authored evidence. The shape of anirudh's 34 remediation commits (RBAC tiering, missing audit rows, unbounded reads, a PII leak) suggests pre-PR gate gaps, but that is an inference about work done on 08-24/08-25 and is not scored here.
- **Consistency 7.0** — 47 commits in the week, 248 in the month.
- **Overall NR** — only two rated dimensions. This is not a low score; it reflects a window in which his work was being landed by someone else.

### ashwinsk-medicodio — Medicodio (engine) — **NR** — confidence Low
- **Delivery 4.0** — one commit on `feat/icd-memory-recall` behind draft PR #393; nothing reached a mergeable state.
- **Consistency 3.0** — 3 commits in the week, 4 in the month.
- All other dimensions **NR**; overall **NR** (fewer than three rated dimensions). Absence of evidence, not evidence of absence.

### SaahilVishwakarma — Global Codio — **NR** — confidence Low
- **Delivery 4.0** — one QA defect issue filed (#1242) with reproduction detail; no code, and his two issues from 08-25 (#1240, #1241) remain unassigned.
- **Consistency 5.0** — 42 commits in the week, 113 in the month (outside this window).
- All other dimensions **NR**; overall **NR**.

## How to read the spread

**Observed Fact.** Today's numbers come from GitHub only: 119 default-branch commits, 20 PRs opened, 23 merged, 25 human review events of which 2 were substantive, 90 Devin Review bot events raising 51 findings of which 38 were followed by pushed commits, 50 `Co-Authored-By: Devin AI` commits across branches, and 0 test commits in the four Medicodio repositories against 16 behaviour commits. Two Devin-authored PRs merged on the same day for the first time in the collected history.

**Inference.** The scored spread is not a spread of talent; it tracks **which repository someone works in**. The three Strong/Solid cards are all Global Codio, where a written PRD or phase plan precedes the code, Devin authors the breadth, an architect reviews with a verdict, and a gate run is recorded before merge. The Needs Support cards cluster on the Medicodio release path, where the same person opens, approves and merges promotion PRs of 46–223 files with one word or nothing written down, and where nobody wrote a test today. That is a **process difference**, and it would move most of these scores by two points if the process moved — which is why the corrective actions in the companion report are all mechanisms (branch protection, a review template, findings-answered-before-promotion, a promotion script) rather than individual performance conversations.

**Recommendation.** Treat three cards as calls to action rather than judgements: NandanDate-Medicodio, amit-pandey-medicodio and sumedh-codio are each doing the *structurally* right thing (being the independent approver on a production path) and are scored down only for recording nothing while doing it. Fixing that costs three lines per approval and is the highest-leverage change available to the Medicodio side of the org. Conversely, do not read SaijyotiMeti's and anirudh-medicodio's Strong cards as headroom to load them further: today they were the only two substantive reviewers in a 25-review day, and the companion report's first recommendation is to make their practice a template so it survives their absence.
