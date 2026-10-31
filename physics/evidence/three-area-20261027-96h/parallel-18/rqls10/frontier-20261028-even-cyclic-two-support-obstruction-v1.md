# Even cyclic resolutions require three-support quantum vectors

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:28:04 PDT 2026**. This is a new application of the classicalization idea in [Ball–Simoens Lemma13](https://arxiv.org/html/2603.02334v1), with a self-contained proof below. It concerns ANY 1-resolvable QLS, not merely Fourier products, but requires a cyclic resolution and global two-sparsity. It does not solve unrestricted 1-RQLS10.

## Theorem

Let n be even. There is NO QLS(n) whose vectors all have support at most2 in SOME common orthonormal basis and whose transversal-resolution label square is isotopic to the cyclic Latin square of Z_n. No maximal-cardinality premise is needed.

Consequently, an even-order Fourier-product QLS with a transversal, if one exists, must contain a vector of support at least3 in EVERY common basis. In particular, normalize its first row to the standard basis; with `U=K† D K` for normalized K and D the Fourier coordinate-shift, at least one column among `U^0,...,U^(n-1)` must have support>=3. This criterion does not assert that the needed vector or transversal exists.

## Proof

Take the given sparse basis. Within any row, column, or transversal block, two orthogonal nonzero vectors of support<=2 have either disjoint supports or the SAME two-element support: an intersection of exactly one coordinate would give a single nonzero term in their inner product.

Choose a cell vector v of exact support {a,b}. Let U_ab be a 2×2 unitary on the span of those coordinates carrying v to e_a; leave the orthogonal complement fixed. Apply U_ab to EVERY array vector whose exact support is {a,b}, but leave all other cells unchanged. Every originally orthogonal pair in each of the SAME three block families remains orthogonal: two vectors both in that plane are transformed together, and an orthogonal vector outside that exact support has disjoint support. Unit norms remain1. No support increases above2, and v's support drops to1. Repeat; the finite count of two-support cells strictly decreases at every step. The result consists entirely of standard-basis rays and still satisfies all original row, column and transversal ONBs.

Thus its standard-basis labels form a classical Latin square orthogonal to the SAME classical resolution label square. A cyclic Latin square of even order has no classical orthogonal mate: if `(r,c_r)` were a transversal then both c_r and `r+c_r` would be permutations, but their total sums would imply `0≡n(n−1)/2≡n/2 (mod n)`. Contradiction.

A Fourier-product transversal induces, by common-unitary cyclic row shifts, a whole resolution with labels `r−r(c)` after a column relabelling; this is isotopic to the cyclic Latin square. The final necessary support statement follows. No assumption that an arbitrary QLS CAN be made two-sparse is made.

## Scope

This strengthens the earlier general two-sparse maximal-cardinality bound `frontier-20261028-two-sparse-cardinality-obstruction-v1.md` SHA **ed80901c...** in the SPECIAL case of a cyclic resolution: here even a nonmaximal sparse object cannot exist. It does not address arrays with three-support vectors, noncyclic resolutions or Fourier products in full generality. The classicalization proof, basis changes and cyclic-resolution caller require independent review.
