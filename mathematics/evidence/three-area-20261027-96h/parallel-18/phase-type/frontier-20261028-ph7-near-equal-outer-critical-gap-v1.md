# A uniform near-equal-outer exclusion neighborhood around z=8/9 for the 5/7 theta graph

**WRITTEN CANDIDATE, explicitly conditional on two separately unreviewed proofs; no global 8/9 decision.** MathResearch96h-2. This is a genuine extension from equal to SOME unequal outer rates, but it does not cover arbitrary unequal rates or other topologies.

## Claim

Normalize by `d=a-c` and positive Perron similarity so the spectral matrix is a seven-state row generator G. Consider the 5-/7-cycle theta graph with eight directed edges and arbitrary positive rates, whose two vertices outside the 5-cycle have diagonal escape rates `V1,V2`.

There exist **positive real constants** eta_z and eta_V such that NO such generator can contain `D_z(y)=y[(y+1)^2+z]^2` whenever

    |z-8/9|<eta_z,          |V1-V2|<eta_V.          (GAP)

In particular, if an 8/9 spectral witness exists on this theta graph, its two outer escape rates differ by at least a positive constant. The constants are existential; no numerical value or effective bound is claimed. Original PH realizations are included because Perron similarity preserves diagonal entries.

## Proof

Use as separate named dependencies:

1. The prospective global spectral compactness theorem `frontier-20261028-ph7-global-spectral-compactness-v1.md`, SHA256 `e1b9ec89f5e5f9770a2ca3b1b9ed88c3eb633102e0c94d125fc53de5d8c4b4db`, asserts compactness of ALL seven-state row generators with `D_z` dividing their characteristic polynomial and `z in [7/9,1]`. Its singular-resolvent limit proof remains independently unreviewed.
2. The exact critical equal-outer theorem `frontier-20261028-ph7-equal-outer-all-common-rates-critical-exclusion-v1.md`, SHA256 `4e3dc5292f40e0d16dba0f57a4b106956ce78ae35d1d3cdcfdb680376981f9f3`, excludes this full theta graph at8/9 when V1=V2, with arbitrary common rates. Its CAD and two-valued dependencies remain subject to the requested independent audit.
3. The SCC and >=8-edge proofs in `frontier-20261028-ph7-global-irreducibility-v1.md` and `frontier-20261028-ph7-minimum-eight-edges-v1.md` apply SPECTRALLY to any row generator with this repeated pair at z>1/2: it must be irreducible and has at least8 positive off-diagonal entries. The parent has reported independent written support for their PH application; the present spectral-only use is stated explicitly.

Fix labels for the theta edges `1->2->3->4->5`, `5->1`, and `5->6->7->1`. Let K be the subset of the compact spectral set over `[7/9,1]` where every off-diagonal edge outside these eight is zero. K is closed, hence compact. If K is empty, any sufficiently small positive constants satisfy(GAP).

Otherwise, every `(G,z)` in K has at most8 positive edges, and the spectral version of dependency3 requires at least8. Therefore every one of the eight allowed edges is strictly positive, and its graph is exactly the stated theta graph. Irreducibility and the positive Perron vector imply all seven diagonal escape rates are strictly positive.

Define the continuous nonnegative function on K

    f(G,z)=|z-8/9|+|(-G_66)-(-G_77)|.

If f were0, then z=8/9 and the two outer rates would agree. Dependency2 would exclude the resulting actual characteristic factor. Thus f is strictly positive everywhere on compact K and attains a positive minimum m. Set `eta_z=eta_V=m/3`. Any point satisfying(GAP) would have `f<2m/3`, contradiction. □

The proof uses compactness and a closed-support argument, not a local optimizer or a bounded numerical search. It handles simultaneous variation of ALL five common rates and all eight edge weights, and it does not assume their maximum or minimum values in advance. There is no hidden dismissal of a vanishing-edge boundary: at z>1/2 the separately supported irreducibility and edge lower bound rule it out.

## Limits and review needs

The global spectral compactness theorem and equal-outer critical exclusion are not yet independently accepted, so(GAP) is CONDITIONAL. A reviewer must verify their full dependencies and the spectral-only use of the >=8-edge conclusion. No explicit eta, all-unequal-rate exclusion, other-shape exclusion, 8/9 feasibility/exclusion, global maximum, minimum8, novelty or formal/kernel acceptance is claimed. Earlier holds and process findings are not altered.

END — an existential nonzero open neighborhood of the equal-outer slice is excluded around the critical ratio, conditional on the named proofs.
