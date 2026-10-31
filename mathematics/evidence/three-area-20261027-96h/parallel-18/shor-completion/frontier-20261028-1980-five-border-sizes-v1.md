# Shor completion: five remaining border sizes at order 1980

Owner **MathShor-2**, math-5. Native `/bin/date` after the exact checks: **Wed Oct 28 19:49:40 PDT 2026**.
**Conditional candidate reduction with exact finite checks; order1980 and the original all-order completion problem remain OPEN. No formal/peer/cross-family review or novelty clearance is claimed.**

## 1. Result and complete cardinality sieve

For any hypothetical finite UD factor-complete extension of the literal Shor code with actual pure-a order1980, the classical same-D direct border factorization has old anchors `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`. The earlier independently written anchor argument gives `|P|>=7`; the old-anchor gcd screen gives exactly158 P-candidates. Cardinality divisibility therefore initially gives the20 possibilities

    {9,10,11,12,15,18,20,22,30,33,36,44,45,55,60,66,90,99,110,132}.

Primes5 and11 divide1980 only once. When either divides |P|, P is uniform modulo that prime. The candidate screen has only8 heads in mod5 class2 and8 in mod11 class1, so it eliminates every 5-divisible size above40 and every 11-divisible size above88. Size11 is impossible because0,11 already occupy a mod11 class of capacity1. This leaves

    {9,10,12,15,18,20,22,30,33,36,44,66}.                   (1)

The separately pinned P12, P15 and P36 packets exclude those three sizes. The exact checks and simple arguments below exclude9,10,20,44. Thus the remaining necessary sizes are

    |P| in {18,22,30,33,66}.                                  (2)

None of (2) is asserted feasible. This reduction is independent of the unreviewed candidate `n>=1980` floor.

## 2. Size9: a 17-pair tail matching

If |P|=9, |Q|=220 and Q is uniform modulo11, with20 tails in each of classes1 and2. The old-anchor Q screen has56 candidates in the union of these two classes. The pinned checker exhibits17 disjoint pairs among them, each with gcd-difference in the old head classes `{3,4,5,11}`. Q can take at most one member of each pair, hence at most `56-17=39` from the union, fewer than the required40.

## 3. Size10: two relaxed tail quotas

If |P|=10, |Q|=198. Since P is coprime to3 and11, Q is uniform modulo9 and modulo11. Retain only old-anchor-compatible Q candidates in class8 mod9 or class0 mod11: there are56. The actual old anchor0 is retained; the required quotas are22 and18 respectively. Under old-head gcd exclusions `{3,4,5,11}`, exhaustive bitset include/exclude search reports UNSAT (55 nodes,28 quota prunes); a separate set-based search with another branch ordering reports UNSAT (61 nodes,31 prunes). The producer checks a literal40-residue witness to the same two quotas after only gcd4 is removed; it has gcd4 collisions and is not a tiling. No solver timeout is used as evidence.

## 4. Size20: overlapping residue capacities

If |P|=20, Q has odd size99, forcing P uniform modulo4 with5 heads in class2. P is also uniform modulo5 with4 heads in class3. The old heads3 and8 already consume two places in that mod5 class, and neither is2 modulo4. The screened mod4 class2 has exactly11 candidates; only1070 and1746 lie outside mod5 class3. At most2 of the five could occupy mod5 class3, and at most2 can lie outside it: impossible.

## 5. Size44: a forced old-tail conflict

If |P|=44, Q has odd size45, so P is uniform modulo4 with11 heads in class1. The old-anchor screen has exactly11 such candidates, all forced; among them33 and921 have difference gcd12. This matches the gcd12 difference of the old Q-tails1 and13, contradicting Sands.

## 6. Pins and scope

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1980-cardinality-screen.py` | f53b7caef690926bea0e08b520cc408668241abd4b34ac36ffba32bff5d45c8e | 16 / 887 |
| `frontier-20261028-1980-small-branches-check.py` | eee341e9e34a6fd928491e1f3f0bb480c7f33b466b8a912caabb1c76cbbb6a83 | 62 / 3466 |
| `frontier-20261028-1980-p10-quota-replay.py` | 93cf38e0d69bba53979b847971aa14fc64974ad8790fcc49cd332b963f93febc | 31 / 1437 |
| `frontier-20261028-1980-p12-border-obstruction-v1.md` | 9ff383efd20d41524ff9778ae146318ff5370990b53862289491c8cb716b4db6 | 43 / 3284 |
| `frontier-20261028-1980-p15-border-obstruction-v1.md` | 674a327045a49e7706a8511a77525c614fd93c4eccdee0ade37d254d212e09eb | 48 / 3700 |
| `frontier-20261028-1980-p36-border-obstruction-v1.md` | cfbbb939338561f2e6d7410a73adba96dc9eb2f6f628c0d6930cfb63837d26f5 | 51 / 3980 |

The classical border and Sands results, the elementary cyclotomic balances, and `|P|>=7` are explicitly stated imports reconstructed in prior written packets. The 17-pair matching, candidate counts and finite searches have been checked in exact integer arithmetic, not formally verified. Further disjoint scientific review is required before any adoption.

**END OF FIVE-SIZE ORDER-1980 REDUCTION.**
