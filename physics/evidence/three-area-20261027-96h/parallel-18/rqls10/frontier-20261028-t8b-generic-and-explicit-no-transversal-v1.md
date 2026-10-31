# A non-affine order-eight family and an explicit non-Butson QLS

**WRITTEN / EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:22:05 PDT 2026**. This reaches a non-affine Hadamard family beyond the full 2×4 Diţă family and beyond all finite Butson classes. It does NOT settle the even-order Fourier-product question.

## 1. Generic no-T result for the actual non-affine family

[Valtonen Proposition3.2](https://arxiv.org/html/2505.22947v1) gives the 3-parameter non-affine `T_8B(a,b,c,d)` complex Hadamard family with unit parameters and

`d=(1+ab+ac+bc)/(a+b+c+abc)`

whenever the denominator is nonzero. If a,b,c are algebraically independent unit complex numbers over Q, then the generated conjugation-stable field `F=Q(a,b,c)` contains all entries and their conjugates (because conjugation sends each unit parameter to its inverse). Its purely transcendental extension contains no new algebraic constants, so `Phi8` remains irreducible over F. The prime-power field theorem `frontier-20261028-prime-power-fourier-field-obstruction-v1.md` SHA **ad1efe46cb9c4c7fc2c9856e8e4e11f63ec53c9de752154c3d7b91c78824b04c** therefore rules out ANY Fourier-product transversal.

The algebraically dependent triples form a countable union of proper polynomial zero sets and have Haar measure zero on the three-torus. Thus **Haar-almost-every** parameter triple of this non-affine family has no Fourier-product T. This is a generic result, not an exclusion of dependent triples. Source Proposition3.2 is explicitly imported for its exact Hadamard-family assertion; its excluded denominator-zero set is not silently included.

## 2. A fully checked explicit point outside all Butson and 2×4 Diţă classes

Take `s=zeta6`, `a=b=c=s`, and `d=(5+3s)/7`. Direct exact arithmetic gives `d=(1+ab+ac+bc)/(a+b+c+abc)`, with nonzero denominator `3s−1`. The corresponding literal T8B matrix is in the checker below. Every entry lies in Q(zeta6), so Phi8 is irreducible over that field by coprime-conductor cyclotomic disjointness. Consequently the Fourier-product QLS8 has NO T, for ANY K-row order and phases, by the same written field theorem. For the source's displayed row order it is an actual maximal-cardinality QLS8 with **64 distinct rays**, but NOT a 1-RQLS8.

The point is not monomially equivalent to ANY finite-Butson matrix: `d+conj(d)=13/7` is rational but not an integer, so d cannot be a root of unity. The matrix is dephased, and the 2×2 cross-ratio from source rows0,1 and columns0,2 equals `-d`, a nonroot-of-unity invariant under row/column phase gauges and permutations.

It is also NOT monomially equivalent to any 2×4 Diţă block matrix `[[A,B],[A,-B]]`: such a matrix must have four disjoint row pairs whose entrywise quotients take two opposite values, each four times. For this K, exact arithmetic finds **no such row pair at all**; the 28 row-pair quotient multisets have respectively4,6,8 distinct values, with counts4,12,12. This invariant survives row/column phases and permutations. No external inequivalence classification is assumed.

## 3. Original-vector evidence

`frontier-20261028-t8b-nonbutson-explicit-v1.py` SHA **6ce6e5df6b6a7901d8822971dffdc1d05c17cc05dbb5f2687664cf568701b0cd**, result SHA **9029c83002df7588d58e9b57388bb720128e08dfd5039abac9cff9d5bedb1e6f**, performs rational arithmetic in `Q(zeta8) tensor Q(zeta6)` and checks ALL64 norms,224 row Gram pairs,224 column Gram pairs and2016 ray pairs; no rays coincide. A full transversal DFS in the normalized physical-row-shift caller returns none after one node (corroboration, not the no-T proof).

Separately written `frontier-20261028-t8b-original-vector-replay-v1.py` SHA **f3a8a629b868105a2080001095a2800a4ba8471f8f816d85ea1e2ca8fc3daba7**, result SHA **84c369fc61438c56803e705da7862648143da66bd6ed0816bcb473312af988cb**, rechecks the SAME original vector conditions in the distinct exact field representation `Q[zeta24]/(x^8−x^4+1)`. `frontier-20261028-t8b-structural-invariants-v1.py` SHA **73cc5a5ef1f1c982ac552345d733c014b7ccb9a030cfae21824a70a7f34816d6**, result SHA **82bf92965b70da3a379006fd39be24bc283ef4f7de7f3f8976b8d92066df73db**, checks the cross-ratio and all28 Diţă row-pair obstructions.

The literal source formula, generic field theorem, two exact original-vector implementations and structural callers require full independent review. Other T8B parameters, other order8 Hadamards, arbitrary even n, and the original order10 100-ray 1-RQLS remain open.
