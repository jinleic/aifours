# Level-five entire 10 and dual primitive maps for r,s≥4 — exact candidate

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 17:59:52 PDT 2026**. This is an unreviewed, computer-assisted candidate, not parent adoption, a formal/kernel, independent-model/human, novelty or priority verdict.

## 1. Claim and dependencies

For all integers `r,s>=4` and every allowed full complex Cartan realization `C` of the registered `A(r,s)`, let `S=G_C/J` be the original full Serre quotient and `P_alpha=ker(f1) intersect ker(f2)` inside the ACTUAL `S_alpha`. At the named unreviewed full-Cartan/positive-presentation/PBW/Levi inputs and exact certificate below, the full maps

\[
D_3:P_{(4,3,5)}\to S_{(4,3,4)},\qquad
D_3:P_{(3,4,5)}\to S_{(3,4,4)}
\]

are injective. Their entire joint-lowest sources are the type 10 and diagram-dual 10*, 20 source copies each. This would cover two original nontrivial primitive obligations only in the `r,s>=4` quadrant, not all positive pairs, other types, F5/B5, general Serre equality, H13, old19, arbitrary GCMs or priority/novelty. Earlier 10-type models did not establish the entire general quadrant.

The common actual source inputs are `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`: these are separately written unreviewed candidates with their full-Cartan, positive-presentation and PBW qualifications, not a parent verdict. The entire ideal geometry is spelled out in the new unreviewed 64 candidate `frontier-20261028-level5-64-entire-quadrant-candidate-v1.md` SHA `88a3d51503547c715e399ba8ced980dfbcb8df3c3575deb1c4fca5f9ea7dd0e6`, §2; this paper applies its argument afresh to the different actual 10/10* weights.

## 2. Full actual quotient and exact labels

After imposing the positive and negative Serre relations repeated at nodes 1 and 2, the positive source is `n_+(sl3) semidirect FreeLie(M)` with `M` the eight-dimensional adjoint module. The remaining WHOLE positive node-3 ideal has seeds `-(ad m0)^r m1`, `-(ad m0)^s m2` and every Levi descendant and free-Lie bracket descendant. Since `r,s>=4`, it is zero at level four. At level five, only seeds with parameter 4 occur; their complete finite-Levi types are 154 and 154*. The source argument includes both ideals and their possible intersection. There can be no additional type in their sum, by finite-Levi semisimplicity.

For degree `(4,3,5)`, the actual Levi weight is `(2*4-3-5,2*3-4-5)=(0,-3)`, whose joint-lowest irreducible is the 10 type. Neither 154 nor 154* is 10. Hence the whole 10 lowest source in the actual quotient is exactly the free 10 lowest space, while the level-four target is unchanged. This is an isotypic identification, NOT the false claim that the entire level-five quotient is free.

The diagram exchange interchanges the two Levi nodes, `r,s` and the corresponding columns/rows of the full realization `C`; it also permutes the columns of every extra Cartan row. It is a genuine isomorphism preserving full rank and transports the entire `(4,3,5)` map to `(3,4,5)`. No 35, H13 or older grade3 assay is transferred as a 10 proof.

## 3. Exact alternate full-source determinant

At `(4,3,5)` the free-Lie source has 220 complete Lyndon words. The full combined horizontal-lowering map has rank 200; its kernel has dimension 20. The pinned producer JSON contains all 220 words and the 20 exact rational source vectors. The same actual `f3` table as in the 64 candidate is extended by ordinary Jacobi:

    [f3,m_j]=(-h3,-r e1,-s e2,-(r+s)e12,-s e12,0,0,0)_j,
    [h3,m_j]=(2-r a_j-s b_j)m_j.

Thus every f3 entry is affine in `x=r-4,y=s-4`.

**First minor remains mixed:** the baseline pivot determinant has 142 positive and 87 negative nonzero monomial coefficients and is not an orthant nonvanishing certificate. Its frozen full polynomial and original pencil are retained below, not edited or declared passing.

A deterministic exact one-row search replaced the first target row `0057` by `0714` and found the following 20 actual free-target word rows:

    0714 0075 0137 0147 0165 0173 0255 0317 0335 0345
    0353 0371 0417 0435 0445 0453 0471 0507 0525 0533.

This complete alternate determinant has total degree at most 20, **229 strictly positive nonzero monomial coefficients**, and exact nonzero constant

    2047131140020475540036124672.

Therefore it is positive for all `x,y>=0`, and the whole 20-dimensional free `D3` source injects into the actual unchanged target. Section 2 transports this to the original quotient and to the diagram-dual map. Full 400 affine entries, all coefficients, pivot order and the actual deterministic search are in the pinned output, not inferred from a sample.

## 4. Exact verification and pinned artifacts

The alternate search found the one-sign minor after 16 deterministic substitutions. It used full exact total-degree-20 bivariate interpolation on the 231 triangular integer grid points, with integer Bareiss determinants and an exact reconstruction check at all points. The separate replay rebuilds the actual matrix-unit actions and all 220 Lyndon basis words, verifies the entire horizontal rank 200 and all 20 lowest vectors, and applies the local `f3` action with bracket-tree Jacobi. It independently checks every constant/x/y entry of the 20×20 pencil and recomputes all 231 determinants via Fraction Gaussian elimination against the complete polynomial. The triangular binomial basis makes that grid unisolvent for degree<=20, so this establishes the full polynomial at the stated computational trust boundary, not merely 231 sample parameters.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level5-free-type-pencil.py` | 62 | `ceb2ec1169ceaa81fdb0b12804f8f3c4aeae05103d2d6684707b6ba86cf56294` |
| `frontier-20261028-level5-free-43-pencil-v1.json` | 4641 | `e9621d5b438f1320c27679ec5215812f83c529c97143e1557020e13c1bdb2c4f` |
| **initial mixed** `frontier-20261028-level5-free-43-determinant-v1.json` | 1189 | `8ee3e673e71ff6e47ec0514950d4b5f99affa99a456ed4796d47f369b8e1606c` |
| `frontier-20261028-level5-10-alternate-minor-search.py` | 54 | `f4ddfe083de11fe9362817def622375e004fdfec0de3aec54ae700b22e89ce87` |
| `frontier-20261028-level5-10-alternate-minor-search-v1.json` | 3233 | `4544fa493a404775cf250fd865f8a304ac8a83988bce43ea37dc76e8d4499d83` |
| `frontier-20261028-level5-alternate-type-independent-replay.py` | 70 | `10418fc327c11d931b29fac7a1d0164f9a5481f97bc2844ab68432f1dbb528fa` |
| `frontier-20261028-level5-10-alternate-independent-replay-v1.json` | 26 | `ee961070a312a80b6f2a5ea32f0bdc8c23c23abd85ace85da5355c72af092dd1` |
| generic search helpers `frontier-20261028-level5-35-alternate-minor-search.py` | 130 | `d9683fa9d604621ca163cc00be8315fb33493f691e93e39f88470f8578b288e5` |
| separate tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

Actual replay returned `PASS (4, 3, 5) source 220 kernel 20 grid 231 one-sign terms 229` followed by native **Wed Oct 28 17:59:36 PDT 2026**. The implementations share some generic local helpers and are not a formal/external-family review. The whole source/ideal argument and every exact-code premise need independent reconstruction. Earlier held/withdrawn output and process findings remain historical and unaccepted as premises.

**END — whole 10 and dual in r,s≥4, exact-source candidate only; review pending.**
