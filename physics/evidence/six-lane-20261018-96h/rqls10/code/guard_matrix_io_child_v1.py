#!/usr/bin/env python3
"""REVIEW CANDIDATE / WRITTEN ONLY. Fixed wire/mutation/channel child; no numerical runtime or forks.

CLI (only source19 launches it): CHILD wire|mutation|channel CASE_ID.
External parent SHA is the fixed RQLS_MATRIX_APPROVAL_SHA256 child-only overlay.
Exact child12 bytes are pinned below and in the external parent-approved review source set.
Its original wait_go/mutate_original execute only after exact external authority.
Channel mode observes the original mutation-channel parser, never mutates a target.
"""
import time
ENTRY = time.monotonic()
import ast
import hashlib
import json
import math
import os
import resource
import signal
import stat
import sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
BASE = LANE + "/code/guard_qual_child_v12.py"
BASE_SHA = "e3a8006890a164d36fdacbadc6e63b64c87302ec46149c7f3a6c731e1a3e186b"
SELF = LANE + "/code/guard_matrix_io_child_v1.py"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
MUTATIONS = ("io_mutation_pin_before_manifest", "io_mutation_pin_before_child_open",
             "io_mutation_launch_before_manifest", "io_mutation_launch_before_child_open")
AUTH = tuple("io_auth_" + a + "_" + p for p in ("helper", "main", "go", "ack") for a in ("replace", "revoke"))
PUB = tuple("io_pub_" + p + "_" + r for p in ("write", "fsync", "close", "readback", "dirsync")
            for r in ("error", "late")) + ("io_pub_readback_mismatch", "io_pub_short_write")
WIRE = AUTH + PUB + ("io_staged_same_content", "io_account_pre_payload", "io_account_pre_b", "io_account_pre_end",
                    "io_account_post_end", "io_post_ack_stderr_write", "io_post_ack_stderr_flush",
                    "io_post_ack_stderr_persistent_write", "io_post_ack_stderr_persistent_flush", "io_channel_ordinary")
EXTRA = ("io_extra_write_short", "io_extra_write_zero", "io_extra_write_error", "io_extra_write_late",
         "io_extra_close_error", "io_extra_close_late", "io_extra_go_age", "io_extra_deadline", "io_extra_expiry") + \
        tuple("io_extra_signal_" + sig + "_" + op for sig in ("term", "int", "hup") for op in ("write", "close"))


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return set(a) == set(b) and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def original_created(wanted, actual):
    if not isinstance(wanted, dict) or set(wanted) != {"path", "inode", "bytes", "sha256", "nlink", "creation_ordinal"} or \
            type(wanted["creation_ordinal"]) is not int or wanted["creation_ordinal"] < 0 or \
            not all(typed_equal(wanted[k], actual[k]) for k in ("path", "inode", "bytes", "sha256", "nlink")) or \
            type(wanted["nlink"]) is not int or wanted["nlink"] != 1:
        raise ValueError("original created descriptor continuity")

LIFE = ENTRY + 60
DEADLINE = LIFE - 0.25
CANCELLED = False
REPORTING = False
EVENTS = []
TRUNCATED = [0]


def check(where):
    if (CANCELLED and not REPORTING) or time.monotonic() >= (LIFE - 0.05 if REPORTING else DEADLINE):
        raise OSError("CHILD_COOPERATIVE_DEADLINE_OR_TERM " + where)
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 256 << 20:
        raise OSError("CHILD_RSS_OVER_256M")


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


def packed(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def err(exc):
    raw = str(exc).encode("utf-8", "surrogateescape")
    return {"type": type(exc).__name__, "errno": getattr(exc, "errno", None),
            "UTF8_HEX": raw[:16384].hex(), "utf8_bytes": len(raw),
            "text_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE"}


def event(operation, **facts):
    # Never raises into frozen base-method paths; truncation is reported as unresolved evidence.
    value = {"seq": len(EVENTS), "operation": operation, "scope": "NATIVE_OBSERVATION",
             "mono": time.monotonic(), **facts}
    try:
        raw = packed(value)
    except (TypeError, ValueError):
        raw = None
    if raw is None or len(EVENTS) >= 512 or len(raw) > 1 << 16:
        TRUNCATED[0] += 1
    else:
        EVENTS.append(decode(raw))
    return value


def directory(path):
    if not path.startswith("/") or os.path.normpath(path) != path:
        raise ValueError("noncanonical path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for name in path.split("/")[1:]:
            check("directory traversal")
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def inode(fd):
    value = os.fstat(fd)
    return [value.st_dev, value.st_ino]


def regular(path, cap=1 << 20):
    parent = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or not 0 <= st.st_size <= cap:
            raise ValueError("not bounded regular")
        raw = bytearray()
        while len(raw) < st.st_size:
            check("regular read")
            part = os.read(fd, min(65536, st.st_size - len(raw)))
            if not part:
                raise OSError("short read")
            raw.extend(part)
        end = os.fstat(fd)
        if os.read(fd, 1) or (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns) != \
                (end.st_dev, end.st_ino, end.st_size, end.st_mtime_ns, end.st_ctime_ns):
            raise OSError("changed regular")
        named = os.stat(os.path.basename(path), dir_fd=parent, follow_symlinks=False)
        if (named.st_dev, named.st_ino, named.st_size, named.st_mtime_ns, named.st_ctime_ns) != \
                (end.st_dev, end.st_ino, end.st_size, end.st_mtime_ns, end.st_ctime_ns):
            raise OSError("original regular pathname replaced during read")
        return {"path": path, "inode": [st.st_dev, st.st_ino], "bytes": len(raw), "sha256": sha(raw), "nlink": st.st_nlink}, bytes(raw)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def write(fd, raw):
    old = os.get_blocking(fd)
    os.set_blocking(fd, False)
    view = memoryview(raw)
    try:
        while view:
            check("native bounded child write")
            try:
                count = os.write(fd, view[:65536])
            except BlockingIOError:
                time.sleep(0.002)
                continue
            if count <= 0:
                raise OSError("zero write")
            view = view[count:]
    finally:
        os.set_blocking(fd, old)


def create(path, raw):
    if len(raw) > 1 << 18:
        raise ValueError("bounded child evidence/barrier cap256KiB")
    parent = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NONBLOCK | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        created = inode(fd)
        write(fd, raw)
        os.fsync(fd)
        got = os.pread(fd, len(raw) + 1, 0)
        if got != raw or inode(fd) != created:
            raise OSError("child created-descriptor readback mismatch")
        facts = {"path": path, "inode": created, "sha256": sha(got), "bytes": len(got), "nlink": os.fstat(fd).st_nlink}
        os.close(fd)
        fd = None
        os.fsync(parent)
        return facts
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def authorize(mode, case):
    global LIFE, DEADLINE
    if mode not in ("wire", "mutation", "channel") or mode == "wire" and case not in WIRE or mode == "mutation" and case not in MUTATIONS or mode == "channel" and case not in EXTRA:
        raise ValueError("fixed child mode/case whitelist")
    trusted = os.environ.get("RQLS_MATRIX_APPROVAL_SHA256", "")
    if len(trusted) != 64 or any(x not in "0123456789abcdef" for x in trusted):
        raise ValueError("external child invocation SHA absent")
    run = ROOT + "/" + case
    af, ar = regular(run + "/parent-authorization.json")
    rf, rr = regular(run + "/request.json")
    approval, request = decode(ar), decode(rr)
    if af["sha256"] != trusted or approval.get("kind") != "rqls10-guard-matrix-invocation-v1" or \
            request.get("kind") != "rqls10-guard-matrix-request-v1" or approval.get("request_sha256") != rf["sha256"] or \
            request.get("case") != case or request.get("hook_set") != [case] or request.get("scope") != "MODIFIED_QUALIFICATION_FIXTURE":
        raise ValueError("child parent/request binding")
    if set(approval) != set(request) | {"request_sha256", "request_created"}:
        raise ValueError("child authority exact top-level schema")
    for key in set(request) - {"kind"}:
        if not typed_equal(request[key], approval[key]):
            raise ValueError("child authority field mismatch")
    original_created(approval["request_created"], rf)
    if af["nlink"] != 1:
        raise ValueError("single-link original approval")
    if request["negative_control"] is not (case != "io_channel_ordinary"):
        raise ValueError("child literal negative scope")
    expected_limits = {"max_wall_s": 300, "rss_bytes": 256 << 20, "output_bytes": 16 << 20, "busy_ceiling": 2, "max_loops": 2}
    if not typed_equal(request["limits"], expected_limits):
        raise ValueError("child resource envelope")
    life = request["parameters"]["child_life_s"]
    if isinstance(life, bool) or not isinstance(life, (int, float)) or not math.isfinite(life) or not 1 <= life <= 60:
        raise ValueError("child finite owned life")
    expiry = request["not_after_epoch"]
    if isinstance(expiry, bool) or not isinstance(expiry, (int, float)) or not math.isfinite(expiry) or expiry <= time.time():
        raise ValueError("child expired authority")
    LIFE = min(ENTRY + life, ENTRY + expiry - time.time())
    DEADLINE = LIFE - 0.25
    for role, pin in request["sources"].items():
        if set(pin) != {"path", "sha256"} or not pin["path"].startswith(LANE + "/"):
            raise ValueError("child source binding schema")
        facts, raw = regular(pin["path"], 2 << 20)
        if facts["sha256"] != pin["sha256"]:
            raise ValueError("child actual source pin")
    if request["sources"]["child"]["path"] != SELF or request["sources"]["base_child"] != {"path": BASE, "sha256": BASE_SHA} or \
            request["sources"]["supervisor"]["sha256"] != SUP_SHA:
        raise ValueError("child immutable source/overlay provenance")
    for role, path in (("run", run), ("out", run + "/out")):
        fd = directory(path)
        try:
            if not typed_equal(request["anchors"][role], {"path": path, "inode": inode(fd)}):
                raise ValueError("child original anchor identity")
        finally:
            os.close(fd)
    for role in ("config", "stability", "go_original"):
        binding = request[role]
        facts, raw = regular(binding["path"])
        if facts["sha256"] != binding["sha256"] or binding["path"] != run + "/" + {"config": "config.json", "stability": "stability.json", "go_original": "GO.original.json"}[role]:
            raise ValueError("child immutable approved input changed")
        original_created(request["created_facts"][role], facts)
    if mode in ("mutation", "channel"):
        binding = request["preparation"]
        facts, raw = regular(run + "/preparation.json")
        if not typed_equal(binding, {"path": facts["path"], "sha256": facts["sha256"]}):
            raise ValueError("child preparation pin")
        original_created(request["created_facts"]["preparation"], facts)
        prep = decode(raw)
        expected_pins = {"supervisor": {"path": LANE + "/code/owned_supervisor_v19.py", "sha256": SUP_SHA},
                         "child": {"path": BASE, "sha256": BASE_SHA}}
        for role, name in (("writer", "guard_qual_configs_v12.py"), ("checker", "guard_qual_check_v11.py")):
            path = LANE + "/code/" + name
            expected_pins[role] = {"path": path, "sha256": regular(path, 2 << 20)[0]["sha256"]}
        if not typed_equal(prep.get("source_pins"), expected_pins) or not typed_equal(prep.get("allocation"), request["allocation"]):
            raise ValueError("child preparation actual original source/allocation")
        for pin in expected_pins.values():
            if regular(pin["path"], 2 << 20)[0]["sha256"] != pin["sha256"]:
                raise ValueError("child original method source set changed")
        if regular(prep["python"]["path"], 64 << 20)[0]["sha256"] != prep["python"]["sha256"]:
            raise ValueError("child actual Python interpreter bytes")
    event("authority_checked", approval_sha256=trusted, request_sha256=rf["sha256"], sources=request["sources"],
          original_run=request["anchors"]["run"], original_output=request["anchors"]["out"],
          deadline_mono=DEADLINE, life_deadline_mono=LIFE)
    return run, request, trusted


class OriginalOS:
    def __init__(self):
        self.target_fds = set()
    def __getattr__(self, name):
        return getattr(os, name)
    def open(self, path, flags, mode=0o777, *, dir_fd=None):
        before = time.monotonic()
        fd = os.open(path, flags, mode, dir_fd=dir_fd)
        if path in ("pinned-scratch.txt", "launch.json") and flags & os.O_RDWR:
            self.target_fds.add(fd)
            try:
                observed = inode(fd)
            except OSError as exc:
                observed = {"error": err(exc)}
            event("original_target_open", fd=fd, basename=path, flags=flags, inode=observed,
                  mono_before=before, mono_after=time.monotonic())
        return fd
    def write(self, fd, data):
        before = time.monotonic()
        try:
            result = os.write(fd, data)
        except BaseException as exc:
            if fd in self.target_fds:
                event("original_target_write_error", fd=fd, error=err(exc), mono_before=before, mono_after=time.monotonic())
            raise
        if fd in self.target_fds:
            event("original_target_write_return", fd=fd, bytes=len(data), result=result,
                  data_sha256=sha(data), mono_before=before, mono_after=time.monotonic())
        return result
    def close(self, fd):
        try:
            return os.close(fd)
        finally:
            self.target_fds.discard(fd)


def original_child():
    raw = regular(BASE, 2 << 20)[1]
    if sha(raw) != BASE_SHA:
        raise ValueError("immutable base changed before load")
    tree = ast.parse(raw, filename=BASE)
    terminal = tree.body[-1]
    if not isinstance(terminal, ast.If) or not isinstance(terminal.test, ast.Compare) or \
            not isinstance(terminal.test.left, ast.Name) or terminal.test.left.id != "__name__" or \
            len(terminal.test.comparators) != 1 or not isinstance(terminal.test.comparators[0], ast.Constant) or terminal.test.comparators[0].value != "__main__":
        raise ValueError("fixed pinned original child12 terminal guard")
    namespace = {"__file__": BASE, "__name__": "__matrix_original_child12__"}
    exec(compile(ast.Module(body=tree.body[:-1], type_ignores=[]), BASE, "exec"), namespace)
    namespace["os"] = OriginalOS()
    event("original_child_loaded", source_sha256=BASE_SHA, original_methods=["wait_go", "mutate_original"],
          scope_label="MODIFIED_QUALIFICATION_FIXTURE; original module sans terminal, native observation proxy only")
    return namespace


def ordinary_extra_probe(original):
    # Controlled native pipe, original parser, no strengthened toy parser.
    saved, rd, wr = None, None, None
    try:
        saved = os.dup(0)
        rd, wr = os.pipe()
        write(wr, b"GO\nEXTRA\n")
        os.close(wr)
        wr = None
        os.dup2(rd, 0)
        os.close(rd)
        rd = None
        value = {"input_utf8_hex": b"GO\nEXTRA\n".hex(), "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE",
                 "source_sha256": BASE_SHA, "source_method": "wait_go", "exception": None, "return": None}
        try:
            value["return"] = original["wait_go"]("ok", DEADLINE)
        except BaseException as exc:
            value["exception"] = err(exc)
        return value
    finally:
        if saved is not None:
            os.dup2(saved, 0)
            os.close(saved)
        if rd is not None:
            os.close(rd)
        if wr is not None:
            os.close(wr)


def wait_open_barrier(run, case, manifest_sha):
    expected = {"kind": "rqls10-fixture-open-barrier-v1", "case": case, "child_pid": os.getpid(), "manifest_sha256": manifest_sha}
    while True:
        check("bounded fixture open barrier")  # Raises at the life deadline or after a handled TERM.
        try:
            facts, raw = regular(run + "/child-open-release.json")
            value = decode(raw)
        except (OSError, ValueError):
            time.sleep(0.002)  # Absent or still being exclusively written: bounded retry.
            continue
        if value != expected:
            raise ValueError("open barrier is not exact fixture coordination")
        event("native_open_barrier_observed", artifact=facts, authority="NOT_GO_NOT_ADMISSION_NOT_RELEASE")
        return


def main(mode, case):
    global REPORTING
    run, request, trusted = authorize(mode, case)
    original = original_child()
    scenario = ("mutate_pin" if "_pin_" in case else "mutate_evidence") if mode in ("mutation", "channel") else "ok"
    report = {"kind": "rqls10-matrix-io-child-outcome-v1", "case": case, "mode": mode,
              "scope": "MODIFIED_QUALIFICATION_FIXTURE", "approval_sha256": trusted,
              "owner": {"pid": os.getpid(), "pgid": os.getpgrp(), "mono_entry": ENTRY},
              "base_source_sha256": BASE_SHA, "base_pin_fixture_sha256": sha(original["FIXTURE"]), "protocol": None, "manifest": None,
              "method_return": None, "method_exception": None, "ordinary_extra_probe": None,
              "observations": EVENTS, "unresolved": [], "selected_status_not_actual_exit": None}
    status = 0
    rfd, ofd = None, None
    try:
        protocol, manifest = original["wait_go"](scenario, DEADLINE)
        report["protocol"], report["manifest"] = protocol, manifest
        event("actual_source_go_parser_return", protocol=protocol, manifest=manifest)
        if mode == "wire":
            if case == "io_channel_ordinary":
                report["ordinary_extra_probe"] = ordinary_extra_probe(original)
        elif mode == "mutation":
            if case.endswith("before_child_open"):
                ready = create(run + "/child-ready.json", packed({"kind": "rqls10-matrix-child-open-ready-v1",
                               "case": case, "pid": os.getpid(), "pgid": os.getpgrp(), "mono": time.monotonic(),
                               "manifest_sha256": protocol["creation_manifest_sha256"]}))
                event("native_manifest_received_before_target_open", artifact=ready, manifest_sha256=protocol["creation_manifest_sha256"])
                wait_open_barrier(run, case, protocol["creation_manifest_sha256"])
            rfd = original["directory"](run, DEADLINE)
            ofd = os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=rfd)
            report["method_return"] = original["mutate_original"](scenario, run, rfd, ofd, manifest, protocol, DEADLINE)
    except BaseException as exc:
        report["method_exception"] = err(exc)
        status = 3 if report["protocol"] is not None else 6
        event("original_child_method_exception", error=err(exc), selected_status_not_actual_exit=status)
    finally:
        if ofd is not None:
            os.close(ofd)
        if rfd is not None:
            os.close(rfd)
    report["owner"]["mono_end"] = time.monotonic()
    report["selected_status_not_actual_exit"] = status
    report["observed_maxrss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Reserve evidence time inside the earlier absolute module-entry life.
    REPORTING = True  # Only bounded close/evidence work remains after a handled TERM.
    if time.monotonic() >= LIFE - 0.05:
        return 2  # No evidence time remains inside the absolute module-entry life; nothing further is written.
    if TRUNCATED[0]:
        report["unresolved"].append({"kind": "event_trace_truncated", "dropped_events": TRUNCATED[0]})
    create(run + "/out/child-result.json", packed(report))
    write(1, packed({"kind": "rqls10-matrix-io-child-record-v1", "case": case,
                     "selected_status_not_actual_exit": status, "report_sha256": sha(packed(report))}))
    return status


def term(signum, frame):
    global CANCELLED
    CANCELLED = True


if __name__ == "__main__":
    # First native PID/PGID framing record, before request/source/test work.
    owner = {"kind": "rqls10-matrix-child-owner-v1", "pid": os.getpid(), "pgid": os.getpgrp(),
             "mono_begin": ENTRY, "scope": "NATIVE_OWNER_RECORD"}
    write(1, packed(owner))
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)
    signal.signal(signal.SIGHUP, term)
    try:
        if len(sys.argv) != 3:
            raise ValueError("fixed wire|mutation|channel CASE arguments required")
        sys.exit(main(sys.argv[1], sys.argv[2]))
    except SystemExit:
        raise
    except BaseException as exc:
        try:
            write(2, packed({"kind": "rqls10-matrix-child-refusal-v1", "error": err(exc)}))
        except BaseException:
            pass
        sys.exit(2)
