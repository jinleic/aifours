# PA(19,8,6) conditional proof map v2 (PA19FinalBridgeDesk; draft for hostile review; v1 = PROOF-MAP.md, superseded)

Written 2026-10-18 01:48-01:55 PDT from static reading only. NOT a verdict and NOT parent acceptance. Every
statement is conditional on the trust base in section 10. Paths are lane-relative (LANE = information-science/
evidence/six-lane-20261016/packing-array19) unless prefixed `review/`. In the snapshot, lane files are under
`snapshot/lane/`, review files under `snapshot/review/`, the frozen contract under `snapshot/run/screening/`,
supplements under `snapshot-supp1/` and `snapshot-supp2/`.

Pinned inputs: `cycle2/m1-complete-candidate-20261018T012523.json` sha256 cf3e87c5...d791 (label "M1-complete finite
nonexistence candidate; NOT parent final acceptance"), `STATUS15.json` b0dac6b0...45f3, `README.md` 7eb046e1...e60.
At the pin: M1 counts all 5577 A2 cases and all 486 E0 graphs UNSAT; M2 counts 486 E0 + 5411/5577 A2, 166 open.
A complete M1 is the producer's candidate, NOT the final gate (the gate also needs independent M2 + parent audit).

## 0. Target and the "exact 18" corollary

* Valid array: 19 x 8 over 6 symbols, every two rows agree in at most one column (equivalently no ordered symbol
  pair repeats in any two columns; equivalently a length-8 code over 6 symbols with minimum distance >= 7, i.e.
  A_6(8,7) >= 19). Contract: `run/screening/info-1-packing-array19-contract.json`.
* Lower bound 18: `data/cpro1-pa-18-8-6.txt` (CPro1), verified by `src/verify_pa.py` (row pairs) and
  `src/verify_pa2.c` (column pairs); mutation controls `controls/verifier-mutations/`.
* Upper bound 19: for 20 rows the least kappa per column is at (4,4,3,3,3,3), kappa 24; 8*24 = 192 > C(20,2) = 190.
* Corollary: NO valid 19-row array => maximum exactly 18. (Row deletion preserves validity.)

## 1. Counting and profiles (L1, L2): every valid array is in one of 10 multisets

* kappa_c = sum_s C(n_{c,s},2) = row pairs agreeing in column c; validity gives sum_c kappa_c <= 171. Min kappa for 19
  in 6 parts is 21 at (4,3^5); 8*21 = 168; total excess <= 3; exactly L = 3 - excess row pairs agree nowhere.
* Profiles (exhaustive over 235 partitions of 19 into <= 6 parts, zeros allowed): P0 (4,3,3,3,3,3) e0;
  P1 (4,4,3,3,3,2) e1; P2a (5,3,3,3,3,2), P2b (4,4,4,3,2,2) e2; P3a (4,4,4,3,3,1), P3b (5,4,3,3,2,2) e3.
  All have 6 nonzero parts: every block size n >= 1 (production-domain fact used in section 4).
* Multisets (8 columns, excess <= 3): E0 {P0^8} L3; E1 {P1,P0^7} L2; {P2a,P0^7}, {P2b,P0^7}, {P1^2,P0^6} L1;
  {P3a,P0^7}, {P3b,P0^7}, {P2a,P1,P0^6}, {P2b,P1,P0^6}, {P1^3,P0^5} L0. Indices ms00..ms09 per
  `data/profiles-19-8-6.json`/skeleton headers (ms01 = E1, ms06 = {P1^2,P0^6}, ms09 = {P1^3,P0^5}).
* Code `src/profiles.py`; independent recount in `src/gen_skel_b.py` multisets(); parent R1
  (`review/pa19-parent-cover-replay-v1/cover-binding-result.json`: 235, 6, 10, min 21, budget 3).
* NO balanced-only restriction: every multiset is covered (E0 by section 3, the other nine by sections 4-7).

## 2. Row identity (used everywhere)

For a valid array the rows agreeing with r in different columns are disjoint sets, so r agrees with exactly
A(r) = sum_c (n_{c,A[r][c]} - 1) <= 18 others and misses l(r) = 18 - A(r) rows; sum_r l(r) = 2L, 0 <= l(r) <= L.
With T(r) = P0 columns whose size-4 block (quad) contains r and w(r) = sum over special columns of e = block size - 3:
A(r) = 16 + |T(r)| + w(r), so |T(r)| + w(r) = 2 - l(r) in [2 - L, 2]. Necessary consequences:
* E0 (w = 0): t(r) <= 2 and l(r) = 2 - t(r) exactly.
* Quads of distinct P0 columns share <= 1 row; rows with identical nonempty T agree in every column of T.
* |T(r)| <= tmax = min(c0, 2 - wmin), wmin = sum over special columns X of (min block size of X) - 3.
* |T(r)| >= 3 forces w(r) <= -1, so r lies in a block of size <= 2 of some special column; hence the number of such
  rows <= hmax = total number of rows in size-<=2 blocks of the special columns (a union bound).
* One special column (c0 = 7): its multiset of e-values must be assignable to rows with 0 <= 2 - |T(r)| - e <= L.

## 3. E0 (ms00): one of 486 quad graphs  [README "Amendment A1"]

* n1 + 2 n2 = 32, n0 + n1 + n2 = 19, 2 n0 + n1 = 6 give n2 = 13 + n0, n0 <= 3. t = 2 rows are the edges of a simple
  graph G on the 8 columns (two quads share <= 1 row), max degree <= 4, |E| = 13..16; 4 - deg(a) private rows per
  column; |E| - 13 rows in no quad (always 19 rows).
* List `geng -q 8 13:16 -D4` = 486 (309/136/35/6), `data/quadgraphs-8v-13to16e-D4.g6` (687602738d82...); independent
  `src/graphs_check.py` (networkx atlas extension) bijection; parent R2 replay (geng ad2f68ad..., labelg 0be70bdb...)
  and atlas bijection (`generator-replay-result.json` balanced_atlas).
* M1 CNF `src/encode_q0.py`; M2 CNF `src/encode_q0b.py` (independent code). See section 8 for symmetry.
* Certificates: M1 cycle-1 kissat DRAT FILE -> drat-trim -> `cases19q0/results/gNNN.check.json` (ok and
  drat_trim_verified; "s VERIFIED" substring, rc not gated; ok needs CNF sha now == at solve and also lrat-check,
  whose extra conjunct is harmless). M2 `m2q0c/results/gNNN.json` (rev 5, CaDiCaL binary DRAT streamed into drat-trim).
  Cycle-1 `m2q0b/` (lrat-check only) is UNCERTIFIED and not counted.
* Binding: index graph6 == g6 line (parent R2). E0 CNF bytes were NEVER rebuilt from graph6 by a parent for either
  method (producer-only representation binding). The aggregator counts E0 files (486 hard-coded "graphs"), not
  per-index coverage.

## 4. A2 (ms01..ms09): one of 5577 P0-quad skeletons  [README "Amendment A2"]

* Skeleton = linear hypergraph on the c0 P0 columns: rows with |T| = 2 are edges of a simple graph (max degree 4),
  rows with |T| in 3..tmax are hyperedges (pairwise sharing <= 1 vertex, containing no graph edge), each vertex in
  exactly 4 rows (4 - deg private rows), the rest empty; filters: #hyperedges <= hmax, rows <= 19, one-special-column
  matching. Counts ms01..ms09: 3215/59/674/39/73/482/482/482/71 = 5577.
* M1 list `src/gen_skel.py`: `geng -q c0 -D4` (all graphs, disconnected included) + every set of <= hmax pairwise
  linear hyperedges respecting degree 4, dedup by WL-hash bucket (with invariant key) + networkx is_isomorphic.
* M2 list `src/gen_skel_b.py`: `genbg -q -Z1 -d2:0 -D{tmax}:4 h c0`, h = 0..2c0 (first class rows in >= 2 quads,
  degree 2..tmax; second class quads, degree <= 4; -Z1: two quads share <= 1 row; flags logged in
  `cycle2/genbg-help-flags.txt`); filters re-coded independently (Kuhn matching). SHARED: tmax/hmax/filter formulas.
* `src/compare_skel.py` bijection per multiset + `a_to_b` maps; parent R3 regenerated both lists and all 9 maps
  (`generator-semantic-check-v1.json` PASS). Specs `cases19skel/index.json` + `specs/*.json` bound (parent R4).
* M1 CNF `src/encode_skel.py` (+ `src/encode_e1.py` CNF class): EO; P0 quad cells fixed; P0 symbols 1..5 exactly 3;
  special exact counts (sequential counters); AMO agreements; ROW sum_c (n-1) in [18-L, 18] (weighted counters);
  COVER at most L non-agreeing pairs; symmetry in section 8.
* M2 CNF `src/encode_skel_b.build_v2` (direct runs): EO; quad cells fixed; binomial at-most counts (sum 19 => exact);
  column-pair 4-clauses; EXACT per-row identity sum_{r'} u(r,r') + sum_special (n - 2) = 2 - |T(r)| + ns by a
  totalizer (size-1 blocks moved across as negated literals, target + 1); symmetry in section 8.
* Unreachable degenerate branches (production domain): (i) M2 `target < 0 or target > len(o)` emits an empty
  clause; target = 2 - |T| + ns + #(special labels with n = 1); with |T| <= tmax <= 2 - wmin one gets
  target >= sum_X (min_X - 2 + [min_X = 1]) >= 0 (min_X in {1,2,3}) and target <= 2 + ns + #(n=1) < 18 <= len(o).
  (ii) M1 ROW lower-bound cap = sum(wmax) - (18 - L) >= 24 - 18 > 0, so weighted_at_most never negates all literals.
  (iii) every count n >= 1, so the M2 `else` (n == 1) branch never sees n = 0. (iv) encode_q0 caps 2 - t >= 0.

## 5. Splits of undecided A2 cases (all-P1 multisets ms01, ms06, ms09)

* A3, ms01 (31 cases, `cycle2/a3/<tag>/`): the single P1 column's blocks (A, B size 4, P size 2) are fixed ("full
  skeleton"). Enumerator `src/extend_p1.py`; CNFs `src/encode_full.py` (all non-triple cells fixed; at most l(r)
  misses per row, at most L total; value precedence of triple symbols; row lex for identical fixed pattern) and
  `src/encode_full2.py` (adds exact leave counts; used for f00012_exact). Single records f%05d(.json|_exact|_r3).
* A3', ms06 (19 cases) and ms09 (43 cases) (`cycle2/part/<tag>/`): one-column split m = 1, enumerator
  `src/extend_p1q.py`; singles `src/encode_partq.py`; batches A3'' `src/encode_partbatch.py` (B = 100 typical).
* Enumerator necessary conditions: blocks disjoint; two rows that already agree (common P0 quad or common earlier
  special block) never share a block; per-row budget with every remaining special column moving w by at most +-1.
  Orbit reduction: within each class of rows with identical history (T and roles so far) only a lowest-index
  prefix is chosen (class-uniform availability, agreement and budget); final dedup by networkx isomorphism of
  coloured incidence graphs (rows, P0 quads, blocks tied to their column; A and B share a colour) = Aut(S) x A/B
  swap (x identical fixed P1 columns when m > 1).
* Batch semantics (A3''): selectors t_i, clause (t_1 | ... | t_b); unguarded constraints identical for all
  placements; placement i's fixed cells and (M1 only) its row lex guarded by -t_i. Any model of subcase i extends to
  the batch (t_i true, all other t_j false), so batch UNSAT => each listed subcase UNSAT. M1 batch records list
  explicit indices (no `multiset` key); M2 batch records use [first, last] and carry `multiset`.
* M2 splits: `src/extend_b.py` (count vectors (a,b,p) per row class; nonempty-T classes give <= 1 row per block;
  classes with intersecting T never share a block; budget with ns - 1 free columns; canonical minimum over a
  brute-force Aut(S) (all c0! P0 permutations preserving the type multiset) x A/B swap; lowest rows of each class);
  CNF `encode_skel_b.build_partbatch` (M2 v1 symmetry, section 8).
* Parent bindings: R6 (`review/pa19-placement-binding-v1/`) byte-replayed the 31 ms01 + 43 ms09 lists and 74 M2
  lists (5 byte-equal, 69 parent-generated counts), with stdlib `r6_indep.py` (Burnside) orbit counts agreeing and
  32 mutation controls; `review/pa19-ms06-placement-binding-v2/` replayed ms06_s00150 (49,902 placements).
  The other 18 ms06 M1 lists (s00204 s00212 s00214 s00216 s00228 s00266 s00285 s00287 s00297 s00310 s00311 s00368
  s00370 s00389 s00406 s00410 s00414 s00430) and all M2 lists produced later are PRODUCER-ONLY.
* Split-record formula binding: R8 (`review/pa19-subcase-binding-v1/`) regenerated a frozen sample (374 records incl.
  20 reruns) at 14:56 plus inc-001 (253 ms06_s00150 batches FORMULA_EQUAL, list then unverified); all other split
  records are producer-only (records carry cnf_sha256 and indices but no ext.json hash or encoder hash).

## 6. ms06_s00468: exact six-unit cell cover  [README "Amendment S00468-SIX-UNIT"]

* Base = pinned encode_skel CNF (sha 137407b6...; equals parent R5's in-memory rebuild of encode_skel.build(spec);
  stored file `cases19skel/cnf/ms06_s00468.cnf` hashes to it, 1,504,628 bytes).
* Subcase s (0..5) = base with header clause count + 1 and appended unit `421+s 0`; x[8][6][s] = 1 + 48*8 + 6*6 + s
  (encode_skel allocates all cell variables first in row/column/symbol order). Column 6 >= c0 = 6: first P1 column.
* Cover: the base contains the at-least-one clause of cell (8,6), so every model of the base satisfies some unit;
  base UNSAT iff all six subcases UNSAT. No symmetry argument is used. Positive units only (no negated units needed).
* Acceptance: `src/summarize15.py` cell_cover rebuilds the six expected subcase byte strings from the pinned base and
  requires identity fields, base sha/body/header/length, unit bytes, subcase sha/length, revision 13/14 and the full
  predicate. Records `cycle2/cell-cover/ms06_s00468/r08_c06/s00..s05.json`; runner `src/run_s00468_cell(14).py`.

## 7. Certificates and acceptance predicates (lane aggregator `src/aggregate15.py` + `src/summarize15.py`)

* M1 route per A2 case (first applicable): (a) pass-1 UNSAT + `cases19skel/proofcheck/<tag>.json` ok and
  drat_trim_verified (`src/run_proofpass.py`: kissat --seed=1 DRAT FILE (retained in cases19skel/proof/), drat-trim
  on files, "s VERIFIED" substring, no rc gate; ok = cnf matches pass 1, kissat rc 20, drat_trim_verified,
  lrat_verified); (b) pass-1 UNSAT + `cycle2/proofstream/<tag>.json` ok, drat_trim_verified, cnf_matches_pass1_sha
  (revisions 1-5; rev 1 substring only, rev 2 dt_ok + substring, rev 3-4 self exit + rc 0 + substring (+ lrat
  conjunct), rev 5 self exit + rc 0 + substring); (c5) `cycle2/hard5/<tag>.json` certified() + cnf_matches_pass1_sha;
  (d) A3 coverage; (e) A3'/A3'' coverage; then the s00468 cell route (summarize15).
* Pin counts: ms01 a1436 b1748 d31; ms02-05 all a; ms06 b376 c5 86 e19 cell 1; ms07 a209 b273; ms08 b482;
  ms09 b28 e43. M2: direct-drat (cycle2/m2skel_drat, mapped by a_to_b) or partbatch-drat coverage.
* certified(r): status UNSAT; never lratstrict (rev 6), rev 8 or rev 10 (retired); rev 11-15: checked,
  drat_trim_verified, drat_trim.s_lines == ["s VERIFIED"] ('\r'-stripped lines starting "s "), replay_ok,
  reader_ok, no admission_denied, no aborted_by_sigterm (stream_check11-15 set drat_trim_verified only if drat-trim
  exited by itself with rc 0, exact s-lines and replay_ok; checked only if the solver exited by itself with rc 20,
  no proof cap, reader_ok, not ABORT); rev 9: checked, drat_trim_verified, exact s_lines; rev 5: checked and
  drat_trim_verified; otherwise (rev 1-4/none): drat_trim_verified and checked.
* Split coverage: union over certified f*.json (suffix none/_exact/_r3; _r2 ignored) and batch_*.json (not _r2;
  indices from the record; `multiset` key + 2 entries => range) must contain range(n), n from ext.json
  (num_full / num_placements). n = 0 is accepted VACUOUSLY by this code (see section 9).
* Staged pipeline (rev 11-15): CNF bytes hashed in memory and written through FIFOs to the solver and later to
  drat-trim; binary DRAT read from a FIFO, hashed, zstd-compressed in RAM; after solver exit, decompressed bytes are
  fed to drat-trim -i stdin; replay_ok binds delivered bytes/sha to the streamed proof. FIFO writer errors are
  swallowed (`_writer`), so CNF-consumer identity rests on the same in-memory bytes plus drat-trim parsing.
* drat-trim (tools/drat-trim, commit 2e3b2dc0, binary sha 111b0405...): verdict lines "\rs VERIFIED" (rc 0),
  "\ns NOT VERIFIED" (rc 1), "s TIMEOUT" (exit 0), "\rc trivial UNSAT\ns VERIFIED" (rc 1), early CNF EOF = warning
  then stop parsing; `-i` = binary proof, proof from stdin when no proof path is given.

## 8. Symmetry ledger: WLOG steps and simultaneous compatibility

Global group G = S_19 (rows) x (S_6 wr S_8) (per-column symbol relabeling, column permutations). In every route
the order of normalisation is: (W1) permute columns so P0 columns come first and special columns follow the
canonical order; (W2) relabel symbols (quad -> 0; special labels by non-increasing count); (W3) permute rows and
P0 columns so the quad structure equals the listed labelled representative (graph G for E0, skeleton S for A2);
(W4, splits only) move a chosen P1 column to c* = c0 and map its (A,B,P) to the listed representative by an element
of Aut(S) x A/B swap x within-class row permutations, then A -> 0, B -> 1, P -> 5, triples -> 2..4; (W5) apply the
route's breaking. W1-W4 keep the case/subcase fixed; W5 must not move the array out of it.
* Lex-leader routes (M1 E0 encode_q0; M1 encode_skel; M1 encode_full/full2/partq/partbatch; M2 build_v2): all
  breaking constraints are A <= g(A) in ONE row-major order (rows top-down, columns left-right, cells compared by
  integer value) for generators g of the stabilizer H of the fixed structure: adjacent equal-count symbol swaps in a
  column (value precedence: first occurrence of s before s+1), transpositions of rows with identical fixed pattern
  (row r <= row r' lexicographically, columns left to right), transpositions of consecutive identical free special
  columns (column c <= column c+1 top-down). The lex-least element of the H-orbit of any canonical array satisfies
  every such constraint at once and still has the fixed structure (H preserves it).
* M2 v1 routes (build / build_part / build_partbatch): P0 triple-label FIXING per column (rows of Q_d \ Q_c,
  d maximizing |Q_d \ Q_c|, ties smallest d, get labels 1,2,3(,4) in row order) is a per-column relabeling applied
  after rows are fixed; the remaining breaking (first-occurrence among c* triple labels, equal-count labels of free
  special columns, top-down lex of consecutive identical free special columns) is lex-leader for a group acting only
  on special-column cells and not moving rows; no row lex. Hence both hold simultaneously.
* E0 M2 encode_q0b: only the per-column fixing (no lex constraints).
* Aut(G), Aut(S) and the choice among tied columns are left unbroken (cost, not soundness).

## 9. Structural versus proof-checked

* M1 at the pin: every counted case or placement index is backed by >= 1 drat-trim-verified UNSAT record; no M1
  placement list is empty (PA19FinalReceiptAudit: smallest M1 num_full 41). Split routes additionally rest on
  enumerator completeness (structural reduction, not proof-checked).
* EXPLICIT STRUCTURAL ROW (M2 only): ms09 b-index 3 (a_to_b inverse = M1 ms09_s00003, itself M1 route b, rev 5
  proofstream). Skeleton types [[0,1,2,3,4]], empty 3 (c0 = 5, L = 0, three P1 columns). `extend_b` wrote a complete
  EMPTY list (`cycle2/m2part_drat/ms09_b00003/ext.json` sha 2fd71b8e..., num_placements 0). Parent microproof
  `review/pa19-ms09-b3-structural-parent-v1.md` (sha f311d68d..., 01:46:28; copy in snapshot-supp2/): 5*21 + 3*22 =
  171 so every pair agrees exactly once; t(r) + e_1 + e_2 + e_3 = 2; the universal row h (t = 5) needs e_j = -1 in
  all three P1 columns; every other nonempty row shares a P0 quad with h; an empty row (t = 0) can never be in a
  pair (-1 + 1 + 1 < 2); so h has no partner. Count it as STRUCTURAL; it never inherits a solver/checker/proof hash
  or "s VERIFIED". aggregate15 would accept it vacuously (0/0); a different empty list is NOT accepted by this note.

## 10. Trust base (the conditional statement)

IF (i) sections 1-6 and 8 are correct; (ii) nauty geng/genbg (sha ad2f68ad... / 638224266...) enumerate completely as
documented and networkx 3.7 is_isomorphic/WL hashing behave as documented; (iii) every encoder admits every
canonical valid array of its case/subcase (completeness direction; an over-weak CNF is harmless for UNSAT);
(iv) the drat-trim binary (sha 111b0405...) correctly verifies the CNF bytes and DRAT it read, and each record's
cnf_sha256 is the hash of those bytes; (v) each counted record is the genuine output of its recorded pipeline on
the formula its tag/indices denote (no mislabelled tag/index/list, no forgery); (vi) aggregate15/summarize15 select
exactly the coverage described; (vii) the structural b3 argument (M2 only); THEN no valid PA(19,8,6) exists and the
optimum is 18. Cross-checks: (ii) atlas + two generators + R3/R6; (iii) two encoders + static audits + post hoc
controls; (v)/(vi) R5 (all 5577 base CNFs), R6 (lists), R8 (sample), R7 (14:39 snapshot), PA19FinalReceiptAudit
(all-case metadata). No parent native proof replay exists; drat-trim and the staged harness are shared by M1 and M2.

## 11. Old scout gaps: proposed dispositions (reviewers must contest or confirm)

Cover scout (`review/pa19-cover-scout-audit-v1.md`):
* Major-1 unfinished cases: M1 CLOSED at the pin (0 open); M2 OPEN (166).
* Major-2 binding: pass-1 CNF regeneration RESOLVED by R5 (all 5577 M1 base CNFs); M2 direct CNFs not parent-rebuilt
  (OPEN); split records PARTIAL (R8 sample + inc-001; rest producer-only); hash manifest PARTIAL
  (`cycle2/MANIFEST-cycle2-20261017T121839.sha256`, 5823 entries at 12:18; later lists need PA19FinalReceiptAudit
  hashes); STATUS open-list cut RESOLVED (aggregate15 writes full lists); ms00 hard-coded 486 PARTIAL (files counted,
  not indices).
* Minor-3 shared formulas/nauty/networkx: ACCEPTED as trust base, formulas re-derived (section 2).
* Minor-4 stale README text: RESOLVED by [STALE] annotations at README lines 47, 83, 137, 262.
* Minor-5 M2 batch-range heuristic: STILL PRESENT in aggregate15 (benign only if every counted batch's indices are
  a consecutive range equal to its filename; M1 records have no `multiset` key).
* Minor-6 control coverage (PA18 empty skeleton; gen_skel_b hard-wired 19/8/6): STILL TRUE (controls are post hoc,
  not load-bearing).
* Minor-7 genbg flags: RESOLVED (`cycle2/genbg-help-flags.txt`).
* ms01_s02573 f00012: RESOLVED by A3-exact (`encode_full2.py`, f00012_exact checked).
Encoder scout (`review/pa19-encoder-scout-audit-v1.md`):
* F1 lrat-check unsound: RESOLVED for acceptance (no counted record depends on lrat-check; m2q0b and CaDiCaL-LRAT
  records listed as uncertified; E0 M2 recertified by m2q0c). Note: path a / E0-M1 / rev 1-4 "ok" also conjoin
  lrat-check (harmless).
* Major missing control receipts: PARTIAL (`cycle2/control13-v5.json` covers (13,5,4) M1/M2 pipelines incl. q-generalised
  full encoders; build_v2g byte identity claim and batch controls to be confirmed by reviewers).
* Major uncontrolled production encoders (encode_full q=6, encode_q0/q0b 19/8/6): PARTIAL/OPEN (q-generalised copies
  only; E0 encoders have no positive control).
* Major weak binding: PARTIAL (see Major-2 above).
* Major one checker for everything: OPEN (shared drat-trim binary and staged harness).
* Minor items (64 KiB stalls, deterministic FIFO names, SAT listing, range heuristic, weak controls, nits): mostly
  RESOLVED or non-load-bearing; reviewers to confirm.

## 12. Residuals before any final claim (draft)

1. Independent M2 completion (166 open at the pin) under the same strict predicate, with the b3 structural row kept
   separate; parent audit of every further empty or structural list.
2. Parent native replay sample (re-solve + independently built drat-trim or second checker) across M1 routes
   a/b/c5/d/e/cell and M2; path-a DRAT files are retained, staged-revision proofs are not.
3. All-case formula binding for split records (CNF sha from spec + ext.json + indices); parent replay of the 18
   producer-only ms06 lists and of all later M2 lists.
4. E0 CNF-from-graph6 rebuild for both methods and per-index E0 coverage.
5. A parent final aggregator that fails closed on n = 0 lists, filename/indices mismatches, missing identity fields
   and route mixing, and reports structural rows separately.
