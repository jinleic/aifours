# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — (S0) type (6,9) with o0 = 6 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 09:05:26 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

This is v66 §4 (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`) with **A = o0 = 6**, P in {7, 8, 9} and r0 = 3. Then l = 15-P, lam = 21-P, lam3 = 9+P and |T2| = 10+P. The rows are:
- B_0 = e6..e1, v, a1..a4
- B_1 = a4..a_(l-1), w, b_(9+P)..b11
- B_2 = b11..b1
- B_3 = b1, v, c1..c9
- D_0 = c9..c_(lam3-1), w, a_(l-1)..a5
- D_1 = a5..a1, v, b1..b5
- D_2 = b5..b15
- D_3 = b15..b_(9+P), w, e_(lam-1)..e6
- R_0 = c3, c2, c1, v, e1..e7
- R_1 = e7..e_(lam-1), w, c_(lam3-1)..c13
- R_2 = c13..c3

The cuts are:
- P6: e6, a4, b11, b1, c9, a5, b5, b15;
- P2: e7, c13, c3.

Imports and method are those of v69 (SHA256 `627942a9c34e0bd03583a2c03509fe0adb1f5c6a797e9cc240d253d280142046`).

## 2. Exchanges

- (Z1) R_0 vs B_0: {c1, c2, c3, e7} = {a1..a4}, and a4 is in {c1, c2}. The path v, c1, c2, c3 may not repeat T1's {v,a1}, {a1,a2}, {a2,a3}, {a3,a4}. This leaves:
  - **(i)** (c1, c2, c3) = (a4, a1, a3) with e7 = a2;
  - **(ii)** (c1, c2, c3) = (a2, a4, a1) with e7 = a3.
- (Z7) R_2 vs B_3 (rule (R), k = 4): T3[10..13] is the complementary P4 of b1, v, c1, c2, so it reads **(c1, b1, c2, v) or (v, c2, b1, c1)**.
- (X1) B_0 vs D_1: {e1..e6} = {a5, b1..b5}.
- (X2) together with (Z2) (R_0 vs B_3): {c4..c9} = {e7, a5, b2, b3, b4, b5}.
- (Z4) R_1 vs D_0: {e7..e_(lam-1)} = {c9..c12, a5..a_(l-1)}.
- (Z3) R_1 vs D_3: {c13..c_(lam3-1)} = {e6, b15..b_(9+P)}.
- (X3) B_2 vs D_2: {b1..b4} = {b12..b15}, complementary P4s; so b12 and b15 lie in {b2, b3}.
- (X9) B_2 vs D_1: {b6..b11} = {a1..a5, v}.
- (X11) B_1 vs D_2: {b5..b10} = {a4..a_(l-1), w, b16..b_(9+P)}.

**The w-cut.** The P2 cuts carry e7 (a2 or a3), c3 (a3 or a1) and c13 (v or c1, with c1 = a4 or a2). None is w. As in v69 §3, the w-cut is the D_1|D_2 cut, so **b5 = w**. The w-vertices are:
- b_w;
- T2[5];
- T3[t] with 4 <= t <= 8 (c3 ≠ w);
- T4[i] with 1 <= i <= 5.

Also **c9 is in {b2, b3, b4}**: the labels e7, a5 and w belong to other cuts.

**The v-layouts.** As in v69 §4:
- **(alpha):** b11 = v is the v-cut, there is a T4 copy, and T3[10..13] = (v, c2, b1, c1);
- **(beta):** c13 = v is the v-cut, the T2 copies are T2[j] with 6 <= j <= 10 and T2[j'] with 16 <= j' <= 9+P, and T3[10..13] = (c1, b1, c2, v).

## 3. (alpha) is impossible

**Option (i).** T3[10] = v neighbours T3[11] = c2 = a1. This repeats the edge b_v T1[1].

**Option (ii).** Here c1 = a2 and c2 = a4.
- (Z4) becomes {e7..e_(lam-1)} = {c9, v, a4, b1, a5..a_(l-1)}. Since e7 = a3, **a3 is one of a6..a_(l-1)**.
- **(N) for v.** The v-vertices are b_v (neighbours a1, b1, a2, e1), T2[11] (b10, b12), T3[10] (c9, a4) and T4[k]. Here:
  - b10 is in {a3, a5};
  - b12 is in {b2, b3};
  - e1 is in {a5, b2, b3, b4, w};
  - T4[k]'s neighbours carry labels in {a3, a5, w}. By (X9) and (X11), the a6..a_(l-1) lie in {a1, a2, a3}.
- The labels b2, b3, b4 can come only from c9, b12 and e1, so w is a T4[k]-neighbour label. Hence k = lam-1, and {b10, e_(lam-2)} = {a3, a5}.
- T4[7] = a3 and T4[lam-2] both lie in R_1, so **e_(lam-2) = a5 and b10 = a3**.
- **(N) for w.** The label a4 must neighbour a w-vertex. This cannot happen at T3[t], whose neighbours lie in T3[3..9] with labels a1, a3, a5, b2, b3, b4, w. It cannot happen at T4[i], whose neighbours carry v, a5, b1..b4 or w. It cannot happen at T2[5]'s neighbour b4. Among b_w's neighbours:
  - a_(l-1) shares B_1 with T1[4];
  - b_(9+P) is in {a1, a2, a3};
  - c_(lam3-1) is in {e6, b15, b16..b_(9+P)} minus c13 = a2 (a T4[1..6] label, a b2/b3 label, or one of a1, a2, a3), so it is not a4;
  - e_(lam-1) = v.
- So **b6 = a4**. Then T2[7] carries a1, a2 or a5. But {a4, a1} = T3[2]T3[3], {a4, a2} = T3[1]T3[2] and {a4, a5} = T1[4]T1[5] are all used. Contradiction.

## 4. (beta) is impossible

**Option (i).** T3[13] = v neighbours T3[12] = c2 = a1. This repeats b_v T1[1].

**Option (ii).** Here c1 = a2 and c2 = a4.
- **b11 = a2.** b11 is a P6 cut other than the v-cut. By (X9) it is in {a1..a5}, and a1 = c3, a3 = e7 (P2 cut labels) and a4, a5 (P6 cut labels) are excluded.
- So T2[6..10] carries a1, a3, a4, a5 and v. (X11) gives {a6..a_(l-1), b16..b_(9+P)} = {a1, a3, v}.
- **(N) for v.** b_v's neighbours carry a1, b1, a2 and e1, and T3[13]'s carry a4 and c14.
  - No neighbour of T2[j] (labels in T2[5..11]) carries a b-label.
  - A neighbour of T2[j'] can carry a b-label only via T2[15], since b16.. lie in {a1, a3, v}.
  - So b2, b3, b4 must be e1, c14 and b15. This forces **j' = 16** and c14 = e6 (by (Z3), with c13 = v).
- If P >= 8, T2[17] carries a1 or a3. Not a1, which would repeat {v, a1}. So the second neighbour of T2[16] carries a3. T2[j]'s two neighbours must then carry w and a5, so j = 6.
  - **(N) for w** needs a4 among w-neighbour labels. T2[5]'s neighbours are b4 and v, so a4 must be e_(lam-1).
  - It also needs a2. None of T3[t], T4[i], T2[5], a_(l-1), b_(9+P) or c_(lam3-1) can carry a2, and e_(lam-1) = a4 is already used. Contradiction.
- If P = 7, T2[16]'s neighbours carry b15 and w, and T2[j]'s carry a3 and a5.
  - **(N) for w:** a2 can only be e13, so a4 must be b6.
  - Then T2[7] carries a1, a3, a5 or v. But {a4, a1} = T3[2]T3[3], {a4, a3} = T1[3]T1[4], {a4, a5} = T1[4]T1[5] and {a4, v} = T3[12]T3[13] are all used. Contradiction.

## 5. Result

**(S0) type (6,9) with o0 = 6 is impossible**, and so is its mirror type (1,4) with p0 = 6. With v69 (SHA256 `627942a9c34e0bd03583a2c03509fe0adb1f5c6a797e9cc240d253d280142046`), the four/four shape remains open in (S0) only for:
- type (6,9) with A = 5 and P in {7, 8, 9};
- type (9,6) with A in {8, 9, 10} and P in {6, 7, 8};
- the mirrors of these cases.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
