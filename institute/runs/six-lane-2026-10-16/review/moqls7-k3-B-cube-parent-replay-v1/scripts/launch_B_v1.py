#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1).

Usage: launch_B_v1.py selfcheck
       launch_B_v1.py run ITEM

Both modes wait, with bounded sleeps of 90 s (never spinning), until a fresh lane scan and a fresh free-space reading
admit a native launch under the parent's slot rule (bklib_v1.admission: <= 2 busy lane natives, lane RSS headroom
for the projected peak, a computable RSS cap >= 2.5 GiB, free bytes >= 12.2e9 + projected growth, before 15:30 PDT).
If no slot opens by then, nothing is launched and the gate receipt records it.
  selfcheck: runs replay_B_v1.py selfcheck as a child and reaps it (blocking wait, no timeout).
  run: requires receipts/regen-ITEM.json = MATCH and receipts/selfcheck-summary.json all_ok; takes this desk's RSS cap
       from the fresh scan (min(3.5 GiB, 8 GiB - reservations of every other lane process)); writes the gate receipt
       exclusively; runs the pinned lane supervisor supervise_r3.py (own session) around
       'replay_B_v1.py run ITEM --rss-stop CAP' with record and quarantine paths in this desk; reaps it and writes an
       outcome receipt. A SIGTERM to this launcher is forwarded to its supervisor child, which stops the group.
No SIGKILL, no Popen.kill, no subprocess timeouts.
"""
import datetime
import json
import os
import signal
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bklib_v1 as K  # noqa: E402

DEADLINE = datetime.datetime.fromisoformat("2026-10-18T15:30:00-07:00")
NO_LAUNCH_AFTER = datetime.datetime.fromisoformat("2026-10-18T17:00:00-07:00")
SLEEP = 90
SUP_WALL = 10200
SUP_GRACE = 180
SLOT_RULE = ("Main message received about 04:20 PDT 2026-10-18: this desk owns phys-2 lane slot 2; launch the B/C321 "
             "native replay as soon as regeneration and self-checks PASS, using a fresh gate >= 12.2e9 B plus growth "
             "and a fresh lane scan showing <= 2 busy processes; a floor or other stop is UNKNOWN, no retry without "
             "parent GO. Unchanged: lane total RSS <= 8 GiB, <= 4 busy lane natives, floor 12e9, 15:30/17:00 PDT.")
STATE = {"child": None, "forwarded": []}


def deadline_ok():
    t = datetime.datetime.now().astimezone()
    return t < DEADLINE and t < NO_LAUNCH_AFTER


def on_term(signum, frame):
    pid = STATE["child"]
    entry = {"signal": signal.Signals(signum).name, "at": K.now(), "child": pid}
    if pid is not None:
        try:
            os.kill(pid, signal.SIGTERM)
            entry["forwarded_sigterm"] = True
        except OSError as e:
            entry["forward_error"] = repr(e)
    STATE["forwarded"].append(entry)


def wait_for_admission(logfd, purpose):
    while True:
        scan = K.lane_scan(own_root=os.getpid())
        fb = K.free_bytes()
        adm = K.admission(scan, fb, deadline_ok())
        line = {"at": scan.get("at"), "purpose": purpose, "ok": adm["ok"], "why": adm["why"], "free_bytes": fb,
                "busy": scan.get("lane_native_busy"),
                "natives": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("lane_natives", [])],
                "lane_rss": scan.get("lane_rss_bytes"), "reserved": scan.get("reserved_bytes"),
                "cap": scan.get("computable_cap"), "route_A_running": scan.get("route_A_running"),
                "route_B_started": scan.get("route_B_started")}
        os.write(logfd, (json.dumps(line) + "\n").encode())
        if adm["ok"] or not deadline_ok() or STATE["forwarded"]:
            return scan, fb, adm
        time.sleep(SLEEP)


def reap(p):
    pid, st, ru = os.wait4(p.pid, 0)
    p.returncode = os.waitstatus_to_exitcode(st)
    return {"pid": p.pid, "rc": p.returncode, "maxrss_bytes": ru.ru_maxrss, "user_seconds": round(ru.ru_utime, 3)}


def mode_selfcheck():
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-selfcheck.log"))
    scan, fb, adm = wait_for_admission(logfd, "selfcheck")
    rec = {"purpose": "selfcheck", "launcher_pid": os.getpid(), "at": K.now(), "slot_rule": SLOT_RULE,
           "scan": scan, "free_bytes": fb, "admission": adm, "scripts_sha256": K.script_hashes()}
    path = os.path.join(K.RECEIPTS, "selfcheck.gate.json")
    if not adm["ok"]:
        rec["not_launched"] = "admission failed: %s" % adm["why"]
        print(json.dumps({"selfcheck_gate_sha256": K.write_json_x(path, rec), "launched": False,
                          "why": adm["why"]}), flush=True)
        os.close(logfd)
        return 2
    print(json.dumps({"selfcheck_gate_sha256": K.write_json_x(path, rec), "launched": True}), flush=True)
    p = subprocess.Popen([K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v1.py"), "selfcheck"],
                         stdin=subprocess.DEVNULL, cwd=K.TMP, env=K.ENV)
    STATE["child"] = p.pid
    out = reap(p)
    STATE["child"] = None
    os.write(logfd, (json.dumps({"at": K.now(), "selfcheck_child": out}) + "\n").encode())
    os.close(logfd)
    print(json.dumps({"selfcheck_child": out}), flush=True)
    return out["rc"]


def mode_run(item):
    regen_path = os.path.join(K.RECEIPTS, "regen-%s.json" % item)
    summary_path = os.path.join(K.RECEIPTS, "selfcheck-summary.json")
    with open(regen_path) as f:
        regen = json.load(f)
    with open(summary_path) as f:
        summary = json.load(f)
    if regen.get("result") != "MATCH" or summary.get("all_ok") is not True:
        raise SystemExit("prerequisites not met: regen %r, selfcheck all_ok %r" % (regen.get("result"),
                                                                                  summary.get("all_ok")))
    gate_path = os.path.join(K.RECEIPTS, item + ".gate.json")
    outcome_path = os.path.join(K.RECEIPTS, item + ".launch-outcome.json")
    record = os.path.join(K.RECEIPTS, item + ".supervisor.json")
    quarantine = os.path.join(K.RECEIPTS, item + ".QUARANTINE.json")
    stdout_log = os.path.join(K.LOGS, item + ".supervisor-stdout.log")
    for pth in (gate_path, outcome_path, record, quarantine, stdout_log):
        if os.path.lexists(pth):
            raise SystemExit("exists: " + pth)
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-run-%s.log" % item))
    scan, fb, adm = wait_for_admission(logfd, "run " + item)
    cap = scan.get("computable_cap")
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", item + "-parent-replay-v1", "--wall", str(SUP_WALL),
            "--rss-cap", str(cap), "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", record,
            "--quarantine", quarantine, "--grace", str(SUP_GRACE), "--",
            K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v1.py"), "run", item, "--rss-stop", str(cap)]
    sup_sha = K.sha_file(K.SUPERVISOR)
    rec = {"purpose": "run " + item, "launcher_pid": os.getpid(), "at": K.now(), "slot_rule": SLOT_RULE,
           "scan": scan, "free_bytes": fb, "admission": adm,
           "rss_cap": {"value": cap, "rule": "min(CAP_MAX, LANE_RSS_LIMIT - reserved - SAFETY_MARGIN)",
                       "CAP_MAX": K.CAP_MAX, "LANE_RSS_LIMIT": K.LANE_RSS_LIMIT, "SAFETY_MARGIN": K.SAFETY_MARGIN,
                       "MIN_CAP": K.MIN_CAP, "PROJECTED_PEAK": K.PROJECTED_PEAK,
                       "UNSUPERVISED_GROUP_RESERVE": K.UNSUPERVISED_GROUP_RESERVE,
                       "OTHER_LANE_MARGIN": K.OTHER_LANE_MARGIN, "reserved": scan.get("reserved_bytes")},
           "supervisor": {"path": K.SUPERVISOR, "sha256": sup_sha, "pin": K.SUPERVISOR_SHA256,
                          "equals_pin": sup_sha == K.SUPERVISOR_SHA256, "wall": SUP_WALL, "grace": SUP_GRACE,
                          "floor": K.FLOOR, "record": record, "quarantine": quarantine},
           "argv": argv, "cwd": K.TMP, "env": K.ENV, "scripts_sha256": K.script_hashes(),
           "regen_receipt_sha256": K.sha_file(regen_path), "selfcheck_summary_sha256": K.sha_file(summary_path)}
    if not adm["ok"] or sup_sha != K.SUPERVISOR_SHA256:
        rec["not_launched"] = "admission failed: %s / supervisor pin %s" % (adm["why"], sup_sha == K.SUPERVISOR_SHA256)
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
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=out_fd, stderr=subprocess.STDOUT, cwd=K.TMP,
                         env=K.ENV, start_new_session=True)
    STATE["child"] = p.pid
    os.write(logfd, (json.dumps({"at": started, "supervisor_pid": p.pid, "gate_sha256": gate_sha}) + "\n").encode())
    res = reap(p)
    STATE["child"] = None
    os.close(out_fd)
    outcome = {"item": item, "gate_receipt_sha256": gate_sha, "supervisor_started_at": started,
               "supervisor_finished_at": K.now(), "seconds": round(time.monotonic() - t0, 3), "supervisor": res,
               "launcher_signals": STATE["forwarded"],
               "supervisor_record_exists": os.path.exists(record),
               "supervisor_record_sha256": K.sha_file(record) if os.path.exists(record) else None,
               "quarantine_exists": os.path.lexists(quarantine),
               "supervisor_stdout_log_sha256": K.sha_file(stdout_log),
               "free_bytes_end": K.free_bytes()}
    h = K.write_json_x(outcome_path, outcome)
    os.write(logfd, (json.dumps({"at": K.now(), "outcome_sha256": h, "supervisor_rc": res["rc"]}) + "\n").encode())
    os.close(logfd)
    print(json.dumps({"outcome_sha256": h, "supervisor_rc": res["rc"], "seconds": outcome["seconds"],
                      "quarantine_exists": outcome["quarantine_exists"]}), flush=True)
    return 0


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("selfcheck", "run"):
        raise SystemExit(__doc__)
    if sys.argv[1] == "run" and (len(sys.argv) != 3 or sys.argv[2] not in K.ITEMS):
        raise SystemExit("usage: launch_B_v1.py run ITEM")
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    rc = mode_selfcheck() if sys.argv[1] == "selfcheck" else mode_run(sys.argv[2])
    sys.exit(rc)


if __name__ == "__main__":
    main()
