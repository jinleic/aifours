# Triality groups ³D4(q): source-conditional three-index exclusion

**Status: WRITTEN candidate, conditional on named external results; no independent review, formal verification, adoption or novelty claim.** For every prime power q, the finite simple triality group ³D4(q) has no three proper subgroups whose indices have every pairwise gcd at most 7. Consequently the direct P7 and Sun8 configurations are excluded for this simple-group family. Neither Sun7 nor a normal-section reduction is imported.

## Named external inputs

- Proposition 7.3 and Theorem 2/Table C of https://arxiv.org/html/2307.13976v2, at G=T=³D4(q): for a primitive prime divisor r of q^12−1, a Sylow r-subgroup R has exactly one maximal overgroup provided (q^(1/k))^6 is not −1 modulo r for every prime k dividing f except the explicitly exempted k=3,r, where q=p^f. The proposition quotes the maximal-subgroup classification; neither that classification nor the source proof DAG is independently reproduced here.
- The simplicity and order |³D4(q)|=q^12(q²−1)(q⁶−1)(q⁸+q⁴+1), also stated in the proposition.
- Zsigmondy's primitive-prime-divisor theorem for p^(12f)−1; exponent 12f≥12 is outside its exceptions.

## Written argument

Choose r with ord_r(p)=12f. Then ord_r(q)=12f/gcd(12f,f)=12, and r≡1 mod 12f, so r≥13>7. For every prime k|f, the congruence p^(6f/k)≡−1 mod r would imply p^(12f/k)≡1, contradicting the definition of the order. Hence the cited condition holds for **all** primes k|f, in particular for its required subset, and the chosen R has one maximal overgroup M.

The prime r divides |G|: q^6≡−1 mod r and q²≠−1 mod r, so r divides q⁴−q²+1. The identity
\[(q^2-q+1)(q^2+q+1)(q^4-q^2+1)=q^8+q^4+1\]
places that factor in the group order. Also [G:M]≥8: a smaller proper index gives a faithful coset action G→S_n for n≤7 (simplicity makes the core trivial), but r>7 divides |G| and not |S_n|.

Suppose three proper subgroup indices have pairwise gcd≤7. At most one is divisible by r. Each of the other two subgroups contains a Sylow r-subgroup; after conjugation it contains R and hence lies in its unique maximal overgroup M. Their original indices are therefore both divisible by [G:M]≥8, contradicting their pairwise gcd bound. This also excludes every longer configuration, including the stated eight-index target.

## Exact finite control and boundary

`frontier-20261028-triality-primitive-check.py`, SHA-256 `5485966aeeafa6f8eeeccb884c32397a64e651af70ca91b7e6a8a69c0173cb49`, 42 LF / 1144 bytes, was run at 18:24:43 PDT on 2026-10-28. Using integer trial factoring and modular arithmetic it found and checked primitive primes and the relevant subfield congruences for p=2,3,5,7 and f=1,2,3; it also checked the displayed factor identities for those 12 q values. This finite check does not establish the all-field conclusion, classify subgroups, or prove the cited sources. Review must specifically check the 2024 source's G=T applicability, its exclusions k=3,r, the primitive-order implication and the elementary index lemma.
