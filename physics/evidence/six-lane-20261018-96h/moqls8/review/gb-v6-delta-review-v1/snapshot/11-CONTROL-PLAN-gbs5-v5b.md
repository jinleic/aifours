# GB staged parent replay v5: the parent's conservative cutover for the gbs4 delta review, frozen pins and native-control plan

Written 2026-10-18T13:12:44-07:00 (host clock). **No kissat or drat-trim process has been started by this desk, and no n=8 GB
generation has run.** v1–v4 are kept unchanged, and none of them is authorized for native work. v4 is b9f9d562…9cdf.
The Codex delta review `review/n8-gb-staged-v4-delta-codex-v1.note.md` (f1630833…4bc2) left two
MAJORs. v5 implements the parent's cutover for exactly those two and adds no further producer-side completion file.
The previous cancellation semantics are kept: every SIGTERM/SIGINT before the actual terminal exit vetoes. The 18
inputs and 7 controls are unchanged apart from their `gbs5-` labels. Scope is exact-input proof certification only;
this makes no claim about the n8 theorem, transfer or novelty.

## Frozen identity (delta re-review target)

| artifact | sha256 | bytes |
|---|---|---|
| `scripts/gb_staged_v5.py` (runtime) | `a0e59977c3bd2e97ca0a39c33f5af11302e001d5f3ec22c5b4fc0b67f79c353a` | 199473 |
| `DIFF-gb_staged_v4-to-v5.txt` (25 hunks) | `054cf52359d9bf99fc07e3519f685566da1185e21c292002b9439b6507d7ea7e` | 29654 |
| `scripts/selfcheck_gb_staged_v5b.py` (pure checks) | `09560f64e903f2127d58655230f0c197976819d86b68eda8538b37c84589883e` | 108471 |
| `SELFCHECK-gbs5-v5b.json` (**PASS 90/90**) | `595d93171c01b7649e7c1d45b8221fd075ea85da66b6883a84edd4d4c29fd13d` | 37398 |
| `PINS-gbs5-v5.json` (pin manifest and dispositions) | `ff6ab285c920e9a338ae7b041507854f923cf7531cfe115a270ffc56d4b4a09d` | 51657 |
| `PRE-EXEC-gbs5-controls-v5.json` (the 7 controls) | `8fad6b7456889e974537d29e2526d26f00cbf95fad803ed090ca98d50c1b19dc` | 33537 |

Retained failed attempt: `selfcheck_gb_staged_v5.py` (861ae613…9cf5) produced `SELFCHECK-gbs5-v5.json`, FAIL 89/90
(ff96a28b…7d48). The fault was in the selfcheck, not the runtime: H17 kept only the last 160 bytes of the child's
output, which cut off the `REFUSED` marker it then looked for. The child had in fact refused (exit 7, mask unchanged).
v5b keeps 400 bytes; the runtime is unchanged.

## Delta dispositions (line numbers in gb_staged_v5.py)

| delta finding | repair | where | pure checks |
|---|---|---|---|
| (1) MAJOR: the final run summary is admissible before its publication succeeds; a failed veto creation can leave it permanently admissible (reader race, failed-veto fallback) | parent cutover, no new producer completion file: qualification_problems() admits nothing from producer bytes alone; it also requires the EXTERNAL parent end/release attestation review/moqls8-gb-staged-release-gbs5-run-<run_tag>.json (RELEASE_RULE) - a regular parent file directly under review/ outside this desk, exactly schema/status/desk/scope, script_sha256 = this script, pre_exec_sha256 = the receipt's PRE-EXEC, run_tag, run_summary_sha256 = the current summary bytes, receipts {label: receipt sha256}, driver_exit_code the integer 0, owned_children_after_exit [], stop_or_signal_observed null, raw_audit PASS. The parent writes it only after observing the run fully returned with exit status 0, no owned child and no stop or signal, and a raw audit; cmd_run returns a non-zero code for any stop, publication error, run cancellation or latched signal, so the v4 schedule (summary link succeeds, its sync fails, its veto creation fails) exits non-zero and is never released. validate_controls() binds the release sha256 into the science admission identity, re-checked at run time and before each spawn | L476, L766, L772, L800, L859, L1658, L2832, L3230, L3147 | H1 (nothing admitted before the release; all seven after it; exit 0); H2 (release sha256 in the admission identity); H14 concurrent reader after the completion and the run-summary publication and after return; 12 forged/mismatched/misplaced releases refused; H15 summary post-link directory sync EIO + run-veto creation ENOSPC -> non-zero exit; a release recording it is refused; H16 every failure run exits non-zero |
| (2) MAJOR: restoring an already-blocked mask can conceal a signal received during final settlement; the terminal boundary is unspecified | run refuses an inherited mask blocking SIGTERM or SIGINT before any record, log or spawn, without changing the caller's mask (refuse_inherited_mask); latch_signals() latches a still-pending SIGTERM/SIGINT at each settlement (before evaluation, children reaped) and after each publication mask restore; terminal_exit() is the finite terminal boundary after every child was reaped and every record published: flush, block both signals (running any tripped handler), switch both to SIG_DFL, inspect latch, pending set, thread count and saved mask, unblock (a pending signal now terminates the process by that signal, as does any later one) and os._exit(code). Every signal before the actual terminal exit therefore vetoes through a non-zero exit status even if no veto file can be written; no early snapshot, last latch sample or summary link is an acceptance boundary | L686, L2962, L675, L654, L748, L3108, L696, L710, L716, L717, L3260 | H13 inherited blocked SIGTERM and SIGINT refused in-process, mask unchanged, no log; H17 child processes: clean 0, stopped 3, latched 4, SIGTERM after the last sample -> killed by SIGTERM, SIGINT before the exit syscall -> killed by SIGINT, inherited mask refused; H4-H12 (unchanged windows) all exit non-zero (H16) |
| stale commit rule naming a linearization point and the removed publish_commit() | rule text now names the decision in publish_qualification() and the full admission chain | L3147 | — |

## The parent release attestation (RELEASE_RULE, L476)

The runtime only reads this record and never writes it. `qualification_problems` admits a receipt only if the record
exists at the exact path `review/moqls8-gb-staged-release-gbs5-run-<run_tag>.json`, as a regular file (not a symlink)
directly under `review/`. Every field must match:

```json
{
 "schema": "moqls8-gb-staged-parent-release/5",
 "status": "PARENT_RELEASE",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "scope": "controls",
 "script_sha256": "a0e59977c3bd2e97ca0a39c33f5af11302e001d5f3ec22c5b4fc0b67f79c353a",
 "pre_exec_sha256": "8fad6b7456889e974537d29e2526d26f00cbf95fad803ed090ca98d50c1b19dc",
 "run_tag": "<run_tag from the driver log / run summary>",
 "run_summary_sha256": "<sha256 of runs/run-<run_tag>.json as audited>",
 "receipts": {
  "gbs5-ctl-unsat": "<sha256 of receipts/gbs5-ctl-unsat.json as audited>",
  "gbs5-ctl-sat-checker": "<sha256 of receipts/gbs5-ctl-sat-checker.json as audited>",
  "gbs5-ctl-short-cnf": "<sha256 of receipts/gbs5-ctl-short-cnf.json as audited>",
  "gbs5-ctl-truncate": "<sha256 of receipts/gbs5-ctl-truncate.json as audited>",
  "gbs5-ctl-suffix": "<sha256 of receipts/gbs5-ctl-suffix.json as audited>",
  "gbs5-ctl-digest-alter": "<sha256 of receipts/gbs5-ctl-digest-alter.json as audited>",
  "gbs5-ctl-early-close": "<sha256 of receipts/gbs5-ctl-early-close.json as audited>"
 },
 "driver_exit_code": 0,
 "owned_children_after_exit": [],
 "stop_or_signal_observed": null,
 "raw_audit": "PASS"
}
```

The parent writes this record (create-exclusive) **only** after all of the following hold:

1. Its own tool observed the driver process fully return with exit status 0.
2. `ps` shows that no owned child survives: no kissat, drat-trim or helper with this desk's paths.
3. No stop or signal was observed.
4. The raw audit passes:
   - every receipt, commit, completion and log;
   - no `.cancelled.json` record;
   - `runs/run-<run_tag>.json` with `stopped_reason` null and every entry COMPLETE.

A non-zero exit status is never released. That includes 3 (stopped or publication error), 4 (signal latched),
5 (terminal failure) and death by a signal (shell status 143 or 130).

## Native-control plan (needs a NEW explicit parent GO bound to v5; nothing here has been run)

Preconditions:
- a delta source GO for `gb_staged_v5.py` a0e59977…353a;
- the parent GA driver has exited. At 13:07 PDT it was still running: pid 64001, drat-trim 98331, cadical 98333.
- the shell that launches the driver must not block SIGTERM/SIGINT; the driver refuses an inherited blocked mask.
- disk: the monitor showed 27.4e9 B free at 13:10 PDT, falling about 0.4e9 B/min. The launch gate re-measures it
  against the unchanged floor.

1. Parent GO record, written under `review/` outside this desk:

```json
{
 "status": "PARENT_GO",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "script_sha256": "a0e59977c3bd2e97ca0a39c33f5af11302e001d5f3ec22c5b4fc0b67f79c353a",
 "pre_exec_sha256": "8fad6b7456889e974537d29e2526d26f00cbf95fad803ed090ca98d50c1b19dc",
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

2. Launch in the **foreground**, so that the parent's tool observes the actual exit status (no `nohup`, no `&`):

```sh
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1
GO=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/<parent-go-file>.json
( cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v5.py" run "$DESK/PRE-EXEC-gbs5-controls-v5.json" "$GO" \
  > "$DESK/logs/run-gbs5-controls-v5.console.txt" 2>&1
  driver_rc=$?; printf 'driver exit status %s\n' "$driver_rc"; exit "$driver_rc" )
```

3. After it returns:
   - record the exit status;
   - run `ps -axo pid,ppid,pgid,etime,command`, which must show no owned survivor;
   - check each label read-only. Before the release, each one must report exactly one problem, the missing release,
     and exit 2:
     `TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v5.py" qualification gbs5-ctl-<name>`
   - do the raw audit; if everything passes, write the release record above;
   - re-run `qualification` for all seven labels, which must now exit 0. Only then can science be considered.

4. Preregistered verdicts. These are unchanged; the allowed outcomes and vetoes are in `PINS-gbs5-v5.json`
   `controls_7`.

| control | label | verdict |
|---|---|---|
| `control:unsat` | `gbs5-ctl-unsat` | PASS |
| `control:sat-checker` | `gbs5-ctl-sat-checker` | AS_PREREGISTERED_NOT_VERIFIED |
| `control:short-cnf` | `gbs5-ctl-short-cnf` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:truncate` | `gbs5-ctl-truncate` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:suffix` | `gbs5-ctl-suffix` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:digest-alter` | `gbs5-ctl-digest-alter` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:early-close` | `gbs5-ctl-early-close` | AS_PREREGISTERED_FAIL_CLOSED |

## Science procedure (a separate GO per item, then a separate release per run; not authorized here)

```sh
TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v5.py" \
  preexec "$DESK/PRE-EXEC-gbs5-<ID>-a1.json" gb:<ID>:a1     # admitted only with all 7 released controls
# parent GO: "scope": "science", "items": ["gb:<ID>:a1"], "pre_exec_sha256": <that PRE-EXEC>, script v5
( cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v5.py" run "$DESK/PRE-EXEC-gbs5-<ID>-a1.json" "$GO" \
  > "$DESK/logs/run-gbs5-<ID>-a1.console.txt" 2>&1
  driver_rc=$?; printf 'driver exit status %s\n' "$driver_rc"; exit "$driver_rc" )
```

A science PASS is admitted only after the parent's release for that run, with `"scope": "science"`. After the release,
`qualification gbs5-<ID>-a1` must exit 0.

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

## Boundaries

- While a run is active, do not run the selfcheck, a second driver, or any process whose argv contains `gb_staged_v`.
  Any of these is an exclusion breach and fails closed. The H17 children receive the runtime path through the
  environment, so their argv does not name the runtime.
- The pure checks use stub natives, fake lane scans, real SIGTERM/SIGINT, and pure-Python child processes for the
  terminal boundary. They do not establish native behaviour. Only the seven control runs, together with the parent's
  observation and release, can do that.
- Power loss before the release can only prevent admission. Acceptance depends on the exit status the parent observed
  and on the audited bytes, which are re-hashed at every admission.
- Nothing is deleted. Spent FIFOs, `.prepare` records, logs, failed attempts and UNKNOWN receipts are kept.
- Known limits accepted by the parent for the control run. Source: the Codex v5 delta review
  `review/n8-gb-staged-v5-delta-codex-v1.note.md` (af2a46b3…631e). The code is not changed, to avoid a new review
  cycle.
  - MINOR 2: `release_problems()` validates the release path (`lexists`, `islink`, `isfile`, `realpath`) and then
    opens it with an ordinary `open()`: no `O_NOFOLLOW`, no descriptor-relative open, no `fstat` of the opened file.
    The runtime does not exclude a replacement in `review/` between the check and the open. Operationally it cannot
    happen: only the parent publishes releases, each created exclusively and never replaced, and the producer has
    no release-writing path.
  - MINOR 3: some selfcheck descriptions overstate coverage.
    - H14 calls the reader synchronously inside the publication wrapper. It is not an independent concurrent reader,
      and it never reads between the summary link and its directory sync.
    - H2 checks that release hashes are present. It does not mutate a release and show rejection at science launch.
    - H17 omits exit-5 cases and the deferred-handler handoff around blocking and default-disposition installation.
    The check results, not their descriptions, are the evidence.
