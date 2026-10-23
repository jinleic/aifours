#!/usr/bin/env python3
"""owned_supervisor_v10 -- ONE separately reviewed SINGLE-PROCESS child, standard library only.

Binding scope: RUN/review/rqls10-supervisor-v10-scope-parent-decision-v1.json
sha256 e441d8585228c2976700cba2c3397acfa1e544bc3dfe7af919205581572af22b.
This replaces v9's generic ancestry/helper contract. No helper, forked worker or automatic next launch is supported.
The child must not fork, exec, spawn subprocesses or use multiprocessing; native threads are permitted. The Python
framework launcher must not be used as argv[0]; use its actual Python.app executable, which does not re-exec.

OWNERSHIP: retain the child and every identity ever observed in its process group or with an observed owned current
parent. Any identity other than the child is a latched SINGLE_PROCESS_CONTRACT_VIOLATION. It remains in the receipt's
owned registry, and parent release remains blocked until each such identity is independently verified ended. Current
parent links are bracketed by full identity reads. Unlinked same-uid processes are NOT blocking. Residual: a violating
child can fork+setsid+lose its intermediate parent before sampling, evading ownership detection. Child source review is
the mitigation, not speculative genealogy. This is not an OS sandbox or a universal malicious-program guard.

CLOCKS: NO human-readable timestamp is written, no /bin/date helper is spawned. mono_* and epoch_* are explicitly
labelled raw time.monotonic/time.time telemetry. The parent alone writes /bin/date timestamps in GO/audit/release.
The per-invocation GO carries a raw not_after_epoch and stability_receipt_sha256. Its exact bytes and the stability
receipt are re-read/bound at launch, GO and acknowledgment preparation; expiry/fit are checked with fresh clocks AFTER
I/O at protected commits. Stability age is the parent's responsibility when computing not_after_epoch.

CANCEL COMMITS: SIGTERM/INT/HUP set a latch on the main thread. Sink threads inherit these signals blocked. A commit
blocks them on the main thread, checks both the latch and sigpending, checks fresh expiry/fit, and records its decision.
Launch commits authorization immediately before Popen, then restores the mask BEFORE spawning (the child does not
inherit blocked SIGTERM); a later cancel is an immediate post-spawn stop and prevents GO. GO writes+flushes while masked;
a later cancel is a post-GO stop. Acknowledgment writes+flushes while masked; a later cancel is post-acknowledgment. A
completion overrun after an irreversible write returns an unsuccessful exit code; the parent must match exit+summary.

STOP/CLEAR: one full-identity-checked child-group SIGTERM, no escalation, no SIGKILL/timeouts/ulimit/deletion. Grace
starts at first stop request and at observed child reap. Clearance time is recorded only AFTER reap, both closed clean
streams, ended sink threads, and a fresh complete empty-owned census have ALL been verified, then checked against every
cutoff. Later cleanup cannot undo expiry. A lost wait status or any observation/capture/evidence error latches failure.

IDENTITY/ACCOUNTING: bracket every ownership/accounting measurement by (pid, uniqueid, idversion, euid, ruid, ppid,
pgid, trace flag). XNU changes idversion on exec (lane tmp/xnu_kern_exec.c:7096-7104). Same uid means real OR effective
uid matches. A same-real/different-effective-uid process is NOT silently exempt: unreadable cwd/argv/task makes census
incomplete and admission/clearance fail closed. Cwd is read before and after argv; any positive establishes membership,
all negatives must be readable and bracket-stable. Completeness is sampled, never an atomic global snapshot. Missing
metadata before identification/measurement is incomplete coverage, not proven absence. Lane RSS and busy limits apply
at every observation; single-process admission reserves cpu_slots (1..2), irrespective of the test trip threshold.

DISK: retain the lane-disk root fd/device/inode; reach output roots and TMPDIR through no-follow directory descriptors
under that anchor, verify path identities before accounting. No mount boundary, vanished or retyped charged subtree is
accepted. Walk bytes = sum of logical regular-file st_size over DISTINCT (device,inode), so settlement/.staged is charged
once. Run charge = ALL output-root bytes (including launch/samples/sinks/strays) + ALL TMPDIR bytes. No child writes
elsewhere are permitted by its reviewed contract. Capped streams/samples and sampled OUTPUT/lane/free trips are not an
OS write sandbox; the separately reviewed child caps remain necessary. Reservation retained until parent release.

I/O: absolute shared deadlines checked before/after native calls, final writes, fsyncs, closes, sorting and every
completion path. Observation deadlines are clamped to known grace/chunk cutoffs. Uninterruptible native calls can
return late; lateness is a failure, not an invented universal latency guarantee.

PUBLICATION: final census/aggregate/RSS/busy/overflow/root/pin/digest checks first. Build the FINAL receipt and settlement
payloads ONCE, then budget exactly those bytes against fresh free floor, distinct-inode lane ceiling and total run
charge + payload <= reservation. If budget is unavailable or insufficient, REFUSE publication (no receipt/settlement
write). Publish those SAME buffers exclusively, fsync/close/readback, link NAME.staged to NAME and verify same inode,
fsync EVERY output directory; read post_publish_mono. Fresh resource/freshness/fit checks precede the protected final
acknowledgment. The parent must verify exit code + captured one-line summary + both file digests, all ended-owned
identities and late artifacts before its exclusive release commit. Standalone JSON/exit/checker PASS releases nothing.

Exit: 0 acknowledged SETTLED, 10 acknowledged NOT_LAUNCHED, 11 acknowledged UNSETTLED, 12 publication refused/receipt
failed, 13 settlement/sync/finalization failed, 14 acknowledgment refused or overran, 2 unusable config/anchors.
All versions before v10 stay immutable and unrun. Usage: owned_supervisor_v10.py CONFIG.json
"""
import contextlib
import ctypes
import errno
import hashlib
import json
import math
import os
import signal
import stat
import struct
import subprocess
import sys
import threading
import time

VERSION = "owned_supervisor_v10"
CANCEL_SIGNALS = {signal.SIGTERM, signal.SIGINT, signal.SIGHUP}
CANCEL = {"signal": None, "mono": None}
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
          "admission": dict, "fault_injection": dict}
ADMISSION = {"go_path": str, "stability_receipt_path": str, "reservation_bytes": int,
             "outstanding_reservations_bytes": int, "lane_outstanding_reservations_bytes": int}
BOUND_KEYS = ("output_roots", "argv", "max_wall_s", "cpu_slots", "reservation_bytes",
              "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")
MY_PID, MY_UID = os.getpid(), os.getuid()
SELF = os.path.abspath(__file__)


class GuardError(OSError):
    pass


def cancel(signum, frame):
    if CANCEL["signal"] is None:
        CANCEL.update(signal=signum, mono=time.monotonic())


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
        self.end = time.monotonic() + seconds
        if until is not None:
            self.end = min(self.end, until)

    def check(self, operation):
        if time.monotonic() > self.end:
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


def identify(pid):
    a, s1, b, s2, c = unique(pid), short(pid), unique(pid), short(pid), unique(pid)
    if not (a == b == c):
        raise GuardError("IDENTITY_CHANGED %d" % pid)
    for s in (s1, s2):
        s.update(uniqueid=a[0], idversion=a[1])
    if fingerprint(s1) != fingerprint(s2):
        raise GuardError("IDENTITY_METADATA_CHANGED %d" % pid)
    return s2


def stable(pid, before):
    return fingerprint(identify(pid)) == fingerprint(before)


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


def write_all(fd, data, dl):
    view = memoryview(data)
    while view:
        dl.check("before write")
        n = os.write(fd, view)
        if n <= 0:
            raise GuardError("ZERO_PROGRESS_WRITE")
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
    return a["sha256"]


def linked_publication(fd, name, data, dl):
    h = publish(fd, name + ".staged", data, dl)
    os.link(name + ".staged", name, src_dir_fd=fd, dst_dir_fd=fd)
    dl.check("after settlement link")
    a, _ = read_file(name, len(data), dl, fd)
    s = os.stat(name + ".staged", dir_fd=fd, follow_symlinks=False)
    if a["sha256"] != h or a["inode"] != [s.st_dev, s.st_ino] or a["nlink"] != 2:
        raise GuardError("SETTLEMENT_LINK_MISMATCH")
    dl.check("after settlement link readback")
    return h


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def integer(x):
    return isinstance(x, int) and not isinstance(x, bool)


def hex64(x):
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


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
    if set(cfg["fault_injection"]) - {"identity_check_fails"} or any(not isinstance(x, bool) for x in cfg["fault_injection"].values()):
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


class Supervisor:
    def __init__(self, cfg, path, digest):
        self.cfg, self.config_path, self.config_sha = cfg, path, digest
        self.num_tb, self.arg_max = timebase(), argmax()
        self.self_sha = read_file(SELF, PIN_CAP, Deadline(IO_S))[0]["sha256"]
        self.start_epoch, self.start_mono = time.time(), time.monotonic()
        self.fit_epoch = min(self.start_epoch + cfg["max_chunk_seconds"] - 120, cfg["owned_compute_settled_by_epoch"] - 180)
        self.fit_mono = self.start_mono + self.fit_epoch - self.start_epoch
        self.rec = {"supervisor": VERSION, "supervisor_sha256": self.self_sha, "config_sha256": digest,
                    "config_path": path, "supervisor_pid": MY_PID, "uid": MY_UID,
                    "clock_note": "mono_*: raw time.monotonic seconds; epoch_*: raw time.time seconds; NO human-readable timestamps",
                    "parent_scope_sha256": "e441d8585228c2976700cba2c3397acfa1e544bc3dfe7af919205581572af22b",
                    "ownership_residual": "fast contract-violating fork+setsid+intermediate exit can evade sampling; not an OS sandbox"}
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

    def deadline(self, seconds, phase=None):
        cut = min([self.fit_mono] + [x[1] for x in self.cutoffs()])
        if phase is not None:
            cut = min(cut, phase.end)
        return Deadline(seconds, cut)

    def fail(self, key, detail=None):
        if key in self.failure_keys:
            return
        self.failure_keys.add(key)
        self.failures.append({"code": key, "detail": str(detail)[:600] if detail is not None else None, "mono": time.monotonic()})
        if self.pid is not None and self.stop is None:
            self.request_stop("FAILURE")

    def trip(self, key, detail=None):
        if key not in self.trips:
            self.trips[key] = {"trip": key, "detail": detail, "mono": time.monotonic(), "epoch": time.time()}
        self.request_stop(key)

    def reap(self):
        if self.pid is None or self.rc is not None or self.lost_wait:
            return
        try:
            p, st = os.waitpid(self.pid, os.WNOHANG)
        except ChildProcessError:
            self.lost_wait = True
            self.fail("WAIT_STATUS_LOST")
            return
        if p:
            self.rc, self.exit_mono, self.exit_epoch = os.waitstatus_to_exitcode(st), time.monotonic(), time.time()

    def request_stop(self, reason):
        if self.stop is not None:
            return
        self.stop = {"reason": reason, "mono": time.monotonic(), "epoch": time.time()}
        s = {"sent": False, "mono_check": time.monotonic()}
        self.signal = s
        if self.ident is None:
            s["why_not"] = "NO_IDENTITY"
            return
        if self.rc is not None:
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
            now = identify(self.pid)
            ok = fingerprint(now) == fingerprint(self.ident)
            s["identity_ok"] = ok
            if not ok:
                raise GuardError("identity mismatch")
            os.killpg(self.group, signal.SIGTERM)
            s.update(sent=True, mono_sent=time.monotonic())
        except ProcessLookupError as e:
            s["error"] = repr(e)
        except BaseException as e:
            s["error"] = repr(e)
            self.fail("IDENTITY_UNVERIFIED", repr(e))

    def cutoffs(self):
        cuts = []
        if self.stop is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_STOP_REQUEST", self.stop["mono"] + self.cfg["settle_s"]))
        if self.exit_mono is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_CHILD_EXIT", self.exit_mono + self.cfg["settle_s"]))
        return cuts

    def register_owned(self, p, via):
        u = p["uniqueid"]
        if u not in self.owned:
            self.owned[u] = {"identity": dict(p), "via": via, "first_seen_mono": time.monotonic()}
            if self.ident is not None and u != self.ident["uniqueid"]:
                self.violations.append(dict(p))
                self.fail("SINGLE_PROCESS_CONTRACT_VIOLATION", p)

    def census(self, dl):
        procs, missing = {}, []
        for pid in all_pids(dl):
            dl.check("census identification")
            try:
                procs[pid] = identify(pid)
            except OSError as e:
                missing.append([pid, "identify", repr(e)])
        live_owned = {u for u in self.owned if any(p["uniqueid"] == u for p in procs.values())}
        if self.ident is not None:
            for p in procs.values():
                if p["uniqueid"] == self.ident["uniqueid"] and fingerprint(p) != fingerprint(self.ident):
                    self.fail("CHILD_IDENTITY_CHANGED", p)
        for p in procs.values():
            if self.group is not None and p["pgid"] == self.group:
                self.register_owned(p, "child_group")
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
                    a = identify(parent["pid"])
                    b = identify(p["pid"])
                    c = identify(parent["pid"])
                    if fingerprint(a) != fingerprint(parent) or fingerprint(c) != fingerprint(parent) or fingerprint(b) != fingerprint(p):
                        raise GuardError("CURRENT_PARENT_EDGE_CHANGED")
                    self.register_owned(p, "current_parent:%d" % parent["uniqueid"])
                    live_owned.add(p["uniqueid"])
                    changed = True
                except OSError as e:
                    missing.append([p["pid"], "parent_edge", repr(e)])
        lane, cpu = {}, {}
        for pid, p in procs.items():
            dl.check("census accounting")
            if p["status"] == SZOMB or not (p["euid"] == MY_UID or p["ruid"] == MY_UID):
                continue
            owned = p["uniqueid"] in live_owned
            try:
                if not stable(pid, p):
                    raise GuardError("BEFORE_MEASUREMENT_CHANGED")
                member = owned
                if not member:
                    c1 = cwd_of(pid)
                    av = argv_of(pid, self.arg_max)
                    c2 = cwd_of(pid)
                    member = any(below(c, r) for c in (c1, c2) for r in self.cfg["lane_roots"]) or any(
                        r in a for a in av for r in self.cfg["lane_roots"])
                if not stable(pid, p):
                    raise GuardError("MEMBERSHIP_IDENTITY_CHANGED")
                if not member:
                    continue
                rss, ticks = task_of(pid)
                key = (p["uniqueid"], p["idversion"])
                prior = self.prev_cpu.get(key)
                start = start_of(pid) if prior is None else None
                if not stable(pid, p):
                    raise GuardError("TASK_IDENTITY_CHANGED")
                now_m, now_e = time.monotonic(), time.time()
                if prior is None:
                    seconds = now_e - start
                    busy = seconds <= 0.05 or ticks * self.num_tb >= seconds * 1e9 * self.cfg["busy_cpu_fraction"]
                else:
                    seconds = now_m - prior[0]
                    busy = seconds <= 0 or (ticks - prior[1]) * self.num_tb >= seconds * 1e9 * self.cfg["busy_cpu_fraction"]
                cpu[key] = (now_m, ticks)
                lane[pid] = {"rss": rss, "busy": busy}
            except OSError as e:
                missing.append([pid, "real_or_effective_uid_measurement", repr(e)])
        self.prev_cpu = cpu
        dl.check("after census")
        owned = [p for p in procs.values() if p["uniqueid"] in live_owned]
        return {"complete": not missing, "incomplete_n": len(missing), "incomplete": missing[:30], "pids": len(procs),
                "owned_live": [dict(p) for p in sorted(owned, key=lambda x: x["pid"])],
                "group_live": sorted(p["pid"] for p in procs.values() if self.group is not None and p["pgid"] == self.group),
                "owned_zombies": sorted(p["pid"] for p in owned if p["status"] == SZOMB),
                "lane_pids": sorted(lane), "lane_rss": sum(v["rss"] for v in lane.values()),
                "lane_busy_pids": sorted(pid for pid, v in lane.items() if v["busy"]),
                "lane_busy": sum(1 for v in lane.values() if v["busy"]), "mono_complete": time.monotonic()}

    def full_census(self, dl):
        c = None
        for _ in range(3):
            c = self.census(dl)
            if c["complete"]:
                break
            dl.check("before census retry")
            time.sleep(min(0.05, max(0, dl.end - time.monotonic())))
        dl.check("after census retries")
        return c

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
        s = os.fstatvfs(self.lane_fd)
        value = s.f_bavail * s.f_frsize
        dl.check("after fstatvfs")
        return value

    def accounting(self, dl, lane=True):
        self.verify_anchors(dl)
        seen = set()
        charge = sum(walk_fd(fd, self.lane_id[0], dl, seen) for fd, _ in self.root_fds.values())
        charge += walk_fd(self.tmp_fd, self.lane_id[0], dl, seen)
        total = walk_fd(self.lane_fd, self.lane_id[0], dl) if lane else self.lane_bytes
        free = self.free(dl)
        self.charged, self.lane_bytes = charge, total
        self.min_free = free if self.min_free is None else min(self.min_free, free)
        self.maxima["charged_bytes"] = max(charge, self.maxima["charged_bytes"])
        dl.check("after accounting")
        return {"charged_bytes": charge, "lane_bytes": total, "free": free}

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
        expected = {k: self.cfg[k] for k in BOUND_KEYS[:4]}
        expected.update({k: adm[k] for k in BOUND_KEYS[4:]})
        entries = go.get("configs")
        if not isinstance(entries, dict) or self.config_sha not in entries:
            raise GuardError("GO_DOES_NOT_NAME_THIS_CONFIG")
        if entries != {self.config_sha: expected}:
            raise GuardError("GO_BINDING_MISMATCH")
        if not number(go.get("not_after_epoch")) or not hex64(go.get("stability_receipt_sha256")):
            raise GuardError("GO_FRESHNESS_FIELDS_INVALID")
        if go["stability_receipt_sha256"] != sa["sha256"] or not isinstance(sr, dict) or sr.get("verdict") != "PASS":
            raise GuardError("STABILITY_DIGEST_OR_VERDICT_MISMATCH")
        out = {"go_sha256": ga["sha256"], "stability_receipt_sha256": sa["sha256"], "not_after_epoch": go["not_after_epoch"]}
        if self.authorization is not None and self.authorization != out:
            raise GuardError("AUTHORIZATION_CHANGED")
        self.authorization = out
        dl.check("after authorization I/O")
        return out

    def time_commit(self, phase, required_s=0):
        """called with cancellation signals masked, AFTER all I/O. No timestamp formatting or helper."""
        epoch, mono = time.time(), time.monotonic()
        if pending_cancel():
            raise GuardError("CANCEL_AT_" + phase)
        if self.authorization is None or epoch > self.authorization["not_after_epoch"]:
            raise GuardError("GO_EXPIRED_AT_" + phase)
        if epoch + required_s > self.fit_epoch or mono + required_s > self.fit_mono:
            raise GuardError("FIT_FAILED_AT_" + phase)
        return {"phase": phase, "mono": mono, "epoch": epoch, "required_s": required_s}

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
        return self.rc is not None and len(self.streams) == 2 and all(v["closed"] and v["error"] is None for v in self.streams.values()) and len(self.threads) == 2 and all(not t.is_alive() for t in self.threads)

    def clearance(self):
        self.reap()
        if not self.cheap_clear():
            return False
        c = self.full_census(self.deadline(CENSUS_S))
        self.limits(c)
        if not c["complete"] or c["owned_live"] or c["group_live"] or not self.cheap_clear():
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
    sup.created[path] = ident
    rec = {"bytes_seen": 0, "bytes_written": 0, "overflow": False, "closed": False, "error": None, "sha256_written": None}
    sup.streams[name] = rec

    def run():
        h = hashlib.sha256()
        try:
            while True:
                chunk = pipe.read1(65536)
                if not chunk:
                    break
                rec["bytes_seen"] += len(chunk)
                room = max(0, cap - rec["bytes_written"])
                if room:
                    b = chunk[:room]
                    write_all(out, b, sup.deadline(IO_S))
                    h.update(b)
                    rec["bytes_written"] += len(b)
                if len(chunk) > room:
                    rec["overflow"] = True
        except BaseException as e:
            rec["error"] = repr(e)
        finally:
            dl = sup.deadline(IO_S)
            errors = []
            for label, action in (("fsync", lambda: os.fsync(out)), ("close", lambda: os.close(out)), ("pipe_close", pipe.close)):
                try:
                    action()
                    dl.check("sink " + label)
                except BaseException as e:
                    errors.append(repr(e))
            if errors:
                rec["error"] = (rec["error"] or "") + ";".join(errors)
            rec["sha256_written"] = h.hexdigest()
            rec["mono_close_completed"] = time.monotonic()
            rec["closed"] = rec["error"] is None
    # Every sink permanently inherits blocked cancellation signals; only the main thread receives them.
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
        a = s.accounting(dl)
        rec["resources"] = a
        res = s.cfg["admission"]["reservation_bytes"]
        if a["free"] < s.cfg["launch_free_min_bytes"] + res or a["free"] - res - s.cfg["admission"]["outstanding_reservations_bytes"] < POLICY["free"]:
            raise GuardError("LAUNCH_FREE_FAILED")
        if a["lane_bytes"] + res + s.cfg["admission"]["lane_outstanding_reservations_bytes"] > s.cfg["lane_disk_ceiling_bytes"]:
            raise GuardError("LANE_CEILING_AT_ADMISSION")
        rec["censuses"] = []
        for n in range(2):
            c = s.full_census(dl)
            rec["censuses"].append(c)
            if not c["complete"] or not s.limits(c, True):
                raise GuardError("ADMISSION_CENSUS_INCOMPLETE_OR_LIMITS")
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


def launch_and_go(s):
    dl = s.deadline(IO_S)
    fd, base = s.location(s.cfg["samples"])
    s.samples_fd, ident = create_file(fd, base)
    s.created[s.cfg["samples"]] = ident
    s.authorization_io(dl)
    c = s.full_census(dl)
    s.rec["launch_census"] = c
    if not c["complete"] or not s.limits(c, True):
        raise GuardError("LAUNCH_CENSUS_INCOMPLETE_OR_LIMITS")
    a = s.accounting(dl)
    if a["free"] < s.cfg["launch_free_min_bytes"] + s.cfg["admission"]["reservation_bytes"] or not s.reservation_fits(a):
        raise GuardError("LAUNCH_RESOURCES_FAILED")
    dl.check("after launch preparation")
    with protected():
        s.resource_age(c)
        s.rec["launch_commit"] = s.time_commit("LAUNCH", s.cfg["max_wall_s"] + s.cfg["settle_s"] + FINALIZE_S)
    # Launch authorization is committed; mask restored before Popen. Any subsequent cancel is a post-launch stop.
    s.mono_spawn, s.epoch_spawn = time.monotonic(), time.time()
    s.rec.update(mono_spawn=s.mono_spawn, epoch_spawn=s.epoch_spawn,
                 mono_child_deadline=s.mono_spawn + s.cfg["max_wall_s"])
    child = subprocess.Popen(s.cfg["argv"], cwd=s.cfg["lane"], env=dict(s.cfg["env"]), stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, close_fds=True)
    try:
        s.child, s.pid = child, child.pid
        s.keep.append(child)
        s.ident = identify(s.pid)
        if s.ident["pgid"] != s.pid or s.ident["euid"] != MY_UID or s.ident["ruid"] != MY_UID:
            raise GuardError("CHILD_IDENTITY_OR_GROUP_INVALID")
        s.group = s.ident["pgid"]
        s.register_owned(s.ident, "child")
        s.threads = [sink(s, "stdout", child.stdout), sink(s, "stderr", child.stderr)]
        if CANCEL["signal"] is not None:
            s.cancel_handled = True
            s.trip("SUPERVISOR_CANCEL", CANCEL["signal"])
        launch = {"supervisor": VERSION, "supervisor_sha256": s.self_sha, "config_sha256": s.config_sha,
                  "supervisor_pid": MY_PID, "identity": s.ident, "argv": s.cfg["argv"], "cwd": s.cfg["lane"],
                  "env": s.cfg["env"], "mono_spawn": s.mono_spawn, "epoch_spawn": s.epoch_spawn,
                  "authorization": s.authorization, "launch_commit": s.rec["launch_commit"],
                  "cpu_slots": s.cfg["cpu_slots"], "reservation_bytes": s.cfg["admission"]["reservation_bytes"]}
        fd, name = s.location(s.cfg["launch_record"])
        data = bytes_json(launch)
        s.rec["launch_record_sha256"] = publish(fd, name, data, s.deadline(IO_S))
        st = os.stat(name, dir_fd=fd, follow_symlinks=False)
        s.created[s.cfg["launch_record"]] = (st.st_dev, st.st_ino)
        gd = s.deadline(IO_S)
        c = s.full_census(gd)
        s.rec["pre_go_census"] = c
        if not c["complete"] or len(c["owned_live"]) != 1 or c["owned_live"][0]["uniqueid"] != s.ident["uniqueid"] or not s.limits(c, True):
            raise GuardError("GO_CENSUS_INCOMPLETE_OR_LIMITS")
        s.authorization_io(gd)
        a = s.accounting(gd)
        if a["free"] < s.cfg["launch_free_min_bytes"] + s.cfg["admission"]["reservation_bytes"] or not s.reservation_fits(a):
            raise GuardError("GO_RESOURCES_FAILED")
        gd.check("after GO preparation")
        with protected():
            s.resource_age(c)
            remaining = max(0, s.mono_spawn + s.cfg["max_wall_s"] - time.monotonic())
            if remaining <= 0 or s.stop is not None or s.failures:
                raise GuardError("GO_STOP_OR_DEADLINE")
            s.rec["go_commit"] = s.time_commit("GO", remaining + s.cfg["settle_s"] + FINALIZE_S)
            child.stdin.write(b"GO\n")
            child.stdin.flush()
            s.rec["go_written_mono"] = time.monotonic()
            child.stdin.close()
            gd.check("after GO write/flush/close")
            s.rec["go_delivered"] = True
    except BaseException as e:
        if s.pid is None:
            s.child, s.pid = child, child.pid
            s.keep.append(child)
        s.fail("POST_SPAWN_FAILURE", repr(e))
    finally:
        if child.stdin is not None and not child.stdin.closed:
            try:
                child.stdin.close()
            except OSError as e:
                s.fail("STDIN_CLOSE_FAILED", repr(e))
    if not s.rec.get("go_delivered"):
        s.fail("GO_NOT_DELIVERED")
    observe(s)


def observe(s):
    s.loop_status = "RUNNING"
    while True:
        try:
            s.reap()
            if CANCEL["signal"] is not None:
                s.cancel_handled = True
                s.trip("SUPERVISOR_CANCEL", CANCEL["signal"])
            if s.clearance():
                return
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
            s.sample({"mono": time.monotonic(), "epoch": time.time(), "rc": s.rc, "census": c,
                      "resources": a, "streams": {k: dict(v) for k, v in s.streams.items()},
                      "stop": None if s.stop is None else s.stop["reason"], "failure_codes": sorted(s.failure_keys),
                      "trips": list(s.trips)})
        except BaseException as e:
            s.fail("OBSERVATION_FAILED", repr(e))
        for name, cut in s.cutoffs():
            if time.monotonic() > cut:
                s.fail(name)
                s.loop_status = name
                return
        remaining = [cut - time.monotonic() for _, cut in s.cutoffs()]
        time.sleep(max(0, min([s.cfg["sample_s"]] + remaining)))


def unsuccessful(code, reason, extra=None):
    obj = {"supervisor": VERSION, "acknowledged": False, "exit_code": code, "reason": reason,
           "clock_note": "raw monotonic/epoch telemetry only"}
    if extra:
        obj.update(extra)
    sys.stdout.write(json.dumps(obj, allow_nan=False) + "\n")
    sys.stdout.flush()
    return code


def finalize(s):
    phase = Deadline(FINALIZE_S, s.fit_mono)
    try:
        return final_body(s, phase)
    except BaseException as e:
        sys.stderr.write("FINALIZATION_FAILED %r\n" % e)
        return unsuccessful(13, "FINALIZATION_FAILED", {"config_sha256": s.config_sha})


def final_body(s, phase):
    s.reap()
    if s.pid is not None:
        if s.rc is None:
            s.fail("CHILD_NOT_REAPED")
        c = s.full_census(Deadline(CENSUS_S, phase.end))
        s.rec["final_census"] = c
        s.limits(c)
        if not c["complete"]:
            s.fail("FINAL_CENSUS_INCOMPLETE", c["incomplete"])
        if c["owned_live"]:
            s.fail("OWNED_LIVE", c["owned_live"])
        if not s.cheap_clear():
            s.fail("STREAMS_OR_THREADS_NOT_CLOSED")
        if s.clear is None and not c["owned_live"] and s.cheap_clear():
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
        if s.streams.get(k, {}).get("sha256_written") is not None:
            expected[s.cfg[k]] = s.streams[k]["sha256_written"]
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
    state = "NOT_LAUNCHED" if s.pid is None else "UNSETTLED" if s.failures else "SETTLED"
    code = {"SETTLED": 0, "NOT_LAUNCHED": 10, "UNSETTLED": 11}[state]
    s.rec.update(settlement=state, child_pid=s.pid, child_identity=s.ident, child_returncode=s.rc,
                 child_exit_mono=s.exit_mono, child_exit_epoch=s.exit_epoch, wait_status_lost=s.lost_wait,
                 failures=s.failures, trips=list(s.trips.values()), stop_request=s.stop, signal=s.signal,
                 owned_identities=list(s.owned.values()), contract_violations=s.violations, clear=s.clear,
                 streams=s.streams, loop_status=s.loop_status, samples_written=s.sample_count,
                 samples_bytes=s.sample_bytes, maxima=s.maxima, min_free=s.min_free, artifacts=arts,
                 evidence_expected_sha256=expected, pins_at_end=pin_end, output_root_inventory=inventory,
                 publication_precheck=a, reservation_bytes=s.cfg["admission"]["reservation_bytes"],
                 mono_decision=time.monotonic(), epoch_decision=time.time(), cancel=dict(CANCEL))
    # Serialize ONCE. No budget fields or failures are appended after these exact buffers have been budgeted.
    rb = bytes_json(s.rec)
    rsha = hashlib.sha256(rb).hexdigest()
    sb = bytes_json({"supervisor": VERSION, "config_sha256": s.config_sha, "settlement": state,
                    "receipt": s.cfg["receipt"], "receipt_sha256": rsha, "child_returncode": s.rc,
                    "failure_codes": sorted(s.failure_keys), "trips": list(s.trips),
                    "authority": "only independent parent commit releases reservations"})
    payload = len(rb) + len(sb)
    b = s.accounting(Deadline(IO_S, phase.end))
    adm = s.cfg["admission"]
    fits = payload <= PUBLICATION_CAP and s.reservation_fits(b, payload)
    if not fits:
        return unsuccessful(12, "PUBLICATION_REFUSED", {"config_sha256": s.config_sha, "payload_bytes": payload,
                                                         "resources": b, "reservation_bytes": adm["reservation_bytes"]})
    pub = Deadline(60, phase.end)
    fd, name = s.location(s.cfg["receipt"])
    try:
        got = publish(fd, name, rb, pub)
        if got != rsha:
            raise GuardError("RECEIPT_DIGEST_MISMATCH")
    except OSError as e:
        return unsuccessful(12, "RECEIPT_PUBLICATION_FAILED", {"error": repr(e)})
    fd, name = s.location(s.cfg["settlement_record"])
    try:
        ssha = linked_publication(fd, name, sb, pub)
        for root, (fd, ident) in s.root_fds.items():
            os.fsync(fd)
            pub.check("after directory fsync")
    except OSError as e:
        return unsuccessful(13, "SETTLEMENT_OR_DIRECTORY_SYNC_FAILED", {"receipt_sha256": rsha, "error": repr(e)})
    post_publish = time.monotonic()
    # I/O FIRST, fresh raw-clock/cancel checks LAST at the protected acknowledgment commit.
    try:
        s.authorization_io(Deadline(IO_S, phase.end))
        end = s.accounting(Deadline(IO_S, phase.end))
        if not s.reservation_fits(end):
            raise GuardError("ACK_RESOURCE_RECHECK_FAILED")
        phase.check("after acknowledgment preparation")
        with protected():
            # A cancel already acted on as the cause of this result does not masquerade as an unobserved late cancel.
            if s.cancel_handled and CANCEL["signal"] is not None and not (set(signal.sigpending()) & CANCEL_SIGNALS):
                epoch, mono = time.time(), time.monotonic()
                if epoch > s.authorization["not_after_epoch"] or epoch > s.fit_epoch or mono > s.fit_mono:
                    raise GuardError("ACK_EXPIRY_OR_FIT")
                commit = {"phase": "ACK", "epoch": epoch, "mono": mono, "cancel_handled": True}
            else:
                commit = s.time_commit("ACK")
            phase.check("acknowledgment commit")
            ack = {"supervisor": VERSION, "acknowledged": True, "exit_code": code, "settlement": state,
                   "config_sha256": s.config_sha, "receipt_sha256": rsha, "settlement_record_sha256": ssha,
                   "receipt_bytes": len(rb), "settlement_bytes": len(sb), "post_publish_mono": post_publish,
                   "ack_commit": commit, "publication_resources": b, "ack_resources": end,
                   "child_returncode": s.rc, "failure_codes": sorted(s.failure_keys),
                   "owned_live": s.rec.get("final_census", {}).get("owned_live", []),
                   "contract_violations": s.violations}
            sys.stdout.write(json.dumps(ack, sort_keys=True, allow_nan=False) + "\n")
            sys.stdout.flush()
            phase.check("after acknowledgment write/flush")
        return code
    except BaseException as e:
        # If stdout already committed a line, do not emit a contradictory second line: mismatch exit refuses release.
        if "ack" in locals():
            sys.stderr.write("ACK_COMPLETION_FAILED %r\n" % e)
            return 14
        return unsuccessful(14, "ACK_REFUSED", {"receipt_sha256": rsha, "settlement_record_sha256": ssha,
                                               "post_publish_mono": post_publish, "error": repr(e)})


def main():
    for sig in CANCEL_SIGNALS:
        signal.signal(sig, cancel)
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_UNBLOCK, CANCEL_SIGNALS)
    if len(sys.argv) != 2:
        sys.stderr.write("usage: owned_supervisor_v10.py CONFIG.json\n")
        return 2
    try:
        path = os.path.abspath(sys.argv[1])
        a, raw = read_file(path, SMALL, Deadline(IO_S), keep=True)
        cfg = parse_json(raw)
        validate(cfg)
        s = Supervisor(cfg, path, a["sha256"])
        s.open_anchors()
    except BaseException as e:
        sys.stderr.write("CONFIG_OR_ANCHORS_UNUSABLE %r\n" % e)
        return 2
    s.rec["admission"] = admission(s)
    if not s.rec["admission"]["reasons"]:
        try:
            launch_and_go(s)
        except BaseException as e:
            if s.pid is None:
                s.rec["launch_refusal"] = repr(e)
                if CANCEL["signal"] is not None:
                    s.cancel_handled = True
            else:
                s.fail("LAUNCH_OR_OBSERVE_EXCEPTION", repr(e))
                try:
                    observe(s)
                except BaseException as e2:
                    s.fail("EXCEPTION_OBSERVATION_FAILED", repr(e2))
    return finalize(s)


if __name__ == "__main__":
    sys.exit(main())
