# Fourteen-step alternating P7 exclusion in one residue class

**Status: WRITTEN candidate, conditional on the stated public A_r theorem and earlier written projection/window lemmas; not independently reviewed or accepted.** Let r≥419 be a prime, not a prime-power repunit (q^d−1)/(q−1), d≥2, with r≡3 mod 4 and r+1>7·14!. Then A_(r+14) has no seven proper subgroup indices whose pairwise gcds are all exactly 7. This does not cover r≡1 mod 4, unrestricted Sun8, all alternating degrees, or the global target.

For the statement that the eligible residue class contains infinitely many primes, we additionally name the classical prime number theorem in arithmetic progressions, π(x;4,3)∼x/(2 log x), e.g. https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The earlier written count shows only O(√x log x) primes up to x are excluded repunits. The fixed-r group argument does not require the analytic theorem. No priority or historical novelty is claimed.

## 1. Named dependencies

Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2 gives the unique maximal Sylow-r overgroup AGL1(r)∩A_r for the stated eligible primes. The base, actual orbit/window descent and alternating-block projection are frozen in `frontier-20261028-alternating-interval-packing-p7-v1.md` SHA `cc6aa191d75c2658a6f93e92468d6ac9aab178c1cfc54effa3c0e50e1cc11e4f` and `frontier-20261028-alternating-twelve-step-projection-p7-v1.md` SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`. Those are unreviewed written inputs, not source-proof replay, human or formal verification. No Sun7 is used.

Writer exposure was nonblind, including the incidental cross-topic display recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No content of those excerpts is used and no historical hold is changed.

## 2. No factorial terminal and no one-cell terminal

Suppose seven proper subgroup indices in A_(r+14) have pairwise gcd 7. At most one is divisible by r, so choose six r-free labels and follow the actual projection chains from the cited written lemma.

A chain ending in a proper subgroup of A_r makes the original index divisible by F=(r−2)!. If this happened, the other six indices would each be 7 times a number >1, pairwise coprime and with all prime factors at least r−1. But among primes in [r−1,r+14], only r and the seven odd candidates r+2,r+4,…,r+14 can occur. At least three candidates are composite:

- if r≡1 mod 3, r+2,r+8,r+14 are divisible by 3;
- if r≡2 mod 3, r+4,r+10 are divisible by 3, and at least one **different** candidate is divisible by 5: r+14 when r≡1 mod 5, r+8 when r≡2, r+2 or r+12 when r≡3, and r+6 when r≡4.

All these multiples exceed 5. Thus there are at most four candidate primes beyond r, and at most five primes in total, insufficient for six pairwise-coprime cofactors. The factorial terminal is impossible.

Any nonfactorial one-cell terminal must be the point-stabilizer index r+14: a terminal at lower degree would give a proper A_(r+14) subgroup of index <r+14, impossible by the faithful coset-action order bound. But 7∤(r+14), since r≠7. It therefore cannot occur in a P7 pattern. All six r-free chains consume at least two numerator cells each. Cells are disjoint across different labels by the factor (r+h)/gcd(r+h,14!)>7 and within a chain by decreasing degree.

## 3. Odd windows force three adjacent clusters

There are seven even positions 2,4,…,14 and seven odd positions. At most one of the six indices is even, since each also has a factor 7. Every odd label has each extracted binomial odd and uses at least as many even positions as odd positions. In particular an odd label with exactly one even position and at least two cells is one odd adjacent window.

For r≡3 mod 4, an adjacent binomial window is odd exactly when its odd center is 3,7 or 11. Each cluster contributes at most one disjoint adjacent window. Among five or more odd labels and seven even positions, at most two labels can use two or more even positions. Thus at least three odd labels use one even position and give adjacent windows. There cannot be six odd labels, because then at least five would require adjacent windows. Therefore precisely five labels are odd and one even; exactly three odd labels are adjacent, and the remaining two odd labels each use exactly two even positions. All seven even positions are consumed by the odd labels.

The total number of cells is at least 3·2+2·2+2=12, so each of the two multi-even labels uses at most four cells. It cannot contain a length-two odd window, which would be a fourth odd adjacent window. An odd length-three binomial window is centered at an allowed cluster and blocks that cluster, while the three adjacent labels need all three clusters. Any length-four window in positions 1,…,14 contains at least one of the centers 3,7,11 and likewise blocks a required cluster. An odd-position singleton would contribute an even factor. Hence each multi-even label is exactly two singleton windows at even positions.

For an odd adjacent window centered at c∈{3,7,11}, division by 2 removes a factor from the even numerator r+c, so its index is divisible by r+k at its unique even position k. The double-singleton labels have the same property for both their even positions. Thus each even position k=2,4,…,14 belongs to an odd label whose index is divisible by r+k.

## 4. The unavoidable factor 3

If r≡1 mod 3, positions 2,8,14 have r+k divisible by 3. They would all have to occur in one index to avoid two indices with gcd≥21, but each odd label contains at most two even positions. Contradiction.

If r≡2 mod 3, positions 4 and 10 have r+k divisible by 3 and must belong to the same label, necessarily one of the double-singleton labels. In addition, all three odd-edge clusters are occupied, including center 7. That adjacent binomial has factor (r+7)/2, which is divisible by 3; its index is a **different** label from the double-singleton label. Both are divisible by 7, so their gcd is at least 21, contradiction. This excludes the seven-index P7 pattern.

## 5. Actual finite control and boundary

`frontier-20261028-alternating-fourteen-check.py`, SHA-256 `3c936eb17bba59efe891052752dad2893839ae649eeac8fe663563d3c9ed64d4`, 94 LF / 2729 bytes, ran at 19:08:50 PDT on 2026-10-28. It found eligible r above 7·14! in both r mod 3 classes with r≡3 mod 4 and checked exact finite 2/3-divisibility no-point window relaxations. It did not enumerate subgroups, verify the source theorem, or establish the general collision proof.

**Review-critical:** rederive the mod-5 extra composite in the factorial case; verify no point terminal and the complete odd multi-window alternatives through four cells; check the center-7 collision and all source/prime-distribution qualifications. The r≡1 mod 4 branch is intentionally not claimed, and all historical holds remain unchanged.
