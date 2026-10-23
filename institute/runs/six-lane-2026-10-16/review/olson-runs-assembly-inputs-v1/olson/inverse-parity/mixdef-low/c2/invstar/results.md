# INV*b-rig attack: results and exact unresolved part

Owner OlsonParity2.  Written after host clock 2026-10-17T19:34:34-07:00.  All written lemmas here are UNREVIEWED.
No claim of INV*(p), INV*b-rig(p) for general p, or ordered Olson.  p >= 5 throughout; p = 3 stays separate.
All paths below are relative to c2/invstar/.

## 1. Written progress [W]

* proof-GR0-r1.md (205ee0c7...4964; supersedes proof-GR0.md): Lemma AR (all-reflection words of length 4p-2 are
  solvable by EGZ on adjacent reflection pairs); Lemma GR0 (GR's exact criterion permits EMPTY rotation runs);
  Corollaries WAS0, H0, MP0 (pair removal and even-block merging); Lemma NF (a generalised avoider with a genuine
  empty run reduces to one whose rotation runs are empty/pure/(1,1), and every even reflection block is adjacent
  to ALL the empty runs).  Reduces INV*b-rig(p) to exclusion of such normal forms with theta_i != 0 at empty runs.
* proof-sharpness.md (20bcdde7...d3c2): for every prime p >= 5,
      sigma_(v-2) rho_1^(2p-3) sigma_v^(2p-1)
  is a rigid-rotation non-RGR avoider of length 4p-3.  This is NOT a counterexample at the target length 4p-2 or
  at the ordered-Olson length 4p-1.  Three natural one-letter extensions (extra rho_1, sigma_v, or sigma_(v-2))
  all have explicit identity 2p-subwords.  No literature/novelty claim.

## 2. Controls, separate by checker [F]

* gr0_check.py: Lemma GR0 criterion from the unchanged code/gr_window.py versus the raw ordered-product DP of
  unchanged code/was_verify.py: 2,400 seeded random words, p = 5,7, lengths 4p-3,4p-2,4p-1, k <= 7; 2,108 had
  empty rotation runs; 0 disagreements.  The six DP-NO cases include positive controls; none is a genuine non-RGR
  avoider at length 4p-2 (the p=7,N=26 case is rho_1^13 sigma_3^13).
* gwas_verify_r1.py (asserted expectations): all 237 genuine-empty-run candidates printed by the p=5,N=17 search
  are raw-DP avoiders; all 400 printed candidates from the MUT=1 p=5,N=18 search contain identity 10-subwords,
  so every one is rejected.  The mutation deletes the top element of every nonempty Ach window; it weakens the
  forbidden sets.  There are 65,536 mutant candidates in total; ONLY the first 400 printed ones were DP-checked.
  Earlier gwas_verify.py printed an unused rgr_after_merge field; no claim uses that field; r1 removes it and
  asserts the actual expectation (out/gwas_controls_verified.jsonl).
* sharpness_check.py: raw DP, no GR/GR0/WAS formulas: p = 5,7,11,13,17,19,23,29,31, v = 0,1,p-1; 27 avoiders
  and their three extensions, 108 total checks, 0 failures (out/sharpness_check.json).  These extension controls
  are distinct from the window-shrinking mutation above.

## 3. Exact searches [W+F], code fidelity unreviewed

The search gwas.cpp enumerates rotation-canonical triples (a_i,b_i,l_i), A >= B by the v -> -v automorphism,
with at least one empty rotation run, and every theta (sum theta = 0, theta_i != 0 at empty runs), checked against
EVERY subset pattern's GR0 window.  It uses only the necessary conditions proved in proof-GR0-r1.md Sec. 2;
R=0 is skipped because Lemma AR handles it.  gwas2.cpp adds the M0/NF reductions (unreviewed Lemma NF).

| p, N | scope | run data | candidate avoiders | files |
|---|---|---:|---:|---|
| 5,18 | ALL k <= 18, no M0/PM/NF restrictions | 6,061,009 | 0 | out/gwas_p5_N18.txt + out/gwas_p5_N18_k13-18.txt |
| 5,17 | ALL k <= 17, no M0/PM/NF restrictions | 3,248,817 | 237 (all DP-confirmed) | out/gwas_p5_N17.txt |
| 5,18 | M0/PM/NF, ALL k <= 18 | 925,495 | 0 | out/gwas2_p5_N18_nf.txt |
| 5,17 | M0/PM/NF, ALL k <= 17 | 493,931 | 237 (all DP-confirmed) | out/gwas2_p5_N17_nf.txt |
| 7,26 | M0/PM/NF, k <= 8 | 65,690,741 | 0 | out/gwas2_p7_N26_k1-9.txt (only completed CNT lines through k=8) |
| 7,26 | M0/PM/NF, k = 9 | 111,859,657 | 0 | out/gwas2_p7_N26_k9.txt (completed TOTAL) |

Thus [W+F, unreviewed] INV*b-rig(5) is rederived by a different search (it was already known from the exhaustive
D10 avoider list).  At p=7, any non-RGR rigid-rotation avoider would reduce to a normal form with k >= 10
(k <= 19 = 3p-2 since Theorem P gives F <= 19).  Only k <= 9 has been excluded: do NOT claim INV*b-rig(7).
This also excludes an original hypothetical non-RGR rigid-rotation avoider with at most 9 constant reflection
blocks, since the reductions cannot increase k.  No such avoider was found.  No full INV*(7) conclusion.

## 4. Stops, limits, status

Every new native run used one busy process, a soft CPU limit and a larger tool wall deadline.  The combined
p=7 k<=9 run hit its soft CPU limit after completing k<=8; its in-progress k=9 result is UNKNOWN.  The later
k=9-only run completed in 1,461.24 seconds and found zero.  No SIGKILL or deletion occurred in this INV* cycle.
The README's 30-minute progress log was overdue before this closeout entry; Main received checkpoints at
18:31 and 19:07 (the first gap exceeded 30 minutes).  This is a logging deviation, not evidence of compliance.
The old PAR-cycle deviations remain recorded in c2/README.md and are not erased by this cycle.

## 5. Open obligations after this attack

* INV*(p), rotation-value half (a): still open (no work on rho_0 or rotation values outside a single +/- pair).
* INV*b-rig(p), the reflection-constant half for already-rigid rotations: written exact criterion and merge-normal
  form, but still open for all p >= 7; p=7 normal forms with 10 <= k <= 19 remain uncomputed.
* RUNS(iii): owned by OlsonRunCount5, not touched.
* All-p PAR/MIX_low closure and M0 reviews remain with Main; reviewed closure files were not edited.
