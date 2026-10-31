# A group-valued Latin-label obstruction lifts through quantum tensor factors

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:02:47 PDT 2026**. This generalizes `frontier-20261029-odd-quantum-even-cyclic-tensor-no-transversal-v1.md` SHA **12a38a89c17da80b0b534324058957519138fdcbd75e441a77a27699efdaa397**; it is not a general even-order QLS no-go.

## Theorem

Let Q be ANY order-n QLS, L ANY classical Latin square of order m, and A an abelian group. Suppose there are maps from the rows, columns and symbols of L to A, respectively alpha, beta, gamma, such that

`alpha(u)+beta(v)=gamma(L(u,v))` for every u,v.

Set `Delta=sum_u alpha(u)+sum_v beta(v)-sum_s gamma(s)` in A. If `n Delta != 0`, the tensor QLS `Q tensor L` has NO orthogonal transversal, even with repeated rays.

## Proof

For a hypothetical transversal, every row index u and every column index v of the second factor occurs n times. Its second-factor symbol s also occurs n times: the cells with a fixed s must be pairwise orthogonal in the n-dimensional first factor, so there are at most n of them; all nm selected cells force equality for every s. Summing the displayed identity over the transversal yields `n Delta=0`, contradiction.

For a group Latin square `L(u,v)=u+v` on a finite abelian group G, take alpha=beta=gamma=identity. Then `Delta=sum_(g in G) g`. Pairing g with -g shows this sum is the sum of the 2-torsion subgroup: it is the unique nonzero involution when G has exactly one, and zero otherwise. Hence for ANY odd n, tensoring ANY QLS(n) with the group Latin square of any finite abelian group with a unique involution has no transversal. Cyclic even groups give the earlier theorem. This is a necessary obstruction; failure of the group-sum test does not imply a transversal exists.

For ordinary cyclic Fourier products, CRT transfers this conclusion only where the factorization into the stated QLS and a classical group factor is actually valid. In particular arbitrary mixed-coordinate source permutations and arbitrary K_nm remain outside scope. The algebraic caller requires independent review.
