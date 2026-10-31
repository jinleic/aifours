# Order ten: no Fourier transversal for any 2×5 Diţă matrix, even after arbitrary source-row reordering

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:18:44 PDT 2026**. This is a genuine restriction on the original order10 search, but it neither constructs nor excludes an unrestricted 1RQLS(10).

## 1. Statement and named import

Let A,B be ANY 5×5 complex Hadamard matrices, and Delta ANY diagonal unitary. Form the order10 Diţă matrix

`K = [[A, Delta B], [A, -Delta B]]`.

For EVERY permutation of K's ten source rows, and arbitrary row/column phases and column permutations, the ordinary cyclic Fourier-product QLS

`psi_(r,c)(tau) = 10^(-1/2) zeta10^(r tau) K_(tau,c)`

has NO orthogonal transversal, even if the array contains repeated rays. This includes a continuous set of non-Butson matrices. It does NOT classify general 10×10 Hadamards, the distinct 5×2 Diţă orientation, arbitrary Fourier-product K, or unrestricted order10 QLS.

**Imported theorem:** Haagerup's uniqueness of the complex Hadamard matrix of order5 up to row/column permutations and unit phases; see [Szöllősi, *Construction, classification and parametrization of complex Hadamard matrices*, Introduction](https://arxiv.org/html/1110.5590v1), which attributes the uniqueness theorem to Haagerup. Without this import, the computation proves the literal two-F5-block statement below only.

## 2. Reduction to finitely many symbolic branches

Use the import and absorb independent row phases of B into Delta. Up to harmless common source-row phases and independent column gauges/permutations, write

`K_(a,t;0,b)=zeta5^(t b)`,  `K_(a,t;1,c)=(-1)^a delta_t zeta5^(sigma(t)c)`,

where `a in {0,1}`, `t,b,c in Z5`, sigma is a permutation of Z5, and the five `delta_t` are arbitrary unit complex numbers. An affine transformation of sigma's values merely reorders/phases the second block's columns; choose `sigma(0)=0,sigma(1)=1`, leaving exactly six possibilities. Cyclic source-coordinate rotation, a cyclic reindexing of t, and independent swaps of the two source rows in each t-pair (the last absorbed into the delta signs) allow coordinate0 to occupy the first member of the t=0 pair. Thus all 10! source-row orders are covered by 22680 labeled position pairings `(p_t,q_t)` with `p_0=0`, `p_t<q_t`, times the six normalized sigmas. The arithmetic is `9*28*15*6*1=22680`; independent code instead permutes the other nine literal source labels and retains the canonical pair orientation.

For a putative transversal, let f_b and g_c be its physical rows in the first and second five-column blocks. These are disjoint 5-tuples covering all ten physical rows. A common physical row translation is a common diagonal unitary, so set `f_0=0`. The ten within-block Gram constraints have the exact form

`S_h(d,k)=sum_t zeta5^(pi_h(t) k) [zeta10^(d p_t)+zeta10^(d q_t)]=0`,

with `pi_0(t)=t`, `pi_1(t)=sigma(t)`, `d` the row difference and `k` the column difference. These impose no delta dependence and are exhaustively checked before the cross-block test. The remaining 25 cross-block conditions are the linear system `M delta=0`, with

`M_(b,c;t)=zeta5^(sigma(t)c-tb) [zeta10^((g_c-f_b)p_t)-zeta10^((g_c-f_b)q_t)]`.

All identities and the normalization preserve orthogonality and the one-per-row/column transversal condition.

## 3. Exact branch certificates

There are **136080** `(source pairing,sigma)` cases, **82560** first-block configurations and **224200** compatible two-block configurations. All are excluded:

1. **220200** have rank5 over F31 after `zeta10 -> 15`. A nonzero 5×5 minor in this reduction is a nonzero exact algebraic minor, so `M delta=0` has no nonzero solution.
2. **3200** have four independently certified constraint rows. For an invertible 4×4 pivot D and replacement determinant N, a unit-modulus solution would give `N conjugate(N)=D conjugate(D)`. An explicit differing residue at the root and conjugate-root embeddings proves this algebraic equality false, regardless of whether the full matrix has larger rank.
3. **800** have three independently certified rows. Exact cyclotomic replacement determinants vanish for BOTH free columns of one pivot coordinate, forcing that delta coordinate to be zero, contrary to unimodularity. The pivot minor is nonzero in the relevant finite-field reduction, so Cramer's rule applies over Q(zeta10).

The first checker `frontier-20261028-n10-dita-arbitrary-block-rank-scan-v2.cpp` SHA **ca7df7586a3b3da92dc2a5195c6c6f0445ef857fa7a07513a42f4aaf9d5fbffd**, result SHA **92c4363096df4b3eef457d3157b045433abb93552138e69d91a33808a4ed24c8**, uses Z[zeta10] same-block Grams and mod31 cross-rank filtering. The independent `frontier-20261028-n10-dita-arbitrary-block-independent-v1.cpp` SHA **c451219464ab66c8b745937b92c50731698df1bb54a96f4ea34a762486c8f223**, result SHA **5a949974fcd5e1508bccfab9b6fa4df6b1c34e8acdcea4ff7df3d61ecb1a0e63**, uses signed fifth-root counts, a different source-order enumeration, prime41 for rank/norm witnesses, and exact `Z[zeta5]/(1+x+x²+x³+x⁴)` determinants for the zero-coordinate cases; it reports precisely **220200/3200/800**, **0 unresolved**. `frontier-20261028-n10-dita-arbitrary-block-coverage-comparison-v1.py` SHA **6611028d7b17b8e275309894a7a695bc73af285edc1333aea237cf60a39ecead**, result SHA **863c4401d6684e30a5cdaa8135236b6531fb405963ce1e3a106fcfe9e180d4ce**, checks the per-order f/g/full/low counts for all136080 cases and matches all4000 literal low-rank branch keys and ranks. Matching aggregate/per-order counts alone is not an independently checked equality of every full-rank branch; the separate complete enumeration and exact checks are the evidence.

## 4. Error disclosure and boundary

The earlier exploratory `frontier-20261028-n10-dita-lowrank-modulus-v1.py` incorrectly treated a modular linear-rank increase 0→1 as sufficient for characteristic-zero inconsistency on the 800 rank3 cases. That conclusion was withdrawn immediately in `frontier-20261028-n10-dita-modulus-caller-correction-v1.json` SHA **3131080b8fa43287fb78184612ead668c3e87cd209d011024ef76b8e7892039b**. It is NOT an input to the proof. An exact successor `frontier-20261028-n10-dita-rank3-exact-zero-v1.py` SHA **5c8f9d0d4e95f0a507662af2f3fe353ea3e8f824af796fc82edaaac3f7ffde8f**, result SHA **380611bbd2d5da61fed3162ed5a14e7f51bd95352a7dc7e6c2c9974d5832eb01**, exhibits zero-coordinate determinants on all800 previously affected branches; the independent arbitrary-block replay separately checks them in the fifth-root basis. The defective preliminary bytes are preserved.

This is exact computation plus a written reduction and named external classification theorem; it is not formal verification, cross-model/human review, or a novelty assessment. Full independent review of the matrix normalization, branch coverage, modular-to-characteristic-zero logic and original-vector caller is requested.
