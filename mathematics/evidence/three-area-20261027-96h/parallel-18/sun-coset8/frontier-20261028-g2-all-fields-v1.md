# G2(q)′: source-conditional exclusion of three small-gcd subgroup indices

**Status: WRITTEN candidate, conditional on explicitly identified external classification/order inputs; not independently reviewed or accepted.** For every prime power q, the finite nonabelian simple group G2(q)′ has no three proper subgroups whose indices have every pairwise gcd at most 7. Consequently it has no direct P7 or Sun8 configuration. Here G2(q) is already simple for q≥3 and G2(2)′≅PSU3(3). No Sun7 or normal-section theorem is assumed. No novelty or priority is claimed.

Unlike a blanket unique-maximal-overgroup argument, the proof keeps the p=3 family, G2(4), and G2(2)′ separate and uses common index divisors for them.

## 1. Named source and theorem imports

1. Proposition 7.4, Theorem 2/Table C, and Remark 9.2 of https://arxiv.org/html/2307.13976v2: for G=G2(q), q≥3, the order is q⁶(q⁶−1)(q²−1). In characteristic 2, q≥8, a primitive r of q⁶−1 with α(3,−1) gives a unique Sylow-r maximal overgroup. In characteristic p≥5, for a primitive r of q³−1 or q⁶−1 with the matching α(3,+1) or α(3,−1), either r>13 or |R|>r is sufficient for a unique Sylow-r maximal overgroup. The same source identifies G2(2)′≅U3(3). These are imports, not independently reconstructed classification proofs.
2. For odd q≥7, Table 2 of https://www.personal.kent.edu/~htongvie/Publications/G2.pdf lists maximal subgroups. We use it at q=3^f with f≥2 as a **complete list of possible types**; our type-by-type r and 3-part extraction is in Section 4. The source's other results are not imported. Its underlying subgroup classification and any computations are not independently verified here.
3. The ATLAS pages https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/G23/ and https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/G24/ list the maximal types of the simple groups G2(3) and G2(4), respectively. The GAP Character Table Library page https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/U3%283%29.html lists the maximal indices 28,36,63,63 of U3(3). These exhaustive lists and the standard group orders used to calculate their indices are imports, not subgroup enumerations performed here.
4. Zsigmondy's theorem is used at exponents 6f≥12 or 6f≥18 as explicitly stated below. Its n=6, base 2 exception is not used. Elementary standard PSL3, PSU3 and PSL2 order formulas are used for the finite cases.

## 2. Index lemma

For a finite nonabelian simple G and r>7 dividing |G|, every proper subgroup index is at least 8: the core-free coset action would otherwise embed G into S7, whose order is not divisible by r. In a three-index pattern with pairwise gcd≤7 at most one index is r-divisible. Each r-free subgroup contains a Sylow r-subgroup, conjugate to a fixed R; placing it inside a maximal overgroup M gives [G:M] dividing its original index. Therefore three indices are impossible if R has a unique maximal overgroup, or if every such [G:M] is divisible by one common D>7. We shall use both forms.

## 3. Characteristics other than 3

### Characteristic 2, f≥3

Put q=2^f. Choose r with ord_r(2)=6f by Zsigmondy. Then ord_r(q)=6 and r>7. For each prime k|f, 2^(3f/k)≠−1 mod r, since otherwise its square would contradict the order. Thus α(3,−1) holds, and the p=2, q≥8 source branch gives a unique maximal overgroup. Section 2 applies. The cases q=2,4 are handled in Section 5.

### Characteristic p≥5, f≥3

Choose r with ord_r(p)=6f. Then ord_r(q)=6, r≡1 mod 6f and r>13. As above α(3,−1) follows by squaring, and the source gives a unique maximal overgroup. Section 2 applies.

### Characteristic p≥5, f=2

Set C=p⁴−p²+1. The identity (p²+1)C=p⁶+1 and C≡1 mod 2,3 show every prime r|C has ord_r(p)=12: possible order 4 would imply r|p²+1, but C≡3 modulo p²+1. In particular r≡1 mod 12 and r≥13. Since C≥C(5)=601>13, some factor r is >13 or 13² divides C. Select that r. Then ord_r(q)=6, and α(3,−1) holds because ord_r(p)=12 prevents p³≡−1. In the repeated-13 case |R|>13 as the r² factor survives in the group order. The source's indicated branch and Section 2 apply.

### Characteristic p≥5, f=1

For p=5 choose r=31, a primitive divisor of 5³−1, which is >13. For p≥7 define A=p²+p+1 and B=p²−p+1. They are odd and coprime: gcd(A,B) divides 2p and neither is divisible by 2 or p. Each has 3-adic valuation at most 1. A prime r>3 dividing A has ord_r(p)=3; a prime r>3 dividing B has ord_r(p)=6. Therefore, apart from 3, their prime factors are 1 mod 6, and the only ones at most 13 are 7 and 13.

Both A and B exceed 39 when p≥7. At most one is divisible by 7. Choose a 7-free one. If it had no prime >13 and at most one factor 13, it would divide 3·13=39, impossible. Hence it has a prime r>13 or a factor 13²; in the latter case |R|>13. The chosen r is >7, is a primitive r3 or r6 as appropriate, and α is vacuous. The source's corresponding unique-overgroup branch applies.

## 4. Characteristic 3, all f≥2

Let q=3^f. Choose r with ord_r(3)=6f; then ord_r(q)=6 and r>7. We extract from the imported odd-q table the following bound on each maximal subgroup M whose order is divisible by r:

- Parabolics, the A1(q)A1(q) type, and the SL3(q):2 type have non-characteristic order factors among q^d−1 with d=1,2,3, so none contains r.
- SU3(q):2 has 3-part q³. A possible small-Ree subgroup ²G2(q) at odd f has 3-part q³ as well.
- A proper subfield group G2(q0), q0=3^(f/k) with prime k|f, cannot contain r: its non-characteristic factors have exponents at most 6f/k, strictly below ord_r(3)=6f.
- The other types listed in the imported table either have incompatible field/characteristic conditions or, if overcounted, have 3-part at most q³. In particular PSL2(13) has 3-part 3; the other fixed small candidates have no prime r>7 relevant to their characteristic-3 occurrence. Exact table scope is review-critical.

Consequently v₃(|M|)≤3f while v₃(|G|)=6f, so every [G:M] is divisible by D=3^(3f)>7. Section 2 proves the exclusion. We do not pretend that the two characteristic-3 maximal A2 classes are a singleton.

## 5. Three small simple groups

- **G2(3):** r=13. From the imported ATLAS maximal list the only types with 13 dividing their orders are the two classes PSL3(3):2 and PSL2(13). Their indices are 378 and 3888, with 3-adic valuations 3 and 5. Thus every relevant index is divisible by 27>7; Section 2 applies. Here G2(3) has order 4,245,696.
- **G2(4):** r=13. From its ATLAS list the only 13-containing maximal types are PSU3(4):2 and PSL2(13), of indices 2016 and 230400. Both are divisible by 32>7; Section 2 applies. The other maximal types listed in the source have no 13 in their orders.
- **G2(2)′≅U3(3):** the imported complete maximal-index list is 28,36,63,63. Every proper subgroup index is divisible by 28 or 9. Three indices therefore have two divisible by the same one of these two numbers, giving gcd>7. No r>7 is assumed for this small group.

## 6. Actual arithmetic checks and remaining boundary

`frontier-20261028-g2-cyclotomic-check.py`, SHA-256 `d3b68f3f723a5a787e759c830b6831ad5bd5cc4af8ab7ade9f795c6ea8fb7481`, 72 LF / 2146 bytes, ran at 18:29:42 PDT on 2026-10-28. Exact integer factoring and modular arithmetic checked the stated Φ3/Φ6 prime properties and Φ12 cases for p=5,7,11,13,17,19,23,29,31; primitive candidates at (p,f)=(2,3),(2,4),(3,2),(3,3),(3,4); and the displayed G2(3), G2(4), U3(3) integer indices and valuations. It did not reconstruct source subgroup lists or prove any universal claim.

**Review-critical:** reconstruct every characteristic-3 source-table row and its order/field restriction, check that all possible r-containing overgroups have 3-part≤q³, verify complete ATLAS/GAP lists and exceptional source branches, and check every primitive-prime implication. Until then this is a source-conditional written candidate, not an independently reviewed theorem.
