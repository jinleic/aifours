# One-normal compound certificate: exact structural classes and a sufficient region

**Disposition: scoped same-harness written support adopted from f281 (0F/0M/0m).** Native clock before composition: 2026-10-29T21:00:58-0700 PDT. Parent read the complete 103-LF manuscript, 492-LF review and 22-LF named f274 import, with live bindings checked. Throughout A,B are traceless complex 4×4 matrices, A is normal, X=A⊗I+I⊗B, L=‖A‖_F²+‖B‖_F², and η is the f274 optimized entrywise-modulus radius of the additive second compound.

## Adopted scope

1. With A diagonal and a **single common** B-site unitary V, H=X†X splits into four PSD blocks Hᵢ=V(B+aᵢI)†(B+aᵢI)V†. The 120 pair coordinates split exactly as four sectors of dimension six and six of dimension sixteen. Their modulus radius is
   max{maxᵢ ρ(|K(Hᵢ)|), maxᵢ<ⱼ[ρ(|Hᵢ|)+ρ(|Hⱼ|)]}.
   Minimizing this A-diagonal expression supplies an **upper bound** on η; equality to the unrestricted η is not asserted in general.
2. If that common V makes every Hᵢ off-diagonal graph a linear forest, then **η=S₂(X)≤2L**. Per-block phase gauges/reorderings evaluate invariant radii only; they are not independently chosen physical site bases. This includes unitarily reducible B with blocks of size at most two without separate block-trace restrictions, and unitarily upper/lower-bidiagonal B, including irreducible nonnormal examples.
3. For every PSD 4×4 H, t=Tr H and h=‖H‖_F,
   ρ(|K(H)|)≤min{3t/2, 2h, t/2+√3√(h²−t²/4)}.
   The 3t/2 constant is sharp on uniform-modulus rank-one PSD matrices; zero/scalar cases are included.
4. Consequently, with tᵢ=‖B‖_F²+4|aᵢ|² and hᵢ=‖Hᵢ‖_F, the simultaneous inequalities maxᵢ min{3tᵢ/2,2hᵢ,tᵢ/2+√3√(hᵢ²−tᵢ²/4)}≤2L and maxᵢ<ⱼ(hᵢ+hⱼ)≤2L certify η≤2L in every common V. The source's trace expansion for hᵢ² is supported. These are sufficient, not necessary.
5. If all four eigenvalue moduli of A agree, these inequalities hold for **every** traceless B. If the four eigenvalues are distinct and L>0, η<2L. A strict relative-open neighborhood inside the normal simple-spectrum A stratum contains irreducible B that are not unitarily bidiagonalizable and have nonnormal squares. This escapes the two concrete B-classes; it is not a converse classification of the full common-Hᵢ-forest condition or an ambient-open assertion for arbitrary A.

## Parent reconstruction

On a cross sector the two Kronecker-sum off-diagonal terms occupy disjoint entries and PSD diagonals add without cancellation, so taking modulus gives |Hᵢ|⊗I+I⊗|Hⱼ| exactly. A path gauge and consecutive ordering make allowed two-particle moves noncrossing; the compound's wedge signs become positive. Thus the same/cross sector maxima exhaust all eigenvalue pairs and yield η=S₂ under the forest condition. Branching trees do not satisfy this argument.

For the centered PSD bound, use H=αI+C and the real-symmetric hard-core compression to obtain ρ(|K(H)|)≤2α+2‖H−αI‖_F. With d²=h²−t²/4, minimizing at α=t/4−d/(2√3) is allowed because PSD gives h≤t; the value is t/2+√3d. The rank-one decomposition and traceless zero-diagonal Rayleigh matrix give 3t/2 independently. Parent checked this optimization and its scalar/zero boundary in writing.

Equal moduli give tᵢ=L and hᵢ≤L. Distinct shifts B+aᵢI and B+aⱼI cannot both have rank at most one: their difference has rank four whereas a difference of rank-one matrices has rank at most two. Thus at most one hᵢ equals L, every cross sum is strict, and the same-block bound is at most 3L/2. This proves the strict claim without numerical sampling.

The supporting S₂≤2L statement for one normal factor is independently reconstructed in review §4.3: the two leading right singular vectors have a two-dimensional leg at the normal site; the compressed local operator has a positive product-Haar decomposition; rank-two trace Cauchy–Schwarz on the other site gives the half-Frobenius bound. No arbitrary-T 4×2 norm estimate or unlisted f168 proof is imported. This supports that inequality, not exactness of η for every one-normal pair.

## Residual and evidence

For general normal A outside the sufficient region and B outside the common-forest condition, control of the **one-common-V minimax** remains unpaid. A restricted A-diagonal failure cannot refute η because other A-site bases remain available. No global T2/T3/Z2, necessity, equality classification or novelty follows.

The source's auxiliary branching-tree, centering and non-necessity families are disclosed symbolic diagnostics, not physical counterexamples or premises of the main theorem. Review and parent used written derivations; no scientific executable or author code ran in this integration. All sources, coverage and live hashes are pinned in the companion receipt in the [f281 wave directory](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f281-werner-d4-one-normal-factor-compound-bridge/). Same-harness only: not human, independent-family, formal/kernel, provenance or novelty certification.
