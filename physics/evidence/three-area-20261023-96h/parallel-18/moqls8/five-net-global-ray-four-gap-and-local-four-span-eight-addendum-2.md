# FIVE-net: GLOBAL ray-four gap, local four-span>=8, ENTIRE3+4+1 and4+4 exclusions

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE.** Actual precreation clock bound: **2026-10-26T06:07:18-0700 PDT**. This is an additive NEW packet, not an edit of any frozen/reviewed packet. No independent/parent/formal/executable/novelty acceptance.

## 1. Exact original remaining interface; predecessor inputs and delta

Let N be ANY actual FIVE-net of order8. Q is an arbitrary complex C8 unit assignment whose entries on EVERY actual N-line form an ONB. In an original FOUR-member MOQLS8 family this is precisely a selected member Q with THREE classical members. No fifth family, affine net, real-entry ansatz, artificial local ONB at cells or catalogue hypothesis is used.

Actual intrinsic components of the finite ray set are mutually orthogonal. A component V of dimension r has8r cells and r entries in every N-line, forming an ONB of V. A ray means a complex projective ray; individual phases never count as distinct rays. Its global cell multiplicity is m. Real projector spans have dimensions b locally and a globally.

The ENTIRE173LF `five-net-qutrit-ray-gap-and-span-budget-v1.md`, SHA256 **4adb77be94c8e2f867aa5581e89122e5d759dbc530f1017f6c2c264828018aa1**, and ENTIRE120LF `five-net-qutrit-span-six-and-3plus5-exclusion-addendum-1.md`, SHA256 **3556699f530c89006bdcf3ec0f70dd9b24d6cb1f58c80c6dd9312bc28a1eae13**, remain unchanged. Their whole written union supplies the ACTUAL range budget29-a>=15r(8-r)/16, the new qutrit b3>=6 and the ordinary general ONB span b_r>=2r-1. Those inputs require fresh complete reconstruction at this actual mate count; no accepted FIVE-family local bound is substituted.

New claims proved here:

1. EVERY nonfixed actual ray has m<=3, in ALL component dimensions. In particular m4 is excluded GLOBALLY, not merely in a qutrit/four-space.
2. EVERY irreducible dimension4 component has b4>=8 at the FIVE-net interface.
3. ENTIRE actual partitions3+4+1 and4+4 are excluded by the SAME actual range budget. The earlier3+5 exclusion remains separate and supported only at its own named union.

The global ray proof is reproduced from the start below. The local4 proof uses a pure-edge spectral-cone representation and actual grid incidence, NOT a list of degree4 unitary zero patterns.

## 2. Positive-cell identities and the m5/6/7 gap

Fix an actual unit ray v with m<8. Each class contains m distinct lines occupied by v, because a line is an ONB. Put d=8-m. Write

    g_x=|<v,Q_x>|^2;  S={x:0<g_x<1};  L=|S|.

Any line occupied by v has all other g0. Each of the d unoccupied lines in a class has positive-cell mass1 and at least TWO S-cells: a sole positive mass1 would be another occurrence of v. Thus S is partitioned into d groups by every N-class, with mass1 per group, and

    sum_S g=d,      2d<=L<=d^2.

The upper bound uses the actual d unused rows/d unused columns. Two distinct net classes cannot join the same pair of cells. The simple actual collinearity graph G on S therefore has

    e(G)>=5 L(L-d)/(2d),      e(G)<=L(L-1)/2,
    hence (5-d)L<=4d.

At d1, L<=1 contradicts L>=2. At d2,3L<=8 contradicts L>=4. At d3, L6 is forced; every positive group is a pair and all five class matchings are disjoint, so G=K6. The six actual Q-vectors are mutually orthogonal, whereas their squared overlaps with v sum3, contradicting Bessel. Thus m7,m6,m5 are impossible. This is the same earlier ray-gap argument, explicitly recalled so it is not a hidden four-full-mate premise.

At m8, v occurs in every board row; every other actual ray is orthogonal to v. Hence v is a fixed one-dimensional intrinsic component. Such classical rays are ALLOWED. In any irreducible component of dimension>1 all its actual rays are nonfixed.

## 3. At m4 the complement graph has at most six edges, except a degree-two case

Now suppose m4, so d4. The preceding identities give8<=L<=16 and total positive mass4. Every unused N-line has TWO, THREE or FOUR S-cells. For a non-row class it meets each of the four unused rows at most once; for a row line the four unused columns give the same upper bound. Thus the upper size4 is GLOBAL, not a low-component-dimension assumption.

In one class let n2,n3,n4 count positive groups of those sizes. Their sum is4 and L=2n2+3n3+4n4. The class edge count is

    n2+3n3+6n4 =2L-12+n4 =3L-24+n2.

Since the five class edge sets are disjoint,

    e(G)>=max(10L-60,15L-120).

Let H be the simple complement of G on the ACTUAL S-cells. At L8 all class groups are pairs, so G is5-regular and H is2-regular. At9<=L<=12,

    e(H)<=(L^2-21L+120)/2<=6,

by convexity and endpoint values6,6. At12<=L<=16,

    e(H)<=(L^2-31L+240)/2<=6,

by convexity and endpoint values6,0. Therefore for EVERY9<=L<=16, H has at most SIX edges. This replaces a long support enumeration by one actual graph inequality; it does not replace actual rows with an arbitrary rotation graph.

## 4. Two elementary spectral bounds, with their proofs

### 4.1 A graph with at most six edges

For any finite graph K with clique number<=3 and weights w_i>=0 summing1,

    sum_{ij edge} w_i w_j<=1/3.

Indeed choose a maximizing weight vector with minimum positive support. Two nonadjacent positive vertices can have all their combined weight moved to the one with larger linear coefficient without decreasing the objective. At a maximizer this reduces positive support, a contradiction. The positive support is therefore a clique of size<=3, and the objective there is(1-sum w_i^2)/2<=1/3. Compactness of the finite simplex supplies a maximizer; no graph software is used.

Let rho be the largest adjacency eigenvalue of H. A unit Rayleigh maximizer can be chosen nonnegative by replacing its coordinates with absolute values. For this x, Cauchy and the preceding weighted inequality give

    rho^2=4(sum_{ij edge}x_i x_j)^2
          <=4e(H) sum_{ij edge}x_i^2x_j^2
          <=4e(H)/3<=8<9

when H has no K4. Thus rho<3. If H has a K4 and at most six edges, it is EXACTLY K4 plus isolated vertices, and rho3. These are the ONLY possibilities. For the L8 degree-two case directly rho2, by the degree bound and A_H*1=2*1.

### 4.2 Actual complex Gram domination

Let B have the actual Q_x, x in S, as columns, and C=B*B. Its diagonal is1. Every G-edge gives C_xy0, since the cells share an ACTUAL ONB line. The remaining off-diagonal entries satisfy |C_xy|<=1. For arbitrary complex z, with w_i=|z_i|,

    z* C z <= ||z||^2+2sum_{ij in H}|z_i||z_j|
            <=(1+rho)||z||^2.

Thus C<=(1+rho)I and the frame operator T=BB* also satisfies T<=(1+rho)I on C8. This keeps ALL arbitrary complex phases; no reflection/real Gram ansatz is made.

But <v,Tv>=sum_S g=4. The cases rho<3 are impossible. In the only equality case H=K4 plus isolates, C<=4I and T<=4I, and mass4 forces Tv=4v. Put z=B*v. EVERY z_i is nonzero by the definition of S, and Cz=4z. Each isolated H-vertex has its entire C-row equal to the corresponding identity row, so z_i=4z_i, impossible. Such an isolate EXISTS because L>=9 while the K4 has only four vertices.

The L8 case gives T<=3I, also impossible. This closes ALL m4 supports, in every actual component dimension.

Consequently

    every actual ray has m in{1,2,3,8}; m8 is fixed.      (GLOBALGAP)

No enumeration/interpreter/eigenvalue program or numerical approximation was used; all inequalities above are exact WRITTEN proofs.

## 5. Closed actual orthogonal pairs and the all-light conditional lemma

Suppose p,q are two distinct orthogonal actual rays such that EVERY actual N-line containing either contains the other. Each class gives a perfect matching between the p-occurrences and q-occurrences; their multiplicities are equal, say m. No pair of cells can be matched by two classes. Thus the ACTUAL2m-cell graph is simple5-regular bipartite, and m>=5. In an irreducible component of dimension>1 this contradicts GLOBALGAP. We call this the closed-pair obstruction. It concerns actual rays/cells, not a basis vector merely introduced in a proof.

A useful consequence: if all rays in a nontrivial component have at most two coordinates in ONE ACTUAL component ONB E, it is impossible. An actual two-supported ray p on coordinates a,b has both coefficients nonzero. Any other at-most-two-supported ray orthogonal to it either lies in their coordinate two-plane B and is its unique orthogonal ray q, or lies in B-perp. A ray meeting B in exactly one coordinate cannot be orthogonal to p, because its inner product has one nonzero summand. An actual ONB containing p therefore MUST contain q: the other r-1 vectors cannot all fit B-perp of dimension r-2. Conversely every line containing q contains p. The closed-pair obstruction applies. If no such ray exists, all rays are E axes and the component splits into singleton components.

This ALL-LIGHT conclusion is conditional on ALL actual rays having coordinate weight<=2 in the SAME actual E. It is NOT inferred from the four columns meeting a component row. The latter inference in the earlier HELD checkpoint lead was wrong and is withdrawn in §10.

## 6. An assumed irreducible four-span7 cannot have an actual3+1 transition

Let V be an irreducible dimension4 component, and assume its real projector span S has dimension7. The general ONB bound supplies b4>=7, so this is the only lower equality to exclude. Fix ANY actual local line ONB E; its diagonal space D_E has dimension4, and W=Off_E(S) has dimension3.

Suppose an ACTUAL local basis F has a connected3 block on A=span(e0,e1,e2) and singleton e3. The connected3 block contributes two independent real off-diagonal directions supported inside A: its diagonal algebra meets the E-diagonal algebra only in scalars on that block. Thus W has at most ONE real dimension of cross terms between A and e3.

Those cross terms cannot vanish identically, for then all actual projectors are block diagonal on A/e3 and V is reducible. Choose their fixed nonzero A-vector c. Any actual rank-one projector P_q has cross vector q_A*conjugate(q_3) proportional to c, so every actual ray lies in

    A  OR  B=span(c,e3).

Irreducibility supplies an actual ray p genuinely mixing c/e3. Every A-pure ray orthogonal to it lies in A intersect c-perp, a dimension2 space. An actual four-ONB containing p must therefore include the unique orthogonal B-ray q. The same holds with p,q exchanged. Both are actual irreducible-component rays, and the closed-pair obstruction contradicts their existence.

Thus NO actual connected3+1 transition is possible under b4=7. c and B are necessary cone descriptors, NOT replacement cell frames or falsely asserted actual rays. The paired p,q, by contrast, are explicitly forced actual entries in every relevant line.

## 7. Actual grid incidence forces a pure-edge direction

Fix ANY actual E line basis in V. Choose its N-class as board rows and another actual class as columns; the net axioms allow this relabeling and all Q line conditions remain unchanged. The selected row has exactly FOUR V-cells, in FOUR DISTINCT columns. Each of those four column bases shares an E-axis ray.

A unitary transition sharing an axis has only the following possibilities on the remaining coordinates: monomial; one2 block plus two singletons; connected3 block plus a singleton. Section6 excluded the last. If all four columns were monomial, each would contain all four E rays, giving each ray at least FOUR global occurrences, contrary to GLOBALGAP in the irreducible component. Hence one of these ACTUAL columns has a nontrivial2+1+1 transition.

Its projectors supply a nonzero off-diagonal Hermitian direction X on one coordinate edge a,b only. Subtracting its E-diagonal part keeps X in S, because D_E is contained in S. Thus S contains an ACTUAL pure-edge direction. Only the FOUR intersecting columns were used. The OTHER FOUR columns were NOT assumed to share an E-ray, and no false ALL-light conclusion has been made.

## 8. Pure-edge spectral cones exclude EVERY connected4 transition

Suppose an ACTUAL local basis F is connected on all four E coordinates. Then D_E intersect D_F consists of scalars: a shared diagonal operator has equal E-eigenvalues across every F-ray support, and connectedness propagates this to all four coordinates. Hence dim(D_E+D_F)=4+4-1=7, so

    S=D_E+D_F.

Take the nonzero pure ab-edge X supplied in §7. Write X=D+Y with D E-diagonal and Y F-diagonal. Thus Y is a Hermitian operator whose ONLY E-off-diagonal entries are the nonzero ab pair. Its ab block has two DISTINCT eigenvalues lambda+,lambda- and orthogonal eigenrays w+,w-, each with BOTH a,b coefficients nonzero. The other E-axes c,d have eigenvalues lambda_c,lambda_d.

F diagonalizes Y. Connectedness of F forces BOTH lambda_c and lambda_d to belong to{lambda+,lambda-}. Otherwise an eigenspace supported only on c/d, separate from the ab block, would produce a separate coordinate component of F. There are exactly two eigenvalue placements up to relabeling; no zero-pattern catalogue or phase enumeration is needed.

### 8.1 Both c,d have the same ab eigenvalue

Suppose both equal lambda+. F-projectors then lie in the three-space A=span(w+,c,d) or on the singleton w-. Their B-to-C cross blocks, B=span(ea,eb), C=span(ec,ed), have B-range only span(w+). D_E has no such cross block. Since S=D_E+D_F, every actual rank-one q with nonzero C part has its B part proportional to w+. Thus ALL actual rays lie in

    B  OR  A.

In an actual ONB containing ea, any A-pure ray orthogonal to ea lies in C, because <ea,w+> is nonzero. Any B-pure orthogonal ray is ONLY eb. Three other orthonormal rays cannot all fit the dimension2 space C, so eb is forced. The same reasoning with eb forces ea. This is a closed ACTUAL pair, impossible by §5. The placement with both eigenvalues lambda- is identical after naming the two eigenspaces, not a new WLOG deletion of complex cases.

### 8.2 c,d have different ab eigenvalues

Now F's eigenspaces are A+=span(w+,c) and A-=span(w-,d). Their projectors have zero c-d coherence; B-c cross vectors are parallel to w+, and B-d cross vectors to w-. All these properties persist in S=D_E+D_F. A rank-one actual q therefore has q_c*conjugate(q_d)=0; if q_c is nonzero, its B component is parallel to w+, and if q_d is nonzero it is parallel to w-. Consequently ALL actual rays lie in

    B OR A+ OR A-.

For a basis containing ea, a ray in A+ orthogonal to it must be c-pure, since <ea,w+> is nonzero; a ray in A- must be d-pure. A B-pure orthogonal ray is ONLY eb. Without eb the other three orthonormal rays would lie in span(c,d), again impossible. The reverse implication for a basis containing eb is the same, because BOTH w+,w- have nonzero b coefficient. Thus ea,eb form a closed actual pair and §5 contradicts the case.

The spectral cones are exhaustive for Y and connected F. The w-rays themselves need NOT be actual entries and are never substituted as independent local frames. Only the ORIGINAL E-rays ea,eb are used in the closed-pair conclusion. Arbitrary complex phases of X/F/w are retained by the Hermitian eigenvalue argument.

We have excluded EVERY actual connected4 transition relative E, not merely a full-support4 matrix or a selected13-nonzero staircase.

## 9. Local span8 and ENTIRE new partition exclusions

Section6 excludes connected3+1; §8 excludes connected4. Every actual basis transition relative the SAME actual E therefore decomposes into blocks of sizes at most2. Thus EVERY actual component ray has weight<=2 in E. The conditional ALL-LIGHT lemma §5 applies and makes the dimension4 component reducible, a contradiction.

Therefore

    EVERY irreducible dimension4 component has b4>=8.   (LOCAL8)

Combine LOCAL8 with the predecessor's complete LOCAL6 proof and actual range bound. If Q has partition3+4+1, then by span additivity a>=6+8+1=15, but either its3- or4-component gives a<=14. If it has partition4+4, then a>=8+8=16 whereas a<=14. Hence BOTH ENTIRE strata are excluded at the original cardinalityFOUR q1/FIVE-net interface.

The predecessor independently excludes3+5. No positive-q FIVE-family residual is revived. Remaining q1 FOUR-family component possibilities are not asserted to exist:3+3+1+1 retains a14 with local qutrit spans6; a single irreducible3,4,5,6,7or8 component accompanied by the appropriate singleton rays remains an exact compatibility problem. Intrinsic2 components are excluded as previously proved. The present local4 result upgrades4+1+1+1+1 to12<=a<=14 but DOES NOT close it.

The higher-component/four-family q2/q3/q4 coupled problems, exact M(8), a fourth companion to any OTHER triple, A10/A11 and the THREE exact GB UNKNOWNs are NOT solved by this packet. An accepted FIVE-family classicality theorem is not silently turned into a numerical maximum. Classical q0/five-families remain allowed.

## 10. Additive held-lead correction and exact assurance

`original-four-family-checkpoint-v4.json` records an ADDITIVE correction of checkpointv3's HELD, undelivered argument: the statement that minrowdegree>=3 forces ALL Q-cells light was wrong because a dimension4 component row meets only FOUR component columns, not all eight. The consequent claim that only a13-nonzero staircase remains was NOT established and is withdrawn. No accepted/frozen body,164LF triple proof,173LF ray/range proof or120LF qutrit proof consumed those tentative claims. They are not premises here. The NEW proof uses actual four-column incidence only to obtain a pure edge, and then treats ALL connected4 transitions by the spectral cones above. This is a replacement representation, not a suppressed countercase or a retroactive clean draft history.

All mathematical claims here are exact WRITTEN AUTHOR CANDIDATES; separate ENTIRE-source reconstruction and parent disposition are required before promotion. Named ordinary imports are finite-dimensional complex Hermitian/ONB/PSD spectral theory, finite-simplex compactness, Cauchy/Bessel, the actual net axioms and the predecessor's fully exposed general span/range/qutrit proofs. No missing transitive proof is certified by a hash/headline. No configured-family/human/formal/kernel/executable/novelty clearance. Generic clique/Gram/cone methods may be PRIOR; specialist theorem priority remains UNCLEARED.

No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO, private float/decimal gloss or numerical parameter trial was used. Metadata date/hashes/LF only. ALL own permanent intake read-order PROCESS MAJOR findings/currentv112+visiblev105/v107/v109 and older parent/owner/reviewer process histories remain; no clean-thought/runtime census or retroactive cure. The new held-argument correction is additionally preserved as above.

No source/shared edits, git/deletion/publication; exclusive owner-root writes; same18/original primary/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/<=30min substantive checkpoints. No early final-park or roundcompletion. Original remaining companion/higher-component geometry continues.
