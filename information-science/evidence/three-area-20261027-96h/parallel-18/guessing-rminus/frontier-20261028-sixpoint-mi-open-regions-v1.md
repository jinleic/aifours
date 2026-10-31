# Six open families of six-word distributions cannot have a strict gap

**Status: WRITTEN with independently replayed exact finite coloring certificates, conditional on the pinned graph-FD inequality; scientific review and novelty clearance pending.** Normalize each of the following six positive weight vectors to a probability vector on six labeled support words:

```text
(20,20,1,1,1,1)       (40,20,1,1,1,1)       (50,5,1,1,1,1)
(100,100,2,2,1,1)     (100,50,3,2,1,1)      (100,5,4,3,2,1)
```

For each vector there is an **open neighborhood in the positive six-point probability simplex** such that no original-neighbour R-minus FD law with those six labeled word probabilities has `Delta>0`, regardless of coordinate alphabets or word assignments. This is an open-family obstruction, not a statement about all six-point laws or a numerical guessing-number upper bound.

## Exact potential-MI coloring

There are 203 partitions of six labeled atoms. A strict-gap law cannot use the constant partition, an injective partition, or two copies of one partition: the conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` requires all ten coordinates nonconstant and forbids one coordinate determining another. Thus each coordinate must use a distinct member of the remaining 201 partitions.

For a positive probability vector, make a graph on these 201 partitions: join two distinct partitions `P,Q` if **both** `2I(P;Q)<=H(P)` and `2I(P;Q)<=H(Q)`. Any ten coordinates of a strict-gap law would form a ten-clique, because the pinned inequality gives both inequalities strictly. The exact certificates color this **weak-inequality potential graph** with, respectively, `7,7,8,7,6,8` colors. Hence no ten-clique exists.

The actual probability neighborhoods can be specified without an unknown radius. For each of the six pinned colorings, take all strictly positive probability vectors for which, for every pair of distinct partitions with the same certified color,

\[
2I(P;Q)>\min\{H(P),H(Q)\}.
\]

This is an open set: it is a finite intersection of strict inequalities between continuous functions. It contains its stated normalized weight vector, because the exact checker verifies that every same-color pair is a **strict** nonedge of the weak-inequality graph. The same coloring rules out ten-cliques throughout this set. Relabeling the six support atoms gives the corresponding permuted regions.

## Integer comparison and evidence

For positive integer weights `w` with total `W`, put `F(P)=product_B (sum_{i in B}w_i)^(sum_{i in B}w_i)` over partition blocks. If `P join Q` denotes their common refinement, the weak condition `2I(P;Q)<=H(P)` is equivalent to

\[
F(P)F(Q)^2\ge W^W F(P\vee Q)^2,
\]

and the other condition swaps `P,Q`. Thus no floating logarithm enters the certificate. Producer `frontier-20261028-sixpoint-mi-color-certificate.py` SHA-256 `d8203857dbb0586302f3468e8f05614e6c994a2d371e81c5d4e7fb4547d8fed3`, receipt SHA-256 `11b8bda399a8e2636595a79bd62b5b135eda00ec94e59ae2e9976196c3f2dc61`. Independent checker `frontier-20261028-sixpoint-mi-color-independent.py` SHA-256 `5d131d5f9518bca377bd81237d76711289ea2dd21d1df54e5265cbebcc81d24d`, receipt SHA-256 `af9e0744dda0be9a5fc55a0be62bd40d5da2981f2d5145e1cf0ad2eee3fb7c20`, reconstructs the 201 partitions by a different enumeration, verifies all graph edges and the strict same-color nonedges, and rejects six altered-color controls. The finite checks do not replace independent scientific review of the entropy and continuity deductions.
