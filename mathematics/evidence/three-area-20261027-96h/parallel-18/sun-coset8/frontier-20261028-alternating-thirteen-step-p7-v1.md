# Thirteen-step alternating P7 exclusion by projected-window packing

**Status: WRITTEN candidate, contingent on the public A_r theorem and the previously written projection/window lemmas; not independently reviewed or accepted.** Let r≥419 be prime, not a prime-power repunit (q^d−1)/(q−1) for any prime power q and d≥2, and assume r+1>7·13!. Then A_(r+13) has no seven proper subgroups with pairwise index gcd exactly 7. Together with the prior t≤12 work, the same sufficient bound excludes direct P7 in each of A_(r+1),…,A_(r+13). The earlier elementary count of eligible primes makes the family unbounded. No publication-priority, historical-novelty, unrestricted Sun8 or global all-simple-group conclusion is claimed.

## 1. Dependencies and the additional step

The public source is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: eligible r gives the unique maximal Sylow-r overgroup AGL1(r)∩A_r in A_r. The index-divisibility base, actual orbit descent, denominator/window overlap and eligible-prime count are in `frontier-20261028-alternating-interval-packing-p7-v1.md` SHA `cc6aa191d75c2658a6f93e92468d6ac9aab178c1cfc54effa3c0e50e1cc11e4f`. The actual alternating-block projection, full-projection terminal and factorial-terminal arguments are in `frontier-20261028-alternating-twelve-step-projection-p7-v1.md` SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`. Those are unreviewed written inputs, not a source-proof replay or formal verification. The source classification and standard alternating-group facts are imports; no Sun7 is used.

The writer was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such excerpt is used here and no historical hold is changed.

## 2. Factorial leaves and actual windows

At most one of seven P7 indices is divisible by r>7, so choose six r-free labels. Apply the earlier actual block-projection descent to each. Every chain terminates either in a full alternating large-block projection or in a proper subgroup of A_r, the latter forcing divisibility by F=(r−2)!.

The factorial case is impossible in a seven-pattern. If F divides one index, each of the other six indices is 7 times a number >1 with no prime factor ≤r−2; the six cofactors are pairwise coprime. Prime factors of |A_(r+13)| in [r−1,r+13] can only be r or primes among r+2,r+4,r+6,r+8,r+10,r+12: r−1 and r+odd are even. Two of those six odd candidates are divisible by 3, so there are at most five possible primes, insufficient for six coprime cofactors.

With no factorial chain, a chain uses at least two numerator-window cells, except possibly a single-cell point-stabilizer chain at the **top** degree, whose index is n=r+13 and which requires 7|n. To justify the exception, a one-cell full-projection terminal must have u=1, so its index at the terminating degree is r+j. All prior descents are transitive and preserve index. A proper subgroup of A_n has index≥n (otherwise its core-free coset action would embed A_n in S_(n−1)); hence j=13. There can be at most one point label because two identical indices n>7 would not have gcd 7.

All cells in a chain are distinct, and cells from distinct labels are disjoint: a shared cell h gives common divisor (r+h)/gcd(r+h,13!)>7. Every odd-index label has every associated binomial odd. Such a window has at least as many even positions as odd positions: at an even endpoint this follows from alternating positions, while at an odd endpoint r+j is even and an odd binomial has even length. An odd label using exactly one even position and at least two cells is therefore exactly one odd length-two adjacent window.

For an adjacent length-two window with odd position c and one neighboring even position, the binomial is odd iff r+c≡2 mod 4. Thus allowed edges occur in disjoint clusters centered at c=1,5,9,13 when r≡1 mod 4, and c=3,7,11 when r≡3 mod 4. A cluster contributes at most one disjoint edge. The previous t=12 packet also proves the following useful observation: an odd length-three window ending at an even position has a center belonging to one of these allowed clusters and occupies that center and both neighbors; consequently it blocks the entire cluster.

## 3. No point-stabilizer label

Choose six r-free labels. If none is the one-cell point label, each uses at least two disjoint cells in {1,…,13}, so there is at most one spare cell. At least five labels are odd, since all indices are divisible by 7 and at most one can also be even. Each odd label uses at least one of the six even positions. At most one such label can use two or more even positions; otherwise five labels would require at least seven.

If six labels are odd, all use exactly one even position and therefore require six allowed adjacent edges, impossible. Hence exactly five are odd and one is even. At least four odd labels use exactly one even position, so they give four allowed edges. This already rules out r≡3 mod 4, which has only three edge clusters. For r≡1 mod 4 the four centers 1,5,9,13 must all be used, and the remaining odd label uses exactly two even positions and at most three cells.

That remaining label cannot consist of an allowed adjacent window plus a singleton: it would give five allowed disjoint edges. It cannot be one odd length-three window, because it would block one of the four clusters needed by the other four edges. Three singleton windows cannot give an odd label using exactly two even positions, as the odd-position singleton contributes an even factor. Thus it is exactly two singleton windows at two even positions. Every even position 2,4,6,8,10,12 is now occupied either by this double-singleton label or by an allowed adjacent label, and each such label's index is divisible by r+k for the even position k it uses.

If r≡1 mod 3, the two 3-divisible positions are 2 and 8; if r≡2 mod 3, they are 4 and 10. They must belong to the **same** label, because all indices also contain 7. An adjacent label contains only one even position, so the double-singleton label must occupy the bad pair. In the first residue case it uses position 2, blocking the compulsory center-1 edge {1,2}. In the second it uses 4 and 10; the compulsory edge {1,2} has index divisible by C(r+2,2), which contains (r+1)/2 divisible by 3. It therefore collides with the double label through 3·7. Both cases are impossible.

## 4. With the point-stabilizer label

The point index r+13 is even, so it is the only even index. Select it and five other r-free labels; all five other labels are odd and use at least two cells. The point window occupies position 13, leaving the six even positions 2,4,6,8,10,12. At most one of the five odd labels can use more than one even position, so at least four require disjoint allowed adjacent windows.

If r≡3 mod 4 there are only three allowed clusters. If r≡1 mod 4 there would be four, but position 13 is already occupied by the point label and blocks the entire center-13 cluster. Again at most three remain. This contradiction completes the t=13 proof.

## 5. Actual exact controls and review boundary

`frontier-20261028-alternating-thirteen-check.py`, SHA-256 `f2f1c3a69ed8a479c1cd35a4c41dd14017e5a6325a950ba00fdc593599558a3a`, 103 LF / 3331 bytes, ran at 19:05:21 PDT on 2026-10-28. It found four eligible primes above 7·13!, one for each combination of r mod 4 and mod 3 with 7|(r+13), and checked exact finite no-point 2/3-cell packings under the necessary parity/3 conditions, together with the point case's bound of at most three odd adjacent edges. These are selected arithmetic relaxations, not subgroup enumeration, proof of the general argument, or independent source verification.

**Review-critical:** rederive the alternating-block projection lemma and factorial-terminal prime bound for t=13; verify the one-cell terminal, the even-position accounting, the allowed-edge cluster obstruction to length-three windows, the mod-3 bad-position grouping and the point-label case. All prior holds and frozen packets remain unchanged.
