# Actual Tuscan11, m = 9, L3, one face (W1), c = 70, sub-case (β): the surviving skeletons are excluded by a w-neighbour count, so c = 70 is closed

Actual `/bin/date` before this body: **Mon Oct 26 14:34:08 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

v101 (SHA256 `efe08c76556deb7613ccb769f61223f6a04065861062b94ea31a3043512a4008`), §3.3:
- the skeleton of sub-case (β) in its only surviving order (G3 < H9, G4 < H8);
- the options Hs, Gs (and Yα, Cα, Dα);
- the formulas t = 6 − Hs − Gs, u = 4 + Hs + Gs and q = 7 + Yα + Hs;
- the exclusion of Hs = Gs = 0.

The neighbour rule (v97): w has exactly one edge to every other label, through its 10 slots. Those slots are:
- ℓ (one neighbour, T[t−1]);
- b_w (three: Q[q−1], Y1[y1−1], Y2[y2−1]);
- P-w1 in P2 = P(u,10) (two);
- P-w2 in P4 = P(u+10,20) (two);
- Y1-w (two).

## 2. w needs exactly t − 1 = 5 − Hs − Gs neighbours with T_int-labels

Four slots are forced to carry T_int-labels:
1. **ℓ–T[t−1].** T's interior carries only T_int-labels.
2. **b_w–Q[q−1].** Q2 = Q(u, q−1] has size 2 + Yα − Gs ≥ 1. Its users are the P[10]-label (if Yα), the P[20]-label, and the Y1[G4]-label (if Gs = 0). All are T_int.
3. **b_w–Y1[y1−1].** The last Y1-vertex lies in the (4,7) segment, whose users are the P[10]-label (if Yα = 0) and the Y1[H9]-label (if Hs = 0). If that segment is empty, the last Y1-vertex is Y1[H8]. Either way the label is T_int.
4. **P-w1.** P2 is bounded by P[u] (label c1, S) and P[10] (T_int). Every other user of P2 is T_int. So P-w1 has at least one T_int-neighbour, and exactly one only when **P-w1 = P[u+1]**, adjacent to c1.

**Case Hs = Gs = 1.** Here t − 1 = 3, but the four forced slots give at least 4 T_int-neighbours. Contradiction.

**Case Hs + Gs = 1.** Here t − 1 = 4, so the four forced slots give exactly 4:
- **P-w1.** It has exactly one T_int-neighbour, so P[u+1] = w.
- **P-w2.** It needs both neighbours in S.
  - P4 is bounded by P[u+10] (S) and P[20] (T_int).
  - The only S-user inside P4 is c1.
  - So P[u+11] = w and P[u+12] = c1.
- **Two c1–w edges.** Label c1 is joined to w both by P[u]–P[u+1] and by P[u+12]–P[u+11]. This contradicts one edge per label pair (F2).

## 3. Result

The c = 70 (β) skeletons are impossible. With v101 §3.2, **c = 70 of L3 W1 is impossible** (WRITTEN, Tuscan-1 necessary case).

**Still open in L3 W1:** c ∈ {50, 60}.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
