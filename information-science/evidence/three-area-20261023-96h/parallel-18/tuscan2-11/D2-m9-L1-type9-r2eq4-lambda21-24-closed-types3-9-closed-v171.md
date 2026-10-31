# Original Tuscan-2(11), entire m = 9 distance-two branch, part 58: L1 type 9 with r2 = 4 and λ ∈ [21, 24] is impossible, so L1 types 3 and 9 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq4-lambda12-14-closed-v170.md` (SHA256 `94d814050b7585809f8ede7b7668b03191eb317a947d8438a51683854a969e44`). It uses:
- the data of v166;
- Lemma DP★ of v165;
- the v152 anatomy;
- the F2 conventions of v170 §1.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data for λ ∈ [21, 24] (so u ≥ λ − 20 ≥ 1)

**F1.**
- b3 lies at 15 and at B2 = 55 − λ ∈ [31, 34].
- b6 lies at t, at C1 = 15 + ℓ2, at C2 = 60 + u − λ ∈ [40, 49] and at C3 = 60 + u.
- t2 runs over [16, 14 + ℓ2] and t3 over [16 + ℓ2, 54 − λ], with 54 − λ ≥ 30.
- ℓ2 + ℓ3 = 40 − λ.
- The run [55 − λ, 60 − λ] = b3, t1[u+4..u] lies inside R3 = [30, 40].

**Q5 positions.**
- R1 ∩ R3 = {b3, t1[u..u+4]}.
- So R1 ∖ R3 = positions 16–20 and R3 ∖ R1 = {30..54 − λ} ∪ {61 − λ..40}, and both carry Q5 = {c5, X20, X30, X40, X50}.
- Hence positions 16–19 carry {c5, X30, X40, X50}, and every block position 31..54 − λ carries a Q5-label.

**F2 (40 positions).**
- b6 lies at offsets 0 and β := 40 − λ ∈ [16, 19].
- t2[q] lies at offset q (F1 position 15 + ℓ2 − q), and b3 at ℓ2.
- An offset q ∈ [ℓ2 + 1, β − 1] carries a t3-vertex at F1 position 55 + ℓ2 − λ − q.
- Λ[k] lies at offset 40 − k.
- No F2-cut lies on b3, on a Q5-labelled vertex, or (in case (A)) on b6.

**(DP) No F2-cut lies in [β + 1, 19].** A cut c′ there makes [c′, c′ + 20] = Λ[40 − c′..20 − c′] two consecutive pure F2-rows, with s = 20 − c′ ≥ 1 and s + 20 ≤ λ − 1. Λ's other pass is in F1, so Lemma DP★ applies. For λ = 21 the interval is empty.

**Copies of R2.** Whenever R2 = [20, 30] is a pure t2- or t3-row, its F2-copy is an 11-window carrying all labels.
- Its end-labels are X30 and X20, both F1-cut, so the window is not an F2-row.
- So it contains exactly one F2-cut c, in its interior.

## 2. ℓ2 ∈ [5, 14]: X30 twice

X30 has two vertices in the block:
- one at an F1 position in 16–19, a t2-vertex at an offset in [ℓ2 − 4, ℓ2 − 1];
- its F1-cut vertex at 30, a t3-vertex at offset β − 15 + ℓ2 ∈ [ℓ2 + 1, ℓ2 + 4].

If v = X30, these are v's two G2-V's. The offsets strictly between them carry Q5-labels (F1 positions 16–19 and 31..54 − λ) or b3, so no cut separates them. X30 occurs twice in one F2-row. Impossible.

## 3. ℓ2 = 15

- C1 = 30, so v = X30 (case (A)).
- R2 = t2[10..1] together with C1, and its F2-copy is the window [0, 10] (b6 at 0, then t2[1..10]).
- Its single cut c lies in [1, 9], so c + 10 ∈ [11, 19]. But offsets 11–14 (Q5), 15 (b3), 16..β − 1 (t3, Q5) and β (b6) cannot be cuts.
- So c + 10 ∈ [β + 1, 19], which contradicts (DP).

## 4. ℓ2 ≥ 16 (so ℓ3 ≤ 3 and C1 ∈ [31, 33] ⊆ R3)

**Case (B).** v ∈ R3 ∖ R1 (C1), but R3 ∖ R1 carries Q5, while v is F2-cut. Also v's t1-vertex t1[u+i] has its S_31-passage at 60 − λ − i ∈ R3. Impossible.

**Case (A).**
- If C2 = 40, v appears in R3 twice, at C1 and at 40. So C2 ∈ [41, 49].
- v's b6-corners then cover R0, R3, R4 and R6. Its two G2-V's, one of them an F1-cut, must cover R1, R2 and R5. Only the cut at 20 fits, so v = X20.
- R2 = t2[ℓ2−5..ℓ2−15] is pure. Its copy [ℓ2 − 15, ℓ2 − 5] has its cut c ∈ [ℓ2 − 14, ℓ2 − 6].
- c + 10 ∈ [ℓ2 − 4, ℓ2 + 4] must avoid [ℓ2 − 4, β], which holds Q5 (16–19), b3, t3 (Q5) and b6. So c + 10 ≥ β + 1.
- Then row [c, c + 10] contains both v = X20 (offset ℓ2 − 5) and b6 at β. Impossible.

## 5. ℓ2 ≤ 4

- C1 ∈ [16, 19], so v ∈ Q5 (case (A)), and R2 = t3[5−ℓ2..15−ℓ2] is pure.
- Its copy is [β − 15 + ℓ2, β − 5 + ℓ2], with its cut c in the interior.
- **c ≤ 9.** Offsets [0, β − 15 + ℓ2] cannot be cuts: they are b6, then t2 (Q5), b3, t3 at F1 31..54 − λ (Q5), and X30. So the preceding cut c − 10 must be negative.
- **c + 10 ≥ β + 1.** Offsets β − 4 + ℓ2..β − 1 (F1 positions 16 + ℓ2..19, Q5) and β (b6) cannot be cuts.
- So c + 10 ∈ [β + 1, 19], which contradicts (DP).

## 6. Result

**WRITTEN:**
- L1 type 9 with r2 = 4 and λ ∈ [21, 24] is impossible.
- With v166 and v170, L1 type 9 with r2 = 4 is impossible.
- With v156 (r2 = 2), v158, v159, v168 and v169 (r2 = 3), and the atlas of v167 (r2 ∈ {2, 3, 4}), **L1 types 9 and 3 are impossible** (type 3 by the mirror, v156 §3).

**OPEN (m = 9, L1):**
- type 7 with r2 ∈ {3, 4};
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

L2 is closed (v151). The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
