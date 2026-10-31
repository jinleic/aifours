# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — x = 9 (Sigma = 21, 24) and Sigma = 21 with x = 8 are impossible

Actual `/bin/date` before this body: **Mon Oct 26 07:52:48 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result.

## 1. Setting and imports

The setting is the v56 survivor set (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`, read with v59, SHA256 `413003f4ce2b9349febccd794821dde011121c380df41bfe332dea29d3206222`): four/three shape, P2 shift d = 6, O inside T3, x = 15-o0 in {7, 8, 9}. Labels a_i, b_i, c_i, e_i are as in v61 (SHA256 `5dd3c58a33e185a94c8025cfb8213f8e68802e392bad379bf95ff283109cfa43`).

The imports are those of v63 §1 (SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`):
- rows are complete;
- cut labels are pairwise distinct;
- (F2) each unordered label pair lies on one edge, so a second occurrence is a repeat;
- (N) the ten neighbours of the four w-vertices carry the ten labels other than w, each once, and likewise for v.

## 2. x = 9 is impossible for Sigma = 21 and Sigma = 24 (set level)

For x = 9, the rows read off the v56/v61 formulas are as follows. Both Sigma values share:
- B_0 = e6..e1, v, a1..a4
- B_3 = b1, v, c1..c9
- O = c9..c19
- R_3 = c5..c1, v, e1..e5
- R_- = c15..c5

They differ in D_1 and the cuts:
- **Sigma = 21:** D_1 = a5..a1, v, b1..b5. The cuts are e6, a4, b11, b1, c9, c19, a5, b5 and c5, c15, e5.
- **Sigma = 24:** D_1 = a8..a1, v, b1, b2. The cuts are e6, a4, a14, b1, c9, c19, a8, b2 and c5, c15, e5.

In both, b1 = T2[1] is the B_2|B_3 cut and e5 = T4[5] is a P2 cut.

The exchanges are:
- B_0 vs R_3: {c1..c5} = {e6, a1, a2, a3, a4}.
- B_3 vs D_1: {c1..c9} = L(D_1) minus {v, b1}.
- R_- vs O: {c5..c8} = {c16..c19}.
- B_3 vs R_3: **{e1..e5} = {b1, c6, c7, c8, c9}**.

D_1 contains two further cut labels, z and z': a5 and b5 for Sigma = 21, a8 and b2 for Sigma = 24. They lie in L(D_1) minus {v, b1}, so in {c1..c9}. They are not among e6, a1..a4: e6 and a4 are other cuts, and a1..a3 share the row D_1 with them. So z and z' lie in {c6..c9}, and not on the cut c9; hence they lie in {c6, c7, c8}. The cut c19 lies in {c5..c8} and is not c5, so c19 also lies in {c6, c7, c8}. Therefore **{c6, c7, c8} = {z, z', c19}**.

Every label in {e1..e5} = {b1, z, z', c19, c9} is now the label of a cut other than T4[5]. Yet e5, the label of the cut T4[5], is in that set. This contradicts distinct cut labels. QED

## 3. Sigma = 21, x = 8: rows

Here l = 14-y, |T2| = 11+y, lam3 = 18+y, lam = 12-y, with y in {3, 4}. The rows are:
- B_0 = e7..e1, v, a1, a2, a3
- B_1 = a3..a_(l-1), w, b_(10+y)..b12
- B_2 = b12..b2
- B_3 = b2, b1, v, c1..c8
- O = c8..c18
- D_0 = c18..c_(17+y), w, a_(l-1)..a4
- D_1 = a4..a1, v, b1..b6
- D_2 = b6..b_(10+y), w, e_(11-y)..e7
- R_3 = c4..c1, v, e1..e6
- R_- = c14..c4
- R_+ = e6..e_(11-y), w, c_(17+y)..c14

The cuts are e7, a3, b12, b2, c8, c18, a4, b6 (P6) and c4, c14, e6 (P2). The b_w-neighbour labels are **a10, b13, c20, e8 (y = 3)** and **a9, b14, c21, e7 (y = 4)**.

## 4. Sigma = 21, x = 8: common steps

**Step 1.** B_0 vs R_3 gives {c1..c4} = {e7, a1, a2, a3}, and the cut c4 is a1 or a2. The path T3[0..4] may not repeat T1's pairs {v, a1}, {a1, a2}, {a2, a3}.
- If c4 = a1: c3 ≠ a2, and c3 = e7 would leave a2 and a3 adjacent. So c3 = a3, c2 = e7 and c1 = a2. This is **(alpha) T3[1..4] = a2, e7, a3, a1**.
- If c4 = a2: c3 is not a1 or a3, so c3 = e7; and c1 ≠ a1. This is **(beta) T3[1..4] = a3, a1, e7, a2**.

Write a-bar for a2 in (alpha) and a1 in (beta). Then c1..c3 = {e7, a3, a-bar}. The pairs used at e7 are {a2, e7}, {e7, a3} in (alpha) and {a1, e7}, {e7, a2} in (beta).

**Step 2.** B_3 vs D_1 gives {c1..c8} = {a1..a4, b3..b6}, and R_- vs O gives {c4..c7} = {c15..c18}. Hence {e7, c5, c6, c7, c8} = {a4, b3, b4, b5, b6}, and cut placement gives:
- **{c5, c6, c7} = {a4, b6, c18}**;
- **{b3, b4, b5} = {e7, c8, c18}**;
- {c15, c16, c17} = {c4, a4, b6}.

**Step 3.** B_2 vs D_2 gives {b2..b5} = {b13..b_(10+y), w, e7..e_(11-y)}. So {b2, c8, c18} is {b13, w, e8} (y = 3) or {b13, b14, w} (y = 4).
- c18 ≠ w, since D_0 holds T3[18] and b_w.
- For y = 3, also c18 ≠ e8, since R_+ holds T3[18] and T4[8]. So c18 = b13 and {b2, c8} = {w, e8}.

So **w is b2 or c8**. Let u be the other one.

**Step 4.** Four exchanges:
- B_1 vs D_0: {a3, b12..b_(10+y)} = {c18..c_(17+y)}.
- R_- vs B_3: {c9..c14} = {b1, b2, v, c1, c2, c3}.
- O vs R_+: {c8..c13} = {e6..e_(11-y), w, c19..c_(17+y)}.
- B_3 vs R_3: {e1..e6} = {b1, b2, c5..c8}.

In the last, b2, c8, a4, b6 and c18 are labels of other cuts, so **e6 = b1**. The cut labels b2, e7, a3 and b1 = e6 sit on non-cut vertices among T3[9..13]. So {c9..c13} = {b2, e7, a3, b1, q}, and the second exchange gives {q, c14} = {v, a-bar}. The third exchange becomes {c8, b2, a3, q} = {e8..e_(11-y), w, c19..c_(17+y)}:
- **y = 3:** {a3, q} = {c19, c20}, while the first exchange gives {a3, b12} = {c19, c20}.
- **y = 4:** {u, a3, q} = {c19, c20, c21}, and {u, c18} = {b13, b14}; so the first exchange gives {a3, b12, u} = {c19, c20, c21}.

Either way q = b12. So **{c9..c13} = {b2, e7, a3, b1, b12}** and **{b12, c14} = {v, a-bar}**.

**Step 5.** By the last exchange of Step 4, T4[1..5] carries b2, c8, a4, b6 and c18. D_0 vs R_+ gives {a4..a_(l-1)} = {e6..e_(11-y), c14..c17}, so {a5..a_(l-1)} = {b1, e7..e_(11-y), c14, c4, b6}. R_3 must hold w, while c1..c4 lie in {e7, a1, a2, a3} and e6 = b1. So one w-copy is **T4[k] with k <= 5**.

## 5. Sigma = 21, x = 8: w = c8 is impossible

T2[j] = w for some j in {3, 4, 5}, since {b3, b4, b5} = {e7, w, c18}.
- **y = 3** (b2 = e8, c18 = b13): j = 3 neighbours T2[2] = e8, and j = 4 has a neighbour carrying b13; both repeat a b_w pair. So j = 5, T2[4] = e7, T2[3] = b13 and T2[6] = b6.
- **y = 4:** j = 4 has a neighbour carrying e7, which repeats b_w T4[7]. j = 3 forces T2[4] = c18 and T2[5] = e7, so T2[3]'s neighbours carry b2 and c18, i.e. b13 and b14, and {w, b14} repeats. So j = 5, T2[4] = c18 and T2[3] = e7. Also c18 ≠ b14, so c18 = b13 and b2 = b14.

Then c7 is in {a4, b6, c18}. b6 already neighbours T2[5], and c18 = b13 neighbours b_w (y = 3) or T2[5] (y = 4). So **c7 = a4**.

T4[1..5] carries w, a4, b6, b13, and e8 (y = 3) or b14 (y = 4). Each of these four non-w labels already neighbours a w-vertex. Every k <= 5 gives T4[k] a neighbour inside T4[1..5] (T4[2] for k = 1, T4[4] for k = 5), so that edge repeats a pair. QED

## 6. Sigma = 21, x = 8: w = b2 is impossible

Then T2[2] is the w-cut and u = c8.
- **y = 3:** {b3, b4, b5} = {e7, e8, b13}. T2[3] carries neither e8 nor b13, so b3 = e7. b4 ≠ e8 (that would repeat T4[7]T4[8]), so b4 = b13 and b5 = e8. T2[2]'s neighbours carry b1 and e7.
- **y = 4:** {b3, b4, b5} = {e7, b13, b14}. b3 is neither e7 nor b14, so b3 = b13. b4 ≠ b14 (that would repeat T2[13]T2[14]), so b4 = e7 and b5 = b14. T2[2]'s neighbours carry b1 and b13.

In both cases the labels used by b_w and T2[2] include b1, e7, c8 and c18. Apply (N): {a_(l-1), c_(17+y), two O-copy neighbours, two T4[k]-neighbours} = {v, a1, a2, a3, a4, b6}. Here:
- **O-copy.** w = b2 lies in {c9..c13}, so T3[i] = w with 9 <= i <= 13. i ≠ 9, because T3[8] = c8 is used. The neighbours carry labels in {a3, b12, c14}, since e7 and b1 are used.
- **T4 copy.** T4[1..5] carries w, c8, a4, b6, c18, and T4[6] = b1. So T4[k]'s neighbours carry labels in {v, a4, b6}.
- a_(l-1) is in {c14, c4, b6} (Step 5 minus used labels).
- c_(17+y) is in {a3, b12} (for y = 4 the third option c8 is used).

The label c4 (the one of a1, a2 other than a-bar) can only be a_(l-1), because b12 and c14 are v and a-bar. So **a_(l-1) = c4**. Then a4 and b6 can only come from the T4 copy, so its neighbours carry a4 and b6. Hence {c_(17+y), O-copy neighbours} = {a3, b12, c14}:
- If c_(17+y) = a3, the O-copy neighbours carry b12 and c14, so i = 13 and T3[12] = b12.
- If c_(17+y) = b12, they carry a3 and c14, so i = 13 and T3[12] = a3.

So **T3[13] = w**, and T3[9..12] carry e7, a3, b1, b12.

**Placing e7.** e7 sits in T3[9..12], and both its neighbours lie in T3[8..13]. They cannot carry:
- c8: e8 (y = 3) repeats T4[7]T4[8]; b13 or b14 (y = 4) repeats T2[3]T2[4] or T2[4]T2[5];
- b1: repeats T4[6]T4[7];
- w: repeats T2[2]T2[3] (y = 3) or b_w T4[7] (y = 4).

Only a3 and b12 remain. In (alpha) the pair {e7, a3} is used, so both neighbours of e7 would have to carry b12, which only one vertex of T3[8..13] does; (alpha) is impossible. In (beta), e7's neighbours are a3 and b12. Since T3[12] is b12 or a3, this forces e7 = T3[11], T3[9] = b1 and {T3[10], T3[12]} = {a3, b12}. In (beta), a-bar = a1, c1 = a3 and {b12, c14} = {v, a1}.
- **c_(17+y) = a3, T3[12] = b12.**
  - If b12 = a1, the vertex T3[12] = a1 neighbours e7, which repeats T3[2]T3[3] = {a1, e7}.
  - If b12 = v, then T2[12] is a v-vertex next to T2[13] = b13. For y = 3, c19 = b12 = v neighbours c18 = b13: repeat. For y = 4, {c19, c20} = {v, c8}. A v at T3[19] neighbours c18 and c8, i.e. b13 and b14, which repeats {v, b13}. A v at T3[20] neighbours c21 = a3, which repeats b_v T3[1] = {v, a3}.
- **c_(17+y) = b12, T3[12] = a3, T3[10] = b12.**
  - If b12 = v, T3[10] neighbours T3[9] = b1, which repeats b_v T2[1].
  - If b12 = a1, T3[10] neighbours T3[11] = e7, which repeats {a1, e7}.

Every branch repeats a pair. QED

## 7. Result

**In the four/three shape, x = 9 is impossible for both Sigma = 21 and Sigma = 24 (by §2, at set level), and Sigma = 21 with x = 8 is impossible (§5-§6).** With v61-v63, the only remaining four/three survivor is **Sigma = 24 with x = 8 and y in {1, 2}**. Other open lines are as in manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
