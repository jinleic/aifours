# Level-six (2,2,6) entire-source broad ratio cone — exact candidate

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:00:44 PDT 2026**. This is a NEW exact-program-assisted UNREVIEWED mathematical candidate. The independently authored full-target/tree-Jacobi/Sylvester replay has returned PASS at the scope below; it is NOT a parent decision, human/formal/kernel, independent-model, novelty or priority result.

## 1. Exact entire-map region

For every pair of positive integers `r,s>=6` satisfying

\[
(r-6)+(s-6)\ \ge\ \frac92\,|r-s|,\tag{1}
\]

and every allowed FULL complex Cartan realization of original `A(r,s)`, let `S=G_C/J` and `P=ker(f1) intersect ker(f2)` in its actual degree `(2,2,6)`. At the named unreviewed full-Cartan/positive-presentation/PBW and exact-code inputs, the candidate is that the ENTIRE original map

\[
D_3:P_{(2,2,6)}\longrightarrow S_{(2,2,5)}
\]

is injective. Its source is the full 34-dimensional type125 lowest multiplicity space. Equality in (1) is INCLUDED. This is a broad unbounded **ratio** cone, not the whole quadrant or a fixed finite gap: for every positive integer q the non-diagonal family `(r,s)=(6+11q,6+7q)` lies on its boundary and has unbounded gap `4q`.

The separate exact `|r-s|<=41` strip candidate `frontier-20261028-level6-226-gap41-strip-candidate-v1.md`, 74LF SHA `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40`, uses a DIFFERENT one-sided minor/sign proof and node exchange; at their jointly named unreviewed inputs the two regions can be unioned. The earlier explicit cofactor cone is yet another separate sufficient condition. None implies F6/B6, full quadrant injectivity, other root degrees, arbitrary-GCM/all-level Serre, novelty or priority.

## 2. Actual source, complete target and affine operators

The actual full-Cartan/free-Levi/PBW source inputs are `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`, both UNREVIEWED with their stated structural/PBW transcription qualification. For r,s>=6 the original remaining node-3 seeds have level at least7. Therefore the entire level6 source and level5 target are the ACTUAL free-Levi spaces, not a quotient with a hidden level5/6 ideal.

The fixed degree `(2,2,6)` contains 74 free-Lie Lyndon words. The full `f1/f2` horizontal map has rank40 and its entire joint kernel has dimension34. The full actual f3 target coordinate vectors occupy 235 tensor-word rows in the faithful free associative word host. Any words outside these 235 are identically zero in the affine pencil; no selected target minor is used in the argument.

Put `x=r-6`, `y=s-6`, `m=(x+y)/2`, `d=(x-y)/2`. On all 235 target rows and all 34 source vectors, the exact original h3/Jacobi lowering is

\[
D(x,y)=A+xB+yC=A+mL+dK,\qquad L=B+C,\quad K=B-C.
\]

A,B,C are the full rational matrices pinned below. Define real symmetric 34×34 forms

\[
H_0=L^TA+A^TL,\quad H_L=2L^TL,\quad H_K=L^TK+K^TL,\quad\lambda=9/2.
\]

The exact certificate reconstructs ALL 235×34×3 entries and proves by 34 positive rational LDL pivots each that

\[
H_0\succ0,\qquad \lambda H_L+H_K\succ0,\qquad \lambda H_L-H_K\succ0.\tag{2}
\]

`H_L` itself is positive semidefinite by its literal form `2L^TL`. The separate independent replay checks every actual source vector, every full-target affine entry and all three entire matrices, then recomputes their **102 positive leading principal determinants** using exact row-cleared integer Bareiss. This is a different determinant/positivity algorithm from the producer's rational LDL.

## 3. Written all-variable proof, including equality

For a nonzero complex source-coordinate vector z, the real symmetric forms act as Hermitian forms on `C^34`, so (2) implies `z*H0 z>0`. Also

\[
2\operatorname{Re}((Lz)^*D(x,y)z)
=z^*\bigl(H_0+mH_L+dH_K\bigr)z.\tag{3}
\]

Condition (1) is exactly `m>=lambda |d|`. If `d>=0`,

\[
mH_L+dH_K=(m-\lambda d)H_L+d(\lambda H_L+H_K)\succeq0.
\]

If `d<=0`, replace the last term by `|d|(lambda H_L-H_K)` and use `m-lambda|d|>=0`. Thus the right side of (3) is STRICTLY positive for every nonzero z, even when equality holds in (1). If `D(x,y)z=0` the left side is zero, contradiction. This proves full column rank, hence injectivity of the entire actual original D3 map on the stated region.

The Euclidean word-coordinate pairing in (3) is an AUXILIARY finite-dimensional linear-algebra test on the faithful tensor-word host. It is NOT asserted to be an invariant, positive or contravariant form on the nonsymmetrizable Lie algebra. Nor is `D` claimed to equal `A* A`. The left test here is `L^T`, different from the separately disproved naive `A^T` slope forms; there is no contradiction with `frontier-20261028-level6-226-euclidean-accretivity-obstruction-v1.md` SHA `27376ed275b3814b62b8963831270499388940dae63e3d424aefa96f05da79af`. Lambda `9/2` is a proved sufficient rational constant, not an optimality assertion.

## 4. Exact evidence and separate replay

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-226-ratio-cone-certificate.py` | 61 | `49bd5d8c0970e9d7e7e4a2e7ceef64c44188b19604ae4cee8635c83bcd5a45ab` |
| `frontier-20261028-level6-226-ratio-cone-certificate-v1.json` | 44464 | `ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b` |
| `frontier-20261028-level6-226-ratio-cone-independent-replay.py` | 78 | `f98b4f2041bcb3cb233e8768516db294cea3f6dd248e81d09019f503970e3267` |
| `frontier-20261028-level6-226-ratio-cone-independent-replay-v1.json` | 135 | `3eb7f2f9ee8211b3510715eddc72f56bb5cc85d1c2aab67b63b1225033437879` |
| current actual source pencil `frontier-20261028-level6-free-22-pencil-v1.json` | 6561 | `b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc` |
| independent tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

Actual producer returned `PASS full target 235 rows; H0 and (9/2)HL ± HK each have 34 positive exact LDL pivots` at **18:59:47 PDT**. The separately authored replay returned `PASS level6 (2, 2, 6) 74 source/34 lowest/235 target rows; all entries and 102 positive Sylvester minors` at **19:00:26 PDT 2026-10-28**. Every operation was exact integer/Fraction, not a spectral floating approximation. Source generation and LDL versus independent tree-Jacobi and Bareiss are different paths, but they share generic local helpers; this is not independent-model/vendor, human or formal proof.

A full review must reconstruct the PBW/source ideal absence, all 235×34×3 entries, all three positivity certificates, the complex-Hermitian implication and exact parameter region. The earlier incidental older cone-status methodological exposure, all prior ZERO/STOP/HOLD/process qualifications and the outstanding separate 162-source `(4,4,6)` replay remain unchanged. No novelty, priority or parent adoption is claimed.

**END — entire actual level-six type125 map on the exact broad ratio cone, independent review pending.**
