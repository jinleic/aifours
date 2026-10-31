# At ε=ln 64, an actual full-diamond private law beats every centered diamond staircase

**Disposition: same-harness written support for the corrected composite.** In the registered two-dimensional additive pure-DP model—every Borel event, every shift in the **full closed unit ℓ₁ diamond** D, objective `J=E‖X‖₂²`—there is an explicit nonradial private law P_S with

`J(P_S)+10⁻⁶ < J(P_γ)` for every centered diamond staircase `P_γ`, `0≤γ≤1`, at **ε=ln 64**.

Thus none of that staircase family is an all-law J minimizer at this ε. This supplies an actual feasible competitor and an upper bound on the all-law infimum; it does **not** identify that infimum, its optimizer, an all-radial optimum, a novelty result or a contradiction to a theorem optimizing a different objective.

Native clock observed before composing: **2026-10-28T21:34:04-0700 PDT**, not an asserted file-creation time.

## Mandatory correction and exact construction

Read the complete [numeric correction](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/parent-required-numeric-correction-v1.json), SHA-256 `3b29787c171857d35099fded30bc7d1c2bd9b957537d64b54891209a8a1197bb`, **before** the affected [87-LF candidate](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-ln64-rational-nonradial-obstruction-v1.md), `028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01`. Its Eq.(10) as printed has a denominator **10⁶ too small**, so the displayed equality is false. Both reviewers classify this original defect as MAJOR. The correction preserves the numerator and supplies the correct denominator; this disposition adopts only that corrected composite. Frozen original bytes and the historical finding remain unchanged.

Set `b=1/64`, `m=b/(1−b)=1/63`, `a=3761763123/10¹⁰`, `z=3761763124/10¹⁰`, `η=1/100` and

`S=aD ∩ {‖x‖∞≤a−η}`, `n_S(x)=min{k≥0 integer:x∈S+kD}`.

Take density proportional to `b^{n_S(x)}`. For every x and every h∈D, the inclusions `(S+kD)+h⊆S+(k+1)D` and their reverse give `|n_S(x+h)−n_S(x)|≤1`. The density ratio is everywhere between b and 1/b; integration gives privacy for all Borel events, including closed-boundary shifts. The density is Borel and integrable because shell areas grow quadratically while their weights decay geometrically.

## Geometry, all layers and the strict comparison

Let p=|x₁|, q=|x₂| and c=a−η. Exact clipping toward x gives

`dist₁(x,S)=p+q−min(a,min(p,c)+min(q,c))`.

Since `2η<a`, this implies for **every** real k≥0, and hence every shell integer, `S+kD=(a+k)D∩{‖x‖∞≤a+k−η}`. The four removed axis caps have area η² each and squared-Euclidean moment `R²η²−(4/3)Rη³+(2/3)η⁴` at R=a+k. All signs and boundary points are included; no sampled support geometry is used as proof.

For `Pr(N=k)=(1−b)b^k`, write `M_j(g)=E(g+N)^j`. Abel summation includes every geometric layer exactly:

`Z_S=2M₂(a)−4η²`,

`J(P_S)=[(2/3)M₄(a)−4M₂(a)η²+(16/3)M₁(a)η³−(8/3)η⁴]/Z_S`.

The actual exact cost is

`4355768046089487574226880288026708390699272667 / 26721376640271909097532496900000000000000000000`.

For the uncut diamond staircase, `J(P_γ)=M₄(γ)/(3M₂(γ))`. Its derivative numerator is twice

`P_m(g)=g⁵+5mg⁴+(2m+12m²)g³+(12m³−2m)g²−m(1+2m)(1+6m)g+m²(1+2m)`.

At m=1/63 it has two Descartes sign changes. The exact signs `P_m(0)>0`, `P_m(a)<0<P_m(z)`, `P_m(1)>0` place its two simple positive roots in `(0,a)` and `(a,z)`. The larger root g_* is the local minimum. Equality of the endpoint laws `P₀=P₁` and strict increase after g_* show it is the global minimum on `[0,1]`. Positive-coefficient moment polynomials give

`min_γ J(P_γ)=J(P_{g_*}) > M₄(a)/(3M₂(z))`.

The corrected exact lower bound `M₄(a)/(3M₂(z))−J(P_S)` is

`55892104628095766169604064637687395172793197064705238995982813 / 28589579218686463271455054512504719394059809867200000000000000000000 > 10⁻⁶`.

This is a **lower bound** on the gap, not its unknown exact value. At equal ℓ₁ radius `r=a−η/2`, `(r,0)` has shell index one while `(r/2,r/2)` has index zero, so the constructed density really is nonradial.

## Independent checks and assurance boundary

- The complete [proof/geometry review](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/proof-review-v1.md), `e4a654dc75ff319c1d8e8f74ed59779db969525f1f07398c3214e562bc0fce5a`, reconstructs privacy, all-k geometry, cap integrals, infinite sums, scalar optimization and the corrected gap. Its [v2 control receipt](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/proof-controls-v2-receipt.json) reports 115 checks, zero failures. Its retained v1 had one reviewer hull-range defect, corrected additively in v2; it is not a candidate counterexample.
- The complete separate [arithmetic review](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/arithmetic-review-v1.md) independently derives the geometric moments, polynomial identity, root signs and exact comparison, conditional on geometry that the proof review separately discharges. Its [receipt](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/arithmetic-receipt-v1.json) preserves the original-denominator and coarse-bracket failure controls.
- Parent independently reconstructed the written argument and wrote/ran [a separate exact control](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/parent-geometric-staircase-check-v1.py), importing no author/reviewer code. It checked the derivative identity, root signs, actual cost and corrected bound; 320 rational geometry cases with constructed closest points; 1,280 full-closed-D shift checks; and nonradiality, η-hypothesis, outside-D and enclosure countercontrols. The [actual receipt](../review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/parent-geometric-staircase-result-v1.json), `903733d664a3bd8d4b8a86c089d9800d576023ff3bb4c03f40e9ddc14a8e1e71`, records PASS and observed finish 21:29:51 PDT. The checkpoint068 construction had not yet received that delivery; its pending-control wording is an observation-state record, not the actual completion time.

The theorem needs only the registered model, written elementary geometry/analysis and exact rational arithmetic. **No LAW642, v241, v253 or MDA26 theorem is a premise.** The optional claim about beating every ℓ₁-radial law is not admitted here: its additional MDA26 premise was outside both review packets and unread by those reviewers. Later finite-ε optimum/density and uniform-ε candidates remain separate unreviewed work. All evidence is same-harness, not human, independent-model-family, formal/kernel or novelty acceptance.
