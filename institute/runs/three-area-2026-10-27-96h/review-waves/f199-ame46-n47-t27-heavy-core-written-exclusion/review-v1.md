# Same-harness review: N=47, t=27 heavy-core written exclusion

**Disposition: 0 FATAL / 0 MAJOR / 0 MINOR for the stated branch; 0 INCONCLUSIVE load-bearing mathematical claims.** The written contradiction reconstructs for all four requested cases: merged triangle, balanced, antibalanced, and mixed. The advertised CNF/search corroboration and the contents of the author's control receipt are **INCONCLUSIVE / not inspected and not premises**. The separate N=47→t=27 reduction, unconditional N=47 exclusion, support ≥48, novelty, and stronger verification are outside this review, not proved or assessed here.

Native clock observed immediately before composing this review: `2026-10-29T13:18:28-0700 PDT`. This observation is not a claimed creation or completion time.

## Frozen inputs and actual sequence

The first research artifact opened was `manifest-v1.json` in this wave. Its measured SHA-256 was `605e4e2cc9593d8d8b6e3bebc2ac3ac60c6c6f720c870e1a66272fa9b42a582e`, matching the assigned prefix `605e4e2cc959`; it measured 3,092 bytes and 30 LF. The initial manifest display shortened its long requirements line, so that line was separately displayed in full as raw line 29. Before opening either input body, I measured both inputs' SHA-256, byte count, and LF count; every measurement matched the manifest. Operational memory and skill instructions were read after those measurements; they are not mathematical evidence.

| Read order | Frozen input | Measured SHA-256 | Bytes / LF | Actually displayed raw windows, inclusive |
|---|---|---|---|---|
| 1 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-no-hamming-one-parent-v1.md` | `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0` | 5,552 / 25 | `1–13`, `14–25` |
| 2 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261029-n47-heavy-core-written-exclusion-v1.md` | `7fbfc5ce1255e1575b64d3d0b73c612afb2af2c93d8e682f16c8031ff6fa2fea` | 11,903 / 115 | `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–115` |

Both bodies were completely displayed in that order, including their final lines, before mathematical reconstruction or controls. A raw window did not exceed 15 lines. The N=46 disposition is context only: its conditional N=46 no-Hamming-one result and finite branch are **not** assumed here. Linked bodies, earlier reviews, author programs, author PASS/receipts, and the 69 claimed certificates were not opened or used as evidence.

## Per-claim findings

`0F/0M/0m` means no fatal, major, or minor defect found at the reconstructed scope; it is not formal verification.

| Claim | Verdict | Basis and boundary |
|---|---|---|
| AME flattenings and maximal-entry removal give 9×9 residual unitaries with 20 nonzeros and no singleton line | 0F/0M/0m | Direct row/column norm argument, §1 below. |
| Excess-two residual classification and forced 2×2 heavy rectangle in every cut | 0F/0M/0m | Component proof uses both the no-one-overlap rule and the two-row spanning argument, §2. |
| Same-tensor pair partition; j-independent d and h; at most one merged party | 0F/0M/0m | Counts apply to the original P and E in every cut, §3. |
| Activity inequality forces ≥3 size-4 parties; these have degrees 2,2,2,3 and yield ≥3 low-heavy parties after merged exclusion | 0F/0M/0m | Inclusion–exclusion count, §4. |
| **Merged triangle:** both sign types contradict the same 3×3 residual block | 0F/0M/0m | Even parity overloads; odd parity gives different supports for the two full rows, §5. |
| All-split signed K4 has exactly balanced, antibalanced, mixed switching/permutation classes | 0F/0M/0m | Explicit star switching and triangle cases, §6. |
| **Mixed:** one heavy pair has four distinct extensions | 0F/0M/0m | Four forced rectangle intersections, §7. |
| **Balanced:** any low-heavy fiber would require a duplicate support word | 0F/0M/0m | The even-parity core already saturates its two-symbol projections, §8. |
| **Antibalanced:** two low-heavy fibers force an overloaded heavy or ordinary pair | 0F/0M/0m | Unique complementary completion and both bit cases, §9. |
| Exact N=47, t=27 nonexistence and stated no-import boundary | 0F/0M/0m | §§1–10 independently reconstruct it without no-OLS, no-Hamming-one, SAT/LRAT, or a prior research program. |
| Author's 69 CNF certificates/search correspondence and author control/receipt contents | INCONCLUSIVE, out of proof scope | Not inspected, executed, or relied on. Independent controls below are not an authentication of those artifacts. |
| General N=47→t=27, unconditional N=47 exclusion, support ≥48, novelty, or stronger verification | Not claimed by this review | These are outside the frozen target; no inference to them is made. |

## Independent written reconstruction

### 1. From the AME hypothesis to a residual matrix

For each partition of the four parties into two pairs, the corresponding flattening `U=6ψ` is a 36×36 unitary by the AME two-party marginal condition. A coefficient of modulus `1/6` gives a unit-modulus matrix entry. Its row and column have all other entries zero, since their squared norms are one. Consequently the 27 such entries occupy distinct rows and columns in each of the three cuts. Deleting those rows and columns leaves a 9×9 unitary supported on the same 20 remaining tensor positions E. No residual row or column can have one nonzero, because then that nonzero has modulus one and would be a 28th maximal coefficient. Every residual line therefore has degree at least two.

### 2. Excess-two classification, including the necessary spanning step

Consider one residual unitary and its bipartite support graph. Its connected components give disjoint matrix blocks. If a component has r rows and c columns, its rows are orthonormal in C^c and its columns are orthonormal in C^r, so r≤c and c≤r: each block is square. The degree lower bound gives nonnegative integer excess `edges−2r` per block, and the total excess is `20−2·9=2`.

Two rows of a unitary cannot have exactly one common nonzero column: their inner product would be a single nonzero term. Also, if two degree-two rows have the same two-column support, their restrictions are orthonormal and span C². Every other row must therefore vanish in those columns; the two rows and columns are an isolated 2×2 block. Thus, in any connected block of size greater than two, the supports of its degree-two rows are pairwise disjoint. Writing s for their number and b for the number of higher-degree rows, these disjoint pairs give `2s≤s+b`, hence `s≤b`. Every higher-degree row contributes at least one unit of excess, so `b≤excess`.

A zero-excess connected block cannot have size >2 by this inequality, and its degree conditions force the full 2×2 block. Excess one would have `b≤1` and hence size `s+b≤2`, impossible for a positive-excess simple 2×2 support. Consequently the total excess two belongs to one connected positive-excess component. It has size at most four. If size four, then `s=b=2` and both higher rows have degree three. The two disjoint degree-two supports partition its four columns into pairs. A higher row must meet each such pair in zero or two columns, since an intersection of size one is forbidden. Its degree is therefore even, a contradiction. Size two cannot carry positive excess, so the component has size three and exactly eight nonzeros: it is a 3×3 block with one zero. All remaining blocks are full 2×2 blocks.

It follows in every cut that the residual pair projection has nine values: two heavy values with three extensions and seven ordinary values with two extensions. In the 3×3 block, the two degree-three rows and two degree-three columns are full on the same three opposite lines. In particular their 2×2 rectangle consists of four actual E words. This conclusion is about the original tensor in each cut, so rectangle words from different cuts may be combined as members of one and the same E.

### 3. Local d and h, and merged versus split

Let `m_i(a)` be the number of maximal P words having local symbol a at party i. For each j≠i, all six pair values `(a,b)` occur in the pair projection of P∪E, because each corresponds to a nonzero row of a unitary flattening. A P value is occupied by exactly one P word and no E word; distinct P words have distinct pair values. Thus

`d_i(a)=|π_j(E_a)|=6−m_i(a)`

is independent of j. For an E symbol, d≥1. If d=1, all E words in that fiber agree at every other party, so there is only one such word; a corresponding residual line would have degree one. Hence d≥2. Summing over E symbols gives `Σ_a d_i(a)=9`, so each E alphabet has at most four symbols. Since each pair projection has nine values and the opposite alphabet has at most four symbols, every E alphabet has at least three symbols.

Let `h_ij(a)` be the number of heavy `(i,j)` values using a. Counting the same fiber gives `|E_a|=2d_i(a)+h_ij(a)`, hence h is also independent of j; write it `h_i(a)`. It is nonnegative and sums to two at each party. Either two symbols have h=1 (split), or one has h=2 (merged). Two merged parties are impossible: both heavy values of their mutual pair would have to be the same distinguished pair value, whereas heavy values are two distinct cells.

### 4. Activity count and low-heavy supply

Write `r_i∈{3,4}` for the E alphabet size. A P word is active at i when its symbol there is in the E alphabet. At i, the number of active P words is `Σ_a(6−d_i(a))=6r_i−9`. At i,j, the number active at both is `r_i r_j−9`: among these `r_i r_j` pair values, nine belong to E and the other values each correspond to one P word. For a P word active at k parties, its contribution to the sum of single activities minus pair activities is `k−C(k,2)≤1`, including the cases k=3,4. Summing over 27 P words gives

`Σ_i(6r_i−9)−Σ_{i<j}(r_i r_j−9)≤27`,

or `6Σ_i r_i−Σ_{i<j}r_i r_j≤9`. For sorted profiles 3333, 3334, 3344 the left side is respectively 18, 15, 11, all impossible. Thus at least three parties have r=4. Their four integer degrees sum to nine and are each at least two, so their multiset is exactly `(2,2,2,3)`. Once §5 rules out merged parties, both heavy symbols at each such party are distinct; at most one has degree three, so at least one has d=2 and h=1. Such a low-heavy symbol has `|E_a|=2·2+1=5`. There are therefore at least three low-heavy parties; in particular the later balanced and antibalanced arguments have enough of them.

### 5. Merged triangle

Suppose A is merged at a. The other three parties B,C,D are split. Each heavy pair relation among B,C,D is a perfect matching of their two heavy symbols. Relabel their bits so BC and BD are equalities; CD is either equality or inequality. For every heavy BC pair and every heavy AD pair the full heavy rectangle forces a word of E, and similarly for BD×AC and CD×AB. Since both heavy A-containing pairs have A-symbol a, the forced binary triples `(b,c,d)` are exactly the union of those satisfying at least one of the three triangle relations.

If CD is equality, every binary triple has an equal pair, so all eight occur. For either b the heavy pair `(a,b)` then has four distinct extensions, exceeding three.

If CD is inequality, the forced CD supports are `{00,01,10}` for b=0 and `{11,01,10}` for b=1. The rows `(a,0)` and `(a,1)` are the two heavy AB rows; each already has exactly three forced extensions, so these are their complete supports. But the two heavy rows of the unique 3×3 block must both have the same three columns. Their supports differ, a contradiction. This second case does not follow from multiplicity caps alone. No party is merged.

### 6. Exhaustive signed K4 classes

With every party split, its two h=1 symbols can be labeled 0 and 1. The two heavy cells for each pair form a perfect matching `x_i xor x_j=e_ij`. Switching the labels at one vertex toggles its three incident edge signs; it is merely a relabeling, with the identity of a low-heavy symbol carried along.

Switch three vertices as necessary so that all edges from one fixed vertex are equalities. The remaining triangle has 0, 1, 2, or 3 inequalities. Zero gives the all-equality balanced representative. Three becomes the all-inequality antibalanced representative by switching the fixed vertex. One is the single-inequality representative. If two are negative, switching their common triangle vertex changes both to equality and makes exactly its edge to the fixed vertex negative. Permuting parties makes the position of the single negative edge immaterial. Thus the three stated classes are exhaustive; their distinct triangle-sign invariants distinguish them.

For a signed representative, define F as the union, inside the four binary heavy alphabets, of the three forced rectangles associated with the three pair partitions. A binary word is in F exactly when both pair relations of at least one of those partitions hold. Every such word is an actual E support position.

### 7. Mixed class

Take BC to be the only inequality, all other edges equalities, and fix the heavy BC value `(b,c)=(0,1)`. The BC×AD rectangle forces `(a,d)=(0,0)` and `(1,1)`. The AB×CD rectangle forces `(0,1)`, and the AC×BD rectangle forces `(1,0)`. These are four different extensions of the same heavy BC value, whose allowed multiplicity is three. Thus mixed is impossible.

### 8. Balanced class

For all-equality relations, F is precisely the eight even-weight binary four-words: 0000 and 1111 occur in all three rectangles, while each of the six weight-two words occurs in the rectangle grouping its equal bits. Let a low-heavy symbol at party i have bit a. Its fiber contains four F words, and at every other party each heavy bit occurs twice. Since its projection degree is only two, these already-present two heavy symbols exhaust the allowed projection at every other party: its fifth word cannot use a third symbol there.

The heavy neighbor of a is a at each other party, and the corresponding pair must occur three times. The four existing words contribute two, so the fifth must have bit a at all three other parties. The resulting uniform word is already in F. A tensor support cannot contain the same word twice, a contradiction. Section 4 supplies a low-heavy symbol, so balanced is impossible.

### 9. Antibalanced class

For all-inequality relations, F is exactly the six weight-two binary four-words. Fix a low-heavy bit 0 at i. Its three F fiber words have other-coordinate triples 011, 101, and 110. At each other party the heavy neighbor 1 occurs twice and ordinary bit 0 once. Two new fiber words must therefore add one 1 and one 0 at each other coordinate: their triples are complements. A triple of weight one has a weight-two complement already in F, and a triple of weight two is itself already in F. The only possible new pair is 000 and 111. Thus the fiber forces the uniform word 0000 and the star `W_i,0` with bit 0 at i and bit 1 everywhere else. Complementing bits shows that a low-heavy bit 1 forces 1111 and `W_i,1` with bit 1 at i and 0 elsewhere.

Choose low-heavy symbols at distinct i,j with bits a,b; §4 provides at least two. If a≠b, their pair value is heavy. F contributes two extensions and the two distinct stars `W_i,a` and `W_j,b` contribute two more, for four >3. If a=b, let k,l be the remaining parties. Their pair `(1−a,1−a)` is ordinary: F contributes one extension and the two distinct stars contribute two more, for three >2. In each case the stars are outside F and are distinct, so no multiplicity is counted twice. Antibalanced is impossible.

### 10. Conclusion and no-import check

The merged case and each of the three exhaustive all-split classes are impossible. Therefore the assumed normalized complex AME(4,6) state with exactly N=47 and t=27 cannot exist. The proof uses only the stated AME hypothesis/definition, elementary complex linear algebra and orthogonality, and finite counting. It does not require no-OLS(6), the N=46 no-Hamming-one lemma, SAT or LRAT, phase solving, a prior research program, the 69 certificates, or a floating search result. The N=46 context was not transported to N=47. This confirms the candidate's no-import claim at the reconstructed branch scope; it does not verify claims about external programs or certificates.

## Independently written finite controls and receipts

I wrote only `reviewer-heavy-core-control-v1.py` in this wave, using Python standard-library combinatorics and exact rational arithmetic, and did not read, import, compile, or run author code. These finite checks corroborate parts of the written proof; they are not premises and do not replace the general component argument. Each run was invoked with a 120-second tool deadline. Native times below came from `/bin/date`; identical displayed seconds mean only that both observations had the same one-second resolution.

| Run | Script SHA-256 observed before run | Native start / end (PDT) | Exit | Observed result |
|---|---|---|---|---|
| Initial | `294c313bbd95ef42cb7963bf2e6fc4de058da86810da2c0a4225cc38a4f58aa5` | `2026-10-29T13:16:31-0700` / `2026-10-29T13:16:31-0700` | 1 | My assertion wrongly treated the no-one-overlap condition alone as sufficient: it found 72 connected 4×4 excess-two patterns as well as the expected 2×2 and 3×3 patterns. This was a defect in my initial control, not evidence against the candidate, which explicitly supplies the additional span argument. |
| Corrected | `0739b0cc94328b851e484aa6c9309532e2f44911f90e8578525ff09d63bb0b5a` | `2026-10-29T13:17:04-0700` / `2026-10-29T13:17:04-0700` | 0 | Added the independent necessary equal-degree-two-row spanning condition; all checks then completed. |
| Final, with an added one-low-fiber negative | `676ad43f771b0af5fca50eb7bba04f44072b8d0b24a77f32501620499f115626` | `2026-10-29T13:17:51-0700` / `2026-10-29T13:17:51-0700` | 0 | All checks completed, with the results listed below. This hash identifies the retained final script. |

The script was first composed after native clock `2026-10-29T13:15:56-0700 PDT`, corrected after `2026-10-29T13:16:55-0700 PDT`, and enhanced after `2026-10-29T13:17:42-0700 PDT`. Earlier script versions were edited in place, so their hashes and run outcomes above are execution observations, not claims that separate copies are retained. No run hit its cap.

Final exact-control observations:

- Connected supports of sizes 2–4 and excess 0–2, after the necessary no-one-overlap and two-row-span conditions: one labeled 2×2 zero-excess support and nine labeled 3×3 excess-two supports. An exact rational 3×3 orthogonal matrix with eight nonzeros supplies a positive realizability control. Larger sizes are excluded by the written argument, not by this enumeration.
- Intended-reason negatives: a connected 3×3 degree-two six-cycle fails because row intersections have size one; 72 connected 4×4 excess-two patterns pass no-one-overlap alone but fail the equal-pair span condition. A single word active at all four parties shows that the raw activity-incidence sum can exceed the number of words, while `k−C(k,2)` correctly accounts for overlap.
- All eight merged triangle signatures were checked: four force four extensions of a heavy row; the other four give three extensions per heavy row but unequal row-support sets. In particular the odd-triangle cases pass a multiplicity-only check, exposing why the common-block support condition is necessary.
- Direct switching/permutation orbits of the 64 signed K4s have sizes 8 balanced, 8 antibalanced, and 48 mixed. Every mixed signature has a heavy-pair overload. The balanced and antibalanced forced cores alone satisfy all pair caps, an intended nonvacuity negative.
- Across 64 balanced low-heavy fiber instances there is no distinct fifth binary word. As an intended negative, allowing the already-present uniform word a second time would fake the required counts, so support uniqueness is load-bearing. Across 64 antibalanced instances the two-word completion is unique; each individual completed fiber still satisfies all pair caps. For two such fibers, all 192 instances overload a pair: 96 opposite-bit cases exceed a heavy cap and 96 same-bit cases exceed an ordinary cap. Switching mixed to balanced removes the immediate mixed overload, another intended class-boundary negative.

## Imports, gaps, and contract deviations

**Explicit imports:** the normalized complex AME(4,6) hypothesis, N=47, and t=27, plus standard definitions of a unitary and elementary linear algebra. No earlier mathematical result is imported. The finite script uses only standard-library `collections`, `fractions`, and `itertools` and no research program.

**Remaining gap:** there is no identified unproved step in this written branch reconstruction. Whether every N=47 AME state has t=27, the status of other support sizes, the cited certificate/search artifacts, and any novelty claim remain outside this frozen review. A cap or timeout would have been UNKNOWN, not an exclusion; none occurred in these controls.

**Deviations:** no deviation from the assigned manifest/input-order, evidence, ownership, or execution contract identified. The initial reviewer-control assertion failure and its repair are disclosed above rather than concealed or treated as a pass.

This same-harness review is **not** human review, independent-model-family review, formal/kernel verification, or novelty verification.
