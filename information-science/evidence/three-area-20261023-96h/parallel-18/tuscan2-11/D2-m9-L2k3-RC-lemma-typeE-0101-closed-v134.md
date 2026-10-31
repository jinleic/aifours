# Original Tuscan-2(11), entire m = 9 distance-two branch, part 22: row coverage (RC), and type E (0,1,0,1) closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-0101-shift-screen-v133.md` (SHA256 `ffb46131b119660a8e40742c63d987c0ba0a40d88a70e67fd28ca677606c20f9`) and completes `D2-m9-L2k3-typeE-0101-reduced-v132.md` (SHA256 `d1f51603a7728e7efca3be8e171cfd390511b7ea6294ce78ebab110b9616df1c`), with that packet's notation. D2Q is v125 §1 and R3-pair is v130 §1; both use R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Lemma RC (row coverage)

Every row contains each label exactly once, and each label has exactly one cut. Combined with the face identity (I), this gives the following:
- the passages of a label x in a face F lie in pairwise distinct rows of F;
- the only exception is x's cut vertex, if it lies in F, which occupies two adjacent rows;
- the passages cover all rows of F.

**Face counts in type E (0,1,0,1)** (a = 5, b = 6). A T-vertex has two F1-passages. A t1-, t3- or Λ-vertex has one passage in each face. A t2-vertex has two F2-passages.

The F1 cuts sit at ℓ, t1[u], Λ[α], Λ[α+10] and t3[u]. So the F1-cut labels are v, c1, c2, q1 = L(Λ[α]) and λ** = L(Λ[α+10]). Every other label has its cut in F2. In particular:
- an S-label with its cut in F2 has all five vertices on t1 ∪ t3 ∪ Λ;
- a T_int-label with its cut in F2 has one vertex on T, three on t1 ∪ t3 ∪ Λ, and one on t2.

## 2. Type E (0,1,0,1) with δ = 4 is impossible

**Recall (v132 §4).**
- x1 + p2 = 14, β = α + 4 and p1 ∈ {6, 7, 8}.
- Q = L(Λ[α..α+3]) = L(Λ[α+11..α+14]) with P = (q1, q2, q3, q4).
- q_last = L(Λ[α+14]) ∈ {q2, q3}, and F := Q ∖ {q_last}.
- (X1): t1[u..u+p1−1] carries q2, q3 and q4.
- (X2): s2's t2-part carries F.
- T3's Q-labels lie on the part B3 of T3 below t3[u], which has 9 − p1 vertices. Also q1 ∈ L(B3), and L(T3) ⊇ L(t1[u..u+x1−6]).

**Extra bound.** V2's forward passage lies strictly inside s1. So b4 sits at 5 + x1 + u ≤ 18, that is, u ≤ 13 − x1. Hence s2's t2-part is the pure path t2[15−u−x1..14−u], with x1 vertices.

**Step 1: F ∖ {q1} = {c1, τ*}, where τ* := L(t1[u+x1−5]), the t1-vertex on the s0/s1 cut.** Each label of F has a vertex on t2. The candidates fall as follows:
- **S-labels cut in F2:** they have no t2-vertex, so they are excluded.
- **w:** w ∈ Q would need W's on P, on P′, on t1 and on t2, which is four W's. Excluded.
- **λ\*\*:** it would need three Λ-vertices, which is too many for either face count. Excluded.
- **c2:** to lie in F ∖ {q1} it must lie on t1[u..u+p1−1], but its four t1/t3/Λ-vertices are t3[u], a t1-arm vertex, a P-vertex and a P′-vertex. Excluded.
- **A T_int-label τ ∈ F ∖ {q1}:** its five F2-passages are its P-vertex (s4), its P′-vertex (s3), its t2-vertex (forward in s2, backward in s5) and its t1-vertex. By RC that t1-vertex must cover both s0 and s1, so it is the s0/s1 cut, and τ = τ*.

What remains is c1 and τ*, and |F ∖ {q1}| = 2.

**Step 2: p1 = 6 and c1 = q4.**
- c1 = L(t1[u]) lies in L(t1[u..u+x1−6]) ⊆ L(T3). Its only t3-vertex is its arm vertex, so c1 lies on B3 together with q1.
- For p1 ∈ {7, 8}, B3 has at most two vertices, so q1 and c1 cannot both sit there non-adjacently.
- So p1 = 6, and B3 = (q1, ·, c1) up to order. By D2Q, {q1, c1} is special, so c1 = q4.

**Step 3: x1 = 8.** t1[u..u+5] carries {q4, τ*, q_last}, with q4 at t1[u]. D2Q forces the pattern 1, 4, 6, with {t1[u+3], t1[u+5]} = {τ*, q_last}. (The pattern 1, 3, 6 would pair q4 with q2 or q3, which is not special.) Since τ* = L(t1[u+x1−5]), this gives x1 = 8, and then u ≤ 5.

**Step 4: contradiction.** Take x1 = 8 and p1 = 6. In F2 (mod 60):
- t2[j] sits at 13 + u + j going forward and at 63 − u − j going backward;
- s2's t2-part is t2[7−u..14−u];
- s4 ends at the cut t2[13−u], and s5 = t2[13−u..1], b4, ….

Each of q1, c1 and τ* has its P-vertex in s4. By RC, its t2-vertex from (X2) must avoid t2[13−u] and t2[14−u], so it lies in t2[7−u..12−u].
- By D2Q these three Q-labels include a gap-2 pair, and the pair must be special. Since τ* ∈ {q2, q3}, the special pair is {q1, q4}.
- Its middle is a non-cut 2-vertex, because the t2 cuts are at 7−u, 13−u and 3−u. So it produces both orders.
- The same pair {q1, q4} is realised on B3, at the following middle:
  - for u ≥ 4, at t3[u−2], a non-cut 2-vertex;
  - for u = 3, B3 = t3[2], t3[1], b4 would make q1 and c1 adjacent or equal to w, which is impossible;
  - for u = 2, B3 = t3[1], b4, t2[1], and the middle is the b4 corner.

R3-pair gives a contradiction in every case.

## 3. Result

**WRITTEN, uses (R3):** type E cell (0,1,0,1) is impossible. With v132 this closes the cell completely.

**Residual (v131 §3, updated):**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0); (0,1,0,1) as in v133 (with x0 = 1 also excluded: the exchange M/s_K5 forces all of Q onto t1[u..ℓ1−1], which s_K3 forbids for q_last); the (1,1,0,0) list of v130 §3 |
| E | (0,2,0,0) |
| L1 | types 1–4 and 7–12 |

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
