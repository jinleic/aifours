# Varying syndrome factors must cover every vertex of R-minus

**Status: WRITTEN conditional on the pinned exact proper-subgraph inequality; scientific review and novelty clearance pending.** In the standard q=8 triangle-factor bit encoding, let `J` be the set of factor indices whose XOR syndromes are **nonconstant** under an arbitrary original-neighbour R-minus FD law. If the triangles indexed by `J` do not cover all ten graph vertices, then `Delta<=0`.

Equivalently, any strict-gap q=8 law must have varying syndrome factors covering every vertex. At least **four** of the ten syndrome bits must therefore vary; exactly 19 four-factor sets cover all vertices. This is an entropy-law statement for arbitrary probabilities and arbitrary support, not merely a fixed-point cardinality bound. It does not say that four varying factors suffice, and does not settle the unrestricted guessing number.

This strictly generalizes the independent unit-syndrome theorem `frontier-20261028-unit-syndrome-global-entropy-v1.md` SHA-256 `a66ca3e2ce69bdf72606ef80bc7cda3019d5ba620bc5e6745bf1bd67227f3a2d`. In particular, it rules out **every** reweighting of the two-outside-word replacement searched in `frontier-20261028-triangle-two-word-reweight-result.json` SHA-256 `e52572b09b47fdea4d3ee3e49f02a3aae2e231a36100ef643293c5402c34492c`: that support varies only factors 1 and 2, whose triangles do not cover the graph.

## Proof

Process the fixed-syndrome factors first in any order. Each has a fixed affine XOR parity, so any two of its bits determine the third and, even after conditioning on previous factor tuples,

\[
H(Z_t\mid Z_{<t})\le\frac23\sum_{i\in T_t}H(X_i^t\mid Z_{<t}).
\]

Now condition on **all** fixed-syndrome factor tuples and treat the remaining `J` factors jointly as one block. On each positive-probability conditional law, the vertex components belonging to those factors still satisfy the original graph FDs: the conditioned fixed components can be supplied as constants to every original decoder. At any vertex outside the union of the triangles in `J`, that variable block is constant. The proper-subgraph theorem `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` therefore gives

\[
H(Z_J\mid Z_{\rm fixed})\le\frac23\sum_i H(X_i^J\mid Z_{\rm fixed}).
\]

Sum the fixed-factor inequalities and this last block inequality. Replacing conditioning on all earlier components by conditioning only on the respective vertex's earlier components can only increase the right side; the chain rule yields `H(X_V)<=(2/3)sum_i H(X_i)`. No factor independence or uniformity is assumed. If `J` is empty, the fixed-factor tensorization alone gives the result.

`frontier-20261028-syndrome-cover-check.py` SHA-256 `8f8121c8e31a1a55ddac81e627eacbeea013fd39e8baebccb0596d5d187b059a`, receipt SHA-256 `e1bf3ece1f9204a8f0f779bf98a236d689946df2bef5d2a50408b30bc9f3418d`, verifies all 1,024 factor subsets, the 19 four-factor covers and one intended mutation. The entropy/conditional-FD argument is written, not proof-assistant formalization or independent scientific review.
