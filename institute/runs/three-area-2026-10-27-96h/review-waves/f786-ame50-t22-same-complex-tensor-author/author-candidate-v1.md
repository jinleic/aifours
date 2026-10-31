# Actual AME(4,6), N=50 and t=22: exact phase reduction and residual obstruction

**Status.** NONBLIND, same-harness GENERAL AUTHOR written candidate; not independently checked or adopted. Native clock observed before this exclusive creation: **2026-10-30T18:23:12-0700 PDT**. This is an observation before the write, not an asserted creation time. The result is an exact necessary-and-sufficient reduction of the assigned same-complex-tensor branch to a finite support/incidence and integer-kernel question, accompanied by independently written structural exclusions. It does **not** decide that finite question, exclude support 50, produce a 50-term state, establish a phase witness, or prove a global minimum of 51. In particular the 13 alphabet profiles and the two component alternatives below are necessary possibilities, not claimed realizations.

## 1. Scope and actual tensor

Let `psi` be one normalized complex AME(4,6) tensor in one local orthonormal product basis, let `U=6 psi`, and fix its same four physical parties throughout. By the AME definition all three balanced 36-by-36 flattenings of U are unitary. This return assumes exactly `N=50` nonzero coefficients, of which exactly `t=22` have modulus one in U. Let P be those 22 coefficients/words and E the remaining 28. These are the same words in all six pair projections and all three cuts; no independent graphs, phases, or bases are substituted.

A P entry exhausts its unitary row and column in every cut. Thus P is injective in each physical pair projection and no E word has any P pair value. Removing those rows and columns in a cut leaves a 14-by-14 unitary with 28 nonzeros. It has no singleton row or column, because a singleton of a unitary has modulus one. Hence every residual row and column has exactly two nonzeros. Its support is a disjoint union of even cycles. A cycle longer than four has two rows sharing exactly one nonzero column, forbidden by their complex inner product. Therefore each cut has exactly **seven full 2-by-2 unitary blocks**. Equivalently every physical pair has precisely 14 E values, each with exactly two E extensions, and 22 distinct P values, each with exactly one P extension. All 36 pair values occur. The zero-excess block conclusion uses only elementary complex unitarity, not a global t bound, no-OLS, or an assumed equal-modulus ansatz.

For each physical pair `ij`, let `M_ij` take an E word to its unique other E extension of that pair value. Each `M_ij` is a fixed-point-free involution. For complementary pairs `ij|kl`, the two involutions commute and generate a four-word block; they cannot give the same mate, because two distinct words cannot agree in all four coordinates. These are actual operations on one E, not abstract independently chosen matchings.

## 2. Full complex amplitudes reduce exactly to flat residual amplitudes

Write `U_w=sqrt(p_w) z_w` for `w in E`, where `0<p_w<1` and `|z_w|=1`. Every actual pair line gives

    p_w + p_{M_ij w} = 1.                                      (1)

For one of the 21 actual square blocks, order its rows and columns arbitrarily and call its entries `a,b,c,d` in the usual arrangement `[[a,b],[c,d]]`. The row and column norm equations give `|a|=|d|` and `|b|=|c|`. Row orthogonality is therefore **equivalent** to

    z_a z_d + z_b z_c = 0.                                    (2)

This is a phase equation; it is generally false that the unnormalized products `a d` and `-b c` are equal when the two squared magnitudes differ. P phases are arbitrary, since their rows and columns are isolated in every cut.

Conversely, suppose one common support P,E satisfies the pair-line and seven-square conditions in Section 1 and phases `z_w` satisfy (2) for **all 21 squares in all three cuts**. Setting every E coefficient to `z_w/sqrt(2)` and every P coefficient to any modulus-one number makes every square a complex Hadamard unitary and every singleton unitary, simultaneously in the same tensor. Thus every flattening is unitary. The resulting U has squared Frobenius norm `22+28/2=36`, so `U/6` is normalized. Therefore an arbitrary-modulus tensor with this exact support exists **if and only if** its residual support admits the displayed simultaneous phase system; in the positive direction all residual moduli may be chosen `1/sqrt(2)`. This is a reduction, not an assertion that the phase system has a solution.

For the original arbitrary tensor, the agreement graph on E has an edge between two words sharing at least two physical coordinates. Each edge gives (1). On each connected component, either an odd cycle forces all `p_w=1/2`, or the graph is bipartite and the squared moduli alternate between `p` and `1-p`. This follows by following (1) along paths. It is not needed to assume that every original modulus is flat in order to justify the flat-representative reduction above.

## 3. An exact integer phase obstruction, including the converse

Take any proposed P,E satisfying the incidence conditions of Section 1. For each of its 21 squares choose any ordering of rows and columns. Form the integer matrix `A` of size 21-by-28, with the square's row having `+1` at its two diagonal E words, `-1` at its two off-diagonal E words, and zero elsewhere. Changing an ordering may negate a row, which does not change the criterion below. Writing `z_w=exp(2 pi i theta_w)`, equations (2) are exactly

    A theta = (1/2) 1    in (R/Z)^21.                           (3)

**Integer-kernel criterion.** The support is phase-realizable in all three cuts if and only if

    for every y in Z^21 with A^T y=0,  sum_j y_j is even.         (4)

Necessity is immediate by multiplying (3) by `y^T`: the left side is zero and the right side is `sum(y)/2` modulo one. For sufficiency, use integer unimodular matrices V,W putting A into Smith normal form `V A W = D`, with nonzero diagonal entries followed by zero rows. Since multiplication by any nonzero integer is surjective on `R/Z`, the transformed equations are soluble exactly when the zero rows of `V(1/2)1` vanish modulo one. Those rows of V form an integer basis for `ker_Z(A^T)`: every integer left-kernel vector is their integer combination because V and its inverse are integral. This is exactly (4).

Consequently an **explicit odd-sum integral dependency** `A^T y=0`, `sum y` odd, is a complete phase obstruction for that proposed support. Conversely, absence of such a dependency proves existence of common complex phases, without solving a separate modulus system. It is essential that the dependency be an exact **integer** kernel vector; a left-null vector merely modulo two is not generally sufficient. No matrix for the assigned 28-word branch was enumerated or solved here.

To make the frontier literal rather than hide it behind a relaxation: a support-50/t-22 tensor exists exactly when there are sets `P,E subset [6]^4` with `|P|=22`, `|E|=28`, each P pair projection injective, each E pair value occurring twice and disjoint from P, each of the three E cut graphs a union of seven `K_2,2`s, **and** (4) for their common 21-by-28 A. These are finite exact conditions on the same physical words. The current return supplies no P,E meeting them and no proof that every P,E violates them.

## 4. Actual binary-box obstruction and component structure

For any choice of two local symbols in each party, an actual E has **at most seven** words in their 2-by-2-by-2-by-2 box. Indeed each of its four pair values in any chosen pair has at most two E extensions, so at most eight words fit. If eight fit, all four pair values in every physical pair occur exactly twice inside the box and are saturated there. The common binary subtensor is then a closed 4-by-4 unitary block in each of the three cuts; dividing it by 2 gives a normalized four-qubit AME state.

Here is a complete elementary contradiction for that last assertion, not an imported no-OLS claim. Trace out one qubit. The resulting three-qubit density matrix has all one- and two-qubit marginals maximally mixed, so its Pauli expansion is `rho=(I+M)/8` with M a real linear combination of weight-three Pauli strings. Its nonzero Schmidt eigenvalues are `1/2,1/2`, hence `rho^2=rho/2`, or `M^2=3I+2M`. Two weight-three Pauli strings can multiply to a weight-three string only if they differ in all three places; then they anticommute, so their anticommutator cancels. The weight-three part of `M^2` is zero, forcing M=0, a contradiction. This pays all three cuts and arbitrary complex phases, not just a binary support count.

As a concrete exact phase obstruction within this general lemma, suppose the eight even-parity binary words all occur in a box. In the square-matrix notation of Section 3 the following are rows for the indicated cuts, with a word standing for its standard basis vector:

    AB|CD:  0000 + 1111 - 0011 - 1100 = r1,
    AC|BD:  0011 + 1100 - 0110 - 1001 = r2,
    AD|BC:  0000 + 1111 - 0110 - 1001 = r3.

They obey `r1+r2-r3=0`, an exact integral dependency with coefficient sum one, so (4) rules it out. This is an illustrative eight-word obstruction, not a proposed 28-word E or global witness.

Now let C be a connected component of the E agreement graph. It is closed under all six `M_ij`. Each complementary pair of involutions partitions C into four-word squares; hence `|C|` is a multiple of four. For a symbol x used at party i within C, let `s_i^C(x)` be its number of C words and `d_ij^C(x)` the number of partners at party j. Each used pair value has both extensions in C, so `s_i^C(x)=2 d_ij^C(x)` for every j. Write this common degree `d_i^C(x)`. It is at least two: degree one would fix all other coordinates, leaving only one word, whereas its pair value has two extensions. Also `sum_x d_i^C(x)=|C|/2`.

A four-word component would have only one used symbol in every party, by the last inequality, but two pair values, impossible. An eight-word component has at most two symbols per party; its four pair values force exactly two per party and fill an eight-word binary box, impossible by the preceding paragraph. Therefore every component has at least 12 words. Since E has 28 words, the only possibilities are

    one 28-word component;  or  two components of sizes 12 and 16.  (5)

For the 12-word component, each party has at most three symbols and every pair needs six values; up to party permutation its alphabet profile is exactly a **necessary** `2333` or `3333`. In `2333` its two-symbol party has degrees `3,3` and each three-symbol party has degrees `2,2,2`; in `3333` all degrees are `2,2,2`. For a 16-word component each pair needs eight values and each alphabet has at most four symbols, so the only necessary profiles, up to permutation, are `2444`, `3333`, `3334`, `3344`, `3444`, `4444`. Pair values of distinct agreement components are disjoint. None of these profile listings is a realization or a complete feasibility classification.

A local 12-word construction shows why (5) alone is not a contradiction. Let `i` range over Z/3 and use three symbols 0,1,2 in A,B,C and two symbols 0,1 in D. Put `L_i=(i,i,i)` and `R_i=(i,i-1,i+1)`. Give `(L_i,0),(L_i,1),(R_i,0)` amplitude `1/sqrt(2)` and `(R_i,1)` amplitude `-1/sqrt(2)`; all other entries of this partial tensor are zero. In each of A,B,C, every symbol occurs in exactly one L and one R, and every pair among A,B,C identifies one of the six triples. Thus in each of the three cuts the six active rows and six active columns are three actual 2-by-2 Hadamard blocks. Its agreement graph is connected: each L meets each R in exactly one of A,B,C, and each triple also has its two D entries. This is a **12-word partial unitary gadget only**; its remaining rows and columns are zero, it has no 22-word P completion here, and it is not an AME or a 50-word phase witness.

A useful local corollary for the actual E is that two different degree-two symbols at the same party cannot have the same two-element neighbor set in **each** of the other three parties: together their four-word slices would give eight words in one binary box. For a degree-two symbol, its four partner triples form either a parity tetrahedron of a binary cube, or two tied coordinates with the third free. This follows because the three balanced 2+2 partitions of the four words are either all distinct or exactly two coincide; all three coinciding would yield only two distinct words. In the parity case every pair of its four words agrees in the fixed party and one other party, so (1) forces all four squared magnitudes to `1/2`. The tied-coordinate alternative is not silently discarded.

## 5. Necessary global E-alphabet profiles and three sharp subcases

Let `X_i` be the E-used symbols at party i, `q_i=|X_i|`, and for `x in X_i` let `d_i(x)` be its common E degree in another party. Each E pair value has exactly two extensions, so `s_i(x)=2d_i(x)` and the same degree-one argument gives `d_i(x)>=2`. Each pair system has 14 E values, hence

    sum_x d_i(x)=14,    3 <= q_i <= 6,    q_i q_j >= 14.       (6)

For a P word w let `k(w)` count its coordinates in their corresponding E alphabets, and let `n_k` be the number of P words with that count. Since the 36 pair values are partitioned into P and E, every used symbol x occurs in exactly `6-d_i(x)` P words, and every `X_i x X_j` contains exactly `q_i q_j-14` P cells. Therefore

    sum_k n_k = 22,
    S1 := sum_k k n_k = 6 sum_i q_i - 56,
    S2 := sum_k binom(k,2)n_k = sum_{i<j} q_i q_j - 84,
    3n_0+n_1+n_4 = 66 - 2 S1 + S2 >= 0.                        (7)

The nonnegative expression excludes, up to permutation, `3555`, `3556`, `4444`, `4445`, `4446`, and `4455`. For instance its value is `-2` for `444q`, `-1` for `4455`, `-2` for `3555`, and `-1` for `3556`. In view of (6), the remaining **necessary**, not necessarily realizable, profiles are exactly

    3566, 3666, 4456, 4466, 4555, 4556, 4566,
    4666, 5555, 5556, 5566, 5666, 6666.                        (8)

The following refinements use the same actual tensor and are recorded without claiming any of these profiles survives the phase system.

* `3566`: the three-symbol party's degrees are `4,5,5`, the five-symbol party's are `2,3,3,3,3`, and each six-symbol party's are `2,2,2,2,3,3`, because all degrees are bounded by the partner alphabet sizes. Here `S1=64`, `S2=63`. Since two parties use all six symbols, every P word has `k>=2`; (7) then gives `(n_0,n_1,n_2,n_3,n_4)=(0,0,3,18,1)`.
* `3666`: each six-symbol party again has degrees `2,2,2,2,3,3`; the three-symbol party has one of `2,6,6`, `3,5,6`, `4,4,6`, `4,5,5`. Since every P word has `k>=3`, `S1=70`, `S2=78` give `(n_0,n_1,n_2,n_3,n_4)=(0,0,0,18,4)`.
* `4456`: `S1=58`, `S2=50`, so (7) gives `(n_0,n_1,n_2,n_3,n_4)=(0,0,8,14,0)`. For a fixed value of the six-symbol party, each of the two unused symbols in each four-symbol party and the one unused symbol in the five-symbol party occurs in exactly one P word with it: five outside-alphabet incidences. Each P word has at most two such incidences, so at least three P words occur at that value; hence its E degree is at most three. Its degree multiset is consequently `2,2,2,2,3,3`. Each four-symbol party has degrees `2,4,4,4` or `3,3,4,4`; the five-symbol party has degrees `2,2,2,4,4`, `2,2,3,3,4`, or `2,3,3,3,3`.

The exact unresolved work is to decide, for the common P,E on each remaining profile and component alternative, whether an odd integral square dependency must occur, or else produce and check actual P,E and phases satisfying the exact criterion. None of (5), (8), the local gadget, or the box theorem alone supplies that decision. No numerical, solver, executable, finite-enumeration, independent-family, human, kernel, or parent result is implied.

## 6. Inputs, controls, exact coverage, and SHA pins

The actual dispatch confirmation arrived directly from Main before any file was read. I then read the entire actual dispatch receipt, manifest, prepared metadata, freeze receipt, final binding, and all **22** listed controls through their endings, using controls for status/permissions only. Before any body, I sent Main the direct PREBODY ACK naming 22 controls, the single ordered part's 404 LF, and that no body, mathematical research, or comparison had occurred. The part was then read serially in raw windows `1-20,21-40,41-60,61-80,81-100,101-120,121-140,141-160,161-180,181-200,201-220,221-240,241-260,261-280,281-300,301-320,321-340,341-360,361-380,381-400,401-404`, including complete long lines and the ending, before research/comparison. No presentation or sequence failure is known. It contains complete bodies S1 `1-29`, S2 `1-29`, S3 `1-31`, S4 `1-161`, S5 `1-132`.

The body pins below are the packet/manifest-declared source SHA-256 values. I did not open the linked original source paths or claim an independent roundtrip; the parent freeze/binding reports that check. No packet-body scientific conclusion is imported as an unproved premise of Sections 1-5; the elementary facts and four-qubit obstruction used there are reconstructed above.

* S1 `physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md`: `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0`.
* S2 `physics-6-actual-ame49-t28-entire-same-complex-tensor-exclusion-parent-v1.md`: `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a`.
* S3 `physics-6-actual-ame49-t23-through-t27-exclusion-and-t28-frontier-parent-v1.md`: `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0`.
* S4 `f745-ame49-excess-component-and-t28-frontier-proof-author/author-candidate-v1.md`: `ac4f6284549678e0e0430242baed238230680b74a0f1facbd8e8e1cd99691181`.
* S5 `f744-ame49-t25-whole-same-tensor-proof-author/author-t25-reconstruction-v1.md`: `c852a533a2e26cd2b7bcf37f38827c63511544d7b5d1a9e98b5454ac7b7f2b3a`.

After the complete packet read, metadata-only SHA-256 observations with `openssl dgst -sha256` were:

* Manifest `d84435a27025235783b165418482adf5fe5e6ed9259fe6140c137aa925dc0d62`.
* Freeze receipt `4c6e14f8267e55cdf289d418aafde0aec9efa7735553d1473628e0536b1250b3`.
* Final pre-dispatch binding `bdfd8356ee553a9c446be148ac025fc39aeba6b8775fbd5c07c4c6708af5328a`.
* Prepared metadata `0f62a2dd8c42d707344450e81ddcab68504bbb8c3ff8ec511bf9e8ad4d99ef2c`.
* Actual dispatch receipt `0fef927cbc6d02d06047dcf5310fbd5d25198ee40dceadec6fd850bc96aced2f`.
* Complete 404-LF packet part `564667431351ec1b2b91c4b469866ee6d425fb91ca50e7dcc8d205e4c88ad4db`.

For the 22 controls, let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h` and `W=R/review-waves`. The complete files read, in manifest order, and their observed SHA-256 pins are:

1. `R/prospective-author-method-scope-restoration-20261030-v1.json` — `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95`.
2. `R/contract-addendum-2-frontier-first-owner-direction-v1.json` — `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`.
3. `R/parent-L1-selected-diagnostic-release-quarantine-v1.json` — `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f`.
4. `R/parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` — `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc`.
5. `R/parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` — `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4`.
6. `R/parent-ame-held-compression-claim-consumer-quarantine-v1.json` — `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0`.
7. `R/parent-held-ph-registration-report-consumer-quarantine-v1.json` — `97fbd5967b472783c5ed860f0745b88d7917eb93e1c340f043c974a531ac1453`.
8. `W/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `74f9f9d57eb5866f68dec331b9bf4facca2bc8d4116186cd241b3bff1539dfee`.
9. `W/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `d00f41bf0205680ef8256f38c97d2023058da935c260ba5cc7f17cb77bd8e184`.
10. `W/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `f6ccc5fa10f0e30536921ea86828c437359869413919eae258cbbd82d4989805`.
11. `W/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `649349cfe636c88e60bee96400512ae6db8d8e12b875d3d100fcce3312785fd8`.
12. `W/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `cb9a81b76acaf740e2d691664e57e46a274c208f44fb071f5f0724973ae1a1a8`.
13. `W/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `e4d3dca7c41456e4e48dc154719b1df9e653b656b2cbf9324c82b195e3539681`.
14. `W/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json` — `df412094a47e89be2507d7a7809d68449f08476aabfaca44fd9ecb4dce2a40b8`.
15. `W/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` — `3f4b2c6d31a420ecff35a6478ce7a302637765b1203c046619715eda634b6927`.
16. `W/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `a85930a9b268d472d5ded2f31b4b9916394e99f97e854c3a3869a9c8fd7ec8de`.
17. `W/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `9aaf84aabb3ea428e3622c5e6b7961d21bd3f1a8b3a16a727be203077e784462`.
18. `W/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `abf867950e1425ed74e1a766f6838957b255694cf0f64e936a23321c1324913b`.
19. `W/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json` — `f5007a354d6acb8335ad2b9cc170f457c542640e1bbd15c5439d69d0c76039ab`.
20. `W/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json` — `7dc07513bb05a7b08ba9795b566f38c39750a8f71fc68d576ea4367d4b0e4c38`.
21. `R/parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` — `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c`.
22. `R/parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` — `27390c73fd6741217ce1d86c5f41e388ef87e3f51b306565053943e0333afbce`.

Hashes are metadata observations, not source-identity authentication or a cognition/separation certificate. All genuinely held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remain NONINPUT. No outgoing links, old code, sibling returns, or unspecified scientific files were opened. No scientific code, interpreter, solver, test, build, lint, formatter, external-model CLI, network, Git, installation, or deletion was run. No scientific source was created. The only commands were metadata hashing and native clock observations. All mathematical assertions above are written, unreviewed author claims; any correction must be a new additive record, with no overwrite or backdating.
