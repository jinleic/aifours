# Dyadic population boxes exclude the consecutive cyclic spectrum

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:34:08 PDT 2026. This is an all-field, all-phase exclusion under the specified **cyclic-unitary** G6 hypotheses; it is not a general 1RQLS10 no-go.

## Result

The spectrum representative `(0,1,2,3,4,5)` cannot occur in a 45-distinct-ray cyclic-equivariant C6 lift of `Circ(15;±2,±5,±7)`. Conditional on the prior reductions, **nine** cyclic spectrum classes remain: seven with U^5 multiplicities `(3,2,1)` and two with `(2,2,2)`. Their list is `frontier-20261029-cyclic15-9-residual-spectra-v1.json` SHA-256 `0bd4271bc6a00005d826d7073b3f50307aacf9eaced6d5759c2a713ee2c81ffa`; no remaining case is claimed feasible.

## Exact branch and box argument

All three 2D U^5 groups for this spectrum are short ±3 pairs. By the row-imbalance theorem, in each group one v5 population is below `7/240` and the other is above `73/240`. Use the positive group-simplex substitution of `frontier-20261029-cyclic15-imbalance-16-no-go-v1.md` SHA-256 `ffb91f78c106751d67a6322bf568a9fc624356872ee1d6acf1beb4adaa7917d1`. There are eight possible low-index branches, using zero-based positions in the spectrum:

- Four branches `(0,1,2)`, `(0,1,5)`, `(0,4,5)`, `(3,4,5)` have a globally positive cross-plane determinant polynomial.
- Two branches `(3,1,2)` and `(3,4,2)` have two high-population rows congruent modulo 5, contradicting the row triangle/Cauchy inequality.
- The remaining branches `(0,4,2)` and `(3,1,5)` are each covered by 15 dyadic population boxes. Fourteen boxes have a strictly nonzero cross-plane determinant; the other has a positive-definite v7 self-plane compression, at theta 0 in the first branch and `13pi/15` in the second.

Each 15-box cover is seven half-cubes plus the eight quarter-cubes partitioning the remaining half-cube. The exact checker verifies coverage of all 64 quarter-grid cells, not merely a sample of points. The determinant and self-plane trace/determinant tests use the Cauchy–Binet polynomials from `frontier-20261029-cyclic15-crossplane-38-no-go-v1.md` SHA-256 `0a4bd44d9dca934397153be9547e029b6e171677f0690c9862e6262293d06bd8` and `frontier-20261029-cyclic15-selfplane-3-no-go-v1.md` SHA-256 `f4f22317a1d497473b7767ef84924da11fcd018e47fad8be084618cb21f37479`.

For every cross box all 27 degree-(2,2,2) coefficients are strictly positive. In each self box, all nonzero trace and determinant coefficients are strictly positive; moreover a specified positive monomial uses only local barycentric variables that are strictly positive whenever the original population variables lie in the allowed open simplex. This explicitly covers internal dyadic boundaries while respecting the strict global population bounds.

## Exact evidence and limits

`frontier-20261029-cyclic15-boxcover-proof-v1.py` SHA-256 `9dbf8140330c61a713887f7ae761102d0c395e45285855a8e6f3fc01f7639c4c` produces all branch, box, cofactor and coefficient data in `frontier-20261029-cyclic15-boxcover-proof-v1.json` SHA-256 `bd00a6b9ad1186b0379882847885b10eb1505b54660ee788fd102b35588a1218`.

The separate same-owner replay `frontier-20261029-cyclic15-boxcover-replay-v1.py` SHA-256 `8c2ac634ddba0780a08089b58111fd7b070b81d16492d8c3fe4a31edc2cf3cb` reconstructs the polynomials in a different cyclotomic basis, checks **1098** strict coefficient signs by rational intervals, verifies all eight branches, both 15-box covers and the boundary-positive monomials. Result `frontier-20261029-cyclic15-boxcover-replay-v1.json` SHA-256 `9f42348e94ff1590aaad932eabfb940d4ef79dd71b14a2904d8d1ab02790e70a` is **PASS** at 03:34:08 PDT.

The imported cyclic full-support and affine-quotient reductions, exact rational imbalance, box substitution, positivity and coverage still require independent mathematical review. The nine cyclic cases, all symmetry-breaking 6D complements, and the 25 omitted QLS cells remain open. No formal-kernel or novelty claim is made.
