# Shor completion: an even-tail P20 obstruction at order 2640

Owner **MathShor-2**, math-5. Actual native clock of the completed set-based replay: **Wed Oct 28 20:58:11 PDT 2026**.
**Conditional necessary-border reduction with exact finite checks. It does not exclude n2640 or solve the all-order problem, and is not formally/peer/cross-family accepted or novelty-cleared.**

## 1. Complete partial-head partition

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code direct border factors `|P|=20, |Q|=132`; Q is EVEN. The actual-word border theorem and Sands gcd-difference disjointness are classical and independently reconstructed in earlier packets. The old anchors are `A={0,3,8,11}` and `Y={0,1,7,13,14}`.

Because Q is coprime to5, P is uniform modulo5, with4 heads in every class. Its old-anchor screen has exactly12 candidates in each of mod5 classes2 and4, so there are exactly `C(12,4)^2=245,025` partial choices. Each is joined to the four old heads. Of these choices,141,425 have an old-tail forbidden gcd difference. The other103,600 induce223 distinct sets H of partial-head gcd classes.

Q is uniform modulo3 and11, with44 and12 elements per class. For each induced H, Q must avoid H against every old tail by Sands. Of the surviving103,600 partial choices,97,146 leave fewer than12 individually compatible tails in some mod11 class. The remaining6,454 choices induce69 H-sets; for EVERY one, the exact relaxed Q instance with just quotas `mod3 class0=44` and `mod11 class2=12`, retaining old anchors0,13, has no solution. No mod3 capacity rejection occurred. This exhausts every partial-head possibility and excludes P20/Q132 at the stated candidate scope.

## 2. Checks, control and failure disclosure

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-p20-check.py` | 2da9f318c8fbc18e28e896bc9c3b845cfc09f66ecde050858ebfe3889c657e44 | 66 / 3424 |
| `frontier-20261028-2640-even-p20-replay-v2.py` | 1952802a81e18f1be08f5ebbf67be42c20af9ef86cff39cb4aef3ba8eed1ebb6 | 56 / 2763 |

The producer enumerates selected four-subsets and uses bitsets. The separately written replay enumerates their eight-element complements in reverse class order and uses set states. Both reproduce all counts; the maximum quota-search size is523 nodes. They use the SAME slack-based branching criterion, so they are different representations/replays, not independent model-family proof.

The producer directly checks a 50-element Q-only relaxation satisfying both displayed quotas and all old-anchor compatibility when extra partial-head gcd restrictions are omitted. It is not a tiling or code. The prior independently ordered set replay `frontier-20261028-2640-even-p20-replay.py` timed out after35 seconds and gave no verdict; the immutable v2 successor is the completed replay and explicitly preserves that failure.

With the preceding even-Q sieve and P10/P15/P30/P33/P40/P55/P88 exclusions, the remaining even-Q head sizes at order2640 are `{12,22,24,44}`. None is claimed feasible. The pending odd-Q theorem is not used, and the original finite UD factor-completion problem remains OPEN.

**END OF ORDER-2640 EVEN P20 OBSTRUCTION.**
