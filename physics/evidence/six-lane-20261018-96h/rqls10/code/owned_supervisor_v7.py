#!/usr/bin/env python3
"""owned_supervisor_v7: run ONE child process under a fail-closed guard. Standard library only (ctypes for read-only
macOS libproc/sysctl process metadata). Supersedes the never-run v3-v6 (v6 = v5 + evidence digests). v5 was reviewed by
Codex (RUN/review/rqls10-owned-supervisor-v5-source-codex-v1.prompt.stdout.txt, HOLD: 9 FATAL, 5 MAJOR, 1 MINOR); the
per-finding disposition is review/rqls10-owned-supervisor-v7-disposition-v1.json. code/owned_supervisor_v2.py untouched.

Outcomes (three only): SETTLED, UNSETTLED, NOT_LAUNCHED. Every uncertain outcome is UNSETTLED.
 1. Failure latch. Any failure of identity, observation (census, free space, output size, lane walk, any budget), helper,
    capture (sink threads, samples), GO delivery, launch-record publication, grace expiry, evidence binding or an
    unexpected exception is appended to a monotonic latch that is never cleared, and requests a stop. A non-empty latch
    makes a launched run UNSETTLED. Resource trips (DEADLINE, RSS, BUSY, FREE, OUTPUT, STREAM_CAP, LANE_CEILING,
    SUPERVISOR_CANCEL) request a stop and are recorded, but are not failures by themselves.
 2. Stop and grace. The first stop request (trip or failure) is latched with a monotonic time; at most one SIGTERM goes to
    the child's process group, only after the identity check of item 4. The observation grace (settle_s) runs from the
    first stop request and from the reaping of the child; every decision reads a fresh monotonic clock. Grace expiry
    with anything unresolved is latched (GRACE_EXPIRED_*) and is irreversible: later cleanup cannot settle the run.
    No SIGKILL, no escalation, no subprocess or tool timeouts, no ulimit, no deletion.
 3. Single reaper. SIGCHLD is reset to SIG_DFL before any spawn. The child and every /bin/date helper are spawned with
    subprocess.Popen; the Popen objects stay referenced for the whole run and are never polled, waited or communicated;
    only this supervisor reaps them, with os.waitpid(pid, WNOHANG). ECHILD (lost wait status) is a failure and disables
    signalling. (At interpreter exit, after publication, Popen finalizers may poll; no decision depends on that.)
 4. Identity = (pid, p_uniqueid, p_idversion, pgid, uid) from libproc PROC_PIDUNIQIDENTIFIERINFO and
    PROC_PIDT_SHORTBSDINFO (zombie-inclusive queries), captured immediately after spawn, before any other fallible
    setup. A signal is sent only to an unreaped process whose tuple is re-read equal immediately before killpg (the
    child; a /bin/date helper in its own group likewise). Otherwise no signal and IDENTITY_UNVERIFIED is latched.
 5. Lineage census (every sample; libproc and sysctl only, no ps/lsof). XNU assigns p_uniqueid at fork from a global
    increasing counter, keeps it across exec, records the parent's p_uniqueid at fork (p_puniqueid) and does not change
    it on reparenting (xnu bsd/kern/kern_fork.c, kern_proc.c pinsertchild, kern_exit.c proc_reparentlocked; copies in
    lane tmp/). Every observed (uniqueid -> puniqueid) is remembered for the run. With U0 = the child's uniqueid, a
    process u is OWNED if u == U0 or its parent is OWNED; OTHER if u < U0, or its parent is OTHER, or its parent was never
    observed and has a uniqueid < U0; UNRESOLVED if its parent is UNRESOLVED or was never observed and has a uniqueid
    > U0 (for example the dead intermediate of a fast double fork). Live OWNED, UNRESOLVED and child-group processes,
    zombies included (proc_listallpids lists zombies; the queries above pass a nonzero arg so zombies are found), block
    settlement. UNRESOLVED processes of unrelated programs also block (fail-closed). Every listed pid must yield both
    records (ESRCH = gone, rechecked for pid reuse) or the census fails.
 6. Lane accounting (RSS sum, busy count) covers live non-zombie processes of this uid that are OWNED, UNRESOLVED or whose
    cwd or argv references a lane root. Exclusion needs BOTH a successful cwd read and a completely parsed argv without
    a match; one positive read includes; any other unreadable process of this uid fails the census. Busy = CPU time
    over wall time since the previous sample of the same uniqueid, or since process start when first seen, >=
    busy_cpu_fraction; the FIRST observed excess over busy_limit trips BUSY (the limit is sampled, not enforced between
    samples). OWNED or UNRESOLVED processes of another uid block settlement but cannot be RSS/CPU-accounted (recorded).
 7. Bounded observation. Files are read or hashed only if regular (lstat and fstat agree; O_NOFOLLOW|O_NONBLOCK), within
    a byte limit and a monotonic time budget, and must not grow or change while read; the lane walk has an entry and
    time budget; helper output is read non-blocking after reaping; every write checks progress and a time budget.
    Overruns are failures. Native libproc/sysctl/statvfs/listdir calls cannot be time-bounded from Python (limitation
    stated in the HOLD); they are only made between budget checks.
 8. Admission (else NOT_LAUNCHED): strict JSON config (duplicate keys, NaN/Infinity, non-finite numbers and unknown keys
    rejected; the hashed bytes are exactly the parsed bytes) within the hard policy (lane ceiling <= 10737418240,
    free_trip >= 12e9, launch free minimum >= 12.2e9, busy_limit <= 2, rss_trip <= 48 GiB, positive bounded durations,
    nonnegative reservations, reservation >= samples, stream and output caps plus a 4 MiB receipt allowance); pins;
    single parent authority, one use: the GO file (strict JSON, bounded read; its sha256 is recorded) must say
    decision "GO" for this item, must not be expired (not_after_epoch) and must list THIS config's sha256 under
    "configs" with exactly the config's output_roots, argv, max_wall_s, reservation_bytes,
    outstanding_reservations_bytes and lane_outstanding_reservations_bytes (GO_BOUND_KEYS); the output roots must be
    existing, EMPTY, real directories under lane_disk_root (so a GO entry admits one launch), opened once as directory
    fds; every evidence and output path a direct child of an output root; fresh stability receipt (path outside the
    output roots, verdict PASS, age by /bin/date; its sha256 recorded); TMPDIR an existing real directory under
    lane_disk_root outside the output roots; free-space and lane-ceiling checks including the reservation; two complete
    censuses 2 s apart with busy and RSS headroom; libproc setup; working /bin/date; no latched failure. Commit boundary
    immediately before spawn: fresh /bin/date and stability age, GO expiry, cancel, free space and chunk fit
    (now + max_wall_s + settle_s + FINALIZE_ALLOWANCE_S within the chunk and 180 s before the settled-by epoch).
    Reservations and busy slots are allocated and released only by the parent (itemGO, parent release after its
    commit); this supervisor never releases anything and keeps no second ledger.
 9. GO is written only if the identity was captured, both sink threads started, the launch record was published and
    verified, one complete lineage census succeeded after spawn, no failure is latched, no cancel arrived and the spawn
    was at most GO_MAX_DELAY_S ago. GO must be written and flushed and stdin closed; otherwise GO_NOT_DELIVERED is
    latched. Any exception after spawn: failure latched, stop requested, bounded observation, publication attempted.
10. Disk: fresh statvfs floor; declared-output bytes (plus sinks and samples) <= output_trip_bytes; capped sinks; capped
    samples (reaching the cap is a failure); lane-walk bytes + lane outstanding reservations + this run's unused
    reservation (reservation minus bytes written so far) <= ceiling; fresh floor check before final publication.
    Sampling cannot enforce a hard ceiling against child writes between samples; the child's own caps and the
    reservation are the bound.
11. Evidence binding: the config hash is of the parsed bytes; launch record, samples and both sinks must re-hash at
    settlement to the supervisor's own digests (EVIDENCE_MUTATED); pins re-hashed; each output root unchanged (device,
    inode, real directory chain) and holding only declared names; child outputs regular files with one link, born
    after the spawn.
12. Publication: the receipt by exclusive create through the output-root directory fd, writes with progress checks, fsync,
    close, bounded re-read. The settlement record is written in full to NAME.staged the same way and then hard-linked to
    NAME (atomic; NAME never holds partial content), then the directory is fsynced and NAME re-read. Neither file is
    authoritative by itself: the outcome becomes authoritative only when the supervising parent has received the exit
    code and the stdout summary line and has verified the receipt and settlement sha256 values (parent commit). This
    supervisor no longer reads earlier settlement records (no require_settled).
13. Timeliness and helpers (lessons shared from RUN/review/pa19-PSTREAM-v2-source-codex-v1.prompt.stdout.txt):
    SETTLED additionally requires that the child's exit was observed by abs_end_epoch + sample_s + 5 s, or that the
    DEADLINE trip was raised by then (DEADLINE_NOT_ENFORCED_IN_TIME otherwise), and that the settlement decision is
    taken before the chunk limit fixed at admission (SETTLEMENT_PAST_CHUNK_LIMIT). A /bin/date helper is not started
    after any latched failure (null date, recorded as skipped) or after the chunk limit (failure); after reaping, its
    process group must be empty (proc_listpgrppids; HELPER_GROUP_LIVE otherwise). A supervisor cancel that arrives
    after the loop is recorded as SUPERVISOR_CANCEL_LATE at the decision boundary. /bin/date helpers (cwd /, no lane
    path in argv) are not lane processes and are not RSS-accounted.
Exit codes: 0 SETTLED, 10 NOT_LAUNCHED, 11 UNSETTLED, 12 receipt publication failed, 13 settlement record failed,
2 unusable config or output roots (nothing written).
"""
import ctypes, datetime, errno, hashlib, json, math, os, re, signal, stat, struct, subprocess, sys, threading, time

VERSION = "owned_supervisor_v7"
CANCEL = [None]
FINALIZE_ALLOWANCE_S = 120.0
GO_MAX_DELAY_S = 60.0
RECEIPT_ALLOWANCE_BYTES = 4 << 20
SMALL_MAX_BYTES = 1 << 20
PIN_MAX_BYTES = 64 << 20
HASH_BUDGET_S = 60.0
PUBLISH_BUDGET_S = 30.0
WALK_MAX_ENTRIES = 500000
WALK_BUDGET_S = 30.0
ROOT_MAX_ENTRIES = 10000
SEEN_MAX = 200000
DEADLINE_SLACK_EXTRA_S = 5.0
HARD = {"lane_ceiling_max": 10737418240, "free_floor_min": 12000000000, "launch_free_min_min": 12200000000,
        "busy_limit_max": 2, "rss_trip_max": 51539607552, "max_chunk_max": 10800, "stability_age_max": 300}
CONFIG_KEYS = {
    "item": str, "owner": str, "purpose": str, "lane": str, "argv": list, "env": dict, "stdout": str, "stderr": str,
    "stdout_cap_bytes": "int", "stderr_cap_bytes": "int", "outputs": list, "launch_record": str, "samples": str,
    "samples_cap_bytes": "int", "receipt": str, "settlement_record": str, "output_roots": list, "pins": list,
    "max_wall_s": "num", "settle_s": "num", "sample_s": "num", "max_chunk_seconds": "num",
    "owned_compute_settled_by_epoch": "num", "rss_trip_bytes": "int", "free_trip_bytes": "int",
    "output_trip_bytes": "int", "launch_free_min_bytes": "int", "lane_roots": list, "lane_disk_root": str,
    "lane_disk_ceiling_bytes": "int", "lane_walk_s": "num", "busy_limit": "int", "busy_cpu_fraction": "num",
    "rss_projection_bytes": "int", "admission": dict, "helper_budget": dict, "fault_injection": dict}
ADMISSION_KEYS = {"go_path": str, "reservation_bytes": "int", "outstanding_reservations_bytes": "int",
                  "lane_outstanding_reservations_bytes": "int", "stability_receipt_path": str,
                  "stability_max_age_s": "num"}
GO_BOUND_KEYS = ("output_roots", "argv", "max_wall_s", "reservation_bytes", "outstanding_reservations_bytes",
                 "lane_outstanding_reservations_bytes")
HELPER_KEYS = {"max_calls": "int", "call_budget_s": "num", "term_grace_s": "num"}
FAULTS = ("identity_check_fails", "date_helper_fails")
DATE_RE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+-]\d{4}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _cancel(signum, frame):
    if CANCEL[0] is None:
        CANCEL[0] = signum


class Bounded(OSError):
    """an observation or publication that is not a complete, bounded, regular-file operation."""


# ---------------------------------------------------------------- read-only process metadata (macOS libproc, sysctl)
_LP = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
_LP.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
_LP.proc_pidinfo.restype = ctypes.c_int
_LP.proc_listallpids.argtypes = (ctypes.c_void_p, ctypes.c_int)
_LP.proc_listallpids.restype = ctypes.c_int
_LP.proc_listpgrppids.argtypes = (ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
_LP.proc_listpgrppids.restype = ctypes.c_int
_LC = ctypes.CDLL("/usr/lib/libSystem.B.dylib", use_errno=True)
_LC.sysctl.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t),
                       ctypes.c_void_p, ctypes.c_size_t)
_LC.sysctl.restype = ctypes.c_int
_LC.mach_timebase_info.argtypes = (ctypes.c_void_p,)
_LC.mach_timebase_info.restype = ctypes.c_int
# sys/proc_info.h: PROC_PIDTBSDINFO 3 (struct proc_bsdinfo, 136 bytes; pbi_uid uint32 at 20, pbi_pgid uint32 at 100,
# pbi_start_tvsec and pbi_start_tvusec uint64 at 120 and 128), PROC_PIDTASKINFO 4 (struct proc_taskinfo, 96 bytes;
# pti_resident_size uint64 at 8, pti_total_user and pti_total_system uint64 at 16 and 24 in mach time units),
# PROC_PIDVNODEPATHINFO 9 (struct proc_vnodepathinfo, 2352 bytes; pvi_cdir.vip_path char[1024] at 152),
# PROC_PIDT_SHORTBSDINFO 13 (struct proc_bsdshortinfo, 64 bytes; pid, ppid, pgid, status uint32 at 0, 4, 8, 12,
# comm char[16] at 16, uid uint32 at 36). xnu bsd/sys/proc_info_private.h: PROC_PIDUNIQIDENTIFIERINFO 17 (struct
# proc_uniqidentifierinfo, 56 bytes; p_uuid[16] at 0, p_uniqueid uint64 at 16, p_puniqueid uint64 at 24, p_idversion
# int32 at 32), no same-user restriction. xnu proc_info.c: for flavors 3, 13, 17 and 18 a nonzero arg also finds
# zombies. sysctl {CTL_KERN, KERN_PROCARGS2, pid}: int argc, exec path, NUL padding, argc NUL-terminated strings.
PROC_PIDTBSDINFO, PROC_PIDTASKINFO, PROC_PIDVNODEPATHINFO, PROC_PIDT_SHORTBSDINFO = 3, 4, 9, 13
PROC_PIDUNIQIDENTIFIERINFO = 17
BSD_SIZE, TASK_SIZE, VNP_SIZE, SHORT_SIZE, UNIQ_SIZE = 136, 96, 2352, 64, 56
SZOMB = 5
CTL_KERN, KERN_ARGMAX, KERN_PROCARGS2 = 1, 8, 49


class _TB(ctypes.Structure):
    _fields_ = [("numer", ctypes.c_uint32), ("denom", ctypes.c_uint32)]


def _timebase():
    tb = _TB()
    if _LC.mach_timebase_info(ctypes.byref(tb)) != 0 or tb.denom == 0:
        return None
    return (tb.numer, tb.denom)


def _argmax():
    mib = (ctypes.c_int * 2)(CTL_KERN, KERN_ARGMAX)
    val = ctypes.c_int(0)
    size = ctypes.c_size_t(ctypes.sizeof(val))
    if _LC.sysctl(mib, 2, ctypes.byref(val), ctypes.byref(size), None, 0) != 0 or val.value <= 0:
        return None
    return val.value


TIMEBASE = _timebase()
ARGMAX = _argmax()
_ARGBUF = ctypes.create_string_buffer(ARGMAX) if ARGMAX else None
MY_UID = os.getuid()
MY_PID = os.getpid()
SELF = os.path.abspath(__file__)


def _pidinfo(pid, flavor, size, arg):
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    n = _LP.proc_pidinfo(pid, flavor, arg, buf, size)
    if n == size:
        return buf.raw, 0
    e = ctypes.get_errno()
    return None, (e if e else -1)


def short_info(pid):
    raw, e = _pidinfo(pid, PROC_PIDT_SHORTBSDINFO, SHORT_SIZE, 1)
    if raw is None:
        return None, e
    p, pp, pg, status = struct.unpack_from("=IIII", raw, 0)
    uid = struct.unpack_from("=I", raw, 36)[0]
    comm = raw[16:32].split(b"\0")[0].decode("utf-8", "replace")
    return {"pid": p, "ppid": pp, "pgid": pg, "status": status, "uid": uid, "comm": comm}, 0


def uniq_info(pid):
    raw, e = _pidinfo(pid, PROC_PIDUNIQIDENTIFIERINFO, UNIQ_SIZE, 1)
    if raw is None:
        return None, e
    u, pu = struct.unpack_from("=QQ", raw, 16)
    idv = struct.unpack_from("=i", raw, 32)[0]
    return {"uniqueid": u, "puniqueid": pu, "idversion": idv}, 0


def bsd_start(pid):
    raw, e = _pidinfo(pid, PROC_PIDTBSDINFO, BSD_SIZE, 1)
    if raw is None:
        return None, e
    s, us = struct.unpack_from("=QQ", raw, 120)
    return s + us / 1e6, 0


def task_info(pid):
    raw, e = _pidinfo(pid, PROC_PIDTASKINFO, TASK_SIZE, 0)
    if raw is None:
        return None, e
    rss = struct.unpack_from("=Q", raw, 8)[0]
    usr, sysm = struct.unpack_from("=QQ", raw, 16)
    return {"rss": rss, "cpu_ticks": usr + sysm}, 0


def cwd_of(pid):
    raw, e = _pidinfo(pid, PROC_PIDVNODEPATHINFO, VNP_SIZE, 0)
    if raw is None:
        return None, e
    field = raw[152:152 + 1024]
    k = field.find(b"\0")
    if k <= 0:
        return None, -7
    return field[:k].decode("utf-8", "surrogateescape"), 0


def argv_of(pid):
    if _ARGBUF is None:
        return None, -2
    mib = (ctypes.c_int * 3)(CTL_KERN, KERN_PROCARGS2, pid)
    size = ctypes.c_size_t(ARGMAX)
    ctypes.set_errno(0)
    if _LC.sysctl(mib, 3, _ARGBUF, ctypes.byref(size), None, 0) != 0:
        e = ctypes.get_errno()
        return None, (e if e else -1)
    data = ctypes.string_at(_ARGBUF, size.value)
    if len(data) < 4:
        return None, -3
    argc = struct.unpack_from("=i", data, 0)[0]
    if argc < 0 or argc > ARGMAX:
        return None, -5
    k = data.find(b"\0", 4)
    if k < 0:
        return None, -4
    out = [data[4:k].decode("utf-8", "surrogateescape")]
    pos = k
    while pos < len(data) and data[pos] == 0:
        pos += 1
    for _ in range(argc):
        k = data.find(b"\0", pos)
        if k < 0:
            return None, -6
        out.append(data[pos:k].decode("utf-8", "surrogateescape"))
        pos = k + 1
    return out, 0


def list_pids():
    ctypes.set_errno(0)
    n = _LP.proc_listallpids(None, 0)
    if n <= 0:
        return None
    cap = 2 * n + 1024
    for _ in range(4):
        buf = (ctypes.c_int * cap)()
        m = _LP.proc_listallpids(buf, ctypes.sizeof(buf))
        if m <= 0:
            return None
        if m < cap:
            return [buf[i] for i in range(m)]
        cap *= 2
    return None


def pgrp_members(pgid):
    """pids (zombies included) in process group pgid, or None if unreadable. libproc returns a count and 0 on error,
    so errno decides between an empty group and a failure."""
    buf = (ctypes.c_int * 256)()
    ctypes.set_errno(0)
    m = _LP.proc_listpgrppids(pgid, buf, ctypes.sizeof(buf))
    e = ctypes.get_errno()
    if m < 0 or (m == 0 and e != 0) or m >= 256:
        return None
    return [buf[i] for i in range(m)]


# ---------------------------------------------------------------- bounded file operations
def _open_regular(path, max_bytes, dir_fd=None):
    st0 = os.stat(path, dir_fd=dir_fd, follow_symlinks=False)
    if not stat.S_ISREG(st0.st_mode):
        raise Bounded("not a regular file: %s" % path)
    if st0.st_size > max_bytes:
        raise Bounded("larger than %d bytes: %s" % (max_bytes, path))
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dir_fd)
    st1 = os.fstat(fd)
    if (st1.st_dev, st1.st_ino, st1.st_size) != (st0.st_dev, st0.st_ino, st0.st_size) or not stat.S_ISREG(st1.st_mode):
        os.close(fd)
        raise Bounded("changed while opening: %s" % path)
    return fd, st1


def hash_regular(path, max_bytes, budget_s, dir_fd=None, keep=False):
    """sha256 of a regular file read completely within max_bytes and budget_s; returns (hex, size, bytes|None, stat)."""
    deadline = time.monotonic() + budget_s
    fd, st = _open_regular(path, max_bytes, dir_fd)
    h, got, parts = hashlib.sha256(), 0, []
    try:
        while got < st.st_size:
            if time.monotonic() > deadline:
                raise Bounded("time budget exceeded: %s" % path)
            chunk = os.read(fd, min(1 << 20, st.st_size - got))
            if not chunk:
                raise Bounded("short read: %s" % path)
            h.update(chunk)
            got += len(chunk)
            if keep:
                parts.append(chunk)
        if os.read(fd, 1):
            raise Bounded("grew while read: %s" % path)
        st2 = os.fstat(fd)
        if st2.st_size != st.st_size or st2.st_mtime_ns != st.st_mtime_ns:
            raise Bounded("changed while read: %s" % path)
    finally:
        os.close(fd)
    return h.hexdigest(), st.st_size, (b"".join(parts) if keep else None), st


def write_all(fd, data, deadline):
    view = memoryview(data)
    while view:
        if time.monotonic() > deadline:
            raise Bounded("write time budget exceeded")
        k = os.write(fd, view)
        if k <= 0:
            raise Bounded("zero-progress write")
        view = view[k:]


def jbytes(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, allow_nan=False, default=repr) + "\n").encode("utf-8")


def publish(dirfd, name, data):
    """exclusive create through dirfd, progress-checked write, fsync, close, bounded re-read; returns sha256."""
    deadline = time.monotonic() + PUBLISH_BUDGET_S
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dirfd)
    try:
        write_all(fd, data, deadline)
        os.fsync(fd)
    finally:
        os.close(fd)
    h = hashlib.sha256(data).hexdigest()
    got, size, _, _ = hash_regular(name, len(data), max(1.0, deadline - time.monotonic()), dir_fd=dirfd)
    if got != h or size != len(data):
        raise Bounded("re-read mismatch: %s" % name)
    return h


def publish_linked(dirfd, name, data):
    """write NAME.staged completely (publish), hard-link it to NAME (atomic, exclusive), fsync the directory, re-read
    NAME. Returns (sha256, directory fsync error or None)."""
    h = publish(dirfd, name + ".staged", data)
    os.link(name + ".staged", name, src_dir_fd=dirfd, dst_dir_fd=dirfd)
    dir_err = None
    try:
        os.fsync(dirfd)
    except OSError as ex:
        dir_err = repr(ex)
    got, size, _, _ = hash_regular(name, len(data), PUBLISH_BUDGET_S, dir_fd=dirfd)
    if got != h or size != len(data):
        raise Bounded("linked record re-read mismatch: %s" % name)
    return h, dir_err


def walk_bytes(root):
    """regular-file bytes under root by lstat; symlinks not followed; entries vanishing during the walk count 0; at
    most WALK_MAX_ENTRIES entries and WALK_BUDGET_S seconds (else Bounded)."""
    deadline = time.monotonic() + WALK_BUDGET_S
    total, n, stack, first = 0, 0, [root], True
    while stack:
        d = stack.pop()
        try:
            it = os.scandir(d)
        except FileNotFoundError:
            if first:
                raise
            continue
        first = False
        with it:
            for ent in it:
                n += 1
                if n > WALK_MAX_ENTRIES or time.monotonic() > deadline:
                    raise Bounded("lane walk budget exceeded after %d entries" % n)
                try:
                    st = ent.stat(follow_symlinks=False)
                except FileNotFoundError:
                    continue
                if stat.S_ISDIR(st.st_mode):
                    stack.append(ent.path)
                elif stat.S_ISREG(st.st_mode):
                    total += st.st_size
    return total


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def under(path, roots):
    ap = os.path.abspath(path)
    return any(ap == os.path.abspath(r) or ap.startswith(os.path.abspath(r).rstrip("/") + "/") for r in roots)


def real_dir_chain(d):
    d = os.path.abspath(d)
    cur = ""
    for comp in d.split("/")[1:]:
        cur = cur + "/" + comp
        try:
            st = os.lstat(cur)
        except OSError:
            return False
        if stat.S_ISLNK(st.st_mode) or not stat.S_ISDIR(st.st_mode):
            return False
    return True


def _no_dup(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError("duplicate key %r" % k)
        out[k] = v
    return out


def _no_const(name):
    raise ValueError("non-finite JSON constant %s" % name)


def strict_json(raw):
    obj = json.loads(raw.decode("utf-8"), object_pairs_hook=_no_dup, parse_constant=_no_const)
    stack = [obj]
    while stack:
        x = stack.pop()
        if isinstance(x, float) and not math.isfinite(x):
            raise ValueError("non-finite number")
        if isinstance(x, dict):
            stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    return obj


def _int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def _num(x):
    return (isinstance(x, (int, float)) and not isinstance(x, bool)) and math.isfinite(x)


def _norm_abs(p):
    return isinstance(p, str) and p.startswith("/") and os.path.abspath(p) == p


# ---------------------------------------------------------------- configuration
def validate(cfg):
    bad = []

    def keys(d, spec, where):
        if not isinstance(d, dict):
            bad.append("%s is not an object" % where)
            return
        extra, missing = sorted(set(d) - set(spec)), sorted(set(spec) - set(d))
        if extra:
            bad.append("%s unknown keys %s" % (where, extra))
        if missing:
            bad.append("%s missing keys %s" % (where, missing))
        for k, ty in spec.items():
            if k in d:
                v = d[k]
                ok = _int(v) if ty == "int" else _num(v) if ty == "num" else (isinstance(v, ty) and not isinstance(v, bool))
                if not ok:
                    bad.append("%s bad type %s" % (where, k))

    keys(cfg, CONFIG_KEYS, "config")
    if bad:
        return bad
    a, h, fi = cfg["admission"], cfg["helper_budget"], cfg["fault_injection"]
    keys(a, ADMISSION_KEYS, "admission")
    keys(h, HELPER_KEYS, "helper_budget")
    if bad:
        return bad

    def rng(name, v, lo, hi, lo_open=False):
        if (v <= lo if lo_open else v < lo) or v > hi:
            bad.append("%s=%r outside %s%r, %r]" % (name, v, "(" if lo_open else "[", lo, hi))

    rng("max_chunk_seconds", cfg["max_chunk_seconds"], 0, HARD["max_chunk_max"], True)
    rng("max_wall_s", cfg["max_wall_s"], 0, cfg["max_chunk_seconds"], True)
    rng("settle_s", cfg["settle_s"], 0, 600, True)
    rng("sample_s", cfg["sample_s"], 0.2, 10)
    rng("lane_walk_s", cfg["lane_walk_s"], 1, 600)
    rng("owned_compute_settled_by_epoch", cfg["owned_compute_settled_by_epoch"], 0, 4e9, True)
    rng("rss_trip_bytes", cfg["rss_trip_bytes"], 0, HARD["rss_trip_max"], True)
    rng("rss_projection_bytes", cfg["rss_projection_bytes"], 0, cfg["rss_trip_bytes"])
    rng("free_trip_bytes", cfg["free_trip_bytes"], HARD["free_floor_min"], 1 << 60)
    rng("launch_free_min_bytes", cfg["launch_free_min_bytes"], HARD["launch_free_min_min"], 1 << 60)
    rng("output_trip_bytes", cfg["output_trip_bytes"], 0, HARD["lane_ceiling_max"], True)
    rng("lane_disk_ceiling_bytes", cfg["lane_disk_ceiling_bytes"], 0, HARD["lane_ceiling_max"], True)
    rng("busy_limit", cfg["busy_limit"], 1, HARD["busy_limit_max"])
    rng("busy_cpu_fraction", cfg["busy_cpu_fraction"], 0, 1, True)
    for k in ("stdout_cap_bytes", "stderr_cap_bytes", "samples_cap_bytes"):
        rng(k, cfg[k], 0, 1 << 30, True)
    rng("admission.reservation_bytes", a["reservation_bytes"], 0, HARD["lane_ceiling_max"])
    rng("admission.outstanding_reservations_bytes", a["outstanding_reservations_bytes"], 0, 1 << 60)
    rng("admission.lane_outstanding_reservations_bytes", a["lane_outstanding_reservations_bytes"], 0,
        HARD["lane_ceiling_max"])
    rng("admission.stability_max_age_s", a["stability_max_age_s"], 0, HARD["stability_age_max"], True)
    rng("helper_budget.max_calls", h["max_calls"], 1, 64)
    rng("helper_budget.call_budget_s", h["call_budget_s"], 0, 10, True)
    rng("helper_budget.term_grace_s", h["term_grace_s"], 0, 10, True)
    need = cfg["samples_cap_bytes"] + cfg["stdout_cap_bytes"] + cfg["stderr_cap_bytes"] + cfg["output_trip_bytes"] + \
        RECEIPT_ALLOWANCE_BYTES
    if a["reservation_bytes"] < need:
        bad.append("admission.reservation_bytes below caps + output_trip_bytes + receipt allowance (%d)" % need)
    for k in ("go_path", "stability_receipt_path"):
        if not _norm_abs(a[k]):
            bad.append("admission.%s must be a normalized absolute path" % k)
    for k, v in fi.items():
        if k not in FAULTS or not isinstance(v, bool):
            bad.append("fault_injection entry %r invalid" % k)
    if any(v is True for v in fi.values()) and cfg["purpose"] != "guard-qualification":
        bad.append("fault injection outside guard-qualification")
    if not cfg["argv"] or not all(isinstance(x, str) for x in cfg["argv"]) or not cfg["argv"][0].startswith("/"):
        bad.append("argv must be a non-empty list of strings with an absolute argv[0]")
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in cfg["env"].items()):
        bad.append("env must map str to str")
    elif not _norm_abs(cfg["env"].get("TMPDIR", "")):
        bad.append("env.TMPDIR must be a normalized absolute path")
    for k in ("lane", "lane_disk_root"):
        if not _norm_abs(cfg[k]):
            bad.append("%s must be a normalized absolute path" % k)
    if not cfg["lane_roots"] or not all(_norm_abs(r) for r in cfg["lane_roots"]):
        bad.append("lane_roots must be a non-empty list of normalized absolute paths")
    if bad:
        return bad
    roots = cfg["output_roots"]
    if not roots or not all(_norm_abs(r) for r in roots) or len(set(roots)) != len(roots):
        bad.append("output_roots must be distinct normalized absolute paths")
        return bad
    if under(a["stability_receipt_path"], roots) or under(a["go_path"], roots):
        bad.append("GO and stability receipt must lie outside the output roots")
    for r in roots:
        if not under(r, [cfg["lane_disk_root"]]) or r == cfg["lane_disk_root"]:
            bad.append("output root %s not strictly under lane_disk_root" % r)
        if any(r != q and under(r, [q]) for q in roots):
            bad.append("output root %s nested in another output root" % r)
    if under(cfg["env"]["TMPDIR"], roots) or not under(cfg["env"]["TMPDIR"], [cfg["lane_disk_root"]]):
        bad.append("env.TMPDIR must be under lane_disk_root and outside the output roots")
    for o in cfg["outputs"]:
        if not isinstance(o, dict) or set(o) != {"path", "required"} or not isinstance(o["path"], str) or \
                not isinstance(o["required"], bool):
            bad.append("outputs entries need exactly path (str) and required (bool)")
            return bad
    for p in cfg["pins"]:
        if not isinstance(p, dict) or set(p) != {"path", "sha256"} or not _norm_abs(p.get("path")) or \
                not isinstance(p.get("sha256"), str) or not HEX64.match(p["sha256"]):
            bad.append("pins entries need exactly a normalized absolute path and a sha256")
            return bad
    paths = evidence_paths(cfg) + [o["path"] for o in cfg["outputs"]]
    if not all(_norm_abs(p) for p in paths):
        bad.append("evidence and output paths must be normalized absolute paths")
        return bad
    if len(set(paths)) != len(paths):
        bad.append("evidence and output paths must be distinct")
    for p in paths:
        if os.path.dirname(p) not in roots:
            bad.append("%s is not a direct child of an output root" % p)
        if p == cfg["settlement_record"] + ".staged" or p.endswith(".staged"):
            bad.append("%s uses the reserved .staged suffix" % p)
    return bad


def evidence_paths(cfg):
    return [cfg["stdout"], cfg["stderr"], cfg["launch_record"], cfg["samples"], cfg["receipt"], cfg["settlement_record"]]


# ---------------------------------------------------------------- supervisor state
class Sup:
    def __init__(self, cfg, cfg_path, cfg_sha):
        self.cfg = cfg
        try:
            self_sha = hash_regular(SELF, PIN_MAX_BYTES, HASH_BUDGET_S)[0]
            self_err = None
        except OSError as ex:
            self_sha, self_err = None, repr(ex)
        self.rec = {"supervisor": VERSION, "supervisor_path": SELF, "supervisor_sha256": self_sha,
                    "supervisor_hash_error": self_err, "config": cfg_path, "config_sha256": cfg_sha,
                    "supervisor_pid": MY_PID, "uid": MY_UID, "timebase": TIMEBASE, "argmax": ARGMAX,
                    "authority": "not authoritative until the supervising parent verifies exit code, stdout summary, "
                                 "receipt and settlement sha256 (parent commit)",
                    "clock_note": "mono_* = time.monotonic() s, epoch_* = time.time() s (raw clock values); *_date = "
                                  "/bin/date output or null (never invented)"}
        self.failures, self.failures_n = [], 0
        self.trips, self.tripped = [], set()
        self.stop = None
        self.signal = None
        self.helper_calls = 0
        self.helper_log = []
        self.helper_open = []
        self.keep = []
        self.child = None
        self.child_pid = None
        self.child_rc = None
        self.child_lost = False
        self.child_exit_mono = None
        self.child_exit_epoch = None
        self.ident = None
        self.u0 = None
        self.pgid0 = None
        self.seen = {}
        self.prev_cpu = {}
        self.streams = {}
        self.threads = []
        self.samples_fd = None
        self.samples_bytes = 0
        self.samples_n = 0
        self.samples_dead = False
        self.samples_hash = hashlib.sha256()
        self.root_fds = {}
        self.lane_bytes = None
        self.next_walk = 0.0
        self.max = {"lane_rss": 0, "lane_busy": 0, "blocking_live": 0, "output_bytes": 0, "lane_bytes": 0}
        self.min_free = None
        self.loop_status = "NOT_STARTED"
        self.epoch_spawn = None
        self.census_errors = 0
        self.fit_limit_epoch = None

    # ------------------------------------------------------------ latches
    def fault(self, name):
        return self.cfg["purpose"] == "guard-qualification" and self.cfg["fault_injection"].get(name) is True

    def fail(self, reason):
        self.failures_n += 1
        if len(self.failures) < 200:
            self.failures.append({"reason": str(reason)[:600], "mono": time.monotonic(), "epoch": time.time()})
        if self.child_pid is not None and self.stop is None:
            try:
                self.request_stop("FAILURE")
            except Exception as ex:
                self.failures_n += 1
                self.failures.append({"reason": "REQUEST_STOP_EXCEPTION %r" % ex, "mono": time.monotonic(),
                                      "epoch": time.time()})

    def trip(self, name, detail=None):
        if name in self.tripped:
            return
        self.tripped.add(name)
        if len(self.trips) < 64:
            self.trips.append({"trip": name, "detail": detail, "mono": time.monotonic(), "epoch": time.time()})
        self.request_stop(name)

    def request_stop(self, reason):
        if self.stop is not None:
            return
        self.stop = {"reason": reason, "mono": time.monotonic(), "epoch": time.time()}
        if self.child_pid is not None:
            try:
                self.try_signal()
            except Exception as ex:
                self.signal = {"sent": False, "why_not": "EXCEPTION %r" % ex}
                self.fail("SIGNAL_PATH_EXCEPTION %r" % ex)
        self.stop["date"] = self.date_now()

    # ------------------------------------------------------------ reaping and identity
    def _waitpid(self, pid):
        try:
            got, status = os.waitpid(pid, os.WNOHANG)
        except ChildProcessError:
            return "LOST"
        if got == 0:
            return None
        return os.waitstatus_to_exitcode(status)

    def _wait_bounded(self, pid, budget_s):
        t0 = time.monotonic()
        while True:
            r = self._waitpid(pid)
            if r is not None or time.monotonic() - t0 >= budget_s:
                return r
            time.sleep(0.005)

    def reap_child(self):
        if self.child_pid is None or self.child_rc is not None or self.child_lost:
            return
        r = self._waitpid(self.child_pid)
        if r == "LOST":
            self.child_lost = True
            self.fail("WAIT_STATUS_LOST child %d" % self.child_pid)
        elif r is not None:
            self.child_rc = r
            self.child_exit_mono = time.monotonic()
            self.child_exit_epoch = time.time()

    @staticmethod
    def read_identity(pid):
        ui, e1 = uniq_info(pid)
        si, e2 = short_info(pid)
        if ui is None or si is None:
            return None, "unreadable %r %r" % (e1, e2)
        return {"pid": pid, "uniqueid": ui["uniqueid"], "idversion": ui["idversion"], "pgid": si["pgid"],
                "uid": si["uid"], "comm": si["comm"]}, None

    @staticmethod
    def same_identity(a, b):
        return a is not None and b is not None and all(a[k] == b[k] for k in ("pid", "uniqueid", "idversion", "pgid",
                                                                                "uid"))

    def try_signal(self):
        res = {"mono": time.monotonic(), "sent": False}
        if self.ident is None:
            res["why_not"] = "NO_CHILD_IDENTITY"
        elif self.child_rc is not None:
            res["why_not"] = "CHILD_ALREADY_REAPED"
        elif self.child_lost:
            res["why_not"] = "WAIT_STATUS_LOST"
        elif self.fault("identity_check_fails"):
            res["why_not"] = "FAULT_INJECTED_IDENTITY_FAILURE"
            self.signal = res
            self.fail("IDENTITY_UNVERIFIED fault injected")
            return
        else:
            now_id, why = self.read_identity(self.child_pid)
            ok = self.same_identity(now_id, self.ident) and self.child_rc is None and not self.child_lost
            res["identity_ok"] = ok
            if ok:
                try:
                    os.killpg(self.ident["pgid"], signal.SIGTERM)
                    res["sent"] = True
                    res["mono_sent"] = time.monotonic()
                except ProcessLookupError as ex:
                    res["error"] = repr(ex)
                except OSError as ex:
                    res["error"] = repr(ex)
                    self.signal = res
                    self.fail("SIGNAL_FAILED %r" % ex)
                    return
            else:
                res["why_not"] = "IDENTITY_MISMATCH_OR_UNREADABLE %s" % (why or now_id)
                self.signal = res
                self.fail("IDENTITY_UNVERIFIED %s" % res["why_not"])
                return
        self.signal = res

    # ------------------------------------------------------------ /bin/date helper
    def date_now(self):
        hb = self.cfg["helper_budget"]
        entry = {"n": len(self.helper_log) + 1, "mono_start": time.monotonic()}
        try:
            if self.failures_n:
                entry["outcome"] = "SKIPPED_AFTER_FAILURE_LATCH"
                return None
            if self.fault("date_helper_fails"):
                entry["outcome"] = "FAULT_INJECTED"
                self.fail("HELPER_FAULT_INJECTED")
                return None
            if self.fit_limit_epoch is not None and time.time() > self.fit_limit_epoch:
                entry["outcome"] = "REFUSED_PAST_CHUNK_LIMIT"
                self.fail("HELPER_REFUSED_PAST_CHUNK_LIMIT")
                return None
            if self.helper_calls >= hb["max_calls"]:
                entry["outcome"] = "BUDGET_EXHAUSTED"
                self.fail("HELPER_BUDGET_EXHAUSTED")
                return None
            self.helper_calls += 1
            try:
                p = subprocess.Popen(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], stdin=subprocess.DEVNULL,
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env={"PATH": "/usr/bin:/bin"},
                                     start_new_session=True, close_fds=True, cwd="/")
            except (OSError, ValueError, subprocess.SubprocessError) as ex:
                entry["outcome"] = "SPAWN_FAILED %r" % ex
                self.fail("HELPER_SPAWN_FAILED %r" % ex)
                return None
            self.keep.append(p)
            entry["pid"] = p.pid
            ident, why = self.read_identity(p.pid)
            entry["identity"] = ident
            rc = self._wait_bounded(p.pid, hb["call_budget_s"])
            if rc is None:
                sent = False
                now_id, _ = self.read_identity(p.pid)
                if ident is not None and ident["pgid"] == p.pid and ident["uid"] == MY_UID and \
                        self.same_identity(now_id, ident):
                    try:
                        os.killpg(p.pid, signal.SIGTERM)
                        sent = True
                    except OSError as ex:
                        entry["sigterm_error"] = repr(ex)
                entry["sigterm"] = sent
                rc = self._wait_bounded(p.pid, hb["term_grace_s"])
                if rc is None:
                    entry["outcome"] = "HELPER_UNSETTLED"
                    self.helper_open.append(p.pid)
                    self.fail("HELPER_UNSETTLED %d" % p.pid)
                    return None
            if rc == "LOST":
                entry["outcome"] = "WAIT_STATUS_LOST"
                self.fail("WAIT_STATUS_LOST helper %d" % p.pid)
                return None
            members = pgrp_members(p.pid)
            entry["group_after_reap"] = members
            if members is None or members:
                entry["outcome"] = "HELPER_GROUP_LIVE_OR_UNREADABLE"
                self.fail("HELPER_GROUP_LIVE_OR_UNREADABLE %d %r" % (p.pid, members))
                return None
            fd = p.stdout.fileno()
            os.set_blocking(fd, False)
            try:
                out = os.read(fd, 257)
            except BlockingIOError:
                out = b""
            finally:
                p.stdout.close()
            txt = out.decode("utf-8", "replace").strip()
            entry.update({"rc": rc, "mono_end": time.monotonic()})
            if rc != 0 or len(out) > 256 or not DATE_RE.match(txt):
                entry["outcome"] = "BAD_OUTPUT"
                self.fail("HELPER_BAD_OUTPUT rc %r" % rc)
                return None
            entry["outcome"] = "OK"
            return txt
        except Exception as ex:
            entry["outcome"] = "EXCEPTION %r" % ex
            self.fail("HELPER_EXCEPTION %r" % ex)
            return None
        finally:
            if len(self.helper_log) < 256:
                self.helper_log.append(entry)

    # ------------------------------------------------------------ census
    def _proc(self, pid):
        """(record, None) or (None, errno); rechecks the uniqueid so the two reads describe one process."""
        for _ in range(3):
            u1, e = uniq_info(pid)
            if u1 is None:
                return None, e
            si, e = short_info(pid)
            if si is None:
                return None, e
            u2, e = uniq_info(pid)
            if u2 is None:
                return None, e
            if u1 == u2:
                si.update(u1)
                return si, 0
        return None, -8

    def _class(self, u, memo):
        chain, cur = [], u
        while True:
            if cur in memo:
                res = memo[cur]
                break
            if cur == self.u0:
                res = "OWNED"
                break
            if cur < self.u0:
                res = "OTHER"
                break
            ent = self.seen.get(cur)
            if ent is None:
                res = "UNRESOLVED"
                break
            chain.append(cur)
            cur = ent["puniqueid"]
            if len(chain) > SEEN_MAX:
                res = "UNRESOLVED"
                break
        for c in chain:
            memo[c] = res
        memo[u] = res
        return res

    def census(self):
        """one complete scan; raises RuntimeError on any failure (fail-closed)."""
        pids = list_pids()
        if pids is None:
            raise RuntimeError("LISTPIDS_FAILED")
        procs = {}
        for pid in pids:
            if pid <= 0:
                continue
            p, e = self._proc(pid)
            if p is None:
                if e == errno.ESRCH:
                    continue
                raise RuntimeError("PROCINFO pid %d errno %d" % (pid, e))
            procs[pid] = p
            if p["uniqueid"] not in self.seen:
                if len(self.seen) >= SEEN_MAX:
                    raise RuntimeError("SEEN_TABLE_FULL")
                self.seen[p["uniqueid"]] = {"pid": pid, "puniqueid": p["puniqueid"], "comm": p["comm"],
                                            "uid": p["uid"]}
        memo = {}
        for p in procs.values():
            p["class"] = "OTHER" if self.u0 is None else self._class(p["uniqueid"], memo)
            p["blocking"] = p["class"] in ("OWNED", "UNRESOLVED") or (self.pgid0 is not None and p["pgid"] == self.pgid0)
        roots = self.cfg["lane_roots"]
        frac = self.cfg["busy_cpu_fraction"]
        now_m, now_e = time.monotonic(), time.time()
        lane, other_uid_blocking, cpu_now = {}, [], {}
        for pid, p in procs.items():
            if p["uid"] != MY_UID:
                if p["blocking"]:
                    other_uid_blocking.append(pid)
                continue
            if p["status"] == SZOMB:
                continue
            member = p["blocking"]
            if not member:
                cw, e1 = cwd_of(pid)
                if cw is not None and under(cw, roots):
                    member = True
                else:
                    av, e2 = argv_of(pid)
                    if av is not None and any(r in x for x in av for r in roots):
                        member = True
                    elif cw is None or av is None:
                        if (cw is None and e1 == errno.ESRCH) or (av is None and e2 == errno.ESRCH):
                            continue
                        raise RuntimeError("UNREADABLE_SAME_UID pid %d comm %s cwd_err %r argv_err %r" %
                                           (pid, p["comm"], None if cw is not None else e1,
                                            None if av is not None else e2))
            if not member:
                continue
            ti, e = task_info(pid)
            if ti is None:
                if e == errno.ESRCH:
                    continue
                raise RuntimeError("TASKINFO lane pid %d errno %d" % (pid, e))
            u = p["uniqueid"]
            prev = self.prev_cpu.get(u)
            if prev is None:
                st, e = bsd_start(pid)
                if st is None:
                    if e == errno.ESRCH:
                        continue
                    raise RuntimeError("BSDINFO lane pid %d errno %d" % (pid, e))
                age = now_e - st
                ns = ti["cpu_ticks"] * TIMEBASE[0] / TIMEBASE[1]
                busy = age <= 0.05 or ns >= frac * age * 1e9
            else:
                dt = now_m - prev[0]
                ns = (ti["cpu_ticks"] - prev[1]) * TIMEBASE[0] / TIMEBASE[1]
                busy = dt <= 0 or ns >= frac * dt * 1e9
            cpu_now[u] = (now_m, ti["cpu_ticks"])
            lane[pid] = {"rss": ti["rss"], "busy": busy, "class": p["class"]}
        self.prev_cpu = cpu_now
        blocking = sorted(pid for pid, p in procs.items() if p["blocking"])
        unresolved = [[pid, procs[pid]["comm"], procs[pid]["uniqueid"], procs[pid]["puniqueid"]]
                      for pid in blocking if procs[pid]["class"] == "UNRESOLVED"]
        return {"pids": len(procs), "seen": len(self.seen), "blocking_live": blocking,
                "owned_live": sorted(pid for pid in blocking if procs[pid]["class"] == "OWNED"),
                "unresolved_live": sorted(x[0] for x in unresolved), "unresolved_detail": unresolved[:20],
                "group_live": sorted(pid for pid in blocking if self.pgid0 is not None and procs[pid]["pgid"] == self.pgid0),
                "blocking_zombies": sorted(pid for pid in blocking if procs[pid]["status"] == SZOMB),
                "other_uid_blocking": sorted(other_uid_blocking), "lane_pids": sorted(lane),
                "lane_rss": sum(v["rss"] for v in lane.values()),
                "lane_busy": sum(1 for v in lane.values() if v["busy"])}

    def streams_closed(self):
        return len(self.streams) == 2 and all(st["closed"] for st in self.streams.values())

    def is_clear(self, c):
        return c is not None and self.child_rc is not None and not c["blocking_live"] and self.streams_closed()

    # ------------------------------------------------------------ evidence files
    def root_for(self, path):
        d = os.path.dirname(path)
        return self.root_fds[d][0], os.path.basename(path)

    def open_roots(self):
        for r in self.cfg["output_roots"]:
            fd = os.open(r, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            st = os.fstat(fd)
            self.root_fds[r] = (fd, st.st_dev, st.st_ino)

    def write_sample(self, obj):
        if self.samples_fd is None or self.samples_dead:
            return
        try:
            line = (json.dumps(obj, sort_keys=True, allow_nan=False, default=repr) + "\n").encode("utf-8")
            if self.samples_bytes + len(line) > self.cfg["samples_cap_bytes"]:
                self.samples_dead = True
                self.fail("SAMPLES_CAP")
                return
            write_all(self.samples_fd, line, time.monotonic() + 10.0)
            self.samples_hash.update(line)
            self.samples_bytes += len(line)
            self.samples_n += 1
        except Exception as ex:
            self.samples_dead = True
            self.fail("SAMPLES_WRITE_FAILED %r" % ex)


def sink_thread(name, pipe, dirfd, fname, cap, sup):
    st = {"bytes_seen": 0, "bytes_written": 0, "overflow": False, "closed": False, "error": None, "eof": False,
          "sha256_written": None}
    digest = hashlib.sha256()
    sup.streams[name] = st

    def run():
        fd = None
        try:
            fd = os.open(fname, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dirfd)
            while True:
                chunk = pipe.read1(65536)
                if not chunk:
                    st["eof"] = True
                    break
                st["bytes_seen"] += len(chunk)
                room = cap - st["bytes_written"]
                if room > 0:
                    part = chunk[:room]
                    write_all(fd, part, time.monotonic() + 30.0)
                    digest.update(part)
                    st["bytes_written"] += len(part)
                if len(chunk) > max(room, 0):
                    st["overflow"] = True
        except BaseException as ex:
            st["error"] = repr(ex)
            try:
                while True:
                    chunk = pipe.read1(65536)
                    if not chunk:
                        break
                    st["bytes_seen"] += len(chunk)
                    st["overflow"] = True
            except BaseException:
                pass
        finally:
            try:
                if fd is not None:
                    os.fsync(fd)
                    os.close(fd)
                pipe.close()
                st["sha256_written"] = digest.hexdigest()
                st["closed"] = True
            except BaseException as ex:
                st["error"] = (st["error"] or "") + " close: %r" % ex
    t = threading.Thread(target=run, name="sink-" + name, daemon=True)
    t.start()
    return t


# ---------------------------------------------------------------- admission and commit boundary
def _stability_age(date, now_date):
    return (datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
            - datetime.datetime.strptime(now_date, "%Y-%m-%dT%H:%M:%S%z")).total_seconds()


def admission(sup):
    cfg, adm, R, reasons = sup.cfg, sup.cfg["admission"], {}, []
    R["date"] = sup.date_now()
    if R["date"] is None:
        reasons.append("DATE_HELPER_UNAVAILABLE")
    if TIMEBASE is None or ARGMAX is None:
        reasons.append("LIBPROC_SETUP_FAILED")
    if sup.rec["supervisor_sha256"] is None:
        reasons.append("SUPERVISOR_SOURCE_UNHASHABLE")
    pins = []
    for p in cfg["pins"]:
        try:
            ok = hash_regular(p["path"], PIN_MAX_BYTES, HASH_BUDGET_S)[0] == p["sha256"]
        except OSError:
            ok = False
        pins.append([p["path"], ok])
        if not ok:
            reasons.append("PIN_MISMATCH %s" % p["path"])
    R["pins"] = pins
    for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
        try:
            st = os.lstat(r)
            names = os.listdir(fd)
        except OSError as ex:
            reasons.append("OUTPUT_ROOT_UNREADABLE %s %r" % (r, ex))
            continue
        if (st.st_dev, st.st_ino) != (dev, ino) or not real_dir_chain(r):
            reasons.append("OUTPUT_ROOT_NOT_REAL_DIR %s" % r)
        if names:
            reasons.append("OUTPUT_ROOT_NOT_EMPTY %s (%d entries)" % (r, len(names)))
    tmpd = cfg["env"]["TMPDIR"]
    if not real_dir_chain(tmpd):
        reasons.append("TMPDIR_NOT_REAL_DIR %s" % tmpd)
    if not real_dir_chain(cfg["lane"]) or not real_dir_chain(cfg["lane_disk_root"]):
        reasons.append("LANE_DIR_NOT_REAL_DIR")
    try:
        gh, _, graw, _ = hash_regular(adm["go_path"], SMALL_MAX_BYTES, HASH_BUDGET_S, keep=True)
        R["go_sha256"] = gh
        g = strict_json(graw)
        entry = g.get("configs", {}).get(sup.rec["config_sha256"]) if isinstance(g, dict) and \
            isinstance(g.get("configs"), dict) else None
        if not isinstance(g, dict) or g.get("decision") != "GO" or g.get("item") != cfg["item"]:
            reasons.append("GO_NOT_FOR_THIS_ITEM")
        elif not isinstance(entry, dict):
            reasons.append("GO_DOES_NOT_NAME_THIS_CONFIG")
        else:
            bound = {"output_roots": cfg["output_roots"], "argv": cfg["argv"], "max_wall_s": cfg["max_wall_s"]}
            bound.update({k: adm[k] for k in GO_BOUND_KEYS[3:]})
            for k in GO_BOUND_KEYS:
                if k not in entry or entry[k] != bound[k] or type(entry[k]) is bool:
                    reasons.append("GO_BINDING_MISMATCH %s" % k)
            na = g.get("not_after_epoch")
            if not _num(na):
                reasons.append("GO_EXPIRY_INVALID")
            else:
                R["go_not_after_epoch"] = na
                if time.time() > na:
                    reasons.append("GO_EXPIRED")
    except (OSError, ValueError, UnicodeDecodeError) as ex:
        reasons.append("GO_UNREADABLE %r" % ex)
    try:
        sh, _, sraw, _ = hash_regular(adm["stability_receipt_path"], SMALL_MAX_BYTES, HASH_BUDGET_S, keep=True)
        R["stability_sha256"] = sh
        sr = strict_json(sraw)
        if not isinstance(sr, dict) or sr.get("verdict") != "PASS":
            reasons.append("STABILITY_NOT_PASS")
        nd = sr.get("now_date") if isinstance(sr, dict) else None
        if R["date"] is None or not isinstance(nd, str) or not DATE_RE.match(nd):
            reasons.append("STABILITY_AGE_UNVERIFIABLE")
        else:
            R["stability_now_date"] = nd
            R["stability_age_s"] = _stability_age(R["date"], nd)
            if not (0 <= R["stability_age_s"] <= adm["stability_max_age_s"]):
                reasons.append("STABILITY_STALE")
    except (OSError, ValueError, UnicodeDecodeError) as ex:
        reasons.append("STABILITY_UNREADABLE %r" % ex)
    res = adm["reservation_bytes"]
    try:
        fr = free_bytes(cfg["lane"])
        R["free"] = fr
        if fr < cfg["launch_free_min_bytes"] + res:
            reasons.append("FREE_BELOW_LAUNCH_MIN")
        if fr - adm["outstanding_reservations_bytes"] - res < HARD["free_floor_min"]:
            reasons.append("FREE_MINUS_RESERVATIONS_BELOW_12E9")
    except OSError as ex:
        reasons.append("STATVFS_FAILED %r" % ex)
    try:
        lb = walk_bytes(cfg["lane_disk_root"])
        R["lane_bytes"] = lb
        if lb + adm["lane_outstanding_reservations_bytes"] + res > cfg["lane_disk_ceiling_bytes"]:
            reasons.append("LANE_CEILING")
    except OSError as ex:
        reasons.append("LANE_WALK_FAILED %r" % ex)
    w0 = time.time()
    R["epoch_admission"] = w0
    R["fit_limit_epoch"] = min(w0 + cfg["max_chunk_seconds"] - 120, cfg["owned_compute_settled_by_epoch"] - 180)
    sup.fit_limit_epoch = R["fit_limit_epoch"]
    if w0 + cfg["max_wall_s"] + cfg["settle_s"] + FINALIZE_ALLOWANCE_S > R["fit_limit_epoch"]:
        reasons.append("CHUNK_FIT")
    if TIMEBASE is not None and ARGMAX is not None:
        try:
            sup.census()
            time.sleep(2.0)
            c2 = sup.census()
            R["census"] = {k: c2[k] for k in ("pids", "lane_pids", "lane_rss", "lane_busy")}
            if c2["lane_busy"] + 1 > cfg["busy_limit"]:
                reasons.append("LANE_BUSY")
            if c2["lane_rss"] + cfg["rss_projection_bytes"] > cfg["rss_trip_bytes"]:
                reasons.append("LANE_RSS")
        except RuntimeError as ex:
            reasons.append("CENSUS_FAILED %s" % ex)
    if CANCEL[0] is not None:
        reasons.append("CANCELLED %d" % CANCEL[0])
    if sup.failures_n:
        reasons.append("FAILURE_LATCHED")
    R["reasons"] = reasons
    return R


def commit_boundary(sup, adm_rec):
    cfg, adm, R, reasons = sup.cfg, sup.cfg["admission"], {}, []
    R["date"] = sup.date_now()
    if R["date"] is None:
        reasons.append("DATE_HELPER_UNAVAILABLE")
    else:
        try:
            R["stability_age_s"] = _stability_age(R["date"], adm_rec["stability_now_date"])
            if not (0 <= R["stability_age_s"] <= adm["stability_max_age_s"]):
                reasons.append("STABILITY_STALE")
        except (KeyError, ValueError) as ex:
            reasons.append("STABILITY_AGE_UNVERIFIABLE %r" % ex)
    res = adm["reservation_bytes"]
    try:
        fr = free_bytes(cfg["lane"])
        R["free"] = fr
        if fr < cfg["launch_free_min_bytes"] + res or fr - adm["outstanding_reservations_bytes"] - res < \
                HARD["free_floor_min"]:
            reasons.append("FREE_BELOW_LAUNCH_MIN")
    except OSError as ex:
        reasons.append("STATVFS_FAILED %r" % ex)
    w = time.time()
    R["epoch"] = w
    if w + cfg["max_wall_s"] + cfg["settle_s"] + FINALIZE_ALLOWANCE_S > adm_rec["fit_limit_epoch"]:
        reasons.append("CHUNK_FIT")
    if not _num(adm_rec.get("go_not_after_epoch")) or w > adm_rec["go_not_after_epoch"]:
        reasons.append("GO_EXPIRED_OR_INVALID")
    if CANCEL[0] is not None:
        reasons.append("CANCELLED %d" % CANCEL[0])
    if sup.failures_n:
        reasons.append("FAILURE_LATCHED")
    R["reasons"] = reasons
    return R


# ---------------------------------------------------------------- supervised run
def run_supervised(sup, child, mono0, epoch0, abs_end):
    cfg = sup.cfg
    ident, why = sup.read_identity(child.pid)
    if ident is None or ident["pgid"] != child.pid or ident["uid"] != MY_UID:
        sup.fail("IDENTITY_CAPTURE_FAILED %s" % (why or ident))
    else:
        sup.ident, sup.u0, sup.pgid0 = ident, ident["uniqueid"], ident["pgid"]
    fd_out, n_out = sup.root_for(cfg["stdout"])
    fd_err, n_err = sup.root_for(cfg["stderr"])
    sup.threads = [sink_thread("stdout", child.stdout, fd_out, n_out, cfg["stdout_cap_bytes"], sup),
                   sink_thread("stderr", child.stderr, fd_err, n_err, cfg["stderr_cap_bytes"], sup)]
    if sup.ident is not None:
        launch = {"item": cfg["item"], "owner": cfg["owner"], "purpose": cfg["purpose"], "identity": sup.ident,
                  "argv": cfg["argv"], "argv_sha256": hashlib.sha256(json.dumps(cfg["argv"]).encode()).hexdigest(),
                  "argv0_realpath": os.path.realpath(cfg["argv"][0]), "cwd": cfg["lane"], "env": cfg["env"],
                  "start_date": sup.rec.get("start_date"), "mono_spawn": mono0, "epoch_spawn": epoch0,
                  "abs_end_epoch": abs_end, "max_wall_s": cfg["max_wall_s"], "settle_s": cfg["settle_s"],
                  "pins": cfg["pins"], "admission": sup.rec["admission"], "commit_boundary": sup.rec["commit_boundary"],
                  "go": {"path": cfg["admission"]["go_path"], "sha256": sup.rec["admission"].get("go_sha256"),
                         "not_after_epoch": sup.rec["admission"].get("go_not_after_epoch")},
                  "stability_receipt": {"path": cfg["admission"]["stability_receipt_path"],
                                        "sha256": sup.rec["admission"].get("stability_sha256")},
                  "reservation_bytes": cfg["admission"]["reservation_bytes"], "outputs": cfg["outputs"],
                  "evidence": {k: cfg[k] for k in ("stdout", "stderr", "samples", "receipt", "settlement_record")},
                  "supervisor": VERSION, "supervisor_sha256": sup.rec["supervisor_sha256"], "supervisor_pid": MY_PID,
                  "config_sha256": sup.rec["config_sha256"], "fault_injection": cfg["fault_injection"]}
        try:
            fd, name = sup.root_for(cfg["launch_record"])
            sup.rec["launch_record_sha256"] = publish(fd, name, jbytes(launch))
        except Exception as ex:
            sup.fail("LAUNCH_RECORD_FAILED %r" % ex)
    census_ok = False
    try:
        c = sup.census()
        sup.rec["pre_go_census"] = {k: c[k] for k in ("pids", "blocking_live", "lane_pids", "lane_rss", "lane_busy")}
        census_ok = True
    except RuntimeError as ex:
        sup.fail("CENSUS_FAILED pre-GO %s" % ex)
    go = (sup.ident is not None and "launch_record_sha256" in sup.rec and census_ok and not sup.failures_n and
          CANCEL[0] is None and time.time() - epoch0 <= GO_MAX_DELAY_S and sup.stop is None)
    sup.rec["go_decision"] = go
    try:
        if go:
            child.stdin.write(b"GO\n")
            child.stdin.flush()
            sup.rec["go_written_mono"] = time.monotonic()
    except Exception as ex:
        sup.rec["go_error"] = repr(ex)
        go = False
    for _ in range(2):
        try:
            child.stdin.close()
        except Exception as ex:
            sup.rec["stdin_close_error"] = repr(ex)
    sup.rec["stdin_closed"] = bool(child.stdin.closed)
    sup.rec["go_delivered"] = bool(go and child.stdin.closed)
    if not sup.rec["go_delivered"]:
        sup.fail("GO_NOT_DELIVERED")
    sup.loop_status = "RUNNING"
    while True:
        sup.reap_child()
        if CANCEL[0] is not None:
            sup.trip("SUPERVISOR_CANCEL_%d" % CANCEL[0])
        try:
            c = sup.census()
            sup.max["lane_rss"] = max(sup.max["lane_rss"], c["lane_rss"])
            sup.max["lane_busy"] = max(sup.max["lane_busy"], c["lane_busy"])
            sup.max["blocking_live"] = max(sup.max["blocking_live"], len(c["blocking_live"]))
        except RuntimeError as ex:
            c = None
            sup.census_errors += 1
            sup.fail("CENSUS_FAILED %s" % str(ex)[:400])
        fr = ob = None
        try:
            fr = free_bytes(cfg["lane"])
            sup.min_free = fr if sup.min_free is None else min(sup.min_free, fr)
        except OSError as ex:
            sup.fail("FREE_UNREADABLE %r" % ex)
        try:
            ob = 0
            for o in cfg["outputs"]:
                fd, name = sup.root_for(o["path"])
                try:
                    ob += os.stat(name, dir_fd=fd, follow_symlinks=False).st_size
                except FileNotFoundError:
                    pass
            ob += sum(st["bytes_written"] for st in sup.streams.values()) + sup.samples_bytes
            sup.max["output_bytes"] = max(sup.max["output_bytes"], ob)
        except OSError as ex:
            ob = None
            sup.fail("OUTPUT_UNREADABLE %r" % ex)
        if time.monotonic() >= sup.next_walk:
            try:
                sup.lane_bytes = walk_bytes(cfg["lane_disk_root"])
                sup.max["lane_bytes"] = max(sup.max["lane_bytes"], sup.lane_bytes)
            except OSError as ex:
                sup.fail("LANE_WALK_FAILED %r" % ex)
            sup.next_walk = time.monotonic() + cfg["lane_walk_s"]
        for name, st in sup.streams.items():
            if st["error"] is not None and not st.get("error_reported"):
                st["error_reported"] = True
                sup.fail("STREAM_%s_ERROR %s" % (name.upper(), st["error"][:200]))
        if c is not None and c["lane_rss"] > cfg["rss_trip_bytes"]:
            sup.trip("RSS", c["lane_rss"])
        if c is not None and c["lane_busy"] > cfg["busy_limit"]:
            sup.trip("BUSY", c["lane_busy"])
        if fr is not None and fr < cfg["free_trip_bytes"]:
            sup.trip("FREE", fr)
        if ob is not None and ob > cfg["output_trip_bytes"]:
            sup.trip("OUTPUT", ob)
        if any(st["overflow"] for st in sup.streams.values()):
            sup.trip("STREAM_CAP")
        if sup.lane_bytes is not None and ob is not None:
            unused = max(0, cfg["admission"]["reservation_bytes"] - ob)
            if sup.lane_bytes + cfg["admission"]["lane_outstanding_reservations_bytes"] + unused > \
                    cfg["lane_disk_ceiling_bytes"]:
                sup.trip("LANE_CEILING", sup.lane_bytes)
        sup.reap_child()
        if sup.child_rc is None and (time.monotonic() - mono0 > cfg["max_wall_s"] or time.time() > abs_end):
            sup.trip("DEADLINE")
        sup.write_sample({"mono": time.monotonic(), "epoch": time.time(), "rc": sup.child_rc, "free": fr, "out": ob,
                          "lane_bytes": sup.lane_bytes,
                          "census": None if c is None else {k: c[k] for k in (
                              "pids", "blocking_live", "owned_live", "unresolved_live", "group_live",
                              "blocking_zombies", "other_uid_blocking", "lane_pids", "lane_rss", "lane_busy")},
                          "streams": {k: [v["bytes_seen"], v["bytes_written"], v["overflow"], v["closed"]]
                                      for k, v in sup.streams.items()},
                          "stop": None if sup.stop is None else sup.stop["reason"], "trips_n": len(sup.trips),
                          "failures_n": sup.failures_n, "signal_sent": bool(sup.signal and sup.signal.get("sent"))})
        if sup.is_clear(c):
            sup.loop_status = "EXITED"
            return
        t = time.monotonic()
        if sup.stop is not None and t - sup.stop["mono"] > cfg["settle_s"]:
            sup.loop_status = "GRACE_EXPIRED_AFTER_STOP_REQUEST"
            sup.fail("GRACE_EXPIRED_AFTER_STOP_REQUEST")
            return
        if sup.child_exit_mono is not None and t - sup.child_exit_mono > cfg["settle_s"]:
            sup.loop_status = "GRACE_EXPIRED_AFTER_CHILD_EXIT"
            sup.fail("GRACE_EXPIRED_AFTER_CHILD_EXIT")
            return
        time.sleep(cfg["sample_s"])


def emergency_observe(sup):
    """after an exception: stop requested; observe (reap + census only) until clear or the grace has expired."""
    cfg = sup.cfg
    if sup.stop is None:
        sup.request_stop("SUPERVISOR_EXCEPTION")
    while True:
        sup.reap_child()
        try:
            c = sup.census()
        except Exception as ex:
            c = None
            sup.census_errors += 1
            if sup.census_errors <= 3:
                sup.fail("CENSUS_FAILED after exception %s" % str(ex)[:200])
        if sup.is_clear(c):
            sup.loop_status = "EXITED_AFTER_EXCEPTION"
            return
        if time.monotonic() - sup.stop["mono"] > cfg["settle_s"]:
            sup.loop_status = "GRACE_EXPIRED_AFTER_EXCEPTION"
            sup.fail("GRACE_EXPIRED_AFTER_EXCEPTION")
            return
        time.sleep(cfg["sample_s"])


# ---------------------------------------------------------------- finalization and publication
def finalize(sup, status_note):
    try:
        return _finalize(sup, status_note)
    except BaseException as ex:
        sys.stderr.write("FINALIZE_EXCEPTION %r\n" % ex)
        try:
            fd, name = sup.root_for(sup.cfg["settlement_record"])
            h, _ = publish_linked(fd, name, jbytes({"settlement": "UNSETTLED", "supervisor": VERSION,
                                                     "config_sha256": sup.rec.get("config_sha256"),
                                                     "receipt": None, "receipt_sha256": None,
                                                     "reasons": ["FINALIZE_EXCEPTION %r" % ex]}))
            sys.stdout.write(json.dumps({"settlement": "UNSETTLED", "settlement_record_sha256": h,
                                         "receipt_sha256": None, "reasons": ["FINALIZE_EXCEPTION"]}) + "\n")
        except BaseException as ex2:
            sys.stderr.write("SETTLEMENT_RECORD_FAILED %r\n" % ex2)
            return 13
        return 12


def _finalize(sup, status_note):
    cfg, R = sup.cfg, sup.rec
    launched = sup.child_pid is not None
    end_date = sup.date_now()
    for pid in list(sup.helper_open):
        r = sup._waitpid(pid)
        if r is not None and r != "LOST":
            sup.helper_open.remove(pid)
    if sup.helper_open:
        sup.fail("HELPER_ALIVE %s" % sup.helper_open)
    if launched:
        sup.reap_child()
        if sup.child_rc is None:
            sup.fail("CHILD_NOT_REAPED")
        try:
            c = sup.census()
            R["final_census"] = c
            if c["blocking_live"]:
                sup.fail("BLOCKING_LIVE owned %s unresolved %s group %s" % (c["owned_live"], c["unresolved_live"],
                                                                            c["group_live"]))
        except RuntimeError as ex:
            sup.fail("FINAL_CENSUS_FAILED %s" % ex)
        if not sup.streams_closed():
            sup.fail("STREAMS_NOT_CLOSED")
        for name, st in sorted(sup.streams.items()):
            if st["error"] is not None:
                sup.fail("STREAM_%s_ERROR %s" % (name.upper(), st["error"][:200]))
        if any(t.is_alive() for t in sup.threads) or len(sup.threads) != 2:
            sup.fail("SINK_THREADS_NOT_FINISHED")
    if sup.samples_fd is not None:
        try:
            os.fsync(sup.samples_fd)
            os.close(sup.samples_fd)
        except OSError as ex:
            sup.fail("SAMPLES_CLOSE_FAILED %r" % ex)
        sup.samples_fd = None
    pins_end = []
    for p in cfg["pins"]:
        try:
            pins_end.append([p["path"], hash_regular(p["path"], PIN_MAX_BYTES, HASH_BUDGET_S)[0] == p["sha256"]])
        except OSError:
            pins_end.append([p["path"], False])
    R["pins_at_end"] = pins_end
    if not all(ok for _, ok in pins_end):
        sup.fail("PIN_CHANGED_OR_UNREADABLE")
    allowed = {os.path.basename(p) for p in evidence_paths(cfg) + [o["path"] for o in cfg["outputs"]]}
    allowed.add(os.path.basename(cfg["settlement_record"]) + ".staged")
    inventory = {}
    for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
        try:
            st_fd, st_path = os.fstat(fd), os.lstat(r)
            names = os.listdir(fd)
        except OSError as ex:
            sup.fail("OUTPUT_ROOT_UNREADABLE %s %r" % (r, ex))
            continue
        if (st_fd.st_dev, st_fd.st_ino) != (dev, ino) or (st_path.st_dev, st_path.st_ino) != (dev, ino) or \
                not real_dir_chain(r):
            sup.fail("OUTPUT_ROOT_CHANGED %s" % r)
        inventory[r] = sorted(names)[:ROOT_MAX_ENTRIES]
        stray = sorted(n for n in names if n not in allowed)
        if stray:
            sup.fail("UNDECLARED_ENTRIES %s %s" % (r, stray[:20]))
    R["output_root_inventory"] = inventory
    arts = {}
    for p in [cfg["stdout"], cfg["stderr"], cfg["launch_record"], cfg["samples"]] + [o["path"] for o in cfg["outputs"]]:
        fd, name = sup.root_for(p)
        try:
            st = os.stat(name, dir_fd=fd, follow_symlinks=False)
        except FileNotFoundError:
            arts[p] = None
            continue
        except OSError as ex:
            arts[p] = {"error": repr(ex)}
            sup.fail("ARTIFACT_STAT_FAILED %s" % p)
            continue
        try:
            h, size, _, st2 = hash_regular(name, max(cfg["output_trip_bytes"], 1 << 30), HASH_BUDGET_S, dir_fd=fd)
            arts[p] = {"bytes": size, "sha256": h, "nlink": st2.st_nlink, "birthtime": st2.st_birthtime}
            if st2.st_nlink != 1:
                sup.fail("ARTIFACT_LINK_COUNT %s %d" % (p, st2.st_nlink))
            if sup.epoch_spawn is not None and st2.st_birthtime < sup.epoch_spawn - 2.0:
                sup.fail("ARTIFACT_OLDER_THAN_SPAWN %s" % p)
        except OSError as ex:
            arts[p] = {"error": repr(ex)}
            sup.fail("ARTIFACT_HASH_FAILED %s %r" % (p, ex))
    R["artifacts"] = arts
    expected = {}
    if R.get("launch_record_sha256"):
        expected[cfg["launch_record"]] = R["launch_record_sha256"]
    if launched and R.get("samples_opened"):
        expected[cfg["samples"]] = sup.samples_hash.hexdigest()
    for name, p in (("stdout", cfg["stdout"]), ("stderr", cfg["stderr"])):
        st_ = sup.streams.get(name)
        if st_ is not None and st_.get("sha256_written"):
            expected[p] = st_["sha256_written"]
    R["evidence_expected_sha256"] = expected
    for p, h in sorted(expected.items()):
        a = arts.get(p)
        if not isinstance(a, dict) or a.get("sha256") != h:
            sup.fail("EVIDENCE_MUTATED %s" % p)
    if launched:
        for o in cfg["outputs"]:
            if o["required"] and arts.get(o["path"]) is None:
                sup.fail("REQUIRED_OUTPUT_MISSING %s" % o["path"])
        for p in (cfg["launch_record"], cfg["samples"], cfg["stdout"], cfg["stderr"]):
            if arts.get(p) is None:
                sup.fail("EVIDENCE_MISSING %s" % p)
    try:
        fr = free_bytes(cfg["lane"])
        R["final_free"] = fr
        if fr < cfg["free_trip_bytes"]:
            sup.fail("FINAL_FREE_BELOW_FLOOR %d" % fr)
    except OSError as ex:
        sup.fail("FINAL_FREE_UNREADABLE %r" % ex)
    if launched and R.get("abs_end_epoch") is not None:
        bound = R["abs_end_epoch"] + cfg["sample_s"] + DEADLINE_SLACK_EXTRA_S
        dl = next((t for t in sup.trips if t["trip"] == "DEADLINE"), None)
        exit_ok = sup.child_exit_epoch is not None and sup.child_exit_epoch <= bound
        trip_ok = dl is not None and dl["epoch"] <= bound
        R["deadline_timeliness"] = {"bound_epoch": bound, "exit_observed_epoch": sup.child_exit_epoch,
                                    "deadline_trip_epoch": None if dl is None else dl["epoch"]}
        if not (exit_ok or trip_ok):
            sup.fail("DEADLINE_NOT_ENFORCED_IN_TIME")
    if CANCEL[0] is not None and not any(t["trip"].startswith("SUPERVISOR_CANCEL") for t in sup.trips):
        sup.trips.append({"trip": "SUPERVISOR_CANCEL_LATE", "detail": CANCEL[0], "mono": time.monotonic(),
                          "epoch": time.time()})
    R["epoch_decision"] = time.time()
    if sup.fit_limit_epoch is not None and R["epoch_decision"] > sup.fit_limit_epoch:
        sup.fail("SETTLEMENT_PAST_CHUNK_LIMIT")
    if not launched:
        settlement = "NOT_LAUNCHED" if not sup.helper_open else "UNSETTLED"
    else:
        settlement = "SETTLED" if sup.failures_n == 0 else "UNSETTLED"
    R.update({"end_date": end_date, "mono_end": time.monotonic(), "epoch_end": time.time(),
              "helper_calls": sup.helper_calls, "helper_log": list(sup.helper_log), "helper_open": sup.helper_open,
              "trips": sup.trips, "stop_request": sup.stop, "signal": sup.signal, "failures": sup.failures,
              "failures_n": sup.failures_n, "child_pid": sup.child_pid, "child_returncode": sup.child_rc,
              "child_wait_status_lost": sup.child_lost, "child_exit_mono": sup.child_exit_mono,
              "child_exit_epoch": sup.child_exit_epoch, "streams": sup.streams, "max": sup.max,
              "min_free": sup.min_free, "samples_written": sup.samples_n, "samples_bytes": sup.samples_bytes,
              "lineage_seen": len(sup.seen), "loop_status": sup.loop_status, "status_note": status_note,
              "settlement": settlement})
    code = {"SETTLED": 0, "NOT_LAUNCHED": 10}.get(settlement, 11)
    fd_r, n_r = sup.root_for(cfg["receipt"])
    fd_s, n_s = sup.root_for(cfg["settlement_record"])
    try:
        rsha = publish(fd_r, n_r, jbytes(R))
    except Exception as ex:
        sys.stderr.write("RECEIPT_PUBLICATION_FAILED %r\n" % ex)
        try:
            h, _ = publish_linked(fd_s, n_s, jbytes({"settlement": "UNSETTLED", "receipt": cfg["receipt"],
                                                      "receipt_sha256": None, "supervisor": VERSION,
                                                      "config_sha256": R["config_sha256"],
                                                      "reasons": ["RECEIPT_PUBLICATION_FAILED %r" % ex]}))
            sys.stdout.write(json.dumps({"settlement": "UNSETTLED", "settlement_record_sha256": h,
                                         "receipt_sha256": None, "reasons": ["RECEIPT_PUBLICATION_FAILED"]}) + "\n")
        except Exception as ex2:
            sys.stderr.write("SETTLEMENT_RECORD_FAILED %r\n" % ex2)
            return 13
        return 12
    final = {"settlement": settlement, "receipt": cfg["receipt"], "receipt_sha256": rsha, "supervisor": VERSION,
             "config_sha256": R["config_sha256"], "child_returncode": sup.child_rc, "status_note": status_note,
             "failures": [f["reason"] for f in sup.failures], "failures_n": sup.failures_n,
             "trips": [t["trip"] for t in sup.trips], "authority": R["authority"]}
    try:
        ssha, dir_err = publish_linked(fd_s, n_s, jbytes(final))
    except Exception as ex:
        sys.stderr.write("SETTLEMENT_RECORD_FAILED %r\n" % ex)
        return 13
    sys.stdout.write(json.dumps({"settlement": settlement, "receipt_sha256": rsha, "settlement_record_sha256": ssha,
                                 "settlement_dir_fsync_error": dir_err, "child_returncode": sup.child_rc,
                                 "trips": [t["trip"] for t in sup.trips],
                                 "failures": [f["reason"] for f in sup.failures][:10]}) + "\n")
    return code


def main():
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, _cancel)
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    if len(sys.argv) != 2:
        sys.stderr.write("usage: owned_supervisor_v7.py CONFIG.json\n")
        return 2
    cfg_path = os.path.abspath(sys.argv[1])
    try:
        cfg_sha, _, raw, _ = hash_regular(cfg_path, SMALL_MAX_BYTES, HASH_BUDGET_S, keep=True)
        cfg = strict_json(raw)
        if not isinstance(cfg, dict):
            raise ValueError("config is not a JSON object")
        problems = validate(cfg)
        if problems:
            raise ValueError("; ".join(problems))
    except Exception as ex:
        sys.stderr.write("CONFIG_UNUSABLE %r\n" % ex)
        return 2
    sup = Sup(cfg, cfg_path, cfg_sha)
    try:
        sup.open_roots()
    except OSError as ex:
        sys.stderr.write("OUTPUT_ROOTS_UNUSABLE %r\n" % ex)
        return 2
    adm = admission(sup)
    sup.rec["admission"] = adm
    if adm["reasons"]:
        return finalize(sup, "NOT_LAUNCHED_ADMISSION")
    cb = commit_boundary(sup, adm)
    sup.rec["commit_boundary"] = cb
    if cb["reasons"]:
        return finalize(sup, "NOT_LAUNCHED_COMMIT_BOUNDARY")
    try:
        fd, name = sup.root_for(cfg["samples"])
        sup.samples_fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=fd)
        sup.rec["samples_opened"] = True
    except OSError as ex:
        cb["reasons"].append("SAMPLES_OPEN_FAILED %r" % ex)
        return finalize(sup, "NOT_LAUNCHED_SAMPLES")
    sup.rec["start_date"] = cb["date"]
    mono0, epoch0 = time.monotonic(), time.time()
    abs_end = epoch0 + cfg["max_wall_s"]
    sup.rec.update({"mono_spawn": mono0, "epoch_spawn": epoch0, "abs_end_epoch": abs_end})
    sup.epoch_spawn = epoch0
    try:
        child = subprocess.Popen(cfg["argv"], cwd=cfg["lane"], env=dict(cfg["env"]), stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, close_fds=True)
    except Exception as ex:
        sup.rec["spawn_error"] = repr(ex)
        cb["reasons"].append("SPAWN_FAILED %r" % ex)
        return finalize(sup, "NOT_LAUNCHED_SPAWN")
    sup.keep.append(child)
    sup.child, sup.child_pid = child, child.pid
    try:
        run_supervised(sup, child, mono0, epoch0, abs_end)
    except BaseException as ex:
        sup.rec["exception"] = repr(ex)
        sup.fail("SUPERVISOR_EXCEPTION %r" % ex)
        try:
            emergency_observe(sup)
        except BaseException as ex2:
            sup.fail("EMERGENCY_OBSERVE_EXCEPTION %r" % ex2)
    return finalize(sup, sup.loop_status)


if __name__ == "__main__":
    sys.exit(main())
