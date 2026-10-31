# Alternating direct-P7 exclusions at offsets 36–38 in explicit residue classes

**Status: WRITTEN candidate, conditional on the named public A_r theorem and the previously written exact quotient/factorial lemmas; not independently reviewed, formally verified or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2, and let r+1>7t!. Direct P7 is excluded in A_(r+t) in each of these stated, nonexhaustive cases:

| t | allowed r mod 7 | coprime classes mod 105 |
|---|---|---:|
| 36 | 1,2,3,4,5 | 40 of 48 |
| 37 | 1,2,3,4 | 32 of 48 |
| 38 | 1,2,3 | 24 of 48 |

Here direct P7 means seven proper subgroups with all pairwise index gcds exactly 7. The omitted residue classes are **not** resolved by this packet. Each displayed class mod 105 contains infinitely many eligible primes, conditional on the standard prime number theorem in arithmetic progressions stated in Section 4. No unrestricted t≥36, Sun8, all-alternating/global, historical novelty or priority claim is made.

## 1. Source and written inputs

The public group input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, giving a unique maximal Sylow-r overgroup in A_r for eligible r. The exact alternating-block quotient, its product iteration, and seven-cell pigeonhole are written in `frontier-20261028-alternating-seven-cell-p7-v1.md` SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`. The separate general-offset factorial incompatibility lemma is `frontier-20261028-alternating-factorial-general-v1.md` SHA `83f5f6884f76466408bc48cd264aa12f61b030ba1a338641c4af54e547c7d05a`. Both are **unreviewed** written inputs; no acceptance, independent replay or source-proof verification is assumed. No Sun7 is used.

The writer was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such content is used, and no historic hold is changed.

## 2. Fixed-r seven-cell argument

Suppose seven actual proper-subgroup indices have all pairwise gcd 7. At most one is divisible by r>7, so at least six are r-free. The general factorial lemma implies none of the seven indices is divisible by (r−2)!: any such index would have another r-free index with gcd 7, contrary to that lemma. This is precisely where the stronger unreviewed factorial input is needed for the enlargement beyond the parent's ≤10-prime sieve classes.

For each r-free subgroup, the previously written projection chain therefore terminates at a full alternating block and has exact index product of binomial windows and quotient factors c|u!. If the chain used no position h with 7|(r+h), then every window has length at most 6, and both its binomial and its c|u! are 7-free. Its index would be 7-free, impossible. Thus every one of the six r-free labels consumes a seven-cell.

Different labels cannot consume the same cell: their binomials would share (r+h)/gcd(r+h,t!)>7 by r+1>7t!. Let h0∈{1,…,6} be the first positive solution of r+h0≡0 mod 7. For t=35+s with s=1,2,3, there are six seven-cells exactly when h0≤s. Since h0=7−(r mod 7), the displayed residue conditions are exactly h0>s, giving **five** seven-cells. Six labels cannot consume distinct cells. This proves the fixed-r conditional candidate.

## 3. Reproduction of the narrower parent sieve

For each residue a mod 105 coprime to 105, let
\[b_t(a)=1+\#\{k\in\{2,4,\ldots,2\lfloor t/2\rfloor\}:\gcd(a+k,105)=1\}.\]
For large prime r in the class, b_t(a) is an upper bound on the number of possible primes in [r−1,r+t]: r itself plus odd-offset candidates not already known composite by 3,5,7. The originally reported joint conditions b_t(a)≤10 and at most five seven-cells give 38,30,23 of the 48 classes for t=36,37,38. The seven-cell-only conditions above enlarge these to 40,32,24 classes, respectively. The additional mod-105 residues are {11,58}, {11,58}, and {58}.

For the narrower joint classes, one can alternatively avoid the new general factorial lemma: the earlier actual no-7p lemma and ≤10-prime singleton-support argument still exclude factorial terminals. Its inequalities C(r+1,2)>7(r+38) and (r−2)!>7(r+38) hold for r≥419. That fallback still depends on the public theorem, actual subgroup/no-7p proof, and exact quotient; it is not an independent review.

`frontier-20261028-alternating-conditional-sieve-check.py`, SHA-256 `bb99b4eb11edfc55cc59900356b957e0c753e08ca0b57855998bb0bdbcaa9085`, 25 LF / 1051 bytes, ran at 19:34:09 PDT on 2026-10-28. It reproduced the 38/30/23 joint counts, the 40/32/24 cell-only counts and the stated additional residue lists by exact integer arithmetic, and checked the inequalities at r=419. It does not prove subgroup statements or prime infinitude.

## 4. Each displayed arithmetic progression is infinite

The prime number theorem for arithmetic progressions is an additional **named import for infinitude only**: for gcd(a,105)=1,
\[\pi(x;105,a)\sim\frac{x}{\varphi(105)\log x}=\frac{x}{48\log x}.\]
For a standard statement see https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The earlier elementary calculation in `frontier-20261028-alternating-orbit-induction-v1.md`, SHA `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5`, bounds **all** prime-power-repunit primes up to x by O(√x log x). Subtracting these and the finite size/threshold exceptions from each displayed progression leaves infinitely many eligible r, in fact asymptotically the same x/(48 log x) count. The fixed-r subgroup conclusion does not depend on this analytic import.

**Review-critical:** inspect the general factorial incompatibility argument and c|u! exact iteration, the mod-7 cell count and three stated class counts, the fallback no-7p/≤10 argument, and the progression and repunit count. No source theorem, sibling work, historical hold, or previous DP case is implicitly adopted.
