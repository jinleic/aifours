# In the original q1 four-family, every intrinsic C6 has projector span at least thirteen

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual native clock observed before this write: Thu Oct 29 13:27:53 PDT 2026. This is a strict local improvement over the earlier adopted unrestricted C6 lower bound of 12, but ONLY in the original four-family q1 setting: the selected member has THREE actual classical mates. It is not an unrestricted C6 bound, a C6 nonexistence theorem, or a q1 exclusion. The sole adopted import is GAP3; all other mathematics and the actual five-net caller are derived here.

## 1. Original physical objects and exact scope

Let Q,L1,L2,L3 be ANY four ordinary MOQLS of order 8: all actual rows and columns are ONBs in C^8, and every pair of members has its 64 same-cell tensor products forming an ONB of C^8 tensor C^8. Equivalently, for distinct cells y,z and distinct members M,N,

    <M_y,M_z><N_y,N_z>=0.                                        (1)

Assume L1,L2,L3 are classical in their OWN global output bases, independently chosen. Phases and individual output unitaries are arbitrary. Let C be an intrinsic irreducible component of Q with complex span W of dimension SIX. Different intrinsic components are orthogonal. Compressing an actual Q-row ONB to W shows that every row meets C in a six-ONB of W, so C contains 48 original cells. With P_z=|Q_z><Q_z|,

    sum_{z in C} P_z=8 P_W.

Let S=span_R{P_z:z in C}, and b=dim_R S. We prove **b>=13**.

**Only imported theorem, GAP3:** every ray in a nontrivial intrinsic component of any member of an ordinary four-MOQLS(8) has GLOBAL multiplicity at most three. This is Gate 1 of `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. No C4, C5, C6, tested-qutrit, prior span, budget, catalogue, solver or unreviewed result is used as a premise. In particular, later parent adoptions of no-C4, LOCAL5 and q4 are not inputs here.

## 2. The five net lines are actual Q-ONBs

In the fixed ONB of each classical L_i, its rays label an ordinary Latin square: every row and column has each label once. For i!=j, (1) forces every ordered pair of L_i,L_j labels to occur at most once and therefore exactly once among the 64 cells. The row class, column class and three classical symbol classes are consequently five line classes: every line has eight cells, every two lines in different classes meet exactly once, and two lines of the same class are disjoint.

For Q, every classical-symbol line is an actual Q-ONB: its eight L_i rays agree, so (1) makes its Q entries pairwise orthogonal. Every row and column is also an actual Q-ONB. Thus every one of the five lines through a selected component cell y meets C in a six-ONB of W. These five lines share ONLY the cell y. Their other 35 original cells, and in particular their 25 other C-cells, are pairwise distinct across the five lines. No affine net, common output frame, phase restriction or catalogue is assumed.

## 3. Two physical star identities

Fix an actual component cell y with ray u and let H=W intersect u-perp, dimension five. For each mate L_i, evaluate the L_i factor in the Q-L_i tensor-ONB resolution along (L_i)_y. The z=y term is P_u; all other terms vanish unless z is outside y's row and column and Q_z is perpendicular to u. The weights for the three mates at any distinct z are disjoint by their pair-product orthogonality, and each is at most one. Adding back the disjoint original row and column star ONBs gives

    A_u := sum_{z in C, Q_z perpendicular to u} P_z >=5(P_W-P_u).  (STAR)

In particular every actual u has at least 25 orthogonal-star CELLS. If a star ray g is perpendicular to every other distinct star ray, evaluating STAR at g gives m(g)>=5, contradicting GAP3.

We also need a two-ray consequence. Let u,v be orthogonal actual rays of C and put K=W intersect u-perp intersect v-perp. The Q rays which are NOT perpendicular to u contribute on H a positive operator

    F_u=8I_H-A_u|_H <=3I_H.

Compress STAR(v) to K and remove its terms which are not perpendicular to u; their contribution is at most F_u|_K. Therefore

    sum_{z in C, Q_z perpendicular to both u and v} P_K P_z P_K
          >=2I_K.                                                (COMMON)

In particular, the common-star actual rays project to a spanning set of EVERY subspace of K. This is derived from both actual resolutions; no virtual Q entry is inserted.

## 4. Uniform two- and three-space ray capacities

### 4.1 Two-space: at most three rays, with a unique third

Let B be any complex two-space in W. Its total Q projection mass is 16. For each distinct actual ray v in B, STAR(v) evaluated along its unique in-plane perpendicular direction v' gives at least five units of projection mass on the cells whose nonzero B-projection is parallel to v'. Those target directions and cell sets are distinct for distinct v. Thus B contains at most three distinct actual component rays.

If three rays in B had no orthopair, their own occurrence cells would contribute at least three more units outside the three target sets, giving at least 18>16. Hence three contain an orthopair. The third ray is nonorthogonal to both, and its occurrence cells lie outside the target sets, so 15+m(third)<=16. It is actual; therefore its GLOBAL multiplicity is exactly one. Consequently TWO different unordered actual ONBs of the same two-plane are impossible.

### 4.2 Three-space: at most six rays

Let D be any complex three-space in W, and let v_1,...,v_N be the distinct actual component rays in D. Compress STAR(v_i) to D and take traces: each gives at least 10. For each cell z with nonzero D-projection, the tested rays perpendicular to Q_z lie in a two-plane and number at most three by 4.1. Since the total D-projection mass is 24,

    10N <=3*24=72,  so N<=7.                                    (2)

Suppose N=7. For an actual occurrence of each v_i, write d_i for the number of OTHER v_j perpendicular to it. The common two-plane cap gives d_i<=3. The slack in (2) is at most two, so summing the seven occurrence contributions to the deficit gives sum_i(3-d_i)<=2. The degree sum is even while 21 is odd, so the deficit is odd: it is exactly one. Thus six vertices have degree three and one vertex has degree two.

The three neighbors of a degree-three vertex lie in a two-plane; by 4.1 they contain exactly one orthopair. Hence that vertex lies in exactly one orthogonality triangle. The degree-two vertex is in at most one triangle, so triangles are vertex-disjoint. The six degree-three vertices must be covered by two disjoint triangles; the seventh vertex is outside them. Each triangle is an actual three-ONB of D. The six triangle vertices each need one additional edge, and the seventh vertex supplies at most two of those endpoints, so there are at least TWO orthogonality edges between the two disjoint ONBs.

That is impossible for a 3-by-3 unitary with no shared basis ray: two zeros in one row/column give a singleton common ray; two zeros in different rows and columns leave their two rows with only one common possible nonzero column, forcing another zero and again a singleton. Thus two disjoint three-ONBs have at most one zero overlap. Contradiction; **N<=6**.

Two useful exact corollaries will be used:

- Two disjoint actual three-ONBs cannot have a FULL 3-by-3 transition. Otherwise no plane contains three of their six rays: among any triple two belong to one ONB, and the third would have to be perpendicular to the remaining ray of that ONB, a zero overlap. The double count then gives 60<=2*24=48, impossible.
- A connected 3-by-3 transition has no shared ray and at most one zero; hence for two actual three-ONBs it has EXACTLY one zero. The six actual rays exhaust D by N<=6. The one-zero pattern has an actual ray f in the plane of two E axes and the remaining E axis e perpendicular to f. Each of f,e is the third ray beyond an actual orthopair in a two-plane, hence each has multiplicity one. The orthogonality graph of the six rays is two triangles joined by the single edge e-f, so their ONLY actual three-ONBs are the two original bases.

## 5. Cross-image bookkeeping and an elementary unitary lemma

For actual u let T_u be the real projector span of its u-orthogonal component rays, sigma=dim T_u. Write the real image of Z -> P_u Z P_H on S as {u chi*:chi in L}. The kernel contains RP_u and T_u in direct sum, so

    b>=1+sigma+dim_R L.                                          (3)

L is not contained in a complex line. Otherwise all u-active rays would lie in one complex two-plane B=span(u,a). Irreducibility gives an actual mixed u-active ray x. Every u-inactive ray orthogonal to x lies in B-perp; the other five vectors of an actual six-ONB through x cannot all fit in its four-dimensional complement. The unique in-plane orthogonal partner x' is actual and is perpendicular to every other distinct star-x ray. STAR(x) gives m(x')>=5, contrary to GAP3. Therefore dim_R L>=2.

Assume for contradiction that **b<=12**. Then sigma<=9. The projected H-parts of all u-active rays lie in the complex space Pi=span_C L; if dim_R L=2, dim_C Pi<=2.

We shall also use this elementary fact.

**Lemma U5.** Every connected-support 5-by-5 unitary has a row OR a column with at most one zero.

Proof. If not, every row and every column has at most three nonzero entries. A connected unitary has no degree-one row or column. Suppose a row has support {1,2}. Any other row touching either coordinate must touch BOTH, since two unitary rows cannot overlap in exactly one nonzero position. The two columns have the same support, of size at least two and at most three. If it has size two, the corresponding 2-by-2 square submatrix is unitary and forms a disconnected block. If it has size three, call the other two rows p,q. Their restrictions to {1,2} are nonzero and both perpendicular to the first row, hence proportional; their overlap there is nonzero. Orthogonality forces p and q to share one further coordinate. Their supports have size at most three, so these three rows are supported in one three-coordinate space, form its ONB, and again give a disconnected block. Transpose gives no degree-two column. Thus the support is 3-regular on both sides.

The five row zero-sets are two-element subsets of five columns, and each column belongs to exactly two zero-sets. Two row supports cannot meet in only one position, so their zero-sets must intersect. No zero-set can repeat: a duplicate exhausts the zero counts at both its vertices and leaves every other zero-set disjoint from it. The five distinct zero-sets thus form a simple 2-regular graph on five vertices, necessarily a five-cycle, which has disjoint edges. Contradiction. ∎

## 6. No connected five-block or 4+1 star-line transition at b<=12

At the selected cell y, choose the Q row's five-ONB E of H, and compare it with the five-ONB F from any OTHER net line through the SAME y. Every shared ray of E and F occurs at two different cells, because the two net lines meet only at y.

For two ONBs, the intersection of their real diagonal algebras has dimension equal to the number of connected blocks of their unitary transition: common diagonal eigenvalues must agree along every nonzero support edge, and one scalar per block is possible. Thus a connected k-block contributes k-1 independent off-diagonal directions. A connected two-block is impossible, because its two different two-ONBs would give FOUR actual rays in one plane, contrary to 4.1. Hence the only transition partitions without a two-block are

    5,    4+1,    3+1+1,    1+1+1+1+1.                         (4)

### 6.1 Connected five-block

Suppose E,F have connected five-dimensional transition. Their diagonal algebras add dimension nine, so sigma>=9. By (3), b<=12 forces sigma=9 and dim_R L=2. Hence T_u=D_E+D_F and Pi=span_C L has dimension at most two.

By Lemma U5, swapping E,F if needed, some E-axis e_i has at most one zero overlap with the F-basis. Let v be ANY actual u-star ray perpendicular to e_i. Write P_v=D+Y with D E-diagonal and Y F-diagonal. From P_v e_i=0, e_i is an eigenvector of Y. If there is no F-zero in its row, all F eigenvalues of Y coincide, so P_v is E-diagonal and v is an E-axis.

If there is exactly one zero, at F_j, then after absorbing a scalar into D,

    P_v = D' + t P_(F_j),        t real,                         (5)

where F_j is perpendicular to e_i and has at least two nonzero E-coordinates (otherwise the transition has a singleton block). Every actual rank-one projector of form (5) is an E-axis or P_(F_j). Indeed if t!=0 its off-diagonal support is exactly the complete support of F_j. With at least three supported coordinates, rank-one purity recovers every diagonal from a triple of off-entries and trace one forces P_v=P_(F_j). With exactly two supported coordinates, 4.1 permits only the two E-axis rays plus the already actual F_j in that plane.

Choose nonzero xi in H perpendicular to Pi, e_i and, if present, F_j. Such a vector exists: these conditions span at most four complex dimensions of H. All u-active rays have H-projections in Pi and make no xi contribution. Every u-inactive actual ray perpendicular to e_i is another E-axis or F_j; F_j contributes zero and the E-axes contribute at most 3||xi||^2 by GAP3. This contradicts STAR(e_i), whose right side is 5||xi||^2. Thus a connected five-block is impossible.

### 6.2 A 4+1 block

Suppose F is connected on A4 and shares the singleton E-axis e. Its A-off-directions span three dimensions. Since the whole H-off-space has dimension sigma-5<=4, the A-to-Ce cross image has real dimension at most one. If it is zero, every u-star ray is in A or on e, and STAR(u) along e gives m(e)>=5, contrary to GAP3.

If the cross image has dimension one, an actual mixed star ray supplies its rank-one generator a e*. Every mixed star ray lies in the same plane B=span(a,e). Choose such a mixed ray x. All pure-A star rays perpendicular to x lie in A intersect a-perp, dimension three; pure e is not perpendicular to x. COMMON(u,x) requires common-star rays to span the four-space H intersect x-perp, so the unique in-plane orthogonal partner x' is actual. The plane B now contains the orthopair x,x' and the third ray e. Section 4.1 forces m(e)=1. But e lies on both net lines E,F at different cells, so m(e)>=2. Contradiction.

## 7. A 3+1+1 pivot: all cross cases except one are impossible

If all five line bases through y were equal to E, every E-ray would occur on each of the five distinct net lines, contradicting GAP3. By (4) and Section 6, some other line has a connected 3+1+1 transition. Let A be its connected three-coordinate block and B its orthogonal two-plane, with E and F sharing the actual B axes e,f. Thus m(e),m(f)>=2. Their A-bases are disjoint. By Section 4.2 they have exactly one zero; their six actual A rays are all actual component rays in A, and each A-basis contains one globally unique ray. In particular these are the ONLY two actual three-ONBs in A.

The H-off-space has dimension at most four. The A-block contributes two independent off-directions V_A, so its A-B cross image X has real dimension at most two.

### 7.1 Cross dimension zero or one

If X=0, all u-star rays lie in A or B. STAR(u) compressed to B has trace at least 10. But B has at most three actual rays; if it has three they consist of an orthopair and a third of multiplicity one. Its total possible occurrence count is at most 3+3+1=7, contradiction.

If dim_R X=1, an actual mixed ray supplies a rank-one generator a b_0*. All u-star rays are pure A, pure B, or lie in C=span(a,b_0). B already contains e,f. A possible third pure-B ray w is nonorthogonal to both e,f and has m(w)=1. If w is not perpendicular to b_0, no genuine C-mixed ray can be perpendicular to it. All common-star rays of u and w outside B then lie in A, dimension three. COMMON(u,w) forces the unique B-partner w' to be actual, giving four distinct actual B-rays e,f,w,w', contrary to 4.1. Thus the only possible third pure-B ray is b_0-perp, with multiplicity one. Evaluate STAR(u) along b_0-perp: e,f contribute at most three, the possible third contributes one, and A or C rays contribute zero. This is at most four, contradicting five.

### 7.2 Cross dimension two: the real pencil

If dim_R X=2, then the off-space has dimension exactly four and its cross-kernel is exactly V_A. Consequently every pure-B star projector is E_B-diagonal; the ONLY pure-B rays are e,f. X is spanned by rank-one crosses of actual mixed rays. Choose two real-independent such crosses a_1 b_1*, a_2 b_2*. If their B-factors are parallel, all mixed B-parts have one direction. If their A-factors are parallel, all mixed A-parts have one direction. Otherwise both factor pairs are complex-independent, and any real combination with both coefficients nonzero has rank two, so every actual mixed ray lies in one of

    C_1=span(a_1,b_1),        C_2=span(a_2,b_2),

with a_1,a_2 independent in A and b_1,b_2 independent in B. These alternatives cover even complex-scalar multiples: they fall in a common-factor case.

The common-B case is impossible: test STAR(u) in B perpendicular to the common B-factor. Only e,f contribute and their weighted sum is at most three.

The common-A case is also impossible. Let its A-factor be a_0. The six pure-A rays are the two original A-ONBs, with one unique ray r in E_A and one unique ray s in F_A; r perpendicular s. Their weighted projector sum is at most

    3I_A+3I_A-2(P_r+P_s)=6I_A-2(P_r+P_s).

Choose nonzero eta in span(r,s) intersect a_0-perp, which exists in A3. Pure-B and mixed rays make zero eta contribution; pure-A rays contribute at most 4||eta||^2, contradicting STAR(u)>=5I on eta.

The ONLY remaining pencil is therefore the independent two-plane case above. We now use the ORIGINAL five-net lines, rather than claiming that this algebraic cone alone is impossible.

## 8. The independent two-plane cone cannot supply the five net lines

Every u-star ray is pure A, one of the two B axes e,f, or a genuine mixed ray in C_1 or C_2. The pure-A rays are EXACTLY the six from E_A,F_A. A pure-only five-ONB of H must contain e,f and a three-ONB of A, so it is either E_A union {e,f} or F_A union {e,f}. Each such basis includes its own globally unique ray r or s. The two already occurring pivot net lines use them, and neither pure-only basis can occur on another line through y.

Consider any actual five-ONB of H containing genuine mixed rays. Let n_i be its number of mixed rays in C_i. It cannot have more than two in one C_i. The independent factors imply:

- If (n_1,n_2)=(1,0) or (0,1), the remaining pure-A rays lie in a two-space and pure-B rays in a one-space, giving at most four vectors total.
- If (n_1,n_2)=(1,1), the remaining pure-A rays lie in the one-space A intersect a_1-perp intersect a_2-perp, and no pure-B ray is available; there are at most three vectors total.
- If it has exactly two mixed rays in C_i and none in the other, the pair is an ONB of C_i. The remaining three vectors must include the unique pure-B ray perpendicular to b_i. As the ONLY pure-B rays are e,f, b_i itself is the OTHER actual B-axis. Then C_i contains its two mixed ONB rays plus this third actual ray b_i. Section 4.1 would force m(b_i)=1, but m(e),m(f)>=2. Impossible.
- If it has two mixed rays in one C_i and at least one in the other, orthogonality to the first in-plane ONB forces both a_1 perpendicular a_2 AND b_1 perpendicular b_2. The mixed planes are orthogonal. In that case one mixed ray in the other plane is insufficient to complete the five-ONB, because at most one pure-A ray and no pure-B ray remain. Hence the basis has TWO mixed rays in EACH C_i, and its fifth ray is the unique pure-A direction

    t = A intersect a_1-perp intersect a_2-perp.

Thus every possible mixed five-ONB contains the SAME actual t. Since all pure-A rays are among the six E_A,F_A rays, t already occurs on one of the two pivot net lines. Its multiplicity is at most three, and the five net lines through y share no other cell, so at most TWO further net lines through y can be mixed. At most TWO can be pure-only, as just proved. Four lines cannot cover the FIVE actual net lines through y. Contradiction.

This closes every possible 3+1+1 pivot and hence the assumption b<=12.

## 9. Result, exact residual and assurance

**Theorem, WRITTEN author candidate:** in any ordinary four-MOQLS(8) containing three actual classical members, every intrinsic SIX-dimensional component of the remaining member has real projector span **at least 13**.

All complex phases and every ordinary physical row, column, classical-symbol and pair-product ONB are retained. The proof uses only the adopted GAP3 statement plus elementary linear algebra and the derived actual five-net interface. Its new global three-space capacity is proved here and is not imported from a pending C4 review. The older unrestricted LOCAL6>=12 result was NOT weakened, changed or adopted anew; without the three classical mates this new span-13 argument does not apply.

This is a genuine q1 local increment, not a q1 no-go: intrinsic C6 with b>=13, all allowed C5/C7/C8 cases, and all compatibility/phase/gluing constraints remain open. It does not prove a C6 cannot exist or decide the original four-family existence/classicality alternative, M(8), maximum-three, A10, A11, source priority or novelty. Main's later same-harness q4 exclusion is a separately scoped parent composition, not inferred or re-proved by this packet. Its no-C4 and LOCAL5 adoptions are status only, not proof inputs here.

The source is immutable after pinning; a NEW full-scope reviewer must reconstruct STAR/COMMON, the 3-space capacity, Lemma U5, every cross-pencil case, the exact mixed-ONB counting and the five-net caller. No independent review, parent adoption, formal/kernel, human, configured-family, executable or novelty acceptance is asserted here. No scientific interpreter, selected numeric probe, solver, heavy/multi-GB run, external model CLI or nested agent was used. Earlier frozen packets and all historical cadence/process findings remain preserved.
