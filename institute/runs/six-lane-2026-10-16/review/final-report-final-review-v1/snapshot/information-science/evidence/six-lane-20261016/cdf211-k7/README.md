# info-1 / cdf211-k7: cyclic (211,7,1) difference family (six-lane run 2026-10-16)

- **Lane owner:** worker `InfoBalanced` until 2026-10-16 23:58 PDT (request-capped); from
  2026-10-17 00:03 PDT worker `InfoCdf211`.
- **Contract:** `institute/runs/six-lane-2026-10-16/screening/info-1-cdf211-contract.json`, recorded
  2026-10-16T23:43:22 PT.
- **File ownership:** every new file is in this directory. The InfoCdf k5 lane, the shared indexes and the
  parent's control folder are read-only.

## Frozen target

Find five 7-subsets of Z_211 whose 210 ordered within-block differences are exactly Z_211 \ {0}. This
gives a cyclic S(2,7,211) with 1055 developed blocks.

- No multiplier or symmetry is part of the target.
- A restricted-model UNSAT, miss, UNKNOWN or timeout is not nonexistence.
- A noncyclic S(2,7,211) would be a separately labelled broader result.

Primary status (parent-attested in the contract):

- Hetman, arXiv:2511.20708v3: "S(2,7,211) is undecided".
- The 2026 prime-power theorem (Chen–Wei–Zhu 2002 lineage) leaves 211 as a possible cyclic exception.
- Chen–Wei–Zhu 2002 methods: not audited here (not accessed).

## Representation, frozen before compute

Multiplier subgroups of F_211^* (cyclic of order 210).

- **Even orders are impossible (proof).** An even-order multiplier group contains −1.
  - A block fixed by −1 can be translated so that B = −B, i.e. B = {0, ±a, ±b, ±c}. For x ≠ −y, the
    difference x − y also equals (−y) − (−x), so it is repeated. Hence no block is fixed.
  - Without fixed blocks, −1 pairs up the 5 blocks, which is impossible because 5 is odd.
- **Odd orders 5, 7, 15, 21, 35 and 105** each contain the order-5 or order-7 subgroup. They are covered
  by those two searches.
- **Remaining classes:** order 3 (orbit types 1+1+1+1+1 and 3+1+1) and no multiplier.
- **Order-7 structure:** with 5 blocks, every block is fixed, so it is a coset c·H7.
- **Order-5 structure:** the only H5-fixed point is 0, so no 7-set is fixed and the blocks form one orbit
  {m^i B}.
- **Order-3 fixed blocks** have the form {0} ∪ aH3 ∪ bH3. The orbits of H3 are {0} and the 3-cosets,
  and a block fixed up to translation can be translated to be fixed exactly because (μ − 1) is a unit.

## Independent verifier and retained controls

- **Verifier:** `code/cdf_tools.py` provides `diff_check`, `pair_check` (develop all blocks; every pair
  covered exactly once) and `corr_check` (auto- and cross-correlation at most 1).
- **Calibration:** both published cyclic (505,7,1) families (Hetman arXiv:2604.04975v1). Blocks are
  parsed from the TeX source: `sources/hetman-2604.04975v1.eprint`, SHA-256 3f453d3f…1e05.
  - Both families: 12 blocks, 504 differences, 6060 developed blocks, 127260 pairs, correlation 1.
  - Mirror, translate and unit-multiple variants are accepted.
  - The element-change, drop-block, duplicate-block and repeated-element mutations are rejected for the
    intended reason.
  - Output: `evidence/verifier-controls-505.json`, all_controls_pass = true.
- **Parent checks:** the parent holds a separate transcription and checker
  (`review/cdf-k7-parent-controls-v1/`). This verifier is a separate implementation.

## Exact restricted-model results

Run 2026-10-16 23:50:35 → 23:56:51 PDT (`code/multiplier_headroom.py` → `evidence/headroom-211.json`).
Primitive root g = 2.

| Ansatz | Exact model | 211 result | Controls |
|---|---|---|---|
| order 7 (radical) | exact cover of Z_30 by 5 translates of D = {2,24,6,21,9,17} (logs of ε^j − 1 mod 30) | **0 solutions, complete.** The Buratti sufficient condition (D distinct mod 6) also fails | Same routine finds and verifies DFs for p = 337, 421, 463. It finds 0 for 127 (consistent with known nonexistence) and for 379. At 43, D is not distinct |
| order 5 (single orbit) | DFS over {0,1,x3<…<x7}: the 21 unordered differences need distinct classes log(d) mod 21 | **0 normalised solutions, complete, 10,045,581 nodes** | Same DFS finds and verifies 8, 12, 40 and 10 normalised solutions for (31,3), (61,4), (101,5), (151,6) |
| order 3, all 5 blocks fixed | exact cover of Z_35 (H6-cosets) by 5 of 1960 candidate blocks {0} ∪ aH3 ∪ bH3 | **0 solutions, complete, 519,577 nodes** | No positive control yet: the p = 337 control hit its 2·10^6-node cap (UNKNOWN). Coset bookkeeping was cross-checked directly (below) |
| order 3, type 3+1+1 | — | **NOT RUN** | — |
| no multiplier | — | **NOT RUN** | — |

Reduction cross-checks (`evidence/reduction-consistency-211.txt`):

- All 1960 order-3 candidates match their direct difference cosets, each with multiplicity 6. All 455
  rejected pairs indeed have repeated differences.
- All 30 order-7 coset blocks cover exactly c + D, each with multiplicity 7.
- The order-5 pair-class predicate agrees with the direct H5-coset test on 200000 random sets. All of
  these were negatives, so this check is weak; the equivalence itself is proved above.

**Consequence (restricted, exact, subject to parent replay).** No cyclic (211,7,1) DF is invariant under:

- a multiplier group whose order is even or divisible by 5 or 7;
- an order-3 multiplier fixing all five blocks.

This says nothing about unrestricted cyclic DFs. A heuristic count predicted about 0.7 order-5 solution
classes, so this miss is unsurprising.

## Next bounded steps (for a fresh worker)

1. **Order 3, type 3+1+1.**
   - Take pairs of disjoint fixed candidate blocks from the 1960 above, reduced up to scaling by
     Z_211^*/H3.
   - For each pair, search B ∋ 0 such that ΔB is a transversal of the 42 H3-cosets left uncovered.
   - Python is too slow for this; use C, numba or SAT. Add a positive control first.
2. **Unrestricted search.**
   - Option (a): a SAT/exact-cover encoding with x_{i,e}, auxiliary pair-difference variables and
     exactly-one per difference; kissat and cadical are installed. Symmetry breaking: 0 ∈ every block,
     1 ∈ block 1 (scaling), and ordered blocks.
   - Option (b): tabu search over 5 × 6 free elements.
3. Audit the Chen–Wei–Zhu 2002 methods before any long run.
4. Add a positive control for the order-3 all-fixed routine: a prime where an all-fixed family exists,
   searched without a cap.

Hashes: `evidence/manifest-sha256.txt` (written 2026-10-16T23:57:37-0700).

## Owner `InfoCdf211`: frozen plan v2 (written 2026-10-17 00:15:30 PDT, before any v2 run)

### R3: order-3 models in compiled code (`code/o3_models.c`)

Frozen source SHA-256 `4fd1bb1e6a6fffaee06dc97ceb2834e583902172712beb033e3628360a65b435`, binary
`bin/o3_models` `3565ead50eea45e1ff7d8486eaddf187a8632206adc934644da32d223a12555a` (Apple clang 17.0.0,
`cc -O2`). Output re-verification: `code/verify_o3.py` (`0484da4c…6d66`) runs `cdf_tools.all_checks` on
every reported family and hashes the canonical family set.

- **H6-classes.** g = least primitive root, cls(d) = log_g(d) mod n6 with n6 = (p−1)/6.
- **Fixed blocks.** {0} ∪ a_1H3 ∪ … ∪ a_mH3 with m = (k−1)/3. The block is admissible iff every class count
  of its ordered differences is 0 or 6, computed directly from the elements.
- **Orbit block.** B with all k(k−1)/2 unordered differences in distinct classes. Each orbit {B, wB, w²B}
  is counted once: if c is the least class of ΔB, the unique c-class pair is moved to {0, g^c} by a
  translation and a power of w.
- **`allfixed p k`.** Dancing-links exact cover of the n6 classes by admissible fixed blocks, with the
  fewest-candidates column chosen first. All solutions are enumerated.
- **`m1 p k f`.** f fixed blocks plus one orbit, with t = f + 3. Enumerate every normalised orbit block,
  then exact-cover the complement by f fixed blocks.
- **`m2 p k`.** Only for f = 2, so t = 5. For every unordered class-disjoint pair {F1, F2}, run a separate
  DFS for normalised B over exactly the 21 remaining classes. This is an independent second method for
  type 3+1+1.
- **`rawB p k`.** Count all B = {0 < x2 < … < xk} with distinct classes. Cross-check: it must equal
  3k × the normalised orbit-block count.

Run order:

1. Same-shape control (61,4,1) type 3+1+1, using m1, m2 and rawB.
2. All-fixed controls without a cap: C at 211 (must agree with the earlier 0), complete at 337, and the
   original Python `order3_all_fixed(337, cap=1)` with no node cap.
3. k = 7 code-path control: m1 at 337 with f = 5, first solutions.
4. Target: m1 and m2 complete at 211, and rawB at 211.

Heuristic: a random-model estimate is about 340 type-3+1+1 families at 211, about 5 classes under
scaling. It is a guide, not a bound. A zero count is a restricted-model miss only.

### Later steps

The unrestricted search (step 3 of the handoff) and the Chen–Wei–Zhu audit (step 4) are frozen in their
own sections before they run.

### R3 results (runs 2026-10-17 00:15:50 → 00:28 PDT; outputs under `evidence/o3/`)

| Run | Result | Check |
|---|---|---|
| control (61,4,1) type 3+1+1, `m1 61 4 2` | 160 families, complete | all 160 pass all three `cdf_tools` checks |
| control (61,4,1), `m2 61 4` | 160 families, complete | identical canonical set to m1 (sha `25be4151…a7ef`) |
| control `rawB 61 4` | 8640 = 12 × 720 normalised orbit blocks | matches m1's 720 |
| control `allfixed 61 4` | 0 | — |
| **independent** control, `bin/indep_full_cdf 61 4 47` (separate C code: all CDFs by exact cover, then filter by x ↦ 47x) | 1,087,552 cyclic (61,4,1) DFs in total; **160** invariant under the order-3 multiplier, all with 2 fixed blocks (type 3+1+1); 0 all-fixed | equals m1 = m2 = 160 and allfixed = 0 (`evidence/o3/indep_full_61_4.json`) |
| k = 7 code path, `m1 337 7 5 5` (5 fixed + 1 orbit) | first 5 families after 876,863 orbit blocks, 127 s | all 5 pass all three checks |
| all-fixed, C, `allfixed 211 7` | 1960 candidates, **0**, complete | agrees with the earlier Python 0 (1960 candidates) |
| all-fixed control, C, `allfixed 337 7` | **14,336 families, complete** (4.07·10^8 nodes, 742.6 s) | **all 14,336 pass all three checks**, 14,336 distinct canonical families (sha `7ef95de5…8962`) |
| all-fixed control, original Python `order3_all_fixed(337, cap=1)`, no node cap | no solution in 30 min (00:16:03–00:46:28); stopped by the owner to free a slot (`py_allfixed_337.KILLED.txt`) | not completed; its candidate count (5488) equals the C count |
| **target, `m1 211 7 2`** | **0 families, complete**: 8,524,260 normalised orbit blocks, 3.29·10^7 nodes, 7.2 s | — |
| **target, `m2 211 7`** | **0 families, complete**: all 326,480 class-disjoint pairs, 7.14·10^8 nodes, 233 s | the pair count matches an independent Python count |
| target, `rawB 211 7` | 179,009,460 = 21 × 8,524,260 | consistent with m1 |

**Consequence (restricted, exact, worker-level; parent replay pending).** The order-3 multiplier group
admits no cyclic (211,7,1) DF of either orbit type, 1+1+1+1+1 or 3+1+1. With the earlier results (even
orders, orders divisible by 5 or 7), every nontrivial multiplier group is excluded: any cyclic (211,7,1)
DF has trivial multiplier group.

- This is still not unrestricted nonexistence.
- [INFERENCE, not checked by a proof assistant] By Burnside, a transitive group of prime degree is
  2-transitive or lies in AGL(1,p). The CFSG list has no non-alternating 2-transitive group of degree
  211. So the full automorphism group of the developed design would then be exactly Z_211.

Heuristic context, not a bound: a random-model estimate from the actual counts is about 150 matching
class sets (about 1200 families, roughly 4 orbits under scaling). Under that model a zero count has
probability of order 1%. For all-fixed, the model predicts about 0.05 orbits at 211, so a zero there was
expected.

### Chen–Wei–Zhu 2002 audit (bounded; 2026-10-17 00:30 PDT)

- **DOI.** 10.1002/jcd.998, J. Combin. Des. 10 (2002) 126–138.
- **Access.** `onlinelibrary.wiley.com` abs and pdf both return HTTP 403. OpenAlex reports
  `is_oa: false`, `oa_status: closed`. The full text is **inaccessible**.
- **Abstract** (OpenAlex record saved as `sources/openalex-cwz2002-jcd998.json`, sha `857f1de9…1dde`):
  - Method: Weil's theorem on character sums.
  - Result: q ≡ 1 (mod 42) suffices, except q = 43 and possibly q = 127, 211, 31^6, and primes in
    [261239791, 1.236597·10^13] with (−3)^((q−1)/14) = 1.
- **What was searched at q = 211 is not determinable** from the accessible text.
- **Related context (read-only k5-lane copy of Hetman–Baicheva–Topalova 2026, p. 114–116).**
  - The same exception list is restated, with 127 settled by Baicheva–Topalova 2019.
  - Their exhaustive algorithm A2 classified (169,7,1), with 4 CDFs, 2 of them having a multiplier of
    order 3, and (175,7,1), with none. Each took about 2 weeks on a 12-core PC.
  - They report no (211,7,1) search.

## U1: unrestricted search, frozen 2026-10-17 01:06:40 PDT (before any 211 production run)

These searchers impose no multiplier and no symmetry. An unrestricted DF satisfies the normalisations
each one uses. All C searchers are deterministic given the seed; the time limit only decides when to
stop. A run that finds cost 0 writes `<prefix>.sol` in the strict `CDF v k` format.

| Producer | Source sha256 | Binary sha256 | Method |
|---|---|---|---|
| `ls_cdf` | `0da0f495…3857` | `387b12bc…f7bd` | Tabu over single-element moves, every move evaluated exactly. Restart from the run best after a stall. Exact 1-block repair (DFS for a block with exactly the uncovered classes) whenever the other blocks are collision-free and cost ≤ repair_max |
| `sa_cdf` | `f954bbef…2da1` | `51562031…62b1` | Metropolis annealing, optionally focused on colliding elements, with geometric temperature cycles |
| `wls_cdf` | `079cb603…84df` | `5a41940c…c121` | Weighted breakout: class weights on \|cnt−1\|, bumped at weighted local minima, scaled by 3/4 every `decay` bumps, with a short tabu |
| `sat_cdf.py` → kissat 4.0.4 | `41099c3a…6b62` | — | CNF: z ↔ x∧x′ pair variables. Exactly one pair per class (sequential counter), at most k per block; 0 in every block, {0,1} in block 0, optional block order |
| `cpsat_cdf.py` (OR-tools 9.15 in the lane `venv/`) | `99081a21…6531` | — | AllDifferent on the 105 classes. Each block starts at its unique smallest circular gap; class 1 is in block 0; blocks are sorted by smallest gap |

Compiler: Apple clang 17.0.0, `-O3 -march=native`. Detached launches go through `code/launch.py`
(`9072c754…1ea7`), which records host time, pid and argv in `<run>/launch-registry.jsonl`.

### Calibration before the freeze

Outputs: `runs/lscal`, `runs/lscal2`, `runs/sat`, `runs/cpsat`. Every `.sol` was checked by
`cdf_tools`.

| Instance (classes) | tabu `ls_cdf` | SA `sa_cdf` | weighted `wls_cdf` | kissat | CP-SAT (4 workers) |
|---|---|---|---|---|---|
| (31,6,1) (15), (91,6,1) (45) | solved in 0.0 s and 0.4 s | — | — | — | — |
| (61,4,1) (30) | 0.0 s | — | — | SAT in 0.3 s | — |
| (101,5,1) (50) | 0.1 s | 0.4 s at T = 0.25 (no solve at T ≥ 0.5 within 20 s) | 0.6 s with decay 50; stuck at cost 1 without decay | UNKNOWN at 120 s | UNKNOWN at 60 s |
| (151,6,1) (75) | not solved in 600 s; best cost 1, 107 cost-1 visits | not solved in 600 s; best cost 2 | not solved in 600 s; best cost 1, up to 333 cost-1 visits | — | — |
| (211,7,1) (105), 60 s probe at 00:33, seed 1 (disclosed: it ran before this freeze) | best cost 4, about 13.7k iterations/s | — | — | — | — |

Reading of the calibration [INFERENCE]:

- SAT and CP-SAT lose to local search by orders of magnitude on these instances.
- Local search stops working between (101,5,1) and (151,6,1). The target (211,7,1) is much harder:
  under the random model, solutions are about 10^-45 of configurations, against 10^-32 for (151,6,1).
- A local-search hit at 211 within this budget is therefore unlikely. Running it is a lottery ticket,
  not an expected result.

Production plan: up to 4 detached `wls_cdf` / `ls_cdf` processes on (211,7,1) with distinct seeds.

- Chunks are at most 3 h, with a `.ckpt` written every 10 min.
- Seeds, argv and host times go in `runs/u211/launch-registry.jsonl`.
- Any cost-0 state is re-verified by `cdf_tools` and byte-replayed from the seed before it is reported.

### U1 outcome (stopped by the owner)

Launched 01:07:45 PDT: `wls` seeds 101 and 102, tabu seed 103, `wls` seed 104.

- Seeds 103 and 104 were stopped at 01:19 after 660 s; best costs 3 and 4.
- Seeds 101 and 102 were stopped at 02:10 after 3721 s, both at best cost 3, with about 5.2·10^7
  iterations each.
- No cost-0 state was reached. Logs and registry are in `runs/u211/`.
- They were stopped because the exact search X1 below has measurably better prospects.

## X1: exact search per prescribed first block, frozen 2026-10-17 02:11:10 PDT

**Producer.** `code/xr1_v1.c`, SHA-256 `20e4fc8c4e07bf7e33ce3b57387f68da3a2fc3dcfb5aaa0a43148d76d29f5365`.
Binary `bin/xr1_v1`, `4b395c7722728b2226b5a80119cbb677237d84c882e23f74745350d5a23e41b3`. Built with Apple
clang 17, `-O3 -march=native`.

**Classes.** Index the ± classes by Z_n, n = 105, via cls(d) = log_2(d) mod 105. Scaling by 2^r rotates
class sets by r. A cyclic DF is the same thing as a partition of Z_105 into five realizable 21-sets
(class sets of 7-subsets), together with a block for each set.

**Normalisation.**

- Every DF is equivalent under scaling to one in which some block's class set R1 is in canonical
  rotation: the lexicographically least rotation, which contains 0.
- R1 is enumerated by a DFS over blocks {0,1,x3<…<x7}. Mirrors {B, 1−B} are deduplicated. The DFS index
  numbers the canonical R1 that pass the single-block bound.

**Search for each R1.** It is complete. It finds every exact cover of Q = Z_105 \ R1 by four realizable
sets:

- Bitset DFS over blocks {0, g^c, …} enumerates every realizable set in Q.
- The branching class is always the lowest uncovered class.

**Pruning.** The pruning is only a necessary condition, so it is safe:

- For a DF, Σ_i |B̂_i(s)|² = 34 for all s ≠ 0.
- Since every term is ≥ 0, every subfamily (single blocks, pairs with R1, and 3- and 4-block partial
  families) must have spectral sum ≤ 34 + 10^-3.
- A control switch `XR1_NOSPEC` disables all pruning.

**Output.** One `R1 idx=…` line per completed R1. This is the checkpoint, and runs resume at idx+1.
Each solution is a `SOL` line with all five blocks.

**Validation** (`evidence/xr1/`, rerun with the frozen binary; the counts are filled in below once the
rerun completes):

- **(61,4,1), all 109 canonical R1.** Independent `validate_xr1.py` (`d77e3f40…cff3`, no shared code):
  - It enumerates all class partitions (33,986) by its own exact cover.
  - It reproduces 1,087,552 DFs, the same count as the independent C enumeration `indep_full_cdf`.
  - Per-R1 solution counts match exactly: 5703 incidences, 0 mismatches.
- **(101,5,1), first 300 R1.** 2476 solutions. A sample of 300 passes all three `cdf_tools` checks.
  Identical counts across the code revisions.
- **(151,6,1), planted control.** The input is the block {0,1,12,33,83,90} of a known H5-invariant family.
  - xr1 finds 8 families containing that block's class set. All 8 pass all three checks, and the
    planted family is among them up to scaling.
  - `XR1_NOSPEC` on the same R1 gives the same 8, so the pruning lost nothing.
- **(127,7,1).** 63,757 canonical R1. A 600 s partial run (41,711 R1, earlier build) found 0, consistent
  with the published nonexistence.

**211 probes before this freeze (disclosed).**

- Earlier builds ran R1 idx 0–11 with 0 solutions. Per-R1 enumeration took about 2.2 s, and search
  took 0.1–26 s, rising steeply as the R1 spectral peak falls: peak 34 gives nsets 1.6·10^4, peak 32.6
  gives 1.1·10^6.
- Two detached probes with peak caps 28 and 30.5 are running from 02:10:14 (`runs/xr1probe/`).

**Heuristic yield [INFERENCE, random model, not a bound].**

- The measured realizable-set density gives about 1.2·10^9 realizable class sets, about 5.8·10^3 DF
  class partitions, about 55 scaling orbits, and about 2.7·10^-5 solution incidences per canonical R1.
- The same model predicted 8.6 per R1 for (101,5,1); 8.8 was observed.
- For (151,6,1) it predicts about 0.3 per R1, but 0 were seen in the first 32 R1 (earlier build). So
  the model may overestimate at t = 5.

**Plan.**

- Run ≤ 4 detached `xr1_v1` processes over disjoint DFS index ranges, in ≤ 3 h chunks with
  `maxsec=10800`, logged in `runs/x211/launch-registry.jsonl`.
- A peak cap is chosen from the probes. Covered R1 are listed exactly in the logs; SKIP lines list the
  uncovered ones.
- Any `SOL` line is checked with `cdf_tools`, written as `certificates/cdf_211.txt`, byte-replayed, and
  reported immediately.
- A complete per-R1 search with no solution is an exact restricted result: no cyclic (211,7,1) DF
  contains a block whose class set is a rotation of that R1. It is not nonexistence.

### X1 v2 and calibrated cost model (2026-10-17 02:25 PDT)

**v2.** `code/xr1_v2.c` `e6f466be…db46`, binary `bin/xr1_v2` `e847c534…51ab1`. The only change from v1:
the second-to-last block is found by a bitset DFS inside the remainder instead of a bit-slice scan.

- On (61,4,1) all R1, (101,5,1) first 300 R1, and (151,6,1) planted, the per-R1 statistics and the SOL
  lines are byte-identical to v1.
- All 2476 + 8 SOL families pass all three `cdf_tools` checks (`evidence/xr1/v1_verify_101_151.json`).
- On 211 R1 idx 36, v2 searches in 114 s against v1's 174 s.

**R1 census at 211** (`xr1_v1 211 7 count`, 50 s): **22,515,491** canonical R1 pass the single-block
bound. The peak histogram, in half units, runs from 18.0 to 34.0, with mode about 26.5; about 61% have
peak ≤ 28.

**Yield model, compatible-pool form.** The expected number of solutions for a given R1 is about
#partitions(Q into 4 sets) × (nsets / C(84,21))^4.

- Calibration on (101,5,1), first 300 R1, by peak quartile: predicted 13.7 / 3.5 per R1 against observed
  12.05 / 3.03 (low / high quartile).
- At 211: nsets 2.15·10^6 (peak 30.2) gives about 4·10^-7 per R1. nsets 4·10^6 gives about 5·10^-6, and
  nsets 8·10^6 gives about 8·10^-5.
- Search cost grows at least quadratically in nsets: about 2 min at peak 30, and over 15 min at
  peak ≤ 28 (probes still running).
- **Consequence [INFERENCE].** At these rates, the expected number of solutions within this lane's
  remaining budget (about 3 processes × 35 h) is of order 10^-3 to 10^-2. The expected cost of one
  solution is of order 10^5 core-hours.
- The earlier global-density estimate (2.7·10^-5 per R1 on average) used independence between blocks.
  Measured realizable sets avoid a fixed realizable set only about half as often as random 21-sets do,
  so that estimate was optimistic.

## Wrap-up status (2026-10-17 02:35 PDT, owner InfoCdf211; request budget reached)

- **No candidate.** There is no `certificates/` directory. Across every 211 run, the number of `SOL`
  lines is 0, and no cost-0 local-search state was reached.
- **No lane process is running.** The probes pk28 and pk21_v2 were stopped at 02:35; registries are in
  `runs/*/launch-registry.jsonl`.
- **Complete X1 searches at 211 (each R1 searched completely, 0 solutions):**
  - DFS idx 0–11 (earlier builds with the same algorithm).
  - idx 36 (pre-freeze build, and again with frozen v2).
  - idx 61, with peak 27.74, nsets 3.54·10^6, l3 1.07·10^7, 910 s (pre-freeze build).
  - Total: 14 of the 22,515,491 canonical R1. This is a negligible exclusion and not nonexistence.
- **`code/xr1_v3.c` is an UNFINISHED DRAFT.** It switches to int8 quantised spectra with floor-based
  safe pruning, to cut memory 4×. It was never compiled, validated or run, and it is not a producer.
- **Exact restricted results stand.** They are the R3 table and its consequence: every nontrivial
  multiplier group is excluded. Parent replay is pending.
- **Concrete next representation** (needs cluster-scale compute):
  - Use X1 (`xr1_v2`, validated), prioritising low-peak R1. Calibrated yield is ≈ 3·10^-6 per peak-28
    R1 at about 15 min each, so the expected cost is ≈ 10^5 core-hours per solution [INFERENCE].
  - First finish v3 (memory), MRV class ordering, and intra-R1 progress or resume at L2 granularity.
  - Then distribute disjoint DFS index ranges over many cores.
- **Alternative, separately labelled broader target.** A non-cyclic S(2,7,211) via other automorphism
  groups (Hetman-style). It is not a substitute for the frozen cyclic target.
