# Original Tuscan-2(11), entire m = 9 distance-two branch, part 17: ARM-C+ (u = 8), and type E (1,0,1,0), E (1,0,0,1) ≅ (0,0,1,1) and type C (1,0,1,0) excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-ARMC-lemma-typeE-1100-closed-v127.md` (SHA256 `c9d8952ee4f9d636d39c929cf63f81407c05bbaa97b11dde15c6f694fadd8027`). Notation is that of v116 §2, the arm table is v115 §2, and D2Q and ARM-C are v125 §1 and v127 §2 (both use R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. ARM-C+ : under the hypotheses of ARM-C, u = 8

**Hypotheses.** Assume those of ARM-C with u ≥ 5. In addition, assume that the backward pass of t1 continues at b4 into t2, as it does in types C and E. The backward cuts of t1 then sit at u + 6 and u − 4, so the row after s1 is:

    s2 = t1[u−4..1], b4, Y,   with |Y| = 14 − u and Y vertex-disjoint from t1.

**Exchange.** R_out and s2 have the common part {b4} ∪ t1[1..u−4]. Exchanging them gives:

    L(Y) = {v} ∪ T_int ∪ L(t1[u−3..u]) ⊇ Q ∖ {L(t1[u−4])}.

**Conclusion.** Y carries three Q-labels, so by D2Q, 14 − u ≥ 6, that is, u ≤ 8. With ARM-C this gives u = 8.

The mirror statement holds for t3 with ρ3 = 4.

## 2. Type E, cell (1,0,1,0) (self-mirror)

**Parameters.** ℓ2 = 5 − u, so u ≤ 4.

**Ruling out x1 = 1.** For n1 = 1, the arm table gives x1 ∈ {9, 1}. The value x1 = 1 has ρ1 = 6, so ARM-C would force u ≥ 8. Hence x1 = 9.

**Ruling out ρ3 = 4.** For n3 = 1, the arm table gives ρ3 ∈ {4, 5, 6}. The value ρ3 = 4 would force u ≥ 8 by the mirror of ARM-C. So ρ3 = x1 + 5 − p1 + p2 ∈ {5, 6}, that is, p2 − p1 ≡ 1 or 2 (mod 10).

**Contradiction.** The F2 v-order is K3, V1, K2, K1, V3. There is no V on Λ, so K2 and K1 lie in consecutive rows. This means x1 + λ ∈ [11, 19], so λ ≤ 10 and p2 ≤ p1.

The only pair with p2 − p1 ≡ 1 or 2 and p2 ≤ p1 is (p1, p2) = (9, 1). That gives λ = 2, a double edge b5–Λ[1]–b5, which contradicts (E).

**Cell (1,0,1,0) is impossible.**

## 3. Type E, cell (1,0,0,1), and by the mirror (0,0,1,1)

**Parameters.**
- ℓ2 = 5 − u, so u ≤ 4. As in §2, ARM-C forces x1 = 9, so x0 = 14 − p1 and p1 ≥ 5.
- Lemma OL on Λ, with λ = 20 + p2 − p1 and ρΛ = p2 − 1, leaves only p2 = 5.

**Rows.**

| Face | Row | Vertices |
|---|---|---|
| F1 | r1 | t1[u..u+10] |
| F1 | r2 | t1[u+10..u+9+p1], b5, Λ[1..10−p1] |
| F2 | s1 | t1[u+14..u+4] |
| F2 | s2 | t1[u+4..1], b4, t2[1..4−u], K2, Λ[λ−1] |
| F2 | s4 | Λ[14−p1..1], K1, (p1 − 4 vertices along t2, b4, t3[1..]) |

**Exchanges.**
- r1 with s1 gives Q′ := L(t1[u..u+3]) = L(t1[u+11..u+14]), saturated.
- r2 with s4 gives L(t1[u+10..u+9+p1]) = L(Λ[11−p1..14−p1]) ⊔ L(post-K1), and the left side contains Q′.

**Where Q′ can sit in post-K1.** Row s2 contains t1[1..u+3], t2[1..4−u] and b4, so:
- Q′ ∩ S = {c1};
- t2 carries no Q′-label;
- w ∉ Q′.

The t3-part of post-K1 lies in t3[1..u], so it carries only S-labels, and of Q′ at most c1.

**Contradiction.** Q′ ∖ {c1} therefore consists of three labels on the four consecutive vertices Λ[11−p1..14−p1]. Two of them are adjacent, which contradicts (E).

**The cells (1,0,0,1) and (0,0,1,1) are impossible.**

## 4. Type C, cell (1,0,1,0) (self-mirror)

**Parameters.** a = 5 and b = 6. The F2 v-order is K3, V1, K2, K1, V3, K5, so K2/K1 and K5/K3 lie in consecutive rows. Also:
- ℓ2 = 10 + x1 − x0 − p1 − u ≥ 1;
- λ = 5 + x0 + p1 − x1;
- ρ1 = p1 + x0, which lies in {4, 5, 6} (mod 10) by the arm table;
- ρ3 = x1 + 5 ∈ {4, 6}, so x1 ∈ {9, 1}.

**x1 = 9.** Here ρ3 = 4, so u ≥ 8 by the mirror of ARM-C. But λ = x0 + p1 − 4 ≥ 3 forces x0 + p1 ∈ {14, 15, 16}, and then ℓ2 = 19 − (x0 + p1) − u ≥ 1 forces u ≤ 4. Contradiction.

**x1 = 1.** Consecutive K2/K1 needs λ ≥ 10, so x0 + p1 ≥ 6. And ℓ2 ≥ 1 needs x0 + p1 ≤ 10 − u ≤ 8. The arm table then leaves x0 + p1 = 6, so ρ1 = 6, and ARM-C gives u ≥ 8. That contradicts x0 + p1 ≤ 10 − u.

**Cell (1,0,1,0) is impossible.**

## 5. Result

**WRITTEN, uses (R3) through ARM-C and D2Q:**
- ARM-C+ (§1);
- type E (1,0,1,0) is impossible;
- type E (1,0,0,1) and (0,0,1,1) are impossible;
- type C (1,0,1,0) is impossible.

**Residual:**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0), (0,1,0,1), (1,1,0,0) ≅ (0,1,1,0), (1,0,0,1) ≅ (0,0,1,1) |
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
