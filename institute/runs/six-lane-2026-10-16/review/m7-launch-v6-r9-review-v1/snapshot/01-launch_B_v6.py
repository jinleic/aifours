#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v6.

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

Usage: launch_B_v6.py run ITEM --label ITEM-<suffix>
       launch_B_v6.py wait-start LABEL
       launch_B_v6.py test-exception-path LABEL          (LABEL: test-...; the v5 test mode, unchanged)

run waits, with bounded sleeps of 90 s (never spinning), until two fresh readings admit a native launch (gate (a)-(d)
above plus the slot-2 condition, <= 2 busy lane natives and lane RSS headroom for the projected peak). If nothing is
admitted by 17:30 PDT, nothing is launched and the gate receipt records it. Then it requires receipts/regen-ITEM.json
= MATCH and receipts/selfcheck-summary.json all_ok, writes the gate receipt exclusively, runs the pinned
supervise_r3.py (own session) around 'replay_B_v2.py run ITEM --label LABEL --rss-stop CAP' through run_owned(), and
writes an outcome receipt. wait-start sleeps 60 s at a time until receipts/LABEL.launch.json or LABEL.driver.json
exists, or LABEL.gate.json records 'not_launched', then prints a summary; it never scans the lane.
No SIGKILL, no Popen.kill, no subprocess timeouts.
"""
import datetime
import glob
import json
import os
import re
import signal
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bklib_v1 as K  # noqa: E402

DEADLINE = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
NO_LAUNCH_AFTER = datetime.datetime.fromisoformat("2026-10-18T17:30:00-07:00")
SLEEP = 90
SUP_WALL = 10200
SUP_GRACE = 180
CAP_FIXED = 2797076480                          # Main, about 07:05 PDT
SECOND_READING_DELAY = 62                       # >= 60 s between the two free-space readings
ATTEMPT_RULE = ("Main messages 05:00-07:05 PDT 2026-10-18: attempts are UNKNOWN on any stop and never relabelled. "
                "B_C321-a3 is a NEW attempt in SLOT 2 (after B/C411 r7 reaped and end-recorded) with its own receipts "
                "and a fresh gate: two free readings >= 12.2e9 + projected growth, 60 s apart; lane caps (<= 2 busy "
                "lane natives by ancestry, lane RSS <= 8 GiB); RSS cap 2,797,076,480 B unless an ancestry scan shows "
                "more headroom; no stacking; floor 12e9 in flight; no new launches after 17:30 PDT.")
B411_R7 = re.compile(r"B_C411|k3_direct_B_r\d+\.py C411")
B411_R7_END_RECORD = os.path.join(K.K3DIR, "cert_B_r7", "B_C411.json")
STATE = {"signals": [], "seen_live": False}
POLL = 0.25
STOP_WAIT = SUP_GRACE + 120


def deadline_ok():
    t = datetime.datetime.now().astimezone()
    return t < DEADLINE and t < NO_LAUNCH_AFTER


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


def lane_scan_ancestry(own_root):
    """One fresh scan with lane identity by cwd and ancestry (gate (a)). Returns bklib_v1.lane_scan's keys used by
    bklib_v1.admission and the slot condition, plus the ancestry headroom and the foreign marker matches."""
    at = K.now()
    a = K._run_text(["/bin/ps", "-axww", "-o", "pid=,ppid=,pgid=,state=,rss=,comm="])
    b = K._run_text(["/bin/ps", "-axww", "-o", "pid=,args="])
    lo = K._run_text(["/usr/sbin/lsof", "-a", "-d", "cwd", "-Fpn"])
    if a.returncode != 0 or b.returncode != 0:
        return {"at": at, "error": "ps failed: rc %d/%d" % (a.returncode, b.returncode)}
    procs = {}
    for line in a.stdout.splitlines():
        parts = line.split(None, 5)
        if len(parts) == 6:
            procs[int(parts[0])] = {"pid": int(parts[0]), "ppid": int(parts[1]), "pgid": int(parts[2]),
                                    "state": parts[3], "rss_bytes": int(parts[4]) * 1024, "comm": parts[5].strip(),
                                    "args": "", "cwd": ""}
    for line in b.stdout.splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2 and parts[0].isdigit() and int(parts[0]) in procs:
            procs[int(parts[0])]["args"] = parts[1]
    cur = None
    for line in lo.stdout.splitlines():
        if line.startswith("p"):
            cur = int(line[1:])
        elif line.startswith("n") and cur in procs:
            procs[cur]["cwd"] = line[1:]
    children = {}
    for p in procs.values():
        children.setdefault(p["ppid"], []).append(p["pid"])

    def descendants(root):
        out, stack = set(), [root]
        while stack:
            for c in children.get(stack.pop(), []):
                if c not in out:
                    out.add(c)
                    stack.append(c)
        return out

    own = {own_root} | descendants(own_root)
    roots = {pid for pid, p in procs.items() if pid not in own and cwd_in_lane(p["cwd"])}
    ids = set(roots)
    for r in roots:
        ids |= descendants(r)
    ids -= own
    live = [procs[i] for i in sorted(ids) if not procs[i]["state"].startswith("Z")]
    natives = [p for p in live if os.path.basename(p["comm"]) in K.NATIVE]
    covered, supervised = set(), []
    for p in live:
        m = K.CAP_ARG.search(p["args"])
        if "supervise_r" in p["args"] and m:
            desc = descendants(p["pid"])
            groups = {procs[d]["pgid"] for d in desc if d in procs}
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
    foreign = [{"pid": p["pid"], "comm": os.path.basename(p["comm"]), "cwd": p["cwd"], "args": p["args"][:160]}
               for p in procs.values() if p["pid"] not in ids and p["pid"] not in own
               and any(m in p["args"] or m in p["cwd"] for m in K.LANE_MARKERS)]
    return {"at": at, "identity": "cwd/ancestry", "own_excluded": sorted(own),
            "lane_natives": [{k: p[k] for k in ("pid", "ppid", "pgid", "state", "rss_bytes", "comm", "cwd")}
                             | {"args": p["args"][:300]} for p in natives],
            "lane_native_busy": len(natives),
            "lane_processes": [{k: p[k] for k in ("pid", "ppid", "pgid", "state", "rss_bytes", "cwd")}
                               | {"args": p["args"][:200]} for p in live],
            "lane_rss_bytes": sum(p["rss_bytes"] for p in live), "supervised": supervised,
            "unsupervised_native_groups": unsup, "other_lane_rss_bytes": others_rss, "reserved_bytes": reserved,
            "computable_cap_by_ancestry": headroom,
            "computable_cap": CAP_FIXED if headroom >= CAP_FIXED else headroom,
            "foreign_marker_matches_excluded": foreign}


def slot_condition(scan):
    """Main's corrected rule: slot 2 is free only when B/C411 r7 is fully reaped AND end-recorded."""
    procs = scan.get("lane_natives", []) + scan.get("lane_processes", [])
    live = any(B411_R7.search(p.get("args", "")) for p in procs) or "error" in scan
    STATE["seen_live"] = STATE["seen_live"] or (live and "error" not in scan)
    st = os.lstat(B411_R7_END_RECORD) if os.path.lexists(B411_R7_END_RECORD) else None
    recorded = st is not None and (st.st_mode & 0o170000) == 0o100000
    return {"b411_r7_live": live, "b411_r7_seen_live": STATE["seen_live"], "end_record": B411_R7_END_RECORD,
            "end_record_exists": recorded, "ok": (not live) and recorded}


def admission_v6(scan, fb):
    adm = K.admission(scan, fb, deadline_ok())
    slot = slot_condition(scan)
    if "conditions" not in adm:
        return {"ok": False, "why": adm["why"], "slot": slot}
    cond = dict(adm["conditions"], slot2_b411_r7_reaped_and_end_recorded=slot["ok"],
                ancestry_headroom_for_fixed_cap=scan["computable_cap_by_ancestry"] >= CAP_FIXED)
    return {"ok": all(cond.values()), "conditions": cond, "why": [k for k, v in cond.items() if not v], "slot": slot}


def log_line(logfd, purpose, scan, fb, adm, reading):
    line = {"at": scan.get("at"), "purpose": purpose, "reading": reading, "ok": adm["ok"], "why": adm["why"],
            "free_bytes": fb, "busy": scan.get("lane_native_busy"),
            "natives": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("lane_natives", [])],
            "lane_rss": scan.get("lane_rss_bytes"), "reserved": scan.get("reserved_bytes"),
            "headroom": scan.get("computable_cap_by_ancestry"), "cap": scan.get("computable_cap"),
            "foreign_excluded": len(scan.get("foreign_marker_matches_excluded", [])),
            "b411_r7_live": adm["slot"]["b411_r7_live"], "b411_r7_end_record_exists": adm["slot"]["end_record_exists"]}
    os.write(logfd, (json.dumps(line) + "\n").encode())


def wait_for_admission(logfd, purpose):
    while True:
        scan = lane_scan_ancestry(os.getpid())
        fb = K.free_bytes()
        adm = admission_v6(scan, fb)
        log_line(logfd, purpose, scan, fb, adm, 1)
        if adm["ok"] and not STATE["signals"]:
            t1 = time.monotonic()
            time.sleep(SECOND_READING_DELAY)
            scan2 = lane_scan_ancestry(os.getpid())
            fb2 = K.free_bytes()
            adm2 = admission_v6(scan2, fb2)
            gap = round(time.monotonic() - t1, 1)
            log_line(logfd, purpose, scan2, fb2, adm2, 2)
            adm2["two_readings"] = {"first": {"at": scan["at"], "free_bytes": fb}, "second": {"at": scan2["at"],
                                    "free_bytes": fb2}, "gap_seconds": gap, "gate": K.GATE,
                                    "both_at_least_gate": fb >= K.GATE and fb2 >= K.GATE}
            if adm2["ok"] and gap >= 60 and fb >= K.GATE and fb2 >= K.GATE:
                return scan2, fb2, adm2
            adm, scan, fb = adm2, scan2, fb2
            adm["ok"] = False
        if not deadline_ok() or STATE["signals"]:
            return scan, fb, adm
        time.sleep(SLEEP)


def mode_run(item, label):
    regen_path = os.path.join(K.RECEIPTS, "regen-%s.json" % item)
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
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-run-%s.log" % label))
    scan, fb, adm = wait_for_admission(logfd, "run " + label)
    cap = CAP_FIXED
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", label + "-parent-replay", "--wall", str(SUP_WALL),
            "--rss-cap", str(cap), "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", record,
            "--quarantine", quarantine, "--grace", str(SUP_GRACE), "--",
            K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v2.py"), "run", item, "--label", label,
            "--rss-stop", str(cap)]
    sup_sha = K.sha_file(K.SUPERVISOR)
    rec = {"purpose": "run " + label, "item": item, "label": label, "previous_attempt": previous,
           "launcher_pid": os.getpid(), "at": K.now(), "attempt_rule": ATTEMPT_RULE,
           "scan": scan, "free_bytes": fb, "admission": adm,
           "rss_cap": {"value": cap, "rule": "fixed by Main (about 07:05 PDT); ancestry headroom must be >= it",
                       "CAP_FIXED": CAP_FIXED, "computable_cap_by_ancestry": scan.get("computable_cap_by_ancestry"),
                       "CAP_MAX": K.CAP_MAX, "LANE_RSS_LIMIT": K.LANE_RSS_LIMIT, "SAFETY_MARGIN": K.SAFETY_MARGIN,
                       "MIN_CAP": K.MIN_CAP, "PROJECTED_PEAK": K.PROJECTED_PEAK,
                       "UNSUPERVISED_GROUP_RESERVE": K.UNSUPERVISED_GROUP_RESERVE,
                       "OTHER_LANE_MARGIN": K.OTHER_LANE_MARGIN, "reserved": scan.get("reserved_bytes")},
           "supervisor": {"path": K.SUPERVISOR, "sha256": sup_sha, "pin": K.SUPERVISOR_SHA256,
                          "equals_pin": sup_sha == K.SUPERVISOR_SHA256, "wall": SUP_WALL, "grace": SUP_GRACE,
                          "floor": K.FLOOR, "record": record, "quarantine": quarantine},
           "argv": argv, "cwd": K.TMP, "env": K.ENV, "scripts_sha256": K.script_hashes(),
           "regen_receipt_sha256": K.sha_file(regen_path), "selfcheck_summary_sha256": K.sha_file(summary_path)}
    if not adm["ok"] or sup_sha != K.SUPERVISOR_SHA256 or STATE["signals"]:
        rec["not_launched"] = "admission failed: %s / supervisor pin %s / launcher signals %s" % (
            adm["why"], sup_sha == K.SUPERVISOR_SHA256, STATE["signals"])
        print(json.dumps({"gate_sha256": K.write_json_x(gate_path, rec), "launched": False,
                          "why": rec["not_launched"]}), flush=True)
        os.close(logfd)
        return 2
    gate_sha = K.write_json_x(gate_path, rec)
    print(json.dumps({"gate_sha256": gate_sha, "launched": True, "rss_cap": cap, "free_bytes": fb,
                      "busy": scan["lane_native_busy"]}), flush=True)
    out_fd = K.open_append_x(stdout_log)
    started = K.now()
    t0 = time.monotonic()
    ev = run_owned(argv, out_fd, launcher_marker)
    os.close(out_fd)
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


def main():
    a = sys.argv[1:]
    if a and a[0] == "run":
        if (len(a) != 4 or a[1] not in K.ITEMS or a[2] != "--label"
                or not (re.fullmatch(r"[A-Za-z0-9_.-]+", a[3]) and a[3].startswith(a[1] + "-"))):
            raise SystemExit("usage: launch_B_v6.py run ITEM --label ITEM-<suffix>")
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_run(a[1], a[3]))
    if a and a[0] == "wait-start" and len(a) == 2 and re.fullmatch(r"[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_wait_start(a[1]))
    if a and a[0] == "test-exception-path" and len(a) == 2 and re.fullmatch(r"test-[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_test_exception_path(a[1]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
