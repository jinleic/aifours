# First-norm and squared-cost staircase selectors differ at every ε

Native clock observed before writing: **2026-10-28T18:02:55-0700 PDT**. The all-law first- and squared-L1 optimality statements below are conditional on the named prior per-cost staircase theorem. This is a same-harness written and exact-arithmetic disposition, not a source-paper refutation, complete mixed-norm optimization, human/cross-model review, formal proof or priority determination.

## Exact statement and source boundary

Let `ε>0`, `b=e^(−ε)`, `m=b/(1−b)`, and let feasible laws on `R²` satisfy additive ε-privacy for **every Borel event and every shift in the full closed** L1 unit ball. Let `Q_g` be the normalized centered L1-radial staircase with density proportional to `b^min{k≥0: ||x||₁≤g+k}`, `0≤g≤1`.

There are unique interior scalar selectors `γ₁,γ₂` for `E_Q ||X||₁` and `E_Q ||X||₁²`, respectively, and **`γ₁<γ₂` for every finite ε>0**. By §I of the earlier [MDA26 alternative per-cost theorem](../../three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md), `Q_γ₁` is an actual global all-Borel first-L1 minimizer and `Q_γ₂` is an actual global all-Borel squared-L1 minimizer. Moreover,

`E_Qγ₂ ||X||₁² < E_Qγ₁ ||X||₁²`,
`E_Qγ₂ ||X||₂² < E_Qγ₁ ||X||₂²`, and
`E_Qγ₁ ||X||₁ < E_Qγ₂ ||X||₁`.

Thus this **particular globally mean-L1-optimal law** is strictly suboptimal for the registered squared-Euclidean objective, with `Q_γ₂` an actual feasible comparator. This does not show that every mean-L1 optimizer is suboptimal, that `Q_γ₂` is the Euclidean optimizer, or that any optimizer is unique outside the scalar staircase family.

The parent read the cited publisher PDF [Kulesza–Suresh–Wang, PMLR 258 (2025)](https://proceedings.mlr.press/v258/kulesza25a.html), pp. 2–3 / extracted lines 59–111: its theoretical Definition 5 and Theorem 2 optimize **expected first-power K-norm**, while the paper also reports empirical comparisons under other metrics. This separation is **not** a counterexample to what that paper states. It rules out substituting its mean-optimal selector as a squared-Euclidean solution solely on the basis of that theorem.

## Parent reconstruction

For `0≤g≤1`, the L1 triangle inequality gives `|n_g(x+h)−n_g(x)|≤1` for every `x` and every `||h||₁≤1`. Therefore the density ratio obeys the privacy bound pointwise; translating and integrating pays every Borel event, including closed-ball boundary shifts. The normalized endpoint laws `Q_0` and `Q_1` agree almost everywhere.

Writing

`D=g²+2mg+m+2m²`,
`M₃=g³+3mg²+3(m+2m²)g+m+6m²+6m³`,
`M₄=g⁴+4mg³+6(m+2m²)g²+4(m+6m²+6m³)g+m+14m²+36m³+24m⁴`,

layer integration over L1 diamonds gives `L(g)=(2/3)M₃/D` and `W(g)=M₄/(2D)`. For these radial laws only, the angular integral gives `J(g)=(2/3)W(g)` for squared Euclidean cost. Both `r` and `r²` are nonnegative nondecreasing matching-norm costs, so the named per-cost theorem applies **separately**; it is not imported for Euclidean loss.

Set `v=m(1+m)`, `t=1+2m`, `x=g+m`. The derivative numerators are

`Q=g⁴+4mg³+6m²g²−2m(1+3m)g+m² = x⁴−2vtx+3v²`,

`P=g⁵+5mg⁴+(2m+12m²)g³+(12m³−2m)g²−m(1+2m)(1+6m)g+m²(1+2m)`,

with `L'=(2/3)Q/D²`, `W'=P/D²`. The negative Q value at `g₀=√v−m∈(0,1)`, positive endpoint values, and Descartes' two-sign-change bound show two simple positive Q roots in `(0,1)`; the second is the unique scalar minimum `γ₁`. Thus `z=(γ₁+m)²/v>1`.

Eliminating Q at that root gives the strictly negative identity

`P(γ₁)=−v³(z−1)³(z+3)/(4(γ₁+m))<0`.

P also has positive endpoint values and exactly two coefficient sign changes, even at the exceptional zero coefficient. Consequently its unique scalar minimum `γ₂` lies strictly to the right of `γ₁`; W decreases and L increases between them. The exact fixed-ε positive Euclidean gap and selector-distance bounds are specified in §5 of the [author candidate](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-universal-pmlr-selector-separation-v1.md). They use a valid bound on `|P'|` and an actual feasible comparison; no existence or radiality of a Euclidean minimizer is needed.

## Actual checks and limits

The parent read the complete 74-LF prior MDA26 parent theorem, the full 148-LF author candidate, and the complete [f64 review](../review-waves/f64-privacy-universal-selector-separation/review-v1.md). Review verdict: **0 FATAL / 0 MAJOR / 0 MINOR at the explicit per-cost import**. The reviewer independently rebuilt the geometric-moment/layer formulas and strict-root proof and ran 46 exact checks with six intended-reason controls; [checker](../review-waves/f64-privacy-universal-selector-separation/checker-v1.py), SHA-256 `9ad78623ce9d0b01e516b9a79c4f466700eae1a76ebba30d300032f9c7ae41c9`, [receipt](../review-waves/f64-privacy-universal-selector-separation/checker-receipt-v1.json), SHA-256 `fe837e04b152cdfeb2e3665b50e98a51a2f023edb8646bbbed0d9f362e1f86b1`. Its first checker invocation had a missing argument and did not create a receipt; the corrected invocation completed, as the review records.

Independently, the parent used standard-library rational polynomial dictionaries to derive both derivative numerators from the displayed moments, verify the shifted Q/R identities and strict-factor polynomial, and reject an altered identity. At `m=1`, exact rational evaluation gives `W(71/100)−W(18/25)=2962881/24812660000>0`. The parent's first isolated numeric diagnostic mistakenly typed the M₄ constant as 65 rather than 75 and printed a negative value; correcting that one diagnostic step yielded the fraction just stated. The all-variable polynomial identities had already passed using the correctly specified M₄ and were not rerun. The finite rational example is a control, not the proof for all ε.

The earlier MDA26 per-cost result is an imported written-supported alternative proof, not re-proved here or a blanket certification of the original printed proof. This disposition does not alter the earlier mixed-norm `LAW642` result or its qualifications. Worldwide priority and the full set of first-norm optimizers remain unassessed; the author's later all-law equality/uniqueness and asymptotic manuscripts are separate unreviewed candidates.
