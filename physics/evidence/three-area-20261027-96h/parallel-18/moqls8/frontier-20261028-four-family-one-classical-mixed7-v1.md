# One classical member forces seven mixed cells in any nonclassical mate

**WRITTEN author candidate; no catalogue, computation or external theorem premise. Disjoint mathematical review pending.** In any actual ordinary four-MOQLS(8) containing at least one classical member L, every other nonclassical member Q has **at least seven mixed cells** relative to any Q basis line among the rows, columns and L-symbol lines. The other two members R,S are arbitrary complex QLS. “Mixed” means not a ray of that chosen Q line basis. This is a q3-relevant structural restriction, not a full q3/q4 exclusion, M(8) statement, A10/A11 result or novelty claim.

## 1. Three-net ONBs and mixed-line facts

The rows, columns and classical L-symbol classes form a three-net. Q,R,S are actual ONBs on each such line: on an L-symbol line the classical ray is the same, so the relevant pair-product orthogonality forces their rays pairwise orthogonal. Any two cells share at most one net line. Choose any net line as row 0; independently normalize Q,R,S and L there to coordinate rays e_j with common labels j.

A line containing a mixed Q ray contains at least two mixed cells. On any coordinate used by a mixed ray, its squared coefficient is strictly below 1, no same-line singleton can use that coordinate, and ONB completeness forces another mixed ray. If a line has exactly two mixed rays, its six light singleton rays occupy six distinct axes, so the mixed rays lie in the same two-dimensional complement and have the **same two-coordinate support**. If a line has exactly three mixed rays, they lie in a three-dimensional complement and at most one has support size 2: two distinct 2-subsets of three axes intersect once and cannot be orthogonal; two orthogonal rays with the same 2-support force the third to be the remaining singleton.

## 2. Fewer than six mixed cells are impossible

Pick any mixed point x. Each of the three net lines through x contains another mixed point, and those points are distinct. Thus there are at least four mixed cells.

If exactly four existed, write them x,y_1,y_2,y_3, one y per class through x. At each y_i, its other two class-lines must contain the other two y points, so the mixed-cell graph is K4 and every mixed line has exactly two points. The two-line lemma propagates one common two-axis support over the connected graph, but a triangle of mutually orthogonal nonzero rays cannot lie in two dimensions. Thus four is impossible.

If exactly five existed, a net class cannot have all five on one line: any point on that line needs mixed neighbors on its two other class-lines, which would have to be outside. Since no mixed line is a singleton, the class partitions the five as 3+2. Choose a support-3 Q ray x from the three-point line; such a ray exists by the three-line lemma. Each of x's two other net lines must contain at least three mixed points, because a two-mixed line would force x's support to have size 2. Those lines intersect only at x and each requires two distinct outside mixed points; only two outside points exist. Contradiction.

## 3. Six mixed cells force an actual K3,3 trade

Suppose there are exactly six mixed points H. No net line contains four or more: if L contains k mixed points, each of its points needs at least one neighbor on each of two other classes, giving at least 2k cross-adjacencies. Each of the 6−k outside points is adjacent to at most two points of L, one per other class, so k≤6−k and k≤3. Thus each net class partitions the six as `2+2+2` or `3+3`.

A `3+3` class is impossible. Pick a support-3 ray x from one triple. Each of its other two net lines must contain at least three mixed points; it cannot contain another point of x's parallel line, nor two points of the other parallel triple, because any two cells share at most one line. Such a line can contain at most x plus one other mixed point. Contradiction.

All net lines therefore meet H in 0 or 2 cells. The mixed-cell graph is 3-regular on six vertices and connected, since every component has at least four vertices. Along each edge, Q's two mixed supports coincide and have size 2. Thus all six Q rays have the same two-axis support `{a,b}`. Orthogonality in C² alternates between one ray and its unique perpendicular ray, so the connected graph is bipartite; a 3-regular bipartite graph on six vertices is K3,3. Within either part Q rays are collinear, and across the parts every pair shares an actual net line.

## 4. The other two members rule out the six-cell case

For R, any two H cells in opposite parts share a net line, so their R rays are orthogonal. Any two in the same part have collinear Q rays, so Q⊗R product orthogonality forces their R rays orthogonal. Hence the six R rays on H are pairwise orthogonal. Every Q ray on H overlaps both first-row Q axes a,b; comparing Q⊗R products with the first-row products at a,b forces all six R rays into the six-dimensional complement of first-row R axes a,b. They therefore form an ONB of that complement. Exactly the same argument applies to S.

Every row meets H in 0 or 2 cells, so the six mixed cells occupy exactly three rows. In each of the other five rows Q is entirely light and, being an ONB, contains both e_a and e_b; at least four of those rows are off the first row. Choose an off-first-row cell y with Q_y=e_a. Since every Q_H ray overlaps e_a, product orthogonality forces R_y orthogonal to all six R_H rays. Those rays span the complement of `{e_a,e_b}`, hence `R_y∈span{e_a,e_b}`; similarly `S_y∈span{e_a,e_b}`.

At y, product orthogonality with the first-row Q⊗R and Q⊗S products at a forces both R_y and S_y orthogonal to e_a. Each is therefore the ray e_b. But their product at y then equals, up to phase, the R⊗S product at first-row column b, contradicting the actual R⊗S product ONB. Thus six mixed cells are impossible.

Combining the cases gives **at least seven** mixed cells for Q. In a q3 four-family, all three nonclassical members obey the bound, giving at least 21 mixed-cell incidences and at least 21 units of summed off-first-row support surplus. These incidences can overlap across members; the local upper surplus budget remains three per off-row cell. This is a necessary all-variable bound, not a completed q3 exclusion or a physical witness.

The proof relies on no previously held result, source classification or solver outcome. A disjoint reviewer should reconstruct the three-net line lemmas, the six-cell graph/connectivity, the two six-dimensional ONB spans and the final off-row/first-row product contradiction before adoption.
