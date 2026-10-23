# GB staged parent replay v4 — delta repairs of the gbs3 delta review, frozen pins and native-control plan

Written 2026-10-18T12:36:17-07:00 (host clock). **No kissat or drat-trim process has been started by this desk; no n=8 GB generation.**
v1, v2 and v3 (6f5b3a8a…0f14) are preserved unchanged and are not authorized for native work. The Codex delta review
`review/n8-gb-staged-v3-delta-codex-v1.note.md` (eb8f8ac4…be17) closed the scalar-FD finding and left two MAJORs; v4
repairs exactly those. The previous cancellation semantics are kept (no weakened snapshot). Generation stays in RAM.
There is no FIFO deletion and no automatic retry. The 18 inputs and the 7 controls are unchanged; only the labels
change, to `gbs4-`. Scope: exact-input proof certification; no n8 theorem, transfer or novelty claim.

## Frozen identity (delta re-review target)

| artifact | sha256 | bytes |
|---|---|---|
| `scripts/gb_staged_v4.py` (runtime) | `b9f9d562ca2640185c57f1aeded895f0159feef156f73391acb9c73fba339cdf` | 188562 |
| `DIFF-gb_staged_v3-to-v4.txt` (20 hunks) | `d2a06f4fcd3237db5541bed224a98e4d07a4625238b149685e3a0615138a6e03` | 35243 |
| `scripts/selfcheck_gb_staged_v4b.py` (pure checks) | `8b86ed1bfb1acf9161f543cf12bc48d698b13029de0a428be865475c51eb6b40` | 93438 |
| `SELFCHECK-gbs4-v4b.json` — **PASS 85/85** | `83454189baaebcd3942e6db24b7b260d770459e1e566d167475da66960425796` | 32360 |
| `PINS-gbs4-v4.json` (pin manifest + dispositions) | `17f10d1d7f812bf0fe5886666fd2c44e39a38167710e45f6c798c8f4bcce92d9` | 41486 |
| `PRE-EXEC-gbs4-controls-v4.json` (the 7 controls) | `814b23d4a761b6dd64caa9b324ee0a6e2d2c626e0d6dc40658e501506ffcf3b3` | 32228 |

Retained failed attempt: `selfcheck_gb_staged_v4.py` (4fc608a9…b79e) produced `SELFCHECK-gbs4-v4.json` FAIL 82/83
(40ca881b…5f69). The failure was selfcheck-only. Its H10 hook failed every `os.link`, so the run summary could not be
published either; the runtime correctly published nothing admissible, and the check then crashed reading the absent
summary. v4b fails only the commit's link. The runtime is unchanged.

## Delta dispositions (line numbers in gb_staged_v4.py)

| delta finding | repair | where | pure checks |
|---|---|---|---|
| (1) os.link publishes qualified:true before the post-link directory sync; a later failure leaves an admissible commit and the reader ignores the failed run entry | the commit is now only the decision record ('meaning': admission also needs the bound completion record, no cancellation and a clean durable run summary). Only a qualified decision with nothing pending/latched after the commit's durable publication (publish_record: synced .prepare, os.link, directory sync; any failure raises) gets the completion record <label>.complete.json bound to the exact receipt and commit sha256 (publication_completed true), published the same way. Any failure after a qualified decision (commit link, post-link directory sync, F_FULLFSYNC, close, completion write, an interruption) creates the persistent cancellation veto <label>.cancelled.json. The reader qualification_problems() requires the durable receipt, the qualified commit, the completion bound to that commit and receipt, NO cancellation, and the durable summary of the producing run (run_tag) with stopped_reason None, no signal at the summary, no run cancellation, and the label's entry with publication COMPLETE and the same three digests; validate_controls() admits only through it (an early commit flag alone never qualifies); the read-only CLI 'qualification LABEL' prints it. cmd_run stops the desk on a CANCELLED/FAILED publication and the run summary is itself published durably | L587, L598, L607, L610, L536, L546, L691, L719, L726, L734, L1535, L3039, L658, L3096 | H1 (completion bound, no cancellation, clean summary, qualification_problems == []); H9 receipt fsync EIO; H10 commit link ENOSPC; H10b directory sync EIO after the commit link; H10c directory sync EIO after the completion link; H10d F_FULLFSYNC failure after the commit link; H10e directory close failure after the commit link; H10f interrupted completion; H12 run-summary signal (run cancellation) |
| (2) the pending-signal snapshot precedes active_count/decided_at/serialization and H8 accepts a signal after the link (weakened cancellation semantics) | previous cancellation semantics preserved through the successful publication, no snapshot linearization: SIGTERM/SIGINT stay blocked from the decision to the end of the item's publication; the decision itself requires no latched and no pending signal and a single-threaded driver (another thread could run the handler); after the commit publication and again after the completion publication the pending and latched signals are re-checked; any signal there cancels the item (veto record, no completion or a completion that admission refuses because the veto exists); the restored mask delivers a pending signal to the latching handler before the status is decided, and a signal delivered then also cancels the item; the run summary is published under the same protocol and a signal through it creates runs/run-<tag>.cancelled.json, which admission refuses. Residual: a crash (power loss) after the veto's exclusive creation but before its directory sync could lose the veto; a failed veto write is recorded as an error and the run summary (required by admission) then records the stop | L577, L582, L588, L599, L617, L618, L632, L652, L667, L711, L729 | H0 single-threaded preflight; H4 SIGTERM during evaluation; H5 SIGTERM in the preparation window; H7 SIGINT pending at the decision; H8 SIGTERM after the commit link; H8b SIGINT before the commit link; H8c SIGTERM during the commit serialization; H8d SIGINT after the completion link; H8e SIGTERM delivered at the mask restore; H11 another thread at the decision; H12 SIGTERM during the run-summary publication |

Publication protocol (`publish_qualification`, L564–L636):

1. Block SIGTERM/SIGINT (L577).
2. Decide (L582). The decision requires eligibility, no latched signal, no pending signal and
   `active_count()==1`.
3. Publish the commit (L587): durable `.prepare`, `os.link`, then a directory sync.
4. Re-check the pending and latched signals (L588).
5. Qualified items only: publish the completion record, bound to the receipt sha and the commit sha (L598).
6. Re-check again (L599).
7. Any signal or failure after the decision creates the `.cancelled.json` veto (L607, L610).
8. Restore the mask (L617). A signal delivered then also cancels (L618).

Only status COMPLETE can be admitted. The run summary is published the same way (L652–L667).

Admission is `qualification_problems` (L691–L740),
used by `validate_controls` (L1535) and by the read-only CLI `qualification LABEL`. It requires:

- the durable receipt;
- a qualified commit;
- a completion bound to that commit and receipt;
- no item cancellation;
- the producing run's durable summary, which must show `stopped_reason` None, no signal at the summary and no run
  cancellation, and must list the label's entry as COMPLETE with the same three digests.

Residual risk: a power loss after the veto's exclusive creation but before its directory sync could lose the veto.

## Native-control plan (needs a NEW explicit parent GO bound to v4; nothing here has been run)

Preconditions:

- a delta source GO for `gb_staged_v4.py` b9f9d562…9cdf;
- the parent GA driver (pid 64001, still running at 12:30 PDT, with drat-trim 47633) has exited. The gate waits for it.

1. Parent GO record under `review/` outside this desk:

```json
{
 "status": "PARENT_GO",
 "desk": "review/moqls8-gb-parent-staged-replay-v1",
 "script_sha256": "b9f9d562ca2640185c57f1aeded895f0159feef156f73391acb9c73fba339cdf",
 "pre_exec_sha256": "814b23d4a761b6dd64caa9b324ee0a6e2d2c626e0d6dc40658e501506ffcf3b3",
 "scope": "controls",
 "items": ["control:unsat", "control:sat-checker", "control:short-cnf", "control:truncate", "control:suffix", "control:digest-alter", "control:early-close"]
}
```

2. Launch:

```sh
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1
GO=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/<parent-go-file>.json
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v4.py" run "$DESK/PRE-EXEC-gbs4-controls-v4.json" "$GO" \
  > "$DESK/logs/run-gbs4-controls-v4.console.txt" 2>&1 &
```

   Per control the run writes:
   - `receipts/gbs4-ctl-<name>.json`, durable;
   - `.commit.json` and `.complete.json`, each with its hard-linked `.prepare`;
   - no `.cancelled.json`;
   - the kissat log, the filtered drat-trim log and the retained FIFO.

   It also writes `logs/driver-<tag>.log` and `runs/run-<tag>.json` (+ `.prepare`). Any non-COMPLETE control
   publication stops the run.

3. After the run, check each label read-only: `TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B
   "$DESK/scripts/gb_staged_v4.py" qualification gbs4-ctl-<name>` (exit 0 only if admitted).

4. Preregistered verdicts. These, and the allowed outcomes and vetoes, are unchanged from v3 and are listed in
   `PINS-gbs4-v4.json` `controls_7`:

| control | verdict |
|---|---|
| `control:unsat` | PASS |
| `control:sat-checker` | AS_PREREGISTERED_NOT_VERIFIED |
| `control:short-cnf` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:truncate` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:suffix` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:digest-alter` | AS_PREREGISTERED_FAIL_CLOSED |
| `control:early-close` | AS_PREREGISTERED_FAIL_CLOSED |

## Science procedure (a separate GO per item; not authorized here)

```sh
TMPDIR="$DESK/tmp/" /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B "$DESK/scripts/gb_staged_v4.py" \
  preexec "$DESK/PRE-EXEC-gbs4-<ID>-a1.json" gb:<ID>:a1
# parent GO: "scope": "science", "items": ["gb:<ID>:a1"], "pre_exec_sha256": <that PRE-EXEC>, script v4
cd "$DESK" && set -C && TMPDIR="$DESK/tmp/" nohup /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B \
  "$DESK/scripts/gb_staged_v4.py" run "$DESK/PRE-EXEC-gbs4-<ID>-a1.json" "$GO" \
  > "$DESK/logs/run-gbs4-<ID>-a1.console.txt" 2>&1 &
```

A science PASS qualifies only if `qualification gbs4-<ID>-a1` returns no problems.

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

- While a run is active, do not run the selfcheck, a second driver, or any process whose argv contains `gb_staged_v`.
  Any of these is an exclusion breach and fails closed.
- Pure checks use stub natives, fake lane scans, and real SIGTERM/SIGINT delivered to the single-threaded selfcheck
  process. They do not establish native behaviour; only the seven control receipts and their COMPLETE publications
  can do that.
- Free space measured by the sandbox gate at 12:30 PDT was 51.7e9 B and falling (other lanes). The launch gate
  re-measures it.
- Nothing is deleted. Spent FIFOs, `.prepare` records, logs, failed attempts and UNKNOWN receipts are retained.
