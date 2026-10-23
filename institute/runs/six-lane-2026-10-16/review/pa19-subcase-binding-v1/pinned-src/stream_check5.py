#!/usr/bin/env python3
"""Revision 5 of the online proof-checking helpers (earlier revisions kept unchanged).

Change (parent finding 2026-10-17 ~12:20): lrat-check from the drat-trim repository accepts an
empty-clause LRAT step without a conflict (unsound), so it is no longer used at all. The only
acceptance criterion is drat-trim: it must exit ON ITS OWN with exit code 0 and print
's VERIFIED' while checking the solver's binary DRAT proof streamed into its stdin (-i).
  kissat_drat : kissat 4.0.4 -q -f --seed=1 --time=LIMIT, binary DRAT
  cadical_drat: cadical 3.0.1 -q -t LIMIT (binary DRAT, --lrat=false)
Process policy as revision 4: native limits (solver; drat-trim -t LIMIT+BUDGET because its
clock starts before the streamed solve), bounded waits, SIGTERM only, survivors left running
and reported, interrupted checker => UNKNOWN. FIFO directories get a unique suffix
(pid + nanosecond time) so a rerun never reuses a FIFO of an earlier run.
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
GRACE = 60
TERM_WAIT = 60
MAX_CHECK_BUDGET = 1200


def _fifos(wdir, names):
    wdir = "%s_%d_%d" % (wdir, os.getpid(), time.time_ns())
    os.makedirs(wdir, exist_ok=True)
    out = {}
    for n in names:
        p = os.path.join(wdir, n)
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


def stop_cooperatively(p, bound, events, name):
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


def _drat_stream(cnf_bytes, wdir, limit, check_budget, solver_cmd, solver_name):
    cb = int(min(check_budget, MAX_CHECK_BUDGET))
    F = _fifos(wdir, ["cnf_s", "cnf_d", "prf"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "%s; binary DRAT streamed to drat-trim -i -t %d" % (" ".join(solver_cmd(0, "CNF", "PROOF", limit)), int(limit) + cb),
           "stream_check_revision": 5, "check_budget": cb, "fifo_dir": os.path.relpath(os.path.dirname(F["prf"]), LANE)}
    events = []
    dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-t", str(int(limit) + cb)], stdin=True)
    hp, npf = hashlib.sha256(), [0]
    fw = threading.Thread(target=_forward, args=(F["prf"], dt.stdin, hp, npf), daemon=True)
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_d", "cnf_s")]
    for t in [fw] + wr:
        t.start()
    t0 = time.time()
    sp, sp_out, sp_t = _start(solver_cmd(1, F["cnf_s"], F["prf"], limit))
    s_stop = stop_cooperatively(sp, limit + GRACE, events, solver_name)
    rc = sp.returncode if s_stop == "self" else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["solver_stop"] = s_stop
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if s_stop != "running":
        sp_t.join(timeout=10)
    res["solver_out"] = b"".join(sp_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if s_stop == "running":
        res.update({"events": events, "checked": False, "drat_trim_verified": False, "checker_interrupted": True})
        return res
    unsat = res["status"] == "UNSAT"
    fw.join(timeout=(cb if unsat else GRACE))
    dt_stop = stop_cooperatively(dt, (cb + GRACE) if unsat else GRACE, events, "drat-trim")
    if dt_stop != "running":
        dt_t.join(timeout=10)
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["drat_sha256"] = hp.hexdigest()
    res["drat_bytes"] = npf[0]
    dto = b"".join(dt_out).decode(errors="replace")
    res["drat_trim"] = {"stop": dt_stop, "rc": dt.returncode if dt_stop != "running" else None,
                        "says_verified": "s VERIFIED" in dto, "says_timeout": "s TIMEOUT" in dto}
    res["checker_interrupted"] = dt_stop != "self"
    res["drat_trim_verified"] = dt_stop == "self" and dt.returncode == 0 and res["drat_trim"]["says_verified"]
    res["events"] = events
    res["checked"] = unsat and res["drat_trim_verified"]
    return res


def _kissat_cmd(real, cnf, prf, limit):
    return [KISSAT, "-q", "-f", "--seed=1", "--time=%d" % int(limit), cnf, prf]


def _cadical_cmd(real, cnf, prf, limit):
    return [CADICAL, "-q", "-t", str(int(limit)), cnf, prf]


def kissat_drat(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_stream(cnf_bytes, wdir, limit, check_budget, _kissat_cmd, "kissat")


def cadical_drat(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_stream(cnf_bytes, wdir, limit, check_budget, _cadical_cmd, "cadical")


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
