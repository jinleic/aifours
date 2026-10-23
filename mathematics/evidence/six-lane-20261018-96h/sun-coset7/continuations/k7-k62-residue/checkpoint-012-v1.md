# Checkpoint 012 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T06:01:24-0700. Previous: checkpoint-011 at 2026-10-19T05:54:42-0700.
- No computation run; no process running; no old/sibling artifact edited. Parent directed: (a1) Case B/A with the
  transfer-count lever first.

## Actual results (written; to be frozen next as K7-TC-v1, conditional on RICH/A1-STRUCT)
1. **Lemma TC (general transfer):** at apex u, L_j subset L_a (every fibre meeting coset j meets coset a) iff at apex a
   (g_a = 1) D_j subset X_u; hence D_j cap D_u = empty there. Rigidity sources: FG-tight rows (Corollary 5/6 equality).
2. **Case B, alpha*_v1v2 = 1: impossible** (rows (1,4,4,4|c*|2) at v give L*_z subset L*_a; count at a in C*: union >= 11/12).
3. **Case B, alpha*_v1v2 = 2, alpha*-pattern (1,2,2) on T*: impossible** (rows (1,2,4,4|3|e*) at the 1-edge ends give
   L*_z, L*_a3 subset L*_v; count at v in C*: union >= 11/12 > 5/6).
4. **Pc5' violates TC**: R1 rows at u3, u5 give D_u2 cap D_u3 = D_u1 cap D_u5 = empty at apex u4 (C^alpha); there the
   alpha*-masses (4,4,2,2 | z 3 | t 4)/6 force union >= 1. So Pc5' is no longer an obstruction.
5. **Surviving obstruction Q_B'** = Q_B with alpha*_v1v2 = 2 (Case B, pattern (2,2,2)): all alpha*-rows slack; the
   alpha-rigid rows (R1 at a, R3 at v) give only D_a' cap D_a'' = empty at a, D_z, D_t disjoint from D_v at v', and
   D_z, D_v' disjoint from D_v at t; explicit coset distributions satisfy every resulting count (union 4/6 at a,
   17/24 at v and v', 5/6 at t). Case A in general is not yet analysed beyond Pc5'.

## Next bounded action
Freeze K7-TC-v1 (items 1-5) with full proofs and explicit distributions; then either continue Case A in general or,
per parent, resume (a2). Next checkpoint by 06:55 PDT.
