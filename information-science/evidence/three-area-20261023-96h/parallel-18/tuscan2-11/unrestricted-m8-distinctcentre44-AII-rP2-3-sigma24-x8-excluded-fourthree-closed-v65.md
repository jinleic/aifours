# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 — Sigma = 24 with x = 8 is impossible, closing the four/three shape

Actual `/bin/date` before this body: **Mon Oct 26 07:57:13 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result.

## 1. Setting

This is the last four/three survivor left by v64 (SHA256 `09d2025a07f6cfe6519b9c73a97436271cce888c577ffa9940aeb1171d44839e`): v56 shape, P2 shift d = 6, O inside T3, **Sigma = 24, x = 8** (o0 = 7), y in {1, 2}. Then l = 17-y, |T2| = 8+y, lam3 = 18+y and lam = 12-y. With the labels of v61 (SHA256 `5dd3c58a33e185a94c8025cfb8213f8e68802e392bad379bf95ff283109cfa43`), the rows are:
- B_0 = e7..e1, v, a1, a2, a3
- B_1 = a3..a13
- B_2 = a13..a_(l-1), w, b_(7+y)..b2
- B_3 = b2, b1, v, c1..c8
- O = c8..c18
- D_0 = c18..c_(17+y), w, a_(l-1)..a7
- D_1 = a7..a1, v, b1, b2, b3
- D_2 = b3..b_(7+y), w, e_(11-y)..e7
- R_3 = c4..c1, v, e1..e6
- R_- = c14..c4
- R_+ = e6..e_(11-y), w, c_(17+y)..c14

The cuts are e7, a3, a13, b2, c8, c18, a7, b3 (P6) and c4, c14, e6 (P2). The b_w-neighbour labels are **a15, b8, c18, e10 (y = 1)** and **a14, b9, c19, e9 (y = 2)**. The imports are those of v63 §1 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`), including (N).

## 2. Common steps

**Step 1.** B_0 and R_3 have the same ends as in v64 Step 1, so T3[1..4] is **(alpha) a2, e7, a3, a1** or **(beta) a3, a1, e7, a2**. Write a-bar = a2 in (alpha) and a1 in (beta).

**Step 2.** B_3 vs D_1 gives {c1..c8} = {a1..a7, b3}, and R_- vs O gives {c4..c7} = {c15..c18}. Hence {e7, c5, c6, c7, c8} = {a4, a5, a6, a7, b3}, and cut placement gives:
- **{c5, c6, c7} = {a7, b3, c18}**;
- **{a4, a5, a6} = {e7, c8, c18}**;
- {c15, c16, c17} = {c4, a7, b3}.

**Step 3.** B_1 vs D_0 gives {a3, a4, a5, a6} = {a14..a_(l-1), w, c18..c_(17+y)}, so {a3, e7, c8} is {a14, a15, w} (y = 1) or {a14, w, c19} (y = 2). e7 ≠ w, since D_2 holds T4[7] and b_w. So **w is a3 or c8**.

**Step 4.** Four exchanges:
- B_3 vs R_3: {e1..e6} = {b1, b2, a7, b3, c18, c8}. All but b1 are labels of other cuts, so **e6 = b1**, and T4[1..5] carries b2, a7, b3, c18, c8.
- R_- vs B_3: {c9..c14} = {b1, b2, v, e7, a3, a-bar}.
- O vs R_+: {c8..c13} = {e6..e_(11-y), w, c19..c_(17+y)}.
- B_2 vs D_2: {a13..a_(l-1), b2} = {e7..e_(11-y)}.

As in v64 Step 4, {c9..c13} = {b2, e7, a3, b1, q} with {q, c14} = {v, a-bar}. Also {c8, b2, a3, q} is {e8, e9, e10, w} (y = 1) or {e8, e9, w, c19} (y = 2).
- **w = c8:** y = 1 gives {a3, e7} = {a14, a15}, so {a13, a3, b2} = {e8, e9, e10} = {b2, a3, q}. For y = 2, c19 ≠ e7 because R_+ holds T3[19] and T4[7]. So a14 = e7, c19 = a3 and {a13, b2} = {e8, e9}, while {b2, q} = {e8, e9}.
- **w = a3:** y = 1 gives {e7, c8} = {a14, a15}, so {a13, c8, b2} = {e8, e9, e10} = {c8, b2, q}. For y = 2, again a14 = e7, so c19 = c8, {a13, b2} = {e8, e9} and {b2, q} = {e8, e9}.

So in every case **q = a13**: {c9..c13} = {b2, e7, a3, b1, a13} and **{a13, c14} = {v, a-bar}**.

**Step 5.** The alphabet (from D_1) is {v, w, a1, a2, b1, b2, b3, a7, e7, c18} plus whichever of a3, c8 is not w. D_2 vs R_+ gives {b3..b_(7+y)} = {e6, c14..c_(17+y)}, so {b4..b_(7+y)} = {b1, c14, c4, a7, c18, c19..c_(17+y)}.

## 3. w = c8 is impossible

The w-vertices are b_w, the cut T3[8], a copy T1[j] with a_j = c8 (j in {4, 5, 6}, by Step 2), and a copy T4[k] with k <= 5 (R_3 needs w; c1..c4 avoid w and e6 = b1).

**Placing T1[j].**
- **y = 2.** a14 = e7 and c19 = a3 are b_w-neighbour labels. j = 4 neighbours T1[3] = a3, and j = 5 neighbours a vertex carrying e7. So j = 6, T1[5] = c18, T1[4] = e7, and T1[3..7] = a3, e7, c18, w, a7.
- **y = 1.** c18 is a b_w-neighbour label, and a15 is a3 or e7. j = 5 neighbours c18. j = 4 forces T1[5] = e7, so its neighbours carry a3 and e7, one of which is a15. So j = 6, T1[5] = e7 and T1[4] = c18. Then a15 ≠ e7, so a15 = a3 and a14 = e7. T1[3..7] = a3, c18, e7, w, a7.

In both cases a14 = e7, and a3, e7, c18, a7 are used w-neighbour labels. c7 is in {a7, b3, c18}, so **c7 = b3**. By (N):
- {b_(7+y), e_(11-y), c9, two T4[k]-neighbours} = {v, a1, a2, b1, b2}.

Here:
- c9 is in {b2, b1, a13}.
- T4[1..5] carries w, b2, a7, b3, c18, and T4[6] = b1. So the T4 neighbours are {v, b2} (k = 1, T4[2] = b2) or {b2, b1} (k = 5, T4[4] = b2); other k are impossible.
- b_(7+y) is in {b1, c14, c4} (Step 5 minus used labels).
- e_(11-y) is in {a13, b2}. For y = 1, {a13, a3, b2} = {e8, e9, e10}, and e10 ≠ a3 because a3 = a15 already neighbours b_w. For y = 2, {a13, b2} = {e8, e9}.

The label c4 (the one of a1, a2 other than a-bar) can only be b_(7+y), so b_(7+y) = c4. Both T4 options contain b2, so e_(11-y) = a13 and c9 = b1. Hence the T4 neighbours are {v, b2}, k = 1, **a13 = a-bar and c14 = v**.

**e7's used pairs.** {a13, e7} lies on T1[13]T1[14]. {a3, e7} lies on T1[3]T1[4] (y = 2) or T1[14]T1[15] (y = 1). So **(alpha)**, whose T3[2]T3[3] is {e7, a3}, **is impossible**.

In **(beta)**, a13 = a1 and T3[9] = c9 = b1. e7 lies in T3[10..13], and its neighbours carry labels from {b1, b2, a3, a1, v}:
- b1 repeats T4[6]T4[7];
- a3 and a1 repeat T1 pairs;
- b2 repeats T4[7]T4[8] whenever e8 = b2, which always holds for y = 2 (e9 = a13 forces e8 = b2).

So if e8 = b2 (always for y = 2) only v is left, which is impossible. Otherwise y = 1 and e8 = a3, and e7 must be T3[13] (next to T3[14] = v) with T3[12] = b2. Then T3[10], T3[11] carry a3 and a1, and that edge repeats T3[1]T3[2] = {a3, a1}. QED

## 4. w = a3 is impossible

The w-vertices are b_w, the cut T1[3], the T3 copy from Step 1 (T3[3] in (alpha), T3[1] in (beta)), and the O-copy T3[i] with 9 <= i <= 13 (w = a3 lies in {c9..c13}). That makes four, so T4 holds no w. T1[3]'s neighbours carry a2 and a4. Also a4 is in {e7, c8, c18}.
- **y = 2.** By Step 4, a14 = e7 and c19 = c8 are b_w-neighbour labels.
  - (alpha) puts e7 next to T3[3] = w, which is a repeat.
  - In (beta), T3[1]'s neighbours carry v and a1, and a4 = c18 (e7 and c8 are b_w-neighbour labels). By (N), {b9, e9, O-copy neighbours} = {b1, b2, b3, a7}. Since {a13, b2} = {e8, e9} and a13 is v or a1, **e9 = b2**.
- **y = 1.** {e7, c8} = {a14, a15}, and c18 is a b_w-neighbour label.
  - (alpha): T3[3]'s neighbours carry e7 and a1, so a4 = c8. Then a15, which is e7 or c8, repeats.
  - (beta): T3[1]'s neighbours carry v and a1. a4 is e7 or c8 and is not a15, so {a4, a15} = {e7, c8}. By (N), {b8, e10, O-copy neighbours} = {b1, b2, b3, a7}. Since {a13, c8, b2} = {e8, e9, e10}, **e10 = b2**.

In both (beta) cases, the O-copy's neighbours lie in T3[8..14]:
- T3[8] = c8 and T3[14] = c14 (v or a1) carry used labels, so 10 <= i <= 12.
- The other labels there are b2, e7, b1 and a13; of these, e7, a13 and b2 are used.

So only b1 is available, and the O-copy cannot have two neighbours. QED

## 5. Result

**Sigma = 24 with x = 8 is impossible.** Together with v61 (Sigma = 24, x = 7), v62 (Sigma = 26), v63 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`; Sigma = 21, x = 7) and v64 (x = 9; Sigma = 21, x = 8), **every v56/v59 survivor of the four/three shape is excluded**.

So, as WRITTEN, unreviewed work: distinct-centre 4+4, class (a)-II with r_P2 = 3, is impossible in the four/three shape. The written layer of manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) then leaves (a)-II open only in the four/four shape at Sigma = 21 (its R2). R3-R6 are unchanged.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
