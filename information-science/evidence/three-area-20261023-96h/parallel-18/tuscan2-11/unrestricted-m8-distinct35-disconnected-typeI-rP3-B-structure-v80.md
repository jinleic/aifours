# Actual Tuscan11 distinct 3+5, disconnected, Type I with r_P = 3 — structure of the self-dual thread B

Actual `/bin/date` before this body: **Mon Oct 26 11:35:36 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case reduction, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

This is Type I of v60 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`) with r_P = 3:
- P = A D C^-, with 3 rows and length 30 = x+t+z;
- O = B D^- B^- C A^-, with 6 rows;
- |B| = 15.

By v60 §2, B carries exactly one v-copy (B-coordinate s_v) and one w-copy (s_w). O visits each of them twice. The cross paths A, C, D carry two v-copies and one w-copy.

**Imports:**
- Lemma W of v76 (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`);
- rule (R), the bd chain and the shift-5 chain (v49 §4, v50 §2);
- (L3) of v57;
- the uncuttable property of B: its ends b_v and b_w are never boundaries.

O-positions:
- B at [0, 15];
- D^- at [15, 15+t];
- B^- at [15+t, 30+t], where B[s] sits at 30+t−s;
- C, then A^-.

## 2. Lemma W along the two passes of B

**Forward pass.** O visits b_v(0) and later the v-copy s_v, with no other v-visit between. So exactly one O-boundary lies in (0, s_v). Likewise exactly one lies in (s_w, 15), between the w-copy and b_w(15).

**Backward pass**, in B-coordinates:
- exactly one boundary lies in (s_w, 15), between b_w(15+t) and the w-copy;
- exactly one lies in (0, s_v), between the v-copy and b_v(30+t).

**Boundary pattern of a pass.** A pass has its least boundary b ∈ 1..9; b ≠ 5, since b+10 = 15 would be b_w. Either:
- it has one boundary b ∈ 6..9, or
- it has two boundaries b, b+10, with b ∈ 1..4.

## 3. Lemma B (structure of B)

**(i) s_w < s_v.**

Suppose s_v < s_w. Then the intervals (0, s_v) and (s_w, 15) are disjoint, so each pass needs two boundaries b and b+10, with b ∈ (0, s_v) and b+10 ∈ (s_w, 15). Hence both passes have their least boundary in 1..4.

Each pass then has an inside row [b, b+10]. The forward inside row is clean against the backward one, at offset |b − g| ≤ 3. Rule (R) forbids this; offset 0 would also double a cut by (L3).

**(ii) A two-boundary pass forces both copies into its inside row.**

Its inside row lies inside B and needs one v and one w. B carries only s_v and s_w, so b < s_w < s_v < b+10.

**(iii) At most one pass has two boundaries,** by the same rule-(R) argument as in (i).

**(iv) A one-boundary pass has b ∈ 6..9 ∩ (s_w, s_v).**

## 4. Consequences for the copies and rows when exactly one pass has two boundaries

Take the forward pass with two boundaries (b1 ∈ 1..4) and the backward pass with one (g1 ∈ 6..9). Lemma W then forces the following.

**The rows near B.**
- The b_v(0)-row X0 cannot hold the B w-copy, since s_w > b1. So the cross w-copy lies on A, in X0, and C and D carry no w-copy.
- Q1 (through b_w(15)) takes its v from a D-copy.
- O's rows are X0, M, Q1, Q2, Y0 and Q3 in this order, with exactly one boundary on D^-.

**Lengths.**
- t = b1 + g1.
- O's D-boundary sits at ω = g1 − 5.
- O's A-boundary sits at 10 − b1, and its C-boundary at 10 − g1.

**Rule (R) between the passes.** The forward inside row against the backward rows gives g1 − b1 ∈ {4, 5, 6}.

**Lemma T3 at b_v** applies to P's b_v-row R_P = C[10−p..1], v, A[1..p], to X0 and to Y0. X0 is shorter on B (b1 < g1), which gives:
- p < 10 − b1;
- p < g1.

**Cross paths A, C, D** (rule (R)):
- p + b1 ≥ 4;
- 1 ≤ g1 − p ≤ 6;
- |π − ω| ≤ 6, where π is P's D-boundary.

The case where the backward pass has the two boundaries is the mirror image. Reversing all rows, swapping A ↔ C and reversing D keeps Type I and exchanges B's two passes.

## 5. Status

**WRITTEN** (Lemma B and the reductions of §4).

Type I with r_P = 3 is **not closed**. Two sub-cases remain:
- one pass with two boundaries (§4), plus its mirror;
- both passes with one boundary, b1 and g1 both in 6..9 ∩ (s_w, s_v).

In each, Lemma U of v77 leaves a few candidate v–w edges:
- a D v-copy at D[t−1];
- a cross v-copy next to b_w;
- the A w-copy at A[1].

Type I with r_P = 4, Type II with r_P = 2 and the Type II, r_P = 3 survivors of v78 remain open; so does R6. R1–R4 are empty if the unreviewed bodies (v47–v79) are correct.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
