# Case-A working notes v1 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T06:54:34-0700. Unreviewed scratch record so that partial
  reasoning is not lost; nothing here is claimed. No computation.

## Case A residue (T = T* = W; entries on W and W-t in {1,2,4}; c = 3 everywhere)
1. Every alpha-row and alpha*-row has at least one W-four (zero fours means >= 3 entries <= 2, and Lemma B then forces
   exactly one four). (1,1,4,4) rows have value >= 6 (y = 1 on ones, 1/2 on fours), so they do not occur.
2. A row with exactly one four (Lemma B: W-part (1,2,2,4) or (2,2,2,4)) has e = 4 and E >= 2. Hence no vertex has a
   single four in both orientations (alpha_ut = alpha*_ut = 4 contradicts INV). Degree types (d, d*) per vertex:
   (1,2), (1,3), (2,1), (3,1), (2,2); all-(2,2) is K7-TC-A22. So in the remaining Case A, E >= 2.
3. Rigidity of the single-four rows (C^x at u, four-neighbour f): R3 = ({2,2,2,4}|3|4) (K7-TC) and
   R3' = ({1,2,2,4}|3|4): y_A = (o 1, f 1/2, s 1/2, s' 1/2), y_B = (o 1, s 1/2, s' 1/2, t 1/2), both value 5 and feasible
   ({f,s,s'}, {t,s,s'}, {z,s,s'} have all gcds 2; {f,t,s}, {z,t,s}, {z,f,s} allowed with weight 1). Equality clause:
   L_f = L_t and L_z subset L_t (the one o is isolated).
4. Transfers (Lemma TC) from such a u: at apex f: D_t, D_z disjoint from D_u; at apex t: D_f, D_z disjoint from D_u.
5. Twin rule: x_uv = 1 forces x_uw = x_vw for all other w in W and x_ut = x_vt.

## Next
Combine 2-5 with Corollary L (|P|, |P*| >= 2 when the complement graphs are connected) and a VFC count at t or at f.
