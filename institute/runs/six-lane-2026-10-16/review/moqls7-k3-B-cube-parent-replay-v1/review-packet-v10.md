# M7 B-side parent replay desk: review packet for the v9 (B/C311+cuts) and v10 (Codex HOLD repairs) scripts

Generated 2026-10-18T07:54:08-07:00 by M7BCubeParentReplay. Desk: `review/moqls7-k3-B-cube-parent-replay-v1/`.
The staged files are in `staging-Bcuts/`. Nothing in `scripts/` changes while B_C321-a3 (launch_B_v8) runs. After a3 has ended, the staged files will be copied into `scripts/` with `cp -n`, and their SHA-256s re-checked against this table. B_C411-p1 and B_C311cuts-p1 launch only under `launch_B_v10.py`, after Codex's re-review and Main's explicit GO.

## Inputs

- `review/m7-launch-v6-r9-codex-v1.note.md` 7897 B sha256 `b9db41b60ade5623f7651fa55f60815d8e0cfc0798f9f40a1a09d4a99c344f93`
- `review/m7-launch-v6-r9-parent-addendum-v1.md` 4046 B sha256 `595999fba42c7b89d4d9b1dc5a04b3a5d152fcc772b9107562ef2df115f57c1a`
- Main, 07:32 PDT, long-job stability amendment. It is adopted in v10 and cited in `MON["source"]` and in the docstring:
  - last free >= 13.5e9 B;
  - max peak-to-later drop within the last 300 s <= max(300,000,000 B, (free_last - 13.5e9)/12);
  - sample quality: tz-aware, strictly increasing timestamps; 0 <= age <= 30 s; >= 25 samples spanning >= 290 s;
  - a stale monitor refuses.
  Source: the parent monitor `review/disk-monitor-v1-20261018T0722-to-1810.jsonl`.

## Staged files (`staging-Bcuts/`)

| file | bytes | sha256 |
|---|---|---|
| `bklib_v3.py` | 44858 | `51d34190e25001862699642558de0b157734096e9472ac25e2040bda11c406bc` |
| `compose_Bcuts_v1.py` | 8586 | `a5d303fda264026ae9ed644618da0d9142dfeaf6e98ec065bfbcc630a96907dc` |
| `replay_B_v4.py` | 24442 | `1a67794572b2b8b9c73737f3581f85c474c94a544b0f090ed6e0af77fd19f03f` |
| `launch_B_v9.py` | 35581 | `dee90b9bb30819a73c591dfb03d6bd60fb046a08ca7a555ecc3668320305960f` |
| `assemble_B_v9.py` | 40739 | `9c3c4241b53360df2c3ac7c4b1d8269ce0d266d72f2843c3b643b073afd7226c` |
| `launch_B_v10.py` | 63837 | `d55f12186deac37c2d74d359dcf2df26c286f03d1df3aa6af9c197635a38afad` |
| `assemble_B_v10.py` | 45469 | `3339537292a83aa3dc9a7918a7fdf2f084960ebd56773573dfb3cd9848882dee` |

## Diffs (desk root)

| diff | bytes | sha256 | content |
|---|---|---|---|
| `scripts-v8-to-v9-Bcuts.r2.diff` | 34600 | `54385cd424128e71ca2eca46ede11df930c8b74788a13c3c732de97110641e20` | v9 set vs scripts/ v8 set: bklib_v3, replay_B_v4, launch_B_v9, assemble_B_v9, new compose_Bcuts_v1 |
| `scripts-v8-to-v9-Bcuts.diff` | 31613 | `4fef55ab4f66bd57fe391f40bf3476494e8984dd5055e8cd9cf4da3787545ae3` | superseded first v9 diff (before the planned-compose and read-only-list fixes) |
| `scripts-v9-to-v10.diff` | 71254 | `f262ea22ecb061b9ec030039a6ab6d5a1701bd4ce3814dea8ac122a1724e673d` | Codex HOLD repairs: launch_B_v9 -> launch_B_v10, assemble_B_v9 -> assemble_B_v10 |
| `assembler-v5-to-v6-generalization.diff` | 27152 | `ca3e4e65fe5bb9b83331415cdc616c9c0e25e247a993c2c7c62a37bc3f8b9971` | item 5: the assembler hunks of scripts-v5-to-v6.diff, separately identified |

Evidence: `receipts/test-v10-selftest.selftest.json` 23627 B sha256 `e02396e68b5d7fd0e13995e28be21ab7795aa00f13ffbc0a2aad83d46c09ef1e`, all_ok True. It was produced by `staging-Bcuts/launch_B_v10.py` sha256 `d55f12186deac37c2d74d359dcf2df26c286f03d1df3aa6af9c197635a38afad`, the file in the table above.

## Mapping of the Codex HOLD items (part 1) to v10

1. **Fail-closed enumeration (BLOCKER).**
   - `run_helper` (launch_B_v10.py 290-364): rc must be 0 for both `ps` snapshots and for `lsof`, stderr must be empty, no SIGTERM, no exception, no lost child, and both readers must finish.
   - Strict parsers `parse_ps_id`/`parse_ps_args`/`parse_lsof` (367-417): any malformed, duplicate or empty row raises, and the census is then an error.
   - `census_once` (420-530): a live own-uid process whose args (same lstart), cwd (lsof) or identity (ppid/pgid/uid/lstart/comm equal in both identity snapshots) is unresolved is *unknown*. A live native of another uid is unknown.
   - `census` (533-551) retries at most 5 times, 2 s apart, and then returns an error, so admission is refused (`K.admission` returns not ok for an error scan).
2. **Consistent census (MAJOR).**
   - Order: ps identity (A), ps args (B), lsof cwd (L), ps identity (C).
   - C is classified. The join is by (pid, lstart), and C is re-validated against A; there is no PID-only join.
   - Cap detection (`--rss-cap`) and the slot veto use full argv. Receipts truncate argv only after matching.
   - The B/C411 r7 veto searches every process of every uid, zombies included, except: this launcher, its descendants and ancestors, and processes whose resolved cwd is inside this desk.
   - The desk's own slot-2 exclusivity is a separate condition, `desk_idle_no_other_attempt_process` (`admission_v10` 565-573).
   - Lane zombies are recorded separately and never counted as busy or RSS.
3. **Launch boundary (BLOCKER).** In `mode_run` (698-835):
   - the supervisor stdout log is opened at launcher start;
   - `prepare` (670-695) computes all hashes and the gate-receipt body, and `monitor_stability` runs, BEFORE the final census;
   - right after the final census, free bytes (>= GATE), `deadline_ok()`, launcher signals and the `*.QUARANTINE.json` glob are rechecked, then `Popen` follows;
   - the gate receipt is written by `after_spawn`, the `inject` hook of the unchanged `run_owned` (201-260), inside the ownership scope. An exception there takes run_owned's SIGTERM, bounded-wait and UNKNOWN path;
   - `deadline_ok` (160-163) also requires launch + 10,380 s <= 17:57 PDT.
   - *Not implemented:* serializing admissions with other desks' launchers. It needs their cooperation and a shared lock outside this desk's write scope.
4. **Helper bounds and isolation (MAJOR).** Exact sources follow.
   - `run_helper`: own session; after 60 s exactly one SIGTERM to the owned, unreaped child; a bounded 30 s wait; then a blocking wait with no further signal. Never SIGKILL, never a subprocess timeout.
   - On this host `/bin/ps` is setuid root (`-rwsr-xr-x root wheel`) and `/usr/sbin/lsof` is not setuid. Helpers run only before the supervisor spawn and never in a supervised group.
   - The driver `replay_B_v4.py` calls neither ps/lsof nor `_run_text`; it reads RSS through libproc.
5. **Assembler scope (MAJOR).** See the hunk table below and deviation D33 in `assemble_B_v10.py`.
6. **Tagged precheck provenance (MINOR).** `assemble_B_v10.py` lines 491-495 refuse before writing anything unless the selected `receipts/regen-ITEM[-TAG].json` hashes to the gate's `regen_receipt_sha256`. The result also records `bound_to_gate_regen_receipt_sha256`.

Main's 07:32 amendment: `monitor_stability` (591-657). It reads a bounded tail; complete JSON-object lines only; an unfinished last line is ignored; malformed lines and end events inside the window refuse. The deadline is checked before evaluation and again before success. It replaces v8's own statvfs window; the >= 62 s pause (`pause`, 660-667) between the two censuses remains.

## Item 4: exact helper sources

### bklib `_run_text` (identical in v1, v2, v3; no longer called by launch_B_v10.py)

`scripts/bklib_v1.py` sha256 `b17dee3d5b2685001e479bae5ceaf07277dce8d5aff8f2dbd4c8b3c6f2832c17`, lines 319-320:

```python
 319  def _run_text(argv):
 320      return subprocess.run(argv, stdin=subprocess.DEVNULL, capture_output=True, text=True, env=ENV, cwd=TMP)
```

`scripts/bklib_v2.py` sha256 `421fc576a4e766fd2fd0ef7740861ccb4cd4f8b58f342a4afd6d18f24467d2d7`, lines 335-336:

```python
 335  def _run_text(argv):
 336      return subprocess.run(argv, stdin=subprocess.DEVNULL, capture_output=True, text=True, env=ENV, cwd=TMP)
```

`staging-Bcuts/bklib_v3.py` sha256 `51d34190e25001862699642558de0b157734096e9472ac25e2040bda11c406bc`, lines 437-438:

```python
 437  def _run_text(argv):
 438      return subprocess.run(argv, stdin=subprocess.DEVNULL, capture_output=True, text=True, env=ENV, cwd=TMP)
```

Its only caller is `bklib.lane_scan`; neither `launch_B_v10.py` nor `replay_B_v4.py` calls `lane_scan` or `_run_text` (launch_B_v10 mentions `_run_text` only in its docstring).

### launch_B_v10.py `_pump`, `helper_reap`, `run_helper` (lines 271-364)

```python
 271  def _pump(stream, sink):
 272      for chunk in iter(lambda: stream.read(1 << 16), b""):
 273          sink.append(chunk)
 274  
 275  
 276  def helper_reap(p, box, ev, flags):
 277      """One waitpid on the owned helper. Ownership ends with the first statement after a successful wait, or on ECHILD
 278      (lost child: recorded, and the helper result is then not ok)."""
 279      try:
 280          pid, st = os.waitpid(box["owned"], flags)
 281      except ChildProcessError as e:
 282          box["owned"] = None
 283          ev["lost_child"] = repr(e)
 284          return
 285      if pid:
 286          box["owned"] = None
 287          p.returncode = ev["rc"] = os.waitstatus_to_exitcode(st)
 288  
 289  
 290  def run_helper(argv, limit=HELPER_LIMIT, term_wait=HELPER_TERM_WAIT):
 291      """Bounded, owned scan helper (ps, lsof), started in its own session: pgid = sid = helper pid, never in this
 292      launcher's group or in any supervised group. stdout and stderr are drained by reader threads. Past `limit` s, or on
 293      an exception after Popen, exactly one SIGTERM goes to the owned, unreaped child (its PID is reserved), then a
 294      bounded wait of `term_wait` s; if the child is still unreaped, a blocking wait with no further signal. Never
 295      SIGKILL, never a subprocess timeout. ok only for rc 0, empty stderr, no SIGTERM, no exception, no lost child, no
 296      wait error and both readers finished."""
 297      t0 = time.monotonic()
 298      ev = {"argv": argv, "pid": None, "pgid": None, "sid": None, "rc": None, "term_sent_after": None,
 299            "unreaped_after_term_wait": False, "blocking_wait": False, "exception": None, "lost_child": None,
 300            "wait_errors": [], "readers_finished": None, "stdout": "", "stderr": "", "seconds": None, "ok": False}
 301      p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
 302                           cwd=K.TMP, env=K.ENV, start_new_session=True)
 303      box = {"owned": p.pid}                          # registration: the statement right after Popen
 304      out, err, readers = [], [], []
 305      try:
 306          try:
 307              ev["pid"] = box["owned"]
 308              for stream, sink in ((p.stdout, out), (p.stderr, err)):
 309                  readers.append(threading.Thread(target=_pump, args=(stream, sink), daemon=True))
 310                  readers[-1].start()
 311              try:
 312                  ev["pgid"], ev["sid"] = os.getpgid(ev["pid"]), os.getsid(ev["pid"])
 313              except OSError as e:                    # the helper may already have exited (still unreaped)
 314                  ev["pgid"] = ev["sid"] = repr(e)
 315              while box["owned"] is not None:
 316                  helper_reap(p, box, ev, os.WNOHANG)
 317                  if box["owned"] is None:
 318                      break
 319                  elapsed = time.monotonic() - t0
 320                  if ev["term_sent_after"] is None and elapsed >= limit:
 321                      os.kill(box["owned"], signal.SIGTERM)       # owned => unreaped => PID reserved
 322                      ev["term_sent_after"] = round(elapsed, 3)
 323                  elif ev["term_sent_after"] is not None and elapsed >= limit + term_wait:
 324                      ev["unreaped_after_term_wait"] = True
 325                      break
 326                  time.sleep(0.02)
 327          except BaseException as exc:
 328              ev["exception"] = repr(exc)
 329              if box["owned"] is not None and ev["term_sent_after"] is None:
 330                  try:
 331                      os.kill(box["owned"], signal.SIGTERM)
 332                      ev["term_sent_after"] = round(time.monotonic() - t0, 3)
 333                  except BaseException as e:
 334                      ev["wait_errors"].append(repr(e))
 335              end = time.monotonic() + term_wait
 336              while box["owned"] is not None and time.monotonic() < end:
 337                  try:
 338                      helper_reap(p, box, ev, os.WNOHANG)
 339                  except BaseException as e:
 340                      ev["wait_errors"].append(repr(e))
 341                  if box["owned"] is not None:
 342                      time.sleep(0.02)
 343              ev["unreaped_after_term_wait"] = box["owned"] is not None
 344      finally:
 345          while box["owned"] is not None:             # no further signals: wait for the known child to exit
 346              ev["blocking_wait"] = True
 347              try:
 348                  helper_reap(p, box, ev, 0)
 349              except BaseException as e:
 350                  ev["wait_errors"].append(repr(e))
 351                  time.sleep(0.25)
 352      for t in readers:
 353          t.join(10)
 354      ev["readers_finished"] = len(readers) == 2 and not any(t.is_alive() for t in readers)
 355      if ev["readers_finished"]:
 356          p.stdout.close()
 357          p.stderr.close()
 358      ev["stdout"] = b"".join(out).decode("utf-8", "replace")
 359      ev["stderr"] = b"".join(err).decode("utf-8", "replace")
 360      ev["seconds"] = round(time.monotonic() - t0, 3)
 361      ev["ok"] = (ev["rc"] == 0 and ev["term_sent_after"] is None and ev["exception"] is None
 362                  and ev["lost_child"] is None and not ev["wait_errors"] and ev["readers_finished"]
 363                  and ev["stderr"] == "")
 364      return ev
```

### GATE and lane-budget constants: bklib_v3.py lines 70-88 (sha256 `51d34190e25001862699642558de0b157734096e9472ac25e2040bda11c406bc`)

```python
  70  GIB = 1 << 30
  71  FLOOR = 12000000000                   # in-flight free-space floor: cooperative stop below it
  72  LAUNCH_BASE = 12200000000             # admission gate base (parent rule)
  73  PROJECTED_GROWTH = 1048576            # upper bound on this desk's remaining retained growth (logs, receipts, report)
  74  GATE = LAUNCH_BASE + PROJECTED_GROWTH
  75  LANE_RSS_LIMIT = 8 * GIB              # phys-2 lane total RSS limit
  76  LANE_NATIVE_MAX = 4                   # phys-2 lane busy native processes limit
  77  OTHER_NATIVE_MAX_AT_LAUNCH = 2        # launch only if a fresh scan shows at most this many busy lane natives
  78  PROJECTED_PEAK = 2 * GIB              # this run's projected aggregate peak (producer B/C321 peak 1,629,880,320 B)
  79  CAP_MAX = 3584 * 1024 * 1024          # never set this desk's RSS cap above the lane's standard 3.5 GiB stop
  80  MIN_CAP = 2560 * 1024 * 1024          # refuse admission if the computable cap is below 2.5 GiB
  81  UNSUPERVISED_GROUP_RESERVE = 3584 * 1024 * 1024   # reserve for an unsupervised lane native group (lane's 3.5 GiB stop)
  82  OTHER_LANE_MARGIN = 256 * 1024 * 1024 # added to the current RSS of uncovered non-native lane processes
  83  SAFETY_MARGIN = 128 * 1024 * 1024
  84  GRACE = 120                           # bounded wait after SIGTERM to own children, seconds
  85  PERIOD = 0.25
  86  CHECKPOINT_EVERY = 600
  87  ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
  88         "PYTHONDONTWRITEBYTECODE": "1", "HOME": TMP}
```

GATE = 12,200,000,000 + 1,048,576 = 12201048576 B. FLOOR = 12,000,000,000 B (in flight, enforced by the supervisor and the driver).

### Self-test evidence (`receipts/test-v10-selftest.selftest.json`, all_ok True)

The test process had pid 81367, pgid 81367 and sid 81367. Signals sent (os.kill instrumented): [{"pid": 81369, "signal": "SIGTERM", "t": 2.043}, {"pid": 81375, "signal": "SIGTERM", "t": 4.097}].

| case | pid | pgid | sid | rc | SIGTERM after s | unreaped after bounded wait | blocking wait | seconds | ok |
|---|---|---|---|---|---|---|---|---|---|
| ps_ok | 81368 | 81368 | 81368 | 0 | None | False | False | 0.033 | True |
| term_honoring | 81369 | 81369 | 81369 | -15 | 2.009 | False | False | 2.04 | False |
| term_ignoring | 81375 | 81375 | 81375 | 0 | 2.023 | True | True | 8.057 | False |
| nonzero_rc | 81419 | 81419 | 81419 | 1 | None | False | False | 0.033 | False |
| stderr_output | 81420 | 81420 | 81420 | 0 | None | False | False | 0.06 | False |

Checks: ps_ok_is_ok_rc0_own_pid=True, term_honoring_one_sigterm_at_limit_reaped_in_bounded_wait=True, term_ignoring_one_sigterm_then_blocking_wait_until_self_exit=True, exactly_two_signals_both_sigterm_to_owned_helpers=True, timed_helpers_in_own_sessions=True, nonzero_rc_not_ok=True, stderr_output_not_ok=True, every_helper_reaped_no_lost_child=True, census_complete=True.

Census at 2026-10-18T07:50:22-07:00: 1 try (['complete']); counts {"first": 1199, "args": 1199, "lsof": 833, "second": 1199}; helper rc/seconds/pgid {"ps_id_1": [0, 0.059, 81421], "ps_args": [0, 0.089, 81422], "lsof_cwd": [0, 0.329, 81423], "ps_id_2": [0, 0.084, 81425]}.

- Busy lane natives: 4 ([[74330, 'drat-trim'], [74331, 'cadical'], [75121, 'drat-trim'], [75122, 'kissat']]).
- Supervised: [[74322, 3758096384], [75097, 2797076480]].
- Reserved 6849921024 B; ancestry headroom 1605795840 B.
- Desk attempt processes (B_C321-a3): [[73730, 'Python'], [75097, 'Python'], [75099, 'Python'], [75121, 'drat-trim'], [75122, 'kissat']].
- B/C411 matches: 0. Lane zombies: 0.

Informational admission (no launch): not ok, because ['natives_at_most_2', 'cap_at_least_min', 'ancestry_headroom_for_fixed_cap', 'desk_idle_no_other_attempt_process'].

Monitor stability: ok True; age 0.1 s; 30 window samples spanning 291.0 s; free_last 184491978752; max_drop 1271812096; limit 14249331562.666666.

## Item 5: assembler hunk set v5 -> v6 (`assembler-v5-to-v6-generalization.diff`)

| hunk | diff lines | class | rationale |
|---|---|---|---|
| `@@ -1,14 +1,13 @@` | 3-26 | docstring and usage text | describes v6; no code |
| `@@ -24,76 +23,55 @@` | 27-146 | deviation texts; new ITEM_DEVIATIONS dict (D29) | attempt-2-only texts (D22-D24) stay in deviations-v2.json; item pins documented per item; data only |
| `@@ -277,10 +255,10 @@` | 148-162 | scope string from item pins | B/C321 constant -> it['cube'], it['cnf_sha256']; text only |
| `@@ -293,17 +271,22 @@` | 163-193 | report title/verdict row by item; attempt-1 line optional | B/C411 and B/C311+cuts have no attempt 1; report text only |
| `@@ -348,13 +331,14 @@` | 194-212 | report wording; regen receipt path | tagged regen receipts; text only |
| `@@ -387,20 +371,20 @@` | 213-242 | report section names by label | outputs are per label; text only |
| `@@ -427,17 +411,18 @@` | 243-267 | output names by label; deviation composition (ITEM_DEVIATIONS + generic D30 stop) | v5's RESULT.v2.json/REPORT.v2.md/deviations-v2.json exist from attempt 2 and outputs are exclusive-create; D22 was attempt-2 specific |
| `@@ -445,30 +430,37 @@` | 268-314 | desk-listing exclusion by label; attempt-1 history optional; result entries for newer diffs | v5 raises without receipts/<ITEM>.json; recorded as None instead |
| `@@ -502,7 +494,7 @@` | 315-323 | deviations path by label | output naming |
| `@@ -516,8 +508,8 @@` | 324-334 | printed summary keys by label | stdout only |

None of these hunks touches `item_receipt`'s conditions, the PASS/UNKNOWN rule, the measured feeds or the strict status-line parser (bklib). The behaviour is kept; restoring v5 would fail on exclusive names and on missing attempt-1 history.

## Copy-in and launch plan (after Codex re-review and Main's GO)

1. After B_C321-a3 ends and is assembled with `assemble_B_v8.py`: `cp -n staging-Bcuts/{bklib_v3.py,compose_Bcuts_v1.py,replay_B_v4.py,launch_B_v9.py,assemble_B_v9.py,launch_B_v10.py,assemble_B_v10.py} scripts/`. Then re-hash each file and compare it with the table above.
2. `replay_B_v4.py regen B_C311cuts` precheck (B_C411 reuses `receipts/regen-B_C411-r2.json` bfad6051...89c5e).
3. `launch_B_v10.py run B_C411 --label B_C411-p1 --regen-tag r2`. After it ends cleanly: `launch_B_v10.py run B_C311cuts --label B_C311cuts-p1`. Assemble each with `assemble_B_v10.py`.

