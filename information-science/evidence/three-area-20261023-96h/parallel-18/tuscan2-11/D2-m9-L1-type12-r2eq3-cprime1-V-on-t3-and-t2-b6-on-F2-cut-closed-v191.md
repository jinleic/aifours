# Original Tuscan-2(11), entire m = 9 distance-two branch, part 78: L1 type 12 with r2 = 3, c′ = 1, V's on t3 and t2, b6 on an F2-cut — closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime1-V-on-t1-and-t2-b6-on-F2-cut-closed-v190.md` (SHA256 `3879267b83b7fc12239477613fca822dc82c5943c863cbce23e8d5b0f4f0ab23`).
- **Data and imports.** It uses the data of v186 §1, the imports of v188, the counts of v188 §1 and the grid lemma (v184 §2, SHA256 `cc0f130b350b434119cfc43806a961b1c671f4416b3b5fdc495e079c79db5532`).
- **The counts of v188 §1.** An F1-cut label has a = 2 and b = 3; an F2-cut label has a = 3 and b = 2; b3 never lies on a cut.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case (β3)

c′ = 1 and c = 0, with one V of v on t2 (t2V = t2[J]) and one on t3 (t3V = t3[j3]).

**v's F1 passages.** The middle ones, in order, are t2V₁₂ = P2 − J, P2, P3, t2V₂₃ = P3 + J, t3V and P5, one in each of R1..R6. Hence:
- ℓ1 = P3 − 25 ∈ [6,14], ℓ2 ∈ [6,14] and ℓ3 ∈ [16,24];
- P1 ≤ 18;
- P4 ≥ 42;
- t3V lies in R5 at P5 − j3, so P4 ≤ 58 and j3 ∈ [ℓ2−4, ℓ2+4].

**The G1-only pair R2, R3.** Put α = P2 − 20, β = 40 − P3, μ = ℓ1 − 5 and κ = 15 − ℓ2 = λ − u. Then:
- R2 = t2[α..1], b6 (P2), Λ[λ−1..μ];
- R3 = Λ[μ..1], b6 (P3), t2[1..β];
- R6 = t3[ℓ2−5..1], b6 (P5), Λ[1..κ];
- R7 = Λ[κ..λ−1], b6, T_int, ℓ.

The cuts are 20 = t2[α], 30 = Λ[μ] (X30), 40 = t2[β], 50, 60 = t3[ℓ2−5] and 70 = c7. J > max(α, β).

**(G0), (G-A).** These are word for word as in v190 §2, with (R3, R4) replaced by (R2, R3) and X40 by X30:
- w's single G1-W is t2[jw] with jw ≤ min(α, β), and w has no Λ-vertex.
- If μ < κ, then α < β, and:
  - **(I1)** L(t2[1..α]) ∪ L(Λ[μ..κ−1]) = {w} ∪ T_int, so X30 ∈ T_int;
  - **(I2)** L(t2[1..β]) = L(t3[1..ℓ2−5]) ∪ L(Λ[μ+1..κ]).

## 2. b6 on an F2-cut

The F2-cuts are 0, 10 and 20, and ℓ3 ≠ 20.

**ℓ3 ≤ 19.** Then ℓ1 ≥ 11 and [20,30] = t1[10..1], b6. Against R0 this gives L(t1[u+1..10]) = {w} ∪ T_int, so w lies on t1[u+1..9], at F1 positions 11..19, in R1. But b3 sits at P1 ∈ [12,18] ⊂ R1. So w appears twice in R1. **Impossible.** (If u = 9, L(t1[10]) = w lies on a cut.)

**ℓ3 ∈ [21,24].** Then ℓ1 ∈ [6,9], and the F2-rows are:
- E0 = b6, t3[1..10];
- E1 = t3[10..20] (pure);
- E2 = t3[20..ℓ3−1], b3, t1[ℓ1−1..1], b6.

Put τ10 = L(t3[10]) and τ20 = L(t3[20]).
- **Grid on E1.** E1 occupies F1 positions 35+ℓ2..45+ℓ2 around the cut 50, so ℓ2 ∈ [9,11]. Then P4 = 25 + ℓ1 + ℓ2 ≤ 45, and R5 = t3[ℓ2−5..ℓ2+5] is a pure t3-row.
- **μ < κ.** ℓ1 + ℓ2 ≤ 20, and = 20 would give μ = κ. So (G-A) applies.
- **E2 against R0:** L(t3[20..ℓ3−1]) ∪ L(t1[u+1..ℓ1−1]) = T_int. So τ20 ∈ T_int.
- **X30** (T and Λ[μ]; cut 30; P+ in R6). Its three G2 cover R1, R4 and R5:
  - a t1-vertex in t1[u+1..ℓ1−1] (in E2);
  - a t3-vertex of R4, i.e. t3[ℓ2+6..ℓ3−1]. It must lie in E1, so it is t3[ℓ2+6..19];
  - a t3-vertex of R5 lying in E0, i.e. t3[ℓ2−4..9].
- **τ20** (F2-cut). Its G2 are t3[20] (at F1 35+ℓ2, in R4) and a t3-vertex of the pure row R5. That vertex lies in E0, so it is in t3[ℓ2−4..9]. Its two G1 besides T must cover R1, R2, R3 and R6. The only way is:
  - t2[j] with S_12 in R1 and S_23 in R3 (α < j < β);
  - Λ[k] with P− in R2 and P+ in R6 (μ < k < κ).
- **v's neighbours** are b6's six, t2[J±1] (or b3), and t3[j3±1]. Here 11 ≤ j3 ≤ ℓ2 + 4 ≤ 15, because v's F2-cut is b6, so t3V lies inside E1. None of the vertices of τ20 other than its T-vertex is among them:
  - t2[j] with 1 < j < β < J is neither t2[1] nor next to t2[J];
  - Λ[k] has 1 < k < λ − 1;
  - the t3-indices 20 and ℓ2−4..9 are neither 1 nor next to j3 ≥ 11.

  The same holds for X30, except that Λ[μ] is adjacent to b6 when μ = 1. By (PC) both labels meet v. So τ20 is T_int's last vertex, Λ[1] carries X30, and **μ = 1, ℓ1 = 6**.
- **The numbers.** t2V₂₃ ∈ R4 needs P4 = 31 + ℓ2 ≥ 42, so ℓ2 = 11, κ = 4, β = 9 and ℓ3 = 24. The arm lies inside t1[1..5], so u ∈ {4,5}, α = 7 − u and λ = u + 4. Hence:
  - R1 = t1[u..5], b3 (16−u), t2[10..α];
  - R2 = t2[α..1], b6, Λ[u+3..1];
  - R3 = Λ[1], b6, t2[1..9].
- **u = 4.** X30's R1-vertex must be a t1-vertex of t1[u+1..5], because its G1 avoid R1. So u = 4 and t1[5] = X30, which makes α = 3.
- **E0 against R6** (which share b6 and t3[1..6]) gives L(t3[7..10]) = L(Λ[1..4]). So τ10 ∈ L(Λ[2..3]). τ20 also lies on Λ[2..3], so Λ[2..3] carry {τ10, τ20}, and the F2-cut labels are v, τ10 and τ20.
- **The last T_int labels.** By (I1), L(t2[1..3]) ∪ {X30, τ10, τ20} = {w} ∪ T_int, and |T_int| = 5. So t2[1..3] carries w and two F1-cut T_int-labels. Such a label has G1 = T + t2[j], and it must meet R1 = c1, X30, b3, t2[10..3]. It can do so only through a t2-passage in R1, which needs j = 3 (the cut 20). Two labels, one vertex. **Impossible.**

## 3. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1, v's V's on t3 and t2, and b6 on an F2-cut, is impossible. The same holds for its type-2 mirror image (v160 §1).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) and t1V on an F2-cut;
  - c′ = 1 with V's on (t3, t2) and t3V on an F2-cut.

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
