# Sun8 for odd-prime-power-dimensional unitary groups over nonprime fields

**NEW FAMILY CANDIDATE at NAMED INPUTS — WRITTEN plus bounded exact checks; not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:59:56 PDT 2026**. This is a full actual-eight-coset theorem for the stated infinite finite-simple families, with extra explicitly limited prime-field cases. It does not claim unrestricted Sun8 or completeness for all unitary dimensions/fields.

## 1. Exact statement

Let `Sun_8(X)` mean: every eight pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X have a pair of subgroup indices with gcd at least8.

**Theorem.** Let `n=t^a>=5`, where t is an ODD prime and a>=1, and let `q=p^f`, where p is a prime. Assume the named finite-unitary order/simplicity, unique-Sylow-overgroup and primitive-prime statements in Section2. Then `Sun_8(PSU_n(q))` holds in each of the following EXACT cases:

1. **Every nonprime field:** f>=2, with arbitrary p and every stated n.
2. **Prime fields with composite 2n+1:** f=1 and 2n+1 is composite, with arbitrary p.
3. **Other prime fields under an explicit arithmetic condition:** f=1 and SOME primitive prime r of `p^(2n)−1` satisfies either `r>2n+1` or `r² | (p^n+1)`.
4. **The separate small endpoint:** `(n,q)=(5,2)`, using the written order-support argument in Section7, not the general maximal-overgroup table or a Magma-only claim.

The cases may overlap. The theorem does NOT claim all prime-field cases when 2n+1 is prime and the condition in3 fails. `PSU_3(q)` for all q>=3 was handled separately by `frontier-20261028-psu3-all-fields-v1.md`, SHA256 `c32a27c4e2c71cf76e3b129d37513dba9680da34cf4186a35d1d70126b7b8e7b`, with its own dependencies and pending review. No result for even unitary dimensions or arbitrary finite simple groups is claimed.

## 2. Named source statements and their limits

- [Baumeister–Burness–Guralnick–Tong-Viet, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2), Theorem2 and Table B, U_n(q), r=r_(2n), states: for `n=t^a` with t>=3 prime, if `beta(n,−1)` holds and either `|R|>r`, or `r>2n+1`, or the stated quadratic-residue alternative holds, a Sylow r-subgroup R has a UNIQUE maximal overgroup of type `GU_(n/t)(q^t)`. The source Proposition6.4 separately handles small groups `U4(2),U4(3),U5(2),U6(2)`; we DO NOT silently apply the generic row to `(5,2)`, which Section7 treats independently. For the present claims we use only the first two displayed alternatives, NOT the quadratic-residue condition.
- The same source's Remark9.2 defines `beta(n,−1)` as

      (q^(1/k))^n != −1 (mod r)

  for every ODD prime divisor k of f with k!=r. We verify this explicitly for the selected r.
- [Projective special unitary group order and simplicity, MathWorld](https://mathworld.wolfram.com/ProjectiveSpecialUnitaryGroup.html):

      |PSU_n(q)| = q^(n(n−1)/2) product_(j=2)^n(q^j−(−1)^j) / gcd(n,q+1),

  with nonabelian simplicity except PSU2(2), PSU2(3), PSU3(2). Thus every group in the theorem's n>=5 range is simple. This is a secondary reference for the explicit standard statement, not a proof-source authentication.
- The same 2024 arXiv source §2.1 states Zsigmondy's theorem: a primitive prime divisor of `p^d−1` exists for d>=2 except `(p,d)=(2,6)` or d=2 with p a Mersenne prime. We use d=2nf>=10, so neither exception occurs.

**NR-UNIQUE-SYLOW-CLASSIFICATION / NR-UNITARY-ORDER-SIMPLICITY / NR-ZSIGMONDY-PROOF:** none of these external theorem proof DAGs has been independently rederived in this packet. The exact result is conditional on the stated inputs, not on a vague 'classification' or on a finite test. No Sun7, NC7, old P7 reduction or held unitary candidate is an input.

## 3. A general actual-coset lemma

Let G be finite, let r>7 divide |G|, and suppose a fixed Sylow r-subgroup has a UNIQUE maximal proper overgroup M of index d>=8. Then G has Sun8.

Indeed, if eight actual disjoint cosets had every index gcd<=7, at most one original index could be divisible by r. At least seven corresponding subgroups have r-free index and contain a Sylow r-subgroup of G. By Sylow conjugacy and uniqueness, every such subgroup lies in SOME conjugate of M, so its index is divisible by d. Two actual original indices would share d>=8, contradiction. The subgroups need not lie in the same conjugate; no freely specified fibre or cover is introduced. □

In fact, whenever G is nonabelian simple and r>7 divides |G|, EVERY proper subgroup has index>=8. A proper subgroup's coset-action kernel is normal and proper, hence trivial, so an index d<=7 would embed G into S_d. Its order would then divide d!, which is impossible because r>7 divides |G|. This proves the actual index bound needed for M without importing a minimum-index table.

## 4. Nonprime fields: all f>=2

Fix ALL n=t^a>=5 and all p,f>=2. Zsigmondy gives a prime r with

    ord_r(p)=2nf.

It is prime to p and satisfies `r≡1 (mod 2nf)`, hence

    r>=2nf+1 > 2n+1 >7.                                      (4.1)

Writing q=p^f, `ord_r(q)=2n`, so q^n≡−1 (mod r) and r divides q^n+1. Because n is odd, q^n+1 is one of the explicit unitary-order factors; the projective-center denominator divides n<r. Thus r divides |PSU_n(q)|.

For EVERY odd prime k|f,

    (q^(1/k))^n = p^(nf/k) != −1 (mod r).

Otherwise squaring gives `p^(2nf/k)=1 (mod r)` with smaller positive exponent, contradicting the primitive order2nf. This pays the source's entire beta(n,−1) condition, including any excluded k=r. The source row applies: n is the required odd prime power, `(n,q)` is not the separately handled `(5,2)` since f>=2, beta holds, and the explicit alternative `r>2n+1` holds by (4.1). Thus the Sylow r-subgroup has a unique maximal proper overgroup. Simplicity and the r>7 divisor give its index>=8 by Section3. The actual-coset lemma proves Sun8.

This covers ALL field characteristics, ALL f>=2 and ALL odd prime-power n>=5, not only the finite sample in Section8.

## 5. Prime fields under exact primitive-prime alternatives

For f=1, Zsigmondy supplies a primitive prime r of `p^(2n)−1`; here 2n>=10 so there is no exceptional pair. Then `ord_r(p)=2n`, `r≡1 (mod 2n)`, r>=2n+1>7, and r divides `p^n+1` and the unitary group order as in Section4. The beta condition is vacuous because f has no prime divisor.

- If 2n+1 is composite, r cannot equal it, so r>2n+1. The source row supplies the unique maximal overgroup.
- More generally, if ANY such r is >2n+1, use the same alternative.
- If r² divides p^n+1, the explicit n-th unitary-order factor shows r² divides |G|: the projective-center denominator is at most n<r. Hence the actual Sylow r-subgroup has order >r, satisfying the source's other displayed alternative.

In each case, `(n,q)=(5,2)` is not inadvertently covered by the generic classification row: `2^10−1=3*11*31`, its sole primitive prime for exponent10 is11=2n+1 and `11²` does not divide `2^5+1=33`. Section7 handles it by a separate argument. For all nonexceptional cases in this section, simplicity and r>7 imply the maximal-overgroup index>=8, so Section3 gives Sun8.

For prime-field cases outside these alternatives, we make NO assertion: a primitive r=2n+1 with Sylow order r can have an additional exceptional maximal subgroup in the source classification. We do not assume its absence, treat its index as the Singer index, or promote an arithmetic primitive-prime witness to a unique-maximal theorem.

## 6. Small-prime-support bound used once below

Suppose a finite group has no subgroup index2 through7 and its order is supported on primes {2,3,5,11}. A family of pairwise-disjoint cosets with pairwise index gcd<=7 has at most FIVE members.

Every index is >=8, and disjoint actual cosets have index gcd>=2 by the coprime-index diagonal-map lemma. At most one index can be divisible by11. For the remaining indices, whose prime supports lie inside {2,3,5}, at most four are possible:

- If pure support {2} occurs, all indices are even; there is at most one pure 2-power (both >=8 would share8), at most two supported on {2,3} (each >=8 is divisible by12 or18, and repeated divisibility would force gcd>=12 or18), and at most one divisible by2*5=10. Total<=4.
- If pure support {3} occurs, analogously at most one pure3-power, at most two supported on {2,3}, and at most one divisible by3*5=15. Total<=4.
- If pure support {5} occurs, at most one pure5-power and at most one each of even/3-divisible 5-bearing indices, since repeated pairs would share10/15. Total<=3.
- If no singleton support occurs, {2,3} contributes at most2; {2,5} and {3,5} at most1 each; and a {2,3,5} index can occur at most1 and cannot coexist with either {2,5} or {3,5} because it would share10 or15. Total<=4.

Every case uses ALL actual original indices and their pairwise noncoprimality; it does not assume all divisors occur as subgroup indices. The bound is a theorem about this explicit order support, not a general prime-count assertion.

## 7. The exceptional small group PSU5(2)

From the named unitary order formula,

    |PSU_5(2)| = 2^10 * 3^5 * 5 * 11 = 13685760.

It is nonabelian simple by the stated simplicity theorem. The prime11 divides its order, so no proper subgroup can have index2 through7 by the faithful-coset action argument in Section3. Section6 therefore gives Sun8(PSU5(2)), independently of the source Proposition6.4's separately reported Magma classification of its maximal subgroups. No Sun7 is needed.

## 8. Actual bounded checks and explicit limitations

1. `frontier-20261028-unitary-odd-dimension-check.py`, SHA256 `13844ae7e9095abb697ad49a1d1be5ea3b8838ea20232387d58063423bf7c319`, independently used exact modular exponentiation/trial primality for n=3,5,7,9, p=2,3, f=2,3. It checked each found r has primitive order2nf, exceeds2n+1, divides the stated unitary-order product and satisfies the beta modular tests. All16/16 bounded searches returned witnesses and PASS; actual native post-run clock **Wed Oct28 17:59:04 PDT2026**. Its finite cases do not prove Zsigmondy or the all-n theorem.
2. `frontier-20261028-u5q2-order-check.py`, SHA256 `3629cb9e8996f6490cead9b872e4de8e2d6d9c3a9cbdae5007629e6408b5ea29`, independently evaluated the unitary order product exactly and returned

       unitary_order: 13685760
       factor_product: 13685760
       eleven_divides_order: True
       PASS: exact PSU(5,2) order arithmetic
       Wed Oct 28 17:59:41 PDT 2026

   This checks the arithmetic, not the imported simplicity or the general support lemma.

No group enumeration or unbounded computation is claimed. No finite index pattern, numerical bound or assumed all-simple classification is substituted for an actual-coset proof.

## 9. Prior comparison and remaining original target

The old final math-6 summary separately supported all SL/PSL and symplectic families, while later unitary candidates retained their individual unreviewed/held statuses. The earlier provenance correction for rediscovered R8 and normal-section implications remains binding. This packet uses the NEWLY READ external unique-Sylow theorem plus a fresh exact arithmetic/overgroup application; it does NOT claim that prior unitary work is false, absent, or independently revalidated. Targeted parent-source searches did not identify an adopted full odd-prime-power unitary family, but the source/priority search is incomplete and novelty is NOT asserted.

Even if fully reviewed, the theorem leaves all even dimensions, odd dimensions not prime powers, and the unlisted prime-field cases open, as well as all remaining simple families and arbitrary-group Sun8. The external unique-overgroup classification, its exceptional groups, Zsigmondy and unitary order/simplicity must be reviewed at the exact named source rows before adoption. Formal/kernel, independent-family/human verification, priority and publication remain unpaid.
