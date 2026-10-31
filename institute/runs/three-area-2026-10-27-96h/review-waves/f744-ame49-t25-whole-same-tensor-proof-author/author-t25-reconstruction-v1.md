# N=49, t=25: same-tensor written reconstruction

**Status and exact claim.** GENERAL AUTHOR, NONBLIND same-harness reconstruction of the complete t=25 branch of S2, including the elementary omissions corrected in S1. Subject to independent scrutiny, no normalized complex AME(4,6) state in a local orthonormal product basis has exactly 49 nonzero coefficients, of which exactly 25 have modulus 1/6. Equivalently, for the *one* tensor U=6ψ, no such tensor has N=49 and exactly t=25 entries of modulus 1. The argument below is an actual complex-tensor support contradiction. It does not assume real amplitudes, equal phases, equal residual magnitudes, independent pair graphs, an orthogonal array, or an OLS theorem. It does not use a global bound on t. It does not prove N≠49 for other t, an exact minimum, or existence/nonexistence of a support-49 witness. Parent full read and disposition, and any independent reviews required by the run, are separate and have not happened by this author write.

Native clock observed before this write: **2026-10-30T17:28:39-0700 PDT**. The clock is a prior observation, not an asserted exact creation time. Each displayed reduction below is a necessary consequence for the same U; no arbitrary support satisfying a surrogate is claimed realizable.

## 1. One complex tensor and the exceptional support in every cut

AME means each of the three 36×36 two-versus-two flattenings of U is unitary. Let P be its 25 unit-modulus entries and E its other 24 nonzero entries. A modulus-one entry exhausts its row and column, so no other nonzero shares any of its six physical pair values. P is injective in each pair projection. In a fixed cut, deleting the P rows and columns leaves an 11×11 unitary with 24 nonzeros and no degree-one row or column: a singleton in a unitary has modulus one and would belong to P. Thus each pair value occurs either once in P and never in E, or at least twice in E and never in P.

We prove the required support classification without an external graph theorem. A connected component of a unitary's bipartite row-column support is square: its row vectors give row count ≤ column count, while its column vectors give the reverse inequality. In any unitary two distinct rows or columns cannot have exactly one common nonzero, since their inner product would be one nonzero complex product. This remains true for arbitrary complex phases and moduli.

For a square connected component of order m, let e be its number of nonzeros minus 2m. Minimum degree two gives e≥0. If m>2 and a row has degree two at columns c,d, every other row meets both c,d or neither; hence c,d have identical row-neighborhoods. Both column degrees are at least three. Indeed, if their common degree were two, those two columns form a 2×2 unitary on their two rows, exhausting those rows as well and splitting off a component. Two distinct degree-two rows cannot share a column unless they share both columns; in that event their 2×2 row submatrix is unitary and isolates a 2×2 component. Hence all degree-two rows have disjoint twin pairs of degree-at-least-three columns. There are at least m−e degree-two rows and at most e degree-at-least-three columns, giving

    m − e ≤ floor(e/2),    i.e. m ≤ e + floor(e/2),    for m>2.

An order-two component is the full 2×2 support and has excess zero. Thus excess zero has only 2×2 components, excess one is impossible, and a component of excess two has order three and eight nonzeros: all entries of a 3×3 support except one. Since the entire 11×11 residual has excess 24−22=2, in *each* of the three cuts it consists of exactly one such 3×3-minus-one component and four full 2×2 components.

Consequently, in each of the six physical pair systems there are exactly 11 E pair values: two **high pair values** of E multiplicity three and nine **low pair values** of multiplicity two. In every cut the two high row values meet exactly the same three column values: both high columns and one common low column. The analogous statement holds after interchanging rows and columns. In particular, every high-row/high-column corner of that component is an actual nonzero word of the same E, and the unique extra neighbor of either high row is the *same* low column. No phases have been chosen or equations discarded to obtain these necessary facts.

## 2. Common degrees, addendum cases, and the five-vertex cube

For a party i and an E-used symbol x let d_i(x) be its number of distinct E neighbors in another party j, and let s_i(x) be its number of occurrences in E. The degree does not depend on j: among the six possible ij values, the 6−d_i(x) values not used by E are exactly the P values with i-symbol x, and P is pair-injective. Hence this number is the number of P words containing x, independent of j. Set h_i(x)=s_i(x)−2d_i(x). For *each* j≠i, h_i(x) counts the high ij pair values incident to x, since E pair multiplicities are two or three. Therefore

    sum_x d_i(x)=11,     sum_x h_i(x)=2,     h_i(x) is a nonnegative integer.

Every E-used symbol has d_i(x)≥2. If its common degree were one, all E words at x would have the same unique symbol in each of the three other parties, hence there could be at most one word at x, contrary to every E-used pair value having at least two E extensions. In particular q_i, the number of E-used symbols at i, is at most five.

This also pays the explicit q=1 omission: if q_i=1 then the 11 E values of any ij projection must fit into q_i q_j≤5 cells, impossible. If q_i=2, then similarly q_i q_j≤10<11, so q_i≥3. These two conclusions do not rely on a degree-one symbol secretly existing.

We need the following elementary slice lemma. If d_i(x)=2 and h_i(x)=1, its s_i(x)=5 E words occupy five vertices of the binary 3-cube of its partner symbols. For each of the three remaining parties, the two actual unitary rows at the corresponding pair values contain two and three entries among the four complementary cube coordinates. Their supports intersect, and cannot intersect in exactly one position; hence at least two cube edges in that direction have both endpoints present. That requires at least six induced cube edges in total. But deleting three vertices from the cube removes 3·3−e_removed edges, and the three deleted vertices induce at most two edges because the cube is bipartite. Thus the five retained vertices induce at most 12−9+2=5 edges, a contradiction. Therefore

    h_i(x)=1  implies  d_i(x)≥3.                                      (1)

The same d≥2 proof is not specific to t=25: at N=49,t=28 there are eight E pair values in each system, the common degree sum is eight, every used degree is at least two, and q_j≤4. Thus q_i=1 would require eight values in at most four ij cells. This establishes precisely the degree-one/q=1 assertions of S1 also for that other exact branch; it does not import or certify any further t=28 argument.

## 3. Concentrated versus diffuse and the alphabet moments

At a party, total h=2 means either one symbol has h=2 (concentrated) or two symbols each have h=1 (diffuse). Two concentrated parties cannot coexist: their two distinct high pair values would both have the same two endpoints. Suppose A is concentrated at a; B,C,D are then diffuse. In AB the high values are (a,b_0),(a,b_1); in CD they form a matching (c_0,d_0),(c_1,d_1). The high-by-high 2×2 corner in the AB|CD exceptional block gives the four actual words (a,b_p,c_q,d_q), p,q∈{0,1}. In AC|BD, both (a,c_0) and (a,c_1) are high rows, so they have the same three BD neighbors. Yet the four displayed words give the union of their neighbors at least four distinct values (b_p,d_q), impossible. Hence **every party is diffuse**.

Call its two h=1 symbols high symbols. The two high ij values form a matching of the high symbols at i and j: each high endpoint has one incident high value. By (1) the two high-symbol degrees are at least three, while all other degrees are at least two. Since their sum is 11, q_i≤4, and because q_i≥3 we have q_i∈{3,4}. Two size-three alphabets cannot coexist: they contain only nine pair cells but there are 11 E values. Thus the only possible alphabet profiles, up to party permutation, are 3444 and 4444.

Let k(w) count how many coordinates of a P word w lie in the corresponding E alphabets; write n_k for its number and Q=Σ_i q_i. Because the same pair-injective P set saturates precisely the complements of the E pair values,

    Σ_k n_k=25,
    Σ_k k n_k = 6Q−44,
    Σ_k binom(k,2)n_k = Σ_{i<j} q_i q_j−66.                          (2)

For 3444, the last two quantities are 46 and 18, so

    n_0+n_3+3n_4 = 25−46+18 = −3,

contrary to nonnegativity. Therefore q_i=4 for every i. Its high degrees and low degrees, respectively, are either (3,3;2,3) or (3,4;2,2); in particular every party has a high symbol of degree three.

For completeness, the 4444 moments in (2) are 52 and 30, hence n_0+n_3+3n_4=3. They even force exactly one of the following two P-count vectors, listed in order (n_0,n_1,n_2,n_3,n_4):

    (0,1,21,3,0)   or   (0,0,24,0,1).                               (3)

Indeed set a=n_0 and c=n_4. Then n_3=3−a−3c and the other two moment equations yield n_1=1−3a−c, n_2=21+3a+3c. Nonnegative integral counts imply a=0 and c=0 or 1. This refinement is a necessary P-incidence calculation, not an assertion either vector is tensor-realizable; the contradiction below does not rely on it.

## 4. Matching consistency, without assuming a balanced signing

Choose bit labels 0,1 on each party's high symbols. For each ij, its two high pair values are described by x_i⊕x_j=c_ij for a bit c_ij. In the AB|CD exceptional block the four high-by-high words have x_A⊕x_B=c_AB and x_C⊕x_D=c_CD. Among those four, exactly two have a high AC pair, one in each high AC row. Their BD values are distinct. If they were low BD values, the AC|BD high rows would have two different low neighbors, contrary to their common unique low neighbor. Hence both BD values are high. This gives

    c_AB⊕c_CD = c_AC⊕c_BD.

The same argument for AD|BC gives equality to c_AD⊕c_BC. Switching local bit labels makes c_AB=c_AC=c_AD=0; the displayed equalities then force

    c_BC=c_BD=c_CD=p,  where p∈{0,1}.                               (4)

These are both cases. The p=1 frustrated case is not eliminated by a relabeling.

## 5. The eight-box obstruction

Suppose the same E contains the eight even-parity binary words on the high symbols. In each physical pair all four high-high values already occur twice. The two low values are therefore exhausted, while each of the two high values has exactly one more E extension. In every cut, the two high rows share a low complementary pair L. If L contained a high symbol in either complementary party, then among the two high-row extension words one would use a low high-high cross-pair value, already exhausted by the eight words. Thus L has no high coordinate. The 12 third extensions, one for each of the two high values on each of the six pairs, are consequently distinct words with exactly two high coordinates.

We record an equality of their low coordinates needed both here and in the next case. Let ℓ_{j|r} be the j-coordinate of the common low complementary pair for the high pair consisting of the two parties other than j,r. Fix j and distinct r,s among the other parties; let i be the remaining party. Choose a high i-symbol of degree three. The eight box gives it both high j-symbols as neighbors, so it has exactly one nonhigh j-neighbor. Its extensions on high pairs ir and is have j-coordinates ℓ_{j|s} and ℓ_{j|r}, respectively. They must be equal. Varying i shows all three ℓ_{j|r} are one symbol ℓ_j.

For a given j, all six extensions on high pairs not containing j contain ℓ_j, and these are distinct. Since ℓ_j is nonhigh, h_j(ℓ_j)=0 and s_j(ℓ_j)=2d_j(ℓ_j)≥6. Its degree is at least three; the two high degrees are at least three and the remaining low degree at least two, while their sum is 11. Therefore d_j(ℓ_j)=3 and both high degrees are exactly three. Each high symbol has s=2·3+1=7 occurrences, all used by its four box occurrences and three extension occurrences; ℓ_j has s=6, all used by the extensions.

The eight box plus the 12 extensions uses 20 of the 24 E words. No other word can contain two high symbols: whichever physical pair they form, its value is already exhausted by the box alone if low, or by the box and its unique third extension if high. Moreover all occurrences of both high symbols and of ℓ_j are already spent. Each of the four remaining distinct words would therefore have to use the one remaining low symbol in every party; there is only one such word. Contradiction. This proves the **eight-box lemma** for the same tensor and all six pair systems.

When p=0 in (4), all high pair matchings are equality. The high-high corners of the three cuts force the two constant words and the six weight-two words, exactly the even eight-box. Thus p=0 is impossible.

## 6. Frustrated matching: six words and all bundle cases

For p=1, complement the B,C,D labels from (4). Now every high pair value consists of unequal bits. Each two-zero/two-one word can be partitioned into two opposite-bit pairs; it is a high-by-high corner in that cut. Hence all six balanced words occur. For any pair, each unequal-bit high value occurs in exactly two of the six and needs one further E extension; each equal-bit low value occurs in exactly one and needs one further extension.

No other four-high word occurs. For a weight-one or weight-three word, choose an opposite-bit high pair ij. Its complementary pair kl has equal bits and is low. This low kl value already occurs in a balanced word with a low ij row. If it were the word's neighbor in the exceptional component, both high ij rows would meet that same low column, giving at least three E extensions of the low kl value, a contradiction. If 0000 occurs, in any cut the low 00 row contains columns 11 (from a balanced word) and 00, while the low 11 row contains column 00 (from another balanced word). Row orthogonality prohibits one overlap, forcing column 11 in that second row, i.e. 1111. Conversely 1111 forces 0000. Both constants with the six balanced words would be the excluded even eight-box. Thus the six balanced words are the only four-high words.

A three-high word is **mixed** if its three high bits are not all equal. Such a word forces exactly a three-word bundle. Write it, after choosing party names and if needed interchanging 0 and 1, as

    (i0,j0,k1,lλ),

where λ is nonhigh. In the ik|jl cut, (j0,λ) is a low column adjacent to a high row, so it is also adjacent to the other high row. This forces (i1,j0,k0,lλ). Likewise jk|il forces (i0,j1,k0,lλ). These three words use both high values on each of ij,ik,jk and exhaust their unique third extensions beyond the six balanced words.

There can be at most one such bundle. Any two three-party subsets of four parties have a common pair. If the subsets differ, their respective bundle words realizing a high value of that pair cannot be the same word, because the sets of high coordinates differ, yet the pair has only one extension beyond the balanced words. If the subsets agree, sharing any already saturated high pair value forces the identical word, including its nonhigh coordinate; the same common-low-neighbor argument then forces the same entire bundle. Thus the alternatives **no bundle** and **one bundle** below are exhaustive, and homogeneous three-high words cannot supply an opposite-bit high pair.

### 6a. No bundle

In any cut, the common low column L for the high rows cannot contain exactly one high coordinate: the resulting extension would be a mixed three-high word. It cannot contain two high coordinates: an unequal-bit pair is a high column, not L, while an equal-bit pair would give a forbidden weight-one or weight-three four-high word. Hence L contains two nonhigh coordinates. The 12 unique high-pair extensions are distinct two-high words.

The equality-of-low-coordinates argument of Section 5 applies unchanged: the six balanced words contain both high j-symbols as neighbors of every chosen high i-symbol, and every party has a high symbol of degree three. It gives a common ℓ_j occurring in six of the 12 extensions, and the same degree-sum argument gives both high degrees equal to three. Every high symbol occurs in three balanced words and in three two-high extensions, so its total s=7 leaves exactly one further E occurrence.

Fix iε. For each j≠i, the equal-bit pair (iε,jε) is low, occurs once among the balanced words, and needs one further extension. None of the 12 two-high extensions supplies such a pair, since their two high bits are unequal. Therefore the one remaining word containing iε would have to contain jε for all three j, making the forbidden constant four-high word. Contradiction.

### 6b. One bundle

Let the bundle's high parties be A,B,C and its nonhigh party be D. Interchanging 0 and 1 if necessary, the three bundle words on A,B,C have majority bit zero. They exhaust both high values of AB, AC, BC. Each of the six high values on DA, DB, DC has one extension beyond the balanced words. That extension cannot be a four-high word outside the six, and cannot have three high coordinates: because it contains an opposite-bit pair it would be mixed, forcing a second bundle with a different high-party set. Thus these six are distinct two-high words, and each of D0,D1 occurs in three of them as well as in three balanced words.

For D0, each low pair (D0,A0),(D0,B0),(D0,C0) already occurs once in the balanced words and needs one further extension; none of the six just counted or the bundle supplies one. A new word cannot supply two of them: e.g. A0B0 is already saturated by one balanced word and one bundle word, and similarly for A0C0 and B0C0. Thus D0 has at least three further occurrences, for at least nine in total, giving d_D(D0)≥4 from s=2d+1.

For D1, each of (D1,A1),(D1,B1),(D1,C1) likewise needs one additional extension beyond the already counted words. One word can supply at most two, since supplying all three would be the forbidden 1111 word. Hence at least two further occurrences are needed: s_D(D1)≥8. Since h_D(D1)=1, s_D(D1)=2d_D(D1)+1 is odd, so in fact s_D(D1)≥9 and d_D(D1)≥4. The two other D-symbols have degree at least two, and the degree sum is at least 4+4+2+2=12, contradicting 11.

Both possible signings and both frustrated bundle alternatives have now been excluded. The assumed N=49,t=25 complex tensor cannot exist. The proof uses only support restrictions necessarily obeyed by its actual complex amplitudes; it makes no claim that other supports or phase systems have been fully classified.

## 7. Source boundary, coverage, and verification status

Actual dispatch receipt was read first. Before any packet body, I read the complete 270-LF manifest, 116-LF freeze receipt, 198-LF final binding, 258-LF prepared metadata, actual dispatch receipt, and all **22** manifest-listed controls through their endings; controls were used only for permissions/status. I sent the direct PREBODY ACK to Main with the one-part/205-LF count. Thereafter the single body was read serially in RAW ranges 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–205, through the ending before research or comparison. This covers S1 1–9, S2 1–95, S3 1–11, S4 1–27, and S5 1–41 in their entirety. S2 is the unadopted original candidate, not an independent review of this reconstruction. S3–S5 are context only; their conditional global/computer-assisted scopes are not imported in Sections 1–6. No outgoing links, held episodes/history/methods/consumers, old code, or unspecified sibling proof were followed.

Metadata-only SHA-256 observations after the completed read:

- `manifest-v1.json`: `9abdab208cac87c7a0367243ef028c295c0507570a10e8f029303b15f72b6a6a`.
- `freeze-receipt-v1.json`: `6a7c9a5f7cc1a9fd4563c1dde107f10ce89694c41df2bf9c6de8b7737e242b68`.
- `final-pre-dispatch-binding-v1.json`: `6eb77f63b39d607146a2c20d0111bea36713b9948feefb74daeb0822cba2a9c2`.
- `parent-live-metadata-supply-v1.json`: `2d3931bd42ef0aa839aabea396e94454b1726479e498b6c75d53480c462b9232`.
- `dispatch-receipt-v1.json`: `73fbecac4afe98af913d25bcb611b1a39fb10a07174c59f4b75e41530cee91f5`.
- `literal-packet-part-01-v1.md`: `625558a37d711881d775d72ae77aa2b88a3154b7ec91d713e6bae20689c9c78e`.

Packet-declared complete source pins, as supplied by the parent binding and not independently rehashed by opening outgoing original paths: S1 `a1f4949715b7d057e2ade33c7d81f9007a076f28d8c15abd76559857ee1384cc`; S2 `0af317016bcd029932cc915f3c4535ab848db08d4d12809c0b32270143003a9f`; S3 `eeaa78deff17346a72477cc06197af28b8150bf940163ed6ca8f8e7800e04bb6`; S4 `f7d6be4da84004d8b8a163f6cd02583772735ebc53df44dd5d3c9905493ead86`; S5 `25c34705825561d501701a26b50c08a7b734bf2282f72f3283568c8cb459f968`. The parent freeze/binding asserts source identity and packet roundtrip; this author did not repeat that byte comparison. No new correction to an earlier frozen artifact is asserted; if an error in this reconstruction is found it requires a separate additive correction, never overwrite/backdating.

**NOT TESTED / remaining frontier.** No scientific executable, solver, compiler, test, build, lint, formatter, external-model CLI, paid/heavy action, or standalone finite source was run or prepared by this child; the SHA operation was metadata only. There is no finite PASS, full original-caller or family review, human check, kernel proof, parent adoption, source-identity authentication, or novelty/priority claim. Other t values, especially the actual N=49,t=28 feasibility/phase problem, and unconditional exclusion of support 49 are outside this isolated result. The conditional baseline and its no-OLS/f113/computer-assisted provenance remain exactly those of their separately cited dispositions; this t=25 reconstruction neither removes nor silently imports their global dependencies. All genuine held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT.
