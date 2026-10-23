# Receipt: fixedb_anchors_v1 (initial-scope stdlib EXACT probe, integer cyclotomic arithmetic)

Recorded 2026-10-19T04:45:27-0700 (from /bin/date). Owner ContinueRQLS10b. Source code/fixedb_anchors_v1.py
87069e53a64d4d877497c45d9288111099b3a12fc0446aac17307cb9ad73431b (0444); launch record evidence/fixedb_anchors_v1.launch.json
e31450944b631e1f810cb73615e5e67c16bf739099cdf20dcd23f418a9b5d5ea (written 0444 before the run). Command (cwd lane, tool timeout
0): /bin/bash -c 'echo START ... PID $$ ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B
code/fixedb_anchors_v1.py evidence/fixedb_anchors_v1.result.json'. START 2026-10-19T04:37:34-0700, PID 82955 = PGID 82955,
EXIT 0, END 04:37:34 (0.138 s in-run); single process. Output (0444, 22,736 bytes) evidence/fixedb_anchors_v1.result.json
13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92. One implementation; exact arithmetic in Z[zeta_7], Z[zeta_8]
(integer coefficient lists, zero test by reduction modulo the cyclotomic polynomial).

Purpose: exact positive anchors, written in the U-form q_ij = U_i e_j with U_0 = I, for the proposed fixed-B no-symmetry
model (design note evidence/fixedb-unitary-model-proposal-v1.md).

Results (all gates true):
- v = 7, Huang-Li complete-mapping construction (arXiv:2606.27758, Theorem "Construction--complete mapping" with the
  pan-diagonal transversals T_s): Z_7 has 133 complete mappings, 35 affine, 98 non-affine; mu = (0,1,3,5,2,6,4) (first
  non-affine in lexicographic order). B(i,j) = (j - i) mod 7 (cyclic, isotopic to Cay(Z_7)). Exact Gram = I on all 21
  lines; 49 distinct rays; B Latin. U-form (U_i = F^* Phi_i, F = Fourier = row 0): Gram exact on all 21 lines, 49 rays,
  U_0 = I exactly. Mutation of one entry: 18 nonzero Gram entries. Control mu(x) = 2x (affine complete mapping): exact
  1-RQLS(7) with 7 rays (not maximal), as the construction predicts.
- v = 8, Zhang-Cao Example 3.3 (arXiv:2608.29201v2), transcribed from the source TeX: exact Gram = I on all 24 lines (rows,
  columns, the printed transversals T_k = {(i,j): i XOR j = k}); 64 distinct rays; B = XOR Latin; row 0 is the
  computational basis, so U_0 = I exactly. Mutation (cell (3,3) := cell (3,2)): 5 nonzero Gram entries.
Scope: these are exact checks of two published constructions (transcription + arithmetic), used as calibration anchors;
nothing about v = 10 follows from them.
