# GB staged parent replay v2 — repairs of the gbs1 source audit, frozen pins and native-control plan

Written 2026-10-18T11:36:08-07:00 (host clock). **No kissat or drat-trim process has been started by this desk; no n=8 GB
generation.** v1 (`scripts/gb_staged_v1.py` b36fbb57…8151) is preserved unchanged and is not authorized for native
work (Codex `review/n8-gb-staged-v1-source-codex-v1.note.md` 480ef541…24a6: CONTROL GO-WITH-FIXES BLOCKING, SCIENCE
HOLD). v2 repairs only the six MAJOR findings; generation stays in RAM, no FIFO deletion, no automatic retry, the same
18 inputs, formulas unchanged. Scope: exact-input proof certification; no n8 theorem, transfer or novelty claim.

## Frozen identity (re-review target)

| artifact | sha256 | bytes |
|---|---|---|
| `scripts/gb_staged_v2.py` (runtime) | `89db96359ba1a94c3c6a45f7386a34006178fd38d4653e9fefcd921c62532844` | 165869 |
| `DIFF-gb_staged_v1-to-v2.txt` (51 hunks) | `a54971c1371af2a3447c839b331b7887bb5cb372de5dd793623c3d0118e761d2` | 83228 |
| `scripts/selfcheck_gb_staged_v2.py` (pure checks) | `57fc2f3f1ce6669f2f05de2d8ac65ba3113226a2f6f14434ffebcb572db0599d` | 77800 |
| `SELFCHECK-gbs2-v2.json` — **PASS 78/78** | `1c974162d5f6ca498e84b140f731895fd374b347ed50b0509267435fdca607ec` | 29316 |
| `PINS-gbs2-v2.json` (pin manifest + finding dispositions) | `e8e7bf5125d3ba1419c1443b9dd08259aeabe96df7733da7687a8d34436c77a1` | 25529 |
| `PRE-EXEC-gbs2-controls-v2.json` (the 7 controls) | `eb04650070587186a47c58776786c07d20dcf65034d3aa428f6a9a8bf6238287` | 30859 |

Interpreter `/opt/homebrew/opt/python@3.14/bin/python3.14 -I -B` (realpath sha256 `cbf84109…ca43`). All v2 file names
use the `gbs2-` prefix; v1 artifacts (`gbs1-`, PRE-EXEC-gbs1-controls-v1.json, SELFCHECK-gbs1-v1*.json) are retained.

## Finding dispositions (line numbers in gb_staged_v2.py)

| Codex finding | repair | where | pure checks |
|---|---|---|---|
| F1 negative controls can falsely qualify on native failures | every control preregisters its only allowed (normal exit code, exact status lines, allowed fatal-class diagnostics) outcomes; control_vetoes() independently refuses a non-normal/self exit of either native, any TIMEOUT, an unregistered outcome, an unlisted fatal diagnostic or a capped list; science gains checker_no_timeout and checker_no_fatal_diagnostic (ERROR, MEMOUT, illegal literal, error opening, wrong binary prefix, failed to reallocate) | L245, L1469, L2208, L2300 | D8, E1, E4, D1 |
| F2 reaped PIDs can remain eligible for signaling | procs/reaped/sigterm/rss slots preallocated before any Popen; reaped[name] = True and p.returncode set immediately after wait4 returns the pid, before any allocation; term_live/reap act only on live() children; diagnostics built afterwards by _child_record() | L1718, L1764, L1670 | D9a, D4, D5c |
| F3 FD exception safety incomplete | acquire() registers each os.open/os.pipe result and closes any descriptor whose insertion did not commit; the feeder closes its descriptor in an unconditional nested finally before chunks.clear() and diagnostics | L1642, L1448 | D9b, D9c, D4 |
| F4 signal/cutoff checks do not cover spawn and publication | boundary() re-checks latched signal/scanner/exclusion/survivor, 17:29 cutoff, 17:57 deadline and the launch threshold immediately before each Popen (after the stage setup); SIGINT latched like SIGTERM; a signal latched during evaluation downgrades the verdict; qualification needs receipts/<label>.commit.json written after the receipt is durable (qualified only with no signal at pre-evaluation, after evaluation or at commit); validate_controls requires qualified commits | L1898, L1972, L2033, L2567, L2365, L2697, L1247 | D9d, H4, H5, H6, H1 |
| F5 GB exclusion misses orphaned checkers; completion can bypass the newest exclusion | exclusion_flags adds natives whose cwd/argv lies in a GB desk or GB evidence tree and orphaned lane natives (ppid 1); lane_scan adds natives owned by a GB driver; the Scanner thread latches the first exclusion itself and latched_stop() reports it at every completion break, launch boundary and evaluation (criterion no_exclusion_breach) | L588, L690, L731, L928 | F4, F5, D9g, D6b |
| F6 resource enforcement gaps | other busy + 1 <= 4 enforced in flight (safety stop) and at the drat-trim boundary; the launch threshold 12.2e9 + 10 MiB (not the 12e9 floor) applied immediately before both spawns | L1860, L1911 | D9e, D9f |

## Native-control plan (needs a NEW explicit parent GO bound to v2; nothing here has been run)

Preconditions: Codex/parent source GO for `gb_staged_v2.py` 89db9635…2844; the parent GA driver has
exited (the 11:35 PDT PRE-EXEC fresh check flagged GA pid 64001 + cadical 93310 + drat-trim 93309; the gate waits).

1. Parent GO record under `review/` outside this desk (only these fields are checked; extra fields allowed):

```json
{
 "status": "PARENT_GO",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "script_sha256": "89db96359ba1a94c3c6a45f7386a34006178fd38d4653e9fefcd921c62532844",
 "pre_exec_sha256": "eb04650070587186a47c58776786c07d20dcf65034d3aa428f6a9a8bf6238287",
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

2. Launch (absolute paths; `set -C` makes the console redirect exclusive; nohup keeps SIGHUP away):

```sh
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1
GO=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/<parent-go-file>.json
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v2.py" run "$DESK/PRE-EXEC-gbs2-controls-v2.json" "$GO" \
  > "$DESK/logs/run-gbs2-controls-v2.console.txt" 2>&1 &
```

   Outputs per control: `receipts/gbs2-ctl-<name>.json` + `receipts/gbs2-ctl-<name>.commit.json` (qualification),
   kissat log, filtered drat-trim log, retained FIFO; `logs/driver-<tag>.log`, `runs/run-<tag>.json`. A control whose
   commit is not qualified stops the run. Expected wall ≈ 7 × (gate ≥ 62 s + a few seconds of natives).

3. Preregistered outcomes (every criterion outside must fail/may fail must hold; vetoes are independent):

| control | solver / checker CNF | verdict | allowed drat-trim outcomes (exit/status + allowed fatal-class lines) | must fail | may fail |
|---|---|---|---|---|---|
| `control:unsat` | UNSAT3D / UNSAT3D | `PASS` | 0/['s VERIFIED'] | none | none |
| `control:sat-checker` | UNSAT3D / SAT3 | `AS_PREREGISTERED_NOT_VERIFIED` | 1/['s NOT VERIFIED'] | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified | none |
| `control:short-cnf` | UNSAT3D / UNSAT3D minus final LF | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED'] | checker_feed_measured_complete | none |
| `control:truncate` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] + c ERROR: no conflict | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified, checker_consumed_proof_bytes_equal_fed, checker_no_fatal_diagnostic |
| `control:suffix` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified |
| `control:digest-alter` | UNSAT3D / UNSAT3D | `AS_PREREGISTERED_FAIL_CLOSED` | 0/['s VERIFIED']; 1/['s NOT VERIFIED'] | feeder_plain_complete, proof_fed_equals_collected | checker_self_exit_0, checker_status_exact_verified, checker_no_not_verified |
| `control:early-close` | UNSAT3D / NOHEADER | `AS_PREREGISTERED_FAIL_CLOSED` | 0/no status + c ERROR: did not find p cnf line in input file | feeder_plain_complete, proof_fed_equals_collected, checker_status_exact_verified, checker_no_fatal_diagnostic, checker_header_counts_match, checker_consumed_proof_bytes_equal_fed | none |

   Independent vetoes for every control: kissat or drat-trim not exiting normally by itself (signal, driver SIGTERM),
   any `s TIMEOUT`, an (exit, status) pair outside its list, a fatal-class line not allowed with that outcome, a capped
   status/diagnostic list. Observations as in v1 (`control_observation()`), plus: truncate N ∈ {D, D+1} with one
   count line; early-close exactly one fatal-class line (the header error).

## Science procedure (a separate GO per item; not authorized here)

After seven controls with **qualified commit records** of this script sha256:

```sh
TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v2.py" \
  preexec "$DESK/PRE-EXEC-gbs2-<ID>-a1.json" gb:<ID>:a1
# parent GO: "scope": "science", "items": ["gb:<ID>:a1"], "pre_exec_sha256": <that PRE-EXEC>, script v2
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v2.py" run "$DESK/PRE-EXEC-gbs2-<ID>-a1.json" "$GO" \
  > "$DESK/logs/run-gbs2-<ID>-a1.console.txt" 2>&1 &
```

A science PASS qualifies only through `receipts/gbs2-<ID>-a1.commit.json` with `qualified: true`.

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

- Do not run the selfcheck, a second driver, or any process whose argv contains `gb_staged_v` while a run is
  active: that is an exclusion breach and stops the run (fail closed). A hot lane python (≥ 50 % CPU) now also counts
  toward the in-flight busy cap.
- The unchanged monitor rule's 290 s span holds only while the newest 10 s sample is ≤ ~10 s old; a failing check
  resets the streak and the gate retries after 60 s.
- Pure checks use stub natives and fake lane scans (D8/D9/H4–H6 deliver real SIGTERMs to the selfcheck process);
  they establish plumbing, ownership, evaluator and publication logic, not native behaviour. Native behaviour is
  established only by the seven control receipts and their commit records.
- Nothing is deleted; spent FIFOs, logs, failed attempts and UNKNOWN receipts are retained.
