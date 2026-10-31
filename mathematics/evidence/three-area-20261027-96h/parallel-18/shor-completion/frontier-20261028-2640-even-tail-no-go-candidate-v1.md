# Candidate theorem: no even tail border at order 2640

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 21:28:26 PDT 2026**.
**HIGH-CONSEQUENCE CONSOLIDATION of written/finite-check candidates. It is NOT independently scientifically reviewed, formally verified, cross-family verified, novelty-cleared or adopted. The original all-order completion problem remains OPEN.**

## 1. Exact candidate and nonclaims

> **Candidate theorem.** If a finite UD factor-complete extension D of the literal Shor code has actual pure-a atom `a^2640`, then its actual b-run tail-border set Q cannot have even cardinality.

This claim is strictly conditional on the complete pinned proof chain below. It does **not** exclude an odd Q, conclude that order2640 is impossible, or prove unrestricted Shor noncompletion. In particular, the pending odd-Q/55-tail theorem and f128 review are **not used** here.

The same actual D defines both direct border factors P,Q and old anchors

    A={0,3,8,11} subset P,     Y={0,1,7,13,14} subset Q.

The general actual-border factorization and the necessary Sands gcd-difference disjointness criterion are prior classical results, independently reconstructed in named predecessor packets. We explicitly also import **Coven–Meyerowitz T2 for a tile with at most two DISTINCT prime factors**, as stated in [Łaba–Londner, Theorem1.1](https://arxiv.org/html/2106.14044v3), only where named below.

## 2. Complete even-Q size partition

At n2640, the independently verified old-anchor gcd-clique certificate gives `|Q|<=266`; prime-class capacities and divisibility reduce even-Q head sizes to EXACTLY the following necessary list:

    {10,12,15,20,22,24,30,33,40,44,55,88}.                  (1)

"Exactly" here means the complete list surviving the stated preliminary sieve, NOT that any size is feasible. The screen also verifies P8/Q330 is impossible. All twelve sizes in (1) are excluded by the pinned packets in §3. No odd-Q step is used.

## 3. Branch exclusions and main assurance boundaries

| P size | Q size | exclusion and support |
|---:|---:|---|
| 10 | 264 | Complete 4,356 partial-head choices; 64 reduced tail gcd/quota cases; separate bitset/set replays. |
| 12 | 220 | T2 forces mod3-class head parity; all three remaining two-power allocations exhausted, including146 nonvacuous mod8-tail cases. |
| 15 | 176 | Complete184 partial-head sets; 9 reduced mod16/mod11 tail quota cases; separate bitset/set replays. |
| 20 | 132 | Complete245,025 partial-head choices; 69 reduced tail quota cases; complement-head/set replay. |
| 22 | 120 | T2 for the two-prime tile 22 forces opposite parity within every mod11 P-class and the Q mod16 a/b pattern; 139 reduced tail cases. |
| 24 | 110 | T2 for the two-distinct-prime tile24 forces mod3-class parity; complete245,025 partial heads; 43 reduced tail cases. |
| 30,33 | 88,80 | Written head blocker-capacity arguments on the same 24-candidate mod3 class. |
| 40 | 66 | Written forced head gcd classes4,16,660,1320; exact457-candidate tail quota contradiction. |
| 44 | 60 | Separately checked forced head gcd240; complete245,025 partial-head partition; 161 reduced tail quota cases. |
| 55 | 48 | Four disjoint forbidden head pairs vs required 11-of-12 in each of two mod5 classes. |
| 88 | 30 | Written forced head gcds4,55,240; exhaustive12,870-tail-seed/24-slot check, independently replayed. |

All computations use exact integer gcds, residue counts and finite include/exclude or subset enumeration. Producer and replay use distinct representations and, where explicitly noted in branch packets, sometimes the SAME slack-based branching; none constitutes formal proof or independent-model-family review. Each program's control is described at its exact scope. In particular, P22's positive control satisfies balances and anchors only after ALL gcd restrictions are removed; the P12 residual has a stronger explicit 2-quota SAT control with its actual H restrictions retained.

The P40 producer's first version failed an overly strong candidate-set equality and its first separately ordered replay timed out; immutable v2 successors and both failures are explicitly disclosed in the P40 packet. The P20 first independently ordered replay also timed out; its successful v2 uses the producer's slack criterion and that limitation is disclosed. Failed/UNKNOWN runs are not counted as proof.

## 4. Immutable branch pins

| Artifact | SHA256 |
|---|---|
| `frontier-20261028-2640-even-tail-screen-v1.md` | 1268f81eb28a696c2224801176daaee04ad63662a66811173c87bf074960534d |
| `frontier-20261028-2640-even-p10-obstruction-v1.md` | 67eba1a96ecd7ad65136e36ab481f63fd766c18db97fb5920bb1766db23e8a6c |
| `frontier-20261028-2640-even-p12-obstruction-v1.md` | 30b487b4fc8d676a85f1a30c2bcebae5e8bacaf5f2fb6ee2d8fdcbe246b9ab0a |
| `frontier-20261028-2640-even-p15-obstruction-v1.md` | 07848a281b3860aaeb27141e3a73365feb203fffc528bda107d993e8b9203b43 |
| `frontier-20261028-2640-even-p20-obstruction-v1.md` | 45587f23be04b012dac75705f1dbb1039556d6a8ec20796c8ef03cfb29001c52 |
| `frontier-20261028-2640-even-p22-obstruction-v1.md` | 0bf04e20757fcf83808d5764659c68e40c25e27dc87d2b5ba1917cae75130056 |
| `frontier-20261028-2640-even-p24-obstruction-v1.md` | ba761a938c3b41f8d9cc204fa15ed0ba8c5841d0dd47219689736ebfd2bdca4e |
| `frontier-20261028-2640-even-p30-p33-obstruction-v1.md` | 0424f27c9a7b5e1e1750c24a498e2688efff4d29563055c5cd355886d224b6c3 |
| `frontier-20261028-2640-even-p40-obstruction-v1.md` | 4a6e2ee447c6b6dd4d82671fc8bddc851ae3f80cac24a06ffb1a3edc4413de62 |
| `frontier-20261028-2640-even-p44-obstruction-v1.md` | 1cc6a902259724bd2ff1f45c939d2014a48492773d22651cffa0203959e86e76 |
| `frontier-20261028-2640-even-p55-obstruction-v1.md` | a8d24ba874c1d4dfef906bafbdf2be59a20c960124670fdd0b3196967affe87d |
| `frontier-20261028-2640-even-p88-obstruction-v1.md` | d94df0cb35bffa1106db3ab825330e429acb78f9f2f8af020f50a4b6b00e695f |
| `frontier-20261028-p22-cyclotomic-structure-v1.md` | eed84fa627cbf2498bc5f73a7561c199b508c8582706e4ca75a34a5b2624befd |
| `frontier-20261028-three-times-power-two-parity-v1.md` | 02b659fc96a070329901da487e855feae1d74c62cb67667d58cfcba2cd2675ea |

Individual packets pin their source scripts, finite certificates and controls. A disjoint scientific review must reconstruct (1), every allocation and relaxation, the two classical imports and all relevant search soundness/completeness; these recorded results are NOT an adoption.

**END OF ORDER-2640 EVEN-TAIL NO-GO CANDIDATE.**
