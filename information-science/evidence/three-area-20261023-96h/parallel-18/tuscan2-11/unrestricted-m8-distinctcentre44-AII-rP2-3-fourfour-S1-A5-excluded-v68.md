# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — the (S1) family with o0 = 5 is impossible, closing (S1)

Actual `/bin/date` before this body: **Mon Oct 26 08:42:12 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

This is the last (S1) survivor of v66 §6 (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`): kappa'' = 4, **A = o0 = 5**, P = p0 in {6, 7, 8}. Then lam3 = P, lam = 30-P, l = 16-P and |T2| = 9+P.

The P2 cuts are T3[1], T4[9] and T4[19]. The rows are:
- B_0 = e5..e1, v, a1..a5
- B_1 = a5..a_(l-1), w, b_(8+P)..b10
- B_2 = b10..b1, v
- S = v, c1..c_(P-1), w, a_(l-1)..a6
- D_1 = a6..a1, v, b1..b4
- D_2 = b4..b14
- D_3 = b14..b_(8+P), w, e_(29-P)..e15
- O = e15..e5
- R_0 = c1, v, e1..e9
- R_1 = e9..e19
- R_2 = e19..e_(29-P), w, c_(P-1)..c1

The cuts are:
- P6: e5, a5, b10, b_v(25) (label v), a6, b4, b14, e15;
- P2: c1, e9, e19.

So **the v-cut is b_v(25)**. By the v47 §1 row formula with eps_v = 0, there are two v-copies on T3/T4 and one on T1/T2. Imports are as in v63 §1 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`), including (N) for v.

## 2. The four v-vertices

- **R_0 vs B_0** gives {c1, e6..e9} = {a1..a5}. The P2 cut label c1 is not the P6 cut label a5, so **c1 ≠ a5**.
- **R_0 vs O** gives: T4[10..15] carries {c1, v, e1..e4}. T4[15] is a cut whose label is not v, so there is a v-copy **T4[k1] with 10 <= k1 <= 14**.
- **R_2 vs S** gives: T4[19..29-P] carries {v, a6..a_(l-1)}. T4[19] is a P2 cut, not the v-cut, so there is a v-copy **T4[k2] with 20 <= k2 <= 29-P**.
- **B_2 vs D_2** gives {v, b1, b2, b3} = {b11..b14}. By rule (R) with k = 4 (v49 §4), T2[11..14] is the complementary P4 of T2[0..3] = v, b1, b2, b3, so it reads b2, v, b3, b1 or b1, b3, v, b2. In either case there is a **v-copy T2[j]** (j = 12 or 13), and its neighbours carry b2 and b3.

These are b_v and its three copies, so they are all four v-vertices.

## 3. The label a5 is not a v-neighbour label

Check each v-vertex:
- **b_v** has neighbours a1, b1, c1 and e1. The labels a1 and b1 differ from a5 because D_1 lists labels once. c1 ≠ a5 by §2. e1 ≠ a5 because T4[1] and T1[5] both lie in B_0.
- **T2[j]** has neighbours b2 and b3, which are D_1 labels different from a5.
- **T4[k1]** has its neighbours in T4[9..15]. T4[9] carries the P2 cut label e9, which is not the P6 cut label a5. The labels of T4[10..15] are c1, v and e1..e4, and e1..e4 share the row B_0 with T1[5].
- **T4[k2]** has its neighbours in T4[19..30-P]. T4[19] carries the P2 cut label e19. The labels of T4[20..29-P] lie in {v, a6..a_(l-1)}, and a6..a_(l-1) share the row B_1 with T1[5]. T4[30-P] = b_w, and w ≠ a5 because B_1 contains both T1[5] and b_w.

So no edge at a v-vertex carries {v, a5}. This contradicts (N), which needs all ten labels other than v among the v-neighbour labels. QED

## 4. Result

**The (S1) family with o0 = 5 (kappa'' = 4, P in {6, 7, 8}) is impossible.** With v67 (SHA256 `a489d4b4ad64856d5f130dcf5598b0d1a70e8de4b13c11dfde60a219b251a24f`) and v66 §6, **the entire s = o = 1 part of the four/four shape is excluded**: (S1), and by v<->w its mirror layout B_0 = D_3.

The four/four shape is now open only in (S0):
- type (6,9) with A in {5, 6, 7} and P in {7, 8, 9};
- type (9,6) with A in {8, 9, 10} and P in {6, 7, 8};
- their v<->w mirrors (1,4) and (4,1).

Other open lines are as in manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
