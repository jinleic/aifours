# Support 50: proposed whole-tensor exclusions at t=25 and t=27

**Status: GENERAL AUTHOR, NONBLIND, same harness; proposed written proof, not yet reviewed or adopted.** Native UTC clock actually observed immediately before preparation of these final bytes: **2026-10-31T01:21:35Z**; this is not asserted to be the exact creation time. The claims concern one normalized complex AME(4,6) state in one local orthonormal product basis, with arbitrary phases and moduli. Put `U=6ψ`, let `N` be its support, and let `t` count the entries of `U` of modulus one.

**Proposed exact-branch results.** `N=50,t=25` and `N=50,t=27` are impossible. These two claims use the three unitary flattenings of the *same* complex tensor and, for t=25, all six physical pair systems; neither imports a global t bound, no-OLS, a computer-assisted count, a phase ansatz, or an independently chosen support in each cut. The proofs below reconstruct their necessary facts. Sections 5–6 also give necessary same-tensor per-cut structures for `t=26,28`; they do **not** exclude those branches. The proof, including its permutation and inclusion–exclusion steps, needs an independent complete review.

For global composition, the elementary count gives `t≥22` when `N=50`. **Only if** the separately stated global `t≤28` proposition is imported, with its no-OLS(6), f113 and prior `t≤30` provenance retained, would the two proposed exclusions leave `t∈{22,23,24,26,28}`. This is not a claim that those remaining cases are possible or are all the remaining cases after other work. It is not a support-50 witness, an exclusion of support 50, a 51 lower bound, an exact minimum, a novelty claim, or a stronger assurance claim. The packet's conditional baseline and any lower-bound/upper-witness composition retain their own stated computer-assisted and source-history boundaries.

## 1. Actual tensor, support components, and common degrees

Every two-versus-two flattening of `U` is a 36×36 unitary. A modulus-one entry exhausts its row and column, so its pair value in every one of the six physical pair systems is occupied by exactly that one entry, and no other nonzero entry can share it. Call these entries `P`; call the other nonzeros `E`. In any fixed cut, delete the `t` saturated rows and columns. The remaining square unitary has

    n=36−t rows,  |E|=50−t nonzeros,  excess e=|E|−2n=t−22.

It has no singleton line: a singleton of a unitary row or column has modulus one and would have belonged to `P`. In every physical pair system each of the 36 pair values is therefore either a singleton P value or has at least two E extensions; exactly `n` pair values are of the latter kind. These are statements about the same actual entries in all cuts, not about three separately constructed graphs.

Consider a connected component of the residual row/column support of a cut. Its order `m` is the same on both sides, because its block has both orthonormal rows and orthonormal columns. Distinct rows, or distinct columns, cannot meet in exactly one nonzero position. A size-two component is a full 2×2 block. In a component of order greater than two, the two columns of every degree-two row have identical row neighborhoods, since another row meets both or neither. They have degree at least three: if they had degree two, their two columns would form an isolated unitary 2×2 block. Two degree-two rows have disjoint column neighborhoods, for a single overlap is forbidden and identical neighborhoods again isolate a 2×2 block. Transposition gives the symmetric statements for degree-two columns.

If a component has excess `ec=edges−2m`, at least `m−ec` of its rows have degree two and at most `ec` columns have degree above two. The preceding disjoint twin pairs imply

    m ≤ ec + floor(ec/2)                  (m>2).                 (1)

Thus excess one is impossible; an excess-two component has order three and is 3×3 minus one entry. An excess-three component has order three and is a full 3×3: (1) allows at most order four. At order four there is at least one and at most one degree-two row; both sides have one low line and three degree-three lines. The low row's twin columns meet it and at least two high rows. A remaining high row avoids both twins and would have at most two neighbors, contradicting its degree three. This uses only support consequences of actual unitarity, regardless of phases.

For an E-used symbol `x` at party `i`, let `d_i(x)` be its number of E partner symbols in another party, and let `s_i(x)` be its number of E occurrences. This degree is independent of the other party: `6−d_i(x)` is exactly the number of P words containing `x`. Define `h_i(x)=s_i(x)−2d_i(x)`. For every partner, `h_i(x)` is the sum of E-line multiplicity excesses incident to `x`. Hence

    d_i(x)≥2,     Σ_x d_i(x)=n,     h_i(x)≥0,     Σ_x h_i(x)=e.  (2)

The first inequality holds because degree one would fix all three other coordinates of every E word containing `x`, leaving at most one such word, whereas its E pair line must have at least two extensions.

We will also use the following elementary *actual-slice* lemma. If `d_i(x)=2` and `h_i(x)=1`, its five E words occupy five vertices of a binary three-cube. In each direction the two corresponding actual unitary rows have sizes two and three among four complementary coordinates, so they overlap; since one overlap is forbidden, they overlap in at least two positions. Thus the five vertices induce at least six cube edges. But deleting three vertices removes at least `3·3−2=7` of the cube's 12 edges, since three cube vertices induce at most two edges; the five retained vertices induce at most five. Contradiction. Consequently

    h_i(x)=1  ⇒  d_i(x)≥3.                                    (3)

## 2. Exact t=25: all excess symbols are diffuse

Here `n=11`, `|E|=25`, and `e=3`. Every cut consists of one full 3×3 component and four full 2×2 components. Thus each physical pair system has exactly three *high* E pair values of multiplicity three; its other eight E pair values have multiplicity two. In any cut, the three high row values and three high column values form a complete 3×3 block. In particular, for every E word, its value in a pair is high **iff** its complementary pair value is high; and every combination of the three high pair values on one side with the three on the other is an actual E word.

For each party the nonzero `h` values partition three: `(3)`, `(2,1)`, or `(1,1,1)`. We exclude the first two using the same tensor.

**No `(3)`.** Suppose party A has `h_A(a)=3`. In each of AB, AC, AD the three high pair values form a star centered at `a`; consequently each other party has three distinct high symbols, all of `h=1`, and the high CD graph is a three-edge matching. Write the three high AB values `(a,b_i)` and the high CD values `(c_j,d_j)`. The full AB|CD component contains all nine `(a,b_i,c_j,d_j)`. The three high AC rows `(a,c_j)` consequently have disjoint sets `{(b_i,d_j):i=1,2,3}` of BD neighbors. But in the full AC|BD 3×3 component those three high rows must have the *same* three BD neighbors. Contradiction.

**No `(2,1)`.** First, two such parties A and C cannot coexist. Their high-high graph has three edges and endpoint degrees `(2,1)` on both sides, so the two `h=2` symbols `a,c` must be adjacent. Let B,D be the remaining parties. In AB there are two high values `(a,b_1),(a,b_2)`; in CD there are two high values `(c,d_1),(c,d_2)`. The full AB|CD block then contains four distinct words `(a,b_i,c,d_j)`, all at the high AC pair `(a,c)`, although that pair has multiplicity exactly three.

Thus if A had `(2,1)`, each of B,C,D would have `(1,1,1)`. Let `a` be A's `h=2` symbol, let `(a,b_1),(a,b_2)` and `(a,c_1),(a,c_2)` be its high AB and AC values, and let the high CD matching send `c_j` to `d_j`. The `d_j` are distinct. The AB|CD block contains `(a,b_i,c_j,d_j)` for both `i,j=1,2`. Hence the two high AC rows `(a,c_1)` and `(a,c_2)` have at least four distinct BD neighbors together. They must instead share the same three neighbors in AC|BD. Contradiction.

Accordingly each party has three distinct `h=1` symbols, called **high symbols**, and every other E-used symbol is **low**. By (2)–(3), `q_i`, the E alphabet size, is at most four: the three high degrees are at least three and each additional degree is at least two. It is at least three. Two size-three parties cannot coexist since their pair has 11 E values but only nine cells. If one size-three party exists, the profile is `3444`; this is impossible by the following P moments, which use one common P set.

For a P word let `k` be its number of coordinates in the respective E alphabets, and let `n_k` count such words. Each party contributes `6q_i−11` such P incidences, and each pair of E alphabets has `q_i q_j−11` P cells. For `3444`,

    Σ n_k=25,   Σ k n_k=6·15−44=46,
    Σ binom(k,2)n_k=84−66=18,
    n_0+n_3+3n_4 = 25−46+18 = −3,

an impossibility. Thus `q_i=4` for all four parties. Equation (2) now forces each high symbol to have `d=3,s=7`, and the unique low symbol to have `d=2,s=4`. In every pair system the three high pair values form a bijective matching between its two three-symbol high alphabets.

## 3. Exact t=25: matchings, both permutation classes, and contradiction

Relabel each party's three high symbols so that the high matchings AB, AC, AD are equality on `{0,1,2}`. Write the remaining bijections as `β: B→C`, `γ: B→D`, and `δ: C→D`. The full AB|CD block contains

    (a,b,c,d)=(x,x,y,δ(y))              for all x,y.

For an actual E word, a pair is high iff its complementary pair is high. Applying this to AC versus BD gives `γ=δ`; applying it to AD versus BC gives `β=δ⁻¹`. The full AC|BD block contains `(x,y,x,γ(y))`; comparing AD with BC there gives `γ=β`. Hence all three equal one involution `π` of the three high labels. Up to a simultaneous relabeling, `π` is either the identity or the transposition `0↔1` fixing `2`.

Let `X_AB`, `X_AC`, `X_AD` be the actual nine-word high blocks in the three cuts. Explicitly,

    X_AB = {(a,a,c,π(c))},
    X_AC = {(a,b,a,π(b))},
    X_AD = {(a,b,π(b),a)},                 a,b,c∈{0,1,2}.       (4)

Their pairwise intersections, respectively, are

    X_AB∩X_AC = {(a,a,a,π(a))},
    X_AB∩X_AD = {(a,a,π(a),a)},
    X_AC∩X_AD = {(a,π(a),a,a)}.                                (5)

Each has three words; the triple intersection consists exactly of `(a,a,a,a)` for fixed points of `π`. Every high symbol occurs three times in each set in (4) and once in each intersection in (5). Therefore it occurs `6+1_{π(a)=a}` times in their union, using the corresponding label in its own party. These are counts of actual distinct E words.

*Identity.* The triple intersection has three words and the union has `27−9+3=21`. Every high symbol occurs seven times in that union, exhausting its actual `s=7`. The four remaining E words must therefore use the unique low symbol at every party. There is only one such quadruple, a contradiction.

*Transposition.* The triple intersection has one word and the union has `27−9+1=19`. Each fixed high symbol `2` already occurs seven times; each of `0,1` occurs six times and therefore has exactly one occurrence outside the union. There are six E words outside the union. In AB the low pair `(0,1)` has multiplicity two, but by (4)–(5) it appears only once in the union, namely `(0,1,0,0)`. The same calculation applies to `(A0,C1)` and `(A0,D1)`: each occurs only once in the union and needs one further E extension. Since A0 has only one remaining occurrence, that single word must be `(0,1,1,1)`. Similarly the unique remaining occurrence of A1 is `(1,0,0,0)`.

These two forced words exhaust the remaining occurrences of labels 0 and 1 at *every* party; label 2 was already exhausted. The other four outside-union words would all use the unique low symbol at every party, again giving only one quadruple. Contradiction. This exhausts both involution classes and proves the proposed whole-tensor `N=50,t=25` exclusion.

## 4. Low-excess lemmas needed for the other exact branches

All arguments in this section concern an arbitrary connected component of a genuine unitary support and use the twin/one-overlap facts from Section 1.

**Excess four, order five is impossible.** There are one or two degree-two rows. If there is one, the other four rows all have degree three. Its twin columns have degree three or four, so at least one high row avoids them and must use all three other columns. Any high row meeting the twins has only one other neighbor and hence overlaps the avoiding row once, impossible. If there are two low rows, their four twin columns must all have degree three, consuming the four units of column excess. Each twin pair has the low row plus a two-subset of the other three rows as neighborhood. The two such two-subsets meet; one overlap between columns is forbidden, so they are equal. The third high row can then meet only the fifth column, contrary to degree at least two.

**Excess four, order six is impossible.** There are exactly two degree-two rows, four degree-three rows, and, by transposition, two degree-two columns and four degree-three columns. The four high columns are the low-row twin pairs. The two low columns meet only the four high rows, in disjoint two-subsets `A,B`: a one-overlap is forbidden and equal neighborhoods would isolate a 2×2 component. Every twin column has two high neighbors and must meet each low-column neighborhood in zero or two positions, so those two neighbors are exactly A or exactly B. If both twin pairs choose the same subset, the other high rows have degree one; if they choose different subsets, the support disconnects. Both contradict a connected component.

**Excess five, order five is impossible.** If there is a degree-two line, transpose if needed and choose a low row. There can be at most two low rows. With one, the other row degrees are `3,3,3,4`. Its twin columns have degree three or four, so at least one high row avoids them and uses all three remaining columns. Each of the at least two high rows meeting the twins must then use at least two remaining columns to avoid a one-overlap, hence must have degree at least four; only one can. With two low rows, their four twin columns must all have degree three, because making either equal-degree pair degree four would use at least six units of column excess. Each pair again uses a two-subset of the three high rows, and different pairs cannot meet in exactly one high row. The subsets must coincide, leaving the third high row at most the fifth column.

If neither side has a low line, all five rows and columns have degree three. Each row omits two columns, and every column is omitted by exactly two rows. Two rows meet in at least one position; since one overlap is forbidden, they meet in at least two, so their two-column omission sets intersect. Fix one omitted pair `{u,v}`: among the other four rows, at most one also omits `u` and at most one also omits `v`, contradicting the requirement that all four omission pairs intersect `{u,v}`. Thus this last case is also impossible.

**Excess five, order seven is impossible.** There are exactly two low rows and two low columns; every other line has degree three. The four twin columns of the low rows are high. The two low columns have disjoint two-subsets `A,B` of the five high rows as neighborhoods: one overlap is forbidden, and identical two-row neighborhoods isolate a 2×2 block. Each twin column has exactly two high-row neighbors and meets each of A,B in zero or two positions, so its high neighborhood is A or B. The one high row outside A∪B meets neither low column nor any of the four twin columns, leaving at most one remaining column. Contradiction.

## 5. Exact t=27 exclusion

Here `n=9`, `|E|=23`, `e=5`. A positive component's excess partition is either `5` or `3+2`, since excess one is impossible. In the `3+2` case the positive components both have order three, and any other components have order two; the total order would be even, not nine. In the single-excess-five case, (1) gives order at most seven, and its order must be odd because the remaining components have even order. Order three cannot carry excess five, while orders five and seven are excluded in Section 4. Therefore no actual unitary residual support exists, proving the proposed standalone `N=50,t=27` exclusion. No alphabet, global t bound, phase restriction, or finite computation is needed for this branch.

## 6. Exact remaining target branches, and limits

For `t=26`, `n=10`, `|E|=24`, `e=4`. Each cut necessarily has **either** two 3×3-minus-one blocks and two 2×2 blocks, **or** one connected 4×4/12-entry component and three 2×2 blocks. Indeed, the positive excess partition is `2+2` or `4`; in the latter case parity, (1), and Section 4 leave order four. This is a necessary condition for each of the same three flattenings, not a classification of compatible all-six-pair incidences or phases. Both alternatives and their cross-cut couplings remain open here.

For `t=28`, `n=8`, `|E|=22`, `e=6`. In each cut, the positive excess partition is `6`, `4+2`, `3+3`, or `2+2+2`. The last needs order at least nine. In `4+2`, the excess-two component has order three; order eight and parity would force the excess-four component to have order five, excluded in Section 4. Thus the remaining per-cut alternatives are **either** two full 3×3 blocks and one 2×2 block, **or** one excess-six component of order 4, 6, or 8 with, respectively, two, one, or zero 2×2 blocks. Their possible supports, arbitrary complex phases, all-six-pair compatibility, and common-tensor realizability have not been settled. No independent-cut choices are asserted realizable.

## 7. Actual input coverage, administrative pins, and verification boundary

Main directly confirmed that the actual dispatch receipt existed. I read it, the entire manifest, freeze receipt, final binding, prepared metadata and all **22** manifest controls through their endings, as permission/status only. Before reading any packet body I sent Main a DIRECT PREBODY ACK identifying 22 controls and the ordered one-part/404-LF packet, and stating that no body, mathematics, or comparison had yet occurred. I then read the single packet serially in RAW windows `1–20,21–40,…,381–400,401–404`, through the ending, before research or comparison. The windows included the complete long lines. No sequence/presentation failure is known.

Complete body coverage and parent-declared original source SHA-256 pins (I did not open or separately re-hash the original outgoing source paths):

| ID | Original body LF | SHA-256 |
|---|---:|---|
| S1 | 1–29 | `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0` |
| S2 | 1–29 | `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a` |
| S3 | 1–31 | `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0` |
| S4 | 1–161 | `ac4f6284549678e0e0430242baed238230680b74a0f1facbd8e8e1cd99691181` |
| S5 | 1–132 | `c852a533a2e26cd2b7bcf37f38827c63511544d7b5d1a9e98b5454ac7b7f2b3a` |

Metadata-only local SHA-256 observations after complete packet reading:

| Own-directory file | Observed SHA-256 |
|---|---|
| `manifest-v1.json` | `940c76822c50d04ac69c3ea6d430ed986ec62e9f260192a49c3cc0dc689cb80f` |
| `freeze-receipt-v1.json` | `54e3b7864fa3a650e0d1ac2ae221510ed7f41cd2e4b543bd90c89d42c21de066` |
| `final-pre-dispatch-binding-v1.json` | `6a84820b28ca089eed299a52a751746dc32cc5daf99401603b88fa09c14909f9` |
| `parent-live-metadata-supply-v1.json` | `3c9fdb44b467bdd582e35ad398b794563aab7bf8a07114c64807c7a6fd3da2d1` |
| `dispatch-receipt-v1.json` | `5e4dcd0257616c1c0c55aa1fb5b2ce43c6b9c72c550cee351cd4d15b01621ce5` |
| `literal-packet-part-01-v1.md` | `564667431351ec1b2b91c4b469866ee6d425fb91ca50e7dcc8d205e4c88ad4db` |

All 22 manifest-listed permission/status controls were read through their endings and independently metadata-hashed. Names below are the manifest control identifiers; their exact full paths are in the pinned manifest. In manifest order:

| Control | Observed SHA-256 |
|---|---|
| prospective-author-method-scope-restoration-20261030-v1 | `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95` |
| contract-addendum-2-frontier-first-owner-direction-v1 | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` |
| parent-L1-selected-diagnostic-release-quarantine-v1 | `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` |
| parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1 | `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc` |
| parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1 | `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4` |
| parent-ame-held-compression-claim-consumer-quarantine-v1 | `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0` |
| parent-held-ph-registration-report-consumer-quarantine-v1 | `97fbd5967b472783c5ed860f0745b88d7917eb93e1c340f043c974a531ac1453` |
| f439 process quarantine | `74f9f9d57eb5866f68dec331b9bf4facca2bc8d4116186cd241b3bff1539dfee` |
| f444 process quarantine | `d00f41bf0205680ef8256f38c97d2023058da935c260ba5cc7f17cb77bd8e184` |
| f448 process quarantine | `f6ccc5fa10f0e30536921ea86828c437359869413919eae258cbbd82d4989805` |
| f508 process quarantine | `649349cfe636c88e60bee96400512ae6db8d8e12b875d3d100fcce3312785fd8` |
| f513 process quarantine | `cb9a81b76acaf740e2d691664e57e46a274c208f44fb071f5f0724973ae1a1a8` |
| f586 process quarantine | `e4d3dca7c41456e4e48dc154719b1df9e653b656b2cbf9324c82b195e3539681` |
| f602 process quarantine | `df412094a47e89be2507d7a7809d68449f08476aabfaca44fd9ecb4dce2a40b8` |
| f596 process quarantine | `3f4b2c6d31a420ecff35a6478ce7a302637765b1203c046619715eda634b6927` |
| f653 process quarantine | `a85930a9b268d472d5ded2f31b4b9916394e99f97e854c3a3869a9c8fd7ec8de` |
| f654 process quarantine | `9aaf84aabb3ea428e3622c5e6b7961d21bd3f1a8b3a16a727be203077e784462` |
| f659 process quarantine | `abf867950e1425ed74e1a766f6838957b255694cf0f64e936a23321c1324913b` |
| f660 process quarantine | `f5007a354d6acb8335ad2b9cc170f457c542640e1bbd15c5439d69d0c76039ab` |
| f662 process quarantine | `7dc07513bb05a7b08ba9795b566f38c39750a8f71fc68d576ea4367d4b0e4c38` |
| parent-remaining-d0-occupancy-E-row-omission-process-major-v1 | `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c` |
| parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1 | `27390c73fd6741217ce1d86c5f41e388ef87e3f51b306565053943e0333afbce` |

The parent-supplied freeze/binding asserts original-source roundtrip and matches; the hashes above do not certify correctness, original-source identity, independence, or clean cognition. No outgoing links, unlisted scientific sources, old code, sibling returns, or held episodes/consumers were opened. All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No scientific code, interpreter, solver, test, build, lint, formatter, external-model CLI, network, Git, install, or deletion was run; clock and SHA commands were administrative metadata observations only. No code was prepared and there is no executable output to claim. No parent adoption, independently reconstructed proof, family/human/kernel check, or novelty/priority is asserted. The parent must whole-read and independently dispose of this candidate; any correction is additive, never overwrite/backdating.
