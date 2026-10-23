# GB staged parent replay v1 — frozen source, pins and native-control plan

Written 2026-10-18T10:53:20-07:00 (host clock), before any native process. This desk has started **no kissat or drat-trim process** and
has run **no n=8 GB generation**; the only GB encode executed was the binder's own n=5 storage control inside the pure
selfcheck. Scope: exact-input proof certification of the 18 GB inputs of `review/gb-parent-replay-brief-v1.md`
(d95f3a0b…27ed); no n8 theorem, transfer or novelty claim.

## Frozen identity

| artifact | sha256 | bytes |
|---|---|---|
| `scripts/gb_staged_v1.py` (runtime, review target) | `b36fbb57f279d1b622c1b1b111ad36a542e0ac85c7b9edce92e4c6c7733f8151` | 148063 |
| `scripts/selfcheck_gb_staged_v1b.py` (pure checks) | `9fed6cbd9f9d15527cf67e2f1f89a5ac126165059de31b409606c1797babec5b` | 61424 |
| `SELFCHECK-gbs1-v1b.json` — **PASS 67/67** | `130414bd49363abb4978944c9fd517297eaef3b22699be948d90fc57a78a3efb` | 24885 |
| `DIFF-replay_v5d-to-gb_staged_v1.txt` (vs reviewed GA runtime ee52004b…339e) | `f74aaa3af028dc3b31b90511d40cedceea604d19e49c8f11e73e09b1e5693045` | 248176 |
| `PINS-gbs1-v1.json` (pin manifest) | `573f93bab5d957b2efd73dff277620624ddc60bcbbaaf32781e38e30896d44fe` | 18262 |
| `PRE-EXEC-gbs1-controls-v1.json` (the 7 controls) | `3a09d5bd43467b60d96d3e72cc0b5170da5dcf6a4bdf41bee1fab54d77a3addb` | 27477 |

Interpreter: `/opt/homebrew/opt/python@3.14/bin/python3.14 -I -B` → realpath
`…/python@3.14/3.14.3_1/…/bin/python3.14`, sha256 `cbf84109…ca43` (the binder's interpreter). Retained failed attempt:
`scripts/selfcheck_gb_staged_v1.py` (2bc70196…e709) → `SELFCHECK-gbs1-v1.json` (060e4e9d…ac33) FAIL 62/67, five
selfcheck expectation errors (a never-started thread is correctly reported unfinished; two proof criteria are
definitionally coupled). The runtime was not changed; v1b corrects only those expectations. `devcheck-kernel-1/` holds
pre-freeze stub smokes (development only).

## Runtime in one paragraph

Bytes: the pinned binder `bind_gb_v2.py` (188c88de…5f51) is executed from its verified bytes into a fresh module; its
unchanged `check_inputs()`, `load_gb()` and 16 MiB `make_sink_class()` regenerate the GB base in RAM; units/tail come
from that encode's own `F.tab` with the binder's `compose()` expressions (selfcheck A6: equal to the binder's own
`compose()` for all 18 ids). Before any launch header, variables, clauses, bytes, sha256 and every piece must equal the
GBBINDING record (d917203d…c673) and its PRE-EXEC copy; after admission the CNF parts, script, interpreter, both
binaries, GBBINDING, binder, PRE-EXEC, GO record and (gb) the 7 control receipts are re-hashed immediately before each
spawn. Stage 1: kissat 4.0.4 alone (`--time=3600 /dev/fd/N fifo/<label>.kissat.fifo`), measured CNF writer, RAM
collector with sha256/count/actual EOF, keepalive closed at the reap. Stage 2 only after kissat's self-exit 20, exact
`s UNSATISFIABLE`, clean collector EOF with R > 0, complete solver feed and finished stage-1 threads: an independent
buffer digest, then the parent drat-trim alone (`/dev/fd/N -i -t 7200`) with a second measured CNF feed, the RAM proof
fed on stdin (chunks released as written) and stdout+stderr through a filter that hashes the full raw stream and drops
only exact `\rc WARNING: detected and deleted duplicate literal %i at position %i of proof line %i\n` lines (counted
per phase). No CNF/proof regular file; FIFOs never unlinked; each tool has its own TMPDIR/cwd under `tmp/<label>/`.
Reused verbatim from replay_v5d.py: `_stop_helper`, `run_helper`, `Scanner`, `gate_scan`, `monitor_stability`,
`latched_stop`, `Fds`, `taskinfo` (selfcheck G3). PASS = all 26 criteria of `CRITERIA` (the brief's conjunction:
bound identity and pre-spawn re-hash, both measured feeds, kissat self-exit 20 + singleton `s UNSATISFIABLE`,
drat-trim self-exit 0 + singleton `s VERIFIED` (CR removed only), no NOT VERIFIED/TIMEOUT/early EOF/less-than-expected,
exactly one parse line with the bound counts, R > 0 == buffer == D with equal digests, exactly one consumed-count line
N == D, clean filter, no stop/exception/skipped stage/grace overrun, no latched signal, clean stopped scanner, 5 threads
finished, no fd left or close error, both children reaped, no helper survivor). Anything else is UNKNOWN.

Admission: parent GO record (below) **and** the gate: lane busy + 1 ≤ 4; other lane RSS + max(measured driver, 6 GiB
gb reservation | 512 MiB control) ≤ 11 GiB; free ≥ 12.2e9 + 10 MiB; **no exclusion** (any parent GA replay native or
replay/launch driver, any other kissat, any other GB driver — the GA driver must have exited); two passes 60 s apart;
gb items also the unchanged monitor rule (amendment 0bbf4fdf…ce87; event records ignored, nothing reconstructed). In
flight (every 0.25 s): pipeline cap 6 GiB (controls 1 GiB) counting the driver's CNF parts and RAM proof, lane 11 GiB,
floor 12e9, latched exclusion breach, scanner failure/staleness, stage backstops 3720/7320 s, 17:57 PDT; no spawn at or
after 17:29 PDT; SIGTERM-only, bounded 120 s, never escalated.

## Native-control plan (needs the explicit parent GO; nothing here has been run)

Preconditions: Codex/parent source GO for `gb_staged_v1.py` b36fbb57…8151; the parent GA driver has exited (the
10:50 PDT PRE-EXEC fresh check flagged GA pid 64001 + cadical 94621 + drat-trim 94620; the gate waits while any GA
replay process is in the lane).

1. Parent writes a GO record under `review/` **outside this desk** (any name, e.g.
   `review/moqls8-gb-staged-v1-controls-parent-go-v1.json`). Only these fields are checked; extra fields are allowed:

```json
{
 "status": "PARENT_GO",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "script_sha256": "b36fbb57f279d1b622c1b1b111ad36a542e0ac85c7b9edce92e4c6c7733f8151",
 "pre_exec_sha256": "3a09d5bd43467b60d96d3e72cc0b5170da5dcf6a4bdf41bee1fab54d77a3addb",
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

2. Launch (absolute paths: the driver changes to `tmp/` before resolving arguments; `set -C` makes the console
   redirect exclusive):

```sh
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1
GO=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/<parent-go-file>.json
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v1.py" run "$DESK/PRE-EXEC-gbs1-controls-v1.json" "$GO" \
  > "$DESK/logs/run-gbs1-controls-v1.console.txt" 2>&1 &
```

   Expected wall ≈ 7 × (gate ≥ 62 s + a few seconds of natives). Outputs: `receipts/gbs1-ctl-<name>.json`,
   `logs/gbs1-ctl-<name>.kissat.log`, `logs/gbs1-ctl-<name>.drat.filtered.log`, `fifo/gbs1-ctl-<name>.kissat.fifo`
   (retained), `logs/driver-<tag>.log`, `runs/run-<tag>.json`. A control whose verdict differs from its
   preregistration stops the run.

3. Preregistered outcomes (UNSAT3D = the 3-variable all-sign UNSAT formula + clause `1 1 2 0`; every criterion not
   listed as must_fail/may_fail must hold, plus the control's observation in `control_observation()`):

| control | solver / checker CNF | verdict | must fail | may fail (recorded as observed) |
|---|---|---|---|---|
| `control:unsat` | UNSAT3D / UNSAT3D | `PASS` | none | none |
| `control:sat-checker` | UNSAT3D / SAT3 | `AS_PREREGISTERED_NOT_VERIFIED` | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified_or_timeout | none |
| `control:short-cnf` | UNSAT3D / UNSAT3D minus final LF | `AS_PREREGISTERED_FAIL_CLOSED` | checker_feed_measured_complete | none |
| `control:truncate` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified_or_timeout, checker_consumed_proof_bytes_equal_fed |
| `control:suffix` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified_or_timeout |
| `control:digest-alter` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified_or_timeout |
| `control:early-close` | UNSAT3D / NOHEADER | `AS_PREREGISTERED_FAIL_CLOSED` | feeder_plain_complete, proof_fed_equals_collected, checker_status_exact_verified, checker_header_counts_match, checker_consumed_proof_bytes_equal_fed | none |

   Observations: `unsat` — full PASS and exactly one formula-phase duplicate-literal line (the filter class matches the
   real drat-trim output); `sat-checker` — D == R, N == D, parse 3/7, drat-trim self-exit 1 with exactly
   `['s NOT VERIFIED']`; `short-cnf` — checker feed written == bound − 1 (exact prefix sha256) while drat-trim
   self-exits 0 with exactly `['s VERIFIED']` and N == D: **a native VERIFIED cannot substitute for incomplete
   delivery**; `truncate` — D == R − 2, no delivery error, digests differ; `suffix` — D == R + 5 and N == D (consumed
   suffix), digests differ; `digest-alter` — D == R and N == D but the transported digest differs (first one-byte
   literal of the first `a` line negated in transit); `early-close` — header-less CNF fully delivered, exact
   `c ERROR: did not find p cnf line in input file`, drat-trim self-exit 0 with no status or count, the held feeder
   write gets EPIPE with 0 bytes fed, every thread/fd/child settled. Preregistration basis: pinned drat-trim.c
   (L1065, L1107–1115, L1160–1163, L1480–1500) and the v5d native controls; if real drat-trim deviates (e.g.
   `short-cnf` not VERIFIED), the control is INVALID_CONTROL and no science item is admitted.

## Science procedure (each item a separate parent GO; not authorized by this plan)

Only after the seven control receipts of this script sha256 exist with their preregistered verdicts (re-validated at
preexec, run start and every identity check). One item per run, new attempt tag per attempt, no retries:

```sh
TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v1.py" \
  preexec "$DESK/PRE-EXEC-gbs1-<ID>-a1.json" gb:<ID>:a1
# parent GO: same fields with "scope": "science", "items": ["gb:<ID>:a1"], "pre_exec_sha256": <that PRE-EXEC>
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v1.py" run "$DESK/PRE-EXEC-gbs1-<ID>-a1.json" "$GO" \
  > "$DESK/logs/run-gbs1-<ID>-a1.console.txt" 2>&1 &
```

Each run regenerates the input in RAM (~10–15 s, peak ≈ 0.45 GB before natives), demands the bound identity, gates
with the monitor rule and runs the two stages. Worker r6 timing references only (not evidence): staged P0-B1 kissat
342 s, drat-trim 357 s, proof 0.77 GB, aggregate peak 4.91 GB; direct items 3–12 min each.

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

- Do not run the selfcheck or a second driver while a run is active: another `gb_staged_v*` driver is an exclusion
  breach and stops the run (fail closed).
- The unchanged monitor rule's 290 s span holds only while the last 10 s sample is ≤ ~10 s old; a failing check
  resets the streak and the gate retries after 60 s.
- The pure checks run stub natives; they establish plumbing, ownership and evaluator behaviour, not native behaviour.
  Real native behaviour is established only by the seven control receipts.
- Nothing is deleted; spent FIFOs, logs, failed attempts and UNKNOWN receipts are retained.
