# Original Tuscan-2(11), entire m = 9 distance-two branch, part 57: L1 type 9 with r2 = 4 and λ ∈ {12, 13, 14} is impossible (type 3 by the mirror)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq3-lambda14-u-ge5-closed-types3-9-r2eq3-closed-v169.md` (SHA256 `0ffe0db4b6a95e7cd360d50808d49c2f322b6e94ba0929259748f244ff2414f4`). It uses:
- the data and reductions of `D2-m9-L1-types9-3-r2eq4-lambda-reductions-v166.md` (SHA256 `4e6381c2cf9052bdc55357853efa837f76b1340cbce1c9f71e09ebfcf66e4f0e`);
- the v152 anatomy;
- the F2 conventions of v168 §3.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data (v166) for λ ∈ {12, 13, 14}

**F1 (70 positions).**
- t1[j] lies at 10 − u + j and at C2 − j.
- b3 lies at 15 and at B2 = 55 − λ ∈ {41, 42, 43}.
- b6 lies at t, at C1 = 15 + ℓ2, at C2 = 60 + u − λ and at C3 = 60 + u.
- t2[j] lies at C1 − j (run [16, 14 + ℓ2]) and t3[j] at C1 + j (run [16 + ℓ2, 54 − λ]).
- Λ is P+ on [61 + u − λ, 59 + u].
- By v166 (d) and (e), ℓ2 ≥ 5, and ℓ2 ≤ 25 in every remaining case (ℓ3 = 40 − λ − ℓ2 ≥ 1, with ℓ2 ∈ {26, 27} excluded there).

**R1 against R4.**
- R1 = t1[u..u+4], b3, positions 16–20. R4 = [40, 50] contains b3 (B2) and t1[u+4..u] (56 − λ..60 − λ).
- So R1 ∖ R4 = positions 16–20, and R4 ∖ R1 = positions 40..54 − λ (t3, when ℓ2 ≤ 24) together with 61 − λ..50.
- Both carry Q5 = {c5, X20, X30, X40, X50}, with X20 at 20.
- Hence positions 16–19 carry {c5, X30, X40, X50}, and the t3-positions 41..54 − λ carry F1-cut labels from Q5.
- t1[u+1..u+4] carry the four F2-cut labels.

**F2 = S_23 P− (40 positions).**
- b6 at offsets 0 and 40 − λ;
- t2[q] at offset q, which is F1 position 15 + ℓ2 − q;
- b3 at offset ℓ2;
- t3[40 − λ − q] at offset q ∈ [ℓ2 + 1, 39 − λ], which is F1 position 55 + ℓ2 − λ − q;
- Λ[k] at offset 40 − k.
- The four F2-rows are cut at o, o + 10, o + 20 and o + 30. Every F2-cut vertex carries an F2-cut label. So no F2-cut lies on b3 (w), on a vertex with a Q5-label, or (case (A)) on b6.

## 2. ℓ2 ∈ [5, 24]: X40 twice in one F2-row

X40 has two vertices in the block:
- one at an F1 position p ∈ [16, 19] (a t2-vertex, since ℓ2 ≥ 5), at F2 offset 15 + ℓ2 − p ∈ [ℓ2 − 4, ℓ2 − 1];
- its F1-cut vertex at position 40 (a t3-vertex, since 16 + ℓ2 ≤ 40), at F2 offset q40 = 15 + ℓ2 − λ ∈ {ℓ2 + 1, ℓ2 + 2, ℓ2 + 3}.

If v = X40, these are v's two G2-V's, so the argument is the same.

The F2 offsets strictly between them are:
- F1 positions in 16–19 (Q5-labels);
- b3 at ℓ2;
- F1 positions 41..54 − λ (Q5-labels).

None of these can be an F2-cut, and neither X40-vertex is one. So both lie in one F2-row, which carries X40 twice. Impossible.

## 3. ℓ2 = 25

**Setup.** Here C1 = 40, so the F1-cut at 40 is the corner b6 and **v = X40** (case (A): v is F1-cut, with two G2-V's and n1 = 0). λ = 12 and λ = 13 give ℓ3 = 3 and ℓ3 = 2, with t3 at 41..54 − λ; λ = 14 gives ℓ3 = 1. F1 positions 16–39 are t2[24..1], at F2 offsets 40 − p.

**v's vertices.**
- In F1, v has b6 at t (R0), at 40 (R3/R4) and at C3 = 60 + u (R6).
- C2 = 60 + u − λ ≥ 47 cannot lie in R4 (a second v) and cannot be the cut at 50 (that cut is X50 ≠ v). So C2 lies in R5.
- v's two G2-V's must therefore cover R1 and R2:
  - g1 sits at an F1 position in 16–19 (X40 ∈ Q5), at F2 offset in [21, 24];
  - g2 sits at an F1 position in 21–29, at F2 offset in [11, 19].
- In F2, v's four passages are b6 at 0, b6 at 40 − λ ∈ {26, 27, 28}, g1 and g2. They must lie in four different F2-rows.

**The cuts.**
- F1 R2 = [20, 30] is pure t2, so its F2-copy, the window [10, 20], carries all labels.
- Its end-labels X30 and X20 are F1-cut, so the window is not an F2-row and contains exactly one F2-cut o + 10 ∈ [11, 19], with o ∈ [1, 9].
- The cut o + 20 ∈ [21, 29] must avoid:
  - offsets 21–24 (Q5-labels);
  - b3 at 25;
  - b6 at 40 − λ;
  - the t3-offsets (Q5-labels).
- So it lies on Λ at offset ≥ 41 − λ, which gives o + 20 > 40 − λ.

**Contradiction.** Row B = [o + 10, o + 20] then contains both b6 at 40 − λ and g1, since o + 10 ≤ 19 < 21 ≤ g1 ≤ 24 < 26 ≤ 40 − λ < o + 20. So v occurs twice in row B. Impossible.

## 4. Result

**WRITTEN:**
- L1 type 9 with r2 = 4 and λ ∈ {12, 13, 14} is impossible.
- With v166, type 9 with r2 = 4 survives only with λ ∈ {21, 22, 23, 24} and λ ≤ 20 + u.
- By the mirror (v156 §3), the same holds for type 3.

**OPEN (m = 9, L1):**
- types 3 and 9 with r2 = 4 and λ ∈ [21, 24];
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
