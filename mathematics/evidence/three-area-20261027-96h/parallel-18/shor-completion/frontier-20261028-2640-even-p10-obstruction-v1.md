# Shor completion: an even-tail P10 obstruction at order 2640

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 20:35:40 PDT 2026**.
**Conditional necessary-border reduction with two independently implemented exact finite checks. It does not exclude order2640, resolve the all-order problem, or claim peer/formal/cross-family/novelty acceptance.**

## 1. Branch and prime forcing

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code actual direct border factors

    |P|=10,   |Q|=264,
    A={0,3,8,11} subset P,    Y={0,1,7,13,14} subset Q.

The border theorem and necessary Sands gcd-difference disjointness are classical, independently reconstructed in earlier pinned packets. Here Q is EVEN, as required by the current research direction.

Because 5 divides |P| and not |Q|, P is uniform mod5, with2 heads in every class. The old-anchor head screen has exactly12 candidates in class2 and12 in class4; P must select two from each. Because P is coprime to3 and11, Q is uniform mod3 and11, requiring88 and24 tails respectively in every class.

## 2. Complete partial-head enumeration

Enumerate all `C(12,2)^2=4,356` ways to choose the two class2 and two class4 heads. Join each choice with the actual four old heads. Exactly866 violate an old-tail gcd restriction and are rejected. The remaining3,490 choices induce210 distinct sets H of gcd classes from their partial-head differences. Every actual P in this branch induces one of them, and actual Q must avoid its H by Sands.

For each H, screen tail candidates against ALL five old tails and H. Of the 3,490 head choices:

* 408 leave fewer than88 individually allowed tails in some mod3 class;
* 2,636 more leave fewer than24 in some mod11 class;
* 446 induce64 distinct remaining H-sets. For EACH such H, retain only the necessary Q quotas `mod3 class0=88` and `mod11 class2=24`, together with retained old tails0,13. The exact include/exclude quota search finds no solution.

The quota instance ignores every other Q condition and is therefore a relaxation. The first two counts plus the 64 checked cases cover the ENTIRE partial-head partition, so P10/Q264 is impossible if the written reduction and finite checks are independently confirmed.

## 3. Checks and positive control

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-p10-check.py` | f57009251811683d4d038f42fb8d1cbb486b844444a950dfb993f7f03373ab67 | 69 / 3787 |
| `frontier-20261028-2640-even-p10-replay.py` | 76e146cf3ce2efbcf6134f682b78c061dc01dc6df152c5126ba98074d19999a9 | 55 / 2630 |

The producer enumerates selected pairs, uses bitset branching, and reports a maximum1,297 quota-search nodes. The independently written replay enumerates complementary ten-element omissions in reverse class order, uses a separately ordered set-based search, reproduces the exact partition counts and reports a maximum3,441 nodes. A directly checked 106-residue witness satisfies the retained Q quotas and ALL old-anchor compatibility when the extra forced-head gcd classes are omitted. It is a positive RELAXATION control, not a direct tiling or a code.

The earlier even-tail screen left `{10,12,15,20,22,24,30,33,40,44,55,88}`; this packet removes10 only. The other eleven branches, order2640 itself and the original finite completion problem remain OPEN. This result does not depend on the pending odd-tail classification or its review.

**END OF ORDER-2640 EVEN P10 OBSTRUCTION.**
