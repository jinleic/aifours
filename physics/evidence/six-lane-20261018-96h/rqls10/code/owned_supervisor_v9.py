#!/usr/bin/env python3
"""owned_supervisor_v9: run ONE child process under a fail-closed guard. Standard library only (ctypes for read-only
macOS libproc/sysctl process metadata). v9 = v8 (472fddf9...27a3, frozen, never run; Codex v7 findings disposed in
review/rqls10-owned-supervisor-v8-disposition-v1.json) with the owner-required /bin/date clock restored as the SOLE
metadata helper under a repaired owned and bounded lifecycle (parent objection 07:2x: Python-formatted wall-clock
timestamps do not satisfy "/bin/date before timestamp writes"). code/owned_supervisor_v2.py untouched.

Outcomes: SETTLED, UNSETTLED, NOT_LAUNCHED; every uncertain outcome is UNSETTLED. No birth-ancestry inference
(p_puniqueid is not used); every unproved new identity blocks settlement.
 0. Clock and helper. Every written timestamp (*_date) is the output of /bin/date "+%Y-%m-%dT%H:%M:%S%z" or null (never
    invented); raw time.monotonic() (mono_*) and time.time() (epoch_*) values are telemetry, labelled as such. A helper
    call: refused (null, recorded) after any latched failure, after a supervisor cancel, after the chunk limit or
    beyond helper_budget.max_calls; otherwise spawned in its own session with cwd /, stdin /dev/null and stdout a pipe,
    REGISTERED immediately after Popen returns (pid, Popen object, pipe), its full identity (pid, uniqueid, idversion,
    pgid = pid, uid) read with zombie-inclusive queries (a fast exit leaves an unreaped zombie, so identity stays
    readable; unreadable identity is a failure even if the helper then exits cleanly), reaped only by this supervisor
    (os.waitpid WNOHANG polling within call_budget_s; on overrun one identity-checked SIGTERM to its group and
    term_grace_s more), then checked: process group empty, stdout at EOF after a non-blocking read of at most 256 bytes,
    rc 0 and a well-formed date. Any failure or exception latches a failure; a helper that is not verified reaped stays
    registered and makes the outcome UNSETTLED (also when the child was never launched).
 1. Failure latch (monotonic, never cleared): identity, observation (census coverage, free space, output size, lane
    walk), capture, GO delivery, launch-record publication, grace expiry, evidence binding, publication budget and
    unexpected exceptions. A launched run with a non-empty latch is UNSETTLED. Resource trips (DEADLINE, RSS, BUSY,
    FREE, OUTPUT, STREAM_CAP, LANE_CEILING, SUPERVISOR_CANCEL) request a stop and are recorded; they are not failures.
 2. Stop and grace: the first stop request is latched with a monotonic time; at most one SIGTERM goes to the child's
    process group, after the identity check of item 4. The grace (settle_s) runs from the first stop request and from
    the reaping of the child. A clear observation is accepted only if the census that established it completed before
    every applicable grace cutoff; otherwise GRACE_EXPIRED_* is latched (irreversible). Sleeps are clamped to the
    remaining grace. No SIGKILL, no escalation, no subprocess or tool timeouts, no ulimit, no deletion.
 3. Single reaper: SIGCHLD is reset to SIG_DFL before the spawn; the child's Popen object stays referenced and is never
    polled or waited; only os.waitpid(pid, WNOHANG) reaps it; ECHILD is a failure and disables signalling. The child is
    registered inside the protected post-spawn block.
 4. Identity = (pid, p_uniqueid, p_idversion, pgid, uid) read with zombie-inclusive libproc queries immediately after the
    spawn and re-read equal immediately before the one killpg; otherwise no signal and IDENTITY_UNVERIFIED.
 5. Census (libproc and sysctl only, no ps/lsof). Every listed pid is identified by uniqueid, short info and uniqueid
    again (bracket); every later measurement of that pid (cwd, argv, task, start) is followed by another uniqueid read.
    A listed pid that disappears or changes before it is identified or measured makes the census INCOMPLETE (failed
    coverage, never absence). Classification relative to U0 (the child's uniqueid; p_uniqueid is assigned at fork from
    an increasing counter and kept across exec): uniqueid < U0 OLD; == U0 CHILD; > U0 NEW. A NEW process whose effective
    and real uid both differ from this supervisor's is FOREIGN_NEW (recorded, not blocking; a descendant that drops both
    uids is outside this guarantee, which relies on the reviewed child caps). Any other NEW process is UNRELATED only
    if its chain of CURRENT parents (ppid) consists of identified, untraced NEW processes none of which has ppid <= 1
    and ends at an identified OLD process other than launchd; it is OWNED if the chain reaches the child; otherwise it
    is UNPROVED. This uses only current-parent edges and the kernel rule that an orphan is reparented to initproc (or a
    traced process to its original parent; xnu kern_exit.c, copy in lane tmp/); traced processes are UNPROVED. CHILD,
    OWNED, UNPROVED and child-group members (zombies included) block settlement. NEW processes started by launchd
    (ppid 1) are UNPROVED and therefore block while alive (fail-closed; the receipt names them).
 6. Lane accounting (RSS sum, busy count, busy pids) covers live non-zombie same-uid blocking processes and same-uid
    processes whose cwd or argv references a lane root (exclusion needs a successful cwd read AND a completely parsed
    argv without a match). Busy = CPU over wall time since the previous sample of the same uniqueid, or since process
    start when first seen, >= busy_cpu_fraction. Every census applies the limits: admission and the pre-GO census
    require lane_busy + cpu_slots <= 2 and lane_rss + rss_projection <= rss_trip; running and final censuses trip BUSY
    (lane_busy > busy_limit) and RSS (lane_rss > rss_trip). The limits are sampled, not enforced between samples.
 7. Bounded operations share absolute monotonic deadlines that are checked before and after every operation (also
    after the final write, fsync and close); files are read only if regular (lstat/fstat agree, O_NOFOLLOW|O_NONBLOCK)
    within a byte limit and must not change; directories are traversed only through O_DIRECTORY|O_NOFOLLOW descriptors
    with entry and time limits, refusing mount boundaries. Native calls cannot be interrupted; an overrun detected on
    return fails closed.
 8. Admission (else NOT_LAUNCHED): strict JSON config within the hard policy; pins; single parent authority, one use:
    the GO file must say decision GO for this item, be unexpired and list THIS config's sha256 with exactly
    output_roots, argv, max_wall_s, cpu_slots and the three reservation values; output roots EMPTY real directories
    strictly under lane_disk_root; every charged location (lane, lane_disk_root, output roots, TMPDIR) on one filesystem
    (same st_dev) and every lane root a real directory chain; fresh stability receipt (age = /bin/date reading minus the
    receipt's now_date; no reading -> STABILITY_AGE_UNVERIFIABLE); free space (fstatvfs on the output root) and lane
    ceiling including the reservation; two complete censuses 2 s apart within the limits; no cancel. Commit boundary
    immediately before spawn re-checks, with a fresh /bin/date reading, stability age, GO expiry (epoch telemetry),
    free space, cancel and chunk fit (now + max_wall_s + settle_s + FINALIZE_ALLOWANCE_S within the chunk and 180 s
    before the settled-by epoch).
 9. GO linearization: after the spawn, the identity capture, the sink threads and the launch-record publication, the
    supervisor re-validates immediately before GO: a complete census whose only blocking process is the child and which
    satisfies the admission limits, stability age (commit-boundary age plus monotonic time elapsed since that reading),
    GO expiry, free space, spawn age <= min(60 s, max_wall_s / 2), no stop, no latched failure and no cancel; the
    cancel flag is read once more immediately before the single write of "GO\n" (the linearization point). A cancel
    after that point is a stop request. GO must be written, flushed and stdin closed, else GO_NOT_DELIVERED.
10. Disk: free space by fstatvfs on the output root; declared-output bytes (plus sinks and samples) <= output_trip_bytes;
    capped sinks; capped samples (cap reached = failure); anchored lane walk + lane outstanding reservations + this
    run's unused reservation <= ceiling. Finalization repeats the aggregate output, overflow, lane, RSS and busy
    checks, then serializes the receipt and settlement record and requires the exact publication bytes to fit the free
    floor, the lane ceiling and the remaining reservation (PUBLICATION_BUDGET otherwise). Sampling cannot stop child
    writes between samples; the reviewed child caps and the reservation are the bound. No OS sandbox is provided.
11. Evidence binding: config hash of the parsed bytes; supervisor-created files keep their (device, inode) from creation
    and must still be those inodes with one link; launch record, samples and sinks must re-hash to the supervisor's own
    digests; pins re-hashed; each output root unchanged and holding exactly its own declared names (per-root manifest);
    child outputs must be regular files with one link and birth time >= the spawn epoch (recorded check; exclusive
    creation itself is the reviewed child's contract).
12. Publication and acknowledgment: receipt and settlement record are published by exclusive create through the root
    fd, complete writes, fsync, close and bounded re-read; the settlement record is written to NAME.staged, hard-linked
    to NAME and checked to be the same inode; then EVERY output root directory is fsynced. Only after all of that is
    post_publish_mono read and ONE stdout summary line printed with the verified receipt and settlement sha256 values.
    Any publication, re-read or directory-fsync failure gives exit 12 or 13 with an unsuccessful summary; a supervisor
    cancel that was not handled as a stop during the run (arriving after the observation loop, before the summary)
    suppresses success (exit 14). The files and the exit code are not authoritative: only the parent's own verified
    commit is, and only it releases reservations. /bin/date helpers are not lane processes (cwd /, no lane path).
Exit codes: 0 SETTLED and acknowledged, 10 NOT_LAUNCHED, 11 UNSETTLED, 12 receipt publication failed, 13 settlement
publication or directory sync failed, 14 cancel before acknowledgment, 2 unusable config or output roots (nothing written).
"""
import ctypes, datetime, errno, hashlib, json, math, os, re, signal, stat, struct, subprocess, sys, threading, time

VERSION = "owned_supervisor_v9"
CANCEL = [None]
FINALIZE_ALLOWANCE_S = 120.0
GO_MAX_DELAY_S = 60.0
RECEIPT_ALLOWANCE_BYTES = 4 << 20
SMALL_MAX_BYTES = 1 << 20
PIN_MAX_BYTES = 64 << 20
HASH_BUDGET_S = 60.0
PUBLISH_BUDGET_S = 30.0
WALK_MAX_ENTRIES = 500000
WALK_MAX_DEPTH = 64
WALK_BUDGET_S = 30.0
ROOT_MAX_ENTRIES = 4096
CENSUS_BUDGET_S = 10.0
CENSUS_RETRIES = 3
DEADLINE_SLACK_EXTRA_S = 5.0
HARD = {"lane_ceiling_max": 10737418240, "free_floor_min": 12000000000, "launch_free_min_min": 12200000000,
        "busy_max": 2, "rss_trip_max": 51539607552, "max_chunk_max": 10800, "stability_age_max": 300}
CONFIG_KEYS = {
    "item": str, "owner": str, "purpose": str, "lane": str, "argv": list, "env": dict, "stdout": str, "stderr": str,
    "stdout_cap_bytes": "int", "stderr_cap_bytes": "int", "outputs": list, "launch_record": str, "samples": str,
    "samples_cap_bytes": "int", "receipt": str, "settlement_record": str, "output_roots": list, "pins": list,
    "max_wall_s": "num", "settle_s": "num", "sample_s": "num", "max_chunk_seconds": "num",
    "owned_compute_settled_by_epoch": "num", "rss_trip_bytes": "int", "free_trip_bytes": "int",
    "output_trip_bytes": "int", "launch_free_min_bytes": "int", "lane_roots": list, "lane_disk_root": str,
    "lane_disk_ceiling_bytes": "int", "lane_walk_s": "num", "busy_limit": "int", "busy_cpu_fraction": "num",
    "cpu_slots": "int", "rss_projection_bytes": "int", "admission": dict, "helper_budget": dict,
    "fault_injection": dict}
ADMISSION_KEYS = {"go_path": str, "reservation_bytes": "int", "outstanding_reservations_bytes": "int",
                  "lane_outstanding_reservations_bytes": "int", "stability_receipt_path": str,
                  "stability_max_age_s": "num"}
GO_BOUND_KEYS = ("output_roots", "argv", "max_wall_s", "cpu_slots", "reservation_bytes",
                 "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")
HELPER_KEYS = {"max_calls": "int", "call_budget_s": "num", "term_grace_s": "num"}
FAULTS = ("identity_check_fails", "date_helper_fails")
DATE_RE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+-]\d{4}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _cancel(signum, frame):
    if CANCEL[0] is None:
        CANCEL[0] = signum


class Bounded(OSError):
    """an observation or publication that is not a complete, bounded, regular-file operation."""


class Deadline:
    def __init__(self, seconds):
        self.t = time.monotonic() + seconds

    def check(self, what):
        if time.monotonic() > self.t:
            raise Bounded("deadline exceeded: %s" % what)

    def left(self):
        return self.t - time.monotonic()


def date_age_s(later, earlier):
    """seconds between two /bin/date strings (both carry their UTC offset)."""
    fmt = "%Y-%m-%dT%H:%M:%S%z"
    return (datetime.datetime.strptime(later, fmt) - datetime.datetime.strptime(earlier, fmt)).total_seconds()


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
# sys/proc_info.h: PROC_PIDTBSDINFO 3 (136 bytes; pbi_start_tvsec/tvusec uint64 at 120/128), PROC_PIDTASKINFO 4 (96
# bytes; pti_resident_size uint64 at 8, pti_total_user/system uint64 at 16/24 in mach time units), PROC_PIDVNODEPATHINFO
# 9 (2352 bytes; pvi_cdir.vip_path char[1024] at 152), PROC_PIDT_SHORTBSDINFO 13 (64 bytes; pid, ppid, pgid, status
# uint32 at 0/4/8/12, comm char[16] at 16, flags uint32 at 32 (PROC_FLAG_TRACED 2), uid at 36, ruid at 44). xnu
# proc_info_private.h: PROC_PIDUNIQIDENTIFIERINFO 17 (56 bytes; p_uniqueid uint64 at 16, p_idversion int32 at 32), no
# same-user restriction; a nonzero arg also finds zombies for flavors 3, 13, 17. sysctl KERN_PROCARGS2: int argc, exec
# path, NUL padding, argc NUL-terminated strings.
PROC_PIDTBSDINFO, PROC_PIDTASKINFO, PROC_PIDVNODEPATHINFO, PROC_PIDT_SHORTBSDINFO = 3, 4, 9, 13
PROC_PIDUNIQIDENTIFIERINFO = 17
BSD_SIZE, TASK_SIZE, VNP_SIZE, SHORT_SIZE, UNIQ_SIZE = 136, 96, 2352, 64, 56
PROC_FLAG_TRACED = 2
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
    flags, uid = struct.unpack_from("=II", raw, 32)
    ruid = struct.unpack_from("=I", raw, 44)[0]
    comm = raw[16:32].split(b"\0")[0].decode("utf-8", "replace")
    return {"pid": p, "ppid": pp, "pgid": pg, "status": status, "flags": flags, "uid": uid, "ruid": ruid,
            "comm": comm}, 0


def uniq_info(pid):
    raw, e = _pidinfo(pid, PROC_PIDUNIQIDENTIFIERINFO, UNIQ_SIZE, 1)
    if raw is None:
        return None, e
    u = struct.unpack_from("=Q", raw, 16)[0]
    idv = struct.unpack_from("=i", raw, 32)[0]
    return {"uniqueid": u, "idversion": idv}, 0


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
    """pids (zombies included) in process group pgid, or None if unreadable (libproc returns 0 on error; errno decides)."""
    buf = (ctypes.c_int * 256)()
    ctypes.set_errno(0)
    m = _LP.proc_listpgrppids(pgid, buf, ctypes.sizeof(buf))
    e = ctypes.get_errno()
    if m < 0 or (m == 0 and e != 0) or m >= 256:
        return None
    return [buf[i] for i in range(m)]


# ---------------------------------------------------------------- bounded file operations (shared deadlines)
def _open_regular(path, max_bytes, dl, dir_fd=None):
    dl.check("before open %s" % path)
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


def hash_regular(path, max_bytes, dl, dir_fd=None, keep=False):
    """sha256 of a regular file read completely within max_bytes before dl; returns (hex, size, bytes|None, stat)."""
    fd, st = _open_regular(path, max_bytes, dl, dir_fd)
    h, got, parts = hashlib.sha256(), 0, []
    try:
        while got < st.st_size:
            dl.check("reading %s" % path)
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
    dl.check("after reading %s" % path)
    return h.hexdigest(), st.st_size, (b"".join(parts) if keep else None), st


def write_all(fd, data, dl):
    view = memoryview(data)
    while view:
        dl.check("write")
        k = os.write(fd, view)
        if k <= 0:
            raise Bounded("zero-progress write")
        view = view[k:]
    dl.check("after write")


def jbytes(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, allow_nan=False, default=repr) + "\n").encode("utf-8")


def create_exclusive(dirfd, name):
    """exclusive no-follow create through dirfd; returns (fd, (st_dev, st_ino))."""
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dirfd)
    st = os.fstat(fd)
    return fd, (st.st_dev, st.st_ino)


def publish(dirfd, name, data, dl):
    """exclusive create, complete write, fsync, close, re-read within dl; returns (sha256, (dev, ino))."""
    fd, ident = create_exclusive(dirfd, name)
    try:
        write_all(fd, data, dl)
        os.fsync(fd)
        dl.check("after fsync %s" % name)
    finally:
        os.close(fd)
    dl.check("after close %s" % name)
    h = hashlib.sha256(data).hexdigest()
    got, size, _, st = hash_regular(name, len(data), dl, dir_fd=dirfd)
    if got != h or size != len(data) or (st.st_dev, st.st_ino) != ident:
        raise Bounded("re-read mismatch: %s" % name)
    return h, ident


def publish_linked(dirfd, name, data, dl):
    """NAME.staged completely published, hard-linked to NAME (atomic, exclusive), same inode verified, re-read."""
    h, ident = publish(dirfd, name + ".staged", data, dl)
    os.link(name + ".staged", name, src_dir_fd=dirfd, dst_dir_fd=dirfd)
    got, size, _, st = hash_regular(name, len(data), dl, dir_fd=dirfd)
    if got != h or (st.st_dev, st.st_ino) != ident or st.st_nlink != 2:
        raise Bounded("linked record mismatch: %s" % name)
    return h, ident


def walk_bytes(root, dl):
    """regular-file bytes under root, traversed only through O_DIRECTORY|O_NOFOLLOW descriptors, refusing mount
    boundaries; entries vanishing during the walk count 0; entry, depth and time limits (else Bounded)."""
    fd0 = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    count = [0]
    try:
        dev = os.fstat(fd0).st_dev
        return _walk_fd(fd0, dev, dl, count, 0)
    finally:
        os.close(fd0)


def _walk_fd(fd, dev, dl, count, depth):
    if depth > WALK_MAX_DEPTH:
        raise Bounded("lane walk depth limit")
    total, subdirs = 0, []
    with os.scandir(fd) as it:
        for ent in it:
            count[0] += 1
            if count[0] > WALK_MAX_ENTRIES:
                raise Bounded("lane walk entry limit")
            dl.check("lane walk")
            try:
                st = os.stat(ent.name, dir_fd=fd, follow_symlinks=False)
            except FileNotFoundError:
                continue
            if st.st_dev != dev:
                raise Bounded("mount boundary at %s" % ent.name)
            if stat.S_ISDIR(st.st_mode):
                subdirs.append((ent.name, st.st_ino))
            elif stat.S_ISREG(st.st_mode):
                total += st.st_size
    for name, ino in subdirs:
        try:
            cfd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
        except (FileNotFoundError, NotADirectoryError):
            continue
        try:
            cst = os.fstat(cfd)
            if (cst.st_dev, cst.st_ino) != (dev, ino):
                raise Bounded("directory replaced during walk: %s" % name)
            total += _walk_fd(cfd, dev, dl, count, depth + 1)
        finally:
            os.close(cfd)
    dl.check("lane walk directory end")
    return total


def list_root(fd, dl):
    names = []
    with os.scandir(fd) as it:
        for ent in it:
            names.append(ent.name)
            if len(names) > ROOT_MAX_ENTRIES:
                raise Bounded("output root entry limit")
            dl.check("root inventory")
    return sorted(names)


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


def _float(s):
    x = float(s)
    if not math.isfinite(x):
        raise ValueError("overflowing numeric literal %s" % s)
    return x


def strict_json(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=_no_dup, parse_constant=_no_const, parse_float=_float)


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
    a, fi, h = cfg["admission"], cfg["fault_injection"], cfg["helper_budget"]
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
    rng("busy_limit", cfg["busy_limit"], 1, HARD["busy_max"])
    rng("cpu_slots", cfg["cpu_slots"], 1, HARD["busy_max"])
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
        if p.endswith(".staged"):
            bad.append("%s uses the reserved .staged suffix" % p)
    return bad


def evidence_paths(cfg):
    return [cfg["stdout"], cfg["stderr"], cfg["launch_record"], cfg["samples"], cfg["receipt"], cfg["settlement_record"]]


# ---------------------------------------------------------------- supervisor state
class Sup:
    def __init__(self, cfg, cfg_path, cfg_sha):
        self.cfg = cfg
        try:
            self_sha = hash_regular(SELF, PIN_MAX_BYTES, Deadline(HASH_BUDGET_S))[0]
            self_err = None
        except OSError as ex:
            self_sha, self_err = None, repr(ex)
        self.rec = {"supervisor": VERSION, "supervisor_path": SELF, "supervisor_sha256": self_sha,
                    "supervisor_hash_error": self_err, "config": cfg_path, "config_sha256": cfg_sha,
                    "supervisor_pid": MY_PID, "uid": MY_UID, "timebase": TIMEBASE, "argmax": ARGMAX,
                    "authority": "not authoritative: only the supervising parent's own verified commit is",
                    "clock_note": "*_date = /bin/date +%Y-%m-%dT%H:%M:%S%z output or null (never invented); mono_* = "
                                  "time.monotonic() s and epoch_* = time.time() s are raw telemetry"}
        self.failures, self.failures_n = [], 0
        self.trips, self.tripped = [], set()
        self.stop = None
        self.signal = None
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
        self.prev_cpu = {}
        self.streams = {}
        self.threads = []
        self.samples_fd = None
        self.samples_bytes = 0
        self.samples_n = 0
        self.samples_dead = False
        self.samples_hash = hashlib.sha256()
        self.root_fds = {}
        self.allow = {}
        self.created = {}
        self.lane_bytes = None
        self.next_walk = 0.0
        self.max = {"lane_rss": 0, "lane_busy": 0, "blocking_live": 0, "output_bytes": 0, "lane_bytes": 0}
        self.min_free = None
        self.loop_status = "NOT_STARTED"
        self.epoch_spawn = None
        self.mono_spawn = None
        self.fit_limit_epoch = None
        self.clear = None
        self.census_incomplete = 0
        self.helpers = []
        self.helper_calls = 0
        self.helper_log = []

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
        self.stop["date"] = self.date_now("stop")

    # ------------------------------------------------------------ /bin/date, the sole metadata helper
    def _helper_reap(self, h, budget_s):
        """poll os.waitpid(pid, WNOHANG) up to budget_s (monotonic); records rc or LOST in h."""
        t0 = time.monotonic()
        while True:
            try:
                got, status = os.waitpid(h["pid"], os.WNOHANG)
            except ChildProcessError:
                h["state"] = "LOST"
                return
            if got != 0:
                h["rc"] = os.waitstatus_to_exitcode(status)
                h["state"] = "REAPED"
                return
            if time.monotonic() - t0 >= budget_s:
                return
            time.sleep(0.005)

    def date_now(self, purpose):
        """one /bin/date reading or None; see item 0 of the module docstring."""
        hb = self.cfg["helper_budget"]
        entry = {"purpose": purpose, "mono_start": time.monotonic()}
        h = None
        try:
            if self.failures_n:
                entry["outcome"] = "REFUSED_AFTER_FAILURE_LATCH"
                return None
            if CANCEL[0] is not None:
                entry["outcome"] = "REFUSED_AFTER_CANCEL"
                return None
            if self.fit_limit_epoch is not None and time.time() > self.fit_limit_epoch:
                entry["outcome"] = "REFUSED_PAST_CHUNK_LIMIT"
                self.fail("HELPER_REFUSED_PAST_CHUNK_LIMIT")
                return None
            if self.fault("date_helper_fails"):
                entry["outcome"] = "FAULT_INJECTED"
                self.fail("HELPER_FAULT_INJECTED")
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
            h = {"pid": p.pid, "popen": p, "state": "OPEN", "rc": None, "entry": entry}
            self.helpers.append(h)
            self.keep.append(p)
            entry["pid"] = p.pid
            ident, why = self.read_identity(p.pid)
            entry["identity"] = ident
            if ident is None or ident["pgid"] != p.pid or ident["uid"] != MY_UID:
                self.fail("HELPER_IDENTITY_UNVERIFIED %s" % (why or ident))
            self._helper_reap(h, hb["call_budget_s"])
            if h["state"] == "OPEN":
                now_id, _ = self.read_identity(p.pid)
                sent = False
                if ident is not None and ident["pgid"] == p.pid and self.same_identity(now_id, ident):
                    try:
                        os.killpg(p.pid, signal.SIGTERM)
                        sent = True
                    except OSError as ex:
                        entry["sigterm_error"] = repr(ex)
                entry["sigterm"] = sent
                self._helper_reap(h, hb["term_grace_s"])
            if h["state"] != "REAPED":
                entry["outcome"] = "HELPER_" + h["state"]
                self.fail("HELPER_NOT_REAPED %d %s" % (p.pid, h["state"]))
                return None
            members = pgrp_members(p.pid)
            entry["group_after_reap"] = members
            fd = p.stdout.fileno()
            os.set_blocking(fd, False)
            try:
                out = os.read(fd, 257)
            except BlockingIOError:
                out = None
            try:
                eof = os.read(fd, 1) == b"" if out is not None else False
            except BlockingIOError:
                eof = False
            p.stdout.close()
            entry.update({"rc": h["rc"], "mono_end": time.monotonic(), "stdout_eof": eof})
            if members is None or members:
                self.fail("HELPER_GROUP_LIVE_OR_UNREADABLE %d %r" % (p.pid, members))
            if not eof:
                self.fail("HELPER_STREAM_NOT_CLOSED %d" % p.pid)
            txt = (out or b"").decode("utf-8", "replace").strip()
            if h["rc"] != 0 or out is None or len(out) > 256 or not DATE_RE.match(txt):
                self.fail("HELPER_BAD_OUTPUT rc %r" % h["rc"])
            if members is None or members or not eof or ident is None or h["rc"] != 0 or not DATE_RE.match(txt) or \
                    out is None or len(out) > 256 or ident["pgid"] != p.pid or ident["uid"] != MY_UID:
                h["state"] = "REAPED_WITH_FAILURE"
                entry["outcome"] = "FAILED"
                return None
            h["state"] = "SETTLED"
            entry["outcome"] = "OK"
            entry["date"] = txt
            return txt
        except Exception as ex:
            entry["outcome"] = "EXCEPTION %r" % ex
            self.fail("HELPER_EXCEPTION %r" % ex)
            return None
        finally:
            self.helper_log_append(entry)

    def helper_log_append(self, entry):
        if len(self.helper_log) < 256:
            self.helper_log.append(entry)

    def helpers_unreaped(self):
        for h in self.helpers:
            if h["state"] == "OPEN":
                self._helper_reap(h, 0.0)
        return [h["pid"] for h in self.helpers if h["state"] in ("OPEN", "LOST")]

    # ------------------------------------------------------------ reaping and identity
    def reap_child(self):
        if self.child_pid is None or self.child_rc is not None or self.child_lost:
            return
        try:
            got, status = os.waitpid(self.child_pid, os.WNOHANG)
        except ChildProcessError:
            self.child_lost = True
            self.fail("WAIT_STATUS_LOST child %d" % self.child_pid)
            return
        if got != 0:
            self.child_rc = os.waitstatus_to_exitcode(status)
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
            if not ok:
                res["why_not"] = "IDENTITY_MISMATCH_OR_UNREADABLE %s" % (why or now_id)
                self.signal = res
                self.fail("IDENTITY_UNVERIFIED %s" % res["why_not"])
                return
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
        self.signal = res

    # ------------------------------------------------------------ census
    def _proc(self, pid):
        """(record, 0) or (None, errno); uniqueid read before and after the short info (one process)."""
        u1, e = uniq_info(pid)
        if u1 is None:
            return None, e
        si, e = short_info(pid)
        if si is None:
            return None, e
        u2, e = uniq_info(pid)
        if u2 is None:
            return None, e
        if u1 != u2:
            return None, -8
        si.update(u1)
        return si, 0

    def _still(self, pid, p):
        u, _ = uniq_info(pid)
        return u is not None and u["uniqueid"] == p["uniqueid"]

    def classify(self, procs):
        U0, memo = self.u0, {}
        for pid, p in procs.items():
            if U0 is None:
                p["class"] = "OLD"
                continue
            if p["uniqueid"] == U0:
                p["class"] = "CHILD"
                continue
            if p["uniqueid"] < U0:
                p["class"] = "OLD"
                continue
            if p["uid"] != MY_UID and p["ruid"] != MY_UID:
                p["class"] = "FOREIGN_NEW"
                continue
            chain, cur, res = [], pid, None
            while res is None:
                if cur in memo:
                    res = memo[cur]
                    break
                q = procs.get(cur)
                if q is None or (q["flags"] & PROC_FLAG_TRACED) or q["ppid"] <= 1 or len(chain) > 4096:
                    res = "UNPROVED"
                    break
                chain.append(cur)
                a = procs.get(q["ppid"])
                if a is None:
                    res = "UNPROVED"
                elif a["uniqueid"] == U0:
                    res = "OWNED"
                elif a["uniqueid"] < U0:
                    res = "UNRELATED" if a["pid"] != 1 else "UNPROVED"
                else:
                    cur = q["ppid"]
            for c in chain:
                memo[c] = res
            p["class"] = memo.get(pid, res)
        for p in procs.values():
            p["blocking"] = p["class"] in ("CHILD", "OWNED", "UNPROVED") or \
                (self.pgid0 is not None and p["pgid"] == self.pgid0)

    def census(self, dl):
        """one scan; raises RuntimeError on a hard failure; 'complete' is False when any listed pid disappeared or
        changed before identification or measurement (failed coverage)."""
        pids = list_pids()
        if pids is None:
            raise RuntimeError("LISTPIDS_FAILED")
        dl.check("census list")
        procs, vanished = {}, []
        for k, pid in enumerate(pids):
            if pid <= 0:
                continue
            if k % 64 == 0:
                dl.check("census identify")
            p, e = self._proc(pid)
            if p is None:
                if e in (errno.ESRCH, -8):
                    vanished.append(pid)
                    continue
                raise RuntimeError("PROCINFO pid %d errno %d" % (pid, e))
            procs[pid] = p
        self.classify(procs)
        roots, frac = self.cfg["lane_roots"], self.cfg["busy_cpu_fraction"]
        now_m, now_e = time.monotonic(), time.time()
        lane, cpu_now, unmeasured = {}, {}, []
        for k, (pid, p) in enumerate(procs.items()):
            if k % 64 == 0:
                dl.check("census measure")
            mine = p["uid"] == MY_UID
            if p["status"] == SZOMB or (not mine and not p["blocking"]):
                continue
            if not mine:
                unmeasured.append(pid)
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
                        if not self._still(pid, p):
                            vanished.append(pid)
                            continue
                        raise RuntimeError("UNREADABLE_SAME_UID pid %d comm %s cwd_err %r argv_err %r" %
                                           (pid, p["comm"], None if cw is not None else e1,
                                            None if av is not None else e2))
                if not self._still(pid, p):
                    vanished.append(pid)
                    continue
            if not member:
                continue
            ti, e = task_info(pid)
            st0, e2 = bsd_start(pid) if p["uniqueid"] not in self.prev_cpu else (None, 0)
            if ti is None or (p["uniqueid"] not in self.prev_cpu and st0 is None) or not self._still(pid, p):
                if (ti is None and e not in (errno.ESRCH,)) or (st0 is None and p["uniqueid"] not in self.prev_cpu
                                                                and e2 not in (errno.ESRCH,)):
                    if self._still(pid, p):
                        raise RuntimeError("MEASURE pid %d errno %r %r" % (pid, e, e2))
                vanished.append(pid)
                continue
            prev = self.prev_cpu.get(p["uniqueid"])
            ns_total = ti["cpu_ticks"] * TIMEBASE[0] / TIMEBASE[1]
            if prev is None:
                age = now_e - st0
                busy = age <= 0.05 or ns_total >= frac * age * 1e9
            else:
                dt = now_m - prev[0]
                busy = dt <= 0 or (ti["cpu_ticks"] - prev[1]) * TIMEBASE[0] / TIMEBASE[1] >= frac * dt * 1e9
            cpu_now[p["uniqueid"]] = (now_m, ti["cpu_ticks"])
            lane[pid] = {"rss": ti["rss"], "busy": busy}
        self.prev_cpu = cpu_now
        dl.check("census end")
        blocking = sorted(pid for pid, p in procs.items() if p["blocking"])
        out = {"pids": len(procs), "complete": not vanished, "vanished_n": len(vanished), "vanished": vanished[:20],
               "blocking_live": blocking,
               "blocking_detail": [[pid, procs[pid]["comm"], procs[pid]["class"], procs[pid]["ppid"],
                                    procs[pid]["status"] == SZOMB] for pid in blocking[:40]],
               "owned_live": sorted(pid for pid in blocking if procs[pid]["class"] == "OWNED"),
               "unproved_live": sorted(pid for pid in blocking if procs[pid]["class"] == "UNPROVED"),
               "group_live": sorted(pid for pid in blocking if self.pgid0 is not None and procs[pid]["pgid"] == self.pgid0),
               "blocking_zombies": sorted(pid for pid in blocking if procs[pid]["status"] == SZOMB),
               "blocking_unmeasured": sorted(unmeasured),
               "foreign_new_n": sum(1 for p in procs.values() if p["class"] == "FOREIGN_NEW"),
               "lane_pids": sorted(lane), "lane_rss": sum(v["rss"] for v in lane.values()),
               "lane_busy": sum(1 for v in lane.values() if v["busy"]),
               "lane_busy_pids": sorted(pid for pid, v in lane.items() if v["busy"]),
               "mono_done": time.monotonic()}
        return out

    def census_complete(self, budget_s):
        """up to CENSUS_RETRIES censuses until one is complete; returns the last census (complete or not)."""
        dl = Deadline(budget_s)
        c = None
        for _ in range(CENSUS_RETRIES):
            c = self.census(dl)
            if c["complete"]:
                return c
            self.census_incomplete += 1
            time.sleep(0.05)
        return c

    def streams_closed(self):
        return len(self.streams) == 2 and all(st["closed"] for st in self.streams.values())

    def is_clear(self, c):
        return c is not None and c["complete"] and self.child_rc is not None and not c["blocking_live"] and \
            self.streams_closed()

    def grace_cutoffs(self):
        cuts = []
        if self.stop is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_STOP_REQUEST", self.stop["mono"] + self.cfg["settle_s"]))
        if self.child_exit_mono is not None:
            cuts.append(("GRACE_EXPIRED_AFTER_CHILD_EXIT", self.child_exit_mono + self.cfg["settle_s"]))
        return cuts

    # ------------------------------------------------------------ evidence files
    def root_for(self, path):
        return self.root_fds[os.path.dirname(path)][0], os.path.basename(path)

    def open_roots(self):
        for r in self.cfg["output_roots"]:
            fd = os.open(r, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            st = os.fstat(fd)
            self.root_fds[r] = (fd, st.st_dev, st.st_ino)
            self.allow[r] = set()
        for p in evidence_paths(self.cfg) + [o["path"] for o in self.cfg["outputs"]]:
            self.allow[os.path.dirname(p)].add(os.path.basename(p))
        r = os.path.dirname(self.cfg["settlement_record"])
        self.allow[r].add(os.path.basename(self.cfg["settlement_record"]) + ".staged")

    def free_now(self):
        fd = self.root_fds[self.cfg["output_roots"][0]][0]
        st = os.fstatvfs(fd)
        return st.f_bavail * st.f_frsize

    def output_bytes(self):
        ob = 0
        for o in self.cfg["outputs"]:
            fd, name = self.root_for(o["path"])
            try:
                ob += os.stat(name, dir_fd=fd, follow_symlinks=False).st_size
            except FileNotFoundError:
                pass
        return ob + sum(st["bytes_written"] for st in self.streams.values()) + self.samples_bytes

    def write_sample(self, obj):
        if self.samples_fd is None or self.samples_dead:
            return
        try:
            line = (json.dumps(obj, sort_keys=True, allow_nan=False, default=repr) + "\n").encode("utf-8")
            if self.samples_bytes + len(line) > self.cfg["samples_cap_bytes"]:
                self.samples_dead = True
                self.fail("SAMPLES_CAP")
                return
            write_all(self.samples_fd, line, Deadline(10.0))
            self.samples_hash.update(line)
            self.samples_bytes += len(line)
            self.samples_n += 1
        except Exception as ex:
            self.samples_dead = True
            self.fail("SAMPLES_WRITE_FAILED %r" % ex)

    def limits_ok(self, c):
        cfg = self.cfg
        return c["lane_busy"] + cfg["cpu_slots"] <= HARD["busy_max"] and \
            c["lane_rss"] + cfg["rss_projection_bytes"] <= cfg["rss_trip_bytes"]

    def apply_trips(self, c, fr, ob):
        cfg = self.cfg
        if c is not None and c["lane_rss"] > cfg["rss_trip_bytes"]:
            self.trip("RSS", c["lane_rss"])
        if c is not None and c["lane_busy"] > cfg["busy_limit"]:
            self.trip("BUSY", [c["lane_busy"], c["lane_busy_pids"]])
        if fr is not None and fr < cfg["free_trip_bytes"]:
            self.trip("FREE", fr)
        if ob is not None and ob > cfg["output_trip_bytes"]:
            self.trip("OUTPUT", ob)
        if any(st["overflow"] for st in self.streams.values()):
            self.trip("STREAM_CAP", {k: [v["bytes_seen"], v["bytes_written"]] for k, v in self.streams.items()})
        if self.lane_bytes is not None and ob is not None:
            unused = max(0, cfg["admission"]["reservation_bytes"] - ob)
            if self.lane_bytes + cfg["admission"]["lane_outstanding_reservations_bytes"] + unused > \
                    cfg["lane_disk_ceiling_bytes"]:
                self.trip("LANE_CEILING", self.lane_bytes)


def sink_thread(name, pipe, dirfd, fname, cap, sup):
    st = {"bytes_seen": 0, "bytes_written": 0, "overflow": False, "closed": False, "error": None, "eof": False,
          "sha256_written": None}
    digest = hashlib.sha256()
    sup.streams[name] = st
    fd, ident = create_exclusive(dirfd, fname)
    sup.created[os.path.join(os.path.dirname(sup.cfg[name]), fname)] = ident

    def run():
        try:
            while True:
                chunk = pipe.read1(65536)
                if not chunk:
                    st["eof"] = True
                    break
                st["bytes_seen"] += len(chunk)
                room = cap - st["bytes_written"]
                if room > 0:
                    part = chunk[:room]
                    write_all(fd, part, Deadline(30.0))
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


# ---------------------------------------------------------------- admission, commit boundary, GO revalidation
def read_go(sup, R, reasons):
    cfg, adm = sup.cfg, sup.cfg["admission"]
    try:
        gh, _, graw, _ = hash_regular(adm["go_path"], SMALL_MAX_BYTES, Deadline(HASH_BUDGET_S), keep=True)
        R["go_sha256"] = gh
        g = strict_json(graw)
        entry = g.get("configs", {}).get(sup.rec["config_sha256"]) if isinstance(g, dict) and \
            isinstance(g.get("configs"), dict) else None
        if not isinstance(g, dict) or g.get("decision") != "GO" or g.get("item") != cfg["item"]:
            reasons.append("GO_NOT_FOR_THIS_ITEM")
        elif not isinstance(entry, dict):
            reasons.append("GO_DOES_NOT_NAME_THIS_CONFIG")
        else:
            bound = {"output_roots": cfg["output_roots"], "argv": cfg["argv"], "max_wall_s": cfg["max_wall_s"],
                     "cpu_slots": cfg["cpu_slots"]}
            bound.update({k: adm[k] for k in GO_BOUND_KEYS[4:]})
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


def stability_check(sup, R, reasons):
    adm = sup.cfg["admission"]
    try:
        sh, _, sraw, _ = hash_regular(adm["stability_receipt_path"], SMALL_MAX_BYTES, Deadline(HASH_BUDGET_S), keep=True)
        R["stability_sha256"] = sh
        sr = strict_json(sraw)
        if not isinstance(sr, dict) or sr.get("verdict") != "PASS":
            reasons.append("STABILITY_NOT_PASS")
        nd = sr.get("now_date") if isinstance(sr, dict) else None
        if R.get("date") is None or not isinstance(nd, str) or not DATE_RE.match(nd):
            reasons.append("STABILITY_AGE_UNVERIFIABLE")
        else:
            R["stability_now_date"] = nd
            R["stability_age_s"] = date_age_s(R["date"], nd)
            if not (0 <= R["stability_age_s"] <= adm["stability_max_age_s"]):
                reasons.append("STABILITY_STALE")
    except (OSError, ValueError, UnicodeDecodeError) as ex:
        reasons.append("STABILITY_UNREADABLE %r" % ex)


def admission(sup):
    cfg, adm, R, reasons = sup.cfg, sup.cfg["admission"], {"epoch": time.time()}, []
    R["date"] = sup.date_now("admission")
    R["date_mono"] = time.monotonic()
    if R["date"] is None:
        reasons.append("DATE_HELPER_UNAVAILABLE")
    if TIMEBASE is None or ARGMAX is None:
        reasons.append("LIBPROC_SETUP_FAILED")
    if sup.rec["supervisor_sha256"] is None:
        reasons.append("SUPERVISOR_SOURCE_UNHASHABLE")
    pins = []
    for p in cfg["pins"]:
        try:
            ok = hash_regular(p["path"], PIN_MAX_BYTES, Deadline(HASH_BUDGET_S))[0] == p["sha256"]
        except OSError:
            ok = False
        pins.append([p["path"], ok])
        if not ok:
            reasons.append("PIN_MISMATCH %s" % p["path"])
    R["pins"] = pins
    try:
        devs = {"lane": os.stat(cfg["lane"]).st_dev, "lane_disk_root": os.stat(cfg["lane_disk_root"]).st_dev,
                "TMPDIR": os.stat(cfg["env"]["TMPDIR"]).st_dev}
        for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
            devs["root:" + r] = dev
        R["devices"] = devs
        if len(set(devs.values())) != 1:
            reasons.append("CHARGED_LOCATIONS_ON_DIFFERENT_FILESYSTEMS")
    except OSError as ex:
        reasons.append("DEVICE_CHECK_FAILED %r" % ex)
    for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
        try:
            st = os.lstat(r)
            names = list_root(fd, Deadline(10.0))
        except OSError as ex:
            reasons.append("OUTPUT_ROOT_UNREADABLE %s %r" % (r, ex))
            continue
        if (st.st_dev, st.st_ino) != (dev, ino) or not real_dir_chain(r):
            reasons.append("OUTPUT_ROOT_NOT_REAL_DIR %s" % r)
        if names:
            reasons.append("OUTPUT_ROOT_NOT_EMPTY %s (%d entries)" % (r, len(names)))
    for d in [cfg["env"]["TMPDIR"], cfg["lane"], cfg["lane_disk_root"]] + list(cfg["lane_roots"]):
        if not real_dir_chain(d):
            reasons.append("NOT_A_REAL_DIRECTORY_CHAIN %s" % d)
    read_go(sup, R, reasons)
    stability_check(sup, R, reasons)
    res = adm["reservation_bytes"]
    try:
        fr = sup.free_now()
        R["free"] = fr
        if fr < cfg["launch_free_min_bytes"] + res:
            reasons.append("FREE_BELOW_LAUNCH_MIN")
        if fr - adm["outstanding_reservations_bytes"] - res < HARD["free_floor_min"]:
            reasons.append("FREE_MINUS_RESERVATIONS_BELOW_12E9")
    except OSError as ex:
        reasons.append("STATVFS_FAILED %r" % ex)
    try:
        lb = walk_bytes(cfg["lane_disk_root"], Deadline(WALK_BUDGET_S))
        R["lane_bytes"] = lb
        if lb + adm["lane_outstanding_reservations_bytes"] + res > cfg["lane_disk_ceiling_bytes"]:
            reasons.append("LANE_CEILING")
    except OSError as ex:
        reasons.append("LANE_WALK_FAILED %r" % ex)
    w0 = time.time()
    R["fit_limit_epoch"] = min(w0 + cfg["max_chunk_seconds"] - 120, cfg["owned_compute_settled_by_epoch"] - 180)
    sup.fit_limit_epoch = R["fit_limit_epoch"]
    if w0 + cfg["max_wall_s"] + cfg["settle_s"] + FINALIZE_ALLOWANCE_S > R["fit_limit_epoch"]:
        reasons.append("CHUNK_FIT")
    if TIMEBASE is not None and ARGMAX is not None:
        try:
            c1 = sup.census_complete(CENSUS_BUDGET_S)
            time.sleep(2.0)
            c2 = sup.census_complete(CENSUS_BUDGET_S)
            R["census"] = [{k: c[k] for k in ("pids", "complete", "lane_pids", "lane_rss", "lane_busy",
                                                "lane_busy_pids")} for c in (c1, c2)]
            for c in (c1, c2):
                if not c["complete"]:
                    reasons.append("CENSUS_INCOMPLETE")
                if not sup.limits_ok(c):
                    reasons.append("LANE_LIMITS (busy %d + cpu_slots %d, rss %d)" % (c["lane_busy"], cfg["cpu_slots"],
                                                                                    c["lane_rss"]))
        except (RuntimeError, OSError) as ex:
            reasons.append("CENSUS_FAILED %s" % ex)
    if CANCEL[0] is not None:
        reasons.append("CANCELLED %d" % CANCEL[0])
    if sup.failures_n:
        reasons.append("FAILURE_LATCHED")
    R["reasons"] = reasons
    return R


def freshness(sup, adm_rec, R, reasons, spawn_mono=None):
    """re-checks shared by the commit boundary (fresh /bin/date reading) and the GO linearization (commit-boundary age
    plus monotonic time elapsed since that reading)."""
    cfg, adm = sup.cfg, sup.cfg["admission"]
    w = time.time()
    R["epoch"] = w
    nd = adm_rec.get("stability_now_date")
    if spawn_mono is None:
        R["date"] = sup.date_now("commit_boundary")
        R["date_mono"] = time.monotonic()
        if R["date"] is None or not isinstance(nd, str):
            reasons.append("STABILITY_AGE_UNVERIFIABLE")
        else:
            R["stability_age_s"] = date_age_s(R["date"], nd)
            if not (0 <= R["stability_age_s"] <= adm["stability_max_age_s"]):
                reasons.append("STABILITY_STALE")
    else:
        cb = sup.rec.get("commit_boundary") or {}
        if not _num(cb.get("stability_age_s")) or not _num(cb.get("date_mono")):
            reasons.append("STABILITY_AGE_UNVERIFIABLE")
        else:
            R["stability_age_s_extrapolated"] = cb["stability_age_s"] + (time.monotonic() - cb["date_mono"])
            if not (0 <= R["stability_age_s_extrapolated"] <= adm["stability_max_age_s"]):
                reasons.append("STABILITY_STALE")
    na = adm_rec.get("go_not_after_epoch")
    if not _num(na) or w > na:
        reasons.append("GO_EXPIRED_OR_INVALID")
    res = adm["reservation_bytes"]
    try:
        fr = sup.free_now()
        R["free"] = fr
        if fr < cfg["launch_free_min_bytes"] + res or fr - adm["outstanding_reservations_bytes"] - res < \
                HARD["free_floor_min"]:
            reasons.append("FREE_BELOW_LAUNCH_MIN")
    except OSError as ex:
        reasons.append("STATVFS_FAILED %r" % ex)
    if spawn_mono is None:
        if w + cfg["max_wall_s"] + cfg["settle_s"] + FINALIZE_ALLOWANCE_S > adm_rec["fit_limit_epoch"]:
            reasons.append("CHUNK_FIT")
    else:
        age = time.monotonic() - spawn_mono
        R["spawn_age_s"] = age
        if age > min(GO_MAX_DELAY_S, cfg["max_wall_s"] / 2.0):
            reasons.append("SPAWN_TOO_OLD_FOR_GO")
    if CANCEL[0] is not None:
        reasons.append("CANCELLED %d" % CANCEL[0])
    if sup.failures_n:
        reasons.append("FAILURE_LATCHED")


def commit_boundary(sup, adm_rec):
    R, reasons = {}, []
    freshness(sup, adm_rec, R, reasons)
    R["reasons"] = reasons
    return R


# ---------------------------------------------------------------- supervised run
def run_supervised(sup, child, mono0, epoch0, abs_end):
    cfg = sup.cfg
    sup.keep.append(child)
    sup.child, sup.child_pid = child, child.pid
    ident, why = sup.read_identity(child.pid)
    if ident is None or ident["pgid"] != child.pid or ident["uid"] != MY_UID:
        sup.fail("IDENTITY_CAPTURE_FAILED %s" % (why or ident))
    else:
        sup.ident, sup.u0, sup.pgid0 = ident, ident["uniqueid"], ident["pgid"]
    fd_out, n_out = sup.root_for(cfg["stdout"])
    fd_err, n_err = sup.root_for(cfg["stderr"])
    sup.threads = [sink_thread("stdout", child.stdout, fd_out, n_out, cfg["stdout_cap_bytes"], sup),
                   sink_thread("stderr", child.stderr, fd_err, n_err, cfg["stderr_cap_bytes"], sup)]
    if CANCEL[0] is not None:
        sup.trip("SUPERVISOR_CANCEL_%d" % CANCEL[0])
    if sup.ident is not None and sup.stop is None:
        launch = {"item": cfg["item"], "owner": cfg["owner"], "purpose": cfg["purpose"], "identity": sup.ident,
                  "argv": cfg["argv"], "argv_sha256": hashlib.sha256(json.dumps(cfg["argv"]).encode()).hexdigest(),
                  "argv0_realpath": os.path.realpath(cfg["argv"][0]), "cwd": cfg["lane"], "env": cfg["env"],
                  "mono_spawn": mono0, "epoch_spawn": epoch0, "start_date": sup.rec["commit_boundary"].get("date"),
                  "abs_end_epoch": abs_end, "max_wall_s": cfg["max_wall_s"], "settle_s": cfg["settle_s"],
                  "cpu_slots": cfg["cpu_slots"], "pins": cfg["pins"], "admission": sup.rec["admission"],
                  "commit_boundary": sup.rec["commit_boundary"],
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
            h, ident_lr = publish(fd, name, jbytes(launch), Deadline(PUBLISH_BUDGET_S))
            sup.rec["launch_record_sha256"] = h
            sup.created[cfg["launch_record"]] = ident_lr
        except Exception as ex:
            sup.fail("LAUNCH_RECORD_FAILED %r" % ex)
    G, reasons = {}, []
    try:
        c = sup.census_complete(CENSUS_BUDGET_S)
        G["census"] = {k: c[k] for k in ("pids", "complete", "blocking_live", "lane_pids", "lane_rss", "lane_busy",
                                         "lane_busy_pids")}
        if not c["complete"]:
            reasons.append("CENSUS_INCOMPLETE")
        if c["blocking_live"] != [child.pid]:
            reasons.append("UNEXPECTED_BLOCKING_BEFORE_GO %s" % c["blocking_live"][:10])
        lane_wo_child = dict(c, lane_busy=c["lane_busy"] - (1 if child.pid in c["lane_busy_pids"] else 0))
        if not sup.limits_ok(lane_wo_child):
            reasons.append("LANE_LIMITS_BEFORE_GO")
    except (RuntimeError, OSError) as ex:
        reasons.append("CENSUS_FAILED %s" % ex)
    freshness(sup, sup.rec["admission"], G, reasons, spawn_mono=mono0)
    if sup.ident is None or "launch_record_sha256" not in sup.rec:
        reasons.append("NO_IDENTITY_OR_LAUNCH_RECORD")
    if sup.stop is not None:
        reasons.append("STOP_ALREADY_REQUESTED")
    G["reasons"] = reasons
    sup.rec["go_revalidation"] = G
    go = not reasons
    try:
        if go and CANCEL[0] is None:
            sup.rec["go_linearization_mono"] = time.monotonic()
            child.stdin.write(b"GO\n")
            child.stdin.flush()
            sup.rec["go_written_mono"] = time.monotonic()
        else:
            go = False
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
        sup.fail("GO_NOT_DELIVERED %s" % reasons[:5])
    sup.loop_status = "RUNNING"
    observe(sup, mono0, abs_end, write_samples=True)


def observe(sup, mono0, abs_end, write_samples):
    """bounded observation until a timely clear observation or an expired grace (both latched precisely)."""
    cfg = sup.cfg
    while True:
        sup.reap_child()
        if CANCEL[0] is not None:
            sup.trip("SUPERVISOR_CANCEL_%d" % CANCEL[0])
        c = None
        try:
            c = sup.census(Deadline(CENSUS_BUDGET_S))
            if not c["complete"]:
                sup.census_incomplete += 1
                if sup.child_rc is not None and not c["blocking_live"] and sup.streams_closed():
                    c = sup.census_complete(CENSUS_BUDGET_S)
            sup.max["lane_rss"] = max(sup.max["lane_rss"], c["lane_rss"])
            sup.max["lane_busy"] = max(sup.max["lane_busy"], c["lane_busy"])
            sup.max["blocking_live"] = max(sup.max["blocking_live"], len(c["blocking_live"]))
        except (RuntimeError, OSError) as ex:
            c = None
            sup.fail("CENSUS_FAILED %s" % str(ex)[:400])
        fr = ob = None
        if write_samples:
            try:
                fr = sup.free_now()
                sup.min_free = fr if sup.min_free is None else min(sup.min_free, fr)
            except OSError as ex:
                sup.fail("FREE_UNREADABLE %r" % ex)
            try:
                ob = sup.output_bytes()
                sup.max["output_bytes"] = max(sup.max["output_bytes"], ob)
            except OSError as ex:
                sup.fail("OUTPUT_UNREADABLE %r" % ex)
            if time.monotonic() >= sup.next_walk:
                try:
                    sup.lane_bytes = walk_bytes(cfg["lane_disk_root"], Deadline(WALK_BUDGET_S))
                    sup.max["lane_bytes"] = max(sup.max["lane_bytes"], sup.lane_bytes)
                except OSError as ex:
                    sup.fail("LANE_WALK_FAILED %r" % ex)
                sup.next_walk = time.monotonic() + cfg["lane_walk_s"]
        for name, st in sup.streams.items():
            if st["error"] is not None and not st.get("error_reported"):
                st["error_reported"] = True
                sup.fail("STREAM_%s_ERROR %s" % (name.upper(), st["error"][:200]))
        sup.apply_trips(c, fr, ob)
        sup.reap_child()
        if sup.child_rc is None and (time.monotonic() - mono0 > cfg["max_wall_s"] or time.time() > abs_end):
            sup.trip("DEADLINE")
        if write_samples:
            sup.write_sample({"mono": time.monotonic(), "epoch": time.time(), "rc": sup.child_rc, "free": fr,
                              "out": ob, "lane_bytes": sup.lane_bytes,
                              "census": None if c is None else {k: c[k] for k in (
                                  "pids", "complete", "vanished_n", "blocking_live", "blocking_detail", "owned_live",
                                  "unproved_live", "group_live", "blocking_zombies", "blocking_unmeasured",
                                  "foreign_new_n", "lane_pids", "lane_rss", "lane_busy", "lane_busy_pids",
                                  "mono_done")},
                              "streams": {k: [v["bytes_seen"], v["bytes_written"], v["overflow"], v["closed"]]
                                          for k, v in sup.streams.items()},
                              "stop": None if sup.stop is None else sup.stop["reason"], "trips_n": len(sup.trips),
                              "failures_n": sup.failures_n, "signal_sent": bool(sup.signal and sup.signal.get("sent"))})
        if sup.is_clear(c):
            late = [name for name, cut in sup.grace_cutoffs() if c["mono_done"] > cut]
            if late:
                sup.loop_status = late[0]
                sup.fail(late[0] + " (clear observed after the cutoff)")
            else:
                sup.loop_status = "EXITED"
                sup.clear = {"mono": c["mono_done"], "census_pids": c["pids"]}
            return
        t = time.monotonic()
        for name, cut in sup.grace_cutoffs():
            if t > cut:
                sup.loop_status = name
                sup.fail(name)
                return
        cuts = [cut for _, cut in sup.grace_cutoffs()]
        time.sleep(max(0.0, min([cfg["sample_s"]] + [cut - t for cut in cuts])))


# ---------------------------------------------------------------- finalization, publication, acknowledgment
def finalize(sup, status_note):
    try:
        return _finalize(sup, status_note)
    except BaseException as ex:
        sys.stderr.write("FINALIZE_EXCEPTION %r\n" % ex)
        try:
            fd, name = sup.root_for(sup.cfg["settlement_record"])
            publish_linked(fd, name, jbytes({"settlement": "UNSETTLED", "supervisor": VERSION,
                                             "config_sha256": sup.rec.get("config_sha256"), "receipt": None,
                                             "receipt_sha256": None, "reasons": ["FINALIZE_EXCEPTION %r" % ex]}),
                           Deadline(PUBLISH_BUDGET_S))
        except BaseException as ex2:
            sys.stderr.write("SETTLEMENT_RECORD_FAILED %r\n" % ex2)
        sys.stdout.write(json.dumps({"acknowledged": False, "exit_code": 13, "settlement": "UNSETTLED",
                                     "reason": "FINALIZE_EXCEPTION"}) + "\n")
        return 13


def _finalize(sup, status_note):
    cfg, R = sup.cfg, sup.rec
    launched = sup.child_pid is not None
    R["end_date"] = sup.date_now("end")
    R["end_date_mono"] = time.monotonic()
    unreaped = sup.helpers_unreaped()
    if unreaped:
        sup.fail("HELPER_ALIVE %s" % unreaped)
    if launched:
        sup.reap_child()
        if sup.child_rc is None:
            sup.fail("CHILD_NOT_REAPED")
        try:
            c = sup.census_complete(CENSUS_BUDGET_S)
            R["final_census"] = c
            if not c["complete"]:
                sup.fail("FINAL_CENSUS_INCOMPLETE vanished %s" % c["vanished"])
            if c["blocking_live"]:
                sup.fail("BLOCKING_LIVE %s" % c["blocking_detail"][:10])
            sup.apply_trips(c, None, None)
        except (RuntimeError, OSError) as ex:
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
    dl = Deadline(HASH_BUDGET_S + WALK_BUDGET_S)
    pins_end = []
    for p in cfg["pins"]:
        try:
            pins_end.append([p["path"], hash_regular(p["path"], PIN_MAX_BYTES, dl)[0] == p["sha256"]])
        except OSError:
            pins_end.append([p["path"], False])
    R["pins_at_end"] = pins_end
    if not all(ok for _, ok in pins_end):
        sup.fail("PIN_CHANGED_OR_UNREADABLE")
    inventory = {}
    for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
        try:
            st_fd, st_path = os.fstat(fd), os.lstat(r)
            names = list_root(fd, dl)
        except OSError as ex:
            sup.fail("OUTPUT_ROOT_UNREADABLE %s %r" % (r, ex))
            continue
        if (st_fd.st_dev, st_fd.st_ino) != (dev, ino) or (st_path.st_dev, st_path.st_ino) != (dev, ino) or \
                not real_dir_chain(r):
            sup.fail("OUTPUT_ROOT_CHANGED %s" % r)
        inventory[r] = names
        stray = [n for n in names if n not in sup.allow[r]]
        if stray:
            sup.fail("UNDECLARED_ENTRIES %s %s" % (r, stray[:20]))
    R["output_root_inventory"] = inventory
    arts = {}
    for p in [cfg["stdout"], cfg["stderr"], cfg["launch_record"], cfg["samples"]] + [o["path"] for o in cfg["outputs"]]:
        fd, name = sup.root_for(p)
        try:
            os.stat(name, dir_fd=fd, follow_symlinks=False)
        except FileNotFoundError:
            arts[p] = None
            continue
        except OSError as ex:
            arts[p] = {"error": repr(ex)}
            sup.fail("ARTIFACT_STAT_FAILED %s" % p)
            continue
        try:
            h, size, _, st2 = hash_regular(name, max(cfg["output_trip_bytes"], cfg["samples_cap_bytes"],
                                                     cfg["stdout_cap_bytes"], cfg["stderr_cap_bytes"]), dl, dir_fd=fd)
            arts[p] = {"bytes": size, "sha256": h, "nlink": st2.st_nlink, "birthtime": st2.st_birthtime,
                       "inode": [st2.st_dev, st2.st_ino]}
            if st2.st_nlink != 1:
                sup.fail("ARTIFACT_LINK_COUNT %s %d" % (p, st2.st_nlink))
            if p in sup.created and (st2.st_dev, st2.st_ino) != sup.created[p]:
                sup.fail("EVIDENCE_REPLACED %s" % p)
            if p not in sup.created and sup.epoch_spawn is not None and st2.st_birthtime < sup.epoch_spawn:
                sup.fail("OUTPUT_OLDER_THAN_SPAWN %s" % p)
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
    ob = None
    if launched:
        for o in cfg["outputs"]:
            if o["required"] and arts.get(o["path"]) is None:
                sup.fail("REQUIRED_OUTPUT_MISSING %s" % o["path"])
        for p in (cfg["launch_record"], cfg["samples"], cfg["stdout"], cfg["stderr"]):
            if arts.get(p) is None:
                sup.fail("EVIDENCE_MISSING %s" % p)
        try:
            ob = sup.output_bytes()
            sup.max["output_bytes"] = max(sup.max["output_bytes"], ob)
            sup.lane_bytes = walk_bytes(cfg["lane_disk_root"], Deadline(WALK_BUDGET_S))
        except OSError as ex:
            sup.fail("FINAL_ACCOUNTING_FAILED %r" % ex)
        sup.apply_trips(None, None, ob)
    if launched and R.get("abs_end_epoch") is not None:
        bound = R["abs_end_epoch"] + cfg["sample_s"] + DEADLINE_SLACK_EXTRA_S
        dlt = next((t for t in sup.trips if t["trip"] == "DEADLINE"), None)
        exit_ok = sup.child_exit_epoch is not None and sup.child_exit_epoch <= bound
        trip_ok = dlt is not None and dlt["epoch"] <= bound
        R["deadline_timeliness"] = {"bound_epoch": bound, "exit_observed_epoch": sup.child_exit_epoch,
                                    "deadline_trip_epoch": None if dlt is None else dlt["epoch"]}
        if not (exit_ok or trip_ok):
            sup.fail("DEADLINE_NOT_ENFORCED_IN_TIME")
    cancel_at_decision = CANCEL[0]
    if cancel_at_decision is not None and not any(t["trip"].startswith("SUPERVISOR_CANCEL") for t in sup.trips):
        sup.trips.append({"trip": "SUPERVISOR_CANCEL_LATE", "detail": cancel_at_decision, "mono": time.monotonic(),
                          "epoch": time.time()})
    fd_r, n_r = sup.root_for(cfg["receipt"])
    fd_s, n_s = sup.root_for(cfg["settlement_record"])

    def decide():
        if sup.helpers_unreaped():
            return "UNSETTLED"
        if not launched:
            return "NOT_LAUNCHED"
        return "SETTLED" if sup.failures_n == 0 else "UNSETTLED"

    def serialize(settlement):
        R.update({"mono_decision": time.monotonic(), "epoch_decision": time.time(),
                  "helper_calls": sup.helper_calls, "helper_log": list(sup.helper_log),
                  "helpers": [{k: h[k] for k in ("pid", "state", "rc")} for h in sup.helpers],
                  "trips": sup.trips, "stop_request": sup.stop, "signal": sup.signal, "failures": sup.failures,
                  "failures_n": sup.failures_n, "child_pid": sup.child_pid, "child_returncode": sup.child_rc,
                  "child_wait_status_lost": sup.child_lost, "child_exit_mono": sup.child_exit_mono,
                  "child_exit_epoch": sup.child_exit_epoch, "streams": sup.streams, "max": sup.max,
                  "min_free": sup.min_free, "samples_written": sup.samples_n, "samples_bytes": sup.samples_bytes,
                  "clear": sup.clear, "census_incomplete_count": sup.census_incomplete, "loop_status": sup.loop_status,
                  "status_note": status_note, "cancel_at_decision": cancel_at_decision, "settlement": settlement})
        rb = jbytes(R)
        sb = jbytes({"settlement": settlement, "receipt": cfg["receipt"],
                     "receipt_sha256": hashlib.sha256(rb).hexdigest(), "supervisor": VERSION,
                     "config_sha256": R["config_sha256"], "child_returncode": sup.child_rc, "status_note": status_note,
                     "failures": [f["reason"] for f in sup.failures], "failures_n": sup.failures_n,
                     "trips": [t["trip"] for t in sup.trips], "authority": R["authority"]})
        return rb, sb

    if sup.fit_limit_epoch is not None and time.time() > sup.fit_limit_epoch:
        sup.fail("SETTLEMENT_PAST_CHUNK_LIMIT")
    rb, sb = serialize(decide())
    projected = len(rb) + len(sb)
    try:
        fr = sup.free_now()
        R["final_free"] = fr
        lane_now = sup.lane_bytes if sup.lane_bytes is not None else walk_bytes(cfg["lane_disk_root"],
                                                                                 Deadline(WALK_BUDGET_S))
        remaining_res = cfg["admission"]["reservation_bytes"] - (ob if ob is not None else 0)
        R["publication_budget"] = {"projected_bytes": projected, "free": fr, "lane_bytes": lane_now,
                                   "remaining_reservation": remaining_res}
        if fr - projected < cfg["free_trip_bytes"] or \
                lane_now + cfg["admission"]["lane_outstanding_reservations_bytes"] + projected > \
                cfg["lane_disk_ceiling_bytes"] or projected > remaining_res:
            sup.fail("PUBLICATION_BUDGET")
    except OSError as ex:
        sup.fail("PUBLICATION_BUDGET_UNCHECKABLE %r" % ex)
    settlement = decide()
    rb, sb = serialize(settlement)
    code = {"SETTLED": 0, "NOT_LAUNCHED": 10}.get(settlement, 11)
    pub = Deadline(2 * PUBLISH_BUDGET_S)
    try:
        rsha, _ = publish(fd_r, n_r, rb, pub)
    except Exception as ex:
        sys.stderr.write("RECEIPT_PUBLICATION_FAILED %r\n" % ex)
        sys.stdout.write(json.dumps({"acknowledged": False, "exit_code": 12, "settlement": settlement,
                                     "reason": "RECEIPT_PUBLICATION_FAILED"}) + "\n")
        return 12
    try:
        ssha, _ = publish_linked(fd_s, n_s, sb, pub)
        for r, (fd, dev, ino) in sorted(sup.root_fds.items()):
            os.fsync(fd)
        pub.check("after directory fsync")
    except Exception as ex:
        sys.stderr.write("SETTLEMENT_PUBLICATION_FAILED %r\n" % ex)
        sys.stdout.write(json.dumps({"acknowledged": False, "exit_code": 13, "settlement": settlement,
                                     "receipt_sha256": rsha, "reason": "SETTLEMENT_PUBLICATION_OR_DIRECTORY_SYNC_FAILED"})
                         + "\n")
        return 13
    post_publish_mono = time.monotonic()
    ack = {"acknowledged": True, "exit_code": code, "settlement": settlement, "receipt": cfg["receipt"],
           "receipt_sha256": rsha, "settlement_record": cfg["settlement_record"], "settlement_record_sha256": ssha,
           "post_publish_mono": post_publish_mono, "child_returncode": sup.child_rc,
           "trips": [t["trip"] for t in sup.trips], "failures": [f["reason"] for f in sup.failures][:10],
           "supervisor": VERSION, "config_sha256": R["config_sha256"]}
    run_cancel = any(t["trip"].startswith("SUPERVISOR_CANCEL_") and t["trip"] != "SUPERVISOR_CANCEL_LATE"
                     for t in sup.trips)
    if CANCEL[0] is not None and not run_cancel:
        ack.update({"acknowledged": False, "exit_code": 14, "cancel_before_acknowledgment": CANCEL[0],
                    "cancel_seen_at_decision": cancel_at_decision})
        code = 14
    sys.stdout.write(json.dumps(ack, sort_keys=True) + "\n")
    sys.stdout.flush()
    return code


def main():
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, _cancel)
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    if len(sys.argv) != 2:
        sys.stderr.write("usage: owned_supervisor_v8.py CONFIG.json\n")
        return 2
    cfg_path = os.path.abspath(sys.argv[1])
    try:
        cfg_sha, _, raw, _ = hash_regular(cfg_path, SMALL_MAX_BYTES, Deadline(HASH_BUDGET_S), keep=True)
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
        sup.samples_fd, ident_s = create_exclusive(fd, name)
        sup.created[cfg["samples"]] = ident_s
        sup.rec["samples_opened"] = True
    except OSError as ex:
        cb["reasons"].append("SAMPLES_OPEN_FAILED %r" % ex)
        return finalize(sup, "NOT_LAUNCHED_SAMPLES")
    if CANCEL[0] is not None:
        cb["reasons"].append("CANCELLED %d" % CANCEL[0])
        return finalize(sup, "NOT_LAUNCHED_CANCEL")
    mono0, epoch0 = time.monotonic(), time.time()
    abs_end = epoch0 + cfg["max_wall_s"]
    sup.rec.update({"mono_spawn": mono0, "epoch_spawn": epoch0, "start_date": cb.get("date"), "abs_end_epoch": abs_end})
    sup.epoch_spawn, sup.mono_spawn = epoch0, mono0
    try:
        child = subprocess.Popen(cfg["argv"], cwd=cfg["lane"], env=dict(cfg["env"]), stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, close_fds=True)
    except Exception as ex:
        sup.rec["spawn_error"] = repr(ex)
        cb["reasons"].append("SPAWN_FAILED %r" % ex)
        return finalize(sup, "NOT_LAUNCHED_SPAWN")
    try:
        run_supervised(sup, child, mono0, epoch0, abs_end)
    except BaseException as ex:
        sup.rec["exception"] = repr(ex)
        if sup.child_pid is None:
            sup.keep.append(child)
            sup.child, sup.child_pid = child, child.pid
        sup.fail("SUPERVISOR_EXCEPTION %r" % ex)
        try:
            if sup.stop is None:
                sup.request_stop("SUPERVISOR_EXCEPTION")
            observe(sup, mono0, abs_end, write_samples=False)
        except BaseException as ex2:
            sup.fail("EMERGENCY_OBSERVE_EXCEPTION %r" % ex2)
    return finalize(sup, sup.loop_status)


if __name__ == "__main__":
    sys.exit(main())
