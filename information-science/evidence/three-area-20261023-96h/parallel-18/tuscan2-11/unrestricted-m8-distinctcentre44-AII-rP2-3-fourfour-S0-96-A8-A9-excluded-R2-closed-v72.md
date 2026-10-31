# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — (S0) type (9,6) with o0 = 8, 9 is impossible; the four/four shape is closed

Actual `/bin/date` before this body: **Mon Oct 26 09:27:31 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting and tools

This is v66 §5 (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`): (S0), type (9,6), r0 = 16-A, with **A in {8, 9}** and P in {6, 7, 8}. The rows and cuts are those of v66 §2 and §5 with A substituted.

The tools are:
- distinct cut labels;
- (F2), under which a second occurrence of a pair is a repeat;
- rule (R) (v49 §4);
- (N) for v and for w (v63 §1, SHA256 `5a495a2be842c863435f53812a830502ace03e1ce582a1f57e2878f5166f67aa`);
- v52's four-row conditions eps_v + X = 1 and eps_w + X' = 1.

Exchanges are written `X vs Y: L = M`.

## 2. o0 = 8

Here l = 13-P, lam = 23-P, lam3 = 7+P and |T2| = 12+P. The rows are:
- B_0 = e8..e1, v, a1, a2
- B_1 = a2..a_(l-1), w, b_(11+P)..b13
- B_2 = b13..b3
- B_3 = b3, b2, b1, v, c1..c7
- D_0 = c7..c_(lam3-1), w, a_(l-1)..a3
- D_1 = a3, a2, a1, v, b1..b7
- D_2 = b7..b17
- D_3 = b17..b_(11+P), w, e_(lam-1)..e8
- R_0 = c8..c1, v, e1, e2
- R_1 = e2..e12
- R_2 = e12..e_(lam-1), w, c_(lam3-1)..c8

The cuts are:
- P6: e8, a2, b13, b3, c7, a3, b7, b17;
- P2: e2, e12, c8.

**2.1 First labels.**
- R_0 vs B_3 gives {c8, e1, e2} = {b1, b2, b3}. The P2 cut labels e2 and c8 are not b3, so **e1 = b3**. The edge T4[1]T4[2] may not repeat T2[2]T2[3] = {b2, b3}, so **e2 = b1 and c8 = b2**.
- R_1 vs B_0 is rule (R) with k = 4. So T4[9..12] is the complementary P4 of (a2, a1, v, b3) = T1[2], T1[1], b_v, T4[1]. It reads **(v, a2, b3, a1) or (a1, b3, a2, v)**.
- Hence all six pairs of {v, a1, a2, b3} are used: **a saturated K4**.
- Further exchanges:
  - B_0 vs D_1: {e1..e8} = {a3, b1..b7}.
  - B_3 vs D_1: {c1..c7} = {a1, a2, a3, b4..b7}.
  - R_0 vs B_0 with the above: {e3..e8} = {a3, b2, b4, b5, b6, b7}.
  - B_2 vs D_2: T2[14..17] is the complementary P4 of b3, b4, b5, b6. Its pairs are {b3,b5}, {b3,b6}, {b4,b6}, and b14, b17 lie in {b4, b5}.
  - B_2 vs D_1: {b8..b13} = {a1, a2, a3, v, b1, b2}.
  - B_1 vs D_2: {a2..a_(l-1), w, b18..b_(11+P)} = {b7..b12}.
  - R_2 vs D_0: {e12..e_(lam-1)} = {c7, a3..a_(l-1)}.
  - R_2 vs D_3: {c8..c_(lam3-1)} = {b17..b_(11+P), e8..e11}.
- e8 is a P6 cut, and a3, b7 (P6) and b2 = c8 (P2) are other cuts' labels, so **e8 is in {b4, b5, b6}**. Also **c1 is in {a3, b4..b7}**: c1 ≠ a1 because of b_v's edges, and c1 ≠ a2 because {v, a2} is used.

**2.2 The w-cut.** The P2 cuts e12 and c8 lie in R_2, which contains b_w, so neither can be the w-cut. So either e2 = b1 is the w-cut (**w = b1**), or eps_w = 0 and the w-cut is the D_1|D_2 cut T2[7] (**w = b7**). The other D-boundaries T1[3] and T2[17] fail as in v69 §3.

**2.3 v-layouts.**
- **(o1)** T4[9..12] = (v, a2, b3, a1). Then T4[9] is not a cut, so eps_v = 0. By v52 the v-cut is the B_1|B_2 cut, **b13 = v**. The remaining copy serves D_0 and R_2, so it is a T3 copy T3[t] with t >= 9.
- **(o2)** T4[9..12] = (a1, b3, a2, v). Then T4[12] is the P2 v-cut. The other copies are a T2 copy T2[j] with 8 <= j <= 12 (serving B_2 and D_2) and a T1 copy T1[i] with i >= 4 (serving B_1 and D_0).

**2.4 (o2) is impossible.**
- b13 is a P6 cut. It is not v, a2, a3 (cut labels), b1 = e2 or b2 = c8, so b13 = a1.
- The neighbours of T2[j] then carry labels in {b7, a2, a3, b1, b2, a1}. Removing the used a1, a2, b1 leaves **{b7, a3, b2}**.
- By B_1 vs D_2, the labels a4..a_(l-1) lie in {b7, v, b1, b2}. So T1[i]'s neighbours carry labels in {a3, b7, v, b1, b2, w}.
- Hence b4, b5, b6 can be v-neighbour labels only as c1 or as e13. e13 lies in {c7, a3..a_(l-1)}, and c7 is in {a1, b4, b5, b6}.
- So at most two of b4, b5, b6 occur, contradicting (N) for v.

**2.5 (o1) is impossible.**
- Here e12 = a1. R_2 vs D_0 then puts a1 among a4..a_(l-1).
- R_2 vs D_3 puts c8 = b2 among b18..b_(11+P), since b17 is in {b4, b5} and e8 ≠ b2. So **P >= 7**.
- B_2 vs D_1 with b13 = v gives T2[8..12] = {a1, a2, a3, b1, b2}.
- B_1 vs D_2 gives {a4..a_(l-1), w, b18..b_(11+P)} = {b7, a1, b1, b2}.

**(N) for v.** The v-vertices are b_v (neighbour labels a1, b1, c1, b3), T2[13] (b12, b14), T4[9] (e8, a2) and T3[t]. So **{c1, e8, b12, b14, c_(t-1), c_(t+1)} = {a3, b2, b4, b5, b6, b7}**. Here:
- b12 is in {a3, b2};
- the labels of T3[t]'s neighbours lie in {b2, b17, b7, w}.

**P = 7.** Here l = 6, so b18 = b2 is b_w's T2-neighbour.
- **w = b1:** T2[1] = w neighbours T2[2] = b2, which repeats {w, b2}.
- **w = b7:** T2[7] is the w-cut, w-copies are T3[t'] (t' <= 6) and T4[i'] (3 <= i' <= 7), and {a4, a5} = {a1, b1}. R_2 vs D_0 gives {e13, e14, e15} = {c7, a3, b1}. By the (N)-for-v equation, either:
  - **(X)** c1 = a3, e8 = b6, b12 = b2, and T3[12..13] = (b17, v) next to b_w. Then b3 is not a w-neighbour label. b_w's neighbours carry a5 (a1 or b1), b2, v and e15 (c7, a3 or b1, with c7 in {b4, b5, b6}). T2[7]'s carry b6 and b8 (in {a1, a2, a3, b1}). T3[t'] meets labels a3, a1, a2, b4, b5, b6, w, and T4[i'] meets b1, a3, b2, b4, b5, b6, w. This contradicts (N) for w.
  - **(Y)** c1 = w, b12 = a3, e8 = b6, and T3[9..10] = (v, b17). Then (N) for w forces b3 = c13. But T3[12] next to T3[13] = b3 cannot be a2 ({a2, b3} = T4[10]T4[11]), so T3[12] = b6. Then {b6, b3} repeats the T2 complement.

  The remaining placements of c1 fail the same equation: c1 = b6 or c1 in {b4, b5} would need T3[t] next to both T3[8] = b2 and b_w.

**P = 8.** Here l = 5, a4 = a1, {w, b18, b19} = {b7, b1, b2}, and R_2 vs D_0 gives {e13, e14} = {c7, a3}.
- **w = b1.** b19 ≠ b2 (that would repeat {w, b2}), so b19 = b7 and b18 = b2.
  - (N) for w forces the neighbours of the T2 w-copy T2[j'] (8 <= j' <= 11) to carry a2 and a3. It also forces {c14, e14, e3} = {b4, b5, b6}.
  - T2[8] is not w, since its neighbour T2[7] = b7 is not a2 or a3. Nor is it b2, since {b7, b2} = T2[18]T2[19]. j' = 9 and j' = 10 repeat {a1, a2} or {a1, a3} (T1 pairs, as a4 = a1), so **T2[8..13] = (a1, b2, a2, w, a3, v)**.
  - Then b12 = a3, so c1 ≠ a3 and T3[9] = v, with T3[10] in {b17, b7} and T3[14] in {b17, e8}.
  - The label b3 sits in T3[11..13]. Its neighbours there may carry only b7, because {b3, b17}, {b3, e8} (T2 path/complement pairs) and {b3, a2} (T4) are used. Contradiction.
- **w = b7.** {b18, b19} = {b1, b2}.
  - (N) for w forces c14 = b3. Then no T3 v-copy neighbours b_w, so (N) for v needs **c1 = w**.
  - Then the (N)-for-v equation gives b12 = a3, T3[9..10] = (v, b17) and e8 = b6. T3[13] carries b1, b6 or a2.
  - {b3, b1} = T4[1]T4[2], {b3, b6} (T2 complement) and {b3, a2} (T4) are all used. Contradiction.

## 3. o0 = 9

Here l = 12-P, lam = 24-P, lam3 = 6+P and |T2| = 13+P. The rows are:
- B_0 = e9..e1, v, a1
- B_1 = a1..a_(l-1), w, b_(12+P)..b14
- B_2 = b14..b4
- B_3 = b4..b1, v, c1..c6
- D_0 = c6..c_(lam3-1), w, a_(l-1)..a2
- D_1 = a2, a1, v, b1..b8
- D_2 = b8..b18
- D_3 = b18..b_(12+P), w, e_(lam-1)..e9
- R_0 = c7..c1, v, e1, e2, e3
- R_1 = e3..e13
- R_2 = e13..e_(lam-1), w, c_(lam3-1)..c7

The cuts are:
- P6: e9, a1, b14, b4, c6, a2, b8, b18;
- P2: e3, e13, c7.

**3.1 First labels.**
- R_0 vs B_3 gives {c7, e1, e2, e3} = {b1..b4}.
- R_1 vs B_0 (rule (R), k = 4): T4[10..13] is the complementary P4 of (a1, v, e1, e2). It reads **(e1, a1, e2, v) or (v, e2, a1, e1)**, so the T4 v-copy neighbours e2.
- e1 ≠ b1 (b_v's edges) and e2 ≠ b1 ({v, b1} is used). {e1, e2} is an edge, so it is not a T2 path pair. Hence {e1, e2} = {b2, b4}.
- T4[2]T4[3] = {e2, e3} is not a T2 path pair. So **e1 = b2, e2 = b4, e3 = b1 and c7 = b3**.
- **{v, a1, b2, b4} is a saturated K4.**
- Further exchanges:
  - B_0 vs D_1: {e1..e9} = {a2, b1..b8}, so {e4..e9} = {a2, b3, b5, b6, b7, b8}, and the P6 cut e9 is in {b5, b6, b7}.
  - B_3 vs D_1: {c1..c6} = {a1, a2, b5..b8}, with c1 ≠ a1.
  - B_2 vs D_2: T2[15..18] is the complementary P4 of b4..b7. Its pairs are {b4,b6}, {b4,b7}, {b5,b7}, and b15, b18 lie in {b5, b6}.
  - B_2 vs D_1: {b9..b14} = {a1, a2, v, b1, b2, b3}.
  - B_1 vs D_2: {a1..a_(l-1), w, b19..b_(12+P)} = {b8..b13}.
  - R_2 vs D_0: {e13..e_(lam-1)} = {c6, a2..a_(l-1)}.
  - R_2 vs D_3: {c7..c_(lam3-1)} = {b18..b_(12+P), e9..e12}.
- **The w-cut.** As in §2.2, either w = b1 (e3 = b1 is the w-cut), or w = b8 (the D_1|D_2 cut T2[8]).

**3.2 Layout T4[13] = v (the P2 v-cut) is impossible.**
- The other copies are T2[j] (9 <= j <= 13) and a T1 copy T1[i] with i >= 3.
- b14 is a P6 cut. By B_2 vs D_1 its candidates are a1, a2, b1, b2 and b3 (not v, since the v-cut is T4[13]). Of these, a1, a2, b1 = e3 and b3 = c7 are other cuts' labels, so b14 = b2 and T2[9..13] = {a1, a2, v, b1, b3}.
- The neighbours of T2[j] carry labels in {b8, a2, b3}. By B_1 vs D_2, the labels a3..a_(l-1) lie in {b8, v, b1, b3}, so T1[i]'s neighbours carry labels in {a2, b8, b1, b3, w}.
- So b5, b6, b7 can occur as v-neighbour labels only as c1 and e14 (via c6). That is at most two of three, contradicting (N) for v.

**3.3 Layout T4[10] = v is impossible.**
- Here T4[10..13] = (v, b4, a1, b2) and eps_v = 0, so **b14 = v** is the v-cut. The third copy is T3[t] with t >= 8.
- T2[9..13] = {a1, a2, b1, b2, b3}.
- R_2 vs D_3 places c7 = b3 among b19..b_(12+P), so **P >= 7**.
- B_1 vs D_2 gives {a3..a_(l-1), w, b19..b_(12+P)} = {b8, b1, b2, b3}.

**(N) for v.** **{c1, b13, b15, e9, c_(t-1), c_(t+1)} = {a2, b3, b5, b6, b7, b8}**, where:
- b13 is in {a2, b3};
- b15 is in {b5, b6};
- e9 is in {b5, b6, b7};
- T3[t]'s neighbours carry labels in {b3, b18, b8, w}.

**w = b1.** Then T2[1] = w, and T4[3] = w is the P2 w-cut.
- (N) for w forces {a_(l-1), b_(12+P)} = {b8, b3}, the T2 w-copy T2[j'] (9 <= j' <= 13) to have neighbours a1 and a2, and {e4, c_(lam3-1), e_(lam-1)} = {b5, b6, b7}.
- Both neighbours of T2[j'] lie in T2[9..13], so j' is 10, 11 or 12. j' = 10 and j' = 12 repeat {b2, b3} = T2[2]T2[3]. So j' = 11, and since {a1, b2} is in the K4, **T2[8..14] = (b8, b2, a2, w, a1, b3, v)**.
- Then b13 = b3 forces c1 = a2, e9 = b7, and T3[t]'s neighbours carry b18 and b8.
- For P = 7, no T3 vertex next to T3[t] can carry b8.
- For P = 8, {b19, b20} = {b3, b8}, and T3[8..13] carries b18, b7, v, b4, a1, b8. The label b4 may neighbour only b8 there:
  - {b4, v}, {b4, a1} are used in the K4;
  - {b4, b7} and {b4, b5}/{b4, b6} are used on T2;
  - {b4, b3} = T2[3]T2[4];
  - {b4, w} = T4[2]T4[3].

  But b4 cannot be at an end of T3[8..13]: the ends neighbour T3[7] = b3 and b_w. Contradiction.

**w = b8.** Then T2[8] is the w-cut, and the w-copies are T3[t'] (t' <= 5) and T4[i'] (4 <= i' <= 8). B_1 vs D_2 gives {a3..a_(l-1), b19..b_(12+P)} = {b1, b2, b3}.
- The (N)-for-v equation leaves two placements:
  - **(A)** c1 = w, b13 = a2, e9 = b7, T3[8..9] = (v, b18);
  - **(B)** c1 = a2, b13 = b3, e9 = b7, and T3[lam3-1] = v next to b_w.
- In **(B)**, b4 is not a w-neighbour label:
  - b_w's neighbours carry labels in {b1, b2, b3}, v, and {c6, a2, a3..};
  - T2[8]'s carry b7 and a label in {a1, a2, b1, b2};
  - T3[t'] meets a1, a2, b5, b6, b7, w;
  - T4[i'] meets b1, a2, b3, b5, b6, b7, w.
  This contradicts (N) for w.
- In **(A)**, (N) for w forces **c_(lam3-1) = b4**.
  - For P = 7, T3[8..12] = (v, b18, a1, b7, b4), because {b18, b7} is a T2 pair. Then {b7, b4} repeats the T2 complement.
  - For P = 8, T3[13] = b4 neighbours T3[12], which carries b7, a1, b1 or b2. But {b4, b7} is used on T2, {b4, a1} and {b4, b2} in the K4, and {b4, b1} at T4[2]T4[3].

Every branch repeats a pair or violates (N). QED

## 4. Result

**(S0) type (9,6) with o0 = 8 and o0 = 9 is impossible.** With v71 (SHA256 `0d4f837885a17ee6fd0c9972798b6b267a10db9a53bb8f677e741783ae112211`, o0 = 10), all of type (9,6) is excluded, and by v<->w so is type (4,1). Together with v66-v71, **the whole four/four shape is impossible** (residual R2 of manifest v12 is empty).

With v53 (three/three) and v61-v65 (four/three), **distinct-centre 4+4 class (a)-II with r_P2 = 3 is impossible**. With v47-v51 (r_P2 = 2), v53 (r_P2 = 5) and v55 (r_P2 = 4), **all of class (a)-II is excluded**. With the parent-gated (a)-I result (v44), **core (a) of distinct-centre 4+4 is excluded at support 8**.

All of this is WRITTEN, unreviewed, necessary-case only. Open at m = 8:
- class (b) with d = 3 one-gap and d = 1;
- distinct 3+5 connected;
- distinct 3+5 disconnected, except Type I with r_P = 2.

All m >= 9 also remain open.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
