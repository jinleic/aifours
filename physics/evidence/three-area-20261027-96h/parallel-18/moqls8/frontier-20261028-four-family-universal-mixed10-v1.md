# Nine mixed cells are impossible for any nonclassical four-family member

**WRITTEN author candidate; no classical-mate, catalogue, solver or finite-witness premise. Disjoint full mathematical review pending.** In an actual ordinary four-MOQLS(8), every nonclassical member Q has at least **ten** mixed cells relative to any chosen actual Q row. The other three members R,S,T may all be arbitrary complex and nonclassical. This is a universal necessary support bound, not a full four-family classicality, M(8), A10/A11 or novelty claim.

The separately review-pending universal ≥9 result `frontier-20261028-four-family-universal-mixed9-v1.md`, SHA256 73e9df96b79f897ef360d26982cda35b5929a85cc674fd82a3f0ad16fa447559, is a named WRITTEN input. This packet excludes exactly nine mixed cells.

## 1. Nine mixed cells force a 3×3 mixed board

Choose an actual row and independently standardize Q,R,S,T there to their own e_j bases with common column labels. A *mixed* Q cell is not a first-row basis ray. Every mixed row or column contains at least two mixed cells. On a line with exactly k mixed cells, its 8−k distinct light singleton rays occupy 8−k axes; the mixed rays form an ONB of the complementary k-coordinate space. Hence a two-mixed line has two rays with the same two-axis support, and a three-mixed line has at most one support-2 ray: two different 2-subsets of three coordinates meet once and cannot be orthogonal; two orthogonal rays on the same two axes force the third to be the remaining singleton.

Suppose there are nine mixed cells. If r rows and c columns meet them, minimum degree two gives r,c≤4. A 2×4 grid has at most eight cells, so, up to exchanging row/column in the counting argument, the only possible pairs are `(3,3),(3,4),(4,4)`.

In a `(3,4)` graph, the four column degrees are `(3,2,2,2)`, and the row degrees are either `(3,3,3)` or `(4,3,2)`. Any degree-3 row intersects at least two degree-2 columns. Its corresponding Q rays both have support size 2 by the two-line fact, contradicting the three-line fact. In a `(4,4)` graph, row and column degrees are each `(3,2,2,2)`; the degree-3 row again meets at least two degree-2 columns and gives the same contradiction. Therefore `(r,c)=(3,3)` and all nine cells of that board are mixed.

## 2. The actual Q mixed board is a classical order-3 QLS in three axes

Each mixed row and column has exactly three mixed rays, at most one of support 2. Consider the bipartite graph of the three mixed rows and three mixed columns retaining just cells whose Q support has size 3. It is K3,3 with at most one edge deleted at each vertex, hence it is connected. A support-3 cell equals the full three-coordinate mixed subspace of its row and of its column, so connectedness identifies **one common coordinate triple T** for all six line subspaces. Every one of the nine actual Q_H rays lies in span(T), and each mixed row/column is an ONB there. The 3×3 Q_H board is therefore an actual order-3 QLS.

Every order-3 QLS is classical. To see this directly, normalize its first row to e_0,e_1,e_2. Its second row has coordinate form `(0,a,b),(c,0,d),(e,f,0)`. If all three rays had support 2, a pair would overlap in exactly one nonzero coordinate and could not be orthogonal. A singleton in the second row, together with column zeros and row orthogonality, forces the other two to be the remaining singleton rays; the third row is then forced columnwise. Thus all nine rays belong to one ONB.

At most one of these three Q basis rays has support size 2 in T: every board row contains all three basis rays, and a three-mixed line permits at most one support-2 ray. At least two Q basis rays therefore have **full support T**. Denote their three occurrences each by p_1,p_2,p_3 and m_1,m_2,m_3. They form the two symbol classes of a classical 3×3 Latin square. Within each class every Q ray is collinear; between classes their row/column mixed-cell graph is a six-cycle `K_(3,3)` minus a perfect matching. Label it so that p_i,m_i are the three nonadjacent pairs.

## 3. Three pair-product mates saturate a five-dimensional span

For any actual mate R, the R rays on the p-class are an orthonormal triple because the Q rays there coincide; the R rays on the m-class are another orthonormal triple. For i≠j, p_i,m_j share a row or column and their R rays are orthogonal. Every one of the six selected Q rays uses all three first-row axes in T, so comparing Q⊗R products with the three corresponding first-row products puts all six R rays in the five-dimensional complement of those axes.

The only cross-part R overlaps not already zero are the three numbers `α_i^R=⟨R_(p_i),R_(m_i)⟩`. They cannot all vanish, for that would give six orthogonal vectors in five dimensions. The same statement holds for S and T. At each nonedge p_i,m_i, actual R⊗S, R⊗T and S⊗T product orthogonality makes the nonzero-index sets of their three α-vectors pairwise disjoint. Each is nonempty and there are only three indices, so each set contains exactly one index and the sets partition `{1,2,3}`.

For any one mate, its six selected rays are all pairwise orthogonal except possibly one matched pair. Taking one ray from that pair and all four other rays gives five orthonormal vectors in the five-dimensional complement of T. They are an ONB there; the omitted matched ray is orthogonal to the other four and hence collinear with the selected one. Thus the six selected R rays **span all of** the five-dimensional complement of T. The same is true for S and T.

There are five Q rows with no mixed cells, one being the standardized first row. Choose any first-row axis a∈T and an off-first-row cell y in one of the other four rows with Q_y=e_a. Q_y overlaps every one of the six selected Q rays, so Q⊗R orthogonality forces R_y orthogonal to their full five-dimensional span; hence `R_y∈span(T)`. Likewise `S_y,T_y∈span(T)`.

Comparing Q⊗R, Q⊗S and Q⊗T products at y with their first-row products at column a forces R_y,S_y,T_y all orthogonal to e_a. Thus each is nonzero and supported on only the other **two** axes of T. For any pair among R,S,T, product orthogonality against each first-row product forces their supports at this off-row cell disjoint. Three nonzero pairwise-disjoint supports cannot fit in two axes. Contradiction.

All nine-cell cases are impossible. The named ≥9 input therefore yields **≥10 mixed cells per nonclassical member** of any four-MOQLS(8), including q4. This gives at least 40 total mixed-cell incidences/support-surplus units in q4, or 30 in q3; the incidences may overlap, and the lower budget alone is not a global exclusion.

A disjoint review should reconstruct the incidence count, connected support-3 graph, exact order-3 QLS classification, six-ray five-dimensional saturation, and final same-cell support pigeonhole, as well as both named written inputs. No source priority or stronger acceptance is inferred.
