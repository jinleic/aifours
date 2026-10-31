# Shor completion: an even-tail P40 obstruction at order 2640

Owner **MathShor-2**, math-5. Native clock of the exact set-based replay: **Wed Oct 28 20:53:37 PDT 2026**.
**Conditional written/finite-computation branch reduction; no n2640 or unrestricted completion no-go, formal/peer/cross-family acceptance or novelty claim.**

## 1. Branch and forced head gcd classes

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code direct border factors `|P|=40, |Q|=66`. Q is EVEN. P is uniform modulo5 with8 heads per class; Q is uniform modulo3 and11 with22 and6 tails per class. The old anchors and classical Sands gcd-disjointness criterion are as in `frontier-20261028-2640-even-tail-screen-v1.md`.

The old-anchor P screen and elementary exact matching/capacity arguments force P to use gcd classes `{4,16,660,1320}`:

* If P avoided4, its screened mod5 classes2 and4 have exactly8 candidates each; all are forced, including872 and459, whose difference has old-tail forbidden gcd1. If P avoided16 the same argument forces872 and1779, again gcd1.
* If P avoided1320, its12 screened candidates in mod5 class4 form six disjoint gcd1320 pairs. It could select at most6, below the required8.
* If P avoided660, its12 candidates in mod5 class4 split into two four-cycles of gcd660 plus four singletons. Selecting8 forces every singleton and one of two opposite pairs in each cycle. In EACH of the four possibilities, compatibility with those heads and all old anchors leaves only6 candidates in mod5 class1, below its quota8.

## 2. Tail quota contradiction

By Sands, actual Q must avoid all four forced P gcd classes as well as old P-difference classes `{3,5,8,11}`. The old-anchor tail screen has457 candidates. Both the bitset and separately written set-based programs exhaust the exact Q-mod3 and Q-mod11 quotas, enforce all five old tail anchors and find no selection: each reports2,983 search nodes and611 quota prunes. The set-based successor uses the SAME slack-based branching criterion as the bitset implementation, so this is a distinct representation/replay, not a wholly independent search strategy or model family.

The producer directly verifies a literal 66-element tail-only set satisfying both prime balances and old-head gcd restrictions when all four extra forced-head classes are omitted. This is a positive relaxation control, not a tiling or complete code.

## 3. Failure disclosure and immutable pins

The first producer `frontier-20261028-2640-even-p40-check.py` FAILED a too-strong equality in the no660 subcase: it expected8 class1 candidates while the correctly anchor-filtered set has6. It produced no scientific result. The preserved successor v2 states and checks the correct stronger count6. The first separately ordered set replay timed out after35s and gave no verdict; the separately written v2 replay completed using the stated slack criterion. Neither failed attempt is silently counted as verification.

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-p40-check-v2.py` | 66ade09cb0653daf1bd97a686571bc81ed11e34f2552e0f4d209f846c572d463 | 66 / 3865 |
| `frontier-20261028-2640-even-p40-replay-v2.py` | 983e4c73b8d3aa400aab31fd9ab0495b56041580b1a885610641a7a044a1dd32 | 35 / 1689 |

With the prior even-Q screen and P10/P15/P30/P33/P55/P88 exclusions, the remaining even-Q P-sizes at order2640 are `{12,20,22,24,44}`. None is claimed feasible. The pending odd-Q theorem is not used, and the original finite UD factor-completion problem remains OPEN.

**END OF ORDER-2640 EVEN P40 OBSTRUCTION.**
