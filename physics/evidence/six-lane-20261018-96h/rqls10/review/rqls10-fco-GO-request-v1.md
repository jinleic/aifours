# Exact admission request: fourier_co_enum_v1 (finite Fourier-type clock-orbit family FCO(n)) - NOT run

Recorded 2026-10-19T05:48:49-0700 (from /bin/date). Requester ContinueRQLS10b. Same physics-2 target (controls at small n,
target n = 10); not a third slot. Nothing has been executed for this item (no smoke); launch only after the parent pins
it and sends an item-specific GO naming the launcher.

## 1. Pins
- source code/fourier_co_enum_v1.py 2b72ec879f44239ba441160b2174baad0b107021be2e2475e7de42dde96e83a6 (0444, 482 lines,
  standard library only, no input files)
- written basis evidence/fourier-co-ansatz-v1.md b3a79dd2a87f8d4477188f91e2777c2afc2efa41e431316b028a6c7e49f844bf
  (lemmas F1-F6; unreviewed). The probe does NOT rely on F5 for coverage (checked as a prediction only).
- tightening 8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20; stop registry review/stop-registry-v2.json
  a47bb3ffbff22c0f15b1d7fba186812c27ac925ec77a73c76b1d7eb3f639acb7 (no relevant stop)

## 2. Family, arithmetic, coverage (stated precisely)
- FCO(n): q_ij(t) = omega^(t j + pi(t) rho(i)) / sqrt n, omega = e^(2 pi i/n), pi, rho permutations of Z_n; classes
  C_s = {(i,j): j - i = s mod n} (B = Cay(Z_n) up to isotopy). Rows/columns always orthonormal (F1); 1-RQLS iff
  S_pi(i'-i, rho(i')-rho(i)) = 0 for all i != i' (F2). Huang-Li's construction is rho = id.
- Exact test: a sum of n-th roots of unity vanishes iff its integer exponent histogram polynomial is divisible by Phi_n
  (monic exact integer division; Phi_n by exact division of x^n - 1). Norms are exactly 1 by construction.
- Normalisation: (pi, rho) is a solution iff (pi + d, rho + d') is (F3). Enumeration: EVERY permutation pi with
  pi(0) = 0, (n-1)! of them (n = 10: 362,880), no prefilter or sampling; exact zero table row by row (row n/2 first for
  even n), pi dropped only when a row a has no zero (sound: every a != 0 occurs as i' - i); for the rest, EVERY rho with
  rho(0) = 0 satisfying the exact pairwise condition, by exhaustive DFS. COMPLETE for n = the normalised solution set is
  exactly enumerated and every solution is a unique translate (pi + d, rho + d') of one of them; INCOMPLETE_TIME /
  TERMINATED / INCOMPLETE_STOPPED / NOT_DONE = no conclusion for that n. No fallback, no post-hoc widening.
- Rays: same projective ray iff the exponent difference is constant mod n (exact for unit-modulus entries; covers every
  coefficient incl. zero divisors 2, 4, 5, 6, 8 at n = 10). R1 = union-find over (c, k); R2 = explicit exponent table
  and ALL n^2 (n^2-1)/2 cell pairs (4,950 at n = 10). G = exact Gram check of all 3n lines.

## 3. Gates (in this order; exit 3 on failure, nothing later runs)
1. Self-tests: Phi_n degree = phi(n) and |Phi_n(omega)| < 1e-9 (n = 2..10); exact test vs floating evaluation on 3,000
   random histograms incl. constructed vanishing ones: 0 mismatches.
2. Imports (Zhang-Cao arXiv:2608.29201v2 Sec. 3, citing Ball-Simoens and Paczos et al.): n = 2, 4, 6 COMPLETE with 0
   solutions; n = 3, 5 COMPLETE with >= 1 solution and every solution exactly n rays.
3. n = 7 Huang-Li with normalisations: brute force over ALL 5,040 permutations mu of Z_7 (no normalisation): 133
   complete mappings (as in evidence/fixedb_anchors_v1.result.json), 35 affine, 98 non-affine; among mu(0) = 0
   (translation acts freely and preserves both properties): 19, of which 5 affine and 14 non-affine (computed directly).
   FCO(7) COMPLETE, its rho = id solutions are exactly the 19 normalised complete mappings and those with 49 rays are
   exactly the 14 non-affine ones (set equalities).
4. Exact zero-table symmetry Z[a][b] = Z[-a][-b] on every full table.
5. Mutation controls, intended reasons: M1 transposing pi(1), pi(2) of a maximal FCO(7) square: rows 0, columns 0,
   classes > 0 bad pairs; M2 +1 on one exponent of cell (2,3): exactly 6 bad pairs in each of rows/columns/classes, all
   through that cell; M3 pi = 2t, rho = id (n = 7): solution, R1 = R2 = 7 rays; M4 zero divisor (n = 10)
   pi = [0,3,4,1,2,7,8,9,6,5], rho = id: R1 = R2 = 50, all 50 coincident pairs have rho-difference 5 and column
   difference 5, R1 directions only c = 5; M5 pi = rho = id (n = 10): rows 0, columns 0, classes > 0.
Then: n = 8 (recorded), n = 10 TARGET, n = 9 (recorded, only if n = 10 is COMPLETE and time remains).

## 4. Stop rules and outputs
- Immediate candidate stop: the first n = 10 solution with 100 rays by R1 or R2 -> output written with pi, rho, the
  convention, the full exponent table, G, R1, R2, then exit 7. Nothing is claimed; parent notified at once.
- Internal defect: R1 != R2 or G failing on any solution that is recorded in full (every n = 10 solution; the first 5 and
  up to 20 maximal per other n) -> exit 8 with the offending (pi, rho) and exponent table.
- Non-maximal n = 10 solutions (if any): counted, the first 50 recorded in full with G and R1/R2; enumeration continues.
- Protocol: waits for "GO" on stdin (else exit 6, no output); SIGTERM -> cooperative stop, status TERMINATED, exit 5;
  exit 0 = finished with per-n status; 3 = gate failure.
- Budget: cooperative self budget 240 s (checks per pi, every 2,048 DFS nodes, every 256 solutions); estimated total
  60-120 s (n = 10: 362,880 tables with early exit). Single process; RSS expected < 100 MB; one output JSON (exclusive
  create), expected < 2 MB (all lists capped).
- Proposed launch (parent to choose): (A) wrapper as for earlier small probes: /bin/bash -c 'echo START date PID $$
  PGID; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/fourier_co_enum_v1.py
  evidence/fourier_co_enum_v1.result.json <<< GO' (here-string keeps exec's PID), tool timeout 0, operator SIGTERM to
  the PGID at 280 s if still running; or (B) owned_supervisor_v2 with a config the parent pins (the probe already
  implements the GO/SIGTERM protocol). Launch-record path + sha to the parent at launch; terminal receipt + empty-child
  census on return.

## 5. Claims discipline
A COMPLETE n = 10 enumeration with no solution would be a restricted result for FCO(10) only (one implementation;
needs independent replication), not a statement about 1-RQLS(10) in general. Any n = 10 solution is a CANDIDATE until
independent exact verification (three checkers chosen by the parent); a maximal one would be an exact algebraic object
(entries 10th roots of unity / sqrt 10) but is still not claimed before that. No novelty or priority claims.
