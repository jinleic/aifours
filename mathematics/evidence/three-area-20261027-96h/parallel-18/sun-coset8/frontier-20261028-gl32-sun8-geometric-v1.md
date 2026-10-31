# A written Fano-plane proof of Sun8 for GL3(2)

**Status: WRITTEN, UNREVIEWED.** Every eight pairwise disjoint left cosets of subgroups of GL3(2) have two subgroup indices with gcd at least 8. This is a self-contained proof for this one finite nonabelian simple group using elementary group theory and 3-dimensional linear algebra; it does not import Jordan/Jones, Sun7, R8 or a classification theorem. It explicitly allows the seven distinct index-7 point stabilizers and their seven disjoint cosets. It makes no claim for all simple groups or arbitrary groups, no source-specific P7 equivalence, no novelty claim, and no independent/formal acceptance claim.

The author's earlier exact computation `frontier-20261028-gl32-sun8-v1.md` SHA `f54d7aa6fecce85a311d6314a656abc284f18bf958064254946e7027fa0f0823` found that all 1568 disjoint six-tuples of index-7 cosets have a coset complement. The Fano-plane proof below gives a written explanation and does **not** depend on that enumeration or its checker. This is nonblind follow-on reasoning, not a claim of independent discovery. Before earlier affected sources and successors, read the complete pre-source overlays `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, then `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, then `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. No historical hold is modified. Incidental cross-topic display remains disclosed and unused.

## 1. The group and simplicity

Let V=F2^3, P=V\{0}, and G=GL(V). The seven points are the elements of P; the seven lines are the two-dimensional subspaces, each represented by its three nonzero vectors. Every point belongs to three lines, every line has three points, any two distinct lines meet in one point, and three distinct lines have union at least six points. An ordered-basis count gives |G|=(8−1)(8−2)(8−4)=168. G is transitive on ordered pairs of distinct points, because any two distinct nonzero F2-vectors are linearly independent and extend to a basis. By duality it is also 2-transitive on lines.

For completeness, G is simple by the elementary class equation. The possible irreducible factors of a degree-three characteristic polynomial of an invertible matrix over F2 are x+1, x²+x+1, and the two irreducible cubics x³+x+1 and x³+x²+1. Primary decomposition and Jordan form give these conjugacy classes:

| Type | Class sizes | Reason |
|---|---|---|
| identity | 1 | one element |
| unipotent Jordan type 2+1 | 21 | N=vφ, v≠0, φ≠0, φ(v)=0 gives 7·3 choices |
| unipotent Jordan type 3 | 42 | the invertible centralizer has 4 polynomial elements |
| one linear and one irreducible quadratic factor | 56 | the invertible centralizer is F4* of size 3 |
| either irreducible cubic | 24,24 | each invertible centralizer is F8* of size 7 |

All matrices in each displayed type are conjugate for its characteristic polynomial and Jordan type. The sizes sum to 168. A normal subgroup is a union of classes containing the identity, and by Lagrange its size divides 168. Any nontrivial such union has size at least 22; the only proper divisors to consider are 24,28,42,56,84. The nonidentity class sizes other than 56 are divisible by 3. Thus size 56 is impossible modulo 3; sizes 24 or 42 would require including the class of size 56 and are too small; size 28 would require a class-size sum 27, impossible from 21,24,42,56; and size 84 would require 56 plus a class-size sum 27, also impossible. Hence G is nonabelian simple.

## 2. All index-seven subgroups and their cosets

Every point stabilizer has order 24, because G is transitive on P; every line stabilizer also has order 24 by duality. These are 14 distinct subgroups: a point stabilizer has point orbits of sizes 1 and 6, while a line stabilizer has point orbits of sizes 3 and 4.

Conversely let H have index 7, so |H|=24. Its action on seven points is intransitive because 7 does not divide |H|. Some H-orbit U has size at most 3. If |U|=1, H fixes a point. If |U|=2, the sum of the two distinct vectors is a nonzero H-fixed vector. If |U|=3, either the sum of its vectors is zero, in which case U is a line, or that nonzero sum is H-fixed. Thus H stabilizes a point or a line and, since both stabilizers have order 24, H equals it.

Consequently every index-7 left coset is one of the following events, with p,q points and L,M lines:

\[P(p,q)=\{g\in G:g(p)=q\},\qquad E(L,M)=\{g\in G:g(L)=M\}.\]

Two distinct point events are disjoint exactly when they have the same source p with different targets, or the same target q with different sources. Otherwise a linear bijection realizes the two compatible point mappings. The dual statement holds for line events. In particular, three or more pairwise disjoint point events form a common-source star or a common-target star; the same holds for line events.

A point event P(p,q) and a line event E(L,M) intersect exactly when the incidences agree:

\[p\in L\quad\Longleftrightarrow\quad q\in M.\]

Necessity follows from incidence preservation. For sufficiency, when incident choose bases beginning with p in L and q in M; when nonincident choose bases of L and M extended by p and q. A basis-to-basis map realizes the two prescribed images.

## 3. Six disjoint index-seven cosets leave one coset

**Lemma.** The complement of any six pairwise disjoint index-7 left cosets of G is another index-7 left coset.

By point-line duality, exchange point and line actions if needed, so at least three of the six are point events. Explicitly, identifying a line with the kernel of a nonzero covector, the group automorphism g↦(g^(-1))^T interchanges the point and line actions and preserves left cosets. Inverting every group element swaps source and target in both kinds of event and turns each left coset into a left coset of a conjugate subgroup. We may therefore take the point events to be P(p,q) for q in a set Q of distinct targets. Let a=|Q| and b=6−a be the number of line events; then a≥3. An event E(L,M) is disjoint from all these point events precisely when

- p∈L and Q is contained in the four points outside M; or
- p∉L and Q is contained in the three points of M.

If b=0 then a=6 and the complement is the point event with the seventh target. If b=1 then a=5, but neither a three-point line nor its four-point complement contains Q, impossible.

If b=2 then a=4. Both line events must have p in their source lines and the same target line M, since Q is exactly the complement of M. Their source lines are distinct and are two of the three lines through p; let L* be the third. If g(p) is outside M it is covered by a point event, while if g(p) is in M then g^(-1)(M) is one of the three lines through p. Thus the only uncovered elements are exactly E(L*,M).

If b=3 then a=3, and the three line events form a star. They cannot have one common source L and three distinct targets M_i: if p∉L, the three targets would all have to equal Q; if p∈L, Q would have to avoid all three M_i, but three distinct lines cover at least six points. Thus they have one common target M and three distinct sources L_i. If the L_i had mixed incidence with p then Q would need to lie both in M and outside M, impossible. If all three contain p, they are the three lines through p and Q is three of the four points outside M; the complement is the point event for the remaining target outside M. If all three avoid p, Q=M and the L_i are three of the four lines avoiding p; the complement is E(L*,M) for the fourth. This proves the lemma.

## 4. The eight-coset conclusion

Every proper subgroup has index at least 7: by simplicity a coset action of degree m<7 would faithfully embed G in S_m, but 7 divides |G| and not m!. Two cosets of coprime-index subgroups always intersect, by the standard subgroup-intersection index calculation. Suppose eight cosets were pairwise disjoint and every pair of indices had gcd at most 7; all their pairwise gcds would lie in 2,…,7. Let b be the number of indices equal to 7.

If b=0, the indices are distinct divisors of 168 at least 8. They lie in three classes `[8,21,168]`, `[12,24,84]`, `[14,28,42,56]`, each having pairwise gcd either 1 or greater than 7. Hence at most three indices occur. If 1≤b≤5, all remaining indices are 7a with a>1 and pairwise-coprime a dividing 24; at most two such a occur, as 24 has only primes 2 and 3. If b=7 the cosets cover G, and b>7 is impossible by counting.

If b=6, the lemma makes the complement of those six cosets a single left coset F of a subgroup K of index 7. Both remaining cosets lie in F. Translating F to K identifies them with cosets of two subgroups of K whose relative indices are a,a', where their ambient indices are 7a,7a'. Since their gcd is at most 7 it is exactly 7, so gcd(a,a')=1; their relative cosets must intersect. This contradiction completes the proof.

## 5. Verification and scope

A disjoint reviewer should reconstruct the elementary conjugacy classes and normal-subgroup argument; prove completeness of point/line stabilizers; attack all Fano incidence and six-coset case splits; and verify the coset orientation/inversion and divisor coloring. The earlier author computation is corroborative only, not independent verification or a premise. The result is written and unreviewed, not Lean-checked, independently cross-model/human-reviewed, adopted, priority-cleared or global.
