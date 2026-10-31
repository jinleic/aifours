# Alternating simple groups: three-index exclusion in four prime-parameter families

**Status: WRITTEN candidate, conditional on the exact public maximal-overgroup theorem below; not independently reviewed or accepted.** Let r≥11 be an odd prime and let G=A_n in any of these cases:

1. n=r^k+1 with k≥2;
2. n=2r;
3. n=r²;
4. n=r, r∉{11,23}, and r is not (q^d−1)/(q−1) for any prime power q and integer d≥2.

Then G has no three proper subgroups whose indices have every pairwise gcd at most 7. In particular it excludes the direct P7 and Sun8 configurations. The families are infinite at least in the first three cases, since there are infinitely many primes r≥11. This statement neither invokes Sun7 nor claims all alternating simple groups. No discovery, published-priority or novelty claim is made.

**Nonblind provenance:** the writer had earlier Sun8 normal-section/R8 and source exposure; this candidate uses only the public theorem and elementary argument stated here, but is not represented as a clean or blind derivation. An unrelated overbroad search incident is recorded, without mathematical content, in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no Olson/Kac-Moody snippet was used as an input or proof. Original historical holds remain unchanged. A narrowly scoped text search of the named Sun parent normal-section record, `reduction-and-generation-v1.md`, and `consolidated-chain-v1.md` returned no matches for the alternating-family terms queried; it was not an exhaustive priority or earlier-packet audit.

## 1. Precise public input

Theorem 2(i)(a)–(d) of https://arxiv.org/html/2307.13976v2 says the following for G=T=A_n, odd prime r, and a Sylow r-subgroup R: in each listed case the set M(R) of maximal overgroups is the singleton {M}, where respectively

1. M=A_(n−1) for n=r^k+1, k≥2;
2. M=(S_r wr S_2)∩A_(2r) for n=2r;
3. M=(S_r wr S_r)∩A_(r²) for n=r²;
4. M=AGL1(r)∩A_r for n=r with r≠11,23 and either r=5 or r not of the displayed prime-power repunit form.

The present r≥11 range uses only the second alternative in item 4. We also import the standard simplicity of A_n for n≥5 and standard finite-group Sylow/Lagrange results. The source's Proposition 4.2 explicitly says n≤24 can be handled with Magma before proceeding to n≥25. Consequently cases in that small range—including n=22 and the n=19 example below—carry this source-reported, unreproduced computational handling. Neither the source classification/proof DAG nor any source Magma calculation is independently reproduced here.

## 2. Written proof

In each of the four cases G is nonabelian simple and r>7 divides |G|. Every proper subgroup has index at least 8: a coset action at index n≤7 has trivial core by simplicity and would inject G into S_n, but r does not divide |S_n|.

For any three positive subgroup indices with pairwise gcd≤7, at most one is divisible by r. Each of the other two subgroups contains a Sylow r-subgroup; conjugate it to contain the fixed R. It is then contained in a maximal subgroup containing R, which the public theorem identifies uniquely as M. Thus [G:M] divides each of those two indices. As M is proper, [G:M]≥8, contradicting the gcd bound. This proves the claimed three-index exclusion for all four actual group families, including all coset configurations since their underlying proper subgroups would already violate the conclusion.

## 3. Exact common divisors in the four families

The proof only needs [G:M]≥8, but the source's subgroup types give the following exact values:

1. r^k+1.
2. (1/2)·binom(2r,r), the number of unordered partitions into two r-element blocks.
3. (r²)!/((r!)^r r!), the number of unordered partitions into r blocks of size r.
4. (r−2)!, because AGL1(r) has order r(r−1) and has an odd element: multiplication by a generator of F_r^× fixes 0 and acts as one (r−1)-cycle on the nonzero points. Its intersection with A_r therefore has half its order.

For cases 2 and 3, the relevant wreath product also contains odd permutations, so intersecting with A_n divides its symmetric-group order by 2. These index formulas are auxiliary arithmetic, not new maximal-subgroup classifications.

For a concrete nonempty case 4, r=19 qualifies. If 19=1+q+⋯+q^(d−1) with q≥2 and d≥2, then 2^d−1≤19 forces d≤4. At d=2 one gets q=18, which is not a prime power; at d=3 the values for q=3,4 straddle 19, and at d=4 those for q=2,3 do likewise. Thus no permitted repunit representation exists. This one check does not claim infinitely many primes satisfy case 4.

## 4. Actual exact control and review boundary

`frontier-20261028-alternating-index-check.py`, SHA-256 `d4ed0bad8b298f8493144fd8be200fc628df798053ec91cbe8d80c2f8a97fdb8`, 48 LF / 1349 bytes, ran at 18:33:33 PDT on 2026-10-28. It checked the two wreath-order arithmetic identities for r=11,13,19, and exhaustively checked the elementary r=19 geometric-sum possibilities described above. The computation is finite integer arithmetic, not a maximal-subgroup enumeration or proof of the all-prime theorem.

**Review-critical:** check the exact Theorem 2(i) application to the simple group G=T, particularly the r^k+1 and wreath cases, intersections with A_n, the excluded repunit cases, and the subgroup-index argument. The quoted public classification and its n≤24 Magma branch remain named unreviewed imports; this packet does not adjudicate old frozen findings or the remaining alternating degrees outside the stated families.
