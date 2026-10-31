# The five triangle triples cannot share a 3D sector

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:33:47 PDT 2026. The first statement has **no cyclic-unitary or number-field assumption**; it is a structural condition on the new 6D graph, not a general no-go.

## General graph lemma

Let a simple 6-regular graph on 15 vertices contain five vertex-disjoint triangles that cover all vertices. Suppose distinct rays are assigned to the 15 triangle edges, all graph edges carry rays in C6, and the six incident rays at each vertex form an ONB. Then the 15 triangle-edge rays cannot all lie in one common 3D subspace T.

For otherwise, each triangle's three edge rays form an ONB of T. Consider an edge joining two different triangles. At either endpoint, its ray is orthogonal to the two incident triangle rays, so its orthogonal projection onto T lies on the third ray of that triangle. The two relevant third rays belong to different triangle edges and are distinct, so those lines meet only at zero. Hence every inter-triangle edge ray lies in `T-perp`, which has dimension 3. But each vertex has two triangle edges and **four** inter-triangle edges; their four incident rays would be mutually orthogonal in a 3D space, a contradiction. Nontriangle rays need not be assumed distinct.

## Application to the 600-cell complement

For `G6=Circ(15;±2,±5,±7)`, the five triangles are `{r,r+5,r+10}` for `r=0,1,2,3,4`, with all indices modulo 15. Therefore any distinct-ray 6D completion of the 600-cell 4D parity core in `frontier-20261029-600cell-circulant4d-core-v1.md` SHA-256 `c9370b9c56c57c0ef93ea501cccb0c8fbc34f287e6c418a1a4486bc384498ec1` has the 15 triangle rays spanning dimension **at least 4**. This applies equally to symmetry-breaking completions.

If a unitary U implements translation and v5 is the ray on `(0,5)`, those 15 triangle rays are the orbit `U^i v5`. For a normal unitary, the dimension of its cyclic span equals the number of distinct eigenvalues on which v5 has nonzero projection. Thus any cyclic-equivariant lift must give v5 nonzero weight on **at least four distinct U eigenvalues**. Orthogonality of `v5` and `U^(-5)v5` already forces all three U^5 eigenvalue classes to occur, so at least one class must contain two distinct U eigenvalues with nonzero v5 population.

The lemma excludes a natural common-3D-triangle ansatz; it does not exclude a 4D or larger span, noncyclic or cyclic complements generally, or a 1RQLS10. Its graph caller and projection argument require independent written review; no formal-kernel or novelty claim is made.
