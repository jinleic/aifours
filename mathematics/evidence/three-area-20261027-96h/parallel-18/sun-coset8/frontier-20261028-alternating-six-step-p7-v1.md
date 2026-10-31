# Six-step alternating refinement using the actual P7 prime

**Status: WRITTEN candidate, contingent on the source theorem and the written orbit induction below; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2, and suppose r≡1,3 or 5 mod 8. Then A_(r+6) has no seven proper subgroups whose indices all have pairwise gcd **exactly 7**. Thus direct P7 is excluded in these additional alternating groups. This is a P7-specific refinement: it does **not** assert the absence of seven indices with gcd≤7 when 7 need not divide them.

The condition is nonempty: r=419 and 421 both qualify, giving A425 and A427. Subject additionally to the standard prime number theorem in the progression 1 mod 4, infinitely many eligible r satisfy the residue condition. No published-priority or historical novelty is claimed.

## 1. Named dependencies

The base subgroup input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: for eligible r the Sylow-r subgroup of A_r has the unique maximal overgroup AGL1(r)∩A_r. The written all-subgroup orbit induction and binomial-divisor calculation are those frozen in `frontier-20261028-alternating-orbit-induction-v1.md`, SHA-256 `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5`; their key conclusion is restated explicitly in Section 2. Both require independent review; no source classification proof or previous review is represented as completed here.

For the optional **infinitude** statement only, import the classical prime number theorem in arithmetic progressions π(x;4,1)∼x/(2 log x), e.g. https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The fixed-r subgroup conclusion does not require this analytic input. The orbit packet gives the independent elementary upper bound O(√x log x) on all prime-power-repunit primes ≤x, so the progression has infinitely many remaining eligible primes. The theorem is cited, not re-proved.

Writer exposure was nonblind, with the incidental cross-topic display documented in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No content of those excerpts is used, and no historical hold is changed.

## 2. Six buckets and the new collision

For j=1,…,6 define
\[L_j=\operatorname{lcm}(1,\ldots,j),\qquad
 d_j=\frac{r+j}{\gcd(r+j,L_j)}.\]
The cited written orbit induction says each proper subgroup index in A_(r+6) not divisible by r is divisible by at least one d_j, and every d_j>7. In any direct P7 pattern all seven indices are divisible by 7, and at most one is divisible by r>7. If all seven are r-free, two share one of six divisors d_j, contradiction. Otherwise precisely six are r-free and no two can share a d_j>7; hence these six must occupy all six buckets d1,…,d6 exactly once.

Always d1=r+1 is even. Since r>3 is prime, 3 does not divide r+3, so d3=(r+3)/2. If r≡1 mod 4, d3 is even. Then the indices assigned to d1 and d3 are both even and both divisible by 7, so their gcd is at least 14, contradiction.

If r≡3 mod 8, then r+5 is divisible by 8. Since v2(L5)=v2(60)=2, d5=(r+5)/gcd(r+5,60) is even. The indices assigned to d1 and d5 are again both divisible by 14, contradiction. These cases are precisely r≡1,3,5 mod 8. They imply the desired P7 exclusion without requiring a unique maximal overgroup in A_(r+6).

## 3. Explicit limit of this parity argument

The omitted residue r≡7 mod 8 is not silently covered. For the eligible prime r=431, the six bucket divisors are
\[(d_1,\ldots,d_6)=(432,433,217,145,109,437),\]
which are pairwise coprime. The seven integers
\[(7r,7d_1,\ldots,7d_6)=(3017,3024,3031,1519,1015,763,3059)\]
have every pairwise gcd exactly 7. Each even divides |A437|=437!/2: in each case the two factors 7 and the other factor, both distinct from 2 and at most 437, occur in the factorial. This is an **integer-level obstruction only**: no subgroups with those indices are constructed, and no counterexample to P7 or Sun8 is claimed. It shows why the six-bucket/parity argument alone cannot justify removing the stated residue restriction.

## 4. Actual finite control and review boundary

`frontier-20261028-alternating-residue-check.py`, SHA-256 `bc62109865dac90b49fff07cbfbbaa6c3ab97bae94a027794cd985c691e749df`, 52 LF / 1419 bytes, ran at 18:42:42 PDT on 2026-10-28. It used exact integer square roots, modular arithmetic and gcd/lcm to check primality and the repunit exclusions for r=419,421,431, calculate the buckets, check the two parity cases, and check the seven displayed gcds. It did not enumerate subgroups, prove the orbit induction, establish source classification, or prove the arithmetic-progression prime theorem.

**Review-critical:** check that the predecessor induction applies at j=6 to every r-free subgroup index, the exactly-one-per-bucket reasoning, the modulus conditions, the independent prime-counting bound, and the integer-only status of the r=431 obstruction. The r≡7 mod 8 case remains open for this refinement; no old HOLD or prior claim is rehabilitated.
