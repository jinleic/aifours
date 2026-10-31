# Candidate global AME(4,6) support lower bound 44

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:49:24 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, not an independently accepted or formal proof. This strengthens the complete ≤30-maximal-coefficients candidate `frontier-20261028-global-ame46-lower42-review-packet-v2.md`, SHA-256 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`; review of that dependency is prerequisite. The only named external mathematical import is the classical no-OLS(6) theorem.

## 1. Claim and scope

For **every** complex AME(4,6) state and **every** product basis,

`support(ψ) ≥ 44`.                                                     (1)

Together with the published 60-support witness, this would give `44≤m≤60` for the global minimum. [Pandya arXiv:2610.16673v1 §VI](https://arxiv.org/html/2610.16673#S6) reports 38 as a lower bound; this is only a comparison with that cited statement, not a completed priority or novelty audit. No 44-support state is claimed.

The proof has two parts: exclusion of the sole possible 42-support case using the residual support's unitary coupling, and exclusion of the two possible 43-support cases by an elementary unitary-support lemma.

## 2. Prerequisites and a unitary-support lemma

As proved in the dependency, let t be the number of coefficients with modulus 1/6 and E the nonmaximal support. The maximal coefficients are singleton rows and columns in every 2|2 flattening. The residual matrix in every cut is an `n×n` unitary with `n=36−t`; every residual row and column has at least two nonzeros, and every two-coordinate projection of E has cardinality n. The dependency proves `t≤30` and the global count `N≥72−t`. It also proves the incidence bound: if a residual coordinate uses r values, then `2r≤3(n−r)`.

We need two general support facts for any n×n unitary V with no singleton rows or columns. If two distinct rows share a nonzero column, they must share **at least two** nonzero columns; otherwise their inner product has exactly one nonzero term.

**Lemma.** Such a V cannot have exactly `2n+1` nonzero entries. If it has exactly `2n`, then n is even and its support is a disjoint union of full 2×2 blocks.

Proof. With `2n+1` entries, exactly one row has degree three and every other row has degree two. Let the exceptional row use columns `{a,b,c}`. Every one of these columns has degree at least two. Every other row meeting the exceptional row must use two of its three columns, to avoid a unique overlap. Distinct two-subsets of `{a,b,c}` intersect in exactly one column, so all those neighboring degree-two rows must use the **same** two-subset; then the third column has no other neighbor, contradiction.

With `2n` entries, every row and column has degree two. The support graph is a union of even bipartite cycles. A component longer than a 4-cycle contains two rows sharing exactly one column, which is impossible. Each component is therefore a complete 2×2 block, so n is even. ∎

## 3. The only putative 42-support case

If N=42, the dependency's `t≤30` and `N≥72−t` force

`t=30`, `n=6`, `|E|=12`.                                           (2)

Every residual row has degree at least two, so all 12 entries are needed to give the six rows degree exactly two. This holds in **every** cut: each of the six coordinate-pair projections has six values, each with exactly two E extensions.

By the dependency's incidence bound, every local residual alphabet has size at most `floor(18/5)=3`. No coordinate is constant, since its pair projection with another coordinate would then have at most three values rather than six. No two coordinates can both use two values, since their pair projection would have at most four values. Hence either all four alphabets have size 3, or exactly one has size 2 and the others size 3.

Fix any size-3 coordinate A. Each of its three nonempty fibers varies in at least two other coordinates. For any varying coordinate j, each of its values forms a pair `(A,j)` with exactly two extensions, so the fiber has at least four entries. Since |E|=12, each A fiber has exactly four entries. For every other coordinate, in each fiber it therefore assumes exactly two values, each twice.

If a second coordinate j also has three values, its three fibers likewise have size four. Thus the pair projection `π_Aj(E)` is a 3×3 bipartite graph where every vertex has degree 2: it is the complement of a perfect matching. Independently relabel the three values of every size-3 coordinate j so that the missing matching is the diagonal; in the A=g fiber, j then takes the two values other than g.

For any pair of the other coordinates inside a four-point A fiber, their 2×2 frequency table has row and column sums two. It is therefore either full (four different pairs, each once) or perfectly correlated (two pairs, each twice). A fiber can be perfectly correlated on **at most one** of the three coordinate pairs: two such correlations would make all three coordinates functions of one binary value, giving at most two tuples, not four.

## 4. Four ternary residual alphabets are impossible

Suppose all four local residual alphabets have size three. For any pair j,k among the three non-A coordinates, their possible pair values in A fiber g lie in the 2×2 square `(3\{g})×(3\{g})`. Squares for two different g intersect in exactly one pair. If two A fibers had full j,k projections, their union would have 7 pairs, contradicting `|π_jk(E)|=6`. Hence at least two fibers are perfectly correlated on j,k.

This requirement holds for each of the three pairs j,k, demanding at least six fiber/pair correlations. But each of the three fibers supplies at most one, a maximum of three. Contradiction.

## 5. One binary residual alphabet forces a forbidden Latin completion

Now suppose B has two residual values and A,C,D each have three. Normalize A,C and A,D as in §3: in the A=g fiber both C and D use the two colors other than g. The same square-intersection argument shows at least two A fibers have a two-point, perfectly correlated C,D projection.

In such a fiber B takes both of its values, and each of its two C,D pairs appears with both B values. Each C,D pair already has its full allowed multiplicity two. Therefore the two correlated fibers' C,D pair sets are disjoint, and no third fiber can use any of those four pairs. If the third fiber had a full four-point C,D projection, the total projection would have at least eight pairs, not six. Hence all three fibers are C,D-correlated and B is free in each. Thus

`E = S × {b_0,b_1}`,

where S is a six-element set of triples on A,C,D. Every coordinate value in S occurs twice, and each two-coordinate projection of S is injective: E has six pair values and each S tuple occurs at both B values.

Make a graph with vertex set S, joining two triples when they share A, C, or D. They cannot share two of these coordinates. Each shared coordinate value occurs in exactly two triples. Let `u_{s,0},u_{s,1}` be the two nonzero residual-unitary coefficients at s and B=b_0,b_1, and define `r_s=u_{s,0}/u_{s,1}`.

For any graph edge s—s′, choose the 2|2 flattening whose row indices are B and the coordinate they share. The two corresponding columns have nonzeros only at those two B rows, so their orthogonality gives

`conjugate(r_s) r_{s′} = −1`, equivalently `r_{s′}=−1/conjugate(r_s)`.  (3)

The map `r↦−1/conjugate(r)` is an involution and has no fixed nonzero complex value. Thus (3) forbids every odd cycle: the graph is bipartite. Choose a 2-coloring and assign one of b_0,b_1 to each vertex s according to its color. The resulting six selected words are pairwise distinct on every pair of coordinates: any two s agreeing in one of A,C,D are adjacent and receive different B values, while no two s agree in two of A,C,D.

No selected word shares a coordinate pair with any existing maximal word in P, since each selected word was already an E support position and every maximal coefficient exhausts its pair row. Together with the 30 mutually pair-distinct P words, the six selected words give 36 words with injective projections to every coordinate pair. Every projection must therefore be bijective, producing a pair of orthogonal Latin squares of order six. Tarry's no-OLS(6) theorem gives the contradiction. Hence N=42 is impossible.

## 6. Excluding support 43

If N=43, the prerequisite `t≤30` and `N≥72−t` imply t is 29 or 30. For t=30, the residual 6×6 unitary has `|E|=13=2n+1` nonzeros, excluded by the lemma in §2. For t=29, the residual 7×7 unitary has `|E|=14=2n` nonzeros; the lemma requires n even, contradiction. Since the prerequisite candidate already gives N≥42 and §5 rules out 42, no N≤43 can occur. This proves the candidate bound (1), conditional on the dependency and independent review.

## 7. Exact finite controls, not premises

`frontier-20261028-six-residual-support-controls-v1.py`, SHA-256 `535a9f85b8e389f412ed44455982af723813c9028a3fbe9949629e4b5ab20dd0`, enumerates the `8³=512` canonical balanced fiber combinations in each residual alphabet case. Receipt `frontier-20261028-six-residual-support-controls-v1.json`, SHA-256 `35d51dd2fc7b3965df30c3a8972191aa8d0f45a6934ac95aeb459be6a972f62b`, finds no all-ternary support with all pair projections 6; in the one-binary case it finds four, all B-fibered, with three odd-cycle graphs and one bipartite graph. The written completion argument covers **all** bipartite graphs, not merely that finite example.

`frontier-20261028-unitary-one-excess-controls-v1.py`, SHA-256 `ab2a08d06b5a267503a8779c46888d5789bea70f36800157598796a0ebb09c7d`, enumerates all support patterns for n=2,3,4 under the necessary no-unique-row-intersection rule and finds no `2n+1` pattern and no odd-size `2n` pattern. It also checks an exact 3×3 unitary with **eight** nonzeros, preventing the false stronger claim that an odd residual must have at least `2n+3`. Receipt `frontier-20261028-unitary-one-excess-controls-v1.json`, SHA-256 `c79d6b6ea68f5b38592a091bdccfe6c88484526197acf79c8d2b9f62fb781813`.

The controls are exact and same-harness; neither the finite normal-form enumeration nor an unreviewed prior adoption is used as a substitute for the written proof. The original global minimum remains unknown beyond the candidate lower bound and published 60-term witness.
