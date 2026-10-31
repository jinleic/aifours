# Original Tuscan-2(11), entire m = 9 distance-two branch, part 19: type C (1,1,0,0) with ρ1 = 6 excluded, and with ρ1 = 4 reduced

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-1001-excluded-1100-reduced-v129.md` (SHA256 `13bd2fed9b2caa79cd31fe75a7a44087ad218e21b9527eb466e54ad3b08087e3`). Notation is that of v129 §1 and §3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R3) directly and through D2Q.

## 1. Fact R3-pair

Suppose y and y′ are distinct vertices, and each has, in some passage interior to its row, path-neighbours labelled a and b. If y is a 2-vertex with neither passage on a cut, then y produces both (a,b) and (b,a), and y′ produces at least one of them. This contradicts (R3).

**Consequence for D2Q.** For a saturated Q, D2Q leaves the two special pairs {q1,q4} and {q2,q3}. Each of them can be realised at distance 2 around a non-cut middle vertex at most once in the whole array.

## 2. Type C (1,1,0,0) with ρ1 = 6 is impossible

### Set-up

**Parameters.**
- x0 + p1 = 6, so p1 ≤ 5. By ARM-C+, u = 8.
- λ = 11 − x1, ℓ2 = 6 + x1 and ℓ3 = 18 − p1.
- T_int = {τ}.

**F2 positions** (mod 70).
- t1[j] at 24 − j, and b4 at 24.
- t2[j] at 24 + j.
- K2 at 30 + x1, Λ[k] at 41 − k, and K1 at 41.
- t2[j] (backward pass) at 47 + x1 − j, b4 again at 47 + x1, and t3[j] at 47 + x1 + j.

**Rows.**

| Row | Vertices |
|---|---|
| s2 | t1[4..1], b4, t2[1..6] |
| s3 | t2[6..5+x1], K2, Λ[10−x1..1] |
| s4 | Λ[1], K1, t2[5+x1..x1−3] |
| s5 | t2[x1−3..1], b4, t3[1..13−x1] |

### Three consequences of the ARM-C setting

1. Q = L(t1[15..18]) = L(t1[4..7]) ⊆ S. By D2Q on t3[1..8], which lies inside R_in, the Q-labels sit at t3[1], t3[3], t3[6] and t3[8]. So c2 ∈ Q, and the pairs {L(t3[1]), L(t3[3])} and {L(t3[6]), c2} are the two special pairs.
2. Exchanging R_out with s2 gives L(t2[1..6]) = {v, τ, c1} ∪ (Q ∖ {q*}), where q* = L(t1[4]). By D2Q, Q-labels sit at t2[1] and t2[6], and at t2[3] or t2[4].
3. V2 must lie in s2 and in s5, but not in s3 or s4. This forces x1 ≥ 5, and then exchanging R_in with s5 gives:

       L(t2[1..x1−3]) = L(t3[14−x1..8]) ∪ {τ, v}.

### The values of x1

| x1 | Outcome |
|---|---|
| 5 | L(t2[1..2]) = {τ, v}, but t2[1] carries a Q-label. Contradiction. |
| 7 | t2[1..4] carries only one Q-label (t3[7] is not a Q-label), but needs two. Contradiction. |
| 9 | t3[5] and t3[7] would both carry c1. Contradiction. |
| 6 | Excluded by R3-pair (below). |
| 8 | Excluded by R3-pair (below). |

**x1 = 6.**
- L(t2[1..3]) = {τ, v, c2}, so t2[1] = c2. The Q-pattern is then 1, 4, 6, with {L(t2[4]), L(t2[6])} special.
- The special pairs are therefore {L(t2[4]), L(t2[6])} and {c2, q*}. By point 1 of the consequences above, {L(t3[1]), L(t3[3])} = {L(t2[4]), L(t2[6])}.
- Then t3[2], which is interior in R_in and in s5, and t2[5], which is interior in s2 and in s4, carry the same neighbour pair.
- R3-pair gives a contradiction.

**x1 = 8.**
- L(t2[1..5]) = {τ, v, L(t3[6]), c1, c2}, with t3[7] = c1.
- The pattern 1, 4, 6 would pair t2[4] with t2[6], but t2[4] already lies in the special pair {L(t3[6]), c2}. So the pattern is 1, 3, 6, with {t2[1], t2[3]} = {L(t3[6]), c2}.
- Then t2[2], interior in s2 and in s5, and t3[7], interior in R_in and in s6, carry the same neighbour pair.
- R3-pair gives a contradiction.

## 3. Type C (1,1,0,0) with ρ1 = 4: reduction

From v129 §3, (x1, p1) ∈ {(6,7), (6,8), (7,8)}. Recall Q′ = L(t1[u..u+3]) = L(t1[u+11..u+14]).

**Q′ ∖ {c1} ⊆ T_int.** Exchanging R_out with r1 gives L(t1[u+1..u+10]) = {v, w} ∪ T_int ∪ (S ∖ {c1}). Row s2 contains t1[1..u+3] and b4, so Q′ ∩ S = {c1} and w ∉ Q′. Also v ∉ Q′, because n1 = 1.

**u ≤ 3.** T_int lies on T = T[1..9−u], a sub-path of R_out that is disjoint from t1. By D2Q, three Q′-labels there need 9 − u ≥ 6.

**The pair {q′1, q′4}.** Among Q′ ∖ {c1} = {q′1, q′4, q′_o}, the only special pair is {q′1, q′4}.
- When |A1| = 5 + p1 − x1 = 6, that is for (6,7) and (7,8), A1 must realise {q′1, q′4} at a gap of 2.
- At u = 3, T has 6 vertices and must realise it as well. Both middles are non-cut 2-vertices, so R3-pair gives a contradiction.
- Hence (6,7) and (7,8) force u = 2, with T carrying its three Q′-labels at T[1], T[4] and T[7].

**OPEN residual of this sub-case:**
- (6,7) and (7,8) with u = 2 and T-pattern 1, 4, 7;
- (6,8) with u ∈ {2, 3}.

## 4. Result

**WRITTEN, uses (R3):**
- Fact R3-pair (§1);
- type C (1,1,0,0) ≅ (0,1,1,0) with ρ1 = 6 is impossible (§2);
- the ρ1 = 4 sub-case is reduced to the OPEN list of §3.

**Residual:**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0), (0,1,0,1), and the §3 OPEN list of (1,1,0,0) |
| E | (0,2,0,0), (0,1,0,1) |
| L1 | types 1–4 and 7–12 |

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
