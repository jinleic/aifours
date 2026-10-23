#!/usr/bin/env python3
"""Revision 10 of the online proof-checking helpers = revision 9 (strict drat-trim verdict) run in a
STAGED pipeline under a lane-wide CPU token semaphore (parent CPU accounting, 2026-10-17 14:4x):

* The solver (kissat 4.0.4 --seed=1, or CaDiCaL 3.0.1) writes its binary DRAT proof into a FIFO. A
  Python thread reads it, hashes it (SHA-256, byte count) and compresses it with zstd level 1 into
  memory. drat-trim starts only AFTER the solver has exited with UNSAT and reads the decompressed
  proof from stdin (-i). Solver and checker of one pipeline never run at the same time.
* Every pipeline holds ONE lane CPU token from CNF construction (when a callable is passed) through
  solver start to checker exit: an exclusive
  fcntl.flock on cycle2/tokens/tN for some N < COUNT, where COUNT is read from cycle2/tokens/COUNT
  at every acquisition (default 1). Hence the number of busy solver/checker processes started
  through this module is at most COUNT (Python controllers excluded, as agreed with the parent).
* RAM: the compressed buffer is capped (MAX_ZBUF bytes) and the raw proof is capped (MAX_RAW
  bytes); when a cap is hit the solver is stopped with SIGTERM and the case is UNKNOWN (no proof is
  ever written to disk). Checks of proofs larger than BIG raw bytes are serialized by an exclusive
  lock cycle2/tokens/bigmem. drat-trim's peak RSS is sampled every 5 s and recorded.
* Limits/stops as before: native solver limit, drat-trim -t BUDGET (its clock now starts after the
  solve), bounded waits, SIGTERM only, survivors left running and reported, interrupted => UNKNOWN.
  Acceptance (checked=True) iff: solver exited on its own with rc 20, no proof cap hit, drat-trim
  exited on its own with rc 0, the list of 's ' lines of its output (each stripped of '\\r') is exactly
  ['s VERIFIED'], and the SHA-256 and length of the proof replayed into drat-trim equal those of the
  streamed proof. Anything else is not checked (UNKNOWN for the case).
"""
import fcntl
import hashlib
import os
import subprocess
import threading
import time
from compression import zstd

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"
CADICAL = "/opt/homebrew/bin/cadical"
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
TOK = os.path.join(LANE, "cycle2", "tokens")
GRACE = 60
TERM_WAIT = 60
MAX_CHECK_BUDGET = 1200
MAX_ZBUF = 500 * 1024 * 1024
MAX_RAW = 1200 * 1024 * 1024
BIG = 300 * 1024 * 1024
DISK_FLOOR = 12000000000
SOLVER_INFO = {"kissat": {"version": "kissat 4.0.4 (/opt/homebrew/bin/kissat)", "seed": "--seed=1"},
               "cadical": {"version": "cadical 3.0.1 (/opt/homebrew/bin/cadical)", "seed": "default (no --seed option given)"}}


def disk_free_bytes(path=LANE):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def disk_free_ok(path=LANE):
    return disk_free_bytes(path) >= DISK_FLOOR


def token_count():
    try:
        return max(0, int(open(os.path.join(TOK, "COUNT")).read().split()[0]))
    except (OSError, ValueError, IndexError):
        return 1


class Token:
    """exclusive lane CPU token; polls every 2 s"""

    def __init__(self):
        os.makedirs(TOK, exist_ok=True)
        self.fd = None
        self.name = None
        self.waited = 0.0

    def __enter__(self):
        t0 = time.time()
        while True:
            for i in range(token_count()):
                p = os.path.join(TOK, "t%d" % i)
                fd = os.open(p, os.O_CREAT | os.O_RDWR)
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    os.close(fd)
                    continue
                self.fd, self.name = fd, "t%d" % i
                self.waited = round(time.time() - t0, 1)
                return self
            time.sleep(2)

    def __exit__(self, *a):
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)


class BigLock:
    def __init__(self, active):
        self.active = active
        self.fd = None

    def __enter__(self):
        if self.active:
            os.makedirs(TOK, exist_ok=True)
            self.fd = os.open(os.path.join(TOK, "bigmem"), os.O_CREAT | os.O_RDWR)
            fcntl.flock(self.fd, fcntl.LOCK_EX)
        return self

    def __exit__(self, *a):
        if self.fd is not None:
            fcntl.flock(self.fd, fcntl.LOCK_UN)
            os.close(self.fd)


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


def _rss_kb(pid):
    try:
        out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
        return int(out) if out else 0
    except (OSError, ValueError):
        return 0


def _drat_staged(cnf_source, wdir, limit, check_budget, solver_cmd, solver_name):
    """cnf_source: CNF bytes, or a callable returning them (then the CNF is built while the token is
    held, so Python encoding work is also covered by the token)"""
    with Token() as tok:
        t_enc = time.time()
        cnf_bytes = cnf_source() if callable(cnf_source) else cnf_source
        res = _drat_staged_locked(cnf_bytes, wdir, limit, check_budget, solver_cmd, solver_name)
        res["token"], res["token_wait_seconds"] = tok.name, tok.waited
        res["encode_seconds"] = round(res.pop("_t_solver_start") - t_enc, 2)
        return res


def _drat_staged_locked(cnf_bytes, wdir, limit, check_budget, solver_cmd, solver_name):
    cb = int(min(check_budget, MAX_CHECK_BUDGET))
    F = _fifos(wdir, ["cnf_s", "cnf_d", "prf"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "%s; binary DRAT staged (zstd-1 in memory) then drat-trim -i -t %d" % (
               " ".join(solver_cmd("CNF", "PROOF", limit)), cb),
           "solver_info": SOLVER_INFO[solver_name], "drat_trim_binary": "tools/drat-trim/drat-trim",
           "stream_check_revision": 10, "staged": True, "check_budget": cb,
           "fifo_dir": os.path.relpath(os.path.dirname(F["prf"]), LANE)}
    events = []
    hp, nraw = hashlib.sha256(), [0]
    zc = zstd.ZstdCompressor(level=1)
    chunks, zbytes, over = [], [0], [None]
    sp_holder = {}

    def reader():
        with open(F["prf"], "rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""):
                if over[0]:
                    continue  # drain so the solver is not blocked while it is being stopped
                hp.update(b)
                nraw[0] += len(b)
                z = zc.compress(b)
                if z:
                    chunks.append(z)
                    zbytes[0] += len(z)
                if nraw[0] > MAX_RAW or zbytes[0] > MAX_ZBUF:
                    over[0] = "raw" if nraw[0] > MAX_RAW else "zbuf"
                    p = sp_holder.get("p")
                    if p is not None and p.poll() is None:
                        p.terminate()
                        events.append({"process": solver_name, "pid": p.pid, "action": "SIGTERM (proof size cap %s)" % over[0],
                                       "time": round(time.time(), 1)})
        tail = zc.flush()
        if tail and not over[0]:
            chunks.append(tail)
            zbytes[0] += len(tail)

    if True:
        rt = threading.Thread(target=reader, daemon=True)
        ws = threading.Thread(target=_writer, args=(F["cnf_s"], cnf_bytes), daemon=True)
        rt.start()
        ws.start()
        t0 = time.time()
        res["_t_solver_start"] = t0
        sp, sp_out, sp_t = _start(solver_cmd(F["cnf_s"], F["prf"], limit))
        sp_holder["p"] = sp
        s_stop = stop_cooperatively(sp, limit + GRACE, events, solver_name)
        rc = sp.returncode if s_stop == "self" else None
        res["solve_seconds"] = round(time.time() - t0, 2)
        res["solver_rc"] = rc
        res["solver_stop"] = s_stop
        res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
        if over[0]:
            res["status"] = "UNKNOWN"
            res["proof_cap_hit"] = over[0]
        if s_stop != "running":
            sp_t.join(timeout=10)
        res["solver_out"] = b"".join(sp_out).decode(errors="replace") if rc == 10 else ""
        if s_stop == "running":
            res.update({"events": events, "checked": False, "drat_trim_verified": False, "checker_interrupted": True})
            return res
        rt.join(timeout=GRACE)
        ws.join(timeout=2)
        res["drat_sha256"] = hp.hexdigest()
        res["drat_bytes"] = nraw[0]
        res["zbuf_bytes"] = zbytes[0]
        if res["status"] != "UNSAT" or rt.is_alive():
            res.update({"events": events, "checked": False, "drat_trim_verified": False, "checker_interrupted": False,
                        "check_seconds": 0.0})
            return res
        with BigLock(nraw[0] > BIG) as bl:
            t1 = time.time()
            dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-t", str(cb)], stdin=True)
            wd = threading.Thread(target=_writer, args=(F["cnf_d"], cnf_bytes), daemon=True)
            wd.start()
            peak = [0]
            done = threading.Event()

            def feed():
                hc, n = hashlib.sha256(), 0
                d = zstd.ZstdDecompressor()
                try:
                    for z in chunks:
                        b = d.decompress(z)
                        hc.update(b)
                        n += len(b)
                        dt.stdin.write(b)
                except (OSError, ValueError):
                    pass
                finally:
                    try:
                        dt.stdin.close()
                    except (OSError, ValueError):
                        pass
                res["replay_sha256_matches"] = hc.hexdigest() == res["drat_sha256"] and n == nraw[0]

            def mon():
                while not done.wait(5):
                    peak[0] = max(peak[0], _rss_kb(dt.pid))

            ft = threading.Thread(target=feed, daemon=True)
            mt = threading.Thread(target=mon, daemon=True)
            ft.start()
            mt.start()
            dt_stop = stop_cooperatively(dt, cb + GRACE, events, "drat-trim")
            done.set()
            if dt_stop != "running":
                dt_t.join(timeout=10)
            ft.join(timeout=10)
            wd.join(timeout=2)
            res["bigmem_lock"] = bl.active
        res["check_seconds"] = round(time.time() - t1, 2)
        res["drat_trim_peak_rss_kb"] = peak[0]
        dto = b"".join(dt_out).decode(errors="replace")
        s_lines = [l for l in (x.strip("\r") for x in dto.split("\n")) if l.startswith("s ")]
        res["drat_trim"] = {"stop": dt_stop, "rc": dt.returncode if dt_stop != "running" else None,
                            "s_lines": s_lines, "says_verified": s_lines == ["s VERIFIED"],
                            "wall_seconds": res["check_seconds"]}
        res["checker_interrupted"] = dt_stop != "self"
        res["drat_trim_verified"] = (dt_stop == "self" and dt.returncode == 0 and res["drat_trim"]["says_verified"]
                                     and res.get("replay_sha256_matches") is True)
        res["events"] = events
        res["checked"] = bool(rc == 20 and not over[0] and res["drat_trim_verified"])
        chunks.clear()
        return res


def _kissat_cmd(cnf, prf, limit):
    return [KISSAT, "-q", "-f", "--seed=1", "--time=%d" % int(limit), cnf, prf]


def _cadical_cmd(cnf, prf, limit):
    return [CADICAL, "-q", "-t", str(int(limit)), cnf, prf]


def kissat_staged(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_staged(cnf_bytes, wdir, limit, check_budget, _kissat_cmd, "kissat")


def cadical_staged(cnf_bytes, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_staged(cnf_bytes, wdir, limit, check_budget, _cadical_cmd, "cadical")


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
