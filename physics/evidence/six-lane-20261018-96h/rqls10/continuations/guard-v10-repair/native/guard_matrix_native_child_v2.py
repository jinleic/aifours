#!/usr/bin/env python3
"""REVIEW CANDIDATE / WRITTEN ONLY. Fixed native qualification workloads, never science.
v2 (guard-v10 native repair): install-path successor of child_v1; workloads unchanged.

Only an individually approved driver/source19 spawn may enter: main CASE,
probe CASE ROLE, helper CASE, or reexec CASE. The external approval SHA is a
child-only environment overlay, not a self-referential hashed authority field.
A helper-shaped negative is NOT /bin/date, is never a clock, and emits no date.
All lifetimes derive from the first entry, survive reexec, and remain <=290s.
"""
import time
ENTRY = time.monotonic()
import ctypes
import errno
import hashlib
import json
import math
import os
import resource
import select
import signal
import stat
import struct
import sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
SELF = LANE + "/code/guard_matrix_native_child_v2.py"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
RSS_CAP = 256 << 20
LIFE = ENTRY + 290.0
WORK = LIFE - 1.0
CANCEL = []
EVENTS = []
RUN = None
REQUEST = None
TRUSTED = None
LP = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
LP.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LP.proc_pidinfo.restype = ctypes.c_int


def packed(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def decode(raw):
    def finite(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError("nonfinite JSON")
        return value
    return json.loads(raw.decode(), object_pairs_hook=pairs, parse_float=finite,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


def error(exc):
    raw = str(exc).encode("utf-8", "surrogateescape")
    return {"type": type(exc).__name__, "errno": getattr(exc, "errno", None), "UTF8_HEX": raw[:8192].hex(),
            "utf8_bytes": len(raw), "text_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE"}


def check(report=False):
    if time.monotonic() >= (LIFE - 0.05 if report else WORK):
        raise OSError("CHILD_COOPERATIVE_DEADLINE")
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_CAP:
        raise OSError("CHILD_RSS_OBSERVED_OVER_256M")


def event(operation, **facts):
    row = {"seq": len(EVENTS), "operation": operation, "scope": "NATIVE_OBSERVATION", "mono": time.monotonic(), **facts}
    if len(EVENTS) >= 128 or len(packed(row)) > 32768:
        raise OSError("CHILD_EVIDENCE_CAP")
    EVENTS.append(decode(packed(row)))
    return row


def directory(path):
    if not path.startswith("/") or os.path.normpath(path) != path:
        raise ValueError("noncanonical directory")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.split("/")[1:]:
            check(True)
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def inode(fd):
    st = os.fstat(fd)
    return [st.st_dev, st.st_ino]


def regular(path, cap=2 << 20):
    pfd = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=pfd)
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or not 0 <= before.st_size <= cap:
            raise ValueError("not bounded regular")
        raw = bytearray()
        while len(raw) < before.st_size:
            check(True)
            b = os.read(fd, min(65536, before.st_size - len(raw)))
            if not b:
                raise OSError("short regular read")
            raw.extend(b)
        after = os.fstat(fd)
        keys = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
        if os.read(fd, 1) or any(getattr(before, k) != getattr(after, k) for k in keys):
            raise OSError("regular changed")
        return {"path": path, "inode": inode(fd), "sha256": sha(raw), "bytes": len(raw), "nlink": before.st_nlink}, bytes(raw)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(pfd)


def write(fd, data, report=False):
    old = os.get_blocking(fd)
    os.set_blocking(fd, False)
    try:
        view = memoryview(data)
        while view:
            check(report)
            try:
                n = os.write(fd, view[:65536])
            except BlockingIOError:
                time.sleep(0.002)
                continue
            if n <= 0:
                raise OSError("zero write")
            view = view[n:]
    finally:
        os.set_blocking(fd, old)


def create(path, data):
    if len(data) > 256 << 10:
        raise OSError("CHILD_ARTIFACT_CAP")
    pfd = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=pfd)
        original = inode(fd)
        write(fd, data, True)
        os.fsync(fd)
        got = os.pread(fd, len(data) + 1, 0)
        if got != data or inode(fd) != original:
            raise OSError("created-descriptor readback mismatch")
        facts = {"path": path, "inode": original, "sha256": sha(got), "bytes": len(got), "nlink": os.fstat(fd).st_nlink}
        os.close(fd)
        fd = None
        os.fsync(pfd)
        return facts
    finally:
        if fd is not None:
            os.close(fd)
        os.close(pfd)


def native_identity(pid):
    def info(flavor, size):
        buf = ctypes.create_string_buffer(size)
        ctypes.set_errno(0)
        n = LP.proc_pidinfo(pid, flavor, 1, buf, size)
        if n != size:
            raise OSError(ctypes.get_errno() or errno.EIO, "native identity bytes")
        return buf.raw
    a, b, c = info(17, 56), info(13, 64), info(17, 56)
    if a[16:40] != c[16:40]:
        raise OSError("identity changed")
    p, pp, pg, status = struct.unpack_from("=IIII", b)
    return {"pid": p, "ppid": pp, "pgid": pg, "status": status,
            "uniqueid": struct.unpack_from("=Q", a, 16)[0], "idversion": struct.unpack_from("=i", a, 32)[0],
            "euid": struct.unpack_from("=I", b, 36)[0], "ruid": struct.unpack_from("=I", b, 44)[0],
            "traced": bool(struct.unpack_from("=I", b, 32)[0] & 2),
            "comm": b[16:32].split(b"\0")[0].decode("utf-8", "replace")}


def authorize(mode, case, role):
    global RUN, REQUEST, TRUSTED, LIFE, WORK
    if mode not in ("main", "probe", "helper", "reexec"):
        raise ValueError("fixed mode only")
    trusted = os.environ.get("RQLS_MATRIX_APPROVAL_SHA256", "")
    if len(trusted) != 64 or any(c not in "0123456789abcdef" for c in trusted):
        raise ValueError("external parent SHA missing")
    run = ROOT + "/" + case
    af, ar = regular(run + "/parent-authorization.json")
    rf, rr = regular(run + "/request.json")
    ap, rq = decode(ar), decode(rr)
    if af["sha256"] != trusted or ap.get("request_sha256") != rf["sha256"] or \
            ap.get("kind") != "rqls10-guard-matrix-invocation-v1" or rq.get("kind") != "rqls10-guard-matrix-request-v1" or \
            set(ap) != set(rq) | {"request_sha256"} or any(packed(ap[k]) != packed(rq[k]) for k in rq if k != "kind"):
        raise ValueError("exact parent authority/request join")
    if rq.get("case") != case or rq.get("scope") != "MODIFIED_QUALIFICATION_FIXTURE" or rq.get("hook_set") != [case]:
        raise ValueError("case/scope/hooks")
    sources = rq["sources"]
    expected = {"supervisor": LANE + "/code/owned_supervisor_v19.py", "driver": LANE + "/code/guard_matrix_native_v2.py",
                "child": SELF, "oracle": LANE + "/code/guard_matrix_native_check_v2.py",
                "case_specs": LANE + "/review/rqls10-matrix-native-v2-cases.json"}
    if set(sources) != set(expected):
        raise ValueError("fixed source set")
    for key, path in expected.items():
        pin = sources[key]
        if set(pin) != {"path", "sha256"} or pin["path"] != path or regular(path)[0]["sha256"] != pin["sha256"]:
            raise ValueError("actual source binding")
    if sources["supervisor"]["sha256"] != SUP_SHA:
        raise ValueError("immutable source19")
    specs = decode(regular(expected["case_specs"])[1])
    if specs.get("kind") != "rqls10-matrix-native-v2-cases" or case not in specs["cases"]:
        raise ValueError("fixed v2 native case catalog")
    spec = specs["cases"][case]
    if sha(packed(spec)) != rq["case_spec_sha256"]:
        raise ValueError("case spec digest")
    if mode == "main" and spec["mode"] != "FULL_ORIGINAL_MAIN_FIXED_HOOKS":
        raise ValueError("main mode not this case")
    if mode == "helper" and spec["family"] not in ("helper_method", "cap"):
        raise ValueError("helper negative not admitted")
    if mode == "probe" and role not in ("final", "ack", "retry1", "retry2", "retry3", "unproved"):
        raise ValueError("fixed probe role")
    if mode == "reexec" and case not in ("nat_platform_startup_reexec", "nat_helper_unverified_identity"):
        raise ValueError("fixed reexec case")
    if mode in ("probe", "helper") and rq["ownership_negative"] is not True:
        raise ValueError("explicit process-negative authority")
    expiry = rq["not_after_epoch"]
    if type(expiry) not in (int, float) or not math.isfinite(expiry) or expiry <= time.time():
        raise ValueError("expired authority")
    for key, path in (("run", run), ("out", run + "/out"), ("tmp", run + "/tmp"), ("scratch", run + "/scratch")):
        fd = directory(path)
        try:
            if rq["anchors"][key] != {"path": path, "inode": inode(fd)}:
                raise ValueError("original current-run anchor")
        finally:
            os.close(fd)
    for key, name in (("config", "config.json"), ("go", "GO.json"), ("stability", "stability.json")):
        if rq[key] != {"path": run + "/" + name, "sha256": regular(run + "/" + name)[0]["sha256"]}:
            raise ValueError("fixed actual input bytes")
    if os.environ.get("RQLS_MATRIX_LIFE_MONO"):
        first = float(os.environ["RQLS_MATRIX_LIFE_MONO"])
        if case not in ("nat_platform_startup_reexec", "nat_helper_unverified_identity") or not ENTRY < first <= ENTRY + 290:
            raise ValueError("inherited original reexec life")
        LIFE = first
    LIFE = min(LIFE, ENTRY + expiry - time.time())
    WORK = LIFE - 1.0
    RUN, REQUEST, TRUSTED = run, rq, trusted
    return spec


def read_stdin(cap=3):
    raw = bytearray()
    os.set_blocking(0, False)
    begin = time.monotonic()
    while True:
        check()
        if CANCEL:
            raise OSError("GO_CANCELLED")
        ready, _, _ = select.select([0], [], [], min(0.05, max(0, WORK - time.monotonic())))
        if not ready:
            continue
        try:
            b = os.read(0, cap + 1 - len(raw))
        except BlockingIOError:
            continue
        if not b:
            return {"raw_hex": raw.hex(), "bytes": len(raw), "sha256": sha(raw), "eof": True,
                    "mono_begin": begin, "mono_eof": time.monotonic()}
        raw.extend(b)
        if len(raw) > cap:
            raise OSError("GO_EXTRA_BYTES")


def sleep_until(target, ignore_cancel=False):
    while time.monotonic() < target:
        check()
        if CANCEL and not ignore_cancel:
            return
        time.sleep(min(0.01, max(0, target - time.monotonic())))


def own_fork(case, detach):
    gate_read, gate_write = os.pipe()
    pid = os.fork()
    if pid:
        registered = {"pid": pid, "parent_pid": os.getpid(), "mono_registered": time.monotonic(),
                      "parent_identity": native_identity(os.getpid()), "detach": detach}
        os.close(gate_read)
        event("native_fork_registered", **registered)
        try:
            create(RUN + "/scratch/helper-fork-registration.json", packed(registered))
            write(gate_write, b"R")
        finally:
            os.close(gate_write)
        return pid
    try:
        os.close(gate_write)
        if detach:
            os.setsid()
        owner = {"kind": "rqls10-native-helper-member-owner-v1", "case": case, "pid": os.getpid(),
                 "pgid": os.getpgrp(), "ppid": os.getppid(), "mono_begin": time.monotonic(),
                 "scope": "MODIFIED_NATIVE_METHOD_NEGATIVE_NOT_CLOCK", "identity": native_identity(os.getpid())}
        create(RUN + "/scratch/helper-member-owner.json", packed(owner))
        os.close(1)
        signal.signal(signal.SIGTERM, lambda s, f: None)
        os.set_blocking(gate_read, False)
        raw, eof = bytearray(), False
        gate_begin = time.monotonic()
        while time.monotonic() < min(WORK, ENTRY + 20.0):
            check()
            try:
                b = os.read(gate_read, 2 - len(raw))
            except BlockingIOError:
                time.sleep(0.002)
                continue
            if not b:
                eof = True
                break
            raw.extend(b)
            if len(raw) > 1:
                raise ValueError("fixed native member gate extra bytes")
        os.close(gate_read)
        if bytes(raw) != b"R" or not eof:
            raise ValueError("member ownership registration gate not complete")
        create(RUN + "/scratch/helper-member-gate.json", packed({"pid": os.getpid(), "mono_begin": gate_begin,
               "mono_end": time.monotonic(), "raw_hex": raw.hex(), "eof": eof, "scope": "FIXTURE_COORDINATION_NOT_GO"}))
        sleep_until(min(WORK, ENTRY + 20.0), True)
        os._exit(0)
    except BaseException:
        os._exit(2)


def helper(case):
    # Deliberately not date_now: this process can only be used by the original
    # helper_probe/cleanup method fixture. Its invalid bytes are never a clock.
    create(RUN + "/scratch/helper-owner.json", packed({"pid": os.getpid(), "pgid": os.getpgrp(),
           "mono": time.monotonic(), "identity": native_identity(os.getpid()), "not_date": True}))
    if case == "nat_helper_bad_output":
        write(1, b"FIXTURE_NOT_A_DATE\n")
        return 0
    if case == "nat_helper_nonzero_exit":
        return 3
    if case == "nat_helper_unverified_identity":
        sleep_until(ENTRY + 0.4, True)
        env = dict(os.environ, RQLS_MATRIX_LIFE_MONO=str(LIFE))
        os.execve(sys.executable, [sys.executable, "-I", "-B", SELF, "reexec", case], env)
    if case in ("nat_helper_live_group", "nat_helper_live_descendant_unproved"):
        own_fork(case, case.endswith("descendant_unproved"))
        if case == "nat_helper_live_group":
            return 0
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        sleep_until(min(WORK, ENTRY + 15.0), True)
        return 0
    if case == "nat_helper_grace_exhaustion":
        signal.signal(signal.SIGTERM, lambda s, f: None)
        sleep_until(min(WORK, ENTRY + 20.0), True)
        return 0
    if case == "nat_cap_helper_term":
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        sleep_until(min(WORK, ENTRY + 15.0), True)
        return 0
    raise ValueError("case has no fixed helper-shaped workload")


def main_work(case, spec, reexec=False):
    start_identity = native_identity(os.getpid())
    startup = {"pid": os.getpid(), "pgid": os.getpgrp(), "sid": os.getsid(0), "ppid": os.getppid(),
               "mask": sorted(int(s) for s in signal.pthread_sigmask(signal.SIG_BLOCK, set())),
               "identity": start_identity, "mono": time.monotonic()}
    report = {"kind": "rqls10-native-child-outcome-v1", "case": case, "scope": "MODIFIED_QUALIFICATION_FIXTURE",
              "approval_sha256": TRUSTED, "owner": startup, "protocol": None, "error": None,
              "observations": EVENTS, "cancel_signals": CANCEL, "selected_status_not_actual_exit": None,
              "science_acceptance": False, "no_date_output": True}
    status = 0
    block = None
    try:
        if case == "nat_platform_fast_exit_zombie":
            event("fast_exit_before_GO", identity=start_identity)
        else:
            if case == "nat_platform_startup_reexec" and not reexec:
                create(RUN + "/scratch/preexec.json", packed(startup))
                while not os.path.lexists(RUN + "/out/launch.json"):
                    check()
                    time.sleep(0.002)
                env = dict(os.environ, RQLS_MATRIX_LIFE_MONO=str(LIFE))
                os.execve(sys.executable, [sys.executable, "-I", "-B", SELF, "reexec", case], env)
            if reexec:
                create(RUN + "/scratch/postexec.json", packed(startup))
            protocol = read_stdin()
            report["protocol"] = protocol
            event("GO_EOF_return", **protocol)
            if protocol["raw_hex"] != b"GO\n".hex():
                raise ValueError("ORDINARY_GO_NOT_EXACT")
            if case == "nat_cap_final_rss":
                before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                block = bytearray(160 << 20)
                for i in range(0, len(block), 4096):
                    block[i] = 1
                    if i % (4 << 20) == 0:
                        check()
                event("bounded_RSS_touch", allocated=len(block), before_peak=before,
                      after_peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, touch_stride=4096)
                sleep_until(min(WORK, time.monotonic() + 25.0))
            else:
                duration = 0.0 if case == "nat_integration_immediate_exit" else 2.0
                sleep_until(min(WORK, time.monotonic() + duration))
            if case == "nat_integration_rc7":
                status = 7
    except BaseException as exc:
        report["error"] = error(exc)
        status = 0 if CANCEL else 6
    report["identity_at_output"] = native_identity(os.getpid())
    report["owner"]["mono_end"] = time.monotonic()
    report["selected_status_not_actual_exit"] = status
    report["observed_maxrss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    created = create(RUN + "/out/child-result.json", packed(report))
    write(1, packed({"kind": "rqls10-native-child-record-v1", "case": case,
                    "selected_status_not_actual_exit": status, "report_sha256": sha(packed(report)), "artifact": created}), True)
    return status


def term(signum, frame):
    if not CANCEL:
        CANCEL.append({"signal": signum, "mono": time.monotonic()})


if __name__ == "__main__":
    try:
        if len(sys.argv) not in (3, 4):
            raise ValueError("fixed MODE CASE [ROLE]")
        mode, case = sys.argv[1:3]
        role = sys.argv[3] if len(sys.argv) == 4 else None
        # For helper negatives this invalid non-date frame deliberately remains
        # in stdout. It is <=256 bytes and cannot become clock metadata.
        frame = {"kind": "rqls10-native-child-owner-v1", "pid": os.getpid(), "pgid": os.getpgrp(),
                 "mono_begin": ENTRY, "scope": "NATIVE_OWNER_BEFORE_WORK", "mode": mode}
        write(1, packed(frame), True)
        spec = authorize(mode, case, role)
        if mode == "helper":
            sys.exit(helper(case))
        if mode == "probe":
            read_stdin(0)  # Only EOF releases this fixed idle observation probe.
            sys.exit(0)
        if mode == "reexec" and case == "nat_helper_unverified_identity":
            create(RUN + "/scratch/helper-postexec.json", packed({"identity": native_identity(os.getpid()),
                   "mono": time.monotonic(), "not_clock": True}))
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            sleep_until(min(WORK, ENTRY + 15.0), True)
            sys.exit(0)
        for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
            signal.signal(sig, term)
        sys.exit(main_work(case, spec, mode == "reexec"))
    except SystemExit:
        raise
    except BaseException as exc:
        try:
            write(2, packed({"kind": "rqls10-native-child-refusal-v1", "error": error(exc)}), True)
        except BaseException:
            pass
        sys.exit(2)
