#!/usr/bin/env python3
"""Revision 3 of the online proof-checking helpers (stream_check.py and stream_check2.py are
kept unchanged as the record of earlier results).

Policy (parent safety rule 2026-10-17 + corrections):
  * no SIGKILL anywhere; subprocess.run(timeout=...) is never used;
  * solvers have native limits (kissat --time=T, cadical -t T); drat-trim has native
    -t CHECK_BUDGET; every wait is bounded; a process still running after its bound gets
    SIGTERM (Popen.terminate) and a bounded wait; a survivor is LEFT RUNNING and reported;
  * per-case checker wall time is bounded by CHECK_BUDGET (default 1200 s, never more) plus
    a fixed grace;
  * a checker counts as passed only if it exited ON ITS OWN (no SIGTERM, not left running)
    with exit code 0 and printed its success line ('s VERIFIED' / 'c VERIFIED'). If any
    checker needed SIGTERM or was left running, the case is UNKNOWN (checked = False), even
    if partial output says VERIFIED;
  * checker exits are recorded explicitly (rc, self_exited, events).
Streams: kissat binary DRAT -> drat-trim -i (stdin) -> LRAT -> lrat-check, or CaDiCaL ASCII
LRAT -> lrat-check; CNF bytes from memory through FIFOs (fresh directory per case); SHA-256
of every stream recorded; nothing stored on disk except zero-size FIFOs.
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
GRACE = 60
TERM_WAIT = 60
MAX_CHECK_BUDGET = 1200


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
    try:
        fd = os.open(path, os.O_WRONLY | os.O_NONBLOCK)
        os.close(fd)
    except OSError:
        pass


def stop_cooperatively(p, bound, events, name):
    """wait up to `bound` s; then SIGTERM + wait TERM_WAIT s; never SIGKILL.
    Returns 'self' (exited on its own), 'term' (exited after SIGTERM) or 'running'."""
    try:
        p.wait(timeout=max(1.0, bound))
        return "self"
    except subprocess.TimeoutExpired:
        pass
    p.terminate()
    events.append({"process": name, "pid": p.pid, "action": "SIGTERM", "time": round(time.time(), 1)})
    try:
        p.wait(timeout=TERM_WAIT)
        return "term"
    except subprocess.TimeoutExpired:
        events.append({"process": name, "pid": p.pid, "action": "left-running", "time": round(time.time(), 1)})
        return "running"


def kissat_stream(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    cb = int(min(check_budget, MAX_CHECK_BUDGET))
    F = fifos(wdir, ["cnf_k", "cnf_d", "cnf_l", "prf", "lrat"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "kissat 4.0.4 -q -f --seed=1 --time=%d; DRAT streamed to drat-trim -i -t %d" % (int(limit), cb),
           "stream_check_revision": 3, "check_budget": cb}
    events = []
    lc, lc_out, lc_t = _start([LC, F["cnf_l"], "/dev/stdin"], stdin=True)
    dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-L", F["lrat"], "-t", str(cb)], stdin=True)
    hl, nl = hashlib.sha256(), [0]
    hp, npf = hashlib.sha256(), [0]
    fw_l = threading.Thread(target=_forward, args=(F["lrat"], lc.stdin, hl, nl), daemon=True)
    fw_p = threading.Thread(target=_forward, args=(F["prf"], dt.stdin, hp, npf), daemon=True)
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_d", "cnf_l", "cnf_k")]
    for t in [fw_l, fw_p] + wr:
        t.start()
    t0 = time.time()
    ks, ks_out, ks_t = _start([KISSAT, "-q", "-f", "--seed=1", "--time=%d" % int(limit), F["cnf_k"], F["prf"]])
    ks_stop = stop_cooperatively(ks, limit + GRACE, events, "kissat")
    rc = ks.returncode if ks_stop == "self" else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["solver_stop"] = ks_stop
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if ks_stop != "running":
        ks_t.join(timeout=10)
    res["solver_out"] = b"".join(ks_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if ks_stop == "running":
        res.update({"events": events, "checked": False, "drat_trim_verified": False, "lrat_verified": False,
                    "checker_interrupted": True})
        return res
    unsat = res["status"] == "UNSAT"
    fw_p.join(timeout=(cb if unsat else GRACE))
    dt_stop = stop_cooperatively(dt, (cb + GRACE) if unsat else GRACE, events, "drat-trim")
    if dt_stop != "running":
        dt_t.join(timeout=10)
        _release_reader(F["lrat"])
    remaining = max(GRACE, cb + 2 * GRACE - (time.time() - t1))
    fw_l.join(timeout=(remaining if unsat else GRACE))
    lc_stop = stop_cooperatively(lc, remaining if unsat else GRACE, events, "lrat-check")
    if lc_stop != "running":
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
    res["drat_trim"] = {"stop": dt_stop, "rc": dt.returncode if dt_stop != "running" else None,
                        "says_verified": "s VERIFIED" in dto}
    res["lrat_check"] = {"stop": lc_stop, "rc": lc.returncode if lc_stop != "running" else None,
                         "says_verified": "c VERIFIED" in lco.splitlines()}
    res["checker_interrupted"] = dt_stop != "self" or lc_stop != "self"
    res["drat_trim_verified"] = dt_stop == "self" and dt.returncode == 0 and res["drat_trim"]["says_verified"]
    res["lrat_verified"] = lc_stop == "self" and lc.returncode == 0 and res["lrat_check"]["says_verified"]
    res["events"] = events
    res["checked"] = unsat and not res["checker_interrupted"] and res["drat_trim_verified"] and res["lrat_verified"]
    return res


def cadical_stream(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    cb = int(min(check_budget, MAX_CHECK_BUDGET))
    F = fifos(wdir, ["cnf_c", "cnf_l2", "lrat2"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "cadical 3.0.1 -q -t %d --lrat=true --binary=false; LRAT streamed to lrat-check" % int(limit),
           "stream_check_revision": 3, "check_budget": cb}
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
    cs_stop = stop_cooperatively(cs, limit + GRACE, events, "cadical")
    rc = cs.returncode if cs_stop == "self" else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["solver_stop"] = cs_stop
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if cs_stop != "running":
        cs_t.join(timeout=10)
    res["solver_out"] = b"".join(cs_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if cs_stop == "running":
        res.update({"events": events, "checked": False, "lrat_verified": False, "checker_interrupted": True})
        return res
    _release_reader(F["lrat2"])
    unsat = res["status"] == "UNSAT"
    fw.join(timeout=(cb if unsat else GRACE))
    lc_stop = stop_cooperatively(lc, max(GRACE, cb + GRACE - (time.time() - t1)) if unsat else GRACE, events, "lrat-check")
    if lc_stop != "running":
        lc_t.join(timeout=10)
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["lrat_sha256"] = hl.hexdigest()
    res["lrat_bytes"] = nl[0]
    lco = b"".join(lc_out).decode(errors="replace")
    res["lrat_check"] = {"stop": lc_stop, "rc": lc.returncode if lc_stop != "running" else None,
                         "says_verified": "c VERIFIED" in lco.splitlines()}
    res["checker_interrupted"] = lc_stop != "self"
    res["lrat_verified"] = lc_stop == "self" and lc.returncode == 0 and res["lrat_check"]["says_verified"]
    res["events"] = events
    res["checked"] = unsat and not res["checker_interrupted"] and res["lrat_verified"]
    return res


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
