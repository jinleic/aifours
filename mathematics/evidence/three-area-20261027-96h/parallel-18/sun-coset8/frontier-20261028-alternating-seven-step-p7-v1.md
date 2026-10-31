# Seven-step alternating P7 exclusion via four-of-five type collisions

**Status: WRITTEN candidate, conditional on the public A_r source theorem and earlier written base/orbit argument; not independently reviewed or accepted.** Let r≥419 be an eligible prime, meaning r is not (q^d−1)/(q−1) for a prime power q and d≥2. Put
\[d_7=\frac{r+7}{\gcd(r+7,420)}.\]
If d7>7, then the actual simple group A_(r+7) has no seven proper subgroups whose indices all have pairwise gcd exactly 7. The condition is automatic for r≥2934, since r+7>7·420. The earlier elementary count gives infinitely many eligible primes; therefore this is an unbounded written family conditional on the cited classification, not a finite enumeration. No publication-priority or novelty claim is made.

The result includes r=419,421,431, yielding A426, A428, A438. The case r=431 illustrates an actual improvement over the previously frozen coarse-bucket integer obstruction; no subgroup counterexample was ever claimed there.

## 1. Dependencies and typed descent

The public group-classification input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: a Sylow-r subgroup of A_r has unique maximal overgroup AGL1(r)∩A_r for eligible r≥419. The base index divisibility in A_(r+1) and the d1,…,d6 orbit induction were written in `frontier-20261028-alternating-orbit-induction-v1.md`, SHA `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5`; the typed branches and their 1–2–3 collision were written in `frontier-20261028-alternating-six-step-typed-p7-v1.md`, SHA `b58cde595c44155c158d0d2226b721ace070322233774611d79b7c4772c57aa4`. All are unreviewed inputs here, not source-proof replay or formal acceptance. No Sun7 is used.

For j=1,…,7 set d_j=(r+j)/gcd(r+j,lcm(1,…,j)). The previous proof gives d_j>7 for j≤6, and d7>7 is assumed. Its actual orbit/stabilizer descent applies verbatim one additional step: each proper subgroup index in A_(r+7) not divisible by r can be assigned one **type** j∈{1,…,7}. A type-1 index is divisible by r+1. For type j≥2 there is a specific u∈{1,…,j} such that the index is divisible by the full binomial C(r+j,u); in either case it is divisible by d_j. The index is unchanged at each transitive point-stabilizer descent, and the full binomial appears at the first intransitive orbit. Different choices are allowed; choose any valid chain for each index.

The writer's source exposure was nonblind. The incidental cross-topic display is recorded at `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is used here. No clean-cognition or historical-hold rehabilitation claim follows.

## 2. Arithmetic used in collisions

Write n_j=r+j. Since r is odd, n1,n3,n5 are even and n2,n4 are odd. As r≠3, n3 is not divisible by 3 and d3=n3/2>7. In any direct P7 pattern every index is divisible by 7, so two even indices have gcd≥14. Any other common divisor >7 is also forbidden.

For any factor a appearing in the numerator of C(n,u), the integer a/gcd(a,u!) divides C(n,u): u!·C(n,u) is the product of the u consecutive numerator factors. For the only large factors used below, n2/gcd(n2,24)≥n2/24>7, and n2/gcd(n2,6)>7.

The relevant consequences are:

- Type 1 is even. Each type-2 alternative C(n2,1) or C(n2,2) is divisible by n2 because n2 is odd.
- Type 3 at u=2 is divisible by n2 and d3, since C(n3,2)=d3·n2. Its u=1 and u=3 alternatives are even and divisible by d3: n3|C(n3,3) because 3∤n3. Thus types 1,2,3 cannot all occur in a P7 pattern.
- Type 4 at u=1 or 2 is divisible by n4, since C(n4,2)=n4·d3. Its u=2 or 3 alternative is divisible by d3; its u=3 or 4 alternative is divisible by a divisor >7 of n2.
- For type 5, odd u gives an even binomial: n5/gcd(n5,u) is even and divides C(n5,u). At u=2 the binomial is divisible by n4; at u=4 it is divisible by n2/gcd(n2,24)>7.

All these are exact integer implications, not statements that arbitrary numbers satisfying them are subgroup indices.

## 3. Four types among 1,…,5 are impossible

If four occupied types include 1,2,3, Section 2 already gives a contradiction. Otherwise they include 4 and 5 plus two of 1,2,3. Three cases cover every possibility:

1. **Types 1,2,4,5.** Type-4 u=3 or 4 collides with type 2 through a divisor >7 of n2. Hence type 4 has u=1 or 2 and its index is divisible by n4. For type 5, odd u is even and collides with type 1 via 14; u=2 collides with n4; u=4 collides with type 2 via n2/gcd(n2,24)>7. No alternative remains.
2. **Types 1,3,4,5.** Type-3 u=1 or 3 is even and collides with type 1 via 14, so u=2; its index is divisible by n2. The preceding case applies with this type-3 index replacing type 2: type 4 must supply n4, and every type-5 alternative collides.
3. **Types 2,3,4,5.** Type-3 u=2 collides with type 2 through n2, so u=1 or 3. Its index is even and divisible by d3. Type-4 u=2 or 3 collides through d3, and u=4 collides with type 2 through n2/gcd(n2,24)>7. Hence type 4 is u=1 and supplies n4. Every odd-u type-5 alternative is even and collides with type 3 via 14; u=2 collides with n4; u=4 collides with type 2 through n2/gcd(n2,24)>7.

Thus at most three of the first five types can occur in any direct P7 pattern, regardless of the choice of valid descent chains.

## 4. Seven actual indices

Assume seven proper subgroup indices in A_(r+7) have every pairwise gcd equal to 7. At most one is divisible by r>7, so at least six are r-free. Choose one valid type for each. Two cannot share a type j, since both indices would be divisible by d_j>7. Among six distinct choices from seven types, at least four must lie in {1,…,5}, because only types 6 and 7 lie outside. This contradicts Section 3. Hence direct P7 is excluded.

## 5. Exact controls and review boundary

`frontier-20261028-alternating-five-type-check.py`, SHA-256 `2508dfd5a74034e682a29c0f848c8b54cfb0ca83e27fc7a1130944929e490be0`, 20 LF / 801 bytes, ran at 18:47:14 PDT on 2026-10-28. It checked all 274 choices of a four-type subset of the first five and their possible binomials, after multiplication by 7, for each r=419,421,431, and checked d7>7. These finite checks neither establish the general collision proof nor enumerate any actual subgroup.

**Review-critical:** reconstruct the d7 one-step extension of the actual orbit induction; verify every factorial-divisibility and parity implication, especially the three missing-type cases; confirm d7>7 and the source/prime-density dependencies. No unrestricted all-alternating or all-simple-group conclusion, historical novelty, or modification of old holds is claimed.
