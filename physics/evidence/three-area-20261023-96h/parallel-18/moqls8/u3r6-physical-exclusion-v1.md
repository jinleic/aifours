# Full physical exclusion of U3-6 by a ray gap and a weighted orthogonality graph — candidate v1

Actual clock observed before creation: **2026-10-23T16:22:24-0700**. PhysicsMOQLS8, physics-4, same original primary and deadline. **AUTHOR-WRITTEN FULL EXCLUSION CANDIDATE, NOT ACCEPTED CLOSURE.** No scientific program, arithmetic interpreter, enumeration, solver, CAS, Lean, compilation, tests, modelCLI or nested agent was used. Every finite case below is written explicitly; no catalogue is imported.

This attacks the exact parent-assigned U3R-6 physical residual. In fact the proof retains a COMPLEX isolated three-space throughout; the previously derived local real form is not needed. It does not replace the four mates by real vectors, replace the board by a colouring, or exhibit an abstract control as a physical family.

## 1. Literal full physical hypothesis and claimed conclusion

Let Q_1,...,Q_5 be full MOQLS(8): every actual row/column is an ONB of C^8, and every pair of product-cell arrays is an ONB of C^8 tensor C^8. Suppose Q_1 has the U3-6 structure:

- a globally isolated COMPLEX three-space A;
- exactly24actual A-cells, three per actual row/column;
- five fixed orthogonal complement rays, one occurrence of each per line;
- real Hermitian span of the24A-projectors has dimension6.

All four other squares, all64cells and ALL tensor-product equations remain physical and arbitrary complex. The claim is that this family does NOT exist. This would exclude U3R-6 as well, without assuming reality.

For any distinct cells x,y and squares s!=u,

    <Q_s(x),Q_s(y)><Q_u(x),Q_u(y)>=0.                     (T)

Product completeness gives

    sum_x P_sx tensor P_ux=I_8 tensor I_8,                 (P)
    P_sx=Q_s(x)Q_s(x)^*.

The only checked new-core lemmas consumed are MATCH and ISOLATE, recalled at their physical interfaces below. Old K-count exclusions, T16/F14, GA/GB, native proofs and classical catalogues are NOT premises.

## 2. Ray-weighted Parseval, with multiplicities5/6/7 excluded

We restate the physical weighted identity so the new multiplicity4 step can be reconstructed directly.

If an actual Q_1 ray v occurs exactly m<8times, its occurrences are in m distinct rows and columns. Put d=8-m. Every other nonzero overlap with v occurs on the residual d-by-d missing-row/missing-column board. Let

    g_x=|<v,Q_1(x)>|^2.

The residual row/column sums are1, its total weight is d and every positive g_x is strictly below1 (otherwise there is another v-occurrence). Each residual line needs at least two positive weights.

For each mate s=2,...,5, the repeated-v entries form an orthonormal m-set spanning K_s. Every residual entry at g_x>0 lies in W_s=K_s-perp. Taking the v,v matrix element of(P) gives

    sum_residual g_x P_sx=P_(W_s),          dim W_s=d.      (1)

At a positive cell x with w=g_x, the Q_s(x) diagonal element has total1 and own contribution w. Row/column orthogonality removes two DISJOINT other-cell weight sums1-w each. The remaining off-diagonal supports are disjoint across the FOUR mates by(T), and each squared overlap is<=1. Therefore

    4(1-w)<=d-w-2(1-w)=d-2+w,
    w>=(6-d)/5.                                           (2)

For d<=3, two positive weights>=3/5 cannot sum1. Thus actual ray multiplicities5,6,7 are impossible. This is the earlier checked weighted argument, reproduced here rather than substituted by a numerical test.

## 3. The new gap: exact multiplicity4 is also impossible

**Lemma M4.** No ray of ANY member of a full five-MOQLS(8) family has exact multiplicity4. No sector or reality hypothesis is needed for this lemma.

*Proof.* Take m=d=4 in §2. Every positive residual g is>=2/5 and<1. Every residual row/column must therefore have exactly TWO positive entries: one would have weight1, while three would exceed1. The positive support is a simple two-regular bipartite graph on four actual rows and four actual columns.

At a residual row, the ray v lies in the span of its two positive-overlap ONB vectors, by the exact expansion of v in that row basis. Since neither is parallel to v, either vector together with v determines that two-space F. The same holds in each column. A shared positive cell propagates the same F along a connected component, and the orthogonal partner is unique inside F. Thus every component alternates two FIXED orthogonal Q_1 rays, up to phases.

A simple two-regular4-by4board is either one8cycle or two4cycles. A component cannot use only one row/column, since a cell cannot be doubled; a6cycle would leave an impossible one-row component.

### One8cycle

Each alternating ray has four occurrences, giving two disjoint matchings on the same four actual rows and columns. In every mate, all eight entries lie in W_s of dimension4 by(1). Each repeated Q_1 ray makes its four mate vectors orthonormal, hence an ONB of W_s. MATCH applies: a transition row to the other matching is nonempty, has TWO distinct row/column zeros and is disjoint across four mates. It would require4<=4-2, contradiction.

### Two4cycles

Each component is an actual2-by2rectangle. In every mate its four vectors are PAIRWISE orthogonal: row/column pairs are already orthogonal, while each of the two opposite diagonal pairs has the same Q_1 ray and is forced orthogonal by(T). All four belong to W_s of dimension4, so the component gives an ONB of W_s.

Fix a cell of the first rectangle, with Q_1 ray u. The second rectangle's two Q_1 rays span a two-space F_2 containing v. Since u has nonzero overlap with v, u cannot be orthogonal to all of F_2. It overlaps at least one of those two rays, which occupies TWO cells of the second rectangle. Equation(T) therefore forces zeros at both positions in EVERY mate's transition row from the fixed cell to the second rectangle's W_s-ONB. Each row is nonempty; across the four mates they are disjoint. Only at most TWO positions remain for FOUR nonempty supports, contradiction.

Both exhaustive support cases fail. This proves M4 with all complex phases retained. QED.

## 4. Sector ray multiplicities and orthogonality mass

Collapse the actual24A-cells of Q_1 into distinct complex rays. Give ray r its positive integer multiplicity m_r. The total weight is

    sum_r m_r=24.                                         (3)

Multiplicities4/5/6/7 are excluded by §§2–3. An A-ray of multiplicity8 would appear in every actual row/column, forcing every other A-vector into its orthogonal two-plane. That two-plane is globally isolated in Q_1. Two different pairs there violate ISOLATE at8<12; only one pair would leave the local A-projector span at most3, contrary to6. Thus

    1<=m_r<=3 for every actual A-ray.                     (4)

For each mate s, the24 product vectors on A-cells are mutually orthogonal inside A tensor C^8 of dimension24. They form a COMPLETE ONB, so partial trace gives

    sum_(A-cells x) P_sx=3I_8.                             (5)

At a fixed A-cell x, each mate has total squared overlap3 on the A-cells, own term1 and off-diagonal mass2. Across four mates the off-diagonal supports are disjoint by(T), and can occur only where Q_1(x) is orthogonal to Q_1(y). Hence each A-ray is orthogonal to at least EIGHT A-cells, counted with ray multiplicity.

Let G be the simple graph on DISTINCT A-rays, adjacent exactly when orthogonal in complex C^3. Write

    d(v)=ordinary degree,
    D(v)=sum_(u adjacent v) m_u.

Then

    D(v)>=8 for EVERY vertex v.                           (6)

Each vertex belongs to an actual ONB triangle, because each actual cell lies on an A-ONB row. These facts use the full physical mates; an abstract tight frame alone would not imply them.

## 5. Complex three-space graph geometry and the weighted Moore inequality

Two distinct complex rays in C^3 have a one-dimensional common orthogonal complement. Thus G has NO4cycle: opposite vertices would have two distinct common orthogonal rays. For the same reason the graph induced on N(v) is a matching: within the complex two-space v-perp each ray has a unique orthogonal ray.

Fix v of weight m=m_v. Let U(v) be the TOTAL WEIGHT of the neighbors left UNMATCHED inside N(v). For a neighbor u, decompose its weighted degree into the contribution m from v, a possible one internal-neighbor contribution, and outside-neighborhood weight. No vertex outside {v} union N(v) can be adjacent to TWO different members of N(v), or it would make a4cycle. Therefore those outside weight sets are disjoint.

Summing D(u)>=8 over the d(v) neighbors and adding v and N(v) gives

    24 >= m + d(v)(8-m) + U(v).                           (WM)

For clarity about the exact cancellation: the sum of internal-neighbor contributions is the total weight of MATCHED vertices of N(v), each counted once via its partner. Its difference from D(v) is exactly U(v). Thus(WM) does not double-count an outside ray or omit unmatched mass.

This is a written weighted count, not an imported graph census.

## 6. Weight1 disappears; all degrees are3or4

By(4) every neighbor weight is at most3, so(6) forces d(v)>=3.

If m_v=2, d(v)>=4 would make(WM) at least2+4*6=26>24. Hence every weight2 vertex has degree exactly3. It cannot have a weight1 neighbor: the other two neighbors have weights at most3 each, giving D(v)<=1+3+3=7.

If m_v=1, degree>=4 similarly gives at least1+4*7=29>24, so its degree is3. Its weighted degree>=8 rules out a weight1 neighbor. A weight2 neighbor was just shown impossible. Hence all three neighbors have weight3. Three vertices in the induced neighborhood matching leave at least one unmatched, of weight3. Inequality(WM) now gives at least1+3*7+3=25>24. Contradiction.

Thus ALL weights are2or3. Weight2 vertices have degree3. A weight3 vertex cannot have degree>=5, since3+5*5=28>24. It has degree3or4. If its degree is4, (WM) has base23; an imperfect matching of its four neighbors leaves at least TWO unmatched vertices, total weight>=4, contradicting24. Consequently:

- every degree4 vertex has its neighborhood partitioned into exactly TWO orthogonal pairs, hence belongs to exactly TWO triangles;
- every degree3 vertex belongs to exactly ONE triangle: an actual ONB gives one, while a three-vertex neighborhood matching allows only one.

Every degree4 edge is a triangle edge. A degree3 vertex has exactly one remaining edge outside its unique triangle; that edge cannot meet a degree4 vertex, whose edges all lie in triangles. These remaining edges therefore form a PERFECT MATCHING on the degree3 vertices. Call them bare edges.

## 7. Triangle-intersection bookkeeping, with no catalogue

An orthogonal pair in C^3 has a unique third orthogonal ray, so two distinct triangles cannot share an edge. They can share one vertex; such a vertex has degree4 and belongs to exactly two triangles.

Define J with one vertex for EACH triangle of G and one edge for EACH shared degree4 ray. It is simple, of maximum degree3. J has no triangle: three pairwise intersections would form an orthogonal triple and force the original triangles equal. It has no4cycle: its four distinct intersection rays would form a4cycle in G. Thus J has girth at least5.

If G has N vertices and q triangles, and r of its vertices have degree4, then

    3q=N+r,
    r=3q-N,
    number of degree3 vertices=2N-3q.                    (7)

Bare edges form a perfect matching on the last set, so q is EVEN. Also N/3<=q<=2N/3.

A bare edge cannot connect degree3 vertices of triangles at J-distance0,1or2. Distance0 would already be a triangle edge. At distance1, let a be the shared ray, x the endpoint in the first triangle and z its other ray; then x-z-a-y-x would be a4cycle. At distance2, if a,b are the successive intersection rays, the cycle is x-a-b-y-x. All named rays are distinct because the endpoints have unique triangles and no ray belongs to three triangles. Hence bare endpoints must belong to triangles at J-distance>=3 or in different components.

We will also use this elementary size fact: a simple girth>=5 graph on SIX vertices has at most SIX edges. If acyclic it has at most5. A6cycle admits no chord without a triangle/4cycle. A5cycle admits no chord, and the sixth vertex can meet at most one cycle vertex, since any two attachments see a cycle path of length<=2 and make a triangle/4cycle. This exhausts its possible cycles.

## 8. The four exhaustive weight counts

Let h be the number of weight3 rays and l the number of weight2 rays. Equation(3) gives

    3h+2l=24.

Thus h is one of0,2,4,6,8. If h=0, every vertex has degree3 but weighted degree6, contradicting(6). The four positive possibilities now fail explicitly.

### h=2, l=9, N=11

Every weight2 vertex has degree3 and weighted degree>=8, so it has at least TWO weight3 neighbors. All nine light vertices would be common neighbors of the SAME two heavy vertices. Two distinct vertices in a4cycle-free graph have at most ONE common neighbor. Contradiction.

### h=4, l=6, N=10

Each light vertex has at least two heavy neighbors. Count pairs of heavy neighbors through light vertices. There are only binom(4,2)=6 heavy pairs, each permitting at most one common neighbor by4cycle-freeness. Six light vertices already require at least6pairs, so equality forces each light to meet exactly two heavy vertices and every heavy pair to have its unique light common neighbor. Label it x_AB for heavy pair A,B. Each light's third neighbor is light, so the light subgraph is a perfect matching.

Every heavy vertex meets its three pair-lights, of total weight6. It needs another neighbor to reach weighted degree8 and has degree at most4. That extra neighbor cannot be light, whose two heavy neighbors are already fixed; it is heavy. Thus the four heavy vertices form a perfect matching, say AB and CD.

Heavy A has neighbors B,x_AB,x_AC,x_AD. Its degree4 neighborhood MUST be a perfect matching by §6. Since B is adjacent to x_AB, the other pair must be x_AC-x_AD. But then

    C-x_AC-x_AD-D-C

is a4cycle, using the heavy edge CD. Contradiction.

### h=6, l=3, N=9

From(7), q is even and3<=q<=6, so q=4or6. If q=6, J has6vertices and r=18-9=9edges, contrary to the six-edge girth fact.

If q=4, J has4vertices and r=12-9=3edges. It has no cycle on four vertices, so it is a TREE: a four-vertex path or a three-leaf star. Every triangle of J-degree d contains3-d degree3 rays that require bare partners.

For the star every pair of triangles has distance<=2, so its leaf stubs cannot have bare partners. For the path, either internal triangle has degree2 and hence ONE degree3 ray requiring a bare partner, but its distance to every triangle is at most2. Again impossible. These are exactly the two tree shapes, with all bare edges retained.

### h=8, l=0, N=8

Equation(7) makes q even with8/3<=q<=16/3, so q=4. Then J has4vertices and r=12-8=4edges. Any graph on four vertices with four edges has a cycle of length at most4, contrary to J's girth>=5. Contradiction.

All weight counts are exhausted. No weighted orthogonality graph satisfying the FULL physical consequences can exist.

## 9. Candidate theorem and exact scope

The contradictions prove the claimed candidate exclusion of full physical U3-6, and therefore U3R-6. The argument did NOT assume the sector or mates real; all three-space geometry holds for distinct COMPLEX rays. Local span6 was used only to rule out the classical three-ray alternative in the multiplicity8 case, not to replace physical vectors by arbitrary operators.

A classical isolated sector is not excluded: its three rays may each have multiplicity8, and §4 correctly separates that allowed case. Thus complete classical MOQLS8 families are not accidentally ruled out.

No part of the proof is a board-only colouring, an abstract weighted graph treated as a witness, or a search miss treated as nonexistence. The graph conditions were all derived from the actual24sector cells and four complex physical mates. The finite weight cases and small J arguments are written proofs, not executable enumerations or unverified catalogue lookups.

## 10. Consequences requiring actual separate and parent reconstruction

If this physical exclusion is validated, combine it with the already supported all-object span11 reduction in the uniform packet: every nonclassical member of every five-MOQLS8 family has projector span at least12. The checked14surplus budget then excludes K4/K5 without ANY of the fifteen F14 native-input imports or T16/template normalization.

For full Problem16/n8 classicality, OLD K12/K3 still remain explicit separate premises excluding exactly1/2/3 nonclassical members. Their catalogue/native/checker/provenance limits are not erased. This manuscript does not freshly verify them and does not itself close their acceptance gates.

**No promotion is claimed now.** This complete new proof needs actual separate reconstruction on pinned bytes, especially LemmaM4, the weighted Moore count, the degree/triangle matching implications and all four weight cases. A clean review of the earlier reduction does not pre-certify this new exclusion. A10/A11, the three exact GB UNKNOWNs and all runtime HOLDs remain unchanged; no Boolean refutation, formal/kernel/human/novelty acceptance, publication or contact occurred.
