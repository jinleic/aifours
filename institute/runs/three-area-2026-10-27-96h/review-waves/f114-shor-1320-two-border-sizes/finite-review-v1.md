# f114 Shor 1320: independent finite review

Clock observed before this report: **2026-10-28T19:41:09-0700 PDT**. Review is limited to the frozen f114 inputs and the finite, necessary-condition calculations specified in the manifest.

## Disposition

**Finite-slice verdict: no FATAL, MAJOR, or MINOR defect found.** The retained packing, all stated residue witnesses and capacity bounds, both Hall counts, and the 91,125-seed relaxed obstruction reproduce. The endpoint, conditional on the stated mathematical dependencies, is `( |P|, |Q| ) ∈ {(24,55),(44,30)}`. This is a review of the enumerated finite premises and their one-sided implications, **not an independent proof of the border-factorization theorem or a scientific acceptance of the full chain**. The theorem-level conclusion remains dependent on those general results; this review alone is INCONCLUSIVE as a stand-alone proof of the border theorem or of any order-1320 exclusion.

The 80-element P witness realizes an upper bound for the **one-sided old-anchor gcd screen only**; it is not a P/Q tiling. No feasibility claim is made for either surviving cardinality pair. In particular, these data are not an all-conditions border solver, a finite-code solver, a completion, or a noncompletion result. No human, independent-model-family, formal/kernel, peer, or novelty clearance is claimed.

## Source binding and execution

The manifest was read first and hashed as `ad3f0ad3e4a7d80afa037fe238e791f267d993ba0c0cbf8945abe72224c30eaf` (5,366 bytes, 95 LF). Before reading the listed bodies, every source's complete SHA-256, byte count, and LF count was checked against it; every body was then read fully in its declared order. The independent program rechecked the same pins and read the packing JSON as data only. It did not import or execute any author checker.

| # | Manifest input | SHA-256 | bytes / LF |
|---|---|---|---:|
| 1 | Original code definitions | `12db546b559de7db391bdc3755b02e391296852b3d188532d8a90dc483686bc9` | 2633 / 40 |
| 2 | Actual border factorization and prime balance | `56fd2cff931af2da61e2f8a17c513d8af5c3cc8064c9d9ed66c5c361fb3a6051` | 9229 / 114 |
| 3 | Divisor-disjointness and packing | `228757d547c671685c9e2c1b58332b6e8615b15dc9f7db9b49814591dd072b23` | 5532 / 62 |
| 4 | Packing witness JSON | `eb73d65b4e9d2f79b917e4da2d390cd157388341bb75e5c5049a914cf6ef39cb` | 2081 / 1 |
| 5 | Packing author checker, read only | `937a789eba003c735dd6e0b72dc7c6967058d9b4417a48d9d9b8a9689567dfc6` | 2027 / 36 |
| 6 | Four-border deduction | `3d93c233bc6ea6802a797564edf0c18e21de2215dbf85c70136bad4556399c3e` | 6566 / 85 |
| 7 | Three-border deduction | `9f2835c4f7e55eb909b342ed96d95f9c543ce7e169d9d0e865a19fc641a9d461` | 4263 / 46 |
| 8 | Two-border candidate | `0e2474a0de932d626eac2322fbfe7a627121638f2beac972c45e01938efae946` | 5512 / 54 |
| 9 | Author prime-residue control, read only | `fd5bb126e37396ec73681954c9e67205ed8c1ffaa4b8e62d8cf454612181068d` | 1753 / 32 |
| 10 | Author Hall control, read only | `715b325871c8148c1d62647e4925fca1edc23a4a9e71840bd41a6250b59404b6` | 1522 / 33 |
| 11 | Author forced-gcd control, read only | `7dcf4ce407c2e13178db3e774d7c4518aca6364687f208011aba49c6ef79a6a3` | 2931 / 53 |
| 12 | Author alternative forced-gcd control, read only | `f9f237d6c1da97124992aba49fd05b73774f0140fc4e7ebc19bb9ad2dc19d640` | 2030 / 36 |

The one observed independent run was `python3 -B finite-check-v1.py`, in this directory; it exited 0. Native `/bin/date` read at start was **2026-10-28T19:39:48-0700 PDT** and immediately before receipt creation **2026-10-28T19:39:49-0700 PDT**; monotonic elapsed time was 1.302 s. The standard-library checker is `finite-check-v1.py`, SHA-256 `a2ae6d6e97ee7f7ddc509f56e0572e822c1b9f8dea2b313c363324720e1c43a5`. Its exclusive-create output `finite-receipt-v1.json` has SHA-256 `a6ee2cef60ad25eb7b5862788ee05035cfb22edbeb752059727514afa72ef9f9` (28,509 bytes, 1,783 LF). The receipt contains the entire generated P/Q candidate sets, complete Hall histograms and minimizers, residue witnesses, seed pools, controls, all input pins, interpreter version, and timing.

## Exact integer reconstruction

Take `n=1320`, `A={0,3,8,11}` and `Y={0,1,7,13,14}`. Enumerating gcds of distinct anchor differences gives `G_A={3,5,8,11}` and `G_Y={1,2,6,12}`. The reconstructed P candidate universe consists of all residues avoiding `G_Y` against A, except equality with an anchor; the Q universe is defined dually using `G_A` against Y. Exact universe sizes are **112 and 286**.

The pinned witness supplies 16 disjoint P conflict triangles (48 vertices), each pair having gcd in `G_Y`, so `|P| ≤ 112−2·16=80`. Its Q groups are a disjoint and complete partition of all 286 candidates into **130** nonempty conflict cliques: 36 singletons, 55 pairs, 18 triples, 19 quadruples, and two quintuples. Thus `|Q| ≤ 130`. The retained 80-element P witness contains all four anchors, has distinct in-range candidate residues, and every pair avoids `G_Y`; its full list is in the receipt. No Q clique-bound sharpness is asserted.

With `|P||Q|=1320`, the packing alone leaves P sizes `{11,12,15,20,22,24,30,33,40,44,55,60,66}`. The mod-11 balance and the two old P anchors in one class remove 11. The simple mod-3 and mod-5 bounds remove 30, 33, 40, 55, 60, and 66, leaving `{12,15,20,22,24,44}`; the P15 and Q22 tests below leave `{12,20,24,44}`.

### Residue capacities and witnesses

- The 12 candidate P residues congruent to 1 mod 3 are `88,253,256,415,418,583,748,913,916,1075,1078,1243`. The four disjoint forbidden pairs are `(88,916),(256,748),(253,415),(583,1075)`. Exhausting all their subsets gives exact one-sided independence maximum **8**, uniquely attained by `{88,253,418,583,748,913,1078,1243}`. This also verifies the claimed upper bound of eight.
- The P candidates congruent to 2 mod 5 are `{132,407,792,872,987,1067}`; those congruent to 4 mod 5 are `{264,344,459,539,924,1199}`. Each six-element set is independent for the old-anchor P gcd screen; its exact one-sided capacity is six.
- For P size 15, prime balance would require five candidates in mod-3 class 1 and at most one of those in mod-5 class 3. There are exactly **eight** five-subsets satisfying just those cardinalities. All eight fail the forbidden-pair test; equivalently the four outside mod-5 class 3 are forced and each of the other eight candidates conflicts with one of them. The eight literal subsets and blocking edges are in the receipt.
- Q has no candidate `4 mod 6`. For each mod-5 class 1, 2, 3, exactly ten Q candidates are not `1 mod 3`, four of the ten odd; each supplied set of four disjoint pairs is indeed gcd 5. Exhaustive subset checks give exact gcd-5 independence maximum **6** in each class, with unique respective maximizers `{276,386,716,936,1046,1266}`, `{62,282,612,722,1052,1272}`, and `{68,288,398,618,948,1058}`. The same maxima hold under all four forbidden anchor gcds. These are candidate-screen witnesses, not Q factorizations.
- For Q size 60, mod-3 and mod-5 balance would give 20 in class `1 mod 3` and 12 in each mod-5 class. The ten-element capacities force at least six `1 mod 3` elements in each of the three classes. They are odd, and any fixed `(mod 5, mod 6, mod 11)` has at most four representatives modulo 1320, so at least two have different mod-11 residues. An even selected non-`1 mod 3` element in the same mod-5 class would then have gcd difference 5 with at least one of them. Hence at most the four odd candidates can be selected outside `1 mod 3`, forcing at least eight such elements in each of three classes, contradiction `24>20`. This is the Q22 exclusion, relying on the stated balance and gcd-disjointness premises.

### Q=110: exact two-class Hall calculation

After removing the mandatory anchors 0 and 14, the two candidate classes `0 mod 11` and `3 mod 11` contain **25 vertices each**. An edge is exactly a cross-class pair whose gcd difference is 3, 5, or 8; the independently reconstructed graph has **217 edges**. The checker enumerated non-neighborhood intersections (rather than importing an author program):

| Orientation | subsets | minimum neighborhood | minimizers |
|---|---:|---:|---:|
| 9 from the `0 mod 11` side | 2,042,975 | 18 | 11 |
| 8 from the `3 mod 11` side | 1,081,575 | 17 | 10 |

For example, `{55,264,330,385,594,660,924,1045,1254}` attains the first minimum. Uniform Q balance requires nine non-anchor vertices on **each** side: any nine on the first side leave at most seven unblocked vertices on the second. The reverse count independently gives at most eight unblocked first-side vertices. Either eliminates P size 12, assuming the common tiling and balance premises.

### P=20, Q=66: forced gcd 264 and relaxed seed search

The exact six-pair matching between the two P mod-5 classes is `(132,924),(407,1199),(792,264),(872,344),(987,459),(1067,539)`; all differences have gcd 264. All **225** choices of four from each class contain a matching edge. As a positive threshold control, among **400** choices of three from each class, **20** avoid all six edges; one is `{132,407,792}` versus `{344,459,539}`. P size 20 and mod-5 uniformity force four in each class and therefore a P difference of gcd 264.

For the Q side, under the temporary assumption of no gcd-264 difference, all Q candidates `1 mod 3` are odd, and two in the same `(mod 11, mod 8)` slot necessarily differ by a nonzero multiple of 264 and hence have gcd 264 with 1320. There are 116 such candidates in **44** slots: eight singleton slots and 36 slots of size three. Every slot therefore contributes at most one. Q size 66 and prime balance require 22 elements `1 mod 3` and six elements in each mod-11 class. In each of classes 1, 2, 7, at least two of those six must be non-`1 mod 3`; the candidate pool in each class has size ten. Every potential Q therefore contains at least one of the `C(10,2)^3=91,125` six-element seeds.

| Stage | Exact count |
|---|---:|
| All seeds | 91,125 |
| Seeds compatible pairwise and with old anchors for gcds `3,5,8,11,264` | 1,143 |
| Compatible seeds with fewer than 22 seed-compatible open slots | 1,089 |
| Remaining seeds failing at least one class-1/2/7 six-element quota | 54 |
| Residual seeds | 0 |

The complete open-slot histogram for the 1,143 is `{6:36, 7:34, 14:4, 16:18, 17:132, 20:865, 26:54}`. For example, seed `[89,419,288,618,282,612]` opens 26 slots, yet the upper bounds for total Q elements in classes 1, 2, 7 are respectively 7, 5, 5. The quota computation counts every still-individually-compatible non-`1 mod 3` candidate and every open `1 mod 3` slot. It deliberately ignores conflicts among those extras, between extras and slot occupants, and the possible gcd-264 conflicts between slot occupants and old anchors. Thus it can only **overcount** what an actual Q could supply; rejection is sound in that direction. The argument exhausts seeds for these necessary conditions, not all UD or factor-completeness conditions, and it does not search the two surviving border cases. Under the imported divisor-disjointness premise, Q's forced 264 contradicts P's forced 264, removing P size 20.

## Controls and sensitivity

All controls were exercised within the same single program run; arbitrary exceptions were not counted as expected rejections.

- Positive tiling: `P={0,2,4}`, `Q={0,1,6,7}` directly and uniquely tile `Z_12` and have disjoint nonzero gcd-difference classes. Replacing Q element 7 by 8 gives the intended `TILING_NOT_DIRECT_COVER` rejection.
- A one-byte in-memory flip of the packing input produces `SOURCE_SHA`. Duplicating a vertex in a P triangle produces `P_TRIANGLE_DUPLICATE`; removing a Q clique member produces `Q_CLIQUE_COVERAGE`; duplicating a P80 witness vertex produces `P80_DUPLICATE`.
- A positive 4-by-4 identity graph has six 2-subsets with exactly two neighbors. Removing one edge changes the histogram to three with one neighbor and three with two. On the actual 25-by-25 graph, removing the single edge incident to right vertex 47 from the first minimizing 9-subset lowers its neighborhood from 18 to 17 and produces the intended `HALL_NEIGHBORS` rejection.
- Mutating matching pair `(132,924)` to `(132,264)` gives `P264_GCD`. The 3+3 positive pigeonhole case above shows that the four-per-class threshold matters. Dropping the P15 conflicts leaves the eight relaxed five-subsets, whereas applying them leaves zero.
- Seed `[89,386,288,948,612,1272]` passes the compatibility screen; a duplicated member gives `SEED_DUPLICATE`, while replacing 89 by 705 gives `SEED_CONFLICT`. For all 54 quota rejections, the recorded upper bounds are at least 2, so relaxing the required class size from 6 to 2 would let all 54 through that quota stage. Neither the accepted seed nor this artificial relaxation is a Q solution.

## Dependencies and interpretation

The finite deduction needs the **same actual D** to give a direct P+Q tiling with the displayed anchors and `|P||Q|=1320`; it needs the prime-balance implication for primes 3, 5, 11 occurring to the first power; and it needs nonzero gcd-difference classes of the two actual tiles to be disjoint. The frozen border packet presents guarded-factor and UD arguments for the first and cyclotomic reasoning for the second; the divisor packet presents a unit/cyclotomic argument for the third. These general mathematical steps are dependencies of the finite replay, not consequences of its enumeration. The linked source [Cordero, Theorem 1.1](https://arxiv.org/html/2301.13566v1) states the classical actual `a^k b^+` / `b^+ a^k` border factorization for finite maximal codes containing `b,a^n`; [Kiss–Londner–Matolcsi–Somlai, Theorem 2.1](https://arxiv.org/html/2411.03854v3) states the Sands divisor-class criterion. These direct cited-source reads are not a novelty or literature-status search. No held mathematical output was used as a premise, no older review was changed, and no contact, external-model call, Git operation, deletion, or publication was performed.
