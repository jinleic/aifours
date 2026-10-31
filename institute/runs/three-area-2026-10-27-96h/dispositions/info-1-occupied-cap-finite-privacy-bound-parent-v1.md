# Finite-privacy occupied-cap lower bound and budget constraints

**Disposition: ACCEPT as written mathematics at every finite ε.** Native clock observed before composing: **2026-10-28T20:07:55-0700 PDT**. Same-harness verification only; not a human, independent-model-family, formal/kernel, novelty or finite-ε optimality certification.

## Adopted statement

Fix ε>0, `b=e^(−ε)`, κ≥0 and the original all-Borel, all-event, full closed ℓ1-unit-diamond private noise class on ℝ². Let `φ(x)=|x|²+κ‖x‖₁`, `G(T)=∫(T−φ)₊`, `d=∫_D φ=2/3+4κ/3`, and let B be the unique positive root of

`(1−b)G(B)+2bB=b d`.

Then every feasible law satisfies `J+κL≥B`. The root satisfies `B<d/2<κ+1/2`, its sublevel set lies inside D, and B strictly exceeds the looser root of `G(B)+2bB=bd` obtained by capping the residual density by M everywhere. For κ=0,

`J≥(2b/3)/[b+√(b²+(π/3)b(1−b))]`,

tending to 1/3 as b→1 and to `(2/√(3π))√b` as b→0. The necessary budget conditions (8)–(11) of the candidate follow, including `b≤ℓ³F(r)/[1−9j+ℓ³F(r)]` for `r=j/ℓ<1/6, j<1/9` with `F(r)=27r(1−2r)²/4`, the L-only form `b≤ℓ³/(2−3ℓ+ℓ³)` for ℓ<2/3 and all r, and the J-only form `b≤3πj²/(4−12j+3πj²)`.

## Reconstructed argument

All-event privacy forces absolute continuity with density at most `1/(2b)`; the limsup representative obeys the shift inequality at every point and is bounded by the essential peak M. Near a peak, the density is at least `(1−η)bM` on a translated diamond E. The residual `g=p−ℓ1_E` has cap `M−ℓ1_E`, not merely M; the capped bathtub inequality plus the actual floor cost gives the exact signed identity `J+κL≥T−MG(T)+ℓ∫_E(φ−T)₊`. The translated positive-part integral is minimized at the origin by even convexity. At the root `G(T)=b d(T)` the M-dependence cancels; sublevel containment converts `d(B)=d−2B+G(B)` into the displayed equation. Budget bounds use monotonicity of `(1−b)G(T)+2bT` and the containment bound `G(H)≤2H³/(3κ²)`; the substitution `κ=2r/(1−6r)` gives exact rational identities `H/(1+2κ)=3j` and `H³/[κ²(1+2κ)]=ℓ³F(r)`.

## Evidence

- [Candidate, 100 LF](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-overlap-corrected-finite-dual-v1.md): `d57a58caedd6efd0751c5a4c6059c5c86db31446811e08bab317531da7d124f3`; parent read completely.
- [Frozen manifest](../review-waves/f118-privacy-occupied-cap-finite-dual/manifest-v1.json): `f650d734052325037c8a33f673a2adf6b35505976e168becf2d1ee679d6ac481`.
- [Independent review](../review-waves/f118-privacy-occupied-cap-finite-dual/review-v1.md): 0 FATAL / 0 MAJOR / 7 presentation MINORs; every step reconstructed, 44/44 exact and labelled-diagnostic controls, including negative wrong-cap, wrong-mass and failed-containment rectangle controls, exact ε-private staircase and Laplace positive controls. Its disclosed first-run tooling failure and size erratum are preserved, not edited.
- Parent spot-checked the κ=0 closed form against the quadratic (residuals ≤6e−17), its strict improvement over the looser root at four privacy levels, B<1/3, and the exact rational κ-substitution identities and sample values `F(1/24)=121/512, F(1/12)=25/64, F(1/9)=49/108`.

## Boundaries

The MINORs are adopted as qualifications: ℓ denotes a floor level in §2 and the L budget in §4; `d(T)` is nonincreasing; the containment remark at H is unused; the comparison with the earlier file is against the reconstructed looser root, not that file's bytes. No finite-ε optimality, exact optimizer, uniform-in-κ sharpness, novelty or source-selector claim follows. Later multilayer, exact-1D-marginal and ε=ln2 certificate candidates are separate and unadopted.
