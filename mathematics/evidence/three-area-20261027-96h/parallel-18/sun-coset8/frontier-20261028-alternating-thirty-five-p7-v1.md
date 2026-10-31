# Seven-cell alternating P7 exclusion through 35 positions

**Status: WRITTEN successor candidate, conditional on the cited public classification and previous written quotient argument; not independently reviewed or accepted.** Let r≥419 be a prime not of the form (q^d−1)/(q−1) for any prime power q and d≥2. For every 1≤t≤35 satisfying r+1>7t!, the actual finite simple group A_(r+t) has no seven proper subgroup indices whose pairwise gcds are all exactly 7. Eligible primes have relative density one among primes by the earlier elementary count, so each fixed t gives an unbounded family. No historical novelty, priority, unrestricted Sun8 or global conclusion is claimed.

This extends `frontier-20261028-alternating-seven-cell-p7-v1.md` SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f` from 33 to 35. That earlier written proof imports Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2 and derives the exact alternating-block quotient and 7-cell necessity. None of those inputs has been independently reviewed or formally verified; no Sun7 is assumed. The writer was nonblind and the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is used.

## 1. Extend the factorial-terminal bound

For t≤33 the source-conditional factorial exclusion is given in `frontier-20261028-alternating-factorial-terminal-33-v1.md` SHA `363205fefd1b34bde523523e87f9c981a0a45409f006c53391a46c4e29384186`. For t=34 or 35 there are 17 odd candidates r+2,r+4,…,r+34 for primes in [r−1,r+t], in addition to r. Since r>3 is prime, exactly six of the 17 are composite multiples of 3: offsets 2,8,14,20,26,32 when r≡1 mod 3, and 4,10,16,22,28,34 when r≡2.

According as r≡1,2,3,4 mod 5, the offsets 4,14,24; 8,18,28; 2,12,22; or 6,16,26 are all composite multiples of 5. The three members of each list have different residues mod 3, so at least two are additional to the six above. At most 17−6−2=9 of the odd candidates, plus r, can be prime: at most ten in total. All stated multiples exceed 5.

If a P7 index were divisible by (r−2)!, the other six would be 7 times nontrivial pairwise-coprime squarefree cofactors supported on those at most ten primes. At least two cofactor supports would be singletons, and at most one of these primes would be r. Thus some actual subgroup index would be 7p with r<p≤r+t. The earlier no-7p argument applies verbatim: after transitive fixed-point descents, an intransitive set-stabilizer binomial with complement size≥2 is at least C(r+1,2)>7(r+35)≥7p, while complement size 1 forces an impossible index-7 subgroup of A_(p−1). An all-transitive descent forces (r−2)!>7(r+35) into 7p. Both inequalities hold for all r≥419. Hence no factorial-terminal P7 index exists for t≤35.

## 2. Consume distinct seven-cells

For every r-free P7 index, the prior exact quotient formula yields a finite chain product of binomials C(r+j,u) and quotient factors c|u!, terminating in a full alternating-block projection: a proper A_r terminal would put (r−2)! into the index, just excluded. If a chain used no position h with 7|(r+h), every window would have length at most 6, its binomial and its quotient c|u! would both be 7-free, and so would the entire index. This contradicts the actual common gcd 7. Thus every r-free label consumes at least one such seven-cell.

Windows belonging to different labels cannot share a cell h, since then (r+h)/gcd(r+h,t!)>(r+1)/t!>7 divides both indices. At least six of the seven indices are r-free, while any 35 consecutive positions contain at most five seven-cells. Contradiction. This covers t=34,35 as well as the earlier t≤33 and does not import the older finite residue certificates as theorem inputs.

## 3. Actual control and review boundary

`frontier-20261028-alternating-thirty-five-check.py`, SHA-256 `5975e0b492c895adf84f101c513479018cebc70d5381d619a96dcc240b5e2ded`, 30 LF / 1094 bytes, ran at 19:30:02 PDT on 2026-10-28. It checked the 3/5 possible-prime upper bound for all eight residues coprime to 15 and t≤35, the needed inequalities at r=419, and the seven-cell/window implication for r=419,421,431. These are finite integer controls, not actual subgroup enumeration, source replay, or proof of the universal theorem.

**Review-critical:** audit the E=17 sieve, no-7p actual-subgroup lemma, exact c|u! quotient iteration and the five-seven-cell pigeonhole; separately verify the public A_r theorem and prime-density ancestor. Frozen predecessors and all historical holds remain unchanged.
