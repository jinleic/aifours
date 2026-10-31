# A six-variable gluing inequality outside the Shannon cone

**Disposition: ACCEPT as written mathematics with an exactly checked finite separator.** Native clock observed before composing: **2026-10-28T20:07:55-0700 PDT**. Same-harness review only; no human, independent-model-family, formal/kernel certification. **Novelty is not established**: the inequality may be known or derivable from known non-Shannon inequalities, and nothing here improves the original guessing-number bounds.

## Adopted statement

For arbitrary finite random variables `B,C,R,H,P,Q`,

`Φ=−H(BC)−H(BR)+2H(BCRH)+H(BCP)+H(BRP)−H(BCRP)−H(BHP)+H(BCHP)−H(BCRHP)−H(BQ)+H(BCQ)+H(BRQ)+H(BHQ)−H(CHQ)+H(CRHQ)−2H(BCRHQ)≥0.`

The inequality also holds on the almost-entropic closure, and conditioning on any further finite vector Z gives the same sixteen-term pattern with Z adjoined. The explicit 64-coordinate rational vector `r/6,900,000` in the witness is a six-variable polymatroid with `Φ(r)=−12637/1,725,000<0`. Hence `Φ≥0` is valid for all entropy vectors but is not a nonnegative combination of six-variable elemental Shannon inequalities, and that witness lies outside the almost-entropic closure.

## Reconstructed proof

The formal identity

`Φ=I(B;R|CHPQ)+I(C;R|BPQ)+I(C;Q|BHP)+I(R;P|CHQ)+I(H;P|BQ)+I(H;Q|BCRP)+I(P;Q|BR)+I(P;Q|BC)−2I(P;Q|BCRH)`

holds on every set function: expanding all nine conditional mutual informations, the nine mixed P-and-Q coordinates cancel exactly and the remaining coefficients are the sixteen written terms. The written expression contains no term with both P and Q. For any law, replace the conditional joint law of (P,Q) given `Y=(B,C,R,H)` by the product of its conditional marginals. This keeps every (Y,P) and (Y,Q) marginal, so Φ is unchanged, while the glued law has `I(P;Q|Y)=0`. Applying the identity to the glued law expresses the unchanged value of Φ as eight nonnegative conditional mutual informations of that glued law. The half-space `Φ≥0` is closed, so the almost-entropic closure satisfies it. Conditioning on Z averages the inequality over the conditional laws, and zero coefficient sum turns conditional entropies into joint entropies with Z.

For the separator, the exactly verified polymatroid axioms and the Farkas characterization of the Shannon cone give the stated non-Shannon classification; it is a cone-separation statement, not a priority statement.

## Evidence

- [Candidate inequality and proof, 62 LF](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-six-variable-gluing-inequality-v1.md): `f5c83b572ecc2ec25a62b22e24e405a897b37152385a11a1e31f37f567a07075`. [Exact witness](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-six-variable-nonshannon-witness-v1.json): `10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169`.
- [Frozen manifest](../review-waves/f122-six-variable-gluing-nonshannon/manifest-v1.json): `b8bdc86c7281c3c8e1d0c6a2abdc980848e620650a8df95906cae854a6524907`.
- [Proof review, 137 LF](../review-waves/f122-six-variable-gluing-nonshannon/proof-review-v1.md): `1add2540068d271d469978952ca2689c9283c5478f00fd76f4a9cbaa2bcedd88`; 0 FATAL / 0 MAJOR / 3 MINOR (wording of glued-law CMIs, unverified provenance paragraph, author checker not tying the displayed table). It hand-expanded all nine terms over 64 coordinates, verified polymatroid axioms directly, and ran exact finite-law gluing examples, nine identity mutations, witness perturbations and a false-coefficient negative control. Parent rehashed this file after a sibling reviewer's disclosed scratch collision; the bytes are unchanged.
- [Finite replay, independently structured](../review-waves/f122-six-variable-gluing-nonshannon/finite-review-v1.md): `d3b8e929f243a7e773c5c7bf7bc3364ee1c4e9252c3d3ede5b8038f4995d3607`; PASS with 246 elemental, 729 monotonicity and 4,096 submodularity checks, exact value `−50548/6,900,000`, fifteen intended-reason rejections, two positive polymatroids and an exact finite-law gluing control.
- Parent read all three frozen inputs and both reviews completely and verified the mixed-term cancellation argument by hand on the row table; no author code was executed.

## Boundaries

The twelve-variable provenance, the 45,360 substitution LP statements, any fixed star-profile exclusion, the five-variable successor and any claim about the original R-minus profile are not adopted here. The f110 specified three-branch LP optimum and its author citation erratum remain a separate disposition. No entropic realization of any LP point and no guessing-number improvement follows.
