# Universal boundary routing in T1/T2: actual-row cycle lengths, a parity identity, and unique Latin completion

Owner **InfoRecursiveMDS18-2**, info-4. Actual native clock observed before writing: **Wed Oct 28 22:13:01 PDT 2026**.

**NEW author-WRITTEN candidate, unreviewed.** All results are quantified over actual unrestricted linear arrays. Inputs are the T1/T2 definition, elementary permutation signs and finite counting only. No scientific execution, selected array, external theorem, solver receipt, held guidance or unexecuted encoder is an input. No formal/kernel, independent-model, novelty or parent-adoption claim.

## 1. Canonical completion of every local predecessor-to-successor map

Let A be any T1(n), n≥2. Each symbol starts exactly one row and ends exactly one row: its n−1 incoming and outgoing arcs must each occur once. Index row R_s by its first symbol s. Write E(s) for its last symbol. Thus E is a permutation of the symbols with no fixed point.

For each symbol b define:

- P_b: the penultimate symbol of the unique row ending in b;
- Q_b: the second symbol of the unique row starting in b.

For each consecutive triple (a,b,c) in any row, map a↦c at middle symbol b. The incoming arcs at b show that its n−2 interior occurrences have predecessor set S\{b,P_b}; the outgoing arcs show that their successor set is S\{b,Q_b}. Both lists have no repetitions by T1. Thus they give a bijection between these two sets. Complete it uniquely to a permutation σ_b of S\{b} by setting

σ_b(P_b) = Q_b.                                           (1)

The added pair is called the boundary pair at b. No claim of Latin completion is needed here: the σ_b always exist for every T1 array. Apart from (1), σ_b has no fixed point, because a consecutive triple in a permutation row has distinct outer symbols. Consequently σ_b has either no fixed point or exactly one, the latter occurring precisely when P_b=Q_b.

## 2. Actual-row routing has prescribed cycle lengths

Let Ω={(a,b)∈S² : a≠b}, and define the permutation

Φ(a,b) = (b,σ_b(a)).                                      (2)

It is bijective because each σ_b is a bijection of S\{b}. Within an actual row, Φ sends one directed adjacency to the next. At the final adjacency (P_b,b), equation (1) sends it to (b,Q_b), which is the first adjacency of row R_b. Thus Φ follows the actual row and then continues with the row whose first symbol equals the previous row's last symbol.

Let E have cycles of lengths k_1,…,k_c. The adjacencies of all rows in one E-cycle concatenate to one Φ-cycle of length (n−1)k_i. They are distinct by T1, and there is no earlier return: a row path reaches its final adjacency before crossing into the next row; the corresponding row transition is exactly E. These cycles partition Ω. Hence

cycle lengths of Φ = {(n−1)k_1,…,(n−1)k_c}.                (3)

This uses the actual Hamiltonian rows, not an arbitrary marginal transition system. In particular, a collection of local bijections with unrelated Φ-cycles does NOT establish an original row realization.

## 3. Universal sign identity

Let τ(a,b)=(b,a). It is the product of n(n−1)/2 disjoint transpositions on Ω. Let F(b,a)=(b,σ_b(a)); it preserves each fibre with first coordinate b, and sign(F)=product_b sign(σ_b). Since Φ=F∘τ,

sign(Φ) = (−1)^[n(n−1)/2] · product_b sign(σ_b).           (4)

By (3), sign(Φ)=(−1)^[n(n−1)−c]=(−1)^c. Also sign(E)=(−1)^[n−c]. Substitution gives the all-variable necessary identity

product_b sign(σ_b) = (−1)^[n(n+1)/2] · sign(E).            (5)

For the original order n=11, n(n+1)/2=66 is even, so

**product_b sign(σ_b) = sign(E).**                         (6)

No parity is substituted from a particular candidate, and (6) is NOT a contradiction: it couples the eleven local permutations to the global endpoint permutation. The n−2 interior pairs alone do not determine the global row routing without the boundary completion (1) and cycle condition (3).

## 4. Exact T2 multiplicities and the Latin-completion question

Now suppose A is T2(n). Define T_ac to be 1 when (a,c) occurs as an original LINEAR distance-two pair, and 0 otherwise. Let

B_ac = #{b : (P_b,Q_b)=(a,c)}.

The n(n−2) original triples together with the n added boundary triples exhaust all entries of all σ_b. Therefore, for every pair a,c (including a=c),

#{b≠a : σ_b(a)=c} = T_ac + B_ac,                          (7)

where σ_b(a) is defined only if b≠a. In particular T_aa=0, all original T_ac are 0 or 1, and every extra multiplicity in the completed routing is exactly accounted for by a boundary pair. Equation (7) is an actual common-row coupling, not a claim that arbitrary matrices T and B satisfying degree counts can be realized.

Build an outer-triple partial Latin square L as follows: at cell (a,c), enter b for every original consecutive triple (a,b,c), and put a on each diagonal cell (a,a).

- Cells are unambiguous by T2.
- Row a contains no repeated entry b: repetition would reuse adjacency a→b.
- Column c contains no repeated entry b: repetition would reuse adjacency b→c.
- The diagonal additions cause no repetition, since every original triple uses three distinct symbols.
- Each symbol b occurs n−2 times as an interior middle symbol, plus its diagonal occurrence; thus it occurs exactly n−1 times.

The only row missing symbol b is row P_b, and the only column missing it is column Q_b. For rows this follows from the unique omitted adjacency a→b, namely the one ending row at b; the column argument uses the unique omitted adjacency b→c, namely the one starting row at b. Therefore **any full Latin completion preserving all displayed cells is forced to place b at (P_b,Q_b)**.

There are exactly n empty cells. Let M be the set of off-diagonal pairs absent from T (the n missing original distance-two pairs). The diagonal is already filled. Thus the following are equivalent:

1. L has a full Latin completion;
2. the n ordered boundary pairs (P_b,Q_b) are all distinct, all off-diagonal and absent from T;
3. their multiplicity matrix B is exactly the 0/1 incidence matrix of M.

When these hold, the completion is **unique**, obtained by adding precisely those n forced entries. Its permutation describing the positions of each symbol b, restricted off its own diagonal, is σ_b, so its product of symbol-position permutation signs is governed by (5), in particular by sign(E) at n=11.

This is NOT the separate construction inserting an extra symbol to form circular Hamiltonian rows. Here no extra symbol is introduced: rows are concatenated by their shared endpoint/start symbols, producing the Φ-cycles in (3), generally much longer than n.

## 5. Scope and remaining gap

**WRITTEN universal necessary conditions:** the canonical local completions (1), the exact actual-row cycle lengths (3), the parity identity (5) for every T1(n), and the multiplicity coupling (7) for every T2(n).

**WRITTEN conditional completion theorem:** for every actual T2(n), its outer-triple partial Latin square has a full completion if and only if B equals its missing-pair matrix; if so, the completion is unique.

**NOT proved:** that B must equal the missing-pair matrix in any or every T2(11), that the boundary-completion route is necessary for original existence, that local parity or degree counts force actual rows, or that a compatible family exists. No original-array no-go or witness follows. The unrestricted T2(11) problem remains **OPEN**, with no support-9 or novelty promotion.
