# Lane info-2: the shortest (12,3) covering sequence, L(12,3) in {34, 35, 36}

Owner: worker `InfoCyclic100`. Contract (read-only): `institute/runs/six-lane-2026-10-16/screening/info-2-cover12-r3-contract.json`
(recorded 2026-10-17T06:42:21-07:00). Lane opened 2026-10-17 06:48:06 PDT (host clock, `notes/lane-opened.txt`).
Deadline 2026-10-18 18:31:43 PDT. Prior lanes and review files are read-only; files from them are copied, never moved.
No file is deleted or moved. Every program writes only into fresh output paths and refuses to overwrite, and no
program performs automatic cleanup.

Status label: one exact table entry. Chee-Etzion-Ta-Vu (arXiv:2502.08424v2, Table I) list 34-40, the parent has
verified the length-36 CPro1 sequence, so 34 <= L(12,3) <= 36. This is not an asymptotic result. No novelty,
priority or "first" claim is made anywhere in this lane.

## 1. Frozen plan (written 2026-10-17 06:48-06:51 PDT, BEFORE any search in this lane)

### 1.1 Exact object (contract definitions)
* A cyclic binary sequence x_0..x_{L-1} (L >= 1).
* Window j (0 <= j < L) is (x_{j mod L}, ..., x_{(j+11) mod L}). The modulus is the ACTUAL length L, and a window
  wraps repeatedly when L < 12.
* The sequence is (12,3)-covering iff EVERY y in {0,1}^12, including all-zero and all-one, has some window at
  Hamming distance <= 3.
* L(12,3) is the minimum such L. Existence is NOT assumed monotone in L. Chung-Cooper (statement 8 and Section 6)
  exhibit gaps for other parameters.

### 1.2 Sources and the imported lower bound (text layers by `pdftotext -layout`)
* [CETV] Chee, Etzion, Ta, Vu, arXiv:2502.08424v2. Copy of the parent's layout text:
  `sources/parent-screen-chee-etzion-ta-vu-2502.08424v2.layout.txt` (SHA-256 c22fc0e0…04ac); PDF SHA-256 c17e9592…7915
  (parent pin `review/cover12-3-parent-screen-v1/manifest.json`, copied to `sources/parent-screen-manifest.json`).
  * Table I (p.11), row n = 12, R = 3: "34-40b". Footnote: "b - Chung and Cooper [10]".
  * p.11: "the lower bounds are either by computer search for very small n or the known lower bound on the smallest
    size of an (n, R)-covering code."
  * Exact entries used as calibration: L(9,3) = 12, L(10,3) = 16, L(11,3) = 20, L(9,2) = 20, L(10,2) = 38 (all
    marked b).
* [CC] Chung and Cooper, "De Bruijn cycles for covering codes" (Random Structures Algorithms 25 (2004) 421-431),
  author PDF `sources/chung-cooper-debruijn-covering-codes.pdf` (http://www.math.sc.edu/~cooper/debruijn.pdf, dated
  August 4, 2003; SHA-256 ef1e52e7…92a4); text layer `sources/chung-cooper-debruijn-covering-codes.layout.txt`
  (SHA-256 134c9b26…3522). The published version may differ.
  * The definition (p.1-2) is the same object: "the set of n-strings appearing as (s_i, ..., s_{i+n-1}), with indices
    taken modulo M, form a covering code of radius R".
  * Table 1 (p.16), "Best known bounds for M(n, R, 2)", row R = 3, column n = 12: "34-40". Also M(9,3) = 12,
    M(10,3) = 16, M(11,3) = 20, M(9,2) = 20, M(10,2) = 38, M(8,2) = 14, M(8,3) = 6.
  * p.15: "Bounds were achieved using the observations above, the table in [10], as well as software that searched
    the string space randomly (for upper bounds), and one which searched it exhaustively (for lower bounds)."
* Imported bound: L(12,3) >= 34, with exactly these citations (CETV Table I, entry 34-40b, attributed to CC Table 1).
  The CC search itself is not available. The lane plan also re-derives the bound by exhaustive search of every length
  14..33 (Section 1.6); lengths L <= 13 are excluded by counting, since at most L distinct windows each cover
  V(12,3) = 1 + 12 + 66 + 220 = 299 words, and 13 · 299 = 3887 < 4096.

### 1.3 Bit conventions (both implementations)
* A sequence is an L-bit integer s with bit i = x_i.
* A window is a 12-bit integer w with bit t = x_{(j+t) mod L}.
* A target is a 12-bit integer y with bit t = y_t.
* The distance is popcount(y XOR w).

### 1.4 Two independently written exact implementations (no shared code)
Each implementation reports every covering string it finds and a full coverage account. Neither uses a heuristic.

* **Impl B, `code/cs_brute.c`: all strings.**
  * Enumeration: every s in [lo, hi) for a given L. Jobs partition [0, 2^L) into disjoint consecutive ranges.
  * Windows: from the periodic extension e of s (bits 0..L+n-2), w_j = (e >> j) & (2^n - 1).
  * Balls: precomputed BY FLIP ENUMERATION (every subset of at most R positions; no popcount). Stored as chunk tables
    tab[c][w] = bits of the target words 64c..64c+63 that lie in the ball of w.
  * Coverage: for each chunk c, OR tab[c][w_j] over all j. The string is covering iff all chunks are full. Chunks are
    tested in an adaptive order (the failing chunk moves to the front); the order only changes speed, since all chunks
    are tested before acceptance.
  * Account: examined = hi - lo, and the jobs' ranges must sum to 2^L.
* **Impl A, `code/cs_neck.c`: one representative per rotation class (necklaces).**
  * Enumeration: the Fredricksen-Kessler-Maiorana (FKM) recursion. This generates the binary strings that are
    lexicographically minimal among their rotations (lex order of the tuple (x_0, ..., x_{L-1})).
  * The program SELF-CHECKS completeness:
    * every generated string is verified to be lex-minimal among all L rotations;
    * generation order is strictly increasing in lex order, so all strings are distinct;
    * the total count equals the necklace number N(L) = (1/L) Σ_{d|L} φ(d) 2^{L/d};
    * the sum over generated strings of their rotation period equals 2^L.

    Consequently the generated strings are exactly one representative per rotation class, and the classes cover
    all 2^L strings. Covering is invariant under rotation (the multiset of windows is unchanged), so checking one
    representative per class is complete.
  * Windows: rolling update over an index array with explicit modulo L.
  * Coverage: popcount distances. A move-to-front cache of "killer" words is tried first; otherwise all 2^n targets are
    scanned with early exit. A string is accepted only after all 2^n targets are covered.
* No symmetry other than rotation is used anywhere; reversal and complement are not used for pruning. No pruning
  besides complete checks is used, so every exclusion is a complete enumeration with an exact count.
* Agreement checks: on the same L, the covering strings found by B, reduced to their lex-minimal rotations, must equal
  the set found by A, and |B| = Σ over A's representatives of their periods.

### 1.5 Strict witness verifier `code/verify_cs.py` (stdlib; independent of both)
* Format: line 1 `COVERING-SEQUENCE n R L`, line 2 exactly L space-separated tokens 0/1, final newline, nothing else.
* It checks all 2^n targets (including all-zero and all-one) against all L windows built with explicit (j+t) mod L,
  where L is the declared length, which must equal the token count.
* It reports the max nearest distance, the histogram, and the all-zero and all-one distances.

Controls (contract):
* n=1,R=0,L=1 "0" must be rejected (the all-one target is uncovered; the public CPro1 verifier would accept it).
* n=1,R=0,L=2 "0 1" passes.
* The de Bruijn sequence 00010111 at n=3,R=0 passes (cyclic wrap).
* The CPro1 length-36 sequence at (12,3) passes.
* Format and semantic mutations (bad header, wrong L, bad token, missing newline, extra line, all-zero sequence of
  length 36) fail for the intended reason.

### 1.6 Calibration, benchmark, main runs and stop rules
1. Verifier controls (1.5).
2. Search calibration with both implementations; cheap, every L from 1 up to the published value.
   * (9,3): none for L <= 11, some at 12. (10,3): none for L <= 15, some at 16. (11,3): none for L <= 19, some at 20.
     (9,2): none for L <= 19, some at 20.
   * Every found string at the published length must pass `verify_cs.py`.
   * (10,2) up to 38 only if affordable after the main runs.
3. Benchmark at (12,3), L = 28 and 30: measure strings per second for both implementations before any projection.
4. Main run 1: (12,3), L = 34, B and A.
5. If L = 34 has no covering string: L = 35, B and A.
6. If L = 34 and 35 have none: L = 36 with both, as the positive control. The CPro1 sequence's class must be among
   the found strings, and B and A must agree on the full set.
7. Lower-bound re-derivation: (12,3), every L = 14..33, with both.
8. Stop rule: on the FIRST covering string found at any L <= 35, stop all runs, verify it with `verify_cs.py`, pin it
   under `certs/`, and report to Main immediately with its SHA-256.
9. Resources:
   * <= 4 processes, <= 8 GiB, <= 10 GiB new disk;
   * checkpoints <= 30 min, chunks <= 3 h;
   * native time limits only (each C program takes a seconds argument and stops itself with status TIMEOUT); SIGTERM
     only if ever needed, never SIGKILL;
   * thread variables set to 1 (OMP/OPENBLAS/MKL/VECLIB);
   * initial assay <= 2 CPU-hours (B and A together, all lengths). Projected costs at 1e8 strings/s would be:
     L = 34, 1.7e10 strings, about 3 CPU-min for B; L = 35, 3.4e10; L = 36, 6.9e10; lengths 14..33 together,
     1.7e10. These are projections only. If the measured rates in step 3 project beyond the assay, stop and report a
     new bounded plan.
10. Outcomes:
    * a timeout or partial run is UNKNOWN;
    * an exclusion at L requires both B and A to complete with exact accounting and zero covering strings;
    * L(12,3) = 36 requires exclusions at 34 and 35, plus the imported lower bound (and/or the re-derivation of
      14..33), plus the parent-verified 36 witness.

## 2. Status
(Section 2 and later are written after the freeze; Section 1 is unchanged except the 06:51 time-label correction.)

Status at 07:14 PDT: UNTRUSTED until parent review. Not labelled novel or final. The parent is running a third,
independently written exhaustive check (different reduction) and a priority audit.

* **No (12,3)-covering sequence exists for any length L <= 35.**
  * L <= 13 is excluded by counting, without any search. A cyclic sequence of length L has at most L distinct windows,
    and each radius-3 ball holds V(12,3) = 1 + 12 + 66 + 220 = 299 words. So the windows cover at most
    L · 299 <= 13 · 299 = 3887 < 4096 = 2^12 words.
  * As a redundant cross-check, both implementations also enumerated L = 1..13 completely and found 0 covering
    strings.
  * L = 14..35 is excluded by two complete, independently written enumerations. Every length shows 0 covering strings
    and exact accounting:
    * Impl B checks all 2^L strings, in job ranges that partition [0, 2^L).
    * Impl A checks all N(L) necklaces; it self-checks lex-minimality and strict order, and its periods sum to 2^L.

    Per-length accounting is in `evidence/run-manifest-v1.json` (key `accounting`). The compare receipts are
    `runs/lower-v1/n12R3L*/compare.json`, `runs/L34-v1/compare/compare.json` and `runs/L35-v1/compare/compare.json`,
    all all_ok.
* **L = 36.** The CPro1 sequence is a witness: the parent verified it, and so does `verify_cs.py`.
  * Impl B finds exactly 432 covering strings among all 2^36. Impl A finds exactly 12 covering rotation classes, each
    of period 36. The sets agree (12 · 36 = 432). Under rotation, reversal and complement the 12 classes form 5
    orbits. The CPro1 sequence is in class 7.
* **Hence L(12,3) = 36, given the parent-verified length-36 witness.**
  * Every L <= 35 is excluded here: by counting for L <= 13, and by exhaustive search for L = 14..35. The claim
    therefore does NOT depend on the imported lower bound 34 (CETV Table I entry 34-40b; CC Table 1), which it is
    consistent with.
  * Not established: novelty, priority or significance; no claim is made about any of them. The exhaustive search
    that CC p.15 refers to is not available for comparison.
* **Witness files** (strict format `COVERING-SEQUENCE 12 3 36` + 36 bits, one sequence per file; created by
  `code/export_l36.py`):
  * `certs/L36-v1/all-432/`: 432 files, one per covering string s found by Impl B. Token i is x_i = bit i of s.
    `SHA256SUMS` cd07653a34874e73bcd36f5f3ccd7a7c63a4ad723e684f603d6e1b6f4aad8d62.
  * `certs/L36-v1/classes-12/`: Impl A's 12 lex-minimal representatives. `SHA256SUMS`
    3393fb4b0f7ac2d99d621228985e1e607f931848e03605ba2021d6c94b09e579.
  * `certs/L36-v1/index.json` (7fd5b20bde31eb698b1d4b90545be8b19d8681177dcdfefd9b9ac3e1e96d8ca7): per file, the SHA-256,
    class, rotation offset and B job. It also records that the 432 strings are exactly the 36 rotations of each of the
    12 representatives.
  * `certs/L36-v1/verification.json` (13077eae0b9ef5950c19f3e622cff75605de1f4ae8c8c8a8c466229e74bd9303): all 444 files
    are VALID under `verify_cs.py FILE --expect 12 3 36 --sha256 <pin>` (verifier v2, 3cb419f6…fcfe). Each file was
    checked against all 4096 targets, with max nearest distance 3.
  * The CPro1 sequence as given is `certs/L36-v1/all-432/cs-12-3-36-s09d7d8d8a.cs`
    (1dea2c286313cdaa6105956ae24598cdd35afe8e83d87e0a7b8e006cdfb9469b). Its histogram {0:36, 1:432, 2:2076, 3:1552}
    equals the parent baseline.
* **Manifests.**
  * `evidence/run-manifest-v1.json` (b4cd86bdf51501fdf046aa346316dba22d03f7e1eccc74db2240f424dcc7591f) contains:
    * the toolchain, and the SHA-256 of every code, archive, bin and source file;
    * the exact commands;
    * 269 job records (argv, range or necklace count, examined, covering, status, host start/end);
    * 131 per-(n,R,L) accounting groups. all_accounting_ok is true, and every L = 1..35 is excluded by both
      implementations.
  * `evidence/MANIFEST.sha256` holds the SHA-256 of every lane file. It is generated last, and its own hash goes in
    the report to the parent.
* **Not run.** The optional (10,2) up-to-38 calibration (plan 1.6 item 2, "only if affordable") was not run, by
  parent instruction (no new searches).
* **Deviations from the frozen plan** (recorded between 07:14:25 and 07:15:10; neither changes any count or result):
  1. Plan 1.6 item 3 named benchmarks at L = 28 and 30. Only L = 28 was benchmarked before the projection and the
     main runs. The complete L = 30 runs are in `runs/lower-v1/n12R3L30/`.
  2. Plan 1.6 item 6 makes L = 36 conditional on no covering string at 34 and 35. The L = 36 Impl B jobs started at
     06:59:37, after all three L = 35 Impl B jobs had finished with 0 covering strings (06:59:31). That was 14 s before
     the L = 35 Impl A run ended (06:59:51, 0 covering) and before the L = 35 compare, which completed by 06:59:56. Had
     A reported a covering string, the stop rule (item 8) would still have applied.
* **Manifest versions.**
  * `evidence/MANIFEST.sha256` (v1, 07:14:24, 1514 files) predates the edits above to this section.
  * `evidence/MANIFEST-v2.sha256` (07:15:10, 1515 files) predates two corrections: a guessed time label "07:16" in
    the deviations heading was replaced by the host-clock interval, and the wording of the L = 35 compare timing was
    fixed.
  * `evidence/MANIFEST-v3.sha256` is generated after this line. It covers every lane file except itself, including
    v1 and v2.

## 3. Log (host clock, PDT)
- 06:43 contract read; 06:48:06 lane created; CC author PDF fetched (`sources/`); parent screen files copied with
  SHA-256 checked (`sources/parent-screen-*`).
- 06:48-06:51 this frozen section written; no search run before this point. Freeze hash in `notes/freeze-receipt.txt`
  (06:50:46). The first version carried a guessed time "07:10" in the heading and in this line; both were corrected to
  the host-clock time at 06:51 (wording only).
- 06:52:20 verifier controls v1 (`controls/verifier-v1/`): all prefixes matched, but two mutations were rejected for a
  different specific reason than intended (a "bad token" case that changed the token count, and a double space that hit
  the header). The control script was tightened to require the specific reason and re-run as v2 at 06:52:50
  (`controls/verifier-v2/verifier-controls.json`): VERIFIER-CONTROLS PASS, all 21 cases as intended. Positives:
  - n=1,R=0,L=1 "0" rejected (the all-one target is uncovered);
  - "0 1" passes;
  - the de Bruijn 00010111 passes;
  - CC's 111000 at (4,1) passes;
  - "1100" at (10,4), L=4 < n (repeated wrap) passes;
  - CPro1 L=36 passes.
  All 36 single-bit flips of the CPro1 sequence fail coverage (informational).
- 06:53 `code/cs_brute.c` (Impl B) and `code/cs_neck.c` (Impl A) written; cc -O2 (Apple clang 17.0.0).
  `code/compare_runs.py` (run/compare driver: accounting, set agreement, strict verification of found classes).
- 06:54:56-06:55:15 search calibration with both implementations, every L from 1 up to one past the published value
  (`controls/calibration-v1/`, one compare.json per (n,R,L)). Every run COMPLETE with exact accounting and B/A sets
  agreeing. The published exact values are reproduced:
  - L(9,3) = 12 (33 rotation classes);
  - L(10,3) = 16 (26 classes);
  - L(11,3) = 20 (1 class);
  - L(9,2) = 20 (1 class);
  - L(8,2) = 14 (2 classes);
  - L(8,3) = 6 (3 classes).

  Every found class passes `verify_cs.py`. Non-monotonicity observed: (11,3) and (9,2) have no covering string at
  L = 21, and (8,2) none at 15, (8,3) none at 7.
- 06:55:23-06:55:26 benchmark at (12,3), L = 28 (`runs/bench-v1/`):
  - B: 2^28 strings in 2.16 s, 1.24e8 strings/s; 98.0% rejected at the first chunk test.
  - A: 9587580 necklaces (= formula) in 1.06 s, 9.1e6 necklaces/s; sum of periods = 2^28.
  - Both found 0 covering strings.
  - Projection (rate scaled by L/28): L = 34 about 170 s B + 70 s A; L = 35 about 350 + 140 s; L = 36 about
    720 + 280 s; L = 14..33 about 150 + 60 s. Total about 0.55 CPU-h, inside the 2 CPU-h assay.
- 06:55:49-06:56:29 L = 34, Impl B (`runs/L34-v1/B-12-3-34-00{0..3}`): 4 parallel jobs over the 4 quarters of
  [0, 2^34). All COMPLETE: 4 × 4294967296 = 17179869184 = 2^34 strings examined, 0 covering, about 40 s each.
- 06:56:34-06:57:37 L = 34, Impl A (`runs/L34-v1/A-12-3-34`): 505294128 necklaces, equal to the formula N(34); sum of
  periods 17179869184 = 2^34; self-check flags 0; 0 covering; 63.2 s.
  `runs/L34-v1/compare/compare.json`: all_ok, sets agree (both empty). Result: NO (12,3)-covering sequence of length
  34 exists (two complete enumerations). This is not yet parent-reviewed.
- 06:57:4x L = 35 started: Impl B as 3 parallel jobs (thirds of [0, 2^35)), Impl A as the 4th process.
- 06:57:40-06:59:31 L = 35, Impl B (`runs/L35-v1/B-12-3-35-00{0,1,2}`): 3 parallel jobs over the thirds of
  [0, 2^35). All COMPLETE: 34359738368 = 2^35 strings examined, 0 covering.
- 06:57:46-06:59:51 L = 35, Impl A (`runs/L35-v1/A-12-3-35`): 981706832 necklaces (= N(35)); sum of periods 2^35;
  flags 0; 0 covering; 125.0 s. `runs/L35-v1/compare/compare.json`: all_ok. Result: NO (12,3)-covering sequence of
  length 35 exists (two complete enumerations).
- 06:59:37-07:03:26 L = 36, Impl B (`runs/L36-v1/`, 3 jobs): 2^36 strings examined, 432 covering strings.
- 06:59:56-07:04:05 L = 36, Impl A: 1908881900 necklaces (= N(36)); sum of periods 2^36; flags 0; 12 covering
  rotation classes, each of period 36; 249.2 s.
- 07:04:11 `runs/L36-v1/compare/compare.json`: all_ok.
  - Agreement: B's 432 strings reduce to exactly A's 12 classes, and 12 · 36 = 432.
  - All 12 classes pass `verify_cs.py --expect 12 3 36`.
  - `runs/L36-v1/classes-report.json`: the CPro1 sequence's rotation class (r = 0x51b1beb9) is among them. The set is
    closed under reversal and complement and forms 5 orbits under rotation, reversal and complement (orbit sizes in
    rotation classes 2, 2, 2, 2, 4).
- 07:07:24-07:09:14 lower-bound re-derivation (`runs/lower-v1/`), (12,3) every L = 1..33 with both implementations
  via `compare_runs.py run`, using 3 parallel loops: L = 33; L = 32, 31; L = 1..30. Every length is COMPLETE, with
  B examined = 2^L, A necklaces = N(L), periods summing to 2^L, 0 covering strings, and compare all_ok
  (L = 33: 2^33 strings by B in 77.5 s; 260301176 necklaces by A in 32.2 s).
- Parent instruction, received between 07:07:24 and 07:08:44:
  1. finish 14..33, then write a manifest and receipts;
  2. write all 432 L = 36 strings and the 12 representatives in strict format;
  3. state the counting exclusion for L <= 13 and the independence from the imported 34.

  No new searches; do not label the result novel or final.
- 07:08:44 copies of `code/verify_cs.py` (v1, aa209ac5…9507) and `code/verifier_controls.py` (v2, b112ff48…82d2) were
  placed in `archive/code/`. v1 was used by `controls/verifier-v2` and by every compare_runs.py verification up to
  07:04:11.
  - 07:09: `verify_cs.py` v2 (3cb419f6…fcfe) adds only `--sha256 HEX`, a binding of the certificate bytes that is
    checked first.
  - 07:09:37 `controls/verifier-v3`: VERIFIER-CONTROLS PASS, all 31 cases as intended. New cases:
    - header range (n = 0, n = 17, L = 0, R = -1) fails as a format error;
    - a correct SHA pin passes;
    - a wrong pin, a bit flip under the CPro1 pin, and a trailing space under the CPro1 pin all fail as
      "binding: sha256";
    - an uppercase pin is refused with exit 2.

    The controls JSON records the verifier and script SHA-256.
- 07:10:25-07:11:17 `code/export_l36.py` wrote `certs/L36-v1/` (Section 2): 444 strict files, all VALID with SHA
  pins. The B set equals all rotations of A's 12 representatives. The CPro1 sequence is class 7, rotation offset 4.
- 07:13:06 `code/build_manifest.py` wrote `evidence/run-manifest-v1.json`, with all_accounting_ok true.
- 07:14 Section 2 (status) written. `evidence/MANIFEST.sha256` (SHA-256 of every lane file except itself) is
  generated after this line; any later change to the lane requires a new manifest version.
