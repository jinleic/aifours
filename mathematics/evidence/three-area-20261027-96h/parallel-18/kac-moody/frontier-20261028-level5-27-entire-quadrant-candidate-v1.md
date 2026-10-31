# Level-five entire 27 primitive map for r,s≥4 — exact candidate

**MathKacMoody-2 / math-3.** Native clock observed before this additive write: **Wed Oct 28 18:03:52 PDT 2026**. This whole-source exact-program-assisted candidate is UNREVIEWED and NOT a parent disposition, formal/kernel, external-model/human, novelty or priority acceptance.

## 1. Complete original map, exact scope

For every integer `r,s>=4` and every allowed full complex Cartan realization `C` of the registered `A(r,s)`, let `S=G_C/J` be the full original Serre quotient and `P_alpha=ker(f1) intersect ker(f2)` INSIDE `S_alpha`. At the exact candidate full-Cartan/free-Levi/PBW and code inputs below,

\[
D_3:P_{(3,3,5)}\longrightarrow S_{(3,3,4)}\quad\text{is injective}.
\]

The domain is the entire 36-dimensional type-27 lowest-weight multiplicity space; it is not the entire 27-isotypic module and is not a selected source subspace. This would cover the last of the seven nontrivial primitive slots in the `r,s>=4` quadrant together with the separate 64/35/35*/10/10*/8 candidates, if all are fully reviewed; it does NOT by itself cover the smaller rows, F5/B5, global Serre equality, arbitrary GCMs, H13/old19 or novelty.

## 2. Whole actual ideals, source and target

The separately written UNREVIEWED inputs `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f` provide the full-Cartan positive-presentation/finite-Levi/PBW identification `n_+(sl3) semidirect FreeLie(M)`, with `M` the adjoint eight. The common quadrant ideal proof is stated in the separately unreviewed `frontier-20261028-level5-64-entire-quadrant-candidate-v1.md` SHA `88a3d51503547c715e399ba8ced980dfbcb8df3c3575deb1c4fca5f9ea7dd0e6`, §2. Its actual application is rechecked here for type 27.

The TWO remaining node-3 Serre seeds and their entire Levi/free-Lie descendants are retained. For `r,s>=4` they first appear at level five, and only at entry 4; their full Levi types are 154 and 154*, so there is NO level-four ideal. At degree `(3,3,5)` the horizontal lowest weight is `(-2,-2)`, hence the irreducible 27 type. It cannot occur in 154 or 154*, even when both seeds occur or overlap. Finite-Levi complete reducibility gives a full source-isotype quotient isomorphism and an unchanged level-four target. It does NOT give an equality of the WHOLE level-five quotient with the free source.

On the same eight actual basis letters the original local table is

    [f3,m_j]=(-h3,-r e1,-s e2,-(r+s)e12,-s e12,0,0,0)_j,
    [h3,m_j]=(2-r a_j-s b_j)m_j.

Extend by ordinary Jacobi over every source bracket, keeping the actual Cartan row and all full-realization directions. Each resulting entry is affine in `x=r-4,y=s-4`.

## 3. Every source and one global determinant

At the full degree `(3,3,5)` there are 172 free-Lie Lyndon words. The combined horizontal-lowering map on all 172 has rank 136, leaving exactly 36 joint-lowest vectors. All 172 words and all rational coefficients of a basis of the full 36-space are in the pinned source pencil.

The **first** 36×36 baseline pivot determinant had 58 positive and 633 negative monomial coefficients. This mixed sign fails the global one-sign test; its exact file remains unchanged and is not used as a proof. The deterministic alternate search preserved it, tried 37 one-row replacements, and chose the actual target word `1261` in place of `0037` as the first row. The entire 36-row order is

    1261 0047 0056 0065 0073 0074 0127 0136 0146 0163
    0164 0172 0217 0235 0245 0253 0254 0271 0307 0316
    0325 0333 0334 0343 0344 0352 0361 0407 0416 0425
    0433 0434 0443 0444 0452 0461.

The complete alternate determinant has total degree at most 36, with **691 nonzero coefficients, all strictly positive**, and exact constant

    19175725549449184660682408903476128274905563136.

The determinant is therefore positive for all `x,y>=0`, proving that `D3` is injective on every one of the 36 free lowest vectors throughout the quadrant. Section 2 transports that statement to the original entire quotient source and unchanged target. The full 36×36 affine matrix and all 691 coefficients are supplied, not a guessed rank from finitely many parameter values.

## 4. Exact producer, independent replay, pinned evidence

The search computed every determinant on the triangular grid `(i,j)` with `i+j<=36`: 703 integer points. It uses exact row-cleared Bareiss elimination, bivariate Newton finite differences and exact verification against the complete recovered polynomial. A determinant of a 36×36 affine pencil has total degree at most 36; the binomial basis on that triangular grid is unisolvent, so the 703 identities determine the complete polynomial.

The separately constructed replay rebuilds ALL 172 Lyndon source vectors and both horizontal actions from matrix units, checks their full rank 136 and every one of the 36 spanning lowest vectors, then reconstructs node-3 lowering by bracket-tree Jacobi instead of the producer's suffix method. It verifies the constant/x/y coefficient of every one of the 1296 alternate entries and independently computes every one of the 703 determinant values via Fraction Gaussian elimination. It checks all 691 polynomial coefficients have the same strict sign and the constant is nonzero. The paths share generic local helpers and are neither a different-model/human review nor a formal proof.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level5-free-type-pencil.py` | 62 | `ceb2ec1169ceaa81fdb0b12804f8f3c4aeae05103d2d6684707b6ba86cf56294` |
| `frontier-20261028-level5-free-33-pencil-v1.json` | 9704 | `8b3db2e4e8430e052c40d6d546c8c85c65ded0a18aa27f13f2121805f4646900` |
| **initial mixed** `frontier-20261028-level5-free-33-determinant-v1.json` | 3515 | `30e9ab84a47d12570a19a16c889f43e2df16c907f5f76f6e03617d9d6057d223` |
| `frontier-20261028-level5-alternate-type-minor-search.py` | 83 | `4384a94d18dee66db2cc94c238b487a19c0a9caec8ac6fd63f36e180b08d8a75` |
| `frontier-20261028-level5-27-alternate-minor-search-v1.json` | 10073 | `f6433e26341b1b601e771dc164a3292e54ba49df347661cd9d82933c67b7b009` |
| `frontier-20261028-level5-alternate-type-independent-replay.py` | 70 | `10418fc327c11d931b29fac7a1d0164f9a5481f97bc2844ab68432f1dbb528fa` |
| `frontier-20261028-level5-27-alternate-independent-replay-v1.json` | 26 | `c12dd6d21d2c9e22e341caaeac92d625fd3d0896e8083fc690d17341175510b7` |
| generic search helpers `frontier-20261028-level5-35-alternate-minor-search.py` | 130 | `d9683fa9d604621ca163cc00be8315fb33493f691e93e39f88470f8578b288e5` |
| independent tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

Actual replay printed `PASS (3, 3, 5) source 172 kernel 36 grid 703 one-sign terms 691` followed by native **Wed Oct 28 18:03:36 PDT 2026**. All arithmetic is integer/Fraction. A reviewer must reconstruct the full source/ideal/Cartan/Jacobi/interpolation union before any parent adoption; merely reading a table or this summary is insufficient. Prior held/withdrawn artifacts and process findings remain historical and are not accepted as new premises.

**END — full actual 27 map for r,s≥4, exact-program-assisted candidate only.**
