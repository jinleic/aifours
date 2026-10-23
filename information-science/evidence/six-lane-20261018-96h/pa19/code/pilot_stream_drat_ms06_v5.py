#!/usr/bin/env python3
"""PA19 96h P-STREAM v5, ms06; CONTROLS-ONLY reviewed-source successor of immutable pilot_stream_drat_ms06_v4.py (fe9ccadb...).
Combined guards G1-G9 and integration A1-A11 fixes. ITEMS=[] and PHASE='controls-only': run_plan RETURNS
before reading/executing encoder bytes or visiting any item. Science requires a distinct reviewed item pin and exact GO.
One single parent allocator; exact full reservation; NEW parent post-exit release dispositions for every prior attempt.
Uncertain ownership/census/publication/resource state -> retain parent block and return (never wait without bound).
WNOWAIT observations preserve the leader anchor; only owned waitpid consumes a real status; ECHILD is never rc0.
At most one verified group SIGTERM, bounded grace, no escalation or uncertain signalling. All cleanup stages share
one deadline. Every creation is inventoried; no existing evidence is edited, moved, removed or silently truncated.
Native executable pins/identities are bound at each launch and settlement under the parent's exclusive-writer premise;
this is not atomic fexecve. Verified Python source bytes are compiled/executed directly, not reopened by a loader.
All settlement/item/summary records are PROVISIONAL until completed publication is observed within bounds,
closeout.json binds the summary, and the parent independently observes the matching actual runner exit and raw-audits.
C6 uses unrounded monotonic observations and --time=2. Deferred science uses kissat --time=300; checker bound 600 s.
No source approval here authorizes execution, qualification, science coverage or a PA(19,8,6) verdict.
"""
import ctypes
import errno
import hashlib
import types
import itertools
import json
import math
import os
import re
import select
import signal
import stat
import struct
import subprocess
import sys
import threading
import time
from datetime import datetime

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
KISSAT = ("/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat", "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848")
DRAT_OLD = (OLD + "/tools/drat-trim/drat-trim", "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4")
DRAT = LANE + "/code/vendor/drat-trim"
DRAT_PROV = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/drat-trim",
             "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37")
DRAT_PROV_RECEIPT = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/"
                     "parent-result.json", "200d307dd52ab4d6559ff89d5faa6c3859e256bbd20c6d1fb439d237b9af3bfe")
DRAT_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
CHECKERS = (("A", DRAT, DRAT_OLD[1]), ("B", DRAT_PROV[0], DRAT_PROV[1]))  # S2: sequential, same frozen buffer
DATE = ("/bin/date", "931edbfcbd847f3c1ccb504325a502db313ce20db27634744a7416c3c4b812f0")   # V1: pinned helper
CONTRACT = (RUN + "/contract-v1.json", "55baff0cf1ac1a4b0ab38b0eb1b1fa5a35a47c890f352b79dae4dfea919ffcaa")
LANE_CEILING = 10_737_418_240         # V2: contract resources.per_lane_new_disk_bytes (re-read at prestart)
PILOT_ROOT = LANE + "/evidence/pilot-v1"
CONTROL_DIR = LANE + "/control"            # N8: anchored directory of the SAT-candidate latch
TREE_SUBDIRS = ("children", "cwd", "fifo", "controls")   # N8: created and anchored with the run tree
BUSY_SLOTS = 2                              # N3: contract resources.per_lane_busy_processes (runner + one child)
ALLOCATION_SCHEMA = "PA19-96H-PARENT-ALLOCATION-v2"
KNOWN_SUMMARY_SCHEMAS = {"PA19-96H-PILOT-SUMMARY-v14", "PA19-96H-PSTREAM-SUMMARY-v4",
                         "PA19-96H-PILOT-SUMMARY-v32", "PA19-96H-PSTREAM-SUMMARY-v5", "PA19-96H-PILOT-SUMMARY-v33"}
DISPOSITION_SCHEMA = "PA19-96H-PARENT-RELEASE-v2"
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
REGISTRY = (LANE + "/evidence/inherited-stop-registry-v1.json", "ee370929f20ffe514e71bce6961e31ed32faaf243e0433d9268179956a0e9873")
LAUNCH_CONTRACT = (RUN + "/control/launch-contract-tightening-v1.json", "8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20")
BINARY_IMPORTS = (LANE + "/evidence/probes/binary-process-imports-v1.json", "c822c4f07974b3f107c18c91bd910a972aa6ddee025e8087c256917492b7cffc")
KISSAT_SOURCE = (LANE + "/evidence/kissat-source-evidence-v2.json", "d4495a3f0d526604e586b11cbd2b1ed717e2872419e31536848bd2000f51a7a7")
MONITOR = RUN + "/control/resource-observer-live-v3.jsonl"
OBSERVER_SOURCE_SHA = "fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196"
OBSERVER_CWD = RUN
SAMPLE_SCOPE = "metadata only; not scientific checkpoint or launch admission"
OLD_LIVE_MARKERS = {  # inherited registry v1 live cycle2-root markers: must stay byte-identical and complete
    "STOP-m2skel7": "06359a697a2029fc599f176944f8ec11d5403739e9a12e96e8a098edca561974",
    "STOP-m2skel8": "294e4946af9b8d84d556aeef37eed717aa69c5502f016f1c609a34374c7b5b86",
    "STOP-m2skel9": "52c9581db260d317bf0fbfe440fbb8acc9e54fd0f46a55ce63be80196c8a0152",
    "STOP-m2partbatch5": "117fc85ffa66c20f31271cfde01fa82bcbae18f12599752bb7057ea8deea750c",
    "STOP-hard10": "300493c629141543b71db391f98f8d2098618d1cee57c84d68be106874411287",
    "STOP-m2r10": "300493c629141543b71db391f98f8d2098618d1cee57c84d68be106874411287",
    "STOP-hard12": "94b56f04b59849923b41db6929760de00a33c12f077983faa2670a2080015bb2",
    "STOP-m2r12": "94b56f04b59849923b41db6929760de00a33c12f077983faa2670a2080015bb2",
    "STOP-K1": "b05f12b9587bb89a8b30d3d040074e1958463109d866bddeb96527d79c9716bf",
}
FAMILY = "ms06"                       # V12: item shape family of this runner
P0 = [4, 3, 3, 3, 3, 3]
ITEMS = []  # Separate science pin + exact GO required after controls qualification
SOLVER_SECONDS = 300
CHECK_SECONDS = 600                   # per checker, two per item (measured max 0.598 s per proof MB)
GRACE = 60
TERM_WAIT = 60
STREAM_JOIN = 60
SINK_UNBLOCK = 10
SETTLE_TAIL = TERM_WAIT + STREAM_JOIN + SINK_UNBLOCK + STREAM_JOIN + 30   # 220 s serial settlement bound
PROOF_CAP = 629_145_600              # HARD: the RAM buffer never retains more than this (never written to disk)
CONTROL_PROOF_CAP = 8 * 1024 * 1024  # HARD RAM cap for control proofs
LOG_CAP = 16 * 1024 * 1024           # HARD per captured stdout+stderr stream
RECORD_MAX = 512 * 1024              # HARD per exact retained JSON record; never truncate evidence
STR_MAX = 1000
ITEM_RECORDS = 3 * 5 + 3 * 3 + 2
CONTROL_RECORDS = 14 * 5 + 2
RUN_RECORDS = 3 + 2 * 3 + 1  # launch,summary,closeout + helper intent/launch/quarantine + spare
CNF_ITEM_MAX = max((it["cnf"][1] for it in ITEMS), default=0)
ITEM_RESERVE = CNF_ITEM_MAX + (1 + len(CHECKERS)) * LOG_CAP + ITEM_RECORDS * RECORD_MAX  # S1: no proof bytes on disk
CONTROL_CHILDREN = 14                 # C1 kissat+A+B, C2 A+B, C3 A+B, C4 A+B, C5 kissat, C6 kissat, C7 kissat, C7b A+B
CONTROL_CNF_ALLOW = 1024 * 1024       # six PHP CNFs, each < 64 KiB
CONTROL_RESERVE = CONTROL_CHILDREN * LOG_CAP + CONTROL_CNF_ALLOW + CONTROL_RECORDS * RECORD_MAX  # S1: RAM proofs only
RUN_RESERVE = RUN_RECORDS * RECORD_MAX
FREE_FLOOR = 12_000_000_000
FRESH_BASE = 12_200_000_000
LANE_RSS_TRIP = 6 * 1024 ** 3
CONTROL_CHILD_WALL = 60
CONTROLS_WORST_SECONDS = CONTROL_CHILDREN * (CONTROL_CHILD_WALL + GRACE + SETTLE_TAIL + 30)
HELPER_WALL = 5                       # V1: /bin/date helper bounded wait
HELPER_TERM_WAIT = 10                 # V1: bounded wait after the helper's single SIGTERM
HELPER_ALLOW = HELPER_WALL + HELPER_TERM_WAIT + 5   # V1/V3: per helper call in the timing model
HELPERS_PER_ITEM = 3                  # item start, item end, SAT candidate
HELPERS_PER_RUN = 2                   # launch record, closeout
HELPER_OUT_CAP = 4096
SUPERVISE_SLICE = 0.05                # N4/N10: poll slice of supervision, reaping and helpers
META_MAX = 64 * 1024 * 1024           # N7: bound of a whole-file metadata read (GO, pinned inputs, records)
MONITOR_MAX = 32 * 1024 * 1024        # N7: bound of the monitor read
SHA_FILE_MAX = 1 << 30                # N7: bound of a streamed hash
CONTROL_TIMER_S = 2                   # N10: kissat --time of C6
C6_MIN_RUN_S = 1.5                    # N10: required monotonic runtime lower bound of C6
C6_MAX_RUN_S = 5.0                    # N10: allowed monotonic runtime upper bound of C6
SETTLE_ALL_ATTEMPTS = 1               # B1: settle() attempts per child in the bounded settle_all pass
ITEM_WORST_SECONDS = (30 + (SOLVER_SECONDS + GRACE + SETTLE_TAIL) + 30
                      + len(CHECKERS) * (CHECK_SECONDS + GRACE + SETTLE_TAIL + 30) + HELPERS_PER_ITEM * HELPER_ALLOW)
RUN_HELPER_SECONDS = HELPERS_PER_RUN * HELPER_ALLOW
MAX_CHUNK = 10800
SETTLE = 120
MARGIN = 60
OWNED_SETTLED_BY = datetime.fromisoformat("2026-10-22T21:56:33-07:00").timestamp()
CHILD_ENV = dict(os.environ, TMPDIR=LANE + "/tmp", PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1",
                 OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
EXIT_PLAN_COMPLETE = 0      # every planned item has a terminal record (UNSAT or UNKNOWN); NOT a science verdict
EXIT_SAT_CANDIDATE = 10
EXIT_CONTROLS_FAILED = 20
EXIT_ADMISSION_REFUSED = 30
EXIT_CANCELLED = 40
EXIT_SAFETY_STOP = 50
EXIT_EXCEPTION = 60
EXIT_PRESTART_REFUSED = 70
EXIT_CODES = (0, 10, 20, 30, 40, 50, 60, 70)
NONLATCHING_TRIPS = {"proof_cap", "owner_cancel_sigterm"}
RESOURCE_DIAG = re.compile(r"(?i)(memout|memory allocation error|out of memory|out-of-memory|failed to reallocate|reallocation failed)")
FEED_BLOCK = 1 << 20                  # S1: RAM block size and collector read size
WRITE_SLICE = 1 << 16                 # S2: feeder os.write slice
HOLD_SECONDS = 30                     # S6: a C7b held feed waits at most this long for the checker reap
SUFFIX = b"x"                         # S6: C3 trailing byte appended in transit
STDIN_LINE = "c reading proof from stdin"
DUP_LINE = re.compile(rb"\rc WARNING: detected and deleted duplicate literal (-?[1-9][0-9]*) at position ([1-9][0-9]*) "
                      rb"of proof line ([1-9][0-9]*)\n")
PARSE_LINE = re.compile(rb"\rc parsing input formula with ([0-9]+) variables and ([0-9]+) clauses\n")
PENDING_MAX = 1 << 16                 # S3: no duplicate-literal line is this long; longer pending bytes are kept
DATE_ARGV = [DATE[0], "+%Y-%m-%dT%H:%M:%S%z"]
DATE_RE = re.compile(rb"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{4}\n")
LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)   # V1: in-process process metadata (no /bin/ps)
LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_pidinfo.restype = ctypes.c_int
LIBPROC.proc_listpids.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_listpids.restype = ctypes.c_int
PROC_ALL_PIDS, PROC_PGRP_ONLY, PROC_PPID_ONLY = 1, 2, 6
PROC_PIDTBSDINFO, BSD_SIZE = 3, 136   # sys/proc_info.h struct proc_bsdinfo
PROC_PIDTASKINFO, TASK_SIZE = 4, 96   # sys/proc_info.h struct proc_taskinfo
SZOMB = 5
LIST_SLOTS = 4096


KNOWN_CLOSEOUT_SCHEMAS = {"PA19-96H-PSTREAM-CLOSEOUT-v5", "PA19-96H-PILOT-CLOSEOUT-v33"}
PHASE = "controls-only"
LAUNCH_SCHEMA = "PA19-96H-PSTREAM-LAUNCH-v5"
SUMMARY_SCHEMA = "PA19-96H-PSTREAM-SUMMARY-v5"
CLOSEOUT_SCHEMA = "PA19-96H-PSTREAM-CLOSEOUT-v5"
KNOWN_LAUNCH_SCHEMAS = {"PA19-96H-PILOT-LAUNCH-v14", "PA19-96H-PSTREAM-LAUNCH-v4", "PA19-96H-PILOT-LAUNCH-v32",
                        "PA19-96H-PSTREAM-LAUNCH-v5", "PA19-96H-PILOT-LAUNCH-v33"}
TREE_ENTRY_MAX, TREE_DEPTH_MAX, CENSUS_SECONDS, SHA_SECONDS = 50000, 24, 30.0, 30.0
ALL_PID_SLOTS = 65536
NATIVE_LAUNCH_STOP = datetime.fromisoformat("2026-10-22T20:56:33-07:00").timestamp()
SCIENCE_STOP = datetime.fromisoformat("2026-10-22T21:26:33-07:00").timestamp()
CREATED = {}          # all complete, partial, failed creations and acquisition identities
LIVE_SINKS = []       # file collectors, including inspectable partially constructed objects

ORDER = itertools.count(1)
LATCH = []          # persistent safety/unsettled reasons; non-empty refuses every later child
OWNED = []          # every Child (pre-allocated before Popen), for the computed settlement summary
LIVE_BUFFERS = []   # S5: every ProofBuffer; the unreleased ones are charged to the lane RSS trip
LIVE_FEEDERS = []   # V5: every Feeder; a feeder still holding its tuple is charged too
HELPERS = []        # V1: every metadata Helper (pre-allocated before Popen)
HELPER_LOG = []     # V1: bounded helper records for the summary
TREE = {}           # N8: anchored directories: path -> (fd, dev, ino)
WRITTEN = {}        # N8: runner-written retained files: path -> (sha256, bytes), re-verified at closeout
KILLPG = os.killpg  # N1: the only signalling primitive (one verified group SIGTERM)
STATE = {"seq": 0, "out": None, "abs_end": None, "chunk_end": None, "remaining_reserve": 0,
         "cancel_order": None, "run_record": None, "go": None, "runner_sha": None, "mono0": None, "mono_end": None,
         "mono_chunk_end": None, "written": 0, "output_limit": None, "last_ledger": None, "reservation": 0,
         "pilot_entries": None, "runner_identity": None, "prior_census": {}, "cleanup_deadline": None}


def on_term(signum, frame):
    """r3#2: lock-free; only stamps a scalar order once."""
    if STATE["cancel_order"] is None:
        STATE["cancel_order"] = next(ORDER)


def cancelled():
    return STATE["cancel_order"] is not None


def latch(reason):
    LATCH.append(str(reason)[:STR_MAX])


def clock():
    """A4: missing required clock is nonqualification, never silently replaced by a second helper."""
    try:
        return Helper(DATE_ARGV).run()
    except HelperRefused as exc:
        HELPER_LOG.append({"refused": str(exc)})
        if not cancelled() and not LATCH:
            latch("required host clock unavailable: " + str(exc))
        return None
    except BaseException as exc:
        latch("required host clock failed %r" % (exc,))
        return None


def serialize(obj):
    """G1/G3: never truncate ownership or publication evidence. Oversize records fail closed."""
    data = json.dumps(obj, indent=1, sort_keys=True, allow_nan=False).encode()
    if len(data) > RECORD_MAX:
        raise RuntimeError("record exceeds RECORD_MAX (%d bytes); complete evidence not published" % len(data))
    return data


def charge_output(n):
    """V2: hard output guard.  Every retained write is counted against this run's total reservation before it is
    made; capture files are pre-charged at LOG_CAP each when their child is prepared; N5: item commits too."""
    if STATE["output_limit"] is not None and STATE["written"] + n > STATE["output_limit"]:
        latch("output guard: %d + %d > %d" % (STATE["written"], n, STATE["output_limit"]))
        raise RuntimeError("output guard: retained bytes would exceed the run reservation")
    STATE["written"] += n


def write_all(fd, data):
    view = memoryview(data)
    while view:
        k = os.write(fd, view)
        if not isinstance(k, int) or k <= 0 or k > len(view):
            raise OSError(errno.EIO, "write made no valid forward progress")
        view = view[k:]


def register_written(path, digest, n):
    """G7: successful retained publication, including previously inventoried partial creations."""
    WRITTEN[path] = (digest, n)
    if path in CREATED:
        CREATED[path].update(state="complete", sha256=digest, bytes=n)


def write_x(path, obj):
    return write_bytes_x(path, serialize(obj))[0]


def write_bytes_x(path, data):
    """Publication completes only after write, file fsync, close AND anchored parent fsync return."""
    charge_output(len(data))
    fd = create_excl(path)
    try:
        try:
            write_all(fd, data)
            os.fsync(fd)
        finally:
            os.close(fd)
        os.fsync(tree_path(path)[0])
    except BaseException as exc:
        CREATED[path].update(state="failed", error=repr(exc))
        raise
    h = hashlib.sha256(data).hexdigest()
    register_written(path, h, len(data))
    return h, len(data)


def open_regular(path, dir_fd=None):
    """N7/N8: open an existing REGULAR file read-only without following a final symlink and without blocking on a
    FIFO (O_NONBLOCK; the fstat check refuses every non-regular kind); returns (fd, fstat)."""
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC, dir_fd=dir_fd)
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode):
            raise RuntimeError("not a regular file: %s" % path)
    except BaseException:
        os.close(fd)
        raise
    return fd, st


def read_regular_bounded(path, limit, dir_fd=None):
    """N7: whole-file read of a regular file of at most `limit` bytes; larger files and growth are refused."""
    fd, st = open_regular(path, dir_fd)
    try:
        if st.st_size > limit:
            raise RuntimeError("%s is %d bytes > limit %d" % (path, st.st_size, limit))
        parts, n = [], 0
        while True:
            b = os.read(fd, min(1 << 20, limit + 1 - n))
            if not b:
                break
            parts.append(b)
            n += len(b)
            if n > limit:
                raise RuntimeError("%s grew beyond limit %d" % (path, limit))
        return b"".join(parts)
    finally:
        os.close(fd)


def sha_file(path, limit=SHA_FILE_MAX, dir_fd=None):
    fd, before = open_regular(path, dir_fd)
    end = work_deadline(SHA_SECONDS)
    try:
        h, n = hashlib.sha256(), 0
        while True:
            if time.monotonic() > end:
                raise RuntimeError("hash work deadline exhausted: " + path)
            b = os.read(fd, 1 << 20)
            if not b:
                break
            h.update(b)
            n += len(b)
            if n > limit:
                raise RuntimeError("hash byte limit exceeded: " + path)
        if census_entry(os.fstat(fd)) != census_entry(before):
            raise RuntimeError("file changed while hashing: " + path)
        return h.hexdigest(), n
    finally:
        os.close(fd)


def sha_tree(path, limit=SHA_FILE_MAX):
    """N8: SHA-256 of a run-tree file read through its anchored directory descriptor."""
    dfd, name = tree_path(path)
    return sha_file(name, limit, dfd)


def read_tree(path, limit):
    """N8: bounded read of a run-tree file through its anchored directory descriptor."""
    dfd, name = tree_path(path)
    return read_regular_bounded(name, limit, dfd)


def read_pinned(path, expect, limit=META_MAX):
    """Pinned input read: bounded regular-file read (N7) whose SHA-256 must equal `expect`."""
    raw = read_regular_bounded(path, limit)
    got = hashlib.sha256(raw).hexdigest()
    if got != expect:
        raise RuntimeError(f"pin mismatch {path}: {got} != {expect}")
    return raw


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def _pidinfo(pid, flavor, size):
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    n = LIBPROC.proc_pidinfo(pid, flavor, 0, buf, size)
    return n, ctypes.get_errno(), buf.raw


def parse_pid_buffer(values, nbytes, allow_kernel_zero=False):
    """Validate exact returned c_int entries. PID 0 is a real kernproc member of PROC_ALL_PIDS only;
    all group/PPID consumers still require strictly positive PIDs. Never accept a negative or truncated buffer."""
    size = ctypes.sizeof(ctypes.c_int)
    if type(nbytes) is not int or nbytes < 0 or nbytes % size or nbytes // size > len(values):
        raise OSError(errno.EIO, "malformed proc_listpids byte count %r" % (nbytes,))
    entries = list(values[:nbytes // size])
    if any(p < 0 or (p == 0 and not allow_kernel_zero) for p in entries):
        raise OSError(errno.EIO, "malformed proc_listpids PID entry")
    return sorted(set(p for p in entries if p != 0))


def list_pids(kind, value):
    """Zombie-inclusive libproc listing; malformed or potentially truncated output is uncertainty, never empty."""
    slots = ALL_PID_SLOTS if kind == PROC_ALL_PIDS else LIST_SLOTS
    buf = (ctypes.c_int * slots)()
    ctypes.set_errno(0)
    n = LIBPROC.proc_listpids(kind, value, buf, ctypes.sizeof(buf))
    err = ctypes.get_errno()
    if n < 0 or (n == 0 and err != 0) or n >= ctypes.sizeof(buf):
        raise OSError(err or errno.EIO, "proc_listpids(%d,%d) incomplete (%d bytes)" % (kind, value, n))
    return parse_pid_buffer(buf, n, allow_kernel_zero=kind == PROC_ALL_PIDS)


def bsd_identity(pid):
    """(identity, None) from PROC_PIDTBSDINFO (sys/proc_info.h struct proc_bsdinfo, 136 bytes), or (None, error)."""
    n, err, raw = _pidinfo(pid, PROC_PIDTBSDINFO, BSD_SIZE)
    if n != BSD_SIZE:
        return None, {"bsd_bytes": n, "errno": err}
    status, _xstatus, rpid, ppid = struct.unpack_from("=IIII", raw, 4)
    return {"pid": rpid, "ppid": ppid, "pgid": struct.unpack_from("=I", raw, 100)[0], "status": status,
            "start": list(struct.unpack_from("=QQ", raw, 120)),
            "comm": raw[48:64].split(b"\0")[0].decode("ascii", "replace")}, None


def task_rss(pid):
    """Resident bytes from PROC_PIDTASKINFO (struct proc_taskinfo, 96 bytes, pti_resident_size at offset 8); None
    when unreadable, never mapped to zero."""
    n, _err, raw = _pidinfo(pid, PROC_PIDTASKINFO, TASK_SIZE)
    if n != TASK_SIZE:
        return None
    return struct.unpack_from("=Q", raw, 8)[0]


def identity_checked(pid, runner_pid):
    """G2: no ESRCH/group-membership wildcard. Missing BSD start identity remains explicit unknown.
    Only waitid(WNOWAIT) can prove a fast-exited retained child; this NEVER authorizes a live signal."""
    ident, err = bsd_identity(pid)
    if ident is not None:
        if ident["pid"] != pid or ident["ppid"] != runner_pid or ident["pgid"] != pid or not ident.get("start"):
            raise RuntimeError("start identity mismatch %r" % (ident,))
        return dict(ident, state="zombie" if ident["status"] == SZOMB else "alive")
    info = os.waitid(os.P_PID, pid, os.WEXITED | os.WNOHANG | os.WNOWAIT)
    if info is not None and info.si_pid == pid and pid in list_pids(PROC_PGRP_ONLY, pid):
        return {"pid": pid, "pgid": pid, "ppid": runner_pid, "start": None,
                "state": "owned_exit_WNOWAIT", "identity_unknown": True, "bsd_read": err,
                "waitid": [info.si_pid, info.si_code, info.si_status]}
    raise RuntimeError("unavailable start identity %r" % (err,))


def descendants(pid, pgid, deadline=None):
    found = {p for p in list_pids(PROC_PGRP_ONLY, pgid) if p != pid}
    seen, todo = {pid}, [pid]
    end = work_deadline(deadline=deadline)
    while todo:
        if len(seen) > LIST_SLOTS or time.monotonic() > end:
            raise RuntimeError("descendant census incomplete: work cap")
        q = todo.pop()
        for c in list_pids(PROC_PPID_ONLY, q):
            if c not in seen:
                seen.add(c)
                found.add(c)
                todo.append(c)
    return sorted(found)


def _entry_kind(m):
    return ("dir" if stat.S_ISDIR(m) else "file" if stat.S_ISREG(m) else "symlink" if stat.S_ISLNK(m)
            else "fifo" if stat.S_ISFIFO(m) else "socket" if stat.S_ISSOCK(m) else "other")


def census_entry(st):
    """N8: census evidence of one entry: directories (kind, dev, ino, mode) (their content is covered entry by
    entry); every other kind (kind, dev, ino, size, mtime_ns, ctime_ns, mode, nlink), so an in-place same-size
    rewrite or a replacement is visible."""
    k = _entry_kind(st.st_mode)
    if k == "dir":
        return (k, st.st_dev, st.st_ino, stat.S_IMODE(st.st_mode))
    return (k, st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns, stat.S_IMODE(st.st_mode), st.st_nlink)


def run_tree_census(root=None):
    base = STATE["out"] if root is None else root
    return walk_bounded(base, TREE[base][0] if root is None else None)


def lane_usage(root=LANE):
    """G4/G6: measured physical logical consumption, bounded work, hard links counted once."""
    total, seen = 0, set()
    for v in walk_bounded(root).values():
        if v[0] != "dir" and (v[1], v[2]) not in seen:
            seen.add((v[1], v[2]))
            total += v[3]
    return total


def ancestry_refusal(path):
    """N8: every component of `path` must be a real directory (lstat; a symlink anywhere refuses)."""
    p = os.sep
    for comp in [c for c in path.split(os.sep) if c]:
        p = os.path.join(p, comp)
        try:
            st = os.lstat(p)
        except OSError as exc:
            return "ancestor %s unreadable %r" % (p, exc)
        if not stat.S_ISDIR(st.st_mode):
            return "ancestor %s is not a real directory" % p
    return None


def out_dir_refusal(out_dir, parent=PILOT_ROOT):
    """V4: the output must be a NEW direct child of parent, and parent and each of its ancestors must be a real
    directory (lstat: a symlink anywhere refuses); creation stays exclusive."""
    if os.path.dirname(out_dir) != parent or os.path.basename(out_dir) in ("", ".", ".."):
        return "output must be a direct child of " + parent
    why = ancestry_refusal(parent)
    if why:
        return why
    if os.path.lexists(out_dir):
        return "output path exists"
    return None


def anchor_dir(path, dir_fd, name):
    fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=dir_fd)
    try:
        st = os.fstat(fd)
        TREE[path] = (fd, st.st_dev, st.st_ino)
    except BaseException:
        os.close(fd)
        raise
    return TREE[path]


def anchor_existing_dir(path):
    """N8: anchor an existing directory given by absolute path after an ancestry check, then re-validate that the
    path still names the anchored directory (closes the check/open window)."""
    why = ancestry_refusal(path)
    if why:
        raise RuntimeError(why)
    fd, dev, ino = anchor_dir(path, None, path)
    st = os.lstat(path)
    if not stat.S_ISDIR(st.st_mode) or (st.st_dev, st.st_ino) != (dev, ino) or ancestry_refusal(path):
        raise RuntimeError("directory changed while anchoring: " + path)
    return fd


def tree_path(path):
    """N8: (anchored directory fd, final name) for a path whose parent directory is anchored; refuses others."""
    d, name = os.path.dirname(path), os.path.basename(path)
    if d not in TREE or not name or name in (".", ".."):
        raise RuntimeError("path is not inside an anchored directory: " + path)
    return TREE[d][0], name


def create_excl(path, mode=0o644):
    """G7/G9: inventory the acquired descriptor immediately; failed/partial creations remain visible."""
    dfd, name = tree_path(path)
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, mode, dir_fd=dfd)
    try:
        CREATED[path] = {"state": "open", "kind": "file", "identity": None}
        st = os.fstat(fd)
        CREATED[path]["identity"] = [st.st_dev, st.st_ino]
    except BaseException:
        os.close(fd)
        raise
    return fd


def mkdir_anchored(path):
    dfd, name = tree_path(path)
    os.mkdir(name, 0o755, dir_fd=dfd)
    CREATED[path] = {"state": "dir", "kind": "dir"}
    try:
        return anchor_dir(path, dfd, name)
    except BaseException as exc:
        CREATED[path].update(state="unanchored_dir", error=repr(exc))
        raise


def create_run_tree(out_dir, parent=PILOT_ROOT):
    """N8: exclusive creation of the run tree, anchored to directory descriptors opened without following
    symlinks; every later runner-side creation or read in the tree goes through these descriptors."""
    why = out_dir_refusal(out_dir, parent)
    if why:
        raise RuntimeError(why)
    anchor_existing_dir(parent)
    mkdir_anchored(out_dir)
    for sub in TREE_SUBDIRS:
        mkdir_anchored(os.path.join(out_dir, sub))
    why = confinement_refusals(out_dir)
    if why:
        raise RuntimeError("run tree confinement: %r" % (why,))


def confinement_refusals(out_dir=None):
    """N8: every anchored directory still resolves by path, without symlinks, to its anchored (dev, inode), and
    every ancestor of the run tree is a real directory."""
    why = []
    try:
        root = out_dir or STATE["out"]
        if root is not None:
            w = ancestry_refusal(root)
            if w:
                why.append(w)
        for path, (fd, dev, ino) in list(TREE.items()):
            st, fst = os.lstat(path), os.fstat(fd)
            if not stat.S_ISDIR(st.st_mode) or (st.st_dev, st.st_ino) != (dev, ino) \
                    or (fst.st_dev, fst.st_ino) != (dev, ino):
                why.append("anchored directory moved or replaced: " + path)
    except BaseException as exc:
        why.append("confinement check failed %r" % (exc,))
    return why


def preservation_refusals(exclude=()):
    """G7: complete artifact/identity inventory, including refused/failed/partial creations. The only exclusion
    is the currently open exclusive item publication owned by this very call; it is rechecked after close."""
    why = []
    prior_end = STATE.get("cleanup_deadline")
    STATE["cleanup_deadline"] = work_deadline()
    try:
        snap = run_tree_census()
        for path, v in snap.items():
            if path in exclude:
                continue
            made = CREATED.get(path)
            if made is None:
                why.append("unregistered retained entry: " + path)
                continue
            if made.get("state") not in ("complete", "fifo", "dir"):
                why.append("partial/failed retained creation: " + path)
            if v[0] == "file" and v[7] != 1:
                why.append("runner-exclusive retained file acquired extra hard links: " + path)
            ident = made.get("identity")
            if ident is not None and list(v[1:3]) != ident:
                why.append("retained creation identity changed: " + path)
        for path, made in CREATED.items():
            if path not in exclude and path.startswith(STATE["out"] + os.sep) and path not in snap:
                why.append("retained creation disappeared: " + path)
        for path, (digest, n) in list(WRITTEN.items()):
            if path in exclude:
                continue
            if time.monotonic() > STATE["cleanup_deadline"]:
                raise RuntimeError("complete preservation work deadline exhausted")
            if sha_tree(path, limit=n) != (digest, n):
                why.append("retained bytes changed: " + path)
    except BaseException as exc:
        why.append("complete preservation inventory unproved %r" % (exc,))
    finally:
        STATE["cleanup_deadline"] = prior_end
    return why


def _hex64(x):
    return isinstance(x, str) and HEX64.fullmatch(x) is not None


def attempt_owner_manifest(entry_dir, launch):
    """G1: derive inventory from durable runner, child/helper intents/launches, settlements and full censuses.
    Never infer complete ownership from summary booleans. Legacy/missing/partial evidence is explicit uncertainty
    that only a NEW parent disposition can resolve; all known identities still get independent liveness checks."""
    ids, unknowns = [], []
    if not isinstance(launch, dict):
        launch = {}
        unknowns.append("runner failed before launch publication; independent parent runner inventory required")
    def add(pid, ident=None, bound=None, leader=False, source=None):
        if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 0:
            unknowns.append("invalid/missing pid at %s" % source)
            return
        start = ident.get("start") if isinstance(ident, dict) else None
        if start is not None and not (isinstance(start, list) and len(start) == 2
                                     and all(isinstance(x, int) and not isinstance(x, bool) and x >= 0 for x in start)):
            unknowns.append("malformed start at %s" % source)
            start = None
        ids.append({"pid": pid, "start": start, "started_by_epoch": bound, "group_leader": leader, "source": source})
    ri = launch.get("runner_identity") if isinstance(launch, dict) else None
    bound = launch.get("runner_started_by_epoch")
    if bound is None and isinstance(launch.get("host_clock"), str):
        try:
            bound = _aware(launch["host_clock"]).timestamp() + 1.0
        except BaseException:
            pass
    add(launch.get("pid"), ri, bound, False, "launch-record.json:runner")
    if not isinstance(ri, dict) or not ri.get("start"):
        unknowns.append("legacy/incomplete runner identity and unrecorded legacy helpers")
    snap = run_tree_census(entry_dir)
    intents, launches, nolaunches = set(), set(), set()
    for path, v in sorted(snap.items()):
        if not path.startswith(os.path.join(entry_dir, "children") + os.sep) or v[0] != "file":
            continue
        if not path.endswith((".intent.json", ".launch.json", ".nolaunch.json", ".QUARANTINE.json", ".settle.json")):
            continue
        try:
            rec = json.loads(read_regular_bounded(path, RECORD_MAX))
            if not isinstance(rec, dict):
                raise ValueError("not object")
        except BaseException as exc:
            unknowns.append("unreadable ownership record %s: %r" % (path, exc))
            continue
        if path.endswith(".intent.json"):
            intents.add(path[:-len(".intent.json")])
        elif path.endswith(".nolaunch.json"):
            if rec.get("no_launch") is True:
                nolaunches.add(path[:-len(".nolaunch.json")])
            else:
                unknowns.append("unproved no-launch record " + path)
        elif path.endswith(".launch.json"):
            launches.add(path[:-len(".launch.json")])
            add(rec.get("pid"), rec.get("identity"), rec.get("started_by_epoch", rec.get("start_epoch")), True, path)
        else:
            if path.endswith(".QUARANTINE.json"):
                unknowns.append("UNSETTLED receipt " + path)
                add(rec.get("pid"), rec.get("identity_at_start"), rec.get("started_by_epoch"), True, path)
            census = rec.get("live_census") or {}
            extra = rec.get("known_identities") or []
            for item in extra + (census.get("group_members") or []) + (census.get("descendants") or []):
                if isinstance(item, dict):
                    add(item.get("pid"), item.get("identity"), item.get("observed_by_epoch", census.get("at_epoch")),
                        False, path)
                else:
                    add(item, None, census.get("at_epoch"), False, path)
            if rec.get("census_uncertainty") or census.get("complete") is False:
                unknowns.append("incomplete census " + path)
    for base in sorted(intents - launches - nolaunches):
        unknowns.append("intent without proven launch/no-launch: " + base)
    def collect_record(record, source):
        stack, count = [record], 0
        while stack:
            count += 1
            if count > TREE_ENTRY_MAX:
                unknowns.append("ownership JSON traversal work cap: " + source)
                break
            item = stack.pop()
            if isinstance(item, dict):
                identity = item if isinstance(item.get("start"), list) else item.get("identity_at_start", item.get("identity"))
                if type(item.get("pid")) is int:
                    add(item["pid"], identity, item.get("started_by_epoch", item.get("observed_by_epoch")),
                        item.get("pgid") == item["pid"] or item.get("kind") in ("child", "helper"), source)
                for key, value in item.items():
                    if key in ("runner", "runner_identity", "children", "helpers", "metadata_helpers", "ownership_manifest", "unresolved",
                               "unsettled_owners", "known_identities", "live_census", "group_members", "descendants"):
                        stack.append(value)
            elif isinstance(item, list):
                stack.extend(item)
            elif type(item) is int:
                add(item, None, None, False, source)
    for name in ("summary.json", "closeout.json"):
        path = os.path.join(entry_dir, name)
        if os.path.lexists(path):
            try:
                collect_record(json.loads(read_regular_bounded(path, RECORD_MAX)), path)
            except BaseException as exc:
                unknowns.append("incomplete ownership publication %s: %r" % (name, exc))
    # Every manifest identity is retained. Conflicting known starts for a reused pid are distinct identities.
    unique = {}
    for x in ids:
        key = (x["pid"], tuple(x["start"]) if x["start"] is not None else None)
        old = unique.get(key)
        if old is None:
            unique[key] = x
        else:
            old["group_leader"] = old["group_leader"] or x["group_leader"]
            bounds = [b for b in (old.get("started_by_epoch"), x.get("started_by_epoch"))
                      if isinstance(b, (int, float)) and not isinstance(b, bool)]
            old["started_by_epoch"] = min(bounds) if bounds else None
    return {"identities": list(unique.values()), "unknowns": unknowns,
            "runner_identity": {"pid": launch.get("pid"),
                                "start": ri.get("start") if isinstance(ri, dict) else None}}


def owner_identities_of_attempt(entry_dir, summary=None):
    launch = json.loads(read_regular_bounded(os.path.join(entry_dir, "launch-record.json"), RECORD_MAX))
    return attempt_owner_manifest(entry_dir, launch)["identities"]


def identity_ended_refusals(identity, present):
    pid = identity["pid"]
    if pid not in present:
        if identity.get("group_leader") and list_pids(PROC_PGRP_ONLY, pid):
            return ["pid %d absent but its process group still has members" % pid]
        return []
    current, err = bsd_identity(pid)
    if current is None or current.get("status") == SZOMB:
        return ["pid %d is listed (zombies included) but unreadable/zombie: %r" % (pid, err)]
    start = identity.get("start")
    if start is not None:
        return [] if current.get("start") != start else ["pid %d original identity still present" % pid]
    # No wall-clock upper-bound heuristic: a clock adjustment is not identity proof. Unknown original start
    # plus a currently listed pid remains a parent blocker, even if it might be innocent PID reuse.
    return ["pid %d present with unknown original start; reuse cannot be proved" % pid]


def disposition_refusals(entry_dir, release, manifest, summary_sha):
    """G1/G5: EVERY release uses NEW independent parent authority. No parseable self-summary certifies its own
    successful publication, prior-runner return, memory release or absence of unrecorded owners.
    Parent binds launch/summary/closeout, a complete tree census and an after-exit audit; runner independently
    checks all known/certified identities against a zombie-inclusive census. Unknown -> retain parent block."""
    disp = release.get("disposition")
    if not (isinstance(disp, dict) and isinstance(disp.get("path"), str) and _hex64(disp.get("sha256"))):
        return ["NEW parent release disposition missing; reservation retained"]
    try:
        d = json.loads(read_pinned(disp["path"], disp["sha256"], RECORD_MAX))
        census = census_digest(entry_dir)
    except BaseException as exc:
        return ["parent disposition/census unreadable: %r" % (exc,)]
    if not isinstance(d, dict) or d.get("schema") != DISPOSITION_SCHEMA or d.get("attempt_dir") != entry_dir \
            or d.get("launch_record_sha256") != release.get("launch_record_sha256") \
            or d.get("summary_sha256") != summary_sha or d.get("closeout_sha256") != release.get("closeout_sha256") \
            or d.get("attempt_tree_census") != census:
        return ["parent disposition does not bind this exact attempt, publications and late-artifact census"]
    required = ("all_processes_ended", "ownership_inventory_complete", "all_runner_resources_released",
                "all_unknown_owners_resolved", "publication_audited", "ram_accounting_audited", "late_artifacts_audited")
    if any(d.get(k) is not True for k in required) or not isinstance(d.get("identities"), list):
        return ["parent disposition lacks affirmative complete post-run audit"]
    if manifest.get("publication_unknowns") and d.get("publication_failure_disposed") is not True:
        return ["partial/unknown publication needs explicit NEW parent failure disposition"]
    observed_exit = d.get("observed_runner_exit_code")
    if type(observed_exit) is not int or not -255 <= observed_exit <= 255:
        return ["parent-observed runner exit missing/invalid"]
    certified = {}
    for x in d["identities"]:
        if not isinstance(x, dict) or not isinstance(x.get("pid"), int) or isinstance(x.get("pid"), bool) or x["pid"] <= 0:
            return ["malformed parent identity"]
        s = x.get("start")
        if s is not None and not (isinstance(s, list) and len(s) == 2 and all(type(v) is int and v >= 0 for v in s)):
            return ["malformed parent start identity"]
        certified[(x["pid"], tuple(s) if s is not None else None)] = dict(x)
    identities = []
    why = []
    runner = d.get("runner_identity")
    if not isinstance(runner, dict) or type(runner.get("pid")) is not int or runner["pid"] <= 0:
        return ["independent parent runner identity missing"]
    runner_start = runner.get("start")
    runner_key = (runner["pid"], tuple(runner_start) if isinstance(runner_start, list) else None)
    if runner_key not in certified:
        why.append("parent runner identity is not covered by full certified identities")
    known_runner = manifest.get("runner_identity") or {}
    if known_runner.get("pid") is not None and (runner["pid"] != known_runner["pid"]
                                               or runner_start != known_runner.get("start")):
        why.append("parent runner identity contradicts durable launch identity")
    for x in manifest["identities"]:
        key = (x["pid"], tuple(x["start"]) if x["start"] is not None else None)
        if key not in certified:
            why.append("parent disposition does not cover known identity %r" % (key,))
        identities.append(x)
        certified.pop(key, None)
    identities += list(certified.values())
    if not identities:
        why.append("empty ownership inventory is not release authority")
    try:
        present = set(list_pids(PROC_ALL_PIDS, 0))
        for x in identities:
            why += identity_ended_refusals(x, present)
    except BaseException as exc:
        why.append("complete liveness census unavailable: %r" % (exc,))
    closeout_sha = release.get("closeout_sha256")
    if closeout_sha is not None:
        try:
            raw_closeout = read_pinned(os.path.join(entry_dir, "closeout.json"), closeout_sha, RECORD_MAX)
        except BaseException as exc:
            return why + ["closeout exact bytes unreadable/digest mismatch %r" % (exc,)]
        publication_matches = False
        try:
            c = json.loads(raw_closeout)
            publication_matches = (isinstance(c, dict) and c.get("schema") in KNOWN_CLOSEOUT_SCHEMAS
                                   and c.get("summary_sha256") == summary_sha and c.get("exit_code") == observed_exit
                                   and c.get("publication_completion_self_certified") is False)
            if summary_sha is not None:
                publication_matches = publication_matches and c.get("summary_bytes") == os.lstat(
                    os.path.join(entry_dir, "summary.json")).st_size
        except BaseException:
            publication_matches = False
        if not publication_matches and d.get("publication_failure_disposed") is not True:
            why.append("closeout/observed exit/malformed publication needs explicit parent failure disposition")
    elif d.get("publication_failure_disposed") is not True and d.get("legacy_audit") is not True:
        why.append("missing closeout requires explicit legacy/failed-publication disposition")
    return why


def release_refusals(entry_dir, release, go_sha):
    if release is None or not isinstance(release, dict):
        return ["attempt not explicitly released by single parent allocation: " + entry_dir]
    try:
        if not stat.S_ISDIR(os.lstat(entry_dir).st_mode):
            return ["attempt is not a real directory"]
        publication_unknowns = []
        launch_path = os.path.join(entry_dir, "launch-record.json")
        launch = None
        if release.get("launch_record_sha256") is None:
            if os.path.lexists(launch_path):
                return ["launch exists but release does not bind its exact bytes"]
        else:
            raw = read_pinned(launch_path, release["launch_record_sha256"], RECORD_MAX)
            try:
                launch = json.loads(raw)
            except BaseException as exc:
                publication_unknowns.append("partial/unparseable launch: %r" % (exc,))
            if not isinstance(launch, dict):
                publication_unknowns.append("missing structured launch authority")
                launch = None
            elif launch.get("schema") not in KNOWN_LAUNCH_SCHEMAS:
                publication_unknowns.append("unknown launch schema; independent parent failure audit required")
            if isinstance(launch, dict):
                if isinstance(launch.get("go"), dict) and launch["go"].get("sha256") == go_sha:
                    return ["this exact GO already consumed"]
                if not isinstance(launch.get("go"), dict):
                    publication_unknowns.append("GO binding absent; independent one-use audit required")
        smsha = release.get("summary_sha256")
        smpath = os.path.join(entry_dir, "summary.json")
        if smsha is None:
            if os.path.lexists(smpath):
                return ["summary exists but release does not bind it"]
        else:
            raw = read_pinned(smpath, smsha, RECORD_MAX)
            try:
                summary = json.loads(raw)
                if not isinstance(summary, dict) or summary.get("schema") not in KNOWN_SUMMARY_SCHEMAS:
                    publication_unknowns.append("unknown/malformed summary")
            except BaseException as exc:
                publication_unknowns.append("partial/unparseable summary: %r" % (exc,))
        if release.get("closeout_sha256") is None and os.path.lexists(os.path.join(entry_dir, "closeout.json")):
            return ["closeout exists but release does not bind its exact digest"]
        manifest = attempt_owner_manifest(entry_dir, launch)
        manifest["publication_unknowns"] = publication_unknowns
        manifest["unknowns"].extend(publication_unknowns)
        return disposition_refusals(entry_dir, release, manifest, smsha)
    except BaseException as exc:
        return ["release evidence incomplete/unreadable %r" % (exc,)]


def allocation_refusals(go, go_sha, out_dir, full_reserve, root=PILOT_ROOT):
    a = go.get("allocation") if isinstance(go, dict) else None
    if not isinstance(a, dict) or a.get("schema") != ALLOCATION_SCHEMA:
        return ["GO lacks exact parent allocation " + ALLOCATION_SCHEMA], None
    why = []
    res = a.get("reservation_bytes")
    if type(res) is not int or res != full_reserve:
        why.append("parent reservation must EQUAL exact full runner reservation")
    if a.get("out_dir") != out_dir or a.get("lane_ceiling_bytes") != LANE_CEILING or a.get("busy_slots") != BUSY_SLOTS:
        why.append("parent allocation output/ceiling/busy slots mismatch")
    releases = a.get("released_attempts")
    if not isinstance(releases, list):
        return why + ["release inventory is not a list"], None
    by_dir = {}
    for r in releases:
        if not isinstance(r, dict) or not isinstance(r.get("dir"), str) or os.path.dirname(r["dir"]) != root \
                or r["dir"] in by_dir \
                or (r.get("launch_record_sha256") is not None and not _hex64(r["launch_record_sha256"])) \
                or (r.get("summary_sha256") is not None and not _hex64(r["summary_sha256"])) \
                or (r.get("closeout_sha256") is not None and not _hex64(r["closeout_sha256"])):
            why.append("malformed/duplicate release entry")
            continue
        by_dir[r["dir"]] = r
    prior = {}
    try:
        entries = sorted(os.listdir(root))
        if len(entries) > TREE_ENTRY_MAX:
            raise RuntimeError("pilot entry cap")
        usage = lane_usage()
        for e in entries:
            d = os.path.join(root, e)
            if d == out_dir:
                why.append("output already exists; one-use GO")
            else:
                why += [e + ": " + w for w in release_refusals(d, by_dir.get(d), go_sha)]
                prior[d] = census_digest(d)
        if set(by_dir) != {os.path.join(root, e) for e in entries}:
            why.append("release inventory != complete existing pilot inventory")
        if type(res) is not int or usage + res > LANE_CEILING:
            why.append("measured lane usage plus exact full reservation exceeds ceiling")
    except BaseException as exc:
        return why + ["allocation census incomplete: %r" % (exc,)], None
    return why, {"allocation_id": a.get("allocation_id"), "reservation_bytes": res,
                 "runner_reservation_bytes": full_reserve, "lane_usage_bytes": usage,
                 "ceiling_bytes": LANE_CEILING, "pilot_entries": entries, "prior_attempt_census": prior}



def ledger_refusals():
    """G6/G7: capacity never disappears because it was PREcharged. Bound = other-lane physical consumption +
    this run's FULL exact reservation, independent of partial captures/record-size precharges. Same snapshot
    classifies outside/inside bytes; previous attempts' complete metadata/identity inventories stay unchanged."""
    why = []
    try:
        entries = sorted(os.listdir(PILOT_ROOT))
        expect = sorted(STATE["pilot_entries"] + [os.path.basename(STATE["out"])])
        if entries != expect:
            why.append("pilot root entry set drift")
        for d, old in (STATE.get("prior_census") or {}).items():
            if census_digest(d) != old:
                why.append("prior attempt immutable inventory drift: " + d)
        snap = walk_bounded(LANE)
        outside, own, seen = 0, 0, set()
        # Outside first: a hard link into the run cannot subtract pre-existing consumption.
        ordered = sorted(snap.items(), key=lambda p: p[0].startswith(STATE["out"] + os.sep))
        for p, v in ordered:
            if v[0] == "dir" or (v[1], v[2]) in seen:
                continue
            seen.add((v[1], v[2]))
            if p.startswith(STATE["out"] + os.sep):
                own += v[3]
            else:
                outside += v[3]
        bound = outside + STATE["reservation"]
        if own > STATE["reservation"] or bound > LANE_CEILING:
            why.append("actual consumption/full future capacity exceeds lane ceiling or run reservation")
        led = {"other_lane_consumption_bytes": outside, "this_run_physical_bytes": own,
               "lane_usage_bytes": outside + own, "full_reservation_bytes": STATE["reservation"],
               "outstanding_future_growth_bytes": max(0, STATE["reservation"] - own),
               "conservative_bound_bytes": bound, "ceiling_bytes": LANE_CEILING,
               "charged_capacity_bytes": STATE["written"], "pilot_entries_unchanged": entries == expect}
        return why, led
    except BaseException as exc:
        return ["ledger/preservation census incomplete: %r" % (exc,)], None


def registry_refusals():
    """Fail-closed STOP registry: new-round STOP*/HALT*/SAT-CANDIDATE* markers in LANE/control or
    RUN/control; any change, loss or addition in the inherited old cycle2-root STOP/HALT set."""
    why = []
    for d in (LANE + "/control", RUN + "/control"):
        for name in sorted(os.listdir(d)):
            if re.match(r"(?i)^(stop|halt|sat-candidate)", name) or "HALT" in name:
                why.append("new-round marker " + os.path.join(d, name))
    c2 = OLD + "/cycle2"
    present = sorted(n for n in os.listdir(c2) if re.match(r"^(STOP|HALT)", n) or "HALT" in n)
    if present != sorted(OLD_LIVE_MARKERS):
        why.append("inherited cycle2 marker set changed: " + json.dumps(present))
    for name, h in OLD_LIVE_MARKERS.items():
        try:
            if sha_file(os.path.join(c2, name))[0] != h:
                why.append("inherited marker changed: " + name)
        except Exception as exc:
            why.append(f"inherited marker unreadable: {name}: {exc!r}")
    try:
        if sha_file(REGISTRY[0])[0] != REGISTRY[1]:
            why.append("lane registry changed")
        if sha_file(LAUNCH_CONTRACT[0])[0] != LAUNCH_CONTRACT[1]:
            why.append("launch contract changed")
    except Exception as exc:
        why.append("registry/contract unreadable: %r" % exc)
    return why


def _aware(s):
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("naive timestamp")
    return dt


def _int(x, lo=None):
    if not isinstance(x, int) or isinstance(x, bool) or (lo is not None and x < lo):
        raise ValueError("bad integer %r" % (x,))
    return x


def stability_refusals(projected):
    """resource-stability-addendum v1 rule over the v2-pinned v3 monitor; strict schema.  V4: the first record must be
    the pinned observer_start provenance header (a sample-only log is refused)."""
    try:
        raw = read_regular_bounded(MONITOR, MONITOR_MAX)   # N7: regular, no symlink, never blocks, bounded
    except BaseException as exc:
        return ["monitor unreadable %r" % (exc,)]
    complete = raw.split(b"\n")[:-1]  # last element: b"" after a final newline, or an ignored partial line
    rows = []
    header_seen = False
    for i, ln in enumerate(complete):
        try:
            o = json.loads(ln)
            if not isinstance(o, dict):
                raise ValueError("not an object")
            if "event" in o:
                if not (i == 0 and set(o) == {"event", "at", "pid", "pgid", "cwd", "source_sha256"}
                        and o["event"] == "observer_start" and o["source_sha256"] == OBSERVER_SOURCE_SHA
                        and o["cwd"] == OBSERVER_CWD):
                    return ["monitor event line %d is not the allowed first observer_start: %r" % (i, ln[:160])]
                _aware(o["at"])
                _int(o["pid"], 1)
                _int(o["pgid"], 1)
                header_seen = True
                continue
            if set(o) != {"t", "free", "floor_bytes", "scope"} or o["floor_bytes"] != 12_000_000_000 \
                    or o["scope"] != SAMPLE_SCOPE:
                raise ValueError("sample schema/fixed values")
            _int(o["floor_bytes"], 0)
            rows.append((_aware(o["t"]).timestamp(), _int(o["free"], 0)))
        except Exception as exc:
            return ["malformed monitor line %d: %r (%r)" % (i, ln[:160], exc)]
    if not header_seen:
        return ["monitor lacks the pinned observer_start provenance header"]
    if not rows:
        return ["no monitor samples"]
    for a, b in zip(rows, rows[1:]):
        if not b[0] > a[0]:
            return ["monitor timestamps not strictly increasing"]
    why = []
    now = time.time()
    t_last, free_last = rows[-1]
    if not (0 <= now - t_last <= 30):
        why.append(f"monitor last sample age {now - t_last:.1f}s outside [0,30]")
    win = [r for r in rows if now - 300 <= r[0] <= now]
    if len(win) < 25:
        why.append(f"only {len(win)} samples in [now-300, now]")
    elif win[-1][0] - win[0][0] < 280:
        why.append(f"window span {win[-1][0] - win[0][0]:.1f}s < 280 s")
    if free_last < 13_500_000_000 + projected:
        why.append(f"last free {free_last} < 13.5e9 + projected {projected}")
    allowed = max(300_000_000, (free_last - 13_500_000_000) // 12)
    peak, drop = None, 0
    for _, fr in win:
        peak = fr if peak is None else max(peak, fr)
        drop = max(drop, peak - fr)
    if drop > allowed:
        why.append(f"peak-to-later drop {drop} > allowed {allowed}")
    return why



def full_admission(projected, child_deadline, child_deadline_mono):
    """Blocking part of admission (registry, monitor, statvfs, N3 lane ledger, N8 confinement, V3 absolute and
    elapsed fit).  Returns refusal reasons."""
    why = []
    try:
        why += registry_refusals()
        why += stability_refusals(projected)
        fb = free_bytes()
        if fb < FRESH_BASE + projected:
            why.append(f"fresh free {fb} < 12.2e9 + {projected}")
        if fb - STATE["remaining_reserve"] < FREE_FLOOR:
            why.append(f"free {fb} - remaining reservations {STATE['remaining_reserve']} < 12e9")
        led_why, STATE["last_ledger"] = ledger_refusals()
        why += led_why
        why += confinement_refusals()
    except Exception as exc:
        why.append("admission exception %r" % exc)
    if child_deadline + SETTLE_TAIL > STATE["abs_end"] or child_deadline + SETTLE_TAIL + MARGIN > STATE["chunk_end"] \
            or child_deadline + SETTLE_TAIL > OWNED_SETTLED_BY - 180 \
            or child_deadline_mono + SETTLE_TAIL > STATE["mono_end"] \
            or child_deadline_mono + SETTLE_TAIL + MARGIN > STATE["mono_chunk_end"]:
        why.append("per-child chunk fit / absolute or elapsed end (with full settlement tail)")
    if time.time() > NATIVE_LAUNCH_STOP:
        why.append("after frozen native launch cutoff")
    return why


def buffer_charge():
    held = {}
    for b in LIVE_BUFFERS:
        if not isinstance(b.retained, int) or isinstance(b.retained, bool) or b.retained < 0:
            raise RuntimeError("unknown proof RAM accounting")
        alive = b.thread is not None and b.thread.is_alive()
        if alive or not b.released:
            blocks = b.blocks
            key = ("tuple", id(blocks)) if isinstance(blocks, tuple) and blocks else ("collector", id(b))
            held[key] = max(held.get(key, 0), b.retained)
    for f in LIVE_FEEDERS:
        if f.blocks:
            key = ("tuple", id(f.blocks))
            held[key] = max(held.get(key, 0), f.expected)
    return sum(held.values())


class ProofBuffer:
    """S1: owned FIFO reader retaining the proof in RAM only (immutable FEED_BLOCK blocks) with a HARD byte cap;
    bytes and SHA-256 are measured as they arrive from the producer; nothing is written to disk.  N8: the FIFO is
    created, opened and re-checked through its anchored directory descriptor; N7: monotonic unblock deadline;
    N6: charged while the collector thread lives or until released."""

    def __init__(self, fifo_path, cap):
        self.fifo_path, self.cap = fifo_path, cap
        self.dir_fd = self.fifo_name = self.fifo_identity = self.fifo_ino = None
        self.blocks = []
        self.sha = hashlib.sha256()
        self.retained = self.received = self.discarded = 0
        self.over_cap = self.connected = self.eof = self.released = self.release_requested = False
        self.frozen_id = None
        self.error = self.construction_error = None
        self.unblocked_by_runner = False
        self.finished = None
        self.thread = None
        self.thread_started = False
        self.reader_fd = None
        self.reader_fd_closed = True
        LIVE_BUFFERS.append(self)                 # fully inspectable even if any later acquisition fails
        try:
            self.dir_fd, self.fifo_name = tree_path(fifo_path)
            st = mkfifo_anchored(fifo_path)
            self.fifo_ino = st.st_ino
            self.fifo_identity = [st.st_dev, st.st_ino]
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            self.thread_started = True
        except BaseException as exc:
            self.construction_error = repr(exc)
            latch("proof buffer construction unproven %r" % (exc,))
            try:
                self.finish()
                self.release()
            except BaseException as cleanup_exc:
                self.error = "construction rollback unproven: %r" % (cleanup_exc,)
            raise

    def _run(self):
        acc = bytearray()
        try:
            fd = os.open(self.fifo_name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=self.dir_fd)  # blocks until a writer opens
            self.reader_fd = fd
            self.reader_fd_closed = False
            try:
                fst = os.fstat(fd)
                if not stat.S_ISFIFO(fst.st_mode) or [fst.st_dev, fst.st_ino] != self.fifo_identity:
                    raise RuntimeError("collector opened a different FIFO")
                self.connected = True
                while True:
                    b = os.read(fd, FEED_BLOCK)
                    if not b:
                        self.eof = True
                        break
                    self.received += len(b)
                    if not self.over_cap and self.retained + len(b) <= self.cap:
                        acc += b
                        self.sha.update(b)
                        self.retained += len(b)
                        while len(acc) >= FEED_BLOCK:       # exact FEED_BLOCK blocks; the tail stays in acc
                            self.blocks.append(bytes(acc[:FEED_BLOCK]))
                            del acc[:FEED_BLOCK]
                    else:
                        self.over_cap = True       # never retain beyond the cap; drain so the producer can exit
                        self.discarded += len(b)
            finally:
                try:
                    os.close(fd)
                    self.reader_fd_closed = True
                    self.reader_fd = None
                except BaseException as exc:
                    self.error = "reader close: %r" % (exc,)
        except Exception as exc:
            self.error = repr(exc)
        finally:
            try:
                if acc:
                    self.blocks.append(bytes(acc))
            except Exception as exc:
                self.error = (self.error or "") + " tail:" + repr(exc)

    def digest(self):
        """Independent second pass over the retained RAM blocks."""
        h = hashlib.sha256()
        n = 0
        for b in self.blocks:
            h.update(b)
            n += len(b)
        return [h.hexdigest(), n]

    def finish(self, timeout=None):
        if self.finished is not None:
            return self.finished
        end = work_deadline(SINK_UNBLOCK + STREAM_JOIN if timeout is None else max(0.0, timeout))
        active = lambda: self.thread is not None and self.thread.is_alive()
        while active() and not self.connected and time.monotonic() < end:
            try:
                fd = os.open(self.fifo_name, os.O_WRONLY | os.O_NONBLOCK | os.O_CLOEXEC, dir_fd=self.dir_fd)
                try:
                    self.unblocked_by_runner = True
                finally:
                    os.close(fd)
                break
            except OSError as exc:
                if exc.errno != errno.ENXIO:
                    self.error = (self.error or "") + " unblock:" + repr(exc)
                    break
                time.sleep(min(SUPERVISE_SLICE, max(0.0, end - time.monotonic())))
        if self.thread is not None and self.thread.ident is not None:
            self.thread.join(max(0.0, min(STREAM_JOIN, end - time.monotonic())))
        alive = active()
        rec = {"fifo": self.fifo_path, "storage": "RAM only", "cap": self.cap, "connected": self.connected,
               "eof": self.eof, "received": self.received, "retained": self.retained, "discarded": self.discarded,
               "over_cap": self.over_cap, "error": self.error, "construction_error": self.construction_error,
               "unblocked_by_runner": self.unblocked_by_runner, "thread_alive_after_join": alive,
               "reader_fd_closed": self.reader_fd_closed, "sha256_of_retained": self.sha.hexdigest()}
        try:
            st = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False)
            rec["fifo_same_inode_still_fifo"] = stat.S_ISFIFO(st.st_mode) and [st.st_dev, st.st_ino] == self.fifo_identity
        except BaseException as exc:
            rec.update(fifo_same_inode_still_fifo=False, fifo_check_error=repr(exc))
        if not alive and self.construction_error is None:
            try:
                self.blocks = tuple(self.blocks)
                self.frozen_id = id(self.blocks)
                rec["blocks"] = len(self.blocks)
                rec["buffer_rehash"] = self.digest()
            except BaseException as exc:
                rec["buffer_rehash_error"] = repr(exc)
        rec["buffer_rehash_matches"] = rec.get("buffer_rehash") == [self.sha.hexdigest(), self.retained]
        rec["finish_deadline_in_bounds"] = time.monotonic() <= end
        rec["sink_settled"] = (not alive and self.error is None and self.construction_error is None
                               and rec["fifo_same_inode_still_fifo"] is True and rec["buffer_rehash_matches"] is True
                               and self.reader_fd_closed is True and rec["finish_deadline_in_bounds"] is True)
        if rec["sink_settled"] is not True:
            latch("proof buffer integrity/closure unproven: " + self.fifo_path)
        self.finished = rec
        return rec

    def release(self):
        """N6: drop this buffer's reference to its RAM blocks, but only once its collector thread has ended: a live
        collector keeps its blocks (it may still append) and stays charged; release is retried by the owner's
        finally and at closeout.  The bytes stay charged while any feeder still holds the frozen tuple.  Returns
        True iff released."""
        self.release_requested = True
        if self.thread is not None and self.thread.is_alive():
            return False
        self.released = True
        self.blocks = ()
        return True

    def holders(self):
        """V5: feeders that still hold this buffer's frozen tuple."""
        return [f.label for f in list(LIVE_FEEDERS) if f.blocks and self.frozen_id is not None
                and id(f.blocks) == self.frozen_id]

    def accounting(self):
        return {"fifo": self.fifo_path, "retained": self.retained, "released": self.released,
                "release_requested": self.release_requested,
                "collector_alive": self.thread is not None and self.thread.is_alive(),
                "thread_constructed": self.thread is not None, "thread_started": self.thread_started,
                "construction_error": self.construction_error, "reader_fd_closed": self.reader_fd_closed,
                "still_held_by_feeders": self.holders(), "frozen": self.frozen_id is not None,
                "finished": self.finished}

    def census_paths(self):
        return {self.fifo_path}

    def census_refusals(self, snap):
        v = snap.get(self.fifo_path)
        return [] if v is not None and v[0] == "fifo" and list(v[1:3]) == self.fifo_identity else ["proof FIFO identity drift"]

    def late_obligations(self):
        return [{"path": self.fifo_path, "kind": "fifo", "note": "native writer or runner collector may retain endpoint"},
                {"what": "RAM collector blocks", "bytes_known": self.retained, "note": "runner resources until exit"}]



class Feeder:
    """S2: owned writer of a frozen RAM proof buffer into ONE checker's stdin pipe; hashes/counts exactly the
    bytes os.write() accepted.  Modes: plain; suffix (C3: SUFFIX after the proof); hold (C7b: the first write
    waits until the checker was reaped).  The runner's read end is closed right after Popen (close_read);
    the write end is closed exactly once: by the thread, or by abandon() when the thread never started."""

    def __init__(self, blocks, mode="plain", label=""):
        if mode not in ("plain", "suffix", "hold"):
            raise RuntimeError("unknown feed mode %r" % (mode,))
        if not isinstance(blocks, tuple):
            raise RuntimeError("proof buffer not frozen")
        self.blocks, self.mode, self.label = blocks, mode, label
        self.expected = sum(len(b) for b in blocks)
        self.sha = hashlib.sha256()
        self.fed = self.proof_fed = 0
        self.delivery_error = self.exception = self.close_error = None
        self.hold = threading.Event()
        self.hold_released_by_event = None
        self.started = False
        self.finished = None
        self.thread = None
        self.rfd = self.wfd = None
        self.construction_error = None
        LIVE_FEEDERS.append(self)
        try:
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.rfd, self.wfd = os.pipe()
        except BaseException as exc:
            self.construction_error = repr(exc)
            self.abandon()
            latch("feeder construction unproven %r" % (exc,))
            raise

    def plan(self):
        return {"mode": self.mode, "buffer_bytes": self.expected, "blocks": len(self.blocks)}

    def close_read(self):
        fd, self.rfd = self.rfd, None
        if fd is not None:
            try:
                os.close(fd)
            except BaseException as exc:
                self.close_error = "read endpoint closure uncertain: %r" % (exc,)
                raise

    def start(self):
        try:
            self.thread.start()
        finally:
            self.started = self.thread is not None and self.thread.ident is not None

    def abandon(self):
        """Never-started feeder: close each still-open pipe end independently and drop the blocks.  V6: returns the
        close errors so that the caller incorporates them before any settlement is published."""
        errs = []
        for name in ("rfd", "wfd"):
            fd = getattr(self, name)
            setattr(self, name, None)
            if fd is not None:
                try:
                    os.close(fd)
                except OSError as exc:
                    errs.append("%s %r" % (name, exc))
        self.blocks = ()
        if errs:
            self.close_error = "; ".join(errs)
        return errs

    def _deliver(self, data):
        mv, off = memoryview(data), 0
        while off < len(mv):
            try:
                n = os.write(self.wfd, mv[off:off + WRITE_SLICE])
            except OSError as exc:
                self.delivery_error = "%s after %d fed bytes" % (
                    "EPIPE" if isinstance(exc, BrokenPipeError) else repr(exc), self.fed)
                return off, False
            if not isinstance(n, int) or n <= 0 or n > len(mv) - off:
                raise OSError(errno.EIO, "feeder write made no valid progress")
            self.sha.update(mv[off:off + n])
            off += n
            self.fed += n
        return off, True

    def _run(self):
        try:
            if self.mode == "hold":
                self.hold_released_by_event = self.hold.wait(HOLD_SECONDS)
            ok = True
            for b in self.blocks:
                k, ok = self._deliver(b)
                self.proof_fed += k
                if not ok:
                    break
            if ok and self.mode == "suffix":
                self._deliver(SUFFIX)
        except Exception as exc:
            self.exception = repr(exc)
        finally:
            fd, self.wfd = self.wfd, None
            if fd is not None:
                try:
                    os.close(fd)                   # EOF for the checker
                except OSError as exc:
                    self.close_error = repr(exc)

    def finish(self, timeout):
        """After the checker is reaped: release a held feed, bounded join, record; drops the shared blocks."""
        if self.finished is not None:
            return self.finished
        if self.started:
            self.hold.set()
            self.thread.join(timeout)
        alive = self.started and self.thread.is_alive()
        self.finished = {"mode": self.mode, "started": self.started, "buffer_bytes": self.expected,
                         "fed_bytes": self.fed, "fed_sha256": self.sha.hexdigest(), "proof_bytes_fed": self.proof_fed,
                         "undelivered_proof_bytes": self.expected - self.proof_fed,
                         "delivery_error": self.delivery_error, "exception": self.exception,
                         "close_error": self.close_error, "hold_released_by_event": self.hold_released_by_event,
                         "thread_alive_after_join": alive, "construction_error": self.construction_error,
                         "read_endpoint_closed": self.rfd is None, "write_endpoint_closed": self.wfd is None}
        if not alive:
            self.blocks = ()
        return self.finished


def new_filter():
    """S3: per-checker capture-filter state; V8: 'cont' = pass through until the next newline after an over-long
    partial line was flushed."""
    return {"raw_sha": hashlib.sha256(), "raw_bytes": 0, "raw_eof": False, "pending": b"", "header_clauses": None,
            "dup_low": 0, "dup_high": 0, "dup_bytes": 0, "tail": 0, "cont": False, "flushes": 0}


def open_wb(path):
    """G9: raw descriptor has a rollback owner until fdopen transfers it."""
    fd = create_excl(path)
    try:
        return os.fdopen(fd, "wb")
    except BaseException as exc:
        try:
            os.close(fd)
        finally:
            CREATED[path].update(state="failed", error="fdopen: %r" % (exc,))
        raise


def mkfifo_anchored(path):
    dfd, name = tree_path(path)
    os.mkfifo(name, 0o600, dir_fd=dfd)
    CREATED[path] = {"state": "open_fifo", "kind": "fifo", "identity": None}
    st = os.stat(name, dir_fd=dfd, follow_symlinks=False)
    CREATED[path] = {"state": "fifo", "kind": "fifo", "identity": [st.st_dev, st.st_ino]}
    return st


def work_deadline(seconds=CENSUS_SECONDS, deadline=None):
    end = time.monotonic() + seconds
    for x in (deadline, STATE.get("cleanup_deadline")):
        if x is not None:
            end = min(end, x)
    return end


def walk_bounded(root, root_fd=None, deadline=None):
    """G4: bounded incremental descriptor-relative walk; no whole-directory list before checking work caps.
    No symlink following; every fd/iterator has a finally owner. Exceeding depth/entry/time caps is uncertainty."""
    end = work_deadline(deadline=deadline)
    count = [0]
    snap = {}
    fd = os.dup(root_fd) if root_fd is not None else os.open(
        root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    def visit(dfd, base, depth):
        if depth > TREE_DEPTH_MAX:
            raise RuntimeError("census depth exceeds cap")
        with os.scandir(dfd) as entries:
            for entry in entries:
                count[0] += 1
                if count[0] > TREE_ENTRY_MAX or time.monotonic() > end:
                    raise RuntimeError("census entry/work deadline exhausted; incomplete")
                st = os.stat(entry.name, dir_fd=dfd, follow_symlinks=False)
                path = os.path.join(base, entry.name)
                snap[path] = census_entry(st)
                if stat.S_ISDIR(st.st_mode):
                    child = os.open(entry.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                                    dir_fd=dfd)
                    try:
                        fst = os.fstat(child)
                        if (fst.st_dev, fst.st_ino) != (st.st_dev, st.st_ino):
                            raise RuntimeError("directory replaced while walking: " + path)
                        visit(child, path, depth + 1)
                    finally:
                        os.close(child)
    try:
        visit(fd, root, 0)
    finally:
        os.close(fd)
    if time.monotonic() > end:
        raise RuntimeError("census completed beyond work deadline")
    return snap


def census_digest(root):
    snap = run_tree_census(root)
    raw = json.dumps(sorted((os.path.relpath(p, root), v) for p, v in snap.items()),
                     separators=(",", ":"), allow_nan=False).encode()
    st = os.lstat(root)
    return {"sha256": hashlib.sha256(raw).hexdigest(), "entries": len(snap), "root_identity": [st.st_dev, st.st_ino]}


def exe_identity(path, pin):
    """A2: hash a regular no-follow executable, binding file AND parent directory identities around the hash.
    Launch/settlement rechecks detect pathname replacement. This is not an atomic fexecve guarantee: the reviewed
    exclusive-writer premise for pinned binary directories is required; any observed drift blocks qualification."""
    parent = os.path.dirname(path)
    before, db = os.lstat(path), os.lstat(parent)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink < 1 or not stat.S_ISDIR(db.st_mode):
        raise RuntimeError("native executable not a regular direct file")
    digest, n = sha_file(path)
    after, da = os.lstat(path), os.lstat(parent)
    file_id = census_entry(before)
    dir_id = [db.st_dev, db.st_ino, db.st_mtime_ns, db.st_ctime_ns]
    if digest != pin or n != before.st_size or census_entry(after) != file_id             or [da.st_dev, da.st_ino, da.st_mtime_ns, da.st_ctime_ns] != dir_id:
        raise RuntimeError("native executable identity/pin changed: " + path)
    return {"path": path, "sha256": digest, "bytes": n, "file_identity": list(file_id), "parent_identity": dir_id}


def exe_refusals(binding):
    try:
        if not isinstance(binding, dict) or exe_identity(binding["path"], binding["sha256"]) != binding:
            return ["native executable identity/pin drift"]
        return []
    except BaseException as exc:
        return ["native executable unverifiable %r" % (exc,)]


def expected_binary_pin(path):
    if path == KISSAT[0]:
        return KISSAT[1]
    if path == DATE[0]:
        return DATE[1]
    if path == DRAT:
        return DRAT_OLD[1]
    for name, p, pin in CHECKERS:
        if p == path:
            return pin
    raise RuntimeError("unadmitted native executable " + path)


def load_verified_module(name, path, pin):
    """A2: execute exactly the already read and hash-verified bytes, never a pathname loader reopen."""
    raw = read_pinned(path, pin)
    mod = types.ModuleType(name)
    mod.__file__ = path
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


def receipt_contradictions(rec):
    """A7: literal True is not sufficient: every resource/reap/publication claim must agree."""
    if not isinstance(rec, dict):
        return ["receipt missing"]
    bad = []
    for key in ("settled", "actual_owned_reap", "group_empty_after_reap", "settlement_publication_in_bounds",
                "native_exec_identity_verified"):
        if rec.get(key) is not True:
            bad.append(key + " is not true")
    for key in ("stream_thread_alive_after_join", "quarantined", "stop_refused"):
        if rec.get(key) is not False:
            bad.append(key + " is not false")
    for key in ("reader_error", "wait_lost", "unsettled"):
        if key not in rec or rec[key] is not None:
            bad.append(key + " missing or not null")
    if rec.get("problems") != []:
        bad.append("problems not empty")
    if rec.get("resource_diagnostics") != []:
        bad.append("resource diagnostics missing/nonempty")
    if type(rec.get("returncode")) is not int:
        bad.append("return code missing/not exact integer")
    if not isinstance(rec.get("trips"), list):
        bad.append("trip inventory missing/not list")
    if not _hex64(rec.get("output_sha256")):
        bad.append("capture digest missing")
    return bad


def unresolved_inventory():
    """G1/G3/A5: derive retained ownership from ALL unproven states, never optional .unsettled presence.
    Threads/descriptors/RAM belong to the runner identity; runner end must be independently verified at release."""
    out = []
    for c in OWNED:
        if c.proc is None:
            continue
        rec = c.settled_rec
        child_open = (c.reader is not None and c.reader.is_alive()) or c.capture is None or not c.capture.closed \
                     or c.proc.stdout is None or not c.proc.stdout.closed
        if receipt_contradictions(rec) or child_open:
            out.append({"kind": "child", "seq": c.seq, "label": c.label, "pid": c.pid, "pgid": c.pgid,
                        "identity_at_start": c.identity_at_start, "started_by_epoch": c.started_epoch,
                        "actual_owned_reap": c.reaped, "wait_lost": c.wait_lost,
                        "known_identities": list(c.known_identities.values()), "live_census": c.last_census,
                        "census_uncertainty": list(c.census_uncertainty), "late_obligations": c.late_obligations(),
                        "receipt": c.quarantine_path, "receipt_state": c.quarantine_receipt_state,
                        "unknowns": receipt_contradictions(rec) + (["actual reader/endpoint still open"] if child_open else [])})
    for h in HELPERS:
        if h.proc is not None and (h.settled is not True or not h.reaped or h.wait_lost is not None
                                  or not h.group_closed_before_reap or h.census_uncertainty
                                  or h.proc.stdout is None or not h.proc.stdout.closed):
            out.append({"kind": "helper", "pid": h.pid, "pgid": h.pgid, "identity_at_start": h.identity_at_start,
                        "started_by_epoch": h.started_epoch, "record": h.record,
                        "known_identities": list(h.known_identities.values()), "live_census": h.last_census,
                        "census_uncertainty": list(h.census_uncertainty), "late_obligations": h.late_obligations()})
    for b in LIVE_BUFFERS:
        a = b.accounting()
        if a.get("collector_alive") is not False or a.get("released") is not True \
                or a.get("reader_fd_closed") is not True or a.get("construction_error") is not None \
                or (a.get("finished") or {}).get("sink_settled") is not True or b.blocks:
            out.append({"kind": "RAM collector", "runner_identity": STATE.get("runner_identity"), "state": a,
                        "late_obligations": b.late_obligations()})
    for f in LIVE_FEEDERS:
        alive = f.thread is not None and f.thread.is_alive()
        if alive or f.blocks or f.rfd is not None or f.wfd is not None or f.construction_error is not None \
                or f.close_error is not None:
            out.append({"kind": "stdin feeder", "runner_identity": STATE.get("runner_identity"), "label": f.label,
                        "thread_alive": alive, "retained_bytes": f.expected if f.blocks else 0,
                        "read_endpoint": f.rfd, "write_endpoint": f.wfd, "close_error": f.close_error,
                        "construction_error": f.construction_error})
    for s in LIVE_SINKS:
        a = s.accounting()
        if (s.finished or {}).get("sink_settled") is not True:
            out.append({"kind": "file sink", "runner_identity": STATE.get("runner_identity"), "state": a,
                        "late_obligations": s.late_obligations()})
    for path, state in CREATED.items():
        if state.get("state") not in ("complete", "fifo", "dir"):
            out.append({"kind": "partial publication", "path": path, "state": dict(state),
                        "runner_identity": STATE.get("runner_identity")})
    return out


def choose_exit_code(outcome, unresolved, cancel_before):
    if LATCH or unresolved:
        return EXIT_SAFETY_STOP
    if outcome.get("exception"):
        return EXIT_EXCEPTION
    if cancel_before:
        return EXIT_CANCELLED
    if outcome.get("sat"):
        return EXIT_SAT_CANDIDATE
    if outcome.get("controls_failed"):
        return EXIT_CONTROLS_FAILED
    if outcome.get("refused"):
        return EXIT_ADMISSION_REFUSED
    return EXIT_PLAN_COMPLETE if outcome.get("complete") else EXIT_EXCEPTION


class Owned:
    """G1-G4: one retained Popen, exclusive wait owner (SIGCHLD=SIG_DFL), non-reaping WNOWAIT
    observations and a real owned waitpid status. Popen.poll/wait are NEVER evidence. One verified SIGTERM;
    no escalation. UNSETTLED is irreversible and precedes every later observation/reap/census.
    An unreaped child anchors pid/pgid; a missing start identity NEVER wildcard-matches a live process."""

    def _owned_init(self):
        self.proc = self.pid = self.pgid = None
        self.identity_at_start = None
        self.launch_order = None
        self.stop = None
        self.term_sent_mono = self.term_sent_epoch = self.term_refused_mono = None
        self.term_delivery = None
        self.quarantined = False
        self.quarantine_receipt_state = "none"
        self.quarantine_path = None
        self.unsettled = None
        self.popen_call_mono = self.started_mono = self.started_epoch = None
        self.last_alive_mono = None
        self.exit_observed_mono = self.exit_observed_epoch = None
        self.exit_status = self.wait_status = None
        self.reaped = False
        self.wait_lost = None
        self.group_closed_before_reap = False
        self.known_identities = {}
        self.census_uncertainty = []
        self.last_census = None
        self.cleanup_end = None
        self.exe_binding = None
        self.argv_sha256 = None

    def stop_requested(self):
        return self.term_sent_mono is not None or self.term_refused_mono is not None

    def observe_exit(self):
        """WNOWAIT preserves leader/group identity until census closure and the explicit owned reap."""
        if self.quarantined or self.wait_lost is not None:
            return None
        if self.reaped:
            return self.exit_status
        if signal.getsignal(signal.SIGCHLD) != signal.SIG_DFL:
            self.wait_lost = "SIGCHLD disposition changed; exclusive wait premise lost"
            latch(self.wait_lost)
            return None
        try:
            info = os.waitid(os.P_PID, self.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT)
        except ChildProcessError as exc:
            self.wait_lost = "ECHILD: exclusive wait ownership lost: %r" % (exc,)
            latch(self.wait_lost)
            return None
        if info is None:
            return None
        if info.si_pid != self.pid or info.si_code not in (os.CLD_EXITED, os.CLD_KILLED, os.CLD_DUMPED):
            self.wait_lost = "unexpected waitid identity/status %r" % (info,)
            latch(self.wait_lost)
            return None
        self.exit_status = info.si_status if info.si_code == os.CLD_EXITED else -info.si_status
        if self.exit_observed_mono is None:
            self.exit_observed_mono, self.exit_observed_epoch = time.monotonic(), time.time()
        return self.exit_status

    def _reap_once(self):
        if self.quarantined or self.reaped or self.wait_lost is not None:
            return self.exit_status if self.reaped else None
        try:
            pid, status = os.waitpid(self.pid, os.WNOHANG)
        except ChildProcessError as exc:
            self.wait_lost = "ECHILD from owned waitpid (never normalized to rc0): %r" % (exc,)
            latch(self.wait_lost)
            return None
        if pid != self.pid:
            self.wait_lost = "waitid observed exit but owned waitpid did not reap this pid"
            latch(self.wait_lost)
            return None
        rc = os.waitstatus_to_exitcode(status)
        expected = self.exit_status
        self.wait_status, self.exit_status, self.reaped = status, rc, True
        self.proc.returncode = rc                 # real owned reap happened, even if observation contradicts it
        if expected is not None and rc != expected:
            self.wait_lost = "waitid/waitpid status contradiction"
            latch(self.wait_lost)
            return None
        return rc

    def verify_owned(self):
        if self.proc is None or self.reaped or self.wait_lost is not None or self.quarantined:
            return False, "no exclusive unreaped ownership"
        if signal.getsignal(signal.SIGCHLD) != signal.SIG_DFL:
            return False, "SIGCHLD disposition changed"
        ident0 = self.identity_at_start
        if not isinstance(ident0, dict) or not ident0.get("start"):
            return False, "required complete start identity unknown; no signal even to an owned fast-exit group"
        exited = self.observe_exit()
        if self.wait_lost is not None:
            return False, self.wait_lost
        if exited is not None:
            if self.pid in list_pids(PROC_PGRP_ONLY, self.pgid) and self.pgid == self.pid:
                return True, "WNOWAIT kernel-owned exited leader anchors its own group (not a start wildcard)"
            return False, "owned exited leader absent from its anchored group"
        ident, err = bsd_identity(self.pid)
        if ident is not None and ident.get("pid") == self.pid and ident.get("pgid") == self.pgid == self.pid \
                and ident.get("ppid") == os.getpid() and ident.get("start") == ident0.get("start"):
            return True, "live pid/ppid/pgid/start re-verified"
        if self.observe_exit() is not None and self.wait_lost is None \
                and self.pid in list_pids(PROC_PGRP_ONLY, self.pgid):
            return True, "leader exited during check; WNOWAIT retains exact kernel ownership"
        return False, "live identity unavailable/mismatched %r %r" % (ident, err)

    def term(self, reason):
        if self.stop is None:
            self.stop = reason
        if self.proc is None or self.stop_requested() or self.quarantined or self.reaped:
            return
        try:
            ok, evidence = self.verify_owned()
        except BaseException as exc:
            ok, evidence = False, repr(exc)
        if not ok:
            self.term_refused_mono = time.monotonic()
            self.term_delivery = {"delivered": False, "refused": evidence}
            latch("stop refused for pid %s: %s; parent block" % (self.pid, evidence))
            return
        self.term_sent_mono, self.term_sent_epoch = time.monotonic(), time.time()
        try:
            KILLPG(self.pgid, signal.SIGTERM)
            self.term_delivery = {"delivered": True, "pgid": self.pgid, "evidence": evidence}
        except OSError as exc:
            self.term_delivery = {"delivered": False, "pgid": self.pgid, "error": repr(exc), "evidence": evidence}

    def late_obligations(self):
        return [{"what": "runner-owned stdout read endpoint", "note": "closes at runner exit; survivor may see EPIPE"}]

    def live_census(self):
        """Complete within LIST_SLOTS/work bounds, exact identities; uncertainty is durable, never truncated."""
        if self.quarantined:
            return self.last_census or {"complete": False, "unknown": "UNSETTLED before census completed"}
        out = {"leader_pid": self.pid, "pgid": self.pgid, "at_epoch": time.time(), "complete": True,
               "start_identity": self.identity_at_start, "group_members": [], "descendants": []}
        try:
            census_end = work_deadline()
            if self.cleanup_end is not None:
                census_end = min(census_end, self.cleanup_end)
            members = list_pids(PROC_PGRP_ONLY, self.pgid)
            found = descendants(self.pid, self.pgid, census_end)
            for key, pids in (("group_members", members), ("descendants", found)):
                for p in pids:
                    if time.monotonic() > census_end:
                        raise RuntimeError("exact identity census work allowance exhausted")
                    ident, err = bsd_identity(p)
                    if ident is None and p == self.pid and isinstance(self.identity_at_start, dict) \
                            and self.identity_at_start.get("start"):
                        # Kernel-exclusive unreaped ownership rules out PID reuse; retain exact established start,
                        # while preserving the failed live read separately. Never substitute for a nonleader.
                        ident = dict(self.identity_at_start, live_read_unavailable=True)
                    item = {"pid": p, "identity": ident, "identity_error": err, "rss_bytes": task_rss(p),
                            "observed_by_epoch": out["at_epoch"]}
                    out[key].append(item)
                    self.known_identities[p] = item
                    # Own zombie leader is proved by WNOWAIT; any other unreadable identity remains uncertain.
                    if ident is None and p != self.pid:
                        out["complete"] = False
            if not out["complete"]:
                self.census_uncertainty.append("unreadable nonleader census identity")
        except BaseException as exc:
            out.update(complete=False, census_error=repr(exc))
            self.census_uncertainty.append(repr(exc))
        self.last_census = out
        return out

    def _unsettled_receipt(self):
        return {"schema": "PA19-UNSETTLED-v2", "pid": self.pid, "pgid": self.pgid, "argv": self.argv,
                "identity_at_start": self.identity_at_start, "started_by_epoch": self.started_epoch,
                "argv_sha256": self.argv_sha256,
                "stop": self.stop, "term_delivery": self.term_delivery, "settlement": "UNSETTLED",
                "actual_owned_reap": self.reaped, "wait_lost": self.wait_lost,
                "known_identities": list(self.known_identities.values()), "live_census": self.last_census,
                "census_uncertainty": list(self.census_uncertainty), "late_obligations": self.late_obligations(),
                "reservation": "retained; NEW parent disposition required", "runner_action": "return, no further wait/signal"}

    def _receipt_valid(self):
        try:
            return json.loads(read_tree(self.quarantine_path, RECORD_MAX)) == self.unsettled
        except BaseException:
            return False

    def _record_unsettled(self, reason="bounded settlement unproven"):
        if self.quarantined:
            return
        # Irreversible BEFORE any publication. No new poll, wait or census is permitted after this assignment.
        self.quarantined = True
        self.census_uncertainty.append(str(reason))
        latch("UNSETTLED pid %s: %s; reservation retained" % (self.pid, reason))
        self.unsettled = self._unsettled_receipt()
        if self.quarantine_path is None:
            self.quarantine_receipt_state = "unpublishable: no anchored tree"
            return
        try:
            write_x(self.quarantine_path, self.unsettled)
            self.quarantine_receipt_state = "written"
        except FileExistsError:
            self.quarantine_receipt_state = "written" if self._receipt_valid() else "contradictory existing receipt"
        except BaseException as exc:
            self.quarantine_receipt_state = "failed: %r" % (exc,)

    def reap_owned(self, term_wait):
        if self.quarantined:                       # G4: before ALL observations, including cached Popen state
            return None
        if self.reaped:
            return self.exit_status
        end = work_deadline(term_wait, self.cleanup_end)
        t0 = self.term_sent_mono if self.term_sent_mono is not None else self.term_refused_mono
        if t0 is not None:
            end = min(end, t0 + term_wait)
        self.cleanup_end = min(self.cleanup_end, end) if self.cleanup_end is not None else end
        while time.monotonic() < end:
            try:
                census = self.live_census()        # G3: capture group/descendants BEFORE any reap
                rc = self.observe_exit()
                if self.wait_lost is not None:
                    break
                others = [x for x in census.get("group_members", []) if x["pid"] != self.pid]
                if rc is not None and census.get("complete") is True and not others \
                        and not census.get("descendants"):
                    self.group_closed_before_reap = True
                    result = self._reap_once()
                    if result is not None:
                        return result
                    break
                if self.stop is None:
                    self.stop = "nonleader_resources" if rc is not None else "reap_of_live_owner"
                if not self.stop_requested():
                    self.term(self.stop)
                time.sleep(min(SUPERVISE_SLICE, max(0.0, end - time.monotonic())))
            except BaseException as exc:
                self.census_uncertainty.append("reap: %r" % (exc,))
                if time.monotonic() < end:
                    time.sleep(min(SUPERVISE_SLICE, max(0.0, end - time.monotonic())))
        self._record_unsettled("finite grace exhausted or wait/census ownership unproven")
        return None


class HelperRefused(Exception):
    pass


class Helper(Owned):
    """Owned pinned /bin/date. Every launch has durable intent/identity evidence; no helper overlaps an unproven
    native owner. Common frozen cutoffs rechecked after pinning, intent publication, observations and settlement."""

    def __init__(self, argv):
        self._owned_init()
        self.argv = argv
        self.argv_sha256 = hashlib.sha256(json.dumps(argv, separators=(",", ":")).encode()).hexdigest()
        self.settled = False
        self.out = bytearray()
        self.out_total = 0
        self.eof = False
        self.record = {"argv": argv}
        self.intent_path = self.launch_path = None

    def admission_refusals(self):
        why = []
        if LATCH:
            why.append("latch held")
        if cancelled():
            why.append("cancel stamped")
        if any(c.proc is not None and ((c.settled_rec or {}).get("settled") is not True
                or (c.reader is not None and c.reader.is_alive()) or c.capture is None or not c.capture.closed
                or c.proc.stdout is None or not c.proc.stdout.closed) for c in OWNED) \
                or any(h is not self and h.proc is not None and h.settled is not True for h in HELPERS):
            why.append("an owned process is not affirmatively settled")
        m, e = time.monotonic(), time.time()
        if STATE["mono_end"] is not None and (m + HELPER_ALLOW > STATE["mono_end"]
                or e + HELPER_ALLOW > STATE["abs_end"] or m + HELPER_ALLOW > STATE["mono_chunk_end"]):
            why.append("helper allowance does not fit frozen cutoffs")
        return why

    def run(self):
        if self.argv != DATE_ARGV:
            raise HelperRefused("only the exact pinned date argv is admitted")
        self.exe_binding = exe_identity(self.argv[0], DATE[1])
        why = self.admission_refusals()            # AFTER blocking executable hash
        if why:
            raise HelperRefused("; ".join(why))
        HELPERS.append(self)
        self.launch_order = next(ORDER)
        d = None if STATE["out"] is None else os.path.join(STATE["out"], "children")
        if d in TREE:
            base = os.path.join(d, "helper-%04d" % self.launch_order)
            self.intent_path, self.launch_path = base + ".intent.json", base + ".launch.json"
            self.quarantine_path = base + ".QUARANTINE.json"
            write_x(self.intent_path, {"schema": "PA19-OWNER-INTENT-v1", "launch_order": self.launch_order,
                                      "argv": self.argv, "argv_sha256": self.argv_sha256, "kind": "helper", "runner_identity": STATE.get("runner_identity")})
        why = exe_refusals(self.exe_binding) + self.admission_refusals()
        if why:
            self.record.update(no_launch=True, refused=why)
            if self.intent_path is not None:
                write_x(self.intent_path.replace(".intent.json", ".nolaunch.json"), self.record)
            raise HelperRefused("; ".join(why))
        self.popen_call_mono = time.monotonic()
        try:
            self.proc = subprocess.Popen(self.argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, start_new_session=True, close_fds=True,
                                         env=CHILD_ENV)
        except BaseException as exc:
            self.record.update(no_launch=True, popen_error=repr(exc))
            if self.intent_path is not None:
                write_x(self.intent_path.replace(".intent.json", ".nolaunch.json"), self.record)
            raise
        rc = None
        try:
            self.pid = self.pgid = self.proc.pid
            self.started_mono, self.started_epoch = time.monotonic(), time.time()
            self.identity_at_start = identity_checked(self.pid, os.getpid())
            if self.launch_path is not None:
                write_x(self.launch_path, {"kind": "helper", "pid": self.pid, "pgid": self.pgid,
                                          "identity": self.identity_at_start, "started_by_epoch": self.started_epoch,
                                          "launch_order": self.launch_order, "exe_binding": self.exe_binding,
                                          "argv": self.argv, "argv_sha256": self.argv_sha256})
            drift = exe_refusals(self.exe_binding)
            if drift:
                raise RuntimeError(drift)
            self._supervise_and_capture()
        except BaseException as exc:
            self.record["exception"] = repr(exc)
            self.stop = self.stop or "helper_exception"
        finally:
            self.cleanup_end = work_deadline(HELPER_TERM_WAIT)
            rc = self.reap_owned(HELPER_TERM_WAIT)
            try:
                self.proc.stdout.close()
            except BaseException as exc:
                self.record["stdout_close_error"] = repr(exc)
        return self._settle(rc)

    def _supervise_and_capture(self):
        fd = self.proc.stdout.fileno()
        end = self.popen_call_mono + HELPER_WALL
        hard_end = end + HELPER_TERM_WAIT
        peak = 0
        while time.monotonic() <= hard_end:
            self.live_census()                    # before observing the exit; failures remain durable
            alive = self.observe_exit() is None
            m, e = time.monotonic(), time.time()
            reasons = []
            if cancelled():
                reasons.append("owner_cancel_sigterm")
            if m > end or (STATE["mono_end"] is not None and (m > STATE["mono_end"] or e > STATE["abs_end"])):
                reasons.append("helper_wall_or_cutoff")
            if self.out_total > HELPER_OUT_CAP:
                reasons.append("helper_output_cap")
            if self.census_uncertainty:
                reasons.append("helper_census_uncertain")
            if any(p != self.pid for p in self.known_identities):
                reasons.append("helper_descendant")
            if alive:
                rss_h, rss_r = task_rss(self.pid), task_rss(os.getpid())
                if rss_r is None or (rss_h is None and self.observe_exit() is None):
                    reasons.append("helper_rss_unreadable")
                else:
                    peak = max(peak, (rss_h or 0) + rss_r)
                    if peak > LANE_RSS_TRIP:
                        reasons.append("helper_lane_rss")
            if reasons:
                self.record.setdefault("trips", []).extend(reasons)
                self.term(reasons[0])
                break
            if self.eof and not alive:
                break
            if not self.eof:
                ready, _w, _x = select.select([fd], [], [], min(SUPERVISE_SLICE, max(0.0, hard_end - m)))
                if ready:
                    b = os.read(fd, min(65536, HELPER_OUT_CAP + 1))
                    if not b:
                        self.eof = True
                    else:
                        self.out_total += len(b)
                        self.out += b[:max(0, HELPER_OUT_CAP + 1 - len(self.out))]
            else:
                time.sleep(SUPERVISE_SLICE)
        self.record["peak_rss_bytes"] = peak

    def _settle(self, rc):
        problems = []
        if not self.reaped or rc is None or self.wait_lost is not None:
            problems.append("actual owned reap unproven")
        if not isinstance(self.identity_at_start, dict) or not self.identity_at_start.get("start"):
            problems.append("required helper full start identity unproven; no timestamp qualifies")
        if self.quarantined or self.term_refused_mono is not None:
            problems.append("UNSETTLED or unverifiable stop")
        if not self.group_closed_before_reap or self.census_uncertainty:
            problems.append("group/descendant census closure unproven")
        if any(p != self.pid for p in self.known_identities):
            problems.append("nonleader process observed")
        if self.record.get("stdout_close_error"):
            problems.append("stdout endpoint closure unproven")
        native_drift = exe_refusals(self.exe_binding)
        invalid = list(native_drift)
        if self.stop is not None or not self.eof or self.out_total > HELPER_OUT_CAP or rc != 0 \
                or DATE_RE.fullmatch(bytes(self.out)) is None:
            invalid.append("stopped/incomplete/invalid required host clock")
        done, epoch = time.monotonic(), time.time()
        if self.exit_observed_mono is None or self.exit_observed_mono > self.popen_call_mono + HELPER_WALL \
                or done > self.popen_call_mono + HELPER_ALLOW \
                or (STATE["abs_end"] is not None and (epoch > STATE["abs_end"] or done > STATE["mono_end"])):
            invalid.append("helper observed completion outside frozen bounds")
        self.settled = not problems
        self.record.update(pid=self.pid, pgid=self.pgid, launch_order=self.launch_order, rc=rc,
                           settled=self.settled, problems=problems, unsettled=problems, invalid=invalid,
                           identity=self.identity_at_start, actual_owned_reap=self.reaped, wait_lost=self.wait_lost,
                           known_identities=list(self.known_identities.values()), live_census=self.last_census,
                           census_uncertainty=list(self.census_uncertainty),
                           group_empty_after_reap=self.group_closed_before_reap, eof=self.eof,
                           exe_binding=self.exe_binding, exe_identity_ok=not native_drift,
                           out_bytes=self.out_total, term_delivery=self.term_delivery,
                           settled_after_launch_s=done - self.popen_call_mono)
        HELPER_LOG.append(self.record)
        if not self.settled:
            self._record_unsettled("helper resources/census unproven: %r" % problems)
            raise RuntimeError("metadata helper not settled")
        if invalid:
            if self.stop == "owner_cancel_sigterm":
                raise HelperRefused("settled helper cancelled; required clock unavailable")
            latch("metadata helper invalid: %r" % invalid)
            raise RuntimeError("required host clock invalid")
        return bytes(self.out).decode("ascii").strip()



class Child(Owned):
    """One owned native child: pre-allocated ownership, V7 launch/cancel boundary, own session, HARD capped capture
    created through the anchored run tree (N8), V4/N8 complete run-tree census before admission and after
    settlement, V6 independent descriptor cleanup, N1 identity-verified single group SIGTERM (Owned), N4 timing
    evidence: settled only if the settlement completes within its frozen tail; qualifying only if the exit was
    observed by the child's deadline; B1: a survivor of the bounded stop grace is recorded UNSETTLED (identities,
    live census, late obligations) and never waited for again."""

    def __init__(self, argv, label, wall, reserve, inputs, sink, cwd, feeder=None):
        self._owned_init()
        STATE["seq"] += 1
        self.seq = STATE["seq"]
        self.argv, self.label, self.sink_obj, self.cwd = argv, label, sink, cwd
        self.argv_sha256 = hashlib.sha256(json.dumps(argv, separators=(",", ":")).encode()).hexdigest()
        self.feeder = feeder
        self.filt = None if feeder is None else new_filter()
        base = os.path.join(STATE["out"], "children", "%02d-%s" % (self.seq, label))
        self.out_path, self.launch_path, self.settle_path = base + ".out", base + ".launch.json", base + ".settle.json"
        self.intent_path, self.nolaunch_path = base + ".intent.json", base + ".nolaunch.json"
        self.quarantine_path = base + ".QUARANTINE.json"
        self.captured = self.capture_written = 0
        self.over_cap, self.reader_error = False, None
        self.reader = self.capture = self.settled_rec = None
        self.descendants = []
        self.inputs, self.reserve = inputs, reserve
        self.refused = None
        self.fd_errors = []
        self.trips = []
        self.cleanup_started = False
        charge_output(LOG_CAP)
        self.capture = open_wb(self.out_path)
        try:
            self.tree_before = run_tree_census()
            self.exe_binding = exe_identity(argv[0], expected_binary_pin(argv[0]))
            now, mono = time.time(), time.monotonic()
            self.deadline = min(now + wall + GRACE, STATE["abs_end"] - SETTLE_TAIL)
            self.deadline_mono = min(mono + wall + GRACE, STATE["mono_end"] - SETTLE_TAIL)
            preparing = {self.out_path}
            if sink is not None:
                preparing.update(sink.census_paths())
            why = full_admission(reserve, self.deadline, self.deadline_mono)
            why += preservation_refusals(exclude=preparing)
            if why:
                self.refused = why
                self._close_refused_capture()
                return
            OWNED.append(self)                    # retain ALL acquired owner states, including launch failure
            self.launch_order = next(ORDER)
            write_x(self.intent_path, {"schema": "PA19-OWNER-INTENT-v1", "kind": "child", "seq": self.seq,
                                       "label": label, "argv": argv, "argv_sha256": self.argv_sha256, "launch_order": self.launch_order,
                                       "runner_identity": STATE["runner_identity"], "exe_binding": self.exe_binding})
            # Hashing/admission/intent are blocking; actual spawn boundary rechecks all frozen timing.
            why = exe_refusals(self.exe_binding)
            if LATCH or cancelled() or time.time() > NATIVE_LAUNCH_STOP or time.time() + wall > self.deadline \
                    or time.monotonic() + wall > self.deadline_mono:
                why.append("latch/cancel/remaining allowance at actual spawn boundary")
            if why:
                self.refused = why
                write_x(self.nolaunch_path, {"no_launch": True, "why": why, "launch_order": self.launch_order})
                self._close_refused_capture()
                return
            self.popen_call_mono = time.monotonic()
            child_env = dict(CHILD_ENV, TMPDIR=cwd)
            try:
                self.proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL if feeder is None else feeder.rfd,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                             start_new_session=True, close_fds=True, cwd=cwd, env=child_env)
            except BaseException as exc:
                write_x(self.nolaunch_path, {"no_launch": True, "popen_error": repr(exc),
                                           "launch_order": self.launch_order})
                raise
            self.pid = self.pgid = self.proc.pid   # before ANY other fallible step
            self.started_mono, self.started_epoch = time.monotonic(), time.time()
            if feeder is not None:
                feeder.close_read()
            self.identity_at_start = identity_checked(self.pid, os.getpid())
            write_x(self.launch_path, {"seq": self.seq, "kind": "child", "label": label, "pid": self.pid,
                                       "pgid": self.pgid, "identity": self.identity_at_start,
                                       "started_by_epoch": self.started_epoch, "argv": argv, "argv_sha256": self.argv_sha256, "cwd": cwd,
                                       "launch_order": self.launch_order, "runner_identity": STATE["runner_identity"],
                                       "exe_binding": self.exe_binding, "absolute_deadline_epoch": self.deadline,
                                       "elapsed_deadline_s": self.deadline_mono - STATE["mono0"],
                                       "capture": self.out_path, "capture_cap": LOG_CAP, "inputs": inputs,
                                       "go": STATE["go"], "run_launch_record": STATE["run_record"],
                                       "stdin_feed": None if feeder is None else feeder.plan()})
            if exe_refusals(self.exe_binding):
                raise RuntimeError("native executable changed across actual exec boundary")
            self.reader = threading.Thread(target=self._read, daemon=True)
            self.reader.start()
            if feeder is not None:
                feeder.start()
            print("CHILD_LAUNCH", self.launch_path, flush=True)
        except BaseException as exc:
            if self.proc is None:
                self._close_refused_capture()
            else:
                self.stop = self.stop or "registration_failure"
                if feeder is not None and not feeder.started:
                    self.fd_errors += feeder.abandon()
                latch("post-Popen registration failure %r" % (exc,))
                # caller's finally owns settlement; never repeat a wait from this constructor
            raise

    def _close_refused_capture(self):
        if self.capture is None:
            return
        try:
            self.capture.close()
            digest, n = sha_tree(self.out_path, limit=LOG_CAP)
            register_written(self.out_path, digest, n)
        except BaseException as exc:
            self.fd_errors.append("refused capture cleanup %r" % (exc,))
            CREATED[self.out_path].update(state="failed", error=repr(exc))
            latch("refused capture publication/closure unproven %r" % (exc,))

    def _keep(self, b):
        room = LOG_CAP - self.capture_written
        if room > 0:
            chunk = b[:room]
            n = self.capture.write(chunk)
            if n != len(chunk):
                raise OSError(errno.EIO, "capture write incomplete")
            self.capture_written += n
        self.captured += len(b)
        if self.captured > LOG_CAP:
            self.over_cap = True

    def _read(self):
        """Capped capture.  S3: for a checker child the raw stream is hashed/counted in-stream and ONLY lines that
        fullmatch DUP_LINE at a genuine line start are dropped (counted by phase and bytes); V8: after an over-long
        partial line is flushed, the rest of that physical line is kept unconditionally."""
        f = self.filt
        try:
            while True:
                b = self.proc.stdout.read1(65536)
                if not b:
                    if f is not None:
                        f["raw_eof"] = True
                    break
                if f is None:
                    self._keep(b)
                    continue
                f["raw_sha"].update(b)
                f["raw_bytes"] += len(b)
                parts = (f["pending"] + b).split(b"\n")
                f["pending"] = parts.pop()
                for ln in parts:
                    ln += b"\n"
                    if f["cont"]:                  # V8: tail of a flushed physical line, never a whole line
                        f["cont"] = False
                        self._keep(ln)
                        continue
                    m = DUP_LINE.fullmatch(ln)
                    if m is None:
                        hm = PARSE_LINE.fullmatch(ln)
                        if hm is not None and f["header_clauses"] is None:
                            f["header_clauses"] = int(hm.group(2))
                        self._keep(ln)
                        continue
                    f["dup_bytes"] += len(ln)
                    if f["header_clauses"] is not None and int(m.group(3)) <= f["header_clauses"]:
                        f["dup_low"] += 1
                    else:
                        f["dup_high"] += 1
                if len(f["pending"]) > PENDING_MAX:
                    self._keep(f["pending"])
                    f["pending"] = b""
                    f["cont"] = True
                    f["flushes"] += 1
            if f is not None and f["pending"]:
                f["tail"] = len(f["pending"])
                self._keep(f["pending"])
                f["pending"] = b""
        except Exception as exc:
            self.reader_error = repr(exc)
        finally:
            for what, fn in (("flush", self.capture.flush), ("fsync", lambda: os.fsync(self.capture.fileno())),
                             ("capture close", self.capture.close), ("stdout close", self.proc.stdout.close)):
                try:
                    fn()                           # V6: every cleanup step independent
                except Exception as exc:
                    self.reader_error = (self.reader_error or "") + " %s:%r" % (what, exc)

    def late_obligations(self):
        out = [{"path": self.cwd, "kind": "dir", "note": "native cwd/TMPDIR may gain entries"},
               {"path": self.out_path, "kind": "file", "note": "runner capture writer may still own it"},
               {"what": "stdout/stderr read endpoint", "note": "closes at runner exit"}]
        if self.feeder is not None:
            out.append({"what": "checker stdin endpoints and retained RAM blocks", "note": "runner-owned until exit"})
        if self.sink_obj is not None:
            out.extend(self.sink_obj.late_obligations())
        return out

    def alive(self):
        return self.observe_exit() is None

    def census(self):
        if self.quarantined:
            raise RuntimeError("irreversible UNSETTLED: no further process census")
        snap = self.live_census()
        if snap.get("complete") is not True:
            raise RuntimeError("owned census incomplete")
        found = sorted(p for p in self.known_identities if p != self.pid)
        rss = task_rss(self.pid)
        for p in found:
            r = task_rss(p)
            rss = None if rss is None or r is None else rss + r
        return found, rss

    def timing(self):
        # A10: qualification consumes raw monotonic values; display rounding NEVER feeds a predicate.
        rel = lambda t: None if t is None else t - STATE["mono0"]
        return {"popen_call_s": rel(self.popen_call_mono), "started_s": rel(self.started_mono),
                "last_alive_s": rel(self.last_alive_mono), "exit_observed_s": rel(self.exit_observed_mono),
                "deadline_s": rel(self.deadline_mono), "exit_observed_epoch": self.exit_observed_epoch,
                "deadline_epoch": self.deadline}

    def settle(self):
        """G3-G5/A3: idempotent cleanup under ONE common remaining deadline. No stage repeats a prior wait.
        Receipt is PROVISIONAL; only the in-memory result after fsync/close/directory-fsync can become settled.
        Later authoritative closeout + parent's observed exit binds every qualified receipt/publication."""
        if self.settled_rec is not None:
            return self.settled_rec
        if self.cleanup_started:
            self._record_unsettled("settlement stage previously escaped; never repeat cleanup waits")
            self.settled_rec = {"seq": self.seq, "label": self.label, "pid": self.pid, "settled": False,
                                "unsettled": self.unsettled, "problems": ["incomplete earlier cleanup"]}
            return self.settled_rec
        self.cleanup_started = True
        self.cleanup_end = min(time.monotonic() + SETTLE_TAIL, self.deadline_mono + SETTLE_TAIL)
        previous_end = STATE.get("cleanup_deadline")
        STATE["cleanup_deadline"] = self.cleanup_end
        problems, diag = [], []
        rc = sink_rec = feed_rec = filt_rec = out_sha = None
        stream_alive = None
        publication = None
        def stage(label, fn, default=None):
            try:
                if time.monotonic() > self.cleanup_end:
                    raise RuntimeError("common cleanup deadline exhausted")
                return fn()
            except BaseException as exc:
                problems.append("%s: %r" % (label, exc))
                return default
        def remaining(cap):
            return max(0.0, min(cap, self.cleanup_end - time.monotonic()))
        try:
            total_cleanup_end = self.cleanup_end
            rc = stage("owned reap", lambda: self.reap_owned(TERM_WAIT))
            self.cleanup_end = total_cleanup_end
            if not self.reaped or rc is None or self.wait_lost is not None:
                problems.append("actual owned reap unproven")
            if not isinstance(self.identity_at_start, dict) or not self.identity_at_start.get("start"):
                problems.append("required full launch start identity unproven (fast exit cannot qualify)")
            if self.quarantined or self.term_refused_mono is not None:
                problems.append("irreversible UNSETTLED or refused stop")
            if self.reader is not None and self.reader.ident is not None:
                stage("capture join", lambda: self.reader.join(remaining(STREAM_JOIN)))
                stream_alive = self.reader.is_alive()
            else:
                problems.append("capture reader never started")
                stage("stdout close", self.proc.stdout.close)
                stage("capture close", self.capture.close)
            if stream_alive is not False:
                problems.append("capture writer closure unproven")
            if self.reader_error is not None:
                problems.append("capture reader error %s" % self.reader_error)
            if self.feeder is not None:
                if not self.feeder.started:
                    self.fd_errors += self.feeder.abandon()
                feed_rec = stage("stdin feeder finish", lambda: self.feeder.finish(remaining(STREAM_JOIN)))
                if not isinstance(feed_rec, dict) or feed_rec.get("started") is not True \
                        or feed_rec.get("thread_alive_after_join") is not False \
                        or feed_rec.get("exception") is not None or feed_rec.get("close_error") is not None:
                    problems.append("stdin feeder ownership unproven")
                if stream_alive is False:
                    f = self.filt
                    filt_rec = {"raw_bytes": f["raw_bytes"], "raw_sha256": f["raw_sha"].hexdigest(),
                                "raw_eof": f["raw_eof"], "header_clauses": f["header_clauses"],
                                "dup_bytes_dropped": f["dup_bytes"],
                                "dup_lines_at_or_below_header_clauses": f["dup_low"],
                                "dup_lines_above_header_clauses": f["dup_high"],
                                "nondropped_bytes": self.captured, "capture_file_bytes": self.capture_written,
                                "unterminated_tail_bytes": f["tail"], "over_long_line_flushes": f["flushes"]}
            if self.fd_errors:
                problems.append("descriptor close errors %r" % self.fd_errors)
            if not self.group_closed_before_reap or self.census_uncertainty:
                problems.append("complete pre-reap group/descendant closure unproven")
            if any(p != self.pid for p in self.known_identities) or self.descendants:
                problems.append("unexpected nonleader ownership observed")
            if self.sink_obj is not None:
                sink_rec = stage("proof collector finish", lambda: self.sink_obj.finish(remaining(STREAM_JOIN + SINK_UNBLOCK)))
                if not isinstance(sink_rec, dict) or sink_rec.get("sink_settled") is not True:
                    problems.append("proof collector integrity/closure unproven")
            cwd_tree = stage("cwd census", lambda: walk_bounded(self.cwd), None)
            if cwd_tree is None or cwd_tree:
                problems.append("cwd nonempty or census incomplete")
            now = stage("run-tree census", run_tree_census)
            if now is not None:
                expected = {self.out_path, self.intent_path, self.nolaunch_path, self.launch_path,
                            self.settle_path, self.quarantine_path}
                if self.sink_obj is not None:
                    expected.update(self.sink_obj.census_paths())
                    problems += self.sink_obj.census_refusals(now)
                changed = [p for p in set(now) | set(self.tree_before)
                           if p not in expected and now.get(p) != self.tree_before.get(p)]
                if changed:
                    problems.append("unexpected run-tree changes %r" % changed)
            problems += confinement_refusals()
            if stream_alive is False:
                out_pair = stage("capture hash", lambda: sha_tree(self.out_path, limit=LOG_CAP))
                if out_pair is not None and out_pair[1] == self.capture_written:
                    out_sha = out_pair[0]
                    register_written(self.out_path, out_sha, out_pair[1])
                    text = stage("capture diagnostic scan", lambda: read_tree(self.out_path, LOG_CAP).decode("utf-8", "replace"))
                    if text is not None:
                        diag = sorted(set(m.group(0) for m in RESOURCE_DIAG.finditer(text)))
                else:
                    problems.append("capture digest/byte identity unproven")
            native_drift = exe_refusals(self.exe_binding)
            problems += native_drift
            if self.over_cap:
                latch("capture hard cap exceeded on " + self.label)
            if diag:
                latch("native memory diagnostic in %s: %r" % (self.label, diag))
            exit_by = (self.exit_observed_mono is not None and self.exit_observed_epoch is not None
                       and self.exit_observed_mono <= self.deadline_mono and self.exit_observed_epoch <= self.deadline)
            m, e = time.monotonic(), time.time()
            if m > self.cleanup_end or e > self.deadline + SETTLE_TAIL:
                problems.append("cleanup work outside common frozen deadline")
            rec = {"seq": self.seq, "label": self.label, "pid": self.pid, "pgid": self.pgid,
                   "identity_at_start": self.identity_at_start, "argv": self.argv, "returncode": rc,
                   "stop": self.stop or "self", "trips": list(self.trips), "term_delivery": self.term_delivery,
                   "stop_refused": self.term_refused_mono is not None, "unsettled": self.unsettled,
                   "actual_owned_reap": self.reaped, "wait_lost": self.wait_lost,
                   "known_identities": list(self.known_identities.values()), "live_census": self.last_census,
                   "census_uncertainty": list(self.census_uncertainty),
                   "seconds": e - self.started_epoch, "timing": self.timing(),
                   "exit_observed_by_deadline": exit_by, "launch_order": self.launch_order,
                   "cancel_order": STATE["cancel_order"], "nondropped_bytes": self.captured,
                   "capture_file_bytes": self.capture_written, "capture_over_cap": self.over_cap,
                   "reader_error": self.reader_error, "stream_thread_alive_after_join": stream_alive,
                   "group_empty_after_reap": self.group_closed_before_reap, "quarantined": self.quarantined,
                   "problems": problems, "resource_diagnostics": diag, "proof_sink": sink_rec,
                   "stdin_feed": feed_rec, "stdout_filter": filt_rec, "exe_binding": self.exe_binding,
                   "native_exec_identity_verified": not native_drift,
                   "launch_record": self.launch_path, "output_path": self.out_path, "output_sha256": out_sha,
                   "settled": False, "settlement_publication_in_bounds": False,
                   "authority": "PROVISIONAL until observed publication and run closeout + parent exit audit"}
            ok = stream_alive is False and self.group_closed_before_reap and self.reaped and not problems \
                 and not self.quarantined and out_sha is not None
            try:
                publication = write_x(self.settle_path, dict(rec, provisionally_resources_closed=ok))
                done_m, done_e = time.monotonic(), time.time()
                within = done_m <= self.cleanup_end and done_e <= self.deadline + SETTLE_TAIL
                rec.update(settlement_publication_in_bounds=within, settlement_receipt_sha256=publication,
                           settlement_publication_done_mono=done_m, settlement_publication_done_epoch=done_e)
                if not within:
                    problems.append("settlement receipt publication completed outside frozen bound")
                rec["settled"] = bool(ok and within)
            except BaseException as exc:
                problems.append("settlement publication unproved %r" % (exc,))
            if rec["settled"] is not True:
                self._record_unsettled("child resource/census/publication unproven: %r" % problems)
                rec.update(unsettled=self.unsettled, quarantined=self.quarantined)
            self.settled_rec = rec
            return rec
        finally:
            STATE["cleanup_deadline"] = previous_end



def segments(path):
    """Capture lines (CR or LF separated), read through the anchored run tree (N8), bounded by LOG_CAP (N7)."""
    txt = read_tree(path, LOG_CAP).decode("utf-8", "replace")
    return [s for s in re.split(r"[\r\n]", txt) if s != ""]


def supervise(child, sink):
    """G3/G8: census before non-reaping exit observation; evaluate ALL safety conditions before one stop.
    An intended proof cap cannot mask simultaneous capture/disk/ownership defects."""
    last_rss = last_reg = float("-inf")
    peak = 0
    while True:
        mono = time.monotonic()
        reasons = []
        try:
            if mono - last_rss >= 1.0:
                last_rss = mono
                found, rss = child.census()
                if found:
                    child.descendants = sorted(set(child.descendants) | set(found))
                    reasons.append("descendant_process")
                runner_rss = task_rss(os.getpid())
                if runner_rss is None or (rss is None and child.observe_exit() is None):
                    reasons.append("rss_unreadable")
                else:
                    total = (rss or 0) + max(runner_rss, buffer_charge())
                    peak = max(peak, total)
                    if total > LANE_RSS_TRIP:
                        reasons.append("lane_rss")
            rc = child.observe_exit()              # WNOWAIT, no loss of group anchor
            if child.wait_lost is not None:
                reasons.append("wait_ownership_lost")
            if child.reader_error is not None:
                reasons.append("capture_reader_error")
            if child.over_cap:
                reasons.append("capture_cap")
            if sink is not None and sink.error:
                reasons.append("proof_sink_error")
            if child.feeder is not None and (child.feeder.exception is not None or child.feeder.construction_error is not None):
                reasons.append("feeder_exception")
            if free_bytes() < FREE_FLOOR:
                reasons.append("inflight_disk_floor")
            if mono - last_reg >= 5.0:
                last_reg = mono
                if registry_refusals():
                    reasons.append("stop_registry")
            if time.time() > child.deadline or time.monotonic() > child.deadline_mono:
                reasons.append("absolute_or_elapsed_deadline")
            if sink is not None and sink.over_cap:
                reasons.append("proof_cap")
            if cancelled():
                reasons.append("owner_cancel_sigterm")
        except BaseException as exc:
            reasons.append("monitor_exception:%r" % (exc,))
            rc = None
        for reason in reasons:
            if reason not in child.trips:
                child.trips.append(reason)
                if reason not in NONLATCHING_TRIPS:
                    latch("trip %s on %s" % (reason, child.label))
        if reasons:
            child.term(reasons[0])
            break
        if rc is not None:
            break
        child.last_alive_mono = mono
        time.sleep(SUPERVISE_SLICE)
    return child.stop, peak


def run_child(argv, label, wall, reserve, inputs, sink=None, feeder=None):
    """Prepared outputs -> admission -> spawn -> supervise -> settle.  Returns (rec|None, lines, refusal)."""
    ch = None
    try:
        cwd = os.path.join(STATE["out"], "cwd", "%02d-%s" % (STATE["seq"] + 1, label))
        mkdir_anchored(cwd)  # r4#4: inside the cleanup guard; N8: exclusive and anchored
        ch = Child(argv, label, wall, reserve, inputs, sink, cwd, feeder)
        if ch.refused:
            return None, [], ch.refused
        peak = None
        try:
            if cancelled():
                ch.term("owner_cancel_sigterm")
            _, peak = supervise(ch, sink)
        except BaseException as exc:
            latch("runner exception during supervision %r" % exc)
            ch.term("runner_exception")
        rec = ch.settle()
        rec["trip"] = ch.stop
        rec["peak_sampled_lane_rss_bytes"] = peak
        lines = segments(ch.out_path) if rec.get("stream_thread_alive_after_join") is False else []
        return rec, lines, []
    finally:
        settle_all()
        if sink is not None and (ch is None or ch.proc is None):
            sink.finish()  # never-spawned producer: unblock and join the reader
        if feeder is not None and not feeder.started:
            errs = feeder.abandon()  # never-spawned checker: both pipe ends closed; V6: errors latch
            if errs:
                latch("never-started feeder endpoint close errors %r" % (errs,))



def settle_all():
    """G4: exactly ONE pass. Each Child performs idempotent stages under its single remaining deadline.
    An escaped cleanup never gets another round of joins or process waits."""
    for c in tuple(OWNED):
        if c.proc is None or c.settled_rec is not None:
            continue
        try:
            c.settle()
        except BaseException as exc:
            try:
                c._record_unsettled("settlement escaped: %r" % (exc,))
            except BaseException:
                c.quarantined = True
            c.settled_rec = {"seq": c.seq, "label": c.label, "pid": c.pid, "settled": False,
                             "problems": ["settlement escaped %r" % (exc,)],
                             "unsettled": getattr(c, "unsettled", None), "actual_owned_reap": getattr(c, "reaped", None),
                             "settlement_publication_in_bounds": False}
            latch("child cleanup unproven; retain parent block")


def run_kissat(cnf_path, label, seconds, cap, reserve, inputs, owner):
    """kissat -q -f --seed=1 --time=S CNF [PROOF_FIFO]; with a cap the proof goes ONLY to a RAM ProofBuffer (S1).
    N6: a created ProofBuffer is appended to the caller's `owner` list at creation, so the caller's finally
    releases it on every path, including an exception before this function returns.
    Returns (rec|None, lines, refusal, buffer|None)."""
    argv = [KISSAT[0], "-q", "-f", "--seed=1", "--time=%d" % seconds, cnf_path]
    sink = None
    if cap is not None:
        sink = ProofBuffer(os.path.join(STATE["out"], "fifo", label + ".proof.fifo"), cap)
        try:
            owner.append(sink)
        except BaseException:
            sink.finish()
            sink.release()
            raise
        argv.append(sink.fifo_path)
    rec, lines, refused = run_child(argv, label + ".kissat", seconds, reserve,
                                    dict(inputs, proof_storage=None if sink is None else "RAM only", proof_cap=cap),
                                    sink)
    return rec, lines, refused, sink


def run_check(cnf_path, buf, checker, label, seconds, reserve, inputs, mode="plain"):
    name, path, pin = checker
    if buf.released:
        raise RuntimeError("proof buffer already released")
    feeder = None
    try:
        feeder = Feeder(buf.blocks, mode, label="%s.drat%s" % (label, name))
        return run_child([path, cnf_path, "-i", "-t", str(seconds)], "%s.drat%s" % (label, name), seconds, reserve,
                         dict(inputs, cnf=cnf_path, checker=[name, path, pin], proof_source="RAM stdin", feed_mode=mode),
                         feeder=feeder)
    finally:
        if feeder is not None and not feeder.started:
            if feeder.abandon():
                latch("never-started feeder endpoint rollback unproven")


def buffer_integrity(rec):
    if not isinstance(rec, dict):
        return False
    if "error" not in rec or "construction_error" not in rec:
        return False
    required_true = ("sink_settled", "fifo_same_inode_still_fifo", "reader_fd_closed",
                     "buffer_rehash_matches", "finish_deadline_in_bounds")
    return (all(rec.get(k) is True for k in required_true)
            and rec.get("thread_alive_after_join") is False and rec.get("error") is None
            and rec.get("construction_error") is None and _hex64(rec.get("sha256_of_retained"))
            and all(type(rec.get(k)) is int and rec[k] >= 0 for k in ("received", "retained", "discarded", "cap"))
            and rec["retained"] <= rec["cap"] and rec["received"] == rec["retained"] + rec["discarded"]
            and rec.get("buffer_rehash") == [rec["sha256_of_retained"], rec["retained"]])


def sink_complete(sink_rec):
    return (buffer_integrity(sink_rec) and sink_rec.get("connected") is True and sink_rec.get("eof") is True
            and sink_rec.get("over_cap") is False and sink_rec.get("unblocked_by_runner") is False
            and sink_rec["discarded"] == 0 and sink_rec["received"] == sink_rec["retained"])


def status_lines(lines):
    return [s[:200] for s in lines if s.startswith("s ")][:8]


FORBIDDEN = (("early EOF", "EARLY_EOF"), ("clauses less than expected", "LESS_THAN_EXPECTED"),
             ("trivial UNSAT", "TRIVIAL_UNSAT"), ("ERROR", "ERROR"), ("MEMOUT", "MEMOUT"),
             ("wrong binary prefix", "WRONG_PREFIX"), ("no empty clause detected", "NO_EMPTY_CLAUSE"),
             ("NOT VERIFIED", "NOT_VERIFIED"), ("TIMEOUT", "TIMEOUT"), ("illegal literal", "ILLEGAL_LITERAL"),
             ("error opening", "ERROR_OPENING"), ("failed to reallocate", "FAILED_REALLOC"))


def defect(code, text):
    """V10: every defect carries a stable ID: 'ID: text'."""
    return "%s: %s" % (code, text)


def defect_ids(defects):
    """V10: the complete, sorted list of stable defect IDs (the comparison key of controls and tests)."""
    return sorted(d.split(": ", 1)[0] for d in defects)


def checker_defects(name, cnf_expect, buf_sha, buf_bytes, drat_rec, drat_lines):
    """S4/V9/V10: per-checker P-STREAM qualification with canonical (unique) parser records; every defect ID is
    prefixed with the checker name."""
    bad = []
    X = name + "."
    feed = drat_rec.get("stdin_feed") or {}
    filt = drat_rec.get("stdout_filter") or {}
    if drat_rec.get("returncode") != 0 or drat_rec.get("stop") != "self":
        bad.append(defect(X + "EXIT", "checker not self-exit rc0"))
    st = status_lines(drat_lines)
    if st != ["s VERIFIED"]:
        bad.append(defect(X + "STATUS", "status lines %r != ['s VERIFIED']" % (st,)))
    v, c = cnf_expect[2].split()[2:4]
    hdr = [s[:200] for s in drat_lines if s.startswith("c parsing input formula")]
    if hdr != ["c parsing input formula with %s variables and %s clauses" % (v, c)]:
        bad.append(defect(X + "HEADER", "parser header records %r != the CNF pin header" % (hdr[:4],)))
    rd = [s[:200] for s in drat_lines if s.startswith("c reading proof")]
    if rd != [STDIN_LINE]:
        bad.append(defect(X + "STDIN", "stdin records %r != [%r]" % (rd[:4], STDIN_LINE)))
    if feed.get("mode") != "plain":
        bad.append(defect(X + "FEED_MODE", "feed mode %r is not plain" % (feed.get("mode"),)))
    if feed.get("fed_bytes") != buf_bytes or feed.get("fed_sha256") != buf_sha or feed.get("proof_bytes_fed") != buf_bytes:
        bad.append(defect(X + "FEED_DIGEST", "fed bytes/SHA-256 != collected proof buffer"))
    if feed.get("started") is not True or feed.get("thread_alive_after_join") is not False \
            or any(k not in feed or feed[k] is not None for k in
                   ("delivery_error", "exception", "close_error", "construction_error")) \
            or feed.get("read_endpoint_closed") is not True or feed.get("write_endpoint_closed") is not True:
        bad.append(defect(X + "FEED_STATE", "stdin feed incomplete, failed or unsettled"))
    fb = feed.get("fed_bytes")
    fin = [s[:200] for s in drat_lines if s.startswith("c finished parsing")]
    if not isinstance(fb, int) or isinstance(fb, bool) or fin != ["c finished parsing, read %d bytes from proof file" % fb]:
        bad.append(defect(X + "CONSUMED", "consumed records %r != [read %r bytes]" % (fin[:4], fb)))
    nd = drat_rec.get("nondropped_bytes")
    if filt.get("raw_eof") is not True or not isinstance(filt.get("dup_bytes_dropped"), int) or not isinstance(nd, int) \
            or isinstance(nd, bool) or filt.get("raw_bytes") != nd + filt["dup_bytes_dropped"]:
        bad.append(defect(X + "FILTER", "checker output filter accounting mismatch"))
    for pat, key in FORBIDDEN:
        if any(pat in s for s in drat_lines):
            bad.append(defect(X + "FORBIDDEN." + key, "checker output contains %r" % pat))
    if drat_rec.get("settled") is not True or drat_rec.get("capture_over_cap") is not False:
        bad.append(defect(X + "SETTLE", "settlement/capture defect seq %s" % drat_rec.get("seq")))
    if drat_rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect(X + "TIMING", "exit not observed by the checker deadline (N4)"))
    contradictions = receipt_contradictions(drat_rec)
    if contradictions:
        bad.append(defect(X + "RECEIPT", "contradictory/incomplete ownership evidence %r" % contradictions))
    return bad



def qualify_stream(cnf_expect, solver_rec, kissat_lines, proof_cap, checks, cnf_post, buf_post):
    """S4/V9/V10: item-level qualification over the solver leg (complete output exactly ['s UNSATISFIABLE']), the
    RAM buffer and every pinned checker in order; checks = [(name, drat_rec, drat_lines), ...].  UNSAT requires []."""
    bad = []
    if solver_rec.get("returncode") != 20 or solver_rec.get("stop") != "self":
        bad.append(defect("SOLVER_EXIT", "solver not self-exit rc20"))
    if kissat_lines != ["s UNSATISFIABLE"]:
        bad.append(defect("SOLVER_OUTPUT", "complete solver output %r != ['s UNSATISFIABLE']" % (kissat_lines[:4],)))
    buf = solver_rec.get("proof_sink") or {}
    if not sink_complete(solver_rec.get("proof_sink")):
        bad.append(defect("BUFFER_INCOMPLETE", "proof buffer incomplete/over cap/error"))
    buf_sha, buf_bytes = buf.get("sha256_of_retained"), buf.get("retained")
    if not isinstance(buf_bytes, int) or isinstance(buf_bytes, bool) or buf_bytes <= 0 or buf_bytes > proof_cap:
        bad.append(defect("BUFFER_SIZE", "proof size outside (0, cap]"))
    if [c[0] for c in checks] != [c[0] for c in CHECKERS]:
        bad.append(defect("CHECKER_SET", "not every pinned checker ran, in order"))
    for name, rec, lines in checks:
        bad += checker_defects(name, cnf_expect, buf_sha, buf_bytes, rec, lines)
    if cnf_post != (cnf_expect[0], cnf_expect[1]):
        bad.append(defect("CNF_POST", "CNF file digest/bytes != expected"))
    if buf_post != [buf_sha, buf_bytes]:
        bad.append(defect("BUFFER_POST", "proof buffer re-hash after the checks != collector measurement"))
    if solver_rec.get("settled") is not True or solver_rec.get("capture_over_cap") is not False:
        bad.append(defect("SOLVER_SETTLE", "settlement/capture defect seq %s" % solver_rec.get("seq")))
    if solver_rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect("SOLVER_TIMING", "exit not observed by the solver deadline (N4)"))
    contradictions = receipt_contradictions(solver_rec)
    if contradictions:
        bad.append(defect("SOLVER_RECEIPT", "contradictory/incomplete ownership evidence %r" % contradictions))
    return bad



def verify_sat(cnf_path, kissat_lines, label):
    """Two independent checks of a SAT model: clause satisfaction and both PA19 definitions."""
    lits = set()
    for s in kissat_lines:
        if s.startswith("v "):
            lits.update(int(x) for x in s[2:].split() if x != "0")
    sat_all = True
    dfd, name = tree_path(cnf_path)                # N8: anchored read of the run-tree CNF
    fd, _st = open_regular(name, dfd)
    with os.fdopen(fd, "rb") as f:
        for ln in f:
            if ln.startswith(b"p") or ln.startswith(b"c"):
                continue
            cl = [int(x) for x in ln.split()[:-1]]
            if not any(l in lits for l in cl):
                sat_all = False
                break
    A = [[None] * 8 for _ in range(19)]
    cells_ok = True
    for r in range(19):
        for c in range(8):
            ss = [s for s in range(6) if (1 + 48 * r + 6 * c + s) in lits]
            if len(ss) != 1:
                cells_ok = False
            else:
                A[r][c] = ss[0]
    rowpair_ok = cells_ok and all(sum(A[r][c] == A[q][c] for c in range(8)) <= 1
                                  for r in range(19) for q in range(r + 1, 19))
    colpair_ok = cells_ok and all(len({(A[r][c], A[r][d]) for r in range(19)}) == 19
                                  for c in range(8) for d in range(c + 1, 8))
    cand = os.path.join(STATE["out"], label + ".SAT-CANDIDATE.json")
    write_x(cand, {"host_clock": clock(), "array": A, "clauses_all_satisfied": sat_all,
                   "cells_exactly_one": cells_ok, "row_pair_agreements_le_1": rowpair_ok,
                   "column_pair_ordered_pairs_distinct": colpair_ok,
                   "status": "CANDIDATE_UNVERIFIED - notify parent immediately"})
    latch_path = os.path.join(LANE, "control", "SAT-CANDIDATE-" + label)
    write_bytes_x(latch_path, cand.encode())
    return {"candidate": cand, "latch": latch_path, "clauses_all_satisfied": sat_all, "cells": cells_ok,
            "rowpair": rowpair_ok, "colpair": colpair_ok}



def php_cnf(p, h):
    """Pigeonhole: p pigeons into h holes; UNSAT iff p > h."""
    var = lambda i, j: i * h + j + 1  # noqa: E731
    cl = [[var(i, j) for j in range(h)] for i in range(p)]
    for j in range(h):
        for i in range(p):
            for k in range(i + 1, p):
                cl.append([-var(i, j), -var(k, j)])
    return ("p cnf %d %d\n" % (p * h, len(cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cl)).encode()


def healthy(rec):
    return (isinstance(rec, dict) and not receipt_contradictions(rec) and rec.get("stop") == "self"
            and rec.get("trips") == [] and rec.get("capture_over_cap") is False
            and type(rec.get("returncode")) is int and rec["returncode"] >= 0
            and rec.get("resource_diagnostics") == [] and rec.get("exit_observed_by_deadline") is True)


def c6_timer_refusals(rec, lines):
    """N10: C6 intended cause = expiry of kissat's --time=CONTROL_TIMER_S timer, bound to monotonic execution
    evidence rather than cleanup-inclusive wall time: healthy self-exit rc 0 with complete output exactly
    ['s UNKNOWN']; runtime lower bound (last_alive - started: the process was seen alive at last_alive and had
    started before started) >= C6_MIN_RUN_S; runtime upper bound (exit_observed - popen_call) <= C6_MAX_RUN_S.
    Cleanup time is recorded separately and plays no role.  Returns refusal reasons ([] = intended)."""
    why = []
    if not healthy(rec) or rec.get("returncode") != 0:
        why.append("not a healthy rc-0 self-exit observed by its deadline")
    if lines != ["s UNKNOWN"]:
        why.append("complete output %r != ['s UNKNOWN']" % (lines[:4],))
    t = rec.get("timing") or {}
    nums = [t.get(k) for k in ("popen_call_s", "started_s", "last_alive_s", "exit_observed_s")]
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x) for x in nums):
        why.append("monotonic timing evidence incomplete %r" % (nums,))
    else:
        popen_call, started, last_alive, exit_obs = nums
        if not 0 <= popen_call <= started <= last_alive <= exit_obs:
            why.append("contradictory monotonic event order")
        if last_alive - started < C6_MIN_RUN_S:
            why.append("runtime lower bound %.3f s < %.1f s" % (last_alive - started, C6_MIN_RUN_S))
        if exit_obs - popen_call > C6_MAX_RUN_S:
            why.append("runtime upper bound %.3f s > %.1f s" % (exit_obs - popen_call, C6_MAX_RUN_S))
    return why


def completed_checker(rec, lines, expect):
    """r3#8: a completed drat-trim outcome: exactly 's VERIFIED' rc0 or 's NOT VERIFIED' rc1, no
    MEMOUT/TIMEOUT/ERROR text, healthy settlement."""
    st = status_lines(lines)
    if not healthy(rec) or any(p in s for s in lines for p in ("MEMOUT", "TIMEOUT", "ERROR")):
        return False
    if expect == "VERIFIED":
        return st == ["s VERIFIED"] and rec["returncode"] == 0
    return st == ["s NOT VERIFIED"] and rec["returncode"] == 1


def controls():
    """S6/V11: same-binary positive and intended-reason controls through the RAM/stdin transport for BOTH pinned
    checkers.  Each checker's intended predicate is evaluated before the next child is launched; C2/C3/C4 compare
    complete defect-ID sets; C6/C7/C7b are bound to the pinned binaries' measured or source-stated diagnostics.
    Stops at the first refused, unhealthy or not-as-intended control (later controls are not started).  V5/N6:
    every control buffer is owned by `bufs` from its creation (run_kissat) and released in the finally.  N10: C6
    is bound to monotonic execution evidence of the --time=CONTROL_TIMER_S expiry (c6_timer_refusals)."""
    recs = {}
    bufs = []
    d = os.path.join(STATE["out"], "controls")    # N8: created and anchored with the run tree
    per_child = LOG_CAP + 3 * RECORD_MAX

    def fail(name, why):
        recs[name] = dict(recs.get(name, {}), failed=why)
        return False, recs

    def checked(tag, cnf_path, pins, buf, mode, predicate):
        out = []
        for chk in CHECKERS:
            dr, dl, rf = run_check(cnf_path, buf, chk, tag, CONTROL_CHILD_WALL, per_child, pins, mode)
            if dr is None:
                return out, "checker %s refused %r" % (chk[0], rf)
            out.append((chk[0], dr, dl))
            if (pins.get("cnf_pin") is not None and list(sha_tree(cnf_path)) != pins["cnf_pin"]) or buf.digest() != pins["proof_pin"]:
                latch("control artifacts changed across checker execution")
                return out, "post-check control artifact identity mismatch"
            if LATCH or cancelled():
                return out, "safety/cancellation cannot be an intended control outcome"
            why = predicate(chk[0], dr, dl)
            if why:
                return out, "checker %s: %s" % (chk[0], why)   # V11: the next checker is never launched
        return out, None

    def view(checks):
        return {n: {"drat": r, "checker_status_lines": status_lines(l)} for n, r, l in checks}

    try:
        raw = php_cnf(6, 5)
        cnf = os.path.join(d, "php6x5.cnf")
        h, n = write_bytes_x(cnf, raw)
        exp = (h, n, raw.split(b"\n", 1)[0].decode())
        ks, kl, rf, b1 = run_kissat(cnf, "C1", CONTROL_CHILD_WALL, CONTROL_PROOF_CAP, per_child, {"cnf_pin": [h, n]},
                                    bufs)
        if ks is None:
            return fail("C1_positive_php6x5", "refused %r" % rf)
        recs["C1_positive_php6x5"] = {"kissat": ks, "kissat_lines": kl[:8]}
        if not (healthy(ks) and ks["returncode"] == 20 and kl == ["s UNSATISFIABLE"] and sink_complete(ks["proof_sink"])):
            return fail("C1_positive_php6x5", "solver leg not exactly rc20 ['s UNSATISFIABLE'], unhealthy or buffer incomplete")
        ph, pn = ks["proof_sink"]["sha256_of_retained"], ks["proof_sink"]["retained"]
        pins = {"cnf_pin": [h, n], "proof_pin": [ph, pn]}

        def positive(name, r, l):
            ids = defect_ids(checker_defects(name, exp, ph, pn, r, l))
            return None if ids == [] and completed_checker(r, l, "VERIFIED") else "positive predicate failed %r" % ids

        c1k, why = checked("C1", cnf, pins, b1, "plain", positive)
        recs["C1_positive_php6x5"]["checkers"] = view(c1k)
        if why:
            return fail("C1_positive_php6x5", why)
        c1 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c1k, sha_tree(cnf), b1.digest())
        recs["C1_positive_php6x5"].update(intended="PASS: qualify_stream == [] through checker A then checker B", defects=c1)
        if c1 != []:
            return fail("C1_positive_php6x5", "positive control did not pass %r" % defect_ids(c1))
        # C2 (deterministic): same header and clause count, first clause missing one literal; the deterministic
        # PHP(6,5) proof stays VERIFIED (measured in every earlier run), so the ONLY item defect is CNF_POST.
        lines = raw.split(b"\n")
        first = lines[1].split()
        mutated = b"\n".join([lines[0], b" ".join(first[:-2] + first[-1:])] + lines[2:])
        cnf2 = os.path.join(d, "php6x5-one-literal-removed.cnf")
        h2, n2 = write_bytes_x(cnf2, mutated)
        c2k, why = checked("C2", cnf2, {"cnf_pin": [h2, n2], "proof_pin": [ph, pn]}, b1, "plain", positive)
        recs["C2_mutated_cnf_digest"] = {"intended": "each checker completed 's VERIFIED' with no checker defect; item "
                                                     "defect IDs exactly ['CNF_POST']", "checkers": view(c2k)}
        if why:
            return fail("C2_mutated_cnf_digest", why)
        c2 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c2k, sha_tree(cnf2), b1.digest())
        recs["C2_mutated_cnf_digest"]["defects"] = c2
        if defect_ids(c2) != ["CNF_POST"]:
            return fail("C2_mutated_cnf_digest", "item defect IDs %r != ['CNF_POST']" % defect_ids(c2))
        # C3: the valid proof + one trailing byte appended IN TRANSIT.
        def suffix_reject(name, r, l):
            ids = defect_ids(checker_defects(name, exp, ph, pn, r, l))
            want = sorted(name + "." + k for k in ("FEED_MODE", "FEED_DIGEST", "CONSUMED", "FORBIDDEN.WRONG_PREFIX"))
            if ids != want or not completed_checker(r, l, "VERIFIED") \
                    or (r.get("stdin_feed") or {}).get("fed_bytes") != pn + len(SUFFIX):
                return "suffix predicate failed: IDs %r != %r or not completed/fed+1" % (ids, want)
            return None

        c3k, why = checked("C3", cnf, pins, b1, "suffix", suffix_reject)
        recs["C3_trailing_proof_byte"] = {"intended": "per checker: completed 's VERIFIED', checker defect IDs exactly "
                                                      "{FEED_MODE, FEED_DIGEST, CONSUMED, FORBIDDEN.WRONG_PREFIX}, fed == "
                                                      "buffer + 1", "checkers": view(c3k)}
        if why:
            return fail("C3_trailing_proof_byte", why)
        # C4: satisfiable PHP(5,5) with the PHP(6,5) proof.
        raw4 = php_cnf(5, 5)
        cnf4 = os.path.join(d, "php5x5-sat.cnf")
        h4, n4 = write_bytes_x(cnf4, raw4)
        exp4 = (h4, n4, raw4.split(b"\n", 1)[0].decode())

        def foreign_reject(name, r, l):
            ids = defect_ids(checker_defects(name, exp4, ph, pn, r, l))
            want = sorted(name + "." + k for k in ("EXIT", "STATUS", "FORBIDDEN.NOT_VERIFIED"))
            if ids != want or not completed_checker(r, l, "NOT VERIFIED"):
                return "foreign-proof predicate failed: IDs %r != %r or not completed 's NOT VERIFIED' rc1" % (ids, want)
            return None

        c4k, why = checked("C4", cnf4, {"cnf_pin": [h4, n4], "proof_pin": [ph, pn]}, b1, "plain", foreign_reject)
        recs["C4_sat_formula_foreign_proof"] = {"intended": "per checker: completed exactly ['s NOT VERIFIED'] rc1, "
                                                            "checker defect IDs exactly {EXIT, STATUS, "
                                                            "FORBIDDEN.NOT_VERIFIED}", "checkers": view(c4k)}
        if why:
            return fail("C4_sat_formula_foreign_proof", why)
        # C5: HARD RAM proof cap 4096 B on PHP(11,10).
        raw5 = php_cnf(11, 10)
        cnf5 = os.path.join(d, "php11x10.cnf")
        h5, n5 = write_bytes_x(cnf5, raw5)
        ks5, kl5, rf, b5 = run_kissat(cnf5, "C5", CONTROL_CHILD_WALL, 4096, per_child, {"cnf_pin": [h5, n5]}, bufs)
        if ks5 is None:
            return fail("C5_proof_hard_cap", "refused %r" % rf)
        ps5 = ks5["proof_sink"] or {}
        recs["C5_proof_hard_cap"] = {"intended": "stop=proof_cap, retained<=4096 B, received == retained + discarded > "
                                                 "retained, settled, over_cap, collector joined", "kissat": ks5}
        if not (not LATCH and not cancelled() and ks5.get("trips") == ["proof_cap"]
                and ks5.get("capture_over_cap") is False and not receipt_contradictions(ks5)
                and buffer_integrity(ps5) and ks5["stop"] == "proof_cap" and ps5.get("retained", 4097) <= 4096 and ps5.get("over_cap")
                and ps5.get("discarded", 0) > 0 and ps5.get("received") == ps5.get("retained", 0) + ps5.get("discarded", 0)
                and ks5["settled"] is True and ps5.get("thread_alive_after_join") is False and not ks5["resource_diagnostics"]):
            return fail("C5_proof_hard_cap", "intended reason or settlement missing")
        # C6: kissat --time=CONTROL_TIMER_S, no proof, on PHP(13,12): N10 timer expiry bound to monotonic
        # execution evidence (runtime in [C6_MIN_RUN_S, C6_MAX_RUN_S]), rc 0 and exactly ['s UNKNOWN'].
        raw6 = php_cnf(13, 12)
        cnf6 = os.path.join(d, "php13x12.cnf")
        h6, n6 = write_bytes_x(cnf6, raw6)
        ks6, kl6, rf, _ = run_kissat(cnf6, "C6", CONTROL_TIMER_S, None, per_child, {"cnf_pin": [h6, n6]}, bufs)
        if ks6 is None:
            return fail("C6_native_time_limit", "refused %r" % rf)
        why6 = c6_timer_refusals(ks6, kl6)
        recs["C6_native_time_limit"] = {"intended": "healthy self-exit rc 0, complete output exactly ['s UNKNOWN'], "
                                                    "monotonic runtime lower bound >= %.1f s and upper bound <= %.1f "
                                                    "s for --time=%d (runs 008/010/012 at --time=1: rc 0, "
                                                    "'s UNKNOWN')" % (C6_MIN_RUN_S, C6_MAX_RUN_S, CONTROL_TIMER_S),
                                        "kissat": ks6, "kissat_lines": kl6[:8], "refusals": why6}
        if why6:
            return fail("C6_native_time_limit", "intended timer-expiry outcome missing %r" % (why6,))
        # C7: missing input with a RAM proof buffer: kissat's missing-input diagnostic, collector unblocked and joined.
        absent = os.path.join(d, "absent.cnf")
        ks7, kl7, rf, b7 = run_kissat(absent, "C7", 10, CONTROL_PROOF_CAP, per_child, {"cnf_pin": None}, bufs)
        if ks7 is None:
            return fail("C7_no_input_sink_liveness", "refused %r" % rf)
        ps7 = ks7["proof_sink"] or {}
        want7 = ["kissat: error: can not read '%s'" % absent]
        recs["C7_no_input_sink_liveness"] = {"intended": "healthy self-exit rc 1, complete output exactly %r (runs "
                                                         "008/010/012), collector unblocked by the runner, 0 bytes, "
                                                         "joined" % want7, "kissat": ks7, "kissat_lines": kl7[:8]}
        if not (healthy(ks7) and buffer_integrity(ps7) and ks7["returncode"] == 1 and kl7 == want7 and ps7.get("unblocked_by_runner") is True
                and ps7.get("retained") == 0 and ps7.get("thread_alive_after_join") is False):
            return fail("C7_no_input_sink_liveness", "intended missing-input outcome or collector settlement missing")
        # C7b: missing CNF for each checker with a HELD feed: drat-trim.c:1425-1427 prints exactly
        # 'c error opening "<path>".' and returns ERROR (-1, exit status 255) before reading stdin; the feeder then
        # meets a closed read end (EPIPE, 0 bytes fed); every thread settles.
        absent2 = os.path.join(d, "absent-checker.cnf")
        want7b = ['c error opening "%s".' % absent2]

        def missing_input(name, r, l):
            f7 = r.get("stdin_feed") or {}
            if not (healthy(r) and r["returncode"] == 255 and l == want7b and f7.get("fed_bytes") == 0
                    and str(f7.get("delivery_error")).startswith("EPIPE") and f7.get("hold_released_by_event") is True
                    and f7.get("thread_alive_after_join") is False):
                return "missing-input predicate failed (rc %r, lines %r, feed %r)" % (r.get("returncode"), l[:4],
                                                                                    {k: f7.get(k) for k in ("fed_bytes", "delivery_error")})
            return None

        c7k, why = checked("C7b", absent2, {"cnf_pin": None, "proof_pin": [ph, pn]}, b1, "hold", missing_input)
        recs["C7b_checker_no_input_feed_liveness"] = {"intended": "per checker: healthy self-exit rc 255, complete output "
                                                                  "exactly %r, held feed EPIPE with 0 bytes fed, hold "
                                                                  "released by the reap, feeder joined" % want7b,
                                                      "checkers": view(c7k)}
        if why:
            return fail("C7b_checker_no_input_feed_liveness", why)
        return True, recs
    finally:
        for b in bufs:
            if b is not None:
                b.release()
        recs["buffer_accounting"] = [b.accounting() for b in bufs if b is not None]



def cutoff_refusals():
    """N4: the frozen run cutoffs (elapsed and absolute) have not passed."""
    why = []
    if STATE["mono_end"] is None or time.monotonic() > STATE["mono_end"]:
        why.append("after the frozen elapsed cutoff")
    if STATE["abs_end"] is None or time.time() > STATE["abs_end"]:
        why.append("after the frozen absolute cutoff")
    if time.time() > SCIENCE_STOP:
        why.append("after absolute new-science cutoff")
    return why


def terminal_gate():
    why = []
    try:
        why += registry_refusals()
        if free_bytes() < FREE_FLOOR:
            why.append("in-flight disk floor")
        led_why, STATE["last_ledger"] = ledger_refusals()
        why += led_why
        why += confinement_refusals()
        why += preservation_refusals()
        why += cutoff_refusals()                 # AFTER all blocking observations
    except BaseException as exc:
        why.append("terminal gate unproven %r" % (exc,))
    for w in why:
        latch("terminal gate: " + w)
    return why


def commit_record(path, rec_unknown, rec_unsat):
    """G5/G7: item bytes are PROVISIONAL, never self-authoritative scientific coverage. Exact preservation and
    confinement are checked before selection; promotion additionally requires publication observed in bounds,
    final closeout binding this digest, and independent parent observed-exit/raw audit."""
    unknown = dict(rec_unknown, count_for_scientific_coverage=False, publication_authority="PROVISIONAL")
    unsat = None if rec_unsat is None else dict(rec_unsat, status="UNSAT_PROVISIONAL",
                                               count_for_scientific_coverage=False,
                                               publication_authority="requires run closeout + parent raw audit")
    unknown_bytes = serialize(unknown)
    unsat_bytes = None if unsat is None else serialize(unsat)
    charge_output(max(len(unknown_bytes), len(unsat_bytes or b"")))
    fd = create_excl(path)
    chosen = unknown_bytes
    boundary = None
    try:
        try:
            for w in confinement_refusals() + preservation_refusals(exclude=(path,)) + cutoff_refusals():
                latch("commit: " + w)
            boundary = next(ORDER)
            co = STATE["cancel_order"]
            chosen = unsat_bytes if unsat_bytes is not None and not LATCH and (co is None or co > boundary) else unknown_bytes
            write_all(fd, chosen)
            os.fsync(fd)
        finally:
            os.close(fd)
        os.fsync(tree_path(path)[0])
    except BaseException as exc:
        CREATED[path].update(state="failed", error=repr(exc))
        latch("item publication incomplete %r" % (exc,))
        raise
    h = hashlib.sha256(chosen).hexdigest()
    register_written(path, h, len(chosen))
    completion_why = cutoff_refusals() + confinement_refusals() + preservation_refusals()
    completion_why += cutoff_refusals()           # recheck AFTER post-publication preservation work
    for w in completion_why:
        latch("item publication completion: " + w)
    before = STATE["cancel_order"]
    qualified = chosen is unsat_bytes and not completion_why and not LATCH and before is None
    return {"boundary": boundary, "cancel_order": before, "committed_unsat": qualified,
            "scientific_authority": "PROVISIONAL; parent raw audit required", "sha256": h,
            "publication_completed_in_bounds": not completion_why, "publication_defects": completion_why,
            "publication_done_mono": time.monotonic(), "publication_done_epoch": time.time()}


HEX64 = re.compile(r"[0-9a-f]{64}")
HEADER_RE = re.compile(r"p cnf [1-9][0-9]* [1-9][0-9]*")


def _nat(x):
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


def item_shape_refusals(it):
    """V12: exact item types and shape for this runner's family.  ms09: exact non-bool ints with
    0 <= lo <= hi < denominator, canonical id 'bBBBBB:LLLLL-HHHHH', pinned list (path, sha256); ms06: canonical id
    'ms06:bBBBBB:direct' and no interval fields; both: pinned CNF triple (sha256, bytes > 0, header)."""
    if not isinstance(it, dict) or not _nat(it.get("b")):
        return ["item or b malformed"]
    why = []
    cnf = it.get("cnf")
    if not (isinstance(cnf, tuple) and len(cnf) == 3 and isinstance(cnf[0], str) and HEX64.fullmatch(cnf[0])
            and _nat(cnf[1]) and cnf[1] > 0 and isinstance(cnf[2], str) and HEADER_RE.fullmatch(cnf[2])):
        why.append("cnf pin malformed")
    interval_keys = {"lo", "hi", "denominator", "list"}
    if FAMILY == "ms09":
        lo, hi, den, lst = it.get("lo"), it.get("hi"), it.get("denominator"), it.get("list")
        if not (_nat(lo) and _nat(hi) and _nat(den) and lo <= hi < den):
            why.append("interval not exact ints with 0 <= lo <= hi < denominator")
        elif it.get("id") != "b%05d:%05d-%05d" % (it["b"], lo, hi):
            why.append("id not canonical")
        if not (isinstance(lst, tuple) and len(lst) == 2 and isinstance(lst[0], str) and isinstance(lst[1], str)
                and HEX64.fullmatch(lst[1])):
            why.append("list pin malformed")
    else:
        if interval_keys & set(it):
            why.append("interval fields on a whole-case item")
        if it.get("id") != "ms06:b%05d:direct" % it["b"]:
            why.append("id not canonical")
    return why


def main():
    # G2: establish exclusive wait ownership before any resource/thread/child is acquired. No SIGCHLD handler,
    # SIG_IGN/auto-reap, Popen.poll/wait/communicate, wildcard waitpid or unretained Popen is allowed in this source.
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if threading.active_count() != 1 or not all(hasattr(os, n) for n in ("waitid", "WNOWAIT", "WEXITED")):
        print("REFUSED: exclusive wait ownership/kernel WNOWAIT unavailable", flush=True)
        return EXIT_PRESTART_REFUSED
    if len(sys.argv) != 4:
        print("usage:", os.path.basename(__file__), "GO.json GO_SHA256 OUT_DIR", flush=True)
        return EXIT_PRESTART_REFUSED
    go_path, go_sha, out_dir = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
    why = out_dir_refusal(out_dir)
    shape = [w for it in ITEMS for w in item_shape_refusals(it)]
    if why or shape or len({it.get("id") for it in ITEMS}) != len(ITEMS):
        print("REFUSED: output/item shape", why, shape, flush=True)
        return EXIT_PRESTART_REFUSED
    try:
        self_sha = sha_file(os.path.abspath(__file__))[0]
        go = json.loads(read_pinned(go_path, go_sha))
        read_pinned(*BINARY_IMPORTS)
        read_pinned(*KISSAT_SOURCE)
        contract = json.loads(read_pinned(*CONTRACT))
        if contract["resources"]["per_lane_new_disk_bytes"] != LANE_CEILING \
                or contract["resources"]["per_lane_busy_processes"] != BUSY_SLOTS:
            raise RuntimeError("live pinned contract resource mismatch")
        phase = "controls-only" if not ITEMS else "science"
        if phase != PHASE or go.get("phase") != PHASE or go.get("decision") != "GO" \
                or go.get("runner_sha256") != self_sha or go.get("items") != [it["id"] for it in ITEMS] \
                or go.get("binary_path_exclusivity") is not True or go.get("run_tree_exclusivity") is not True \
                or go.get("prior_attempt_exclusivity") is not True:
            raise RuntimeError("GO does not name exact phase/pin/items and exclusive pinned-executable premise")
        runner_ident, err = bsd_identity(os.getpid())
        if runner_ident is None or not runner_ident.get("start"):
            raise RuntimeError("runner identity unavailable %r" % (err,))
    except BaseException as exc:
        print("REFUSED: GO/evidence/runner identity", repr(exc), flush=True)
        return EXIT_PRESTART_REFUSED
    span = RUN_HELPER_SECONDS + CONTROLS_WORST_SECONDS + len(ITEMS) * ITEM_WORST_SECONDS
    if span + SETTLE + MARGIN > MAX_CHUNK or time.time() + span + SETTLE > OWNED_SETTLED_BY \
            or time.time() > NATIVE_LAUNCH_STOP:
        print("REFUSED: complete chunk/absolute launch fit", flush=True)
        return EXIT_PRESTART_REFUSED
    full_reserve = RUN_RESERVE + CONTROL_RESERVE + len(ITEMS) * ITEM_RESERVE
    alloc_why, ledger = allocation_refusals(go, go_sha, out_dir, full_reserve)
    if alloc_why:
        print("REFUSED: parent allocation", alloc_why, flush=True)
        return EXIT_PRESTART_REFUSED
    try:
        fb = free_bytes()
        pre = registry_refusals() + stability_refusals(full_reserve)
        if fb < FRESH_BASE + full_reserve or fb - full_reserve < FREE_FLOOR:
            pre.append("free space cannot retain full reserved growth")
        if time.time() > NATIVE_LAUNCH_STOP:
            pre.append("after native launch cutoff")
    except BaseException as exc:
        pre = ["prestart observation unproved %r" % (exc,)]
    if pre:
        print("REFUSED: prestart", pre, flush=True)
        return EXIT_PRESTART_REFUSED
    if time.time() + span + SETTLE > OWNED_SETTLED_BY or time.time() > NATIVE_LAUNCH_STOP:
        print("REFUSED: complete bound no longer fits after admission observations", flush=True)
        return EXIT_PRESTART_REFUSED
    epoch, mono0 = time.time(), time.monotonic()
    STATE.update(abs_end=epoch + span, chunk_end=epoch + MAX_CHUNK, mono0=mono0, mono_end=mono0 + span,
                 mono_chunk_end=mono0 + MAX_CHUNK, remaining_reserve=full_reserve, reservation=full_reserve,
                 output_limit=full_reserve, written=0, last_ledger=ledger, pilot_entries=list(ledger["pilot_entries"]),
                 prior_census=dict(ledger["prior_attempt_census"]), runner_identity=runner_ident,
                 go={"path": go_path, "sha256": go_sha}, runner_sha=self_sha, cleanup_deadline=None)
    try:
        anchor_existing_dir(CONTROL_DIR)
        create_run_tree(out_dir)
    except BaseException as exc:
        print("REFUSED: partial run tree remains reserved for parent disposition", repr(exc), flush=True)
        return EXIT_PRESTART_REFUSED
    STATE["out"] = out_dir
    summary = {"schema": SUMMARY_SCHEMA, "phase": PHASE, "items": {}, "controls_ok": None, "stopped": None,
               "terminal_policy": "all scientific/controls publications PROVISIONAL; parent complete raw audit required"}
    outcome = {"sat": False, "controls_failed": False, "refused": False, "exception": False, "complete": False}
    try:
        host = clock()
        launch = {"schema": LAUNCH_SCHEMA, "host_clock": host, "phase": PHASE, "owner": "ContinuePA19b",
                  "go": STATE["go"], "runner": {"path": os.path.abspath(__file__), "sha256": self_sha},
                  "runner_identity": runner_ident, "runner_started_by_epoch": epoch,
                  "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "cwd": os.getcwd(), "argv": sys.argv,
                  "argv_sha256": hashlib.sha256(json.dumps(sys.argv, separators=(",", ":")).encode()).hexdigest(),
                  "python": sys.version, "wait_ownership": "SIGCHLD=SIG_DFL; WNOWAIT observations; owned waitpid only",
                  "binaries": {"kissat": KISSAT, "checkers": CHECKERS, "date": DATE},
                  "exclusive_writer_premise": {"native_binaries": True, "run_tree": True, "prior_attempts": True},
                  "binary_path_race": "per-launch/settlement file+directory pin binding plus parent exclusive-writer premise; not fexecve",
                  "inputs": {"encoder": ENC, "skeleton": SKEL, "items": ITEMS, "registry": REGISTRY,
                             "binary_imports": BINARY_IMPORTS, "launch_contract": LAUNCH_CONTRACT,
                             "kissat_source_evidence": KISSAT_SOURCE, "monitor": MONITOR},
                  "absolute_end_epoch": STATE["abs_end"], "elapsed_span_s": span,
                  "limits": {"solver_s": SOLVER_SECONDS, "checker_s": CHECK_SECONDS, "proof_cap": PROOF_CAP,
                             "capture_cap": LOG_CAP, "settle_tail_s": SETTLE_TAIL, "chunk_s": MAX_CHUNK},
                  "timing": {"run_helper_s": RUN_HELPER_SECONDS, "controls_worst_s": CONTROLS_WORST_SECONDS,
                             "item_worst_s": ITEM_WORST_SECONDS, "settle_plus_margin_s": SETTLE + MARGIN},
                  "retained_output_reservation_bytes": full_reserve, "parent_allocation": ledger,
                  "prior_attempt_census": STATE["prior_census"], "output_dir": out_dir,
                  "publication_authority": "summary+closeout must be bound to parent-observed runner exit"}
        run_record = os.path.join(out_dir, "launch-record.json")
        STATE["run_record"] = {"path": run_record, "sha256": write_x(run_record, launch)}
        if host is None or LATCH or cancelled():
            outcome["exception"] = not cancelled()
            summary["stopped"] = {"phase": "required launch clock unavailable"}
        else:
            run_plan(summary, outcome)
    except BaseException as exc:
        outcome["exception"] = True
        summary["stopped"] = {"phase": "exception", "error": repr(exc)}
    finally:
        try:
            settle_all()
            code = final_code(summary, outcome)
        except BaseException as exc:
            # Missing closeout is never authority. The parent retains the entire reservation and audits the tree.
            print("CLOSEOUT UNPROVEN; PARENT BLOCK", repr(exc), flush=True)
            code = EXIT_SAFETY_STOP
    return code



def run_plan(summary, outcome):
    """The plan body; every early stop is a plain return with the outcome flags set.  V5: an item's proof buffer is
    released in a finally on every path (N6: owned by `item_bufs` from its creation); V12: item shape re-checked
    immediately before generation; N8: run-tree files are hashed through the anchored tree."""
    out_dir = STATE["out"]
    if sha_file(DRAT_OLD[0])[0] != DRAT_OLD[1] or sha_file(KISSAT[0])[0] != KISSAT[1]:
        raise RuntimeError("binary pin mismatch")
    if sha_file(DRAT)[0] != DRAT_OLD[1] or os.lstat(DRAT).st_ino == os.lstat(DRAT_OLD[0]).st_ino:
        raise RuntimeError("vendored drat-trim mismatch or shared inode")
    prov = json.loads(read_pinned(*DRAT_PROV_RECEIPT)).get("drat_trim") or {}
    if prov.get("binary_sha256") != DRAT_PROV[1] or prov.get("source_sha256") != DRAT_SOURCE_SHA \
            or sha_file(DRAT_PROV[0])[0] != DRAT_PROV[1] \
            or os.lstat(DRAT_PROV[0]).st_ino in (os.lstat(DRAT).st_ino, os.lstat(DRAT_OLD[0]).st_ino):
        raise RuntimeError("provenanced drat-trim pin/receipt mismatch or shared inode")
    ok, recs = controls()
    summary["controls_ok"] = ok
    summary["controls_record_sha256"] = write_x(os.path.join(out_dir, "controls.json"), recs)
    if not ok:
        outcome["controls_failed"] = True
        summary["stopped"] = {"phase": "controls"}
        return
    if PHASE == "controls-only":
        if ITEMS:
            raise RuntimeError("controls-only pin contains science items")
        summary["controls_terminal_gate"] = terminal_gate()
        summary["controls_qualification"] = "PROVISIONAL; complete closeout + parent raw audit required"
        outcome["complete"] = not summary["controls_terminal_gate"] and not LATCH and not cancelled()
        return                              # binding boundary: no encoder read/exec or item work
    if PHASE != "science" or not ITEMS:
        raise RuntimeError("science requires distinct exact phase/pin/items GO")
    E = load_verified_module("encode_skel_b_lane", ENC[0], ENC[1])
    D = json.loads(read_pinned(*SKEL))
    special = [p for p in D["profiles"] if list(p) != P0]
    for it in ITEMS:
        why = item_shape_refusals(it)
        if why:
            raise RuntimeError("item shape %r" % (why,))
        label = it["id"].replace(":", "_")
        rec = {"id": it["id"], "status": "UNKNOWN", "count_for_scientific_coverage": False,
               "host_clock_start": clock()}
        rec_path = os.path.join(out_dir, label + ".record.json")
        if rec["host_clock_start"] is None:
            rec["reason"] = "required item start host clock unavailable; no item work admitted"
            write_x(rec_path, rec)
            summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": rec["reason"]}
            summary["stopped"] = {"phase": "required_item_clock", "item": it["id"]}
            outcome["refused"] = True
            return
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = (hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode())
        if got != it["cnf"]:
            raise RuntimeError("CNF digest mismatch %r" % (got,))
        cnf_path = os.path.join(out_dir, label + ".cnf")
        write_bytes_x(cnf_path, cnf)
        del cnf
        if sha_tree(cnf_path) != (it["cnf"][0], it["cnf"][1]):
            raise RuntimeError("CNF file re-hash mismatch")
        inputs = {"item": it["id"], "cnf_pin": [it["cnf"][0], it["cnf"][1]], "case_b": it["b"],
                  "skeleton_pin": SKEL[1], "encoder_pin": ENC[1]}
        buf = None
        item_bufs = []                             # N6: owns the item's buffer from its creation
        try:
            ks, kl, refused, buf = run_kissat(cnf_path, label, SOLVER_SECONDS, PROOF_CAP, LOG_CAP + 3 * RECORD_MAX,
                                              inputs, item_bufs)
            if ks is None:
                rec.update(reason="solver admission refused", refusal=refused, host_clock_end=clock())
                write_x(rec_path, rec)
                summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "solver admission refused"}
                summary["stopped"] = {"phase": "solver_admission", "item": it["id"], "why": refused}
                outcome["refused"] = True
                return
            rec["solver"] = ks
            rec["solver_lines"] = kl[:8]
            rec["solver_status_lines"] = status_lines(kl)
            if ks["returncode"] == 10 and rec["solver_status_lines"] == ["s SATISFIABLE"] and ks["stop"] == "self" \
                    and ks["settled"]:
                rec["status"] = "SAT_CANDIDATE"
                rec["sat"] = verify_sat(cnf_path, kl, label)
                rec["host_clock_end"] = clock()
                write_x(rec_path, rec)
                summary["items"][it["id"]] = {"status": "SAT_CANDIDATE", "sat": rec["sat"]}
                summary["stopped"] = {"phase": "sat_candidate", "item": it["id"]}
                outcome["sat"] = True
                return
            sink_ok = sink_complete(ks["proof_sink"])
            if sink_ok:
                rec["proof"] = {"sha256": ks["proof_sink"]["sha256_of_retained"], "bytes": ks["proof_sink"]["retained"],
                                "storage": "RAM only (P-STREAM); never written to disk"}
            if ks["returncode"] == 20 and ks["stop"] == "self" and ks["settled"] and sink_ok and not LATCH \
                    and not cancelled():
                checks = []
                rec["checkers"] = {}
                for name, path, pin in CHECKERS:
                    dr, dl, refused = run_check(cnf_path, buf, (name, path, pin), label, CHECK_SECONDS,
                                                LOG_CAP + 3 * RECORD_MAX,
                                                dict(inputs, proof_pin=[rec["proof"]["sha256"], rec["proof"]["bytes"]]))
                    if dr is None:
                        rec.update(reason="checker %s admission refused" % name, refusal=refused,
                                   host_clock_end=clock())
                        write_x(rec_path, rec)
                        summary["items"][it["id"]] = {"status": "UNKNOWN",
                                                      "reason": "checker %s admission refused" % name}
                        summary["stopped"] = {"phase": "checker_admission", "item": it["id"], "checker": name,
                                              "why": refused}
                        outcome["refused"] = True
                        return
                    checks.append((name, dr, dl))
                    filt = dr.get("stdout_filter") or {}
                    rec["checkers"][name] = {
                        "record": dr, "status_lines": status_lines(dl),
                        "parse_lines": [s[:200] for s in dl if s.startswith("c parsing") or
                                        s.startswith("c finished parsing") or s.startswith("c reading proof")][:6],
                        "duplicate_literal_warnings": {   # V8/P3: both phases counted and disclosed, never gated
                            "formula_phase_proof_line_le_header_clauses": filt.get("dup_lines_at_or_below_header_clauses"),
                            "proof_phase_proof_line_gt_header_clauses": filt.get("dup_lines_above_header_clauses"),
                            "basis": "drat-trim.c:1133/1153/1229: exact phase partition for any log without early EOF"}}
                    if checker_defects(name, it["cnf"], rec["proof"]["sha256"], rec["proof"]["bytes"], dr, dl) \
                            or LATCH or cancelled():
                        break  # S4: a later checker cannot rescue the item
                post_cnf, post_buf = sha_tree(cnf_path), buf.digest()
                buf.release()
                rec["post_check_hashes"] = {"cnf": list(post_cnf), "proof_buffer": post_buf}
                rec["defects"] = qualify_stream(it["cnf"], ks, kl, PROOF_CAP, checks, post_cnf, post_buf)
                rec["defect_ids"] = defect_ids(rec["defects"])
                rec["host_clock_end"] = clock()
                rec["terminal_gate"] = terminal_gate()
                unsat = None
                if not rec["defects"] and not rec["terminal_gate"] and not LATCH:
                    unsat = dict(rec, status="UNSAT", count_for_scientific_coverage=True,
                                 commit="UNSAT chosen at an explicit commit boundary with no earlier cancel stamp or "
                                        "latch")
                commit = commit_record(rec_path, dict(rec, commit="UNKNOWN record"), unsat)
                rec["status"] = "UNSAT_PROVISIONAL" if commit["committed_unsat"] else "UNKNOWN"
                summary.setdefault("commits", {})[it["id"]] = commit
            else:
                rec["reason"] = "no settled self-exit rc20 verdict with a complete proof buffer (or latch/cancel)"
                rec["host_clock_end"] = clock()
                write_x(rec_path, rec)
        finally:
            for b in item_bufs:
                b.release()                        # N6: a live collector stays charged; closeout retries
        summary["items"][it["id"]] = {k: rec.get(k) for k in ("status", "defect_ids", "terminal_gate", "reason", "proof")}
        summary["items"][it["id"]]["duplicate_literal_warnings"] = {
            n: v.get("duplicate_literal_warnings") for n, v in (rec.get("checkers") or {}).items()}
        if LATCH or cancelled():
            summary["stopped"] = {"phase": "latch_or_cancel", "item": it["id"]}
            return
    outcome["complete"] = True



def final_code(summary, outcome):
    """G1/G5/A3: summary is PROVISIONAL. closeout.json binds its completed publication, final ledger and owner
    inventory. Neither file certifies itself: parent observed runner exit + pinned closeout + raw audit are REQUIRED.
    Any uncertain owner/census/publication/resource retains parent block; no waits/traversals after UNSETTLED
    beyond separately bounded runner-metadata work. Safety overrides candidate/control while preserving candidate info."""
    out_dir = STATE["out"]
    host_end = clock()
    previous_end = STATE.get("cleanup_deadline")
    STATE["cleanup_deadline"] = min(time.monotonic() + SETTLE, STATE["mono_end"] + SETTLE)
    defects = []
    try:
        for b in LIVE_BUFFERS:
            if b.release_requested and not b.released:
                b.release()                      # no join; a live collector keeps its ownership
        try:
            outstanding = buffer_charge()
            unresolved = unresolved_inventory()
        except BaseException as exc:
            outstanding = None
            unresolved = [{"kind": "unknown resource accounting", "error": repr(exc)}]
        if outstanding is None or type(outstanding) is not int or outstanding != 0:
            defects.append("proof RAM accounting not affirmatively zero")
        children = [c.settled_rec for c in OWNED if c.proc is not None]
        all_settled = all(not receipt_contradictions(r) for r in children)
        helpers_settled = all(h.settled is True for h in HELPERS if h.proc is not None)
        if not all_settled or not helpers_settled:
            defects.append("owned settlement unproven")
        if host_end is None and not cancelled() and not LATCH:
            defects.append("required closeout host clock unavailable")
        try:
            defects += confinement_refusals() + preservation_refusals()
            tree = run_tree_census()
            tree_bytes = sum(v[3] for v in tree.values() if v[0] != "dir")
            if tree_bytes > STATE["reservation"]:
                defects.append("physical retained output exceeds full reservation")
            led_why, ledger = ledger_refusals()
            defects += led_why
        except BaseException as exc:
            tree_bytes, ledger = None, None
            defects.append("closeout census/ledger unproved %r" % (exc,))
            unresolved.append({"kind": "unknown census/resource", "error": repr(exc)})
        m, e = time.monotonic(), time.time()
        late = m > STATE["mono_end"] + SETTLE or e > STATE["abs_end"] + SETTLE \
               or m - STATE["mono0"] > MAX_CHUNK
        if late:
            defects.append("closeout observations outside frozen bounds")
        if unresolved:
            defects.append("unproven owners/resources/publications retain parent block")
        for w in defects:
            latch("closeout: " + w)
        boundary = next(ORDER)
        co = STATE["cancel_order"]            # N9 AFTER boundary
        code = choose_exit_code(outcome, unresolved, co is not None and co < boundary)
        runner = STATE["runner_identity"]
        ownership = {"runner": runner, "runner_resources": "threads, descriptors, all RAM until runner exit",
                     "children": [{"pid": c.pid, "pgid": c.pgid, "identity_at_start": c.identity_at_start,
                                   "started_by_epoch": c.started_epoch, "actual_owned_reap": c.reaped,
                                   "wait_lost": c.wait_lost, "known_identities": list(c.known_identities.values()),
                                   "live_census": c.last_census, "census_uncertainty": c.census_uncertainty}
                                  for c in OWNED if c.proc is not None],
                     "helpers": list(HELPER_LOG), "unresolved": unresolved}
        summary.update(schema=SUMMARY_SCHEMA, publication_authority="PROVISIONAL until closeout + parent exit/raw audit",
                       proposed_exit_code=code, exit_code=code, host_clock_end=host_end, children=children,
                       all_children_settled=all_settled, all_helpers_settled=helpers_settled,
                       metadata_helpers=list(HELPER_LOG), ownership_manifest=ownership, unsettled_owners=unresolved,
                       reservation_retained=True, parent_block=bool(unresolved),
                       release_requires="NEW parent disposition after runner exit, complete liveness/resource/publication audit",
                       proof_ram_accounting_valid=type(outstanding) is int, proof_ram_outstanding_bytes=outstanding,
                       quarantine_receipts=[c.quarantine_path for c in list(OWNED) + list(HELPERS) if c.quarantined],
                       latch=list(LATCH), cancel_order=co, closeout_boundary=boundary,
                       cancel_before_closeout=co is not None and co < boundary,
                       candidate_observed=bool(outcome.get("sat")), run_tree_bytes_before_summary=tree_bytes,
                       physical_lane_ledger_before_summary=ledger, closeout_defects=defects,
                       retained_capacity_charged=STATE["written"], full_parent_reservation=STATE["reservation"],
                       chunk_claim="held" if not late and not unresolved else "voided")
        summary_path = os.path.join(out_dir, "summary.json")
        try:
            summary_sha, summary_bytes = write_bytes_x(summary_path, serialize(summary))
        except BaseException as exc:
            print("SUMMARY PUBLICATION FAILED", repr(exc), flush=True)
            return EXIT_SAFETY_STOP
        # A parseable pre-publication summary cannot promote anything. Observe completion and reconcile roots NOW.
        after_summary = {"mono": time.monotonic(), "epoch": time.time()}
        if after_summary["mono"] > STATE["mono_end"] + SETTLE or after_summary["epoch"] > STATE["abs_end"] + SETTLE:
            latch("summary publication observed beyond frozen bounds")
            defects.append("late summary publication")
        try:
            led_why, final_ledger = ledger_refusals()
            defects += led_why + confinement_refusals() + preservation_refusals()
            unresolved = unresolved_inventory()
        except BaseException as exc:
            final_ledger = None
            unresolved.append({"kind": "post-summary resource/census unknown", "error": repr(exc)})
            defects.append("post-summary observations unproved")
        for w in defects:
            if "closeout: " + w not in LATCH:
                latch("closeout: " + w)
        code = choose_exit_code(outcome, unresolved, cancelled())
        closeout = {"schema": CLOSEOUT_SCHEMA, "summary_sha256": summary_sha, "summary_bytes": summary_bytes,
                    "exit_code": code, "runner_identity": runner, "summary_publication_observed": after_summary,
                    "parent_block": bool(unresolved) or final_ledger is None, "unresolved": unresolved,
                    "full_parent_reservation_retained_until_disposition": STATE["reservation"],
                    "final_ledger_including_summary": final_ledger, "publication_defects": defects,
                    "closeout_capacity_reserved_bytes": RECORD_MAX,
                    "post_closeout_ledger_reconciled_by_matching_actual_exit": True,
                    "host_clock_required_and_available": host_end is not None,
                    "qualified_item_publications": summary.get("commits", {}) if code == EXIT_PLAN_COMPLETE else {},
                    "authority": "only with matching parent-observed runner exit and complete raw audit",
                    "publication_completion_self_certified": False}
        try:
            closeout_sha = write_x(os.path.join(out_dir, "closeout.json"), closeout)
        except BaseException as exc:
            print("CLOSEOUT PUBLICATION FAILED", repr(exc), flush=True)
            return EXIT_SAFETY_STOP
        final_ledger_why, _post_publication_ledger = ledger_refusals()
        if final_ledger_why:
            return EXIT_SAFETY_STOP
        print("SUMMARY", summary_path, "CLOSEOUT", closeout_sha, "proposed_exit", code, flush=True)
        # LAST observation after every write/fsync/close and output. Parent compares the actual returned code.
        if time.monotonic() > STATE["mono_end"] + SETTLE or time.time() > STATE["abs_end"] + SETTLE:
            return EXIT_SAFETY_STOP
        return choose_exit_code(outcome, unresolved, cancelled())
    finally:
        STATE["cleanup_deadline"] = previous_end



if __name__ == "__main__":
    sys.exit(main())
