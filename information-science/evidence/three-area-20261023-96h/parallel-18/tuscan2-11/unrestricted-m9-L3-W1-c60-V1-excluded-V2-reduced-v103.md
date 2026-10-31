# Actual Tuscan11, m = 9, L3, one face (W1), c = 60: V1 excluded; V2 reduced

Actual `/bin/date` before this body: **Mon Oct 26 14:36:35 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This packet gives a necessary-case exclusion and reductions, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- **v100** (SHA256 `86cb5e2723ae0fbcf3be7090a662ac6df461ca38538cce4ac9c528453788b591`): the W1 face and the stretch counts. At c = 60 the counts allow:
  - for v: V1 (n_P = n_Q = 1) or V2 (n_Y = 2);
  - for w: (m_P, m_Y, m_Q) = (2,0,1) or (1,2,0).
- **v96** (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`): Lemma VL and the matching method.
- **v97**: the neighbour-count rule.

**Positions at c = 60:**
- q = p − 5 and y1 + y2 = 60 − t − 2p;
- A1 = t + p, A2 = 60 − p, B2 = 55 + p, B3 = 115 − t − p;
- R_end is row 5 and R_start is row 6.

## 2. V1 is impossible

### 2.1 Placements

**The P-v vertex.**
- In rows 1–4, the P-v passages must sit in rows f < row(A1) < row(A2) < g.
- So f = 1, A1 lies in row 2, A2 lies in row 3, and g = 4.
- Hence 21 ≤ p and t + p ≤ 29. The P-v lies in P(10, u+10).

**The Q-v vertex.** It lies in Q(10, u+10), with rows {7, 9}. So b″'s third passage lies in row 8.

**The w-vertices.**
- With m_Y = 2, R_start would need q ≤ 9. That contradicts q ≥ 16, so (m_P, m_Y, m_Q) = (2,0,1).
- The vertex types are then:
  - P-w at {1,5} and {2,4};
  - b_w's first passage in row 3;
  - Q-w at {6,9};
  - b_w's other passages in rows 7 and 8.
- These placements give 26 ≤ t + p ≤ 29 and p ≤ 24.

### 2.2 The Y1 order

**Types.**
- P: {0,5}, {1,5}, {1,4}, {2,4}, {2,3}.
- Q: {6,10}, {6,9}, {7,9}, {7,8}.
- Y2: {3,8}.
- Y1: either {2,8}, {3,8}, {3,7} (order G2 < H8) or {2,8}, {2,7}, {3,7} (order H8 < G2).

**Order H8 < G2.** The Y1[G2]-label has cut rows {2,3,7}. Row 8's partners are 2 (via Y1), 3 (via Y2) and 7 (via Q(u+10..]), all used. Contradiction.

**Order G2 < H8.**
- The matchings make the T_int-labels P[10], P[20], Q[10] and Y1[H8]. So t = 5.
- The P[20]-label and the Y1[H8]-label have no vertex adjacent to any v-vertex except through T[1]. Their vertices lie in P2, P4, Q2, Q4, T, at the P[20] cut, or at Y1[H8]. Meanwhile:
  - the P-v and the Q-v lie in P3 and Q3;
  - b″'s neighbours lie in P5, Y1[1,G2) and Y2.
- So v misses one of these two labels. Contradiction.

## 3. V2: forced shape

### 3.1 Placements

**Parameters.**
- Lemma VL gives p ≤ 20 − t and q ≤ 9. So 11 ≤ p ≤ 14 and 16 ≤ t + p ≤ 19.
- A second P-w would sit at {1,4} and give row 1 two w's. So (m_P, m_Y, m_Q) = (1,2,0), with the P-w at {1,5}.

**v and w.**
- The two Y-v vertices have first passages in rows 2 and 3.
- The two Y-w vertices have second passages in rows 7 and 8.
- The first-stretch w-rows {2,3,4} are shared by b_w's first passage and the two Y-w first passages.

**The cuts.** Six of the nine non-v, non-w cuts lie on Y, at positions 20, 30, 40, 70, 80 and 90.

### 3.2 Sub-case: A3 in row 9

**Forced shape.**
- All four Y-vertices lie on Y1, and b_w's first passage lies in row 4.
- The types are forced: (2,8) for one v and one w, and (3,7) for one v and one w. Y2 is the single type {4,9}.

**Order δ = H9 − G2 > 0.**
- The fourteen segment equations are consistent:

      p = 12,  t = 5 + O1 + O2,  G2 = 3 − O1 − O2,  H9 = G2 + 4 − [opt2],  y1 = H9 + 23.

  Here O1 and O2 indicate the T-options of the Y1[G2+10]-label and the Y1[G2+20]-label, and [opt2] is P[u]'s second matching.
- The Y1[H9+20]-label is reachable from v only through T[1]. So the four Y-v slots must reach the other T_int-labels, which forces O1 + O2 ≤ 1.
- **These skeletons are not yet decided.** They survive the v-count and the w-count. With O1 = O2 = 0, the w-count forces P-w = P[u+1] and puts both Y-w vertices away from T_int-neighbours.

**The order δ < 0, and the sub-cases with A3 in row 7 or row 8, are not yet analysed.**

## 4. Result

**WRITTEN, Tuscan-1 necessary cases, L3 with one face at c = 60:**
- V1 is impossible.
- V2 is reduced to the forced shape of §3.1, and its sub-case "A3 in row 9, δ > 0" to explicit skeletons with O1 + O2 ≤ 1.

**Still open in L3 W1:**
- c = 60, V2: these skeletons, the order δ < 0, and A3 in row 7 or 8;
- all of c = 50.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
