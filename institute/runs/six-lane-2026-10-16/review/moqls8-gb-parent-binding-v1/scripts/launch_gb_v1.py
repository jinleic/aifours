#!/usr/bin/env python3
"""Single-run launcher for scripts/bind_gb_v1.py (desk moqls8-gb-parent-binding-v1), stdlib only, v1.

Usage (environment exactly TMPDIR=<desk>/tmp/launch-v1/):
  /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B <desk>/scripts/launch_gb_v1.py BIND_SHA256
Refuses (writes receipts/LAUNCH-REFUSED-<HHMMSS>.json, starts nothing) unless the bind script's sha256 equals
BIND_SHA256, local time is before 17:30 PDT 2026-10-18 and a fresh free-space reading is >= 12.2e9 B + 2 MB
projected growth (frozen launch gate). Otherwise: creates tmp/gen-v1 (must not exist), writes
receipts/PRE-EXEC.v1.json (exclusive; must not exist) with both script hashes BEFORE the child starts, then starts
ONE child  <interpreter> -I -B <desk>/scripts/bind_gb_v1.py BIND_SHA256  with env {TMPDIR=<desk>/tmp/gen-v1/,
PATH=/usr/bin:/bin}, stdin /dev/null, stdout/stderr to receipts/bind_gb_v1.std{out,err}.log (exclusive).
Supervision: os.wait4(WNOHANG) every 1 s, free-space reading every 10 s. The child is stopped ONLY by SIGTERM
(in-flight free < 12e9 B, wall > 2700 s + 15 s grace when the child's own 2700 s abort has not ended it, or a
SIGTERM received by this launcher), followed by a bounded 120 s wait that is never escalated. Finally writes
receipts/POST-EXEC.v1.json (exclusive) with exit status, child rusage, output and log hashes and the verdict.
"""
import datetime
import hashlib
import json
import os
import signal
import subprocess
import sys
import time

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1"
BIND = DESK + "/scripts/bind_gb_v1.py"
LAUNCHER = DESK + "/scripts/launch_gb_v1.py"
TMP_LAUNCH = DESK + "/tmp/launch-v1"
TMP_GEN = DESK + "/tmp/gen-v1"
PRE = DESK + "/receipts/PRE-EXEC.v1.json"
POST = DESK + "/receipts/POST-EXEC.v1.json"
OUT_LOG = DESK + "/receipts/bind_gb_v1.stdout.log"
ERR_LOG = DESK + "/receipts/bind_gb_v1.stderr.log"
OUTPUTS = {"manifest": DESK + "/GBBINDING.json", "primary_map": DESK + "/GB-PRIMARY-MAP.v1.txt",
           "child_stop_record": DESK + "/receipts/CHILD-ABORT.v1.json",
           "selftest_receipt": DESK + "/receipts/SELFTEST.v1.json", "static_notes": DESK + "/STATIC-NOTES.md"}
INTERPRETER = "/opt/homebrew/opt/python@3.14/bin/python3.14"
GROWTH = 2_000_000
GATE = 12_200_000_000 + GROWTH
FLOOR = 12_000_000_000
WALL = 2700.0
GRACE = 15.0
TERM_WAIT = 120.0
FREE_PERIOD = 10.0
POLL = 1.0
RSS_LIMIT = 1 << 30
PARENT_AUTHORITY = [
    "GO (Main IRC, received between 07:05 and 07:10:17 PDT): 'GO for your single generation run as soon as your "
    "script is frozen and pinned: the M8 lane is idle of native work now ... Keep <=1 GiB RSS, one CPU, 2700 s "
    "wall, fresh free-space gate >=12.2e9 B ... If the 12e9 floor trips mid-run, stop cooperatively, record "
    "UNKNOWN, and report.'",
    "Clarification (Main IRC, ~07:17-07:23 PDT): in-memory Python job with a small manifest may run while free is "
    "between 12.0e9 and 12.2e9 B; stop cooperatively below 11.5e9 B (the child's internal backstop values).",
    "Update (Main IRC 07:19 PDT): native work resumes under the frozen gates (fresh >=12.2e9 B + growth, in-flight "
    "12e9 floor); this launcher enforces those stricter values.",
]
STATE = {"launcher_sigterm": False}


def on_sigterm(signum, frame):
    STATE["launcher_sigterm"] = True


def sha_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def now():
    return datetime.datetime.now().astimezone()


def free_bytes():
    st = os.statvfs(DESK)
    return st.f_bavail * st.f_frsize


def write_x(path, obj):
    data = (json.dumps(obj, indent=1) + "\n").encode("utf-8")
    with open(path, "xb") as f:
        f.write(data)
    return hashlib.sha256(data).hexdigest()


def refuse(reason, info):
    t = now()
    path = DESK + "/receipts/LAUNCH-REFUSED-%s.json" % t.strftime("%H%M%S")
    write_x(path, {"schema": "moqls8-gb-launch-refused/1", "at": t.isoformat(timespec="seconds"), "reason": reason,
                   "child_started": False, **info})
    print("REFUSED: %s (%s)" % (reason, path), flush=True)
    return 5


def file_info(path):
    if not os.path.lexists(path):
        return None
    return {"path": path, "sha256": sha_file(path), "bytes": os.path.getsize(path)}


def main(argv):
    signal.signal(signal.SIGTERM, on_sigterm)
    if len(argv) != 2 or len(argv[1]) != 64:
        print(__doc__, flush=True)
        return 4
    expected = argv[1]
    if os.environ.get("TMPDIR") != TMP_LAUNCH + "/" or not os.path.isdir(TMP_LAUNCH):
        print("TMPDIR must be %s/ (existing)" % TMP_LAUNCH, flush=True)
        return 4
    os.chdir(TMP_LAUNCH)
    if os.path.realpath(__file__) != LAUNCHER:
        print("launcher path %s != %s" % (os.path.realpath(__file__), LAUNCHER), flush=True)
        return 4
    bind_sha, launcher_sha = sha_file(BIND), sha_file(LAUNCHER)
    t = now()
    stop = t.replace(year=2026, month=10, day=18, hour=17, minute=30, second=0, microsecond=0)
    fb = free_bytes()
    info = {"bind_script_sha256": bind_sha, "expected_bind_sha256": expected, "launcher_sha256": launcher_sha,
            "free_bytes_fresh": fb, "gate_bytes": GATE}
    if bind_sha != expected:
        return refuse("bind script sha256 differs from the pinned value", info)
    if t.utcoffset() != datetime.timedelta(hours=-7) or t >= stop:
        return refuse("outside the launch window (PDT, before 17:30 on 2026-10-18)", info)
    if fb < GATE:
        return refuse("fresh free %d B < launch gate %d B" % (fb, GATE), info)
    if os.path.lexists(PRE) or os.path.lexists(POST):
        print("PRE-EXEC/POST-EXEC already exist: the single run was already launched", flush=True)
        return 4
    os.mkdir(TMP_GEN)
    child_argv = [INTERPRETER, "-I", "-B", BIND, bind_sha]
    env = {"TMPDIR": TMP_GEN + "/", "PATH": "/usr/bin:/bin"}
    pre = {"schema": "moqls8-gb-parent-binding-pre-exec/1", "written_at": now().isoformat(timespec="seconds"),
           "desk": DESK, "purpose": "single in-memory GB generation/binding run (no CNF or proof bytes on disk, no "
                                    "native tool, one thread)",
           "bind_script": {"path": BIND, "sha256": bind_sha, "bytes": os.path.getsize(BIND)},
           "launcher": {"path": LAUNCHER, "sha256": launcher_sha, "bytes": os.path.getsize(LAUNCHER)},
           "interpreter": {"path": INTERPRETER, "realpath": os.path.realpath(INTERPRETER),
                           "launcher_python_version": sys.version},
           "child_argv": child_argv, "child_env": env, "child_cwd": TMP_GEN,
           "stdout_log": OUT_LOG, "stderr_log": ERR_LOG,
           "limits": {"rss_bytes_self_abort": RSS_LIMIT, "wall_s_self_abort": WALL,
                      "launcher_sigterm_after_s": WALL + GRACE, "bounded_wait_after_sigterm_s": TERM_WAIT,
                      "cpu": "one (single-threaded child, idle launcher)", "in_flight_free_floor_bytes": FLOOR,
                      "free_reading_period_s": FREE_PERIOD, "never": "SIGKILL / Popen.kill / subprocess timeouts"},
           "free_bytes_fresh": fb, "launch_gate_bytes": GATE, "projected_growth_bytes": GROWTH,
           "launch_window_end": stop.isoformat(timespec="seconds"), "parent_authority": PARENT_AUTHORITY,
           "selftest_receipt": file_info(OUTPUTS["selftest_receipt"]),
           "static_notes": file_info(OUTPUTS["static_notes"])}
    pre_sha = write_x(PRE, pre)
    print("PRE-EXEC %s sha256 %s; bind %s" % (PRE, pre_sha, bind_sha), flush=True)
    out_fh, err_fh = open(OUT_LOG, "xb"), open(ERR_LOG, "xb")
    started = now().isoformat(timespec="seconds")
    t_start = time.monotonic()
    p = subprocess.Popen(child_argv, cwd=TMP_GEN, env=env, stdin=subprocess.DEVNULL, stdout=out_fh, stderr=err_fh,
                         close_fds=True)
    out_fh.close()
    err_fh.close()
    pid = p.pid
    termed, t_term, status, ru, unreaped = None, None, None, None, False
    min_free, readings, last_free_t, free_errors = fb, 1, t_start, 0
    while True:
        wpid, st, r = os.wait4(pid, os.WNOHANG)
        if wpid == pid:
            status, ru = st, r
            break
        mono = time.monotonic()
        if mono - last_free_t >= FREE_PERIOD:
            last_free_t = mono
            try:
                f2 = free_bytes()
                readings += 1
                min_free = min(min_free, f2)
                if f2 < FLOOR and termed is None:
                    termed = "in-flight free %d B < floor %d B" % (f2, FLOOR)
            except OSError:
                free_errors += 1
        if termed is None and STATE["launcher_sigterm"]:
            termed = "launcher received SIGTERM"
        if termed is None and mono - t_start > WALL + GRACE:
            termed = "wall %.0f s > %.0f s + %.0f s grace" % (mono - t_start, WALL, GRACE)
        if termed is not None and t_term is None:
            os.kill(pid, signal.SIGTERM)    # pid is unreaped (WNOHANG returned 0), so it cannot have been reused
            t_term = mono
        if t_term is not None and mono - t_term > TERM_WAIT:
            unreaped = True                 # bounded wait exhausted; no escalation
            break
        time.sleep(POLL)
    wall = time.monotonic() - t_start
    exit_code = os.waitstatus_to_exitcode(status) if status is not None else None
    if exit_code is not None:
        p.returncode = exit_code
    manifest_status = None
    if os.path.exists(OUTPUTS["manifest"]):
        with open(OUTPUTS["manifest"], "rb") as f:
            manifest_status = json.loads(f.read()).get("status")
    if unreaped or termed is not None or exit_code == 3:
        verdict = "UNKNOWN"
    elif exit_code == 0 and manifest_status == "PASS":
        verdict = "COMPLETED-PASS"
    elif exit_code == 2:
        verdict = "COMPLETED-FAILED-GATES"
    else:
        verdict = "STOPPED"
    with open(ERR_LOG, "rb") as f:
        err_tail = f.read()[-4000:].decode("utf-8", "replace")
    post = {"schema": "moqls8-gb-parent-binding-post-exec/1", "written_at": now().isoformat(timespec="seconds"),
            "verdict": verdict, "pre_exec_sha256": pre_sha, "bind_script_sha256_at_end": sha_file(BIND),
            "launcher_sha256_at_end": sha_file(LAUNCHER), "child_pid": pid, "child_started_at": started,
            "wall_s": round(wall, 2), "exit_code": exit_code, "unreaped_after_bounded_wait": unreaped,
            "sigterm_sent": t_term is not None, "sigterm_reason": termed,
            "child_rusage": None if ru is None else {"maxrss_bytes": ru.ru_maxrss, "utime_s": round(ru.ru_utime, 2),
                                                     "stime_s": round(ru.ru_stime, 2),
                                                     "maxrss_within_1GiB": ru.ru_maxrss <= RSS_LIMIT},
            "free": {"at_launch": fb, "min_observed": min_free, "readings": readings, "read_errors": free_errors,
                     "floor": FLOOR},
            "manifest_status": manifest_status,
            "outputs": {k: file_info(v) for k, v in OUTPUTS.items()},
            "logs": {"stdout": file_info(OUT_LOG), "stderr": file_info(ERR_LOG)}, "stderr_tail": err_tail,
            "cnf_or_proof_bytes_written_to_disk": False, "native_tools_started": 0}
    post_sha = write_x(POST, post)
    print("POST-EXEC %s sha256 %s verdict %s exit %s wall %.1f s maxrss %s" % (
        POST, post_sha, verdict, exit_code, wall, None if ru is None else ru.ru_maxrss), flush=True)
    return 0 if verdict == "COMPLETED-PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
