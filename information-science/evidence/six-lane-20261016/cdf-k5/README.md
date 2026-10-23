# Lane info-2 replacement: cyclic (v,5,1) difference families, v in {321,501,621,681,801,901}

Owner: worker `InfoCdf`. Parent run: `institute/runs/six-lane-2026-10-16` (contract.json; transitions.json entry
`info-2`, frozen 2026-10-16T22:08:23-07:00). Lane opened 2026-10-16 22:08:48 PDT (host clock).

## 1. Frozen contract (written 2026-10-16 22:15 PDT, before any target search)

### Exact target
For each v in {321, 501, 621, 681, 801, 901} (smallest first), construct n = (v-1)/20 base blocks B_1..B_n, each a
5-subset of Z_v, such that the multiset of ordered differences {b - b' : b != b' in B_i, 1 <= i <= n} contains every
nonzero residue of Z_v exactly once. Equivalent forms: perfect (v,5,1) optical orthogonal code; strictly cyclic
S(2,5,v). n = 16, 25, 31, 34, 40, 45 respectively. Each v is a separate finite claim.

Not the target: S(2,5,v) without the cyclic condition (classical existence), relative/almost difference families,
OOCs that miss a difference class, families over a non-cyclic group of order v.

### Sources (local copies, SHA-256 in `sources/SOURCES.md`)
- Abel, Costa, Finizio, Discrete Appl. Math. 143 (2004) 43-53, Section 3 and Theorem 14 (academia.edu reader text;
  the extraction renders the set-exclusion sign of Theorem 14 as "∈"; the sense is "v not in").
- Hetman, Baicheva, Topalova, J. Algebra Comb. Discrete Appl. 13(1) (2026) 111-119, Section 1, p. 114: "A (20t+1,5,1)
  CDF exists for 1 <= t <= 50 except possibly for t = 16, 25, 31, 34, 40, 45 [2]".

### Baseline
All v = 1 (mod 20), v <= 1001 have a cyclic (v,5,1)-DF except possibly these six (ACF 2004 Thm 14, restated 2026).
ACF 2004 found unstructured ("Type 1") families only for v <= 221 and used multipliers of order 2, 3, 5 (or q^2
structure) above that. No construction for any of the six is known to this lane at freeze time; a priority audit
is a separate gate (Handbook 2nd ed. tables, Baicheva-Topalova data page, forward citations) owned by the parent.

### Acceptance gate (per v)
1. `certificates/cdf_<v>.txt` in the strict format of `code/verify_cdf.py` (header `CDF v k`, then exactly n lines
   of k distinct integers in [0,v), single spaces, LF, nothing else).
2. `code/verify_cdf.py` (stdlib only, written from the definition, no import of search code) exits 0 with all of:
   block count, range/distinctness, exact ordered-difference multiset = Z_v\{0} once each; cross-check A: cyclic
   development covers every unordered pair of Z_v exactly once; cross-check B: binary-sequence periodic auto- (nonzero
   shift) and cross-correlations all <= 1.
3. SHA-256 recorded here; the same verifier rejects every negative control for the intended reason.
4. Parent notified with path, SHA-256 and checker output. Parent independent verification and cross-vendor hostile
   review are parent gates, not claimed by this lane.

### Controls (all fixtures retained under `controls/`)
- Positive: ACF 2004 explicit families v = 81, 121, 141, 161, 201, 221 (Type 1) and multiplier-expanded families
  (order 2: 261; order 3: 381 and others; order 5: 341; q^2: 361), expanded by a separate builder script.
- Negative (per positive family): one changed element; elements swapped between two blocks; a duplicated difference
  (a block replaced by a translate of another block); wrong v in header; plus format faults (duplicate element,
  out-of-range element, missing/extra block, bad header, stray whitespace).
- Validity-preserving mutations (must be accepted): translate a block, negate a block, reorder blocks.

### Attack and compute plan
- Exact arithmetic multiplier analysis per v (`code/multipliers.py`): unit-group element orders, fixed-class counts,
  admissible fixed-block types, counting conditions; recorded in `evidence/multipliers.md`.
- Searches in compiled C (own code): tabu / annealing local search on the collision count of difference classes
  (plain and multiplier-prescribed orbit representatives), randomized exact-cover completion; SAT (kissat/cadical)
  as a secondary encoding. Calibrate first on known orders (221, 261, 341, 381, ...).
- Limits: at most 4 concurrent CPU processes, <= 8 GiB RSS, every run writes a checkpoint (seed, iteration, best
  state) at least every 30 min, no single chunk over 3 h. Seeds, commands, versions and runtimes in `evidence/`.
- Claim discipline: a search miss/timeout is not nonexistence; a found family is a finite existence certificate
  only; novelty and significance are separate, parent-owned gates.

## 2. Per-v status (updated 2026-10-17 00:15 PDT): all six FOUND
| v | n | status | certificate SHA-256 | producer / replay |
|---|---|---|---|---|
| 321 | 16 | FOUND 23:15:55 PDT; parent stdlib + cross-vendor checkers VALID | `0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b` | `cdf_hyb3p 321 1 1700 <p> 1 20000 50000000 evidence/gpairs/gpairs_p107_k30.txt`; byte replay OK |
| 501 | 25 | FOUND 22:59:50 PDT; parent checkers VALID | `517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74` | `cdf_inv3p 501 1 1700 <p>`; byte replay OK (`evidence/v501/REPLAY.md`) |
| 621 | 31 | FOUND (.sol written 23:32:11 PDT); parent checkers VALID; parent seed replay identical | `257d85f25cd85afc06f6762f1a8f7d4f72e37cbfde806927838f1ac6b7ae05f5` | `cdf_mq2 621 27 1 1700 <p> 30 3 50000000` (Z_27 x Z_23; 9 stable + 11 free pairs); byte replay OK (`evidence/REPLAYS.md`) |
| 681 | 34 | FOUND 23:23:23 PDT; parent checkers VALID | `16af75391a6b01bd6fc7ee8ec45bd3b53396bd72403e667297af89c1dc09f7b7` | `cdf_hyb3p 681 1 1700 <p> 1 20000 50000000 evidence/gpairs/gpairs_p227_k5.txt`; byte replay OK |
| 801 | 40 | FOUND (.sol written 23:41:08 PDT); parent checkers VALID; lane + parent known-source replays identical | `0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c` | `cdf_mq4 801 9 21 1700 <p> 30 0 30000000 5000000 1` (Z_9 x Z_89; 20 stable + 10 free pairs). Original-run source bytes not preserved; frozen source 68028470... / binary b1f56985... replay identical (`evidence/v801/PROVENANCE.md`) |
| 901 | 45 | FOUND (.sol written 23:57:41 PDT); parent checkers VALID; lane byte replay identical 2026-10-17 00:14:19 PDT | `06bd6ae8b5349d8e2b1b11aae3be9297abcc46af9858c4370d0a98f8a8ee56d3` | frozen `cdf_mq4` (68028470... / b1f56985..., launched 23:42:00 after the freeze): `cdf_mq4 901 17 41 1700 <p> 30 -11 30000000 5000000 0`, attempt 21, 940.2 s (Z_17 x Z_53; 11 stable + 17 free pairs, 6 random + 11 by exact cover). Replay: `evidence/v901/replay/` |

Alternate witnesses (lane verifier ACCEPT, not the pinned certificates): `evidence/v501/cdf_501_alt_seed2.txt`
(fd1f9a65...), `evidence/v321/cdf_321_alt_seed2.txt` (a71174db...), `evidence/v321/cdf_321_alt_seed3.txt`
(789bc79b...), `evidence/v681/cdf_681_alt_seed2.txt` (f21fd866...).

### How the three were found (Z_v = Z_3 x Z_p, p = 107, 167, 227)
- Exact analysis (`code/multipliers.py`, `evidence/multipliers-targets.{txt,json}`): no element of prime order in
  Z_v^*/{+-1} can map the family to itself up to translation and negation for v = 321 and 681 (the order-2 unit
  mu = (1 mod 3, -1 mod p) fails: every class of 3Z_v is mu-fixed, a pigeonhole on residues mod 3 puts a fixed class
  in every block, and the fixed-class counting has no solution); odd orders fail by orbit counting. For 501 the same
  mu admits a structure in which every block has a mu-stable difference multiset (20 + 4 + 1 blocks).
- Key representation: the classes of Z_3 x Z_p split into p-1 "orbit items" pairs {[(1,y)],[(1,-y)]}, (p-1)/2 pure
  classes [(0,y)] and [(1,0)]. Blocks T1 = {(0,0),(1,+-y1),(2,+-y2)} cover 4 orbit items + 2 pure classes;
  T3 = {(0,0),(0,f1),(0,f2),(1,y),(2,y)} covers 3 + 3 + [(1,0)]; T5 = 5 points of {0} x Z_p covers 10 pure classes.
  Stage A: exact cover of the orbit items by T1 quadruples (dense: ~e^45 covers for p = 167); stage B: exact cover of
  the leftover pure classes by T5 quintuples. For p = 167 the counts close (20 T1 + 1 T3 + 4 T5, `code/cdf_inv3p.c`).
  For p = 107, 227 the orbit count is 2 mod 4 off; two general blocks of shape {(0,0),(0,u2),(0,u3),(1,w1),(1,w2)}
  whose 12 mixed differences are jointly closed under negation absorb 6 orbit items (`code/gpairs.c` enumerates such
  pairs; `code/cdf_hyb3p.c` mode 1). This is a representation choice, not a restriction proven necessary.
- In 501 the unit 166 maps 20 blocks to themselves and 5 blocks to their negatives: difference-multiset stable under
  166, but 166 is not a multiplier in the Hetman-Baicheva-Topalova Definition 1.2 sense (parent audit agrees).

## 3. Log
- 2026-10-16 22:08:48 PDT lane created; sources saved 22:10-22:12 PDT.
- 22:17-22:18 controls: 24 ACF 2004 families ACCEPT; 117 mutations REJECT for the intended check; 36 validity-
  preserving mutations ACCEPT (`evidence/controls-receipt-v2.json`, verifier sha 7fa0ee83...).
- 22:20-22:50 plain searches (tabu `cdf_ls`, focused walk `cdf_walk`, random prefix + exact cover `cdf_xc`/`cdf_dlx`,
  Z_3-lift `cdf_lift`) solved calibration orders <= 201 but not 321 (tabu reached cost 1 only; 10k r=7 completions
  and 5 r=8 completions found nothing; projected lift LS stalled at cost 1). Logs under `runs/`.
- 22:59:50 501 found (structured stage A/B); 23:15:55 321 found; 23:23:23 681 found (hybrid with general pair).
- 23:32:11 621 found (`code/cdf_mq2.c`: Z_m x Z_q stable blocks first, then exact cover of the last free pairs).
- 23:41:08 801 found (`code/cdf_mq4.c`, same method plus an optional label-class feasibility filter).
- 23:43 stretch target (211,7,1): sources saved under `stretch-211-k7/sources/` (Hetman arXiv:2511.20708v3 PDF
  e800419f..., abstract page 40259c20...); no contract frozen and no search run. Target transferred by the parent
  to worker InfoBalanced (lane cdf211-k7); this lane will not search it.

## 4. Limits
- Each certificate is a finite existence witness for one v; no general construction is claimed. Priority/novelty is
  the parent's audit (review/cdf-k5-priority-audit.md); significance is not assessed here.
- The structures used (Z_3 x Z_p labels, stable blocks, jointly closed general pairs, free pairs) are search
  representations. Their failure for 901 so far says nothing about existence.
- Calibration claims are empirical; the expected-solution estimates in the logs are heuristics, not bounds.
- 2026-10-16 23:54:37-23:55:32 901 cycle 1 stage 1 (`code/defect13.c`): exhaustive exclusion of "3 orbits of 13
  blocks under the order-13 subgroup + 6 further blocks" (all 46376 choices, `evidence/v901/PLAN-cycle1.md`).
- 23:57:41 901 found by the frozen `cdf_mq4` mu-route run (seed 41); cycle 1b runs stopped (counts in the plan file).
