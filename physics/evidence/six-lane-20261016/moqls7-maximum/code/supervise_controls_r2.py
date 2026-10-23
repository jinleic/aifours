#!/usr/bin/env python3
"""supervise_controls_r2.py: controls for supervise_r2.py (expected outcomes below are design targets until run).

Runs as a plain top-level process, not under a supervisor: each test command gets its own process group, which an
outer supervisor would correctly report as an escape. Every test child is supervised by the supervisor under test,
in-process or as a separate supervisor process. All records and quarantine files go in this script's own directory,
evidence/k3cubes/supervise_controls_r2 (os.mkdir), never at the production quarantine path. New version of
supervise_controls_r1.py (0f61b466...01c5, preserved, never run); it adds S12-S13 for the fail-closed exception path.
Probe classification (P1-P9; deterministic fakes wrap the real proc_pidinfo):
  P1 the supervisor itself is alive with RSS > 0;  P2 an unreaped exited child is a zombie;  P3 after reaping it is
  gone;  P4 a short task-info read is unknown;  P5 a full task-info read with zero RSS is unknown;  P6 a short BSD
  read is unknown;  P7 EPERM on the BSD read is unknown;  P8 ESRCH on the BSD read is gone;  P9 a pid mismatch is
  unknown;  P10 a task-info failure followed by a zombie BSD re-read with the same start time is zombie (exit race).
  The pid-1 probe result is recorded for information only.
Supervision (S1-S13):
  S1 a clean short command completes cleanly;  S2 the wall cap stops the leader (rc -15);  S3 a short command still
  meets the completion check: a floor above the free space trips;  S4 injected RSS above the cap trips and stops;
  S5 an injected unknown probe trips as uncertain, stops the group and writes a capacity quarantine with no
  survivors;  S6 a re-parented grandchild that ignores SIGTERM is listed with ppid 1, survives the grace period, is
  quarantined and exits by itself;  S7 a re-parented grandchild that obeys SIGTERM is stopped through the reserved
  group ID with no quarantine;  S8 a child that leaves the group is detected as uncertain, is not signalled, is
  quarantined and exits by itself;  S9 external SIGTERM to a separate supervisor process stops its leader (rc -15)
  and exits 3;  S10 an existing quarantine record refuses admission;  S11 the driver r4 refuses to run unsupervised
  and creates nothing;  S12 a real statvfs exception inside the loop (nonexistent lane path) still SIGTERMs the
  reserved group (leader rc -15), records UNKNOWN as uncertain and writes a capacity quarantine;  S13 a probe that
  raises a real exception (not an unknown return) inside the loop and again during the stop takes the fallback: one
  killpg, a bounded unmeasured wait, survivors unknown, quarantine, leader rc -15, record written.
Usage: /usr/bin/python3 -I -B supervise_controls_r2.py
"""
import ctypes
import errno
import json
import os
import signal
import struct
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import supervise_r2 as sv  # noqa: E402

LANE = os.path.dirname(HERE)
K3DIR = os.path.join(LANE, "evidence", "k3cubes")
OUT = os.path.join(K3DIR, "supervise_controls_r2.json")
TEST_DIR = os.path.join(K3DIR, "supervise_controls_r2")
RSS_CAP, FLOOR = 3584 * 1024 * 1024, 12000000000
REAL = sv.LIBPROC.proc_pidinfo


def fake(mode):
    def pidinfo(pid, flavor, arg, buf, size):
        if mode == "bsd_eperm" and flavor == sv.PROC_PIDTBSDINFO:
            ctypes.set_errno(errno.EPERM)
            return 0
        if mode == "bsd_esrch" and flavor == sv.PROC_PIDTBSDINFO:
            ctypes.set_errno(errno.ESRCH)
            return 0
        n = REAL(pid, flavor, arg, buf, size)
        if mode == "task_short" and flavor == sv.PROC_PIDTASKINFO:
            return 48
        if mode == "task_zero_rss" and flavor == sv.PROC_PIDTASKINFO:
            buf[8:16] = b"\0" * 8
            return n
        if mode == "bsd_short" and flavor == sv.PROC_PIDTBSDINFO:
            return 100
        if mode == "pid_mismatch" and flavor == sv.PROC_PIDTBSDINFO:
            buf[12:16] = struct.pack("=I", pid + 1)
            return n
        if mode == "exit_race":
            if flavor == sv.PROC_PIDTASKINFO:
                ctypes.set_errno(errno.ESRCH)
                return 0
            state = pidinfo.calls = getattr(pidinfo, "calls", 0) + 1
            if state >= 2:
                buf[4:8] = struct.pack("=I", sv.SZOMB)
            return n
        return n
    return pidinfo


def probe_controls():
    out = {}
    state, rss, _ = sv.probe(os.getpid())
    out["P1_self_alive"] = {"state": state, "rss": rss, "ok": state == "alive" and rss > 0}
    child = subprocess.Popen(["/usr/bin/true"])
    deadline, state = time.monotonic() + 5, None
    while time.monotonic() < deadline:
        state = sv.probe(child.pid)[0]
        if state == "zombie":
            break
        time.sleep(0.05)
    out["P2_unreaped_exit_is_zombie"] = {"state": state, "ok": state == "zombie"}
    child.wait()
    state = sv.probe(child.pid)[0]
    out["P3_reaped_is_gone"] = {"state": state, "ok": state == "gone"}
    expected = {"P4_task_short": ("task_short", "unknown"), "P5_task_zero_rss": ("task_zero_rss", "unknown"),
                "P6_bsd_short": ("bsd_short", "unknown"), "P7_bsd_eperm": ("bsd_eperm", "unknown"),
                "P8_bsd_esrch": ("bsd_esrch", "gone"), "P9_pid_mismatch": ("pid_mismatch", "unknown"),
                "P10_exit_race_zombie": ("exit_race", "zombie")}
    for label, (mode, wanted) in expected.items():
        state, rss, ident = sv.probe(os.getpid(), pidinfo=fake(mode))
        out[label] = {"mode": mode, "state": state, "rss": rss, "expected": wanted, "ok": state == wanted and rss == 0}
    state, rss, ident = sv.probe(1)
    out["info_pid1"] = {"state": state, "identity": ident, "ok": True, "note": "information only"}
    return out


def alive(pid):
    return sv.probe(pid)[0] == "alive"


def run(name, command, wall=30, floor=FLOOR, grace=5.0, probe_fn=sv.probe, lane=LANE):
    record = os.path.join(TEST_DIR, name + ".record.json")
    quarantine = os.path.join(TEST_DIR, name + ".quarantine.json")
    rec = sv.supervise(command, name, wall, RSS_CAP, floor, lane, record, quarantine, grace, probe_fn=probe_fn)
    rec["record_exists"] = os.path.exists(record)
    rec["quarantine_exists"] = os.path.exists(quarantine)
    return rec


def wait_gone(pids, seconds):
    deadline = time.monotonic() + seconds
    while any(alive(p) for p in pids) and time.monotonic() < deadline:
        time.sleep(0.25)
    return not any(alive(p) for p in pids)


def supervision_controls():
    out = {}
    r = run("s1_clean", ["/usr/bin/true"])
    out["S1_clean_completion"] = {"record": r, "ok": r["completed_cleanly"] and r["trip_reason"] is None
                                  and not r["quarantine_exists"] and r["final_check"] is not None}
    r = run("s2_wall", ["/bin/sleep", "30"], wall=2)
    out["S2_wall_trip"] = {"record": r, "ok": str(r["trip_reason"]).startswith("wall cap") and r["leader_returncode"] == -15
                           and not r["uncertain"] and not r["quarantine_exists"] and r["stop"]["survivors"] == []}
    st = os.statvfs(LANE)
    r = run("s3_short_floor", ["/usr/bin/true"], floor=st.f_bavail * st.f_frsize + 10 ** 15)
    out["S3_short_command_checked"] = {"record": r, "ok": "below floor" in str(r["trip_reason"])
                                       and not r["completed_cleanly"]}

    def big(pid, pidinfo=None):
        state, rss, ident = sv.probe(pid)
        return (state, 10 ** 13, ident) if state == "alive" and pid != os.getpid() else (state, rss, ident)
    r = run("s4_rss", ["/bin/sleep", "30"], probe_fn=big)
    out["S4_rss_trip"] = {"record": r, "ok": str(r["trip_reason"]).startswith("aggregate RSS")
                          and r["leader_returncode"] == -15 and not r["quarantine_exists"]}

    calls = {"n": 0}

    def flaky(pid, pidinfo=None):
        state, rss, ident = sv.probe(pid)
        if pid != os.getpid():
            calls["n"] += 1
            if calls["n"] > 3:
                return "unknown", 0, dict(ident, injected="unknown")
        return state, rss, ident
    r = run("s5_unknown", ["/bin/sleep", "30"], probe_fn=flaky)
    out["S5_unknown_probe_quarantines"] = {"record": r, "ok": str(r["trip_reason"]).startswith("unknown probe")
                                           and r["uncertain"] and r["quarantine_exists"]
                                           and r["leader_returncode"] == -15}

    r = run("s6_reparent_survivor", ["/bin/sh", "-c", "(trap '' TERM; exec /bin/sleep 6) & exit 0"], grace=3.0)
    survivors = [s["pid"] for s in (r["stop"] or {}).get("survivors", [])]
    reparented = any(s["identity"].get("ppid") == 1 for s in (r["stop"] or {}).get("survivors", []))
    exited = wait_gone(survivors, 20)
    out["S6_reparented_survivor_quarantined"] = {
        "record": r, "survivors": survivors, "survivors_reparented_to_pid1": reparented,
        "survivors_exited_by_themselves": exited,
        "ok": "alive after leader exit" in str(r["trip_reason"]) and len(survivors) >= 1 and reparented
              and r["quarantine_exists"] and exited}

    r = run("s7_reparent_stopped", ["/bin/sh", "-c", "/bin/sleep 30 & exit 0"])
    out["S7_reparented_member_stopped"] = {"record": r, "ok": "alive after leader exit" in str(r["trip_reason"])
                                           and r["stop"]["survivors"] == [] and r["stop"]["sigterm_sent"]
                                           and not r["quarantine_exists"] and not r["uncertain"]}

    r = run("s8_escape", ["/usr/bin/python3", "-c",
                          "import subprocess, time\n"
                          "subprocess.Popen(['/bin/sleep', '6'], start_new_session=True)\n"
                          "time.sleep(4)\n"])
    escaped = [int(p) for p, ident in r["observed_identities"].items() if ident.get("comm") == "sleep"]
    exited = wait_gone(escaped, 20)
    out["S8_escape_detected_not_signalled"] = {
        "record": r, "escaped_pids": escaped, "escaped_exited_by_themselves": exited,
        "ok": "left the supervised process group" in str(r["trip_reason"]) and r["uncertain"]
              and r["quarantine_exists"] and len(escaped) == 1 and exited}

    record = os.path.join(TEST_DIR, "s9_external.record.json")
    quarantine = os.path.join(TEST_DIR, "s9_external.quarantine.json")
    proc = subprocess.Popen(["/usr/bin/python3", "-I", "-B", os.path.join(HERE, "supervise_r2.py"), "--name", "s9",
                             "--wall", "60", "--rss-cap", str(RSS_CAP), "--floor", str(FLOOR), "--lane", LANE,
                             "--record", record, "--quarantine", quarantine, "--grace", "5", "--", "/bin/sleep", "30"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1.5)
    os.kill(proc.pid, signal.SIGTERM)
    deadline = time.monotonic() + 40
    while proc.poll() is None and time.monotonic() < deadline:
        time.sleep(0.1)
    stdout, stderr = proc.communicate() if proc.returncode is not None else (b"", b"")
    r = json.load(open(record)) if os.path.exists(record) else {}
    out["S9_external_sigterm"] = {"record": r, "exit_code": proc.returncode,
                                  "stderr_tail": stderr[-300:].decode("utf-8", "replace"),
                                  "ok": r.get("trip_reason") == "external SIGTERM" and r.get("leader_returncode") == -15
                                  and proc.returncode == 3 and not os.path.exists(quarantine)}

    blocked = os.path.join(TEST_DIR, "s10_existing.quarantine.json")
    with open(blocked, "x") as f:
        f.write("{}\n")
    try:
        sv.supervise(["/usr/bin/true"], "s10", 30, RSS_CAP, FLOOR, LANE, os.path.join(TEST_DIR, "s10.record.json"),
                     blocked)
        refused = False
    except SystemExit as exc:
        refused = "admission refused" in str(exc)
    out["S10_quarantine_refuses_admission"] = {"refused": refused,
                                               "record_absent": not os.path.exists(os.path.join(TEST_DIR, "s10.record.json")),
                                               "ok": refused and not os.path.exists(os.path.join(TEST_DIR, "s10.record.json"))}

    before = sorted(n for n in os.listdir(K3DIR) if n.startswith("C311cuts_"))
    drv = subprocess.run(["/usr/bin/python3", "-I", "-B", os.path.join(HERE, "k3_cuts_certify_r4.py"), "A"],
                         stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    after = sorted(n for n in os.listdir(K3DIR) if n.startswith("C311cuts_"))
    message = (drv.stdout + drv.stderr).decode("utf-8", "replace")
    out["S11_driver_refuses_unsupervised"] = {"returncode": drv.returncode, "message_tail": message[-300:],
                                              "created": [n for n in after if n not in before],
                                              "ok": drv.returncode != 0 and "under the pinned supervise_r2.py" in message
                                              and after == before}

    r = run("s12_statvfs_exception", ["/bin/sleep", "30"], lane=os.path.join(TEST_DIR, "no-such-lane"))
    out["S12_statvfs_exception_fails_closed"] = {
        "record": r, "ok": str(r["trip_reason"]).startswith("supervisor exception") and r["uncertain"]
        and r["quarantine_exists"] and r["record_exists"] and r["leader_returncode"] == -15
        and r["stop"]["survivors"] == [] and r["stop_error"] is None}

    calls = {"n": 0}

    def raising(pid, pidinfo=None):
        calls["n"] += 1
        if calls["n"] > 6:
            raise RuntimeError("injected probe exception")
        return sv.probe(pid)
    r = run("s13_probe_exception", ["/bin/sh", "-c", "trap '' TERM; exec /bin/sleep 8"], grace=2.0, probe_fn=raising)
    leader_exited = wait_gone([r["leader_pid"]], 20) if r.get("leader_pid") else False
    out["S13_probe_exception_fallback"] = {
        "record": r, "leader_exited_by_itself": leader_exited,
        "ok": str(r["trip_reason"]).startswith("supervisor exception") and r["uncertain"]
        and r["quarantine_exists"] and r["record_exists"] and r["leader_returncode"] is None
        and r["stop_error"] is not None and r["stop"]["survivors"] == "unknown: stop measurement failed"
        and leader_exited}
    return out


def main():
    if os.path.exists(OUT):
        raise FileExistsError(OUT)
    os.mkdir(TEST_DIR)
    t0 = time.monotonic()
    rec = {"started_at": sv.now(), "controls_sha256": sv.sha(os.path.abspath(__file__)),
           "supervisor_sha256": sv.sha(os.path.join(HERE, "supervise_r2.py")),
           "executable": sys.executable, "version": sys.version, "isolated": bool(sys.flags.isolated),
           "design_note": "Signals go only to the supervised group while its leader is unreaped (the group ID is "
                          "reserved by the zombie leader); escaped processes are never signalled. PID reuse is "
                          "excluded by construction, not tested."}
    failures = []
    try:
        rec["probe_controls"] = probe_controls()
        rec["supervision_controls"] = supervision_controls()
        for group in ("probe_controls", "supervision_controls"):
            failures.extend("%s:%s" % (group, k) for k, v in rec[group].items() if not v["ok"])
    except Exception as exc:
        failures.append("exception: %r" % (exc,))
    rec.update({"status": "PASS" if not failures else "FAIL", "failures": failures, "finished_at": sv.now(),
                "seconds": round(time.monotonic() - t0, 3)})
    with open(OUT, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "failures": failures, "seconds": rec["seconds"]}))
    print("receipt_sha256", sv.sha(OUT))


if __name__ == "__main__":
    main()
