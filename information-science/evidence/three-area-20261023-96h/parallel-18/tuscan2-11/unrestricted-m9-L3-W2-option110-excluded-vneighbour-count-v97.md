# Actual Tuscan11, m = 9, L3, W2, option (1,1,0): the eight skeletons are excluded by counting v's T_int-neighbours

Actual `/bin/date` before this body: **Mon Oct 26 14:12:37 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- **v96** (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`), §4:
  - option (1,1,0) with δ > 0 is impossible;
  - δ < 0 forces the eight skeletons (B, C, V), with t = 4 + B + D, D = 1 − C, and the listed segment labels.
- **F2 / one edge per pair** (v12 §1): each label has exactly one split edge to every other label.
- T_int is the set of labels of T's interior. It has t − 1 elements, and T[1], the T-vertex next to b′, carries one of them.

## 2. The count

Label v must have exactly t − 1 = 3 + B + D distinct neighbours carrying T_int labels. In the skeleton, v's split vertices and their possible T_int-neighbours are:

| Vertex of v | Neighbours | T_int-neighbours |
|---|---|---|
| b′ | T[1] ∈ T_int; P[1] ∈ P1 and Q[1] ∈ Q1, both S-labels | exactly 1 |
| b″ | P[p−1] ∈ P3 = {λ5, λ8α} ⊆ S; Y1[1] ∈ Y1a = {c_in, λ7α} ⊆ S; Y2[1] ∈ Y2a = {c1 if V=0, λ8β, w} | at most 1, and only if Y2[1] = λ8 with 8β |
| Y1c-vertex of v | its Y1-neighbours lie in {Y1[h] = λ5, c1 if V=0, λ7α, b_w = w}, all S or w | 0 |
| Y2c-vertex of v | its two Y2-neighbours lie in {Y2[s] = λ7, c1 if V=0, y0, λ5, w, Y2[f1+10] = λ8}; the T_int candidates are y0, λ7 if 7β, λ8 if 8β | at most 2 |

**Case (B, D) = (0, 0).** Here 3 are needed, but λ7 and λ8 are S-labels. The Y2c-vertex gives at most y0 and b″ gives nothing, so at most 2 are available. Contradiction.

**Case (1, 0).** 4 are needed. At most T[1], y0 and λ7 are available: 3. Contradiction.

**Case (0, 1).** 4 are needed. The candidates are T[1], λ8 (through Y2[1]), and the Y2c-vertex's y0 and λ8. Label λ8 can be counted only once, since v has one edge to each label. So at most 3. Contradiction.

**Case (1, 1).** 5 are needed. The candidates are T[1], λ8 (through Y2[1] or the Y2c-vertex, counted once), y0 and λ7: at most 4. Contradiction.

## 3. Result

All eight skeletons of v96 §4.3 are impossible. With v96 §4.2, **option (1,1,0) of L3, W2 is impossible** (WRITTEN, Tuscan-1 necessary case).

The method is a neighbour-class count on a label's split vertices against the label classes S, T_int, {v}, {w}. It applies to any skeleton.

**Still open in L3:** W2 options (1,0,1) and (2,0,0), and all of W1.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
