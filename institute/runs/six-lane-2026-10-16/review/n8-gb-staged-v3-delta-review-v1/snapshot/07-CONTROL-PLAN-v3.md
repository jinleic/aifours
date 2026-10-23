# GB staged parent replay v3 — delta repairs of the gbs2 re-review, frozen pins and native-control plan

Written 2026-10-18T12:06:39-07:00 (host clock). **No kissat or drat-trim process has been started by this desk; no n=8 GB
generation.** v1 (b36fbb57…8151) and v2 (89db9635…2844) are preserved unchanged and are not authorized for native
work. The Codex re-review `review/n8-gb-staged-v2-source-codex-v1.note.md` (f39a65cd…fe16) closed F1, F2, F5 and F6
and left three MAJORs; v3 repairs exactly those. Generation stays in RAM, no FIFO deletion, no automatic retry, the
same 18 inputs, formulas unchanged. Scope: exact-input proof certification; no n8 theorem, transfer or novelty claim.

## Frozen identity (delta re-review target)

| artifact | sha256 | bytes |
|---|---|---|
| `scripts/gb_staged_v3.py` (runtime) | `6f5b3a8adab95d41f609f31c59704592071be91124dbeba622a329ff541a0f14` | 173253 |
| `DIFF-gb_staged_v2-to-v3.txt` (16 hunks) | `d08360528b0857f1da2df56b626cacd5a65ce44e37f3859911279025550f7d0e` | 21856 |
| `scripts/selfcheck_gb_staged_v3b.py` (pure checks) | `1d60cc972e28a4b1310e0cede5d4b992c215e3f3510ba8161d3aadb1630f5510` | 85849 |
| `SELFCHECK-gbs3-v3b.json` — **PASS 85/85** | `bd07a6ceeff65b5b00d6c68c63cd23a217c5641ac2f896900163bb3cfe4fce1a` | 32804 |
| `PINS-gbs3-v3b.json` (pin manifest + dispositions) | `a1d44ca1d9282f51c7fb7be0e57de2ba7460075fa0554cab5786e86c9b38d097` | 31067 |
| `PRE-EXEC-gbs3-controls-v3.json` (the 7 controls) | `b06d797119c0e60d42913c34e7e34850cb2523915df30dabe89783b908252040` | 31527 |

Retained failed/superseded attempts: `selfcheck_gb_staged_v3.py` (415f1d8f…a292) → `SELFCHECK-gbs3-v3.json` FAIL
81/82 (its D9d still hooked the removed `acquire()`; runtime unchanged; v3b moves the hook); `PINS-gbs3-v3.json`
(1ed99e2a…d078; its controls list carried v2 labels; v3b derives it from v3). All v3 names use the `gbs3-` prefix.

## Delta dispositions (line numbers in gb_staged_v3.py)

| re-review finding | repair | where | pure checks |
|---|---|---|---|
| (1) F3: tuple-wrapped os.open lets a descriptor escape before acquire() receives it | acquire_open() keeps the scalar fd returned by os.open() in its own cleanup scope (state preallocated, no wrapper object) and closes it unless its registration committed; acquire_pipe() for pipes; all three single-descriptor sites converted | L1729, L1745, L2064, L2127 | D9h, D9b, G1 (no tuple-wrapped os.open; exact acquisition sites) |
| (2) F4: a signal during commit serialization/publication can leave qualified true | publish_commit(): the commit base is prepared first; SIGTERM/SIGINT are blocked; the decision is taken at one explicit linearization point (latched signal, pending blocked signals, driver single-threaded, eligibility); the decided record is written durably to <label>.commit.json.prepare and published atomically by os.link() to <label>.commit.json; the directory is synced; the mask is restored afterwards so a signal arriving during publication is handled after it and stops the desk; any failure before the link leaves no commit | L506, L517, L524, L528, L533, L2813, L1335 | H5, H7, H8, H10, H11, H1 |
| (3) F4: receipt durability not established | write_json_durable(): exclusive create, full write, fsync + F_FULLFSYNC, close, directory fsync + F_FULLFSYNC, on-disk sha256 == written bytes; used for the receipt before any decision and for the prepared commit; a durability failure makes the commit unqualified (receipt_durable false) and stops the desk; admission requires receipt_durable true | L473, L479, L487, L2796 | H9, H1 |

Linearization: qualification is decided inside `publish_commit()` with SIGTERM/SIGINT blocked (L517–L524); it
requires no latched signal, no pending blocked signal, a single-threaded driver (so no other thread can run the
handler while the mask is set) and eligibility (qualifying verdict, durable receipt, no signal at pre-evaluation or
after evaluation). The decided record becomes visible only by `os.link()` of its fsynced `.prepare` file (L528); the
mask is restored after the directory sync (L533), so a signal during publication is linearized after it and stops
the desk. Admission (`validate_controls`) requires qualified, receipt-durable, no-pending, single-thread commits.

## Native-control plan (needs a NEW explicit parent GO bound to v3; nothing here has been run)

Preconditions: delta source GO for `gb_staged_v3.py` 6f5b3a8a…0f14; the parent GA driver has exited
(the 12:05 PDT fresh check flagged GA pid 64001 + cadical 47634 + drat-trim 47633; the gate waits).

1. Parent GO record under `review/` outside this desk (only these fields are checked):

```json
{
 "status": "PARENT_GO",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "script_sha256": "6f5b3a8adab95d41f609f31c59704592071be91124dbeba622a329ff541a0f14",
 "pre_exec_sha256": "b06d797119c0e60d42913c34e7e34850cb2523915df30dabe89783b908252040",
 "scope": "controls",
 "items": [
  "control:unsat",
  "control:sat-checker",
  "control:short-cnf",
  "control:truncate",
  "control:suffix",
  "control:digest-alter",
  "control:early-close"
 ]
}
```

2. Launch:

```sh
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1
GO=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/<parent-go-file>.json
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v3.py" run "$DESK/PRE-EXEC-gbs3-controls-v3.json" "$GO" \
  > "$DESK/logs/run-gbs3-controls-v3.console.txt" 2>&1 &
```

   Per control: `receipts/gbs3-ctl-<name>.json` (durable), `receipts/gbs3-ctl-<name>.commit.json` (+ its hard-linked
   `.prepare`), kissat log, filtered drat-trim log, retained FIFO; `logs/driver-<tag>.log`, `runs/run-<tag>.json`.
   A control whose commit is not qualified stops the run. Expected wall ≈ 7 × (gate ≥ 62 s + seconds of natives).

3. Preregistered outcomes (unchanged from v2; vetoes independent):

| control | solver / checker CNF | verdict | allowed drat-trim outcomes | must fail | may fail |
|---|---|---|---|---|---|
| `control:unsat` | UNSAT3D / UNSAT3D | `PASS` | 0/['s VERIFIED'] | none | none |
| `control:sat-checker` | UNSAT3D / SAT3 | `AS_PREREGISTERED_NOT_VERIFIED` | 1/['s NOT VERIFIED'] | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified | none |
| `control:short-cnf` | UNSAT3D / UNSAT3D minus final LF | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED'] | checker_feed_measured_complete | none |
| `control:truncate` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] + c ERROR: no conflict | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified, checker_consumed_proof_bytes_equal_fed, checker_no_fatal_diagnostic |
| `control:suffix` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified |
| `control:digest-alter` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified |
| `control:early-close` | UNSAT3D / NOHEADER | `AS_PREREGISTERED_FAIL_CLOSED` | 0/no status + c ERROR: did not find p cnf line in input file | feeder_plain_complete, proof_fed_equals_collected, checker_status_exact_verified, checker_no_fatal_diagnostic, checker_header_counts_match, checker_consumed_proof_bytes_equal_fed | none |

## Science procedure (a separate GO per item; not authorized here)

```sh
TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v3.py" \
  preexec "$DESK/PRE-EXEC-gbs3-<ID>-a1.json" gb:<ID>:a1
# parent GO: "scope": "science", "items": ["gb:<ID>:a1"], "pre_exec_sha256": <that PRE-EXEC>, script v3
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v3.py" run "$DESK/PRE-EXEC-gbs3-<ID>-a1.json" "$GO" \
  > "$DESK/logs/run-gbs3-<ID>-a1.console.txt" 2>&1 &
```

A science PASS qualifies only through `receipts/gbs3-<ID>-a1.commit.json` with `qualified: true`.

| # | item | kind | bytes | GBBINDING sha256 |
|---|---|---|---|---|
| 1 | `gb:P1-B4:a1` | template | 350551013 | `03271e5afc5b…408b` |
| 2 | `gb:P0-B4:a1` | template | 350551012 | `77df8b038dc9…9a9a` |
| 3 | `gb:P0-B5:a1` | template | 350551013 | `dad7a44837d7…9d10` |
| 4 | `gb:P0-B6:a1` | template | 350551010 | `76f4b6634f0d…4abf` |
| 5 | `gb:P1-B6:a1` | template | 350551011 | `10d40a85c310…9cb2` |
| 6 | `gb:P2-C4:a1` | template | 350551010 | `88fa1587fcd1…f977` |
| 7 | `gb:P2-C3:a1` | template | 350551011 | `24d93eb50a0f…2f78` |
| 8 | `gb:P0-B1:a1` | template | 350551018 | `b364c1e6e21a…c9fa` |
| 9 | `gb:P0-B2:a1` | template | 350551016 | `259bc80bbadb…9b9d` |
| 10 | `gb:P0-B3:a1` | template | 350551014 | `ca58afda03a7…dc63` |
| 11 | `gb:P2-C2:a1` | template | 350551014 | `9ecc9df48738…7326` |
| 12 | `gb:P2-C1:a1` | template | 350551016 | `2311bd829bcf…3135` |
| 13 | `gb:P1-B2.M2:a1` | strengthened | 350552781 | `1aa38ae7c04c…a3f8` |
| 14 | `gb:P1-B2.M4:a1` | strengthened | 350552781 | `2544240d14e1…8293` |
| 15 | `gb:P1-B5.M2:a1` | strengthened | 350552778 | `6a423719e4f0…7065` |
| 16 | `gb:P1-B5.M3:a1` | strengthened | 350552778 | `0ae019350469…7c51` |
| 17 | `gb:P1-B3.M2:a1` | strengthened | 350552779 | `47e099afcf7b…8871` |
| 18 | `gb:P1-B1.M2:a1` | strengthened | 350552783 | `1873f550493e…3687` |

## Operational notes and boundaries

- Do not run the selfcheck, a second driver or any process whose argv contains `gb_staged_v` while a run is active
  (exclusion breach, fail closed); hot lane pythons count toward the in-flight busy cap.
- The unchanged monitor rule's 290 s span holds only while the newest sample is ≤ ~10 s old; the gate retries.
- Pure checks use stub natives, fake lane scans and real SIGTERM/SIGINT delivered to the selfcheck process; they do
  not establish native behaviour, which only the seven control receipts and their qualified commits establish.
- Nothing is deleted; spent FIFOs, `.prepare` records, logs, failed attempts and UNKNOWN receipts are retained.
