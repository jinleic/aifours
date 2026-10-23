#!/usr/bin/env python3
"""Capacity-gated launcher of the parent B-side K3 cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v4.

v4 = launch_B_v3.py with one change, the launcher's signal handling (Main's source review, about 05:16 PDT):
  * on_term is flag-only: it records the signal and never signals any PID;
  * run_owned() spawns the supervisor and owns it in a wait loop. The flag is checked first in every iteration,
    starting immediately after the child is registered, so a signal that arrived while Popen ran is forwarded in
    the first iteration. SIGTERM is forwarded only while the child is owned, i.e. not yet reaped. An exited child
    stays a zombie until this loop reaps it, so its PID cannot be recycled. Ownership is cleared at the same
    control-flow point as the successful wait4, and nothing is signalled after it;
  * any exception after Popen forwards SIGTERM to the still-owned child and waits a bounded SUP_GRACE + 120 s for it;
    an attempt stopped this way stays UNKNOWN;
  * a signal that races Popen yields a prompt cooperative stop and an UNKNOWN attempt; it does not guarantee that
    no supervisor process was created;
  * a 'smoke-signal LABEL' mode, a targeted smoke of the signal intervals around a harmless '/bin/sleep 117' under
    the pinned supervisor (no solver, checker or CNF).
v3 (unchanged here): attempt 2 owns lane SLOT 2 ONLY, after PhysEpQutrit's B/C411 r7 is fully reaped and
end-recorded. That means no live lane process of B/C411 r7 (driver or natives) in a fresh scan AND
evidence/k3cubes/cert_B_r7/B_C411.json exists as a regular file; a low busy count alone never admits. A signal
received before launch prevents the launch. Labels, refusal while any receipts/*.QUARANTINE.json exists, the
wait-start watcher, pins, limits, supervisor arguments and the RSS-cap rule are as in v2/v3.

Usage: launch_B_v4.py run ITEM --label ITEM-<suffix>
       launch_B_v4.py wait-start LABEL
       launch_B_v4.py smoke-signal LABEL

run waits, with bounded sleeps of 90 s (never spinning), until a fresh lane scan and a fresh free-space reading admit a
native launch: the slot-2 condition above AND <= 2 busy lane natives, lane RSS headroom for the projected peak, a
computable RSS cap >= 2.5 GiB, free bytes >= 12.2e9 + projected growth, before 15:30 PDT. If no slot opens by then,
nothing is launched and the gate receipt records it. Then it requires receipts/regen-ITEM.json = MATCH and
receipts/selfcheck-summary.json all_ok, takes this desk's RSS cap from the fresh scan, writes the gate receipt
exclusively, runs the pinned supervise_r3.py (own session) around
'replay_B_v2.py run ITEM --label LABEL --rss-stop CAP' through run_owned(), and writes an outcome receipt.
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
ATTEMPT_RULE = ("Main messages about 05:00 and 05:10 PDT 2026-10-18: B/C321 attempt 1 UNKNOWN (external floor stop) "
                "accepted; attempt 2 uses new exclusive names and the same scripts, pins and limits. Scheduling "
                "correction: slot 1 remains PhysEpQutrit's (route B r6, then route A r7); attempt 2 owns SLOT 2 ONLY, "
                "after B/C411 r7 is fully reaped/end-recorded; the 'or route B ends first' permission is withdrawn; do "
                "not act on a merely low busy count. Fresh >= 12.2e9 gate plus growth. Unchanged: lane total RSS <= "
                "8 GiB, <= 4 busy lane natives, floor 12e9, 15:30/17:00 PDT, a stop is UNKNOWN.")
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


def run_owned(argv, out_fd, inject=None):
    """Spawn one child in its own session and own it until this function reaps it (see the module docstring)."""
    ev = {"argv0": argv[0], "pid": None, "spawned_at": None, "forwarded": [], "reaped": None, "exception": None,
          "lost_child": None, "stop_wait": None}
    t0 = time.monotonic()
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=out_fd, stderr=subprocess.STDOUT, cwd=K.TMP,
                         env=K.ENV, start_new_session=True)
    if inject is not None:
        inject()                                    # smoke only: a signal inside the spawn/registration interval
    owned = p.pid                                   # registration
    ev.update(pid=owned, spawned_at=K.now())

    def try_reap():
        nonlocal owned
        try:
            pid, st, ru = os.wait4(owned, os.WNOHANG)
        except ChildProcessError as e:              # not our unreaped child any more: never signal it
            owned = None
            ev["lost_child"] = repr(e)
            return True
        if pid:
            owned = None                            # ownership cleared with the successful wait4
            p.returncode = os.waitstatus_to_exitcode(st)
            ev["reaped"] = {"at": K.now(), "rc": p.returncode, "maxrss_bytes": ru.ru_maxrss,
                            "user_seconds": round(ru.ru_utime, 3),
                            "after_spawn_seconds": round(time.monotonic() - t0, 3)}
            return True
        return False

    iteration = 0
    try:
        while owned is not None:
            iteration += 1
            if STATE["signals"] and not ev["forwarded"]:
                os.kill(owned, signal.SIGTERM)      # owned => unreaped => PID reserved
                ev["forwarded"].append({"at": K.now(), "after_spawn_seconds": round(time.monotonic() - t0, 3),
                                        "iteration": iteration, "signals_seen": len(STATE["signals"])})
            if try_reap():
                break
            time.sleep(POLL)
    except BaseException as exc:
        ev["exception"] = repr(exc)
        if owned is not None:
            try:
                os.kill(owned, signal.SIGTERM)
                ev["forwarded"].append({"at": K.now(), "why": "exception after Popen"})
            except OSError as e:
                ev["forwarded"].append({"at": K.now(), "why": "exception after Popen", "error": repr(e)})
            deadline = time.monotonic() + STOP_WAIT
            while owned is not None and time.monotonic() < deadline:
                if try_reap():
                    break
                time.sleep(POLL)
            ev["stop_wait"] = {"bounded_seconds": STOP_WAIT, "unreaped_after_wait": owned is not None}
    ev["owned_at_return"] = owned
    return ev


def slot_condition(scan):
    """Main's corrected rule: slot 2 is free only when B/C411 r7 is fully reaped AND end-recorded."""
    procs = scan.get("lane_natives", []) + scan.get("lane_processes", [])
    live = any(B411_R7.search(p.get("args", "")) for p in procs) or "error" in scan
    STATE["seen_live"] = STATE["seen_live"] or (live and "error" not in scan)
    st = os.lstat(B411_R7_END_RECORD) if os.path.lexists(B411_R7_END_RECORD) else None
    recorded = st is not None and (st.st_mode & 0o170000) == 0o100000
    return {"b411_r7_live": live, "b411_r7_seen_live": STATE["seen_live"], "end_record": B411_R7_END_RECORD,
            "end_record_exists": recorded, "ok": (not live) and recorded}


def admission_v2(scan, fb):
    adm = K.admission(scan, fb, deadline_ok())
    slot = slot_condition(scan)
    if "conditions" not in adm:
        return {"ok": False, "why": adm["why"], "slot": slot}
    cond = dict(adm["conditions"], slot2_b411_r7_reaped_and_end_recorded=slot["ok"])
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
                "cap": scan.get("computable_cap"), "b411_r7_live": adm["slot"]["b411_r7_live"],
                "b411_r7_end_record_exists": adm["slot"]["end_record_exists"]}
        os.write(logfd, (json.dumps(line) + "\n").encode())
        if adm["ok"] or not deadline_ok() or STATE["signals"]:
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
    ev = run_owned(argv, out_fd)
    os.close(out_fd)
    os.write(logfd, (json.dumps({"at": started, "supervisor_pid": ev["pid"], "gate_sha256": gate_sha}) + "\n").encode())
    outcome = {"item": item, "label": label, "gate_receipt_sha256": gate_sha, "supervisor_started_at": started,
               "supervisor_finished_at": K.now(), "seconds": round(time.monotonic() - t0, 3), "owned_child": ev,
               "supervisor": {"pid": ev["pid"], "rc": (ev["reaped"] or {}).get("rc")},
               "launcher_signals": STATE["signals"],
               "stopped_by_launcher": bool(ev["forwarded"]),
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
                      "stopped_by_launcher": outcome["stopped_by_launcher"],
                      "quarantine_exists": outcome["quarantine_exists"]}), flush=True)
    return 0 if ev["exception"] is None and ev["owned_at_return"] is None else 3


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


SMOKE_ARGS = "/bin/sleep 117"


def sleep_survivors():
    out = subprocess.run(["/bin/ps", "-axww", "-o", "pid=,ppid=,pgid=,args="], stdin=subprocess.DEVNULL,
                         capture_output=True, text=True, env=K.ENV, cwd=K.TMP).stdout
    rows = [ln.split(None, 3) for ln in out.splitlines()]
    return [r for r in rows if len(r) == 4 and r[3].strip() == SMOKE_ARGS]


def mode_smoke(label):
    """Targeted signal-interval smoke (no solver, checker or CNF). Case A: a real SIGTERM to this launcher inside the
    spawn/registration interval of run_owned(), around the pinned supervisor and '/bin/sleep 117'. Expected: flag set,
    SIGTERM forwarded exactly once to the owned child in the first loop iteration, the supervisor exits and is reaped,
    no sleep survivor, no quarantine. Case B: a SIGTERM after the reap. Expected: a recorded flag only, no os.kill of
    any PID other than this process's own self-signal."""
    paths = {"receipt": os.path.join(K.RECEIPTS, label + ".smoke.json"),
             "record": os.path.join(K.RECEIPTS, label + ".supervisor.json"),
             "quarantine": os.path.join(K.RECEIPTS, label + ".QUARANTINE.json"),
             "stdout": os.path.join(K.LOGS, label + ".supervisor-stdout.log")}
    for p in paths.values():
        if os.path.lexists(p):
            raise SystemExit("exists: " + p)
    if sleep_survivors():
        raise SystemExit("a '%s' process already exists; smoke not run" % SMOKE_ARGS)
    argv = [K.PY, "-I", "-B", K.SUPERVISOR, "--name", label, "--wall", "120", "--rss-cap", str(512 * 1024 * 1024),
            "--floor", str(K.FLOOR), "--lane", K.DESK, "--record", paths["record"], "--quarantine", paths["quarantine"],
            "--grace", "30", "--"] + SMOKE_ARGS.split()
    kills, real_kill, t0 = [], os.kill, time.monotonic()

    def logged_kill(pid, sig):
        kills.append({"pid": pid, "signal": signal.Signals(sig).name, "self": pid == os.getpid(),
                      "t": round(time.monotonic() - t0, 4)})
        real_kill(pid, sig)

    os.kill = logged_kill
    try:
        out_fd = K.open_append_x(paths["stdout"])
        ev_a = run_owned(argv, out_fd, inject=lambda: os.kill(os.getpid(), signal.SIGTERM))
        os.close(out_fd)
        n_a, kills_a = len(STATE["signals"]), list(kills)
        os.kill(os.getpid(), signal.SIGTERM)        # case B: after the reap
        time.sleep(1.0)
        n_b = len(STATE["signals"])
    finally:
        os.kill = real_kill
    kills_b = kills[len(kills_a):]
    survivors = sleep_survivors()
    child_kills = [k for k in kills_a if not k["self"]]
    fw = ev_a["forwarded"]
    checks = {
        "A_self_signal_in_spawn_window": any(k["self"] for k in kills_a) and n_a >= 1,
        "A_forwarded_exactly_once_to_owned_child": (len(child_kills) == 1 and len(fw) == 1
                                                    and child_kills[0]["pid"] == ev_a["pid"]),
        "A_forwarded_in_first_iteration": bool(fw) and fw[0].get("iteration") == 1,
        "A_child_reaped_after_forward": (ev_a["reaped"] is not None and ev_a["owned_at_return"] is None
                                         and ev_a["exception"] is None and ev_a["lost_child"] is None),
        "A_no_sleep_survivor": not survivors,
        "A_no_quarantine": not os.path.lexists(paths["quarantine"]),
        "B_post_reap_signal_is_flag_only": n_b == n_a + 1 and len(kills_b) == 1 and kills_b[0]["self"],
    }
    record = json.loads(K.read_regular(paths["record"])) if os.path.exists(paths["record"]) else None
    out = {"label": label, "at": K.now(), "argv": argv, "case_A": ev_a, "kills_A": kills_a, "kills_B": kills_b,
           "signals": STATE["signals"], "sleep_survivors": survivors,
           "supervisor_record": ({k: record.get(k) for k in ("trip_reason", "uncertain", "stop", "leader_returncode",
                                                             "quarantine_record", "completed_cleanly",
                                                             "observed_identities")} if record else None),
           "supervisor_record_sha256": K.sha_file(paths["record"]) if record else None,
           "supervisor_stdout_sha256": K.sha_file(paths["stdout"]),
           "note": ("rc -15 means the forwarded SIGTERM reached the supervisor before it installed its handler (it "
                    "had not spawned its command); rc 3 means its own group stop. Either is a prompt cooperative "
                    "stop; a real attempt stopped this way is UNKNOWN."),
           "checks": checks, "all_ok": all(checks.values()), "scripts_sha256": K.script_hashes()}
    h = K.write_json_x(paths["receipt"], out)
    print(json.dumps({"smoke_receipt_sha256": h, "all_ok": out["all_ok"], "checks": checks,
                      "supervisor_rc": (ev_a["reaped"] or {}).get("rc"), "record_written": record is not None}),
          flush=True)
    return 0 if out["all_ok"] else 1


def main():
    a = sys.argv[1:]
    if a and a[0] == "run":
        if (len(a) != 4 or a[1] not in K.ITEMS or a[2] != "--label"
                or not (re.fullmatch(r"[A-Za-z0-9_.-]+", a[3]) and a[3].startswith(a[1] + "-"))):
            raise SystemExit("usage: launch_B_v4.py run ITEM --label ITEM-<suffix>")
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_run(a[1], a[3]))
    if a and a[0] == "wait-start" and len(a) == 2 and re.fullmatch(r"[A-Za-z0-9_.-]+", a[1]):
        sys.exit(mode_wait_start(a[1]))
    if a and a[0] == "smoke-signal" and len(a) == 2 and re.fullmatch(r"smoke-[A-Za-z0-9_.-]+", a[1]):
        signal.signal(signal.SIGTERM, on_term)
        signal.signal(signal.SIGINT, on_term)
        sys.exit(mode_smoke(a[1]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
