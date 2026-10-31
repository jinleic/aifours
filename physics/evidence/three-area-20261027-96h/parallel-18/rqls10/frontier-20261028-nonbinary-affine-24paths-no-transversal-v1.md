# Twenty-four nonbinary q18-containing affine paths have no transversal at any phase

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at complete independent replay: **Wed Oct 28 20:28:13 PDT 2026**. This strengthens the twelve literal paths in `frontier-20261028-nonbinary-affine-12paths-no-transversal-v1.md` SHA **7e866978d4414b661b00e6a4c514198e9cf4a0063bc9b5466bba995ab75ae072**. It does NOT cover full four-parameter tori, all BH(10,18), or general QLS10.

## 1. Claim

For EACH of the 24 literal cases in `frontier-20261028-q18-nonbinary-twentyfour-v1.json` SHA **776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2**, take the indicated literal sixth-root H, four rectangle masks and coefficients, and define

`K(z)=H ⊙ z^(sum_j coefficient_j M_j)`, `|z|=1`.

The independent program below checks every path is Hadamard for all unit z. **Claim:** all24 corresponding Fourier-product arrays have NO orthogonal transversal for ANY unit z and ANY physical K-row ordering, even allowing repeated rays. Row/column phases and column permutations are harmless. At z=zeta18 every case is an actual maximal 100-ray QLS10 and provably NOT binary-gaugeable, by independent original-vector/F3-certificate replay `frontier-20261028-q18-nonbinary-twentyfour-replay-v1.py` SHA **1ae8695da15fe9dc813539c9853f47bddcafe28cfaaff727ee69eb8088ec778b**; none is a 1-RQLS.

The proof for the 16 cases `0–3,12–23` is LITERAL and does not require catalog completeness: they have NO matching even at all72 exceptional phases. The other eight cases `4–11` may have half-matchings at some sixth-root endpoints; ruling out their transversals there imports `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de**, which in turn imports the published 34-class classification. All claims remain unreviewed.

## 2. Squarefree reciprocal-gcd correction

For each five-row subset E and column pair, form the Laurent half-orthogonality polynomial over Q(zeta6), remove powers of z, and call the nonzero result P. Any unit-circle zero is a common root of P and its reversed conjugate P*. The earlier first 24-path scan tested whether the ENTIRE gcd(P,P*) divides `z^72-1`, and conservatively left cases8–11 and20–23 unresolved when this failed. That test was unnecessarily strong: some gcds contain repeated roots already in mu72, whereas `z^72-1` is squarefree. No prior bytes are altered.

The corrected successor `frontier-20261028-nonbinary-affine-24paths-squarefree-v1.py` SHA **3d394fe4e7a01d3d7563b3b1b3697d49ed9f6f1759c8199d39558698259a7859** computes the squarefree part `G/gcd(G,G')` of each `G=gcd(P,P*)` and verifies it divides `z^72-1`. It also checks every generic identity-edge graph has no perfect matching. Thus any unit phase permitting a transversal must lie in mu72. On the66 phases outside mu6, every one of252 half graphs lacks a perfect matching for every case. At the six mu6 phases each K is BH(10,6); the cited q6 theorem excludes a transversal. For the16 cases in §1, direct endpoint scans in fact show no matching at all72 phases.

## 3. Independent exact replay

`frontier-20261028-nonbinary-affine-24paths-replay-v1.py`, SHA **0994d524b39be1f15764082a79cd4546c300e93bcaf50910a7e88f7b8098c53e**, independently reconstructs all24 literal paths, verifies their Hadamard Laurent coefficients, and checks

```text
272160 literal half-polynomials (24*252*45);
all squarefree reciprocal gcds divide z^72-1;
399168 non-mu6 endpoint half graphs (24*66*252), no perfect matching.
```

It uses Q(sqrt(-3)) rational-polynomial gcd arithmetic and the Q(zeta8,zeta9) tensor basis for endpoint sums, distinct from the producer's Q(zeta6)/Phi72 implementations. Its result SHA **99554b306a89d16ae89b4870fbff6133e8d3243c6dd0eed9167a7906fd6c3bc3** records the full24-path PASS. The 16-path literal all72 endpoint replay is `frontier-20261028-nonbinary-affine-16paths-replay-v1.py` SHA **eaf4daab381c2eb832b1bab98cdad03baaf113c4bd480d7a98427d6c6976f996**, result SHA **6a07716f27bce9a870fd1afe4203671df1fc5efdfc30c8fd19e7f932334c23e3**.

A perfect half-graph matching is a NECESSARY condition for any transversal because full column orthogonality and row-difference5 force both even- and odd-half sums to vanish. All252 E subsets account for every K-row ordering; row/column gauges and column permutations preserve zero sums.

## 4. Remaining boundary

The input contains24 particular one-parameter diagonal paths inside four-parameter affine families; it does not establish no-T on their other phase directions or any complete BH(10,18) classification. The root bounds, q6 endpoint import, finite-code completeness and symmetry caller require independent mathematical review. Arbitrary irrational phases in other families, nonproduct QLSs and the original maximal 1-RQLS10 target remain open; no witness or unrestricted no-go is claimed.
