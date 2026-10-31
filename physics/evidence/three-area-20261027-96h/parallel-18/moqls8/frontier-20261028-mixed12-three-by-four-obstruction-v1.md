# A 12-cell 3×4 mixed board has no orthogonal mate

**WRITTEN author candidate; disjoint review pending.** Let Q be an order-8 QLS and choose any actual Q row as coordinate basis. If Q has exactly 12 mixed cells on exactly three rows and four columns, then Q has no orthogonal QLS mate. The same conclusion holds for four mixed rows and three mixed columns. The proof uses actual arbitrary-complex rays and the row/column mixed-subspace projectors, with no catalogue, classical mate, phase or amplitude assumption. It excludes this complete 12-cell stratum, not all 12-cell possibilities or the global four-family target.

## 1. Projector balance forces one four-axis row subspace

The 3×4 incidence board is full. Every mixed row has degree 4; every mixed column has degree 3. Let K_i be the 4-axis mixed subspace of row i and T_j the 3-axis mixed subspace of column j. Since both row and column sums of the twelve rank-one Q projectors are the same operator,

`Σ_i P_(K_i) = Σ_j P_(T_j)`,

where P denotes the coordinate projector. Every degree-3 column has at most one support-2 ray: distinct support-2 sets in a 3-set overlap once, while identical orthogonal support-2 rays would force the remaining singleton. Thus each T_j is the full support of at least two Q rays and is contained in at least two of the K_i. The projector identity now implies every axis used by a K_i belongs to at least two K_i: an axis belonging to only one row subspace could occur in no T_j.

If two K_i coincide and the third differs, an axis of the third outside the first two belongs to only one; impossible. Suppose instead the three K_i are distinct. Let g be the number of axes in all three and d_12,d_13,d_23 the numbers in precisely the indicated two. There are no one-row axes, and each row has four axes, so

`g+d_12+d_13 = g+d_12+d_23 = g+d_13+d_23 = 4`.

Thus all d_ij equal some positive integer d and g+2d=4. An axis in precisely rows i,j must appear in two column sets by the projector identity. Any such T is contained in K_i∩K_j, whose size is g+d=4−d; hence d≤1. Therefore d=1,g=2. Each of the three distinct axes belonging to precisely a given row pair requires two columns with T_j=K_i∩K_j, giving six columns rather than four. Contradiction. Hence K_1=K_2=K_3=:K.

Each T_j is a 3-subset of K, so write T_j=K\{a_j}. The projector identity says every a∈K is omitted from exactly one column: the four a_j are distinct. The twelve Q rays can consequently be completed to an actual 4×4 QLS in span(K) by adding the coordinate row e_(a_j); that completion is not assumed classical.

## 2. A row with two support-2 rays is already impossible with a mate

Every mixed cell in this board has support at most 3 because it lies in a degree-3 column. In a degree-4 row, two support-2 rays therefore force all four rays to have support 2. If the two supports agree they fill their plane, leaving the other two rays in the complementary 2-plane. If they are disjoint they fill the 4-axis subspace; an orthogonal support-3 ray would meet one of the two support-2 rays in exactly one coordinate, so the remaining rays have support 2, one on each plane. In either case the supports are U,U,V,V for disjoint 2-sets U,V. Suppose row i has this pattern. Choose a∈U and one column j where the row-i Q ray has support V. Since T_j contains V and has size 3 inside K=U∪V, it contains exactly one axis of U; take a to be that axis. The other two Q rays in column j have full support T_j, because that degree-3 column already contains its unique support-2 ray. The two U-support Q rays in row i and those two full-support column-j Q rays all overlap e_a. The two row-i mate R rays are orthogonal, the two column-j R rays are orthogonal, and each cross Q inner product is nonzero because the supports meet only at a. Therefore all four R rays are pairwise orthogonal.

Five Q rows contain no mixed cells, one being the chosen first row. Each contains Q=e_a, and the five corresponding R rays are pairwise orthogonal and orthogonal to the four selected rays by Q⊗R. This would give nine orthogonal rays in C^8. Hence with a mate each mixed row has at most one support-2 ray.

## 3. The remaining support patterns also force four mate rays

There are at most three support-2 cells, and at most one in any degree-3 column. We choose a mixed row i, a column j, and a coordinate a∈T_j so that:

1. its row-i ray q_j overlaps e_a;
2. the other two Q rays in column j have full support T_j;
3. the other three row-i rays have full support 3.

If a support-2 cell exists, take it as q_j and choose either a in its support. Then its row's other three rays and its column's other two rays have full support. If no support-2 cell exists, choose any row, column and a∈T_j. These are all possibilities.

In row i, let q_0 be the ray in the unique column with missing axis a, and let q_j,q_k,q_l be the remaining three rays. They form an orthonormal basis of K, and q_0,q_k,q_l have full support 3; q_0 has zero a-coordinate, while q_j,q_k,q_l all overlap e_a. Denote by x,y the two other Q rays in column j. They are orthogonal, have full support T_j and hence both overlap e_a. They are both orthogonal to q_j by the column QLS condition.

At least one of x,y must overlap **both** q_k and q_l. Otherwise each is orthogonal to at least one of q_k,q_l. Neither can be orthogonal to both: together with orthogonality to q_j this would make it collinear with q_0, which has zero a-coordinate. Thus each is orthogonal to exactly one of q_k,q_l and is a linear combination of q_0 and the other one. Both coefficients are nonzero. Indeed x and y have zero coordinate a_j, whereas q_0 and q_k,q_l have nonzero a_j coordinates: their own omitted axes are different from a_j. If x and y use the same active basis ray, the zero-a_j condition puts them on the same one-dimensional ray; if they use different active basis rays, their inner product consists solely of the nonzero q_0-coefficient product. Either case contradicts x⊥y.

Choose x or y with nonzero overlap with both q_k and q_l. In any orthogonal mate R, the three rays at q_j,q_k,q_l are pairwise orthogonal because they lie in row i. The fourth, at the selected column-j Q ray, is orthogonal to the R ray at q_j by its column and to the R rays at q_k,q_l by Q⊗R orthogonality and the nonzero Q overlaps. Thus the four R rays are mutually orthogonal and all four Q rays overlap e_a. As in §2, the five Q=e_a light cells in the five unmixed rows force five additional orthogonal R rays, contradiction.

The proof uses no numerical or selected-instance premise. During discovery a bounded exact-support SAT query and a separate rational QLS(4) example were explored; the SAT model was only a necessary support pattern, not a physical witness, and neither is an input to this all-variable proof. Independent mathematical review must reconstruct the projector equality, the two-pair row argument, the exact nonzero-coordinate selection and the 4+5 mate-ray contradiction. No independent, parent, formal, human, executable or novelty verdict is asserted; A10/A11 remain OPEN.
