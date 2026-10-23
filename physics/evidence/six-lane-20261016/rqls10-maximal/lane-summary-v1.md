# rqls10-maximal: lane summary (v1)

Written about 15:00 PDT, 2026-10-18. This supplements the frozen README.md (sha256
05a3045270102cdc2c21734aabab23121f5dd73d548a6fc83b896206c0ad10e5) with everything recorded after 14:42 PDT.

## Verdict

**UNKNOWN.**
- There is no candidate witness of a maximal-cardinality 1-RQLS(10).
- There is no unrestricted nonexistence proof.
- No novelty, priority or significance is claimed.
- Order 10 remains open in the primary source (Zhang-Cao arXiv:2608.29201v2, Thm 1.3 and Section 5).

## Computation performed (exactly two parent-authorised probes plus exact controls)

1. **Exact checker controls** (14:17 PDT, Q(zeta_8)).
   - Source Example 2.4 passes: 64 distinct rays, 24 ONB lines.
   - The four mutation and negative controls fail exactly their intended predicates.
   - Receipt: controls/controls-receipt-v1.md, sha256 276c72de8cd69011d324bf3961876001b3139d6960f3b6eb029fefcc504cb2d2.
2. **Float structure probe** (14:15:38-14:19:49 PDT).
   - It stopped at the in-run DISK_FLOOR guard (free 11,999,363,072 B), so its outcome is UNKNOWN.
   - WH10 gave no candidate (best residuals 0.0523 and 0.2020). G10 was truncated. The G8 control was weak.
   - The causal writer of the floor breach is unidentified.
   - Records: result sha256 b854adf9a9fa8adc80bbb3f07a120f1495f9ffdf14fc00e00390b86e748d6346; receipt sha256
     be1949c68619525844ad08697501b9e73cd7d13f57ef38a53b3665d2bd3dcfac; addendum sha256
     87bdd775dd0b9080ddd54576a07e140b5e39f3c711abf0f73c31e72ed7dcbbbb.
3. **Exact quaternary Paley probe**, under GO review/phys-2-rqls10-hadamard-probe-go-v1.json sha256 7d8d298b...e4b
   (14:47:25-14:47:38 PDT).
   - All 2000/2000 sampled pi completed: stop MAX_SAMPLES, EXIT=0.
   - Rows and columns are ONB in every case, and 824 cases have 100 distinct rays.
   - **No orthonormal transversal occurs in any case.** Hits: 0. Per the GO this is a sampled UNKNOWN.
   - Records:
     - script sha256 eff3718539da43e20f2b20485da0994d9d13a5c042b4d2c8187b786df96c81f2;
     - prereg sha256 6f33e0c47d4e1590400efa9b6428bf51cfd4c0a4702b8bbbf764051ae8d58210;
     - result sha256 4eda225a09443e3f72894092ca1d4422ae8c13b07edb249146b037d0fd899bd8;
     - receipt sha256 7feba8dd46b9308ead3eacd17d0c31789e32a8a231e98ffc3345b8dedc9bc3fb.

## Restricted-ansatz derivations

All of these are unreviewed and ansatz-only. They are not no-go theorems for the target, and their external imports
are marked in the files.

| id | file (sha256) | statement |
|---|---|---|
| R1 | restricted-results-v1.md (4ccf86cd...111e) | Laminar coordinate trade rotations from a classical MOLS(10) pair always repeat rays. |
| R2 | same | Superposing two classical mates repeats rays. |
| R3 | same (full proof) | Flat Fourier-permutation family omega^{i mu(t)+jt}/sqrt10: no orthonormal transversal when mu(t) - t is non-constant mod 2, hence at most 50 rays for every B. Uses de Bruijn vanishing sums, CRT, Rédei [IMPORT]. |
| R4 | same | Z_10^2 regular-orbit ansatz: 3 of 4 cocycle cases impossible; the WH10 case is UNKNOWN (numerically infeasible). |
| R5 | same | Rectangular 5+5 halves fail by Mann parity. A dim-2 part, or a closed 3x3 dim-3 block, repeats rays. |
| R6 | same | Common orthogonal subsquares have order <= 5 and are classical [IMPORT]. |
| R7 | restricted-results-addendum-1.md (7ee05dd2...64c15a28) | Product sigma (x) e with e from pairwise non-orthogonal bases of C^5 (e.g. MUBs) cannot give 100 rays. The classes are essential to the argument. |
| R8 | restricted-results-addendum-2.md (5bebfb32...a07a) | Controlled tensor products 2x5 and 5x2 fail. The 4+6 corner split is parity-feasible and open. |
| — | restricted-results-addendum-3.md (61bee974...fa5101) | Flat 5th-root half-splits form an exact AG(4,5) combinatorial family. The uniform-direction sub-case is rectangular and fails by Mann. The mixed-direction case is open. |
| R9 | restricted-results-addendum-4.md (589a62a2...241775) | Quaternary parity for n = 10: three mutually orthogonal +-1/+-i vectors satisfy sum of pairwise type intersections = 1 + sum of weights (mod 2). So the Paley product family has no orthonormal transversal for any pi, which explains probe 3. A necessary parity filter is stated for general BH(10,4) products. |
| — | restricted-results-addendum-5.md (30326860...e0175d) | The R9 parity is specific to 4th roots. Alphabets containing mu_8 avoid it, which is a lead. |
| R10 | restricted-results-addendum-6.md (b6022794...52e61a) | Paley rows times any i-free Hadamard family (incl. Fourier/BH(10,10)) has no orthonormal transversal: vanishing principal 2x2 minors force a Hermitian unit-diagonal Hadamard of order 10, contradicting trace 10 = (n_+ - n_-) sqrt10. |
| — | restricted-results-addendum-7.md (hash in final report) | Rank reformulation: a Hadamard-product square alpha o beta is resolvable by L iff a(t,t')^T M_{b(t,t')} = 0 for all t != t', where (M_b)_{i,s} = b_{L(i,s)}. This needs rank M_b <= 8 for all 45 coordinate pairs. Structural lead only. |

## Exact remaining obstruction

**Positive direction.**
- Every family examined either provably fails (R1-R3, R5-R10, partial R4) or failed in the sampled or numeric probes
  (WH10, Cay(Z10) descent, Paley sample).
- The recurring mechanism is a Z_2 parity tied to 10 = 2 * 5:
  - Hall-Paige for Cay(Z10);
  - Mann parity for halves;
  - de Bruijn-CRT (Lemma A) for 10th-root Fourier families;
  - mod-4 parity (Lemma Q) for quaternary alphabets;
  - the non-square order (sqrt10 trace) for Paley x i-free products.
- In addition, 3 ONB lines per cell make naive real counting overdetermined by a factor of 1.5. Solutions must
  therefore be special algebraic objects, unlike QLS(10) alone (ratio 1, where maximal-cardinality QLS(10) are known).

**Families not excluded** (candidates for a parent-authorised search with exact reconstruction):
- Hadamard products alpha o beta over Q(zeta_8), or using non-Paley BH(10,4) classes passing the R9 filter;
- mixed-direction flat 5th-root half-splits (AG(4,5) SAT/CSP);
- non-rectangular 5+5, 4+6 and 3+7 splits;
- general product sigma (x) e with arbitrary e in C^5;
- Parker-type Z_7 + 3 quantum prolongations;
- non-abelian or non-regular group orbits;
- unstructured vectors with a non-group B.

**Negative direction.** No route to an unrestricted proof exists within the lane. It would need control of every
Latin square B and every complex vector; even v = 4, 5 needed the Ball-Simoens case analysis.

**Acceptance for any future candidate:**
- frozen witness;
- exact_rqls_checker_v1 (sha256 90aaf3beefd049087b7b3d5f00644884a7a99bebcdfdbf90d26c2985cbe89a5d);
- an independent second checker and mutation controls;
- producer replay;
- Codex and Claude hostile reviews;
- a primary-source comparison.

## Process notes

- Every lane file was created exclusively and frozen read-only after writing. Corrections are separate addenda.
- No deletions or overwrites. No /tmp, Git, paid APIs, external contact, global configuration or native solvers.
- The single side effect is probes/__pycache__ from one pre-freeze py_compile; it is retained.
- Disk: an in-run guard observed the floor breach at about 14:19:49 PDT. Fresh df readings: 11,771,092,992 B at
  14:20:05; 14,505,951,232 B at 14:54:45.
