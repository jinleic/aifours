# Actual N=50, t=28: whole-tensor common-hole and closed-block exclusion

**Status: proposed written author reconstruction, NONBLIND, same harness; not a review or a parent disposition.** The following argument concerns one normalized complex AME(4,6) state, in one fixed local orthonormal product basis, with arbitrary nonzero complex coefficients and arbitrary phases. Write its coefficient tensor as ψ and U=6ψ. Let N be the number of nonzero coefficients and t the number with modulus one. The proposed conclusion is that **N=50 and t=28 cannot both hold for that same tensor**. Every quantifier below refers to that actual U and its three balanced unitary flattenings; no independent cut masks are selected. The proof includes a written reconstruction of the per-cut lemma, rather than using the incomplete finite order-eight search. It does not establish a global N=50 exclusion, a lower bound of 51, a witness, novelty, priority, human/model-family review, or formal verification. Parent and disjoint reviewers must decide the candidate.

The argument is nonblind: packet S1 already proposes this exclusion, and S2/S4 discuss the cut lemma. I reconstruct the necessary claims below from the displayed actual-unitary interface. S2 mentions f810/f811/f812, but their bodies were not inputs, and neither their correctness nor any partial finite output is imported. The entire cut proof used here is written below; if any part of it fails scrutiny, the downstream result remains conditional on the precisely stated cut lemma in §2, not an unconditional exclusion. No other missing load-bearing theorem, global t bound, no-OLS assertion, source link, computational enumeration, or phase ansatz is used.

## 1. Same U, pair lines, and all alphabet profiles

Assume for contradiction N=50,t=28. Every 36×36 two-versus-two flattening of U is unitary. Let P be its 28 modulus-one four-coordinate words and E its other 22 nonzero words. In every flattening, an entry of modulus one exhausts its entire row and column. Thus each of the six physical coordinate-pair systems partitions its 36 pair values into 28 distinct P values and eight E values; no P and E words share a pair value. Deleting the P rows and columns leaves an 8×8 unitary, with 22 E entries and no row or column of degree one: such a line would contain another modulus-one entry. Its total excess over two entries per residual row is 22−16=6. Each E pair value consequently has at least two extensions, in every pair system.

For party i, let Q_i be the actual symbols occurring in E, q_i=|Q_i|. For x∈Q_i, let s_i(x) be its number of E occurrences and d_ij(x) its number of distinct E partners in party j. Because each of the six possible j-symbols gives either an E pair value or a P pair value, the number of P occurrences with i-symbol x is 6−d_ij(x), independent of j. Therefore d_ij(x)=d_i(x) for all j≠i. Define h_i(x)=s_i(x)−2d_i(x). Pair-line multiplicities are at least two, so h_i(x)≥0 and, for every i,

    Σ_{x∈Q_i} d_i(x)=8,             Σ_{x∈Q_i} h_i(x)=6.            (1)

Also d_i(x)≥2. Indeed, if it were one, x would have exactly one partner in each of the other three coordinates, hence at most one E word, while its E pair line has at least two distinct extensions. Thus q_i≤4. The eight distinct E values in pair ij all lie in Q_i×Q_j, so q_iq_j≥8; in particular q_i≥2, and q_i=2 forces the other three q's to be 4.

Now count the *same* P words, not six independent projections. Let n_k be the number of P words with exactly k of their four coordinates in the corresponding Q alphabets. P has 6q_i−8 incidences with Q_i, and q_iq_j−8 incidences with Q_i×Q_j. Hence

    Σ n_k = 28,
    Σ k n_k = 6Σ_i q_i − 32,
    Σ C(k,2)n_k = Σ_{i<j} q_iq_j − 48,
    n_0+n_3+3n_4 = 12−6Σ_i q_i+Σ_{i<j}q_iq_j.               (2)

The last line follows by weighting n_k by 1−k+C(k,2), which is 1,0,0,1,3 for k=0,…,4. For 3333 the right side is −6, and for 3334 it is −3. If a q is 2, the other three are 4; otherwise every q is 3 or 4 and the two just excluded profiles are exactly those with fewer than two 4's. **At least two parties have q=4.** This handles all q and all surplus distributions, including 2444, rather than assuming a particular alphabet profile.

## 2. Necessary cut lemma, including actual-unitary boundaries

**Lemma.** In each actual balanced cut, the residual 8×8 unitary support is either

* F: two full 3×3 components and one full 2×2 component; or
* B: one connected 4×4 component with 14 nonzeros, plus two full 2×2 components.

The two zeros in B can share a row, share a column, or be in different rows and columns. This is a per-cut necessity, not a simultaneous three-cut existence assertion.

For completeness, here is the written derivation. Every connected support component of a unitary is square: after permuting rows and columns, its row orthogonality gives #rows≤#columns and its column orthogonality gives the reverse. Every line has degree at least two. Two distinct rows, or two distinct columns, cannot have exactly one common nonzero, because their inner product would have one nonzero term.

If a connected component has order m>2, a degree-two row supported in columns c,d forces c,d to have identical row neighborhoods, by the no-single-overlap rule for rows. Both columns have degree at least three: degree two for both would give an isolated 2×2 unitary, since its two columns already span their two common rows. Two degree-two rows have disjoint pairs of columns: a one-column overlap is forbidden, while equal pairs give two orthonormal rows spanning those columns and hence an isolated 2×2 unitary. These twin/isolation facts also hold on transposing. If the component has excess e=#nonzeros−2m and k degree-two rows, its other m−k rows each contribute at least one excess unit, and its 2k distinct twin columns each contribute at least one. Therefore

    k≥m−e,             2k≤e,             m≤e+floor(e/2).            (3)

A zero-excess component is a full 2×2 block: it is 2-regular on both sides, and any row sharing one neighbor with another must share both, isolating that block. Excess one is impossible. Excess two gives order three and 3×3 minus one entry. For excess three, (3) gives order at most four; at order four, exactly one row is low and three have degree three. Its twin columns have degree three and share two of the three high rows, leaving a high row avoiding both with at most two possible neighbors, contradiction. Thus excess three is a full 3×3 block.

**Excess four.** At order five there are one or two low rows. With one, all four high rows have degree three; the twin columns have degree three or four, so some high row avoids them and uses all three other columns. A high row meeting the twins has exactly one other neighbor, giving a forbidden one-overlap with the avoiding row. With two low rows, all four twin columns have degree three. Their high neighborhoods are two-subsets of three high rows; they cannot intersect once, so coincide, leaving the remaining high row at most one neighbor. At order six there are exactly two low rows and two low columns; all other lines have degree three. The low columns have disjoint two-high-row neighborhoods A,B, partitioning the four high rows. Each low-row twin pair has high neighborhood A or B. Equal choices leave the other two high rows with only one neighbor; different choices disconnect the component. Thus excess four, if present, has order four.

**Excess six, order six.** Let k be the number of low rows, 0≤k≤3.

* k=3: the six twin columns all have degree three. Their high neighborhoods are two-subsets of the three high rows, pairwise not meeting in one; they coincide, leaving a high row empty.
* k=2: the degrees of the two twin pairs are either (3,3) or (4,3), writing one degree per pair. In the first case, their two-high-row neighborhoods must be disjoint A,B: if equal, the two other high rows have at most two neighbors. The remaining two columns avoid the low rows, meet each of A,B in zero or two positions, and have total degree six; their degrees are 2 and 4. A row of A and a row of B then meet exactly in the degree-four column. In the second case, the two remaining columns are low and have disjoint two-high-row neighborhoods A,B partitioning the four high rows; the degree-four twins have three high neighbors and meet one of A,B exactly once. Both cases contradict no-single-overlap.
* k=1: the k=2,3 exclusions also apply after transposition, so there is at most one low column. The twins therefore both have degree three: if there is no low column, all columns are cubic, and if there is one, at most one high column has degree four. Their two high rows have identical neighborhoods, because any other column avoids the low row and meets a twin in zero or two places. The five high-row degrees are 3,3,3,3,4, so the two equal degrees are 3. Their one further common column cannot meet any other row without a one-overlap; the resulting 3×3 subcomponent is isolated, contrary to connectedness.
* k=0: transposition of the preceding exclusions forbids low columns, so all rows and columns are cubic. If two rows have the same three neighbors, the three remaining incidences on those columns must come from a third identical row, isolating a K3,3. Otherwise all row neighborhoods are distinct. A fixed row has six total intersections with the other five rows, each intersection being 0 or 2; exactly two other rows are disjoint from it. A three-subset of six columns has only one disjoint three-subset, forcing those two rows to have identical neighborhoods. Contradiction.

**Excess six, order eight.** Each side has two or three low lines by (3). With three low rows, their six twin columns use all six column-excess units and are cubic; the two other columns are low, avoid those rows, and have disjoint two-subset neighborhoods A,B among the five high rows. Each twin has two high neighbors and cannot meet A or B once, so it uses all A or all B. The fifth high row is empty. Transposition excludes three low columns. Thus there are exactly two low rows and columns and every other line is cubic. Let the low-column neighborhoods be disjoint two-sets A,B, with Z the other two high rows. Each low-row twin pair has high neighborhood A, B, or Z. A Z row must have degree three, so at least one twin pair uses Z; both cannot use Z. If the other uses A, each B row needs both remaining high columns in addition to its low column. Both Z rows need one of those columns, and no-single-overlap with a Z twin forces them to use the same one. That column then has at least four neighbors, not three. The case B is symmetric.

Finally, the positive-excess partitions of the total six are 6, 4+2, 3+3, 2+2+2. Three order-three excess-two components need order nine. The 4+2 case uses orders four and three, leaving one unfillable order after adding only 2×2 blocks. The 3+3 case gives F. With one excess-six component, the leftover order is even, so its order is even and at most eight; order two has zero excess, and orders six and eight have just been excluded. Order four gives B. Its two zero positions have exactly the three stated incidence types. This proves the lemma as a written argument, subject to review; it is not a claim that the old partial order-eight finite search completed.

## 3. Every d=2 binary slice, including boundaries and complex phases

Fix any party i and x∈Q_i with d_i(x)=2. In each other party its E neighbors form a two-symbol set. The actual x-slice is a subset of a binary three-cube with s_i(x)=4+h_i(x) vertices, hence 0≤h_i(x)≤4. The two (i,j)-pair rows for either value of any other coordinate j have squared norm one and are orthogonal in the corresponding actual cut. In particular they have at least two E entries each, and their supports may not overlap in exactly one column.

**h=1 is impossible.** Five vertices have at most five cube edges: deleting three vertices removes 9 minus the number of edges internal to the deleted triple, which is at most two because the cube has no triangles. On each axis the two row degrees are 2 and 3; their supports are subsets of four columns and hence overlap at least once, and actual orthogonality makes the overlap at least two. The three axes would yield at least six retained cube edges.

**If h=2, the two missing words differ in exactly two coordinates of the slice.** If they differ in one coordinate, fix the other two coordinates and sum squared moduli over the varying coordinate. The resulting 2×2 table has every row and column sum equal to one, by the two relevant actual pair-row norms. One zero cell forces the opposite cell to vanish too, giving at least four missing cube words, not two. If instead the missing words differ in all three, relabel them 000 and 111 and denote the six nonzero coefficients at 001,010,011,100,101,110 by a,b,c,d,e,f. Orthogonality along the three slice axes gives

    a conjugate(e)=−b conjugate(f),
    a conjugate(c)=−d conjugate(f),
    b conjugate(c)=−d conjugate(e).

All six coefficients are nonzero. Multiplying the first and third identities and dividing by the second yields b conjugate(e)=−b conjugate(e), impossible. No real, equal-modulus, or restricted-phase assumption is involved. Distance two is left as a necessary case, not asserted impossible locally.

Let H_x be those two actual missing four-coordinate words. They agree in i and in one other physical coordinate and differ in the remaining two. For the cut pairing i with the agreeing coordinate, the two x-rows have degrees 2 and 4. In each other cut they have degrees 3 and 3, overlap in two columns, and have distinct neighborhoods. F is impossible in the first cut because it has no degree-four line, and in the other cuts because two intersecting degree-three F rows lie in one full 3×3 component and have identical neighborhoods. In B, both x-rows are in the unique 4×4 component: in the first cut the degree-two row meets the degree-four row, and in the other cuts the two degree-three rows meet. Their union contains all four core columns. Thus the two omitted slice vertices are exactly the two internal zero cells, and **the same actual two-word set H_x is the B-core hole set in all three cuts**.

**h=3:** the seven-vertex slice has, in every cut, x-row degrees 3 and 4 with overlap three. Both rows lie in the B core, and the unique omitted slice word is one of its two internal holes in every cut. **h=4:** both x-rows have degree four, so every cut is B. **h=0:** four vertices are not excluded or assigned an extra form here. These statements cover every 0≤h≤4 and all arbitrary nonzero complex coefficients.

## 4. Common holes for all X/Y parties and every weighted pair case

If q_i=4, (1) and d_i(x)≥2 force all four d_i(x)=2. By §3, h_i(x)∈{0,2,3,4}, with sum six. The only multisets are (4,2,0,0), (3,3,0,0), (2,2,2,0). The last is impossible: two distinct h=2 symbols in the same party yield two disjoint actual two-word hole sets, yet in any fixed cut each is the whole two-cell hole set of the unique B core. Call the two remaining profiles X=(4,2,0,0) and Y=(3,3,0,0); call their two positive-h symbols high and their two zero-h symbols low.

An X party supplies the same two actual holes H in all cuts through its h=2 symbol. For a Y party, each of its two h=3 symbols supplies one actual hole in all cuts. Those holes differ in the Y coordinate, so they are distinct and together exhaust the B-core holes in every cut. Comparing a fixed cut shows that every q=4 party, regardless of type, supplies **the same H**, not merely isomorphic holes.

Choose any two q=4 parties A and B, whose existence was proved in §1. In their actual E pair graph every vertex has degree two. Put weight multiplicity−2 on an edge. These weights are nonnegative, their sum at a vertex is its h, and each is at most two because the cut lemma bounds every E pair-line multiplicity by four. The entire high-high graph, with high symbols ordered as h=4,h=2 for X, and arbitrary order for Y, is (up to relabeling)

    X / X          X / Y          Y / Y
    [ 2  2 ]       [ 2  2 ]       [ 2  1 ]
    [ 2  0 ]       [ 1  1 ]       [ 1  2 ].                         (4)

This includes existence of each displayed edge, including the zero-weight edge:

* An X h=4 vertex has two incident weights 2, so both neighbors have positive h and are exactly the two opposite high symbols. A Y h=3 vertex has incident weights 1 and 2, again both neighbors are high. This directly forces every edge and weight in X/Y and Y/Y, up to relabeling.
* In X/X the two h=4 vertices force the three shown weight-2 edges. The common two holes H have the h=2 symbol of A and the h=2 symbol of B in every word. In the actual AB cut those two zero cells are in the *same* core row indexed by that pair. The row is an E pair value, has the other two core entries nonzero, and therefore is precisely the h=2/h=2 edge of weight 0. This does not assume that a generic degree-two line is external.

All high vertices have now used both their neighbors. No high-low edge exists; the two low symbols on each side form a full K2,2, and every low-low edge has weight zero, i.e. multiplicity two.

Let L be the actual E words with A low. By the graph just proved, these are exactly the E words with B low. The four low-low AB pair values each have two extensions, so |L|=8. The same cut is B. In X/Y and Y/Y, all four high AB rows have degrees three or four and therefore fill the 4×4 core. In X/X, the three degree-four high rows and the h=2/h=2 degree-two row just located by H fill it. Thus in *all* three type pairs the four low AB rows lie in the two external 2×2 components. In particular, the internal degree-two row in X/X was not mistakenly assigned outside the core.

The four complementary CD columns used by these external components have degree two and no E outside L. For AC, AD, BC, BD, a pair value used by L contains a low A or low B symbol; its h=0 forces every incident E line to have multiplicity two, and the specified low coordinate forces both extensions into L. AB has the same property by construction. P cannot use any of these E pair values. Consequently, **in each of all six physical pair systems, the same L has exactly four pair values, each with exactly two extensions, and no word of P or E outside L shares one of those values.**

For any L-used symbol x in party i, let s_L(x) count its L occurrences and d^L_ij(x) its number of L partners at party j. The two-extension property gives s_L(x)=2d^L_ij(x), so d^L_ij(x)=d^L_i(x) is independent of j. It is at least two: if it were one, all three other coordinates would be fixed, so there could be at most one distinct L word, whereas s_L=2. Each pair projection has four values, hence Σ_x d^L_i(x)=4, so each party has at most two L symbols. It cannot have only one, since every used symbol of another party would then have at most one partner there, contradicting d^L≥2. Thus each party has exactly two symbols, each d^L_i=2, and every physical pair projection is the complete binary 2×2 alphabet, each value appearing twice.

For each balanced cut, the four L rows and four L columns are complete actual U lines: the previous paragraph excludes every P or E entry outside them. Their 4×4 restriction is therefore unitary, with row and column degrees two. Its support consists of two full 2×2 blocks: two intersecting degree-two rows must share both columns, and all columns also have degree two. This is a single closed eight-word subtensor L in **all six pair systems and all three actual unitaries**, not a separate choice for each cut.

## 5. Complete binary support classification and phase contradiction

Label the two L symbols in each party by bits, equivalently x_i∈{−1,+1}. Let f be the indicator of L on the 16 binary words, and g=2f−1. The size-eight and two-coordinate-marginal conditions make the Fourier coefficients of g of degrees 0, 1, and 2 vanish. With χ_S=∏_{i∈S}x_i,

    g = χ_{1234}(a_0+a_1x_1+a_2x_2+a_3x_3+a_4x_4).

The coefficients are real and g²=1 pointwise. Comparing the x_i and x_ix_j coefficients gives a_0a_i=0 and a_ia_j=0 for i≠j, while the constant coefficient gives a_0²+Σa_i²=1. Exactly one coefficient is nonzero, equal to ±1. Thus, after physical-party and bit relabeling, the complete possibilities are four-bit even parity, or three-bit even parity times a free fourth bit. There is no unexamined binary support.

For any actual full 2×2 unitary block with nonzero entries [[p,q],[r,s]], row orthogonality gives p conjugate(r)+q conjugate(s)=0, and therefore their unit phases satisfy phase(p)phase(s)=−phase(q)phase(r). The positive magnitudes need not be equal; only the unit phases are divided below.

**Three-bit support.** Write its words as (a,b,a⊕b,d), and let r_ab be the phase of the d=1 coefficient divided by that of the d=0 coefficient. The two actual AB|CD blocks give r_00=−r_11 and r_01=−r_10. The AC|BD block with b=0 gives r_00=−r_10. Hence r_00=r_01. But in AD|BC the two rows (a,d)=(0,0),(0,1), supported at b=0,1, give r_00=−r_01. All r_ab are nonzero unit phases, contradiction.

**Four-bit support.** Write its words as (a,b,c,a⊕b⊕c), and z_abc for the unit phase of the corresponding coefficient. In AB|CD use the block a⊕b=0; in AC|BD use a⊕c=0; in AD|BC use a⊕d=1. Their actual 2×2 orthogonalities give respectively

    z_000 z_111 = − z_001 z_110,
    z_000 z_111 = − z_010 z_101,
    z_001 z_110 = − z_010 z_101.

The first two equate the right-hand products, and the third makes them negatives of one another, impossible since all phases are nonzero. These are identities of unit phases; no false equality of unequal-magnitude unnormalized products is used.

Both exhaustive supports contradict the three actual flattenings. Thus the same L forced by any two q=4 parties cannot exist, while §1 proves such parties must exist. Subject to independent scrutiny of the written cut lemma and deductions, the exact N=50,t=28 branch is excluded for arbitrary complex coefficients. No statement about other t, a global N=50 impossibility, minimum support, or existence is implied.

## 6. Boundary: local cut realizations are only illustrative

The lemma is not vacuous as a one-cut support statement. Let F_3 be a normalized 3×3 Fourier unitary and H_2=(1/√2)[[1,1],[1,−1]]. For B, define

    M=(1/(5√3)) [[0,5,5,5], [−5,0,5,−5], [−7,1,−4,3], [1,7,−3,−4]],
    R=[[1/√2,1/√2,0,0],
       [1/(3√2),−1/(3√2),−2/3,−2/3],
       [−2/(3√2),2/(3√2),1/3,−2/3],
       [−2/(3√2),2/(3√2),−2/3,1/3]].

M's numerator rows are pairwise orthogonal and each has squared norm 75, giving disjoint holes. For R, the first row is orthogonal to the other three; in the orthonormal basis (1,−1,0,0)/√2, e_3,e_4, those three are the rows of I−(2/3)J_3, an orthogonal matrix. R has same-row holes, and its transpose has same-column holes. Thus I_28⊕F_3⊕F_3⊕H_2 has the F mask, and I_28⊕M⊕H_2⊕H_2, with R or Rᵀ replacing M, realizes each B zero-incidence type, as 36×36 single-cut unitaries with N=50,t=28. This says nothing about their other two reshaped flattenings; none is presented as an AME tensor or as an exception to the whole-tensor contradiction.

## 7. Complete source, exposure, and method declaration

Before any mathematical body reading or task-specific derivation I read the manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual dispatch receipt, and all 23 manifest-listed controls, and wrote the exclusive new prebody-ack-v1.md. I also **directly sent** that acknowledgment to Main and received the tool's delivery confirmation before packet reading. The initial non-raw administrative displays elided nested fields and the dispatch line 45; I recovered the administrative material with complete raw reads, including raw dispatch line 45, before acknowledging. My prior exposure also included the user/task text, the procedural written-math skill, and the displayed advisory root memory summary; some long memory-summary lines were displayed truncated and were not recovered, and memory was not used as a mathematical source or as current-repository evidence. No private-cognition or independent source-identity certificate is asserted.

The 23 controls were read only for status/permissions: prospective-author-method-scope-restoration; contract-addendum-2; parent-L1-selected-diagnostic; parent-privacy-auxiliary-parameter; parent-core-gram-auxiliary-operator; parent-ame-held-compression-claim-consumer; parent-held-ph-registration-report-consumer; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660, and f662 respective quarantine controls; parent-remaining-d0-occupancy-E-row-omission; parent-prerun-f746-matching-and-f749-occupancy-design-corrections; and parent-f826-f832-direct-ack-transport-observations. The manifest supplies their exact paths and pins. All genuine held episodes and all proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT.

After the two acknowledgments, I read the complete single packet part serially in raw LF windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, and 321–329, including all source endings. Every individual display was below 30,000 bytes; no packet clipping or recovery was needed. Reasoning commenced only after the final window. Parent-supplied packet metadata: 60,720 bytes, 329 LF, SHA-256 00741594014748db3e269eb43202643b8b4908c27e381dbc8c50190c1e4f081d. Its complete source bodies, with parent-supplied hashes, were:

| ID | Complete original body | Supplied SHA-256 |
|---|---|---|
| S1 | f827-ame50-t28-entire-same-tensor-frontier-author/author-candidate-v1.md, LF 1–145 | c78020e48e7ca16159cf74debcb25cc2b747be06b4c371230142298c1ea95814 |
| S2 | dispositions/physics-6-actual-unitary-excess6-order6-order8-exclusion-and-AME50-t28-cut-frontier-parent-v1.md, LF 1–23 | f84c4b2eba89f99b693fa1c9fdfd5b4ef90eb5e6f7d9c5a99ca7373cc11fd0dc |
| S3 | dispositions/physics-6-actual-AME50-t25-t27-exclusion-and-excess-frontier-parent-v1.md, LF 1–33 | 9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336 |
| S4 | f799-ame50-unitary-excess-five-t27-proof-author/author-candidate-v1.md, LF 1–110 | 61dfb5205f9b6bf2022c17d6149f1926571c48d24307556f67a7f2201b684197 |

S1 and S4 are under review-waves; all paths are fully specified in this wave's manifest. The hashes, packet roundtrip, and final binding are parent-supplied administrative metadata, not independent rehashing, source-identity proof, or mathematical correctness. No unlisted scientific source or outgoing link, sibling source, held body/consumer, network, external model, code, subprocess, scientific execution, test, compiler, solver, build, lint, formatter, Git, or deletion was used. No verifier or other code was prepared, so there is no code hash or computational verification. These are newly written derivations, not a review verdict; corrections must be new additive files, never edits to this candidate.
