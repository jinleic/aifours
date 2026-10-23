# SUN7-COMP-erratum-v2 — mandatory gate-status overlay after the parent computation-gate ruling (no mathematical change)

- **Written:** `/bin/date` read at 2026-10-19T16:40:40-0700, immediately before this exclusive write. Owner SunM13MixedFibres. Applies to
  `SUN7-COMP-v1.md` (98796f95bf2faa7f0530ad9d4d999817fb5234d89ea09ea35eb232f2954913d7) after `SUN7-COMP-erratum-v1.md` (be365c34f1c7ed6c81472edbeb407ddd535c477a6a4602c398c1b2eb1fa06778); both stay byte-identical.
- **Input (factual update, no promotion):** parent ruling `RUN/control/sun7-full-result-computation-gate-ruling-v1.json`,
  sha256 4818f1ca96c99e012d758e165982ec0844228eae07ff3f38b95dc2b7a3a5eada (recorded 2026-10-19T16:37:41-0700): two separately written exact certificate checkers are required for
  EVERY computation still load-bearing in the full Sun(7) composition, including the accepted Sun(5)/Sun(6) imports; no
  waiver; accepted import statuses remain valid historically and at their scoped verdicts. Per the parent's IRC, the gate
  audits found exactly one qualified checker each for StageB (K5.2*/KII), Sun(5) and Sun(6), the Sun(6) auxiliary route
  being unqualified. RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

| # | location in SUN7-COMP-v1.md | replacement |
|---|---|---|
| Q1 | line 142 (gate G4) | **G4 — UNMET in all three components.** Requirement (ruling above, from contract line 46): two independently written qualified exact checkers, or an accepted written replacement, for every load-bearing computation. C1 StageB (K5.2* incl. D2', KII): UNMET, one qualified checker. N2 Sun(5): UNMET, one qualified checker. N3 Sun(6): UNMET, one qualified checker (auxiliary route unqualified). K5.3 is NOT a gap (accepted written X1, C2). |
| Q2 | lines 150-152 (section 8, outstanding obligations) | ... and G4 in all three components: a second qualified independent checker or an accepted written replacement for (i) StageB K5.2*/KII, (ii) Sun(5), (iii) Sun(6). G5 (F-1) stays a permanent disclosed deviation. |
| Q3 | section 6, after line 131 | Gate status of the three load-bearing computer-assisted nodes N2, N3, C1: each UNMET (one qualified checker; ruling above). |
| Q4 | lines 87-89 (reading note, not a statement change) | Theorem SUN7-COMP stays CONDITIONAL. Even if (H-NF) and (H-A2X) were accepted, no full Sun(7) acceptance follows while G4 is UNMET; the accepted scoped verdicts of N2, N3, C1 are unchanged. |

Unchanged: every mathematical statement, proof, hypothesis, case split, DAG edge and status (ACC/NEW) of SUN7-COMP-v1.md.
No full Sun(7), acceptance, novelty, Lean or human-review claim. No scientific computation; metadata only.
