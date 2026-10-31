# Original Tuscan-2(11), entire m = 9 distance-two branch, part 37: type A (0,2,0,0) — the R2-slot lemma, and δ = 5 closed, so type A (0,2,0,0) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeA-0200-setup-rules-delta-closures-v148.md` (SHA256 `b49584adf1f302e0d3918195518f6a9e2cff3f579d867c15f32af6cbfe9c0687`), whose notation and Rules A1–A2 it uses. DP-2 is v114 §2.

This uses (E), (C), (X) and RC only. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The R2-slot lemma

**Lemma S.** In type A (0,2,0,0), if u + p2 ≥ 6, then y1 ≤ 4.

**Proof.**
1. Take α (cut R3/R4), β (cut R4/R5) and c2 (cut R5/R6). None of these cuts covers R2, so each must cover R2 by a non-cut vertex.
2. **Allowed vertices.** By Rule A1, the single group-1 vertex of each is T or a t1-arm vertex. T has no R2-passage. A t1-arm vertex t1[j] has its S_12-passage in R2 exactly when u + p2 − 4 ≤ j ≤ u − 1. R2's group-2 vertices are Λ[6..4+p2], and an F1-cut label avoids F2 cuts.
3. **If w is one of the three.** As an F1-cut label, w consists of b4 and three group-2 W's. b4's F1-corners lie in R0, R3 and R6 when u + p2 ≥ 6, so w also needs a group-2 W in Λ[6..4+p2].
4. **Count.** The three labels need three distinct "slots" from t1[u+p2−4..u−1] ∪ (Λ[6..4+p2] ∖ {Λ[y1]}). These sets have 4 − p2 and p2 − 1 vertices, and Λ[y1] is the q0/q1 cut.
5. Since y0 ≤ 9, y1 = y0 + p2 − 5 ≤ 4 + p2. So if y1 ≥ 6, then Λ[y1] lies in Λ[6..4+p2], and only two slots remain. Contradiction. Also y1 ≠ 5. ∎

**Consequence.** If u + p2 ≥ 6, then δ = p3 + y1 − 10 ≤ 9 + 4 − 10 = 3, so every δ > 0 is impossible. This independently re-proves v148 §4 (δ = 4) and v148 §3 (δ = 6) in that range.

## 2. δ = 5 is impossible

Recall G2 = A + 5 and H2 = A + 15. Exchanging R4 with q2 gives the 5-block L(t2[A..A+4]) = L(t2[A+11..A+15]).

**A ≥ 5: DP-2.**
- Exchange R3 with q3. For A ≥ 6, q3 = t2[A+5..A−5] is pure, and the rows share t2[A−5..A]. For A = 5, q3 = t2[10..1], b4, and they share b4 and t2[1..5].
- Either way, L(t2[A+1..A+5]) = L(P1), where P1 is the first five vertices of R3. That is t1[u+p2−5..1], b4, t2[1..A−6] when u + p2 ≥ 6, and a path through b4 or along t2 otherwise; it is t1[5..1] when A = 5.
- With P1′ = t2[A+1..A+5], P2 = t2[A..A+4] = (t2[A], P1′ minus its last vertex) and P2′ = t2[A+11..A+15], the four paths are pairwise disjoint as needed. DP-2 with m = 5 gives a contradiction.

**A ≤ 4.** Then u + p2 = 15 − A ≥ 11, so Lemma S gives y1 ≤ 4. But δ = 5 means y1 = 15 − p3 ≥ 6. Contradiction.

## 3. Result

**WRITTEN:**
- Lemma S.
- Type A (0,2,0,0) with δ = 5 is impossible.

With v148 (δ ∈ {4, 6, −4, −5, −6}) and the shift screen δ ∈ {±4, ±5, ±6}, **type A (0,2,0,0) is closed.**

**OPEN residual of L2 (k = 3):** type A (0,1,1,0) only.

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
