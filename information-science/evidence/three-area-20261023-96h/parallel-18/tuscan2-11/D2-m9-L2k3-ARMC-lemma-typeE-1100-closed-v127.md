# Original Tuscan-2(11), entire m = 9 distance-two branch, part 16: the arm C-block lemma ARM-C, and type E (1,1,0,0) closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-1100-x1eq1-u-ge5-excluded-v126.md` (SHA256 `94a97cf4bb6b37bc34c45889f5f4e89f40a8b1a3609ba1660dbc24ed46c32845`). Notation is that of v116, and Lemma D2Q is v125 §1, which uses R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. §2 and §3 use (R3).

## 1. u = 1 is impossible in L2 (k = 3)

The arm rows end on cuts at t1[u] (the end of R_out) and at t3[u] (the start of R_in). So c1 = L(t1[u]) and c2 = L(t3[u]) are cut labels, and by (C) they are distinct.

If u = 1, then S = {c1} = {c2}. Contradiction.

## 2. Lemma ARM-C (uses R3)

**Hypotheses.** Suppose t1 has:
- a forward row r1 = t1[u..u+10] in the face of R_out;
- a backward pass whose cuts sit at indices ≡ u + 6, so ρ1 = 6.

The backward row s1 runs from t1[u+6] down through t1[1], then b4, then into t2 = σ_b4(t1). Exchanging r1 with s1 gives:

    Q := L(t1[u+7..u+10]) = L(P′),

where P′ is the 4 vertices of s1 after t1[u]:
- P′ = t1[u−4..u−1] if u ≥ 5;
- P′ = t1[u−1..1], b4, t2[1..4−u] if u ≤ 4.

The interiors of P = t1[u+7..u+10] are t1[u+8] and t1[u+9]. They are not on cuts, because the t1 cuts are at u, u+10, u+6 and u−4.

**Claim.** u ∈ {8, 9}.

*u = 2.*
- S = {c1, c2}, with t1[1] = c2, t3[1] = c1 and t3[2] = c2.
- P′ = (c2, w, τ1, τ0), where τi = L(t2[i]). By (E), P is the complementary path τ1–c2–τ0–w.
- The τ0-vertex of P is interior and not on a cut, so it produces both (c2, w) and (w, c2).
- But R_in = t3[2], t3[1], b4, … produces (c2, w) at t3[1].
- This contradicts (R3).

*u = 3.*
- S = {c1, c2, s3}, and L(t1[1..2]) = {c2, s3} ⊆ Q.
- On t3[1..3], which lies inside R_in, these two Q-labels are not adjacent, by (E). So t3[1] = s3, t3[2] = c1 and t3[3] = c2. Then R_in produces (c2, s3) at t3[2].
- The pair {c2, s3} is the end edge t1[2]–t1[1] of P′ = (t1[2], t1[1], b4, t2[1]). In P it therefore lies at distance 2, around an interior vertex that is not on a cut. So P also produces (c2, s3).
- This contradicts (R3).

*u = 4.*
- L(t1[1..3]) = S ∖ {c1} ⊆ Q.
- t3[1..4] carries all of S, so three Q-labels lie on four consecutive vertices of R_in. Two of them are adjacent, which contradicts (E).

*u ∈ {5, 6, 7}.*
- P′ lies inside the arm t1[1..u], so Q ⊆ S.
- t3[1..u] carries S. By D2Q, its four Q-labels need u ≥ 8.

**By the mirror (v125 §2):** the same holds for t3 when its other pass has ρ3 = 4, that is, when its block is the mirror of a C-block.

## 3. Type E (1,1,0,0), x1 = 1, is impossible

For x1 = 1 the arm has ρ1 = 6, and the hypotheses of ARM-C hold:
- r1 is an F1 row;
- s1 is the F2 row through t1[u+6..u−4], or down through b4.

So u ∈ {8, 9}. Two results from v126 finish the case:
- **u = 9** is excluded by (U3): fewer than 6 vertices of t2 would carry three Q-labels.
- **u = 8** is excluded by v126 §3.

Together with v125 §3 (x1 = 9):

**WRITTEN, uses (R3): type E cell (1,1,0,0) is impossible, and by the mirror so is (0,1,1,0).**

## 4. Result and residual

**WRITTEN:**
- u ≥ 2 in L2 with k = 3 (§1);
- Lemma ARM-C and its mirror (§2), using (R3);
- type E (1,1,0,0) and (0,1,1,0) are closed (§3).

**Residual:**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | the five mirror classes |
| E | (0,2,0,0), (0,1,0,1), (1,0,1,0), and (1,0,0,1) ≅ (0,0,1,1) |
| L1 | types 1–4 and 7–12 |

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
