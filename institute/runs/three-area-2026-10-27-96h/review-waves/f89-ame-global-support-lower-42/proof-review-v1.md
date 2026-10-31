# Independent same-harness written-proof review: AME(4,6) support

Native `/bin/date` clock observed immediately before exclusive creation: `Wed Oct 28 19:03:44 PDT 2026`. This is an observation before the write, not a claimed completion timestamp.

## Verdicts and limits

- **Global ≥42:** **0 FATAL / 0 MAJOR / 0 MINOR** found in the pinned v2 written argument, **conditional on the explicitly identified Tarry no-OLS(6) theorem**. The quantifier is every normalized complex AME(4,6) state and every local product basis. This is an independent same-harness written reconstruction, not a formal proof, a human review, or an external-family review.
- **Global ≥44:** **0 FATAL / 0 MAJOR / 0 MINOR** found in the pinned successor, with the same Tarry condition and depending on the preceding ≥42 argument. The exclusions at N=42 and N=43 have been separately reconstructed below.
- These findings do **not** establish novelty, priority, a 42-, 43-, or 44-term example, the exact minimum, independent acceptance, or an unconditional proof of the external classical import. The 38/60 numbers are comparative published statements, not premises of either lower-bound proof.

References below use **P** for `frontier-20261028-global-ame46-lower42-review-packet-v2.md` and **S** for `frontier-20261028-global-ame46-support-lower44-v1.md`; line numbers refer to the pinned complete files, not excerpts or author controls.

## Input identity and review method

Read `manifest-v2.json` first (SHA-256 `354f4562acbeb9b774ba0f0785f0bcbbfd6191b6332b6359c59de336595594d8`). Before reaching a verdict, checked the SHA-256, byte count, and LF count of **all 14** declared inputs, and read each whole input in manifest order using exact raw windows. All matched the manifest:

| # | Manifest role | SHA-256 |
|---:|---|---|
| 1 | public table transcription | `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` |
| 2 | ≥42 candidate v1 history | `956dbda5fa0b0c3b932bf7988ef7d6b537cc546ba840c1f9b80a3c0aa95251a8` |
| 3 | ≥42 binding packet P | `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` |
| 4 | ≥44 successor S | `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30` |
| 5 | XOR author code | `ed1624509435de960f40816de5f8e4a9dbd37fd46d14125402323b0133f76ce4` |
| 6 | XOR author receipt | `a3787da565a2d45757857deddf654f387b6616704ae0aa2ac1ef29dd9c8b7570` |
| 7 | n=5 author code | `b3430b4b49d9660715976fdb7bb1467253767a821d09e40132057b7c108d7180` |
| 8 | n=5 author receipt | `3e86e8f7164d4a8986199124e78c7f86f872b99e6dcf157a7332d744362c856f` |
| 9 | graph author code | `0364d35d908e44db9e061c9bdd24044a6a3006838bb30a64a3c8382c16fbaecc` |
| 10 | graph author receipt | `8de5dd28dc01f80564e6ba16256f5fe1270e448b265a0903c5d4527b38150401` |
| 11 | n=6 author code | `535a9f85b8e389f412ed44455982af723813c9028a3fbe9949629e4b5ab20dd0` |
| 12 | n=6 author receipt | `35d51dd2fc7b3965df30c3a8972191aa8d0f45a6934ac95aeb459be6a972f62b` |
| 13 | support author code | `ab2a08d06b5a267503a8779c46888d5789bea70f36800157598796a0ebb09c7d` |
| 14 | support author receipt | `c79d6b6ea68f5b38592a091bdccfe6c88484526197acf79c8d2b9f62fb781813` |

Hashes establish identity, not correctness. Author controls were read for scope and not used as proof. The arguments and separately written local controls below are the basis of this review.

## ≥42: reconstructed proof and line-level disposition

### Saturation, all six projections, and the global count — P:11–27

Fix **any** normalized complex AME(4,6) state and **any** product basis. For every bipartition ij|kl, the matrix U=6ψ with rows ij and columns kl obeys UU†=I; it is square and therefore unitary. Hence all rows and columns of ψ have squared norm 1/36. If a coefficient has modulus 1/6, its contribution exhausts **both** norms in **every** cut. All other entries in each such row and column vanish. Conversely any singleton row or column has a unique entry of modulus 1/6. Thus distinct maximal positions cannot agree on any coordinate pair.

Let P be **all** maximal positions, t=|P|, and E all the remaining nonzero positions, n=36−t. In each cut, after row and column permutations U is the direct sum of t scalar unitary blocks and an n×n unitary. The remaining rows and columns have at least one entry; if one had precisely one, that entry would itself be maximal and its row or column would have been removed. Therefore, **for every one of the six pairs ij and every pair value in π_ij(E)**, that value has at least two distinct extensions in E, and |π_ij(E)|=n. The pair not present in the residual projection is not claimed to have two extensions. For any fixed cut, |E| is the sum of n residual row degrees, so N=t+|E|≥t+2n=72−t.

For n=0, the 36 words P project bijectively onto every coordinate pair. Taking the first two as the cell coordinates, the third and fourth form an orthogonal pair of Latin squares of order six. This contradicts the **unverified here** Tarry import. For n=1, the residual 1×1 unitary is a singleton already belonging to P, contradiction. These are exhaustive including the corner t=36.

### Fiber incidence — P:29–43

For **each** coordinate i let r=|π_i(E)|, and let E_v be a nonempty i-fiber. Its other-coordinate supports cannot vary in zero or one position: in either case fixing i and one suitable other position uniquely determines a word, contradicting the above ≥2-extension statement. Thus each fiber contributes at least two incidences (fiber, varying coordinate).

For **each** j≠i, disjointness by the i-value gives `Σ_v (|π_j(E_v)|−1)=|π_ij(E)|−r=n−r`; the number of fibers varying in j is no greater than that sum. Counting the same incidences above and below yields `2r≤Σ_{j≠i}(n−r)=3(n−r)`, so r≤floor(3n/5). For n=2 or 3 this holds with r≤1 for **all four** coordinates, whereas each pair projection must have size n>1. Both cases are impossible. No phase or unproved cardinality assumption is used.

### n=4 and the Pauli spin-flip contradiction — P:45–63

The incidence bound gives each local residual alphabet size ≤2. If one were constant, its pair projection with any other coordinate would have at most 2 values, not 4. Therefore all four alphabets have size 2; every pair projection is the whole 2×2 alphabet. In **each of the three cuts**, the surviving four rows and four columns are exactly these binary pairs, and the entire residual 4×4 matrix is unitary. Restrict ψ to E, obtaining ψ_E of squared norm 4/36. The normalized binary state φ=3ψ_E has each cut matrix equal to the corresponding residual U-block divided by 2, so all six two-qubit reductions are I₄/4. There is no unproved identification of just one flattening with all three.

For a hypothetical such four-qubit pure state write `ρ=2^−4 Σ_P r_P P` in the 4-qubit Pauli basis. Two-uniformity forces r_P=0 for weights 1 and 2; r_I=1 and orthogonality of Pauli matrices with Tr(ρ²)=1 gives Σ r_P²=16. For **each** triple T, Schmidt equality of complementary marginal purities and the maximally mixed one-qubit complement imply Tr(ρ_T²)=1/2. Expanding ρ_T gives `(1+Σ_{supp P=T}r_P²)/8=1/2`, so each triple contributes 3, total weight-3 sum 12. The remaining weight-4 sum is 16−1−12=3. The positive semidefinite spin flip `ρ̃=Y^⊗4 conjugate(ρ) Y^⊗4` sends each Pauli word of weight w to (−1)^w times itself. Orthogonality therefore yields `Tr(ρρ̃)=(1−12+3)/16=−1/2`, contradicting nonnegativity of the trace of the product of positive semidefinite matrices. This proves the needed AME(4,2) nonexistence in the packet; it is **not** an additional external import.

### n=5 normal form and Boolean parity — P:65–89

Every coordinate has at most three values; at least one has three since otherwise a two-coordinate projection has ≤4 values. Fix such an i with r=3. The incidence count has lower and upper bounds both equal to six. Equality therefore forces each i-fiber to vary in exactly two other coordinates, each other coordinate to vary in exactly two fibers, and each variation to use exactly two values (the sum of excesses in each coordinate is exactly two). The fixed-coordinate/fiber relation is a bijection: label the three other coordinates j=0,1,2 and the fibers so that fiber j fixes j.

**For every fiber**, its other two coordinates have two values apiece. Fix i and one of those varying values. At least two E extensions are required, and the fixed coordinate and the other binary coordinate leave only two possible extensions. Both must occur. Thus every fiber is exactly its full four-word 2×2 product.

For each j define e_j to be 1 exactly when j's two binary value sets in the other two fibers agree. Fix any distinct j,k, let l be the third coordinate, and project to j,k. Fiber l supplies a four-point rectangle. Fiber j and fiber k supply edges. If either fixed singleton lies outside the corresponding base binary set, its edge alone adds two outside points, making ≥6; a five-point projection hence forces both singletons inside. Each differing two-set then adds exactly one point, while an equal set adds none. The two possible added points lie respectively inside/outside and outside/inside the rectangle, so they cannot coincide. Consequently, under the singleton membership already forced by size five, `|π_jk(E)|=4+(1−e_j)+(1−e_k)`. Size five implies e_j≠e_k. This must hold for **all three** pairs among three Boolean flags, impossible. In particular, OR is not enough: the proof requires XOR.

### Final ≥42 case split — P:91–97

The exclusions are n=0 (Tarry), n=1 (singleton), n=2,3 (incidence), n=4 (Pauli contradiction), n=5 (parity). Thus n≥6, t≤30, and N≥72−t≥42. No case of a fixed basis, selected support orbit, or a supposed 42-term construction is substituted for the global assertion.

## ≥44: reconstructed proof and line-level disposition

### Unitary-support facts, including 2n+2 — S:15–25

For **every** n×n complex unitary with no singleton row or column, two distinct rows sharing a nonzero column must share a second: otherwise their inner product has a single nonzero summand. The same holds for columns. There are at least 2n entries.

If there are 2n, every row and column has degree two. Its bipartite support graph is a union of even cycles. A cycle longer than four has two rows sharing exactly one column; hence every component is a full 2×2 block and n is even. If there are 2n+1, exactly one row has degree three and all others degree two. Every row meeting the exceptional row must use two of its three columns. Distinct 2-subsets of those three meet once, so all such rows use the same pair, leaving the third exceptional column with no other nonzero; contradiction. Thus 2n+1 is impossible, and in particular an odd-size matrix has **at least 2n+2** entries. These are the universal facts actually used in S; 2n+2 is a lower bound in the odd case, not a blanket claim of attainability for every n.

An additional independent check of the 2n+2 edge case: in fact such a unitary can exist only for odd n and its support is a direct sum of one 3×3 eight-entry support and 2×2 blocks. To see this, two degree-two rows with the same two-column support form an orthonormal basis of that two-dimensional column space, so every other row is zero there; delete the resulting isolated 2×2 block. After deleting all such blocks, the supports of distinct degree-two rows are disjoint. With 2n+2 entries, either one row has degree four and all others degree two, or two rows have degree three and all others degree two. In the remaining m×m unitary, the first case has 2(m−1)≤m, impossible since the degree-four row needs m≥4. In the second, 2(m−2)≤m and m≥3, hence m=3 or 4. At m=4 the two degree-two supports partition the columns; each degree-three row meets each such support in 0 or 2 columns, so would have even degree, contradiction. At m=3 the two degree-three rows are full and the third has degree two, giving the stated eight-entry support. For example

`[[1/√2, 1/√2, 0], [1/2, −1/2, 1/√2], [1/2, −1/2, −1/√2]]`

is real orthogonal with eight nonzeros; direct-summing 2×2 Hadamard blocks realizes the classification for every odd n≥3. This extra observation is not needed for the claimed ≥44 result and is not attributed as a lemma of S.

### N=42: exact six-fiber alternatives — S:27–47

Given the ≥42 dependency, N=42 forces t=30, n=6 and |E|=12. In **each** residual cut every one of the six rows and columns has degree exactly two, so every value of **each** pair projection has exactly two E extensions. The incidence bound puts each residual alphabet size in {2,3}: size 1 would make its pair projection ≤3. Two size-2 coordinates are impossible because their pair projection has ≤4 rather than 6 values. Hence the only patterns are (3,3,3,3) and, up to permutation, (3,2,3,3).

Fix any ternary coordinate A. Each of its fibers varies in at least two other coordinates; selecting one varying coordinate, its two distinct A-pairs each have exactly two E extensions, so the fiber has ≥4 words. All three fibers sum to 12, so each has exactly four. For **every** other coordinate j in **each** A-fiber, the four words partition into A,j pair fibers of exactly two, hence j assumes exactly two values, each twice. When j is ternary its own fibers also have size four, so π_Aj is a 3×3 bipartite graph with degree two on both sides, namely the complement of a matching. Relabel the j values independently so its missing value in A=g is g.

Within a four-word fiber, every pair of the other coordinates has a 2×2 table with each row and column sum two. It is either four distinct pairs or two perfectly correlated pairs occurring twice. A fiber cannot be correlated on two different coordinate pairs: two such binary functional relations make all three other coordinates functions of one bit, allowing at most two distinct words instead of four.

If all four coordinates are ternary, for any other pair j,k, the four possible pairs in A=g lie in the square `(3\{g})²`. Two different such squares intersect in exactly one point, so two full fibers would yield seven pair values, exceeding the required six. Thus each of the three pairs needs at least two correlated fibers, at least six fiber/pair incidences, but the three fibers supply at most three. The all-ternary case is impossible.

### N=42: binary case, complex orthogonality, and OLS completion — S:49–67

Suppose B is binary and A,C,D ternary. The same square argument forces at least two A-fibers to be correlated in C,D. In each, both B values occur for each of its two C,D pairs; each pair therefore already uses its exactly two allowed extensions. Different correlated fibers have disjoint C,D pair sets. A full third fiber could share none of those four saturated pairs and would add four more, giving ≥8 rather than six; it too is correlated. Consequently `E=S×{b₀,b₁}` for six triples S on A,C,D. Each A,C,D value occurs twice in S, and every two-coordinate projection of S is injective: two S triples with a common pair would give four E extensions of that pair.

Join two triples when they agree on one of A,C,D; they cannot agree on two. For each edge s—s′, take the cut whose rows are B and that common coordinate. The columns are the other two coordinates; injectivity of the appropriate S-pair means each of these columns is supported exactly on the two rows with B=b₀,b₁ at the shared coordinate. The two columns of the unitary are orthogonal. With nonzero coefficients `u_{s,0},u_{s,1}` and ratio `r_s=u_{s,0}/u_{s,1}`, this gives `conjugate(r_s) r_s′=−1`, or `r_s′=−1/conjugate(r_s)`. This map is an involution without nonzero fixed points, so an odd cycle is impossible and the graph is bipartite. A 2-coloring selects one B value for each s such that the resulting six words are distinct on all coordinate pairs: pairs among A,C,D are already injective, and equality in one such coordinate gives an edge and opposite B colors.

No selected word can share any coordinate pair with a maximal P word: each selected word was already a nonzero E position in the saturated row or column. Thus the six selected words plus 30 P words are 36 pairwise pair-distinct words. Each projection to a coordinate pair is an injection into a 36-element set, hence a bijection. The first two coordinates define the cells and the other two define two orthogonal Latin squares of order six, contradicting the named Tarry import. This checks the complex conjugation and the full completion, not just an odd-cycle support test.

### N=43 and final conclusion — S:69–71

For N=43, t≤30 and N≥72−t leave only t=30 or 29. If t=30, n=6 and |E|=13=2n+1, impossible by the unitary-support lemma. If t=29, n=7 and |E|=14=2n, impossible because the 2n lemma requires n even. Together with N≥42 and the N=42 contradiction, this yields N≥44, conditional on the dependency and Tarry. No case at N<42 is silently omitted.

## Independently written exact controls

Created `proof-review-v1-check.py` exclusively in this review directory; SHA-256 `59a84796446654bb1297171b637846e58c1f36b70d95bd2e7dacb0f9a6927234`. Ran `python3 -B proof-review-v1-check.py`. It imports no author checker. The following are observed results, not substitutes for the written arguments or proofs that every graph survivor has unitary amplitudes.

- **n=5:** independently built 19,683 full three-fiber supports; zero have projection sizes (5,5,5); 648 have (5,5,6), a nonempty relaxed control. Over all constructed pair projections, the membership-plus-XOR equivalence had zero discrepancies. Coverage relies on the separately established incidence normal form.
- **n=6:** in each of the all-ternary and one-binary canonical cases, independently generated the 8 balanced four-point subsets in each of three fibers, for 512 supports per case. The all-ternary case had zero supports with every pair projection of size six. The binary case had four, all with every pair multiplicity exactly two and all binary-fibered; their graphs comprised three odd-cycle and one bipartite cases. Relabeling completeness and the graph-to-OLS implication are established in the written argument above, not by the enumeration alone.
- **n=4 and n=6 unitary-support controls:** enumerated multisets of row masks for totals 2n, 2n+1, and 2n+2, weighting by the exact number of row labelings; filtered by minimum column degree two and the necessary no-unique-overlap condition for both rows and columns. Results are as follows. "Survivors" are necessary graph patterns only; no complex amplitudes were solved for.

| n | nnz | labeled patterns counted | necessary graph survivors | non-block survivors at 2n |
|---:|---:|---:|---:|---:|
| 4 | 8 | 1,296 | 18 | 0 |
| 4 | 9 | 3,456 | 0 | — |
| 4 | 10 | 4,320 | 0 | — |
| 6 | 12 | 11,390,625 | 1,350 | 0 |
| 6 | 13 | 91,125,000 | 0 | — |
| 6 | 14 | 372,093,750 | 0 | — |

These are same-harness finite controls. They do not by themselves prove the universal support lemmas or validate the no-OLS theorem, nor do they constitute independent model-family or formal verification.

## Explicit imports and statements not established

1. **Tarry/no-OLS(6): unverified mathematical import.** I independently checked the reductions from 36 pair-distinct words to orthogonal Latin squares in both uses. I did not reconstruct Tarry's theorem or check an independently certified exhaustive proof. [Pandya arXiv:2610.16673v1, Introduction](https://arxiv.org/html/2610.16673v1) states the classical no-pair result and cites Tarry; this is corroboration of the source statement, not a verification of Tarry's proof.
2. **AME(4,2) nonexistence: not an unverified import.** The specific fact needed here is proved by the self-contained purity and Pauli spin-flip reconstruction above, conditional only on elementary linear algebra; no external AME(4,2) theorem is assumed.
3. **Published comparison, not a premise:** the cited [Pandya §VI](https://arxiv.org/html/2610.16673v1#S6) states the 38 lower bound; its abstract and §II state a 60-support AME example. I read these claims but did not independently certify the 60-term tensor or all underlying published arguments in this review. Neither number proves the candidate bound.
4. **Not established:** novelty or priority, an attained minimum or a 44-term witness, a formal proof, a cross-model-family or human verdict, or authority to publish or adopt either claim. The assessment is limited to the exact pinned global statements above and the explicitly identified imported theorem.
