# If critical PH7 has exactly nine transitions, its graph is two disjoint triangles linked through one state

**NEW CONDITIONAL ALL-TOPOLOGY WRITTEN GRAPH REDUCTION.** MathResearch96h-2. It depends on the separately frozen triangle-imbalance capacity and overlap-budget candidates, whose independent reviews are pending. It does NOT establish that a nine-edge realization exists or exclude all PH7 realizations.

## Theorem

Suppose the original H at `z=8/9` has a PH representation with at most seven states and exactly nine positive off-diagonal transitions. Then its graph has this structure, up to relabeling:

* Exactly seven states; two vertex-disjoint directed 3-cycles occupying six states; no directed 2-cycle.
* The remaining seventh state and the two directed triangles become a **directed 3-cycle after contracting each triangle**. The three connector edges are the ONLY edges outside the two triangles.
* There are exactly two or three triangle vertex sets. In the three-triangle case the connector edges themselves form the third triangle, meeting each of the two disjoint triangles at one vertex.
* Both disjoint triangles are imbalanced (indeed the graph has no reverse edges on either triangle).

The exact supported-route theorem further requires at least one simple 5-edge path from positive initial support to positive exit support. All these conditions are necessary, not sufficient. Higher-edge graphs and the original 8/9 PH7 question remain open.

## 1. Dependencies and an elementary edge-count fact

The separately frozen `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` and `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` force at least TWO imbalanced triangle vertex sets. The independently supported SCC theorem supplies strong connectivity. The separately frozen shared-hub and shared-edge budget sources exclude, respectively, an imbalanced disjoint-petal sunflower and any imbalanced family whose triples all share one edge. The strictly stronger linear-packing source excludes an intersecting linear imbalanced family. All of these proofs require their named independent reviews; they are not assumed adopted here.

We use this fact: if a strongly connected subgraph H has k<n vertices and e edges inside an n-vertex strongly connected graph, at least `n-k+1` further edges are needed. Contract H to one vertex. The quotient is strongly connected on `n-k+1` vertices and hence has at least that many non-loop edges. If equality holds, every quotient vertex has outdegree1 and the quotient is a single directed cycle. This applies even if additional edges inside H would become loops: equality leaves no room for such loops.

## 2. If two imbalanced triangles intersect, a disjoint triangle must exist

Choose two imbalanced directed triangles. If their vertex sets intersect in exactly ONE vertex, their union H has five vertices and six edges and is strongly connected. Exactly three edges remain. The contracted graph has the three vertices H,x,y, so the edge-count fact forces a single directed 3-cycle `H->x->y->H`. A new directed triangle can appear only when its exit and return vertices in H coincide. If no such new triangle exists, the only two triangle triples are the original intersecting pair and the shared-hub budget excludes them. If it exists and uses their common vertex, the three triples form a disjoint-petal sunflower, also excluded. If it uses a private vertex of one original triangle, it is vertex-disjoint from the other; a disjoint pair exists.

If the chosen triples share TWO vertices, either their common edge is used in the same direction, in which case their union has four vertices/five edges, or in opposite directions, in which case it has four vertices/six edges. The opposite-direction case needs at least four further edges to connect the three missing vertices and therefore at least ten total, impossible. In the same-direction case exactly four edges remain. The quotient on H plus the three missing vertices is a directed 4-cycle. No new directed triangle can use those connector edges, because every such cycle must traverse the full 4-edge quotient cycle. Inside H there are exactly the two original triangle triples. They share the same edge and the common-edge hitting budget excludes them.

Thus some pair of triangle triples is vertex-disjoint. The argument also rules out both orientations of any triangle in a 9-edge graph: those six edges on three vertices would need at least five additional edges to incorporate the other four vertices.

## 3. Contract the disjoint triangles

Let the vertex-disjoint triangles be A and B. Their six directed edges use six vertices, leaving one vertex x and exactly three other edges. Contract A and B. Strong connectivity of the quotient on `{A,B,x}` and the edge count force those three edges to form a directed 3-cycle of components. In particular every remaining edge goes between distinct components; there is no reverse internal triangle edge and no directed 2-cycle.

Any additional directed triangle not equal to A or B must project to a closed directed walk in the quotient and hence use all three connector edges. It is a 3-cycle in the original graph iff the incoming/outgoing connector at A meet the same A vertex and likewise at B. There is then exactly one such connector triangle, and it meets A and B at one vertex each. No other triangle vertex set exists.

Because there is no reverse orientation for any triangle, each directed triangle has positive imbalance. Therefore both disjoint original triangles are imbalanced, as claimed. The separate supported-path theorem `frontier-20261028-ph7-five-edge-path-and-hidden-sum-bound-v1.md` SHA256 `f38f7874e21431cf3a1661c566570b215f656c59d9d9d0b1c73bc876ea31381b` supplies the additional exactly-five-edge supported path condition. □

## Review boundary and exact remaining problem

A disjoint review should check the edge-count fact with contraction, both shared-edge orientations, all possible new triangles on an equality quotient, the zero/positive triangle-imbalance cases, and the underlying capacity/packing certificates. This is a written graph reduction, not an exhaustive enumeration or a PH witness. The remaining 9-edge target is a finite family of connector-endpoint choices and real positive rates/inputs/exits; no such family is excluded here. Graphs with >=10 edges, global PH7 existence at8/9, order8, novelty and historical process repair remain open.

END — any nine-transition critical PH7 candidate has two disjoint directed triangles joined cyclically through the seventh state.
