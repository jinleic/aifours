# Original Tuscan-2(11), entire m = 9 distance-two branch, part 21: type C (0,1,0,1) — loop-shift screen and one sub-case excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-0101-reduced-v132.md` (SHA256 `d1f51603a7728e7efca3be8e171cfd390511b7ea6294ce78ebab110b9616df1c`). Notation is that of v129 §1 (type C), and D2Q is v125 §1, which uses R3.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Cell parameters.** Cell (0,1,0,1) has n2 = nΛ = 1, so a = 3 and b = 8. Then:
- ℓ1 = p1 + u and ℓ3 = 10 − p1 + u;
- λ = 15 + x0 + p1 − x1;
- ℓ2 = 20 + x1 − x0 − p1 − u.

**The v-order.** The F2 v-order is K3, V2, K2, VΛ, K1, V2, K5, VΛ. Hence:
- x1 + λ ∈ [21, 29], that is, x0 + p1 ∈ [6, 14];
- x2 = x0 + p1 − 5;
- x3 ≡ x1 + 5 − p1;
- x3 + λ ∈ [21, 29].

**Cuts on Λ.** Both passes of Λ lie in F2:
- S_Λ2 has cuts at α′ = 10 − x3 and α′ + 10;
- S_Λ1 has cuts at β′ = x2 and β′ + 10.

Their middle rows are the pure Λ-rows Λ[α′..α′+10] and Λ[β′..β′+10]. Put δ′ = β′ − α′ = x0 + x1 − 10. Then ρΛ ≡ x0 + x1.

**Lemma OL on Λ** (L = λ, φ ≡ −x1). Since x0 + p1 ≥ 6, it leaves:
- ρΛ = 4, needing x1 ≥ 4;
- ρΛ = 5, needing x1 ≥ 5 and x0 + p1 ≤ 10;
- ρΛ = 6, needing x0 + p1 ≤ 11.

## 2. Shift screen

| δ′ | Condition | Outcome |
|---|---|---|
| −5 | x1 ≥ 5 | x0 = 5 − x1 ≤ 0: impossible |
| −6 | x1 ≥ 4 | x0 = 4 − x1 ≤ 0: impossible |
| −4 | x0 + x1 = 6 | possible |
| 4 | x0 + x1 = 14, x1 ≥ 5 | possible |
| 5 | x0 + x1 = 15, x0 + p1 ≤ 10, so p1 ≤ 4 | possible |
| 6 | x0 + x1 = 16, x0 + p1 ≤ 11, so p1 ≤ 4 | possible |

## 3. δ′ = −4: reductions, and x0 = 2 excluded

**The saturated block.** Exchanging the two pure Λ-rows gives:

    Q = L(Λ[β′..β′+3]) = L(Λ[β′+11..β′+14]),

with q_last := L(Λ[β′+14]) = L(Λ[α′+10]). The vertex Λ[α′+10] is an F2 cut, so q_last has its cut there.

**End-row exchanges.**
- **s_K1 with s_K5:** the t2-tail, which has 10 − β′ vertices, carries three Q-labels. By D2Q, β′ ≤ 4, so x0 + p1 ≤ 9.
- **s_K2 with s_K3:** the t1-part of s_K3, which has 10 − x0 vertices, carries the first three labels of P′. By D2Q, x0 ≤ 4.

**Exchanges with M = t1[u..ℓ1−1], b5, t3[u..ℓ3−1].**
- **M with s_K3:** L(t3[u..ℓ3−1]) ∋ q_last.
- **M with s_K5**, for x0 ≥ 2: Q ⊆ L(t1[u..ℓ1−1]) ∪ L(t3[u..ℓ3−x3−1]). The last piece has x0 − 1 vertices.

**x0 = 2 is impossible.** Here the t3-piece is the single vertex t3[u]. q_last cannot lie on t1, because s_K3 contains both Λ[α′+10] and t1[u..ℓ1−1]. So q_last = L(t3[u]) = c2. But c2 already has its cut at t3[u], in F1, while q_last has its cut at Λ[α′+10], in F2. A label has only one cut. Contradiction.

**What remains of δ′ = −4:** x0 ∈ {1, 3, 4}. These sub-cases are OPEN.

## 4. Result

**WRITTEN:**
- type C (0,1,0,1) has δ′ ∈ {−4, 4, 5, 6} (§2);
- δ′ = −4 is reduced to x0 ∈ {1, 3, 4}, using (R3) through D2Q (§3).

**OPEN in this cell:**
- δ′ = −4 with x0 ∈ {1, 3, 4};
- δ′ ∈ {4, 5, 6}.

Every other residual item (v131 §3, v132 §4) is unchanged. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
