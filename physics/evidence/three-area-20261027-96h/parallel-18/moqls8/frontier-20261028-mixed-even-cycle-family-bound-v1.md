# A general even-cycle bound for mutually orthogonal quantum Latin squares

**WRITTEN author candidate; no classical-mate, catalogue, numerical solver or finite-witness premise. Disjoint review pending.** Let Q be a nonclassical member of an actual family of t ordinary mutually orthogonal QLS of order n. In a chosen actual Q first-row basis, suppose its entire mixed-cell row/column incidence graph is one simple cycle `C_(2k)`. Then

`t ≤ k−1`.

The result is conditional on this exact mixed-incidence shape, not a global bound on t or M(n). It generalizes the written m=4/m=6 arguments of `frontier-20261028-three-qls-universal-mixed8-v1.md` SHA256 7464f79b7bddaf7c4345544b2fad332d6c1b56698238df4cee215bc790d63a7f and the separate four-family C8 obstruction `frontier-20261028-four-family-mixed8-cycle-obstruction-v1.md` SHA256 d1e76c0f6f60a8af0fb2567596f48a7a66a6ab3e24d45060c29fec4455741fc5. The proof below is self-contained and does not assume those earlier candidate verdicts.

## 1. From the actual cycle to unitary overlap patterns

The cycle has k mixed rows and k mixed columns, with exactly two mixed cells on each. On a row or column with exactly two mixed Q rays, the other n−2 light rays are distinct first-row coordinate rays, so the two mixed rays are an ONB of the complementary two-axis subspace. Along the connected cycle all mixed Q rays therefore have the same two-axis support `{a,b}` and alternate between two perpendicular one-dimensional rays. Label the two k-cell parts `p_1,...,p_k` and `m_1,...,m_k`.

For any other member R, its k rays on the p-part are pairwise orthogonal because the corresponding Q rays are collinear and the actual Q⊗R products are orthogonal. The same holds on the m-part. The k mixed rows account for all mixed cells, so each of the other n−k rows contains only light Q rays and hence has exactly one Q=e_a cell. Their R rays are mutually orthogonal, and each is orthogonal to all R rays on the cycle because every Q_H ray has nonzero e_a overlap. Thus the cycle's R rays span a space of dimension at most k. Each p- and m-part is an orthonormal k-tuple, so they are two ONBs of the **same k-dimensional space**.

The transition matrix `U^R_ij=⟨R_(p_i),R_(m_j)⟩` is therefore unitary. Each p_i is adjacent along the cycle to exactly two m_j, and those cells share a row or column, so the corresponding two entries of U^R vanish. Every row of U^R has at most `k−2` possible nonzero positions. This construction applies separately to every other QLS in the family.

## 2. The family-size bound and its equality boundary

For two distinct other members R,S, their actual product vectors at p_i,m_j are orthogonal, so `U^R_ij U^S_ij=0` for every i,j. Thus the supports of all `t−1` unitary transition matrices are pairwise disjoint. Each unitary matrix has at least one nonzero entry in any fixed row, and that row has at most k−2 available positions. Hence `t−1≤k−2`, i.e. `t≤k−1`.

For a four-family, `k≥5`: a 4-, 6- or 8-cell single-cycle mixed pattern cannot occur. If k=5 and t=4, equality forces each of the three 5×5 transition matrices to be monomial: in every row the three disjoint supports must occupy the three available positions one each, and unitarity then supplies one entry per column. Their three permutation patterns partition the complement of the ten-cycle in K5,5. This is only a **necessary equality structure** for a potential ten-cell cycle; it neither constructs a family nor asserts that the remaining row/column/product equations are feasible.

No assumption is made about whether R,S or other members are classical. Different mixed-incidence shapes, multiple components, and the unrestricted four-family alternative remain open. A disjoint reviewer should verify the two-axis propagation, the n−k light-cell span bound, the original pair-product disjointness and the k=5 equality statement before adoption.
