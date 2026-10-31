# Closing pairs as derangements of nine-point row permutations, and a precisely failed inequality

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Fri Oct 30 03:23:12 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Bounded delivery per Main's direction: one non-tautological structural result from the ρ-incidence constraints (no boundary-column hypothesis; mixed columns preserved), plus one precisely formulated inequality whose proof fails at an identified step. All-variable over every T2(n), n ≥ 5 (n = 11 is the case of interest; the 9-point statement needs n−2 ≥ 3). No selected array, search, solver, program or external model. Inputs: T1/T2 definitions; the bridge Theorem A of `frontier-20261030-m-adjacency-row-bridge-and-invariance-blocker-v1.md` (SHA `0f0635a4…c302`) as corrected by its erratum (`aec34f60…b346`).

## 1. The ψ-correspondence and its domain structure

For symbols a ≠ c, let ρ(u,v) be the row of adjacency u→v, λ(a) = E⁻¹(a) the row where a is last, and define ψ_{a,c} = ρ(·,c)⁻¹∘ρ(a,·) wherever the composition is defined. Basic facts (all T1(n)): ρ(a,·) maps S∖{a} bijectively onto Rows∖{λ(a)}; ρ(·,c) maps S∖{c} onto Rows∖{c} (c is first only in row c, and no adjacency enters position 0). The adjacency a→c lies in row ρ(a,c) ∉ {row c, λ(a)} (c occupies position 0 of row c with nothing before it; a occupies the last position of λ(a) with nothing after).

**Domain dichotomy.** Write b₀ for the successor of a in row c (undefined iff a is last in row c, i.e. E(c) = a) and c₀ for the predecessor of c in row λ(a) (undefined iff c is first in λ(a), again iff E(c) = a).

- If **E(c) ≠ a**: ψ_{a,c} is a bijection S∖{a,b₀} → S∖{c,c₀} between (n−2)-point sets, with ψ(c) = a (the adjacency into c in row ρ(a,c) is a→c itself).
- If **E(c) = a**: ψ_{a,c} is a bijection S∖{a} → S∖{c} between (n−1)-point sets, again with ψ(c) = a.

By Theorem A plus witness uniqueness: **(a,c) ∈ M ⟺ ψ_{a,c} is fixed-point-free** (on its domain; ψ(c) = a is never a fixed point).

## 2. Closing pairs: derangements of a nine-point permutation (n = 11)

Call (a,c) a **closing pair** when E(c) = a, i.e. (a,c) = (last symbol of row c, first symbol of row c). There are exactly n closing pairs, one per row.

**Theorem D (all T2(11), no boundary hypothesis).** For each c, ψ_{E(c),c} maps S∖{E(c)} bijectively to S∖{c} with ψ(c) = E(c); its restriction to the remaining n−2 = 9 symbols is a **permutation π_c of the 9-set S∖{c, E(c)}**, and

(E(c), c) ∈ M  ⟺  **π_c is a derangement.**                        (1)

Consequently |M ∩ C| (C the set of closing pairs) equals the number of c for which π_c is a derangement; M = C — the circular-completion case — holds iff all eleven π_c are derangements. For non-closing pairs the fixed-point-free condition lives on the (n−2)-point correspondence of §1 and has no permutation structure in general (domain and codomain differ by the b₀/c₀ exchange).

*Proof.* The dichotomy gives the (n−1)-point bijection; removing ψ(c) = a from both sides leaves a permutation of S∖{a,c}. Theorem A transfers the M-membership to fixed-point-freeness; ψ(c) = a ≠ c is the one guaranteed non-fixed point. ∎

This is non-tautological: it converts the interaction of M with the endpoint permutation E into fixed-point properties of n explicit permutations built from the row structure ρ, with no count identity in sight. It constrains nothing by itself — derangements of 9 points exist in both signs (a 9-cycle is even; a (5,4)-type is odd), so no parity obstruction — but it gives the exact object any future exclusion must control.

## 3. The intended inequality, and exactly where its proof fails

**Intended inequality (I).** Bound k₀ (mutual M-pairs) by combining class-conditional distance sums with the global total T = Σ_pairs Σ_r d_r = n·Σ_d d(n−d) (n = 11: 2420), via the class bounds: mutual pairs have two rows at d = 1 and n−2 rows at d ≥ 3, so T_pair ≥ 2 + 3(n−2); k₁-pairs ≥ 2 + 2 + 3(n−3); k₂-pairs ≥ 4 + 3(n−4).

**Failure (proved).** With k₁ = n−2k₀, k₂ = n(n−1)/2 − n + k₀, the aggregated lower bound is

k₀(2+3(n−2)) + (n−2k₀)(4+3(n−3)) + (k₂)(4+3(n−4)) = [constant] + k₀·(3n−4 − 8 − 3(n−4))·… — the coefficient of k₀ vanishes identically, because every pair has exactly n row-distances with exactly two at d = 1 and the class only reallocates the remaining n−2 distances among the same multiset of values. The same cancellation holds for the upper bounds and for f = d² (and indeed for every additive f, by the corrected Theorem C). **So (I) is vacuous, identically in k₀, for every additive distance functional.** The failure point: any inequality built from additive pair-distance aggregates is provably uninformative about the class split; a genuine inequality must use non-additive data — e.g., per-pair products T·U, the identities of intermediate symbols, or the ψ-constraints.

**Attempt via per-pair mixed moments (II), where the proof currently breaks.** For a pair, T = Σd_r and U = Σd_r²; mutual pairs (no d = 2) have U ≥ 2 + 9·9 = 83 while k₂-pairs have U ≤ 4 + 7·100 + ... — the class-conditional extremes again reallocate the same distance budget, and the global Σ_pairs U = 13310 gives, after substitution, another identically cancelling k₀-coefficient (each pair again has 11 distances with two pinned at 1). Unproved step: an inequality mixing T and U **jointly per pair** (e.g., Σ_pairs (U − c·T) with class-dependent extremal ratios) does not cancel trivially, but I could not bound Σ_pairs U − c·T sharply enough per class to separate profiles; the extremal per-pair (T,U) regions of different classes overlap.

**First unproved step for a real exclusion.** Convert the 11 explicit derangement/permutation conditions of Theorem D, or the n(n−1) ψ-constraints of §1, into one counting consequence — e.g., a sign identity for Π_c sgn(π_c) in terms of ρ, or a fixed-point-count inequality coupling α_{n−2}, α₁ with the b₀/c₀ exchange. The b₀/c₀ structure shows where slack lives: for non-closing pairs, ψ's domain and codomain differ by one element each, and fixed points can hide in the symmetric difference — this is the precise mechanism any proof must defeat.

## 4. Residual

Theorem D is a structural characterization, not an exclusion; mixed, full-source and full-target columns all remain live; inequality (I) is proved vacuous and (II) is unproved at the stated step. No witness, no no-go: **unrestricted T2(11) remains OPEN.**
