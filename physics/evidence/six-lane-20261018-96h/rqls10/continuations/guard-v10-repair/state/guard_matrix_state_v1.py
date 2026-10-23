#!/usr/bin/env python3
"""Fixed STATE_ONLY matrix; WRITTEN_ONLY, no invocation or release authority.

CLI: guard_matrix_state_v2.py CASE_ID PARENT_APPROVAL_SHA256
All source methods run from the SHA-pinned original AST, never a source import.
The namespace is MODIFIED_QUALIFICATION_FIXTURE: os/time/signal/LP/LC/sys/threading
are closed MODEL backends. No model PID/FD ever reaches a native process API.
Native operations outside that namespace only read approved files, identify this
owner, measure its resource/runtime budget, and publish one exclusive outcome.
Human synthetic clock/error text is exported only as explicitly labelled UTF8_HEX.
The separately captured actual exit belongs to the parent, not to this report.
"""
import ast
import builtins
import contextlib
import ctypes
import datetime
import errno
import hashlib
import json
import math
import os
import re
import resource
import signal
import stat
import struct
import sys
import time
from types import SimpleNamespace

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
# Successor install paths (parent-pinned at integration; originals stay frozen at their v1 paths).
DRIVER = LANE + "/code/guard_matrix_state_v2.py"
ORACLE = LANE + "/code/guard_matrix_state_check_v2.py"
SPECS = LANE + "/review/rqls10-matrix-state-v2-cases.json"
# Review candidate only; source readiness is not runtime, qualification or release authority.
SUPERVISOR = LANE + "/code/owned_supervisor_v19.py"
SUPERVISOR_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
SCOPE = "STATE_ONLY"
HOOK_SET = "rqls10-state-model-v1"
MAX_BYTES = 16 << 20
RSS_LIMIT = 256 << 20
MAX_RUNTIME = 300.0
MODEL_PID = 700000001
MODEL_MAIN = 700000010
MODEL_UID = 501
EPOCH = 1700000000.0
MONO = 1000.0
CASES = (
    "st_runtime_999", "st_runtime_1000", "st_runtime_1026",
    "st_go_w10_lt", "st_go_w10_eq", "st_go_w10_gt",
    "st_go_w200_lt", "st_go_w200_eq", "st_go_w200_gt",
    "st_age_lt", "st_age_eq", "st_age_gt", "st_date_missing",
    "st_date_malformed", "st_date_naive", "st_date_future",
    "st_stability_rollback", "st_stability_refresh", "st_stability_tighten",
    "st_ack_age_lt", "st_ack_age_eq", "st_ack_age_gt",
    "st_retry_unproved", "st_retry_busy", "st_retry_rss",
    "st_abort_identity", "st_abort_resource",
    "st_cap_bytes_lt", "st_cap_bytes_eq", "st_cap_bytes_gt",
    "st_cap_identity_lt", "st_cap_identity_eq", "st_cap_identity_gt",
    "st_cap_unproved_lt", "st_cap_unproved_eq", "st_cap_unproved_gt",
    "st_cap_coverage_lt", "st_cap_coverage_eq", "st_cap_coverage_gt",
    "st_cap_attempt_lt", "st_cap_attempt_eq", "st_cap_attempt_gt",
    "st_cap_census_lt", "st_cap_census_eq", "st_cap_census_gt",
    "st_cap_variants_lt", "st_cap_variants_eq", "st_cap_variants_gt",
    "st_cap_final_rss", "st_cap_initial_main", "st_cap_helper_term",
    "st_budget_output_lt", "st_budget_output_eq", "st_budget_output_gt",
    "st_budget_reservation_lt", "st_budget_reservation_eq", "st_budget_reservation_gt",
    "st_budget_free_lt", "st_budget_free_eq", "st_budget_free_gt",
    "st_budget_lane_lt", "st_budget_lane_eq", "st_budget_lane_gt",
    "st_cutoff_census_lt", "st_cutoff_census_eq", "st_cutoff_census_gt",
    "st_cutoff_helper_lt", "st_cutoff_helper_eq", "st_cutoff_helper_gt",
    "st_cutoff_stop_grace_lt", "st_cutoff_stop_grace_eq", "st_cutoff_stop_grace_gt",
    "st_cutoff_exit_grace_lt", "st_cutoff_exit_grace_eq", "st_cutoff_exit_grace_gt",
    "st_cutoff_finalize_lt", "st_cutoff_finalize_eq", "st_cutoff_finalize_gt",
    "st_write_short", "st_write_zero", "st_write_late",
    "st_manifest_4095", "st_manifest_4096", "st_manifest_4097",
    "st_cancel_pending_after_handled",
    "st_complete_go_auth_lt", "st_complete_go_auth_eq", "st_complete_go_auth_gt",
    "st_complete_go_fit_lt", "st_complete_go_fit_eq", "st_complete_go_fit_gt",
    "st_complete_go_stability_lt", "st_complete_go_stability_eq", "st_complete_go_stability_gt",
    "st_complete_ack_auth_lt", "st_complete_ack_auth_eq", "st_complete_ack_auth_gt",
    "st_complete_ack_fit_lt", "st_complete_ack_fit_eq", "st_complete_ack_fit_gt",
    "st_complete_ack_stability_lt", "st_complete_ack_stability_eq", "st_complete_ack_stability_gt",
    "st_ident_signal_uniqueid", "st_ident_signal_euid", "st_ident_signal_ruid", "st_ident_signal_idversion",
    "st_ident_signal_ppid", "st_ident_signal_pgid", "st_ident_signal_traced",
    "st_ident_read_uniqueid", "st_ident_read_euid", "st_ident_read_ruid", "st_ident_read_idversion",
    "st_ident_read_ppid", "st_ident_read_pgid", "st_ident_read_traced",
    "st_ident_bracket_changed", "st_ident_mixed_uid_unreadable", "st_ident_main_initial_invalid", "st_ident_helper_signal_changed",
    "st_clock_cancel_before_target", "st_clock_cancel_after_target",
    "st_clock_reap_before_wait", "st_clock_reap_before_wait_prior_stop",
    "st_clock_reap_after_wait", "st_clock_reap_after_wait_prior_stop", "st_clock_recovery_post_wait",
    "st_acq_main_identity_end_clock", "st_acq_task_end_clock_rss", "st_acq_final_bracket_end_clock_rss",
    "st_acq_accounting_late_return", "st_acq_accounting_observed_clock", "st_acq_reap_mono_clock",
    "st_write_progress_late", "st_cap_raw_lt", "st_cap_raw_eq", "st_cap_raw_gt",
    "st_cap_clockless_lt", "st_cap_clockless_eq", "st_cap_clockless_gt",
)


class Invalid(Exception):
    pass


class ModelBoundary(Exception):
    pass


class ModelClockUnavailable(Exception):
    """Declared API-response injection, never a native clock failure observation."""
    pass


class CalibrationStop(BaseException):
    pass


class BudgetStop(BaseException):
    pass


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise Invalid("duplicate JSON key")
        out[key] = value
    return out


def decode(raw):
    def floating(text):
        value = float(text)
        if not math.isfinite(value):
            raise Invalid("nonfinite number")
        return value
    def constant(text):
        raise Invalid("nonfinite constant")
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                      parse_float=floating, parse_constant=constant)


def integer(value, minimum=0):
    return type(value) is int and value >= minimum


def finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def hex64(value):
    return type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def same(left, right):
    return canonical(left) == canonical(right)


def directory(path):
    if not path.startswith("/") or os.path.normpath(path) != path:
        raise Invalid("noncanonical directory")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.lstrip("/").split("/"):
            if part in ("", ".", ".."):
                raise Invalid("directory component")
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


class NativeBudget:
    def __init__(self, begin):
        self.begin = begin
        self.max_rss = 0
        self.checks = 0

    def check(self):
        now = time.monotonic()
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Darwin ru_maxrss is bytes. This fixture refuses other platforms.
        self.max_rss = max(self.max_rss, rss)
        self.checks += 1
        if now - self.begin > 280.0 or rss > RSS_LIMIT:
            raise BudgetStop("native cooperative budget exhausted")
        return now


def signature(s):
    return (s.st_dev, s.st_ino, s.st_mode, s.st_size, s.st_nlink, s.st_mtime_ns, s.st_ctime_ns)


def snapshot(fdroot, name, budget, cap=MAX_BYTES):
    budget.check()
    before = os.stat(name, dir_fd=fdroot, follow_symlinks=False)
    if not stat.S_ISREG(before.st_mode) or not 0 <= before.st_size <= cap or before.st_nlink != 1:
        raise Invalid("not a bounded one-link regular file")
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fdroot)
    try:
        if signature(os.fstat(fd)) != signature(before):
            raise Invalid("changed open")
        data = bytearray()
        while len(data) < before.st_size:
            budget.check()
            part = os.read(fd, min(65536, before.st_size - len(data)))
            if not part:
                raise Invalid("short read")
            data.extend(part)
        if os.read(fd, 1) or signature(os.fstat(fd)) != signature(before) or \
                signature(os.stat(name, dir_fd=fdroot, follow_symlinks=False)) != signature(before):
            raise Invalid("changed read")
    finally:
        os.close(fd)
    budget.check()
    raw = bytes(data)
    return {"raw": raw, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
            "inode": [before.st_dev, before.st_ino], "nlink": before.st_nlink,
            "mode": stat.S_IMODE(before.st_mode)}


def absolute_snapshot(path, budget):
    fd = directory(os.path.dirname(path))
    try:
        return snapshot(fd, os.path.basename(path), budget)
    finally:
        os.close(fd)


def facts(entry):
    return {k: entry[k] for k in ("sha256", "bytes", "inode", "nlink", "mode")}


def authority(case, digest, runfd, budget):
    approval = snapshot(runfd, "parent-authorization.json", budget, 1 << 20)
    request = snapshot(runfd, "request.json", budget, 1 << 20)
    if approval["sha256"] != digest:
        raise Invalid("external parent SHA mismatch")
    ap, rq = decode(approval["raw"]), decode(request["raw"])
    run = {"path": ROOT + "/" + case, "inode": [os.fstat(runfd).st_dev, os.fstat(runfd).st_ino]}
    request_keys = {"kind", "case", "scope", "run", "hook_set", "negative_control", "allocation",
                    "not_after_epoch", "model_inputs_sha256"}
    approval_keys = {"kind", "case", "scope", "request_sha256", "run", "sources", "hook_set",
                     "negative_control", "allocation", "not_after_epoch", "authority", "ownership_negative",
                     "mutation_negative", "native_config"}
    if type(rq) is not dict or set(rq) != request_keys or type(ap) is not dict or set(ap) != approval_keys:
        raise Invalid("authority exact schema")
    if rq["kind"] != "rqls10-guard-matrix-request-v1" or ap["kind"] != "rqls10-guard-matrix-invocation-v1":
        raise Invalid("authority kind")
    negative = {"kind": "MODEL_STATE", "case": case, "native_process": False, "native_mutation": False}
    for item in (rq, ap):
        if item["case"] != case or item["scope"] != SCOPE or not same(item["run"], run) or \
                item["hook_set"] != HOOK_SET or not same(item["negative_control"], negative):
            raise Invalid("case/scope/current inode/negative bindings")
    if ap["request_sha256"] != request["sha256"] or ap["authority"] != "PARENT_INDIVIDUAL_INVOCATION_NO_RELEASE" or \
            ap["ownership_negative"] is not False or ap["mutation_negative"] is not False or ap["native_config"] is not None:
        raise Invalid("state authority cannot imply native GO or mutation")
    allocation = rq["allocation"]
    expected_keys = {"bytes", "cpu_slots", "max_wall_s", "rss_bytes", "output_bytes", "busy_limit",
                     "no_three_loops", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"}
    if type(allocation) is not dict or set(allocation) != expected_keys or not same(ap["allocation"], allocation) or \
            allocation["cpu_slots"] != 1 or type(allocation["cpu_slots"]) is not int or \
            allocation["bytes"] != MAX_BYTES or type(allocation["bytes"]) is not int or \
            allocation["max_wall_s"] != MAX_RUNTIME or type(allocation["max_wall_s"]) is not float or \
            allocation["rss_bytes"] != RSS_LIMIT or type(allocation["rss_bytes"]) is not int or \
            allocation["output_bytes"] != MAX_BYTES or type(allocation["output_bytes"]) is not int or \
            allocation["busy_limit"] != 2 or type(allocation["busy_limit"]) is not int or \
            allocation["no_three_loops"] is not True or any(not integer(allocation[k]) for k in
                ("outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")):
        raise Invalid("bounded parent allocation")
    now = time.time()  # Native raw epoch telemetry for authority only, never a human timestamp.
    if not finite(rq["not_after_epoch"]) or not same(rq["not_after_epoch"], ap["not_after_epoch"]) or \
            not now <= rq["not_after_epoch"] <= now + MAX_RUNTIME:
        raise Invalid("expired/unbounded authority")
    paths = {"supervisor": SUPERVISOR, "driver": DRIVER, "oracle": ORACLE, "case_specs": SPECS}
    if type(ap["sources"]) is not dict or set(ap["sources"]) != set(paths):
        raise Invalid("source keys")
    sources = {}
    for key, path in paths.items():
        pin = ap["sources"][key]
        if type(pin) is not dict or set(pin) != {"path", "sha256"} or pin["path"] != path or not hex64(pin["sha256"]):
            raise Invalid("source pin schema")
        actual = absolute_snapshot(path, budget)
        if actual["sha256"] != pin["sha256"] or actual["mode"] != 0o444:
            raise Invalid("source not exact frozen bytes")
        sources[key] = actual
    if sources["supervisor"]["sha256"] != SUPERVISOR_SHA:
        raise Invalid("original source SHA")
    spec = decode(sources["case_specs"]["raw"])
    if spec.get("kind") != "rqls10-matrix-state-v1-cases" or set(spec.get("cases", {})) != set(CASES) or \
            spec.get("supervisor") != {"path": SUPERVISOR, "sha256": SUPERVISOR_SHA} or \
            rq["model_inputs_sha256"] != hashlib.sha256(canonical(spec["cases"][case])).hexdigest():
        raise Invalid("fixed case inputs/spec/source pin mismatch")
    return ap, rq, sources, approval, request, spec["cases"][case], now


def utf8_hex(text):
    raw = text.encode("utf-8", "surrogatepass")
    return {"encoding": "UTF8_HEX", "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "hex": raw.hex(),
            "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def safe(value):
    if isinstance(value, str):
        if re.search(r"\d{4}-\d\d-\d\d[T ]\d\d:", value):
            return utf8_hex(value)
        return value
    if isinstance(value, bytes):
        return {"encoding": "BYTES_HEX", "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "hex": value.hex(),
                "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}
    if isinstance(value, dict):
        return {str(k): utf8_hex(v) if isinstance(v, str) and
                (str(k) in ("error", "detail", "reason") or str(k).endswith("_error")) else safe(v)
                for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [safe(x) for x in value]
    if isinstance(value, signal.Signals):
        return int(value)
    if value is None or type(value) in (bool, int, float):
        return value
    return {"model_type": type(value).__name__}


def source_frames():
    frame = sys._getframe(1)
    result = []
    while frame is not None:
        if frame.f_code.co_filename == SUPERVISOR:
            result.append((frame.f_code.co_name, frame.f_lineno, frame))
        frame = frame.f_back
    return result


class ModelClock:
    def __init__(self, model):
        self.model = model
        self.mono = MONO
        self.epoch_origin = EPOCH
        self.civil_shift = 0.0
        self.rules = []

    def snapshot_epoch(self):
        """UNHOOKED MODEL civil value for replacement dependency responses; never an original clock call."""
        return self.epoch_origin + self.mono - MONO + self.civil_shift

    def reading(self, clock):
        self.model.guard()
        stack = source_frames()
        self.model.checkpoint(stack)
        value = self.mono if clock == "monotonic" else self.epoch_origin + self.mono - MONO + self.civil_shift
        for rule in self.rules:
            if rule["fired"] or rule["clock"] != clock or not self.model.matches(stack, rule):
                continue
            rule["seen"] += 1
            if rule["seen"] != rule["occurrence"]:
                continue
            rule["fired"] = True
            rule["mono_before"] = self.mono
            if rule["action"] == "set":
                self.mono = rule["set_to"]
                value = self.mono if clock == "monotonic" else self.epoch_origin + self.mono - MONO + self.civil_shift
            elif rule["action"] == "epoch":
                value = rule["set_to"]
                self.civil_shift = value - (self.epoch_origin + self.mono - MONO)
            elif rule["action"] == "raise":
                rule["returned"], rule["exception_type"] = None, "ModelClockUnavailable"
                self.model.record("clock_rule", dict(rule, response_scope="API_RESPONSE_INJECTION"))
                raise ModelClockUnavailable("MODEL declared clock response unavailable")
            rule["returned"], rule["exception_type"] = value, None
            self.model.record("clock_rule", dict(rule, response_scope="API_RESPONSE_INJECTION"))
        return value

    def monotonic(self):
        return self.reading("monotonic")

    def time(self):
        return self.reading("time")

    def sleep(self, seconds):
        self.model.guard()
        if not finite(seconds) or not 0 <= seconds <= 600:
            self.model.bad("unbounded model sleep")
        # Zero sleep advances one model scheduling quantum; never a native sleep.
        self.mono += max(seconds, 0.000001)
        self.model.record("sleep", {"requested_s": seconds, "model_quantum_s": max(seconds, 0.000001)})


class ModelSignals:
    def __init__(self, model):
        self.model = model
        self.pending = set()
        self.mask = set()
        for key in ("SIGTERM", "SIGINT", "SIGHUP", "SIGPIPE", "SIGCHLD", "SIG_BLOCK", "SIG_SETMASK", "SIG_UNBLOCK"):
            setattr(self, key, getattr(signal, key))

    def sigpending(self):
        self.model.guard()
        self.model.record("sigpending", {"signals": sorted(self.pending)})
        return set(self.pending)

    def pthread_sigmask(self, how, values):
        self.model.guard()
        old = set(self.mask)
        if how == self.SIG_BLOCK:
            self.mask |= set(values)
        elif how == self.SIG_SETMASK:
            self.mask = set(values)
        elif how == self.SIG_UNBLOCK:
            self.mask -= set(values)
        else:
            self.model.bad("signal mask operation")
        self.model.record("sigmask", {"how": int(how), "signals": sorted(values)})
        return old


class ModelJSON:
    """Pure serialization passthrough plus declared read-only source-state checkpoint."""
    def __init__(self, model):
        self.model = model

    def dumps(self, value, *args, **kwargs):
        self.model.guard()
        self.model.checkpoint(source_frames())
        return json.dumps(value, *args, **kwargs)

    @staticmethod
    def loads(value, *args, **kwargs):
        return json.loads(value, *args, **kwargs)


class ModelStream:
    def __init__(self, model, name):
        self.model, self.name = model, name
        self.buffer = ""

    def write(self, text):
        self.model.guard()
        if len(self.buffer.encode()) + len(text.encode()) > 4 << 20:
            self.model.bad("model stream bound")
        self.buffer += text
        self.model.record("stream_write", {"stream": self.name, "bytes": len(text.encode()),
                                           "sha256": hashlib.sha256(text.encode()).hexdigest()})
        return len(text)

    def flush(self):
        self.model.guard()
        self.model.record("stream_flush", {"stream": self.name})


class ModelNode:
    def __init__(self, inode, directory=False, data=b"", logical_size=None):
        self.inode, self.directory = inode, directory
        self.data = bytearray(data)
        self.logical_size = logical_size
        self.nlink = 1
        self.changed = 1

    @property
    def size(self):
        return len(self.data) if self.logical_size is None else self.logical_size


class ModelOS:
    """Only explicit model primitives. There is deliberately no generic native fallback."""
    path = SimpleNamespace(abspath=os.path.abspath, normpath=os.path.normpath, dirname=os.path.dirname,
                           basename=os.path.basename, relpath=os.path.relpath)
    WNOHANG = os.WNOHANG
    for _key in ("O_RDONLY", "O_WRONLY", "O_RDWR", "O_CREAT", "O_EXCL", "O_NOFOLLOW", "O_NONBLOCK",
                 "O_DIRECTORY", "POSIX_SPAWN_DUP2", "POSIX_SPAWN_CLOSE"):
        locals()[_key] = getattr(os, _key)

    def __init__(self, model):
        self.model = model
        self.nodes = {}
        self.fds = {}
        self.nextfd = 10
        self.nextino = 100
        self.free_value = 13000000000
        self.write_mode = None
        self.write_count = 0
        self.ensure_dir("/")

    def getpid(self):
        return MODEL_PID

    def getuid(self):
        return MODEL_UID

    def ensure_dir(self, path):
        path = os.path.normpath(path)
        if path not in self.nodes:
            if path != "/":
                self.ensure_dir(os.path.dirname(path))
            self.nodes[path] = ModelNode(self.nextino, True)
            self.nextino += 1
        return self.nodes[path]

    def put(self, path, data=b"", logical_size=None):
        self.ensure_dir(os.path.dirname(path))
        node = ModelNode(self.nextino, False, data, logical_size)
        self.nextino += 1
        self.nodes[path] = node
        return node

    def resolve(self, path, dir_fd=None):
        if os.path.isabs(path):
            return os.path.normpath(path)
        if dir_fd not in self.fds or self.fds[dir_fd]["kind"] != "file":
            self.model.bad("model relative fd")
        return os.path.normpath(self.fds[dir_fd]["path"] + "/" + path)

    def status(self, node):
        return SimpleNamespace(st_dev=771, st_ino=node.inode, st_size=node.size,
                               st_mode=(stat.S_IFDIR | 0o755) if node.directory else (stat.S_IFREG | 0o644),
                               st_nlink=node.nlink, st_mtime_ns=node.changed, st_ctime_ns=node.changed,
                               st_birthtime=EPOCH - 1000)

    def stat(self, path, dir_fd=None, follow_symlinks=False):
        self.model.guard()
        resolved = self.resolve(path, dir_fd)
        if resolved not in self.nodes:
            raise FileNotFoundError(errno.ENOENT, "MODEL absent file")
        return self.status(self.nodes[resolved])

    def fstat(self, fd):
        self.model.guard()
        item = self.fds.get(fd)
        if item is None or item["kind"] != "file":
            self.model.bad("model fstat descriptor")
        return self.status(item["node"])

    def open(self, path, flags, mode=0o644, dir_fd=None):
        self.model.guard()
        resolved = self.resolve(path, dir_fd)
        if resolved == "/dev/null":
            node = self.nodes.get(resolved) or self.put(resolved)
        elif flags & self.O_CREAT:
            if resolved in self.nodes and flags & self.O_EXCL:
                raise FileExistsError(errno.EEXIST, "MODEL exclusive collision")
            node = self.nodes.get(resolved) or self.put(resolved)
        elif resolved in self.nodes:
            node = self.nodes[resolved]
        else:
            raise FileNotFoundError(errno.ENOENT, "MODEL absent file")
        if flags & self.O_DIRECTORY and not node.directory:
            raise NotADirectoryError(errno.ENOTDIR, "MODEL not directory")
        fd = self.nextfd
        self.nextfd += 1
        self.fds[fd] = {"kind": "file", "path": resolved, "node": node, "offset": 0}
        self.model.record("open", {"fd": fd, "path": resolved, "inode": [771, node.inode], "flags": flags})
        return fd

    def close(self, fd):
        self.model.guard()
        if fd not in self.fds:
            raise OSError(errno.EBADF, "MODEL closed fd")
        item = self.fds.pop(fd)
        if item["kind"] == "pipe_write":
            item["pipe"]["eof"] = not any(p.get("pipe") is item["pipe"] and p.get("hold") and not p.get("term")
                                          for p in self.model.procs.values())
        self.model.record("close", {"fd": fd})

    def pipe(self):
        self.model.guard()
        pipe = {"data": bytearray(), "eof": False}
        left, right = self.nextfd, self.nextfd + 1
        self.nextfd += 2
        self.fds[left] = {"kind": "pipe_read", "pipe": pipe, "offset": 0}
        self.fds[right] = {"kind": "pipe_write", "pipe": pipe, "offset": 0}
        self.model.record("pipe", {"read_fd": left, "write_fd": right})
        return left, right

    def read(self, fd, count):
        self.model.guard()
        item = self.fds[fd]
        if item["kind"] == "pipe_read":
            pipe = item["pipe"]
            data = bytes(pipe["data"][item["offset"]:item["offset"] + count])
            if not data and not pipe["eof"]:
                raise BlockingIOError(errno.EAGAIN, "MODEL pipe alive")
        elif item["kind"] == "file":
            if item["node"].logical_size is not None:
                self.model.bad("virtual accounting-only file read")
            data = bytes(item["node"].data[item["offset"]:item["offset"] + count])
        else:
            self.model.bad("model read direction")
        item["offset"] += len(data)
        self.model.record("read", {"fd": fd, "requested": count, "returned": len(data),
                                    "sha256": hashlib.sha256(data).hexdigest()})
        return data

    def write(self, fd, data):
        self.model.guard()
        self.write_count += 1
        raw = bytes(data)
        count = min(2, len(raw)) if self.write_mode == "short" else 0 if self.write_mode == "zero" else len(raw)
        part = raw[:count]
        item = self.fds[fd]
        if item["kind"] == "pipe_write":
            item["pipe"]["data"].extend(part)
        elif item["kind"] == "file":
            start = item["offset"]
            item["node"].data[start:start + count] = part
            item["node"].changed += 1
            item["offset"] += count
        else:
            self.model.bad("model write direction")
        before = self.model.clock.mono
        if self.write_mode == "late":
            self.model.clock.mono = self.model.write_cutoff + 0.01
        self.model.record("write", {"fd": fd, "requested": len(raw), "returned": count,
                                     "mono_before": before, "mono_after": self.model.clock.mono,
                                     "sha256": hashlib.sha256(part).hexdigest(), "response_scope": "API_RESPONSE_INJECTION"})
        return count

    def fsync(self, fd):
        self.model.guard()
        if fd not in self.fds:
            self.model.bad("model fsync closed fd")
        self.model.record("fsync", {"fd": fd})

    def set_blocking(self, fd, value):
        self.model.guard()
        if fd not in self.fds:
            self.model.bad("model set_blocking fd")
        self.model.record("set_blocking", {"fd": fd, "value": value})

    def fstatvfs(self, fd):
        self.model.guard()
        return SimpleNamespace(f_bavail=self.free_value, f_frsize=1)

    def scandir(self, fd):
        self.model.guard()
        path = self.fds[fd]["path"]
        names = sorted({p[len(path.rstrip("/")) + 1:].split("/", 1)[0] for p in self.nodes
                        if p.startswith(path.rstrip("/") + "/") and p != path})
        @contextlib.contextmanager
        def listing():
            yield iter([SimpleNamespace(name=name) for name in names])
        return listing()

    def link(self, source, target, src_dir_fd=None, dst_dir_fd=None):
        self.model.guard()
        left, right = self.resolve(source, src_dir_fd), self.resolve(target, dst_dir_fd)
        if right in self.nodes:
            raise FileExistsError(errno.EEXIST, "MODEL link collision")
        self.nodes[right] = self.nodes[left]
        self.nodes[right].nlink += 1
        self.model.record("link", {"source": left, "target": right, "inode": [771, self.nodes[right].inode]})

    def posix_spawn(self, path, argv, env, file_actions, setsid, setsigmask, setsigdef):
        self.model.guard()
        if not setsid or setsigmask != ():
            self.model.bad("model spawn mask/session")
        helper = path == "/bin/date"
        if not helper and argv != self.model.cfg["argv"]:
            self.model.bad("model arbitrary command")
        pid = self.model.next_helper if helper else MODEL_MAIN
        p = self.model.process(pid)
        p["helper"] = helper
        p["hold"] = self.model.helper_holds if helper else True
        p.update(self.model.spawn_overrides.get("helper" if helper else "child", {}))
        pipes, text = [], None
        if helper:
            # Replacement /bin/date bytes use an UNHOOKED model-clock snapshot; no supervisor clock hook can fire here.
            text = datetime.datetime.fromtimestamp(math.floor(self.model.clock.snapshot_epoch()), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z").encode("ascii") + b"\n"
            for action in file_actions:
                if action[0] == self.POSIX_SPAWN_DUP2 and action[2] == 1:
                    item = self.fds.get(action[1])
                    if item is None or item["kind"] != "pipe_write":
                        self.model.bad("model helper stdout action")
                    pipes.append(item["pipe"])
        self.model.record("posix_spawn", {"pid": pid, "pgid": pid, "argv": argv, "setsid": setsid,
                                           "setsigmask": list(setsigmask), "helper": helper,
                                           "scope": "MODEL_PROCESS_NOT_NATIVE"})
        # Every fallible response is constructed: commit the process side effect, then return its PID (no later raise).
        if helper:
            self.model.next_helper += 1
        self.model.procs[pid] = p
        for pipe in pipes:
            pipe["data"].extend(text)
            pipe["eof"] = not self.model.helper_holds
            p["pipe"] = pipe
        return pid

    WIFEXITED = staticmethod(os.WIFEXITED)
    WIFSIGNALED = staticmethod(os.WIFSIGNALED)

    def waitpid(self, pid, flags):
        self.model.guard()
        if flags != self.WNOHANG:
            self.model.bad("non-WNOHANG model wait")
        before = self.model.clock.mono
        if self.model.wait_return_mono is not None and pid == MODEL_MAIN:
            self.model.clock.mono = self.model.wait_return_mono
            result = (pid, 0)
            self.model.procs.pop(pid, None)
            self.model.wait_return_mono = None
        else:
            p = self.model.procs.get(pid)
            if p is None:
                raise ChildProcessError("MODEL wait ownership absent")
            if p.get("term"):
                result = (pid, int(signal.SIGTERM))
                self.model.procs.pop(pid)
                if p.get("pipe") is not None:
                    p["pipe"]["eof"] = True
            elif p.get("helper") and not p.get("hold"):
                result = (pid, 0)
                self.model.procs.pop(pid)
            else:
                result = (0, 0)
        self.model.record("waitpid", {"pid": pid, "flags": flags, "mono_before": before,
                                       "mono_after": self.model.clock.mono, "returned": list(result)})
        return result

    @staticmethod
    def waitstatus_to_exitcode(status):
        return os.waitstatus_to_exitcode(status)  # Pure status decoder, not a process operation.

    def killpg(self, pgid, sig):
        self.model.guard()
        if sig != signal.SIGTERM:
            self.model.bad("model escalation")
        matches = [p for p in self.model.procs.values() if p["pgid"] == pgid]
        if not matches:
            raise ProcessLookupError(errno.ESRCH, "MODEL group absent")
        for p in matches:
            p["term"] = True
        self.model.record("killpg", {"pgid": pgid, "signal": int(sig), "scope": "MODEL_SIGNAL_NOT_NATIVE"})

    def __getattr__(self, name):
        self.model.bad("unmodelled os operation " + name)


class ModelLP:
    def __init__(self, model):
        self.model = model

    def proc_listallpids(self, buf, size):
        self.model.guard()
        if buf is None:
            self.model.scan_begin()
        pids = sorted(self.model.procs)
        if buf is not None:
            for i, pid in enumerate(pids):
                buf[i] = pid
        self.model.record("proc_listallpids", {"pids": pids, "capacity_bytes": size})
        return len(pids)

    def proc_pidinfo(self, pid, flavor, zombies, buf, size):
        self.model.guard()
        stack = source_frames()
        self.model.checkpoint(stack)
        self.model.metadata_read(pid, stack)
        p = self.model.procs.get(pid)
        error = self.model.flavor_errors.get((pid, flavor))
        if p is None or pid in self.model.ident_errors or error is not None:
            ctypes.set_errno(error or (errno.EACCES if pid in self.model.ident_errors else errno.ESRCH))
            self.model.record("proc_pidinfo", {"pid": pid, "flavor": flavor, "returned": 0,
                                               "model_errno": ctypes.get_errno()})
            return 0
        raw = bytearray(size)
        if flavor == 17 and size == 56:
            struct.pack_into("=Q", raw, 16, p["uniqueid"])
            struct.pack_into("=i", raw, 32, p["idversion"])
        elif flavor == 13 and size == 64:
            struct.pack_into("=IIII", raw, 0, pid, p["ppid"], p["pgid"], p["status"])
            raw[16:32] = p["comm"].encode()[:15].ljust(16, b"\0")
            struct.pack_into("=II", raw, 32, 2 if p["traced"] else 0, p["euid"])
            struct.pack_into("=I", raw, 44, p["ruid"])
        elif flavor == 4 and size == 96:
            # Persistent monotonic CPU accumulator over declared rate history; civil time never alters ticks.
            ticks = self.model.cpu_ticks(p)
            struct.pack_into("=QQQ", raw, 8, p["rss"], ticks, 0)
        elif flavor == 3 and size == 136:
            seconds = int(p["start_epoch"])
            struct.pack_into("=QQ", raw, 120, seconds, 0)
        elif flavor == 9 and size == 2352:
            cwd = self.model.cfg["lane"].encode() + b"\0"
            raw[152:152 + len(cwd)] = cwd
        else:
            self.model.bad("unmodelled libproc flavor")
        buf.raw = bytes(raw)
        self.model.record("proc_pidinfo", {"pid": pid, "flavor": flavor, "returned": size,
                                           "identity": self.model.identity(p)})
        return size


class ModelLC:
    def __init__(self, model):
        self.model = model

    def mach_timebase_info(self, pointer):
        self.model.guard()
        pointer._obj.numer, pointer._obj.denom = 1, 1
        return 0

    def sysctl(self, mib, count, out, size, new, length):
        self.model.guard()
        if list(mib) == [1, 8]:
            out._obj.value = 1 << 20
            size._obj.value = ctypes.sizeof(ctypes.c_int)
            return 0
        if count == 3 and list(mib)[:2] == [1, 49]:
            raw = struct.pack("=i", 1) + b"/MODEL/python\0\0/MODEL/python\0"
            out.raw = raw.ljust(len(out), b"\0")
            size._obj.value = len(raw)
            return 0
        self.model.bad("unmodelled sysctl")


class Model:
    def __init__(self, budget, source_raw):
        self.budget, self.source_raw = budget, source_raw
        budget.model = self  # Preserve partial raw evidence if a fixed boundary is not reached.
        self.calls = 0
        self.operations = []
        self.op_hash = hashlib.sha256()
        self.verbose = True
        self.violations = []
        self.halted = False
        self.clock = ModelClock(self)
        self.signals = ModelSignals(self)
        self.os = ModelOS(self)
        self.stdout, self.stderr = ModelStream(self, "stdout"), ModelStream(self, "stderr")
        self.procs = {1: self.process(1, 0)}
        self.ident_errors = set()
        self.flavor_errors, self.transitions, self.spawn_overrides = {}, [], {}
        self.next_helper = 700000100
        self.helper_holds = False
        self.wait_return_mono = None
        self.scan_mode = None
        self.top_scans = 0
        self.checkpoint_mode = None
        self.mark = None
        self.calibration = False
        self.s = None
        self.ns = None
        self.cfg = None
        self.inputs = {}
        self.steps = []
        self.disclosures = []

    def guard(self):
        if self.halted:
            raise CalibrationStop()
        self.calls += 1
        if self.calls > 1500000:
            raise BudgetStop("model operation ceiling")
        if self.calls % 128 == 0:
            self.budget.check()

    def bad(self, reason):
        self.violations.append(reason)
        raise ModelBoundary(reason)

    def record(self, operation, fields):
        event = {"index": self.calls, "operation": operation, "scope": "MODEL_INPUT", **safe(fields)}
        self.op_hash.update(canonical(event))
        if self.verbose:
            if len(self.operations) >= 16000:
                self.bad("model retained trace ceiling")
            self.operations.append(event)

    @staticmethod
    def process(pid, uid=MODEL_UID):
        return {"pid": pid, "uniqueid": pid + 1000000000, "idversion": 1, "ppid": MODEL_PID if pid != 1 else 0,
                "pgid": pid, "status": 2, "euid": uid, "ruid": uid, "traced": False, "comm": "MODEL",
                "rss": 4096, "cpu_rate": 0.0, "start_epoch": EPOCH - 100.0,
                # Declared MODEL start in UNHOOKED monotonic time (same 100s age); accumulated CPU ns since then.
                "cpu_ns": 0.0, "cpu_mono": MONO - 100.0, "cpu_observed": False}

    @staticmethod
    def identity(p):
        return {k: p[k] for k in ("pid", "ppid", "pgid", "status", "euid", "ruid", "traced", "comm", "uniqueid", "idversion")}

    def accrue_cpu(self, p):
        """Settle the declared rate over UNHOOKED elapsed MODEL monotonic time; returned counters never decrease."""
        now = self.clock.mono
        if now > p["cpu_mono"]:
            p["cpu_ns"] += (now - p["cpu_mono"]) * 1e9 * p["cpu_rate"]
            p["cpu_mono"] = now

    def cpu_ticks(self, p):
        self.accrue_cpu(p)
        p["cpu_observed"] = True
        return int(p["cpu_ns"])

    def set_cpu_rate(self, p, rate):
        """Declared rate transition: the previous rate is settled first; history is never rewritten."""
        self.accrue_cpu(p)
        p["cpu_rate"] = rate

    def declare_cpu_history(self, p, rate):
        """Declared constant rate since the declared MODEL start; refused once any counter was returned."""
        if p["cpu_observed"]:
            self.bad("retroactive MODEL CPU history after a returned counter")
        p.update(cpu_rate=rate, cpu_ns=0.0, cpu_mono=MONO - 100.0)

    def site(self, function, snippet):
        nodes = [n for n in ast.walk(self.tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == function]
        if len(nodes) != 1:
            raise ModelBoundary("ambiguous source symbol " + function)
        node = nodes[0]
        lines = self.source_raw.decode().splitlines()
        hits = [n for n in range(node.lineno, node.end_lineno + 1) if snippet in lines[n - 1]]
        if len(hits) != 1:
            raise ModelBoundary("missing/ambiguous source anchor " + function + ":" + snippet)
        return hits[0]

    @staticmethod
    def matches(stack, rule):
        if not any(name == rule["function"] and line == rule["line"] for name, line, _ in stack):
            return False
        return all(any(name == item["function"] and (item["line"] is None or line == item["line"])
                       for name, line, _ in stack) for item in rule.get("within", []))

    def within(self, function, snippet=None):
        return {"function": function, "snippet": snippet, "line": None if snippet is None else self.site(function, snippet)}

    def clock_rule(self, function, snippet, value=None, occurrence=1, clock="monotonic", action="set", within=()):
        rule = {"function": function, "snippet": snippet, "line": self.site(function, snippet),
                "clock": clock, "action": action, "within": list(within),
                "set_to": value, "occurrence": occurrence, "seen": 0, "fired": False,
                "returned": None, "exception_type": None}
        self.clock.rules.append(rule)
        return rule

    def transition(self, pid, field, value, after_reads=0, source=None):
        rule = {"pid": pid, "field": field, "value": value, "after_reads": after_reads,
                "source": source, "seen": 0, "fired": False}
        self.transitions.append(rule)
        return rule

    def metadata_read(self, pid, stack):
        for rule in self.transitions:
            if rule["fired"] or pid != rule["pid"]:
                continue
            if rule["source"] is not None and not any(
                    name == "acquire_identity" and frame.f_locals.get("source") == rule["source"]
                    for name, _, frame in stack):
                continue
            if rule["seen"] == rule["after_reads"]:
                p = self.procs[pid]
                rule["before"] = self.identity(p)
                p[rule["field"]] = rule["value"]
                rule["after"], rule["fired"] = self.identity(p), True
                self.record("metadata_transition", dict(rule, response_scope="API_RESPONSE_INJECTION"))
            rule["seen"] += 1

    def checkpoint(self, stack):
        if self.mark is not None or self.checkpoint_mode is None or self.s is None:
            return
        found = False
        if self.checkpoint_mode in ("final_rss", "initial_main"):
            wanted = "measurement_final_bracket" if self.checkpoint_mode == "final_rss" else "main_initial"
            found = any(name == "retain_identity" and frame.f_locals.get("source") == wanted for name, _, frame in stack)
        elif self.checkpoint_mode == "helper_term":
            found = any(name == "census" for name, _, _ in stack) and self.s.in_helper
        if not found:
            return
        self.mark = {"mode": self.checkpoint_mode, "history_charge_before": self.s.history_charge,
                     "mono_before": self.clock.mono, "stack": [{"symbol": n, "line": line} for n, line, _ in stack]}
        self.record("history_checkpoint", self.mark)
        if self.calibration:
            self.halted = True
            raise CalibrationStop()

    def scan_begin(self):
        if self.s is None or self.s.in_helper:
            return
        stack = source_frames()
        if not any(name == "census" for name, _, _ in stack):
            return
        self.top_scans += 1
        self.ident_errors.clear()
        if self.scan_mode and self.top_scans == 1:
            unknown, broken = self.process(700000030), self.process(700000031, 0)
            if self.scan_mode == "unproved":
                self.procs[unknown["pid"]] = unknown
            elif self.scan_mode == "busy":
                self.declare_cpu_history(self.procs[MODEL_MAIN], 1.0)
                other = self.process(700000020)
                self.declare_cpu_history(other, 1.0)
                self.procs[other["pid"]] = other
                acquired = self.s.observed_identity(other["pid"], "MODEL_RUNNING_EXTRA", True)
                self.s.register_owned(acquired, "child")
                self.disclosures.append("Declared MODEL listing-callback insertion: extra pid700000020 is acquired/registered by original methods before listing return; no native sampled-ownership claim.")
                self.disclosures.append("MODEL CPU ticks are persistent accumulators over UNHOOKED monotonic MODEL time and declared rate history (busy history declared before any returned counter); civil-clock shifts never alter ticks.")
            elif self.scan_mode == "rss":
                self.procs[MODEL_MAIN]["rss"] = self.cfg["rss_trip_bytes"] + 1
            self.procs[broken["pid"]] = broken
            self.ident_errors.add(broken["pid"])
        elif self.scan_mode and self.top_scans > 1:
            for pid in (700000020, 700000030, 700000031):
                self.procs.pop(pid, None)
            if MODEL_MAIN in self.procs:
                self.procs[MODEL_MAIN]["rss"] = 4096
                self.set_cpu_rate(self.procs[MODEL_MAIN], 0.0)


def config(run, wall=10.0):
    out = run + "/out"
    return {"item": "MODEL_NOT_AN_ITEM_GO", "owner": "MODEL", "purpose": "guard-qualification", "lane": LANE,
            "argv": ["/MODEL/python", "/MODEL/fixed-nonforking-child"], "env": {"TMPDIR": run + "/tmp"},
            "stdout": out + "/stdout", "stderr": out + "/stderr", "samples": out + "/samples",
            "launch_record": out + "/launch.json", "receipt": out + "/receipt.json", "settlement_record": out + "/settlement.json",
            "stdout_cap_bytes": 65536, "stderr_cap_bytes": 65536, "samples_cap_bytes": 65536,
            "outputs": [], "output_roots": [out], "pins": [], "max_wall_s": wall, "settle_s": 0.5,
            "sample_s": 0.2, "max_chunk_seconds": 10800.0, "owned_compute_settled_by_epoch": EPOCH + 20000,
            "rss_trip_bytes": 1048576, "rss_projection_bytes": 4096, "free_trip_bytes": 12000000000,
            "launch_free_min_bytes": 12200000000, "output_trip_bytes": 1048576, "lane_roots": [LANE],
            "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 30.0,
            "busy_limit": 1, "busy_cpu_fraction": 0.5, "cpu_slots": 1,
            "admission": {"go_path": run + "/go.json", "stability_receipt_path": run + "/stability.json",
                          "reservation_bytes": 20971520, "outstanding_reservations_bytes": 0,
                          "lane_outstanding_reservations_bytes": 0, "stability_max_age_s": 300.0},
            "helper_budget": {"max_calls": 32, "call_budget_s": 1.0, "term_grace_s": 0.01},
            "fault_injection": {}, "creation_channel": {}}


def extract(model):
    tree = ast.parse(model.source_raw.decode(), filename=SUPERVISOR)
    model.tree = tree
    names = {"VERSION", "CANCEL_SIGNALS", "CANCEL", "CANCEL_FAILURE_TARGET", "POLICY", "SMALL", "PIN_CAP", "PUBLICATION_CAP", "IO_S",
             "CENSUS_S", "FINALIZE_S", "WALK_ENTRIES", "ROOT_ENTRIES", "CONFIG", "HELPER", "HELPER_FAULTS",
             "ADMISSION", "BOUND_KEYS", "MY_PID", "MY_UID", "SELF", "SZOMB"}
    classes = {"GuardError", "Deadline", "Timebase", "Supervisor"}
    functions = {"cancel", "protected", "pending_cancel", "timebase", "argmax", "pidinfo", "unique", "short", "fingerprint",
                 "identify", "cwd_of", "argv_of", "task_of", "start_of", "all_pids", "read_file", "write_all", "bytes_json",
                 "pairs", "json_float", "json_constant", "parse_json", "parse_date_epoch", "norm_abs", "below", "directory_at",
                 "absolute_directory", "stat_id", "list_directory", "walk_fd", "create_file", "publish", "linked_publication",
                 "number", "integer", "hex64", "validate", "spawn_registered", "admission", "launch_and_go", "observe",
                 "exception_code", "refuse", "unsuccessful", "finalize", "final_body"}
    functions.update(("identity_form", "typed_equal", "install_main_identity", "recover_registered_main"))
    def thread_unavailable(*args, **kwargs):
        model.bad("thread creation outside fixed state fixtures")
    allowed_builtins = {key: getattr(builtins, key) for key in (
        "__build_class__", "object", "property", "staticmethod", "classmethod", "dict", "list", "tuple", "set",
        "frozenset", "bytes", "bytearray", "str", "float", "int", "bool", "memoryview", "len", "min", "max", "sum",
        "sorted", "reversed", "all", "any", "range", "enumerate", "zip", "next", "iter", "isinstance", "type", "getattr",
        "hasattr", "repr", "abs", "round", "BaseException", "Exception", "OSError", "ValueError", "TypeError",
        "KeyError", "AttributeError", "IndexError", "ChildProcessError", "ProcessLookupError", "BlockingIOError",
        "FileNotFoundError", "FileExistsError", "NotADirectoryError", "StopIteration")}
    memory_ctypes = SimpleNamespace(**{key: getattr(ctypes, key) for key in (
        "Structure", "c_int", "c_uint", "c_uint64", "c_void_p", "c_size_t", "c_uint32", "create_string_buffer",
        "sizeof", "byref", "set_errno", "get_errno", "string_at")})
    ns = {"__name__": "MODIFIED_QUALIFICATION_FIXTURE", "__file__": SUPERVISOR, "__builtins__": allowed_builtins,
          "contextlib": contextlib, "ctypes": memory_ctypes, "datetime": datetime, "errno": errno, "hashlib": hashlib,
          "json": ModelJSON(model), "math": math, "os": model.os, "signal": model.signals, "stat": stat, "struct": struct,
          "sys": SimpleNamespace(stdout=model.stdout, stderr=model.stderr), "threading": SimpleNamespace(Thread=thread_unavailable),
          "time": model.clock, "LP": ModelLP(model), "LC": ModelLC(model)}
    selected, symbols = [], []
    lines = model.source_raw.splitlines(keepends=True)
    for node in tree.body:
        take = isinstance(node, ast.ClassDef) and node.name in classes or isinstance(node, ast.FunctionDef) and node.name in functions
        label = node.name if isinstance(node, (ast.ClassDef, ast.FunctionDef)) else None
        if isinstance(node, ast.Assign):
            assigned = {x.id for target in node.targets for x in ast.walk(target) if isinstance(x, ast.Name)}
            if assigned and assigned <= names:
                take, label = True, ",".join(sorted(assigned))
        if take:
            selected.append(node)
            start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
            raw = b"".join(lines[start - 1:node.end_lineno])
            symbols.append({"symbol": label, "line_begin": start, "line_end": node.end_lineno,
                            "sha256": hashlib.sha256(raw).hexdigest()})
    present = {n.name for n in selected if isinstance(n, (ast.ClassDef, ast.FunctionDef))}
    if present != classes | functions:
        raise ModelBoundary("required original AST symbol set changed")
    exec(compile(ast.Module(body=selected, type_ignores=[]), SUPERVISOR, "exec"), ns)
    model.ns = ns
    model.symbols = symbols
    return ns


def install_model_files(model, cfg):
    model.cfg = cfg
    fs = model.os
    fs.ensure_dir(LANE)
    fs.ensure_dir(cfg["output_roots"][0])
    fs.ensure_dir(cfg["env"]["TMPDIR"])
    fs.put(SUPERVISOR, model.source_raw)
    raw_cfg = canonical(cfg)
    digest = hashlib.sha256(raw_cfg).hexdigest()
    model.config_digest = digest
    model.config_bytes = raw_cfg
    receipt_epoch = EPOCH - 200.0
    text = datetime.datetime.fromtimestamp(receipt_epoch, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
    stability = canonical({"verdict": "PASS", "now_date": text})
    go = {"decision": "GO", "item": cfg["item"], "configs": {digest: {k: cfg[k] for k in model.ns["BOUND_KEYS"][:5]}},
          "not_after_epoch": EPOCH + 10000, "stability_receipt_sha256": hashlib.sha256(stability).hexdigest()}
    go["configs"][digest].update({k: cfg["admission"][k] for k in model.ns["BOUND_KEYS"][5:]})
    if cfg["creation_channel"]:
        go["qualification_negative"] = {"scenario": cfg["creation_channel"]["scenario"], "kind": "mutation", "creation_channel": True}
    fs.put(cfg["admission"]["go_path"], canonical(go))
    fs.put(cfg["admission"]["stability_receipt_path"], stability)
    model.virtual_authority = {"scope": "MODEL_AUTHORIZATION_BYTES_NOT_AUTHORITY", "config": cfg,
                               "config_sha256": digest, "go": go, "stability": decode(stability)}
    return digest


def setup(case, source_raw, budget, wall=None, run_override=None, ready=True):
    m = Model(budget, source_raw)
    ns = extract(m)
    cfg = config(run_override or ROOT + "/" + case, wall or (200.0 if case.startswith("st_go_w200_") else 10.0))
    if case.startswith(("st_complete_go_fit_", "st_complete_ack_fit_")):
        cfg["owned_compute_settled_by_epoch"] = EPOCH + 220.0  # Original constructor selects fit epoch EPOCH+40.
    digest = install_model_files(m, cfg)
    ns["validate"](cfg)
    s = ns["Supervisor"](cfg, ROOT + "/" + case + "/MODEL_CONFIG_NOT_NATIVE.json", digest)
    m.s = s
    s.open_anchors()
    s.establish_baseline()
    s.authorization_io(ns["Deadline"](30.0))
    if ready:
        value = s.date_now("admission")
        if value is None or s.failures:
            raise ModelBoundary("model setup helper failed")
    # Only initial construction is common; every later prestate is declared in the case report.
    m.operations.clear()
    m.op_hash = hashlib.sha256()
    m.calls = 0
    return m


def registered_main(m):
    """Declared MODEL registered-record prestate, with no native spawn or implicit identity."""
    s = m.s
    m.procs[MODEL_MAIN] = m.process(MODEL_MAIN)
    m.procs[MODEL_MAIN]["hold"] = True
    child = {"pid": MODEL_MAIN, "role": "child", "identity": None, "leader_reaped": False, "rc": None,
             "wait_lost": False, "term_attempted": False, "settled": False, "stdout_fd": None,
             "stderr_fd": None, "stdin_fd": None, "spawn_error": None, "parent_close_fds": [],
             "mono_spawn": MONO, "epoch_spawn": EPOCH}
    s.child, s.pid = child, MODEL_MAIN
    s.keep.append(child)
    s.mono_spawn, s.epoch_spawn = MONO, EPOCH
    s.phase = "RUNNING"
    m.disclosures.append("MODEL registered child prestate, not a native spawn/session/ownership proof.")


def running(m, previous_stop=False):
    s = m.s
    registered_main(m)
    ident = s.observed_identity(MODEL_MAIN, "MODEL_RUNNING_INITIAL", True)
    s.ident, s.group = ident, MODEL_MAIN
    s.register_owned(ident, "child")
    if previous_stop:
        s.stop = {"reason": "MODEL_PREEXISTING_STOP", "mono": MONO - 0.01, "epoch": EPOCH - 0.01, "date": None}
        m.disclosures.append("Declared reachable prior-stop prestate isolates resource retention from nested stop-date census; no new stop/signal claim.")


def step(m, label, function, *args):
    if not m.verbose:
        raise ModelBoundary("step operation trace must be retained")
    # The model call counter brackets this step so the oracle can prove its event slice is complete.
    before = {"mono": m.clock.mono, "history_charge": None if m.s is None else m.s.history_charge, "calls": m.calls}
    item = {"label": label, "before": before, "args": safe(list(args)), "return": None, "exception": None}
    item["event_begin"] = len(m.operations)
    item["counts_before"] = {name: None if m.s is None else len(getattr(m.s, name)) for name in
                             ("identity_history", "unproved_history", "coverage_history", "attempt_history", "census_history")}
    try:
        item["return"] = safe(function(*args))
    except CalibrationStop:
        raise
    except BudgetStop:
        raise
    except BaseException as error:
        item["exception"] = {"type": type(error).__name__, "code": m.ns["exception_code"](error),
                             "text": utf8_hex(repr(error))}
    item["after"] = {"mono": m.clock.mono, "history_charge": None if m.s is None else m.s.history_charge, "calls": m.calls}
    item["event_end"] = len(m.operations)
    item["counts_after"] = {name: None if m.s is None else len(getattr(m.s, name)) for name in item["counts_before"]}
    m.steps.append(item)
    return item


def caps(m):
    def comparison(function, left_fragment, value):
        line = m.site(function, left_fragment)
        node = next(n for n in ast.walk(m.tree) if isinstance(n, ast.FunctionDef) and n.name == function)
        matches = [n for n in ast.walk(node) if isinstance(n, ast.Compare) and n.lineno == line]
        if len(matches) != 1:
            raise ModelBoundary("cap comparison changed")
        expression = matches[0].comparators[0]
        # Only constant integer/left-shift expressions are admitted, never eval arbitrary source.
        def number(n):
            if isinstance(n, ast.Constant) and type(n.value) is int:
                return n.value
            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.LShift):
                return number(n.left) << number(n.right)
            raise ModelBoundary("nonliteral source cap")
        actual = number(expression)
        if actual != value:
            raise ModelBoundary("original source cap changed")
        return {"value": actual, "symbol": function, "line": line, "operator": type(matches[0].ops[0]).__name__}
    return {"bytes": comparison("reserve_history", "self.history_charge + charge >", 4 << 20),
            "identity": comparison("retain_identity", "len(self.identity_history) >=", 8192),
            "unproved": comparison("retain_identity", "len(self.unproved_history) >=", 8192),
            "coverage": comparison("retain_coverage", "len(self.coverage_history) >=", 16384),
            "attempt": comparison("observation_attempt", "len(self.attempt_history) >=", 4096),
            "census": comparison("census", "len(self.census_history) >=", 4096),
            "variants": comparison("retain_identity", "len(variants) >=", 64),
            "raw": comparison("raw_acquisition", "len(self.raw_acquisitions) >=", 128),
            "clockless": comparison("helper_clockless_once", "if count >=", 3)}


def histories(m):
    s = m.s
    def limited(value):
        seq = list(value.values()) if isinstance(value, dict) else list(value)
        if len(seq) <= 100:
            return {"count": len(seq), "entries": seq, "omitted": 0}
        return {"count": len(seq), "entries": seq[:1] + seq[-2:], "omitted": len(seq) - 3,
                "scope": "MODEL_PRESTATE_COUNT_ISOLATION_NOT_FULL_PHYSICAL_HISTORY"}
    out = {k: limited(getattr(s, k)) for k in ("identity_history", "unproved_history", "coverage_history",
                                              "attempt_history", "census_history")}
    return out


def raw_state(m):
    s = m.s
    names = ("phase", "pid", "ident", "group", "rc", "lost_wait", "mono_spawn", "epoch_spawn", "exit_mono", "exit_epoch",
             "stop", "signal", "clear", "loop_status", "failures", "trips", "runtime_observations", "history_charge",
             "history_halted", "history_overflow", "stability_expiry_mono", "clock_observation", "authorization",
             "maxima", "min_free", "publication_resources", "ack_resources", "publication_payload_bytes",
             "last_accounting_observation", "accounting_observations", "min_free_witness", "identity_events",
             "helper_calls", "helper_log", "ack_output_started", "cancel_handled", "rec", "timing_failed",
             "last_native_free", "streams", "raw_sequence")
    out = {key: getattr(s, key) for key in names}
    out.update(histories=histories(m), helpers=s.helper_reports(), cancel=dict(m.ns["CANCEL"]),
               pending_signals=sorted(int(x) for x in m.signals.pending), failure_codes=sorted(s.failure_keys),
               owned=list(s.owned.values()), baseline_uniqueids=sorted(s.baseline or []),
               raw_acquisitions=list(s.raw_acquisitions.values()),
               main_wait=None if s.child is None else {key: s.child.get(key) for key in
                   ("pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "wait_lost",
                    "mono_reaped", "epoch_reaped", "mono_reaped_error", "epoch_reaped_error")},
               cancellation_target_installed=m.ns["CANCEL_FAILURE_TARGET"] is s,
               anchor_fds={"lane": s.lane_fd, "tmp": s.tmp_fd, "roots": sorted(fd for fd, _ in s.root_fds.values())})
    return safe(out)


def suffix_delta(case, amount=0.01):
    return {"lt": -amount, "eq": 0.0, "gt": amount}[case.rsplit("_", 1)[1]]


def count_cap_case(m, case, limits):
    s, ns = m.s, m.ns
    family = case.split("_")[2]
    limit = limits[family]["value"]
    desired = limit + int(suffix_delta(case, 1))
    pre = max(0, desired - 1)
    m.inputs.update(family=family, cap=limits[family], requested_post_count=desired, pre_count=pre,
                    count_semantics="one attempted append; lt/eq allowed, gt rejected")
    s.pid = None
    s.baseline = set()
    s.identity_history, s.unproved_history = {}, {}
    s.coverage_history, s.attempt_history, s.census_history = [], [], []
    s.identity_events, s.identity_refs = [], {}
    m.verbose = False
    total = 0
    if family in ("identity", "unproved"):
        for i in range(pre):
            p = m.process(100000 + i)
            s.history_charge = 0
            s.retain_identity(m.identity(p), "MODEL_PREFILL", family == "identity", (MONO, MONO))
            total += s.history_charge
        # Byte charge is deliberately independent; these are explicit count-predicate prestates.
        s.history_charge = 0
        if family == "unproved":
            s.identity_history = {}
            m.disclosures.append("Unproved-count isolation resets the separate identity ledger so its equal8192 cap cannot preempt the tested unproved branch; this joint prestate is not physical coverage.")
        test = m.identity(m.process(900000))
        m.target_uid = test["uniqueid"]
        m.verbose = True
        step(m, "retain_identity", s.retain_identity, test, "MODEL_TARGET", family == "identity", (MONO, MONO))
    elif family == "coverage":
        for i in range(pre):
            s.history_charge = 0
            s.retain_coverage([[i + 1, "identify", "MODEL_EACCES"]], MONO)
            total += s.history_charge
        s.history_charge = 0
        m.verbose = True
        step(m, "retain_coverage", s.retain_coverage, [[900000, "identify", "MODEL_EACCES"]], MONO)
    elif family == "attempt":
        for _ in range(pre):
            s.history_charge = 0
            with s.observation_attempt("MODEL_PREFILL"):
                pass
            total += s.history_charge
        s.history_charge = 0
        m.verbose = True
        def attempt():
            with s.observation_attempt("MODEL_TARGET") as value:
                return dict(value)
        step(m, "observation_attempt", attempt)
    elif family == "census":
        template = s.census(ns["Deadline"](10.0))
        total = s.history_charge
        s.census_history = [dict(template) for _ in range(pre)]
        s.attempt_history = []
        s.history_charge = 0
        m.verbose = True
        step(m, "census", s.census, ns["Deadline"](10.0))
        m.inputs["census_template"] = safe(template)
        m.disclosures.append("Census templates are replicated MODEL prestates; corresponding attempt ledger is reset. Every real census ordinarily consumes resource+identity attempts; attempt/byte caps dominate this isolated count boundary.")
    elif family == "variants":
        p = m.process(900000)
        for i in range(pre):
            p["idversion"] = i + 1
            s.retain_identity(m.identity(p), "MODEL_VARIANT_PREFILL", True, (MONO, MONO))
        total = s.history_charge
        p["idversion"] = pre + 1
        m.target_uid = p["uniqueid"]
        m.verbose = True
        step(m, "retain_identity", s.retain_identity, m.identity(p), "MODEL_TARGET", True, (MONO, MONO))
    else:
        raise ModelBoundary("fixed cap family")
    m.inputs["prefill_unreset_charge_sum"] = total
    m.inputs["prestate_byte_charge_reset"] = family != "variants"
    if family != "variants":
        m.disclosures.append("Count-cap prestate isolates original count branch by resetting history charge during construction; jointly unreachable/dominated byte-cap states are NOT physical/native coverage. Sum before resets is disclosed, not silently treated as a reachable complete ledger.")


def critical_case(case, source_raw, budget, limits):
    mode = {"st_cap_final_rss": "final_rss", "st_cap_initial_main": "initial_main", "st_cap_helper_term": "helper_term"}[case]
    def prepared(calibration):
        q = setup(case, source_raw, budget)
        q.inputs = {"critical_mode": mode}
        if mode == "final_rss":
            running(q, True)
            q.procs[MODEL_MAIN]["rss"] = q.cfg["rss_trip_bytes"] + 1
        elif mode == "initial_main":
            q.s.phase = "ADMISSION"
        else:
            q.helper_holds = True
        q.checkpoint_mode, q.calibration = mode, calibration
        return q
    calibration = prepared(True)
    baseline = calibration.s.history_charge
    try:
        if mode == "final_rss":
            calibration.s.census(calibration.ns["Deadline"](10.0))
        elif mode == "initial_main":
            calibration.ns["launch_and_go"](calibration.s)
        else:
            calibration.s.date_now("start")
    except CalibrationStop:
        pass
    if calibration.mark is None:
        raise ModelBoundary("critical original source boundary was not reached")
    target = calibration.mark["history_charge_before"]
    m = prepared(False)
    precharge = m.s.history_charge + limits["bytes"]["value"] - target
    if precharge < m.s.history_charge:
        raise ModelBoundary("calibration already beyond cap")
    m.s.history_charge = precharge
    m.inputs.update(cap=limits["bytes"], declared_precharge=precharge,
                    calibration={"baseline_charge": baseline, "target": calibration.mark,
                                 "scope": "ORIGINAL_METHOD_CALIBRATION_MODEL_ONLY"})
    if mode == "final_rss":
        step(m, "census", m.s.census, m.ns["Deadline"](10.0))
        step(m, "halted_census_retry", m.s.census, m.ns["Deadline"](10.0))
    elif mode == "initial_main":
        step(m, "launch_and_go", m.ns["launch_and_go"], m.s)
    else:
        step(m, "date_now", m.s.date_now, "start")
    if m.mark is None or not m.s.history_halted or m.s.history_overflow is None or \
            m.s.history_overflow["kind"] != "HISTORY_BYTE_CAP":
        raise ModelBoundary("actual critical byte-cap boundary was not reached")
    return m


def output_budget(case, source_raw, budget):
    delta = int(suffix_delta(case, 1))
    size = 500000
    calibration = []
    result = None
    for _ in range(5):
        m = setup(case, source_raw, budget)
        m.inputs = {}
        m.os.put(m.cfg["env"]["TMPDIR"] + "/MODEL_CHARGED_PADDING", logical_size=size)
        step(m, "finalize", m.ns["finalize"], m.s)
        payload = m.s.publication_payload_bytes
        calibration.append({"padding": size, "payload": payload})
        if payload is None:
            raise ModelBoundary("finalize payload boundary not reached")
        desired = m.cfg["output_trip_bytes"] + delta - payload
        if desired == size:
            result = m
            break
        if not 10000 <= desired <= m.cfg["output_trip_bytes"]:
            raise ModelBoundary("bounded output calibration unavailable")
        size = desired
    if result is None:
        raise ModelBoundary("output byte calibration did not converge")
    result.inputs = {"family": "output", "delta": delta, "padding": size, "calibration": calibration,
                     "payload_bytes": result.s.publication_payload_bytes,
                     "limit": result.cfg["output_trip_bytes"], "source_entry": "finalize -> final_body actual serialized rb+sb"}
    return result


def manifest_case(case, source_raw, budget):
    target = int(case.rsplit("_", 1)[1])
    selected = None
    # Padding appears three times in original canonical line. Inode digit width supplies the residue.
    for residue in range(3):
        trial = setup(case, source_raw, budget, run_override=ROOT + "/" + case + "/" + "x" * 10)
        base = build_manifest(trial, 10 ** (3 + residue))
        item = step(trial, "creation_manifest", trial.s.creation_manifest, trial.ns["Deadline"](30.0))
        if item["exception"] is not None or not isinstance(item["return"], dict):
            raise ModelBoundary("manifest calibration failed")
        length = item["return"]["bytes"]
        difference = target - length
        if difference >= 0 and difference % 3 == 0:
            width = 10 + difference // 3
            m = setup(case, source_raw, budget, run_override=ROOT + "/" + case + "/" + "x" * width)
            prep = build_manifest(m, 10 ** (3 + residue))
            m.inputs = {"target_length": target, "padding_width": width, "inode_residue": residue,
                        "preparation": prep, "actual_original_target": m.fixture_facts,
                        "scope": "MODEL_LONG_PATH_AND_MODEL_INODE_NOT_NATIVE_PATH_COVERAGE"}
            step(m, "creation_manifest", m.s.creation_manifest, m.ns["Deadline"](30.0))
            selected = m
            break
    if selected is None:
        raise ModelBoundary("manifest exact length calibration unavailable")
    return selected


def build_manifest(m, inode):
    cfg, fs, s = m.cfg, m.os, m.s
    out = cfg["output_roots"][0]
    run = os.path.dirname(out)
    path = run + "/pinned-scratch.txt"
    data = b"MODEL original fixture bytes\n"
    node = fs.put(path, data)
    node.inode = inode
    fixture = {"path": path, "inode": [771, inode], "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "nlink": 1}
    prep = {"kind": "qualification-creation-preparation-v1", "scenario": "mutate_pin",
            "run": {"path": run, "inode": [771, fs.nodes[run].inode]},
            "output_root": {"path": out, "inode": list(s.root_fds[out][1])}, "fixture": fixture,
            "source_pins": {key: {"path": SUPERVISOR if key == "supervisor" else LANE + "/MODEL/" + key,
                                  "sha256": SUPERVISOR_SHA if key == "supervisor" else "0" * 64}
                            for key in ("supervisor", "child", "writer", "checker")},
            "python": {"path": cfg["argv"][0], "sha256": "0" * 64},
            "allocation": {"bytes": cfg["admission"]["reservation_bytes"], "cpu_slots": cfg["cpu_slots"],
                           "outstanding_reservations_bytes": 0, "lane_outstanding_reservations_bytes": 0}, "negative_control": True}
    raw = canonical(prep)
    fs.put(run + "/preparation.json", raw)
    cfg["creation_channel"] = {"kind": "qualification-creation-v1", "scenario": "mutate_pin",
                               "preparation_path": run + "/preparation.json", "preparation_sha256": hashlib.sha256(raw).hexdigest(),
                               "target_path": path}
    # This is solely a virtual model config/GO update, never a physical authorization or fixture mutation.
    s.config_sha = install_model_files(m, cfg)
    s.authorization = None
    s.authorization_io(m.ns["Deadline"](30.0))
    m.fixture_facts = fixture
    return prep


def helper_prestate(m):
    """Original fixed /bin/date MODEL spawn, held only in the closed process model."""
    s, ns = m.s, m.ns
    m.helper_holds, s.in_helper = True, True
    call = s.deadline(s.cfg["helper_budget"]["call_budget_s"])
    start = m.clock.mono
    try:
        h = ns["spawn_registered"](s, ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], {"PATH": "/usr/bin:/bin"},
                                    "helper", call, 1.01)
    finally:
        s.in_helper = False
    h.update(capture=b"", raw_eof=False, stdout_closed=False, capture_overflow=False,
             initial_identity_valid=False, clock_failed=False, fault_group=False, fault_eof=False,
             mono_call_start=start, mono_call_deadline=call.end, call_deadline=call.telemetry(), date=None)
    m.disclosures.append("Held helper is a MODEL process; original spawn/deadline record retained. No native helper or ownership clearance.")
    return h


def completion_case(m, case):
    _, _, phase, boundary, relation = case.split("_")
    phase = phase.upper()
    s, ns = m.s, m.ns
    if phase == "GO":
        running(m)
    delta = suffix_delta(case)
    deadline = ns["Deadline"](120.0, s.fit_mono)
    site = "epoch, mono = time.time(), time.monotonic()"
    if boundary == "auth":
        target = s.authorization["not_after_epoch"] + delta
        m.clock_rule("completion_check", site, target, clock="time", action="epoch")
    else:
        target = (s.fit_mono if boundary == "fit" else s.stability_expiry_mono) + delta
        m.clock_rule("completion_check", site, target, clock="time")
    m.clock_rule("completion_check", site, clock="monotonic", action="observe")
    m.inputs.update(phase=phase, boundary=boundary, relation=relation, delta=delta, target=target,
                    deadline=deadline.end, authorization=dict(s.authorization), fit_epoch=s.fit_epoch, fit_mono=s.fit_mono,
                    stability_expiry=s.stability_expiry_mono, observation=dict(s.clock_observation),
                    initial_mono=m.clock.mono, max_age=s.cfg["admission"]["stability_max_age_s"])
    m.disclosures.append("Original completion_check only; clock responses at its final paired read are API_RESPONSE_INJECTION. No native GO/ACK commit or caller cleanup claim.")
    with ns["protected"]():
        step(m, "protected_" + phase + "_completion", s.completion_check, phase, deadline)


def identity_case(m, case):
    s, ns = m.s, m.ns
    changed = {"uniqueid": 2700000010, "euid": 0, "ruid": 0, "idversion": 2,
               "ppid": 1, "pgid": 700000099, "traced": True}
    if case.startswith(("st_ident_signal_", "st_ident_read_")):
        field = case.rsplit("_", 1)[1]
        reading = case.startswith("st_ident_read_")
        running(m, reading)
        before = dict(s.ident)
        m.inputs.update(field=field, value=changed[field], before=before, mechanism="MID_IDENTIFY_READ" if reading else "FRESH_SIGNAL_RECHECK")
        if reading:
            m.transition(MODEL_MAIN, field, changed[field], after_reads=2, source="pid_scan")
            step(m, "full_census_with_identity_transition", s.full_census, ns["Deadline"](10.0))
        else:
            m.procs[MODEL_MAIN][field] = changed[field]
            m.inputs["after"] = m.identity(m.procs[MODEL_MAIN])
            step(m, "request_stop_changed_identity", s.request_stop, "MODEL_STOP_REQUEST")
    elif case == "st_ident_bracket_changed":
        running(m, True)
        m.transition(MODEL_MAIN, "ppid", 1, source="measurement_final_bracket")
        m.inputs.update(field="ppid", value=1, before=dict(s.ident))
        step(m, "census_final_bracket_changed", s.census, ns["Deadline"](10.0))
    elif case == "st_ident_mixed_uid_unreadable":
        running(m, True)
        p = m.process(700000040)
        p["euid"] = 0
        m.procs[p["pid"]] = p
        m.flavor_errors[(p["pid"], 4)] = errno.EACCES
        m.inputs.update(mixed_identity=m.identity(p), unreadable_flavor=4, model_errno=errno.EACCES)
        step(m, "full_census_mixed_real_effective_uid_unreadable", s.full_census, ns["Deadline"](10.0))
    elif case == "st_ident_main_initial_invalid":
        m.spawn_overrides["child"] = {"euid": 0}
        m.inputs.update(spawn_overrides=m.spawn_overrides)
        step(m, "launch_invalid_initial_effective_uid", ns["launch_and_go"], s)
    elif case == "st_ident_helper_signal_changed":
        h = helper_prestate(m)
        raw = s.acquire_identity(h["pid"], "MODEL_HELPER_INITIAL")
        h["identity"], h["initial_identity_valid"] = raw["identity"], True
        h["identity_event_ref"] = s.retain_acquisition(raw, True)
        s.register_owned(h["identity"], "helper")
        m.procs[h["pid"]]["pgid"] += 1
        m.inputs.update(before=dict(h["identity"]), after=m.identity(m.procs[h["pid"]]))
        dl = s.deadline(s.cfg["helper_budget"]["term_grace_s"])
        step(m, "helper_TERM_changed_fingerprint", s.helper_term, h, dl)
        step(m, "helper_TERM_not_retried", s.helper_term, h, dl)
        step(m, "helper_raw_cleanup_not_settlement", s.helper_clockless_once, h)
    m.disclosures.append("All UID/eUID/rUID/version/parent/group/trace bytes and transitions are MODEL ABI responses, not native metadata/platform qualification.")


def clock_case(m, case):
    s, ns = m.s, m.ns
    if case == "st_clock_cancel_after_target":
        running(m)
        m.clock_rule("cancel", 'CANCEL["mono"] = time.monotonic()', action="raise")
        step(m, "cancel_handler_clock_unavailable", ns["cancel"], int(signal.SIGTERM), None)
        m.inputs["immediate_handler_timing_failed"] = s.timing_failed
        s.cancel_handled = True  # Reconstruct the reported handled-cancel ACK escape prestate.
        step(m, "observe_cancel_clock_hold", ns["observe"], s)
    else:
        recovery = case == "st_clock_recovery_post_wait"
        prior = case.endswith("_prior_stop")
        if recovery:
            registered_main(m)
        else:
            running(m, prior)
        post = "after_wait" in case or recovery
        where = 'self.enforce_runtime("after_waitpid_including_success")' if post else 'self.enforce_runtime("before_waitpid")'
        m.clock_rule("enforce_runtime", "now = time.monotonic()", action="raise",
                     within=(m.within("reap", where),))
        if post and not recovery:
            m.wait_return_mono = MONO + 0.1
        m.inputs.update(runtime_check="after_waitpid_including_success" if post else "before_waitpid",
                        prior_stop=None if s.stop is None else dict(s.stop), recovery=recovery)
        if recovery:
            step(m, "recover_registered_main", ns["recover_registered_main"], s, ns["GuardError"]("MODEL postspawn failure"))
        else:
            step(m, "reap_clock_failure", s.reap)
        step(m, "reap_consumed_guard_or_zero_observation", s.reap)
    step(m, "finalize_sticky_timing_HOLD", ns["finalize"], s)


def cancel_before_target(case, source_raw, budget):
    m = Model(budget, source_raw)
    ns = extract(m)
    cfg = config(ROOT + "/" + case)
    digest = install_model_files(m, cfg)
    ns["validate"](cfg)
    m.inputs = {"handler_before_target": True}
    m.clock_rule("cancel", 'CANCEL["mono"] = time.monotonic()', action="raise")
    step(m, "cancel_before_target", ns["cancel"], int(signal.SIGHUP), None)
    m.inputs["target_at_handler"] = ns["CANCEL_FAILURE_TARGET"]
    m.s = ns["Supervisor"](cfg, ROOT + "/" + case + "/MODEL_CONFIG_NOT_NATIVE.json", digest)
    step(m, "baseline_refused_missing_timing", m.s.establish_baseline)
    step(m, "protected_commit_refused", m.s.time_commit, "ACK")
    step(m, "finalize_sticky_timing_HOLD", ns["finalize"], m.s)
    return m


def acquisition_case(m, case):
    s, ns = m.s, m.ns
    if case == "st_acq_main_identity_end_clock":
        registered_main(m)
        m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", action="raise",
                     within=(m.within("acquire_identity", 'self.aux_clock(raw, "mono_end")'), m.within("recover_registered_main")))
        step(m, "recover_identity_before_aux_end_failure", ns["recover_registered_main"], s, ns["GuardError"]("MODEL postspawn failure"))
        step(m, "finalize_sticky_timing_HOLD", ns["finalize"], s)
    elif case in ("st_acq_task_end_clock_rss", "st_acq_final_bracket_end_clock_rss"):
        running(m, True)
        m.procs[MODEL_MAIN]["rss"] = s.cfg["rss_trip_bytes"] + 1
        if case == "st_acq_task_end_clock_rss":
            within = (m.within("census", 'self.aux_clock(task, "mono_end")'),)
        else:
            within = (m.within("acquire_identity", 'self.aux_clock(raw, "mono_end")'),
                      m.within("census", 'final = self.acquire_identity(pid, "measurement_final_bracket", install_final)'))
        m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", action="raise", within=within)
        step(m, "census_acquisition_before_clock", s.census, ns["Deadline"](10.0))
        step(m, "timing_failure_forbids_scan_resume", s.census, ns["Deadline"](10.0))
    elif case in ("st_acq_accounting_late_return", "st_acq_accounting_observed_clock"):
        dl = ns["Deadline"](1.0)
        if case == "st_acq_accounting_late_return":
            m.clock_rule("check", "now = time.monotonic()", dl.end + 0.01,
                         within=(m.within("accounting", 'dl.check("after accounting")'),))
        else:
            m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", action="raise",
                         within=(m.within("accounting", 'self.aux_clock(event, "mono_observed")'),))
        m.inputs.update(deadline=dl.end, free=m.os.free_value)
        step(m, "accounting_preserves_native_values", s.accounting, dl)
        if case.endswith("_clock"):
            step(m, "timing_failure_forbids_accounting_resume", s.accounting, ns["Deadline"](1.0))
    elif case == "st_acq_reap_mono_clock":
        running(m)
        m.wait_return_mono = MONO + 0.1
        m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", action="raise",
                     within=(m.within("reap_record", 'self.aux_clock(record, "mono_reaped")'),))
        step(m, "destructive_wait_before_reap_clock", s.reap)
        step(m, "consumed_wait_not_repeated", s.reap)
        step(m, "missing_exit_clock_denies_deadline", s.deadline, 1.0)
        step(m, "finalize_sticky_timing_HOLD", ns["finalize"], s)
    else:  # Only st_write_progress_late reaches this fixed branch.
        left, right = m.os.pipe()
        data, progress = b"MODEL returned bytes before clock failure\n", bytearray()
        dl = ns["Deadline"](1.0)
        m.os.write_mode, m.write_cutoff = "late", dl.end
        step(m, "write_progress_before_completion_refusal", ns["write_all"], right, data, dl, progress.extend)
        m.inputs.update(data_hex=data.hex(), progress_hex=bytes(progress).hex(), deadline=dl.end,
                        result_data_hex=bytes(m.os.fds[left]["pipe"]["data"]).hex())
        m.os.close(left)
        m.os.close(right)


def auxiliary_cap_case(m, case, limits):
    s = m.s
    family = case.split("_")[2]
    cap = limits[family]["value"]
    desired = cap + int(suffix_delta(case, 1))
    m.inputs.update(family=family, cap=limits[family], requested_post_count=desired, pre_count=desired - 1)
    if family == "raw":
        m.verbose = False
        for _ in range(desired - 1):
            s.acquire_identity(1, "MODEL_PENDING_PREFILL")
        m.verbose = True
        step(m, "raw_acquisition_count_boundary", s.acquire_identity, 1, "MODEL_PENDING_TARGET")
    else:
        h = helper_prestate(m)
        for _ in range(desired - 1):
            step(m, "clockless_prefill_pass", s.helper_clockless_once, h)
        step(m, "clockless_target_pass", s.helper_clockless_once, h)


def dispatch(case, source_raw, budget):
    if case == "st_clock_cancel_before_target":
        return cancel_before_target(case, source_raw, budget)
    if case.startswith("st_budget_output_"):
        return output_budget(case, source_raw, budget)
    if case.startswith("st_manifest_"):
        return manifest_case(case, source_raw, budget)
    m = setup(case, source_raw, budget, ready=not case.startswith("st_date_"))
    m.inputs = {}
    s, ns = m.s, m.ns
    limits = caps(m)
    m.cap_values = limits
    if case in ("st_cap_final_rss", "st_cap_initial_main", "st_cap_helper_term"):
        return critical_case(case, source_raw, budget, limits)
    if case.startswith("st_complete_"):
        completion_case(m, case)
        return m
    if case.startswith("st_ident_"):
        identity_case(m, case)
        return m
    if case.startswith("st_clock_"):
        clock_case(m, case)
        return m
    if case.startswith("st_acq_") or case == "st_write_progress_late":
        acquisition_case(m, case)
        return m
    if case.startswith(("st_cap_raw_", "st_cap_clockless_")):
        auxiliary_cap_case(m, case, limits)
        return m
    if case.startswith("st_runtime_"):
        running(m)
        age = {"st_runtime_999": 9.99, "st_runtime_1000": 10.0, "st_runtime_1026": 10.26}[case]
        m.clock.mono = MONO + 9.98
        m.wait_return_mono = MONO + age
        m.inputs.update(wait_enter_mono=m.clock.mono, wait_return_mono=m.wait_return_mono,
                        max_wall_s=s.cfg["max_wall_s"], sample_s=s.cfg["sample_s"], mono_spawn=MONO,
                        wait_status=0, native_wait_exercised=False)
        step(m, "reap", s.reap)
    elif case.startswith("st_go_"):
        running(m)
        bound = min(60.0, s.cfg["max_wall_s"] / 2.0)
        m.clock.mono = MONO + bound + suffix_delta(case)
        m.inputs.update(mono_spawn=MONO, max_wall_s=s.cfg["max_wall_s"], sample_s=s.cfg["sample_s"],
                        observed_mono=m.clock.mono, bound=bound)
        step(m, "completion_check_GO", s.completion_check, "GO", ns["Deadline"](30.0))
    elif case.startswith("st_age_"):
        age = 300.0 + suffix_delta(case)
        before = s.clock_observation["mono_before_read"]
        base = s.clock_observation["epoch_date_floor"] - s.authorization["stability_epoch"] + 1.0
        m.clock.mono = before + age - base
        m.inputs.update(requested_age=age, mono=m.clock.mono, observation=dict(s.clock_observation),
                        stability_epoch=s.authorization["stability_epoch"], expiry=s.stability_expiry_mono,
                        max_age=s.cfg["admission"]["stability_max_age_s"])
        step(m, "stability_age", s.stability_age, m.clock.mono)
    elif case.startswith("st_date_"):
        if case == "st_date_future":
            # Actual original date_now future branch; model civil floor is behind pinned model stability floor.
            m.clock.civil_shift = -201.0
            m.inputs.update(receipt_stability_epoch=s.authorization["stability_epoch"],
                            model_epoch_floor=math.floor(m.clock.snapshot_epoch()))
            step(m, "date_now", s.date_now, "admission")
        else:
            value = {"st_date_missing": None, "st_date_malformed": "MODEL_NOT_A_DATE",
                     "st_date_naive": bytes.fromhex("323032332d31312d31345432323a31303a3030").decode()}[case]
            m.inputs["parser_input"] = value
            step(m, "parse_date_epoch", ns["parse_date_epoch"], value)
    elif case.startswith("st_stability_"):
        first = {"expiry": s.stability_expiry_mono, "observation": dict(s.clock_observation)}
        m.clock.mono += 10.0
        m.clock.civil_shift = {"st_stability_rollback": -60.0, "st_stability_refresh": -1.0,
                               "st_stability_tighten": 30.0}[case]
        step(m, "later_date_now", s.date_now, "start")
        second = {"expiry": s.stability_expiry_mono, "observation": dict(s.clock_observation)}
        m.clock.mono = s.stability_expiry_mono + 0.01
        m.inputs.update(first=first, second=second, later_check_mono=m.clock.mono,
                        max_age=s.cfg["admission"]["stability_max_age_s"], stability_epoch=s.authorization["stability_epoch"])
        step(m, "nonrenewing_stability_age", s.stability_age, m.clock.mono)
    elif case.startswith("st_ack_age_"):
        c = s.full_census(ns["Deadline"](10.0))
        m.clock.mono = c["mono_complete"] + 1.0 + suffix_delta(case)
        m.inputs.update(census=c, mono=m.clock.mono, sample_s=s.cfg["sample_s"])
        step(m, "resource_age", s.resource_age, c)
    elif case.startswith("st_retry_"):
        running(m, True)
        m.scan_mode = case.split("_")[2]
        m.top_scans = 0
        m.inputs.update(mode=m.scan_mode, busy_limit=s.cfg["busy_limit"], rss_limit=s.cfg["rss_trip_bytes"],
                        previous_stop=dict(s.stop), transient_unproved_uid=1700000030)
        step(m, "full_census", s.full_census, ns["Deadline"](10.0))
    elif case.startswith("st_abort_"):
        running(m, True)
        dl = ns["Deadline"](10.0)
        if case == "st_abort_identity":
            m.clock_rule("check", "now = time.monotonic()", dl.end + 0.01,
                         occurrence=2, within=(m.within("scan_identities", 'dl.check("census identification")'),))
            step(m, "scan_identities", s.scan_identities, dl)
        else:
            m.procs[700000040] = m.process(700000040)
            m.clock_rule("check", "now = time.monotonic()", dl.end + 0.01,
                         occurrence=3, within=(m.within("census", 'dl.check("census accounting")'),))
            step(m, "census", s.census, dl)
        m.inputs.update(deadline=dl.end, rule=m.clock.rules[-1])
    elif case.startswith("st_cap_bytes_"):
        item = [900000, "identify", "MODEL_EACCES"]
        old = s.history_charge
        s.retain_coverage([item], MONO)
        charge = s.history_charge - old
        s.coverage_history.pop()
        target = limits["bytes"]["value"] + int(suffix_delta(case, 1))
        s.history_charge = target - charge
        m.inputs.update(cap=limits["bytes"], entry={"mono": MONO, "observation": item},
                        charge=charge, precharge=s.history_charge, attempted_charge=target)
        step(m, "retain_coverage", s.retain_coverage, [item], MONO)
    elif case.startswith("st_cap_"):
        count_cap_case(m, case, limits)
    elif case.startswith("st_budget_"):
        family = case.split("_")[2]
        delta = int(suffix_delta(case, 1))
        adm = s.cfg["admission"]
        payload = 100
        a = {"charged_bytes": 1000, "lane_bytes": 1000, "free": 14000000000}
        if family == "reservation":
            a["charged_bytes"] = adm["reservation_bytes"] - payload + delta
        elif family == "free":
            remaining = max(0, adm["reservation_bytes"] - a["charged_bytes"] - payload)
            a["free"] = s.cfg["free_trip_bytes"] + payload + adm["outstanding_reservations_bytes"] + remaining + delta
        elif family == "lane":
            remaining = max(0, adm["reservation_bytes"] - a["charged_bytes"] - payload)
            a["lane_bytes"] = s.cfg["lane_disk_ceiling_bytes"] - payload - adm["lane_outstanding_reservations_bytes"] - remaining + delta
        else:
            raise ModelBoundary("fixed budget family")
        m.inputs.update(family=family, resources=a, payload=payload, admission=dict(adm),
                        free_trip_bytes=s.cfg["free_trip_bytes"], lane_ceiling=s.cfg["lane_disk_ceiling_bytes"], delta=delta)
        m.disclosures.append("reservation_fits predicate isolation with declared model accounting/payload, not a native reservation or physical payload publication; OUTPUT can dominate reservation in final_body.")
        step(m, "reservation_fits", s.reservation_fits, a, payload)
    elif case.startswith("st_cutoff_census_"):
        running(m, True)
        dl = ns["Deadline"](ns["CENSUS_S"])
        rule = m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", dl.end + suffix_delta(case),
                            within=(m.within("census", 'self.aux_clock(measured, "mono_observed")'),))
        m.inputs.update(deadline=dl.end, rule=rule, max_wall_s=s.cfg["max_wall_s"])
        step(m, "census", s.census, dl)
    elif case.startswith("st_cutoff_helper_"):
        start = m.clock.mono
        end = start + s.cfg["helper_budget"]["call_budget_s"]
        rule = m.clock_rule("aux_clock", "value = time.time() if epoch else time.monotonic()", end + suffix_delta(case),
                            within=(m.within("helper_probe", 'self.aux_clock(h, "mono_proof_complete")'),))
        m.inputs.update(call_start=start, deadline=end, rule=rule)
        step(m, "date_now", s.date_now, "start")
    elif case.startswith("st_cutoff_stop_grace_") or case.startswith("st_cutoff_exit_grace_"):
        running(m)
        s.rc, s.exit_mono, s.exit_epoch = 0, MONO, EPOCH
        s.child.update(leader_reaped=True, rc=0, native_wait_result=(MODEL_MAIN, 0), raw_wait_status=0,
                       mono_reaped=MONO, epoch_reaped=EPOCH)
        m.procs.pop(MODEL_MAIN)
        if "stop_grace" in case:
            s.stop = {"reason": "MODEL_STOP", "mono": MONO - 0.1, "epoch": EPOCH - 0.1, "date": None}
        s.streams = {name: {"closed": True, "error": None} for name in ("stdout", "stderr")}
        s.threads = [SimpleNamespace(is_alive=lambda: False), SimpleNamespace(is_alive=lambda: False)]
        cuts = s.cutoffs()
        cut = min(value for _, value in cuts)
        rule = m.clock_rule("clearance", "now = time.monotonic()", cut + suffix_delta(case))
        m.inputs.update(cutoffs=cuts, deadline=cut, rule=rule, settled_streams_and_threads="MODEL_PRESTATE")
        step(m, "clearance", s.clearance)
    elif case.startswith("st_cutoff_finalize_"):
        phase = ns["Deadline"](ns["FINALIZE_S"], s.fit_mono)
        m.clock.mono = phase.end + suffix_delta(case)
        # A fresh declared clock observation isolates finalization phase from the separate stability bound.
        s.clock_observation["mono_before_read"] = m.clock.mono
        s.stability_expiry_mono = m.clock.mono + 99.0
        m.inputs.update(deadline=phase.end, observed_mono=m.clock.mono, seconds=ns["FINALIZE_S"],
                        source_path="completion_check(ACK, actual Deadline(FINALIZE_S, fit_mono))")
        step(m, "completion_check_ACK", s.completion_check, "ACK", phase)
    elif case.startswith("st_write_"):
        left, right = m.os.pipe()
        data = b"GO\nMODEL bounded wire\n"
        dl = ns["Deadline"](1.0)
        m.os.write_mode = case.split("_")[2]
        m.write_cutoff = dl.end
        m.inputs.update(data_hex=data.hex(), bytes=len(data), deadline=dl.end, mode=m.os.write_mode)
        step(m, "write_all", ns["write_all"], right, data, dl)
        m.inputs["result_data_hex"] = bytes(m.os.fds[left]["pipe"]["data"]).hex()
        m.os.close(left)
        m.os.close(right)
    elif case == "st_cancel_pending_after_handled":
        s.cancel_handled = True
        ns["CANCEL"].update(signal=int(signal.SIGTERM), mono=MONO)
        dl = ns["Deadline"](30.0)
        step(m, "handled_cancel_no_new_pending", s.completion_check, "ACK", dl)
        m.signals.pending.add(signal.SIGINT)
        step(m, "new_pending_cancel", s.completion_check, "ACK", dl)
        m.inputs.update(handled_signal=int(signal.SIGTERM), new_pending_signal=int(signal.SIGINT))
    else:
        raise ModelBoundary("case absent from implemented fixed dispatch")
    return m


def exclusive_outcome(runfd, obj, budget):
    raw = canonical(obj)
    if len(raw) > MAX_BYTES - 8192:
        raise Invalid("outcome over output reservation")
    fd = os.open("fixture-outcome.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o444, dir_fd=runfd)
    try:
        view = memoryview(raw)
        while view:
            budget.check()
            count = os.write(fd, view[:65536])
            if count <= 0:
                raise Invalid("zero-progress outcome write")
            view = view[count:]
        os.fsync(fd)
        identity = [os.fstat(fd).st_dev, os.fstat(fd).st_ino]
    finally:
        os.close(fd)
    os.fsync(runfd)
    readback = snapshot(runfd, "fixture-outcome.json", budget)
    if readback["raw"] != raw or readback["inode"] != identity:
        raise Invalid("outcome readback mismatch")
    return facts(readback), identity


def main():
    begin = time.monotonic()
    owner = {"pid": os.getpid(), "pgid": os.getpgrp(), "mono_begin": begin}
    os.write(1, canonical({"kind": "rqls10-matrix-owner-v1", **owner, "scope": SCOPE}))
    native_epoch_begin = time.time()
    budget = NativeBudget(begin)
    if sys.platform != "darwin" or os.path.abspath(__file__) != DRIVER or os.path.realpath(__file__) != DRIVER or \
            len(sys.argv) != 3 or sys.argv[1] not in CASES or not hex64(sys.argv[2]):
        raise Invalid("fixed STATE_ONLY path/platform/CASE_ID APPROVAL_SHA interface")
    case, digest = sys.argv[1:]
    runfd = directory(ROOT + "/" + case)
    try:
        # Refuse an already used root before source AST extraction or model work.
        try:
            os.stat("fixture-outcome.json", dir_fd=runfd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise Invalid("current-run outcome already exists")
        ap, rq, sources, approval, request, spec, binding_epoch = authority(case, digest, runfd, budget)
        # Fresh live-lease proof AFTER every source/spec binding step, immediately before dispatch; otherwise no dispatch.
        validation_epoch = time.time()  # Native raw epoch telemetry for authority only, never a human timestamp.
        if not native_epoch_begin <= binding_epoch <= validation_epoch <= rq["not_after_epoch"] <= validation_epoch + MAX_RUNTIME:
            raise Invalid("expired authority or invalid native clock order before dispatch")
        status, error, m = "RECORDED", None, None
        try:
            m = dispatch(case, sources["supervisor"]["raw"], budget)
            if any(not rule["fired"] for rule in m.clock.rules + m.transitions):
                status, error = "NOT_EXERCISED", utf8_hex("declared original-source boundary not reached")
        except ModelBoundary as failure:
            status = "NOT_EXERCISED"
            error = utf8_hex(repr(failure))
        except BudgetStop as failure:
            status = "HOLD"
            error = utf8_hex(repr(failure))
        except BaseException as failure:
            status = "HOLD"
            error = utf8_hex(repr(failure))
        if m is None:
            partial = getattr(budget, "model", None)
            if partial is not None and partial.s is not None:
                m = partial
        budget.check()
        current_approval = snapshot(runfd, "parent-authorization.json", budget, 1 << 20)
        current_request = snapshot(runfd, "request.json", budget, 1 << 20)
        if facts(current_approval) != facts(approval) or facts(current_request) != facts(request):
            raise Invalid("authority changed during model work")
        final_epoch = time.time()  # Captured ONCE: this exact value is enforced and reported as raw_epoch_end.
        if not validation_epoch <= final_epoch <= ap["not_after_epoch"]:
            status = "HOLD"
            error = utf8_hex("native authority expired or native clock order invalid at final proof")
        owner["mono_end"] = time.monotonic()
        model = None if m is None else {
            "scope": "MODEL_INPUT_NOT_NATIVE", "inputs": safe(m.inputs), "config": safe(m.cfg),
            "virtual_authority": safe(m.virtual_authority), "caps": caps(m), "symbols": m.symbols,
            "clock_rules": safe(m.clock.rules), "metadata_transitions": safe(m.transitions),
            "operations": m.operations, "operation_count": m.calls,
            "operation_trace_sha256": m.op_hash.hexdigest(), "violations": m.violations,
            "steps": safe(m.steps), "final_state": raw_state(m), "disclosures": m.disclosures,
            "checkpoint": safe(m.mark), "stdout": utf8_hex(m.stdout.buffer), "stderr": utf8_hex(m.stderr.buffer),
            "live_model_processes": [safe(m.identity(p)) for p in m.procs.values()],
            "artifacts": {path: {"inode": [771, node.inode], "bytes": node.size, "nlink": node.nlink,
                                  "sha256": hashlib.sha256(node.data).hexdigest(), "data_hex": bytes(node.data).hex(),
                                  "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "artifact_scope": "MODEL_ARTIFACT_NOT_NATIVE"}
                          for path, node in m.os.nodes.items()
                          if any(path.startswith(root + "/") for root in m.cfg["output_roots"]) and not node.directory},
            "open_model_fds": sorted(m.os.fds), "note": "MODEL PID/FD handles, never native ownership claims"}
        outcome = {"kind": "rqls10-guard-matrix-outcome-v1", "case": case, "scope": SCOPE,
                   "bindings": {"approval_sha256": digest, "request_sha256": request["sha256"], "run": rq["run"],
                                "sources": ap["sources"], "hook_set": HOOK_SET, "allocation": rq["allocation"],
                                "negative_control": rq["negative_control"], "model_inputs_sha256": rq["model_inputs_sha256"],
                                "not_after_epoch": rq["not_after_epoch"], "native_config": None},
                   "owner": owner, "observations": [{"scope": "NATIVE_OBSERVATION", "kind": "owner_runtime",
                        "rss_peak_bytes": budget.max_rss, "budget_checks": budget.checks,
                        "raw_epoch_begin": native_epoch_begin, "authority_validation_epoch": validation_epoch,
                        "raw_epoch_end": final_epoch,
                        "runtime_s": owner["mono_end"] - begin}],
                   "source_outcome": {"status": status, "error": error, "selected_driver_status": 0,
                                      "actual_exit": None, "fixture_identity": "MODIFIED_QUALIFICATION_FIXTURE",
                                      "native_supervisor_terminal14_exercised": False},
                   "artifacts": {"approval": {"original": facts(approval), "current": facts(current_approval)},
                                 "request": {"original": facts(request), "current": facts(current_request)},
                                 "sources": {k: facts(v) for k, v in sources.items()}},
                   "unresolved": {"native_coverage": "NOT_EXERCISED", "native_children_created": [],
                                  "native_end_identity_proof": None, "science_acceptance": None, "release": None,
                                  "limits": ["Exact equality/model clocks/API responses are STATE_ONLY, not OS latency or physical cap coverage.",
                                             "No native helper, child, signal, wait, proc ABI, disk accounting, mutation, publication, stdout error or terminal14 is exercised.",
                                             "Count-prestate resets can be jointly unreachable under byte/attempt caps; no state result closes native matrix obligations.",
                                             "Model live processes/FDs are pure Python objects and do not claim native ownership settlement."]},
                   "accounting": {"scope": "MODEL_ONLY", "publication_stage": None, "native_payload": None,
                                  "native_publication_resources": None, "native_ack_resources": None}, "model": model}
        got, created_inode = exclusive_outcome(runfd, outcome, budget)
        # Exact six-key marker; the inode is fstat of the ORIGINAL O_EXCL-created descriptor (origin proof stays J18).
        os.write(1, canonical({"kind": "rqls10-state-outcome-written-v1", "case": case, "scope": SCOPE,
                               "outcome_sha256": got["sha256"], "bytes": got["bytes"], "outcome_inode": created_inode}))
        return 0
    finally:
        os.close(runfd)


if __name__ == "__main__":
    try:
        status = main()
    except BaseException as failure:
        # No model or date text is emitted in human form, even for parsing failures.
        raw = repr(failure).encode("utf-8", "surrogatepass")
        os.write(2, canonical({"kind": "rqls10-state-infrastructure-refusal-v1", "encoding": "UTF8_HEX",
                               "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "hex": raw[:4096].hex()}))
        status = 2
    sys.exit(status)
