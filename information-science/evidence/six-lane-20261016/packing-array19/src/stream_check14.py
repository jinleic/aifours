#!/usr/bin/env python3
"""Revision 14: parent fresh-admission margin update (2026-10-17 23:26). Same revision-13 lifecycle, caps and certification predicate; only the per-stage DISK_FLOOR becomes 12.2e9 bytes plus 64 MiB projected retained-metadata headroom. Proofs/CNFs remain in RAM/FIFO. Every existing post-token, construction, helper, solver and checker admission re-check uses this stronger threshold; records carry revision 14.
Revision 13 = revision 12 plus helper memory safeguards (REV11c proposal, 2026-10-17 ~16:5x; extend_p1q used
~4.7 GB on ms06_s00214): run_helper (1) takes an exclusive helper lock cycle2/tokens/helper, so at most one helper
runs in the lane; (2) refuses to start (AdmissionDenied "lane RSS headroom") unless the current lane RSS (one ps sum
over processes whose command line contains the lane path or an exact lane runner path) plus HELPER_RSS_CAP_KB is
at most LANE_RSS_LIMIT_KB (8 GiB); (3) samples the helper's RSS every second and, above HELPER_RSS_CAP_KB (5 GiB),
sends SIGTERM to that helper -- its own registered, not yet reaped Popen child, so the pid cannot have been reused --
then waits for it (quarantine if it survives). The result is recorded in LAST_HELPER (peak RSS, cap hit). Records
carry stream_check_revision 13. Revision-12 text follows.
Revision 12 = revision 11 plus an admission re-check INSIDE the bigmem lock, immediately before the checker
spawn (parent re-review ~16:1x: a stage could wait for the bigmem lock and then start drat-trim after a stop
file / disk-floor change). If not admitted there, the stage returns UNKNOWN (admission_denied) without
starting drat-trim. Records carry stream_check_revision 12. Revision-11 text follows.
Revision 11 of the online proof-checking helpers: the staged, token-gated pipeline of revision 10 with the
parent audit fixes (PA19StagedAudit, 2026-10-17 ~15:3x-15:4x):

* No silent token release. A solver, checker or helper that survives SIGTERM + TERM_WAIT is QUARANTINED: a
  record cycle2/QUARANTINE-<runner pid>-<child pid>-<time>.json is written and the pipeline keeps holding its
  CPU token (and the bigmem lock, if held) while polling the survivor every 5 s, without further signals,
  until it exits by itself. Only then does the stage return (UNKNOWN). Helpers run through run_helper()
  (Popen + unbounded wait) under the token.
* Runner SIGTERM handling (install_sigterm_handler): sets ABORT; if the runner has registered live children
  (solver, checker, helper) it forwards SIGTERM to each of them and lets the stage finish as UNKNOWN (token
  released only after they have exited, quarantine otherwise); if it has none and is not in the middle of
  starting one (e.g. CNF construction in Python) it raises SystemExit so the stage is abandoned before any
  child is started. While a child is being started (SPAWNING) the handler does not abandon the stage; the
  new child is terminated right after registration. SIGTERM is never blocked around child creation (a blocked
  signal mask is inherited across fork/exec and made children unstoppable in a first smoke run).
* Proof replay binding: the hash/count of the proof fed to drat-trim are taken only over bytes whose write
  to drat-trim's stdin completed; the decompressor must reach the end of the single zstd frame; stdin must
  close without error; the reader of the solver's proof must reach EOF without error. Any failure ->
  replay_ok False -> not checked (UNKNOWN), even if drat-trim prints 's VERIFIED'.
* CPU accounting (parent decision 15:4x): one token covers the stage's solver or checker PLUS the runner's
  concurrent compression/decompression/feeding (or the runner's CNF construction, or one helper), i.e. at
  most 2 busy processes per token; the lane runs with COUNT <= 2 tokens (cycle2/tokens/COUNT).
* The token file records the holder (pid, time, stage) on acquisition, for the RSS watchdog.
* Admission re-checks (parent audit 15:5x): immediately AFTER every token acquisition and again before every
  CNF construction, helper start, solver start and checker start, admitted() checks the runner's ABORT flag,
  the runner's stop files (set_stop_files) and the 12e9-byte free-disk floor. A refused admission raises
  AdmissionDenied before the token acquisition returns / before construction or a helper, or ends the stage as
  UNKNOWN (admission_denied) before a solver/checker start; the token is released only when no owned child
  is alive (Token.__exit__ waits, quarantine otherwise).
Acceptance (checked=True) iff: solver exited on its own with rc 20; no proof cap hit; proof reader reached EOF
without error; drat-trim exited on its own (no quarantine) with rc 0; its 's ' lines, each stripped of '\\r',
are exactly ['s VERIFIED']; replay_ok (complete delivery, SHA-256 and length equal to the streamed proof).
Caps unchanged from revision 10 (raw proof 1200 MiB, compressed buffer 500 MiB including the final frame
tail, bigmem > 300 MiB, check budget <= 1200 s, solver limit as given). The proof caps are checked after
each read chunk of at most 1 MiB, so the buffers can exceed a cap by at most one chunk (<= 1 MiB raw and
its compressed output) plus zstd's internal state before the solver is stopped; they are admission/size
limits, not instantaneous RSS limits. The lane RAM guard is the aggregate watchdog (sampled every 2 s),
also not instantaneous; with COUNT <= 2 the margins (2 x (500 MiB buffer + solver + checker), checks of
proofs > 300 MiB serialized) are chosen to stay well below 8 GiB with room for sampling delay.
"""
import fcntl
import hashlib
import json
import os
import signal
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
DISK_FLOOR = 12200000000 + 64 * 1024 * 1024
SOLVER_INFO = {"kissat": {"version": "kissat 4.0.4 (/opt/homebrew/bin/kissat)", "seed": "--seed=1"},
               "cadical": {"version": "cadical 3.0.1 (/opt/homebrew/bin/cadical)", "seed": "default (no --seed option given)"}}

ABORT = [False]
SPAWNING = [False]
ACTIVE = set()
_alock = threading.RLock()
ADMISSION = {"stop_files": []}


class AdmissionDenied(Exception):
    pass


def set_stop_files(paths):
    ADMISSION["stop_files"] = list(paths)


def admitted_reason():
    """None if a new admission is allowed, else the reason"""
    if ABORT[0]:
        return "abort (SIGTERM)"
    for p in ADMISSION["stop_files"]:
        if os.path.exists(p):
            return "stop file " + os.path.basename(p)
    try:
        if disk_free_bytes() < DISK_FLOOR:
            return "disk floor"
    except OSError:
        return "disk free unknown"
    return None


def disk_free_bytes(path=LANE):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def disk_free_ok(path=LANE):
    return disk_free_bytes(path) >= DISK_FLOOR


def _on_term(signum, frame):
    ABORT[0] = True
    with _alock:
        live = [p for p in ACTIVE if p.poll() is None]
    if not live and not SPAWNING[0]:
        raise SystemExit(143)
    for p in live:
        try:
            p.terminate()
        except OSError:
            pass


def install_sigterm_handler():
    signal.signal(signal.SIGTERM, _on_term)


def spawn(cmd, stdin=False):
    """Popen + registration in ACTIVE. SIGTERM is NOT blocked (a blocked mask would be inherited by the child,
    which then could not be stopped -- found by smoke test L). Instead SPAWNING tells the handler not to abandon
    the stage while a child may exist unregistered; a SIGTERM that arrived meanwhile is honoured right after
    registration by terminating the new child."""
    SPAWNING[0] = True
    try:
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE if stdin else subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        with _alock:
            ACTIVE.add(p)
    finally:
        SPAWNING[0] = False
    if ABORT[0]:
        try:
            p.terminate()
        except OSError:
            pass
    return p


def write_json(path, obj):
    """record write with SIGTERM blocked (a pending SIGTERM is handled after the record is complete)"""
    old = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGTERM})
    try:
        with open(path, "w") as f:
            json.dump(obj, f, indent=1)
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)


def unregister(p):
    with _alock:
        ACTIVE.discard(p)


def _collect(stream, sink):
    for line in iter(stream.readline, b""):
        sink.append(line)
    stream.close()


def _start(cmd, stdin=False):
    p = spawn(cmd, stdin)
    sink = []
    t = threading.Thread(target=_collect, args=(p.stdout, sink), daemon=True)
    t.start()
    return p, sink, t


def quarantine(p, name, events):
    t0 = time.time()
    q = {"time": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "runner_pid": os.getpid(), "child_pid": p.pid, "child": name,
         "note": "child survived SIGTERM + TERM_WAIT; token (and bigmem lock if held) retained until it exits; no further signals"}
    qp = os.path.join(LANE, "cycle2", "QUARANTINE-%d-%d-%s.json" % (os.getpid(), p.pid, time.strftime("%Y%m%dT%H%M%S")))
    with open(qp, "w") as f:
        json.dump(q, f, indent=1)
    while p.poll() is None:
        time.sleep(5)
    events.append({"process": name, "pid": p.pid, "action": "quarantine-ended", "quarantine_seconds": round(time.time() - t0, 1),
                   "record": os.path.relpath(qp, LANE)})
    return "quarantined"


def stop_cooperatively(p, bound, events, name):
    """returns 'self' (exited on its own within bound), 'term' (exited after SIGTERM) or 'quarantined'
    (survived SIGTERM + TERM_WAIT and has exited since; it was waited for while the token was held)"""
    try:
        try:
            p.wait(timeout=max(1.0, bound))
            return "self" if not ABORT[0] or p.returncode >= 0 else "term"
        except subprocess.TimeoutExpired:
            pass
        p.terminate()
        events.append({"process": name, "pid": p.pid, "action": "SIGTERM", "time": round(time.time(), 1)})
        try:
            p.wait(timeout=TERM_WAIT)
            return "term"
        except subprocess.TimeoutExpired:
            events.append({"process": name, "pid": p.pid, "action": "survived-SIGTERM", "time": round(time.time(), 1)})
            return quarantine(p, name, events)
    finally:
        if p.poll() is not None:
            unregister(p)


HELPER_RSS_CAP_KB = 5 * 1024 * 1024
LANE_RSS_LIMIT_KB = 8 * 1024 * 1024
HELPER_LOCK = os.path.join(TOK, "helper")
LAST_HELPER = {}
RUNNER_NAMES = ("run_hard13.py", "run_m2_13.py", "smoke_rev13.py", "smoke13_runner.py", "run_hard12.py", "run_m2_12.py")


def lane_rss_kb():
    out = subprocess.run(["ps", "-Ao", "rss=,command="], capture_output=True, text=True).stdout
    tot = 0
    for line in out.splitlines():
        parts = line.split(None, 1)
        if len(parts) < 2:
            continue
        rss, cmd = parts
        argv = cmd.split()
        if LANE in cmd or any(os.path.join(LANE, "src", r) in argv for r in RUNNER_NAMES):
            try:
                tot += int(rss)
            except ValueError:
                pass
    return tot


def run_helper(cmd):
    """helper subprocess under the caller's token: exclusive helper lock, lane-RSS headroom check, per-helper RSS cap
    enforced on the helper itself (own child), unbounded wait (a stubborn helper keeps the token and the lock)"""
    r = admitted_reason()
    if r:
        raise AdmissionDenied(r)
    os.makedirs(TOK, exist_ok=True)
    lfd = os.open(HELPER_LOCK, os.O_CREAT | os.O_RDWR)
    fcntl.flock(lfd, fcntl.LOCK_EX)
    try:
        r = admitted_reason()
        if r:
            raise AdmissionDenied(r)
        now = lane_rss_kb()
        if now + HELPER_RSS_CAP_KB > LANE_RSS_LIMIT_KB:
            raise AdmissionDenied("lane RSS headroom: %d KB in use + helper cap %d KB > %d KB" % (now, HELPER_RSS_CAP_KB, LANE_RSS_LIMIT_KB))
        info = {"cmd": " ".join(cmd)[:300], "lane_rss_kb_at_start": now, "cap_kb": HELPER_RSS_CAP_KB, "peak_rss_kb": 0,
                "cap_hit": False, "events": []}
        p = spawn(cmd)
        done = threading.Event()

        def mon():
            while not done.wait(1):
                rss = _rss_kb(p.pid) if p.poll() is None else 0
                info["peak_rss_kb"] = max(info["peak_rss_kb"], rss)
                if rss > HELPER_RSS_CAP_KB and not info["cap_hit"] and p.poll() is None:
                    info["cap_hit"] = True
                    try:
                        p.terminate()
                        info["events"].append({"action": "SIGTERM (helper RSS cap)", "rss_kb": rss, "time": round(time.time(), 1)})
                    except OSError as e:
                        info["events"].append({"terminate_error": str(e)})

        mt = threading.Thread(target=mon, daemon=True)
        mt.start()
        try:
            out, _ = p.communicate()
        finally:
            done.set()
            if p.poll() is None:
                quarantine(p, "helper", info["events"])
            unregister(p)
        info["rc"] = p.returncode
        LAST_HELPER.clear()
        LAST_HELPER.update(info)
        return p.returncode, (out or b"").decode(errors="replace")
    finally:
        fcntl.flock(lfd, fcntl.LOCK_UN)
        os.close(lfd)


def token_count():
    try:
        return max(0, int(open(os.path.join(TOK, "COUNT")).read().split()[0]))
    except (OSError, ValueError, IndexError):
        return 0


class Token:
    """exclusive lane CPU token (flock); polls every 2 s; records the holder in the token file"""

    def __init__(self, stage="stage"):
        os.makedirs(TOK, exist_ok=True)
        self.fd, self.name, self.waited, self.stage = None, None, 0.0, stage

    def __enter__(self):
        t0 = time.time()
        while True:
            if ABORT[0]:
                raise SystemExit(143)
            for i in range(token_count()):
                p = os.path.join(TOK, "t%d" % i)
                fd = os.open(p, os.O_CREAT | os.O_RDWR)
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    os.close(fd)
                    continue
                os.ftruncate(fd, 0)
                os.pwrite(fd, ("%d %.3f %s\n" % (os.getpid(), time.time(), self.stage)).encode(), 0)
                r = admitted_reason()
                if r:  # re-check right after acquisition; nothing has been started yet
                    fcntl.flock(fd, fcntl.LOCK_UN)
                    os.close(fd)
                    raise AdmissionDenied(r)
                self.fd, self.name = fd, "t%d" % i
                self.waited = round(time.time() - t0, 1)
                return self
            time.sleep(2)

    def __exit__(self, *a):
        with _alock:
            live = [p for p in ACTIVE if p.poll() is None]
        for p in live:  # never release with a live child: wait for it (quarantine, no new signal)
            quarantine(p, "child-at-token-release", [])
            unregister(p)
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)


class BigLock:
    def __init__(self, active):
        self.active, self.fd = active, None

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


def _rss_kb(pid):
    try:
        out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
        return int(out) if out else 0
    except (OSError, ValueError):
        return 0


def _drat_staged(cnf_source, wdir, limit, check_budget, solver_cmd, solver_name):
    """cnf_source: CNF bytes, or a callable returning them (built while the token is held)"""
    with Token(stage=solver_name) as tok:
        r = admitted_reason()
        if r:
            raise AdmissionDenied(r)
        t_enc = time.time()
        cnf_bytes = cnf_source() if callable(cnf_source) else cnf_source
        res = _drat_staged_locked(cnf_bytes, wdir, limit, check_budget, solver_cmd, solver_name)
        res["token"], res["token_wait_seconds"] = tok.name, tok.waited
        res["encode_seconds"] = round(res.pop("_t_solver_start") - t_enc, 2)
        res["aborted_by_sigterm"] = ABORT[0]
        if ABORT[0]:
            res["checked"] = False
        return res


def _drat_staged_locked(cnf_bytes, wdir, limit, check_budget, solver_cmd, solver_name):
    cb = int(min(check_budget, MAX_CHECK_BUDGET))
    F = _fifos(wdir, ["cnf_s", "cnf_d", "prf"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "%s; binary DRAT staged (zstd-1 in memory) then drat-trim -i -t %d" % (
               " ".join(solver_cmd("CNF", "PROOF", limit)), cb),
           "solver_info": SOLVER_INFO[solver_name], "drat_trim_binary": "tools/drat-trim/drat-trim",
           "stream_check_revision": 14, "staged": True, "check_budget": cb,
           "fifo_dir": os.path.relpath(os.path.dirname(F["prf"]), LANE)}
    events = []
    hp, nraw = hashlib.sha256(), [0]
    zc = zstd.ZstdCompressor(level=1)
    chunks, zbytes, over, reader_ok = [], [0], [None], [False]
    sp_holder = {}

    def reader():
        try:
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
                            events.append({"process": solver_name, "pid": p.pid,
                                           "action": "SIGTERM (proof size cap %s)" % over[0], "time": round(time.time(), 1)})
            if not over[0]:
                tail = zc.flush()
                if zbytes[0] + len(tail) > MAX_ZBUF:  # the frame tail counts against the cap too
                    over[0] = "zbuf-tail"
                    events.append({"proof_cap": "zbuf-tail", "zbuf_before_tail": zbytes[0], "tail_bytes": len(tail)})
                else:
                    if tail:
                        chunks.append(tail)
                        zbytes[0] += len(tail)
                    reader_ok[0] = True
        except Exception as e:  # noqa: BLE001 -- any reader failure makes the case UNKNOWN
            events.append({"reader_error": repr(e)[:200]})

    r = admitted_reason()
    if r:  # before the solver start
        res.update({"_t_solver_start": time.time(), "status": "UNKNOWN", "admission_denied": r, "checked": False,
                    "drat_trim_verified": False, "events": events, "solver_out": ""})
        return res
    rt = threading.Thread(target=reader, daemon=True)
    ws = threading.Thread(target=_writer, args=(F["cnf_s"], cnf_bytes), daemon=True)
    rt.start()
    ws.start()
    t0 = time.time()
    res["_t_solver_start"] = t0
    sp, sp_out, sp_t = _start(solver_cmd(F["cnf_s"], F["prf"], limit))
    sp_holder["p"] = sp
    speak = [0]
    sdone = threading.Event()

    def smon():
        while not sdone.wait(5):
            speak[0] = max(speak[0], _rss_kb(sp.pid))

    threading.Thread(target=smon, daemon=True).start()
    s_stop = stop_cooperatively(sp, limit + GRACE, events, solver_name)
    sdone.set()
    rc = sp.returncode if s_stop == "self" else None
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["solver_stop"] = s_stop
    res["solver_peak_rss_kb"] = speak[0]
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if over[0]:
        res["status"] = "UNKNOWN"
        res["proof_cap_hit"] = over[0]
    sp_t.join(timeout=10)
    res["solver_out"] = b"".join(sp_out).decode(errors="replace") if rc == 10 else ""
    rt.join(timeout=GRACE)
    ws.join(timeout=2)
    res["drat_sha256"] = hp.hexdigest()
    res["drat_bytes"] = nraw[0]
    res["zbuf_bytes"] = zbytes[0]
    res["reader_ok"] = reader_ok[0] and not rt.is_alive()
    r = admitted_reason()
    if r:
        res["admission_denied"] = r
    if res["status"] != "UNSAT" or not res["reader_ok"] or r:
        res.update({"events": events, "checked": False, "drat_trim_verified": False, "checker_interrupted": False,
                    "check_seconds": 0.0, "replay_ok": False})
        return res
    with BigLock(nraw[0] > BIG) as bl:
        r2 = admitted_reason()  # re-check after a possible bigmem wait, immediately before the checker spawn
        if r2:
            res.update({"admission_denied": r2, "events": events, "checked": False, "drat_trim_verified": False,
                        "checker_interrupted": False, "check_seconds": 0.0, "replay_ok": False, "bigmem_lock": bl.active})
            chunks.clear()
            return res
        t1 = time.time()
        dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-t", str(cb)], stdin=True)
        wd = threading.Thread(target=_writer, args=(F["cnf_d"], cnf_bytes), daemon=True)
        wd.start()
        peak = [0]
        done = threading.Event()
        feed = {"ok": False, "sha": None, "n": 0, "error": None}

        def feeder():
            hc, n = hashlib.sha256(), 0
            d = zstd.ZstdDecompressor()
            try:
                for z in chunks:
                    b = d.decompress(z)
                    if b:
                        dt.stdin.write(b)  # raises on a broken pipe; bytes are counted only after it returns
                        hc.update(b)
                        n += len(b)
                if not d.eof:
                    raise ValueError("zstd frame incomplete")
                dt.stdin.close()
                feed["ok"] = True
            except Exception as e:  # noqa: BLE001 -- any feed failure makes the case UNKNOWN
                feed["error"] = repr(e)[:200]
                try:
                    dt.stdin.close()
                except Exception:  # noqa: BLE001
                    pass
            feed["sha"], feed["n"] = hc.hexdigest(), n

        def mon():
            while not done.wait(5):
                peak[0] = max(peak[0], _rss_kb(dt.pid))

        ft = threading.Thread(target=feeder, daemon=True)
        mt = threading.Thread(target=mon, daemon=True)
        ft.start()
        mt.start()
        dt_stop = stop_cooperatively(dt, cb + GRACE, events, "drat-trim")
        done.set()
        dt_t.join(timeout=10)
        ft.join(timeout=30)
        wd.join(timeout=2)
        res["bigmem_lock"] = bl.active
    res["check_seconds"] = round(time.time() - t1, 2)
    res["drat_trim_peak_rss_kb"] = peak[0]
    res["replay_ok"] = bool(feed["ok"] and not ft.is_alive() and feed["sha"] == res["drat_sha256"] and feed["n"] == nraw[0])
    res["replay"] = {"ok": feed["ok"], "bytes": feed["n"], "sha256": feed["sha"], "error": feed["error"]}
    res["replay_sha256_matches"] = res["replay_ok"]
    dto = b"".join(dt_out).decode(errors="replace")
    s_lines = [l for l in (x.strip("\r") for x in dto.split("\n")) if l.startswith("s ")]
    res["drat_trim"] = {"stop": dt_stop, "rc": dt.returncode, "s_lines": s_lines, "says_verified": s_lines == ["s VERIFIED"],
                        "wall_seconds": res["check_seconds"]}
    res["checker_interrupted"] = dt_stop != "self"
    res["drat_trim_verified"] = (dt_stop == "self" and dt.returncode == 0 and res["drat_trim"]["says_verified"]
                                 and res["replay_ok"])
    res["events"] = events
    res["checked"] = bool(rc == 20 and not over[0] and res["reader_ok"] and res["drat_trim_verified"] and not ABORT[0])
    chunks.clear()
    return res


def _kissat_cmd(cnf, prf, limit):
    return [KISSAT, "-q", "-f", "--seed=1", "--time=%d" % int(limit), cnf, prf]


def _cadical_cmd(cnf, prf, limit):
    return [CADICAL, "-q", "-t", str(int(limit)), cnf, prf]


def kissat_staged(cnf_source, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_staged(cnf_source, wdir, limit, check_budget, _kissat_cmd, "kissat")


def cadical_staged(cnf_source, wdir, limit, check_budget=MAX_CHECK_BUDGET):
    return _drat_staged(cnf_source, wdir, limit, check_budget, _cadical_cmd, "cadical")


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
