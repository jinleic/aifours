# Candidate global AME(4,6) support lower bound 45: the eight-row residual

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:04:26 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently accepted, formally verified, or novelty-cleared. It depends on the exact residual construction, t≤30 proof and named no-OLS(6) import in `frontier-20261028-global-ame46-lower42-review-packet-v2.md`, SHA-256 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`; on the exclusion of 42 and one-excess lemma in `frontier-20261028-global-ame46-support-lower44-v1.md`, SHA-256 `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30`; and on the sharp even-size two-excess lemma `frontier-20261028-unitary-two-excess-classification-v1.md`, SHA-256 `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0`. All dependencies remain subject to independent review.

## 1. Claim and reduction

Every complex AME(4,6) state in every product basis has at least **45** nonzero coefficients. The published 60-term witness would then give `45≤m≤60`. [Pandya arXiv:2610.16673v1 §VI](https://arxiv.org/html/2610.16673#S6) reports lower bound 38; this is a comparison with that source, not a priority or novelty conclusion.

As in the dependencies, let P be the t coefficients of modulus 1/6 and E the remaining support. Every 2|2 flattening `6ψ` is unitary, P occupies t singleton rows and columns, and the residual `n=36−t` square unitary has no singleton row or column. For **every** coordinate pair, E has n distinct projected pairs, each with at least two E extensions. The dependencies claim `t≤30` and `N≥72−t`; in particular N≤43 is excluded there.

If N=44 then t is 28, 29, or 30. If t=29, `n=7` and `|E|=15=2n+1`, impossible by the one-excess lemma. If t=30, `n=6` and `|E|=14=2n+2`, impossible for even n by the sharp two-excess lemma. The only remaining case is

`t=28`, `n=8`, `|E|=16`.                                           (1)

Every pair projection has exactly eight values, **each with exactly two E extensions**. We exclude (1) below without computer enumeration as a premise.

## 2. Alphabet and balanced-fiber facts

The incidence lemma in the 42-packet gives `r_i≤floor(3n/5)=4` for the number of residual values of any coordinate. No coordinate is constant, since its pair projection would have at most four values, not eight. A size-2 coordinate cannot be paired with a size-2 or size-3 coordinate, whose product has size at most six. Hence if any coordinate has size 2, the other three have size 4; otherwise every coordinate has size 3 or 4.

Fix a size-4 coordinate A. Each A-fiber varies in at least two of the other coordinates. For any varying coordinate, each occurring pair with A has exactly two E extensions, so the fiber has at least four entries. Four such fibers contain the entire 16-point E, so each has exactly four entries. For each of the other coordinates, each A-fiber uses exactly two values, each appearing twice. For a pair j,k of those three coordinates, the 2×2 frequency table in one fiber has row and column sums two. Its projection is either **full**, four distinct pairs each occurring once, or **correlated**, two pairs each occurring twice. In the correlated case the third coordinate is free over its two fiber values. A four-point balanced fiber is correlated on at most one of its three coordinate pairs: two correlations would make the entire triple a function of one binary coordinate and give at most two points.

For a size-4 coordinate j, each of its four fibers also has size four; hence the incidence graph `π_Aj(E)` is 2-regular on 4+4 vertices. It is either one 8-cycle or two copies of `K_2,2`. Its four row sets are 2-subsets, and no row set occurs three times. In the two-`K_2,2` case, equal row sets partition the A-fibers into two pairs.

## 3. A fiberwise-free coordinate would complete the forbidden classical array

We first use residual unitarity, not merely its support. Suppose for one pair j,k every A-fiber is correlated. Then the remaining coordinate B is free over two values in each fiber and

`E = ⋃_{s∈S} {s}×B_s`,

where S has eight triples on A,j,k and each `B_s` is a two-element set. Every pair projection among A,j,k has size eight, so each is injective on S.

Join two vertices s,s′ when they share one of A,j,k. If they share coordinate j, look at the cut with row indices `(j,B)` and column indices `(A,k)`. Pair-injectivity of S means the two corresponding columns are supported on exactly the B-sets `B_s,B_s′`, with all those entries nonzero. Column orthogonality forbids an intersection of size one. Thus along every graph edge the two 2-sets are equal or disjoint.

For an edge with equal set `{b_0,b_1}`, put `r_s=u_{s,b_0}/u_{s,b_1}` using the residual-unitary coefficients. Orthogonality gives `r_{s′}=−1/conjugate(r_s)`. This fixed-point-free involution forbids odd cycles in the graph of equal-set edges; each of its components is bipartite and has one common B-set. Choose b_0 or b_1 according to a 2-coloring in each component. An edge between different sets has disjoint B-sets, so its choices are automatically different. The eight selected words therefore share no two coordinates with one another. They also share no coordinate pair with any of the 28 maximal P words, because those P pair rows are singletons.

The resulting 36 pair-injective words form an orthogonal array OA(36,4,6,2), hence a pair of orthogonal Latin squares of order six, contradicting the named no-OLS(6) theorem. Therefore **each** of the three coordinate pairs j,k must be full in at least one A-fiber.

## 4. Rectangle-parity lemmas over F₂

For a pair j,k and a fiber g let `u_g,v_g` be the indicator vectors of the two local two-sets. Because every global projected pair has multiplicity two, correlated fibers contribute even multiplicities, and the full fibers F obey

`Σ_{g∈F} u_g v_g^T = 0` over F₂.                                (2)

The 2-sets below are nonzero vectors, and neither relevant incidence graph has three identical row sets. For the size-3 graph considered later the row-set multiset is `{H,H,L_1,L_2}`, where H omits the low symbol and L_1,L_2 are the other two 2-subsets; for size 4 it is 2-regular.

First, |F| cannot be 1. It cannot be 3 either: if a sum of three nonzero rank-one tensors vanishes, two of their left vectors or two of their right vectors must coincide (otherwise the sum of the first two has rank two). Equality then forces the third vector on that same side to coincide as well, contradicting the absence of triple-identical row sets. If |F|=2, the two rank-one tensors are equal, so **both** left row sets and **both** right row sets coincide on those two fibers.

For two size-4 incidence graphs, a nonempty F is therefore of size 2 or 4. In the size-2 case both graphs split into two `K_2,2` components with the same A-fiber partition. In the size-4 case let U,V be the 4×4 incidence matrices. An 8-cycle has F₂ rank 3 and two `K_2,2` components have rank 2. Equation (2) is `U^T V=0`; the elementary rank inequality implies both ranks are 2. The kernel of U^T is spanned by the indicators of its two A-fiber pairs. Every column of V has weight two and lies in that kernel, so V has exactly the same two-pair partition. Thus:

**(R44)** Any nonempty full-fiber set for a 4/4 pair makes both size-4 incidence graphs split with the same A-fiber partition.

For a size-3 graph with degrees `(2,3,3)`, order fibers so its unique duplicate row-set pair is `P={0,1}` and its low symbol occurs in fibers 2,3. Its rows are `(0,1,1),(0,1,1),(1,1,0),(1,0,1)`. The F₂ kernel of its transpose is `{0000,1100,1011,0111}`; its only weight-two vector is the indicator of P. For a 3/4 pair, |F|=4 would require every weight-two column of the 4-graph to equal P, leaving other A rows empty, impossible. A nonempty F must therefore be the two duplicate fibers P, and the 4-graph splits as P and its complement.

**(R34)** For a 3/4 pair, the nonempty full-fiber set is exactly the duplicate row-set pair of the size-3 graph, and the size-4 graph splits along that pair and its complement.

## 5. Three grouped qubits need a purifier of dimension at least four

We use the following self-contained shadow bound. If a three-qubit density matrix ρ has every two-qubit marginal `I_4/4`, then its Pauli expansion has only the identity and weight-3 terms. Spin flip sends the weight-3 terms to their negatives, so

`ρ̃=Y^{⊗3}\barρ Y^{⊗3}=I_8/4−ρ ≥ 0`.

Thus every eigenvalue of ρ is at most 1/4, and `Tr ρ=1` implies `rank ρ≥4`. A pure state whose fourth subsystem has dimension at most 3 cannot purify such a ρ.

Suppose a partition of the A-fibers into two pairs simultaneously partitions the values of two other coordinates C,D into disjoint two-sets, one for each A-fiber pair. Each group contains eight E entries. For any pair among A,C,D, a pair row of the full residual unitary belongs to only one group. The group has `8/2=4` such rows, which are all four pairs of its two local binary alphabets. Those rows remain orthonormal inside the group. After normalizing the group state (its squared norm is `4/36`), its three two-qubit marginals on A,C,D are `I_4/4`. If its fourth coordinate has at most three values, the shadow bound gives a contradiction.

## 6. Zero, one, or a size-2 residual alphabet

If all four residual alphabets have size 4, choose A of size 4. By §3 every pair among the other three has nonempty F. By (R44), the three size-4 incidence graphs all split with the same A-fiber partition. Each group then has two values at **every** party. The shadow bound of §5 applies with a two-dimensional fourth subsystem.

If the alphabet sizes are `(2,4,4,4)` or `(3,4,4,4)`, choose A and C,D of size 4, with B the size-2 or size-3 coordinate. The C,D pair has nonempty F by §3; (R44) groups A,C,D as in §5. The fourth subsystem B has dimension at most 3, so the same shadow contradiction applies.

## 7. Exactly two size-3 alphabets

Let A,D have size 4 and B,C size 3. For each size-3 coordinate, its fiber sizes are `(4,6,6)`: the pair projection to the other size-3 coordinate is a 3×3 graph with eight edges, hence all pairs except one. The symbol on the missing edge is the **low** symbol (degree 2); the two high symbols have degree 3. Let P_B be the two A-fibers where B's two-set is the repeated high/high set, equivalently where B's low symbol is absent; define P_C analogously.

By §3 the full-fiber sets for BD and CD are nonempty. By (R34), they are exactly P_B and P_C respectively, and the size-4 D graph splits along each pair and its complement. Therefore P_C is either P_B or its complement.

If `P_C=P_B`, equation (2) for BC cannot have |F|=4: the low-C column of its incidence matrix has membership vector `complement(P_B)`, but the only weight-two vector in the transpose kernel of the B incidence matrix is `P_B`. Nonempty F must have size 2, and equal rectangles force it to be P_B. Thus every fiber outside P_B is correlated on BC, BD and CD, contradicting the at-most-one-correlation fact of §2.

If `P_C` is the complement of P_B, |F_BC|=2 is impossible because the unique duplicate row-set pairs of B and C are different. Section 4 excludes sizes 1 and 3, and §3 excludes zero; thus BC is full in all four fibers. In an A fiber in P_B, CD is correlated and B is free over its two high symbols; C uses its low symbol and one high. In an A fiber in P_C, BD is correlated and C is free over its two high symbols; B uses its low symbol and one high.

In the AD|BC flattening, choose a row from the first type with fixed **high C**, and a row from the second type with fixed **high B**. The first row has exactly the two BC columns obtained by varying B over its two highs at that fixed C. The second has exactly the two columns obtained by varying C over its two highs at that fixed B. Their supports intersect in **exactly one** BC column, contradicting row orthogonality. Hence this alphabet case is impossible.

## 8. Three or four size-3 alphabets

If at least two coordinates have size 3, their pair projection is a 3×3 graph with eight edges: all pairs except `(low,low)`. The low symbol occurs in four E entries and each high symbol in six. In P, therefore, each low symbol occurs `6−2=4` times and each high symbol `6−3=3` times. A P word containing a high symbol at one size-3 party cannot contain **any** residual-alphabet symbol at a second size-3 party, since all those pair combinations occur in E and a maximal P coefficient exhausts its pair row.

With four size-3 coordinates, the two high symbols at each party account for six distinct P words, 24 in all, none containing another active symbol. The remaining four P words must supply all four occurrences of the low symbol at each party. Hence every one of those four words would have the low symbol at every party, making them identical. Contradiction.

With exactly three size-3 coordinates and one size-4 coordinate D, the high symbols account for 18 distinct P words. For each high symbol, exactly one of its three P words has D in its residual alphabet: among four active D values, three are paired with that high symbol in E. Thus these 18 words contain exactly six active-D occurrences. Each of the four D symbols occurs `6−2=4` times in P, so there are 16 active-D occurrences in all. The ten remaining non-high P words must therefore **all** have D active. But any low symbol of a size-3 coordinate occurs four times in P, only among those non-high words, and only `4−2=2` active-D values can pair with it outside E. Pair-injectivity allows at most two such words, contradiction.

All possible residual-alphabet patterns have been excluded. Therefore N=44 is impossible and, together with the pinned lower-44 dependency, the candidate bound N≥45 follows.

## 9. Exact controls and scope

`frontier-20261028-eight-residual-rectangle-parity-v1.py`, SHA-256 `e8fd4a05b0305fe399b39230c965cffb9110d68701346d258b34b8a5525950ee`; receipt `frontier-20261028-eight-residual-rectangle-parity-v1.json`, SHA-256 `78fb02b43d535fb1228c3e940b5c45afabb49278c2aeb0816ff1bd9fa4886494`, checks all 90 size-4 and 12 `(2,3,3)` incidence graphs and all nonempty full-fiber masks. It records the 4/4, 3/4 and 3/3 parity classifications used above.

Independently, `frontier-20261028-eight-residual-mixed-direct-v1.py`, SHA-256 `77cb2b5ebaca90b43c06f996a1d4279be19130d4a2751d89808bc21d73741a82`; receipt SHA-256 `3c7e09fc9bfcb4dd20d5c8149feddad2a5722893c58117a69f0d02d8fa320cc2`, constructs mixed-case supports by direct pair counting rather than XOR masks. It finds 144 parity normal forms and 576 with all pair projections of size eight and multiplicity two; all 576 have the AD|BC unique-row-overlap obstruction, with one explicit witness in the receipt.

`frontier-20261028-three-qubit-shadow-control-v1.py`, SHA-256 `9ed98305b8ad05ce15642dc05da8a3024a7d352929bdb53b4f062b7feee72017`; receipt SHA-256 `2db5eeabadae4bcee850cd0078622e49777bfadeb4a2f478c3ac8940bb685f96`, checks an exact rank-4 three-qubit 2-uniform mixed-state example and the spin-flip identity, and rejects a rank-3 deletion mutation. This shows the rank-four lower bound is sharp; it is not a formal proof of the universal statement.

These are bounded exact controls, not substitutes for independent reconstruction, a formal proof, or a novelty screen. N=45 and the gap to the published 60-term witness remain open in this work.
