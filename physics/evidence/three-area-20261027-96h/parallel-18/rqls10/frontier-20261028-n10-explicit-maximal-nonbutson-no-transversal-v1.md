# A literal maximal non-Butson QLS10 with no transversal

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:34:24 PDT 2026**. This is an explicit 100-ray QLS10 with NO transversal, not the requested 100-ray 1-resolvable construction and not an unrestricted no-go.

## Construction

Let `b=(-1-i sqrt15)/4`, so `|b|=1`, `2b²+b+2=0`, and `b+conjugate(b)=-1/2`. Set `K_(t,c)=b^E_(t,c)` with the following literal exponent matrix, transcribed from [Bruzda's Y_10_0_9A.m](https://github.com/matrix-toolbox/chm/blob/main/CHM_SINKHORN/Y_10_0_9A.m):

```text
0 0 0 0  0  0  0  0  0  0
0 2 4 4  1  2  3  0  2  2
0 4 4 2  2  0  3  2  1  2
0 4 3 4  2  2  1  2  2  0
0 2 2 1  0  0 -1 -2 -2  0
0 0 2 2  0 -1  1  0 -2 -2
0 2 0 2  0 -2  1 -2  0 -1
0 3 1 3 -1  1  2  1 -1  1
0 2 2 0 -2  0  1 -1  0 -2
0 1 2 2 -2 -2 -1  0  0  0
```

Define the QLS rays by `psi_(r,c)(t)=10^(-1/2) zeta10^(r t) K_(t,c)`. The 10 rows and 10 columns are orthonormal bases because K is Hadamard and unit-modulus. For EVERY ordering of K's ten source rows, these 100 rays are pairwise distinct and there is NO orthogonal transversal.

## Why the 100 rays are distinct

b is not a root of unity: otherwise `b+1/b=-1/2` would be a rational algebraic integer. If two distinct cells shared a ray, then comparing their coordinate ratios with coordinate0 would give an integer power of b equal to a tenth root of unity. Non-root status forces that power to be zero, and hence the physical-row difference must be zero. The cells would then be in the same row and different columns, which are orthogonal, contradiction. Source-row permutations preserve this reasoning. Thus this is maximal in the ray-count sense, despite having no transversal.

## No transversal and genuinely non-Diţă/non-Butson

K has entries in the conjugation-stable imaginary quadratic field `Q(sqrt(-15))`. Its intersection with `Q(zeta5)` is Q: the unique quadratic subfield of Q(zeta5) is real Q(sqrt5). Hence Phi5 is irreducible over the entry field. The m=2,p=5 case of `frontier-20261028-large-prime-field-fourier-obstruction-v1.md` SHA **3348a6acd5876859722d980c20ec42433c4b7a6e91fa274fa34ba8a4e40fe286** excludes any transversal for every source order.

The dephased cross-ratio b is not a root of unity, so K is outside ALL Butson monomial equivalence classes. Exact source exponent ratios show no row pair and no column pair with multiplicities 5+5; because b is not a root of unity, distinct exponent differences give distinct complex ratios. Every 2×5 Diţă matrix requires five disjoint 5+5 row pairs, and every 5×2 Diţă matrix requires five disjoint 5+5 column pairs. Thus this literal K is outside both order10 Diţă orientations, without a generic-parameter qualification.

## Exact evidence and limits

`frontier-20261028-n10-qminus15-isolated-matrix-v1.py` SHA **a1925c7cab0ab60cfcb2ef6e9ffe8126a304a1062c0b712706b58ae3dfa143bd**, result SHA **7b92d371b3ac4c5a7539117fffa36106f4f862eeecf8ea23f14a4de279b41cbc**, verifies all45 K-row and45 K-column Gram identities in Q(b) using `2b²+b+2=0`. Independently transcribed `frontier-20261028-n10-qminus15-isolated-replay-v1.py` SHA **86647eb27274fe99b4069c7736af131f1d6a6a577edb8a6a66b07a9d8687c2f8**, result SHA **ee5652480110b62fddb15a533a2defa6c0b92358f4d624bfa619999063e58055**, uses integer-scaled Q(sqrt(-15)), checks all100 norms,90 row/column Gram pairs and ratio multiplicities; the two recorded exponent matrices match exactly. Distinct rays and the field no-go are the written arguments above, not a numerical overlap search.

The upstream file describes the matrix as isolated, but that classification is not needed or independently checked here. The source transcription, field no-go, ray-distinctness and Diţă ratio caller require independent review. This does not decide whether some OTHER 100-ray QLS10 is 1-resolvable.
