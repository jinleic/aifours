# Theorem A (mod-3 constant-character / affine-rank theorem) — text v1

Author: ContinueCFR21 (Claude Code harness), lane info-2 CFR(6,21). Frozen 2026-10-18T23:55:44-0700.
Status: WORKER PROOF, not yet reviewed. Scope: a necessary condition only; it does NOT decide CFR(6,21).

## Setting
Let n be a positive integer with 3 | n and 9 ∤ n. Let D = (D_i(c)) be a (Z_n,k;1) difference matrix: rows i ∈ R
(|R| = k), columns c ∈ C (|C| = n), entries in Z_n, and for all i ≠ j the map c ↦ D_i(c) − D_j(c) is a bijection
C → Z_n. Put a_i(c) := D_i(c) mod 3 ∈ F_3. No normalisation of rows or columns is assumed.

A *translation-invariant character* is χ ∈ F_3^R with Σ_i χ_i = 0; its column function is χ(c) := Σ_i χ_i a_i(c).
Let K := {χ : Σχ_i = 0 and χ(c) is constant on C} (an F_3-subspace). The *mod-3 affine rank* is
r := (k − 1) − dim K. Equivalently, for any fixed row i_0, r + 1 = rank_F3 of the k × n matrix whose rows are
a_i − a_{i_0} (i ≠ i_0) and the all-ones row; r is the dimension of the affine span of the column points
(a_i(c))_i in F_3^R / F_3·(1,…,1).
Invariance: adding t_i to row i shifts χ(c) by Σχ_i t_i (constant); adding g_c to column c shifts χ(c) by
g_c Σχ_i = 0; permuting rows permutes coordinates; a unit u of Z_n multiplies every a_i by u mod 3 = ±1; permuting
columns is harmless. Hence K (up to the induced coordinate permutation) and r are equivalence invariants.

## Theorem A
If k ≥ 4, every nonzero χ ∈ K has support size ≥ 6.
**Corollary A1 (k = 7, e.g. CFR(6,21) ⇔ (Z_21,7;1)-DM).** dim K ≤ 1, i.e. r ∈ {5, 6}; and r = 5 iff
K = ⟨χ⟩ with χ, up to sign and row relabelling, one of e_1+…+e_6, e_a+e_b+e_c−e_d−e_e−e_f, e_a+…+e_e−e_f−e_g.
**Corollary A2.** k = 4, 5: r = k − 1 (full); k = 6: r ≥ 4.
Equivalent point form: if r is the affine rank, choose coordinates y_c ∈ F_3^r of the column points and dual points
λ_i with a_i(c) = ⟨λ_i, y_c⟩ + s_i. Then K ≅ {χ : Σχ_i = 0, Σχ_iλ_i = 0} (affine dependencies of the λ_i), and
Theorem A says the k points λ_i have no affine dependency with ≤ 5 nonzero coefficients: in particular they form a
cap (no three collinear: L3), contain no parallelogram λ_a+λ_b = λ_c+λ_d, and no relation λ_a+λ_b+λ_c+λ_d = λ_e.

## Proof
**Step 0 (balance).** For i ≠ j, D_i − D_j is a bijection C → Z_n and 3 | n, so a_i − a_j takes each value of F_3
exactly n/3 times ("balanced"). For t ∈ F_3^*, s ∈ F_3, t(a_i − a_j) + s is balanced as well.

**Step 1 (uniformity lemma).** Let f, g : C → F_3 be such that f, g, f+g, f−g are all balanced. Then for every
(u,v) ∈ F_3^2, N(u,v) := |{c : f(c)=u, g(c)=v}| = n/9. Proof: with ω = e^{2πi/3},
N(u,v) = (1/9) Σ_{(x,y)∈F_3^2} ω^{−xu−yv} Σ_c ω^{x f(c) + y g(c)}. For (x,y) ≠ (0,0) the function xf + yg is
one of ±f, ±g, ±(f+g), ±(f−g), hence balanced, and its exponential sum is (n/3)(1+ω+ω²) = 0. Only (0,0)
contributes, giving n/9. Since 9 ∤ n, **no such pair (f, g) exists.**

**Step 2 (support ≤ 5).** Let 0 ≠ χ ∈ K with constant value s. A vector of support m with all nonzero entries in
{1,2} and coordinate sum 0 has exactly μ entries equal to 2 where m + μ ≡ 0 (mod 3). Hence, up to sign:
* m = 1: impossible; m = 2: χ = e_a − e_b, but a_a − a_b is balanced, not constant (n/3 < n).
* m = 3: χ = e_a+e_b+e_c. Pick d ∉ {a,b,c} (k ≥ 4). f = a_b − a_a, g = a_d − a_a. Then f, g, f−g = a_b − a_d
  are balanced and f+g = a_a + a_b + a_d (since −2 ≡ 1) = (a_a+a_b+a_c) + (a_d − a_c) = s + (a_d − a_c) is
  balanced. Contradiction with Step 1. (This is Lemma L3.)
* m = 4: χ = e_a+e_b−e_c−e_d. f = a_a − a_c, g = a_b − a_c; f−g = a_a − a_b; f+g = a_a+a_b+a_c
  = (a_a+a_b−a_c−a_d) + (a_d − a_c) = s + (a_d − a_c). All balanced: contradiction.
* m = 5: χ = e_a+e_b+e_c+e_d−e_e. f = a_a − a_c, g = a_b − a_c; f−g = a_a − a_b;
  f+g = a_a+a_b+a_c = (a_a+a_b+a_c+a_d−a_e) + (a_e − a_d) = s + (a_e − a_d). Contradiction.
(For the negative of each shape the same pair (f, g) works with s replaced by −s.) ∎

**Step 3 (dimension, k = 7).** Suppose dim K ≥ 2 and take a 2-dimensional U ⊆ K. For each coordinate i the map
U → F_3, u ↦ u_i, is either 0 or onto; if onto, exactly 9 − 3 = 6 elements of U have u_i ≠ 0. So
Σ_{u∈U} wt(u) ≤ 6·7 = 42, while the 8 nonzero u have weight ≥ 6 by Theorem A: Σ ≥ 48. Contradiction; dim K ≤ 1
and r = 6 − dim K ≥ 5. Shapes of support 6 and 7 are listed by the same congruence (m = 6: μ ∈ {0,3,6}; m = 7:
μ ∈ {2,5}). For k = 6 the same count gives Σ ≤ 36 < 48, so dim K ≤ 1. ∎

## Machine checks (frozen stdlib probes; receipts under evidence/probes/)
* p4-mod3-rank-lemma-v1 (source e80ac121…, stdout 8722ac2d…, 42.2 s): over all 728 nonzero sum-zero χ ∈ F_3^7,
  every χ of support 3, 4, 5 (70 + 210 + 210) has a 2-dim plane spanned by roots whose 4 lines are ±roots mod ⟨χ⟩
  (the Step-2 witness); support 6/7 (154 + 42) have none; no 2-dim subspace of the sum-zero space has all nonzero
  vectors of support ≥ 6 (Step 3, exhaustive over 196 heavy vectors); for the five support-6/7 shapes there is no
  3-dim subspace W (W ∩ ⟨χ⟩ = 0) whose 13 lines are all root lines mod ⟨χ⟩ (so 3-dim uniformity cannot exclude
  r = 5); parent's cap lead: all 32,760 seven-point caps of AG(3,3) through the origin have affine rank 3 and
  determine exactly 12 of the 13 directions (independent confirmation of the parent's elementary lemma; that route
  excludes r ≤ 3 and is subsumed by Corollary A1).
* p5-theoremA-anchors-v1 (source 16b5638d…, stdout 068d3914…): all 96 pinned P21 (Z_21,6;1)-DMs have K = 0 (r = 5,
  full); the two pinned Z_27 six-row DMs (CFR(5,27) witnesses A/B, 9 | 27) also have K = 0 (no boundary violation
  observed there); Fourier control: no balanced pairs (f,g) with f±g balanced on 3 or 6 points (counts 0, 0); the
  coordinate pair on 9 points is a positive example.

## Scope and consequence
* Unrestricted necessary condition for CFR(6,21): the mod-3 image of every candidate has affine rank 5 or 6; rank 5
  only with one of the three listed support-6/7 relations. This excludes every construction in which some ≤ 5 rows
  satisfy a mod-3 affine relation (linear triples, parallelogram rows, 4-plus-1 relations), whatever the other rows.
* It does not exclude the generic stratum r = 6 (where all 96 known Z_21 DM6 live) and gives no nonexistence.
* Hypothesis 9 ∤ n is used only in Step 1; k ≥ 4 only for m = 3.
* Priority: L3 (m = 3) is the elementary mod-3 counting already in the old lane and is closely related to Evans
  (2013, Thm 4: the linear (p−2)-clique is maximal when the Sylow p-subgroup is cyclic, here p = 3). The m = 4, 5
  extensions and the rank corollary were not found in the sources read; no novelty claim before a primary screen.
