# Actual AME(4,6), N=50/t=22: binary boxes, components and physical incidence

**Status and scope.** This is a NONBLIND, same-harness GENERAL AUTHOR written candidate, not an independently reviewed or parent-adopted result. Everything mathematical below concerns ONE normalized complex AME(4,6) tensor in ONE local orthonormal product basis, with `U=6 psi`, exactly 50 nonzero entries and exactly 22 modulus-one entries. No support-50 witness, global support bound, novelty, priority, human/family/kernel verification or parent adoption is asserted. In addition to reconstructing the frozen claims, I give written arguments that (i) a 12-word component must be the stated `2333` gadget, up to the displayed relabelings and phases, and (ii) an actual tensor on each of profiles `3566`, `3666`, `4456` must have a connected 28-word residual agreement graph. These are new **unreviewed conditional claims**, not decisions of those profiles.

## 1. Common physical incidence and exact phase interface

All three balanced flattenings of the same `U` are 36-by-36 unitaries. Let `P` be the 22 modulus-one entries and `E` the other 28 nonzeros. A P entry exhausts its row and column in each cut, so its pair value is unique, different P words have different values in each physical pair, and no E word uses a P pair value. Deleting these singleton rows and columns leaves, in each cut, a 14-by-14 unitary with 28 entries. It has no singleton row or column: a singleton in a unitary would have modulus one. Thus every row and column has degree exactly two. A connected degree-two bipartite support is an even cycle; a cycle longer than four has two rows overlapping in exactly one nonzero column, contradicting their complex orthogonality. Consequently each cut consists of exactly seven full 2-by-2 unitary blocks.

Equivalently, for each of the six physical pairs there are 14 E pair values, each occurring twice, and 22 P pair values, each occurring once. Together these cover all 36 values. The six pair systems, their pair mates and all block equations are on the SAME 28 physical E words. If `C` is an agreement component, any pair value occurring in C has both its extensions in C and cannot also occur in another component.

For an E entry write `U_w=sqrt(p_w) z_w` with `0<p_w<1` and `|z_w|=1`. Every pair mate satisfies `p_w+p_mate=1`. In any square `[[a,b],[c,d]]`, row and column norms give `|a|=|d|`, `|b|=|c|`; orthogonality is exactly the phase relation `z_a z_d + z_b z_c=0`. This is **not** the generally false unnormalized relation `a d + b c=0`.

For a proposed common support, orient its 21 squares and let A be the 21-by-28 integer matrix with entries +1 on a square's diagonal and -1 on its off-diagonal. Common phases exist precisely when `A theta=(1/2)1` in `(R/Z)^21`, equivalently

    for every y in Z^21 with A^T y=0,  sum(y) is even.             (1)

Necessity is immediate. For sufficiency, integer unimodular row and column transformations give Smith normal form. Nonzero diagonal multiplication is onto `R/Z`; each zero row imposes that its integer left-kernel vector have even sum. Those zero rows form an integer basis of the full left kernel. An odd-sum **integral** dependence is therefore a phase obstruction; an arbitrary mod-two null vector alone need not be. Conversely, if the common pair incidence and seven-square conditions hold and (1) holds, using the resulting phases with every E modulus `1/sqrt(2)` and arbitrary unit-modulus P phases makes all three cuts unitary; `U/6` is normalized since `22+28/2=36`. Thus this is an exact existence interface, not a claimed solution of it.

## 2. Eight-word binary box: actual closure and complex contradiction

Choose two symbols in each physical party. Any selected pair has four possible pair values, each with at most two E extensions, so the box contains at most eight E words. If it contained eight, every one of those four values in **every** physical pair would have two box extensions, exhausting that value globally. Consequently in each balanced cut the four corresponding rows and four corresponding columns have no nonzero outside the selected 4-by-4 submatrix; the same complex submatrix is a unitary block. It has squared norm 4, so dividing the restricted four-party tensor by 2 gives a normalized four-qubit state with all three two-qubit marginals maximally mixed. In particular this uses actual common closure and all three cuts, not a one-cut support mask or an assumed flat phase pattern.

For a self-contained contradiction, trace out one qubit. The resulting three-qubit density matrix has all one- and two-qubit marginals maximally mixed and, by the Schmidt spectrum of the omitted qubit, obeys `rho^2=rho/2`. Its Pauli expansion is `rho=(I+M)/8`, with M a real linear combination of weight-three Pauli strings. Hence `M^2=3I+2M`. Two weight-three strings can have a weight-three product only if they differ at all three local factors; they then anticommute, so their two cross terms cancel. Squares are scalar. Thus the weight-three part of `M^2` is zero, forcing `M=0`, contrary to the scalar equation. Therefore every actual binary box contains **at most seven** E words, for arbitrary complex phases.

For comparison with the integral phase criterion, if the eight even-parity binary words occurred then the following are actual square rows for `AB|CD`, `AC|BD`, `AD|BC`:

    r1 = 0000 + 1111 - 0011 - 1100,
    r2 = 0011 + 1100 - 0110 - 1001,
    r3 = 0000 + 1111 - 0110 - 1001.

Here `r1+r2-r3=0`, with odd coefficient sum 1. This example is not used to assert that every eight-word box has this particular support; the preceding closure/Pauli proof covers every box.

## 3. Components and the 12-word component, completely paid

For a physical pair, its unique other E extension is an involution. In any complementary cut the two involutions act as row and column flips on a square, commute, and generate its four distinct words. Therefore every agreement component C is a union of four-word orbits and `|C|` is divisible by four.

For a symbol x of party i in C let `d_i^C(x)` be its number of pair-neighbors in any other party. Since each used pair value has exactly two extensions and both lie in C, its occurrence count is `2d_i^C(x)`, independent of the other party, and `sum_x d_i^C(x)=|C|/2`. Every used degree is at least two: degree one in each other party would fix all coordinates, contradicting the two distinct extensions. A four-word component is impossible. An eight-word component has at most two symbols per party; its four pair values force two symbols in every party, placing all eight words inside a forbidden binary box. Thus the only component-size alternatives for the 28 E words are

    one component of size 28; or two components of sizes 12 and 16.    (2)

For size 12, each party uses at most three symbols, and each pair needs six values. Its only possible sorted local alphabet profiles are `2333` and `3333`. Every symbol in a ternary party has degree 2; a binary party has two degree-3 symbols.

### 3a. Pure-incidence exclusion of a 12-word `3333` component

Each of its six pair graphs is 2-regular on 3+3 vertices, hence the full 3-by-3 graph minus a perfect matching. Fix a symbol in one party. Its four words use two symbols twice in each of the other three parties. Any 2-by-2 rectangle of a 3-by-3 graph minus a perfect matching contains a missing cell: two matched columns must meet any chosen set of two columns. Therefore, for each pair of the other parties, their two balanced 2+2 partitions of these four words cannot be distinct, since distinct partitions would realize all four cells. All three partitions must coincide, leaving only two distinct triples, contradicting four distinct words. No phase or finite enumeration is used. Thus a 12-word component must have profile `2333`.

### 3b. Its physical support, phase constraint and gadget

Write the ternary parties as A,B,C and the binary party as D. Their pair graphs among A,B,C again are 3-by-3 minus perfect matchings, while each D-versus-ternary graph is the full 2-by-3 rectangle. Fix `A=a`. As above, the B and C 2+2 partitions of the four words must coincide. Distinctness then forces D to take both its values in each of the two resulting ABC triples. Hence the component is `T x {0,1}`, where T has six triples and each AB, AC, BC value identifies at most one triple; each symbol in A,B,C occurs in exactly two triples.

Form the graph on T joining two triples sharing one ternary coordinate. It is a simple 3-regular graph on six vertices: the three edges at a triple are distinct because no two triples share two coordinates. Each graph edge gives an actual 2-by-2 block with the two D values. Writing `r_t=z_(t,0)/z_(t,1)`, its phase equation gives `r_t=-r_t'`. An odd cycle is therefore impossible. A simple 3-regular bipartite graph on six vertices is `K_3,3`. Its two classes L and R each contain every ternary symbol exactly once. Relabel the symbols so

    L_i=(i,i,i),       R_i=(i,i-1,i+1),       i in Z/3,                (3)

possibly interchanging B and C. Indeed, relative to the L class the B and C coordinates of the R class must be the two opposite nonidentity 3-cycles; an equal choice would make two triples share two coordinates. This proves necessity of the displayed gadget support, rather than merely exhibiting one selected construction.

Conversely this support really is a local partial unitary in **each** cut. Let `0<p<1`, let `eta` and all `v_t` be arbitrary unit phases, and set

    U_(L_i,0) = sqrt(p) v_(L_i),       U_(L_i,1) = sqrt(1-p) eta v_(L_i),
    U_(R_i,0) = sqrt(1-p) v_(R_i),   U_(R_i,1) = -sqrt(p) eta v_(R_i).

For any shared ternary symbol the corresponding two triples form a full 2-by-2 unitary with the two D values; these are three disjoint blocks per cut, up to transposition. The local agreement graph is exactly `K_3,3` on triples with a vertical D flip, i.e. `K_3,3 square K_2`, and is connected. Its bipartition makes the squared magnitudes alternate between p and 1-p. Conversely, the preceding block equations give precisely this common phase-ratio form and the same alternating moduli, up to choosing which side carries p. The other physical rows and columns of this **partial** tensor are zero: there is no claimed P completion, AME state, or 50-word witness.

For a 16-word component the pair count is eight, all degrees are at least two, and each party has at most four symbols. The necessary local profiles, sorted, are `2444,3333,3334,3344,3444,4444`. A binary party has degrees `4,4`; a four-symbol party has `2,2,2,2`. A three-symbol party has `2,3,3` when another component party has three symbols. In the sole-three-symbol case `3444`, its degrees may instead be `2,2,4` or `2,3,3`; neither alternative is silently discarded. No realization of the entire 16-word component is claimed.

## 4. Whole-alphabet and P-moment restrictions

Let `X_i` be the E-used alphabet in party i, `q_i=|X_i|`, and `d_i(x)` the common degree of an E-used symbol. The actual pair incidence gives

    sum_x d_i(x)=14,    d_i(x)>=2,    3<=q_i<=6,    q_i q_j>=14.      (4)

For the lower bound on q, two symbols would have total degree at most `2*6=12`. A used symbol x occurs in exactly `6-d_i(x)` P words; an unused symbol occurs in six. Let `n_k` count P words using E-alphabet symbols in exactly k positions. Each `X_i x X_j` contains `q_i q_j-14` P pair values. Hence

    sum n_k = 22,
    S1 := sum k n_k = 6 sum_i q_i - 56,
    S2 := sum binom(k,2)n_k = sum_(i<j) q_i q_j - 84,
    3 n_0+n_1+n_4 = 66-2 S1+S2 >= 0.                              (5)

Sorted profiles allowed by (4) are `3555,3556,3566,3666`; `4444,4445,4446,4455,4456,4466,4555,4556,4566,4666`; and `5555,5556,5566,5666,6666`. The right side of (5) is -2 for `3555` and each `444q`, and -1 for `3556` and `4455`. Thus the complete list surviving these stated necessary restrictions is

    3566, 3666, 4456, 4466, 4555, 4556, 4566,
    4666, 5555, 5556, 5566, 5666, 6666.                              (6)

This list is not a claim that any listed profile has a completion.

* **3566.** Degrees are `4,5,5` at the three-symbol party, `2,3,3,3,3` at the five-symbol party, and `2,2,2,2,3,3` at each six-symbol party. Here `(S1,S2)=(64,63)` and two full alphabets force `n_0=n_1=0`; (5) and the first moment give `(n_2,n_3,n_4)=(3,18,1)`. The 3-by-5 E pair graph is full except for one cell; the missing P cell is between the degree-4 and degree-2 symbols. If A is the three-symbol party and B the five-symbol party, the P outside masks among A,B have counts both outside 3, A only outside 15, B only outside 3, neither outside 1. The three both-outside words use the three distinct unused A symbols, by P-pair injectivity.
* **3666.** Each six-symbol party has degrees `2,2,2,2,3,3`; the three-symbol degrees are one of `2,6,6`, `3,5,6`, `4,4,6`, `4,5,5`. Here `(S1,S2)=(70,78)` and `(n_3,n_4)=(18,4)`, with smaller n zero. For any symbol x of a six-symbol party, all three pairs with the three unused symbols of the three-symbol party are P. Thus x has one additional all-inside P occurrence exactly when its E degree is 2. The four all-inside P words therefore use each of the four degree-2 symbols exactly once at **each** of the three six-symbol parties; these are common P words, not three independently chosen matchings.
* **4456.** Here `(S1,S2)=(58,50)` and `(n_0,n_1,n_2,n_3,n_4)=(0,0,8,14,0)`. At a fixed value of the six-symbol party the two unused symbols of each four-symbol party and the one unused symbol of the five-symbol party give five P incidences. Every P word has at most two outside-alphabet coordinates, so there are at least three P words there, and its E degree is at most three. Consequently its degrees are `2,2,2,2,3,3`. Each four-symbol party has degrees `2,4,4,4` or `3,3,4,4`; the five-symbol party has `2,2,2,4,4`, `2,2,3,3,4`, or `2,3,3,3,3`. The two four-symbol parties **cannot both** have `2,4,4,4`: their 4-by-4 pair graph has just two missing P cells; both profiles would require the two cells to lie in one common row and also in one common column, impossible for two distinct cells. More precisely the holes either share a row, share a column, or share neither, giving degree-profile pairs `(2444,3344)`, `(3344,2444)`, or `(3344,3344)`.

For the last profile, if A,B are the four-symbol parties, C the five-symbol party and D the full six-symbol party, all P outside masks are determined. Counts for exactly one of A,B,C outside are respectively `6,6,2`; counts for exactly two outside are `AB:4, AC:2, BC:2`. For example, the single-C count is the two P cells inside `X_A x X_B`, while the outside-A and outside-B counts follow from their 12 outside incidences each. For a fixed D value, its five outside incidences occupy either three P words (two double-outside and one single-outside) or four P words (one double-outside and three single-outside), according as its E degree is 3 or 2.

## 5. New written refinement: the three displayed profiles cannot split 12+16

The following argument uses actual pair-value disjointness, P coverage/injectivity and the 12-word structure, not separate per-cut designs. Write C12 and C16 for the hypothetical components and `X_i^12`, `X_i^16` for their local alphabets. At a shared symbol their degrees add, since their pair-neighbor sets are disjoint. In each of `3566`, `3666`, `4456`, the global degree at every six-symbol-party value is at most 3. Every C12 and C16 used degree is at least 2. Therefore at such a party the two component alphabets are disjoint. As their union has six symbols, a ternary C12 alphabet forces a ternary C16 alphabet there, and a binary C12 alphabet forces a four-symbol C16 alphabet there.

We repeatedly use the following literal counting principle. If X and Y have disjoint C12/C16 alphabets, every pair in `X^12 x Y^16` is a P pair, because it is an E pair in neither component. Distinct such pairs require distinct P words. For a third party Z whose two component alphabets are disjoint, these words can be partitioned by whether their Z symbol belongs to `Z^12`, `Z^16`, or is unused by E. P-pair injectivity bounds each class by the number of available P cells in, respectively, `Z^12 x X^12`, `Z^16 x Y^16`, and the unused-Z cross pairs. All counts below are for these actual P cells.

### 5a. `3666`

If the binary party of C12 is the global three-symbol party, all three six-symbol parties have `3+3` disjoint component alphabets. Choose them as X,Y,Z. The nine P pairs in `X^12 x Y^16` would require at most three words with Z in `Z^12` (nine possible cells minus six C12 E cells) and at most one with Z in `Z^16` (nine minus eight C16 E cells). No Z symbol is unused: `9 <= 3+1` is impossible.

If instead the binary C12 party is one of the full parties, take that party for Z and the other two full parties for X,Y. Now `|Z^12|=2`, `|Z^16|=4`, and both X and Y split `3+3`. The C12 rectangle `Z^12 x X^12` is completely E, while `Z^16 x Y^16` has eight E cells among twelve. The same nine cross P pairs would give `9 <= 0+4`, impossible. Thus `3666` has one 28-word component.

### 5b. `3566`

Call the global parties A,B,X,Y with alphabet sizes 3,5,6,6. At X,Y the component alphabets are disjoint.

* If C12 is binary at A, then its X and Y alphabets are ternary, so C16 has three symbols at each. C16 cannot have two A symbols, since a binary C16 party has degree 4 and needs at least four symbols at every partner. It has all three A symbols with degrees `2,3,3`. Both A symbols shared with the binary C12 contribute degree 3 there, and their global degree is at most 5; each corresponding C16 degree would have to be at most 2, but there is only one such symbol. Contradiction.
* If C12 is binary at one six-symbol party, say X, it is ternary at A,B,Y, while C16 has four X symbols and three Y symbols. Again C16 must use all three A symbols, with degrees `2,3,3`; the C12 A/B graph is 3-by-3 minus a perfect matching. The two A symbols of global degree 5 see all five B symbols. Each already sees two distinct C12 B-neighbors, so its three C16 B-neighbors are the two B symbols outside `B^12` plus its unique missing `B^12` symbol. The two missing symbols are distinct. Thus C16 uses at least these four B symbols; it uses at most four, hence exactly these four, each with C16 degree 2. The third A symbol cannot use either of the two shared B symbols in C16, because both are already its C12 neighbors. Its C16 degree is 2, so it uses both outside B symbols. Each outside B symbol now has all three A neighbors, contradicting C16 degree 2.
* If C12 is binary at B, its two B symbols have degree 3. Since global B degrees are at most 3, they cannot overlap the C16 B alphabet; hence C16 has three disjoint B symbols, with one B symbol unused by E. The two full parties split `3+3`. The nine pairs in `X^12 x Y^16` are P. With B in `B^12`, none is possible because `B^12 x X^12` is all E; with B in `B^16`, at most one is possible because the 3-by-3 C16 B/Y graph has eight E cells; with the single unused B symbol, at most three are possible by its B/Y pairs. Thus `9 <= 0+1+3`, a contradiction.

All possible locations of the binary C12 party are exhausted, so `3566` has one 28-word component.

### 5c. `4456`

Let A,B be the four-symbol parties. Suppose C12 is ternary at one of them, say A. Its three A symbols have C12 degree 2; global A degrees are at most 4. C16 cannot use two A symbols: any overlap would have degree at least `2+4>4`. If C16 uses three A symbols, exactly two are shared, and each shared C16 degree must be 2. Their remaining C16 symbol has degree 4 because the degree sum is 8, so the global A degrees are `2,4,4,4`. If C16 uses four A symbols, all C12 A symbols are shared and each C16 degree is 2, giving the same global profile `2,4,4,4`.

Both A and B cannot have that profile by the two-hole argument in Section 4. Thus the binary C12 party must be A or B. At that binary party, C12 degree is 3 while global degree is at most 4, so no symbol can also occur in C16. The global alphabet has four symbols, hence C16 has two there. Its degree-4 symbols force four C16 symbols in every other party. At the full six-symbol party C12 is ternary; its three symbols plus C16's four must overlap, but any overlap has global degree at least 4, contradicting the established bound 3. Thus `4456` also has one 28-word component.

These three connectivity results do **not** rule out the connected cases. They also do not decide whether any of the other ten profiles admits a split or a completion.

## 6. Literal remaining frontier

For every profile in (6), the connected 28-word case remains unresolved here. For the other ten profiles `4466,4555,4556,4566,4666,5555,5556,5566,5666,6666`, the `12+16` possibility also remains unless independently excluded. In that split, the 12-component must have the explicitly derived `(3)` support and compatible block phases; the 16-component must use one of the stated necessary local profiles. Every pair projection of the two components must be disjoint, and all missing pair values must be simultaneously covered by the **same** 22 P words. The squares lie within agreement components, so in this split phase compatibility of the canonical 12-component is paid locally; the 16-component phase system and the common P completion remain unproved.

The exact decision is still: find common physical sets P,E with 22 and 28 distinct words, respectively, satisfying all six pair partitions and all three seven-square decompositions and the integral criterion (1), or prove that no such common sets satisfy all of them. Neither the 13-profile sieve, the connectivity refinements, the local gadget, nor a per-cut support survivor settles this question. No numerical assay, finite enumeration, solver result or phase witness is reported.

## 7. Frozen inputs, controls, sequence and limitations

Main's direct finalized-receipt notice preceded reading the actual dispatch receipt. I read the complete manifest, freeze receipt, final binding, parent metadata and all 22 listed status/permission controls before sending Main a direct PREBODY ACK naming 22 controls and the ordered 250-LF packet. I then read the sole packet serially, in RAW windows `1-20,21-40,41-60,61-80,81-100,101-120,121-140,141-160,161-180,181-200,201-220,221-240,241-250`, including the ending and complete long lines, before doing mathematics or comparison. An initial administrative final-binding read used a mistyped home-directory path and failed; the correct complete binding was read before the ACK. No other presentation or sequencing failure is known. Memory summary and the applicable research/acceptance skill instructions were read before the direct notice; they were not mathematical sources.

The declared packet part SHA-256 is `d3c36d2bf9c1ed8e3eaff5e9f1df74cc81e83b6c7d52779b23ba47ea50f90a86`. Its complete-body inputs, declared source pins and source logical line coverage are:

1. S1 `f786-ame50-t22-same-complex-tensor-author/author-candidate-v1.md`, LF 1-143, `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c`.
2. S2 `physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md`, LF 1-29, `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0`.
3. S3 `physics-6-actual-ame49-t28-entire-same-complex-tensor-exclusion-parent-v1.md`, LF 1-29, `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a`.
4. S4 `physics-6-actual-ame49-t23-through-t27-exclusion-and-t28-frontier-parent-v1.md`, LF 1-31, `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0`.

The 22 controls are exactly the complete `controls_before_body` list in this wave's `manifest-v1.json`: the prospective-method and frontier-direction records; L1, privacy, core-Gram, AME and PH quarantine records; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660 and f662 quarantine records; the remaining-d0 process-major record; and the f746/f749 prerun-correction record. They supplied status and permission boundaries only. Every genuine held episode and every method, selection, planning, proof, verification, reporting, confidence and downstream consumer remains NONINPUT. No held source or sibling scientific return was opened.

Pins above are the manifest/packet declarations, not hashes independently recomputed here, a source-identity certificate, or a claim about private cognition. The freeze/binding records report their own administrative checks. No old code, unlisted scientific source, network, Git, deletion, installation, scientific interpreter/solver/CLI, test, compile, build, lint, or scientific execution was used. No finite source was created. The exclusive creation of this candidate is an administrative file write, not a scientific run. All proofs and new refinements remain author claims pending a separately scoped independent check and parent disposition.
