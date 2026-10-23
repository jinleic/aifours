# ME3 dual charts — parent-desk derivation (ME3ParentDual, v1)

Scope: Lemma D and the six dual charts LW, LD1, LD2, G, SWB, SWC. Not covered here: primal chart P, Lemma M, the
reductions L1–L6, and the global assembly. Those belong to the parent's assembly and the other slices. Everything
below was re-derived from the theorem draft (§2) and charts-spec-v1.md. The worker code was not used, except the
leaf-line serialization and split order, which are labelled FORMAT DEPENDENCY in `code/dualcheck_v1.py`. The exact
identities cited as I1–I16 are checked with sympy in runs r02, r05 (`code/identities_v1.py`, `code/identities_v4_I15.py`).

## 1. Lemma D (checked)

Pole normal form: real pole 1 and pair 1 + ξ, 1 + ξ̄, with ξ = δ − iω, δ ≥ 0, ω > 0. Every f in the cone has the
form f = e^{−t}H, with H(t) = a + Re(c e^{−ξt}) ≥ 0. Then a ≥ 0:
* if δ > 0, because H(t) → a;
* if δ = 0, by averaging H over a period.

Fix T = 11/50, κ = 1/(1+T) = 50/61 and ρ = 1 − κ, and put q_θ(t) = (t−θ)² − ρθ².
* (I1) ∫₀^∞ q_θ e^{−zt} dt = θ³Q_T(θz), where Q_T(y) = (κy² − 2y + 2)/y³.
* Hence ∫q_θ f = θ³Q_T(θ)·[a + Re(cW)], with W := Q_T(θ(1+ξ))/Q_T(θ) and θ³Q_T(θ) > 0. Positivity holds because
  N(y) = κy² − 2y + 2 has discriminant 4 − 8κ < 0.
* Suppose W = Σλ_k e^{−ξt_k} with λ_k ≥ 0, Σλ_k ≤ 1 and t_k ≥ 0. Then a + Re(cW) = (1 − Σλ)a + Σλ_k H(t_k) ≥ 0.
  So R_θ(f) ≥ ρ for every θ > 0, and by (I14) min_θ R_θ = SCV/(1+SCV). This gives SCV ≥ T.
* T = 0.22 > U > v_cos, where U is the reductions' certified upper bound (arb check C_v_cos_upper_lt_T, r02).

Certificate forms. Each is an explicit finite combination, and W = 0 is admissible with λ = 0.
* RADIAL: W = |W|e^{iα} with α ≥ 0 and |W| ≤ e^{−δα/ω}. Take t = α/ω and λ = |W|e^{δα/ω} ≤ 1.
* SMALL: |W| ≤ e^{−2πδ/ω}. This is RADIAL with α = Arg₊W ∈ [0, 2π).
* TRIANGLE: W = a′ + b′V with V = e^{−ξθ′/ω} = e^{−rθ′}e^{iθ′}, a′, b′ ≥ 0, a′ + b′ ≤ 1 and θ′ > 0. Solving
  (I16) gives b′ = Im W·e^{rθ′}/sin θ′, a′ = Re W − Im W·cot θ′ and a′ + b′ = Re W + Im W(e^{rθ′} − cos θ′)/sin θ′.
  Validity does not depend on θ′; the checker picks θ′ ≈ θ₁(r) by a float heuristic, then rounds it to a rational.
* If g is a continuous logarithm of W along a path and Im g ≥ 0, then α = Im g is an argument of W. RADIAL then
  reads Φ := ω Re g + δ Im g ≤ 0.

## 2. Test-centre compactification

Put s = θ/(1+θ). The map s ↔ θ is a bijection (0, 1) ↔ (0, ∞).
* (I2) W = zz(w₁ + zz(w₂ + zz·w₃)), with zz = 1/(1+ξ), w₁ = κs²/N₁, w₂ = −2s(1−s)/N₁, w₃ = 2(1−s)²/N₁.
* (I2b) Equivalently W = q(s, 1+ξ)/(N₁(1+ξ)³), with q(s, z) = κs²z² − 2s(1−s)z + 2(1−s)².
* (I3) N₁ = (κ+4)s² − 6s + 2. Its discriminant is −156/61 < 0, so N₁ > 0 on ℝ.

Closed boxes may contain s ∈ {0, 1}. Those values are not test centres, but the ball enclosures still contain every
value for s ∈ (0, 1). Lemma D needs the representation only for s ∈ (0, 1).

## 3. Charts, physical subsets, and the inequalities replayed

"Physical" means: s ∈ (0, 1), δ ≥ 0, ω > 0, and in the chart coordinates below the corresponding open conditions.
Every replayed inequality is an enclosure over the whole closed (padded) box, so it holds in particular on the box's
physical subset. Each claim below is stated only for the physical points of the box.

* **LW.** ν = 1/ω ∈ (0, 1/640], δ ∈ [0, 64]; (I12) zz = ν/(ν(1+δ) − i). Test: |W|_box < exp(−2πδ_hν_h), and
  exp(−2πδ_hν_h) ≤ e^{−2πδ/ω} on the box. This is SMALL. The padding ν = 0 (ω = ∞) is not physical.
* **G.** Here s ∈ [0, 1], δ ∈ [0, 64], ω ∈ [1/5, 640]. The SKIP rule ω_h ≤ 40, ω_l ≥ 1/5, δ_h ≤ 3ω_l is checked
  exactly and implies box ⊂ P (P is closed). The tests:
  * SMALL: |W| < exp(−2πδ_h/ω_l).
  * RADIAL on a fixed branch. The branch region is certified on the box: Im W > 0 (α = Arg W), Im W < 0
    (α = Arg W + 2π) or Re W < 0 (α = π + atan(Im W/Re W)). On that region α is continuous and smooth, with
    values in [0, 2π). Test: F = ω log|W| + δα < 0, either naively or by MVF.
  * The MVF is F(mid) + Σ|∂_jF(box)|h_j, with gradients ∂_sF = ωRe L_s + δIm L_s, ∂_δF = ωRe L + α + δIm L and
    ∂_ωF = log|W| + ωIm L − δRe L. Here L = q_z/q − 3/z and L_s = q_s/q − N₁′/N₁ (I13). The midpoint is
    re-checked on the same branch.
  * TRIANGLE, as in §1, in balls.
* **LD1** (δ ≥ 64). Coordinates d = 1/(1+δ) ∈ (0, 1/65], β = atan(ω/(1+δ)) ∈ (0, π/2) and s ∈ [1/16, 1).
  * (I10) ζ := 1/(1+ξ) = d cos β e^{iβ} and δ/ω = (1−d)/tan β.
  * W = ζP, with P = w₁ + w₂ζ + w₃ζ², so arg W = β + arg P because d cos β > 0.
  * Padding that is not physical: d = 0, β = 0, β ∈ [π/2, 15708/10000] (15708/10000 > π/2 certified, r02), s = 1.
  * Tests:
    * fallback (β_l > 0, β_l < π/2 certified): |W| < exp(−(1−d_l)2π/tan β_l). This uses α = Arg₊W and
      δα/ω ≤ (1−d_l)·2π/tan β_l, since tan β ≥ tan β_l > 0 for physical β ∈ [β_l, π/2).
    * principal (β_l > 0): Re P > 0 on the box, α = β + atan(Im P/Re P) ≥ 0, and |W| < exp(−(1−d_l)α_h/tan β_l).
    * mvt0 (β_l = 0): Re P > 0 on the box and U := 1 + Im(P_β/P) ≥ 0, with P_β = (w₂ + 2w₃ζ)·i·d·e^{2iβ} (I10).
      Then |W| < exp(−(1−d_l)U_h). The argument: Arg P(0) = 0 because P(β = 0) > 0. By the mean value theorem in β
      at fixed (s, d) inside the box, α = β(1 + J(β*)) with J = ∂_β Arg P = Im(P_β/P). Since β/tan β ∈ (0, 1],
      0 ≤ α/tan β ≤ U_h.
* **LD2** (δ ≥ 64, s ≤ 1/16). Blow-up coordinates s = χρ_t and d cos β = (1−χ)ρ_t, with χ ∈ [0, 1],
  ρ_t ∈ (0, 81/1040] and 81/1040 = 1/16 + 1/65 (I11).
  * P = ρ_t²P̂ and W = (1−χ)ρ_t³e^{iβ}P̂ (I11). The same three tests apply to P̂, with ∂_βP̂ from I11.
  * The factor 1 − d is replaced by 1. This is conservative because every exponent is ≥ 0.
  * SKIP-s: χ_lρ_l > 1/16 exactly. Then s > 1/16 at every physical point, which lies in LD1.
  * SKIP-d: (1−χ_h)ρ_l > cos(β_l)/65, certified in balls. Then for physical β ∈ [β_l, π/2),
    d = (1−χ)ρ_t/cos β > cos β_l/(65 cos β) ≥ 1/65, so δ < 64 and the point is covered by the δ < 64 charts.
  * For a fixed physical pole (δ ≥ 64, ω > 0), the universal quantifier over s ∈ (0, 1) is split: (0, 1/16] by
    LD2 and [1/16, 1) by LD1. The union is (0, 1).
* **SWB** (δ ∈ [3/10, 64], ω ∈ (0, 1/5]).
  * On the real axis W > 0, so g = log W is real-analytic in δ.
  * (I9) g′ = q_z/q − 3/z, g″ = q_zz/q − (q_z/q)² + 3/z² and g‴ = −3(q_z/q)q_zz/q + 2(q_z/q)³ − 6/z³.
  * Taylor's theorem in y for h(y) = g(δ − iy), using the real and imaginary parts separately:
    Φ/ω = (g − δg′) + ω²(−g″/2 + δg‴/6) + E with |E| ≤ ω⁴(M₄/24 + δM₅/120), and
    Im g/ω = −g′ + ω²g‴/6 + R with |R| ≤ ω⁴M₅/120.
  * M_k bounds |g^{(k)}| on the rectangle [δ_l, δ_h] − i[0, ω_h] by the root form (I9),
    |g^{(k)}| ≤ (k−1)!(|v₁|^k + |v₂|^k + 3|z|^{−k}). Here v_{1,2} = κs/(κsz − (1−s)(1 ± i√(2κ−1))), and their
    denominators are bounded below in balls (nonzero, so W ≠ 0 there and g continues analytically along the
    vertical segment).
  * Tests: S + E < 0 and Im/ω − R > 0, naively or with MVF on the smooth part. Then Im g > 0 for ω > 0, so
    α = Im g, and Φ < 0. This is RADIAL.
* **SWC** (δ ∈ [0, 3/10], ω ∈ (0, 1/5]).
  * (I4) W = (1 − pξ)(1 − p̄ξ)/(1+ξ)³, with p = (s(1−s)(1+i√(2κ−1)) − κs²)/N₁.
  * (I5) |p|² = B = κs²/N₁ ≤ 100/39, because 100N₁ − 39κs² = 50(3s−2)².
  * Hence for |ξ| ≤ √(0.3² + 0.2²) < 0.361 < 39^{1/2}/10 the principal-log series gives a continuous logarithm
    g = Σ c_jξ^j, with g(0) = 0 and c_j = −2Re(p^j)/j + 3(−1)^j/j (I7).
  * (I6, I8) ξ^m = X_m − iωU_m and X_j − δU_j = −|ξ|²U_{j−1}. Hence Φ = −ω|ξ|²Σ_{j≥2}c_jU_{j−1} and
    Im g = −ωΣ_{j≥1}c_jU_j.
  * |U_m| ≤ m|ξ|^{m−1} follows from ξ^m − ξ̄^m = (ξ − ξ̄)Σξ^kξ̄^{m−1−k}, and |c_j| ≤ (2ρ^j + 3)/j.
  * Tails for N terms: 2ρ²(ρx)^{N−1}/(1−ρx) + 3x^{N−1}/(1−x) and 2ρ(ρx)^N/(1−ρx) + 3x^N/(1−x), with
    x = √(δ_h² + ω_h²) and ρ = √(B_up). They require ρx < 1 and x < 1, which is checked.
  * Tests: Ψ_N + tail < 0 and Ig_N − tail > 0, naively or with MVF on the polynomial part. Then Φ = ω|ξ|²Ψ < 0
    and Im g > 0, which is RADIAL.

## 4. Coverage of all far poles and all test centres

For δ ≥ 0, ω > 0 and every s ∈ (0, 1):
* δ ≥ 64: LD1 for s ≥ 1/16, LD2 for s ≤ 1/16. Every physical point of LD2's (χ, ρ_t, β) box lies either in
  δ ≥ 64 (certified) or in a SKIP box, and SKIP boxes contain only s > 1/16 or δ < 64.
* δ < 64 and ω ≥ 640: LW.
* δ < 64 and 1/5 ≤ ω ≤ 640: G, except G SKIP boxes, which lie in P (ω ∈ [1/5, 40], δ ≤ 3ω, the primal chart; not
  this desk).
* δ < 64 and ω < 1/5: SWC if δ ≤ 3/10, SWB if δ ≥ 3/10.

The checker verifies the stated chart ranges exactly from the spec breakpoints.

Tiling audit. Leaf boxes are rebuilt from (cell, path) with the deterministic split sequence; the sequence depends
only on depth, because widths halve. In file order, each cell's paths must:
* start at 0^k;
* follow the DFS successor rule, from q01^j to q10^i;
* end at 1^m.
By induction this makes the leaves exactly the leaves of a full binary tree: the covered set grows contiguously in
lexicographic order, with no gap and no overlap. Cells must appear as 0…n−1.

## 5. Limitations

* The same Arb library (python-flint 0.9.0) as the worker is used, so this is not an independent numerical kernel.
* FORMAT DEPENDENCY on the producer's leaf serialization and split order. The tiling audit itself is independent.
* Floats are used only to choose the TRIANGLE vertex angle and the control T′ (see records/float-audit-and-freeze-v2.json).
* SWC is replayed only against the forthcoming new worker run, as the parent instructed (worker float-rounding defect).
* P, Lemma M, the reductions and Δ₃/v_cos are not covered.
