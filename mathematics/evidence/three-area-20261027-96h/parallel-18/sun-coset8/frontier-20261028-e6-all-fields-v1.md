# E6(q): source-conditional exclusion of three, hence eight, small-gcd subgroup indices

**Status: WRITTEN candidate, contingent on explicitly named external classification and order statements; not independently reviewed or accepted.** For every prime power q, the finite simple group E6(q) has, subject to these imports, no three proper subgroups whose indices have every pairwise gcd at most 7. In particular it has no eight-index Sun8 counterconfiguration and no direct P7 counterconfiguration. Neither Sun7 nor any normal-section reduction is assumed. No priority or novelty is asserted. External source proofs, source computations, and formal verification are not reproduced here.

The primitive-prime unique-maximal-overgroup condition has an actual exception at q=4. We treat E6(4) by bounding the 2-parts of *all* possible maximal overgroups of its Sylow 19-subgroup, rather than claiming uniqueness.

## 1. Exact imports

1. E6(q) is simple, and for q=p^f its order is
   \[
   |G|=\frac{q^{36}(q^2-1)(q^5-1)(q^6-1)(q^8-1)(q^9-1)(q^{12}-1)}{\gcd(3,q-1)}.
   \]
   We cite Proposition 7.6 of https://arxiv.org/html/2307.13976v2.
2. For a primitive prime divisor r of q^9−1, Theorem 2/Table C of that source gives a unique maximal overgroup of a Sylow r-subgroup when α(9,1) holds and at least one of f>2, r>19, or |R|>r holds. Remark 9.2 defines α(9,1) by requiring p^(9f/k) ≠ 1 mod r for each relevant prime divisor k of f. Proposition 7.6 says that for G=E6(4), r=19, the maximal overgroups of R, apart from the maximal rank type A2(4³), can only be almost simple with socle J3 or PSL2(19); α(9,1) removes subfield cases. This classification is an imported statement and its proof is not reconstructed.
3. The rank-type maximal subgroup has shape PSL3(4³).3, by Table 9 of https://arxiv.org/html/2103.04869v4. The v4 source says it includes known corrections and its abstract explicitly describes computational-algebra/Magma contributions. Its classification and computations are not reproduced here.
4. The ATLAS pages https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/J3/ and https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L219/ list |J3|=2^7·3^5·5·17·19, |PSL2(19)|=2²·3²·5·19, and outer automorphism groups of order 2 for both. Thus an almost-simple subgroup with either of these socles has 2-part at most 2^8 or 2^3 respectively. This intentionally overcounts possible overgroups: it does not assume the full outer extension actually occurs as a maximal subgroup of E6(4).
5. Zsigmondy's primitive-prime-divisor theorem is used for p^(9f)−1 when f≥3 only (exponent at least 27, outside the usual exceptions). The standard order formula |PSL3(Q)|=Q³(Q³−1)(Q²−1)/gcd(3,Q−1) is also used. All such cited statements are imports, not independently verified claims.

## 2. Index lemma

Let G be finite nonabelian simple, r>7 divide |G|, and M(R) be the maximal subgroups containing a fixed Sylow r-subgroup R. No proper subgroup has index below 8: its core-free coset action would embed G in S_n for n≤7, but r does not divide |S_n|.

In any three indices whose pairwise gcd is at most 7, at most one is divisible by r. Each of the other two subgroups contains a Sylow r-subgroup; conjugate it to contain R and place it inside some M∈M(R). Its original index is divisible by [G:M]. Therefore three such indices are impossible if either |M(R)|=1 or there is a single D≥8 dividing every [G:M], M∈M(R). In the unique case D=[G:M]≥8. This lemma is written here directly, independent of Sun7.

## 3. Cyclotomic facts

For x≥2 put A(x)=x^6+x^3+1 and B(x)=x^6−x^3+1. Then
\[(x^3-1)A(x)=x^9-1,\qquad (x^3+1)B(x)=x^9+1.\]
Both A and B are odd. If 3 divides A(x), then x≡1 mod 3 and x³≡1 mod 9, so A(x)≡3 mod 9; otherwise A(x)≡1 mod 3. Similarly 3|B(x) exactly when x≡−1 mod 3, and then B(x)≡3 mod 9. Thus each has 3-adic valuation at most 1.

If r>3 is prime and r|A(x), then r cannot also divide x³−1: A(x)≡3 mod x³−1. Since x⁹≡1, its order mod r is 9, so r≡1 mod 9, and because r is odd in fact r≡1 mod 18. If r>3 divides B(x), then x⁹≡−1; the possible orders 2 or 6 would imply r|x³+1, but B(x)≡3 mod x³+1. Hence the order is 18 and r≡1 mod 18. In either case r≥19.

## 4. All fields except q=4

### f≥3

Zsigmondy yields r with ord_r(p)=9f. Then ord_r(q)=9, r≡1 mod 9f and r>7. For each prime k|f, p^(9f/k)≠1 mod r, so α(9,1) holds. The source's f>2 branch gives a unique maximal overgroup of the Sylow r-subgroup, and the index lemma applies.

### f=1

A(p)≥A(2)=73>3·19. By Section 3, v₃(A(p))≤1 and every other prime factor is ≡1 mod 18. If no prime factor exceeded 19 and 19 occurred at most once, A(p) would divide 3·19, a contradiction. Thus some prime r>3 dividing A(p) has r>19 or r²|A(p). Its order mod p is 9, α(9,1) is vacuous, and in the second case |R|>r because r² divides the group order and r≠3. The source's corresponding branch and Section 2 apply.

### f=2 and p≥3

For r>3 dividing B(p), ord_r(p)=18 and ord_r(p²)=9. Moreover p^9≡−1 mod r, establishing α(9,1) for the only prime divisor k=2 of f. Since B(p)≥B(3)=703>3·19, the same prime-factor argument shows that some such r satisfies r>19 or r²|B(p). Hence the unique-overgroup branch and index lemma apply. The case p=2, q=4 is excluded from this argument: B(2)=57=3·19 and does not meet either numerical condition.

## 5. Exceptional E6(4)

Set r=19. Since 4 has order 9 modulo 19, r is a primitive divisor of 4^9−1. The order formula gives v₁₉(|G|)=1, so |R|=19. Also 2^9≡−1 mod 19, so α(9,1) holds for f=2. By the imports in Section 1, every M∈M(R) is the rank type PSL3(64).3 or is almost simple with socle J3 or PSL2(19).

Here v₂(|G|)=72: q^36=2^72, every q^d−1 is odd, and the denominator is 3. For the rank type, the standard PSL3 formula gives v₂(|M|)=18, because 64³=2^18 and the other factors and the .3 extension are odd. For the two almost-simple socles, the ATLAS outer-order bounds give v₂(|M|)≤8 and ≤3 respectively. Hence **every** M∈M(R) has v₂([G:M])≥54. Taking D=2^54 in Section 2 excludes three indices. This argument allows both outer extensions even if they are not actual maximal subgroups, so it does not depend on resolving the q=4 novelty notation.

## 6. Arithmetic control and review boundary

`frontier-20261028-e6-cyclotomic-check.py`, SHA-256 `68666e9b6b0535228f7617dd70845cf7ea81527e5e67e1d222361682383de12e`, 82 LF / 2379 bytes, was run at 18:19:31 PDT on 2026-10-28. It uses integer arithmetic and trial factorization; it checks the two identities and 3-adic bounds for x=2,…,100, factor/order conditions for the listed small p at f=1 and f=2, and exact E6(4), PSL3(64).3, J3 and PSL2(19) order divisibility and 2-/19-valuations. Its printed index valuations 54,65,70 refer to the **listed simple socle orders** for J3 and PSL2(19), while the written argument conservatively allows an additional outer factor 2. The checker does not classify maximal subgroups, prove any infinite statement, execute source Magma, or verify external proofs.

**Required review:** check the original E6(4) r=19 classification scope and rank-group normalization against both stated source versions, the two ATLAS outer-order imports, all primitive-prime cases, and the subgroup-index implication. No independently reviewed or novelty-cleared theorem is claimed here.
