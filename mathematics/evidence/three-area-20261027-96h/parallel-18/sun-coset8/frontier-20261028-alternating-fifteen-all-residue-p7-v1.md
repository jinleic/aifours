# Fifteen-step alternating P7 exclusion: 480-class exact integer certificate

**Status: WRITTEN + one finite Python exact-integer exhaustive check, conditional on the public A_r theorem and earlier written projection lemma; not independently reviewed, formally verified, accepted or priority-cleared.** Let r≥419 be a prime, not a prime-power repunit (q^d−1)/(q−1), d≥2, and suppose r+1>7·15!. Then A_(r+15) has no seven proper subgroup indices whose pairwise gcds are all exactly 7. This removes the r≡7 mod 12 restriction in `frontier-20261028-alternating-fifteen-step-p7-v1.md`, SHA `a42675bc032a4d5ca577f9eb86ac8a652bcf2b6049f2860624e84eb24b506a6e`. Combining the earlier packets gives direct-P7 exclusion for A_(r+1),…,A_(r+15) under this common sufficient size bound. The earlier elementary count gives infinitely many eligible primes. No unrestricted Sun8, all-alternating or global verdict, published priority or historical novelty is claimed.

## 1. Named sources and provenance

The public group input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, giving the unique maximal Sylow-r overgroup in A_r for eligible r. The actual alternating-block projection, product divisibility, terminal structure and disjoint numerator windows are in `frontier-20261028-alternating-twelve-step-projection-p7-v1.md`, SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`, with base and prime-density ancestors named there. Their correctness and the public theorem remain unreviewed inputs. Standard alternating-group simplicity/order, Sylow and orbit-stabilizer are also used. No Sun7 or arithmetic-progression prime theorem is needed for the fixed-r result or its stated infinitude.

The writer was nonblind; the incidental cross-topic display is documented in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such excerpt is used and no historic hold is modified.

## 2. Necessary group-theoretic reduction

Assume seven proper-subgroup indices in A_(r+15) have pairwise gcd 7. At most one is divisible by r>7, so at least six are r-free. Follow the actual projection chains of the cited written lemma.

No chain can end at a proper subgroup of A_r. Such a terminal makes its index divisible by F=(r−2)!, so the six other indices would be 7 times pairwise-coprime integers >1 whose prime factors lie in [r−1,r+15]. Apart from r, only the seven odd candidates r+2,r+4,…,r+14 can be prime. If r≡1 mod 3, offsets 2,8,14 are composite. If r≡2 mod 3, offsets 4,10 are composite, and a distinct candidate is divisible by 5: offsets 14,8,2,6 respectively for r≡1,2,3,4 mod 5. Thus at most four candidate primes plus r remain, fewer than six.

Every nonfactorial chain uses at least two numerator cells except possibly the top point-stabilizer with one cell and index r+15. A lower one-cell terminal would be an index less than r+15, impossible for a proper subgroup of A_(r+15). The top point label, if present, is unique because r+15>7. It is even, and is not divisible by 3 or 5 since r is a prime greater than 5 and 15 is divisible by both.

Different labels' cells are disjoint: a shared factor r+h would give common divisor (r+h)/gcd(r+h,15!)>7. Cells within each label are disjoint by strictly decreasing degree in the projection chain. Every index contains 7, so at most one can also contain each of 2,3,5. We use only these necessary conditions and intentionally ignore all further subgroup/gcd constraints.

- **No point label:** choose any six r-free labels, each using at least two cells among 1,…,15. Each uses at most five cells, since the other five require ten.
- **Point label present:** choose it and five other r-free labels. Cell 15 is unavailable; each other label uses at least two of cells 1,…,14 and at most six. The point already consumes the unique possible 2-divisible-index flag. We do not require 7|(r+15) in the finite relaxation, so this branch is deliberately overinclusive.

Each actual group of cells decomposes into contiguous binomial windows, with factor C(r+b,ℓ) for interval [b−ℓ+1,b]. Products of those extracted factors divide the actual index by the projection lemma. The finite search below permits **every** disjoint interval decomposition, including many that need not be realizable by a subgroup.

## 3. Exact modulus and finite recurrence

All relevant interval lengths satisfy ℓ≤6. In characteristic p, (1+X)^(p^e)=1+X^(p^e). The powers 8,9,25 are respectively greater than 6 for p=2,3,5; hence C(r+b,ℓ) mod p depends only on r mod that power. The lcm is 1800, and every r prime>5 lies in one of the 480 residues a, 1≤a<1800 with gcd(a,30)=1. The checker may use 1800+a as a representative without changing any of the relevant 2/3/5 flags.

An option is any 2–6 cell subset split into contiguous intervals, carrying a bitmask for divisibility of the binomial product by 2,3,5. Identical (cell mask, flag mask) options can be deduplicated. The recurrence on available mask M, remaining label count k and used prime flags either skips the smallest available cell or chooses any compatible option whose smallest cell is that cell; k=0 succeeds, and |M|<2k fails. The skip is considered only when enough cells remain. This is an exhaustive search of a **relaxation** of actual subgroup chains.

`frontier-20261028-alternating-fifteen-residue-certificate.py`, SHA-256 `ed18d17e65662f99d87e1edb207d964c8fbc18a44b8c3a017273c89388cbc599`, 89 LF / 3191 bytes, implements the recurrence. One bounded Python 3 run completed at 19:20:17 PDT on 2026-10-28. For all **480** residue classes it returned no six-group no-point witness and no five-group point witness, with 7,048,936 and 387,076 memoized states respectively; reported wall time was 116.32 seconds. The point branch removes cell 15 and begins with the 2-divisibility flag set; it also overcounts residues where a point label would not in fact be 7-divisible. Execution receipt: `frontier-20261028-alternating-fifteen-residue-receipt-v1.json`, SHA `47cb9f7fd2d928ff555224f183b24493b3cc039b48dcba71bd82ca4da7870bcd`.

Any actual seven-pattern would yield one of the two finite-search witnesses, contrary to that run. The result is therefore a source- and checker-conditional **written/computer-assisted candidate**, not a Lean/kernel proof, actual subgroup enumeration, independent replay, external-model review, human proof verification, or novelty finding.

## 4. Review obligations

Independently reconstruct the actual projection/product and factorial/point-terminal reductions, check the mod-1800 coefficient argument, audit all decompositions and the skip recurrence for false negatives, and independently replay or replace both 480-class searches. Check the public source theorem and elementary prime-density proof separately. The 116.32-second check was one run only; no cross-review or historical-hold rehabilitation is implied.
