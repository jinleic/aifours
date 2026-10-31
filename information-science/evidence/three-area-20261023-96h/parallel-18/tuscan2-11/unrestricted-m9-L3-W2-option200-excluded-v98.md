# Actual Tuscan11, m = 9, L3, W2, option (2,0,0) — excluded

Actual `/bin/date` before this body: **Mon Oct 26 14:15:31 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- **v96** (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`):
  - the L3 setting and Lemma VL;
  - the W2 identities, with option (2,0,0): c1 = 2, c2 = 0, a = b = 0, r = (5,3,3), y1 = 25 − t, y2 = 5 + t, p + q = 25 − t;
  - the row-pair / matching method.
- **v97** (SHA256 `eb504cf48859a839e2f335c8e40cae7a9a3a812074d206d77e7cc77381b891e2`): the neighbour-class count.

## 2. Forced shape

**Parameters.**
- **Lemma VL.** a = 0 gives p ≤ u+10; b = 0 gives q ≤ 10, and q ≤ 9 because b_w is not a cut.
- **b_w in F1.** It sits at 25 + p and must avoid R_in, so p ≤ 14.
- **b″ in R_1.** This gives t+p ≤ 19, and q ≤ 9 gives t+p ≥ 16.
- **The w-2-vertices.** The identities give c1′ = 1 and c2′ = 1. Since a′ ≥ 1, also a′ = 1 (in P(u..10)) and b′ = 0.
- **t ≥ 2.** P[10] is an F2 cut whose label y0 lies in T_int.
- Put g = 20 − t − p ∈ [1,4] and s = q + t − 5 = 20 − p.

**Rows of F1.**
- R_out = ℓ, T, b′, P[1..u].
- R_1 = P[u..p−1], b″, Y1[1..g].
- R_2 = Y1[g..g+10], a pure Y1 row.
- R_3 = Y1[g+10..24−t], b_w, Q[q−1..u].
- R_in = Q[u..1], b′, T, ℓ.

**Rows of F2.**
- R_start = b′, Q[1..q−1], b_w, Y2[4+t..s].
- mid = Y2[s..1], b″, P[p−1..10].
- R_end = P[10..1], b′.

**v and w in F1 and F2.** R_2 and R_3 each need a Y1-v-vertex, and R_2 needs the Y1-w-vertex. The Y2-w-vertex lies in mid, at an index j < s.

**Rows of F3.** F3 is b″, Y2[1..4+t], b_w, Y1⁻. Counting cyclically one v and one w per row gives cuts f1, f1+10, f1+20 with j < f1 < 5+t. With h = 10 − f1:
- Row_A = Y2[f1..4+t], b_w, Y1[24−t..h+10];
- Row_B = Y1[h+10..h], a pure Y1 row;
- Row_C = Y1[h..1], b″, Y2[1..f1].

**The cuts.** The nine non-v, non-w cuts are P[u], P[10], Q[u], Y1[g], Y1[g+10] (in F1 and F2), Y2[s], and the F3 cuts Y2[f1], Y1[h+10], Y1[h].

## 3. The four relative orders

Two independent comparisons remain: f1 against s (Y-I: f1 < s; Y-II: s < f1) and g against h (Z-I: g < h; Z-II: h < g).

### Y-II with Z-I

The Q[u]-label (Q[u] = c_in) has cut rows {R_3, R_in, R_start}. Row_A lies only in 2-vertex types paired with R_start (on Y2(f1..]) or with R_3 (on Y1(h+10..]). Both partners are already used, so Row_A cannot be covered. Contradiction.

### Y-I with Z-II

The Y1[h]-label has cut rows {R_1, Row_C, Row_B}. With those rows used:
- mid can only pair with Row_A, on Y2(f1,s);
- R_2 can only pair with Row_A, on Y1(h+10, g+10).

Both need Row_A. Contradiction.

### Y-II with Z-II

The Y1[h]-label again has cut rows {R_1, Row_C, Row_B}. mid's only 2-vertex types are {R_1, mid} (P3) and {mid, Row_C} (Y2[1,s)), and both partners are used. Contradiction.

### Y-I with Z-I

**Matchings.** v takes b′, b″ and the Y1 types {R_2, Row_B} and {R_3, Row_A}. w takes ℓ, b_w, P2 = {R_1, R_end}, Y1(h,g+10) and Y2[1,f1). The other nine labels have the following matchings. Here c1 = L(P[u]) and y0 = L(P[10]); the other labels are named by their cut vertex.

| Label | Vertices |
|---|---|
| c1 | Q1, plus {Y1(g,h), Y2(f1,s), Y1(g+10,h+10)} (M1) or {Y2[1,f1), Y1(h+10..], Y1(h,g+10)} (M2) |
| y0 | T, Y1(g,h), Y1(g+10,h+10), Y2(s..] |
| c_in | P1, Y2(f1,s), Y1(h,g+10), Y1[1,g) |
| Y2[f1] | T, P2, Q2, Y1(h,g+10) |
| Y2[s] | T, P2, Y1(g,h), Y1(g+10,h+10) |
| Y1[g] | P1, Q1, Y2(f1,s), Y1(g+10,h+10) |
| Y1[h] | T, Q2, Y2(f1,s), P2 (N1) or Q1, Y1(h+10..], P3, P1 (N2) |
| Y1[g+10] | Q1, P1, Y2(f1,s), Y1[1,g) (K1) or Y2(s..], T, P2, Y2[1,f1) (K2) |
| Y1[h+10] | Y1(g,h), P3, P1, Q1 |

**Segment equations.** The fourteen segment-length equations are consistent:

    t = 4 + N1 + K2,  p = 12 + N2,  s = 7 + N1,  g = 2 + K1,  h = 6 + K1 + M1,  f1 = 2 + M2 + K2.

**v's T_int-neighbours.** v needs t − 1 = 3 + N1 + K2 of them. The possible ones are:
- **b′:** gives T[1] only. P1 and Q1 carry S-labels.
- **b″:** P[p−1] ∈ P3 and Y1[1] ∈ Y1[1,g) carry S-labels. Y2[1] carries T_int only if it is the Y1[g+10]-label under K2.
- **The Y1(h,g+10)-vertex of v:** at most the Y2[f1]-label, the Y1[h]-label under N1, and the Y1[g+10]-label under K2.
- **The Y1(h+10..]-vertex of v:** its neighbours carry S-labels or w. That gives 0.

In each of the four cases of (N1, K2), the number of distinct T_int-neighbours is one less than needed. **Contradiction.**

## 4. Result

**Option (2,0,0) of L3, W2 is impossible** (WRITTEN, Tuscan-1 necessary case).

**Still open in L3:** W2 option (1,0,1) and all of W1.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
