# Shor completion: one remaining border size at order 1980

Owner **MathShor-2**, math-5. Native `/bin/date` after exact checks: **Wed Oct 28 19:57:13 PDT 2026**.
**Conditional written/finite-computation candidate, not a completed n=1980 exclusion, original all-order solution, formal proof, peer acceptance or novelty claim.**

## 1. Complete scoped result

For any hypothetical finite UD factor-complete extension of the literal Shor code with actual pure-a order1980, its actual direct border factorization must have

    |P|=33,   |Q|=60.                                          (1)

This is a necessary condition only: (1) has not been shown either possible or impossible. The preceding `frontier-20261028-1980-five-border-sizes-v1.md` reduced the complete cardinality partition to `{18,22,30,33,66}`. The present packet excludes the four other sizes by exact integer certificates. The candidate is conditional on independently reviewing the predecessor's cardinality sieve, actual-word border theorem, classical Sands gcd disjointness, and the new finite checks.

All uses are for the SAME hypothetical D, with its old border anchors `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`. At n1980, old gcd classes are respectively `G_A={3,4,5,11}` and `G_Y={1,2,6,12}`.

## 2. Sizes18 and22: forced gcd on both sides

At `|P|=18, |Q|=110`, P is uniform modulo9 with2 in each class, and Q is uniform modulo11 with10 in each class. If either P or Q avoids gcd660, the corresponding relaxed exact quota instance below has no solution:

| side | retained quota classes | candidates | bitset nodes / prunes | independent set-based nodes / prunes |
|---|---|---:|---:|---:|
| P18 | mod9 classes1,4,7, each2 | 18 | 47 / 24 | 45 / 23 |
| Q18 | mod11 classes1,2, each10 | 52 | 327 / 148 | 415 / 208 |

At `|P|=22, |Q|=90`, P is uniform modulo11 with2 in each class, and Q is uniform modulo9 and5 with10 and18 in each respective class. If either side avoids gcd180, the relevant relaxed instances have no solution:

| side | retained quota classes | candidates | bitset nodes / prunes | independent set-based nodes / prunes |
|---|---|---:|---:|---:|
| P22 | mod11 classes6,7,9,2, each2 | 24 | 147 / 69 | 161 / 81 |
| Q22 | mod5 classes4,3, each18; mod9 classes6,3,8, each10 | 178 | 573 / 287 | 555 / 278 |

Each instance retains only candidates in its named classes, checks compatibility against ALL old anchors, forbids the opposite old-anchor gcd classes plus its named gcd, and enforces only the displayed quotas and retained anchors. These are relaxations: dropping other actual border elements or constraints cannot create a false exclusion. The producer checks a concrete SAT relaxation witness for EACH of the four instances when the extra named gcd ban is removed. In either size, both actual borders therefore use the same gcd class, contradicting Sands.

## 3. Size30: two compatible-subset Hall counts

If |P|=30, P is uniform modulo5 with6 elements per class. Its old-anchor screen has exactly eight heads in class4 mod5:

    {264,539,924,1119,1199,1584,1664,1859}.

The triples `{264,924,1584}` and `{539,1199,1859}` have pairwise gcd660; the remaining two candidates are singletons. Avoiding gcd660 would allow at most4 heads in the class, so P uses gcd660.

Q has size66 and is uniform modulo11, with6 tails in each class. If Q avoided gcd660, each of its old-anchor-screened mod11 classes0 and3 has28 candidates including anchors0 and14. Hence Q must choose5 vertices from each of the two remaining 27-sets L,R. Exact enumeration checks all `C(27,5)=80,730` L-subsets:1,458 are internally gcd-compatible, and every one leaves at most4 compatible R-candidates. Independently reversing L,R gives exactly the same counts. Thus Q also uses gcd660, a contradiction.

## 4. Size66: three forced head gcd classes and five tail cliques

If |P|=66, P is uniform modulo11, requiring6 heads in EACH of classes1 and2. The old-anchor candidate sets are

    P1={155,188,243,848,903,936,1508,1563},
    P2={68,123,695,728,783,1388,1443,1476}.

Within P1, the triples `{188,848,1508}` and `{243,903,1563}` have pairwise gcd660; avoiding660 allows at most4 heads, so P uses660. Across P1,P2 the certificate gives eight disjoint gcd180 pairs, and six disjoint gcd60 pairs. Choosing12 vertices from the16 endpoints would force at least one pair of each matching, so P also uses180 and60.

Q has size30 and is uniform modulo5, requiring6 tails in class0. If Q avoided all three forced P gcd classes and the four old head gcd classes, its old-anchor screen would contain61 candidates in that tail class. The pinned check partitions them into FIVE pairwise-conflicting cliques of sizes27,24,6,3,1, so Q could choose at most5. Contradiction.

## 5. Pins and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1980-five-border-sizes-v1.md` | 7f69d2a58fad50ab59883c234b13a9ee0fa318457a8b6b21043c1d75043ff572 | 51 / 4836 |
| `frontier-20261028-1980-p18-p22-check.py` | 8077fa9747a612e71cd6d62b7977a24d9189e81af34eada714512aca50e59252 | 54 / 3053 |
| `frontier-20261028-1980-p18-p22-replay.py` | 4af2eff429d1bfa92dadb5046be1196de1a73afa97b5b6fe419fb7e7a58a67cd | 39 / 1943 |
| `frontier-20261028-1980-p30-hall-check.py` | 4c9bab2b65e08325711fa260bdc7e4b3b235b8aa4a191e0c093e267bb3bdcd99 | 33 / 1493 |
| `frontier-20261028-1980-p66-matching-check.py` | 778b6813b6f9bbd4c86b6d5772e98a561855198d98e9b0fe672bf122b8096137 | 30 / 1782 |

The separate SAT/timeout observations are not used as proof. All asserted finite checks use exact integer arithmetic; paired implementations are same-harness, not independent model-family or formal verification. The original finite UD factor-completion problem and the remaining order1980 border case (1) remain OPEN.

**END OF ONE-SIZE ORDER-1980 REDUCTION.**
