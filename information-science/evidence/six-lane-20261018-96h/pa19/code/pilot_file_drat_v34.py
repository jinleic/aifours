#!/usr/bin/env python3
"""PA19 96h D2 file-proof v34 (ms09), combined successor of immutable D2 v33.
CONTROLS ONLY: PHASE='controls-only', ITEMS=[]; exact GO returns before encoder/items; science needs a distinct pin.
Carries all old20 G1-G9/A1-A11 repairs plus all three v5/v33 review HOLDs (guards 5F/2M, integration3M/1m,
tests5M/1m) and the parent dual-disk clarification. Unproved Popen acquisition remains owned even with proc=None.
No speculative PID signalling; one verified SIGTERM plus finite grace only. Successful census/reap completion
is fenced by the ORIGINAL stop grace. Mandatory bounded /bin/date has no native-cutoff exemption.
Every observed (pid,start) is retained; descendant census traverses every current group member and retained root.
All namespace enumeration and user-space IO progress has bounded remaining work. Individual OS/filesystem calls
may be uninterruptible: NO hard native-call latency promise or timeout/escalation is made. Late/unavailable
completion is nonqualifying, retains parent block and reservation, and never supplies synthetic settlement.
Disk accounting separately records distinct-inode logical payload and allocated st_blocks*512 incldirs/root;
cap uses MAX of both, with actual statvfs floors. APFS shared allocation overcounts conservatively.
Retained publications are provisional; NEW independent parent disposition binds complete owners, all known
identity history, exact artifacts/tree census and summary/closeout/ACTUAL exit; any mismatch or missing mandatory
launch publication needs explicit publication-failure disposition. Pinned-directory/exclusive-writer premises remain.
Deferred science command: kissat --time=300; D2 checker1200s, P checker600s; C6 --time=2 with raw ordered finite times.
No test/native/probe/preflight/review is authorized by this source freeze; PA(19,8,6) remains UNDECIDED.
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
CHECKERS = (("A", DRAT, DRAT_OLD[1]),)
DATE = ("/bin/date", "931edbfcbd847f3c1ccb504325a502db313ce20db27634744a7416c3c4b812f0")   # V1: pinned helper
CONTRACT = (RUN + "/contract-v1.json", "55baff0cf1ac1a4b0ab38b0eb1b1fa5a35a47c890f352b79dae4dfea919ffcaa")
LANE_CEILING = 10_737_418_240         # V2: contract resources.per_lane_new_disk_bytes (re-read at prestart)
PILOT_ROOT = LANE + "/evidence/pilot-v1"
CONTROL_DIR = LANE + "/control"            # N8: anchored directory of the SAT-candidate latch
TREE_SUBDIRS = ("children", "cwd", "fifo", "controls")   # N8: created and anchored with the run tree
BUSY_SLOTS = 2                              # N3: contract resources.per_lane_busy_processes (runner + one child)
ALLOCATION_SCHEMA = "PA19-96H-PARENT-ALLOCATION-v2"
KNOWN_SUMMARY_SCHEMAS = {'PA19-96H-PILOT-SUMMARY-v14', 'PA19-96H-PILOT-SUMMARY-v32', 'PA19-96H-PILOT-SUMMARY-v33', 'PA19-96H-PILOT-SUMMARY-v34', 'PA19-96H-PSTREAM-SUMMARY-v4', 'PA19-96H-PSTREAM-SUMMARY-v5', 'PA19-96H-PSTREAM-SUMMARY-v6'}
DISPOSITION_SCHEMA = "PA19-96H-PARENT-RELEASE-v2"
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
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
FAMILY = "ms09"                       # V12: item shape family of this runner
P0 = [4, 3, 3, 3, 3, 3]
ITEMS = []  # Separate science pin + exact GO required after controls qualification
SOLVER_SECONDS = 300
CHECK_SECONDS = 1200
GRACE = 60
TERM_WAIT = 60
STREAM_JOIN = 60
SINK_UNBLOCK = 10
SETTLE_TAIL = TERM_WAIT + STREAM_JOIN + SINK_UNBLOCK + STREAM_JOIN + 30   # 220 s serial settlement bound
PROOF_CAP = 629_145_600              # HARD: the sink never writes more than this to an item proof file
CONTROL_PROOF_CAP = 8 * 1024 * 1024  # HARD cap for control proofs
LOG_CAP = 16 * 1024 * 1024           # HARD per captured stdout+stderr stream
RECORD_MAX = 512 * 1024              # HARD per exact retained JSON record; never truncate evidence
STR_MAX = 1000
ITEM_RECORDS = 2 * 5 + 3 * 3 + 2
CONTROL_RECORDS = 9 * 5 + 2
RUN_RECORDS = 3 + 2 * 3 + 1  # launch,summary,closeout + helper intent/launch/quarantine + spare
CNF_ITEM_MAX = max((it["cnf"][1] for it in ITEMS), default=0)
ITEM_RESERVE = CNF_ITEM_MAX + PROOF_CAP + 2 * LOG_CAP + ITEM_RECORDS * RECORD_MAX
CONTROL_CHILDREN = 9                  # C1 kissat+drat, C2-C4 drat, C5-C7 kissat, C7b drat (V11)
CONTROL_CNF_ALLOW = 1024 * 1024       # six PHP CNFs, each < 64 KiB
CONTROL_RESERVE = (CONTROL_CHILDREN * LOG_CAP + 3 * CONTROL_PROOF_CAP + 1 + 4096 + CONTROL_CNF_ALLOW
                   + CONTROL_RECORDS * RECORD_MAX)
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
ITEM_WORST_SECONDS = (30 + (SOLVER_SECONDS + GRACE + SETTLE_TAIL) + 30 + (CHECK_SECONDS + GRACE + SETTLE_TAIL) + 30
                      + HELPERS_PER_ITEM * HELPER_ALLOW)
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

FEED_BLOCK = 1 << 20                  # S1: RAM block size and collector read size
WRITE_SLICE = 1 << 16                 # S2: feeder os.write slice
HOLD_SECONDS = 30                     # S6: a C7b held feed waits at most this long for the checker reap
PENDING_MAX = 1 << 16                 # S3: no duplicate-literal line is this long; longer pending bytes are kept
DUP_LINE = re.compile(rb"\rc WARNING: detected and deleted duplicate literal (-?[1-9][0-9]*) at position ([1-9][0-9]*) "
                      rb"of proof line ([1-9][0-9]*)\n")
PARSE_LINE = re.compile(rb"\rc parsing input formula with ([0-9]+) variables and ([0-9]+) clauses\n")


KNOWN_CLOSEOUT_SCHEMAS = {'PA19-96H-PILOT-CLOSEOUT-v33', 'PA19-96H-PILOT-CLOSEOUT-v34', 'PA19-96H-PSTREAM-CLOSEOUT-v5', 'PA19-96H-PSTREAM-CLOSEOUT-v6'}
PHASE = "controls-only"
LAUNCH_SCHEMA = "PA19-96H-PILOT-LAUNCH-v34"
SUMMARY_SCHEMA = "PA19-96H-PILOT-SUMMARY-v34"
CLOSEOUT_SCHEMA = "PA19-96H-PILOT-CLOSEOUT-v34"
KNOWN_LAUNCH_SCHEMAS = {'PA19-96H-PILOT-LAUNCH-v14', 'PA19-96H-PILOT-LAUNCH-v32', 'PA19-96H-PILOT-LAUNCH-v33', 'PA19-96H-PILOT-LAUNCH-v34', 'PA19-96H-PSTREAM-LAUNCH-v4', 'PA19-96H-PSTREAM-LAUNCH-v5', 'PA19-96H-PSTREAM-LAUNCH-v6'}
TREE_ENTRY_MAX, TREE_DEPTH_MAX, CENSUS_SECONDS, SHA_SECONDS = 50000, 24, 30.0, 30.0
ALL_PID_SLOTS = 65536
NATIVE_LAUNCH_STOP = datetime.fromisoformat("2026-10-22T20:56:33-07:00").timestamp()
SCIENCE_STOP = datetime.fromisoformat("2026-10-22T21:26:33-07:00").timestamp()
CREATED = {}          # all complete, partial, failed creations and acquisition identities
LIVE_SINKS = []       # file collectors, including inspectable partially constructed objects

ORDER = itertools.count(1)
LATCH = []          # persistent safety/unsettled reasons; non-empty refuses every later child
OWNED = []          # every Child (pre-allocated before Popen), for the computed settlement summary
LIVE_BUFFERS = []
LIVE_FEEDERS = []
HELPERS = []        # V1: every metadata Helper (pre-allocated before Popen)
HELPER_LOG = []     # V1: bounded helper records for the summary
TREE = {}           # N8: anchored directories: path -> (fd, dev, ino)
WRITTEN = {}        # N8: runner-written retained files: path -> (sha256, bytes), re-verified at closeout
KILLPG = os.killpg  # N1: the only signalling primitive (one verified group SIGTERM)
STATE = {"seq": 0, "out": None, "abs_end": None, "chunk_end": None, "remaining_reserve": 0,
         "cancel_order": None, "run_record": None, "go": None, "runner_sha": None, "mono0": None, "mono_end": None,
         "mono_chunk_end": None, "written": 0, "output_limit": None, "last_ledger": None, "reservation": 0,
         "pilot_entries": None, "runner_identity": None, "prior_census": {}, "cleanup_deadline": None}


PUBLICATION_SECONDS = 30.0
UNSETTLED_PUBLICATION_SECONDS = 5.0  # consumes already reserved cleanup allowance, never another stop grace


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


def write_all(fd, data, deadline=None):
    end = work_deadline(PUBLICATION_SECONDS, deadline)
    view = memoryview(data)
    deadline_check(end, "before write progress")
    while view:
        deadline_check(end, "before write progress")
        k = os.write(fd, view[:65536])
        if type(k) is not int or k <= 0 or k > min(len(view), 65536):
            raise OSError(errno.EIO, "write made no valid forward progress")
        view = view[k:]
        deadline_check(end, "after write progress")


def register_written(path, digest, n):
    """G7: successful retained publication, including previously inventoried partial creations."""
    WRITTEN[path] = (digest, n)
    if path in CREATED:
        CREATED[path].update(state="complete", sha256=digest, bytes=n)


def write_x(path, obj, deadline=None):
    try:
        data = serialize(obj)
    except BaseException as exc:
        latch("required record serialization unavailable: %r" % (exc,))
        raise
    return write_bytes_x(path, data, deadline=deadline)[0]


def write_bytes_x(path, data, deadline=None):
    """One remaining publication allowance covers progress, file fsync/close and parent fsync. A syscall may
    stall in kernel: no hard-latency guarantee is asserted. Missing/late completion retains a failed publication."""
    end = work_deadline(PUBLICATION_SECONDS, deadline)
    if deadline is None and STATE.get("cleanup_deadline") is None and STATE.get("mono_end") is not None:
        end = min(end, STATE["mono_end"])
    try:
        deadline_check(end, "before publication creation")
    except BaseException as exc:
        latch("required publication not admitted within remaining budget: %r" % (exc,))
        raise
    charge_output(len(data))
    fd = create_excl(path)
    CREATED[path].update(writer_fd=fd, writer_fd_close_confirmed=False)
    try:
        try:
            write_all(fd, data, deadline=end)
            deadline_check(end, "before publication fsync")
            os.fsync(fd)
            deadline_check(end, "after publication fsync")
        finally:
            try:
                os.close(fd)
                CREATED[path]["writer_fd_close_confirmed"] = True
            except BaseException as exc:
                CREATED[path].update(writer_fd_close_confirmed=None, writer_close_error=repr(exc))
                raise
        deadline_check(end, "after publication close")
        os.fsync(tree_path(path)[0])
        deadline_check(end, "after publication parent fsync")
    except BaseException as exc:
        CREATED[path].update(state="failed", error=repr(exc), publication_complete=False)
        raise
    h = hashlib.sha256(data).hexdigest()
    register_written(path, h, len(data))
    CREATED[path]["publication_complete"] = True
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


def read_regular_bounded(path, limit, dir_fd=None, deadline=None):
    """N7: whole-file read of a regular file of at most `limit` bytes; larger files and growth are refused."""
    end = work_deadline(deadline=deadline)
    fd, st = open_regular(path, dir_fd)
    try:
        if st.st_size > limit:
            raise RuntimeError("%s is %d bytes > limit %d" % (path, st.st_size, limit))
        parts, n = [], 0
        while True:
            deadline_check(end, "bounded metadata read")
            b = os.read(fd, min(1 << 20, limit + 1 - n))
            if not b:
                break
            parts.append(b)
            n += len(b)
            if n > limit:
                raise RuntimeError("%s grew beyond limit %d" % (path, limit))
        deadline_check(end, "bounded metadata read completion")
        return b"".join(parts)
    finally:
        os.close(fd)


def sha_file(path, limit=SHA_FILE_MAX, dir_fd=None, deadline=None):
    fd, before = open_regular(path, dir_fd)
    end = work_deadline(SHA_SECONDS, deadline)
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


def read_tree(path, limit, deadline=None):
    """N8: bounded read of a run-tree file through its anchored directory descriptor."""
    dfd, name = tree_path(path)
    return read_regular_bounded(name, limit, dfd, deadline=deadline)


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


def descendants(pid, pgid, deadline=None, roots=()):
    """Traverse the leader, EVERY observed group member and every retained owned root. Reparenting a group
    member must not hide its out-of-group children. Unknown/unlinked census coverage remains a parent block."""
    end = work_deadline(deadline=deadline)
    members = list_pids(PROC_PGRP_ONLY, pgid)
    deadline_check(end, "process-group listing completion")
    seeds = {pid} | set(members) | set(roots)
    if len(seeds) > LIST_SLOTS or any(type(p) is not int or p <= 0 for p in seeds):
        raise RuntimeError("descendant seed inventory invalid/over cap")
    # Retained out-of-group roots remain known ownership, not merely traversal seeds that can disappear.
    found = (set(members) | set(roots)) - {pid}
    seen, todo = set(seeds), list(seeds)
    while todo:
        deadline_check(end, "descendant traversal")
        q = todo.pop()
        children = list_pids(PROC_PPID_ONLY, q)
        deadline_check(end, "PPID listing completion")
        for child in children:
            if child not in seen:
                if len(seen) >= LIST_SLOTS:
                    raise RuntimeError("descendant census incomplete: process cap")
                seen.add(child)
                found.add(child)
                todo.append(child)
    deadline_check(end, "descendant traversal completion")
    return sorted(found)



def _entry_kind(m):
    return ("dir" if stat.S_ISDIR(m) else "file" if stat.S_ISREG(m) else "symlink" if stat.S_ISLNK(m)
            else "fifo" if stat.S_ISFIFO(m) else "socket" if stat.S_ISSOCK(m) else "other")


def census_entry(st):
    """Retained identity/metadata plus allocated st_blocks*512. Directory allocation is NOT omitted.
    First four directory/eight non-directory fields retain their meanings; allocated bytes are appended."""
    blocks = st.st_blocks
    if type(blocks) is not int or blocks < 0:
        raise RuntimeError("allocated-block accounting unavailable")
    allocated = blocks * 512
    k = _entry_kind(st.st_mode)
    if k == "dir":
        return (k, st.st_dev, st.st_ino, stat.S_IMODE(st.st_mode), allocated)
    return (k, st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns,
            stat.S_IMODE(st.st_mode), st.st_nlink, allocated)


def run_tree_census(root=None):
    base = STATE["out"] if root is None else root
    return walk_bounded(base, TREE[base][0] if root is None else None)


def lane_usage(root=LANE):
    """Budget metric: ENFORCED max(logical payload, allocated blocks incldirs), not 'physical st_size'."""
    return disk_usage(root)["enforced_max_bytes"]


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
        CREATED[path] = {"state": "open", "kind": "file", "identity": None,
                         "acquired_fd": fd, "fd_owner": "raw_creation"}
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
    end = work_deadline()
    ids, unknowns = [], []
    if not isinstance(launch, dict):
        launch = {}
        unknowns.append("runner failed before launch publication; independent parent runner inventory required")
    def add(pid, ident=None, bound=None, leader=False, source=None):
        if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 0:
            unknowns.append("invalid/missing pid at %s" % source)
            return
        if isinstance(ident, dict) and type(ident.get("pid")) is int and ident["pid"] != pid:
            unknowns.append("record/identity PID contradiction at %s" % source)
            add(ident["pid"], ident, bound, leader, source)
            ident = None
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
        deadline_check(end, "ownership manifest record traversal")
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
            if rec.get("no_launch") is True and rec.get("no_launch_proof") == "popen_not_called" \
                    and rec.get("popen_call_started") is False:
                nolaunches.add(path[:-len(".nolaunch.json")])
            else:
                unknowns.append("unproved no-launch record " + path)
        elif path.endswith(".launch.json"):
            launches.add(path[:-len(".launch.json")])
            add(rec.get("pid"), rec.get("identity"), rec.get("started_by_epoch", rec.get("start_epoch")), True, path)
        else:
            # A readable settlement's OWN leader is evidence, even when launch/summary/census is absent.
            leader_ids = [rec[key] for key in ("identity_at_start", "identity") if isinstance(rec.get(key), dict)]
            if not leader_ids:
                add(rec.get("pid"), None, rec.get("started_by_epoch"), True, path)
            for identity in leader_ids:
                add(rec.get("pid"), identity, rec.get("started_by_epoch"), True, path)
            if path.endswith(".QUARANTINE.json"):
                unknowns.append("UNSETTLED receipt " + path)
            if rec.get("launch_state") == "popen_exception_unproven":
                unknowns.append("unproved kernel process acquisition " + path)
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
            deadline_check(end, "ownership JSON work allowance")
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
    deadline_check(end, "ownership manifest completion")
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
    end = work_deadline()
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
    if any(proposed != observed_exit for field, proposed in manifest.get("summary_exit_proposals", [])) \
            and d.get("publication_failure_disposed") is not True:
        return ["summary proposed/declared versus actual runner exit mismatch requires explicit failure disposition"]
    certified = {}
    for x in d["identities"]:
        deadline_check(end, "parent certified identity audit")
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
            deadline_check(end, "complete known-owner liveness audit")
            why += identity_ended_refusals(x, present)
            deadline_check(end, "known-owner liveness completion")
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
    deadline_check(end, "parent disposition validation completion")
    return why


def release_refusals(entry_dir, release, go_sha):
    if release is None or not isinstance(release, dict):
        return ["attempt not explicitly released by single parent allocation: " + entry_dir]
    try:
        if not stat.S_ISDIR(os.lstat(entry_dir).st_mode):
            return ["attempt is not a real directory"]
        publication_unknowns = []
        summary_exit_proposals = []
        launch_path = os.path.join(entry_dir, "launch-record.json")
        launch = None
        if release.get("launch_record_sha256") is None:
            if os.path.lexists(launch_path):
                return ["launch exists but release does not bind its exact bytes"]
            publication_unknowns.append("mandatory runner launch publication absent")
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
                else:
                    for field in ("proposed_exit_code", "exit_code"):
                        if field in summary:
                            proposed = summary[field]
                            if type(proposed) is not int or not -255 <= proposed <= 255:
                                publication_unknowns.append("invalid summary exit proposal " + field)
                            else:
                                summary_exit_proposals.append([field, proposed])
                    if not summary_exit_proposals:
                        publication_unknowns.append("summary exit proposal unavailable")
                    if summary["schema"] in ("PA19-96H-PSTREAM-SUMMARY-v6", "PA19-96H-PILOT-SUMMARY-v34") \
                            and ("proposed_exit_code" not in summary or "exit_code" not in summary):
                        publication_unknowns.append("mandatory current summary exit proposal missing")
            except BaseException as exc:
                publication_unknowns.append("partial/unparseable summary: %r" % (exc,))
        if release.get("closeout_sha256") is None and os.path.lexists(os.path.join(entry_dir, "closeout.json")):
            return ["closeout exists but release does not bind its exact digest"]
        manifest = attempt_owner_manifest(entry_dir, launch)
        manifest["publication_unknowns"] = publication_unknowns
        manifest["summary_exit_proposals"] = summary_exit_proposals
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
    if not isinstance(releases, list) or len(releases) > TREE_ENTRY_MAX:
        return why + ["release inventory missing or over bounded entry cap"], None
    previous_end = STATE.get("cleanup_deadline")
    end = work_deadline()
    STATE["cleanup_deadline"] = end
    try:
        by_dir = {}
        for r in releases:
            deadline_check(end, "parent release entry validation")
            if not isinstance(r, dict) or not isinstance(r.get("dir"), str) or os.path.dirname(r["dir"]) != root \
                    or r["dir"] in by_dir \
                    or (r.get("launch_record_sha256") is not None and not _hex64(r["launch_record_sha256"])) \
                    or (r.get("summary_sha256") is not None and not _hex64(r["summary_sha256"])) \
                    or (r.get("closeout_sha256") is not None and not _hex64(r["closeout_sha256"])):
                why.append("malformed/duplicate release entry")
                continue
            by_dir[r["dir"]] = r
        prior = {}
        entries = bounded_names(root, deadline=end)
        usage_detail = disk_usage()
        usage = usage_detail["enforced_max_bytes"]
        for e in entries:
            deadline_check(end, "prior attempt release audit")
            d = os.path.join(root, e)
            if d == out_dir:
                why.append("output already exists; one-use GO")
            else:
                why += [e + ": " + w for w in release_refusals(d, by_dir.get(d), go_sha)]
                prior[d] = census_digest(d)
        if set(by_dir) != {os.path.join(root, e) for e in entries}:
            why.append("release inventory != complete existing pilot inventory")
        if type(res) is not int or usage + res > LANE_CEILING:
            why.append("max(logical,allocated) lane usage plus exact full reservation exceeds ceiling")
        deadline_check(end, "allocation completion")
        return why, {"allocation_id": a.get("allocation_id"), "reservation_bytes": res,
                     "runner_reservation_bytes": full_reserve, "lane_usage_bytes": usage,
                     "lane_usage_detail": usage_detail, "ceiling_bytes": LANE_CEILING,
                     "pilot_entries": entries, "prior_attempt_census": prior}
    except BaseException as exc:
        return why + ["allocation census incomplete: %r" % (exc,)], None
    finally:
        STATE["cleanup_deadline"] = previous_end



def ledger_refusals():
    """Enforce BOTH logical and allocated accounting through max, never relabel st_size physical consumption.
    Full reservation is retained until NEW parent disposition; precharged capacity cannot disappear."""
    why = []
    previous_end = STATE.get("cleanup_deadline")
    end = work_deadline()
    STATE["cleanup_deadline"] = end
    try:
        entries = bounded_names(PILOT_ROOT, deadline=end)
        expect = sorted(STATE["pilot_entries"] + [os.path.basename(STATE["out"])])
        if entries != expect:
            why.append("pilot root entry set drift")
        for d, old in (STATE.get("prior_census") or {}).items():
            deadline_check(end, "prior attempt census")
            if census_digest(d) != old:
                why.append("prior attempt immutable inventory drift: " + d)
        snap = walk_bounded(LANE, deadline=end)
        own, outside, seen = {}, {}, set()
        belongs = lambda p: p == STATE["out"] or p.startswith(STATE["out"] + os.sep)
        # Outside first: shared hard links cannot subtract already-existing consumption.
        for inside in (False, True):
            for path, value in snap.items():
                deadline_check(end, "dual-metric ledger classification")
                if belongs(path) != inside or (value[1], value[2]) in seen:
                    continue
                seen.add((value[1], value[2]))
                (own if inside else outside)[path] = value
        own_usage = usage_from_census(own)
        outside_usage = usage_from_census(outside, os.lstat(LANE))
        total_logical = outside_usage["logical_distinct_inode_bytes"] + own_usage["logical_distinct_inode_bytes"]
        total_allocated = outside_usage["allocated_st_blocks_bytes"] + own_usage["allocated_st_blocks_bytes"]
        bound_logical = outside_usage["logical_distinct_inode_bytes"] + STATE["reservation"]
        bound_allocated = outside_usage["allocated_st_blocks_bytes"] + STATE["reservation"]
        bound = max(bound_logical, bound_allocated)
        if own_usage["enforced_max_bytes"] > STATE["reservation"] or bound > LANE_CEILING:
            why.append("logical/allocated consumption plus full future reservation exceeds cap")
        led = {"outside_run_usage": outside_usage, "this_run_usage": own_usage,
               "lane_logical_distinct_inode_bytes": total_logical, "lane_allocated_st_blocks_bytes": total_allocated,
               "lane_usage_bytes": max(total_logical, total_allocated), "full_reservation_bytes": STATE["reservation"],
               "logical_future_bound_bytes": bound_logical, "allocated_future_bound_bytes": bound_allocated,
               "conservative_bound_bytes": bound, "ceiling_bytes": LANE_CEILING,
               "charged_logical_capacity_bytes": STATE["written"], "pilot_entries_unchanged": entries == expect,
               "APFS_shared_allocation_overcount": "conservative; allocated blocks incldirs/root are not deduplicated by extent"}
        deadline_check(end, "ledger completion")
        return why, led
    except BaseException as exc:
        return ["ledger/preservation census incomplete: %r" % (exc,)], None
    finally:
        STATE["cleanup_deadline"] = previous_end



def registry_refusals():
    """Fail-closed STOP registry: new-round STOP*/HALT*/SAT-CANDIDATE* markers in LANE/control or
    RUN/control; any change, loss or addition in the inherited old cycle2-root STOP/HALT set."""
    why = []
    end = work_deadline()
    for d in (LANE + "/control", RUN + "/control"):
        for name in bounded_names(d, deadline=end):
            if re.match(r"(?i)^(stop|halt|sat-candidate)", name) or "HALT" in name:
                why.append("new-round marker " + os.path.join(d, name))
    c2 = OLD + "/cycle2"
    present = sorted(n for n in bounded_names(c2, deadline=end) if re.match(r"^(STOP|HALT)", n) or "HALT" in n)
    if present != sorted(OLD_LIVE_MARKERS):
        why.append("inherited cycle2 marker set changed: " + json.dumps(present))
    for name, h in OLD_LIVE_MARKERS.items():
        deadline_check(end, "inherited marker audit")
        try:
            if sha_file(os.path.join(c2, name), deadline=end)[0] != h:
                why.append("inherited marker changed: " + name)
        except Exception as exc:
            why.append(f"inherited marker unreadable: {name}: {exc!r}")
    try:
        if sha_file(REGISTRY[0], deadline=end)[0] != REGISTRY[1]:
            why.append("lane registry changed")
        if sha_file(LAUNCH_CONTRACT[0], deadline=end)[0] != LAUNCH_CONTRACT[1]:
            why.append("launch contract changed")
    except Exception as exc:
        why.append("registry/contract unreadable: %r" % exc)
    deadline_check(end, "registry audit completion")
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



class ProofSink:
    """Owned, inspectable FIFO-to-file transport; a failed construction remains in LIVE_SINKS."""

    def __init__(self, fifo_path, file_path, cap):
        self.fifo_path, self.file_path, self.cap = fifo_path, file_path, cap
        self.dir_fd = self.fifo_name = None
        self.fifo_ino = self.fifo_identity = self.file_identity = None
        self.fifo_create_started = self.fifo_created = False
        self.file_create_started = self.file_created = False
        self.cap_charged = False
        self.file = None
        self.file_closed = None
        self.flush_completed = self.fsync_completed = self.close_completed = False
        self.reader_fd = self.unblock_fd = self.rehash_fd = None
        self.reader_fd_closed = self.unblock_fd_closed = self.rehash_fd_closed = True
        self.sha = hashlib.sha256()
        self.written = self.received = self.discarded = 0
        self.over_cap = self.connected = self.eof = False
        self.error = self.construction_error = None
        self.unblocked_by_runner = False
        self.thread = None
        self.started = False
        self.stage = "initialized"
        self.finish_started = False
        self.finish_deadline = None
        self.finished = None
        LIVE_SINKS.append(self)                 # ownership precedes charge, creation, wrapping and startup
        try:
            if not isinstance(cap, int) or isinstance(cap, bool) or cap < 0:
                raise RuntimeError("invalid proof cap %r" % (cap,))
            self.stage = "charging"
            charge_output(cap)
            self.cap_charged = True
            self.dir_fd, self.fifo_name = tree_path(fifo_path)
            self.stage = "creating_fifo"
            self.fifo_create_started = True
            st = mkfifo_anchored(fifo_path)     # raw creation is inventoried before any later operation can fail
            self.fifo_created = True
            self.fifo_ino = st.st_ino
            self.fifo_identity = [st.st_dev, st.st_ino]
            if not stat.S_ISFIFO(st.st_mode):
                raise RuntimeError("created proof FIFO is not a FIFO")
            self.stage = "opening_file"
            self.file_create_started = True
            self.file = open_wb(file_path)      # helper owns/rolls back the raw fd if fdopen fails
            self.file_created = True
            self.file_closed = False
            st = os.fstat(self.file.fileno())
            self.file_identity = [st.st_dev, st.st_ino]
            if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1 or st.st_size != 0:
                raise RuntimeError("new proof file is not an empty, singly-linked regular file")
            self.stage = "allocating_thread"
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.stage = "starting_thread"
            self.thread.start()
            self.started = True
            self.stage = "running"
        except BaseException as exc:
            self.construction_error = repr(exc)
            self._error("construction", exc)
            self.stage = "construction_failed"
            latch("proof sink construction failed %s: %r" % (self.file_path, exc))
            try:
                self.finish()                 # bounded rollback; never removes a created entry
            except BaseException as rollback_exc:
                self._error("construction rollback", rollback_exc)
                latch("proof sink construction rollback failed %s: %r" % (self.file_path, rollback_exc))
            raise

    def _error(self, what, exc):
        self.error = (self.error + "; " if self.error else "") + "%s:%r" % (what, exc)

    def _close_file(self):
        if self.file is None:
            return
        for what, fn in (("flush", self.file.flush), ("fsync", lambda: os.fsync(self.file.fileno())),
                         ("close", self.file.close)):
            try:
                fn()                          # every cleanup stage is independent; close is attempted after errors
                if what == "flush":
                    self.flush_completed = True
                elif what == "fsync":
                    self.fsync_completed = True
                else:
                    self.close_completed = True
            except BaseException as exc:
                self._error(what, exc)
        try:
            self.file_closed = self.file.closed is True
        except BaseException as exc:
            self.file_closed = None
            self._error("file closed inspection", exc)

    def _run(self):
        self.started = True
        try:
            st = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False)
            if not stat.S_ISFIFO(st.st_mode) or [st.st_dev, st.st_ino] != self.fifo_identity:
                raise RuntimeError("proof FIFO changed before reader open")
            self.reader_fd = os.open(self.fifo_name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC,
                                     dir_fd=self.dir_fd)           # blocks only until finish supplies a writer
            self.reader_fd_closed = False
            st = os.fstat(self.reader_fd)
            if not stat.S_ISFIFO(st.st_mode) or [st.st_dev, st.st_ino] != self.fifo_identity:
                raise RuntimeError("opened proof reader is not the retained FIFO")
            self.connected = True
            while True:
                b = os.read(self.reader_fd, 1 << 20)
                if not b:
                    self.eof = True
                    break
                self.received += len(b)
                if not self.over_cap and self.written + len(b) <= self.cap:
                    view, offset = memoryview(b), 0
                    while offset < len(view):
                        n = self.file.write(view[offset:])
                        if not isinstance(n, int) or isinstance(n, bool) or n <= 0 or n > len(view) - offset:
                            raise RuntimeError("proof file write made invalid progress %r" % (n,))
                        self.sha.update(view[offset:offset + n])
                        self.written += n
                        offset += n
                else:
                    self.over_cap = True       # preserve the hard cap while draining the producer to EOF
                    self.discarded += len(b)
        except BaseException as exc:
            self._error("reader", exc)
        finally:
            if self.reader_fd is not None and not self.reader_fd_closed:
                try:
                    os.close(self.reader_fd)
                    self.reader_fd_closed = True
                except BaseException as exc:
                    self._error("reader fd close", exc)
            self._close_file()

    def _rehash_file(self, end):
        """Hash the retained inode itself, not an independently reopened pathname; close ownership is recorded."""
        if time.monotonic() >= end:
            raise RuntimeError("proof sink allowance exhausted before rehash open")
        dfd, name = tree_path(self.file_path)
        self.rehash_fd, before = open_regular(name, dfd)
        self.rehash_fd_closed = False
        try:
            if [before.st_dev, before.st_ino] != self.file_identity or before.st_nlink != 1 \
                    or before.st_size != self.written or not 0 <= before.st_size <= self.cap:
                raise RuntimeError("rehash descriptor is not the retained singly-linked proof at written size")
            h, n = hashlib.sha256(), 0
            while True:
                if time.monotonic() >= work_deadline(deadline=end):
                    raise RuntimeError("proof sink allowance exhausted during rehash")
                b = os.read(self.rehash_fd, min(1 << 20, self.cap + 1 - n))
                if not b:
                    break
                h.update(b)
                n += len(b)
                if n > self.cap:
                    raise RuntimeError("proof file grew beyond its hard cap during rehash")
            after = os.fstat(self.rehash_fd)
            named = os.stat(name, dir_fd=dfd, follow_symlinks=False)
            if time.monotonic() >= end:
                raise RuntimeError("proof sink allowance exhausted after rehash")
            return [h.hexdigest(), n], before, after, named
        finally:
            try:
                os.close(self.rehash_fd)
                self.rehash_fd_closed = True
            except BaseException as exc:
                self._error("rehash fd close", exc)

    def finish(self, timeout=None):
        """One irreversible attempt under the caller's remaining cleanup allowance; later calls never wait again."""
        if self.finished is not None:
            return self.finished
        self.finish_started = True
        end = work_deadline(SINK_UNBLOCK + STREAM_JOIN if timeout is None else max(0.0, timeout))
        self.finish_deadline = end
        alive = None
        rec = {"fifo": self.fifo_path, "file": self.file_path, "cap": self.cap,
               "fifo_identity": self.fifo_identity, "file_identity": self.file_identity,
               "fifo_same_inode_still_fifo": False, "file_same_identity_regular": False,
               "file_nlink_one": False, "file_size_matches_written": False, "file_within_cap": False,
               "file_metadata_stable_during_rehash": False, "file_identity_at_finish": None,
               "file_rehash": None, "file_rehash_matches": False, "file_integrity": False,
               "finish_deadline_in_bounds": False, "sink_settled": False}
        try:
            alive = self.thread is not None and self.thread.is_alive()
            unblock_end = min(end, time.monotonic() + SINK_UNBLOCK)
            while alive and not self.connected and time.monotonic() < unblock_end:
                try:
                    st = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False)
                    if not stat.S_ISFIFO(st.st_mode) or [st.st_dev, st.st_ino] != self.fifo_identity:
                        raise RuntimeError("proof FIFO changed before unblock")
                    self.unblock_fd = os.open(self.fifo_name,
                                              os.O_WRONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC,
                                              dir_fd=self.dir_fd)
                    self.unblock_fd_closed = False
                    st = os.fstat(self.unblock_fd)
                    if not stat.S_ISFIFO(st.st_mode) or [st.st_dev, st.st_ino] != self.fifo_identity:
                        raise RuntimeError("opened unblock writer is not the retained FIFO")
                    self.unblocked_by_runner = True
                    break
                except OSError as exc:
                    if exc.errno != errno.ENXIO:
                        self._error("unblock", exc)
                        break
                    time.sleep(min(0.05, max(0.0, unblock_end - time.monotonic())))
                except BaseException as exc:
                    self._error("unblock", exc)
                    break
                finally:
                    if self.unblock_fd is not None and not self.unblock_fd_closed:
                        try:
                            os.close(self.unblock_fd)
                            self.unblock_fd_closed = True
                        except BaseException as exc:
                            self._error("unblock fd close", exc)
                alive = self.thread is not None and self.thread.is_alive()
            if self.thread is not None and self.thread.ident is not None:
                self.thread.join(min(STREAM_JOIN, max(0.0, end - time.monotonic())))
            alive = self.thread is not None and self.thread.is_alive()
            if not alive and not self.started and self.file is not None and self.file_closed is not True:
                self._close_file()             # constructor rollback before any reader acquired the file
            if time.monotonic() >= end:
                raise RuntimeError("proof sink cleanup allowance exhausted")
            if self.fifo_identity is not None:
                st = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False)
                rec["fifo_same_inode_still_fifo"] = (stat.S_ISFIFO(st.st_mode)
                                                      and [st.st_dev, st.st_ino] == self.fifo_identity)
            if not alive and self.file_closed is True and self.file_identity is not None:
                if time.monotonic() >= end:
                    raise RuntimeError("proof sink allowance exhausted before file integrity check")
                rec["file_rehash"], before, after, named = self._rehash_file(end)
                rec["file_identity_at_finish"] = [after.st_dev, after.st_ino]
                rec["file_same_identity_regular"] = (stat.S_ISREG(before.st_mode) and stat.S_ISREG(after.st_mode)
                                                       and [before.st_dev, before.st_ino] == self.file_identity
                                                       and [after.st_dev, after.st_ino] == self.file_identity
                                                       and stat.S_ISREG(named.st_mode)
                                                       and [named.st_dev, named.st_ino] == self.file_identity)
                rec["file_nlink_one"] = before.st_nlink == after.st_nlink == named.st_nlink == 1
                rec["file_size_matches_written"] = before.st_size == after.st_size == named.st_size == self.written
                rec["file_within_cap"] = (0 <= before.st_size <= self.cap and 0 <= after.st_size <= self.cap
                                           and 0 <= named.st_size <= self.cap)
                rec["file_metadata_stable_during_rehash"] = (census_entry(before) == census_entry(after)
                                                             == census_entry(named))
                rec["file_rehash_matches"] = rec["file_rehash"] == [self.sha.hexdigest(), self.written]
                rec["file_integrity"] = all(rec[k] is True for k in
                                            ("file_same_identity_regular", "file_nlink_one",
                                             "file_size_matches_written", "file_within_cap",
                                             "file_metadata_stable_during_rehash", "file_rehash_matches"))
                if rec["file_integrity"]:
                    register_written(self.file_path, self.sha.hexdigest(), self.written)
                else:
                    latch("proof file identity/size/rehash mismatch: " + self.file_path)
        except BaseException as exc:
            rec["finish_error"] = repr(exc)
            self._error("finish", exc)
            latch("proof sink finish failed %s: %r" % (self.file_path, exc))
        rec.update(connected=self.connected, eof=self.eof, received=self.received, written=self.written,
                   discarded=self.discarded, over_cap=self.over_cap, error=self.error,
                   construction_error=self.construction_error, unblocked_by_runner=self.unblocked_by_runner,
                   thread_started=self.started, thread_alive_after_join=alive,
                   reader_fd_closed=self.reader_fd_closed, unblock_fd_closed=self.unblock_fd_closed,
                   rehash_fd_closed=self.rehash_fd_closed,
                   file_closed=self.file_closed, flush_completed=self.flush_completed,
                   fsync_completed=self.fsync_completed, close_completed=self.close_completed,
                   sha256_of_written=self.sha.hexdigest())
        rec["finish_deadline_in_bounds"] = time.monotonic() <= end
        rec["sink_settled"] = (rec["finish_deadline_in_bounds"] is True and self.construction_error is None
                                and self.started is True and alive is False and self.error is None
                                and self.reader_fd_closed is True and self.unblock_fd_closed is True
                                and self.rehash_fd_closed is True
                                and self.file_closed is True and self.flush_completed is True
                                and self.fsync_completed is True and self.close_completed is True
                                and rec["fifo_same_inode_still_fifo"] is True and rec["file_integrity"] is True)
        self.finished = rec                     # failed/live transport is frozen too: no repeated waits or hashes
        self.stage = "settled" if rec["sink_settled"] else "unresolved"
        if rec["fifo_same_inode_still_fifo"] is not True:
            latch("proof FIFO replaced, missing or identity unproved: " + self.fifo_path)
        if alive is not False:
            latch("proof sink thread unsettled or unreadable: " + self.fifo_path)
        if self.error is not None:
            latch("proof sink I/O error %s" % self.error)
        if not rec["sink_settled"]:
            latch("proof sink not settled: " + self.file_path)
        return rec

    def census_paths(self):
        return {p for p in (self.fifo_path, self.file_path) if p is not None}

    def census_refusals(self, snapshot):
        """Growth is allowed only for the retained, singly-linked proof inode at its exact settled size."""
        why = []
        if not isinstance(snapshot, dict):
            return ["proof sink census is not a complete snapshot mapping"]
        if self.construction_error is not None:
            why.append("proof sink construction failed: " + self.construction_error)
        fifo = snapshot.get(self.fifo_path)
        if not isinstance(fifo, (tuple, list)) or len(fifo) != 9 or fifo[0] != "fifo" \
                or self.fifo_identity is None or list(fifo[1:3]) != self.fifo_identity:
            why.append("proof FIFO census identity/kind mismatch: " + self.fifo_path)
        proof = snapshot.get(self.file_path)
        if not isinstance(proof, (tuple, list)) or len(proof) != 9 or proof[0] != "file" \
                or self.file_identity is None or list(proof[1:3]) != self.file_identity:
            why.append("proof file census identity/kind mismatch: " + self.file_path)
        else:
            if proof[7] != 1:
                why.append("proof file census link count is not one: " + self.file_path)
            if not isinstance(proof[3], int) or isinstance(proof[3], bool) or proof[3] != self.written \
                    or not isinstance(self.cap, int) or isinstance(self.cap, bool) or not 0 <= proof[3] <= self.cap:
                why.append("proof file census size does not equal written within cap: " + self.file_path)
        return why

    def late_obligations(self):
        state = self.accounting()
        return [{"path": self.fifo_path, "kind": "fifo", "identity": self.fifo_identity,
                 "creation_started": self.fifo_create_started, "created": self.fifo_created,
                 "note": "retain FIFO and any producer/reader endpoint until parent disposition"},
                {"path": self.file_path, "kind": "file", "identity": self.file_identity,
                 "creation_started": self.file_create_started, "created": self.file_created,
                 "written": self.written, "cap": self.cap,
                 "outstanding_growth_bytes": state["outstanding_growth_bytes"],
                 "note": "retain partial proof and reservation; a live collector can still write to the cap"},
                {"what": "proof sink reader and descriptors", "thread_ident": state["thread_ident"],
                 "thread_alive": state["thread_alive"], "reader_fd": self.reader_fd,
                 "reader_fd_closed": self.reader_fd_closed, "unblock_fd": self.unblock_fd,
                 "unblock_fd_closed": self.unblock_fd_closed, "rehash_fd": self.rehash_fd,
                 "rehash_fd_closed": self.rehash_fd_closed, "file_closed": self.file_closed,
                 "construction_error": self.construction_error}]

    def accounting(self):
        alive = None
        inspection_error = None
        try:
            alive = self.thread is not None and self.thread.is_alive()
        except BaseException as exc:
            inspection_error = repr(exc)
        file_open = self.file is not None and self.file_closed is not True
        settled = self.finished is not None and self.finished.get("sink_settled") is True
        growth = max(0, self.cap - self.written) if isinstance(self.cap, int) and not isinstance(self.cap, bool) \
            and (file_open or alive is not False) else 0
        return {"kind": "proof_file_sink", "fifo": self.fifo_path, "file": self.file_path, "cap": self.cap,
                "stage": self.stage, "cap_charged": self.cap_charged,
                "fifo_create_started": self.fifo_create_started, "fifo_created": self.fifo_created,
                "fifo_identity": self.fifo_identity, "file_create_started": self.file_create_started,
                "file_created": self.file_created, "file_identity": self.file_identity,
                "file_open": file_open, "file_closed": self.file_closed,
                "flush_completed": self.flush_completed, "fsync_completed": self.fsync_completed,
                "close_completed": self.close_completed, "thread_allocated": self.thread is not None,
                "thread_started": self.started, "thread_ident": None if self.thread is None else self.thread.ident,
                "thread_alive": alive, "thread_inspection_error": inspection_error,
                "reader_fd": self.reader_fd, "reader_fd_closed": self.reader_fd_closed,
                "unblock_fd": self.unblock_fd, "unblock_fd_closed": self.unblock_fd_closed,
                "rehash_fd": self.rehash_fd, "rehash_fd_closed": self.rehash_fd_closed,
                "received": self.received, "written": self.written, "discarded": self.discarded,
                "over_cap": self.over_cap, "connected": self.connected, "eof": self.eof,
                "unblocked_by_runner": self.unblocked_by_runner, "sha256_of_written": self.sha.hexdigest(),
                "construction_error": self.construction_error, "error": self.error,
                "finish_started": self.finish_started, "finish_deadline": self.finish_deadline,
                "finished": self.finished is not None, "sink_settled": settled,
                "outstanding_growth_bytes": growth,
                "unresolved": not settled or alive is not False or file_open
                              or self.reader_fd_closed is not True or self.unblock_fd_closed is not True
                              or self.rehash_fd_closed is not True
                              or inspection_error is not None}



def new_filter():
    """S3: per-checker capture-filter state; V8: 'cont' = pass through until the next newline after an over-long
    partial line was flushed."""
    return {"raw_sha": hashlib.sha256(), "raw_bytes": 0, "raw_eof": False, "pending": b"", "header_clauses": None,
            "dup_low": 0, "dup_high": 0, "dup_bytes": 0, "tail": 0, "cont": False, "flushes": 0}

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


def open_wb(path):
    """Raw acquisition is inventoried before fdopen; after a successful return the caller holds the file owner."""
    fd = create_excl(path)
    try:
        CREATED[path]["fd_owner"] = "fdopen_handoff"
        return os.fdopen(fd, "wb")
    except BaseException as exc:
        try:
            os.close(fd)
            CREATED[path]["raw_close_confirmed"] = True
        except BaseException as close_exc:
            CREATED[path].update(raw_close_confirmed=None, raw_close_error=repr(close_exc))
            raise
        finally:
            CREATED[path].update(state="failed", error="fdopen transfer: %r" % (exc,))
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
    end = work_deadline()
    snapshot = run_tree_census(root)
    root_stat = os.lstat(root)
    root_entry = census_entry(root_stat)
    raw = json.dumps({"root": root_entry,
                      "entries": sorted((os.path.relpath(path, root), value) for path, value in snapshot.items())},
                     separators=(",", ":"), allow_nan=False).encode()
    digest = hashlib.sha256(raw).hexdigest()
    deadline_check(end, "census digest completion")
    return {"sha256": digest, "entries": len(snapshot), "root_identity": [root_stat.st_dev, root_stat.st_ino],
            "root_census_entry": list(root_entry), "disk_accounting": "logical-and-st_blocks-including-directories"}


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


def receipt_contradictions(rec, allowed_trips=()):
    """Strict ordinary receipt policy: no trips and self stop. The sole explicit exception is
    C5's exact ('proof_cap',) tuple; structural closure alone is never ordinary qualification."""
    bad = receipt_resource_contradictions(rec)
    if not isinstance(rec, dict):
        return bad
    if type(allowed_trips) is not tuple or allowed_trips not in ((), ("proof_cap",)):
        bad.append("unsupported permitted trip policy")
        return bad
    expected_trips = list(allowed_trips)
    if isinstance(rec.get("trips"), list) and rec["trips"] != expected_trips:
        bad.append("trips do not match permitted inventory %r" % (expected_trips,))
    expected_stop = "proof_cap" if allowed_trips else "self"
    if rec.get("stop") != expected_stop:
        bad.append("stop does not match permitted inventory " + expected_stop)
    return bad


def unresolved_inventory():
    """Every unproved launch/process/thread/endpoint/publication remains owned, including proc=None.
    resource_id is exact in-process identity for test-only dispositions; labels never substitute for identity."""
    out = []
    for c in OWNED:
        if c.proc is None:
            if getattr(c, "launch_state", None) == "popen_exception_unproven":
                out.append({"kind": "unknown process acquisition", "resource_id": id(c), "owner_kind": "child",
                            "pid": None, "identity_unknown": True, "launch_state": c.launch_state,
                            "launch_error": c.launch_error, "launch_intent": c.launch_intent,
                            "argv": c.argv, "argv_sha256": c.argv_sha256,
                            "late_obligations": c.late_obligations(), "unsettled": c.unsettled})
            continue
        rec = c.settled_rec
        child_open = (c.reader is not None and c.reader.is_alive()) or c.capture is None or not c.capture.closed \
                     or c.proc.stdout is None or not c.proc.stdout.closed
        bad = receipt_resource_contradictions(rec)
        if bad or child_open:
            out.append({"kind": "child", "resource_id": id(c), "seq": c.seq, "label": c.label,
                        "pid": c.pid, "pgid": c.pgid, "identity_at_start": c.identity_at_start,
                        "started_by_epoch": c.started_epoch, "actual_owned_reap": c.reaped,
                        "wait_lost": c.wait_lost, "launch_state": c.launch_state,
                        "known_identities": list(c.known_identities.values()), "live_census": c.last_census,
                        "census_uncertainty": list(c.census_uncertainty), "late_obligations": c.late_obligations(),
                        "receipt": c.quarantine_path, "receipt_state": c.quarantine_receipt_state,
                        "unknowns": bad + (["actual reader/endpoint still open"] if child_open else [])})
    for h in HELPERS:
        if h.proc is None:
            if getattr(h, "launch_state", None) == "popen_exception_unproven":
                out.append({"kind": "unknown process acquisition", "resource_id": id(h), "owner_kind": "helper",
                            "pid": None, "identity_unknown": True, "launch_state": h.launch_state,
                            "launch_error": h.launch_error, "launch_intent": h.launch_intent,
                            "argv": h.argv, "argv_sha256": h.argv_sha256,
                            "late_obligations": h.late_obligations(), "unsettled": h.unsettled})
            continue
        if h.settled is not True or not h.reaped or h.wait_lost is not None or not h.group_closed_before_reap \
                or h.census_uncertainty or h.grace_completion_in_bounds is not True \
                or h.proc.stdout is None or not h.proc.stdout.closed:
            out.append({"kind": "helper", "resource_id": id(h), "pid": h.pid, "pgid": h.pgid,
                        "identity_at_start": h.identity_at_start, "started_by_epoch": h.started_epoch,
                        "record": h.record, "known_identities": list(h.known_identities.values()),
                        "live_census": h.last_census, "census_uncertainty": list(h.census_uncertainty),
                        "late_obligations": h.late_obligations()})
    for b in LIVE_BUFFERS:
        try:
            state = b.accounting()
            if state.get("collector_alive") is not False or state.get("released") is not True \
                    or state.get("reader_fd_closed") is not True or state.get("unblock_fd_closed") is not True \
                    or state.get("construction_error") is not None \
                    or (state.get("finished") or {}).get("sink_settled") is not True or b.blocks:
                out.append({"kind": "RAM collector", "resource_id": id(b), "runner_identity": STATE.get("runner_identity"),
                            "state": state, "late_obligations": b.late_obligations()})
        except BaseException as exc:
            out.append({"kind": "unknown RAM collector", "resource_id": id(b), "error": repr(exc)})
    for f in LIVE_FEEDERS:
        try:
            state = f.accounting()
            if state.get("unresolved") is not False:
                out.append({"kind": "stdin feeder", "resource_id": id(f), "runner_identity": STATE.get("runner_identity"),
                            "label": f.label, "state": state, "late_obligations": f.late_obligations()})
        except BaseException as exc:
            out.append({"kind": "unknown stdin feeder", "resource_id": id(f), "error": repr(exc)})
    for sink in LIVE_SINKS:
        try:
            state = sink.accounting()
            if state.get("unresolved") is not False or (sink.finished or {}).get("sink_settled") is not True:
                out.append({"kind": "file sink", "resource_id": id(sink), "runner_identity": STATE.get("runner_identity"),
                            "state": state, "late_obligations": sink.late_obligations()})
        except BaseException as exc:
            out.append({"kind": "unknown file sink", "resource_id": id(sink), "error": repr(exc)})
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


def deadline_check(end, what):
    """User-space progress fence only; individual OS calls may be uninterruptible. Late completion never qualifies."""
    if time.monotonic() > end:
        raise TimeoutError(what + ": remaining operation budget exhausted")


def bounded_names(path_or_fd, deadline=None, cap=TREE_ENTRY_MAX):
    """Incrementally cap enumeration BEFORE allocating/sorting the complete namespace. No os.listdir fallback."""
    end = work_deadline(deadline=deadline)
    names = []
    with os.scandir(path_or_fd) as scan:
        for entry in scan:
            deadline_check(end, "namespace enumeration")
            if len(names) >= cap:
                raise RuntimeError("namespace entry cap exhausted; inventory incomplete")
            names.append(entry.name)
    deadline_check(end, "before bounded namespace sort")
    names.sort()
    deadline_check(end, "after bounded namespace sort")
    return names


def usage_from_census(snapshot, root_stat=None):
    """Distinct-inode logical payload bytes and allocated blocks, including directories/root allocation.
    APFS clones/shared extents can be counted repeatedly across different inodes: deliberately conservative."""
    logical = allocated = 0
    seen = set()
    if root_stat is not None:
        root = census_entry(root_stat)
        seen.add((root[1], root[2]))
        allocated += root[-1]
        if root[0] != "dir":
            logical += root[3]
    for value in snapshot.values():
        key = (value[1], value[2])
        if key in seen:
            continue
        seen.add(key)
        allocated += value[-1]
        if value[0] != "dir":
            logical += value[3]
    return {"logical_distinct_inode_bytes": logical, "allocated_st_blocks_bytes": allocated,
            "enforced_max_bytes": max(logical, allocated), "distinct_inodes": len(seen),
            "directory_allocation_included": True, "APFS_shared_allocation_overcount": "conservative"}


def disk_usage(root=LANE):
    end = work_deadline()
    before = os.lstat(root)
    if not stat.S_ISDIR(before.st_mode):
        raise RuntimeError("disk usage root is not a real directory")
    snapshot = walk_bounded(root, deadline=end)
    after = os.lstat(root)
    if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
        raise RuntimeError("disk usage root identity changed")
    result = usage_from_census(snapshot, after)
    deadline_check(end, "dual disk usage completion")
    return result


def receipt_resource_contradictions(rec):
    """Independent resource/reap/publication closure checks, not an ordinary UNSAT qualifier.
    A consistent stopped receipt may describe closed resources without authorizing scientific use."""
    if not isinstance(rec, dict):
        return ["receipt missing"]
    bad = []
    for key in ("settled", "actual_owned_reap", "group_empty_after_reap", "settlement_publication_in_bounds",
                "native_exec_identity_verified", "grace_completion_in_bounds"):
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
    trips, stop = rec.get("trips"), rec.get("stop")
    if not isinstance(trips, list):
        bad.append("trip inventory missing/not list")
    else:
        if any(not isinstance(trip, str) or not trip for trip in trips):
            bad.append("trip inventory has invalid entries")
        elif len(set(trips)) != len(trips):
            bad.append("trip inventory has duplicate entries")
        if stop == "self" and trips:
            bad.append("self stop with nonempty trips")
        elif isinstance(stop, str) and stop and stop != "self":
            if not trips:
                bad.append("non-self stop with empty trips")
            if stop not in trips:
                bad.append("stop missing from trip inventory")
    if not isinstance(stop, str) or not stop:
        bad.append("stop missing/not nonempty string")
    if not _hex64(rec.get("output_sha256")):
        bad.append("capture digest missing")
    return bad


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
        self.launch_state = "not_requested"
        self.launch_error = None
        self.launch_intent = None
        self.stop_grace_end = None
        self.grace_completion_in_bounds = None

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

    def _reap_once(self, deadline=None):
        if self.quarantined or self.reaped or self.wait_lost is not None:
            return self.exit_status if self.reaped else None
        if deadline is not None:
            deadline_check(deadline, "before actual owned reap")
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
        self.proc.returncode = rc               # record the real reap even when its completion is late
        if deadline is not None and time.monotonic() > deadline:
            self.grace_completion_in_bounds = False
            self.census_uncertainty.append("actual owned reap completed after stop-grace deadline")
            return None
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
        if self.stop_grace_end is not None and time.monotonic() > self.stop_grace_end:
            self.term_refused_mono = time.monotonic()
            self.term_delivery = {"delivered": False, "refused": "verified stop completed after grace authority"}
            latch("stop refused after admitted grace; parent block")
            return
        self.term_sent_mono, self.term_sent_epoch = time.monotonic(), time.time()
        try:
            KILLPG(self.pgid, signal.SIGTERM)
            self.term_delivery = {"delivered": True, "pgid": self.pgid, "evidence": evidence}
        except OSError as exc:
            self.term_delivery = {"delivered": False, "pgid": self.pgid, "error": repr(exc), "evidence": evidence}

    def late_obligations(self):
        return [{"what": "runner-owned stdout read endpoint", "note": "closes at runner exit; survivor may see EPIPE"}]

    def known_pids(self):
        return sorted({item["pid"] for item in self.known_identities.values()})

    def remember_identity(self, item):
        pid = item["pid"]
        ident = item.get("identity")
        start = ident.get("start") if isinstance(ident, dict) else None
        key = (pid, tuple(start) if isinstance(start, list) else None)
        if key not in self.known_identities:
            if len(self.known_identities) >= LIST_SLOTS:
                raise RuntimeError("persistent identity history cap exhausted; completeness unproven")
            self.known_identities[key] = dict(item, first_observed_by_epoch=item.get("observed_by_epoch"), observations=1)
        else:
            retained = self.known_identities[key]
            retained["observations"] += 1
            retained["last_observed_by_epoch"] = item.get("observed_by_epoch")
            retained["ever_unreadable"] = retained.get("ever_unreadable", False) or item.get("identity_error") is not None
        # A distinct start/unknown observation never overwrites a previous readable start for this PID.
        starts = {k[1] for k in self.known_identities if k[0] == pid and k[1] is not None}
        if len(starts) > 1:
            reason = "multiple retained starts for pid %s; owned census identity uncertain" % pid
            if reason not in self.census_uncertainty:
                self.census_uncertainty.append(reason)

    def live_census(self, deadline=None):
        if self.quarantined:
            return self.last_census or {"complete": False, "unknown": "UNSETTLED before census completed"}
        end = work_deadline(deadline=deadline)
        if self.cleanup_end is not None:
            end = min(end, self.cleanup_end)
        out = {"leader_pid": self.pid, "pgid": self.pgid, "at_epoch": time.time(), "complete": True,
               "start_identity": self.identity_at_start, "group_members": [], "descendants": []}
        try:
            deadline_check(end, "before live group census")
            members = list_pids(PROC_PGRP_ONLY, self.pgid)
            deadline_check(end, "after live group census")
            found = descendants(self.pid, self.pgid, deadline=end, roots=self.known_pids())
            for category, pids in (("group_members", members), ("descendants", found)):
                for pid in pids:
                    deadline_check(end, "before exact identity observation")
                    ident, err = bsd_identity(pid)
                    if ident is None and pid == self.pid and isinstance(self.identity_at_start, dict) \
                            and self.identity_at_start.get("start"):
                        ident = dict(self.identity_at_start, live_read_unavailable=True)
                    item = {"pid": pid, "identity": ident, "identity_error": err, "rss_bytes": task_rss(pid),
                            "observed_by_epoch": out["at_epoch"]}
                    out[category].append(item)
                    self.remember_identity(item)
                    deadline_check(end, "after exact identity/RSS observation")
                    if ident is None and pid != self.pid:
                        out["complete"] = False
            if not out["complete"]:
                reason = "unreadable nonleader census identity"
                if reason not in self.census_uncertainty:
                    self.census_uncertainty.append(reason)
            if self.census_uncertainty:
                out["complete"] = False          # past unproved/reused identity is not silently cleared by a retry
            deadline_check(end, "successful live census completion")
        except BaseException as exc:
            out.update(complete=False, census_error=repr(exc))
            if repr(exc) not in self.census_uncertainty:
                self.census_uncertainty.append(repr(exc))
        self.last_census = out
        return out

    def _unsettled_receipt(self):
        return {"schema": "PA19-UNSETTLED-v3", "pid": self.pid, "pgid": self.pgid, "argv": self.argv,
                "identity_at_start": self.identity_at_start, "started_by_epoch": self.started_epoch,
                "argv_sha256": self.argv_sha256, "launch_state": self.launch_state, "launch_error": self.launch_error,
                "launch_intent": self.launch_intent, "stop_grace_end": self.stop_grace_end,
                "grace_completion_in_bounds": self.grace_completion_in_bounds,
                "stop": self.stop, "term_delivery": self.term_delivery, "settlement": "UNSETTLED",
                "actual_owned_reap": self.reaped, "wait_lost": self.wait_lost,
                "owned_wait_status": self.wait_status, "observed_returncode": self.exit_status,
                "known_identities": list(self.known_identities.values()), "live_census": self.last_census,
                "census_uncertainty": list(self.census_uncertainty), "late_obligations": self.late_obligations(),
                "reservation": "retained; NEW parent disposition required", "runner_action": "return, no further wait/signal"}

    def _receipt_valid(self, deadline=None):
        try:
            if deadline is None:
                return False
            deadline_check(deadline, "existing quarantine validation entry")
            record = json.loads(read_tree(self.quarantine_path, RECORD_MAX, deadline=deadline))
            deadline_check(deadline, "existing quarantine validation completion")
            return record == self.unsettled
        except BaseException:
            return False

    def _record_unsettled(self, reason="bounded settlement unproven"):
        if self.quarantined:
            return
        self.quarantined = True               # irreversible before publication; no more process census/wait
        self.census_uncertainty.append(str(reason))
        latch("UNSETTLED pid %s: %s; reservation retained" % (self.pid, reason))
        self.unsettled = self._unsettled_receipt()
        if self.quarantine_path is None:
            self.quarantine_receipt_state = "unpublishable: no anchored tree"
            return
        # Publication consumes ONLY the already allocated common cleanup allowance, never a fresh grace.
        end = self.cleanup_end
        if end is None:
            self.quarantine_receipt_state = "unpublished: no common publication budget"
            return
        end = work_deadline(UNSETTLED_PUBLICATION_SECONDS, end)
        if time.monotonic() >= end:
            self.quarantine_receipt_state = "unpublished: common cleanup allowance exhausted"
            return
        try:
            write_x(self.quarantine_path, self.unsettled, deadline=end)
            deadline_check(end, "quarantine publication completion")
            self.quarantine_receipt_state = "written"
        except FileExistsError:
            self.quarantine_receipt_state = "written" if time.monotonic() <= end and self._receipt_valid(deadline=end) \
                and time.monotonic() <= end else "contradictory/unverified existing receipt"
        except BaseException as exc:
            self.quarantine_receipt_state = "late/unavailable publication; parent block: %r" % (exc,)

    def reap_owned(self, term_wait):
        if self.quarantined:
            return None
        if self.reaped:
            return self.exit_status if self.grace_completion_in_bounds is not False else None
        entry = time.monotonic()
        if self.cleanup_end is None:
            self.cleanup_end = work_deadline(term_wait + UNSETTLED_PUBLICATION_SECONDS)
        end = min(entry + term_wait, self.cleanup_end)
        t0 = self.term_sent_mono if self.term_sent_mono is not None else self.term_refused_mono
        if t0 is not None:
            end = min(end, t0 + term_wait)
        self.stop_grace_end = end
        while time.monotonic() < end:
            try:
                census = self.live_census(deadline=end)
                deadline_check(end, "census completion before exit observation")
                rc = self.observe_exit()
                deadline_check(end, "exit observation before owned reap")
                if self.wait_lost is not None:
                    break
                others = [x for x in census.get("group_members", []) if x["pid"] != self.pid]
                if rc is not None and census.get("complete") is True and not others and not census.get("descendants"):
                    deadline_check(end, "successful census/reap boundary")
                    result = self._reap_once(deadline=end)
                    if result is not None and time.monotonic() <= end:
                        self.group_closed_before_reap = True
                        self.grace_completion_in_bounds = True
                        return result
                    break
                if self.stop is None:
                    self.stop = "nonleader_resources" if rc is not None else "reap_of_live_owner"
                if not self.stop_requested():
                    self.term(self.stop)
                time.sleep(min(SUPERVISE_SLICE, max(0.0, end - time.monotonic())))
            except BaseException as exc:
                reason = "reap: %r" % (exc,)
                if reason not in self.census_uncertainty:
                    self.census_uncertainty.append(reason)
                if time.monotonic() < end:
                    time.sleep(min(SUPERVISE_SLICE, max(0.0, end - time.monotonic())))
        self.grace_completion_in_bounds = False
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
        if any(getattr(c, "launch_state", None) == "popen_exception_unproven" for c in OWNED) \
                or any(h is not self and getattr(h, "launch_state", None) == "popen_exception_unproven" for h in HELPERS):
            why.append("an unproved process acquisition retains ownership")
        if any(c.proc is not None and ((c.settled_rec or {}).get("settled") is not True
                or (c.reader is not None and c.reader.is_alive()) or c.capture is None or not c.capture.closed
                or c.proc.stdout is None or not c.proc.stdout.closed) for c in OWNED) \
                or any(h is not self and h.proc is not None and h.settled is not True for h in HELPERS):
            why.append("an owned process is not affirmatively settled")
        m, e = time.monotonic(), time.time()
        if e > NATIVE_LAUNCH_STOP:
            why.append("after frozen native launch cutoff (mandatory date is not exempt)")
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
            self.launch_intent = self.intent_path
            write_x(self.intent_path, {"schema": "PA19-OWNER-INTENT-v1", "launch_order": self.launch_order,
                                      "argv": self.argv, "argv_sha256": self.argv_sha256, "kind": "helper", "runner_identity": STATE.get("runner_identity")})
        self.launch_state = "intent_published" if self.intent_path is not None else "prepared_without_run_tree"
        why = exe_refusals(self.exe_binding) + self.admission_refusals()
        if why:
            self.launch_state = "proved_no_launch_before_popen"
            self.record.update(no_launch=True, no_launch_proof="popen_not_called", popen_call_started=False, refused=why)
            if self.intent_path is not None:
                write_x(self.intent_path.replace(".intent.json", ".nolaunch.json"), self.record)
            raise HelperRefused("; ".join(why))
        # Actual birth boundary after every blocking observation and intent publication.
        if time.time() > NATIVE_LAUNCH_STOP:
            self.launch_state = "proved_no_launch_before_popen"
            raise HelperRefused("mandatory date actual spawn is after native cutoff")
        self.popen_call_mono = time.monotonic()
        self.cleanup_end = work_deadline(HELPER_ALLOW, self.popen_call_mono + HELPER_ALLOW)
        self.launch_state = "popen_entered"
        try:
            self.proc = subprocess.Popen(self.argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, start_new_session=True, close_fds=True,
                                         env=CHILD_ENV)
        except BaseException as exc:
            # Popen may create a kernel child before raising in parent-side constructor work. No PID is guessed.
            self.launch_state = "popen_exception_unproven"
            self.launch_error = repr(exc)
            self.record.update(launch_state=self.launch_state, launch_error=self.launch_error, no_launch_proven=False)
            self._record_unsettled("Popen acquisition exception; no-child outcome unproven")
            raise
        rc = None
        try:
            self.pid = self.pgid = self.proc.pid
            self.launch_state = "process_retained"
            self.started_mono, self.started_epoch = time.monotonic(), time.time()
            self.identity_at_start = identity_checked(self.pid, os.getpid())
            if self.launch_path is not None:
                write_x(self.launch_path, {"kind": "helper", "pid": self.pid, "pgid": self.pgid,
                                          "identity": self.identity_at_start, "started_by_epoch": self.started_epoch,
                                          "launch_order": self.launch_order, "exe_binding": self.exe_binding,
                                          "argv": self.argv, "argv_sha256": self.argv_sha256})
            if self.started_epoch > NATIVE_LAUNCH_STOP:
                raise RuntimeError("date actual launch completion observed after native cutoff")
            drift = exe_refusals(self.exe_binding)
            if drift:
                raise RuntimeError(drift)
            self._supervise_and_capture()
        except BaseException as exc:
            self.record["exception"] = repr(exc)
            self.stop = self.stop or "helper_exception"
        finally:
            self.cleanup_end = min(self.cleanup_end, work_deadline(HELPER_TERM_WAIT + UNSETTLED_PUBLICATION_SECONDS))
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
            if any(p != self.pid for p in self.known_pids()):
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
        if self.grace_completion_in_bounds is not True:
            problems.append("owned reap/census completion not within stop grace")
        if not self.reaped or rc is None or self.wait_lost is not None:
            problems.append("actual owned reap unproven")
        if not isinstance(self.identity_at_start, dict) or not self.identity_at_start.get("start"):
            problems.append("required helper full start identity unproven; no timestamp qualifies")
        if self.quarantined or self.term_refused_mono is not None:
            problems.append("UNSETTLED or unverifiable stop")
        if not self.group_closed_before_reap or self.census_uncertainty:
            problems.append("group/descendant census closure unproven")
        if any(p != self.pid for p in self.known_pids()):
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
                           launch_state=self.launch_state, grace_completion_in_bounds=self.grace_completion_in_bounds,
                           owned_wait_status=self.wait_status, observed_returncode=self.exit_status,
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
        self.launch_intent = self.intent_path
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
            self.cleanup_end = self.deadline_mono + SETTLE_TAIL
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
            self.launch_state = "intent_published"
            # Hashing/admission/intent are blocking; actual spawn boundary rechecks all frozen timing.
            why = exe_refusals(self.exe_binding)
            if LATCH or cancelled() or time.time() > NATIVE_LAUNCH_STOP or time.time() + wall > self.deadline \
                    or time.monotonic() + wall > self.deadline_mono:
                why.append("latch/cancel/remaining allowance at actual spawn boundary")
            if why:
                self.refused = why
                self.launch_state = "proved_no_launch_before_popen"
                write_x(self.nolaunch_path, {"no_launch": True, "no_launch_proof": "popen_not_called",
                                           "popen_call_started": False, "why": why, "launch_order": self.launch_order})
                self._close_refused_capture()
                return
            self.popen_call_mono = time.monotonic()
            self.launch_state = "popen_entered"
            child_env = dict(CHILD_ENV, TMPDIR=cwd)
            try:
                self.proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL if feeder is None else feeder.rfd,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                             start_new_session=True, close_fds=True, cwd=cwd, env=child_env)
            except BaseException as exc:
                self.launch_state = "popen_exception_unproven"
                self.launch_error = repr(exc)
                self._record_unsettled("Popen acquisition exception; no-child outcome unproven")
                raise
            self.pid = self.pgid = self.proc.pid   # before ANY other fallible step
            self.launch_state = "process_retained"
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
            if self.started_epoch > NATIVE_LAUNCH_STOP:
                raise RuntimeError("native launch completion observed after cutoff")
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
        found = sorted(p for p in self.known_pids() if p != self.pid)
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
            if self.grace_completion_in_bounds is not True:
                problems.append("owned reap/census completion not within stop grace")
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
                        or feed_rec.get("exception") is not None or feed_rec.get("close_error") is not None \
                        or feed_rec.get("read_endpoint_closed") is not True \
                        or feed_rec.get("write_endpoint_closed") is not True:
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
            if any(p != self.pid for p in self.known_pids()) or self.descendants:
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
                   "grace_completion_in_bounds": self.grace_completion_in_bounds, "stop_grace_end": self.stop_grace_end,
                   "owned_wait_status": self.wait_status, "observed_returncode": self.exit_status,
                   "launch_state": self.launch_state,
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
                publication = write_x(self.settle_path, dict(rec, provisionally_resources_closed=ok), deadline=self.cleanup_end)
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



def run_child(argv, label, wall, reserve, inputs, sink=None):
    """Prepared outputs -> admission -> spawn -> supervise -> settle.  Returns (rec|None, lines, refusal)."""
    ch = None
    try:
        cwd = os.path.join(STATE["out"], "cwd", "%02d-%s" % (STATE["seq"] + 1, label))
        mkdir_anchored(cwd)  # r4#4: inside the cleanup guard; N8: exclusive and anchored
        ch = Child(argv, label, wall, reserve, inputs, sink, cwd)
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



def settle_all():
    """G4: exactly ONE pass. Each Child performs idempotent stages under its single remaining deadline.
    An escaped cleanup never gets another round of joins or process waits."""
    for c in tuple(OWNED):
        if c.proc is None:
            if getattr(c, "launch_state", None) == "popen_exception_unproven":
                c._record_unsettled("unproved process acquisition remains owned with unknown PID")
            continue
        if c.settled_rec is not None:
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


def run_kissat(cnf_path, proof_file, label, seconds, cap, reserve, inputs):
    argv = [KISSAT[0], "-q", "-f", "--seed=1", "--time=%d" % seconds, cnf_path]
    sink = None
    if proof_file is not None:
        sink = ProofSink(os.path.join(STATE["out"], "fifo", label + ".proof.fifo"), proof_file, cap)   # N8: anchored
        argv.append(sink.fifo_path)
    return run_child(argv, label + ".kissat", seconds, reserve, dict(inputs, proof_file=proof_file, proof_cap=cap), sink)



def run_drat(cnf_path, proof_path, label, seconds, reserve, inputs):
    return run_child([DRAT, cnf_path, proof_path, "-i", "-t", str(seconds)], label + ".drat", seconds, reserve,
                     dict(inputs, cnf=cnf_path, proof=proof_path))


def sink_integrity(sink_rec):
    """Closure/file integrity shared by ordinary, capped and never-connected proof sinks."""
    if not isinstance(sink_rec, dict):
        return False
    r = sink_rec
    true_fields = ("sink_settled", "thread_started", "reader_fd_closed", "unblock_fd_closed", "rehash_fd_closed", "file_closed",
                   "flush_completed", "fsync_completed", "close_completed", "fifo_same_inode_still_fifo",
                   "file_same_identity_regular", "file_nlink_one", "file_size_matches_written", "file_within_cap",
                   "file_metadata_stable_during_rehash", "file_rehash_matches", "file_integrity",
                   "finish_deadline_in_bounds")
    if any(r.get(k) is not True for k in true_fields) or r.get("thread_alive_after_join") is not False:
        return False
    if "error" not in r or r["error"] is not None or "construction_error" not in r \
            or r["construction_error"] is not None:
        return False
    if any(not isinstance(r.get(k), int) or isinstance(r[k], bool) or r[k] < 0
           for k in ("cap", "written", "received", "discarded")):
        return False
    ident = r.get("file_identity")
    if not isinstance(ident, list) or len(ident) != 2 \
            or any(not isinstance(x, int) or isinstance(x, bool) or x < 0 for x in ident) \
            or r.get("file_identity_at_finish") != ident:
        return False
    digest = r.get("sha256_of_written")
    return (isinstance(digest, str) and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
            and r["written"] <= r["cap"] and r["received"] == r["written"] + r["discarded"]
            and r.get("file_rehash") == [digest, r["written"]])


def sink_complete(sink_rec):
    """Only an affirmatively closed, uncapped complete proof is eligible for ordinary qualification."""
    return (sink_integrity(sink_rec) and sink_rec.get("connected") is True and sink_rec.get("eof") is True
            and sink_rec.get("over_cap") is False and sink_rec.get("unblocked_by_runner") is False
            and sink_rec.get("discarded") == 0 and sink_rec.get("received") == sink_rec.get("written"))


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



def file_checker_defects(name, cnf_expect, proof_bytes, drat_rec, drat_lines):
    """Canonical file-checker records plus independently validated, noncontradictory ownership receipts."""
    bad = []
    X = name + "."
    rec = drat_rec if isinstance(drat_rec, dict) else {}
    if rec.get("returncode") != 0 or rec.get("stop") != "self":
        bad.append(defect(X + "EXIT", "checker not self-exit rc0"))
    st = status_lines(drat_lines)
    if st != ["s VERIFIED"]:
        bad.append(defect(X + "STATUS", "status lines %r != ['s VERIFIED']" % (st,)))
    v, c = cnf_expect[2].split()[2:4]
    hdr = [s[:200] for s in drat_lines if s.startswith("c parsing input formula")]
    if hdr != ["c parsing input formula with %s variables and %s clauses" % (v, c)]:
        bad.append(defect(X + "HEADER", "parser header records %r != the CNF pin header" % (hdr[:4],)))
    fin = [s[:200] for s in drat_lines if s.startswith("c finished parsing")]
    if not isinstance(proof_bytes, int) or isinstance(proof_bytes, bool) \
            or fin != ["c finished parsing, read %d bytes from proof file" % proof_bytes]:
        bad.append(defect(X + "CONSUMED", "consumed records %r != [read %r bytes]" % (fin[:4], proof_bytes)))
    for pat, key in FORBIDDEN:
        if any(pat in s for s in drat_lines):
            bad.append(defect(X + "FORBIDDEN." + key, "checker output contains %r" % pat))
    if not rec.get("settled") or rec.get("capture_over_cap") is not False:
        bad.append(defect(X + "SETTLE", "settlement/capture defect seq %s" % rec.get("seq")))
    receipt_bad = receipt_contradictions(drat_rec, allowed_trips=())
    if receipt_bad:
        bad.append(defect(X + "RECEIPT", "contradictory or incomplete checker receipt %r" % (receipt_bad,)))
    if rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect(X + "TIMING", "exit not observed by the checker deadline (N4)"))
    return bad



def qualify_unsat(cnf_expect, solver_rec, kissat_lines, proof_sha, proof_bytes, proof_cap, drat_rec, drat_lines,
                  cnf_post, proof_post):
    """UNSAT requires exact solver output, sink-bound proof identity, fresh post-hashes and complete receipts."""
    bad = []
    rec = solver_rec if isinstance(solver_rec, dict) else {}
    sink = rec.get("proof_sink")
    if rec.get("returncode") != 20 or rec.get("stop") != "self":
        bad.append(defect("SOLVER_EXIT", "solver not self-exit rc20"))
    if kissat_lines != ["s UNSATISFIABLE"]:
        bad.append(defect("SOLVER_OUTPUT", "complete solver output %r != ['s UNSATISFIABLE']" % (kissat_lines[:4],)))
    if not sink_complete(sink):
        bad.append(defect("SINK_INCOMPLETE", "proof sink incomplete/over cap/error"))
    if not isinstance(proof_bytes, int) or isinstance(proof_bytes, bool) or proof_bytes <= 0 or proof_bytes > proof_cap:
        bad.append(defect("PROOF_SIZE", "proof size outside (0, cap]"))
    if not isinstance(sink, dict) or proof_sha != sink.get("sha256_of_written") \
            or not isinstance(proof_bytes, int) or isinstance(proof_bytes, bool) \
            or type(sink.get("written")) is not int or proof_bytes != sink.get("written"):
        bad.append(defect("PROOF_SINK_BINDING", "passed proof digest/bytes do not equal the solver sink measurement"))
    bad += file_checker_defects("A", cnf_expect, proof_bytes, drat_rec, drat_lines)
    if cnf_post != (cnf_expect[0], cnf_expect[1]):
        bad.append(defect("CNF_POST", "CNF file digest/bytes != expected"))
    if proof_post != (proof_sha, proof_bytes):
        bad.append(defect("PROOF_POST", "fresh proof file digest/bytes != the passed proof measurement"))
    if not rec.get("settled") or rec.get("capture_over_cap") is not False:
        bad.append(defect("SOLVER_SETTLE", "settlement/capture defect seq %s" % rec.get("seq")))
    receipt_bad = receipt_contradictions(solver_rec, allowed_trips=())
    if receipt_bad:
        bad.append(defect("SOLVER_RECEIPT", "contradictory or incomplete solver receipt %r" % (receipt_bad,)))
    if rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect("SOLVER_TIMING", "exit not observed by the solver deadline (N4)"))
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
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in nums):
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
    """Sequential controls only: safety outranks intended outcomes; every checker is followed by fresh file hashes."""
    recs = {}
    artifacts = {}                              # immutable intended bytes, including capped and empty proof files
    d = os.path.join(STATE["out"], "controls")
    per_child = LOG_CAP + CONTROL_PROOF_CAP + 3 * RECORD_MAX

    def fail(name, why):
        recs[name] = dict(recs.get(name, {}), failed=why)
        if LATCH or cancelled():
            recs[name].update(safety_latch=list(LATCH), cancelled=cancelled())
        return False, recs

    def launch(fn, *args):
        if LATCH or cancelled():
            return None, [], ["controls stopped by a safety latch or cancellation"]
        return fn(*args)                       # run_child retains the final native-pin/admission authority

    def post_files(name):
        fresh, errors = {}, []
        for path, pin in artifacts.items():
            try:
                fresh[path] = sha_tree(path, limit=pin[1])
                if fresh[path] != pin:
                    errors.append("control artifact changed %s: %r != %r" % (path, fresh[path], pin))
            except BaseException as exc:
                errors.append("control artifact rehash failed %s: %r" % (path, exc))
        recs.setdefault(name, {})["artifact_post"] = fresh
        if errors:
            recs[name]["artifact_integrity_errors"] = errors
            for error in errors:
                latch(error)
            return None
        return fresh

    def adopt_sink(name, path, rec):
        sink = rec.get("proof_sink") if isinstance(rec, dict) else None
        if not sink_integrity(sink):
            return None
        artifacts[path] = (sink["sha256_of_written"], sink["written"])
        return post_files(name)                # baseline is the sink measurement, never an unbound fresh digest

    c1name = "C1_positive_php6x5"
    if LATCH or cancelled():
        return fail(c1name, "controls not admitted while safety/cancellation is pending")
    raw = php_cnf(6, 5)
    cnf = os.path.join(d, "php6x5.cnf")
    h, n = write_bytes_x(cnf, raw)
    artifacts[cnf] = (h, n)
    exp = (h, n, raw.split(b"\n", 1)[0].decode())
    proof = os.path.join(d, "php6x5.drat")
    ks, kl, rf = launch(run_kissat, cnf, proof, "C1", CONTROL_CHILD_WALL, CONTROL_PROOF_CAP,
                        per_child, {"cnf_pin": [h, n]})
    recs[c1name] = {"kissat": ks, "kissat_lines": kl[:8]}
    if LATCH or cancelled():
        return fail(c1name, "safety/cancellation after solver leg")
    if ks is None:
        return fail(c1name, "refused %r" % rf)
    if not (healthy(ks) and not receipt_contradictions(ks) and ks["returncode"] == 20
            and kl == ["s UNSATISFIABLE"] and sink_complete(ks.get("proof_sink"))):
        return fail(c1name, "solver leg not exactly rc20 ['s UNSATISFIABLE'], unhealthy or sink incomplete")
    before1 = adopt_sink(c1name, proof, ks)
    if before1 is None or LATCH or cancelled():
        return fail(c1name, "solver artifacts changed or sink integrity/safety failed")
    ph, pn = artifacts[proof]
    dr, dl, rf = launch(run_drat, cnf, proof, "C1", CONTROL_CHILD_WALL, per_child,
                        {"cnf_pin": [h, n], "proof_pin": [ph, pn]})
    recs[c1name]["drat"] = dr
    post1 = post_files(c1name)
    if post1 is None or LATCH or cancelled():
        return fail(c1name, "post-check artifact integrity or safety/cancellation failure")
    if dr is None:
        return fail(c1name, "checker refused %r" % rf)
    c1 = qualify_unsat(exp, ks, kl, ph, pn, CONTROL_PROOF_CAP, dr, dl, post1[cnf], post1[proof])
    recs[c1name].update(intended="PASS: qualify_unsat == [] and completed 's VERIFIED'", defects=c1)
    if c1 != [] or not completed_checker(dr, dl, "VERIFIED"):
        return fail(c1name, "positive control did not pass %r" % defect_ids(c1))

    # C2 changes only the CNF's intended bytes; both actual post-check files are freshly rehashed.
    c2name = "C2_mutated_cnf_digest"
    if LATCH or cancelled():
        return fail(c2name, "safety/cancellation prevents the next control")
    lines = raw.split(b"\n")
    first = lines[1].split()
    mutated = b"\n".join([lines[0], b" ".join(first[:-2] + first[-1:])] + lines[2:])
    cnf2 = os.path.join(d, "php6x5-one-literal-removed.cnf")
    h2, n2 = write_bytes_x(cnf2, mutated)
    artifacts[cnf2] = (h2, n2)
    dr2, dl2, rf = launch(run_drat, cnf2, proof, "C2", CONTROL_CHILD_WALL, per_child,
                          {"cnf_pin": [h2, n2], "proof_pin": [ph, pn]})
    recs[c2name] = {"drat": dr2, "checker_status_lines": status_lines(dl2)}
    post2 = post_files(c2name)
    if post2 is None or LATCH or cancelled():
        return fail(c2name, "post-check artifact integrity or safety/cancellation failure")
    if dr2 is None:
        return fail(c2name, "refused %r" % rf)
    c2 = qualify_unsat(exp, ks, kl, ph, pn, CONTROL_PROOF_CAP, dr2, dl2, post2[cnf2], post2[proof])
    recs[c2name].update(intended="completed 's VERIFIED'; defect IDs exactly ['CNF_POST']", defects=c2)
    if not (completed_checker(dr2, dl2, "VERIFIED") and defect_ids(c2) == ["CNF_POST"]):
        return fail(c2name, "defect IDs %r != ['CNF_POST'] or not completed" % defect_ids(c2))

    # C3 also rejects a proof that is not the solver sink's measurement, not merely its parser prefix.
    c3name = "C3_trailing_proof_byte"
    if LATCH or cancelled():
        return fail(c3name, "safety/cancellation prevents the next control")
    pbytes = read_tree(proof, CONTROL_PROOF_CAP)
    proof3 = os.path.join(d, "php6x5-trailing.drat")
    p3h, p3n = write_bytes_x(proof3, pbytes + b"x")
    artifacts[proof3] = (p3h, p3n)
    dr3, dl3, rf = launch(run_drat, cnf, proof3, "C3", CONTROL_CHILD_WALL, per_child,
                          {"cnf_pin": [h, n], "proof_pin": [p3h, p3n]})
    recs[c3name] = {"drat": dr3, "checker_status_lines": status_lines(dl3)}
    post3 = post_files(c3name)
    if post3 is None or LATCH or cancelled():
        return fail(c3name, "post-check artifact integrity or safety/cancellation failure")
    if dr3 is None:
        return fail(c3name, "refused %r" % rf)
    c3 = qualify_unsat(exp, ks, kl, p3h, p3n, CONTROL_PROOF_CAP + 1, dr3, dl3, post3[cnf], post3[proof3])
    want3 = ["A.CONSUMED", "A.FORBIDDEN.WRONG_PREFIX", "PROOF_SINK_BINDING"]
    recs[c3name].update(intended="completed 's VERIFIED'; defect IDs exactly %r" % want3, defects=c3)
    if not (completed_checker(dr3, dl3, "VERIFIED") and defect_ids(c3) == want3):
        return fail(c3name, "defect IDs %r != %r or not completed" % (defect_ids(c3), want3))

    # C4 preserves the measured native NOT VERIFIED outcome; artifact drift is a separate safety failure.
    c4name = "C4_sat_formula_foreign_proof"
    if LATCH or cancelled():
        return fail(c4name, "safety/cancellation prevents the next control")
    raw4 = php_cnf(5, 5)
    cnf4 = os.path.join(d, "php5x5-sat.cnf")
    h4, n4 = write_bytes_x(cnf4, raw4)
    artifacts[cnf4] = (h4, n4)
    exp4 = (h4, n4, raw4.split(b"\n", 1)[0].decode())
    dr4, dl4, rf = launch(run_drat, cnf4, proof, "C4", CONTROL_CHILD_WALL, per_child,
                          {"cnf_pin": [h4, n4], "proof_pin": [ph, pn]})
    recs[c4name] = {"drat": dr4, "checker_status_lines": status_lines(dl4)}
    post4 = post_files(c4name)
    if post4 is None or LATCH or cancelled():
        return fail(c4name, "post-check artifact integrity or safety/cancellation failure")
    if dr4 is None:
        return fail(c4name, "refused %r" % rf)
    c4 = file_checker_defects("A", exp4, pn, dr4, dl4)
    want4 = ["A.EXIT", "A.FORBIDDEN.NOT_VERIFIED", "A.STATUS"]
    recs[c4name].update(intended="completed exactly ['s NOT VERIFIED'] rc1; checker defect IDs exactly %r" % want4,
                        defects=c4)
    if not (completed_checker(dr4, dl4, "NOT VERIFIED") and defect_ids(c4) == want4):
        return fail(c4name, "defect IDs %r != %r or not completed" % (defect_ids(c4), want4))

    # C5 permits only the intended proof-cap trip; capture, ownership and file integrity must remain clean.
    c5name = "C5_proof_hard_cap"
    if LATCH or cancelled():
        return fail(c5name, "safety/cancellation prevents the next control")
    raw5 = php_cnf(11, 10)
    cnf5 = os.path.join(d, "php11x10.cnf")
    h5, n5 = write_bytes_x(cnf5, raw5)
    artifacts[cnf5] = (h5, n5)
    proof5 = os.path.join(d, "php11x10.drat")
    ks5, kl5, rf = launch(run_kissat, cnf5, proof5, "C5", CONTROL_CHILD_WALL, 4096, per_child, {"cnf_pin": [h5, n5]})
    recs[c5name] = {"kissat": ks5, "kissat_lines": kl5[:8]}
    if LATCH or cancelled():
        return fail(c5name, "safety/cancellation after capped solver leg")
    if ks5 is None:
        return fail(c5name, "refused %r" % rf)
    ps5 = ks5.get("proof_sink") or {}
    post5 = adopt_sink(c5name, proof5, ks5)
    if post5 is None or LATCH or cancelled():
        return fail(c5name, "capped sink settlement/file integrity or safety failed")
    size5 = post5[proof5][1]
    recs[c5name].update(intended="only proof_cap; capture clean; exact rehash and settled retained proof inode <=4096 B",
                        proof_file_bytes=size5)
    if not (ks5.get("stop") == "proof_cap" and ks5.get("trips") == ["proof_cap"]
            and ks5.get("capture_over_cap") is False and ks5.get("settled") is True
            and not receipt_contradictions(ks5, allowed_trips=("proof_cap",)) and ks5.get("resource_diagnostics") == []
            and sink_integrity(ps5) and ps5.get("sink_settled") is True and ps5.get("over_cap") is True
            and ps5.get("connected") is True and ps5.get("eof") is True
            and ps5.get("unblocked_by_runner") is False and size5 == ps5.get("written") <= 4096
            and ps5.get("discarded", 0) > 0 and ps5.get("received") == ps5.get("written", 0) + ps5.get("discarded", 0)):
        return fail(c5name, "intended reason alone, exact file integrity, capture cleanliness or settlement missing")

    # C6 retains the exact native timer contract; core timing supplies unrounded monotonic evidence.
    c6name = "C6_native_time_limit"
    if LATCH or cancelled():
        return fail(c6name, "safety/cancellation prevents the next control")
    raw6 = php_cnf(13, 12)
    cnf6 = os.path.join(d, "php13x12.cnf")
    h6, n6 = write_bytes_x(cnf6, raw6)
    artifacts[cnf6] = (h6, n6)
    ks6, kl6, rf = launch(run_kissat, cnf6, None, "C6", CONTROL_TIMER_S, None, per_child, {"cnf_pin": [h6, n6]})
    recs[c6name] = {"kissat": ks6, "kissat_lines": kl6[:8]}
    if LATCH or cancelled():
        return fail(c6name, "safety/cancellation after timer solver leg")
    if ks6 is None:
        return fail(c6name, "refused %r" % rf)
    why6 = c6_timer_refusals(ks6, kl6)
    if receipt_contradictions(ks6):
        why6.append("contradictory or incomplete solver ownership receipt")
    recs[c6name].update(intended="healthy self-exit rc 0, complete output exactly ['s UNKNOWN'], unrounded monotonic "
                                "runtime lower bound >= %.1f s and upper bound <= %.1f s for --time=%d "
                                "(runs 008/010/012 at --time=1: rc 0, 's UNKNOWN')"
                                % (C6_MIN_RUN_S, C6_MAX_RUN_S, CONTROL_TIMER_S), refusals=why6)
    if why6:
        return fail(c6name, "intended timer-expiry outcome missing %r" % (why6,))

    # C7's empty file must be just as settled and inode/hash-bound as an ordinary or capped proof file.
    c7name = "C7_no_input_sink_liveness"
    if LATCH or cancelled():
        return fail(c7name, "safety/cancellation prevents the next control")
    absent = os.path.join(d, "absent.cnf")
    proof7 = os.path.join(d, "absent.drat")
    ks7, kl7, rf = launch(run_kissat, absent, proof7, "C7", 10, CONTROL_PROOF_CAP, per_child, {"cnf_pin": None})
    recs[c7name] = {"kissat": ks7, "kissat_lines": kl7[:8]}
    if LATCH or cancelled():
        return fail(c7name, "safety/cancellation after missing-input solver leg")
    if ks7 is None:
        return fail(c7name, "refused %r" % rf)
    ps7 = ks7.get("proof_sink") or {}
    post7 = adopt_sink(c7name, proof7, ks7)
    if post7 is None or LATCH or cancelled():
        return fail(c7name, "never-connected sink settlement/file integrity or safety failed")
    want7 = ["kissat: error: can not read '%s'" % absent]
    recs[c7name].update(intended="healthy self-exit rc 1, complete output exactly %r (runs 008/010/012); "
                                "runner-unblocked, joined sink and exact empty proof inode/hash" % want7)
    if not (healthy(ks7) and not receipt_contradictions(ks7) and ks7["returncode"] == 1 and kl7 == want7
            and sink_integrity(ps7) and ps7.get("sink_settled") is True
            and ps7.get("unblocked_by_runner") is True and ps7.get("connected") is True and ps7.get("eof") is True
            and ps7.get("over_cap") is False and ps7.get("written") == ps7.get("received") == ps7.get("discarded") == 0
            and post7[proof7] == (ps7.get("sha256_of_written"), 0)):
        return fail(c7name, "intended missing-input outcome or exact empty sink settlement missing")

    # C7b retains drat-trim.c:1425-1427's measured rc255 diagnostic and rehashes every retained artifact afterward.
    c7bname = "C7b_checker_no_input"
    if LATCH or cancelled():
        return fail(c7bname, "safety/cancellation prevents the next control")
    absent2 = os.path.join(d, "absent-checker.cnf")
    dr7, dl7, rf = launch(run_drat, absent2, proof, "C7b", CONTROL_CHILD_WALL, per_child,
                          {"cnf_pin": None, "proof_pin": [ph, pn]})
    recs[c7bname] = {"drat": dr7, "checker_lines": dl7[:8]}
    post7b = post_files(c7bname)
    if post7b is None or LATCH or cancelled():
        return fail(c7bname, "post-check artifact integrity or safety/cancellation failure")
    if dr7 is None:
        return fail(c7bname, "refused %r" % rf)
    want7b = ['c error opening "%s".' % absent2]
    recs[c7bname].update(intended="healthy self-exit rc 255, complete output exactly %r" % want7b)
    if not (healthy(dr7) and not receipt_contradictions(dr7) and dr7["returncode"] == 255 and dl7 == want7b):
        return fail(c7bname, "intended missing-input outcome missing")
    if LATCH or cancelled():
        return fail(c7bname, "safety/cancellation at controls completion")
    return True, recs



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
    end = work_deadline(PUBLICATION_SECONDS, STATE["mono_end"])
    try:
        deadline_check(end, "item publication creation")
    except BaseException as exc:
        latch("item publication not admitted within frozen cutoff: %r" % (exc,))
        raise
    fd = create_excl(path)
    CREATED[path].update(writer_fd=fd, writer_fd_close_confirmed=False)
    chosen = unknown_bytes
    boundary = None
    try:
        try:
            for w in confinement_refusals() + preservation_refusals(exclude=(path,)) + cutoff_refusals():
                latch("commit: " + w)
            boundary = next(ORDER)
            co = STATE["cancel_order"]
            chosen = unsat_bytes if unsat_bytes is not None and not LATCH and (co is None or co > boundary) else unknown_bytes
            write_all(fd, chosen, deadline=end)
            deadline_check(end, "item fsync entry")
            os.fsync(fd)
            deadline_check(end, "item fsync completion")
        finally:
            try:
                os.close(fd)
                CREATED[path]["writer_fd_close_confirmed"] = True
            except BaseException as exc:
                CREATED[path].update(writer_fd_close_confirmed=None, writer_close_error=repr(exc))
                raise
        deadline_check(end, "item close completion")
        os.fsync(tree_path(path)[0])
        deadline_check(end, "item parent fsync completion")
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
    if span + SETTLE + MARGIN > MAX_CHUNK or time.time() + span + SETTLE > min(OWNED_SETTLED_BY, NATIVE_LAUNCH_STOP) \
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
    if time.time() + span + SETTLE > min(OWNED_SETTLED_BY, NATIVE_LAUNCH_STOP) or time.time() > NATIVE_LAUNCH_STOP:
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
                  "disk_accounting": "enforce max(distinct-inode logical payload, st_blocks*512 including directories); APFS extent sharing overcounts conservatively",
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
    """The plan body; every early stop is a plain return with the outcome flags set.  V12: item shape re-checked
    immediately before generation; N8: run-tree files are hashed through the anchored tree."""
    out_dir = STATE["out"]
    if sha_file(DRAT_OLD[0])[0] != DRAT_OLD[1] or sha_file(KISSAT[0])[0] != KISSAT[1]:
        raise RuntimeError("binary pin mismatch")
    if sha_file(DRAT)[0] != DRAT_OLD[1] or os.lstat(DRAT).st_ino == os.lstat(DRAT_OLD[0]).st_ino:
        raise RuntimeError("vendored drat-trim mismatch or shared inode")
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
        why = item_shape_refusals(it)              # V12: again, immediately before generation
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
        Ej = json.loads(read_pinned(*it["list"]))
        if not (Ej["num_placements"] == len(Ej["placements"]) == it["denominator"]):
            raise RuntimeError("list denominator mismatch " + it["id"])
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                   [Ej["placements"][i] for i in range(it["lo"], it["hi"] + 1)])
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
        inputs = {"item": it["id"], "cnf_pin": [it["cnf"][0], it["cnf"][1]], "list_pin": it["list"][1],
                  "skeleton_pin": SKEL[1], "encoder_pin": ENC[1]}
        proof_path = os.path.join(out_dir, label + ".drat")
        ks, kl, refused = run_kissat(cnf_path, proof_path, label, SOLVER_SECONDS, PROOF_CAP,
                                     PROOF_CAP + LOG_CAP + 3 * RECORD_MAX, inputs)
        if ks is None:
            rec.update(reason="solver admission refused", refusal=refused, host_clock_end=clock())
            write_x(rec_path, rec)
            summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "solver admission refused"}
            summary["stopped"] = {"phase": "solver_admission", "item": it["id"], "why": refused}
            outcome["refused"] = True
            return
        rec["solver"] = ks
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
            rec["proof"] = {"sha256": ks["proof_sink"]["sha256_of_written"], "bytes": ks["proof_sink"]["written"]}
        if ks["returncode"] == 20 and ks["stop"] == "self" and ks["settled"] and sink_ok and not LATCH \
                and not cancelled():
            dr, dl, refused = run_drat(cnf_path, proof_path, label, CHECK_SECONDS, LOG_CAP + 3 * RECORD_MAX,
                                       dict(inputs, proof_pin=[rec["proof"]["sha256"], rec["proof"]["bytes"]]))
            if dr is None:
                rec.update(reason="checker admission refused", refusal=refused, host_clock_end=clock())
                write_x(rec_path, rec)
                summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "checker admission refused"}
                summary["stopped"] = {"phase": "checker_admission", "item": it["id"], "why": refused}
                outcome["refused"] = True
                return
            rec["checker"] = dr
            rec["checker_status_lines"] = status_lines(dl)
            rec["checker_parse_lines"] = [s[:200] for s in dl if s.startswith("c parsing")
                                          or s.startswith("c finished parsing")][:4]
            rec["solver_lines"] = kl[:8]
            post_cnf, post_proof = sha_tree(cnf_path), sha_tree(proof_path, limit=PROOF_CAP)
            rec["post_check_hashes"] = {"cnf": list(post_cnf), "proof": list(post_proof)}
            rec["defects"] = qualify_unsat(it["cnf"], ks, kl, rec["proof"]["sha256"], rec["proof"]["bytes"],
                                           PROOF_CAP, dr, dl, post_cnf, post_proof)
            rec["defect_ids"] = defect_ids(rec["defects"])
            rec["host_clock_end"] = clock()
            rec["terminal_gate"] = terminal_gate()
            unsat = None
            if not rec["defects"] and not rec["terminal_gate"] and not LATCH:
                unsat = dict(rec, status="UNSAT", count_for_scientific_coverage=True,
                             commit="UNSAT chosen at an explicit commit boundary with no earlier cancel stamp or latch")
            commit = commit_record(rec_path, dict(rec, commit="UNKNOWN record"), unsat)
            rec["status"] = "UNSAT_PROVISIONAL" if commit["committed_unsat"] else "UNKNOWN"
            summary.setdefault("commits", {})[it["id"]] = commit
        else:
            rec["reason"] = "no settled self-exit rc20 verdict with a complete proof sink (or latch/cancel)"
            rec["host_clock_end"] = clock()
            write_x(rec_path, rec)
        summary["items"][it["id"]] = {k: rec.get(k) for k in ("status", "defect_ids", "terminal_gate", "reason", "proof")}
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
        all_settled = (all(not receipt_resource_contradictions(r) for r in children)
                       and not any(getattr(c, "launch_state", None) == "popen_exception_unproven" for c in OWNED))
        helpers_settled = (all(h.settled is True for h in HELPERS if h.proc is not None)
                           and not any(getattr(h, "launch_state", None) == "popen_exception_unproven" for h in HELPERS))
        if not all_settled or not helpers_settled:
            defects.append("owned settlement unproven")
        if host_end is None and not cancelled() and not LATCH:
            defects.append("required closeout host clock unavailable")
        try:
            defects += confinement_refusals() + preservation_refusals()
            tree_usage = disk_usage(out_dir)
            tree_bytes = tree_usage["enforced_max_bytes"]
            if type(tree_bytes) is not int or tree_bytes < 0:
                raise RuntimeError("retained output usage is not an exact nonnegative integer")
            if tree_bytes > STATE["reservation"]:
                defects.append("retained output max(logical, allocated) exceeds full reservation")
            led_why, ledger = ledger_refusals()
            defects += led_why
        except BaseException as exc:
            tree_usage, tree_bytes, ledger = None, None, None
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
                       reservation_retained=True, parent_block=bool(unresolved or defects or LATCH or ledger is None),
                       release_requires="NEW parent disposition after runner exit, complete liveness/resource/publication audit",
                       proof_ram_accounting_valid=type(outstanding) is int, proof_ram_outstanding_bytes=outstanding,
                       quarantine_receipts=[c.quarantine_path for c in list(OWNED) + list(HELPERS) if c.quarantined],
                       latch=list(LATCH), cancel_order=co, closeout_boundary=boundary,
                       cancel_before_closeout=co is not None and co < boundary,
                       candidate_observed=bool(outcome.get("sat")), run_tree_usage_before_summary=tree_usage,
                       run_tree_enforced_bytes_before_summary=tree_bytes,
                       lane_ledger_before_summary=ledger, closeout_defects=defects,
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
                    "parent_block": bool(unresolved or defects or LATCH or final_ledger is None), "unresolved": unresolved,
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
