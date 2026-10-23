#!/usr/bin/env python3
"""REVIEW CANDIDATE / WRITTEN ONLY / NO GO. Fixed source19 I/O matrix, not a scheduler.

CLI: guard_matrix_io_v1.py CASE_ID PARENT_APPROVAL_SHA256
Request/authority: <MATRIX_ROOT>/<CASE>/request.json, parent-authorization.json.
The independent parent captures actual exit and complete stdout/stderr. Neither
selected_status nor an ACK is an actual-exit observation or release authority.
Source19 is compiled only AFTER exact external authority checks. Its original
terminal AST, including os._exit(14), is executed unchanged. Every overlay below
is fixed by CASE and bound by the approved hook_set; none is production code.
No numerical module, arbitrary command, clock substitution, deletion or mount.
"""
import ast
import errno
import hashlib
import io
import json
import math
import os
import resource
import signal
import stat
import sys
import threading
import time
import types

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
SUP = LANE + "/code/owned_supervisor_v19.py"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
BASE_CHILD = LANE + "/code/guard_qual_child_v12.py"
# Exact child12 body; external parent approval must bind the complete frozen review source set.
BASE_SHA = "e3a8006890a164d36fdacbadc6e63b64c87302ec46149c7f3a6c731e1a3e186b"
TERMINAL_LINES = [2688, 2692]
HELD = LANE + "/code/rqls_fixedb_lm_v7.py"
HELD_SHA = "4a78a7a078b52dd55e4348b2ecac357c95ef8fcea461768f4f05d9809d1edf07"
PATHS = {"supervisor": SUP, "driver": LANE + "/code/guard_matrix_io_v1.py",
         "child": LANE + "/code/guard_matrix_io_child_v1.py",
         "oracle": LANE + "/code/guard_matrix_io_check_v1.py",
         "case_specs": LANE + "/review/rqls10-matrix-io-v1-cases.json",
         "base_child": BASE_CHILD, "held_consumer": HELD}
AUTH = tuple("io_auth_" + action + "_" + phase for phase in ("helper", "main", "go", "ack")
             for action in ("replace", "revoke"))
PUB = tuple("io_pub_" + op + "_" + result for op in ("write", "fsync", "close", "readback", "dirsync")
            for result in ("error", "late")) + ("io_pub_readback_mismatch", "io_pub_short_write")
ACCOUNT = ("io_account_pre_payload", "io_account_pre_b", "io_account_pre_end", "io_account_post_end")
POST = ("io_post_ack_stderr_write", "io_post_ack_stderr_flush", "io_post_ack_stderr_persistent_write",
        "io_post_ack_stderr_persistent_flush")
CHANNEL = ("io_channel_wrong_purpose", "io_channel_wrong_scenario", "io_channel_wrong_target",
           "io_channel_missing_negative", "io_channel_wrong_negative", "io_channel_numeric_boolean",
           "io_channel_missing_schema", "io_channel_extra_schema", "io_channel_malformed",
           "io_channel_preparation_digest", "io_channel_ordinary", "io_channel_certificate_extra")
MUTATION = ("io_mutation_pin_before_manifest", "io_mutation_pin_before_child_open",
            "io_mutation_launch_before_manifest", "io_mutation_launch_before_child_open")
ANCHOR = ("io_root_swap", "io_subtree_swap", "io_different_device")
TYPE_GO = ("io_type_go_cpu_slots_true", "io_type_go_outstanding_false", "io_type_go_lane_outstanding_false")
TYPE_PREP = ("io_type_prep_cpu_slots_true", "io_type_prep_outstanding_false", "io_type_prep_lane_outstanding_false")
NEGATIVE_KEYS = ("io_channel_negative_missing_key", "io_channel_negative_extra_key", "io_channel_negative_false")
EXTRA = ("io_extra_write_short", "io_extra_write_zero", "io_extra_write_error", "io_extra_write_late",
         "io_extra_close_error", "io_extra_close_late", "io_extra_go_age", "io_extra_deadline", "io_extra_expiry") + \
        tuple("io_extra_signal_" + sig + "_" + op for sig in ("term", "int", "hup") for op in ("write", "close"))
METHOD = ANCHOR + tuple(c for c in CHANNEL if c != "io_channel_ordinary") + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS
PREPARATION = MUTATION + tuple(c for c in CHANNEL if c not in ("io_channel_ordinary", "io_channel_certificate_extra")) + TYPE_PREP + NEGATIVE_KEYS + EXTRA
SOURCE_WRITER = LANE + "/code/guard_qual_configs_v12.py"
SOURCE_CHECKER = LANE + "/code/guard_qual_check_v11.py"
CASES = AUTH + PUB + ("io_staged_same_content",) + ANCHOR + ACCOUNT + POST + CHANNEL + MUTATION + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS + EXTRA
CAP, OUTPUT_CAP, RSS_CAP = 1 << 20, 16 << 20, 256 << 20
BEGIN = time.monotonic()
END = BEGIN + 300.0
WORK_END = END - 15.0  # Reserved bounded evidence/reporting time inside the 300 s envelope.
REPORTING = False
TRUNCATED = {"events": 0, "first_operation": None, "retained_bytes": 0}
EVENTS = []
REC_AT_B = None
FINAL_PHASE = None
ENVELOPE_REFUSAL = None
SOURCE = None
STATE = None
REQUEST = None
APPROVAL = None
APPROVED_CFG = None
RUN = None
SELECTED = None
TRUSTED_SHA = None
UNRESOLVED = []
PREREQUISITES = []
ARTIFACT_ROOTS = []
MUTATED = False
ORIGINAL_STDOUT, ORIGINAL_STDERR = sys.stdout, sys.stderr
OUTPUT_LOCK = threading.RLock()
EVENT_LOCK = threading.RLock()
EMITTED = {"stdout": 0, "stderr": 0}
FD_LOCK = threading.RLock()


class FixtureOwnershipHold(RuntimeError):
    """Never impersonates a native errno when the fixture cannot exclude FD reuse."""


def typed_equal(left, right):
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(typed_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def scenario(case):
    return "mutate_pin" if case in MUTATION and "_pin_" in case else "mutate_evidence"


def child_mode(case):
    return "mutation" if case in MUTATION else "channel" if case in EXTRA else "wire"


def check(where):
    global ENVELOPE_REFUSAL
    late = time.monotonic() >= (END if REPORTING else WORK_END)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if late or rss > RSS_CAP:
        if ENVELOPE_REFUSAL is None:
            ENVELOPE_REFUSAL = {"where": where, "deadline_reached": late, "observed_maxrss_bytes": rss}
        raise OSError("FIXTURE_ENVELOPE_REFUSAL " + where)


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def decode(raw):
    def finite(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError("nonfinite number")
        return value
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_float=finite,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("nonfinite constant")))


def packed(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def hex64(value):
    return isinstance(value, str) and len(value) == 64 and all(x in "0123456789abcdef" for x in value)


def integer(value):
    return type(value) is int


def exception(exc):
    # Error strings can contain model dates: never print them as actual dates.
    # Bounded text; utf8_bytes lets the oracle reject a partial text as evidence.
    raw = str(exc).encode("utf-8", "surrogateescape")
    return {"type": type(exc).__name__, "errno": getattr(exc, "errno", None),
            "UTF8_HEX": raw[:16384].hex(), "utf8_bytes": len(raw),
            "text_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE"}


def raw_clock(epoch=False):
    try:
        return time.time() if epoch else time.monotonic()
    except BaseException as exc:
        UNRESOLVED.append({"kind": "fixture_clock_unavailable", "clock": "epoch" if epoch else "mono", "error": exception(exc)})
        return None


def event(operation, scope="NATIVE_OBSERVATION", **fields):
    # Never raises into source paths (cap, size, serialization or envelope); truncation becomes
    # unresolved evidence. Cooperative envelope checks happen only BEFORE native side effects.
    with EVENT_LOCK:
        value = {"seq": len(EVENTS), "operation": operation, "scope": scope, "mono": raw_clock(),
                 "epoch_raw": raw_clock(True), **fields}
        try:
            raw = packed(value)
        except (TypeError, ValueError):
            raw = None
        if raw is None or TRUNCATED["events"] or len(EVENTS) >= 4096 or len(raw) > 256 << 10 or TRUNCATED["retained_bytes"] + len(raw) > 2 << 20:
            TRUNCATED["events"] += 1
            if TRUNCATED["first_operation"] is None:
                TRUNCATED["first_operation"] = operation
        else:
            EVENTS.append(decode(raw))  # Freeze facts before source state extends them.
            TRUNCATED["retained_bytes"] += len(raw)
    return value


def ident(fd):
    value = os.fstat(fd)
    return [value.st_dev, value.st_ino]


def directory(path):
    if not isinstance(path, str) or not path.startswith("/") or os.path.normpath(path) != path:
        raise ValueError("noncanonical directory")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.split("/")[1:]:
            check("directory component")
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def read_regular(path, cap=CAP):
    parent = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or not 0 <= before.st_size <= cap:
            raise ValueError("not bounded regular")
        data = bytearray()
        while len(data) < before.st_size:
            check("regular read")
            block = os.read(fd, min(65536, before.st_size - len(data)))
            if not block:
                raise OSError("short regular read")
            data.extend(block)
        tail = os.read(fd, 1)
        after = os.fstat(fd)
        if tail or (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns) != \
                (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
            raise OSError("regular read changed")
        named = os.stat(os.path.basename(path), dir_fd=parent, follow_symlinks=False)
        if (named.st_dev, named.st_ino, named.st_size, named.st_mtime_ns, named.st_ctime_ns) != \
                (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
            raise OSError("original regular pathname replaced during read")
        facts = {"path": path, "inode": [before.st_dev, before.st_ino], "bytes": len(data),
                 "sha256": sha(data), "nlink": before.st_nlink, "mode": stat.S_IMODE(before.st_mode),
                 "birth_epoch_raw": before.st_birthtime, "mtime_ns_raw": before.st_mtime_ns}
        return facts, bytes(data)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def full_write(fd, data):
    view = memoryview(data)
    counts = []
    old = os.get_blocking(fd)
    os.set_blocking(fd, False)
    try:
        while view:
            check("fixture full write")
            try:
                count = os.write(fd, view[:65536])
            except BlockingIOError:
                time.sleep(0.002)
                continue
            if count <= 0:
                raise OSError("zero fixture write")
            counts.append(count)
            view = view[count:]
    except BaseException as exc:
        exc.fixture_native_write_counts = list(counts)
        raise
    finally:
        os.set_blocking(fd, old)
    return counts


def output_room(additional=0, stream=None):
    """Conservative distinct-inode RUN bound, including outgoing parent captures.

    4MiB remains for bounded child evidence and later parent/oracle records.
    This is a cooperative fixture limit, not a reservation-release accountant.
    """
    if RUN is None:
        return
    seen, entries, capture_sizes = set(), [0], {"stdout": 0, "stderr": 0}
    def walk(path, depth=0):
        if depth > 16:
            raise OSError("FIXTURE_OUTPUT_DEPTH")
        fd = directory(path)
        total = 0
        try:
            for name in os.listdir(fd):
                check("bounded entire current-run output census")
                entries[0] += 1
                if entries[0] > 4096:
                    raise OSError("FIXTURE_OUTPUT_ENTRY_CAP")
                value = os.stat(name, dir_fd=fd, follow_symlinks=False)
                child = path + "/" + name
                if stat.S_ISDIR(value.st_mode):
                    total += walk(child, depth + 1)
                elif stat.S_ISREG(value.st_mode):
                    key = (value.st_dev, value.st_ino)
                    if key in seen:
                        continue
                    seen.add(key)
                    if child in (RUN + "/driver.stdout", RUN + "/driver.stderr"):
                        capture_sizes[name.split(".")[-1]] = value.st_size
                    else:
                        total += value.st_size
                else:
                    raise OSError("FIXTURE_OUTPUT_UNDECLARED_NONREGULAR")
        finally:
            os.close(fd)
        return total
    total = walk(RUN)
    for name in EMITTED:
        total += max(capture_sizes[name], EMITTED[name] + (additional if stream == name else 0))
    if total + (additional if stream is None else 0) > 12 << 20:
        raise OSError("FIXTURE_OUTPUT_12M_PLUS_4M_PARENT_CHILD_RESERVE")


def exclusive(path, data):
    fd = None
    parent = directory(os.path.dirname(path))
    try:
        fd = os.open(os.path.basename(path), os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        created = ident(fd)
        with OUTPUT_LOCK:
            output_room(len(data))
            full_write(fd, data)
        os.fsync(fd)
        os.lseek(fd, 0, os.SEEK_SET)
        got = bytearray()
        while len(got) < len(data):
            check("exclusive readback")
            part = os.read(fd, min(65536, len(data) - len(got)))
            if not part:
                raise OSError("exclusive short readback")
            got.extend(part)
        if os.read(fd, 1) or bytes(got) != data or ident(fd) != created:
            raise OSError("exclusive readback mismatch")
        facts = {"path": path, "inode": created, "sha256": sha(got), "bytes": len(got), "nlink": os.fstat(fd).st_nlink}
        os.close(fd)
        fd = None
        os.fsync(parent)
        return facts
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def anchors(case, run):
    charge = run + "/fixture-root" if case in ANCHOR else run
    return {"run": run, "charge": charge, "out": charge + "/out", "tmp": charge + "/tmp", "scratch": run + "/scratch"}


def created_match(wanted, actual):
    keys = {"path", "inode", "sha256", "bytes", "nlink", "creation_ordinal"}
    if not isinstance(wanted, dict) or set(wanted) != keys or not integer(wanted["creation_ordinal"]) or \
            wanted["creation_ordinal"] < 0 or not integer(wanted["bytes"]) or wanted["bytes"] < 0 or \
            not integer(wanted["nlink"]) or wanted["nlink"] != 1 or not hex64(wanted["sha256"]) or \
            not isinstance(wanted["inode"], list) or len(wanted["inode"]) != 2 or \
            any(not integer(x) or x < 0 for x in wanted["inode"]):
        raise ValueError("exact original created-descriptor schema")
    if not all(typed_equal(wanted[k], actual[k]) for k in ("path", "inode", "sha256", "bytes", "nlink")):
        raise ValueError("original created inode/content/link continuity")


def authorize(case, trusted):
    global REQUEST, APPROVAL, RUN, END, WORK_END, ARTIFACT_ROOTS, TRUSTED_SHA
    if case not in CASES or not hex64(trusted):
        raise ValueError("fixed CASE and external SHA required")
    RUN = ROOT + "/" + case
    af, ar = read_regular(RUN + "/parent-authorization.json")
    if af["sha256"] != trusted:
        raise ValueError("external parent authorization SHA mismatch")
    approval = decode(ar)
    rf, rr = read_regular(RUN + "/request.json")
    request = decode(rr)
    akeys = {"kind", "case", "scope", "request_sha256", "sources", "anchors", "allocation", "not_after_epoch",
             "negative_control", "hook_set", "config", "go", "go_original", "stability", "preparation", "mutable",
             "parameters", "limits", "different_device", "created_facts", "request_created"}
    rkeys = akeys - {"request_sha256", "request_created"}
    if set(approval) != akeys or set(request) != rkeys:
        raise ValueError("authority/request exact schema")
    if approval["kind"] != "rqls10-guard-matrix-invocation-v1" or request["kind"] != "rqls10-guard-matrix-request-v1" or \
            approval["request_sha256"] != rf["sha256"] or request["case"] != case:
        raise ValueError("authority kind/case/request")
    for key in rkeys - {"kind"}:
        if not typed_equal(request[key], approval[key]):
            raise ValueError("authority field mismatch: " + key)
    created_match(approval["request_created"], rf)
    if af["nlink"] != 1:
        raise ValueError("parent approval must be single-link original exclusive creation")
    if request["scope"] != "MODIFIED_QUALIFICATION_FIXTURE" or request["hook_set"] != [case]:
        raise ValueError("fixture scope/fixed hook set")
    if request["negative_control"] is not (case != "io_channel_ordinary"):
        raise ValueError("literal negative designation")
    limits = {"max_wall_s": 300, "rss_bytes": RSS_CAP, "output_bytes": OUTPUT_CAP, "busy_ceiling": 2, "max_loops": 2}
    if request["limits"] != limits or any(type(request["limits"][k]) is not int for k in limits):
        raise ValueError("fixed resource envelope")
    allocation = request["allocation"]
    if set(allocation) != {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} or \
            any(not integer(v) or v < 0 for v in allocation.values()) or not 1 <= allocation["cpu_slots"] <= 2 or \
            allocation["bytes"] != 20 << 20:
        raise ValueError("serialized allocation")
    expiry = request["not_after_epoch"]
    if isinstance(expiry, bool) or not isinstance(expiry, (int, float)) or not math.isfinite(expiry) or \
            not time.time() < expiry <= time.time() + 300:
        raise ValueError("current finite invocation authority")
    END = min(END, time.monotonic() + expiry - time.time())
    WORK_END = END - 15.0
    if set(request["sources"]) != set(PATHS):
        raise ValueError("source set")
    for role, path in PATHS.items():
        binding = request["sources"][role]
        if set(binding) != {"path", "sha256"} or binding["path"] != path or not hex64(binding["sha256"]):
            raise ValueError("source pin schema")
        facts, raw = read_regular(path, 2 << 20)
        if facts["sha256"] != binding["sha256"]:
            raise ValueError("actual source digest mismatch: " + role)
        expected = {"supervisor": SUP_SHA, "base_child": BASE_SHA, "held_consumer": HELD_SHA}.get(role)
        if expected is not None and facts["sha256"] != expected:
            raise ValueError("immutable source mismatch")
    paths = anchors(case, RUN)
    if set(request["anchors"]) != set(paths):
        raise ValueError("anchor set")
    for role, path in paths.items():
        binding = request["anchors"][role]
        fd = directory(path)
        try:
            if not typed_equal(binding, {"path": path, "inode": ident(fd)}):
                raise ValueError("original current-run anchor mismatch")
        finally:
            os.close(fd)
    for role in ("out", "tmp", "scratch"):
        fd = directory(paths[role])
        try:
            allowed_initial = ["replacement.bin"] if role == "scratch" and case in MUTATION else []
            if sorted(os.listdir(fd)) != allowed_initial:
                raise ValueError("not an empty/fresh explicitly owned fixture root: " + role)
        finally:
            os.close(fd)
    if case in ANCHOR:
        fd = directory(paths["charge"])
        try:
            if sorted(os.listdir(fd)) != ["out", "tmp"]:
                raise ValueError("isolated fixture-root contains undeclared original objects")
        finally:
            os.close(fd)
    for name in ("fixture-outcome.json", "GO.archived.json", "child-ready.json", "child-open-release.json"):
        if os.path.lexists(RUN + "/" + name):
            raise FileExistsError("current-run one-use output already exists")
    output_room()
    for key, name in (("config", "config.json"), ("go", "GO.json"), ("go_original", "GO.original.json"),
                      ("stability", "stability.json"), ("preparation", "preparation.json")):
        binding = request[key]
        if binding is None and key == "preparation" and case not in PREPARATION:
            continue
        if not isinstance(binding, dict) or set(binding) != {"path", "sha256"} or binding["path"] != RUN + "/" + name:
            raise ValueError("fixed input path: " + key)
        facts, raw = read_regular(binding["path"])
        if facts["sha256"] != binding["sha256"]:
            raise ValueError("input digest: " + key)
    if request["go"]["sha256"] != request["go_original"]["sha256"]:
        raise ValueError("test GO copy differs before entry")
    # Explicit mutable names, never parent approval or old/frozen evidence.
    allowed = [RUN + "/GO.json", RUN + "/GO.archived.json", RUN + "/scratch/replacement.bin",
               RUN + "/scratch/target.original", RUN + "/scratch/staged.original", RUN + "/scratch/root.original",
               RUN + "/scratch/out.original", RUN + "/child-ready.json", RUN + "/child-open-release.json",
               RUN + "/pinned-scratch.txt", paths["charge"], paths["out"], paths["out"] + "/launch.json",
               paths["out"] + "/settlement.json.staged", paths["out"] + "/receipt.json",
               RUN + "/scratch/stderr-attempt.bin", RUN + "/scratch/pre-b-record.json"]
    if request["mutable"] != allowed:
        raise ValueError("fixed current-run mutation allowlist")
    created = request["created_facts"]
    names = {"GO": "GO.json", "go_original": "GO.original.json", "config": "config.json",
             "stability": "stability.json", "preparation": "preparation.json",
             "pin": "pinned-scratch.txt", "replacement": "scratch/replacement.bin"}
    if not isinstance(created, dict) or set(created) != set(names):
        raise ValueError("all approved declaration/config/preparation creation facts required")
    ordinals = []
    for role, name in names.items():
        required = role not in ("preparation", "pin", "replacement") or \
                   role == "preparation" and case in PREPARATION or \
                   role == "pin" and case in MUTATION and "_pin_" in case or role == "replacement" and case in MUTATION
        if not required:
            if created[role] is not None:
                raise ValueError("undeclared created object: " + role)
            continue
        facts, raw = read_regular(RUN + "/" + name)
        created_match(created[role], facts)
        ordinals.append(created[role]["creation_ordinal"])
        binding_role = "go" if role == "GO" else role
        if binding_role in request and not typed_equal(request[binding_role], {"path": facts["path"], "sha256": facts["sha256"]}):
            raise ValueError("input binding/created-descriptor mismatch")
    if len(ordinals) != len(set(ordinals)) or any(n >= approval["request_created"]["creation_ordinal"] for n in ordinals):
        raise ValueError("original exclusive creation order")
    if typed_equal(created["GO"]["inode"], created["go_original"]["inode"]):
        raise ValueError("GO copy cannot alias immutable original")
    params = request["parameters"]
    if set(params) != {"io_deadline_s", "max_flush_delay_s", "child_life_s"} or \
            any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in params.values()) or \
            not 0.02 <= params["io_deadline_s"] <= 1 or not 0.02 <= params["max_flush_delay_s"] <= 10 or \
            not 1 <= params["child_life_s"] <= 60:
        raise ValueError("fixed bounded parameters")
    cfg = decode(read_regular(request["config"]["path"])[1])
    if cfg.get("lane") != LANE or cfg.get("lane_disk_root") != paths["charge"] or cfg.get("output_roots") != [paths["out"]] or \
            cfg.get("env", {}).get("TMPDIR") != paths["tmp"] or not typed_equal(cfg.get("cpu_slots"), allocation["cpu_slots"]) or \
            cfg.get("busy_limit", 3) > 2 or cfg.get("max_wall_s", 301) > 60 or cfg.get("settle_s", 301) > 30 or \
            cfg.get("max_chunk_seconds", 301) > 300 or cfg.get("rss_trip_bytes", RSS_CAP + 1) > RSS_CAP:
        raise ValueError("native config isolation/resources")
    if cfg.get("lane_roots") != [LANE] or cfg.get("fault_injection") != {}:
        raise ValueError("fixed readonly lane membership and no undeclared original-source injection")
    adm = cfg.get("admission", {})
    if adm.get("go_path") != RUN + "/GO.json" or adm.get("stability_receipt_path") != RUN + "/stability.json" or \
            any(not typed_equal(adm.get(k), allocation[q]) for k, q in (("reservation_bytes", "bytes"),
                ("outstanding_reservations_bytes", "outstanding_reservations_bytes"),
                ("lane_outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"))):
        raise ValueError("exact config allocation and authority paths")
    expected_mode = child_mode(case)
    argv = cfg.get("argv")
    if not isinstance(argv, list) or len(argv) != 4 or argv[1:] != [PATHS["child"], expected_mode, case] or \
            not os.path.isabs(argv[0]) or os.path.realpath(argv[0]) != os.path.realpath(sys.executable):
        raise ValueError("only fixed child mode/interpreter allowed")
    if cfg.get("env") != {"PATH": "/usr/bin:/bin", "TMPDIR": paths["tmp"], "PYTHONDONTWRITEBYTECODE": "1"}:
        raise ValueError("fixed child environment; external SHA travels only in the declared spawn overlay")
    for key, name in (("stdout", "child.stdout"), ("stderr", "child.stderr"), ("samples", "samples.jsonl"),
                      ("launch_record", "launch.json"), ("receipt", "receipt.json"), ("settlement_record", "settlement.json")):
        if cfg.get(key) != paths["out"] + "/" + name:
            raise ValueError("fixed source output names")
    if cfg.get("outputs") != [{"path": paths["out"] + "/child-result.json", "required": True}] or \
            cfg.get("pins") != ([{"path": RUN + "/pinned-scratch.txt", "sha256": request["created_facts"]["pin"]["sha256"]}]
                              if case in MUTATION and "_pin_" in case else []):
        raise ValueError("fixed output/pin set")
    if any(not integer(cfg.get(k)) or not 1 <= cfg[k] <= CAP for k in ("stdout_cap_bytes", "stderr_cap_bytes", "samples_cap_bytes")):
        raise ValueError("bounded capture caps")
    if cfg.get("helper_budget", {}).get("max_calls", 0) < 3 or cfg.get("busy_limit") not in (1, 2):
        raise ValueError("three original date calls and busy limit one/two required")
    if case in TYPE_GO + TYPE_PREP:
        field = "cpu_slots" if "cpu_slots" in case else "lane_outstanding_reservations_bytes" if "lane_outstanding" in case else "outstanding_reservations_bytes"
        if not typed_equal(allocation[field], 1 if field == "cpu_slots" else 0):
            raise ValueError("typed alias control requires original integer one/zero")
    if case in MUTATION and case.endswith("before_child_open") and (cfg["sample_s"] < 2 or cfg["max_wall_s"] < 10):
        raise ValueError("fixed barrier controls need actual sample_s>=2/max_wall_s>=10; never an age override")
    if case == "io_extra_go_age" and (cfg["max_wall_s"] != 10 or cfg["sample_s"] != 10 or params["child_life_s"] < 15):
        raise ValueError("fixed real age case requires wall10/sample10/childlife>=15")
    if case == "io_extra_deadline" and (cfg["max_wall_s"] != 40 or cfg["settle_s"] > 5 or cfg["sample_s"] != 10 or params["child_life_s"] < 50):
        raise ValueError("original IO_S30 crossing requires wall40/settle<=5/sample10/childlife>=50")
    if case == "io_extra_expiry" and cfg["sample_s"] != 10:
        raise ValueError("real extra expiry requires unchanged source sample10 freshness window")
    # External digest travels in one fixed child-only spawn-env overlay,
    # never the hashed config/request/approval: no digest cycle.
    TRUSTED_SHA = trusted
    APPROVAL, REQUEST = approval, request
    ARTIFACT_ROOTS = ([paths["charge"], paths["scratch"]] if case in ANCHOR else
                      [paths["out"], paths["tmp"], paths["scratch"]])
    declared_design(cfg, request, case)
    event("authority_checked", approval_sha256=trusted, request_sha256=rf["sha256"],
          original_run_inode=request["anchors"]["run"]["inode"], sources=request["sources"],
          limits=limits, allocation=allocation)
    return cfg


def declared_design(cfg, request, case):
    """Closed defects; no caller-selected schema, target, code, command or hook."""
    if cfg.get("item") != case or cfg.get("purpose") != ("ordinary" if case == "io_channel_wrong_purpose" else "guard-qualification"):
        raise ValueError("fixed item/purpose design")
    name = scenario(case)
    uses_channel = case in PREPARATION
    expected = {}
    if uses_channel:
        expected = {"kind": "qualification-creation-v1", "scenario": name,
                    "preparation_path": RUN + "/preparation.json", "preparation_sha256": request["preparation"]["sha256"],
                    "target_path": RUN + ("/pinned-scratch.txt" if name == "mutate_pin" else "/out/launch.json")}
        if case == "io_channel_wrong_scenario":
            expected["scenario"] = "fixed-invalid-scenario"
        elif case == "io_channel_wrong_target":
            expected["target_path"] = RUN + "/fixed-forbidden-target.txt"
        elif case == "io_channel_missing_schema":
            del expected["kind"]
        elif case == "io_channel_extra_schema":
            expected["extra"] = True
        elif case == "io_channel_malformed":
            expected = []
        elif case == "io_channel_preparation_digest":
            expected["preparation_sha256"] = "0" * 64
    if not typed_equal(cfg.get("creation_channel"), expected):
        raise ValueError("one exact declared channel defect")
    original_go = decode(read_regular(request["go_original"]["path"])[1])
    keys = {"decision", "item", "configs", "not_after_epoch", "stability_receipt_sha256"}
    negative = None
    if case != "io_channel_ordinary":
        keys.add("qualification_negative")
        negative = {"scenario": name, "kind": "mutation", "creation_channel": True} if uses_channel else \
                   {"scenario": case, "kind": "matrix_io", "creation_channel": False}
    if case == "io_channel_missing_negative":
        keys.remove("qualification_negative")
        negative = None
    elif case == "io_channel_wrong_negative":
        negative["scenario"] = "fixed-wrong-scenario"
    elif case == "io_channel_numeric_boolean":
        negative["creation_channel"] = 1
    elif case == "io_channel_negative_missing_key":
        del negative["kind"]
    elif case == "io_channel_negative_extra_key":
        negative["extra"] = True
    elif case == "io_channel_negative_false":
        negative["creation_channel"] = False
    if not isinstance(original_go, dict) or set(original_go) != keys or original_go.get("decision") != "GO" or \
            original_go.get("item") != case or original_go.get("stability_receipt_sha256") != request["stability"]["sha256"]:
        raise ValueError("fixed exact original GO schema")
    if negative is not None and not typed_equal(original_go["qualification_negative"], negative):
        raise ValueError("exact negative GO keys/scalar types")
    bound = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
    bound.update({k: cfg["admission"][k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
    if case in TYPE_GO:
        field = "cpu_slots" if "cpu_slots" in case else "lane_outstanding_reservations_bytes" if "lane_outstanding" in case else "outstanding_reservations_bytes"
        bound[field] = field == "cpu_slots"
    if not typed_equal(original_go["configs"], {request["config"]["sha256"]: bound}):
        raise ValueError("fixed original GO binding or its one typed defect")
    expiry = original_go["not_after_epoch"]
    if isinstance(expiry, bool) or not isinstance(expiry, (int, float)) or not math.isfinite(expiry) or \
            not time.time() < expiry <= request["not_after_epoch"]:
        raise ValueError("original GO current real expiry")
    if case in MUTATION and request["allocation"]["cpu_slots"] != 1:
        raise ValueError("original child12 mutation allocation is one slot")
    if uses_channel:
        prep = decode(read_regular(request["preparation"]["path"])[1])
        source_pins = {"supervisor": {"path": SUP, "sha256": SUP_SHA}, "child": {"path": BASE_CHILD, "sha256": BASE_SHA}}
        for role, path in (("writer", SOURCE_WRITER), ("checker", SOURCE_CHECKER)):
            source_pins[role] = {"path": path, "sha256": read_regular(path, 2 << 20)[0]["sha256"]}
        python = cfg["argv"][0]
        if not python.endswith("/Resources/Python.app/Contents/MacOS/Python") or os.path.realpath(python) != python:
            raise ValueError("actual canonical Python.app required")
        pin = request["created_facts"]["pin"]
        fixture = None if name != "mutate_pin" else {k: pin[k] for k in ("path", "inode", "sha256", "bytes", "nlink")}
        allocation = dict(request["allocation"])
        if case in TYPE_PREP:
            field = "cpu_slots" if "cpu_slots" in case else "lane_outstanding_reservations_bytes" if "lane_outstanding" in case else "outstanding_reservations_bytes"
            allocation[field] = field == "cpu_slots"
        expected_prep = {"kind": "qualification-creation-preparation-v1", "scenario": name,
                         "run": request["anchors"]["run"], "output_root": request["anchors"]["out"],
                         "fixture": fixture, "source_pins": source_pins,
                         "python": {"path": python, "sha256": read_regular(python, 64 << 20)[0]["sha256"]},
                         "allocation": allocation, "negative_control": True}
        if not typed_equal(prep, expected_prep):
            raise ValueError("exact original preparation, current actual source bytes and its declared typed defect")


def archive_and_create(path, archive, data):
    if archive not in REQUEST["mutable"] or not path.startswith(RUN + "/"):
        raise ValueError("undeclared mutation")
    original, original_bytes = read_regular(path, OUTPUT_CAP)
    if os.path.lexists(archive):
        raise FileExistsError("archive already exists")
    os.rename(path, archive)
    created = exclusive(path, data)
    archived, check_bytes = read_regular(archive, OUTPUT_CAP)
    if archived["inode"] != original["inode"] or check_bytes != original_bytes:
        raise OSError("archived original changed")
    event("archive_replace", original=original, archive=archived, replacement=created,
          original_bytes_unchanged=True, declaration=REQUEST["mutable"])
    return original, created


def mutate_go(phase):
    global MUTATED
    if MUTATED:
        return
    path = RUN + "/GO.json"
    facts, raw = read_regular(path)
    wanted = REQUEST["created_facts"]["GO"]
    if any(facts[k] != wanted[k] for k in ("inode", "sha256", "bytes", "nlink")):
        raise OSError("test GO no longer original created copy")
    value = decode(raw)
    if "_revoke_" in REQUEST["case"]:
        value["decision"] = "HOLD"
    else:
        value["fixture_binding_revision"] = "fixed-replacement-not-parent-approval"
    with OUTPUT_LOCK:
        archive_and_create(path, RUN + "/GO.archived.json", packed(value))
    MUTATED = True
    event("authorization_copy_mutated", phase=phase, action="revoke" if "_revoke_" in REQUEST["case"] else "replace",
          preceding_preparation_io=True, immutable_parent_approval_untouched=True)


def replacement_target(s):
    return RUN + "/pinned-scratch.txt" if "_pin_" in REQUEST["case"] else s.cfg["launch_record"]


def replace_target(s, point):
    global MUTATED
    if MUTATED:
        return
    target = replacement_target(s)
    original, raw = read_regular(target)
    expected_inode = REQUEST["created_facts"]["pin"]["inode"] if "_pin_" in REQUEST["case"] else list(s.created[target])
    expected_sha = REQUEST["created_facts"]["pin"]["sha256"] if "_pin_" in REQUEST["case"] else s.rec["launch_record_sha256"]
    if original["inode"] != expected_inode or original["sha256"] != expected_sha:
        raise OSError("not original source/created descriptor target")
    replacement = REQUEST["created_facts"]["replacement"]
    path = RUN + "/scratch/replacement.bin"
    before, before_bytes = read_regular(path)
    if before_bytes or any(not typed_equal(before[k], replacement[k]) for k in ("inode", "sha256", "bytes", "nlink")) or \
            ("_pin_" in REQUEST["case"] and replacement["creation_ordinal"] >= REQUEST["created_facts"]["pin"]["creation_ordinal"]):
        raise ValueError("approved older empty current-run replacement required")
    parent = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDWR | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
        if ident(fd) != replacement["inode"] or os.fstat(fd).st_size != 0:
            raise OSError("replacement descriptor changed")
        output_room(len(raw))
        full_write(fd, raw)
        os.fsync(fd)
        value = os.fstat(fd)
        created_fd_facts = {"inode": [value.st_dev, value.st_ino], "bytes": value.st_size, "nlink": value.st_nlink,
                            "sha256": sha(raw), "original_empty_inode": replacement["inode"]}
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)
    archive = RUN + "/scratch/target.original"
    if os.path.lexists(archive):
        raise FileExistsError("target archive exists")
    os.rename(target, archive)
    os.rename(path, target)
    after, after_raw = read_regular(target)
    archived, archived_raw = read_regular(archive)
    if after_raw != raw or archived_raw != raw or archived["inode"] != expected_inode or after["inode"] != replacement["inode"]:
        raise OSError("same-content original/replacement continuity")
    MUTATED = True
    event("target_replaced_before_mutation", point=point, original=original, archive=archived,
          replacement=after, created_descriptor=created_fd_facts, expected_original_inode=expected_inode,
          expected_original_sha256=expected_sha, approved_empty_creation=replacement)


def wait_child_ready():
    until = min(WORK_END - 1, time.monotonic() + REQUEST["parameters"]["child_life_s"] - 0.5,
                STATE.mono_spawn + STATE.cfg["max_wall_s"] - max(1.0, STATE.cfg["sample_s"] + 0.05))
    while time.monotonic() < until:
        try:
            facts, raw = read_regular(RUN + "/child-ready.json")
            value = decode(raw)
        except (OSError, ValueError):
            time.sleep(0.002)  # Absent or still being exclusively written: bounded retry.
            continue
        if set(value) != {"kind", "case", "pid", "pgid", "mono", "manifest_sha256"} or \
                value["kind"] != "rqls10-matrix-child-open-ready-v1" or value["case"] != REQUEST["case"]:
            raise ValueError("child readiness schema")
        if STATE is None or value["pid"] != STATE.pid or value["pgid"] != STATE.group:
            raise ValueError("child readiness incarnation")
        event("native_child_ready", artifact=facts, value=value)
        return value
    PREREQUISITES.append("child pre-open readiness not observed inside its bounded life")
    event("child_ready_not_observed", until_mono=until)
    return None


def safe_hook(label, function, *args, **kwargs):
    """A fixture action failure is retained evidence, never injected into source control flow."""
    try:
        return function(*args, **kwargs)
    except Exception as exc:
        UNRESOLVED.append({"kind": "fixture_hook_failed", "hook": label, "error": exception(exc)})
        event("fixture_hook_failed", hook=label, error=exception(exc))
        return None


def wait_past(target, clock):
    """Real-clock wait that never raises into source code and stops at the cooperative envelope."""
    while clock() <= target:
        remaining = (END if REPORTING else WORK_END) - time.monotonic()
        if remaining <= 0 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_CAP:
            return False
        time.sleep(max(0.0001, min(0.002, remaining, target - clock())))
    return True


def replace_locked(s, point):
    with OUTPUT_LOCK:
        replace_target(s, point)


def replace_staged(path):
    raw = read_regular(path)[1]
    with OUTPUT_LOCK:
        archive_and_create(path, RUN + "/scratch/staged.original", raw)


def mutate_receipt_byte(path):
    original, raw = read_regular(path, OUTPUT_CAP)
    if not raw:
        raise ValueError("empty receipt cannot carry the fixed same-length byte change")
    parent = directory(os.path.dirname(path))
    target = None
    try:
        target = os.open(os.path.basename(path), os.O_RDWR | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
        if ident(target) != original["inode"]:
            raise OSError("receipt replaced before the declared byte change")
        byte = bytes([raw[0] ^ 1])
        check("before declared receipt byte change")
        count = os.pwrite(target, byte, 0)
        os.fsync(target)
        event("native_readback_bytes_mutated", original=original, native_pwrite_return=count, offset=0,
              replacement_byte_hex=byte.hex(), target_inode=ident(target))
    finally:
        if target is not None:
            os.close(target)
        os.close(parent)


def open_barrier_replacement():
    ready = wait_child_ready()
    if ready is None:
        return
    # A failed replacement raises here, so the child is never released onto the original target.
    replace_locked(STATE, "between_delivery_and_child_open")
    released = exclusive(RUN + "/child-open-release.json", packed({"kind": "rqls10-fixture-open-barrier-v1",
                         "case": REQUEST["case"], "child_pid": STATE.pid,
                         "manifest_sha256": ready["manifest_sha256"]}))
    event("fixture_open_barrier_released", artifact=released,
          authority="barrier only, never GO/approval/admission/release")


class SourceOS:
    """Fixed namespace overlay; real native returns precede fallible completion checks.

    An EBADF stimulus retains OUTPUT_LOCK then FD_LOCK until the source's last
    close of that number. Source sink threads never allocate except through this
    locked proxy/output census. Every source operation on the closed number
    independently observes fstat EBADF first. Reuse means HOLD, never a forged errno.
    """
    def __init__(self):
        self.fds, self.fired = {}, set()
        self.spawn_role = self.publication = self.dirsync_deadline = None
        self.account_context = self.go_deadline = self.stimulus = None
        self.extra_in_write = False

    def __getattr__(self, name):
        return getattr(os, name)

    def call(self, operation, function, args, kwargs, guard=True, **facts):
        if guard:
            check("before native " + operation)
        before = time.monotonic()
        try:
            result = function(*args, **kwargs)
        except BaseException as exc:
            event("native_" + operation, mono_before=before, mono_after=raw_clock(), error=exception(exc), **facts)
            raise
        event("native_" + operation, mono_before=before, mono_after=raw_clock(),
              result=result if isinstance(result, (int, str, type(None))) else None, **facts)
        return result

    def path(self, path, dir_fd=None):
        if not isinstance(path, str):
            return None
        if os.path.isabs(path):
            return os.path.normpath(path)
        base = self.fds.get(dir_fd, {}).get("path") if dir_fd is not None else os.getcwd()
        return os.path.normpath(os.path.join(base, path)) if base else None

    def interesting(self, fd, path):
        if self.stimulus is not None and fd == self.stimulus["fd"]:
            return True
        if STATE is None:
            return False
        return STATE.child is not None and fd == STATE.child.get("stdin_fd") or \
               path in (STATE.cfg["receipt"], STATE.cfg["settlement_record"], STATE.cfg["settlement_record"] + ".staged",
                        STATE.cfg["launch_record"]) or path in STATE.root_fds

    def remember(self, fd, path):
        try:
            value = os.fstat(fd)
        except OSError as exc:
            UNRESOLVED.append({"kind": "fixture_fd_bookkeeping_failed", "fd": fd, "error": exception(exc)})
            return None
        self.fds[fd] = {"path": path, "inode": [value.st_dev, value.st_ino], "mode": value.st_mode}
        return value

    def open(self, path, flags, mode=0o777, *, dir_fd=None):
        check("before native open")
        with FD_LOCK:
            full = self.path(path, dir_fd)
            fd = os.open(path, flags, mode, dir_fd=dir_fd)
            value = self.remember(fd, full)
            immutable = {REQUEST[role]["path"]: role for role in ("config", "go_original", "stability", "preparation") if REQUEST[role] is not None}
            role = immutable.get(full)
            if role is not None:
                wanted = REQUEST["created_facts"][role]
                if value is None or not typed_equal([value.st_dev, value.st_ino], wanted["inode"]) or value.st_size != wanted["bytes"] or value.st_nlink != 1:
                    os.close(fd)
                    self.fds.pop(fd, None)
                    raise FixtureOwnershipHold("approved original input inode changed before source open")
        if flags & os.O_CREAT and value is not None:
            event("source_created_descriptor", fd=fd, path=full, inode=[value.st_dev, value.st_ino],
                  bytes=value.st_size, nlink=value.st_nlink, flags=flags)
        return fd

    def fdopen(self, fd, *args, **kwargs):
        stream = os.fdopen(fd, *args, **kwargs)
        self.fds.pop(fd, None)
        return stream

    def pipe(self):
        check("before native pipe")
        before = time.monotonic()
        with FD_LOCK:
            result = os.pipe()
            for fd in result:
                self.remember(fd, None)
        event("native_pipe", mono_before=before, mono_after=raw_clock(), fds=list(result), spawn_role=self.spawn_role)
        phase = REQUEST["case"].rsplit("_", 1)[1]
        if REQUEST["case"] in AUTH and phase == ("main" if self.spawn_role == "child" else self.spawn_role):
            safe_hook("authorization_copy_" + phase, mutate_go, phase)
        return result

    def selected(self, kind, operation, path):
        if STATE is None or REQUEST["case"] != "io_pub_" + operation + "_" + kind or (kind, operation) in self.fired:
            return False
        if operation == "dirsync":
            return path in STATE.root_fds and STATE.publication_resources is not None and STATE.ack_resources is None
        return path == STATE.cfg["receipt"]

    def sabotage(self, fd, operation, path):
        case = REQUEST["case"]
        extra = case == "io_extra_write_error" and operation == "write" and self.extra_in_write or \
                case == "io_extra_close_error" and operation == "close" and self.go_deadline is not None and STATE.child is not None and fd == STATE.child.get("stdin_fd")
        key = ("error", operation)
        if key in self.fired or not (extra or self.selected("error", operation, path)):
            return
        allowed = {threading.main_thread(), *STATE.threads}
        live = threading.enumerate()
        if any(t not in allowed for t in live):
            PREREQUISITES.append("unregistered live thread prevents FD-reuse exclusion for " + operation)
            return
        OUTPUT_LOCK.acquire()
        FD_LOCK.acquire()
        facts = dict(self.fds.get(fd, {}))
        try:
            self.call("owned_fd_close_stimulus", os.close, (fd,), {}, fd=fd, path=path, original=facts)
        except BaseException:
            FD_LOCK.release()
            OUTPUT_LOCK.release()
            raise
        self.fired.add(key)
        self.fds.pop(fd, None)
        self.stimulus = {"fd": fd, "closed": False, "closes_left": 2 if case == "io_extra_close_error" else 0 if operation == "dirsync" else 1}
        event("descriptor_fault_stimulus", operation_target=operation, fd=fd, original=facts,
              live_threads=[t.name for t in live], allocation_lock_held=True,
              source_close_observations_required=self.stimulus["closes_left"],
              limit="native owned-descriptor EBADF, not media/durability failure")

    def unallocated(self, fd, operation):
        s = self.stimulus
        if s is None or s["closed"] or fd != s["fd"]:
            return
        try:
            value = os.fstat(fd)
        except OSError as exc:
            if exc.errno != errno.EBADF:
                raise
            event("closed_number_unallocated_before_source_call", fd=fd, operation_target=operation, native_errno=exc.errno)
            return
        UNRESOLVED.append({"kind": "closed_number_reused", "fd": fd, "inode": [value.st_dev, value.st_ino]})
        raise FixtureOwnershipHold("closed source descriptor number was reused")

    def end_window(self, reason):
        s = self.stimulus
        if s is None or s["closed"]:
            return
        s["closed"] = True
        if reason != "all_expected_native_calls_completed":
            UNRESOLVED.append({"kind": "descriptor_window_incomplete", "reason": reason, "fd": s["fd"]})
        event("descriptor_fault_window_end", fd=s["fd"], reason=reason, closes_left=s["closes_left"])
        FD_LOCK.release()
        OUTPUT_LOCK.release()

    def after_native(self, fd, operation):
        s = self.stimulus
        if s is None or s["closed"] or s["fd"] != fd:
            return
        if operation == "close":
            s["closes_left"] -= 1
        if s["closes_left"] == 0:
            self.end_window("all_expected_native_calls_completed")

    def arm_late(self, operation, path):
        if not self.selected("late", operation, path):
            return False
        self.fired.add(("late", operation))
        if operation == "dirsync":
            self.publication = self.dirsync_deadline
        if self.publication is None:
            UNRESOLVED.append({"kind": "fixture_hook_failed", "hook": "late_" + operation})
            return False
        self.publication.end = min(self.publication.end, time.monotonic() + REQUEST["parameters"]["io_deadline_s"], WORK_END - 0.1)
        event("late_boundary_armed", "API_RESPONSE_INJECTION", operation_target=operation, path=path, deadline_mono=self.publication.end)
        return True

    def delayed(self, operation, before, after, armed):
        if not armed:
            return
        start, dl = time.monotonic(), self.publication
        crossed = start < dl.end and wait_past(dl.end + 0.01, time.monotonic)
        if not crossed:
            PREREQUISITES.append("declared " + operation + " crossing not observed")
        event("declared_response_delay" if crossed else "response_delay_boundary_missed", "API_RESPONSE_INJECTION",
              operation_target=operation, native_before=before, native_after=after, injection_start=start,
              injection_end=time.monotonic(), deadline_mono=dl.end,
              limit="real native return; wrapper delay is not native syscall-latency coverage")

    def write(self, fd, data):
        check("before native write")
        info = dict(self.fds.get(fd, {}))
        path, length = info.get("path"), len(data)
        case = REQUEST["case"]
        short = (case == "io_pub_short_write" and STATE is not None and path == STATE.cfg["receipt"] or
                 case == "io_extra_write_short" and self.extra_in_write) and "short" not in self.fired
        passed = data[:max(1, length // 2)] if short else data
        if self.extra_in_write and case == "io_extra_write_zero" and "zero" not in self.fired:
            self.fired.add("zero")
            event("extra_zero_response", "API_RESPONSE_INJECTION", caller_bytes=length, result=0,
                  native_call_made=False, reason="explicit API zero-response control, not a native OS return")
            return 0
        with OUTPUT_LOCK:
            if stat.S_ISREG(info.get("mode", 0)):
                output_room(len(passed))
            self.sabotage(fd, "write", path)
            armed = self.arm_late("write", path)
            self.unallocated(fd, "write")
            before = time.monotonic()
            if self.interesting(fd, path):
                result = self.call("write", os.write, (fd, passed), {}, guard=False, fd=fd, path=path,
                                   caller_bytes=length, native_argument_bytes=len(passed), data_sha256=sha(passed),
                                   extra_line=self.extra_in_write)
            else:
                result = os.write(fd, passed)
            after = raw_clock()
        if short:
            self.fired.add("short")
            event("short_write_response", "API_RESPONSE_INJECTION", caller_bytes=length,
                  native_argument_bytes=len(passed), native_return=result, extra_line=self.extra_in_write)
        if self.extra_in_write and case in ("io_extra_write_late", "io_extra_deadline") and "extra_late" not in self.fired:
            self.fired.add("extra_late")
            if case == "io_extra_deadline":
                start, target = time.monotonic(), self.go_deadline.end
                reached = start < target < WORK_END - 0.1 and wait_past(target + 0.01, time.monotonic)
                if not reached:
                    PREREQUISITES.append("original unchanged IO_S30 extra-write deadline crossing not exercised")
                event("accounting_late_response" if reached else "accounting_late_boundary_missed", "API_RESPONSE_INJECTION",
                      stage="extra_write", native_before=before, native_after=after, injection_start=start,
                      deadline_mono=target, original_deadline_mono=target, injection_end=time.monotonic(),
                      deadline_clamped=False)
            else:
                safe_hook("extra_write_return_delay", late_stage, self.go_deadline, "extra_write", native_before=before, native_after=after)
        safe_hook("publication_write_return_delay", self.delayed, "write", before, after, armed)
        return result

    def fsync(self, fd):
        check("before native fsync")
        info = dict(self.fds.get(fd, {}))
        path, isdir = info.get("path"), stat.S_ISDIR(info.get("mode", 0))
        operation = "dirsync" if isdir and STATE is not None and path in STATE.root_fds else "fsync"
        self.sabotage(fd, operation, path)
        armed = self.arm_late(operation, path)
        self.unallocated(fd, operation)
        before = time.monotonic()
        try:
            result = self.call("fsync", os.fsync, (fd,), {}, guard=False, fd=fd, path=path, directory=isdir)
        finally:
            self.after_native(fd, "fsync")
        safe_hook("publication_fsync_return_delay", self.delayed, operation, before, raw_clock(), armed)
        return result

    def close(self, fd):
        info = dict(self.fds.get(fd, {}))
        path = info.get("path")
        stdin = STATE is not None and STATE.child is not None and fd == STATE.child.get("stdin_fd")
        if stdin and self.go_deadline is not None and REQUEST["case"].startswith("io_extra_signal_") and REQUEST["case"].endswith("_close") and "extra_signal" not in self.fired:
            self.fired.add("extra_signal")
            extra_signal("close")
        self.sabotage(fd, "close", path)
        armed = self.arm_late("close", path)
        self.unallocated(fd, "close")
        before = time.monotonic()
        try:
            result = self.call("close", os.close, (fd,), {}, guard=False, fd=fd, path=path) if self.interesting(fd, path) else os.close(fd)
        finally:
            self.fds.pop(fd, None)
            self.after_native(fd, "close")
        after = raw_clock()
        if STATE is not None and REQUEST["case"] == "io_pub_readback_mismatch" and path == STATE.cfg["receipt"] and "mismatch" not in self.fired:
            self.fired.add("mismatch")
            safe_hook("readback_bytes_mutation", mutate_receipt_byte, path)
        if stdin and self.go_deadline is not None and REQUEST["case"] == "io_extra_close_late" and "extra_close_late" not in self.fired:
            self.fired.add("extra_close_late")
            safe_hook("extra_close_return_delay", late_stage, self.go_deadline, "extra_close", native_before=before, native_after=after)
        safe_hook("publication_close_return_delay", self.delayed, "close", before, after, armed)
        return result

    def read(self, fd, count):
        path = self.fds.get(fd, {}).get("path")
        receipt = STATE is not None and path == STATE.cfg["receipt"]
        if receipt:
            check("before native receipt read")
            self.sabotage(fd, "readback", path)
        armed = self.arm_late("readback", path) if receipt else False
        self.unallocated(fd, "readback")
        before = time.monotonic()
        try:
            result = os.read(fd, count)
        except BaseException as exc:
            if receipt:
                event("native_read", fd=fd, path=path, requested=count, mono_before=before, mono_after=raw_clock(), error=exception(exc))
            raise
        after = raw_clock()
        if receipt:
            event("native_read", fd=fd, path=path, requested=count, returned=len(result), bytes_sha256=sha(result), mono_before=before, mono_after=after)
            safe_hook("publication_readback_return_delay", self.delayed, "readback", before, after, armed)
        return result

    def fstatvfs(self, fd):
        check("before native fstatvfs")
        before = time.monotonic()
        value = os.fstatvfs(fd)
        facts = {"f_bavail": value.f_bavail, "f_frsize": value.f_frsize, "free": value.f_bavail * value.f_frsize}
        if STATE is not None:
            STATE.last_native_free = dict(facts)  # Original native acquisition survives even optional wrapper timing failure.
        after = raw_clock()  # A failed optional clock never erases or replaces the native statvfs return.
        context = self.account_context
        event("native_fstatvfs", fd=fd, mono_before=before, mono_after=after, raw=facts,
              phase=None if STATE is None else STATE.phase, accounting_stage=None if context is None else context[1])
        if context is not None and REQUEST["case"] == "io_account_" + str(context[1]):
            safe_hook("accounting_native_return_delay", late_stage, context[0], context[1], native_before=before, native_after=after, raw_free=facts)
        return value

    def link(self, src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True):
        path = self.path(src, src_dir_fd)
        if REQUEST["case"] == "io_staged_same_content" and "staged" not in self.fired:
            self.fired.add("staged")
            safe_hook("staged_same_content_replacement", replace_staged, path)
        return self.call("link", os.link, (src, dst), {"src_dir_fd": src_dir_fd, "dst_dir_fd": dst_dir_fd,
                         "follow_symlinks": follow_symlinks}, src=path, dst=self.path(dst, dst_dir_fd))

    def posix_spawn(self, path, argv, env, **kwargs):
        if self.spawn_role == "helper":
            if argv != ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"]:
                raise ValueError("helper is only original /bin/date")
        elif self.spawn_role == "child":
            if argv != STATE.cfg["argv"]:
                raise ValueError("fixed child argv mismatch")
            env = dict(env, RQLS_MATRIX_APPROVAL_SHA256=TRUSTED_SHA)
        else:
            raise ValueError("unregistered source spawn role")
        check("before native posix_spawn")
        return os.posix_spawn(path, argv, env, **kwargs)


def source_load():
    global SOURCE
    raw = read_regular(SUP, 2 << 20)[1]
    if sha(raw) != SUP_SHA:
        raise ValueError("source changed after authority")
    tree = ast.parse(raw, filename=SUP)
    terminal = tree.body[-1]
    if not isinstance(terminal, ast.If) or [terminal.lineno, terminal.end_lineno] != TERMINAL_LINES:
        raise ValueError("fixed original source19 terminal AST shape")
    env = {"__file__": SUP, "__name__": "__qualified_original_source19__"}
    exec(compile(ast.Module(body=tree.body[:-1], type_ignores=[]), SUP, "exec"), env)
    SOURCE = env
    proxy = SourceOS()
    env["os"] = proxy
    event("source_loaded", "MODIFIED_QUALIFICATION_FIXTURE", source_sha256=SUP_SHA,
          wrapper_sha256=REQUEST["sources"]["driver"]["sha256"], config_sha256=REQUEST["config"]["sha256"],
          hook_set=REQUEST["hook_set"], terminal_lines=[terminal.lineno, terminal.end_lineno],
          source_mode="full immutable module minus terminal, followed by unchanged original terminal AST")
    return env, proxy, terminal


def late_stage(dl, stage, **native):
    """Delay a fixed API return; the original source performs its own check.

    Accounting delays are inside fstatvfs return, before source19 creates its
    accounting event. Source19 therefore honestly records returned=false.
    """
    if dl is None:
        UNRESOLVED.append({"kind": "fixture_hook_failed", "hook": "missing_original_deadline", "stage": stage})
        return
    previous = dl.end
    dl.end = min(previous, time.monotonic() + REQUEST["parameters"]["io_deadline_s"], WORK_END - 0.1)
    start = time.monotonic()
    crossed = start < dl.end and wait_past(dl.end + 0.01, time.monotonic)
    if not crossed:
        PREREQUISITES.append("declared real response crossing not exercised: " + stage)
    event("accounting_late_response" if crossed else "accounting_late_boundary_missed", "API_RESPONSE_INJECTION",
          stage=stage, injection_start=start, deadline_mono=dl.end, original_deadline_mono=previous,
          injection_end=time.monotonic(), **native,
          limit="native result retained; delayed wrapper return, not native syscall latency")


def accounting_snapshot():
    fields = ("publication_payload_bytes", "publication_resources", "ack_resources", "last_accounting_observation",
              "accounting_observations", "min_free_witness", "min_free", "last_native_free")
    if STATE is None:
        return {k: [] if k == "accounting_observations" else None for k in fields}
    return {k: getattr(STATE, k) for k in fields}


def extra_signal(boundary):
    name = REQUEST["case"].split("_")[3]
    sig = {"term": signal.SIGTERM, "int": signal.SIGINT, "hup": signal.SIGHUP}[name]
    start = time.monotonic()
    before = SOURCE["identify"](os.getpid())
    again = SOURCE["identify"](os.getpid())
    mask = signal.pthread_sigmask(signal.SIG_BLOCK, set())
    if SOURCE["fingerprint"](before) != SOURCE["fingerprint"](again) or sig not in mask or before["pid"] != os.getpid():
        PREREQUISITES.append("exact self incarnation/protected mask not established at extra " + boundary)
        return
    native_before = time.monotonic()
    os.kill(os.getpid(), sig)
    native_after = raw_clock()
    pending = sorted(int(x) for x in signal.sigpending())
    event("extra_native_signal", "NATIVE_SIGNAL_AT_PROTECTED_SOURCE_API_BOUNDARY", boundary=boundary, signum=int(sig),
          identity_before=before, identity_checked=again, self_pid=os.getpid(), self_pgid=os.getpgrp(),
          mono_check_begin=start, mono_before=native_before, mono_after=native_after,
          blocked_mask=sorted(int(x) for x in mask), pending=pending, native_syscall_overlap_claim=False)


def install_hooks(env, proxy):
    cls = env["Supervisor"]
    init = cls.__init__
    def initial(self, cfg, path, digest):
        global STATE
        if path != REQUEST["config"]["path"] or digest != REQUEST["config"]["sha256"] or not typed_equal(cfg, APPROVED_CFG):
            raise FixtureOwnershipHold("source config differs from exact externally approved original bytes/schema")
        init(self, cfg, path, digest)
        STATE = self
        event("supervisor_instance", source_self_sha256=self.self_sha, config_sha256=self.config_sha)
    cls.__init__ = initial
    original_spawn = env["spawn_registered"]
    def spawn(s, argv, e, role, dl, required_s):
        proxy.spawn_role = role
        before = time.monotonic()
        try:
            record = original_spawn(s, argv, e, role, dl, required_s)
            pgid, error = None, None
            try:
                pgid = os.getpgid(record["pid"])
            except OSError as exc:
                error = exception(exc)
            event("native_spawn_registered", pid=record["pid"], native_pgid=pgid, pgid_error=error, role=role,
                  mono_before=before, mono_after=raw_clock(), source_ledger_registered=record in s.keep,
                  argv=argv, child_external_sha_overlay=TRUSTED_SHA if role == "child" else None,
                  mono_pid_registered=record.get("mono_pid_registered"))
            return record
        finally:
            proxy.spawn_role = None
    env["spawn_registered"] = spawn
    original_auth = cls.authorization_io
    def auth(self, dl):
        event("final_binding_read_begin", phase=self.phase, inside_helper=self.in_helper, after_mutation=MUTATED)
        try:
            value = original_auth(self, dl)
        except BaseException as exc:
            event("final_binding_read_exception", phase=self.phase, inside_helper=self.in_helper,
                  after_mutation=MUTATED, error=exception(exc))
            raise
        event("final_binding_read_return", phase=self.phase, inside_helper=self.in_helper,
              after_mutation=MUTATED, authorization=value)
        return value
    cls.authorization_io = auth
    original_commit = cls.time_commit
    def commit(self, phase, required_s=0):
        value = original_commit(self, phase, required_s)
        event("source_commit_return", phase=phase, after_mutation=MUTATED, value=value)
        return value
    cls.time_commit = commit
    original_pub = env["publish"]
    def pub(fd, name, data, dl):
        target, previous = proxy.path(name, fd), proxy.publication
        if STATE is not None and target == STATE.cfg["receipt"]:
            proxy.publication = dl
        if STATE is not None and target == STATE.cfg["settlement_record"] + ".staged":
            proxy.dirsync_deadline = dl
        try:
            value = original_pub(fd, name, data, dl)
            roles = {} if STATE is None else {STATE.cfg["launch_record"]: "launch", STATE.cfg["receipt"]: "receipt",
                                               STATE.cfg["settlement_record"] + ".staged": "staged"}
            if target in roles:
                event("original_" + roles[target] + "_publish_return", path=target, sha256=value[0], inode=list(value[1]), bytes=len(data))
            return value
        finally:
            proxy.publication = previous
    env["publish"] = pub
    original_account = cls.accounting
    def accounting(self, dl, lane=True):
        global REC_AT_B
        stage = None
        if self.phase == "FINAL":
            stage = "pre_payload" if self.publication_payload_bytes is None else "pre_b" if self.publication_resources is None else "pre_end" if self.ack_resources is None else None
        if REQUEST["case"] == "io_account_pre_b" and stage == "pre_b":
            # Capture exactly the record which source19 just serialized, BEFORE b.
            raw = packed(self.rec)
            REC_AT_B = raw if len(raw) <= 3 << 20 else {"truncated_bytes": len(raw), "sha256": sha(raw)}
        prior, proxy.account_context = proxy.account_context, (dl, stage)
        try:
            value = original_account(self, dl, lane)
        except BaseException as exc:
            event("actual_accounting_exception", stage=stage, error=exception(exc),
                  observation=self.last_accounting_observation, accounting=accounting_snapshot())
            raise
        finally:
            proxy.account_context = prior
        event("actual_accounting_return", stage=stage, resources=value,
              last_accounting_observation=self.last_accounting_observation)
        if REQUEST["case"] in AUTH and REQUEST["case"].endswith("_go") and self.phase == "PRE_GO" and self.pid is not None and self.rec.get("pre_go_census") is not None:
            safe_hook("authorization_copy_go", mutate_go, "go")
        return value
    cls.accounting = accounting
    original_census = cls.full_census
    def full_census(self, dl):
        value = original_census(self, dl)
        if self.phase == "FINAL" and self.ack_resources is not None:
            if REQUEST["case"] in AUTH and REQUEST["case"].endswith("_ack"):
                safe_hook("authorization_copy_ack", mutate_go, "ack")
            if REQUEST["case"] == "io_account_post_end":
                event("post_end_accounting_state", accounting=accounting_snapshot(),
                      census_complete=value["complete"], census_mono_complete=value["mono_complete"])
                late_stage(FINAL_PHASE, "post_end")
        return value
    cls.full_census = full_census
    original_final = env["final_body"]
    def final(s, phase):
        global FINAL_PHASE
        FINAL_PHASE = phase
        return original_final(s, phase)
    env["final_body"] = final
    original_manifest = cls.creation_manifest
    def manifest(self, dl):
        if REQUEST["case"] in MUTATION and REQUEST["case"].endswith("before_manifest"):
            safe_hook("before_manifest_preparation", replace_locked, self, "before_manifest_preparation")
        try:
            value = original_manifest(self, dl)
        except BaseException as exc:
            event("original_manifest_exception", error=exception(exc), after_replacement=MUTATED)
            raise
        event("original_manifest_return", bytes=len(value), sha256=sha(value), raw_hex=value.hex(),
              source_scope="original source19 creation_manifest")
        return value
    cls.creation_manifest = manifest
    original_completion = cls.completion_check
    def completion(self, phase, dl):
        before = time.monotonic()
        try:
            value = original_completion(self, phase, dl)
        except BaseException as exc:
            event("original_completion_exception", phase=phase, error=exception(exc),
                  mono_before=before, mono_after=raw_clock(), go_completion=self.rec.get("go_delivery_completion"))
            raise
        event("original_completion_return", phase=phase, mono_before=before, mono_after=raw_clock(),
              go_completion=self.rec.get("go_delivery_completion"))
        return value
    cls.completion_check = completion
    original_observe = env["observe"]
    def observe(s):
        if REQUEST["case"] in MUTATION and REQUEST["case"].endswith("before_child_open") and not MUTATED and "barrier" not in proxy.fired:
            proxy.fired.add("barrier")
            if s.rec.get("go_delivered") is True and "POST_SPAWN_FAILURE" not in s.failure_keys:
                # AFTER original GO completion AND freshness checks; never stall the source GO window.
                event("barrier_after_verified_go_completion", completion=s.rec.get("go_delivery_completion"),
                      pre_go_census_mono=s.rec["pre_go_census"]["mono_complete"], sample_s=s.cfg["sample_s"])
                safe_hook("between_delivery_and_child_open", open_barrier_replacement)
            else:
                PREREQUISITES.append("original GO completion/freshness not reached before child-open barrier")
        return original_observe(s)
    env["observe"] = observe
    original_write = env["write_all"]
    def write_all(fd, data, dl, on_progress=None):
        extra = REQUEST["case"] in EXTRA and STATE is not None and STATE.child is not None and fd == STATE.child.get("stdin_fd") and \
                sha(data) == STATE.rec.get("go_creation_manifest_sha256")
        if not extra:
            return original_write(fd, data, dl, on_progress)
        proxy.go_deadline, proxy.extra_in_write = dl, True
        before = time.monotonic()
        event("extra_line_write_begin", raw_hex=bytes(data).hex(), bytes=len(data), sha256=sha(data), fd=fd,
              deadline_mono=dl.end, pre_go_census_mono=STATE.rec["pre_go_census"]["mono_complete"],
              mono_spawn=STATE.mono_spawn, age_bound=min(60.0, STATE.cfg["max_wall_s"] / 2))
        try:
            if REQUEST["case"].startswith("io_extra_signal_") and REQUEST["case"].endswith("_write"):
                proxy.fired.add("extra_signal")
                extra_signal("write")
            value = original_write(fd, data, dl, on_progress)
            if REQUEST["case"] in ("io_extra_go_age", "io_extra_expiry"):
                target = STATE.mono_spawn + min(60.0, STATE.cfg["max_wall_s"] / 2) if REQUEST["case"] == "io_extra_go_age" else STATE.authorization["not_after_epoch"]
                clock = time.monotonic if REQUEST["case"] == "io_extra_go_age" else time.time
                begin_value, start = clock(), time.monotonic()
                maximum = 6.0 if REQUEST["case"] == "io_extra_go_age" else REQUEST["parameters"]["max_flush_delay_s"]
                reached = begin_value < target <= begin_value + maximum and wait_past(target + 0.01, clock)
                if not reached:
                    PREREQUISITES.append("extra-line real age/expiry crossing not exercised")
                event("extra_real_crossing" if reached else "extra_real_crossing_missed", "API_RESPONSE_INJECTION",
                      cutoff="GO_AGE" if REQUEST["case"] == "io_extra_go_age" else "AUTHORIZATION_EXPIRY",
                      cutoff_value_raw=target, clock_begin_raw=begin_value, clock_end_raw=clock(),
                      injection_start=start, injection_end=time.monotonic(), original_go_deadline=dl.end)
            event("extra_line_write_return", mono_before=before, mono_after=raw_clock(), bytes=len(data), sha256=sha(data))
            return value
        except BaseException as exc:
            event("extra_line_write_exception", mono_before=before, mono_after=raw_clock(), error=exception(exc))
            raise
        finally:
            proxy.extra_in_write = False
    env["write_all"] = write_all


class BoundedStdout:
    def __init__(self, stream, name="stdout"):
        self.stream, self.bytes, self.name = stream, 0, name
        self.delayed = False
    def __getattr__(self, name):
        return getattr(self.stream, name)
    def write(self, text):
        raw = text.encode("utf-8")
        self.bytes += len(raw)
        if self.bytes > OUTPUT_CAP - 4096:
            raise OSError("STANDARD_STREAM_CAP")
        before = time.monotonic()
        with OUTPUT_LOCK:
            output_room(len(raw), self.name)
            try:
                native_counts = full_write(self.stream.fileno(), raw)
            except BaseException as exc:
                counts = getattr(exc, "fixture_native_write_counts", [])
                EMITTED[self.name] += sum(counts)
                UNRESOLVED.append({"kind": "standard_stream_incomplete", "stream": self.name, "requested_bytes": len(raw),
                                   "actual_native_bytes": sum(counts), "error": exception(exc)})
                event("source_" + self.name + "_partial_write", caller_bytes=len(raw), native_write_counts=counts,
                      bytes_written=sum(counts), error=exception(exc), mono_before=before, mono_after=raw_clock())
                raise
            EMITTED[self.name] += sum(native_counts)
        event("source_" + self.name + "_write", caller_bytes=len(raw), text_sha256=sha(raw), returned=len(text),
              native_write_counts=native_counts, mono_before=before, mono_after=raw_clock(),
              ack_started=bool(STATE and STATE.ack_output_started))
        return len(text)
    def flush(self):
        # Writes bypass the TextIOWrapper buffer, so this native flush is a bounded no-op that never
        # raises an envelope error at CPython shutdown (which could otherwise manufacture120).
        before = time.monotonic()
        result = self.stream.flush()
        after = raw_clock()
        if self.name == "stdout" and REQUEST["case"] in POST and STATE is not None and STATE.ack_output_started and \
                not self.delayed:
            self.delayed = True
            expiry = STATE.authorization["not_after_epoch"]
            start_epoch, start = time.time(), time.monotonic()
            maximum = REQUEST["parameters"]["max_flush_delay_s"]
            crossed = start_epoch < expiry <= start_epoch + maximum and wait_past(expiry + 0.01, time.time)
            if not crossed:
                PREREQUISITES.append("real approved GO expiry not crossed within max_flush_delay_s during ACK flush")
                event("ack_flush_boundary_missed", expiry_epoch_raw=expiry, start_epoch_raw=start_epoch,
                      end_epoch_raw=time.time(), max_delay_s=maximum)
            else:
                event("ack_flush_real_expiry_crossing", "NATIVE_CLOCK_DECLARED_RESPONSE_DELAY",
                      native_flush_before=before, native_flush_after=after, injection_start=start,
                      injection_start_epoch_raw=start_epoch, injection_end=time.monotonic(),
                      injection_end_epoch_raw=time.time(), approved_expiry_epoch_raw=expiry,
                      limit="real stdout bytes already written; fixture delayed this return, never a fake clock")
        return result


class NativeStderr:
    """The first native EPIPE is real. Plain cases then use a working native fd2;
    persistent cases keep the broken pipe and unchanged buffered bytes until
    the original terminal. Probes are explicit fixture work, not shutdown calls.
    """
    encoding, errors, closed = "utf-8", "strict", False
    def __init__(self, case):
        self.case, self.pending, self.attempts, self.faults = case, bytearray(), 0, 0
        rd, self.fd = os.pipe()
        event("stderr_owned_pipe", fds=[rd, self.fd], inode=ident(self.fd))
        os.close(rd)
        event("stderr_native_reader_closed", writer_fd=self.fd, errno_expected=errno.EPIPE)
    def fileno(self):
        return self.fd
    def isatty(self):
        return False
    def attempt(self, label):
        self.attempts += 1
        data, before = bytes(self.pending), time.monotonic()
        armed = bool(STATE and STATE.ack_output_started)
        broken = armed and ("persistent" in self.case or self.faults == 0)
        target = self.fd if broken else ORIGINAL_STDERR.fileno()
        try:
            if broken:
                counts = [os.write(target, data)]
            else:
                with OUTPUT_LOCK:
                    output_room(len(data), "stderr")
                    counts = full_write(target, data)
                    EMITTED["stderr"] += sum(counts)
        except BaseException as exc:
            completed = getattr(exc, "fixture_native_write_counts", []) if not broken else []
            if completed:
                EMITTED["stderr"] += sum(completed)
                del self.pending[:sum(completed)]
                event("stderr_partial_native_delivery", label=label, native_write_counts=completed,
                      bytes_delivered=sum(completed), pending_after_bytes=len(self.pending),
                      pending_after_sha256=sha(self.pending), semantic_scope="INCOMPLETE_ACTUAL_PARENT_STDERR_DELIVERY")
            if broken and isinstance(exc, OSError) and exc.errno == errno.EPIPE:
                self.faults += 1
            event("stderr_native_error", label=label, attempt=self.attempts, fd=target, broken_fixture=broken,
                  mono_before=before, mono_after=raw_clock(), error=exception(exc),
                  pending_bytes=len(self.pending), pending_sha256=sha(self.pending), native_argument_bytes=len(data))
            if "persistent" not in self.case and self.faults == 1:
                event("stderr_one_shot_fault_consumed", next_sink="unchanged actual parent-captured fd2", broken_fd_retained=self.fd)
            raise
        event("stderr_native_return", label=label, attempt=self.attempts, returned=sum(counts), fd=target,
              mono_before=before, mono_after=raw_clock(), pending_bytes=len(self.pending),
              data_sha256=sha(data), native_write_counts=counts, working_parent_sink=not broken)
        del self.pending[:sum(counts)]
        return sum(counts)
    def write(self, text):
        raw = text.encode("utf-8")
        if len(self.pending) + len(raw) > OUTPUT_CAP:
            raise OSError("STDERR_BUFFER_CAP")
        self.pending.extend(raw)
        event("stderr_buffered_write", caller_bytes=len(raw), text_sha256=sha(raw), pending_bytes=len(self.pending), source_attempt=True)
        if self.case.endswith("write"):
            self.attempt("source_write")
        return len(text)
    def flush(self):
        if self.pending:
            self.attempt("source_or_interpreter_flush")
    def persistent_probes(self):
        if not self.pending or self.faults == 0:
            return
        labels = ["FIXTURE_POST_MAIN_PROBE_0", "FIXTURE_POST_MAIN_PROBE_1"] if "persistent" in self.case else ["FIXTURE_ONE_SHOT_RECOVERY_PROBE"]
        for label in labels:
            try:
                self.attempt(label)
            except OSError:
                pass
    def retain_until_terminal(self):
        event("stderr_owned_writer_retained_until_original_terminal", fd=self.fd, native_inode=ident(self.fd),
              pending_bytes=len(self.pending), pending_sha256=sha(self.pending), stream_closed=self.closed,
              owner_pid=os.getpid(), persistent="persistent" in self.case,
              closure="actual native process exit closes owned FD; no preclose/restore masks shutdown")
        if self.pending:
            attempted = exclusive(RUN + "/scratch/stderr-attempt.bin", bytes(self.pending))
            event("attempted_stderr_artifact", artifact=attempted,
                  semantic_scope="ACTUAL_SOURCE_ATTEMPTED_BYTES_NOT_DELIVERED_STDERR_CAPTURE")


def source_state():
    if STATE is None:
        return None
    value = {"phase": STATE.phase, "rec": STATE.rec, "reconciliation": STATE.reconciliation_evidence(),
             "created": {p: list(i) for p, i in STATE.created.items()}, "pid": STATE.pid, "group": STATE.group,
             "rc": STATE.rc, "identity": STATE.ident, "failures": STATE.failures,
             "failure_codes": sorted(STATE.failure_keys), "trips": STATE.trips,
             "ack_output_started": STATE.ack_output_started, "go_delivered": STATE.rec.get("go_delivered"),
             "accounting": accounting_snapshot(), "evidence_truncated": False}
    raw = packed(value)
    if len(raw) > 3 << 20:
        # Never silently truncate a record and use it as complete evidence.
        value = {"phase": STATE.phase, "pid": STATE.pid, "group": STATE.group, "rc": STATE.rc,
                 "failure_codes": sorted(STATE.failure_keys), "evidence_truncated": True,
                 "original_bytes": len(raw), "original_sha256": sha(raw)}
        UNRESOLVED.append({"kind": "source_state_truncated", "original_bytes": len(raw), "original_sha256": sha(raw)})
    return value


def method_fixture(cfg):
    case = REQUEST["case"]
    env = SOURCE
    result = {"mode": "ORIGINAL_METHOD_ONLY", "method_return": None, "exception": None,
              "original_main_called": False}
    if case == "io_channel_certificate_extra":
        raw = read_regular(HELD, 2 << 20)[1]
        tree = ast.parse(raw, filename=HELD)
        matches = [node for node in tree.body if isinstance(node, ast.If) and node.lineno == 84 and node.end_lineno == 85]
        if len(matches) != 1:
            raise ValueError("held parser exact AST pin/lines missing")
        rd, wr = os.pipe()
        stream = None
        try:
            wire = b"GO\nEXTRA\n"
            full_write(wr, wire)
            os.close(wr)
            wr = None
            stream = io.TextIOWrapper(io.FileIO(rd, "r", closefd=True), encoding="utf-8")
            rd = None
            parser_sys = types.SimpleNamespace(stdin=stream, exit=sys.exit)
            code = compile(ast.Module(body=matches, type_ignores=[]), HELD, "exec")
            outcome = "fallthrough"
            status = None
            try:
                exec(code, {"sys": parser_sys, "__builtins__": __builtins__})
            except SystemExit as exc:
                outcome, status = "SystemExit", exc.code
            remainder = stream.read(4097)
            event("held_exact_parser_observation", "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", source_sha256=HELD_SHA,
                  ast_lines=[84, 85], ast_source_utf8_hex=b"".join(raw.splitlines(keepends=True)[83:85]).hex(),
                  input_wire_hex=wire.hex(), actual_parser_outcome=outcome, actual_parser_systemexit=status,
                  unread_suffix_hex=remainder.encode().hex(), no_full_assay_import=True, no_numpy_import=True,
                  expected_strict_rejection_status=6)
            result["method_return"] = {"parser_outcome": outcome, "systemexit": status}
        finally:
            if stream is not None:
                stream.close()
            if rd is not None:
                os.close(rd)
            if wr is not None:
                os.close(wr)
        return result
    try:
        env["validate"](cfg)
        if case in CHANNEL:
            event("original_validate_return", cfg_sha256=REQUEST["config"]["sha256"])
        s = env["Supervisor"](cfg, REQUEST["config"]["path"], REQUEST["config"]["sha256"])
        if case == "io_different_device":
            device = REQUEST["different_device"]
            if device is None:
                PREREQUISITES.append("independently approved existing genuinely different-device directory")
                result["method_return"] = None
                return result
            if not isinstance(device, dict) or set(device) != {"path", "inode", "read_only_existing"} or device["read_only_existing"] is not True:
                raise ValueError("different-device prerequisite schema")
            fd = directory(device["path"])
            try:
                actual = ident(fd)
            finally:
                os.close(fd)
            native_root = directory(cfg["lane_disk_root"])
            try:
                root_device = ident(native_root)[0]
            finally:
                os.close(native_root)
            event("different_device_readonly_preflight", approved=device, actual_inode=actual, root_device=root_device,
                  native_device_distinct=actual[0] != root_device, no_external_write=True)
            if actual != device["inode"] or actual[0] == root_device:
                PREREQUISITES.append("approved existing directory identity/device distinctness not established")
                return result
            # Fixed method-only overlay of cfg.lane. The original verify_anchors
            # performs its own native readonly open/fstat device comparison.
            s.cfg = dict(cfg, lane=device["path"])
            event("readonly_lane_method_overlay", "MODIFIED_QUALIFICATION_FIXTURE", original_lane=cfg["lane"],
                  approved_existing_lane=device["path"], source_method="Supervisor.verify_anchors")
            s.open_anchors()
        else:
            s.open_anchors()
        if case in ("io_root_swap", "io_subtree_swap"):
            paths = anchors(case, RUN)
            target = paths["charge"] if case == "io_root_swap" else paths["out"]
            archived = RUN + "/scratch/" + ("root.original" if case == "io_root_swap" else "out.original")
            marker = target + "/fixture-marker.txt"
            created = exclusive(marker, b"fresh bounded fixture marker\n")
            if os.path.lexists(archived):
                raise FileExistsError("directory archive exists")
            before = directory(target)
            try:
                original_inode = ident(before)
            finally:
                os.close(before)
            os.rename(target, archived)
            os.mkdir(target, 0o700)
            if case == "io_root_swap":
                os.mkdir(target + "/out", 0o700)
                os.mkdir(target + "/tmp", 0o700)
            replacement = exclusive(marker, b"fresh bounded fixture marker\n")
            after = directory(target)
            try:
                replacement_inode = ident(after)
            finally:
                os.close(after)
            event("native_directory_replacement", target=target, archive=archived, original_inode=original_inode,
                  replacement_inode=replacement_inode, original_marker=created, replacement_marker=replacement,
                  no_old_or_approval_objects_moved=True)
            s.verify_anchors(env["Deadline"](1, WORK_END - 0.1))
        elif case in CHANNEL + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS:
            result["method_return"] = s.authorization_io(env["Deadline"](1, WORK_END - 0.1))
            if case in TYPE_PREP:
                result["method_return"] = s.creation_manifest(env["Deadline"](1, WORK_END - 0.1))
    except BaseException as exc:
        result["exception"] = exception(exc)
        event("original_method_exception", error=exception(exc), source_method=("validate/authorization_io/creation_manifest" if case in CHANNEL + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS else "verify_anchors"))
    return result


def artifact_inventory():
    result = []
    seen_paths = set()
    def visit(path, depth=0):
        check("artifact inventory")
        if depth > 12 or len(result) >= 1024:
            raise OSError("artifact inventory cap")
        try:
            fd = directory(path)
        except FileNotFoundError:
            result.append({"path": path, "missing": True})
            return
        try:
            result.append({"path": path, "directory_inode": ident(fd)})
            names = sorted(os.listdir(fd))
            for name in names:
                child = path + "/" + name
                value = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if stat.S_ISDIR(value.st_mode):
                    visit(child, depth + 1)
                elif stat.S_ISREG(value.st_mode):
                    result.append(read_regular(child, OUTPUT_CAP)[0])
                else:
                    result.append({"path": child, "inode": [value.st_dev, value.st_ino], "mode_raw": value.st_mode,
                                   "unsupported_artifact": True})
        finally:
            os.close(fd)
    for path in ARTIFACT_ROOTS:
        if path not in seen_paths:
            seen_paths.add(path)
            visit(path)
    for name in ("GO.json", "GO.archived.json", "pinned-scratch.txt", "child-ready.json", "child-open-release.json"):
        path = RUN + "/" + name
        try:
            result.append(read_regular(path, OUTPUT_CAP)[0])
        except FileNotFoundError:
            result.append({"path": path, "missing": True})
    return result


def close_source_descriptors(proxy):
    # Only descriptors created/opened by this source namespace. No generic fd
    # sweep and no close of parent captures/standard descriptors.
    if STATE is not None:
        for record in STATE.keep:
            if record.get("pid") is not None and not (record.get("leader_reaped") or
                    (record is STATE.child and STATE.rc is not None)):
                UNRESOLVED.append({"kind": "source_owned_process", "pid": record["pid"],
                                   "identity": record.get("identity") or STATE.ident,
                                   "role": record["role"], "reason": "source return is not endedness proof"})
        for thread in STATE.threads:
            if thread.is_alive():
                UNRESOLVED.append({"kind": "source_sink_thread", "name": thread.name})
    if any(x["kind"] == "source_sink_thread" for x in UNRESOLVED):
        UNRESOLVED.append({"kind": "source_fds", "reason": "live source thread retains its owned descriptors"})
        return
    for fd, info in list(proxy.fds.items()):
        if fd < 3:
            continue
        try:
            if ident(fd) != info["inode"]:
                UNRESOLVED.append({"kind": "fd_identity_changed", "fd": fd, "expected": info})
                continue
            os.close(fd)
            event("fixture_closes_source_owned_fd", fd=fd, original=info)
        except OSError as exc:
            event("fixture_source_fd_close_error", fd=fd, original=info, error=exception(exc))
        proxy.fds.pop(fd, None)


def write_pre_b_record():
    if REC_AT_B is None:
        return
    if isinstance(REC_AT_B, bytes):
        facts = exclusive(RUN + "/scratch/pre-b-record.json", REC_AT_B)
        event("pre_b_record_artifact", artifact=facts, scope_label="SOURCE_RECORD_BEFORE_ORIGINAL_B_ACCOUNTING")
    else:
        UNRESOLVED.append({"kind": "pre_b_record_truncated", **REC_AT_B})


def write_outcome(case, trusted, source_outcome, selected, source_main_called):
    if TRUNCATED["events"]:
        UNRESOLVED.append({"kind": "event_trace_truncated", "dropped_events": TRUNCATED["events"],
                           "first_dropped_operation": TRUNCATED["first_operation"]})
    if ENVELOPE_REFUSAL is not None:
        UNRESOLVED.append({"kind": "fixture_envelope_refusal", **ENVELOPE_REFUSAL})
    payload = {"kind": "rqls10-guard-matrix-outcome-v1", "case": case, "scope": "MODIFIED_QUALIFICATION_FIXTURE",
               "bindings": {"approval_sha256": trusted, "request_sha256": APPROVAL["request_sha256"],
                            "request_created": APPROVAL["request_created"],
                            "sources": REQUEST["sources"], "config": REQUEST["config"], "go_original": REQUEST["go_original"],
                            "go": REQUEST["go"], "stability": REQUEST["stability"], "preparation": REQUEST["preparation"],
                            "anchors": REQUEST["anchors"], "allocation": REQUEST["allocation"],
                            "hook_set": REQUEST["hook_set"], "negative_control": REQUEST["negative_control"]},
               "owner": {"pid": os.getpid(), "pgid": os.getpgrp(), "mono_begin": BEGIN, "mono_end": time.monotonic()},
               "observations": EVENTS, "source_outcome": source_outcome, "source_state": source_state(),
               "accounting": accounting_snapshot(), "artifacts": artifact_inventory(), "unresolved": UNRESOLVED,
               "missing_prerequisites": PREREQUISITES, "selected_status_not_actual_exit": selected,
               "original_main_called": source_main_called, "evidence_complete": not bool(UNRESOLVED),
               "terminal": {"source_sha256": SUP_SHA, "ast_lines": TERMINAL_LINES, "unchanged": True,
                            "actual_exit_authority": "independent parent capture only; actual14 never120"},
               "limits": REQUEST["limits"], "observed_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               "authority": "NO_GO_NO_RELEASE_NO_SCIENCE_ACCEPTANCE"}
    data = packed(payload)
    if len(data) > 8 << 20:
        payload = {k: payload[k] for k in ("kind", "case", "scope", "bindings", "owner", "terminal", "limits", "authority")}
        payload.update(evidence_complete=False, oversized_original_bytes=len(data), oversized_original_sha256=sha(data),
                       unresolved=[{"kind": "outcome_oversized"}], selected_status_not_actual_exit=selected)
        data = packed(payload)
    exclusive(RUN + "/fixture-outcome.json", data)


def run(case, trusted):
    global SELECTED, APPROVED_CFG
    cfg = authorize(case, trusted)
    APPROVED_CFG = cfg
    env, proxy, terminal = source_load()
    install_hooks(env, proxy)
    original_main = env["main"]
    stderr_fixture = None
    if case in POST:
        stderr_fixture = NativeStderr(case)
        sys.stderr = stderr_fixture
    else:
        sys.stderr = BoundedStdout(ORIGINAL_STDERR, "stderr")
    sys.stdout = BoundedStdout(ORIGINAL_STDOUT)
    method_only = case in METHOD
    def fixture_main():
        global SELECTED, REPORTING
        outcome = None
        try:
            if method_only:
                outcome = method_fixture(cfg)
                SELECTED = 0  # Method transport only; original method exception is independently checked.
            else:
                old_argv = sys.argv
                sys.argv = [SUP, REQUEST["config"]["path"]]
                try:
                    SELECTED = original_main()
                finally:
                    sys.argv = old_argv
                outcome = {"mode": "ORIGINAL_FULL_MAIN_WITH_FIXED_OVERLAY", "selected_source_return": SELECTED,
                           "exception": None, "original_main_called": True}
        except BaseException as exc:
            SELECTED = 2
            outcome = {"mode": "FIXTURE_EXCEPTION", "exception": exception(exc), "original_main_called": not method_only}
            UNRESOLVED.append({"kind": "fixture_exception", "error": exception(exc)})
        REPORTING = True  # Source work ended; only bounded evidence/reporting may use the reserve.
        # Reporting failures are retained (or leave a missing outcome => parent HOLD); they never
        # change the selected source status handed to the unchanged original terminal.
        safe_hook("finish_descriptor_fault_window", proxy.end_window, "main_returned_before_expected_close")
        if stderr_fixture is not None:
            safe_hook("persistent_stderr_probes", stderr_fixture.persistent_probes)
            safe_hook("retain_stderr_until_terminal", stderr_fixture.retain_until_terminal)
        safe_hook("write_pre_b_record", write_pre_b_record)
        safe_hook("close_source_descriptors", close_source_descriptors, proxy)
        safe_hook("write_outcome", write_outcome, case, trusted, outcome, SELECTED, not method_only)
        # The original terminal now sees this result. Never translate14 to0/120,
        # and never call normal sys.exit instead of original source19 _exit14.
        return SELECTED
    env["main"] = fixture_main
    env["__name__"] = "__main__"
    exec(compile(ast.Module(body=[terminal], type_ignores=[]), SUP, "exec"), env)


if __name__ == "__main__":
    # First framing record precedes request reads, source loading and any child.
    owner = {"kind": "rqls10-matrix-owner-v1", "pid": os.getpid(), "pgid": os.getpgrp(),
             "mono_begin": BEGIN, "scope": "NATIVE_OWNER_RECORD_NOT_GUARDIAN_SUMMARY"}
    owner_raw = packed(owner)
    full_write(1, owner_raw)
    EMITTED["stdout"] = len(owner_raw)
    if len(sys.argv) != 3:
        ORIGINAL_STDERR.write("fixed CASE_ID and external PARENT_APPROVAL_SHA256 required\n")
        sys.exit(2)
    try:
        run(sys.argv[1], sys.argv[2])
    except SystemExit:
        raise
    except BaseException as exc:
        # No request/source authority failure can admit work or manufacture a
        # successful outcome. Hex prevents an error's model date masquerade.
        full_write(2, packed({"kind": "rqls10-matrix-authority-or-envelope-refusal-v1", "error": exception(exc)}))
        sys.exit(2)
