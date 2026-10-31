# Level-five entire adjoint primitive map for r,s≥4 — exact candidate

**MathKacMoody-2 / math-3.** Native clock observed before this additive write: **Wed Oct 28 18:01:45 PDT 2026**. New whole-source, exact-program-assisted candidate; no parent adoption, formal/kernel, human, independent-model, novelty or priority acceptance.

## 1. Exact whole-map scope

For every integer `r,s>=4` and every allowed full complex Cartan realization `C` of the registered `A(r,s)`, define `S=G_C/J` as the original Serre quotient and `P_alpha=ker(f1) intersect ker(f2)` inside ACTUAL `S_alpha`. At the named full-Cartan/free-Levi/PBW and exact-code inputs below, the candidate is

\[
D_3:P_{(4,4,5)}\longrightarrow S_{(4,4,4)}\quad\text{injective}.
\]

This is the entire original adjoint-8 lowest-weight source, with 29 copies, not selected input columns. The source degree is fixed; the whole isotypic `sl3` module has 8 times as many vectors and is not the domain of this displayed map. This settles one of the seven nontrivial original primitive slots only for the quadrant `r,s>=4` if subsequently reviewed and accepted. No other parameter ranges, F5/B5, global Serre equality, H13/old19, arbitrary GCMs or novelty/priority is established.

## 2. Actual quotient, all ideals, and full lowering

The common separately written unreviewed inputs are `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`, including their actual full-Cartan, positive-presentation and PBW qualifications. The complete quadrant ideal argument is explicitly written in the unreviewed 64 candidate `frontier-20261028-level5-64-entire-quadrant-candidate-v1.md` SHA `88a3d51503547c715e399ba8ced980dfbcb8df3c3575deb1c4fca5f9ea7dd0e6`, §2; this paper checks the present different source label and full map.

The positive source after the repeated-1/2 relations is `n_+(sl3) semidirect FreeLie(M)`, `M` the eight-dimensional adjoint. The remaining full node-3 ideals have seeds `-(ad m0)^r m1`, `-(ad m0)^s m2` with entire Levi closures and Lie descendants. For `r,s>=4` these ideals have no level-four part. In level five, only an r=4 or s=4 seed can occur, of irreducible Levi type 154 or 154*; both and any overlap are retained. The actual degree `(4,4,5)` has lowest Levi weight `(-1,-1)`, hence is type 8. Since 154 and 154* have no 8 summand, semisimplicity identifies the whole actual 8 lowest space with the free 8 lowest space. The actual level-four target is free in this quadrant. This is NOT an equality of whole level-five free and quotient spaces.

The actual local node-3 table, in the same eight source letters, is

    [f3,m_j]=(-h3,-r e1,-s e2,-(r+s)e12,-s e12,0,0,0)_j,
    [h3,m_j]=(2-r a_j-s b_j)m_j.

Its ordinary Jacobi extension is affine in `r,s`; all eight letters, repeated Cartan rows and original signs are retained. Extra realization directions remain full and are not projected away.

## 3. Entire 29-source determinant and prior mixed pivot

There are 356 free-Lie Lyndon words at `(4,4,5)`. The full `f1/f2` horizontal map has rank 327; the complete joint lowest source has dimension 29. The pinned source JSON gives every word and every coefficient of a basis of that whole kernel.

The first 29×29 baseline pivot minor had 331 positive and 132 negative nonzero coefficients in `x=r-4,y=s-4`; it is not a global certificate and is explicitly retained. A separate deterministic search found a one-signed minor after 37 row substitutions, replacing the first selected target word `0077` with the actual word `1634`. In determinant order the full 29 target rows are

    1634 0167 0176 0257 0275 0337 0347 0356 0365 0373
    0374 0437 0447 0456 0465 0473 0474 0527 0536 0563
    0564 0617 0635 0653 0654 0716 0725 0733 0734.

The resulting determinant has total degree at most 29 and **463 nonzero monomial coefficients, all strictly positive**. Its exact nonzero constant is

    65952704290729348871841255666401031487488.

Thus it is positive for all real `x,y>=0` and all original integer `r,s>=4`. This proves injectivity on the entire free 29-source space, and §2 transports it to the entire actual quotient source and actual target. The complete 29×29 affine matrix, 463 coefficients and target row order are in the pinned alternate JSON. No assumption is made that raw tensor coordinates descend through a nonzero level-four ideal outside this quadrant.

## 4. Exact replay and proof ceiling

The producer used exact row-cleared integer Bareiss determinants on all 465 grid points `(i,j)` with `i+j<=29`; the complete ordinary monomial polynomial was reconstructed by exact bivariate Newton interpolation and verified on all grid points. Each matrix entry is affine, so degree<=29, and the triangular binomial basis evaluation matrix is invertible; these 465 checks determine the WHOLE polynomial.

A separately constructed replay rebuilds the 356 source words and the entire rank-327 horizontal map from matrix units, proves the 29 recorded source vectors independent and killed by `f1,f2`, checks all three coefficients of all 841 alternate matrix entries using bracket-tree Jacobi, and recomputes all 465 determinant values by exact Fraction Gaussian elimination. It verifies all 463 signs and the nonzero constant. This is an independent implementation of critical calculation paths, sharing some generic helpers; it is not external-family, human or formal verification.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level5-free-type-pencil.py` | 62 | `ceb2ec1169ceaa81fdb0b12804f8f3c4aeae05103d2d6684707b6ba86cf56294` |
| `frontier-20261028-level5-free-44-pencil-v1.json` | 10687 | `537e3c12b37c77ce2af6e37e32c31a65bbe2025c2994619981060ef10d8e694b` |
| **initial mixed** `frontier-20261028-level5-free-44-determinant-v1.json` | 2368 | `47568d55b1edbd1a903501089be11fb1f293a8c72ef7ae03a4346b9db2d2d04b` |
| `frontier-20261028-level5-alternate-type-minor-search.py` | 83 | `4384a94d18dee66db2cc94c238b487a19c0a9caec8ac6fd63f36e180b08d8a75` |
| `frontier-20261028-level5-8-alternate-minor-search-v1.json` | 6637 | `c0c98f8b764386b4b0d7c31803887446adf163575d79228500056976e05adff9` |
| `frontier-20261028-level5-alternate-type-independent-replay.py` | 70 | `10418fc327c11d931b29fac7a1d0164f9a5481f97bc2844ab68432f1dbb528fa` |
| `frontier-20261028-level5-8-alternate-independent-replay-v1.json` | 26 | `65a95bda84e801ccc7c575360b56694a3442c90fe003660dde556c46c53c4a48` |
| generic search helpers `frontier-20261028-level5-35-alternate-minor-search.py` | 130 | `d9683fa9d604621ca163cc00be8315fb33493f691e93e39f88470f8578b288e5` |
| separate tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

Actual replay returned `PASS (4, 4, 5) source 356 kernel 29 grid 465 one-sign terms 463`, with native **Wed Oct 28 18:01:32 PDT 2026**. A separate reviewer must reconstruct the full source, quotient, actual local lowering and complete code/certificate union. Prior held/withdrawn outputs and process findings are not reclassified or used as accepted premises.

**END — entire actual adjoint map at r,s≥4; independent review pending.**
