# Employee Rating Cards — 2026-09-06

**Review window:** Saturday 2026-09-05 03:00 UTC → Sunday 2026-09-06 03:00 UTC. Comparison windows: previous day (09-04 → 09-05), week (08-29 → 09-05), month (08-06 → 09-05). Companion to `2026_09_06_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **Devin session telemetry is unavailable.** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing) for the 14th consecutive run. "Observable Devin Leverage" is scored only from GitHub artefacts: Devin Review findings and how they were dispositioned, `devin-ai-integration[bot]` QA-gate comments, and commit trailers. Prompt quality, scoping, ACU effort and correction loops cannot be assessed.
- **Weekend window.** Only two people (both Global Codio) had observed activity; every Medicodio member and six Global Codio members are **NR** on all dimensions. Do not compare today's means with weekday cards.
- **Attribution gap.** 14 commits were authored as `Claude <noreply@anthropic.com>` with no human identity. They are excluded from both members' evidence; where context makes the owner likely (a reviewer's own comment claiming the fix) this is stated as Inference and does not raise a score.
- **Jira and Sentry** were not available; ticket flow and incident load are unscored.
- **Volume is not productivity.** Commit, file, PR and finding counts appear only as context. Two very large PRs merged today count against Rigor, not for Delivery.
- A dimension with no in-window evidence is **NR** and excluded from the weighted average; fewer than three rated dimensions → overall **NR**.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure; loose ends accumulate | Stalled or abandoned work; commitments not met |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR too large to review | Template body, no tests, inaccurate claims, findings ignored |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence, or substantive but non-independent | Empty/one-word approvals; rubber-stamping |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed | Findings ignored; Devin used where manual is faster |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| akanksh-rv | Global Codio | **7.1** | Solid | 7.5 | 7.0 | 7.5 | 8.0 | 5.0 | 6.5 | Medium |
| SaijyotiMeti | Global Codio | **6.3** | Mixed | 7.0 | 5.5 | 7.0 | 6.0 | 5.0 | 7.0 | Medium |
| ragha82, svh-medicodio, SaahilVishwakarma, anirudh-medicodio, Pj-Vineeth-Kumar, Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, weekend) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, ashwinsk-medicodio, vishnu-saikarthik, afifashaikh007, Medicodio-Amit, sameer-s-mansur, avinash-codio, nandanchouhan-medicodio, sumedh-medicodio, Karthik Khatavkar, hitesh-medicodio, shaheen-medicodio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, weekend) |

Weighted overall = Σ(score × weight) / Σ(weights of rated dimensions).

## akanksh-rv — Global Codio — Overall 7.1 (Solid) — Confidence: Medium

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#1317` (support-letter chase + letter groups) opened 03:19 and merged 19:37; drove `#1305` and `#1318` to merge with 57 commits. Loose ends: nine "your call" decision items left open in his own reviews at merge; QA gate produced no verdict on either merge he performed. |
| Engineering Rigor | 7.0 | 13 test commits; PRD decision log, HLD and `database_info.md` corrected; fixes name the defect class (tenancy, PII, atomicity, RBAC, retry). Against: `#1317` is 199 files / +25.6k in one PR (fourth > 100-file PR this month); two `dev` merges required repair, one had silently reverted live `dev` fixes. |
| Code Review Contribution | 7.5 | Two architect reviews (9.7k and 8.3k chars, 10 inline) verified against `schema.prisma`/`pg_indexes` with a Stop-and-Check table — the deepest reviews observed in the org this month. Capped below 8 because he approved and merged PRs on which he had just authored 25/25 and 32/32 in-window commits, and approved with his own open items. |
| Observable Devin Leverage | 8.0 | Written disposition of all 15 Devin comments on `#1318` (10 fixed, 3 rejected with reasons, 2 out of scope); credited Devin for `ab7e2dfb6`; cited Devin finding IDs as open decisions. No Devin authoring (session data unavailable). Not 9–10: the mechanical remediations he did by hand on others' branches are Devin-class work. |
| Automation of Repetitive Work | 5.0 | Header backfill (3), review-log (4), spec-realignment (5) and `dev`-merge-repair (2) commits repeated from 09-04; no automation attempted. |
| Consistency Across Windows | 6.5 | Day Improved (reviews given, findings dispositioned); week Stable; month Needs Improvement on PR size (documented 08-30, 09-02, 09-04). |

Inference: the 04:33–04:59 `Claude`-identity commits on his branch are likely his Claude Code session; not counted. Confidence Medium because of this gap and missing session telemetry.

## SaijyotiMeti — Global Codio — Overall 6.3 (Mixed) — Confidence: Medium

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.0 | `#1305` (open since 09-03, idle 48 h per the 09-05 report) and `#1318` both merged today; 15 own fix/test commits. The merges depended on 57 reviewer-authored commits; four decisions on `#1305` remain hers and are open. |
| Engineering Rigor | 5.5 | Regression tests shipped with her `#1317` blocker fix; standards-audit log maintained. Against: the `#1305` body's "Tests green — 39 gates" claim was disproved (six specs mocked `findUnique` while code calls `findFirst`), two further claims were untrue, and `#1305` merged at 115 files (third 100+-file PR). |
| Code Review Contribution | 7.0 | `#1317` architect review (7.1k chars) found a real correctness blocker (approvers never chased) and a major fan-out, with a Stop-and-Check table; adjudicated a Devin comment as false positive with reasoning. Capped because she fixed the blocker herself and then approved (fifth such instance since 09-03). |
| Observable Devin Leverage | 6.0 | Reasoned disposition of one Devin finding on `#1317`; but the 39 Devin findings on her two PRs were resolved by the reviewer's commits, not hers, and no Devin delegation is observable. |
| Automation of Repetitive Work | 5.0 | Four mock/fixture/registry-drift repair commits today after similar ones on 09-03; repetition acknowledged in commit messages, not addressed. |
| Consistency Across Windows | 7.0 | Day Improved from Regressed; week Stable (most reviews in Global Codio, 4 substantive); month Consistent as a top-three contributor and reviewer. |

Inference: the 18:17–18:34 `Claude`-identity commits (including the blocker fix) are hers per her own comment; not counted toward scores. Confidence Medium.

## Members with no in-window evidence — NR

Global Codio: ragha82, svh-medicodio, SaahilVishwakarma, anirudh-medicodio, Pj-Vineeth-Kumar, Amrutha-Beedikar. Medicodio: amit-pandey-medicodio, jatinkushwaha-medicodio, ashwinsk-medicodio, vishnu-saikarthik, afifashaikh007, Medicodio-Amit, sameer-s-mansur, avinash-codio, nandanchouhan-medicodio, sumedh-medicodio, Karthik Khatavkar, hitesh-medicodio, shaheen-medicodio. Saturday window; no dimension has evidence, so no card is scored. Their 09-05 cards remain the latest weekday assessment.

## How to read the spread

- **Observed Fact:** Two members scored, both Global Codio, both on a weekend day in which they merged three feature PRs to `dev` by reviewing and remediating each other's branches. Review depth was the highest recorded this month; review independence was the lowest. Fourteen commits are unattributable to either person.
- **Inference:** akanksh-rv's higher score reflects review depth and the first complete Devin-finding disposition, not the 64-commit volume; SaijyotiMeti's Rigor score is held down by a PR body whose test claims did not survive verification, not by the size of her contribution. Both scores would move with session telemetry and correct git identities.
- **Recommendation:** Treat these two cards as a weekend snapshot, not a ranking against the 09-05 weekday cohort. Management's highest-leverage moves are outside the individuals: a second-approver rule for `dev`, resetting the `E2E_SUPERADMIN` QA-gate credential, granting `org.sessions.view`, and making `Mgmt_Reports` private.
