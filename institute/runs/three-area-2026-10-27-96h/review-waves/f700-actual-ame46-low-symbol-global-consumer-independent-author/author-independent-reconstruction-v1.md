# Independent nonblind reconstruction: actual AME(4,6), N=45 and N=46

**Result: complete written candidate, not a parent disposition.** For a single normalized complex AME(4,6) tensor in any product basis, the cases (N,t)=(45,27),(45,28),(46,26),(46,27),(46,28) are impossible, where t counts coefficients of modulus 1/6. The (46,26) proof below uses only the three actual unitary flattenings and their shared amplitudes and support, not t≤28, no-OLS, or an equal-magnitude assumption. Thus **assuming t≤28**, N=45 and N=46 are both excluded. The supplied S3 records t≤28 only conditional on its f113 provenance, including classical no-OLS(6) and the prior t≤30 boundary; I do not independently authenticate that chain. The unconditional branch proof does not inherit it.

This is a new, nonblind independent reconstruction of the S1 proposal, not an acceptance, a family/human/kernel review, an original-source authentication, or a novelty claim. I found no unpaid mathematical case within the stated branches in the reconstruction below. In particular I do not infer N≥49 or the global minimum. S4's stated lower bound is 44 at its named import; N=44 is not excluded here. S3's separate N=47 disposition and S2's support-48 composition are not proved or adopted by this document. Without the t≤28 import, higher t values are not exhausted by this proof.

## 1. Original tensor, six pair projections, and actual complex phases

Write U=6ψ and take the same four parties A,B,C,D throughout. The balanced flattenings AB|CD, AC|BD and AD|BC are 36×36 unitaries; there is one common complex entry U(a,b,c,d) in all three. Let P be the t entries of modulus one and E the other nonzero entries. A modulus-one entry exhausts its row and column, so P projects injectively to each of AB, AC, AD, BC, BD, CD, and an E word cannot share a pair value with P. In any cut deletion of the occupied singleton rows and columns gives a unitary V of order n=36−t with N−t nonzeros. Every remaining line has degree at least two, since a singleton would have modulus one and belong to P. Therefore

    e = (N−t)−2(36−t) = N+t−72 ≥ 0.

Two distinct rows of a unitary cannot have exactly one common nonzero column: their inner product would be one nonzero complex product. The same holds for columns. Every connected support component has equal row and column counts, since its isolated rectangular submatrix has both orthonormal rows and orthonormal columns.

For later use, every full 2×2 component of V has its *actual* entries

    [a b; c d],   a,b,c,d ≠ 0,
    |a|²=|d|²,  |b|²=|c|²=1−|a|²,
    a conjugate(c)+b conjugate(d)=0,
    a conjugate(b)+c conjugate(d)=0,
    ad/(bc) is negative real.

The last equation follows by rearranging the first orthogonality equation. These relations apply to the same U entries wherever they appear in the other cuts. Nothing below assigns separate amplitudes to different cuts or declares every residual modulus equal.

## 2. Unitariy-support classification and the simple count cases

The following classification applies to any square complex unitary whose line degrees are at least two. The total excess is the sum of degree−2 on either side, and each connected component has nonnegative excess.

* Excess 0: every line has degree two. If two rows meet, their two-column supports coincide by the no-one-overlap rule. The two columns then have no other row neighbor, so that component is a full 2×2 block. The order is even.
* Excess 1: exactly one row R has degree three, all others degree two. Every other row meeting R must use a pair of R's three columns. Two different such pairs would overlap once; hence all use the same pair. The third column has no neighbor except R, contradicting its minimum degree two.
* Excess 2: an excess-one component is impossible. In the unique positive-excess component either one row R has degree four and every other row degree two, or two rows R,S have degree three and every other row degree two. In the former case all degree-two rows touching R use pairs of its four columns; distinct such pairs are disjoint, and minimum column degree forces two disjoint pairs covering all four columns. A column from each pair meets the other in R alone, contradicting column orthogonality. In the latter case R,S cannot meet in one column. If they meet in two, another row at R's private column must use a second column of R and so meets S exactly once. If they are disjoint, any degree-two row touching R stays entirely inside R's support, so the component cannot reach S. Hence R and S have the same three columns. Every adjacent degree-two row stays inside those columns, making the component isolated on three columns; squareness gives three rows. Its support is the full 3×3 array with one missing entry. All other components are 2×2, so the total order is odd.

At N=45, e=t−27. Under t≤28, t=27 gives n=9 with zero excess, and t=28 gives excess one; both are impossible. At N=46, e=t−26. Under t≤28, t=27 has excess one, and t=28 has excess two but even order n=8; both are impossible. Each of these individual contradictions is unconditional. We now treat (N,t)=(46,26) without an upper-bound import.

## 3. Exact N=46, t=26 interface and binary obstruction

There are |P|=26 and |E|=20 words. In **each** cut the 10×10 residual has excess zero, hence five full 2×2 blocks. Consequently, for each of the six physical pairs, the 36 pair values partition into 26 values used once by P and 10 values used twice by E. This exhausts every pair system; there are no further extensions of an E-pair value and no P/E overlap. The same P, E, and twenty complex numbers U(w) satisfy all three cut decompositions simultaneously.

For any symbol x of party i, let s_i(x) be its number of E occurrences, p_i(x) its P occurrences, and d_i(x) the number of its E neighbors in another party. The six pair partitions imply, for **every** choice of the other party,

    s_i(x)=2d_i(x),   p_i(x)=6−d_i(x),   Σ_x d_i(x)=10.       (1)

Thus d_i(x) is independent of the other party. An E symbol has d_i(x)≥2: if d_i(x)=1, all three other coordinates are fixed, but (1) requires two distinct E words. Its E alphabet size q_i is at most five. Each physical pair uses ten different values, so q_i q_j≥10.

We also need a closed binary-block obstruction. Suppose two symbols per party support eight E words with each of the four pair values in **every** physical pair occurring twice. The original two-extension rule says those pair values are already exhausted and P cannot use them. In any one of the three cuts, the four selected pair rows have no entries outside the four selected pair columns. Their 4×4 submatrix is therefore unitary; this holds for the same subarray in all three cuts. Dividing it by 2 would give a normalized four-qubit AME state.

Such a state cannot exist. Its three-qubit reduced density matrix has two nonzero eigenvalues, both 1/2, and all its one- and two-qubit marginals are maximally mixed. Its Pauli expansion is ρ=(I+M)/8 with M Hermitian and consisting only of weight-three Pauli strings. The identity ρ²=ρ/2 yields M²=3I+2M. In the symmetrized product of two weight-three strings, terms differing on an odd number of sites anticommute; terms differing on zero or two sites have weight zero or two. Hence M² has no weight-three part. This forces M=0 and then contradicts M²=3I. The binary obstruction consequently uses all six pair-exhaustion properties and all three cuts, not a support rectangle in only one cut.

## 4. No two E words have distance one: shared-phase propagation

Suppose two E words differ only in D, with common base triple s=(a,b,c) and D values d0≠d1. In AB|CD, the two columns (c,d0),(c,d1) belong to one full 2×2 block, so there is a second AB row and hence another base triple s' containing **both** D values and sharing c with s. The other two cuts give analogous operations sharing a or b. Close the base triples under these operations, obtaining a finite connected set S.

Each base symbol occurs in exactly two S triples: the pair (x,d0) has exactly two E extensions, and block closure puts both into S. Two different S triples cannot share two base coordinates, since each occurs with both d0,d1 and would give at least four E extensions of that base-pair value. Thus adjacency by a shared base coordinate is a simple 3-regular graph. Put

    z_s = U(s,d0) conjugate(U(s,d1)) ≠ 0.

For an edge sharing c, column orthogonality in the **same actual** AB|CD block gives z_s+z_s'=0; edges sharing a or b give the same relation in the other physical cuts. Since the z_s are nonzero, no odd cycle is possible. The connected graph is bipartite, its two sides have equal size at least three, and m=|S| is even with 6≤m≤10 because S×{d0,d1} uses 2m of the 20 E words. Hence m=6,8,10.

Every physical pair system uses exactly m pair values in this S block, each already twice: base-base projections are injective on S, while each base symbol occurs twice with each of d0,d1. Thus the remaining 20−2m words use exactly 10−m other pair values in each system, each twice.

* m=10: each dν has five E neighbors in each base party, so p_D(dν)=1. Its unique P word must use the one symbol outside each of those three five-symbol alphabets. The P words for d0,d1 then share their three base coordinates, contradicting pair injectivity.
* m=8: four E words remain, with two pair values in each system, each twice. Every coordinate has one or two values, and every variable coordinate splits the four words 2+2. For two variable coordinates, only two pair values force their partitions to be identical up to swapping the labels. Thus at most two distinct words remain, contradiction.
* m=6: eight words remain, with four pair values in each system, each twice. For any symbol in this residual set its multiplicity is twice its number of neighbors in each other party, and that number is at least two by distinctness of the words. Hence each residual alphabet has at most two symbols. An alphabet of size one would force four distinct neighbors in each other party, contradicting that bound. Every residual alphabet therefore has two symbols, and all four pair values in each system occur twice. They make the prohibited closed binary block.

Therefore any two E words have Hamming distance at least two. This was derived using the actual complex phase products, not postulated for a separately chosen support.

## 5. Low symbols, the seven-to-eight closure, and its exact cut

Call a symbol low when d_i(x)=2 and high otherwise. At a low symbol x, its four E words use two values in each of the other three parties. With distance one forbidden, those four vertices form one parity class in the resulting 3-cube: two opposite-parity nonadjacent vertices would be antipodal, and their neighbors exhaust the other six vertices, so they could not lie in a four-vertex independent set. In particular, the slice projects onto the complete 2×2 product in any two of the other coordinates, once per cell.

Form a simple graph on low symbols, with an edge for each E pair value connecting two lows in different parties. It has **no triangle**. To prove this with the actual same tensor, let low symbols a,b,c in A,B,C be pairwise adjacent. The two E words at (a,b) differ in both C and D, so they identify both C- and D-neighbor sets of the a- and b-slices. Likewise the two words at (a,c) identify the two B and D neighbors of a and c, and the two at (b,c) identify the two A and D neighbors of b and c. Thus all three slices lie in one common 2×2×2×2 physical box. Each is a parity class on its fixed-coordinate slice; their nonempty intersections force one common four-bit parity. The three slices contain precisely seven of its eight vertices: every vertex with at least one of A=a,B=b,C=c is present, and the vertex with all three alternative values is the only missing one.

Here is the load-bearing closure without an implicit row assumption. Label a,b,c by 0 in their respective binary alphabets and let the common parity be h∈{0,1}. In the **same** AB|CD cut, residual row AB=00 contains the columns (C,D)=(0,h) and (1,h⊕1), and residual row AB=11 contains (0,h), because the latter word has the low C symbol. The rows 00 and 11 are distinct physical pair values. Each occurs in E, so neither belongs to P; each has exactly two E entries. Their shared (0,h) entry is nonzero. Orthogonality excludes exactly one common column; since both rows have degree two, their supports coincide. The other column (1,h⊕1) is a legal distinct CD pair, so the actual eighth word (1,1,1,h⊕1) is forced. All eight words then exhaust all four values of all six pair systems twice, giving the prohibited closed binary block. This proves no low triangle.

Two consequences hold for the actual E. (i) All low neighbors of a fixed low symbol are in one other physical party: if low neighbors y,z were in different parties, the complete two-coordinate projection of its parity slice would contain a word with both and hence create a triangle. (ii) An E word contains at most two low symbols, since three would form a triangle.

## 6. Exhausting the alphabet profiles, including the q=5 count

A residual alphabet of size one is impossible by q_i q_j≥10 and q_j≤5. If q_i=2, all other q are five and both i-symbols have degree five. Each has exactly one P occurrence and all five E neighbors in every other party. Those two P words must therefore both use the unique outside symbol in each of the other three parties, violating pair injectivity. Hence q_i∈{3,4,5}, and at most one q_i is three.

A five-symbol party consists entirely of lows, since its five degrees sum to ten and each is at least two. A four-symbol party has at least two lows; its only possible degree multisets are (2,2,2,4) and (2,2,3,3). If two parties had size five, at least one of the other two would have size four or five, hence a low x. Its two neighbors in each of the size-five parties would be low, violating the one-destination conclusion of §5. Thus at most one party has size five.

Suppose exactly one party D has size five. Since at most one of the other three has size three, choose two four-symbol parties B,C. Any low B symbol has low D neighbors, so its two C neighbors must be high. Thus C has at least two highs and is type (2,2,3,3); symmetrically B is too. There is no low-low B–C edge. The B–C pair graph is therefore exactly the two complete 2×2 quadrants L_B×H_C and H_B×L_C plus a perfect matching between H_B and H_C: each high vertex has degree three and already meets both opposite lows. These are the graph's only 2×2 complete subgraphs, since a low and a high on one side have only one common high neighbor.

Each of D's five low slices selects two B and two C neighbors whose cross-product is an E subgraph, so it selects exactly one of those two complete quadrants. The two lows in B have four total D incidences, and each D slice selecting L_B×H_C accounts for two; precisely two D symbols select it. Similarly precisely two select H_B×L_C. Only four D symbols are accounted for, contradiction. No q_i is five.

Therefore the only sorted profiles are 3444 and 4444. This is an exhaustive reduction of the nine elementary profiles 3444, 3445, 3455, 3555, 4444, 4445, 4455, 4555, 5555; it does not replace the common physical pair systems by independent graphs.

## 7. The full 3444 case: exact P complement and all three forced low edges

Let A have size three and B,C,D size four. Since a B,C,or D symbol has at most three A neighbors, each four-symbol party has degree multiset (2,2,3,3). The three A degrees sum to ten and are at most four, so *both* (2,4,4) and (3,3,4) are initially possible.

For a P word w, let k(w) count coordinates in the corresponding E alphabets. From (1) and the exact P/E complement in all six physical pair systems,

    Σ_P k = 6(3+4+4+4)−4·10 = 50,
    Σ_P binom(k,2) = 3·(3·4)+3·(4·4)−6·10 = 24.

There are 26 P words, so Σ_P [binom(k,2)−k+1]=0. The summand at k=0,1,2,3,4 is respectively 1,0,0,1,3. Thus every P word has k=1 or 2 and precisely two have k=1.

For an A symbol of degree d, in each of B,C,D it has 4−d P neighbors inside that party's E alphabet. These correspond to disjoint P words because k≤2. There are 6−d P words with that A symbol, giving 3(4−d)≤6−d, hence d≥3. This eliminates (2,4,4), not by assumption, leaving A degrees (3,3,4). Let z be the degree-four symbol and u,v the degree-three symbols. The two P words with z have no other E-alphabet coordinate and are exactly the k=1 words. Their outside symbols differ coordinatewise by P injectivity; label the two outside values in B,C,D so those words are (z,0,0,0) and (z,1,1,1).

Both high symbols in each of B,C,D meet all three A symbols. Each low in those parties meets z and exactly one of u,v. Thus each degree-three A symbol has exactly one missing low in each of B,C,D. Its three P words have their sole other E-alphabet coordinate in B, C, or D respectively. Let r be the outside B value in its C-residual word. Avoiding the two z-words and avoiding repeated pairs among the three words with common A forces the outside pairs to be

    B-residual: (C,D)=(1−r,r),
    C-residual: (B,D)=(r,1−r),
    D-residual: (B,C)=(1−r,r).                              (2)

Indeed its C-residual D value must be 1−r; the B-residual D value must differ from that and is r, so its C value is 1−r; the last word must differ in B from the C-residual word and in C from the B-residual word. The two degree-three A symbols must have different r, since otherwise their B-residual words repeat the same CD pair. Name them u_0,u_1. Denote by b_r,c_r,d_r the lows missing from u_r in B,C,D. Their three actual P words are

    (u_r,b_r,1−r,r),  (u_r,r,c_r,1−r),  (u_r,1−r,r,d_r).   (3)

Each of the three low-low pairs b_r c_r, b_r d_r, c_r d_r must instead be in E. For example, if b_r c_r were a P pair, k≤2 forces its A and D coordinates outside; the first word in (3) forbids D=r, and the second forbids D=1−r. Likewise, a P word using b_r d_r would have outside C; the first and third words in (3) forbid C=1−r and C=r. A P word using c_r d_r would have outside B; the second and third words forbid B=r and B=1−r. The pair partition has no third option. Thus b_r,c_r,d_r are pairwise adjacent lows, contradicting §5. All possibilities in 3444 are excluded.

## 8. The full 4444 case: complementary pairs and low incidences

Each party has degree type (2,2,2,4) or (2,2,3,3). Suppose an E pair between i and j joins low symbols. By §5 either endpoint's two neighbors in each complementary party k,l must all be high. Hence k,l each have two highs, are type (2,2,3,3), and that endpoint's parity slice uses all four H_k×H_l pair values.

For any two type-(2,2,3,3) parties, let x be their number of low-low edges. The two low symbols on either side have total degree four, and the complete E pair graph has ten edges, so its quadrant counts are

    LL=x,   LH=4−x,   HL=4−x,   HH=2+x.                  (4)

Here all four HH values occur, so the complementary pair k,l has x=2. In particular it has a low-low edge; applying the same reasoning to that edge forces i,j to have two highs and all four of their HH values. Equation (4) then gives exactly two LL edges in i,j too. Therefore the existence of any low-low edge forces all four parties to have type (2,2,3,3), and every nonempty LL physical pair and its complementary pair each contain exactly two LL edges.

At most one complementary pairing of parties can be nonempty. Otherwise choose two different pairings. At each party their incident LL edges lead to two different physical destinations. By §5 the sets of low endpoint symbols assigned to those destinations are disjoint and both nonempty. There are exactly two low symbols, so each destination has exactly one available low at each end. A simple pair graph with one available endpoint at each end has at most one LL edge, contradicting the required two. This explicitly covers different assignments of the two low symbols to the two destinations. Hence there are at most four LL edges overall.

In the edge-present case there are eight low symbols, each occurring in four E words, so there are 32 low-coordinate incidences. Let N₂ be the number of E words with two lows. Every word has at most two lows, hence 32≤20+N₂ and N₂≥12. Each LL edge has exactly two E extensions, and no word has three lows, so N₂ is exactly twice the number of LL edges. The upper bound of four edges gives N₂≤8, contradiction.

If there is no LL edge, the 4444 parties may still include type (2,2,2,4); nevertheless each party has at least two low symbols, so there are at least 32 low incidences. With no LL edge, each of the 20 words has at most one low, giving at most 20 incidences, again a contradiction. This finishes every 4444 case and therefore the whole actual (46,26) branch.

## 9. Exact caller and remaining scope

Equivalently, the excluded branch asks for disjoint P,E⊂{0,…,5}⁴ with |P|=26 and |E|=20; P injective in every one of the six pair projections; no E projection meeting P; in each of AB|CD, AC|BD, AD|BC the residual graph on the ten unoccupied values of each side a union of five full 2×2 blocks; and one common choice z_w∈C with 0<|z_w|<1 making all fifteen actual 2×2 blocks unitary. Necessity follows from §3. Conversely, these conditions plus arbitrary unit phases at P make every original 36×36 flattening unitary, hence define the original AME state after scaling by 1/6. Sections 3–8 exclude this exact system; a support-only relaxation or independent block-phase choices are not substituted for it.

The count consequences for all N=45,46 require the separately stated t≤28 premise to rule out larger t, even though each branch analyzed above is unconditional. The packet's S3 states that premise with f113/no-OLS/prior-t≤30 provenance; its underlying proofs were not supplied for reauthentication. S4 reports the separate ≥44 result and a 60-term witness at its own boundaries. No mathematical claim concerning the existence or nonexistence of N=44, the separate N=47 or N=48 compositions, N≥49, exact minimum, optimality or novelty follows solely from this document. Parent intake, a distinct proof review, and any finite execution/GO remain separate; no finite execution was performed here.

## 10. Source coverage, process, and assurance

This is a nonblind original-tensor reconstruction of the complete F700 packet, not a blind prior-independent discovery. Before opening its scientific body I read the manifest, freeze receipt, final binding, prepared metadata, actual dispatch and all 21 listed status/permission controls through their endings, then sent Main the direct PREBODY ACK. After the ACK I read the sole ordered packet part, raw LF 1–349 consecutively in ranges of at most 20 LF, including the endings of complete S1–S4. No packet links, sibling proofs, held episodes, held consumers, old code or external-model CLI were followed or used. Manifest/freeze/final-binding live SHA-256 respectively matched `7c54445b4485e362e76ec1de915497edb5e30ba16ddca28bde0b961f9e642cda`, `1d37367ea4fe55fb9b3828ff2642372cf135567b93ad08bfe951a9fc6d82762c`, `13b5838f95653ba812d7ac0d519f975f757aa6f65198797f75cb152e156295ba`; the read packet's live SHA-256 matched `0a0ed0ffc67947d5d13976794b6ce9e6be2854bcc1de3a5e5f90d273401b508a`. Those hash commands and native clock observation are metadata operations, not scientific computations. The parent binding reports the source-to-packet roundtrip and source hashes; I did not separately open or authenticate the underlying linked files.

The read packet binds complete S1 to `3a4a84350b561c58c43b0c2dd2db49d50032a0ca9b621b6896ef0fc027b964ef`, complete S2 to `a65362c7ee5477e176f2a0ccf07f0dae1277731c132b00a5a4087d520dc5c2bf`, complete S3 to `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003`, and complete S4 to `c6e578a2555f476c45ac5e3e31753fceda1e855c1d5a3adf90847f477444d90a`. The conditional t≤28 source is S3 only as stated above; S2 is used to check the exact caller and count boundary, not as a substituted N=46 theorem. No science program, test, search, solver, external CLI, linked source or scientific child execution was run. All held episodes and their consumers remain NONINPUT. No cognitive-isolation certificate, independent model-family check, human check, kernel proof, reviewer pass or parent adoption is asserted.

Native clock observed before creation: 2026-10-30T16:40:34-0700 PDT; this is an observation, not a claimed file-creation time.
