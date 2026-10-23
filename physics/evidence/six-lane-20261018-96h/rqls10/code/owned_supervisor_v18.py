#!/usr/bin/env python3
"""owned_supervisor_v18: narrow cancel-timing/recovery-runtime successor; v17 acquisition-first core retained.

BINDING correction: RUN/review/rqls10-supervisor-v10-scope-parent-correction-v1.json
fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2. V10's scope weakening is withdrawn,
not launch authority. Every earlier file stays immutable/unexecuted.

CLOCK: /bin/date is the sole metadata helper. *_date is its real output or null, never Python-formatted/invented.
mono_*/epoch_* are labelled raw telemetry. Helper budget starts BEFORE spawn, checks completion lateness even on
successful reap, and on exceptions/overrun performs at most one full-identity-checked group SIGTERM plus bounded grace.
Leader reaping is not settlement: initial full identity, known wait status, complete group/descendant closure and
stdout EOF/close must ALL be proved. Otherwise helper ownership stays unresolved and outcome UNSETTLED, including
before a scientific child exists. Final polling repeats the whole proof; it never discharges ownership on reap alone.
No new helper after a failure/cancel. Reviewed injection controls are explicitly labelled; none invents a date string.

OWNERSHIP: before ANY helper/child, obtain a complete identity-only baseline. Retain every known child/helper/group/
observed current-parent identity. Every later identity not in that baseline and not already owned is UNPROVED,
regardless of UID, cwd or argv, and blocks clearance while alive. No exemption for ordinary launchd activity,
unlinked processes or foreign/mixed UIDs is assumed. This deliberately sacrifices availability instead of guessing
ancestry. Incomplete metadata is failed coverage, not proven absence. Source-reviewed nonforking science children
remain the intended interface; separately authorized ownership-negative controls may fork. Known ownership and
unproved identities are retained in receipts and must be independently verified ended by the parent before release.
This is sampled evidence, not an OS sandbox or universal native-call latency guarantee.

IDENTITY: every ownership/resource measurement is bracketed by pid, uniqueid, idversion, euid, ruid, ppid, pgid and
trace metadata. Same uid means real OR effective uid matches. Unreadable same-real/different-effective-uid metadata
fails closed; no login exception. XNU changes idversion on exec. Current-parent edges are bracketed, no puniqueid
birth inference. BUSY/RSS enforcement occurs on EVERY census retry, including incomplete retries; admission/GO use
reserved-slot/headroom predicates, running/final phases use trip predicates. Observed excess never disappears on retry.

SPAWN/COMMIT: os.posix_spawn supplies an EMPTY child signal mask and a fresh session, while cancellation is masked in
the main thread around actual spawn and immediate registration. Sink threads inherit blocked cancellation signals.
At helper launch, child launch, GO and ACK commits check the latch AND sigpending, then fresh clocks/expiry/fit after
I/O. Post-commit cancellation becomes an owned stop. Only /bin/date helpers and the ONE admitted child are spawned by
the supervisor. Inherited cwd must equal the admitted lane; argv paths are absolute. No global cwd change/preexec hook.

STOP/CLEAR: one identity-checked main-child-group SIGTERM, no SIGKILL/escalation/tool timeout/ulimit/deletion. A separate
once-only stop is owned by each helper. Grace begins at first stop and at observed main-child reap. Clearance time is
read only AFTER main reap, closed clean streams, ended sink threads, all helpers settled and a fresh complete census
with no owned OR unproved live identities have all been verified. Compare that fresh time with every cutoff; never
backdate using a census timestamp or restore an expired result during finalization.

DISK/PUBLICATION: retain root fd/device/inode, no-follow anchored output/TMPDIR walks, reject changed/mounted/retyped/
vanished charged subtrees. Charge distinct-inode logical bytes of ALL output-root files (launch/samples/sinks/
declared/stray) and TMPDIR. Own unused and all parent outstanding reservations remain held through ACK. Final receipt
and settlement buffers are serialized ONCE and exactly those bytes budgeted/written. Insufficient/unavailable budget
REFUSES publication. Exclusive create, complete writes, fsync/close/readback, same-inode staged link and every output
directory fsync precede post_publish_mono. I/O deadlines check every completion path; late native return fails closed.
Fresh resource/freshness/fit checks precede protected ACK. Parent must join actual exit, captured summary and both
digests, complete ended-owned/unproved evidence and late-artifact audit in its NEW exclusive release disposition.
No standalone receipt, shell return code, summary or checker PASS releases a reservation or claims science success.

Exit:0 acknowledged SETTLED;10 acknowledged NOT_LAUNCHED;11 acknowledged UNSETTLED;12 publication refused/receipt
failed;13 settlement/sync/finalization failed;14 ACK refused/overran;2 unusable config/anchors. NOEXEC until separately
accepted source/package and an exact item GO. Usage: owned_supervisor_v18.py CONFIG.json
V12 preserves v11 helper/clearance/identity/root machinery and fabe57ab. Repairs all nine v11 review findings plus
three package integration blockers: enforce main runtime before/after every reap (late observation cannot erase it),
restore bounded spawn-to-GO age, fresh ACK census, actual conservative /bin/date stability age, authorization last
after preparation I/O, post-write pending-cancel/expiry checks, aggregate OUTPUT including exact publication bytes,
retained unproved/coverage/resource-observation history, original fsynced staged inode through link, proved injected
overrun, nonempty fast-exit samples, complete retry extrema provenance, and no end-helper attempt without authority.
History caps fail closed, never silently discard evidence. Every commit checks stability age against the configured
maximum; a run outliving its frozen stability window may refuse ACK rather than weakening that policy.
V13 additionally checks ACTUAL completed GO delivery age/runtime and enters owned stop on lateness; a first-date
monotonic stability expiry can only tighten, never renew after civil-clock rollback; completed identity/resource and
abort evidence is retained incrementally, with current capped reconciliation evidence emitted on post-publication
refusal. The v12 review's finite empirical matrix remains REQUIRED and UNEXERCISED; the existing22 controls do not
claim to cover that matrix. Rebound qualification is deferred pending the separate package review.
"""
import contextlib
import ctypes
import errno
import datetime
import hashlib
import json
import math
import os
import signal
import stat
import struct
import sys
import threading
import time

VERSION = "owned_supervisor_v18"
CANCEL_SIGNALS = {signal.SIGTERM, signal.SIGINT, signal.SIGHUP}
CANCEL = {"signal": None, "mono": None}
CANCEL_FAILURE_TARGET = None
POLICY = {"disk": 10737418240, "free": 12000000000, "launch_free": 12200000000,
          "rss": 51539607552, "busy": 2, "chunk": 10800}
SMALL = 1 << 20
PIN_CAP = 64 << 20
PUBLICATION_CAP = 4 << 20
IO_S = 30.0
CENSUS_S = 10.0
FINALIZE_S = 120.0
WALK_ENTRIES = 500000
ROOT_ENTRIES = 4096
CONFIG = {"item": str, "owner": str, "purpose": str, "lane": str, "argv": list, "env": dict,
          "stdout": str, "stderr": str, "stdout_cap_bytes": int, "stderr_cap_bytes": int,
          "samples": str, "samples_cap_bytes": int, "launch_record": str, "receipt": str,
          "settlement_record": str, "outputs": list, "output_roots": list, "pins": list,
          "max_wall_s": float, "settle_s": float, "sample_s": float, "max_chunk_seconds": float,
          "owned_compute_settled_by_epoch": float, "rss_trip_bytes": int, "rss_projection_bytes": int,
          "free_trip_bytes": int, "launch_free_min_bytes": int, "output_trip_bytes": int,
          "lane_roots": list, "lane_disk_root": str, "lane_disk_ceiling_bytes": int,
          "lane_walk_s": float, "busy_limit": int, "busy_cpu_fraction": float, "cpu_slots": int,
          "admission": dict, "helper_budget": dict, "fault_injection": dict, "creation_channel": dict}
HELPER = {"max_calls": int, "call_budget_s": float, "term_grace_s": float}
HELPER_FAULTS = {"date_helper_fails", "helper_observation_overrun", "helper_group_unproved", "helper_eof_unproved"}
ADMISSION = {"go_path": str, "stability_receipt_path": str, "reservation_bytes": int,
             "outstanding_reservations_bytes": int, "lane_outstanding_reservations_bytes": int,
             "stability_max_age_s": float}
BOUND_KEYS = ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel", "reservation_bytes",
              "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")
MY_PID, MY_UID = os.getpid(), os.getuid()
SELF = os.path.abspath(__file__)


class GuardError(OSError):
    pass


def cancel(signum, frame):
    if CANCEL["signal"] is None:
        CANCEL["signal"] = signum
        try:
            CANCEL["mono"] = time.monotonic()
        except BaseException as e:
            CANCEL["mono"] = None
            CANCEL["clock_error"] = type(e).__name__
            if CANCEL_FAILURE_TARGET is not None:
                CANCEL_FAILURE_TARGET.timing_failed = True  # Handler does no re-entrant failure-list mutation.


@contextlib.contextmanager
def protected():
    old = signal.pthread_sigmask(signal.SIG_BLOCK, CANCEL_SIGNALS)
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)


def pending_cancel():
    return CANCEL["signal"] is not None or bool(set(signal.sigpending()) & CANCEL_SIGNALS)


class Deadline:
    def __init__(self, seconds, until=None):
        self.mono_created, self.seconds, self.until = time.monotonic(), seconds, until
        self.end = self.mono_created + seconds
        if until is not None:
            self.end = min(self.end, until)

    def telemetry(self):
        return {"mono_created": self.mono_created, "seconds": self.seconds, "until": self.until, "end": self.end}

    def check(self, operation):
        try:
            now = time.monotonic()
        except BaseException as e:
            raise GuardError("CLOCK_UNAVAILABLE " + operation) from e
        if now > self.end:
            raise GuardError("DEADLINE_EXCEEDED " + operation)


# macOS proc_info ABI (SDK and pinned XNU copies in lane tmp/).
LP = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
LP.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LP.proc_pidinfo.restype = ctypes.c_int
LP.proc_listallpids.argtypes = (ctypes.c_void_p, ctypes.c_int)
LP.proc_listallpids.restype = ctypes.c_int
LC = ctypes.CDLL("/usr/lib/libSystem.B.dylib", use_errno=True)
LC.sysctl.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_void_p,
                      ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p, ctypes.c_size_t)
LC.sysctl.restype = ctypes.c_int
LC.mach_timebase_info.argtypes = (ctypes.c_void_p,)
LC.mach_timebase_info.restype = ctypes.c_int
SZOMB = 5


class Timebase(ctypes.Structure):
    _fields_ = [("numer", ctypes.c_uint32), ("denom", ctypes.c_uint32)]


def timebase():
    tb = Timebase()
    if LC.mach_timebase_info(ctypes.byref(tb)) or not tb.denom:
        raise GuardError("MACH_TIMEBASE_UNREADABLE")
    return tb.numer / tb.denom


def argmax():
    mib, val = (ctypes.c_int * 2)(1, 8), ctypes.c_int()
    n = ctypes.c_size_t(ctypes.sizeof(val))
    if LC.sysctl(mib, 2, ctypes.byref(val), ctypes.byref(n), None, 0) or not (0 < val.value <= 16 << 20):
        raise GuardError("ARGMAX_UNREADABLE")
    return val.value


def pidinfo(pid, flavor, size, zombies=False):
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    got = LP.proc_pidinfo(pid, flavor, 1 if zombies else 0, buf, size)
    if got != size:
        raise GuardError(ctypes.get_errno() or errno.EIO, "PIDINFO %d flavor %d bytes %d" % (pid, flavor, got))
    return buf.raw


def unique(pid):
    raw = pidinfo(pid, 17, 56, True)
    return struct.unpack_from("=Q", raw, 16)[0], struct.unpack_from("=i", raw, 32)[0]


def short(pid):
    raw = pidinfo(pid, 13, 64, True)
    p, pp, pg, st = struct.unpack_from("=IIII", raw)
    flags, uid = struct.unpack_from("=II", raw, 32)
    return {"pid": p, "ppid": pp, "pgid": pg, "status": st, "euid": uid,
            "ruid": struct.unpack_from("=I", raw, 44)[0], "traced": bool(flags & 2),
            "comm": raw[16:32].split(b"\0")[0].decode("utf-8", "replace")}


def fingerprint(p):
    return tuple(p[k] for k in ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced"))


def identity_form(p):
    """Full acquired identity metadata except the separately recorded native status."""
    return tuple(p[k] for k in ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced", "comm"))


def identify(pid):
    a, s1, b, s2, c = unique(pid), short(pid), unique(pid), short(pid), unique(pid)
    if not (a == b == c):
        raise GuardError("IDENTITY_CHANGED %d" % pid)
    for s in (s1, s2):
        s.update(uniqueid=a[0], idversion=a[1])
    if fingerprint(s1) != fingerprint(s2):
        raise GuardError("IDENTITY_METADATA_CHANGED %d" % pid)
    return s2




def cwd_of(pid):
    field = pidinfo(pid, 9, 2352)[152:1176]
    end = field.find(b"\0")
    if end <= 0:
        raise GuardError("CWD_MALFORMED %d" % pid)
    return field[:end].decode("utf-8", "surrogateescape")


def argv_of(pid, maximum):
    mib = (ctypes.c_int * 3)(1, 49, pid)
    buf, size = ctypes.create_string_buffer(maximum), ctypes.c_size_t(maximum)
    ctypes.set_errno(0)
    if LC.sysctl(mib, 3, buf, ctypes.byref(size), None, 0):
        raise GuardError(ctypes.get_errno() or errno.EIO, "ARGV %d" % pid)
    raw = ctypes.string_at(buf, size.value)
    if len(raw) < 5:
        raise GuardError("ARGV_SHORT %d" % pid)
    argc = struct.unpack_from("=i", raw)[0]
    end = raw.find(b"\0", 4)
    if not (0 <= argc <= maximum) or end < 0:
        raise GuardError("ARGV_MALFORMED %d" % pid)
    out, pos = [raw[4:end].decode("utf-8", "surrogateescape")], end
    while pos < len(raw) and raw[pos] == 0:
        pos += 1
    for _ in range(argc):
        end = raw.find(b"\0", pos)
        if end < 0:
            raise GuardError("ARGV_UNTERMINATED %d" % pid)
        out.append(raw[pos:end].decode("utf-8", "surrogateescape"))
        pos = end + 1
    return out


def task_of(pid):
    raw = pidinfo(pid, 4, 96)
    rss = struct.unpack_from("=Q", raw, 8)[0]
    u, s = struct.unpack_from("=QQ", raw, 16)
    return rss, u + s


def start_of(pid):
    s, us = struct.unpack_from("=QQ", pidinfo(pid, 3, 136, True), 120)
    return s + us / 1e6


def all_pids(dl):
    dl.check("before pid list")
    count = LP.proc_listallpids(None, 0)
    if count <= 0:
        raise GuardError("PID_LIST_FAILED")
    cap = count * 2 + 1024
    for _ in range(4):
        buf = (ctypes.c_int * cap)()
        n = LP.proc_listallpids(buf, ctypes.sizeof(buf))
        dl.check("after pid list")
        if n <= 0:
            raise GuardError("PID_LIST_FAILED")
        if n < cap:
            vals = list(buf[:n])
            if any(p < 0 for p in vals) or len(set(vals)) != len(vals):
                raise GuardError("PID_LIST_MALFORMED")
            return [p for p in vals if p > 0]
        cap *= 2
    raise GuardError("PID_LIST_OVERFLOW")


# Bounded regular-file and descriptor-anchored directory operations.
def read_file(path, cap, dl, dir_fd=None, keep=False):
    dl.check("before file open")
    st = os.stat(path, dir_fd=dir_fd, follow_symlinks=False)
    if not stat.S_ISREG(st.st_mode) or not 0 <= st.st_size <= cap:
        raise GuardError("NOT_BOUNDED_REGULAR %s" % path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dir_fd)
    parts, h, got = [], hashlib.sha256(), 0
    try:
        fs = os.fstat(fd)
        if (fs.st_dev, fs.st_ino, fs.st_size) != (st.st_dev, st.st_ino, st.st_size):
            raise GuardError("FILE_CHANGED_OPEN %s" % path)
        while got < st.st_size:
            dl.check("file read")
            b = os.read(fd, min(1 << 20, st.st_size - got))
            if not b:
                raise GuardError("FILE_SHORT %s" % path)
            h.update(b)
            got += len(b)
            if keep:
                parts.append(b)
        tail = os.read(fd, 1)
        end = os.fstat(fd)
        if tail or (end.st_size, end.st_mtime_ns) != (st.st_size, st.st_mtime_ns):
            raise GuardError("FILE_CHANGED_READ %s" % path)
    finally:
        os.close(fd)
    dl.check("after file close")
    return {"sha256": h.hexdigest(), "bytes": got, "inode": [st.st_dev, st.st_ino], "nlink": st.st_nlink,
            "birth_epoch": st.st_birthtime}, b"".join(parts) if keep else None


def write_all(fd, data, dl, on_progress=None):
    view = memoryview(data)
    while view:
        dl.check("before write")
        n = os.write(fd, view)
        if n <= 0:
            raise GuardError("ZERO_PROGRESS_WRITE")
        if on_progress is not None:
            on_progress(view[:n])  # Native progress is captured before the next deadline/clock check.
        view = view[n:]
    dl.check("after write")


def bytes_json(obj):
    return (json.dumps(obj, sort_keys=True, indent=1, allow_nan=False) + "\n").encode()


def pairs(kv):
    out = {}
    for k, v in kv:
        if k in out:
            raise ValueError("duplicate JSON key %r" % k)
        out[k] = v
    return out


def json_float(s):
    x = float(s)
    if not math.isfinite(x):
        raise ValueError("nonfinite JSON number")
    return x


def json_constant(s):
    raise ValueError("nonfinite JSON constant %s" % s)


def parse_json(raw):
    return json.loads(raw.decode(), object_pairs_hook=pairs, parse_float=json_float, parse_constant=json_constant)


def parse_date_epoch(text):
    if not isinstance(text, str):
        raise GuardError("STABILITY_TIMESTAMP_MISSING")
    parsed = datetime.datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
    if parsed.strftime("%Y-%m-%dT%H:%M:%S%z") != text:
        raise GuardError("STABILITY_TIMESTAMP_NONCANONICAL")
    return parsed.timestamp()


def norm_abs(p):
    return isinstance(p, str) and p.startswith("/") and os.path.abspath(p) == p


def below(p, root):
    return p == root or p.startswith(root.rstrip("/") + "/")


def directory_at(fd, rel, dl):
    """new directory open descriptions, no symlink components, relative to the retained anchor."""
    dl.check("before directory traversal")
    cur = os.open(".", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
    try:
        for component in rel.split("/"):
            if component in ("", "."):
                continue
            if component == "..":
                raise GuardError("PARENT_DIRECTORY_REFUSED")
            nxt = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=cur)
            os.close(cur)
            cur = nxt
            dl.check("directory traversal")
        dl.check("after directory traversal")
    except BaseException:
        os.close(cur)
        raise
    return cur


def absolute_directory(path, dl):
    root = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        fd = directory_at(root, path.lstrip("/"), dl)
    finally:
        os.close(root)
    dl.check("after absolute directory open")
    return fd


def stat_id(fd):
    s = os.fstat(fd)
    return s.st_dev, s.st_ino


def list_directory(fd, dl):
    names = []
    with os.scandir(fd) as it:
        for e in it:
            if len(names) >= ROOT_ENTRIES:
                raise GuardError("ROOT_ENTRY_CAP")
            names.append(e.name)
            dl.check("directory inventory")
    names.sort()
    dl.check("after directory inventory sort")
    return names


def walk_fd(anchor, dev, dl, seen=None):
    """distinct-inode logical bytes; disappeared/retyped entries are incomplete accounting, never zero."""
    seen = set() if seen is None else seen
    count = [0]

    def descend(fd, depth):
        if depth > 64:
            raise GuardError("WALK_DEPTH_CAP")
        total, dirs = 0, []
        with os.scandir(fd) as it:
            for e in it:
                dl.check("walk entry")
                count[0] += 1
                if count[0] > WALK_ENTRIES:
                    raise GuardError("WALK_ENTRY_CAP")
                s = os.stat(e.name, dir_fd=fd, follow_symlinks=False)
                if s.st_dev != dev:
                    raise GuardError("WALK_MOUNT_BOUNDARY %s" % e.name)
                if stat.S_ISDIR(s.st_mode):
                    dirs.append((e.name, s.st_ino))
                elif stat.S_ISREG(s.st_mode):
                    key = (s.st_dev, s.st_ino)
                    if key not in seen:
                        seen.add(key)
                        total += s.st_size
        for name, ino in dirs:
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            try:
                if stat_id(child) != (dev, ino):
                    raise GuardError("WALK_DIRECTORY_REPLACED %s" % name)
                total += descend(child, depth + 1)
            finally:
                os.close(child)
            dl.check("after walk child close")
        dl.check("after walk directory")
        return total
    fd = os.open(".", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=anchor)
    try:
        total = descend(fd, 0)
    finally:
        os.close(fd)
    dl.check("after walk root close")
    return total


def create_file(fd, name):
    out = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=fd)
    return out, stat_id(out)


def publish(fd, name, data, dl):
    out, ident = create_file(fd, name)
    try:
        write_all(out, data, dl)
        os.fsync(out)
        dl.check("after publication fsync")
    finally:
        os.close(out)
    dl.check("after publication close")
    a, _ = read_file(name, len(data), dl, fd)
    if a["sha256"] != hashlib.sha256(data).hexdigest() or tuple(a["inode"]) != ident:
        raise GuardError("PUBLICATION_READBACK_MISMATCH")
    return a["sha256"], ident


def linked_publication(fd, name, data, dl):
    h, published_inode = publish(fd, name + ".staged", data, dl)
    os.link(name + ".staged", name, src_dir_fd=fd, dst_dir_fd=fd)
    dl.check("after settlement link")
    a, _ = read_file(name, len(data), dl, fd)
    s = os.stat(name + ".staged", dir_fd=fd, follow_symlinks=False)
    if a["sha256"] != h or tuple(a["inode"]) != published_inode or (s.st_dev, s.st_ino) != published_inode or a["nlink"] != 2:
        raise GuardError("SETTLEMENT_LINK_MISMATCH")
    dl.check("after settlement link readback")
    return h


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def integer(x):
    return isinstance(x, int) and not isinstance(x, bool)


def hex64(x):
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def typed_equal(left, right):
    """Exact JSON structure and scalar types; bool never aliases an integer authority field."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(typed_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def validate(cfg):
    def schema(obj, spec):
        if not isinstance(obj, dict) or set(obj) != set(spec):
            raise ValueError("missing/extra config keys")
        for k, t in spec.items():
            ok = number(obj[k]) if t is float else integer(obj[k]) if t is int else isinstance(obj[k], t)
            if not ok:
                raise ValueError("invalid config type: " + k)
    schema(cfg, CONFIG)
    schema(cfg["admission"], ADMISSION)
    schema(cfg["helper_budget"], HELPER)
    hb = cfg["helper_budget"]
    if not (1 <= hb["max_calls"] <= 32 and 0.001 <= hb["call_budget_s"] <= 10 and 0.01 <= hb["term_grace_s"] <= 10):
        raise ValueError("helper budget policy")
    if not 0.01 <= cfg["admission"]["stability_max_age_s"] <= 300:
        raise ValueError("stability freshness policy")
    limits = {"max_chunk_seconds": (1, POLICY["chunk"]), "max_wall_s": (0.01, cfg["max_chunk_seconds"]),
              "settle_s": (0.01, 600), "sample_s": (0.2, 10), "lane_walk_s": (1, 600),
              "owned_compute_settled_by_epoch": (1, 4e9), "rss_trip_bytes": (1, POLICY["rss"]),
              "rss_projection_bytes": (0, cfg["rss_trip_bytes"]), "free_trip_bytes": (POLICY["free"], 1 << 60),
              "launch_free_min_bytes": (POLICY["launch_free"], 1 << 60),
              "output_trip_bytes": (1, POLICY["disk"]), "lane_disk_ceiling_bytes": (1, POLICY["disk"]),
              "cpu_slots": (1, 2), "busy_limit": (0 if cfg["purpose"] == "guard-qualification" else 1, 2),
              "busy_cpu_fraction": (0.001, 1), "stdout_cap_bytes": (1, 1 << 30),
              "stderr_cap_bytes": (1, 1 << 30), "samples_cap_bytes": (1, 1 << 30)}
    for k, (lo, hi) in limits.items():
        if not lo <= cfg[k] <= hi:
            raise ValueError("policy range: " + k)
    a = cfg["admission"]
    for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"):
        if not 0 <= a[k] <= 1 << 60:
            raise ValueError("negative/large reservation: " + k)
    if a["reservation_bytes"] > POLICY["disk"]:
        raise ValueError("reservation over lane cap")
    cap = cfg["output_trip_bytes"] + cfg["stdout_cap_bytes"] + cfg["stderr_cap_bytes"] + cfg["samples_cap_bytes"] + PUBLICATION_CAP
    if a["reservation_bytes"] < cap:
        raise ValueError("reservation below caps + publication allowance")
    if set(cfg["fault_injection"]) - ({"identity_check_fails"} | HELPER_FAULTS) or any(not isinstance(x, bool) for x in cfg["fault_injection"].values()):
        raise ValueError("invalid fault injection")
    if any(cfg["fault_injection"].values()) and cfg["purpose"] != "guard-qualification":
        raise ValueError("fault outside qualification")
    if not cfg["argv"] or not all(isinstance(x, str) for x in cfg["argv"]) or not norm_abs(cfg["argv"][0]):
        raise ValueError("argv invalid")
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in cfg["env"].items()) or not norm_abs(cfg["env"].get("TMPDIR")):
        raise ValueError("env/TMPDIR invalid")
    for k in ("lane", "lane_disk_root"):
        if not norm_abs(cfg[k]):
            raise ValueError("not normalized absolute: " + k)
    for k in ("lane_roots", "output_roots"):
        if not cfg[k] or not all(norm_abs(p) for p in cfg[k]) or len(set(cfg[k])) != len(cfg[k]):
            raise ValueError("invalid roots: " + k)
    if any(r == cfg["lane_disk_root"] or not below(r, cfg["lane_disk_root"]) for r in cfg["output_roots"]):
        raise ValueError("output root outside lane-disk root")
    if any(r != q and below(r, q) for r in cfg["output_roots"] for q in cfg["output_roots"]):
        raise ValueError("nested output roots")
    if not below(cfg["env"]["TMPDIR"], cfg["lane_disk_root"]) or any(below(cfg["env"]["TMPDIR"], r) for r in cfg["output_roots"]):
        raise ValueError("TMPDIR outside charge or inside output root")
    for o in cfg["outputs"]:
        if not isinstance(o, dict) or set(o) != {"path", "required"} or not norm_abs(o["path"]) or type(o["required"]) is not bool:
            raise ValueError("invalid output")
    for p in cfg["pins"]:
        if not isinstance(p, dict) or set(p) != {"path", "sha256"} or not norm_abs(p["path"]) or not hex64(p["sha256"]):
            raise ValueError("invalid pin")
    paths = [cfg[k] for k in ("stdout", "stderr", "samples", "launch_record", "receipt", "settlement_record")] + [o["path"] for o in cfg["outputs"]]
    if len(paths) != len(set(paths)) or any(not norm_abs(p) or os.path.dirname(p) not in cfg["output_roots"] or p.endswith(".staged") for p in paths):
        raise ValueError("invalid/distinct output paths")
    for p in (a["go_path"], a["stability_receipt_path"]):
        if not norm_abs(p) or any(below(p, r) for r in cfg["output_roots"]):
            raise ValueError("invalid authorization path")
    channel = cfg["creation_channel"]
    if channel:
        keys = {"kind", "scenario", "preparation_path", "preparation_sha256", "target_path"}
        if cfg["purpose"] != "guard-qualification" or set(channel) != keys or \
                channel["kind"] != "qualification-creation-v1" or channel["scenario"] not in ("mutate_pin", "mutate_evidence") or \
                len(cfg["output_roots"]) != 1 or not hex64(channel["preparation_sha256"]):
            raise ValueError("creation channel is restricted to declared mutation qualification negatives")
        run = os.path.dirname(cfg["output_roots"][0])
        expected_target = run + "/pinned-scratch.txt" if channel["scenario"] == "mutate_pin" else cfg["launch_record"]
        if channel["target_path"] != expected_target or channel["preparation_path"] != run + "/preparation.json":
            raise ValueError("creation channel target/preparation is not the fixed current-run fixture")


def spawn_registered(s, argv, env, role, dl, required_s):
    """Spawn with an explicitly empty signal mask while cancellation is protected in the parent.
    Registration is the FIRST operation after posix_spawn returns a PID; no Popen finalizer or second reaper exists.
    Returned pipe descriptors remain owned even when post-spawn close/deadline work fails."""
    allocated = []
    record = {"pid": None, "role": role, "identity": None, "leader_reaped": False, "rc": None,
              "wait_lost": False, "term_attempted": False, "settled": False, "stdout_fd": None,
              "stderr_fd": None, "stdin_fd": None, "spawn_error": None, "parent_close_fds": []}
    s.keep.append(record)  # Retain the allocation/pipe ledger even before a PID exists.
    if role == "helper":
        s.helpers.append(record)
    try:
        out_read, out_write = os.pipe()
        allocated.extend((out_read, out_write))
        if role == "helper":
            null = os.open("/dev/null", os.O_RDWR)
            allocated.append(null)
            in_read, err_write = null, null
            close_parent = {null, out_write}
        else:
            in_read, in_write = os.pipe()
            err_read, err_write = os.pipe()
            allocated.extend((in_read, in_write, err_read, err_write))
            record["stdin_fd"], record["stderr_fd"] = in_write, err_read
            close_parent = {in_read, out_write, err_write}
        record["parent_close_fds"] = list(close_parent)
        record["stdout_fd"] = out_read
        if any(fd < 3 for fd in allocated):
            raise GuardError("STANDARD_DESCRIPTORS_MUST_BE_OPEN")
        actions = [(os.POSIX_SPAWN_DUP2, in_read, 0), (os.POSIX_SPAWN_DUP2, out_write, 1),
                   (os.POSIX_SPAWN_DUP2, err_write, 2)]
        actions += [(os.POSIX_SPAWN_CLOSE, fd) for fd in allocated]
        with protected():
            dl.check("before protected spawn")
            if role == "helper" and (s.failures or s.in_helper is False):
                raise GuardError("HELPER_LAUNCH_REFUSED")
            s.authorization_io(dl)  # LAST preparation I/O before the protected fresh-clock spawn commit.
            dl.check("after protected spawn authorization")
            record["launch_commit"] = s.time_commit("HELPER" if role == "helper" else "LAUNCH", required_s)
            record["mono_spawn"], record["epoch_spawn"] = time.monotonic(), time.time()
            if role != "helper":
                s.mono_spawn, s.epoch_spawn = record["mono_spawn"], record["epoch_spawn"]
                s.rec.update(mono_spawn=s.mono_spawn, epoch_spawn=s.epoch_spawn,
                             mono_child_deadline=s.mono_spawn + s.cfg["max_wall_s"])
            pid = os.posix_spawn(argv[0], argv, env, file_actions=actions, setsid=True, setsigmask=(),
                                 setsigdef=tuple(CANCEL_SIGNALS | {signal.SIGPIPE, signal.SIGCHLD}))
            record["pid"] = pid
            if role == "helper":
                s.helper_calls += 1
            if role != "helper":
                s.child, s.pid = record, pid
            s.aux_clock(record, "mono_pid_registered")
        try:
            for fd in close_parent:
                os.close(fd)
                allocated.remove(fd)
                record["parent_close_fds"].remove(fd)
            dl.check("after spawn/parent pipe closes")
        except BaseException as e:
            record["spawn_error"] = repr(e)
        return record
    except BaseException:
        if record["pid"] is None:
            record["settled"] = True  # No process was created; no leader/descendant can be abandoned.
            for fd in allocated:
                try:
                    os.close(fd)
                except OSError:
                    pass
        raise


class Supervisor:
    def __init__(self, cfg, path, digest):
        global CANCEL_FAILURE_TARGET
        self.cfg, self.config_path, self.config_sha = cfg, path, digest
        self.num_tb, self.arg_max = timebase(), argmax()
        self.self_sha = read_file(SELF, PIN_CAP, Deadline(IO_S))[0]["sha256"]
        self.start_epoch, self.start_mono = time.time(), time.monotonic()
        self.fit_epoch = min(self.start_epoch + cfg["max_chunk_seconds"] - 120, cfg["owned_compute_settled_by_epoch"] - 180)
        self.fit_mono = self.start_mono + self.fit_epoch - self.start_epoch
        initial_fit = {"start_epoch": self.start_epoch, "start_mono": self.start_mono,
                       "chunk_epoch_bound": self.start_epoch + cfg["max_chunk_seconds"] - 120,
                       "owned_epoch_bound": cfg["owned_compute_settled_by_epoch"] - 180,
                       "fit_epoch": self.fit_epoch, "fit_mono": self.fit_mono}
        self.rec = {"supervisor": VERSION, "supervisor_sha256": self.self_sha, "config_sha256": digest,
                    "config_path": path, "supervisor_pid": MY_PID, "uid": MY_UID,
                    "clock_note": "*_date: owned /bin/date output or null, never invented; mono_* and epoch_*: raw telemetry",
                    "parent_correction_sha256": "fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2",
                    "ownership_residual": "all post-baseline unproved identities block; sampled coverage is not an OS sandbox"}
        self.rec["initial_fit"] = initial_fit
        self.failures, self.failure_keys, self.trips = [], set(), {}
        self.child, self.keep = None, []
        self.pid, self.ident, self.rc = None, None, None
        self.lost_wait, self.exit_mono, self.exit_epoch = False, None, None
        self.mono_spawn, self.epoch_spawn, self.group = None, None, None
        self.stop, self.signal, self.clear = None, None, None
        self.cancel_handled = False
        self.owned, self.violations = {}, []
        self.streams, self.threads, self.prev_cpu = {}, [], {}
        self.samples_fd, self.sample_hash = None, hashlib.sha256()
        self.sample_count, self.sample_bytes, self.samples_dead = 0, 0, False
        self.created, self.root_fds, self.allow = {}, {}, {}
        self.lane_fd, self.lane_id, self.tmp_fd, self.tmp_id = None, None, None, None
        self.lane_bytes, self.charged, self.min_free = None, None, None
        self.maxima = {"lane_rss": 0, "lane_busy": 0, "owned_live": 0, "charged_bytes": 0}
        self.loop_status, self.authorization = "NOT_STARTED", None
        self.baseline = None
        self.helpers, self.helper_log = [], []
        self.helper_calls = 0
        self.phase = "ADMISSION"
        self.in_helper = False
        self.clock_observation = None
        self.unproved_history, self.coverage_history, self.census_history = {}, [], []
        self.runtime_observations = []
        self.stability_expiry_mono = None
        self.identity_history, self.attempt_history = {}, []
        self.history_charge, self.history_halted, self.history_overflow = 0, False, None
        self.ack_output_started = False
        self.publication_resources, self.ack_resources = None, None
        self.publication_payload_bytes, self.last_accounting_observation = None, None
        self.identity_events, self.identity_refs = [], {}
        self.accounting_observations, self.min_free_witness = [], None
        self.timing_failed, self.raw_sequence, self.raw_acquisitions = False, 0, {}
        self.last_native_free = None
        self.capture_fds = {}
        CANCEL_FAILURE_TARGET = self
        self.propagate_cancel_clock_error()

    def propagate_cancel_clock_error(self):
        if CANCEL.get("clock_error") is not None:
            self.timing_failed = True
            self.latch_failure("TIMING_EVIDENCE_UNAVAILABLE", ["cancel", CANCEL["clock_error"]])

    def deadline(self, seconds, phase=None):
        if (self.stop is not None and self.stop["mono"] is None) or \
                (self.child is not None and self.child["leader_reaped"] and self.exit_mono is None):
            raise GuardError("CLEANUP_DEADLINE_UNVERIFIABLE")
        cut = min([self.fit_mono] + [x[1] for x in self.cutoffs()])
        if phase is not None:
            cut = min(cut, phase.end)
        return Deadline(seconds, cut)

    def latch_failure(self, key, detail=None):
        if key not in self.failure_keys:
            self.failure_keys.add(key)
            self.failures.append({"code": key, "detail": str(detail)[:600] if detail is not None else None, "mono": None})
        return next(f for f in self.failures if f["code"] == key)

    def aux_clock(self, record, field, epoch=False, sink=False):
        """Optional evidence only. Never manufacture time or let it erase an already returned native value."""
        try:
            value = time.time() if epoch else time.monotonic()
            record[field] = value
            return value
        except BaseException as e:
            record[field], record[field + "_error"] = None, type(e).__name__
            self.timing_failed = True
            if not sink:
                self.latch_failure("TIMING_EVIDENCE_UNAVAILABLE", [field, type(e).__name__])
            return None

    def raw_acquisition(self, kind, source):
        if len(self.raw_acquisitions) >= 128:
            self.latch_failure("RAW_ACQUISITION_CAP")
            raise GuardError("RAW_ACQUISITION_CAP")
        self.raw_sequence += 1
        raw = {"id": self.raw_sequence, "kind": kind, "source": source, "native_returned": False,
               "mono_begin": None, "mono_end": None, "identity": None, "event_ref": None}
        self.raw_acquisitions[raw["id"]] = raw
        return raw

    def acquire_identity(self, pid, source, install=None):
        raw = self.raw_acquisition("identity", source)
        self.aux_clock(raw, "mono_begin")
        try:
            raw["identity"] = identify(pid)  # Preserve the returned native value BEFORE the end clock.
        except BaseException:
            if not self.timing_failed:
                del self.raw_acquisitions[raw["id"]]  # No complete identity was returned; coverage records the failure.
            raise
        raw["native_returned"] = True
        if install is not None:
            install(raw["identity"])
        self.aux_clock(raw, "mono_end")
        return raw

    def retain_acquisition(self, raw, known=False):
        if raw["mono_begin"] is None or raw["mono_end"] is None:
            self.timing_failed = True
            self.fail("IDENTITY_TIMING_UNAVAILABLE", raw["id"])
            raise GuardError("IDENTITY_TIMING_UNAVAILABLE")
        ref = self.retain_identity(raw["identity"], raw["source"], known, (raw["mono_begin"], raw["mono_end"]))
        raw["event_ref"] = ref
        del self.raw_acquisitions[raw["id"]]  # The complete canonical event now retains this same acquisition.
        return ref

    def fail(self, key, detail=None):
        fresh = key not in self.failure_keys
        row = self.latch_failure(key, detail)
        if fresh:
            self.aux_clock(row, "mono")
        if self.pid is not None and self.stop is None:
            self.request_stop("FAILURE")

    def latch_trip(self, key, detail=None):
        if key not in self.trips:
            self.trips[key] = {"trip": key, "detail": detail, "mono": None, "epoch": None}
        return self.trips[key]

    def trip(self, key, detail=None):
        row = self.latch_trip(key, detail)  # Preserve the known excess BEFORE any auxiliary clock can fail.
        if row["mono"] is None:
            self.aux_clock(row, "mono")
        if row["epoch"] is None:
            self.aux_clock(row, "epoch", epoch=True)
        self.request_stop(key)

    def enforce_runtime(self, where):
        if self.pid is None or self.mono_spawn is None:
            return
        now = time.monotonic()
        cutoff = self.mono_spawn + self.cfg["max_wall_s"]
        if now >= cutoff and "DEADLINE" not in self.trips:
            self.runtime_observations.append({"where": where, "mono": now, "mono_deadline": cutoff})
            late = now > cutoff + self.cfg["sample_s"] + 0.05
            self.trip("DEADLINE")
            if late:
                self.fail("MAIN_DEADLINE_ENFORCEMENT_LATE", {"mono_observed": now, "mono_deadline": cutoff})

    def reap_record(self, record, main=False):
        if record.get("pid") is None or record["leader_reaped"] or record["wait_lost"]:
            return
        try:
            result = os.waitpid(record["pid"], os.WNOHANG)
            record["native_wait_result"] = result  # Destructive result is latched before clocks or conversions.
        except ChildProcessError:
            record["wait_lost"] = True
            if main:
                self.lost_wait = True
            self.fail("WAIT_STATUS_LOST" if main else "HELPER_WAIT_STATUS_LOST")
            return
        pid, status = result
        if pid:
            record["raw_wait_status"] = status
            if not (os.WIFEXITED(status) or os.WIFSIGNALED(status)):
                self.fail("WAIT_RESULT_NOT_TERMINAL", [pid, status])
                return
            record["leader_reaped"] = True
            record["rc"] = os.waitstatus_to_exitcode(status)
            if main:
                self.rc = record["rc"]
            self.aux_clock(record, "mono_reaped")
            self.aux_clock(record, "epoch_reaped", epoch=True)
            if main:
                self.exit_mono, self.exit_epoch = record["mono_reaped"], record["epoch_reaped"]

    def reap(self):
        if self.pid is None or self.rc is not None or self.lost_wait or self.child.get("leader_reaped"):
            return
        try:
            self.enforce_runtime("before_waitpid")
        except BaseException as e:
            self.timing_failed = True
            self.fail("MAIN_RUNTIME_CLOCK_UNAVAILABLE", type(e).__name__)
        self.reap_record(self.child, main=True)
        if not self.timing_failed:
            self.enforce_runtime("after_waitpid_including_success")

    def request_stop(self, reason):
        if self.stop is not None:
            return
        self.stop = {"reason": reason, "mono": None, "epoch": None, "date": None}
        self.aux_clock(self.stop, "mono")
        self.aux_clock(self.stop, "epoch", epoch=True)
        self.signal_main_group()
        self.stop["date"] = self.date_now("stop")

    def signal_main_group(self):
        s = {"sent": False, "mono_check": None}
        self.signal = s
        self.aux_clock(s, "mono_check")
        if self.ident is None:
            s["why_not"] = "NO_IDENTITY"
            return
        if self.rc is not None or (self.child is not None and self.child["leader_reaped"]):
            s["why_not"] = "CHILD_ALREADY_REAPED"
            return
        if self.lost_wait:
            s["why_not"] = "WAIT_STATUS_LOST"
            return
        if self.cfg["fault_injection"].get("identity_check_fails"):
            s["why_not"] = "FAULT_INJECTED"
            self.fail("IDENTITY_UNVERIFIED", "fault injected")
            return
        try:
            dl = self.deadline(IO_S)
            raw = self.acquire_identity(self.pid, "main_signal",
                                        lambda p: s.update(identity_observed=dict(p)))
            s.update(mono_identity_begin=raw["mono_begin"], mono_identity_observed=raw["mono_end"],
                     raw_identity_ref=raw["id"])
            dl.check("after main stop identity")
            ok = fingerprint(raw["identity"]) == fingerprint(self.ident)
            s["identity_ok"] = ok
            if not ok:
                raise GuardError("identity mismatch")
            os.killpg(self.group, signal.SIGTERM)
            s["sent"] = True  # Native side effect is latched before its auxiliary timestamp.
            self.aux_clock(s, "mono_sent")
            dl.check("after main group SIGTERM")
        except ProcessLookupError as e:
            s["error"] = repr(e)
        except BaseException as e:
            s["error"] = repr(e)
            self.fail("IDENTITY_UNVERIFIED", repr(e))
        finally:
            if "identity_observed" in s:
                self.retain_signal_observation(s, "main_signal")

    def cutoffs(self):
        cuts = []
        if self.stop is not None and self.stop["mono"] is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_STOP_REQUEST", self.stop["mono"] + self.cfg["settle_s"]))
        if self.exit_mono is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_CHILD_EXIT", self.exit_mono + self.cfg["settle_s"]))
        return cuts

    def history_abort(self, kind, witness=None):
        if not self.history_halted:
            self.history_overflow = {"kind": kind, "mono": None, "witness": witness}
        self.history_halted = True  # The refusal boundary is latched before auxiliary timing.
        self.aux_clock(self.history_overflow, "mono")
        self.fail(kind, witness)
        raise GuardError(kind)

    def reserve_history(self, kind, new, old=None, witness=None, extra=0):
        if self.history_halted:
            raise GuardError("HISTORY_ALREADY_HALTED")
        def size(value):
            return len(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode())
        # Deliberate overcharge bounds the complete compact refusal envelope, not just entry counts.
        delta = max(0, size(new) - (0 if old is None else size(old)))
        charge = 2 * delta + (64 if old is None else 0) + extra
        if self.history_charge + charge > 4 << 20:
            self.history_abort("HISTORY_BYTE_CAP", witness)
        self.history_charge += charge

    def retain_identity(self, p, source, known=False, interval=None):
        """Retain one completed native acquisition. Event index is its one-based immutable reference."""
        if interval is None:
            raise GuardError("IDENTITY_OBSERVATION_INTERVAL_MISSING")
        begin, end = interval
        uid, old = p["uniqueid"], self.identity_history.get(p["uniqueid"])
        observed = {"identity": dict(p), "mono_begin": begin, "mono_end": end, "source": source}
        try:
            if old is None:
                if len(self.identity_history) >= 8192:
                    self.history_abort("IDENTITY_HISTORY_CAP", observed)
                variants, index = [dict(p)], 0
            else:
                variants = old["variants"]
                index = next((i for i, v in enumerate(variants) if identity_form(v) == identity_form(p)), None)
                if index is None:
                    if len(variants) >= 64:
                        self.history_abort("IDENTITY_VARIANT_CAP", observed)
                    index, variants = len(variants), variants + [dict(p)]
            ref = len(self.identity_events) + 1
            unproved = not known and self.baseline is not None and uid not in self.baseline and uid not in self.owned
            event = [uid, index, p["status"], begin, end, unproved]
            if old is None:
                new = {"first_identity": dict(p), "last_identity": dict(p), "mono_first_begin": begin,
                       "mono_first_seen": end, "mono_last_begin": begin, "mono_last_seen": end,
                       "first_event_ref": ref, "last_event_ref": ref, "source": source, "observations": 1, "variants": variants}
            else:
                new = dict(old, observations=old["observations"] + 1, variants=variants)
                if end < old["mono_first_seen"]:
                    new.update(first_identity=dict(p), mono_first_begin=begin, mono_first_seen=end, first_event_ref=ref)
                if end >= old["mono_last_seen"]:
                    new.update(last_identity=dict(p), mono_last_begin=begin, mono_last_seen=end, last_event_ref=ref)
            self.reserve_history("identity", new, old, observed)
            self.reserve_history("identity_event", event, [], observed, extra=4)
            self.identity_events.append(event)
            self.identity_history[uid] = new
            self.identity_refs[(uid, index, p["status"])] = ref
            # Unproved classification is retained NOW, even if a later PID/edge/measurement aborts.
            if unproved:
                previous = self.unproved_history.get(uid)
                if previous is None:
                    if len(self.unproved_history) >= 8192:
                        self.history_abort("UNPROVED_HISTORY_CAP", observed)
                    unknown = {"first_identity": dict(p), "last_identity": dict(p), "mono_first_begin": begin,
                               "mono_first_seen": end, "mono_last_begin": begin, "mono_last_seen": end,
                               "first_event_ref": ref, "last_event_ref": ref}
                else:
                    unknown = dict(previous)
                    if end < previous["mono_first_seen"]:
                        unknown.update(first_identity=dict(p), mono_first_begin=begin, mono_first_seen=end, first_event_ref=ref)
                    if end >= previous["mono_last_seen"]:
                        unknown.update(last_identity=dict(p), mono_last_begin=begin, mono_last_seen=end, last_event_ref=ref)
                self.reserve_history("unproved", unknown, previous, observed)
                self.unproved_history[uid] = unknown
            return ref
        except BaseException:
            if self.history_halted and self.history_overflow is not None:
                self.history_overflow["completed_identity_observation"] = observed
            raise

    def identity_ref(self, p):
        entry = self.identity_history[p["uniqueid"]]
        index = next(i for i, v in enumerate(entry["variants"]) if identity_form(v) == identity_form(p))
        return self.identity_refs[(p["uniqueid"], index, p["status"])]

    def retain_signal_observation(self, record, source):
        """Signal safety never waits for telemetry. Preserve the raw bounded witness even after a cap."""
        record["identity_event_ref"] = None
        if self.history_halted or record.get("mono_identity_begin") is None or record.get("mono_identity_observed") is None:
            return
        try:
            raw = self.raw_acquisitions.get(record.get("raw_identity_ref"))
            if raw is not None:
                record["identity_event_ref"] = self.retain_acquisition(raw, record.get("identity_ok") is True)
            else:
                record["identity_event_ref"] = self.retain_identity(
                    record["identity_observed"], source, record.get("identity_ok") is True,
                    (record["mono_identity_begin"], record["mono_identity_observed"]))
        except BaseException as e:
            record["identity_event_error"] = repr(e)[:600]

    @contextlib.contextmanager
    def observation_attempt(self, kind, resources=None):
        if self.history_halted:
            raise GuardError("HISTORY_ALREADY_HALTED")
        if len(self.attempt_history) >= 4096:
            self.history_abort("ATTEMPT_HISTORY_CAP", {"kind": kind})
        attempt = {"kind": kind, "phase": self.phase, "inside_helper": self.in_helper,
                   "mono_start": time.monotonic(), "mono_end": None, "aborted": False, "error": None}
        self.reserve_history("attempt", attempt, extra=2048)
        self.attempt_history.append(attempt)
        try:
            yield attempt
        except BaseException as e:
            attempt.update(aborted=True, error=repr(e)[:600])
            if resources is not None:
                resources.update(complete=False, aborted=True, abort_error=repr(e)[:600], mono_aborted=None)
                self.aux_clock(resources, "mono_aborted")
                self.enforce_observed_resources(resources)
            raise
        finally:
            self.aux_clock(attempt, "mono_end")
            if resources is not None:
                resources["mono_end"] = attempt["mono_end"]

    def enforce_observed_resources(self, c):
        if self.phase in ("ADMISSION", "PRE_GO"):
            if not self.limits(c, True):
                self.fail("ADMISSION_RESOURCE_VIOLATION",
                          {"busy": c["lane_busy"], "rss": c["lane_rss"], "partial": True})
        else:
            self.limits(c)

    def reconciliation_evidence(self):
        view = {"owned_identities": list(self.owned.values()), "unproved_history": list(self.unproved_history.values()),
                "identity_history": list(self.identity_history.values()), "coverage_history": self.coverage_history,
                "identity_events": list(self.identity_events), "initial_fit": self.rec["initial_fit"],
                "authorization": self.authorization, "accounting_observations": list(self.accounting_observations),
                "min_free_witness": self.min_free_witness,
                "census_observations": self.census_history, "observation_attempts": self.attempt_history,
                "helpers": self.helper_reports(), "helper_log": self.helper_log, "failures": self.failures,
                "main_identity": self.ident, "main_signal": self.signal, "main_stop": self.stop,
                "baseline_uniqueids": [] if self.baseline is None else sorted(self.baseline),
                "stability_expiry_mono": self.stability_expiry_mono,
                "history_charge_bytes": self.history_charge, "history_cap_bytes": 4 << 20,
                "history_halted": self.history_halted, "history_overflow": self.history_overflow,
                "publication_resources": self.publication_resources, "ack_resources": self.ack_resources,
                "publication_payload_bytes": self.publication_payload_bytes,
                "last_accounting_observation": self.last_accounting_observation,
                "maxima": dict(self.maxima), "min_free": self.min_free,
                "streams": {k: dict(v) for k, v in self.streams.items()}, "mono_snapshot": None,
                "timing_failed": self.timing_failed, "raw_acquisitions": list(self.raw_acquisitions.values()),
                "last_native_free": self.last_native_free,
                "main_wait": None if self.child is None else {k: self.child.get(k) for k in
                    ("pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "mono_reaped", "epoch_reaped")}}
        self.aux_clock(view, "mono_snapshot")
        view["timing_failed"] = self.timing_failed
        return view

    def observed_identity(self, pid, source, known=False):
        if self.timing_failed:
            raise GuardError("TIMING_EVIDENCE_UNAVAILABLE_NO_SCAN_RETRY")
        raw = self.acquire_identity(pid, source)
        self.retain_acquisition(raw, known)
        return raw["identity"]

    def identity_stable(self, pid, before):
        p = self.observed_identity(pid, "measurement_bracket")
        return fingerprint(p) == fingerprint(before)

    def register_owned(self, p, via, root=None, proof=None):
        u = p["uniqueid"]
        ref = self.identity_ref(p)  # Registration reuses its actual acquisition, never invents another observation.
        if u not in self.owned:
            entry = {"identity": dict(p), "identity_event_ref": ref, "via": via, "root": u if root is None else root,
                     "first_seen_mono": None, "proof": proof}
            self.aux_clock(entry, "first_seen_mono")
            self.reserve_history("owned", entry, witness=dict(p))
            self.owned[u] = entry
            if via not in ("child", "helper"):
                self.violations.append(dict(p))

    def scan_identities(self, dl):
        if self.timing_failed:
            raise GuardError("TIMING_EVIDENCE_UNAVAILABLE_NO_SCAN_RETRY")
        with self.observation_attempt("identity_scan") as attempt:
            procs, missing = {}, []
            for pid in all_pids(dl):
                dl.check("census identification")
                try:
                    p = self.observed_identity(pid, "pid_scan")
                    procs[pid] = p
                    attempt["identified_count"] = len(procs)
                except OSError as e:
                    if self.history_halted or self.timing_failed:
                        raise
                    error = [pid, "identify", repr(e)[:600]]
                    missing.append(error)
                    self.retain_coverage([error], None)
            live_owned = {p["uniqueid"] for p in procs.values() if p["uniqueid"] in self.owned}
            groups = {self.group: self.ident["uniqueid"]} if self.group is not None and self.ident is not None else {}
            for h in self.helpers:
                if h.get("identity") is not None:
                    groups[h["identity"]["pgid"]] = h["identity"]["uniqueid"]
            if self.ident is not None:
                for p in procs.values():
                    if p["uniqueid"] == self.ident["uniqueid"] and fingerprint(p) != fingerprint(self.ident):
                        self.fail("CHILD_IDENTITY_CHANGED", p)
            for p in procs.values():
                if p["pgid"] in groups:
                    self.register_owned(p, "owned_group", groups[p["pgid"]])
                    live_owned.add(p["uniqueid"])
            changed = True
            while changed:
                changed = False
                for p in procs.values():
                    if p["uniqueid"] in live_owned:
                        continue
                    parent = procs.get(p["ppid"])
                    if parent is None or parent["uniqueid"] not in live_owned:
                        continue
                    try:
                        a = self.observed_identity(parent["pid"], "edge_parent_before")
                        a_ref = self.identity_ref(a)
                        b = self.observed_identity(p["pid"], "edge_child")
                        b_ref = self.identity_ref(b)
                        c = self.observed_identity(parent["pid"], "edge_parent_after")
                        c_ref = self.identity_ref(c)
                        if fingerprint(a) != fingerprint(parent) or fingerprint(c) != fingerprint(parent) or fingerprint(b) != fingerprint(p):
                            raise GuardError("CURRENT_PARENT_EDGE_CHANGED")
                        root = self.owned[parent["uniqueid"]]["root"]
                        self.register_owned(p, "current_parent:%d" % parent["uniqueid"], root,
                                            {"parent_before_ref": a_ref, "child_ref": b_ref, "parent_after_ref": c_ref})
                        live_owned.add(p["uniqueid"])
                        changed = True
                    except OSError as e:
                        if self.history_halted or self.timing_failed:
                            raise
                        error = [p["pid"], "parent_edge", repr(e)[:600]]
                        missing.append(error)
                        self.retain_coverage([error], None)
            unproved = {p["uniqueid"] for p in procs.values()
                        if self.baseline is not None and p["uniqueid"] not in self.baseline and p["uniqueid"] not in live_owned}
            dl.check("after identity/ownership scan")
            return procs, missing, live_owned, unproved

    def retain_coverage(self, missing, stamp=None):
        for item in missing:
            if len(self.coverage_history) >= 16384:
                self.history_abort("COVERAGE_HISTORY_CAP", {"observation": item})
            entry = {"mono": stamp, "observation": list(item)}
            if stamp is None:
                self.aux_clock(entry, "mono")
            self.reserve_history("coverage", entry, witness={"observation": item})
            self.coverage_history.append(entry)

    def establish_baseline(self):
        dl = Deadline(20, self.fit_mono)
        for _ in range(3):
            procs, missing, _, _ = self.scan_identities(dl)
            if not missing:
                self.baseline = {p["uniqueid"] for p in procs.values()}
                ordered = sorted(procs.values(), key=lambda p: p["pid"])
                self.rec["baseline"] = {"mono_complete": time.monotonic(), "identities": ordered,
                                        "event_refs": [self.identity_ref(p) for p in ordered]}
                dl.check("after baseline")
                return
            time.sleep(0.05)
        raise GuardError("NO_COMPLETE_PRESPAWN_BASELINE")

    def census(self, dl):
        if len(self.census_history) >= 4096:
            self.history_abort("CENSUS_HISTORY_CAP", {"phase": self.phase})
        record = {"phase": self.phase, "inside_helper": self.in_helper, "complete": False, "aborted": False,
                  "mono_start": time.monotonic(), "mono_complete": None, "incomplete_n": 0, "incomplete": [],
                  "pids": 0, "owned_live": [], "unproved_live": [], "group_live": [], "owned_zombies": [],
                  "owned_event_refs": [], "unproved_event_refs": [],
                  "lane_pids": [], "lane_rss": 0, "lane_busy_pids": [], "lane_busy": 0, "measurements": []}
        self.reserve_history("resource_attempt", record, extra=2048)
        self.census_history.append(record)  # Retained BEFORE identity or resource I/O can abort.
        with self.observation_attempt("resource_scan", record):
            procs, missing, live_owned, unproved = self.scan_identities(dl)
            header = dict(record, pids=len(procs), incomplete_n=len(missing), incomplete=missing[:30],
                          owned_live=[dict(p) for p in procs.values() if p["uniqueid"] in live_owned],
                          unproved_live=[dict(p) for p in procs.values() if p["uniqueid"] in unproved],
                          owned_event_refs=[self.identity_ref(p) for p in procs.values() if p["uniqueid"] in live_owned],
                          unproved_event_refs=[self.identity_ref(p) for p in procs.values() if p["uniqueid"] in unproved],
                          group_live=sorted(p["pid"] for p in procs.values() if self.group is not None and p["pgid"] == self.group),
                          owned_zombies=sorted(p["pid"] for p in procs.values() if p["uniqueid"] in live_owned and p["status"] == SZOMB))
            self.reserve_history("resource_header", header, record, {"phase": self.phase})
            record.update(header)
            cpu = {}
            for pid, p in procs.items():
                dl.check("census accounting")
                if p["status"] == SZOMB or not (p["euid"] == MY_UID or p["ruid"] == MY_UID):
                    continue
                owned = p["uniqueid"] in live_owned or p["uniqueid"] in unproved
                task = None
                try:
                    if not self.identity_stable(pid, p):
                        raise GuardError("BEFORE_MEASUREMENT_CHANGED")
                    member = owned
                    if not member:
                        c1 = cwd_of(pid)
                        av = argv_of(pid, self.arg_max)
                        c2 = cwd_of(pid)
                        member = any(below(c, r) for c in (c1, c2) for r in self.cfg["lane_roots"]) or any(
                            r in a for a in av for r in self.cfg["lane_roots"])
                    if not self.identity_stable(pid, p):
                        raise GuardError("MEMBERSHIP_IDENTITY_CHANGED")
                    if not member:
                        continue
                    before_task_ref = self.identity_ref(self.identity_history[p["uniqueid"]]["last_identity"])
                    task = self.raw_acquisition("task", "lane_measurement")
                    task["identity"] = dict(p)
                    self.aux_clock(task, "mono_begin")
                    task["native_result"] = task_of(pid)  # Raw RSS/ticks are retained BEFORE task-end timing.
                    task["native_returned"] = True
                    rss, ticks = task["native_result"]
                    self.aux_clock(task, "mono_end")
                    key = (p["uniqueid"], p["idversion"])
                    prior = self.prev_cpu.get(key)
                    task["native_start_epoch"] = start_of(pid) if prior is None else None
                    measured = {"identity": dict(p), "identity_event_ref": self.identity_ref(p),
                                "before_task_event_ref": before_task_ref, "identity_after": None,
                                "identity_after_event_ref": None, "identity_after_interval": [None, None],
                                "mono_task_begin": task["mono_begin"], "mono_task_end": task["mono_end"],
                                "rss": rss, "cpu_ticks": ticks, "busy": None, "mono_observed": None,
                                "bracket_verified": False}
                    task["measurement"] = measured
                    record.setdefault("raw_measurements", []).append(measured)
                    def install_final(after):
                        measured["identity_after"] = dict(after)
                        if fingerprint(after) != fingerprint(p):
                            raise GuardError("TASK_IDENTITY_CHANGED")
                        measured["bracket_verified"] = True
                        record["lane_pids"].append(pid)
                        record["lane_rss"] += rss
                        record["measurements"].append(measured)
                        # Latch the verified excess itself before any end-clock or telemetry can fail.
                        if self.phase not in ("ADMISSION", "PRE_GO") and record["lane_rss"] > self.cfg["rss_trip_bytes"]:
                            self.latch_trip("RSS", record["lane_rss"])
                        if self.phase in ("ADMISSION", "PRE_GO") and \
                                record["lane_rss"] + self.cfg["rss_projection_bytes"] > self.cfg["rss_trip_bytes"]:
                            self.latch_failure("ADMISSION_RESOURCE_VIOLATION", {"rss": record["lane_rss"], "partial": True})
                    final = self.acquire_identity(pid, "measurement_final_bracket", install_final)
                    measured["identity_after_interval"] = [final["mono_begin"], final["mono_end"]]
                    self.aux_clock(measured, "mono_observed")
                    self.aux_clock(measured, "epoch_observed", epoch=True)
                    times = (task["mono_begin"], task["mono_end"], final["mono_begin"], final["mono_end"],
                             measured["mono_observed"], measured["epoch_observed"])
                    if any(value is None for value in times):
                        self.timing_failed = True
                        self.enforce_observed_resources(record)  # The known RSS latch survives missing BUSY timing.
                        self.fail("RESOURCE_TIMING_UNAVAILABLE", task["id"])
                        raise GuardError("RESOURCE_TIMING_UNAVAILABLE")
                    now_m, now_e = measured["mono_observed"], measured["epoch_observed"]
                    if prior is None:
                        seconds = now_e - task["native_start_epoch"]
                        busy = seconds <= 0.05 or ticks * self.num_tb >= seconds * 1e9 * self.cfg["busy_cpu_fraction"]
                    else:
                        seconds = now_m - prior[0]
                        busy = seconds <= 0 or (ticks - prior[1]) * self.num_tb >= seconds * 1e9 * self.cfg["busy_cpu_fraction"]
                    measured["busy"] = busy
                    if busy:
                        record["lane_busy_pids"].append(pid)
                        record["lane_busy"] += 1
                    record["mono_last_observation"] = now_m
                    cpu[key] = (now_m, ticks)
                    try:
                        self.enforce_observed_resources(record)
                        measured["identity_after_event_ref"] = self.retain_acquisition(final)
                        self.reserve_history("measurement", measured, witness=measured, extra=256)
                        record["raw_measurements"].remove(measured)
                        del self.raw_acquisitions[task["id"]]
                    except BaseException:
                        if self.history_halted and self.history_overflow is not None:
                            self.history_overflow["completed_measurement"] = measured
                        self.enforce_observed_resources(record)
                        raise
                except OSError as e:
                    if task is not None:
                        if task.get("native_returned"):
                            self.fail("RESOURCE_ACQUISITION_INCOMPLETE", task["id"])
                            raise  # A later retry must not erase this returned native observation.
                        self.raw_acquisitions.pop(task["id"], None)
                    if self.history_halted or self.timing_failed:
                        raise
                    error = [pid, "real_or_effective_uid_measurement", repr(e)[:600]]
                    missing.append(error)
                    self.retain_coverage([error], None)
                    record["incomplete_n"] = len(missing)
                    record["incomplete"] = missing[:30]
            self.prev_cpu = cpu
            record["lane_pids"].sort()
            record["lane_busy_pids"].sort()
            self.enforce_observed_resources(record)
            dl.check("after census including completed resource observations")
            record.update(complete=not missing, incomplete_n=len(missing), incomplete=missing[:30],
                          mono_complete=time.monotonic())
            return record

    def full_census(self, dl):
        c = None
        for _ in range(3):
            c = self.census(dl)
            # Enforce EVERY observation, not only the final successful retry.
            if self.phase in ("ADMISSION", "PRE_GO"):
                if not self.limits(c, True):
                    self.fail("ADMISSION_RESOURCE_VIOLATION", {"busy": c["lane_busy"], "rss": c["lane_rss"],
                                                               "incomplete": not c["complete"]})
            else:
                self.limits(c)
            if c["complete"]:
                break
            dl.check("before census retry")
            time.sleep(min(0.05, max(0, dl.end - time.monotonic())))
        dl.check("after census retries")
        return c

    def close_record_endpoints(self, record, readers=False):
        errors = record.setdefault("endpoint_errors", [])
        for fd in list(record["parent_close_fds"]):
            try:
                os.close(fd)
                record["parent_close_fds"].remove(fd)
            except OSError as e:
                errors.append([fd, type(e).__name__])
        names = ("stdin_fd", "stdout_fd", "stderr_fd") if readers else ("stdin_fd",)
        for name in names:
            fd = record.get(name)
            if fd is not None:
                try:
                    os.close(fd)
                    record[name] = None
                except OSError as e:
                    errors.append([name, type(e).__name__])

    def helper_clockless_once(self, h):
        """Finite reap/drain/endpoint attempt, never a clockless ownership proof or extra TERM."""
        count = h.get("clockless_probe_count", 0)
        if count >= 3:
            h["settled"] = False
            return
        h["clockless_probe_count"] = count + 1
        h["clockless_probe_done"] = True
        self.close_record_endpoints(h)
        self.reap_record(h)
        fd = h.get("stdout_fd")
        if fd is not None:
            try:
                os.set_blocking(fd, False)
                data = os.read(fd, max(1, 257 - len(h.get("capture", b""))))
                h["capture"] = h.get("capture", b"") + data
                h["raw_eof"] = data == b""
                h["capture_overflow"] = len(h["capture"]) > 256
                if h["raw_eof"] or h["capture_overflow"]:
                    os.close(fd)
                    h["stdout_fd"], h["stdout_closed"] = None, True
            except BlockingIOError:
                pass
            except BaseException as e:
                h["clockless_capture_error"] = type(e).__name__
        h["settled"] = False

    def helper_probe(self, h, dl):
        """Refresh ALL ownership predicates; REAPED alone never marks a helper settled."""
        if h["pid"] is None:
            return
        if self.timing_failed:
            self.helper_clockless_once(h)
            raise GuardError("HELPER_TIMING_EVIDENCE_UNAVAILABLE")
        for fd in list(h["parent_close_fds"]):
            os.close(fd)
            h["parent_close_fds"].remove(fd)
            dl.check("helper parent endpoint close")
        if self.history_halted:
            # Still reap/drain within the bounded cleanup; never claim group/coverage proof from a full ledger.
            self.reap_record(h)
            dl.check("after cap-path helper reap")
            if h.get("stdout_fd") is not None:
                os.set_blocking(h["stdout_fd"], False)
                try:
                    data = os.read(h["stdout_fd"], max(1, 257 - len(h["capture"])))
                    h["capture"] += data
                    if data == b"" or len(h["capture"]) > 256:
                        h["raw_eof"] = data == b""
                        h["capture_overflow"] = len(h["capture"]) > 256
                        os.close(h["stdout_fd"])
                        h["stdout_fd"], h["stdout_closed"] = None, True
                    dl.check("after cap-path helper capture/close")
                except BlockingIOError:
                    pass
            h["settled"] = False
            raise GuardError("HISTORY_HALTED_HELPER_PROOF_UNAVAILABLE")
        if h.get("identity") is None and not h["leader_reaped"]:
            def install(p):
                h["identity"] = p
                h["initial_identity_valid"] = p["pgid"] == h["pid"] and p["euid"] == MY_UID and p["ruid"] == MY_UID
            raw = self.acquire_identity(h["pid"], "helper_initial", install)
            p = h["identity"]
            h["raw_identity_ref"] = raw["id"]
            h["identity_event_ref"] = self.retain_acquisition(raw, h["initial_identity_valid"])
            if not h["initial_identity_valid"]:
                raise GuardError("HELPER_IDENTITY_INVALID")
            self.register_owned(p, "helper")
        if not h["leader_reaped"] and not self.identity_stable(h["pid"], h["identity"]):
            raise GuardError("HELPER_EXEC_OR_CREDENTIAL_CHANGE")
        if not h["leader_reaped"] and not h["wait_lost"]:
            self.reap_record(h)
            dl.check("after helper reap, including a successful reap")
        fd = h.get("stdout_fd")
        if fd is not None:
            os.set_blocking(fd, False)
            for _ in range(2):
                try:
                    room = 257 - len(h["capture"])
                    if room <= 0:
                        h["capture_overflow"] = True
                        break
                    b = os.read(fd, room)
                except BlockingIOError:
                    break
                h["capture"] += b  # Native bytes/EOF survive a subsequent deadline clock failure.
                if b == b"":
                    h["raw_eof"] = True
                if len(h["capture"]) > 256:
                    h["capture_overflow"] = True
                dl.check("after helper stdout read")
                if h["raw_eof"] or h["capture_overflow"]:
                    break
            if h["raw_eof"] or h["capture_overflow"]:
                os.close(fd)
                h["stdout_fd"], h["stdout_closed"] = None, True
                dl.check("after helper stdout close")
        c = self.full_census(dl)
        proof = {k: c[k] for k in ("complete", "incomplete_n", "owned_live", "unproved_live", "mono_complete")}
        self.reserve_history("helper_proof", proof, h.get("proof"), {"helper_pid": h["pid"]})
        h["proof"] = proof
        root = None if h.get("identity") is None else h["identity"]["uniqueid"]
        h["group_clear"] = h.get("identity") is not None and not any(p["pgid"] == h["identity"]["pgid"] for p in c["owned_live"])
        h["descendants_clear"] = root is not None and not any(self.owned[p["uniqueid"]]["root"] == root for p in c["owned_live"])
        h["coverage_complete"] = c["complete"] and not c["unproved_live"]
        h["eof_proved"] = h["raw_eof"] and not h["capture_overflow"]
        if h["fault_group"]:
            h["group_clear"] = False
        if h["fault_eof"]:
            h["eof_proved"] = False
        dl.check("after full helper ownership proof")
        self.aux_clock(h, "mono_proof_complete")
        h["settled"] = bool(not self.timing_failed and h.get("initial_identity_valid") and h["leader_reaped"] and not h["wait_lost"] and
                            h["group_clear"] and h["descendants_clear"] and h["coverage_complete"] and
                            h["eof_proved"] and h["stdout_closed"])

    def helper_term(self, h, dl):
        if h["term_attempted"] or h["leader_reaped"] or h["wait_lost"]:
            return
        h["term_attempted"] = True
        ident = h.get("identity")
        if ident is None or not h.get("initial_identity_valid"):
            h["signal"] = {"sent": False, "reason": "NO_VERIFIED_IDENTITY"}
            return
        h["signal"] = {"sent": False, "mono_check": None}
        self.aux_clock(h["signal"], "mono_check")
        try:
            raw = self.acquire_identity(h["pid"], "helper_signal",
                                        lambda p: h["signal"].update(identity_observed=dict(p)))
            p = raw["identity"]
            h["signal"].update(mono_identity_begin=raw["mono_begin"], mono_identity_observed=raw["mono_end"],
                               raw_identity_ref=raw["id"])
            dl.check("after helper stop identity")
            h["signal"]["identity_ok"] = fingerprint(p) == fingerprint(ident)
            if not h["signal"]["identity_ok"]:
                raise GuardError("HELPER_SIGNAL_IDENTITY_CHANGED")
            os.killpg(ident["pgid"], signal.SIGTERM)
            h["signal"].update(sent=True, identity_ok=True)
            self.aux_clock(h["signal"], "mono_sent")
            dl.check("after helper group SIGTERM")
        except BaseException as e:
            h["signal"]["reason"] = repr(e)
        finally:
            if "identity_observed" in h["signal"]:
                self.retain_signal_observation(h["signal"], "helper_signal")

    def helper_cleanup(self, h):
        """One fresh checked TERM at most; missing clock evidence permits only finite raw cleanup and HOLD."""
        h["mono_cleanup_start"] = None
        self.aux_clock(h, "mono_cleanup_start")
        try:
            dl = self.deadline(self.cfg["helper_budget"]["term_grace_s"])
            h["mono_cleanup_deadline"], h["cleanup_deadline"] = dl.end, dl.telemetry()
        except BaseException as e:
            h["mono_cleanup_deadline"], h["cleanup_deadline"] = None, None
            h["cleanup_error"] = type(e).__name__
            self.timing_failed = True
            self.helper_clockless_once(h)
            self.fail("HELPER_OWNERSHIP_UNSETTLED", h["pid"])
            return
        if h.get("identity") is None and not h["leader_reaped"]:
            try:
                def install(p):
                    h["identity"] = p
                    h["initial_identity_valid"] = p["pgid"] == h["pid"] and p["euid"] == MY_UID and p["ruid"] == MY_UID
                raw = self.acquire_identity(h["pid"], "helper_cleanup_initial", install)
                h["raw_identity_ref"] = raw["id"]
                h["identity_event_ref"] = self.retain_acquisition(raw, h["initial_identity_valid"])
                if h["initial_identity_valid"]:
                    self.register_owned(h["identity"], "helper")
            except BaseException as e:
                h["identity_error"] = repr(e)
        try:
            dl.check("before cleanup signal")
            self.helper_term(h, dl)
        except BaseException as e:
            h["cleanup_error"] = repr(e)
        while not self.timing_failed:
            try:
                dl.check("before cleanup probe")
                self.helper_probe(h, dl)
                if h["settled"]:
                    return
            except BaseException as e:
                h["cleanup_error"] = repr(e)
                if isinstance(e, GuardError) and str(e).startswith("CLOCK_UNAVAILABLE"):
                    self.timing_failed = True
                    self.latch_failure("TIMING_EVIDENCE_UNAVAILABLE", str(e))
                    break
            try:
                remaining = dl.end - time.monotonic()
            except BaseException as e:
                self.timing_failed = True
                self.latch_failure("TIMING_EVIDENCE_UNAVAILABLE", type(e).__name__)
                break
            if remaining < 0:
                break
            time.sleep(min(0.005, remaining))
        if self.timing_failed:
            self.helper_clockless_once(h)
        self.fail("HELPER_OWNERSHIP_UNSETTLED", {"pid": h["pid"], "reaped": h["leader_reaped"],
                                                "group_clear": h.get("group_clear"), "eof": h.get("eof_proved")})

    def date_now(self, purpose):
        """Actual /bin/date output only. Logical refusals return null; no synthetic timestamp."""
        entry = {"purpose": purpose, "mono_start": None, "mono_end": None}
        self.aux_clock(entry, "mono_start")
        h = None
        hb = self.cfg["helper_budget"]
        try:
            if self.failures or self.timing_failed or pending_cancel() or self.in_helper:
                entry["outcome"] = "REFUSED_FAILURE_CANCEL_OR_REENTRANCY"
                return None
            if self.authorization is None:
                entry["outcome"] = "REFUSED_NO_AUTHORIZATION"
                return None
            if self.helper_calls >= hb["max_calls"]:
                self.fail("HELPER_CALL_BUDGET")
                entry["outcome"] = "CALL_BUDGET_REFUSED"
                return None
            if self.cfg["fault_injection"].get("date_helper_fails"):
                self.fail("HELPER_FAULT_INJECTED")
                entry["outcome"] = "FAULT_BEFORE_SPAWN"
                return None
            if self.baseline is None:
                self.fail("NO_PREHELPER_BASELINE")
                entry["outcome"] = "NO_BASELINE"
                return None
            self.in_helper = True
            call = self.deadline(hb["call_budget_s"])  # BEFORE pipe creation and spawn.
            try:
                h = spawn_registered(self, ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], {"PATH": "/usr/bin:/bin"},
                                     "helper", call, hb["call_budget_s"] + hb["term_grace_s"])
            except BaseException:
                # The allocation ledger is pre-registered; recover any returned PID even if later setup failed.
                h = next((r for r in reversed(self.helpers) if r.get("pid") is not None and "capture" not in r), None)
                raise
            h.update(capture=b"", raw_eof=False, stdout_closed=False, capture_overflow=False,
                     initial_identity_valid=False, clock_failed=False,
                     fault_group=bool(self.cfg["fault_injection"].get("helper_group_unproved")),
                     fault_eof=bool(self.cfg["fault_injection"].get("helper_eof_unproved")),
                     mono_call_start=entry["mono_start"], mono_call_deadline=call.end, date=None)
            h["call_deadline"] = call.telemetry()
            entry["pid"] = h["pid"]
            if self.cfg["fault_injection"].get("helper_observation_overrun"):
                h["mono_injection_start"] = time.monotonic()
                time.sleep(max(0.0, call.end - time.monotonic()) + 0.01)
                h["mono_injection_end"] = time.monotonic()
                if h["mono_injection_end"] <= call.end:
                    raise GuardError("OVERRUN_STIMULUS_NOT_ESTABLISHED")
            if h["spawn_error"] is not None:
                raise GuardError(h["spawn_error"])
            while True:
                if pending_cancel():
                    raise GuardError("HELPER_CANCELLED_AFTER_COMMIT")
                self.helper_probe(h, call)
                call.check("after helper completion, never accept a late successful reap")
                if h["settled"]:
                    break
                time.sleep(min(0.005, max(0, call.end - time.monotonic())))
            text = h["capture"].decode("ascii", "strict").strip()
            shape = len(text) == 24 and text[4:5] == "-" and text[7:8] == "-" and text[10:11] == "T" and text[19:20] in ("+", "-")
            digits = text[:4] + text[5:7] + text[8:10] + text[11:13] + text[14:16] + text[17:19] + text[20:24]
            if h["rc"] != 0 or not shape or not digits.isdigit() or text[13:14] != ":" or text[16:17] != ":":
                raise GuardError("HELPER_BAD_DATE_OUTPUT")
            h["date"] = text
            observation = {"date": text, "mono_before_read": entry["mono_start"],
                           "mono_after_read": time.monotonic(), "epoch_date_floor": parse_date_epoch(text)}
            base_age = observation["epoch_date_floor"] - self.authorization["stability_epoch"] + 1.0
            if base_age < 1.0:
                raise GuardError("STABILITY_TIMESTAMP_IN_FUTURE")
            candidate = observation["mono_before_read"] + self.cfg["admission"]["stability_max_age_s"] - base_age
            h["stability_expiry_before"] = self.stability_expiry_mono
            h["stability_expiry_candidate"] = candidate
            self.stability_expiry_mono = candidate if self.stability_expiry_mono is None else min(self.stability_expiry_mono, candidate)
            h["stability_expiry_effective"] = self.stability_expiry_mono
            self.clock_observation = observation
            entry["outcome"] = "OK"
            return text
        except BaseException as e:
            entry["outcome"], entry["error"] = "FAILED", repr(e)
            self.fail("HELPER_CALL_FAILED", repr(e))
            if h is not None and h.get("pid") is not None:
                # Populate absent fields before exceptional cleanup; registered ownership is never discarded.
                for key, value in {"capture": b"", "raw_eof": False, "stdout_closed": False, "capture_overflow": False,
                                   "initial_identity_valid": False,
                                   "fault_group": bool(self.cfg["fault_injection"].get("helper_group_unproved")),
                                   "fault_eof": bool(self.cfg["fault_injection"].get("helper_eof_unproved")),
                                   "mono_call_start": entry["mono_start"], "mono_call_deadline": call.end,
                                   "call_deadline": call.telemetry(),
                                   "date": None}.items():
                    h.setdefault(key, value)
                h["clock_failed"] = True
                self.helper_cleanup(h)
            return None
        finally:
            self.in_helper = False
            self.aux_clock(entry, "mono_end")
            self.helper_log.append(entry)

    def refresh_helpers(self, dl):
        for h in self.helpers:
            if h.get("pid") is not None and not h["settled"]:
                try:
                    self.helper_probe(h, dl)
                except BaseException as e:
                    h["final_proof_error"] = repr(e)
                if not h["settled"]:
                    self.fail("HELPER_OWNERSHIP_UNSETTLED", h["pid"])

    def helper_reports(self):
        keys = ("pid", "identity", "identity_event_ref", "leader_reaped", "rc", "wait_lost", "term_attempted", "settled",
                "initial_identity_valid", "stdout_closed", "eof_proved", "group_clear", "descendants_clear",
                "coverage_complete", "clock_failed", "date", "signal", "proof", "spawn_error", "launch_commit",
                "mono_spawn", "epoch_spawn", "mono_pid_registered", "call_deadline", "cleanup_deadline",
                "native_wait_result", "raw_wait_status", "epoch_reaped", "raw_identity_ref", "clockless_probe_done", "clockless_probe_count", "endpoint_errors",
                "mono_call_start", "mono_call_deadline", "mono_cleanup_start", "mono_cleanup_deadline",
                "mono_proof_complete", "mono_reaped", "mono_injection_start", "mono_injection_end",
                "stability_expiry_before", "stability_expiry_candidate", "stability_expiry_effective")
        return [{**{k: h.get(k) for k in keys}, "capture_hex": h.get("capture", b"").hex()}
                for h in self.helpers if h.get("pid") is not None]

    def open_anchors(self):
        dl = Deadline(IO_S)
        root = self.cfg["lane_disk_root"]
        self.lane_fd = absolute_directory(root, dl)
        self.lane_id = stat_id(self.lane_fd)
        for r in self.cfg["output_roots"]:
            fd = directory_at(self.lane_fd, os.path.relpath(r, root), dl)
            self.root_fds[r] = (fd, stat_id(fd))
            self.allow[r] = set()
        tmp = self.cfg["env"]["TMPDIR"]
        self.tmp_fd = directory_at(self.lane_fd, os.path.relpath(tmp, root), dl)
        self.tmp_id = stat_id(self.tmp_fd)
        for p in [self.cfg[k] for k in ("stdout", "stderr", "samples", "launch_record", "receipt", "settlement_record")] + [o["path"] for o in self.cfg["outputs"]]:
            self.allow[os.path.dirname(p)].add(os.path.basename(p))
        self.allow[os.path.dirname(self.cfg["settlement_record"])].add(os.path.basename(self.cfg["settlement_record"]) + ".staged")
        self.verify_anchors(dl)

    def verify_anchors(self, dl):
        root = self.cfg["lane_disk_root"]
        fd = absolute_directory(root, dl)
        try:
            if stat_id(fd) != self.lane_id or stat_id(self.lane_fd) != self.lane_id:
                raise GuardError("LANE_ANCHOR_CHANGED")
        finally:
            os.close(fd)
        dl.check("after lane identity close")
        locations = [(r, fd, ident) for r, (fd, ident) in self.root_fds.items()] + [(self.cfg["env"]["TMPDIR"], self.tmp_fd, self.tmp_id)]
        for path, held, ident in locations:
            fd = directory_at(self.lane_fd, os.path.relpath(path, root), dl)
            try:
                if stat_id(fd) != ident or stat_id(held) != ident or ident[0] != self.lane_id[0]:
                    raise GuardError("CHARGED_ANCHOR_CHANGED " + path)
            finally:
                os.close(fd)
            dl.check("after charged anchor close")
        lane = absolute_directory(self.cfg["lane"], dl)
        try:
            if os.fstat(lane).st_dev != self.lane_id[0]:
                raise GuardError("LANE_CWD_DIFFERENT_VOLUME")
        finally:
            os.close(lane)
        for root in self.cfg["lane_roots"]:
            fd = absolute_directory(root, dl)
            os.close(fd)
            dl.check("after lane root close")

    def location(self, path):
        return self.root_fds[os.path.dirname(path)][0], os.path.basename(path)

    def free(self, dl):
        dl.check("before fstatvfs")
        self.last_native_free = os.fstatvfs(self.lane_fd)  # Native result retained before any completion clock.
        s = self.last_native_free
        value = s.f_bavail * s.f_frsize
        self.last_native_free = {"f_bavail": s.f_bavail, "f_frsize": s.f_frsize, "free": value}
        return value

    def accounting(self, dl, lane=True):
        if self.timing_failed:
            raise GuardError("TIMING_EVIDENCE_UNAVAILABLE_NO_ACCOUNTING_RETRY")
        start = {"mono_begin": None}
        begin = self.aux_clock(start, "mono_begin")
        if begin is None:
            raise GuardError("ACCOUNTING_BEGIN_UNAVAILABLE")
        self.verify_anchors(dl)
        seen = set()
        charge = sum(walk_fd(fd, self.lane_id[0], dl, seen) for fd, _ in self.root_fds.values())
        charge += walk_fd(self.tmp_fd, self.lane_id[0], dl, seen)
        total = walk_fd(self.lane_fd, self.lane_id[0], dl) if lane else self.lane_bytes
        free = self.free(dl)
        self.charged, self.lane_bytes = charge, total
        self.min_free = free if self.min_free is None else min(self.min_free, free)
        self.maxima["charged_bytes"] = max(charge, self.maxima["charged_bytes"])
        resources = {"charged_bytes": charge, "lane_bytes": total, "free": free}
        event = {"id": len(self.accounting_observations) + 1, "phase": self.phase, "inside_helper": self.in_helper,
                 "mono_begin": begin, "mono_observed": None, "resources": dict(resources),
                 "retained": False, "returned": False}
        self.last_accounting_observation = event
        if self.min_free_witness is None or free < self.min_free_witness["resources"]["free"]:
            self.min_free_witness = event
        self.aux_clock(event, "mono_observed")
        try:
            self.reserve_history("accounting_observation", event, [], event, extra=128)
            self.accounting_observations.append(event)
            event["retained"] = True
            dl.check("after accounting")
            if event["mono_observed"] is None:
                raise GuardError("ACCOUNTING_COMPLETION_TIME_UNAVAILABLE")
            event["returned"] = True
            return resources
        except BaseException:
            if self.history_halted and self.history_overflow is not None:
                self.history_overflow["completed_accounting_observation"] = event
            raise

    def reservation_fits(self, a, payload=0):
        adm = self.cfg["admission"]
        remaining = max(0, adm["reservation_bytes"] - a["charged_bytes"] - payload)
        return a["charged_bytes"] + payload <= adm["reservation_bytes"] and \
            a["free"] - payload - adm["outstanding_reservations_bytes"] - remaining >= self.cfg["free_trip_bytes"] and \
            a["lane_bytes"] + payload + adm["lane_outstanding_reservations_bytes"] + remaining <= self.cfg["lane_disk_ceiling_bytes"]

    def resource_age(self, c):
        if time.monotonic() - c["mono_complete"] > max(1.0, self.cfg["sample_s"]):
            raise GuardError("RESOURCE_CENSUS_STALE_AT_COMMIT")

    def limits(self, c, admission=False):
        busy = c["lane_busy"]
        if admission:
            if self.pid in c["lane_busy_pids"]:
                busy -= 1
            return busy + self.cfg["cpu_slots"] <= POLICY["busy"] and c["lane_rss"] + self.cfg["rss_projection_bytes"] <= self.cfg["rss_trip_bytes"]
        if c["lane_busy"] > self.cfg["busy_limit"]:
            self.trip("BUSY", {"count": c["lane_busy"], "pids": c["lane_busy_pids"]})
        if c["lane_rss"] > self.cfg["rss_trip_bytes"]:
            self.trip("RSS", c["lane_rss"])
        self.maxima["lane_busy"] = max(self.maxima["lane_busy"], c["lane_busy"])
        self.maxima["lane_rss"] = max(self.maxima["lane_rss"], c["lane_rss"])
        self.maxima["owned_live"] = max(self.maxima["owned_live"], len(c["owned_live"]))
        return True

    def disk_trips(self, a):
        if a["free"] < self.cfg["free_trip_bytes"]:
            self.trip("FREE", a["free"])
        if a["charged_bytes"] > self.cfg["output_trip_bytes"]:
            self.trip("OUTPUT", a["charged_bytes"])
        unused = max(0, self.cfg["admission"]["reservation_bytes"] - a["charged_bytes"])
        if a["lane_bytes"] + self.cfg["admission"]["lane_outstanding_reservations_bytes"] + unused > self.cfg["lane_disk_ceiling_bytes"]:
            self.trip("LANE_CEILING", a["lane_bytes"])
        if any(v["overflow"] for v in self.streams.values()):
            self.trip("STREAM_CAP", {k: [v["bytes_seen"], v["bytes_written"]] for k, v in self.streams.items()})

    def authorization_io(self, dl):
        adm = self.cfg["admission"]
        ga, gb = read_file(adm["go_path"], SMALL, dl, keep=True)
        sa, sb = read_file(adm["stability_receipt_path"], SMALL, dl, keep=True)
        go, sr = parse_json(gb), parse_json(sb)
        if not isinstance(go, dict) or go.get("decision") != "GO" or go.get("item") != self.cfg["item"]:
            raise GuardError("GO_NOT_FOR_ITEM")
        expected = {k: self.cfg[k] for k in BOUND_KEYS[:5]}
        expected.update({k: adm[k] for k in BOUND_KEYS[5:]})
        entries = go.get("configs")
        if not isinstance(entries, dict) or self.config_sha not in entries:
            raise GuardError("GO_DOES_NOT_NAME_THIS_CONFIG")
        if not typed_equal(entries, {self.config_sha: expected}):
            raise GuardError("GO_BINDING_MISMATCH")
        channel = self.cfg["creation_channel"]
        if channel:
            negative = go.get("qualification_negative")
            if not isinstance(negative, dict) or set(negative) != {"scenario", "kind", "creation_channel"} or \
                    negative["scenario"] != channel["scenario"] or negative["kind"] != "mutation" or negative["creation_channel"] is not True:
                raise GuardError("MUTATION_NEGATIVE_GO_NOT_EXPLICIT")
            pa, _ = read_file(channel["preparation_path"], SMALL, dl)
            if pa["sha256"] != channel["preparation_sha256"]:
                raise GuardError("CREATION_PREPARATION_BINDING_CHANGED")
        if not number(go.get("not_after_epoch")) or not hex64(go.get("stability_receipt_sha256")):
            raise GuardError("GO_FRESHNESS_FIELDS_INVALID")
        if go["stability_receipt_sha256"] != sa["sha256"] or not isinstance(sr, dict) or sr.get("verdict") != "PASS":
            raise GuardError("STABILITY_DIGEST_OR_VERDICT_MISMATCH")
        stability_epoch = parse_date_epoch(sr.get("now_date"))
        out = {"go_sha256": ga["sha256"], "stability_receipt_sha256": sa["sha256"],
               "not_after_epoch": go["not_after_epoch"], "stability_epoch": stability_epoch,
               "stability_date": sr["now_date"]}
        if self.authorization is not None and not typed_equal(self.authorization, out):
            raise GuardError("AUTHORIZATION_CHANGED")
        self.authorization = out
        dl.check("after authorization I/O")
        return out

    def stability_age(self, mono):
        if self.authorization is None or self.clock_observation is None or self.stability_expiry_mono is None:
            raise GuardError("STABILITY_AGE_UNVERIFIABLE")
        obs = self.clock_observation
        # Include whole-second resolution and elapsed time from BEFORE the actual reading/cleanup.
        base = obs["epoch_date_floor"] - self.authorization["stability_epoch"]
        if base < 0:
            raise GuardError("STABILITY_TIMESTAMP_IN_FUTURE")
        upper = max(base + 1.0 + max(0.0, mono - obs["mono_before_read"]),
                    self.cfg["admission"]["stability_max_age_s"] + mono - self.stability_expiry_mono)
        if upper > self.cfg["admission"]["stability_max_age_s"]:
            raise GuardError("STABILITY_STALE")
        return upper

    def creation_manifest(self, dl):
        """Only explicitly declared mutation negatives receive this fixed extra JSON line; ordinary GO stays exact."""
        channel = self.cfg["creation_channel"]
        if not channel:
            return b""
        pa, raw = read_file(channel["preparation_path"], SMALL, dl, keep=True)
        prep = parse_json(raw)
        required = {"kind", "scenario", "run", "output_root", "fixture", "source_pins", "python", "allocation", "negative_control"}
        if pa["sha256"] != channel["preparation_sha256"] or not isinstance(prep, dict) or set(prep) != required or \
                prep["kind"] != "qualification-creation-preparation-v1" or prep["scenario"] != channel["scenario"] or prep["negative_control"] is not True:
            raise GuardError("CREATION_PREPARATION_SCHEMA_OR_BINDING")
        pins = prep["source_pins"]
        if not isinstance(pins, dict) or set(pins) != {"supervisor", "child", "writer", "checker"} or any(
                not isinstance(v, dict) or set(v) != {"path", "sha256"} or not norm_abs(v["path"]) or not hex64(v["sha256"])
                for v in pins.values()) or not typed_equal(pins["supervisor"], {"path": SELF, "sha256": self.self_sha}):
            raise GuardError("CREATION_PREPARATION_SOURCE_PINS")
        expected_allocation = {"bytes": self.cfg["admission"]["reservation_bytes"], "cpu_slots": self.cfg["cpu_slots"],
                               "outstanding_reservations_bytes": self.cfg["admission"]["outstanding_reservations_bytes"],
                               "lane_outstanding_reservations_bytes": self.cfg["admission"]["lane_outstanding_reservations_bytes"]}
        if not typed_equal(prep["allocation"], expected_allocation) or not isinstance(prep["python"], dict) or set(prep["python"]) != {"path", "sha256"} or \
                prep["python"]["path"] != self.cfg["argv"][0] or not hex64(prep["python"]["sha256"]):
            raise GuardError("CREATION_PREPARATION_ALLOCATION_OR_INTERPRETER")
        out = self.cfg["output_roots"][0]
        run = os.path.dirname(out)
        rfd = directory_at(self.lane_fd, os.path.relpath(run, self.cfg["lane_disk_root"]), dl)
        try:
            if not typed_equal(prep["run"], {"path": run, "inode": list(stat_id(rfd))}) or \
                    not typed_equal(prep["output_root"], {"path": out, "inode": list(self.root_fds[out][1])}):
                raise GuardError("CREATION_RUN_ANCHOR_CHANGED")
            if channel["scenario"] == "mutate_pin":
                expected = prep["fixture"]
                if not isinstance(expected, dict) or set(expected) != {"path", "inode", "sha256", "bytes", "nlink"} or \
                        expected["path"] != channel["target_path"] or not integer(expected["nlink"]) or expected["nlink"] != 1 or \
                        not integer(expected["bytes"]) or expected["bytes"] < 1 or not hex64(expected["sha256"]) or \
                        not isinstance(expected["inode"], list) or len(expected["inode"]) != 2 or not all(integer(v) and v >= 0 for v in expected["inode"]):
                    raise GuardError("PIN_CREATION_MANIFEST_SCHEMA")
                actual, _ = read_file("pinned-scratch.txt", SMALL, dl, rfd)
            else:
                if prep["fixture"] is not None:
                    raise GuardError("LAUNCH_MUTATION_HAS_UNDECLARED_PIN_FIXTURE")
                target = self.cfg["launch_record"]
                expected = {"path": target, "inode": list(self.created[target]),
                            "sha256": self.rec["launch_record_sha256"], "bytes": None, "nlink": 1}
                fd, name = self.location(target)
                actual, _ = read_file(name, SMALL, dl, fd)
                expected["bytes"] = actual["bytes"]
            for k in ("inode", "sha256", "bytes", "nlink"):
                if actual[k] != expected[k]:
                    raise GuardError("ORIGINAL_CREATION_IDENTITY_CHANGED_BEFORE_GO")
            manifest = {"kind": "qualification-creation-manifest-v1", "scenario": channel["scenario"],
                        "preparation_sha256": pa["sha256"], "run": prep["run"], "output_root": prep["output_root"],
                        "target": expected}
            line = (json.dumps(manifest, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
            if len(line) > 4096:
                raise GuardError("CREATION_MANIFEST_BYTE_CAP")
            self.rec["go_creation_manifest"] = manifest
            self.rec["go_creation_manifest_sha256"] = hashlib.sha256(line).hexdigest()
            dl.check("after original-creation manifest")
            return line
        finally:
            os.close(rfd)
            dl.check("after creation manifest anchor close")

    def time_commit(self, phase, required_s=0):
        """Fresh raw clocks after LAST binding I/O, while cancellation is protected."""
        self.propagate_cancel_clock_error()
        if self.timing_failed:
            raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
        epoch, mono = time.time(), time.monotonic()
        if pending_cancel():
            raise GuardError("CANCEL_AT_" + phase)
        if self.authorization is None or epoch > self.authorization["not_after_epoch"]:
            raise GuardError("GO_EXPIRED_AT_" + phase)
        if epoch + required_s > self.fit_epoch or mono + required_s > self.fit_mono:
            raise GuardError("FIT_FAILED_AT_" + phase)
        age = None if phase == "HELPER" and self.clock_observation is None else self.stability_age(mono)
        return {"phase": phase, "mono": mono, "epoch": epoch, "required_s": required_s,
                "stability_age_upper_s": age}

    def completion_check(self, phase, dl):
        if self.timing_failed:
            raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
        if phase == "GO":
            observed = time.monotonic()
            age = observed - self.mono_spawn
            remaining = self.mono_spawn + self.cfg["max_wall_s"] - observed
            bound = min(60.0, self.cfg["max_wall_s"] / 2.0)
            self.rec["go_delivery_completion"] = {"mono": observed, "spawn_age_s": age,
                                                  "spawn_age_bound_s": bound, "remaining_main_runtime_s": remaining}
            late = age > bound or remaining <= 0
            if age > bound:
                self.fail("GO_COMPLETION_AGE_EXCEEDED", self.rec["go_delivery_completion"])
            if remaining <= 0:
                self.fail("GO_COMPLETION_MAIN_RUNTIME_EXPIRED", self.rec["go_delivery_completion"])
                self.enforce_runtime("actual_GO_completion")
            if late:
                raise GuardError("LATE_ACTUAL_GO_DELIVERY_OWNED_STOP")
        dl.check("after " + phase + " completion")
        if set(signal.sigpending()) & CANCEL_SIGNALS or (CANCEL["signal"] is not None and not self.cancel_handled):
            raise GuardError("CANCEL_DURING_" + phase + "_COMPLETION")
        epoch, mono = time.time(), time.monotonic()
        if self.authorization is None or epoch > self.authorization["not_after_epoch"]:
            raise GuardError("AUTHORIZATION_EXPIRED_DURING_" + phase)
        if epoch > self.fit_epoch or mono > self.fit_mono:
            raise GuardError("FIT_EXPIRED_DURING_" + phase)
        self.stability_age(mono)

    def sample(self, obj):
        if self.samples_dead or self.samples_fd is None:
            return
        data = bytes_json(obj)
        if self.sample_bytes + len(data) > self.cfg["samples_cap_bytes"]:
            self.samples_dead = True
            self.fail("SAMPLES_CAP")
            return
        try:
            write_all(self.samples_fd, data, self.deadline(10))
            self.sample_hash.update(data)
            self.sample_count += 1
            self.sample_bytes += len(data)
        except OSError as e:
            self.samples_dead = True
            self.fail("SAMPLES_WRITE_FAILED", e)

    def cheap_clear(self):
        return self.rc is not None and len(self.streams) == 2 and all(v["closed"] and v["error"] is None for v in self.streams.values()) and len(self.threads) == 2 and all(not t.is_alive() for t in self.threads) and all(h["settled"] for h in self.helpers)

    def clearance(self):
        self.reap()
        if not self.cheap_clear():
            return False
        c = self.full_census(self.deadline(CENSUS_S))
        self.limits(c)
        if not c["complete"] or c["owned_live"] or c["unproved_live"] or c["group_live"] or not self.cheap_clear():
            return False
        # ALL predicates have now been verified. Do not use the earlier census timestamp as clearance time.
        now = time.monotonic()
        for name, cut in self.cutoffs():
            if now > cut:
                self.fail(name, "all-clear verified after cutoff")
                self.loop_status = name
                return True
        self.clear = {"mono_all_predicates_verified": now, "census": c}
        self.loop_status = "EXITED"
        return True


def sink(sup, name, pipe):
    path, cap = sup.cfg[name], sup.cfg[name + "_cap_bytes"]
    fd, base = sup.location(path)
    out, ident = create_file(fd, base)
    sup.capture_fds[name] = out  # Own the native descriptor before any auxiliary timestamp.
    sup.created[path] = ident
    rec = {"bytes_seen": 0, "bytes_written": 0, "cap_bytes": cap, "overflow": False,
           "write_inflight": False, "pending_bytes": 0, "closed": False, "error": None,
           "sha256_prefix": hashlib.sha256().hexdigest(), "prefix_bytes": 0, "hash_pending": False, "sha256_written": None,
           "mono_created": None, "mono_last_update": None, "mono_last_read": None,
           "mono_last_write": None, "mono_eof": None, "mono_close_completed": None,
           "eof_seen": False, "fsync_returned": False, "out_closed": False, "pipe_closed": False}
    sup.streams[name] = rec
    created = sup.aux_clock(rec, "mono_created", sink=True)
    rec["mono_last_update"] = created
    if created is None:
        rec["error"] = "TIMING_EVIDENCE_UNAVAILABLE"

    def run():
        h = hashlib.sha256()
        def written(part):
            pending = rec["pending_bytes"] - len(part)
            count = rec["bytes_written"] + len(part)
            rec.update(bytes_written=count, pending_bytes=pending, write_inflight=pending > 0, hash_pending=True)
            h.update(part)
            rec.update(sha256_prefix=h.hexdigest(), prefix_bytes=count, hash_pending=False)
            completed = sup.aux_clock(rec, "mono_last_write", sink=True)
            rec["mono_last_update"] = completed
            if completed is None:
                raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
        try:
            if rec["error"] is not None:
                raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
            while True:
                chunk = pipe.read1(65536)
                if not chunk:
                    rec["eof_seen"] = True  # Native EOF is retained before its clock.
                    rec["mono_last_update"] = sup.aux_clock(rec, "mono_eof", sink=True)
                    if rec["mono_eof"] is None:
                        raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
                    break
                total = rec["bytes_seen"] + len(chunk)
                room = max(0, cap - rec["bytes_written"])
                kept = chunk[:room]
                rec.update(bytes_seen=total, overflow=total > cap, write_inflight=bool(kept),
                           pending_bytes=len(kept))  # Returned read bytes are latched before timing.
                rec["mono_last_update"] = sup.aux_clock(rec, "mono_last_read", sink=True)
                if rec["mono_last_read"] is None:
                    raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
                if kept:
                    write_all(out, kept, sup.deadline(IO_S), on_progress=written)
        except BaseException as e:
            rec.update(error=repr(e), write_inflight=False)
        finally:
            errors = []
            try:
                dl = sup.deadline(IO_S)
            except BaseException as e:
                dl = None
                errors.append(type(e).__name__)
            for label, action in (("fsync", lambda: os.fsync(out)), ("close", lambda: os.close(out)), ("pipe_close", pipe.close)):
                try:
                    action()
                    if label == "fsync":
                        rec["fsync_returned"] = True
                    elif label == "close":
                        rec["out_closed"], sup.capture_fds[name] = True, None
                    else:
                        rec["pipe_closed"] = True
                    if dl is not None:
                        dl.check("sink " + label)
                except BaseException as e:
                    errors.append(repr(e))
            error = (rec["error"] or "") + ";".join(errors) if errors else rec["error"]
            digest = h.hexdigest()
            rec.update(error=error, sha256_prefix=digest, sha256_written=digest, write_inflight=False, closed=False)
            completed = sup.aux_clock(rec, "mono_close_completed", sink=True)
            rec["mono_last_update"] = completed
            if completed is None:
                rec["error"] = (rec["error"] or "") + ";TIMING_EVIDENCE_UNAVAILABLE"
            rec["closed"] = rec["error"] is None and rec["eof_seen"] and rec["out_closed"] and rec["pipe_closed"]
    with protected():
        t = threading.Thread(target=run, name="capture-" + name, daemon=True)
        t.start()
    return t


def admission(s):
    dl = Deadline(90, s.fit_mono)
    reasons, rec = [], {}
    try:
        s.verify_anchors(dl)
        for root, (fd, ident) in s.root_fds.items():
            if list_directory(fd, dl):
                raise GuardError("OUTPUT_ROOT_NOT_EMPTY " + root)
        for pin in s.cfg["pins"]:
            if read_file(pin["path"], PIN_CAP, dl)[0]["sha256"] != pin["sha256"]:
                raise GuardError("PIN_MISMATCH " + pin["path"])
        rec["authorization"] = s.authorization_io(dl)
        rec["date"] = s.date_now("admission")
        if rec["date"] is None:
            raise GuardError("DATE_HELPER_UNAVAILABLE")
        a = s.accounting(dl)
        rec["resources"] = a
        rec["accounting_ref"] = s.last_accounting_observation["id"]
        res = s.cfg["admission"]["reservation_bytes"]
        if a["free"] < s.cfg["launch_free_min_bytes"] + res or a["free"] - res - s.cfg["admission"]["outstanding_reservations_bytes"] < POLICY["free"]:
            raise GuardError("LAUNCH_FREE_FAILED")
        if a["lane_bytes"] + res + s.cfg["admission"]["lane_outstanding_reservations_bytes"] > s.cfg["lane_disk_ceiling_bytes"]:
            raise GuardError("LANE_CEILING_AT_ADMISSION")
        rec["censuses"] = []
        for n in range(2):
            c = s.full_census(dl)
            rec["censuses"].append(c)
            if not c["complete"] or c["owned_live"] or c["unproved_live"] or not s.limits(c, True) or s.failures:
                raise GuardError("ADMISSION_CENSUS_INCOMPLETE_OWNERSHIP_OR_LIMITS")
            if n == 0:
                time.sleep(2)
        dl.check("after admission")
        with protected():
            rec["checked"] = s.time_commit("ADMISSION", s.cfg["max_wall_s"] + s.cfg["settle_s"] + FINALIZE_S)
    except (OSError, ValueError, TypeError, KeyError) as e:
        reasons.append(str(e))
        if CANCEL["signal"] is not None:
            s.cancel_handled = True
    rec["reasons"] = reasons
    return rec


def install_main_identity(s, p):
    s.rec["main_initial_identity_observed"] = dict(p)
    if p["pgid"] != s.pid or p["euid"] != MY_UID or p["ruid"] != MY_UID:
        raise GuardError("CHILD_IDENTITY_OR_GROUP_INVALID")
    s.ident, s.group = p, p["pgid"]  # Mandatory cleanup state precedes ALL auxiliary end timing/history.


def recover_registered_main(s, error):
    record = s.child
    if record is None:
        record = next((r for r in s.keep if r["role"] == "child" and r.get("pid") is not None), None)
    if record is None:
        return False
    s.child, s.pid = record, record["pid"]
    if s.mono_spawn is None:
        s.mono_spawn, s.epoch_spawn = record.get("mono_spawn"), record.get("epoch_spawn")
    s.rec["main_recovery"] = {"pid": record["pid"], "error": repr(error), "identity_error": None}
    try:
        if s.ident is None and not record["leader_reaped"]:
            raw = s.acquire_identity(s.pid, "main_recovery", lambda p: install_main_identity(s, p))
            s.rec["main_initial_identity_interval"] = [raw["mono_begin"], raw["mono_end"]]
            s.rec["mono_main_initial_identity_observed"] = raw["mono_end"]
            s.rec["main_initial_identity_event_ref"] = s.retain_acquisition(raw, True)
            s.register_owned(s.ident, "child")
    except BaseException as identity_error:
        s.rec["main_recovery"]["identity_error"] = repr(identity_error)
    try:
        s.fail("POST_SPAWN_FAILURE", repr(error))
    finally:
        s.close_record_endpoints(record, readers=True)
        s.reap()  # Retain the original pre/post native-wait runtime enforcement, including a late successful reap.
    return True


def launch_and_go(s):
    s.phase = "PRE_GO"
    s.rec["start_date"] = s.date_now("start")
    if s.rec["start_date"] is None or s.failures:
        raise GuardError("START_DATE_UNAVAILABLE")
    dl = s.deadline(IO_S)
    fd, base = s.location(s.cfg["samples"])
    s.samples_fd, ident = create_file(fd, base)
    s.created[s.cfg["samples"]] = ident
    s.authorization_io(dl)
    c = s.full_census(dl)
    s.rec["launch_census"] = c
    if not c["complete"] or c["owned_live"] or c["unproved_live"] or not s.limits(c, True) or s.failures:
        raise GuardError("LAUNCH_CENSUS_INCOMPLETE_OWNERSHIP_OR_LIMITS")
    a = s.accounting(dl)
    s.rec["launch_resources"], s.rec["launch_accounting_ref"] = a, s.last_accounting_observation["id"]
    if a["free"] < s.cfg["launch_free_min_bytes"] + s.cfg["admission"]["reservation_bytes"] or not s.reservation_fits(a):
        raise GuardError("LAUNCH_RESOURCES_FAILED")
    s.resource_age(c)
    dl.check("after launch preparation")
    try:
        child = spawn_registered(s, s.cfg["argv"], dict(s.cfg["env"]), "child", dl,
                                 s.cfg["max_wall_s"] + s.cfg["settle_s"] + FINALIZE_S)
    except BaseException as e:
        if not recover_registered_main(s, e):
            raise
        s.phase = "RUNNING"
        observe(s)
        return
    s.rec["launch_commit"] = child["launch_commit"]
    try:
        raw = s.acquire_identity(s.pid, "main_initial", lambda p: install_main_identity(s, p))
        s.rec["mono_main_initial_identity_observed"] = raw["mono_end"]
        s.rec["main_initial_identity_interval"] = [raw["mono_begin"], raw["mono_end"]]
        s.rec["main_initial_identity_event_ref"] = s.retain_acquisition(raw, True)
        s.register_owned(s.ident, "child")
        if child["spawn_error"] is not None:
            raise GuardError(child["spawn_error"])
        for name in ("stdout", "stderr"):
            pipe = os.fdopen(child[name + "_fd"], "rb", buffering=65536)
            child[name + "_fd"] = None
            child[name] = pipe
            s.threads.append(sink(s, name, pipe))
        if CANCEL["signal"] is not None:
            s.cancel_handled = True
            s.trip("SUPERVISOR_CANCEL", CANCEL["signal"])
        launch = {"supervisor": VERSION, "supervisor_sha256": s.self_sha, "config_sha256": s.config_sha,
                  "supervisor_pid": MY_PID, "identity": s.ident, "argv": s.cfg["argv"], "cwd": s.cfg["lane"],
                  "env": s.cfg["env"], "mono_spawn": s.mono_spawn, "epoch_spawn": s.epoch_spawn,
                  "start_date": s.rec["start_date"], "baseline_count": len(s.baseline),
                  "authorization": s.authorization, "launch_commit": s.rec["launch_commit"],
                  "cpu_slots": s.cfg["cpu_slots"], "reservation_bytes": s.cfg["admission"]["reservation_bytes"]}
        fd, name = s.location(s.cfg["launch_record"])
        launch_sha, launch_inode = publish(fd, name, bytes_json(launch), s.deadline(IO_S))
        s.rec["launch_record_sha256"] = launch_sha
        s.created[s.cfg["launch_record"]] = launch_inode
        gd = s.deadline(IO_S)
        c = s.full_census(gd)
        s.rec["pre_go_census"] = c
        live = [p["uniqueid"] for p in c["owned_live"]]
        if not c["complete"] or c["unproved_live"] or live != [s.ident["uniqueid"]] or not s.limits(c, True):
            raise GuardError("GO_CENSUS_INCOMPLETE_OWNERSHIP_OR_LIMITS")
        a = s.accounting(gd)
        s.rec["pre_go_resources"], s.rec["pre_go_accounting_ref"] = a, s.last_accounting_observation["id"]
        if a["free"] < s.cfg["launch_free_min_bytes"] + s.cfg["admission"]["reservation_bytes"] or not s.reservation_fits(a):
            raise GuardError("GO_RESOURCES_FAILED")
        gd.check("after GO preparation")
        with protected():
            creation_line = s.creation_manifest(gd)
            s.authorization_io(gd)  # Last I/O, after census/accounting, before commit clocks.
            gd.check("after GO authorization read")
            s.resource_age(c)
            remaining = max(0, s.mono_spawn + s.cfg["max_wall_s"] - time.monotonic())
            spawn_age = time.monotonic() - s.mono_spawn
            if spawn_age > min(60.0, s.cfg["max_wall_s"] / 2.0):
                raise GuardError("SPAWN_TO_GO_AGE_EXCEEDED")
            if remaining <= 0 or s.stop is not None or s.failures:
                raise GuardError("GO_STOP_OR_DEADLINE")
            s.rec["go_commit"] = s.time_commit("GO", remaining + s.cfg["settle_s"] + FINALIZE_S)
            s.rec["go_write_attempted"] = True
            write_all(child["stdin_fd"], b"GO\n", gd)
            if creation_line:
                write_all(child["stdin_fd"], creation_line, gd)
            s.rec["go_written_mono"] = time.monotonic()
            os.close(child["stdin_fd"])
            child["stdin_fd"] = None
            s.rec["go_delivered"] = True  # Bytes were delivered; a later completion failure is not hidden.
            s.completion_check("GO", gd)
            s.resource_age(c)
    except BaseException as e:
        s.fail("POST_SPAWN_FAILURE", repr(e))
    finally:
        if child.get("stdin_fd") is not None:
            try:
                os.close(child["stdin_fd"])
                child["stdin_fd"] = None
            except OSError as e:
                s.fail("STDIN_CLOSE_FAILED", repr(e))
    if not s.rec.get("go_delivered"):
        s.fail("GO_NOT_DELIVERED")
    s.phase = "RUNNING"
    observe(s)


def observe(s):
    s.loop_status = "RUNNING"
    while True:
        if s.timing_failed:
            if s.child is not None:
                s.close_record_endpoints(s.child)
                s.reap_record(s.child, main=True)
            return
        try:
            s.reap()
            if s.timing_failed:
                return
            if CANCEL["signal"] is not None:
                s.cancel_handled = True
                s.trip("SUPERVISOR_CANCEL", CANCEL["signal"])
            for name, cut in s.cutoffs():
                if time.monotonic() > cut:
                    s.fail(name)
                    s.loop_status = name
                    return
            dl = s.deadline(IO_S)
            c = s.census(dl)
            s.limits(c)
            a = s.accounting(dl)
            s.disk_trips(a)
            for name, v in s.streams.items():
                if v["error"] is not None:
                    s.fail("STREAM_ERROR_" + name, v["error"])
            s.reap()
            if s.rc is None and time.monotonic() >= s.mono_spawn + s.cfg["max_wall_s"]:
                s.trip("DEADLINE")
            stream_sample = {k: dict(v) for k, v in s.streams.items()}
            s.sample({"mono": time.monotonic(), "epoch": time.time(), "rc": s.rc, "census": c,
                      "resources": a, "accounting_ref": s.last_accounting_observation["id"], "streams": stream_sample,
                      "stop": None if s.stop is None else s.stop["reason"], "failure_codes": sorted(s.failure_keys),
                      "trips": list(s.trips)})
            if s.clearance():
                return
        except BaseException as e:
            s.fail("OBSERVATION_FAILED", repr(e))
            if not s.timing_failed:
                s.enforce_runtime("observation_exception_after_native_return")
        if s.timing_failed:
            return
        for name, cut in s.cutoffs():
            if time.monotonic() > cut:
                s.fail(name)
                s.loop_status = name
                return
        remaining = [cut - time.monotonic() for _, cut in s.cutoffs()]
        time.sleep(max(0, min([s.cfg["sample_s"]] + remaining)))


def exception_code(e):
    if isinstance(e, GuardError) and e.args and isinstance(e.args[0], str):
        return e.args[0].split(" ", 1)[0]
    if isinstance(e, OSError):
        return "OS_ERROR_%s" % e.errno
    return type(e).__name__


def refuse(s, code, reason, extra=None):
    fields = dict(extra or {})
    fields["reconciliation"] = s.reconciliation_evidence()
    return unsuccessful(code, reason, fields)


def unsuccessful(code, reason, extra=None):
    obj = {"supervisor": VERSION, "acknowledged": False, "exit_code": code, "reason": reason,
           "clock_note": "raw monotonic/epoch telemetry only"}
    if extra:
        obj.update(extra)
    sys.stdout.write(json.dumps(obj, allow_nan=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()
    return code


def finalize(s):
    try:
        s.propagate_cancel_clock_error()
        if s.timing_failed:
            if s.child is not None and not s.child["leader_reaped"] and s.stop is None:
                s.request_stop("FAILURE")  # Still requires the unchanged fresh deadline and full fingerprint checks.
            for record in s.keep:
                if record.get("pid") is None:
                    continue
                if record["role"] == "helper":
                    s.helper_clockless_once(record)
                else:
                    s.close_record_endpoints(record, readers=True)
                    s.reap_record(record, main=True)
            return refuse(s, 13, "TIMING_EVIDENCE_UNAVAILABLE", {"config_sha256": s.config_sha})
        phase = Deadline(FINALIZE_S, s.fit_mono)
        return final_body(s, phase)
    except BaseException as e:
        if s.ack_output_started:
            return 14  # A begun ACK never falls back to a second stdout summary, even if stderr reporting failed.
        diagnostic_error = None
        try:
            sys.stderr.write("FINALIZATION_FAILED %r\n" % e)
        except BaseException as diagnostic:
            diagnostic_error = type(diagnostic).__name__
        return refuse(s, 13, "FINALIZATION_FAILED", {"config_sha256": s.config_sha, "error": repr(e),
                                                    "error_code": exception_code(e), "diagnostic_error": diagnostic_error})


def final_body(s, phase):
    s.phase = "FINAL"
    s.rec["end_date"] = s.date_now("end")
    s.refresh_helpers(Deadline(CENSUS_S, phase.end))
    s.reap()
    c = s.full_census(Deadline(CENSUS_S, phase.end))
    s.rec["final_census"] = c
    if not c["complete"]:
        s.fail("FINAL_CENSUS_INCOMPLETE", c["incomplete"])
    if c["owned_live"]:
        s.fail("OWNED_LIVE", c["owned_live"])
    if c["unproved_live"]:
        s.fail("UNPROVED_LIVE", c["unproved_live"])
    if s.pid is not None:
        if s.rc is None:
            s.fail("CHILD_NOT_REAPED")
        s.limits(c)
        if not s.cheap_clear():
            s.fail("STREAMS_OR_THREADS_NOT_CLOSED")
        if s.clear is None and not c["owned_live"] and not c["unproved_live"] and s.cheap_clear():
            # Finalization cannot retroactively replace a missing timely clearance observation.
            s.fail("TIMELY_CLEARANCE_NOT_ESTABLISHED")
    if s.samples_fd is not None:
        dl = Deadline(IO_S, phase.end)
        try:
            os.fsync(s.samples_fd)
            dl.check("after samples fsync")
        finally:
            os.close(s.samples_fd)
            s.samples_fd = None
        dl.check("after samples close")
    dl = Deadline(60, phase.end)
    pin_end = []
    for pin in s.cfg["pins"]:
        try:
            ok = read_file(pin["path"], PIN_CAP, dl)[0]["sha256"] == pin["sha256"]
        except OSError:
            ok = False
        pin_end.append([pin["path"], ok])
    if not all(x[1] for x in pin_end):
        s.fail("PIN_CHANGED_OR_UNREADABLE")
    s.verify_anchors(dl)
    inventory = {}
    for root, (fd, ident) in s.root_fds.items():
        names = list_directory(fd, dl)
        inventory[root] = names
        stray = sorted(set(names) - s.allow[root])
        if stray:
            s.fail("UNDECLARED_ENTRIES", [root, stray])
    stream_snapshot = {k: dict(v) for k, v in s.streams.items()}
    stream_snapshot_mono = time.monotonic()
    arts, expected = {}, {}
    paths = [s.cfg[k] for k in ("stdout", "stderr", "samples", "launch_record")] + [o["path"] for o in s.cfg["outputs"]]
    for path in paths:
        fd, name = s.location(path)
        try:
            a, _ = read_file(name, max(s.cfg["output_trip_bytes"], s.cfg["samples_cap_bytes"]), dl, fd)
            arts[path] = a
            if a["nlink"] != 1 or (path in s.created and tuple(a["inode"]) != s.created[path]):
                s.fail("ARTIFACT_IDENTITY_CHANGED", path)
            if path not in s.created and s.epoch_spawn is not None and a["birth_epoch"] < s.epoch_spawn:
                s.fail("CHILD_OUTPUT_PREDATES_SPAWN", path)
        except FileNotFoundError:
            arts[path] = None
        except OSError as e:
            arts[path] = {"error": repr(e)}
            s.fail("ARTIFACT_UNREADABLE", path)
    if s.rec.get("launch_record_sha256"):
        expected[s.cfg["launch_record"]] = s.rec["launch_record_sha256"]
    if s.pid is not None:
        expected[s.cfg["samples"]] = s.sample_hash.hexdigest()
    for k in ("stdout", "stderr"):
        if stream_snapshot.get(k, {}).get("sha256_written") is not None:
            expected[s.cfg[k]] = stream_snapshot[k]["sha256_written"]
    for p, h in expected.items():
        if not isinstance(arts.get(p), dict) or arts[p].get("sha256") != h:
            s.fail("EVIDENCE_MUTATED", p)
    if s.pid is not None:
        for o in s.cfg["outputs"]:
            if o["required"] and arts[o["path"]] is None:
                s.fail("REQUIRED_OUTPUT_MISSING", o["path"])
        for p in [s.cfg[k] for k in ("stdout", "stderr", "samples", "launch_record")]:
            if arts.get(p) is None:
                s.fail("EVIDENCE_MISSING", p)
    a = s.accounting(dl)
    s.disk_trips(a)
    phase.check("before final payload decision")
    s.propagate_cancel_clock_error()
    unresolved = any(not h["settled"] for h in s.helpers) or not c["complete"] or bool(c["owned_live"] or c["unproved_live"])
    state = "UNSETTLED" if unresolved else "NOT_LAUNCHED" if s.pid is None else "UNSETTLED" if s.failures else "SETTLED"
    code = {"SETTLED": 0, "NOT_LAUNCHED": 10, "UNSETTLED": 11}[state]
    frozen_failure_codes, frozen_trip_codes = tuple(sorted(s.failure_keys)), tuple(s.trips)
    s.rec.update(settlement=state, child_pid=s.pid, child_identity=s.ident, child_returncode=s.rc,
                 child_exit_mono=s.exit_mono, child_exit_epoch=s.exit_epoch, wait_status_lost=s.lost_wait,
                 timing_failed=s.timing_failed, raw_acquisitions=list(s.raw_acquisitions.values()),
                 last_native_free=s.last_native_free,
                 main_wait=None if s.child is None else {k: s.child.get(k) for k in
                     ("pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "mono_reaped", "epoch_reaped")},
                 failures=s.failures, trips=list(s.trips.values()), stop_request=s.stop, signal=s.signal,
                 owned_identities=list(s.owned.values()), contract_violations=s.violations, clear=s.clear,
                 unproved_history=list(s.unproved_history.values()), coverage_history=list(s.coverage_history),
                 census_observations=list(s.census_history), runtime_observations=s.runtime_observations,
                 identity_history=list(s.identity_history.values()), observation_attempts=list(s.attempt_history),
                 identity_events=list(s.identity_events), accounting_observations=list(s.accounting_observations),
                 min_free_witness=s.min_free_witness, authorization=s.authorization,
                 history_charge_bytes=s.history_charge, history_overflow=s.history_overflow,
                 stability_expiry_mono=s.stability_expiry_mono,
                 clock_observation=s.clock_observation,
                 helper_calls=s.helper_calls, helper_log=s.helper_log, helpers=s.helper_reports(),
                 streams=stream_snapshot, loop_status=s.loop_status, samples_written=s.sample_count,
                 samples_bytes=s.sample_bytes, maxima=s.maxima, min_free=s.min_free, artifacts=arts,
                 evidence_expected_sha256=expected, pins_at_end=pin_end, output_root_inventory=inventory,
                 publication_precheck=a, publication_precheck_ref=s.last_accounting_observation["id"],
                 stream_snapshot_mono=stream_snapshot_mono, reservation_bytes=s.cfg["admission"]["reservation_bytes"],
                 mono_decision=time.monotonic(), epoch_decision=time.time(), cancel=dict(CANCEL))
    # Serialize ONCE. No budget fields or failures are appended after these exact buffers have been budgeted.
    rb = bytes_json(s.rec)
    rsha = hashlib.sha256(rb).hexdigest()
    sb = bytes_json({"supervisor": VERSION, "config_sha256": s.config_sha, "settlement": state,
                    "receipt": s.cfg["receipt"], "receipt_sha256": rsha, "child_returncode": s.rc,
                    "failure_codes": sorted(s.failure_keys), "trips": list(s.trips),
                    "authority": "only independent parent commit releases reservations"})
    payload = len(rb) + len(sb)
    s.publication_payload_bytes = payload
    b = s.accounting(Deadline(IO_S, phase.end))
    s.publication_resources = b
    adm = s.cfg["admission"]
    fits = payload <= PUBLICATION_CAP and s.reservation_fits(b, payload) and \
        b["charged_bytes"] + payload <= s.cfg["output_trip_bytes"]
    if not fits:
        return refuse(s, 12, "PUBLICATION_REFUSED", {"config_sha256": s.config_sha, "payload_bytes": payload,
                                                         "resources": b, "reservation_bytes": adm["reservation_bytes"]})
    pub = Deadline(60, phase.end)
    fd, name = s.location(s.cfg["receipt"])
    try:
        got, receipt_inode = publish(fd, name, rb, pub)
        if got != rsha:
            raise GuardError("RECEIPT_DIGEST_MISMATCH")
    except OSError as e:
        return refuse(s, 12, "RECEIPT_PUBLICATION_FAILED", {"error": repr(e), "error_code": exception_code(e)})
    fd, name = s.location(s.cfg["settlement_record"])
    try:
        ssha = linked_publication(fd, name, sb, pub)
        for root, (fd, ident) in s.root_fds.items():
            os.fsync(fd)
            pub.check("after directory fsync")
    except OSError as e:
        return refuse(s, 13, "SETTLEMENT_OR_DIRECTORY_SYNC_FAILED", {"receipt_sha256": rsha, "error": repr(e), "error_code": exception_code(e)})
    post_publish = time.monotonic()
    # I/O FIRST, fresh raw-clock/cancel checks LAST at the protected acknowledgment commit.
    try:
        end = s.accounting(Deadline(IO_S, phase.end))
        s.ack_resources = end
        if not s.reservation_fits(end) or end["charged_bytes"] > s.cfg["output_trip_bytes"]:
            raise GuardError("ACK_RESOURCE_OR_AGGREGATE_OUTPUT_FAILED")
        ack_census = s.full_census(Deadline(CENSUS_S, phase.end))
        final_ids = {p["uniqueid"] for p in c["owned_live"] + c["unproved_live"]}
        ack_ids = {p["uniqueid"] for p in ack_census["owned_live"] + ack_census["unproved_live"]}
        if not ack_census["complete"] or not ack_ids <= final_ids or (state != "UNSETTLED" and ack_ids):
            raise GuardError("ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING")
        if tuple(sorted(s.failure_keys)) != frozen_failure_codes or tuple(s.trips) != frozen_trip_codes:
            raise GuardError("ACK_OBSERVATION_CHANGED_FROZEN_OUTCOME")
        phase.check("after acknowledgment preparation")
        with protected():
            s.authorization_io(phase)  # Last binding read after ALL preparation I/O.
            s.resource_age(ack_census)
            s.propagate_cancel_clock_error()
            if s.timing_failed:
                raise GuardError("TIMING_EVIDENCE_UNAVAILABLE")
            # A cancel already acted on as the cause of this result does not masquerade as an unobserved late cancel.
            if s.cancel_handled and CANCEL["signal"] is not None and not (set(signal.sigpending()) & CANCEL_SIGNALS):
                epoch, mono = time.time(), time.monotonic()
                if epoch > s.authorization["not_after_epoch"] or epoch > s.fit_epoch or mono > s.fit_mono:
                    raise GuardError("ACK_EXPIRY_OR_FIT")
                age = s.stability_age(mono)
                commit = {"phase": "ACK", "epoch": epoch, "mono": mono, "cancel_handled": True,
                          "stability_age_upper_s": age}
            else:
                commit = s.time_commit("ACK")
            phase.check("acknowledgment commit")
            ack = {"supervisor": VERSION, "acknowledged": True, "exit_code": code, "settlement": state,
                   "config_sha256": s.config_sha, "receipt_sha256": rsha, "settlement_record_sha256": ssha,
                   "receipt_bytes": len(rb), "settlement_bytes": len(sb), "post_publish_mono": post_publish,
                   "ack_commit": commit, "publication_resources": b, "ack_resources": end,
                   "publication_payload_bytes": payload,
                   "child_returncode": s.rc, "failure_codes": sorted(s.failure_keys),
                   "owned_live": ack_census["owned_live"], "unproved_live": ack_census["unproved_live"],
                   "ack_census": ack_census, "contract_violations": s.violations,
                   "unproved_history": list(s.unproved_history.values()), "coverage_history": s.coverage_history,
                   "census_observations": s.census_history, "reconciliation": s.reconciliation_evidence()}
            ack_line = json.dumps(ack, sort_keys=True, allow_nan=False, separators=(",", ":")) + "\n"
            s.ack_output_started = True
            sys.stdout.write(ack_line)
            sys.stdout.flush()
            s.completion_check("ACK", phase)
            s.resource_age(ack_census)
        return code
    except BaseException as e:
        # If stdout already committed a line, do not emit a contradictory second line: mismatch exit refuses release.
        if s.ack_output_started:
            try:
                sys.stderr.write(json.dumps({"kind": "POST_ACK_REFUSAL_EVIDENCE", "exit_code": 14,
                                             "error": repr(e), "error_code": exception_code(e),
                                             "reconciliation": s.reconciliation_evidence()},
                                            allow_nan=False, separators=(",", ":")) + "\n")
                sys.stderr.flush()
            except BaseException:
                pass  # Missing/incomplete refusal capture is never release authority; preserve actual14 and one stdout line.
            return 14
        return refuse(s, 14, "ACK_REFUSED", {"receipt_sha256": rsha, "settlement_record_sha256": ssha,
                                           "post_publish_mono": post_publish,
                                           "publication_resources": s.publication_resources, "ack_resources": s.ack_resources,
                                           "publication_payload_bytes": s.publication_payload_bytes,
                                           "error": repr(e), "error_code": exception_code(e)})


def main():
    for sig in CANCEL_SIGNALS:
        signal.signal(sig, cancel)
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_UNBLOCK, CANCEL_SIGNALS)
    if len(sys.argv) != 2:
        sys.stderr.write("usage: owned_supervisor_v18.py CONFIG.json\n")
        return 2
    s = None
    try:
        path = os.path.abspath(sys.argv[1])
        a, raw = read_file(path, SMALL, Deadline(IO_S), keep=True)
        cfg = parse_json(raw)
        validate(cfg)
        s = Supervisor(cfg, path, a["sha256"])
        s.open_anchors()
        if os.path.realpath(os.getcwd()) != cfg["lane"]:
            raise GuardError("SUPERVISOR_CWD_MUST_EQUAL_LANE")
        s.establish_baseline()
    except BaseException as e:
        sys.stderr.write("CONFIG_OR_ANCHORS_UNUSABLE %r\n" % e)
        if s is not None:
            return refuse(s, 2, "CONFIG_OR_ANCHORS_UNUSABLE", {"error": repr(e), "error_code": exception_code(e)})
        return 2
    s.rec["admission"] = admission(s)
    if not s.rec["admission"]["reasons"]:
        try:
            launch_and_go(s)
        except BaseException as e:
            if s.pid is None and not recover_registered_main(s, e):
                s.rec["launch_refusal"] = repr(e)
                if CANCEL["signal"] is not None:
                    s.cancel_handled = True
            else:
                if s.ident is None:
                    recover_registered_main(s, e)
                s.fail("LAUNCH_OR_OBSERVE_EXCEPTION", repr(e))
                try:
                    observe(s)
                except BaseException as e2:
                    s.fail("EXCEPTION_OBSERVATION_FAILED", repr(e2))
    return finalize(s)


if __name__ == "__main__":
    status = main()  # All existing bounded cleanup, publication and diagnostic attempts run before selecting this status.
    if status == 14:
        os._exit(14)  # Do not reflush failed buffered streams at CPython shutdown; missing evidence still holds allocations.
    sys.exit(status)
