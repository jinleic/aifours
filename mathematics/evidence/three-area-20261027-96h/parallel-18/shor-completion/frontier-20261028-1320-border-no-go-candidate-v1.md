# Candidate theorem: the Shor code has no order-1320 finite completion

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 19:32:24 PDT 2026**.
**HIGH-CONSEQUENCE CANDIDATE: written reduction plus exact finite computations with separate same-harness implementations; NOT YET independently reviewed, formally verified, cross-family reviewed, novelty-cleared or adopted. This is not an all-order solution.**

## 1. Exact claim and boundary

> **Candidate theorem.** No finite uniquely decipherable factor-complete extension D of the literal Shor code can have `a^1320` as its actual pure-a atom.

The code has old atoms `b,a^3b,a^8b,a^11b` and `b,ba,ba^7,ba^13,ba^14`. For any hypothetical D define its actual multi-b-permitting border sets

    P={i mod1320 : a^i b^k in D, k>=1},
    Q={j mod1320 : b^l a^j in D, l>=1}.

The classical Restivo–Salemi–Sportelli border theorem, also independently reconstructed from actual word lists and guarded factors in the pinned predecessor, forces `P+Q` to tile `Z_1320` directly, with

    A={0,3,8,11} subset P,   Y={0,1,7,13,14} subset Q.       (2)

The claim follows if the finite cyclic tiling problem (2) has no solution. The argument below gives a complete conditional cardinality partition and separately checked exclusion of every part. **The original unrestricted finite-completion/noncompletion problem remains OPEN.** No new lower bound beyond the specific exclusion1320 is asserted here; in particular no unreviewed historical divisibility claim is imported.

## 2. Shared arithmetic imports and initial finite partition

The necessary direction of the classical Sands divisor-class theorem is independently derived in `frontier-20261028-1320-divisor-class-obstruction-v1.md`: in any direct cyclic tiling, nonzero differences from P and Q cannot have the same gcd with the order. For the actual old anchors at1320,

    gcd-classes(A-A)\{1320} = {3,5,8,11},
    gcd-classes(Y-Y)\{1320} = {1,2,6,12}.                    (3)

Since `1320=2^3*3*5*11`, primes3,5,11 occur only once. For each of these, the side whose cardinality is divisible by the prime is uniform in that prime modulus: at a primitive prime root the other side cannot vanish, since its cardinality is prime-coprime.

The independently checked divisor-packing certificate in the cited predecessor proves `|P|<=80, |Q|<=130`. Together with the product identity this leaves exactly

    |P| in {11,12,15,20,22,24,30,33,40,44,55,60,66}.

The `|P|=11` case fails mod11 uniformity because the old heads0,11 occupy the same residue class. All further exclusions are quantified only at n=1320.

## 3. Written small-prime reductions

The independently checked exact residue tables in `frontier-20261028-1320-four-border-sizes-v1.md` show:

* The old-anchor head candidate set has 12 residues in class1 modulo3, and four explicit disjoint gcd-forbidden pairs leave at most8 selectable. Thus 3-uniform sizes30,33,60,66 are impossible.
* The head candidate set has only6 residues in class2 modulo5, excluding 5-uniform sizes40 and55.
* Size15 would require five heads in the first class mod3 and only one new head in class3 mod5; the packet gives eight explicit pairwise blocking witnesses, a contradiction.
* For size22, Q has size60 and is uniform modulo3 and5. In each mod5 class1,2,3, an explicit four-pair gcd-5 cover and parity/mod11 pigeonhole force at least8 of the12 elements to be1 modulo3. These three classes contribute at least24, contradicting the uniform requirement20.

Thus only sizes `{12,20,24,44}` remain. Exact finite gcd checks and all numerical lists are pinned in that predecessor.

## 4. Size12: exact two-class Hall obstruction

For `|P|=12`, Q has size110 and is uniform modulo11, with10 elements in each class. From the screened tail candidates, the mod11 classes0 and3 contain26 candidates each, including the old anchors0 and14. After deleting those anchors there are sets L,R of25 each; actual Q must choose9 from each.

Connect a left and right candidate when their difference gcd lies in `{3,5,8}`, all forbidden by the old heads. `frontier-20261028-1320-hall-check.py` checks all `C(25,9)=2,042,975` left nine-sets and finds at least18 neighbors each, leaving at most7 right vertices. A separate transposed enumeration of all `C(25,8)=1,081,575` right eight-sets finds at least17 neighbors each, leaving at most8 left vertices. Either exact count refutes the needed9-by-9 independent selection. The full histogram, minimizers and code are named in the three-size predecessor.

## 5. Size20: forced shared gcd264

For `|P|=20`, Q has size66. P is uniform modulo5, selecting four from each of the six individually screened head candidates in classes2 and4. These two six-sets have six disjoint cross pairs of gcd264, explicitly listed in `frontier-20261028-1320-two-border-sizes-v1.md`; selecting eight endpoints forces one pair, so P uses gcd264.

The same packet shows that Q also must use gcd264. If not, Q is uniform mod11 (six per class) and mod3 (22 in class1). Individually screened tail candidates contain no4 modulo6, so the class1 tails are odd and occupy at most one of the44 `(mod11,mod8)` slots apiece. Classes1,2,7 mod11 require two non-class1 elements each. Both a bitset implementation and a separately written set implementation enumerate the `C(10,2)^3=91,125` seed choices; exactly1,143 survive seed compatibility, of which1,089 have fewer than22 open slots and54 cannot fill a required mod11 quota even under a deliberately relaxed upper bound. No seed remains. Simultaneous gcd264 in P and Q contradicts (3).

## 6. Size24: forced heads and four exact tail quotas

For `|P|=24`, Q has size55, which is odd. Therefore all `Phi_2,Phi_4,Phi_8` divide the P-mask and P is uniform mod8, with exactly3 heads in each class. The old-anchor head screen has exactly3 candidates in EACH of mod8 classes1,2,5,6, forcing all twelve residues

    33,198,253,418,473,638,693,858,913,1078,1133,1298.

In particular P contains33,198,253,418,473,693. Their differences from33 have gcds respectively165,220,55,440,660. Hence Q must avoid all five gcd classes

    H={55,165,220,440,660},

in addition to the four classes in (3) forbidden by old heads. Q's size55 forces prime balance: 11 tails in each class mod5, and5 tails in each class mod11.

A relaxation keeps only candidates in mod5 classes0,4 OR mod11 classes0,3, and ignores all other Q-elements except for their mandatory old-anchor compatibility. It requires only the four quotas `(11,11,5,5)` and actual anchors0,14. There are144 screened core candidates. Under the nine forbidden gcd classes `{3,5,8,11} union H`, exhaustive include/exclude search, with explicit per-quota upper-bound pruning, has no solution. The two independent implementations returned:

* Bitset search: 831 search nodes,356 quota prunes,60 memo hits, UNSAT.
* Separately ordered set-based search: 991 nodes,496 quota prunes, UNSAT.

The bitset program additionally checks a literal 22-residue positive control satisfying the SAME four quotas and all old-anchor compatibility after **only gcd220 is removed**; its exhibited gcd220 collisions make that relaxation nonvacuous. Therefore Q must use a gcd class already forced in P, contradiction.

## 7. Size44: forced gcd55 and a 495-seed tail enumeration

For `|P|=44`, Q has size30; prime balance makes P uniform modulo11, four heads per class. In the old-anchor head screen, classes1 and2 modulo11 are exactly

    C1={155,188,243,848,903,936},
    C2={35,68,123,728,783,816}.

Assuming P avoids gcd55, the four choices from C1 must include155: the four elements `{188,243,848,903}` form a 4-cycle of gcd55 conflicts and936 is the sole remaining candidate. Likewise the four choices from C2 must include816. But `gcd(155-816,1320)=1`, a gcd class already present in Y, impossible. Hence P uses gcd55 and Q must avoid it.

For Q, prime balance requires6 elements in each mod5 class and10 each in mod3 classes0 and2. Applying only old-anchor compatibility and forbidding gcd55 leaves **no** candidate congruent1 modulo3 in mod5 classes0 or4. The actual six elements in each of these classes therefore account for12 of Q's exactly20 non-1-mod3 elements. The other8 must come from exactly the following12 screened candidates in mod5 classes1,2,3:

    47,363,443,561,627,641,693,707,773,891,971,1287.

There are `C(12,8)=495` eight-element seeds. Two separately implemented exact programs, one enumerating the seeds and the other their four-element complements, both find 474 seed conflicts and21 compatible seeds. For each compatible seed they exhaust all six-element selections in the mod5 classes0 and4, retaining old anchors0 and14, checking internal and cross gcd conflicts and the exact two mod3 quotas. Exactly156 candidate pairs meet the balance quotas before the cross-gcd test; NONE meets that test. The producer also checks an explicit 20-residue relaxation witness when gcd55 alone is removed. Thus Q must use gcd55, contradicting the forced P class.

## 8. Immutable evidence pins

All scripts operate on exact integers and are finite; all independently replayed results are same-harness, not independent-model-family or formal verification.

| Artifact | SHA256 |
|---|---|
| `frontier-20261028-six-head-border-factorization-v1.md` | 56fd2cff931af2da61e2f8a17c513d8af5c3cc8064c9d9ed66c5c361fb3a6051 |
| `frontier-20261028-1320-divisor-class-obstruction-v1.md` | 228757d547c671685c9e2c1b58332b6e8615b15dc9f7db9b49814591dd072b23 |
| `frontier-20261028-1320-divisor-packing-v1.json` | eb73d65b4e9d2f79b917e4da2d390cd157388341bb75e5c5049a914cf6ef39cb |
| `frontier-20261028-1320-divisor-packing-check.py` | 937a789eba003c735dd6e0b72dc7c6967058d9b4417a48d9d9b8a9689567dfc6 |
| `frontier-20261028-1320-four-border-sizes-v1.md` | 3d93c233bc6ea6802a797564edf0c18e21de2215dbf85c70136bad4556399c3e |
| `frontier-20261028-1320-prime-residue-check.py` | fd5bb126e37396ec73681954c9e67205ed8c1ffaa4b8e62d8cf454612181068d |
| `frontier-20261028-1320-hall-check.py` | 715b325871c8148c1d62647e4925fca1edc23a4a9e71840bd41a6250b59404b6 |
| `frontier-20261028-1320-two-border-sizes-v1.md` | 0e2474a0de932d626eac2322fbfe7a627121638f2beac972c45e01938efae946 |
| `frontier-20261028-1320-forced-264-check.py` | 7dcf4ce407c2e13178db3e774d7c4518aca6364687f208011aba49c6ef79a6a3 |
| `frontier-20261028-1320-forced-264-replay.py` | f9f237d6c1da97124992aba49fd05b73774f0140fc4e7ebc19bb9ad2dc19d640 |
| `frontier-20261028-1320-p24-quota-check.py` | 4b1cb58dbcc836880c501078d8b5137b58bb05019e75730a3671839c252d76bf |
| `frontier-20261028-1320-p24-quota-replay.py` | 5aaee98e8141379e2478477cf1f312a3ed7f756e1eed4b397b64c05f038f9fc6 |
| `frontier-20261028-1320-p44-seed-check.py` | 419611fff1e8f8c9759a7cb30fa6353f58c989e207be33a090b1c5b354727f7f |
| `frontier-20261028-1320-p44-seed-replay.py` | 8aa5e270d1d1c7d9b55913d327360ec1c988fc55bd4dec526757030422edff80 |

The earlier 12-branch Z3 UNSAT observation is not used as a premise and is not a proof certificate. The general border factorization and Sands' theorem are prior literature; no priority or novelty screening is claimed. Acceptance requires a disjoint scientific review of the reduction, both graph-search soundness/completeness and each candidate/prime-balance premise. Historical status/process records are not substituted for that review.

**END OF ORDER-1320 BORDER NONCOMPLETION CANDIDATE.**
