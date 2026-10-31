# Original Tuscan-2(11), entire m = 9 distance-two branch, part 77: L1 type 12 with r2 = 3, c′ = 1, V's on t1 and t2, b6 on an F2-cut — closed; the G1-only-pair lemma

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime1-V-on-t3-and-Lambda-closed-v189.md` (SHA256 `5f8447f6e6eda67ce7682440c4357fe1c7b2bf6c1effb14ca634f77f03c850b2`), with the data of v186 §1, the imports of v188 (v117, v152, v160 §1, v165 §1, v176 §1, v185 §2) and the counts of v188 §1 (an F1-cut label has a = 2 and b = 3; an F2-cut label has a = 3 and b = 2; b3 never lies on a cut).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case (β1)

c′ = 1 and c = 0, with one V of v on t1 (t1V) and one on t2 (t2V = t2[J]).

**v's F1 passages.** The middle ones, in order, are t1V, t2V₁₂ = P2 − J, P2, P3, t2V₂₃ = P3 + J and P5, one in each of R1..R6. Hence:
- ℓ1 = P3 − 25 ∈ [16,24] and ℓ2 = P5 − 55 ∈ [6,14], so ℓ3 ∈ [6,14];
- P1 < P2 − J ≤ 29, so P1 ≤ 28;
- P4 > P3 + J ≥ 51, so P4 ≥ 52.

## 2. The G1-only pair R3, R4

**The rows.** Put α = P2 − 30 ∈ [1,9], β = 50 − P3 ∈ [1,9], μ = 10 − β = ℓ1 − 15 and κ = 15 − ℓ2 = λ − u.
- R3 = t2[α..1], b6 (P2), Λ[λ−1..μ].
- R4 = Λ[μ..1], b6 (P3), t2[1..β].
- R6 = t3[ℓ2−5..1], b6 (P5), Λ[1..κ], **provided P4 < 60**. In every case, Λ[1..κ] occupy P5+1..70.
- R7 = Λ[κ..λ−1], b6, T_int, ℓ.

The cuts are 30 = t2[α], 40 = Λ[μ], 50 = t2[β] and 70 = Λ[κ] (c7), and 60 = t3[ℓ2−5] when P4 < 60. So **R3 and R4 contain no G2-vertex and no b3**, and the whole P− run of Λ lies in them. J ≥ β + 1, since t2V₂₃ ∈ R5. μ < κ means ℓ1 + ℓ2 ≤ 29, which gives P4 = 25 + ℓ1 + ℓ2 ≤ 54.

**(G0)**
- **w.** w must meet R3 and R4 with its single G1-W, so that G1-W is t2[jw] with jw ≤ min(α, β), and w has no Λ-vertex.
- **R6.** Λ[1..κ−1] have P+ strictly inside R6, so they carry distinct labels, none equal to v or c7. Also μ ≠ κ (c7 is cut at 70).

**(G-A) μ < κ.** Then:
- **(I1)** R3 against R7: L(t2[1..α]) ∪ L(Λ[μ..κ−1]) = {w} ∪ T_int. So X40 := L(Λ[μ]) ∈ T_int.
- **(I2)** R4 against R6: L(t2[1..β]) = L(t3[1..ℓ2−5]) ∪ L(Λ[μ+1..κ]).
- **α < β.** If α ≥ β, R3 against R4 gives L(Λ[1..μ−1]) = L(t2[β+1..α]) ∪ L(Λ[μ+1..λ−1]). That set contains c7, so c7 would have a second vertex inside R6.
- **(I3)** Hence L(Λ[μ+1..λ−1]) = L(Λ[1..μ−1]) ∪ L(t2[α+1..β]).
- **Consequences.** c7 lies on t2[α+1..β], and w (on t2[1..α]) lies on t3[1..ℓ2−6] by (I2).

**(G-B) μ > κ and P4 < 60.** Then:
- **(I1′)** L(t2[1..α]) = L(Λ[κ..μ−1]) ∪ T_int ∪ {w}.
- **(I2′)** L(t3[1..ℓ2−5]) = L(Λ[κ+1..μ]) ∪ L(t2[1..β]).
- **α > β.** If α ≤ β, then c7 ∈ L(t2[1..α]) ⊆ L(t3[1..ℓ2−5]), which is a second c7 in R6.
- **Consequences.** c7 lies on t2[β+1..α], and w lies on t3[1..ℓ2−6].

## 3. (β1-i): b6 on an F2-cut

The F2-cuts are 0, 10 and 20, and ℓ3 ≠ 10. The F2-row E2 = [20,30] = t1[10..1], b6.

**3.1 R1 is pure.**
- E2 against R0 gives L(t1[u+1..10]) = {w} ∪ T_int.
- τ\* := L(t1[10]) lies on the cut 20, so τ\* ∈ T_int and w lies on t1[u+1..9], in R1.
- So P1 ∉ R1, i.e. P1 ≥ 21, and **R1 = t1[u..u+10] is pure**, with ends c1 and X20 := L(t1[u+10]).
- R1's labels are c1, then {w} ∪ T_int on t1[u+1..10], then (S ∖ {c1}) ∪ {v} on t1[11..u+10]. So X20 ∈ S and t1V ∈ t1[11..u+9].

**3.2 ℓ3 ≤ 9 is impossible.** Then E1 = [10,20] = t1[20..10] is pure. E1 against R1 gives L(t1[u..9]) = L(t1[u+11..20]). So w also lies on t1[u+11..20], at F1 positions 21..30−u inside R2, before P1 ≥ 31 − u. With b3 at P1 ∈ R2, w appears twice in R2.

**3.3 The case ℓ3 ∈ [11,14] (ℓ1 ∈ [16,19]).** Here E0 = b6, t3[1..10] and E1 = t3[10..ℓ3−1], b3, t1[ℓ1−1..10].
- **E1 against R1** (removing w) gives L(t3[10..ℓ3−1]) ∪ L(t1[u+11..ℓ1−1]) = {c1} ∪ (T_int ∖ {τ\*}). So τ10 := L(t3[10]) ∈ T_int, the three F2-cut labels are v, τ\* and τ10, and every S-label is F1-cut.
- **S-labels other than c1.** Their G2 are exactly their t1-arm vertex (E2), a t1-vertex in t1[11..u+10] (E1) and a t3-vertex in t3[1..9] (E0).
- **S-labels other than c1 and X20.** Such a label meets R2 = t1[u+10..ℓ1−1], b3, t2[ℓ2−1..α] only through t2, so it has a t2-vertex t2[j] with j ≥ α.

**Case μ > κ.** Here ℓ1 + ℓ2 ≤ 33, so P4 ≤ 58 and (G-B) applies. c7 ∉ {c1, X20}, and its only non-arm G1 is a t2-vertex t2[j] with j ≥ α. By (G-B), j ≤ α. So c7 = L(t2[α]) sits on the cut 30. **Impossible.**

**Case μ < κ.** Here P4 = 25 + ℓ1 + ℓ2 ≤ 54, so R5 contains t3-vertices.
- **X20.** Its rows so far are R0, R1/R2 (cut 20), R3 (arm P−; the arm lies in R3 because κ > μ) and R7. It needs R4, R5 and R6 from one G1 and one G2. A t2-vertex would have S_12 in R2 ∪ R3, which are taken. So the G1 is Λ[k] with P− ∈ R4 and P+ ∈ R6, i.e. 1 ≤ k ≤ μ − 1, and **μ ≥ 2**.
- **X40** (∈ T_int by (I1); cut 40; P+ of Λ[μ] in R6). Its three G2 cover R1, R2 and R5:
  - a t1-vertex in t1[u+1..9];
  - a t1-vertex in t1[u+11..ℓ1−1], the only G2 of R2 apart from X20's;
  - a t3-vertex, which must lie in E0, hence in t3[ℓ2−4..9].
- **τ10.** Its G2 are t3[10] (in R5) and a t1-vertex in t1[u+1..9] (R1 is pure, and τ10 is not one of R1's end labels c1, X20). Besides T, its two G1 must cover R2, R3, R4 and R6. The only way is:
  - Λ[k] with P− in R3 and P+ in R6 (μ+1 ≤ k ≤ κ−1);
  - t2[j] with S_12 in R2 and S_23 in R4 (α < j ≤ β).

  Using t2 for R3 and R4 would leave R2 and R6 to one G1, and using Λ for R4 and R6 would leave R2 and R3 to one t2. Both are impossible.
- **(PC) at v.** v's neighbours are:
  - b6's six: T_int's last vertex, t1[1], t2[1], t3[1], Λ[1] and Λ[λ−1];
  - t1V's two, on t1[10..u+10];
  - t2V's two, t2[J−1] with J − 1 ≥ β, and t2[J+1] or b3.

  Apart from its T-vertex, no vertex of X40 or of τ10 is among them:
  - Λ-indices 2 ≤ μ and μ+1..κ−1 lie strictly between 1 and λ − 1;
  - t1-vertices in t1[u+1..9] or t1[u+11..ℓ1−1] are neither t1[1] nor adjacent to t1[11..u+9];
  - t3-indices ≥ 2;
  - τ10's t2[j] with j ≤ β is t2[1] for no j > α, and is adjacent to t2[J] only if j = β, but t2[β] carries X50 ≠ τ10.

  So v meets both X40 and τ10 only through T_int's last vertex, which has a single label. **(PC) fails.**

## 4. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1, v's V's on t1 and t2, and b6 on an F2-cut, is impossible. The same holds for its type-2 mirror image (v160 §1).

**WRITTEN (lemma):** For type 12 with r2 = 3, c′ = 1 and V's on t1 and t2, (G0), (G-A) and (G-B) of §2 hold.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) and t1V on an F2-cut;
  - c′ = 1 with V's on (t3, t2).

  These are in type-12 notation; type 2 is the mirror.
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
