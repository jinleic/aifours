# Lane info-2: circular Florentine rectangle CFR(4,33) (alternates CFR(5,27), CFR(6,21) only after parent decision)

Owner: worker `InfoCFR33`. Contract (read-only, copied with SHA-256 verified): `sources/contract-info-2-cfr33.json`
(b8eca3da…ec36bd, frozen 14:37:06 PDT); pre-freeze screen `sources/info2-killcheck-screen-v2.md` (a2220cf3…ba3).
Lane opened 2026-10-17 14:40:17 PDT (`notes/lane-opened.txt`). Deadline 2026-10-18 18:31:43 PDT.

This README is append-only. Section 1 was written 2026-10-17 14:46:21 PDT (host clock) BEFORE any computation other than
read-only source pinning (`code/fetch_pin.py`). Later sections are appended checkpoints.

Only this directory is writable. No deletion/overwrite (files opened with mode 'x'; a corrected file gets a new
version name), no /tmp, no commit/push/publication/contact, no model CLI, no paid API, no global config, no
SIGKILL / Popen.kill() / subprocess.run(timeout=...). Solver limits are native (`kissat --time=`, `cadical -t`);
a timeout/limit/interruption is UNKNOWN. A restricted-model UNSAT is about that model only. No "first"/"new"
wording; a literature miss is not novelty. Resources: <=4 busy CPU processes, <=8 GiB total RSS, <=10 GiB new
data, shared free-disk floor 12,000,000,000 bytes, compute chunks <=3 h, checkpoints <=30 min.

## 1. Frozen plan

### 1.1 Object and event count
* CFR(r,n): r rows, each a permutation (sequence) of Z_n = {0..n-1}; for every ordered pair of distinct symbols
  (a,b) and every m in 1..n-1, at most one row has pos(b)-pos(a) = m (mod n), positions read circularly.
* Exact event count r*n*(n-1) (computed generically by the checkers): CFR(4,33) 4224; CFR(5,33) 5280;
  CFR(5,25) 3000; CFR(5,27) 3510; CFR(6,21) 2520. All events must be pairwise distinct.

### 1.2 Equivalences used (written proofs to go in `notes/facts-v1.md`; [P] = proof written, checked by code too)
* E1 (normal form). With position maps p_i (p_i(s) = column of symbol s in row i): CFR iff every p_i - p_j
  (i != j) is a bijection of Z_n. Symbol relabelling (p_i -> p_i o s) and independent row rotations
  (p_i -> p_i + c_i) preserve this, so WLOG f_0 = id and f_i(0) = 0; then CFR iff each f_i and each f_i - f_j
  is a bijection.
* E2 (difference matrices). CFR(r,n) exists iff a (Z_n, r+1; 1) difference matrix exists (rows 0, f_0..f_{r-1};
  conversely subtract row 0 and re-index columns by row 1). Consequently the DM / orthomorphism-graph
  literature (MOLS based on Z_n) is prior art for CFR, beyond the Florentine/Tuscan literature screened so far.
* E3 (fixed-set bound for multiplier models). If every f_i commutes with x -> kx for all k in a subgroup K of
  Z_n^*, every f_i preserves Fix(K') for each K' <= K, and the restrictions form a CFR on the cyclic group
  Fix(K'); so r <= F_c(|Fix(K')|). At n = 33 any K containing an element of order 5 (Fix = 11Z_33, order 3)
  or the element 10 (Fix order 3) allows at most 2 rows; usable multiplier subgroups at n = 33, r = 4 are only
  {1}, <-1>, <23>.

### 1.3 Prior-art lead found DURING source pinning (before any computation)
* Pinned `sources/web/sage-designs-database.py` (SageMath develop, sha256 55a30e8a…23a9) contains
  `DM_33_6_1()`: "Return a (33,6,1)-difference matrix. As explained in the Handbook III.3.56", over
  `AdditiveCyclic(33)` (= Z_33; every group of order 33 is cyclic). If valid, E2 gives CFR(5,33) and hence
  CFR(4,33): the target would be STALE (implied by published prior art), not open.
* First computation therefore = verification of this lead: re-implement the Sage expansion from the pinned
  literal data (no Sage), check the DM property with a dedicated checker, convert by E2 to a strict raw
  CFR(5,33) and to CFR(4,33) (first 4 rows), run both CFR checkers and mutation controls, and notify the parent
  immediately. This object is prior art and is never presented as a lane result.
* Provenance dating of the Sage entry (older pinned Sage release) and the Handbook citation are recorded as
  [SOURCE CLAIM] unless the Handbook text itself is read.

### 1.4 Checkers (written before use; no solver/source assumptions inside witness validation)
* Strict raw format `cfr-raw-v1`: ASCII, exactly r lines, each line n tokens separated by single spaces, tokens
  match ^(0|[1-9][0-9]*)$, every line ends with LF, no other bytes. r, n are command-line expectations.
* `code/cfr_check_events.py` (checker A): every row a permutation of 0..n-1; enumerate all r*n*(n-1) direct
  events (R[i], R[(i+m) mod n], m) and require pairwise distinct (first duplicate reported).
* `code/cfr_check_posdiff.py` (checker B, separately written parser): position maps, every pairwise
  difference p_i - p_j must be a permutation of Z_n.
* `code/dm_check.py`: (Z_n, k; 1) difference-matrix checker (all pairwise row differences are permutations).
* Intended-reason controls (`controls/`): Kirtchakov CFR(5,25) (pinned, sha256 9e2d9b33…779ffdcc) accepted by
  both; mutations (swap two symbols in a row, duplicated symbol, a row replaced by a rotation of another row,
  wrong row count, non-canonical token, trailing space, CRLF) rejected for the stated reason by both.

### 1.5 Search plan (held for alternates until the parent decides; target search is moot if 1.3 verifies)
* Primary restricted model (odd position maps, K = <-1>): n = 2m+1, f_i(-a) = -f_i(a), so f_i is a signed
  permutation of 1..m; one-hot X[i,a,v] (i = 1..r-1, a = 1..m, v != 0), bijectivity per absolute value,
  f_i - id via X directly, pairs i<j via one-hot auxiliaries D[i,j,a,w] (w != 0) with table clauses
  X[i,a,u] & X[j,a,v] -> D[i,j,a,u-v] (u = v forbidden), exactly-one per (i,j,a) and per (i,j,|w|).
  Search-only restriction; no symmetry breaking in the base CNF (variant: f_1(1) < f_2(1) < ... labelled).
* Controls before any alternate run: planted Kirtchakov CFR(5,25) satisfies the odd model (unit clauses ->
  SAT; its K = <7> contains -1); known-dev calibration instances (e.g. CFR(4,27), CFR(3,33), CFR(5,21),
  CFR(4,15)) solved from scratch by the encoder and decoded witnesses pass both checkers.
* Solvers: kissat 4.0.4 (`--time=`, `--seed=`), CaDiCaL 3.0.1 (`-t`, `--seed=`), <=3 h per call, <=4 at once.
  Each run: exclusive JSON record (spec, CNF sha256, command, host start/end, exit code, SAT/UNSAT/UNKNOWN).
  UNSAT counts as restricted-model exhaustion only with a DRAT proof checked by drat-trim (copied/built inside
  this lane), otherwise UNKNOWN. On failure: change representation before more long calls.
* Stop rules: any valid target witness -> stop all searches, strict raw + SHA, both checkers + mutations, pin
  producer spec/CNF/model/expander, replay, notify parent, start nothing else until cleared. Disk floor hit or
  deadline -> SIGTERM + bounded wait, UNKNOWN.
