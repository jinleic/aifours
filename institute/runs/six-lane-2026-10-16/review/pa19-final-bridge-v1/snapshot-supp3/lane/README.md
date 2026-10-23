# PA(19,8,6) lane (info-1, six-lane-2026-10-16)

Frozen 2026-10-17T03:10-07:00 (host clock) BEFORE any search. Contract (read-only):
`institute/runs/six-lane-2026-10-16/screening/info-1-packing-array19-contract.json`.
Owner of this directory only. No edits elsewhere.

## Target (unchanged)
Decide whether a 19x8 array over {0,...,5} exists in which every pair of rows agrees in at
most one column (equivalently every N x 2 subarray has no repeated ordered pair; A_6(8,7) >= 19).
18 is known (CPro1 `result-18-8-6-seed1000.txt`); 19 is the counting upper bound.

## Priority kill check (done 03:00-03:10, <=15 min)
* Colbourn-Ling 1999 and Cao-Du 2004 primary PDFs: NOT accessed. ScienceDirect and CORE
  (core.ac.uk/download/pdf/82008246.pdf) return captcha/Cloudflare challenges; not bypassed.
  Non-PDF challenge page retired to `archive/core-82008246-cloudflare-challenge.html`.
* zbMATH Zbl 0929.05013 (review of Colbourn-Ling): KSP design = maximum admissible number of
  parallel classes of triples plus possibly one block of size 2 or 4; resolves v = 4 (mod 6)
  completely and "nearly completely" v = 1 (mod 6). zbMATH Zbl 1064.05039 (Cao-Du summary):
  "improve the existence results on KPD({3,s*},v) for s=4,5". Neither summary names v=19.
* Secondary source with full statement: Su-Wang, Ars Combin. 91 (2009) 219-230,
  `sources/ars91-kpd-345star.pdf` (sha256 a314e0e6...8a7, OCR in `sources/ocr/`), Theorem 1.3:
  "(Cerny et al., Phillips et al., Colbourn and Ling, Cao and Du) There is a KPD({3,4*},v)
  containing floor((v-3)/2) parallel classes for every v = 1 (mod 3) with v > 25."
* Relation: a KPD({3,4*},19) with 8 classes is exactly a PA(19,8,6) whose 8 columns all have
  profile (4,3,3,3,3,3). The summarized theorem does not cover v = 19. No published v=19
  construction was found. This is an access-limited check: it does NOT establish open status,
  nonexistence, novelty or priority.

## Exact representation and lemmas (frozen)
Array A: rows R = {0..18}, columns C = {0..7}, symbols S = {0..5}. Valid iff for all r<r',
|{c : A[r][c] = A[r'][c]}| <= 1.

L1 (counting). For column c with symbol counts n_{c,s}, kappa_c = sum_s C(n_{c,s},2) is the
number of row pairs agreeing in c. Validity => sum_c kappa_c <= C(19,2) = 171. By convexity
min kappa_c = 21 at counts (4,3,3,3,3,3). Hence total excess sum_c (kappa_c - 21) <= 3, and the
number of row pairs agreeing nowhere is exactly 3 - (total excess).

L2 (profiles). Column profiles = partitions of 19 into <= 6 parts with kappa <= 24. Enumerated
by `src/profiles.py` (exhaustive over all partitions); expected list:
P0=(4,3,3,3,3,3) e0; P1=(4,4,3,3,3,2) e1; P2a=(5,3,3,3,3,2), P2b=(4,4,4,3,2,2) e2;
P3a=(4,4,4,3,3,1), P3b=(5,4,3,3,2,2) e3. All have exactly 6 nonzero parts.
Profile multisets over 8 columns with total excess <= 3 (also enumerated by the script):
E0 {P0^8}; E1 {P1,P0^7}; E2a {P2a,P0^7}; E2a' {P2b,P0^7}; E2b {P1^2,P0^6}; E3a {P3a,P0^7};
E3a' {P3b,P0^7}; E3b {P2a,P1,P0^6}; E3b' {P2b,P1,P0^6}; E3c {P1^3,P0^5}. ALL are searched.
No case is dropped; balanced-only results are never reported as nonexistence.

## Symmetry reduction (frozen, justified) [SUPERSEDED for the final cover: this M-class normalization was used only by the abandoned cycle-1 M-class runs (cases19/); the cover now consists of A1 (ms00) and A2/A3/A3'/A3'' (ms01..ms09), see the amendments below]
Validity is invariant under G = S_19 (rows) x (S_6 wr S_8) (per-column symbol relabeling and
column permutation). For UNSAT soundness every valid array must have a G-image satisfying all
breaking constraints. Normalization N applied to an arbitrary valid array:
1. col0, col1 := two columns of profile P0 (every multiset has at least five P0 columns).
   Positions 2..7 := the remaining six columns ordered by excess non-increasing (ties
   arbitrary), so the profile multiset fixes the profile of every position.
   (Pre-search amendment 03:20: originally col0/col1 were the two largest-excess columns;
   switched before any search because M-class counts are 29 for (P0,P0) versus up to 653
   otherwise, giving 10 x 29 = 290 cases. Class counts: data/mclass-counts.txt.)
2. Relabel symbols of col0 and col1 so counts are non-increasing in the label. The 6x6 0/1
   matrix M[a][b] = #{r : (A[r][0],A[r][1]) = (a,b)} (entries <= 1 by validity) has row and
   column sums (4,3,3,3,3,3). Remaining relabelings permute rows/columns of M inside
   equal-sum groups; apply one that maps M to the lexicographically smallest matrix in its
   orbit (the class representative enumerated by `src/mclasses.py`).
3. Sort rows lexicographically by (A[r][0], A[r][1]); unique keys, so row order is now fixed.
4. Each column c >= 2: relabel symbols ordered by (count descending, first-occurrence row
   ascending). Deterministic given the row order.
5. Permute positions 2..7 among columns of identical profile so their label vectors
   (rows 0..18) are lexicographically increasing (strict: two equal vectors are the same
   partition and would make two rows agree twice).
Steps 4-5 do not change rows or columns 0,1, so every valid array has an image meeting all of:
fixed (col0,col1) = representative of its M class; per-column exact counts; value precedence
among equal-count symbols of columns >= 2; lex order between consecutive equal-profile columns
>= 2. Each SAT case = (profile multiset, M class). Aut(M) and the col0/col1 choice among ties
are left unbroken (costs time, not soundness).

## Methods (frozen)
* M1 (primary): `src/encode_e1.py` CNF: one-hot x[r][c][s] (exactly-one), agreement aux
  y[r][r'][c] <- x[r][c][s] & x[r'][c][s], pairwise AMO_c y; exact per-column symbol counts
  (sequential counters both directions); value precedence via exact prefix vars; lex via
  one-directional equal-prefix vars; col0/col1 units. Solver kissat 4.0.4 with DRAT proof,
  checked by drat-trim (-> LRAT) and lrat-check, both compiled lane-locally from source.
* M2 (independent): the planned `src/encode_e2.py` for the M-class split was NOT written
  (M-class split abandoned, see A1). Actual independent method for E0: M2' in Amendment A1
  (`src/encode_q0b.py` + CaDiCaL 3.0.1 direct LRAT). The non-balanced skeleton split (A2)
  has no independent encoder or generator replication yet. [STALE as of cycle 2: generator replicated by gen_skel_b.py (bijection, cycle2/skel-b/compare-*.json); independent encoders encode_skel_b.build/build_v2/build_part/build_partbatch; see "M2 for the hard cases" and "M2 encoder version 2"]
* M3 (positive search): seeded simulated annealing `src/sa19.c`, bounded CPU, reproducible.
* Witness verifiers: `src/verify_pa.py` (row-pair definition) and `src/verify_pa2.c`
  (column-pair ordered-pair definition), plus mutation controls.

## Amendment A1 (recorded 04:04; encoder written ~03:53, first run 03:55): E0 quad-graph split
M1 M-class cases proved too slow (UNKNOWN at 600-900 s each; see checkpoints.md), so the
balanced multiset E0 is searched by a finer, complete split. Lemma (E0 only): let t(r) be
the number of columns in which row r lies in the size-4 block (quad). Row r meets
sum_c (n_{c,A[r][c]}-1) = 16 + t(r) <= 18 other rows, so t(r) <= 2 and the leave degree is
2 - t(r). Two quads share <= 1 row (else two rows agree twice). With n_i rows of t = i:
n_1 + 2 n_2 = 32, n_0+n_1+n_2 = 19, 2 n_0 + n_1 = 2*3 (leave has 3 edges), so n_2 = 13 + n_0,
n_0 <= 3. Hence the quads are the dual of a simple graph G on the 8 columns: rows in two quads
= edges, max degree <= 4, |E(G)| = 13..16, plus 4-deg(a) private rows per column and |E|-13
rows in no quad; G determines the array's quad cells up to row/column/symbol renaming.
All such G: `geng -q 8 13:16 -D4` = 486 graphs (309/136/35/6 for 13/14/15/16 edges),
`data/quadgraphs-8v-13to16e-D4.g6` (sha256 687602738d82...56d8c); independently reproduced as
a bijection by `src/graphs_check.py` (networkx atlas extension) in
`data/quadgraphs-independent-check.json`. Per G (`src/encode_q0.py`): quad cells fixed, five
triple symbols with count 3 per column, AMO agreements, per-row leave count exactly 2-t(r)
(<= on each row plus <= 3 total), value precedence of symbols 1..5 per column and lex order
between consecutive rows with identical quad membership. Both breaking families are
lex-leader constraints for the same row-major reading order, so every orbit's lex-least
array satisfies all of them. Independent replication M2' (`src/encode_q0b.py`, no shared
code, no auxiliary variables, column-pair 4-clauses, binomial counts, different symmetry
breaking: in column c the rows of Q_d minus Q_c (d maximizing that set) get labels 1,2,3(,4))
solved by CaDiCaL 3.0.1 with direct LRAT output. E0 results are RESTRICTED to all-balanced
columns; they say nothing about the other 9 multisets.

## Amendment A2 (recorded 04:11; generator written 04:06, first sample run 04:10): P0-quad
## skeleton split for the 9 non-balanced multisets E1..E3c
Facts (all from validity, any multiset): every P0 column has one quad; two quads of
different columns share <= 1 row. For row r let T(r) = set of P0 columns whose quad contains
r and w(r) = sum over special (non-P0) columns of (block size - 3). Row r meets
16 + |T(r)| + w(r) <= 18 rows, so |T(r)| <= 2 - w(r) and its leave degree is
l(r) = 2 - |T(r)| - w(r) in [0, L] (L = 3 - excess = number of row pairs agreeing nowhere).
Hence |T(r)| <= tmax = 2 - sum_X(min block size - 3), and a row with |T(r)| >= 3 has
w(r) <= -1, i.e. lies in a block of size <= 2 of a special column, so the number of such
rows is <= hmax = number of rows in size-1/2 blocks of the special columns. With a single
special column the multiset of its values e = size-3 must be assignable to rows with
0 <= 2 - |T(r)| - e <= L (exact necessary condition, checked by interval matching).
Skeleton = P0 columns as vertices, |T|=2 rows as edges of a simple graph (max degree 4),
|T|>=3 rows as hyperedges, 4-deg private rows per vertex, remaining rows empty.
`src/gen_skel.py` enumerates all of them from `geng -q c0 -D4` (all graphs on c0 vertices)
plus every set of <= hmax pairwise-linear hyperedges of sizes 3..tmax respecting degree 4,
drops those needing more than 19 rows or failing the single-column filter, and deduplicates
colored incidence graphs with networkx isomorphism. Counts (skeletons/*.json):
ms01 E1 3215, ms02 E2a 59, ms03 E2a' 674, ms04 E3a' 39, ms05 E3a 73, ms06 E2b 482,
ms07 E3b 482, ms08 E3b' 482, ms09 E3c 71 (total 5577 SAT cases, `cases19skel/`).
Per skeleton (`src/encode_skel.py`): P0 quad cells fixed, P0 triple symbols count 3, special
columns free with exact counts, AMO agreements, row budget in [18-L, 18], at most L
non-agreeing pairs, value precedence (P0 symbols 1..5; equal-count special labels), row lex
for consecutive rows with identical T (|T| <= 1), column lex for consecutive identical
special columns; all lex-leader for one row-major order (P0 columns first). Aut(skeleton)
unbroken. The skeleton generator has no independent replication yet. [STALE as of cycle 2: see gen_skel_b.py / compare_skel.py; NOTE the two generators share the derived tmax/hmax/single-column-filter formulas (both implement README A2), so the bijection checks the enumeration code, not those formulas]
A2 end-to-end control (same code, parameters (13,5,4), `controls/skel13`, `controls/c13skel`):
SAT exactly for the two multisets where the M-class encoder found SAT ((4,4,4,1)+P0^4 and
(4,4,3,2)^3+P0^2; both models pass both verifiers), UNSAT for the other five (matches
`controls/c13-5-4`). The (7,2,2) control is degenerate (0 admissible M classes). The CPro1
N=18 model-check control was NOT done (the A1/A2 encoders are specific to 19 = 3q+1 rows).

## Controls (frozen)
CPro1 PA(18,8,6) must pass both verifiers; mutated copies must fail. Encoder controls: the
same generator with (N,k,s)=(13,5,4) (same excess-3 structure, exists by deleting 3 rows of
an OA(16,5,4)) must be SAT for some case and its model must verify; (7,2,2) must be UNSAT.
The canonicalized CPro1 18-array must satisfy its own N=18 normalized CNF (model check).

## Stop rules (frozen)
* Valid 19x8 array found: stop search, write strict text + SHA256, verify with both
  verifiers, message Main immediately.
* All cases UNSAT with checked LRAT proofs for M1 and agreeing M2 verdicts: report
  "optimum 18" as a candidate for parent verification (with the 18 construction).
* Any case unresolved at its time limit is UNKNOWN; the overall verdict is then UNKNOWN.
* Cycle limit 2 h (until ~05:10 host time), <=4 CPU processes, <=8 GiB, checkpoints <=30 min.

## Status at end of cycle 1 (2026-10-17 ~05:20 host time) -- overall verdict UNKNOWN
Live numbers: `STATUS.json` (regenerate with `python3 src/summarize.py`).
* No 19-row witness. M3 local search NOT run this cycle (CPU spent on exhaustive search).
* ms00 E0 (all columns (4,3^5) = KPD({3,4*},19) with 8 classes): UNSAT within A1 by two
  pipelines (M1 kissat DRAT -> drat-trim -> lrat-check, 486/486 ok; M2' CaDiCaL LRAT,
  486/486 ok); quad-graph list independently reproduced. RESTRICTED to balanced columns.
* ms02, ms03, ms04, ms05: every A2 skeleton case UNSAT with checked proofs (845/845 ok),
  single pipeline only (no independent generator/encoder yet).
* ms07, ms08: all 482+482 cases UNSAT in pass 1 (no proof, 30 s); proof pass started.
* ms01: 3184 UNSAT (pass 1) + 31 UNKNOWN at 30 s; proof pass partially done.
* ms06: 376 UNSAT + 106 UNKNOWN; ms09: 28 UNSAT + 43 UNKNOWN (pass 1, 30 s, no proof).
* Pass-1 UNSAT verdicts without a checked proof are unchecked solver assertions, not results.
Irreducible next work: (1) resolve the 180 UNKNOWN skeleton cases (longer runs, or a finer
split that also fixes the special columns' size-4/5 blocks); (2) finish the proof pass;
(3) independent replication of A2: second skeleton generator (e.g. orbit-count check
labeled count = sum c0!/|Aut|) and a Q0B-style independent encoder with CaDiCaL LRAT.
Disk: this lane holds ~60 GB (cases19/ 8.6 GB partial proofs of abandoned M-class runs,
m2q0b/ 24 GB LRAT, cases19q0/ 12 GB); nothing deleted.

## Amendment A3 (recorded 2026-10-17T05:33 host clock, before any A3 solving): full-skeleton split of
## the undecided A2 cases (all of them have only P1 = (4,4,3,3,3,2) special columns)
Scope: the 180 A2 cases left UNKNOWN by pass 1 (ms01 31, ms06 106, ms09 43); may also be
applied to any other A2 case of ms01/ms06/ms09. Soundness note:
1. Fix an A2 case: P0 skeleton S, rows labeled as in `encode_skel.rows_of`. In any valid
   array of this case each special column c has two size-4 blocks A_c, B_c, one size-2 block
   P_c and three triples. Necessary conditions (validity only): blocks of a column are
   disjoint; two rows that already agree (common P0 quad or common earlier special block)
   are never in a common block; row budget 2 - L <= |T(r)| + w(r) <= 2 with
   w(r) = sum_c e_c(r), e = +1 (A,B), 0 (triple), -1 (P) (A2 facts); during search the bound
   uses that each remaining column changes w(r) by at most +1 and at least -1.
2. `src/extend_p1.py` enumerates all (A_c, B_c, P_c) satisfying 1, choosing within each
   class of rows with identical history (same P0 set T(r) and same roles so far) only the
   lowest-index rows. Such rows are interchangeable under row permutations fixing S and all
   earlier choices, so every placement is equivalent to an enumerated one. Both orders of
   A_c, B_c are enumerated; results are deduplicated by isomorphism of colored incidence
   graphs (P0 quads, special blocks tied to their column, rows), which only merges placements
   related by Aut(S), A/B swaps or permutations of identical P1 columns.
3. Completion CNF per full skeleton (`src/encode_full.py`): every non-triple cell fixed
   (P1 column: A -> 0, B -> 1, P -> 5, triples 2..4; P0: quad -> 0, triples 1..5), each row's
   leave degree l(r) = 2 - |T(r)| - w(r) is known; constraints: exactly-one cells, triple
   counts 3, AMO agreements, row r misses <= l(r) rows and <= L pairs miss overall (equality
   by counting), value precedence among triple symbols of each column, lex(row i) <=
   lex(row j) for rows with identical fixed pattern. Breaking constraints are lex-leader for
   one row-major order, so every valid completion has an image satisfying all of them.
4. Verdicts: a full skeleton is decided only by an UNSAT answer whose proof is checked
   online (kissat binary DRAT streamed into drat-trim -i, its LRAT streamed into lrat-check;
   stream SHA-256 recorded) or by a SAT model verified by both verifiers. Timeouts/errors
   stay UNKNOWN. An A2 case is UNSAT only if all of its full skeletons are.
Disk rule (cycle 2): no CNF/proof is stored for new work (`src/stream_check.py`); CNFs are
regenerated deterministically from the spec + encoder (SHA-256 recorded).

## Cycle-2 verification plan (recorded 2026-10-17T06:19 host clock)
* ms06/ms09 undecided A2 cases: the full-skeleton split of A3 explodes there (22,782 full
  skeletons for ms06_s00028), so they are decided directly: the identical A2 CNF
  (encode_skel, regenerated in memory; SHA-256 must equal the pass-1 CNF) is solved by
  CaDiCaL 3.0.1 with LRAT streamed into lrat-check (`src/run_hard.py direct`), limit 3600 s.
  ms01 undecided cases use A3 (`src/run_hard.py a3`, kissat DRAT -> drat-trim -> LRAT ->
  lrat-check, streamed).
* Independent replication of A2 (M2): generator `src/gen_skel_b.py` (nauty genbg) is compared
  case-for-case with gen_skel by isomorphism (`src/compare_skel.py`); encoder
  `src/encode_skel_b.py` (no shared code; column-pair 4-clauses, binomial counts, totalizer
  row identity, different symmetry breaking) solved by CaDiCaL with streamed LRAT
  (`src/run_m2skel.py`) on every skeleton of every non-balanced multiset.
* M1 proofs for the remaining pass-1 UNSAT A2 cases: stored pass-1 CNF, kissat DRAT streamed
  into drat-trim and lrat-check (no new proof files).
* PA18 positive control: `src/control18.py` (18-row variants of both skeleton encoders).

## Process-stopping deviation log (recorded 2026-10-17T06:33 host clock)
Parent safety rule (received 06:2x): stop owned processes cooperatively only; no SIGKILL;
subprocess.run(..., timeout=...) itself SIGKILLs. Past SIGKILLs sent by this lane:
* Cycle 1, `src/run_cases.py` (subprocess.run timeout -> SIGKILL to kissat): 196 = cases19
  M-class runs 4 (900 s) + trials/pb1 3 + trials/cov1 3 (600 s) + sample pass 6 (300 s,
  archived in archive/skel-sample-pass0) + A2 pass 1 180 (30 s). Every one of these cases is
  recorded as UNKNOWN (returncode -1); none was ever counted as UNSAT.
* Cycle 2, `src/stream_check.py` revision 1 (Popen.kill): 7 SIGKILLs, all to drat-trim /
  lrat-check after a SAT answer in (13,5,4) controls: module test 3, inline M2 (13,5,4) test
  2, control13_m2.py 2. No production case was affected (all production results so far are
  UNSAT on the non-kill path).
* All other stops in this lane were SIGTERM (bash kill/pkill default, 'timeout' utility).
New rule applied from now: `src/stream_check2.py` (native limits kissat --time / cadical -t /
drat-trim -t, bounded waits, SIGTERM only, processes that survive SIGTERM are left running and
reported, case UNKNOWN) and runner revisions `src/run_hard2.py`, `src/run_m2skel2.py`,
`src/run_proofpass_stream2.py`. Old files are kept unchanged. The revision-1 direct runner
was stopped with SIGTERM to its main process at 06:29; its two in-flight cases
(ms06_s00148, ms06_s00150) were allowed to finish.

## Stream-check revisions 3 and 4 (recorded ~06:41 host clock; header first written with a wrong "06:50", corrected)
Parent corrections (06:3x): a checker passes only if it exited on its own with exit code 0
and printed its success line; any checker that needed SIGTERM or was left running makes the
case UNKNOWN; per-case checker wall time <= 1200 s (+60 s grace), drat-trim native -t set
consistently. `src/stream_check3.py` implements this; `src/stream_check4.py` additionally
fixes the drat-trim clock (drat-trim starts before the streamed solve, so it gets
-t = solver limit + check budget, while the post-solve wall bound stays check budget + grace).
drat-trim prints 's TIMEOUT' and exits 0 on its own timeout, which the gating rejects
because 's VERIFIED' is required too (smoke D2 of revision 3). Runner revisions
`src/run_hard4.py`, `src/run_m2skel4.py`, `src/run_proofpass_stream4.py` (FIFO prefix v4)
are used for all further batches. Revision-2 batches were stopped with SIGTERM after a few
seconds (06:34, in-flight ms06_s00148 UNKNOWN; M2 test case ms06 b85 UNKNOWN); no
revision-2 result was written. Smoke results: cycle2/smoke-stream3*.json,
cycle2/smoke-stream4*.json.

## Amendment A3' (recorded 2026-10-17T07:35 host clock, before production use): partial split
For A2 cases whose special columns are all P1 (ms01, ms06, ms09), fix only the blocks of the
FIRST m special columns (m = 1 used for ms09): `src/extend_p1q.py SPEC OUT m` (q-generalized
copy of extend_p1.py; for q = 6 it reproduces extend_p1.py exactly, checked on ms09_s00001 [NOTE: this compares two copies of the same algorithm; the independent cross-check is extend_b.py, which gives the same counts]:
815 placements, identical lists), with the same necessary conditions and orbit reduction
(A3 note 1-2) and the budget bound that every remaining (free) column changes w(r) by at most
+1 / at least -1. Soundness: in any valid array choose any P1 column as the fixed one; its
(A, B, P) is equivalent under row permutations preserving the P0 skeleton to an enumerated
placement; the remaining P1 columns stay interchangeable. Subcase CNF `src/encode_partq.py`:
encode_skel constraints with the fixed column's cells fixed (A -> 0, B -> 1, P -> q-1, other
rows restricted to the triple labels 2..q-2), value precedence only among triple labels in the
fixed column (A/B order is fixed by the placement), row lex only between rows with identical
fixed pattern (P0 set and fixed-column role), column lex only between consecutive identical
free special columns; all lex-leader for one row-major order. Control
(cycle2/control13-part.json, (13,5,4)): SAT subcase with a valid model exactly in skeleton
ms07_s00001, all subcases of the other all-(4,4,3,2) skeletons UNSAT with checked proofs.
An A2 case is decided UNSAT by A3' only if every subcase is UNSAT with an online-checked proof
(kissat DRAT -> drat-trim -> LRAT -> lrat-check, stream_check4). Timeouts are UNKNOWN.

## M2 for the hard cases (recorded 2026-10-17T07:41 host clock, before production use)
* M2 partial split for all-P1 cases (ms01, ms09 hard cases): independent enumerator
  `src/extend_b.py` (class-count assignments of rows to A/B/P, budget bounds re-derived,
  orbit representatives under the skeleton automorphism group found by brute force plus the
  A/B swap; no networkx, no code shared with extend_p1/extend_p1q) and independent subcase
  encoder `encode_skel_b.build_part` (M2 clause families; first-occurrence order among the
  triple labels of the fixed column and equal-count labels of free columns; lex only between
  consecutive identical free columns; P0 label fixing unchanged), solved by CaDiCaL with
  streamed LRAT (`src/run_m2part.py`, stream_check4). Cross-checks: extend_b reproduces the
  M1 enumerator counts (ms09_s00001: 815 placements, ms01_s01260: 62) and the (13,5,4) control
  gives the same per-skeleton placement counts and the same single SAT subcase as M1
  (cycle2/control13-m2part.json vs cycle2/control13-part.json).
* M2 for ms06 hard cases: direct encode_skel_b CNF with CaDiCaL + streamed LRAT
  (`src/run_m2skel4.py`), as for all easy cases.

## Amendment A3'' (recorded 2026-10-17T08:05 host clock, before production use): batching
One-column placements of an A2 case are solved in batches (default 100) instead of one CNF
each: `src/encode_partbatch.py` (M1) and `encode_skel_b.build_partbatch` (M2) add a selector
t_i per placement with the clause (t_1 | ... | t_b); the batched column gets exact label counts
and, guarded by t_i, placement i's fixed cells (and, M1 only, placement i's row-lex constraints
between rows with identical fixed pattern). A satisfying assignment satisfies some t_i together
with exactly that subcase's constraints, so a batch CNF is UNSAT iff all its subcases are UNSAT
(A3' soundness carries over). Controls: (13,5,4) all-(4,4,3,2) skeletons, all placements of a
skeleton in one batch: SAT (valid model) exactly for ms07_s00001, all others UNSAT with checked
proofs, for both M1 (kissat DRAT -> drat-trim -> lrat-check) and M2 (CaDiCaL LRAT). Timing on
ms09_s00001: 815 single subcases ~0.38 s each; batches of 100 ~2.7 s per batch; one batch of
815: 19 s solve + 74 s check. Non-batched A3' results already written remain valid; a case is
decided when every placement is covered by a checked UNSAT single-subcase or batch result.

## M2 encoder version 2 (recorded 2026-10-17T10:06 host clock, before production use)
`encode_skel_b.build_v2` = M2 clause families (column-pair 4-clauses, binomial counts,
totalizer row identity) with symmetry breaking that is entirely lex-leader for one row-major
order: first-occurrence order of the P0 triple labels (replacing the P0 label fixing),
first-occurrence among equal-count special labels, top-down lex between consecutive identical
special columns, and row lex between consecutive rows of identical P0 type (order-literal
encoding, independent code from M1). Controls: (13,5,4) all skeletons SAT exactly for
ms04_s00000 and ms07_s00001 (valid models), all others UNSAT with checked proofs; PA18:
the CPro1 normal form satisfies the 18-row variant `build_v2g(base_quad=False)` with all cells
fixed and three corrupted arrays are UNSAT (cycle2/control18/control18-m2v2.json);
build_v2g(base_quad=True) is byte-identical to build_v2 on ms06 b85. Used for all M2 direct
runs (`src/run_m2skel5.py`, results cycle2/m2skel_v2). The partial/batched M2 builders keep
the version-1 breaking (P0 label fixing, no row lex).

## Amendment A3-exact (recorded 2026-10-17T12:19 host clock, before use)
`src/encode_full2.py` = encode_full.py plus exact leave counts: z(r,r') is forced false when the
two rows agree in some column, and each row r misses AT LEAST l(r) rows (in addition to at most
l(r)). Valid for every array of the case: row r agrees with exactly sum_c (n_{c,A[r][c]} - 1)
= 18 - l(r) other rows because the agreeing sets of different columns are disjoint, so it
misses exactly l(r) rows. Used for A3 full skeletons that the original encoding left UNKNOWN
(first: ms01_s02573 f00012, where kissat hit 600 s; there only rows 16 and 18 have l = 2, so the
leave graph would need a double edge). Results: cycle2/a3/<tag>/fNNNNN_exact.json (originals
untouched); online check kissat DRAT -> drat-trim -> LRAT -> lrat-check (stream_check4).

## Cycle-2 notes for the parent audit (recorded 2026-10-17T12:19 host clock)
* Manifest: cycle2/MANIFEST-cycle2-20261017T121839.sha256 (sha256 a11dcb372709c90958edf49fd40c3f43b008eeb9be50753a23853f8b6349819d,
  5,823 entries: case index, 5,577 specs, both skeleton lists and maps, ext.json files, job
  lists, sources, controls, docs); later supplements will be additive.
* genbg flags used: -q -Z1 -d2:0 -D{tmax}:4; `genbg -help` lines logged in
  cycle2/genbg-help-flags.txt (-Z#: two second-class vertices have at most # common
  neighbours; second class = the P0 quads).
* Deviation: at 12:17 a shell redirection of mine wrote a 12-byte file /tmp/x (child-PID list)
  outside the repository. Not deleted (rule); owner may run `mv /tmp/x ~/.Trash/`.
* The PA18 control exercises the skeleton encoders with an EMPTY skeleton only; the cover
  (skeleton/placement enumeration + fixed cells) is exercised by the (13,5,4) controls
  (A2, A3', A3'' for M1 and M2; M2 v2).

## CHECKER FINDING and response (recorded 2026-10-17T12:30 host clock)
Parent finding (confirmed here, cycle2/checker-smoke/checker-smoke.json via src/smoke_checkers.py):
tools/drat-trim/lrat-check (upstream 2e3b2dc0, lrat-check.c bf07c2ac...) is UNSOUND: on the
satisfiable CNF 'p cnf 1 1 / 1 0' it prints 'c VERIFIED' with rc 0 for the LRAT lines '2 0 0' and
'2 0 1 0'. drat-trim rejects the empty proof, ASCII '0' and binary empty-clause proofs on that CNF
and accepts a genuine proof (controls N3-N5, P1). Consequences:
* lrat-check is no longer an acceptance criterion anywhere. Acceptance = drat-trim exited on its
  own, rc 0, 's VERIFIED' on the solver's DRAT (stream_check5.py: kissat_drat / cadical_drat;
  CaDiCaL writes binary DRAT; no lrat-check process).
* UNCERTIFIED (kept, never deleted): cycle-1 E0 M2' (m2q0b/, 486 graphs, CaDiCaL LRAT +
  lrat-check); all CaDiCaL-only direct results cycle2/hard/*.json produced by run_hard.py /
  run_hard4.py / run_hard5.py directc (stream_check/2/3/4 cadical_stream); the two *_r2.json
  reruns; the M2 (13,5,4) controls control13-m2*.json and cycle2/m2skel* (none in production).
  The M1 kissat paths are unaffected: their 'checked' flag required drat-trim's own verdict
  (cycle-1 check_proofs.py and stream_check rev 1-4 kissat_stream all gate on drat_trim_verified).
* Re-certification running: E0 M2' with the unchanged encoder encode_q0b.py + CaDiCaL DRAT ->
  drat-trim (src/run_m2q0c.py -> m2q0c/; CNF SHA equals the cycle-1 M2' CNF, e.g. g001);
  all 106 ms06 hard cases with kissat DRAT -> drat-trim (src/run_hard8.py -> cycle2/hard5/);
  the two stalled-check subcases with CaDiCaL DRAT -> drat-trim (smoke-stream5 D1/D2 checked;
  formal results via src/rerun5.py -> *_r3.json). All further M2 runs use run_m2skel6.py /
  run_m2partbatch2.py (CaDiCaL DRAT -> drat-trim).
* drat-trim stalls: both earlier drat-trim stalls had binary DRAT streams of exactly a multiple
  of 64 KiB (589,824 and 6,356,992 bytes); they were treated as UNKNOWN (SIGTERM at budget) and
  are re-certified with CaDiCaL proofs of other lengths.

## Scripts added after the checker finding (recorded 2026-10-17T12:37 host clock)
* src/stream_check5.py (kissat_drat, cadical_drat; drat-trim-only acceptance; unique FIFO dirs);
  src/smoke_stream5.py -> cycle2/smoke-stream5.json; src/smoke_checkers.py -> cycle2/checker-smoke/.
* M1: src/run_hard8.py (directk/directc via stream_check5 -> cycle2/hard5/; its 'part' mode is
  NOT usable: it still calls the rev-4 API), src/run_proofpass_stream5.py (remaining pass-1 UNSAT
  cases, kissat_drat, same output dir cycle2/proofstream, records carry revision 5),
  src/rerun5.py (CaDiCaL DRAT -> drat-trim reruns of single subcases/batches -> *_r3.json).
* M2: src/run_m2q0c.py (E0 M2' re-cert -> m2q0c/), src/run_m2skel6.py (-> cycle2/m2skel_drat/),
  src/run_m2partbatch2.py (-> cycle2/m2part_drat/).
* Controls: src/control13_v5.py -> cycle2/control13-v5.json (all (13,5,4) pipelines incl. the
  production A3 full encoders via src/encode_fullq.py / src/encode_full2q.py, q-generalized copies
  of encode_full.py / encode_full2.py; byte-identical CNFs for N = 19 checked on ms01_s02573
  full skeletons 0, 12, 500).
* Aggregation/binding: src/summarize5.py -> STATUS5.json; src/bind_check.py ->
  cycle2/binding-pass1.json.

## Amendment M2-strict: strict LRAT checker for M2 (recorded 2026-10-17T13:04 host clock, before production use)
src/lratstrict.c (sha256 c2151bd5b7c4ddd53e3f2762b6a0d7956568437cd12710bbc7dbcf06263cf4bc), built in the lane with `cc -O2 -Wall -Wextra` (Apple clang 17.0.0)
as bin/lratstrict (sha256 2f08a0f9dcaa45658a6bd915eb9bda48ab69d38490e0d54832b6e07e98dae20c). Strict RUP-only ASCII-LRAT checker: exactly C CNF clauses
with literals in 1..V; strictly increasing addition ids; no tautological lemma; positive hints only
(no RAT); each hint must refer to a live clause, have no true literal and at most one unassigned
literal; the conflict must occur exactly at the last hint; deletions must name live clauses;
VERIFIED (rc 0) only after a verified empty clause. Controls (cycle2/lratstrict-tests.json via
src/test_lratstrict.py): the parent's negatives N1 ('2 0 0') and N2 ('2 0 1 0') on 'p cnf 1 1 / 1 0'
are rejected and P3 verifies; 20 genuine CaDiCaL LRAT proofs ((13,5,4) UNSAT skeletons, a 19-row
M1 CNF, five M2 build_v2 CNFs) verify; 140 guaranteed-invalid mutations of them (drop the
empty-clause line, drop its last hint, empty hint list, unknown hint id, deletion of a used clause,
truncation, non-increasing id) are all rejected; 28 checks of genuine (13,5,4) proofs against the
two SAT (13,5,4) CNFs are all rejected. Cross-check (cycle2/lratstrict-crosscheck.json): E0 g000
(encode_q0b CNF, same SHA as the drat-trim run) UNSAT verified (912 MB LRAT, solve 91 s, checked
online) vs the drat-trim pipeline 83 s + 87 s; M2 ms01 b0..b49 agree with the drat-trim results.
Use: src/stream_check6.py cadical_lrat_strict (acceptance = lratstrict's own exit, rc 0,
's VERIFIED'; budget by bounded wait + SIGTERM => UNKNOWN), runners src/run_m2skel7.py
(-> cycle2/m2skel_strict; skips cases already certified in cycle2/m2skel_drat) and
src/run_m2partbatch3.py (-> cycle2/m2part_strict). Both runners honour a stop file
(cycle2/STOP-m2skel7, cycle2/STOP-m2partbatch3). M1 keeps kissat DRAT -> drat-trim, so M1 and M2
now use different solvers, different encoders/generators and different proof checkers.
Aggregation: src/summarize6.py -> STATUS6.json.

## Deviations recorded 2026-10-17T13:23 host clock
* 13:05: a timing measurement redirected /usr/bin/time output to /tmp/zt_3, /tmp/zt_9 and
  /tmp/zt_19 (three files of a few bytes each, outside the repository). They were not deleted
  (rule); the owner may run `mv /tmp/zt_3 /tmp/zt_9 /tmp/zt_19 ~/.Trash/`.
* 13:07-13:22: a trimmed-core size test (scratch/trimtest-130730) started drat-trim with
  `-l FIFO` and no native -t limit. Its zstd reader had been launched in a '( ... &)' subshell,
  which did not survive, so drat-trim blocked opening the FIFO (no CPU used) until the harness's
  900 s command timeout ended the shell command (signal not observed by me). No output was
  produced or used. The measurement was redone by src/measure_retention.py (Popen, drat-trim
  -t 1200, bounded waits, SIGTERM only).
* 13:06: M2 easy runner run_m2skel7.py stopped through its stop file cycle2/STOP-m2skel7 (no
  signal), to add proof retention requested by the parent.

## Parent route A and disk floor (recorded 2026-10-17T13:33 host clock)
* Parent decision: M2 uses CaDiCaL binary DRAT -> drat-trim -i (standard checker) with a strict
  verdict; lratstrict may run only as an extra signal and is NOT counted (the 139 lratstrict-only
  ms01 records in cycle2/m2skel_strict are not counted and are re-run). No proof retention beyond
  existing files; per-case records carry CNF SHA, solver command/version/seed, verdict, streamed
  proof bytes + SHA-256, drat-trim time, so the parent can re-solve a stratified sample.
  Retention measurements kept: cycle2/retention-measure.json (+ cycle2/retention-measure/ small
  compressed test outputs: 17.4 MB + 58.1 MB).
* src/stream_check8.py (strict verdict) had a parser bug: drat-trim prefixes every output line
  with '\r', so splitting on '\n' found no 's ' line; its smoke (cycle2/smoke-stream8.json) failed
  and the six records it wrote (ms01 b634-b639, all UNSAT with checked=false) plus their claims were
  moved to archive/rev8-verdict-parsing-bug-20261017T1331/ (NOTE.txt). Fixed in
  src/stream_check9.py (lines stripped of '\r' on both sides; the set of 's ' lines must be exactly
  ['s VERIFIED']); smoke cycle2/smoke-stream9.json all expected (UNSAT verified, SAT/timeout
  's NOT VERIFIED'). Production M2 runners: src/run_m2skel9.py (-> cycle2/m2skel_drat, claims
  m2d9_*, stop file cycle2/STOP-m2skel9) and src/run_m2partbatch5.py (-> cycle2/m2part_drat, claims
  m2pbd9_*, stop file cycle2/STOP-m2partbatch5). Records carry stream_check_revision 5 or 9.
* Parent run-wide disk floor: no new work when filesystem free < 12,000,000,000 bytes. The rev-9
  runners check it before every case/batch (and then write their stop file); src/disk_guard.py
  (sleeping watcher, 120 s) creates both stop files and SIGTERMs the M1 runners and their
  solver/checker children if the floor is crossed, writing cycle2/DISK-GUARD-<time>.json.
* Per-case retention index: src/retention_index.py -> cycle2/proof-retention-index.json.

## Amendment A3''-ms06 and CPU accounting (recorded 2026-10-17T15:01 host clock, before production use)
* M1 for the remaining ms06 hard cases uses the one-column batched split (A3'/A3'', valid for all-P1
  multisets; ms06 is all-P1): src/run_hard9.py = run_hard6.py with stream_check9.kissat_drat (kissat
  binary DRAT -> drat-trim -i, strict 's ' line verdict), claims pb9_<tag>, stop file
  cycle2/STOP-hard9, parent disk floor before every batch. Batch size B is a command-line parameter
  (100 or 400); every batch record lists its placement indices explicitly, so its CNF is
  encode_partbatch.build(spec, [ext.full[i] for i in indices]) for any B. First case ms06_s00150,
  whose direct proof (2.55 GB DRAT) could not be checked in the 1200 s checker budget
  (cycle2/hard5/ms06_s00150.json, UNSAT, checked=false, drat-trim SIGTERM => UNKNOWN).
* CPU accounting (parent clarification 14:4x): the cap counts concurrently busy solver AND checker
  processes. My earlier "load 4"/"3 production" figures counted runner pipelines (solver + drat-trim,
  for revision 4 also lrat-check), so cap compliance during cycle 2 is NOT established and peaks
  above 4 busy processes were possible (parent will report this as a deviation). Measured 14:47
  (scratch/busy-sample-144*.txt): kissat solve 29/30 runnable while its streaming drat-trim 1/30;
  a drat-trim backward check 30/30; a short-batch CaDiCaL pipeline ~0.7-0.8. From 14:57: one
  pipeline while the parent's R8 runs, at most two afterwards.
* The 73 untouched ms06 tags were reserved with claim files 14:47 so both run_hard8 runners stopped
  at a case boundary; the reservations were released by src/release_reservations.py into
  archive/claims-released/ (collision-checked); archive/MANIFEST.tsv records source, destination and
  SHA-256 of every cycle-2 archive move (earlier moves backfilled).

## Amendment STAGED (recorded 2026-10-17T15:25 host clock, frozen before first use; parent-approved design)
Files (sha256):
  355ba0513a0d3ecd35cd878ba84805e8b774480bc49ce3aab0da1490fdc08615  src/stream_check10.py
  2af97702883d3bee2b0ed488c7133decb0c8abf45cb748478de9c90515098b7a  src/run_hard10.py
  536f0107b5cc348cf0d20bf4f1515f8386ac0739d82910cbe93fad126096820e  src/run_m2_10.py
  77da58732823ec4a7a51fda773554bc77fcdbbe75c8d0e327ba8c4fc399384a0  src/rss_watchdog.py
  2b66c81a8a82f3874a7f735e8aac07d0e83d0ac231df03e138721a60194194bc  src/smoke_stream10.py
  2f5b3c8adfbd33e90a20093d2bbb26f47a41cc4feed58ee3bebf152a83e00461  src/summarize8.py
* Pipeline: solver binary DRAT -> FIFO -> Python thread (SHA-256, byte count, zstd level 1 into memory;
  never written to disk) -> after the solver exits with rc 20: decompressed proof -> drat-trim -i -t
  BUDGET (BUDGET <= 1200 s). Solver and checker of one pipeline never run at the same time.
* Acceptance predicate (record field checked=True) iff ALL of: solver exited on its own with rc 20; no
  proof cap hit; drat-trim exited on its own with rc 0; the list of 's ' lines of drat-trim's output, each
  stripped of '\r', is exactly ['s VERIFIED']; SHA-256 and length of the proof replayed into drat-trim
  equal those of the streamed proof. Anything else: not checked -> UNKNOWN for the case/batch.
* Caps: raw proof <= 1,258,291,200 bytes (1200 MiB) and compressed buffer <= 524,288,000 bytes
  (500 MiB), else SIGTERM to the solver and UNKNOWN; checks of proofs > 314,572,800 bytes (300 MiB)
  serialized by cycle2/tokens/bigmem; solver limits as given on the command line; drat-trim -t budget.
* CPU: one exclusive flock token (cycle2/tokens/tN, N < COUNT; COUNT read from cycle2/tokens/COUNT
  at every acquisition) held across CNF construction, solve and check (and around extend_p1q/extend_b
  for split cases). COUNT = 4 only when no non-staged pipeline of this lane is running (otherwise
  COUNT = 4 minus the number of such pipelines).
* RAM: src/rss_watchdog.py samples all lane runner/solver/checker/helper processes every 2 s; if their
  summed RSS exceeds 8 GiB it SIGTERMs the newest pipeline (bounded wait 60 s, no SIGKILL), lowers COUNT
  by one and writes cycle2/RSS-WATCHDOG-<time>.json. It also appends busy-process samples (state R
  solver/checker processes min/mean/max per 30 s window, lane RSS max, COUNT) to
  cycle2/watchdog-samples.log. drat-trim peak RSS is recorded per case (5 s sampling).
* Disk: rev-10 pipelines write only small JSON records; runners check the 12e9-byte free floor before
  every case/batch (stop file on violation).
* Records: CNF SHA-256 and size, solver command/version/seed, proof SHA-256 and bytes, zbuf bytes,
  verdict lines, solve/encode/check seconds, token and token wait, peak RSS -- enough for the parent's
  deterministic stratified re-solve (kissat --seed=1; CaDiCaL default seed).
* Runners: src/run_hard10.py (M1 ms06: direct encode_skel, solver limit 600 s, -> cycle2/hard5;
  one-column split encode_partbatch B=100 -> cycle2/part/<tag>), src/run_m2_10.py (M2 direct build_v2
  -> cycle2/m2skel_drat; split extend_b + build_partbatch -> cycle2/m2part_drat). Aggregation:
  src/summarize8.py -> STATUS8.json. Smoke: src/smoke_stream10.py -> cycle2/smoke-stream10.json.

## Amendment REV11 (recorded 2026-10-17T15:57 host clock, frozen before any production use; supersedes STAGED/rev 10 for new work)
Parent audit (PA19StagedAudit) found escape paths in rev 10 (token/bigmem released while a SIGTERM survivor
could still run; watchdog not attributing helper/CNF memory and lowering COUNT without stopping the owner; no
admission re-check after token acquisition; replay hash taken before successful delivery; compressed frame tail
not counted against the cap). Rev-10 records stay as they are (summarize9 still applies the rev-10 predicate to
them). Admission was paused 15:34:36 (COUNT=0 + stop files); the last rev-10 stage ended 15:35:32.
Files (sha256):
  40ee9ac20a4a1f128c7279f3f443169becefd35f1d5007d4a41d9b1e0be3ae99  src/stream_check11.py
  03b8ff3cf4cbb033b5572155dd747126060551b3268c819fad3fcdbb42f95e92  src/run_hard11.py
  efa3a94981a433967d680f6040bb7359aa6d9a56c7628f208ae33bb96f9170d4  src/run_m2_11.py
  0b6484c96d0e7b0a27744f3cb5148ff1489641501fa2b422c4b73481aa1ec285  src/rss_watchdog2.py
  3c68303f0fdeb1a2650f62d304e0e9c60a1fd79be31cc576ad4b5db56d76c1c3  src/smoke_stream11.py
  62d13ae18795b2e5cf4bc8cea5221bbd71c7b759cb634b79b2549327a095975d  src/smoke11_helper_runner.py
  256f4ad86d22a538965f2d2f54fc6157328d96f9c238d6aed848caaf19c04dc1  src/summarize9.py
  24c05e6b77cfa0e71433b5a7c2ac4d5fb1bc261557e7d76d05078822148fa1db  src/list_pending2.py
* Acceptance (checked=True) iff: solver exited on its own with rc 20; no proof cap hit (raw 1200 MiB; compressed
  500 MiB INCLUDING the final zstd frame tail); the proof reader reached EOF without error; drat-trim exited on its
  own (not after SIGTERM, not quarantined) with rc 0; its 's ' lines (each stripped of '\r') are exactly
  ['s VERIFIED']; replay_ok: every decompressed chunk was written completely to drat-trim's stdin, the zstd frame
  ended (eof), stdin closed without error, and SHA-256 + length of the delivered bytes equal those of the streamed
  proof; no admission refusal and no SIGTERM abort. Anything else: not checked (UNKNOWN).
* Caps are checked after every read chunk (<= 1 MiB): buffers may exceed a cap by one chunk plus zstd state before
  the solver is stopped -- size limits, not instantaneous RSS limits.
* No silent release: a solver/checker/helper surviving SIGTERM + 60 s is quarantined (cycle2/QUARANTINE-*.json);
  the token and bigmem lock stay held until it exits by itself (5 s polling, no further signals); Token.__exit__
  never releases while an owned child is alive.
* Admission re-checks (runner ABORT flag, the runner's stop file cycle2/STOP-hard11 or cycle2/STOP-m2r11, free disk
  >= 12e9 bytes) immediately after every token acquisition and before every CNF construction, helper start, solver
  start and checker start. A refused/aborted stage writes no result record (its record goes to cycle2/aborted/),
  the claim is released (archive/claims-released + archive/MANIFEST.tsv) and the runner ends. SAT results are never
  routed to aborted.
* Runner SIGTERM handler: sets ABORT; forwards SIGTERM to live registered children; abandons the stage (SystemExit)
  only when no child is alive and none is being started. SIGTERM is not blocked around child creation (a blocked
  mask is inherited across exec: smoke run 2 showed an unstoppable helper); records are written with SIGTERM blocked.
* CPU (parent decision): COUNT <= 2 (cycle2/tokens/COUNT). One token covers the stage's solver or checker plus the
  runner's concurrent compression / decompression+feeding, or the runner's CNF construction, or one helper
  (extend_p1q/extend_b through run_helper): at most 2 busy processes per token, 4 per lane. Busy-process samples
  (rss_watchdog2: busy_all = state R among runners and their descendants, and solver/checker only, per 30 s window
  with the window's first and last sample clock) are observations, not the bound.
* RAM: src/rss_watchdog2.py groups processes by owner runner (runner + all descendants, full command-line
  matching), samples every 2 s, trips above 8 GiB by SIGTERM to the runner holding the most recently acquired token
  (else the largest group's runner), bounded wait 60 s, then COUNT-1 (min 1); disk floor -> creates both stop files.
* Smoke (src/smoke_stream11.py): run 1 (15:45) was ended by its own test-L watchdog (matching on a truncated command
  line missed the test runner and targeted the largest group; no result JSON; fixed: full command lines); run 2
  (15:48-15:53, cycle2/smoke-stream11-run2.json): A-K pass, L fail (helper not stopped: inherited blocked SIGTERM
  mask; fixed); run 3 (15:54-15:56, cycle2/smoke-stream11-run3.json): all 12 tests pass (UNSAT checked; SAT models
  verified by both verifiers; native timeout and raw cap UNKNOWN with SIGTERM effective in 0.15 s; COUNT=1
  serialization; forged empty clause rejected; compressed-tail cap boundary; stubborn solver and stubborn checker
  quarantined with the token retained until exit; feed failure UNKNOWN despite 's VERIFIED' rc 0; admission refused
  after acquisition; watchdog trip on helper memory stops the token holder and its helper before token release).
  Deviation: the fixed output path cycle2/smoke-stream11.json was rewritten by runs 2 and 3; copies of runs 2 and 3
  were made before/after (run-2 copy taken while run 3 was still running).

## Amendment RUNCONF-REV11 (recorded 2026-10-17T15:58 host clock, before use; pending the parent's explicit GO)
Files (sha256):
  a709bb5e7301d9ffda6241fdb1f356da1cb114a45892d8e7c0c4aa7e0ac750ee  cycle2/smoke-stream11-run2.json
  e12296fea3faf2ff9ad048adfe1cbd667e8d713222b6f4b2a55b359d3602c3f6  cycle2/smoke-stream11-run3.json
  e12296fea3faf2ff9ad048adfe1cbd667e8d713222b6f4b2a55b359d3602c3f6  cycle2/smoke-stream11.json
  cd9c9b713685e3e9c7fd6cf03bfb746fd5b786ca361302daa611acf2c2f730ac  cycle2/tags-ms06-m1-direct.txt
  de45b05c69d5df8b55fadfbe2b8bd409bda6d3b1cb7b26f6db5ac2d6e26fe7c2  cycle2/tags-ms06-m1-split.txt
  2e55adec2846472f4194bc97c826537ba10335058610607bd4dc94fadf38512a  cycle2/m2-jobs-easy.txt
  42d6570a7e31ded28f97498ffbd5f2c303b7f178ea010c9417a3c819ad7b090c  cycle2/m2-jobs-part.txt
  21fdc72f7ed21feda7cbc56d246421453c1e8c7dc3a47ddb82425f5b8d985c96  cycle2/m2-jobs-hard-direct.txt
* Smoke-output overwrite deviation: cycle2/smoke-stream11.json was written by smoke run 2 and rewritten by run 3
  (same fixed path). Copies: smoke-stream11-run2.json (taken while run 3 was running, before its final write)
  and smoke-stream11-run3.json (taken after run 3); hashes above. From now on every smoke attempt writes a new
  file name (no overwrite).
* Run configuration (frozen values; no other configuration is used):
  - cycle2/tokens/COUNT = 2 (parent decision); rss_watchdog2: `python3 src/rss_watchdog2.py 2 30` (log
    cycle2/watchdog2-samples.log), started before any rev-11 runner; the rev-1 watchdog is stopped only after
    rss_watchdog2 runs and no rev-10 holder exists.
  - M1 runner R1: `python3 src/run_hard11.py direct 300 1200 1 <tags-ms06-m1-direct.txt>` (kissat solve limit
    300 s, drat-trim budget 1200 s), then `python3 src/run_hard11.py split 600 1200 100 $(python3 src/list_pending2.py m1split)`.
  - M1 runner R2: `python3 src/run_hard11.py split 600 1200 100 <tags-ms06-m1-split.txt>` (per batch of 100
    placements: kissat limit 600 s, budget 1200 s), then the R1 direct command, then the R1 split command (claims
    are shared, so every tag/batch runs once).
  - M2 runners, started when M1 nears completion: `python3 src/run_m2_11.py direct 600 1200 1 <m2-jobs-easy.txt>`;
    `python3 src/run_m2_11.py split 600 1200 100 <m2-jobs-part.txt>`; `python3 src/run_m2_11.py direct 300 1200 1
    <m2-jobs-hard-direct.txt>` then `python3 src/run_m2_11.py split 600 1200 100 $(python3 src/list_pending2.py m2split)`.
* All pending cases remain UNKNOWN until certified under the strict predicates (summarize9).

## Amendment REV11a (recorded 2026-10-17T16:06 host clock, frozen before any production use; supersedes REV11 and RUNCONF-REV11 for new work; pending parent re-review/GO)
Audit references (PA19StagedAudit, parent IRC 2026-10-17 15:3x-16:0x). Rev 10: stream_check10.py 242-244 and 291-314
with Token 175-181/91-93 (token/bigmem released while a SIGTERM survivor runs); 269-279 (replay hash before
delivery); 217-220 (flush tail not capped); run_hard10.py 128-140 and run_m2_10.py 124-135 (no admission re-check after
token acquisition); rss_watchdog.py 63-79 (helpers/CNF not attributed; COUNT lowered without stopping the owner).
Rev 11 final (REJECT for resumption): rss_watchdog2.py 111-120 (admissions not frozen before SIGTERM/grace), 102-106
(largest-runner fallback), 49-50 (runner discovery not lane-exact); stream_check11.py 427-429 (no admission re-check
inside the acquired bigmem lock before drat-trim); run_hard11.py 90-92 (SAT verifiers outside the token/registered
child lifecycle). The rev-11 fixes for survivor quarantine, replay delivery binding, flush-tail cap and the strict
verdict are kept unchanged in stream_check12 (= stream_check11 + the bigmem-lock re-check).
Files (sha256):
  3490b07f63409aab8eb6d554f1604f9b6f6393bf383f491d10d8aebf45e41319  src/stream_check12.py
  b3040375b2d733214f26d863d4d7afcdaa234a6bdad49d8034d59c4b1333db00  src/run_hard12.py
  da5fa0b8b924bc76ede084f1d3f09d3d65acf6de8fce7e45e578dccf84d95b39  src/run_m2_12.py
  22fb46608add73a7fa45baac777c77f1d5bebcd7cb5be5ad881a54c2ac5d347a  src/rss_watchdog3.py
  afca0710d098cbea6befc3d575b6d718fa6f9b32881fa1a604c5716026f5a090  src/smoke_rev12.py
  f96da8dfc965d4ccf8f0ebecf3e654273bec2fdbafee17f92c58da9b409b5889  src/smoke12_runner.py
  d51664cae84f7d4f54bb4da82f48e6355569a85c4f0e1b2a4236647c5eaece05  src/summarize10.py
  21256b128c376dded8767c65ff81e5b16333c79e68fcedd3af91660b45d9c15e  src/list_pending3.py
  d1fdbd7f6702e04f8df089a92be473786041bcff85dc38761a20d55e497bd857  cycle2/smoke-rev12-20261017T160257.json
  b6d3676fb48c62a52fe750bc6b75dae019a53f450f2bec7d61fff329837b5014  cycle2/smoke-rev12-20261017T160454.json
* stream_check12.py: admission re-check (ABORT, stop file, free-disk floor) inside the acquired bigmem lock immediately
  before the drat-trim spawn; refused -> UNKNOWN (admission_denied), no checker started. Records: revision 12.
* run_hard12.py / run_m2_12.py: rev-11 runners on stream_check12; stop files cycle2/STOP-hard12 / cycle2/STOP-m2r12.
  run_hard12.handle_sat writes the raw solver output and the decoded array FIRST, then runs both verifiers via
  run_helper (registered ACTIVE/SPAWNING lifecycle, SIGTERM forwarding) under a CPU token with admission re-checks;
  refusal/abort -> candidate preserved, verification_deferred. SAT results are never routed to cycle2/aborted/.
* rss_watchdog3.py: runner discovery requires the exact absolute lane path of a runner script as a command-line
  argument (runners are started as `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/<runner>.py ...`); on a trip it FIRST sets COUNT=0 and
  creates STOP-hard12, STOP-m2r12, STOP-hard11, STOP-m2r11 (admissions frozen, never re-enabled by the watchdog),
  THEN SIGTERMs only a proven token owner (pid recorded in a token file that it holds open, lsof) and waits up to
  60 s; with no proven owner nothing is signalled (pause + operator review). No largest-group fallback.
* Production helpers (extend_p1q.py, extend_b.py, verify_pa.py, verify_pa2) start no subprocesses (code inspection:
  no subprocess/fork/Popen/multiprocessing), so SIGTERM to the registered child reaches the whole helper.
* Smoke (src/smoke_rev12.py, new output name per attempt, never overwritten): attempt 1 (cycle2/smoke-rev12-20261017T160257.json):
  M1, M2, W1, W2, V_normal, V_stopfile pass; V_sigterm failed its 10 s bound because the test's fake verifier
  ('sleep 30' under sh) left a sleep grandchild holding the output pipe: the shell died at once (rc -15) and the
  stage -- and its token -- waited 27 s for the grandchild (no early release). Attempt 2
  (cycle2/smoke-rev12-20261017T160454.json, fake verifier 'exec sleep 30'): all 7 pass -- bigmem wait + stop file and
  + disk floor -> UNKNOWN with 0 drat-trim spawns; RSS trip: COUNT=0 and stop files at t, SIGTERM at t+0.58 s to the
  proven owner, its helper rc -15 before token release, the waiting runner started 0 children and was refused after
  COUNT was set back to 1; no eligible owner -> nothing signalled, the memhog saw no SIGTERM; SAT verifiers run under a
  token (rc 0/0), are deferred under a stop file (0 children), and a SIGTERM during verification terminates the
  verifier (rc -15) with the candidate preserved. These are controls of the code paths, not a proof of the RSS cap.
* Run configuration (replaces RUNCONF-REV11): COUNT=2; `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/rss_watchdog3.py 2 30` started first (rev-1
  watchdog stopped after it runs); M1 R1 `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_hard12.py direct 300 1200 1 <tags-ms06-m1-direct.txt>`
  then `... split 600 1200 100 $(python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/list_pending3.py m1split)`; M1 R2 `... split 600 1200 100
  <tags-ms06-m1-split.txt>` then the R1 commands; M2 later with `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_12.py` and the arguments of
  RUNCONF-REV11 (list_pending3 for m2split). Aggregation: src/summarize10.py -> STATUS10.json.

## Note (recorded 2026-10-17T16:07 host clock): retained failed smoke attempt; GO preparation
* Retained failed attempt: smoke_rev12 attempt 1 (cycle2/smoke-rev12-20261017T160257.json, log cycle2/smoke-rev12-run1.log):
  6/7; V_sigterm failed because the fake verifier's sh left a sleep grandchild holding the output pipe for 27 s; the
  token stayed held during that time (no early release). Attempt 2 passed 7/7.
* Prepared, not executed: launch plan cycle2/launch-plan-rev12-20261017T160702.json (absolute-path commands, R1 direct
  queue 58 tags starting ms06_s00255, ms06_s00257, ms06_s00207; R2 split queue 9 tags starting ms06_s00212,
  ms06_s00214); proposed src/retire_rev10.py (moves the 371 rev-10 records -- 291 M2 direct, 27 M2 batch, 53 M1
  batch -- plus their batch summaries to archive/rev10-superseded-<time>/ with MANIFEST lines so that rev 12
  recomputes them; only on parent agreement).

## Rev-10 record retirement (recorded 2026-10-17T16:09 host clock; parent-approved MOVE, COUNT=0, no runner alive)
src/retire_rev10b.py (sha256 5fe43ab4e017a3ac74836a014e46caae33d40fddd1c1093e49da2b9ce9103f1f). Predicate: JSON under
cycle2/{hard5,part,m2skel_drat,m2part_drat} with stream_check_revision == 10, or summary_batched.json written by
run_hard10.py/run_m2_10.py; never ext.json. Selected 375 = 291 M2 direct + 27 M2 batch + 3 M2 summaries + 53 M1
batch + 1 M1 summary (count check enforced). Dry-run lists: cycle2/rev10-retire-dryrun-20261017T160916.json and
-160921.json (sha256 ab8d0498...f53e, the one used). Read-only scan of 17,703 files under
institute/runs/six-lane-2026-10-16/review/pa19*/: 0 references to any selected path. before.json:
cycle2/rev10-retire-before-20261017T160921.json (c2c65371...1244); moved by collision-checked os.rename to
archive/rev10-superseded-20261017T160921/<relative path>; after.json: cycle2/rev10-retire-after-20261017T160921.json
(2827bf0b...a7a8): all 375 at their new paths with identical sha256, old paths absent, all 10,041 other inventoried
files unchanged. 375 archive/MANIFEST.tsv lines with reason "rev10 staged pipeline rejected by PA19StagedAudit; superseded by REV11a final predicate".
These cases (M2 ms01 direct/batches, M2 ms06 b101, M1 ms06_s00204) are open again and will be recomputed under rev 12.

## Amendment REV11b (recorded 2026-10-17T16:25 host clock, frozen before use; replaces the watchdog of REV11a)
Audit reference: PA19StagedAudit REV11a final review, MAJOR rss_watchdog3.py 92-98 and 132-142 ('lsof shows the
token file open' does not prove that the pid holds the flock; the pid is signalled after several lsof calls, so a
release/exit plus pid reuse could direct SIGTERM to a non-owned process). Parent decision: a watchdog that never
signals. src/rss_watchdog4.py (sha256 b178c185ceba2f20e9b61abf51eeb81746e170659225dd7b3f1044ee24875b28): same
owner grouping (exact absolute runner paths) and sampling as rss_watchdog3; on a trip (lane RSS > 8 GiB) it sets
COUNT=0, creates cycle2/STOP-hard12 and cycle2/STOP-m2r12, writes cycle2/RSS-ALERT4-<time>.json (time, lane RSS,
per-group RSS, token metadata) and exits; no process is signalled (no signal import, no kill/terminate path);
running stages remain bounded by their native limits; recovery is a parent decision. Disk floor -> stop files.
Diff vs rss_watchdog3: cycle2/diff-rss_watchdog3-to-4.diff (sha256 dfafe4c4...92ed7).
Smoke src/smoke_rev12b.py (728f9c39...2a4a): attempt 1 cycle2/smoke-rev12b-20261017T162342.json (6b6eb8c5...7386,
retained failed attempt: its static check was a substring search that matched the docstring sentence stating that
no kill/terminate code exists; S1 and S2 passed); attempt 2 cycle2/smoke-rev12b-20261017T162424.json
(d271618f...8def): all pass -- AST check finds no signalling code; a 400 MiB memhog fixture (group RSS 430,496 KB)
trips the watchdog: COUNT 1 -> 0, both stop files, alert written with signals_sent 0, the memhog receives no SIGTERM
and ends by itself; afterwards (COUNT set back to 1 by the smoke) a waiting runner is refused by STOP-hard12 with 0
children. Stop files archived (MANIFEST); COUNT = 0. Run configuration as REV11a with `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/rss_watchdog4.py 2 30`
in place of rss_watchdog3.

## Launch under GO (recorded 2026-10-17T16:28 host clock)
* Parent GO received ~16:25. rss_watchdog4 started 16:25:5x (first sample window 16:25:54-16:26:25, pid 27737);
  rev-1 watchdog (pid 4363) SIGTERM at 16:26:4x, exited within the bounded wait (handled by 16:26:46); COUNT=2 at
  16:26:50; R1 and R2 (run_hard12.py with absolute paths, launch plan cycle2/launch-plan-rev12-20261017T160702.json)
  launched 16:27:01; first stages held tokens t0 (R1 pid 27929) and t1 (R2 pid 27930) by 16:27:52.
* Deviation list additions: (a) smoke_rev12b attempt 1 (cycle2/smoke-rev12b-20261017T162342.json) failed its static
  check (substring search matched the docstring) -- retained; (b) smoke_rev12 attempt 1 (V_sigterm grandchild) --
  retained; (c) stop files created by watchdog smokes were archived with MANIFEST lines:
  archive/stopfiles-smoke12-W1-*/, archive/stopfiles-smoke12-W2-*/, archive/stopfiles-smoke12b-20261017T162449/;
  (d) smoke_stream11 fixed output path rewritten by runs 2 and 3 (copies kept, see RUNCONF-REV11).

## Amendment REV11c (recorded 2026-10-17T17:00 host clock, frozen before use; parent decision ~17:0x)
Trigger: lane RSS 5,109,408 KB at 16:35:49-16:36:21 from extend_p1q on ms06_s00214 (387,814 raw placements).
Files (sha256):
  82b00193481ecb86eed4159b27e3a168094eaebb194175894e61e72f5ada9efe  src/stream_check13.py
  b2ad202144b7ed16a4f3a93ce4e45205643d40e7c55a511d316f30965580c917  src/run_hard13.py
  562715bd61d8fc8787f42e92a82ac0c3b725fb7daa3ced8fb329eb9105de8a69  src/run_m2_13.py
  7054526cfab66e400016511ff40f23a1aeb79924adefab71f6f7816e6b3f6283  src/extend_exclusive.py
  fca1f42f52d03d2149f6b63056e6f2e2246d2ba52785cb542cb77d63ae76462e  src/smoke_rev13.py
  3b00279255fb1634b596af168faa0df83282d9d4e15c1f8c88aa6c31243ba5b7  src/with_token.py
* Per-helper RSS guard (stream_check13.run_helper): the helper's RSS is SAMPLED every second (ps); above 5 GiB the
  helper -- the runner's own registered, not yet reaped Popen child -- gets SIGTERM; run_helper returns only after the
  helper has exited (the caller's token held throughout); a cap trip makes the enumeration a failure (UNKNOWN for the
  item) even with rc 0. This is a sampled guard, not an instantaneous OS memory bound. run_helper also takes an
  exclusive helper lock and refuses to start when the sampled lane RSS + 5 GiB exceeds 8 GiB; these do not reserve
  memory against other pipelines, therefore:
* Exclusive extends (parent condition): memory-heavy enumerations run ALONE. Procedure: stop the production runners at
  a stage boundary (stop file cycle2/STOP-hard12, which also refuses their next admissions), COUNT=0, then
  src/extend_exclusive.py acquires exclusive flocks on all token files t0..t7 and the bigmem lock (draining any held
  stage) and runs the enumerations one by one under the guard; temporary output renamed to ext.json only on success;
  extend-receipt-*.json / extend-failed-*.json per item; cycle2/extend-exclusive-<time>.json summary; locks released.
  COUNT is restored to 2 (and STOP-hard12 archived with a MANIFEST line, runners relaunched) only after the helper
  has exited and ext.json is retained.
* Reservations: pb9_ claims hold every ms06 tag without ext.json (7 at 16:5x, 95 more at 17:0x) so that no rev-12
  runner starts an unguarded extend_p1q; released with MANIFEST lines once their ext.json exists (or kept, with a
  failure record, if the guard trips).
* run_hard13.py / run_m2_13.py: rev-12 runners on stream_check13 (extend via temporary file, receipts, failure records,
  no crash on helper failure); used for new split work after this amendment; batch-only work on existing ext.json may
  continue with run_hard12/run_m2_12 (identical batch path).
* src/with_token.py: auxiliary commands (aggregation) run under a CPU token.
* Smoke src/smoke_rev13.py (new output name per attempt): H1 cap -> SIGTERM own child; H5 stubborn helper above the
  cap -> waited for, token held, cap_hit failure; H2 headroom refusal; H3 helper lock; H4 extend failure/receipt paths.
  Run inside the paused window.

## REV11c pre-relaunch confirmations (recorded 2026-10-17T17:05 host clock)
Files (sha256):
  548dd9db14cd86423a8a6419e17e06c48d3a28e3ef81fe71de4a7fa6d082a856  src/summarize11.py
  a06a0924ee38bccd7758c542709b8cf11ae7dcf83d63809cac57dd7e93c347a4  src/list_pending4.py
  bf4fe845124970238fd6caead0953a18afbb7295e211a123ea5e2ca59e6e8ef8  src/release_rev10_claims.py
  fde2553cae1713b6c9f300fca680b66b755aac9b0275f6dc79c3241b74e43ffe  cycle2/smoke-rev13-20261017T170337.json
  eb3e23363fab8cfa753fb5de2dfa897e25bb9d4dc3f148d7e4018285503fc6ee  cycle2/check-partial-ext-20261017T170532.json
* Aggregation for revision-13 records: src/summarize11.py (-> STATUS11.json) and src/list_pending4.py accept stream_check
  revisions 11, 12 and 13 under the SAME full predicate (checked, drat_trim_verified, drat-trim 's ' lines exactly
  ['s VERIFIED'], replay_ok, reader_ok, no admission_denied, no aborted_by_sigterm); revision-10 records are never
  counted (retired). summarize10/list_pending3 (revisions 11-12 only) are superseded for aggregation.
* Helper failure leaves the item UNKNOWN: an extend helper with non-zero rc or an RSS-cap trip writes no ext.json
  (its temporary output is never renamed; smoke_rev13 H4/H5, cycle2/smoke-rev13-20261017T170337.json); a truncated
  ext.json is refused by run_hard13.run_split (JSON parse error, no batch record, no summary;
  cycle2/check-partial-ext-20261017T170532.json).
* The 5 GiB per-helper cap and the lane-RSS headroom check are SAMPLED guards (ps every second / at start), not
  instantaneous OS bounds.
* 295 claims left by rev-10 runners whose records were retired were released (src/release_rev10_claims.py; MANIFEST
  reason "claim of a rev-10 runner whose record was retired; released so rev 12/13 recompute the item").
* Exclusive window: STOP-hard12 and COUNT=0 at 17:01:01; R1 stopped 17:01:42, R2 17:03:29; smoke_rev13 17:03:37-17:03:54
  (COUNT=1 for the smoke only); extend_exclusive m1 for the 7 reserved tags started 17:04 (COUNT=0, flocks t0-t7+bigmem).

## Relaunch after the REV11c exclusive window (recorded 2026-10-17T17:21 host clock)
* extend_exclusive m1 17:04:22-17:20:35 (cycle2/extend-exclusive-20261017T172035.json): ext.json for ms06_s00216
  (204,699 raw / 17,496 orbits, peak 1,133,552 KB), s00228 (227,496 / 2,526, 503,280 KB), s00266 (262,175 / 65,755,
  3,135,472 KB), s00285 (193,331 / 48,672, 2,527,312 KB), s00287 (135,731 / 34,040, 1,716,320 KB), s00297 (178,717 /
  44,839, 2,330,336 KB); ms06_s00291: per-helper RSS guard tripped (sampled peak 5,270,640 KB > 5 GiB), helper rc -15,
  no ext.json, cycle2/part/ms06_s00291/extend-failed-20261017T171808.json; its reservation is kept; the tag is UNKNOWN
  (another route needs a parent decision).
* STOP-hard12 archived (MANIFEST) and the 6 extend reservations released (MANIFEST) at ~17:21; COUNT=2 at 17:21:03;
  R1b and R2b (run_hard12 direct 300/1200, shared h5_ claims, then list_pending4 m1split -- tags without ext.json stay
  reserved, so no unguarded extend) and R3 (run_hard12 split 600/1200/B=100 on ms06_s00204 and the 6 new ext.json
  tags, batch-only; ext.json existence and num_full consistency checked before launch) launched ~17:21 with absolute paths.

## Amendment RUNCONF-S00291 (recorded 2026-10-17T17:22 host clock, before use; parent-approved ~17:2x)
ms06_s00291 (its exclusive extend tripped the 5 GiB per-helper guard; no ext.json) is attempted by the DIRECT route only:
`python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_hard13.py direct 1800 1200 1 ms06_s00291` -- kissat 4.0.4 --seed=1 native limit 1800 s, drat-trim
check budget 1200 s (unchanged), unchanged proof caps (raw 1200 MiB, compressed 500 MiB incl. tail), full revision-13
predicate (summarize11), inside the normal COUNT=2 token scheme (no helper, no exclusive window). Any non-verified
outcome (timeout, cap, check budget, refusal) stays UNKNOWN; no budget or cap is raised without a new parent decision.
Its pb9_ reservation stays in place (no split attempt).

## Second exclusive window and M2 continuation (recorded 2026-10-17T20:24 host clock)
* COUNT=0 since 19:16:42. The direct queues drained; R3 was stopped as a childless token waiter at 19:16:50 and released its claim. The already-admitted s00291 direct fallback finished at 19:26:45: UNSAT, full rev13 checked, solve 290.28 s, check 379.96 s, DRAT 600,779,427 bytes, checker peak RSS 802,960 KB. It was not duplicated.
* The queued exclusive tool acquired t0-t7 and bigmem at 19:26:45. Three fresh representative M2 jobs (receipt cycle2/extend-exclusive-20261017T192651.json): 1:2749 0.3 s, 1,460 raw /6 aut /138 orbits (completed before a 1 s RSS sample); 9:20 1.3 s, 31,850 /2 /8,373, sampled RSS 39,552 KB; 9:55 4.6 s, 107,298 /2 /27,082, sampled RSS 107,776 KB. The remaining 49 missing M2 lists then completed in 110.34 s wall; all 74 partial-job ext.json files now satisfy num_placements == len(placements), no guard hit. Existing lists were skipped, not rewritten.
* Ten M1 direct-UNKNOWN tags were extended sequentially/exclusively under the same frozen sampled 5 GiB guard: nine succeeded (s00310, s00311, s00368, s00370, s00389, s00406, s00410, s00414, s00430); s00468 hit the guard at sampled RSS 5,252,800 KB, helper rc -15, no ext.json. Its reservation remains; the tag is UNKNOWN pending an approved alternate route. No cap increase or helper retry.
* Window completed by 20:23:44. Nine successful-list reservation claims and STOP-hard12 were moved with MANIFEST lines; receipt cycle2/exclusive2-resume-20261017T202415.json. COUNT=2 restored at 20:24:51; the s00291 admission-ordering step was skipped because it was already certified.
* Continuation uses two pipelines with the already-frozen settings: one M1 batch-only chunk (s00266/s00285/s00287/s00297, run_hard12 split 600/1200/B=100), one independent M2 ms01 easy-direct chunk (run_m2_12 direct 600/1200, ranges from m2-jobs-easy.txt with multiset 1). All script paths are absolute. Further bounded M1 batch and M2 direct/partial chunks follow with COUNT<=2.


## Bounded alternate-solver batch rerun (recorded 2026-10-17T22:18 host clock, before use)
* M1 ms06_s00368 left exactly one unresolved batch, batch_42500_42599: the original staged kissat record reports solver rc20 in 0.09 s but reader_ok=false with zero DRAT bytes; it is UNKNOWN, not accepted. The other 59,895 placements were checked. No inference of nonexistence is made from the missing stream.
* src/rerun_batch12.py (sha256 3c1aeda56e43ae62f2072bdb416fa790fc4d5cdb5c970a2151205b01131c82f0) reuses encode_partbatch on the original explicit indices, under the normal token; CaDiCaL binary DRAT goes through the unchanged stream_check12 staged pipeline (strict standard drat-trim, same caps), with limits 600 s solve /1200 s check. The CNF SHA must match the original record or checked is forced false. Output uses the existing `<batch>_r3.json` rerun convention, never overwrites. SAT handling delegates to run_hard12.handle_sat (candidate preservation plus registered verifier helpers under a token). Acceptance and aggregation predicates are unchanged.
* Checkpoint cadence deviation: the 21:27:32 manual checkpoint was followed by a token-gated aggregation whose completion returned at 22:08 (gap >30 min). No timestamp was backdated. src/checkpoint_clock.py (sha256 0ab2e03701cef3894ed84d984301eda95310e296f026282f4a51ffcd8c10425b) now appends a metadata-only receipt every 15 min: current host clock, COUNT, free bytes, latest watchdog line, and the timestamped last-saved STATUS11 counts explicitly labelled as not a live recount. No stage admission, token/config changes, signals or research work.


## Amendment RUNCONF-S00468 (recorded 2026-10-17T22:37:52-0700 host clock, before use; parent-approved)
* ms06_s00468 is retried by the direct route only: `python3 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_hard13.py direct 1800 1200 1 ms06_s00468`. Kissat 4.0.4 --seed=1 native solve limit 1800 s; drat-trim check budget 1200 s; full revision-13 predicate. Its helper-cap failure and pb9 reservation remain; no helper retry and no cap increase.
* Proof caps unchanged: 1200 MiB raw, 500 MiB compressed INCLUDING the final zstd frame tail, with the documented at-most-one-read-chunk margin before a sampled/size stop (not an instantaneous memory bound). Compression is entirely in memory; no compressed-tail/proof bytes are retained on disk, no CNF file is written or copied. Projected retained growth for this one-case chunk is <1 MiB of JSON/FIFO/possible SAT-candidate metadata, conservatively; result records normally occupy a few KiB.
* Pre-launch floor check at the heading's host time: available 13,558,776 KB = 13,884,186,624 bytes, above 12,000,000,000 bytes even after the projected retained growth. Admission re-checks the live floor after token acquisition and before construction/solver/checker. COUNT remains 2; this job must hold one of the two existing tokens and never increases concurrency. Timeout, cap hit, feed/read/refusal/check failure remain UNKNOWN.


## Amendment S00468-SIX-UNIT (recorded 2026-10-17T22:55:03-0700 host clock, before any subcase solve; parent-approved)
* The approved full direct retry ended UNKNOWN at 22:51:49: compressed-buffer cap hit (raw prefix 831,520,768 B, compressed 524,511,652 B), own kissat child SIGTERM/rc -15, no checker started. All original receipts remain; no cap increase.
* Freeze cell (r,c)=(8,6), ZERO-BASED (ninth row, seventh/first special column). It is not a base-quad fixed cell (base columns are 0..5). `encode_skel.py:37` allocates all cell variables first in row/column/symbol order, so x[8,6,s] has literal 421+s. The exact six subcases append respectively `421 0`, `422 0`, `423 0`, `424 0`, `425 0`, `426 0` to the SAME pinned CNF body (only the DIMACS clause count is increased by one).
* Base SHA-256: `137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994`. Each stage regenerates encode_skel under its token and byte-compares to the pinned file before taking the mapped cell literal. Every receipt records base SHA, base body/header/length, exact unit bytes, and subcase SHA/length.
* Cover: exactly one symbol holds in this cell in any base model; the six symbol-unit subcases exhaust the base. No other clause, symmetry, placement list, reduction or deeper split is introduced.
* Frozen contract: `cycle2/s00468-six-unit-contract.json`. Runner `src/run_s00468_cell.py` SHA `964e2c61d00e9ab08ff9196de2a18432b7f74b81c35a95eb2dca67b0f069b37e`; strict aggregator `src/summarize12.py` SHA `7933b3b10c4ff2fc7e9fbaef30134de8fe10616a699ad9abfe1fdc6a2c60fae0`, producing STATUS12.json from the unchanged base summarize11 plus this bound six-unit route.
* Per subcase: kissat 4.0.4 --seed=1, 300 s solve /1200 s check, unchanged proof caps/full rev13 predicate, live floor check at every admission, one subcase at a time under an existing COUNT<=2 token. No helper. No proof/CNF file retention; projected six-receipt growth <1 MiB; compressed proof including frame tail stays in RAM.
* Stop rule: SAT is pinned and verified, then stop immediately. Any miss remains UNKNOWN; other frozen subcases may finish but the case counts only when all SIX exact-index records are bound and strictly checked. No deeper split without a new parent decision. `summarize12` independently rebuilds each expected unit-CNF hash and refuses missing/wrong identity, unit, base hash, subcase hash or predicate; summary files are not trusted and SAT records are always listed.


## Amendment DISK-MARGIN-14 (recorded 2026-10-17T23:29:00-0700 host clock, frozen before resumed stages)
* Parent 23:26 release permits versioned multi-stage guards: every NEW stage must see >=12.2e9 free bytes plus projected retained growth. No owner deletion/thinning; proof and CNF copies remain forbidden. At 23:28:14 the fresh filesystem check showed 13,571,604 KB available, above the new threshold. COUNT remains 0 during preparation.
* `stream_check14.py` is the frozen stream_check13 implementation with only documentation, the admission constant `DISK_FLOOR = 12200000000 + 64*1024*1024` (effective minimum 12,267,108,864 bytes), and the receipt revision tag 14 changed. Lifecycle/quarantine, proof caps, native limits, replay/delivery checks and certification predicate are unchanged. The existing post-token, construction, helper, solver and post-bigmem checker checks all use this stronger floor; the 64 MiB headroom conservatively covers the bounded next chunk's JSON/FIFO/claim metadata. Compressed proof/tail stays in RAM, retained proof bytes zero.
* Exact source hashes and configuration: `cycle2/guard14-freeze-20261017T232900.json`. Guard SHA `1a82f5aff5ee38411daa232ee4c1ea0cf59e09c7b34df7c3a14f7e5764c47219`. New import-only runner variants are `run_hard14.py`, `run_m2_14.py`, `run_s00468_cell14.py`, and `with_token14.py`; same STOP-hard12/STOP-m2r12 controls and COUNT<=2. No old frozen source was changed.
* `aggregate14.py` and `summarize14.py` accept prior 11/12/13 and new 14 records under the same full predicate; retired 10 stays excluded. The frozen s00468 six-unit cover is unchanged (row8,column6, literals421..426, exact pinned base). Existing s00..s04 records are preserved; only missing subcases run. The cover aggregator accepts both prior13 and new14 with identical binding/predicate, producing STATUS14.json. `list_pending14.py` uses that same record predicate.
* Boundary-only control (`cycle2/guard14-boundary-control-20261017T232814.json`): no child or token acquisition, COUNT stayed0; 12.2e9 and effective-minimum-minus-one refused, exact effective minimum and plus-one admitted. This tests the new admission threshold only, not a new proof-checker smoke or a memory bound.
* The three pre-margin controllers were tokenless and childless at 23:27:26, then stopped with SIGTERM at 23:27:35: old M1/M2 claims released, cell runner wrote a deferred receipt; no proof interrupted. STOP files are archived with MANIFEST lines only after another fresh live-floor check. New-margin stages then resume with COUNT2; if the stronger gate fails they defer and the parent is notified once.


## M2 ms09_b00002 capped-direct fallback (recorded 2026-10-17T23:56:42-0700 host clock, before enumeration)
* The independent direct attempt is UNKNOWN (compressed-buffer cap at raw prefix 1,191,182,336 B /compressed 524,714,246 B, own CaDiCaL child SIGTERM); its base CNF SHA is `22d35806c973c8efff24333ebb82b08414f00f7dcbc5c31d927585c773d8a224`. No cap increase or direct miss-to-UNSAT inference.
* Use the already-frozen M2 all-P1 one-column cover (extend_b + build_partbatch, A3'/A3'') for this same skeleton: c0=5, three special profiles (4,4,3,3,3,2), one row type {1,2,3,4}, two empty rows. No new symmetry reduction or deeper split. Every enumerated placement must be covered by strict checked UNSAT batches, else the case stays UNKNOWN; SAT is pinned and stops the runner.
* Enumeration is exclusive while COUNT=0 with all token flocks+bigmem, using `extend_exclusive14.py` SHA `dc10f6082522242ddbf6f761d546fed01cc8eb8a416b2fe82e686435c66d3e6e`: only the stream_check14 import/margin differs from the approved exclusive tool; same sampled5GiB own-child guard, no cap retry. Subsequent batches use run_m2_14 split600/check1200/B=100 under normal COUNT<=2 and the identical full predicate.
* Retained-growth projection: this skeleton has one t=4 class (at most2 role choices: triple/pair), five singleton classes (at most8 choices each), and one empty class of size2 (no pair role by the row-budget condition, at most6 A/B choices). Thus raw class assignments <=2*8^5*6=393,216 and orbit placements no more than that. Each JSON placement has exactly4+4+2 row numbers <=18, bounded conservatively by60 bytes, so the complete placement file is <24 MiB plus tiny headers/receipts; the frozen64MiB margin covers it. No proof/CNF copies or >10MiB snapshots are made (the placement list is new scientific data, not a snapshot/copy).
* The helper and each batch independently re-check the live12.2e9+64MiB gate; a failure defers, keeps the case UNKNOWN and is reported once. All old receipts remain.


## Amendment RELEASE-GATE-15 (recorded 2026-10-18T00:45:42-0700 host clock, before resumed stages)
* Parent 00:44 release requires fresh free >=12,267,108,864 B PLUS projected stage retention. To enforce that literally at every inner admission rather than only process launch, the immutable guard15 variant requires 12,334,217,728 B (the released base threshold plus an additional64 MiB conservative metadata headroom). The safety floor stays12e9; no proof caps, native limits or acceptance predicates change.
* `stream_check15.py` SHA `13cea48adcee59507d44e5c1985f89d26ccae3bb65b25068b2b5b1331423e22b` differs from guard14 only in documentation, this disk threshold, and receipt revision15. Existing post-token/construction/helper/solver/post-bigmem-checker gates all apply it. No retained proofs or CNF copies; no new snapshot/copy >10MiB.
* Complete runner/helper/aggregation hashes and configuration: `cycle2/guard15-freeze-20261018T004542.json`. The new import-only variants are run_hard15/run_m2_15/with_token15/extend_exclusive15/rerun_batch15, with unchanged STOP-hard12/STOP-m2r12 and COUNT<=2. aggregate15/summarize15/list_pending15 accept prior approved records and new15 under the identical full predicate; retired10 stays excluded. The completed frozen s00468 six-unit records remain13/14, are accepted unchanged, and are never rerun.
* Fresh preparation gate: 17,637,208,064 B. Boundary-only controls (no child/token acquisition, COUNT0) refused the base threshold and effective-minimum-minus-one, admitted exact effective minimum and plus-one. These are admission controls, not proof/memory-cap verification.
* The old guard14 M2 controller was childless/tokenless at00:44:38 and stopped with SIGTERM, releasing its active claim at00:45:00; no proof interrupted. Recovery STOP files are archived with MANIFEST only after another fresh live gate; then COUNT2 and bounded existing-list M1/M2 chunks resume.


## Frozen remaining M2 ms09 one-column inventory (recorded 2026-10-18T01:08:13-0700 host clock, before new helpers)
* Parent approved the existing all-P1 A3'/A3'' route for the remaining26 uncompleted easy ms09 cases; no new reduction/deeper split. `cycle2/ms09-split-inventory-20261018T010710.json` SHA `d45499bdcb4718a38fafa0f82f49c8d28d06ab680444b6e1ad2cad6c82ca414a` (63,242 B) freezes exact pending IDs, the input/source hashes, all43 unchanged hard-list SHA/counts, skipped complete cases b1/b2, and the no-truncation rule.
* Complete mathematical denominator: ALL compatible per-row-class (A,B,P) count assignments satisfying the frozen row-budget/capacity/totals, modulo the full skeleton automorphism group and A/B swap. No subset is sampled/dropped. As clarified by the parent, the unknown exact numeric orbit count is not invented before generation; a successful COMPLETE list's num_placements and SHA are pinned before any batch solve. A missing/partial/capped/failed list supplies no denominator and stays UNKNOWN.
* Resource bound script `freeze_ms09_split_inventory.py` SHA `6e715a75e1774f9cb3218cf43e6ce4fdf66a91dc1ef1a56dfddbea1dc656be9f`: finite class-count DP includes all existing per-class choices and totals but ignores only inter-class incompatibilities, so it upper-bounds actual raw assignments and orbit placements. Output bound is60 bytes per (4,4,2) placement plus65,536 B headers/receipts. Controls on completed b2/b20/b55 confirm actual_orbits<=actual_raw<=DP upper; no placement materialization occurred.
* Nineteen helpers fit the frozen64MiB per-stage allowance and may run only at the natural exclusive window: 9:3,9:7,9:21,9:30,9:33,9:35,9:40,9:42,9:44,9:46,9:50,9:54,9:59,9:61,9:63,9:66,9:67,9:69,9:70. Complete per-job byte bounds are in the inventory (maximum eligible67,029,436 B). Their summed worst-case output bound is696,450,004 B, not a disk reservation; every helper rechecks the fresh guard15 gate.
* Seven helpers are DEFERRED before execution because their rigorous conservative bound exceeds64MiB: 9:49 70,548,136 B;9:52 71,048,236 B;9:58 94,215,856 B;9:60 71,048,236 B;9:62 94,215,856 B;9:65 135,220,336 B;9:68 135,220,336 B. Parent was given these exact bounds and options (stronger bound-specific outer gate, or a frozen count-only compatibility-bound pass); no assumption that the fixed64MiB guard covers them.
* Helper execution: owned lane TMPDIR, COUNT0, all token+bigmem flocks, one helper, sampled5GiB own-child guard, no cap increase. Only incomplete/missing jobs are generated; all existing43 hard lists and completed b1/b2 remain unchanged. Subsequent batches stay600/1200/B100 and strict checked coverage for EVERY placement under COUNT<=2; all stops/failures remain UNKNOWN.


## Bound-specific post-lock helper gate (recorded 2026-10-18T01:15:21-0700 host clock, frozen before execution; parent-approved)
* Parent chose stronger bound-specific outer gates for the seven >64MiB projections, not a count-only pass and not a cap increase. New `extend_ms09_growth_guarded.py` SHA `ad50ee64210c7b342b95f9076119067edded2beb05bc37246b064649f884dc59` reuses stream_check15.run_helper unchanged. Exact delta vs extend_exclusive15 and every per-job threshold/source hash are frozen in `cycle2/ms09-growth-wrapper-delta-20261018T011521.diff` and `cycle2/ms09-growth-wrapper-freeze-20261018T011521.json`.
* A spawn hook runs AFTER all token/bigmem locks and the unchanged run_helper helper lock are held. It computes current conservative additional-data usage and the WHOLE remaining generator-plan bound, then requires fresh free >=`max(12,334,217,728,12,267,108,864+this_frozen_output_bound+1,048,576)`. After writing the admission receipt it rechecks immediately before the registered Popen call, with no intervening lock wait. Internal guard15 and the in-flight12e9 safety floor remain. No new proof/certification logic.
* `lane_new_data_accounting.py` SHA `6f2b57ad7de99179a8343153ee0eb68ff7711f257cece1f75b52439e4f35a584` charges the FULL logical/allocation bytes of every lane entry born or modified since05:22 on Oct17 (one minute before the recorded05:23 cycle-2 baseline), plus unknown-birth entries. Moves preserve their charges; copies with old mtimes are charged by birth time; modified baseline files are charged in full. Symlinks are counted without following. Usage is max(exact selected logical-byte sum, exact selected st_blocks*512 sum), a conservative upper accounting set, not an invented exact net baseline subtraction.
* At01:13:58: selected logical300,343,959 B, allocated430,231,552 B, charged usage upper430,231,552 B; no stat errors. Remaining original10GiB allowance10,307,186,688 B; this wrapper enforces a stricter10,000,000,000 B cap (remaining9,569,768,448 B). Whole remaining26-helper output+receipt bound1,395,229,972 B; reference usage+plan1,825,461,524 B fits both. Accounting/remaining allowance/whole remaining plan are recomputed in each admission receipt; any unknown accounting or cap failure defers before spawn.
* Inventory SHA is hard-pinned; sources/skeleton SHA rechecked after lock waits; existing43 hard lists checked unchanged before/after each chunk. Owned lane TMPDIR is set before helpers. Only requested missing jobs run; no overwrite or regeneration of complete lists. Exact complete list SHA/size/raw/aut/num_placements is pinned before any batch solve; actual output must fit its frozen bound. All gate/helper/cap/validation failures stop the chunk UNKNOWN and preserve receipts/partial temp output, with no automatic retry.


## Enumeration helper safety correction V2 (recorded 2026-10-18T01:26:05-0700 host clock, frozen before any new ms09 generation)
* Parent static read correctly found that old run_helper's communicate wait was unbounded and its monitor covered RSS only; no elapsed/in-flight-disk bound was established. That helper wrapper has NOT been used to generate these26 lists. New helper-only guard/caller variants correct this without changing placement or proof predicates. Exact hashes/deltas/config: `cycle2/ms09-helper-safety-v2-freeze-20261018T012605.json`.
* `enumeration_helper_guard.py` SHA `2d815d1cee5a5695f50b5217a6332efda911dcf4b2b305f7eb4798977fdc8986`: owned registered Popen child, existing helper flock/headroom checks, <=1s RSS/time/free sampling; helper elapsed1800s, chunk<=10800s with90s shutdown reserve, and original run deadline2026-10-18T18:31:43-07:00 minus90s. Sampled helper RSS5GiB and in-flight free floor12e9 remain. A trip SIGTERMs only that child, waits at most60s, then retains all caller token/bigmem/helper locks in creation-only quarantine until it exits. A trip or observed late completion is UNKNOWN even with rc0; no new helper starts afterward. A stubborn survivor is recorded, never SIGKILLed or silently released.
* `extend_b_x.py` SHA `9862d9eb3541cc6a50ee3959cf4e1b909e8afe2b6d448875ddc0f394b07a14fb` is the frozen generator with only module documentation and output open mode w->x changed; the complete algorithm AST is identical after that mode normalization. Exact generator diff: `cycle2/extend-b-output-x-delta-20261018T012605.diff`. Original sources remain untouched.
* `extend_ms09_growth_guarded_v2.py` SHA `4e323121b6c83569bc7856f6d4066701f7eac6abe88b7278ae3d30a695627158`: preserved post-all-lock/accounting/growth hook, plus deadlines rechecked after accounting immediately before Popen, new bounded helper call, guard_tripped failure regardless of rc, x-mode receipts, absent-only exist_ok=False new directories, owned TMPDIR, and creation-only survivor receipts before lock release. Exact delta: `cycle2/ms09-growth-v2-delta-20261018T012605.diff`. Runtime PYTHONDONTWRITEBYTECODE=1. Final ext.json publish remains collision-checked rename under the sole exclusive owner locks; no existing list/receipt is overwritten.
* Required tiny-child controls (NO full enumeration rerun): `cycle2/enumeration-guard-smoke-1792311784358838000/receipt.json` SHA `a99bc8fb90993154b58bb36f7d8bdf49b1abed20ac12ebec3cab8855189839b8`, host01:23:04-01:23:49. All9 pass: elapsed, simulated in-flight floor, chunk deadline, run deadline, stubborn-child quarantine (rc0 later still guard-tripped, token/bigmem/helper flocks observed held), tiny RSS cap, expired admission with0 children, x-mode collision preserving original hash, and AST output-I/O-only generator equivalence. No owned child remained. These are resource/I-O controls, not scientific proof or proof-mutation controls.


## Final fail-closed helper supervision correction (recorded 2026-10-18T01:32:43-0700 host clock, before generation)
* Parent re-review found two V2 gaps: exceptional sampler exit could quarantine without first SIGTERM/bounded wait, and final completion checked deadlines but not the free-space floor. New `enumeration_helper_guard_v3.py` SHA `85307d5a81b0df3152f88ebcfa20aaf0ce3d7505dd910cebebb0b2bd4064544c` fixes both: supervision exceptions return UNKNOWN after owned-child bounded stop/quarantine (capacity held until exit); final disk-read error or <12e9 makes UNKNOWN even with rc0/fast completion. Startup-owned children are also cleaned up before releasing locks. Quarantine receipt I/O errors are explicitly reported and never release capacity around a survivor.
* New `extend_ms09_growth_guarded_v4.py` SHA `a03c0c2c0a4b497e4695b90145354de40c59b51458bb9278f8751aef2b863f77` only imports this final guard and corrects stale documentation: it uses the versioned H.run_helper plus stream15 registered-spawn lifecycle, not old stream15.run_helper. The growth/accounting/creation/placement/proof rules are unchanged.
* Exact final deltas/hashes/config: `cycle2/ms09-helper-final-freeze-20261018T013243.json`, `cycle2/ms09-final-helper-delta-20261018T013243.diff`, `cycle2/ms09-final-wrapper-delta-20261018T013243.diff`. The output-I/O-only extend_b_x copy is unchanged. Old V2/H sources remain untouched and have not generated any of the26 lists.
* Only new targeted tiny-child controls were run (NO repeat of the9 retained normal-path controls, NO full enumeration): `cycle2/enum-final-smoke-1792312304299525000/receipt.json` SHA `0632e87bebf69c7defaa5fad87b9bad73c44cb31bc57c6fa5bef92f0d9067185`. All4 pass: post-spawn RSS sampler exception terminates the own child (rc-15) with token/bigmem/helper locks observed held during wait; already-completed child with final simulated floor failure is UNKNOWN rc0; final read error is UNKNOWN rc0; simulated quarantine-receipt errors still retain all locks until a stubborn rc0 child exits. No owned child remained. Unchanged paths cite the earlier9-control receipt and exact SHA from the V2 amendment.
* M1 finite-cover candidate is complete and pinned separately: `cycle2/m1-complete-candidate-20261018T012523.json` SHA `cf3e87c5fd8201286aa7a2b1e09999733cab7e5018a7e49c738f91ff13d1d791` (all5,577 A2 +486 balanced E0 checked by M1). This is not parent final acceptance; independent M2 and final audit remain required.


## Structural empty cover ms09_b00003 (recorded 2026-10-18T01:45:39-0700 host clock; PENDING PARENT ACCEPTANCE)
* `cycle2/structural-ms09-b00003-proof.json` SHA `25b7df6aa32b42cff74873c33c27da5a24b008078038816d25bdd6c94b4f676a` pins the exact skeleton/list/source/map/spec hashes (mapped A2 ms09_s00003). It is STRUCTURAL/EMPTY-COVER, NOT a DRAT-certified case and NOT an unqualified0/0 pass.
* Exact input: c0=5,L=0, five P0=(4,3,3,3,3,3) and three P1=(4,4,3,3,3,2) columns; one row h in all five P0 quads, fifteen private nonempty rows, three empty rows. Total column agreements5*21+3*22=171=binom(19,2), so the at-most-one-agreement condition saturates every pair. For each row, t+e1+e2+e3=2 (t=P0-quad memberships, e=+1/0/-1 for special quad/triple/pair).
* For h,t=5 forces allthree e=-1: h must lie in each special pair. Every nonempty row already shares a P0 quad with h, so cannot be its special partner. An empty row t=0 cannot lie in any pair because -1+1+1<=1<2. No partner exists; contradiction for this exact case. The complete empty enumeration corroborates this argument but is not labelled a solver certificate.
* New fail-closed `aggregate16.py` SHA `3994ac713188aeaf984d3dcac6710f4a9eb5465fa64b2caf8c06bdbe8fe31663` /`summarize16.py` SHA `e9127efe5bb9f2b054159ad86193370f0241fbe9a07353509738e2ddb571bb8d` expose empty M2 covers separately as structural_empty_covers_pending_parent and do NOT count generic0/0. Nonempty proof predicates are unchanged. No parent acceptance is inferred.
* `freeze_ms09_batch_denominators_v2.py` SHA `98fcbaa9bee9034416f0f6416509df5ab22361641312f2582ec2c5cda20bdef6` similarly keeps structural-empty cases outside solver batch jobs, pending explicit parent acceptance. Full numerical denominators/SHA for all nonempty lists must be pinned before their batches.

