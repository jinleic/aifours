# Original Tuscan-2(11), entire m = 9 distance-two branch (parent direction v143): consolidated status and exact gap

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4). This is a status packet. It gathers v112–v118 and adds one refinement for L1 (§3). It is not reviewed, formal or novelty-cleared. Written reasoning only.

## 1. What v143 asked, and the acceptance ceiling

**The ask.** Apply the original distance-two condition (R3) to the entire remaining m = 9 families, with every variable free. Those families are:
- L1;
- L2 with k = 3;
- L4-B W1.

**The ceiling.**
- Only if all three families are excluded may one state: "every eligible original Tuscan-2(11) array with support 9 is impossible."
- Any m ≥ 10 consequence needs the full joint gate.
- Every m in 10..110 stays unresolved.

## 2. Closed, all by (R1)–(R2) alone

(R3) was not needed anywhere.

| Family or cell | Packets | Status |
|---|---|---|
| L4-B (W1 for every k_x, and W2) | v106, v107, v112 §4, v113 | **closed** |
| L2 (k = 3) with two v-2-vertices on t1, or two on t3 | v114 §3, v116 (K1) | closed |
| L2 type A, case (0,0,0,2) | v116 (K4) | closed |
| L2 type A b = 3 with λ ∈ {6,7,8,9,17,18,19,24}, or with λ = 14 and u ≥ 7 | v115 §3 | closed |
| L2 type B, b = 2, n1 = 1, λ = 6 | v116 (K5) | closed |
| L1 types 5 and 6 | v118 | closed |

**General lemmas proved** (v114 §2, v115 §1):
- DP-1 and DP-2, together with the overlap lemma OL;
- consequently, no thread or loop of length ≥ 27 exists in any m = 9 family;
- for length ≥ 21, only ρ ∈ {4, 6} survives.

## 3. One refinement for L1: (L-K1)

In R_out the walk runs ℓ, T, b6 and then along h1. If h1 is the thread t_i, the next w-passages are the W's on t_i, followed by b3. b3 is never on a cut, because w's cut is ℓ. So, writing m_i for the number of W's on t_i:

    t + ℓ_i = 10 m_i + 10 + q,   with q ∈ [1, 9].

Hence ℓ_i ≥ u + 21 whenever m_i ≥ 2, and the v115 arm table then kills t_i.

**(L-K1).** If h1 = t_i then m_i ≤ 1. By row reversal, if h5 = t_j then m_j ≤ 1.

## 4. The exact remaining gap

**L2 with k = 3.** The finite family of v116 §4: a type in {A, B, C, E}, an n-vector, u, and the type's three free offsets. It is subject to:
- the length and ρ/φ formulas of v116 §2;
- the arm table and the OL windows;
- the row-level tests (V-placement, alternation of w, exchanges);
- minus the closed cells of §2.

The live cells are:

| Type | Live cells |
|---|---|
| A | (1,1,0,0) with λ = 14 and u ≤ 6; (1,0,0,1) with λ = 16; (0,2,0,0); (0,1,1,0); (0,1,0,1); (0,0,1,1) |
| B | (1,1,0,0); (1,0,1,0); (0,2,0,0); (0,1,1,0); (0,1,0,1); (0,0,1,1); minus (K5) |
| C, E | all eight vectors with n1, n3 ≤ 1 |

**L1.** Types 1–4 and 7–12, with every n-vector, every position of v's cut, every u and every corner offset, subject to:
- (L-a)–(L-e) of v117;
- (L-K1);
- OL;
- the row-level tests.

**The distance-two gap.** No cell of the residual has been excluded by (R3). Conditions (C1), (C2) and Theorem A of v108–v109 have not yet been applied to these families. Exactly that coupling is open:
- the distinct neighbour pairs of fully internal 2-vertices;
- distinct corner turns;
- the 99 internal K-entries.

No example is chosen. No method-exhaustion claim is made.

## 5. Result

**WRITTEN:**
- L4-B is closed;
- L1 types 5 and 6 are closed;
- the closed L2 cells of §2;
- the lemmas DP-1, DP-2 and OL;
- (L-K1).

The support-9 statement is **not** made, because L1 and L2 (k = 3) are not fully excluded. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
