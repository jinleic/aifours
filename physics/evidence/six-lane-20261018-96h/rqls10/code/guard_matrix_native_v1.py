#!/usr/bin/env python3
"""REVIEW CANDIDATE, WRITTEN ONLY: source19 fixed NATIVE/MIXED finite matrix slice.

CLI: DRIVER CASE PARENT_APPROVAL_SHA256. No preparation, approval, GO, release,
commands, plugins or scheduling are provided. The parent precreates a fresh RUN,
config, GO, stability and exact created-descriptor bindings, then separately
captures actual native exit and complete stdout/stderr. Successful fixture
predicates are not empirical closure, native latency guarantees or science.
Full-main cases run original source19 and its unchanged actual14 terminal AST.
Helper-shaped negatives run original helper methods ONLY, never replace date_now
clock output. Every hook is fixed by CASE and externally pinned, never a plugin.
"""
import time
BEGIN = time.monotonic()
import ast
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
import threading

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
SUP = LANE + "/code/owned_supervisor_v19.py"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
PATHS = {"supervisor": SUP, "driver": LANE + "/code/guard_matrix_native_v1.py",
         "child": LANE + "/code/guard_matrix_native_child_v1.py", "oracle": LANE + "/code/guard_matrix_native_check_v1.py",
         "case_specs": LANE + "/review/rqls10-matrix-native-v1-cases.json"}
RUNTIME = ("nat_runtime_999", "nat_runtime_1000", "nat_runtime_1026")
GO = tuple("nat_go_w%d_%s" % (wall, side) for wall in (10, 200) for side in ("lt", "eq", "gt"))
ACK = tuple("nat_ack_" + x for x in ("clean", "new_unproved", "incomplete", "disappearing_retry", "existing_blocker_subset", "additional_blocker"))
ACK_AGE = ("nat_ack_age_099", "nat_ack_age_100", "nat_ack_age_101")
SIGNALS = tuple("nat_signal_" + s + "_" + p for s in ("term", "int", "hup")
                for p in ("before_helper", "before_main", "go_write", "ack_flush")) + ("nat_pending_after_handled",)
PROTECTED = ("nat_protected_go_expiry", "nat_protected_go_stability", "nat_protected_ack_expiry", "nat_protected_ack_stability",
             "nat_completion_go_deadline", "nat_completion_ack_deadline")
HELPER_FULL = ("nat_helper_timely_success", "nat_helper_late_successful_reap", "nat_helper_pre_spawn_allocation_failure", "nat_helper_registered_pid_setup_failure")
HELPER_METHOD = tuple("nat_helper_" + x for x in ("bad_output", "nonzero_exit", "unverified_identity", "lost_wait", "live_group",
                      "live_descendant_unproved", "missing_eof", "close_error", "grace_exhaustion"))
CAPS = ("nat_cap_final_rss", "nat_cap_initial_main", "nat_cap_helper_term")
PLATFORM_METHOD = ("nat_platform_abi_layout", "nat_platform_mixed_uid_unreadable", "nat_platform_trace_observation", "nat_platform_pid_reuse",
                   "nat_platform_uid_change_observation", "nat_platform_trace_change_observation")
PLATFORM_FULL = ("nat_platform_startup_reexec", "nat_platform_fast_exit_zombie", "nat_platform_session_mask_solewait")
INTEGRATION = ("nat_integration_normal_exit", "nat_integration_immediate_exit", "nat_integration_rc7", "nat_integration_printed_ack_actual14")
DERIVED = ("nat_integration_incomplete_capture", "nat_integration_digest_inode_mismatch", "nat_integration_unresolved_identity", "nat_integration_late_artifact")
CASES = RUNTIME + GO + ACK + ACK_AGE + SIGNALS + PROTECTED + HELPER_FULL + HELPER_METHOD + CAPS + PLATFORM_METHOD + PLATFORM_FULL + \
        ("nat_hardlink_distinct_inode",) + INTEGRATION + DERIVED + ("nat_post_publication_stop_helper",)
METHOD = HELPER_METHOD + PLATFORM_METHOD + ("nat_hardlink_distinct_inode", "nat_cap_helper_term")
OWNERSHIP = ("nat_ack_new_unproved", "nat_ack_incomplete", "nat_ack_disappearing_retry", "nat_ack_existing_blocker_subset", "nat_ack_additional_blocker") + \
            HELPER_METHOD + ("nat_cap_helper_term", "nat_platform_startup_reexec", "nat_platform_fast_exit_zombie")
POSITIVE = ("nat_ack_clean", "nat_helper_timely_success", "nat_platform_session_mask_solewait", "nat_hardlink_distinct_inode",
            "nat_platform_abi_layout", "nat_integration_normal_exit", "nat_integration_immediate_exit", "nat_integration_rc7")
ABI = {"sdk": {"path": "/Library/Developer/CommandLineTools/SDKs/MacOSX26.0.sdk/usr/include/sys/proc_info.h",
               "sha256": "e427fa96b348537b21552b9de71e01039410bcad2cedee5584c5e5fddafd70fc"},
       "private": {"path": LANE + "/tmp/xnu_proc_info_private.h", "sha256": "ccc01e88d5bf47bc9c3f5ba3a25c3e6202bbcd7b86aa967af31d714657571c3b"},
       "implementation": {"path": LANE + "/tmp/xnu_proc_info.c", "sha256": "557092f14fbad3341100f59e0391d2e812c54b79a7404c89b2af97471ad67082"}}
LIMITS = {"max_wall_s": 300, "rss_bytes": 256 << 20, "output_bytes": 16 << 20, "busy_ceiling": 2, "max_loops": 2}
END, WORK_END = BEGIN + 300.0, BEGIN + 285.0
REPORTING = False
RUN = None
REQUEST = None
APPROVAL = None
TRUSTED = None
SPEC = None
ENV = None
STATE = None
EVENTS = []
UNRESOLVED = []
MISSING = []
PROBES = []
EXTRA_FDS = []
DROPPED = 0
EMITTED = {"stdout": 0, "stderr": 0}
LOCK = threading.RLock()
ORIGINAL_STDOUT, ORIGINAL_STDERR = sys.stdout, sys.stderr


def packed(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs(items):
    obj = {}
    for key, value in items:
        if key in obj:
            raise ValueError("duplicate JSON key")
        obj[key] = value
    return obj


def decode(raw):
    def finite(text):
        v = float(text)
        if not math.isfinite(v):
            raise ValueError("nonfinite JSON")
        return v
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_float=finite,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


def same(a, b):
    return packed(a) == packed(b)


def hex64(v):
    return type(v) is str and len(v) == 64 and all(c in "0123456789abcdef" for c in v)


def number(v):
    return type(v) in (int, float) and math.isfinite(v)


def error(exc):
    raw = str(exc).encode("utf-8", "surrogateescape")
    return {"type": type(exc).__name__, "errno": getattr(exc, "errno", None), "UTF8_HEX": raw[:8192].hex(),
            "utf8_bytes": len(raw), "text_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE"}


def check(where):
    if time.monotonic() >= (END if REPORTING else WORK_END):
        raise OSError("COOPERATIVE_ENVELOPE " + where)
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > LIMITS["rss_bytes"]:
        raise OSError("OBSERVED_FIXTURE_RSS_OVER_256M " + where)


def event(operation, scope="NATIVE_OBSERVATION", **facts):
    global DROPPED
    # Observation cannot erase a completed native return, release or side effect.
    with LOCK:
        try:
            row = {"seq": len(EVENTS), "operation": operation, "scope": scope, "mono": time.monotonic(), **facts}
            raw = packed(row)
            if DROPPED or len(EVENTS) >= 4096 or len(raw) > 256 << 10:
                DROPPED += 1
            else:
                EVENTS.append(decode(raw))
        except BaseException:
            DROPPED += 1


def inode(fd):
    st = os.fstat(fd)
    return [st.st_dev, st.st_ino]


def directory(path):
    if type(path) is not str or not path.startswith("/") or os.path.normpath(path) != path:
        raise ValueError("canonical directory required")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.split("/")[1:]:
            check("directory traversal")
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def regular(path, cap=2 << 20):
    pfd, fd = directory(os.path.dirname(path)), None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=pfd)
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or not 0 <= before.st_size <= cap:
            raise ValueError("not bounded regular")
        raw = bytearray()
        while len(raw) < before.st_size:
            check("regular read")
            b = os.read(fd, min(65536, before.st_size - len(raw)))
            if not b:
                raise OSError("short regular read")
            raw.extend(b)
        after = os.fstat(fd)
        if os.read(fd, 1) or any(getattr(before, k) != getattr(after, k) for k in
                                ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")):
            raise OSError("regular read changed")
        return {"path": path, "inode": inode(fd), "bytes": len(raw), "sha256": sha(raw), "nlink": before.st_nlink}, bytes(raw)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(pfd)


def full_write(fd, data):
    counts, view = [], memoryview(data)
    old = os.get_blocking(fd)
    os.set_blocking(fd, False)
    try:
        while view:
            check("full write")
            try:
                n = os.write(fd, view[:65536])
            except BlockingIOError:
                time.sleep(0.002)
                continue
            if n <= 0:
                raise OSError("zero write")
            counts.append(n)
            view = view[n:]
    finally:
        os.set_blocking(fd, old)
    return counts


def inventory(root, facts_only=True):
    rows, seen, total = [], set(), 0
    def walk(path, depth):
        nonlocal total
        if depth > 12 or len(rows) >= 1024:
            raise OSError("inventory cap")
        fd = directory(path)
        try:
            rows.append({"path": path, "directory_inode": inode(fd)})
            for name in sorted(os.listdir(fd)):
                check("current-run inventory")
                st = os.stat(name, dir_fd=fd, follow_symlinks=False)
                full = path + "/" + name
                if stat.S_ISDIR(st.st_mode):
                    walk(full, depth + 1)
                elif stat.S_ISREG(st.st_mode):
                    key = (st.st_dev, st.st_ino)
                    if key not in seen:
                        seen.add(key)
                        total += st.st_size
                    if facts_only:
                        rows.append(regular(full, 16 << 20)[0])
                    else:
                        rows.append({"path": full})
                else:
                    raise OSError("nonregular current-run artifact")
        finally:
            os.close(fd)
    walk(root, 0)
    return rows, total


def room(extra=0):
    if RUN is None:
        return
    _, total = inventory(RUN, False)
    capture = 0
    for name in EMITTED:
        try:
            current = os.stat(RUN + "/driver." + name, follow_symlinks=False).st_size
        except FileNotFoundError:
            current = 0
        capture += max(0, EMITTED[name] - current)
    if total + capture + extra > 12 << 20:
        raise OSError("12M_OWN_WRITE_PLUS_4M_PARENT_RESERVE")


def exclusive(path, data):
    pfd, fd = directory(os.path.dirname(path)), None
    try:
        fd = os.open(os.path.basename(path), os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=pfd)
        created = inode(fd)
        with LOCK:
            room(len(data))
            full_write(fd, data)
        os.fsync(fd)
        got = os.pread(fd, len(data) + 1, 0)
        if got != data or inode(fd) != created:
            raise OSError("exclusive created-descriptor readback mismatch")
        out = {"path": path, "inode": created, "bytes": len(data), "sha256": sha(data), "nlink": os.fstat(fd).st_nlink}
        os.close(fd)
        fd = None
        os.fsync(pfd)
        return out
    finally:
        if fd is not None:
            os.close(fd)
        os.close(pfd)


def wait_until(target, clock=time.monotonic):
    while clock() < target:
        check("fixed real-clock wait")
        time.sleep(max(0.0001, min(0.002, target - clock())))


def await_file(path, seconds=10.0):
    until = min(WORK_END, time.monotonic() + seconds)
    while time.monotonic() < until:
        try:
            return regular(path)
        except (FileNotFoundError, OSError, ValueError):
            time.sleep(0.002)
    MISSING.append("bounded actual fixture barrier not observed: " + path)
    return None


def authorize(case, trusted):
    global RUN, REQUEST, APPROVAL, TRUSTED, SPEC, END, WORK_END
    if case not in CASES or not hex64(trusted):
        raise ValueError("fixed CASE/external SHA required")
    RUN = ROOT + "/" + case
    af, ar = regular(RUN + "/parent-authorization.json")
    rf, rr = regular(RUN + "/request.json")
    if af["sha256"] != trusted:
        raise ValueError("external exact approval SHA")
    ap, rq = decode(ar), decode(rr)
    keys = {"kind", "case", "scope", "sources", "anchors", "allocation", "not_after_epoch", "negative_control", "ownership_negative",
            "hook_set", "config", "go", "stability", "python", "created_facts", "case_spec_sha256", "derived_base", "limits"}
    if set(rq) != keys or set(ap) != keys | {"request_sha256"} or ap["request_sha256"] != rf["sha256"] or \
            ap["kind"] != "rqls10-guard-matrix-invocation-v1" or rq["kind"] != "rqls10-guard-matrix-request-v1" or \
            any(not same(ap[k], rq[k]) for k in keys - {"kind"}):
        raise ValueError("authority exact schema/types/request join")
    if rq["case"] != case or rq["scope"] != "MODIFIED_QUALIFICATION_FIXTURE" or rq["hook_set"] != [case] or \
            rq["negative_control"] is not (case not in POSITIVE) or rq["ownership_negative"] is not (case in OWNERSHIP):
        raise ValueError("fixed case/scope/hook/negative designation")
    if not same(rq["limits"], LIMITS):
        raise ValueError("fixed resource envelope")
    alloc = rq["allocation"]
    if set(alloc) != {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} or \
            any(type(x) is not int or x < 0 for x in alloc.values()) or alloc["bytes"] != 20 << 20 or \
            alloc["cpu_slots"] != (2 if case in OWNERSHIP else 1):
        raise ValueError("parent serialized bounded allocation")
    now = time.time()
    if not number(rq["not_after_epoch"]) or not now < rq["not_after_epoch"] <= now + 300:
        raise ValueError("current finite authority")
    END = min(END, time.monotonic() + rq["not_after_epoch"] - now)
    WORK_END = END - 15.0
    if set(rq["sources"]) != set(PATHS):
        raise ValueError("fixed source set")
    for key, path in PATHS.items():
        pin = rq["sources"][key]
        facts, raw = regular(path)
        if set(pin) != {"path", "sha256"} or pin["path"] != path or pin["sha256"] != facts["sha256"]:
            raise ValueError("actual pinned source bytes: " + key)
        if key == "supervisor" and pin["sha256"] != SUP_SHA:
            raise ValueError("immutable source19")
    specs = decode(regular(PATHS["case_specs"])[1])
    if specs["kind"] != "rqls10-matrix-native-v1-cases" or set(specs["cases"]) != set(CASES) or \
            specs["supervisor"] != {"path": SUP, "sha256": SUP_SHA}:
        raise ValueError("fixed complete native case catalog")
    spec = specs["cases"][case]
    if rq["case_spec_sha256"] != sha(packed(spec)):
        raise ValueError("exact fixed case spec")
    anchors = {"run": RUN, "out": RUN + "/out", "tmp": RUN + "/tmp", "scratch": RUN + "/scratch"}
    if set(rq["anchors"]) != set(anchors):
        raise ValueError("anchor set")
    for key, path in anchors.items():
        fd = directory(path)
        try:
            if not same(rq["anchors"][key], {"path": path, "inode": inode(fd)}):
                raise ValueError("original current-run anchor")
            if key != "run" and os.listdir(fd):
                raise ValueError("fresh empty out/tmp/scratch required")
        finally:
            os.close(fd)
    if os.path.lexists(RUN + "/fixture-outcome.json"):
        raise FileExistsError("one-use outcome exists")
    if set(rq["created_facts"]) != {"config", "go", "stability"}:
        raise ValueError("parent created-descriptor input facts")
    for key, name in (("config", "config.json"), ("go", "GO.json"), ("stability", "stability.json")):
        facts, raw = regular(RUN + "/" + name)
        if not same(rq[key], {"path": facts["path"], "sha256": facts["sha256"]}) or not same(rq["created_facts"][key], facts) or facts["nlink"] != 1:
            raise ValueError("original parent-created current-run input: " + key)
    python = rq["python"]
    if set(python) != {"path", "sha256"} or python["path"] != os.path.realpath(sys.executable) or \
            regular(python["path"], 64 << 20)[0]["sha256"] != python["sha256"]:
        raise ValueError("actual real interpreter bytes")
    cfg = decode(regular(rq["config"]["path"])[1])
    wall = 200.0 if case in GO and "w200" in case else 10.0
    fixed = {"item": case, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE,
             "argv": [python["path"], "-I", "-B", PATHS["child"], "main", case],
             "env": {"PATH": "/usr/bin:/bin", "TMPDIR": RUN + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"},
             "output_roots": [RUN + "/out"], "lane_disk_root": RUN, "lane_roots": [LANE], "pins": [],
             "outputs": [{"path": RUN + "/out/child-result.json", "required": True}], "max_wall_s": wall,
             "settle_s": 20.0, "sample_s": 0.2, "max_chunk_seconds": 10800.0, "rss_projection_bytes": 16 << 20,
             "rss_trip_bytes": (128 << 20) if case == "nat_cap_final_rss" else 256 << 20,
             "free_trip_bytes": 12000000000, "launch_free_min_bytes": 12200000000, "output_trip_bytes": 12 << 20,
             "lane_disk_ceiling_bytes": 64 << 20, "lane_walk_s": 5.0, "busy_limit": 2, "busy_cpu_fraction": 0.5,
             "cpu_slots": alloc["cpu_slots"], "fault_injection": {}, "creation_channel": {},
             "stdout_cap_bytes": 128 << 10, "stderr_cap_bytes": 128 << 10, "samples_cap_bytes": 1 << 20,
             "helper_budget": {"max_calls": 8, "call_budget_s": 2.0, "term_grace_s": 1.0}}
    for key, name in (("stdout", "child.stdout"), ("stderr", "child.stderr"), ("samples", "samples.jsonl"),
                      ("launch_record", "launch.json"), ("receipt", "receipt.json"), ("settlement_record", "settlement.json")):
        fixed[key] = RUN + "/out/" + name
    for key, wanted in fixed.items():
        if key not in cfg or not same(cfg[key], wanted):
            raise ValueError("fixed native config: " + key)
    adm = cfg["admission"]
    expected_adm = {"go_path": RUN + "/GO.json", "stability_receipt_path": RUN + "/stability.json", "reservation_bytes": alloc["bytes"],
                    "outstanding_reservations_bytes": alloc["outstanding_reservations_bytes"],
                    "lane_outstanding_reservations_bytes": alloc["lane_outstanding_reservations_bytes"],
                    "stability_max_age_s": 45.0 if case.endswith("_stability") else 300.0}
    if not same(adm, expected_adm) or not number(cfg["owned_compute_settled_by_epoch"]) or \
            cfg["owned_compute_settled_by_epoch"] < rq["not_after_epoch"] + 1000:
        raise ValueError("fixed admission/fit headroom")
    go = decode(regular(rq["go"]["path"])[1])
    bound = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
    bound.update({k: adm[k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
    expected_go = {"decision": "GO", "item": case, "configs": {rq["config"]["sha256"]: bound},
                   "not_after_epoch": go.get("not_after_epoch"), "stability_receipt_sha256": rq["stability"]["sha256"]}
    if rq["negative_control"]:
        expected_go["qualification_negative"] = {"scenario": case, "kind": "matrix_native", "creation_channel": False}
    if not same(go, expected_go) or not number(go["not_after_epoch"]) or not now < go["not_after_epoch"] <= rq["not_after_epoch"]:
        raise ValueError("fixed exact parent GO and typed config mapping")
    if case in DERIVED:
        base = rq["derived_base"]
        if type(base) is not dict or set(base) != {"case", "approval_sha256", "capture_sha256"} or \
                base["case"] != "nat_integration_normal_exit" or not all(hex64(base[k]) for k in ("approval_sha256", "capture_sha256")):
            raise ValueError("fixed original normal-exit base evidence")
    elif rq["derived_base"] is not None:
        raise ValueError("undeclared derived evidence")
    APPROVAL, REQUEST, TRUSTED, SPEC = ap, rq, trusted, spec
    event("authority_checked", approval_sha256=trusted, request_sha256=rf["sha256"], sources=rq["sources"],
          anchors=rq["anchors"], allocation=alloc, case_spec_sha256=rq["case_spec_sha256"])
    room()
    return cfg


def signal_self(signum, point):
    before = ENV["identify"](os.getpid())
    if before["pid"] != os.getpid() or before["pgid"] != os.getpgrp() or before["euid"] != os.geteuid() or before["ruid"] != os.getuid():
        raise OSError("self signal identity unavailable")
    begin = time.monotonic()
    os.kill(os.getpid(), signum)
    event("native_self_signal", point=point, signum=signum, identity=before, pid=os.getpid(), pgid=os.getpgrp(),
          mono_before=begin, mono_after=time.monotonic(), pending=sorted(int(s) for s in signal.sigpending()),
          source_cancel=dict(ENV["CANCEL"]), only_approved_self=True)


def spawn_probe(role):
    cfg = STATE.cfg
    rd, wr = os.pipe()
    out, childout = os.pipe()
    null = os.open("/dev/null", os.O_RDWR)
    record = {"role": role, "pid": None, "identity": None, "stdin_fd": wr, "stdout_fd": out, "reaped": False,
              "native_wait_result": None, "term_attempted": False, "signal": None, "owner_raw_hex": None}
    PROBES.append(record)
    try:
        argv = [REQUEST["python"]["path"], "-I", "-B", PATHS["child"], "probe", REQUEST["case"], role]
        actions = [(os.POSIX_SPAWN_DUP2, rd, 0), (os.POSIX_SPAWN_DUP2, childout, 1), (os.POSIX_SPAWN_DUP2, null, 2)]
        actions += [(os.POSIX_SPAWN_CLOSE, fd) for fd in (rd, wr, out, childout, null)]
        check("fixed idle probe spawn")
        pid = os.posix_spawn(argv[0], argv, dict(cfg["env"], RQLS_MATRIX_APPROVAL_SHA256=TRUSTED), file_actions=actions,
                             setsid=True, setsigmask=(), setsigdef=(signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGCHLD, signal.SIGPIPE))
        record["pid"] = pid  # No fallible operation between native return and ownership registration.
        record["identity"] = ENV["identify"](pid)
        event("native_fixture_probe_registered", pid=pid, pgid=record["identity"]["pgid"], identity=record["identity"], role=role, argv=argv)
    finally:
        for fd in (rd, childout, null):
            os.close(fd)
    os.set_blocking(out, False)
    raw, until = bytearray(), min(WORK_END, time.monotonic() + 5.0)
    while time.monotonic() < until and b"\n" not in raw:
        try:
            b = os.read(out, 4096 - len(raw))
        except BlockingIOError:
            time.sleep(0.002)
            continue
        if not b:
            break
        raw.extend(b)
    record["owner_raw_hex"] = raw.hex()
    event("native_probe_owner_capture", pid=pid, role=role, raw_hex=raw.hex(), bytes=len(raw), sha256=sha(raw))
    wait_until(time.monotonic() + 0.4)  # Idle, not a CPU workload; avoid startup BUSY measurement artifacts.
    return record


def finish_probe(p):
    if p["pid"] is None or p["reaped"]:
        return
    if p["stdin_fd"] is not None:
        os.close(p["stdin_fd"])
        p["stdin_fd"] = None
    until = min(END - 2, time.monotonic() + 5.0)
    while time.monotonic() < until and not p["reaped"]:
        before = time.monotonic()
        try:
            result = os.waitpid(p["pid"], os.WNOHANG)
        except ChildProcessError as exc:
            p["wait_error"] = error(exc)
            break
        p["last_wait_result"] = result
        if result[0]:
            p["native_wait_result"] = result
            p["reaped"] = True  # Destructive native return precedes every auxiliary observation.
            p["rc"] = os.waitstatus_to_exitcode(result[1])
            p["mono_reaped"] = time.monotonic()
            event("native_probe_reaped", role=p["role"], pid=p["pid"], native_wait_result=list(result),
                  mono_before=before, mono_after=p["mono_reaped"])
            break
        if time.monotonic() > until - 1.0 and not p["term_attempted"]:
            p["term_attempted"] = True
            try:
                identity = ENV["identify"](p["pid"])
                if ENV["fingerprint"](identity) != ENV["fingerprint"](p["identity"]):
                    raise OSError("probe signal identity changed")
                os.killpg(identity["pgid"], signal.SIGTERM)
                p["signal"] = {"sent": True, "identity": identity, "mono_sent": time.monotonic()}
            except BaseException as exc:
                p["signal"] = {"sent": False, "error": error(exc)}
        time.sleep(0.005)
    if p["stdout_fd"] is not None:
        os.close(p["stdout_fd"])
        p["stdout_fd"] = None
    if not p["reaped"]:
        UNRESOLVED.append({"kind": "fixture_probe", "pid": p["pid"], "identity": p["identity"]})


def target_go():
    case = REQUEST["case"]
    if case in GO:
        return STATE.mono_spawn + min(60.0, STATE.cfg["max_wall_s"] / 2.0) + {"lt": -0.01, "eq": 0.0, "gt": 0.01}[case.rsplit("_", 1)[1]]
    if case.endswith("_stability"):
        return STATE.stability_expiry_mono + 0.01
    return time.monotonic() + STATE.authorization["not_after_epoch"] - time.time() + 0.01


class SourceOS:
    def __init__(self):
        self.fds, self.role, self.purpose, self.active_helper = {}, None, None, None
        self.method_negative, self.ack_scan, self.ack_attempt = False, False, 0
        self.fired = set()
    def __getattr__(self, name):
        return getattr(os, name)
    def open(self, path, flags, mode=0o777, *, dir_fd=None):
        case = REQUEST["case"]
        if case == "nat_helper_pre_spawn_allocation_failure" and self.role == "helper" and self.purpose == "start" and path == "/dev/null":
            event("fixed_allocation_fault", "API_RESPONSE_INJECTION", errno=errno.EMFILE, source_site="spawn_registered /dev/null", native_call_made=False)
            raise OSError(errno.EMFILE, "fixed API allocation failure, no native exhaustion")
        check("source open")
        fd = os.open(path, flags, mode, dir_fd=dir_fd)
        self.fds[fd] = {"inode": None, "path": path}
        try:
            self.fds[fd]["inode"] = inode(fd)
        except BaseException as exc:
            UNRESOLVED.append({"kind": "native_open_identity_unavailable", "fd": fd, "error": error(exc)})
        return fd
    def pipe(self):
        case = REQUEST["case"]
        point = "before_helper" if self.role == "helper" and self.purpose == "start" else "before_main" if self.role == "child" else None
        if point is not None and case in SIGNALS and case.endswith(point) and "signal" not in self.fired:
            self.fired.add("signal")
            signal_self({"term": signal.SIGTERM, "int": signal.SIGINT, "hup": signal.SIGHUP}[case.split("_")[2]], point)
        check("source pipe")
        result = os.pipe()
        for fd in result:
            self.fds[fd] = {"inode": None, "path": None}
        for fd in result:
            try:
                self.fds[fd]["inode"] = inode(fd)
            except BaseException as exc:
                UNRESOLVED.append({"kind": "native_pipe_identity_unavailable", "fd": fd, "error": error(exc)})
        event("native_source_pipe", fds=list(result), role=self.role, purpose=self.purpose)
        if case == "nat_helper_missing_eof" and self.method_negative and self.role == "helper" and "hold_eof" not in self.fired:
            self.fired.add("hold_eof")
            hold = os.dup(result[1])
            EXTRA_FDS.append(hold)
            event("native_extra_pipe_writer_held", fd=hold, inode=inode(hold), source_writer=result[1])
        return result
    def fdopen(self, fd, *args, **kwargs):
        stream = os.fdopen(fd, *args, **kwargs)
        self.fds.pop(fd, None)
        return stream
    def posix_spawn(self, path, argv, env, **kwargs):
        if self.role == "helper":
            expected = ([REQUEST["python"]["path"], "-I", "-B", PATHS["child"], "helper", REQUEST["case"]]
                        if self.method_negative and REQUEST["case"] not in ("nat_helper_lost_wait", "nat_helper_missing_eof", "nat_helper_close_error")
                        else ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"])
        elif self.role == "child":
            expected = STATE.cfg["argv"]
        else:
            raise ValueError("fixed registered source role")
        if argv != expected or path != argv[0] or kwargs.get("setsid") is not True or kwargs.get("setsigmask") != ():
            raise ValueError("fixed argv/session/mask")
        if self.role == "child" or self.method_negative:
            env = dict(env, RQLS_MATRIX_APPROVAL_SHA256=TRUSTED)
        check("source registered spawn")
        # Source's original record[pid] assignment is first after this return.
        return os.posix_spawn(path, argv, env, **kwargs)
    def close(self, fd):
        case, h = REQUEST["case"], self.active_helper
        if self.method_negative and h is not None and fd == h.get("stdout_fd") and case == "nat_helper_close_error" and "close_fault" not in self.fired:
            self.fired.add("close_fault")
            event("fixed_close_fault", "API_RESPONSE_INJECTION", fd=fd, inode=inode(fd), errno=errno.EIO,
                  native_close_made=False, descriptor_retained=True)
            raise OSError(errno.EIO, "fixed API close error; owned descriptor remains open")
        before = time.monotonic()
        result = os.close(fd)
        info = self.fds.pop(fd, None)
        event("native_source_close", fd=fd, original=info, mono_before=before, mono_after=time.monotonic())
        return result
    def waitpid(self, pid, options):
        case = REQUEST["case"]
        if options != os.WNOHANG:
            raise ValueError("sole nonblocking wait only")
        h = next((h for h in STATE.helpers if h.get("pid") == pid), None) if STATE is not None else None
        is_main = STATE is not None and pid == STATE.pid
        start = time.monotonic()
        if is_main and case in RUNTIME and "runtime" not in self.fired:
            try:
                zombie = ENV["short"](pid)["status"] == ENV["SZOMB"]
            except OSError:
                zombie = False
            if zombie:
                self.fired.add("runtime")
                target = STATE.mono_spawn + {RUNTIME[0]: 9.99, RUNTIME[1]: 10.00, RUNTIME[2]: 10.26}[case]
                event("native_successful_wait_target", "FIXED_NATIVE_CALL_SCHEDULING", target_mono=target,
                      spawn_mono=STATE.mono_spawn, hook_begin=start, status_observed=ENV["short"](pid))
                wait_until(target)
        if h is not None and self.purpose == "start" and case == "nat_helper_late_successful_reap" and "helper_late" not in self.fired:
            if ENV["short"](pid)["status"] == ENV["SZOMB"]:
                self.fired.add("helper_late")
                begin = time.monotonic()
                wait_until(h["mono_call_deadline"] + 0.01)
                event("native_helper_call_crossing", "FIXED_NATIVE_CALL_SCHEDULING", injection_start=begin,
                      call_deadline=h["mono_call_deadline"], injection_end=time.monotonic(), pid=pid)
        if h is not None and case == "nat_helper_lost_wait" and self.method_negative and "lost_wait" not in self.fired:
            if ENV["short"](pid)["status"] == ENV["SZOMB"]:
                self.fired.add("lost_wait")
                destructive = os.waitpid(pid, os.WNOHANG)
                event("native_competing_reaper", "MODIFIED_NATIVE_METHOD_NEGATIVE_NOT_CLOCK", pid=pid, options=options,
                      native_result=list(destructive), no_recovered_wait_right=True)
        before = time.monotonic()
        try:
            result = os.waitpid(pid, options)
        except BaseException as exc:
            event("native_waitpid", pid=pid, options=options, mono_before=before, mono_after=time.monotonic(), error=error(exc))
            raise
        # Store the destructive result before ANY other fallible work.
        event("native_waitpid", pid=pid, options=options, native_result=list(result), mono_before=before, mono_after=time.monotonic(),
              spawn_mono=STATE.mono_spawn if is_main else h.get("mono_spawn") if h else None,
              target_mono=(STATE.mono_spawn + {RUNTIME[0]: 9.99, RUNTIME[1]: 10.0, RUNTIME[2]: 10.26}[case]) if is_main and case in RUNTIME else None)
        return result
    def write(self, fd, data):
        stdin = STATE is not None and STATE.child is not None and fd == STATE.child.get("stdin_fd")
        if stdin and bytes(data) == b"GO\n":
            case = REQUEST["case"]
            if case in GO or case in PROTECTED and "_go_" in case:
                target = target_go() if case != "nat_completion_go_deadline" else time.monotonic() + 0.03
                start = time.monotonic()
                if case == "nat_completion_go_deadline":
                    self.go_deadline.end = min(self.go_deadline.end, start + 0.02)
                    target = self.go_deadline.end + 0.01
                    event("fixed_original_deadline_clamp", "API_RESPONSE_INJECTION", phase="GO", deadline=self.go_deadline.telemetry())
                wait_until(target)
                event("GO_native_delivery_delay", "FIXED_NATIVE_CALL_SCHEDULING", injection_start=start, target_mono=target,
                      injection_end=time.monotonic(), original_deadline=self.go_deadline.telemetry(),
                      epoch_end_raw=time.time(), authorization=STATE.authorization, stability_expiry_mono=STATE.stability_expiry_mono)
            if (case in SIGNALS and case.endswith("go_write")) or case == "nat_pending_after_handled":
                signum = signal.SIGTERM if case == "nat_pending_after_handled" else {"term": signal.SIGTERM, "int": signal.SIGINT, "hup": signal.SIGHUP}[case.split("_")[2]]
                signal_self(signum, "go_write")
            before = time.monotonic()
            result = os.write(fd, data)
            event("native_GO_write", fd=fd, data_hex=bytes(data).hex(), native_return=result, mono_before=before, mono_after=time.monotonic())
            return result
        return os.write(fd, data)
    def killpg(self, pgid, signum):
        if signum != signal.SIGTERM or STATE is None or not any(
                p is not None and p["pgid"] == pgid for p in [STATE.ident] + [h.get("identity") for h in STATE.helpers]):
            raise ValueError("no broadened source TERM scope")
        before = time.monotonic()
        try:
            result = os.killpg(pgid, signum)
        except BaseException as exc:
            event("native_source_TERM", pgid=pgid, signal=signum, mono_before=before, mono_after=time.monotonic(), error=error(exc))
            raise
        event("native_source_TERM", pgid=pgid, signal=signum, native_return=result, mono_before=before, mono_after=time.monotonic())
        return result


class Output:
    def __init__(self, stream, name, proxy):
        self.stream, self.name, self.proxy = stream, name, proxy
        self.delayed = False
    def __getattr__(self, key):
        return getattr(self.stream, key)
    def write(self, text):
        raw = text.encode("utf-8")
        if EMITTED[self.name] + len(raw) > 4 << 20:
            raise OSError("standard stream cap4M")
        case = REQUEST["case"]
        if self.name == "stdout" and STATE is not None and STATE.ack_output_started and not self.delayed:
            if case in ACK_AGE or case in ("nat_protected_ack_expiry", "nat_protected_ack_stability", "nat_completion_ack_deadline"):
                self.delayed = True
                start, epoch_start = time.monotonic(), time.time()
                if case in ACK_AGE:
                    target = self.proxy.ack_census["mono_complete"] + {ACK_AGE[0]: 0.99, ACK_AGE[1]: 1.0, ACK_AGE[2]: 1.01}[case]
                elif case == "nat_completion_ack_deadline":
                    self.proxy.ack_deadline.end = min(self.proxy.ack_deadline.end, start + 0.02)
                    target = self.proxy.ack_deadline.end + 0.01
                    event("fixed_original_deadline_clamp", "API_RESPONSE_INJECTION", phase="ACK", deadline=self.proxy.ack_deadline.telemetry())
                elif case.endswith("_stability"):
                    target = STATE.stability_expiry_mono + 0.01
                else:
                    target = start + STATE.authorization["not_after_epoch"] - epoch_start + 0.01
                wait_until(target)
                event("ACK_native_output_delay", "FIXED_NATIVE_CALL_SCHEDULING", injection_start=start, injection_start_epoch_raw=epoch_start,
                      target_mono=target, injection_end=time.monotonic(), epoch_end_raw=time.time(),
                      census_mono=self.proxy.ack_census["mono_complete"], original_deadline=self.proxy.ack_deadline.telemetry(),
                      authorization=STATE.authorization, stability_expiry_mono=STATE.stability_expiry_mono)
        before = time.monotonic()
        with LOCK:
            room(len(raw))
            counts = full_write(self.stream.fileno(), raw)
            EMITTED[self.name] += sum(counts)
        event("native_source_" + self.name + "_write", mono_before=before, mono_after=time.monotonic(),
              bytes=len(raw), sha256=sha(raw), native_counts=counts, ack_started=bool(STATE and STATE.ack_output_started))
        return len(text)
    def flush(self):
        case = REQUEST["case"]
        ack = self.name == "stdout" and STATE is not None and STATE.ack_output_started
        if ack and "flush_signal" not in self.proxy.fired and ((case in SIGNALS and case.endswith("ack_flush")) or case == "nat_integration_printed_ack_actual14"):
            self.proxy.fired.add("flush_signal")
            signum = signal.SIGTERM if case == "nat_integration_printed_ack_actual14" else {"term": signal.SIGTERM, "int": signal.SIGINT, "hup": signal.SIGHUP}[case.split("_")[2]]
            signal_self(signum, "ack_flush")
        before = time.monotonic()
        result = self.stream.flush()
        if ack:
            event("native_ACK_flush_return", mono_before=before, mono_after=time.monotonic(),
                  census_mono=self.proxy.ack_census["mono_complete"], pending=sorted(int(s) for s in signal.sigpending()))
        return result


def source_load():
    global ENV
    raw = regular(SUP)[1]
    if sha(raw) != SUP_SHA:
        raise ValueError("source changed before load")
    tree = ast.parse(raw, filename=SUP)
    terminal = tree.body[-1]
    if not isinstance(terminal, ast.If) or (terminal.lineno, terminal.end_lineno) != (2688, 2692):
        raise ValueError("source19 exact terminal AST")
    env = {"__file__": SUP, "__name__": "__native_original19__"}
    exec(compile(ast.Module(body=tree.body[:-1], type_ignores=[]), SUP, "exec"), env)
    proxy = SourceOS()
    env["os"] = proxy
    ENV = env
    event("source_loaded", "MODIFIED_QUALIFICATION_FIXTURE", supervisor_sha256=SUP_SHA,
          wrapper_sha256=REQUEST["sources"]["driver"]["sha256"], config_sha256=REQUEST["config"]["sha256"],
          hook_set=REQUEST["hook_set"], terminal_lines=[2688, 2692])
    return env, proxy, terminal


def install(env, proxy):
    cls = env["Supervisor"]
    init, spawn, date = cls.__init__, env["spawn_registered"], cls.date_now
    def initial(self, cfg, path, digest):
        global STATE
        init(self, cfg, path, digest)
        STATE = self
    cls.__init__ = initial
    def dated(self, purpose):
        old = proxy.purpose
        proxy.purpose = purpose
        try:
            return date(self, purpose)
        finally:
            proxy.purpose = old
    cls.date_now = dated
    def spawned(s, argv, e, role, dl, required_s):
        old = proxy.role
        proxy.role = role
        try:
            record = spawn(s, argv, e, role, dl, required_s)
            if role == "helper":
                proxy.active_helper = record
            pgid, pgid_error = None, None
            try:
                pgid = os.getpgid(record["pid"])
            except OSError as exc:
                pgid_error = error(exc)
            event("native_spawn_registered", pid=record["pid"], pgid=pgid, pgid_error=pgid_error, role=role, argv=argv,
                  source_ledger_registered=record in s.keep, purpose=proxy.purpose, setsid=True, setsigmask=[],
                  setsigdef=sorted(int(x) for x in env["CANCEL_SIGNALS"] | {signal.SIGPIPE, signal.SIGCHLD}))
            if REQUEST["case"] == "nat_helper_registered_pid_setup_failure" and role == "helper" and proxy.purpose == "start":
                begin = time.monotonic()
                wait_until(dl.end + 0.01)
                event("registered_PID_setup_crossing", "API_RESPONSE_INJECTION", pid=record["pid"], injection_start=begin,
                      call_deadline=dl.end, injection_end=time.monotonic(), native_PID_registered=True)
                try:
                    dl.check("fixed registered-PID setup completion")
                except OSError as exc:
                    record["spawn_error"] = repr(exc)
            return record
        finally:
            proxy.role = old
    env["spawn_registered"] = spawned
    original_write = env["write_all"]
    def written(fd, data, dl, on_progress=None):
        if STATE.child is not None and fd == STATE.child.get("stdin_fd"):
            proxy.go_deadline = dl
        try:
            return original_write(fd, data, dl, on_progress)
        except BaseException as exc:
            if STATE.child is not None and fd == STATE.child.get("stdin_fd"):
                event("original_GO_write_all_exception", error=error(exc), deadline=dl.telemetry(),
                      actual_GO_delivery_not_committed=STATE.rec.get("go_delivered") is not True)
            raise
    env["write_all"] = written
    original_publish = env["publish"]
    def published(fd, name, data, dl):
        result = original_publish(fd, name, data, dl)
        for role, target in (("receipt", STATE.cfg["receipt"]), ("staged", STATE.cfg["settlement_record"] + ".staged")):
            if name == os.path.basename(target):
                event("native_original_publication", role=role, path=target, inode=list(result[1]), sha256=result[0], bytes=len(data))
        if name == os.path.basename(STATE.cfg["launch_record"]):
            event("native_original_launch_publish", inode=list(result[1]), sha256=result[0], bytes=len(data))
            case = REQUEST["case"]
            if case in GO or case in ("nat_protected_go_expiry", "nat_protected_go_stability"):
                target = target_go() - 0.6
                if target > time.monotonic():
                    wait_until(target)
                else:
                    MISSING.append("pre-GO census target lead already missed")
            if case == "nat_platform_startup_reexec":
                got = await_file(RUN + "/scratch/postexec.json")
                if got is not None:
                    event("native_startup_reexec_barrier", artifact=got[0], value=decode(got[1]))
        return result
    env["publish"] = published
    launch = env["launch_and_go"]
    def launched(s):
        case = REQUEST["case"]
        if case in ("nat_protected_go_expiry", "nat_protected_go_stability"):
            target = (s.stability_expiry_mono if case.endswith("_stability") else time.monotonic() + s.authorization["not_after_epoch"] - time.time()) - 4.0
            if target > time.monotonic():
                wait_until(target)
        return launch(s)
    env["launch_and_go"] = launched
    original_acquire = cls.acquire_identity
    def acquired(self, pid, source, install=None):
        if source == "main_initial" and REQUEST["case"] == "nat_platform_fast_exit_zombie":
            until = min(WORK_END, time.monotonic() + 10)
            while time.monotonic() < until and env["short"](pid)["status"] != env["SZOMB"]:
                time.sleep(0.002)
            event("native_fast_exit_status_before_initial", identity=env["identify"](pid), source_site=source)
        return original_acquire(self, pid, source, install)
    cls.acquire_identity = acquired
    original_census, full = cls.census, cls.full_census
    def census(self, dl):
        if proxy.ack_scan:
            proxy.ack_attempt += 1
        return original_census(self, dl)
    cls.census = census
    original_observed, stable = cls.observed_identity, cls.identity_stable
    def observed(self, pid, source, known=False):
        if proxy.ack_scan and REQUEST["case"] == "nat_ack_incomplete" and source == "pid_scan":
            p = next((p for p in PROBES if p["role"] == "retry%d" % proxy.ack_attempt and p["pid"] == pid and not p["reaped"]), None)
            if p is not None:
                finish_probe(p)
                event("native_probe_disappeared_before_identification", pid=pid, attempt=proxy.ack_attempt,
                      native_wait_result=p["native_wait_result"])
        return original_observed(self, pid, source, known)
    cls.observed_identity = observed
    def identity_stable(self, pid, before):
        if proxy.ack_scan and REQUEST["case"] == "nat_ack_disappearing_retry":
            p = next((p for p in PROBES if p["pid"] == pid and not p["reaped"]), None)
            if p is not None:
                finish_probe(p)
                event("native_probe_disappeared_after_identity", pid=pid, identity_before=before, native_wait_result=p["native_wait_result"])
        return stable(self, pid, before)
    cls.identity_stable = identity_stable
    def full_census(self, dl):
        case = REQUEST["case"]
        final = self.phase == "FINAL" and not self.in_helper
        ack = final and self.ack_resources is not None
        if final and not ack and case in ("nat_ack_existing_blocker_subset", "nat_ack_additional_blocker") and "final_probe" not in proxy.fired:
            proxy.fired.add("final_probe")
            spawn_probe("final")
        if ack:
            if case == "nat_post_publication_stop_helper" and "postpub" not in proxy.fired:
                proxy.fired.add("postpub")
                if self.failures or self.trips or env["pending_cancel"]() or self.stop is not None:
                    MISSING.append("clean post-publication request_stop entry prerequisite false")
                else:
                    event("post_publication_API_entry", "API_ENTRY_STIMULUS", helper_prefix=self.helper_reports(), accounting=self.ack_resources,
                          stop_before=self.stop, trips_before=self.trips, failures_before=self.failures)
                    self.request_stop("FIXED_POST_PUBLICATION_API_ENTRY")
                    event("post_publication_native_helper_activity", "NATIVE_HELPER_ACTIVITY", helpers=self.helper_reports(),
                          stop=self.stop, signal=self.signal, no_resource_excess_claim=True)
            if case in ("nat_ack_new_unproved", "nat_ack_additional_blocker") and "ack_probe" not in proxy.fired:
                proxy.fired.add("ack_probe")
                spawn_probe("ack")
            if case == "nat_ack_incomplete" and "retry_probes" not in proxy.fired:
                proxy.fired.add("retry_probes")
                for role in ("retry1", "retry2", "retry3"):
                    spawn_probe(role)
            if case == "nat_ack_disappearing_retry" and "retry_probe" not in proxy.fired:
                proxy.fired.add("retry_probe")
                spawn_probe("ack")
            if case in ("nat_protected_ack_expiry", "nat_protected_ack_stability"):
                target = (self.stability_expiry_mono if case.endswith("_stability") else time.monotonic() + self.authorization["not_after_epoch"] - time.time()) - 0.6
                if target > time.monotonic():
                    wait_until(target)
            proxy.ack_scan, proxy.ack_attempt = True, 0
            proxy.ack_deadline = proxy.final_phase
        try:
            result = full(self, dl)
        finally:
            proxy.ack_scan = False
        if ack:
            proxy.ack_census = result
            event("native_ACK_census_return", census=result, attempt_count=proxy.ack_attempt)
        return result
    cls.full_census = full_census
    original_auth = cls.authorization_io
    def authorization(self, dl):
        result = original_auth(self, dl)
        if REQUEST["case"] == "nat_pending_after_handled" and self.phase == "FINAL" and self.ack_resources is not None and self.cancel_handled and "pending_second" not in proxy.fired:
            proxy.fired.add("pending_second")
            signal_self(signal.SIGHUP, "ACK_after_handled_TERM")
        return result
    cls.authorization_io = authorization
    completion = cls.completion_check
    def completed(self, phase, dl):
        before = time.monotonic()
        try:
            result = completion(self, phase, dl)
        except BaseException as exc:
            event("original_completion_exception", phase=phase, mono_before=before, mono_after=time.monotonic(), error=error(exc),
                  go_delivery=self.rec.get("go_delivery_completion"), deadline=dl.telemetry())
            raise
        event("original_completion_return", phase=phase, mono_before=before, mono_after=time.monotonic(), deadline=dl.telemetry())
        return result
    cls.completion_check = completed
    original_age = cls.resource_age
    def age(self, c):
        before = time.monotonic()
        try:
            result = original_age(self, c)
        except BaseException as exc:
            event("original_resource_age_exception", mono_before=before, mono_after=time.monotonic(), census_mono=c["mono_complete"], error=error(exc))
            raise
        event("original_resource_age_return", mono_before=before, mono_after=time.monotonic(), census_mono=c["mono_complete"])
        return result
    cls.resource_age = age
    final_body = env["final_body"]
    def final(s, phase):
        proxy.final_phase = phase
        return final_body(s, phase)
    env["final_body"] = final
    original_reserve = cls.reserve_history
    def reserve(self, kind, new, old=None, witness=None, extra=0):
        case = REQUEST["case"]
        desired = False
        if case == "nat_cap_initial_main":
            desired = type(witness) is dict and witness.get("source") == "main_initial"
        elif case == "nat_cap_final_rss":
            desired = not self.in_helper and "RSS" in self.trips and type(witness) is dict and witness.get("source") == "measurement_final_bracket" and witness.get("identity", {}).get("pid") == self.pid
        elif case == "nat_cap_helper_term":
            desired = proxy.method_negative and self.in_helper and kind == "resource_attempt"
        if desired and "cap" not in proxy.fired:
            proxy.fired.add("cap")
            before = self.history_charge
            self.history_charge = 4 << 20
            event("fixed_history_cap_precharge", "API_CAP_STATE_INJECTION_NOT_NATIVE_COUNT", before_charge=before,
                  injected_charge=self.history_charge, source_kind=kind, witness=witness, native_cap_attainment_claim=False,
                  raw_acquisitions=list(self.raw_acquisitions.values()), main_identity=self.ident, signal=self.signal)
        return original_reserve(self, kind, new, old, witness, extra)
    cls.reserve_history = reserve


def helper_method(cfg, proxy):
    case, env = REQUEST["case"], ENV
    env["validate"](cfg)
    s = env["Supervisor"](cfg, REQUEST["config"]["path"], REQUEST["config"]["sha256"])
    s.open_anchors()
    s.establish_baseline()
    s.authorization_io(env["Deadline"](5, WORK_END))
    if s.date_now("admission") is None:
        MISSING.append("real owned /bin/date admission prerequisite unavailable")
        return {"mode": "ORIGINAL_HELPER_METHODS", "exception": None, "helper": None}
    s.phase, s.in_helper = "RUNNING", True  # Declared native-method prestate, not a full production admission.
    proxy.method_negative = True
    argv = (["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"] if case in ("nat_helper_lost_wait", "nat_helper_missing_eof", "nat_helper_close_error") else
            [REQUEST["python"]["path"], "-I", "-B", PATHS["child"], "helper", case])
    dl, h, exc = s.deadline(2.0), None, None
    event("declared_native_method_helper", "MODIFIED_NATIVE_METHOD_NEGATIVE_NOT_CLOCK", argv=argv,
          original_symbols=["spawn_registered", "Supervisor.helper_probe", "Supervisor.helper_cleanup"], date_assignment_forbidden=True,
          source_phase=s.phase, phase_scope="DECLARED_METHOD_PRESTATE_NOT_PRODUCTION_LAUNCH")
    try:
        h = env["spawn_registered"](s, argv, dict(cfg["env"]), "helper", dl, 3.0)
        proxy.active_helper = h
        h.update(capture=b"", raw_eof=False, stdout_closed=False, capture_overflow=False, initial_identity_valid=False,
                 clock_failed=False, fault_group=False, fault_eof=False, mono_call_start=dl.mono_created, mono_call_deadline=dl.end,
                 call_deadline=dl.telemetry(), date=None)
        while True:
            s.helper_probe(h, dl)
            if case == "nat_helper_unverified_identity" and h.get("identity") is not None and "reexec_seen" not in proxy.fired:
                proxy.fired.add("reexec_seen")
                await_file(RUN + "/scratch/helper-postexec.json", 5.0)
            dl.check("after original helper native-method completion")
            if h["settled"]:
                break
            time.sleep(0.005)
        if case in ("nat_helper_bad_output", "nat_helper_nonzero_exit"):
            raw = regular(SUP)[1]
            tree = ast.parse(raw, filename=SUP)
            cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Supervisor")
            method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "date_now")
            block = next(n for n in method.body if isinstance(n, ast.Try))
            nodes = [n for n in block.body if 1663 <= n.lineno and n.end_lineno <= 1667]
            if len(nodes) != 4 or nodes[0].lineno != 1663 or nodes[-1].end_lineno != 1667:
                raise ValueError("exact original bad-output AST fragment")
            exec(compile(ast.Module(body=nodes, type_ignores=[]), SUP, "exec"), dict(env, h=h))
    except BaseException as e:
        exc = error(e)
        event("original_helper_method_exception", error=exc, helper_pid=None if h is None else h["pid"])
        s.fail("HELPER_CALL_FAILED", type(e).__name__)
        if h is not None:
            s.helper_cleanup(h)
    finally:
        s.in_helper = False
        for fd in list(EXTRA_FDS):
            os.close(fd)
            EXTRA_FDS.remove(fd)
            event("native_extra_pipe_writer_closed", fd=fd)
    if h is not None:
        event("native_helper_method_end", helper=s.helper_reports()[-1], failure_codes=sorted(s.failure_keys),
              history_halted=s.history_halted, no_date_metadata=h.get("date") is None)
    return {"mode": "ORIGINAL_HELPER_METHODS", "exception": exc, "helper": None if h is None else s.helper_reports()[-1],
            "source_date_now_not_replaced": True, "negative_argv": argv}


def platform_method(cfg):
    env, case = ENV, REQUEST["case"]
    if case == "nat_platform_abi_layout":
        facts = {key: regular(pin["path"])[0] for key, pin in ABI.items()}
        if any(facts[k]["sha256"] != ABI[k]["sha256"] for k in ABI):
            MISSING.append("pinned ABI/header bytes absent or changed")
            return {"mode": "ORIGINAL_PLATFORM_METHODS", "exception": None}
        p = os.getpid()
        raws = {str(flavor): env["pidinfo"](p, flavor, size, flavor in (3, 13, 17)).hex()
                for flavor, size in ((17, 56), (13, 64), (4, 96), (3, 136), (9, 2352))}
        event("native_ABI_layout", pinned_files=facts, raw_by_flavor=raws, original_identity=env["identify"](p),
              original_task=list(env["task_of"](p)), original_start_epoch_raw=env["start_of"](p),
              original_cwd=env["cwd_of"](p), original_argv=env["argv_of"](p, env["argmax"]()),
              native_reference={"pid": p, "ppid": os.getppid(), "pgid": os.getpgrp(), "euid": os.geteuid(), "ruid": os.getuid(),
                                "cwd": os.getcwd(), "argv": sys.orig_argv, "maxrss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
              timebase=env["timebase"](), argmax=env["argmax"]())
        return {"mode": "ORIGINAL_PLATFORM_METHODS", "exception": None}
    s = env["Supervisor"](cfg, REQUEST["config"]["path"], REQUEST["config"]["sha256"])
    s.open_anchors()
    seen, matches = {}, []
    continuous = case in ("nat_platform_pid_reuse", "nat_platform_uid_change_observation", "nat_platform_trace_change_observation")
    until = min(WORK_END - 2, time.monotonic() + (30.0 if continuous else 2.0))
    while time.monotonic() < until:
        dl = env["Deadline"](2, until)
        for pid in env["all_pids"](dl):
            try:
                before = env["identify"](pid)
            except OSError as exc:
                event("native_readonly_identity_missing", pid=pid, error=error(exc))
                continue
            prior = seen.get(pid)
            seen[pid] = before
            if case == "nat_platform_pid_reuse" and prior is not None and prior["uniqueid"] != before["uniqueid"]:
                matches.append({"prior": prior, "current": before})
                event("native_real_PID_reuse", prior=prior, current=before)
            elif case in ("nat_platform_uid_change_observation", "nat_platform_trace_change_observation") and prior is not None and prior["uniqueid"] == before["uniqueid"]:
                keys = ("euid", "ruid") if case == "nat_platform_uid_change_observation" else ("traced",)
                if any(prior[k] != before[k] for k in keys):
                    matches.append({"prior": prior, "current": before})
                    event("native_existing_metadata_change", prior=prior, current=before, changed_keys=list(keys),
                          no_credential_or_trace_change=True)
            elif case == "nat_platform_trace_observation" and before["traced"]:
                after = env["identify"](pid)
                matches.append({"before": before, "after": after})
                event("native_existing_trace_observation", before=before, after=after, no_trace_change=True)
            elif case == "nat_platform_mixed_uid_unreadable" and (before["euid"] == os.getuid() or before["ruid"] == os.getuid()) and before["euid"] != before["ruid"]:
                for name, fn in (("cwd", lambda: env["cwd_of"](pid)), ("argv", lambda: env["argv_of"](pid, s.arg_max)), ("task", lambda: env["task_of"](pid))):
                    try:
                        value, exc = fn(), None
                    except OSError as e:
                        value, exc = None, error(e)
                    after = env["identify"](pid)
                    event("native_existing_mixed_UID_read", before=before, after=after, operation_target=name, native_result=value,
                          error=exc, no_credential_or_trace_change=True)
                    if exc is not None and exc["errno"] in (errno.EPERM, errno.EACCES) and env["fingerprint"](before) == env["fingerprint"](after):
                        matches.append({"before": before, "after": after, "error": exc})
        if matches or not continuous:
            break
        time.sleep(0.05)
    event("native_readonly_prerequisite_scan", case=case, distinct_pids=len(seen), matches=matches,
          mono_scan_end=time.monotonic(), no_spawn_no_credentials_no_trace_no_PID_pressure=True)
    if not matches:
        MISSING.append({"nat_platform_pid_reuse": "genuine native PID reuse during bounded read-only observation",
                        "nat_platform_uid_change_observation": "genuine existing same-incarnation real/effective UID change, no forced credentials",
                        "nat_platform_trace_change_observation": "genuine existing same-incarnation trace flag change, no forced trace mutation",
                        "nat_platform_trace_observation": "already-traced native identity; no trace mutation permitted",
                        "nat_platform_mixed_uid_unreadable": "already-existing same-real/effective mixed-UID process with genuine unreadability"}[case])
    return {"mode": "ORIGINAL_PLATFORM_METHODS", "exception": None, "matches": matches}


def hardlink_method(cfg):
    env = ENV
    s = env["Supervisor"](cfg, REQUEST["config"]["path"], REQUEST["config"]["sha256"])
    s.open_anchors()
    payload = b"same fixed native inode charge bytes\n" * 19
    a = exclusive(RUN + "/tmp/a.bin", payload)
    pfd = directory(RUN + "/tmp")
    try:
        os.link("a.bin", "alias.bin", src_dir_fd=pfd, dst_dir_fd=pfd, follow_symlinks=False)
        os.fsync(pfd)
    finally:
        os.close(pfd)
    b = exclusive(RUN + "/tmp/distinct.bin", payload)
    alias = regular(RUN + "/tmp/alias.bin")[0]
    original = regular(RUN + "/tmp/a.bin")[0]
    total = env["walk_fd"](s.tmp_fd, s.lane_id[0], env["Deadline"](5, WORK_END))
    event("native_hardlink_charge", payload_sha256=sha(payload), payload_bytes=len(payload), original=original, alias=alias,
          created_original=a, distinct=b, source_walk_total=total, raw_path_sum=3 * len(payload),
          publication_scope="METHOD_ONLY; guardian does not accept arbitrary multilink output artifacts; staged pair rule unchanged")
    return {"mode": "ORIGINAL_WALK_METHOD", "return": total, "exception": None}


def derived_fixture():
    base = REQUEST["derived_base"]
    root = ROOT + "/" + base["case"]
    af, _ = regular(root + "/parent-authorization.json")
    cf, cr = regular(root + "/parent-capture.json")
    if af["sha256"] != base["approval_sha256"] or cf["sha256"] != base["capture_sha256"]:
        raise ValueError("derived base externally pinned actual evidence")
    capture = decode(cr)
    out = {"mode": "FIXED_ORACLE_NEGATIVE_FRESH_COPY", "base": base, "base_run": root,
           "negative_scope": "ORACLE_INPUT_NOT_NATIVE_SOURCE_OUTCOME", "objects": {}}
    case = REQUEST["case"]
    if case == "nat_integration_incomplete_capture":
        original, raw = regular(root + "/driver.stdout", 4 << 20)
        copy = exclusive(RUN + "/scratch/incomplete.stdout", raw[:-1])
        out["objects"] = {"original": original, "copy": copy, "original_capture": capture["stdout"]}
    elif case == "nat_integration_digest_inode_mismatch":
        original, raw = regular(root + "/out/receipt.json", 4 << 20)
        copy = exclusive(RUN + "/scratch/same-content-receipt.json", raw)
        out["objects"] = {"original": original, "copy": copy, "expected_original_inode": original["inode"]}
    elif case == "nat_integration_unresolved_identity":
        # Genuine live owner acquisition, explicitly inserted only into a fresh
        # verifier-negative input; never claimed as original supervisor evidence.
        identity = ENV["identify"](os.getpid())
        _, raw = regular(root + "/fixture-outcome.json", 8 << 20)
        obj = decode(raw)
        obj["unresolved"] = [{"kind": "ORACLE_NEGATIVE_ACTUAL_LIVE_OWNER", "identity": identity}]
        copy = exclusive(RUN + "/scratch/unresolved-outcome.json", packed(obj))
        out["objects"] = {"copy": copy, "actual_identity": identity, "scope": "ORACLE_NEGATIVE_INPUT_INSERTION"}
    else:
        before = []
        pfd = directory(RUN + "/scratch")
        try:
            before = sorted(os.listdir(pfd))
        finally:
            os.close(pfd)
        before_mono = time.monotonic()
        extra = exclusive(RUN + "/scratch/late.bin", b"fixed late artifact after empty captured inventory\n")
        out["objects"] = {"before_names": before, "before_mono": before_mono, "late_artifact": extra,
                          "reference_scope": "FRESH_ORACLE_NEGATIVE_INVENTORY_NOT_OLD_RUN_MUTATION"}
    event("fresh_oracle_negative_bytes", "ORACLE_INPUT_NOT_NATIVE_SOURCE_OUTCOME", **out)
    return out


def state_view():
    if STATE is None:
        return None
    return {"rec": STATE.rec, "reconciliation": STATE.reconciliation_evidence(), "failure_codes": sorted(STATE.failure_keys),
            "trips": STATE.trips, "pid": STATE.pid, "group": STATE.group, "identity": STATE.ident, "rc": STATE.rc,
            "stop": STATE.stop, "signal": STATE.signal, "clear": STATE.clear, "cancel_handled": STATE.cancel_handled,
            "go_delivered": STATE.rec.get("go_delivered"), "ack_output_started": STATE.ack_output_started,
            "created": {p: list(ident) for p, ident in STATE.created.items()},
            "keep": [{k: v for k, v in r.items() if k not in ("capture", "stdout", "stderr")} for r in STATE.keep]}


def settle_fixture_ownership(proxy):
    for p in PROBES:
        finish_probe(p)
    for fd in list(EXTRA_FDS):
        os.close(fd)
        EXTRA_FDS.remove(fd)
    # Original helpers may intentionally remain unresolved. Never recover wait
    # rights or emit an extra TERM after the source's one attempt. Their fixed
    # own lifetimes, raw identities and parent endedness obligations survive.
    if STATE is not None:
        for r in STATE.keep:
            if r.get("pid") is not None and not r.get("leader_reaped"):
                UNRESOLVED.append({"kind": "source_owned_process", "pid": r["pid"], "role": r["role"],
                                   "identity": r.get("identity") or STATE.ident, "wait_lost": r.get("wait_lost")})
        for thread in STATE.threads:
            if thread.is_alive():
                UNRESOLVED.append({"kind": "source_sink_thread", "name": thread.name})
        member = RUN + "/scratch/helper-member-owner.json"
        if os.path.lexists(member):
            facts, raw = regular(member)
            row = decode(raw)
            event("native_helper_member_original_record", artifact=facts, value=row)
            # Finite read-only observation of this fixed self-expiring member;
            # no own wait right exists after leader exit, no broadened TERM.
            until = min(END - 3.0, time.monotonic() + 22.0)
            alive = None
            while time.monotonic() < until:
                try:
                    alive = ENV["identify"](row["pid"])
                except ProcessLookupError:
                    alive = None
                    break
                except OSError as exc:
                    if exc.errno == errno.ESRCH:
                        alive = None
                        break
                    UNRESOLVED.append({"kind": "member_end_observation", "error": error(exc)})
                    break
                if alive["uniqueid"] != row["identity"]["uniqueid"]:
                    break
                time.sleep(0.02)
            if alive is not None and alive["uniqueid"] == row["identity"]["uniqueid"]:
                UNRESOLVED.append({"kind": "fixture_member_still_observable_after_bound", "original": row["identity"], "current": alive})
            event("native_helper_member_end_observation", pid=row["pid"], last_identity=alive,
                  parent_must_independently_prove_ended=True)
    if any(x.get("kind") == "source_sink_thread" for x in UNRESOLVED):
        return
    for fd, facts in list(proxy.fds.items()):
        if fd < 3:
            continue
        try:
            if inode(fd) == facts["inode"]:
                os.close(fd)
                event("native_fixture_releases_source_FD", fd=fd, original=facts)
            else:
                UNRESOLVED.append({"kind": "source_FD_identity_changed", "fd": fd, "original": facts})
        except OSError as exc:
            event("source_FD_release_error", fd=fd, error=error(exc))
        proxy.fds.pop(fd, None)


def outcome(case, source_outcome, selected, full):
    if DROPPED:
        UNRESOLVED.append({"kind": "raw_event_trace_dropped", "count": DROPPED})
    artifacts = []
    for root in (RUN + "/out", RUN + "/tmp", RUN + "/scratch"):
        artifacts.extend(inventory(root)[0])
    value = {"kind": "rqls10-guard-matrix-outcome-v1", "case": case, "scope": "MODIFIED_QUALIFICATION_FIXTURE",
             "bindings": {"approval_sha256": TRUSTED, "request_sha256": APPROVAL["request_sha256"],
                          **{k: REQUEST[k] for k in ("sources", "anchors", "allocation", "config", "go", "stability", "python", "created_facts",
                                                    "hook_set", "negative_control", "ownership_negative", "case_spec_sha256", "derived_base")}},
             "owner": {"pid": os.getpid(), "pgid": os.getpgrp(), "mono_begin": BEGIN, "mono_end": time.monotonic()},
             "observations": EVENTS, "source_outcome": source_outcome, "source_state": state_view(), "artifacts": artifacts,
             "fixture_processes": PROBES, "missing_prerequisites": MISSING, "unresolved": UNRESOLVED,
             "original_main_called": full, "selected_status_not_actual_exit": selected,
             "terminal": {"source_sha256": SUP_SHA, "ast_lines": [2688, 2692], "unchanged": full},
             "observed_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "limits": LIMITS,
             "no_empirical_closure": True, "science_acceptance": False,
             "authority": "NO_GO_NO_ADMISSION_NO_RELEASE_NO_SCIENCE"}
    raw = packed(value)
    if len(raw) > 8 << 20:
        raise OSError("outcome cap8M")
    exclusive(RUN + "/fixture-outcome.json", raw)


def run(case, trusted):
    global REPORTING
    cfg = authorize(case, trusted)
    env, proxy, terminal = source_load()
    install(env, proxy)
    full = case not in METHOD + DERIVED
    original_main = env["main"]
    sys.stdout, sys.stderr = Output(ORIGINAL_STDOUT, "stdout", proxy), Output(ORIGINAL_STDERR, "stderr", proxy)
    def fixture_main():
        global REPORTING
        selected, source_outcome = 0, None
        try:
            if case in DERIVED:
                source_outcome = derived_fixture()
            elif case in HELPER_METHOD or case == "nat_cap_helper_term":
                source_outcome = helper_method(cfg, proxy)
            elif case in PLATFORM_METHOD:
                source_outcome = platform_method(cfg)
            elif case == "nat_hardlink_distinct_inode":
                source_outcome = hardlink_method(cfg)
            else:
                argv = sys.argv
                sys.argv = [SUP, REQUEST["config"]["path"]]
                try:
                    selected = original_main()
                finally:
                    sys.argv = argv
                source_outcome = {"mode": "FULL_ORIGINAL_MAIN_FIXED_HOOKS", "selected_source_return_not_actual_exit": selected, "exception": None}
        except BaseException as exc:
            selected = 2
            source_outcome = {"mode": "FIXTURE_EXCEPTION", "exception": error(exc)}
            UNRESOLVED.append({"kind": "fixture_exception", "error": error(exc)})
        REPORTING = True
        try:
            settle_fixture_ownership(proxy)
            outcome(case, source_outcome, selected, full)
        except BaseException as exc:
            full_write(2, packed({"kind": "NATIVE_FIXTURE_REPORTING_INCOMPLETE", "error": error(exc)}))
        return selected
    env["main"], env["__name__"] = fixture_main, "__main__"
    # Includes source19's os._exit(14); NEVER substitute selected status for the
    # parent's actual native exit, and never allow CPython flush to turn14 to120.
    exec(compile(ast.Module(body=[terminal], type_ignores=[]), SUP, "exec"), env)


if __name__ == "__main__":
    owner = {"kind": "rqls10-matrix-owner-v1", "pid": os.getpid(), "pgid": os.getpgrp(), "mono_begin": BEGIN,
             "scope": "NATIVE_OWNER_RECORD_BEFORE_WORK_NOT_GUARDIAN_SUMMARY"}
    raw = packed(owner)
    full_write(1, raw)
    EMITTED["stdout"] = len(raw)
    try:
        if len(sys.argv) != 3:
            raise ValueError("CASE PARENT_APPROVAL_SHA256 required")
        run(sys.argv[1], sys.argv[2])
    except SystemExit:
        raise
    except BaseException as exc:
        full_write(2, packed({"kind": "NATIVE_MATRIX_AUTHORITY_OR_ENVELOPE_REFUSAL", "error": error(exc)}))
        sys.exit(2)
