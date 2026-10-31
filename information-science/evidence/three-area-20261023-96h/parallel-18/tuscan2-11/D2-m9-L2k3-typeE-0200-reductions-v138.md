# Original Tuscan-2(11), entire m = 9 distance-two branch, part 26: type E (0,2,0,0) — reductions

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-0101-closed-v137.md` (SHA256 `2c3383e18cf486da3deeedf05ea83cbca4d0496319d13e4f4caadb39cd9ef603`). Notation is that of v116 §2 (type E). RC is v134 §1; D2Q (v125 §1) uses R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Parameters.**
- a = 4 and b = 7.
- ℓ1 = p1 + u, ℓ3 = 10 − p2 + u, λ = 10 + p2 − p1 and ℓ2 = 25 − u.
- The F2 v-order is K3, V_a, V_b, K2, K1, V_b, V_a.

**F2 rows.** Put A = 15 − x1 − u and B = x2 + 5 − u.

| Row | Vertices |
|---|---|
| s0 | T3 = t3[5+u−x2..ℓ3−1], K3, T1 = t1[x1+u−5..ℓ1−1] |
| s1 | t1[x1+u−5..1], b4, t2[1..A] |
| s2 | t2[A..A+10] |
| s3 | t2[A+10..A+9+x1], K2, Λ[λ−1..x2] |
| s4 | Λ[x2..1], K1, t2[ℓ2−1..B+10] |
| s5 | t2[B+10..B] |
| s6 | t2[B..1], b4, t3[1..5+u−x2] |

Rows s2 and s5 are pure t2-rows. Put d := B − A = x1 + x2 − 10 ≡ ρ2.

**F1 rows.**
- M1 = t1[u..u+p1−1], b5, Λ[1..10−p1].
- M2 = Λ[10−p1..λ−1], b5, t3[ℓ3−1..u].

## 2. General reductions

**(a) Mirror.** Row reversal maps this cell to itself, exchanging t1 and t3 and sending (x1, x2) to (10 − x2, 10 − x1). So d ↦ −d, and **we may take d > 0.**

**(b) DP-1.** Comparing s2 with s5, |d| ∉ {0, 1, 2, 3}. Comparing s2 with s6 (for d ∈ {7, 8}) leaves complementary blocks of size 10 − d ∈ {3, 2}, on paths in different regions, which DP-1 also forbids. **So d ∈ {4, 5, 6}.**

**(c) x1, x2 ≠ 5.** The s0/s1 cut sits at t1[x1+u−5]. If x1 = 5, that vertex is t1[u], which already carries c1's F1 cut, so one label would have two cuts. In the same way, the s6/s0 cut sits at t3[5+u−x2], and x2 = 5 would make it t3[u].

## 3. The case d = 4

**The saturated block.** Exchanging s2 with s5 gives:

    Q = L(t2[A..A+3]) = L(t2[A+11..A+14]),   P = t2[A..A+3] = (q1, q2, q3, q4).

**Two Q-labels are pinned.**
- **q1 = L(t2[A]).** Exchanging R_out with s1 makes it a T_int-label. Its cut is the s1/s2 cut t2[A].
- **q_end := L(t2[A+14]).** This lies in {q2, q3}. It is a T_int-label with its cut at the s4/s5 cut.

**Every Q-label other than q_end has a vertex on Λ[1..x2−1].** RC is applied to each candidate type: the T_int-labels q1 and τ01 (the label on the s0/s1 cut), c1, c2, and λ\* = L(Λ[10−p1]). In every case, after P and P′, the label must still cover row s4, and the only admissible vertex there is on Λ[1..x2−1].

By D2Q these three Q-labels force x2 ≥ 7. By (c), x2 ≠ 9.

**x2 = 8 is impossible.** Then x1 = 6. q_end's remaining vertices must cover s0 and s1. Exchanging M1 with s4 puts q_end on t1[u..u+p1−1]. Its t1-vertex must lie strictly inside s1, that is, in t1[u..x1+u−6] = {t1[u]}. But t1[u] carries c1. Contradiction.

**x2 = 7.** Then x1 = 7, λ = 10, p2 = p1 and p1 ∈ [4, 9].
- q_end = L(t1[u+1]).
- c1 and τ01 = L(t1[u+2]) would both be adjacent to q_end on t1, so neither lies in Q.
- Hence Q = {q1, c2, λ\*, q_end}.

Λ[1..6] carries q1, c2 and λ\*. D2Q fixes their placement, and the M1/M2 membership of each type leaves only three configurations:

| p1 | Λ[1] | Λ[3] | Λ[4] | Λ[6] | Special pair |
|---|---|---|---|---|---|
| 6 | c2 | — | λ\* | q1 | λ\* = q4 |
| 4 | q1 or c2 | c2 or q1 | — | λ\* | c2 = q4 |
| 4 | c2 | — | q1 | λ\* | λ\* = q4 |

**OPEN residual of type E (0,2,0,0):**
- the three configurations above (d = 4, x2 = x1 = 7);
- d ∈ {5, 6}.

## 4. Result

**WRITTEN:** the reductions (a)–(c) of §2 and §3 for type E (0,2,0,0). D2Q uses (R3).

**Residual:** as in v137 §4, with type E (0,2,0,0) narrowed as above. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
