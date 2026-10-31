# A proper resolved quantum subblock requires N at least 3k

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:20:25 PDT 2026**. This extends the classical OLS common-subsquare bound to arbitrary quantum vectors and arbitrary external cells. It is not an unrestricted QLS10 no-go.

## Theorem

Let Q be a 1-resolvable QLS of order N with resolution Latin square L. Suppose there are k rows R, k columns C, and a k-dimensional subspace H such that the k×k subarray on R×C is itself a QLS(k) in H. Suppose additionally that the labels occurring there form a set T of k symbols and that the restriction of L to R×C is a Latin square on T. If k<N, then

`N >= 3k`.

The rays outside the block may be completely arbitrary and may mix H with H-perpendicular; they are NOT assumed classical, separable, or assigned to an orthogonal direct-sum sector.

## Proof

Every column c in C contains k orthonormal block vectors spanning H. Therefore every cell in that column outside the block is orthogonal to H. Likewise, because L restricted to the block is Latin on T, each of the k global transversal bases labelled t in T contains k block cells forming an ONB of H; every other cell with such a label is also orthogonal to H.

Fix any outside row r not in R. Its k cells in columns C lie in H-perpendicular. Its k cells whose labels lie in T also lie in H-perpendicular, and these are disjoint from the first k cells: each column in C already uses all k labels of T inside R, so no outside row can have a T label in those columns. Thus row r contains 2k mutually orthogonal nonzero vectors in H-perpendicular, whose dimension is N-k. Hence `2k<=N-k`.

## Order10 consequence

A proper resolved quantum subblock in any 1RQLS10 has `k<=3`. For k=3 the local QLS is necessarily classical up to a local unitary and cell phases (the elementary proof is in `frontier-20261029-odd-common-subsquare-packing-obstruction-v1.md` SHA **e554bf7006011d2c527ee7d3ffca322aac89ccd44387975528cc1c3c1b637471**). Thus a direct embedding of the known maximal resolved QLS8 as an 8×8 subblock into order10 is impossible even if all outside vectors are unconstrained quantum states. This also rules out analogous 4×4 and 5×5 resolved subblocks, not just the classical OLS-block replacement construction.

The result does not preclude an order10 solution with no such subblock, an approximate/non-spanning subarray, or a different resolution labeling. The dimension-count caller requires independent written review.
