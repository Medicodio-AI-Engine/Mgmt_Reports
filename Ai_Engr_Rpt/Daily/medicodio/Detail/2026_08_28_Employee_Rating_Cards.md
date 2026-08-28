# Employee Rating Cards — 2026-08-28 (review window 2026-08-27 03:00 → 2026-08-28 03:00 UTC)

Companion to `2026_08_28_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable** (`org.sessions.view` denied — HTTP 403, **9th consecutive run**). "Observable Devin Leverage" is scored **only** from Git evidence: `Co-Authored-By: Devin AI` trailers, `devin/*` branches and bot-authored PRs, and whether Devin Review findings were answered with pushed commits. Prompt quality, requested tests, correction burden and sessions that produced no commit are unobservable. A member who used Devin well without a commit scores **NR**, not low.
- **Jira is not queryable** (installed org-side, no tool exposed). Coordination, requirement quality, support load and ticket hygiene are outside the evidence base and their absence is not held against anyone.
- **"Findings answered" is an inference** — commits pushed after a finding report, not a verified fix.
- **Volume is not productivity.** Commit, PR and review counts are used only as evidence of *what kind* of work happened. One 3-file fix with a 5,000-character rationale can outscore 60 merge-and-promote commits, and the Rigor column reflects that.
- **Commit counting** follows the 08-27 method: commits are attributed to the day they were **authored**. Cherry-picks to `release/prod_*` are counted where they were authored, which inflates per-member all-branch totals for anyone who promotes; the report's default-branch series is the comparable one.
- **Members with no observed in-window activity are not scored** — absence is not a signal. Not scored today: akanksh-rv, hiteshjrxmedicodio, Amrutha-Beedikar, shaheen-khan11, SaahilVishwakarma, Murali-Shetty19, karthikmed, ANANYANG8055, SohamKakade.
- **Not rated (external):** `Azhao15` (`andrew.zhao@cognition.ai`, 3 commits opening the Devin KB-sync sub-PRs) is a Cognition address, not a team member.

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
| SaijyotiMeti | Global Codio | 8.1 | Strong | 8.0 | 9.0 | 10.0 | 6.0 | 5.0 | 9.0 | High |
| anirudh-medicodio | Global Codio | 7.9 | Solid | 9.0 | 8.5 | 5.0 | 8.0 | 7.0 | 9.0 | High |
| ragha82 | Global Codio | 7.1 | Solid | 8.0 | 7.0 | 3.0 | 9.0 | 9.0 | 6.0 | Medium |
| Pj-Vineeth-Kumar | Global Codio | 6.7 | Mixed | 7.0 | 7.0 | NR | 6.0 | 5.0 | 8.0 | Medium |
| svh-medicodio | Global Codio | 6.7 | Mixed | 8.0 | 7.5 | NR | 4.0 | 5.0 | 7.0 | Medium |
| amit-pandey-medicodio | Medicodio (app + integration) | 6.3 | Mixed | 8.5 | 5.0 | 2.0 | 8.0 | 7.0 | 7.5 | High |
| sameer-s-mansur | Medicodio (integration) | 6.2 | Mixed | 8.0 | 6.0 | NR | 3.0 | 5.0 | 8.0 | High |
| jatinkushwaha-medicodio | Medicodio (app) | 5.7 | Mixed | 7.5 | 5.5 | NR | 3.0 | 4.0 | 7.5 | High |
| NandanDate-Medicodio | Medicodio (engine) | 5.6 | Mixed | 8.0 | 4.5 | 2.0 | 6.0 | NR | 7.0 | High |
| Medicodio-Amit | Medicodio (engine) | 5.3 | Mixed | 7.5 | 6.5 | 2.0 | 3.0 | NR | 5.5 | Medium |
| Shashvi1 | Medicodio (engine) | 5.3 | Mixed | 7.0 | 6.5 | 3.0 | 3.0 | NR | 4.5 | Low |
| vishnu-saikarthik | Medicodio (engine) | 5.0 | Mixed | 6.5 | 4.0 | NR | NR | NR | 4.0 | Low |
| sumedh-codio | Medicodio (integration) | 4.6 | Needs Support | 5.0 | NR | 3.5 | NR | NR | 5.0 | Low |
| avinash-codio | Medicodio (engine) | 4.3 | Needs Support | 7.0 | 3.5 | 2.0 | 3.0 | NR | 5.0 | Medium |
| ashwinsk-medicodio | Medicodio (engine) | NR | — | 4.0 | NR | NR | NR | NR | 3.5 | Low |

Dimension means across scored members: **Delivery 7.3** (15 raters), **Rigor 6.2** (13), **Review 3.6** (9), **Devin 5.4** (11), **Automation 5.9** (8), **Consistency 6.4** (15).
Against the 08-27 cards (Delivery 7.4, Rigor 6.3, Review 4.4, Devin 5.2, Automation 5.5, Consistency 6.9): Devin leverage and automation rose, review fell sharply (42 of 43 human review events were empty or one word, against 23 of 25 the previous day), and delivery/rigor/consistency are essentially flat.

## Cards

### SaijyotiMeti — Global Codio — **8.1 (Strong)** — confidence High
- **Delivery 8.0** — 10 commits closing five defects on svh-medicodio's QA-hardening branch, then merged #1252 (28 files, +1,564/−129) at 00:01 after gates were confirmed green on re-run. Below 9 only because the window's authored volume was small.
- **Rigor 9.0** — shared the duplicate-name error code across API and web instead of duplicating it, added focus-on-error and honest partial-failure feedback, corrected a SQLSTATE regex, moved recruitment-clock dates onto `formatUtcDate`, stripped ticket/PR references from shipped comments, and recorded four separate evidence passes (`/check` + `/fix`, `/architect-review --advisory`, `/pr-review`, confirmed-green gates).
- **Review 10.0** — the organisation's **only** substantive human review today: a 5,597-character "Architect + EM Review — APPROVE (post-remediation)" verifying both Devin Review findings against the real code plus three of her own comments. The other 42 human review events org-wide were one word or empty.
- **Devin 6.0** — no delegation this window; Devin Review findings were verified against the code and fixed before approval, which is active consumption rather than the passive kind, but there is no session output of her own to credit.
- **Automation 5.0** — aware but manual: four hand-written `docs(review-log)` commits, and the duplicate-name defect fixed on two layers by hand rather than pinned by a contract test.
- **Consistency 9.0** — 153 commits in the week, 441 in the month; the only recurring source of architect-level review in the collected history, and the reason #1252 did not merge on an empty approval.

### anirudh-medicodio — Global Codio — **7.9 (Solid)** — confidence High
- **Delivery 9.0** — 45 commits taking the KB environment-sync branch from "does not run" to merged-and-evidenced: three sync-engine blockers, the operator surface finished, three Devin sub-PRs integrated, #1251 merged, and a three-environment preflight matrix closed out.
- **Rigor 8.5** — fixed a **bundle signature check that failed open**, closed platform-lane and cascade-delete tenancy holes, stopped a missing signing secret from burning a valid MFA code, added audit provenance and pagination conformance, and wrote 4 test commits including specs deliberately made *able to fail*. He also reverted his own bundle-budget change once the HLD showed the original value was intentional. Held below 9 by the empty GitHub approval on #1251.
- **Review 5.0** — the substance exists (his `/check` audit drove most of the day's fixes) but it is recorded in `docs(review-logs)` commits while the GitHub approval on #1251 is empty, so the audit trail is not where the merge happened. Down from 7.0 on 08-27 for the same reason, now with less independent review of others.
- **Devin 8.0** — merged three Devin-authored sub-PRs (discovery pack → shared-types contracts → docs reconciliation) into his branch and used the #1244 findings as a work queue; the delegation shape is exemplary. Not 9, because he authored no Devin-trailer commits himself (40 of 45 carry Claude trailers) and the sub-PRs were opened from a Cognition address.
- **Automation 7.0** — replaced three rollback implementations with one engine and extracted `EmailOtpService` so a second consumer stops re-implementing the flow; against that, 45 doc headers and 4 unit tests were backfilled by hand.
- **Consistency 9.0** — 279 commits in the week, 804 in the month, with test commits in both of his last two windows.

### ragha82 — Global Codio — **7.1 (Solid)** — confidence Medium
- **Delivery 8.0** — two delegated deliverables in one window: the URL-backed Documents tab view state (PRD → three scoped fixes → merged as #1251) and the hosted-dev Devin QA e2e enablement (#1253, opened 00:45 with a validation report); also merged #1249.
- **Rigor 7.0** — PRD before code, a written validation report for the first hosted Devin QA run, one `test(e2e)` commit, and an ESM-safe fix to the copy-completeness guard. Held at 7 because #1250 sits on the same branch with an unanswered Devin Review finding.
- **Review 3.0** — one approval on #1249 with an empty body.
- **Devin 9.0** — 7 of his 8 commits carry Devin trailers, scoped narrowly (search-buffer clear, rapid-group-toggle race, URL-back) with a PRD as the acceptance artefact. He is also the only member using Devin to *build* automation rather than features.
- **Automation 9.0** — the QA e2e skill adapter, UI/interaction matrix and explicit hosted API origin remove a class of repetitive work — the manual `qa update` cycles this repo has absorbed on 08-24, 08-25 and 08-27 — for the whole team.
- **Consistency 6.0** — 19 commits in the week, 30 in the month; contribution is sporadic in volume, but each appearance has left a mechanism behind (CI gates and auto-merge-on-green on 08-21, e2e enablement today).

### Pj-Vineeth-Kumar — Global Codio — **6.7 (Mixed)** — confidence Medium
- **Delivery 7.0** — #1249 merged (attorney case filters, 7 files) and the file-number display fixed; but his own Devin PR #1239 (155 files) is in its third window open with no reviewer, and today he removed a feature from it rather than landing any of it.
- **Rigor 7.0** — PRD-anchored work continued and the label/filter change is small and coherent; no tests of his own, and the executive-report removal has no recorded rationale in the repository.
- **Review NR** — no review events in the window.
- **Devin 6.0** — no Devin-trailer commits today, and the well-scoped delegation credited on 08-27 has stalled. Passive rather than absent, hence mid-band.
- **Automation 5.0** — three manual `dev`-into-branch merges, and case-list filter behaviour changed per surface across two windows rather than once.
- **Consistency 8.0** — 61 commits in the week, 162 in the month, with PRD-first delivery now his normal shape.

### svh-medicodio — Global Codio — **6.7 (Mixed)** — confidence Medium
- **Delivery 8.0** — 16 commits producing #1252 (28 files, 25 commits), merged the same window after a full review; nothing stalled.
- **Rigor 7.5** — Prisma-7 driver-adapter error detection, impossible calendar dates rejected on deadlines, a stale-closure bug in `clearFilters`, URL-state write races, a11y focus restore and label/copy accuracy, one test commit closing branch-coverage gaps, plus his own `/check` audit and recorded gate results (8/9 then 9/9). Below 8 because this whole PR is a post-merge QA pass on a feature that shipped two windows ago.
- **Review NR** — no review events.
- **Devin 4.0** — no delegation; the two Devin Review findings on his PR were closed by his reviewer, not by him.
- **Automation 5.0** — URL-state and focus-restoration corrected surface-by-surface (four commits) instead of extracted into one tested utility; three hand-written review-log commits.
- **Consistency 7.0** — 43 commits in the week, 232 in the month; the pre-review self-audit is new and worth keeping.

### amit-pandey-medicodio — Medicodio (app + integration) — **6.3 (Mixed)** — confidence High
- **Delivery 8.5** — 13 Devin ops-dashboard PRs merged to `Dev_1.0` plus two prod cherry-picks, and a substantial hand-built F35 prompt registry (#249). Nothing stalled; the ops dashboard's facility-day model went from broken to coherent in one window.
- **Rigor 5.0** — the PR bodies are genuinely good (1.4k–2.9k characters each, naming defect and state semantics), but **13 behaviour changes to a production operations dashboard shipped with zero tests**, two were merged with a Devin Review findings report outstanding (#585, #590), and two reached `release/prod_1.0` the same morning.
- **Review 2.0** — **20 approvals, every single one with an empty body**, including the 13 PRs produced by his own sessions. This is the day's largest control gap and it is his to close.
- **Devin 8.0** — 38 Devin-trailer commits, the highest single-day figure in the collected history, with the best scoping in the org: small single-purpose PRs, iterative correction, cherry-picks documented separately. Held below 9 only because he is also the approver of his own output, so the loop has no independent reader.
- **Automation 7.0** — the F35 prompt registry moves prompt text out of files into seeded DB tables **with a drift check for duplicated sections** — a real removal of repetitive editing. Against that, the promotion fan-out flagged since 08-20 recurred.
- **Consistency 7.5** — 128 commits in the week, 308 in the month, with the mix shifting from merges/promotions toward delegated authorship.

### sameer-s-mansur — Medicodio (integration) — **6.2 (Mixed)** — confidence High
- **Delivery 8.0** — four production-correctness fixes (cached re-run false warning, dual batch-row writers, blank insurance category, event-driven batch silencing the RPA warning) plus the gender-logic revamp, carried through UAT and prod in six PRs.
- **Rigor 6.0** — the reasoning is written down before the code ("problem space + blast radius (parked, nothing implemented)"; verified SIS column names and values), which is the best requirement practice in the Medicodio repos — but four changes to production batch semantics shipped with **zero tests**, and #254 was self-merged 7 minutes after opening.
- **Review NR** — no review events.
- **Devin 3.0** — no Devin evidence for a sixth consecutive window, while the four invariants he specified in prose today are the most obviously delegable test suite in the organisation.
- **Automation 5.0** — repeated the promotion fan-out (4 of 6 PRs) with template-only bodies, flagged every day since 08-20.
- **Consistency 8.0** — 75 commits in the week, 186 in the month; the steadiest contributor in the collected data, and self-merges fell from 2 to 1.

### jatinkushwaha-medicodio — Medicodio (app) — **5.7 (Mixed)** — confidence High
- **Delivery 7.5** — 12 commits across both app repos; five PRs merged (encounters context endpoint, mentions-to-plain-text, router catch-all fix, login error handling in both layers) plus the batch-outcome index cherry-picked to prod.
- **Rigor 5.5** — commit subjects name the user-facing effect and the index ships with its migration, but the patient-data **decryption refactor and age-preservation fix carry no tests**, and #511 was self-merged.
- **Review NR** — no review events.
- **Devin 3.0** — no Devin usage; the login error-message matrix and the encounter decrypt/patch path are both table-driven test work.
- **Automation 4.0** — the same change authored twice across nodejs and react in four pairs today, plus a manual `Dev_1.0` sync — repetition already flagged on 08-27.
- **Consistency 7.5** — 45 commits in the week, 137 in the month, steady scope across both repos.

### NandanDate-Medicodio — Medicodio (engine) — **5.6 (Mixed)** — confidence High
- **Delivery 8.0** — 19 commits and two substantial features landed (#406 14 files, #407 17 files: `guidelines_journey` per-target attribution, laterality/BMI/split/`excludes1` lanes with STEP-10 push logging), plus 7 engine PRs merged. His strongest delivery window in the collected history.
- **Rigor 4.5** — every behaviour change is paired with a `docs` commit explaining the projection semantics, which is genuinely good; but there are **no tests** on logic he has now rewritten three days running, and he merged promotion #410 (53 files to `release/prod_3.0`) on a 439-character template body with a Devin Review finding reported.
- **Review 2.0** — 8 approvals, every body "okay" or "ok", including two 14–17-file features and two prod promotions.
- **Devin 6.0** — opened his **first** Devin PR (#405, 3.7k-character body, three named deliverables, 2 trailer commits) — a real step forward, still a draft at collection time.
- **Automation NR** — no automation evidence either way.
- **Consistency 7.0** — 43 commits in the week, 129 in the month; reliably the engine's non-author approver, which is why engine PRs are rarely self-merged.

### Medicodio-Amit — Medicodio (engine) — **5.3 (Mixed)** — confidence Medium
- **Delivery 7.5** — #409 merged (24 files, +1,326: ENM diagnosis-drop escalation with prod-only Teams alerts) and #411 opened (combination-code I.B.9 redesign). Capped because #411 carries 3 open findings and his Devin draft #393 has not moved since 08-25.
- **Rigor 6.5** — the best PR bodies in the engine (5.9k and 4.5k characters, stating intent and risk) and deliberate blast-radius control (Teams alerts production-only, `enm_dx_coverage` kept off in podiatry); no tests, and the promotion he opened for his own change (#410, 53 files) has a template-only body.
- **Review 2.0** — two comment events on #409, both with empty bodies.
- **Devin 3.0** — draft #393 (episodic ICD memory recall) idle since 08-25; the only commit on that branch today came from someone else. Delegated effort not carried to a reviewable state.
- **Automation NR**.
- **Consistency 5.5** — 10 commits in the week, 79 in the month, delivered as occasional large pieces.

### Shashvi1 — Medicodio (engine) — **5.3 (Mixed)** — confidence Low
- **Delivery 7.0** — #402 (3 files) opened and merged the same window and promoted onward; a clean delivery shape.
- **Rigor 6.5** — a 5,462-character PR body on a 3-file diff explaining the rule semantics is the best body-to-diff ratio of the day and makes review possible without reading the diff. No tests, and the change is not pinned by anything.
- **Review 3.0** — one comment event on her own PR with an empty body.
- **Devin 3.0** — no delegation, and 1 Devin Review finding was still reported when the PR merged 22 minutes later.
- **Automation NR**.
- **Consistency 4.5** — 3 commits in the week, 9 in the month; too little history to trend, hence Low confidence.

### vishnu-saikarthik — Medicodio (engine) — **5.0 (Mixed)** — confidence Low
- **Delivery 6.5** — #400 (7 files, Z68 gated by the E66 code for `vital_gastro_enm`) landed and reached production the same hour.
- **Rigor 4.0** — precise commit subject naming the gating condition and the client config, but no tests, and #401 promoted 17 files to `release/prod_3.0` 32 seconds after #400 merged, on a template-only body, with a finding reported.
- **Review NR / Devin NR / Automation NR** — no evidence either way.
- **Consistency 4.0** — 2 commits in the week, 14 in the month.
- Three rated dimensions, so an overall is given, but treat it as a thin sample.

### sumedh-codio — Medicodio (integration) — **4.6 (Needs Support)** — confidence Low
- **Delivery 5.0** — four merge commits; his contribution in this window is gatekeeping, not authorship.
- **Rigor NR** — no authored behaviour change to assess.
- **Review 3.5** — six approvals on integration PRs including a 16-file prod sync, all with empty bodies. Above the floor because his availability is *why* only one integration PR was self-merged, but nothing was recorded about what he checked.
- **Devin NR / Automation NR**.
- **Consistency 5.0** — appears as a reviewer in only his second collected window; Low confidence accordingly.

### avinash-codio — Medicodio (engine) — **4.3 (Needs Support)** — confidence Medium
- **Delivery 7.0** — two scoped changes landed and reached production: #403 (15 files, `tcm_trigger` field correction) and #408 (8 files, lab CPT sourced from P039). A real improvement in shape on the 223-file branch of 08-27.
- **Rigor 3.5** — #404 promoted 17 files to `release/prod_3.0` **26 seconds** after #403 merged and was merged 25 seconds later, on a 439-character template body, with a finding reported; no tests on chart-routing changes; this is the same mechanism flagged on 08-25 and 08-27.
- **Review 2.0** — two approvals, both the word "ok", on 14- and 17-file features.
- **Devin 3.0** — no Devin evidence, while he has now corrected trigger-field mismatches twice in one week — the textbook fixture-suite delegation.
- **Automation NR**.
- **Consistency 5.0** — 11 commits in the week, 78 in the month.

### ashwinsk-medicodio — Medicodio (engine) — **NR** — confidence Low
- **Delivery 4.0** — one commit ("added icd memory manager agent") on the `feat/icd-memory-recall` branch behind draft PR #393; nothing reached a reviewable state for a third window.
- **Consistency 3.5** — 4 commits in the week, 6 in the month.
- All other dimensions **NR**; overall **NR** (fewer than three rated dimensions). This is absence of evidence, not evidence of absence.

## How to read the spread

**Observed Fact.** Today's numbers come from GitHub only: 118 default-branch commits, 48 PRs opened, 43 merged, **19 Devin-authored PRs opened and 17 merged** (against 29/23 for the whole preceding month), 49 unique `Co-Authored-By: Devin AI` commits, 103 Devin Review bot events, 43 human review events of which **1** was substantive, 6 test commits — all six in Global Codio and **none** in the four Medicodio repositories — and 9 PRs merged after a findings report with no recorded response.

**Inference.** The spread has changed character since 08-27. It is no longer mainly a Devin-adoption spread: the highest Devin score in the org today belongs to a Medicodio member (amit-pandey, 8.0) and the biggest automation contribution to a Global Codio member who used Devin to automate QA (ragha82, 9.0). What still separates the top of the table from the bottom is **whether anything independent happens between "code written" and "code in production"**. The three highest cards all have a recorded verification step — an architect review, a three-environment preflight matrix, a validation report. The four lowest all merge on a one-word or empty approval, most of them within minutes, and several while a machine reviewer is still reporting findings. Adoption solved the throughput problem this window and made the review problem the binding constraint: 17 Devin PRs merged and one substantive human review is not a sustainable ratio.

**Recommendation.** Do not act on these scores as individual performance verdicts. Four mechanisms would move most of the bottom half by two points without anyone working differently: (1) a non-author approver required on `Dev_1.0` and `dev`; (2) merge blocked while a Devin Review finding is unanswered; (3) generated promotion PR bodies; (4) one delegated test-suite session per Medicodio repo, seeded with the defects already listed in today's PR titles. Three of the four are configuration changes, and the fourth is a Devin task the team has now demonstrated it can run 17 times in a day.
