# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — the survivor Sigma = 21 with x = 7 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 07:30:04 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result.

## 1. Setting

The setting is the v56 survivor (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`, read with v59, SHA256 `413003f4ce2b9349febccd794821dde011121c380df41bfe332dea29d3206222`): four/three shape, P2 shift d = 6, O inside T3, **Sigma = 21**, here with **x = 7** (o0 = 8) and y = p0 in {3, 4}. Then:
- l = 13-y, |T2| = 12+y, lam3 = 17+y, lam = 13-y.

Labels a_i, b_i, c_i, e_i are as in v61 (SHA256 `5dd3c58a33e185a94c8025cfb8213f8e68802e392bad379bf95ff283109cfa43`). The rows are:
- B_0 = e8..e1, v, a1, a2
- B_1 = a2..a_(l-1), w, b_(11+y)..b13
- B_2 = b13..b3
- B_3 = b3, b2, b1, v, c1..c7
- O = c7..c17
- D_0 = c17..c_(16+y), w, a_(l-1)..a3
- D_1 = a3, a2, a1, v, b1..b7
- D_2 = b7..b_(11+y), w, e_(12-y)..e8
- R_3 = c3, c2, c1, v, e1..e7
- R_- = c13..c3
- R_+ = e7..e_(12-y), w, c_(16+y)..c13

The cuts are e8, a2, b13, b3, c7, c17, a3, b7 (P6) and c3, c13, e7 (P2); their labels are pairwise distinct. The neighbours of b_w carry a_(l-1), b_(11+y), c_(16+y), e_(12-y): **a9, b14, c19, e9 for y = 3** and **a8, b15, c20, e8 for y = 4**.

**Imports.** Rows are complete. By (F2) (v48 §1, SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`), every unordered label pair lies on exactly one edge; a second occurrence is a *repeat*. Adjacent vertices have distinct labels, since every edge lies in a row. By v47 §1 (SHA256 `3a60200022a7d702a4589e6e0752fc2e86d7421f11f3d7210499b90a72d6a321`), besides b_v and b_w there are exactly three degree-2 vertices labelled v and three labelled w. Hence:
- **(N)** The ten edges at the four w-vertices end at ten distinct labels, namely all labels other than w. The same holds for v.

## 2. Steps common to both y

**Step 1** (as v61 Step 1). B_0 vs R_3 gives {e8, a1, a2} = {c1, c2, c3}. Hence **c3 = a1, c2 = e8, c1 = a2**, and the pairs {a1, a2}, {a2, e8}, {e8, a1} are all used.

**Step 2.** B_3 vs D_1 gives {c1..c7} = {a1, a2, a3, b4..b7}, and R_- vs O gives {c3..c6} = {c14..c17}. Removing a2 and a1 leaves {e8, c4, c5, c6, c7} = {a3, b4, b5, b6, b7}. Since e8, c7, a3, b7 and c17 are cuts:
- **{c4, c5, c6} = {a3, b7, c17}**;
- **{b4, b5, b6} = {e8, c7, c17}**;
- {c14, c15, c16} = {a1, a3, b7}.

**Step 3.** B_2 vs D_2 gives {b3, b4, b5, b6} = {b14..b_(11+y), w, e8..e_(12-y)}, so {b3, c7, c17} is **{b14, w, e9} for y = 3** and **{b14, b15, w} for y = 4**. c17 ≠ w, since D_0 holds T3[17] and b_w. For y = 3, also c17 ≠ e9, since R_+ holds T3[17] and T4[9]; so c17 = b14 and {b3, c7} = {w, e9}. In both cases **w is b3 or c7**, so the w-cut is T2[3] or T3[7]. Let u be the other label of {b3, c7}.

**Step 4.** Three more exchanges:
- B_1 vs D_0: {a2, b13..b_(11+y)} = {c17..c_(16+y)}.
- R_- vs B_3: {c8..c13} = {b1, b2, b3, v, a2, e8}.
- O vs R_+: {c7..c12} = {e7..e_(12-y), w, c18..c_(16+y)}.

The cut labels b3, a2, e8, e7 cannot sit on the cuts c7 or c13, so {c8..c12} = {b3, a2, e8, e7, q} for one further label q, and the second exchange gives {e7, q, c13} = {b1, b2, v}. Since R_3 holds T4[7] and b_v, **e7 is b1 or b2**. The third exchange becomes {c7, b3, a2, q} = {e9..e_(12-y), w, c18..c_(16+y)}. With the first exchange:
- **y = 3:** {a2, b13} = {c18, c19} and {a2, q} = {c18, c19}.
- **y = 4:** {u, c17} = {b14, b15}, so {a2, b13, u} = {c18, c19, c20} = {u, a2, q}.

Either way q = b13. So **{c8..c12} = {b3, a2, e8, e7, b13}** and **{e7, b13, c13} = {v, b1, b2}**. Write b' for the label in {b1, b2} other than e7.

**Step 5.** D_1 lists every label once, so the alphabet is {v, a1, a2, a3, b1..b7}. By Steps 2-3 that is {v, w, a1, a2, a3, b1, b2, b7, b14, e8, e9} (y = 3) or {v, w, a1, a2, a3, b1, b2, b7, b14, b15, e8} (y = 4). Two further exchanges:
- B_3 vs R_3: {e1..e7} = {b1, b2, b3, c4, c5, c6, c7}. So T4[1..6] carries b', b3, c7, a3, b7 and c17.
- D_0 vs R_+: {a3..a_(l-1)} = {e7..e_(12-y), c13..c16}. So {a4..a_(l-1)} = {e7..e_(12-y), c13, a1, b7}.

**Step 6** (placing e8). e8 sits on some T3[i] with 8 <= i <= 12. Its neighbours carry labels from {c7, b3, a2, e7, b13, c13}:
- a2 repeats Step 1's {a2, e8}, and e7 repeats the edge T4[7]T4[8].
- In every case below, the labels c7 and b3 also repeat (each case says how).

The only labels left are b13, carried once in T3[8..12], and c13, carried by T3[13]. Hence **T3[12] = e8 and T3[11] = b13**, and T3[8..10] carry {b3, a2, e7}.

**Step 7** (the other w-copies). R_3 must hold w, but c1..c3 = a2, e8, a1 and e7 is in {b1, b2}. So one w-copy is **T4[k] with k <= 6**.

## 3. y = 4 (b_w-neighbour labels a8, b15, c20, e8)

### 3.1 w = c7

Then {b3, c17} = {b14, b15}, and T2[j] = w for some j in {4, 5, 6}, the other two of b4, b5, b6 being e8 and c17.
- **j = 5:** a T2-neighbour carries e8, which repeats b_w T4[8].
- **j = 4:** b5 ≠ e8 (T2[5] would repeat {w, e8}), so b5 = c17. T2[4]'s neighbours then carry b3 and c17, which are b14 and b15; {w, b15} repeats b_w T2[15].
- **j = 6:** b5 ≠ e8 as before, so b5 = c17 and b4 = e8. c17 ≠ b15 (it would repeat {w, b15}), so **c17 = b14 and b3 = b15**, and T2[3..7] = b15, e8, b14, w, b7.

Continue with j = 6. Step 6 holds: c7 = w repeats b_w T4[8] = {w, e8}, and b3 = b15 repeats T2[3]T2[4] = {b15, e8}. Also c6 is in {a3, b7, b14}; b7 and b14 already neighbour T2[6], so **c6 = a3**.

By Step 5, T4[1..6] carries b', b15, a3, b7, b14, w. Four of these labels already neighbour w-vertices, so T4[k]'s neighbours can only carry v (k = 1), b', or e7 (k = 6). Hence **k is 1 or 6**.

Now apply (N) to w. The used labels are b15, e8, b14, b7, a3, so {a8, c20, c8, two T4[k]-neighbours} = {v, a1, a2, b1, b2}. Here:
- a8 is in {e7, c13, a1, b7} (Step 5, minus e8);
- c20 is in {a2, b13} (Step 4 gives {c18, c19, c20} = {a2, b13, b15}, and c20 ≠ b15);
- c8 is in {a2, e7} (Step 6, minus the used b15).

Only a8 can be a1, so **a8 = a1**.
- **k = 6:** the T4 neighbours carry b' and e7, so {c20, c8} = {v, a2}. c8 ≠ v, so c8 = a2, c20 = v and hence b13 = v.
  - The v-vertices are b_v, T2[13], T3[11] and T3[20]. Their neighbours carry a1, b1, a2, e1 / b12, b14 / c10, e8 / c19, w.
  - By (N) for v, c19 ≠ a2. So c19 = b15 and c18 = a2.
  - c10 ≠ b15, since b15 = c19 is already a v-neighbour label. So c10 = e7 and c9 = b15.
  - Now T3[8]T3[9] = {a2, b15} = T3[18]T3[19], a repeat.
- **k = 1:** the T4 neighbours carry v and b' (T4[2]), so {c20, c8} = {a2, e7}. Since b13 ≠ e7, c20 = a2 and c8 = e7. Then {c18, c19} = {b13, b15}, and {c9, c10} = {a2, b15}.
  - If (c9, c10) = (b15, a2), the edge T3[19]T3[20] = {c19, a2} repeats {b13, a2} (T3[10]T3[11]) or {b15, a2} (T3[9]T3[10]).
  - If (c9, c10) = (a2, b15), then c19 = b15 repeats {b15, a2}. And c19 = b13 forces c18 = b15, so T3[17]T3[18] = {b14, b15} repeats T2[14]T2[15].

### 3.2 w = b3

Then T2[3] is the w-cut, {c7, c17} = {b14, b15} and {b4, b5, b6} = {e8, b14, b15}.
- T2[4] neighbours the w-cut T2[3], so b4 is neither e8 nor b15 (both are b_w-neighbour labels). Hence b4 = b14.
- b5 ≠ b15 (it would repeat T2[14]T2[15]), so b5 = e8 and b6 = b15.
- Step 6 holds: b3 = w repeats b_w T4[8], and c7 in {b14, b15} repeats T2[4]T2[5] = {b14, e8} or T2[5]T2[6] = {e8, b15}.
- By Step 4, w = b3 lies in {c8..c12}, so O holds a w-copy T3[i] with i in {8, 9, 10}. i ≠ 8, because T3[7] carries b14 or b15 and both already neighbour w (T2[3]T2[4] and b_w T2[15]).
- By Step 5, T4[1..6] carries b', w, a3, b7, b14, b15.

Apply (N) to w. The used labels are b15, e8, b2, b14, so {a8, c20, two T3[i]-neighbours, two T4[k]-neighbours} = {v, a1, a2, a3, b1, b7}. Here:
- a8 is in {e7, c13, a1, b7};
- c20 is in {a2, b13}, since {c18, c19, c20} = {a2, b13, c7} and c7 (b14 or b15) is a used label;
- the T3[i]-neighbours carry labels in {a2, e7, b13};
- the T4[k]-neighbours carry labels in {v, b', a3, b7, e7}.

So a8 = a1, the T4[k]-neighbours carry a3 and b7, and {c20, T3[i]-neighbours} = {v, a2, b1}.
- **i = 9:** the neighbours carry a2 and e7, so e7 = b1 and c20 = v = b13. Then T3[11] is a v-vertex whose neighbour T3[10] carries a2 or b1, both b_v-neighbour labels. Repeat.
- **i = 10:** the neighbours are T3[9] and T3[11] = b13. c20 ≠ b13 (it would repeat {w, b13}), so c20 = a2. Then {c9, b13} = {v, b1} with c9 in {a2, e7}, so c9 = e7 = b1, b13 = v and {c18, c19} = {v, c7}.
  - If c19 = v, the edge T3[19]T3[20] = {v, a2} repeats b_v T3[1].
  - If c18 = v, its neighbours carry c17 and c7, i.e. b14 and b15. But T2[13] (label v) neighbours T2[14] = b14, so {v, b14} repeats.

## 4. y = 3 (b_w-neighbour labels a9, b14, c19, e9)

Here c17 = b14, {b3, c7} = {w, e9} and {c18, c19} = {a2, b13}.

### 4.1 w = c7, b3 = e9

- T2[j] = w with j in {4, 5, 6}, and {b4, b5, b6} = {e8, w, b14}.
  - j = 4 neighbours T2[3] = e9, which repeats b_w T4[9].
  - j = 5 has a neighbour carrying b14, which repeats b_w T2[14].
  - So **j = 6**. b5 ≠ b14 (T2[5] neighbours T2[6] = w), so b5 = e8, b4 = b14, and T2[3..7] = e9, b14, e8, w, b7.
- Step 6 holds: c7 = w repeats T2[5]T2[6] = {e8, w}, and b3 = e9 repeats T4[8]T4[9].
- c6 is in {a3, b7, b14}; b7 (T2[7]) and b14 (b_w) already neighbour w, so **c6 = a3**.
- T4[1..6] carries b', e9, a3, b7, b14, w. As in 3.1, **k is 1 or 6**.

Apply (N) to w. The used labels are b14, e9, e8, b7, a3, so {a9, c19, c8, two T4[k]-neighbours} = {v, a1, a2, b1, b2}. Here:
- a9 is in {e7, c13, a1} (Step 5, minus used labels);
- c19 is in {a2, b13};
- c8 is in {a2, e7}.

So **a9 = a1**.
- **k = 6:** {c19, c8} = {v, a2}. So c8 = a2, c19 = v = b13 and c18 = a2. Then T3[18]T3[19] = {a2, v} repeats b_v T3[1].
- **k = 1:** {c19, c8} = {a2, e7}. So c19 = a2, c8 = e7, c18 = b13, and {c9, c10} = {e9, a2}.
  - (e9, a2): T3[10]T3[11] = {a2, b13} = T3[18]T3[19].
  - (a2, e9): T3[17]T3[18] = {b14, b13} = T2[14]T2[13].

### 4.2 w = b3, c7 = e9

- {b4, b5, b6} = {e8, e9, b14}.
  - T2[4] neighbours the w-cut T2[3], so b4 is neither e9 nor b14 (b_w-neighbour labels). Hence b4 = e8.
  - b5 ≠ e9 (it would repeat T4[8]T4[9]), so b5 = b14 and b6 = e9.
- Step 6 holds: b3 = w repeats T2[3]T2[4] = {w, e8}, and c7 = e9 repeats T4[8]T4[9].
- O holds a w-copy T3[i] (by Step 4, w = b3 lies in {c8..c12}), with i in {9, 10}, since T3[8] would neighbour T3[7] = e9.
- T4[1..6] carries b', w, a3, b7, b14, e9.

Apply (N) to w. The used labels are b14, e9, b2, e8, so {a9, c19, two T3[i]-neighbours, two T4[k]-neighbours} = {v, a1, a2, a3, b1, b7}. Here:
- a9 is in {e7, c13, a1, b7};
- c19 is in {a2, b13};
- the T3[i]-neighbours carry labels in {a2, e7, b13};
- the T4[k]-neighbours carry labels in {v, b', a3, b7, e7}.

So a9 = a1, the T4 neighbours carry a3 and b7, and {c19, T3[i]-neighbours} = {v, a2, b1}.
- **i = 9:** e7 = b1 and c19 = v = b13, so c18 = a2, and T3[18]T3[19] = {a2, v} repeats b_v T3[1].
- **i = 10:** c19 ≠ b13 (it would repeat {w, b13}), so c19 = a2 and c18 = b13. Then c9 = e7 = b1 and b13 = v. T3[18] (label v) neighbours T3[17] = b14, which repeats T2[13]T2[14] = {v, b14}.

Every branch repeats a pair. QED

## 5. Result

**The v56 survivor Sigma = 21 with x = 7 (y = 3, 4) is impossible.** With v61 and v62, the remaining four/three survivors are:
- Sigma = 24 with x in {8, 9} and y in {1, 2};
- Sigma = 21 with x in {8, 9} and y in {3, 4}.

The method here is new relative to v61 and v62: the full alphabet is read off D_1, and (N) — the ten w-neighbour (or v-neighbour) labels are exactly the other ten labels — forces a8 = a1 (resp. a9 = a1) and pins the T4 copy. Whether it closes x = 8, 9 is not claimed. Other open lines are as in manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
