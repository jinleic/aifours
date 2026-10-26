# Uniform span12 obligation — consolidated all-object reduction to one complex three-space case, v1

**Status: AUTHOR-WRITTEN CANDIDATE / UNIFORM BOUND NOT PROVED.** This is the ONE consolidated manuscript requested by Main after `moqls8-mixed-route-parent-v1.md`. Exposure/ACK preceded new derivation in `uniform-span12-exposure-v1.json`, actual clock15:24:01-0700. The parent lead and prior optional B2 exposure are disclosed there; no blind/preregistered discovery claim.

No scientific executable, arithmetic script, enumeration, solver, Lean, compilation, tests, modelCLI, nested agent or new GO was used. All arguments below are written. Earlier frozen sources and the conditional assembly remain unchanged.

## 1. Literal uniform question and honest outcome

Let Q_1,...,Q_5 be EVERY actual family of five MOQLS(8): each array is8-by8 in C^8, every actual row and column is an ONB, and every pairwise product-cell array is an ONB of C^8 tensor C^8. Put

    a_s=dim_R span_R{Q_s(x)Q_s(x)^*: all64cells x}.

The parent-assigned uniform question is whether every nonclassical member has a_s>=12. No classical member, real form, template, phase alphabet, coordinate support or partial Gram realization is assumed.

The already checked LS theorem gives a_s>=11. This manuscript attacks the ONLY missing value11 directly. It proposes the following complete reduction, not a proof of the requested12bound:

> Any physical counterexample to uniform a_s>=12 can be chosen with Q_1 having a globally isolated COMPLEX three-dimensional sector A; the other five coordinate rays are fixed full rays of Q_1; there are24actual A-cells, three in each actual row/column; and the real span of their rank-one Hermitian projectors has dimension exactly6. All four other full squares remain arbitrary complex physical QLS.

Call this full-physical residual **U3-6**. Its exclusion is the first unproved case. A full physical U3-6 family would itself refute the uniform bound (and supply a nonclassical five-family), but no such family is constructed here. Abstract six-dimensional operator spaces, tight frames or support patterns are NOT physical counterexamples.

The new intermediate claims include an individual light-square theorem and a ray-multiplicity gap. They are part of this ONE reduction, not separate problem slots or accepted discovery counts. Every new step requires actual separate/parent reconstruction.

## 2. Physical identities and permitted old NEW-mathematics imports

For distinct cells x,y and distinct squares s,u,

    <Q_s(x),Q_s(y)> <Q_u(x),Q_u(y)>=0.                     (T)

For every s!=u, completeness of their64product vectors also gives

    sum_x P_{s,x} tensor P_{u,x}=I_8 tensor I_8,            (P)
    P_{s,x}=Q_s(x)Q_s(x)^*.

Every actual line may be used as an ONB frame independently in each square. The dimension a_s is invariant under output unitaries, phases and cell permutations.

We consume only the checked physical lemmas from the earlier written core, with their exact stated proof boundaries:

- **MATCH:** two disjoint ray-occurrence matchings on the same m actual rows/columns that are ONBs of the SAME m-space in each of the FOUR other squares require m>=6. For a fixed first-matching cell, two DIFFERENT second-matching cells share its row and column. Four nonempty disjoint transition supports must avoid those two positions, so4<=m-2.
- **ISOLATE:** a globally isolated two-space of Q_1 cannot use two different orthonormal ray-pairs at n8,t5. Distinct pair classes have every cross overlap nonzero, their repeated-ray dimension lower bounds sum to8, and MATCH makes every class use>=6rows.
- **ONE-CHANNEL:** if every Q_1 cell is B-pure, B-perp, or mixed in one fixed span(b,c), b in a two-space B and c in B-perp, and both a mixed cell and a B-pure ray outside{b,b-perp} occur, the two saturated row classes have sizes>=6 each, impossible in8rows.
- **LS:** a nonclassical member has a_s>=11 since8<2(5+1). This consumes the complete low-span proof, including overlapping edges and arbitrary complex line frames.

These are from `proof-low-span-rigidity-v1.md` and simple ISOLATE in `proof-isolated-sector-exclusion-v1.md`, with actual peer/parent written checks recorded by Main. NO K12/K3, T16, WMAN, GB/GA, F14, native proof or classical catalogue is a premise of the reduction below. The14budget is only the consequence bridge in §13, not a substitute for the missing uniform step.

## 3. Star saturation: one individual light square is classical

**Lemma L2.** In a physical five-MOQLS8 family, if ALL entries of ONE member Q_1 have weight<=2 in ANY actual line frame, that square is classical. The other four squares need not be light.

*Proof.* Choose that reference basis e_1,...,e_8. A noncoordinate vector with support{a,b} in any ONB must be paired with its unique orthogonal ray on that same two-space. Indeed another basis vector cannot meet its support in exactly one position; the two-space must be completely spanned, giving a2-by2unitary block. This applies to every actual row and every column because ALL cell supports have weight<=2.

Fix coordinate a. Let m_a be the number of cells on ray e_a. They occupy m_a distinct rows/columns, and in every remaining row/column exactly two vectors carry coordinate a, in one noncoordinate orthonormal pair on some{a,b}. Put k_a=8-m_a. Group these noncoordinate a-cells by their coordinate edge and unordered orthonormal ray-pair. A class on ell rows is on ell columns and has ell occurrences of each ray, as two matchings; the ell sum to k_a.

Distinct star classes have ALL cross overlaps nonzero. On different edges incident to a there is just the common coordinate a, giving a single nonzero term. On the same edge, two different orthonormal ray-pairs in C^2 have all cross overlaps nonzero.

For each other square s, its entries on the m_a pure-e_a cells are orthonormal and span K_{s,a} of dimension m_a. Every noncoordinate a-cell of Q_1 overlaps e_a, so its other-square vector lies in W_{s,a}=K_{s,a}-perp, of dimension k_a. Repeated rays force each star class to span at least ell dimensions; distinct classes give orthogonal spans. The lower bounds sum to k_a, forcing equality and making the two matchings ONBs of the SAME ell-space. MATCH gives ell>=6 for every star class.

Since k_a<=8, there can be at most ONE noncoordinate class incident to a. If Q_1 is nonclassical there is some class on{a,b}; neither coordinate can be used in any other noncoordinate class. Thus every cell is wholly in span(e_a,e_b) or wholly perpendicular to it. That two-space is globally isolated and contains both its reference coordinate pair and the noncoordinate pair, contradicting ISOLATE. QED.

Consequently EVERY nonclassical member has a weight3 entry in EVERY actual line frame: the physical five-support budget bounds all weights by3. This conclusion used no old K-count exclusions.

## 4. A uniform ray-multiplicity gap from weighted Parseval

Fix ANY unit ray v of Q_1 that occurs exactly m<8times, and put d=8-m. Its m occurrences lie in distinct rows and columns. Any other Q_1 vector with nonzero overlap with v must be in the residual d-by-d board of rows/columns missing those occurrences. Write

    g_x=|<v,Q_1(x)>|^2

there. Each residual row and column has g-sum1; sum_x g_x=d. Every positive g_x is STRICTLY below1, or there would be another v-ray occurrence. Hence every residual row has at least two positive entries.

For each s>=2, the m entries on v-occurrences are orthonormal and span K_s. At a residual cell with g_x>0, (T) puts Q_s(x) in W_s=K_s-perp, dim d. Taking the v,v matrix element of (P) gives

    sum_residual g_y P_{s,y}=P_(W_s).                      (1)

For fixed positive cell x with g_x=w, take the Q_s(x) diagonal element of(1):

    sum_y g_y |<Q_s(x),Q_s(y)>|^2=1.

The own-cell term is w. Row/column orthogonality removes two disjoint sets of other cells of total g-weight2(1-w). Summing over the FOUR other squares, their off-diagonal supports are disjoint by(T) and each squared overlap is<=1. Therefore

    4(1-w)<=d-w-2(1-w)=d-2+w,
    w>=(6-d)/5.                                           (2)

More generally the same proof for t squares gives w>=(t-d+1)/t.

If d<=3, every positive w is>=3/5, contrary to two positive entries summing1 in a residual row. Thus

    NO ray of any member has multiplicity5,6 or7.          (3)

Multiplicity8 is not excluded by this lemma. No vector-space or phase restriction entered its proof. If m=4, then d=4 and every positive residual overlap is>=2/5; in a three-space sector this forces exactly two positive overlaps in each row not containing v.

## 5. Uniform line cost at span11

Suppose now Q_1 is nonclassical with a_1=11, the only possible counterexample value after LS. In a chosen actual reference line frame, let D be the eight-dimensional real diagonal algebra and L the off-diagonal image of the full projector span S. Then

    D subset S,   dim_R L=3.                              (4)

For any other actual line with transition U, the span of the two ONBs' projectors has dimension16-c(U), where c(U) is the number of connected components of its bipartite support graph. The intersection of the diagonal algebras is exactly the real labels constant on graph components. Thus a connected unitary component of size r costs r-1 off-diagonal dimensions, and total line cost is8-c(U)<=3.

In every row AND column of any transition the number of nonzeros is<=3. This follows directly from(T): align the same actual reference cells, whose five nonempty supports are disjoint and avoid the one collinear reference cell, leaving seven; each support has size<=7-4=3. No template normalization is used.

For completeness, a connected unitary component of size at most4 under these degree bounds has the following shapes:

- size1: one edge;
- size2: full2-by2;
- size3: full3-by3 or exactly one zero;
- size4: all degrees3, hence4-by4with one zero per row/column.

To justify the last assertion rather than import T16: a degree1 line is isolated. If a row has degree2 on{x,y}, every row touching x must also touch y; their common neighbor set has size2or3. Size2 closes a2-by2component, since a new third neighbor would make a singleton column intersection. Size3 closes a3-by3one-zero component: the other two rows must use the SAME extra column to avoid singleton intersections. The transpose handles degree2columns. A connected size4component therefore has no degree1or2line, so all degrees are3 and its zeros are a perfect matching. For size3, two different zeros would either create a degree1line or a singleton row/column intersection, so only zero or one zero is possible.

The cost3 partitions are a single size4component; one size3plus one size2; or three size2components. In the latter two cases the full two-axis span already has dimension11, equals S and is block diagonal. A nontrivial size2block would then be globally isolated, with two different axis ray-pairs, contrary to ISOLATE. Thus those cost3types are excluded uniformly.

## 6. The entire size4 matching-complement branch is excluded

Suppose some line pair has one connected size4component. It exhausts all three off-diagonal dimensions, so every cell is either wholly in its four-space F or a singleton reference coordinate outside F. The local F-projector span is exactly the span of the two original F-ONBs E={e_i} and Q={q_i}, dimension7. Label the zero matching so<e_i,q_i>=0, with ALL other overlaps nonzero.

**Zero-pair span fact.** If P_v lies in the real span of projectors of two ONBs and e_i is orthogonal to q_j, then

    <v,e_i><q_j,v>=0.                                    (5)

Both Hermitian parts of e_i q_j* are orthogonal in trace inner product to EVERY projector of either ONB: on E only its i entry could survive and<q_j,e_i>=0; on Q only its j entry could survive and<q_j,e_i>=0. Orthogonality to P_v gives both real and imaginary parts of the displayed scalar zero. This proves(5) without a real-form assumption.

Here(5) says every nonzero E-coordinate x_i forces the corresponding Q-coordinate y_i to vanish. A vector with four nonzero E-coordinates would have all y_i=0. With three nonzero coordinates, it is parallel to the remaining q_i. With exactly two coordinates i,j nonzero, y_i has the one nonzero term<q_i,e_j>x_j, contradiction. With one coordinate it is an e_i ray. Therefore the local rank-one cone contains ONLY the eight E/Q rays.

A full F-ONB cannot mix the two bases. An e_i is orthogonal to only ONE Q-ray; it cannot coexist with two or more Q-rays. Likewise a q_j cannot coexist with three E-rays. Thus every actual row/column F-basis is either all E or all Q.

Let r actual rows use E and s use Q, r+s=8; both are positive from the two original axes. Each has equally many corresponding columns, and every ray's occurrence set is a matching on that class's rows/columns. For another square, let A_i be its r-dimensional span at the e_i occurrences, and B_j its s-dimensional span at q_j occurrences. For i!=j, (T) gives A_i perpendicular to B_j. Hence the span of any three B_j has dimension<=8-r=s. Each B_j already has dimension s, so those three coincide; varying i shows ALL four B_j coincide. Every A_i is their common orthogonal complement, of dimension r.

Thus any two E-ray matchings are ONBs of the SAME r-space in each other square, and similarly for Q. MATCH gives r>=6 and s>=6, contradicting r+s=8. This excludes the entire size4line-component branch, with arbitrary complex coefficients.

## 7. A two-channel physical lemma used only in the uniform reduction

We record the needed all-object version, not a B2-selected import. Let B be a coordinate two-space with reference coordinate pair E_B. Suppose every cell is B-pure, B-perp or mixed in one of

    F_1=span(b_1,c_1),   F_2=span(b_2,c_2),

where c_1,c_2 are orthogonal unit rays in B-perp, each b_j has BOTH coordinates nonzero in E_B, and both channels actually occur. Then the configuration is impossible at n8,t5.

Each line using a channel has exactly two vectors in it forming its ONB: its B/complement cross sum cannot cancel one nonzero contribution, and two orthogonal vectors exhaust F_j. The two c-directions separate the cross sums. Let k_j count its rows/columns.

If b_1,b_2 are parallel, put beta={b,b-perp}. Channel rows cannot overlap. Pure-B beta cells contain m_beta copies of b and m_beta+k_1+k_2 copies of b-perp; other pure pair classes have m_alpha occurrences of each ray. Their other-square spans are orthogonal, and the lower dimensions add to8. Saturation makes every pure alpha pair complete. Reference E_B is different from beta, so its class has m_E>=6. All mixed entries lie in the remaining k_1+k_2-space after removing the beta pure-b span. Distinct channel ray-pair classes have all cross overlaps nonzero: between channels only their common nonzero B component contributes; inside one channel use complex two-space geometry. Saturation and MATCH give k_1+k_2>=6. The mixed rows and reference-pair rows are disjoint, contradiction8>=6+6.

If b_1,b_2 are independent and nonorthogonal, their beta pairs are different and channel rows cannot overlap. Their pure-beta lower dimensions are m_beta_j+k_j; all other classes have lower m_alpha. Again they sum to8 and saturate. Each channel's other-square entries then lie in its k_j-space after removing pure b_j, and MATCH on its pair classes gives k_j>=6. Two disjoint channel row sets contradict8.

If b_1 is orthogonal to b_2, both have one beta pair. Let h count rows using both channels; m_beta and m_alpha count nonmixed pure pair rows. Then

    8=m_beta+sum_alpha m_alpha+k_1+k_2-h.

Reference E_B is different from beta since b_j have both coordinates nonzero; at least one alpha exists. In another square, alpha spans have dimensions>=m_alpha. Pure b_j occurs m_beta+k_(3-j)-h times, spanning that dimension and orthogonal to all alpha spans. Channel-j entries lie in their common orthogonal complement, of dimension<=k_j. Its pair classes force dimension>=k_j, so equality holds, EVERY alpha span has dimension m_alpha and its two matchings are complete. MATCH gives m_alpha>=6 and k_j>=6. Alpha rows are nonmixed and disjoint from channel-j rows, again contradiction8>=12.

This exhausts the B directions. Nothing required the other squares' projected parts to be orthogonal, or global real phases.

## 8. Two different size3coordinate supports cannot coexist

By L2, in a chosen reference line frame Q_1 has a weight3 cell. Its containing line has a size3component on some coordinate triple A, since size4 was excluded. Its off-diagonal projector span L_A has dimension2.

Suppose another actual line has a size3component on a DIFFERENT triple T, with span L_T also dimension2. Both lie in the three-space L. Their intersection is nonzero. Its matrix support lies only on edges inside A intersect T; hence |A intersect T|>=2. As the triples differ, they share exactly a pair B={a,b}. The intersection is a one-real-dimensional nonzero Hermitian direction on that edge: dimension2intersection would make both spans supported on one edge and could not support a connected size3component. Also L=L_A+L_T.

Write A=B union{c}, T=B union{d}. In each span, the cross map from B to its extra coordinate has real dimension1. Its actual mixed projectors therefore have a FIXED B factor ray u_c or u_d. A connected three-ONB cannot have all its vectors in the resulting two-space; it has one B-pure vector, which has both B-coordinates nonzero (a singleton would be an isolated component), and two mixed vectors. The fixed u is orthogonal to that B-pure vector and likewise has both coordinates nonzero.

All actual off-diagonal projectors lie in L_A+L_T. Their c,d entry is zero, so no rank-one cell can have both c and d nonzero. Outside A union T any nonzero coordinate must be a singleton. Every remaining cell is therefore B-pure, B-perp or mixed in span(u_c,e_c) or span(u_d,e_d). Both channels occur, their complement rays are orthogonal and their B factors have both coordinates nonzero. Section7 gives a contradiction.

Thus ALL size3components in actual transitions from this chosen reference line use the SAME triple A.

## 9. An outside coordinate edge is also impossible

If L is not supported entirely on A, some actual cell projector supplies an off-diagonal entry outside A. Its vector cannot have weight3, since that would give another size3support, and cannot have weight4 by the five-support bound. It is a weight2 vector on an edge E not contained in A. Since dim L_A=2 and dim L=3,

    L=L_A + the one-real-dimensional direction on E.       (6)

If E is disjoint from A, its coordinate two-space is globally isolated and nontrivial, contradicting ISOLATE.

Otherwise name A={a,b,c}, E={a,d}. Every cell is inside A, inside span(e_a,e_d), or a singleton outside. Any noncoordinate a,d cell belongs to an orthonormal pair on that two-space in its row/column. Let k be the number of such rows, and hence columns. Coordinate ray e_d occurs exactly8-k times elsewhere.

For every other square the entries at the e_d occurrences span an(8-k)-space; every noncoordinate a,d entry lies in its k-dimensional orthogonal complement. Its orthonormal-pair classes have row counts summing to k, repeated rays force those dimensions and different classes have all cross overlaps nonzero. Saturation plus MATCH yields k>=6.

There are now two exhaustive possibilities inside L_A:

- If L_A contains a nonzero off-diagonal direction on edge{b,c}, its cross image from span(e_b,e_c) to e_a has real dimension1. All A-vectors mixed across that split lie in one fixed channel span(u,e_a). The a,d vectors are wholly in the complement. The connected A-line supplies a noncoordinate pure{b,c}ray and the reference row supplies its coordinate pair, so a pure-B ray outside{u,u-perp} exists. ONE-CHANNEL contradicts8<12.
- If L_A has NO such{b,c}direction, every cell supported on{b,c} is a coordinate ray. In each a,d rotation row, the remaining A-vectors form an ONB of span(e_b,e_c), so both e_b and e_c occur there. Their multiplicities are therefore>=k>=6. Neither can have multiplicity8, since the actual connected A-transition uses that coordinate in at least two vectors on a line; a full ray would occur once in every line and exclude all other occurrences of its coordinate. The only remaining multiplicities6or7 are excluded by §4. Contradiction.

Thus no outside edge E exists. This argument uses the full residual-ray weighted inequality, not a numerical test or a template table.

## 10. The exact first unproved full case U3-6

Sections5–9 give L supported entirely inside A. Every rank-one full-cell projector is then either wholly in V_A or a singleton coordinate outside it. The five outside reference rays occur once in every actual row and column. There are exactly24 A-cells, three per line, each selected line giving an ONB of the COMPLEX three-space V_A.

The full span splits as the direct sum of those five fixed singleton projectors and the local A-projector span. Since a_1=11,

    dim_R span{P_{1,x}: x an A-cell}=11-5=6.              (7)

This is U3-6, the precise unproved case. Its quantifiers retain:

1. ALL five full8-by8physical arrays and every tensor-product pair equation, including pairs involving cells outside A;
2. arbitrary complex A-vectors, not assumed real or chosen from a finite palette;
3. arbitrary complex vectors/supports/phases in the other four squares;
4. any3-regular A-cell board on eight actual rows and columns consistent with the full Q_1 array, not one selected board;
5. the five outside fixed rays' full row/column arrangement, not a prescribed Latin square or classical member;
6. exact local real Hermitian projector span6, not just a PSD Gram relaxation or a claimed rank from sampled entries.

Conversely a genuine full family satisfying these conditions has a_1=5+6=11 and is nonclassical, so it really would refute uniform>=12. No existence is asserted. This identifies an EXACT full-physical failure case, not a toy control object.

## 11. Additional necessary constraints on U3-6, not its solution

All A-rays have multiplicity at most4. Multiplicities5/6/7 are excluded by §4. If an A-ray occurred8times, every other A-vector would lie in its orthogonal two-plane; together with the five singleton complement rays this makes that plane globally isolated. If it uses two different pairs ISOLATE excludes it; if only one, the local A-span is at most3, contrary to6. Thus multiplicity8 also fails inside A.

For each other square s, the24 product vectors Q_1(x) tensor Q_s(x) on A-cells are mutually orthogonal inside V_A tensor C^8 of dimension24, hence form a COMPLETE ONB. Partial trace gives

    sum_(A-cells) P_{s,x}=3I_8.                            (8)

For a fixed A-cell x, each other square has total squared overlap3 on those cells, own-cell contribution1 and off-diagonal contribution2. Across the four other squares the off-diagonal supports are disjoint and can only occur where Q_1(x) is orthogonal to Q_1(y). Therefore Q_1(x) must be orthogonal to at least8 A-cells.

If its ray has multiplicity4, §4 gives every positive residual squared overlap>=2/5. Each A-row not containing that ray has exactly two positive overlaps, since three would sum to more than1. It consequently has exactly twelve orthogonal A-cells: eight from the four rows containing the ray, plus four from the four missing rows.

These are genuine necessary constraints on the FULL physical case. They do NOT prove it impossible. No frame with these scalar properties has been promoted to a five-family witness, and no abstract operator violating missing physical constraints is presented as a counterexample.

## 12. Current obstruction, source trust and next exact input

**Uniform>=12 remains NOT PROVED.** The first missing mathematical input is:

> Exclude or construct a genuine U3-6 family with ALL conditions of §10, including the other four full complex squares and every tensor-product relation.

The bottleneck is complex rank-one/ONB interaction in the three-space, not an unrun support enumeration. The two-space proof works because distinct orthonormal ray-pairs have every cross overlap nonzero. Distinct three-dimensional ONBs can share zero overlaps in more complicated patterns; treating them as disjoint qubit channels would silently remove the case. A real six-dimensional operator space is also NOT automatically the real-symmetric matrices in some basis, so no global real reduction is asserted.

No T16/F14/classical-catalogue/native premise was used in this uniform reduction. Its mathematical inputs are the physical definitions, elementary complex linear algebra, and the previously checked LS/MATCH/ISOLATE/ONE-CHANNEL physical lemmas. All NEW star, multiplicity, size4cone, two-overlap and pendant deductions are author candidates requiring actual reconstruction.

Primary-source context remains distinct: Ball–Simoens gives QLS/MOQLS definitions and Problem16, not this span12 claim; *Magic Squares: Latin, Semiclassical and Quantum* gives the established rank-one-projector representation and semiclassical characterization, not an authenticated uniform span bound here. Zhang–Wang–Ji arXiv:2507.05642 concerns NUMBER OF RAYS, not dimension of their projector span. No equivalence between these invariants is assumed. The bounded screen is not novelty clearance.

## 13. Consequence if the remaining uniform case is closed

A complete exclusion of U3-6, after this reduction is validated, would establish every nonclassical member's a_s>=12. The checked surplus budget<=14 would then exclude K4 and K5 directly: four nonclassical members require16>14. OLD K12/K3 would still be explicit premises to conclude full five-square classicality, but ALL fifteen F14 native inputs and T16/template normalization would leave that new K4/K5 mathematical dependency set.

That would reduce inherited computational trust; it would NOT retroactively mark original A10 completed, change its three UNKNOWN Boolean facts, clear A11 without acceptance, repair runtime HOLD, manufacture unretained proof bytes, or establish formal/human/priority acceptance. Until U3-6 is excluded or an exact full physical counterexample is given, the original mixed route remains CONDITIONAL_WRITTEN_SUPPORTED and the new uniform obligation remains open.
