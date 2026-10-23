# Lane info-2 (sixth target): existence of a symmetric weighing matrix SW(25,16)

Owner: worker `InfoSW25`. Contract (read-only; copied with SHA to `sources/contract-info-2-sw25-16.json`):
`institute/runs/six-lane-2026-10-16/screening/info-2-sw25-16-contract.json`, sha256
09115ab0a8f146d35c32d305e80301c74ce343561482d3e77110097dccf3bdc7 (frozen 13:24:13 PDT). Pre-freeze screen copied as
`sources/info2-killcheck-screen-v1.md` (7a06d9c7…7e). Lane created 2026-10-17 13:31:51 PDT (`notes/lane-opened.txt`).
Deadline 2026-10-18 18:31:43 PDT.

Only this directory is writable. No deletion, no overwrite (files created with mode x; a corrected file gets a new
version name), no /tmp, no commit/push/publication/contact, no model CLI, no paid API, no SIGKILL, no Popen.kill(),
no subprocess.run(timeout=...). A timeout is UNKNOWN. A restricted-model UNSAT is never nonexistence of SW(25,16).
No "first"/"new" wording; a literature miss is not novelty.

## 1. Frozen plan (written 2026-10-17 13:36:21-13:38:35 PDT by host clock, BEFORE any search computation)

### 1.1 Object
* SW(25,16): W in {-1,0,1}^{25x25}, W = W^T, W W^T = 16 I (so every row has exactly 16 nonzeros).
* Alternates (contract order, only after SW(25,16) is decided or its structured models are exhausted/bounded):
  SW(27,16), then SW(29,16), same definition with n = 27, 29.
* Validity-preserving symmetries (notes/facts-v1.md F2): W -> H W H^T for any signed permutation matrix H, and
  W -> -W.

### 1.2 Sources (read-only GET, pinned by `code/fetch_pin.py`: URL, host time, HTTP status, SHA-256 in `*.pin.json`)
* Munemasa page `sources/web/munemasa-wo.htm` (89318a8c…a270) and data files `munemasa-{W-23-16,SW-23-16,W-25-16,
  W-27-16,W-29-16}.magma`; Dinitz page `sources/web/dinitz-page404.html` (211fbc51…4158) and the files it links
  (`dinitz-{weighing2516,W2316symmetric,W2716file,wieghing2916}.txt`). Each W(25|27|29,16) is posted once (the
  Dinitz and Munemasa W(25,16) look identical by eye; equality is checked by code, not assumed).
* drat-trim source copied from lane btd14-28 (`tools/drat-trim/`, upstream commit 2e3b2dc0, drat-trim.c
  d834b649…c2ee); `bin/drat-trim` built with `cc -O2` has sha256 a46c0c71…8e37, byte-identical to earlier lanes.
  Known quirks: positional INPUT must be argv[1] and PROOF argv[2]; output lines start with "\r" (strip before
  matching "s VERIFIED"); with no PROOF argument it reads stdin and needs `-i` for binary proofs; `-D` deletes the
  proof file and is never used. lrat-check is not used.

### 1.3 Written facts (proofs in `notes/facts-v1.md`; [W] = written proof, information unless stated)
* F1 trace W = 8p - 100 in {+-4, +-12, +-20} for n = 25 (diagonal never zero). F2 symmetries. F3 W(n,w) is
  equivalent to a symmetric matrix iff some signed permutation M makes M W symmetric. F4 Fix(G) is
  conjugacy-invariant, so one model per B_n-conjugacy class. F5 odd prime order elements are conjugate to unsigned
  permutations of type r^s 1^f. F6 orbit-matrix identities (E1)-(E5). F7 for SW(25,16): no symmetric automorphism of
  prime order 7, 11, 13, 17, 19, 23; order 5 only with cycle type 5^5; order 3 only with f in {1,4,7,10,13} fixed
  points. F8 Z_5 semiregular forces trace = +-20. F9 involution classes (a,b,c) and the identity (E6).
* F7 is also cross-checked by SAT (batch B4) as an encoder test; no encoding uses F6-F9 unless labelled.

### 1.4 Representation and encodings (one generic encoder for every model)
* Model = subgroup G of B_n given by generators (signed permutations), as a JSON spec from `code/sw_models.py`
  (sha256 recorded per run). Fix(G): W symmetric with W_{pi(i),pi(j)} = s_i s_j W_{ij} for every generator.
  G = 1 is the unrestricted problem.
* `code/sw_cnf.py`: cells = unordered pairs {i,j} (i <= j), so symmetry is built in. Cells are merged into G-orbits
  with a relative sign (union-find with parity); an orbit containing a cell and its own negative is forced to 0.
  Per orbit two variables: A (nonzero) and S (sign, true = -1 on the representative); clause (A or not S) removes
  the free sign of zero orbits. Row-orbit representatives: exactly w nonzeros (totalizer with both directions).
  Row-pair-orbit representatives {i,j}: for each column k, E_k <-> (both nonzero, product +1), D_k <-> (both nonzero,
  product -1) by full Tseitin definitions (shared per orbit pair and relative sign); #E = #D is encoded as two
  totalizers capped at w/2 + 1 with output_t(E) <-> output_t(D) for t = 1..w/2 and output_{w/2+1} false for both
  (sound: #E + #D <= w). Output: DIMACS CNF + map JSON (cell -> orbit variable, parity).
* Labelled variants only: `S1` = trace > 0 (#(+1 on diagonal) > #(-1 on diagonal)); complete by F1 (trace != 0)
  and F2/F4 (-W is in Fix(G)). `Q` = quotient case split (1.6). No other pruning without a written proof first.
* Decoder: map + solver model -> strict witness file (1.7) -> both checkers.

### 1.5 Solvers, certificates, records
* kissat 4.0.4 (search, native `--time=`), CaDiCaL 3.0.1 (`-t`) as second solver. Drivers write an exclusive JSON
  record per run (CNF sha256, command, start/end host time, exit code, verdict SAT/UNSAT/UNKNOWN).
* A model is called EXHAUSTED only with: CNF regenerated from the recorded spec with identical sha256, solver UNSAT
  with a DRAT proof, and `bin/drat-trim CNF PROOF` printing a line equal to "s VERIFIED" after stripping "\r" and
  whitespace. Proofs are written compressed (zstd) when small and kept; when large they are streamed into drat-trim
  and only the receipt is kept (CNF regenerable). Negative controls for the DRAT gate: a satisfiable CNF with an
  empty-clause "proof" and a truncated real proof must not verify.
* Disk guard (parent 13:29): before every write-heavy solve or proof stream, free bytes on the volume must be
  >= 12,000,000,000; a growing stream is stopped (SIGTERM, bounded wait, UNKNOWN) if it falls below.

### 1.6 Models and order (RESTRICTED: a miss or UNSAT is about the model only)
* B0 calibration (n != 25): encoder finds SW(6,5) and SW(10,9) unrestricted; the pinned symmetric W(23,16) fixed by
  unit clauses is SAT, and three mutations of it (sign flip, entry moved within a row, zeroed pair) are UNSAT;
  symmetric automorphisms of the pinned SW(23,16) are computed and one of them is used as a model to re-find an
  SW(23,16) from scratch (positive control of the model machinery).
* B1 posted matrices: for each posted W(25,16), W(27,16), W(29,16) decide "exists signed permutation M with M W
  symmetric" (F3) by `code/equiv_cnf.py` + SAT; UNSAT with DRAT. A SAT answer is a candidate SW(n,16) (checked as
  in 1.7).
* B2 Z_5 semiregular (type 5^5; by F7 the only order-5 class): quotient feasibility first
  (`code/quotients_z5.py`: all integer symmetric 5x5 B with B^2 = 16 I and block-weight matrices compatible with
  (E3)-(E5) and symmetric diagonal circulants, exact count and classes under the normalizer), then the whole-model
  CNF (no split) with DRAT; per-quotient lifts (variant Q) only if the whole model is UNKNOWN at its limit.
* B3 Z_3 with f = 1, 4, 7, 10, 13 fixed points (all order-3 classes by F7): whole-model CNFs, then DRAT.
  Quotient enumeration for f = 1 (9 x 9 orbit matrices) as information.
* B4 F7-excluded classes (orders 5 with f > 0, 7, 11, 13, 17, 19, 23): SAT cross-check of F7 (information).
* B5 involution classes (a,b,c), a >= b, c from 12 downward (most symmetric first), 600 s first pass each, DRAT
  for UNSAT; unresolved classes listed as UNKNOWN with their limits.
* B6 further groups (order 4 classes, Z_2^2, S_3, Z_6, ...) and an unrestricted S1 background search only after a
  README amendment written before they run.
* Alternates SW(27,16), SW(29,16): same pipeline after an amendment with their own F7-type analysis.

### 1.7 Checkers and controls
* Strict witness format: line 1 `SW n w`, then exactly n lines of n entries from {-1,0,1} separated by single
  spaces, LF line ends, final LF, nothing else.
* `code/verify_sw.py` (stdlib, definition-first) and `code/sw_check.c` (independent C, `bin/sw_check`). Both
  compute every category and print the full failing set and the primary reason, the first failing category in the
  order FORMAT, HEADER, ENTRIES, SYMMETRY, WEIGHT, ORTHO (ENTRIES = token not in {-1,0,1}; SYMMETRY = W != W^T;
  WEIGHT = some row weight != w; ORTHO = some off-diagonal entry of W W^T != 0).
* `code/checker_controls.py` -> `controls/checkers-v1/`: positives = the pinned symmetric W(23,16), Paley symmetric
  conference matrices SW(6,5), SW(10,9), SW(14,13), SW(18,17), SW(26,25), Sylvester SW(16,16); negatives with
  intended primary reason: posted W(25,16) as `SW 25 16` (SYMMETRY: valid weighing matrix, not symmetric), SW(26,25)
  presented as `SW 26 16` (WEIGHT), one symmetric off-diagonal pair of SW(23,16) sign-flipped (ORTHO; a symmetric
  matrix cannot fail exactly one row pair, notes/facts-v1.md), one symmetric pair set to 2 (ENTRIES), header and
  format mutations (FORMAT/HEADER). Both checkers must agree on primary reason and failing set for every case.

### 1.8 Stop rules and resources
* On ANY SW(25,16) witness: SIGTERM all lane searches, verify with both checkers, pin under `certs/` with SHA-256,
  run witness controls (mutations, numpy recomputation, producer replay), message Main, end with the report.
* Restricted UNSAT never becomes a nonexistence claim; the final table lists EXHAUSTED (with receipts), UNKNOWN
  (with limits) and untried models.
* At most 4 busy processes (at most 3 concurrent solvers + 1 slot for encoders/checkers), <= 8 GiB RAM, <= 10 GiB new
  data, disk guard 1.5, README log at least every 30 min, compute chunks <= 3 h, native limits or SIGTERM plus
  bounded wait only.

## 2. Status (below the freeze only; host clock PDT; rewritten 13:53)
* WITNESS (candidate, pending parent checks): `certs/sw25-16-witness-v1.sw`, 1459 bytes, sha256
  bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0. Both lane checkers: VALID SW(25,16)
  (`python3 -B code/verify_sw.py FILE --expect 25 16 --sha256 …`, `bin/sw_check FILE 25 16`). numpy recomputation:
  entries in {-1,0,1}, W = W^T, W W^T = 16 I, every row weight 16; trace 20, eigenvalue +4 (x15), -4 (x10).
  [F] exact computation only; nothing is claimed beyond this one matrix. No novelty or priority claim.
* Producer: RESTRICTED model B2 = Z_5 semiregular (`python3 -B code/sw_models.py cyc 25 16 5 0`: g maps point
  5a+u to 5a+((u+1) mod 5)), plain variant (no S1), `code/sw_cnf.py` CNF f48f02bd…53a1 (14820 vars, 83645 clauses),
  map 0eacc4e7…f9a8, spec 93ec6590…a646; kissat 4.0.4 (/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat, 05d6f3e9…a848),
  default options and seed, `--time=3600`, proof streamed to a FIFO (unused for SAT); SAT in 6.06 s
  (13:48:47-13:48:53); decoded by `code/sw_decode.py`. Producer receipt with all hashes and the replay recipe:
  `evidence/producer-receipt-v1.json` (6203bea7…e1b0; canonical model hash fc983c61…2b8c).
* `controls/witness-v1/witness-controls.json` (e9306775…2229): WITNESS-CONTROLS PASS: both checkers VALID; numpy;
  eight intended-reason mutations rejected identically by both checkers (row 0 negated -> SYMMETRY only;
  symmetric sign flip -> ORTHO only; diagonal flip -> ORTHO only; entry 2 -> ENTRIES; zeroed pair -> WEIGHT;
  header -> HEADER; CRLF and missing final LF -> FORMAT); invariance under the model generator; producer replay:
  spec and CNF regenerated byte-identical, kissat rerun with and without the proof stream returns identical
  witness bytes.
* Short form: `certs/sw25-16-witness-v1.circulant-first-rows.txt` (307ba47d…36ba); `code/expand_circulant_array.py
  expand` rebuilds identical bytes (`controls/witness-v1/expanded-from-first-rows.sw`).
* Second, different witness from the S1 variant (CNF 669e8a3a…7b97, SAT in 38.3 s): `certs/sw25-16-witness-v1b.sw`
  (6cbe3651…5b3a), both checkers VALID, `controls/witness-v1b/witness-controls.json` (262ed50d…eaa4) PASS (same
  controls and replay), short form `certs/sw25-16-witness-v1b.circulant-first-rows.txt` (77228388…b152).
* Stop rule executed: both B2 batches stopped at their first SAT (13:48:53, 13:49:26); afterwards only the
  sequential producer replays of the witness controls ran (one kissat at a time, 13:50:56-13:53:02); no lane
  process is running. B3-B6 never run. SW(27,16) and SW(29,16) not started (parent 13:51: not before the SW25
  witness and priority disposition are complete).

### 2.1 Witness structure (explanation only, no claims)
* Rows/columns are numbered 5a+u (orbit a = 0..4, u in Z_5). Block (a,b) is circulant:
  W[5a+u][5b+v] = f_ab[(v-u) mod 5], with first rows f_ab (sign characters, f_ab[x] = W[5a][5b+x]):
  ```
          b=0   b=1   b=2   b=3   b=4
    a=0  +0++0 +-+00 +---0 00-++ 00--+
    a=1  +00+- +0--0 0+0+0 +--00 ---+-
    a=2  +0--- 00+0+ 0+--+ 0++-+ --000
    a=3  0++-0 +00-- 0+-++ +0++0 0++-0
    a=4  0+--0 --+-- -000- 00-++ +-00-
  ```
  Symmetry of W is f_ba[x] = f_ab[-x] (diagonal blocks are symmetric circulants).
* Orbit matrix (block row sums) B = [[3,1,-2,1,-1],[1,-1,2,-1,-3],[-2,2,0,2,-2],[1,-1,2,3,1],[-1,-3,-2,1,-1]],
  B^2 = 16 I, trace B = 4; block row weights [[3,3,4,3,3],[3,3,2,3,5],[4,2,4,4,2],[3,3,4,3,3],[3,5,2,3,3]];
  orbit diagonal values (1,1,0,1,1), so trace W = 20, as F6/F8 predict.

## 3. Log (host clock, PDT)
- 13:24:35 contract read (sha256 matches 09115ab0…dc7). 13:29 parent disk-guard message (free >= 12e9 bytes before
  write-heavy solves; streaming certification preferred) adopted in README 1.5.
- 13:31:51 lane created (`notes/lane-opened.txt`); sources copied (`notes/copied-sources.sha256.txt`);
  `bin/drat-trim` built (a46c0c71…8e37, identical to earlier lanes).
- 13:32:12-13:36 read-only GETs, pinned (`sources/web/*.pin.json`): Munemasa page + 5 data files, Dinitz page + 4
  linked files. The Dinitz page's "W(23,16)" link points to W2716file.txt (a page quirk; recorded, not used).
- 13:36:21-13:38:35 README section 1 and `notes/facts-v1.md` written; 13:38:42 freeze receipt
  (`notes/freeze-receipt.txt`: README cc0f41de…754c, facts 21ea4089…83aa).
- 13:39-13:41 checkers `code/verify_sw.py` (79af81eb…) and `code/sw_check.c` (c6e51f54…) -> `bin/sw_check`
  (f34de858…, Apple clang 17.0.0, cc -O2 -Wall). 13:41:00 first control run aborted on a parser error before writing
  any file (`controls/checkers-v1/` is an empty directory, kept). 13:41:17 `code/checker_controls.py` ->
  `controls/checkers-v2/`: CHECKER-CONTROLS PASS, 22 cases (7 positives: pinned symmetric W(23,16), Paley SW(6,5),
  SW(10,9), SW(14,13), SW(18,17), SW(26,25), Sylvester SW(16,16); 15 negatives, each with the intended primary
  reason and failing set for both checkers: posted W(25,16) -> SYMMETRY only; conference 26 as weight 16 -> WEIGHT
  only; one symmetric off-diagonal sign flip -> ORTHO only (30 bad pairs); diagonal flip -> ORTHO only; entry 2 ->
  ENTRIES (+WEIGHT, ORTHO); zeroed pair -> WEIGHT (+ORTHO); header -> HEADER; 8 format cases -> FORMAT). Code facts:
  Munemasa and Dinitz SW(23,16) files are the same matrix; Munemasa and Dinitz W(25,16) are the same matrix; it is a
  W(25,16) and not symmetric.
- 13:43:21 DRAT gate controls (`code/drat_gate_controls.py` -> `controls/drat-gate-v1/`): PASS. PHP(7,6) UNSAT
  by kissat and CaDiCaL with streamed zstd proofs, both "s VERIFIED"; empty-clause proof on a SAT CNF, a truncated
  proof, and a proof against a different SAT CNF all "s NOT VERIFIED".
- 13:46:21 B0 encoder calibration (`runs/calib-v1/`, `code/sw_models.py` + `code/sw_cnf.py` + kissat): trivial
  SW(6,5) and SW(10,9) SAT, Z_5-invariant SW(6,5) (cycle type 5^1 1^1) and Z_13-invariant SW(14,13) SAT, all decoded
  VALID by both checkers; pinned SW(23,16) fixed by units SAT and decoded to the identical bytes (e36a0144…);
  four mutations fixed by units (sign flip, zeroed pair, diagonal flip, entry moved within a row) UNSAT with DRAT
  VERIFIED.
- 13:47:21 `code/symaut.py`: the pinned SW(23,16) has symmetric automorphism group {I, -I} (order 2, complete:
  final UNSAT). DEVIATION from 1.6 B0: "re-find SW(23,16) from one of its automorphisms" is impossible; the Z_5 and
  Z_13 Paley controls above are the positive controls of the model machinery. Information: the one posted SW(23,16)
  lies in no nontrivial symmetric-automorphism model.
- 13:47:46-13:48:19 B1 (`runs/equiv-v1/`, `code/equiv_cnf.py`, F3, E0 = sign of row 0): positive control
  scrambled SW(23,16) (random signed P W Q, seed 20261017) SAT in 3 s and decoded to a VALID SW(23,16). Posted
  W(25,16) (CNF 531bd7bf…, proof 288cdf5f…), W(27,16) (dc225d6d…, f7abdc24…), W(29,16) (9dede001…, fd275fc9…): each
  UNSAT in about 4 s, DRAT "s VERIFIED". So none of the three posted matrices is equivalent (signed row and column
  permutations) to a symmetric matrix.
- 13:48:47 B2 started: Z_5 semiregular whole model plain (`runs/b2-z5-plain-v1/`, 14820 vars, 83645 clauses,
  f48f02bd…) and S1 (`runs/b2-z5-s1-v1/`, 669e8a3a…), kissat --time=3600 with streamed proofs (2 solver processes).
- 13:48:47-13:48:53 B2 plain: kissat SAT in 6.06 s; decoded `runs/b2-z5-plain-v1/z5-plain.sw`, both checkers VALID
  SW(25,16); the batch stopped at this first SAT. 13:48:47-13:49:26 B2 S1: kissat SAT in 38.3 s, decoded
  `runs/b2-z5-s1-v1/z5-s1.sw` (a different matrix), both checkers VALID; batch stopped.
- CORRECTION (13:53) to the 13:49 status line ("B2 ... started. No SW(25,16) witness"), written at 13:49:25 without
  reading the run output: the plain run had already returned SAT at 13:48:53. Section 2 was rewritten at 13:53 (its
  heading first said "13:55", typed before reading the clock; corrected at 13:54).
- 13:49:38 output read; process list: no lane process (the kissat/cadical processes listed belong to other lanes and
  were not touched). 13:50:02 both witnesses pinned (copied, exclusive) in `certs/`; both checkers VALID with
  `--sha256`; numpy recheck (ternary, symmetric, W W^T = 16 I, weights 16). 13:50 Main messaged with path and SHA.
- 13:50:56-13:51:09 `code/witness_controls.py` on witness v1: WITNESS-CONTROLS PASS (`controls/witness-v1/`).
- 13:51 parent message: remaining controls and replays sequential, <= 1 busy CPU; no SW27/29 before the SW25
  witness and priority disposition are complete; preserve seed/expander, CNF/map, kissat command/version/seed and
  model hashes. Followed: everything after this point ran one process at a time.
- 13:51:42-13:53:02 witness controls on v1b: PASS (`controls/witness-v1b/`). 13:51-13:53
  `code/expand_circulant_array.py` short forms for v1 and v1b, both re-expand to identical bytes.
- 13:53:06 `code/producer_receipt.py` -> `evidence/producer-receipt-v1.json` (kissat binary sha256, recorded command,
  default seed, CNF/map/spec/decoder hashes, canonical model hash, replay recipe).
- 13:54:07 integrity: README bytes before "\n## 2. Status" hash to cc0f41de…754c (the freeze receipt), and
  `notes/facts-v1.md` still hashes to 21ea4089…83aa; section 1 and the facts are unchanged since the freeze.
- 13:54:31 lane data 159 MB (mostly kept SAT-run proof streams: z5-s1 45 MB, z5-plain 5.9 MB, replays); volume free
  about 23.6 GB (> 12e9 floor). Only processes naming this lane are the parent's read-only Codex verifier (not
  touched).

## 4. Deviations and rule notes (host clock; appended 13:54:44, heading time corrected from a typed-ahead "13:55")
1. B0: re-finding SW(23,16) from one of its symmetric automorphisms was impossible (group {I,-I}); replaced by the
   Z_5 (n=6) and Z_13 (n=14) Paley model controls (log 13:47:21).
2. B2 order: the frozen plan said "quotient feasibility first" (`code/quotients_z5.py`) and then the whole-model
   CNF. The whole-model CNFs were run first and returned the witness in 6 s; `code/quotients_z5.py` was never
   written and no quotient enumeration was run. The witness's quotient data (2.1) were computed afterwards, as
   explanation only.
3. The 13:49 status line was wrong when written (log CORRECTION 13:53); a typed-ahead "13:55" heading was corrected.
4. `controls/checkers-v1/` is an empty directory from an aborted run (kept, not used).
5. Concurrency: at most two kissat processes at once (13:48:47-13:49:26), each with a zstd proof compressor reading
   its FIFO and a driver blocked in a 1 s poll loop; from 13:51 everything ran one process at a time (parent
   request). FIFO nodes `*.fifo` are left in place (never deleted).
6. The two SAT runs wrote DRAT streams that are useless for SAT answers (`runs/b2-z5-*/z5-*-kissat.drat.zst`); they
   are kept, not deleted.
7. No network access other than the logged read-only GETs; no /tmp, no model CLI, no commit, no deletion, no SIGKILL,
   no Popen.kill(), no subprocess.run(timeout=...). `evidence/MANIFEST.sha256` lists every lane file (written last).
