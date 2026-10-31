# Any nonclassical member of three mutually orthogonal QLS has at least eight mixed cells

**WRITTEN author candidate; no classical-mate, catalogue, numerical solver or finite-witness premise. Disjoint mathematical review pending.** For any ordinary set of at least three mutually orthogonal QLS of order n, choose any member Q, any actual Q row and its n rays as a coordinate ONB. If Q is nonclassical then at least **eight** of its n² cell rays are not coordinate rays of that row. The other QLS may be arbitrary complex and nonclassical. For n<4 the conclusion is understood conditionally and may be vacuous.

In particular, in an actual four-MOQLS(8), every nonclassical member has at least eight mixed cells even if **none** of the other members is classical. Thus a q4 family would have at least 32 mixed-cell incidences and at least 32 summed support-surplus units; q3 would have at least 24. These incidences may overlap, so this is a universal necessary lower budget, not an M(8), q3/q4 exclusion, A10/A11, novelty or formal-review claim. The exact three-member example in `frontier-20261028-two-classical-mixed8-sharp-v1.md` SHA256 867bc6deb512ab74e3779f5489b05a852dc7d4097cb1a8900d80064d8ac9e899 attains eight, conditional on its separately verified physical witness; it is not used as a proof premise or as a four-family witness.

## 1. Mixed rows, columns and the two-line lemma

Independently normalize the chosen first row of Q and of two other actual orthogonal members R,S to their own coordinate rays e_0,...,e_(n−1), with common column labels. A Q cell is *light* if its ray is one of Q's first-row basis rays and *mixed* otherwise. Nonclassicality is equivalent to at least one mixed cell because the chosen row already contains a complete basis.

Any row or column containing a mixed Q ray contains at least two mixed cells: on an occupied coordinate, the mixed ray's squared coefficient is strictly below 1, no light ray on that same line can use the coordinate, and ONB completeness forces another mixed ray there. If a line has exactly k mixed rays, its n−k light rays occupy distinct coordinate axes, so the mixed rays form an ONB of the complementary k-dimensional coordinate space. In particular, exactly two mixed rays have the **same two-coordinate support**; on a three-mixed line, at most one ray has support size 2. The latter follows because distinct 2-subsets of three coordinates meet in one axis and cannot be orthogonal, while two orthogonal rays on the same 2-support force the third ray to be the remaining singleton.

## 2. Four and five mixed cells are impossible with one mate

The bipartite graph with mixed rows and mixed columns as vertices and mixed cells as edges has minimum degree at least two. Therefore there are at least four mixed cells. With exactly four, the graph is a 2×2 rectangle. The two-line lemma propagates one common two-axis support `{a,b}` to all four mixed Q rays; their row/column orthogonality graph is K2,2 and its two parts carry two collinear Q rays in perpendicular directions.

The four R rays on that rectangle are pairwise orthogonal: opposite K2,2 parts share a row or column, while same-part Q rays overlap and the Q⊗R product ONB forces R orthogonality. The rectangle occupies two Q rows. Every other row contains only light Q rays and therefore contains e_a exactly once, giving **n−2** light e_a cells. Their R rays are mutually orthogonal because their Q rays are collinear; each is also orthogonal to all four rectangle R rays because every mixed Q ray has nonzero overlap with e_a. This would give `4+(n−2)=n+2` pairwise orthogonal R rays in C^n. So four mixed cells are impossible whenever Q has even one orthogonal QLS mate.

With exactly five mixed cells, minimum degree two gives at most two incident rows and at most two incident columns, but a 2×2 grid has at most four cells. So five is impossible for any QLS.

## 3. Six mixed cells are impossible with two mates

Suppose there are exactly six mixed cells. Minimum degree two permits either a 2×3 complete rectangle, a 3×2 complete rectangle, or three incident rows and three incident columns each of degree 2. In the 2×3 case, every mixed column contains exactly two mixed rays and therefore all six Q rays have support size 2. But each of the two three-mixed rows has at most one support-2 ray by §1, contradiction; the 3×2 case is symmetric.

In the remaining case the row/column graph is a single six-cycle. Every mixed row and column has exactly two mixed rays, so the two-line lemma propagates one common two-axis support `{a,b}` around the cycle. Its Q rays alternate between two perpendicular one-dimensional rays. Label the two bipartition parts `p_1,p_2,p_3` and `n_1,n_2,n_3` so the row/column graph is `K_(3,3)` minus the three pairs p_i,n_i.

For R, its three p-rays are pairwise orthogonal and its three n-rays are pairwise orthogonal, because the corresponding Q rays are collinear within each part. For i≠j the cells p_i,n_j share a row or column, so their R rays are also orthogonal. The six mixed cells occupy exactly three Q rows. In each of the other n−3 rows all Q cells are light, so there is exactly one Q=e_a cell. The corresponding n−3 R rays are pairwise orthogonal by Q⊗R, and each is orthogonal to every R ray on H because every mixed Q ray has a nonzero e_a coefficient. Thus all six R_H rays lie in a subspace of dimension at most 3. The two orthonormal triples therefore span the same three-dimensional space. Cross-orthogonality for i≠j makes each R_(n_i) collinear with R_(p_i).

The identical argument applies to S. At each nonedge p_i,n_i, both R rays are collinear and both S rays are collinear. Their R⊗S product vectors consequently have nonzero overlap, contradicting the actual R⊗S product ONB. Thus six mixed cells are impossible when Q has two other mutually orthogonal QLS mates.

## 4. Seven mixed cells are impossible even for one QLS

If exactly seven mixed cells existed, minimum degree two gives at most three incident rows and at most three incident columns. A 2×3 or 3×2 grid has at most six cells, so there are exactly three of each. The mixed-cell graph is a 3×3 grid with seven edges and minimum degree two, hence the two missing edges form a matching. Both row degrees and column degrees are `(3,2,2)`.

The degree-3 row contains two cells in degree-2 columns. The two-line lemma forces both those Q rays to have support size 2, but the three-line lemma permits at most one support-2 ray on a three-mixed ONB line. Contradiction.

The cases below eight are exhausted. This is an all-variable written argument using only the actual QLS and pair-product ONBs; it does not use the special explicit three-member witness, a source-classification theorem, a selected instance, or a solver. A disjoint reviewer must check the m=6 graph/three-dimensional span and R⊗S nonedge argument before adoption.
