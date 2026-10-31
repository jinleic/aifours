# Consolidated source-free Sun8 criteria for finite groups

**Status: WRITTEN, UNREVIEWED.** The statements below are a single consolidated candidate, with complete elementary proofs, for the strongest source-free prime-support criteria developed in this slot. They use no Sun7/R8, Jordan/Jones, CFSG, maximal-subgroup classification, or finite-enumeration certificate. They do not claim that any earlier unreviewed candidate is adopted, that arbitrary-group Sun8 is proved, that the displayed classes are infinite, or that the results are novel or formally verified.

For a finite group G, let μ(G) be the smallest index of a proper subgroup, with μ(G)=∞ if there is none. Let Y be the set of prime divisors of |G| in {2,3,5,7}, and let k be the number of distinct prime divisors of |G| greater than 7. In any family of at least two pairwise disjoint left cosets whose subgroup-index gcds are all at most 7:

1. If μ(G)≥8, the family has at most **k+5** cosets.
2. If μ(G)≥8 and 2∉Y or 3∉Y, it has at most **k+|Y|≤k+3** cosets.
3. If μ(G)≥13 and |Y|≤2, it has at most **k+2** cosets.
4. If μ(G)≥13 and |Y|≤3, it has at most **k+4** cosets; the sharper bounds 2–3 still apply where their hypotheses hold.

Consequently Sun8(G) holds whenever at least one of these exact sufficient conditions holds: **(i)** μ≥8 and k≤2; **(ii)** μ≥8, 2 or 3 absent, and k≤4; **(iii)** μ≥13, |Y|≤2 and k≤5; **(iv)** μ≥13, |Y|≤3 and k≤3. These are alternative sufficient conditions, not a classification or necessary conditions. The stronger bound in item 4 is a new written consolidation of earlier saturation reasoning and has not received a separate review.

## 1. Provenance and status boundaries

The author’s earlier, separately unreviewed source-free candidates are `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`, `frontier-20261028-small-prime-missing-sun8-v1.md` SHA `69d48e99d0f6fd092dc57aac8735beb75f0acd9c22fe8e0c42ded5d4ea334ed9`, and `frontier-20261028-two-small-primes-sun8-v1.md` SHA `7cec2a55c1f723ce8e42cf2848f9ebcf805b6093bd5c03121bce28dbaf815f25`. Their author-side type/coset controls and the earlier finite coloring motivated this nonblind consolidation; none is a proof input to the complete written argument below. The fourth bound, for at most three small primes, also subsumes the missing-small-prime k=3 consequences of `frontier-20261028-simple-three-large-primes-frontier-v1.md` SHA `1d78631af7f11cb0393af6850c760a7b6a7b43a8fc26770595066951561e4c55`, but does not assume its optional Sun3 import.

Read the earlier complete pre-source corrections in order before affected source bodies or successor consumers: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The false A7 seven-index exclusion is not used. Prior STOP/ZERO, incidental cross-topic disclosure and all historical findings remain unchanged.

## 2. Elementary reduction and one-use resources

A coset of the whole group cannot be disjoint from another nonempty coset, so all subgroup indices m_i in such a family are at least μ(G) and divide |G|. Cosets of coprime-index subgroups always intersect: their subgroup-intersection index is a multiple of the product and at most the product, so the subgroup product is G. Thus every pairwise gcd of our indices lies in 2,…,7.

Put T_i={p∈Y:p divides m_i}. Each T_i is nonempty and every two T_i intersect, since a common prime above 7 would make the gcd exceed 7. The product of the primes in T_i∩T_j is at most 7, so the only possible two-prime intersection is {2,3}; three common small primes are impossible. Every prime greater than 7 divides at most one index.

A **one-use resource** is a divisor which can occur in at most one index: if two used it, their gcd would exceed 7, possibly using a small prime known to be common. If each of N indices uses at least one of R one-use resources, assigning one resource to each index gives N≤R.

## 3. Proof of the k+5 bound when μ≥8

First suppose some p∈Y divides every index. The following small resources, together with the k primes above 7, are one-use:

- p=2: 8,9,5,7. If none occurs, m is one of 2,4,6,12; only 12 is at least 8 and it can occur at most once. Hence N≤k+5.
- p=3: 4,9,5,7. Two indices sharing 4 also share 3 and have gcd at least 12. With no resource m is 3 or 6. Hence N≤k+4.
- p=5: 2,3,7,25. With no resource m=5; two indices sharing any listed resource have gcd above 7. Hence N≤k+4.
- p=7: 2,3,5,49. With no resource m=7; again N≤k+4. No restriction on v_7(|G|) is imposed.

Now suppose no small prime divides every index. No T_i is a singleton, and the **distinct** support types have size at least 2. There are at most four distinct types. To see this, a four-element type can coexist only with {2,3}, giving a common intersection. If all types are pairs, their pairwise-intersecting edges in K4 form a star or a triangle and there are at most three. If a triple T occurs, let d be its missing element. If T does not contain both 2 and 3, every other compatible type meets T in exactly one x and is {x,d}, giving at most four total. If T={2,3,c}, {c,d}={5,7}, the only other possible types are {2,d}, {3,d}, {c,d}, {2,3}, {2,3,d}. The last is incompatible with {2,d} and {3,d}, while {2,3} is disjoint from {c,d}; checking those alternatives gives at most four total.

Only {2,3} can repeat: every other type of size at least two has prime product at least 10. Each index of type {2,3} must use 4,9 or a prime above 7, because otherwise it equals 6<8. Two such indices using 4 also share 3 and have gcd at least 12; sharing 9 or a large prime also exceeds 7. Hence at most k+2 indices have type {2,3}, and at most three others occur, proving N≤k+5. If {2,3} is absent, the four-type bound is stronger.

## 4. Proof when 2 or 3 is absent

If 2∉Y or 3∉Y, any two distinct primes in Y have product greater than 7 and |Y|≤3. If a small prime p is common, the one-use resources are the other |Y|−1 small primes, the least p-power greater than 7, and the k large primes. An index using none is a p-power at most 7, impossible since μ≥8. Hence N≤k+|Y|.

If no small prime is common, no support is a singleton and no support of size at least two can repeat. On a universe of size at most three, the full three-element support cannot coexist with any other nonsingleton support; otherwise there are at most the three two-element supports. Thus N≤3≤k+|Y| whenever this case is nonempty. This proves item 2.

## 5. The μ≥13 refinements

If |Y|≤2, pairwise-intersecting nonempty supports have a common prime p. If Y={2,3} and p=2, use one-use resources 8,9 and the k large primes: without one, m∈{2,4,6,12}<13. If Y={2,3} and p=3, use 4,9 and the large primes: without one, m∈{3,6}. In any other two-prime or one-prime Y, use the other small prime, the least p-power greater than 7, and the k large primes; a resource-free index is a p-power at most 7. Hence N≤k+2, proving item 3.

For |Y|≤3, cases missing 2 or 3 already satisfy item 2, while |Y|≤2 satisfies item 3. It remains to take Y={2,3,d}, where d is 5 or 7. If a small p is common, the one-use resources are 8,9,d for p=2; 4,9,d for p=3; or 2,3 and the least d-power above 7 for p=d, together with the k large primes. Because μ≥13 the only former base value 12 is excluded, so N≤k+3.

If no small prime is common, supports are nonsingletons. The triple {2,3,d} can coexist only with {2,3}, which would give a common intersection; hence it is absent. The only possible types are {2,3}, {2,d}, {3,d}. Nonempty common-intersection failure requires all three. The first type has at most k+2 labels, using one-use resources 4,9 and the k large primes; each of the other types appears at most once because 2d and 3d exceed 7. Therefore N≤k+4, proving item 4.

## 6. Simple-group and alternating consequences

For finite nonabelian simple S, every proper coset action is faithful. If r is the largest prime divisor of |S|, every proper subgroup index m satisfies r≤m because |S| divides m!. Thus μ(S)≥11 when k≥1 and μ(S)≥13 when k≥2. Without any small-index classification, the four criteria yield, for example:

- Sun8 for every such S with 1≤k≤2;
- Sun8 for 1≤k≤4 if 2 or 3 does not divide |S|;
- Sun8 for 2≤k≤5 if |Y|≤2;
- Sun8 for 2≤k≤3 if |Y|≤3.

Each is an unreviewed written candidate, not a statement about all simple groups or an infinitude claim. A_n for 8≤n≤13 has μ(A_n)≥n and k≤2, so is included without any large finite coloring certificate. The A5,A6,A7 cases are separately addressed in the unreviewed `frontier-20261028-alternating-small-written-sun8-v1.md` SHA `cb2c2ae804915798e5545cb4be9432677cac012df567f82b114967ba732b6647`; they are **not** included in the source-free bounds unless their hypotheses happen to hold.

For n≥14, Main has separately adopted same-harness written support for the stronger four-index gcd≥9 result, conditional on the unreplayed Nagura and Jordan theorem statements, in `institute/runs/three-area-2026-10-27-96h/dispositions/math-6-alternating-n14-nagura-jordan-parent-v1.md` SHA `f7c0c3ed5ad915e20bbf9ba13c42bb061cc075bb58ad75783b60a88aef99b3b8`. The formal Nagura strict-endpoint citation is page 180 of the pinned 1952 paper; the additive source record is `frontier-20261028-nagura-page180-citation-addendum-v1.json` SHA `d7742db1d8a57320773da7874d37fc6cf434606980dbaeffae10bf7838b11ba6`. That adoption is **source-conditional and n≥14 only**; it is not a review or acceptance of this consolidated source-free candidate or of n≤13.

## 7. Arithmetic tightness and independent review

The four numerical bounds are sharp as **integer-divisor relaxations**, not as actual coset constructions. For distinct primes p_1,…,p_k>7, examples are: `8,12,18,20,28,6p_1,…,6p_k` for k+5; `8,10,14,2p_1,…,2p_k` for k+3 with 3 absent; `16,18,6p_1,…,6p_k` for k+2 with μ≥13 and two small primes; and `24,18,20,15,6p_1,…,6p_k` for k+4 with μ≥13 and small primes {2,3,5}. In each list all values meet the stated lower bound and have pairwise gcds in 2,…,7. These examples do not show that a group with the required minimum index realizes the integers as subgroup indices, let alone as disjoint cosets.

A disjoint reviewer should reconstruct the entire type-family argument, all one-use resource counts, the μ≥13 three-small-prime refinement, and the simple-group applications without importing the author's earlier proof or checker. These are written claims only: no human/cross-model review, formal proof, priority clearance, all-simple result or global Sun8 conclusion follows.
