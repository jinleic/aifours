# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — (S0) type (6,9) with o0 = 7 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 08:59:25 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

This is v66 §4 (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`): layout (S0), type (6,9), **A = o0 = 7**, P = p0 in {7, 8, 9}, r0 = 2. Then l = 14-P, lam = 22-P, lam3 = 8+P and |T2| = 11+P. The rows are:
- B_0 = e7..e1, v, a1, a2, a3
- B_1 = a3..a_(l-1), w, b_(10+P)..b12
- B_2 = b12..b2
- B_3 = b2, b1, v, c1..c8
- D_0 = c8..c_(lam3-1), w, a_(l-1)..a4
- D_1 = a4..a1, v, b1..b6
- D_2 = b6..b16
- D_3 = b16..b_(10+P), w, e_(lam-1)..e7
- R_0 = c2, c1, v, e1..e8
- R_1 = e8..e_(lam-1), w, c_(lam3-1)..c12
- R_2 = c12..c2

The cuts are:
- P6: e7, a3, b12, b2, c8, a4, b6, b16;
- P2: e8, c12, c2.

Imports are as in v63 §1 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`): distinct cut labels, (F2), and (N) for v and for w. Also used are v52's four-row condition eps_w + X' = 1 (SHA256 `c7d0b41044cda03fb4879c2c2b89594665e2c13dccd52d8cf3aff6868443fc45`) and v49 rule (R) (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`).

## 2. Exchanges and first labels

- (Z1) R_0 vs B_0: {c1, c2, e8} = {a1, a2, a3}. The cut label a3 is not a P2 cut label, so **c1 = a3**. The edge T3[1]T3[2] may not repeat T1's {a2, a3}, so **c2 = a1 and e8 = a2**.
- (X1) B_0 vs D_1: {e1..e7} = {a4, b1..b6}.
- (X2) B_3 vs D_1: {c1..c8} = {a1..a4, b3..b6}, so {c3..c8} = {a2, a4, b3, b4, b5, b6}.
- (Z7) R_2 vs B_3: this is rule (R) with k = 4. The path b2, b1, v, a3 = T2[2], T2[1], b_v, T3[1] has the complementary P4 T3[9..12]. So **T3[9..12] is (v, b2, a3, b1) or (b1, a3, b2, v)**.
- (Z4) R_1 vs D_0: {e8..e_(lam-1)} = {c8..c11, a4..a_(l-1)}. Since e8 = a2, a2 lies in {c8..c11, a4..a_(l-1)}.
  - c8 is a P6 cut and a2 is the label of the P2 cut e8, so a2 ≠ c8.
  - c9..c11 lie in {v, b1, b2, a3}.
  - a4 shares D_1 with a2.
  - So **a2 is one of a5..a_(l-1)**, which needs l >= 6, i.e. **P <= 8**.
- (Z3) R_1 vs D_3: {c12..c_(lam3-1)} = {e7, b16..b_(10+P)}.
- (X3) B_2 vs D_2: {b2..b5} = {b13..b16}.
- (X9) B_2 vs D_1: {b7..b12} = {a1..a4, v, b1}.
- (X11) B_1 vs D_2: {b6..b11} = {a3..a_(l-1), w, b17..b_(10+P)}.

## 3. The w-cut is T2[6]

The P2 cuts carry a2, a1, and b1 or v, so none is w and eps_w = 0. By v52 the w-cut then lies in H2's w-run, at a D-row boundary. The candidates are:
- T1[4] (D_0|D_1) and T2[16] (D_2|D_3): impossible, because D_0 and D_3 already contain b_w;
- b_w(W) and b_w(W+25): impossible, since they are interior to D_0 and D_3.

So **b6 = w**. The w-vertices are therefore:
- b_w;
- T2[6];
- a T3 copy T3[t] with 3 <= t <= 7 (because (Z6), R_2 vs D_0, puts w in {c2..c7}, and c2 = a1);
- a T4 copy T4[i] with 1 <= i <= 6 (by (X1); e7 is a cut).

Moreover (X11) becomes {b7..b11} = {a3..a_(l-1), b17..b_(10+P)}.

## 4. The v-copies: two layouts

By (X9) there is a T2 v-copy T2[j] with 7 <= j <= 12; it serves B_2 and D_2. By §2 there is a T3 v-copy at T3[9] or T3[12]; it serves R_2 and D_0.

The third copy must serve D_3. It cannot lie on D_3's cut T2[16], since D_2 already has T2[j]. So it is a T2 copy in T2[17..10+P] or a T4 copy in T4[9..lam-1].
- **(alpha)** The third copy is on T4. Then B_1 can only get its v from j = 12, so T2[12] is the v-cut. Hence T3[12] ≠ v, and **T3[9..12] = (v, b2, a3, b1)**.
- **(beta)** The third copy is a T2 copy T2[j'] with 17 <= j' <= 10+P; it serves B_1 and D_3. Then R_1 needs T3[12] = v, the P2 v-cut, so **T3[9..12] = (b1, a3, b2, v)** and j <= 11.

## 5. (alpha) is impossible

**(N) for v.** The v-vertices are b_v, T2[12], T3[9] and T4[k]. Their neighbours carry:
- a1, b1, a3, e1 (b_v);
- b11, b13 (T2[12]);
- c8, b2 (T3[9]);
- e_(k-1), e_(k+1) (T4[k]).

These must be the ten labels other than v. Here:
- c8 is in {b3, b4, b5}. Of {c3..c8} = {a2, a4, b3, b4, b5, w}, the labels a2, a4 and w belong to the other cuts e8, T1[4] and T2[6].
- b13 is in {b3, b4, b5}: it lies in {b2..b5}, and b2 is already used.
- b11 is in {a2, a4}: by (X9) the labels of T2[7..11] are a1..a4 and b1, and a1, a3, b1 are used.
- e1 is in {a4, b3, b4, b5, w}.
- e_(k±1) is in {a2, a4, w}. By (Z4) the labels of T4[9..lam-1] are c8, v, b2, a3, a4 and the a5..a_(l-1) other than a2. By (X9) and (X11), those a5..a_(l-1) lie in {a1, a2, b1}.

Only c8, b13 and e1 can carry b3, b4, b5, so e1 is one of them and w = e_(k+1). Hence **k = lam-1** and {b11, e_(lam-2)} = {a2, a4}. T4[8] = a2 and T4[lam-2] both lie in R_1, so e_(lam-2) ≠ a2. Hence **e_(lam-2) = a4 and b11 = a2**.

**(N) for w.** The label a3 must neighbour a w-vertex. It cannot do so at:
- T3[t]: its neighbours lie in T3[2..8], whose labels are a1, a2, a4, b3, b4, b5, w;
- T4[i]: its neighbours lie in T4[0..7], whose labels are v, a4, b1..b5, w;
- T2[6]'s neighbour b5;
- b_w's neighbours a_(l-1) (in B_1 with T1[3]), b_(10+P) (one of b17..b_(10+P), which by (X11) lie outside a3..a_(l-1)), c_(lam3-1) (in {e7, b16..b_(10+P)}, where e7 is a T4[1..7] label and b16 is in {b2..b5}) and e_(lam-1) = v.

So **b7 = a3**. Then T2[8] carries a1, a4 or b1. It cannot carry a4, because {a3, a4} is the edge T1[3]T1[4], or a1, because {a3, a1} is T3[1]T3[2]. So **T2[8] = b1**. But {a3, b1} is already the edge T3[11]T3[12], a repeat. QED for (alpha).

## 6. (beta) is impossible

T2[12] is a P6 cut, not the v-cut. Its label is not a3 or a4 (P6 cut labels), a1 = c2 or a2 = e8 (P2 cut labels), so by (X9) **b12 = b1** and the labels of T2[7..11] are a1..a4 and v. (X11) then gives {a3..a_(l-1), b17..b_(10+P)} = {a1..a4, v}.
- **P = 8.** Here a5 = a2, so {b17, b18} = {v, a1}. These two vertices are adjacent, so {v, a1} repeats the edge b_v T1[1].
- **P = 7.** There is no T1 v-copy, so b17 = v and {a5, a6} = {a1, a2}. The edge T1[5]T1[6] then repeats {a1, a2} = T1[1]T1[2].

QED for (beta).

## 7. Result

**(S0) type (6,9) with o0 = 7 is impossible.** By v66's v<->w symmetry, so is its mirror, type (1,4) with p0 = 7.

The four/four shape remains open in (S0) only for:
- type (6,9) with A in {5, 6}, P in {7, 8, 9};
- type (9,6) with A in {8, 9, 10}, P in {6, 7, 8};
- the mirrors of these cases.

Other open lines are as in manifest v13-delta (SHA256 `fa811e9a0911c31382de72c0a85a04df55719f28cffbf7424f27d2552ac277da`).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
