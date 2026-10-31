# Original Tuscan-2(11), entire m = 9 distance-two branch, part 53: L1 type 9 with r2 = 4 is reduced to λ ∈ {12, 13, 14} with ℓ2 ≥ 5, or λ ∈ {21, …, 24} with λ ≤ 20 + u (type 3 by the mirror)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-DPstar-lemma-types12-2-r2eq2-short-thread-closed-v165.md` (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`). It uses:
- the type-9 table of v156 §1;
- the v152 anatomy;
- Lemma DP★ of v165;
- the mirror principle of v155 §5.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data for type 9 with r2 = 4

**Dimensions.** r1 = 7, F1 has 70 positions, t + ℓ1 = 15 (so ℓ1 = u + 5), and ℓ2 + ℓ3 + λ = 40.

**F1 positions.**
- t1[j] lies at 10 − u + j (S_12, positions 11 − u..14) and at C2 − j (S_31).
- b3 lies at 15 and at B2 = 55 − λ.
- b6 lies at C1 = 15 + ℓ2, C2 = 60 + u − λ and C3 = 60 + u.
- t2 runs over [16, 14 + ℓ2], t3 over [16 + ℓ2, 54 − λ], and Λ over [61 + u − λ, 59 + u] (P+).
- c1 = L(t1[u]) is cut at 10, and c5 = L(Λ[λ−u]) at 60.

**Anatomy (v152, G3 = ∅).** An F1-cut label has a = 1 and b = 4. An F2-cut label has a = 2 and b = 3. Here G1 = {T, t1}.

**v (v152).**
- **(A)** c = 1, n1 = 0, and two G2-V's;
- **(B)** c′ = 1, n1 = 1, and one G2-V.

## 2. Structure of R1 = [10, 20]

R1 consists of t1[u] (c1), t1[u+1..u+4] (positions 11–14), b3 (15), and five vertices at positions 16–20.

**Who sits on t1[u+1..u+4].**
- Every F1-cut label other than c1 and w has its single G1-vertex equal to T (a T_int-label) or to its t1-arm vertex (an S-label, index ≤ u). So it cannot sit on t1[u+1..u+4].
- In case (A), v has no t1-V.
- Hence the four vertices t1[u+1..u+4] carry exactly the four F2-cut labels (in case (B), v is one of them).

**Who sits on positions 16–20.** The five remaining labels: Q5 := {c5, X20, X30, X40, X50}, where Xp is the label cut at p.

## 3. The constraints on λ

**(a) λ ≥ 12.**
- c5's single G1-vertex is a t1-arm vertex t1[j5] with j5 ≤ u − 1.
- Its S_31-passage at 60 + u − λ − j5 must avoid R5 ∪ R6 = [50, 70], which c5's cut at 60 covers, and must avoid the cut at 50.
- So 60 + u − λ − j5 ≤ 49, i.e. λ ≥ 11 + u − j5 ≥ 12.

**(b) λ mod 10 ∈ {1, 2, 3, 4}.**
- The run [55 − λ, 60 − λ] is b3, t1[u+4..u+1], t1[u].
- It contains no F1-cut: w's cut is ℓ, the labels on t1[u+1..u+4] are F2-cut (§2), and c1's cut is at 10.
- So no multiple of 10 lies in it, i.e. (55 − λ) mod 10 ∈ [1, 4].

**(c) λ ≤ 20 + u.** Suppose λ ≥ 21 + u. Then R4 = [40, 50] and R5 = [50, 60] lie inside the P+-run:
- R4 = Λ[λ−u−20..λ−u−10] and R5 = Λ[λ−u−10..λ−u];
- these are consecutive pure Λ-rows with s = λ − u − 20 ≥ 1 and s + 20 = λ − u ≤ λ − 1;
- Λ's other pass is P− in F2 (F′ ≠ F).

Lemma DP★ then excludes the configuration.

**(d) If λ ≤ 14, then ℓ2 ≥ 5.** Suppose ℓ2 ≤ 4. Then R2 = [20, 30] and R3 = [30, 40] lie inside the t3-run (16 + ℓ2 ≤ 20 and 54 − λ ≥ 40):
- R2 = t3[5−ℓ2..15−ℓ2] and R3 = t3[15−ℓ2..25−ℓ2];
- s = 5 − ℓ2 ≥ 1 and s + 20 = 25 − ℓ2 ≤ ℓ3 − 1 = 39 − λ − ℓ2;
- t3's other pass is S_23 in F2.

Lemma DP★ excludes the configuration.

**(e) λ = 12 with ℓ2 ∈ {26, 27}, and λ = 13 with ℓ2 = 26.** Here R2 and R3 lie inside the t2-run [16, 14 + ℓ2]. They are pure t2-rows with s = ℓ2 − 25 ≥ 1 and s + 20 = ℓ2 − 5 ≤ ℓ2 − 1, and t2's other pass is in F2. Lemma DP★ excludes these as well.

## 4. Result

**WRITTEN:** L1 type 9 with r2 = 4 survives only with:
- λ ∈ {12, 13, 14}, ℓ2 ≥ 5 (and not the cases of (e)); or
- λ ∈ {21, 22, 23, 24} with λ ≤ 20 + u.

In both cases L(positions 16–20) = Q5 and L(t1[u+1..u+4]) is the set of F2-cut labels. By the mirror (v156 §3), the same holds for type 3 with r2 = 4.

**OPEN (m = 9, L1):**
- types 3 and 9 with r2 = 4 (above), and with r2 = 3 (λ = 14, u ≥ 4);
- type 7 with r2 ∈ {3, 4};
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
