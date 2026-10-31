# Original Tuscan-2(11), entire m = 9 distance-two branch, part 85: L1 type 12, r2 = 3, c′ = 0, one V on each G2-thread — the sub-case k = 4 with b3 in Q2 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime0-alpha3-k2-and-k3-closed-v197.md` (SHA256 `d6584b49cc2e30abfa8a638bca7c5b79f5441a3ca975e2d433cbea500cf5a2a8`). It uses the notation of v196 §1 and the G1-only-pair lemma (v190 §2, transposed to the pair (R2, R3) as in v191 §1):
- α = P2 − 20, β = 40 − P3, μ = ℓ1 − 5, κ = 15 − ℓ2;
- (G0) and (G-A) with (I1) and (I2).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**The cut and the rows.** k = 4: v's cut is t3V at 50, with t1V ∈ R1, P2 ∈ R2, P3 ∈ R3 and P5 ∈ R6.
- So ℓ1, ℓ2 ∈ [6,14], ℓ3 ≥ 16, and t3V = t3[ℓ2+5].
- R5 = t3[ℓ2+5..ℓ2−5] is a pure t3-row.
- If P4 ≤ 39, R4 would be a pure t3-row as well, which DP★ excludes. So P4 ∈ [41,49] and R4 = t2[β..ℓ2−1], b3, t3[ℓ3−1..ℓ2+6], v.

**b3 ∈ Q2.** So Q1 = t3[10−x..20−x] is a pure t3-row with t3V inside. Comparing Q1 with R5 (difference paths of size 15 − ℓ2 − x, one end on the cut 60) and with R4 (size ℓ2 + x − 5) gives, by "one cut per label" and (E), **ℓ2 + x ∈ [9,11]**. So x ≤ 5 < ℓ1.

**The F2-cut labels.** These are f0 = L(t1[x]), f1 = L(t3[10−x]) (F1 position 45+ℓ2+x, in R5) and f2 = L(t3[20−x]) (F1 position 35+ℓ2+x, in R4).

## 2. The labels

**f2.**
- Its G2 are t3[20−x] and a t3-vertex of the pure row R5, which lies in Q0, i.e. t3[ℓ2−4..9−x]. So f2 ∈ T_int.
- Its two G1 besides T must cover R1, R2, R3 and R6. R1 can only be reached by a t2-passage, so these are a t2-vertex with S_12 in R1 and S_23 in R3, and a Λ-vertex with P− in R2 and P+ in R6.
- Hence P1 ≤ 19, and μ < k ≤ κ − 1, i.e. ℓ1 + ℓ2 ≤ 18.

**(G-A) applies.** R2 and R3 form a G1-only pair, and μ < κ. So α < β, X30 = L(Λ[μ]) ∈ T_int, w's G1-W is t2[jw] with jw < α (so α ≥ 2), and w lies on t3[1..ℓ2−6].

**f2 meets v only through T_int's last vertex.**
- v's neighbours are b6's six (T_last, t1[1], t2[1], t3[1], Λ[1], Λ[λ−1]), t1V's two and t3[ℓ2+4], t3[ℓ2+6].
- f2's t2-vertex (α < j < β) and Λ-vertex (μ < k < κ) are none of these.
- Its t3-indices, 20 − x and ≤ 9 − x, are neither 1 nor within 1 of ℓ2 + 5, since ℓ2 + x ∈ [9,11].

**f1 ∈ S.**
- If f1 were a T_int-label, its second G2 would lie in Q2. A t1-vertex of R1 there would leave R4 to a t2-vertex t2[j] with j > β > α, whose S_12 also lies in R1 (Λ's P− never reaches R4). So that G2 is a t3-vertex of R4 ∩ Q2, and f1 = {T, t2 (R1, R3), Λ (R2, R6), t3[10−x], t3[21−x..ℓ3−1]}.
- Like f2, it would then meet v only through T_last, contrary to (PC).
- So f1 is an S-label, with G2 its t1-arm vertex (in Q2, index in [x+1, u−1]) and t3[10−x]. Hence x ≤ u − 2, and **f0 is an S-label** too, t1[x] being an arm vertex.

**T_int.**
- f0 and f1 are S-labels, so the only F2-cut T_int-label is f2.
- An F1-cut T_int-label has a single G1 besides T covering R2 and R3: t2[j] with j ≤ α and j < β, or Λ[μ]. Its cut is therefore 20 (X20), 30 (X30) or 60 (X60).
- So T_int ⊆ {f2, X20, X30, X60}, and u ≥ 5. Since α = ℓ1 + ℓ2 − u − 10 ≥ 2 and ℓ1 + ℓ2 ≤ 18, u ≤ 6.

**Non-arm Λ-vertices.** Λ[1..κ−1] have P+ inside R6, so they carry distinct labels. Exactly five labels have such a vertex:
- f2;
- f0 and f1, whose G1 are the arm, a t2-vertex covering R1 and R4, and a non-arm Λ covering R6;
- X30 = Λ[μ];
- c1, whose second G1 must be a non-arm Λ. A t2 would have to cover the row of R2, R3 not covered by c1's arm, together with R4. That needs j < α and j > β, or a double cover.

Every other label's G1 are T or the arm, plus t2-vertices. So κ − 1 = 5, i.e. **ℓ2 = 9**, x ∈ {1,2} and ℓ1 ∈ [7,9].

**Pinning the rest.**
- (I1) says t2[1..α] ∪ Λ[μ..5] carry {w} ∪ T_int.
- Of the non-arm labels, only f2 and X30 lie in T_int. So 6 − μ ≤ 2, which forces **ℓ1 = 9**, μ = 4, Λ[4] = X30, Λ[5] = f2 and α = 8 − u.
- So t2[1..α] carries w, X20 (at t2[α]) and, if u = 5, X60.

## 3. The two shapes

Here ℓ3 = 21, P3 = 34, P4 = 43, P5 = 64 and β = 6.
- **R1.** R1 = t1[u..8], b3, t2[8..α]. Its t1-vertices besides c1 carry exactly the labels that must meet R1 on t1: v, X30 and, if u = 5, X60. So t1[u+1..8] = {v, X30} for u = 6, and {v, X30, X60} for u = 5.
- **R6.** R6 = t3[4] (X60), t3[3..1], b6, Λ[1..6], with Λ[1..3] = {f0, f1, c1}. So t3[1..3] = {w, X20, X40}.
- **T.** f2 is T_int's last vertex (§2), so T_int[1] is one of the other T_int-labels.

**u = 6** (α = 2, T_int = {f2, X20, X30}).
- t2[1] = w and t2[2] = X20, so w is joined to v (b6t2[1]) and to X20.
- T_int[1] ≠ X20, so T_int[1] = X30, and w is joined to X30 through ℓ.
- b3's neighbour t1[8] ∈ {v, X30} repeats one of these pairs. **(PC) fails.**

**u = 5** (α = 3, T_int = {f2, X20, X30, X60}). t2[3] = X20 and t2[1..2] carry {w, X60}, so w–X60 is used.
- **b3 and ℓ.** t1[8] ∈ {v, X30} and T_int[1] ∈ {X20, X30}.
- **The F2-rows.** For x = 1 they force t3[20] = X20, and for x = 2 they force t3[19..20] = {c7, X20}:
  - Q0 and Q2 each contain every label once;
  - Q0 = t1[x..1], b6, t3[1..10−x] and Q2 = t3[20−x..20], b3, t1[8..x];
  - for x = 2, t1[1] = c7.
- **w = t2[1].** Then w–v is used, so t1[8] = X30, so T_int[1] = X20.
  - For x = 1, b3t3[20] repeats w–X20.
  - For x = 2, w's t3-vertex in R6 ∩ Q0 = t3[1..3] has neighbours among b6, X20, X40 and t3[4] = X60. Each choice repeats v, X20 or X60.
- **w = t2[2].** Then w–X20 is used, so T_int[1] = X30 and t1[8] = v. The same two F2 facts give the same repeats.

**(PC) fails** in every branch.

## 4. Result

**WRITTEN:** In L1 type 12 with r2 = 3, c′ = 0 and one V on each of t1 and t3, the sub-case k = 4 with b3 in Q2 is impossible. The same holds for its type-2 mirror image (v160 §1).

With v196 and v197, only **k = 1** remains in (α3).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3, c′ = 0, one V on each G2-thread, k = 1 (type-12 notation; type 2 is the mirror);
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
