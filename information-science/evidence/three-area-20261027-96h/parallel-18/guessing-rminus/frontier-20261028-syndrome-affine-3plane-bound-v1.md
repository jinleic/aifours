# Every affine three-plane of q=8 syndromes has FD capacity at most 2^20

**Status: WRITTEN with independently replayed exact finite clique lifts; scientific review and novelty clearance pending.** Fix the standard ten-triangle factor-bit encoding and let `W0` be its `2^20`-word kernel. For **every affine subspace of syndrome dimension at most three**, any original-neighbour R-minus FD support contained in the corresponding syndrome classes has at most `2^20` words.

Consequently any q=8 fixed-point set strictly larger than the triangle code must have syndrome support of **affine dimension at least four**, and in particular must meet at least five distinct syndrome classes. This is a fixed-label cardinality result, not an arbitrary reweighted entropy-gap exclusion, q=8 no-gain theorem, or unrestricted guessing-number bound.

## Three ways to cover a syndrome 3-plane

It is enough to consider 3-dimensional linear syndrome subspaces `V`; an ambient translation handles affine offsets, and lower-dimensional planes extend to a 3-plane. There are exactly `6,347,715` such subspaces.

1. **Fixed-factor hyperplanes.** `3,487,095` lie in a coordinate hyperplane for one of the six factor indices `{1,2,3,6,8,10}`. The exact clique-tiling theorem `frontier-20261028-syndrome-hyperplane-bound-v1.md` SHA-256 `90e92ee0bc19a29f25e04ebb8ca4d55cca85301d04ba15f26060522db32f48a4` bounds any support in that entire hyperplane by `2^20`.
2. **A vertex-local linear section.** Another `2,835,534` have a vertex `i` for which the restriction map from `V` to the three syndrome bits incident with `i` is injective. There is a linear section `L_i:V -> F_2^30` of the syndrome map whose words have zero neighbour symbols at `i`: in a factor incident with `i`, put its desired syndrome bit at `i`; in every other factor choose one fixed vertex outside `N(i)` for that bit. Such a vertex exists because no triangle is contained in a neighbourhood of the `K4`-free graph. Every nonzero section word has nonzero symbol at `i`, so all eight words in `L_i(V)` form a conflict clique.
3. **Explicit exceptional lifts.** For the remaining `25,086` subspaces, the pinned receipt gives three 30-bit representatives whose syndromes form a basis of that subspace and for which **all seven nonzero XOR combinations** are confusable differences. Their span is an eight-word conflict clique. A separate checker recomputes the subspace coverage and verifies all `175,602` nonzero differences directly from the graph.

In cases 2 and 3, the clique span maps bijectively to `V`. It intersects `W0` only at zero, so its `W0` translates partition all eight syndrome classes in the corresponding linear or affine 3-plane into `2^20` disjoint 8-cliques. An FD-consistent support meets each clique at most once. In case 1 the previously proved larger-hyperplane tiling applies.

## Exact evidence

Producer `frontier-20261028-syndrome-3plane-lifts.py` SHA-256 `3afed9a4daf661c04d3503a63a9c459cd3dce0c1dda974a405354cfd99c58edd`, receipt with the 25,086 explicit basis/lift records SHA-256 `f31739ca90dde765c9d272567809fc5ec7c21803413db0248429e71e0e0a7562`. Separately written `frontier-20261028-syndrome-3plane-independent.py` SHA-256 `056c141ca84d7620ba6b8222c80ba55b27e34091e23472a3068919a0fe26cfd6`, receipt SHA-256 `4783589e5cbc72e8a93e2a0ce6052b728c72269d6b49a23c2923b7121198d462`, re-enumerates every syndrome subspace, verifies the six hyperplane and vertex-local classifications, checks the syndrome and seven graph conflicts for each exceptional lift, and rejects two intended-reason controls. The linear-section and clique-tiling deductions are written mathematics; the checks are not proof-assistant formalization or an independent scientific review.
