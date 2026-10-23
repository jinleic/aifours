#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v10.

v10 = launch_B_v9.py with the repairs required by Codex's HOLD on the v6 admission (review/m7-launch-v6-r9-codex-v1.
note.md b9db41b6...4f93; parent addendum review/m7-launch-v6-r9-parent-addendum-v1.md 595999fb...7c1a, items 1-4) and
Main's 07:32 PDT long-job stability amendment:
  (1) fail-closed enumeration. Every scan helper (ps identity snapshot, ps args snapshot, lsof cwd listing, second ps
      identity snapshot) must exit 0 with empty stderr within its bound. Every row must parse completely
      (pid ppid pgid uid state rss lstart comm; pid lstart args; lsof p/f/n records only). A live own-uid process
      without resolved identity (args with the same lstart, a cwd from lsof, the same ppid/pgid/uid/lstart/comm in
      both identity snapshots) is unknown, never foreign. The census is then retried (at most 5 tries, 2 s apart)
      and otherwise refused. A live native of another uid (cwd unreadable) is unknown and refused the same way;
  (2) consistent census. The two identity snapshots bracket the args snapshot and the lsof listing. The join is by
      (pid, lstart) and is re-validated by the second snapshot, which is the one classified. Cap and slot detection
      search full argv; receipts truncate argv only after matching. The B/C411 r7 veto searches every process of every
      uid, zombies included. It excludes only this launcher, its descendants, its ancestors and processes whose
      resolved cwd is inside this desk. This desk's exclusivity in slot 2 is a separate condition: no other attempt
      process with cwd inside this desk (a native, supervise_r*, replay_B_*, compose_B* or 'launch_B_* run'). Lane
      zombies are recorded separately, as ownership/reaping evidence, and are never counted as busy or as RSS;
  (3) launch boundary. The supervisor stdout log is opened when the launcher starts. Hashes and the gate-receipt
      body are prepared, and the monitor stability rule is evaluated, BEFORE the final census. Immediately before
      Popen, after the final census, the launcher rechecks free bytes (>= 12.2e9 + growth), deadline_ok(), its
      signals and the quarantine glob. The gate receipt is written right after the spawn, inside run_owned()'s
      ownership scope via its inject hook. A failure there takes run_owned()'s exception path (UNKNOWN);
  (4) scan helpers run through run_helper(). Each runs in its own session (pgid = sid = helper pid), so it is never
      in this launcher's group or any supervised group; /bin/ps is setuid root on this host. Each is bounded: after
      60 s exactly one SIGTERM goes to the owned, unreaped child, then a bounded 30 s wait, then a blocking wait with
      no further signal. There is never a SIGKILL or a subprocess timeout. bklib's _run_text is no longer called.
      'selftest-v10 LABEL' demonstrates this, plus one census and one monitor evaluation, and launches nothing;
  (5) deadline_ok() also requires launch + supervisor wall + grace (10,380 s) <= 17:57 PDT (Main: native work ends by
      17:57), i.e. no launch after 15:04 PDT;
  (6) stability, per Main's 07:32 PDT amendment, evaluated from the parent monitor
      review/disk-monitor-v1-20261018T0722-to-1810.jsonl:
        * complete JSON-object lines only; an unfinished last line is ignored, other malformed lines in the window
          refuse;
        * timezone-aware, strictly increasing sample timestamps; last-sample age 0..30 s;
        * >= 25 samples in [t_last - 300 s, t_last], spanning >= 290 s;
        * last free >= 13.5e9 B, and maximum peak-to-later drop in the window <= max(300,000,000,
          (free_last - 13.5e9) / 12);
        * an end event or a stale monitor refuses.
      This replaces v8's own 300 s statvfs window. A >= 62 s pause between the first admitting census and the final
      census remains, and both free readings must be >= 12.2e9 + growth (v6 rule (c)).
Not implemented: serializing admissions with other desks' launchers. That needs their cooperation and a shared lock
outside this desk's write scope. The final census and rechecks immediately before spawn narrow the window but cannot
make it atomic. run_owned(), on_term, the outcome receipt, the fixed RSS cap, supervisor arguments, the driver
(replay_B_v4.py) and bklib_v3 are unchanged.

v9 = launch_B_v8.py with an import-only bump for B/C311+cuts: bklib_v3 (B_C311cuts item) instead of bklib_v2, and the
driver replay_B_v4.py (bklib_v3 import; planned compose names the item's script). The usage string names v9;
everything else is byte-identical to v8.

v8 = launch_B_v7.py with one change, Main's long-job stability rule (07:16 PDT) in the admission. Between the first
admitting scan and the second fresh scan (immediately before launch), the 62 s pause becomes a stability window. For
300 s, free bytes are read by statvfs every 30 s (no new processes). Admission requires every reading >= 13.5e9 B and
no drop above 300,000,000 B from any earlier reading to any later one within the window. The second scan must still
pass all v6 conditions, including free >= 12.2e9 + growth. A window that fails or is interrupted restarts the cycle.
v8 serves both items, because bklib_v2 pins B_C321 exactly as bklib_v1 did and adds B_C411; the driver is
replay_B_v3.py. Everything else is byte-identical to v7, including the optional --regen-tag.

v7 = launch_B_v6.py with an import bump for B/C411: bklib_v2 (B_C411 item pin) instead of bklib_v1, and the driver
replay_B_v3.py. One addition: 'run ITEM --label LABEL [--regen-tag TAG]' takes the regeneration precheck from
receipts/regen-ITEM-TAG.json instead of receipts/regen-ITEM.json, which a 07:12:31 free-space deferral spent for B_C411.

v6 = launch_B_v5.py with one change, the admission gate (Main's a3 GO, about 07:05 PDT):
  (a) lane identity by cwd and ancestry. A process counts as phys-2 (M7) only if its cwd is inside the moqls7-maximum
      lane or a review/moqls7-* desk, or it descends from such a process. Binary and script paths in argv no longer
      count. v5's marker scan counted ME3's supervise_r3 runs and PA19's drat-trim, which only use M7/parent paths;
  (b) RSS cap fixed at Main's conservative 2,797,076,480 B for the supervisor and the driver. Admission also requires
      the ancestry headroom min(3.5 GiB, 8 GiB - ancestry reservations - 128 MiB) to be >= that cap;
  (c) two fresh free-space readings >= 12.2e9 + projected growth, the second >= 60 s after the first and taken with a
      fresh scan immediately before launch; all admission conditions must hold at both readings;
  (d) no admission or launch after 17:30 PDT.
Everything else is unchanged from v5:
v5: run_owned() never returns while its child is owned and unreaped (best-effort marker, then a blocking wait);
  * every operation after a successful Popen is inside the cleanup scope: the PID is registered by the statement right
    after Popen and everything else runs inside try/except/finally;
  * the finally block never lets run_owned() return or raise while the child is owned and unreaped. After the bounded
    SIGTERM wait of the exception path, if ownership remains, it writes a desk-owned quarantine/UNKNOWN marker (best
    effort: a write failure is recorded and never skips the wait). It then keeps ownership and waits (blocking wait4)
    for that known child to be reaped, with no further signals and no escalation. The launcher may therefore stay
    alive beyond its stage deadline; that attempt is UNKNOWN, never PASS;
  * a lost child (wait4 ECHILD) also writes the marker: UNKNOWN, never a known-clean exit;
  * the outcome receipt reports the slot released only for a cleanly reaped child with no marker and no lost child;
  * the v4 'smoke-signal' mode stays in v4, where it ran. v5 has a 'test-exception-path LABEL' mode instead: the
    exception path once, with a short, self-exiting, SIGTERM-ignoring python child and an injected marker-write error.
v4 (unchanged): on_term is flag-only; the wait loop checks the flag first from registration on and forwards SIGTERM
only while the child is owned (unreaped, so its PID is reserved); ownership is cleared by the first statement after
the successful wait4; a signal racing Popen gives a prompt cooperative stop and an UNKNOWN attempt.
v3 (unchanged): attempt 2 owns lane SLOT 2 ONLY, after PhysEpQutrit's B/C411 r7 is fully reaped and end-recorded (no
live lane process of B/C411 r7 in a fresh scan AND evidence/k3cubes/cert_B_r7/B_C411.json exists as a regular file);
a low busy count alone never admits; a signal received before launch prevents the launch. Labels, refusal while any
receipts/*.QUARANTINE.json exists, the wait-start watcher, pins, limits, supervisor arguments and the RSS-cap rule are
as in v2/v3.

Usage: launch_B_v10.py run ITEM --label ITEM-<suffix> [--regen-tag TAG]
       launch_B_v10.py wait-start LABEL
       launch_B_v10.py test-exception-path LABEL         (LABEL: test-...; the v5 test mode, unchanged)
       launch_B_v10.py selftest-v10 LABEL                (LABEL: test-...; helper bounds, census, monitor; no launch)

run waits, with bounded sleeps of 90 s (never spinning), until admission (rules above plus v6's <= 2 busy lane
natives, lane RSS headroom for the projected peak, fixed cap with ancestry headroom and the slot-2 condition). If
nothing is admitted while deadline_ok() holds, nothing is launched and the gate receipt records it. It requires
receipts/regen-ITEM[-TAG].json = MATCH and receipts/selfcheck-summary.json all_ok. It runs the pinned supervise_r3.py
(own session) around 'replay_B_v4.py run ITEM --label LABEL --rss-stop CAP' through run_owned(), and writes an outcome
receipt. wait-start sleeps 60 s at a time until receipts/LABEL.launch.json or LABEL.driver.json exists, or
LABEL.gate.json records 'not_launched', then prints a summary; it never scans the lane.
No SIGKILL, no Popen.kill, no subprocess timeouts.
"""
import datetime
import glob
import json
import os
import re
import signal
import stat
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bklib_v3 as K  # noqa: E402

DEADLINE = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
NO_LAUNCH_AFTER = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
END_BY = datetime.datetime.fromisoformat("2026-10-18T17:57:00-07:00")   # Main: native work ends by 17:57 PDT
SLEEP = 90
SUP_WALL = 10200
SUP_GRACE = 180
CAP_FIXED = 2797076480                          # Main, about 07:05 PDT
FIRST_TO_FINAL = 62                             # v6 rule (c): >= 60 s between the two free readings
HELPER_LIMIT, HELPER_TERM_WAIT = 60, 30         # scan-helper bound, then one SIGTERM and a bounded wait
CENSUS_TRIES, CENSUS_PAUSE = 5, 2
PS_ID = ["/bin/ps", "-axww", "-o", "pid=,ppid=,pgid=,uid=,state=,rss=,lstart=,comm="]
PS_ARGS = ["/bin/ps", "-axww", "-o", "pid=,lstart=,args="]
LSOF_CWD = ["/usr/sbin/lsof", "-a", "-u", str(os.getuid()), "-d", "cwd", "-Fpn"]
LSTART = re.compile(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} "
                    r"\d\d:\d\d:\d\d \d{4}")
DESK_ATTEMPT = re.compile(r"launch_B_v\d+\.py run |replay_B_v\d+\.py (run|regen) |compose_B\w*_v\d+\.py |"
                          r"supervise_r\d+\.py ")
MONITOR = os.path.join(K.REVIEW, "disk-monitor-v1-20261018T0722-to-1810.jsonl")
MON = {"source": "Main 07:32 PDT amendment (long jobs >= 60 min)", "min_free": 13500000000, "window_seconds": 300,
       "min_samples": 25, "min_span_seconds": 290, "max_age_seconds": 30, "drop_floor": 300000000,
       "runway_divisor": 12, "tail_bytes": 262144}
ATTEMPT_RULE = ("Main messages 05:00-07:32 PDT 2026-10-18: attempts are UNKNOWN on any stop and never relabelled. "
                "B_C321-a3, B/C411 and B/C311+cuts are NEW attempts in slot 2, one at a time, each launched only on "
                "Main's explicit GO, with a fresh gate: free >= 12.2e9 + projected growth at both scans and again "
                "immediately before spawn; long-job stability per Main's 07:32 amendment (parent monitor: last free "
                ">= 13.5e9 B, max 5-min peak-to-later drop <= max(300 MB, (free_last - 13.5e9)/12)); lane caps "
                "(<= 2 busy lane natives by ancestry, lane RSS <= 8 GiB); RSS cap 2,797,076,480 B with ancestry "
                "headroom; no stacking; floor 12e9 in flight; no new launches after 17:30 PDT; native work ends by "
                "17:57 PDT.")
B411_R7 = re.compile(r"B_C411|k3_direct_B_r\d+\.py C411")
B411_R7_END_RECORD = os.path.join(K.K3DIR, "cert_B_r7", "B_C411.json")
STATE = {"signals": [], "seen_live": False}
POLL = 0.25
STOP_WAIT = SUP_GRACE + 120


def deadline_ok():
    t = datetime.datetime.now().astimezone()
    return (t < DEADLINE and t < NO_LAUNCH_AFTER
            and t + datetime.timedelta(seconds=SUP_WALL + SUP_GRACE) <= END_BY)


def on_term(signum, frame):
    """Flag only; never signals any PID. run_owned() forwards while it owns an unreaped child."""
    STATE["signals"].append({"signal": signal.Signals(signum).name, "at": K.now()})


def reap_step(p, box, ev, t0, flags):
    """One wait4 on the owned child. Ownership (box['owned']) is cleared by the first statement after a successful
    wait4, or on ECHILD (lost child: never signalled again, and recorded so that the caller quarantines)."""
    try:
        pid, st, ru = os.wait4(box["owned"], flags)
    except ChildProcessError as e:
        box["owned"] = None
        ev["lost_child"] = repr(e)
        return
    if pid:
        box["owned"] = None
        p.returncode = os.waitstatus_to_exitcode(st)
        ev["reaped"] = {"at": K.now(), "rc": p.returncode, "maxrss_bytes": ru.ru_maxrss,
                        "user_seconds": round(ru.ru_utime, 3), "after_spawn_seconds": round(time.monotonic() - t0, 3)}


def write_marker(path, ev, reason):
    """Best-effort desk-owned quarantine/UNKNOWN marker; a failure is recorded and never raised."""
    ev["marker"] = path
    try:
        with open(path, "x") as f:
            json.dump({"at": K.now(), "pid": ev.get("pid"), "argv0": ev.get("argv0"), "reason": reason,
                       "lost_child": ev.get("lost_child"), "exception": ev.get("exception"),
                       "rule": ("UNKNOWN; no further signals or escalation; the launcher keeps waiting for this known "
                                "child; every later admission is refused while this record exists")}, f, indent=2)
            f.write("\n")
    except BaseException as e:
        ev["marker_error"] = repr(e)


def run_owned(argv, out_fd, marker_path, inject=None, stop_wait=STOP_WAIT):
    """Spawn one child in its own session and own it; never return or raise while it is owned and unreaped."""
    ev = {"argv0": argv[0], "pid": None, "spawned_at": None, "forwarded": [], "reaped": None, "exception": None,
          "lost_child": None, "stop_wait": None, "marker": None, "marker_error": None, "wait_errors": [],
          "blocking_wait": None}
    t0 = time.monotonic()
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=out_fd, stderr=subprocess.STDOUT, cwd=K.TMP,
                         env=K.ENV, start_new_session=True)
    box = {"owned": p.pid}                          # registration: the statement right after Popen
    try:
        try:
            ev["pid"] = box["owned"]
            ev["spawned_at"] = K.now()
            if inject is not None:
                inject()                            # tests only
            iteration = 0
            while box["owned"] is not None:
                iteration += 1
                if STATE["signals"] and not ev["forwarded"]:
                    os.kill(box["owned"], signal.SIGTERM)       # owned => unreaped => PID reserved
                    ev["forwarded"].append({"at": K.now(), "after_spawn_seconds": round(time.monotonic() - t0, 3),
                                            "iteration": iteration, "signals_seen": len(STATE["signals"])})
                reap_step(p, box, ev, t0, os.WNOHANG)
                if box["owned"] is not None:
                    time.sleep(POLL)
        except BaseException as exc:
            ev["exception"] = repr(exc)
            if box["owned"] is not None:
                try:
                    os.kill(box["owned"], signal.SIGTERM)
                    ev["forwarded"].append({"at": K.now(), "why": "exception after Popen"})
                except BaseException as e:
                    ev["forwarded"].append({"why": "exception after Popen", "error": repr(e)})
                deadline = time.monotonic() + stop_wait
                while box["owned"] is not None and time.monotonic() < deadline:
                    try:
                        reap_step(p, box, ev, t0, os.WNOHANG)
                    except BaseException as e:
                        ev["wait_errors"].append(repr(e))
                    if box["owned"] is not None:
                        time.sleep(POLL)
                ev["stop_wait"] = {"bounded_seconds": stop_wait, "unreaped_after_wait": box["owned"] is not None}
    finally:
        if box["owned"] is not None:
            write_marker(marker_path, ev, "child unreaped after the bounded SIGTERM wait")
            try:
                ev["blocking_wait"] = {"started_at": K.now(), "after_spawn_seconds": round(time.monotonic() - t0, 3)}
            except BaseException as e:
                ev["wait_errors"].append(repr(e))
        while box["owned"] is not None:             # no further signals or escalation; wait for the known child
            try:
                reap_step(p, box, ev, t0, 0)
            except BaseException as e:
                ev["wait_errors"].append(repr(e))
                time.sleep(POLL)
        if ev["lost_child"] and ev["marker"] is None:
            write_marker(marker_path, ev, "lost child: wait4 ECHILD; exit status unknown")
        ev["owned_at_return"] = box["owned"]
        ev["returned_after_spawn_seconds"] = round(time.monotonic() - t0, 3)
    return ev


def cwd_in_lane(cwd):
    return cwd == K.LANE or cwd.startswith(K.LANE + "/") or cwd.startswith(os.path.join(K.REVIEW, "moqls7-"))


def in_desk(cwd):
    return cwd is not None and (cwd == K.DESK or cwd.startswith(K.DESK + "/"))


def _pump(stream, sink):
    for chunk in iter(lambda: stream.read(1 << 16), b""):
        sink.append(chunk)


def helper_reap(p, box, ev, flags):
    """One waitpid on the owned helper. Ownership ends with the first statement after a successful wait, or on ECHILD
    (lost child: recorded, and the helper result is then not ok)."""
    try:
        pid, st = os.waitpid(box["owned"], flags)
    except ChildProcessError as e:
        box["owned"] = None
        ev["lost_child"] = repr(e)
        return
    if pid:
        box["owned"] = None
        p.returncode = ev["rc"] = os.waitstatus_to_exitcode(st)


def run_helper(argv, limit=HELPER_LIMIT, term_wait=HELPER_TERM_WAIT):
    """Bounded, owned scan helper (ps, lsof), started in its own session: pgid = sid = helper pid, never in this
    launcher's group or in any supervised group. stdout and stderr are drained by reader threads. Past `limit` s, or on
    an exception after Popen, exactly one SIGTERM goes to the owned, unreaped child (its PID is reserved), then a
    bounded wait of `term_wait` s; if the child is still unreaped, a blocking wait with no further signal. Never
    SIGKILL, never a subprocess timeout. ok only for rc 0, empty stderr, no SIGTERM, no exception, no lost child, no
    wait error and both readers finished."""
    t0 = time.monotonic()
    ev = {"argv": argv, "pid": None, "pgid": None, "sid": None, "rc": None, "term_sent_after": None,
          "unreaped_after_term_wait": False, "blocking_wait": False, "exception": None, "lost_child": None,
          "wait_errors": [], "readers_finished": None, "stdout": "", "stderr": "", "seconds": None, "ok": False}
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=K.TMP, env=K.ENV, start_new_session=True)
    box = {"owned": p.pid}                          # registration: the statement right after Popen
    out, err, readers = [], [], []
    try:
        try:
            ev["pid"] = box["owned"]
            for stream, sink in ((p.stdout, out), (p.stderr, err)):
                readers.append(threading.Thread(target=_pump, args=(stream, sink), daemon=True))
                readers[-1].start()
            try:
                ev["pgid"], ev["sid"] = os.getpgid(ev["pid"]), os.getsid(ev["pid"])
            except OSError as e:                    # the helper may already have exited (still unreaped)
                ev["pgid"] = ev["sid"] = repr(e)
            while box["owned"] is not None:
                helper_reap(p, box, ev, os.WNOHANG)
                if box["owned"] is None:
                    break
                elapsed = time.monotonic() - t0
                if ev["term_sent_after"] is None and elapsed >= limit:
                    os.kill(box["owned"], signal.SIGTERM)       # owned => unreaped => PID reserved
                    ev["term_sent_after"] = round(elapsed, 3)
                elif ev["term_sent_after"] is not None and elapsed >= limit + term_wait:
                    ev["unreaped_after_term_wait"] = True
                    break
                time.sleep(0.02)
        except BaseException as exc:
            ev["exception"] = repr(exc)
            if box["owned"] is not None and ev["term_sent_after"] is None:
                try:
                    os.kill(box["owned"], signal.SIGTERM)
                    ev["term_sent_after"] = round(time.monotonic() - t0, 3)
                except BaseException as e:
                    ev["wait_errors"].append(repr(e))
            end = time.monotonic() + term_wait
            while box["owned"] is not None and time.monotonic() < end:
                try:
                    helper_reap(p, box, ev, os.WNOHANG)
                except BaseException as e:
                    ev["wait_errors"].append(repr(e))
                if box["owned"] is not None:
                    time.sleep(0.02)
            ev["unreaped_after_term_wait"] = box["owned"] is not None
    finally:
        while box["owned"] is not None:             # no further signals: wait for the known child to exit
            ev["blocking_wait"] = True
            try:
                helper_reap(p, box, ev, 0)
            except BaseException as e:
                ev["wait_errors"].append(repr(e))
                time.sleep(0.25)
    for t in readers:
        t.join(10)
    ev["readers_finished"] = len(readers) == 2 and not any(t.is_alive() for t in readers)
    if ev["readers_finished"]:
        p.stdout.close()
        p.stderr.close()
    ev["stdout"] = b"".join(out).decode("utf-8", "replace")
    ev["stderr"] = b"".join(err).decode("utf-8", "replace")
    ev["seconds"] = round(time.monotonic() - t0, 3)
    ev["ok"] = (ev["rc"] == 0 and ev["term_sent_after"] is None and ev["exception"] is None
                and ev["lost_child"] is None and not ev["wait_errors"] and ev["readers_finished"]
                and ev["stderr"] == "")
    return ev


def parse_ps_id(text):
    """Identity snapshot rows 'pid ppid pgid uid state rss lstart(5 fields) comm'. Any malformed row raises."""
    rows = {}
    for line in text.splitlines():
        f = line.split(None, 11)
        if (len(f) != 12 or not all(re.fullmatch(r"-?\d+", x) for x in f[:4] + f[5:6]) or not f[4]
                or not LSTART.fullmatch(" ".join(f[6:11])) or not f[11].strip()):
            raise ValueError("malformed ps identity row: %r" % line[:200])
        pid = int(f[0])
        if pid in rows:
            raise ValueError("duplicate pid %d in one ps snapshot" % pid)
        rows[pid] = {"pid": pid, "ppid": int(f[1]), "pgid": int(f[2]), "uid": int(f[3]), "state": f[4],
                     "rss_bytes": int(f[5]) * 1024, "lstart": " ".join(f[6:11]), "comm": f[11].strip()}
    if not rows:
        raise ValueError("empty ps identity snapshot")
    return rows


def parse_ps_args(text):
    """Args snapshot rows 'pid lstart(5 fields) args' (args may be empty). Any malformed row raises."""
    rows = {}
    for line in text.splitlines():
        f = line.split(None, 6)
        if len(f) < 6 or not f[0].isdigit() or not LSTART.fullmatch(" ".join(f[1:6])):
            raise ValueError("malformed ps args row: %r" % line[:200])
        pid = int(f[0])
        if pid in rows:
            raise ValueError("duplicate pid %d in the args snapshot" % pid)
        rows[pid] = {"lstart": " ".join(f[1:6]), "args": f[6].strip() if len(f) == 7 else ""}
    if not rows:
        raise ValueError("empty ps args snapshot")
    return rows


def parse_lsof(text):
    """lsof -Fpn cwd records: 'p<pid>', 'f<fd>' and one non-empty 'n<path>' per process. Anything else raises."""
    cwd, cur = {}, None
    for line in text.splitlines():
        tag, val = line[:1], line[1:]
        if tag == "p" and val.isdigit() and int(val) not in cwd:
            cur = int(val)
            cwd[cur] = None
        elif tag == "f" and cur is not None:
            continue
        elif tag == "n" and cur is not None and cwd[cur] is None and val:
            cwd[cur] = val
        else:
            raise ValueError("malformed lsof record: %r" % line[:200])
    if not cwd:
        raise ValueError("empty lsof cwd listing")
    return cwd


def census_once(own_root):
    """One census: ps identity, ps args, lsof cwd, ps identity again (v10 (1)-(2)). The second identity snapshot is
    classified; the join is by (pid, lstart) and re-validated against the first snapshot. Returns a scan, a scan with
    'error' (fail-closed) or a scan with 'retry' (unresolved own-uid identities)."""
    at, helpers, outs = K.now(), {}, {}
    for name, argv in (("ps_id_1", PS_ID), ("ps_args", PS_ARGS), ("lsof_cwd", LSOF_CWD), ("ps_id_2", PS_ID)):
        try:
            ev = run_helper(argv)
        except Exception as e:                      # Popen failed: nothing was spawned
            return {"at": at, "error": "helper %s not started: %r" % (name, e), "helpers": helpers}
        outs[name] = ev["stdout"]
        helpers[name] = {k: ev[k] for k in ("pid", "pgid", "sid", "rc", "seconds", "term_sent_after", "exception",
                                            "lost_child", "readers_finished", "ok")}
        helpers[name].update(stderr=ev["stderr"][:500], stdout_bytes=len(ev["stdout"]))
        if not ev["ok"]:
            return {"at": at, "error": "helper %s failed (fail-closed)" % name, "helpers": helpers}
    try:
        A, B = parse_ps_id(outs["ps_id_1"]), parse_ps_args(outs["ps_args"])
        L, C = parse_lsof(outs["lsof_cwd"]), parse_ps_id(outs["ps_id_2"])
    except ValueError as e:
        return {"at": at, "error": "malformed enumeration (fail-closed): %s" % e, "helpers": helpers}
    me, children = os.getuid(), {}
    for c in C.values():
        children.setdefault(c["ppid"], []).append(c["pid"])

    def descendants(roots):
        out, stack = set(), list(roots)
        while stack:
            for ch in children.get(stack.pop(), []):
                if ch not in out:
                    out.add(ch)
                    stack.append(ch)
        return out

    own = {own_root} | descendants([own_root])
    ancestors, x = set(), C.get(own_root)
    while x is not None and x["ppid"] in C and x["ppid"] not in ancestors and x["ppid"] != x["pid"]:
        ancestors.add(x["ppid"])
        x = C[x["ppid"]]
    procs, unresolved, foreign_native = {}, [], []
    for pid, c in C.items():
        a, b = A.get(pid), B.get(pid)
        same = a is None or all(a[k] == c[k] for k in ("ppid", "pgid", "uid", "lstart", "comm"))
        p = dict(c, args=b["args"] if b is not None and b["lstart"] == c["lstart"] else None,
                 cwd=L.get(pid) if c["uid"] == me else None, zombie=c["state"].startswith("Z"))
        procs[pid] = p
        if pid in own or p["zombie"]:
            continue
        if c["uid"] == me and (not same or not p["args"] or p["cwd"] is None):
            unresolved.append({"pid": pid, "comm": c["comm"][-80:], "same_in_both_snapshots": same,
                               "args_resolved": bool(p["args"]), "cwd_resolved": p["cwd"] is not None})
        elif c["uid"] != me and os.path.basename(c["comm"]) in K.NATIVE:
            foreign_native.append({"pid": pid, "uid": c["uid"], "comm": c["comm"]})
    counts = {"first": len(A), "args": len(B), "lsof": len(L), "second": len(C)}
    if foreign_native:
        return {"at": at, "error": "live native(s) of another uid, identity unresolvable (fail-closed)",
                "foreign_uid_natives": foreign_native, "helpers": helpers, "census_counts": counts}
    if unresolved:
        return {"at": at, "retry": True, "unresolved": unresolved[:50], "helpers": helpers, "census_counts": counts}
    roots = {pid for pid, p in procs.items() if pid not in own and not p["zombie"] and p["cwd"] is not None
             and cwd_in_lane(p["cwd"])}
    ids = (roots | descendants(roots)) - own
    live = [procs[i] for i in sorted(ids) if not procs[i]["zombie"]]
    zombies = [procs[i] for i in sorted(ids) if procs[i]["zombie"]]
    natives = [p for p in live if os.path.basename(p["comm"]) in K.NATIVE]
    covered, supervised = set(), []
    for p in live:
        m = K.CAP_ARG.search(p["args"] or "")
        if "supervise_r" in (p["args"] or "") and m:
            desc = descendants([p["pid"]])
            groups = {procs[d]["pgid"] for d in desc}
            cov = ({p["pid"]} | desc | {q["pid"] for q in procs.values() if q["pgid"] in groups}) - own
            covered |= cov
            supervised.append({"supervisor_pid": p["pid"], "rss_cap": int(m.group(1)), "covered_pids": sorted(cov)})
    groups = {}
    for p in natives:
        if p["pid"] not in covered:
            groups.setdefault(p["pgid"], set()).add(p["pid"])
    unsup = []
    for pgid in groups:
        members = {q["pid"] for q in live if q["pgid"] == pgid}
        covered |= members
        cur_rss = sum(procs[q]["rss_bytes"] for q in members)
        unsup.append({"pgid": pgid, "pids": sorted(members), "rss_now": cur_rss,
                      "reserve": max(K.UNSUPERVISED_GROUP_RESERVE, cur_rss)})
    others_rss = sum(p["rss_bytes"] for p in live if p["pid"] not in covered)
    reserved = (sum(s["rss_cap"] for s in supervised) + sum(u["reserve"] for u in unsup) + others_rss
                + K.OTHER_LANE_MARGIN)
    headroom = min(K.CAP_MAX, K.LANE_RSS_LIMIT - reserved - K.SAFETY_MARGIN)
    skip = own | ancestors
    b411 = [p for p in procs.values() if p["pid"] not in skip and not in_desk(p["cwd"])
            and B411_R7.search(p["args"] if p["args"] is not None else p["comm"])]
    desk = [p for p in procs.values() if p["pid"] not in skip and not p["zombie"] and in_desk(p["cwd"])
            and (os.path.basename(p["comm"]) in K.NATIVE or DESK_ATTEMPT.search(p["args"] or ""))]
    foreign = [p for p in procs.values() if p["pid"] not in ids and p["pid"] not in own
               and any(m in (p["args"] or "") or m in (p["cwd"] or "") for m in K.LANE_MARKERS)]

    def brief(p, n):
        return dict({k: p[k] for k in ("pid", "ppid", "pgid", "uid", "state", "rss_bytes", "lstart", "comm", "cwd")},
                    args=(p["args"] or "")[:n])

    return {"at": at, "identity": "cwd/ancestry over a validated census (v10)", "helpers": helpers,
            "census_counts": counts, "own_excluded": sorted(own), "own_ancestors": sorted(ancestors),
            "lane_natives": [brief(p, 300) for p in natives], "lane_native_busy": len(natives),
            "lane_processes": [brief(p, 200) for p in live], "lane_zombies": [brief(p, 200) for p in zombies],
            "lane_rss_bytes": sum(p["rss_bytes"] for p in live), "supervised": supervised,
            "unsupervised_native_groups": unsup, "other_lane_rss_bytes": others_rss, "reserved_bytes": reserved,
            "computable_cap_by_ancestry": headroom,
            "computable_cap": CAP_FIXED if headroom >= CAP_FIXED else headroom,
            "b411_matches": [brief(p, 300) for p in b411], "desk_attempt_processes": [brief(p, 300) for p in desk],
            "foreign_marker_matches_excluded": [brief(p, 160) for p in foreign]}


def census(own_root):
    """Validated census with retries: a helper failure, malformed output or an unresolved own-uid identity is retried
    (at most CENSUS_TRIES, CENSUS_PAUSE s apart); after that the scan carries 'error' and is refused (fail-closed)."""
    tries = []
    for i in range(CENSUS_TRIES):
        r = census_once(own_root)
        kind = "error" if "error" in r else ("unresolved" if "retry" in r else "complete")
        tries.append({"at": r["at"], "result": kind, "detail": r.get("error") or r.get("unresolved", [])[:10] or None})
        if kind == "complete":
            r["census_tries"] = tries
            return r
        if STATE["signals"] or i == CENSUS_TRIES - 1:
            break
        time.sleep(CENSUS_PAUSE)
    last = {k: v for k, v in r.items() if k != "retry"}
    last["error"] = "no complete census after %d tries (fail-closed): %s" % (
        len(tries), r.get("error") or "unresolved live identities")
    last["census_tries"] = tries
    return last


def slot_condition(scan):
    """Main's corrected rule: slot 2 is free only when B/C411 r7 is fully reaped AND end-recorded. v10: the matches come
    from the census over the full argv of every process, zombies included (census_once)."""
    live = "error" in scan or bool(scan.get("b411_matches"))
    STATE["seen_live"] = STATE["seen_live"] or (live and "error" not in scan)
    st = os.lstat(B411_R7_END_RECORD) if os.path.lexists(B411_R7_END_RECORD) else None
    recorded = st is not None and (st.st_mode & 0o170000) == 0o100000
    return {"b411_r7_live": live, "b411_r7_seen_live": STATE["seen_live"], "end_record": B411_R7_END_RECORD,
            "end_record_exists": recorded, "ok": (not live) and recorded}


def admission_v10(scan, fb):
    adm = K.admission(scan, fb, deadline_ok())
    slot = slot_condition(scan)
    if "conditions" not in adm:
        return {"ok": False, "why": adm["why"], "slot": slot}
    cond = dict(adm["conditions"], slot2_b411_r7_reaped_and_end_recorded=slot["ok"],
                ancestry_headroom_for_fixed_cap=scan["computable_cap_by_ancestry"] >= CAP_FIXED,
                desk_idle_no_other_attempt_process=not scan["desk_attempt_processes"])
    return {"ok": all(cond.values()), "conditions": cond, "why": [k for k, v in cond.items() if not v], "slot": slot}


def log_line(logfd, purpose, scan, fb, adm, reading):
    line = {"at": scan.get("at"), "purpose": purpose, "reading": reading, "ok": adm["ok"], "why": adm["why"],
            "free_bytes": fb, "busy": scan.get("lane_native_busy"),
            "natives": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("lane_natives", [])],
            "lane_rss": scan.get("lane_rss_bytes"), "reserved": scan.get("reserved_bytes"),
            "headroom": scan.get("computable_cap_by_ancestry"), "cap": scan.get("computable_cap"),
            "foreign_excluded": len(scan.get("foreign_marker_matches_excluded", [])),
            "b411_r7_live": adm["slot"]["b411_r7_live"], "b411_r7_end_record_exists": adm["slot"]["end_record_exists"],
            "b411_matches": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("b411_matches", [])],
            "desk_attempts": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("desk_attempt_processes", [])],
            "lane_zombies": len(scan.get("lane_zombies", [])), "census_tries": len(scan.get("census_tries", [])),
            "error": scan.get("error")}
    os.write(logfd, (json.dumps(line) + "\n").encode())


def monitor_stability():
    """Main's 07:32 PDT amendment (long jobs), evaluated on the parent monitor; fail-closed on any doubt (v10 (6))."""
    out = {"rule": MON, "monitor": MONITOR, "ok": False, "why": None}
    if not deadline_ok():
        out["why"] = "deadline"
        return out
    try:
        st = os.lstat(MONITOR)
        if not stat.S_ISREG(st.st_mode):
            raise ValueError("not a regular file")
        start = max(0, st.st_size - MON["tail_bytes"])
        with open(MONITOR, "rb") as f:
            f.seek(start)
            data = f.read(MON["tail_bytes"])
    except (OSError, ValueError) as e:
        out["why"] = "monitor unreadable: %r" % e
        return out
    lines = data.split(b"\n")
    out["unfinished_tail_bytes"] = len(lines.pop())  # an unfinished last line is ignored
    if start > 0 and lines:
        lines.pop(0)                                  # partial first line of the tail read
    samples, malformed, ends = [], [], []
    for i, raw in enumerate(lines):
        try:
            d = json.loads(raw)
            if not isinstance(d, dict):
                raise ValueError("not a JSON object")
            if "event" in d:
                if d["event"] in ("end", "ended", "stop", "stopped", "exit", "finished"):
                    ends.append(i)
                continue
            t, fr = datetime.datetime.fromisoformat(d["t"]), d["free"]
            if t.utcoffset() is None or isinstance(fr, bool) or not isinstance(fr, int) or fr < 0:
                raise ValueError("bad sample")
            samples.append((i, t, fr))
        except (ValueError, KeyError, TypeError):
            malformed.append(i)
    if not samples:
        out["why"] = "no samples"
        return out
    now = datetime.datetime.now().astimezone()
    t_last, f_last = samples[-1][1], samples[-1][2]
    window = [s for s in samples if t_last - datetime.timedelta(seconds=MON["window_seconds"]) <= s[1] <= t_last]
    peak, max_drop = None, 0
    for _, _, fr in window:
        peak = fr if peak is None or fr > peak else peak
        max_drop = max(max_drop, peak - fr)
    limit = max(MON["drop_floor"], (f_last - MON["min_free"]) / MON["runway_divisor"])
    age = (now - t_last).total_seconds()
    span = (t_last - window[0][1]).total_seconds()
    checks = {"strictly_increasing_timestamps": all(samples[k][1] < samples[k + 1][1] for k in range(len(samples) - 1)),
              "age_0_to_30_s": 0 <= age <= MON["max_age_seconds"],
              "window_samples_at_least_25": len(window) >= MON["min_samples"],
              "window_span_at_least_290_s": span >= MON["min_span_seconds"],
              "no_malformed_line_in_window": not [i for i in malformed if i > window[0][0]],
              "no_end_event_in_window": not [i for i in ends if i > window[0][0]],
              "last_free_at_least_13_5e9": f_last >= MON["min_free"],
              "max_drop_within_limit": max_drop <= limit}
    out.update(checks=checks, samples_read=len(samples), malformed_lines=len(malformed), t_last=t_last.isoformat(),
               age_seconds=round(age, 1), window_samples=len(window), span_seconds=span, free_last=f_last,
               max_drop=max_drop, limit=limit)
    ok = all(checks.values())
    out["why"] = None if ok else [k for k, v in checks.items() if not v]
    out["ok"] = ok and deadline_ok()                 # the deadline is checked again before success
    if ok and not out["ok"]:
        out["why"] = "deadline"
    return out


def pause(seconds):
    """Bounded sleeps (never spinning); False if a launcher signal or the deadline interrupts the pause."""
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        if STATE["signals"] or not deadline_ok():
            return False
        time.sleep(min(2.0, max(0.01, end - time.monotonic())))
    return not STATE["signals"] and deadline_ok()


def prepare(item, label, argv, cap, previous, regen_path, regen_sha0, summary_path, record, quarantine):
    """The gate receipt without its admission evidence, computed before the final census (v10 (3)). ok only if the
    supervisor equals its pin and the regeneration precheck receipt is unchanged since the launcher started."""
    sup_sha = K.sha_file(K.SUPERVISOR)
    regen_sha = K.sha_file(regen_path)
    me = os.path.abspath(__file__)
    rec = {"purpose": "run " + label, "item": item, "label": label, "previous_attempt": previous,
           "launcher_pid": os.getpid(), "launcher": {"path": me, "sha256": K.sha_file(me)}, "prepared_at": K.now(),
           "attempt_rule": ATTEMPT_RULE,
           "rss_cap": {"value": cap, "rule": "fixed by Main (about 07:05 PDT); ancestry headroom must be >= it",
                       "CAP_FIXED": CAP_FIXED, "CAP_MAX": K.CAP_MAX, "LANE_RSS_LIMIT": K.LANE_RSS_LIMIT,
                       "SAFETY_MARGIN": K.SAFETY_MARGIN, "MIN_CAP": K.MIN_CAP, "PROJECTED_PEAK": K.PROJECTED_PEAK,
                       "UNSUPERVISED_GROUP_RESERVE": K.UNSUPERVISED_GROUP_RESERVE,
                       "OTHER_LANE_MARGIN": K.OTHER_LANE_MARGIN},
           "supervisor": {"path": K.SUPERVISOR, "sha256": sup_sha, "pin": K.SUPERVISOR_SHA256,
                          "equals_pin": sup_sha == K.SUPERVISOR_SHA256, "wall": SUP_WALL, "grace": SUP_GRACE,
                          "floor": K.FLOOR, "record": record, "quarantine": quarantine},
           "argv": argv, "cwd": K.TMP, "env": K.ENV, "scripts_sha256": K.script_hashes(),
           "regen_receipt": os.path.relpath(regen_path, K.DESK), "regen_receipt_sha256": regen_sha,
           "regen_receipt_unchanged_since_start": regen_sha == regen_sha0,
           "selfcheck_summary_sha256": K.sha_file(summary_path),
           "rules": {"gate": K.GATE, "floor": K.FLOOR, "monitor_stability": MON,
                     "no_launch_after": NO_LAUNCH_AFTER.isoformat(), "end_by": END_BY.isoformat(),
                     "first_to_final_min_seconds": FIRST_TO_FINAL, "helper_limit_seconds": HELPER_LIMIT,
                     "helper_term_wait_seconds": HELPER_TERM_WAIT, "census_tries": CENSUS_TRIES}}
    return rec, sup_sha == K.SUPERVISOR_SHA256 and regen_sha == regen_sha0


def mode_run(item, label, regen_tag=None):
    regen_path = os.path.join(K.RECEIPTS, "regen-%s%s.json" % (item, "-" + regen_tag if regen_tag else ""))
    summary_path = os.path.join(K.RECEIPTS, "selfcheck-summary.json")
    with open(regen_path) as f:
        regen = json.load(f)
    with open(summary_path) as f:
        summary = json.load(f)
    if regen.get("result") != "MATCH" or summary.get("all_ok") is not True:
        raise SystemExit("prerequisites not met: regen %r, selfcheck all_ok %r" % (regen.get("result"),
                                                                                  summary.get("all_ok")))
    held = sorted(glob.glob(os.path.join(K.RECEIPTS, "*.QUARANTINE.json")))
    if held:
        raise SystemExit("quarantine record(s) present, admission refused: %s" % held)
    gate_path = os.path.join(K.RECEIPTS, label + ".gate.json")
    outcome_path = os.path.join(K.RECEIPTS, label + ".launch-outcome.json")
    record = os.path.join(K.RECEIPTS, label + ".supervisor.json")
    quarantine = os.path.join(K.RECEIPTS, label + ".QUARANTINE.json")
    stdout_log = os.path.join(K.LOGS, label + ".supervisor-stdout.log")
    launcher_marker = os.path.join(K.RECEIPTS, label + ".launcher.QUARANTINE.json")
    for pth in (gate_path, outcome_path, record, quarantine, stdout_log, launcher_marker):
        if os.path.lexists(pth):
            raise SystemExit("exists: " + pth)
    prev_path = os.path.join(K.RECEIPTS, item + ".json")
    prev = json.loads(K.read_regular(prev_path)) if os.path.isfile(prev_path) else {}
    previous = {"label": item, "item_receipt": "receipts/%s.json" % item,
                "sha256": K.sha_file(prev_path) if os.path.isfile(prev_path) else None,
                "status": prev.get("status"), "stop_reason": (prev.get("stop") or {}).get("reason")}
    regen_sha0 = K.sha_file(regen_path)
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-run-%s.log" % label))
    out_fd = K.open_append_x(stdout_log)            # v10 (3): output file prepared before any admission census
    cap = CAP_FIXED
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", label + "-parent-replay", "--wall", str(SUP_WALL),
            "--rss-cap", str(cap), "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", record,
            "--quarantine", quarantine, "--grace", str(SUP_GRACE), "--",
            K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v4.py"), "run", item, "--label", label,
            "--rss-stop", str(cap)]
    while True:
        scan = census(os.getpid())
        fb = K.free_bytes()
        adm = admission_v10(scan, fb)
        log_line(logfd, "run " + label, scan, fb, adm, 1)
        last = {"scan": scan, "free_bytes": fb, "admission": adm}
        if adm["ok"] and not STATE["signals"]:
            t1 = time.monotonic()
            paused = pause(FIRST_TO_FINAL)
            rec, prepared_ok = prepare(item, label, argv, cap, previous, regen_path, regen_sha0, summary_path,
                                       record, quarantine)
            stab = monitor_stability()
            os.write(logfd, (json.dumps({"at": K.now(), "paused_ok": paused, "prepared_ok": prepared_ok,
                                         "stability": {k: stab.get(k) for k in (
                                             "ok", "why", "age_seconds", "window_samples", "free_last", "max_drop",
                                             "limit")}}) + "\n").encode())
            scan2 = census(os.getpid())                 # the final census
            fb2 = K.free_bytes()
            adm2 = admission_v10(scan2, fb2)
            gap = round(time.monotonic() - t1, 1)
            extra = [w for w, bad in (("pause interrupted", not paused),
                                      ("supervisor pin or regen receipt changed", not prepared_ok),
                                      ("monitor stability", not stab["ok"]), ("gap below 60 s", gap < 60),
                                      ("a free reading below the gate", fb < K.GATE or fb2 < K.GATE)) if bad]
            pre = None
            if adm2["ok"] and not extra:                # immediate pre-spawn rechecks (microseconds)
                pre = {"free_bytes": K.free_bytes(), "deadline_ok": deadline_ok(),
                       "launcher_signals": len(STATE["signals"]),
                       "quarantine_records": sorted(glob.glob(os.path.join(K.RECEIPTS, "*.QUARANTINE.json")))}
                pre["ok"] = (pre["free_bytes"] >= K.GATE and pre["deadline_ok"] and not pre["launcher_signals"]
                             and not pre["quarantine_records"])
                if not pre["ok"]:
                    extra.append("pre-spawn recheck")
            adm2.update(first=adm, stability=stab, paused_ok=paused, prepared_ok=prepared_ok, prespawn_recheck=pre,
                        two_readings={"first": {"at": scan["at"], "free_bytes": fb},
                                      "second": {"at": scan2["at"], "free_bytes": fb2}, "gap_seconds": gap,
                                      "gate": K.GATE, "both_at_least_gate": fb >= K.GATE and fb2 >= K.GATE})
            adm2["ok"] = adm2["ok"] and not extra
            adm2["why"] = adm2["why"] + extra
            if adm2["ok"]:
                break
            log_line(logfd, "run " + label, scan2, fb2, adm2, 2)
            last = {"scan": scan2, "free_bytes": fb2, "admission": adm2}
        if not deadline_ok() or STATE["signals"]:
            rec, _ = prepare(item, label, argv, cap, previous, regen_path, regen_sha0, summary_path, record,
                             quarantine)
            rec.update(last, at=K.now(), not_launched="not admitted while deadline_ok() held, or launcher signals: "
                       "%s / signals %s" % (last["admission"]["why"], STATE["signals"]))
            print(json.dumps({"gate_sha256": K.write_json_x(gate_path, rec), "launched": False,
                              "why": rec["not_launched"]}), flush=True)
            os.close(out_fd)
            os.close(logfd)
            return 2
        time.sleep(SLEEP)
    rec["rss_cap"].update(computable_cap_by_ancestry=scan2.get("computable_cap_by_ancestry"),
                          reserved=scan2.get("reserved_bytes"))
    rec.update(scan=scan2, free_bytes=fb2, admission=adm2)
    box = {"gate_sha": None}

    def after_spawn():
        """run_owned()'s inject hook, right after Popen and registration, inside its ownership scope: the gate receipt
        (prepared before the spawn), the reading-2 log line and the launch print. An exception here takes
        run_owned()'s exception path (SIGTERM to the owned supervisor, bounded wait): UNKNOWN."""
        rec["at"] = K.now()
        rec["gate_receipt_written_after_spawn"] = True
        box["gate_sha"] = K.write_json_x(gate_path, rec)
        log_line(logfd, "run " + label, scan2, fb2, adm2, 2)
        try:
            print(json.dumps({"gate_sha256": box["gate_sha"], "launched": True, "rss_cap": cap, "free_bytes": fb2,
                              "busy": scan2["lane_native_busy"]}), flush=True)
        except OSError as e:
            box["print_error"] = repr(e)

    started = K.now()
    t0 = time.monotonic()
    ev = run_owned(argv, out_fd, launcher_marker, inject=after_spawn)
    os.close(out_fd)
    gate_sha = box["gate_sha"]
    os.write(logfd, (json.dumps({"at": started, "supervisor_pid": ev["pid"], "gate_sha256": gate_sha}) + "\n").encode())
    clean = ev["reaped"] is not None and ev["lost_child"] is None and ev["marker"] is None and ev["owned_at_return"] is None
    outcome = {"item": item, "label": label, "gate_receipt_sha256": gate_sha, "supervisor_started_at": started,
               "supervisor_finished_at": K.now(), "seconds": round(time.monotonic() - t0, 3), "owned_child": ev,
               "supervisor": {"pid": ev["pid"], "rc": (ev["reaped"] or {}).get("rc")},
               "launcher_signals": STATE["signals"],
               "stopped_by_launcher": bool(ev["forwarded"]),
               "launcher_marker_exists": os.path.lexists(launcher_marker),
               "slot_released": clean,
               "unknown_by_launcher": (not clean) or ev["exception"] is not None or bool(ev["forwarded"]),
               "supervisor_record_exists": os.path.exists(record),
               "supervisor_record_sha256": K.sha_file(record) if os.path.exists(record) else None,
               "quarantine_exists": os.path.lexists(quarantine),
               "supervisor_stdout_log_sha256": K.sha_file(stdout_log),
               "free_bytes_end": K.free_bytes()}
    h = K.write_json_x(outcome_path, outcome)
    os.write(logfd, (json.dumps({"at": K.now(), "outcome_sha256": h, "supervisor_rc": outcome["supervisor"]["rc"]})
                     + "\n").encode())
    os.close(logfd)
    print(json.dumps({"outcome_sha256": h, "supervisor_rc": outcome["supervisor"]["rc"], "seconds": outcome["seconds"],
                      "stopped_by_launcher": outcome["stopped_by_launcher"], "slot_released": clean,
                      "launcher_marker_exists": outcome["launcher_marker_exists"],
                      "quarantine_exists": outcome["quarantine_exists"]}), flush=True)
    return 0 if clean and ev["exception"] is None else 3


def read_json_settled(path):
    """Parse one of this desk's own JSON receipts; tolerate a write still in progress (bounded retries)."""
    for _ in range(6):
        try:
            return json.loads(K.read_regular(path))
        except ValueError:
            time.sleep(5)
    return json.loads(K.read_regular(path))


def mode_wait_start(label):
    paths = {k: os.path.join(K.RECEIPTS, label + s) for k, s in
             (("gate", ".gate.json"), ("launch", ".launch.json"), ("driver", ".driver.json"))}
    while True:
        if os.path.lexists(paths["launch"]) or os.path.lexists(paths["driver"]):
            break
        if os.path.lexists(paths["gate"]) and "not_launched" in read_json_settled(paths["gate"]):
            break
        if datetime.datetime.now().astimezone() > NO_LAUNCH_AFTER:
            print(json.dumps({"label": label, "note": "nothing started by 17:00 PDT"}), flush=True)
            return 2
        time.sleep(60)
    out = {"label": label, "observed_at": K.now()}
    for k, p in paths.items():
        if os.path.lexists(p):
            d = read_json_settled(p)
            out[k] = {"path": os.path.relpath(p, K.DESK), "sha256": K.sha_file(p), "at": d.get("at")}
            if k == "gate":
                out[k].update({"not_launched": d.get("not_launched"), "free_bytes": d.get("free_bytes"),
                               "busy": (d.get("scan") or {}).get("lane_native_busy"),
                               "natives": [[n.get("pid"), os.path.basename(n.get("comm", ""))]
                                           for n in (d.get("scan") or {}).get("lane_natives", [])],
                               "rss_cap": (d.get("rss_cap") or {}).get("value"),
                               "slot": (d.get("admission") or {}).get("slot")})
            if k == "launch":
                out[k].update({"cnf_sha256": (d.get("regen") or {}).get("cnf_sha256"),
                               "binaries_at_spawn": {b: v.get("sha256")
                                                     for b, v in (d.get("binaries_at_spawn") or {}).items()},
                               "free_bytes": (d.get("gate_at_launch_receipt") or {}).get("free_bytes")})
    print(json.dumps(out), flush=True)
    return 0


TEST_CHILD_SECONDS = 6
TEST_STOP_WAIT = 2


def mode_test_exception_path(label):
    """The new exception path, once. No solver, checker, CNF or supervisor. The child is a short python sleeper that
    inherits SIGTERM=SIG_IGN from this test process, so it ignores SIGTERM from its first instruction, and exits by
    itself after TEST_CHILD_SECONDS. An exception is injected right after Popen, and the marker path points into a
    missing directory (injected record-write error). Expected: exactly one SIGTERM forwarded to the owned child
    (ignored); the bounded wait (TEST_STOP_WAIT) expires with the child unreaped; the marker write fails and is
    recorded; run_owned() keeps waiting with no further signals and returns only after the child exited by itself and
    was reaped."""
    receipt = os.path.join(K.RECEIPTS, label + ".test.json")
    stdout_path = os.path.join(K.LOGS, label + ".child-stdout.log")
    bad_marker = os.path.join(K.RECEIPTS, "no-such-dir-" + label, label + ".launcher.QUARANTINE.json")
    for pth in (receipt, stdout_path, os.path.dirname(bad_marker)):
        if os.path.lexists(pth):
            raise SystemExit("exists: " + pth)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)   # inherited across exec: the child is SIGTERM-resistant
    argv = [K.PY, "-I", "-B", "-c", "import time; time.sleep(%d)" % TEST_CHILD_SECONDS]
    kills, real_kill, t0 = [], os.kill, time.monotonic()

    def logged_kill(pid, sig):
        kills.append({"pid": pid, "signal": signal.Signals(sig).name, "t": round(time.monotonic() - t0, 4)})
        real_kill(pid, sig)

    def inject():
        raise RuntimeError("injected exception after Popen (test)")

    os.kill = logged_kill
    try:
        out_fd = K.open_append_x(stdout_path)
        ev = run_owned(argv, out_fd, bad_marker, inject=inject, stop_wait=TEST_STOP_WAIT)
        returned_at = round(time.monotonic() - t0, 3)
        os.close(out_fd)
    finally:
        os.kill = real_kill
    sw, bw, rp = ev["stop_wait"] or {}, ev["blocking_wait"] or {}, ev["reaped"] or {}
    checks = {
        "exception_recorded": "injected exception after Popen" in (ev["exception"] or ""),
        "exactly_one_sigterm_to_owned_child": (len(kills) == 1 and kills[0]["pid"] == ev["pid"]
                                               and kills[0]["signal"] == "SIGTERM"),
        "bounded_wait_expired_child_unreaped": (sw.get("bounded_seconds") == TEST_STOP_WAIT
                                                and sw.get("unreaped_after_wait") is True),
        "marker_write_attempted_failed_and_recorded": (ev["marker"] == bad_marker and ev["marker_error"] is not None
                                                       and not os.path.lexists(bad_marker)),
        "blocking_wait_after_bounded_wait": bw.get("after_spawn_seconds", -1) >= TEST_STOP_WAIT,
        "child_exited_by_itself_rc0": rp.get("rc") == 0 and rp.get("after_spawn_seconds", 0) >= TEST_CHILD_SECONDS - 0.5,
        "owner_returned_only_after_reap": (ev["owned_at_return"] is None and rp != {}
                                           and returned_at >= rp["after_spawn_seconds"] >= TEST_CHILD_SECONDS - 0.5),
        "no_lost_child_no_wait_errors": ev["lost_child"] is None and not ev["wait_errors"],
    }
    out = {"label": label, "at": K.now(), "argv": argv, "test_stop_wait_seconds": TEST_STOP_WAIT,
           "child_seconds": TEST_CHILD_SECONDS, "injected_marker_path": bad_marker, "ev": ev, "kills": kills,
           "returned_after_start_seconds": returned_at, "child_stdout_sha256": K.sha_file(stdout_path),
           "checks": checks, "all_ok": all(checks.values()), "scripts_sha256": K.script_hashes()}
    h = K.write_json_x(receipt, out)
    print(json.dumps({"test_receipt_sha256": h, "all_ok": out["all_ok"], "checks": checks,
                      "returned_after_start_seconds": returned_at, "reaped": rp, "marker_error": ev["marker_error"]}),
          flush=True)
    return 0 if out["all_ok"] else 1


def mode_selftest(label):
    """v10 self-test; launches nothing. run_helper() bounds, signals and session isolation with short python children,
    then one census, one informational admission evaluation and one monitor-stability evaluation (read-only)."""
    receipt = os.path.join(K.RECEIPTS, label + ".selftest.json")
    if os.path.lexists(receipt):
        raise SystemExit("exists: " + receipt)
    kills, real_kill, t0 = [], os.kill, time.monotonic()

    def logged_kill(pid, sig):
        kills.append({"pid": pid, "signal": signal.Signals(sig).name, "t": round(time.monotonic() - t0, 3)})
        real_kill(pid, sig)

    sleeper = [K.PY, "-I", "-B", "-c", "import time; time.sleep(30)"]
    ignorer = [K.PY, "-I", "-B", "-c",
               "import signal, time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(8)"]
    os.kill = logged_kill
    try:
        cases = {"ps_ok": run_helper(["/bin/ps", "-o", "pid=", "-p", str(os.getpid())]),
                 "term_honoring": run_helper(sleeper, limit=2, term_wait=5),
                 "term_ignoring": run_helper(ignorer, limit=2, term_wait=2),
                 "nonzero_rc": run_helper(["/bin/ps", "-o", "pid=", "-p", "99999999"]),
                 "stderr_output": run_helper([K.PY, "-I", "-B", "-c", "import sys; sys.stderr.write('warning\\n')"])}
    finally:
        os.kill = real_kill
    own_pgid = os.getpgrp()
    th, ti, ps_ok = cases["term_honoring"], cases["term_ignoring"], cases["ps_ok"]

    def isolated(ev):
        return ev["pgid"] == ev["pid"] and ev["sid"] == ev["pid"] and ev["pgid"] != own_pgid

    checks = {
        "ps_ok_is_ok_rc0_own_pid": (ps_ok["ok"] is True and ps_ok["rc"] == 0
                                    and ps_ok["stdout"].strip() == str(os.getpid())),
        "term_honoring_one_sigterm_at_limit_reaped_in_bounded_wait": (
            th["term_sent_after"] is not None and 2 <= th["term_sent_after"] < 3 and th["rc"] == -signal.SIGTERM
            and not th["unreaped_after_term_wait"] and not th["blocking_wait"] and th["ok"] is False),
        "term_ignoring_one_sigterm_then_blocking_wait_until_self_exit": (
            ti["term_sent_after"] is not None and 2 <= ti["term_sent_after"] < 3 and ti["unreaped_after_term_wait"]
            and ti["blocking_wait"] and ti["rc"] == 0 and ti["seconds"] >= 7.5 and ti["ok"] is False),
        "exactly_two_signals_both_sigterm_to_owned_helpers": (
            len(kills) == 2 and all(k["signal"] == "SIGTERM" for k in kills)
            and [k["pid"] for k in kills] == [th["pid"], ti["pid"]]),
        "timed_helpers_in_own_sessions": isolated(th) and isolated(ti),
        "nonzero_rc_not_ok": cases["nonzero_rc"]["rc"] not in (0, None) and cases["nonzero_rc"]["ok"] is False,
        "stderr_output_not_ok": (cases["stderr_output"]["rc"] == 0 and cases["stderr_output"]["stderr"] != ""
                                 and cases["stderr_output"]["ok"] is False),
        "every_helper_reaped_no_lost_child": all(ev["rc"] is not None and ev["lost_child"] is None
                                                 for ev in cases.values()),
    }
    scan = census(os.getpid())
    fb = K.free_bytes()
    adm = admission_v10(scan, fb)
    stab = monitor_stability()
    checks["census_complete"] = "error" not in scan
    keep = ("pid", "pgid", "sid", "rc", "term_sent_after", "unreaped_after_term_wait", "blocking_wait", "exception",
            "lost_child", "wait_errors", "readers_finished", "seconds", "ok")
    me = os.path.abspath(__file__)
    out = {"label": label, "at": K.now(), "launcher": {"path": me, "sha256": K.sha_file(me)},
           "bklib": {"path": os.path.abspath(K.__file__), "sha256": K.sha_file(os.path.abspath(K.__file__))},
           "own_pid": os.getpid(), "own_pgid": own_pgid, "own_sid": os.getsid(0),
           "cases": {k: dict({x: v[x] for x in keep}, argv=v["argv"], stdout=v["stdout"][:200],
                             stderr=v["stderr"][:200]) for k, v in cases.items()},
           "kills": kills, "census": scan, "free_bytes": fb, "admission_informational": adm,
           "monitor_stability": stab, "checks": checks, "all_ok": all(checks.values()),
           "note": "no launch; census, admission and stability are observations only",
           "scripts_sha256": K.script_hashes()}
    h = K.write_json_x(receipt, out)
    print(json.dumps({"selftest_receipt_sha256": h, "all_ok": out["all_ok"], "checks": checks,
                      "census_error": scan.get("error"), "census_tries": len(scan.get("census_tries", [])),
                      "busy": scan.get("lane_native_busy"),
                      "desk_attempts": [[p["pid"], os.path.basename(p["comm"])]
                                        for p in scan.get("desk_attempt_processes", [])],
                      "b411_matches": [[p["pid"], os.path.basename(p["comm"])] for p in scan.get("b411_matches", [])],
                      "admission_why": adm.get("why"),
                      "stability": {k: stab.get(k) for k in ("ok", "why", "age_seconds", "window_samples", "free_last",
                                                             "max_drop", "limit")}}), flush=True)
    return 0 if out["all_ok"] else 1


def main():
    a = sys.argv[1:]
    if a and a[0] == "run":
        tagged = len(a) == 6 and a[4] == "--regen-tag" and re.fullmatch(r"[A-Za-z0-9]+", a[5])
        if ((len(a) != 4 and not tagged) or a[1] not in K.ITEMS or a[2] != "--label"
                or not (re.fullmatch(r"[A-Za-z0-9_.-]+", a[3]) and a[3].startswith(a[1] + "-"))):
            raise SystemExit("usage: launch_B_v10.py run ITEM --label ITEM-<suffix> [--regen-tag TAG]")
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_run(a[1], a[3], a[5] if tagged else None))
    if a and a[0] == "wait-start" and len(a) == 2 and re.fullmatch(r"[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_wait_start(a[1]))
    if a and a[0] == "test-exception-path" and len(a) == 2 and re.fullmatch(r"test-[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_test_exception_path(a[1]))
    if a and a[0] == "selftest-v10" and len(a) == 2 and re.fullmatch(r"test-[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_selftest(a[1]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
