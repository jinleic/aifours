#!/usr/bin/env python3
"""Revision 2 of the online proof-checking helpers (stream_check.py is kept unchanged as the
record of what produced earlier results).

Process-stopping policy (parent safety rule, 2026-10-17): no SIGKILL anywhere.
  * solvers get native limits (kissat --time=T, cadical -t T); drat-trim gets its native -t;
  * every wait is bounded; if a process is still running after its bound it is sent SIGTERM
    (Popen.terminate) and waited for again (bounded); if it still runs it is LEFT RUNNING, its
    pid is recorded in the result ("unstopped") and the case is UNKNOWN;
  * subprocess.run(..., timeout=...) is never used (it would SIGKILL);
  * checkers are normally stopped by end-of-input: when the solver exits its proof stream
    closes, so lrat-check / drat-trim see EOF and finish on their own.
Streams: kissat binary DRAT -> drat-trim -i (stdin) -> LRAT -> lrat-check, or CaDiCaL ASCII
LRAT -> lrat-check; CNF bytes come from memory through FIFOs; SHA-256 of every stream is
recorded; nothing is stored on disk except zero-size FIFOs (fresh directory per case).
"""
import hashlib
import os
import subprocess
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"
CADICAL = "/opt/homebrew/bin/cadical"
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")
GRACE = 60  # seconds after a native limit before SIGTERM
TERM_WAIT = 60  # seconds after SIGTERM before giving up (process left running)


def fifos(wdir, names):
    os.makedirs(wdir, exist_ok=True)
    out = {}
    for n in names:
        p = os.path.join(wdir, n)
        if not os.path.exists(p):
            os.mkfifo(p)
        out[n] = p
    return out


def _writer(path, data):
    try:
        with open(path, "wb") as f:
            f.write(data)
    except OSError:
        pass


def _forward(src_path, dst_file, h, counter):
    try:
        with open(src_path, "rb") as f:
            while True:
                b = f.read(1 << 16)
                if not b:
                    break
                h.update(b)
                counter[0] += len(b)
                try:
                    dst_file.write(b)
                except (OSError, ValueError):
                    pass
    finally:
        try:
            dst_file.close()
        except (OSError, ValueError):
            pass


def _collect(stream, sink):
    for line in iter(stream.readline, b""):
        sink.append(line)
    stream.close()


def _start(cmd, stdin=False):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE if stdin else subprocess.DEVNULL,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sink = []
    t = threading.Thread(target=_collect, args=(p.stdout, sink), daemon=True)
    t.start()
    return p, sink, t


def _release_reader(path):
    # a thread blocked opening this FIFO for reading (writer never came) is released by a
    # non-blocking writer open + close; no process is signalled
    try:
        fd = os.open(path, os.O_WRONLY | os.O_NONBLOCK)
        os.close(fd)
    except OSError:
        pass


def stop_cooperatively(p, bound, log, name):
    """wait up to `bound` s; then SIGTERM and wait TERM_WAIT s; never SIGKILL.
    Returns True if the process exited."""
    try:
        p.wait(timeout=bound)
        return True
    except subprocess.TimeoutExpired:
        pass
    p.terminate()
    log.append({"process": name, "pid": p.pid, "action": "SIGTERM", "time": time.time()})
    try:
        p.wait(timeout=TERM_WAIT)
        return True
    except subprocess.TimeoutExpired:
        log.append({"process": name, "pid": p.pid, "action": "left-running", "time": time.time()})
        return False


def kissat_stream(cnf_bytes, wdir, limit, dt_limit=20000, check_bound=None):
    F = fifos(wdir, ["cnf_k", "cnf_d", "cnf_l", "prf", "lrat"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "kissat 4.0.4 -q -f --seed=1 --time=%d (binary DRAT streamed to drat-trim -i -t %d)"
                     % (int(limit), int(dt_limit)), "stream_check_revision": 2}
    events = []
    lc, lc_out, lc_t = _start([LC, F["cnf_l"], "/dev/stdin"], stdin=True)
    dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-L", F["lrat"], "-t", str(int(dt_limit))], stdin=True)
    hl, nl = hashlib.sha256(), [0]
    hp, npf = hashlib.sha256(), [0]
    fw_l = threading.Thread(target=_forward, args=(F["lrat"], lc.stdin, hl, nl), daemon=True)
    fw_p = threading.Thread(target=_forward, args=(F["prf"], dt.stdin, hp, npf), daemon=True)
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_d", "cnf_l", "cnf_k")]
    for t in [fw_l, fw_p] + wr:
        t.start()
    t0 = time.time()
    ks, ks_out, ks_t = _start([KISSAT, "-q", "-f", "--seed=1", "--time=%d" % int(limit), F["cnf_k"], F["prf"]])
    ok = stop_cooperatively(ks, limit + GRACE, events, "kissat")
    rc = ks.returncode if ok else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if ok:
        ks_t.join(timeout=10)
    res["solver_out"] = b"".join(ks_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    bound = check_bound if check_bound is not None else max(600, 4 * res["solve_seconds"])
    if not ok:
        # solver still running after SIGTERM: leave everything, report
        res.update({"unstopped": events, "checked": False, "drat_trim_verified": False, "lrat_verified": False})
        return res
    fw_p.join(timeout=bound)
    dt_ok = stop_cooperatively(dt, dt_limit + GRACE if res["status"] == "UNSAT" else GRACE, events, "drat-trim")
    if dt_ok:
        dt_t.join(timeout=10)
        _release_reader(F["lrat"])
    fw_l.join(timeout=bound)
    lc_ok = stop_cooperatively(lc, bound if res["status"] == "UNSAT" else GRACE, events, "lrat-check")
    if lc_ok:
        lc_t.join(timeout=10)
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["drat_sha256"] = hp.hexdigest()
    res["drat_bytes"] = npf[0]
    res["lrat_sha256"] = hl.hexdigest()
    res["lrat_bytes"] = nl[0]
    dto = b"".join(dt_out).decode(errors="replace")
    lco = b"".join(lc_out).decode(errors="replace")
    res["drat_trim_verified"] = dt_ok and "s VERIFIED" in dto
    res["lrat_verified"] = lc_ok and lc.returncode == 0 and "c VERIFIED" in lco.splitlines()
    res["events"] = events
    if not (dt_ok and lc_ok):
        res["unstopped"] = [e for e in events if e["action"] == "left-running"]
    res["checked"] = res["status"] == "UNSAT" and res["drat_trim_verified"] and res["lrat_verified"]
    return res


def cadical_stream(cnf_bytes, wdir, limit, check_bound=None):
    F = fifos(wdir, ["cnf_c", "cnf_l2", "lrat2"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "cadical 3.0.1 -q -t %d --lrat=true --binary=false (LRAT streamed to lrat-check)" % int(limit),
           "stream_check_revision": 2}
    events = []
    lc, lc_out, lc_t = _start([LC, F["cnf_l2"], "/dev/stdin"], stdin=True)
    hl, nl = hashlib.sha256(), [0]
    fw = threading.Thread(target=_forward, args=(F["lrat2"], lc.stdin, hl, nl), daemon=True)
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_l2", "cnf_c")]
    for t in [fw] + wr:
        t.start()
    t0 = time.time()
    cs, cs_out, cs_t = _start([CADICAL, "-q", "-t", str(int(limit)), "--lrat=true", "--binary=false",
                               F["cnf_c"], F["lrat2"]])
    ok = stop_cooperatively(cs, limit + GRACE, events, "cadical")
    rc = cs.returncode if ok else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if ok:
        cs_t.join(timeout=10)
    res["solver_out"] = b"".join(cs_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if not ok:
        res.update({"unstopped": events, "checked": False, "lrat_verified": False})
        return res
    _release_reader(F["lrat2"])
    bound = check_bound if check_bound is not None else max(600, 4 * res["solve_seconds"])
    fw.join(timeout=bound)
    lc_ok = stop_cooperatively(lc, bound if res["status"] == "UNSAT" else GRACE, events, "lrat-check")
    if lc_ok:
        lc_t.join(timeout=10)
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["lrat_sha256"] = hl.hexdigest()
    res["lrat_bytes"] = nl[0]
    lco = b"".join(lc_out).decode(errors="replace")
    res["lrat_verified"] = lc_ok and lc.returncode == 0 and "c VERIFIED" in lco.splitlines()
    res["events"] = events
    if not lc_ok:
        res["unstopped"] = [e for e in events if e["action"] == "left-running"]
    res["checked"] = res["status"] == "UNSAT" and res["lrat_verified"]
    return res


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
