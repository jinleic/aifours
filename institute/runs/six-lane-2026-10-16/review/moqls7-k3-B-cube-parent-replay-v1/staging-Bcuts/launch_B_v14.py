#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v14.

v14 = launch_B_v12.py (not v13) with one change, specified by Main at about 09:33 PDT. Two persistent own-uid
zombies were identified by Main's read-only lookup as unrelated GUI children: pid 57860 under WeChat.app and pid
59426 under Signal.app. They are exempted from the unresolved-argv veto, and only those two complete identity tuples
(KNOWN_UNRELATED_ZOMBIES) are exempted. A zombie is exempted only if all of these hold:
  * it is in state Z in BOTH bracketing identity snapshots;
  * its pid, ppid, pgid, uid and lstart equal the tuple in both snapshots;
  * its parent is present in both snapshots, live, with the tuple's pid, uid and lstart, and its comm contains the
    tuple's app bundle path;
  * the parent's lsof cwd equals the tuple's cwd and its identity is consistent.
If any field differs, the original fail-closed rule applies (retry, then refuse). There is no general zombie
heuristic. Each census records every compared identity (expected, both snapshots, parent, cwd) under
known_zombie_comparisons; matches are listed under known_zombie_exclusions. Exempted zombies take no part in the
B/C411 veto, the desk attempts or the lane classification. 'selftest-v14' replaces 'selftest-v12' and adds the
match/mismatch cases. The monitor is the same restored path as v12. Everything else is byte-identical to v12.

v12 = launch_B_v11.py with Main's approvals and Codex's v11 MINOR (review/m7-launch-v11-codex-v1.note.md
d7ed4c3a...c61a, GO-WITH-FIXES):
  (a) slots. 'run ITEM --label LABEL --slot {1,2} [--regen-tag TAG]'. A slot holds at most one attempt of this desk;
      the other slot may be busy.
        * Attribution: each desk attempt process (a native, supervise_r*, replay_B_*, compose_[AB]*, or 'launch_B_* run'
          with cwd in this desk) is attributed to a slot by the first launcher in its ancestry. '--slot N' gives N. The
          launchers up to v11 have no --slot, so they use LEGACY_SLOTS: B_C321-a3 (v8) slot 2, B_C411-p1 (v11) slot 1.
          Any other launcher without a slot, or no launcher at all (e.g. a regen precheck), is 'unknown' and blocks
          both slots.
        * Admission requires the target slot to be free of desk attempts and no 'unknown' attribution. This replaces
          v11's desk_idle condition.
        * Admissions run one at a time. An exclusive flock on locks/admission.lock is taken before the final census
          and held through spawn and the gate receipt. It is released 90 s after the spawn (by then the new attempt's
          natives are visible to a later census), at once on refusal, or at process exit.
        * The lane totals are unchanged: <= 2 busy lane natives at launch (so <= 4 after), lane RSS + 2 GiB <= 8 GiB,
          and ancestry headroom >= the fixed 2,797,076,480 B cap (two caps fit);
  (b) the route-A item A_C311cuts. v12 imports bklib_v4 and runs driver replay_B_v5.py; kissat replays the item
      (item deviation). The set runs from scripts-v12/: bklib_v4 takes SCRIPTS from its own directory, so adding the
      set never changes the scripts/ set recorded by the live v11 run B_C411-p1;
  (c) Codex v11 MINOR: the pre-spawn guard compares the UNROUNDED monitor-sample age with 0..30 s; only the recorded
      value is rounded.
The single-admitter invariant, the monitor rules, the census, the helpers, run_owned() and the outcome receipt are
unchanged from v11. 'selftest-v12 LABEL' adds slot-attribution and lock cases.

v11 = launch_B_v10.py with the repairs required by Codex's HOLD on v10 (review/m7-launch-v10-codex-v1.note.md
f8f86f0d...53f8, items 1-4; item 5 is the review packet):
  (1) monitor freshness at the launch boundary. monitor_stability() is evaluated again AFTER the final census, and
      both evaluations must pass. The final pre-spawn guard recomputes the age of that evaluation's last sample
      (0..30 s). Stale, ended or newly disqualifying monitor evidence refuses;
  (2) identity agreement:
        * a process counts as consistent only if it is present in BOTH identity snapshots with equal
          ppid/pgid/uid/lstart/comm and has args with the same lstart. Absence from the first snapshot is no longer
          consistent;
        * an unresolved own-uid live identity (no consistent identity, or no resolved cwd) is retried and then
          refused, as in v10;
        * every other process the B/C411 veto must see (any uid, zombies included; only this launcher, its
          descendants and ancestors, and own-uid processes with cwd in this desk are excluded) must have resolved
          argv. That is a consistent identity with args that are not empty, not '<defunct>' and not a parenthesized
          comm. Otherwise it is retried and then refused. There is no comm fallback;
        * slot/reaping identity is checked separately from RSS eligibility; zombies still count as neither busy nor
          RSS;
  (3) helper output:
        * each reader thread records explicit EOF and any exception, and helper ok requires both streams to have
          reached EOF without an exception;
        * an lsof record is 'p<pid>', then 'fcwd', then one 'n<path>'. A record without 'fcwd' or without an
          absolute path leaves that cwd unresolved; any other tag or order is malformed;
        * ps numerics must be non-negative decimal (pid >= 1). uid is printed signed by ps (nobody = -2); it must
          lie in [-2^31, 2^32) and is normalized modulo 2^32;
  (4) single-admitter invariant (Main, relaying Codex v10 item 4; replaces a shared lock), recorded in every gate
      receipt. Admission also requires that every M7-lane native outside this desk's ancestry belongs to the route-A
      attempt-5 group (C311cuts_A_r9 / k3_cuts_certify_r9.py A, slot 1). Any other foreign lane native refuses.
The census retries rise from 5 to 15 (2 s apart). System daemons and other agents start short-lived processes, and
an unreaped zombie can persist for seconds; both count as unresolved until a later census. run_owned(), on_term, the
outcome receipt, the RSS cap, supervisor arguments,
the driver (replay_B_v4.py) and bklib_v3 are unchanged. 'selftest-v11 LABEL' replaces 'selftest-v10' and adds
parser cases.

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

Usage: launch_B_v14.py run ITEM --label ITEM-<suffix> --slot {1,2} [--regen-tag TAG]
       launch_B_v14.py wait-start LABEL
       launch_B_v14.py test-exception-path LABEL         (LABEL: test-...; the v5 test mode, unchanged)
       launch_B_v14.py selftest-v14 LABEL                (LABEL: test-...; helper bounds, parsers, slots, lock, zombie
                                                          tuples, census, monitor; no launch)

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
import fcntl
import glob
import io
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
import bklib_v4 as K  # noqa: E402

DEADLINE = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
NO_LAUNCH_AFTER = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
END_BY = datetime.datetime.fromisoformat("2026-10-18T17:57:00-07:00")   # Main: native work ends by 17:57 PDT
SLEEP = 90
SUP_WALL = 10200
SUP_GRACE = 180
CAP_FIXED = 2797076480                          # Main, about 07:05 PDT
FIRST_TO_FINAL = 62                             # v6 rule (c): >= 60 s between the two free readings
HELPER_LIMIT, HELPER_TERM_WAIT = 60, 30         # scan-helper bound, then one SIGTERM and a bounded wait
CENSUS_TRIES, CENSUS_PAUSE = 15, 2
PS_ID = ["/bin/ps", "-axww", "-o", "pid=,ppid=,pgid=,uid=,state=,rss=,lstart=,comm="]
PS_ARGS = ["/bin/ps", "-axww", "-o", "pid=,lstart=,args="]
LSOF_CWD = ["/usr/sbin/lsof", "-a", "-u", str(os.getuid()), "-d", "cwd", "-Fpn"]
LSTART = re.compile(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} "
                    r"\d\d:\d\d:\d\d \d{4}")
DESK_ATTEMPT = re.compile(r"launch_B_v\d+\.py run |replay_B_v\d+\.py (run|regen) |compose_[AB]\w*_v\d+\.py |"
                          r"supervise_r\d+\.py ")
LAUNCHER_SLOT = re.compile(r"launch_B_v(\d+)\.py run \S+ --label (\S+)(?: --slot ([12]))?")
LEGACY_SLOTS = {"B_C321-a3": 2, "B_C411-p1": 1}   # pre-v12 launchers (no --slot): a3 (v8) slot 2; B_C411-p1 (v11) slot 1
KNOWN_UNRELATED_ZOMBIES = {   # v14, Main's read-only lookup about 09:33 PDT; exact tuples only, never a pattern
    57860: {"ppid": 43939, "pgid": 43939, "uid": 501, "lstart": "Tue Oct 13 19:50:17 2026",
            "parent": {"lstart": "Sat Oct 10 09:09:21 2026", "app": "/WeChat.app/",
                       "cwd": "/Users/jinleic/Library/Containers/com.tencent.xinWeChat/Data"}},
    59426: {"ppid": 50856, "pgid": 50856, "uid": 501, "lstart": "Sun Oct 18 09:25:51 2026",
            "parent": {"lstart": "Thu Oct 15 21:52:41 2026", "app": "/Signal.app/", "cwd": "/"}},
}
LOCK_PATH = os.path.join(K.DESK, "locks", "admission.lock")
LOCK_SETTLE = 90                                # seconds the admission lock is held after a spawn
MONITOR = os.path.join(K.REVIEW, "disk-monitor-v1-20261018T0722-to-1810.jsonl")
MON = {"source": "Main 07:32 PDT amendment (long jobs >= 60 min)", "min_free": 13500000000, "window_seconds": 300,
       "min_samples": 25, "min_span_seconds": 290, "max_age_seconds": 30, "drop_floor": 300000000,
       "runway_divisor": 12, "tail_bytes": 262144}
ATTEMPT_RULE = ("Main messages 05:00-08:40 PDT 2026-10-18: attempts are UNKNOWN on any stop and never relabelled. "
                "B_C411, B/C311+cuts and A/C311+cuts are NEW attempts of this desk in slots 1 and 2, at most one per "
                "slot, admitted one at a time, each launched only on Main's explicit GO, with a fresh gate: free >= "
                "12.2e9 + projected growth at both censuses and again immediately before spawn; long-job stability "
                "per Main's 07:32 amendment (parent monitor: last free >= 13.5e9 B, max 5-min peak-to-later drop <= "
                "max(300 MB, (free_last - 13.5e9)/12)); lane caps (<= 2 busy lane natives at launch, <= 4 after; lane "
                "RSS <= 8 GiB with reservations); RSS cap 2,797,076,480 B with ancestry headroom; floor 12e9 in "
                "flight; no new launches after 17:30 PDT; native work ends by 17:57 PDT.")
B411_R7 = re.compile(r"B_C411|k3_direct_B_r\d+\.py C411")
ROUTE_A5 = re.compile(r"C311cuts_A_r9(?![0-9A-Za-z])|k3_cuts_certify_r9\.py A(\s|$)")
ADMITTER_INVARIANT = ("Single-admitter invariant (Main, relaying Codex review m7-launch-v10-codex-v1.note.md "
                      "f8f86f0d...53f8 item 4): from now to the end of the run this desk is the ONLY M7 admitter. "
                      "PhysEpQutrit launches nothing native after route-A attempt 5 (r9, slot 1). The parent A "
                      "replay will also be launched by this desk. Admission refuses if any M7-lane native outside "
                      "this desk's ancestry is not in the route-A attempt-5 group.")
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


def _pump(stream, sink, state):
    """Reader thread: drains one helper stream. Records an explicit EOF, or the exception that ended it (v11 (3))."""
    try:
        while True:
            chunk = stream.read(1 << 16)
            if not chunk:
                state["eof"] = True
                return
            sink.append(chunk)
    except BaseException as e:
        state["exception"] = repr(e)


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
    wait error, and both reader threads finished with an explicit EOF and no exception."""
    t0 = time.monotonic()
    ev = {"argv": argv, "pid": None, "pgid": None, "sid": None, "rc": None, "term_sent_after": None,
          "unreaped_after_term_wait": False, "blocking_wait": False, "exception": None, "lost_child": None,
          "wait_errors": [], "readers_finished": None, "readers": None, "stdout": "", "stderr": "", "seconds": None,
          "ok": False}
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=K.TMP, env=K.ENV, start_new_session=True)
    box = {"owned": p.pid}                          # registration: the statement right after Popen
    out, err, readers = [], [], []
    rstate = {"stdout": {"eof": False, "exception": None}, "stderr": {"eof": False, "exception": None}}
    try:
        try:
            ev["pid"] = box["owned"]
            for key, stream, sink in (("stdout", p.stdout, out), ("stderr", p.stderr, err)):
                readers.append(threading.Thread(target=_pump, args=(stream, sink, rstate[key]), daemon=True))
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
    ev["readers"] = rstate
    if ev["readers_finished"]:
        p.stdout.close()
        p.stderr.close()
    ev["stdout"] = b"".join(out).decode("utf-8", "replace")
    ev["stderr"] = b"".join(err).decode("utf-8", "replace")
    ev["seconds"] = round(time.monotonic() - t0, 3)
    ev["ok"] = (ev["rc"] == 0 and ev["term_sent_after"] is None and ev["exception"] is None
                and ev["lost_child"] is None and not ev["wait_errors"] and ev["readers_finished"]
                and all(s["eof"] and s["exception"] is None for s in rstate.values()) and ev["stderr"] == "")
    return ev


def parse_ps_id(text):
    """Identity snapshot rows 'pid ppid pgid uid state rss lstart(5 fields) comm'. pid, ppid, pgid and rss must be
    non-negative decimal, pid >= 1. uid is printed signed (nobody = -2) and must lie in [-2^31, 2^32); it is normalized
    modulo 2^32. Any malformed row raises."""
    rows = {}
    for line in text.splitlines():
        f = line.split(None, 11)
        if (len(f) != 12 or not all(x.isdigit() for x in (f[0], f[1], f[2], f[5])) or not re.fullmatch(r"-?\d+", f[3])
                or not f[4] or not LSTART.fullmatch(" ".join(f[6:11])) or not f[11].strip()
                or int(f[0]) < 1 or not -(1 << 31) <= int(f[3]) < (1 << 32)):
            raise ValueError("malformed ps identity row: %r" % line[:200])
        pid = int(f[0])
        if pid in rows:
            raise ValueError("duplicate pid %d in one ps snapshot" % pid)
        rows[pid] = {"pid": pid, "ppid": int(f[1]), "pgid": int(f[2]), "uid": int(f[3]) & 0xFFFFFFFF, "state": f[4],
                     "rss_bytes": int(f[5]) * 1024, "lstart": " ".join(f[6:11]), "comm": f[11].strip()}
    if not rows:
        raise ValueError("empty ps identity snapshot")
    return rows


def parse_ps_args(text):
    """Args snapshot rows 'pid lstart(5 fields) args' (args may be empty). pid >= 1. Any malformed row raises."""
    rows = {}
    for line in text.splitlines():
        f = line.split(None, 6)
        if len(f) < 6 or not f[0].isdigit() or int(f[0]) < 1 or not LSTART.fullmatch(" ".join(f[1:6])):
            raise ValueError("malformed ps args row: %r" % line[:200])
        pid = int(f[0])
        if pid in rows:
            raise ValueError("duplicate pid %d in the args snapshot" % pid)
        rows[pid] = {"lstart": " ".join(f[1:6]), "args": f[6].strip() if len(f) == 7 else ""}
    if not rows:
        raise ValueError("empty ps args snapshot")
    return rows


def parse_lsof(text):
    """lsof -Fpn cwd records, each exactly 'p<pid>', 'fcwd', 'n<path>' in this order (v11 (3)). A record without
    'fcwd', without its 'n' line or with a path that is not absolute leaves that pid's cwd unresolved (None). Any other
    tag, order, fd name or duplicate pid raises."""
    cwd, cur, step = {}, None, None
    for line in text.splitlines():
        tag, val = line[:1], line[1:]
        if tag == "p" and val.isdigit() and int(val) >= 1 and int(val) not in cwd:
            cur, step = int(val), "need_f"
            cwd[cur] = None
        elif tag == "f" and step == "need_f" and val == "cwd":
            step = "need_n"
        elif tag == "n" and step == "need_n":
            cwd[cur] = val if val.startswith("/") else None
            step = "done"
        else:
            raise ValueError("malformed lsof record: %r" % line[:200])
    if not cwd:
        raise ValueError("empty lsof cwd listing")
    return cwd


def unresolved_args(args):
    """True when argv is not usable as identity: missing, empty, '<defunct>' (zombie) or a parenthesized comm."""
    a = (args or "").strip()
    return not a or a == "<defunct>" or (a.startswith("(") and a.endswith(")"))


def launcher_slot(chain_args):
    """Slot of a desk attempt process from its argv chain (itself first, then its ancestors). The first launcher
    found decides. '--slot N' gives N. A launcher up to v11 (no --slot) gives its LEGACY_SLOTS entry: B_C321-a3 ran in
    slot 2 under v8, and B_C411-p1 runs in slot 1 under v11. Any other launcher without --slot, or no launcher at all,
    gives 'unknown', which blocks both slots."""
    for args in chain_args:
        m = LAUNCHER_SLOT.search(args or "")
        if m:
            version, label, slot = int(m.group(1)), m.group(2), m.group(3)
            if slot:
                return int(slot)
            if version <= 11 and label in LEGACY_SLOTS:
                return LEGACY_SLOTS[label]
            return "unknown"
    return "unknown"


def known_zombie_match(pid, A, C, procs):
    """v14: compare one KNOWN_UNRELATED_ZOMBIES tuple with both identity snapshots and its parent. match is True only
    if every field agrees; the full compared identity is returned for the gate receipt."""
    k = KNOWN_UNRELATED_ZOMBIES[pid]
    a, c, pa, pc = A.get(pid), C.get(pid), A.get(k["ppid"]), C.get(k["ppid"])
    parent = procs.get(k["ppid"])
    zombie_ok = all(x is not None and x["state"].startswith("Z") and x["pid"] == pid and x["ppid"] == k["ppid"]
                    and x["pgid"] == k["pgid"] and x["uid"] == k["uid"] and x["lstart"] == k["lstart"]
                    for x in (a, c))
    parent_ok = (all(x is not None and not x["state"].startswith("Z") and x["pid"] == k["ppid"]
                     and x["uid"] == k["uid"] and x["lstart"] == k["parent"]["lstart"]
                     and k["parent"]["app"] in x["comm"] for x in (pa, pc))
                 and parent is not None and parent["same"] and parent["cwd"] == k["parent"]["cwd"])
    return {"pid": pid, "expected": k, "first": a, "second": c, "parent_first": pa, "parent_second": pc,
            "parent_cwd": parent["cwd"] if parent is not None else None,
            "parent_consistent": parent["same"] if parent is not None else None,
            "zombie_fields_match": zombie_ok, "parent_identity_match": parent_ok, "match": zombie_ok and parent_ok}


def census_once(own_root):
    """One census: ps identity, ps args, lsof cwd, ps identity again. The second identity snapshot is classified; a
    process is consistent only if present in both identity snapshots with equal ppid/pgid/uid/lstart/comm and with args
    of the same lstart (v11 (2)). Returns a scan, a scan with 'error' (fail-closed) or a scan with 'retry'
    (unresolved own-uid identities, or processes whose argv the B/C411 veto cannot resolve)."""
    at, helpers, outs = K.now(), {}, {}
    for name, argv in (("ps_id_1", PS_ID), ("ps_args", PS_ARGS), ("lsof_cwd", LSOF_CWD), ("ps_id_2", PS_ID)):
        try:
            ev = run_helper(argv)
        except Exception as e:                      # Popen failed: nothing was spawned
            return {"at": at, "error": "helper %s not started: %r" % (name, e), "helpers": helpers}
        outs[name] = ev["stdout"]
        helpers[name] = {k: ev[k] for k in ("pid", "pgid", "sid", "rc", "seconds", "term_sent_after", "exception",
                                            "lost_child", "readers_finished", "readers", "ok")}
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
    procs = {}
    for pid, c in C.items():
        a, b = A.get(pid), B.get(pid)
        same = a is not None and all(a[k] == c[k] for k in ("ppid", "pgid", "uid", "lstart", "comm"))
        procs[pid] = dict(c, args=b["args"] if b is not None and b["lstart"] == c["lstart"] else None,
                          cwd=L.get(pid) if c["uid"] == me else None, zombie=c["state"].startswith("Z"), same=same)
    skip = own | ancestors
    unresolved, veto_unresolved, foreign_native, zcmp = [], [], [], []
    for pid, p in procs.items():
        if pid in skip:
            continue
        argv_ok = p["same"] and not unresolved_args(p["args"])
        note = {"pid": pid, "uid": p["uid"], "state": p["state"], "comm": p["comm"][-80:], "consistent": p["same"],
                "args_resolved": not unresolved_args(p["args"]), "cwd_resolved": p["cwd"] is not None}
        if p["uid"] == me and not p["zombie"] and (not argv_ok or p["cwd"] is None):
            unresolved.append(note)                 # own-uid live identity unresolved
        elif not argv_ok:
            cmpr = known_zombie_match(pid, A, C, procs) if pid in KNOWN_UNRELATED_ZOMBIES else None
            if cmpr is not None:
                zcmp.append(cmpr)
            if cmpr is None or not cmpr["match"]:
                veto_unresolved.append(note)        # any uid or zombie: the B/C411 veto cannot see its argv
        if p["uid"] != me and not p["zombie"] and os.path.basename(p["comm"]) in K.NATIVE:
            foreign_native.append(note)
    excluded = {z["pid"] for z in zcmp if z["match"]}
    counts = {"first": len(A), "args": len(B), "lsof": len(L), "second": len(C)}
    if foreign_native:
        return {"at": at, "error": "live native(s) of another uid, identity unresolvable (fail-closed)",
                "foreign_uid_natives": foreign_native, "helpers": helpers, "census_counts": counts,
                "known_zombie_comparisons": zcmp}
    if unresolved or veto_unresolved:
        return {"at": at, "retry": True, "unresolved": unresolved[:50], "veto_unresolved": veto_unresolved[:50],
                "helpers": helpers, "census_counts": counts, "known_zombie_comparisons": zcmp}

    def brief(p, n):
        return dict({k: p[k] for k in ("pid", "ppid", "pgid", "uid", "state", "rss_bytes", "lstart", "comm", "cwd")},
                    args=(p["args"] or "")[:n])

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
    b411 = [p for p in procs.values() if p["pid"] not in skip and p["pid"] not in excluded and not in_desk(p["cwd"])
            and B411_R7.search(p["args"])]
    desk = [p for p in procs.values() if p["pid"] not in skip and not p["zombie"] and in_desk(p["cwd"])
            and (os.path.basename(p["comm"]) in K.NATIVE or DESK_ATTEMPT.search(p["args"] or ""))]
    foreign = [p for p in procs.values() if p["pid"] not in ids and p["pid"] not in own
               and any(m in (p["args"] or "") or m in (p["cwd"] or "") for m in K.LANE_MARKERS)]

    def chain(pid):
        out, x, seen = [], procs.get(pid), set()
        while x is not None and x["pid"] not in seen:
            seen.add(x["pid"])
            out.append(x)
            x = procs.get(x["ppid"])
        return out

    foreign_lane = []                               # v11 (4): lane natives outside this desk's ancestry
    for p in natives:
        ch = chain(p["pid"])
        if not any(in_desk(q["cwd"]) for q in ch):
            foreign_lane.append(dict(brief(p, 300), route_A5=any(ROUTE_A5.search(q["args"] or "") for q in ch)))
    desk_slot = {p["pid"]: launcher_slot([q["args"] or "" for q in chain(p["pid"])]) for p in desk}

    return {"at": at, "identity": "cwd/ancestry over a validated census (v11: identity agreement in A, B and C)",
            "helpers": helpers,
            "census_counts": counts, "own_excluded": sorted(own), "own_ancestors": sorted(ancestors),
            "lane_natives": [brief(p, 300) for p in natives], "lane_native_busy": len(natives),
            "lane_processes": [brief(p, 200) for p in live], "lane_zombies": [brief(p, 200) for p in zombies],
            "lane_rss_bytes": sum(p["rss_bytes"] for p in live), "supervised": supervised,
            "unsupervised_native_groups": unsup, "other_lane_rss_bytes": others_rss, "reserved_bytes": reserved,
            "computable_cap_by_ancestry": headroom,
            "computable_cap": CAP_FIXED if headroom >= CAP_FIXED else headroom,
            "b411_matches": [brief(p, 300) for p in b411],
            "desk_attempt_processes": [dict(brief(p, 300), slot=desk_slot[p["pid"]]) for p in desk],
            "desk_slots_occupied": sorted({str(s) for s in desk_slot.values()}),
            "foreign_marker_matches_excluded": [brief(p, 160) for p in foreign],
            "foreign_lane_natives": foreign_lane,
            "foreign_lane_natives_outside_route_A5": [f for f in foreign_lane if not f["route_A5"]],
            "known_zombie_comparisons": zcmp, "known_zombie_exclusions": sorted(excluded)}


def census(own_root):
    """Validated census with retries: a helper failure, malformed output, an unresolved own-uid identity or an argv the
    B/C411 veto cannot resolve is retried (at most CENSUS_TRIES, CENSUS_PAUSE s apart); after that the scan carries
    'error' and is refused (fail-closed)."""
    tries = []
    for i in range(CENSUS_TRIES):
        r = census_once(own_root)
        kind = "error" if "error" in r else ("unresolved" if "retry" in r else "complete")
        tries.append({"at": r["at"], "result": kind,
                      "detail": r.get("error") or (r.get("unresolved", []) + r.get("veto_unresolved", []))[:10] or None})
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
    """Main's corrected rule: slot 2 is free only when B/C411 r7 is fully reaped AND end-recorded. The matches come from
    the census over the resolved full argv of every process, zombies included (census_once; v11 has no comm fallback)."""
    live = "error" in scan or bool(scan.get("b411_matches"))
    STATE["seen_live"] = STATE["seen_live"] or (live and "error" not in scan)
    st = os.lstat(B411_R7_END_RECORD) if os.path.lexists(B411_R7_END_RECORD) else None
    recorded = st is not None and (st.st_mode & 0o170000) == 0o100000
    return {"b411_r7_live": live, "b411_r7_seen_live": STATE["seen_live"], "end_record": B411_R7_END_RECORD,
            "end_record_exists": recorded, "ok": (not live) and recorded}


def admission_v12(scan, fb, target):
    adm = K.admission(scan, fb, deadline_ok())
    slot = slot_condition(scan)
    if "conditions" not in adm:
        return {"ok": False, "why": adm["why"], "slot": slot, "target_slot": target}
    occupied = scan["desk_slots_occupied"]
    cond = dict(adm["conditions"], slot2_b411_r7_reaped_and_end_recorded=slot["ok"],
                ancestry_headroom_for_fixed_cap=scan["computable_cap_by_ancestry"] >= CAP_FIXED,
                target_slot_free_of_desk_attempts=str(target) not in occupied and "unknown" not in occupied,
                foreign_lane_natives_only_route_A5_slot1=not scan["foreign_lane_natives_outside_route_A5"])
    return {"ok": all(cond.values()), "conditions": cond, "why": [k for k, v in cond.items() if not v], "slot": slot,
            "target_slot": target, "desk_slots_occupied": occupied}


def try_lock(fd):
    """Non-blocking exclusive flock on the desk admission lock; False if another launcher of this desk holds it."""
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except BlockingIOError:
        return False


def unlock(fd):
    fcntl.flock(fd, fcntl.LOCK_UN)


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
               t_last_epoch=t_last.timestamp(), age_seconds=round(age, 1), window_samples=len(window),
               span_seconds=span, free_last=f_last, max_drop=max_drop, limit=limit)
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


def prepare(item, label, target, argv, cap, previous, regen_path, regen_sha0, summary_path, record, quarantine):
    """The gate receipt without its admission evidence, computed before the final census (v10 (3)). ok only if the
    supervisor equals its pin and the regeneration precheck receipt is unchanged since the launcher started."""
    sup_sha = K.sha_file(K.SUPERVISOR)
    regen_sha = K.sha_file(regen_path)
    me = os.path.abspath(__file__)
    rec = {"purpose": "run " + label, "item": item, "label": label, "previous_attempt": previous,
           "launcher_pid": os.getpid(), "launcher": {"path": me, "sha256": K.sha_file(me)}, "prepared_at": K.now(),
           "attempt_rule": ATTEMPT_RULE, "admitter_invariant": ADMITTER_INVARIANT, "slot": target,
           "admission_lock": {"path": LOCK_PATH, "held_from": "before the final census",
                              "released": "%d s after the spawn, at once on refusal, or at exit" % LOCK_SETTLE},
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


def mode_run(item, label, target, regen_tag=None):
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
    lock_fd = os.open(LOCK_PATH, os.O_RDONLY)       # v12: desk admission lock (created once, at copy-in)
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-run-%s.log" % label))
    out_fd = K.open_append_x(stdout_log)            # v10 (3): output file prepared before any admission census
    cap = CAP_FIXED
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", label + "-parent-replay", "--wall", str(SUP_WALL),
            "--rss-cap", str(cap), "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", record,
            "--quarantine", quarantine, "--grace", str(SUP_GRACE), "--",
            K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v5.py"), "run", item, "--label", label,
            "--rss-stop", str(cap)]
    adm2 = {}                                           # the final admission, once one has been evaluated
    while True:
        scan = census(os.getpid())
        fb = K.free_bytes()
        adm = admission_v12(scan, fb, target)
        log_line(logfd, "run " + label, scan, fb, adm, 1)
        last = {"scan": scan, "free_bytes": fb, "admission": adm}
        if adm["ok"] and not STATE["signals"]:
            t1 = time.monotonic()
            paused = pause(FIRST_TO_FINAL)
            rec, prepared_ok = prepare(item, label, target, argv, cap, previous, regen_path, regen_sha0,
                                       summary_path, record, quarantine)
            stab = monitor_stability()
            os.write(logfd, (json.dumps({"at": K.now(), "paused_ok": paused, "prepared_ok": prepared_ok,
                                         "stability": {k: stab.get(k) for k in (
                                             "ok", "why", "age_seconds", "window_samples", "free_last", "max_drop",
                                             "limit")}}) + "\n").encode())
            if not try_lock(lock_fd):                   # v12: admissions one at a time
                busy = dict(adm, ok=False, why=adm["why"] + ["admission lock held by another launcher of this desk"])
                log_line(logfd, "run " + label, scan, fb, busy, 2)
                last = {"scan": scan, "free_bytes": fb, "admission": busy}
                if not deadline_ok() or STATE["signals"]:
                    break
                time.sleep(SLEEP)
                continue
            scan2 = census(os.getpid())                 # the final census, under the admission lock
            fb2 = K.free_bytes()
            adm2 = admission_v12(scan2, fb2, target)
            stab2 = monitor_stability()                 # v11 (1): re-evaluated after the final census
            gap = round(time.monotonic() - t1, 1)
            extra = [w for w, bad in (("pause interrupted", not paused),
                                      ("supervisor pin or regen receipt changed", not prepared_ok),
                                      ("monitor stability before the final census", not stab["ok"]),
                                      ("monitor stability after the final census", not stab2["ok"]),
                                      ("gap below 60 s", gap < 60),
                                      ("a free reading below the gate", fb < K.GATE or fb2 < K.GATE)) if bad]
            pre = None
            if adm2["ok"] and not extra:                # immediate pre-spawn guard (microseconds)
                age = time.time() - stab2["t_last_epoch"]
                pre = {"free_bytes": K.free_bytes(), "deadline_ok": deadline_ok(),
                       "launcher_signals": len(STATE["signals"]),
                       "quarantine_records": sorted(glob.glob(os.path.join(K.RECEIPTS, "*.QUARANTINE.json"))),
                       "monitor_last_sample_age_seconds": round(age, 3)}
                pre["ok"] = (pre["free_bytes"] >= K.GATE and pre["deadline_ok"] and not pre["launcher_signals"]
                             and not pre["quarantine_records"]
                             and 0 <= age <= MON["max_age_seconds"])     # v12: the unrounded age is compared
                if not pre["ok"]:
                    extra.append("pre-spawn guard")
            adm2.update(first=adm, stability=stab, stability_after_final_census=stab2, paused_ok=paused,
                        prepared_ok=prepared_ok, prespawn_recheck=pre,
                        two_readings={"first": {"at": scan["at"], "free_bytes": fb},
                                      "second": {"at": scan2["at"], "free_bytes": fb2}, "gap_seconds": gap,
                                      "gate": K.GATE, "both_at_least_gate": fb >= K.GATE and fb2 >= K.GATE})
            adm2["ok"] = adm2["ok"] and not extra
            adm2["why"] = adm2["why"] + extra
            if adm2["ok"]:
                break                                   # the admission lock stays held through the spawn
            unlock(lock_fd)
            log_line(logfd, "run " + label, scan2, fb2, adm2, 2)
            last = {"scan": scan2, "free_bytes": fb2, "admission": adm2}
        if not deadline_ok() or STATE["signals"]:
            rec, _ = prepare(item, label, target, argv, cap, previous, regen_path, regen_sha0, summary_path, record,
                             quarantine)
            rec.update(last, at=K.now(), not_launched="not admitted while deadline_ok() held, or launcher signals: "
                       "%s / signals %s" % (last["admission"]["why"], STATE["signals"]))
            print(json.dumps({"gate_sha256": K.write_json_x(gate_path, rec), "launched": False,
                              "why": rec["not_launched"]}), flush=True)
            os.close(out_fd)
            os.close(logfd)
            return 2
        time.sleep(SLEEP)
    if not adm2.get("ok"):                              # left the loop through the lock-busy branch at the deadline
        rec, _ = prepare(item, label, target, argv, cap, previous, regen_path, regen_sha0, summary_path, record,
                         quarantine)
        rec.update(last, at=K.now(), not_launched="admission lock busy when deadline_ok() ended, or launcher signals: "
                   "%s / signals %s" % (last["admission"]["why"], STATE["signals"]))
        print(json.dumps({"gate_sha256": K.write_json_x(gate_path, rec), "launched": False,
                          "why": rec["not_launched"]}), flush=True)
        os.close(out_fd)
        os.close(logfd)
        return 2
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
        releaser = threading.Timer(LOCK_SETTLE, unlock, args=(lock_fd,))
        releaser.daemon = True
        releaser.start()                                # v12: admission lock released LOCK_SETTLE s after the spawn
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
    """v14 self-test; launches nothing. run_helper() bounds, signals, session isolation and reader EOF with short
    python children; reader-exception recording; parser cases (v11); slot-attribution and admission-lock cases (v12);
    known-zombie tuple match/mismatch cases (v14);
    then one census, informational admissions for both slots and one monitor-stability evaluation (read-only)."""
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
        "readers_explicit_eof_no_exception_all_cases": all(
            all(s["eof"] and s["exception"] is None for s in ev["readers"].values()) for ev in cases.values()),
    }

    class Failing:
        def read(self, n):
            raise OSError("injected reader failure")

    def raises(fn, text):
        try:
            fn(text)
        except ValueError:
            return True
        return False

    st_ok, st_bad, sink = {"eof": False, "exception": None}, {"eof": False, "exception": None}, []
    _pump(io.BytesIO(b"abc"), sink, st_ok)
    _pump(Failing(), [], st_bad)
    lst = "Sun Oct 18 08:00:00 2026"
    parser_checks = {
        "pump_records_eof": st_ok == {"eof": True, "exception": None} and sink == [b"abc"],
        "pump_records_exception_without_eof": st_bad["eof"] is False and "injected reader failure" in st_bad["exception"],
        "lsof_complete_record_resolved": parse_lsof("p42\nfcwd\nn/abs/path\n") == {42: "/abs/path"},
        "lsof_n_without_fcwd_malformed": raises(parse_lsof, "p42\nnunknown\n"),
        "lsof_missing_fcwd_unresolved": parse_lsof("p42\np43\nfcwd\nn/x\n") == {42: None, 43: "/x"},
        "lsof_non_absolute_path_unresolved": parse_lsof("p42\nfcwd\nnunknown\n") == {42: None},
        "lsof_other_fd_malformed": raises(parse_lsof, "p42\nftxt\nn/x\n"),
        "lsof_duplicate_pid_malformed": raises(parse_lsof, "p42\nfcwd\nn/x\np42\nfcwd\nn/y\n"),
        "ps_negative_rss_malformed": raises(parse_ps_id, "42 1 42 501 S -5 %s /bin/x\n" % lst),
        "ps_negative_pid_malformed": raises(parse_ps_id, "-42 1 42 501 S 5 %s /bin/x\n" % lst),
        "ps_uid_minus2_normalized": parse_ps_id("42 1 42 -2 S 5 %s /bin/x\n" % lst)[42]["uid"] == 0xFFFFFFFE,
        "ps_empty_args_parsed_and_unresolved": unresolved_args(parse_ps_args("42 %s\n" % lst)[42]["args"]),
        "zombie_and_parenthesized_args_unresolved": (unresolved_args("<defunct>") and unresolved_args("(git)")
                                                     and not unresolved_args("/bin/ps -ax")),
    }
    checks.update(parser_checks)
    py = "/Library/Developer/CommandLineTools/usr/bin/python3 -I -B "
    natives = ["/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat -q -f --time=5400 /dev/fd/11 fifo/X.drat.fifo",
               py + "/d/scripts-v12/replay_B_v5.py run B_C311cuts --label B_C311cuts-p1 --rss-stop 2797076480",
               py + "/c/supervise_r3.py --name B_C311cuts-p1-parent-replay --wall 10200 --rss-cap 2797076480"]
    slot_cases = {
        "v12_slot_2": (natives + [py + "../scripts-v12/launch_B_v12.py run B_C311cuts --label B_C311cuts-p1 --slot 2"], 2),
        "v12_slot_1_tagged": ([py + "../scripts-v12/launch_B_v12.py run A_C311cuts --label A_C311cuts-p1 --slot 1 "
                                    "--regen-tag r1"], 1),
        "legacy_v11_B_C411_p1_slot_1": (natives + [py + "../scripts/launch_B_v11.py run B_C411 --label B_C411-p1 "
                                                      "--regen-tag r2"], 1),
        "legacy_v8_a3_slot_2": (natives + [py + "../scripts/launch_B_v8.py run B_C321 --label B_C321-a3"], 2),
        "legacy_unlisted_label_unknown": ([py + "../scripts/launch_B_v11.py run B_C321 --label B_C321-a4"], "unknown"),
        "v12_without_slot_unknown": ([py + "../scripts-v12/launch_B_v12.py run B_C321 --label B_C321-a5"], "unknown"),
        "no_launcher_unknown": ([py + "/d/scripts-v12/replay_B_v5.py regen A_C311cuts"], "unknown"),
    }
    slot_results = {k: launcher_slot(v[0]) for k, v in slot_cases.items()}
    checks.update({"slot_" + k: slot_results[k] == v[1] for k, v in slot_cases.items()})
    fd1, fd2 = os.open(LOCK_PATH, os.O_RDONLY), os.open(LOCK_PATH, os.O_RDONLY)
    try:
        lock_steps = [try_lock(fd1), try_lock(fd2)]
        unlock(fd1)
        lock_steps += [try_lock(fd2)]
        unlock(fd2)
    finally:
        os.close(fd1)
        os.close(fd2)
    checks["admission_lock_exclusive_then_released"] = lock_steps == [True, False, True]
    zt = KNOWN_UNRELATED_ZOMBIES[57860]
    zrow = {"pid": 57860, "ppid": 43939, "pgid": 43939, "uid": 501, "state": "Z", "rss_bytes": 0,
            "lstart": zt["lstart"], "comm": "<defunct>"}
    prow = {"pid": 43939, "ppid": 1, "pgid": 43939, "uid": 501, "state": "S", "rss_bytes": 1,
            "lstart": zt["parent"]["lstart"], "comm": "/Applications/WeChat.app/Contents/MacOS/WeChat"}
    good_procs = {43939: dict(prow, args="/Applications/WeChat.app/Contents/MacOS/WeChat", cwd=zt["parent"]["cwd"],
                              zombie=False, same=True)}
    variants = {"exact": ({57860: zrow, 43939: prow}, {57860: zrow, 43939: prow}, good_procs, True),
                "zombie_lstart_differs_in_second": ({57860: zrow, 43939: prow},
                                                    {57860: dict(zrow, lstart="Sun Oct 18 09:30:00 2026"),
                                                     43939: prow}, good_procs, False),
                "not_zombie_in_first": ({57860: dict(zrow, state="S"), 43939: prow}, {57860: zrow, 43939: prow},
                                        good_procs, False),
                "missing_from_first": ({43939: prow}, {57860: zrow, 43939: prow}, good_procs, False),
                "parent_restarted": ({57860: zrow, 43939: dict(prow, lstart="Sun Oct 18 09:31:00 2026")},
                                     {57860: zrow, 43939: dict(prow, lstart="Sun Oct 18 09:31:00 2026")},
                                     good_procs, False),
                "parent_other_app": ({57860: zrow, 43939: dict(prow, comm="/usr/bin/python3")},
                                     {57860: zrow, 43939: dict(prow, comm="/usr/bin/python3")}, good_procs, False),
                "parent_cwd_differs": ({57860: zrow, 43939: prow}, {57860: zrow, 43939: prow},
                                       {43939: dict(good_procs[43939], cwd="/tmp")}, False),
                "pgid_differs": ({57860: dict(zrow, pgid=1), 43939: prow}, {57860: dict(zrow, pgid=1), 43939: prow},
                                 good_procs, False)}
    zombie_results = {k: known_zombie_match(57860, v[0], v[1], v[2])["match"] for k, v in variants.items()}
    checks.update({"zombie_tuple_" + k: zombie_results[k] is v[3] for k, v in variants.items()})
    checks["zombie_tuples_exactly_two_known"] = sorted(KNOWN_UNRELATED_ZOMBIES) == [57860, 59426]
    scan = census(os.getpid())
    fb = K.free_bytes()
    adm = {"slot_1": admission_v12(scan, fb, 1), "slot_2": admission_v12(scan, fb, 2)}
    stab = monitor_stability()
    checks["census_complete"] = "error" not in scan
    keep = ("pid", "pgid", "sid", "rc", "term_sent_after", "unreaped_after_term_wait", "blocking_wait", "exception",
            "lost_child", "wait_errors", "readers_finished", "readers", "seconds", "ok")
    me = os.path.abspath(__file__)
    out = {"label": label, "at": K.now(), "launcher": {"path": me, "sha256": K.sha_file(me)},
           "bklib": {"path": os.path.abspath(K.__file__), "sha256": K.sha_file(os.path.abspath(K.__file__))},
           "own_pid": os.getpid(), "own_pgid": own_pgid, "own_sid": os.getsid(0),
           "cases": {k: dict({x: v[x] for x in keep}, argv=v["argv"], stdout=v["stdout"][:200],
                             stderr=v["stderr"][:200]) for k, v in cases.items()},
           "kills": kills, "slot_results": slot_results, "lock_steps": lock_steps, "census": scan, "free_bytes": fb,
           "admission_informational": adm,
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
                      "foreign_lane_natives": [[p["pid"], os.path.basename(p["comm"]), p["route_A5"]]
                                               for p in scan.get("foreign_lane_natives", [])],
                      "census_try_results": [t["result"] for t in scan.get("census_tries", [])],
                      "desk_slots_occupied": scan.get("desk_slots_occupied"),
                      "admission_why": {k: v.get("why") for k, v in adm.items()},
                      "stability": {k: stab.get(k) for k in ("ok", "why", "age_seconds", "window_samples", "free_last",
                                                             "max_drop", "limit")}}), flush=True)
    return 0 if out["all_ok"] else 1


def main():
    a = sys.argv[1:]
    if a and a[0] == "run":
        ok = (len(a) in (6, 8) and a[1] in K.ITEMS and a[2] == "--label"
              and bool(re.fullmatch(r"[A-Za-z0-9_.-]+", a[3])) and a[3].startswith(a[1] + "-")
              and a[4] == "--slot" and a[5] in ("1", "2")
              and (len(a) == 6 or (a[6] == "--regen-tag" and bool(re.fullmatch(r"[A-Za-z0-9]+", a[7])))))
        if not ok:
            raise SystemExit("usage: launch_B_v14.py run ITEM --label ITEM-<suffix> --slot {1,2} [--regen-tag TAG]")
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_run(a[1], a[3], int(a[5]), a[7] if len(a) == 8 else None))
    if a and a[0] == "wait-start" and len(a) == 2 and re.fullmatch(r"[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_wait_start(a[1]))
    if a and a[0] == "test-exception-path" and len(a) == 2 and re.fullmatch(r"test-[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_test_exception_path(a[1]))
    if a and a[0] == "selftest-v14" and len(a) == 2 and re.fullmatch(r"test-[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_selftest(a[1]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
