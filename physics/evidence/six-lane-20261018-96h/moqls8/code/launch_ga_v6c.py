"""Lane ContinueMOQLS8 foreground launcher for ONE code/replay_v6c.py run (phys-1, 96-hour continuation).

It verifies the parent GO record, spawns '/usr/bin/python3 -I -B <lane>/code/replay_v6c.py run PREEXEC' in its own
session (never in the caller's process group) with a clean environment (TMPDIR=<desk>/tmp/, PYTHONDONTWRITEBYTECODE=1,
single-threaded BLAS/OpenMP variables), cwd <desk>/tmp, stdin /dev/null and stdout+stderr to a NEW console log, and
IMMEDIATELY writes the exclusive parent-readable launch record (owner, item(s), parent GO path+sha256, driver
PID/PGID, start identity, argv/source/binary/input pins, cwd, absolute worst-case child end and settlement, output
paths, retained-byte reservation). It then waits for the driver with os.waitpid (no timeout; it never signals
anything), writes the exclusive settlement record (exit status or signal) and exits with the driver's exit status
(128+N for a signal). It launches nothing else.
Usage: /usr/bin/python3 -I -B launch_ga_v6c.py PREEXEC GO_RECORD"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8"
NEW_REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review"
DESK = LANE + "/evidence/ga-replay-v6c"
SCRIPT = LANE + "/code/replay_v6c.py"
SCRIPT_SHA = "584b4778b971e915a1fa3e4761a30de2fec4fd289aa95c0aa8619ec099abd9b5"
PYTHON = "/usr/bin/python3"
CHILD_END_LIMIT, REAP, MARGIN = 10620, 120, 60  # replay_v6c.py: enforced driver chunk (CHUNK 10800 - 120 - 60)
RESERVATION = 80 << 20


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], text=True).strip()


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def write_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=1)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    return sha(path)


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    pre, go = os.path.realpath(sys.argv[1]), os.path.realpath(sys.argv[2])
    if not (pre.startswith(DESK + "/") and os.path.isfile(pre) and not os.path.islink(sys.argv[1])):
        raise SystemExit("PRE-EXEC must be a regular file inside the desk")
    if not (go.startswith(NEW_REVIEW + "/") and os.path.isfile(go) and not os.path.islink(sys.argv[2])):
        raise SystemExit("GO must be a parent regular file under the new-round review/")
    if sha(SCRIPT) != SCRIPT_SHA:
        raise SystemExit("replay_v6c.py sha256 differs from the launcher pin")
    pre_sha, go_sha = sha(pre), sha(go)
    p = json.load(open(pre))
    g = json.load(open(go))
    items = [it["item"] for it in p["items"]]
    want = {"status": "PARENT_GO", "script_sha256": SCRIPT_SHA, "pre_exec_sha256": pre_sha, "items": items}
    bad = ["%s=%r (required %r)" % (k, g.get(k), v) for k, v in want.items() if g.get(k) != v]
    if bad:
        raise SystemExit("GO record refused: " + "; ".join(bad))
    tag = time.strftime("%Y%m%dT%H%M%S")
    console = os.path.join(DESK, "logs", "console-%s.log" % tag)
    record = os.path.join(DESK, "launch", "LAUNCH-%s.json" % tag)
    settle = os.path.join(DESK, "launch", "SETTLED-%s.json" % tag)
    for path in (console, record, settle):
        if os.path.lexists(path):
            raise SystemExit("refusing to reuse " + path)
    argv = [PYTHON, "-I", "-B", SCRIPT, "run", pre]
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": os.environ.get("HOME", DESK), "TMPDIR": DESK + "/tmp/",
           "LC_ALL": "C", "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
           "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"}
    started_epoch = time.time()
    started = clock()
    with open(console, "xb") as log:
        child = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                                 cwd=DESK + "/tmp", env=env, start_new_session=True)
    worst_end = started_epoch + CHILD_END_LIMIT  # the driver's DRIVER_T0 is taken after this spawn
    worst_settled = worst_end + REAP
    iso = lambda t: datetime.datetime.fromtimestamp(t).astimezone().isoformat(timespec="seconds")
    rec = {"schema": "moqls8-lane-launch-record/1", "owner": "ContinueMOQLS8 (phys-1 lane worker)",
           "launcher": {"path": os.path.realpath(__file__), "sha256": sha(os.path.realpath(__file__)),
                        "pid": os.getpid(), "pgid": os.getpgrp()},
           "items": items, "parent_go": {"path": go, "sha256": go_sha}, "pre_exec": {"path": pre, "sha256": pre_sha},
           "driver": {"pid": child.pid, "pgid": os.getpgid(child.pid), "session_leader": True,
                      "started_at": started, "argv": argv,
                      "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(), "cwd": DESK + "/tmp",
                      "env": env},
           "pins": {"script_sha256": SCRIPT_SHA, "python_realpath": os.path.realpath(PYTHON),
                    "python_sha256": sha(os.path.realpath(PYTHON)), "binaries": p.get("binaries"),
                    "item_feeds": [{"item": it["item"], "solver_feed_sha256": it["expected_solver_feed_sha256"],
                                    "solver_feed_bytes": it["expected_solver_feed_bytes"],
                                    "checker_feed_sha256": it["expected_checker_feed_sha256"],
                                    "checker_feed_bytes": it["expected_checker_feed_bytes"]} for it in p["items"]]},
           "absolute_worst_case": {"rule": "replay_v6c.py enforces: no native spawn unless driver elapsed + backstop "
                                           "<= 10620 s and SIGTERM of every live child at driver elapsed 10620 s; + "
                                           "120 s bounded reap; + 60 s margin <= start + 10800 s",
                                   "native_children_end_by": iso(worst_end), "settled_by": iso(worst_settled),
                                   "chunk_end_with_margin": iso(worst_settled + MARGIN)},
           "outputs": {"desk": DESK, "console_log": console, "receipts": DESK + "/receipts/",
                       "logs": DESK + "/logs/", "fifo": DESK + "/fifo/", "tmp": DESK + "/tmp/", "runs": DESK + "/runs/",
                       "settlement_record": settle},
           "retained_reservation_bytes": RESERVATION,
           "enforcement": "driver: byte-capped child-output sinks (<= 32 MiB written per log; overflow -> SIGTERM); free "
                          "< 12e9 -> SIGTERM; desk RSS > reservation + 0.5 GiB -> SIGTERM; lane RSS > 11 GiB -> "
                          "SIGTERM; other lane busy + 4 > 4 -> SIGTERM; sampling every 0.25 s",
           "signalling": "parent may identity-check (pid, pgid, argv_sha256, cwd) and SIGTERM the driver pid; the "
                         "driver latches it, SIGTERMs its own children and reaps them within 120 s; no SIGKILL"}
    rsha = write_x(record, rec)
    print("LAUNCH RECORD %s sha256 %s driver pid %d pgid %d" % (record, rsha, child.pid, rec["driver"]["pgid"]),
          flush=True)
    _pid, status = os.waitpid(child.pid, 0)
    code = os.waitstatus_to_exitcode(status)
    out = {"schema": "moqls8-lane-settlement-record/1", "launch_record": {"path": record, "sha256": rsha},
           "driver_pid": child.pid, "reaped_at": clock(), "exit_code": code if code >= 0 else None,
           "terminating_signal": -code if code < 0 else None, "console_log": console,
           "console_log_sha256": sha(console), "console_log_bytes": os.path.getsize(console),
           "note": "Direct child reaped by the launcher. Owned descendant census, stream closure and final receipts "
                   "are checked separately by the lane and the parent audit; this record alone is not a PASS."}
    ssha = write_x(settle, out)
    print("SETTLEMENT RECORD %s sha256 %s exit %s" % (settle, ssha, code), flush=True)
    return code if code >= 0 else 128 - code


if __name__ == "__main__":
    raise SystemExit(main())
