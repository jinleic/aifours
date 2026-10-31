# Original Tuscan-2(11), entire m = 9 distance-two branch, part 95: L1 types 12 and 2 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≥ 16 — the ranges P2 ≤ 30 and P2 ≥ 41 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime0-b3-in-Q1-C40-d6-closed-l2-le-15-closed-v207.md` (SHA256 `51e2cbaa4195aa9d4b76c98041cdc28397fe9dc759085abf82aebb47337bd04c`).

It uses:
- v200 §1, the data (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`);
- v204 §2(i): w's G2-W is t3[dw] with dw ≤ 9 − x;
- Lemma DP★ (v165 §1, SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- the window argument (grid): an all-label F1-window that is not a row has one inner cut, and both pieces have size in {4,5,6}. Size 1 puts an end label on a second cut, and sizes 2 and 3 contradict (E).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Setting

Type 12, r2 = 2, c′ = 0, 10 − x < ℓ3 < 20 − x and ℓ2 ≥ 16. Then:
- P1 = 10 − u + ℓ1 ∈ [11,19];
- P2 = P1 + ℓ2 ∈ [27,43];
- λ = 25 + u − ℓ2 ∈ [u+1, u+9];
- P3 = P2 + λ = 35 + ℓ1, and P4 = P3 + ℓ2;
- P5 = 55 + ℓ2 ∈ [71,79];
- b6 also sits at 10 − u (R0) and at 80 + u (R8).

**v has no Λ-vertex.** Every Λ P+-passage lies in R7 (P5+1..79), at 80 (c8) or in R8, and b6 already occupies R7 (at P5) and R8. So v = {b6, t2[jv], G2-V}.

## 2. P2 ≥ 41: DP★

**Two pure rows.** R2 = [20,30] and R3 = [30,40] lie inside the S_12-run (P1, P2). They are consecutive pure t2-rows θ[s..s+10] and θ[s+10..s+20] with θ = t2, s = P2 − 40 ≥ 1 and s + 20 = P2 − 20 ≤ ℓ2 − 1 (because P1 ≤ 19).

**The other pass.** t2's other pass, S_23, runs in the opposite direction, with t2[i] at P3 + i.

**Disjointness.** Every backward row used in the proof of DP★ lies at positions in [P3+s−4, P3+s+26]. Since P3 ≥ 46, all these positions are ≥ P3 − 3 ≥ 43. So these rows meet neither R2 nor R3, and DP★ applies. **Impossible.**

## 3. P2 ≤ 30 (so P2 ∈ [27,30], ℓ2 ≤ 19, ℓ1 ≤ u + 4 and P3 ∈ [36+u, 39+u])

**v's rows.**
- R2 contains b6 at P2, or the cut 30 when P2 = 30. So S_12(jv) lies in R1 (the cut 20 would double R2), and therefore v's G2-V is a t3-vertex.
- v must still meet R3. Its only possible passages there are b6 at P2 = 30 or b6 at P3 = 40 (as its cut): the t2 S_23-passage and the t3-vertex lie beyond P3 ≥ 40.
- Hence **either P2 = 30 or P3 = 40**.

**(α1) P2 = 30 (v's cut).**
- **R2.** R2 = t2[10..1], b6.
- **w's G1-W's.** w is in R0, R8 (ℓ) and R1 (P1). R2 forces a t2-W with S_12 ∈ R2. R3 = b6, Λ[λ−1..λ−10] (its first u Λ-vertices carry S-labels) forces a non-arm Λ-W with P− ∈ R3, whose P+ lies in [71+u, 79] ⊂ R7.
- **w's other rows.** So w's t3[dw] lies in R6, and P4 and the S_23-passage of the t2-W fill R4 and R5. Since P4 = P3 + ℓ2 = 55 + u ≥ 59, P4 must be in R5, so u = 4, P4 = 59 and P3 = 59 − ℓ2 ∈ [41,43]. (P3 = 40 would be a second cut of v.)
- **The window.** The vertices of R2 recur in S_23 as the all-label window [P3, P3+10] = b6, t2[1..10]. It contains the cut 50, with a piece of size P3 − 40 ∈ {1,2,3} above it. **Impossible by the window argument.**

**(α2) P3 = 40 (v's cut).**
- **The numbers.** ℓ1 = 5, so u = 4, P1 = 11, ℓ2 = P2 − 11 ∈ [16,18] and λ = 40 − P2 ≥ 11.
- **R3.** R3 = Λ[10..1], b6.
- **The window.** These vertices recur along P+ as the all-label window [P5, P5+10] = b6, Λ[1..10] with P5 = 55 + ℓ2 ∈ [71,73]. It contains the cut 80, with a piece (80, P5+10] of size P5 − 70 ∈ {1,2,3} above it. **Impossible by the window argument.**

## 4. Result

**WRITTEN:** L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1 and ℓ2 ≥ 16 is impossible when P2 ≥ 41 (by DP★) and when P2 ≤ 30 (by the window argument). By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≥ 16 and 31 ≤ P2 ≤ 40;
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
