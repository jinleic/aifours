# E7(q): source-conditional exclusion of three, hence eight, small-gcd subgroup indices

**Status: WRITTEN candidate, with named external classification imports; not yet independently reviewed or accepted.** For every prime power q, assuming exactly the source statements identified below, the finite simple group E7(q) has no three proper subgroups whose indices have every pairwise gcd at most 7. Consequently it has no eight-index Sun8 counterconfiguration and no direct P7 counterconfiguration. This argument does **not** use Sun7, a normal-section reduction, a computer enumeration of subgroups, or the old E8/other-family packets. No assertion of research novelty or priority is made. The elementary part is written mathematics; source classification proofs have not been independently checked.

The key feature is that the regular unique-Sylow-overgroup argument does not cover E7(3). We handle that actual exceptional simple group using the explicitly tabulated orders of *both* possible maximal-overgroup types, rather than pretending that a Sylow 37-subgroup has a unique maximal overgroup.

## 1. Exact imported statements and boundaries

Write R for a Sylow r-subgroup of G, and M(R) for the set of maximal subgroups containing R.

1. The standard order and simplicity of E7(q), with q=p^f and d=gcd(2,q−1), are
   \[
   |G|=d^{-1}q^{63}(q^2-1)(q^6-1)(q^8-1)(q^{10}-1)
     (q^{12}-1)(q^{14}-1)(q^{18}-1).
   \]
   We use these from the E7 statement/proof of Proposition 7.8 in https://arxiv.org/html/2307.13976v2.
2. For r a primitive prime divisor of q^18−1, the E7 row of Theorem 2/Table C of that source gives |M(R)|=1 when its condition α(18,1) holds and at least one of: f>2; r>37; |R|>r; or (q,r)=(2,19). We use only these sufficient branches. Remark 9.2 defines α(18,1) by requiring (q^(1/k))^18 ≠ 1 mod r for each prime k dividing f, apart from the source's optional exclusion k=r. Proposition 7.8 identifies, in the E7(3), r=37 case, maximal overgroups of R as the standard maximal-rank type ²E6(3)×(3+1) and possibly almost-simple subgroups with socle PSL2(37), with no subfield subgroup. This is an imported classification-of-types statement, not proved here.
3. For the **actual finite simple E7(3)**, the subsequent classification https://arxiv.org/html/2201.07081v2, Corollary 1.2 and Tables 1.1 and 4.1, supplies the precise relevant subgroup shapes: the rank type has order 4|²E6(3)| (in Table 4.1, d=2 and e′=1), and an additional subgroup of the above almost-simple type has shape PSL2(37). Classes, if more than one, have the same respective orders. The Table 1.1 row lists two classes of PSL2(37) for p=3, since 15²≡3 mod 37. We only need the upper bound on possible orders, not existence of a particular almost-simple overgroup. That source includes computational methods in its subgroup classification; neither its computations nor its proof dependencies are reproduced here.
4. We use the standard order formula for ²E6(3), recorded in Proposition 7.7 of the 2024 source, and |PSL2(37)|=37(37²−1)/2. The former is 3^36 times a factor prime to 3. No disputed β sign in that source's twisted-E6 row is used here.
5. Zsigmondy's primitive-prime-divisor theorem is used only for p^(18f)−1 when f≥3; its exponent is then at least 54, outside the usual exceptions. The source classification, group simplicity and Zsigmondy are theorem imports, not claims of independent kernel verification.

## 2. The subgroup-index observation

Let G be finite nonabelian simple and let r>7 divide |G|. Every proper H<G has [G:H]≥8: otherwise its coset action embeds G in S_n for n=[G:H]≤7 (the core is a proper normal subgroup), which is impossible since r does not divide |S_n|.

Among three indices with pairwise gcd at most 7, at most one is divisible by r. For each r-free index [G:H], H contains a Sylow r-subgroup, which is conjugate in G to R. Conjugating H if necessary, H contains R and lies in some M∈M(R). Hence [G:M] divides [G:H]. If M(R) contains a single member, the two r-free indices among the three have common divisor [G:M]≥8, contradiction.

More generally, uniqueness is unnecessary if there is an integer D≥8 dividing [G:M] for **every** M∈M(R). Then the same two r-free indices are both divisible by D. We use this second version exactly for E7(3).

## 3. Elementary cyclotomic lemma

Put F(x)=x^6−x^3+1 for x≥2. The identity
\[(x^3+1)F(x)=x^9+1\]
shows that F(x) is odd, and if 3 divides F(x) then v₃(F(x))=1: for x≡−1 mod 3, x³≡−1 mod 9 and F(x)≡3 mod 9; otherwise F(x)≡1 mod 3.

If a prime r>3 divides F(x), then x⁹≡−1 mod r and the order of x mod r divides 18 but not 9. Its only remaining possibilities are 2, 6, 18. The first two force r|(x³+1), whereas gcd(F(x),x³+1) divides 3, since F(x)≡3 mod (x³+1). Thus ord_r(x)=18 and r≡1 mod 18. In particular such an r is at least 19.

## 4. All fields except q=3

### f≥3

Choose r with ord_r(p)=18f by Zsigmondy. Then ord_r(q)=18, r≡1 mod 18f and r>7. For every prime k|f, (q^(1/k))^18=p^(18f/k) is not 1 mod r, so α(18,1) holds. The source's f>2 branch yields |M(R)|=1; Section 2 excludes three indices.

### f=2

Let x=p². F(x) has no factor 3, because x≡0 or 1 mod 3, and no factor 2. Every prime divisor r of F(p²) therefore has ord_r(p²)=18 and hence ord_r(p)=36: if d=ord_r(p), then d/gcd(d,2)=18, forcing d=36. In particular r≡1 mod 36, r≥37, and α(18,1) holds because p^18 is not 1 mod r. Since F(p²)≥F(4)=4033>37, either a prime factor r is greater than 37 or 37² divides F(p²). In the former case use the r>37 branch; in the latter use r=37 and |R|>r, since r² divides q^18−1 and the central denominator d divides 2. Section 2 again applies.

### f=1, p=2 or p≥5

For p=2 take r=19: F(2)=57=3·19 and ord_19(2)=18. The source explicitly lists (q,r)=(2,19), so the unique-overgroup branch applies; α is vacuous.

For every prime p≥5, F(p)≥F(5)=15501>3·19·37. By Section 3, v₃(F(p))≤1 and all other prime factors are ≡1 mod 18. If no factor exceeds 37 and neither 19 nor 37 occurs twice, F(p) would divide 3·19·37, contradiction. Thus some r>3 dividing F(p) satisfies r>37 or r²|F(p). It is a primitive divisor of p^18−1, and the source applies the r>37 or |R|>r branch, respectively. Again α is vacuous and Section 2 applies.

The case p=3 is intentionally not included: F(3)=703=19·37 has no repeated factor and neither r exceeds 37. The unique-overgroup source condition is not asserted for either prime there.

## 5. The actual exceptional case E7(3)

Take r=37. We have 3^9≡−1 mod 37 and 3^6≡26 mod 37, so ord_37(3)=18. The group order in Section 1 gives v₃(|G|)=63 and v₃₇(|G|)=1. Thus the relevant Sylow 37-subgroup has order 37, and the E7(3) classification imports in Section 1 apply.

For the maximal rank subgroup, the exact tabulated order is 4|²E6(3)| and v₃ of this order is 36; its index therefore has v₃ equal to 27. For the other possible maximal overgroup type, the precise tabulated order is |PSL2(37)|=25308, with v₃=2; its index has v₃=61. There are no additional types under the named classification imports. Accordingly **every** M∈M(R) has 3^27 dividing [G:M]. Take D=3^27>7 in Section 2. This proves the claimed exclusion for E7(3) without falsely claiming that M(R) is a singleton.

The argument does not require the 2025 classification's open/ambiguous entries for other characteristics: Corollary 1.2 is the characteristic-3 statement, and the 2024 Proposition 7.8 restricts the r=37 overgroup types as stated. Source versions must remain part of the review packet.

## 6. Actual arithmetic control and remaining review boundary

`frontier-20261028-e7-cyclotomic-check.py`, SHA-256 `be863f8a5fa480ce430012908f178d3dc283ae7e1061a6fe5713f6981e9262c3`, 88 LF / 2485 bytes, was executed at 18:16:58 PDT on 2026-10-28. It uses Python integer arithmetic and exact trial factorization only. It checked (i) the displayed identity and v₃ bound for integers x=2,…,100; (ii) stated order/factor criteria for p=2,3,5,7,11,13,17,19 at f=1 and p=2,3,5,7,11 at f=2; (iii) exact E7(3)/rank-subgroup/PSL2(37) order divisibility and the 3- and 37-valuations printed by the script. These finite checks do **not** establish the all-field lemma, Sylow overgroup classification, subgroup existence, group simplicity, Zsigmondy, novelty, or human/formal verification.

**Review-critical imports:** verify the exact scope of Proposition 7.8/Theorem 2/Table C at G=T, the full rank and almost-simple overgroup types for E7(3), the q=3 shape extraction from Craven's Tables 1.1 and 4.1, and the subgroup-index reasoning. Acceptance remains conditional until such review, and previously frozen packets/hold records are unchanged.
