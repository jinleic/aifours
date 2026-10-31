# Author candidate: conditional support-48 composition and the small-support boundary

**Status: NEW AUTHOR CANDIDATE; NOT ADOPTED.** The support-48 composition below is proved *conditional on the literal imported statements identified in §2*, not re-proved from their unavailable full original sources. The N=45 and N=46 count reductions and the exact N=46 system are new written deductions in this candidate, not prior dispositions. No scientific execution was performed by this child. No current global minimum, N≥49, witness, novelty, original-source identity, independent-model-family/human/kernel verification, or clearance of an old constrained-WRITTEN gate is claimed.

## 1. Exact caller and notation

For every normalized complex AME(4,6) state ψ and every product basis, let N be the number of nonzero coefficients and let t be the number of coefficients of modulus 1/6. Put U=6ψ. For each of the three balanced 2|2 partitions of the **same** four physical parties, the corresponding 36×36 flattening of U is unitary. Conversely, the latter three unitary conditions imply the AME two-party conditions for ψ=U/6. Let P be the same set of t modulus-one coefficients of U, and E its other N−t nonzero coefficients. All claims below allow arbitrary complex amplitudes, all product bases and physical-party permutations; no independent choice of a graph or amplitudes for each cut is allowed.

In any cut a modulus-one entry exhausts its entire row and column. Thus P projects injectively onto each of the six physical pair coordinate systems; no E pair value is used by P. Removing P's singleton rows and columns in a given cut leaves a unitary n×n submatrix, n=36−t, containing all N−t E entries. Every remaining row and column has degree at least two: a degree-one line would have its sole entry of modulus one and would already have belonged to P. Define its row excess

    e=(N−t)−2(36−t)=N+t−72 ≥ 0.                 (1)

The entire tensor U, including the same P and E and the same amplitudes, is carried through every application below.

## 2. Literal scientific imports and their precise scope

Only the complete assigned packet S1–S9 is used. The following are *premises from those records*, not independent reauthentication of the linked original proof bodies. The explicit source IDs and hashes in §9 are the parent-supplied packet bindings.

* **Global maximal-count boundary, S6:** S6 states: “f113 gives t≤29 and [the no-exactly-29 disposition] excludes t=29 for any support; hence every normalized complex AME(4,6) state in every product basis has at most 28 coefficients of modulus 1/6. Conditional on the f113 provenance only.” S6 explicitly describes that provenance as the classical no-OLS(6) theorem **and** the prior t≤30 boundary. Neither the original f113 chain, the earlier t≤30 theorem, nor the classical source is independently authenticated here. Algebra below often states the sharper local assumption t≤28 directly; using S6 to supply it retains all of these upstream conditions.
* **The t=24 alphabet interface, S1:** “The separately adopted f296/f293 no-distance-one and no-six-symbol composition gives q_i∈{3,4,5} under no-OLS(6).” It applies to N=48, t=24 and the same physical E. We do not import an unrestricted six-word selection lemma, and we do not replace this conditional interface by an unconditional alphabet claim.
* **The six fixed-profile consumers, S1:** for the same actual U/P/E and arbitrary nonzero complex residual amplitudes, the separately adopted theorems exclude each entire profile 3555, 4444, 4445, 4455, 4555, 5555, up to physical-party permutations. S1 says these six standalone profile theorems do not themselves require no-OLS. Their individual original bodies are not in the packet: this candidate imports the six exact assertions as reported in S1, not new complete proofs of them.
* **The t=27 consumer, S7:** “No normalized complex AME(4,6) state in ANY product basis has exactly48 nonzero coefficients, of which exactly27 have modulus1/6.” S7 specifies the same tensor, arbitrary complex amplitudes and no no-OLS mathematical prerequisite. Section 5 reconstructs its incidence consumer, conditional on its explicitly imported local excess-three structure; the full standalone theorem is still an import.
* **The t=28 consumer, S4:** “No normalized complex AME(4,6) tensor in any product basis has exactly48 nonzero coefficients, exactly28 of modulus1/6.” S4 states its complete same-tensor written exclusion uses neither no-OLS nor f113 nor a real/equal-amplitude/phase restriction. We import that theorem at exactly this scope; the packet's compressed case summary is not a complete independent reproof of every alphabet case. Section 6 independently proves its binary-block consumer, not the entire t=28 theorem.
* **N=47 consumer, S6:** S6's composition excludes support 47 for every normalized complex AME(4,6) state in any product basis, conditional on its f113 provenance. This is separate from, and unnecessary for, the no-48 theorem.
* **Prior lower/upper record, S6:** S6 records lower bound 45 and known 60, and says “the minimum support now lies in {45,46}∪[48,60] at these imports”; it does not exclude either 45 or 46. Its underlying lower-bound and 60-state source chains are not provided or reauthenticated here. They are additional assumptions when used in §8, not consequences of no-48 alone.

S5's literal support-48 count conclusion is “t is one of24,27,28” at the adopted t≤28/no-OLS boundary. Section 4 reconstructs it from unitarity and the explicitly assumed t≤28 rather than silently importing a stronger unconditional upper bound.

## 3. Unitary-support lemmas (proved here)

Use the bipartite graph of the nonzero entries of a square unitary. Two distinct rows, and likewise two distinct columns, cannot have exactly one common neighbor: their inner product would be one nonzero complex product. Every connected component has equally many rows and columns. Indeed, after grouping its rows and columns it is a rectangular block with both orthonormal rows and orthonormal columns, so each side's size is at most the other. Every component has nonnegative excess, the sum over its rows of degree−2.

**Zero excess.** Every row and column has degree two. If two rows meet, no-one-overlap makes their two-neighbor sets identical. The common two columns each have degree two, so the component is exactly a full 2×2 block. Hence a zero-excess residual has even order and consists entirely of full 2×2 blocks.

**Excess one is impossible.** In such a component exactly one row R has degree three and all other rows degree two. Every degree-two row meeting R must use two of R's three columns. Distinct two-subsets of a three-set intersect once and are forbidden as two row supports, so all those rows use the same pair. The third column of R then has no other neighbor, contradicting its degree at least two.

**Excess two has order three.** If one row R has degree four and every other row degree two, every low row meeting R uses a two-subset of its four columns; different such subsets must be equal or disjoint. Minimum column degree forces at least two distinct disjoint pairs. A column from each pair has only R as a common neighbor: a low row meeting both would overlap either pair-row exactly once. This contradicts column orthogonality.

Otherwise there are exactly two degree-three rows R,S. Their three-element supports cannot meet in one point. If they meet in two, a degree-two row needed at the column private to R must also use a column of R; that second column lies in S, giving a forbidden one-point overlap with S. If they are disjoint, every low row meeting a column of R must use two of R's columns, and the component containing R cannot reach S, contrary to connectedness. Thus their supports coincide. Every low row attached there uses two of the same three columns, and all such pairs must coincide; no edge can leave these three columns. Squareness forces exactly three rows and three columns, namely R,S and one low row. The support is a 3×3 block with one missing entry. Consequently, a residual of total excess two has precisely one such 3×3 component and all other components full 2×2; its order is odd. These arguments use complex unitarity only, not no-OLS or any assumed equal residual magnitudes.

## 4. Same-tensor composition for every support-48 state

Assume N=48 for one actual ψ and use the S6 t≤28 premise. Equation (1) gives e=t−24, so t≥24. At t=25, excess one is impossible. At t=26 the residual order n=10 is even, whereas the excess-two lemma requires odd order. Thus the exact possible count branches are

    t∈{24,27,28}.                                    (2)

This proves the count map in S5 within its stated boundary. It does not assert a branch is realizable.

For t=24 the residual in every cut has order 12 and zero excess, hence is six full 2×2 blocks. For every physical pair, E occupies exactly 12 pair values, each with two E extensions, and P occupies the other 24 pair values exactly once. Let A_i be the alphabet used by E in party i, q_i=|A_i|. The S1 alphabet import gives q_i∈{3,4,5}. Each A_i×A_j contains the 12 E pair values, so two q_i cannot both equal three.

For w∈P let k(w) count its coordinates lying in the respective A_i. For any symbol x in A_i, if p_i(x) is its number of occurrences in P, then the number of E-partners of x in any other party is 6−p_i(x). Summing over A_i gives 12, independently of the other party. All 36 pair values are occupied by exactly one of P or the E projection. Therefore, for the same P and E,

    C = Σ_{w∈P} k(w) = 6Σ_i q_i − 48,
    M = Σ_{w∈P} binom(k(w),2) = Σ_{i<j} q_i q_j − 72.  (3)

For k=0,1,2,3,4, binom(k,2)≥k−1 and binom(k,2)≥2k−3. Since |P|=24, M≥C−24 and M≥2C−72. The only sorted profiles with one 3, apart from 3555, are excluded as follows:

    profile       C     M       violated inequality
    3444         42    12       M ≥ C−24 = 18
    3445         48    23       M ≥ C−24 = 24
    3455         54    35       M ≥ 2C−72 = 36.

The remaining sorted profiles are exactly 3555, 4444, 4445, 4455, 4555 and 5555. The six literal S1 whole-profile imports exclude each profile for this very U/P/E. Therefore t=24 is excluded conditional on the stated no-OLS alphabet interface and those six imports, but **not** on f113 or the t≤28 bound when considered as a standalone branch. The t=27 and t=28 branches are excluded by S7 and S4 respectively, each at its own standalone unitary scope.

**Conditional all-48 result.** Under the S6 t≤28 boundary with its f113/no-OLS/prior-t≤30 provenance, the S1 conditional alphabet and six fixed-profile assertions, and the S7 and S4 branch theorems, no normalized complex AME(4,6) state in any product basis has support 48. This is a complete logical composition at those exact imported boundaries; it is not a new source-independent proof of all of those imports. The t=27 and t=28 branch theorems do not themselves inherit f113 or no-OLS just because the union composition does.

## 5. Independent reconstruction of the t=27 incidence consumer

This section does not pretend to prove the entire imported S7 branch from first principles. It takes S7's exact local support lemma as an import: at N=48,t=27 each residual cut has one full 3×3 core and three full 2×2 blocks. Hence its nine residual pair values have multiplicities three on a set H_ij of three values and two on the other six, and H_ij×H_kl is the complete set of core words in the complementary cut.

For a physical-party symbol x let d_i(x)=6−p_i(x), s_i(x) be its occurrences in E, and h_i(x)=s_i(x)−2d_i(x). In each pair system this equals the number of incident high values; hence it is independent of the partner party and Σ_x h_i(x)=3. If high symbols a,b in two distinct parties had h_i(a),h_j(b)≥2, the Cartesian core in the crossed partition would contain h_i(a)h_j(b)≥4 different words with pair (a,b), but a residual pair has at most three extensions. Thus at most one party can have a high marginal at least two.

Suppose such a symbol a has h_i(a)=m≥2. The other three parties each have three distinct high symbols of marginal one, and their mutual high-pair graphs are perfect matchings. Choose a high neighbor b of a in party j. For every one of the m distinct high neighbors c of a in party k, let d be the matching partner of c in H_kl. The Cartesian H_ij×H_kl core contains the word (a,b,c,d). Since (a,c) is high, the complementary pair (b,d) is also high in the ik|jl cut. Distinct c give distinct d, so b has at least m high neighbors, contradiction. Therefore all positive h_i equal one and each party has exactly three high symbols.

For any two parties i,k and any high symbols a,c, their matching partners b,d give the core word (a,b,c,d). Thus all nine high×high pairs occur in E. There are exactly nine residual pair values, so these are all of them. Hence each high symbol has d_i=3 and p_i=3, and no P word can contain high symbols in two coordinates. The 4×3 high symbols have 36 P incidences, impossible among 27 P words with at most one such incidence each. This reconstructs the S7 high-marginal contradiction for the same tensor; the excess-three structure remains the explicit import stated at the start of this section.

## 6. Independent four-qubit closed-block consumer, and what it does not prove

A normalized four-qubit AME state cannot exist. Its three-qubit marginal ρ has two nonzero eigenvalues, both 1/2, and all one- and two-qubit marginals are maximally mixed. In the Pauli basis, ρ=(I+M)/8 where M is Hermitian and contains only weight-three Pauli strings. The spectral identity ρ²=ρ/2 gives M²=3I+2M. A product of two weight-three strings has weight three only if they differ at all three sites; in that case the two strings anticommute, so their symmetrized contribution to M² vanishes. Squares have weight zero. Thus the weight-three part of M² is zero, forcing M=0; the scalar part then contradicts M²=3I.

In an actual AME(4,6) tensor, suppose two selected symbols per party have the following stronger property: for each of the six physical pairs all four pair values occur in E and **all** their E extensions lie in the same 2×2×2×2 subarray. No P entry uses any of these pair values. In any balanced cut, the four corresponding rows have all their support in the four corresponding columns. Full-unitary row orthogonality makes that 4×4 submatrix unitary; its columns have no support outside those rows. This holds in all three cuts for the same subarray. Dividing it by 2 would produce the impossible four-qubit AME state. Merely finding occupied pair boxes, or closure in one cut, is not enough.

S4 uses a substantially larger, imported same-tensor alphabet case analysis to establish the relevant contradictions for *all* t=28 states. The paragraph above verifies only its closed-binary-block consumer; it does not fill or independently certify the whole S4 alphabet analysis.

## 7. NEW count corollaries for N=45 and N=46

These deductions use only the unitary-support lemmas of §3 and the explicit local hypothesis t≤28; they are not prior adopted statements.

**No N=45 under t≤28.** Equation (1) gives e=t−27, so 27≤t≤28. If t=27, n=9 and e=0, contradicting the even order of a zero-excess residual. If t=28, e=1, which is impossible. Thus no normalized complex AME(4,6) state in any product basis can have N=45 and t≤28. This single theorem is conditional on t≤28; using S6 to assert it for all such states retains f113, classical no-OLS(6), and the prior t≤30 boundary. It is a **new unadopted extension**, not an assertion that S6 already excluded 45.

**N=46 forces t=26 under t≤28.** Here e=t−26, so 26≤t≤28. At t=27, excess one is impossible. At t=28, e=2 but n=8 is even, contrary to §3. Thus t=26. In every cut the same E has 20 words and its residual matrix has order 10 and zero excess: five full 2×2 blocks. Accordingly every physical pair has exactly ten E pair values, each with exactly two E extensions; P has the other 26 pair values, each once.

A further necessary alphabet restriction follows without no-OLS. Let A_i and q_i describe this actual E, and let d_i(x)=6−p_i(x) be its number of partners in any other party. For x∈A_i, the two-extension property gives s_i(x)=2d_i(x), and Σ_{x∈A_i}d_i(x)=10. If d_i(x)=1, all E words containing x use the same single partner in each of the other three coordinates, hence there can be at most one such word, contradicting s_i(x)=2. Therefore 2≤d_i(x)≤6 and 2≤q_i≤5. Each pair box contains ten E values, so q_iq_j≥10.

As in (3), for k(w) counting E-alphabet coordinates in w∈P,

    C=Σ_P k = 6Σ_i q_i−40,
    M=Σ_P binom(k,2) = Σ_{i<j}q_iq_j−60,
    M≥2C−3·26.                                      (4)

If any q_i=2, the pair-box inequalities force sorted profile 2555. It has C=62 and M=45, contradicting M≥46 in (4). Two q_i cannot equal three since 3·3<10. Hence every actual N=46,t=26 tensor has, up to party permutation, one of exactly the following **necessary** residual-alphabet profiles:

    3444, 3445, 3455, 3555, 4444, 4445, 4455, 4555, 5555. (5)

No profile in (5) is claimed feasible, and the list does not prove N=46 impossible.

## 8. Exact unpaid N=46 system and the lower-bound consumer

The following finite complex system is equivalent to an N=46,t=26 state, not just to separate cut-wise graph feasibility. Let Ω={0,1,2,3,4,5}⁴. Choose disjoint P,E⊂Ω with |P|=26 and |E|=20. Require the P projection to every one of the six physical pairs to be injective, and require no E pair projection to meet a P pair projection. For each of the three partitions ij|kl, form the bipartite graph whose left and right vertices are the ten pair values not occupied by P and whose edges are the words of E. Require that graph to be the disjoint union of five complete 2×2 blocks. Choose one shared complex number z_w, 0<|z_w|<1, for each w∈E. In **every** one of the 15 blocks across the three cuts, the 2×2 matrix made from those same z_w must be unitary. Give every word in P an arbitrary modulus-one amplitude and set all other tensor entries to zero.

Necessity follows from §7. Conversely, for each cut, the constructed flattening is a direct sum of 26 modulus-one singleton blocks and five unitary 2×2 blocks, so it is unitary. The same single tensor therefore gives a normalized AME state after division by 6. The unresolved mathematical step is to prove or refute existence of P, E and one common set of z_w satisfying **all** these constraints, including all three pairings simultaneously; (5) only narrows its support alphabets. In particular, locally realizable support graphs, a separate amplitude choice in each cut, and a partial Boolean witness cannot discharge this actual physical caller.

From (1) and t≤28 one has N≥44. Combining the new no-45 result with the conditional S6 no-47 theorem and §4's conditional no-48 theorem yields, for every state under the named imports,

    N ∈ {44,46} ∪ {49,50,...}.                         (6)

If the *additional* S6-recorded prior lower bound N≥45 is admitted at its own original boundary, (6) becomes N∈{46}∪{49,50,...}. If in addition the S6-recorded existence of support 60 is admitted, its conditional minimum lies in {46}∪[49,60]. The underlying lower/upper source chains were not supplied here. These are explicit conditional implications, not a claim that the current global minimum is established or scanned. No-48 alone gives no N≥49: the prior record leaves 45 and 46, and the new conditional argument eliminates 45 only; the exact N=46 system above remains unpaid. Even without using the prior N≥45 record, (1) leaves N=44 at t=28, which this candidate does not exclude.

## 9. Provenance, corrections, chronology and assurance

Parent-supplied manifest and freeze hashes are respectively 263ce247d46019ca0963c2bba7b1ceedbe1a985eaf2c773631ce54a2e6110643 and 4fdb43e34506eb68a771378a4107c8d942e9dd8c7a3a8507712acff55bf4c588. Parent-supplied packet hash is 1c6f94d350a4846ed47e33bb9ef347315c345d021d43431725720d310be9f7bc. Assigned complete-body source bindings S1–S9, in order, are:

    S1 5a9e9128b964051bd667f04fc05ad8b289f1034992422a4666bc76e681fc9880
    S2 cb94f545d8497bff4cabfe8454decacd68c95534c4270820d0628fc10ca03ade
    S3 fcd489d9c04a5c9520159519d7f3c0cae14830e8d356a077ddfcb13f0bb9a918
    S4 25c34705825561d501701a26b50c08a7b734bf2282f72f3283568c8cb459f968
    S5 2af4fde719fbee23fa740160792e152945bd6e352e9006a77f7817c1949fe9aa
    S6 4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003
    S7 fa3e4f124b17621ec7e9be91df0c6f1073f47fd91151be2e9b146c9ed577a4a2
    S8 f6b3afbd63d6771a2483fbc8b83bdfc2c5913f6d5e475b9511ea88146ca0687d
    S9 e1c391362ad0d0493f1189753279706f61590fc52adacca803bd754960763ab2.

S2 corrects S1's incorrect claim that the parent had fully read all eleven underlying source dispositions before writing S1; S3 records ONE parent PROCESS MAJOR and does not backdate that read. S7 records the f316 attempted-ACK failure and later direct delivery after packet reading and derivation; its owner reconciliation does not turn that into a timely ACK or a cognitive-isolation certificate. S4 and S8 retain ONE f682 author source-provenance PROCESS MAJOR for an in-place proof edit: the initial write was recovered and hashed later, the operative correction was not a compliant additive correction, and no held-science inference follows. S8's pre-disposition parent-read limitation is a contemporaneous earlier status, while S4 reports the later prospective parent intake; no read is backdated. S9 corrects the unsupported general q=3 degree claim: (2,2,4) is also possible from the raw degree constraints, and the unique star is justified only in the specified 3344 case, not generally in 3444. These facts neither independently prove S4 nor convert any prohibited episode into an input.

Chronology: I first read the assignment manifest through its full research_task and ending, freeze receipt, prepared parent metadata, actual dispatch receipt, and all 20 status/permission controls through their endings. I sent Main a direct PREBODY ACK before opening the science packet. Then I read packet LF 1–251 in order, in raw windows of at most 20 LF, including all S1–S9 endings, before doing the written deductions in this candidate. The metadata hashes above are parent-supplied observations, not child-computed hash checks. I did not follow packet links, inspect older authors' code, sibling proofs, held history or held mathematics, run a calculation, solver, test, build, formatter, external model, or scientific child executable. All genuinely held episodes and all their proof/method/selection/planning/confidence/verification/reporting consumers remain NONINPUT. Parent's S4 finite run is historical parent-reported local corroboration only, not child execution and not an all-tensor enumeration.

A native clock was observed as 2026-10-30T16:24:35-0700 PDT before creation of this file; this is not a claimed filesystem-creation instant. The candidate is self-contained for its new algebra and composition **given the fully enumerated theorem imports**, not a claim of independent reconstruction of their missing full proofs. Any review, adoption, source authentication and stronger global lower bound are separate unpaid acts.
