# Sun8 when a small prime is missing: a written support bound

**Status: WRITTEN, UNREVIEWED.** Let G be a finite group with no proper subgroup of index below 8. Suppose that 2 or 3 does not divide |G|, and let k be the number of distinct prime divisors of |G| greater than 7. Any family of at least two pairwise disjoint left cosets whose subgroup-index gcds are all at most 7 has size at most k+3. Therefore **k≤4 implies Sun8(G)**. This is an actual-group statement with no Sun7/R8, Jordan/Jones, maximal-subgroup classification, CFSG or finite-enumeration input. It does not claim unrestricted Sun8, infinity, novelty, independent review or adoption.

For a finite nonabelian simple S with 1≤k≤4, the minimum-index condition is automatic: any proper coset action is faithful, so |S| divides m! for every proper subgroup index m; a prime divisor above 7 forces m≥11. Thus any such S with 2 or 3 absent from its order satisfies the source-free written Sun8 candidate. The case k=0 or groups with a subgroup index below 8 is not covered by this simple corollary unless the minimum-index hypothesis is separately checked.

Read prior additive overlays before earlier affected candidates in their specified order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The prior false A7 seven-index claim is not used. This is a nonblind successor of the general k+5 support argument `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`, although the complete simpler argument is given below. Earlier source, review, STOP and incidental-exposure records are not modified.

## 1. Small supports

In a family of at least two pairwise disjoint cosets all subgroups are proper, so all indices are at least 8 and divide |G|. Two cosets of coprime-index subgroups must intersect, by the subgroup-intersection index bound. Thus if every pairwise gcd is at most 7, each pairwise gcd lies in 2,…,7.

Put X={2,3,5,7}∩{prime divisors of |G|}. Since 2 or 3 is absent, |X|≤3 and the product of any two distinct primes in X exceeds 7. Let T_i⊆X be the primes in X dividing index m_i. The T_i are nonempty and pairwise intersect, because a common prime greater than 7 would make the gcd too large. Their pairwise intersections have exactly one element. A prime greater than 7 divides at most one index.

## 2. Common prime

If some p∈X divides every index, use the following one-use resources: each other prime in X, every prime divisor of |G| above 7, and the least power p^e greater than 7. Two indices sharing a different small prime also share p, so their gcd is at least the product of two distinct primes of X and exceeds 7. The large primes and p^e are themselves greater than 7 and cannot be shared. If an index uses no resource it is a power of p at most 7, contradicting its lower bound 8. Thus every index consumes one of at most (|X|−1)+k+1≤k+3 distinct resources.

## 3. No common prime

If no small prime is common, no T_i can be a singleton: every other support must intersect it. No type of size at least 2 can occur twice, since the product of any two primes in it exceeds 7. If |X|≤2 there are at most one possible type, which cannot have empty common intersection. If |X|=3, the only possible distinct types of size at least 2 are its three pairs and X itself. The full X type cannot coexist with another such type, because their intersection would contain two primes; otherwise at most the three pairs occur. Consequently this case has at most three indices, which is at most k+3.

The numerical bound is sharp for the integer-divisor relaxation: for distinct p_1,…,p_k>7, the k+3 values 8,10,14,2p_1,…,2p_k all divide 8·5·7·p_1···p_k and have pairwise gcd 2. This is not an actual coset construction.

## 4. Example and review limits

The published Suzuki order formula in Héthelyi–Horváth–Petényi, [arXiv:1404.1523v1](https://arxiv.org/html/1404.1523v1), §2, gives |Sz(q)|=q²(q²+1)(q−1), and the standard Suzuki theorem says Sz(q) is simple for q=2^(2m+1)≥8. These are **additional named, unreplayed inputs for this example only**, not for the group-theoretic criterion. At q=512 the order is 35,115,786,567,680 = 2^18·5·7·13·37·73·109. Its four prime divisors above 7 are 13,37,73,109 and 3 does not divide the order, so the simple-group corollary applies. The factorization was checked by exact integer arithmetic in the author's eval kernel. This is not a novelty claim about this group: earlier Suzuki-family candidates had different Sun5/maximal-subgroup imports.

A disjoint reviewer should attack the resource injection, the no-common-support case, the simple-group minimum-index deduction, the Suzuki factorization and example-source scope, and the sharpness wording. This is a written candidate, not a human/cross-family review, formal proof, all-simple/global theorem or historic-hold change.
