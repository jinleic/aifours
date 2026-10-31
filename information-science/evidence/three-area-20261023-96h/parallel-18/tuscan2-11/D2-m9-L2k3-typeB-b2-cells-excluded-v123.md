# Original Tuscan-2(11), entire m = 9 distance-two branch, part 12: L2 type B with b = 2 — all four cells excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeA-b4-loop-V-cells-excluded-v122.md` (SHA256 `f180fe11530aca9c61cfc03b0797b6d346e864fe62aa721ef6eea2f5957935c0`). Notation is that of v116 §2 (type B), and Lemma KS is v120 §1.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Type B facts used

**F1.** F1 = S_out S_Λ1 S_12 S_Λ2 S_in has a = 9 rows. Its b5 positions are:
- P1 = 10n1 + 10 + p1;
- P2 = 10(n1 + nΛ) + 25, with offset 5;
- P3 = P2 + ℓ1 + ℓ2, with offset p3;
- P4 = P3 + λ, with offset p4 = p3 + 5 − p1.

Λ is passed twice inside F1:
- forward from P1, with Λ[k] at P1 + k;
- backward from P3, with Λ[k] at P3 + λ − k.

**Λ's pass data.** φΛ ≡ −p1 and ρΛ = p3 + 5.

**Row order.** Every row of F1 holds exactly one v, so the v-passages fall row by row in face order.

**The cells.** With b = 2, v116 §4 leaves the cells (1,1,0,0), (1,0,1,0), (0,1,0,1) and (0,0,1,1).

## 2. Cells with n1 = 1: (1,1,0,0) and (1,0,1,0)

**Parameters.** The t1 arm table (v115 §2) and (K5) leave only p1 = 1. Then:
- λ = 14, ℓ1 = u + 11 and ρ1 = 6;
- P1 = 21 and P2 = 35.

**Row order.** It puts P4 one row after P3, so p3 ≤ 5. Lemma OL on Λ (L = 14, φ = 9) kills p3 = 5. So p3 ∈ {1, 2, 3, 4}.

**DP on t1 (ρ1 = 6).** Exchange row 1 = t1[u..u+10] with row 4 = [40,50]. Row 4 is t1[u+6..u−4], or, when u ≤ 4, the walk through b4 into t2. The exchange gives:

    Q := L(t1[u+7..u+10]) = L(a 4-path),

so Q is saturated.

**The row containing P3.** It is R′ = (t2-part of p3 vertices), b5, Λ[13..4+p3]. Exchange it with row 3 = Λ[9..13], b5, t1[u+10..u+6]. They share b5 and Λ[9..13], so:

    L(t1[u+6..u+10]) = L(t2-part) ⊔ L(Λ[4+p3..8]).

**Counting.** The four Q-labels of t1[u+7..u+10] must be split between two paths:
- the t2-part has p3 vertices;
- Λ[4+p3..8] has 5 − p3 vertices.

Neither path may hold two adjacent Q-labels, and a 4-path may hold at most two Q-labels without contradicting Lemma KS. So:
- **p3 = 1:** the 4-path Λ[5..8] holds at least three Q-labels, which contradicts Lemma KS.
- **p3 = 2:** the 3-path Λ[6..8] holds at least three Q-labels, so two are adjacent.
- **p3 ∈ {3, 4}:** the two paths hold at most 2 + 1 Q-labels, fewer than four.

**Both cells are impossible.**

## 3. Cells with n1 = 0 and nΛ = 1: (0,1,0,1) and (0,0,1,1)

**Parameters.**
- λ = 25 − p1, so L = λ ∈ [16, 24];
- φΛ = 10 − p1 and ρΛ = p3 + 5.

**Lemma OL on Λ.** It leaves:
- p3 = 9 with p1 ≥ 4;
- p3 = 1.

**Row order.** V_Λ's second passage lies in row 5 + n2 and P4 in row 6 + n2, which forces p3 − p1 ∈ (−5, 5). So:
- p3 = 9 needs p1 ∈ {6, 7, 8, 9};
- p3 = 1 needs p1 ∈ {1, 2, 3, 4}.

**F1 rows.**

| Row | Vertices |
|---|---|
| 1 | t1[u..ℓ1−1], b5, Λ[1..10−p1] |
| 2 | Λ[10−p1..20−p1] |
| 3 | Λ[20−p1..24−p1], b5, X (X is the 5-path back along t1 from t1[ℓ1−1]) |
| 5 + n2 | a pure Λ-row of the second pass |

### p3 = 9

**Rows of the second pass.**
- Row 5 + n2 = Λ[24−p1..14−p1].
- Row 6 + n2 = Λ[14−p1..1], b5, (t3-part of p1 − 4 vertices).

**Exchanges.**
- Rows 2 and 5 + n2 give Q := L(Λ[10−p1..13−p1]) = L(Λ[21−p1..24−p1]), saturated.
- Rows 1 and 6 + n2 give L(t1[u..ℓ1−1]) ⊇ L(Λ[11−p1..13−p1]), three Q-labels.

**Contradiction.** Row 3 contains Λ[21−p1..24−p1], so t1[ℓ1−5..ℓ1−1] carries no Q-label. The three Q-labels therefore lie on t1[u..ℓ1−6], which has only p1 − 5 ≤ 4 vertices. They cannot be pairwise non-adjacent there.

### p3 = 1

**Rows of the second pass.**
- Row 4 + n2 = g, b5, Λ[24−p1..16−p1].
- Row 5 + n2 = Λ[16−p1..6−p1].
- Row 6 + n2 = Λ[6−p1..1], b5, (t3-part of p1 + 4 vertices).

**Exchanges.**
- Rows 2 and 5 + n2 give Q := L(Λ[6−p1..9−p1]) = L(Λ[17−p1..20−p1]), saturated.
- Rows 3 and 4 + n2 give L(X) = {L(g)} ⊔ L(Λ[16−p1..19−p1]). So X carries three Q-labels, at its positions 1, 3 and 5. Hence t1[ℓ1−1] ∈ Q, and t1[ℓ1−3] ∈ Q.
- Rows 1 and 6 + n2 give, as a disjoint union:

      L(t3-part) = L(t1[u..ℓ1−1]) ⊔ L(Λ[7−p1..10−p1]).

**Contradiction.** Λ[7−p1..9−p1] supplies three Q-labels, and t1[ℓ1−1] supplies a fourth.
- **p1 ≥ 3:** t1[ℓ1−3] also lies in t1[u..ℓ1−1]. That makes five distinct Q-labels, but |Q| = 4.
- **p1 ≤ 2:** the t3-part has at most 6 vertices, yet must hold four pairwise non-adjacent Q-labels.

**Both cells are impossible.**

## 4. Result

**WRITTEN, (R1)–(R2) only:** L2 type B with b = 2 is impossible. All four of its cells are excluded.

**Type B residual:** the b = 3 cells (0,2,0,0) and (0,1,1,0), with λ = 15 − p1.

**Type A residual (v122):** (0,2,0,0) and (0,1,1,0).

Types C and E, and L1 types 1–4 and 7–12, are as in v119 §4. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
