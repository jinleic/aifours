# f279 — Written-mathematics review v1

## Verdict and assurance boundary

**0 FATAL / 1 MAJOR / 0 MINOR. Overall correctness: incorrect as written.** Confidence in the identified proof gap: **0.99**.

The free-action/sign-coset theorem, the missing-pair degree identities, the stated transitive sign consequences, and the reversal multigraph degree/edge counts are supported. Theorem 4(A) is not established: a permutation penultimate column gives out-degree one in M, not in-degree one; consequently its 14-permutation-type search reduction cannot be accepted as written. The 14-type list itself is complete under the additional hypothesis that M actually is a permutation digraph.

This is a **same-harness written review**, not human, independent-model-family, formal/kernel, novelty, priority, or literature-status verification. Imported dispositions are conditional inputs at their expressly adopted scopes. This review makes no parent-adoption decision and proves neither existence nor nonexistence of T2(11).

## 1. Frozen inputs and reading boundary

Source aliases used below:

- **M:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261029-sign-coset-and-m-dichotomy-manuscript-v1.md`.
- **P:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/park-v3-addendum-5.json`.
- **I175:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-prime-symbol-asymmetry-and-orbit-counts-parent-v1.md`.
- **I187:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-order-21-exists-and-refuted-boundary-shortcuts-parent-v1.md`.

Manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f279-tuscan-sign-coset-and-m-dichotomy/manifest-v1.json`.

Every listed SHA-256, byte count, and LF count was checked before that document’s body was opened. Each observed value matched its frozen value:

| Document | Observed SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | `fedfce34f5e64325eb16d654ad28b4e827097c93c4f3ac0ce6957b45ee5998c3` | 4322 | 51 |
| M | `7d6a567e8c91fdb3b53fdf1585ead85b61a10efd268dc0b34e6d563489716c57` | 9628 | 84 |
| P | `ffc323f67073f1631da91d14e71c76625e97a03629b561af9a165fbfd0bd3676` | 2571 | 27 |
| I175 | `20b187f303624afe0423fb4042b34a028f4cbdd3cc5577759bb709765e42d5eb` | 5995 | 22 |
| I187 | `a1955a3953295908c556ad44b6bd6240c4dad3dff6cbfd916f63a0ea8d4a032d` | 4900 | 22 |

The complete mandatory display sequence was manifest, M, P, I175, I187. All source displays were finished before mathematical consideration or mathematical note-taking began. The native clock observed at that boundary was **2026-10-30T03:20:02Z**. No scientific file linked from these documents was opened.

## 2. Finding

### MAJOR 1 — Require both boundary columns before making M a permutation

**Location:** M, LF60–65; primary affected statement LF60. **Priority:** P1. **Confidence:** 0.99.

At LF60 the manuscript states, “Then by Theorem 1, M is the digraph of a **fixed-point-free permutation** of the 11 symbols (all in/out-degrees 1; no loop, since a distance-two pair has distinct symbols).” LF65 repeats the decisive step: “In (A), Theorem 1 gives a 1-in-1-out loopless digraph on 11 vertices with 11 arcs, i.e., a permutation digraph without fixed points”. The hypothesis in case (A) is only α₉(x)=1 for every x. Theorem 1 then gives outdeg_M(x)=1, whereas indeg_M(x)=α₁(x) remains uncontrolled. Neither the total of 11 arcs nor absence of loops supplies the missing in-degree condition. Thus the proposed branch into 14 permutation types versus full-source symbols omits the unexcluded possibility that the penultimate column is a permutation but the second column is not. This is a load-bearing proof gap, not a demonstrated counterexample T2(11).

**Written negative control for the inference.** On vertices 0,…,10, take the arcs 0→2, 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→8, 8→9, 9→10, 10→0. This is loopless, has 11 arcs, and has out-degree one at every vertex. Its in-degree vector in vertex order is (1,0,2,1,1,1,1,1,1,1,1). It is not a permutation digraph and has no zero-out-degree vertex. All degree/sum facts cited in the disputed inference hold with α₉=(1,…,1) and this α₁. This countermodel refutes the degree-theoretic inference; it is explicitly **not** asserted to be realizable by a T2 array.

**Discrete repair.** Either prove an additional T2-specific implication that α₉≡1 forces α₁≡1, or change the reduction. A valid exhaustive replacement is: if **both** boundary columns are permutations, M is a fixed-point-free permutation with one of the 14 listed types; otherwise there is a full-source symbol or a full-target symbol, possibly both. If retaining a dichotomy based only on the penultimate column, its permutation-column branch must allow a general loopless out-degree-one digraph, not only permutation digraphs. P LF21 inherits the unsupported Theorem 4 claim.

## 3. Written reconstruction

### 3.1 T1 endpoints and the M boundary law

For n≥2, n permutation rows supply exactly n(n−1) directed adjacency events, all on the n(n−1) ordered pairs of distinct symbols. Injectivity therefore implies completeness. Each symbol has n−1 outgoing adjacency events and can supply at most one in a row; since it appears in every row, it is last in exactly one row. Dually, it is first in exactly one row. The rows are distinct: two identical rows would repeat an adjacency.

A symbol x sources a distance-two event except when it is penultimate or last. Consequently its number of outgoing distance-two events is n−1−α₉(x). T2 injectivity makes their targets distinct. Subtracting from the n−1 possible targets gives outdeg_M(x)=α₉(x). The corresponding receiving positions exclude first and second, so indeg_M(x)=α₁(x). Summing either boundary count gives n. Equivalently, |M|=n(n−1)−n(n−2)=n.

These identities support Theorem 1. They do **not** identify α₁ with α₉ or make either count vector uniform. The imported I187 item 3 explicitly permits non-permutation second and penultimate columns at n=8.

### 3.2 Free action, transitivity, and signs

If gR=R, every symbol appearing in the permutation row R is fixed by g; hence g=id. Every row stabilizer is trivial. Orbit–stabilizer gives row-orbit size |G|, and partitioning the n rows gives |G| dividing n.

The first-symbol map from rows to symbols is a bijection by the preceding endpoint argument and is G-equivariant: first(gR)=g(first(R)). Thus, in this setting, row transitivity and symbol transitivity agree. By freeness, transitivity is equivalent to |G|=n.

Treat R as a bijection from positions to symbols. Positionwise application is composition: gR=g∘R. Therefore sgn(gR)=sgn(g)sgn(R). For an orbit through R₀, freeness identifies its rows bijectively with G, so its sign multiset is sgn(R₀) times the sign multiset of G.

More explicitly, writing χ=sgn|G, the orbit’s **support** is the coset sgn(R₀)χ(G); each element of that coset occurs |ker χ| times. If χ is trivial, the orbit is sign-constant. If χ is nontrivial, its two fibers have equal size |G|/2, giving half positive and half negative rows in that orbit. This also shows that any nontrivial sign image forces a globally balanced array even without transitivity. Transitivity is needed for the manuscript’s single-orbit argument and, for an even group, for the conclusion that the whole array is sign-constant; it is not generally necessary for balance.

For transitive G, the entire row set is one orbit. It is a single sign class if and only if G≤A_n; otherwise its split is [n/2,n/2]. If |G| is odd, each element’s order divides an odd integer, all of its disjoint cycle lengths are odd, and its sign is +1. A transitive odd-order G therefore forces [n]. These are all-variable written arguments, not finite tests.

The phrases “exactly when” at M LF53 and “exactly in the transitive cases” at LF84 are not used here as an additional universal necessity theorem: the supported content is the explicit sufficient implications above and their application to the listed examples.

### 3.3 Orders 4 and 6: explicit reviewer-derived witnesses

These small witnesses were derived and checked in writing; no author rows or program were read.

For n=4, take all translates modulo 4 of b=(0,1,3,2). Its consecutive difference list is (1,2,3); its distance-two difference list is (3,1). The first list contains every nonzero residue exactly once, while the second has no repetitions. Translating each event through all four residues therefore makes D1 complete and D2 injective. Translation by one is an odd 4-cycle and acts transitively on the rows, forcing [2,2].

For n=6, take all translates modulo 6 of b=(0,2,1,4,5,3). Its consecutive differences are (2,5,3,1,4), and its distance-two differences are (1,2,4,5). The same difference argument proves T2. Translation by one is an odd 6-cycle and is row-transitive, forcing [3,3].

I187 item 3 conditionally supplies exactly one normalized square at each of orders 4 and 6. Normalizing a square means relabelling one row to the identity and ordering rows by their first symbols; these operations preserve T2 and preserve the unordered sign-class sizes, since a symbol relabelling multiplies all row signs by one common sign. Thus, conditional on those imported counts, the exhibited witnesses cover the order-4 and order-6 classes relevant to the manuscript’s table. The witness existence and sign calculations themselves do not require those counts.

### 3.4 Order 8: what even symmetry does and does not force

A generator with cycle type (2,2,2,2) has sign (−1)^4=+1. A free order-two group on eight rows has four size-two orbits, each sign-constant, so the coset theorem permits counts [2k,8−2k]. It does not force [4,4].

A generator with two 4-cycles has sign (−1)^3(−1)^3=+1, not −1. Every element of its cyclic order-four group is even. Its free row action has two size-four orbits. Equal orbit signs give [8]; opposite orbit signs give [4,4]. Neither alternative is selected by that group alone.

These implications are supported conditional on the listed symmetries. I187 item 3 imports a total of six normalized T2(8) squares and their non-permutation boundary columns, but does **not** import the 4+2 split by automorphism group or their row-sign and reversal profiles. The permitted packet contains no rows for those six squares. Those finer empirical assertions remain INCONCLUSIVE in this review, rather than being promoted from an author-labelled diagnostic to a verified fact.

### 3.5 Order 21 and the order-11 vacuity

I187 item 1 supplies the adopted order-21 T2 square in the form A(i,j)=a_i⁻¹a_j, where the a_i enumerate a group of order 21. For every group element h, left multiplication sends a row to h a_i⁻¹ a_j, again a row because h a_i⁻¹ ranges over the group. This is a regular, transitive symbol action of order 21. An odd-order permutation group is even by §3.2, so the entire square has a single row-sign class [21]. This consequence uses the imported construction, not unlisted row data or a presumed diagnostic group computation.

For n=11, I175 Theorem A applies to T1(11), hence to its subset T2(11), and gives a trivial symbol-automorphism group. The written argument in that import can also be reconstructed: freeness makes a nontrivial group have order 11; its generator is an 11-cycle, relabelled as translation on Z₁₁. A base row and its translates can be T1 only if its ten successive differences are exactly the nonzero residues. Their sum is 55≡0, whereas telescoping gives the difference of two distinct row endpoints, a contradiction.

Thus no nontrivial symbol-symmetry coupling of row signs is available at order 11 by this route. Literally, the trivial group has **11 singleton row orbits**, not “no orbits” as M LF55 says; each singleton gives only a tautological coset statement. Normalizing one row changes all row signs by a common factor and imposes no relative sign restriction through this argument. No conclusion about other possible, non-symbol-symmetry sign arguments is established.

### 3.6 The correct boundary cases

Since the nonnegative integers α₉(x) sum to 11, either all equal one or at least one is zero: if all were at least one, their sum forces equality everywhere. If α₉(y)=0, the outgoing D2 count is 10. It follows that all ten ordered pairs (y,z), z≠y, occur exactly once. The symbol is last in one row and in positions 0,…,8 in the other ten. The analogous argument for α₁ gives a full-target symbol.

What follows from α₉≡1 alone is that M is a loopless functional digraph. It need not follow from the stated argument that its functional map is injective. If **both** α₉≡1 and α₁≡1 hold, all in- and out-degrees are one, hence the functional map is a bijection. Since M contains only pairs with distinct symbols, the resulting permutation has no fixed points. Only under that additional condition does the 14-type classification follow.

An exhaustive repaired split is therefore: both boundary columns are permutations, yielding the 14 permutation types; or at least one boundary column is not a permutation, yielding a full-source or full-target symbol. Neither case is shown realizable or excluded at order 11.

### 3.7 Independent completeness check of the 14 types

Sort each partition in nonincreasing order and group it by its largest part. Parts one are forbidden. The following exhausts the possible remainder partitions, with all remaining parts between two and the chosen largest part:

| Largest part | Partitions of 11 with that largest part | Count |
|---:|---|---:|
| 11 | 11 | 1 |
| 10 | none: remainder 1 | 0 |
| 9 | 9+2 | 1 |
| 8 | 8+3 | 1 |
| 7 | 7+4; 7+2+2 | 2 |
| 6 | 6+5; 6+3+2 | 2 |
| 5 | 5+4+2; 5+3+3; 5+2+2+2 | 3 |
| 4 | 4+4+3; 4+3+2+2 | 2 |
| 3 | 3+3+3+2; 3+2+2+2+2 | 2 |
| 2 | none: 11 is odd | 0 |

The sum is 14. Every displayed partition sums to 11, none has a part one, and the largest-part grouping prevents duplication. This independently confirms exactly the manuscript’s list, conditional on M being a permutation digraph. It does not cure the missing hypothesis in Theorem 4(A).

### 3.8 Reversal map and surviving H facts

D1 completeness gives exactly one row containing x→y and exactly one containing y→x. These rows are distinct: a permutation row containing both edges would have to contain the directed 2-cycle x→y→x, repeating a symbol. Thus every unordered symbol pair defines an edge of a loopless multigraph H on the rows.

There are C(n,2) such symbol pairs and therefore that many edges, counted with multiplicity. A row contains n−1 adjacency events. It cannot contain both orientations of one unordered symbol pair, so those events give n−1 different symbol-pair edges incident with its vertex. Conversely every incident edge arises this way. Consequently every H vertex has degree n−1, with parallel edges counted. This proves the stated surviving facts; it does not make H simple.

The reviewer-derived order-4 witness gives a direct counterexample to injectivity. Its rows are 0132, 1203, 2310, 3021. The third is the reverse of the first, and the fourth is the reverse of the second. Every adjacency’s reverse occurs in that paired row. Hence the six unordered symbol pairs have only two distinct row-pair images, each of multiplicity three: **2/6, maximum 3**.

In the order-6 witness, reversing the base row is translation by three. The six rows similarly form three reversal pairs; all five edges of a row lead to its reverse. Thus the 15 symbol pairs have exactly three distinct images, each of multiplicity five: **3/15, maximum 5**. Conditional on the imported uniqueness counts, these profiles apply to the corresponding normalized classes, since relabelling symbols and rows preserves multiplicities.

The values **12–16/28, maximum 3 at n=8** and **147/210, maximum 3 at n=21** are author-labelled diagnostics at M LF73, repeated only partially in P. Neither named import supplies those profiles or their source rows in this permitted packet. They are INCONCLUSIVE here. The range “multiplicities to 5” is consistent with the verified order-6 example; it is not a claim that the manuscript says the order-21 maximum is five.

The generic reversal-bijection assertion is nevertheless decisively refuted by the explicit order-4 T2 witness, without needing either unresolved larger diagnostic.

## 4. Per-claim dispositions

“Conditional” below means the named import is used at its adopted scope, not independently re-certified wholesale.

| Claim and location | Disposition | Basis / exact limitation |
|---|---|---|
| First/last columns are permutations, M LF14 | SUPPORTED | D1 exactness and one incoming/outgoing slot per row. |
| outdeg_M=α₉, indeg_M=α₁, \|M\|=n, M LF22–26; P LF18 | SUPPORTED | Written event counts in §3.1. |
| Free row action and \|G\| divides n, M LF32 | SUPPORTED | A row contains every symbol; orbit–stabilizer. |
| Sign multiplication and orbit coset multiset, M LF34–39 | SUPPORTED | Composition and sign homomorphism; multiplicities stated in §3.2. |
| Transitive G not contained in A_n forces equal halves, M LF36 | SUPPORTED | Two equal fibers of the nontrivial sign homomorphism. |
| Transitive odd-order G forces a single class, M LF37,51 | SUPPORTED | Odd element orders imply even permutations; one row orbit. |
| Order 4 [2,2] and order 6 [3,3], M LF47–48 | SUPPORTED, conditional I187 item 3 for coverage of the unique normalized classes | Explicit reviewer-derived witnesses and transitive cyclic actions. |
| Order 8: even (2,2,2,2) and (4,4) groups do not choose the observed split, M LF49–50 | SUPPORTED as conditional group-theoretic implications | Both generators are even; free orbits have sizes two or four. |
| Exactly four order-8 examples of the stated Z₂ type and two of the stated Z₄ type, with the stated observed signs, M LF49–50 | INCONCLUSIVE | I187 imports six normalized squares, not these finer diagnostics; rows are not included. |
| Order 21 [21], M LF51 | SUPPORTED, conditional I187 item 1 | The adopted group-table construction explicitly has a left-regular order-21 action. |
| Order-11 symbol-sign mechanism vacuous, M LF55 | SUPPORTED, conditional I175 Theorem A | Trivial symbol group means only singleton orbits and tautological constraints. |
| Penultimate column is a permutation or some full-source symbol exists, M LF59–61 | SUPPORTED as a bare boundary-count dichotomy | Nonnegative counts summing to 11; §3.6. |
| Penultimate permutation alone makes M a permutation, M LF60,65; P LF21 | INCONCLUSIVE as a T2-specific claim; the stated degree inference is REFUTED | MAJOR 1. No T2(11) counterexample is asserted. |
| Exactly 14 possible fixed-point-free permutation types at 11, M LF60 | SUPPORTED conditional on M actually being a permutation | Independent exhaustive largest-part enumeration in §3.7. |
| Full-source and dual full-target conclusions, M LF61–63 | SUPPORTED | Zero missing outgoing/incoming degree gives all ten D2 events. |
| Reversal rows distinct; H regular of degree n−1 with C(n,2) edges, M LF71 | SUPPORTED | Written incidence argument in §3.8. |
| General reversal bijection | REFUTED | Explicit order-4 T2 witness, only two images for six pairs. |
| Reversal profiles 2/6 maximum 3 and 3/15 maximum 5, M LF73 | SUPPORTED for reviewer-derived examples; conditional I187 item 3 for normalized-class coverage | Explicit reverse-row pairing; no author code used. |
| Reversal profiles 12–16/28 and 147/210, M LF73 | INCONCLUSIVE | Permitted inputs lack rows and a checked profile derivation. |
| Supersession of the earlier author packets, M LF78–80; P LF13–15 | SUPPORTED only as the current author’s routing statement | Older packets were not opened and their contents were not re-adjudicated. |
| No order-11 witness or obstruction delivered, M LF82–84; P LF24 | SUPPORTED as a statement about this packet | No global current-literature/status certification is made. |

## 5. Complete raw-display coverage receipt

Every entry below is an actual raw `read` window. All windows contain at most 15 LF. These are complete documents, not selected passages. The last window of each includes its actual ending. No mathematical consideration or mathematical notes preceded completion of the final I187 window.

| Display order | Document | Raw LF windows, in actual order | LF covered |
|---:|---|---|---:|
| 1 | Manifest | 1–15; 16–30; 31–45; 46–51 | 51/51 |
| 2 | M | 1–15; 16–30; 31–45; 46–60; 61–75; 76–84 | 84/84 |
| 3 | P | 1–15; 16–27 | 27/27 |
| 4 | I175 | 1–15; 16–22 | 22/22 |
| 5 | I187 | 1–15; 16–22 | 22/22 |

Total: **16 raw windows, 206/206 LF including the manifest; 155/155 LF excluding it.** Frozen bytes checked: **27,416 including the manifest; 23,094 excluding it.** No omitted ending, read-ahead body, or source-body re-read is claimed.

## 6. Native-clock observations, process disclosures, and control boundary

These are observed `/bin/date -u` outputs, not asserted file-creation times or backdated events:

| Observation | Observed UTC clock |
|---|---|
| Before manifest metadata verification | 2026-10-30T03:19:15Z |
| Before M metadata verification and display phase | 2026-10-30T03:19:28Z |
| Before P metadata verification and display phase | 2026-10-30T03:19:41Z |
| Before I175 metadata verification and display phase | 2026-10-30T03:19:48Z |
| Before I187 metadata verification and display phase | 2026-10-30T03:19:55Z |
| After all required displays; before mathematical reconstruction | 2026-10-30T03:20:02Z |
| After first reconstruction pass; before procedural applicability check | 2026-10-30T03:23:37Z |
| Before report composition/output phase | 2026-10-30T03:24:43Z |

**Additive procedural-read disclosure.** Higher-priority harness instructions required reading `memory://root/memory_summary.md` and `skill://aifours-written-math-acceptance-protocol` before starting the assignment’s source reads. Those two procedural reads preceded the first observed clock; no earlier time is assigned to them. After all required source displays and the first reconstruction pass, `skill://independent-snapshot-review` was also read to check applicability; its independent-model CLI procedure was not launched. These three non-manifest procedural documents are disclosed exceptions to a literal all-files reading of the whitelist. They were not scientific premises; no linked repository file, model configuration, network source, prior review, or author code was opened through them. The late procedural-skill consultation is disclosed rather than represented as having occurred before the review.

All mathematical controls in this review are written reconstructions: the degree-inference countermodel, exhaustive partition enumeration, and explicit order-4/order-6 witnesses and reversal counts. **No scientific program, exact-control script, enumerator, solver, author script, external model, network request, build, or test suite was run.** The only shell calls were native-clock and SHA-256/byte/LF metadata commands, each with a 120-second tool deadline. No metadata mismatch or tool-reported timeout occurred. No script-level exit-code receipt, finite enumeration, or computation-derived acceptance is claimed.

No sibling review, held/withdrawn/ZERO/quarantined source body, prior-wave review output, or unlisted scientific file was opened. Named imports were read as allowed disposition bodies only; their linked evidence was not opened. No frozen source, manifest, disposition, ledger, or README was modified. No cleanup or deletion was performed. Output is restricted to this review, with no adoption decision.

## 7. Review scope at handoff

The sign-coset argument and its qualified applications can stand independently of MAJOR 1. The corrected reversal-map core also stands: distinct endpoint rows, regular multigraph counts, and a genuine failure of injectivity demonstrated already at order four. Exact larger-order reversal profiles and the finer order-eight automorphism/sign census are not verified by the permitted packet.

The asserted 14-type/full-source reduction must not be treated as an exhaustive search reduction until the missing in-degree condition is proved or the full-target alternatives are retained. In particular, none of the 14 conditional permutation cases, nor any complementary boundary case, is excluded here. **T2(11) is unresolved by this packet.**

## 8. Additive publication receipt

The complete review was submitted to the write tool for the assigned wave’s `review-v1.md`. The tool refused that filesystem path, stating that it accepts only `xd://` transport and `local://` scratch paths. No repository output file was written, and no alternative write mechanism or out-of-wave artifact was used.

The native clock observed after this refusal was **2026-10-30T03:27:13Z**. This is an observation after the attempted publication, not a file-creation timestamp. The complete review is therefore delivered in-channel under the manifest’s explicit fallback provision.
