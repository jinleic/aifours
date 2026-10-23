#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v2.

v2 = launch_B_v1.py plus: (1) attempt labels: 'run ITEM --label LABEL' derives the gate receipt, outcome receipt,
supervisor record, quarantine path, supervisor stdout log and launcher log from LABEL, runs replay_B_v2.py with the
same LABEL, and refuses while any receipts/*.QUARANTINE.json exists; (2) Main's attempt-2 launch rule: in addition to
bklib_v1.admission, the slot must have been freed by the end of PhysEpQutrit's B/C411 r7 (slot 2) or of route B
C311 (slot 1); (3) a 'wait-start LABEL' watcher of this desk's own receipts, so the parent can be told when the
natives start. Pins, limits, supervisor arguments and the RSS-cap rule are unchanged. The v1 'selfcheck' mode is
dropped: attempt 2 reuses the attempt-1 self-check summary (same binaries, same bklib_v1 transport code).

Usage: launch_B_v2.py run ITEM --label ITEM-<suffix>
       launch_B_v2.py wait-start LABEL

run waits, with bounded sleeps of 90 s (never spinning), until a fresh lane scan and a fresh free-space reading admit a
native launch: <= 2 busy lane natives, lane RSS headroom for the projected peak, a computable RSS cap >= 2.5 GiB, free
bytes >= 12.2e9 + projected growth, before 15:30 PDT, and the slot condition above ('ended' = no live process of that
run now, and either seen live by this launcher or a new end record that appeared after this launcher started). If no
slot opens by 15:30 PDT, nothing is launched and the gate receipt records it. Then it requires receipts/regen-ITEM.json
= MATCH and receipts/selfcheck-summary.json all_ok, takes this desk's RSS cap from the fresh scan, writes the gate
receipt exclusively, runs the pinned supervise_r3.py (own session) around
'replay_B_v2.py run ITEM --label LABEL --rss-stop CAP', reaps it and writes an outcome receipt. A SIGTERM to this
launcher is forwarded to its supervisor child, which stops the group.
wait-start sleeps 60 s at a time until receipts/LABEL.launch.json or LABEL.driver.json exists, or LABEL.gate.json
records 'not_launched', then prints a summary; it never scans the lane and never touches lane files.
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

DEADLINE = datetime.datetime.fromisoformat("2026-10-18T15:30:00-07:00")
NO_LAUNCH_AFTER = datetime.datetime.fromisoformat("2026-10-18T17:00:00-07:00")
SLEEP = 90
SUP_WALL = 10200
SUP_GRACE = 180
ATTEMPT_RULE = ("Main message received about 05:00 PDT 2026-10-18: B/C321 attempt 1 UNKNOWN (external floor stop) "
                "accepted; prepare attempt 2 with new exclusive receipt/log/supervisor names and the same scripts, pins "
                "and limits (script changes as new versioned files). Slot 2 goes to PhysEpQutrit's B/C411 r7. Launch "
                "when a fresh lane scan shows <= 2 busy and that run has ended, or earlier if route B in slot 1 ends "
                "first and the lane shows <= 2 busy, with a fresh >= 12.2e9 gate plus growth. Unchanged: lane total RSS "
                "<= 8 GiB, <= 4 busy lane natives, floor 12e9, 15:30/17:00 PDT, a stop is UNKNOWN.")
B411_R7 = re.compile(r"B_C411|k3_direct_B_r\d+\.py C411")
END_FILES = {"b411_r7": os.path.join(K.K3DIR, "cert_B_r7", "B_C411.json"),
             "routeB": os.path.join(K.K3DIR, "C311cuts_B_r*.supervisor.json")}
STATE = {"child": None, "forwarded": [], "seen_live": {"b411_r7": False, "routeB": False}, "initial_end_files": None}


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


def end_files():
    return {k: sorted(p for p in glob.glob(g) if os.path.isfile(p)) for k, g in END_FILES.items()}


def slot_condition(scan):
    """Main's attempt-2 rule: B/C411 r7 (slot 2) has ended, or route B C311 (slot 1) has ended."""
    procs = scan.get("lane_natives", []) + scan.get("lane_processes", [])
    live = {"b411_r7": any(B411_R7.search(p.get("args", "")) for p in procs),
            "routeB": bool(scan.get("route_B_pids"))}
    files = end_files()
    if STATE["initial_end_files"] is None:
        STATE["initial_end_files"] = files
    new = {k: sorted(set(files[k]) - set(STATE["initial_end_files"][k])) for k in files}
    for k in live:
        STATE["seen_live"][k] = STATE["seen_live"][k] or live[k]
    ended = {k: (not live[k]) and (STATE["seen_live"][k] or bool(new[k])) for k in live}
    return {"live": live, "seen_live": dict(STATE["seen_live"]), "initial_end_files": STATE["initial_end_files"],
            "new_end_files": new, "ended": ended, "ok": ended["b411_r7"] or ended["routeB"]}


def admission_v2(scan, fb):
    adm = K.admission(scan, fb, deadline_ok())
    slot = slot_condition(scan)
    if "conditions" not in adm:
        return {"ok": False, "why": adm["why"], "slot": slot}
    cond = dict(adm["conditions"], slot_freed_by_b411_r7_or_routeB_end=slot["ok"])
    return {"ok": all(cond.values()), "conditions": cond, "why": [k for k, v in cond.items() if not v], "slot": slot}


def wait_for_admission(logfd, purpose):
    while True:
        scan = K.lane_scan(own_root=os.getpid())
        fb = K.free_bytes()
        adm = admission_v2(scan, fb)
        line = {"at": scan.get("at"), "purpose": purpose, "ok": adm["ok"], "why": adm["why"], "free_bytes": fb,
                "busy": scan.get("lane_native_busy"),
                "natives": [[n["pid"], os.path.basename(n["comm"])] for n in scan.get("lane_natives", [])],
                "lane_rss": scan.get("lane_rss_bytes"), "reserved": scan.get("reserved_bytes"),
                "cap": scan.get("computable_cap"), "live": adm["slot"]["live"], "ended": adm["slot"]["ended"],
                "new_end_files": adm["slot"]["new_end_files"]}
        os.write(logfd, (json.dumps(line) + "\n").encode())
        if adm["ok"] or not deadline_ok() or STATE["forwarded"]:
            return scan, fb, adm
        time.sleep(SLEEP)


def reap(p):
    pid, st, ru = os.wait4(p.pid, 0)
    p.returncode = os.waitstatus_to_exitcode(st)
    return {"pid": p.pid, "rc": p.returncode, "maxrss_bytes": ru.ru_maxrss, "user_seconds": round(ru.ru_utime, 3)}


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
    for pth in (gate_path, outcome_path, record, quarantine, stdout_log):
        if os.path.lexists(pth):
            raise SystemExit("exists: " + pth)
    prev_path = os.path.join(K.RECEIPTS, item + ".json")
    prev = json.loads(K.read_regular(prev_path)) if os.path.isfile(prev_path) else {}
    previous = {"label": item, "item_receipt": "receipts/%s.json" % item,
                "sha256": K.sha_file(prev_path) if os.path.isfile(prev_path) else None,
                "status": prev.get("status"), "stop_reason": (prev.get("stop") or {}).get("reason")}
    logfd = K.open_append_x(os.path.join(K.LOGS, "launch-run-%s.log" % label))
    scan, fb, adm = wait_for_admission(logfd, "run " + label)
    cap = scan.get("computable_cap")
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", label + "-parent-replay", "--wall", str(SUP_WALL),
            "--rss-cap", str(cap), "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", record,
            "--quarantine", quarantine, "--grace", str(SUP_GRACE), "--",
            K.PY, "-I", "-B", os.path.join(K.SCRIPTS, "replay_B_v2.py"), "run", item, "--label", label,
            "--rss-stop", str(cap)]
    sup_sha = K.sha_file(K.SUPERVISOR)
    rec = {"purpose": "run " + label, "item": item, "label": label, "previous_attempt": previous,
           "launcher_pid": os.getpid(), "at": K.now(), "attempt_rule": ATTEMPT_RULE,
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
    outcome = {"item": item, "label": label, "gate_receipt_sha256": gate_sha, "supervisor_started_at": started,
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
                               "ended": ((d.get("admission") or {}).get("slot") or {}).get("ended")})
            if k == "launch":
                out[k].update({"cnf_sha256": (d.get("regen") or {}).get("cnf_sha256"),
                               "binaries_at_spawn": {b: v.get("sha256")
                                                     for b, v in (d.get("binaries_at_spawn") or {}).items()},
                               "free_bytes": (d.get("gate_at_launch_receipt") or {}).get("free_bytes")})
    print(json.dumps(out), flush=True)
    return 0


def main():
    a = sys.argv[1:]
    if a and a[0] == "run":
        if (len(a) != 4 or a[1] not in K.ITEMS or a[2] != "--label"
                or not (re.fullmatch(r"[A-Za-z0-9_.-]+", a[3]) and a[3].startswith(a[1] + "-"))):
            raise SystemExit("usage: launch_B_v2.py run ITEM --label ITEM-<suffix>")
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_run(a[1], a[3]))
    if a and a[0] == "wait-start" and len(a) == 2 and re.fullmatch(r"[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_wait_start(a[1]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
