# A nonclassical four-MOQLS(8) member must have a mixed line of degree at least three

**WRITTEN author candidate; no classical-mate, source catalogue, solver or finite-witness premise. Disjoint review pending.** In any actual ordinary four-MOQLS(8), a nonclassical member Q cannot have every mixed row and every mixed column containing exactly two mixed cells. Equivalently, relative to any actual chosen Q first-row basis, some row or column containing mixed Q rays must contain **at least three** of them. All other three QLS may be arbitrary complex and nonclassical.

This excludes the entire degree-two mixed-incidence branch, including any number of disjoint row/column cycles, not merely the single-cycle branch of `frontier-20261028-mixed-cycle-two-sided-bound-v1.md` (SHA256 eaa19f2d481574471b80ca6ccd8aa83978751121cc718cf812b9e2157c21f5ed). It is a necessary structural obstruction, not complete four-family classicality, an M(8) upper bound, A10/A11 closure, novelty or an independently reviewed theorem.

## 1. Cycle components and an exclusive-axis lemma

Normalize Q and its three actual orthogonal mates independently on the chosen first row to coordinate rays e_j with common column labels. A Q cell is *mixed* if it is not one of its first-row rays. Any mixed row or column has at least two mixed cells: on an occupied coordinate of a non-singleton ray, no same-line singleton can contribute, and ONB completeness forces another mixed ray there. If all mixed line degrees equal two, the finite simple bipartite graph whose vertices are mixed rows and columns and whose edges are mixed cells is a disjoint union of cycles C_(2k_i), each k_i≥2.

On a row/column with exactly two mixed Q rays, the other six light rays are distinct first-row axes; the mixed pair is an ONB of the remaining two-axis coordinate space. Thus each connected cycle component C_i has one common two-axis support T_i={a_i,b_i}, and its Q rays alternate between two perpendicular one-dimensional rays, k_i of each. Since the selected first row is not mixed, if `K=Σ_i k_i` is the number of mixed rows then `K≤7`. There are at most three components because every k_i≥2.

**Exclusive-axis lemma.** Suppose one axis a in a component C of size 2k occurs in no mixed Q ray outside C. Every row outside C contains a light Q=e_a ray: if the row has a different cycle's mixed pair, both of those rays avoid a and all its remaining entries are light, so ONB completeness includes e_a; otherwise the whole row is light. There are exactly n−k such rows. For any other mate R their R rays are mutually orthogonal and orthogonal to all R_C rays by the actual Q⊗R product ONB. The two k-cell ray parts of C each give k mutually orthogonal R rays, so R_C spans exactly k dimensions and the two parts are ONBs of that common space.

Their k×k transition matrix has two zeros in every row, at the actual row/column neighbors on C. Transition supports for different mates are pairwise disjoint by their original pair-product ONBs; for t total family members this gives `t≤k−1`. Also every Q_C ray uses b, so all R_C are orthogonal to first-row R=e_b. The n−k light-e_a R rays form an ONB of the complement of the k-space and include first-row e_a. Since e_b lies in that complement and is orthogonal to e_a, each mate has nonzero e_b overlap at some one of the other n−k−1 light-e_a cells. Pair-product orthogonality between two mates forbids the same cell for both. Hence `t≤n−k`. Thus an exclusive-axis cycle satisfies `t≤min(k−1,n−k)≤floor((n−1)/2)`. In order 8 it cannot occur in a four-family.

From now on suppose no support axis is exclusive to one component.

## 2. One common two-axis support for all components

First consider the case that all component supports equal the same pair `{a,b}`. Group cycle components by their projective Q two-ray basis: two components are in the same group when their two orthogonal ray pairs agree up to phases and interchange. In dimension two, two distinct orthonormal ray bases have no zero cross-overlap; hence Q rays from different groups have nonzero overlaps, and the corresponding R subspaces are pairwise orthogonal for every other mate R.

If group g contains K_g mixed rows, its K_g rays of either local Q direction are collinear in Q and therefore give K_g orthogonal R rays. Its R span has dimension at least K_g. Across groups the spans are orthogonal. The n−K light Q=e_a rays in rows without mixed cells give n−K further orthogonal R rays, orthogonal to every mixed R ray. Since `Σ_g K_g=K`, dimension n forces each group span to have **exactly** dimension K_g. Its two Q-ray parts therefore give two ONBs of that group span.

If there are at least two distinct basis groups, each group's transition matrices for the three other mates have pairwise disjoint supports and at least two row/column zeros per row, so the argument above forces `K_g≥5` for every group. Two groups would give K≥10, contradicting K≤7. If there is only one basis group, both Q ray parts over **all** components are collinear globally. The same two transition and first-row-axis pigeonholes as in the exclusive-axis lemma apply to their common K-dimensional R span, giving `t≤min(K−1,n−K)≤3` at n=8. Thus a common support pair is impossible in a four-family.

## 3. The only remaining support graph is a triangle

With exactly two components, if their 2-sets differ, one component has an axis absent from the other, contrary to the exclusive-axis lemma. If they agree, §2 applies. So two components are impossible; one component is already covered by the exclusive-axis lemma.

With three components and no exclusive axis, consider the three two-element support sets as edges of a multigraph on coordinate axes. If two distinct sets occur and one is repeated, the singleton distinct set has an exclusive axis. If all three distinct sets occur and no axis has degree one, they must form a triangle `{a,b}`, `{a,c}`, `{b,c}`. The remaining possibility—all three supports equal—was excluded in §2.

For the triangle case, take any component C_i and another C_j sharing axis a. Their other support axes differ, so every Q ray on C_i has **exactly one** common support coordinate with every Q ray on C_j; all such overlaps are nonzero. Actual Q⊗R orthogonality therefore makes their R spans mutually orthogonal for every other mate R. The third component does not use a. If C_i,C_j occupy k_i,k_j mixed rows, there are n−k_i−k_j light Q=e_a rays in all remaining rows, including rows of the third component. Their R rays are mutually orthogonal and orthogonal to both spans. Each component has at least k_i or k_j mutually orthogonal R rays from either of its Q-ray parts. Dimension n forces both spans to have exactly those respective dimensions.

The two k_i-ray parts of C_i are therefore ONBs of one k_i-space for every mate R. Their transition matrices have the two row/column zero positions per row and pairwise disjoint supports across mates, so `t≤k_i−1`. But with three components `k_i≥2` and `Σ k_i≤7`, hence every k_i≤3. A four-family is impossible. The same reasoning holds for each component by choosing either shared axis.

All one-, two- and three-component possibilities are exhausted, so the mixed-incidence graph of a nonclassical four-family member in order 8 must have a row or column of mixed degree at least three. No assertion is made for such higher-degree graphs, for non-product generalized QOA entries, or for A10/A11.

A disjoint review should reconstruct the exclusive-axis count including rows occupied by other cycles, the same-support basis grouping/dimension equality, the support-multigraph trichotomy and the triangle case's actual Q⊗R orthogonality before adoption.
