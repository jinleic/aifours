# Original Tuscan-2(11), entire m = 9 distance-two branch, part 15: type E (1,1,0,0) with x1 = 1 and u ≥ 5 excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-D2Q-lemma-mirror-typeE-1100-x1eq9-excluded-v125.md` (SHA256 `85fcc86caa10a2ae94a8297a211a4d5577f034ffd30acbe69a1ec056b3847ec0`), and uses that packet's notation and Lemma D2Q (§1 there, which uses R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up (x1 = 1)

**Parameters.**
- ρ1 = 6, so p1 ≤ 6.
- x0 ≡ 6 − p1 ≠ 0, so p1 ≤ 5 and x0 = 6 − p1.

**F2 positions** (mod 60).
- K3 at x0, and t1[j] at 16 + u − j.
- b4 at 16 + u, and t2[j] at 16 + u + j.
- K2 at 31, and Λ[k] at 31 + λ − k.
- K1 at 41 + p2 − p1.
- t2[j] (backward pass) at 56 + p2 − p1 − u − j, and b4 again at 56 + p2 − p1 − u.

**Constraints on p2.**
- K1 lies in row 4, so p1 ≤ p2.
- p2 = 9 would put Λ[10−p1] on a cut in both faces (ρΛ = 0), so p2 ≤ 8.

**Rows, for u ≥ 5.**

| Face | Row | Vertices |
|---|---|---|
| F1 | R_out | ℓ, T_int, b4, t1[1..u] |
| F1 | r1 | t1[u..u+10] |
| F1 | r2 | t1[u+10..u+9+p1], b5, Λ[1..10−p1] |
| F1 | r3 | Λ[10−p1..λ−1], b5, t3[ℓ3−1..u] |
| F1 | R_in | t3[u..1], b4, T_int, ℓ |
| F2 | s0 | T3, K3, t1[u+9+p1..u+6] (T3 is the 6 − p1 vertices before K3) |
| F2 | s1 | t1[u+6..u−4] |
| F2 | s2 | t1[u−4..1], b4, t2[1..14−u] |
| F2 | s4 | Λ[λ−9..1], K1, t2[14−u..6+p2−p1−u] |
| F2 | s5 | t2[6+p2−p1−u..1], b4, t3[1..4−p2+p1+u] |

s5 must carry V2's second passage, so p2 − p1 ≥ u − 5.

**The C-block.** Exchanging r1 with s1 gives:

    Q := L(t1[u+7..u+10]) = L(P′),   with P′ = t1[u−4..u−1].

The interiors of P′ and P are t1[u−3], t1[u−2], t1[u+8] and t1[u+9]. None is on a cut, because the t1 cuts are at u, u+10, u+6 and u−4. So D2Q applies.

**Two consequences.**
- **(U1)** P′ lies inside t1[1..u], so Q ⊆ S.
- **(b′)** Exchanging r2 with s0 gives L(Λ[1..10−p1]) = L(T3) ⊔ {L(t1[u+6]), q1, q2, q3}, where qi = L(t1[u+6+i]).

## 2. u = 8 is forced

**(U2) u ≥ 8.** The arm t3[1..u] is a sub-path of row R_in, disjoint from t1, and it carries S ⊇ Q. By D2Q, four Q-labels need u ≥ 8.

**(U3) u ≤ 8.** Exchanging R_out with s2 (common part b4, t1[1..u−4]) gives:

    L(t2[1..14−u]) = {v} ∪ T_int ∪ L(t1[u−3..u]).

This contains Q ∖ {q*}, where q* = L(t1[u−4]). By D2Q, 14 − u ≥ 6.

**Placement at u = 8.** The only placement of four Q-labels on t3[1..8] is at positions 1, 3, 6, 8, with gaps 2, 3, 2. So:
- c2 = L(t3[8]) ∈ Q;
- p2 − p1 ≥ 3.

## 3. u = 8 is impossible

Exchanging s2 = t1[4..1], b4, t2[1..6] with s5 gives:

    L(t3[1..12−p2+p1]) = L(t1[1..4]) ⊔ L(t2[p2−p1−1..6]),   with Q ∩ L(t1[1..4]) = {q*}.

**p2 − p1 ∈ {3, 4}.** The left side contains t3[1..8], hence all of Q. So the t2-piece carries Q ∖ {q*}, three Q-labels on at most 5 vertices. This contradicts D2Q.

**p2 − p1 = 6.** t3[1..6] carries three Q-labels, at positions 1, 3 and 6. The right side carries at most two: q*, and at most one Q-label on the adjacent pair t2[5..6]. Contradiction.

**p2 − p1 = 5**, so p1 ≤ 3.
1. t3[1..7] carries three Q-labels, so t2[4] and t2[6] carry Q-labels.
2. Exchanging R_in = t3[8..1], b4, τ, ℓ with s5 = t2[3..1], b4, t3[1..7] gives L(t2[1..3]) = {c2, τ, v}. So L(t2[6]) ≠ c2, because s2 is a row.
3. Exchanging r3 with s3 gives L(t3[8..12−p1]) = {L(t2[6])} ⊔ L(Λ[6..9−p1]). So L(t2[6]) lies on t3[9..12−p1], which is inside T3 = t3[7..12−p1].
4. By (b′), L(t2[6]) lies on Λ[1..10−p1] but is none of q1, q2, q3. So L(t2[6]) = q4 = L(t1[18]).

Row r2 then contains q4 twice. Contradiction.

**p2 − p1 = 7**, so (p1, p2) = (1, 8).
1. The s2/s5 relation becomes L(t3[1..5]) = L(t1[1..4]) ⊔ {L(t2[6])}. Since t3[1] and t3[3] carry Q-labels, L(t2[6]) ∈ Q.
2. Exchanging R_in with s5 = t2[5..1], b4, t3[1..5] gives L(t2[1..5]) ∋ c2, so L(t2[6]) ≠ c2.
3. The r3/s3 relation, L(t3[8..9]) = {L(t2[6])} ⊔ {L(Λ[8])}, then gives L(t2[6]) = L(t3[9]) ∈ L(T3), where T3 = t3[5..9].
4. By (b′), L(t2[6]) = q4 lies on Λ[1..9].

Row r2 = t1[18], b5, Λ[1..9] then contains q4 twice. Contradiction.

**p2 − p1 = 8** would need p2 = 9, which is excluded.

## 4. Result

**WRITTEN, D2Q uses (R3):** type E, cell (1,1,0,0), with x1 = 1 and u ≥ 5, is impossible. Together with v125 §3, the only remaining part of type E (1,1,0,0) is x1 = 1 with u ≤ 4, and its mirror in (0,1,1,0).

**Other residual:** as in v125 §4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
