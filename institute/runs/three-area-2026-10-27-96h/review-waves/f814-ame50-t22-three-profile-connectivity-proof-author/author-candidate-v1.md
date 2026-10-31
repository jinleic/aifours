# Three actual support-50/t=22 profiles: written connectivity reconstruction

**Status.** NONBLIND, same-harness GENERAL AUTHOR candidate. Subject to the actual-tensor hypotheses below, the written argument excludes a `12+16` residual-component split for each of `3566`, `3666`, and `4456`; equivalently their 28-word residual agreement graph is connected. It reconstructs the needed 12-word classification and all binary-party locations. I found no mathematical gap in the scrutinized f805 split argument, but this is an author reconstruction, not an automatic disposition. The connected cases remain open. No support-50 exclusion or witness is claimed.

## 1. Exact object, imports and local incidence

Fix **one** normalized complex AME(4,6) tensor, **one** local orthonormal product basis and the same four physical parties throughout. Set `U=6 psi`. Assume exactly 50 nonzero entries of `U`, exactly 22 of modulus 1. Let `P` be those 22 words and `E` the other 28. Agreement edges join E words sharing at least one physical coordinate pair; components refer to this one graph on these actual words. A profile `q_1q_2q_3q_4` records, up to party permutation, the number `q_i` of local symbols actually used by E, not local Hilbert-space dimensions.

The packet supplies this setup and the elementary unitary-block interface (S1–S5 below). For clarity I reconstruct the portions used rather than assuming the unadopted f805 claims. In any balanced cut, a modulus-1 entry exhausts its row and column. Remove the 22 singleton rows and columns. The remaining 14-by-14 unitary has 28 nonzero entries, no zero or singleton row or column, hence exactly two per row and column. Its support is 2-regular; a cycle longer than four gives two rows with exactly one shared nonzero column, contradicting orthogonality. Thus it is seven disjoint `K_2,2` blocks. Consequently, in **each** physical pair projection there are exactly 14 E values with two E extensions and exactly 22 P values with one P extension; these classes are disjoint and cover all 36 values. In particular, P is injective at every physical pair, and the **same 22 physical P words** cover all missing E pair values. Separate per-cut completions are not sufficient.

For a component `C` and a symbol `x` used at party `i`, let `d_i^C(x)` be its number of distinct neighbors at a different fixed party. It does not depend on that other party: each used pair `(x,y)` has exactly two extensions, and both E extensions are in `C` since they agree on that pair. Thus `x` occurs in exactly `2 d_i^C(x)` C words and `sum_x d_i^C(x)=|C|/2`. Moreover `d_i^C(x)>=2`: if it were one, the same occurrence count forces one neighbor at each of the other three parties, so its two required occurrences would be the same physical word. The same statements hold for global E degrees `d_i(x)` with degree sum 14. If two components both use a symbol, their neighbor sets are disjoint in every other physical party: a common pair value would connect their words. Hence their local degrees add to its global degree. These are actual pair incidences, not abstract degree sequences.

## 2. Why the only split is 12+16, and the NEW 12 claim

For each physical pair, exchange its two E extensions. Each is a fixed-point-free involution on E. Complementary-pair involutions commute on each physical square and form four-element orbits, so every agreement component has size divisible by four. A four-word component has at most one symbol per party from the degree bound, inconsistent with its two distinct pair values. An eight-word component has at most two symbols per party and hence fits in a two-symbol-per-party box. Such a box has at most seven E words:

* It has at most eight because each of four values of any chosen physical pair has at most two E extensions. If it had eight, every internal pair value in every pair would already have both E extensions inside the box. No P word shares such a value. Its same binary subtensor is therefore a closed 4-by-4 unitary block in all three cuts, giving a normalized four-qubit state with maximally mixed two-qubit marginals after division by 2.
* Tracing one qubit of that pure state gives a three-qubit `rho` with maximally mixed one- and two-qubit marginals and `rho^2=rho/2`. Its Pauli expansion is `(I+M)/8`, with M a real sum of weight-three Pauli strings. Thus `M^2=3I+2M`. A product of two distinct weight-three strings has weight three only if all three local factors differ; then the strings anticommute and the cross terms cancel. Squares are scalar, so the weight-three part of `M^2` is zero. This forces `M=0`, contradicting the scalar equation.

Each component has at least 12 words and total size is 28. Thus the alternatives are one component of 28, or exactly components `C12,C16` of sizes 12 and 16.

For C12, each local alphabet has at most three symbols; every pair has six values. All local alphabets have at least two symbols, and two binary parties would provide at most four pair values. Hence the only possibilities are `2333` and `3333`. In a ternary C12 party the degree sequence is `(2,2,2)`; in a binary one it is `(3,3)`.

**Exclusion of `3333`.** Every ternary pair graph is a 3-by-3 complete bipartite graph with a perfect matching removed, because every vertex has degree two. Fix a symbol in one party. Its four words induce a balanced 2+2 partition for the two symbols occurring in each of the other three parties: each pair value has exactly two E extensions. Any 2-by-2 rectangle of `K_3,3` minus a perfect matching has a missing cell, because any two rows' two missing columns meet any two chosen columns. Two distinct balanced 2+2 partitions would realize all four cells, impossible. So all three partitions coincide; then only two distinct remaining-coordinate triples occur among the four words, contradicting distinctness. Therefore C12 has exactly one binary party and three ternary parties.

**Canonical C12 support and phases.** Call the ternary parties A,B,C and the binary party D. Each ternary pair graph is `K_3,3` minus a matching, while a binary–ternary graph is full. Fixing A, the balanced B and C partitions coincide by the same missing-rectangle argument. Distinctness makes D take both values on each resulting ABC triple, so C12 is `T x {0,1}` for six distinct triples. Every ternary pair value identifies at most one triple, and each ternary symbol occurs in precisely two triples. Join triples sharing one ternary coordinate. Because no two share two coordinates, the graph is simple, 3-regular on six vertices.

For two triples joined through, say, A, the two D values form an actual unitary square in cut `AD|BC`. Writing `r_t=z_(t,0)/z_(t,1)` for unit phases, its square equation gives `r_t=-r_t'`. Thus the triple graph is bipartite. A simple 3-regular bipartite graph on six vertices is `K_3,3`; each ternary symbol occurs once on each side. Label the first side `L_i=(i,i,i)` for `i in Z/3`. On the other side, the B and C coordinates relative to A are the two different nonidentity 3-cycles, since a common choice would make two triples share two coordinates. After possible B/C exchange,

`L_i=(i,i,i),  R_i=(i,i-1,i+1),  i in Z/3`.

Along the graph edges squared moduli alternate, and the phase ratios alternate. Equivalently the actual amplitudes have, for `0<p<1`, unit `eta` and unit `v_t`,

`U_(L_i,0)=sqrt(p) v_(L_i)`, `U_(L_i,1)=sqrt(1-p) eta v_(L_i)`,

`U_(R_i,0)=sqrt(1-p) v_(R_i)`, `U_(R_i,1)=-sqrt(p) eta v_(R_i)`.

Conversely these amplitudes make three disjoint active unitary squares in each cut on the displayed 12 words. This is a **partial** tensor only. The split exclusions below actually need only the proven `2333` incidence, not the canonical labels, chosen phases, or a claimed completion.

For C16 each degree sum is eight, every used degree is at least two, so every local alphabet has at most four symbols. A binary C16 party has degrees `(4,4)` and therefore at least four distinct neighbor symbols in **each** other party. A ternary C16 party has degrees either `(2,2,4)` or `(2,3,3)`; if it has a three-symbol C16 partner, every degree is at most three, so only `(2,3,3)` is possible. These facts do not assume that a C16 support exists.

## 3. Global degree and common-P facts used in the cases

For `3566` and `3666`, there is a three-symbol E party, so any symbol in a six-symbol party has global degree at most three. For `3566`, denote the 3- and 5-symbol parties by A and B. Since their degrees sum to 14 and are at most the other party's alphabet size, the global A degrees are `(4,5,5)` and the global B degrees are `(2,3,3,3,3)`. In particular each degree-5 A symbol sees all five B symbols.

For `4456`, let A,B have four E symbols, C five and D six. We justify the D degree bound rather than assume it. For a P word let `k` count how many of its four coordinates are E-used, and let `n_k` count such P words. Actual pair coverage and injectivity give

`sum n_k=22`, `sum k n_k=6 sum q_i-56=58`, and
`sum binom(k,2)n_k=sum_(i<j) q_i q_j-84=50`.

Thus `3 n_0+n_1+n_4=66-2*58+50=0`; in particular a P word has at most two non-E-used coordinates. At a fixed D symbol, each of the two unused A symbols, two unused B symbols and one unused C symbol determines an actual P pair and hence one P occurrence: five outside-coordinate incidences. One P word contributes at most two, so at least three distinct P words occur at this D symbol. Since its six D–A pair values split into `d_D(x)` E values and `6-d_D(x)` P values, `d_D(x)<=3`. No independent pair completions are involved. Global A and B degrees are at most four since they are neighbors of one another.

It follows in all three profiles that C12 and C16 use **disjoint** local alphabets at each six-symbol party: a shared symbol would have global degree at least `2+2=4`. Their union is the entire six-symbol E alphabet there. Thus a ternary C12 alphabet gives a disjoint `3+3` split there, and a binary C12 alphabet gives a disjoint `2+4` split.

The following counting observation is used literally on the common P set. If X and Y have disjoint component alphabets, then every pair in `X_12 x Y_16` is a P pair: neither E component can realize it. These pairs identify different P words by XY injectivity. To bound words with a specified third-party class, map them injectively to a suitable pair of that class with X or Y; only cells not occupied by either component can be P. All bounds below refer to these actual physical P cells.

## 4. `3666`: all four C12-binary locations

Let A be the 3-symbol party and X,Y,Z the full parties.

* **Binary A.** Each of X,Y,Z has a disjoint `3+3` split. The nine `X_12 x Y_16` cells are P. A corresponding P word with Z in `Z_12` uses a `Z_12 x X_12` P cell; this 3-by-3 rectangle contains six C12 E cells, leaving at most three. With Z in `Z_16`, it uses a `Z_16 x Y_16` P cell; that rectangle contains eight C16 E cells, leaving at most one. Every Z symbol lies in one of those two alphabets. Hence the same nine distinct P words would satisfy `9<=3+1`, impossible.
* **Binary X, Y, or Z.** By symmetry take the binary full party as Z. X,Y both split `3+3`, while Z splits `2+4`. Again nine `X_12 x Y_16` pairs are P. With Z in `Z_12`, the relevant `Z_12 x X_12` rectangle is all six C12 E cells, so none is possible. With Z in `Z_16`, the 4-by-3 `Z_16 x Y_16` rectangle has eight C16 E cells, leaving four P cells. Thus `9<=0+4`, impossible.

These two symmetry classes cover binary A, X, Y and Z. The `3666` residual graph is therefore connected under the stated hypotheses.

## 5. `3566`: all four C12-binary locations

Let A,B,X,Y be the parties with E alphabet sizes 3,5,6,6. X and Y always have disjoint component alphabets.

* **Binary A.** Both X and Y split `3+3`. C16 cannot use only two A symbols: its degree-4 binary A symbol would require four neighbors at, for example, Y, where C16 has only three. Thus C16 uses all three A symbols, with C16 degrees `(2,3,3)` because Y has three C16 symbols. Both binary C12 A symbols are shared. Each already has C12 degree 3 and global degree at most 5, so each must have C16 degree at most 2. There is only one such C16 A symbol: contradiction.
* **Binary X or Y.** By symmetry take X binary. C12 is ternary at A,B,Y; Y splits `3+3`. As above C16 must use all three A symbols and has A degrees `(2,3,3)`. Since C12 uses all three A symbols with degree 2, their global degrees are `(4,5,5)`. The C12 A–B graph is `K_3,3` minus a perfect matching. Each of the two degree-5 A symbols sees all five global B symbols; its two C12 B neighbors are already used, so its three C16 B neighbors must be the two B symbols outside `B_12` and its unique missing symbol inside `B_12`. The missing symbols for the two degree-5 A vertices are distinct. C16 therefore uses at least these four B symbols, and at most four by its degree sum; it uses exactly four, each of C16 degree two. The third A vertex has C16 degree two. Its two C12 B neighbors are exactly the two missing symbols just mentioned, so pair-disjointness forbids those two in C16; its only available C16 B neighbors are the two outside `B_12`. Each outside B symbol would then have all three C16 A vertices as neighbors, contradicting C16 degree two.
* **Binary B.** The two C12 B symbols have degree 3, and global B degrees are at most 3, so neither is shared with C16. The union has five B symbols. C16 cannot be binary at B, because its degree 4 would require four C16 neighbors at A, which globally has only three; hence it uses the other three B symbols. X and Y each split `3+3`. The nine `X_12 x Y_16` pairs are P. For B in `B_12` there are no corresponding `B_12 x X_12` P cells, since that rectangle is full C12 E. For B in `B_16`, the `B_16 x Y_16` rectangle has eight C16 E cells out of nine, so at most one P word. There are in fact **no** B symbols unused by E, because the two disjoint component alphabets already partition the five global E symbols. Among the six physical B symbols there is one symbol outside the global E alphabet; its three pairs with `Y_16` allow at most three more P words. Thus `9<=0+1+3`, impossible.

The last distinction is important: the unused B symbol is unused by E, not a sixth member of the five-symbol E alphabet. Binary A, B, X, Y are all covered, so `3566` is connected.

## 6. `4456`: all four C12-binary locations

Write A,B,C,D for global E alphabet sizes 4,4,5,6. There are exactly 14 E values in `A x B`, hence exactly two P holes in its 4-by-4 rectangle. The two holes cannot share both a common row and a common column, because they are distinct cells. In particular A and B cannot both have global degree profile `(2,4,4,4)`: that would require the two holes to share an A row and also share a B column.

First suppose C12 is ternary at A. Its three symbols have degree 2. C16 uses between two and four A symbols, and the two component alphabets together use exactly four:

* If C16 uses two A symbols, at least one overlaps C12. Both C16 symbols have degree 4, so the overlapping global degree is at least 6, exceeding the global A bound 4.
* If C16 uses three, exactly two overlap. Each overlapping C16 degree is at most 2 and hence equals 2; the third has degree 4 by the sum eight. The global degrees are `(2,4,4,4)`.
* If C16 uses four, all three C12 symbols overlap and each of their C16 degrees is exactly 2; the fourth is also degree 2 by the sum eight. The global degrees are again `(2,4,4,4)`.

The same statement holds with A and B exchanged. Now enumerate the binary location:

* **Binary C or D.** C12 is ternary at both A and B. Both global profiles would be `(2,4,4,4)`, contradicting the two distinct holes. This covers both C and D, without treating them as interchangeable alphabet sizes.
* **Binary A or B.** By symmetry take A. Each C12 A symbol has degree 3, so it cannot overlap C16: global A degree is at most 4 and every C16 used degree is at least 2. The two disjoint alphabets together contain all four A symbols; hence C16 has exactly two A symbols, of degree 4 each. D is ternary in C12. Its component alphabets are disjoint by the established global D degree bound, so C16 has exactly three D symbols. A C16 A symbol of degree 4 cannot have four distinct neighbors among those three D symbols: contradiction. The B-binary case is the same after exchanging A and B.

Thus all four locations A,B,C,D are excluded and the `4456` residual graph is connected.

## 7. Result, first open step, and verification boundary

The arguments above exclude a split, not the surviving connected case. On each of `3566`, `3666`, `4456`, the exact next problem is to decide whether **one connected** 28-word E and the **same** 22-word P can satisfy all six pair projections and all three seven-square physical cuts, followed by the simultaneous phase equations/integral-kernel condition on that one support. Neither a separate P matching per pair nor an isolated 12-word partial gadget is such a completion. This candidate does not decide the connected cases, the split or connected cases for the other ten profiles, another `t` value, support 50 generally, or any global minimum. No counterexample to the scrutinized physical split exclusions is exhibited; no alleged nonexistence conclusion is transferred to weaker unrelated incidence relaxations.

No scientific code, solver, CAS, test, compiler, build, linter, formatter, external-model CLI, network, Git, installation or deletion was used, and no scientific source or finite program was written or run. The proof is a written nonblind reconstruction. S4's phase criterion is mentioned only as the explicitly scoped next-step interface; the connectivity proof does not require solving it. S6 is a supplied record of a local check, not a check performed by this author or an actual 22-word P completion.

## 8. Actual packet, control, and sequence coverage

I first read the required memory summary and applicable written-math protocol. I read the manifest (237 LF), freeze receipt (221 LF), final pre-dispatch binding (193 LF), parent live metadata (234 LF), actual dispatch receipt (26 LF), and all 22 manifest controls through their endings for status/permission only. Initial non-raw structural displays of the first four administrative documents elided nested lines; each was reread completely in RAW before controls and before the direct PREBODY ACK, and this presentation detail was separately disclosed to Main after the packet read. The direct PREBODY ACK named all controls and the one 536-LF packet, and was sent before packet body, mathematics, or comparison. Then the sole part was read serially RAW in windows `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–380, 381–400, 401–420, 421–440, 441–460, 461–480, 481–500, 501–520, 521–536`, including complete long lines and the ending, before research. No packet presentation or sequencing fault was observed.

For exact control coverage let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h` and `W=R/review-waves`. The complete controls were:

1. `R/prospective-author-method-scope-restoration-20261030-v1.json` (15 LF).
2. `R/contract-addendum-2-frontier-first-owner-direction-v1.json` (14).
3. `R/parent-L1-selected-diagnostic-release-quarantine-v1.json` (23).
4. `R/parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` (11).
5. `R/parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` (9).
6. `R/parent-ame-held-compression-claim-consumer-quarantine-v1.json` (8).
7. `R/parent-held-ph-registration-report-consumer-quarantine-v1.json` (49).
8. `W/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
9. `W/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (16).
10. `W/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (20).
11. `W/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (22).
12. `W/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (22).
13. `W/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
14. `W/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
15. `W/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` (24).
16. `W/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
17. `W/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
18. `W/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
19. `W/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
20. `W/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
21. `R/parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` (11).
22. `R/parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` (28).

The single declared part is `literal-packet-part-01-v1.md`, 536 LF, declared SHA-256 `36e9a77bfe0386c2f8d1c0c4782e82c70acb5ed3bf274a7c8cf76039f67bcd37`. Complete source bodies in that part, their declared logical LF coverage and declared pins are:

| ID | Packet source, relative to R | LF | Declared SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f805-ame50-t22-binary-box-and-incidence-author/author-candidate-v1.md` | 1–141 | `edbe988b6c814550d84bce78f3fef8b132c07b47af75307b990303dc953696fe` |
| S2 | `review-waves/f786-ame50-t22-same-complex-tensor-author/author-candidate-v1.md` | 1–143 | `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c` |
| S3 | `review-waves/f804-ame50-t22-phase-integer-kernel-author/author-candidate-v1.md` | 1–119 | `12d2e4c748b290b60b9cbd332473d59dc6e6fd14aca6bb1dc682bdfc07641bec` |
| S4 | `dispositions/physics-6-actual-AME50-t22-common-support-phase-integer-kernel-criterion-parent-v1.md` | 1–21 | `85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9` |
| S5 | `dispositions/physics-6-actual-AME50-t22-binary-box-component-and-alphabet-frontier-parent-v1.md` | 1–16 | `4ae01f3ce54accaff22bc43bffbad6008b8fbd46e210252ddfd6552417c016bb` |
| S6 | `review-waves/f806-ame50-t22-exact-local-gadget-finite-author/parent-t22-local-v1-run-v1-receipt.json` | 1–70 | `5e7dcce95218534c9548760142b480b874b374627c974c2db7d9b7a16bcbad30` |

The pins are declarations in the supplied metadata, not independently recomputed here. No linked original, old code, unlisted scientific source, or sibling scientific return was opened. Every genuinely held episode and every consumer remains NONINPUT. This exclusive candidate is the complete written result; subsequent corrections, if needed, require a new additive record.
