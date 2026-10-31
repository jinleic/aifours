# Self-contained author candidate: thirteen mixed cells in an ordinary four-MOQLS(8)

**AUTHOR-COMPOSED WRITTEN CANDIDATE — UNREVIEWED.** This packet explicitly composes the written arguments below; no source name, earlier bound, source catalogue, numerical solver, physical example, or previous parent message is a substitute for their proofs. All 23 load-bearing proof bodies are included in this one document. They have not received a complete independent mathematical review, and this packet is not a formal proof, human review, configured-family assessment, certificate replay, priority/novelty clearance, or parent adoption. The conclusion is conditional on the correctness of all the actual arguments below.

## Exact definitions and candidate assertion

An ordinary QLS of order 8 is an 8×8 array of unit vectors in its own complex Hilbert space C^8 whose eight vectors in every row and in every column form an orthonormal basis (ONB). A four-MOQLS(8) is a set Q,R,S,T of four such arrays such that, for every distinct pair M,N among them, the 64 vectors M_(ij)⊗N_(ij), over all board cells (i,j), form an ONB of C^8⊗C^8. No vector is assumed real, flat, a product across smaller subsystems, or drawn from a catalogue. Phases of individual entries do not affect the statements.

Q is classical if all its entry rays belong to one ONB. Fix **any actual board row**. Each of Q,R,S,T has an ONB there, so independent unitaries on the four Hilbert spaces and entry phases standardize the j-th entry of that row to its own local coordinate vector e_j; the column label j is shared, but the Hilbert spaces and their coordinate bases are not identified. Each unitary preserves the pair-product ONB conditions. A Q cell is light when its ray is one of Q's chosen-row coordinate rays and mixed otherwise. Q is nonclassical exactly when at least one mixed cell exists. Support means the set of nonzero coordinates of the actual Q vector in this fixed basis.

**Candidate U13.** In every ordinary four-MOQLS(8), for every member Q and every chosen actual row, nonclassical Q has at least **13** mixed cells. Consequently, for that common selected board row, the sum of mixed-cell incidences is at least 26, 39 or 52 when respectively 2, 3 or 4 members are nonclassical. Incidences for different members may overlap. U13 is only a necessary structural restriction; it does **not** establish a four-family witness, rule out q1/q2/q3/q4, establish full classicality, improve a numerical M(8) bound, or discharge A10/A11. Original GB15/18 and UNKNOWN exact-input states remain open.

## Actual-product and line convention

For every distinct pair M,N and distinct cells x,y, the physical ONB condition supplies

`<M_x,M_y> <N_x,N_y> = 0`.

A coordinate-support intersection of size one is used only when it actually implies a nonzero vector inner product; overlaps of size two or more are allowed to cancel and are never automatically declared nonzero. Row/column orthogonality is used separately. The proofs below distinguish these facts, collinearity, exact coordinate-subspace complements, and unitary transition matrices. No SAT support model is an input.

In any line with k mixed Q rays, the other 8−k light rays occupy distinct coordinate axes, so the mixed rays are an ONB of the complementary k-axis coordinate subspace. Consequently a mixed line has at least two mixed cells; degree 2 gives one common 2-axis support; degree 3 contains at most one support-2 ray; and comparisons of actual sums of their rank-one projectors give exact coordinate-projector identities. These facts are proved again in the relevant chapters.

Swapping the incidence roles of rows and columns in a case argument does **not** replace the original standardized Q row or identify local Hilbert spaces: the same support coordinates and pair-product ONBs remain fixed. Light-coordinate counting works along either kind of line; any explicitly chosen cell used for a comparison with the standardized row is distinct from that row, as established in its case. A light cell e_a is supplied by line completeness whenever no mixed ray on that line uses a.

## Complete case and internal dependency coverage

The table is a map of actual proofs included below, not an assertion of independent acceptance. The notation Pxx refers only to a chapter in **this file**. Historical SHA-256s in chapters identify original author artifacts; they are not hashes of the edited chapter headings in this combined document. Historical local scope notes such as “other cases remain open” refer to that chapter alone; later chapters supply exactly the additional cases listed here.

| Mixed cells and incidence shape | Complete internal proof chapters | Exact logical role |
|---|---|---|
| 1–7 | P01 | Elementary degree counts and actual one/two-mate contradictions |
| 8 | P01–P03 | All-degree-2 graph, other shapes, actual three-mate 3D argument |
| 9 | P04 plus P01–P03 | All shapes, full-support 3×3 board and five-dimensional saturation |
| 10 | P05 plus P02–P04 | All six incidence shapes and all 4×4 profiles |
| 11 | P06–P07 plus P01–P05 | QLS-only non-4×4 shape reduction and complete 4×4 exclusion |
| 12, either incidence side 6 | P08–P09 plus P02 | Exclusive-axis cycles, bridge, all degree profiles |
| 12, 3×4 | P10 | Actual projector balance and one-mate obstruction |
| 12, 3×5 | P11 | QLS-only all-degree-profile exclusion |
| 12, 4×5 | P08–P09 and P12 | Complete row/column degree profile coverage |
| 12, 5×5 | P08–P09 and P13–P15 | B/B boundary path proof and all other profiles |
| 12, 4×4 with A/A | P08–P09, P12, P16 | A=(4,4,2,2): support-2 or full-4 core |
| 12, 4×4 with A/B | P17 | B=(4,3,3,2): QLS-only |
| 12, 4×4 with A/C | P18–P20 | C=(3,3,3,3): low supports disjoint, equal, or one common axis |
| 12, 4×4 with B/B | P21 | QLS-only both low/low incidence cases |
| 12, 4×4 with B/C | P22 | QLS-only projector balance |
| 12, 4×4 with C/C | P23 | Full-support component and cube-edge cases |

For 12 mixed cells, every incident line has degree at least 2, so r,c≤6 and rc≥12; the table lists all possibilities up to incidence transpose. For 4×4, the only degree profiles on either side are A, B, C, and the six unordered pairings A/A, A/B, A/C, B/B, B/C, C/C are all listed. No other graph profile is assumed absent without one of the proofs.

## Explicit author-audit boundaries

The author traced the load-bearing row/column basis and actual pair-product hypotheses, including the difficult points: P02's component-wise light-coordinate dimension saturation; P05/P07's full-support core and same-cell product constraints; P08/P09's transition matrices and nonexclusive bridge; P10's rank-one projector balance; P16's two opposite-corner slots; P19–P20's norm-one cross-Gram step for actual 2-planes; and P23's full cube classification and common occupied axis. These are *author checks*, not independent validation. The complete bodies below, including all complex nonzero-coordinate and phase-sensitive steps, are the review scope. Auxiliary exact incidence/support observations mentioned historically are not proof premises; no numerical inference is promoted to an actual vector result.

The only editorial changes in the included proof bodies are shifting Markdown headings, mapping their load-bearing historical filenames to the corresponding Pxx chapters, and omitting three expressly non-proof historical witness/single-cycle comparisons. Existing files remain unchanged. If any line of any chapter is defective, U13 and every dependent claim remain unaccepted; the original four-family witness/global-classicality alternative and A10/A11 remain open.

## P01 — Any nonclassical member of three mutually orthogonal QLS has at least eight mixed cells

Original author-artifact SHA256 `7464f79b7bddaf7c4345544b2fad332d6c1b56698238df4cee215bc790d63a7f`; proof reproduced below.

**WRITTEN author candidate; no classical-mate, catalogue, numerical solver or finite-witness premise. Disjoint mathematical review pending.** For any ordinary set of at least three mutually orthogonal QLS of order n, choose any member Q, any actual Q row and its n rays as a coordinate ONB. If Q is nonclassical then at least **eight** of its n² cell rays are not coordinate rays of that row. The other QLS may be arbitrary complex and nonclassical. For n<4 the conclusion is understood conditionally and may be vacuous.

In particular, in an actual four-MOQLS(8), every nonclassical member has at least eight mixed cells even if **none** of the other members is classical. Thus a q4 family would have at least 32 mixed-cell incidences and at least 32 summed support-surplus units; q3 would have at least 24. These incidences may overlap, so this is a universal necessary lower budget, not an M(8), q3/q4 exclusion, A10/A11, novelty or formal-review claim.

### 1. Mixed rows, columns and the two-line lemma

Independently normalize the chosen first row of Q and of two other actual orthogonal members R,S to their own coordinate rays e_0,...,e_(n−1), with common column labels. A Q cell is *light* if its ray is one of Q's first-row basis rays and *mixed* otherwise. Nonclassicality is equivalent to at least one mixed cell because the chosen row already contains a complete basis.

Any row or column containing a mixed Q ray contains at least two mixed cells: on an occupied coordinate, the mixed ray's squared coefficient is strictly below 1, no light ray on that same line can use the coordinate, and ONB completeness forces another mixed ray there. If a line has exactly k mixed rays, its n−k light rays occupy distinct coordinate axes, so the mixed rays form an ONB of the complementary k-dimensional coordinate space. In particular, exactly two mixed rays have the **same two-coordinate support**; on a three-mixed line, at most one ray has support size 2. The latter follows because distinct 2-subsets of three coordinates meet in one axis and cannot be orthogonal, while two orthogonal rays on the same 2-support force the third ray to be the remaining singleton.

### 2. Four and five mixed cells are impossible with one mate

The bipartite graph with mixed rows and mixed columns as vertices and mixed cells as edges has minimum degree at least two. Therefore there are at least four mixed cells. With exactly four, the graph is a 2×2 rectangle. The two-line lemma propagates one common two-axis support `{a,b}` to all four mixed Q rays; their row/column orthogonality graph is K2,2 and its two parts carry two collinear Q rays in perpendicular directions.

The four R rays on that rectangle are pairwise orthogonal: opposite K2,2 parts share a row or column, while same-part Q rays overlap and the Q⊗R product ONB forces R orthogonality. The rectangle occupies two Q rows. Every other row contains only light Q rays and therefore contains e_a exactly once, giving **n−2** light e_a cells. Their R rays are mutually orthogonal because their Q rays are collinear; each is also orthogonal to all four rectangle R rays because every mixed Q ray has nonzero overlap with e_a. This would give `4+(n−2)=n+2` pairwise orthogonal R rays in C^n. So four mixed cells are impossible whenever Q has even one orthogonal QLS mate.

With exactly five mixed cells, minimum degree two gives at most two incident rows and at most two incident columns, but a 2×2 grid has at most four cells. So five is impossible for any QLS.

### 3. Six mixed cells are impossible with two mates

Suppose there are exactly six mixed cells. Minimum degree two permits either a 2×3 complete rectangle, a 3×2 complete rectangle, or three incident rows and three incident columns each of degree 2. In the 2×3 case, every mixed column contains exactly two mixed rays and therefore all six Q rays have support size 2. But each of the two three-mixed rows has at most one support-2 ray by §1, contradiction; the 3×2 case is symmetric.

In the remaining case the row/column graph is a single six-cycle. Every mixed row and column has exactly two mixed rays, so the two-line lemma propagates one common two-axis support `{a,b}` around the cycle. Its Q rays alternate between two perpendicular one-dimensional rays. Label the two bipartition parts `p_1,p_2,p_3` and `n_1,n_2,n_3` so the row/column graph is `K_(3,3)` minus the three pairs p_i,n_i.

For R, its three p-rays are pairwise orthogonal and its three n-rays are pairwise orthogonal, because the corresponding Q rays are collinear within each part. For i≠j the cells p_i,n_j share a row or column, so their R rays are also orthogonal. The six mixed cells occupy exactly three Q rows. In each of the other n−3 rows all Q cells are light, so there is exactly one Q=e_a cell. The corresponding n−3 R rays are pairwise orthogonal by Q⊗R, and each is orthogonal to every R ray on H because every mixed Q ray has a nonzero e_a coefficient. Thus all six R_H rays lie in a subspace of dimension at most 3. The two orthonormal triples therefore span the same three-dimensional space. Cross-orthogonality for i≠j makes each R_(n_i) collinear with R_(p_i).

The identical argument applies to S. At each nonedge p_i,n_i, both R rays are collinear and both S rays are collinear. Their R⊗S product vectors consequently have nonzero overlap, contradicting the actual R⊗S product ONB. Thus six mixed cells are impossible when Q has two other mutually orthogonal QLS mates.

### 4. Seven mixed cells are impossible even for one QLS

If exactly seven mixed cells existed, minimum degree two gives at most three incident rows and at most three incident columns. A 2×3 or 3×2 grid has at most six cells, so there are exactly three of each. The mixed-cell graph is a 3×3 grid with seven edges and minimum degree two, hence the two missing edges form a matching. Both row degrees and column degrees are `(3,2,2)`.

The degree-3 row contains two cells in degree-2 columns. The two-line lemma forces both those Q rays to have support size 2, but the three-line lemma permits at most one support-2 ray on a three-mixed ONB line. Contradiction.

The cases below eight are exhausted. This is an all-variable written argument using only the actual QLS and pair-product ONBs; it does not use the special explicit three-member witness, a source-classification theorem, a selected instance, or a solver. A disjoint reviewer must check the m=6 graph/three-dimensional span and R⊗S nonedge argument before adoption.


## P02 — A nonclassical four-MOQLS(8) member must have a mixed line of degree at least three

Original author-artifact SHA256 `5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8`; proof reproduced below.

**WRITTEN author candidate; no classical-mate, source catalogue, solver or finite-witness premise. Disjoint review pending.** In any actual ordinary four-MOQLS(8), a nonclassical member Q cannot have every mixed row and every mixed column containing exactly two mixed cells. Equivalently, relative to any actual chosen Q first-row basis, some row or column containing mixed Q rays must contain **at least three** of them. All other three QLS may be arbitrary complex and nonclassical.

This excludes the entire degree-two mixed-incidence branch, including any number of disjoint row/column cycles, including the single-cycle case. It is a necessary structural obstruction, not complete four-family classicality, an M(8) upper bound, A10/A11 closure, novelty or an independently reviewed theorem.

### 1. Cycle components and an exclusive-axis lemma

Normalize Q and its three actual orthogonal mates independently on the chosen first row to coordinate rays e_j with common column labels. A Q cell is *mixed* if it is not one of its first-row rays. Any mixed row or column has at least two mixed cells: on an occupied coordinate of a non-singleton ray, no same-line singleton can contribute, and ONB completeness forces another mixed ray there. If all mixed line degrees equal two, the finite simple bipartite graph whose vertices are mixed rows and columns and whose edges are mixed cells is a disjoint union of cycles C_(2k_i), each k_i≥2.

On a row/column with exactly two mixed Q rays, the other six light rays are distinct first-row axes; the mixed pair is an ONB of the remaining two-axis coordinate space. Thus each connected cycle component C_i has one common two-axis support T_i={a_i,b_i}, and its Q rays alternate between two perpendicular one-dimensional rays, k_i of each. Since the selected first row is not mixed, if `K=Σ_i k_i` is the number of mixed rows then `K≤7`. There are at most three components because every k_i≥2.

**Exclusive-axis lemma.** Suppose one axis a in a component C of size 2k occurs in no mixed Q ray outside C. Every row outside C contains a light Q=e_a ray: if the row has a different cycle's mixed pair, both of those rays avoid a and all its remaining entries are light, so ONB completeness includes e_a; otherwise the whole row is light. There are exactly n−k such rows. For any other mate R their R rays are mutually orthogonal and orthogonal to all R_C rays by the actual Q⊗R product ONB. The two k-cell ray parts of C each give k mutually orthogonal R rays, so R_C spans exactly k dimensions and the two parts are ONBs of that common space.

Their k×k transition matrix has two zeros in every row, at the actual row/column neighbors on C. Transition supports for different mates are pairwise disjoint by their original pair-product ONBs; for t total family members this gives `t≤k−1`. Also every Q_C ray uses b, so all R_C are orthogonal to first-row R=e_b. The n−k light-e_a R rays form an ONB of the complement of the k-space and include first-row e_a. Since e_b lies in that complement and is orthogonal to e_a, each mate has nonzero e_b overlap at some one of the other n−k−1 light-e_a cells. Pair-product orthogonality between two mates forbids the same cell for both. Hence `t≤n−k`. Thus an exclusive-axis cycle satisfies `t≤min(k−1,n−k)≤floor((n−1)/2)`. In order 8 it cannot occur in a four-family.

From now on suppose no support axis is exclusive to one component.

### 2. One common two-axis support for all components

First consider the case that all component supports equal the same pair `{a,b}`. Group cycle components by their projective Q two-ray basis: two components are in the same group when their two orthogonal ray pairs agree up to phases and interchange. In dimension two, two distinct orthonormal ray bases have no zero cross-overlap; hence Q rays from different groups have nonzero overlaps, and the corresponding R subspaces are pairwise orthogonal for every other mate R.

If group g contains K_g mixed rows, its K_g rays of either local Q direction are collinear in Q and therefore give K_g orthogonal R rays. Its R span has dimension at least K_g. Across groups the spans are orthogonal. The n−K light Q=e_a rays in rows without mixed cells give n−K further orthogonal R rays, orthogonal to every mixed R ray. Since `Σ_g K_g=K`, dimension n forces each group span to have **exactly** dimension K_g. Its two Q-ray parts therefore give two ONBs of that group span.

If there are at least two distinct basis groups, each group's transition matrices for the three other mates have pairwise disjoint supports and at least two row/column zeros per row, so the argument above forces `K_g≥5` for every group. Two groups would give K≥10, contradicting K≤7. If there is only one basis group, both Q ray parts over **all** components are collinear globally. The same two transition and first-row-axis pigeonholes as in the exclusive-axis lemma apply to their common K-dimensional R span, giving `t≤min(K−1,n−K)≤3` at n=8. Thus a common support pair is impossible in a four-family.

### 3. The only remaining support graph is a triangle

With exactly two components, if their 2-sets differ, one component has an axis absent from the other, contrary to the exclusive-axis lemma. If they agree, §2 applies. So two components are impossible; one component is already covered by the exclusive-axis lemma.

With three components and no exclusive axis, consider the three two-element support sets as edges of a multigraph on coordinate axes. If two distinct sets occur and one is repeated, the singleton distinct set has an exclusive axis. If all three distinct sets occur and no axis has degree one, they must form a triangle `{a,b}`, `{a,c}`, `{b,c}`. The remaining possibility—all three supports equal—was excluded in §2.

For the triangle case, take any component C_i and another C_j sharing axis a. Their other support axes differ, so every Q ray on C_i has **exactly one** common support coordinate with every Q ray on C_j; all such overlaps are nonzero. Actual Q⊗R orthogonality therefore makes their R spans mutually orthogonal for every other mate R. The third component does not use a. If C_i,C_j occupy k_i,k_j mixed rows, there are n−k_i−k_j light Q=e_a rays in all remaining rows, including rows of the third component. Their R rays are mutually orthogonal and orthogonal to both spans. Each component has at least k_i or k_j mutually orthogonal R rays from either of its Q-ray parts. Dimension n forces both spans to have exactly those respective dimensions.

The two k_i-ray parts of C_i are therefore ONBs of one k_i-space for every mate R. Their transition matrices have the two row/column zero positions per row and pairwise disjoint supports across mates, so `t≤k_i−1`. But with three components `k_i≥2` and `Σ k_i≤7`, hence every k_i≤3. A four-family is impossible. The same reasoning holds for each component by choosing either shared axis.

All one-, two- and three-component possibilities are exhausted, so the mixed-incidence graph of a nonclassical four-family member in order 8 must have a row or column of mixed degree at least three. No assertion is made for such higher-degree graphs, for non-product generalized QOA entries, or for A10/A11.

A disjoint review should reconstruct the exclusive-axis count including rows occupied by other cycles, the same-support basis grouping/dimension equality, the support-multigraph trichotomy and the triangle case's actual Q⊗R orthogonality before adoption.


## P03 — Every nonclassical member of a four-MOQLS(8) has at least nine mixed cells

Original author-artifact SHA256 `73e9df96b79f897ef360d26982cda35b5929a85cc674fd82a3f0ad16fa447559`; proof reproduced below.

**WRITTEN author candidate; no classical-mate, catalogue, numerical solver or finite-witness premise. Disjoint full mathematical review is essential.** In any actual ordinary four-MOQLS(8), choose any member Q and any actual Q row as its coordinate ONB. If Q is nonclassical, at least **nine** of its 64 cells are not rays of that row. The other three QLS may all be arbitrary complex and nonclassical.

This is a universal structural bound, not a proof that every four-family is classical, an M(8) bound, an A10/A11 qualification or a novelty claim. It imports two separately review-pending WRITTEN candidates: the universal ≥8 bound `P01` (SHA256 7464f79b7bddaf7c4345544b2fad332d6c1b56698238df4cee215bc790d63a7f), and the no-degree-two-incidence-graph result `P02` (SHA256 5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8). This packet excludes every possible **eight-mixed-cell** graph not already excluded by the latter.

### 1. Basic line facts and exhaustive graph shapes

Independently normalize Q and its three actual orthogonal mates R,S,T on the chosen first row to their own coordinate bases e_j with common column labels. A Q cell is *mixed* if it is not a first-row basis ray. Every row or column meeting the mixed set H contains at least two mixed points: on any coordinate occupied by a mixed ray no same-line singleton can occur, and ONB completeness requires another mixed ray on that coordinate.

On a line with exactly k mixed rays, the n−k light singleton rays occupy distinct coordinate axes, so its mixed rays form an ONB of the complementary k-dimensional coordinate space. In particular, two mixed rays have the same two-axis support, and on a three-mixed line at most one ray has support size 2. Indeed, distinct 2-subsets of three axes intersect once and cannot be orthogonal; two orthogonal rays with the same 2-support force the third to be the remaining singleton.

Suppose `|H|=8`. If r rows and c columns meet H, minimum degree two gives r,c≤4, while rc≥8. Up to exchanging “row” and “column” in the argument, the only possibilities are

`(r,c)=(2,4), (3,4), (3,3), (4,4)`.

For `(4,4)`, every incident row and column has degree exactly 2, excluded by the named no-degree-two theorem. All remaining cases are handled below without assuming any classical mate.

### 2. The (2,4) and (3,4) shapes contain an isolated two-axis rectangle

In either case all four incident columns have exactly two mixed cells. Every mixed ray therefore has support size 2. A row with exactly three mixed rays would contain three support-2 rays, contradicting the line fact above. Thus `(2,4)` has two degree-4 rows, and `(3,4)` has row degrees `(4,2,2)`.

On the degree-4 row, its four mixed rays form an ONB of a four-coordinate subspace and each has support size 2. Distinct 2-supports cannot meet in exactly one coordinate, and no two-dimensional support can contain more than two orthogonal rays. Hence the four supports are exactly **two disjoint two-sets**, each used twice. The two mixed cells in every incident column have equal supports. In the `(2,4)` case this gives two 2×2 mixed rectangles, one for each disjoint support. In the `(3,4)` case each degree-2 row has one common 2-support and occupies the two columns in that same support group, so the mixed cells again split into two 2×2 rectangles, possibly sharing the degree-4 row. The two rectangles have disjoint coordinate supports.

Choose one rectangle H_0 with two-axis support `{a,b}`. Its four Q rays alternate between two collinear ray pairs; opposite parts share a row/column. For any actual orthogonal mate R, same-part R rays are orthogonal by Q⊗R and opposite-part R rays are orthogonal by R's row/column ONB. Thus the four R rays on H_0 are pairwise orthogonal.

No mixed Q ray outside H_0 uses axis a, because the other rectangle's support is disjoint. H_0 occupies two rows. In each of the other six rows, all mixed Q rays avoid a and the remaining Q rays are light, so the row ONB contains exactly one light Q=e_a ray. Their six R rays are mutually orthogonal and each is orthogonal to all four R rays on H_0 by Q⊗R. Ten nonzero orthogonal rays cannot fit in C^8. The cases obtained by exchanging row and column use the identical argument along columns, **without changing the chosen first-row coordinate basis**.

### 3. The (3,3) shape forces three incompatible partial 3×3 QLS

With three incident rows and columns and eight edges, the mixed graph is K3,3 with one missing cell. Relabel these rows and columns so the missing mixed cell is (2,2). Two rows and two columns contain three mixed cells; the remaining row and column contain two. The four cells in the upper-left 2×2 lie on both a three-mixed row and a three-mixed column. In each such row or column, the cell in the degree-2 column/row has support size 2, so the other two mixed rays must have support size 3. The four 2×2 corner rays therefore all have support size 3; their three-coordinate row/column subspaces coincide along intersections. Call the common three-axis set T.

The two rays in the degree-2 row have one common two-axis support U⊂T; the two rays in the degree-2 column have one common two-axis support V⊂T. They cannot be equal. If U=V, each upper-left Q ray has a nonzero projection to this two-space and must be orthogonal both to its row's degree-2-column ray and its column's degree-2-row ray. Those two rays would have to be collinear. For either fixed upper-left row, this would force the two orthogonal rays in the degree-2 row to be collinear, contradiction. Thus U and V are different 2-subsets of T and intersect in one axis a. Every one of the eight mixed Q rays has nonzero coordinate a.

The three mixed rows leave five rows containing only light Q rays. Each has a unique Q=e_a cell. For any mate R, those five R rays are mutually orthogonal and orthogonal to all eight R_H rays by the actual Q⊗R product ONB. Hence `dim span(R_H)≤3`. Any full three-mixed row supplies three orthogonal R rays, so their common span V_R has dimension exactly 3. The same is true independently for S and T.

The eight R_H rays occupy a 3×3 grid missing (2,2); its first two rows and first two columns are ONBs of V_R, and its final row/column each contain two orthogonal rays. Comparing the sum of their eight rank-one projectors by rows and by columns gives

`P_(2,0)+P_(2,1) = P_(0,2)+P_(1,2)`.

Both sides are rank-two orthogonal projections. Their one-dimensional complements in V_R are therefore the same ray. Adding that ray at the missing cell completes the eight **actual** R_H rays to a 3×3 QLS on V_R. Do the same independently for S and T; no claim is made that these auxiliary missing rays equal the original family rays at (2,2).

Every order-3 QLS is classical. For completeness, normalize its first row to e_0,e_1,e_2. Its next row has the form `(0,a,b),(c,0,d),(e,f,0)` in those coordinates. If all three rays had support 2, each pair would have exactly one common nonzero coordinate and could not be orthogonal; hence one is a singleton. That singleton, the column zeros and row orthogonality force the other two second-row rays to be the remaining singletons, and each last-row ray is then forced by its column. Thus all rays are from the same ONB.

Independently label the first row of each completed R,S,T 3×3 QLS as symbols 0,1,2. A Latin square of order 3 with that first row has only **two** possibilities: the other two rows are the two cyclic derangements, in either order. Among three mates, two have the same symbol pattern. In the eight actual cells each symbol occurs at least twice, so for two distinct actual cells both mates have collinear rays in both factors. Their original pair-product vectors then have nonzero overlap, contradicting the actual R⊗S (or corresponding) product ONB. The auxiliary ninth cell is not used in this contradiction.

All eight-cell graph shapes are impossible in an actual four-family. Together with the named universal ≥8 bound this proves the candidate **≥9**. For q4 the summed support-surplus is at least 36, with overlaps between members allowed; for q3 it is at least 27, while stronger results may hold when a classical mate is present. These lower budgets alone do not exceed the total 168-unit upper budget and are not a global q3/q4 exclusion.

A disjoint reviewer should reconstruct the degree enumeration, the isolated-rectangle occurrence count, the common-axis 3×3 span bound, the projector-sum completion and the order-3/pair-product pigeonhole independently, and should review both named written imports before adoption.


## P04 — Nine mixed cells are impossible for any nonclassical four-family member

Original author-artifact SHA256 `eb1ec0ad36ab6c467c4b3931ca81bc9176decaf6a60a67f789bbca20b8a7b9e1`; proof reproduced below.

**WRITTEN author candidate; no classical-mate, catalogue, solver or finite-witness premise. Disjoint full mathematical review pending.** In an actual ordinary four-MOQLS(8), every nonclassical member Q has at least **ten** mixed cells relative to any chosen actual Q row. The other three members R,S,T may all be arbitrary complex and nonclassical. This is a universal necessary support bound, not a full four-family classicality, M(8), A10/A11 or novelty claim.

The separately review-pending universal ≥9 result `P03`, SHA256 73e9df96b79f897ef360d26982cda35b5929a85cc674fd82a3f0ad16fa447559, is a named WRITTEN input. This packet excludes exactly nine mixed cells.

### 1. Nine mixed cells force a 3×3 mixed board

Choose an actual row and independently standardize Q,R,S,T there to their own e_j bases with common column labels. A *mixed* Q cell is not a first-row basis ray. Every mixed row or column contains at least two mixed cells. On a line with exactly k mixed cells, its 8−k distinct light singleton rays occupy 8−k axes; the mixed rays form an ONB of the complementary k-coordinate space. Hence a two-mixed line has two rays with the same two-axis support, and a three-mixed line has at most one support-2 ray: two different 2-subsets of three coordinates meet once and cannot be orthogonal; two orthogonal rays on the same two axes force the third to be the remaining singleton.

Suppose there are nine mixed cells. If r rows and c columns meet them, minimum degree two gives r,c≤4. A 2×4 grid has at most eight cells, so, up to exchanging row/column in the counting argument, the only possible pairs are `(3,3),(3,4),(4,4)`.

In a `(3,4)` graph, the four column degrees are `(3,2,2,2)`, and the row degrees are either `(3,3,3)` or `(4,3,2)`. Any degree-3 row intersects at least two degree-2 columns. Its corresponding Q rays both have support size 2 by the two-line fact, contradicting the three-line fact. In a `(4,4)` graph, row and column degrees are each `(3,2,2,2)`; the degree-3 row again meets at least two degree-2 columns and gives the same contradiction. Therefore `(r,c)=(3,3)` and all nine cells of that board are mixed.

### 2. The actual Q mixed board is a classical order-3 QLS in three axes

Each mixed row and column has exactly three mixed rays, at most one of support 2. Consider the bipartite graph of the three mixed rows and three mixed columns retaining just cells whose Q support has size 3. It is K3,3 with at most one edge deleted at each vertex, hence it is connected. A support-3 cell equals the full three-coordinate mixed subspace of its row and of its column, so connectedness identifies **one common coordinate triple T** for all six line subspaces. Every one of the nine actual Q_H rays lies in span(T), and each mixed row/column is an ONB there. The 3×3 Q_H board is therefore an actual order-3 QLS.

Every order-3 QLS is classical. To see this directly, normalize its first row to e_0,e_1,e_2. Its second row has coordinate form `(0,a,b),(c,0,d),(e,f,0)`. If all three rays had support 2, a pair would overlap in exactly one nonzero coordinate and could not be orthogonal. A singleton in the second row, together with column zeros and row orthogonality, forces the other two to be the remaining singleton rays; the third row is then forced columnwise. Thus all nine rays belong to one ONB.

At most one of these three Q basis rays has support size 2 in T: every board row contains all three basis rays, and a three-mixed line permits at most one support-2 ray. At least two Q basis rays therefore have **full support T**. Denote their three occurrences each by p_1,p_2,p_3 and m_1,m_2,m_3. They form the two symbol classes of a classical 3×3 Latin square. Within each class every Q ray is collinear; between classes their row/column mixed-cell graph is a six-cycle `K_(3,3)` minus a perfect matching. Label it so that p_i,m_i are the three nonadjacent pairs.

### 3. Three pair-product mates saturate a five-dimensional span

For any actual mate R, the R rays on the p-class are an orthonormal triple because the Q rays there coincide; the R rays on the m-class are another orthonormal triple. For i≠j, p_i,m_j share a row or column and their R rays are orthogonal. Every one of the six selected Q rays uses all three first-row axes in T, so comparing Q⊗R products with the three corresponding first-row products puts all six R rays in the five-dimensional complement of those axes.

The only cross-part R overlaps not already zero are the three numbers `α_i^R=⟨R_(p_i),R_(m_i)⟩`. They cannot all vanish, for that would give six orthogonal vectors in five dimensions. The same statement holds for S and T. At each nonedge p_i,m_i, actual R⊗S, R⊗T and S⊗T product orthogonality makes the nonzero-index sets of their three α-vectors pairwise disjoint. Each is nonempty and there are only three indices, so each set contains exactly one index and the sets partition `{1,2,3}`.

For any one mate, its six selected rays are all pairwise orthogonal except possibly one matched pair. Taking one ray from that pair and all four other rays gives five orthonormal vectors in the five-dimensional complement of T. They are an ONB there; the omitted matched ray is orthogonal to the other four and hence collinear with the selected one. Thus the six selected R rays **span all of** the five-dimensional complement of T. The same is true for S and T.

There are five Q rows with no mixed cells, one being the standardized first row. Choose any first-row axis a∈T and an off-first-row cell y in one of the other four rows with Q_y=e_a. Q_y overlaps every one of the six selected Q rays, so Q⊗R orthogonality forces R_y orthogonal to their full five-dimensional span; hence `R_y∈span(T)`. Likewise `S_y,T_y∈span(T)`.

Comparing Q⊗R, Q⊗S and Q⊗T products at y with their first-row products at column a forces R_y,S_y,T_y all orthogonal to e_a. Thus each is nonzero and supported on only the other **two** axes of T. For any pair among R,S,T, product orthogonality against each first-row product forces their supports at this off-row cell disjoint. Three nonzero pairwise-disjoint supports cannot fit in two axes. Contradiction.

All nine-cell cases are impossible. The named ≥9 input therefore yields **≥10 mixed cells per nonclassical member** of any four-MOQLS(8), including q4. This gives at least 40 total mixed-cell incidences/support-surplus units in q4, or 30 in q3; the incidences may overlap, and the lower budget alone is not a global exclusion.

A disjoint review should reconstruct the incidence count, connected support-3 graph, exact order-3 QLS classification, six-ray five-dimensional saturation, and final same-cell support pigeonhole, as well as both named written inputs. No source priority or stronger acceptance is inferred.


## P05 — Ten mixed cells are impossible for a four-family member

Original author-artifact SHA256 `9299801cf3f66a081fb828d0e4ea4568a56edd73d581c6fd833de226c2a93a02`; proof reproduced below.

**WRITTEN author candidate, 2026-10-28 20:45 PDT.** In any actual ordinary four-MOQLS(8), choose any member Q and any actual Q row. If Q is nonclassical, then at least **eleven** Q cells are mixed relative to the basis of that row. All three other members R,S,T are arbitrary complex QLS; no classical mate, finite catalogue, equal-modulus or reality hypothesis is used. The named prior WRITTEN inputs are the arbitrary-member lower bound ≥10, `P04`, SHA256 eb1ec0ad36ab6c467c4b3931ca81bc9176decaf6a60a67f789bbca20b8a7b9e1, and the no-all-degree-2 mixed-incidence theorem for a four-family, `P02`, SHA256 5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8. Both and this new argument need disjoint full review. The conclusion is a necessary condition, not a four-family exclusion, M(8) bound, A10/A11 closure, formal verification, or priority claim.

### Basic facts and an exclusive-rectangle obstruction

Independently standardize the chosen actual row of Q,R,S,T to their respective coordinate bases with common column labels. A mixed Q cell is not one of the first-row coordinate rays; its *support* is its set of nonzero Q coordinates. In a line with k mixed Q cells, its light cells occupy 8−k distinct axes, so the k mixed rays form an ONB of the complementary k-axis subspace. Thus each mixed line has degree at least two; a degree-2 line has two Q rays on the same support-2 set; and a degree-3 line has at most one support-2 ray. Indeed two distinct 2-subsets of a 3-set meet once and cannot support orthogonal rays; two orthogonal rays on the same 2-set fill that plane and force the third ray to be a singleton.

Two support-2 rays on one line have either the same support or disjoint supports, since a single nonzero shared coordinate cannot cancel. A line all of whose mixed rays have support 2 consequently has even mixed degree: each support plane is orthogonally filled by exactly two such rays. In a 4-mixed line with at least three support-2 rays, the fourth also has support 2 and the four supports are U,U,V,V for disjoint 2-sets U,V: two of the first three must share a 2-set, fill it, and the fourth lies in the orthogonal complement of the third ray within the remaining 2-set.

**Exclusive-rectangle lemma.** Suppose four mixed Q cells form a 2×2 rectangle, all have the same support {a,b}, and no other mixed Q cell uses a. Then no orthogonal QLS mate R exists. The four R rays at the rectangle are pairwise orthogonal: two cells in a common row/column give orthogonal R rays; opposite corners have collinear Q rays because the 2×2 Q grid is made of two orthonormal bases of the same plane and the column constraints identify opposite rays, so product orthogonality gives orthogonal R rays there too. In each of the six rows outside the rectangle, Q=e_a occurs as a light ray: no mixed ray uses a, and the row is an ONB. The corresponding six R rays are pairwise orthogonal by Q⊗R orthogonality, and each is orthogonal to all four rectangle R rays because each rectangle Q ray overlaps e_a. This gives ten orthogonal nonzero rays in C^8, contradiction. The lemma requires no restriction on any light Q cells other than row completeness.

### 1. Ten-cell incidence profiles

Let r,c be the number of rows and columns containing mixed Q cells. Minimum degree two gives r,c≤5, and rc≥10. Up to exchanging the incidence roles of rows and columns, the only pairs are

`(2,5), (3,4), (3,5), (4,4), (4,5), (5,5)`.

When c=5 every mixed column has degree 2, so every mixed Q ray has support 2. The even-line fact excludes (2,5), because both mixed rows would have degree 5. It also leaves only row degree profiles `(4,4,2)` for (3,5), and `(4,2,2,2)` for (4,5). The (5,5) case has all mixed row and column degrees 2 and is excluded by the named no-degree-2 theorem.

For (3,4), column degrees are `(3,3,2,2)` and row degrees are `(4,4,2)` or `(4,3,3)`. For (4,4), both degree profiles are either `(4,2,2,2)` or `(3,3,2,2)`; if the profiles differ, a degree-3 line meets at least two degree-2 lines and is impossible by the degree-3 fact. The remaining cases are treated without an incidence catalogue below.

For an auxiliary finite check, an in-kernel enumeration of all 10-subsets of the labelled r×c incidence boards confirmed exactly these profiles before the support restrictions: 1, 54, 210, 2040, 2580 and 2040 labelled graphs respectively for the six displayed `(r,c)` pairs. This enumeration checked only incidence profiles, not amplitudes, existence or the mathematical conclusion. The arguments below are independent of it.

### 2. Five incident columns: two disjoint support planes and a rectangle

For (3,5), regard each degree-2 column as an edge joining its two mixed rows. The row degrees `(4,4,2)` force three edges between the two degree-4 rows and one from each of them to the degree-2 row. That degree-2 row has one support U on both its cells, which propagates through their columns. In a degree-4 row the four support-2 rays are U,U,V,V for a 2-set V disjoint from U. Thus exactly one of the three edges between the degree-4 rows has support U, and the other two have support V. Those two V columns form a 2×2 rectangle on the degree-4 rows, and all other mixed Q rays use U, disjoint from V. Apply the exclusive-rectangle lemma with either coordinate of V.

For (4,5), the row multigraph has degrees `(4,2,2,2)` and five edges. Four meet the degree-4 row, leaving one edge between two of the three degree-2 rows. The remaining degree-2 row is joined to the degree-4 row by two columns. Its common support U occurs twice in the degree-4 row; the remaining two mixed rays there use a disjoint support V. The two degree-2 rows incident with the remaining edge consequently use V throughout. The two U columns form an exclusive 2×2 rectangle, so the lemma applies.

### 3. The 3×4 profiles are impossible already for Q

The two degree-3 columns meet all three mixed rows. Each degree-2 column meets the degree-4 row(s), and its two Q rays have the same support-2 set.

*Profile `(4,4,2)`.* The degree-2 row meets both degree-3 columns. Its support-2 ray in each such column forces the other two rays there to have full support 3. In either degree-4 row, the two cells in the degree-2 columns have supports U,V of size 2. If U=V, these two rays fill that plane and the remaining two rays of the 4-mixed row lie in its complementary 2-space, contradicting their support 3. If U≠V, orthogonality makes U,V disjoint and their union is the entire 4-axis mixed subspace. Each support-3 ray meets one of U,V in exactly one coordinate, so it cannot be orthogonal to the corresponding support-2 ray. Contradiction.

*Profile `(4,3,3)`.* Each degree-2 column meets the degree-4 row and one degree-3 row. The two latter incidences must be on different degree-3 rows, since each degree-3 row has at most one support-2 ray. Its other two rays, both in degree-3 columns, have full support 3. Because each degree-3 column contains both degree-3 rows, all four of these full supports coincide with a single 3-set W, and W contains the support-2 sets U,V of the two degree-2 columns.

If U=V, the two support-U rays in the degree-4 row fill their plane. Its other two rays must then both use the complementary 2-set V' disjoint from U. Both lie in degree-3 columns whose mixed subspace is W, so W contains U∪V', impossible. If U≠V, they are disjoint. The degree-4 row's mixed subspace is U∪V. A ray there orthogonal to the two support-2 rays cannot meet either U or V in exactly one coordinate; in a degree-3 column its support has size at most 3, so it has support exactly U or V. Its two remaining rays must use U and V once each. Again W contains U∪V, impossible. No 3×4 profile exists.

### 4. The `(4,2,2,2)`–`(4,2,2,2)` 4×4 profile

The degree-4 row and degree-4 column meet every incident line; after removing them, the remaining degree-2 rows and columns are joined by a perfect matching. The degree-4 row has three support-2 rays on the degree-2 columns, so its central ray also has support 2, and its four rays use two disjoint supports U,U,V,V. Support equality propagates along each degree-2 column, its matched degree-2 row and that row's intersection with the degree-4 column. Choose U as the central support. Exactly one of the three matched branches has support U; together with the central cell it makes a 2×2 U rectangle. The other two branches use V, disjoint from U. Hence the rectangle is exclusive, contradicting the lemma.

### 5. The `(3,3,2,2)`–`(3,3,2,2)` 4×4 profile

Call the degree-3 rows and columns *high*. A high row has at most one cell in a degree-2 column, so it meets both high columns and exactly one low column; similarly every high column meets both high rows and one low row. The high/high core is therefore a 2×2 board. Its four Q rays have full support 3; their shared row and column subspaces identify a common 3-set W.

The six other mixed cells all have support 2. Form a graph whose vertices are these six cells, joining two when they share a degree-2 row or column. It has four degree-1 vertices (the high/low and low/high cells), two degree-2 vertices (the low/low cells), and four edges. It consists either of two 3-vertex paths or of a 2-vertex and a 4-vertex path. Along either path all Q supports agree, and every path has an endpoint on a high line; its support is therefore a 2-subset of W. Let the two path supports be U,V. As an independent finite incidence check, with fixed high rows/columns and the necessary at-most-one-low-neighbor restriction, all 16 labelled graphs have the asserted core and boundary graph: eight have component sizes (2,4), eight (3,3). This check does not establish any vector identities.

#### 5a. Distinct path supports

If U≠V, they share exactly one axis a in W. Q rays from different paths have nonzero inner product, because their only shared nonzero coordinate is a. For each path, select R rays as follows: on a 3-path select all three; on a 2-path select both; on a 4-path select three consecutive vertices. Within any such selection the R rays are pairwise orthogonal: adjacent cells share a row or column, while two vertices two steps apart have collinear Q rays in the common support plane and are orthogonal in Q⊗R. Cross-path selections are mutually orthogonal in R because their Q rays overlap. Thus there are at least five pairwise-orthogonal selected R rays, all at Q rays overlapping e_a.

Only four Q rows contain mixed cells, so the other four rows each contain a light Q=e_a cell. Their four R rays are pairwise orthogonal and orthogonal to every selected R ray by Q⊗R. This gives at least nine orthogonal R rays in C^8, a contradiction. This case already needs only one mate.

#### 5b. The same path support

Suppose U=V. Denote the four boundary endpoints on high lines by p_i (one for each high row) and q_j (one for each high column). Each high/high Q ray has full support W and is orthogonal to p_i and q_j. Its nonzero projection on U is perpendicular to both; in the 2-plane U this forces p_i and q_j collinear. All four high/high incidences exist, so all four endpoints are the same ray p. A 2-vertex boundary path would have orthogonal endpoints, contradiction. Thus there are two 3-paths, and each middle Q ray is the common ray v in U perpendicular to p.

Let z be the third coordinate of W. The four core Q rays lie in the 2-space span{v,e_z}; their 2×2 row/column orthogonality forces opposite corners collinear, with the two diagonal ray classes mutually orthogonal. Every core ray has nonzero overlap with v because it has full support W. The four core R rays are pairwise orthogonal: shared-row/column pairs are orthogonal in R, and opposite pairs have collinear Q rays. The two middle R rays are orthogonal because their Q rays coincide at v. Every core R ray is orthogonal to each middle R ray because the corresponding Q rays overlap. These six R rays are therefore an ONB of the six-dimensional complement of the two axes in U: comparing their Q⊗R products with the two first-row products puts each R ray in that complement. The same statement holds for S.

Choose an axis a∈U and an off-first-row cell y with Q_y=e_a in any row containing no mixed cells; such rows exist because exactly four rows are mixed and the chosen first row is unmixed. Q_y overlaps all four core and both middle Q rays, so Q⊗R and Q⊗S orthogonality force R_y,S_y into span(U). Comparison with the first-row products at a makes both perpendicular to e_a, hence both are collinear with the other coordinate ray e_b. Their R⊗S product at y then has nonzero inner product with the first-row R⊗S product at b, contradiction. This step uses actual products of two distinct mates; it does not assert a three-family or QLS-only obstruction for all of case 5.

### 6. Scope and exact residual

All ten-cell incidence profiles are excluded, so the named ≥10 input yields **≥11 mixed cells per nonclassical member**. Consequently the per-member lower sum is at least 22 for q2, 33 for q3, and 44 for q4, relative to a fixed selected board row; mixed-cell incidences may overlap between members. No comparison with an unrestricted global upper budget has been established, and no q2/q3/q4 exclusion follows from this bound alone. The three named old A10 exact inputs, GB15/18 and remaining UNKNOWNs are unchanged; A10/A11 remain OPEN.

A full review should reconstruct both named inputs; the exclusive rectangle and all incidence cases; the 3×4 same-versus-distinct plane alternatives; both 4×4 boundary path types; exact dimension and product arguments; and scope. No parent, independent-family, executable-proof, formal, human, or novelty gate is claimed here.


## P06 — An eleven-mixed-cell order-8 QLS is confined to a 4×4 incidence board

Original author-artifact SHA256 `95dc3b835ed5a23fc9376e91b3a5897599650aa7d2d20ccfbbd3b56a88ac2f41`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** For any actual complex QLS Q of order 8 and any chosen Q row, if exactly 11 cells are non-coordinate rays relative to that row, then exactly four rows and four columns contain those cells. No orthogonal mate, classicality, source classification or numerical experiment is assumed. This is a QLS-only shape restriction, not an exclusion of 11 cells or a four-family conclusion. Together with the separately review-pending four-family ≥11 candidate `P05` SHA256 9299801cf3f66a081fb828d0e4ea4568a56edd73d581c6fd833de226c2a93a02, it identifies the next boundary case but does not establish ≥12.

Standardize the chosen Q row to e_0,…,e_7 and call all other Q rays not collinear to these axes *mixed*. A line with k mixed cells has complementary k-axis mixed subspace; degree 2 forces both mixed Q rays to have the same support 2, and a degree-3 line has at most one support-2 ray. A degree-4 line containing three support-2 mixed rays has a fourth support-2 ray as well, since orthogonality forces two disjoint support pairs each repeated twice. Mixed row/column degrees are at least 2.

With exactly 11 mixed cells, r,c≤5 and rc≥11. Up to exchanging rows/columns in the incidence argument, the only possible pairs are `(3,4),(3,5),(4,4),(4,5),(5,5)`.

### (3,5), (4,5) and (5,5)

For c=5 the column degrees are `(3,2,2,2,2)`. Any degree-3 row would meet at least two degree-2 columns, giving two support-2 Q rays and contradicting the degree-3 fact. For r=5 the row degrees are `(3,2,2,2,2)`, so this is impossible. For r=4 the only degree profile without a 3 is `(5,2,2,2)`. The degree-3 column meets at least two degree-2 rows and hence contains two support-2 rays, again impossible.

For r=3 the degree profiles are `(5,4,2),(5,3,3),(4,4,3)`, so the only remaining profile is `(5,4,2)`. The degree-3 column meets all three rows. The degree-4 row's other three rays are in degree-2 columns, hence have support 2, so its ray in the degree-3 column has support 2 as well. The degree-2 row's ray in that column also has support 2, contradicting the degree-3 fact.

### (3,4)

The row degrees are `(4,4,3)` and the column degrees `(3,3,3,2)`. Each degree-3 column meets all three mixed rows; the degree-2 column meets both degree-4 rows. The degree-3 row meets the three degree-3 columns and has at least two full-support-3 rays. Choose two of those rays, q_1,q_2, in distinct columns. Their support is the same 3-set W because they lie in one degree-3 row. Each chosen degree-3 column's mixed subspace is W, since it contains a full-support-W ray.

Fix either degree-4 row. Let x_1,x_2 be its rays in those columns, and let u be its ray in the degree-2 column, with support U of size 2. The two x_j lie in W, are mixed and mutually orthogonal; each is also orthogonal to u. Column orthogonality gives x_j⊥q_j. Let K be the 4-axis mixed subspace of this degree-4 row, which contains U and the supports of x_1,x_2.

* If U⊂W, then u,x_1,x_2 are an orthonormal basis of span(W). The fourth mixed ray of the degree-4 row lies in the 1-axis complement of W inside K, a singleton, contradiction.
* If |U∩W|=1, the single-overlap rule forces each x_j to avoid the common coordinate a. Thus x_1,x_2 form an orthonormal basis of the 2-axis subspace B=W\{a}.
* If U∩W is empty, both x_j are supported in K\U, which has only two axes. Since they are mixed, both have that same 2-axis support B⊂W, and again they form a basis of B. Let a be the unique axis in W\B.

In the latter two cases, q_1|_B is perpendicular to x_1 and hence collinear with x_2, while q_2|_B is perpendicular to x_2 and collinear with x_1. Their B-projections are orthogonal. Both q_1,q_2 have full support W, so their inner product is the single nonzero a-coordinate contribution, contradicting the orthogonality of the degree-3 row. The 3×4 incidence case is impossible.

Therefore only `(r,c)=(4,4)` remains. The original row/column names may be exchanged in the argument; the coordinate basis is always the originally chosen actual Q row. This excludes no 4×4 eleven-cell board by itself. The remaining 4×4 profiles are `(4,3,2,2)` or `(3,3,3,2)` on each side, subject to the at-most-one-support-2 condition on each degree-3 line. Full amplitudes, all mates, and all such profiles remain to be analyzed.


## P07 — Eleven mixed cells are impossible for a nonclassical four-family member

Original author-artifact SHA256 `70a596b860f8d72d7a002538291109069f50110022a8a40bb1891622f3662b34`; proof reproduced below.

**WRITTEN author candidate; full disjoint review pending.** For any ordinary four-MOQLS(8), any member Q, and any chosen actual Q row, if Q is nonclassical then Q has at least **12** mixed cells relative to that row. The other three members R,S,T are unrestricted complex QLS; no classical member, finite catalogue, phase/equal-modulus assumption, source classification or computational certificate is used. This is a universal necessary condition, not a full classicality, M(8), A10/A11 or novelty claim.

Named WRITTEN imports, both still awaiting full review: the ≥11 four-family bound `P05` SHA256 9299801cf3f66a081fb828d0e4ea4568a56edd73d581c6fd833de226c2a93a02, and the QLS-only 11-cell 4×4 shape reduction `P06` SHA256 95dc3b835ed5a23fc9376e91b3a5897599650aa7d2d20ccfbbd3b56a88ac2f41. The latter also establishes the basic line facts used below. The present argument excludes the entire remaining 4×4 board.

### Line facts

Independently standardize the chosen row of Q,R,S,T to their own coordinate bases at common column labels. On a line with k mixed Q rays, they form an ONB in a k-axis coordinate subspace. Degree-2 lines have two rays on one support-2 set. A degree-3 line has at most one support-2 ray; any other mixed ray on that line has full support 3. On a line, two support-2 rays have identical or disjoint support, since an overlap in exactly one nonzero coordinate cannot cancel.

A 4-mixed line cannot contain two support-2 rays and one support-3 ray: if the two 2-supports coincide, they fill their 2-plane and the 3-support ray must fit in the two remaining coordinates; if they are distinct, they are disjoint and fill all four coordinate axes, so a 3-set intersects one of them in exactly one axis, precluding orthogonality. This observation applies to actual rays with arbitrary complex amplitudes.

The 4×4 degree profile on each side is either A=`(4,3,2,2)` or B=`(3,3,3,2)`.

### A/A and A/B are impossible already for Q

For A/A, the degree-4 row meets both degree-2 columns and hence contains two support-2 rays. The degree-3 column meets the degree-4 row and at least one degree-2 row, whose ray has support 2; its ray in the degree-4 row therefore has support 3. This is impossible by the 4-line fact. The argument also covers the row/column transpose.

For A/B, let h be the degree-4 row, g the degree-3 row, and let the other two rows have degree 2. The single degree-2 column meets h. It must also meet a degree-2 row: otherwise it meets g, leaving all four incidences of the two degree-2 rows in the three degree-3 columns, and one such column would meet both degree-2 rows, yielding two support-2 rays on a degree-3 line. Thus g meets all three degree-3 columns. Each of them meets h, g and exactly one degree-2 row, so its low-row ray has support 2 and its ray on g has full support 3. The three g rays have one common 3-axis support W, and each degree-3 column has mixed subspace W. The three h rays in those columns are an ONB of span(W). The fourth h ray must therefore be the lone coordinate ray in the complement of W within its 4-axis mixed subspace, contradicting its being mixed. B/A is the transpose of the same incidence reasoning, with the original chosen Q-row basis unchanged.

### B/B: one common 3-axis subspace

There are three high degree-3 rows and columns and one low degree-2 row and column. In the high/high cells retain only those whose Q support has size 3, viewed as edges between high rows and high columns. Each high line with a low-line cell has one support-2 ray there and hence two support-3 core rays. Each high line without a low-line cell has three core rays, at most one with support 2, hence at least two support-3 core rays. The resulting bipartite graph on three high rows and three high columns has minimum degree two and is connected: each component would require at least two vertices of each color, so two components cannot fit in six vertices. A full-support-3 Q ray identifies the 3-axis mixed subspaces of its row and column. Therefore all six high-line subspaces equal one common 3-set W.

We distinguish whether the intersection of the low row and low column is mixed. All low-line rays have support 2 and these supports are 2-subsets of W by their high-line endpoints.

### Low/low cell absent

Write the high rows A,B,C, high columns X,Y,Z and the low row/column L. After relabeling, the low column meets A,B, the low row meets X,Y, and the two missing high/high cells are A,X and B,Y. Thus A,Y and B,X are mixed, and so are all three cells in row C and column Z. Let p,p^⊥ be the two Q rays in the low column, on support U, and q,q^⊥ the two Q rays in the low row, on support V. Here U,V⊂W and |U|=|V|=2. The core ray at A,Y has full support W: row A already has its support-2 low-column ray, and column Y already has its support-2 low-row ray.

If U≠V, their unique common coordinate a gives nonzero Q overlap between every low-column ray and every low-row ray. If U=V but the two orthonormal bases are genuinely distinct, all four cross overlaps are nonzero as well: for two bases of a complex 2-space, one zero entry forces them to coincide as rays up to permutation. In either situation the four corresponding R rays are pairwise orthogonal: pairs in the same low line are orthogonal as QLS entries, and cross pairs by Q⊗R orthogonality. The R ray at A,Y is orthogonal to the two low-line rays sharing its row or column. It is also orthogonal to the other ray on each low line, because its full-support-W Q ray is perpendicular to the first ray of each support-2 basis and hence has nonzero overlap with the other. Thus these five R rays are pairwise orthogonal. Every one of their Q rays overlaps e_a: choose a∈U∩V in the distinct-support case, or any a∈U in the same-support case. The four rows containing no mixed Q cells each contain a Q=e_a cell. Their four R rays are mutually orthogonal and orthogonal to the five above, by Q⊗R. Nine nonzero orthogonal rays in C^8 are impossible.

The remaining possibility is U=V and the two low-line bases coincide. Since the full-support-W Q ray at A,Y is perpendicular to the low-column ray at A and the low-row ray at Y, these two support-U rays must be collinear; otherwise they span U and the core ray would be the singleton on W\U. Similarly the low-column ray at B equals the low-row ray at X. Call these rays p and p^⊥ respectively, and let z be the third coordinate in W.

Let u=Q_(A,Z) and v=Q_(B,Z). Row A and column Y are ONBs of W containing the same two rays p,Q_(A,Y), so Q_(C,Y) is collinear with u. Similarly Q_(C,X) is collinear with v. Both u and v have full support W: they lie on high rows already containing a support-2 low-column ray. Orthogonality to the low-column rays gives u∈span{p^⊥,e_z} and v∈span{p,e_z}. Their only possible overlap is the z-coordinate, which is nonzero for both; hence ⟨u,v⟩≠0. But u,v lie in the same column Z and must be orthogonal. Contradiction, even without a mate.

### Low/low cell present

Let the low/low Q ray be v on support U. Its two low-line neighbors are orthogonal to v in that same 2-plane and hence collinear; call their ray p. Relabel the high row and column meeting them A and X, and denote the other high rows B,C and columns Y,Z. The sole missing high/high cell is A,X. Every displayed core cell on A or X has full support W. Write

`Q_(A,Y)=q, Q_(A,Z)=q', Q_(B,X)=r, Q_(C,X)=r'`.

Each pair q,q' and r,r' is an orthonormal basis of the 2-space W∩p^⊥. If r is collinear with neither q nor q', the two mixed rays Q_(B,Y) and Q_(B,Z), each perpendicular to r and to q or q' respectively, are both collinear with p, impossible in one row. Hence r equals q or q' as a ray. Swapping Y,Z if necessary, r=q and r'=q'. Orthogonality then forces `Q_(B,Z)=Q_(C,Y)=p`, `Q_(B,Y)=q'`, and `Q_(C,Z)=q`. Thus q appears at A,Y; B,X; C,Z, and q' at A,Z; B,Y; C,X. Both q and q' have full support W. These six cells are two 3-cell symbol classes whose row/column adjacency is a six-cycle.

For any mate M∈{R,S,T}, the three M rays in the q class are pairwise orthogonal by Q⊗M, as are the three in the q' class. Across the classes all pairs are orthogonal in M except possibly the three non-adjacent matched pairs. Because q,q' use all three first-row axes in W, all six M rays lie in the 5-dimensional coordinate complement of W. Therefore at least one of the three exceptional inner products is nonzero for each M; otherwise six rays would be orthogonal in dimension five. For each matched pair, M⊗N orthogonality for distinct mates makes their nonzero exceptional-index sets disjoint. Three nonempty pairwise-disjoint subsets of three indices are singletons. For each mate the six rays are orthogonal except possibly one pair; the other four and one representative form an ONB of the five-dimensional complement, forcing the omitted ray collinear with the representative. Hence all six R rays span that complement, and likewise all six S and all six T rays.

There are four Q rows containing no mixed cells, including the standardized row. Choose a different such row and its cell y with Q_y=e_a for any a∈W. Q_y overlaps q and q', so the saturation just proved forces R_y,S_y,T_y∈span(W). Comparing Q⊗R, Q⊗S and Q⊗T with the first-row product at a forces all three vectors to avoid e_a. Finally, comparing each mate-pair product at y with every first-row mate-pair product says their supports are pairwise disjoint. Three nonzero pairwise-disjoint supports cannot fit into the two axes W\{a}. Contradiction.

### Boundary

The entire 11-cell 4×4 board is excluded. Together with the named ≥11 and shape inputs this proves the **candidate** universal ≥12 lower bound. Its summed necessary mixed incidences are ≥24, ≥36, ≥48 for q2, q3, q4 respectively; incidences of different members need not be disjoint. No global upper bound on that sum, global four-family obstruction, M(8) numerical upgrade, or A10/A11 closure is claimed. The original exact-input GB15/18 and UNKNOWNs are unchanged. This proof and all imported candidate arguments require full disjoint mathematical review; no parent, formal, human, executable-certificate, configured-family or novelty acceptance is inferred.


## P08 — Exclusive-coordinate support cycles inside arbitrary QLS families

Original author-artifact SHA256 `0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** Let a family contain t≥2 pairwise-orthogonal ordinary complex QLS of order n, and standardize an actual row of one member Q to its coordinate basis. Suppose Q has 2k mixed cells on a simple row/column incidence cycle, k≥2, every one with the same 2-axis support U={a,b}, and **no other mixed Q cell uses axis a**. Other mixed Q cells and other incidence components are otherwise arbitrary. Then

`t ≤ k−1`.

In particular an exclusive-axis support-2 C4 rules out any orthogonal mate, C6 rules out three or more family members, and C8 rules out four or more.

At each incident cycle row and column its two Q rays have the same support U and are orthogonal. Going around the cycle alternates the same two orthogonal rays p,p^⊥, each appearing k times. The selected standardizing row contains no mixed cells and hence is outside the k cycle rows. For every cycle-exterior row, no mixed Q ray uses a; row completeness therefore supplies a light Q=e_a cell. There are n−k such cells, including one in the standardizing row.

Fix any mate M. Its rays at the n−k light e_a cells are pairwise orthogonal, and each is orthogonal to every M ray in the cycle, by Q⊗M orthogonality because all cycle Q rays use a. Thus the cycle M rays span dimension at most k. The k M rays over p are pairwise orthogonal by Q⊗M, and the same is true of the k rays over p^⊥. They are therefore two orthonormal bases of one k-dimensional space. Their k×k transition matrix is unitary. In each transition row the two entries for the opposite-class cells sharing its actual QLS row and column are zero, so at most k−2 positions can be nonzero.

For two distinct mates M,N, M⊗N orthogonality at any cycle pair from opposite Q classes makes the product of their corresponding transition entries zero. Their transition supports are therefore disjoint. Each unitary transition matrix has at least one nonzero entry in each row, so at most k−2 mates are possible: t−1≤k−2. No row/column outside the cycle is assumed classical, and no transition matrix is assumed monomial or real.

### A concrete 12-cell stratum

For Q of order 8 with exactly 12 mixed cells on 3 mixed rows and 6 mixed columns, all six columns have degree 2. Every mixed ray has support 2; a row's support-2 rays use disjoint support planes, each repeated exactly twice, so each mixed row has even degree. The row profiles are `(6,4,2)` or `(4,4,4)`. Regard each column as an edge joining its two mixed rows, allowing parallel edges.

* For `(6,4,2)`, four column edges join the degree-6 and degree-4 rows and two join the degree-6 and degree-2 rows. The two latter columns form a 2×2 rectangle on one support U. In the degree-6 row, the remaining four rays use two support pairs disjoint from U; propagation along degree-2 columns shows no other mixed ray uses an axis of U. The exclusive C4 case excludes even one mate.
* For `(4,4,4)`, there are exactly two column edges between every pair of rows. Fix one row; its four rays use disjoint supports U,U,V,V. If both edges to a second row use U, the two edges to the third use V. The second row's two other rays use a support W disjoint from U, and the third row forces W disjoint from V as well. The three pairwise-disjoint supports each form an exclusive C4. If instead each of the two edges to the second row uses one of U,V, the two edges to the third do the same, and row completeness forces the remaining pair of edges to split U,V as well. All mixed rays use the two disjoint supports, each on a C6, so an exclusive C6 excludes a three-member family.

Thus a Q member in any three- or four-MOQLS(8) cannot have the (3 mixed rows, 6 mixed columns, 12 cells) stratum, nor its incidence transpose. This is one new residual exclusion, not a proof that every 12-cell stratum is impossible or a global four-family result. Full arbitrary-complex review of the cycle-axis hypothesis, actual row/column adjacency, light-cell dimension and transition-support argument is required; no parent, formal, human, executable or novelty acceptance is inferred.


## P09 — No 12-cell four-family member with six mixed columns

Original author-artifact SHA256 `bd20c7c8b4c91a754b6ec5c50c01ac8304acad8f971371b3f9ec4fa89b8a826e`; proof reproduced below.

**WRITTEN author candidate; disjoint full review pending.** In an ordinary four-MOQLS(8), no member Q can have exactly 12 mixed cells relative to a chosen actual Q row and exactly six mixed columns. The incidence-transposed statement with six mixed rows also holds. Q and its three mates are arbitrary complex QLS; no classical mate, catalogue, phase or equal-modulus hypothesis is assumed. This excludes one complete 12-cell stratum, not all 12-cell shapes or the four-family target.

Named WRITTEN imports, not yet independently accepted: `P08`, SHA256 0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b, for exclusive-axis support-2 cycles; and `P02`, SHA256 5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8, for an entirely degree-2 mixed incidence graph.

### A bridge of three rectangles

Use the chosen Q row and independently standardize all four members there to their respective coordinate bases. Suppose three mixed 2×2 rectangles have constant Q support sets U,V,W; U∩V=∅ and W meets each of U,V in exactly one coordinate. Suppose the U and V rectangles use disjoint columns and share at least one row. Then at most three family members exist.

For any mate M, each rectangle's four M rays are pairwise orthogonal: row/column pairs are orthogonal as QLS entries and opposite corners have collinear Q rays, forcing orthogonal M rays by Q⊗M. Every U-rectangle Q ray overlaps every W-rectangle Q ray in exactly one nonzero coordinate; likewise for V against W. Consequently the U and V M quadruples are each ONBs of the four-dimensional orthogonal complement of the W M quadruple. Their transition matrix is unitary. For either U-cell in a shared row, its two transition entries against the two V-cells in that row vanish. In that fixed matrix row at most two positions can be nonzero. For distinct mates, M⊗N product orthogonality makes their transition supports disjoint, whereas each transition row is nonzero. Hence at most two mates are possible, i.e. at most three members including Q.

In the cases below, U and V are disjoint because their support-2 rays appear on the same actual mixed Q row. If W fails to meet U, the U rectangle has an exclusive axis; if W fails to meet V, the V rectangle does. Such an exclusive C4 already excludes a single mate by the imported cycle bound. Otherwise the size-2 set W meets each of the disjoint U,V in exactly one axis, so the bridge argument applies. This exhausts the possible W, including W=U or W=V in the exclusive-axis alternatives.

### Degree and support setup

Six mixed columns with 12 cells means every mixed column has degree 2, and both Q rays there have the same support 2. Every incident row has even mixed degree: support-2 rays on one line have identical or disjoint supports, and each support plane is filled by exactly two orthogonal mixed rays. Thus the possible row profiles are `(6,6)`, `(6,4,2)`, `(4,4,4)`, `(6,2,2,2)`, `(4,4,2,2)`, `(4,2,2,2,2)`, and `(2,2,2,2,2,2)`. Regard each column as an edge between its two incident rows; parallel edges represent different columns. Along each degree-2 row and column, the two Q rays have the same 2-support. A degree-4 row contains two disjoint support pairs, each twice; a degree-6 row contains three pairwise-disjoint support pairs, each twice.

The `(6,4,2)` and `(4,4,4)` profiles are excluded by the explicit C4/C6 analysis in the imported cycle packet; the degree-2 profile is excluded by the imported no-degree-2 theorem. In `(6,6)`, all six column edges join the two rows. The degree-6 row uses three pairwise-disjoint support pairs, each twice, so there are three 2×2 rectangles on pairwise-disjoint supports; each is an exclusive C4.

### Four mixed rows

For `(6,2,2,2)`, all six column edges meet the degree-6 row. Each degree-2 row receives two of them and therefore supplies a constant-support rectangle. The three supports are pairwise disjoint in the degree-6 row, so each rectangle has an exclusive axis.

For `(4,4,2,2)`, denote the degree-4 rows A,B and the degree-2 rows C,D. Let e be the number of column edges between C and D.

* e=2: C,D form one W rectangle and A,B share four columns. The latter yield two rectangles with disjoint supports U,V. If W misses one of U,V, that rectangle is exclusive; otherwise the three-rectangle bridge above gives t≤3.
* e=1: C and D each have one remaining edge, and the degree equations force one to A and one to B; the remaining three edges join A to B. Propagating the common low-row supports gives one C8 on support U (the A–C–D–B path plus one A–B edge) and one C4 on a disjoint support V (the other two A–B edges). The V rectangle is exclusive.
* e=0: two edges join A,B, and the other four join high to low rows. Each high row has two high/low edges. If C joins A twice and D joins B twice, the two A–B columns have one common support W disjoint from both low-row supports, and give an exclusive rectangle. Otherwise each low row joins A and B once. If both low-row paths have the same support U, the two A–B columns give a disjoint exclusive-support rectangle V. If they have distinct supports U,V, they are disjoint in row A and the two A–B columns split between U,V; the supports give two exclusive C6s. These cover the high/low degree equations up to swapping A,B or C,D.

### Five mixed rows

For `(4,2,2,2,2)`, let A be the degree-4 row and C,D,E,F the degree-2 rows. Of the six column edges, four meet A and two connect low rows.

* If the two low/low edges are parallel, they give one W rectangle. The other two low rows each join A twice, giving rectangles U,V with U∩V=∅. The exclusive-axis alternative or bridge lemma rules out a four-family.
* If the two low/low edges share one low row but are not parallel, the remaining low row joins A twice and supplies an exclusive U rectangle. The other two A edges are connected through the low/low path and use the disjoint support V forced on A.
* If the two low/low edges are disjoint, each completes a three-edge path from A back to A. The two paths are support-2 C6s with disjoint supports in A, and each has an exclusive axis.

In all cases the 12-cell/six-column stratum is excluded. Transposing the incidence argument preserves the originally selected Q coordinate basis and gives the six-row statement. No conclusion is asserted for the remaining 12-cell boards with at most five mixed rows and columns, and no q2/q3/q4, M(8), A10/A11, formal or novelty gate is closed.


## P10 — A 12-cell 3×4 mixed board has no orthogonal mate

Original author-artifact SHA256 `7e8b9cb83819687b523aac421370349ab11b5b79ddda3a90e09a6e2b050decda`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** Let Q be an order-8 QLS and choose any actual Q row as coordinate basis. If Q has exactly 12 mixed cells on exactly three rows and four columns, then Q has no orthogonal QLS mate. The same conclusion holds for four mixed rows and three mixed columns. The proof uses actual arbitrary-complex rays and the row/column mixed-subspace projectors, with no catalogue, classical mate, phase or amplitude assumption. It excludes this complete 12-cell stratum, not all 12-cell possibilities or the global four-family target.

### 1. Projector balance forces one four-axis row subspace

The 3×4 incidence board is full. Every mixed row has degree 4; every mixed column has degree 3. Let K_i be the 4-axis mixed subspace of row i and T_j the 3-axis mixed subspace of column j. Since both row and column sums of the twelve rank-one Q projectors are the same operator,

`Σ_i P_(K_i) = Σ_j P_(T_j)`,

where P denotes the coordinate projector. Every degree-3 column has at most one support-2 ray: distinct support-2 sets in a 3-set overlap once, while identical orthogonal support-2 rays would force the remaining singleton. Thus each T_j is the full support of at least two Q rays and is contained in at least two of the K_i. The projector identity now implies every axis used by a K_i belongs to at least two K_i: an axis belonging to only one row subspace could occur in no T_j.

If two K_i coincide and the third differs, an axis of the third outside the first two belongs to only one; impossible. Suppose instead the three K_i are distinct. Let g be the number of axes in all three and d_12,d_13,d_23 the numbers in precisely the indicated two. There are no one-row axes, and each row has four axes, so

`g+d_12+d_13 = g+d_12+d_23 = g+d_13+d_23 = 4`.

Thus all d_ij equal some positive integer d and g+2d=4. An axis in precisely rows i,j must appear in two column sets by the projector identity. Any such T is contained in K_i∩K_j, whose size is g+d=4−d; hence d≤1. Therefore d=1,g=2. Each of the three distinct axes belonging to precisely a given row pair requires two columns with T_j=K_i∩K_j, giving six columns rather than four. Contradiction. Hence K_1=K_2=K_3=:K.

Each T_j is a 3-subset of K, so write T_j=K\{a_j}. The projector identity says every a∈K is omitted from exactly one column: the four a_j are distinct. The twelve Q rays can consequently be completed to an actual 4×4 QLS in span(K) by adding the coordinate row e_(a_j); that completion is not assumed classical.

### 2. A row with two support-2 rays is already impossible with a mate

Every mixed cell in this board has support at most 3 because it lies in a degree-3 column. In a degree-4 row, two support-2 rays therefore force all four rays to have support 2. If the two supports agree they fill their plane, leaving the other two rays in the complementary 2-plane. If they are disjoint they fill the 4-axis subspace; an orthogonal support-3 ray would meet one of the two support-2 rays in exactly one coordinate, so the remaining rays have support 2, one on each plane. In either case the supports are U,U,V,V for disjoint 2-sets U,V. Suppose row i has this pattern. Choose a∈U and one column j where the row-i Q ray has support V. Since T_j contains V and has size 3 inside K=U∪V, it contains exactly one axis of U; take a to be that axis. The other two Q rays in column j have full support T_j, because that degree-3 column already contains its unique support-2 ray. The two U-support Q rays in row i and those two full-support column-j Q rays all overlap e_a. The two row-i mate R rays are orthogonal, the two column-j R rays are orthogonal, and each cross Q inner product is nonzero because the supports meet only at a. Therefore all four R rays are pairwise orthogonal.

Five Q rows contain no mixed cells, one being the chosen first row. Each contains Q=e_a, and the five corresponding R rays are pairwise orthogonal and orthogonal to the four selected rays by Q⊗R. This would give nine orthogonal rays in C^8. Hence with a mate each mixed row has at most one support-2 ray.

### 3. The remaining support patterns also force four mate rays

There are at most three support-2 cells, and at most one in any degree-3 column. We choose a mixed row i, a column j, and a coordinate a∈T_j so that:

1. its row-i ray q_j overlaps e_a;
2. the other two Q rays in column j have full support T_j;
3. the other three row-i rays have full support 3.

If a support-2 cell exists, take it as q_j and choose either a in its support. Then its row's other three rays and its column's other two rays have full support. If no support-2 cell exists, choose any row, column and a∈T_j. These are all possibilities.

In row i, let q_0 be the ray in the unique column with missing axis a, and let q_j,q_k,q_l be the remaining three rays. They form an orthonormal basis of K, and q_0,q_k,q_l have full support 3; q_0 has zero a-coordinate, while q_j,q_k,q_l all overlap e_a. Denote by x,y the two other Q rays in column j. They are orthogonal, have full support T_j and hence both overlap e_a. They are both orthogonal to q_j by the column QLS condition.

At least one of x,y must overlap **both** q_k and q_l. Otherwise each is orthogonal to at least one of q_k,q_l. Neither can be orthogonal to both: together with orthogonality to q_j this would make it collinear with q_0, which has zero a-coordinate. Thus each is orthogonal to exactly one of q_k,q_l and is a linear combination of q_0 and the other one. Both coefficients are nonzero. Indeed x and y have zero coordinate a_j, whereas q_0 and q_k,q_l have nonzero a_j coordinates: their own omitted axes are different from a_j. If x and y use the same active basis ray, the zero-a_j condition puts them on the same one-dimensional ray; if they use different active basis rays, their inner product consists solely of the nonzero q_0-coefficient product. Either case contradicts x⊥y.

Choose x or y with nonzero overlap with both q_k and q_l. In any orthogonal mate R, the three rays at q_j,q_k,q_l are pairwise orthogonal because they lie in row i. The fourth, at the selected column-j Q ray, is orthogonal to the R ray at q_j by its column and to the R rays at q_k,q_l by Q⊗R orthogonality and the nonzero Q overlaps. Thus the four R rays are mutually orthogonal and all four Q rays overlap e_a. As in §2, the five Q=e_a light cells in the five unmixed rows force five additional orthogonal R rays, contradiction.

The proof uses no numerical or selected-instance premise. During discovery a bounded exact-support SAT query and a separate rational QLS(4) example were explored; the SAT model was only a necessary support pattern, not a physical witness, and neither is an input to this all-variable proof. Independent mathematical review must reconstruct the projector equality, the two-pair row argument, the exact nonzero-coordinate selection and the 4+5 mate-ray contradiction. No independent, parent, formal, human, executable or novelty verdict is asserted; A10/A11 remain OPEN.


## P11 — An order-8 QLS cannot have a 12-cell 3×5 mixed board

Original author-artifact SHA256 `31b7e1d23d81e954c21f901ae0e3523596fd779a5d058019df170a0c2a5445c2`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** For an arbitrary complex order-8 QLS, relative to any actual row, exactly 12 mixed cells cannot lie in exactly three rows and five columns. The incidence-transposed 5×3 case is also impossible, with the original coordinate basis unchanged. This is a QLS-only exclusion, not a global m12 or four-family claim.

In each degree-k mixed line the mixed rays form an ONB of a coordinate k-space. Degree-2 lines use a common support-2 set; a degree-3 line has at most one support-2 ray, and its remaining rays have full support 3. Two support-2 rays in a line have equal or disjoint supports. On a degree-4 line whose rays all have support at most 3, the presence of two support-2 rays forces all four supports to have size 2, with two disjoint support pairs each used twice: equal pairs span their plane, while distinct pairs are disjoint and a support-3 ray would meet one of them in exactly one coordinate.

We use the following 3-space observation. If u_1,u_2 are orthogonal rays with the same support-2 set U and x_1,x_2 are orthogonal full-support-3 rays on T=U∪{z}, then x_i⊥u_i for both i is impossible. In the ONB u_1,u_2,e_z the two x rays have forms αu_2+βe_z and γu_1+δe_z, and their e_z coefficients β,δ are both nonzero.

The five column degrees must be `(3,3,2,2,2)`: a degree-4 column is impossible with only three mixed rows. Both degree-3 columns meet all three mixed rows, and every Q ray has support at most 3. The three row-degree profiles are `(4,4,4)`, `(5,4,3)`, and `(5,5,2)`.

* `(4,4,4)`: each row meets both degree-3 columns and hence exactly two degree-2 columns. It therefore contains two support-2 rays and, by the degree-4 fact, all its rays have support 2. A degree-3 column then has three support-2 rays, impossible.

* `(5,4,3)`: the degree-3 row meets the two degree-3 columns and one degree-2 column. Its two rays in the high columns have full support 3 on the same 3-set T, so both high-column mixed subspaces are T. The degree-4 row meets the two high and two low columns; its two low-column rays have support 2, so all four of its rays have support 2. If its low supports were distinct, they would be disjoint and the two high rays would use one of each, forcing the 3-set T to contain their 4-axis union. Thus the two low supports agree, and the two high rays have the same complementary support-2 set U⊂T. They are orthogonal. The degree-3 row supplies two orthogonal full-support-T rays, each orthogonal in its column to the corresponding high ray of the degree-4 row, contradicting the 3-space observation.

* `(5,5,2)`: both degree-5 rows meet every column, and the degree-2 row meets both high columns. Each high column therefore has a support-2 ray from the degree-2 row and two full-support-3 rays from the degree-5 rows. In a degree-5 row the three low-column rays have support 2. Two share a support U and span it, while the third has support V disjoint from U: three distinct disjoint 2-sets would need six axes, and three orthogonal rays cannot fit one 2-space. The two high-column rays must lie in the 3-axis complement of U, whose axes are V plus one extra coordinate. Since they have full support 3, both have the same support T. Hence both high-column subspaces are T. The two degree-2-row rays have a common support-2 set W⊂T and are orthogonal; the two full-support-T rays of either degree-5 row are orthogonal and each is orthogonal to the corresponding degree-2-row ray in its column. The 3-space observation gives the contradiction.

All profiles are excluded. This written argument uses no finite computation or numerical/phase premise and needs full independent review. It does not cover the remaining m12 boards with four or five mixed rows and columns; A10/A11 and global q2/q3/q4 remain open.


## P12 — No 12-cell 4×5 mixed board in a four-family

Original author-artifact SHA256 `86ef7a1664b87072b60e157baaf21ca32933b2d952a30dad3c5d574e0eb3ade8`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** For any member Q of an ordinary complex four-MOQLS(8), exactly 12 mixed cells relative to a chosen actual Q row cannot occupy four rows and five columns; the incidence transpose is also excluded. Other members are arbitrary complex QLS. This is a complete 4×5 stratum exclusion, not an all-m12 or global four-family conclusion.

Named WRITTEN inputs: the exclusive-axis cycle bound `P08` SHA256 0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b and the three-rectangle bridge in `P09` SHA256 bd20c7c8b4c91a754b6ec5c50c01ac8304acad8f971371b3f9ec4fa89b8a826e; both need disjoint review. The 3-space observation proved below is repeated explicitly so no selected calculation or source classification is imported.

### Line and 3-space observations

In a degree-k mixed line, its mixed Q rays form an ONB of a complementary k-axis subspace. A degree-2 line has two rays on a common support-2 set; a degree-3 line has at most one support-2 ray. Distinct orthogonal support-2 sets in the same line are disjoint. In a degree-4 line with at least two support-2 rays, if every ray has support at most 3 then all four rays have support 2, in two disjoint pairs each repeated twice. In a degree-4 line with at least three support-2 rays the fourth has support 2 without needing a separate support-size assumption.

If u_1,u_2 are orthogonal rays on a common support-2 set U and x_1,x_2 are orthogonal full-support-3 rays on T=U∪{z}, they cannot also satisfy x_i⊥u_i for i=1,2. In the ONB u_1,u_2,e_z their inner product has the sole contribution of two nonzero e_z coefficients.

### A reusable all-support-2 12-cell lemma

Suppose there are exactly 12 mixed cells, every mixed Q ray has support 2, every mixed-line degree is 2 or 4, and at least one line has degree 4. Pair the two cells on each line having the same support; along degree-4 lines the two pairs have disjoint supports. Row/column partners partition the 12 cells into simple alternating support-constant cycles. The degree-4 line belongs to two distinct cycles, so the only cycle-length partitions are `(4,8)`, `(6,6)`, and `(4,4,4)`.

With two cycles, their supports are disjoint because they both meet the chosen degree-4 line; each has an exclusive axis. The imported cycle bound applied to a C4 or C6 excludes a four-family. With three C4s, the two rectangles meeting that line have disjoint supports U,V and share the line; their opposite-line sets are disjoint, since otherwise their common row/column cell would lie in both rectangles. Let W be the third support. If W misses U or V, that rectangle has an exclusive axis. Otherwise W meets each of U,V once, and the imported three-rectangle bridge gives at most two mates. Thus the lemma rules out a four-family in either case. Transposing all lines is harmless.

### Column profile (4,2,2,2,2)

Each degree-3 row meets the degree-4 column at most once and would meet at least two degree-2 columns, contradicting the degree-3 fact. The only row profile without degree 3 is `(4,4,2,2)`. Every degree-4 row meets three degree-2 columns, so all its four rays have support 2; the degree-2 rows already have support 2. Apply the all-support-2 lemma.

### Column profile (3,3,2,2,2)

Every ray has support at most 3. The row profiles are `(5,3,2,2)`, `(4,4,2,2)`, `(4,3,3,2)`, and `(3,3,3,3)`.

* `(3,3,3,3)`: six incidences lie in degree-2 columns. Some degree-3 row would meet at least two, impossible.

* `(4,4,2,2)`: a degree-3 column can meet at most one degree-2 row, hence meets both degree-4 rows and one degree-2 row. Each degree-4 row meets both high columns and two low columns; its two support-2 low rays force all its rays to have support 2. Each high column then contains at least two support-2 rays, impossible.

* `(4,3,3,2)`: each degree-3 row meets at most one low column and hence meets both high columns. Each high column has only one further incidence. If the degree-4 row meets both, its two low-column rays force all its rays to have support 2; its two high-column support-2 rays are orthogonal and, as the two high columns have the same 3-axis subspace T determined by either degree-3 row, must have the same support U. The two degree-3-row high rays are full-support T, orthogonal, and each is orthogonal to its corresponding U ray, contradicting the 3-space observation.

  If instead the degree-4 row meets only one high column, the degree-2 row meets the other. Each high column has its unique support-2 ray on the degree-4 or degree-2 row, so both degree-3 rows' high rays have full support 3 and the two high-column subspaces coincide at T. The degree-4 row meets all three low columns and has three support-2 low rays, so its high ray also has support 2 and its four support sets are U,U,V,V disjoint. Each of its low-column partner rays lies in a degree-3 row or the degree-2 row; all those partner supports lie in T, as does the high ray. Thus T contains U∪V, four axes, contradiction. The degree-4 row cannot miss both high columns because there are only three low columns.

* `(5,3,2,2)`: the degree-5 row meets every column. The degree-3 row meets both high columns and exactly one low column. Each high column can meet at most one degree-2 row and hence meets the degree-5 row, the degree-3 row, and exactly one low row. The two degree-3-row high rays have full support on a common 3-set T, and so both high-column mixed subspaces are T; their degree-5-row rays have full support T too. The degree-3 row's low ray has support U⊂T; its low-column partner in the degree-5 row has the same support. In that row this support-U ray and the two high rays are orthogonal and span T. The other two rays must lie in the 2-axis complement of T within the row's 5-axis subspace, and hence share a support V disjoint from T.

  If each degree-2 row meets one high and one low column, its two rays share support V by their low-column partner, but its high ray must lie in T, contradiction. Otherwise one degree-2 row meets both high columns and its two rays share a support W⊂T; the other meets both low columns. The degree-3 row's two full-T high rays are orthogonal and each is orthogonal to the corresponding W ray in its column, contradicting the 3-space observation.

All row/column profiles are excluded. This does not settle the remaining 4×4 12-cell board, the original four-family question, numerical M(8), original A10/A11 or novelty. Full independent mathematical review must check the mixed-column neighbor counts, both degree-5-row alternatives, the cycle/bridge imports and the arbitrary-complex nonzero-coordinate claims. No parent, formal, human, configured-family or executable verdict is asserted.


## P13 — The 5×5, (3,3,2,2,2)/(3,3,2,2,2) 12-cell residual

Original author-artifact SHA256 `fb3a73009ecffade1494230a409f7165ce739626dc36e57568acfe44e6f6c34e`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** In an order-8 QLS with 12 mixed cells on five rows and five columns, suppose both mixed-degree profiles are `(3,3,2,2,2)`. If it has even one orthogonal QLS mate, its support-2 boundary must have exactly two 2-cell paths and one 4-cell cycle, and the two paths must use distinct 2-axis supports. All other boundary shapes and the same-support alternative are excluded below. This is a precisely delimited residual, not an exclusion of the whole degree-profile stratum or of 12-cell four-families.

### 1. Forced core and boundary

Standardize the chosen actual Q row to coordinate axes. A degree-2 line has two mixed rays on the same 2-axis support, while a degree-3 line has at most one support-2 ray. Each of the two degree-3 rows must therefore meet both degree-3 columns and exactly one degree-2 column; similarly each high column meets both high rows and exactly one low row. The high/high core is a 2×2 board of four full-support-3 Q rays on a common coordinate 3-set T.

All eight boundary cells meet a degree-2 row or column and therefore have support 2. Join boundary cells when they share a degree-2 line. Four high/low or low/high boundary cells have graph degree one, and the four low/low cells have graph degree two. Along a connected boundary path or cycle, the Q rays alternate between two orthogonal rays on one common support-2 set. Each path has endpoints on high lines, so its 2-support is a subset of T. The graph consists of two paths, with vertex counts `(2,6),(3,5),(4,4)`, or of two 2-paths plus one 4-cycle. A cycle, if present, uses all four degree-2 boundary vertices; the Q support W of that low/low 4-cycle need not lie in T.

There are three Q rows with no mixed cells, including the chosen first row. For any coordinate a, these contain three Q=e_a cells, whose mate R rays are pairwise orthogonal by Q⊗R. They are orthogonal to every selected R ray whose Q component overlaps e_a.

### 2. Identical path supports are impossible

Let U,V⊂T be the two path supports. If U=V, each high/high Q ray has nonzero projection onto U and is orthogonal to the support-U boundary rays on its high row and high column. That projection forces those two boundary rays collinear. As the high core is complete, all four high-line boundary endpoints are the same ray p. Each path has collinear endpoints, so its vertex count is odd. The only possible boundary shape is therefore `(3,5)`; the endpoints of a 2- or 4- or 6-vertex path would be orthogonal.

Let v be the ray in U perpendicular to p. The 3-path and 5-path contain three v-ray cells in total; their R rays are pairwise orthogonal by Q⊗R. The four core Q rays lie in the 2-space span{v,e_z}, where z is the third axis of T, and their actual 2×2 row/column orthogonality makes opposite corners collinear. The four core R rays are therefore pairwise orthogonal. Each core Q ray has full support T and nonzero overlap with v, so all four core R rays are orthogonal to all three v-cell R rays. Every one of these seven Q rays uses both axes of U, so its R ray is in the 6-dimensional complement of those first-row coordinate rays. Seven orthogonal R rays in that space are impossible.

### 3. Distinct path supports exclude every non-cycle shape

If U≠V, the two 2-subsets of T share exactly one axis a. Any Q ray on one path has nonzero inner product with any Q ray on the other, and every such ray overlaps e_a.

For path sizes `(3,5)` or `(4,4)`, choose three consecutive cells from each path. Their mate rays are pairwise orthogonal within each selection: adjacent cells share a row or column, and cells two steps apart have collinear Q rays. Cross-path mate rays are orthogonal by the single shared Q coordinate a. Six selected R rays plus the three light-e_a R rays give nine orthogonal vectors in C^8, contradiction.

For path sizes `(2,6)`, the two endpoints of the 2-path lie on high rows or on high columns, and the two endpoints of the 6-path lie on the other type of high line. Pick a high/high core cell at the intersection of one short-path endpoint's high line and one long-path endpoint's high line. In the short path, its Q ray is orthogonal to the first endpoint and, because it has full support T, overlaps the second; its R ray is orthogonal to both short-path R rays by the shared line and Q⊗R respectively. On the long path choose the three cells in the Q-ray class opposite to the endpoint at the core's high line. The core Q projection on V is nonzero, is perpendicular to the endpoint ray, and hence overlaps this opposite class. The three long-path R rays are orthogonal to one another because their Q rays are collinear; they are all orthogonal to the core R ray and to both short-path R rays. The core and five path Q rays all overlap e_a, so the three light-e_a R rays yield nine orthogonal vectors. Contradiction.

Consequently only two 2-paths plus a 4-cycle can remain, and their path supports U,V must be distinct. In that case the cycle is on the four low/low cells and can have a support W not contained in T; no conclusion about W or the four-family extension is asserted here. This exact case is the next unresolved barrier, alongside the other 5×5 and 4×4/4×5 profiles. A10/A11 and the global q2/q3/q4 target remain open. Full independent review must check path-component classification, endpoint propagation, dimension 6 and the actual core/path selection; no formal, family, parent or novelty gate is claimed.


## P14 — Closing the 5×5 (3,3,2,2,2)/(3,3,2,2,2) 12-cell profile

Original author-artifact SHA256 `8db958397edc7c2e95953eb362a235afc7ba19cb95c225b48ddc1af7cd1b412c`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** No order-8 QLS in this exact 12-cell mixed-degree profile has an orthogonal QLS mate. The named, review-pending reduction `P13`, SHA256 fb3a73009ecffade1494230a409f7165ce739626dc36e57568acfe44e6f6c34e, excludes all but a boundary with two 2-cell paths and one 4-cycle. In fact the following QLS-only argument excludes any one of those 2-cell paths, independent of the cycle support W and independent of a mate.

The reduction's core is a complete 2×2 board of Q rays with full support on a common 3-coordinate set T. Suppose a 2-cell path consists of two Q rays u_1,u_2 in the same degree-2 column, with support U⊂T. They are orthogonal and form an ONB of span(U); their other incidences are the two high rows. Choose either high column of the core. Its two Q rays x_1,x_2 are orthogonal, each has full support T, and x_i⊥u_i because the two cells share high row i.

Let z be the coordinate in T\U. Relative to the ONB u_1,u_2,e_z, orthogonality to u_i gives `x_1=αu_2+βe_z` and `x_2=γu_1+δe_z`. Both β and δ are nonzero because x_1,x_2 have full support T. Their inner product is the single nonzero product of these e_z coefficients, contradicting x_1⊥x_2. If the 2-cell path instead lies in a degree-2 row, exchange the roles of rows and columns in the same argument; the original coordinate basis stays fixed.

Thus the residual is impossible, and the preceding WRITTEN reduction closes this entire degree profile for Q with one mate. The 4×4, 4×5 and other 5×5 12-cell profiles remain open, as do the global four-family, q2/q3/q4 and original A10/A11 gates. Review must reconstruct the named reduction and the full-support/same-2-support observation. This is not a parent, independent-family, human, formal, executable or novelty acceptance.


## P15 — No 12-cell 5×5 mixed board in a four-family

Original author-artifact SHA256 `badc8589907f1d0da02d10c2d49551931f860b9418fbbb29e38c4a3acf3a430e`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** In any ordinary four-MOQLS(8), a member Q cannot have exactly 12 mixed cells on five rows and five columns relative to any chosen actual Q row. All members may be complex and nonclassical. This excludes the complete 5×5 12-cell stratum; it does not exclude the remaining 4×4 or 4×5 strata or prove full classicality.

Named WRITTEN inputs, each independently review-pending: the B/B profile and its reduction/closure `P13` SHA256 fb3a73009ecffade1494230a409f7165ce739626dc36e57568acfe44e6f6c34e and `P14` SHA256 8db958397edc7c2e95953eb362a235afc7ba19cb95c225b48ddc1af7cd1b412c; the exclusive-axis cycle bound `P08` SHA256 0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b; and the three-rectangle bridge in `P09` SHA256 bd20c7c8b4c91a754b6ec5c50c01ac8304acad8f971371b3f9ec4fa89b8a826e.

The only mixed-degree profiles on either side are A=`(4,2,2,2,2)` and B=`(3,3,2,2,2)`. A degree-2 line's rays share support 2; a degree-3 line has at most one such ray. In A/B, every degree-3 column meets at least two degree-2 rows, hence has two support-2 rays, impossible. B/A is the transpose. B/B is excluded even with one mate by the named input. It remains to treat A/A.

### The A/A support-cycle decomposition

Every mixed cell meeting a degree-2 line has support 2. The unique degree-4 row meets at least three degree-2 columns. Three orthogonal support-2 rays in its 4-axis mixed subspace include two on a common 2-set that fill it and one on the disjoint complementary 2-set; the fourth mixed ray is also on that complementary 2-set. Thus **all** mixed Q rays have support 2. On every degree-4 line, they use two disjoint support pairs, each twice; on every degree-2 line, they use one support pair twice.

Pair the two mixed cells with the same support on each row and each column. Each mixed cell has exactly one row partner and one column partner, so the cells decompose into disjoint alternating row/column cycles, each of even length at least four, and each cycle has a constant support-2 set. At a degree-4 line the two cycles through that line have disjoint support sets. The degree-4 row lies in two different cycles, so the possible cycle-length partitions of the 12 cells are `(4,8)`, `(6,6)`, or `(4,4,4)`.

In `(4,8)` or `(6,6)` there are exactly two cycles. Both use the degree-4 row and hence their two support sets U,V are disjoint. No other mixed ray uses either support, so each cycle has an exclusive axis. The imported exclusive-cycle bound excludes a four-family already from the C4 in the first case or from either C6 in the second.

In `(4,4,4)` all three cycles are 2×2 support rectangles. Let U,V be the two supports meeting the degree-4 row; U and V are disjoint. Their rectangles share that row and have disjoint column sets: sharing both a row and a column would place the same cell in both cycles. Let W be the third rectangle's support. If W misses U, an axis of the U rectangle is exclusive; if W misses V, an axis of the V rectangle is exclusive. Otherwise W meets each disjoint 2-set U,V in exactly one coordinate, and the named three-rectangle bridge applies: for every mate, the W rectangle gives a four-dimensional orthogonal complement containing both U and V rectangle bases, while the shared row imposes two zero entries in a transition row. Pairwise product orthogonality makes transition supports disjoint across mates, so at most two mates exist. Either alternative rules out the actual three mates of Q.

All 5×5 degree profiles are excluded at the stated written scope. The remaining 12-cell boards are 4×4 and 4×5 (and transposes); global q2/q3/q4, numerical M(8), original A10/A11, priority and novelty remain open. A full review must reconstruct all named inputs, particularly the arbitrary-outside exclusive-axis condition, cycle partition, the disjoint-column bridge, actual complex product orthogonality and no-four-family scope. No parent, formal, human or configured-family verdict is inferred.


## P16 — The 12-cell 4×4 (4,4,2,2)/(4,4,2,2) profile is impossible in a four-family

Original author-artifact SHA256 `d16ece5820195b57f2b352adb841f6386cf34ab00edce6e7bdaa4baeb304a171`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** For an arbitrary complex ordinary four-MOQLS(8), no member Q can have exactly 12 mixed cells on four rows/four columns with both degree profiles `(4,4,2,2)`. This is one explicit remaining profile, not a full m12/global classicality or A10/A11 result.

Named review-pending import: the all-support-2 12-cell lemma in `P12`, SHA256 86ef7a1664b87072b60e157baaf21ca32933b2d952a30dad3c5d574e0eb3ade8, which itself names the exclusive-axis cycle and three-rectangle bridge dependencies. The remainder is independent written actual-vector reasoning.

### The common 4-axis core and crossed support partitions

Independently standardize the chosen actual Q row and the same board row of its three mates R,S,T to their coordinate bases. The two degree-4 rows and columns meet every incident line. The 12 mixed cells are the 2×2 high/high core, four high-row/low-column cells, and four low-row/high-column cells; the 2×2 low/low board is empty. Every low-line Q ray has support 2, and both Q rays in a low line have the same support.

If any core ray has support 2, its high row has at least three support-2 rays, forcing its fourth ray to have support 2. Its high column does likewise, and the opposite high row then has three support-2 rays and also becomes all-support-2. Thus all 12 mixed rays have support 2; apply the named all-support-2 lemma. Otherwise every core ray has support 4: it cannot have support 3 because a 4-mixed line containing two support-2 rays cannot contain a support-3 ray. A full-support-4 core ray identifies its high row and high column's 4-axis mixed subspaces, so all four high lines share one 4-set K and all core rays have full support K.

Call U,V the supports of the two low columns. They are disjoint 2-subsets of K, for their rays in a high row are orthogonal; if they were equal those two rays would fill their plane and the core rays could not have full support K. Call X,Y the supports of the two low rows, likewise a disjoint partition of K. No X or Y can equal U or V. For example, if X=U then any full-K core ray has nonzero projection into U and is orthogonal both to its high-row boundary ray on U and its high-column boundary ray on X, forcing those two boundary rays collinear. Varying the high row then forces two orthogonal rays in the same low column collinear. Thus the partitions are crossed: each of X,Y meets each of U,V in exactly one coordinate.

### Every mate core ray is orthogonal to all boundary mate rays

Let u_1,u_2 be the two Q rays on the low column with support U, v_1,v_2 the two on V; their index is the high row. Each pair u_1,u_2 and v_1,v_2 is orthogonal. A core ray in high row i is perpendicular to u_i and v_i, but has nonzero projection into U and V because it has full support K. Its projections are therefore collinear with u_(3−i) and v_(3−i), and it overlaps both. For any mate M, its core M ray is orthogonal to the boundary M rays in the same row by the QLS property, and to the two boundary M rays in the other high row by Q⊗M orthogonality. Transposing the same argument proves that each core M ray is orthogonal to all four low-row/high-column M rays as well.

Each core Q ray uses all four first-row axes in K, so each core M ray lies in K^⊥, of dimension four. Its four core M rays are orthogonal on common rows and columns. Let α_M,β_M be their two possible opposite-corner overlaps. For every opposite pair, M⊗N orthogonality makes the α-nonzero sets and the β-nonzero sets disjoint across the three distinct mates. At most two mates can have a nonzero α or β, so at least one mate, say R, has α_R=β_R=0. Its four core rays are therefore an ONB of K^⊥. By the preceding paragraph all eight boundary R rays lie in K.

The two R rays at u_1,u_2 are orthogonal in their low column and, by comparison of Q⊗R with the first-row products on U, lie in V; they are an ONB of V. Similarly the two R rays at v_1,v_2 form an ONB of U. Thus the four high-row/low-column boundary R rays form an ONB of K. But any low-row/high-column Q boundary ray has support X or Y and overlaps every U/V boundary Q ray in exactly one nonzero coordinate. Q⊗R therefore makes its R ray orthogonal to that entire ONB of K. It also lies in K, so it would be zero, contradiction.

The conclusion uses all three actual mates only to force one of their opposite-overlap pairs to vanish; it does not claim the full-support-4 core is impossible with fewer mates. Other 4×4 degree profiles `(4,3,3,2)` and `(3,3,3,3)`, their pairings, and all global/A10/A11 questions remain open. Full review must check all-support-2 propagation, crossed partitions, both opposite-corner slots, the simultaneous boundary orthogonality and both named transitive imports. No formal, human, executable, parent or novelty verdict is asserted.


## P17 — The 12-cell 4×4 (4,4,2,2)/(4,3,3,2) profile is impossible for Q alone

Original author-artifact SHA256 `2f562bcc78eeb769719ff6ce3862a582aa03db36d6f2598d78f4c1fbe75e594d`; proof reproduced below.

**WRITTEN author candidate; independent review pending.** An arbitrary complex order-8 QLS cannot have exactly 12 mixed cells on a 4×4 incidence board with row degrees `(4,4,2,2)` and column degrees `(4,3,3,2)`, nor the incidence transpose, relative to any chosen actual Q row. No mate, numerical source, realness or phase condition is used. This is one profile exclusion, not full m12/four-family classicality.

Choose the actual Q row as coordinate basis. A mixed line of degree k has a complementary k-axis subspace whose mixed rays form an ONB. A degree-2 line uses a common support 2; a degree-3 line has at most one support-2 ray. Orthogonal support-2 rays on one line have equal or disjoint support. A 4-mixed line cannot contain two support-2 rays and a support-3 ray: equal 2-supports fill their plane; distinct supports are disjoint and a 3-support meets one of them in exactly one coordinate.

### Forced incidences

Both degree-4 rows meet all four columns. The degree-2 column therefore meets precisely those rows and has common support U. Each degree-3 column already meets the two degree-4 rows; its third cell lies on a degree-2 row and has support 2, so both of its degree-4-row Q rays have full support 3. The degree-4 column meets all rows, and each degree-2 row therefore has one cell there and one in a degree-3 column. The two degree-3 columns meet different degree-2 rows. Let V_1,V_2 be these two low-row 2-supports; let T_1,T_2 be the degree-3 column 3-axis subspaces, K_1,K_2 the two degree-4 row 4-axis subspaces, and L the degree-4 column 4-axis subspace. Each T_j⊂K_1∩K_2 and V_j⊂T_j.

### The two row subspaces coincide

If K_1≠K_2, their intersection has size exactly 3, so T_1=T_2=:T. The low-row rays in the degree-4 column are orthogonal support-2 rays on V_1,V_2⊂T; in a 3-set they cannot be distinct and disjoint, so V_1=V_2=:V. They fill span(V). The two high-row rays in that degree-4 column therefore avoid V. In high row i they lie in K_i\V, a 2-axis set, and are mixed, so have support 2. That high row already has its support-2 ray in the degree-2 column and full-support-3 rays in the degree-3 columns, contradicting the 4-line fact. Hence K_1=K_2=:K.

The two low-row rays in the degree-4 column cannot share their support, for then they fill that 2-plane and its two high-row rays are support 2 in the 2-axis complement of L; this again gives a high row two support-2 rays and a support-3 ray. Thus V_1,V_2 are disjoint. The high-row rays of the degree-4 column cannot have support 2 (same 4-line contradiction) or support 3 (two disjoint low support-2 rays in a 4-line), so both have full support 4. Consequently L=K and V_1⊔V_2=K.

### Projector balance contradicts the row orthogonality

Sum the twelve actual Q rank-one projectors by rows and by columns. All line subspaces are coordinate subspaces, so

`2 P_K + P_(V_1) + P_(V_2) = P_K + P_(T_1) + P_(T_2) + P_U`.

Using V_1⊔V_2=K and writing T_j=K\{a_j}, this is

`P_U = P_(a_1) + P_(a_2)`.

Thus a_1,a_2 are distinct and U={a_1,a_2}. But in either high row its degree-2-column Q ray has support U and is orthogonal to its degree-3-column Q ray with full support T_j. Since U meets T_j in exactly one coordinate, their inner product cannot vanish. Contradiction.

The incidence transpose is valid without changing the original chosen coordinate basis. No assertion is made about profiles `(4,4,2,2)/(3,3,3,3)`, `(4,3,3,2)/(4,3,3,2)` or those with an all-degree-3 side; A10/A11 and global four-family questions remain open. Review must reconstruct forced low-row incidences, full-support conditions, both cases for K, and the exact projector identity. No parent, formal, human, configured-family, executable or novelty verdict is asserted.


## P18 — A 12-cell 4×4 profile with all degree-3 columns: disjoint low supports excluded

Original author-artifact SHA256 `ea94bc7c6fcc2e1f24115347e7c5647a5fd3984177804f55d85631769dd329c6`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** Let Q be an arbitrary complex order-8 QLS with exactly 12 mixed cells on four rows/four columns relative to a chosen actual row. Suppose the row degrees are `(4,4,2,2)` and all four column degrees are 3. If the supports U,V of its two degree-2 rows are disjoint, Q has no orthogonal QLS mate. The incidence-transposed statement also holds. The cases U=V and |U∩V|=1 remain open here; this is not a full profile or four-family conclusion.

Both degree-4 rows meet all four columns, and each degree-3 column contains precisely one of the two degree-2 rows. That low-row Q ray has support 2, forcing both high-row Q rays in the column to have full support 3. Let K_1,K_2 be the 4-axis high-row subspaces and T_j the 3-axis column subspaces. Each T_j is contained in both K_i. If K_1≠K_2, their intersection has at most three axes, so all four T_j equal one 3-set; four orthogonal rays in either high row cannot fit there. Thus K_1=K_2=:K, and every T_j is a 3-subset of K.

Each low row meets two columns and has two orthogonal Q rays on its common 2-support. For either low row, its two column 3-subspaces must differ. Otherwise its two orthogonal support-2 rays u_1,u_2 and either high row's two orthogonal full-support-3 rays x_1,x_2 would lie in one common coordinate 3-space, with u_i⊥x_i in their shared column. In the ONB u_1,u_2,e_z, the two x rays have nonzero e_z coefficients and no other common component, so their inner product is nonzero, contradiction.

Now suppose U∩V=∅. Since U and V each have two axes and lie in K, K=U⊔V. The two U-low-row columns have distinct 3-subspaces containing U, so their missing axes are the two different coordinates of V. Likewise the V-low-row columns omit the two different axes of U. Choose a∈U and the V-low-row column j whose 3-subspace is T_j=V∪{a}.

Let u_1,u_2 be the two orthogonal U-low-row rays, and x_1,x_2 the high-row Q rays in column j. They have full support T_j and are orthogonal. In any mate R, the R rays at u_1,u_2 are orthogonal by their low row; the R rays at x_1,x_2 are orthogonal by their column; every cross Q inner product is nonzero because U∩T_j={a}. These four R rays are therefore pairwise orthogonal, and their Q rays all overlap e_a.

Choose a high-row-1 Q ray y in either U-low-row column, with same-column low ray u_1 after relabeling. It has full 3-support containing U, so y overlaps e_a. Its R ray is orthogonal to R_(u_1) by the shared column and to R_(u_2) by Q⊗R: y's nonzero U-projection is orthogonal to u_1 and hence collinear with u_2. It is orthogonal to R_(x_1) by the high row. Let v be the support-V low ray in column j. The two high rays x_1,x_2 form an ONB of span{v^⊥ within V,e_a}. The Q ray y is perpendicular to x_1 by the high-row QLS property and has a nonzero e_a coordinate, so its projection on that plane is nonzero and proportional to x_2. Hence y overlaps x_2 and Q⊗R makes R_y⊥R_(x_2). These five R rays are pairwise orthogonal.

There are four Q rows with no mixed cells. Each has a Q=e_a cell; their R rays are pairwise orthogonal, and all five selected R rays are orthogonal to them by Q⊗R. Nine orthogonal rays in C^8 are impossible. Full review should check the common K proof, distinct low-row column subspaces, the y/x_2 nonzero projection, and actual first-row product use. No formal, parent, human, executable or novelty gate is asserted; remaining m12 profiles and A10/A11 stay open.


## P19 — A 12-cell 4×4 profile: equal low-row supports exclude a four-family

Original author-artifact SHA256 `ffbc06bbf85b04df46b5e14ab25b05d3fe455f3c8c8b021259a98cd7c82626b1`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** In an ordinary four-MOQLS(8), the profile `(4,4,2,2)` on rows and `(3,3,3,3)` on columns cannot have equal 2-supports U=V on its degree-2 rows. No classical mate, realness, equal-modulus or finite-source hypothesis is assumed. Named WRITTEN import `P18`, SHA256 ea94bc7c6fcc2e1f24115347e7c5647a5fd3984177804f55d85631769dd329c6, establishes the common 4-axis high-row subspace K, full-support-3 high cells, and that each low row's two column 3-subspaces differ. Its disjoint-support case is not needed for this equal-support proof.

Let U=V, and write K=U⊔{c,d}. Every column 3-space contains U and is U∪{c} or U∪{d}. Each low row has one column of each kind. In the two columns with space U∪{c}, write u,v for the support-U low Q rays, one from each low row. The two high Q rays in each column form an ONB of the 2-plane `u^⊥∩span(U,e_c)` or `v^⊥∩span(U,e_c)`, respectively. They have full support 3, and the Q rays in corresponding high rows of the two columns are orthogonal.

If u,v were not collinear, these two 2-planes would intersect only in span(e_c). The 2×2 cross-Gram matrix of the two ONBs has zero diagonal because of the two high-row orthogonalities. Its operator norm is 1 because the planes share e_c; a zero-diagonal 2×2 matrix of norm 1 has an off-diagonal entry of modulus 1. The corresponding high Q rays would be collinear and lie in the intersection span(e_c), contradicting their full support 3. Hence u and v are collinear. The same argument applies to the two columns with space U∪{d}. The two distinct low-row rays in a fixed low row are orthogonal, so call their classes p for the c-columns and p^⊥ for the d-columns.

In each pair of c-columns the two high Q bases now lie in the same 2-plane. High-row orthogonality makes their opposite high-cell rays collinear; adjacent cells share a row or column. Therefore for any mate M, the four M rays on these c-column high cells are pairwise orthogonal. The same holds for the four d-column high cells. Every one of these eight Q rays has nonzero coordinate a for any chosen a∈U. Exactly four Q rows contain no mixed cells; their four light Q=e_a cells give four pairwise-orthogonal M rays, all orthogonal to the eight high-cell M rays by Q⊗M. Thus the c-column four and the d-column four are each ONBs of the same 4-dimensional complement of those light-cell rays.

For any mate M, the transition matrix between these two 4-ray ONBs has, in each row, two zero entries from the two d-column cells sharing its actual high row with the selected c-cell. For distinct mates M,N, M⊗N orthogonality makes their transition supports disjoint. Each transition row is nonzero, but has at most two available positions, so at most two mates can exist. This contradicts a four-family.

The two other cases are covered only partially: the named packet excludes U∩V=∅ with one mate, while |U∩V|=1 remains open. The transpose is obtained by exchanging incidence roles while preserving the original chosen coordinate basis. No A10/A11, numerical M(8), general m12, formal, human or novelty acceptance follows. A review must reconstruct the 2-plane cross-Gram norm-1 step and actual 4+4 mate subspace/transition argument, as well as the imported K/distinct-subspace proofs.


## P20 — A 12-cell 4×4 profile: one-axis low-support overlap is QLS-impossible

Original author-artifact SHA256 `a42c7866d2f201dfd79b0f0764f6c66533ff6629a18808382a5703d12cd1d6cf`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** An arbitrary complex order-8 QLS cannot have exactly 12 mixed cells on a 4×4 board with row degrees `(4,4,2,2)`, column degrees `(3,3,3,3)`, and two low-row support-2 sets U,V intersecting in exactly one axis. No mate, realness, equal-modulus or computational premise is used. The incidence transpose follows with the original Q coordinate basis fixed.

Named WRITTEN input `P18`, SHA256 ea94bc7c6fcc2e1f24115347e7c5647a5fd3984177804f55d85631769dd329c6, proves that both degree-4 row subspaces equal one 4-axis set K and that each low row's two 3-axis column subspaces are distinct; all high-column rays have full support 3. Let U={a,b}, V={a,c} and K={a,b,c,d}. The two columns meeting the U-low row must have spaces U∪{c} and U∪{d}; the two meeting the V-low row must have spaces V∪{b} and V∪{d}.

Consider the two columns with spaces U∪{d} and V∪{d}. Their low Q rays have supports U and V. Let u and v be the orthogonal complements of those low rays within their respective 2-planes. Both u,v have support exactly U,V, so they are noncollinear. The two high Q rays in the U∪{d} column form an ONB of span{u,e_d}; those in the V∪{d} column form an ONB of span{v,e_d}. The two 2-planes intersect only in span(e_d).

The 2×2 cross-Gram matrix between these two high ONBs has zero diagonal, because corresponding high-row Q rays occupy the same row and are orthogonal. Its operator norm is 1 because the planes share e_d. Hence an off-diagonal entry has modulus 1, forcing the corresponding pair of normalized Q rays to be collinear in the plane intersection span(e_d). This contradicts their full-support-3 property. Therefore the one-axis case is impossible even before introducing a mate.

Together with the named disjoint case (no one mate) and `P19`, SHA256 ffbc06bbf85b04df46b5e14ab25b05d3fe455f3c8c8b021259a98cd7c82626b1 (equal support, no four-family), these review-pending written candidates exclude the entire `(4,4,2,2)/(3,3,3,3)` profile and its transpose from a four-family. Other m12 4×4 profiles `(4,3,3,2)/(4,3,3,2)`, `(4,3,3,2)/(3,3,3,3)`, and `(3,3,3,3)/(3,3,3,3)` remain open. No parent, formal, human, executable, numerical M(8), A10/A11 or novelty gate is claimed.


## P21 — The 12-cell 4×4 (4,3,3,2)/(4,3,3,2) profile is impossible for Q alone

Original author-artifact SHA256 `e3f7708da67406d34ff1c218290ca0a127fee94b65d3ac52590d3a48374d53b1`; proof reproduced below.

**WRITTEN author candidate; full disjoint review pending.** An arbitrary complex order-8 QLS cannot have 12 mixed cells on a 4×4 board with degree profile `(4,3,3,2)` on both sides, relative to any chosen actual Q row. No mate, external classification, realness, equal-modulus or computation is assumed. This is the last 4×4 degree-profile case for the separate universal m12 synthesis; that synthesis and all its dependencies still require review.

### A degree-4 line lemma

In a degree-k mixed line, its mixed Q rays form an ONB of a complementary k-axis subspace. Degree-2 lines have a common support 2. A degree-3 line has at most one support-2 ray. Two orthogonal support-2 rays on one line have equal or disjoint supports. A degree-4 line cannot contain two support-2 rays and a support-3 ray: same supports fill their plane; disjoint 2-supports cover all four axes, and a 3-support meets one of them in exactly one coordinate.

**Stronger fact:** a degree-4 line cannot contain one support-2 ray p and two support-3 rays x,y. If U is p's support in the 4-axis line subspace K, each of x,y must contain both axes of U: a 3-set cannot be disjoint from U inside K, and intersection size one would give a nonzero single-coordinate inner product with p. Their nonzero U-projections are both collinear with the unique ray in U perpendicular to p. If their remaining axes differ, their U-projections give a nonzero inner product. If the remaining axes agree, p,x,y form an ONB of that 3-axis space and the fourth line ray is a singleton on the remaining axis. Both are impossible. In particular three support-2 rays on a 4-line force the fourth to have support 2.

We also use a 3-space observation: if u_1,u_2 are orthogonal on a common support-2 set U and x_1,x_2 are orthogonal full-support-3 rays on `U∪{z}`, then x_i⊥u_i for both i is impossible; relative to the ONB u_1,u_2,e_z, their inner product has a single nonzero e_z contribution.

Let H,A,B,L be the degree-4, degree-3, degree-3 and degree-2 mixed rows, and G,C,D,L' the analogous columns. H and G meet every incident column or row. There are two possible incidence cases.

### Low/low cell present

If `(L,L')` is mixed, row L has precisely G,L' and column L' has precisely H,L. Thus A,B each meet G,C,D and columns C,D each meet H,A,B. The H,L' ray has support 2; H,C and H,D have support at most 3. If exactly one has support 2, the 4-line contains two support-2 rays and a support-3 ray. If neither has support 2, it contains one support-2 ray and two support-3 rays. Both are impossible. Hence H,C and H,D have support 2, and the three-support-2 fact forces H,G to have support 2.

Column G has two support-2 rays at H and L. Its other two rays have support at most 3 because they lie in degree-3 rows; they cannot have support 3, so they have support 2. Each of the columns C,D has a support-2 ray in row H, and its A and B rays have full support 3. The A row's two full-support rays identify the 3-axis spaces of columns C,D; call the common set T. The H,C and H,D Q rays are orthogonal support-2 rays contained in T, and therefore have the same support. The A,C and A,D Q rays are orthogonal full-support-T rays and each is orthogonal to the corresponding H ray in its column. This contradicts the 3-space observation.

### Low/low cell absent

After exchanging A,B or C,D, the mixed incidences are exactly

`H: G,C,D,L'`; `A: G,D,L'`; `B: G,C,D`; `L: G,C`.

Indeed L' meets H and one degree-3 row, say A; L meets G and one degree-3 column, say C. The remaining degree equations force A to miss C and B to meet both C,D.

The A,L' Q ray has support 2, so A,G and A,D have full support 3. The L,C ray has support 2, so H,C and B,C have full support 3. In row H, H,L' has support 2 and H,C has support 3; H,D cannot also have support 3 by the stronger 4-line fact. Since H,D is mixed and belongs to the degree-3 column D, it has support 2. Therefore A,D and B,D have full support 3. The full-support B,C and B,D rays identify one common 3-axis subspace T for columns C,D and row B; the full-support A,D ray identifies T with row A as well.

The two Q rays in the low column L' share support U, so H,L' has support U⊂T because A,L' belongs to row A. The ray H,D has support 2 contained in T. They are orthogonal in row H; two distinct 2-subsets of T overlap once and cannot be orthogonal, so both have support U and fill its plane. But H,C has full support T and is orthogonal to both, impossible. Thus the second incidence case is also excluded.

This QLS-only result plus the separately named 4×4 profile packets can be synthesized only conditionally on complete independent review of each actual proof and import. Global four-family classicality, numerical M(8), original A10/A11, formal/human/executable verification and novelty remain open.


## P22 — The 12-cell 4×4 (4,3,3,2)/(3,3,3,3) profile is impossible for Q alone

Original author-artifact SHA256 `c7044f4ad22117bae630e5225c446b2fc5b6fa265e9fa222ac79fbcd80fe7861`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** An arbitrary complex order-8 QLS cannot have 12 mixed cells on four rows and four columns, with row degree profile `(4,3,3,2)` and all four columns of degree 3. The incidence transpose is likewise impossible, using the same originally chosen coordinate basis. No mate, source catalogue, equal-modulus, reality or numerical premise is used. Other 4×4 profiles are not addressed here.

A degree-k mixed line supplies an ONB of its complementary k-axis subspace; a degree-2 line uses one common support-2 set; a degree-3 line has at most one support-2 ray. A pair of orthogonal support-2 rays in a common 3-set cannot be distinct, since distinct 2-subsets meet once. We also use the following observation: two orthogonal full-support-3 rays x_1,x_2 and two orthogonal support-2 rays u_1,u_2 in their common 3-axis space cannot satisfy x_i⊥u_i for i=1,2, since in the ONB u_1,u_2,e_z the x rays have a single nonzero shared e_z contribution.

Let H be the degree-4 row, A,B the degree-3 rows and L the degree-2 row. H meets all columns. Each column meeting L has a support-2 ray there and hence full-support-3 rays at its other two cells. Since A and B each miss exactly one column, the two L columns omit A and B respectively; the other two columns meet H,A,B. Let the two Q rays in row L have common support U, with orthogonal rays u_A,u_B in the L columns that meet A,B respectively. The column meeting A has the same 3-axis subspace T_A as row A because its A ray has full support 3; similarly the other L column has subspace T_B. Both T_A,T_B contain U and are subsets of H's 4-axis mixed subspace K.

### Same 3-subspace

If T_A=T_B, H's two Q rays in the L columns are orthogonal full-support rays in that common 3-space and each is orthogonal to its corresponding L-row ray u_A or u_B. The observation above gives a contradiction.

### Distinct 3-subspaces

Otherwise T_A∩T_B=U, and write `T_A=U∪{c}`, `T_B=U∪{d}`, `K=U∪{c,d}`. Let C_1,C_2 be the 3-axis subspaces of the other two columns. Summing the actual twelve Q projectors by rows and by columns gives

`P_K + P_(T_A) + P_(T_B) + P_U = P_(T_A) + P_(T_B) + P_(C_1) + P_(C_2)`,

so `P_(C_1)+P_(C_2)=P_K+P_U`. Coordinate multiplicities force C_1,C_2 to be T_A,T_B in some order.

In the column with space T_A, the B-row Q ray belongs both to T_B and T_A and is mixed; its support is exactly U. Similarly the A-row ray in the T_B column has support exactly U. Thus each of those columns already has a unique support-2 ray, and its other two Q rays have full support 3. Let v_B be the B-row support-U ray in the T_A column and v_A the A-row support-U ray in the T_B column.

The H-row ray in the L/B column has full support T_B and is orthogonal to u_B, so its U-projection is a nonzero multiple of u_A. The H-row ray in the other T_A column has full support T_A and is orthogonal to v_B. These H-row rays are orthogonal and their supports meet only in U, so their U-projections are orthogonal. Thus the latter U-projection is a nonzero multiple of u_B, forcing v_B collinear with u_A. Similarly v_A is collinear with u_B.

The A row contains two orthogonal full-support-T_A rays: one in its L column, perpendicular to u_A, and one in the other T_A column, perpendicular to v_B, which is collinear with u_A. They therefore form an ONB of span{u_B,e_c}. But the A-row ray in the T_B column is v_A, collinear with u_B, so it cannot be orthogonal to that ONB. Contradiction.

The full m12 4×4 `(4,3,3,2)/(4,3,3,2)` and all-degree-3/all-degree-3 profiles remain to be analyzed, as do global q2/q3/q4 and original A10/A11. Review must reconstruct the low-column incidence matching, exact projector balance, nonzero support projections and final 2-space saturation. No parent, formal, human, executable or novelty acceptance is inferred.


## P23 — The 12-cell 4×4 all-degree-3 profile is impossible in a four-family

Original author-artifact SHA256 `58e6c68c0858e63c1d50e9da2b5707a6ece0b0a578578ef88c890a4f7d6a7fb8`; proof reproduced below.

**WRITTEN author candidate; disjoint review pending.** In an ordinary complex four-MOQLS(8), no member Q has exactly 12 mixed cells on four rows/four columns when every mixed line has degree 3. This closes the C/C profile only; it is not a complete m12/global/A10/A11 theorem. The proof uses actual Q and mate rays, not a numerical pattern or catalogue.

Choose any actual Q row as coordinate basis and independently standardize the other three members on the same board row. The mixed incidence graph has four row vertices, four column vertices, and all degrees 3, so it is K_(4,4) minus a perfect matching, the cube graph. Every degree-3 line has a 3-axis mixed subspace and at most one support-2 ray: two orthogonal support-2 rays on distinct 2-subsets of the 3-set would share one nonzero coordinate; if their supports agreed they would fill that plane and force the third ray to be a singleton. Thus each line has at least two full-support-3 rays.

Retain the full-support-3 cells as edges of the cube. This graph has minimum degree two. If connected, their full supports identify one common 3-axis subspace T for every mixed line. If disconnected, every component needs at least two row and two column vertices, so there are exactly two components, each a K_(2,2). Each component has a common 3-axis subspace T_1 or T_2. If T_1=T_2, again all lines share T. Otherwise each of the four remaining mixed cells joins different components, has support 2, and is contained in T_1∩T_2. Thus `U=T_1∩T_2` has exactly two axes; the four connecting cells form a perfect matching, all on support U.

### Two distinct component subspaces

In either K_(2,2) core, a full-support-3 Q ray is perpendicular to its row's and column's matching rays on U. Its nonzero projection onto span(U) forces those two matching rays collinear. The core is complete, so all four matching Q rays are one ray p. The four Q rays of the first core lie in `T_1∩p^⊥`, a 2-space, and their row/column orthogonality makes opposite corners collinear. The same holds in the second core. Every core Q ray has a nonzero U-projection collinear with the ray p^⊥ within U. Since T_1∩T_2=U, every Q ray from one core has nonzero inner product with every Q ray from the other.

For any mate R, the four R rays in each core are pairwise orthogonal: adjacent corners share a row/column and opposite Q corners are collinear. All cross-core R pairs are orthogonal by Q⊗R, so these eight R rays are an ONB of C^8. Choose a∈U. There are four Q rows with no mixed cells, including the standardized row; any one has a light Q=e_a cell. Its R ray is orthogonal to all eight core R rays because every core Q ray has nonzero a-coordinate, contradiction. Thus distinct component subspaces are impossible even with one mate.

### Common subspace: cube-ray classification

Now all twelve mixed Q rays lie in one 3-axis set T and every vertex's three incident rays form an ONB of span(T). We give the needed cube classification directly. On any 4-face, if two opposite rays are not collinear, their common orthogonal complement in the 3-space is one-dimensional, so the other two opposite rays are collinear. Hence choose a face with edge rays in cyclic order p,q,p,r, where p⊥q,r.

If q and r are collinear, the four edges leaving this face have the same ray p_0, perpendicular to p and q. The opposite face's four rays alternate between an orthogonal pair in p_0^⊥. The four p_0 edges form a perfect matching; deleting them leaves two disjoint squares whose alternating rays are two ONBs of p_0^⊥.

If q and r are not collinear, let q^⊥ and r^⊥ denote their complements in p^⊥. In cyclic vertex order the four edges leaving the face have rays r^⊥,q^⊥,q^⊥,r^⊥. On the opposite face, the first and third edges are forced to p, being perpendicular to the independent r^⊥,q^⊥; the other two are forced to q and r. The four p edges form a perfect matching. Deleting them leaves two vertex-disjoint squares with alternating ray pairs q,q^⊥ and r,r^⊥. Thus in either case there is a matching ray p occurring four times and, on the two remaining squares, two orthonormal bases q,q^⊥ and r,r^⊥ of p^⊥.

There is some coordinate a∈T used by **all twelve** mixed Q rays. If p has support 2, then every other incident ray at each vertex has full support 3, since a degree-3 line has at most one support-2 ray; choose a in p's support. If p has full support 3, each of the two square bases contains at most one support-2 ray, so across the four square-ray classes at most two coordinates are omitted; one axis a of T is omitted by none.

For any mate M, the four light Q=e_a cells in the four rows without mixed Q cells give four orthogonal M rays. Every mixed Q ray overlaps e_a, so all mixed M rays lie in their 4-dimensional orthogonal complement W_M. The four M rays on the p matching are an ONB of W_M. The four M rays of either square are also an ONB: adjacent cells share a row/column and opposite Q rays are collinear.

If the two square Q bases of p^⊥ differ as ray sets, all four cross-basis Q overlaps are nonzero (two orthonormal bases of a complex 2-space have a zero overlap only when they coincide up to permutation). Q⊗M would make the two square M ONBs mutually orthogonal in W_M, impossible. Therefore any mate forces the two square bases to coincide. There are then three Q ray classes p,q,q^⊥, each appearing four times, and each class's four M rays form an ONB of W_M.

For any mate M, take the transition matrix between the p and q M bases. At each end of a p-matching edge there is a distinct incident q edge, so each transition row has at least two zeros from actual shared row/column orthogonality, leaving at most two positions nonzero. For distinct mates M,N, product orthogonality M⊗N makes their transition supports disjoint. Since each unitary transition row must contain a nonzero entry, at most two mates exist. This contradicts the three actual mates of Q.

The full-support graph alternative and actual cube edge/ray classification must be reviewed independently, along with both dimension arguments and the transition support bound. This packet makes no claim about the remaining `(4,3,3,2)/(4,3,3,2)` profile, M(8), the original A10/A11 exact-input gates, formal or human verification, parent adoption, or novelty.

