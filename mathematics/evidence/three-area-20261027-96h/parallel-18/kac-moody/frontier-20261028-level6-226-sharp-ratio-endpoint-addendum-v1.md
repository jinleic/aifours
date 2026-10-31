# Exact algebraic endpoint for the chosen level-six ratio-cone certificate

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:07:56 PDT 2026**. This is an UNREVIEWED exact-algebraic strengthening of `frontier-20261028-level6-226-full-target-ratio-cone-candidate-v1.md`, 83LF SHA `6e8049679de3cd2d78f390edf0393d0abf31e6a0e65d531356f0d3a47bafb7d3`. No frozen file is edited, and no parent/formal/human/independent-model/novelty or priority acceptance is claimed.

## 1. Exact endpoint and larger full-source region

Retain the entire ACTUAL 34-source/235-target pencil and three real symmetric forms `H0,HL,HK` in the previous candidate, including all unreviewed full-Cartan/free-Levi/PBW and actual-ideal-absence inputs. Define the exact algebraic number

\[
\lambda_*:=\max\{\,|z|:\ z\in\mathbb R,\ \det(H_K-zH_L)=0\,\}.\tag{1}
\]

This is a fully specified finite 34×34 rational determinant and a maximum over its real roots, not a rounded optimizer result. At the same exact inputs, the entire original D3 map at `(2,2,6)` is injective for every integer `r,s>=6` satisfying

\[
r+s-12\ \ge\ \lambda_*|r-s|.\tag{2}
\]

Equality is INCLUDED. Further, exact certificates give

\[
449/100 < \lambda_* < 719/160 < 9/2.\tag{3}
\]

Thus the explicit rational condition `r+s-12 >= (719/160)|r-s|` also suffices and strictly extends the previously written 9/2-ratio cone. For example, **every** positive integer q yields `r=6+1759q, s=6+1119q`, with `r+s-12=2878q`, `|r-s|=640q`; it satisfies the 719/160 condition because `2878q>=2876q`, and lies outside the earlier 9/2 cone because `2878q<2880q`. This is a symbolic infinite family, not a sampled rank inference.

The coefficient `lambda_*` is optimal ONLY for the requirement that BOTH chosen symmetric slope forms in §2 be positive semidefinite. It is NOT asserted to be the maximal injectivity region of the actual map; a different left test or determinant may work outside it. No all-quadrant, F6/B6, global Serre, arbitrary GCM, novelty or priority claim follows.

## 2. Why the algebraic definition is well-defined

The earlier separately replayed certificate proves `H0=L^T A+A^T L` strictly positive definite. Hence L has full column rank: if `Lv=0`, then `v^T H0 v=0`, forcing v=0. Therefore `HL=2L^TL` is strictly positive definite. Since `HK` is real symmetric, the generalized eigenvalues of the pair `(HK,HL)` are the real eigenvalues of `HL^(-1/2) HK HL^(-1/2)`; all 34 roots in (1), counted with multiplicity, are real. Standard finite-dimensional spectral theory makes the maximum in (1) well-defined and algebraic.

By definition, `lambda_* HL ± HK` are positive semidefinite. With `x=r-6`, `y=s-6`, `m=(x+y)/2`, `d=(x-y)/2`, the condition (2) is exactly `m>=lambda_* |d|`. As in the prior paper,

\[
2\Re((Lz)^*D z)=z^*(H_0+mH_L+dH_K)z.
\]

For either sign of d, write `mHL+dHK` as `(m-lambda_* |d|)HL` plus `|d|(lambda_* HL ± HK)`, both positive semidefinite. H0 is strictly positive definite, so the right side is strictly positive for all nonzero complex z, including equality in (2). Thus D has no nonzero kernel. This uses only the auxiliary rational tensor-word coordinate pairing, not a positive invariant form on the nonsymmetrizable Lie algebra.

## 3. Exact bounds and independent replay

For the upper bound, the new exact producer forms `(719/160)HL ± HK` from the already independently reconstructed 235-row target matrices and records **34 positive rational LDL pivots each**. The separate replay reconstructs both matrices from the pinned old `9/2` plus/minus forms and checks **all 68 leading principal determinants** are strictly positive using row-cleared integer Bareiss. Thus every generalized eigenvalue has absolute value strictly less than `719/160`.

For the lower bound, a separate exact rational vector v satisfies

\[
v^T\bigl((449/100)H_L-H_K\bigr)v<0.
\]

Since `HL` is positive definite, its Rayleigh quotient exceeds `449/100`; the maximum absolute generalized eigenvalue is therefore strictly larger. All 34 exact rational coordinates and the negative rational value are in the pinned output. A separately authored replay evaluates the same quadratic directly from the independently pinned old plus/minus matrices and verifies strict negativity. No floating eigenvalue or approximate root is used.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-226-ratio-upper719-certificate.py` | 33 | `2955255c6b030eca8d3935bb38991e79c21fa6392c1acb86f67a3b45814f94c8` |
| `frontier-20261028-level6-226-ratio-upper719-certificate-v1.json` | 2535 | `d4e1dab3ff1885c65d310a621cd6a4ecfd4ab95f85f66d1e0d22ca2ce3ebe131` |
| `frontier-20261028-level6-226-ratio-upper719-independent-replay.py` | 39 | `db5471f3f7201ec0813c217c9e6b02eace038f5d163a41601d242f2dcef5276f` |
| `frontier-20261028-level6-226-ratio-upper719-independent-replay-v1.json` | 80 | `02e76b5b646f9a6e547a5baaadee63b056fb41706ac4a3c94bbd6c1bd2afec64` |
| `frontier-20261028-level6-226-ratio-endpoint-certificate.py` | 43 | `07e8cacfaa716f83c6ed0d3714fd730741a396bee62bb8a4f3605b7c33e15598` |
| `frontier-20261028-level6-226-ratio-endpoint-certificate-v1.json` | 48 | `8b7e843b31f1ed4d64abcfae77bee56764c8d406155c1cb381910e4756871bab` |
| `frontier-20261028-level6-226-ratio-endpoint-independent-replay.py` | 28 | `187309b794e51a0843b8cb521d14fa18dc8673f794a1af2a71849aedb3876cd3` |
| `frontier-20261028-level6-226-ratio-endpoint-independent-replay-v1.json` | 8 | `66e4b913eed12bcaac90768751402a72adcfaab20208fb3bbf992775a4699ffa` |

Actual lower-witness replay returned PASS by **19:06:50 PDT**; the 719/160 upper replay returned `PASS ... 68 exact positive leading-principal determinants` by **19:07:56 PDT 2026-10-28**. The original 235-row/source replay and all prior code/data are required inputs; the present addendum is not an independent proof of those earlier objects. Generic local exact-linear-algebra helpers are shared.

The earlier incidental old cone-status methodological exposure, the separate `(4,4,6)` staged-replay status, and all historical ZERO/STOP/HOLD/process findings remain as disclosed. No actual-map optimality, F6/B6, all-level/arbitrary-GCM result, parent adoption, novelty or priority is asserted.

**END — exact maximal coefficient for this chosen positive-semidefinite slope criterion, review pending.**
