# Shor completion: an even-tail P44 obstruction at order 2640

Owner **MathShor-2**, math-5. Native clock of the independent finite replay: **Wed Oct 28 21:13:40 PDT 2026**.
**Conditional written/finite-computation branch reduction; no n2640 or all-order completion no-go, peer/formal/cross-family acceptance or novelty claim.**

## 1. Branch and necessary gcd240

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code direct border factors `|P|=44, |Q|=60`; Q is EVEN. The classical actual-border and Sands gcd-disjointness criteria were independently reconstructed in earlier packets. Old head and tail anchors are `A={0,3,8,11}` and `Y={0,1,7,13,14}`.

P is uniform modulo11, with4 elements per class. In particular it has at least2 in each of mod11 classes2,10,9,7,3, and must contain the old head3. Assume P avoids gcd240 in addition to old-tail gcd classes. The 63 old-anchor-compatible candidates in those five classes cannot provide even2 per class: exact bitset quota search returns UNSAT in5,521 nodes, and a separately written set-based search returns UNSAT in32,971 nodes. The producer directly checks a positive head-only relaxation when gcd240 is dropped. Thus P uses gcd240, so Q must avoid it.

## 2. Complete partial-head and tail partition

P must choose4 from each of the old-anchor-screened mod11 classes1 and2, each containing exactly12 candidates. Enumerate all `C(12,4)^2=245,025` choices, joined with A:

* 141,425 violate an old-tail gcd class and are rejected.
* The remaining103,600, after adding the independently forced gcd240, induce195 distinct partial-head gcd-class sets H.
* Q is uniform mod3 and5, with20 and12 tails per class. Among the103,600 partial choices,43,562 leave fewer than12 individually compatible tails in some mod5 class. No choice fails the mod3 individual-capacity test first.
* The remaining60,038 choices induce161 H-sets. For EACH H, the exact relaxed Q selection with only quotas `mod3 class0=20`, `mod5 class1=12`, and retained old tails0,1 has no solution.

The producer and a separately written complement-head/set-state replay reproduce the whole partition. Both tail searches use the same slack-based branching criterion, so they are distinct representations, not independent strategies or independent-model-family proofs. A literal 21-element positive Q-only control satisfies the two quotas and old-head restrictions when the extra partial-head gcd classes are omitted; it is not a tiling or complete code.

## 3. Pins and boundary

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-forced-240-check.py` | 8529821909feeb14a11638eaff93450e745e62c6651990997292b072a01d359f | 42 / 2067 |
| `frontier-20261028-2640-even-forced-240-replay.py` | 310e484581c16e9e36807a4f425a4f448867b19a10bd805658c534873bce10d4 | 27 / 1427 |
| `frontier-20261028-2640-even-p44-check.py` | 31bee4b66dcd0d0d15f2c1bf8205325054cbaf4dd34bc9e18f50c73d87a5cc40 | 65 / 3306 |
| `frontier-20261028-2640-even-p44-replay.py` | 74ada7718954db46d77b0e6c4c628a18c3db3e0e351c9cbf109294f43f99cf67 | 55 / 2701 |

The largest individual tail search used8,559 nodes. With the preceding even-Q sieve and P10/P15/P20/P30/P33/P40/P55/P88 exclusions, only `{12,22,24}` remain as necessary even-Q head sizes at order2640. No feasibility is asserted, and the pending odd-Q theorem is not used. Order2640 and the original unrestricted finite UD factor-completion problem remain OPEN.

**END OF ORDER-2640 EVEN P44 OBSTRUCTION.**
