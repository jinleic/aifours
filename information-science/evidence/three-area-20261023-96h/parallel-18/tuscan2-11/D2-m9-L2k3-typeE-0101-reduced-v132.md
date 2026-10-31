# Original Tuscan-2(11), entire m = 9 distance-two branch, part 20: type E (0,1,0,1) reduced to one sign of the loop shift

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-branch-consolidated-status-and-exact-gap-v131.md` (SHA256 `5df681745478e6184c539012cd1c695a046a54b37a5251920aba7f5d0cfda417`). Notation is that of v116 §2 (type E). D2Q is v125 §1 and R3-pair is v130 §1; both use R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Cell parameters.** Cell (0,1,0,1) has n2 = nΛ = 1, a = 5 and b = 6. Then:
- ℓ1 = p1 + u, ℓ2 = 15 − u, λ = 20 + p2 − p1 and ℓ3 = 10 − p2 + u;
- x0 = x1 + 5 − p1 ∈ [1, 9];
- x2 = x1 + p2 − p1 ∈ [1, 9], since K2–VΛ–K1 span two cuts.

**Cuts on Λ.**
- In F1 the cuts sit at α = 10 − p1 and α + 10.
- In F2 they sit at β = x2 and β + 10.
- Put δ = β − α = x1 + p2 − 10.

Lemma OL (the nΛ = 1 screen for type E) leaves:
- ρΛ = 4 with p1 ≥ 4;
- ρΛ = 5 with p1 ≥ 5 and p2 ≤ 5;
- ρΛ = 6 with p2 ≤ 6.

**Rows.**

| Face | Row | Vertices |
|---|---|---|
| F1 | r1 | t1[u..u+p1−1], b5, Λ[1..α] |
| F1 | r2 | Λ[α..α+10] |
| F1 | r3 | Λ[α+10..λ−1], b5, t3[ℓ3−1..u] |
| F2 | s0 | T3, K3, (the top 10 − x0 vertices along t1) |
| F2 | s2 | t2[ℓ2−x1..ℓ2−1], K2, Λ[λ−1..β+10] |
| F2 | s3 | Λ[β..β+10] |
| F2 | s4 | Λ[β..1], K1, (the t2-tail of 10 − β vertices) |

## 2. Only δ = ±4 is possible

| Shift | Condition it needs | Contradiction |
|---|---|---|
| δ = −5 (ρΛ = 5) | p1 ≥ 5 | β = 5 − p1 ≤ 0 |
| δ = −6 (ρΛ = 4) | p1 ≥ 4 | β = 4 − p1 ≤ 0 |
| δ = 5 | p2 ≤ 5 | x1 = 15 − p2 ≥ 10 |
| δ = 6 | p2 ≤ 6 | x1 = 16 − p2 ≥ 10 |

## 3. δ = −4 is impossible (uses R3)

**Parameters.** x1 + p2 = 6, β = 6 − p1 = α − 4 and ρΛ = 6. Since β ≥ 1, p1 ≤ 5. Exchanging r2 with s3 gives:

    Q = L(Λ[β..β+3]) = L(Λ[β+11..β+14]),   P = (q1, q2, q3, q4).

The cuts on Λ sit at β, β+4, β+10 and β+14, so the interiors of both Q-paths are not on cuts.

**Exchanges.**
- **r1 with s4:** the t2-tail carries Λ[β+1..β+3] = {q2, q3, q4}.
- **r3 with s2:** L(t3[u..ℓ3−1]) = L(s2's t2-part) ⊔ L(Λ[β+10..β+13]). Row r3 contains q_last = L(Λ[β+14]) ∈ {q2, q3}, so t3[u..ℓ3−1] carries exactly the three Q-labels of Λ[β+11..β+13]. By D2Q, 10 − p2 ≥ 6, so p2 ≤ 4. Also, s2's t2-part carries no Q-label.

**The t2-piece.** The three Q-labels therefore lie on t2[5+β−u..8+p2−u], which has p1 + p2 − 2 vertices. By D2Q this needs p1 + p2 ≥ 8. They also force a gap-2 realisation of the pair {q2, q3} at a middle vertex inside this piece. That middle is not on a cut: the forward t2 cuts sit at indices ≡ p2 − 1 − u, and the backward cut at 5 + β − u is the first vertex of the piece.

**r1 with s0.** This exchange gives L(Λ[1..α]) = L(T3) ⊔ L(arm part), where:
- the arm part is the p2 − 1 vertices of s0 below t1[u];
- |T3| = x0 = 11 − p1 − p2;
- T3 ⊆ t3[u..ℓ3−1] cannot carry q_last.

Λ[1..α] contains all of Q, with p1 ≤ 5, p2 ≤ 4 and p1 + p2 ≥ 8. Counting non-adjacent Q-labels on T3 and on the arm part then leaves only (p1, p2) = (4, 4), where both have three vertices. There T3 and the arm part each carry two Q-labels at distance 2:
- the arm pair contains q_last, so it is {q2, q3};
- its middle is t1[u−2], or t1[1] when u = 3; both are non-cut 2-vertices;
- when u = 2 the middle is the b4 corner, and the non-cut t2 middle then supplies both orders.

Either way R3-pair gives a contradiction.

## 4. What remains: δ = 4

**Parameters.** x1 + p2 = 14, β = 14 − p1 = α + 4 and ρΛ = 4. Then:

    Q = L(Λ[α..α+3]) = L(Λ[α+11..α+14]).

**Three facts.**
- t1[u..u+p1−1] carries {q2, q3, q4}, so p1 ≥ 6 by D2Q.
- s2's t2-part carries the first three labels of P′, so x1 ≥ 6.
- q1 = L(Λ[α]) lies on T3. But t3[u..ℓ3−1] carries no Q-label, because r3 ⊇ P′. So q1 lies on the part of T3 below t3[u], which has 9 − p1 vertices. Hence p1 ≤ 8.

**Placing {q2, q3, q4} on t1.** The exchange r1/s0 gives L(T3) = L(t1[u..u+x1−6]) ⊔ L(Λ[1..α]). The Q-labels of T3 all lie on its part below t3[u]. So every Q-label on t1[u..u+x1−6] also lies on that part, next to q1.

| p1 | Room below t3[u] | Consequence |
|---|---|---|
| 8 | one vertex, holding q1 | {q2, q3, q4} lie on t1[u+x1−5..u+7]; by D2Q, x1 ≤ 7 |
| 7 | two adjacent vertices, so only q1 | {q2, q3, q4} lie on t1[u+x1−5..u+6]; by D2Q, x1 = 6 |
| 6 | three vertices | D2Q on the six vertices t1[u..u+5] puts a Q-label on t1[u] = c1. So c1 lies two steps from q1, {q1, c1} is special, and c1 = q4 |

**One case closed (uses R3).** For p1 = x1 = 6 with u ≥ 4, the pair {q1, q4} is realised twice: at t3[u−2], a non-cut middle, and at a middle of s2's six-vertex t2-part. R3-pair gives a contradiction.

**OPEN residual of type E (0,1,0,1):**
- δ = 4 with (p1, x1) ∈ {(8,6), (8,7), (7,6), (6,7), (6,8), (6,9)};
- (6,6) with u ≤ 3.

## 5. Result

**WRITTEN:**
- type E (0,1,0,1) with δ ≠ 4 is impossible; the case δ = −4 uses (R3);
- δ = 4 is reduced to the OPEN list of §4.

Every other residual item of v131 §3 is unchanged. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
