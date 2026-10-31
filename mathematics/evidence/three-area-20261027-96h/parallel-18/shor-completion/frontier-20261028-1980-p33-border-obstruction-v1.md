# Shor completion: the last border branch at order 1980

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 20:04:07 PDT 2026**.
**HIGH-CONSEQUENCE CANDIDATE: written reduction plus exact finite checks in two same-harness implementations. Not yet reviewed, formally verified, cross-family verified or adopted. No all-order noncompletion or novelty claim.**

## 1. Scope

For any hypothetical finite UD factor-complete extension D of the literal Shor code with actual pure-a order1980, the earlier complete cardinality sieve in `frontier-20261028-1980-one-border-size-v1.md` leaves only

    |P|=33,   |Q|=60,

for the SAME actual direct border tiling `P+Q=Z_1980`. Here we give a candidate contradiction in this last branch. Together with the explicitly pinned predecessor chain, it is a candidate exclusion of **n=1980 only**, not an all-order solution. All predecessor and present steps require independent scientific review before adoption.

The old anchors are `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`. The known classical border theorem and Sands gcd-difference disjointness criterion were independently reconstructed in earlier written packets. At n1980, old P-differences have gcd classes `G_A={3,4,5,11}` and old Q-differences have gcd classes `G_Y={1,2,6,12}`.

Because Q has size60 and P has size33, Q is uniform modulo4 and5, with15 in every mod4 class and12 in every mod5 class. Because P has size33 and Q is coprime to11, P is uniform modulo11, with3 heads per class.

## 2. Q must use gcd36

Assume Q avoids gcd36. Screen all Q-candidates against Y using the forbidden gcd classes `G_A union {36}`. In EACH of mod5 classes1,2,3 there are exactly four even screened candidates.

For either class1 or class3, choosing any one of the four even candidates leaves at most6 individually compatible odd candidates in that same mod5 class. Even if all four even candidates were used, that class would contain at most10 tails, less than its required12. Thus both classes1 and3 must consist entirely of odd Q-elements.

For class2, choosing any three of the four even candidates leaves at most6 individually compatible odd candidates. Even if all four evens were used, the class would contain at most10 tails. Hence class2 has at most2 evens and at least10 odds.

Those three classes would therefore contain at least `12+10+12=34` odd Q-elements. But mod4 uniformity requires exactly `15+15=30` odds. Contradiction. Therefore Q uses gcd36, and Sands requires P to avoid gcd36.

## 3. P must use gcd180 and gcd660

Suppose P also avoided gcd180. The old-anchor P screen with `{36,180}` additionally forbidden has exactly the following candidates in mod11 classes5 and9:

    class5: {423,1028,1688,1743},
    class9: {603,1208,1868,1923}.

The four cross pairs `(423,603),(1028,1208),(1688,1868),(1743,1923)` all have gcd180. The required three elements from EACH class select six endpoints of four disjoint pairs and therefore force one forbidden pair. Thus P uses gcd180.

Similarly, if P avoided gcd660 as well as36, its screened mod11 class9 would consist exactly of two triples

    {548,1208,1868},  {603,1263,1923},

with pairwise gcd660 within each triple. It could select at most2 in the class, contradicting the required3. Thus P uses gcd660 too.

## 4. Q cannot avoid both head gcd classes

Sands therefore requires Q to avoid `{180,660}` as well as the old head classes G_A. Screening against ALL old tail anchors leaves332 candidate residues. Exhaustive include/exclude search enforces the actual five anchors and all nine exact prime-balance quotas

    mod4 classes0,1,2,3: 15 each;
    mod5 classes0,1,2,3,4: 12 each.

The bitset implementation finds no selection in7,791 search nodes, with3,743 quota prunes; the separately written set-based implementation with another branch ordering finds no selection in8,403 nodes, with4,202 prunes. Both check gcd conflicts and quota pruning with exact integers. The producer also directly checks an explicit 60-residue Q-only relaxation witness satisfying all nine quotas and old-anchor compatibility when gcd660 alone is dropped; that witness contains gcd660 differences, so the control is nonvacuous. It is not a complete border factorization.

The last P33 branch is therefore excluded at the written/finite-computation candidate level. No historical Z3 UNKNOWN or SAT result is used as a proof.

## 5. Pins and next admissible order

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1980-p33-final-check.py` | 9d6b04ebec2d3028182b69e8361b698b491b94b62940b16443c00fa544bbdd3d | 71 / 4007 |
| `frontier-20261028-1980-p33-final-replay.py` | 108a4c1e7023248529649879bf4c98be4c8d72f71b325ffb398b83887afc5d4f | 51 / 2767 |
| `frontier-20261028-1980-one-border-size-v1.md` | 3abbdf4a8300e9a1c6849093811daf40368ec5ea7fc3028a3e433af52940cf10 | 67 / 5811 |
| `frontier-20261028-660-and-order-floor-candidate-v1.md` | cce97442e94386f80e9d63f782c5be83c7c4c0e3a7eddb5eb38e0c999494ab79 | 80 / 6677 |

If the independent review eventually supports BOTH the earlier n660/n1320 exclusions and this n1980 exclusion, then the independently reconstructed all-order alternative `660|n OR 2310|n` implies **n>=2310**. This is a CONDITIONAL candidate floor, not an adopted fact. The original finite completion/noncompletion problem remains OPEN, and no candidate order has been constructed.

**END OF ORDER-1980 P33 BORDER CANDIDATE.**
