# Original Tuscan-2(11), entire m = 9 distance-two branch, part 60: L1 type 7 with r2 = 4 — Lemma T7′; the cases nΛ = 2 (c′ = 0) and nΛ = 1 (c′ = 1) are impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq3-lemmaT7-cprime1-and-VonLambda-closed-v172.md` (SHA256 `6bca223beb5517ee4350ed85fde5422c9284520df01c1aeef85701607b67c802`). It uses:
- the type-7 data of v157 §1;
- the v152 anatomy;
- Lemma DP★ of v165;
- the consecutive-rows property and OL, as in v172.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 7 with r2 = 4: data

**Lengths.** r1 = 7, so F1 has 70 positions and F2 has 40. Then ℓ2 = u + 5 and ℓ1 + λ + ℓ3 = 40.

**F1 positions.**
- t1[j] lies at 10 − u + j, and b3 at P1 = 10 − u + ℓ1.
- t2[j] lies at P2 − j, with b6 at P2 = 15 + ℓ1.
- Λ[k] lies at P3 − k, with b6 at P3 = 55 − ℓ3.
- t2[j] lies at P3 + j, with b3 at P4 = 60 + u − ℓ3.
- t3[j] lies at 60 + u − j, with b6 at P5 = 60 + u.
- T_int lies at 61 + u..69 and ℓ at 70.

**F2 offsets.** b6 at 0 and at λ; Λ[k] at k; t3[j] at λ + j; b3 at λ + ℓ3; t1[j] at 40 − j.

**Rows and labels.**
- R0 = ℓ, T_int, b6, t1[1..u] and R6 = t3[u..1], b6, T_int, ℓ, so S = L(t1[1..u]) = L(t3[1..u]).
- c1 = L(t1[u]) is cut at 10 and c5 = L(t3[u]) at 60.
- c1 ≠ c5, so u ≥ 2. (This holds for type 7 with any r2.)

**v (v152).** n1 + n2 + n3 + nΛ = 2 and n1 + n3 + nΛ + c′ = 2.

## 2. Lemma T7′

**Lemma T7′.** If L(t1[u+1..ℓ1−1]) and L(t3[u+1..ℓ3−1]) are contained in {w} ∪ T_int, and every Λ-vertex lying in R1 or R5 also carries a label from {w} ∪ T_int, the configuration is impossible.

*Proof.*
- **P1 ∈ [11, 19].** If P1 ≥ 21, then R1 = t1[u..u+10] carries labels from {c1, w} ∪ T_int only, at most 11 − u < 11 of them. P1 = 20 puts b3 on a cut.
- **P4 ∈ [51, 59].** The same argument applies to R5.
- **Shapes of R1 and R5.**
  - R1 consists of t1[u..ℓ1−1], b3, and a t2-part that ends at t2[u+4] (next to b3), possibly followed by b6 = P2 and Λ-vertices.
  - R5 consists of possibly some Λ-vertices and b6 = P3, then a t2-part that ends at t2[u+4], then b3 and t3[ℓ3−1..u].
  - The two t2-parts are terminal segments t2[a..u+4] and t2[a′..u+4], so one contains the other.
- **R1's t2-part inside R5's.**
  - Then R1 ∖ R5 consists of t1[u..ℓ1−1] and possibly b6 and Λ-vertices, all with labels in {c1, w, v} ∪ T_int.
  - OL against t3[u] ∈ R5 ∖ R1 then gives c5 ∈ {c1, w, v} ∪ T_int. Impossible.
- **Otherwise**, symmetrically, c1 ∈ L(R5 ∖ R1) ⊆ {c5, w, v} ∪ T_int. Impossible. ∎

**The arm exchange (as in v172 §2).** An F2-row that contains b6 and a whole arm has its remaining 10 − u vertices labelled exactly by {w} ∪ T_int.

## 3. c′ = 0 with nΛ = 2

v's F2-passages b6(0), ΛV1, ΛV2 and b6(λ) lie in consecutive F2-rows A, B, C and D. B and C both lie between b6(0) and b6(λ), so together they form a run [κ1, κ1 + 20] ⊆ [1, λ − 1]: two consecutive pure Λ-rows of F2, with κ1 ≥ 1 and κ1 + 20 ≤ λ − 1. Λ's other pass is in F1, so Lemma DP★ excludes this.

## 4. c′ = 1 with nΛ = 1

**F1.** Here n2 = 1 and n1 = n3 = 0, and v has no F1-cut. So its passages fill the rows in order:

| Row | Passage |
|---|---|
| R0 | t |
| R1 | t2V (S_12) |
| R2 | P2 |
| R3 | ΛV |
| R4 | P3 |
| R5 | t2V (S_23) |
| R6 | P5 |

Hence ℓ1 and ℓ3 lie in [6, 14], so R1 and R5 contain no Λ-vertex.

**F2.** v's passages b6(0), ΛV and b6(λ), one of them a cut, cover the four rows.
- **The cut is ΛV.** The two rows meeting at ΛV both lie inside (0, λ). They are consecutive pure Λ-rows, so Lemma DP★ applies.
- **The cut is b6(0).** The rows are [0, 10], [10, 20], [20, 30] ∋ λ and [30, 40].
  - The t3-arm lies in [20, 30]: λ + u ≤ 29, since otherwise [30, 40] repeats S-labels or c5 lies on the cut 30.
  - The t1-arm lies in [30, 40].
  - Every t1- and t3-vertex lies in these two rows.
  - The arm exchange against R6 and R0 puts all non-arm t1- and t3-labels in {w} ∪ T_int.
  - Lemma T7′ applies.
- **The cut is b6(λ).** The rows are [λ − 20, λ − 10] ∋ ΛV, [λ − 10, λ], [λ, λ + 10] and [λ + 10, λ + 20] ∋ 0.
  - The t1-arm lies in [λ + 10, λ + 20]: 30 − λ ≥ u + 1, by the same repetition argument.
  - The arm exchange against R6 (on [λ, λ + 10]) and R0 (on [λ + 10, λ + 20]) puts all non-arm t1- and t3-labels in {w} ∪ T_int.
  - Lemma T7′ applies.

## 5. Result

**WRITTEN:**
- In type 7, u ≥ 2.
- L1 type 7 with r2 = 4 survives only if v has a G2-V on t1 or on t3:
  - c′ = 0 with (nΛ, n1, n3) ∈ {(1,1,0), (1,0,1), (0,1,1), (0,2,0), (0,0,2)};
  - or c′ = 1 with n1 = 1 or n3 = 1.
- With v172, type 7 with r2 = 3 survives only with c′ = 0 and n1 = 1 (or n3 = 1).

**OPEN (m = 9, L1):**
- type 7 in the cases just listed;
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
