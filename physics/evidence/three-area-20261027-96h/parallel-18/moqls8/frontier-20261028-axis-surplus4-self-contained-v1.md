# An active coordinate costs at least four surplus units in a four-family

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; independent full review pending.** In any ordinary complex four-MOQLS(8), choose an actual common board row and independently standardize each member there. For any one member Q and any chosen-row coordinate a, let its off-standard-row a-channel support consist of cells whose Q ray has nonzero a-coordinate. If that coordinate is active in any mixed Q cell, its channel surplus is at least **4**, not merely the elementary minimum 2. This is a necessary condition on one coordinate; it does not solve the four-family alternative, q1/q2/q3/q4, M(8), A10/A11 or priority. No finite input, support-realizability assumption, numerical solver, reality or equal-amplitude premise is used.

## Actual component and budget definitions

An ordinary order-8 QLS is an 8×8 array of unit C^8 vectors whose rows and columns are ONBs. Four QLS Q,R,S,T are mutually orthogonal when each pair's 64 same-cell tensor products form an ONB of C^8⊗C^8. Standardize an arbitrary actual row of each array independently to its own coordinate basis with common column indices. Thus for distinct cells x,y and distinct members M,N, `<M_x,M_y><N_x,N_y>=0`; local coordinate bases in different factors are not identified.

Fix a member Q and coordinate a. Outside the selected row and column a, the nonzero squared a-coefficients form the support of a 7×7 doubly stochastic matrix: each remaining Q row and each remaining Q column has total squared a-coefficient 1. Each connected support component contains equally many rows and columns. A degree-one vertex has coefficient modulus 1, so its Q ray is exactly e_a and its other endpoint also has degree one; every other component has minimum degree at least two. Define `σ_a=e_a−7`, where e_a is the number of nonzero support cells in this off-row 7×7 graph. It is nonnegative; a nontrivial component on k rows and k columns has at least 2k edges and contributes at least k to σ_a.

For the four members, the four coordinate-a support sets are pairwise disjoint, by actual pair-product orthogonality against the selected-row cell a. Thus their edge counts sum to at most 49 and their coordinate surpluses sum to at most 21. Summing these surpluses over all eight axes gives the actual total off-row support surplus and upper bound 168. This 21-unit four-family budget is not the 14-unit five-family budget, and no input-level A10/A11 implication is inferred.

## A sole nontrivial 2×2 component is impossible with one mate

More generally, let Q have an orthogonal QLS mate R in any order n. Suppose the full coordinate-a support graph has just one nontrivial component, a 2×2 block, and all other components are singleton cells. The n−2 singleton Q=e_a cells have pairwise orthogonal R rays and, by Q⊗R orthogonality, are orthogonal to all four R rays in the 2×2 component. Those four rays therefore lie in a 2-space. Their actual row/column orthogonality makes them a 2×2 QLS there, so opposite R rays are collinear. Product orthogonality then forces opposite Q rays orthogonal, while adjacent Q rays are already orthogonal by Q's row/column ONBs. The four Q rays are pairwise orthogonal.

But the total squared a-coefficient of those four Q rays is exactly 2, one from each component row, while Bessel's inequality for four orthonormal rays gives at most 1. Contradiction. In particular positive σ_a cannot equal 2. It cannot equal 1 by the elementary component degree count.

## A sole nontrivial 3×3 component is impossible with three mates

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

## Surplus conclusion and limits

Every positive surplus is at least 2. Surplus 2 forces one size-2 component and all other components singleton; surplus 3 forces one size-3 component with six edges and all other components singleton. Both are impossible in a four-family. Multiple nontrivial components already cost at least 4, and a sole component of size at least 4 costs at least 4. Thus **every active coordinate has σ_a≥4**.

For the four-family 21-unit per-axis budget, four active members consume at least 16 units, leaving at most 5; this alone is not a contradiction. As an independent comparison, five members on the same 7×7 board would have budget `49−5*7=14`, so at most three can be active on any one axis if this written proof applies; that is not an adoption of an old five-family claim or a waiver of original exact-input gates. Original A10 remains GB15/18 with its three literal UNKNOWN inputs; A11 remains open under its stronger contract.

A full independent review must reconstruct the unique-component light-ray dimension, all 6/7/8/9 adjacency counts, the K4-free graph bound and equality case, every actual mate-pair product constraint, and the final Bessel contradiction. This is written only, not parent, human, formal, configured-family, executable-certificate or novelty acceptance.
