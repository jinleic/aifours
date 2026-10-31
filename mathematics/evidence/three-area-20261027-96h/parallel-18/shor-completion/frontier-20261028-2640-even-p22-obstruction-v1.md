# Shor completion: an even-tail P22 obstruction at order 2640

Owner **MathShor-2**, math-5. Actual native clock of independent finite replay: **Wed Oct 28 21:19:55 PDT 2026**.
**Conditional written/finite-computation branch reduction, with an explicitly named classical import. No n2640 or all-order no-go, formal/peer/cross-family acceptance or novelty claim.**

## 1. Branch and two-prime tile structure

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code direct border factors `|P|=22, |Q|=120`; Q is EVEN. The classical actual-word border theorem and necessary Sands gcd-class disjointness criterion were independently reconstructed in earlier packets. Old anchors are `A={0,3,8,11}` and `Y={0,1,7,13,14}`.

We explicitly import the classical **Coven–Meyerowitz T2 theorem for a tile of cardinality 2*11**, as stated in [Kiss–Londner–Matolcsi–Somlai, Theorem1.2](https://arxiv.org/html/2411.03854v3). The written all-order deduction in `frontier-20261028-p22-cyclotomic-structure-v1.md` proves that the old heads0 and11 force P to have exactly one even and one odd head in every mod11 class. It also proves Q's mod16 counts equal a common a in each even class and a common b in each odd class, with `a+b=15`.

The old-anchor Q screen has NO residue4 modulo6, so all Q-elements `1 mod3` are odd. Q must be uniform modulo3, with40 in that class; hence `8b>=40`, or `b>=5`. The old tail0 forces `a>=1`. Therefore

    1<=a<=10,   b=15-a.                                        (1)

The independent forced-gcd240 head lemma in the preceding even-P44 packet also applies: P has2 elements in each named mod11 class, so P necessarily uses gcd240.

## 2. Complete partial-head and tail partition

The old-anchor P screen has6 even and6 odd candidates in each of mod11 classes1 and2. The T2 consequence requires one of each parity in both classes: `6^4=1,296` partial-head choices. Join each to the four old heads and add the independently forced gcd240. Exactly272 choices violate an old-tail forbidden gcd class; the other1,024 induce37 distinct partial-head gcd-class sets H.

For each H, Q must avoid H against all old tails. Among those1,024 choices,64 fail an individual mod3/mod5 capacity and452 more admit no integer a satisfying (1) and the individual mod16 capacities. The remaining508 choices induce24 H-sets and139 total allowed `(H,a)` cases.

For EVERY one of those139 cases, an exact include/exclude search enforces all16 mod16 fibre quotas from (1), Q's necessary `mod3 class1=40` and `mod5 class1=24` quotas, the old tail anchors, and H-disjointness. All return UNSAT. Other Q quotas are deliberately omitted, so each is a relaxation. This completes the P22/Q120 exclusion, contingent on the named T2 import and independently checked forced240 lemma.

## 3. Finite evidence and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-p22-cyclotomic-structure-v1.md` | eed84fa627cbf2498bc5f73a7561c199b508c8582706e4ca75a34a5b2624befd | 51 / 4305 |
| `frontier-20261028-2640-even-forced-240-check.py` | 8529821909feeb14a11638eaff93450e745e62c6651990997292b072a01d359f | 42 / 2067 |
| `frontier-20261028-2640-even-forced-240-replay.py` | 310e484581c16e9e36807a4f425a4f448867b19a10bd805658c534873bce10d4 | 27 / 1427 |
| `frontier-20261028-2640-even-p22-check.py` | 721abc668e2782ff0f335773667389d88538ebe423df1310c776e32762e5a9d4 | 83 / 4473 |
| `frontier-20261028-2640-even-p22-replay.py` | fa573ee9ee2e1916ee6f60f0cf44d52becc5b3e363ff5e764ddba5ed6a16009d | 60 / 3204 |

The producer uses bitsets and selected head pairs; the separately written replay uses set states and independent even/odd products. Both reproduce the full partition and maximum755 nodes per quota case, using the SAME slack-based branching criterion. This is same-harness replay, not independent-family or formal verification. The producer also verifies a 120-element **balance/anchor-only** CRT control after removing ALL gcd constraints; it explicitly contains old-head-forbidden gcd differences and is NOT a tail tiling or code. This weak control is not represented as a full original-screen SAT witness.

With prior even-Q exclusions, the only remaining even-Q head sizes at order2640 are `{12,24}`. Both remain open. No pending odd-Q theorem is used, and the original finite completion problem remains OPEN.

**END OF ORDER-2640 EVEN P22 OBSTRUCTION.**
