# Original Tuscan-2(11), entire m = 9 distance-two branch, part 59: L1 type 7 with r2 = 3 — Lemma T7; case c′ = 1 and the case of v's G2-V on Λ are impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq4-lambda21-24-closed-types3-9-closed-v171.md` (SHA256 `54aec9aebe264883a00663ade463a01f3d08cb63baa446f3a80e0ed9ebbf06e2`). It uses:
- the type-7 data of `D2-m9-L1-type7-r2eq2-closed-v157.md` §1 (SHA256 `458dce9de731858686a408c773870eb593a854937e2f5b1f46ac08bb40c724f2`);
- the v152 anatomy;
- the consecutive-rows property (v114 (I): in each face, the passages of one label lie in consecutive rows, with a cut passage covering two);
- the overlap exchange (OL).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 7 with r2 = 3: data

**Faces.** F1 = S_T S_12 P− S_23 and F2 = P+ S_31, with G1 = {T, t2} and G2 = {t1, t3, Λ}.

**Lengths.** r1 = 8, so F1 has 80 positions and F2 has 30. Then t + ℓ2 = 25, so ℓ2 = u + 15, and ℓ1 + λ + ℓ3 = 30.

**F1 positions.**
- t1[j] lies at 10 − u + j, and b3 at P1 = 10 − u + ℓ1.
- t2[j] lies at P2 − j, with b6 at P2 = 25 + ℓ1.
- Λ[k] lies at P3 − k, with b6 at P3 = 55 − ℓ3.
- t2[j] lies at P3 + j, with b3 at P4 = 70 + u − ℓ3.
- t3[j] lies at 70 + u − j, with b6 at P5 = 70 + u.
- T_int lies at 71 + u..79 and ℓ at 80.

**F2 offsets.** b6 at 0 and at λ; Λ[k] at k; t3[j] at λ + j; b3 at λ + ℓ3; t1[j] at 30 − j.

**Rows and labels.**
- R0 = ℓ, T_int, b6, t1[1..u] and R7 = t3[u..1], b6, T_int, ℓ, so S = L(t1[1..u]) = L(t3[1..u]).
- c1 = L(t1[u]) is cut at 10 and c5 = L(t3[u]) at 70.
- The labels are w, v, the 9 − u T_int-labels, and the u S-labels.

**Anatomy (v152).**
- An F1-cut label other than v and w has a = 2 and b = 3. An F2-cut label has a = 3 and b = 2.
- An F2-cut S-label therefore has exactly its two arm vertices as G2-vertices.
- v has n1 + n2 + n3 + nΛ = 2 and n1 + n3 + nΛ + c′ = 1.

## 2. Lemma T7

**Lemma T7.** If L(t1[u+1..ℓ1−1]) and L(t3[u+1..ℓ3−1]) are both contained in {w} ∪ T_int, the configuration is impossible.

*Proof.*
- **P1 ∈ [11, 19].** If P1 ≥ 21, then R1 = t1[u..u+10], and L(R1) ⊆ {c1, w} ∪ T_int, a set of 11 − u < 11 labels. P1 = 20 puts b3 on a cut.
- **P4 ∈ [61, 69].** The same argument applies to R6.
- **The two rows.** Hence R1 = t1[u..ℓ1−1], b3, t2[ℓ1+5..u+14] and R6 = t2[ℓ3+5..u+14], b3, t3[ℓ3−1..u].
- **ℓ1 ≥ ℓ3.** R1's t2-part lies inside R6's, so R1 ∖ R6 = t1[u..ℓ1−1]. Then OL gives c5 = L(t3[u]) ∈ L(R1 ∖ R6) ⊆ {c1, w} ∪ T_int. Impossible.
- **ℓ1 < ℓ3.** Symmetrically, R6 ∖ R1 = t3[u..ℓ3−1] and c1 ∈ {c5, w} ∪ T_int. Impossible. ∎

**The arm exchange.** Suppose an F2-row contains b6 together with a whole arm (t1[1..u] or t3[1..u]) and k further vertices. Then OL against R0 (for the t1-arm) or R7 (for the t3-arm) shows that those k vertices carry exactly {w} ∪ T_int.

**Arm cuts.** t1[u] and t3[u] (c1 and c5) are never F2-cuts. An arm vertex that is an F2-cut belongs to an F2-cut S-label, whose only G2-vertices are its two arms.

## 3. Case c′ = 1 (v is F2-cut)

**F1.** v has 2 V's on t2 and no F1-cut. By the consecutive-rows property its passages fill R0..R7 in order:

| Row | Passage |
|---|---|
| R0 | t |
| R1 | V_a (S_12) |
| R2 | V_b (S_12) |
| R3 | P2 |
| R4 | P3 |
| R5 | V_b (S_23) |
| R6 | V_a (S_23) |
| R7 | P5 |

V_a = t2[j_a] needs P2 − j_a ≤ 19 and P3 + j_a ≥ 61 with j_a ≤ u + 14. Hence ℓ1 and ℓ3 lie in [6, u + 8].

**F2.** v's two F2-passages are b6(0) and b6(λ), and one of them is its cut. The other must lie in the third row, which gives λ ∈ [11, 18].

**Sub-case I: the cut is b6(0).** The cuts are 0, 10 and 20.
- **λ + ℓ3 ≤ 19.**
  - The row [20, 30] is t1[10..1], b6. So the F1-window [10 − u, 20 − u] carries all labels.
  - Against R1, this gives L([21 − u, 20]) = {v} ∪ (S ∖ {c1}).
  - But ℓ1 = 30 − λ − ℓ3 ≥ 11 puts b3 at P1 ∈ [21 − u, 18]. Impossible.
- **λ + ℓ3 = 20** puts b3 on a cut.
- **λ + ℓ3 ≥ 21.**
  - The row [20, 30] is t3[20−λ..ℓ3−1], b3, t1[ℓ1−1..1], b6. Against R0, t3[20−λ..ℓ3−1] ∪ t1[u+1..ℓ1−1] carry T_int.
  - In the row [10, 20] = Λ[10..λ−1], b6(λ), t3[1..20−λ]:
    - the t3-arm lies in the interior, since t3[20 − λ] is T_int;
    - L(Λ[10]) is not an S-label (it is not an arm);
    - so t3[u+1..19−λ] carry labels from {w} ∪ T_int.
  - Lemma T7 applies.

**Sub-case II: the cut is b6(λ).** The cuts are λ − 10, λ and λ + 10.
- **ℓ3 ≥ 11.**
  - The row [λ, λ + 10] is b6, t3[1..10]. So the F1-window [60 + u, 70 + u] carries all labels.
  - Against R6, this gives L([60, 59 + u]) = (S ∖ {c5}) ∪ {v}.
  - But P4 ∈ [62, 59 + u] is b3. Impossible.
- **ℓ3 = 10** puts b3 on the cut λ + 10.
- **ℓ3 ≤ 9.**
  - The rows are [λ, λ + 10] = b6, t3[1..ℓ3−1], b3, t1[ℓ1−1..20−λ] and [λ + 10, λ + 20] = t1[20−λ..1], b6(0), Λ[1..λ−10].
  - 20 − λ ≥ u + 1 is forced: otherwise the first row repeats S-labels from both arms, or puts c1 on a cut.
  - Against R7, t3[u+1..ℓ3−1] ∪ t1[20−λ..ℓ1−1] carry T_int. Against R0, t1[u+1..20−λ] ∪ Λ[1..λ−10] carry {w} ∪ T_int.
  - Lemma T7 applies.

**So c′ = 1 is impossible.**

## 4. Case c′ = 0 with v's G2-V on Λ

**F2.** v's F2-passages b6(0), ΛV and b6(λ) lie in consecutive rows A, C and D. So:
- C = [κ1, κ1 + 10] is a pure Λ-row;
- D = [κ1 + 10, κ1 + 20] contains λ;
- the cut κ3 = κ1 + 20 lies in (λ, 30), and it is not b3.

**(i) κ3 = 30 − x lies on t1.**
- A = t1[x..1], b6, Λ[1..κ1], and D contains b6(λ), all of t3, b3 and t1[ℓ1−1..x].
- x ≥ u + 1 holds: otherwise D repeats S-labels or c1 lies on κ3.
- Against R0, t1[u+1..x] carry {w} ∪ T_int. Against R7, t3[u+1..ℓ3−1] ∪ t1[x..ℓ1−1] carry T_int.
- Lemma T7 applies.

**(ii) κ3 = λ + y lies on t3.**
- D = Λ[κ1+10..λ−1], b6, t3[1..y], and A contains t3[y..ℓ3−1], b3, all of t1 and b6(0).
- y ≥ u + 1 holds likewise.
- Against R7, t3[u+1..y] carry {w} ∪ T_int. Against R0, t3[y..ℓ3−1] ∪ t1[u+1..ℓ1−1] carry T_int.
- Lemma T7 applies.

## 5. Result

**WRITTEN:** L1 type 7 with r2 = 3 survives only with c′ = 0 and v's G2-V on t1 (n1 = 1) or, by the mirror (row reversal exchanges t1 and t3), on t3.

**OPEN (m = 9, L1):**
- type 7 with r2 = 3, c′ = 0, n1 = 1 (or n3 = 1);
- type 7 with r2 = 4;
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

L1 types 3, 4, 5, 6, 9 and 10 and L2 are closed. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
