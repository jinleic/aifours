# Seven pairwise-gcd-7 subgroup indices in alternating groups: the A7 exception

**Status: WRITTEN, CONDITIONAL and UNREVIEWED.** Subject to the named public-source inputs and the independently unreviewed n≥14 argument of `frontier-20261028-alternating-all-degrees-p7-v1.md` SHA `6c22ef729ab54ba297b282e5923a749c186aab9c407ec9fc1f975d0e3af2227a`, there exist seven proper subgroups of A_n, n≥5, whose pairwise index gcds are exactly 7 **if and only if n=7**. The n=7 direction holds even with seven distinct subgroups and seven disjoint left cosets. This corrects—not preserves—the false all-n seven-index exclusion; it does not by itself decide a separately defined P7 condition containing further assumptions or yield an eight-coset counterexample. No acceptance, formal review, novelty, all-simple-groups conclusion, or historical-hold change is claimed.

**Mandatory source order:** read completely `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, then `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, then `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`, before the earlier source body or this successor. Only Sections 2–5 of the earlier all-degree candidate are imported, and only at n≥14; the erroneous small-degree table and every conclusion based on it are withdrawn. Its named imports are Bertrand, Jordan/Jones Theorems 1.1 and 1.2(k=2), and Theorem 2(i)(b) of arXiv:2307.13976v2, with the scope and source-proof limitations in that candidate. They are not independently verified here. The author has disclosed nonblind incidental cross-topic display separately; no such excerpt is used.

## Degrees 5,…,13

The order of A_n is n!/2. A proper subgroup index divides this order and, because A_n is simple, is at least n: the coset action has trivial core and embeds A_n in S_m, impossible for m<n since m!≤(n−1)!<n!/2. If 5≤n≤6, the group order is not divisible by 7, so no index is divisible by 7 and the desired seven-index pattern is impossible.

For 8≤n≤13, suppose indices m_i have pairwise gcd 7. Then each m_i=7a_i with a_i a positive integer, and the a_i are pairwise coprime. Since m_i≥n≥8, **each a_i>1**; this is the missing reason that units cannot repeat. Also 7 divides n!/2 exactly once in this range, so none of the a_i is divisible by 7. Every a_i therefore has at least one prime divisor from the set below, and pairwise coprimality makes these chosen primes distinct:

| Degrees | Available non-7 primes | Maximum number of indices in such a pattern |
|---|---|---:|
| 8,9,10 | 2,3,5 | 3 |
| 11,12 | 2,3,5,11 | 4 |
| 13 | 2,3,5,11,13 | 5 |

These bounds exclude seven indices. They are only arithmetic upper bounds, not claims that each maximum is achieved by subgroups. For n=7 the premise a_i>1 fails and the previous source's rule 'at most one a_i=1' is false.

Let H_i≤A7 be the stabilizer of i for i=1,…,7. These seven proper subgroups are distinct, each has index 7, and every pairwise index gcd is 7. For each i choose an even permutation g_i with g_i(i)=1. The left coset g_iH_i is exactly the set of even permutations g with g(i)=1. As g is a bijection, precisely one i maps to 1; the seven left cosets are disjoint and partition A7. This is a written elementary construction requiring independent verification; it is not an eight-coset configuration.

## Degrees n≥14

At the exact conditional scope of the cited candidate's Sections 2–5, no four proper-subgroup indices have pairwise gcd at most 7. In particular there cannot be seven whose pairwise gcds are exactly 7. Combining this with the previous section gives the stated if-and-only-if, pending a full review of both the n≥14 source-dependent proof and the elementary small-degree argument. The separate small-degree Sun8 certificate `frontier-20261028-alternating-small-degrees-sun8-v1.md` SHA `2c91150895a502722274c29cc3a082f992f9f16d38f51c5e2277c37d9717756f` asks a different question about eight **disjoint** cosets and remains independently unreviewed.
