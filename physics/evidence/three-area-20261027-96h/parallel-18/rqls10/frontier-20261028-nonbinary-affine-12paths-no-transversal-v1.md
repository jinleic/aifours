# Twelve nonbinary q18-containing affine paths have no transversal at any phase

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay: **Wed Oct 28 20:22:58 PDT 2026**. This extends the single explicit path in `frontier-20261028-nonbinary-affine-allphase-no-transversal-v1.md` SHA **ab75f4c8d49bf11ef170d57d01f8499a8a36f95e701d6502980635cfd2f9e52e** to twelve LITERAL paths. It does NOT claim all24 paths, full four-parameter tori, all BH(10,18), or general QLS10.

## 1. Exact finite scope

Take cases `0,1,2,3,12,13,14,15,16,17,18,19` from `frontier-20261028-q18-nonbinary-twentyfour-v1.json`, SHA **776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2**. For each case, its literal source H and four listed rectangle masks/coefficient vector define

`K(z)=H ⊙ z^(sum_j coefficient_j M_j)`, `|z|=1`.

The independent program below verifies that ALL row-pair Laurent coefficients vanish, hence each K(z) is Hadamard for every unit z. **Claim:** for each of these twelve paths, the actual Fourier-product array has NO orthogonal transversal for ANY unit z, ANY physical K-row ordering, and arbitrary row/column phases and column permutations. Repeated rays are allowed.

At z=zeta18 each listed K is nonbinary-gaugeable mod3 and yields an actual 100-distinct-ray QLS10, with original vectors and nonbinary certificates independently replayed by `frontier-20261028-q18-nonbinary-twentyfour-replay-v1.py` SHA **1ae8695da15fe9dc813539c9853f47bddcafe28cfaaff727ee69eb8088ec778b**. They are NOT 1-resolvable. No claim is made that the twelve are mutually inequivalent.

## 2. Exhaustive continuous-parameter proof

The exact first scan `frontier-20261028-nonbinary-affine-24paths-v1.py`, SHA **65600b8347722b9f9f59b233c164b60bb1cf2fca19e0c6d02144db244ca86a7f**, considers all24 literal paths and identifies the twelve stated paths as satisfying both:

- for each of252 source-row halves E, the graph of identically-zero half-polynomials has no perfect matching;
- after removing irrelevant powers of z, every nonzero half-polynomial P has `gcd(P,P*)` dividing `z^72-1`, and at EACH of the72 roots, all252 half graphs have no perfect matching.

Here `P*` is the reversed coefficientwise conjugate. Any unit root of P is a common root of P and P*, so a putative transversal at nonexceptional z would require a perfect matching entirely from identity edges, while a transversal at exceptional z would require one of the scanned endpoint matchings. Both are impossible. This is the SAME halfgraph necessary condition as in the single-path packet, with no maximal-ray premise.

Independent `frontier-20261028-nonbinary-affine-12paths-replay-v1.py`, SHA **c9280b77e204ea08a1a651bc6d494c12e825ad1a851e4d8ffb8b4115c4d04154**, reconstructs each literal H, masks and all its half-polynomials, verifies the Hadamard Laurent coefficients, and recomputes reciprocal gcd divisibility using Q(sqrt(-3)) rather than the producer's Q(zeta6) representation. It independently rechecks all exceptional endpoints using the 24-dimensional Q(zeta8,zeta9) product basis instead of Phi72. The result JSON SHA **0ae060e66e0bcb941939e3d4fbddf4bc6e222a6383bf9993b73d45d0c072cb3f** reports

```text
12 paths; 136080 literal half-polynomials;
217728 exceptional-phase half graphs; zero perfect matchings.
```

This finite proof uses the literal input matrices, NOT the prior 34-class catalog completeness. Physical K-row permutations simply select a different E, all252 of which are covered. Column permutations and row/column phase gauges preserve the matching condition.

## 3. Explicitly unresolved paths and general gap

Four other paths, cases4–7, have reciprocal-gcd order bound72 but half matchings at some sixth-root endpoints; the prior all-BH6 theorem would exclude actual transversals there conditionally on its classification, but that conditional inference is NOT included in the twelve-path count. The remaining eight paths, cases8–11 and20–23, have some reciprocal gcds not dividing z^72-1; these are conservatively UNRESOLVED, not claimed to possess unit roots or transversals.

The full four-parameter tori, other q18/non-Butson Hadamards, nonproduct QLSs and the original 1-RQLS10 remain open. Independent code/math review and novelty screening are required before adoption; no general no-go or target witness is claimed.
