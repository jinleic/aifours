# Axial leading reduction v1 — only three genuine graph families can evade the first-order test

Observed before creation: **2026-10-23T16:28:16-07:00**. PhysicsRQLS10. Same all-second-P, arbitrary-independent-complex-phase obligation from `selection-v2-axial-orientation-v1.md`. Written mathematics only, no executable enumeration, arithmetic program, solver or old assay.

**PARTIAL AUTHOR-WRITTEN REDUCTION, not a complete axial no-go.** This classifies every possible first-order graph failure into three explicit residual families. It does not turn those singular leading reductions into phase witnesses or actual low-rank matrices.

## 1. The new first block and the correct nonsymmetric bridge

In pair order(H,V0,V1,V2), H is the horizontal axis pair{1,2}; V0,V1,V2 are the three vertical pairs. All vertical roots are oriented y=1 to y=2. Thus

    A0=2*[0 0 0 0;0 0 1 1;0 1 0 1;0 1 1 0].

Call its isolated vertex H, and its triangle B={V0,V1,V2}. No assumption P_rho M symmetric is used.

Let Q0 be the literal first character matrix, Q1 arbitrary second, Dj=diag(Qj_(i,rho(i))) and s=i sqrt7. The exact coefficient matrix has expansion

    M=N+sM1+s²M2,
    M1=(P_rho Q1-Q0-D1+D0 P_rho)/8,
    N=J-I-P_rho+Fix(rho).

The even5×5 block of N is invertible modulo s. Projecting M1 onto the odd pair space gives

    M1|odd=-(A0+A1)/8,

where Aj has zero diagonal and off-diagonal entries

    (Aj)_ab=[Qj_(r_a,r_b)-Qj_(r_a,rho(r_b))
               -Qj_(rho(r_a),r_b)+Qj_(rho(r_a),rho(r_b))]/2.

This calculation does not require either Qj to preserve rho. Both diagonal correction terms are retained when obtaining the zero diagonal. Consequently

    rank_F7(A0+A1)>=3  ⇒  rank_K M>=8.

The fixed-point norm-descent argument applies to this rho as well: for N z=0, its single fixed coordinate vanishes modulo7; primitive equal-norm K-vectors are impossible; rank8 complex kernels are scalar extensions of a K-line. The full proof is in `candidate-CONFERENCE-GLUING-rank8-v1.md`, whose broader use here remains part of the new packet's reconstruction, not an inherited blanket parent acceptance. Thus every leading-rank>=3 case is excluded for arbitrary complex phases.

## 2. Complete second-grid graph catalogue

For any Q1, the four pair-difference vectors in A2⊕A2 yield the following A1 support/magnitude shapes, with every pair label and orientation allowed:

1. triangle plus isolated vertex, weights(2,2,2) or(2,1,1), with positive or negative cycle-product as appropriate to the complementary rook signatures;
2. a signed matching of two magnitude1 edges;
3. complete K4 with all weights1;
4. complete K4 with one weight2 and five weight1 edges;
5. a paw: a triangle with one weight2 and two weight1 edges, plus a pendant weight1 edge;
6. a diamond with one weight2 and four weight1 edges; its heavy edge is incident to a degree2 vertex, not the edge connecting its two degree3 vertices;
7. complete K4 with a weight2 perfect matching and four weight1 edges;
8. weighted K2,2 with two heavy edges incident to one vertex (weights2,2,1,1);
9. K2,2 with four magnitude2 entries and the signed-Hadamard cycle condition.

This is the same **combinatorial** pair-root catalogue proved by the prior signature classification, not its old central-first rank conclusion. It is independent of which first orientation is under study. A brief source reconstruction is: k4 gives a parallel-root triangle or two disjoint unit edges; k3 gives complete-one-heavy or a paw; k2 gives all-light K4, a diamond, a two-heavy K4, a weighted K2,2 or the central all-heavy K2,2; negating the literal second Q1 gives the complementary k0/k1 shapes and reverses odd-cycle signs. The actual k2 diamond always has its only heavy edge incident to a missing-edge endpoint, as the explicit pair endpoints in the previous classification show. No arbitrary signed graph is admitted beyond these root shapes.

Let L=A0+A1. H's incident entries come entirely from A1. The old B-triangle entries are2 plus the corresponding A1 entry. A cancellation requires exactly A1=-2; a light±1 edge cannot cancel. All nonzero integer entries considered below have magnitude at most4 and hence stay nonzero modulo7.

## 3. All high-degree-H cases close immediately

If H has degree3 in A1, avoiding the three H-based triangles would require **all three** B edges to cancel. Every graph in the catalogue with H degree3 has at most two heavy edges total, so this is impossible. Thus a nonzero triangle remains and rank L>=3.

This closes all complete graphs, the hub-H paw case, and the degree3-H diamond case, for all signs.

If A1 is either K2,2 shape, H has degree2 and its two neighbours are not adjacent in A1. Their L edge is therefore the unchanged2, giving a nonzero H-triangle. Both weighted and all-heavy bipartite shapes close.

If A1 is the signed two-edge matching, H has degree1 and the B-triangle has two unchanged2 edges and a third2±1. All are nonzero, so it closes.

For a diamond with H degree2, the edge between its two neighbours is a light edge, not the heavy edge, by the actual diamond property in the catalogue. It cannot cancel2; the H-triangle remains. Thus every diamond closes.

## 4. Paw cases: only one pendant-star configuration remains

If H is a degree2 triangle vertex, a surviving edge between its two neighbours gives an H-triangle. To avoid that it must be the heavy edge with value-2. H's two incident edges are then light±1. The non-neighbour k is the pendant, joined to one of those neighbours by a light edge p=±1. L is a4-cycle with cross block

    [a    b]
    [2  2+p],        a,b=±1.

Its determinant a(2+p)-2b is nonzero, because|2+p| is1 or3, never2; its magnitude is at most5, so not0 modulo7 either. Hence rank L=4.

If H is the pendant, first inspect the triangle B. Unless a heavy edge of value-2 cancels, it remains a nonzero triangle. If the cancelled edge is incident to the paw hub, L is a path on four vertices; its determinant is the product of the squared two end-edge weights, nonzero modulo7.

The only paw failure left is:

**P:** H is the pendant, and the cancelled heavy-2 edge joins the two non-hub triangle vertices, opposite the hub. The remaining L is a three-leaf star, of rank2. This is a true residual family, not a claimed phase solution. Its two remaining triangle weights2±1 and its pendant weight±1 are retained.

## 5. Triangle-plus-isolated cases

If H lies on the A1 triangle, its two neighbours i,j must have L_ij=0 to avoid an H-triangle. Hence A1_ij=-2. Their incident H-edge magnitudes are equal (both2 in the all-heavy case, or both1 when the unique heavy edge is opposite H). The fourth vertex k is A1-isolated, so the resulting4-cycle has cross block

    [a b]
    [2 2].

The determinant2(a-b) is nonzero modulo7 unless a=b. The equality case has negative triangle product a*b*(-2), so it can only be the negative-cycle triangle class, not a positive A2-root triangle.

Thus the remaining family is:

**T1:** the second triangle contains H, its opposite edge is heavy-2, its two H-incident edges are equal, and its isolated vertex K is one of the three first vertical vertices. L has rank2. Every K and both possible light magnitudes/signs remain in scope.

If H is also the second isolated vertex, L is supported only on B. It has rank3 unless at least one heavy A1 edge equals-2 and cancels. Therefore the final residual is:

**T0:** the second triangle has the same isolated H and at least one heavy-2 cancellation. Its reduced L has rank0 or2. All-heavy and mixed(2,1,1) triangles, and both cycle-sign types, remain retained.

## 6. Complete first-order disposition and actual next step

Every genuine A1 in the root catalogue has been treated by H degree0,1,2 or3. All cases outside **T0,T1,P** have rank L>=3, hence actual rank M>=8 and no arbitrary complex phase vector. No enumeration, numerical rank, field/alphabet restriction on delta, or central-first symmetry was used.

The already written partial-symmetry descent closes a genuine part of T0, including actual C'=conjugate(C) where the full M has rank5: if the second core shares g(x,y)=(x,-y), averaging preserves three actual unit coordinates and leaves an invariant kernel of dimension at most1, allowing primitive norm descent. It does **not** close every T0 core or the new T1/P families.

The remaining analysis must use **both** actual mixed blocks. In the even/odd split,

    (M1)_EO=(B1-B0)/8,
    (M1)_OE=-(B1+B0)^T G_E/16,

where B0 is the fixed first core's rank-one mixed block, and B1 is arbitrary genuine second-grid mixed data. Treating these as negatives of one transpose, or dropping B0, would silently restore the false old symmetry. The goal is to close or exhibit an exact local lead in T0,T1,P, then form one complete axial packet for its own reconstruction.

This is not the complete orientation packet and no new reconstruction/acceptance is requested for a merely partial split. Old parent support remains bounded to the old first/rho route. The permanently superseded old scientific source stays UNRUN; no program or control is admitted for this new orientation. Full maximal1-RQLS10 remains UNKNOWN.
