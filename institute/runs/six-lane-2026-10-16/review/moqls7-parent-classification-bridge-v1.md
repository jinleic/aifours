# MOQLS(7): direct partial-net classification bridge

Parent derivation for review. This offers a shorter imported-theorem boundary for the proposed n=7 proof; it does not independently reproduce the published classical classification.

## Primary statements read

Egan–Wanless, arXiv:1406.3681v2, Section2 (local layout text lines121–150), represents k MOLS(7) by an orthogonal array whose49 rows are `(r,c,L1(r,c),...,Lk(r,c))`. Paratopism is equivalence of these arrays under row permutations, column permutations, and independent symbol permutations within each column. Thus paratopy induces an isomorphism of the49-point net with its k+2 parallel partitions, allowing the partitions themselves to be permuted.

Table6, “Number of reduced sets of k-MOLS(n)” (local lines742–776), has the following **Paratopism** entries: one class for (n,k)=(7,3), and one class for (7,4). Section6 lines732–738 explicitly says Table6 includes non-maximal sets, unlike Table5. These are not the separate PP/DPP columns imported from the Handbook.

## Deduction

For each k=3,4, explicit linear representatives exist: use points `(r,c)` in F7² and Latin squares `L_a(r,c)=c+a*r`, a=1,...,k. Each is Latin, and two different slopes give orthogonal squares because a-b is nonzero in F7. Their row, column and symbol partitions are k+2 distinct parallel classes of AG(2,7).

Since Table6 reports a single paratopy class, **any three MOLS(7) give a five-net isomorphic to five parallel classes of AG(2,7), and any four MOLS(7) give a six-net isomorphic to six such classes.**

This directly supplies the geometric premises of the proposed TheoremsA andB:
- In A, after Lemma10 produces four classical squares, the six-net of rows/columns/symbols has the required affine representation. FactC applies to any three distinct direction classes, including the original rows, columns and any one symbol partition.
- In B, the three classical squares give the five-net to which FactL applies.

## Why no extra quantum isotopy is assumed

Paratopy is used only to identify the **classical incidence net**, not as an allowed transformation of a quantum Latin square. In A it transfers a graph property of the classical symbol cells. In B it relabels the49 points carrying vectors; orthonormality on each of the five classes is already known, and the conclusion that all vectors lie on seven rays is unchanged by relabelling points. The proof does not assert that an arbitrary net paratopy preserves quantum-square row/column isotopy.

## Resulting trust boundary

For this n=7 argument, the direct Table6 route removes the need to invoke Shrikhande's original completion theorem, Hall's plane-uniqueness theorem/correction, or Bose's complete-plane correspondence. It still imports the correctness/completeness of Egan–Wanless's reported classification and its definition of paratopy. Ball–Simoens Lemma10 (with the support-shrinking properties proved in the supplied text), the elementary support arguments, the analytic FactsC/L and the certified SAT exclusions remain necessary.
