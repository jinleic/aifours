# Fresh original-input author candidate: entire actual 4555 profile

**Status: AUTHOR-CANDIDATE / UNADOPTED.** I propose the following complete written contradiction for the actual complex tensor, not a finite enumeration or a relaxation. It requires independent complete written review and parent disposition; it is not a verified theorem, kernel proof, human review, independent-model-family review, or novelty claim. The residual alphabet sizes below are a fixed profile, so no no-OLS(6) import, no-distance-one assumption, equal residual moduli, or real-sign assumption is used. The argument does not exclude other profiles, support sizes, maximal-entry counts, or prove the global AME minimum.

## Theorem candidate and same-tensor interface

There is no complex four-party AME tensor `U = 6 psi`, with local dimension six, exactly 48 nonzero entries of which exactly 24 have modulus one, and residual alphabet sizes `(4,5,5,5)`, up to physical party permutation. All three balanced flattenings of `U` are unitary.

The following interface is from the three complete, frozen original dispositions in the packet, and is included here to make all uses explicit. Let `P` be the 24 modulus-one words and `E` the other 24 nonzero words. For each physical coordinate pair `ij`, `P` projects injectively onto the complement of `R_ij = pi_ij(E)` in `[6]^2`; `|R_ij|=12`; each value in `R_ij` has exactly two extensions in `E`; and each residual balanced flattening is a union of six full nonzero `2 x 2` unitary blocks. For an appearing symbol `a` at party `i`, write `r_i(a)` for its degree in `R_ij`, independent of `j`; it has `2 r_i(a)` occurrences in `E` and `6-r_i(a)` in `P`. Every `r_i(a)>=2`, and `sum_a r_i(a)=12` at every party.

For context, the interface follows from a modulus-one entry occupying its entire unitary row and column, 24 residual entries on 12 residual rows and 12 residual columns, the strict subunit residual moduli, and orthogonality, which forbids a degree-two support cycle longer than four. These are same-tensor statements, not separately chosen pair graphs or separately selected maximal words. `P` and `E` are disjoint on **every** pair value.

Label the four-symbol party `A`, the other parties `B,C,D`; write `O_i` for the symbols absent from the residual alphabet. Thus `|O_A|=2` and `|O_B|=|O_C|=|O_D|=1`. An outside symbol appears in exactly six words of `P`, and no word of `E`.

## 1. Complete 4555 degrees, maximal histograms, and outside footprints

For `A`, every residual degree is at most 5; for each five-symbol party it is at most 4 because its neighbor set at `A` is contained in four symbols. Enumerating partitions of 12 with the above lower and upper bounds gives exactly

- `A`: `3333`, `4332`, `4422`, or `5322`;
- each of `B,C,D`: ordinary `33222` or exceptional `42222`.

These are necessary profiles before the contradiction; neither `5322` nor an exceptional five-party is assumed away. Call a degree-two symbol **low**. An ordinary five-party has three lows and two degree-three **highs**; an exceptional one has four lows and one degree-four high. Every low occurs four times in `E`.

For `w in P`, let `k(w)` be its number of coordinates in their residual alphabets and `n_k` its histogram. Since the same `P` fills the pair complements,

`sum k n_k = 6(4+5+5+5)-48 = 66`, and

`sum binom(k,2)n_k = (3*4*5+3*5*5)-72 = 63`.

Together with `sum n_k=24`, these are equivalent to

`3 n_0+n_1+n_4=3`, `n_2=3(n_0+n_4)`, and `n_3=21-n_0-3n_4`.

At most one `P` word has all four coordinates outside: the `B,C` outside pair is unique. A word with exactly one internal coordinate has three outside coordinates. Such a word whose internal coordinate is `A` uses all three outside pairs among `B,C,D`, so it cannot coexist with another such word. Otherwise its outside footprint is `Aij` for a two-subset `{i,j}` of `{B,C,D}`. Two distinct such footprints have a common five-party `i`; they must use different elements of `O_A` or duplicate the outside `Ai` pair. Three are impossible with only two elements of `O_A`. Thus `n_1<=2`. If `n_0=1`, all outside five-party pairs are already used, so `n_1=0` as also follows from the displayed identity.

Consequently the **complete** histogram list `(n_0,n_1,n_2,n_3,n_4)` is

| `n_0` | `n_1` | `n_2` | `n_3` | `n_4` |
|---:|---:|---:|---:|---:|
| 1 | 0 | 3 | 20 | 0 |
| 0 | 2 | 3 | 18 | 1 |
| 0 | 1 | 6 | 15 | 2 |
| 0 | 0 | 9 | 12 | 3 |

This also specifies **all** multi-outside footprints, including the actual outside letter at `A`. There are exactly two `Ai` outside-pair cells for each `i in {B,C,D}` and exactly one `ij` cell for each five-party pair, nine cells total. A multi-outside `P` word occupies all cells among its outside coordinates; different words cannot occupy the same cell. All cells not occupied by a word with at least three outside coordinates are occupied individually by one word with exactly two outside coordinates.

- If `n_0=1`, its footprint is `ABCD` at one `A`-outside letter `alpha`. The other three multi-outside words have footprints `Ai`, one per five-party, all at the other `A`-outside letter `beta`.
- If `n_1=2`, both three-outside footprints are `Aij`, `Aik` with distinct `i,j,k` and distinct `A`-outside letters `alpha,beta`, respectively. The remaining two-outside cells are `jk`, `A j` at `beta`, and `A k` at `alpha`.
- If `n_1=1`, its footprint is either `BCD` (internal `A`) or `Aij` at one chosen outside `A` letter. In the first case the six remaining cells are the two `Ai` cells for each five-party; in the second the six remaining cells are the four unused `Ai` cells plus the two unused five-party pair cells.
- If `n_1=0=n_0`, all nine cells occur as individual two-outside words.

For every outside letter, the number of singleton-outside words is exactly six minus the number of the just-described multi-outside words containing that letter. This also specifies all one-outside footprint multiplicities; the remaining words have no outside coordinate. It is a necessary same-`P` classification, not a claim that any listed footprint or degree pattern is physically realizable.

## 2. Twins and an unconditional low-low lemma

A **twin** at a party is a pair of different symbols occurring in two residual words that agree at the other three coordinates. For twin symbols `a,a'`, let `T` be the set of common triples. In each of the three cuts, the two residual rows indexed by `a` and `a'` and a fixed value of one other coordinate share a column. Full `2 x 2` block closure supplies their other common column. Hence the triples in `T` have three perfect matchings, one for each other coordinate. Two matching edges cannot coincide: then two triples agree in two coordinates, and their two copies at `a,a'` would give four `E` extensions of that physical pair. The graph is simple cubic.

Set `z_t = U_(a,t) conjugate(U_(a',t))`, which is nonzero. Orthogonality in every matching block gives `z_t+z_t'=0` along each edge, including for arbitrary nonzero complex moduli. Thus the cubic graph is bipartite and has at least six vertices. Each coordinate value appearing in `T` appears exactly twice. Therefore no degree-two symbol can be a twin. If a degree-three symbol is involved, `|T|=6` and its entire six-word slice is common. A degree-four slice cannot properly contain such a six-triple `T`: its remaining two triples would both use the single remaining value in each of the three coordinates and hence coincide. Thus a twin of two degree-four symbols has full common slice of size eight; a degree-three/four twin is impossible. A degree-five/three partial twin is not excluded by this argument and is handled separately below.

A five-party has maximum degree four. Consequently its only possible twin is its two degree-three highs in an ordinary `33222` profile. It is a full six-triple twin and its component has 12 words. Each other-party symbol in that component occurs there four times. Two components with twins at different coordinates are word-disjoint: a common word and its two distinct twins would provide at least three `E` extensions of the complementary physical pair.

**Low-low lemma.** If a physical pair of low symbols has two residual extensions, the two extensions differ in exactly one complementary coordinate; that coordinate is a twin.

*Proof.* They cannot agree in both complementary coordinates. Suppose they differ in both. Write the low symbols as `x,y`, the two complementary values as `c0,c1` and `d0,d1`, and the two words as `(x,y,c0,d0)` and `(x,y,c1,d1)`. Each low has only two neighbors at every other party. Pair multiplicity two, together with the impossibility of a twin through a low symbol, forces the full `x` slice

`(x,y,c0,d0), (x,y,c1,d1), (x,y',c0,d1), (x,y',c1,d0)`

and the full `y` slice

`(x,y,c0,d0), (x,y,c1,d1), (x',y,c0,d1), (x',y,c1,d0)`.

Block closure in the `(first,third)|(second,fourth)` cut adds `(x',y',c0,d0)` and `(x',y',c1,d1)`. The resulting eight words are the binary even-parity support. Each of its six pair projections is already exhausted twice, so these are closed physical blocks in all three cuts.

Let `theta_abcd` be the phase of the indicated even-parity amplitude and define

`p0=theta_0000+theta_1111`, `p1=theta_0011+theta_1100`, `p2=theta_0101+theta_1010`.

Actual nonzero two-term orthogonality in three of the closed blocks gives `p0-p1=pi`, `p0-p2=pi`, and `p1-p2=pi (mod 2pi)`. The first two imply `p1-p2=0`, a contradiction. No modulus equality between blocks or real-phase restriction was used. Hence the extensions differ in precisely one coordinate. ∎

## 3. The common maximal-pair matching for a degree-three full twin

Suppose two symbols `x,y` at one party are full twins of degree three. At each other party `i`, their common six-triple slice uses a set `N_i` of three residual symbols; put `M_i = A_i \ N_i`, where `A_i` is that party's residual alphabet, and `V_i=[6]\N_i`. The six `P` words with twin-coordinate `x` or `y` give six distinct pair values on any two other coordinates. If both those other parties have five residual symbols, then each `V_i` has three elements, namely `M_i` and the one outside symbol. Each element of `V_i` occurs once with `x` and once with `y`, so those six `P` pair values form a 2-regular bipartite graph on `V_i,V_j`. Its complement in `V_i x V_j` is a perfect matching. Since `P` and `E` have disjoint pair projections,

`R_ij intersect (M_i x M_j)` is contained in that matching. (★)

In particular, each symbol in one `M` set has at most one residual neighbor in the other `M` set. This conclusion is about the same actual `P` and `E`; it does not assert that the complement matching itself is entirely residual.

## 4. There must be a twin at the four-symbol party

Assume instead that `A` has no twin. If no five-party has a twin, the low-low lemma forbids an `E` word from having two lows among `B,C,D`. But there are at least `3*3*4=36` low-coordinate occurrences in 24 words, contradiction.

If exactly one five-party, say `D`, has a twin, then a word with low `D` cannot have low `B` or low `C`: a low-low pair would require a twin at `A` or the other five-party. Thus all at least 12 words with low `D` have high `B` and high `C`. Each of `B,C` has at most two highs, and each high-high pair has at most two `E` extensions, so there are at most eight such words. Contradiction.

Each five-party has at most one twin and each such component has 12 words; different-coordinate components are disjoint. Hence there are exactly two, say at `C,D`, and they partition `E`. Every symbol at a non-twin party occurs either zero or four times in each component. Thus all degrees at `A` and `B` are even. The degree lists force `A=4422` and `B=42222`; `C,D` are ordinary. Both degree-four symbols of `A` occur in both components, while its two lows occur one in each. Name them `a_C,a_D` according to the component. The high `C` twin pair `H_C` has `A`-neighbors the two degree-four `A` symbols and `a_C`, and the high `D` pair `H_D` has the same two high `A` symbols and `a_D`.

A full twin exhausts both its high symbols. Therefore the `C`-twin component uses only the three low symbols `L_D` at `D`, and the `D`-twin component uses only `L_C` at `C`. Its six-triple slice contains every one of those three symbols twice. It follows, with the **same** residual `E`, that

`R_CD = (H_C x L_D) disjoint-union (L_C x H_D)`.

All four pairs in `H_C x H_D` consequently occur in `P`. For a fixed `h in H_C`, its three maximal words have `D` partners `H_D` and the outside symbol `o_D`, and have `A` partners `O_A` and `a_D`. For a fixed `k in H_D`, its maximal `A` partners are `O_A` and `a_C`. Thus a maximal word on any `H_C x H_D` pair must use one of the two symbols of `O_A`. The two such words for a fixed `h` use distinct `A` symbols by `AC` injectivity and hence exhaust `O_A`. Its remaining word, with `D=o_D`, must use `A=a_D`. Both distinct `h` therefore force different `P` words with the same pair `(a_D,o_D)`, contradicting `AD` injectivity. So at least one actual twin varies `A`.

## 5. All possible four-party twins are impossible

The degree list and the twin lemma leave only: a full `3,3` twin; a full `4,4` twin; or a partial `5,3` twin. We exclude all three.

### 5.1. Full 4,4 twin

The two degree-four `A` twins have the same four residual neighbors in each of `B,C,D`. For either twin symbol there are exactly two `P` words, and at each of the other coordinates they use exactly the two-element complement of that neighbor set. Call the two triples for the first twin `000` and `111`, after independent two-symbol relabelings. Every triple for the second twin agrees with one of `000,111` in at least two coordinates, so it duplicates a physical pair already occupied by `P`. This contradicts pair injectivity. Thus a full `4,4` twin is impossible.

### 5.2. Partial 5,3 twin

Let `a` have degree five and `b` degree three, with common six-triple set `T`. The degree-five symbol has exactly one maximal word, necessarily `(a,o_B,o_C,o_D)`. Its three outside five-party pairs are now all occupied. The degree-three symbol has exactly three maximal words; each outside pair `(b,o_i)` must occur once, and no such word can have two of `o_B,o_C,o_D`. The residual `b` neighbors at each other party are precisely the three values used in `T`. Let the two remaining residual values be `b0,b1` at `B`, `c0,c1` at `C`, and `d0,d1` at `D`, labeled so the three maximal words are

`(b,o_B,c0,d0)`, `(b,b0,o_C,d1)`, `(b,b1,c1,o_D)`.

The six triples in `T` exhaust the two extensions of every `a`-pair with a `T` value, so the other four words in the degree-five `a` slice must lie in `{b0,b1} x {c0,c1} x {d0,d1}`. The three displayed maximal words forbid their pair values `(c0,d0)`, `(b0,d1)`, `(b1,c1)` from appearing in `E`. The only triples in this binary box avoiding all three forbidden pairs are `(b0,c1,d0)` and `(b1,c0,d1)`, fewer than the four distinct words required. Contradiction.

### 5.3. Full 3,3 twin: preliminary exclusions

Let `x,y` be a full degree-three twin at `A`; its component has 12 words. No five-party twin is possible. Indeed a five-party twin needs three distinct `A` neighbors, while it cannot meet either `x` or `y`: their full slices lie in the `A` component, and a common word of different-coordinate twin components violates pair multiplicity. Only two `A` symbols remain.

There cannot be a second `A` twin. A twin involving `x` or `y` and a third symbol would create a third extension of a complementary pair, so any second twin uses the other two `A` symbols. By the degree list and Section 2, it must be another full degree-three twin. Its 12-word component partitions `E` with the first, making every degree at each of `B,C,D` even. All three are therefore exceptional `42222`; call their degree-four symbols `h_B,h_C,h_D`. In each component the neighbor set at any five-party is its high symbol and two lows, and the low sets of the two components are disjoint.

Fix the first component and two five-parties, say `B,C`. Apply (★) to the *other* `A` twin: its two missing residual values at `B` and `C` are precisely the first component's two low symbols at the respective party. Thus residual edges between those two low pairs form a submatching. Each first-component low `B` symbol has two distinct `C` neighbors, both in the first component's three-symbol `C` set, so it must meet `h_C`. Both low `B` symbols exhaust the two `B` neighbors of `h_C` within that component, leaving no edge `(h_B,h_C)` there. The same applies to the other component; hence `(h_B,h_C)` is not residual. This holds for every pair among `B,C,D`.

Each high-high pair is therefore a `P` pair. Each `h_i` has only two maximal words; its `A` partners are the two outside `A` letters, and at each other five-party its maximal partners are that party's high and outside symbols. If the three high-high pairs belong to three distinct `P` words, their `A` letters must be pairwise different because each two words share one high symbol; two outside letters cannot do this. Otherwise all three pairs belong to one high-high-high word. Each high's other maximal word then has outside symbols at the other two five-parties, and all three such words must use the other outside `A` letter. Two of them share that `A` letter and `o_B`, contradicting `P` pair injectivity. A second `A` twin is impossible.

Now suppose one of `B,C,D`, say `B`, is exceptional. For any low at `C`, its two `B` neighbors include a low `B`, because `B` has only one high. By the low-low lemma and absence of five-party twins, that edge must be resolved by an `A` twin; the unique `A` twin is `x,y`. Thus every low `C` belongs to its six-triple slice, which contains exactly three `C` symbols. The same holds at `D`. Neither `C` nor `D` can be exceptional, because that would require four lows in a three-symbol slice. They are ordinary, and all their lows are exhausted by the `x,y` component. The 12 remaining `E` words then have high symbols at both `C,D`, but the four high-high pairs have at most eight `E` extensions. Contradiction. Hence all of `B,C,D` are ordinary `33222`.

### 5.4. Full 3,3 twin: ordinary five-party contradiction

For each five-party `i`, let `N_i` be the three residual symbols occurring in the `x,y` common slice, and let `h_i` be the number of ordinary degree-three highs in `N_i`. The two residual symbols outside `N_i` contain exactly `h_i` lows and `2-h_i` highs. Every low in `N_i` is exhausted by the twin component: it appears twice in `T`, with both `x` and `y`, giving its four total `E` words.

All other 12 `E` words have at most one low among `B,C,D`. Otherwise a low-low pair would require a five-party twin or an `A` twin, but no five-party twin exists and the only `A` twin is the `x,y` component. The lows outside the common slice account for `4(h_B+h_C+h_D)` of those 12 words, so

`h_B+h_C+h_D <= 3`.  (1)

If all `h_i=0`, all lows lie in the component and the remaining 12 words have highs at both `B,C`; four high-high pairs admit at most eight words. Thus at least one `h_i>0`.

Suppose, for instance, `h_B>0`, and choose a low `B` symbol outside `N_B`. It cannot meet a low at `C`, by the preceding low-low argument, so its two distinct `C` neighbors are the two highs. Among these, `2-h_C` lie outside `N_C`. By (★), its neighbors among `M_C` number at most one. Hence `h_C>=1`; likewise `h_D>=1`. Applying the same reasoning from any positive coordinate, and using (1), forces

`h_B=h_C=h_D=1`.

There is now one low outside the common slice at each five-party. For the outside low at `C`, all four of its `E` words have high `B` and high `D`. They realize all four high-`B`/high-`D` combinations once: for each high `B`, the pair with this low `C` has two extensions, and equal `D` values would give another `A` twin outside the `x,y` component. The same statement holds for the outside low at `D`, with `B,C` interchanged.

Let `h` be the unique high `B` symbol in the common slice. It occurs four times in the `x,y` component. The outside low at `C` contributes two additional words containing `h`, and the outside low at `D` contributes two more; these sets are disjoint because a remaining word cannot contain two lows. This gives at least eight `E` occurrences of `h`, whereas its degree is three and its exact occurrence count is six. Contradiction.

Sections 4 and 5 contradict every possibility for the actual tensor, completing the proposed whole-profile proof. ∎

## Provenance, chronology, and exact unpaid gates

- This is fresh author work from the frozen original packet only: S1 `1e93cfc6ff428aefbf4eb301eba7cfd6fd9b14c62a0dca254b231e41ccadc055`, S2 `3c37fb8e669de19d50317b08d363ca40165fd1817174acf1ed6e799d4558c99c`, S3 `faadf4777ac1b3f0e57d484624080a08835c9d71de980b87ad823866531f3bb4`; source hashes are the parent-supplied metadata, not a child-executed hash verification. S2's no-OLS-dependent result is not imported into this proof. S3 supplies the actual interface, not a transfer of the four-party facts of the 4455 proof.
- Before the packet, I read the complete manifest, freeze/dispatch receipts, parent metadata, and all assigned status controls; I sent the direct prebody ACK to Main. Thereafter I read the whole 97-LF literal packet in order in raw chunks `1–20`, `21–40`, `41–60`, `61–80`, `81–97`, including every source ending, before deriving. The f596 episode and all its consumers, f586/f602 held material, sibling science, linked historical scientific sources, and external sources were not opened or used. No clean-cognition certificate is claimed.
- Child scientific execution: **NOT RUN**. No scientific program, CAS, finite checker, test, build, linter, or external-model CLI was executed; no computational evidence or source code/result is claimed. A native clock observation was metadata only. The binary-box elimination and every other displayed step are written deductions, not reported experimental results.
- Exact unpaid work: independent complete reconstruction of Sections 2–5, including arbitrary-complex phase equations, the matching consequence (★), the two-`A`-twin high-high `P` contradiction, the partial `5,3` binary-box restriction, and the final high-symbol occurrence count; a separately frozen finite source may corroborate interfaces only if the parent authorizes and runs it. Parent must disposition the candidate and its imports before any adoption. No worldwide-priority or novelty audit has been performed.
