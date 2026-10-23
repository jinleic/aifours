"""Lane ContinueMOQLS8 foreground launcher for ONE code/gb_staged_v6b.py run (phys-1, 96-hour continuation).

Before any spawn it verifies: the desk tree is real directories (no symlink, realpath equal to the path) for DESK and
logs/, launch/, tmp/, receipts/, fifo/, runs/; the pinned driver sha256; the PRE-EXEC is a regular file directly in
DESK; the parent GO record is a regular, non-symlink file directly under the new-round review/ with status PARENT_GO,
lane phys-1, this script and driver identity, the PRE-EXEC sha256, the exact ordered items, a lane STOP-registry pin
that re-hashes, the launch-contract-tightening sha256 and the 80 MiB retained reservation; the clock is before the
driver's native-launch cutoff. It then RESERVES its three outputs by exclusive creation (console log, launch record,
settlement record), computes the absolute chunk end CHUNK_END = min(now + 10620 s, owned_compute_settled_by - 180 s)
(refusing a launch for which that leaves less than the two gb stage backstops + reap + 420 s), and spawns
'<python3.14> -I -B <lane>/code/gb_staged_v6b.py run PREEXEC GO' in its own session with a clean environment
(TMPDIR=<desk>/tmp/, PYTHONDONTWRITEBYTECODE=1, single-threaded BLAS/OpenMP variables, MOQLS8_CHUNK_END_EPOCH=CHUNK_END),
cwd <desk>/tmp, stdin /dev/null, stdout+stderr to the reserved console log. The driver itself refuses any native
spawn whose backstop would pass CHUNK_END and SIGTERMs every live child at CHUNK_END; a SIGTERMed child is waited for
at most 120 s and is never escalated, so settlement is bounded but not guaranteed (an unreaped child is reported, the
run is UNSETTLED). Immediately after the spawn the launch record is written into its reserved file; whatever happens
after the spawn, a finally clause waits for the driver with os.waitpid (no timeout; nothing is ever signalled) and
writes the settlement record. Exit status = the driver's (128+N for signal N); 2 for a refused launch (no spawn).
Usage: /usr/bin/python3 -I -B launch_gb_v6b.py PREEXEC GO_RECORD"""
import datetime
import hashlib
import json
import math
import os
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8"
NEW_REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review"
DESK = LANE + "/evidence/gb-staged-v6b"
DESK_REL = "physics/evidence/six-lane-20261018-96h/moqls8/evidence/gb-staged-v6b"
SUBDIRS = ("logs", "launch", "tmp", "receipts", "fifo", "runs")
SCRIPT = LANE + "/code/gb_staged_v6b.py"
SCRIPT_SHA = "7d25186e15332a75c3bf1b684363cc5331eb33e3cfd07c73daadc53c20190f9f"
PYTHON = "/opt/homebrew/opt/python@3.14/bin/python3.14"
TIGHTENING_SHA = "8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20"
RESERVATION = 80 << 20
PDT = datetime.timezone(datetime.timedelta(hours=-7))
NO_LAUNCH_AT = datetime.datetime(2026, 10, 22, 19, 0, 33, tzinfo=PDT).timestamp()  # gb_staged_v6b.py NO_LAUNCH_AT
SETTLED_BY = datetime.datetime(2026, 10, 22, 21, 56, 33, tzinfo=PDT).timestamp()  # owned_compute_settled_by
CHILD_END_LIMIT, BACKSTOP, REAP = 10620, 3720 + 120 + 6360, 120  # gb_staged_v6b.py: both stage backstops + reap


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], text=True).strip()


def iso(t):
    return datetime.datetime.fromtimestamp(t).astimezone().isoformat(timespec="seconds")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def real_dir(p):
    st = os.lstat(p)
    return stat.S_ISDIR(st.st_mode) and os.path.realpath(p) == p


def regular_in(path, parent):
    st = os.lstat(path)
    return (stat.S_ISREG(st.st_mode) and os.path.dirname(path) == parent
            and os.path.realpath(path) == path)


def reserve(path):
    return os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)


def put_json(fd, obj):
    data = (json.dumps(obj, indent=1) + "\n").encode()
    off = 0
    while off < len(data):
        off += os.write(fd, data[off:])
    os.fsync(fd)
    return hashlib.sha256(data).hexdigest()


def refuse(msg):
    print("LAUNCH REFUSED: " + msg, flush=True)
    raise SystemExit(2)


def main():
    if len(sys.argv) != 3:
        refuse(__doc__)
    pre, go = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if not (real_dir(DESK) and all(real_dir(os.path.join(DESK, d)) for d in SUBDIRS)):
        refuse("desk tree is not real directories")
    if not regular_in(pre, DESK):
        refuse("PRE-EXEC must be a regular file directly in the desk")
    if not regular_in(go, NEW_REVIEW):
        refuse("GO must be a regular parent file directly under the new-round review/")
    if sha(SCRIPT) != SCRIPT_SHA:
        refuse("gb_staged_v6b.py sha256 differs from the launcher pin")
    pre_sha, go_sha = sha(pre), sha(go)
    p = json.load(open(pre))
    g = json.load(open(go))
    items = [it["item"] for it in p["items"]]
    me = os.path.realpath(__file__)
    reg = g.get("stop_registry") if isinstance(g.get("stop_registry"), dict) else {}
    reg_path = reg.get("path", "")
    want = {"status": "PARENT_GO", "lane": "phys-1", "desk": DESK_REL, "script_sha256": SCRIPT_SHA,
            "launcher_sha256": sha(me),
            "pre_exec_sha256": pre_sha, "items": items, "launch_contract_tightening_sha256": TIGHTENING_SHA,
            "retained_reservation_bytes": RESERVATION}
    bad = ["%s=%r (required %r)" % (k, g.get(k), v) for k, v in want.items() if g.get(k) != v]
    if not (isinstance(reg_path, str) and reg_path.startswith(LANE + "/review/") and os.path.isfile(reg_path)
            and not os.path.islink(reg_path) and sha(reg_path) == reg.get("sha256")):
        bad.append("stop_registry pin does not re-hash inside the lane review/")
    if bad:
        refuse("GO record: " + "; ".join(bad))
    now = time.time()
    if now >= NO_LAUNCH_AT:
        refuse("native-launch cutoff reached")
    chunk_end = min(now + CHILD_END_LIMIT, SETTLED_BY - 180)
    if chunk_end - now < BACKSTOP + 420:
        refuse("absolute chunk end leaves less than the two stage backstops + reap + 420 s")
    tag = time.strftime("%Y%m%dT%H%M%S")
    console = os.path.join(DESK, "logs", "console-%s.log" % tag)
    record = os.path.join(DESK, "launch", "LAUNCH-%s.json" % tag)
    settle = os.path.join(DESK, "launch", "SETTLED-%s.json" % tag)
    fds = {}
    try:
        for k, path in (("console", console), ("record", record), ("settle", settle)):
            fds[k] = reserve(path)  # exclusive reservation of every output BEFORE the spawn
    except OSError as e:
        for fd in fds.values():
            os.close(fd)
        refuse("could not reserve outputs: %r" % e)
    argv = [PYTHON, "-I", "-B", SCRIPT, "run", pre, go]
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": os.environ.get("HOME", DESK), "TMPDIR": DESK + "/tmp/",
           "LC_ALL": "C", "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
           "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MOQLS8_CHUNK_END_EPOCH": "%.3f" % chunk_end}
    started = clock()
    child = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=fds["console"], stderr=subprocess.STDOUT,
                             cwd=DESK + "/tmp", env=env, start_new_session=True)
    os.close(fds.pop("console"))  # only the driver holds the console log now
    rec_sha = rec_error = None
    try:
        rec = {"schema": "moqls8-lane-launch-record/2", "owner": "ContinueMOQLS8 (phys-1 lane worker)",
               "launcher": {"path": me, "sha256": sha(me), "pid": os.getpid(), "pgid": os.getpgrp()},
               "items": items, "parent_go": {"path": go, "sha256": go_sha}, "pre_exec": {"path": pre, "sha256": pre_sha},
               "stop_registry": reg,
               "driver": {"pid": child.pid, "pgid": os.getpgid(child.pid), "session_leader": True,
                          "started_at": started, "argv": argv,
                          "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(),
                          "cwd": DESK + "/tmp", "env": env},
               "pins": {"script_sha256": SCRIPT_SHA, "python_realpath": os.path.realpath(PYTHON),
                        "python_sha256": sha(os.path.realpath(PYTHON)), "binaries": p.get("binaries"),
                        "item_feeds": [{"item": it["item"],
                                        "solver_feed_sha256": it["expected_solver_feed_sha256"],
                                        "solver_feed_bytes": it["expected_solver_feed_bytes"],
                                        "checker_feed_sha256": it["expected_checker_feed_sha256"],
                                        "checker_feed_bytes": it["expected_checker_feed_bytes"]}
                                       for it in p["items"]]},
               "absolute_child_end": {"epoch": chunk_end, "at": iso(chunk_end),
                                      "enforced_by": "gb_staged_v6b.py: no stage spawn whose remaining stage backstops "
                                                     "pass it; SIGTERM of the live child once it is reached",
                                      "settlement": "each SIGTERMed child waited for at most 120 s (by %s), never "
                                                    "escalated; an unreaped child is reported and the run is UNSETTLED"
                                                    % iso(chunk_end + REAP)},
               "outputs": {"desk": DESK, "console_log": console, "receipts": DESK + "/receipts/",
                           "logs": DESK + "/logs/", "fifo": DESK + "/fifo/", "tmp": DESK + "/tmp/",
                           "runs": DESK + "/runs/", "settlement_record": settle},
               "retained_reservation_bytes": RESERVATION,
               "enforcement": "driver: byte-capped kissat-output sink and filtered drat-trim log (<= 32 MiB each; "
                              "overflow = safety stop); free < 12e9, pipeline RSS > cap, lane RSS > 11 GiB, other lane "
                              "busy + 3 > 4, stage backstops, absolute chunk end -> SIGTERM of the live child; "
                              "sampling 0.25 s",
               "signalling": "the parent may identity-check (pid, pgid, argv_sha256, cwd) and SIGTERM the driver pid; "
                             "the driver latches it and SIGTERMs only its own children; nothing is SIGKILLed"}
        rec_sha = put_json(fds["record"], rec)
        print("LAUNCH RECORD %s sha256 %s driver pid %d" % (record, rec_sha, child.pid), flush=True)
    except BaseException as e:  # the driver keeps running and is still waited for below
        rec_error = repr(e)
    finally:
        _pid, status = os.waitpid(child.pid, 0)
        code = os.waitstatus_to_exitcode(status)
        out = {"schema": "moqls8-lane-settlement-record/2", "launch_record": {"path": record, "sha256": rec_sha,
                                                                              "write_error": rec_error},
               "driver_pid": child.pid, "reaped_at": clock(), "exit_code": code if code >= 0 else None,
               "terminating_signal": -code if code < 0 else None, "console_log": console,
               "console_log_sha256": sha(console), "console_log_bytes": os.path.getsize(console),
               "note": "Direct child (driver) reaped by the launcher. Owned descendants, stream closure and final "
                       "receipts are checked separately by the lane and the parent audit; this record alone is not "
                       "a PASS."}
        try:
            print("SETTLEMENT RECORD %s sha256 %s exit %s" % (settle, put_json(fds["settle"], out), code), flush=True)
        finally:
            for fd in fds.values():
                os.close(fd)
    return code if code >= 0 else 128 - code


if __name__ == "__main__":
    raise SystemExit(main())
