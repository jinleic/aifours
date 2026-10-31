# A written small-prime-support Sun8 criterion

**Status: WRITTEN, UNREVIEWED.** Let G be a finite group with no proper subgroup of index less than 8, and let k be the number of distinct primes greater than 7 dividing |G|. Any family of at least two pairwise disjoint left cosets in G whose subgroup-index gcds are all at most 7 has size at most k+5. Consequently **k≤2 implies Sun8(G)**. This is an actual-group result, independent of Sun7/R8, Jordan, Jones, CFSG and the earlier finite coloring certificate. It does not claim Sun8 for arbitrary groups, an infinite-family result, novelty, external verification or adoption.

In particular, A_n for 8≤n≤13 satisfies the criterion: a proper subgroup has index at least n by the faithful coset action of the simple group A_n, and among the prime divisors of n!/2 at most 11 and 13 exceed 7. More generally, if S is finite nonabelian simple, |S| does not divide 2520 and at most two prime divisors of |S| exceed 7, then S satisfies the criterion and hence Sun8. Indeed, a subgroup index m<8 would give a faithful coset action S→S_m with image in A_m (the sign homomorphism is trivial), so |S| would divide m!/2 and thus 2520. These are conditional only on the written proof below, not on a classification source. No infinitude is claimed.

Before any affected prior candidate or successor, read in order `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The false seven-index exclusion and its table are not used. The author's prior exact finite coloring `frontier-20261028-small-alternating-sun8-colors-v1.json` SHA `e43fedc2b3662b72313e8c5294bc9befa2a9529bb0e5b938fa2a6fec674ad3cc` motivated this nonblind written argument but is not a proof input. Incidental cross-topic display remains separately disclosed and unused.

## 1. Reduction to prime supports

A coset of the whole group intersects every other coset, so a family of at least two disjoint cosets uses proper subgroups. Their indices m_i are divisors of |G| and are all at least 8. Coprime-index cosets necessarily intersect: the index of the intersection of the two subgroups is divisible by both coprime indices and at most their product, forcing their product to be the whole group. Under the contrary gcd hypothesis, therefore, every pair has gcd in {2,3,4,5,6,7}.

Put X={2,3,5,7}, and let T_i⊆X consist of the primes in X dividing m_i. Every T_i is nonempty, and every two T_i intersect: otherwise their common prime divisors are all greater than 7, which cannot yield a gcd between 2 and 7. Moreover, for distinct labels the product of the primes in T_i∩T_j is at most 7. Consequently a two-prime intersection can only be {2,3}; a three-prime intersection is impossible.

Every prime greater than 7 can divide at most one index in the family. More generally, in the cases below a named resource can occur in at most one index whenever sharing it would make a pair's gcd exceed 7. Assign each index with at least one resource to any one of its resources; this injection bounds the number of such indices by the number of resources.

## 2. If a small prime is common to every index

Suppose all indices are divisible by p∈X. Let “large primes” mean the k prime divisors of |G| exceeding 7.

- **p=2:** use resources 8,9,5,7 and all large primes. Each appears in at most one index: sharing 5 or 7 also shares 2, while 8,9 and the large primes are themselves greater than 7. An index with none is in {2,4,6,12}; only 12 is at least 8 and it can occur at most once. Total at most k+5.
- **p=3:** use resources 4,9,5,7 and the large primes. Two indices sharing 4 also share 3, so their gcd is at least 12. With no resource an index is 3 or 6, both below 8. Total at most k+4.
- **p=5:** use resources 2,3,7,25 and the large primes. Any shared resource gives gcd greater than 7; without one the index is 5. Total at most k+4.
- **p=7:** use resources 2,3,5,49 and the large primes. Any shared resource gives gcd greater than 7; without one the index is 7. Total at most k+4. No bound on the 7-adic valuation of |G| is assumed.

## 3. If no small prime is common

Now ⋂T_i is empty. No T_i can be a singleton {p}: every other T_j would then contain p. Consider the **distinct types** among the T_i, all subsets of X of size at least 2, pairwise intersecting with only {2,3} allowed as a two-prime intersection. We claim there are at most four distinct types.

A four-element type X cannot occur: any other compatible type of size at least 2 must be {2,3}, giving a common intersection. If no type has size 3 or 4, the types are pairwise-intersecting edges of the four-vertex complete graph. Such edges are a star or a triangle, and there are at most three.

Suppose a type T has size 3, with missing element d. If T does not contain both 2 and 3, any other compatible type meets T in exactly one element x and, having size at least 2, must equal {x,d}; there are at most three, so at most four types including T.

Otherwise write T={2,3,c} with {c,d}={5,7}. Any other compatible type is one of

\[\{2,d\},\ \{3,d\},\ \{c,d\},\ \{2,3\},\ \{2,3,d\}.\]

If {2,3} occurs, {c,d} is disjoint from it; and {2,3,d} cannot coexist with either {2,d} or {3,d}, because their intersections have products 2d or 3d greater than 7. Thus there are at most four types. If {2,3} does not occur, then either {2,3,d} occurs and excludes {2,d} and {3,d}, leaving at most three types, or it does not occur and at most the three displayed pairs accompany T. This proves the four-type claim.

Only type {2,3} can be repeated by different labels: the product of the primes in any other type of size at least 2 is at least 10. An index of type {2,3} has no factor 5 or 7. Since it is at least 8, it must use at least one resource from 4,9 and the k large primes; otherwise it equals 6. Two such indices sharing 4 also share 3 and have gcd at least 12; two sharing 9 or a large prime have gcd greater than 7. Thus at most k+2 labels have type {2,3}. There are at most three other types and at most one label of each, so the whole family has at most k+5 labels. If {2,3} does not occur, the four-type bound alone is stronger.

## 4. Exact scope and review

Sections 2–3 prove the asserted bound. For k≤2, eight pairwise disjoint cosets cannot have all pairwise gcds ≤7, proving Sun8. The 8≤n≤13 alternating-family consequence and the order-not-dividing-2520 simple-family consequence stated above use only the standard simplicity of A_n, coset actions and Lagrange's theorem. An author-only finite check of the 11 possible support types corroborated the four-type lemma; the proof does not depend on that check, the earlier coloring generator or its replay.

The numerical bound k+5 is sharp for the **integer-divisor relaxation**: choose distinct primes p_1,…,p_k>7 and the k+5 integers 8,12,18,20,28,6p_1,…,6p_k. All divide 2520·p_1···p_k, are at least 8, and have pairwise gcds between 2 and 7. This does not construct subgroups, disjoint cosets or a Sun counterexample.

A disjoint reviewer should attack the common-prime resource counts, especially the allowable index 12 for p=2, all repeated-{2,3} cases, the triple-type enumeration, and the simple-group sign/embedding corollary. This is not a proof of Sun8 when k≥3 or when a subgroup index below 8 exists, and it does not adopt any other packet, historical review, formal proof or novelty claim.
