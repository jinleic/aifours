#!/usr/bin/env python3
"""PA19StoredProofReplay v2: native parent drat-trim replay of the retained M1 route-a DRAT proofs (2490 A2 cases)
and the retained E0 DRAT proofs (486 graphs), read in place from the lane. Not a theorem, gate or M1 verdict.
v2 differs from v1 (3bea2d91...) ONLY in receipt storage (desk-cap fit): run writes receipts as one gzip stream
receipts-<chunk>.jsonl.gz with a zlib Z_SYNC_FLUSH + fsync after every line (prefix-decodable if interrupted);
load_done/finalize read .jsonl and .jsonl.gz; finalize writes DESK/RESULT.json. freeze/controls/check_case, the
checker invocation, guards and the PASS predicate are unchanged (freeze and controls were run under v1).

Subcommands (every output is created exclusively; nothing outside DESK is written; lane files are only opened
O_RDONLY; no CNF or proof is copied):
  freeze   --lane L                 -> DESK/manifest-v1.jsonl, DESK/freeze-v1.json
  controls --lane L                 -> DESK/controls-v1/ (own tiny CNF/DRAT files, receipts, raw log, result)
  run      --lane L --manifest M --manifest-sha S --chunk ID --script-sha X [--start I] [--stop J] [--max-seconds N]
  finalize --lane L --manifest M --manifest-sha S --script-sha X  -> DESK/RESULT.json
Manifest source: the independent audit R/pa19-final-receipts-v1 (M1-manifest-compact.tsv route a in audit order, then
run-v1/cases-E0.jsonl in audit order); route-a CNF expectations reuse the parent R5 rebuild
(R/pa19-cnf-binding-v1/cnf-binding-result.json) by hash. No recursive discovery of proof files.
Checker: parent-built drat-trim (R/moqls7-parent-proofcheck-v1/drat-trim, sha a46c0c71..., upstream source d834b649...),
argv [DT, CNF, PROOF, '-t', '1200'] (standard path mode; binary DRAT is auto-detected by the checker). One native
child at a time. One EXISTING lane token is held per case from pre-hash to post-hash: read-only fd + flock, token
files never written, COUNT never written (semantics of R/pa19-final-receipts-v1/token_ro.py 8e069589...), with a
bounded blocking wait (SIGALRM) instead of an unbounded one.
Guards per case: hard wall 1320 s from token acquisition (includes hashing), native -t 1200, SIGTERM then a bounded
30 s wait; if the child survives the grace, the token stays held until the child exits (quarantine) and the chunk
stops; no SIGKILL. Child+driver resident size < 3.5 GiB (sampled every 0.2 s); free disk >= 12e9 B continuously
(sampled every 1 s); raw log <= 2 MiB per case; desk allocation <= 20e6 B; admission gate free >= 12334217728 +
20 MiB; chunk <= 10800 s; no case admitted unless it can finish by 2026-10-18 18:00 PDT.
PASS iff: rc 0 and self-exit (no signal sent or received); after removing only '\\r' bytes, the lines starting with
's ' are exactly ['s VERIFIED']; no fatal marker; exactly one 'c parsing input formula with V variables and C clauses'
line with (V, C) equal to the CNF p-line and to the manifest expectation; exactly one 'c finished parsing, read N
bytes from proof file' line with N equal to the proof size; exactly one 'c turning on binary mode checking' line;
CNF/proof sha256 before and after the check equal to the pinned expectations, proof size equal to the recorded size,
(dev, ino, size, mtime_ns) unchanged; checker sha before and after equal to the pin; no guard fired. Otherwise UNKNOWN.
No retries: an index with any receipt line (intent or final) is never run again.
"""
import ctypes
import fcntl
import hashlib
import json
import os
import re
import signal
import sys
import time
import zlib
from datetime import datetime
from zoneinfo import ZoneInfo

A = "/Users/jinleic/repos/aifours"
LANE = A + "/information-science/evidence/six-lane-20261016/packing-array19"
R = A + "/institute/runs/six-lane-2026-10-16/review"
DESK = R + "/pa19-final-stored-proof-replay-v1"
TMP = DESK + "/tmp"
AUDIT = R + "/pa19-final-receipts-v1"
DT = R + "/moqls7-parent-proofcheck-v1/drat-trim"
DT_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"
R5 = R + "/pa19-cnf-binding-v1/cnf-binding-result.json"
TSV = AUDIT + "/M1-manifest-compact.tsv"
CASES_A2 = AUDIT + "/run-v1/cases-A2.jsonl"
CASES_E0 = AUDIT + "/run-v1/cases-E0.jsonl"
PINS = {
    TSV: "83cc8df69a876991149ed8cba52bd0f4f8c540c1ed33f7c9dae44007c22bbcd1",
    CASES_A2: "d2471123957ae3ebf0bdcffc1e808efcc945a17262da7786668f4dc80f8a0a28",
    CASES_E0: "4a21c6ec37e39f5ca55c3a724154acdaede653bcdaddc463c60cbb88fc023460",
    AUDIT + "/RESULT.json": "797e4cd6c253146ed363d39f739b07dc3bf9cdff3d654309688708f3ef4894b7",
    AUDIT + "/token_ro.py": "8e069589122a553451670fc51ec5ebed77dc9c54c3728a93fcda14f88b334b79",
    R5: "2a14a1dc4eadec733f73ff460814f94ebffa11b81266eb2eaf8c7df7772a22d9",
}
N_ROUTE_A, N_E0 = 2490, 486
TOK = LANE + "/cycle2/tokens"
TZ = ZoneInfo("America/Los_Angeles")
GLOBAL_STOP = datetime(2026, 10, 18, 18, 0, 0, tzinfo=TZ).timestamp()
NATIVE_T = 1200
WALL = 1320
GRACE = 30
RSS_CAP = 3584 * 2 ** 20
DISK_GATE = 12334217728 + 20 * 2 ** 20
DISK_FLOOR = 12000000000
LOG_CASE_CAP = 2 * 2 ** 20
DESK_CAP = 20000000
DESK_RESERVE = 1500000
RECEIPT_MAX = 16384
CHUNK_MAX = 10800
CKPT_EVERY = 900
TOKEN_WAIT_MAX = 1800
SAMPLE = 0.2
DISK_EVERY = 1.0
RSS_FAIL_MAX = 10
FATAL = (b"NOT VERIFIED", b"TIMEOUT", b"MEMOUT", b"ERROR", b"error opening", b"illegal literal", b"early EOF",
         b"clauses less than expected", b"wrong binary prefix", b"trivial UNSAT", b"DERIVATION", b"conflict claimed",
         b"failed at proof line", b"did not find p cnf")
RE_PARSING = re.compile(rb"^c parsing input formula with (\d+) variables and (\d+) clauses$")
RE_FINISHED = re.compile(rb"^c finished parsing(?:, read (\d+) bytes from proof file)?$")
RE_VTIME = re.compile(rb"^c verification time: ([0-9.]+) seconds$")
RE_PLINE = re.compile(rb"^p cnf (\d+) (\d+)\s*$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CHILD_ENV = {"TMPDIR": TMP + "/", "PATH": "/usr/bin:/bin", "LC_ALL": "C", "LANG": "C"}

STATE = {"stop": False, "waiting": False, "signals": []}


def now_iso():
    return datetime.now(TZ).isoformat(timespec="milliseconds")


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(path, header=False):
    """Streamed read-only sha256; optionally captures the first 64 KiB for the CNF p-line."""
    h, n, head = hashlib.sha256(), 0, b""
    fd = os.open(path, os.O_RDONLY)
    try:
        while True:
            b = os.read(fd, 1 << 22)
            if not b:
                break
            if header and len(head) < 65536:
                head += b[:65536 - len(head)]
            h.update(b)
            n += len(b)
    finally:
        os.close(fd)
    return h.hexdigest(), n, (pline(head) if header else None)


def pline(head):
    """(V, C, first_line_is_pline) from the first line starting with b'p ' (strict 'p cnf V C' form), else None."""
    for k, line in enumerate(head.split(b"\n")):
        if line.startswith(b"p "):
            m = RE_PLINE.match(line)
            return [int(m.group(1)), int(m.group(2)), k == 0] if m else None
    return None


def stat_of(path):
    st = os.stat(path)
    import stat as _s
    return {"dev": st.st_dev, "ino": st.st_ino, "size": st.st_size, "mtime_ns": st.st_mtime_ns,
            "ctime_ns": st.st_ctime_ns, "regular": _s.S_ISREG(st.st_mode)}


def same_stat(a, b):
    return all(a[k] == b[k] for k in ("dev", "ino", "size", "mtime_ns", "regular"))


def disk_free():
    s = os.statvfs(LANE)
    return s.f_bavail * s.f_frsize


def desk_alloc():
    tot = 0
    for root, dirs, files in os.walk(DESK):
        for f in files:
            try:
                tot += os.lstat(os.path.join(root, f)).st_blocks * 512
            except OSError:
                pass
    return tot


def interp_pins():
    exe = os.path.realpath(sys.executable)
    out = {"sys_executable": sys.executable, "realpath": exe, "sha256": sha_file(exe)[0], "version": sys.version}
    fw = os.path.join(sys.base_prefix, "Python")
    if os.path.isfile(fw):
        out["framework_lib"] = fw
        out["framework_lib_sha256"] = sha_file(fw)[0]
    return out


def own_sha():
    return sha_file(os.path.abspath(__file__))[0]


def verify_pins():
    got = {}
    for p, want in PINS.items():
        s = sha_file(p)[0]
        if s != want:
            raise SystemExit("PIN MISMATCH %s: %s != %s" % (p, s, want))
        got[p] = s
    return got


def write_new(path, data):
    with open(path, "xb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())


def jdump(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":")).encode() + b"\n"


def write_all(fd, b):
    while b:
        n = os.write(fd, b)
        b = b[n:]


class GzLines:
    """Append-only gzip stream (one member): Z_SYNC_FLUSH + fsync after every line, so any prefix is decodable."""

    def __init__(self, path):
        self.path = path
        self.fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
        self.co = zlib.compressobj(9, zlib.DEFLATED, 31)

    def write(self, line):
        write_all(self.fd, self.co.compress(line) + self.co.flush(zlib.Z_SYNC_FLUSH))
        os.fsync(self.fd)

    def close(self):
        write_all(self.fd, self.co.flush(zlib.Z_FINISH))
        os.fsync(self.fd)
        os.close(self.fd)


def receipt_lines(path):
    """(complete lines, partial_tail_flag) of a plain or gzip receipt file; a gzip stream without trailer is decoded
    up to its last flush; an incomplete last line is dropped and flagged."""
    data = open(path, "rb").read()
    if path.endswith(".gz"):
        data = zlib.decompressobj(31).decompress(data)
    parts = data.split(b"\n")
    partial = parts[-1].strip() != b""
    return [ln for ln in parts[:-1] if ln.strip()], partial


def receipt_files():
    return [fn for fn in sorted(os.listdir(DESK))
            if fn.startswith("receipts-") and (fn.endswith(".jsonl") or fn.endswith(".jsonl.gz"))]


# ---------------------------------------------------------------- resident size (libproc proc_pid_rusage)
class _RUI2(ctypes.Structure):
    _fields_ = [("ri_uuid", ctypes.c_uint8 * 16)] + [(n, ctypes.c_uint64) for n in (
        "ri_user_time", "ri_system_time", "ri_pkg_idle_wkups", "ri_interrupt_wkups", "ri_pageins", "ri_wired_size",
        "ri_resident_size", "ri_phys_footprint", "ri_proc_start_abstime", "ri_proc_exit_abstime",
        "ri_child_user_time", "ri_child_system_time", "ri_child_pkg_idle_wkups", "ri_child_interrupt_wkups",
        "ri_child_pageins", "ri_child_elapsed_abstime", "ri_diskio_bytesread", "ri_diskio_byteswritten")] + [
        ("pad", ctypes.c_uint8 * 512)]


_LIB = ctypes.CDLL("/usr/lib/libSystem.B.dylib", use_errno=True)
_PPR = _LIB.proc_pid_rusage
_PPR.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(_RUI2)]
_PPR.restype = ctypes.c_int


def resident(pid):
    ri = _RUI2()
    if _PPR(pid, 2, ctypes.byref(ri)) != 0:
        return None
    return int(ri.ri_resident_size)


# ---------------------------------------------------------------- signals and token
class _Alarm(Exception):
    pass


class _Stop(Exception):
    pass


def _on_term(signum, frame):
    STATE["stop"] = True
    STATE["signals"].append([signum, now_iso()])
    if STATE["waiting"]:
        raise _Stop()


def _on_alarm(signum, frame):
    if STATE["waiting"]:
        raise _Alarm()


def install_signals():
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, _on_term)


def token_count():
    with open(os.path.join(TOK, "COUNT")) as f:
        return max(0, int(f.read().split()[0]))


class Token:
    """One existing lane token t<i> (i < COUNT): O_RDONLY + flock; never creates/truncates/writes token files."""

    def __init__(self):
        self.fd, self.name, self.info = None, None, {}

    def acquire(self, max_wait):
        t0 = time.time()
        info = {"requested_at": now_iso(), "max_wait_s": round(max_wait, 1)}
        self.info = info
        n = token_count()
        info["count_at_request"] = n
        if n < 1:
            info["refused"] = "COUNT=%d" % n
            return False
        for i in range(n):
            p = os.path.join(TOK, "t%d" % i)
            if not os.path.isfile(p):
                info["refused"] = "token file missing: " + p
                return False
            fd = os.open(p, os.O_RDONLY)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                os.close(fd)
                continue
            self.fd, self.name = fd, "t%d" % i
            break
        if self.fd is None:
            if max_wait <= 0:
                info["refused"] = "no free token and no wait budget"
                return False
            fd = os.open(os.path.join(TOK, "t0"), os.O_RDONLY)
            got = False
            old = signal.signal(signal.SIGALRM, _on_alarm)
            try:
                STATE["waiting"] = True
                if STATE["stop"]:
                    raise _Stop()
                signal.setitimer(signal.ITIMER_REAL, max_wait)
                fcntl.flock(fd, fcntl.LOCK_EX)
                got = True
            except (_Alarm, _Stop) as e:
                info["wait_interrupted"] = type(e).__name__
            finally:
                STATE["waiting"] = False
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, old)
            if not got:
                os.close(fd)  # also releases a lock granted inside the race window
                info["refused"] = "bounded token wait ended without a token"
                info["waited_s"] = round(time.time() - t0, 3)
                return False
            self.fd, self.name = fd, "t0"
        info["name"] = self.name
        info["waited_s"] = round(time.time() - t0, 3)
        info["acquired_at"] = now_iso()
        n2 = token_count()
        info["count_after_acquire"] = n2
        if int(self.name[1:]) >= n2 or STATE["stop"]:
            self.release()
            info["refused"] = "COUNT dropped below held index or stop requested"
            return False
        return True

    def release(self):
        if self.fd is not None:
            fcntl.flock(self.fd, fcntl.LOCK_UN)
            os.close(self.fd)
            self.fd = None
            self.info["released_at"] = now_iso()


# ---------------------------------------------------------------- one native check
def parse_log(raw):
    lines = [ln.replace(b"\r", b"") for ln in raw.split(b"\n")]
    s_lines = [ln for ln in lines if ln.startswith(b"s ")]
    fatal = {}
    for ln in lines:
        for m in FATAL:
            if m in ln:
                fatal[m.decode()] = fatal.get(m.decode(), 0) + 1
    parsing = [[int(m.group(1)), int(m.group(2))] for m in (RE_PARSING.match(ln) for ln in lines) if m]
    finished = [m for m in (RE_FINISHED.match(ln) for ln in lines) if m]
    vt = [float(m.group(1)) for m in (RE_VTIME.match(ln) for ln in lines) if m]
    return {
        "s_lines": [x.decode("utf-8", "replace") for x in s_lines[:20]],
        "n_s_lines": len(s_lines),
        "n_exact_s_verified": sum(1 for ln in lines if ln == b"s VERIFIED"),
        "fatal_markers": fatal,
        "parsing_lines": parsing[:5],
        "n_parsing_lines": len(parsing),
        "finished_read_bytes": [int(m.group(1)) if m.group(1) is not None else None for m in finished][:5],
        "n_finished_lines": len(finished),
        "n_binary_mode_lines": sum(1 for ln in lines if ln == b"c turning on binary mode checking"),
        "n_warning_lines": sum(1 for ln in lines if ln.startswith(b"c WARNING")),
        "verification_time_s": vt[:3],
        "n_lines": len(lines),
    }


def check_case(case, tok, logf, chunk, interp):
    """Runs one case (token already held). Returns (receipt dict, chunk_stop_reason or None)."""
    t_case0 = time.time()
    deadline = t_case0 + WALL
    rec = {"schema": "pa19-stored-proof-replay-receipt-v1", "kind": "final", "i": case["i"], "set": case["set"],
           "tag": case["tag"], "chunk": chunk, "cnf": case["cnf"], "proof": case["proof"],
           "expect": {k: case[k] for k in ("expect_cnf_sha256", "expect_proof_sha256", "expect_proof_bytes",
                                            "expect_header")},
           "t_case_start": now_iso(), "interpreter_sha256": interp["sha256"],
           "guards_cfg": {"native_t": NATIVE_T, "wall": WALL, "grace": GRACE, "rss_cap": RSS_CAP,
                          "disk_floor": DISK_FLOOR, "log_case_cap": LOG_CASE_CAP}}
    reasons, stop = [], None
    # ---- pre-exec pins and input binding
    pre = {"t": now_iso()}
    th = time.time()
    try:
        pre["checker_sha256"] = sha_file(DT)[0]
        pre["cnf_stat"] = stat_of(case["cnf"])
        pre["proof_stat"] = stat_of(case["proof"])
        pre["cnf_sha256"], pre["cnf_bytes"], pre["cnf_pline"] = sha_file(case["cnf"], header=True)
        pre["proof_sha256"], pre["proof_bytes"], _ = sha_file(case["proof"])
    except OSError as e:
        pre["error"] = repr(e)
        rec.update({"pre": pre, "argv": [DT, case["cnf"], case["proof"], "-t", str(NATIVE_T)],
                    "native": {"started": False}, "state": "UNKNOWN",
                    "reasons": ["not run: input or checker unreadable before the check"]})
        return rec, None
    pre["hash_seconds"] = round(time.time() - th, 3)
    rec["pre"] = pre
    if pre["checker_sha256"] != DT_SHA:
        reasons.append("checker sha pre != pin")
        stop = "checker_sha_mismatch"
    if pre["cnf_sha256"] != case["expect_cnf_sha256"]:
        reasons.append("cnf sha pre != expectation")
    if pre["proof_sha256"] != case["expect_proof_sha256"]:
        reasons.append("proof sha pre != expectation")
    if pre["proof_bytes"] != case["expect_proof_bytes"] or pre["proof_stat"]["size"] != case["expect_proof_bytes"]:
        reasons.append("proof size != recorded size")
    if not (pre["cnf_stat"]["regular"] and pre["proof_stat"]["regular"]):
        reasons.append("input not a regular file")
    pl = pre["cnf_pline"]
    if pl is None or [pl[0], pl[1]] != case["expect_header"]:
        reasons.append("cnf p-line != manifest header expectation")
    if time.time() + 1 >= deadline:
        reasons.append("wall reached during pre-hash")
    argv = [DT, case["cnf"], case["proof"], "-t", str(NATIVE_T)]
    rec["argv"] = argv
    rec["cwd"] = TMP
    rec["env"] = CHILD_ENV
    nat = {"started": False}
    rec["native"] = nat
    if reasons:
        rec["state"] = "UNKNOWN"
        rec["reasons"] = ["not run: " + r for r in reasons]
        return rec, stop
    # ---- spawn
    hdr = ("\n### BEGIN i=%d set=%s tag=%s chunk=%s t=%s\n" % (case["i"], case["set"], case["tag"], chunk,
                                                              now_iso())).encode()
    os.write(logf, hdr)
    log_start = os.fstat(logf).st_size
    sigdef = (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGPIPE, signal.SIGXFSZ, signal.SIGALRM)
    t_spawn = time.time()
    try:
        pid = os.posix_spawn(DT, argv, CHILD_ENV,
                             file_actions=[(os.POSIX_SPAWN_OPEN, 0, "/dev/null", os.O_RDONLY, 0),
                                           (os.POSIX_SPAWN_DUP2, logf, 1), (os.POSIX_SPAWN_DUP2, logf, 2)],
                             setsigdef=sigdef, setsigmask=())
    except OSError as e:
        nat["spawn_error"] = repr(e)
        rec["state"] = "UNKNOWN"
        rec["reasons"] = ["spawn failed"]
        return rec, "spawn_failed"
    nat.update({"started": True, "pid": pid, "t_spawn": now_iso()})
    sig_reason, t_sig, quarantine = None, None, None
    peak_c, peak_d, nsamp, nfail, consec_fail = 0, 0, 0, 0, 0
    min_free, last_disk = None, 0.0
    status = ru = None
    try:
        while True:
            wpid, st, r = os.wait4(pid, os.WNOHANG)
            if wpid == pid:
                status, ru = st, r
                break
            now = time.time()
            if sig_reason is None:
                reason = None
                c = resident(pid)
                d = resident(os.getpid())
                if c is None:
                    nfail += 1
                    consec_fail += 1
                else:
                    nsamp += 1
                    consec_fail = 0
                    peak_c = max(peak_c, c)
                if d is not None:
                    peak_d = max(peak_d, d)
                if now - last_disk >= DISK_EVERY:
                    last_disk = now
                    fr = disk_free()
                    min_free = fr if min_free is None else min(min_free, fr)
                    if fr < DISK_FLOOR:
                        reason = "disk_floor"
                if STATE["stop"]:
                    reason = "driver_signal"
                elif now >= deadline:
                    reason = "wall"
                elif c is not None and c + (d or 0) > RSS_CAP:
                    reason = "rss"
                elif consec_fail >= RSS_FAIL_MAX:
                    reason = "rss_unmeasurable"
                elif os.fstat(logf).st_size - log_start > LOG_CASE_CAP:
                    reason = "log_cap"
                if reason is not None:
                    os.kill(pid, signal.SIGTERM)
                    sig_reason, t_sig = reason, now
                    nat["sigterm_at"] = now_iso()
            elif now >= t_sig + GRACE:
                quarantine = {"from": now_iso()}
                wpid, st, r = os.wait4(pid, 0)  # token stays held until the child exits; no further signal
                status, ru = st, r
                quarantine["until"] = now_iso()
                break
            time.sleep(0.02 if now - t_spawn < 0.5 else SAMPLE)
    finally:
        if status is None:  # unexpected driver exception: own SIGTERM, bounded wait, then quarantine-wait
            try:
                os.kill(pid, signal.SIGTERM)
                t_x = time.time()
                while time.time() < t_x + GRACE:
                    wpid, st, r = os.wait4(pid, os.WNOHANG)
                    if wpid == pid:
                        status, ru = st, r
                        break
                    time.sleep(SAMPLE)
                if status is None:
                    status, ru = os.wait4(pid, 0)[1:]
            except ChildProcessError:
                pass
    t_end = time.time()
    nat.update({"t_end": now_iso(), "elapsed_s": round(t_end - t_spawn, 3), "wait_status": status,
                "exited": os.WIFEXITED(status), "rc": os.WEXITSTATUS(status) if os.WIFEXITED(status) else None,
                "signaled": os.WIFSIGNALED(status), "termsig": os.WTERMSIG(status) if os.WIFSIGNALED(status) else None,
                "maxrss_bytes": ru.ru_maxrss, "utime_s": round(ru.ru_utime, 3), "stime_s": round(ru.ru_stime, 3),
                "sigterm_reason": sig_reason, "quarantine": quarantine,
                "rss_samples": nsamp, "rss_sample_failures": nfail, "peak_sampled_child_rss": peak_c,
                "peak_sampled_driver_rss": peak_d, "min_free_bytes_seen": min_free})
    nat["self_exit"] = bool(nat["exited"] and sig_reason is None and not nat["signaled"])
    # ---- raw log (exact bytes written by the child)
    log_end = os.fstat(logf).st_size
    rfd = os.open(LOGPATH[0], os.O_RDONLY)
    try:
        raw = b""
        while len(raw) < log_end - log_start:
            b = os.pread(rfd, log_end - log_start - len(raw), log_start + len(raw))
            if not b:
                break
            raw += b
    finally:
        os.close(rfd)
    rec["log"] = {"file": os.path.basename(LOGPATH[0]), "offset": log_start, "bytes": len(raw),
                  "sha256": sha_bytes(raw), "complete": len(raw) == log_end - log_start}
    os.write(logf, ("\n### END i=%d raw_bytes=%d raw_sha256=%s\n" % (case["i"], len(raw), sha_bytes(raw))).encode())
    pa = parse_log(raw)
    rec["parse"] = pa
    # ---- post-exec binding
    post = {"t": now_iso()}
    try:
        post["cnf_stat"] = stat_of(case["cnf"])
        post["proof_stat"] = stat_of(case["proof"])
        post["cnf_sha256"] = sha_file(case["cnf"])[0]
        post["proof_sha256"] = sha_file(case["proof"])[0]
        post["checker_sha256"] = sha_file(DT)[0]
    except OSError as e:
        post["error"] = repr(e)
    rec["post"] = post
    # ---- verdict
    if not nat["exited"] or nat["rc"] != 0:
        reasons.append("rc != 0 or not exited (rc=%r termsig=%r)" % (nat["rc"], nat["termsig"]))
    if not nat["self_exit"]:
        reasons.append("not self-exit (sigterm_reason=%r)" % sig_reason)
    if quarantine is not None:
        reasons.append("quarantine: child outlived SIGTERM grace")
    if STATE["stop"]:
        reasons.append("driver stop signal received")
    if pa["s_lines"] != ["s VERIFIED"] or pa["n_s_lines"] != 1 or pa["n_exact_s_verified"] != 1:
        reasons.append("s-lines != ['s VERIFIED']")
    if pa["fatal_markers"]:
        reasons.append("fatal markers present")
    if pa["n_parsing_lines"] != 1 or pa["parsing_lines"][0] != [pl[0], pl[1]] or pa["parsing_lines"][0] != \
            case["expect_header"]:
        reasons.append("parsing line != CNF p-line / expectation")
    if pa["n_finished_lines"] != 1 or pa["finished_read_bytes"][0] != case["expect_proof_bytes"]:
        reasons.append("proof bytes read by checker != proof size")
    if pa["n_binary_mode_lines"] != 1:
        reasons.append("binary-mode line count != 1")
    if not rec["log"]["complete"]:
        reasons.append("raw log read incomplete")
    if "error" in post:
        reasons.append("input or checker unreadable after the check")
    else:
        if post["cnf_sha256"] != case["expect_cnf_sha256"] or post["proof_sha256"] != case["expect_proof_sha256"]:
            reasons.append("input sha changed after check")
        if not (same_stat(pre["cnf_stat"], post["cnf_stat"]) and same_stat(pre["proof_stat"], post["proof_stat"])):
            reasons.append("input stat changed during check")
        if post["checker_sha256"] != DT_SHA:
            reasons.append("checker sha post != pin")
            stop = "checker_sha_mismatch"
    if ru.ru_maxrss >= RSS_CAP:
        reasons.append("child maxrss >= cap")
    rec["state"] = "PASS" if not reasons else "UNKNOWN"
    rec["reasons"] = reasons
    rec["t_case_end"] = now_iso()
    if sig_reason in ("disk_floor", "driver_signal") or quarantine is not None:
        stop = stop or ("quarantine" if quarantine is not None else sig_reason)
    return rec, stop


LOGPATH = [None]


# ---------------------------------------------------------------- subcommands
def need_lane(args):
    if args.get("--lane") != LANE:
        raise SystemExit("--lane must be the absolute lane path " + LANE)


def common_start():
    os.nice(10)
    os.chdir(TMP)
    os.environ["TMPDIR"] = TMP + "/"
    install_signals()


def cmd_freeze(args):
    out_m, out_f = DESK + "/manifest-v1.jsonl", DESK + "/freeze-v1.json"
    t0 = now_iso()
    tok = Token()
    if not tok.acquire(TOKEN_WAIT_MAX):
        raise SystemExit("token refused: %r" % tok.info)
    try:
        pins = verify_pins()
        rows = [ln.rstrip("\n").split("\t") for ln in open(TSV, encoding="utf-8")]
        hdr, rows = rows[0], rows[1:]
        col = {k: j for j, k in enumerate(hdr)}
        a2 = [json.loads(ln) for ln in open(CASES_A2, encoding="utf-8")]
        a2m = {c["tag"]: c for c in a2}
        same_order = [r[col["tag"]] for r in rows] == [c["tag"] for c in a2]
        r5 = json.load(open(R5, encoding="utf-8"))
        r5m = {p["tag"]: p for p in r5["per_tag"]}
        lines, unknown = [], []
        ra = [r for r in rows if r[col["route"]] == "a"]
        for r in ra:
            tag = r[col["tag"]]
            why = []
            c = a2m.get(tag) or {}
            ch = c.get("chosen") or {}
            path, rsha, base = r[col["chosen_path_or_dir"]], r[col["chosen_record_sha256_or_ext_sha256"]], \
                r[col["base_cnf_sha256"]]
            if r[col["state"]] != "COVERED" or c.get("state") != "COVERED":
                why.append("audit state != COVERED")
            if ch.get("route") != "a" or ch.get("path") != path or ch.get("sha256") != rsha:
                why.append("tsv/cases-A2 chosen mismatch")
            if c.get("base_cnf_sha256") != base:
                why.append("tsv/cases-A2 base sha mismatch")
            sp = (ch.get("stored_proof") or {}).get("path")
            if sp != "cases19skel/proof/%s.drat" % tag:
                why.append("stored proof path not canonical")
            if path != "cases19skel/proofcheck/%s.json" % tag:
                why.append("proofcheck path not canonical")
            src = {}
            try:
                b = open(os.path.join(LANE, path), "rb").read()
                src = json.loads(b)
                if sha_bytes(b) != rsha:
                    why.append("source receipt sha != audit pin")
            except (OSError, ValueError) as e:
                why.append("source receipt unreadable: %r" % e)
            p5 = r5m.get(tag) or {}
            if p5.get("status") != "PASS" or p5.get("cnf_sha256") != base:
                why.append("R5 parent binding not PASS/equal")
            if src.get("tag") != tag or src.get("cnf") != "cases19skel/cnf/%s.cnf" % tag or \
                    src.get("cnf_sha256") != base:
                why.append("source receipt tag/cnf/cnf_sha mismatch")
            dsha, dbytes = src.get("drat_sha256"), src.get("drat_bytes")
            if not (isinstance(dsha, str) and HEX64.match(dsha) and isinstance(dbytes, int) and dbytes > 0):
                why.append("source receipt proof sha/bytes malformed")
            cnf, prf = os.path.join(LANE, "cases19skel/cnf/%s.cnf" % tag), os.path.join(LANE, sp or "")
            for p, nm in ((cnf, "cnf"), (prf, "proof")):
                if not os.path.isfile(p):
                    why.append(nm + " missing")
            if os.path.isfile(cnf) and os.stat(cnf).st_size != p5.get("cnf_bytes"):
                why.append("cnf size != R5 cnf_bytes")
            if os.path.isfile(prf) and os.stat(prf).st_size != dbytes:
                why.append("proof size != drat_bytes")
            lines.append({"i": len(lines), "set": "A2-route-a", "tag": tag, "cnf": cnf, "proof": prf,
                          "expect_cnf_sha256": base, "expect_proof_sha256": dsha, "expect_proof_bytes": dbytes,
                          "expect_header": [p5.get("vars"), p5.get("clauses")],
                          "source_receipts": [[path, rsha], [c.get("pass1", {}).get("path"),
                                                             c.get("pass1", {}).get("sha256")]],
                          "cnf_parent_binding": "R5 cnf-binding-result.json 2a14a1dc per_tag PASS (sha, bytes, vars, "
                                                "clauses) reused by hash",
                          "freeze_state": "READY" if not why else "UNKNOWN", "freeze_reasons": why})
            if why:
                unknown.append([tag, why])
        e0 = [json.loads(ln) for ln in open(CASES_E0, encoding="utf-8")]
        for c in e0:
            tag = c["tag"]
            why = []
            res, chk = {}, {}
            for key, slot in (("result", res), ("check", chk)):
                try:
                    b = open(os.path.join(LANE, c[key]["path"]), "rb").read()
                    slot.update(json.loads(b))
                    if sha_bytes(b) != c[key]["sha256"]:
                        why.append(key + " receipt sha != audit pin")
                except (OSError, ValueError, KeyError) as e:
                    why.append(key + " receipt unreadable: %r" % e)
            if not c.get("ok") or c.get("sat") is not False:
                why.append("audit E0 entry not ok/unsat")
            if c["result"]["path"] != "cases19q0/results/%s.json" % tag or \
                    c["check"]["path"] != "cases19q0/results/%s.check.json" % tag:
                why.append("E0 receipt paths not canonical")
            sp = (c.get("stored_proof") or {}).get("path")
            if not (res.get("tag") == chk.get("tag") == tag and res.get("cnf") == "cases19q0/cnf/%s.cnf" % tag and
                    res.get("proof") == sp == "cases19q0/proof/%s.drat" % tag):
                why.append("E0 tag/path mismatch")
            if not (res.get("cnf_sha256") == chk.get("cnf_sha256_now") == chk.get("cnf_sha256_at_solve") ==
                    c.get("cnf_sha256")):
                why.append("E0 cnf sha mismatch")
            if not (chk.get("proof_sha256") == c.get("proof_sha256") and chk.get("proof_bytes") ==
                    res.get("proof_bytes")):
                why.append("E0 proof sha/bytes mismatch")
            if res.get("status") != "UNSAT" or res.get("returncode") != 20:
                why.append("E0 result not UNSAT/20")
            psha, pbytes = c.get("proof_sha256"), chk.get("proof_bytes")
            if not (isinstance(psha, str) and HEX64.match(psha) and isinstance(pbytes, int) and pbytes > 0):
                why.append("E0 proof sha/bytes malformed")
            cnf, prf = os.path.join(LANE, "cases19q0/cnf/%s.cnf" % tag), os.path.join(LANE, sp or "")
            for p, nm in ((cnf, "cnf"), (prf, "proof")):
                if not os.path.isfile(p):
                    why.append(nm + " missing")
            if os.path.isfile(prf) and os.stat(prf).st_size != pbytes:
                why.append("proof size != proof_bytes")
            lines.append({"i": len(lines), "set": "E0", "tag": tag, "cnf": cnf, "proof": prf,
                          "expect_cnf_sha256": c.get("cnf_sha256"), "expect_proof_sha256": psha,
                          "expect_proof_bytes": pbytes, "expect_header": [res.get("vars"), res.get("clauses")],
                          "graph6": c.get("graph6"),
                          "source_receipts": [[c["result"]["path"], c["result"]["sha256"]],
                                              [c["check"]["path"], c["check"]["sha256"]]],
                          "cnf_parent_binding": "none: E0 encode_q0 CNF<->graph6 rebuild pending (TaskA); "
                                                "worker-recorded cnf_sha256 only",
                          "freeze_state": "READY" if not why else "UNKNOWN", "freeze_reasons": why})
            if why:
                unknown.append([tag, why])
        n_a = sum(1 for x in lines if x["set"] == "A2-route-a")
        n_e = sum(1 for x in lines if x["set"] == "E0")
        if n_a != N_ROUTE_A or n_e != N_E0 or len(lines) != N_ROUTE_A + N_E0:
            raise SystemExit("denominator mismatch: route-a %d, E0 %d" % (n_a, n_e))
        if len({(x["set"], x["tag"]) for x in lines}) != len(lines):
            raise SystemExit("duplicate tags in manifest")
        body = b"".join(jdump(x) for x in lines)
        write_new(out_m, body)
        summ = {"schema": "pa19-stored-proof-replay-freeze-v1", "started": t0, "finished": now_iso(),
                "script_sha256": own_sha(), "interpreter": interp_pins(), "pins_verified": pins,
                "token": tok.info, "tsv_order_equals_cases_A2_order": same_order,
                "manifest": os.path.basename(out_m), "manifest_sha256": sha_bytes(body), "manifest_bytes": len(body),
                "counts": {"A2-route-a": n_a, "E0": n_e, "total": len(lines),
                           "ready": sum(1 for x in lines if x["freeze_state"] == "READY"),
                           "unknown_at_freeze": len(unknown)},
                "unknown_at_freeze": unknown,
                "order": "route a in M1-manifest-compact.tsv order, then E0 in cases-E0.jsonl order",
                "not_claimed": "Freeze of stored-pair metadata only; no proof or CNF hashed here."}
        write_new(out_f, json.dumps(summ, indent=1, sort_keys=True).encode() + b"\n")
        print(json.dumps(summ["counts"]), summ["manifest_sha256"])
    finally:
        tok.release()


def load_done():
    done = {}
    for fn in receipt_files():
        lines, _partial = receipt_lines(os.path.join(DESK, fn))
        for ln in lines:
            o = json.loads(ln)
            done.setdefault(o["i"], []).append(o.get("kind"))
    return done


def cmd_run(args):
    chunk = args["--chunk"]
    if not re.match(r"^[0-9a-z-]{1,40}$", chunk):
        raise SystemExit("bad chunk id")
    if own_sha() != args["--script-sha"]:
        raise SystemExit("script sha != --script-sha")
    mpath = args["--manifest"]
    if sha_file(mpath)[0] != args["--manifest-sha"]:
        raise SystemExit("manifest sha mismatch")
    man = [json.loads(ln) for ln in open(mpath, encoding="utf-8")]
    if len(man) != N_ROUTE_A + N_E0:
        raise SystemExit("manifest length mismatch")
    lockfd = os.open(DESK + "/RUN.lock", os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("another driver holds RUN.lock")
    t0 = time.time()
    chunk_end = min(t0 + min(int(args.get("--max-seconds", CHUNK_MAX)), CHUNK_MAX), GLOBAL_STOP)
    start, stop_i = int(args.get("--start", 0)), int(args.get("--stop", len(man)))
    done = load_done()
    interp = interp_pins()
    rpath, cpath = DESK + "/receipts-%s.jsonl.gz" % chunk, DESK + "/checkpoints-%s.jsonl" % chunk
    LOGPATH[0] = DESK + "/rawlog-%s.bin" % chunk
    rw = GzLines(rpath)
    cfd = os.open(cpath, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
    logf = os.open(LOGPATH[0], os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
    head = {"schema": "pa19-stored-proof-replay-chunk-v2", "chunk": chunk, "started": now_iso(),
            "argv": sys.argv, "pid": os.getpid(), "script_sha256": args["--script-sha"],
            "manifest_sha256": args["--manifest-sha"], "checker": DT, "checker_sha256_start": sha_file(DT)[0],
            "interpreter": interp, "start": start, "stop": stop_i, "chunk_end_epoch": chunk_end,
            "already_receipted": len(done), "free_bytes_start": disk_free(), "desk_alloc_start": desk_alloc()}
    counts = {"PASS": 0, "UNKNOWN": 0}
    stop_reason, last_ck, n_done, max_rss, tok_wait = None, 0.0, 0, 0, 0.0
    ran = []

    def ckpt(final=False):
        os.write(cfd, jdump({"t": now_iso(), "chunk": chunk, "final": final, "counts": counts, "cases": n_done,
                             "last_index": ran[-1] if ran else None, "free_bytes": disk_free(),
                             "desk_alloc": desk_alloc(), "max_child_rss": max_rss,
                             "token_wait_s": round(tok_wait, 1)}))
        os.fsync(cfd)

    if head["checker_sha256_start"] != DT_SHA:
        stop_reason = "checker_sha_mismatch_at_start"
    ckpt()
    last_ck = time.time()
    try:
        for case in man[start:stop_i]:
            if stop_reason:
                break
            if case["i"] in done:
                continue
            now = time.time()
            if STATE["stop"]:
                stop_reason = "driver_signal"
                break
            if os.path.exists(DESK + "/STOP"):
                stop_reason = "desk STOP file"
                break
            if now + WALL + GRACE > chunk_end:
                stop_reason = "time_window"
                break
            fr = disk_free()
            if fr < DISK_GATE:
                stop_reason = "disk_gate free=%d" % fr
                break
            da = desk_alloc()
            if da + LOG_CASE_CAP + RECEIPT_MAX > DESK_CAP - DESK_RESERVE:
                stop_reason = "desk_cap alloc=%d" % da
                break
            if case["freeze_state"] != "READY":
                rw.write(jdump({"schema": "pa19-stored-proof-replay-receipt-v1", "kind": "final",
                                "i": case["i"], "set": case["set"], "tag": case["tag"], "chunk": chunk,
                                "state": "UNKNOWN", "native": {"started": False},
                                "reasons": ["freeze: " + r for r in case["freeze_reasons"]]}))
                counts["UNKNOWN"] += 1
                n_done += 1
                ran.append(case["i"])
                continue
            tok = Token()
            if not tok.acquire(min(TOKEN_WAIT_MAX, chunk_end - now - WALL - GRACE)):
                tok_wait += tok.info.get("waited_s", 0) or 0
                stop_reason = "token: " + tok.info.get("refused", "?")
                head.setdefault("token_refusals", []).append(tok.info)
                break
            tok_wait += tok.info["waited_s"]
            try:
                rw.write(jdump({"kind": "intent", "i": case["i"], "tag": case["tag"], "chunk": chunk,
                                "t": now_iso(), "token": tok.name}))
                rec, cstop = check_case(case, tok, logf, chunk, interp)
            finally:
                tok.release()
            rec["token"] = tok.info
            rw.write(jdump(rec))
            counts[rec["state"]] += 1
            n_done += 1
            ran.append(case["i"])
            max_rss = max(max_rss, (rec.get("native") or {}).get("maxrss_bytes") or 0)
            if cstop:
                stop_reason = "case_stop: " + cstop
            if time.time() - last_ck >= CKPT_EVERY:
                ckpt()
                last_ck = time.time()
        else:
            stop_reason = stop_reason or "range_exhausted"
    finally:
        ckpt(final=True)
        rw.close()
        os.close(cfd)
        os.close(logf)
        head.update({"finished": now_iso(), "stop_reason": stop_reason, "counts": counts, "cases_this_chunk": n_done,
                     "first_index": ran[0] if ran else None, "last_index": ran[-1] if ran else None,
                     "max_child_maxrss_bytes": max_rss, "token_wait_s": round(tok_wait, 1),
                     "signals": STATE["signals"], "free_bytes_end": disk_free(), "desk_alloc_end": desk_alloc(),
                     "receipts_sha256": sha_file(rpath)[0], "checkpoints_sha256": sha_file(cpath)[0],
                     "rawlog_sha256": sha_file(LOGPATH[0])[0], "checker_sha256_end": sha_file(DT)[0]})
        write_new(DESK + "/chunk-%s.json" % chunk, json.dumps(head, indent=1, sort_keys=True).encode() + b"\n")
        fcntl.flock(lockfd, fcntl.LOCK_UN)
        os.close(lockfd)
        print(json.dumps({"chunk": chunk, "stop_reason": stop_reason, "counts": counts, "cases": n_done}))


def via_lane(p):
    """Absolute path that literally contains the lane path (for watchdog4 membership) and resolves to p."""
    assert p.startswith(A + "/")
    q = LANE + "/../../../.." + p[len(A):]
    if os.path.realpath(q) != os.path.realpath(p):
        raise SystemExit("via_lane does not resolve: " + q)
    return q


def cmd_controls(args):
    out = DESK + "/controls-v1"
    os.mkdir(out)
    files = {"unsat.cnf": b"p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n",
             "unsat.drat": bytes([0x61, 0x02, 0x00, 0x61, 0x00]),
             "sat.cnf": b"p cnf 2 2\n1 2 0\n-1 2 0\n",
             "forged-empty.drat": bytes([0x61, 0x00])}
    for fn, b in files.items():
        write_new(os.path.join(out, fn), b)
    ctl = [{"i": -1, "set": "CONTROL", "tag": "C1-tiny-unsat-valid-binary-drat", "expected_state": "PASS",
            "cnf": via_lane(out + "/unsat.cnf"), "proof": via_lane(out + "/unsat.drat"),
            "expect_cnf_sha256": sha_bytes(files["unsat.cnf"]), "expect_proof_sha256": sha_bytes(files["unsat.drat"]),
            "expect_proof_bytes": len(files["unsat.drat"]), "expect_header": [2, 4],
            "expected_rc": 0, "expected_s_lines": ["s VERIFIED"], "expected_reasons": []},
           {"i": -2, "set": "CONTROL", "tag": "C2-sat-forged-empty-clause-binary-drat", "expected_state": "UNKNOWN",
            "cnf": via_lane(out + "/sat.cnf"), "proof": via_lane(out + "/forged-empty.drat"),
            "expect_cnf_sha256": sha_bytes(files["sat.cnf"]),
            "expect_proof_sha256": sha_bytes(files["forged-empty.drat"]),
            "expect_proof_bytes": len(files["forged-empty.drat"]), "expect_header": [2, 2],
            "expected_rc": 1, "expected_s_lines": ["s NOT VERIFIED"],
            "expected_reasons": ["rc != 0 or not exited", "s-lines != ['s VERIFIED']", "fatal markers present"]}]
    interp = interp_pins()
    LOGPATH[0] = out + "/rawlog-controls.bin"
    rfd = os.open(out + "/receipts-controls.jsonl", os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
    logf = os.open(LOGPATH[0], os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
    res = {"schema": "pa19-stored-proof-replay-controls-v1", "started": now_iso(), "argv": sys.argv,
           "script_sha256": own_sha(), "interpreter": interp, "checker_sha256": sha_file(DT)[0],
           "files": {fn: sha_bytes(b) for fn, b in files.items()}, "controls": []}
    try:
        for c in ctl:
            tok = Token()
            if not tok.acquire(TOKEN_WAIT_MAX):
                res["controls"].append({"tag": c["tag"], "ok": False, "error": "token: %r" % tok.info})
                continue
            try:
                rec, cstop = check_case(c, tok, logf, "controls", interp)
            finally:
                tok.release()
            rec["token"] = tok.info
            os.write(rfd, jdump(rec))
            os.fsync(rfd)
            pa = rec.get("parse") or {}
            got_r = [x.split(" (")[0] for x in rec["reasons"]]
            res["controls"].append({"tag": c["tag"], "expected_state": c["expected_state"], "state": rec["state"],
                                    "reasons": rec["reasons"], "rc": rec["native"].get("rc"),
                                    "s_lines": pa.get("s_lines"), "parsing_lines": pa.get("parsing_lines"),
                                    "finished_read_bytes": pa.get("finished_read_bytes"),
                                    "ok": (rec["state"] == c["expected_state"] and rec["native"].get("started") is True
                                           and rec["native"].get("rc") == c["expected_rc"]
                                           and pa.get("s_lines") == c["expected_s_lines"]
                                           and sorted(got_r) == sorted(c["expected_reasons"])
                                           and pa.get("parsing_lines") == [c["expect_header"]]
                                           and pa.get("finished_read_bytes") == [c["expect_proof_bytes"]])})
    finally:
        os.close(rfd)
        os.close(logf)
    res["all_ok"] = len(res["controls"]) == 2 and all(x["ok"] for x in res["controls"])
    res["finished"] = now_iso()
    res["receipts_sha256"] = sha_file(out + "/receipts-controls.jsonl")[0]
    res["rawlog_sha256"] = sha_file(LOGPATH[0])[0]
    write_new(out + "/RESULT-controls.json", json.dumps(res, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({"all_ok": res["all_ok"], "controls": [[x["tag"], x.get("state"), x["ok"]]
                                                             for x in res["controls"]]}))


def cmd_finalize(args):
    if own_sha() != args["--script-sha"]:
        raise SystemExit("script sha != --script-sha")
    mpath = args["--manifest"]
    if sha_file(mpath)[0] != args["--manifest-sha"]:
        raise SystemExit("manifest sha mismatch")
    man = [json.loads(ln) for ln in open(mpath, encoding="utf-8")]
    finals, intents, dup, files, partial = {}, {}, [], {}, []
    for fn in receipt_files():
        files[fn] = sha_file(os.path.join(DESK, fn))[0]
        lines, part = receipt_lines(os.path.join(DESK, fn))
        if part:
            partial.append(fn)
        for ln in lines:
            o = json.loads(ln)
            if o.get("kind") == "intent":
                intents.setdefault(o["i"], []).append(fn)
            else:
                if o["i"] in finals:
                    dup.append(o["i"])
                finals[o["i"]] = o
    logs_ok, logs_bad = 0, []
    cache = {}
    for i, o in finals.items():
        lg = o.get("log")
        if not lg:
            continue
        p = os.path.join(DESK, lg["file"])
        if p not in cache:
            cache[p] = open(p, "rb").read()
        if sha_bytes(cache[p][lg["offset"]:lg["offset"] + lg["bytes"]]) == lg["sha256"]:
            logs_ok += 1
        else:
            logs_bad.append(i)
    per = {"A2-route-a": {"PASS": 0, "UNKNOWN": 0, "NOT_ATTEMPTED": 0},
           "E0": {"PASS": 0, "UNKNOWN": 0, "NOT_ATTEMPTED": 0}}
    unresolved, el, mx = [], 0.0, 0
    for c in man:
        o = finals.get(c["i"])
        if o is None:
            st = "UNKNOWN" if c["i"] in intents else "NOT_ATTEMPTED"
            why = ["intent without final receipt (driver interrupted)"] if c["i"] in intents else ["not attempted"]
        else:
            st, why = o["state"], o.get("reasons", [])
            exp = {k: c[k] for k in ("expect_cnf_sha256", "expect_proof_sha256", "expect_proof_bytes", "expect_header")}
            if o["state"] == "PASS" and (o["tag"] != c["tag"] or o["cnf"] != c["cnf"] or o["proof"] != c["proof"]
                                         or o.get("expect") != exp or c["i"] in logs_bad or c["i"] in dup):
                st, why = "UNKNOWN", ["finalize: receipt/manifest identity, duplicate or log hash mismatch"]
            nat = o.get("native") or {}
            el += nat.get("elapsed_s") or 0
            mx = max(mx, nat.get("maxrss_bytes") or 0)
        per[c["set"]][st] += 1
        if st != "PASS":
            unresolved.append({"i": c["i"], "set": c["set"], "tag": c["tag"], "state": st, "reasons": why})
    ctl = None
    cp = DESK + "/controls-v1/RESULT-controls.json"
    if os.path.isfile(cp):
        cj = json.load(open(cp))
        ctl = {"file": "controls-v1/RESULT-controls.json", "sha256": sha_file(cp)[0], "all_ok": cj.get("all_ok"),
               "controls": [[x["tag"], x.get("state"), x.get("ok")] for x in cj.get("controls", [])]}
    chunks = {}
    for fn in sorted(os.listdir(DESK)):
        if fn.startswith("chunk-") and fn.endswith(".json"):
            j = json.load(open(os.path.join(DESK, fn)))
            chunks[fn] = {"sha256": sha_file(os.path.join(DESK, fn))[0], "stop_reason": j.get("stop_reason"),
                          "counts": j.get("counts"), "started": j.get("started"), "finished": j.get("finished"),
                          "max_child_maxrss_bytes": j.get("max_child_maxrss_bytes"),
                          "token_wait_s": j.get("token_wait_s"), "script_sha256": j.get("script_sha256")}
    out = {"schema": "pa19-stored-proof-replay-result-v2", "recorded": now_iso(), "script_sha256": own_sha(),
           "manifest_sha256": args["--manifest-sha"], "denominators": {"A2-route-a": N_ROUTE_A, "E0": N_E0,
                                                                        "total": N_ROUTE_A + N_E0},
           "counts": per, "total_pass": per["A2-route-a"]["PASS"] + per["E0"]["PASS"],
           "unresolved": unresolved, "duplicate_final_receipts": dup, "raw_log_hash_verified": logs_ok,
           "raw_log_hash_mismatch": logs_bad, "receipt_files": files, "receipt_files_with_partial_tail": partial,
           "chunks": chunks, "controls": ctl,
           "sum_native_elapsed_s": round(el, 1), "max_child_maxrss_bytes": mx,
           "checker": {"path": DT, "sha256": DT_SHA},
           "bindings": {"A2-route-a": "CNF bytes equal (pre and post sha) to the parent R5 rebuild hash reused by "
                                      "hash (pa19-cnf-binding-v1 2a14a1dc)",
                        "E0": "CNF bytes equal to the worker-recorded cnf_sha256 only; encode_q0 CNF<->graph6 "
                              "parent rebuild pending (TaskA)"},
           "not_claimed": "Native parent drat-trim replay of retained proofs only. No PA(19,8,6) theorem, M1 or "
                          "gate verdict; streamed routes (b, c5, d, e, cell) are not replayed here."}
    write_new(DESK + "/RESULT.json", json.dumps(out, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({"counts": per, "unresolved": len(unresolved), "logs_bad": len(logs_bad), "dup": len(dup)}))


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd, args, k = sys.argv[1], {}, 2
    while k < len(sys.argv):
        args[sys.argv[k]] = sys.argv[k + 1] if k + 1 < len(sys.argv) else None
        k += 2
    need_lane(args)
    common_start()
    if cmd == "freeze":
        cmd_freeze(args)
    elif cmd == "controls":
        cmd_controls(args)
    elif cmd == "run":
        cmd_run(args)
    elif cmd == "finalize":
        cmd_finalize(args)
    else:
        raise SystemExit("unknown subcommand")


if __name__ == "__main__":
    main()
