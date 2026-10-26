# Full-physical component-span mechanism: q3 reduces to an at-most4 complement — candidate v1

Actual returned `/bin/date` clock before this freeze: **2026-10-24T05:26:52-0700**. Owner PhysicsMOQLS8, physics-4. Same original primary and deadline2026-10-27T12:35:38-07:00. Exposure/scope: `q3-complement-scope-v1.json`; conceptual mechanism preceded that05:10:01 scope record and is NOT relabeled preregistration. This is **AUTHOR-WRITTEN COMPLETE PARTIAL CANDIDATE / NOT REVIEWED / NOT q3 OR FULL CLASSICALITY**. No scientific program, arithmetic interpreter, solver, enumeration, compilation, tests, CLI, new GO, old runtime or nested agent was used.

## 1. Literal result sought and what is actually claimed

The full primary remains Ball–Simoens Problem16 at n8. Here all FIVE arrays are actual ordinary MOQLS(8): unit vectors in C^8 at all64cells, actual row/column ONBs, and every pair's ALL64 same-cell products an ONB of C^8 tensor C^8. Every other mate remains a whole complex vector, never a projected frame. In the q3 branch exactly THREE members are nonclassical and TWO are classical. The latter give the actual four-net; no affine/catalogue/phase/real condition is imposed.

The parent-supported preceding partial result gave one nonclassical member with at least three global multiplicity8 rays, leaving a complement of dimension AT MOST5. This candidate proposes the stronger whole-branch reduction:

> In EVERY actual q3 family there is a nonclassical member with at least FOUR global multiplicity8 rays. Its nonclassical complement has dimension AT MOST4. More precisely, after taking ALL its multiplicity8 rays, the only remaining cases are f=4, r=4, local projector span b in{8,9,10}, or f=5, r=3, b in{7,8,9}.

Neither remaining case is excluded here. In particular there is **no arbitrary three-dimensional exclusion** imported from the old U3-6 theorem. q1/q2 also remain. A stronger low-dimensional span bound is not a physical counterexample or an all-object classicality theorem.

The new mechanism consists of:

1. an elementary span-versus-component inequality for collections of actual ONBs;
2. a weighted, full-tensor proof excluding one/two/three fixed channels around a coordinate two-space;
3. complete small-component equality-case exclusions, yielding local spans at least6,8,10 in nonclassical irreducible dimensions3,4,5;
4. a GLOBAL span-budget pigeonhole over the three actual nonclassical members.

Thus the endpoint is not a variant of the old isolated-three-space theorem: it is an all-member component/rank mechanism for the complete q3 family, and it leaves the arbitrary three-space residual explicit.

## 2. Definitions, supported physical inputs and exact matrix orientation

Write P_x=|q_x><q_x| for the selected member. At distinct actual cells x,y and distinct squares s,t,

`<Q_s(x),Q_s(y)><Q_t(x),Q_t(y)>=0`.                              (T)

For EVERY mate t, completeness also gives

`sum_x P_x tensor P_(t,x)=I8 tensor I8`.                         (P)

Taking the selected-factor expectation in ANY unit vector w yields

`sum_x |<w,q_x>|^2 P_(t,x)=I8`.                                 (E)

The expectation vector need not itself be an actual cell; the mate entries in(E) ARE actual full unit vectors. We never call projected entries an ONB.

Fix an ACTUAL row ONB E of the selected square. A transition matrix will be written with rows indexed by the TARGET actual basis vectors y and columns by E-coordinates i, entries `<e_i,q_y>`. Its row supports are therefore the actual target-vector supports. Both row AND column degrees are at most3, by the physical five-support argument applied independently in the two actual line frames. The same holds after restricting to any globally isolated coordinate component.

The complete complex sparse-unitary classification used below is the actual one in `proof-C4NET-heavy-support-v1.md` §4 plus its MANDATORY adjoint-orientation addendum: singleton, full2, full3, one-zero3, zero-matching4. It is now parent WRITTEN_SUPPORTED through `wave-v16-written-frontiers-parent-v1.md`. Its proof uses no catalogue and is closed under adjoint. We fix the row convention here explicitly rather than leave the earlier U orientation implicit.

Other supported physical inputs:

- **MATCH:** two disjoint actual ray matchings on the SAME m actual rows/columns, each an ONB of the SAME m-space in EACH of the other FOUR squares, require m>=6. Two distinct row/column zeros leave only m−2 slots for four nonempty disjoint coefficient lists.
- **ISOLATE2:** a globally isolated complex two-space cannot use two different orthonormal ray-pairs at n8,t5. Different pair classes have all cross overlaps nonzero; actual mate spans saturate their row counts; MATCH forces at least6rows per class.
- **Uniform/budget:** every nonclassical member has projector span a>=12, and `sum_(five s)(a_s−8)<=14`. Only the latter is needed for the new existence-of-f>=4 pigeonhole; uniform12 narrows the final displayed b ranges.

These are the literal already reconstructed physical interfaces. The new channel and equality-case arguments below require their OWN fresh reconstruction. No old K12/K3, native/Boolean refutation, Egan–Wanless1/39/2165 count, PartII real form, or all-span U3 exclusion is a premise.

## 3. Global projector components and a general span lower bound

In the E-frame join coordinates i,j if SOME actual cell vector has nonzero entries at both. Let its connected components have dimensions d_1,...,d_c. Every actual vector is wholly in one component, since its support is a clique of this graph. Thus every row/column contains an ONB of each component. The total real projector span is the direct sum of its local spans:

`a=sum_j b_j`.

A singleton coordinate component is exactly an actual ray of multiplicity8. One direction is immediate from the row ONBs. Conversely a multiplicity8 ray occurs once in every actual row; every other vector is orthogonal to it because its row contains that ray. It belongs to E and is an isolated E-coordinate. Hence the number f of singleton components is EXACTLY the complete global multiplicity8-ray count, not a selected subset of rays. Every nonsingleton component is irreducible and nonclassical.

### Lemma R: b>=2d−c for a family of ONBs

Let a finite family of ONBs of C^d include E, and let its real projector span have dimension b and coordinate-support graph have c components. Then

`b>=2d−c`.                                                     (R)

In particular a connected component of dimension d has local span at least2d−1.

*Proof.* Start with D, the d-dimensional diagonal algebra. Add the other ONBs one at a time. Suppose the previous coordinate graph has k components C, and let A be the space of ALL Hermitian matrices block diagonal on those C-blocks. The previous projector span is contained in A. For a new basis B=(b_i), let D_B be its d-dimensional real diagonal projector space.

Make a graph on B-indices, joining i,j if `<b_i,Pi_C b_j>!=0` for SOME previous coordinate block C. Here Pi_C is the actual orthogonal block projection. If this graph has g components, then

`dim_R(D_B intersect A)=g`:

in B-coordinates, a real diagonal matrix diag(lambda_i) commutes with every Pi_C exactly when lambda_i=lambda_j on every such edge. Thus the increase of the projector span is at least d−g.

For completeness, let W_1,...,W_g be the B-index component spaces. Each Pi_C preserves every W_j, since all its off-block B-matrix entries vanish. Therefore the nonzero intersections W_j intersect C form an orthogonal decomposition, with total dimensions d. In the bipartite incidence graph between the k old C-blocks and the g spaces W_j, the number e of edges is at most d (every edge has a positive intersection dimension).

Its connected components are exactly the k' new coordinate components after adding B. Indeed, before collapsing the connected B-index components, the incidence graph has an edge from b_i to C whenever Pi_C b_i!=0; this is exactly which old components a new projector connects. A B-index edge has a path through such a C, so collapsing it cannot merge previously different incidence components. Conversely W_j intersects C iff some b_i in W_j has a C-component. Thus the collapsed graph has the same k'. A graph with k+g vertices and k' components has at least k+g−k' edges. Consequently

`d−g >= k−k'`.

Each decrease in component count is therefore paid for by at least as much span growth. Initially b=d and k=d; summing until final c gives b−d>=d−c. QED.

A connected two-component is impossible physically by ISOLATE2, since its reference axes and a noncoordinate actual pair are different pairs. We next sharpen (R) by ONE dimension for dimensions3,4,5; we do NOT claim a span-independent exclusion of dimension3.

## 4. Local LIGHT and a weighted three-channel exclusion

### 4.1 Local LIGHT remains physical with arbitrary outside components

If all actual vectors in a globally isolated component have weight<=2 in an actual reference-row frame, that component is classical. The individual LIGHT star proof applies coordinate by coordinate INSIDE it: for coordinate a, all other-component vectors are perpendicular; each remaining actual row either has pure e_a or one full two-vector pair on an edge{a,b}. Different incident edge/pair classes have all cross selected-square overlaps nonzero. In EACH full mate their spans are orthogonal after the pure-e_a span is removed, and their row-count lower bounds sum to8−m_a. Saturation makes the two fixed-ray matchings bases of the SAME class space; MATCH makes every class use at least6rows. At most one edge class can touch a. A noncoordinate edge would therefore isolate a two-space containing both its reference pair and its different actual pair, contrary to ISOLATE2. Nothing requires vectors in other components to be light.

In particular every irreducible nonclassical component has a weight3 entry in every actual reference-row frame, and some actual row transition contains a3- or4-block.

### 4.2 Channel lemma (at most three channels, all complex)

Let B be a coordinate two-space with an ACTUAL reference-row coordinate pair beta0. Let c_j, j=1,...,m, m<=3, be mutually orthogonal coordinate rays in B-perp. Fix b_j in B with BOTH B-coordinates nonzero. Assume EVERY selected-square cell is B-pure, B-perp, or genuinely mixed in ONE fixed plane span(b_j,c_j), and at least one such mixed cell occurs. There is only ONE assigned B-ray b_j for each outside axis c_j. Then this full physical five-family is impossible.

*Proof — first saturation, without projected bases.* Give each B-active cell its unordered B-ray pair beta={b,b-perp}; for B-pure cells use their ray and its unique B-orthogonal ray. A mixed cell uses beta_j={b_j,b_j-perp}. Selected vectors belonging to DIFFERENT beta classes have nonzero inner product: their B-directions have nonzero cross overlap, and their outside parts cannot share an axis c_j, whose assigned beta is unique. Thus no cancellation from an outside coordinate is possible.

In every actual row, all B-active cells consequently have the SAME beta (they must be pairwise orthogonal). Their B-parts resolve I_B, so both directions occur and the class is well-defined. The same holds in every actual column. Let n_beta be the number of these rows, so sum_beta n_beta=8. For any mate t, the spans V_(t,beta) of its FULL vectors on different beta classes are mutually orthogonal by(T).

Choose one unit w in B nonorthogonal to every finitely many actual B-direction rays. In(E) all beta-cell weights are positive and B-perp weights are zero. The positive operators

`A_(t,beta)=sum_(cells in beta)|<w,q_x>|^2 P_(t,x)`

have mutually orthogonal supports V_(t,beta) and sum to I8. Each is therefore EXACTLY the identity projection on its V_(t,beta). Its trace is n_beta: each selected row of class beta contributes `<w,I_B w>=1`. Hence

`dim V_(t,beta)=n_beta`                                          (C1)

for EVERY full mate. Column trace gives the same column count. This is a derived identity on actual spans, not a guessed completeness of projected entries.

The actual reference pair beta0 differs from EVERY beta_j, because b_j has both coordinates nonzero. Its row class is nonempty and has NO channels. In that class its two pure B-rays each occur once in every class row/column. They give two repeated-ray matchings of size n_beta0, ONBs of the SAME V_(t,beta0) by(C1). MATCH gives

`n_beta0>=6`.                                                   (C2)

*Second saturation, channel by channel.* Choose any occurring channel j and put beta=beta_j. Restrict(E), with w=b_j, to V_(t,beta). Only the pure-b_j cells and the channels k whose b_k is parallel to b_j contribute. Their mate spans are mutually orthogonal, because selected vectors from distinct such categories have a common nonzero B-direction and different outside axes. The restricted sum is the identity on V_(t,beta).

Every row using channel k has exactly TWO vectors forming its ONB. Indeed the B-to-c_k cross entry of the row resolution cannot be canceled by any other category; one genuinely mixed vector is impossible, and two orthogonal vectors exhaust that two-plane. The same holds in columns. Subdivide channel j by its unordered orthonormal ray-pair in span(b_j,c_j). Different pair classes have ALL selected cross overlaps nonzero, so their full mate spans are orthogonal. A pair class on ell rows contributes trace ell in the b_j-expectation (the two B-weights sum1 in each such row). The same positive-operator saturation therefore gives an ell-dimensional actual mate space for the class. Its two repeated selected rays provide ell-cell matchings, ONBs of that SAME space in all FOUR mates. MATCH yields ell>=6. Thus

`n_beta>=ell>=6`.

Since beta!=beta0, (C2) contradicts sum_beta n_beta=8. This handles parallel, nonorthogonal and orthogonal b_j in ONE weighted argument, with no real normalization. QED.

All B-perp vectors were arbitrary full selected-square vectors; their outside components need not be coordinate rays. Every mate remained a full C^8 vector throughout.

## 5. Axis-plane facts needed for the equality cases

Let W_F be the real off-diagonal projector space of a connected basis block F in an E-frame. Its dimension is d−1, since the two diagonal algebras intersect only in scalar multiples of the identity on that support component.

### Three-block facts

For a connected3-block, W_F has dimension2. It contains a NONZERO operator supported on the single edge B=A minus{c} iff some F-vector has zero c-coordinate. To see this, write Y=sum lambda_j P_(f_j). Off(Y) supported on B iff Y e_c is proportional to e_c. In F-coordinates, all lambda_j with `<f_j,e_c>!=0` must equal. In a full3-block that means allthree are equal, so Off(Y)=0. In a one-zero3-block it leaves exactly one nonconstant degree of freedom. Its pure B-edge is Off(P_w), where w is the actual F-vector supported on B.

In the latter case W_F's B-to-c image is real one-dimensional. Its B-factor is the ray b in B orthogonal to w. Both w and b have BOTH B-coordinates nonzero (the3-block is connected). Consequently any rank-one cell projector whose off-diagonal part belongs to W_F is B-pure, B-perp or mixed in span(b,e_c).

Two different3-supports A,T have off-diagonal-plane intersection only on edges inside A intersect T. If their intersection is nonzero it is at most ONE real dimension on their common edge: two pure edge directions would span a plane supported on that edge, whereas a heavy3-projector has allthree edge entries nonzero. If both planes meet in that line, both blocks are one-zero blocks at their extra coordinate, with the fixed B-channel factors just described.

### Four zero-matching block facts

For a zero-matching4-block F, align `<e_i,f_i>=0` and all other overlaps nonzero. Its two-axis projector space S0 has dimension7. For any rank-one P_v in S0,

`<v,e_i><f_i,v>=0` for every i.                                 (Z)

Both Hermitian parts of e_i f_i* are trace-orthogonal to every E/F projector, proving BOTH real and imaginary conditions. If v has four E-coordinates, (Z) makes it orthogonal to all F; if it has three it is an F-ray; if it has two, the f_i at either supported index has a singleton nonzero overlap, impossible; if it has one it is an E-ray. Thus the rank-one cone of S0 consists ONLY of the eight E/F rays. In particular W_F contains NO nonzero pure edge direction: such a direction, together with D_E, would supply a two-support rank-one projector.

Also the part of W_F supported on any coordinate triple has dimension exactly1. For the omitted coordinate c, the condition Y e_c proportional e_c makes the three F-eigenvalues at its nonzero components equal, leaving one free eigenvalue; subtract the scalar identity. The remaining direction is Off(P_(f_c)).

Finally, if this4-support is split as3+1 or2+2 coordinate blocks, the subspace of W_F that is block diagonal for that split has dimension at most1. For3+1 this is the same preceding argument. For2+2, examine Pi_(first2) in F-coordinates. No F-vector is wholly in either side (each has three nonzero coordinates), so its nonzero-off-diagonal graph has no singleton component. On four vertices it has at most two components, giving at most two dimensions in D_F commuting with that projection; subtracting the scalar identity leaves at most1 off-diagonal dimension. These are statements over C, not just real coefficient identities.

## 6. A nonclassical irreducible3-component has b>=6

By(R), b>=5; suppose b=5, so local off-diagonal dimension is2. Local LIGHT supplies an actual3-block F; its W_F exhausts those dimensions.

If F has one zero, §5 puts every cell in one fixed B-channel or B/B-perp, with actual coordinate pair beta0 and noncoordinate channel ray b. Other global components are B-perp. The channel lemma with m=1 contradicts existence.

If F is full, its plane has no pure edge, so no actual local vector has weight2 in that frame. The SAME conclusion holds in EVERY actual row/column frame: if some such frame had a weight2 cell, local LIGHT would still supply a heavy3-block there; its plane again exhausts the two dimensions, and the weight2 projector supplies a pure edge. By §5 that block is one-zero and gives the already excluded channel configuration. Thus every actual local transition is either monomial or FULL3, never a2-block or one-zero3.

A row and column meeting in an actual component cell share that vector, so their local transition cannot be full; their unordered ray bases coincide. Group actual rows/columns by this local basis. Each class alpha uses the same number m_alpha of rows and columns, since each contributes3cells. It has m_alpha occurrences of each of its three rays. Distinct classes have FULL transitions and all selected cross overlaps nonzero, so in each mate their spans are orthogonal. Each span has dimension at least m_alpha by repetitions, and sum_alpha m_alpha=8; saturation makes each span exactly m_alpha. Two of its ray matchings are therefore ONBs of the SAME space in each mate. MATCH makes m_alpha>=6 for every class. An irreducible nonclassical component needs at least two classes, impossible in eight rows. Thus b>=6.

This excludes ONLY b=5, not arbitrary3-dimensional components of larger span.

## 7. A nonclassical irreducible4-component has b>=8

By(R), suppose the remaining equality case b=7, with local off-diagonal dimension3. Local LIGHT supplies a heavy actual basis component.

### A. Some actual basis has a zero-matching4-block

Its W_F exhausts all local off-diagonal dimensions. By §5 every actual component ray is an E- or F-axis; a full actual4-ONB cannot mix them, since an E-axis is orthogonal to only ONE F-axis. Let r rows use E and s use F, r+s=8 and both positive; the corresponding column counts agree.

For any mate, the spans V_i at E_i occurrences have dimension r, and W_j at F_j occurrences dimension s. For i!=j they are perpendicular by(T), so r+s=8 forces complementarity. Varying the three choices i!=j makes all V_i coincide, and all W_j coincide with their complement. Two E-ray matchings are actual ONBs of the SAME r-space; two F-ray matchings of the SAME s-space. MATCH gives r,s>=6, impossible. Other selected components are irrelevant and are not required classical.

### B. No4-block; a3-block occurs

Let its support be A, with plane W_A of dimension2. If another distinct3-support T occurs, they meet in a coordinate pair B. Their planes intersect in one real edge direction because they lie in a three-dimensional space. Section5 makes both blocks one-zero, and their sum is exactly the B-edge plus two real cross channels to the two remaining coordinate axes. There is no edge between those two outside axes. Every rank-one actual cell is therefore B-pure, B-perp or in one of the two fixed channels, whose B-factors are noncoordinate. The channel lemma excludes it.

If every3-support is A, irreducibility requires an actual two-support vector connecting an A-coordinate a to the remaining coordinate d. In the original F-basis that vector has degree `degree_F(a)+1`, so the two-sided bound3 requires degree_F(a)=2. Hence F is one-zero at a. Its plane plus the actual edge a,d exhaust the three off-diagonal dimensions. With B=A minus{a}, the B-to-complement part is only the ONE fixed F-channel to a; the edge a,d is B-perp. The channel lemma again excludes it. A full3-block, or an edge touching any of its degree3 coordinates, would instead give degree4 immediately.

All heavy basis possibilities are exhausted, proving b>=8.

## 8. A nonclassical irreducible5-component has b>=10

By(R), only b=9 remains to exclude. Its off-diagonal space L has dimension4. Every actual local transition has the S3 block types. We split according to whether any actual basis contains a4-block, a3+2 partition, or neither. This is an exhaustive split of actual basis types in dimension5.

### A. Some actual basis contains a4-block F on A, plus singleton e

Its W_F has dimension3. Any actual basis connecting e to A has an actual two-support,3-block, or4-block involving e.

- A two-support vector on{a,e} has degree `3+1=4` in the F+e basis, forbidden. This does not depend on other blocks in its own basis.
- A3-block involving e has a two-dimensional plane. Its intersection with W_F can only be a pure edge on its two A-coordinates, which W_F does not contain. Their sum would have dimension5.
- A4-block involving e meets A in three coordinates. Its plane and W_F can intersect only on that triple, at dimension at most1 by §5. Their sum would have dimension at least3+3−1=5.

Every possible connection is impossible. This contradicts irreducibility on five coordinates.

### B. No4-block; some actual basis F has3+2 supports A and D

Its off-diagonal plane is the direct sum of a two-dimensional W_A and a one-dimensional D-edge, hence dimension3. Any other basis must eventually connect A and D.

- A two-support crossing vector has degree at least2+2=4 in F, since every coordinate of the connected3-block has degree at least2 and every coordinate of the2-block degree2. Forbidden.
- A4-block crossing the partition has a three-dimensional plane whose block-diagonal part for the3+2 split has dimension at most1 (restrict its support as3+1or2+2 and use §5). Its intersection with the old three-plane is therefore at most1; the total is at least5.
- A3-block T crossing the partition must meet the old three-plane in at least one dimension, or their dimensions add to5. The intersection is the pure edge on the side containing TWO T-coordinates. By §5 the new block is one-zero at its single-coordinate side.

In the last case, if its two-coordinate side is D, the global four-plane is W_A plus the D-edge and ONE fixed D-to-A channel. The channel lemma with B=D applies, with arbitrary B-perp vectors on A.

If the two-coordinate side is a pair B inside A, the old W_A must itself contain that pure B-edge, so F's3-block is one-zero at A minus B. The full four-plane is: that B-edge, one fixed B-channel to A minus B, another to one coordinate of D, and the original edge inside D. The D-edge is B-perp; all B-active mixed vectors belong to one of the two fixed channels. The channel lemma applies again.

Thus no actual basis can connect A and D in any of the possible S3 ways. Irreducibility fails.

### C. Every heavy basis is one3-block plus two singleton axes

There is at least one3-support by local LIGHT. All remaining actual basis blocks are2-blocks/singletons.

#### C1. All3-supports are the same triple A

Let its basis plane be W_A. Any actual connecting vector is a two-support edge from an A-coordinate a to one of the two outside coordinates. In the original3-block+axes basis it has degree `degree_F(a)+1`; hence a must be the UNIQUE degree2 coordinate of a one-zero block. All such edges can touch A only at that a.

Connecting both outside coordinates to A requires at least TWO distinct outside-edge directions in L; their matrix supports make them independent modulo the operators supported on A. Therefore `dim(L intersect Off(A))<=2`, so it equals W_A. With B=A minus{a}, its B-to-a image is a single fixed noncoordinate channel, and no B-to-other-outside edge exists. Every actual B-active mixed vector belongs to that one channel; all outside-edge activity is B-perp. The channel lemma excludes it.

#### C2. Two distinct3-supports A,T occur

They cannot meet in only ONE coordinate. A heavy vector of the A-block then has two nonzero coordinates outside T, which are singleton axes in the T-basis, plus at least two coefficients from the shared coordinate's connected T-block expansion: degree at least4.

They thus share a pair B, with A=B+c and T=B+d. If their planes had zero intersection, they would already span four dimensions supported on those four coordinates, leaving no direction to connect the fifth coordinate e. Hence they meet in ONE real B-edge line. Both blocks are one-zero at their extra coordinates, and the old three-plane is the B-edge plus fixed channels b_c-to-c and b_d-to-d. Both B-factors are noncoordinate.

A third3-support inside these four coordinates but different from A,T would use the edge c,d, absent from the old three-plane. It would use up a fourth direction supported on the same four coordinates, again preventing any fifth-coordinate connection. So it cannot occur in an irreducible five-component with dim L=4.

A3-support involving e must meet BOTH A and T in at least two coordinates, by the preceding one-coordinate exclusion. It must therefore be exactly B+e. Its two-plane intersects the old three-plane in the same B-edge, or the sum exceeds4. Thus it supplies a THIRD fixed noncoordinate B-channel, and the total four-plane has no edge between distinct outside coordinates c,d,e. Every B-active mixed cell is in one of those three channels; the channel lemma excludes it.

The remaining way to connect e is a two-support edge{u,e}. If u lies in B, its expansion in the original A-block has degree3, giving degree4 with e. If u=c or d, the total four-plane is the old B-edge/two-channel plane plus this B-perp edge. There is still no B-to-e coherence, and no c,d edge; every B-active mixed vector remains in one of the two fixed channels. The channel lemma excludes it.

All possible fifth-coordinate connections and all actual basis types have been covered. Therefore b=9 is impossible, proving b>=10.

## 9. Global q3 consequence, with all original cases retained

For any nonclassical selected member let f be its number of singleton components/multiplicity8 rays. Dimension2 components are impossible. Every nontrivial component of dimension3,4or5 now has span at least TWICE its dimension. Every larger irreducible component has span at least2d−1 by(R); at most ONE such component can fit inside dimension8.

If f<=3 and no component has dimension>=6,

`a >= f+2(8−f)=16−f >=13`.

If one component has dimension>=6, necessarily f<=2, and

`a >= f+2(8−f)−1=15−f >=13`.

Thus the new complete partial mechanism gives

`NONCLASSICAL and f<=3  ==>  a>=13`.                            (G)

Now take a q3 family. The two classical members have projector spans8 each, so the14-budget says

`a_1+a_2+a_3<=38`.

If allthree had f_s<=3, (G) would require at least39. Hence at least one nonclassical member has f_s>=4. This proves the candidate AT-MOST4 reduction.

Take ALL fixed rays of that member. If f>=7 the remaining dimension is at most1, and its row ONBs supply only further fixed rays, making the square classical. If f=6 its remaining two-space would either use one fixed pair (again additional fixed rays) or violate ISOLATE2. Therefore a nonclassical member here has f=4or5. Uniform12 and the other two spans>=12 give12<=a<=14, so the remaining local span is EXACTLY within:

- **f=4, r=4, b=a−4 in{8,9,10};**
- **f=5, r=3, b=a−5 in{7,8,9}.**

These are UNEXCLUDED full-physical residuals. In particular §6 proved b>=6 for a nonclassical three-component, not its impossibility. The old U3-6 span6 proof is not borrowed to exclude b7/8/9. Every other quantum mate, both classical mates, every fixed matching and every one of the64 product-cell equations remain required in both cases.

## 10. Exact stop and verification boundary

This mechanism gives a materially stronger ALL-q3 reduction but **does not finish q3**. The equality cases excluded were the minimal component spans5/7/9, not every larger projector span. At r4,b8/9/10 a one-extra-direction or larger rank-one cone may contain additional actual bases; the zero-matching two-axis cone argument no longer says there are only E/F rays. At r3,b7/8/9 the two-dimensional off-diagonal/channel argument no longer exhausts the local span. Those are the precise next missing global mechanisms, not consequences of connectivity or a common support.

Before promotion, the NEW complete candidate needs actual hostile reconstruction of: (R)'s incidence/intersection accounting; the two-level weighted channel saturation and same-space MATCH invocations; all small-component equality cases, especially5.B/5.C2; and the full q3 span-count bridge. No old peer/parent verdict pre-certifies these new uses or conclusions.

q1/q2 remain scientifically open here and full classicality still retains oldK12/K3 trust. No catalogue/native payload, UNKNOWN, A10/A11 or runtime/provenance/retention/exit-attestation HOLD is repaired. All originals remain immutable; only this owned-root candidate is new. Same-harness written support of earlier sources is not human, formal/kernel, external-family or novelty acceptance. No execution or new GO is proposed.
