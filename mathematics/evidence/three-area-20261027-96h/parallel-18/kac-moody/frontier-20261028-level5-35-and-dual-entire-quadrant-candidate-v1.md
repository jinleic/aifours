# Level-five entire 35 and dual primitive maps for r,s≥4 — exact candidate

**MathKacMoody-2 / math-3.** Native clock observed before this additive write: **Wed Oct 28 17:57:58 PDT 2026**. New whole-source candidate with separately constructed exact producer and replay. It awaits independent full-chain review and parent assessment; it is not formal/kernel, external-model/human, priority or novelty acceptance.

## 1. Exact claim and nonclaims

For every integer `r,s>=4` and every allowed full complex Cartan realization `C` of the registered `A(r,s)`, let `S=G_C/J` be the actual full Serre quotient. Define `P_alpha=ker(f1) intersect ker(f2)` in the ACTUAL `S_alpha`. At the named candidate inputs and exact certificate below,

\[
D_3:P_{(3,2,5)}\to S_{(3,2,4)},\qquad
D_3:P_{(2,3,5)}\to S_{(2,3,4)}
\]

are both injective. Each is the **ENTIRE** original lowest-weight source, not a selected line. The first is type 35 and the second its diagram-exchanged dual. The 35 source contains 20 lowest vectors. This result, if reviewed and adopted, would solve two of the seven original nontrivial primitive obligations only in the `r,s>=4` quadrant; it does not settle either map on every positive pair or any other primitive type, F5/B5, global Serre equality, H13, old19, arbitrary GCMs or novelty.

Earlier `kac-nontrivial-blocks-parent-v1.md` supported a 35 source line with a still-open 19→35 quotient; it is not a full-source proof. No such earlier detector or held guide is consumed here. The current `frontier-20261028-level5-64-entire-quadrant-candidate-v1.md` gives the common written free-Levi/whole-ideal argument as a separate **unreviewed** candidate; this file explicitly specializes that argument to 35, with a different actual source, target and independent determinant.

## 2. Whole source and target, including both seed ideals

At the separately pinned unreviewed full-Cartan/level-one/PBW inputs `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`, the positive degree is obtained from `FreeLie(M)` for the eight-dimensional adjoint `sl3` module `M` by the FULL remaining node-3 Serre ideal. The actual seed lengths are `r+1,s+1`. Thus for `r,s>=4` the node-3 ideal at level four is zero; at level five it consists only of the complete Levi modules of the r=4 and/or s=4 seeds, of types 154 and 154*. The seed is killed by both horizontal lowerings by `f1 m1=m0`, `f2 m1=f1 m0=f2 m0=0`, with `[m0,m0]=0`; its lowest label at `(1,0,5)` is `(-3,-6)`. Both ideals, including a possible overlap, are retained.

The actual degree `(3,2,5)` has Levi weight `(2*3-2-5,2*2-3-5)=(-1,-4)`, so its joint lowest space is the 35-type multiplicity space. Since 154 and 154* are distinct irreducibles from 35, finite-Levi semisimplicity shows the entire 35 lowest source of the quotient is isomorphic to the entire free 35 lowest source. The level-four target is actually free at this parameter boundary. The analogous diagram exchange swaps the first two simple nodes, `r,s`, and the first two columns/rows of the ENTIRE Cartan realization `C`, including all extra rows; it preserves full rank and transports the whole `(3,2,5)` map into the whole `(2,3,5)` map. No H13 or previous 35/35* assay is imported.

## 3. All 20 sources and a globally nonzero alternate minor

The entire free source degree `(3,2,5)` has 80 Lyndon words. Its full combined `f1/f2` map has rank 60, so the joint lowest space has dimension 20. Its complete rational basis over all 80 words is pinned below. On the actual eight-letter module, retain the same original local brackets

    [f3,m_j]=(-h3,-r e1,-s e2,-(r+s)e12,-s e12,0,0,0)_j,
    [h3,m_j]=(2-r a_j-s b_j)m_j,

and extend by Jacobi over each full source vector. The resulting matrix is affine in `r,s`.

**First attempt explicitly retained, NOT used as a proof:** the 20×20 baseline pivot minor in `frontier-20261028-level5-free-32-determinant-v1.json` has 154 negative and 73 positive nonzero monomial coefficients in `x=r-4,y=s-4`. It therefore does not satisfy the one-sign test; no global rank conclusion follows from that failed test. Its immutable bytes remain and are pinned below.

A separate deterministic exact alternate search replaced the second selected target row `0035` by the actual word row `0414` (zero-based slot 1). Its complete 20 actual free-target rows, in determinant order, are

    0017 0414 0045 0053 0054 0071 0107 0116 0125 0133
    0134 0143 0144 0161 0215 0251 0305 0313 0314 0331.

The FULL resulting determinant polynomial has total degree at most 20, with **227 nonzero coefficients all strictly negative** and constant exactly

    -10377386817618023515422720.

Therefore it is strictly negative for every `x,y>=0`, proving the complete 20-source free `D3` map injective on the entire quadrant, not merely at a selected pair. By §2 this is exactly the actual map; diagram exchange gives the dual. The full 400 entries, each with its exact constant/x/y coefficients, the entire 227-term polynomial, row selection, exact search count and sign are stored in the alternate JSON. Nothing is inferred from matrix dimensions or the original mixed minor.

## 4. Complete exact certificate and independently constructed replay

The alternate search tried 131 deterministic one-row substitutions, with one surviving both necessary exact axis-sign filters. For that candidate it computed all 231 integer-grid determinants `(i,j)` with `i+j<=20`, by integer Bareiss, and recovered every monomial coefficient by exact two-variable Newton interpolation. The total degree bound is 20 because the 20 matrix rows are affine; the binomial basis and triangular grid make the interpolation unisolvent. Every grid value is checked against the recovered polynomial.

The independent replay separately rebuilds all 80 source Lyndon words via matrix-unit `sl3` actions, verifies the complete rank-60 horizontal map and each of the 20 spanning lowest vectors, and computes all original `f3` derivatives via bracket-tree Jacobi rather than the producer's tensor suffix rule. It checks all three coefficients of all 400 alternate matrix entries and all 231 determinant values using exact **rational Gaussian elimination**, not Bareiss or the producer's interpolation. The reconstructed polynomial has the same 227 negative coefficients and nonzero constant. These are separately authored computation paths sharing some generic exact-linear-algebra code, not independent-family or formally verified algorithms.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level5-free-type-pencil.py` | 62 | `ceb2ec1169ceaa81fdb0b12804f8f3c4aeae05103d2d6684707b6ba86cf56294` |
| `frontier-20261028-level5-free-32-pencil-v1.json` | 2769 | `17f68c1d9c6ff9204e839e3d91466d9bae338e5f4cfebefca76f25b50057c324` |
| **mixed initial minor** `frontier-20261028-level5-free-32-determinant-v1.json` | 1179 | `b0540a915da272a5d775799af80ca4f9fcf5d86c5a38778932b9b08238f409e8` |
| `frontier-20261028-level5-35-alternate-minor-search.py` | 130 | `d9683fa9d604621ca163cc00be8315fb33493f691e93e39f88470f8578b288e5` |
| `frontier-20261028-level5-35-alternate-minor-search-v1.json` | 3223 | `a6a84ec980d73e818938d824fb12d35a967dce9131f85523caa7c2c2a13a89ec` |
| `frontier-20261028-level5-35-alternate-independent-replay.py` | 73 | `8cff89fde5c70173c54fcc617fb7a30059586af6cc67dc71e14d49b1f984f381` |
| `frontier-20261028-level5-35-alternate-independent-replay-v1.json` | 26 | `e70221b278c5c6be89b5a7c84fbbb3cd25d094f69664e3b46ab87d7bc5335b67` |
| shared separate tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

Actual replay returned `PASS (3, 2, 5) source 80 kernel 20 grid 231 one-sign terms 227`, followed by native **Wed Oct 28 17:57:50 PDT 2026**. All operations are exact integer/Fraction; code-dependent claims require a separate reviewer to reconstruct the actual source, ideal, matrix and interpolation, not merely read this verdict. Earlier STOP/HOLD/ZERO and process findings remain historical and are not rehabilitated by the new computations.

**END — entire 35 and its diagram dual for r,s≥4, at named inputs and exact-code trust boundary, independent review pending.**
