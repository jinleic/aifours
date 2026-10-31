# Sun8 with at most two small prime divisors

**Status: WRITTEN, UNREVIEWED.** Let G be a finite group with no proper subgroup of index below 13. Suppose at most two of 2,3,5,7 divide |G|, and let k be the number of distinct prime divisors of |G| greater than 7. Any family of at least two pairwise disjoint left cosets with all pairwise subgroup-index gcds at most 7 has size at most k+2. In particular **k≤5 implies Sun8(G)**. This is a written actual-group criterion, not an integer relaxation, and uses no Sun7/R8, Jones, CFSG, maximal-subgroup classification or computational enumeration. It does not claim all-group Sun8, infinity, novelty, review or adoption.

For a finite nonabelian simple group S with 2≤k≤5, the minimum-index hypothesis is automatic: its largest prime divisor r>7 is at least 13, and every proper coset action is faithful, so r divides the factorial of each index and that index is at least r. Thus any such S with at most two prime divisors in {2,3,5,7} satisfies the written Sun8 candidate. No additional claim is made for k=0 or 1 without checking the minimum-index condition.

Before earlier affected bodies, read the complete pre-source overlays in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. No prior source, hold or review is changed. This is a nonblind prospective successor of the support arguments in `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`; the complete proof is written below. The separate incidental cross-topic display remains disclosed and unused.

## 1. Common small prime

Suppose a family of at least two pairwise disjoint left cosets has all index gcds at most 7. Every subgroup is proper, so each index is at least 13 and divides |G|. Two cosets with coprime subgroup indices always meet, by the subgroup-intersection index bound and product formula. Hence every pairwise gcd lies in 2,…,7.

Let Y be the set of prime divisors of |G| among {2,3,5,7}; by hypothesis |Y|≤2. Let T_i be the subset of Y dividing the ith index. Each T_i is nonempty and the T_i are pairwise intersecting, because a common prime above 7 is impossible. A pairwise-intersecting family of nonempty subsets of a set of at most two elements has a common element: if any T_i is a singleton {p}, every other T_j contains p; otherwise they all equal Y. Fix such a common p.

Every prime above 7 is a **one-use resource**: it divides at most one index. The remaining resources are as follows.

- If Y={2,3} and p=2, use 8 and 9. Two indices sharing either have gcd greater than 7. An index using neither and no large prime belongs to {2,4,6,12}, all below 13.
- If Y={2,3} and p=3, use 4 and 9. Two indices sharing 4 also share 3 and have gcd at least 12; two sharing 9 have gcd at least 9. An index using neither and no large prime is 3 or 6.
- In every other case, use the least p-power strictly exceeding 7 and, when present, the other prime in Y. Two indices sharing either resource have gcd greater than 7, because any distinct-prime product from Y is then at least 10. An index using neither resource and no large prime is a p-power at most 7.

Every index consumes at least one resource, and each resource occurs at most once. There are at most k+2, proving the stated bound.

## 2. Sharp arithmetic and a concrete simple example

For any distinct primes p_1,…,p_k>7, the k+2 integers 16,18,6p_1,…,6p_k are at least 13, divide 2^4·3²·p_1···p_k and have all pairwise gcds equal to 2 or 6. Thus k+2 is sharp for the **integer-divisor relaxation**. This does not construct disjoint cosets or an actual counterexample.

For illustration, the classical PSL2 simplicity and order statements give a finite simple group PSL2(2243) of order (the simplicity statement is also stated in these [Stanford group-theory notes](https://sporadic.stanford.edu/bump/group/gr1_10.html)):

\[\frac{2243(2243^2-1)}2=5{,}642{,}320{,}332=2^2\cdot3\cdot11\cdot17\cdot19\cdot59\cdot2243.\]

The author checked exactly that 2243 is prime and checked the factorization in the eval kernel. This group has only small prime divisors 2,3 and exactly five primes above 7, so the simple corollary applies. The standard simplicity/order statements are named, unreplayed inputs for this example only, not for the general criterion; no priority or novelty claim is made.

## 3. Review boundary

A disjoint reviewer should independently verify the no-common-prime reduction on a two-element universe, both exceptional resource pairs for Y={2,3}, the minimum-index bound and the exact example factorization/primality. This packet leaves k≥6, groups of small subgroup index, and all-group/all-simple Sun8 open; no formal/human/independent-family acceptance or historic-hold rehabilitation follows.
