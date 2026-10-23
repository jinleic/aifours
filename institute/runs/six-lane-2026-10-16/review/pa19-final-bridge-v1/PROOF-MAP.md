# PA(19,8,6) conditional proof map (PA19FinalBridgeDesk, draft for hostile review)

Written 2026-10-18 ~01:50 PDT from static reading. Not a verdict, not parent acceptance. Every statement is
conditional on the trust base in section 9. Paths are lane-relative (LANE = information-science/evidence/
six-lane-20261016/packing-array19) unless prefixed `review/` (the run review directory). In the snapshot,
lane files are under `snapshot/lane/`, review files under `snapshot/review/`, the contract under `snapshot/run/`.

Pinned inputs: `cycle2/m1-complete-candidate-20261018T012523.json` (sha256 cf3e87c5...d791; label "M1-complete
finite nonexistence candidate; NOT parent final acceptance"), `STATUS15.json` (b0dac6b0...45f3), `README.md`
(7eb046e1...9ae60). M1: all 5577 A2 cases and all 486 E0 graphs counted UNSAT by the lane aggregator; M2: 486 E0
plus 5411/5577 A2 cases at the pin, 166 open. A complete M1 is the producer's candidate, NOT the final gate.

## 0. Target and the "exact 18" corollary

* Valid array: 19 rows x 8 columns over 6 symbols, every two rows agree in at most one column (equivalently no
  ordered symbol pair repeats in any two columns; equivalently a code of length 8 over 6 symbols with minimum
  distance >= 7, so A_6(8,7) >= 19).
* Lower bound 18: `data/cpro1-pa-18-8-6.txt` (CPro1 PA(18,8,6)); verified by `src/verify_pa.py` (row-pair
  definition) and `src/verify_pa2.c` (column-pair definition), mutation controls `controls/verifier-mutations/`.
* Upper bound 19 (counting): for 20 rows the least kappa per column is at counts (4,4,3,3,3,3), kappa = 24;
  8*24 = 192 > C(20,2) = 190. So no 20-row array exists (and none larger, by row deletion).
* Corollary: if NO valid 19-row array exists, the maximum is exactly 18.

## 1. Counting and profiles (L1, L2) — every valid array is in one of 10 multisets

* kappa_c = sum_s C(n_{c,s}, 2) counts row pairs agreeing in column c. Validity: sum_c kappa_c <= C(19,2) = 171.
  Minimum kappa for 19 into 6 parts is 21 at (4,3,3,3,3,3); 8*21 = 168; total excess sum_c (kappa_c - 21) <= 3.
  The number of row pairs agreeing nowhere is exactly L = 3 - excess.
* Profiles with excess <= 3 (exhaustive over the 235 partitions of 19 into <= 6 parts, zeros allowed):
  P0 (4,3^5) e0; P1 (4,4,3,3,3,2) e1; P2a (5,3^4,2) and P2b (4,4,4,3,2,2) e2; P3a (4,4,4,3,3,1) and
  P3b (5,4,3,3,2,2) e3. All have 6 nonzero parts (production-domain fact used below: every block size n >= 1).
* Multisets (8 columns, excess <= 3): E0 {P0^8} (L=3); E1 {P1,P0^7} (L=2); {P2a,P0^7}, {P2b,P0^7}, {P1^2,P0^6}
  (L=1); {P3a,P0^7}, {P3b,P0^7}, {P2a,P1,P0^6}, {P2b,P1,P0^6}, {P1^3,P0^5} (L=0). Indices ms00..ms09 as in
  `data/profiles-19-8-6.json` and the skeleton-file headers (ms06 = {P1^2,P0^6}, ms09 = {P1^3,P0^5}).
* Code: `src/profiles.py`; independent recount inside `src/gen_skel_b.py` (multisets()); parent R1 recount
  `review/pa19-parent-cover-replay-v1/cover-binding-result.json` (235 partitions, 6 profiles, 10 multisets).
* NO balanced-only restriction: all 10 multisets are in the cover. E0 results alone say nothing about ms01..ms09.

## 2. Row identity (used everywhere)

For a valid array, the sets of rows agreeing with row r in different columns are disjoint, so r agrees with
exactly A(r) = sum_c (n_{c,A[r][c]} - 1) <= 18 other rows and misses l(r) = 18 - A(r) rows; sum_r l(r) = 2L.
With T(r) = set of P0 columns whose size-4 block (quad) contains r, and w(r) = sum over special (non-P0) columns of
e = (block size - 3): A(r) = 16 + |T(r)| + w(r), so |T(r)| + w(r) = 2 - l(r) in [2-L, 2].
Consequences (all necessary conditions):
* (E0) w = 0: t(r) = |T(r)| <= 2 and l(r) = 2 - t(r) exactly.
* Two quads (of distinct P0 columns) share <= 1 row; two rows with identical nonempty T agree in each column of T.
* |T(r)| <= tmax = min(c0, 2 - wmin), wmin = sum_X min_block(X) - 3 per special column X.
* |T(r)| >= 3 forces w(r) <= -1, so r lies in a block of size <= 2 of some special column; hence the number of
  such rows is <= hmax = number of rows in size-<=2 blocks of the special columns.
* One special column (c0 = 7): the multiset of e-values (one per row, from block sizes) must be assignable to rows
  with 0 <= 2 - |T(r)| - e(r) <= L (perfect interval/bipartite matching).

## 3. E0 (ms00): one of 486 quad graphs  [README "Amendment A1"]

* t(r) <= 2; n1 + 2 n2 = 32 (8 quads x 4), n0 + n1 + n2 = 19, 2 n0 + n1 = sum l(r) = 6, so n2 = 13 + n0, n0 <= 3.
  Rows with t = 2 are the edges of a simple graph G on the 8 columns (simple: two quads share <= 1 row), max degree
  <= 4, |E| = 13..16, plus 4 - deg(a) private rows per column and |E| - 13 rows in no quad (always 19 rows).
* List: `geng -q 8 13:16 -D4` = 486 graphs (309/136/35/6), `data/quadgraphs-8v-13to16e-D4.g6` (687602738d82...).
  Independent: `src/graphs_check.py` (networkx atlas extension) bijection; parent replay R2 (geng sha ad2f68ad...,
  labelg) and atlas bijection in `generator-replay-result.json` (balanced_atlas: 486 classes, each matched once).
* WLOG: permute columns so G is exactly the listed labeled graph (column perms realize graph isomorphisms); rows
  ordered: edges (sorted), private rows by column, no-quad rows; quad symbol -> 0 in every column.
* M1 CNF `src/encode_q0.py`: EO cells, quad cells fixed, symbols 1..5 exactly 3 each (sequential counters), AMO
  agreements (aux y), per row at most 2 - t(r) misses and at most 3 misses total; symmetry: value precedence 1..5 in
  every column, row lex between consecutive rows with identical quad membership (t != 2). All lex-leader for ONE
  row-major order with the stabilizer group (row transpositions within identical-membership classes, triple-symbol
  permutations per column). Aut(G) unbroken.
* M2 CNF `src/encode_q0b.py` (independent code): column-pair 4-clauses; binomial "at most 3" per triple symbol;
  leave: per pair not sharing a quad, witness or miss var; rows with t = 2 must agree with everyone; per row <= 2-t
  misses, total <= 3; symmetry: per column c, the rows of Q_d \ Q_c (d maximizing, ties smallest) get labels
  1,2,3(,4) in row order (they pairwise agree in column d, are outside Q_c, so hold distinct triple symbols). Pure
  per-column relabeling, no other breaking.
* Certificates: M1 cycle-1 kissat DRAT file -> drat-trim (`src/check_proofs.py`, `.check.json` ok and
  drat_trim_verified; acceptance "s VERIFIED" substring, rc not gated; ok also needs CNF sha now == at solve).
  M2 `m2q0c/` (rev 5: CaDiCaL binary DRAT streamed into drat-trim; `src/run_m2q0c.py`, `src/stream_check5.py`).
  The cycle-1 `m2q0b/` (lrat-check) is UNCERTIFIED and not counted.
* Binding: graph6 index binding checked by parent (cover-binding R2 all_index_bindings). E0 CNF bytes were NEVER
  rebuilt by a parent from graph6 for either method (producer-only representation binding).

## 4. A2 (ms01..ms09): one of 5577 P0-quad skeletons  [README "Amendment A2"]

* Skeleton = linear hypergraph on the c0 P0 columns: |T| = 2 rows as edges of a simple graph (max degree 4),
  |T| in 3..tmax rows as hyperedges (pairwise sharing <= 1 vertex and containing no graph edge), each vertex in
  exactly 4 rows (4 - deg private rows), remaining rows empty; filters: number of hyperedges <= hmax, rows <= 19,
  one-special-column matching filter.
* M1 list `src/gen_skel.py`: `geng -q c0 -D4` (all graphs on c0 vertices, disconnected included) + every set of
  <= hmax pairwise-linear hyperedges respecting degree 4, dedup by networkx WL-hash bucket + is_isomorphic on
  coloured incidence graphs. Counts ms01..ms09: 3215/59/674/39/73/482/482/482/71 = 5577.
* M2 list `src/gen_skel_b.py`: nauty `genbg -q -Z1 -d2:0 -D{tmax}:4 h c0` for h = 0..2c0 (first class: rows in
  >= 2 quads, degree 2..tmax; second class: quads, degree <= 4; -Z1: two quads share <= 1 row); same filters by
  independently written code (Kuhn matching). SHARED: the tmax/hmax/filter formulas (both implement section 2).
* `src/compare_skel.py`: per multiset bijection under isomorphism; `a_to_b` maps. Parent R3 regenerated both lists
  and all 9 maps (`generator-semantic-check-v1.json` PASS; byte-equal B and maps; A equal up to added metadata).
* Spec binding: `cases19skel/index.json` + 5577 `specs/*.json` bound to skeleton entries (parent R4, all bound).
* WLOG: columns ordered P0 first then special columns in the canonical sorted order (identical special profiles in
  any order); symbols relabeled: quad -> 0 in P0 columns, special labels by non-increasing count (label s has count
  p_s); rows/P0-columns permuted so that the hypergraph equals the listed representative exactly with row order of
  `encode_skel.rows_of` (M1) / `encode_skel_b` member order (M2).
* M1 CNF `src/encode_skel.py` (+ `src/encode_e1.py` CNF class): EO cells; P0 quad cells fixed; P0 symbols 1..5
  exactly 3; special columns exact counts; AMO agreements; ROW: sum_c (n-1) <= 18 and >= 18 - L (weighted
  counters); COVER: at most L non-agreeing pairs; symmetry: value precedence (P0 1..5; equal-count special labels),
  row lex for consecutive rows with identical T and |T| <= 1, column lex for consecutive identical special columns.
  All lex-leader for one row-major order under the stabilizer H(S) (row transpositions within T-classes,
  triple/equal-count symbol permutations, identical-special-column transpositions). Aut(S) unbroken.
* M2 CNF `src/encode_skel_b.build_v2` (direct runs; independent code): EO; quad cells fixed; binomial at-most counts
  (sum 19 forces exact); column-pair 4-clauses; per-row EXACT identity sum_{r'} u(r,r') + sum_special (n-2)
  = 2 - |T(r)| + ns via totalizer (size-1 blocks moved across as negated literals); symmetry all lex-leader for one
  row-major order: P0 triple first-occurrence, equal-count special first-occurrence, top-down column lex of
  consecutive identical special columns, row lex of consecutive rows of identical type (|T| <= 1).
* Production-domain proof that the empty-clause branch of the M2 row identity (`target < 0 or target > len(o)`)
  is unreachable: target = 2 - |T| + ns + #(special labels with n = 1). With |T| <= tmax <= 2 - wmin,
  target >= sum_X (min_X - 2 + [min_X = 1]) >= 0 for min_X in {1,2,3}; target <= 2 + ns + #(n=1) < 18 <= len(o).
  Likewise M1 ROW lower-bound cap sum(wmax) - (18 - L) >= 24 - 18 > 0, so no "w > cap" unit-negation collapse.

## 5. Splits of undecided A2 cases (all-P1 multisets ms01, ms06, ms09)

* A3 (ms01, `cycle2/a3/<tag>/`, 31 cases): fix the single P1 column's blocks (A, B size 4; P size 2) =
  "full skeleton". Enumerator `src/extend_p1.py`: necessary conditions (blocks disjoint; no two rows that already
  agree in a common block; row budget |T| + w in [2-L, 2], with each remaining column moving w by at most +-1);
  within each class of rows with identical history (T and roles so far) take only lowest-index rows (prefix);
  dedup by networkx isomorphism of coloured incidence graphs (merges only Aut(S), A/B swap, identical-P1-column
  permutations). CNF `src/encode_full.py` (every non-triple cell fixed, leave degrees known, at most l(r) misses
  per row, at most L total; value precedence of triple symbols; row lex for identical fixed pattern) and
  `src/encode_full2.py` (adds exact leave counts; used for f00012_exact).
* A3' (ms06 19 cases and ms09 43 cases, `cycle2/part/<tag>/`): one-column split (m = 1) by `src/extend_p1q.py`
  (q-generalised extend_p1); single subcases `src/encode_partq.py`; batches A3'' `src/encode_partbatch.py`.
  WLOG: any P1 column can be moved to position c0 (column permutation among identical P1 columns); its placement is
  mapped to the listed representative by Aut(S) x A/B swap and within-class row permutations; then A -> 0,
  B -> 1, P -> 5, triples -> 2..4. Remaining symmetry broken by lex-leader for the stabilizer H(S, P): value
  precedence among triple labels of c*, P0 1..5, equal-count labels of free special columns; row lex between rows
  with identical fixed pattern (T, role in c*); column lex between consecutive free special columns.
* Batches (A3''): selector t_i per placement, clause (t_1 | ... | t_b), unguarded constraints identical for all
  placements, placement i's fixed cells and (M1 only) its row-lex guarded by -t_i. A model of subcase i extends to
  the batch (t_i true, others false), so batch UNSAT => every listed subcase UNSAT. Batch records list explicit
  indices (M1) or [first, last] with a `multiset` key (M2).
* M2 splits: `src/extend_b.py` (count vectors (a,b,p) per row class; classes with nonempty T contribute <= 1 row
  per block; classes with intersecting T never share a block; per-row budget with ns-1 free columns; canonical
  minimum over a brute-force Aut(S) (all c0! P0 permutations preserving the type multiset) x A/B swap) and
  `encode_skel_b.build_partbatch` (M2 v1 symmetry: P0 triple-label FIXING (non-lex), first-occurrence among c*
  triple labels and equal-count labels of free columns, column lex of consecutive free columns; no row lex).
  Compatibility: the P0 fixing acts on P0 cells after rows are fixed; the lex-leader group acts on special cells
  only and does not move rows.
* Parent bindings: R6 (`review/pa19-placement-binding-v1/`) regenerated all 74 hard lists at the time (31 ms01 A3,
  43 ms09 A3'; byte-equal) plus 74 M2 lists (5 byte-equal, 69 parent-generated counts) with independent
  `r6_indep.py` orbit counts (Burnside) agreeing; `review/pa19-ms06-placement-binding-v2/` replayed ms06_s00150.
  The other 18 ms06 M1 lists (s00204, s00212, s00214, s00216, s00228, s00266, s00285, s00287, s00297, s00310,
  s00311, s00368, s00370, s00389, s00406, s00410, s00414, s00430) and all later M2 lists are producer-only.
* Split-record CNF binding: R8 (`review/pa19-subcase-binding-v1/`) regenerated a frozen sample (374 records incl.
  20 reruns) as of 14:56 plus inc-001 (253 ms06_s00150 batches formula-equal, list then unverified). All other
  split records: producer-only (records carry cnf_sha256 but no ext.json hash).

## 6. ms06_s00468: exact six-unit cell cover  [README "Amendment S00468-SIX-UNIT"]

* Base = pinned encode_skel CNF of the case (sha 137407b6...; parent R5 rebuild of encode_skel.build(spec) gives
  this sha; the stored file `cases19skel/cnf/ms06_s00468.cnf` hashes to it, 1,504,628 bytes).
* Subcase s (s = 0..5) = base with header clause count +1 and one appended unit clause `421+s 0`, where
  x[8][6][s] = 1 + 48*8 + 6*6 + s = 421 + s (encode_skel allocates cell variables first, row/column/symbol order).
  Column 6 >= c0 = 6 is the first special (P1) column, row 8 zero-based.
* Cover: the base contains the at-least-one clause of cell (8,6); every model of the base satisfies some
  x[8][6][s]; so base UNSAT iff all six subcases UNSAT. No symmetry argument is used.
* Acceptance: `src/summarize15.py` cell_cover rebuilds each expected subcase byte string from the pinned base and
  requires identity fields, base sha/body/header/length, unit bytes, subcase sha/length, revision 13/14 and the full
  predicate; records `cycle2/cell-cover/ms06_s00468/r08_c06/s00..s05.json`.

## 7. Certificates and acceptance predicates (lane aggregator `src/aggregate15.py` + `src/summarize15.py`)

M1 route per A2 case (first that applies): (a) pass-1 UNSAT + cycle-1 stored-proof check `cases19skel/proofcheck`
(ok and drat_trim_verified); (b) pass-1 UNSAT + `cycle2/proofstream` record with ok, drat_trim_verified,
cnf_matches_pass1_sha (revisions 1-5); (c5) `cycle2/hard5` record certified() with cnf_matches_pass1_sha;
(d) A3 coverage; (e) A3'/A3'' coverage; then the s00468 cell route in summarize15. Counts at the pin:
ms01 a1436 b1748 d31; ms02-05 a; ms06 b376 c5 86 e19 cell 1; ms07 a209 b273; ms08 b482; ms09 b28 e43.
certified(r): UNSAT; never lratstrict (rev 6) or rev 8 or rev 10; rev 11-15: checked, drat_trim_verified,
drat_trim.s_lines == ["s VERIFIED"] (lines '\r'-stripped), replay_ok, reader_ok, no admission_denied, no
aborted_by_sigterm (stream_check11-15 set drat_trim_verified only if drat-trim exited by itself with rc 0 and
replay_ok, checked only if solver rc 20 by itself, no cap, reader_ok); rev 9: checked, drat_trim_verified, exact
s_lines; rev 5: checked and drat_trim_verified (self exit, rc 0, "s VERIFIED" substring); otherwise (rev 1-4 or
none): drat_trim_verified and checked. Paths (a) and E0-M1 use check_proofs-style "s VERIFIED" substring without an
rc gate. Split coverage: union of indices of certified f*.json (suffix none/_exact/_r3; _r2 ignored) and
batch_*.json (not _r2) must contain range(n), n = ext.json num_full / num_placements.
drat-trim facts (tools/drat-trim/drat-trim.c, commit 2e3b2dc0): verdict lines "\rs VERIFIED", "\ns NOT VERIFIED",
"s TIMEOUT" (exit 0), "trivial UNSAT\ns VERIFIED" (returns 1); early EOF of the CNF is a warning only.

## 8. Structural versus proof-checked

* M1 at the pin: every counted case or index is backed by at least one drat-trim-verified UNSAT record; no M1
  placement list is empty (smallest num_full 41 per PA19FinalReceiptAudit); split routes additionally depend on
  enumerator completeness (structural reduction, not proof-checked).
* M2 ms09 b-index 3 (= M1 ms09_s00003, which is M1 route b): skeleton types [[0,1,2,3,4]], empty 3 (c0 = 5, L = 0).
  `extend_b` produced a COMPLETE EMPTY list (ext.json num_placements 0, sha 2fd71b8e...). aggregate15 split_cover
  would accept n = 0 VACUOUSLY (len(cov & range(0)) == 0). Structural argument (worker; checked by this desk by hand,
  parent microproof pending): L = 0 so every row agrees with exactly 18 rows: |T| + sum_j e_j = 2 over the 3 P1
  columns, e in {+1,0,-1}. The universal row h (|T| = 5) needs e_j = -1 in all three columns (h in all three
  pairs). Every other nonempty row shares a P0 quad with h, so cannot be h's pair partner; an empty row (|T| = 0)
  can never be in a pair (-1 + 1 + 1 < 2). So h has no partner: no valid array has this skeleton. This must be
  counted as STRUCTURAL (enumerator + hand proof), never as DRAT and never as a generic 0/0 pass.

## 9. Trust base (conditional statement)

IF (i) the lemmas of sections 1-6 are correct; (ii) nauty geng/genbg (sha ad2f68ad.../638224266...) enumerate
completely as documented and networkx 3.7 is_isomorphic/WL-hash behave as documented (dedup and bijection); (iii)
the encoders admit every canonical valid array (completeness direction; over-weak clauses are harmless for UNSAT);
(iv) the drat-trim binary (sha 111b0405...) correctly verifies the CNF bytes and DRAT stream it read, and each
record's CNF sha equals the bytes the checker read; (v) every counted record is genuinely the output of the
recorded pipeline on the recorded CNF (no producer forgery or mislabelled index/tag); (vi) aggregate15/summarize15
select exactly the coverage described; THEN no valid PA(19,8,6) exists and the optimum is 18.
Independent cross-checks exist for (ii) (atlas, two generators, R3/R6), (iii) (two encoders, static audits),
(v)/(vi) partially (R5 all base CNFs, R6 lists, R8 sample, R7 at 14:39, PA19FinalReceiptAudit). No parent
native proof replay has been performed; drat-trim is shared by M1 and M2.

## 10. Residuals before any final claim (draft)

1. M2 completion (166 open at the pin) with the same strict predicate; separate structural (ms09 b3 empty list)
   from proof-checked counts; parent microproof for b3.
2. Parent native replay sample (re-solve + independent drat-trim build or second checker) across routes a/b/c5/d/e
   /cell and M2; no proof bytes are retained for staged revisions.
3. All-case formula binding for split records (regenerate CNF sha from spec + ext.json + indices), at least for
   the 18 producer-only ms06 lists and later M2 lists; parent replay of those 18 lists (extend_p1q) and of later M2
   lists (extend_b).
4. E0 CNF-from-graph6 rebuild for both methods; per-index E0 coverage (aggregator counts files).
5. Parent final aggregation with a predicate that fails closed on n = 0 lists, filename/indices mismatches and
   missing identity fields.
