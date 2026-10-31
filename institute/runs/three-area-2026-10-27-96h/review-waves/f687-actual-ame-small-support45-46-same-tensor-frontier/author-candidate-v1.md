# Author candidate: the original support-45/46 frontier at the named maximal-count boundary

**Status: fresh author proof, unadopted and not independently reviewed.** The proposed theorem is that, for one normalized complex AME(4,6) tensor in any product basis, neither support 45 nor support 46 is possible **provided that the tensor has at most 28 coefficients of modulus 1/6**. The mathematical proof below is unconditional for each of the individual branches it treats; the displayed upper bound is needed only to make their list exhaustive. It is not an unconditional all-support minimum claim.

More precisely, the written proof excludes N=45 at t=27,28 and N=46 at t=26,27,28, for arbitrary complex amplitudes and the SAME tensor in all three balanced cuts. The retained import for the conditional composition is the literal S6 statement that every normalized complex AME(4,6) state in any product basis has t≤28, **conditional on its adopted f113 provenance, including classical no-OLS(6) and the prior t≤30 boundary**. S6 is `dispositions/physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md`, SHA-256 `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003`, especially its literal lines 1–11 in the frozen packet. This candidate neither reconstructs nor authenticates that underlying source chain or no-OLS theorem. No other mathematical result from the packet is imported below. In particular, none of the support-48 conclusions is used as an assumed lower-support theorem.

No N≥49, exact minimum, support ≤44 exclusion, witness, original-source identity, novelty, family/human/kernel acceptance, or parent disposition is claimed here. The mathematical argument and its provenance must be checked separately before adoption.

## 1. One tensor, unitarity, and elementary support components

Let ψ be the actual normalized state, U=6ψ, N its number of nonzero entries, P its set of t entries of modulus one, and E the remaining nonzero entries. In every balanced cut, U is a 36-by-36 unitary matrix: the two-party reductions of ψ are I/36. The same complex entry U(w) occurs in every flattening. A unit-modulus entry exhausts its row and column, so P is injective on every one of the six physical pair projections, and no E entry uses any of those pair values. Deleting the t occupied singleton rows and columns leaves an n-by-n unitary V in each cut, where

    n = 36−t,   |E| = N−t,   e = |E|−2n = N−72+t.

Every line of V has at least two nonzeros: a one-entry unitary line would have modulus one and belong to P. In particular N≥72−t. Distinct rows cannot meet in exactly one nonzero column, and the analogous statement holds for columns; a single nonzero product cannot sum to zero. These facts use arbitrary actual complex amplitudes, not a support-only replacement for unitarity.

A connected component of the bipartite support of V is square. Indeed its isolated r-by-c submatrix has orthonormal rows and columns, so r≤c and c≤r. For a component of order m define its excess as its number of entries minus 2m. Both line-degree bounds make this a nonnegative integer. We need the following small-excess classification, proved here for any complex unitary with minimum line degree two.

* **Excess zero:** every row and column has degree two. For a row with columns a,b, any other row meeting it must also use both a,b. Because each of a,b has degree two, there is exactly one such other row, and it has no further neighbor. The component is a complete 2-by-2 block. Thus every zero-excess unitary has even order and consists of such blocks.
* **Excess one is impossible:** the row degrees consist of one 3-row and otherwise 2-rows. Each of the three columns of the 3-row needs a 2-row neighbor. Such a neighbor uses two columns of that 3-row; two distinct chosen pairs would overlap once, forbidden. Therefore all these 2-rows use one pair, leaving the third column with degree one, a contradiction.
* **Excess two:** if one row has degree four and all others degree two, every 2-row meeting that row uses a pair of its four columns; these pairs are equal or disjoint, and must cover all four columns. They therefore form two disjoint pairs. A column from each pair meets the other in precisely the degree-four row, contradiction. Otherwise there are two 3-rows. Their supports cannot meet in one column. If they meet in exactly two, a 2-row meeting a private column of the first must use another column of the first, but then it meets the second 3-row in exactly one column; hence that private column would have degree one. If the supports are disjoint, 2-rows meeting either support use pairs entirely inside it, and 2-row chains cannot leave those pairs, so the two 3-rows cannot be in the same component. If the supports coincide, every adjacent 2-row uses a pair of their common three columns, and distinct pairs are forbidden by one-overlap. All such rows use one pair and cannot connect to any other column. The component has exactly three columns and, by squareness, three rows: it is the eight-entry 3-by-3 block obtained by deleting one entry. Consequently an overall excess-two unitary consists of this one order-three component and zero-excess 2-by-2 blocks, and has odd order. Two excess-one components cannot occur.

At N=45 the count inequality and t≤28 give t=27 or 28. At t=27, n=9 and e=0, contradicting even order; at t=28, e=1, impossible. At N=46 they give t=26,27,28. At t=27, e=1; at t=28, n=8 and e=2, contradicting the odd-order conclusion. It remains to exclude the entire t=26 branch, without any additional assumption.

## 2. The actual N=46, t=26 interface

Here P has 26 actual entries, E has 20 actual entries, and every cut has a residual 10-by-10 unitary of excess zero, namely five complete 2-by-2 blocks. Consequently every one of the six pair systems has exactly ten E-pair values, each with exactly two E extensions; the other 26 values are occupied exactly once by P. For a symbol x in party i, let s_i(x) be its number of E words and let d_i(x) be the number of its E-neighbors in any particular other party. The latter is independent of the other party because

    s_i(x)=2d_i(x),    p_i(x)=6−d_i(x),    Σ_x d_i(x)=10,            (1)

where p_i(x) is its number of P occurrences. This is the common marginal of the SAME P and E, not six independently chosen graphs. An E symbol has d_i(x)≥2: if it had one neighbor in each other party, its two E words would be the same tuple. Thus its residual alphabet size q_i is at most five. Also q_iq_j≥10 for each pair, since all ten pair values lie in the product of the two residual alphabets.

The actual residual phase equations are retained throughout. In any of the fifteen physical 2-by-2 blocks, writing its actual entries as [[a,b],[c,d]], unitarity gives

    |a|²=|d|²=s,  |b|²=|c|²=1−s,  0<s<1,
    a conjugate(c)+b conjugate(d)=0,
    a conjugate(b)+c conjugate(d)=0,  and  a d/(b c) is negative real.    (2)

Equivalently the phase sum around that actual rectangle is π modulo 2π. The same entry and phase appear in its blocks in the other cuts. In particular, the forthcoming sign propagation is a consequence of (2), not an independently feasible graph or a fixed-phase ansatz; no equality of all E moduli is assumed.

## 3. A binary-block obstruction, and exclusion of distance one

### 3.1 Four binary parties cannot be AME

For completeness, suppose a normalized four-qubit state had every two-qubit marginal I/4. Its three-qubit marginal has the form ρ=(I+M)/8, with M a real linear combination of weight-three Pauli strings: all weight-one and weight-two terms vanish. The complementary qubit is I/2, hence ρ has two nonzero eigenvalues 1/2 and ρ²=ρ/2. Therefore M²=3I+2M. In M², anticommutators of two weight-three Pauli strings vanish when they differ at an odd number of sites; if they differ at zero or two sites the surviving product has weight zero or two. Thus M² has no weight-three part, forcing M=0, which contradicts M²=3I.

Accordingly, if two symbols per party support eight E words that exhaust all four values of **every** physical pair, each twice, they give a forbidden four-qubit state. Every such pair value is already exhausted by E, so no other E or P entry can use it. All three 4-by-4 sub-flattenings are consequently isolated unitary blocks of the same U; division by 2 normalizes that same binary subarray. One-cut closure alone would not suffice.

### 3.2 No two E words differ in exactly one coordinate

Suppose instead that two words differ only in the fourth coordinate, with values d0,d1 and a common base triple s=(a,b,c). In each of the three cuts, the complete 2-by-2 support block containing these two entries supplies another base triple with both fourth-coordinate values. Close under these operations and let S be the resulting connected set of base triples, of size m.

Each base symbol occurs in exactly two S triples, because its pair with d0 is an E-pair value of multiplicity two. Two S triples cannot share two base coordinates: each contributes both d0 and d1, which would give that base-pair value at least four E extensions. Thus, joining two S triples when they share a base symbol gives a simple 3-regular graph. For adjacent triples s,s' sharing, say, c, column orthogonality in the ab|cd cut gives the actual complex relation

    z_s + z_s' = 0,       z_s := U(s,d0) conjugate(U(s,d1)) ≠ 0.       (3)

All edges obey the same relation, so this connected graph is bipartite. A simple cubic bipartite graph has equal parts of size at least three; m is even and at least six. Since S×{d0,d1} uses 2m of the 20 E words, m∈{6,8,10}.

In every physical pair, the S block uses exactly m values, each already twice: base-base projections are injective on S, and a base symbol occurs twice with each of d0,d1. Thus all remaining E words have exactly 10−m pair values in each system, each twice, and no P value overlaps the S block.

* If m=10, S uses five symbols in each base party and all E uses only d0,d1 in the fourth. Each dν has d=5 and hence exactly one P occurrence. Because every base residual symbol paired with dν is already used by E, the three base coordinates of this P word are the unique symbols outside the five used alphabets. The P words for d0 and d1 therefore share all three base coordinates, contradicting pair injectivity.
* If m=8, four E words remain, with exactly two pair values in every system, each twice. For any variable coordinate their four occurrences split into two equal parts. Two variable coordinates have only two joint values, so these partitions coincide. All variable coordinates therefore induce the same partition, giving at most two distinct words, not four.
* If m=6, eight E words remain, with exactly four pair values in each system, each twice. The same marginal argument as in (1) gives degree at least two for each used symbol, so each residual alphabet has at most two symbols. An alphabet of size one is also impossible: then each of the other three coordinates has four symbols, each occurring twice; the four values of any pair among them make each symbol in one coordinate determine the other two, leaving at most four distinct words. Hence every remaining alphabet has exactly two symbols and each pair has all four values, twice. These eight actual E words form the forbidden isolated binary block of §3.1.

All three possibilities are impossible. Thus the actual E support has Hamming distance at least two. This conclusion used the actual phase products (3) and all three cuts; it is not an assumption on a selected support.

## 4. Degree-two symbols and the three-low obstruction

Call a residual symbol **low** if d=2, and **high** if d≥3. This terminology is local to this proof. The four E words at a low symbol use exactly two symbols in each of the other parties, each twice. They are four distinct vertices of a 3-cube with no distance-one pair. They must be one parity class: if two chosen vertices had opposite parity, absence of distance one would make them antipodal, whose neighbors exhaust the other six cube vertices, leaving no third chosen vertex. Hence the slice is a complete four-word parity class. In particular its projection to any two of the three other neighbor sets is the entire 2-by-2 product, once per cell.

Construct the simple graph on all low symbols, with an edge whenever their physical pair is used by E. There is **no triangle** in this graph. To see this, take three pairwise adjacent low symbols in three different parties. Their low slices have four words apiece. For any two of the three, the two words at their shared pair value differ in both remaining coordinates, by distance at least two; they therefore exhibit and identify both neighbor symbols in each remaining coordinate for both slices. The three slices consequently lie in a single 2-by-2-by-2-by-2 product box. Each is one parity class in its fixed-coordinate 3-cube, and their nonempty pairwise intersections force the same four-bit parity class. Their three pairwise intersections have size two and their triple intersection has size one: the latter exists because any two neighbor values in a low slice occur together. Their union therefore contains seven of the eight vertices of one four-bit parity class.

The eighth vertex is forced by the original unitary. For two of the low parties use the pair as a row label. The row with both low symbols and the row with both alternative symbols share the column given by the third low symbol and its corresponding fourth symbol; both words are among the seven. Distinct rows cannot overlap in exactly one column, and both have degree two, so their two column supports coincide. The other column of the first row supplies the eighth vertex. Those eight words exhaust all four pair values in all six systems, each twice, and yield the forbidden binary block of §3.1. Thus no such triangle exists.

Two consequences will be used repeatedly:

1. If a low symbol has low neighbors in two different other parties, its parity slice contains a word using both neighbors; they are adjacent and form a forbidden triangle. Hence **all low neighbors of any one low symbol are in one other physical party**.
2. If a word contained three low symbols, its three pair values would form a forbidden triangle. Hence every E word contains at most two lows.

These are universal conclusions for the actual complex tensor, not a selected-instance or independent pair-graph theorem.

## 5. Exhausting the residual alphabet sizes

A size-one residual alphabet is impossible: q_iq_j≥10 while q_j≤5. If q_i=2, every other q_j must equal five, and each of the ten pairs in the 2-by-5 box is used by E. Each of the two i-symbols has d=5 and exactly one P occurrence. In each other party there is just one symbol outside its five-symbol E alphabet, and a P word carrying either i-symbol must use that outside symbol. The two P words then share all other three coordinates, contradicting P pair injectivity. Thus q_i∈{3,4,5}; at most one q_i is three, since 3·3<10.

If at least two parties have q=5, every one of their symbols is low. Among the other two parties, at least one is q=4 or 5, since two q=3 parties are impossible; it has a low symbol. That symbol has low neighbors in both q=5 parties, contrary to §4. Thus at most one q_i is five.

Suppose exactly one party D has q_D=5. At least two others, B and C, have size four. A size-four degree multiset is either (2,2,2,4) or (2,2,3,3). Every low B symbol has two low D neighbors, so by §4 its two C neighbors are high. Hence C has at least two high symbols and is of type (2,2,3,3); symmetrically so is B. There is no low-low B–C edge. Their ten-edge residual pair graph consequently consists of complete low-B/high-C and high-B/low-C 2-by-2 graphs and a perfect matching between the two high sets.

Each of the five low D symbols has two B and two C neighbors, and its parity slice makes those neighbors a complete 2-by-2 subgraph. The displayed B–C graph has exactly two such subgraphs: low-B × high-C and high-B × low-C. The two low B symbols have four incidences with D, so exactly two D symbols use the first subgraph. Similarly exactly two use the second, since the two low C symbols have four incidences with D. This accounts for only four of the five D symbols, a contradiction. Therefore no q_i is five.

The only remaining sorted profiles are 3444 and 4444. Both will be excluded, for the same actual P and E.

## 6. The entire 3444 profile

Let A have q_A=3 and B,C,D have size four. Since each symbol's degree is at most the size of the opposite alphabet, every size-four party has degrees (2,2,3,3), and A has degrees either (2,4,4) or (3,3,4).

For a P word w let k(w) count how many of its four symbols lie in the corresponding E alphabets. Using the exact E/P complement in every physical pair,

    Σ_P k = 6(3+4+4+4)−40 = 50,
    Σ_P binom(k,2) = (3·4+3·4+3·4+3·16)−60 = 24.

There are 26 P words. Since binom(k,2)−k+1 is respectively 1,0,0,1,3 for k=0,1,2,3,4, its total is 24−50+26=0. Thus **every P word has k=1 or k=2**, with exactly two of the former.

For an A symbol of degree d, the numbers of its P neighbors inside B, C and D are each 4−d. These three sets of P words are disjoint because k≤2. Its total number of P words is 6−d, hence 3(4−d)≤6−d, or d≥3. Thus A has degrees (3,3,4), not (2,4,4). For d=3, all its three P words have one other residual coordinate; for the degree-four symbol z, its two P words have no other residual coordinate. Those two words are exactly the two k=1 words.

Write u and v for A's degree-three symbols. In each of B,C,D, both high symbols neighbor all three A symbols; each low symbol neighbors z and exactly one of u,v. Each of u,v neighbors one of the two low symbols and misses the other. The two z-words use outside symbols in B,C,D and differ in each of those coordinates by P pair injectivity. Label the two outside symbols of each of B,C,D as 0,1 so that these z-words are (0,0,0) and (1,1,1).

For a degree-three A symbol, its three P words have respectively B, C, or D residual and the other two coordinates outside. Let the B-outside value in its C-residual word be r. Pair injectivity with the z-words, and between the three words sharing this A symbol, forces their outside coordinates to be

    B-residual word: (C,D)=(1−r,r),
    C-residual word: (B,D)=(r,1−r),
    D-residual word: (B,C)=(1−r,r).                              (4)

For example, if the C-outside value in the first word is c, injectivity at the common A symbol gives the third word B=1−r,C=1−c; the two z-words prohibit equal outside B,C, so c=1−r. The other values follow in the same way. The two degree-three A symbols have different r, since otherwise their B-residual words share a C,D pair. Relabel them u_0,u_1 according to r. Let b_r,c_r,d_r be the unique low B,C,D symbols not neighboring u_r in E. Equation (4) identifies the three actual P words

    (u_r,b_r,1−r,r), (u_r,r,c_r,1−r), (u_r,1−r,r,d_r).          (5)

For each r, the residual pair (b_r,c_r) must be used by E. Otherwise P occupies that pair; since k≤2 its A and D coordinates must both be outside. Its D value cannot be r, by the first P word in (5), and cannot be 1−r, by the second. The same argument for (b_r,d_r), using the first and third words and an outside C value, and for (c_r,d_r), using the second and third and an outside B value, shows that both of those pairs also belong to E. Thus b_r,c_r,d_r are three pairwise adjacent low symbols, contradicting §4. This excludes the entire 3444 profile, not merely a particular arrangement or choice of phases.

## 7. The entire 4444 profile

Each party has either degree multiset (2,2,2,4) or (2,2,3,3). Suppose there is a low-low E edge between parties i and j. A low endpoint cannot have a low neighbor in either complementary party, by §4, so its two neighbors in each complementary party are high. Those parties must therefore each have two highs and hence type (2,2,3,3). The endpoint's parity slice uses all four high-high values in their pair graph.

For two parties of type (2,2,3,3), let x be the number of low-low edges. The low/high degree totals give the four quadrant counts

    LL=x,  LH=4−x,  HL=4−x,  HH=2+x.                              (6)

All four high-high values are used, so x=2 in the complementary pair. Applying the preceding argument to either of those two low-low edges shows that i and j also have two highs, and (6) shows that their pair also has exactly two low-low edges. Therefore, if any low-low edge exists, all four parties are of type (2,2,3,3), every nonempty physical pair of parties has exactly two low-low edges, and its complementary pair is also nonempty with exactly two.

There can be only one such complementary pairing. Indeed, if two different pairings were nonempty, then at every party some low symbol would need a neighbor in each of two different other parties. By §4 the sets of low symbols used for those two destinations are disjoint. There are exactly two low symbols, so each pair graph would have only one available low vertex at each end and hence at most one edge, contradicting its required two. Thus the entire low-symbol graph has at most four edges.

On the other hand the all-(2,2,3,3) case has eight low symbols, each appearing in four E words, for 32 low-coordinate incidences. Every E word has at most two lows. If N_2 is the number with two lows, then 32≤20+N_2, so N_2≥12. Each low-low pair value has exactly two E extensions, and no word has three lows, so N_2 is exactly twice the number of low-low graph edges. The graph has at most four edges, giving N_2≤8, contradiction. If no low-low edge existed initially, the same incidence count is already impossible because there are at least 32 low incidences among 20 words and each word would have at most one low. Hence the entire 4444 profile is excluded.

Sections 5–7 exhaust every actual N=46,t=26 tensor. Together with §1 they prove the branch statements and the conditional support-45/46 exclusion stated at the beginning. No residual global phase predicate is being declared solved by an independent graph assignment: the contradiction follows under all actual complex phases from the one tensor, with the phase products and every pair complement retained as shown.

## 8. Record of inputs, execution, and assurance

Native clock observed before this artifact's creation: 2026-10-30T16:34:04-0700 PDT. Before any packet body or mathematical derivation, the complete manifest, freeze receipt, prepared parent metadata, actual dispatch, and all 20 status/permission controls were read through their endings; a direct PRE-BODY ACK was delivered to Main. Thereafter the entire 251-line literal packet was read in order in raw ranges of at most 20 lines. After that read, native `shasum -a 256` reported manifest `caa786d90b24eb1f5d09b09790a96845f939c26b9024f12cb6bcd73460b0ea93`, freeze `780cb8850371a6a0e02f006b54300bbc4ad276363c83da818b05a4a4e8a1f8e9`, and packet `1c6f94d350a4846ed47e33bb9ef347315c345d021d43431725720d310be9f7bc`, matching the prepared bindings. These are metadata observations, not a proof check. The packet was an allowed, nonblind input; the S6 t≤28 dependency is the only mathematical import used for the conditional composition.

The argument is written derivation, including prospective abstract cases; no selected tensor, scientific program, numerical calculation, finite search, child execution, source follow, external CLI, linked old author code, sibling proof, held episode, or held consumer was used. No source/novelty verification or independent scientific review was performed. All new claims above remain author candidates until separate parent intake and appropriate disjoint review; none inherits an old constrained-WRITTEN PASS. The conditional upper-bound provenance and the exclusion of support ≤44 from the present proof remain explicit dependencies on any stronger global-minimum claim.
