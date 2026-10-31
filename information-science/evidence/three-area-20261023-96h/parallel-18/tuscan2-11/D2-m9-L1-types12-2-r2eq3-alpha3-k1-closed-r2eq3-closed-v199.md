# Original Tuscan-2(11), entire m = 9 distance-two branch, part 86: L1 types 12 and 2 with r2 = 3 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime0-alpha3-k4B2-closed-v198.md` (SHA256 `db608654461efa9977198307fcd82deb45388b7d55ce752b1239d6c7b0b74713`). It closes the last sub-case of (α3), k = 1, using the notation of v196 §1 and the G1-only-pair lemma of v190 §2 for the pair (R3, R4):
- α = P2 − 30, β = 25 − ℓ1, μ = ℓ1 − 15, κ = 15 − ℓ2;
- (G0), (G-A), (G-B), and (I3′): R3 against R4 for α > β.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up for k = 1

**The cut and R1.** v's cut is t1V = t1[u+10] at 20, with P2 ∈ R3, P3 ∈ R4, t3V ∈ R5 and P5 ∈ R6.
- So ℓ1 ∈ [16,24], ℓ2 ∈ [6,14] and ℓ3 ∈ [6,14].
- P1 ∈ [21,29]: P1 ≥ 31 would make R1 and R2 consecutive pure t1-rows (DP★).
- So R1 = t1[u..u+10] is pure, with ends c1 and v.

**F2.** t1V lies inside Q2, so x > u. Q0 holds b6 and the whole t1-arm, and the arm exchange gives L(t1[u+1..x] ∪ t3[1..10−x]) = {w} ∪ T_int. So f0 = L(t1[x]) and f1 = L(t3[10−x]) lie in T_int.

**w.**
- w's rows R0, R7 (ℓ), R2 (P1) and P4's row are covered. Once P4 ≥ 51 (shown below in each case), R3 and R4 form a G1-only pair. Then w's G1-W is t2[jw] with jw < min(α, β) (G0), P4 ∈ R5, and w's two G2-W's lie in R1 and R6.
- By (G-A)/(G-B), w lies on t3[1..ℓ2−6].

## 2. Case B1 (b3 ∈ Q1)

**The numbers.**
- Q2 = t1[x..x+10] is a pure t1-row. Q2 against R1 (pieces x − u; size 1 would put c1 on an F2-cut) and against R2 (pieces u + 10 − x) give x − u ∈ [4,6].
- w's G2-W's lie in Q0 and Q2 (W-rule). Its Q2 one lies in R1, since R2 already holds b3. So its Q0 one is not in R1 and must be t3[1..9−x]. Hence x ≤ 8, so **u = 4, x = 8 and w = L(t3[1])**.
- Then ℓ3 < 20 − x gives ℓ1 ≥ 19, and P4 ≥ 51. f1 = L(t3[2]).

**The labels.**
- R1 against Q2 gives L(t1[4..7]) = L(t1[15..18]). So f2 := L(t1[18]) (F2-cut) lies in L(t1[5..7]).
- t1[5..7] carry {f2, τa, τb} with T_int = {f0, f1, f2, τa, τb}, t1[15..17] carry {c1, τa, τb}, and t1[9..13] carry {w, f1} and the three S-labels other than c1.
- **R2.** R2 = v, t1[15..17], f2, t1[19..ℓ1−1], w (b3), t2[ℓ2−1..α]. So t1[19..ℓ1−1] ∪ t2[α..ℓ2−1] carry {f0, f1} and the S-labels other than c1. Since t2[α] lies on the cut 30, **X30 is an S-label**.

**Case B is forced.**
- f2's G2 are t1[18] (R2) and a t1-vertex of t1[5..7] (R1). Its two G1 besides T must cover R3, R4, R5 and R6. R5 is reached only by a t2-passage S_23 with j > β, whose S_12 must then lie in R3 (j < α). R6 is reached only by a non-arm Λ[k], k ≤ κ − 1, with P− in R4.
- So α > β, i.e. μ > κ (Case (G-B)). Hence X40 = L(Λ[μ]) is an arm label, and S = {c1, c7, X30, X40}.
- X30's arm P− lies in R4 (R3 is covered by its cut), so X30 is of type I (arm vertex in Λ[κ+1..μ−1]). So #type I = μ − κ − 1 = ℓ1 + ℓ2 − 31 ≥ 1.
- Also t3V ∈ R5 forces P4 ≤ 58, so ℓ1 + ℓ2 ∈ [32,33].

**Non-arm Λ-vertices.**
- Q0 against R6 (sharing b6, t3[1..2]) gives L(t1[1..8]) = L(t3[3..ℓ2−5]) ∪ L(Λ[1..κ]). So the non-arm vertices Λ[1..κ−1] carry labels of S ∪ {f0, f2, τa, τb}.
- Of these, a non-arm Λ belongs exactly to:
  - the type-II S-labels (one each, by (I3′));
  - f2;
  - possibly f0.

  The τ's have G1 T and a t2-vertex, since Λ[μ] is an arm vertex in Case B.
- With #type II = 9 − α = 33 − ℓ1 − ℓ2 and κ − 1 = 14 − ℓ2, this gives ℓ1 = 20 + [f0 has a non-arm Λ] ∈ {20, 21}. So (ℓ1, ℓ2) ∈ {(20,12), (20,13), (21,11), (21,12)}.

**c1 = L(t3[ℓ3−1]).** By (PC), w is joined to c1.
- c1's vertices are t1[4], one of t1[15..17], its arm vertex, a second G1 (a non-arm Λ, or a t2-vertex with β < j < α), and a t3-vertex in Q1.
- w's neighbours are T_int[1], t1[ℓ1−1], t2[ℓ2−1], t3[ℓ3−1], t2[jw±1] (index ≤ β), t1[c±1] ⊆ t1[8..14], v and f1.
- The only possible match is c1's t3-vertex = t3[ℓ3−1].

**The final clash.** t3V lies inside Q1 = [2,12], so 3 ≤ j3 ≤ ℓ3 − 1, and in R5, so j3 ∈ [P5−59, P5−51].
- **(20,13) and (21,12):** this forces j3 = ℓ3 − 1, a vertex of c1. Impossible.
- **(20,12) and (21,11):** this forces j3 = ℓ3 − 2, so v is joined to c1 through t3[ℓ3−1]. But #type II = 1, and the type-II label is c1 (X30 is of type I), so c1's arm vertex is Λ[λ−1], adjacent to b6. **(PC) fails.**

## 3. Case B2 (b3 ∈ Q2)

**The numbers.**
- Q1 = t3[10−x..20−x] is a pure t3-row containing t3V.
- ℓ3 ≤ 14 forces x ≥ 7.
- The grid on Q1 (the F1-cut inside must be 60, as ℓ2 + x ≥ 13) gives ℓ2 + x ∈ [19,21]. So ℓ2 ≥ 10, ℓ1 ∈ [16,18] and P4 ≥ 51.

**w's vertices.** w's G2-W's lie in Q0 and Q1 (W-rule). Hence w = {ℓ, b3, t2[jw], t1[c], t3[d]}, with:
- c ∈ [u+1, x−1] (its R1-vertex in Q0);
- d ∈ [11−x, ℓ2−6] (its R6-vertex in Q1).

**c7.**
- Its G2 are its t1-arm vertex (index ≤ u − 1, in Q0) and a t1-vertex of R1. That vertex lies in Q2, i.e. in t1[x+1..u+9], since t1[u+1..x−1] carry T_int and w.
- Its third G2 is a t3-vertex of Q1. That vertex lies in R5, since c7's cut 70 already covers R6, so its index is ≥ ℓ2 − 4.
- R2 contains no t1-vertex of c7, so c7's second G1 is a t2-vertex t2[j] with S_12 in R2 (j > α). Its arm P− and S_23 must then cover R3 and R4, which forces S_23 ∈ R4 (j < β).
- So α < j < β.

**(PC) at w fails: w is not joined to c7.**
- **T_int[1]:** c7 is an S-label.
- **t1[ℓ1−1]:** this has index ≥ u + 10 (P1 ≥ 21), beyond both t1-vertices of c7.
- **t2[ℓ2−1]:** here ℓ2 − 1 ≥ 9 ≥ β > j.
- **t3[ℓ3−1]:** its offset is ≥ 20 − x, so it is f2's cut vertex or lies in Q2, while c7's t3-vertex lies in Q1.
- **t2[jw±1]:** these have index ≤ α < j.
- **t1[c±1]:** these lie in t1[u..x], away from c7's t1-vertices.
- **t3[d±1]:** these have index ≤ ℓ2 − 5 < ℓ2 − 4.

So c7 is not adjacent to any vertex of w. **(PC) fails.**

## 4. Result

**WRITTEN:** In L1 type 12 with r2 = 3, c′ = 0 and one V on each of t1 and t3, the sub-case k = 1 is impossible. With v196–v198, (α3) is impossible.

v186 and v187 (c′ = 0 with both V's on one G2-thread) and v188–v195 (c′ = 1) then give **every L1 configuration of type 12 with r2 = 3 is impossible**. By the mirror (v160 §1), **every L1 configuration of type 2 with r2 = 3 is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2 (the remainder after v160 and v165);
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
