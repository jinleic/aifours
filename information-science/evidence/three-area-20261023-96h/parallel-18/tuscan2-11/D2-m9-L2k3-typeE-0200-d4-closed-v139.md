# Original Tuscan-2(11), entire m = 9 distance-two branch, part 27: type E (0,2,0,0) with d = 4 closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-0200-reductions-v138.md` (SHA256 `5e38a4e0493efd71ecbaa865b52fd39f2395b5f7229f6d5d25a6ec125bc076bb`), whose notation it uses. RC is v134 §1; D2Q (v125 §1) and R3-pair (v130 §1) use R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up (d = 4, x1 = x2 = 7)

**Parameters.**
- A = 8 − u, so u ≤ 6, and B = 12 − u.
- λ = 10, p2 = p1, ℓ1 = p1 + u and ℓ3 = 10 − p1 + u.

**F2 rows** (mod 70).

| Row | Vertices |
|---|---|
| s0 | T3 = t3[u−2..ℓ3−1], K3, T1 = t1[ℓ1−1..u+2] |
| s1 | t1[u+2..1], b4, t2[1..8−u] |
| s2 | t2[8−u..18−u] |
| s3 | t2[18−u..24−u], K2, Λ[9..7] |
| s4 | Λ[7..1], K1, t2[24−u..22−u] |
| s5 | t2[22−u..12−u] |
| s6 | t2[12−u..1], b4, t3[1..u−2] |

**F1 rows.**
- M1 = t1[u..u+p1−1], b5, Λ[1..10−p1].
- M2 = Λ[10−p1..9], b5, t3[ℓ3−1..u].

**The block and its labels.** The two Q-paths are P = t2[8−u..11−u] and P′ = t2[19−u..22−u]. Their interiors are not on cuts, because the t2 cuts are at 8−u, 18−u, 22−u and 12−u.

From v138:
- Q = {q1, c2, λ\*, q_end};
- q_end = L(t1[u+1]) = L(t2[22−u]);
- by the exchange M2/s3, every Q-label on Λ[1..9−p1] also lies on t3[u..ℓ3−1].

## 2. The three configurations are impossible

**Configuration I** (p1 = 6; Λ[1] = c2, Λ[4] = λ\* = q4, Λ[6] = q1).

λ\* is an S-label cut in F1, so by RC it has one passage in each F2-row. Five rows are already taken:

| Vertex of λ\* | F2 row |
|---|---|
| Λ[4] | s4 |
| t1-arm vertex | s1 |
| P-vertex t2[11−u] | s2 and s6 |
| P′-vertex | s3 and s5 |

So its t3-arm vertex must cover s0. It must also avoid the s6/s0 cut t3[u−2], because that cut lies in s6, which is already taken. Hence the t3-arm vertex is t3[u−1]. But t3[u−1] is adjacent to t3[u] = c2 ∈ Q, which contradicts (E).

**Configuration II** (p1 = 4; {Λ[1], Λ[3]} = {q1, c2}, c2 = q4, Λ[6] = λ\*).

- t3[u..u+5] carries c2 (at t3[u]), q1 and q_end. By D2Q the only admissible special pair here is {q1, c2}, which forces t3[u+2] = q1 and t3[u+5] = q_end.
- So {q1, c2} is realised at t3[u+1]. It is also realised at Λ[2], where Λ[1] and Λ[3] carry q1 and c2.
- Both middles are non-cut 2-vertices: the Λ cuts are at 6 and 7, and the t3 cuts are at u and u−2.

R3-pair gives a contradiction.

**Configuration III** (p1 = 4; Λ[1] = c2 = q_o, Λ[4] = q1, Λ[6] = λ\* = q4).

1. Exchanging M1 with s0 gives L(t3[u−2..u+5]) = {c1, q_end} ⊔ L(Λ[1..6]), so λ\* ∈ L(t3[u−2..u+5]). By D2Q on t3[u..u+5], t3[u+2] = q_end and t3[u+5] = q1. The five vertices of λ\* are Λ[6], one t1-arm vertex, one t3-arm vertex, a P-vertex and a P′-vertex, so its only t3-vertex is the arm vertex. Hence λ\* lies on t3[u−2..u−1].
2. λ\* cannot sit at t3[u−1], because it would be adjacent to c2.
3. At t3[u−2], λ\* would lie at distance 2 from c2, across t3[u−1], which is interior in R_in. The pair {q4, q_o} is not special, so D2Q forbids this.

Contradiction.

## 3. Result

**WRITTEN, uses (R3):** type E (0,2,0,0) with d = 4 is impossible. By the mirror (v138 §2(a)), so is d = −4.

**OPEN residual of type E (0,2,0,0):** d ∈ {5, 6}, with x1 + x2 = 10 + d and x1, x2 ≠ 5.

Every other residual item is as in v138. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
