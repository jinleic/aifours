# The non-Diţă conference three-phase family has no Fourier transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:30:21 PDT 2026**. This is an all-phase original-order family result, not a universal even-order or unrestricted 1RQLS10 no-go.

## 1. Explicit source and statement

Take the symmetric conference-derived matrix D10 and its three-parameter affine deformation from [Szöllősi, *Parametrizing Complex Hadamard Matrices*, §4](https://arxiv.org/html/math/0610297v1#S4), as reproduced below. Let A,B,C be arbitrary unit complex numbers. Starting with

```text
D10 =
1  1   1   1   1   1   1   1   1   1
1 -1  -i  -i  -i  -i   i   i   i   i
1 -i  -1   i   i  -i  -i  -i   i   i
1 -i   i  -1  -i   i  -i   i  -i   i
1 -i   i  -i  -1   i   i  -i   i  -i
1 -i  -i   i   i  -1   i   i  -i  -i
1  i  -i  -i   i   i  -1  -i  -i   i
1  i  -i   i  -i   i  -i  -1   i  -i
1  i   i  -i   i  -i  -i   i  -1  -i
1  i   i   i  -i  -i   i  -i  -i  -1
```

multiply its entries by the corresponding monomials below:

```text
1  1    1    1   1     1  1     1   1    1
1  1    A/B  A   C^-1  1  C^-1  A   A/B  1
1  B/A  1    B   C^-1  1  C^-1  B   1    B/A
1  A^-1 B^-1 1   1     1  1     1   B^-1 A^-1
1  C    C    1   1     1  1     1   C    C
1  1    1    1   1     1  1     1   1    1
1  C    C    1   1     1  1     1   C    C
1  A^-1 B^-1 1   1     1  1     1   B^-1 A^-1
1  B/A  1    B   C^-1  1  C^-1  B   1    B/A
1  1    A/B  A   C^-1  1  C^-1  A   A/B  1
```

The resulting K is complex Hadamard for all phases: both exact implementations check all90 row/column Gram pairs as Laurent identities. For EVERY A,B,C, EVERY source-row permutation and arbitrary row/column gauges/permutations, its ordinary cyclic Fourier-product QLS has NO orthogonal transversal, including when rays repeat.

Generically this family lies outside both order10 Diţă orientations: the independently checked symbolic source-row and source-column ratios have no pair with multiplicity pattern 5+5, whereas the 2×5 and 5×2 constructions respectively require five disjoint such row or column pairs. The qualifier excludes special phase coincidences; the no-transversal result does not. Source §4 also proves that the undeformed conference matrix itself is non-Diţă.

## 2. Three-term rigidity and the finite caller

As in `frontier-20261028-n10-nondita-affine-a30-allphase-no-transversal-v1.md` SHA **586014909b52ba5854a41979be9ac900295da4914a2fbdae70af1ad31dc2cf03**, pair the transversal rows r,r+5. The resulting column matching must consist of zero half-Grams on one five-source-coordinate subset E, and by ordinary column orthogonality E and its complement have identical halfgraphs. Among the 126 subsets containing source row0, exact monomial/binomial impossibility filters leave 16 with matchings, **3072** candidate matchings in all.

For each candidate matching the exact caller selects three integer exponent-difference vectors from its matched half-Gram polynomials. Each selected vector comes from a THREE-TERM polynomial whose three nonzero coefficients differ only by fourth roots of unity. Since A,B,C are unit, vanishing of such a polynomial forces the ratio of either nonbase monomial to the base monomial to lie in mu12: three equal-length complex numbers summing to zero are rotations of `1,zeta3,zeta3²`.

The three selected exponent vectors form a 3×3 integer matrix V with `|det V|=1` in **2864** cases or `2` in **208** cases. If each corresponding monomial is in mu12, the adjugate identity gives `A^det(V),B^det(V),C^det(V) in mu12`. Thus in all cases **A,B,C are 24th roots of unity**. This implication is necessary only; the proof does not assume the surviving matching is actually feasible.

Consequently all entries of K lie in `Q(zeta24)`, over which Phi5 is irreducible. Exactly as in §3 of the cited A.30 packet, three selected cells in the same physical-row parity and different columns would force three pairwise orthogonal nonzero two-coordinate column restrictions, impossible in C². Any order10 transversal has five cells of each row parity and distinct columns, contradiction.

## 3. Exact and independent checks

`frontier-20261028-n10-d10-affine-halfgraph-v1.py` SHA **86d2bfe9eef2eb0dfacdba177d412afd55f4c80a788ae193e2b367f02f6edfcd**, result SHA **993b97ad09a2e559a454bf4283b003bc9ab569f0b9e6cce07e548568c56ccb30**, reconstructs source matrix and original symbolic Grams in Z[i]. `frontier-20261028-n10-d10-cube-rigidity-v1.py` SHA **292756e9e0509f281600469694a9759dc03eda08c995ea1daa038d98751e28c4**, result SHA **ad8e47d2afe6e7df154b8f6d2c85913d41facc0deb5f13ba05bcd6a5d7020640**, records the exponent-vector/edge/determinant witness for every candidate matching.

Independently transcribed `frontier-20261028-n10-d10-cube-independent-v1.py` SHA **675a43dc6a32a23e333fb68f4c3fc37308a33f81f10d255f7a7dc512d433c2fa**, result SHA **e3cc78e99ea0e4499b95dea5ec85a328451489e5862a75f4407aecb035aeb67e**, uses four residue counts before reducing in Z[i], exhausts ALL252 halves and ALL945 perfect matchings per half, and independently obtains 5728 determinant1 and 416 determinant2 cases, none unresolved. `frontier-20261028-n10-d10-cube-coverage-v1.py` SHA **71f4a7c00dd33fa29f32c8ef6bb24124c60a6e343dd21bbff55ac6ca9e23c53a**, result SHA **df925cbafc6c9d5a980e6cedb55f345319caba9240c8b7786444515ea13057da**, matches all3072 `(E,matching)` keys and chosen determinant magnitudes between the two algorithms.

This is exact computation plus written mathematics, not a formal or external-model proof and not a novelty clearance. Independent review of both literal transcriptions, all-matchings coverage, rigidity implication, source-order halfgraph caller and field obstruction is required. Nothing here excludes arbitrary K or unrestricted QLS10.
