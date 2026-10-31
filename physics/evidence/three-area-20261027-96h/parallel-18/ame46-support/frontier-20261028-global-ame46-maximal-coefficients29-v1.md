# Candidate: at most 29 maximal coefficients in any AME(4,6)

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:17:24 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, unreviewed and not adopted. It uses the residual and incidence lemmas and t≤30 result in `frontier-20261028-global-ame46-lower42-review-packet-v2.md`, SHA-256 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`. Those prerequisites include the named classical no-OLS(6) theorem. No novelty or formal-proof claim is made.

## 1. Claim

In any product basis, a normalized complex AME(4,6) state has at most **29** coefficients of modulus 1/6. Equivalently it cannot have 30 saturated entries. This is a structural statement valid regardless of total support. In the published 60-term example the number is 12; no claim is made here that 29 is attained or sharp.

The proof is source-free and uses arbitrary complex coefficients only through residual unitarity. It also supplies a route to excluding the t=30 cases in low-support analyses without invoking a three-excess unitary classification.

## 2. Residual and active-coordinate counts

For every 2|2 cut, `U=6ψ` is unitary. A maximal coefficient of modulus 1/6 is the only nonzero entry in each row and column that contains it; deleting the t matched singleton rows and columns leaves an `n×n` unitary with `n=36−t` and at least two nonzeros in every residual row and column. Let E be the nonmaximal support and P the t maximal positions. Every coordinate-pair projection of E has exactly n values, each with at least two E extensions, and `|E|≥2n`.

The dependency proves t≤30. Suppose for contradiction that t=30, so n=6. Its incidence lemma implies each residual local alphabet has size at most three; every pair projection has six values, so no local alphabet has size one and no two have size two. The only possibilities are `(3,3,3,3)` and `(2,3,3,3)` up to party order.

For a P word x call a coordinate active if its value lies in the corresponding residual alphabet, and write `k(x)` for the number of active coordinates. P and E partition the 36 values of every coordinate-pair projection: P pair values are injective and exhaust the singleton rows, while E uses the remaining six. If residual alphabet sizes are r_i, then the number of P words active at i is `6r_i−6`, and the number active at both i,j is `r_i r_j−6`. Thus

`Σ_{x∈P}[k(x)−C(k(x),2)] = Σ_i(6r_i−6)−Σ_{i<j}(r_i r_j−6)`.  (1)

The per-word quantity takes values `0,1,1,0,−2` for k=0,1,2,3,4 and is at most 1. If the alphabet sizes were `(2,3,3,3)`, the right side of (1) would be `42−9=33`, larger than |P|=30. Hence all four residual alphabets have size three.

## 3. Every missing pair set is a perfect matching

Fix an active symbol a of party i. Let `m_i(a)` be the number of P words using it. For any other party j, the P words using a have distinct j symbols, since no two P words share a coordinate pair. The six possible j symbols are partitioned into those P pairs and those appearing in E, so the number `d_ij(a)` of residual partner symbols equals `6−m_i(a)` and is independent of j.

The E fiber at i=a varies in at least two other coordinates: if it varied in zero or one, some occurring coordinate pair would have only one E extension. Thus one d_ij(a) is at least two, so **all** are at least two. Summing d_ij(a) over the three active symbols gives n=6; each is exactly two. Therefore every 3×3 E pair projection is 2-regular, and its complement is a perfect matching.

## 4. A three-color four-party forbidden-matching bound

For each coordinate pair, let its missing perfect matching be forbidden. We claim that at most 12 four-tuples can avoid all six matchings.

Relabel the symbols independently at the three parties B,C,D so that the missing matchings from A to each of them are the identity. Fix `A=a`. Each of B,C,D can then use only the two symbols different from a, giving the eight vertices of a 3-dimensional binary cube. Consider a forbidden matching on one of the three interleaf pairs BC,BD,CD.

- If that matching fixes a, it maps the other two symbols onto the other two, so it forbids two of the four possible pairs and eliminates four cube vertices. At most four survive.
- If none of the three interleaf matchings fixes a, each forbids exactly one of its four allowed ordered pairs, so its bad set is a two-vertex edge of the cube, parallel to the coordinate not involved in that pair. The three bad edges are distinct and parallel to three different axes. Three distinct edges in a bipartite cube cannot be covered by only three vertices, because that would form a triangle. Hence they cover at least four vertices, and at most four survive.

Thus at most four tuples survive for each of the three A values: at most 12 overall. E avoids every forbidden matching, so `|E|≤12`. Residual unitarity requires `|E|≥2n=12`; equality holds, and every pair projection value has exactly two E extensions.

## 5. The equality case is impossible

Each A fiber then has exactly four entries. In it, each other coordinate uses the two symbols other than A and each value occurs twice, because every residual pair row has degree two. For a pair j,k among the other three parties, the fiber's pair projection is either a full 2×2 square of four values, or two perfectly correlated values, each occurring twice. A fiber can be perfectly correlated on at most one such pair: two correlations would make the triple a function of one binary coordinate and give at most two distinct entries.

For each j,k the three potential squares, one per A value, omit distinct symbols on both axes and any two intersect in exactly one point. If two fibers were full, their union would contain seven pair values, contradicting `|π_jk(E)|=6`. Thus at least two of the three fibers are correlated for **each** of the three pairs j,k. That requires at least six fiber/pair correlations, but the three fibers supply at most one each. Contradiction.

Hence t=30 is impossible and the dependency's t≤30 improves to the candidate `t≤29`.

## 6. Exact controls and an explicit non-completion

`frontier-20261028-signed-k4-matching-bound-v1.py`, SHA-256 `2e54209c76a277818a702c6c51049119b221d0c666dbfbce1a5b4e7da8ef67b5`, checks all 216 triples of interleaf permutations. Its receipt `frontier-20261028-signed-k4-matching-bound-v1.json`, SHA-256 `a81641c7129f790aef937efb2c914d08f0590b31c693dadfabdde000d6dda65a`, reports maximum four surviving tuples per A fiber and 12 total; dropping one forbidden matching permits 15. It also checks the three-cube-edge observation. This is an exact finite control, not the proof above.

Separately, a Z3 diagnostic found a 30-word P code satisfying the necessary pair-injectivity and active-pattern constraints; it has **no** E support or amplitudes attached. Its SAT receipt `frontier-20261028-n6-maximal-code-z3-v1.json` has SHA-256 `516cba122e2a7fbd252ccf06267e66410ab8e393089e0fe91c4d8b0f5690c083`. A separate standard-library verifier `frontier-20261028-n6-maximal-code-independent-v1.py`, SHA-256 `b3d3d4e1b422f038edcfc6a9b3a9cae07c962ffa623a364b9f3053860a4937ec`, checks all 30 positions, all six pair projections and four intended corruption controls; its receipt has SHA-256 `9c71a81344dc094491cb082b8ba375c626ec76a7010266fac414149f4549a421`. All six active/active P matchings in this particular diagnostic code are the identity. Any E tuple would need four pairwise distinct active symbols from only three symbols, so **no E tuple is compatible** with that code. This is an obstruction to the sampled code only, not an AME witness or a general P-code impossibility.

The exact finite checks do not establish a formal proof, novelty or independent scientific review. The original global minimum remains open beyond whatever lower bound survives review.
