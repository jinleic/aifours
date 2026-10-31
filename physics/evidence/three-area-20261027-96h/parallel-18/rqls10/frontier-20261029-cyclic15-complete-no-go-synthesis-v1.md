# No unitary-cyclic 6D complement for the 600-cell parity core

**SYNTHESIS OF WRITTEN + EXACT-CERTIFICATE AUTHOR CANDIDATES, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 04:17:50 PDT 2026. This collects a conditional exhaustive reduction; every component still requires independent mathematical and certificate review. It is **not** a general 1RQLS10 no-go.

## Theorem candidate

Let `G6=Circ(15;±2,±5,±7)`, the 6D complement of the context graph of the exact 600-cell 4D parity core `frontier-20261029-600cell-circulant4d-core-v1.md` SHA-256 `c9370b9c56c57c0ef93ea501cccb0c8fbc34f287e6c418a1a4486bc384498ec1`. There is **no** assignment of 45 distinct rays of C6 to the edges of G6 such that

1. the six rays at every vertex form an orthonormal basis, and
2. some unitary U on C6 sends the ray of every edge `{i,j}` to the ray of `{i+1,j+1}`.

No assumptions are made on vector phases, spectral populations or number fields. The 4D core does carry an explicit real orthogonal T of projective order 15 implementing the same translation (`frontier-20261029-600cell-core-cyclic-unitary-v1.md` SHA-256 `41b1c37bc467a64d08ed17210776b4e15bd686e8f10aa606cb4f2e7d71a993e9`). The theorem therefore says this physical cyclic symmetry cannot be extended to a 6D sector completing a 4+6 balanced-quotient parity core with a unitary cyclic action on that sector. A symmetry-breaking 6D complement is not excluded.

## Reduction chain

| Step | Exclusion / reduction | Packet SHA-256 |
|---|---|---|
| Irreducibility, U^15 scalar, projective order 15 | §1 of `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md` | `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada` |
| U^5 multiplicities `(4,1,1)` impossible | `frontier-20261029-cyclic15-unrestricted-multiplicity-v1.md` | `128c8d68c92ef4db22169b0376e7a97758efa4ef18cdb086ecf4914de5482de7` |
| Short-pair row imbalance | `frontier-20261029-cyclic15-row-imbalance-v1.md` | `5fd6191eb69c5720eaf5a272b98693249578a41cab90571ec7b73260e09aef04` |
| Triangle rays span ≥4 | `frontier-20261029-cyclic15-triangle-span-obstruction-v1.md` | `4dafd1cda09d2e35fd96daa8f66c71136dc278c0f37b31cd5301574ab7d3d853` |
| Rank-4 degeneracy; v5 needs ≥5 spectral values | `frontier-20261029-cyclic15-rank4-triangle-degeneracy-v1.md` | `3ced4cb0b85bfacba7f00e5a160753326877e11c19352617d3c60ba81030b9f9` |
| Exactly five values impossible: simple spectrum, full support | `frontier-20261029-cyclic15-no-five-spectral-support-v1.md` | `595b702ae059ef2d94e7f98cf3d111ede1dd134f39a6daced541cd4cc50d75cc` |
| Affine/graph-multiplier quotient: 80 classes | `frontier-20261029-cyclic15-78-residual-spectra-v1.md` | `d709af376455f106e4312f56a29b54b1a6d15ccf025aa85d01f76f337de692b2` |
| Two complete-coset classes (2) | `frontier-20261029-cyclic15-two-coset-determinant-no-go-v1.md` | `b03725b2d3e562ebe70fd2e3e40ef71e167a960a5a3ba866c462ca1bf6fa8463` |
| Two-plane normal form | `frontier-20261029-cyclic15-two-plane-normal-form-v1.md` | `b2b0ca5e4d1242c9849bc7d77b4f8183e59a6f3bdef62e8606989b617a8849e7` |
| Cross determinant positivity (38) | `frontier-20261029-cyclic15-crossplane-38-no-go-v1.md` | `0a4bd44d9dca934397153be9547e029b6e171677f0690c9862e6262293d06bd8` |
| Semicircle spectra (8) | `frontier-20261029-cyclic15-semicircle-8-no-go-v1.md` | `2850d6b2f80e5fa83ae93001e59d9dc6383bb4111be2eeab7f12b3f41e617007` |
| Positive self-plane (3) | `frontier-20261029-cyclic15-selfplane-3-no-go-v1.md` | `f4f22317a1d497473b7767ef84924da11fcd018e47fad8be084618cb21f37479` |
| Imbalance + determinant (16) | `frontier-20261029-cyclic15-imbalance-16-no-go-v1.md` | `ffb91f78c106751d67a6322bf568a9fc624356872ee1d6acf1beb4adaa7917d1` |
| Mixed branches (3) | `frontier-20261029-cyclic15-mixed-branch-3-no-go-v1.md` | `8950c44aff52433f3ab8e4a1c50d49936fccbff8baf1450abfa367f32888575f` |
| Dyadic boxes (1) | `frontier-20261029-cyclic15-boxcover-one-no-go-v1.md`, with hash erratum `frontier-20261029-cyclic15-boxcover-one-erratum-1.md` | `03e8a0cc65ccae8ce13880199690e02a147a45e2faa08c365f49b01a4495937e`; erratum `8e20312760e96347829fcd17225bb62672c98b5f5dcee7f2423ebd2b3e896fb6` |
| Rank-one kernel boxes (2) | `frontier-20261029-cyclic15-rank1-boxcover-2-no-go-v1.md` | `e37ca94bd18d976712df86f7256e2c03da2a4a15462fc7c8acb095ed88076d74` |
| Barycentric simplex covers (7) | `frontier-20261029-cyclic15-simplex-cover-7-no-go-v1.md` | `240d81666275e85ef5964a89e1e6dbb097435f73a6e93afe594a1eb03e8cbf44` |

The exclusion counts are 2+38+8+3+16+3+1+2+7=80, exhausting the 80 affine spectral classes. In more detail: the full-support theorem leaves only six distinct U eigenvalues. Of the 5005 six-element exponent sets, 630 omit a U^5 class and 375 have the excluded multiplicities, leaving 4000 sets in the 80 classes.

## Verification boundary

- **Written mathematics** supplies the irreducibility caller, eigenvalue normalization, multiplicity/row inequalities, rank-4 counting, two-coset determinant contradiction, two-plane normal form, determinant/rank-one/self-compatibility tests, row-collision tests, branch substitutions and all positivity implications.
- **Exact computation** supplies the nonzero-resultant and positive-coefficient certificates. Each certificate family has a separate same-owner replay in an independent exact basis, reported in its packet. Floating-point calculations only chose candidate branches and regions.
- **Not performed:** independent human/model review, formal-kernel verification, and novelty clearance. A separate earlier Z3 attempt for an unrelated Q(sqrt(5)) population census failed and remains recorded as failed in `frontier-20261029-cyclic15-qroot5-smt-failure-record-v1.json`. It is not used in this chain.

## Remaining open problems

The theorem says nothing about G6 realizations without the cyclic unitary, other 4D parity cores or tripartitions, irreducible 10D parity cores, or a full 1RQLS10 with its remaining 25 cells. The earlier Pauli-core exclusions are different, fixed-configuration statements. The question whether a maximal 1-RQLS of order 10 exists therefore remains open in this work.
