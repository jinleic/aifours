"""Lane ContinueMOQLS8 foreground launcher for ONE code/replay_v6f.py run (phys-1, 96-hour continuation).

Before any spawn it verifies: DESK and logs/, launch/, tmp/, receipts/, fifo/, runs/ are real directories (no symlink,
realpath equal to the path); the pinned driver sha256; the PRE-EXEC is a regular file directly in DESK; the parent GO
record is a regular, non-symlink file directly under the new-round review/ with status PARENT_GO, lane phys-1, this
launcher's and the driver's sha256, the PRE-EXEC sha256, the exact ordered items, the launch-contract-tightening
sha256, the 80 MiB retained reservation, a non-empty stop_dispositions field and a stop_registry pin naming a regular
file <lane>/review/STOP-REGISTRY-v<N>.json physically in place (canonical path) with the registry schema and the pinned
sha256; and the clock is before the driver's native-launch cutoff. It RESERVES its three outputs by exclusive creation
(console log, launch record, settlement record) and computes CHUNK_END = min(now + 10620 s, owned_compute_settled_by -
180 s), quantized ONCE to milliseconds (the identical value is passed, recorded and enforced), refusing a launch that
leaves less than one formula backstop + 360 s. All bookkeeping exists before the spawn. From just before the spawn
SIGINT, SIGTERM and SIGHUP are only RECORDED by this launcher (the driver's dispositions are reset to default by exec;
the signal mask is unchanged). The spawn of '/usr/bin/python3 -I -B <lane>/code/replay_v6f.py run PREEXEC' (own session:
the driver leads its session and process group; cadical and drat-trim inherit that group) and every later step run in
ONE ownership scope; its finally waits for the driver whenever it exists (os.waitpid, no timeout) and always writes a
settlement record (failed diagnostics recorded, a minimal record still written). If the launch record cannot be
published the launcher fails closed: it sends ONE SIGTERM to its own unreaped driver (before that driver can pass its
>= 60 s admission gate) and still waits and settles; this fail-closed path covers EVERY failure between a successful
spawn and a successful publication (console close, record construction, write, announcement). The driver is waited
for with Popen.wait() (no timeout; its cached status is never lost). The fit check tolerates the 1 ms quantization.
Exit status: the driver's (128+N for signal N) when the launch was clean, 4 when any launcher error or recorded
launcher signal occurred, 2 for a refused launch (no spawn). (r7 of launch_ga_v6f.py, which is kept unchanged.)
Usage: /usr/bin/python3 -I -B launch_ga_v6g.py PREEXEC GO_RECORD"""
import datetime
import hashlib
import json
import os
import re
import signal
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8"
NEW_REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review"
DESK = LANE + "/evidence/ga-replay-v6f"
SUBDIRS = ("logs", "launch", "tmp", "receipts", "fifo", "runs")
SCRIPT = LANE + "/code/replay_v6f.py"
SCRIPT_SHA = "92964dc05348fad9a251ee47d30b88c6bd00f9fac526439a36059e42ac7218d6"
PYTHON = "/usr/bin/python3"
TIGHTENING_SHA = "8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20"
REGISTRY_RE = re.compile(re.escape(LANE + "/review/") + r"STOP-REGISTRY-v[1-9][0-9]*\.json")
REGISTRY_SCHEMA = "moqls8-inherited-stop-registry/1"
RESERVATION = 80 << 20
PDT = datetime.timezone(datetime.timedelta(hours=-7))
NO_LAUNCH_AT = datetime.datetime(2026, 10, 22, 18, 59, 33, tzinfo=PDT).timestamp()  # replay_v6f.py NO_LAUNCH_AT
SETTLED_BY = datetime.datetime(2026, 10, 22, 21, 56, 33, tzinfo=PDT).timestamp()  # owned_compute_settled_by
CHILD_END_LIMIT, BACKSTOP, REAP = 10620, 10260, 120  # replay_v6f.py constants
SIGNALS_SEEN = []


def on_signal(signum, _frame):
    SIGNALS_SEEN.append(signal.Signals(signum).name)


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], text=True).strip()


def iso(t):
    return datetime.datetime.fromtimestamp(t).astimezone().isoformat(timespec="milliseconds")


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
    return stat.S_ISREG(st.st_mode) and os.path.dirname(path) == parent and os.path.realpath(path) == path


def put_json(fd, obj):
    data = (json.dumps(obj, indent=1, default=repr) + "\n").encode()
    off = 0
    while off < len(data):
        off += os.write(fd, data[off:])
    os.fsync(fd)
    return hashlib.sha256(data).hexdigest()


def refuse(msg):
    print("LAUNCH REFUSED: " + msg, flush=True)
    raise SystemExit(2)


def registry_ok(reg):
    path = reg.get("path") if isinstance(reg, dict) else None
    if not (isinstance(path, str) and REGISTRY_RE.fullmatch(path) and regular_in(path, LANE + "/review")):
        return False
    if sha(path) != reg.get("sha256"):
        return False
    try:
        return json.load(open(path)).get("schema") == REGISTRY_SCHEMA
    except (OSError, ValueError, AttributeError):
        return False


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
        refuse("replay_v6f.py sha256 differs from the launcher pin")
    me = os.path.realpath(__file__)
    pre_sha, go_sha, me_sha = sha(pre), sha(go), sha(me)
    p = json.load(open(pre))
    g = json.load(open(go))
    items = [it["item"] for it in p["items"]]
    want = {"status": "PARENT_GO", "lane": "phys-1", "script_sha256": SCRIPT_SHA, "launcher_sha256": me_sha,
            "pre_exec_sha256": pre_sha, "items": items, "launch_contract_tightening_sha256": TIGHTENING_SHA,
            "retained_reservation_bytes": RESERVATION}
    bad = ["%s=%r (required %r)" % (k, g.get(k), v) for k, v in want.items() if g.get(k) != v]
    if not registry_ok(g.get("stop_registry")):
        bad.append("stop_registry must pin a regular <lane>/review/STOP-REGISTRY-vN.json with its schema and sha256")
    if not g.get("stop_dispositions"):
        bad.append("stop_dispositions missing or empty")
    if bad:
        refuse("GO record: " + "; ".join(bad))
    now = time.time()
    if now >= NO_LAUNCH_AT:
        refuse("native-launch cutoff reached")
    chunk_end = float("%.3f" % min(now + CHILD_END_LIMIT, SETTLED_BY - 180))  # quantized once; used everywhere
    if chunk_end - now < BACKSTOP + 360 - 0.002:  # tolerates the 1 ms quantization
        refuse("absolute chunk end leaves less than one formula backstop + 360 s")
    tag = time.strftime("%Y%m%dT%H%M%S")
    console = os.path.join(DESK, "logs", "console-%s.log" % tag)
    record = os.path.join(DESK, "launch", "LAUNCH-%s.json" % tag)
    settle = os.path.join(DESK, "launch", "SETTLED-%s.json" % tag)
    argv = [PYTHON, "-I", "-B", SCRIPT, "run", pre]
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": os.environ.get("HOME", DESK), "TMPDIR": DESK + "/tmp/",
           "LC_ALL": "C", "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
           "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MOQLS8_CHUNK_END_EPOCH": "%.3f" % chunk_end}
    fds, errors, state = {}, [], {"child": None, "rec_sha": None, "code": None, "status": None, "sigterm_sent": None}
    try:
        for k, path in (("console", console), ("record", record), ("settle", settle)):
            fds[k] = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)  # reserved BEFORE the spawn
    except OSError as e:
        for fd in fds.values():
            os.close(fd)
        refuse("could not reserve outputs: %r" % e)
    started = clock()
    for s in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):  # from here on: recorded, never fatal to the launcher
        signal.signal(s, on_signal)
    try:  # ONE ownership scope from the spawn to the settlement record
        state["child"] = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=fds["console"],
                                          stderr=subprocess.STDOUT, cwd=DESK + "/tmp", env=env,
                                          start_new_session=True)
        child = state["child"]
        try:  # EVERY step until a successful publication: any failure -> one owned SIGTERM (fail closed)
            os.close(fds.pop("console"))  # only the driver holds the console log now
            rec = {"schema": "moqls8-lane-launch-record/5", "owner": "ContinueMOQLS8 (phys-1 lane worker)",
                   "launcher": {"path": me, "sha256": me_sha, "pid": os.getpid(), "pgid": os.getpgrp()},
                   "items": items, "parent_go": {"path": go, "sha256": go_sha},
                   "pre_exec": {"path": pre, "sha256": pre_sha}, "stop_registry": g.get("stop_registry"),
                   "driver": {"pid": child.pid, "pgid": child.pid, "session_leader": True, "started_at": started,
                              "argv": argv, "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(),
                              "cwd": DESK + "/tmp", "env": env},
                   "pins": {"script_sha256": SCRIPT_SHA, "python_realpath": os.path.realpath(PYTHON),
                            "binaries": p.get("binaries"),
                            "item_feeds": [{"item": it["item"],
                                            "solver_feed_sha256": it["expected_solver_feed_sha256"],
                                            "solver_feed_bytes": it["expected_solver_feed_bytes"],
                                            "checker_feed_sha256": it["expected_checker_feed_sha256"],
                                            "checker_feed_bytes": it["expected_checker_feed_bytes"]}
                                           for it in p["items"]]},
                   "absolute_child_end": {"epoch": chunk_end, "at": iso(chunk_end),
                                          "enforced_by": "replay_v6f.py, in the driver's calling thread (pipeline loop): "
                                                         "no native spawn whose backstop passes it; SIGTERM of every live "
                                                         "child once it is reached; a child reaped after it is a stop",
                                          "settlement": "each SIGTERMed child is waited for at most 120 s (until %s), never "
                                                        "escalated; an unreaped child is reported and the run is UNSETTLED"
                                                        % iso(chunk_end + REAP)},
                   "external_rescue": "the driver (pid = pgid above) leads its own session and process group; cadical and "
                                      "drat-trim inherit that process group (ps/lsof helpers run in their own sessions). "
                                      "If the driver were unresponsive, an identity-checked SIGTERM to that process group "
                                      "reaches the driver and both natives; nothing is ever SIGKILLed.",
                   "outputs": {"desk": DESK, "console_log": console, "receipts": DESK + "/receipts/",
                               "logs": DESK + "/logs/", "fifo": DESK + "/fifo/", "tmp": DESK + "/tmp/",
                               "runs": DESK + "/runs/", "settlement_record": settle},
                   "retained_reservation_bytes": RESERVATION,
                   "enforcement": "driver: byte-capped child-output sinks (<= 32 MiB written per log; overflow = safety "
                                  "stop); free < 12e9, desk RSS > reservation + 0.5 GiB, lane RSS > 11 GiB, other lane "
                                  "busy + 4 > 4, backstop, absolute chunk end -> SIGTERM of its own children; sampling 0.25 s"}
            state["rec_sha"] = put_json(fds["record"], rec)
            print("LAUNCH RECORD %s sha256 %s driver pid %d" % (record, state["rec_sha"], child.pid), flush=True)
        except BaseException as e:  # fail closed: registration could not be published
            errors.append("launch record not published: %r" % e)
            if child.returncode is None:  # owned and not yet reaped by us: its pid cannot have been reused
                os.kill(child.pid, signal.SIGTERM)
                state["sigterm_sent"] = time.time()
    except BaseException as e:
        errors.append("post-spawn: %r" % e)
    finally:
        child = state["child"]
        if child is not None:
            try:
                child.wait()  # Popen.wait(): no timeout; the cached return code is never lost
            except BaseException as e:
                errors.append("wait: %r" % e)
        out = {"schema": "moqls8-lane-settlement-record/5", "launch_record": record,
               "launch_record_sha256": state["rec_sha"], "driver_pid": child.pid if child is not None else None,
               "launcher_sigterm_sent_to_driver": state["sigterm_sent"], "errors": errors,
               "launcher_signals_recorded": SIGNALS_SEEN}
        try:
            code = child.returncode if child is not None else None
            state["code"] = code
            out.update({"exit_code": code if code is not None and code >= 0 else None,
                        "terminating_signal": -code if code is not None and code < 0 else None})
        except BaseException as e:
            errors.append("status: %r" % e)
        for key, fn in (("reaped_at", clock), ("console_log_sha256", lambda: sha(console)),
                        ("console_log_bytes", lambda: os.path.getsize(console))):
            try:
                out[key] = fn()
            except BaseException as e:
                errors.append("%s: %r" % (key, e))
        out["note"] = ("Direct child (driver) reaped by the launcher unless errors say otherwise. Owned descendants, "
                       "stream closure and final receipts are checked separately; this record alone is not a PASS.")
        try:
            print("SETTLEMENT RECORD %s sha256 %s exit %s" % (settle, put_json(fds["settle"], out), state["code"]),
                  flush=True)
        finally:
            for fd in fds.values():
                try:
                    os.close(fd)
                except OSError:
                    pass
    code = state["code"]
    if errors or SIGNALS_SEEN or code is None:
        return 4
    return code if code >= 0 else 128 - code


if __name__ == "__main__":
    raise SystemExit(main())
