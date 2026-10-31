# Original Tuscan-2(11), entire m = 9 distance-two branch, part 92: L1 types 12 and 2 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≤ 15 — three of the four window cases closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-R7-copy-lemma-and-cprime0-b3-in-Q1-reductions-v204.md` (SHA256 `79a93d0974841c512910d7a2418011e498fb7989145a143bac39d8e1d5af40ce`).

It uses:
- Lemma R7C and §2(i) of v204;
- the data of v200 §1 (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`);
- Lemma 2R and Corollary 2R of v160 §2.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The cases

**Setting.** Type 12, r2 = 2, c′ = 0 (so 1 ≤ x ≤ 9), b3 inside Q1 (10 − x < ℓ3 < 20 − x), and ℓ2 ≤ 15. Then:
- Q0 = t1[x..1], b6, t3[1..10−x];
- Q1 = t3[10−x..ℓ3−1], b3, t1[ℓ1−1..x];
- Z0 = L(t1[x]) has b = 1, and its only G2-vertex is t1[x];
- by v204 §2(i), w's G2-W is t3[dw] with dw ≤ 9 − x, so w has no t1-vertex.

**The window cut C′.**
- By Lemma R7C, d′ ∈ {4,5,6}, and the cut inside W′ = [P2+u, P2+u+10] is C′ = 10 + ℓ1 + ℓ2 + d′.
- Since 20 ≤ 10 + ℓ1 + ℓ2 ≤ 10 + (u+9) + 15 ≤ 43, we get C′ ∈ {30, 40}.
- Also P4 = 35 + ℓ1 + ℓ2 = 25 + C′ − d′. So d′ = 5 would put b3 on a cut, and **d′ ∈ {4,6}**.

The four cases are (C′, d′) ∈ {(30,4), (30,6), (40,4), (40,6)}.

## 2. (C′, d′) = (30,4)

**Numbers.** ℓ1 + ℓ2 = 16, ℓ3 = ℓ2 + 4, P3 = 51 − ℓ2 ≤ 46, P4 = 51 and P5 = 55 + ℓ2.

**R5.** R5 = [50,60] consists of:
- t2[ℓ2−1] at 50 (S_23-passage P3 + ℓ2 − 1), so its label is the F1-cut label X50;
- b3 at 51;
- t3[ℓ2+3..ℓ2−4] at 52..59;
- at 60, t3[ℓ2−5] if ℓ2 ≥ 6, or b6 if ℓ2 = 5.

**The exchange with Q1.**
- Since ℓ3 < 20 − x, we have 10 − x ≥ ℓ2 − 5. So Q1's t3-part t3[10−x..ℓ2+3] lies inside R5, and R5 ∩ Q1 = {b3} ∪ t3[10−x..ℓ2+3].
- Hence L(t1[x..ℓ1−1]) = L(R5 ∖ Q1) = {X50} ∪ L(t3-vertices of R5 below index 10 − x) ∪ ({v} if ℓ2 = 5).
- Z0 lies on the left side. On the right it would have to be X50, which is F1-cut while Z0 is F2-cut, or have a t3-vertex, which is impossible since b(Z0) = 1, or be v. **Contradiction.**

## 3. (C′, d′) = (30,6)

**Numbers.** ℓ1 + ℓ2 = 14, ℓ3 = ℓ2 + 6, P4 = 49 and P5 = 55 + ℓ2.

**ℓ2 ≥ 6.** R5 = [50,60] lies inside the t3-run 50..54 + ℓ2, so it is an F1-row of interior t3-vertices. Corollary 2R excludes this.

**ℓ2 = 5.**
- Here ℓ3 = 11, P5 = 60 and R5 = t3[10..1], b6.
- Its vertices form the F2-window [0,10], which carries every label. By Lemma 2R that window must be an F2-row, so x = 0, against c′ = 0.

**Impossible.**

## 4. (C′, d′) = (40,4)

**Numbers.** ℓ1 + ℓ2 = 26, so ℓ1 ≥ 11 and ℓ3 ≤ 9. Also P3 = 61 − ℓ2, P4 = 61 and P5 = 61 + ℓ3 ≤ 70.

**R6.** R6 = [60,70] consists of:
- t2[ℓ2−1] at 60;
- b3 at 61;
- t3[ℓ3−1..1];
- b6 at P5;
- Λ[1..9−ℓ3].

**The exchange with Q0.**
- Since 10 − x ≤ ℓ3 − 1, R6 ∩ Q0 = {b6} ∪ t3[1..10−x].
- Hence L(t1[1..x]) = L(R6 ∖ Q0), and R6 ∖ Q0 contains b3. So w ∈ L(t1[1..x]).
- But w has no t1-vertex. **Contradiction.**

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1 and ℓ2 ≤ 15 is impossible except possibly when (C′, d′) = (40,6). By the mirror (v160 §1), the same holds for type 2.

**What (40,6) requires.**
- ℓ1 + ℓ2 = 24, ℓ3 = ℓ2 − 4, P4 = 59 and P2 + u = 34.
- u ≥ 5: when u = 4, case (a) of Lemma R7C forces C′ = 30. Under case (a), v's P− passage lies in Rb′, so P3 > C′ + 10, which for C′ = 40 needs ℓ1 ≥ 16 > u + 9.
- By (a′), the 4-paths Λ[15−ℓ2..18−ℓ2] and Λ[λ−u+1..λ−u+4] carry one set Q of four S-labels. Lemma KS (v120 §1) then excludes u = 5, since any four consecutive t1-arm vertices would hold at least three Q-labels.

**OPEN (m = 9, L1):**
- Types 2 and 12 with r2 = 2, c′ = 0, b3 inside Q1, in two parts:
  - ℓ2 ≤ 15 with (C′, d′) = (40,6) and u ≥ 6;
  - ℓ2 ≥ 16.
- Types 1 and 11 with r1 ∈ {4,5}.
- Type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
