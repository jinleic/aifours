# Jordan's large prime cycle with the P7-specific exact gcd

**Status: WRITTEN candidate, conditional on the public Jordan theorem and earlier written subgroup reduction; not independently reviewed, formally verified or accepted.** Let r>7 be prime, 3≤t<r, n=r+t and D*=n/gcd(n,lcm(1,…,t)). If D* does not divide 7, then A_n has no three proper subgroup indices with pairwise gcd exactly 7; hence direct P7 is excluded. This strictly enlarges the earlier D*>7 family, but does not claim that D*≤7 gives the stronger no-three-gcd≤7 statement, that D*=1 or 7 is settled, or that all alternating degrees are covered.

For D*>7 the previous Jordan result also gives Sun8 without Sun7. When D*≤7 and D*∤7, the Sun8 consequence additionally needs the separately named internally accepted written Sun7 and prior R8 interfaces; it is not asserted as a source-free extension.

## 1. Inputs and prospective-only source boundary

Jordan's classical prime-cycle theorem is stated as Theorem 1.1 of https://arxiv.org/html/1209.5169v1: a primitive group containing a prime cycle fixing at least three points contains A_n. The actual block argument showing every r-free proper H<A_n is intransitive, and the set-stabilizer divisor, are in `frontier-20261028-alternating-jordan-exact-gcd-v1.md` SHA `342df14ff23575c98bf368fcc85d7f9b68db494e36b64f773e467f3c1d9e5829`. The public proof and the prior candidate remain unreviewed inputs, not formal verification or a novelty finding.

Before any prior alternating body, read the mandatory arithmetic correction `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`. This prospective packet does not retroactively add Jordan to f116, held history or the earlier integer model. The writer was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is used.

For the **optional** Sun8 composition at small D*, the exact prior written imports are the Sun7 parent verdict SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2` and R8 source SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`, with their mandatory overlays. No proof-DAG replay, human/formal verification or new R8 credit is claimed.

## 2. P7-specific consequence

The previous Jordan reduction makes every r-free proper-subgroup index divisible by D*. In any three indices whose pairwise gcd is exactly 7, all three are divisible by 7 and at most one is divisible by r>7. Two r-free indices therefore share lcm(7,D*), which is greater than 7 exactly when D*∤7. This contradicts gcd 7 and excludes the stated three-index pattern and direct P7.

When D*>7, the earlier result excludes any three indices with pairwise gcd≤7 and thus gives Sun8 without a Sun7 assumption. When D*∈{2,3,4,5,6}, this new proof excludes only gcd-exactly-7 triples; Sun8 then follows only under the additional S7/R8 import above. For D*=1 or 7 it gives no conclusion.

## 3. Exact finite controls

For A32 take r=19,t=13: D*=4 while n/gcd(n,t!)=1. For A36 take r=29,t=7: D*=3 while the factorial-based divisor is 1. In each case D*∤7, so the direct-P7 conclusion applies under Jordan even though neither earlier D*>7 nor the factorial criterion applies. This is not a claim that a subgroup of index 3 or 4 exists.

`frontier-20261028-alternating-jordan-p7-check.py`, SHA-256 `d4eb34a7c8be5178e1f909e78d37a0bc3ed7b98e5d3c84533456724707f2f6fc`, 14 LF / 622 bytes, ran at 20:13:34 PDT on 2026-10-28. It checked exact primality, binomial divisibility and the two stated D* values for these two cases only. It does not verify Jordan, the subgroup reduction, S7/R8, or an all-degree result.

**Review-critical:** reconstruct the earlier Jordan/set-stabilizer reasoning, lcm(7,D*) collision, actual P7 versus Sun8 conditionality, and prior-source overlay order. No historical hold, source proof or verdict is modified.
