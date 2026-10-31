# Erratum: exact node orders, scales, endpoints, and RI status in the W1 vertex table

Owner InfoSPR7-2, info-2. Native clock before writing: **Fri Oct 30 04:03:26 PDT 2026**. Additive erratum to `frontier-20261030-annihilator-w1-consolidated-vertex-table-v1.md` (51878833…); its bytes are unchanged. No probes run. The three all-positive vertices and the two partial dominations remain unreviewed and are not strengthened here.

## 1. Exact node orders (replacing the garbled §1 chain)

Gap placement: **0 < u₁ < a < u₂ < u₃ < b < u₄ < c < d < u₅ < e.**
Band placement: **0 < u₁ < a < u₂ < u₃ < b < c < u₄ < d < u₅ < e**, with the u₅-extension of §4 below.
Band markers: a ≤ b < c ≤ d < e ≤ f (envelope-root convention of the adopted chain; node inequalities below are all strict).

Justification of strictness (class regions + the adopted genericity perturbation, which moves all nodes off the fixed members' parity roots, so every required O-sign is nonzero): class 0 at u₁ gives u₁ < ρ₁⁽¹⁾ ≤ a; class 2 at u₂ with O(u₂)<0 gives u₂ > σ₁⁽²⁾ ≥ a; class 1 at u₃ with O(u₃)>0 gives u₃ < σ₁⁽³⁾ ≤ b; class 3 at u₄ gives b ≤ ρ₂⁽⁴⁾ < u₄ < σ₂⁽⁴⁾ ≤ d; class 5 at u₅ with O(u₅)>0 gives d ≤ ρ₃⁽⁵⁾ < u₅ < σ₃⁽⁵⁾ ≤ f. Distinctness of nodes is strict. Hence the a priori regions are u₄ ∈ (b,d) and u₅ ∈ (d,f); the delivered table's gap/band split of u₄ at c is exhaustive up to the boundary note in §3, and u₅ ∈ (d,e) is extended in §4.

## 2. Scales and envelope convention

For an independent box with positive leading interval [ℓ₇,u₇]: O₋(t) = ℓ₁−u₃t+ℓ₅t²−u₇t³ = λ₋(a−t)(d−t)(e−t) with **λ₋ = u₇**, and O₊(t) = u₁−ℓ₃t+u₅t²−ℓ₇t³ = λ₊(b−t)(c−t)(f−t) with **λ₊ = ℓ₇**; both > 0 and **λ₋ ≥ λ₊**, with equality iff the leading interval is degenerate. Monic boxes: λ₋ = λ₊ = 1. The band endpoints a,…,f are exactly the six envelope roots (open/closed per §1's marker convention; equalities a=b etc. occur only at degenerate odd intervals, in which case the strict class placements of the annihilator's required signs are already impossible — consistent with the adopted chain's degeneracy handling).

## 3. The u₄ = c boundary

At u₄ = c: for y = c vertices, E(u₄) = 0, so the actual term is exactly 0, which exceeds the continuous extension of the gap worst form (x−c)(z−c)(e−c)/(λ₊(f−c)D₄); for y = b the term is finite with worst endpoint O₋(c) < 0 as in the band form. Hence the gap-case worst-endpoint bounds, continuously extended, remain valid lower bounds at u₄ = c, and the two open placements (b,c), (c,d) plus this note cover u₄ ∈ (b,d) completely. No equality case needs separate hypotheses.

## 4. The u₅ ≥ e extension (small written lemma)

The a priori region is u₅ ∈ (d,f). If u₅ ≥ e then at BOTH z-vertices every T₅ term is nonnegative: for u₅ > e one has x,y,z ≤ e < u₅, so E(u₅) < 0 and F(u₅) = −u₅(b−u₅)(e−u₅) < 0, hence E·F > 0; the required sign is O(u₅) > 0 and H′(u₅) = +D₅ > 0, so T₅ > 0 strictly, with worst endpoint O₊(u₅) (finite). At u₅ = e, F(u₅) = 0 and the term is 0. Consequently the T₅ᵈ-negative case cannot occur for u₅ ≥ e, and every vertex bound proved or listed for u₅ ∈ (d,e) remains a valid lower bound (the u₅ ≥ e case is termwise easier). The table is therefore complete for u₅ ∈ (d,f).

## 5. RI status: sufficient subroutes, not necessary conditions

The RI-1…RI-5 inequalities and the listed partial/total-sum bounds are **sufficient** reduction routes obtained from particular ψ-matchings and term groupings of Lemma A's exact table. They are **not necessary** for full vertex-sum positivity: a full-sum S(x,y,z) > 0 may hold even when the corresponding RI or intermediate domination fails, since the matchings discard positive mass. The only claims that do not route through an RI are: the Lemma C dominations t₂ > |t₁| at gap (a,c,d) and gap (a,c,e) (proven outright by strict matching), and the three all-positive vertices (gap (0,b,e); band (0,b,e); band (0,c,e)) — and, from this erratum, every vertex with u₅ ≥ e reduces to the u₅ < e bounds with T₅ ≥ 0.
