# An isolated non-Butson order-eight Hadamard has no Fourier transversal

**EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:15:35 PDT 2026**. This tests an actual even-order isolated complex Hadamard OUTSIDE every finite Butson equivalence class, not merely a root-alphabet filter or a Diţă-family instance. It is one explicit class, not a universal even-order theorem.

## 1. Primary matrix and scope

Take the isolated `A_8A` in [Valtonen, §3.2](https://arxiv.org/html/2505.22947v1#S3.SS2), with the root `a=(1+2 i sqrt(2))/3` of `3a²−2a+3=0`. Its unnormalized 8×8 entries are exactly

```text
a  1 -a  1 -a -a  a  1
1 -a  1  a -a  a -a  1
-a 1 -a  a  1  a  1 -a
1  a  a  1  1 -a -a -a
-a -a 1  1  a -a  1  a
-a a  a -a -a  1  1  1
a -a  1 -a  1  1  a -a
1  1 -a -a  a  1 -a  a
```

Every Fourier-product QLS built from this matrix has **NO orthogonal transversal**, for every source-row order, arbitrary row/column phases and column permutations, and regardless of ray repetitions. The same holds for its conjugate, because conjugating the whole array and reflecting physical row labels `r -> -r` preserves all Gram zeroes and transversal incidence.

This is truly outside ALL finite Butson monomial classes: if a were a root of unity then `a+conj(a)=2/3` would be a rational algebraic integer, impossible. The 2×2 cross-ratio from rows0,1 and columns0,1 is `-a²`, also not a root of unity; all cross-ratios are invariant under row/column phases and permutations up to reindexing. Thus no monomially equivalent matrix can have all entries roots of unity. No novelty claim is made.

## 2. Complete matching obstruction

Any transversal pairs physical rows r and r+4. Column orthogonality of K and physical orthogonality of such a pair force the corresponding two K columns to have zero inner-product sum on the four even-coordinate rows and separately on the four odd-coordinate rows. Thus the half-orthogonality graph on the eight columns must have a perfect matching.

The half graph for E equals that of its complement because complete K-column inner products vanish. It suffices to inspect the **35** four-row subsets E containing source row0, covering all70 halves. For EACH of these35 graphs there is a directly checkable obstruction:

- **27** have an isolated column;
- the remaining **8** have two degree-one columns with the same sole neighbor.

Either obstruction rules out a perfect matching. Therefore no possible source-row permutation or transversal exists; no DFS or numerical tolerance is needed for this conclusion.

## 3. Two exact calculations and limits

`frontier-20261028-isolated-a8a-product-certificate-v1.py` SHA **842fd5231de9fa915364c560bd2ce823e2f0a4c8388000c3714fd13b4e9b6f7f** reconstructs the primary matrix in Z[zeta8] with common denominator3, checks all64 unit norms and all56 row/column Gram pairs, and finds zero matching halves; output SHA **e2d6d4b7fb20bbaf8ae5683ae8cc036ddcf3d06257881d305464404949de2d89**. A separately written `frontier-20261028-isolated-a8a-halfgraph-replay-v1.py` SHA **fbbb13fa34ab64127c3aacaaf77f0d6e15d89efa41ffe492a69a1c7ca68dc8a7** uses the different integer basis `1,i,sqrt2,i sqrt2`, rechecks all original Hadamard conditions and emits every halfgraph and isolated/leaf witness; its result SHA **d33cd248616465de8a7152e1b4a54c039bde1807590b9e2c044a8dadb8261d96** has witness counts27+8.

The source transcription, exact fields, half-matching implication and witness checker need independent full review. Other isolated matrices, non-affine families and arbitrary order8 K are outside this conclusion. In particular this is not proof that every even Fourier product has no transversal, nor a resolution of the unrestricted order10 question.
