# Original Tuscan-2(11), entire m = 9 distance-two branch, part 25: type C (0,1,0,1) closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-0101-delta-minus4-closed-v136.md` (SHA256 `642135bc8060949872b6203c831304bd84d4f0cba17e7a45eb8de36a66b27953`), with the notation of v133 §1. RC is v134 §1; D2Q (v125 §1) and R3-pair (v130 §1) use R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Row facts for δ′ > 0

The loop's two passes give four rows:
- s0 = Λ[α′+10..λ−1], K3, t1-top. Its Λ-part has x0 vertices, and its t1-top has 10 − x0.
- s2 = t2-part (x1 vertices), K2, Λ[λ−1..β′+10].
- s4 = Λ[β′..1], K1, t2-tail (10 − β′ vertices).
- s6 = t3-part (x3 vertices), K5, Λ[1..α′].

Exchanging s4 with s6 (common part b5, Λ[1..α′]) gives:

    L(t3-part of s6) = L(Λ[α′+1..β′]) ⊔ L(t2-tail).

Hence **x3 ≥ δ′**.

## 2. δ′ ∈ {5, 6} is impossible

**δ′ = 5.** Here ρΛ = 5, so OL requires x0 + p1 ≤ 10. Then x3 ≡ 20 − x0 − p1 lies in [1, 4]. That contradicts x3 ≥ 5.

**δ′ = 6.** Here ρΛ = 6, so OL requires x0 + p1 ≤ 11. Then x3 ≡ 21 − x0 − p1 lies in [1, 3]. That contradicts x3 ≥ 6.

## 3. δ′ = 4 is impossible

**Parameters.** x0 + x1 = 14 and β′ = α′ + 4. Exchanging the two pure rows s7 and s3 gives:

    Q = L(Λ[α′..α′+3]) = L(Λ[α′+11..α′+14]).

P′ ⊆ Λ forces x0 ≥ 5. Every Q-label has its P-vertex in s4 and its P′-vertex in s3 and in s0.

**Bounds.**
- **s4 with s6:** {q2, q3, q4} lies on s6's t3-part. By D2Q, x3 ≥ 6.
- **s2 with s0:** F′ = Q ∖ {q_last}, the first three labels of P′, lies on s2's t2-part. By D2Q, x1 ≥ 6, so x0 ≤ 8.
- **RC:** an F′-label's t2-vertex in s2 must make its backward passage outside s4. So F′ lies on the window W = t2[ℓ2−x1..ℓ2−11+β′], which has x1 + β′ − 10 = p1 − 1 vertices. By D2Q, p1 ≥ 7.
- **OL and the v-order:** x0 + p1 ≤ 14, and x3 = 19 − x0 − p1 ≥ 6 gives x0 + p1 ≤ 13. So (x0, p1) ∈ {(5,7), (5,8), (6,7)}.

**Capacity.** Exchanging M with s0 gives:

    L(Λ[α′+10..λ−1]) = L(t1[u..ℓ1−11+x0]) ⊔ L(t3[u..ℓ3−1]),

and the left side contains all of Q.

| (x0, p1) | t1-piece | t3-piece | Room for non-adjacent Q-labels |
|---|---|---|---|
| (5,7) | 2 vertices | 3 vertices | at most 1 + 2 = 3, too few |
| (5,8) | 3 vertices | 2 vertices | at most 2 + 1 = 3, too few |
| (6,7) | 3 vertices | 3 vertices | exactly 4 |

**The case (6,7).** Here x1 = 8, x3 = 6, λ = 20, α′ = 4 and β′ = 8.
- Q sits at t1[u] = c1, t1[u+2], t3[u] = c2 and t3[u+2].
- Exchanging M with s6 gives q1 ∈ L(t1[u..ℓ1−1]). The cut of q1 lies on Λ, so q1 ∉ {c1, c2}, and therefore q1 = L(t1[u+2]).
- By D2Q, {c1, q1} is special, so c1 = q4.
- Then {c2, L(t3[u+2])} = {q2, q3}. Since q_last is cut in F2 and c2 is not, q_last = L(t3[u+2]).

The window W = t2[7−u..12−u] has six vertices and carries F′ = {q1, c1, c2}. By D2Q it realises the special pair {q1, q4} = {q1, c1} at a non-cut middle, because the t2 cuts are at 7−u, 13−u and 3−u.

The same pair is realised at t1[u+1]. That vertex is a non-cut 2-vertex: the t1 cuts are at u and u+3, and its F2-passage lies inside s1.

R3-pair gives a contradiction.

## 4. Result

**WRITTEN, uses (R3):** type C cell (0,1,0,1) is impossible. With v133, v134 §3 and v136 it is closed in full.

**Residual of the L2 (k = 3) family:**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0) |
| E | (0,2,0,0) |

**L1:** types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
