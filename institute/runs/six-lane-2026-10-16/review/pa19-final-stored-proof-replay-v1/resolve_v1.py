#!/usr/bin/env python3
"""PA19StoredProofReplay resolve v1: parent native RE-SOLVE + parent drat-trim replay of EXACTLY the 737 chosen M1
records that the bridge census (R/pa19-final-bridge-v1/delivery-exposure-census-v1.json, baf3cee6...) lists without
positive checker-CNF delivery evidence: route b rev5 198, c5 rev5 37, d f01788_r3 1, e ms06_s00150 rev9 batches 500,
e ms09_s00010 batch_04300_04399_r3 1. Old records are only read. No proof or CNF is written anywhere; CNF bytes live
in driver memory and reach each child through an anonymous pipe; the proof flows solver -> pipe -> driver relay
(sha/count) -> pipe -> drat-trim stdin. Not a theorem, gate, M1 or M2 verdict.

Subcommands (outputs created exclusively inside DESK; lane files opened O_RDONLY only):
  plan     --lane L                         -> DESK/resolve-plan-v1.jsonl + resolve-plan-v1.json (metadata only)
  controls --lane L --script-sha X          -> DESK/resolve-controls-v1/ (own in-memory tiny CNFs; RC1-RC4)
  run      --lane L --plan P --plan-sha S --chunk ID --script-sha X [--start I] [--stop J] [--max-seconds N]
  finalize --lane L --plan P --plan-sha S --script-sha X  -> DESK/RESOLVE-RESULT.json
Plan order: M2-open cases first (delivery-exposure-m2-overlap-v1.json 007e417d..., m2 status starting 'OPEN'), then
the other exposed records; inside each group audit (M1-manifest-compact.tsv) case order and audit record order, with
records whose recorded proof exceeds 300 MiB moved to the end of their group.
CNF bytes: direct records (b, c5) = the on-disk pass-1 file cases19skel/cnf/<tag>.cnf read once (sha256 and length
must equal the parent R5 rebuild, pa19-cnf-binding-v1 2a14a1dc..., and the record); split records = pinned lane
encoders (encode_e1/encode_skel/encode_full/encode_partbatch, sha-pinned, executed from verified bytes) on the pinned
spec (R5 spec_sha256) and ext.json (audit split-map sha) with the record's exact index/indices, serialized by
cnf_bytes_of (text-identical to stream_check5/stream_check9, checked at start); sha256/length must equal the record.
Solver argv exactly as recorded (kissat -q -f --seed=1 --time=L CNF PROOF | cadical -q -t L CNF PROOF, CNF=/dev/fd/3,
PROOF=/dev/fd/4); checker = parent drat-trim a46c0c71... with [/dev/fd/3, -i, -t T], T as recorded, proof on stdin.
Executables are invoked through an absolute path that literally contains the lane path (watchdog4 membership).
Measured delivery: each CNF writer thread counts bytes after every write returns and closes its end; the driver
keeps a duplicate read end of each CNF pipe and, after the reading child exited and the writer finished, requires
FIONREAD == 0 (every written byte was consumed by that child; any drained remainder is counted as undelivered).
PASS iff: built CNF sha/len equal the record (and R5 for direct); solver self-exit rc 20, s-lines a subset of
['s UNSATISFIABLE'] (at most one), no other status; solver and checker CNF deliveries complete (len written, writer
closed without error, remainder 0); relay read to EOF, bytes_in == bytes_out > 0, no write error, stdin closed;
checker self-exit rc 0, CR-stripped s-lines exactly ['s VERIFIED'], no fatal marker, exactly one parsing line equal
to the CNF p-line, exactly one 'c reading proof from stdin', exactly one 'c finished parsing, read N bytes from proof
file' with N == relayed bytes; solver/checker sha pre and post equal pins; no guard fired. rc 10 = SAT-CLAIM (chunk
stops). Anything else UNKNOWN. No retries: an index with any receipt line is never run again.
Guards: one existing lane token per record (read-only flock, bounded wait) held from build to post-hash; records with
recorded proof > 300 MiB additionally hold the lane bigmem lock (read-only flock, bounded wait); hard wall T + 120 s
from token acquisition; SIGTERM to live children then 30 s bounded wait, quarantine (token held) if a child survives,
no SIGKILL; solver+checker+driver resident < 3.5 GiB (0.2 s samples); free disk >= 12e9 continuously and >= 12334217728
+ 20 MiB at admission; raw logs <= 2 MiB per child per record; desk allocation <= 20e6 B; chunk <= 10800 s; nothing
admitted that could run past 2026-10-18 18:00 PDT.
"""
import ast
import ctypes
import fcntl
import hashlib
import json
import os
import re
import signal
import struct
import sys
import termios
import threading
import time
import types
import zlib
from datetime import datetime
from zoneinfo import ZoneInfo

A = "/Users/jinleic/repos/aifours"
LANE = A + "/information-science/evidence/six-lane-20261016/packing-array19"
R = A + "/institute/runs/six-lane-2026-10-16/review"
DESK = R + "/pa19-final-stored-proof-replay-v1"
TMP = DESK + "/tmp"
AUDIT = R + "/pa19-final-receipts-v1"
TSV = AUDIT + "/M1-manifest-compact.tsv"
CASES_A2 = AUDIT + "/run-v1/cases-A2.jsonl"
SPLITMAP = AUDIT + "/run-v1/split-index-map.jsonl.gz"
CENSUS = R + "/pa19-final-bridge-v1/delivery-exposure-census-v1.json"
OVERLAP = R + "/pa19-final-bridge-v1/delivery-exposure-m2-overlap-v1.json"
R5 = R + "/pa19-cnf-binding-v1/cnf-binding-result.json"
PINS = {
    TSV: "83cc8df69a876991149ed8cba52bd0f4f8c540c1ed33f7c9dae44007c22bbcd1",
    CASES_A2: "d2471123957ae3ebf0bdcffc1e808efcc945a17262da7786668f4dc80f8a0a28",
    SPLITMAP: "8812e2afc798a9fd32ef1fe383d7c16ea2ad8d39b4a7a3632bdb6bcac9826b53",
    CENSUS: "baf3cee6595b8087fb91af48c24594dfc3ecc97bc06ac5c0342ea320c2f9f674",
    OVERLAP: "007e417dce063ddc7a18bb02becfa87322a72a3dafcb0fcf3b7cbd5bc226cd81",
    R5: "2a14a1dc4eadec733f73ff460814f94ebffa11b81266eb2eaf8c7df7772a22d9",
}
DT = R + "/moqls7-parent-proofcheck-v1/drat-trim"
KISSAT = "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"
CADICAL = "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical"
EXE_SHA = {DT: "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37",
           KISSAT: "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848",
           CADICAL: "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa"}
SRC = LANE + "/src"
ENC_PINS = [("encode_e1", "2a76e8bdc813e92e60de4267bc0538eef0e0849effb692671fb044c14b16b830"),
            ("encode_skel", "dd871522a62191a90ee022758d852b1544f321f3f13b49fef1ebd31818a5cc22"),
            ("encode_full", "33a49879518b167a35332f2220d236b95415160224cbb0f9024ac5da84865863"),
            ("encode_partbatch", "ee4496cc927406ad3f0bff10a00c6c04cb6e34080424e2798bbc2af8c31012e9")]
SERIALIZER_PINS = [("stream_check5", "3060a9c064572b603e23fa82a9981f7d1e9d40a09d223c8f9f354c5ffde0c4ad"),
                   ("stream_check9", "d3bcda4c149bf5b2ae94daa9539edb1a43f80bd113e77aebe93a735fb6aec901")]
N_EXPECTED = 737
TOK = LANE + "/cycle2/tokens"
TZ = ZoneInfo("America/Los_Angeles")
GLOBAL_STOP = datetime(2026, 10, 18, 18, 0, 0, tzinfo=TZ).timestamp()
WALL_MARGIN = 120
GRACE = 30
RSS_CAP = 3584 * 2 ** 20
BIGMEM_BYTES = 300 * 2 ** 20
DISK_GATE = 12334217728 + 20 * 2 ** 20
DISK_FLOOR = 12000000000
LOG_CAP = 2 * 2 ** 20
DESK_CAP = 20000000
DESK_RESERVE = 1500000
RECEIPT_MAX = 65536
CHUNK_MAX = 10800
CKPT_EVERY = 900
TOKEN_WAIT_MAX = 1800
SAMPLE = 0.2
RSS_FAIL_MAX = 10
RE_K = re.compile(r"^/opt/homebrew/bin/kissat -q -f --seed=1 --time=(\d+) CNF PROOF; binary DRAT streamed to "
                  r"drat-trim -i -t (\d+)$")
RE_C = re.compile(r"^/opt/homebrew/bin/cadical -q -t (\d+) CNF PROOF; binary DRAT streamed to drat-trim -i -t (\d+)$")
FATAL = (b"NOT VERIFIED", b"TIMEOUT", b"MEMOUT", b"ERROR", b"error opening", b"illegal literal", b"early EOF",
         b"clauses less than expected", b"wrong binary prefix", b"trivial UNSAT", b"DERIVATION", b"conflict claimed",
         b"failed at proof line", b"did not find p cnf")
RE_PARSING = re.compile(rb"^c parsing input formula with (\d+) variables and (\d+) clauses$")
RE_FINISHED = re.compile(rb"^c finished parsing(?:, read (\d+) bytes from proof file)?$")
RE_PLINE = re.compile(rb"^p cnf (\d+) (\d+)$")
CHILD_ENV = {"TMPDIR": TMP + "/", "PATH": "/usr/bin:/bin", "LC_ALL": "C", "LANG": "C"}
HEX64 = re.compile(r"^[0-9a-f]{64}$")
STATE = {"stop": False, "waiting": False, "signals": []}


def now_iso():
    return datetime.now(TZ).isoformat(timespec="milliseconds")


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(path):
    h, n = hashlib.sha256(), 0
    fd = os.open(path, os.O_RDONLY)
    try:
        while True:
            b = os.read(fd, 1 << 22)
            if not b:
                break
            h.update(b)
            n += len(b)
    finally:
        os.close(fd)
    return h.hexdigest(), n


def read_file(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        st0 = os.fstat(fd)
        parts = []
        while True:
            b = os.read(fd, 1 << 22)
            if not b:
                break
            parts.append(b)
        st1 = os.fstat(fd)
    finally:
        os.close(fd)
    stat = lambda s: [s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns]
    return b"".join(parts), stat(st0), stat(st1)


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
        self.fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
        self.co = zlib.compressobj(9, zlib.DEFLATED, 31)

    def write(self, line):
        write_all(self.fd, self.co.compress(line) + self.co.flush(zlib.Z_SYNC_FLUSH))
        os.fsync(self.fd)

    def close(self):
        write_all(self.fd, self.co.flush(zlib.Z_FINISH))
        os.fsync(self.fd)
        os.close(self.fd)


def gz_lines(path):
    data = zlib.decompressobj(31).decompress(open(path, "rb").read())
    parts = data.split(b"\n")
    return [ln for ln in parts[:-1] if ln.strip()], parts[-1].strip() != b""


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


def own_sha():
    return sha_file(os.path.abspath(__file__))[0]


def interp_pins():
    exe = os.path.realpath(sys.executable)
    out = {"sys_executable": sys.executable, "realpath": exe, "sha256": sha_file(exe)[0], "version": sys.version}
    fw = os.path.join(sys.base_prefix, "Python")
    if os.path.isfile(fw):
        out["framework_lib"] = fw
        out["framework_lib_sha256"] = sha_file(fw)[0]
    return out


def through_lane(p):
    """Absolute path that literally contains the lane path and resolves to p (watchdog4 membership)."""
    q = LANE + "/.." * LANE.count("/") + p
    if os.path.realpath(q) != os.path.realpath(p):
        raise SystemExit("through_lane does not resolve: " + q)
    return q


def high_fd(fd):
    """Move a pipe fd to >= 20 (close-on-exec) so file actions never alias the child targets 0..4."""
    n = fcntl.fcntl(fd, fcntl.F_DUPFD_CLOEXEC, 20)
    os.close(fd)
    return n


def fionread(fd):
    return struct.unpack("i", fcntl.ioctl(fd, termios.FIONREAD, b"\0\0\0\0"))[0]


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


# ---------------------------------------------------------------- signals and lane locks
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


def bounded_flock(path, max_wait, info):
    """Read-only fd + exclusive flock: non-blocking try, then ONE blocking wait bounded by SIGALRM. fd or None."""
    fd = os.open(path, os.O_RDONLY)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return fd
    except BlockingIOError:
        pass
    if max_wait <= 0:
        os.close(fd)
        info["refused"] = "busy and no wait budget: " + os.path.basename(path)
        return None
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
        os.close(fd)
        info["refused"] = "bounded wait ended without lock: " + os.path.basename(path)
        return None
    return fd


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
            fd = bounded_flock(os.path.join(TOK, "t0"), max_wait, info)
            if fd is None:
                info["waited_s"] = round(time.time() - t0, 3)
                return False
            self.fd, self.name = fd, "t0"
        info.update({"name": self.name, "waited_s": round(time.time() - t0, 3), "acquired_at": now_iso()})
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


# ---------------------------------------------------------------- pinned encoders and serializer
def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()


def _fn_src(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n)
    return None


def load_encoders():
    """Executes the sha-pinned lane encoder sources from verified bytes (no import-path lookup); checks that this
    file's cnf_bytes_of is text-identical to the pinned stream_check5/stream_check9 serializers."""
    mods, pins = {}, {}
    saved = {k: sys.modules.get(k) for k, _ in ENC_PINS}
    try:
        for name, want in ENC_PINS:
            b, _, _ = read_file(os.path.join(SRC, name + ".py"))
            if sha_bytes(b) != want:
                raise SystemExit("encoder pin mismatch: " + name)
            m = types.ModuleType(name)
            m.__file__ = os.path.join(SRC, name + ".py")
            sys.modules[name] = m
            exec(compile(b, m.__file__, "exec"), m.__dict__)
            mods[name], pins[name] = m, want
        mine = _fn_src(open(os.path.abspath(__file__), encoding="utf-8").read(), "cnf_bytes_of")
        for name, want in SERIALIZER_PINS:
            b, _, _ = read_file(os.path.join(SRC, name + ".py"))
            if sha_bytes(b) != want:
                raise SystemExit("serializer pin mismatch: " + name)
            if _fn_src(b.decode("utf-8"), "cnf_bytes_of") != mine:
                raise SystemExit("cnf_bytes_of text differs from " + name)
            pins[name] = want
    finally:
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
    if mods["encode_full"].encode_e1 is not mods["encode_e1"] or mods["encode_partbatch"].encode_e1 is not \
            mods["encode_e1"]:
        raise SystemExit("encoders do not share the pinned encode_e1")
    return mods, pins


# ---------------------------------------------------------------- plan (metadata only)
def verify_pins():
    for p, want in PINS.items():
        if sha_file(p)[0] != want:
            raise SystemExit("PIN MISMATCH " + p)
    return dict(PINS)


def cmd_plan(args):
    out_p, out_j = DESK + "/resolve-plan-v1.jsonl", DESK + "/resolve-plan-v1.json"
    t0 = now_iso()
    tok = Token()
    if not tok.acquire(TOKEN_WAIT_MAX):
        raise SystemExit("token refused: %r" % tok.info)
    try:
        pins = verify_pins()
        rows = [ln.rstrip("\n").split("\t") for ln in open(TSV, encoding="utf-8")]
        col = {k: j for j, k in enumerate(rows[0])}
        order = [r[col["tag"]] for r in rows[1:]]
        a2 = {c["tag"]: c for c in (json.loads(ln) for ln in open(CASES_A2, encoding="utf-8"))}
        sm = {s["tag"]: s for s in (json.loads(ln) for ln in zlib.decompress(open(SPLITMAP, "rb").read(),
                                                                              31).decode().splitlines() if ln.strip())}
        cen = json.load(open(CENSUS, encoding="utf-8"))["case_detail"]
        ov = json.load(open(OVERLAP, encoding="utf-8"))["per_case"]
        r5 = {p["tag"]: p for p in json.load(open(R5, encoding="utf-8"))["per_tag"]}
        recs, errors = [], []
        for tag in order:
            if tag not in cen:
                continue
            d = cen[tag]
            m2 = (ov.get(tag) or {}).get("m2")
            if m2 is None:
                errors.append([tag, "no M2 overlap entry"])
            if d["route"] in ("b", "c5"):
                ch = a2[tag]["chosen"]
                if ch["route"] != d["route"] or ch["rev"] != 5:
                    errors.append([tag, "chosen route/rev != census"])
                sel = [[ch["path"], ch["sha256"], None, None, ch["tier"], ch["rev"], ch["solver"], "direct"]]
            else:
                sel = [r for r in sm[tag]["chosen[path,sha256,lo,hi,tier,rev,solver,kind]"] if r[5] in (5, 9)]
                n_idx = sum(r[3] - r[2] + 1 for r in sel)
                if n_idx != d["indices_without_positive_evidence"]:
                    errors.append([tag, "selected indices %d != census %d" % (n_idx, d["indices_without_positive_evidence"])])
            for r in sel:
                path, rsha = r[0], r[1]
                why = []
                b, _, _ = read_file(os.path.join(LANE, path))
                if sha_bytes(b) != rsha:
                    why.append("record sha != audit pin")
                j = json.loads(b)
                if not (j.get("status") == "UNSAT" and j.get("solver_rc") == 20 and j.get("solver_stop") == "self"
                        and j.get("tag") == tag):
                    why.append("record not UNSAT/20/self or tag mismatch")
                m = RE_K.match(j.get("solver", "")) or RE_C.match(j.get("solver", ""))
                solver = "kissat" if RE_K.match(j.get("solver", "")) else ("cadical" if m else None)
                if m is None:
                    why.append("solver string not an exact recorded template")
                lim, chk = (int(m.group(1)), int(m.group(2))) if m else (None, None)
                if solver != r[6]:
                    why.append("solver != audit")
                if not (isinstance(j.get("cnf_sha256"), str) and HEX64.match(j["cnf_sha256"]) and
                        isinstance(j.get("cnf_bytes"), int) and isinstance(j.get("drat_bytes"), int)):
                    why.append("record cnf/drat fields malformed")
                ent = {"tag": tag, "route": d["route"], "record": path, "record_sha256": rsha, "rev": r[5],
                       "solver": solver, "time_limit": lim, "drat_trim_t": chk, "kind": r[7],
                       "expect_cnf_sha256": j.get("cnf_sha256"), "expect_cnf_bytes": j.get("cnf_bytes"),
                       "recorded_drat_sha256": j.get("drat_sha256"), "recorded_drat_bytes": j.get("drat_bytes"),
                       "recorded_solve_s": j.get("solve_seconds"), "recorded_check_s": j.get("check_seconds"),
                       "m2_status": m2, "m2_open": bool(m2 and m2.startswith("OPEN")),
                       "bigmem": (j.get("drat_bytes") or 0) > BIGMEM_BYTES}
                p5 = r5.get(tag) or {}
                if d["route"] in ("b", "c5"):
                    ent.update({"source": "base-file", "cnf_file": "cases19skel/cnf/%s.cnf" % tag,
                                "r5_cnf_sha256": p5.get("cnf_sha256"), "r5_cnf_bytes": p5.get("cnf_bytes"),
                                "expect_header": [p5.get("vars"), p5.get("clauses")]})
                    if p5.get("status") != "PASS" or p5.get("cnf_sha256") != j.get("cnf_sha256") or \
                            p5.get("cnf_bytes") != j.get("cnf_bytes"):
                        why.append("R5 base binding != record")
                    if d["route"] == "b" and j.get("cnf_file") != ent["cnf_file"]:
                        why.append("route-b cnf_file != canonical")
                    if d["route"] == "c5" and not (j.get("mode") == "directk" and j.get("encoder") == "encode_skel.py"
                                                   and j.get("cnf_matches_pass1_sha") is True):
                        why.append("c5 record not directk/encode_skel/pass1-equal")
                else:
                    ext = sm[tag]["ext"]
                    ent.update({"source": "build", "spec": "cases19skel/specs/%s.json" % tag,
                                "spec_sha256": p5.get("spec_sha256"), "ext": ext["path"], "ext_sha256": ext["sha256"],
                                "ext_num_full": ext["num_full"], "expect_header": None})
                    if r[7] == "r3" and d["route"] == "d":
                        idx = j.get("index")
                        if not (j.get("kind") == "a3" and j.get("encoder") == "encode_full.py" and isinstance(idx, int)
                                and r[2] == r[3] == idx):
                            why.append("a3 _r3 record fields")
                        ent.update({"build": "encode_full", "index": idx})
                    else:
                        idxs = j.get("indices")
                        if not (j.get("encoder") == "encode_partbatch.py" and isinstance(idxs, list) and
                                idxs == list(range(r[2], r[3] + 1))):
                            why.append("batch record indices/encoder")
                        if r[7] == "batch_r3":
                            ob, _, _ = read_file(os.path.join(LANE, path.replace("_r3.json", ".json")))
                            ent["original_record_sha256"] = sha_bytes(ob)
                            if json.loads(ob).get("indices") != idxs:
                                why.append("_r3 indices != original record indices")
                        ent.update({"build": "encode_partbatch", "indices_lo": r[2], "indices_hi": r[3]})
                ent["wall_s"] = (chk or 0) + WALL_MARGIN
                ent["plan_state"] = "READY" if not why else "UNKNOWN"
                ent["plan_reasons"] = why
                recs.append(ent)
        if len(recs) != N_EXPECTED or errors:
            raise SystemExit("plan census mismatch: %d records, errors %r" % (len(recs), errors[:5]))
        grp = lambda e: (0 if e["m2_open"] else 1, 1 if e["bigmem"] else 0)
        recs = [e for _, e in sorted(enumerate(recs), key=lambda ie: (grp(ie[1]), ie[0]))]
        for i, e in enumerate(recs):
            e["i"] = i
        body = b"".join(jdump(e) for e in recs)
        write_new(out_p, body)
        cnt = {}
        for e in recs:
            k = "%s|%s|rev%s|%s|%s" % ("M2-open" if e["m2_open"] else "other", e["route"], e["rev"], e["solver"],
                                       "bigmem" if e["bigmem"] else "regular")
            cnt[k] = cnt.get(k, 0) + 1
        summ = {"schema": "pa19-resolve-plan-v1", "started": t0, "finished": now_iso(), "script_sha256": own_sha(),
                "pins_verified": pins, "token": tok.info, "plan": os.path.basename(out_p),
                "plan_sha256": sha_bytes(body), "plan_bytes": len(body), "records": len(recs),
                "m2_open_records": sum(1 for e in recs if e["m2_open"]),
                "m2_open_cases": len({e["tag"] for e in recs if e["m2_open"]}),
                "cases": len({e["tag"] for e in recs}), "counts": cnt,
                "plan_unknown": [[e["i"], e["tag"], e["record"], e["plan_reasons"]] for e in recs
                                 if e["plan_state"] != "READY"],
                "recorded_solve_s": round(sum(e["recorded_solve_s"] or 0 for e in recs), 1),
                "recorded_check_s": round(sum(e["recorded_check_s"] or 0 for e in recs), 1),
                "bigmem_records": [[e["i"], e["tag"], e["recorded_drat_bytes"]] for e in recs if e["bigmem"]]}
        write_new(out_j, json.dumps(summ, indent=1, sort_keys=True).encode() + b"\n")
        print(json.dumps({"records": len(recs), "plan_sha256": summ["plan_sha256"], "counts": cnt}))
    finally:
        tok.release()


# ---------------------------------------------------------------- one re-solve
class Feeder(threading.Thread):
    """Writes all bytes to a pipe write end, counting only after each write returns; then closes it."""

    def __init__(self, fd, data, limit=None):
        super().__init__(daemon=True)
        self.fd, self.data, self.limit = fd, data, limit
        self.written, self.error, self.closed, self.done = 0, None, False, False

    def run(self):
        try:
            mv = memoryview(self.data)[:self.limit if self.limit is not None else len(self.data)]
            while self.written < len(mv):
                n = os.write(self.fd, mv[self.written:self.written + (1 << 16)])
                self.written += n
        except OSError as e:
            self.error = repr(e)
        finally:
            try:
                os.close(self.fd)
                self.closed = True
            except OSError as e:
                self.error = (self.error or "") + " close:" + repr(e)
            self.done = True


class Relay(threading.Thread):
    """Solver proof pipe -> sha/count -> checker stdin pipe; counts bytes_out only after writes return."""

    def __init__(self, rfd, wfd):
        super().__init__(daemon=True)
        self.rfd, self.wfd = rfd, wfd
        self.h, self.bytes_in, self.bytes_out = hashlib.sha256(), 0, 0
        self.eof, self.write_error, self.read_error, self.closed, self.done = False, None, None, False, False

    def run(self):
        try:
            while True:
                try:
                    b = os.read(self.rfd, 1 << 20)
                except OSError as e:
                    self.read_error = repr(e)
                    break
                if not b:
                    self.eof = True
                    break
                self.h.update(b)
                self.bytes_in += len(b)
                if self.write_error is None:
                    try:
                        write_all(self.wfd, b)
                        self.bytes_out += len(b)
                    except OSError as e:
                        self.write_error = repr(e)
        finally:
            try:
                os.close(self.wfd)
                self.closed = True
            except OSError as e:
                self.write_error = (self.write_error or "") + " close:" + repr(e)
            os.close(self.rfd)
            self.done = True


def drain(fd, feeder, deadline):
    """After the reading child exited: read what the feeder still pushes so it can finish; bytes are undelivered."""
    os.set_blocking(fd, False)
    n = 0
    while time.time() < deadline:
        try:
            b = os.read(fd, 1 << 16)
        except BlockingIOError:
            if feeder.done:
                break
            time.sleep(0.01)
            continue
        if not b:
            break
        n += len(b)
    return n


def parse_lines(raw):
    return [ln.replace(b"\r", b"") for ln in raw.split(b"\n")]


def read_range(path, start, end):
    fd = os.open(path, os.O_RDONLY)
    try:
        out = b""
        while len(out) < end - start:
            b = os.pread(fd, end - start - len(out), start + len(out))
            if not b:
                break
            out += b
    finally:
        os.close(fd)
    return out


def spawn(path, argv, actions):
    sigdef = (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGPIPE, signal.SIGXFSZ, signal.SIGALRM)
    return os.posix_spawn(path, argv, CHILD_ENV, file_actions=actions, setsigdef=sigdef, setsigmask=())


def resolve_one(e, cnf, logs, chunk, fault=None):
    """cnf = exact CNF bytes; logs = {'solver': (fd, path), 'checker': (fd, path)}. Returns (receipt, stop)."""
    t0 = time.time()
    deadline = t0 + e["wall_s"]
    rec = {"kind": "final", "schema": "pa19-resolve-receipt-v1", "i": e["i"], "tag": e["tag"], "record": e["record"],
           "chunk": chunk, "t_start": now_iso(), "fault_injection": fault}
    hdr = cnf.split(b"\n", 1)[0]
    m = RE_PLINE.match(hdr)
    vc = [int(m.group(1)), int(m.group(2))] if m else None
    rec["cnf"] = {"sha256": sha_bytes(cnf), "bytes": len(cnf), "pline": vc}
    exe = {"solver": KISSAT if e["solver"] == "kissat" else CADICAL, "checker": DT}
    pre = {k: sha_file(p)[0] for k, p in exe.items()}
    rec["exe_sha256_pre"] = pre
    why = []
    if any(pre[k] != EXE_SHA[exe[k]] for k in exe):
        why.append("executable sha pre != pin")
    if vc is None or (e.get("expect_header") and vc != e["expect_header"]):
        why.append("CNF p-line missing or != expectation")
    if why:
        rec.update({"state": "UNKNOWN", "reasons": ["not run: " + w for w in why], "solver": {"started": False}})
        return rec, ("exe_sha_mismatch" if "executable sha pre != pin" in why else None)
    sx, cx = through_lane(exe["solver"]), through_lane(DT)
    if e["solver"] == "kissat":
        s_argv = [sx, "-q", "-f", "--seed=1", "--time=%d" % e["time_limit"], "/dev/fd/3", "/dev/fd/4"]
    else:
        s_argv = [sx, "-q", "-t", str(e["time_limit"]), "/dev/fd/3", "/dev/fd/4"]
    c_argv = [cx, "/dev/fd/3", "-i", "-t", str(e["drat_trim_t"])]
    rec["solver_argv"], rec["checker_argv"] = s_argv, c_argv
    rec["env"] = CHILD_ENV
    cs_r, cs_w = (high_fd(x) for x in os.pipe())
    cd_r, cd_w = (high_fd(x) for x in os.pipe())
    pf_r, pf_w = (high_fd(x) for x in os.pipe())
    pi_r, pi_w = (high_fd(x) for x in os.pipe())
    cs_keep = fcntl.fcntl(cs_r, fcntl.F_DUPFD_CLOEXEC, 20)
    cd_keep = fcntl.fcntl(cd_r, fcntl.F_DUPFD_CLOEXEC, 20)
    offs = {}
    for k, (fd, path) in logs.items():
        write_all(fd, ("\n### BEGIN %s i=%d tag=%s record=%s chunk=%s t=%s\n" % (
            k, e["i"], e["tag"], e["record"], chunk, now_iso())).encode())
        offs[k] = os.fstat(fd).st_size
    pids, procs = {}, {}
    try:
        pids["checker"] = spawn(cx, c_argv, [(os.POSIX_SPAWN_DUP2, pi_r, 0), (os.POSIX_SPAWN_DUP2, cd_r, 3),
                                             (os.POSIX_SPAWN_DUP2, logs["checker"][0], 1),
                                             (os.POSIX_SPAWN_DUP2, logs["checker"][0], 2)])
        procs["checker"] = {"pid": pids["checker"], "t_spawn": now_iso(), "t0": time.time()}
        pids["solver"] = spawn(sx, s_argv, [(os.POSIX_SPAWN_OPEN, 0, "/dev/null", os.O_RDONLY, 0),
                                            (os.POSIX_SPAWN_DUP2, cs_r, 3), (os.POSIX_SPAWN_DUP2, pf_w, 4),
                                            (os.POSIX_SPAWN_DUP2, logs["solver"][0], 1),
                                            (os.POSIX_SPAWN_DUP2, logs["solver"][0], 2)])
        procs["solver"] = {"pid": pids["solver"], "t_spawn": now_iso(), "t0": time.time()}
    except OSError as ex:
        rec["spawn_error"] = repr(ex)
    for fd in (cs_r, cd_r, pf_w, pi_r):
        os.close(fd)
    fs = Feeder(cs_w, cnf)
    fd_ = Feeder(cd_w, cnf, limit=(len(cnf) // 2 if fault == "truncate_checker_cnf" else None))
    rl = Relay(pf_r, pi_w)
    for t in (fs, fd_, rl):
        t.start()
    status, sig_reason, t_sig, quarantine = {}, None, None, None
    peak, nsamp, consec_fail, nfail, min_free, last_disk = {"solver": 0, "checker": 0, "driver": 0}, 0, 0, 0, None, 0.0
    if "spawn_error" in rec:
        sig_reason, t_sig = "spawn_error", time.time()
        for k, pid in pids.items():
            os.kill(pid, signal.SIGTERM)
    drained = {"solver": 0, "checker": 0}
    remainder = {}
    try:
        while True:
            for k, pid in pids.items():
                if k not in status:
                    w, st, ru = os.wait4(pid, os.WNOHANG)
                    if w == pid:
                        status[k] = (st, ru, time.time())
            for k, keep, fe in (("solver", cs_keep, fs), ("checker", cd_keep, fd_)):
                if k in status and k not in remainder:
                    if not fe.done:
                        drained[k] += drain(keep, fe, time.time() + GRACE)
                    fe.join(GRACE)
                    remainder[k] = fionread(keep) if fe.done else None
            if len(status) == len(pids):
                break
            now = time.time()
            if sig_reason is None:
                reason, tot = None, 0
                for k, pid in pids.items():
                    if k not in status:
                        r = resident(pid)
                        if r is None:
                            nfail += 1
                            consec_fail += 1
                        else:
                            consec_fail = 0
                            nsamp += 1
                            peak[k] = max(peak[k], r)
                            tot += r
                d = resident(os.getpid()) or 0
                peak["driver"] = max(peak["driver"], d)
                tot += d
                if now - last_disk >= 1.0:
                    last_disk = now
                    fr = disk_free()
                    min_free = fr if min_free is None else min(min_free, fr)
                    if fr < DISK_FLOOR:
                        reason = "disk_floor"
                if STATE["stop"]:
                    reason = "driver_signal"
                elif now >= deadline:
                    reason = "wall"
                elif tot > RSS_CAP:
                    reason = "rss"
                elif consec_fail >= RSS_FAIL_MAX:
                    reason = "rss_unmeasurable"
                elif "checker" in status and "solver" in pids and "solver" not in status:
                    reason = "checker_exited_before_solver"
                elif any(os.fstat(logs[k][0]).st_size - offs[k] > LOG_CAP for k in logs):
                    reason = "log_cap"
                if reason is not None:
                    for k, pid in pids.items():
                        if k not in status:
                            os.kill(pid, signal.SIGTERM)
                    sig_reason, t_sig = reason, now
                    rec["sigterm_at"] = now_iso()
            elif now >= t_sig + GRACE:
                quarantine = {"from": now_iso()}
                for k, pid in pids.items():
                    if k not in status:
                        w, st, ru = os.wait4(pid, 0)  # token stays held until exit; no further signal
                        status[k] = (st, ru, time.time())
                quarantine["until"] = now_iso()
                continue
            time.sleep(0.02 if now - t0 < 1.0 else SAMPLE)
    finally:
        if len(status) != len(pids):  # unexpected exception: own SIGTERM, bounded wait, then quarantine-wait
            for k, pid in pids.items():
                if k not in status:
                    try:
                        os.kill(pid, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
            t_x = time.time()
            for k, pid in pids.items():
                while k not in status and time.time() < t_x + GRACE:
                    w, st, ru = os.wait4(pid, os.WNOHANG)
                    if w == pid:
                        status[k] = (st, ru, time.time())
                    else:
                        time.sleep(SAMPLE)
                if k not in status:
                    w, st, ru = os.wait4(pid, 0)
                    status[k] = (st, ru, time.time())
    for t in (fs, fd_, rl):
        t.join(GRACE)
    for k, keep, fe in (("solver", cs_keep, fs), ("checker", cd_keep, fd_)):
        if k not in remainder:
            if not fe.done:
                drained[k] += drain(keep, fe, time.time() + GRACE)
            remainder[k] = fionread(keep) if fe.done else None
        os.close(keep)
    # ---- per-child results and raw logs
    out = {}
    for k in ("solver", "checker"):
        o = {"started": k in pids}
        if k in status:
            st, ru, te = status[k]
            o.update({"pid": pids[k], "t_spawn": procs[k]["t_spawn"], "elapsed_s": round(te - procs[k]["t0"], 3),
                      "wait_status": st, "exited": os.WIFEXITED(st),
                      "rc": os.WEXITSTATUS(st) if os.WIFEXITED(st) else None, "signaled": os.WIFSIGNALED(st),
                      "termsig": os.WTERMSIG(st) if os.WIFSIGNALED(st) else None, "maxrss_bytes": ru.ru_maxrss,
                      "utime_s": round(ru.ru_utime, 3), "stime_s": round(ru.ru_stime, 3),
                      "peak_sampled_rss": peak[k]})
            o["self_exit"] = bool(o["exited"] and sig_reason is None)
        fdl, path = logs[k]
        end = os.fstat(fdl).st_size
        raw = read_range(path, offs[k], end)
        o["log"] = {"file": os.path.basename(path), "offset": offs[k], "bytes": len(raw), "sha256": sha_bytes(raw),
                    "complete": len(raw) == end - offs[k]}
        write_all(fdl, ("\n### END %s i=%d raw_bytes=%d raw_sha256=%s\n" % (k, e["i"], len(raw),
                                                                         sha_bytes(raw))).encode())
        lines = parse_lines(raw)
        o["s_lines"] = [x.decode("utf-8", "replace") for x in lines if x.startswith(b"s ")][:10]
        o["n_s_lines"] = sum(1 for x in lines if x.startswith(b"s "))
        if k == "solver":
            o["n_v_lines"] = sum(1 for x in lines if x.startswith(b"v "))
            o["n_c_lines"] = sum(1 for x in lines if x.startswith(b"c "))
        else:
            fatal = {}
            for x in lines:
                for mk in FATAL:
                    if mk in x:
                        fatal[mk.decode()] = fatal.get(mk.decode(), 0) + 1
            o["fatal_markers"] = fatal
            o["parsing_lines"] = [[int(a.group(1)), int(a.group(2))] for a in (RE_PARSING.match(x) for x in lines)
                                  if a][:5]
            o["finished_read_bytes"] = [int(a.group(1)) if a.group(1) is not None else None
                                        for a in (RE_FINISHED.match(x) for x in lines) if a][:5]
            o["n_stdin_lines"] = sum(1 for x in lines if x == b"c reading proof from stdin")
            o["n_warning_lines"] = sum(1 for x in lines if x.startswith(b"c WARNING"))
        out[k] = o
    rec["solver"], rec["checker"] = out["solver"], out["checker"]
    rec["delivery"] = {k: {"written": f.written, "expected": len(cnf), "error": f.error, "closed": f.closed,
                           "done": f.done, "drained_after_exit": drained[k], "fionread_after_exit": remainder[k]}
                       for k, f in (("solver", fs), ("checker", fd_))}
    rec["relay"] = {"bytes_in": rl.bytes_in, "bytes_out": rl.bytes_out, "sha256": rl.h.hexdigest(), "eof": rl.eof,
                    "read_error": rl.read_error, "write_error": rl.write_error, "closed": rl.closed, "done": rl.done,
                    "equals_recorded_drat_sha256": rl.h.hexdigest() == e["recorded_drat_sha256"],
                    "equals_recorded_drat_bytes": rl.bytes_in == e["recorded_drat_bytes"]}
    post = {k: sha_file(p)[0] for k, p in exe.items()}
    rec["exe_sha256_post"] = post
    rec["guards"] = {"sigterm_reason": sig_reason, "quarantine": quarantine, "rss_samples": nsamp,
                     "rss_sample_failures": nfail, "peak_sampled_driver_rss": peak["driver"],
                     "min_free_bytes_seen": min_free, "wall_s": e["wall_s"]}
    # ---- verdict
    so, co, dl, rl_ = out["solver"], out["checker"], rec["delivery"], rec["relay"]
    if so.get("exited") and so.get("rc") == 10:
        rec["state"], rec["reasons"] = "SAT-CLAIM", ["solver rc 10"]
        return rec, "sat_claim"
    if not (so.get("self_exit") and so.get("rc") == 20):
        why.append("solver not self-exit rc 20")
    if so["n_s_lines"] > 1 or any(x != "s UNSATISFIABLE" for x in so["s_lines"]):
        why.append("solver s-lines not a subset of ['s UNSATISFIABLE']")
    for k in ("solver", "checker"):
        d = dl[k]
        if not (d["written"] == d["expected"] and d["error"] is None and d["closed"] and d["done"] and
                d["drained_after_exit"] == 0 and d["fionread_after_exit"] == 0):
            why.append("%s CNF delivery incomplete" % k)
    if not (rl_["eof"] and rl_["read_error"] is None and rl_["write_error"] is None and rl_["closed"] and
            rl_["bytes_in"] == rl_["bytes_out"] > 0):
        why.append("proof relay incomplete")
    if not (co.get("self_exit") and co.get("rc") == 0):
        why.append("checker not self-exit rc 0")
    if co["s_lines"] != ["s VERIFIED"] or co["n_s_lines"] != 1:
        why.append("checker s-lines != ['s VERIFIED']")
    if co.get("fatal_markers"):
        why.append("checker fatal markers present")
    if co.get("parsing_lines") != [vc]:
        why.append("checker parsing line != CNF p-line")
    if co.get("n_stdin_lines") != 1:
        why.append("checker stdin line count != 1")
    if co.get("finished_read_bytes") != [rl_["bytes_out"]]:
        why.append("checker proof bytes read != relayed bytes")
    if not (so["log"]["complete"] and co["log"]["complete"]):
        why.append("raw log read incomplete")
    if any(post[k] != EXE_SHA[exe[k]] for k in exe):
        why.append("executable sha post != pin")
    if sig_reason is not None or quarantine is not None or STATE["stop"]:
        why.append("guard or stop: %r" % sig_reason)
    if any((out[k].get("maxrss_bytes") or 0) >= RSS_CAP for k in out):
        why.append("child maxrss >= cap")
    rec["state"] = "PASS" if not why else "UNKNOWN"
    rec["reasons"] = why
    rec["t_end"] = now_iso()
    stop = None
    if any(post[k] != EXE_SHA[exe[k]] for k in exe):
        stop = "exe_sha_mismatch"
    if sig_reason in ("disk_floor", "driver_signal", "spawn_error") or quarantine is not None:
        stop = "quarantine" if quarantine is not None else sig_reason
    return rec, stop


# ---------------------------------------------------------------- build the exact CNF bytes of one plan entry
class Builder:
    def __init__(self, mods):
        self.mods, self.cache = mods, {}

    def _json(self, rel, want):
        if rel not in self.cache:
            b, _, _ = read_file(os.path.join(LANE, rel))
            self.cache[rel] = (sha_bytes(b), b)
        got, b = self.cache[rel]
        if got != want:
            raise ValueError("input sha mismatch: " + rel)
        return json.loads(b)

    def build(self, e):
        info = {"source": e["source"]}
        if e["source"] == "base-file":
            b, st0, st1 = read_file(os.path.join(LANE, e["cnf_file"]))
            info.update({"file": e["cnf_file"], "stat_pre": st0, "stat_post": st1})
            if st0 != st1 or sha_bytes(b) != e["r5_cnf_sha256"] or len(b) != e["r5_cnf_bytes"]:
                raise ValueError("base CNF != R5 binding or changed while read")
        else:
            spec = self._json(e["spec"], e["spec_sha256"])
            E = self._json(e["ext"], e["ext_sha256"])
            if E.get("num_full") != e["ext_num_full"] or len(E.get("full", [])) != e["ext_num_full"]:
                raise ValueError("ext num_full mismatch")
            if e["build"] == "encode_full":
                sub = dict(spec)
                sub["placed"] = json.loads(json.dumps(E["full"][e["index"]]))
                F = self.mods["encode_full"].build(sub)[0]
            else:
                pl = [json.loads(json.dumps(E["full"][i])) for i in range(e["indices_lo"], e["indices_hi"] + 1)]
                F = self.mods["encode_partbatch"].build(json.loads(json.dumps(spec)), pl)[0]
            b = cnf_bytes_of(F)
            info.update({"spec": e["spec"], "spec_sha256": e["spec_sha256"], "ext": e["ext"],
                         "ext_sha256": e["ext_sha256"]})
        if sha_bytes(b) != e["expect_cnf_sha256"] or len(b) != e["expect_cnf_bytes"]:
            raise ValueError("built CNF != record cnf_sha256/cnf_bytes")
        return b, info


# ---------------------------------------------------------------- subcommands
def load_done():
    done = {}
    for fn in sorted(os.listdir(DESK)):
        if fn.startswith("resolve-receipts-") and fn.endswith(".jsonl.gz"):
            lines, _ = gz_lines(os.path.join(DESK, fn))
            for ln in lines:
                o = json.loads(ln)
                done.setdefault(o["i"], []).append(o.get("kind"))
    return done


def open_log(path):
    """Exclusive append-only raw log, moved to fd >= 20 so it never aliases a child target fd (0..4)."""
    return high_fd(os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644))


def cmd_run(args):
    chunk = args["--chunk"]
    if not re.match(r"^[0-9a-z-]{1,40}$", chunk):
        raise SystemExit("bad chunk id")
    if own_sha() != args["--script-sha"]:
        raise SystemExit("script sha != --script-sha")
    ppath = args["--plan"]
    if sha_file(ppath)[0] != args["--plan-sha"]:
        raise SystemExit("plan sha mismatch")
    plan = [json.loads(ln) for ln in open(ppath, encoding="utf-8")]
    if len(plan) != N_EXPECTED:
        raise SystemExit("plan length mismatch")
    lockfd = os.open(DESK + "/RUN.lock", os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("another driver holds RUN.lock")
    for p in EXE_SHA:
        through_lane(p)
    mods, enc_pins = load_encoders()
    builder = Builder(mods)
    t0 = time.time()
    chunk_end = min(t0 + min(int(args.get("--max-seconds", CHUNK_MAX)), CHUNK_MAX), GLOBAL_STOP)
    start, stop_i = int(args.get("--start", 0)), int(args.get("--stop", len(plan)))
    done = load_done()
    rpath = DESK + "/resolve-receipts-%s.jsonl.gz" % chunk
    cpath = DESK + "/resolve-checkpoints-%s.jsonl" % chunk
    lpaths = {k: DESK + "/resolve-rawlog-%s-%s.bin" % (k, chunk) for k in ("solver", "checker")}
    rw = GzLines(rpath)
    cfd = os.open(cpath, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_EXCL, 0o644)
    logs = {k: (open_log(p), p) for k, p in lpaths.items()}
    head = {"schema": "pa19-resolve-chunk-v1", "chunk": chunk, "started": now_iso(), "argv": sys.argv,
            "pid": os.getpid(), "script_sha256": args["--script-sha"], "plan_sha256": args["--plan-sha"],
            "interpreter": interp_pins(), "exe_sha256": {p: sha_file(p)[0] for p in EXE_SHA},
            "encoder_pins": enc_pins, "start": start, "stop": stop_i, "chunk_end_epoch": chunk_end,
            "already_receipted": len(done), "free_bytes_start": disk_free(), "desk_alloc_start": desk_alloc()}
    counts = {"PASS": 0, "UNKNOWN": 0, "SAT-CLAIM": 0}
    stop_reason, n_done, tok_wait, ran = None, 0, 0.0, []
    if any(head["exe_sha256"][p] != EXE_SHA[p] for p in EXE_SHA):
        stop_reason = "exe_sha_mismatch_at_start"

    def ckpt(final=False):
        write_all(cfd, jdump({"t": now_iso(), "chunk": chunk, "final": final, "counts": counts, "records": n_done,
                              "last_index": ran[-1] if ran else None, "free_bytes": disk_free(),
                              "desk_alloc": desk_alloc(), "token_wait_s": round(tok_wait, 1)}))
        os.fsync(cfd)

    ckpt()
    last_ck = time.time()
    try:
        for e in plan[start:stop_i]:
            if stop_reason:
                break
            if e["i"] in done:
                continue
            now = time.time()
            if STATE["stop"]:
                stop_reason = "driver_signal"
                break
            if os.path.exists(DESK + "/STOP-RESOLVE"):
                stop_reason = "desk STOP-RESOLVE file"
                break
            if now + e["wall_s"] + GRACE > chunk_end:
                stop_reason = "time_window (next wall %d s)" % e["wall_s"]
                break
            fr = disk_free()
            if fr < DISK_GATE:
                stop_reason = "disk_gate free=%d" % fr
                break
            da = desk_alloc()
            if da + 2 * LOG_CAP + RECEIPT_MAX > DESK_CAP - DESK_RESERVE:
                stop_reason = "desk_cap alloc=%d" % da
                break
            if e["plan_state"] != "READY":
                rw.write(jdump({"kind": "final", "schema": "pa19-resolve-receipt-v1", "i": e["i"], "tag": e["tag"],
                                "record": e["record"], "chunk": chunk, "state": "UNKNOWN",
                                "reasons": ["plan: " + r for r in e["plan_reasons"]], "solver": {"started": False}}))
                counts["UNKNOWN"] += 1
                n_done += 1
                ran.append(e["i"])
                continue
            tok = Token()
            if not tok.acquire(min(TOKEN_WAIT_MAX, chunk_end - now - e["wall_s"] - GRACE)):
                tok_wait += tok.info.get("waited_s", 0) or 0
                stop_reason = "token: " + tok.info.get("refused", "?")
                head.setdefault("token_refusals", []).append(tok.info)
                break
            tok_wait += tok.info["waited_s"]
            big, big_info = None, {}
            try:
                if e["bigmem"]:
                    big = bounded_flock(os.path.join(TOK, "bigmem"),
                                        min(TOKEN_WAIT_MAX, chunk_end - time.time() - e["wall_s"] - GRACE), big_info)
                    if big is None:
                        stop_reason = "bigmem: " + big_info.get("refused", "?")
                        break
                rw.write(jdump({"kind": "intent", "i": e["i"], "tag": e["tag"], "record": e["record"],
                                "chunk": chunk, "t": now_iso(), "token": tok.name, "bigmem": e["bigmem"]}))
                try:
                    cnf, binfo = builder.build(e)
                except (ValueError, OSError, KeyError, IndexError) as ex:
                    rec, cstop = {"kind": "final", "schema": "pa19-resolve-receipt-v1", "i": e["i"], "tag": e["tag"],
                                  "record": e["record"], "chunk": chunk, "state": "UNKNOWN",
                                  "reasons": ["not run: CNF build/binding failed: %r" % ex],
                                  "solver": {"started": False}}, None
                else:
                    rec, cstop = resolve_one(e, cnf, logs, chunk)
                    rec["build"] = binfo
            finally:
                if big is not None:
                    fcntl.flock(big, fcntl.LOCK_UN)
                    os.close(big)
                    big_info["released_at"] = now_iso()
                tok.release()
            rec["token"] = tok.info
            rec["bigmem_lock"] = big_info if e["bigmem"] else None
            rw.write(jdump(rec))
            counts[rec["state"]] += 1
            n_done += 1
            ran.append(e["i"])
            if cstop:
                stop_reason = "record_stop: " + cstop
            if time.time() - last_ck >= CKPT_EVERY:
                ckpt()
                last_ck = time.time()
        else:
            stop_reason = stop_reason or "range_exhausted"
    finally:
        ckpt(final=True)
        rw.close()
        os.close(cfd)
        for fd, _ in logs.values():
            os.close(fd)
        head.update({"finished": now_iso(), "stop_reason": stop_reason, "counts": counts, "records_this_chunk": n_done,
                     "first_index": ran[0] if ran else None, "last_index": ran[-1] if ran else None,
                     "token_wait_s": round(tok_wait, 1), "signals": STATE["signals"], "free_bytes_end": disk_free(),
                     "desk_alloc_end": desk_alloc(), "receipts_sha256": sha_file(rpath)[0],
                     "checkpoints_sha256": sha_file(cpath)[0],
                     "rawlog_sha256": {k: sha_file(p)[0] for k, p in lpaths.items()},
                     "exe_sha256_end": {p: sha_file(p)[0] for p in EXE_SHA}})
        write_new(DESK + "/resolve-chunk-%s.json" % chunk, json.dumps(head, indent=1, sort_keys=True).encode() + b"\n")
        fcntl.flock(lockfd, fcntl.LOCK_UN)
        os.close(lockfd)
        print(json.dumps({"chunk": chunk, "stop_reason": stop_reason, "counts": counts, "records": n_done}))


def cmd_controls(args):
    """RC1 kissat tiny UNSAT -> PASS; RC2 kissat tiny SAT -> SAT-CLAIM; RC3 kissat tiny UNSAT with the checker's CNF
    truncated to half by the driver (fault injection of the F-A hazard) -> not PASS, 'checker CNF delivery incomplete'
    among the reasons; RC4 cadical tiny UNSAT -> PASS. Same resolve_one code path as production."""
    if own_sha() != args["--script-sha"]:
        raise SystemExit("script sha != --script-sha")
    out = DESK + "/resolve-controls-v1"
    os.mkdir(out)
    unsat = b"p cnf 3 8\n1 2 3 0\n1 2 -3 0\n1 -2 3 0\n1 -2 -3 0\n-1 2 3 0\n-1 2 -3 0\n-1 -2 3 0\n-1 -2 -3 0\n"
    sat = b"p cnf 2 2\n1 2 0\n-1 2 0\n"
    base = {"recorded_drat_sha256": None, "recorded_drat_bytes": None, "wall_s": 1320, "drat_trim_t": 1200,
            "time_limit": 600, "record": "control"}
    ctl = [dict(base, i=-1, tag="RC1-kissat-tiny-unsat", solver="kissat", cnf=unsat, expect_header=[3, 8],
                fault=None, expected_state="PASS", must_reason=None),
           dict(base, i=-2, tag="RC2-kissat-tiny-sat", solver="kissat", cnf=sat, expect_header=[2, 2],
                fault=None, expected_state="SAT-CLAIM", must_reason=None),
           dict(base, i=-3, tag="RC3-kissat-unsat-checker-cnf-truncated", solver="kissat", cnf=unsat,
                expect_header=[3, 8], fault="truncate_checker_cnf", expected_state="UNKNOWN",
                must_reason="checker CNF delivery incomplete"),
           dict(base, i=-4, tag="RC4-cadical-tiny-unsat", solver="cadical", cnf=unsat, expect_header=[3, 8],
                fault=None, expected_state="PASS", must_reason=None)]
    lpaths = {k: out + "/rawlog-%s.bin" % k for k in ("solver", "checker")}
    logs = {k: (open_log(p), p) for k, p in lpaths.items()}
    rw = GzLines(out + "/receipts.jsonl.gz")
    res = {"schema": "pa19-resolve-controls-v1", "started": now_iso(), "argv": sys.argv, "script_sha256": own_sha(),
           "interpreter": interp_pins(), "exe_sha256": {p: sha_file(p)[0] for p in EXE_SHA},
           "control_cnfs": {"unsat": {"sha256": sha_bytes(unsat), "text": unsat.decode()},
                            "sat": {"sha256": sha_bytes(sat), "text": sat.decode()}}, "controls": []}
    try:
        for c in ctl:
            tok = Token()
            if not tok.acquire(TOKEN_WAIT_MAX):
                res["controls"].append({"tag": c["tag"], "ok": False, "error": "token: %r" % tok.info})
                continue
            try:
                rec, _ = resolve_one(c, c["cnf"], logs, "controls", fault=c["fault"])
            finally:
                tok.release()
            rec["token"] = tok.info
            rw.write(jdump(rec))
            ok = rec["state"] == c["expected_state"] and rec["solver"].get("started") is True
            if c["must_reason"]:
                ok = ok and any(c["must_reason"] in r for r in rec["reasons"])
            res["controls"].append({"tag": c["tag"], "expected_state": c["expected_state"], "state": rec["state"],
                                    "reasons": rec["reasons"], "solver_rc": rec["solver"].get("rc"),
                                    "solver_s_lines": rec["solver"].get("s_lines"),
                                    "checker_rc": rec["checker"].get("rc"),
                                    "checker_s_lines": rec["checker"].get("s_lines"),
                                    "checker_fatal": rec["checker"].get("fatal_markers"),
                                    "delivery": rec.get("delivery"), "relay_bytes": rec["relay"]["bytes_out"],
                                    "ok": ok})
    finally:
        rw.close()
        for fd, _ in logs.values():
            os.close(fd)
    res["all_ok"] = len(res["controls"]) == 4 and all(x["ok"] for x in res["controls"])
    res["finished"] = now_iso()
    res["receipts_sha256"] = sha_file(out + "/receipts.jsonl.gz")[0]
    res["rawlog_sha256"] = {k: sha_file(p)[0] for k, p in lpaths.items()}
    write_new(out + "/RESULT-controls.json", json.dumps(res, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({"all_ok": res["all_ok"], "controls": [[x["tag"], x.get("state"), x["ok"]]
                                                             for x in res["controls"]]}))


def cmd_finalize(args):
    if own_sha() != args["--script-sha"]:
        raise SystemExit("script sha != --script-sha")
    ppath = args["--plan"]
    if sha_file(ppath)[0] != args["--plan-sha"]:
        raise SystemExit("plan sha mismatch")
    plan = [json.loads(ln) for ln in open(ppath, encoding="utf-8")]
    finals, intents, dup, files, partial = {}, set(), [], {}, []
    for fn in sorted(os.listdir(DESK)):
        if fn.startswith("resolve-receipts-") and fn.endswith(".jsonl.gz"):
            files[fn] = sha_file(os.path.join(DESK, fn))[0]
            lines, part = gz_lines(os.path.join(DESK, fn))
            if part:
                partial.append(fn)
            for ln in lines:
                o = json.loads(ln)
                if o.get("kind") == "intent":
                    intents.add(o["i"])
                else:
                    if o["i"] in finals:
                        dup.append(o["i"])
                    finals[o["i"]] = o
    bad_logs, cache = [], {}
    for i, o in finals.items():
        for k in ("solver", "checker"):
            lg = (o.get(k) or {}).get("log")
            if lg:
                p = os.path.join(DESK, lg["file"])
                if p not in cache:
                    cache[p] = open(p, "rb").read()
                if sha_bytes(cache[p][lg["offset"]:lg["offset"] + lg["bytes"]]) != lg["sha256"]:
                    bad_logs.append([i, k])
    bad_i = {i for i, _ in bad_logs}
    per, unresolved, same_proof = {}, [], 0
    for e in plan:
        g = "M2-open" if e["m2_open"] else "other"
        o = finals.get(e["i"])
        if o is None:
            st = "UNKNOWN" if e["i"] in intents else "NOT_ATTEMPTED"
            why = ["intent without final receipt"] if e["i"] in intents else ["not attempted"]
        else:
            st, why = o["state"], o.get("reasons", [])
            if st == "PASS" and (o["record"] != e["record"] or o["tag"] != e["tag"] or e["i"] in bad_i or
                                 e["i"] in dup or o.get("cnf", {}).get("sha256") != e["expect_cnf_sha256"]):
                st, why = "UNKNOWN", ["finalize: identity/duplicate/log-hash mismatch"]
            if st == "PASS" and o["relay"].get("equals_recorded_drat_sha256"):
                same_proof += 1
        per.setdefault(g, {}).setdefault(st, 0)
        per[g][st] += 1
        if st != "PASS":
            unresolved.append({"i": e["i"], "tag": e["tag"], "record": e["record"], "group": g, "state": st,
                               "reasons": why})
    pass_tags = {}
    for e in plan:
        o = finals.get(e["i"])
        pass_tags.setdefault(e["tag"], []).append(bool(o and o["state"] == "PASS" and
                                                       not any(u["i"] == e["i"] for u in unresolved)))
    out = {"schema": "pa19-resolve-result-v1", "recorded": now_iso(), "script_sha256": own_sha(),
           "plan_sha256": args["--plan-sha"], "records": len(plan), "counts": per,
           "cases_all_records_pass": sorted(t for t, v in pass_tags.items() if all(v)),
           "cases_not_all_pass": sorted(t for t, v in pass_tags.items() if not all(v)),
           "proof_sha_equal_to_recorded_among_pass": same_proof, "unresolved": unresolved,
           "duplicate_final_receipts": dup, "raw_log_hash_mismatch": bad_logs, "receipt_files": files,
           "receipt_files_with_partial_tail": partial,
           "not_claimed": "Re-solve + parent drat-trim replay of exposed chosen records only; formula binding of split "
                          "leaves stays with the formula desk; no M1/M2/PA(19,8,6) verdict."}
    write_new(DESK + "/RESOLVE-RESULT.json", json.dumps(out, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({"counts": per, "unresolved": len(unresolved)}))


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd, args, k = sys.argv[1], {}, 2
    while k < len(sys.argv):
        args[sys.argv[k]] = sys.argv[k + 1] if k + 1 < len(sys.argv) else None
        k += 2
    if args.get("--lane") != LANE:
        raise SystemExit("--lane must be " + LANE)
    os.nice(10)
    os.chdir(TMP)
    os.environ["TMPDIR"] = TMP + "/"
    install_signals()
    {"plan": cmd_plan, "controls": cmd_controls, "run": cmd_run, "finalize": cmd_finalize}[cmd](args)


if __name__ == "__main__":
    main()
