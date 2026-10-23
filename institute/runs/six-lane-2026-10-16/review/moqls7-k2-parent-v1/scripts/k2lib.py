#!/usr/bin/env python3
"""Parent K2 replay desk library (review/moqls7-k2-parent-v1). Written by the parent desk; imports no lane code.

Transport (zero disk for CNFs and proofs):
  * CNF bytes stay in this process's memory. The solver and drat-trim each read them through their own
    anonymous pipe, passed as /dev/fd/N.
  * The binary DRAT proof goes solver -> named FIFO -> drat-trim stdin with -i. The FIFO read end is opened
    non-blocking (then made blocking) before any child starts, and this parent holds a write end until the
    solver has been reaped, so drat-trim never sees a premature EOF and no open() can block forever.
  * Only small logs, receipts and zero-length FIFO nodes are written. Every path is exclusively created.
Process control: native limits (-t / --time) plus a cooperative SIGTERM safety stop with a bounded wait;
no SIGKILL, no subprocess timeouts. Children are reaped with os.wait4, giving the kernel's per-child
ru_maxrss (bytes on Darwin); aggregate RSS is also sampled through libproc every 0.25 s.
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
CERT = os.path.join(LANE, "evidence", "gram", "cert_r4")
CLASSFILE = os.path.join(LANE, "evidence", "ls7_main_classes.txt")
CADICAL = "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical"
KISSAT = "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"
DRAT = os.path.join(REVIEW, "moqls7-parent-proofcheck-v1", "drat-trim")
PY = "/usr/bin/python3"
TMP = os.path.join(DESK, "tmp")
FLOOR = 12000000000                    # hard floor: in-flight safety stop
FLOOR_LAUNCH = 12200000000             # parent rule 2026-10-17 23:17: launch only on a fresh check >= 12.2e9
RSS_STOP = 3584 * 1024 * 1024          # cooperative stop, below the 4 GiB desk ceiling
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
       "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", DESK)}

PINS = {  # path -> expected sha256 (task brief / worker print / parent build record)
    os.path.join(LANE, "review", "K2-THEOREM.r1.md"):
        "e846e1d9e345db0630b4aeeee9722d47357daa07daa089b9ae5325c5e58ef05b",
    os.path.join(LANE, "evidence", "gram", "k2A_cert_summary_r4.json"):
        "31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29",
    os.path.join(LANE, "evidence", "gram", "k2B_cert_summary_r4.json"):
        "ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b",
    os.path.join(CODE, "gram_enc.py"): "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833",
    os.path.join(CODE, "gram_encB.py"): "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
    CLASSFILE: "898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158",
    os.path.join(CODE, "gram_certify_r4.py"): "ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a",
    DRAT: "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37",
    CADICAL: "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa",
    KISSAT: "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848",
}
RUNTIME_PINS = [os.path.join(CODE, "gram_enc.py"), os.path.join(CODE, "gram_encB.py"), CLASSFILE,
                DRAT, CADICAL, KISSAT]


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
    st = os.statvfs(REVIEW)
    return st.f_bavail * st.f_frsize


def check_runtime_pins():
    bad = {p: sha_file(p) for p in RUNTIME_PINS if sha_file(p) != PINS[p]}
    return bad


def write_json_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=2, sort_keys=False)
        f.write("\n")


# --- RSS through libproc (macOS sys/proc_info.h: PROC_PIDTASKINFO = 4, struct proc_taskinfo is 96 bytes,
# pti_resident_size is the uint64 at offset 8).
_LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
_LIBPROC.proc_pidinfo.restype = ctypes.c_int


def rss(pid):
    buf = ctypes.create_string_buffer(96)
    n = _LIBPROC.proc_pidinfo(pid, 4, 0, buf, 96)
    return struct.unpack_from("=Q", buf.raw, 8)[0] if n == 96 else 0


# --- lane load: native solver/checker processes whose cwd or argv lies in the moqls7-maximum lane or in a
# review/moqls7-* desk (excluding this desk's own children, which are never alive when this is called).
LANE_MARKERS = ("/moqls7-maximum", "/review/moqls7-")
NATIVE = {"cadical", "kissat", "drat-trim", "lrat-check", "lrat-trim", "cake_lpr", "dpr-trim", "glucose",
          "minisat", "lingeling", "plingeling", "treengeling", "cryptominisat5", "kissat_mab", "dpr2pr"}


def lane_processes():
    ps = subprocess.run(["/bin/ps", "-axww", "-o", "pid=,ppid=,pcpu=,rss=,state=,comm="],
                        capture_output=True, text=True, env=ENV).stdout
    cand = []
    for line in ps.splitlines():
        parts = line.split(None, 5)
        if len(parts) < 6:
            continue
        pid, ppid, pcpu, rss_kb, state, comm = parts
        base = os.path.basename(comm.strip())
        native = base in NATIVE
        pyhot = base.lower().startswith("python") and float(pcpu) >= 50.0
        if (native or pyhot) and int(ppid) != os.getpid():
            cand.append({"pid": int(pid), "ppid": int(ppid), "pcpu": float(pcpu), "rss_kb": int(rss_kb),
                         "state": state, "comm": comm.strip(), "native": native})
    if not cand:
        return []
    pids = ",".join(str(c["pid"]) for c in cand)
    lo = subprocess.run(["/usr/sbin/lsof", "-a", "-d", "cwd", "-p", pids, "-Fpn"],
                        capture_output=True, text=True, env=ENV).stdout
    cwd, cur = {}, None
    for line in lo.splitlines():
        if line.startswith("p"):
            cur = int(line[1:])
        elif line.startswith("n") and cur is not None:
            cwd[cur] = line[1:]
    args = {}
    a = subprocess.run(["/bin/ps", "-ww", "-o", "pid=,args=", "-p", pids], capture_output=True, text=True,
                       env=ENV).stdout
    for line in a.splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            args[int(parts[0])] = parts[1]
    out = []
    for c in cand:
        c["cwd"] = cwd.get(c["pid"], "")
        c["args"] = args.get(c["pid"], "")[:300]
        if any(m in c["cwd"] or m in c["args"] for m in LANE_MARKERS):
            out.append(c)
    return out


def wait_for_capacity(log, mine=2, lane_cap=4, poll=60, max_wait=4 * 3600):
    """Fresh launch check. Disk below FLOOR_LAUNCH -> return {"deferred": ...} at once (parent rule: defer,
    report once, wait for the parent; no disk polling). Lane at capacity -> wait, polling every `poll` s."""
    t0 = time.monotonic()
    waited = []
    while True:
        fb = free_bytes()
        if fb < FLOOR_LAUNCH:
            log("deferred: free=%d < %d" % (fb, FLOOR_LAUNCH))
            return {"deferred": "free space %d below launch threshold %d" % (fb, FLOOR_LAUNCH),
                    "free_bytes": fb, "at": now(), "wait_samples": waited}
        procs = lane_processes()
        if len(procs) + mine <= lane_cap:
            return {"lane_other_busy": len(procs), "lane_other": [
                {k: p[k] for k in ("pid", "comm", "state", "pcpu", "rss_kb", "cwd")} for p in procs],
                "free_bytes": fb, "launch_threshold": FLOOR_LAUNCH,
                "waited_seconds": round(time.monotonic() - t0, 1), "wait_samples": waited}
        waited.append({"at": now(), "lane_other_busy": len(procs), "free_bytes": fb})
        log("capacity wait: lane_other_busy=%d free=%d" % (len(procs), fb))
        if time.monotonic() - t0 > max_wait:
            return None
        time.sleep(poll)


# --- class key decoding (claim section 3: 36 digits = entries off the first row/column, row-major)
def decode_key(key):
    if len(key) != 36 or not key.isdigit():
        raise ValueError("bad key " + key)
    L = [[0] * 7 for _ in range(7)]
    L[0] = list(range(7))
    for r in range(7):
        L[r][0] = r
    for t, ch in enumerate(key):
        L[1 + t // 6][1 + t % 6] = int(ch)
    for i in range(7):
        if sorted(L[i]) != list(range(7)) or sorted(L[r][i] for r in range(7)) != list(range(7)):
            raise ValueError("not a Latin square: " + key)
    return L


def read_classes():
    with open(CLASSFILE) as f:
        return [line.split() for line in f if line.strip()]


# --- encoders, run as subprocesses from the pinned lane files (replay only; -B, no bytecode written)
A_WRAPPER = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import gram_enc
assert gram_enc.__file__ == sys.argv[1] + "/gram_enc.py", gram_enc.__file__
L = json.loads(sys.stdin.read())
F, _ = gram_enc.build(2, L, sys.argv[2] == "heavy", False, None)
sys.stdout.buffer.write(F.text().encode("ascii"))
'''


def _drain(stream, sink):
    sink.append(stream.read())
    stream.close()


def encode_A(L, heavy=True):
    t0 = time.monotonic()
    argv = [PY, "-B", "-c", A_WRAPPER, CODE, "heavy" if heavy else "noheavy"]
    p = subprocess.run(argv, input=json.dumps(L).encode(), capture_output=True, cwd=TMP, env=ENV)
    info = {"argv": ["/usr/bin/python3", "-B", "-c", "<A_WRAPPER: gram_enc.build(2, L, %s, False, None)>"
                     % bool(heavy), CODE, "heavy" if heavy else "noheavy"],
            "rc": p.returncode, "stderr": p.stderr.decode(errors="replace")[-2000:],
            "seconds": round(time.monotonic() - t0, 3), "bytes": len(p.stdout)}
    return (p.stdout if p.returncode == 0 else None), info


def encode_B(L, heavy=True):
    t0 = time.monotonic()
    r, w = os.pipe()
    argv = [PY, "-B", os.path.join(CODE, "gram_encB.py"), "--squares", "2", "--net-L", "/dev/stdin"]
    argv += (["--heavy"] if heavy else []) + ["--out", "/dev/fd/%d" % w]
    p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         pass_fds=(w,), cwd=TMP, env=ENV)
    os.close(w)
    out, err = [], []
    ts = [threading.Thread(target=_drain, args=(p.stdout, out)), threading.Thread(target=_drain, args=(p.stderr, err))]
    for t in ts:
        t.start()
    p.stdin.write(json.dumps(L).encode())
    p.stdin.close()
    chunks = []
    while True:
        b = os.read(r, 1 << 20)
        if not b:
            break
        chunks.append(b)
    os.close(r)
    rc = p.wait()
    for t in ts:
        t.join()
    data = b"".join(chunks)
    info = {"argv": argv, "rc": rc, "stdout": out[0].decode(errors="replace")[-500:],
            "stderr": err[0].decode(errors="replace")[-2000:], "seconds": round(time.monotonic() - t0, 3),
            "bytes": len(data)}
    return (data if rc == 0 else None), info


def cnf_header(cnf):
    head = cnf[:cnf.index(b"\n")].split()
    if head[:2] != [b"p", b"cnf"]:
        raise ValueError("no DIMACS header")
    return int(head[2]), int(head[3])


# --- the solver -> FIFO -> drat-trim pipeline
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


def status_lines(log_bytes):
    text = log_bytes.decode(errors="replace").replace("\r", "\n")
    return [ln.strip() for ln in text.split("\n") if ln.strip().startswith("s ")]


def solver_argv(kind, seconds):
    if kind == "cadical":
        return [CADICAL, "-q", "-t", str(seconds)]
    if kind == "kissat":
        return [KISSAT, "-q", "-f", "--time=%d" % seconds]
    raise ValueError(kind)


def pipeline(label, cnf, solver=None, proof=None, solver_seconds=900, checker_seconds=1800, checker_cnf=None):
    """Run (solver | parent proof bytes) -> FIFO -> drat-trim. Exactly one of solver/proof is given.
    checker_cnf (controls only) lets drat-trim read a different formula from the one the solver gets."""
    if (solver is None) == (proof is None):
        raise ValueError("exactly one of solver/proof")
    if checker_cnf is None:
        checker_cnf = cnf
    fifo = os.path.join(DESK, "fifo", label + ".drat.fifo")
    slog = os.path.join(DESK, "logs", label + ".solver.log")
    clog = os.path.join(DESK, "logs", label + ".checker.log")
    for path in (fifo, slog, clog):
        if os.path.lexists(path):
            raise FileExistsError(path)
    os.mkfifo(fifo)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    fcntl.fcntl(rfd, fcntl.F_SETFL, fcntl.fcntl(rfd, fcntl.F_GETFL) & ~os.O_NONBLOCK)
    kfd = os.open(fifo, os.O_WRONLY)          # parent-held writer (keepalive)
    ccr, ccw = os.pipe()
    rec = {"label": label, "started_at": now(), "cnf_bytes": len(cnf), "cnf_sha256": sha_bytes(cnf),
           "checker_cnf_sha256": sha_bytes(checker_cnf),
           "checker_argv": [DRAT, "/dev/fd/<cnf-pipe>", "-i", "-t", str(checker_seconds)],
           "fifo": os.path.relpath(fifo, DESK)}
    t0 = time.monotonic()
    writers = {}
    procs = {}
    with open(clog, "xb") as cl:
        sl = open(slog, "xb") if solver else None
        try:
            check = subprocess.Popen([DRAT, "/dev/fd/%d" % ccr, "-i", "-t", str(checker_seconds)], stdin=rfd,
                                     stdout=cl, stderr=subprocess.STDOUT, pass_fds=(ccr,), cwd=TMP, env=ENV)
            os.close(rfd)
            os.close(ccr)
            procs["checker"] = check
            writers["checker_cnf"] = _start_writer(ccw, checker_cnf)
            if solver:
                scr, scw = os.pipe()
                argv = solver + ["/dev/fd/%d" % scr, fifo]
                rec["solver_argv"] = solver + ["/dev/fd/<cnf-pipe>", os.path.relpath(fifo, DESK)]
                solve = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=sl, stderr=subprocess.STDOUT,
                                         pass_fds=(scr,), cwd=TMP, env=ENV)
                os.close(scr)
                procs["solver"] = solve
                writers["solver_cnf"] = _start_writer(scw, cnf)
            else:
                rec["proof_source"] = "parent bytes"
                rec["proof_bytes_sha256"] = sha_bytes(proof)
                rec["proof_len"] = len(proof)
                writers["proof"] = _start_writer(kfd, proof)
                kfd = None
            done, peak, reason, term_at = {}, 0, None, None
            while len(done) < len(procs):
                for name, p in procs.items():
                    if name in done:
                        continue
                    pid, st, ru = os.wait4(p.pid, os.WNOHANG)
                    if pid:
                        rc = os.waitstatus_to_exitcode(st)
                        p.returncode = rc
                        done[name] = {"rc": rc, "maxrss_bytes": ru.ru_maxrss,
                                      "wall_seconds": round(time.monotonic() - t0, 3),
                                      "user_seconds": round(ru.ru_utime, 3), "sys_seconds": round(ru.ru_stime, 3)}
                        if name == "solver" and kfd is not None:
                            os.close(kfd)
                            kfd = None
                if len(done) == len(procs):
                    break
                cur = rss(os.getpid()) + sum(rss(p.pid) for n, p in procs.items() if n not in done)
                peak = max(peak, cur)
                if reason is None:
                    if cur > RSS_STOP:
                        reason = "aggregate RSS safety stop %d" % cur
                    elif free_bytes() < FLOOR:
                        reason = "free-space floor"
                    elif time.monotonic() - t0 > solver_seconds + checker_seconds + 120:
                        reason = "combined wall-clock backstop"
                    if reason:
                        term_at = time.monotonic()
                        for n, p in procs.items():
                            if n not in done:
                                os.kill(p.pid, signal.SIGTERM)
                elif time.monotonic() - term_at > 120:
                    raise RuntimeError("SIGTERM grace exceeded; no SIGKILL sent: " + label)
                time.sleep(0.25)
        finally:
            if kfd is not None:
                os.close(kfd)
            if sl:
                sl.close()
    for name, (t, res) in writers.items():
        t.join()
    rec["finished_at"] = now()
    rec["pipeline_seconds"] = round(time.monotonic() - t0, 3)
    rec["children"] = done
    rec["writers"] = {k: v[1] for k, v in writers.items()}
    rec["peak_sampled_aggregate_rss_bytes"] = peak
    rec["safety_stop_reason"] = reason
    with open(clog, "rb") as f:
        cbytes = f.read()
    rec["checker_log"] = os.path.relpath(clog, DESK)
    rec["checker_log_sha256"] = sha_bytes(cbytes)
    rec["checker_status_lines"] = status_lines(cbytes)
    if solver:
        with open(slog, "rb") as f:
            sbytes = f.read()
        rec["solver_log"] = os.path.relpath(slog, DESK)
        rec["solver_log_sha256"] = sha_bytes(sbytes)
        rec["solver_status_lines"] = status_lines(sbytes)
        rec["solver_log_bytes"] = len(sbytes)
    lines = rec["checker_status_lines"]
    rec["checker_verified"] = ("s VERIFIED" in lines and "s NOT VERIFIED" not in lines
                               and "s TIMEOUT" not in lines and done.get("checker", {}).get("rc") == 0
                               and reason is None)
    return rec
