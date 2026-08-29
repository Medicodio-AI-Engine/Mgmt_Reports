# Employee Rating Cards — 2026-08-29 (review window 2026-08-28 03:00 → 2026-08-29 03:00 UTC)

Companion to `2026_08_29_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable** (`org.sessions.view` denied — HTTP 403, **10th consecutive run**). "Observable Devin Leverage" is scored **only** from Git evidence: `Co-Authored-By: Devin AI` trailers, `devin/*` branches and bot-authored PRs, and whether Devin Review findings were answered with pushed commits. Prompt quality, requested tests, acceptance criteria, correction burden, and sessions that produced no commit are unobservable. A member who used Devin well without a commit scores **NR**, not low. **Today the whole organisation produced 0 Devin-trailer commits, so this dimension is measuring consumption and delegation outcomes, not authorship.**
- **Jira is not queryable** (installed org-side, no tool exposed). Coordination, requirement quality, support load and ticket hygiene are outside the evidence base and their absence is not held against anyone. **Sentry** has no usable token, so no production-incident signal is included.
- **"Findings answered" is an inference** — commits pushed after a findings report, not a verified fix.
- **Volume is not productivity.** Commit, PR and review counts are used only as evidence of *what kind* of work happened. One 3-file fix with a written rationale can outscore 60 merge-and-promote commits, and the Rigor column reflects that.
- **Commit counting** attributes commits to the day they were **authored**; cherry-picks to release branches are counted where authored, which inflates all-branch totals for anyone who promotes. Unpushed work is invisible until pushed — this is why akanksh-rv, whose 08-27 commits only became visible with #1260 on 08-28, carries Insufficient-Data comparisons despite real volume.
- **Members with no observed in-window activity are not scored** — absence is not a signal. Not scored today: Medicodio-Amit, Shashvi1, hiteshjrxmedicodio, shaheen-khan11, SaahilVishwakarma, Murali-Shetty19, ANANYANG8055, SohamKakade, anirudhdmedicodio.
- **Not rated (external/upstream or automation):** `devinfoley`, `nickyleach` and other `paperclip-ai` upstream authors; `devin-ai-integration[bot]`, `github-actions[bot]`, `dependabot[bot]`, `claude`.
- `karthikmed` is scored on fork/tooling maintenance only and is not mapped to a product surface.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| Delivery & Follow-Through | 25 | Work stalls or does not reach a reviewable state | Work progresses; landing is uneven | Meaningful work reaches a reviewable/landed state the same day | Substantial scoped delivery, closed out end to end |
| Engineering Rigor | 25 | No tests/docs; unsafe or unreviewable changes | Some care; gaps in tests, docs or risk handling | Tests/docs/risk handled proportionally to blast radius | Risk named, rollback stated, invariants defended, evidence attached |
| Code Review Contribution | 15 | Approvals with no content | One-line reviews on low-risk changes | Specific, evidenced review with a verdict | Architect-level review that changes the outcome |
| Observable Devin Leverage | 15 | Devin signal ignored or discarded | Devin Review consumed passively | Devin delegated on well-scoped work; findings closed | Devin used where leverage is highest, with acceptance criteria and review of output |
| Automation of Repetitive Work | 10 | Repeats manual work already flagged | Aware but manual | Automates or scripts a repeated task | Removes a class of repetitive work for the team |
| Consistency Across Windows | 10 | Erratic; no pattern | Sporadic contribution | Steady across day/week/month | Steady and improving across all windows |

Weighted average of rated dimensions only; **NR** dimensions are excluded and the remaining weights renormalised. Fewer than three rated dimensions → overall **NR**. Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**.

## Summary grid

| Member | Product | Overall | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| ------ | ------- | ------- | ---- | -------- | ----- | ------ | ----- | ---------- | ----------- | ---------- |
| SaijyotiMeti | Global Codio | 8.0 | Strong | 8.0 | 9.0 | 10.0 | 5.0 | 6.0 | 9.0 | High |
| ragha82 | Global Codio | 7.5 | Solid | 7.5 | 7.0 | NR | 8.5 | 9.0 | 6.0 | Medium |
| anirudh-medicodio | Global Codio | 7.0 | Solid | 8.5 | 8.0 | 2.5 | 6.0 | 7.0 | 9.0 | High |
| akanksh-rv | Global Codio | 7.0 | Solid | 8.5 | 8.0 | NR | 3.5 | 5.5 | 7.5 | Medium |
| svh-medicodio | Global Codio | 6.7 | Mixed | 8.0 | 7.0 | NR | 4.5 | 6.0 | 7.0 | Medium |
| sameer-s-mansur | Medicodio (integration) | 6.7 | Mixed | 8.5 | 6.5 | NR | 3.0 | 6.5 | 8.5 | High |
| Pj-Vineeth-Kumar | Global Codio | 5.9 | Mixed | 6.5 | 6.5 | NR | 4.0 | 5.0 | 7.0 | Medium |
| amit-pandey-medicodio | Medicodio (integration + app) | 5.8 | Mixed | 8.0 | 6.5 | 2.0 | 3.0 | 7.0 | 7.5 | High |
| jatinkushwaha-medicodio | Medicodio (app) | 5.7 | Mixed | 7.5 | 5.0 | NR | 3.0 | 6.0 | 7.0 | High |
| karthikmed | Shared (fork/tooling) | 5.3 | Mixed | 5.5 | NR | NR | NR | 6.0 | 4.0 | Low |
| Amrutha-Beedikar | Global Codio | 5.2 | Mixed | 7.5 | 5.0 | 2.0 | NR | 5.0 | 5.0 | Medium |
| vishnu-saikarthik | Medicodio (engine) | 4.8 | Needs Support | 7.0 | 4.0 | NR | 2.5 | NR | 4.5 | Low |
| ashwinsk-medicodio | Medicodio (engine) | 4.6 | Needs Support | 5.0 | 4.5 | NR | NR | NR | 4.0 | Low |
| avinash-codio | Medicodio (engine) | 4.3 | Needs Support | 6.0 | 3.5 | NR | 2.5 | NR | 5.0 | Medium |
| NandanDate-Medicodio | Medicodio (engine) | 4.0 | Needs Support | 5.0 | 4.0 | 2.0 | 2.5 | NR | 6.5 | High |
| sumedh-codio | Medicodio (integration) | 3.9 | Needs Support | 4.5 | NR | 2.0 | NR | NR | 5.0 | Medium |

Dimension means across scored members: **Delivery 7.0** (16 raters), **Rigor 6.0** (14), **Review 3.4** (6), **Devin 4.0** (12), **Automation 6.3** (11), **Consistency 6.4** (16).
Against the 08-28 cards (Delivery 7.3, Rigor 6.2, Review 3.6, Devin 5.4, Automation 5.9, Consistency 6.4): **Automation rose** (three de-duplication mechanisms landed or were designed in one window — the best showing in the collected history), **Devin leverage fell sharply** (0 trailer commits org-wide, from 49), and delivery, rigor, review and consistency are flat. Only six members produced any review artefact at all, and only one of those artefacts had content.

## Cards

### SaijyotiMeti — Global Codio — **8.0 (Strong)** — confidence High
- **Delivery 8.0** — 10 commits remediating svh-medicodio's checklist-visibility branch and merging it as #1256 (11 files, +831/−57) with the `dev` deployment green. Below 9 only because the window's authored scope was small.
- **Rigor 9.0** — routed the platform checklist-name lookup through the repository layer instead of patching the caller, ordered checklist groups by their own `sort_order`, extracted a shared grouping hook so the two web surfaces stop diverging, added the one API test commit that covers `NotFound` and HR-orphan branches, documented `checklistName` nullability and the always-null fields, and recorded four separate evidence passes (`/check` re-audit, `/fix` remediation, `/architect-review --advisory` — Verdict: SOUND, posted PR review with green gates).
- **Review 10.0** — the organisation's **only** substantive human review today: 5,697 characters of architect/EM review on #1256 plus 3 inline comments and an approval. The other 14 human review events org-wide totalled 41 characters between them.
- **Devin 5.0** — no delegation of her own; the two Devin Review findings on #1256 were followed by 9 commits before merge, which is active consumption rather than passive, but there is no delegated output to credit and 0 trailer commits.
- **Automation 6.0** — extracted the shared checklist-grouping hook (a real de-duplication) against five hand-written docs/review-log commits that her own 08-28 improvement said should be emitted by the gate runner.
- **Consistency 9.0** — 128 commits in the week, 431 in the month, and the third consecutive window in which she is the only source of architect-level review. That dependency is a team risk, not a mark against her.

### ragha82 — Global Codio — **7.5 (Solid)** — confidence Medium
- **Delivery 7.5** — landed exactly what the 08-28 report recommended: Devin-authored #1253 (Devin QA enablement — skill adapter, UI/interaction matrix, explicit hosted API origin; 18 files, +490/−10) merged at 21:15 with the Claude QA Validation run green. Also opened #1259 (19 files, +1,343/−188) with an RCA. Held at 7.5 because #1250 is open for a second window.
- **Rigor 7.0** — recorded the empty-extraction RCA and ADR-0028 alongside the fix, and Devin Review returned "No Issues Found" on #1259. Capped at 7.0 because he merged #1253 with **no independent human approval** recorded.
- **Review NR** — no review events in the window.
- **Devin 8.5** — the day's only completed delegation outcome, and it is *test infrastructure* rather than a feature: he is the one member using Devin to build mechanisms the whole team can stand on. Not 9+ because he also merged that output himself.
- **Automation 9.0** — the e2e QA enablement removes a class of repetitive work — the manual `qa update` cycles this repo absorbed on 08-24, 08-25 and 08-27 — for everyone, not just him.
- **Consistency 6.0** — 13 commits in the week, 31 in the month; sporadic in volume, but each appearance leaves a mechanism behind (CI gates and auto-merge-on-green on 08-21, e2e enablement today).

### anirudh-medicodio — Global Codio — **7.0 (Solid)** — confidence High
- **Delivery 8.5** — 24 commits hardening KB environment sync inside Devin PR #1244, plus the full release train landed (#1261 11 files, #1262 331 files, merged inside 8 minutes with five green production deploys).
- **Rigor 8.0** — recovered a sync session from the abandoned-MFA deadlock, refused an untransportable selection *before* spending an MFA code, refused an export whose rows share a natural key, scoped child tables through their parent's platform lane, fixed an untyped keyset-cursor binding, stamped audit timestamps the bundle cannot carry, added a preflight validation script, pinned ruff so the lint gate stops moving, and synced the LLD. Held below 9 by no test commit this window and one uninformative commit subject ("Implement code changes to enhance functionality and improve performance").
- **Review 2.5** — one review event: an **empty-body approval on #1254**, 320 files, bound for `uat` and then production. Down from 5.0 on 08-28 — the substance is in his commits, but the merge records nothing.
- **Devin 6.0** — the only member working inside a Devin-authored PR, and #1244's new finding was answered with 3 commits. But 0 Devin-trailer commits against 37 yesterday: authorship moved wholly to Claude while the delegable work (preflight matrix, bundle-integrity regressions) stayed on his hands.
- **Automation 7.0** — the preflight validation script and the ruff pin each remove a recurring failure, offset by three manual lockfile repairs and hand-written review logs.
- **Consistency 9.0** — 252 commits in the week, 794 in the month, with #1244 advancing in every window.

### akanksh-rv — Global Codio — **7.0 (Solid)** — confidence Medium
- **Delivery 8.5** — 23 commits and #1260 opened (152 files, +16,343/−1,807, 65 commits): AI-workforce assignment, handoff and supervision, one hub with a picker, URL-owned paging, snooze/resume. Substantial and coherent; not 9 because it arrives as one PR nobody can review in a sitting.
- **Rigor 8.0** — `fix(security): case access outranks AI ownership on every read, not most of them` is a real authorisation-precedence fix; he **restored the 33 tests deleted with the AI rewrite** (one of the day's two test commits org-wide), repaired the specs his own contract changes falsified, bounded a firm-wide read, added an audit timeline row for silent reassignment, made RBAC denials read as denials, ran the gates and recorded them green, and synced the PRD, endpoint map and Atlas with what shipped. Held below 9 by the 152-file shape and by 2 Devin Review findings left unanswered at window close.
- **Review NR** — no review events in the window; no evidence either way.
- **Devin 3.5** — no delegation, and Devin Review's findings on #1260 had no response inside the window. The RBAC matrix tests, endpoint-map generation and spec realignment he did by hand are textbook delegable work.
- **Automation 5.5** — aware but manual: five doc-sync commits and three spec-repair commits by hand; the review-log discipline exists but is typed.
- **Consistency 7.5** — 155 commits in the week and 421 in the month with 10 PRs merged, but this is his first window inside the report history, so the trend statements in his individual review are marked Insufficient Data.

### svh-medicodio — Global Codio — **6.7 (Mixed)** — confidence Medium
- **Delivery 8.0** — #1256 merged (checklist grouping before firm ownership) and #1258 opened (central case read-only policy, 24 files) in the same window; nothing stalled.
- **Rigor 7.0** — he published his own `/check` audit as **FAIL with 6 major findings, no tenancy leak** before review — the most honest pre-review artefact in the collected data — and moved from per-surface patches to a central policy. Held at 7.0 because 3 Devin Review findings on #1258 were unanswered at window close and there are no tests of his own.
- **Review NR** — no review events.
- **Devin 4.5** — no delegation; Devin Review findings on #1256 were closed by his reviewer, not by him, for the second consecutive window.
- **Automation 6.0** — the central read-only policy is exactly the right shape (one gate instead of N call-site checks); the per-service migration and its tests are still ahead of him.
- **Consistency 7.0** — 47 commits in the week, 204 in the month, with the self-audit habit now in two consecutive windows.

### sameer-s-mansur — Medicodio (integration) — **6.7 (Mixed)** — confidence High
- **Delivery 8.5** — 18 commits and 11 PRs merged, including the `Uat_1.0`→`release/prod_1.0` sync: per-format registration header tables designed and routed, payer casing matched case-insensitively, Ohio's blank-carrier payer fallthrough and HST's claim parsing fixed, two orphaned payer docstrings removed with the decision recorded.
- **Rigor 6.5** — the **snapshot-before-move sequence** (design commit → inert tables → snapshot current normaliser behaviour → route traffic) is the safest refactor anyone ran this week, and it is why he caught his own silent zero-import inside the same window rather than a client finding it. Capped at 6.5 by **zero tests** on a refactor touching three normalisers plus three client modules, and by 5 merges with no independent approver.
- **Review NR** — no review events.
- **Devin 3.0** — seventh consecutive window with no Devin evidence, while the per-format fixture suite his own design implies is the most obviously delegable test work in the Medicodio repos.
- **Automation 6.5** — the header-mapping tables turn per-client column fixes into data rather than code, which is a genuine class removal; against that, 6 of his 11 PRs were promotions on a 448-character template, flagged every day since 08-20.
- **Consistency 8.5** — 73 commits in the week, 199 in the month, 37 PRs merged in the week; the steadiest contributor in the collected data.

### Pj-Vineeth-Kumar — Global Codio — **5.9 (Mixed)** — confidence Medium
- **Delivery 6.5** — 4 commits and #1257 opened (File Number search, 16 files, +930/−34); nothing landed, and #1239 (169 files) has not moved since 08-27.
- **Rigor 6.5** — `fix(api/prisma): match a P2002 by its constraint name, not only its columns` is a genuine root-cause fix in unique-violation handling. No tests, and 1 Devin Review finding on #1257 was unanswered at window close.
- **Review NR** — no review events.
- **Devin 4.0** — 24 Devin-trailer commits in the week, none today, and his delegated PR #1239 is in a fourth window without a reviewer or a split, which is the exact 08-28 recommendation.
- **Automation 5.0** — File Number behaviour changed per surface across two windows (generation, then search plus labels) rather than once with tests.
- **Consistency 7.0** — 59 commits in the week, 166 in the month, PRD-first delivery still his normal shape.

### amit-pandey-medicodio — Medicodio (integration + app) — **5.8 (Mixed)** — confidence High
- **Delivery 8.0** — 18 commits closing 15 named review findings on the F35 prompt registry (#249, 55 files, 31 commits), an end-to-end dev QA run, four facilities re-baselined on `gemini-3.7-flash`, Trinity restored, plus two `Dev_1.0` merges for jatinkushwaha with green deploys. Capped because #249 is in its third window open.
- **Rigor 6.5** — QA evidence commits record the model the numbers were measured on and the facilities they cover — the best measurement hygiene in the Medicodio repos — and the exception hole, substitution boundary and growing cached failure were each closed explicitly. Still **no test commit**, and #249's own finding was answered only by subsequent commits.
- **Review 2.0** — 3 approvals, all empty bodies, including #591 which he merged while its 4-finding report stood.
- **Devin 3.0** — **38 Devin-trailer commits yesterday, 0 today.** The work he did instead — mechanically closing named findings and re-running per-facility QA — is the most delegable work in his repo.
- **Automation 7.0** — the prompt registry with its duplicate-section drift check genuinely removes repetitive prompt editing; the per-facility QA re-baseline was still done by hand for the second time this week.
- **Consistency 7.5** — 108 commits in the week, 300 in the month, with the mix shifting from promotions toward authored feature work with recorded QA.

### jatinkushwaha-medicodio — Medicodio (app) — **5.7 (Mixed)** — confidence High
- **Delivery 7.5** — #591 (7 files: Prometheus metrics, Loki transport with flush serialization) and #592 (4 files: environment tagging) both merged into `Dev_1.0` with green deploys.
- **Rigor 5.0** — the observability path now has metrics and a serialised log transport and **no tests at all**; #591 merged 23 minutes after a 4-finding report with one commit in between, #592 merged with 1 finding and no commit.
- **Review NR** — no review events.
- **Devin 3.0** — no Devin usage; label-cardinality and transport-failure tests are bounded, well-documented work that Devin does well.
- **Automation 6.0** — metrics and structured logging themselves reduce future manual debugging, which is real leverage; the same-window re-correction of env tagging (#591 → #592 in 90 minutes) is the repetition to remove.
- **Consistency 7.0** — 42 commits in the week, 141 in the month, 24 PRs merged in the week across both app repos.

### karthikmed — Shared (fork/tooling) — **5.3 (Mixed)** — confidence Low
- **Delivery 5.5** — one upstream-sync merge in `paperclip-ai`, with Sync-upstream and Refresh-Lockfile green, the 05:48 Docker and Release runs red, and a Release run green at 12:50 (Inference: retried or fixed).
- **Rigor NR** — no product change to assess.
- **Review NR** — no review events.
- **Devin NR** — no Devin evidence, and none obviously warranted for a workflow-driven sync.
- **Automation 6.0** — the fork tracks upstream through scheduled workflows rather than hand-merges; only failure triage is manual.
- **Consistency 4.0** — 3 commits in the week, 15 in the month; appears only at sync points. Scored on three dimensions, hence Low confidence.

### Amrutha-Beedikar — Global Codio — **5.2 (Mixed)** — confidence Medium
- **Delivery 7.5** — she ran the day's release end to end: #1254 (`dev`→`uat`, 320 files) merged with a green uat deploy, #1255 closed unmerged rather than forced, and the #1261/#1262 prod train merged at 22:05 with **five green production deploys** (Web, API, Worker, Automator, Scheduler).
- **Rigor 5.0** — the release was verified green in CI, which is the substantive control that did work. Against that, a 331-file production PR carries no recorded verification beyond the word "approved", and #1255's abandonment has no recorded rationale.
- **Review 2.0** — 2 approvals, both 8 characters, on prod-bound PRs of 11 and 331 files.
- **Devin NR** — no Devin evidence either way; nothing delegated, nothing discarded.
- **Automation 5.0** — deployment is fully workflow-driven and green (aware and automated), but the promotion bodies are hand-templated and the approval step carries no generated evidence.
- **Consistency 5.0** — 11 commits in the week, 50 in the month, concentrated in release windows; this is her first individually reviewed window, so no trend is asserted.

### vishnu-saikarthik — Medicodio (engine) — **4.8 (Needs Support)** — confidence Low
- **Delivery 7.0** — `fix(agentic_memory): drop parameter scalar filter that entirely blocked DXEX2 memory recall` unblocked the path ashwinsk-medicodio was extending the same morning — real dependency-clearing work — plus #413 (BMI trigger data) merged.
- **Rigor 4.0** — a prediction-affecting data change merged **75 seconds after a 2-finding Devin Review report**, on a 439-character template body, with no fixture and no test; the memory-recall filter removal is equally unpinned.
- **Review NR** — no review events.
- **Devin 2.5** — the findings report on his own PR was effectively discarded, the second consecutive window; the E66/Z68 fixtures recommended on 08-28 were not started.
- **Automation NR** — no automation evidence either way.
- **Consistency 4.5** — 3 commits in the week, 15 in the month, in short bursts; too little history to trend, hence Low confidence.

### ashwinsk-medicodio — Medicodio (engine) — **4.6 (Needs Support)** — confidence Low
- **Delivery 5.0** — 3 commits (DXEX 1/2 memory recall, extra internal-medicine parameters, DXEX2 dedup) — his largest recorded contribution, but pushed to a draft PR owned by someone else and open since 08-25, so nothing of his own reached a reviewable state for a fourth window.
- **Rigor 4.5** — the dedup work shows he is thinking about recall *quality*; against that, two of three commit subjects are terse ("added more paramters…") on pipeline-affecting code, and there are no tests.
- **Review NR** — no review events.
- **Devin NR** — no Devin evidence; scored NR rather than low, per the telemetry limitation.
- **Automation NR** — no evidence.
- **Consistency 4.0** — 3 today, 1 previous day, 5 in the week, 9 in the month — upward from a very low base. Scored on three dimensions, hence Low confidence.

### avinash-codio — Medicodio (engine) — **4.3 (Needs Support)** — confidence Medium
- **Delivery 6.0** — one commit and #412 (3 files: ortho config switching the DXEX model and enabling final-selection RAG) merged into `uat`.
- **Rigor 3.5** — a change to model selection and RAG behaviour in a clinical coding pipeline, merged **96 seconds after a 2-finding report**, on a 449-character template body, with no fixture evidence of effect. Third window with this shape.
- **Review NR** — no review events.
- **Devin 2.5** — findings discarded rather than answered; the routing-trigger fixture suite recommended on 08-28 was not started.
- **Automation NR** — no evidence.
- **Consistency 5.0** — 11 commits in the week, 74 in the month, 66 PRs opened in the month; the cadence is steady, the practice around it has not changed across the reported history.

### NandanDate-Medicodio — Medicodio (engine) — **4.0 (Needs Support)** — confidence High
- **Delivery 5.0** — his entire window is two merge commits: he unblocked #412 and #413 into `uat`, which has value as gatekeeping, but he authored no feature work, tests or docs (down from 19 commits and two landed features on 08-27).
- **Rigor 4.0** — he merged #412 **96 seconds** and #413 **75 seconds** after their 2-finding Devin Review reports, with no commit in between; these are model-selection, RAG and BMI-trigger changes in a clinical pipeline.
- **Review 2.0** — 2 approvals, bodies "okay " and "okay".
- **Devin 2.5** — his first Devin PR (#405) has not moved since 08-27 and is still a draft; today's findings were discarded twice.
- **Automation NR** — no evidence.
- **Consistency 6.5** — 33 commits in the week, 129 in the month with authored features in most windows, and he is reliably available as the engine's non-author approver — which is precisely why the approval artefact matters so much in his case.
- *This score reflects one window in which his contribution was gatekeeping and the gate did not hold. His 08-28 delivery (5.6 overall) shows the capability is there.*

### sumedh-codio — Medicodio (integration) — **3.9 (Needs Support)** — confidence Medium
- **Delivery 4.5** — 4 commits, all merge commits of the promotion PRs he approved; no authored change.
- **Rigor NR** — no authored change to assess.
- **Review 2.0** — 5 approvals, **every one with an empty body**, including #261 (`Uat_1.0`→`release/prod_1.0`, 12 files, +1,787/−97) which carried an open Devin Review finding. Second consecutive window of this pattern (6 empty approvals on 08-28).
- **Devin NR** — no Devin evidence either way.
- **Automation NR** — no evidence.
- **Consistency 5.0** — 11 commits in the week and month, all merge commits; he is consistently available as the non-author approver on the integration train, which is the reason most of sameer-s-mansur's promotions are not self-merged.
- *Recommendation: the fastest score change available to anyone in this report — a three-line verdict (range checked / findings status / rollback point) on each approval would move Review from 2 to 7 without changing his workload.*

## How to read the spread

**Observed Fact.** The spread is 3.9 to 8.0 with a median of 5.8, and it is not driven by output volume. The two highest scores belong to a member with 10 commits (SaijyotiMeti) and a member with 4 (ragha82); the member with the most commits in the window (anirudh-medicodio, 24) sits at 7.0, held down by a single empty approval on a 320-file prod-bound PR. Conversely, the four lowest scores are not low-output people: avinash-codio opened 66 PRs this month and NandanDate-Medicodio authored 19 commits the previous day. What separates the bands today is **verification and review artefacts**, not throughput: Review averages 3.4 across the six members who produced any review event, and Devin Leverage averages 4.0 on a day when the organisation produced zero Devin-authored commits.

**Inference.** Two structural effects, not personal ones, explain most of the spread. First, the **engine repository's merge culture** — approve with "okay", merge within two minutes of a findings report, ship prediction-affecting config with no fixture — puts three of its four active members in the Needs Support band regardless of their individual care; the same people score materially better in windows where they author features. Second, **Devin is placed on features rather than on verification**: the day's delegation produced one QA mechanism (ragha82) and nothing else, while every test suite that would have raised Rigor scores across Medicodio remained undone. A low Devin score in this report almost never means "used Devin badly" — it means the highest-leverage delegable work was carried by hand, and with session telemetry unavailable we cannot see whether sessions were attempted and abandoned.

**Recommendation.** Do not manage to these numbers person by person. Three mechanism changes would move most of the grid in one window: (1) block merge while a Devin Review report is unanswered — this alone addresses NandanDate-Medicodio, avinash-codio, vishnu-saikarthik and jatinkushwaha-medicodio; (2) require a non-empty approval body on protected branches, using SaijyotiMeti's three-line verdict — this addresses sumedh-codio, Amrutha-Beedikar, amit-pandey-medicodio and anirudh-medicodio's only weak column; (3) delegate one test suite per Medicodio repository to Devin, which is simultaneously the Rigor fix and the Devin-leverage fix. Individually, the single highest-value coaching conversation is with **amit-pandey-medicodio and anirudh-medicodio** — the two members who demonstrated the best delegation in the org yesterday and did none today — and the practice to institutionalise is **SaijyotiMeti's review template**, so that the organisation's review floor stops being one person's calendar.

---
*MediCodio AI © 2026. All Rights Reserved — www.medicodio.ai*
