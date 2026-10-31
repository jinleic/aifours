# A 4D triangle span forces degeneracy; cyclic v5 needs five spectral values

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:35:49 PDT 2026. The first result is symmetry-free; the second uses the cyclic action. Neither is an unrestricted G6 or 1RQLS10 no-go.

## Symmetry-free rank-4 condition

Let G6 be `Circ(15; ±2,±5,±7)`, with a distinct C6 ray on every edge and an ONB at every vertex. Its five vertex-disjoint ±5 triangles are `D_r={r,r+5,r+10}`, r modulo 5. Suppose the 15 triangle rays span a **4D** subspace T. For triangle i, write S_i for the 3D span of its three orthogonal edge rays, and let n_i be a unit normal to S_i inside T.

**Claim.** Some triangle ray belongs to the 3D span of a *neighboring* triangle, where neighboring triangle labels differ by ±2 modulo 5. Equivalently, for some neighboring i,j and triangle ray t of i, `<n_j,t>=0` (or the same statement with i and j exchanged).

**Proof.** Suppose no such inclusion occurs in either direction for any neighboring pair. Their normals n_i,n_j are then linearly independent. In the 2D quotient `T / span(n_i,n_j)`, the three triangle rays of i have nonzero, pairwise nonproportional images, and the same holds for j. To see this, a zero image of one ray or proportional images of two rays would put a nonzero combination of those one or two orthogonal rays in `span(n_i,n_j)`; taking its inner product with an unused triangle ray forces that unused ray to be orthogonal to n_j, contrary to the assumption.

At a vertex of triangle i, the projection onto T of any inter-triangle edge ray is orthogonal to the two incident triangle rays; hence it lies in the 2D plane spanned by n_i and the triangle ray opposite that vertex. For an edge between neighboring triangles i,j, a **nonzero** T projection must lie in both endpoint planes. The distinct nonzero quotient images above imply that for each of i's three vertices there is at most one vertex of j whose opposite-ray image can match. Thus at most three of the inter-triangle edges between i and j have nonzero T projection.

The five triangles form a 5-cycle under the remaining graph edges, with six cross edges per neighboring pair. So at most 15 inter-triangle edges have nonzero T projection. On the other hand, each of the 15 vertices has four inter-triangle rays, at most two of which can lie in the 2D space `T-perp`; hence at least two per vertex have nonzero T projection. Counting endpoints gives at least 15 such edges. Equality forces **exactly two** incident rays in `T-perp` at every vertex. A ray in that 2D space has a unique orthogonal partner there. Since it occurs at two distinct contexts and the graph is simple, its partner in those two contexts is carried by two different edges, contradicting global distinctness. The assumed absence of a neighboring span inclusion is impossible.

## Cyclic consequence: at least five spectral values

Assume in addition that a unitary U implements translation by one and v5 is the ray on `(0,5)`. Normalize U so U^15=I, as in `frontier-20261029-cyclic15-unrestricted-multiplicity-v1.md` SHA-256 `128c8d68c92ef4db22169b0376e7a97758efa4ef18cdb086ecf4914de5482de7`. The preceding triangle-span theorem `frontier-20261029-cyclic15-triangle-span-obstruction-v1.md` SHA-256 `4dafd1cda09d2e35fd96daa8f66c71136dc278c0f37b31cd5301574ab7d3d853` gives at least four distinct U eigenvalues with nonzero v5 projection.

Exactly four are also impossible. Orthogonality of `v5,U^5 v5,U^10 v5` means all three U^5 eigenspaces occur; with four distinct U eigenvalues, their support distribution among those eigenspaces is `(2,1,1)`. The triangle span `T=span{U^i v5}` is 4D. The normal n to the 3D span `S_0=span{v5,U^5v5,U^10v5}` lies wholly in the 2D U^5 sector. In normalized U eigenvectors f1,f2 from that sector write its v5 component as `a f1+b f2`, with a,b nonzero and eigenvalues lambda1 != lambda2. Up to normalization take `n=-conjugate(b) f1+conjugate(a) f2`; then

`<n,U^(±2)v5> = a b (lambda2^(±2)-lambda1^(±2)) != 0`.

The inequality holds because the ratio of the distinct eigenvalues is a 15th root of unity, so it cannot be −1. U^5 acts by a common scalar on f1,f2. Consequently **none** of the three triangle rays in S_0 lies in either neighboring span `U^(±2)S_0`, and conversely none of their triangle rays lies in S_0. Translating gives the same for all neighboring triangle pairs, contradicting the rank-4 condition above.

Therefore any cyclic-equivariant 45-distinct-ray lift must have v5 supported on **at least five distinct U eigenvalues**. This holds for arbitrary complex amplitudes and spectral fields. It leaves 5- or 6-value support, broken cyclic symmetry and general QLS10 open. The quotient counting, projective caller and spectral calculation need independent written review; no formal-kernel or novelty claim is made.
