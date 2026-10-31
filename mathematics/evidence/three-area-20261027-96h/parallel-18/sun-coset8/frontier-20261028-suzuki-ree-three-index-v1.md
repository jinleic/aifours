# Suzuki and Ree simple groups: source-conditional three-index exclusion

**Status: WRITTEN candidate, contingent on the stated maximal-subgroup and order imports; no independent review, formal verification, adoption, or novelty claim.** Each of the following simple groups has no three proper subgroups whose indices all have pairwise gcd at most 7, assuming the named external statements:

- Suzuki ²B2(2^f), f odd and f≥3;
- small Ree ²G2(3^f), f odd and f≥3, and the exceptional derived group ²G2(3)′≅PSL2(8);
- large Ree ²F4(2^f)′, f odd and f≥1, including the Tits group at f=1.

Thus all these groups exclude the direct P7 and Sun8 configurations. For Suzuki and small Ree this is a strictly stronger, source-different successor to the earlier eight-index packets `frontier-20261028-suzuki-simple-family-v1.md` and `frontier-20261028-small-ree-simple-family-v1.md`: the general f≥3 argument below does **not** import Sun5 or Sun7. Those earlier frozen bytes are unchanged. This is not a statement of historical novelty.

## 1. Exact source imports

1. Proposition 7.1 of https://arxiv.org/html/2307.13976v2 gives the order, simplicity, and unique Sylow-r maximal-overgroup conditions for Suzuki and small Ree groups. For Suzuki, r has order 4 modulo q and (q^(1/k))²≠−1 mod r for the source's relevant prime k|f. For small Ree, r has order 6 modulo q and α(3,−1) requires (q^(1/k))³≠−1 for its relevant prime k|f. The source identifies ²G2(3)′ with PSL2(8).
2. Proposition 7.2 of that source gives, for f odd≥3, the order, simplicity, and unique Sylow-r maximal-overgroup criterion for large Ree ²F4(2^f), with r of order 12 modulo q and α(6,−1). It explicitly notes the corrected PGL2(13) maximal subgroups at q=8 and explains why they do not contain a primitive r12; we do not import the obsolete uncorrected table. The Tits case f=1 is not covered by the unique-overgroup statement.
3. https://brauer.maths.qmul.ac.uk/Atlas/v3/group/TF42/ lists T=²F4(2)′ of order 2^11·3^3·5²·13 and its maximal subgroup types. Among them the only types whose order is divisible by 13 are the two classes of PSL3(3):2, each of order 11232, and PSL2(25), order 7800. We use this as an external exhaustive table; it is not reconstructed here.
4. https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L28/ lists PSL2(8), order 504, and its maximal subgroup types of orders 56,18,14. We import the list as exhaustive.
5. Zsigmondy's primitive-prime-divisor theorem is used for p^(ef)−1 at (p,e)=(2,4),(3,6),(2,12), with f odd≥3. The exponents are at least 12,18,36 respectively and avoid its exceptions. Source classification proofs, any associated computation, order formulas and group simplicity are not independently verified here.

## 2. Direct finite-group observation

Let G be finite nonabelian simple and r>7 divide |G|. A proper subgroup has index≥8: an index≤7 would give a faithful coset action G→S7, impossible since r does not divide |S7|. If three indices have all pairwise gcd≤7, at most one is divisible by r. Every r-free index comes from a subgroup containing a Sylow r-subgroup and, after conjugation, is divisible by [G:M] for some maximal M containing a fixed Sylow R. Therefore the three-index pattern is impossible if either M(R) is a singleton or every [G:M], M∈M(R), has a common divisor D>7.

## 3. All nonexceptional Suzuki and Ree parameters

For the three families take respectively (p,e)=(2,4), (3,6), (2,12), and q=p^f. Zsigmondy gives a prime r with ord_r(p)=ef. Then ord_r(q)=e and r≡1 mod ef, in particular r>7. The source group-order factors show r divides |G|: r|q²+1 in the Suzuki case, r|q³+1 in the small Ree case, and r|q⁶+1 in the large Ree case.

For any prime k|f, the congruence p^((e/2)f/k)≡−1 mod r would imply p^(ef/k)≡1, contradicting ord_r(p)=ef. Thus **all** source-relevant subfield congruences hold, including any primes the source elects to exempt. Each named source then gives exactly one maximal overgroup for R, and Section 2 excludes three indices. This applies to every allowed f odd≥3, including q=8 in the large Ree family despite the corrected extra PGL2(13) overgroups.

## 4. Tits group at q=2

Let G=²F4(2)′ and r=13. The imported ATLAS list shows all maximal overgroups of a Sylow 13-subgroup have one of the two orders 11232 or 7800. Their indices are 1600 and 2304, respectively; gcd(1600,2304)=64. Thus every 13-free subgroup index is divisible by 64. Since r>7, the common-divisor form of Section 2 excludes three indices. We do not assert a unique maximal overgroup or confuse T with the nonsimple group ²F4(2).

## 5. Exceptional small Ree group at q=3

Here G≅PSL2(8). By the imported complete ATLAS list, maximal subgroup indices are 504/56=9, 504/18=28 and 504/14=36. Every proper subgroup index is a multiple of at least one of these, hence is divisible by 9 or 28. Among any three indices two share one of those two divisors, so their gcd exceeds 7. This argument deliberately does not treat 7 as if it were greater than 7 and does not require a unique Sylow overgroup.

## 6. Actual exact finite control

`frontier-20261028-twisted-rankone-check.py`, SHA-256 `007469600b4e51c361159442885df1691918b8a7182259e72ae907261b2787b4`, 57 LF / 1759 bytes, ran at 18:26:48 PDT on 2026-10-28. With integer trial factoring and modular arithmetic it checked the three source-style primitive primes and all prime-factor subfield congruences at f=3,5,7; it also computed the two Tits indices and their gcd, and the three PSL2(8) maximal indices. These finite computations do not establish any infinite theorem, prove that the source maximal-subgroup lists are exhaustive, or verify an external classification.

**Review-critical:** check source formulas and unique-overgroup scope, the f=1 identifications, completeness and interpretation of both ATLAS lists, all exceptional subgroup orders and subgroup-index pigeonholes. The prior eight-index packets and all earlier holds remain unmodified.
