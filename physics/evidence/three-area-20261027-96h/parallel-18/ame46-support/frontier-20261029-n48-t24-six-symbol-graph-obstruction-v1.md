# A graph-theoretic obstruction for a six-symbol residual party at support 48

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 14:08:19 PDT 2026`; not an asserted completion time. **WRITTEN author candidate**, not reviewed, adopted, formally verified or novelty-cleared. No computation, enumeration, SAT result or certificate is a proof premise.

## 1. Exact theorem and scope

Let ψ be a normalized complex AME(4,6) state in a fixed product basis with support N=48 and exactly t=24 coefficients of modulus 1/6. Let E be its other 24 support words. **Assume that E has no pair of words at Hamming distance one.** Then no party has all six symbols appearing in E.

The no-distance-one property is an explicit hypothesis of this theorem, **not** an application of the recorded f127 lemma (which has N=46, t=26 scope). A separate written candidate at this exact N=48, t=24 scope, `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, SHA-256 `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`, proposes to derive no-distance-one from no-OLS(6); it is unreviewed and is not needed to establish the conditional theorem here. If that separate candidate is reviewed and adopted, this packet would then be applicable at its stated classical import boundary.

This is an elementary graph-theoretic replacement route for a previously explored six-symbol branch, not a claim of blind provenance or novelty. No earlier finite-classification or solver/certificate result is imported. No held v203/v124 material or pending-union claim is used. We do not exclude the remaining alphabet profiles, other values of t, support 48 in general, or assert a ≥49 bound.

## 2. Residual pair systems and parity fibers

In every 2|2 cut U=6ψ is unitary. Its t=24 modulus-one entries are singleton rows and columns. Removing them leaves a 12×12 unitary with 24 nonzeros, every row and column having degree two. Thus every one of the six pair-coordinate systems contains 12 E-carried values, each with exactly two E extensions; the other 24 values are P-carried singletons. A P word and an E word never share a pair value.

For any residual symbol a at party i, the number `d_i(a)` of its E partners at any other party is independent of that party: if p_i(a) P words use a, the six values of the other coordinate are partitioned into p_i(a) P-carried and `6−p_i(a)` E-carried values. If d_i(a)=1, every other coordinate is constant on E_a, giving only one E word and a singleton residual line, impossible. Hence d_i(a)≥2, and `Σ_{a∈E_i} d_i(a)=12`.

Suppose party A has all six E symbols. Each then has d_A(a)=2 and a four-word fiber. At each of B,C,D it uses two values twice. The no-distance-one hypothesis makes each projection onto any two of B,C,D injective: if two words in the same A fiber agreed on those two coordinates, they would differ only in the remaining coordinate. Four words therefore project bijectively onto the complete 2×2 rectangle for every pair of B,C,D. In particular, for fixed A=a and fixed B=b, the two E words use the two C values and the two D values, once each.

## 3. Six-edge incidence graphs and two unitary consequences

Index the six A fibers by edge labels `1,…,6`. For j∈{B,C,D}, form a loopless multigraph G_j: its vertices are the j symbols used by E, and the edge labeled a joins the two j symbols in A fiber a. Parallel edges are allowed. Let U_j be its 6×r_j binary edge–vertex incidence matrix; every row has two ones and every column has weight d_j(b)≥2.

For j≠k, the integer intersection of a column of U_j and a column of U_k counts the number of A fibers containing a specified (j,k) value. By the full-rectangle property of each fiber, this is exactly the number of E words at that pair value. Hence

`(U_j^T U_k)_{bc}∈{0,2}`.                                      (I)

In particular the column spaces W_j of U_j over F₂ are pairwise orthogonal in F₂⁶.

We use two consequences of the **same tensor's** unitary flattenings:

**(O) Two singleton intersections are impossible.** If two different edge labels a,a′ share exactly one graph vertex in each of two graphs G_j,G_k, their jk rectangles intersect in exactly one pair value. Each A fiber supplies exactly one word at that pair; the corresponding two rows of the (A,remaining-party)|(j,k) flattening are distinct and share exactly that one column. Their inner product cannot vanish.

**(Q) Identical endpoints in all three graphs are impossible.** If two edge labels a,a′ have identical endpoints in G_B,G_C,G_D, their two fibers contain eight words on two values at each party. In each partner-pair system, their common 2×2 rectangle is filled once by each fiber and is saturated at multiplicity two. Pair values involving A are also saturated within the corresponding fiber. Thus these eight words form an isolated 4×4 unitary block in every cut. After normalizing, they give AME(4,2), which is impossible by the following elementary argument.

For a pure four-qubit density matrix write its Pauli weight sums as A_0,…,A_4, with A_0=1. Maximal two-qubit marginals give A_1=A_2=0. Each three-qubit marginal has purity 1/2, since its complementary one-qubit marginal is I/2; Pauli orthogonality gives weight-three sum 3 on each of the four triples, hence A_3=12. Global purity gives A_4=16−1−12=3. The spin-flipped density matrix is positive, but its overlap with the original would be `(1−12+3)/16=−1/2`, impossible.

## 4. All three binary incidence spaces cannot have rank at least three

For a loopless graph on r vertices and c connected components, its binary incidence-column space has dimension r−c: the kernel of its incidence map consists exactly of vertex labelings constant on components. Each component has at least two vertices.

Suppose all three W_j have rank at least 3. Pairwise orthogonality in the six-dimensional space implies every rank is exactly 3. Then `W_C=W_B^⊥=W_D`, and W_C is self-orthogonal of dimension 3, hence self-dual; consequently all three spaces coincide with one self-dual W.

A self-dual binary subspace W⊂F₂⁶ of dimension 3 is spanned by the indicators of three disjoint pairs. For completeness: every w∈W has even weight, so the all-ones vector belongs to W=W^⊥. Choose a nonzero w different from all-ones. Its weight is 2 or 4; in the latter case adding all-ones gives a weight-2 vector. Permute the six coordinates so it is e₁+e₂. Orthogonality makes the first two coordinates equal in every vector of W. Projecting to the last four coordinates gives a self-dual dimension-2 subspace; its all-ones vector and a nonzero distinct vector yield another weight-2 vector. Lift it and, if needed, add e₁+e₂ to clear the first two coordinates. The sum with all-ones gives the remaining disjoint weight-2 pair.

Every column of every U_j lies in this common space, so its entries agree on each of the three row-label pairs. The two edges in any such pair therefore have identical endpoints in all three graphs, contradicting (Q).

## 5. A graph on two vertices

If some G_j has r_j=2, every one of its six edges joins those two vertices. Since 12 distinct E pair values occur at (j,k), `2r_k≥12`; so both other partner graphs have r=6. Their six edges have total degree 12 and every vertex has degree at least two, hence every degree is two. Each has at most three components and rank at least three. By orthogonality their ranks are both exactly three, so each has three components of two vertices joined by two parallel edges.

The first such graph's column space is the self-dual span of the three edge-pair indicators. Orthogonality and equal dimension force the second graph to have the same column space, so it has identical endpoint rows on the same edge pairs. The two-vertex graph has identical endpoints for every pair of edges. This contradicts (Q).

## 6. A graph on three vertices

Suppose some G_j has r_j=3. The edge set in any column of U_k or U_l, for the other two graphs, induces degree 0 or 2 at each vertex of G_j by (I). It is nonempty, hence is either two parallel edges (a **2-cycle**) or a triangle with one edge from each of the three possible vertex pairs. Every column has size 2 or 3. Pair capacity gives r_k,r_l≥4.

### 6.1 A four-vertex partner is impossible

If r_k=4, its four column weights sum to 12 and are at most 3, so all four columns are triangles. Every edge label lies in exactly two of those columns. A 2-cycle column of U_l would share exactly one label with some triangle of U_k: take a triangle containing one of its two parallel edges; a triangle contains only one edge from that parallel class. Thus U_l also has only triangle columns and r_l=4.

Each of the three parallel classes in G_j then contains exactly two edge labels: the four U_k triangles use four occurrences from each class, and each edge label occurs twice. Label each class's two edges 0 and 1. A triangle is a binary triple. Fix any U_l triangle. By (I), each U_k triangle agrees with it in 0 or 2 coordinates, so all U_k triples have the same parity. Each bit value occurs twice among those four triples, because each graph edge is incident with two U_k vertices. The only balanced multiset of four binary triples of one parity is the complete parity class, each triple once.

Choose one edge from each of two different parallel classes in G_j. They share exactly one vertex of G_j. The complete parity class realizes each choice of two bits once, so the corresponding two incidence rows of U_k also share exactly one vertex. This contradicts (O).

### 6.2 Both remaining partners have at least five vertices

Now suppose r_k,r_l≥5. Since their column weights are 2 or 3 and sum to 12, a graph on 6 vertices has no triangle columns, and a graph on 5 vertices has exactly two triangle columns.

If U_l has a triangle column T, any 2-cycle column of U_k containing a label of T meets T in exactly one label, forbidden by (I). Each of the three labels of T occurs in exactly two U_k columns, so all those occurrences must be in U_k's triangle columns. If r_k=6 there are none; if r_k=5 there are exactly two, and both must equal T. Either case contradicts (I), the latter because a U_k triangle and T would intersect in three labels. By symmetry neither partner has a triangle column. Both therefore have r=6 and all columns are 2-cycles.

For columns of U_k and U_l, two-element supports must be identical or disjoint by (I). Every row label occurs in two columns of each matrix. If two distinct U_k column supports met in one label, a U_l column containing that label would have to equal both, impossible. Thus the distinct U_k supports are three disjoint pairs, each repeated twice, and the U_l supports use the same pairs. Each such pair is a 2-cycle in G_j, so its two labels have the same endpoints there as well. This contradicts (Q).

## 7. A rank-two graph on four vertices

All remaining graphs have at least four vertices. If a rank is below 3, it must be 2 and its graph G_j has r_j=4 with exactly two components. Since every component has at least two vertices, each component consists of two vertices joined by parallel edges. Let P and Q be their respective disjoint edge-label sets, with `|P|,|Q|≥2` and `|P|+|Q|=6`.

For a vertex of either other graph, its incident edge set meets P in 0 or 2 labels and Q in 0 or 2 labels, by (I). Equivalently, the edges of P form a 2-regular subgraph of each other graph, as do the edges of Q.

If |P|=2 (or symmetrically |Q|=2), those two edges have identical endpoints in each other graph, since a loopless 2-edge 2-regular graph consists of two parallel edges. They also have identical endpoints in G_j, contradicting (Q).

The remaining case is |P|=|Q|=3. In each other graph, P forms a triangle and Q forms a triangle. As each graph has at least four vertices, at least one P-triangle vertex in G_k is not a Q-triangle vertex. Its incidence-column support is a two-element subset S of P. In G_l the three P-triangle vertices have three distinct two-element incidence subsets of P. Intersecting any one of their full incidence columns with S sees only P labels; in a three-element set two 2-subsets meet in 1 or 2 labels. Condition (I) forces intersection 2, so all three subsets would have to equal S, contradiction.

All possible ranks and residual alphabet sizes are exhausted. Hence A cannot have six E symbols. ∎

## 8. Consequence and review boundary

For the stated conditional theorem, a size-two E alphabet would require every partner alphabet to have size six, since each pair projection has 12 values. Therefore all residual alphabets have size 3, 4 or 5. This still leaves numerous support-48 profiles; neither an actual support-48 tensor nor an N≥49 theorem is supplied.

The author has prior exposure to earlier N=48 structural candidates. This is not a blind proof. Review should independently check the exact no-distance-one hypothesis, the parity-fiber rectangle property, (O)/(Q), the binary self-dual-space argument, and every rank-1/r=3/r=4 case. No SAT, selected-instance search, held result, pending union, or computer enumerator is an input.
