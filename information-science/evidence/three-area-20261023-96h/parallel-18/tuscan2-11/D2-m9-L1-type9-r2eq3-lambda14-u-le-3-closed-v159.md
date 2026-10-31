# Original Tuscan-2(11), entire m = 9 distance-two branch, part 46: L1 type 9 with r2 = 3, λ = 14 and u ≤ 3 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq3-reduced-to-lambda14-v158.md` (SHA256 `935a59a9c54429e9a6d2fb5dc827e38d2a010e882038fb605c9fe2556c5eb204`) and uses its §1 data, the v152 anatomy and the overlap exchange. Rows of F2 are cut every 10 positions of F2, exactly as rows of F1 are.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data (type 9, r2 = 3, λ = 14, u ≤ 3)

**F1 (v158 §1 with λ = 14).**
- ℓ2 + ℓ3 = 16, B1 = 25, B2 = 41, C2 = 56 + u.
- t1[j] lies at 10 − u + j (S_12) and at 56 + u − j (S_31).
- Λ[k] lies at 56 + u + k (P+), so c5 = L(Λ[14−u]) is the cut at 70.

**Rows.**
- R1 = t1[u..u+10] (pure).
- R2 ⊆ [20, 30] and R3 = [30, 40] contain no Λ-vertex. Their G2-vertices are t2- and t3-vertices.
- R5 = [50, 60] = t1[u+6..1], b6 (= C2 at 56 + u), Λ[1..4−u].
- R6 = [60, 70] = Λ[4−u..14−u] is a pure P+-row.
- Every t1-arm passage 56 + u − j (1 ≤ j ≤ u) lies in [56, 58] ⊂ R5.

**F2 = S_23 P− (30 positions).**
- b6 at z, t2[j] at z + j, b3 at z + ℓ2, then t3, b6 at z + 16, and Λ[k] at z + 30 − k for k = 13..1.
- So v's b6 occurs in F2 exactly at z + 16 and at z + 30 ≡ z.

## 2. Two facts

**(F1) X60 ∉ S, where X60 is the label of the cut vertex Λ[4−u] at 60.** That cut covers R5, which already contains every S-label once, through its t1-arm.

**(F2) Λ[14−u] is c5's only Λ-vertex.**
- c5 (F1-cut, a = 2, b = 3) covers R6 and R7 by its cut.
- Its t1-arm vertex covers R0 and R5.
- R1 is a pure t1-row, so c5 needs a second t1-vertex g5 there, with its S_12-passage in R1. T is excluded, since it would repeat R7.
- g5's S_31-passage cannot lie in R5 (the arm is there), so it lies in R4.
- c5's two remaining G2-vertices therefore cover R2 and R3, which contain no Λ-vertex.

## 3. The F2-copy of R6

**The window W6.** The vertices of R6 occupy the F2-window W6 = [z + 16 + u, z + 26 + u], with Λ[14−u] (c5) first and Λ[4−u] (X60) last. W6 carries all 11 labels.

**Alignment.** W6 is not an F2-row, because then Λ[14−u] would lie on an F2-cut, a second cut of c5. So W6 = [10b + s, 10b + s + 10] with 1 ≤ s ≤ 9, and it meets the F2-rows f_b and f_{b+1}.

**The two exchanges.**
- f_b ∖ W6 consists of the s positions before W6, and W6 ∖ f_b of the last s positions of W6. The latter carry the R6-positions [60, 59 + s].
- f_{b+1} ∖ W6 consists of the 10 − s positions after W6, and W6 ∖ f_{b+1} of the first 10 − s positions of W6. The latter carry the R6-positions [61 + s, 70], including c5.

**F2-positions just before W6:** Λ[15−u..13] at z + 17..z + 15 + u (these carry S ∖ {c5}), and b6 at z + 16.

**F2-positions just after W6:** Λ[3−u..1] at z + 27 + u..z + 29, b6 at z + 30, then t2[1], t2[2], ….

## 4. The cases

**s ≤ u − 1.**
- f_b ∖ W6 lies inside Λ[15−u..13], so its labels lie in S.
- But W6 ∖ f_b contains X60, at R6-position 60. This contradicts (F1).

**u ≤ s ≤ u + 5.**
- f_b ∖ W6 contains b6 (z + 16). So v occurs at an R6-position in [61, 59 + s]. (Position 60 is X60 ≠ v, since X60's cut covers R5 and v's b6 at 56 + u is already in R5.)
- f_{b+1} ∖ W6 runs from z + 27 + u to z + 36 + u − s ≥ z + 31, so it contains b6 (z + 30). So v also occurs at an R6-position in [61 + s, 70].
- Then v occurs twice in R6. Impossible.

**s ≥ u + 6.**
- f_{b+1} ∖ W6 lies inside Λ[3−u..1] ∪ {b6}.
- But it must contain c5 (from W6 ∖ f_{b+1}). By (F2) and c5 ≠ v, this is impossible.

## 5. Result

**WRITTEN:** L1 type 9 with r2 = 3, λ = 14 and u ≤ 3 is impossible. With v158, **type 9 with r2 = 3 survives only with λ = 14 and u ≥ 4**. By the mirror (v156 §3), the same holds for type 3.

**OPEN:**
- types 3 and 9 with r2 = 3, λ = 14, u ≥ 4;
- types 3 and 9 with r2 = 4;
- type 7 with r2 ∈ {3, 4};
- types 2 and 12 with r2 ∈ {2, 3, 4};
- types 1, 8 and 11 (v152 restrictions).

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
