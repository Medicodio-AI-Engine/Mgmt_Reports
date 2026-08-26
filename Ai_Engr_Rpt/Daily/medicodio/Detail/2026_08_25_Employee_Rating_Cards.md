# Employee Rating Cards — 2026-08-25 (Tuesday, UTC)

Companion to `2026_08_25_Mgmt_Activity_Report.md`. Review window 2026-08-25 03:00 → 2026-08-26 03:00 UTC.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable** (`org.sessions.view` denied, 7th consecutive run). "Observable Devin Leverage" is scored from Git evidence only: `Co-Authored-By: Devin AI` trailers, Devin-authored branches/PRs, and whether Devin Review findings were consumed. A member who used Devin productively without producing a commit scores **NR** here, not low.
- **Jira is not queryable.** Coordination, requirement quality and ticket hygiene are outside the evidence base.
- **This was an unusually quiet day** (14 default-branch commits org-wide vs 193 on 08-24), and Global Codio landed nothing on `dev`. Several members appear with 1–2 evidence points; their cards carry **Low** confidence and should not be trended against a normal weekday.
- **Volume is not productivity.** Commit, PR and review counts are used only as evidence of *what kind* of work happened. A day of one careful config change can outscore a day of twelve self-merged PRs, and does here.
- Members with **no observed activity** in the window are not scored at all (absence is not a signal): akanksh-rv, anirudh-medicodio, SaijyotiMeti, ragha82, Amrutha-Beedikar, shaheen-khan11, Shashvi1.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| Delivery & Follow-Through | 25 | Work stalls or does not reach a reviewable state | Work progresses; landing is uneven | Meaningful work reaches a reviewable/landed state the same day | Substantial scoped delivery, closed out end to end |
| Engineering Rigor | 25 | No tests/docs; unsafe or unreviewable changes | Some care; gaps in tests, docs or risk handling | Tests/docs/risk handled proportionally to blast radius | Risk named, rollback stated, invariants defended, evidence attached |
| Code Review Contribution | 15 | Approvals with no content | One-line reviews on low-risk changes | Specific, evidenced review with a verdict | Architect-level review that changes the outcome |
| Observable Devin Leverage | 15 | Devin signal ignored or discarded | Devin Review consumed passively | Devin delegated on well-scoped work; findings closed | Devin used where leverage is highest, with acceptance criteria and review of output |
| Automation of Repetitive Work | 10 | Repeats manual work already flagged | Aware but manual | Automates or scripts a repeated task | Removes a class of repetitive work for the team |
| Consistency Across Windows | 10 | Erratic; no pattern | Sporadic contribution | Steady across day/week/month | Steady and improving across all windows |

Weighted average of rated dimensions only; **NR** dimensions are excluded and the weights renormalized. Fewer than three rated dimensions → overall **NR**. Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**.

## Summary grid

| Member | Product | Overall | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| ------ | ------- | ------- | ---- | -------- | ----- | ------ | ----- | ---------- | ----------- | ---------- |
| Pj-Vineeth-Kumar | Global Codio | 7.9 | Solid | 7.5 | 8.0 | NR | 9.0 | 7.0 | 8.0 | Medium |
| svh-medicodio | Global Codio | 6.5 | Mixed | 7.0 | 8.0 | NR | 4.0 | 5.0 | 7.0 | Medium |
| hiteshjrxmedicodio | Medicodio (app) | 5.9 | Mixed | 7.0 | 6.0 | NR | 4.0 | NR | 6.0 | Medium |
| ANANYANG8055 | Medicodio (engine) | 5.7 | Mixed | 6.5 | 6.0 | NR | 5.0 | NR | 4.0 | Low |
| Medicodio-Amit | Medicodio (engine) | 5.7 | Mixed | 6.0 | 6.0 | NR | 4.0 | NR | 7.0 | Low |
| sameer-s-mansur | Medicodio (integration) | 5.6 | Mixed | 8.0 | 4.0 | NR | 3.0 | 6.0 | 7.0 | High |
| jatinkushwaha-medicodio | Medicodio (app) | 5.1 | Mixed | 7.0 | 5.0 | 3.0 | 3.0 | NR | 7.0 | High |
| avinash-codio | Medicodio (engine) | 4.8 | Needs Support | 5.0 | 5.0 | NR | NR | NR | 4.0 | Low |
| ashwinsk-medicodio | Medicodio (engine) | 4.8 | Needs Support | 5.0 | 5.0 | NR | NR | NR | 4.0 | Low |
| karthikmed | Medicodio (app) | 4.6 | Needs Support | 5.5 | 5.0 | NR | 3.0 | NR | 4.0 | Low |
| NandanDate-Medicodio | Medicodio (engine) | 4.2 | Needs Support | 5.0 | 4.0 | 2.0 | NR | NR | 6.0 | Medium |
| amit-pandey-medicodio | Medicodio (app) | 4.1 | Needs Support | 5.0 | 4.0 | 2.0 | NR | NR | 5.0 | Medium |
| Murali-Shetty19 | Medicodio (engine) | 4.0 | Needs Support | 4.5 | 4.0 | NR | 3.0 | NR | 4.0 | Low |
| vishnu-saikarthik | Medicodio (engine) | 3.8 | Needs Support | 4.0 | 3.5 | NR | NR | NR | 4.0 | Low |
| SaahilVishwakarma | Global Codio | NR | — | 4.0 | NR | NR | NR | NR | 5.0 | Low |

Dimension means across rated members: Delivery 5.8, Rigor 5.3, Review 2.3 (3 raters), Devin 4.2 (8 raters), Automation 6.0 (3 raters), Consistency 5.5.

## Cards

### Pj-Vineeth-Kumar — Global Codio — **7.9 (Solid)** — confidence Medium
- **Delivery 7.5** — PR #1239: HR Reports hub + 8 reports, 155 files, +21,971/−413, 15 commits in one day, opened for review the same day. Not yet merged or reviewed, which caps this below 8.
- **Rigor 8.0** — Template-complete PR body: reuse-before-creation evidence naming five extended files, itemised cleanup, named risk with a rollback path, additive migration deliberately **not executed**, and H-1B consumed time rendered banded because the source table records stints rather than presence. Six runtime SQL defects were found and fixed inside the PR; a query test suite would have caught them earlier.
- **Review NR** — gave no reviews in the window.
- **Devin 9.0** — 14 Devin-trailer commits; 7 Devin Review passes (15 findings) all answered with pushed fixes in-session. The clearest example this month of Devin used where leverage is highest, against a written PRD.
- **Automation 7.0** — the catalog-driven design (`hr-reports-catalog.ts` as the single source of tabs/params) removes per-report branching for everyone who adds a report next.
- **Consistency 8.0** — 48 commits in the week, 143 in the month, moving from QA-fix batches to owning a product slate.

### svh-medicodio — Global Codio — **6.5 (Mixed)** — confidence Medium
- **Delivery 7.0** — 13 substantial commits on #1238, but the PR is at 171 files on day 2 and nothing landed.
- **Rigor 8.0** — TOCTOU race closed with a database unique index, audit trail added for checklist writes, god-service split into 6 services, oversized component split, `database_info.md`/PRD/standards log synced in the same commits, and the quality gate actually run and its failures closed.
- **Review NR** — no reviews given.
- **Devin 4.0** — Claude-assisted throughout; the 4 Devin Review findings raised on #1238 on 08-24 are not visibly answered in-thread.
- **Automation 5.0** — ran and transcribed the gate by hand rather than dispatching the repo's existing CI workflow.
- **Consistency 7.0** — 44 commits in the week, 232 in the month, same rigor profile each active day.

### hiteshjrxmedicodio — Medicodio (app) — **5.9 (Mixed)** — confidence Medium
- **Delivery 7.0** — two PRs opened (#499 15 files, #500 38 files), both coherent and self-described; neither reviewed or merged.
- **Rigor 6.0** — added a jsdom ResizeObserver polyfill (the only test-infrastructure work in the org today) and extracted a shared `StageHeading` instead of copying chrome; but a 38-file refactor and a 15-file behaviour fix were opened with no reviewer requested.
- **Review NR** — none given.
- **Devin 4.0** — Devin Review raised one finding per PR; both open at end of window.
- **Automation NR** — no automation evidence either way in the window.
- **Consistency 6.0** — 71 commits in the week (via `hitesh.ms@` alias), 84 in the month; the 08-24 duplicate-PR pattern did not recur today.

### ANANYANG8055 — Medicodio (engine) — **5.7 (Mixed)** — confidence Low
- **Delivery 6.5** — #394 client-config tuning (pain-management CPT selection, gastro screening provider) opened, reviewed and merged to `uat` in 18 minutes.
- **Rigor 6.0** — small, single-purpose, conventional-commit change; no verification evidence attached for a change that alters coding behaviour.
- **Review NR** — none given. **Automation NR.**
- **Devin 5.0** — Devin Review ran and returned the only clean pass of the day; consumed passively.
- **Consistency 4.0** — 1 commit in the week window, 10 in the month; sparse and irregular.

### Medicodio-Amit — Medicodio (engine) — **5.7 (Mixed)** — confidence Low
- **Delivery 6.0** — draft #393 opened: episodic coder-correction memory recall for ICD routing, 32 files, +2,355.
- **Rigor 6.0** — substantial feature arriving as a single squashed commit in a repo whose gate/ceiling invariants make per-stage review important; no acceptance criteria in the body.
- **Review NR** — none given. **Automation NR.**
- **Devin 4.0** — Claude-assisted; no Devin delegation today, though he patched Devin Review findings via #389 on 08-24.
- **Consistency 7.0** — 18 commits in the week, 75 in the month, feature-sized contribution on each active day.

### sameer-s-mansur — Medicodio (integration) — **5.6 (Mixed)** — confidence High
- **Delivery 8.0** — 11 PRs opened, 9 merged: four Valley KB defect fixes, three prod hotfix pairs, two uat syncs, plus a 20-file prod→uat migration-trigger feature started.
- **Rigor 4.0** — four PRs self-merged 8–17 seconds after opening; two prod-branch hotfixes approved with `lgtm` inside 2 minutes; duplicate PR #232 opened and closed in 12 s; no tests visible on the migration trigger. Titles and commit messages are genuinely good, which is what keeps this from being lower.
- **Review NR** — gave no reviews.
- **Devin 3.0** — Devin Review commented on all eight of his PRs (15 findings); none addressed, and four merged before the pass finished.
- **Automation 6.0** — #241 is real automation work (post-run env migration, explicit source env), but the promotion fan-out he repeats daily is still hand-cut.
- **Consistency 7.0** — 58 commits in the week, 169 in the month; delivery reliably high, rigor reliably the gap.

### jatinkushwaha-medicodio — Medicodio (app) — **5.1 (Mixed)** — confidence High
- **Delivery 7.0** — #576 (modifier search) and #498 (23-file CSS/font refactor) both merged the same day.
- **Rigor 5.0** — exact conventional commits, but a 23-file styling refactor with no visual/regression evidence and an open Devin Review finding.
- **Review 3.0** — 6 approvals, every one with the body `lgtm`, including two `release/prod_1.0` hotfixes approved within 2 minutes of opening.
- **Devin 3.0** — no delegation; the Devin Review finding on his own PR is unaddressed.
- **Automation NR** — the dev→uat sync PRs he repeats weekly are still manual, but none fell in this window.
- **Consistency 7.0** — 50 commits in the week, 110 in the month.

### avinash-codio — Medicodio (engine) — **4.8 (Needs Support)** — confidence Low
- **Delivery 5.0** — a real registry-level refactor (bind rules by `rule_name`, not guideline id; blank `seq_number` sorts last; three mislabelled ids, a broken import and four undiscovered specialty modules fixed) — but it sits on `feat/guideline` with no PR.
- **Rigor 5.0** — excellent commit body on the refactor and it moves the code toward the repo's no-hardcoding rule; the same branch also carries "claim split prompt handle from db driven and seed files was changes shown before u push", which is not a usable history entry, and there is no test for the discovery defects he fixed four times.
- **Review / Devin / Automation NR.**
- **Consistency 4.0** — 17 commits in the week, 70 in the month, in bursts.

### ashwinsk-medicodio — Medicodio (engine) — **4.8 (Needs Support)** — confidence Low
- **Delivery 5.0** — `feat(engine): structured-output JSON-schema support` plus a hand-merge, on a shared branch with no PR.
- **Rigor 5.0** — the change strengthens the engine's JSON-contract invariant, but ships with no test and no PR target for gates.
- **Review / Devin / Automation NR.**
- **Consistency 4.0** — 3 commits in the week, 4 in the month.

### karthikmed — Medicodio (app) — **4.6 (Needs Support)** — confidence Low
- **Delivery 5.5** — two commits (billing on the client record; cross-client billing summaries) across react and nodejs, both on another member's branch dating from 08-07, no PR.
- **Rigor 5.0** — outcome-oriented commit messages; no PR, no review target, no tests.
- **Review / Automation NR.**
- **Devin 3.0** — Claude-assisted; no Devin signal consumed.
- **Consistency 4.0** — 1 commit in the week window, 6 in the month.

### NandanDate-Medicodio — Medicodio (engine) — **4.2 (Needs Support)** — confidence Medium
- **Delivery 5.0** — one merge (#394 to `uat`); no authored work.
- **Rigor 4.0** — merged a coding-behaviour config change with no verification recorded; the engine's known-red baseline means a diff read cannot distinguish regression from baseline.
- **Review 2.0** — his single review was the body `okay` — the same pattern flagged in the 08-20, 08-21 and 08-24 reports.
- **Devin / Automation NR.**
- **Consistency 6.0** — 41 commits in the week, 122 in the month; steady as the `uat` gatekeeper.

### amit-pandey-medicodio — Medicodio (app) — **4.1 (Needs Support)** — confidence Medium
- **Delivery 5.0** — merged #576 and #498 into `Dev_1.0`; no authored change in the window.
- **Rigor 4.0** — he was the sole gate on both and left no record of what he checked.
- **Review 2.0** — 2 of 2 approvals had an empty body (17 the same way on 08-24).
- **Devin / Automation NR** — no Devin evidence this week; the 17 Devin-trailer commits under `amit.p@` were on 08-21.
- **Consistency 5.0** — 48 commits in the week, 224 in the month, but review depth flat across every window.

### Murali-Shetty19 — Medicodio (engine) — **4.0 (Needs Support)** — confidence Low
- **Delivery 4.5** — one DXEX memory/observation-consolidation commit on a shared branch; his PR #382 has been open since 08-21 with the title "Testing ortho".
- **Rigor 4.0** — conventional commit format, but a 24-file PR with a placeholder title, no body and three new unanswered Devin Review findings.
- **Review NR. Automation NR.**
- **Devin 3.0** — Devin Review findings raised today and ignored.
- **Consistency 4.0** — no default-branch commits in the week window; work stays branch-local.

### vishnu-saikarthik — Medicodio (engine) — **3.8 (Needs Support)** — confidence Low
- **Delivery 4.0** — one commit ("icd-memory-agent updated to handle in better way"); no PR, nothing on a default branch.
- **Rigor 3.5** — the commit message does not state what changed; an agent-behaviour change with no test or doc.
- **Review / Devin / Automation NR.**
- **Consistency 4.0** — 3 commits in the week, 13 in the month, mostly branch-local.

### SaahilVishwakarma — Global Codio — **NR** — confidence Low
- **Delivery 4.0** — no code; two well-documented defect issues filed (#1240 email pre-fill with a cache hypothesis, #1241 questionnaire-import performance), both with screenshots.
- **Rigor / Review / Devin / Automation NR** — no in-window evidence.
- **Consistency 5.0** — 49 commits in the week, 113 in the month; nothing landed since 08-24.
- **Overall NR** by rule: fewer than three rated dimensions. A QA/triage day is not a low-performance day, and scoring it as one would be wrong.

## How to read the spread

**Observed Fact.** The rated spread runs 3.8 to 7.9 with a median of 4.8, and the collapse is concentrated in two dimensions: Review averages 2.3 across the three people who reviewed anything (all nine human review events of the day were `lgtm`, empty, or `okay`), and Devin averages 4.2 with a single outlier at 9.0. Delivery, by contrast, is broadly healthy — twelve of fifteen members produced work that a reviewer could act on. Global Codio landed nothing on `dev`; Medicodio integration produced 11 of the day's 18 PRs.

**Inference.** The low overall scores today are mostly a *scrutiny* signal, not an *effort* signal. On a day with 90% less landed volume than Monday, the review record got worse rather than better, which suggests the review depth seen on 08-23 (full Architect+EM write-ups) depends on two specific people being present rather than on a shared standard. Second inference: the one high card is high because the work was scoped against a written PRD before delegation — #1239's quality tracks its inputs, not the tool. Third: several 4.x cards are low-confidence artefacts of a quiet window plus work that never reached a PR; three shared long-lived branches (`phrase-semantical-matching`, `hitesh/invoicing-billing-suite-20260807`, `feat/guideline`) hold real engineering that neither CI nor review nor these cards can see properly.

**Recommendation.** Fix the two structural causes rather than coaching individuals. (1) Require one non-author approval on `import_main` and `release/prod_1.0` and adopt a 3-line review template (checked / not checked / verdict) — that single change addresses the lowest dimension for jatinkushwaha, amit-pandey, NandanDate and sameer simultaneously. (2) Require a draft PR at first push on any shared branch, so branch-local work becomes reviewable and gate-able — that raises the evidence base for avinash, ashwinsk, karthikmed, Murali and vishnu, whose cards are currently limited by visibility as much as by practice. Do not trend these numbers against a normal weekday: this window is one quiet Tuesday, and the low-confidence cards should be re-read after 08-26.
