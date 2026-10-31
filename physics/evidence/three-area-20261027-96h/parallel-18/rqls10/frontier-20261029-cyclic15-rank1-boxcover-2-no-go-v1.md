# A rank-one cross-kernel test excludes two more cyclic spectra

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:45:46 PDT 2026. This continues the all-field, all-phase reduction of the **cyclic-unitary** 6D complement problem for `G6=Circ(15;±2,±5,±7)`. It is not a general G6 or 1RQLS10 no-go.

## Result

The spectrum representatives `(0,1,2,4,5,9)` and `(0,1,2,4,6,11)` cannot occur. Conditional on the prior reductions, **seven** cyclic spectral classes remain, all with U^5 multiplicities `(3,2,1)` and no short ±3 pair:

`(0,1,2,3,6,8)`, `(0,1,2,3,6,10)`, `(0,1,2,4,6,7)`, `(0,1,2,4,6,10)`, `(0,1,2,4,6,13)`, `(0,1,2,5,7,8)`, `(0,1,2,5,7,11)`.

The manifest is `frontier-20261029-cyclic15-7-residual-spectra-v1.json` SHA-256 `176b424095a49fea70959cb313d85a5c4fd46ec693d5bfc1a0dbe10ce3a8c49a`. None is claimed feasible.

## New necessary test: a rank-one kernel

Use the two-plane normal form `frontier-20261029-cyclic15-two-plane-normal-form-v1.md` SHA-256 `b2b0ca5e4d1242c9849bc7d77b4f8183e59a6f3bdef62e8606989b617a8849e7`. Cross-orthogonality requires a nonzero rank-one 2×2 matrix `X=conjugate(z)w^T` orthogonal, in the bilinear pairing, to the three matrices `C_0,C_(-7),C_2`.

If these three vectorized matrices are linearly independent, their orthogonal complement in C^4 is one-dimensional, spanned by the cofactor vector h of their 3×4 matrix. X must then be a nonzero multiple of h, so `det(h as 2×2)=h0h3-h1h2` must vanish. If they are dependent, h=0 and the determinant also vanishes. Thus **a nonzero value of h0h3-h1h2 excludes every cross-orthogonal pair**, regardless of the fourth matrix, self-orthogonality or vector norms.

Cauchy–Binet gives exact coefficients: with V3 the three exponent rows `0,-7,2`, and `R[j,(a,b)]=conjugate(N_L[j,a])N_M[j,b]`,

`(product_j p_j) h_col = (-1)^col sum_(|I|=3) det(V3[:,I]) det(R[I,cols≠col]) product_(j∉I) p_j`.

Multiplying the rank-one determinant by `(product p)^2` produces a polynomial with coefficients in Q(zeta_15). For a fixed rational angle theta, strict positivity of `Re(e^(-i theta) * conjugate(ref) * F)`, with `ref` a fixed nonzero coefficient, proves F≠0.

## Complete branch and box certificates

As in `frontier-20261029-cyclic15-mixed-branch-3-no-go-v1.md` SHA-256 `8950c44aff52433f3ab8e4a1c50d49936fccbff8baf1450abfa367f32888575f`, every short ±3 pair forces one population below `7/240` and its partner above `73/240`. The certificate covers every branch:

- `(0,1,2,4,5,9)`: low-index branches `(1,2)` and `(3,4)` have globally signed cross-plane determinants; `(3,2)` has a positive v7 self-plane compression at theta 0; `(1,4)` is covered by five exact dyadic boxes, using cross-plane determinant and rank-one tests.
- `(0,1,2,4,6,11)`: low branch `(3)` has a positive v7 self-plane; low branch `(1)` is covered by 35 exact dyadic boxes, using determinant, rank-one and self-plane tests.

Every box polynomial is expanded in local barycentric variables. All nonzero coefficients are strictly positive. For every allowed face of each box that is not on the excluded boundary of the original open population simplex, some positive monomial survives, so positivity is strict even on internal box boundaries. The replay checks the total box volume is 1 and all pairs have disjoint interiors, hence each branch box list tiles its whole cube.

## Exact evidence and boundary

`frontier-20261029-cyclic15-rank1-boxcover-proof-v1.py` SHA-256 `d138b6ebaf5488eeb744bf88c5334a57dcca6ebbb9cb56070855cd931fdec1d8` produces all branch and box data in `frontier-20261029-cyclic15-rank1-boxcover-proof-v1.json` SHA-256 `0e83703505311c6d71ff7e05684b261c2e055cc99184edec9f251ad271d9bd20`. The discovery-only numerical box plan `frontier-20261029-rank1-cover-plan-v1.json` SHA-256 `46d403ced777b29484dcc6495d287001214c1c34290daf3aa4bd6abd05a81b71` is not part of the proof.

The separate same-owner replay `frontier-20261029-cyclic15-rank1-boxcover-replay-v1.py` SHA-256 `aeb37c4798e1c10cf8acd0f303d11c0bb7ab34f670614c5e6a78f3eff2df03ad` independently reconstructs every determinant, self-plane and rank-one polynomial in the basis `1,omega,eta,omega eta` over Q(sqrt(5)), uses the fixed rank-one reference exponent `(0,2,2,1,0,1)`, checks all 40 boxes plus four global branches, verifies **3702** strict coefficient signs by rational intervals, exact tiling and boundary strictness. Its output `frontier-20261029-cyclic15-rank1-boxcover-replay-v1.json` SHA-256 `1b253bb8e44fccb37f29bfdbd64104239e400efaced677cefc35810724effef8` is **PASS** at 03:45:45 PDT.

The rank-one argument and all imported reductions need independent written and certificate review. The seven residual cyclic classes, all noncyclic 6D complements and the omitted 25 QLS cells remain open. No formal-kernel verification or novelty clearance is claimed.
