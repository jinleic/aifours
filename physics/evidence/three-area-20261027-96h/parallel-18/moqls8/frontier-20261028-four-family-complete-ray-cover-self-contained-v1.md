# Complete-ray covering in a putative all-nonclassical four-family

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; independent review pending.** Every cell of an ordinary complex four-MOQLS(8) has a **complete entry ray** in at least one of its four members: a ray occurring once in every row and column of that member. Consequently, if all four members are nonclassical and c_i is the number of complete rays of member i, then

`C=Σ_i c_i ≥ 11`, and at least one member has at least three complete rays.

If C=11, its four counts are a permutation of `(3,3,3,2)`. Thus a putative all-nonclassical four-family necessarily contains a member whose variations relative to any chosen row are confined to at most five coordinate axes. This is a conditional structural reduction for q4, not a four-family witness, full classicality, numerical M(8), original A10/A11 or novelty result.

The complete author proof of the stronger per-axis premise `σ_a≥6` is embedded in Appendix A, including its own earlier component appendices. Nothing is accepted by citation or filename; all proofs remain written and unreviewed. The exact ordinary definitions and physical tensor-product condition are stated again below.

## From coordinate surplus to cell coverage

An ordinary QLS is an 8×8 array of unit C^8 vectors, each row and column an ONB. Four arrays are mutually orthogonal if every pair's 64 same-cell tensor products form an ONB of C^8⊗C^8. Fix any actual common board row r and independently standardize all four members there to their own coordinate bases at the shared column labels. For a member M and index a, call the axis active if a mixed M ray has nonzero a-coordinate. Appendix A proves the candidate `σ_(M,a)≥6` for an active axis. Actual pair-product orthogonality against the row-r cell a makes the four off-row a-support graphs disjoint in a 7×7 board; since each has at least seven edges, `Σ_M σ_(M,a)≤49−4·7=21`. All four cannot be active because `4·6>21`.

If member M is inactive at a, every row and column contains M=e_a: mixed rays avoid a and the line ONB must fill that coordinate with a light singleton. Conversely, if that row-r ray is complete, every other entry in each row is perpendicular to it, so it is inactive. Hence, in row r at column a, at least one of the four entry rays is globally complete. The choice of r was arbitrary, so **all 64 cells** have at least one complete entry ray among the four members. This is an actual-QLS consequence, not the assertion that the four local coordinate vectors are physically identical.

## Complete rays of different members meet exactly once

Let ρ be a complete ray of Q and τ a complete ray of R. Each occurs exactly once in every row and column. A Q entry not collinear with ρ is orthogonal to ρ because its row contains ρ; similarly every R entry not collinear with τ is orthogonal to τ. Therefore a same-cell product Q_x⊗R_x has nonzero inner product with ρ⊗τ exactly when the two complete rays occur in the same cell, in which case the squared inner product is 1. Completeness of the actual Q⊗R product ONB says the sum of those squared overlaps is 1. Thus every pair of complete rays from different members meets at **exactly one cell**. Complete rays within one member have disjoint cell sets.

## The q4 count

Assume all four members are nonclassical. Let c_i<8 be the number of complete rays of member i and put C=Σ_i c_i. Fix i. Its c_i complete rays cover exactly 8c_i cells, leaving `8(8−c_i)` cells. Every complete ray of another member intersects each of those c_i rays exactly once, in distinct cells, and therefore covers exactly `8−c_i` cells outside member i's covered set. Since the other `C−c_i` complete rays must cover all of those remaining cells,

`8(8−c_i) ≤ (C−c_i)(8−c_i)`.

Because c_i<8, this gives `C−c_i≥8` for every i. Summing the four inequalities yields `3C≥32`, so C≥11. The maximum c_i is at least 3. If C=11 then every c_i≤3 by `C−c_i≥8`, and the only four nonnegative integers summing to 11 are `(3,3,3,2)` up to permutation. For the member with at least three complete rays, those complete Q-coordinate axes never appear in a mixed ray, so all its variations relative to any chosen row are confined to at most five of the eight row-basis axes.

The argument does not claim that this five-axis residual is impossible. In particular it does not establish the stronger q4 exclusion or any q1/q2/q3 conclusion.

## Coverage alone is not a contradiction

Even the complete-ray covering and exact pairwise intersection rules, without nonclassicality, are realizable. Take four classical Latin squares of order 8 over the field F_8, `L_i(x,y)=x+s_i y`, with distinct slopes `s_1=1`, `s_2=α`, `s_3=α^2`, `s_4=1+α+α^2`, where `{1,α,α^2}` is an F_2-basis. These slopes sum to zero. For the nonzero F_2-linear field trace Tr, select four symbols of square i by `Tr(symbol)+δ_i=1`, where the four bits δ_i have odd sum. At any cell the XOR of the four selected-indicator expressions is `Tr(4x+(Σ_i s_i)y)+Σ_iδ_i=1`, so at least one selected ray covers that cell. Every selected ray is a complete classical symbol, and any two selected rays from different squares meet once because the squares are orthogonal. The four squares themselves are wholly classical and have eight complete rays each; selecting only four per square is an incidence illustration, **not** a nonclassical four-family or a sharpness witness for C=11.

Complete independent review must reconstruct all of Appendix A, the all-row quantifier, local-basis conventions, exact complete-ray pair intersections and the covering count. The F_8 example is an elementary written construction, not a novelty or priority clearance. Original A10 GB15/18, the three literal UNKNOWNs and stronger A11 remain open. No parent, formal, human, configured-family or executable acceptance is asserted.

## Appendix A — Complete axis-surplus-six proof and its component appendices

The complete author proof is embedded below as mathematics, not an external premise. Its original artifact SHA256 is `4534db97ff45e79ea1d909ad77e6b42d7753d5f9dc93e7ea86ba9765a0bb1a1c`. Historical scope notes inside it refer to their own candidate; all are independently unreviewed.


**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; complete independent review pending.** In any ordinary complex four-MOQLS(8), fix any member Q and any actual Q row. For any coordinate a of that row, if some mixed Q ray uses a, its off-standard-row coordinate-channel surplus satisfies `σ_a≥6`. Therefore the actual 21-unit four-family budget implies that **at most three of the four members can be active at any one standardized-row coordinate**. Equivalently, for every chosen-row column index a, at least one member's locally standardized a-th ray occurs as a light singleton once in every row and every column. Local bases in different members are not identified.

This is a universal necessary condition, not a four-family witness, full classicality, a q1/q2/q3/q4 exclusion, numerical M(8), original A10/A11, formal/human/executable/novelty acceptance, or a resurrection or transfer of an old five-family q3 stratum. The complete earlier proof of `σ_a≥5` is embedded in Appendix A, including its own `σ_a≥4` appendix. No external proof filename, catalogue, numerical solver, equal-modulus or real-vector premise is required. All mathematics remains author-written and unreviewed.

### Setup and surplus-five classification

An ordinary order-8 QLS is an array of unit C^8 vectors whose rows and columns are ONBs. Four arrays are mutually orthogonal if every pair's 64 same-cell tensor products form an ONB of C^8⊗C^8. Independently standardize the chosen actual common board row to each factor's coordinate basis at shared column labels. For different cells x,y and distinct members M,N, actual product orthogonality gives `<M_x,M_y><N_x,N_y>=0`.

Fix Q and coordinate a. Its nonzero a-coefficients form a doubly stochastic support graph on rows and columns, with the selected row/column-a cell a singleton component. Every nontrivial component has equal row and column count k≥2 and minimum degree two; if it has N edges, its surplus contribution is N−k≥k. After removing the selected singleton, the 7×7 graph has surplus `σ_a=e_a−7`. Appendix A proves any positive surplus is at least 5 and proves that a sole nontrivial component with k=2, k=3, or k=4 is impossible in a four-family.

If `σ_a=5`, there are only two possible graphs. With one nontrivial component, k≤5; k=2,3,4 are already excluded, and k=5,N=10 is a 10-cycle. With multiple components each costs at least 2, so there are exactly two: sizes k=2 and k=3, each attaining minimum edge count, hence a 4-cycle and a 6-cycle. Singleton components fill the other rows and columns. We exclude both configurations.

### A cycle's actual two-plane and light-cell pigeonhole

Whenever a coordinate-a component is a cycle, each incident line has exactly two Q rays with nonzero a-coordinate. The line ONB puts e_a in their span. At a cell shared by neighboring lines, that mixed Q ray is not collinear with e_a, so the two line 2-spaces coincide. Connectedness gives one common 2-plane containing e_a, and the Q rays alternate between two perpendicular rays p,q, each using a. This proves a physical vector statement; it is not a support-pattern realization claim.

If **all** nontrivial a-components together use the same ray pair p,q and occupy k rows, then there are 8−k singleton Q=e_a rows. For each actual mate M, their mate rays are pairwise orthogonal and orthogonal to the two k-ray mate classes over p,q, so those classes are ONBs of one k-space W_M. The orthogonality of p,q with both nonzero a-coefficients guarantees some other coordinate b has nonzero coefficients in both: otherwise their a contribution could not cancel. Comparison with the first-row product at b puts M=e_b in W_M^⊥. The singleton-e_a mate rays are an ONB of that complement and one is the standardized-row M=e_a. Each of the three mates therefore has nonzero e_b overlap at one of the other `7−k` singleton cells; pair-product orthogonality forbids two mates using the same cell. Consequently `7−k≥3`, i.e. k≤4.

A sole 10-cycle has k=5, so it is impossible by this exact light-cell pigeonhole.

### A 4-cycle and a 6-cycle

Suppose the two nontrivial components are C4 and C6. Their Q rays alternate in 2-planes P_2 and P_3, both containing e_a. There are three singleton Q=e_a rows, so for any mate M all component M rays lie in their common 5-dimensional orthogonal complement. The two C4 ray classes each give a 2-dimensional mate span; the two C6 ray classes each give a 3-dimensional mate span.

If the two Q planes and their projective orthonormal ray bases coincide, all a-active mixed Q rays use one pair p,q on five rows; the preceding light-cell pigeonhole gives k≤4, contradiction. If the planes coincide but their bases differ, every cross-basis Q overlap is nonzero.

If P_2≠P_3, their intersection is exactly span(e_a). The 2×2 cross-Gram matrix of their Q bases has operator norm 1 because e_a lies in both. It cannot have two zeros in one row or column, since every involved mixed Q ray overlaps e_a. It also cannot have diagonal or off-diagonal two zeros: norm one would make a remaining entry have modulus 1, forcing two basis rays collinear in the plane intersection, hence collinear with e_a, contrary to their being mixed. Thus at least three of the four cross-basis Q overlaps are nonzero in either remaining case.

For any mate M, let A,B be the 2-dimensional mate spans of the two C4 Q-ray classes and C,D the 3-dimensional mate spans of the two C6 classes. Each nonzero cross Q overlap makes the corresponding mate spans orthogonal by Q⊗M. Three edges of a 2×2 bipartite graph include, after relabeling, A⊥C, A⊥D and B⊥D. Since all four spans lie in a 5-space, C=D=A^⊥ and then B=A. The two C4 mate-ray classes are therefore ONBs of the same 2-space. But in the C4 each p cell shares its row and column with the two distinct q cells, so its entire transition row is zero, impossible for a unitary. No ordinary mate can exist in this noncoincident-basis case.

Both surplus-five configurations are excluded. Therefore every active coordinate has `σ_a≥6`. Actual pair-product comparisons with the selected-row cell a make the four members' off-row coordinate-a supports disjoint on a 7×7 board, so `Σ_M σ_(M,a)≤49−4·7=21`. Four active members would cost at least 24, impossible. At least one member is inactive on a; then its coordinate-a support graph has only singleton components and its chosen-row a-th ray occurs once in every row and column.

No full four-family/global conclusion follows merely because the four members may cover different axes. The original A10 GB15/18, the three literal UNKNOWN inputs and the stronger A11 remain OPEN. Complete review must reconstruct Appendix A, all σ=5 component partitions, physical 2-plane propagation, the two-plane cross-Gram zero classification, disjoint mate spans and the light-cell pigeonhole. No parent, formal, human, configured-family, executable, priority or novelty acceptance is claimed.

### Appendix A — Complete proof that an active coordinate costs at least five

The complete earlier author proof, including its own surplus-four appendix, is embedded below. Its original author artifact SHA256 is `665c0f6433b9fac76ac233b0e88d22600eaa4e2034008661497e70b52029cf60`. Historical scope notes refer to their own chapter; none of these claims has been independently reviewed.


**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; full independent mathematical review pending.** In any ordinary complex four-MOQLS(8), fix any member Q, any actual Q row, and any coordinate a of that row. If a is used by a mixed Q ray, its off-standard-row a-channel surplus is at least **5**. The statement uses actual complex vectors and pair-product ONBs, not equal-amplitude, reality, catalogue or support-realizability assumptions. It is a necessary channel condition only: it does not establish a four-family witness, full classicality, q1/q2/q3/q4, a numerical M(8) bound, original A10/A11, formal verification, parent acceptance or novelty.

Appendix A contains the complete written proof that every positive surplus is at least four, including all ordinary definitions, the actual 21-unit four-family per-axis budget, and the exclusions of sole nontrivial components of sizes two and three. It is embedded in this packet, not imported by filename. We exclude every remaining surplus-four configuration. All claims and appendix proofs remain independently unreviewed.

#### Coordinate graphs and exact surplus-four cases

Independently standardize the chosen common board row of all four QLS to their respective local coordinate bases; for distinct cells x,y and distinct members M,N, actual product orthogonality is `<M_x,M_y><N_x,N_y>=0`. In Q's coordinate-a support graph every full graph component has equally many rows and columns because the squared a-coefficient matrix is doubly stochastic. A degree-one vertex is a singleton Q=e_a cell; every nontrivial component has minimum degree two. The chosen-row singleton lies outside all nontrivial components.

A nontrivial component on k rows and k columns and N support cells has N≥2k and contributes N−k to the off-standard-row surplus. Positive surplus four can only be: (i) one 4-row component with N=8; (ii) one 3-row component with N=7; or (iii) two 2-row components, each a 2×2 block. Case (ii) is excluded in Appendix A, which actually excludes all sole nontrivial size-3 components. We exclude cases (i) and (iii) below. We then prove a stronger standalone extension: a sole 4-row component with N=9,…,16 is also impossible.

#### 1. One 4-row, 8-cell coordinate component

Its graph is a single 8-cycle, with two a-nonzero cells on each component row and column. For any such row or column, the two actual Q rays are orthogonal and their span contains e_a: all other rays on the line have zero a-coefficient. Neither ray is e_a. Adjacent row/column 2-spaces therefore agree because they both contain e_a and their shared mixed ray; connectedness gives one common 2-space containing all eight component Q rays. They alternate between two orthogonal rays p,q, four occurrences of each.

The other four rows contain singleton Q=e_a cells. For any mate M, their four M rays are pairwise orthogonal and orthogonal to all component M rays, so the latter lie in a 4-space. Each four-ray p or q class is an orthonormal basis of that same space. Each p cell shares a row and column with two distinct q cells, so each p-to-q transition row has two zeros. For distinct mates their transition supports are disjoint by the actual pair-product ONB. Three unitary transition rows cannot each have a nonzero entry in only two available positions. Contradiction.

#### 2. Two 2×2 coordinate components

The four singleton Q=e_a rows put every mate ray from both components in one 4-space. In each 2×2 component, propagation of the 2-space argument above shows its four Q rays alternate between two orthogonal rays, each with nonzero a-coordinate, spanning a 2-plane containing e_a. For any mate, the two rays over each Q class are orthogonal.

If the two Q 2-planes agree and their ray bases agree, the four occurrences of either common ray give two 4-ray mate ONBs in the 4-space; two row/column zero positions per transition row again contradict three mates. If their bases differ, every cross-basis Q inner product in that 2-space is nonzero.

If the Q planes are different, their intersection is exactly span(e_a). Their 2×2 cross-Gram matrix has operator norm one. It cannot have two zeros in one row or column, since each basis ray has nonzero e_a overlap. If it had two diagonal or two off-diagonal zeros, norm one would force an entry of modulus one and hence a cross-plane ray collinear with e_a, but each component ray is mixed. Thus in all remaining cases at least three of the four cross-basis Q inner products are nonzero.

For a mate M, let A,B be the two-dimensional spans of its two ray classes in the first component and C,D those in the second. Three nonzero cross Q overlaps give three cross orthogonalities among A,B and C,D by Q⊗M. Up to relabeling, A is orthogonal to both C,D and B is orthogonal to D. Since A,C,D are 2-spaces inside a 4-space, C=D=A^⊥ and hence B=A. The two mate ray classes of the first 2×2 component are ONBs of one 2-space, but a transition row has its two row/column neighbor entries zero, impossible. This excludes the two-component configuration without assuming the planes or amplitudes are real.

#### 3. The channel-rank inequality for a sole 4-row component

Suppose now there is a single nontrivial coordinate-a component on k=4 rows and columns, containing N cells, where 8≤N≤16; the other four coordinate-a cells are singleton Q=e_a. Every mate's N component rays lie in a 4-space, perpendicular to the four orthogonal singleton mate rays.

Let A be the number of unordered component-cell pairs sharing a row or column, let H be the number of pairs with **nonzero actual Q inner product**, and let t_4(N) be the largest number of edges in a K5-free graph on N vertices, `floor(3N^2/8)`. Each mate's orthogonality graph is K5-free in dimension four. For every pair of component cells at least two of the three mates are orthogonal; an adjacent pair has all three orthogonal, and a Q-nonorthogonal pair also has all three orthogonal by Q⊗M. These two latter pair sets are disjoint, so

`2*binom(N,2) + A + H ≤ 3*t_4(N)`.  (1)

The graph bound is elementary: a K4-free graph has at most floor(N^2/3) edges by the triangle-deletion/triangle-free Cauchy argument in Appendix A. A K5-free graph with a K4 has at most three edges from any outside vertex into that K4; deleting it and inducting gives the balanced 4-partite bound t_4(N). If it has no K4, the K4-free bound is smaller. Base cases are immediate.

The actual component Q rays give a lower bound on H. Set `S=Σ_x |Q_x><Q_x|` over its N cells. Since the four component rows contain all nonzero a-coefficients in those rows, `<e_a,S e_a>=4` and `tr(S)=N`. In an ONB beginning with e_a, Cauchy–Schwarz for the other seven diagonal entries and `tr(S^2)≥Σ diagonal^2` give

`N + 2 Σ_(x<y) |<Q_x,Q_y>|^2 = tr(S^2) ≥ 16 + (N−4)^2/7`.

Each nonzero-overlap summand is at most 1, so

`H ≥ ceil((16 + (N−4)^2/7 − N)/2)`.  (2)

For N=10,…,16, convexity gives the displayed lower bound on A by making row degrees and column degrees as equal as possible. The table is exact integer arithmetic; no graph enumeration or numerical vector search is a premise.

| N | Minimum A | Minimum H from (2) | t_4(N) | Lower left side of (1) | Upper right side |
|---:|---:|---:|---:|---:|---:|
| 10 | 16 | 6 | 37 | 112 | 111 |
| 11 | 20 | 6 | 45 | 136 | 135 |
| 12 | 24 | 7 | 54 | 163 | 162 |
| 13 | 30 | 8 | 63 | 194 | 189 |
| 14 | 36 | 9 | 73 | 227 | 219 |
| 15 | 42 | 10 | 84 | 262 | 252 |
| 16 | 48 | 11 | 96 | 299 | 288 |

Thus N≥10 is impossible. N=8 was excluded in §1. We now handle the borderline N=9.

#### 4. The N=9 equality case

Every component row and column has degree at least 2, so both degree profiles are `(3,2,2,2)` and A=12. Equation (2) gives H≥6. Equation (1) has lower bound `72+12+6=90` and upper bound `3*t_4(9)=90`, so equality holds and each mate's orthogonality graph has 30 edges.

A K5-free graph on 9 vertices with 30 edges is complete 4-partite with part sizes `(3,2,2,2)`. To see this directly, the K4-free bound is at most 27, so the graph has a K4. Delete it. Equality in `6+3*5+9=30` forces each of the five outside vertices to miss exactly one clique vertex and forces the outside graph to be K5 minus one edge. Adjacent outside vertices cannot miss the same clique vertex, since they and the other three clique vertices would form a K5. The only possible repeated missing label belongs to the unique nonadjacent outside pair; all four labels occur. This is exactly the stated complete 4-partite graph. In a 4-dimensional mate space, all rays in one part are collinear, because they are orthogonal to one ray in each of the other three mutually orthogonal parts.

There are therefore five partitions of the nine component cells into four blocks of sizes `(3,2,2,2)`: the component rows, component columns, and the collinear-ray classes of R,S,T. No two distinct cells share two blocks: row/column intersections are unique, a mate cannot repeat a ray in its row or column, and two mates cannot both repeat their ray at two cells by their product ONB. Let `w_x=|<e_a,Q_x>|^2>0`. Each row or column block has total weight 1. Within any mate-ray block the Q rays are pairwise orthogonal by Q⊗M, so its weight is at most 1 by Bessel. Its four blocks partition the nine cells and total weight is 4; hence each has weight exactly 1. Equality in Bessel means e_a lies in the span of the Q rays in **every** one of the 20 blocks.

Let B be the 9×20 block-incidence matrix, J the all-ones 9×9 matrix, and H_0 the graph whose edges are pairs sharing no block. Every point is in five blocks, each of size at least 2; because no pair shares two blocks, it has at least five distinct block-sharing neighbors, so `deg(H_0)≤3`. Therefore

`B B^T = 4 I + J − Adj(H_0)`.

The symmetric matrix `4 I−Adj(H_0)` is positive definite because the adjacency spectral radius is at most the maximum degree 3; adding J preserves positive definiteness. Hence B has full row rank 9.

Let C be the 8×9 matrix whose columns are the actual Q rays and let D be the invertible diagonal matrix with entries `<Q_x,e_a>`. Expansion of e_a in the orthonormal Q rays of every block gives `C D B = e_a 1^T`. But B has row rank 9 and D is invertible, so the left-hand side has image equal to the image of C. It has rank one; thus every Q ray would be collinear, contradicting the two orthogonal Q rays in any component row. N=9 is impossible.

#### Conclusion and exact remaining boundary

Every surplus-four case is excluded: the sole 2×2+singleton and sole 3-row cases are already excluded in Appendix A; §§1–2 exclude the remaining sole 4-row C8 and two-2×2 alternatives. Hence an active coordinate has **σ_a≥5**. The additional §§3–4 show that any sole 4-row coordinate component, regardless of its edge count, is impossible in a four-family.

The true four-family per-coordinate budget stays 21. Thus if all four members are active at one chosen-row coordinate, they consume at least 20 units and leave at most one; no assertion is made that such a packing is impossible. This theorem does not automatically transfer to any old five-family q3 stratum or literal SAT predicate. Original A10 GB15/18, the three UNKNOWN exact inputs and stronger A11 remain OPEN.

Full review must reconstruct the 2-plane propagation, all 2×2 cross-Gram cases, the actual channel-rank inequality, exact ceiling table, K5-free nine-vertex equality, five physical partitions, Bessel-equality expansion and incidence-rank contradiction, plus Appendix A. No parent, configured-family, formal, human, executable, source-priority or novelty acceptance is claimed.

#### Appendix A — Complete proof that positive surplus is at least four

The entire earlier author proof is embedded below. Its original artifact SHA256 is `9b7790ec7cbe13a5ac3f006a994834451ed95e592589f0c9e22a109850f94d2c`; scope notes in it are historical and it remains independently unreviewed. In particular its comparison with another family size is not an adoption of that family's old frozen claim or any A10/A11 result.


**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; independent full review pending.** In any ordinary complex four-MOQLS(8), choose an actual common board row and independently standardize each member there. For any one member Q and any chosen-row coordinate a, let its off-standard-row a-channel support consist of cells whose Q ray has nonzero a-coordinate. If that coordinate is active in any mixed Q cell, its channel surplus is at least **4**, not merely the elementary minimum 2. This is a necessary condition on one coordinate; it does not solve the four-family alternative, q1/q2/q3/q4, M(8), A10/A11 or priority. No finite input, support-realizability assumption, numerical solver, reality or equal-amplitude premise is used.

##### Actual component and budget definitions

An ordinary order-8 QLS is an 8×8 array of unit C^8 vectors whose rows and columns are ONBs. Four QLS Q,R,S,T are mutually orthogonal when each pair's 64 same-cell tensor products form an ONB of C^8⊗C^8. Standardize an arbitrary actual row of each array independently to its own coordinate basis with common column indices. Thus for distinct cells x,y and distinct members M,N, `<M_x,M_y><N_x,N_y>=0`; local coordinate bases in different factors are not identified.

Fix a member Q and coordinate a. Outside the selected row and column a, the nonzero squared a-coefficients form the support of a 7×7 doubly stochastic matrix: each remaining Q row and each remaining Q column has total squared a-coefficient 1. Each connected support component contains equally many rows and columns. A degree-one vertex has coefficient modulus 1, so its Q ray is exactly e_a and its other endpoint also has degree one; every other component has minimum degree at least two. Define `σ_a=e_a−7`, where e_a is the number of nonzero support cells in this off-row 7×7 graph. It is nonnegative; a nontrivial component on k rows and k columns has at least 2k edges and contributes at least k to σ_a.

For the four members, the four coordinate-a support sets are pairwise disjoint, by actual pair-product orthogonality against the selected-row cell a. Thus their edge counts sum to at most 49 and their coordinate surpluses sum to at most 21. Summing these surpluses over all eight axes gives the actual total off-row support surplus and upper bound 168. This 21-unit four-family budget is not the 14-unit five-family budget, and no input-level A10/A11 implication is inferred.

##### A sole nontrivial 2×2 component is impossible with one mate

More generally, let Q have an orthogonal QLS mate R in any order n. Suppose the full coordinate-a support graph has just one nontrivial component, a 2×2 block, and all other components are singleton cells. The n−2 singleton Q=e_a cells have pairwise orthogonal R rays and, by Q⊗R orthogonality, are orthogonal to all four R rays in the 2×2 component. Those four rays therefore lie in a 2-space. Their actual row/column orthogonality makes them a 2×2 QLS there, so opposite R rays are collinear. Product orthogonality then forces opposite Q rays orthogonal, while adjacent Q rays are already orthogonal by Q's row/column ONBs. The four Q rays are pairwise orthogonal.

But the total squared a-coefficient of those four Q rays is exactly 2, one from each component row, while Bessel's inequality for four orthonormal rays gives at most 1. Contradiction. In particular positive σ_a cannot equal 2. It cannot equal 1 by the elementary component degree count.

##### A sole nontrivial 3×3 component is impossible with three mates

Suppose Q is one member of a four-MOQLS(n) and its coordinate-a support graph has exactly one nontrivial component, on three rows and three columns. Its remaining n−3 components are singleton Q=e_a cells. For any mate M∈{R,S,T}, those n−3 M rays are pairwise orthogonal and orthogonal to every M ray at a component cell. The component mate rays therefore lie in a 3-dimensional space W_M.

The 3×3 support component has N=6,7,8,9 cells: all row and column degrees are at least 2. Let A be the number of unordered pairs of these cells sharing a row or column. A is 6,10,14,18 respectively. In each mate's orthogonality graph on the N cells, all A adjacent pairs are edges. For any other pair, at least two of the three mates' inner products are zero, because every pair among R,S,T has an actual product ONB. Therefore the total number of orthogonality edges across the three mates is at least `2*binom(N,2)+A`.

Each mate's graph is K4-free, since four nonzero mutually orthogonal vectors cannot lie in W_M≅C^3. A self-contained extremal bound is `e≤floor(N^2/3)` for a K4-free graph: if it contains a triangle, delete it; each remaining vertex has at most two neighbors in the triangle, and induction gives the bound. If it is triangle-free, pick an edge: its endpoint degrees sum to at most N, so summing over edges and using Cauchy–Schwarz gives `4e^2/N≤N e`, hence `e≤N^2/4`. The base cases are immediate. Consequently:

| N | Actual row/column adjacency A | Lower bound for three mate graphs | Three K4-free upper bounds |
|---:|---:|---:|---:|
| 6 | 6 | 36 | 36 |
| 7 | 10 | 52 | 48 |
| 8 | 14 | 70 | 63 |
| 9 | 18 | 90 | 81 |

N=7,8,9 are impossible. At N=6 equality holds in all three bounds. A K4-free graph on six vertices with 12 edges is K6 minus a perfect matching: the triangle-free bound is at most 9; otherwise equality in the triangle-deletion argument forces the three outside vertices to form a triangle, each adjacent to exactly two original triangle vertices, and the missed original vertices must be distinct or four vertices would form a K4. In particular, for every non-adjacent pair of component cells, exactly one mate's inner product is nonzero; otherwise the lower total 36 would be exceeded. Q⊗M orthogonality with that mate makes the Q rays orthogonal. Adjacent Q rays are orthogonal in their actual row or column, so all six Q rays are pairwise orthogonal.

The sum of their squared a-coefficients equals 3, one for each component row, contradicting Bessel's upper bound 1. Therefore the sole size-3 component is impossible. The argument treats the actual complex mate vectors and all non-adjacent product constraints; no classical coloring or support-only certificate is substituted.

##### Surplus conclusion and limits

Every positive surplus is at least 2. Surplus 2 forces one size-2 component and all other components singleton; surplus 3 forces one size-3 component with six edges and all other components singleton. Both are impossible in a four-family. Multiple nontrivial components already cost at least 4, and a sole component of size at least 4 costs at least 4. Thus **every active coordinate has σ_a≥4**.

For the four-family 21-unit per-axis budget, four active members consume at least 16 units, leaving at most 5; this alone is not a contradiction. As an independent comparison, five members on the same 7×7 board would have budget `49−5*7=14`, so at most three can be active on any one axis if this written proof applies; that is not an adoption of an old five-family claim or a waiver of original exact-input gates. Original A10 remains GB15/18 with its three literal UNKNOWN inputs; A11 remains open under its stronger contract.

A full independent review must reconstruct the unique-component light-ray dimension, all 6/7/8/9 adjacency counts, the K4-free graph bound and equality case, every actual mate-pair product constraint, and the final Bessel contradiction. This is written only, not parent, human, formal, configured-family, executable-certificate or novelty acceptance.
