# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — the survivor Sigma = 24, x = 7 dies at edge level

Actual `/bin/date` before this body: **Mon Oct 26 07:08:16 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result.

## 1. Setting

The setting is the v56 survivor (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`, read with v59, SHA256 `413003f4ce2b9349febccd794821dde011121c380df41bfe332dea29d3206222`): four/three shape, P2 shift d = 6, O inside T3, Sigma = 24. Here **x = 7** (o0 = 8) and y in {1, 2}, so:
- l = 16 - y, |T2| = 9 + y, lam3 = 17 + y, lam = 13 - y.

Write a_i = L(T1[i]), b_i = L(T2[i]), c_i = L(T3[i]) and e_i = L(T4[i]), all numbered from b_v. The eleven rows, read in face order, are:
- B_0 = e8..e1, v, a1, a2
- B_1 = a2..a12
- B_2 = a12..a_(l-1), w, b_(8+y)..b3
- B_3 = b3, b2, b1, v, c1..c7
- O = c7..c17
- D_0 = c17..c_(16+y), w, a_(l-1)..a6
- D_1 = a6..a1, v, b1..b4
- D_2 = b4..b_(8+y), w, e_(12-y)..e8
- R_3 = c3, c2, c1, v, e1..e7
- R_- = c13..c3
- R_+ = e7..e_(12-y), w, c_(16+y)..c13

The cuts are e8, a2, a12, b3, c7, c17, a6, b4 (P6) and c3, c13, e7 (P2). Their labels are pairwise distinct.

**Imports.** Rows are complete. By (F2) (v48 §1, SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`), every unordered label pair lies on exactly one edge; call a second occurrence of a pair a *repeat*. In particular, two w-vertices never have neighbours carrying the same label.

The neighbours of b_w carry the labels a_(l-1), b_(8+y), c_(16+y) and e_(12-y).

## 2. Exchanges

- (E1) B_0 vs R_3: {e8, a1, a2} = {c1, c2, c3}.
- (E2) B_3 vs D_1: {c1..c7} = {a1..a6, b4}.
- (E3) R_- vs O: {c3..c6} = {c14..c17}.
- (E4) B_1 vs D_0: {a2..a5} = {a13..a_(l-1), w, c17..c_(16+y)}.

**Step 1.** c3 is a cut, and so are e8 and a2, so c3 = a1. The edge T3[2]T3[3] carries {c2, a1}. It may not repeat T1's edge {a1, a2}, so **c2 = e8 and c1 = a2**.

**Step 2.** Removing {a2, e8, a1} from (E2) gives {e8, c4, c5, c6, c7} = {a3, a4, a5, a6, b4}. Here e8, c7, a6 and b4 are all cuts, so e8 and c7 lie in {a3, a4, a5}, while a6 and b4 lie in {c4, c5, c6}. By (E3) the cut c17 also lies in {c4, c5, c6}. Hence:
- {c4, c5, c6} = {a6, b4, c17};
- **{a3, a4, a5} = {e8, c7, c17}**.

**Step 3.** (E4) now reads **{a2, e8, c7} = {a13, a14, w}** for y = 1, and **{a13, w, c18}** for y = 2.

**Step 4.** e8 ≠ w, since T4[8] ends D_2, which already holds b_w. So w is a2 (T1[2] is the w-cut) or c7 (T3[7] is the w-cut).

## 3. w = a2 is impossible

Then c1 = w, and the edge T3[1]T3[2] carries {w, e8}.
- **y = 1.** {e8, c7} = {a13, a14}.
  - If e8 = a14, the edge b_w T1[14] repeats {w, e8}.
  - So e8 = a13 and c7 = a14. The edge T1[2]T1[3] carries {w, a3} with a3 in {a13, a14, c17}. This repeats {w, e8} (at T3[1]T3[2]), {w, a14} (at b_w T1[14]) or {w, c17} (at b_w T3[17]).
- **y = 2.** {e8, c7} = {a13, c18}, and both are b_w-neighbour labels, so {w, e8} repeats.

## 4. w = c7 is impossible

Then {a2, e8} is {a13, a14} for y = 1 and {a13, c18} for y = 2. Also w lies in {a3, a4, a5}, so T1[j] = w for some j in {3, 4, 5}, and the other two of a3, a4, a5 are e8 and c17.

**y = 1** (b_w-neighbour labels include a14 and c17):
- **j = 4:** one T1-neighbour of T1[4] carries c17, so {w, c17} repeats.
- **j = 3:** a4 is e8 or c17, and not c17, so a4 = e8 and a5 = c17.
  - If e8 = a14, then {w, e8} repeats (at T1[3]T1[4] and b_w T1[14]).
  - Otherwise a2 = a14, and {w, a2} repeats (at T1[2]T1[3] and b_w T1[14]).
- **j = 5:** a4 = e8 and a3 = c17 as before.
  - e8 = a14 repeats {w, e8}.
  - Otherwise e8 = a13 and a2 = a14. Then {e8, a2} lies on T1[13]T1[14] and on T3[1]T3[2] (c1 = a2, c2 = e8).

**y = 2** (b_w-neighbour labels include a13 and c18, hence both a2 and e8):
- **j = 3:** T1[2] neighbours T1[3] = w, so {w, a2} repeats.
- **j = 4:** a T1-neighbour of T1[4] carries e8, so {w, e8} repeats.
- **j = 5:** a4 ≠ e8, so a4 = c17 and a3 = e8. Then {a2, e8} lies on T1[2]T1[3] and on T3[1]T3[2].

Every branch repeats a pair. QED

## 5. Result

**The v56 survivor Sigma = 24 with x = 7 (y = 1, 2) is impossible.** The remaining v56/v59 survivors in the four/three shape are:
- Sigma = 24 with x in {8, 9} and y in {1, 2};
- Sigma = 21 with x in {7, 8, 9} and y in {3, 4};
- Sigma = 26 with x in {7, 8} and y in {1, 2, 3}.

Edge-level (DUP) reasoning is needed there as well. For Sigma = 24 with x = 8, the analogues of Steps 1-4 leave several short arrangements of T3[1..4] that the quick repeat checks above do not close; they are not closed here. All other open lines are as in manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`) and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
