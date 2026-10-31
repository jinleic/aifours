# F4(q): source-conditional exclusion of three, hence eight, small-gcd subgroup indices

**Status: WRITTEN candidate, conditional on the explicit external inputs below; not independently reviewed or accepted.** For every prime power q, the finite simple group F4(q) has, subject to those imports, no three proper subgroups whose indices have every pairwise gcd at most 7. Consequently it has neither an eight-index Sun8 counterconfiguration nor a direct P7 counterconfiguration. No Sun7, normal-section reduction, source proof reconstruction, formal proof, or novelty/priority claim is used.

Odd characteristic is handled by a unique-Sylow-maximal-overgroup source theorem. In characteristic 2 there can be two nonconjugate maximal overgroups of the relevant type and, in odd extension degree, a Ree subgroup as well. We instead extract a **common 2-power divisor of every relevant index** from the full cited maximal-subgroup tables.

## 1. Exact external inputs

1. F4(q) is simple and has order
   \[|F4(q)|=q^{24}(q^{12}-1)(q^8-1)(q^6-1)(q^2-1).\]
   Use Proposition 7.5 of https://arxiv.org/html/2307.13976v2 and its group-order statement.
2. For q=p^f odd and r a primitive divisor of q^12−1, that paper's Proposition 7.5 gives a unique maximal overgroup of a Sylow r-subgroup when α(6,−1) holds and either r>13 or |R|>r. Remark 9.2 defines α(6,−1) as (q^(1/k))^6≠−1 mod r for each relevant prime k|f.
3. For q even, we import the full classification of maximal subgroups of the **simple** group F4(q) in https://arxiv.org/html/2103.04869v4, Theorem 1.1 and Tables 1 and 8, including the source's stated correction version. Table 8 entries marked Nov. occur only in an extension inducing a graph automorphism and are not maximal subgroups of simple F4(q). This source explicitly uses computational algebra/Magma; neither its classification proof nor its computational checks are reproduced.
4. Standard order formulas for ³D4(q) and ²F4(q) at q=2^(2m+1) are used in their displayed forms in Section 4. The latter includes the full, nonsimple ²F4(2) at q=2; do not replace it silently by its simple derived subgroup. They are recorded, for example, in Table 9 of https://www.renyi.hu/~maroti/centralizer12.pdf. The elementary PSL4(3) and PSL2(27) order formulas and Zsigmondy's primitive-prime theorem are also imported. Exponents 12f and the odd-characteristic exponents below are outside Zsigmondy's exceptions.

**Source discrepancy, not silently resolved:** the 2024 source's Proposition 7.5 gives an additional f∉{1,3} sufficient branch, while Table C prints f≠3. We use neither of those branches: in every odd-characteristic application below we explicitly satisfy r>13 or |R|>r, which appears in both. No opinion about which differing source formulation is correct is claimed.

## 2. Elementary index lemma

Let G be finite nonabelian simple, let r>7 divide |G|, and let M(R) be the maximal subgroups containing a Sylow r-subgroup R. A proper subgroup H has index at least 8, since its coset action has trivial core and an embedding G→S_n for n≤7 would contradict r||G|.

Among three indices with pairwise gcd≤7 at most one is divisible by r. A subgroup with r-free index contains a Sylow r-subgroup; after conjugation it contains R and is contained in some M∈M(R). Its index is therefore divisible by [G:M]. Thus three such indices cannot exist when M(R) is a singleton, or more generally when a fixed integer D>7 divides [G:M] for every M∈M(R). This argument is direct and does not assume Sun7.

## 3. Odd characteristic

Let q=p^f with p odd. If f≥2, choose r with ord_r(p)=12f by Zsigmondy. Then ord_r(q)=12, r≡1 mod 12f, so r>13, and α(6,−1) holds: if p^(6f/k) were −1 for any prime k|f, squaring would contradict ord_r(p)=12f. The source theorem gives |M(R)|=1.

For f=1 put C(p)=p^4−p²+1. We have (p²+1)C(p)=p^6+1 and C(p)≡1 modulo both 2 and 3. If a prime r divides C(p), then p^6≡−1 mod r, so its order divides 12 but not 6; the only possibilities are 4 or 12. Order 4 would force r|p²+1, but C(p)≡3 mod p²+1, impossible because 3∤C(p). Thus ord_r(p)=12 and r≡1 mod 12, so r≥13. Since C(p)≥C(3)=73>13, either a factor r>13 exists or 13²|C(p). In the first case use r>13; in the second choose r=13 and note |R|>r because r² divides the displayed F4 order. α is vacuous. The source again gives a singleton and Section 2 excludes three indices.

## 4. Even characteristic: source-table extraction

Write q=2^f and choose r with ord_r(2)=12f by Zsigmondy. Then ord_r(q)=12. For f=1, C(2)=13 and r=13. For f≥2, r>13. Since every prime factor with order 12 appears in q^12−1, r divides |G|; the 2-part of |G| is q^24.

We spell out the table extraction so that the source dependency can be audited rather than hidden:

- Among the unmarked simple-group entries of Table 8 other than subfield and Ree types, an r of order 12 mod q can occur only in ³D4(q).3. The parabolic, Sp8, PΩ8+, and A2-product rows have only q^d−1 factors with d∈{1,2,3,4,6,8}, plus 2 and 3 from the displayed extensions. None is divisible by r. The ³D4 row has two conjugacy classes in the simple group, both the same order.
- A subfield row F4(q0), where q= q0^k and k is a prime divisor of f, cannot contain r: if r divided a q0^d−1 factor for d∈{2,6,8,12}, then 12f would divide (f/k)d, forcing 12k≤d≤12. Its characteristic-power factor cannot supply odd r. This also covers all such entries without assuming their absence.
- The table permits ²F4(q) when f is odd. We retain it as a possible r-containing maximal type; no uniqueness or existence inference is needed. Both this type and ³D4(q).3 have 2-part exactly q^12:
  \[
  |{}^3D4(q)|=q^{12}(q^8+q^4+1)(q^6-1)(q^2-1),
  \quad |{}^2F4(q)|=q^{12}(q^6+1)(q^4-1)(q^3+1)(q-1).
  \]
  The .3 extension does not change the 2-part.
- Table 1's almost-simple rows for p=2 reduce, at q=2, to PSL4(3).2₂, and at q=8 to PSL2(27); the latter has order 2²·3³·7·13. Thus for f≥2 its possible occurrence cannot contain the chosen r>13. At f=1 the PSL4(3).2₂ type has 2-part 2^8, at most q^12=2^12. The other Table 1 rows have p/field conditions excluding p=2 or the relevant q. This finite table reading, including the q=2/8 cases, is part of the external-source review boundary.

Consequently, for every M containing R, v₂(|M|)≤12f, so 2^(12f) divides [G:M]. Take D=2^(12f)>7 in Section 2. This covers all f≥1, including F4(2), without assuming that the Ree subgroup is simple or that the two ³D4 classes coincide.

## 5. Actual exact arithmetic controls

`frontier-20261028-f4-cyclotomic-check.py`, SHA-256 `52252c1e1946631c410e298c419a13958445328847e53b0a0654c44e6ce9b60d`, 73 LF / 2120 bytes, ran at 18:22:23 PDT on 2026-10-28. Integer operations/trial factoring checked the C(x) identity and its 2- and 3-residues for x=2,…,100; factorizations and order criteria for p=3,5,7,11,13,17,19,23,29,31; q=2,4,8 primitive divisors and exact F4/³D4/Ree integer order divisibility and 2-valuations where the Ree type is applicable; and the displayed small-group 2-part/factor data. It did not enumerate any actual maximal subgroup, verify any source Magma proof, or establish any infinite statement.

**Review-critical boundary:** verify the characteristic-2 complete table extraction, especially the unmarked vs novelty scope, ²F4(2) versus its derived group, both ³D4 classes and their orders, and all p=2 almost-simple entries; then check the primitive-prime and common-index argument. The cited classification, Zsigmondy, group simplicity and order formulas remain external inputs. No review/adoption is claimed.
