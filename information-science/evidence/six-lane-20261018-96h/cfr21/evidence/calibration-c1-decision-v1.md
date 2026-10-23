# Calibration C1 and decision on LR — 2026-10-18T23:50:39-0700 (ContinueCFR21)

## Measured (frozen probe p3-p21-sister-lifts-v1, source 16751cd8…, stdout 782a80b9…, wall 2.1 s, exit 0)
For every one of the 96 pinned P21 DM6 (generic: full mod-3 and mod-7 affine rank), the exact F3 lift system of its
mod-7 image (105 fibre triple-sum equations on 100 gauge-fixed unknowns) has rank 93, lift space dim 7 (3^7 vectors),
and EXACTLY ONE nowhere-zero solution up to global sign: the original DM. Zero sister DM6, zero new triple classes
(6 P21 triple classes under <C_u, A, I, T_a>).
Consequence (exact, restricted): any DM7 having six rows whose mod-7 image is equivalent to a P21 mod-7 image contains
the corresponding P21 Z21-DM6 itself (unique lift up to the Z21 automorphism 8 and row translations), hence lies inside
the old two-program P21-triple exclusion. The beta-anchored generic family adds nothing.

## Exact dimension accounting (written; to be in proj-theory-v1.md)
Gauge-fixed F3 lift system for k rows over Z21: unknowns 20(k-1); equations 7*C(k,2); the C(k-1,2) constant
circulations of K_k are automatic dependencies. Excess E(k) = 7C(k,2) - C(k-1,2) - 20(k-1): E(6) = -5 (DM6 lift
spaces are automatically >= 5-dim; P21 has 7), E(7) = +12. So a DM7 needs a mod-7 image whose fibre system has
F3-rank <= 119 instead of the generic 120, plus a nowhere-zero kernel vector. Exact bridge: CFR(6,21) exists iff some
(Z7,7;3)-DM beta has such a lift. Structural sources of the missing dependencies seen so far: symmetry (P21: +2) and
affine row relations mod 7 (old CRT families report kernel ranks 6/12/18/24 [old receipts, to be re-derived]).

## Decision
* No candidate-producing generic lift exists in this representation from known positives (rigidity above).
* LR rank<=3 is NOT requested as a native item now (parent concern accepted: generic stratum untouched; heuristic
  hit probability negligible). At most a <=300 s stdlib rank-2 probe will be run as a cheap, clearly scoped lemma
  check plus a test of the affine-dependency count.
* Next: proj-theory-v1.md (CRT bridge; uniformity principle; mod-3 constant characters of support <=5 impossible;
  DM7 mod-3 affine rank >= 5 via Griesmer; mod-7 set property; lift-dimension accounting; P21 anchors) for parent
  check and hostile CLI review. Any native GO request will cite stop-registry-v1 and launch-contract-tightening-v1.
