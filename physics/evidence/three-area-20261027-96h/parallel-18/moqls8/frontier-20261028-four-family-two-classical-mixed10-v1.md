# A second dimension obstruction excludes nine mixed cells

**WRITTEN author candidate; no catalogue or computation premise. Disjoint mathematical review pending.** In an actual ordinary four-MOQLS(8) with two classical members, every other nonclassical QLS Q has at least **ten** mixed cells relative to any Q basis line of the resulting four-net. The fourth member R is arbitrary complex. This strengthens the separately review-pending ≥9 argument `frontier-20261028-four-family-two-classical-mixed9-v1.md` SHA256 25caadec64da9a67f45f9fe3cb20fd166c3250d6c9edc86affca157b09e7cc83, which is a named WRITTEN import here. No full q2 exclusion, M(8), A10/A11 or novelty claim follows.

As in that packet, Q and R are ONBs on every row, column and each of the two classical-mate symbol lines. Choose any such Q line as row 0 and standardize Q and R independently there to `e_0,...,e_7`. A Q cell is mixed if its ray is not one of Q's first-row basis rays. Every net line with a mixed Q ray contains at least two mixed cells. On a line with exactly two mixed cells, their supports are the same two coordinate axes. On a line with exactly three mixed cells, all three lie in a three-coordinate subspace, and at most one has support size 2: two different 2-subsets of three axes intersect once and cannot be orthogonal; if two coincide and are orthogonal, the third vector is the remaining singleton. These line facts use the actual Q ONB.

## 1. Possible line partitions when there are nine mixed cells

Suppose there are exactly nine mixed cells H. A net line L cannot contain five or more of them. If L contains k≥5, each of its k mixed points needs at least one mixed neighbor on each of its other three class-lines. These neighbors lie outside L and are distinct for each point, giving at least 3k cross-adjacencies. Each outside point can be adjacent to at most three L-points, since two L-points cannot share a second line; there are 9−k outside points. Thus `3k≤3(9−k)`, a contradiction for k≥5.

For any fixed one of the four net classes, its lines partition the nine mixed points into groups of sizes 2,3 or4. The only possibilities are

`3+2+2+2`,  `3+3+3`,  or  `4+3+2`.

## 2. Eliminate 3+2+2+2 and 4+3+2

In the `3+2+2+2` case, choose a support-3 Q ray x from the three-point line; at least two exist. Every point in the three two-point parallel lines has Q support size 2 by the two-mixed-line lemma. Each of the other three net lines through x must contain at least three mixed cells, because a two-mixed line would force x to have support size 2. These three lines meet only at x and there are exactly six mixed points outside x's original line, so each contains exactly two outside mixed points. Both outside rays on each of those three-mixed lines have support size 2, contradicting the three-mixed-line lemma.

In the `4+3+2` case, choose a support-3 ray x from the three-point line. Each of its other three class-lines again has at least three mixed points. Such a line can contain at most one point from each of the other two parallel lines, so it must contain one point from the four-point group and one from the two-point group. The three lines through x would require three distinct points from that two-point group. Contradiction.

## 3. Eliminate 3+3+3 using the fourth QLS

Suppose the chosen class has three three-point lines X,Y,Z. Each contains at least two support-3 Q rays. Choose a support-3 x∈X. Every one of the other three class-lines through x has at least three mixed points, and can contain at most one point of Y and one of Z. Hence each contains exactly one from each, and x is net-line-adjacent to **every** point in Y and Z.

Let T_X be the three coordinate axes supporting the three mixed Q rays on X. Since x has support size 3, its support is all of T_X. Every other class-line through x is a three-mixed ONB line; its three-axis mixed subspace contains x and must therefore be exactly T_X. Every Q ray on Y is on one of those lines, so all three Y rays lie in T_X. They are an orthonormal triple on Y, so their three-dimensional span T_Y equals T_X. The same argument gives T_Z=T_X. Denote this common coordinate set by T.

There are at least six support-3 Q rays, two in each of X,Y,Z; each has nonzero coefficients on **all** three axes in T. Any two of these six cells share a net line: within one group by definition, and across groups because a support-3 ray is adjacent to all points in the other groups by the preceding argument. Since R is an ONB on every actual net line, its corresponding six rays are pairwise orthogonal.

For each such cell, Q overlaps all three first-row Q rays indexed by T. Actual Q⊗R product orthogonality against those first-row products forces the corresponding R ray orthogonal to all three first-row R axes indexed by T. All six pairwise orthogonal R rays would therefore lie in a subspace of dimension at most five, impossible.

All three possible line partitions are excluded, so nine mixed cells cannot occur. Together with the cited ≥9 bound this proves **≥10**. In q2, both nonclassical extra members each satisfy the bound, so their total off-first-row support surplus is at least 20, even though their mixed-cell sets may overlap. This is a necessary lower budget, not a global q2 proof.

No finite witness is used. A disjoint review should verify the line-size count, all three partitions, the common-three-axis transfer and the actual six-in-five R dimension contradiction before this WRITTEN candidate is adopted.
