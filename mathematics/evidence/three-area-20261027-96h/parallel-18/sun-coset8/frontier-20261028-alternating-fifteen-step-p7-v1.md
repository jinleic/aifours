# Fifteen-step alternating P7 exclusion for primes 7 mod 12

**Status: WRITTEN candidate, conditional on the named A_r theorem and earlier actual projection/window arguments; not independently reviewed or accepted.** Let r≥419 be a prime not of the form (q^d−1)/(q−1) for a prime power q and d≥2, with r≡7 mod 12 and r+1>7·15!. Then A_(r+15) has no seven proper subgroup indices whose pairwise gcds are all exactly 7. No assertion is made for the other residue classes at t=15, for unrestricted Sun8, for all alternating degrees, or for the global problem.

The fixed-r result imports the public subgroup theorem below. For infinitude only, additionally import the standard prime number theorem in arithmetic progressions π(x;12,7)∼x/(4 log x), e.g. https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The earlier elementary count bounds all excluded repunit primes by O(√x log x), so infinitely many eligible r lie in this progression. This analytic theorem is cited, not re-proved. No historical novelty or published-priority claim is made.

## 1. Source, projection and nonblind boundary

The public group input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, identifying the unique maximal Sylow-r overgroup in A_r. The actual alternating-block projection/product-divisibility lemma, the one-cell terminal classification and disjoint numerator windows are in `frontier-20261028-alternating-twelve-step-projection-p7-v1.md` SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`. Their application through t=15 follows the same decreasing-degree induction, now using 15! in the common-factor bound. These source and written proofs have not been independently reconstructed or formally verified here; no Sun7 is used.

The writer was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such snippet is used here and no historical hold is changed.

## 2. Eliminate factorial leaves and prepare the windows

Write n=r+15. If one P7 index is divisible by (r−2)!, the other six indices would be 7 times pairwise-coprime integers >1 whose prime factors lie in [r−1,r+15]. The only possible primes there are r and the seven odd candidates r+2,r+4,…,r+14. Since r≡1 mod 3, r+2,r+8,r+14 are composite multiples of 3; at most four other candidates and r remain, fewer than the six required. Thus no factorial-terminal chain can occur.

At least six of seven indices are r-free. Every nonfactorial chain uses at least two numerator-window cells, except possibly a top-degree point-stabilizer chain of index n. Any lower one-cell terminal would have index <n, impossible for a proper subgroup of A_n by the simple-group coset-action order bound. The point label is unique if present. Different labels' cells are disjoint because any shared factor r+h would leave (r+h)/gcd(r+h,15!)>7 dividing both indices. Cells within a chain are disjoint by decreasing degree.

Since all indices contain 7, at most one is even. For an odd-index label every window binomial is odd; each such window has at least as many even positions as odd positions. A label with exactly one even position and at least two cells is therefore one odd adjacent binomial window. Because r≡3 mod 4, the odd adjacent-window clusters are centered at 3,7,11,15; a cluster supports at most one disjoint edge. Every odd length-three binomial window is centered at one of these clusters and blocks it; every window of length at least four in positions 1,…,15 contains a cluster center.

## 3. No point label

Choose six r-free labels when none is the one-cell point label. Each uses at least two cells. There are seven even positions, so among at least five odd labels at most two can use more than one even position. Hence at least three odd adjacent windows occur. Six odd labels would require at least five adjacent windows, so there are exactly five odd labels and one even. There are either four adjacent labels and one multi-even odd label, or three adjacent labels and two multi-even odd labels.

If there are four adjacent labels, all four clusters 3,7,11,15 are occupied. The center-11 binomial contains (r+11)/2, divisible by 3 because r≡1 mod 3. The boundary center-15 edge is {14,15} and contains r+14, also divisible by 3. These distinct indices both contain 7, contradicting gcd 7.

Now suppose there are three adjacent labels and two multi-even odd labels. The three adjacent labels use one even position each, and each multi-even label uses at least two; consequently all seven even positions are used and each multi-even label has exactly two even positions. The three bad positions 2,8,14 have r+k divisible by 3. Each multi-even label uses at most five cells: the other multi-even label, three adjacent labels and the even label together use at least 2+6+2=10 of the 15 cells.

A bad position whose window has length 1 or 2 makes its label divisible by 3, since the corresponding numerator factor cannot lose 3 to the denominator. To avoid that, its window must have length at least 3. One multi-even label using at most five cells can neutralize at most one of 2,8,14: one window containing two of them has length at least 7, while two separate length-at-least-three windows need six cells.

- If center 15 is occupied, its boundary edge contributes a 3-divisible index through r+14. The remaining bad positions 2 and 8 must be neutralized in two distinct odd windows of length at least three. Each blocks an allowed cluster center; because the windows are disjoint, they block two different centers. Only two of the four clusters would remain for three adjacent labels, contradiction.
- If center 15 is unoccupied, the three adjacent centers are 3,7,11. Center 11 contributes a 3-divisible index through (r+11)/2 and has even neighbor 10 or 12, neither bad. Thus all three bad positions 2,8,14 must be neutralized by the two multi-even labels, but each can neutralize at most one. Contradiction.

## 4. With the point label

The point index n=r+15 is even, so it is the only even index. Select it and five other r-free labels; all five are odd and use at least two cells. They have seven even positions available, so at least three must be odd adjacent windows. Position 15 is occupied by the point window and blocks the center-15 cluster; only centers 3,7,11 remain. Hence exactly these three are occupied, and the other two odd labels each use exactly two even positions.

Those two multi-even labels cannot use an odd length-two window (it would be a fourth edge), an odd length-three window (it blocks a required cluster), or any length-four-or-longer window in the remaining positions 1,…,14 (it contains at least one of 3,7,11). Odd-position singleton windows are even. Therefore each multi-even label is exactly two even singletons. All seven even positions are occupied by odd labels, each contributing the full factor r+k. The bad positions 2,8,14 must all belong to one label to avoid two 3-divisible indices, but each label contains at most two even positions. Contradiction.

## 5. Actual finite controls and remaining scope

`frontier-20261028-alternating-fifteen-check.py`, SHA-256 `8177648d6679e420bf8177e554bc52c14883f3d7f8adf3c814be37cbae942991`, 98 LF / 3161 bytes, ran at 19:12:34 PDT on 2026-10-28. It checked four exact small eligible primes in the residue class (139,223,439,463), a necessary parity/3 no-point window relaxation for each, and the point case for the first two. These are explicitly **below** the theorem's size bound and are finite arithmetic controls, not source verification or subgroup enumeration.

**Review-critical:** verify the projection lemma for arbitrary t=15, exclusion of the factorial terminal, cell accounting in both cases, the bound of one neutralized bad position per multi-even label, and the distinct-cluster argument. The residue r≡3 mod 4 with r≡2 mod 3, and r≡1 mod 4, remain open for this packet. No historic hold is modified.
