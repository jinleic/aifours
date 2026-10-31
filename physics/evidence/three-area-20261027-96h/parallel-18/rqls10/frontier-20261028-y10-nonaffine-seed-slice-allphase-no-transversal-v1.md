# A one-parameter slice of a nonaffine CH10 family has no transversal

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:42:26 PDT 2026**. This is a literal one-parameter slice, not a claim for the entire three-parameter nonaffine family or unrestricted QLS10.

## Source, explicit slice, scope

In [Bruzda's Y_10_3_278.m](https://github.com/matrix-toolbox/chm/blob/main/CHM_SINKHORN/Y_10_3_278.m), take `a=1`, `b=zeta3`, and the displayed principal radical branches. Exact substitution yields `u=1`, `q=-1`, `r=zeta3²`, `s=zeta3`, `t=zeta3`; the remaining parameter c is an arbitrary unit complex number. With `w=zeta6`, the resulting K(c) has entries `w^E_(t,j) c^X_(t,j)` where

```text
E =
0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 1 1 3 3 3
0 0 3 2 4 2 4 0 3 0
0 0 3 4 2 4 2 0 0 3
0 4 3 0 0 3 0 2 2 4
0 2 5 2 2 2 5 4 0 4
0 4 0 0 3 3 3 2 5 1
0 2 2 5 2 5 5 4 3 1
0 3 3 3 5 0 2 3 0 0
0 3 0 2 0 5 3 0 3 3

X =
0 0 0 0 0 0 0 0  0  0
0 0 0 0 0 0 0 0  0  0
0 0 0 0 0 0 0 0 -1 -1
0 0 0 0 0 0 0 0 -1 -1
0 0 0 0 0 1 1 0  0  0
0 0 0 0 0 1 1 0  0  0
0 0 0 1 1 0 0 0  0  0
0 0 0 1 1 0 0 0  0  0
0 0 1 1 1 1 1 1  1  1
0 0 1 1 1 1 1 1  1  1
```

All90 row/column Gram identities hold as exact Laurent identities in unit c. For EVERY c, EVERY source-row order and arbitrary source gauges/column permutations, the order10 cyclic-Fourier-product QLS has **NO orthogonal transversal**. If c is not a root of unity, the QLS has **exactly100 distinct rays**, and K(c) is outside every Butson class and both Diţă orientations. By transpose duality, K(c)^T also has no transversal for every source order; no inequivalence of the transposed family is asserted.

## Halfgraph proof for all c

Pairing transversal physical rows r,r+5 gives a perfect matching of columns whose five-row half-Grams all vanish; E and its complement have the same halfgraph. For all126 five-subsets E containing source row0, discard nonzero monomial half-Grams and binomials whose coefficient norms differ. The remaining graph has matchings for 52 subsets and **520** possible `(E,matching)` pairs. Every such matching contains a witnessed half-Gram of the form `c^k (A+B c)` with nonzero A,B in `Q(zeta6)`. Hence any actual transversal forces `c=-A/B in Q(zeta6)`. The resulting K belongs to the conjugation-stable field Q(zeta6), where Phi5 is irreducible; the p=5,m=2 large-prime field theorem `frontier-20261028-large-prime-field-fourier-obstruction-v1.md` SHA **3348a6acd5876859722d980c20ec42433c4b7a6e91fa274fa34ba8a4e40fe286** then excludes a transversal. This covers even the exceptional algebraic phases.

## Maximality and non-Diţă for every nonroot c

The dephased cross-ratio `-c` is nonroot, excluding every Butson monomial class. The exact formal ratio scan finds NO row or column pair with ratio multiplicities 5+5; for nonroot c the formal monomials coincide only when both exponents match, so this excludes both Diţă orientations.

Suppose two QLS rays coincide. Comparing their components at each source position against coordinate0 gives `c^k` equal to a 30th root of unity. Nonroot c forces k=0, so the two K-column ratios differ only by sixth roots. For distinct physical rows, the cyclic Fourier ratio must belong to `mu6 intersect mu10=mu2`; its row difference is then 5. But the resulting alternating ± pattern would require a 5+5 source-column ratio pair, which does not exist. For equal physical rows the two distinct columns are orthogonal. Therefore no two cells share a ray, for every source-row order.

## Exact evidence and boundary

`frontier-20261028-y10-nonaffine-seed-v1.py` SHA **7438c1258c1b9da11432788bf32d1b1461e342915675f0da2af2a73cbe18238b**, result SHA **3cc8a22262c7766ff74375b3042e35acd563a02668a3c7b9c13b0cf6804457eb**, checks the seed radical squares and exact auxiliary values in Q(zeta6); the independent seed replay SHA **db16e99a630165cc8dbd3cafa863967b81ecacff1ae98db2512e9bc33e62f2f8**, result SHA **ab66766b4362d5c479141ea1f9290c8b52c777d67cb84f91fb51eb4dae05e390**, verifies the literal seed Gram matrix in a different basis.

The slice census `frontier-20261028-y10-seed-slice-halfgraph-v1.py` SHA **b25f8f44be4c0bccb4a20e5fc48e3e6eb3fa7db30eac943d7b33509138f3243d**, result SHA **93ba57af7cf7e8d13f5be266f2ab6ad9f6c9d82c3d9acbbc428b6879690a0662**, checks all90 symbolic Grams and emits each binomial witness. Independent `frontier-20261028-y10-seed-slice-independent-v1.py` SHA **4b1f3880922d7c42a87d838a5ae35361f6cf9a9bacb0f9cabc241bd1acd21b1b**, result SHA **943c6b5cbb524f876a0735cd02956ef01eabf4fdcb0a8cfe431642de57f46ba6**, uses the different Z[zeta3] basis, checks all252 halves and 945 matchings per half, obtaining1040 forced-field matches. The literal 520 keys/witnesses agree by `frontier-20261028-y10-seed-slice-coverage-v1.py` SHA **a5f490a9207f86839c24d50f3e01a770e712f7379523d67104dac2ac719feaf8**, result SHA **e3f3f677803a61bc3cc3a1c8812327ee7f5c980b94fe0c36fa31b92d801c4e8e**.

All source, branch, original-Gram, halfgraph, ray-distinctness and field callers need independent full review. This written/computer-assisted candidate is neither formal nor a novelty claim; it does not construct 1RQLS10.
