# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — the survivor Sigma = 26 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 07:15:53 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result.

## 1. Setting

The setting is the v56 survivor (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`, read with v59): four/three shape, P2 shift d = 6, O inside T3, **Sigma = 26**, with x in {7, 8} and y in {1, 2, 3}. Then:
- l = 11+x-y, |T2| = 14-x+y, lam3 = x+10+y, lam = 20-x-y.

Labels a_i, b_i, c_i, e_i are as in v61 (SHA256 `5dd3c58a33e185a94c8025cfb8213f8e68802e392bad379bf95ff283109cfa43`). The rows are:
- B_0 = T4[15-x..1] b_v T1[1..x-5]
- B_1 = T1[x-5..x+5]
- B_2 = T1[x+5..l-1] b_w T2[13-x+y..10-x]
- B_3 = T2[10-x..1] b_v T3[1..x]
- O = T3[x..x+10]
- D_0 = T3[x+10..x+9+y] b_w T1[l-1..x+1]
- D_1 = T1[x+1..1] b_v T2[1..9-x]
- D_2 = T2[9-x..13-x+y] b_w T4[19-x-y..15-x]
- R_3 = T3[x-4..1] b_v T4[1..14-x]
- R_- = T3[x-4..x+6]
- R_+ = T4[14-x..19-x-y] b_w T3[x+9+y..x+6]

The cuts are e_(15-x), a_(x-5), a_(x+5), b_(10-x), c_x, c_(x+10), a_(x+1), b_(9-x) (P6) and c_(x-4), c_(x+6), e_(14-x) (P2). Cut labels are pairwise distinct and sit only at the cut vertices themselves.

## 2. Exchanges

- (E1) B_0 vs R_3: {e_(15-x), a_1..a_(x-5)} = {c_1..c_(x-4)}. The cut c_(x-4) differs from the cuts e_(15-x) and a_(x-5), so both of these lie in {c_1..c_(x-5)}.
- (E12) R_- vs B_3: {c_(x+1)..c_(x+6)} = {b_1..b_(10-x), v, c_1..c_(x-5)}.
- (E7) O vs R_+: {c_x..c_(x+5)} = {c_(x+11)..c_(x+9+y), w, e_(14-x)..e_(19-x-y)}.
- (E9) B_2 vs D_2: {a_(x+5)..a_(l-1)} = {b_(9-x), e_(15-x)..e_(19-x-y)}.

## 3. Five cut labels fill T3[x+1..x+5]

- The right side of (E12) contains the cut labels b_(9-x), b_(10-x) (since 9-x >= 1), e_(15-x) and a_(x-5).
- The right side of (E7) contains e_(14-x) and e_(15-x).

Each must sit at a non-cut vertex of the left side. The vertices T3[x] and T3[x+6] are cuts, so all five cut labels b_(9-x), b_(10-x), e_(15-x), a_(x-5) and e_(14-x) lie in T3[x+1..x+5], which they fill. Cancelling e_(14-x) and e_(15-x) in (E7) then gives

(*) {c_x, b_(9-x), b_(10-x), a_(x-5)} = {c_(x+11)..c_(x+9+y), w, e_(16-x)..e_(19-x-y)}.

## 4. Contradiction

- **b_(9-x).** D_2 contains b_(9-x), b_w and T4[16-x..19-x-y]. So b_(9-x) is not w and not any e_(16-x)..e_(19-x-y), and (*) puts **b_(9-x) in {c_(x+11)..c_(x+9+y)}**.
- **b_(10-x).** By (E9), B_2 contains vertices labelled b_(9-x) and e_(15-x)..e_(19-x-y) (on T1), as well as b_w and its own last vertex T2[10-x]. So b_(10-x) is not w, not b_(9-x), and not any of those e's, and (*) puts **b_(10-x) in {c_(x+11)..c_(x+9+y)} minus b_(9-x)**.

So the y-1 labels c_(x+11)..c_(x+9+y) contain both b_(9-x) and b_(10-x).
- **y = 1, 2:** there are fewer than two such labels. Contradiction.
- **y = 3:** {b_(9-x), b_(10-x)} = {c_(x+11), c_(x+12)}. The edges T2[9-x]T2[10-x] and T3[x+11]T3[x+12] then carry the same unordered pair, against (F2) (v48 §1, SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`). QED

## 5. Result

**The v56 survivor Sigma = 26 (x in {7, 8}, y in {1, 2, 3}) is impossible.** With v61, the remaining four/three survivors are:
- Sigma = 24 with x in {8, 9} and y in {1, 2};
- Sigma = 21 with x in {7, 8, 9} and y in {3, 4}.

For Sigma = 24 and Sigma = 21, b_(9-x) is not a cut. The analogue of §3 therefore places only four cut labels in T3[x+1..x+5], leaving one free slot, and §4 does not apply as written. Other open lines are as in manifest v12 and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
