# Conditional alternating P7 progressions at offsets 39 and 40

**Status: WRITTEN candidate, conditional on the named public A_r theorem and prior exact quotient/factorial arguments; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2, and suppose r+1>7t!. Then direct P7 is excluded in these **conditional** cases:

| t | allowed r mod 7 | coprime classes mod 105 |
|---|---|---:|
| 39 | 1,2 | 16 of 48 |
| 40 | 1 | 8 of 48 |

No conclusion is asserted for the omitted classes, for arbitrary t≥36, for all alternating groups, or for unrestricted Sun8. Each displayed mod-105 class contains infinitely many eligible r under the additional prime-number-theorem-in-progressions import below. No priority or historical novelty is claimed.

## Proof and exact inputs

The public source is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2 for the unique Sylow-r maximal overgroup in A_r. The **unreviewed** exact quotient/seven-cell argument is `frontier-20261028-alternating-seven-cell-p7-v1.md` SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`; the separate **unreviewed** general-offset factorial incompatibility lemma is `frontier-20261028-alternating-factorial-general-v1.md` SHA `83f5f6884f76466408bc48cd264aa12f61b030ba1a338641c4af54e547c7d05a`. The latter is needed because the earlier uniform ≤10-prime proof was frozen only through t=35. No source-proof replay, independent review or Sun7 is implied.

In a hypothetical seven-index pattern, at least six indices are r-free and all are divisible by 7. The general factorial lemma prevents any one from taking a proper-A_r terminal. The exact quotient product then forces each r-free chain to consume a position h with 7|(r+h); its quotient c|u! cannot supply a factor 7 unless a consumed window has at least seven consecutive cells and thus itself contains such a position. Shared positions between labels would give a common divisor (r+h)/gcd(r+h,t!)>7. If h0=7−(r mod 7) is the first positive seven-cell, t=39 has at most five precisely when h0≥5, i.e. r mod7 is 1 or 2; t=40 has at most five precisely when h0≥6, i.e. r mod7 is 1. The six labels cannot occupy five cells.

At t=41, h0≤6 for every r prime>7, so **every** nonzero residue has six seven-cells. The present simple pigeonhole therefore gives no t=41 conclusion; this is a specific method boundary, not a counterexample.

For infinitude only, import the prime number theorem in progressions π(x;105,a)∼x/(48 log x) for each a coprime to 105, as stated e.g. in https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The elementary earlier repunit count is O(√x log x), so removing repunit primes and the finite size-threshold exceptions leaves infinitely many eligible r in each displayed class. The fixed-r statement does not require this analytic theorem.

Writer exposure was nonblind; the incidental cross-topic display is documented in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such content is used; historical holds are not changed.

## Actual control

`frontier-20261028-alternating-39-40-check.py`, SHA-256 `5820856425c94f8112606f77ed3a53aec1d0b525e5b8850a6d33c20ce77ef0ca`, 12 LF / 496 bytes, ran at 19:35:42 PDT on 2026-10-28. Exact integer arithmetic counted 16,8,0 eligible mod-105 seven-cell classes for t=39,40,41, respectively. This is not a subgroup enumeration, a source verification or a proof of progression infinitude. Independent review must reconstruct both source-dependent lemmas and the stated cell/progression scope.
