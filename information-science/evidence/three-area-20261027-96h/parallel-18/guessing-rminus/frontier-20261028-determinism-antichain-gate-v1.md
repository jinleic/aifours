# Strict-gap coordinates form a deterministic antichain

**Status: WRITTEN corollary of a pinned exact graph-FD inequality; scientific review pending.** For any finite original-neighbour R-minus FD law, the conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` gives, for every distinct `i,j`,

\[
3\Delta+2I(X_i;X_j)\le\min\{H(X_i),H(X_j)\}.
\]

Hence `Delta>0` requires **all ten variables to be nonconstant and no one to determine another**. More precisely, their pairwise mutual information must be less than half of either singleton entropy. If `X_j` is a function of `X_i`, then `I(X_i;X_j)=H(X_j)`, and the inequality at `j` gives the quantitative obstruction `Delta<=-H(X_j)/3<=0`.

For any finite-group coset law `X_i=gH_i`, under **any** distribution of `g`, subgroup inclusion `H_i<=H_j` makes `X_j` a deterministic function of `X_i`. Thus a strict-gap coset witness must use ten pairwise incomparable subgroups. In particular, no finite group whose subgroup-inclusion poset has width at most nine can produce a strict R-minus coset witness, even with nonuniform `g` or restricted support. The poset-width corollary is elementary: ten pairwise incomparable subgroups would be an antichain of size ten.

This is a necessary condition only. It assumes the pinned graph-FD inequality, does not assert that an antichain of size ten is sufficient, and gives no general guessing-number upper bound or novelty claim.
