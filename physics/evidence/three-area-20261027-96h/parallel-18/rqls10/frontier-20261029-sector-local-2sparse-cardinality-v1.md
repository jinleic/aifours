# A two-sparse sector bounds the cardinality of any resolved QLS

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 01:13:53 PDT 2026**. This localizes the earlier global sparse bound to ONE sector; it does not require the complementary rays to be sparse.

Let Q be a t-resolvable QLS of order N, t>=0, and suppose every cell ray lies in H or H-perpendicular, with `dim H=d`. Suppose only the rays in H have support at most2 in some orthonormal basis of H. Then, for `s=t+2`,

`cardinality(Q) <= N²-dN+d+floor(d(N-1)/s)`.                         (1)

In particular a 1RQLS10 has at most **82** rays if it has such a 3D two-sparse sector, and at most **70** rays for such a 5D sector. Sector membership may be arbitrary. Nothing about the coordinates of the complementary sector is assumed.

Proof: every row ONB contains exactly d rays in H, so the sector has dN cells. Each H-basis is 2-sparse. A support-two ray has a unique orthogonal partner in its coordinate plane, occurring in each of the s contexts of its cell; the partner cells are distinct because the row, column and resolution contexts intersect only at that cell. Applying the same observation to the partner shows every support-two ray occurs at least s times. At most d distinct support-one rays occur, consuming at least one cell each. Hence the number of distinct H-rays is at most `d+floor((dN-d)/s)`, and the remaining `N²-dN` cells contribute at most that many rays. The formula remains valid if some coordinate rays never occur, since the bound is monotone in their number.

The stronger dimension-two sector theorem `frontier-20261029-dim2-sector-cardinality-no-go-v1.md` SHA **045944b9ccc553b4f60f0038ce0131b4d3593ece728ca4e1472faf0bb8192bc4** requires no sparsity hypothesis and uses the involution pairing of ALL 2D rays. The 5D support-three maximal obstruction `frontier-20261029-five-sector-sparsity4-general-v1.md` SHA **bac443fd338c5f1076304a6fa2db50ccc9d8cce1e95debcc6260e9b902bf167f** goes beyond support2 when only maximality is at stake. These are restricted structural results, not general QLS10 impossibility. The written proof requires independent review.
