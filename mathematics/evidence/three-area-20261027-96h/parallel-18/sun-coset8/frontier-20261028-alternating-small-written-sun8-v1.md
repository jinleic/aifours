# Written Sun8 bridge for alternating degrees 5 through 13

**Status: WRITTEN, UNREVIEWED.** Conditional only on the independently unreviewed written support lemma named below, A_n satisfies Sun8 for every 5≤n≤13. The proof uses elementary alternating-group, Sylow and coset facts plus two small divisor tables displayed here; it does not use Sun7/R8, Jordan/Jones, CFSG, or the earlier 3116-vertex coloring certificate. It retains the genuine A7 seven-index example and makes no all-simple-group, arbitrary-group, formal-verification, novelty or adoption claim.

## 1. Inputs and written star lemma

First read the complete overlays in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The earlier no-seven-index claim is false. The named unreviewed input is the arithmetic lemma proved in `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`: if indices are at least 8, all divide a finite group order with k distinct prime divisors greater than 7, and every pair of indices has gcd between 2 and 7, then there are at most k+5 indices. Its proof is written in that source and does not require the earlier machine certificate. The author's nonblind certificate exposure is disclosed; no old hold is reopened.

Coprime-index cosets intersect, by the subgroup-intersection index bound and product formula. Hence a proposed Sun8 counterconfiguration has pairwise index gcds in 2,…,7. A_n is simple for n≥5, and every proper subgroup has index at least n: its coset action is faithful, but n!/2>(n−1)!.

**Star lemma.** In A_n, n≥5, any three or more pairwise disjoint index-n cosets are contained in a single partition of the group into n left cosets of one index-n subgroup, or into n right cosets of one index-n subgroup. Proof: choose one index-n subgroup H. Its faithful degree-n action has image A_n. Any other index-n subgroup K is either transitive, in which case HK=A_n and its cosets all meet the H-cosets, or intransitive. In the latter case an orbit of size u≤n/2 gives binomial(n,u)|n; for u≥2 that binomial exceeds n, so K fixes a point and is the corresponding point stabilizer. All the disjoint index-n cosets are therefore point-mapping events p↦q in one natural A_n action. Two such events with distinct sources and distinct targets intersect because a compatible two-point map has an even extension; thus any three pairwise disjoint events have a common source or common target, giving the stated left- or right-coset partition. Inverting all sets converts a right-coset partition into a left-coset partition and each other left coset into a left coset of a conjugate subgroup, with indices unchanged.

If two residual cosets lie in one index-n left-coset fiber and their ambient indices are n a and n b with gcd(na,nb)≤7 for n=6 or 7, then gcd(a,b)=1 and translating the fiber into its subgroup makes the residual cosets intersect.

## 2. A5

Every subgroup index divides 60 and is at least 5. These divisors form four graph-color classes, where any two values in one class have gcd 1 or greater than 7:

\[{5,6},\quad {12,60},\quad {15,30},\quad {10,20}.\]

Only 5 and 6 can repeat under a gcd≤7 hypothesis, and they cannot both occur in disjoint cosets since gcd(5,6)=1. If neither repeats, at most four indices occur. If one value appears r≤4 times, every other distinct index must lie in one of the other three classes, so there are at most seven cosets. Five index-5 cosets or six index-6 cosets already cover the group. If five index-6 cosets coexist with three others, the other indices must be distinct members of {10,12,15,20,30,60}; the only triples with all pairwise gcds in 2,…,7 are {10,12,15} and {12,15,20}. Their reciprocal sums are 1/4 and 1/5, each larger than the remaining density 1/6. Thus A5 has Sun8.

## 3. A6

The divisors of 360 at least 6 form five such classes:

\[{6},\quad {12,24,36,60,72,120,180,360},\quad {9,18,45,90},\quad {8,15},\quad {10,20,30,40}.\]

Each pair in the second, third or fifth class shares 12,9 or 10; the pair {8,15} is coprime. Only index 6 can repeat. With r=0 occurrences there are at most five labels; with 1≤r≤3, every other index occupies one of the four classes not containing 6, so there are at most r+4≤7.

If r=4, the star lemma makes the four index-6 cosets four cells of a common six-cell partition. Invert if needed so they are events g(p)=q with common source p. Any other coset lies in the two remaining cells, so the orbit of p under its subgroup has size 1 or 2. If the orbit has size 1, the coset lies in one cell; at most one residual coset can lie in each cell by the coprime-relative-index fact above. If the orbit has size 2, its subgroup stabilizes a two-set and its index is divisible by binomial(6,2)=15; at most one such residual coset can occur since two would have gcd at least 15. Hence there are at most three residual cosets. If r=5 the single remaining cell holds at most one residual coset; r=6 fills the group and r>6 is impossible. Thus A6 has Sun8.

## 4. A7

The only subgroup index below 8 is 7. If no index 7 occurs, the named support lemma applies to the actual indices with k=0, giving at most five cosets. If an index 7 occurs, every other index is divisible by 7. Write all indices as 7a_i with pairwise-coprime a_i dividing 360=2³·3²·5.

At most two a_i can exceed 1. Otherwise three disjoint nonempty prime supports from {2,3,5} would force one a_i to be a power of 2, hence 2,4 or 8. A7 has no subgroup of index 14,28 or 56: such a subgroup has order 360/a_i and is intransitive on seven points; an orbit of size u≤3 gives binomial(7,u)|7a_i, forcing u=1. It lies in A6 with relative index 2,4 or 8. Index 2 or 4 is impossible by simplicity and the faithful coset-action order bound. An index-8 subgroup of A6 would have order 45 and a unique Sylow-5 subgroup, since its Sylow count divides 9 and is 1 mod 5. It would normalize a C5, but the C5 normalizer in S6 has order 20 and contains an odd element, so the normalizer in A6 has order 10, contradiction.

If r≤5 indices equal 7, there are at most r+2≤7 cosets. If r=6, the star lemma makes their complement one index-7 coset, and two residual cosets in that fiber have coprime relative indices and must meet. Seven index-7 cosets fill the group and more are impossible. Thus A7 has Sun8 despite its genuine seven-index-7 subgroup configurations.

## 5. Degrees 8 through 13 and review

For 8≤n≤13, all proper subgroup indices are at least n≥8 and |A_n| has at most two prime divisors greater than 7, namely 11 and 13. The written support lemma therefore gives Sun8. Together with §§2–4 this proves the stated small-degree candidate without the earlier large finite certificate.

A disjoint reviewer should reconstruct the support lemma independently, the two hand-checkable divisor tables, A5's two triples, the star lemma including right/left orientation, A6's two-fiber orbit split, and the A7 index-8/Sylow argument. A separate self-contained Nagura/Jordan candidate for n≥14 remains under its own review; adjoining it would be conditional and not an adoption. No old process finding, source proof or historical priority is changed.
