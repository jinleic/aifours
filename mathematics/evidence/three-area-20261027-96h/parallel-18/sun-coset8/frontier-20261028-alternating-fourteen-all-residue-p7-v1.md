# Fourteen-step alternating P7 exclusion: 96-class exact integer certificate

**Status: WRITTEN + finite Python exact-integer exhaustive check, conditional on the public A_r theorem and the earlier written projection lemma; not independently reviewed, formally verified, accepted, or priority-cleared.** Let r≥419 be a prime, not a prime-power repunit (q^d−1)/(q−1), d≥2, and assume r+1>7·14!. Then A_(r+14) has no seven proper subgroup indices with every pairwise gcd exactly 7. This removes the r≡3 mod 4 restriction from `frontier-20261028-alternating-fourteen-step-p7-v1.md`, SHA `68320a70adff5badb1e1889e0b8244f334fc2469d9c26afc596557b48e562fa0`. The earlier elementary count gives infinitely many eligible primes. No unrestricted Sun8, all-alternating, global target, published priority or historical-novelty claim is made.

## 1. Group and source boundary

The only non-elementary group input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, giving the unique Sylow-r maximal overgroup in A_r. The actual alternating-block projection, factor-product divisibility, one-cell terminal and disjoint numerator windows are in the unreviewed written packet `frontier-20261028-alternating-twelve-step-projection-p7-v1.md`, SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`, and its named ancestors. Standard alternating-group order/simplicity, Sylow and orbit-stabilizer are used. The source proof DAG and these written arguments have not been independently reconstructed here.

The writer was nonblind. The incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such excerpt is used here, and no historical hold is rehabilitated.

## 2. Necessity of six small window groups

Suppose seven proper-subgroup indices in A_(r+14) have pairwise gcd 7. At most one is divisible by r, leaving at least six r-free labels. Follow the actual projection/descent chains of the named written lemma.

No chain can end at a proper subgroup of A_r. Such a terminal would make its index divisible by F=(r−2)!. The other six indices would be 7 times pairwise-coprime integers >1 whose prime factors lie in [r−1,r+14]. Apart from r, only r+2,r+4,…,r+14 can be prime. If r≡1 mod 3, offsets 2,8,14 are composite. If r≡2 mod 3, offsets 4,10 are composite, and one different offset is a multiple of 5: respectively 14,8,2,6 for r≡1,2,3,4 mod 5. Thus at most four candidates plus r remain, fewer than six.

A nonfactorial chain with only one numerator cell would be the top point-stabilizer, of index r+14; 7 does not divide this number since r≠7. A lower point terminal would have index less than the minimum possible index r+14 in A_(r+14). Therefore choose six r-free labels each consuming at least two cells.

Cells of different labels cannot overlap: a shared numerator r+h gives common divisor (r+h)/gcd(r+h,14!)>7. Cells within each label are disjoint by the projection chain's decreasing degree. Six labels use at least 12 of 14 cells, so each label uses between 2 and 4 cells. Its actual binomial windows form some decomposition of those cells into disjoint contiguous intervals; transitive descents may skip cells. Every index is divisible by 7, so **at most one** index can also be divisible by each of 2,3,5. These are necessary conditions only; we deliberately discard all other subgroup and gcd constraints.

## 3. Why only 96 residues are needed

For a window interval [a,b] with length ℓ≤4, the extracted binomial factor is C(r+b,ℓ). For p=2,3,5 choose p-powers 8,9,5 respectively, all strictly larger than ℓ. Over F_p,
\[(1+X)^{p^e}=1+X^{p^e}.\]
Thus changing r by a multiple of p^e leaves the coefficient of X^ℓ, and hence C(r+b,ℓ) mod p, unchanged. It follows that **all** 2/3/5 divisibility flags of every possible interval product depend only on r mod lcm(8,9,5)=360. Since r is a prime greater than 5, its residue is one of the 96 a with 1≤a<360 and gcd(a,30)=1. Replacing r by 360+a for the finite check is therefore exact for these flags; it is not a replacement for the actual group.

## 4. Exhaustive necessary-condition recurrence

For one residue, an *option* consists of a subset S⊆{1,…,14} of size 2, 3 or 4, split into contiguous intervals, with flag set P⊆{2,3,5} indicating which primes divide the product of its interval binomials. The checker generates every such option: take the smallest cell in S, choose every possible contiguous initial interval, and recursively decompose the remaining cells. Deduplicating options with identical (S,P) cannot remove a relevant possibility because the following relaxation uses only those two data.

Let T(M,k,P) mean that k further options can be placed using available-cell mask M without repeating a prime already in P. T is true at k=0 and false when |M|<2k. Otherwise let h be the least available cell. Either h is unused (possible only if |M|>2k), or the unique selected option containing h has least cell h; recurse after removing its cells, provided its flag set is disjoint from P. This covers every configuration, while allowing many options that no actual subgroup could realize.

`frontier-20261028-alternating-fourteen-residue-certificate.py`, SHA-256 `11d4208774b4406dee3f48e0d5f2499de918945e7f2ae872ca3584925e878991`, 67 LF / 2406 bytes, implements that integer recurrence. One bounded Python 3 run completed at 19:15:35 PDT on 2026-10-28: **all 96 residue classes returned no six-option witness**, with 287,166 memoized search states in total. The execution/status receipt is `frontier-20261028-alternating-fourteen-residue-receipt-v1.json`, SHA `cdc7891c8d12b87a3d189a16b14d0a7369a10378470c3841aa1cacb9fb233bbe`. The original stdout reported one PASS/state count per class; this is one checker run, not an independent replay.

If seven actual indices existed, their six selected r-free labels would instantiate six disjoint options with no repeated 2/3/5 flag, contradicting the exact finite result. This establishes the stated all-r candidate **conditional on correctness of the public theorem, earlier projection argument, finite checker and the written reduction above**. It is not a Lean/kernel proof, external-model review, human proof verification, or subgroup enumeration.

## 5. Review obligations

Reconstruct the factorial/point-terminal exclusion and actual product windows, verify the modulus-360 polynomial argument, audit the option decomposition/skip recurrence for false negatives, and independently replay or replace the 96-case computation. Check the parent source classification and prime-density proof separately. No old held result is inferred accepted and no frozen predecessor is edited.
