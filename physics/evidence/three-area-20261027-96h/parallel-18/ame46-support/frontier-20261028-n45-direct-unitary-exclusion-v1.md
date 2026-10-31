# Direct candidate exclusion of support 45 for AME(4,6)

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 21:06:30 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, not independently accepted, formally verified, or novelty-cleared. This is a direct attack on N=45; it is separate from the frozen N=46 t=27–29 review.

## 1. Claim and one named prerequisite

Assume the separately recorded statement that every normalized complex AME(4,6) state in every product basis has at most 29 coefficients of modulus 1/6. This is [parent disposition f113](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md), SHA-256 `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`; it is same-harness written support conditional on the prior t≤30 argument and the classical no-OLS(6) theorem, which was not reproved there.

**Candidate:** under that prerequisite, no AME(4,6) state has support exactly 45 in any product basis. If independently accepted together with the separately recorded [global N≥45 disposition](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-global-support-lower45-parent-v1.md), SHA-256 `28ffc96f2b7295dd62c7efcfe39d066ac1a77449fbf0804a67c86cbce8c8a8cc`, this would yield global N≥46 at the inherited no-OLS(6) boundary. That synthesis is **not adopted here**. No 46-support witness, exact minimum, priority result, human review, external model-family review or formal proof is claimed.

## 2. Residual unitary and possible t

For every 2|2 cut of a normalized AME(4,6) state, `U=6ψ` is a 36×36 unitary. A coefficient of modulus 1/6 exhausts the norm of every row and column containing it. Let P be these t singleton positions, E all other nonzero positions, and `n=36−t`. Deleting the matched singleton rows and columns leaves an n×n unitary. Every residual row and column is nonempty and has at least two entries, since a singleton unitary row or column would have been in P.

Each of the six E coordinate-pair projections has exactly n values and every value has at least two E extensions. Thus

`45=t+|E|≥t+2(36−t)=72−t`,

so t≥27. The stated prerequisite gives t≤29. The only cases are

| t | residual size n | |E| | row-degree excess `|E|−2n` |
|---|---:|---:|---:|
| 27 | 9 | 18 | 0 |
| 28 | 8 | 17 | 1 |
| 29 | 7 | 16 | 2 |

We use only complex-unitary orthogonality and the incidence count below to rule them out.

## 3. Three elementary unitary-support facts

Two distinct rows of a unitary cannot overlap in exactly one nonzero column; their inner product would contain exactly one nonzero summand. The same is true for columns.

**Zero excess.** If all rows and columns have degree at least two and the support has exactly 2n entries, every row and column has degree two. Its bipartite support graph is a union of even cycles. Any component longer than a 4-cycle has two rows with exactly one common column, so every component is a full 2×2 block and n is even. This excludes the n=9 case.

**One excess.** If the support has 2n+1 entries, one row R has degree three and every other row degree two. Every column of R has at least one other row. A degree-two row meeting R must use two of R's three columns. Two distinct two-subsets of a three-set intersect in exactly one column, which would violate row orthogonality; hence all such rows use the same pair and R's third column has no other neighbor. That column would have degree one, contradiction. This excludes the n=8 case.

**Two excess: maximum degree three.** Suppose the support has 2n+2 entries. The row-degree excess is either two degree-three rows, or one degree-four row R. In the latter case, every other row has degree two. As above, any row meeting R must use two of its four columns. Different occurring two-subsets cannot intersect in exactly one column, so to give all four of R's columns another neighbor they must be two disjoint pairs. At most one degree-two row can use a given pair: two orthonormal rows supported on the pair span C² and would force R to vanish there. Consequently each pair's columns are supported on R and one other row only. Those two columns form a 2×2 unitary, so R already has norm one on that pair, contradicting its nonzeros on the other pair. Thus a degree-four row is impossible and every residual row has degree at most three. Applying the same argument to `U†` gives the column bound. In the n=7 case, every E pair value therefore has **two or three** extensions.

These arguments use actual complex row/column orthogonality and norms. They do not rely on an uncertified solver status. A previous supplementary n=5 support-pattern count omitted a square-component filter; that control was corrected separately and is not used as proof here.

## 4. The seven-row case forces ternary residual alphabets

Assume t=29,n=7,|E|=16. For a coordinate with r residual symbols, each symbol fiber must vary in at least two other coordinates: otherwise some occurring pair value would have only one E extension. For each other coordinate, the sum of the numbers of extra partner values across the r fibers is `7−r`; hence at most `7−r` fibers vary in it. Counting variation incidences gives

`2r≤3(7−r)`, so `r≤4`.                                           (3)

If a coordinate took four residual values, each of its four fibers would contain at least four E words: select a coordinate in which the fiber varies and use its two distinct pair values, each with at least two extensions. In any other coordinate the fiber cannot be constant, for that would give one pair value with at least four extensions, exceeding the degree-three bound. Thus every one of the four fibers varies in any chosen other coordinate, giving at least eight distinct pair values, contrary to n=7. Hence every residual alphabet has size at most three. Each pair projection has seven values, so no alphabet can have size one or two when its partner has at most three values. All four residual alphabets therefore have size exactly three.

## 5. Counting the maximal words

Call a coordinate of a P word active when its value lies in the corresponding E alphabet. For any fixed party i, there are `6·3=18` possible pair values with i active and a symbol of another party. Exactly seven are residual E pair values; the other 11 are represented by distinct P singleton rows. Thus exactly 11 P words are active at i.

For any party pair ij, there are nine active/active pairs. Seven occur in E, leaving exactly two represented by P. If k(x) is the number of active coordinates in P word x, then

`Σ_{x∈P} k(x)=4·11=44`,  `Σ_{x∈P} C(k(x),2)=6·2=12`.

But `k−C(k,2)` takes the values `0,1,1,0,−2` for k=0,1,2,3,4 and is at most 1. Therefore

`32=Σ_{x∈P}[k(x)−C(k(x),2)]≤|P|=29`,

contradiction. The n=7 case is impossible, so no N=45 state exists under the stated t≤29 prerequisite.

## 6. Bounded controls and review scope

The earlier exact small-support control `frontier-20261028-unitary-one-excess-controls-v1.py` has SHA-256 `ab2a08d06b5a267503a8779c46888d5789bea70f36800157598796a0ebb09c7d`; its receipt has SHA-256 `c79d6b6ea68f5b38592a091bdccfe6c88484526197acf79c8d2b9f62fb781813`. The hardened two-excess control has source SHA-256 `e8a2d9adbdeb11e4a42bd5a9326a41ae3100b479a345b5790c3a54b9dddf31d7` and receipt SHA-256 `724018a563d3667860ba614fda117abf5c23729f1616961bc0a277048c77bf04`; it explicitly excludes rectangular support components and reports 900, not 1,000, n=5 survivors. The active-count arithmetic source has SHA-256 `dccb5f9afa3ccefbb096f1c4dfe5992cd72644410eeb0e293ec30009a69e84b4`, receipt SHA-256 `c49c56b773400248fb7ee2c11e3bb42bdd78c824d2bf68a6bf3d55a5bceee7b6`.

These bounded same-harness controls do not replace a review of the general complex-unitary proof, and the t≤29 prerequisite retains its recorded classical import. The N=46 t=26 alphabet branches and the exact global minimum are not settled by this packet.
