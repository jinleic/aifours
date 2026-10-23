# Checkpoint 009 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T05:37:40-0700. Previous: checkpoint-008 at 2026-10-19T05:32:41-0700.
- No computation run; no process running; no old/sibling artifact edited.

## Actual result since 008 (written derivations, to be frozen next as one structure/obstruction file)
1. **PFG-t (partial FG at t over W):** if the x-graph {uv in W : x_uv <= 2} is connected, the chain along it has every
   k <= 2, so gcd(n_t, T_W) = 6, mu(U_t W_W) >= 1/6, and at t (VFC of C^x) the W-part of t's x*-row has value <= 5;
   at equality D_z must share a right coset with a y-tight W-set. Resulting list of allowed W-multisets of t's
   x*-row: {44222 (z 4-type), 44122 (z 4-type), 44412, 44422, 44442}; all others (22222, 1^k 2^(5-k), 11111, 44441,
   44444, and every multiset with one four) are excluded. This kills the C5/pentagram pattern Pc5 with all t-entries 2.
2. **No t-entry 3** in (a1) (rows without a W-three and e = 3 fail FG).
3. **Case B structure (T = W, T* != W):** |T*| = 3, W \ T* = {v1,v2}, E >= 2; alpha = 4 on all of T*, on v1v2 and on
   t-v; alpha = 2 on T* x {v1,v2}; >= 2 vertices a of T* have alpha_ta = 2, alpha*_ta = 4.
4. **Explicit survivors of every written rule so far** (abstract patterns, not group realisations):
   Q_B (Case B; E >= 2; alpha*: T* inner 2, T*-v 4, v1v2 1, z-v 1, t-a 4, t-v 2) and
   Pc5' (Case A; F_alpha = C5, F_alpha* = pentagram, t-entries alpha (4,4,2,2,2), alpha* (2,2,4,4,2), E >= 2).
   Both pass LFC at z and t, FG (all W rows, both orientations), PFG-t, INV, T on all triangle types, D23, LZ and the
   centre-count inequalities (phi-values free). So the current toolset cannot close (a1).

## Blocker / next bounded action
(a1) needs a new cross-vertex idea (the per-vertex FG rigidity leaves the fibre fractions phi_u free). Next: freeze the
structure/obstruction file with full proofs and the exact missing lemma; then examine (a2) double-(b') with FG under a
compatible base pair. Next checkpoint by 06:30 PDT.
