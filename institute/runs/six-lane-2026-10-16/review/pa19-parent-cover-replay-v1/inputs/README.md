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
