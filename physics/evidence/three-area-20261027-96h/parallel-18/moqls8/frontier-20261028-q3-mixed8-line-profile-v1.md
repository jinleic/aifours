# q3 eight-mixed-cell boundary: only 3+3+2 line profiles remain

**WRITTEN author candidate; disjoint mathematical review pending.** Let an actual ordinary four-MOQLS(8) contain one classical member L and a nonclassical Q; let its other two members R,S be arbitrary complex QLS. Relative to any Q basis line of the three-net (rows, columns, L symbols), suppose Q has exactly eight mixed cells. Then **each of the three net-line classes partitions those eight cells as `3+3+2`**. In particular the `2+2+2+2` boundary is impossible in an actual four-family. This is a necessary residual classification, not a full q3 exclusion, witness, M(8) claim, A10/A11 closure or novelty result.

All Q,R,S are actual ONBs on every three-net line: on a fixed L-symbol line the classical partner is identical, forcing each quantum member's vectors orthogonal. Choose one such line as row 0 and independently normalize Q,R,S and L there to e_j. A mixed Q ray is not one of Q's first-row axes. A line containing a mixed point has at least two mixed points. On a two-mixed line, the mixed rays have the same two-axis support; on a three-mixed line, at most one mixed ray has support size 2. These ONB facts are proved in `frontier-20261028-four-family-one-classical-mixed7-v1.md`, SHA256 7eafc43e165d379c3fb7297ccf40afe9cb381f5da02442f68beaad71b4afafe8, and are a named written input here.

## 1. No line has four or more mixed cells

Let H be the eight mixed points. If a net line has k points of H, each of those points needs at least one mixed neighbor on each of its other two class-lines. Any outside point can meet at most two on-line points, one in each other class, because two cells share at most one net line. Hence `2k≤2(8−k)` and k≤4.

Suppose a line L has four mixed points X and the remaining mixed points form Y, also of size four. Each x∈X needs a mixed neighbor on each of its two other class-lines, giving at least eight X–Y adjacencies. Each y∈Y can meet at most two X points, so there are exactly eight and the cross graph is simple 2-regular bipartite. Each crossing line contains exactly two mixed points. The two-line lemma makes the Q supports equal two-sets along every cross edge.

Every connected cross-graph component is an even cycle and contains at least two X points. It cannot contain three X points, since those Q rays all lie in the same two-dimensional support but are mutually orthogonal on L. Therefore the graph has two K2,2 components. In one component, its two X rays form an ONB of their common two-space; either Y ray is in that same two-space and is orthogonal to both X rays on the two crossing net lines, impossible. Thus no line contains four mixed points.

Every class consequently partitions the eight mixed points as either `2+2+2+2` or `3+3+2`.

## 2. A 2+2+2+2 class forces a 3-regular bipartite trade

Suppose one class has four two-point lines. Every Q ray on H then has support size 2. No class can have a three-point line, because that would contain three support-2 rays, contrary to the three-line lemma; no line has four by §1. Thus **all three classes** partition H into pairs.

The mixed-cell graph has eight vertices and is simple 3-regular, with one edge per class through each vertex. It is connected: a disconnected 3-regular graph on eight vertices would have two four-vertex components, each K4; within such a component the two-line lemma forces all Q rays into one two-space, impossible for its triangle. Hence all eight Q rays have one common two-axis support `{a,b}`. Actual orthogonality in C² makes the graph bipartite, with collinear Q rays within each part and perpendicular rays across parts. The two parts have four vertices each, and a simple 3-regular bipartite graph on 4+4 vertices is `K_(4,4)` minus a perfect matching.

Label the parts p_1,...,p_4 and n_1,...,n_4 so that p_i,n_i are the four **nonedges**. For R, the four R_p rays are pairwise orthogonal because the corresponding Q rays are collinear and Q⊗R is an ONB. The four R_n rays are likewise orthogonal. For i≠j, p_i and n_j share a net line, so `R_(p_i) ⟂ R_(n_j)`. Because all Q_H rays use both axes a,b, their actual Q⊗R products are orthogonal to the first-row products at a,b, so all eight R_H rays lie in the six-dimensional complement of first-row R axes a,b. The same holds for S.

Let U be the four-dimensional span of the orthonormal R_p rays in that six-space. Each `R_(n_i)` has the form `α_i R_(p_i) + w_i`, with `w_i∈U^⊥`. The four w_i are pairwise orthogonal because the R_n rays are orthogonal. Since `dim U^⊥=2`, at least two w_i vanish, and their α_i are nonzero. The same argument for S gives at least two indices with nonzero `β_i=⟨S_(p_i),S_(n_i)⟩`.

The original R⊗S product ONB requires `α_i β_i=0` for every i. Thus the two nonzero-index sets are disjoint, each has exactly two indices, and they partition `{1,2,3,4}`. For R on the complementary two indices, α_i=0 and the two w_i are unit orthogonal vectors spanning U^⊥; on the other two, w_i=0. Hence **all eight R_H rays span the entire six-space**. The same conclusion holds for S, with the complementary index set.

Each row meets H in 0 or 2 points. Eight mixed cells occupy four rows, leaving four rows with no mixed points, one of which is row 0. Pick an off-first-row cell y with Q_y=e_a in one of the other three rows; that row is an ONB of light first-row rays. Every Q_H ray overlaps e_a, so Q⊗R and Q⊗S orthogonality force R_y and S_y orthogonal to all their respective H rays. Both therefore lie in their own `span{e_a,e_b}`. Their products with the first-row Q⊗R and Q⊗S vectors at a force both to be e_b. But then their R⊗S product at y coincides with the first-row R⊗S product at b, contradiction.

Therefore a `2+2+2+2` class is impossible, leaving `3+3+2` in every class when Q has exactly eight mixed cells. The deduction assumes the actual fourth-family product ONBs, not just a support graph. The remaining all-`3+3+2` profile is open here, and the separately written ≥8 q3 bound is not strengthened to ≥9 by this packet.

A disjoint reviewer should check the four-line 2-regular graph step, bipartite 4+4 structure, both six-dimensional equality decompositions, the R⊗S complementary-index argument and the off-row singleton contradiction. No catalogue, numerical solver, finite witness or source-priority claim is an input.
