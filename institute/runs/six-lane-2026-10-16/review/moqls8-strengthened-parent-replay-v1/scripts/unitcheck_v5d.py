#!/usr/bin/env python3
"""Pure-Python pre-review unit checks for scripts/replay_v5d.py (items A-H, v5c F1-F4, v5d F1' and F4'). No
native solver or checker and no ps/lsof helper is started: lane_scan is replaced by fakes, and the pipeline tests run
python -c stubs in place of cadical and drat-trim (the stub solver writes synthetic bytes to the named FIFO; nothing
is written to disk except logs, FIFOs, empty TMPDIRs and one hand-built PRE-EXEC under unitcheck-v5d[-TAG]/). Results
go to the new file UNITCHECK-v5d[-TAG].json. Usage: /usr/bin/python3 -I -B scripts/unitcheck_v5d.py [TAG]"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import threading
import time
import traceback

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-strengthened-parent-replay-v1"
TAG = ("-" + sys.argv[1]) if len(sys.argv) > 1 else ""
TARGET = DESK + "/scripts/replay_v5d.py"
OUT = DESK + "/UNITCHECK-v5d%s.json" % TAG
UDIR = DESK + "/unitcheck-v5d%s" % TAG

spec = importlib.util.spec_from_file_location("replay_v5d", TARGET)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

RESULTS = []


def check(name, ok, **detail):
    RESULTS.append(dict({"check": name, "ok": bool(ok)}, **detail))
    print("%-4s %s %s" % ("ok" if ok else "FAIL", name, json.dumps(detail, default=str)[:300]), flush=True)


def run(name, fn):
    try:
        fn()
    except BaseException as e:  # a crashing check is a failed check
        check(name + " (crashed)", False, error="%s: %s" % (type(e).__name__, e), tb=traceback.format_exc()[-2000:])


def sha(b):
    return hashlib.sha256(b).hexdigest()


def open_fds():
    return set(int(x) for x in os.listdir("/dev/fd"))


# --- B: run_helper ownership scope (python children only)
SLEEPER = [sys.executable, "-I", "-B", "-c", "import time; time.sleep(30)"]
IGNORER = [sys.executable, "-I", "-B", "-c",
           "import signal, time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(4)"]


def t_helper():
    saved = (m.HELPER_DEADLINE, m.HELPER_TERM_WAIT)
    m.HELPER_DEADLINE, m.HELPER_TERM_WAIT = 1.0, 2.0
    try:
        f0 = open_fds()
        t0 = time.monotonic()
        rc, out, err = m.run_helper(SLEEPER)
        check("B1 run_helper overrun: SIGTERM, reaped rc -15, error recorded, no survivor, no fd leak",
              rc == -15 and err and "deadline" in err and "SIGTERM sent" in err and not m.HELPER_SURVIVORS
              and open_fds() == f0, rc=rc, err=err, seconds=round(time.monotonic() - t0, 2))
        real = m.selectors.DefaultSelector

        def boom():
            raise OSError(24, "injected selector failure")
        m.selectors.DefaultSelector = boom
        try:
            rc, out, err = m.run_helper(SLEEPER)
        finally:
            m.selectors.DefaultSelector = real
        check("B2 exception after spawn: same SIGTERM/reap/close cleanup, error returned, no fd leak",
              rc == -15 and "supervision raised OSError" in err and "SIGTERM sent" in err and not m.HELPER_SURVIVORS
              and open_fds() == f0, rc=rc, err=err)

        class Sel:
            def __init__(self):
                self.real = real()

            def register(self, *a):
                return self.real.register(*a)

            def select(self, *a):
                raise KeyboardInterrupt("injected")

            def close(self):
                self.real.close()
        m.selectors.DefaultSelector = Sel
        raised = None
        try:
            m.run_helper(SLEEPER)
        except KeyboardInterrupt as e:
            raised = repr(e)
        finally:
            m.selectors.DefaultSelector = real
        check("B3 KeyboardInterrupt inside the scope: helper stopped and reaped, then re-raised, no fd leak",
              raised is not None and not m.HELPER_SURVIVORS and open_fds() == f0, raised=raised)
        m.HELPER_DEADLINE, m.HELPER_TERM_WAIT = 0.5, 0.5
        rc, out, err = m.run_helper(IGNORER)
        surv = list(m.HELPER_SURVIVORS)
        check("B4 helper ignoring SIGTERM: recorded in HELPER_SURVIVORS (no escalation)",
              len(surv) == 1 and "helper survivor" in err and rc is None, err=err, survivors=surv)
        rc2, _o2, err2 = m.run_helper(SLEEPER)
        check("B5 with a survivor recorded no further helper is spawned", rc2 is None and "no helper launch" in err2,
              err=err2)
        g = m.gate("unit", 512 << 20, {"used": 0.0}, lambda s: None, {}, stable=False)
        check("B6 gate refuses while a survivor is recorded", g["launch"] is False and "survivor" in g.get("stopped", ""),
              stopped=g.get("stopped"))
        late = m.latched_stop({}, FakeScanner())
        check("B7 latched_stop reports the survivor (in-flight guard and completion check)",
              late is not None and "survivor" in late, late=late)
        pid = surv[0]["pid"]
        _p, status = os.waitpid(pid, 0)  # the ignoring child exits by itself after 4 s; reap it here
        check("B8 survivor child exited on its own and was reaped by the test", os.WIFEXITED(status),
              status=status)
    finally:
        m.HELPER_DEADLINE, m.HELPER_TERM_WAIT = saved
        del m.HELPER_SURVIVORS[:]


# --- C: lane_scan exit-code and coverage validation with a fake run_helper
class FakeHelpers:
    def __init__(self, ps1, lsof, ps2):
        self.seq = {"/bin/ps:-axww": ps1, "/usr/sbin/lsof": lsof, "/bin/ps:-ww": ps2}

    def __call__(self, argv):
        key = argv[0] if argv[0].endswith("lsof") else argv[0] + ":" + argv[1]
        return self.seq[key]


def t_lane_scan():
    real = m.run_helper
    live = os.getppid()  # the shell that started this check: alive, our uid, never our child
    gone_child = subprocess.Popen([sys.executable, "-I", "-B", "-c", "pass"])
    gone_child.wait()
    gone = gone_child.pid
    lane_cwd = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16"
    ps1 = ("%d 1 1000 S /usr/bin/python3\n%d 1 2000 S /opt/x/Python\n" % (live, gone)).encode()
    lsof_ok = ("p%d\nfcwd\nn%s\np%d\nfcwd\nn/tmpx\n" % (live, lane_cwd, gone)).encode()
    ps2_ok = ("%d /usr/bin/python3 worker.py\n%d /opt/x/Python y.py\n" % (live, gone)).encode()
    try:
        cases = [
            ("C1 first ps rc 1 fails the scan", (1, ps1, None), (0, lsof_ok, None), (0, ps2_ok, None), False),
            ("C2 lsof rc 2 fails the scan", (0, ps1, None), (2, lsof_ok, None), (0, ps2_ok, None), False),
            ("C3 ps -p rc 1 fails the scan", (0, ps1, None), (0, lsof_ok, None), (1, ps2_ok, None), False),
            ("C4 lsof rc 1 accepted when coverage holds", (0, ps1, None), (1, lsof_ok, None), (0, ps2_ok, None), True),
            ("C5 live candidate without a cwd line fails the scan", (0, ps1, None),
             (1, ("p%d\nfcwd\nn/tmpx\n" % gone).encode(), None), (0, ps2_ok, None), False),
            ("C6 live candidate without an argv line fails the scan", (0, ps1, None), (0, lsof_ok, None),
             (0, ("%d /opt/x/Python y.py\n" % gone).encode(), None), False),
            ("C7 candidate without cwd/argv but gone per libproc is dropped", (0, ps1, None),
             (1, ("p%d\nfcwd\nn%s\n" % (live, lane_cwd)).encode(), None),
             (0, ("%d /usr/bin/python3 worker.py\n" % live).encode(), None), True),
            ("C8 helper error string fails the scan", (0, ps1, None), (None, b"", "lsof exceeded"), (0, ps2_ok, None),
             False),
        ]
        for name, a, b, c, want_ok in cases:
            m.run_helper = FakeHelpers(a, b, c)
            scan, err = m.lane_scan()
            got_ok = scan is not None
            detail = {"err": err, "lane_pids": [x["pid"] for x in scan] if scan else None}
            if want_ok:
                detail["lane_match"] = scan is not None and [x["pid"] for x in scan] == [live]
                check(name, got_ok and detail["lane_match"], **detail)
            else:
                check(name, not got_ok and err, **detail)
        check("C9 pid_gone: reaped child gone, live shell not gone, own pid not gone",
              m.pid_gone(gone) and not m.pid_gone(live) and not m.pid_gone(os.getpid()), gone=gone, live=live)
    finally:
        m.run_helper = real


# --- D: Scanner latch independent of 'latest'
class FakeScanner:
    def __init__(self, failed=None):
        self.failed = failed

    def failure(self):
        return self.failed


def t_scanner():
    real, calls = m.lane_scan, {"n": 0}

    def flaky():
        calls["n"] += 1
        return (None, "injected failure") if calls["n"] == 1 else ([], None)
    m.lane_scan = flaky
    saved = m.LANE_SCAN_PERIOD
    m.LANE_SCAN_PERIOD = 0.05
    try:
        s = m.Scanner()
        s.start()
        time.sleep(0.5)
        s.halt.set()
        s.join(5)
        mono, scan, err = s.reading()
        check("D1 Scanner latches the first failure although later readings are good",
              s.failure() is not None and s.failure()["error"] == "injected failure" and scan == [] and err is None
              and s.failures == 1 and s.scans >= 3 and not s.is_alive(), scans=s.scans, failed=s.failure())
        check("D2 latched_stop: signal first, then latched scanner failure, else None",
              "SIGTERM" in m.latched_stop({"signal": "SIGTERM"}, s) and "scanner failure" in m.latched_stop({}, s)
              and m.latched_stop({}, FakeScanner()) is None)
    finally:
        m.lane_scan, m.LANE_SCAN_PERIOD = real, saved


# --- G: stability rule (amended 07:32 PDT) on synthetic monitor bytes
def mon(samples, extra=b"", start=True):
    lines = [b'{"event": "start", "at": "x", "interval": 10}'] if start else []
    for t, f in samples:
        lines.append(json.dumps({"t": t, "free": f}).encode())
    return b"\n".join(lines) + b"\n" + extra


def iso(ts):
    import datetime
    return datetime.datetime.fromtimestamp(ts, m.PDT).isoformat(timespec="seconds")


def t_stability():
    now = 1792360000.0  # fixed epoch for synthetic samples (2026-10-18 PDT afternoon)
    base = [(now - 5 - 10 * k, 186000000000) for k in range(31)][::-1]
    S = lambda arr: [(iso(t), f) for t, f in arr]
    cases = [
        ("G1 31 steady samples, free 186e9: ok", mon(S(base)), True),
        ("G2 last sample 31 s old: refuse", mon(S([(t - 26, f) for t, f in base])), False),
        ("G3 only 24 samples in the window: refuse", mon(S(base[-24:])), False),
        ("G4 2.26e9 single step with free 186e9 (amendment case): ok",
         mon(S([(t, f - (2260000000 if i >= 20 else 0)) for i, (t, f) in enumerate(base)])), True),
        ("G5 drop 15e9 > (171e9 - 13.5e9) // 12 = 13.1e9: refuse",
         mon(S([(t, f - (15000000000 if i >= 20 else 0)) for i, (t, f) in enumerate(base)])), False),
        ("G6 free_last 13.6e9 with 400e6 drop (> 300e6 floor allowance): refuse",
         mon(S([(t, 14000000000 if i < 20 else 13600000000) for i, (t, f) in enumerate(base)])), False),
        ("G7 free_last 13.5e9 + 5 MiB (below +10 MiB): refuse",
         mon(S([(t, 13500000000 + 5 * (1 << 20)) for t, f in base])), False),
        ("G8 malformed complete line: refuse", mon(S(base[:15])) + b"{bad json\n" + mon(S(base[15:]), start=False),
         False),
        ("G9 naive timestamp (no tz): refuse",
         mon(S(base[:-1]) + [(iso(base[-1][0])[:-6], base[-1][1])]), False),
        ("G10 non-increasing timestamps: refuse", mon(S(base[:-1] + [(base[-2][0], base[-1][1])])), False),
        ("G11 future last sample (negative age): refuse", mon(S(base[:-1] + [(now + 20, base[-1][1])])), False),
        ("G12 unterminated trailing fragment ignored: ok", mon(S(base), extra=b'{"t": "2026-10-18T1'), True),
        ("G13 empty monitor: refuse", b"", False),
        ("G14 sample with free as a string: refuse", mon(S(base[:-1]) + [(iso(base[-1][0]), "186000000000")]), False),
    ]
    for name, raw, want in cases:
        ok, info = m.monitor_stability(raw=raw, nowt=now)
        check(name, ok == want, got=ok, checks=info.get("checks"), allowance=info.get("drop_allowance_bytes"),
              drop=info.get("max_peak_to_later_drop_bytes"))
    ok, info = m.monitor_stability()
    check("G15 real parent monitor read (informational; records the rule's verdict now)", True, monitor_ok=ok,
          checks=info.get("checks"),
          last_free=info.get("last_free"), age=info.get("last_age_seconds"), window=info.get("window_samples"),
          span=info.get("window_span_seconds"), allowance=info.get("drop_allowance_bytes"))


# --- A, D, F: pipeline() with python stubs for cadical and drat-trim
SOLVER_STUB = r"""
import hashlib, sys, time
a = sys.argv[1:]
time.sleep(SLOW)
d = open(a[-2], "rb").read()
blk = hashlib.sha256(d).digest() * 1024
with open(a[-1], "wb") as f:
    for _ in range(96):
        f.write(blk)
print("s UNSATISFIABLE", flush=True)
sys.exit(20)
"""
CHECKER_STUB = r"""
import sys
a = sys.argv[1:]
d = open(a[0], "rb").read()
h = d.split(b"\n", 1)[0].split()
n = 0
while True:
    b = sys.stdin.buffer.read(65536)
    if not b:
        break
    n += len(b)
print("c parsing input formula with %s variables and %s clauses" % (h[2].decode(), h[3].decode()))
print("c finished parsing, read %d bytes from proof file" % n)
print("s VERIFIED", flush=True)
sys.exit(0)
"""
PROOF_BYTES = 96 * 32 * 1024


class Shim:
    """m.subprocess replacement: cadical/drat-trim argv[0] -> python -c stub; optional injected spawn failures;
    slow > 0 makes the stub solver sleep that long first (so in-flight checks see several readings)."""

    def __init__(self):
        self.fail = set()
        self.slow = 0.0

    def __getattr__(self, k):
        return getattr(subprocess, k)

    def Popen(self, argv, **kw):
        if argv[0] == m.CADICAL:
            if "solver" in self.fail:
                raise FileNotFoundError(2, "injected solver spawn failure", argv[0])
            argv = [sys.executable, "-I", "-B", "-c", SOLVER_STUB.replace("SLOW", repr(self.slow))] + list(argv[1:])
        elif argv[0] == m.DRAT:
            if "checker" in self.fail:
                raise FileNotFoundError(2, "injected checker spawn failure", argv[0])
            argv = [sys.executable, "-I", "-B", "-c", CHECKER_STUB] + list(argv[1:])
        return subprocess.Popen(argv, **kw)


ITEM = {"kind": "formula", "expected_solver_feed_sha256": sha(m.UNSAT3), "expected_solver_feed_bytes": len(m.UNSAT3),
        "expected_checker_feed_sha256": sha(m.UNSAT3), "expected_checker_feed_bytes": len(m.UNSAT3),
        "expected_checker_header_counts": [3, 8]}
COUNTER = {"n": 0}


def pipe_run(tag, stop=None, shim_fail=(), start_fail=None, latch_after_checker=False, projected=512 << 20, slow=0.0):
    COUNTER["n"] += 1
    label = "v5d-unit-%02d-%s" % (COUNTER["n"], tag)
    stop = {} if stop is None else stop
    shim = Shim()
    shim.fail = set(shim_fail)
    shim.slow = slow
    orig_start = threading.Thread.start

    def failing_start(self):
        tgt = getattr(self, "_target", None)
        args = getattr(self, "_args", ())
        if start_fail == "relay" and tgt is m._relay:
            raise RuntimeError("injected: relay Thread.start failed")
        if start_fail == "relay-after" and tgt is m._relay:
            orig_start(self)
            raise RuntimeError("injected: relay start() interrupted after the thread started")
        if start_fail == "scw" and tgt is m._writer and len(args) > 1 and args[1] == "scw":
            raise RuntimeError("injected: solver writer Thread.start failed")
        return orig_start(self)
    f0 = open_fds()
    m.subprocess = shim
    threading.Thread.start = failing_start
    holder = {}
    if latch_after_checker:
        real_popen = shim.Popen

        def popen_and_watch(argv, **kw):
            p = real_popen(argv, **kw)
            if argv[0] == m.DRAT:
                def watch():
                    t_end = time.monotonic() + 30
                    while time.monotonic() < t_end and not m.pid_gone(p.pid):
                        time.sleep(0.002)
                    stop["signal"] = "SIGTERM"
                    holder["latched_at"] = time.monotonic()
                th = threading.Thread(target=watch, daemon=True)
                orig_start(th)
                holder["watch"] = th
            return p
        shim.Popen = popen_and_watch
    try:
        rec = m.pipeline(label, [m.UNSAT3], [m.UNSAT3], projected, lambda s: None, stop)
    finally:
        threading.Thread.start = orig_start
        m.subprocess = subprocess
    if "watch" in holder:
        holder["watch"].join(35)
    time.sleep(0.05)
    rec["pre_evaluation_check"] = {"checked": True, "at": m.now(), "stop_signal": stop.get("signal"),
                                   "scanner_failed": (rec.get("lane_scanner") or {}).get("failed"),
                                   "helper_survivors": list(m.HELPER_SURVIVORS)}
    verdict, reasons, crit = m.evaluate(rec, ITEM)
    leak = sorted(open_fds() ^ f0)
    return rec, verdict, reasons, crit, leak


def t_pipeline():
    os.mkdir(UDIR)
    for sub in ("fifo", "logs", "tmp"):
        os.mkdir(os.path.join(UDIR, sub))
    saved = (m.DESK, m.TMP, m.lane_scan)
    m.DESK, m.TMP = UDIR, UDIR + "/tmp"
    m.lane_scan = lambda: ([], None)
    try:
        rec, v, why, crit, leak = pipe_run("normal")
        r = rec["relay"]
        check("A0/F0 normal stub pipeline: PASS, R == D == stub bytes, equal sha, EOF, N == D, nothing left for the "
              "cleanup, no fd leak",
              v == "PASS" and r["read_bytes"] == r["delivered_bytes"] == PROOF_BYTES
              and r["read_sha256"] == r["delivered_sha256"] and r["fifo_eof_seen"] is True
              and rec["checker_parsed_proof_bytes"] == PROOF_BYTES and rec["fds_closed_by_cleanup"] == []
              and rec["threads"]["unfinished"] == [] and not leak,
              verdict=v, reasons=why, read=r["read_bytes"], closed_by_cleanup=rec["fds_closed_by_cleanup"], leak=leak,
              proof_sha=rec["proof_stream_sha256"], seconds=rec["pipeline_seconds"])
        rec, v, why, crit, leak = pipe_run("relay-start-fail", start_fail="relay")
        check("A1 relay Thread.start fails: checker SIGTERMed and reaped, fifo_read/keepalive/ccw/cpw closed once by "
              "the cleanup, no fd leak, UNKNOWN",
              v == "UNKNOWN" and "exception" in rec and rec["children"].get("checker", {}).get("rc") == -15
              and sorted(rec["fds_closed_by_cleanup"]) == ["ccw", "cpw", "fifo_read", "keepalive"]
              and "solver" not in rec["children"] and not leak,
              verdict=v, closed_by_cleanup=rec["fds_closed_by_cleanup"], children=rec["children"], leak=leak,
              events=[e.get("event") for e in rec["events"]])
        rec, v, why, crit, leak = pipe_run("scw-start-fail", start_fail="scw")
        check("A2 solver-writer Thread.start fails after the solver spawn: solver was registered (SIGTERMed and "
              "reaped with the checker), scw closed once by the cleanup, no fd leak, UNKNOWN",
              v == "UNKNOWN" and "exception" in rec and set(rec["children"]) == {"checker", "solver"}
              and rec["fds_closed_by_cleanup"] == ["scw"] and not leak,
              verdict=v, closed_by_cleanup=rec["fds_closed_by_cleanup"],
              rcs={k: c.get("rc") for k, c in rec["children"].items()}, leak=leak)
        rec, v, why, crit, leak = pipe_run("solver-spawn-fail", shim_fail=("solver",))
        check("F1 solver spawn error: stop reason set, live checker SIGTERMed (event) and reaped, UNKNOWN",
              v == "UNKNOWN" and rec.get("solver_spawn_error") and "solver spawn failed" in rec["safety_stop_reason"]
              and "checker" in rec["children"] and not rec.get("sigterm_grace_exceeded")
              and any(e.get("event") == "SIGTERM" and e.get("target") == "checker" for e in rec["events"])
              and not leak,
              verdict=v, reason=rec["safety_stop_reason"], checker=rec["children"].get("checker"), leak=leak)
        rec, v, why, crit, leak = pipe_run("checker-spawn-fail", shim_fail=("checker",))
        check("F2 checker spawn error: stop reason set, nothing launched, all fds closed by the cleanup, UNKNOWN",
              v == "UNKNOWN" and rec.get("checker_spawn_error") and "checker spawn failed" in rec["safety_stop_reason"]
              and rec["children"] == {} and not leak,
              verdict=v, reason=rec["safety_stop_reason"], closed_by_cleanup=rec["fds_closed_by_cleanup"], leak=leak)
        rec, v, why, crit, leak = pipe_run("latched-at-completion", latch_after_checker=True)
        check("D3 SIGTERM latched after the checker exit (children done): PASS vetoed, stop recorded",
              v == "UNKNOWN" and not crit["no_driver_sigterm_latched"]
              and (rec.get("safety_stop_reason") is not None or rec.get("stop_latched_during_pipeline")),
              verdict=v, reason=rec.get("safety_stop_reason"),
              during=rec.get("stop_latched_during_pipeline"), completion_event=[e for e in rec["events"]
                                                                                if "completion" in e.get("event", "")])
        calls = {"n": 0}

        def fail_once():
            calls["n"] += 1
            return (None, "injected scan failure") if calls["n"] == 1 else ([], None)
        m.lane_scan = fail_once
        rec, v, why, crit, leak = pipe_run("scanner-fail-once")
        check("D4 one failed lane reading followed by good ones: latched -> safety stop or veto, never PASS",
              v == "UNKNOWN" and not crit["lane_scanner_no_failure"] and rec["lane_scanner"]["failed"] is not None,
              verdict=v, reason=rec.get("safety_stop_reason"), scanner=rec["lane_scanner"])
    finally:
        m.DESK, m.TMP, m.lane_scan = saved


# --- A: handoff primitives without a pipeline
def t_handoff():
    fds = m.Fds()
    r, w = os.pipe()
    fds.put("w", w)
    orig = threading.Thread.start

    def nostart(self):
        raise RuntimeError("injected")
    threading.Thread.start = nostart
    try:
        try:
            t_unused, _res = m._new_writer(fds, "w", [b"x"])
            t_unused.start()
            started = True
        except RuntimeError:
            started = False
    finally:
        threading.Thread.start = orig
    still = fds.names() == ["w"]
    (fd,) = fds.take("w")
    os.close(fd)
    try:
        os.fstat(w)
        closed = False
    except OSError:
        closed = True
    os.close(r)
    check("A3 failed Thread.start: descriptor stays registered; the cleanup closes it exactly once",
          not started and still and closed and fds.names() == [])
    fds2 = m.Fds()
    r2, w2 = os.pipe()
    fds2.put("w", w2)
    (taken,) = fds2.take("w")  # the cleanup takes first
    os.close(taken)
    r3, w3 = os.pipe()  # may reuse the freed descriptor number
    res = {"ok": False}
    m._writer(fds2, "w", [b"abc"], res)
    alive = True
    for x in (r3, w3):
        try:
            os.fstat(x)
        except OSError:
            alive = False
    for x in (r2, r3, w3):
        os.close(x)
    check("A4 cleanup took the descriptor first: the worker records 'not handed over' and closes nothing",
          res.get("fd_claimed") is False and res["ok"] is False and alive, res=res)


# --- relay on plain os.pipe pairs (v4 checks adapted to the Fds handoff)
def relay_case(mode, payload, close_reader_first=False):
    fr, fw = os.pipe()
    cr, cw = os.pipe()
    fds = m.Fds()
    fds.put("fifo_read", fr)
    fds.put("cpw", cw)
    got = bytearray()

    def drain():
        while True:
            b = os.read(cr, 1 << 16)
            if not b:
                break
            got.extend(b)
    if close_reader_first:
        os.close(cr)
        dr = None
    else:
        dr = threading.Thread(target=drain)
        dr.start()
    t, res = m._new_relay(fds, mode, None)
    t.start()
    off = 0
    try:
        while off < len(payload):
            off += os.write(fw, payload[off:off + 65536])
    finally:
        os.close(fw)
    t.join(30)
    if dr is not None:
        dr.join(30)
        os.close(cr)
    return res, bytes(got), fds.names()


def t_relay():
    import random
    rnd = random.Random(5)
    payload = bytes(rnd.getrandbits(8) for _ in range(2097929))
    res, got, left = relay_case("plain", payload)
    check("R1 relay plain: R == D, equal sha, EOF, claimed both, registry empty",
          res["ok"] and res["read_bytes"] == res["delivered_bytes"] == len(payload) and got == payload
          and res["read_sha256"] == res["delivered_sha256"] == sha(payload) and left == []
          and res["fds_claimed"] == {"fifo_read": True, "cpw": True}, read=res["read_bytes"])
    res, got, left = relay_case("truncate", payload)
    check("R2 relay truncate: D == R - 2", res["ok"] and res["delivered_bytes"] == len(payload) - 2
          and got == payload[:-2] and res["withheld_bytes"] == 2)
    res, got, left = relay_case("suffix", payload)
    check("R3 relay suffix: D == R + 5", res["ok"] and res["delivered_bytes"] == len(payload) + 5
          and got == payload + m.SUFFIX and res["suffix_delivered_bytes"] == 5)
    res, got, left = relay_case("plain", payload, close_reader_first=True)
    check("R4 relay EPIPE: delivery_error EPIPE, 0 delivered, EOF seen, all bytes read, no close error",
          str(res.get("delivery_error", "")).startswith("EPIPE") and res["delivered_bytes"] == 0
          and res["fifo_eof_seen"] is True and res["read_bytes"] == len(payload) and res["close_errors"] == [],
          err=res.get("delivery_error"))
    fds = m.Fds()
    fr, fw = os.pipe()
    fds.put("fifo_read", fr)  # 'cpw' never registered: incomplete handoff
    res = {"ok": False, "mode": "plain"}
    m._relay(fds, res, "plain", None)
    try:
        os.fstat(fr)
        fr_closed = False
    except OSError:
        fr_closed = True
    os.close(fw)
    check("R5 incomplete relay handoff: relay_exception, claimed descriptor closed, not ok",
          res["ok"] is False and "handoff incomplete" in res.get("relay_exception", "") and fr_closed,
          exc=res.get("relay_exception"))


# --- evaluate(): synthetic records
def good_rec(item):
    n = 1000
    return {"children": {"solver": {"rc": 20}, "checker": {"rc": 0}},
            "writers": {k: {"ok": True, "thread_finished": True, "written": item["expected_solver_feed_bytes"],
                            "sha256": item["expected_solver_feed_sha256"]} for k in ("solver_feed", "checker_feed")},
            "relay": {"ok": True, "fifo_eof_seen": True, "thread_finished": True, "close_errors": [], "mode": "plain",
                      "withheld_bytes": 0, "read_bytes": n, "delivered_bytes": n, "read_sha256": "a" * 64,
                      "delivered_sha256": "a" * 64},
            "safety_stop_reason": None, "sigterm_grace_exceeded": False, "solver_status_lines": ["s UNSATISFIABLE"],
            "checker_has_verified_line": True, "checker_has_not_verified": False, "checker_has_timeout": False,
            "checker_parsed_header_counts": item["expected_checker_header_counts"], "checker_early_eof_marker": False,
            "checker_parsed_proof_bytes": n,
            "lane_scanner": {"started": True, "scans": 3, "failures": 0, "failed": None, "alive_after_join": False},
            "threads": {"writers_started": ["checker_feed", "solver_feed"], "relay_started": True, "unfinished": []},
            "stop_latched_during_pipeline": None, "helper_survivors": [],
            "pre_evaluation_check": {"checked": True, "stop_signal": None, "scanner_failed": None,
                                     "helper_survivors": []}}


def t_evaluate():
    leaf_item = dict(ITEM, kind="leaf")
    for kind_item in (ITEM, leaf_item):
        v, _r, _c = m.evaluate(good_rec(kind_item), kind_item)
        check("E0 %s: complete synthetic record is PASS" % kind_item["kind"], v == "PASS", verdict=v)
    muts = {
        "SIGTERM latched during pipeline": lambda r: r.update(stop_latched_during_pipeline="SIGTERM"),
        "SIGTERM latched by evaluation": lambda r: r["pre_evaluation_check"].update(stop_signal="SIGTERM"),
        "pre-evaluation check missing": lambda r: r.pop("pre_evaluation_check"),
        "scanner failure latched": lambda r: r["lane_scanner"].update(failed={"error": "x"}, failures=1),
        "scanner failure only at evaluation": lambda r: r["pre_evaluation_check"].update(scanner_failed={"e": 1}),
        "scanner alive after join": lambda r: r["lane_scanner"].update(alive_after_join=True),
        "unfinished thread": lambda r: r["threads"].update(unfinished=["relay"]),
        "writer never started": lambda r: r["threads"].update(writers_started=["checker_feed"]),
        "helper survivor": lambda r: r.update(helper_survivors=[{"pid": 1}]),
        "relay R != D": lambda r: r["relay"].update(delivered_bytes=999),
        "N != D": lambda r: r.update(checker_parsed_proof_bytes=1001),
        "no FIFO EOF": lambda r: r["relay"].update(fifo_eof_seen=False),
        "feed sha mismatch": lambda r: r["writers"]["solver_feed"].update(sha256="0" * 64),
        "spawn error": lambda r: r.update(solver_spawn_error="x"),
    }
    for name, mut in muts.items():
        for kind_item in (ITEM, leaf_item):
            r = good_rec(kind_item)
            mut(r)
            v, why, _c = m.evaluate(r, kind_item)
            check("E1 %s %s -> UNKNOWN" % (kind_item["kind"], name), v == "UNKNOWN", reasons=why[-3:])
    ctl = dict(ITEM, kind="selftest", mode="negative")
    r = good_rec(ctl)
    r["children"]["checker"]["rc"] = 1
    r.update(checker_has_verified_line=False, checker_has_not_verified=True, checker_line_s_NOT_VERIFIED_exact=True)
    v, why, _c = m.evaluate(r, ctl)
    check("E2 negative control with all observations: AS_PREREGISTERED_NOT_VERIFIED", v == "AS_PREREGISTERED_NOT_VERIFIED",
          verdict=v, reasons=why)
    r["pre_evaluation_check"]["stop_signal"] = "SIGTERM"
    v, why, _c = m.evaluate(r, ctl)
    check("E3 the same control with a latched SIGTERM: INVALID_CONTROL", v == "INVALID_CONTROL", reasons=why)
    r = good_rec(dict(ITEM, kind="selftest", mode="refutation"))
    r["lane_scanner"]["alive_after_join"] = True
    v, why, _c = m.evaluate(r, dict(ITEM, kind="selftest", mode="refutation"))
    check("E4 refutation control with a live scanner: INVALID_CONTROL", v == "INVALID_CONTROL", reasons=why)


# --- E: post-gate identity
def t_post_gate():
    py = os.path.realpath(sys.executable)
    pre = {"python": {"realpath": py, "sha256": m.sha_file(py)}, "admission_controls": []}
    script_sha = m.sha_file(m.SCRIPT)
    pg = m.post_gate_identity({"kind": "selftest"}, pre, script_sha, {})
    check("PG1 controls: script, python, cadical, drat-trim re-hashed equal -> ok",
          pg["ok"] and pg["hashed"]["cadical_sha256"] == m.CADICAL_SHA and pg["hashed"]["drat_trim_sha256"] == m.DRAT_SHA,
          problems=pg["problems"], seconds=pg["seconds"])
    bad = dict(pre, python={"realpath": py, "sha256": "0" * 64})
    pg = m.post_gate_identity({"kind": "selftest"}, bad, script_sha, {})
    check("PG2 python hash differs from the PRE-EXEC record -> refuse", not pg["ok"], problems=pg["problems"])
    pg = m.post_gate_identity({"kind": "selftest"}, pre, "f" * 64, {})
    check("PG3 script hash differs -> refuse", not pg["ok"], problems=pg["problems"])
    pg = m.post_gate_identity({"kind": "leaf"}, pre, script_sha, {})
    check("PG4 leaf without the five v5d control receipts -> refuse (controls re-validated)",
          not pg["ok"] and any("receipt missing" in x for x in pg["problems"]), problems=pg["problems"][:3])
    pg = m.post_gate_identity({"kind": "selftest"}, pre, script_sha, {"signal": "SIGTERM"})
    check("PG5 SIGTERM latched after gate success -> refuse", not pg["ok"], problems=pg["problems"])


# --- H: the twelve direct leaves regenerated in memory and bound to RESULT 65311ab0 + MANIFEST 355b3380
def t_leaves():
    ctx = m.load_strengthened(m.load_inputs(lambda s: None), lambda s: None)
    CTX["ctx"] = ctx
    bres = json.loads(open(m.BIND_DIR + "/RESULT.json", "rb").read())
    man = json.loads(open(os.path.join(m.LANE, m.MANIFEST_REL), "rb").read())
    bl = {x["id"]: x["cnf_sha256"] for x in bres["leaves"]}
    ml = {x["id"]: x["cnf_sha256"] for x in man["cases"]}
    rows, ok = {}, True
    for lid in m.DIRECT_LEAVES:
        it = {"kind": "leaf", "id": lid}
        s_parts, c_parts = m.item_parts(it, ctx)
        hs, ns = m.sha_parts(s_parts)
        hc, nc = m.sha_parts(c_parts)
        good = (hs == hc == bl[lid] == ml[lid] == ctx["cases"][lid]["cnf_sha256"] and ns == nc
                == ctx["cases"][lid]["cnf_bytes"] and m.item_label(it) == "v5d-" + lid
                and m.header_counts(c_parts[0]) == [509915, 5740268])
        ok = ok and good
        rows[lid] = {"sha256": hs, "bytes": ns, "ok": good}
    check("H1 twelve direct leaves: regenerated bytes == parent binding RESULT leaf hash == MANIFEST cnf_sha256",
          ok and len(rows) == 12 and ctx["info"]["parent_binding"]["result_sha256"] == m.BIND_RESULT_SHA
          and m.sha_file(os.path.join(m.LANE, m.MANIFEST_REL)) == m.PINS[m.MANIFEST_REL]
          == "355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74", leaves=rows)
    check("H2 the four open P1 templates are not direct leaves; 16 manifest cases = 12 + 4",
          set(m.DIRECT_LEAVES) | {"P1-B1", "P1-B2", "P1-B3", "P1-B5"} == set(ml) and len(set(m.DIRECT_LEAVES)) == 12
          and not {"P1-B1", "P1-B2", "P1-B3", "P1-B5"} & set(m.DIRECT_LEAVES))
    for fid in m.FORMULAS:
        s_parts, _c = m.item_parts({"kind": "formula", "id": fid}, ctx)
        h, n = m.sha_parts(s_parts)
        ok = ok and h == m.FORMULAS[fid][2]
    check("H3 the six strengthened formulas still compose to their bound hashes (load_strengthened with the v4 pins)",
          ok, pins=sorted(os.path.basename(p) for p in ctx["strong_info"]["pins_verified"]))


# --- v5c F1: worker state before the claim, claimed descriptors closed on every exit, handles kept before start
CTX = {}


def closed(fd):
    try:
        os.fstat(fd)
        return False
    except OSError:
        return True


def t_f1():
    real_sha = m.hashlib.sha256

    def boom(*_a, **_k):
        raise MemoryError("injected hash construction failure")
    fds = m.Fds()
    r, w = os.pipe()
    fds.put("w", w)
    m.hashlib.sha256 = boom
    try:
        try:
            m._writer(fds, "w", [b"x"], {"ok": False})
            raised = None
        except MemoryError as e:
            raised = repr(e)
    finally:
        m.hashlib.sha256 = real_sha
    still = fds.names() == ["w"] and not closed(w)
    for x in fds.take("w") + [r]:
        os.close(x)
    check("F1a writer state construction fails: nothing claimed, the descriptor stays registered for the cleanup",
          raised is not None and still, raised=raised)
    fds = m.Fds()
    fr, fw = os.pipe()
    cr, cw = os.pipe()
    fds.put("fifo_read", fr)
    fds.put("cpw", cw)
    m.hashlib.sha256 = boom
    try:
        try:
            m._relay(fds, {"ok": False}, "plain", None)
            raised = None
        except MemoryError as e:
            raised = repr(e)
    finally:
        m.hashlib.sha256 = real_sha
    still = sorted(fds.names()) == ["cpw", "fifo_read"]
    for x in fds.take("fifo_read", "cpw") + [fw, cr]:
        os.close(x)
    check("F1b relay state construction fails: nothing claimed, both descriptors stay registered",
          raised is not None and still, raised=raised)
    fds = m.Fds()
    r, w = os.pipe()
    fds.put("w", w)
    res = {"ok": False}
    m._writer(fds, "w", [12345], res)  # memoryview(12345) raises TypeError after the claim
    ok = closed(w) and fds.names() == [] and res["ok"] is False and "TypeError" in res.get("error", "")
    os.close(r)
    check("F1c writer exception after the claim: the worker's finally closes its descriptor once", ok, res=res)

    class Hold:
        def wait(self, _t):
            raise KeyboardInterrupt("injected after the claim")
    fds = m.Fds()
    fr, fw = os.pipe()
    cr, cw = os.pipe()
    fds.put("fifo_read", fr)
    fds.put("cpw", cw)
    os.write(fw, b"abc")
    res = {"ok": False}
    try:
        m._relay(fds, res, "plain", Hold())
        raised = None
    except KeyboardInterrupt as e:
        raised = repr(e)
    ok = raised is not None and closed(fr) and closed(cw) and fds.names() == [] and res.get("close_errors") == []
    os.close(fw)
    os.close(cr)
    check("F1d relay BaseException after the claim: both claimed descriptors closed by its finally, then re-raised",
          ok, raised=raised, read=res.get("read_bytes"))
    saved = (m.DESK, m.TMP, m.lane_scan)
    m.DESK, m.TMP = UDIR, UDIR + "/tmp"
    m.lane_scan = lambda: ([], None)
    try:
        rec, v, why, crit, leak = pipe_run("relay-start-interrupted", start_fail="relay-after")
    finally:
        m.DESK, m.TMP, m.lane_scan = saved
    r = rec["relay"]
    check("F1e start() interrupted after the relay thread started: handle kept, thread joined and reported, it "
          "claimed and closed fifo_read/cpw, the cleanup closed only keepalive and ccw, no fd leak, UNKNOWN",
          v == "UNKNOWN" and "exception" in rec and r.get("thread_started") is True and r.get("thread_finished") is True
          and r.get("fds_claimed") == {"fifo_read": True, "cpw": True}
          and sorted(rec["fds_closed_by_cleanup"]) == ["ccw", "keepalive"] and not leak,
          verdict=v, relay={k: r.get(k) for k in ("thread_started", "thread_finished", "fds_claimed", "fifo_eof_seen")},
          closed_by_cleanup=rec["fds_closed_by_cleanup"], leak=leak)


# --- v5c F2: bookkeeping before the spawn; one enclosing scope from the spawn through the cleanup
def t_f2():
    import inspect
    src = inspect.getsource(m.run_helper)
    check("F2a bookkeeping (chunks/err/sel/fatal/p) is assigned before subprocess.Popen inside one try",
          src.index("chunks, err, sel, fatal, p = ") < src.index("subprocess.Popen(") and
          src.index("try:  # (F2) the one enclosing") < src.index("subprocess.Popen("))
    saved = m.HELPER_DEADLINE
    m.HELPER_DEADLINE = None  # 'deadline = time.monotonic() + HELPER_DEADLINE' raises right after the spawn
    try:
        f0 = open_fds()
        rc, out, err = m.run_helper(SLEEPER)
    finally:
        m.HELPER_DEADLINE = saved
    check("F2b exception on the first statement after the spawn: SIGTERM, bounded reap (rc -15), closes, no survivor, "
          "no fd leak", rc == -15 and "supervision raised TypeError" in err and "SIGTERM sent" in err
          and not m.HELPER_SURVIVORS and open_fds() == f0, rc=rc, err=err)


# --- v5c F3: the shared item validator in run and assemble
def selftest_items():
    return [{"item": "selftest:" + n, "kind": "selftest", "name": n, "mode": md, "relay_mode": m.RELAY_MODES[md],
             "early_close_control": md == "early-close", "preregistered_verdict": m.SELFTEST_WANT[md]}
            for n, (_s, _c, md) in m.SELFTESTS.items()]


def t_f3():
    ctx = CTX["ctx"]
    leaf = lambda lid: {"item": "leaf:" + lid, "kind": "leaf", "id": lid,
                        "parent_binding_result_sha256": m.BIND_RESULT_SHA, "manifest_sha256": m.PINS[m.MANIFEST_REL],
                        "bound_cnf_sha256": ctx["cases"][lid]["cnf_sha256"],
                        "expected_solver_feed_sha256": ctx["cases"][lid]["cnf_sha256"],
                        "expected_solver_feed_bytes": ctx["cases"][lid]["cnf_bytes"],
                        "expected_checker_feed_sha256": ctx["cases"][lid]["cnf_sha256"],
                        "expected_checker_feed_bytes": ctx["cases"][lid]["cnf_bytes"],
                        "parent_binding_result_cnf_sha256": ctx["cases"][lid]["binding_cnf_sha256"],
                        "manifest_cnf_sha256": ctx["cases"][lid]["manifest_cnf_sha256"],
                        "expected_checker_header_counts": [509915, 5740268], "projected_peak_bytes": m.FLOOR_HIGH}
    bad_relay = selftest_items()
    bad_relay[0] = dict(bad_relay[0], relay_mode="suffix")
    cases = [
        ("F3a five selftest items valid", selftest_items(), True),
        ("F3b the twelve direct leaves valid", [leaf(x) for x in m.DIRECT_LEAVES], True),
        ("F3c leaf:P1-B1 (correct bound fields) refused", [leaf("P1-B1")], False),
        ("F3d unknown formula refused", [{"item": "formula:P1-B9.M2", "kind": "formula", "id": "P1-B9.M2"}], False),
        ("F3e mixed kinds refused", selftest_items()[:1] + [leaf("P0-B4")], False),
        ("F3f duplicate refused", [leaf("P0-B4"), leaf("P0-B4")], False),
        ("F3g selftest with an altered relay mode refused", bad_relay, False),
        ("F3h empty item list refused", [], False),
        ("F3i item spec mismatch refused", [dict(leaf("P0-B4"), item="leaf:P0-B5")], False),
    ]
    for name, items, want in cases:
        probs = m.validate_items(items)
        check(name, (not probs) == want, problems=probs[:3])
    py = os.path.realpath(sys.executable)
    pre = {"schema": "moqls8-strengthened-parent-replay-preexec/4", "note": "hand-built by the v5d unit check; run "
           "must refuse it", "script": {"path": m.SCRIPT_REL, "sha256": m.sha_file(m.SCRIPT)},
           "python": {"executable": sys.executable, "realpath": py, "sha256": m.sha_file(py)},
           "inputs": ctx["info"], "admission_controls": [], "items": [leaf("P1-B1")]}
    path = UDIR + "/PRE-EXEC-handbuilt-leaf-P1-B1.json"
    m.write_json_x(path, pre)
    logs0 = sorted(os.listdir(DESK + "/logs"))
    try:
        m.cmd_run([path])
        msg = None
    except SystemExit as e:
        msg = str(e)
    check("F3j run refuses a hand-built PRE-EXEC with leaf:P1-B1 before any regeneration, log or launch",
          msg is not None and "P1-B1" in msg and "refused" in msg and sorted(os.listdir(DESK + "/logs")) == logs0,
          msg=msg)
    out = UDIR + "/RESULT-handbuilt-must-not-exist.json"
    try:
        m.cmd_assemble([out, path])
        msg = None
    except SystemExit as e:
        msg = str(e)
    check("F3k assemble refuses the same PRE-EXEC and writes nothing",
          msg is not None and "refused" in msg and not os.path.lexists(out), msg=msg)


# --- v5c F4: parent M8 lane escalation (11 GiB lane limit; this desk counted as max(measured, reservation))
def fake_lane(rss):
    return lambda: ([{"pid": 999999, "ppid": 1, "comm": "python3", "native": False, "rss_bytes": rss, "cpu_ns": 0,
                      "state": "S", "cwd": "/x/moqls8-problem16", "args": "fake lane process"}], None)


def t_f4():
    G = 1 << 30
    check("F4a lane RSS limit 11 GiB = 11,811,160,064 B for admission and in flight; busy cap 4, mine 2",
          m.LANE_RSS_LIMIT == 11811160064 and m.GATE_RSS == m.STOP_LANE_RSS == m.LANE_RSS_LIMIT
          and m.LANE_BUSY_CAP == 4 and m.MINE == 2)
    d = m.lane_decision()
    check("F4b parent decision file re-hashed b9886e24...09ec", d["sha256"] == m.LANE_DECISION_SHA
          == "b9886e242764750f55a2393323dfa7da7eb7696554d493bb107cd5f3815209ec", path=d["path"])
    saved = (m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW)
    try:
        m.WAIT_POLL, m.HOT_WINDOW = 0, 0.01
        m.lane_scan, m.WAIT_BUDGET = fake_lane(10 * G), 3600
        g = m.gate("unit-f4-pass", 512 << 20, {"used": 0.0}, lambda s: None, {}, stable=False)
        check("F4c gate: other lane 10 GiB + reservation 0.5 GiB <= 11 GiB launches (v5b would refuse at 7.6 GiB)",
              g["launch"] is True and g["lane_other_rss_at_launch"] == 10 * G, launch=g["launch"])
        m.lane_scan, m.WAIT_BUDGET = fake_lane(10 * G + 600 * (1 << 20)), 0
        g = m.gate("unit-f4-refuse", 512 << 20, {"used": 0.0}, lambda s: None, {}, stable=False)
        check("F4d gate: other lane 10.59 GiB + reservation 0.5 GiB > 11 GiB refuses (ok_rss False)",
              g["launch"] is False and g["samples"][0]["ok_rss"] is False, launch=g["launch"],
              deferred=g.get("deferred"))
    finally:
        m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW = saved
    saved = (m.DESK, m.TMP, m.lane_scan)
    m.DESK, m.TMP = UDIR, UDIR + "/tmp"
    try:
        m.lane_scan = fake_lane(95 * G // 10)
        rec, v, why, crit, leak = pipe_run("lane-9.5GiB", projected=1 * G, slow=1.5)
        check("F4e in flight: other lane 9.5 GiB + max(desk, reservation 1 GiB) <= 11 GiB runs to PASS",
              v == "PASS" and rec["safety_stop_reason"] is None and rec["lane_rss_limit_bytes"] == 11811160064
              and rec["peak_lane_reserved_rss_bytes"] >= 95 * G // 10 + G, verdict=v, reasons=why,
              reserved=rec["peak_lane_reserved_rss_bytes"], measured=rec["peak_lane_total_rss_bytes"])
        m.lane_scan = fake_lane(75 * G // 10)
        rec, v, why, crit, leak = pipe_run("lane-7.5GiB-res-4GiB", projected=4 * G, slow=1.5)
        reason = rec.get("safety_stop_reason") or ""
        check("F4f in flight: other lane 7.5 GiB + reservation 4 GiB > 11 GiB stops although measured total "
              "< 11 GiB (the declared reservation counts)", v == "UNKNOWN" and "> 11 GiB" in reason
              and "reservation" in reason and rec["peak_lane_total_rss_bytes"] < m.LANE_RSS_LIMIT and not leak,
              verdict=v, reason=reason, measured=rec["peak_lane_total_rss_bytes"])
    finally:
        m.DESK, m.TMP, m.lane_scan = saved


# --- v5d F1': Fds.take builds its result before removing; the relay closes both descriptors before diagnostics
def t_f1p():
    import inspect
    src = inspect.getsource(m.Fds.take)
    check("F1'a Fds.take: the result list is allocated before the first registry pop",
          src.index("[None] * len(names)") < src.index("self._fds.pop("))
    fds = m.Fds()
    fds.put("a", 101)
    fds.put("b", 102)
    got = fds.take("a", "missing", "b")
    check("F1'b Fds.take semantics: values in order, None for absent names, entries removed", got == [101, None, 102]
          and fds.names() == [], got=got)
    rsrc = inspect.getsource(m._relay)
    i_alloc = rsrc.index("close_errors, close_status = [], [None, None]")
    i_claim = rsrc.index('src, dst = fds.take("fifo_read", "cpw")')
    i_close_dst, i_close_src = rsrc.index("os.close(dst)"), rsrc.index("os.close(src)")
    i_diag = rsrc.index('close_errors.append("dst')
    check("F1'c relay: cleanup state allocated before the claim; both closes precede any diagnostic allocation",
          i_alloc < i_claim < i_close_dst < i_close_src < i_diag)
    fr, fw = os.pipe()
    a, b = os.pipe()
    os.close(b)  # 'cpw' is a descriptor number that is already closed: delivery and close both fail with EBADF
    os.write(fw, b"xyz")
    os.close(fw)
    fds = m.Fds()
    fds.put("fifo_read", fr)
    fds.put("cpw", b)
    res = {"ok": False}
    m._relay(fds, res, "plain", None)
    os.close(a)
    check("F1'd relay with a failing dst close: src still closed, the close error recorded afterwards, not ok",
          closed(fr) and res["close_errors"] and res["close_errors"][0].startswith("dst: ")
          and res["ok"] is False and res.get("fifo_eof_seen") is True, close_errors=res["close_errors"],
          delivery=res.get("delivery_error"))


# --- v5d F4': admission uses other + max(fresh measured desk RSS, reservation); unreadable desk RSS refuses
def t_f4p():
    saved = (m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW, m.taskinfo)
    try:
        m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW = 0, 0, 0.01
        desk = m.taskinfo(os.getpid())[0]
        projected = 1 << 20
        other = m.LANE_RSS_LIMIT - projected - desk // 2  # other + reservation fits; other + measured desk does not
        m.lane_scan = fake_lane(other)
        g = m.gate("unit-f4p-desk", projected, {"used": 0.0}, lambda s: None, {}, stable=False)
        s0 = g["samples"][0]
        check("F4'a measured desk RSS above the reservation: other + max(desk, projected) > 11 GiB refuses although "
              "other + projected fits", desk > projected and other + projected <= m.LANE_RSS_LIMIT
              and s0["ok_rss"] is False and s0["desk_rss_bytes"] >= desk // 2 and g["launch"] is False,
              desk=desk, other=other, sample_desk=s0["desk_rss_bytes"])
        real_ti, me = m.taskinfo, os.getpid()
        m.taskinfo = lambda pid: None if pid == me else real_ti(pid)
        m.lane_scan = fake_lane(1 << 30)
        g = m.gate("unit-f4p-unreadable", projected, {"used": 0.0}, lambda s: None, {}, stable=False)
        s0 = g["samples"][0]
        check("F4'b unreadable desk RSS at admission refuses", s0["ok_rss"] is False and s0["desk_rss_bytes"] is None
              and g["launch"] is False, sample=s0["desk_rss_bytes"])
        m.taskinfo = real_ti
        m.WAIT_BUDGET = 3600
        m.lane_scan = fake_lane(1 << 30)
        g = m.gate("unit-f4p-pass", projected, {"used": 0.0}, lambda s: None, {}, stable=False)
        check("F4'c small other lane with measured desk: launches", g["launch"] is True,
              desk=g["samples"][-1]["desk_rss_bytes"])
    finally:
        m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW, m.taskinfo = saved


def main():
    started = m.now()
    for name, fn in (("handoff", t_handoff), ("relay", t_relay), ("helper", t_helper), ("lane_scan", t_lane_scan),
                     ("scanner", t_scanner), ("stability", t_stability), ("evaluate", t_evaluate),
                     ("post_gate", t_post_gate), ("pipeline", t_pipeline), ("leaves", t_leaves),
                     ("f1", t_f1), ("f2", t_f2), ("f3", t_f3), ("f4", t_f4), ("f1p", t_f1p), ("f4p", t_f4p)):
        run(name, fn)
    fails = [r["check"] for r in RESULTS if not r["ok"]]
    out = {"schema": "moqls8-replay-v5d-unitcheck/1", "started_at": started, "finished_at": m.now(),
           "target": TARGET, "target_sha256": m.sha_file(TARGET),
           "unitcheck_script": os.path.realpath(__file__), "unitcheck_sha256": m.sha_file(os.path.realpath(__file__)),
           "python": {"executable": sys.executable, "version": sys.version.split()[0]},
           "native_processes_started": "none (cadical and drat-trim replaced by python -c stubs; ps/lsof helpers "
                                       "replaced by fakes)",
           "checks": RESULTS, "failed": fails, "status": "PASS" if not fails else "FAIL"}
    with open(OUT, "x") as f:
        json.dump(out, f, indent=1, default=str)
        f.write("\n")
    print("UNITCHECK %s status %s failed %d of %d sha256 %s" % (OUT, out["status"], len(fails), len(RESULTS),
                                                                  m.sha_file(OUT)))


if __name__ == "__main__":
    main()
