# P-STREAM design v1 — PA19 info-1 lane (no proof on disk)

Author: ContinuePA19b. Written 2026-10-19T05:25:46-0700 at the parent's request (04:5x): design and code only. Nothing
was run: no native solver/checker, no test, no probe. The worker CPU HOLD is in force while run-012 is
active. These files are frozen for the parent's Codex review before any qualification run. They make no
scientific claim, and none of the planning numbers below is a result.

## 1. Frozen files

| file | SHA-256 | bytes |
|---|---|---|
| `code/pilot_stream_drat_ms06_v1.py` (base `pilot_file_drat_v26.py` d31f1a8e…) | `e66cbc5d5c05cd4f7e0e6256c8ccb6098e6db584f186c47bf814a50fa472333c` | 90844 |
| `code/pilot_stream_drat_ms09_v1.py` (base `pilot_file_drat_v27.py` d9a1d5b3…) | `d3ccc3cfa01720d6837ede729f0ef8ea0bea9a5abf2e92afacae1eecd912187f` | 91189 |
| `code/test_pilot_stream_v1.py` (offline mutation tests; NOT run) | `53e5fe573c4938d2a55881ca5eb7dc39a7f5ccec1c9fe654cb9bb75374b3cb8e` | 24545 |
| `review/pilot-runner-v26-to-pstream-ms06-v1.diff` (exact delta) | `6ec7a9422b16be306ccb2d00a2e9adc19075dc36b146fbfaa5f61f0abb9678e5` | 64830 |
| `review/pilot-runner-v27-to-pstream-ms09-v1.diff` (exact delta) | `096711c2a1ed4bfb69450bfd5da348f91bdcc093e17f23efcfebfa1ae2bb7630` | 65353 |
| `review/pilot-pstream-ms06-v1-to-ms09-v1.diff` (the variants differ only where v26/v27 do) | `661325b678d31dc13b087a9cc228000676d02476878ead6d949f0b1ee7c035f1` | 4052 |

Both runners have `ITEMS = []`, so the v26/v27 template items (already-closed cases) can never execute.
A qualification GO is controls-only. Production needs a later item-only delta, with ITEMS taken from the
current frontier (v8, 841d207a…), a preflight, and its own GO.

## 2. Transport (S1–S3)

```
kissat -q -f --seed=1 --time=300 CNF FIFO ──► ProofBuffer collector thread (RAM, HARD cap PROOF_CAP=629,145,600)
   bytes + SHA-256 measured on arrival; over the cap: stop retaining, drain, trip proof_cap (non-latching, as in v26)
   after the reap: blocks frozen (tuple of exact 1 MiB blocks + tail), independent re-hash == collector measurement
        │ (same immutable blocks, no copy)
        ├─► Feeder A ─► stdin of [LANE/code/vendor/drat-trim, CNF, -i, -t 600]          (checker A, 111b0405…)
        └─► Feeder B ─► stdin of [moqls7-parent-proofcheck-v1/drat-trim, CNF, -i, -t 600] (checker B, a46c0c71…)
             sequential, one native child at a time (CPU busy <= 2: runner + one child)
checker stdout+stderr ─► capture filter (raw bytes + SHA-256; drop ONLY exact duplicate-literal lines; keep the rest, LOG_CAP)
```

- **Producer side.** This is v26's FIFO sink with the file replaced by RAM. FIFO handling is unchanged:
  owned path, inode re-check, runner unblock of a never-connected reader, bounded join, latch on error.
  `sink_complete` now also requires `buffer_rehash == [sha256_of_retained, retained]`.
- **Checker argv.** Only the CNF path is positional, so drat-trim reads the proof from stdin
  (drat-trim.c:1371, and it prints `c reading proof from stdin` at :1463). Binary auto-detection runs only
  for a proof *path* (:1435–1456), so `-i` (:1411) is mandatory. The CNF must be argv[1], because
  drat-trim's fopen uses `argv[1]` (:1425).
- **Feeder.** It writes the frozen blocks in 64 KiB `os.write` slices and hashes/counts exactly the
  accepted bytes. The pipe is non-inheritable and Popen uses `close_fds=True`. The runner closes its read
  end immediately after Popen. The write end is closed exactly once: by the thread, or by `abandon()`
  when the thread never started (refused/never-spawned child). It is joined in `settle()` after the
  reap, and an unsettled, raising or close-failing feeder is a settlement problem (UNSETTLED + latch).
  A feeder exception while the checker is alive trips `feeder_exception`, which latches. A delivery error
  (EPIPE) is not a settlement problem; it is an item defect. Each checker binary is re-hashed against its
  pin when its child is prepared. At run start the provenanced build is bound to its receipt
  (`parent-result.json` 200d307d…: binary_sha256 a46c0c71…, source_sha256 d834b649…) and must not share
  an inode with the lane copy.
- **Filter.** This is the v6e `_filter` model, re-implemented and not imported. Raw bytes and SHA-256 are
  measured in-stream. Only lines that fullmatch
  `\rc WARNING: detected and deleted duplicate literal L at position P of proof line N\n` (drat-trim.c:1162)
  are dropped. They are counted by phase (N <= header clause count, or above) and by bytes. Every other byte
  goes to the retained capped log, which is the checker `.out`. Accounting identity:
  `raw_bytes == kept_bytes + dup_bytes_dropped`. A pending partial line longer than 64 KiB is flushed as
  kept bytes, which bounds memory. The unterminated tail is kept.
- **Read-only census of runs 003–010:**
  - Every ms06 item prints 152 duplicate lines (76 at line <= header clauses, 76 above).
  - Every ms09 item prints 304 (152/152).
  - Controls print 0.
  - The above-header lines are kissat's deletion echoes of the formula clauses that contain duplicates.
  - So proof-phase duplicate lines are **recorded, not gated**. Gating them would reject every item.
  - Retained checker log per item: about 1.3 KB (ms06) and about 2 KB (ms09), against 14–28 KB raw.

## 3. Qualification (S4) and commit

`checker_defects(name, …)` is applied per checker, and every defect string names the checker:
- self-exit rc 0;
- status lines exactly `['s VERIFIED']`;
- the parse header equals the CNF pin header;
- the line `c reading proof from stdin` is present;
- feed mode is `plain`;
- `fed_bytes == proof_bytes_fed == buffer bytes` and `fed_sha256 == buffer SHA-256`;
- the feed started, with no delivery error, exception or close error, and the thread joined;
- `c finished parsing, read N bytes from proof file` with N == fed bytes;
- filter EOF, and the accounting identity holds;
- none of the forbidden patterns appears: v26's nine plus `illegal literal`, `error opening` and
  `failed to reallocate` (v6e F1);
- the child settled with no capture overflow.

`qualify_stream(…)` adds the solver-leg checks (rc 20 self-exit, exactly `['s UNSATISFIABLE']`, settled)
and checks that the buffer is complete and its size is in (0, cap]. It requires that every pinned checker
ran, in the order A then B. It requires the CNF post-hash to equal the pin, and the buffer re-hash after
both checks to equal the collector measurement.

Checker B is skipped once checker A has a defect, a latch or a cancel; the item is UNKNOWN either way.
The terminal gate, `commit_record`, the latch/cancel ordering and `final_code` are unchanged.

## 4. RSS (S5)

`supervise` charges `child RSS + max(runner RSS, retained bytes of unreleased buffers)`. The buffer is
therefore counted in full even if the OS compresses or under-reports the runner's pages. The trip stays
`LANE_RSS_TRIP = 6 GiB`.

A buffer is released after the second feed, on item end, and for every control buffer. Each feeder drops
its block reference once it has joined.

Planning arithmetic (not a result). Measured lane samples from runs 003–010:
- checker peak 755.9 MB at a 478.7 MB proof;
- solver peak 429.5 MB;
- checker RSS at most about 1.8× the proof.

At the cap of 629 MB:
- checker phase: about 1.23 GB (checker) + 0.67 GB (runner + buffer), about 1.9 GB;
- solver phase: about 1.1 GB.

Both are far below 6.44 GB.

## 5. Controls (S6): 14 children, stop at the first failure

| control | children | intended outcome |
|---|---|---|
| C1 positive PHP(6,5) | kissat (RAM buffer), A, B | `qualify_stream == []`; each checker completed `s VERIFIED` rc0 |
| C2 one literal removed | A, B | each checker completed; defect `CNF file digest/bytes != expected` |
| C3 trailing byte in transit (`suffix`) | A, B | each completed `s VERIFIED`, yet defects: feed mode, fed != buffer, consumed != fed, `wrong binary prefix`; fed == buffer + 1 |
| C4 foreign proof on SAT PHP(5,5) | A, B | each completed exactly `s NOT VERIFIED` rc1 |
| C5 RAM cap 4096 on PHP(11,10) | kissat | stop `proof_cap`, retained <= 4096, over_cap, settled, collector joined |
| C6 kissat `--time=1`, no proof | kissat | healthy self-exit, rc not 10/20, no SAT/UNSAT line |
| C7 missing CNF with a RAM buffer | kissat | healthy rc>0 naming absent.cnf; collector joined |
| C7b missing CNF + **held** feed (`hold`) | A, B | healthy rc≠0 naming absent-checker.cnf; feeder EPIPE with 0 bytes fed; hold released by the reap event; feeder joined |

C1–C7 are v26's controls, adapted to both checkers. C7b is new: it is the liveness control for the feeder,
mirroring C7 for the collector.

Not in the per-run set:
- Native alter/truncate transport controls. The runner rejects these by the fed-SHA/bytes comparison
  regardless of what the checker does. The offline tests cover that comparison (see §6), and C3 exercises
  it natively.
- A native checker time-limit control. FX4 was declined earlier. `s TIMEOUT` exits rc 0 (drat-trim.c:905)
  and is rejected by the exact-status and forbidden-pattern checks, which are mutation-tested.

## 6. Mutation tests (offline; written, NOT run)

`code/test_pilot_stream_v1.py` takes `RUNNER RUNNER_SHA256 OUT_DIR`. OUT_DIR must be a new directory
directly under `LANE/evidence/probes`. The test writes a receipt with its PID first and a result last, has
a SIGALRM budget of 280 s, uses the stdlib only, and runs no native binary. It needs a parent WINDOW.

Tests (13):
- the constants and the chunk arithmetic;
- the collector: round trip (exact 1 MiB blocks, independent re-hash, RSS charge, release), cap/drain,
  never-connected unblock, and a replaced FIFO (latch);
- the feeder: plain, suffix (+1 byte), hold → EPIPE with 0 bytes, mid-stream peer close (EPIPE,
  undelivered > 0), and guards (unknown mode, unfrozen list, `abandon()` closes both ends);
- the filter: exact-line drop (two low-phase, one high-phase), near-miss lines kept, the unterminated tail,
  and the accounting identity; the long-line memory bound;
- the qualification matrix: a passing two-checker fixture, plus **58 single-field mutations**. Each must be
  rejected for its intended reason, covering:
  - every solver/buffer/sink field;
  - checker-order and missing-checker cases;
  - rc, stop and status;
  - TIMEOUT rc0;
  - the header and the stdin line;
  - feed mode, fed +1, an altered fed SHA, a truncated feed, a delivery error, an exception, a close
    error, an unsettled or never-started feeder, and a missing feed record;
  - consumed != fed;
  - three filter-accounting cases;
  - all 12 forbidden patterns;
  - settlement and capture;
  - the CNF post-hash and the buffer post-hash.

## 7. Chunk fit (`MAX_CHUNK` 10,800 s; `SETTLE` + `MARGIN` = 180 s)

- Controls worst case: 14 × (60 + 60 + 220 + 30) = **5,180 s**.
- Item worst case: 30 + (300+60+220) + 30 + 2 × (600+60+220+30) = **2,460 s**. v26/D2 was 2,150 s with one checker.

| items | total | verdict |
|---|---|---|
| 0 (qualification) | 5,360 | fits |
| 1 | 7,820 | fits |
| 2 | 10,280 | fits |
| 3 | 12,740 | `REFUSED: chunk-fit` (prestart, exit 70) |

**Why CHECK_SECONDS is 600.** The measured maximum is 0.598 s per proof MB (run-005 b177), which
extrapolates to about 376 s at the 629 MB cap; 600 s gives 1.6× headroom. A timed-out check loses the item
(the proof is not retained), so headroom matters more than in v26.

**Why not 3 items per run.** That would need CHECK <= 276 s with 14 control children, which is below the
extrapolated worst case. Getting 3 items would require shrinking the control set to 12 children (dropping
C7b) **and** setting CHECK to 400 s, with zero chunk margin; this design rejects both.

## 8. Disk

- **Retained per item:** CNF (8.8–9.5 MB) + kissat log + two filtered checker logs + 9 child JSONs +
  item record. That is about 9.1 MB, against v26's CNF + proof (up to 629 MB; measured mean about 170 MB).
- **Reservations:**
  - `ITEM_RESERVE` = CNF_ITEM_MAX + 3 × LOG_CAP + 11 × RECORD_MAX (about 66 MB, against about 676 MB);
  - `CONTROL_RESERVE` = 14 × LOG_CAP + 1 MiB + 44 × RECORD_MAX;
  - kissat child reserve is LOG_CAP + 3 × RECORD_MAX.
- The 10 GiB lane ceiling (D1) is unchanged and is no longer binding for the remaining frontier.

## 9. Exact delta against v26/v27 (see the .diff files)

Unchanged:
- admission, including the stability rule (≥ 280 s, addendum v3);
- the registry/STOP checks;
- pre-allocated ownership, single SIGTERM, quarantine and `settle_all`;
- the terminal gate, commit boundary, `final_code` and exit codes;
- the SAT path (`verify_sat`, candidate latch);
- the encoder, skeleton and GO binding (runner SHA + items).

Changed:
- **Header and scope:** docstring S1–S6.
- **Constants:**
  - `DRAT_PROV`, `DRAT_PROV_RECEIPT`, `DRAT_SOURCE_SHA` and `CHECKERS` added;
  - `ITEMS = []`;
  - `CHECK_SECONDS` 1200 → 600;
  - `ITEM_RECORDS` 8 → 11 and `CONTROL_RECORDS` 26 → 44;
  - `CNF_ITEM_MAX` gets `default=0`;
  - `ITEM_RESERVE` and `CONTROL_RESERVE` no longer contain proof bytes;
  - `CONTROL_CHILDREN` 8 → 14;
  - `ITEM_WORST_SECONDS` covers two checkers;
  - new transport constants `FEED_BLOCK`, `WRITE_SLICE`, `HOLD_SECONDS`, `SUFFIX`, `STDIN_LINE`,
    `DUP_LINE`, `PARSE_LINE`, `PENDING_MAX` and `LIVE_BUFFERS`.
- **Classes:**
  - `ProofSink` → `ProofBuffer` (RAM), plus `buffer_charge()`, `Feeder` and `new_filter()`;
  - `Child`: optional feeder (stdin = pipe read end, read end closed right after Popen, feeder started
    after the reader), filtered `_read` with `_keep`, feeder settlement and records (`stdin_feed`,
    `stdout_filter`), and the proof file removed from the census expectation;
  - `supervise`: the `feeder_exception` trip and the RSS charge;
  - `run_child`: the `feeder` parameter and `abandon()` in `finally`.
- **Functions:**
  - `run_kissat` now returns the buffer;
  - `run_drat` → `run_check`;
  - `sink_complete` uses the buffer fields;
  - `qualify_unsat` → `checker_defects` + `qualify_stream`;
  - `controls()` is rewritten (§5);
  - `run_plan` adds the provenance/receipt/inode check and an item body that loops over the two checkers
    with buffer release;
  - `main` has new launch/summary schema strings, binaries and limits.
- The ms06 and ms09 variants differ only in v26/v27's own lines: docstring, `SKEL`, list read,
  `build_partbatch` and the `inputs` key.

## 10. Open decisions / prerequisites for the parent

1. **P1.** The import evidence (`evidence/probes/binary-process-imports-v1.json`) covers kissat and the
   lane drat-trim copy only. Before qualification, an equivalent `nm -u`/`otool -L` record for the
   provenanced build a46c0c71 should exist. That needs a window or parent action; v1 does not pin it.
2. **P2.** CHECK_SECONDS 600 with 2 items per run (chosen), versus a smaller control set with 3 items and
   no margin (rejected, see §7).
3. **P3.** Proof-phase duplicate lines are recorded, not gated (census in §2).
4. **P4.** A native alter/truncate qualification tier is not implemented in v1. It is covered offline and
   by C3; the parent may require it.
5. **P5.** Sequence: Codex review of these files → a controls-only qualification GO (ITEMS = []) → if the
   qualification and the offline tests are accepted, production item-only deltas on frontier v8 (at most
   2 items per file), then preflight, then GO. The spec-v3 twelve items stay open, re-bound to the
   then-current frontier. No closed-case proof-producing fixture is reused.
6. **P6.** The provenanced build lives in the parent's 2026-10-16 review tree. The runner only reads and
   executes it, with re-pinning at every child.
