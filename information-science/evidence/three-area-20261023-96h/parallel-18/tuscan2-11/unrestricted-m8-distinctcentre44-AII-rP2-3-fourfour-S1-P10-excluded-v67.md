# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — the (S1) family with p0 = 10 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 08:40:40 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

This is the v66 §6 survivor (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`): layout (S1) with kappa'' = 6, **P = p0 = 10** and A = o0 in {7, 8, 9, 10}. Then lam3 = 15-A, lam = 15+A, l = 11-A and |T2| = 14+A. The rows are:
- B_0 = e_A..e1, v, a1..a_(10-A)
- B_1 = a_(10-A), w, b_(13+A)..b_(5+A)
- B_2 = b_(5+A)..b_(A-5)
- S = b_(A-5)..b1, v, c1..c_(14-A), w
- D_1 = w, a_(10-A)..a1, v, b1..b_(A-1)
- D_2 = b_(A-1)..b_(A+9)
- D_3 = b_(A+9)..b_(13+A), w, e_(14+A)..e_(A+10)
- O = e_(A+10)..e_A
- R_0 = c_(14-A)..c1, v, e1..e_(A-4)
- R_1 = e_(A-4)..e_(A+6)
- R_2 = e_(A+6)..e_(14+A), w, c_(14-A)

Conventions: a_0 = v and a_l = w. For A = 10, T1 is the single edge b_v b_w.

The cuts are:
- P6: e_A, a_(10-A), b_(5+A), b_(A-5), b_w(W) (label w), b_(A-1), b_(A+9), e_(A+10);
- P2: c_(14-A), e_(A-4), e_(A+6).

The w-cut is b_w(W), so there are two w-copies on T3/T4 and one on T1/T2 (v47 §1 row formula with eps_w = 0). D_1 lists the eleven labels once each. The neighbours of b_w carry a_(10-A), b_(13+A), c_(14-A) and e_(14+A).

Imports are as in v63 §1 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`), including (N): the ten neighbour labels of the four w-vertices are the ten labels other than w.

## 2. Exchanges

Write `X vs Y: L = M` when the rows X and Y differ exactly by the label sets L and M.
- (U1) S vs R_0: {b1..b_(A-5), w} = {e1..e_(A-4)}.
- (U2) O vs R_2: {e_A..e_(A+5)} = {e_(A+11)..e_(A+14), w, c_(14-A)}.
- (U4) B_0 vs R_1: {e1..e_(A-5), v, a1..a_(10-A)} = {e_(A+1)..e_(A+6)}.
- (U5) B_0 vs R_0: {e_(A-3)..e_A, a1..a_(10-A)} = {c1..c_(14-A)}.
- (U8) S vs D_1: {c1..c_(14-A)} = {a1..a_(10-A), b_(A-4)..b_(A-1)}.
- (U10) B_2 vs D_2: {b_(A-5)..b_(A-2)} = {b_(A+6)..b_(A+9)}.
- (U11) B_2 vs S: {b_(A-4)..b_(A+5)} = {b1..b_(A-6), v, c1..c_(14-A), w}.
- (U13) B_1 vs D_2: {a_(10-A), w, b_(A+10)..b_(13+A)} = {b_(A-1)..b_(A+4)}.
- (U14) B_1 vs D_3: {a_(10-A), b_(5+A)..b_(8+A)} = {e_(A+10)..e_(14+A)}.

**The c_(14-A) clash.**
- By (U2), the P2 cut label c_(14-A) lies in {e_(A+1)..e_(A+5)}, since it is not e_A.
- By (U4) and (U1), the labels of T4[A+1..A+6] lie in {b1..b_(A-5), w, v, a1..a_(10-A)}.
- By (U8), c_(14-A) lies in {a1..a_(10-A), b_(A-4)..b_(A-1)}.

All these labels are D_1 labels, hence pairwise distinct, so c_(14-A) is in {a1..a_(10-A)}. It is not the P6 cut label a_(10-A), so **c_(14-A) lies in {a1..a_(9-A)}**. This set is empty for A >= 9. **So A = 9 and A = 10 are impossible.**

## 3. A = 8 is impossible

Here c6 = a1. Also:
- T4[1..4] carries b1, b2, b3 and w (U1).
- T4[9..14] carries e1, e2, e3, v, a1 and a2 (U4), and {e1, e2, e3} lies in {b1, b2, b3, w}.
- e8 lies in {b4..b7}, by (U5) and (U8).
- T2[8..13] carries {b1, b2, v, w, a1, a2}, by (U11) and (U8).
- e22 lies in {b13..b16}, by (U14), since e22 and a2 are both b_w-neighbour labels. Also {b14, b15, b16} lies in {b3..b6} (U10).
- b21 lies in {b7..b12} (U13), so b21 is not in {b4, b5, b6}.

The four w-vertices are:
- b_w;
- T4[i1] with i1 <= 3 (U1, since e4 is a P2 cut);
- T4[i2] with 9 <= i2 <= 13 (U2);
- T2[j] with 8 <= j <= 12 (U13, since b7 is a cut).

Their neighbours can carry labels from {b4, b5, b6} only in these places:
- T4[i1] meets T4[0..4]: none there.
- T4[i2] meets T4[8..14]: only T4[8] = e8.
- T2[j] meets T2[7..13]: none.
- b_w meets a2, b21, c6 = a1 and e22: only e22.

So at most two of b4, b5, b6 are w-neighbour labels, contradicting (N). QED for A = 8.

## 4. A = 7 is impossible

Here c7 is a1 or a2. Also:
- T4[1..3] carries b1, b2 and w: by (U1), e3 = b1 and {e1, e2} = {b2, w}.
- T4[8..13] carries b2, w, v, a1, a2 and a3 (U4).
- e7 lies in {b3..b6}, by (U5) and (U8).
- T2[7..12] carries {b1, v, w, a1, a2, a3}, by (U11) and (U8).
- b20 lies in {b6..b11} (U13).
- e21 lies in {b12..b15} (U14). Here b12 is a T2[7..12] label, and {b13, b14, b15} lies in {b2..b5} (U10).

The w-vertices are:
- b_w;
- T4[i1] with i1 <= 2;
- T4[i2] with 8 <= i2 <= 12;
- T2[j] with 7 <= j <= 11 (U13, since b6 is a cut).

Neighbour labels in {b3, b4, b5, b6} can arise only as follows:
- T4[i1] meets T4[0..3]: none.
- T4[i2] meets T4[7..13]: only e7.
- T2[j] meets T2[6..12]: only b6.
- b_w meets a3, b20, c7 and e21: b20 can be b6, and e21 can be one of b3, b4, b5.

b6 can be counted only once, so at most three of these four labels occur, contradicting (N). QED for A = 7.

## 5. Result

**The (S1) four/four family with p0 = 10 (kappa'' = 6, A = 7..10) is impossible.** With v66, the four/four shape of distinct-centre 4+4 (a)-II with r_P2 = 3 is open only in:
- (S1) with A = 5 and P in {6, 7, 8} (kappa'' = 4), and its mirror layout;
- (S0) type (6,9) with A in {5, 6, 7} and P in {7, 8, 9};
- (S0) type (9,6) with A in {8, 9, 10} and P in {6, 7, 8};
- the v<->w mirrors of the two (S0) types.

Other open lines are as in manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
