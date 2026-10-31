# A two-sided family-size bound for a single mixed-cell cycle

**WRITTEN author candidate, no catalogue, computation or witness premise; disjoint review pending.** Let Q be a nonclassical member of an actual family of t ordinary mutually orthogonal QLS of order n. In a chosen actual Q first-row basis suppose its **entire** mixed-cell row/column incidence graph is one simple cycle `C_(2k)`. Then

`t ≤ min(k−1, n−k) ≤ floor((n−1)/2)`.

Consequently no nonclassical member of an ordinary four-MOQLS(8) can have an entire mixed-incidence graph that is a single even cycle, of **any** length. Its mixed graph must either have more than one connected component or have a mixed row/column of degree at least three. This is a universal construction/structure obstruction, not a complete four-family classicality theorem or an M(8)/A10/A11/novelty claim.

This is an additive strengthening of `frontier-20261028-mixed-even-cycle-family-bound-v1.md` (SHA256 a7b7126843aa3d91667dd5f6f0d26b9dbbc67bfec161878f699a4055bfeae4dd), which gave only `t≤k−1`. The two-sided proof below is self-contained.

## 1. The shared cycle subspace

Independently standardize Q and every other actual QLS on the chosen first row to their own coordinate bases e_j, with common column labels. The cycle has k mixed rows, k mixed columns and 2k mixed cells, two in each incident row/column. On each such line the other n−2 Q rays are distinct light first-row coordinate rays; its two mixed rays form an ONB of the complementary two-axis coordinate subspace. Connectedness propagates one common two-axis support `{a,b}` around the cycle, and its two k-cell bipartition parts carry perpendicular Q rays, collinear within each part.

For any other member R, Q⊗R orthogonality makes its k rays in either Q-part orthonormal. Every one of the other n−k rows contains only light Q rays and hence contains one Q=e_a cell. Their R rays are mutually orthogonal by Q⊗R, and each is orthogonal to all R rays on the cycle because every mixed Q ray has nonzero e_a overlap. Thus the mixed R rays lie in a subspace `V_R` of dimension at most k. The two orthonormal k-tuples each span V_R, so `dim V_R=k`.

## 2. First bound: two unavailable transition positions

For each other R, the overlap matrix U^R between its two k-ray ONBs of V_R is unitary. A row of U^R has zeros in the two positions adjacent to its mixed cell on the row/column cycle. For any two other members R,S, their actual product ONB gives `U^R_ij U^S_ij=0` at every pair of distinct cycle cells. Therefore all t−1 unitary overlap matrices have pairwise disjoint supports. In any fixed row they each need a nonzero entry, and only k−2 positions are available, giving `t−1≤k−2`, or `t≤k−1`.

## 3. Second bound: first-row-axis pigeonhole

All R rays on the cycle are orthogonal to the first-row R rays e_a **and** e_b: every mixed Q ray has nonzero overlap with both first-row Q axes, and the Q⊗R products at distinct cells are orthogonal. The n−k mutually orthogonal R rays at the light Q=e_a cells lie in `V_R^⊥`, which has dimension n−k; hence they are an ONB of that complement. One is the first-row R ray e_a. Since e_b also lies in `V_R^⊥` and is orthogonal to e_a, at least one of the other `n−k−1` Q=e_a cells has R overlap nonzero with the first-row ray e_b.

The same statement holds separately for every other member. Two distinct other members cannot both have nonzero e_b overlap at the same off-first-row cell, because their product there would have nonzero overlap with their product at first-row column b. Thus their nonempty choices among those `n−k−1` cells are pairwise disjoint, and

`t−1≤n−k−1`, hence `t≤n−k`.

Combining with §2 gives the claimed bound. Since `(k−1)+(n−k)=n−1`, their minimum is at most `floor((n−1)/2)`. For n=8 this is 3, ruling out a fourth mate for every Q with the stated single-cycle mixed shape. The argument uses all relevant original pair-product ONBs and actual QLS rows; no graph-only extension, phase restriction or extra classical square is assumed.

A disjoint reviewer should check the exact occurrence count n−k, that the n−k light-cell R rays really span all of V_R^⊥, the nonempty e_b overlap for each mate, and both independent pair-product pigeonholes. Other mixed graph shapes, multiple components, and all unrestricted four-family alternatives remain open.
