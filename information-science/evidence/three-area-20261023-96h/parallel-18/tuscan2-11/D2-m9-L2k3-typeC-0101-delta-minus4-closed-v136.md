# Original Tuscan-2(11), entire m = 9 distance-two branch, part 24: type C (0,1,0,1) with loop shift δ′ = −4 closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-1100-closed-RC-v135.md` (SHA256 `900fccab4153f7df50b33ef0e4dfb03653f5b3a5b347d045720276118f928379`) and completes the δ′ = −4 part of v133 §3, whose notation it uses. RC is v134 §1; D2Q (v125 §1) and R3-pair (v130 §1) use R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up (δ′ = −4)

**Parameters.**
- x0 + x1 = 6;
- β′ = x2 = x0 + p1 − 5 ∈ [1, 4];
- α′ = β′ + 4;
- x3 = 11 − x0 − p1.

**The saturated block and its rows.**
- Q = L(Λ[β′..β′+3]) = L(Λ[β′+11..β′+14]).
- P′ = Λ[β′+11..β′+14] lies in s2 through its S_Λ1-passage. This holds because λ − 1 = β′ + 19 − x1 ≥ β′ + 14.
- By RC, no Q-label has a further vertex in s2.

**Remaining values.** v133 §3 and v134 §3 leave x0 ∈ {3, 4}. Two exchanges from v133 are used again:
- **s_K1 with s_K5:** the t2-tail of s4, t2[ℓ2−10+β′..ℓ2−1], carries {q2, q3, q4}.
- **M with s_K5** (x0 ≥ 2): Q ⊆ L(t1[u..ℓ1−1]) ∪ L(t3[u..u+x0−2]).

## 2. Lemma T2W (the tail window)

The tail vertices t2[ℓ2−x1..ℓ2−1] make their forward passage in s2, or at the s1/s2 cut, which also lies in s2. So {q2, q3, q4} lies on the window t2[ℓ2−10+β′..ℓ2−x1−1], which has 9 − p1 vertices.
- By D2Q, p1 ≤ 3.
- (E) alone gives p1 ≤ 4.

## 3. x0 = 3 is impossible

Here x0 + p1 ∈ [6, 9] gives p1 ≥ 3, and Lemma T2W gives p1 ≤ 3.

**Placing Q.** By v133 §3, q_last lies on t3[u..u+1]. Since t3[u] = c2, which has a different cut, q_last = L(t3[u+1]). Then:
- c2 ∉ Q, since otherwise it would be adjacent to q_last;
- the other three Q-labels lie on t1[u..u+p1−1].

**Contradiction.** D2Q needs p1 ≥ 6 for three Q-labels on t1[u..u+p1−1]. This contradicts p1 = 3.

## 4. x0 = 4 is impossible

Here p1 ∈ [2, 5], and Lemma T2W gives p1 ≤ 3.

**Placing Q.**
- t1[u..u+p1−1] carries at most two Q-labels, and t3[u..u+2] at most two.
- So p1 = 3, and both pieces carry exactly two, at distance 2.
- On t3 these are c2 = L(t3[u]) and q_last = L(t3[u+2]).
- On t1 they are c1 = L(t1[u]) and q1 = L(t1[u+2]). Here q1 is forced, because its cut lies on Λ, while c1 and c2 are cut in F1.

**Special pairs.** By D2Q, {c2, q_last} is special. Since q_last ∈ {q2, q3}, it is {q2, q3}. This pair is realised at t3[u+1], a non-cut 2-vertex (the t3 cuts are at u and u+3).

**The t2 window.** Here x1 = 2 and β′ = 2. The window t2[7−u..12−u] carries {q2, q3, q4} = {c1, c2, q_last}. By D2Q it realises its special pair {q2, q3} = {c2, q_last} at a middle in t2[8−u..11−u]. That middle is not on a cut, since the t2 cuts are at 13−u and 7−u.

R3-pair gives a contradiction.

## 5. Result

**WRITTEN, uses (R3):** type C (0,1,0,1) with δ′ = −4 is impossible.

**Residual of type C (0,1,0,1):** δ′ ∈ {4, 5, 6}. Every other residual item is as in v135 §4. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
