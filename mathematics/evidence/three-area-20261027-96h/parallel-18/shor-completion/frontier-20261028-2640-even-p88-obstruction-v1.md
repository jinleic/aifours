# Shor completion: an even-tail P88 obstruction at order 2640

Owner **MathShor-2**, math-5. Actual native clock of independent replay: **Wed Oct 28 20:45:19 PDT 2026**.
**Conditional necessary-border reduction with two exact finite implementations. No complete n2640 or all-order no-go, formal/peer/cross-family acceptance or novelty claim.**

## 1. Branch and forced head gcd classes

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and the same-code direct border factors `|P|=88, |Q|=30`. Q is EVEN. The actual-word border theorem and necessary Sands gcd-class disjointness criterion are classical and independently reconstructed in earlier packets. Old anchors are `A={0,3,8,11}` and `Y={0,1,7,13,14}`; old forbidden gcd classes are `G_Y={1,2,6,12}` for P and `G_A={3,5,8,11}` for Q.

P is uniform modulo11 with8 heads per class. Three short old-anchor-screen/matching arguments force P to use gcd classes4,55,240:

* If P avoided4, its screened mod11 classes1 and4 each have exactly8 candidates, so all are forced;155 and576 then have forbidden gcd1.
* If P avoided55, omitting candidate456 from screened mod11 class5 would leave11 candidates containing four disjoint gcd55-conflict pairs, permitting at most7 of the required8; thus456 is forced. The same argument forces35 in class2. Their difference has forbidden gcd1.
* If P avoided240, its screened mod11 classes2 and10 have10 candidates each. Five explicit disjoint cross-conflict pairs leave capacity at most15, below the required16.

The producer checks every candidate count and matching explicitly; the separate replay independently enumerates all admissible eight-subsets in each pair of head classes and tests cross compatibility. Hence Q must avoid `{4,55,240}` as well as G_A.

## 2. Tail quota and 16-candidate slot obstruction

Q is uniform modulo5 and3, requiring6 tails per mod5 class and10 in mod3 class1. After screening against all old tails with the seven forbidden gcd classes, there are NO mod3-class1 candidates in mod5 classes0,4. All such candidates in classes1,2,3 are odd. The three mod5 quotas account for18 tails; exactly10 of them are1 mod3, so exactly8 are not. There are only16 screened candidates for those eight non-1-mod3 tails.

For any two distinct mod3-class1 candidates in the SAME `(mod5,mod16)` slot, the difference is divisible by `3*5*16=240`; since `2640/240=11`, its gcd with2640 is exactly240. Thus under the no240 condition at most one can occupy a slot. There are24 possible slots, eight odd mod16 slots for each of the three mod5 classes.

Exhaust all `C(16,8)=12,870` potential non-1-mod3 seeds:

* 12,657 have an internal forbidden gcd pair;
* 33 overfill a required mod5 class;
* the remaining180 leave too few individually seed-compatible `(mod5,mod16)` slots to complete at least one class's six-tail quota.

The last test deliberately ignores additional conflicts among proposed slot occupants, so it is a relaxation. No seed remains; Q must use one of the gcd classes already forced in P, contradicting Sands.

## 3. Checks and scope

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-p88-check.py` | 4b4967c40f6b7aa57cf66280a9864de130f961c89b89b666fc2a42193c74ad5c | 53 / 3161 |
| `frontier-20261028-2640-even-p88-replay.py` | ee25a2398462eab2875cc636e18dc11e68d09f23614f423d6fc657c99d52a798 | 42 / 2166 |

The producer verifies literal head matchings and enumerates included seeds; the separately written replay independently enumerates head subsets and the complementary omitted seeds, reproducing `12,870 / 12,657 / 33 / 180 / 0`. The producer directly verifies an 18-tail positive relaxation meeting the mod5/mod3 quotas when only gcd240 is dropped; it contains gcd240 collisions and is not a code or border factorization.

With prior even-Q screens and the P10/P15/P55 exclusions, the remaining even-Q P-sizes at order2640 are `{12,20,22,24,30,33,40,44}`. Those branches, order2640 itself and the original all-order problem remain OPEN. No pending odd-tail theorem is used.

**END OF ORDER-2640 EVEN P88 OBSTRUCTION.**
