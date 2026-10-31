# Saturated seven-cell frontier at alternating offset 41

**Status: WRITTEN necessary-condition/obstruction packet, conditional on the cited source and written quotient/factorial lemmas; not a P7 exclusion or counterexample.** Let r≥419 be eligible for the public A_r theorem and satisfy r+1>7·41!. In any hypothetical seven-index pattern with pairwise gcd exactly 7 in A_(r+41), the six-seven-cell count is saturated: exactly one index is divisible by r, the other six consume the six distinct positions h with 7|(r+h), and each of their chains consumes exactly one such cell. The following exact local quotient constraints and a 7-local model show what remains to be paid. No claim is made that the local model can be realized by seven global subgroups or has pairwise gcd 7.

## 1. Named inputs

The unique-maximal-overgroup theorem for A_r is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2. The previously written, **unreviewed** exact index factorization and window disjointness are in `frontier-20261028-alternating-seven-cell-p7-v1.md` SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`; the general-offset factorial incompatibility input is `frontier-20261028-alternating-factorial-general-v1.md` SHA `83f5f6884f76466408bc48cd264aa12f61b030ba1a338641c4af54e547c7d05a`. This packet does not assume those are adopted and does not claim source-proof replay. No Sun7 is used.

Writer exposure was nonblind and the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such content is used and no historical hold is changed.

## 2. Exact saturation and local 7-adic data

For r prime>7, the first seven-cell h0 is in {1,…,6}; the six cells are h_i=h0+7i, i=0,…,5, all at most 41. A hypothetical seven-pattern has at most one r-divisible index. Each r-free index must consume a seven-cell by the written exact-product argument, and different indices cannot share a cell because the retained numerator divisor (r+h)/gcd(r+h,41!) exceeds 7. Seven r-free labels would need seven cells, so there is exactly one r-divisible label and exactly six r-free labels. All six cells are used once; no r-free chain can use a second seven-cell.

For one such chain let its unique seven-cell lie in the window of length u. That window has u≤13, since every 14 consecutive integers contain at least two seven-cells. Every other window has length≤6 and contributes neither a 7-divisible binomial nor a 7-divisible c|u!. For the distinguished factor (B,c), the exact product gives
\[
 v_7(N)=\begin{cases}
 v_7(r+h),&u\le6,\\
 v_7(r+h)-1+v_7(c),&7\le u\le13,
 \end{cases}
\]
because its numerator contains exactly one multiple of 7 and v7(u!)=1 in the second range. The P7 hypothesis requires v7(N)≥1, and at most one of all seven labels may have v7(N)≥2.

In the long-window range the actual small-block kernel L from the quotient proof satisfies c=(2/[H:K])[A_u:L]. Since v7(|A_u|)=1 and 2/[H:K] is 7-free, v7(c)=1 iff 7 does not divide |L|. In particular, when the seven-cell itself has valuation 1, a long local step **requires** a 7-free small-block kernel. The six numbers (r+h_i)/7 are consecutive, so at most one seven-cell can have valuation ≥2. Finally, the six distinguished windows are disjoint and their lengths sum to at most 41; at least one has length≤6, since six length-7 windows would require 42 cells.

## 3. A precise 7-local obstruction to count-only closure

For every prime r≡6 mod 49, the seven cells are 1,8,15,22,29,36 and all have valuation exactly 1. Take five disjoint windows [1,7],[8,14],[15,21],[22,28],[29,35], each with quotient c=7, and the short window [36,41] with c=1. In each length-7 binomial the unique numerator factor 7 is canceled by the one factor 7 in 7!, then c restores one; the short binomial contributes one directly. These six **local integers** therefore all have 7-valuation exactly 1 and their windows exactly occupy 41 cells.

The long quotient c=7 is not a fictitious small-block value: for any large block U, the preimage in B=(S_U×S_7)∩A_(U∪V) of the point stabilizer S6≤S7 has full alternating projection on U and [B:H]=7. Equivalently its even small-block kernel is A6≤A7 and the quotient formula gives c=7. This supplies a genuine **local** block-subgroup example, not six globally compatible subgroups of A_(r+41).

The local construction does not force pairwise gcd 7: it does not control primes other than 7 or realize the required transitive descents. For the selected r=251 integer control below, all 15 pairs of the six local values in fact have extra common factors. Thus the model is an obstruction only to a proof based on 7-cell counts and 7-valuations alone, not an actual P7 counterexample. Under the additionally imported prime number theorem in arithmetic progressions, π(x;49,6)∼x/(42 log x); the earlier O(√x log x) repunit-prime upper bound implies infinitely many eligible primes r≡6 mod49 beyond the size threshold. Fixed-r local statements do not require that analytic import.

## 4. Actual finite controls and exact gap

`frontier-20261028-alternating-saturated-seven-check.py`, SHA-256 `7bea97eb7487287079fa32ee5074e9ae227de834487d2b461b041c8e5e27202b`, 30 LF / 945 bytes, ran at 19:37:09 PDT on 2026-10-28. It checked exact 7-adic binomial valuations for every single-seven-cell window at t=41 for r=419,421,431. `frontier-20261028-alternating-local-model-check.py`, SHA `b7873325bbc9e4163a2d19b2b1de0df722b9b4d0750eccc00afc68c36c197621`, 32 LF / 1052 bytes, ran at 19:37:58 PDT; for r=251 below the theorem size bound it checked the six local valuations and found extra non-7 gcd factors in all 15 pairs. Neither program enumerates global subgroups or proves the universal source-dependent assertions.

**Unresolved:** establish a non-7 prime collision, a genuine cross-window/subgroup compatibility restriction, or another all-variable contradiction for the six saturated r-free labels; the unique r-divisible seventh label must also be accounted for. No direct P7 conclusion at t=41, historical novelty, formal proof or old-hold rehabilitation is claimed.
