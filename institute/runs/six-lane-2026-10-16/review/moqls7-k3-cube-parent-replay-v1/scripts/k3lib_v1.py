#!/usr/bin/env python3
"""Parent K3 cube replay desk library (review/moqls7-k3-cube-parent-replay-v1). Imports no lane code.

Adapted from the parent's K2 desk template review/moqls7-k2-parent-v1/scripts/k2lib.py (read, not imported):
  * The CNF bytes stay in this process's memory; cadical and drat-trim each read them through their own anonymous
    pipe, passed as /dev/fd/N (drat-trim opens argv[1] as its formula).
  * The binary DRAT proof goes cadical -> named FIFO -> drat-trim stdin with -i. The FIFO read end is opened
    non-blocking (then made blocking) before any child starts, and this process holds a write end until the solver
    has been reaped, so drat-trim never sees a premature EOF and no open() can block forever.
  * Native limits bound the children (cadical -t, drat-trim -t). Safety stops are cooperative: SIGTERM, then a
    bounded wait; no SIGKILL, no subprocess timeouts. Children are reaped with os.wait4 (ru_maxrss in bytes on
    Darwin); aggregate RSS (this process plus its live children) is sampled through libproc every 0.25 s.
Differences from the template: a fresh statvfs gate (>= 12.2e9 + projected retained growth) immediately before each
native Popen; logs created O_EXCL|O_APPEND; status lines read with only CR stripped; no lane-capacity wait (this
desk's cap is its own two natives), only an observational lane snapshot; a driver SIGTERM is a safety stop.
"""
import ctypes
import datetime
import fcntl
import hashlib
import json
import os
import signal
import struct
import subprocess
import threading
import time

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
CODE = os.path.join(LANE, "code")
CERT = os.path.join(LANE, "evidence", "k3cubes", "cert_r2")
AMENDMENT2 = os.path.join(LANE, "review", "AMENDMENT-2.r1.md")
CADICAL = "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical"
DRAT = os.path.join(REVIEW, "moqls7-parent-proofcheck-v1", "drat-trim")
PY = "/Library/Developer/CommandLineTools/usr/bin/python3"
SCRIPTS = os.path.join(DESK, "scripts")
TMP = os.path.join(DESK, "tmp")
FLOOR = 12000000000                   # in-flight safety floor: cooperative stop below it
LAUNCH_BASE = 12200000000             # launch gate base (parent rule)
PROJECTED_GROWTH = 262144             # projected retained growth of the whole remaining desk run (upper bound)
GATE = LAUNCH_BASE + PROJECTED_GROWTH
RSS_STOP = 3584 * 1024 * 1024         # aggregate RSS cooperative stop, 3.5 GiB
GRACE = 120                           # bounded wait after SIGTERM, seconds
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
       "PYTHONDONTWRITEBYTECODE": "1", "HOME": TMP}

EXPECTED_CNF = {  # task brief
    "C321": "d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388",
    "C411": "2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2",
}
BASE_CNF_SHA256 = "d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388"   # task brief
PINS = {  # task brief
    os.path.join(CODE, "gram_enc.py"): "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833",
    os.path.join(CODE, "k3_cubes.py"): "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550",
    DRAT: "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37",
}
STOP = {"requested": None}            # set by a driver SIGTERM handler


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def free_bytes():
    st = os.statvfs(DESK)
    return st.f_bavail * st.f_frsize


def gate(what):
    fb = free_bytes()
    return {"what": what, "at": now(), "free_bytes": fb, "threshold": GATE, "pass": fb >= GATE}


def write_json_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")
    return sha_file(path)


def open_append_x(path):
    return os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_APPEND, 0o644)


def script_hashes():
    return {n: sha_file(os.path.join(SCRIPTS, n)) for n in sorted(os.listdir(SCRIPTS)) if n.endswith(".py")}


def pin_status():
    got = {p: sha_file(p) for p in PINS}
    return got, {p: h for p, h in got.items() if h != PINS[p]}


def binary_record(path):
    real = os.path.realpath(path)
    return {"path": path, "realpath": real, "sha256": sha_file(real), "bytes": os.path.getsize(real)}


def producer_evidence(cube):
    """Producer receipt and metadata (read-only), hashed, parsed and cross-checked against the brief's values."""
    rp = os.path.join(CERT, "A_%s.json" % cube)
    mp = os.path.join(CERT, "A_%s.meta.json" % cube)
    cp = os.path.join(CERT, "A_%s.cnf" % cube)
    with open(rp, "rb") as f:
        rb = f.read()
    with open(mp, "rb") as f:
        mb = f.read()
    r, m = json.loads(rb), json.loads(mb)
    out = {"receipt": {"path": rp, "sha256": sha_bytes(rb)}, "meta": {"path": mp, "sha256": sha_bytes(mb)},
           "lane_cnf_copy": {"path": cp, "sha256": sha_file(cp), "bytes": os.path.getsize(cp),
                             "use": "hashed read-only for the record; never given to the solver or checker"},
           "receipt_fields": {k: r.get(k) for k in ("started_at", "finished_at", "seconds", "solver_rc",
                                                     "checker_rc", "checker_status_lines", "verified_unsat",
                                                     "peak_sampled_aggregate_rss_bytes", "safety_stop_reason",
                                                     "cnf_sha256", "solver_binary_sha256",
                                                     "checker_binary_sha256", "solver_log_sha256",
                                                     "checker_log_sha256", "metadata_sha256", "scope")},
           "meta_fields": m}
    checks = {"receipt_cnf_equals_brief": r.get("cnf_sha256") == EXPECTED_CNF[cube],
              "meta_cnf_equals_brief": m.get("cnf_sha256") == EXPECTED_CNF[cube],
              "meta_sha_equals_receipt_metadata_sha256": out["meta"]["sha256"] == r.get("metadata_sha256"),
              "meta_base_cnf_equals_brief": m.get("base_cnf_sha256") == BASE_CNF_SHA256,
              "meta_wrapper_equals_pin": m.get("wrapper_sha256") == PINS[os.path.join(CODE, "k3_cubes.py")],
              "meta_base_encoder_equals_pin": m.get("base_encoder_sha256") == PINS[os.path.join(CODE, "gram_enc.py")],
              "meta_encoder_and_cube": m.get("encoder") == "A" and m.get("cube") == cube,
              "receipt_wrapper_pin_equals_pin": (r.get("pins") or {}).get("k3_cubes.py")
                                                 == PINS[os.path.join(CODE, "k3_cubes.py")]}
    out["checks"] = checks
    out["consistent"] = all(checks.values())
    return out


def regenerate(cube):
    """Run compose_v1.py CUBE in a subprocess (cwd and TMPDIR = desk tmp); the CNF arrives on a pipe and stays in
    memory."""
    t0 = time.monotonic()
    argv = [PY, "-I", "-B", os.path.join(SCRIPTS, "compose_v1.py"), cube]
    started = now()
    p = subprocess.run(argv, stdin=subprocess.DEVNULL, capture_output=True, cwd=TMP, env=ENV)
    info = {"argv": argv, "cwd": TMP, "started_at": started, "finished_at": now(), "rc": p.returncode,
            "seconds": round(time.monotonic() - t0, 3), "stdout_bytes": len(p.stdout),
            "stderr_tail": p.stderr.decode(errors="replace")[-4000:], "compose_info": None}
    if p.returncode == 0:
        try:
            info["compose_info"] = json.loads(p.stderr.decode().strip().splitlines()[-1])
        except Exception as e:  # recorded; the hash comparison below does not depend on it
            info["compose_info_error"] = repr(e)
    return (p.stdout if p.returncode == 0 else None), info


def check_regen(cube, cnf, info, meta):
    got = sha_bytes(cnf) if cnf is not None else None
    ci = info.get("compose_info") or {}
    head = cnf[:cnf.index(b"\n")].decode("ascii", "replace") if cnf else None
    return {"cube": cube, "cnf_sha256": got, "expected_cnf_sha256": EXPECTED_CNF[cube],
            "cnf_hash_match": (got == EXPECTED_CNF[cube]) if got is not None else None,
            "cnf_bytes": len(cnf) if cnf is not None else None, "cnf_header": head,
            "compose_reported_sha_equals_stdout": ci.get("out_sha256") == got if got else None,
            "base_cnf_sha256": ci.get("base_cnf_sha256"),
            "base_cnf_equals_brief": ci.get("base_cnf_sha256") == BASE_CNF_SHA256,
            "meta_agreement": {k: ci.get(k) == meta.get(k) for k in (
                "base_cnf_sha256", "support_sets", "cube_unit_clauses", "same_ray_identities", "extra_clauses")},
            "regen_run": info}


# --- RSS through libproc (macOS sys/proc_info.h: PROC_PIDTASKINFO = 4, struct proc_taskinfo is 96 bytes,
# pti_resident_size is the uint64 at offset 8). Same as the template.
_LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
_LIBPROC.proc_pidinfo.restype = ctypes.c_int


def rss(pid):
    buf = ctypes.create_string_buffer(96)
    n = _LIBPROC.proc_pidinfo(pid, 4, 0, buf, 96)
    return struct.unpack_from("=Q", buf.raw, 8)[0] if n == 96 else 0


# --- observational lane snapshot (no waiting): native solver/checker processes whose cwd or argv lies in the
# moqls7-maximum lane or a review/moqls7-* desk, excluding this process's children. Template filter.
LANE_MARKERS = ("/moqls7-maximum", "/review/moqls7-")
NATIVE = {"cadical", "kissat", "drat-trim", "lrat-check", "lrat-trim", "cake_lpr", "dpr-trim", "glucose",
          "minisat", "lingeling", "plingeling", "treengeling", "cryptominisat5", "kissat_mab", "dpr2pr"}


def lane_snapshot():
    try:
        ps = subprocess.run(["/bin/ps", "-axww", "-o", "pid=,ppid=,pcpu=,rss=,state=,comm="],
                            capture_output=True, text=True, env=ENV, cwd=TMP).stdout
        cand = []
        for line in ps.splitlines():
            parts = line.split(None, 5)
            if len(parts) < 6:
                continue
            pid, ppid, pcpu, rss_kb, state, comm = parts
            if os.path.basename(comm.strip()) in NATIVE and int(ppid) != os.getpid():
                cand.append({"pid": int(pid), "ppid": int(ppid), "pcpu": float(pcpu), "rss_kb": int(rss_kb),
                             "state": state, "comm": comm.strip()})
        if cand:
            pids = ",".join(str(c["pid"]) for c in cand)
            lo = subprocess.run(["/usr/sbin/lsof", "-a", "-d", "cwd", "-p", pids, "-Fpn"],
                                capture_output=True, text=True, env=ENV, cwd=TMP).stdout
            cwd, cur = {}, None
            for line in lo.splitlines():
                if line.startswith("p"):
                    cur = int(line[1:])
                elif line.startswith("n") and cur is not None:
                    cwd[cur] = line[1:]
            args = {}
            a = subprocess.run(["/bin/ps", "-ww", "-o", "pid=,args=", "-p", pids], capture_output=True,
                               text=True, env=ENV, cwd=TMP).stdout
            for line in a.splitlines():
                parts = line.strip().split(None, 1)
                if len(parts) == 2:
                    args[int(parts[0])] = parts[1]
            for c in cand:
                c["cwd"] = cwd.get(c["pid"], "")
                c["args"] = args.get(c["pid"], "")[:300]
        lane = [c for c in cand if any(m in c.get("cwd", "") or m in c.get("args", "") for m in LANE_MARKERS)]
        return {"at": now(), "native_busy_all": len(cand), "lane_native_busy": len(lane), "lane": lane,
                "note": "observational only; this desk's cap is its own two natives"}
    except Exception as e:
        return {"at": now(), "error": repr(e)}


# --- status lines: only CR is stripped (drat-trim prints '\rs VERIFIED', '\ns NOT VERIFIED', 's TIMEOUT')
def status_lines(log_bytes):
    out = []
    for raw in log_bytes.split(b"\n"):
        line = raw.strip(b"\r")
        if line.startswith(b"s "):
            out.append(line.decode("ascii", "replace"))
    return out


def checker_flags(log_bytes):
    lines = status_lines(log_bytes)
    return {"status_lines": lines, "exact_verified": "s VERIFIED" in lines,
            "exact_not_verified": "s NOT VERIFIED" in lines,
            "not_verified_anywhere": b"NOT VERIFIED" in log_bytes, "timeout_anywhere": b"s TIMEOUT" in log_bytes}


def verdict(hash_match, rec):
    """PASS iff the CNF hash matches, solver rc 20, checker rc 0, an exact 's VERIFIED' line (only CR stripped),
    no 'NOT VERIFIED' / 's TIMEOUT' anywhere in the checker log, and no safety stop. FAIL on hash mismatch,
    solver rc 10, or a definitive exact 's NOT VERIFIED' (checker exited normally, no TIMEOUT, no safety stop)
    with solver rc 20. Otherwise UNKNOWN (including a regeneration that produced no bytes)."""
    if hash_match is False:
        return "FAIL"
    if hash_match is not True or rec is None or rec.get("deferred") or "children" not in rec:
        return "UNKNOWN"
    s = rec["children"].get("solver", {}).get("rc")
    c = rec["children"].get("checker", {}).get("rc")
    f = rec["checker_flags"]
    if s == 10:
        return "FAIL"
    if rec["safety_stop_reason"]:
        return "UNKNOWN"
    if s == 20 and c == 0 and f["exact_verified"] and not f["not_verified_anywhere"] and not f["timeout_anywhere"]:
        return "PASS"
    if (s == 20 and f["exact_not_verified"] and not f["exact_verified"] and not f["timeout_anywhere"]
            and c is not None and c >= 0):
        return "FAIL"
    return "UNKNOWN"


# --- the cadical -> FIFO -> drat-trim pipeline
def _writer(fd, data, res):
    mv, off = memoryview(data), 0
    try:
        while off < len(mv):
            off += os.write(fd, mv[off:off + (1 << 20)])
        res["ok"] = True
    except OSError as e:
        res["error"] = repr(e)
    finally:
        os.close(fd)
        res["written"] = off


def _start_writer(fd, data):
    res = {}
    t = threading.Thread(target=_writer, args=(fd, data, res), daemon=True)
    t.start()
    return t, res


def pipeline(label, cnf, solver, solver_seconds, checker_seconds, checker_cnf=None):
    """cadical (argv prefix `solver`) reads `cnf` from a pipe and writes binary DRAT to a FIFO; drat-trim reads
    `checker_cnf` (default `cnf`) from a second pipe and the proof from the FIFO on stdin (-i)."""
    if checker_cnf is None:
        checker_cnf = cnf
    fifo = os.path.join(DESK, "fifo", label + ".drat.fifo")
    slog = os.path.join(DESK, "logs", label + ".solver.log")
    clog = os.path.join(DESK, "logs", label + ".checker.log")
    for path in (fifo, slog, clog):
        if os.path.lexists(path):
            raise FileExistsError(path)
    rec = {"label": label, "cnf_bytes": len(cnf), "cnf_sha256": sha_bytes(cnf),
           "checker_cnf_sha256": sha_bytes(checker_cnf),
           "checker_argv": [DRAT, "/dev/fd/<cnf-pipe>", "-i", "-t", str(checker_seconds)],
           "checker_stdin": os.path.relpath(fifo, DESK),
           "solver_argv": list(solver) + ["/dev/fd/<cnf-pipe>", os.path.relpath(fifo, DESK)],
           "fifo": os.path.relpath(fifo, DESK), "solver_log": os.path.relpath(slog, DESK),
           "checker_log": os.path.relpath(clog, DESK), "solver_seconds": solver_seconds,
           "checker_seconds": checker_seconds, "cwd": TMP, "env": ENV, "gates": [],
           "free_bytes_start": free_bytes(), "started_at": now()}
    os.mkfifo(fifo)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    fcntl.fcntl(rfd, fcntl.F_SETFL, fcntl.fcntl(rfd, fcntl.F_GETFL) & ~os.O_NONBLOCK)
    kfd = os.open(fifo, os.O_WRONLY)          # parent-held writer (keepalive) until the solver is reaped
    cl_fd = open_append_x(clog)
    sl_fd = open_append_x(slog)
    ccr, ccw = os.pipe()
    scr, scw = os.pipe()
    writers, procs, done = {}, {}, {}
    peak, samples, min_free, reason, term_at = 0, 0, None, None, None
    t0 = time.monotonic()
    try:
        g = gate("immediately before drat-trim Popen")
        rec["gates"].append(g)
        if not g["pass"] or STOP["requested"]:
            rec["deferred"] = ("launch gate failed before drat-trim" if not g["pass"] else STOP["requested"])
            return rec
        check = subprocess.Popen([DRAT, "/dev/fd/%d" % ccr, "-i", "-t", str(checker_seconds)], stdin=rfd,
                                 stdout=cl_fd, stderr=subprocess.STDOUT, pass_fds=(ccr,), cwd=TMP, env=ENV)
        procs["checker"] = check
        rec["checker_pid"] = check.pid
        os.close(rfd)
        rfd = None
        os.close(ccr)
        ccr = None
        writers["checker_cnf"] = _start_writer(ccw, checker_cnf)
        ccw = None
        g = gate("immediately before cadical Popen")
        rec["gates"].append(g)
        if not g["pass"] or STOP["requested"]:
            reason = "launch gate failed before cadical" if not g["pass"] else STOP["requested"]
            rec["deferred"] = reason
            rec["safety_stop_at"] = now()
            term_at = time.monotonic()
            os.kill(check.pid, signal.SIGTERM)
        else:
            solve = subprocess.Popen(list(solver) + ["/dev/fd/%d" % scr, fifo], stdin=subprocess.DEVNULL,
                                     stdout=sl_fd, stderr=subprocess.STDOUT, pass_fds=(scr,), cwd=TMP, env=ENV)
            procs["solver"] = solve
            rec["solver_pid"] = solve.pid
            os.close(scr)
            scr = None
            writers["solver_cnf"] = _start_writer(scw, cnf)
            scw = None
        while True:
            for name, p in procs.items():
                if name in done:
                    continue
                pid, st, ru = os.wait4(p.pid, os.WNOHANG)
                if pid:
                    rc = os.waitstatus_to_exitcode(st)
                    p.returncode = rc
                    done[name] = {"rc": rc, "maxrss_bytes": ru.ru_maxrss, "ended_at": now(),
                                  "wall_seconds": round(time.monotonic() - t0, 3),
                                  "user_seconds": round(ru.ru_utime, 3), "sys_seconds": round(ru.ru_stime, 3)}
                    if name == "solver" and kfd is not None:
                        os.close(kfd)
                        kfd = None
            if len(done) == len(procs):
                break
            cur = rss(os.getpid()) + sum(rss(p.pid) for n, p in procs.items() if n not in done)
            peak = max(peak, cur)
            fb = free_bytes()
            min_free = fb if min_free is None else min(min_free, fb)
            samples += 1
            if reason is None:
                if cur > RSS_STOP:
                    reason = "aggregate RSS safety stop: %d > %d" % (cur, RSS_STOP)
                elif fb < FLOOR:
                    reason = "free-space floor: %d < %d" % (fb, FLOOR)
                elif time.monotonic() - t0 > solver_seconds + checker_seconds + GRACE:
                    reason = "combined wall-clock backstop"
                elif STOP["requested"]:
                    reason = STOP["requested"]
                if reason:
                    rec["safety_stop_at"] = now()
                    term_at = time.monotonic()
                    for n, p in procs.items():
                        if n not in done:
                            os.kill(p.pid, signal.SIGTERM)
            elif time.monotonic() - term_at > GRACE:
                rec["grace_exceeded"] = ("children %s still alive %d s after SIGTERM; no SIGKILL sent; they remain "
                                         "bounded by their native limits" % (sorted(set(procs) - set(done)), GRACE))
                break
            time.sleep(0.25)
    finally:
        for fd in (rfd, ccr, ccw, scr, scw, kfd):
            if fd is not None:
                os.close(fd)
        os.close(cl_fd)
        os.close(sl_fd)
    for name, (t, res) in writers.items():
        t.join(30)
        res["thread_alive_after_join"] = t.is_alive()
    rec["finished_at"] = now()
    rec["pipeline_seconds"] = round(time.monotonic() - t0, 3)
    rec["children"] = done
    rec["writers"] = {k: v[1] for k, v in writers.items()}
    rec["peak_sampled_aggregate_rss_bytes"] = peak
    rec["rss_samples"] = samples
    rec["min_sampled_free_bytes"] = min_free
    rec["free_bytes_end"] = free_bytes()
    rec["safety_stop_reason"] = reason
    with open(clog, "rb") as f:
        cbytes = f.read()
    with open(slog, "rb") as f:
        sbytes = f.read()
    rec["checker_log_sha256"] = sha_bytes(cbytes)
    rec["checker_log_bytes"] = len(cbytes)
    rec["checker_flags"] = checker_flags(cbytes)
    rec["solver_log_sha256"] = sha_bytes(sbytes)
    rec["solver_log_bytes"] = len(sbytes)
    rec["solver_status_lines"] = status_lines(sbytes)
    return rec
