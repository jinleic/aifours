# Independent reconstruction: complex AME(4,6), support 45 and 46

**Result and assurance.** I reconstructed the entire S1 route for the original complex tensor and found no remaining mathematical gap in the arguments below. In particular, the exact branch N=46, t=26 is excluded without a maximal-count or no-OLS import. Under the explicit additional hypothesis t≤28, N=45 and N=46 are both excluded. These are new, nonblind, same-harness written deductions, not an adoption, an independent-model-family or human review, a kernel proof, a finite execution, a novelty result, or an old WRITTEN-gate pass. The separately reported global supply of t≤28 is conditional on its f113 provenance, including classical no-OLS(6) and the prior t≤30 boundary; I did not independently authenticate those underlying sources. Nothing here excludes N=44 or proves a global N≥49.

## 1. Caller, six physical projections, and low-excess unitaries

Let ψ be one normalized complex AME(4,6) tensor in an arbitrary product basis. Write U=6ψ. Its matrices for all three complementary two-versus-two partitions are unitary; all cuts use exactly the same complex tensor entries. Let N be its support size, let P be the t entries of modulus 1, and let E be the other nonzero entries. Every P entry alone exhausts its row and its column in each cut. Thus on each of the six physical pair projections, the t values used by P are distinct, and E uses none of them. Removing those singleton rows and columns in each cut leaves an n×n unitary, n=36−t, with all |E|=N−t residual entries and with every line of degree at least 2. Its total row excess over degree 2 is

    e = N−t−2(36−t) = N+t−72 ≥ 0.                 (1)

Two distinct unitary rows cannot share exactly one occupied column, and likewise with rows and columns interchanged: one nonzero complex product cannot sum to zero. Every support component is square because the isolated component block has both orthonormal rows and orthonormal columns. Each component has nonnegative excess; the same is true in the column count.

The following classifications use no equal-modulus or fixed-phase hypothesis.

* If e=0, all residual rows and columns have degree 2. A row meeting another must have the same two columns. Those two columns have degree 2, so the component is exactly a complete 2×2 block. Hence n is even.
* Excess 1 is impossible. The unique degree-3 row R has three columns; every other row is degree 2. A degree-2 row meeting R must use two of those columns. Distinct pairs from three columns intersect once and are forbidden, so all such rows use the same pair, leaving the third column with degree 1.
* For total excess 2, there is a unique positive-excess component. If it has a degree-4 row R, all other rows are degree 2. Their two-subsets inside R are equal or disjoint; column degree ≥2 forces two disjoint pairs covering the four columns. A column from each pair shares only R: any degree-2 row containing both would meet the existing row on one of those pairs exactly once. This contradicts column orthogonality. Otherwise there are two degree-3 rows R,S. Their three-column sets cannot intersect in one. If they intersect in two, a degree-2 row needed at R's private column must also use a shared column and meets S exactly once. If they are disjoint, every degree-2 neighbor of R uses two columns of R, and no path can leave these columns, contrary to connectedness with S. They therefore have identical sets of three columns. Every adjacent degree-2 row uses a two-subset of those columns; all these pairs are the same, as distinct two-subsets would overlap once. The component contains only those three columns and, by squareness, three rows. Its support is an eight-entry 3×3 block. All other components are 2×2, so n is odd.

For N=45, (1) and t≤28 force t=27 or 28. At 27, e=0 and n=9 is odd; at 28, e=1. Both are impossible. For N=46, the same hypothesis forces t∈{26,27,28}. The t=27 branch has e=1; at t=28, e=2 and n=8 is even. Both are impossible. The rest of this record excludes t=26 itself, without assuming t≤28.

## 2. The exact N=46, t=26 interface

Here |P|=26, |E|=20, and each of the three residual 10×10 unitary matrices is five complete 2×2 blocks. In every physical pair system exactly 10 pair values belong to E, each with exactly two extensions, and the other 26 pair values belong to P, each once. In particular, a pair value occupied by E or P is completely unavailable to the other set, and the same P and E serve all six systems.

For a symbol x in party i let d_i(x) be its number of E-neighbors in any other chosen party, let s_i(x) count E words containing it, and let p_i(x) count P words containing it. The pair-complement and multiplicity equations give, independent of the other party,

    s_i(x)=2d_i(x),   p_i(x)=6−d_i(x),   Σ_x d_i(x)=10.           (2)

A used E symbol has d_i(x)≥2: d_i(x)=1 would give the same unique neighbor in each of the other three coordinates, while (2) demands two distinct words. Let A_i be the used E alphabet and q_i=|A_i|. Then q_i≤5 and q_i q_j≥10 for every i≠j.

The actual residual amplitudes also obey each of the fifteen block equations. If [[a,b],[c,d]] is an actual nonzero 2×2 block, then |a|²=|d|²=s, |b|²=|c|²=1−s with 0<s<1, and

    a conjugate(c)+b conjugate(d)=0,
    a conjugate(b)+c conjugate(d)=0,
    ad/(bc) is negative real.                                      (3)

The same entry a, b, c, or d is reused in its other-cut blocks. The later phase argument is a necessary consequence of these actual complex equations; it does not assign independent phases to the cuts or posit equal E moduli.

## 3. Closed binary block and absence of distance one

First, a normalized four-qubit pure state cannot have all two-qubit reductions I/4. Let ρ be its three-qubit marginal. Its complementary qubit is I/2, so ρ²=ρ/2. Its one- and two-body Pauli coefficients vanish, so ρ=(I+M)/8 with M a real linear combination of weight-three Pauli strings. Thus M²=3I+2M. In the symmetrized square, the product of two weight-three strings can have weight three only when they differ at all three sites, in which case they anticommute and cancel. Consequently M² has no weight-three term, forcing M=0, contradicting the identity.

It follows that eight E words inside a two-symbol-per-party box are impossible if each of its four values in every one of the six physical pairs occurs twice within those eight words. Each such pair value is then globally exhausted, and no P value uses it. In every cut the four corresponding rows and columns are isolated from the rest of U, so the same 4×4 subarray is unitary in all three cuts. Dividing that subarray by 2 would give the forbidden four-qubit state. Closure of only one cut is not sufficient; this argument explicitly uses all six physical pair values.

Now suppose two E words differ only in the fourth coordinate, with values d₀,d₁ and common triple s=(a,b,c). In each cut the 2×2 block containing them supplies another base triple with both d₀,d₁, sharing one of a,b,c. Close under these operations and call the resulting set of base triples S, with m=|S|. For each s∈S and each of its three symbols, the pair with d₀ has exactly two E extensions. The second is the base triple supplied by the relevant actual block, and it also occurs with d₁. Thus each used base symbol occurs in exactly two S triples. No two S triples share two base coordinates, since their four words with d₀,d₁ would exceed the two extensions allowed for that base pair. Joining triples that share a base symbol therefore gives a simple 3-regular graph.

For adjacent triples s,s′ sharing c, the actual ab|cd block has rows ab,a′b′ and columns cd₀,cd₁. Its column inner product is

    z_s+z_s′=0,   z_s=U(s,d₀) conjugate(U(s,d₁))≠0.              (4)

The same nonzero z_s is used on every incident edge. Hence an odd cycle is impossible, and this graph is bipartite. A simple cubic bipartite graph has equally sized sides of size at least 3. Since S×{d₀,d₁} contains 2m of the 20 E words, m is 6, 8, or 10.

In each base-base pair, the m S projections are distinct and each occurs twice; in a base-fourth pair, m/2 base symbols each occur twice with each of d₀,d₁. Hence in every physical pair the S words exhaust exactly m E values, each twice. The other 20−2m E words use the remaining 10−m values in each pair, each twice.

* For m=10, each base alphabet of S has five symbols, the whole E is S×{d₀,d₁}, and d(d₀)=d(d₁)=5. Each of d₀,d₁ therefore has one P occurrence. Every one of its five E-neighbors in each base party is exhausted, so each P occurrence must use the sole base symbol outside S in each of the three base coordinates. The two P words share those three coordinates, contradicting pair injectivity.
* For m=8, four E words remain. In every pair they have exactly two values, each twice. In any coordinate there is either one symbol or two symbols with two occurrences each. For any two varying coordinates, having exactly two joint values forces their two-versus-two partitions of the four words to coincide, up to swapping labels. All varying coordinates therefore depend on the same binary partition, so there are at most two distinct words, not four.
* For m=6, eight words remain and each pair has four values, each twice. The local version of (2) gives degree at least 2 for every used symbol, otherwise its two occurrences would be identical in all coordinates. There are four pair values, so each coordinate uses at most two symbols. Since a product of the two coordinate alphabet sizes must contain four values, every coordinate uses exactly two symbols and all four pair values. Each occurs twice, yielding the forbidden closed binary block.

Thus no two distinct E words have Hamming distance one. Every step used one actual U, all three cuts, and the complex relation (4).

## 4. Low slices and the low-triangle lemma

Call a symbol low if d=2 and high if d≥3. A low symbol occurs in four E words and has exactly two neighbors in each other party. Its four different words form an independent set of size four in a 3-cube, because distance one is forbidden. Such a set is one parity class: if it contained opposite parities, the two vertices would have to be antipodal, and their neighborhoods would exhaust the other six vertices. Thus the projection of a low slice onto any two of its three neighbor sets is the complete 2×2 product, once per cell.

Make a graph whose vertices are all low symbols, with an edge for every low-low physical pair used by E. It has no triangle. Suppose low symbols x₁,x₂,x₃ in three parties are pairwise adjacent. Their common pair (x_i,x_j) occurs in two E words; distance ≥2 forces those two words to use different symbols in each of the remaining two parties. Since each low slice has only two neighbors there, this identifies the two actual neighbor symbols of the two slices. Doing this for all three pairs puts all three slices in one physical 2×2×2×2 box. In each slice the four words are a parity class. Intersections of slices are nonempty, so their induced four-bit parity classes agree. Their pairwise intersections have two words; their triple intersection has one, because the projection of the first low slice onto the other two low-coordinate neighbors is complete. Thus their union has seven of the eight vertices of that same four-bit parity class.

To force the eighth using the actual unitary, label each of x₁,x₂,x₃ by 0 and the alternative symbol by 1. Choose the fourth-coordinate bit convention so that the missing vertex is (1,1,1,1−ε), and the common low vertex is (0,0,0,ε). In the 12|34 cut, the residual rows 00 and 11 both have an entry in column (0,ε): those two words are among the seven. Distinct rows cannot overlap once and both residual rows have degree two, so their column supports coincide. The other column of row 00 is (1,1−ε), forcing the missing vertex (1,1,1,1−ε). These eight words exhaust all four values in all six pair systems, twice each, giving the forbidden binary block. This proves the triangle lemma using the physical row overlap, not a separately chosen graph realization.

Two consequences hold universally. First, a low symbol cannot have low neighbors in two different other parties: its parity slice contains a word using both, making the third edge of a low triangle. Thus all low neighbors of a fixed low symbol lie in at most one other physical party. Second, no E word has three low coordinates, since its three low-low pairs would form a triangle.

## 5. Exhaustion of q profiles before 3444 and 4444

As q_i≤5 and q_iq_j≥10, q_i≥2. If q_i=2, each other q_j=5 and all ten pairs in every 2×5 box are E values. Both i-symbols have d=5 and hence one P occurrence. In each other party, P must use the sole symbol outside its five-symbol E alphabet, so those two P words share three coordinates, impossible. Thus q_i∈{3,4,5}, and at most one q_i is 3.

If two parties have q=5, all their symbols are low by (2). Among the other parties at least one has q=4 or 5, hence has a low symbol. That symbol has low neighbors in both q=5 parties, a contradiction. Thus at most one q_i is 5.

Suppose exactly one party D has q_D=5. At least two others, call them B,C, have q=4. Their possible degree multisets are (2,2,2,4) and (2,2,3,3). Every low B symbol has two low D neighbors and therefore only high C neighbors; so C has at least two highs and must be (2,2,3,3). The same holds for B. There are no low-low B–C edges. The ten B–C edges are all four low-B/high-C values, all four high-B/low-C values, and a perfect matching between the two high sets. Indeed each high vertex has degree 3, already has two opposite low neighbors, and needs one high neighbor.

There are exactly two complete K₂,₂ subgraphs of this B–C graph: low-B × high-C and high-B × low-C. Two low B rows share both high C columns; two high B rows share both low C columns; a low and a high B row share only one column. Each low D slice projects to one of those two complete subgraphs. The two low B symbols have four D incidences, and each D symbol choosing the first subgraph accounts for two, so exactly two D symbols choose it. Likewise exactly two choose the second. This accounts for four, not all five, D symbols. Thus no party has q=5.

The only sorted profiles left are 3444 and 4444. Their exclusions below use the same actual P and E and cover all party permutations.

## 6. The 3444 profile: moment equality and actual P words

Let A have q=3 and B,C,D have q=4. Each q=4 symbol has degree at most 3 because its A-neighbor set has size 3, so each q=4 degree multiset is (2,2,3,3). The A degree multiset is either (2,4,4) or (3,3,4).

For w∈P let k(w) count the coordinates lying in their E alphabets. Formula (2) and the exact complement of E in every physical pair give

    Σ_P k = 6(3+4+4+4)−40 = 50,
    Σ_P binom(k,2) = 3·(3·4)+3·(4·4)−60 = 24.                (5)

For k=0,1,2,3,4, the number binom(k,2)−k+1 is 1,0,0,1,3. Summing (5) and |P|=26 yields zero. Therefore each P word has k=1 or 2, and exactly two have k=1.

For an A symbol of degree d, in each of B,C,D it has 4−d P-neighbors in the corresponding E alphabet. These are disjoint P words because k≤2, while the A symbol has 6−d P occurrences total. Therefore 3(4−d)≤6−d, or d≥3. A has degrees (3,3,4). Write z for the degree-4 symbol and u,v for the degree-3 symbols. The two P words at z have no other E-alphabet coordinate and are exactly the two k=1 words. Since each of B,C,D has precisely two outside symbols, pair injectivity lets us label them so that the z-words have outside triples (0,0,0) and (1,1,1).

Both high symbols in each q=4 party neighbor all three A symbols, while each low symbol neighbors z and exactly one of u,v. Each degree-3 A symbol has exactly three P words, with respectively a B, C, or D residual coordinate and the other two outside. Denote the B-outside value in its C-residual word by r. Injectivity among those three words at A forces the other B-outside value to be 1−r, and likewise the two C-outside and two D-outside values differ. Injectivity against the two z-words forces each outside-outside pair in those words to be unequal. The resulting unique pattern is

    W_B=(u_r,b_r,1−r,r),
    W_C=(u_r,r,c_r,1−r),
    W_D=(u_r,1−r,r,d_r).                                           (6)

Here b_r,c_r,d_r are the unique q=4 low symbols not adjacent to u_r in E. The two degree-3 A symbols have different r, because otherwise their B-residual words share the same C,D outside pair, contrary to P injectivity. This also fixes the orientation in (6), not just an unordered pattern.

For each r, (b_r,c_r) must be an E pair. If not, its unique P word has A and D outside, since k≤2. Its D value cannot be r, by W_B, or 1−r, by W_C. Similarly, a P word on (b_r,d_r) would need C outside but both values are forbidden by W_B and W_D; a P word on (c_r,d_r) would need B outside but both values are forbidden by W_C and W_D. All three pairs are therefore E pairs, giving a low triangle. This excludes the entire 3444 profile, including the initially possible (2,4,4) A degrees, which were actually ruled out above rather than assumed absent.

## 7. The 4444 profile

Each party has degree multiset (2,2,2,4) or (2,2,3,3), hence at least two low symbols. Suppose first there is a low-low E edge between parties i,j. A low endpoint has its low neighbors in at most one party, so its two neighbors in each complementary party are high. Both complementary parties therefore have two highs and type (2,2,3,3); the endpoint's parity slice uses all four high-high values in their physical pair.

For two (2,2,3,3) parties let x be their number of low-low edges. Their low and high degree totals are 4 and 6 on each side, so the four quadrant counts are

    LL=x,   LH=4−x,   HL=4−x,   HH=2+x.                        (7)

All four HH values in the complementary pair occur, so x=2 there. Applying the same argument to one of those complementary low-low edges forces i,j also to be of type (2,2,3,3), and then (7) makes their LL count 2. More generally, every nonempty low-low physical pair has exactly two edges and its complementary pair is also nonempty with two edges.

At most one complementary pairing of parties can be active. If two were active, each party would have low-low neighbors in two different other parties. Its two low vertices must be split between those destinations by the low-neighbor restriction. At each end of either physical pair only one low vertex is then available, so that pair has at most one distinct edge, contradicting its required two. Hence the entire low graph has at most four edges.

In this case all four parties have exactly two low symbols, each appearing in four E words: there are 32 low-coordinate incidences. No word has three lows. If n₂ is the number of E words with two lows, then 32≤20+n₂, so n₂≥12. Each low-low edge has exactly two E extensions; since there are no three-low words, these extensions count distinct two-low words for different edges. Hence n₂=2·(# low-low edges)≤8, a contradiction.

If no low-low edge exists initially, every E word has at most one low coordinate. Each of the four parties has at least two lows, each with four occurrences, so there are at least 32 low incidences in only 20 words, already impossible. Thus all 4444 configurations are excluded, including the no-edge and (2,2,2,4) cases.

Together §§2–7 exclude the complete N=46,t=26 complex branch. With §1, t≤28 excludes both support 45 and support 46. The proof never assumes a selected support, independent pair graphs, independent phase choices, a real tensor, or a fixed/equal phase pattern.

## 8. Exact global composition boundary

The direct t=26 branch exclusion is standalone. To turn the N=45/46 conclusions into statements for every AME(4,6) state, one must separately supply t≤28. S3 reports this under f113, classical no-OLS(6), and the prior t≤30 boundary; these are imports, not reconstructed here. Under t≤28, (1) first gives N≥44. At N=44 it forces t=28 and e=0, with four 2×2 residual blocks per cut; that case is not excluded in this reconstruction. At N=47, the elementary lemmas exclude t=25,26 but leave t=27,28 for further results. S3 separately reports a conditional whole-N=47 exclusion; I do not re-prove that source chain. At N=48, the elementary count leaves t∈{24,27,28}; S2 reports a conditional composition using additional alphabet/profile and branch imports, whose full original proofs are not in this packet and are not independently authenticated here. In particular S2 is an unadopted candidate, not an automatic no-48 disposition.

Consequently the present record alone cannot infer N≥49: a valid composition must independently close the ≤44, 47 and 48 cases at their actual boundaries as well as the 45 and 46 cases established here. S4's supplied parent disposition states a lower bound 44 at its no-OLS import and explicitly says the ≥45 successor was not adopted there; S3's reference to a recorded prior lower 45 is not, by itself, a reconstruction of that missing stronger source. The named 60-term witness is a separate recorded upper-bound result, not checked or used here. No support minimum, source identity, novelty, family/human/kernel verdict, or automatic parent adoption follows.

## 9. Exposure, coverage, and execution record

Before the direct PREBODY ACK to Main, I read the complete manifest, freeze receipt, final binding, prepared live metadata, actual dispatch receipt, and all 21 listed status/permission controls through their endings. The three assignment-supplied control SHA-256 hashes were checked with native shasum and matched. I read no science-packet body and performed no mathematical derivation before that ACK. Then I read the sole listed part in order, raw, in consecutive windows of at most 20 LF, through line 349 and its ending. The part's live SHA-256 was 0a0ed0ffc67947d5d13976794b6ce9e6be2854bcc1de3a5e5f90d273401b508a, matching the manifest. The packet contains complete S1 (141 LF; 3a4a84350b561c58c43b0c2dd2db49d50032a0ca9b621b6896ef0fc027b964ef), S2 (137 LF; a65362c7ee5477e176f2a0ccf07f0dae1277731c132b00a5a4087d520dc5c2bf), S3 (17 LF; 4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003), and S4 (36 LF; c6e578a2555f476c45ac5e3e31753fceda1e855c1d5a3adf90847f477444d90a). Those individual source bindings and byte-roundtrip were parent-supplied; I did not separately open the source paths or reproduce the packet writer. The source candidate S1 was a nonblind input and its source-overwrite/packet-process historical qualifications remain as stated in the packet and status controls, not cured by this work.

All held episodes and all their consumers remained NONINPUT. I did not follow links, read old code, sibling proofs or held history, use an external-model CLI, perform scientific child execution, run a solver, build, test, lint or formatter, or perform a finite search. Mathematical cases and identities above are written reasoning, not executable evidence. Parent intake and any finite GO are separate. Native clock observed before creation of this record: 2026-10-30T16:40:04-0700 PDT; this is not a filesystem-creation timestamp.
