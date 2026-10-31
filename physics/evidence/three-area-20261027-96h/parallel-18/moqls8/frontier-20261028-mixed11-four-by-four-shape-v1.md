# An eleven-mixed-cell order-8 QLS is confined to a 4×4 incidence board

**WRITTEN author candidate; disjoint review pending.** For any actual complex QLS Q of order 8 and any chosen Q row, if exactly 11 cells are non-coordinate rays relative to that row, then exactly four rows and four columns contain those cells. No orthogonal mate, classicality, source classification or numerical experiment is assumed. This is a QLS-only shape restriction, not an exclusion of 11 cells or a four-family conclusion. Together with the separately review-pending four-family ≥11 candidate `frontier-20261028-four-family-universal-mixed11-v1.md` SHA256 9299801cf3f66a081fb828d0e4ea4568a56edd73d581c6fd833de226c2a93a02, it identifies the next boundary case but does not establish ≥12.

Standardize the chosen Q row to e_0,…,e_7 and call all other Q rays not collinear to these axes *mixed*. A line with k mixed cells has complementary k-axis mixed subspace; degree 2 forces both mixed Q rays to have the same support 2, and a degree-3 line has at most one support-2 ray. A degree-4 line containing three support-2 mixed rays has a fourth support-2 ray as well, since orthogonality forces two disjoint support pairs each repeated twice. Mixed row/column degrees are at least 2.

With exactly 11 mixed cells, r,c≤5 and rc≥11. Up to exchanging rows/columns in the incidence argument, the only possible pairs are `(3,4),(3,5),(4,4),(4,5),(5,5)`.

## (3,5), (4,5) and (5,5)

For c=5 the column degrees are `(3,2,2,2,2)`. Any degree-3 row would meet at least two degree-2 columns, giving two support-2 Q rays and contradicting the degree-3 fact. For r=5 the row degrees are `(3,2,2,2,2)`, so this is impossible. For r=4 the only degree profile without a 3 is `(5,2,2,2)`. The degree-3 column meets at least two degree-2 rows and hence contains two support-2 rays, again impossible.

For r=3 the degree profiles are `(5,4,2),(5,3,3),(4,4,3)`, so the only remaining profile is `(5,4,2)`. The degree-3 column meets all three rows. The degree-4 row's other three rays are in degree-2 columns, hence have support 2, so its ray in the degree-3 column has support 2 as well. The degree-2 row's ray in that column also has support 2, contradicting the degree-3 fact.

## (3,4)

The row degrees are `(4,4,3)` and the column degrees `(3,3,3,2)`. Each degree-3 column meets all three mixed rows; the degree-2 column meets both degree-4 rows. The degree-3 row meets the three degree-3 columns and has at least two full-support-3 rays. Choose two of those rays, q_1,q_2, in distinct columns. Their support is the same 3-set W because they lie in one degree-3 row. Each chosen degree-3 column's mixed subspace is W, since it contains a full-support-W ray.

Fix either degree-4 row. Let x_1,x_2 be its rays in those columns, and let u be its ray in the degree-2 column, with support U of size 2. The two x_j lie in W, are mixed and mutually orthogonal; each is also orthogonal to u. Column orthogonality gives x_j⊥q_j. Let K be the 4-axis mixed subspace of this degree-4 row, which contains U and the supports of x_1,x_2.

* If U⊂W, then u,x_1,x_2 are an orthonormal basis of span(W). The fourth mixed ray of the degree-4 row lies in the 1-axis complement of W inside K, a singleton, contradiction.
* If |U∩W|=1, the single-overlap rule forces each x_j to avoid the common coordinate a. Thus x_1,x_2 form an orthonormal basis of the 2-axis subspace B=W\{a}.
* If U∩W is empty, both x_j are supported in K\U, which has only two axes. Since they are mixed, both have that same 2-axis support B⊂W, and again they form a basis of B. Let a be the unique axis in W\B.

In the latter two cases, q_1|_B is perpendicular to x_1 and hence collinear with x_2, while q_2|_B is perpendicular to x_2 and collinear with x_1. Their B-projections are orthogonal. Both q_1,q_2 have full support W, so their inner product is the single nonzero a-coordinate contribution, contradicting the orthogonality of the degree-3 row. The 3×4 incidence case is impossible.

Therefore only `(r,c)=(4,4)` remains. The original row/column names may be exchanged in the argument; the coordinate basis is always the originally chosen actual Q row. This excludes no 4×4 eleven-cell board by itself. The remaining 4×4 profiles are `(4,3,2,2)` or `(3,3,3,2)` on each side, subject to the at-most-one-support-2 condition on each degree-3 line. Full amplitudes, all mates, and all such profiles remain to be analyzed.
