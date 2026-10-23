#!/usr/bin/env python3
"""REVIEW CANDIDATE written-only I/O matrix oracle. No execution or release authority.

CLI: CHECK CASE_ID PARENT_APPROVAL_SHA256 PARENT_CAPTURE_SHA256 (guard_matrix_io_check_v2.py, successor of v1)
Reads fixed RUN/parent-capture.json and actual driver.stdout/driver.stderr.
Does not import the driver, child or supervisor; never accepts a driver pass
boolean or selected status as actual exit. Supervisor19 and child12 have exact source pins;
the external parent approval must bind the complete frozen candidate source set.
Status precedence: HOLD (required proof unavailable) > NOT_MET (established failed predicate) >
NOT_EXERCISED (validated case-specific missed real boundary only) > FIXTURE_PREDICATES_MET.
Failures and missing evidence are always retained; expected outcomes equal the frozen case objects.
"""
import hashlib
import json
import math
import os
import signal
import stat
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
BASE_SHA = "e3a8006890a164d36fdacbadc6e63b64c87302ec46149c7f3a6c731e1a3e186b"
HELD_SHA = "4a78a7a078b52dd55e4348b2ecac357c95ef8fcea461768f4f05d9809d1edf07"
# Successor install paths (parent-decided migration; child v1 is unchanged).
PATHS = {"supervisor": LANE + "/code/owned_supervisor_v19.py", "driver": LANE + "/code/guard_matrix_io_v2.py",
         "child": LANE + "/code/guard_matrix_io_child_v1.py", "oracle": LANE + "/code/guard_matrix_io_check_v2.py",
         "case_specs": LANE + "/review/rqls10-matrix-io-v2-cases.json", "base_child": LANE + "/code/guard_qual_child_v12.py",
         "held_consumer": LANE + "/code/rqls_fixedb_lm_v7.py"}
AUTH = tuple("io_auth_" + a + "_" + p for p in ("helper", "main", "go", "ack") for a in ("replace", "revoke"))
PUB = tuple("io_pub_" + p + "_" + r for p in ("write", "fsync", "close", "readback", "dirsync")
            for r in ("error", "late")) + ("io_pub_readback_mismatch", "io_pub_short_write")
ACCOUNT = ("io_account_pre_payload", "io_account_pre_b", "io_account_pre_end", "io_account_post_end")
POST = ("io_post_ack_stderr_write", "io_post_ack_stderr_flush", "io_post_ack_stderr_persistent_write", "io_post_ack_stderr_persistent_flush")
CHANNEL = ("io_channel_wrong_purpose", "io_channel_wrong_scenario", "io_channel_wrong_target", "io_channel_missing_negative",
           "io_channel_wrong_negative", "io_channel_numeric_boolean", "io_channel_missing_schema", "io_channel_extra_schema",
           "io_channel_malformed", "io_channel_preparation_digest", "io_channel_ordinary", "io_channel_certificate_extra")
MUTATION = ("io_mutation_pin_before_manifest", "io_mutation_pin_before_child_open", "io_mutation_launch_before_manifest",
            "io_mutation_launch_before_child_open")
ANCHOR = ("io_root_swap", "io_subtree_swap", "io_different_device")
TYPE_GO = ("io_type_go_cpu_slots_true", "io_type_go_outstanding_false", "io_type_go_lane_outstanding_false")
TYPE_PREP = ("io_type_prep_cpu_slots_true", "io_type_prep_outstanding_false", "io_type_prep_lane_outstanding_false")
NEGATIVE_KEYS = ("io_channel_negative_missing_key", "io_channel_negative_extra_key", "io_channel_negative_false")
EXTRA = ("io_extra_write_short", "io_extra_write_zero", "io_extra_write_error", "io_extra_write_late",
         "io_extra_close_error", "io_extra_close_late", "io_extra_go_age", "io_extra_deadline", "io_extra_expiry") + \
        tuple("io_extra_signal_" + sig + "_" + op for sig in ("term", "int", "hup") for op in ("write", "close"))
METHOD = ANCHOR + tuple(c for c in CHANNEL if c != "io_channel_ordinary") + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS
PREPARATION = MUTATION + tuple(c for c in CHANNEL if c not in ("io_channel_ordinary", "io_channel_certificate_extra")) + TYPE_PREP + NEGATIVE_KEYS + EXTRA
CASES = AUTH + PUB + ("io_staged_same_content",) + ANCHOR + ACCOUNT + POST + CHANNEL + MUTATION + TYPE_GO + TYPE_PREP + NEGATIVE_KEYS + EXTRA
# Exact frozen case-object outcomes (cross-checked against the pinned case specification at authority time).
EXPECTED_FAILURES = {
    "io_auth_replace_helper": ("HELPER_CALL_FAILED",), "io_auth_revoke_helper": ("HELPER_CALL_FAILED",),
    "io_auth_replace_main": ("HELPER_CALL_FAILED",), "io_auth_revoke_main": ("HELPER_CALL_FAILED",),
    "io_auth_replace_go": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"), "io_auth_revoke_go": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"),
    "io_auth_replace_ack": (), "io_auth_revoke_ack": (),
    "io_mutation_pin_before_manifest": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"), "io_mutation_pin_before_child_open": (),
    "io_mutation_launch_before_manifest": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED", "ARTIFACT_IDENTITY_CHANGED"),
    "io_mutation_launch_before_child_open": ("ARTIFACT_IDENTITY_CHANGED",),
    "io_extra_write_short": (), "io_extra_write_zero": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"),
    "io_extra_write_error": ("POST_SPAWN_FAILURE", "STDIN_CLOSE_FAILED", "GO_NOT_DELIVERED"),
    "io_extra_write_late": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"),
    "io_extra_close_error": ("POST_SPAWN_FAILURE", "STDIN_CLOSE_FAILED", "GO_NOT_DELIVERED"),
    "io_extra_close_late": ("POST_SPAWN_FAILURE",), "io_extra_go_age": ("GO_COMPLETION_AGE_EXCEEDED", "POST_SPAWN_FAILURE"),
    "io_extra_deadline": ("POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"), "io_extra_expiry": ("POST_SPAWN_FAILURE",)}
EXPECTED_FAILURES.update((c, ("POST_SPAWN_FAILURE",)) for c in EXTRA if c.startswith("io_extra_signal_"))
# Only these four frozen case objects declare REQUIRED_OUTPUT_MISSING from the ORIGINAL artifact map.
CONDITIONAL_OUTPUT = ("io_auth_replace_go", "io_auth_revoke_go", "io_mutation_pin_before_manifest", "io_mutation_launch_before_manifest")
# Source-wait child status; signal cases derive 0 from their frozen full line/EOF measurement.
EXPECTED_CHILD = {"io_mutation_pin_before_child_open": 3, "io_mutation_launch_before_child_open": 3}
EXPECTED_CHILD.update((c, 6 if c in ("io_extra_write_zero", "io_extra_write_error") else 0) for c in EXTRA)
DELIVERED = ("io_extra_write_short", "io_extra_close_late", "io_extra_go_age", "io_extra_expiry") + \
            tuple(c for c in EXTRA if c.startswith("io_extra_signal_"))
SIGNALS = {"term": int(signal.SIGTERM), "int": int(signal.SIGINT), "hup": int(signal.SIGHUP)}
CANCEL_SIGNALS = sorted(SIGNALS.values())  # source19 CANCEL_SIGNALS blocked by protected().
FINGERPRINT = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
IDENTITY_KEYS = set(FINGERPRINT) | {"status", "comm"}
# Exact native chain on the closed stimulus number: (operation target, ((native op, unallocated target), ...)).
# source19 closes publish/read_file/stdin descriptors in finally blocks and never closes retained root FDs.
FD_CHAINS = {"io_pub_write_error": ("write", (("native_write", "write"), ("native_close", "close"))),
             "io_pub_fsync_error": ("fsync", (("native_fsync", "fsync"), ("native_close", "close"))),
             "io_pub_close_error": ("close", (("native_close", "close"),)),
             "io_pub_readback_error": ("readback", (("native_read", "readback"), ("native_close", "close"))),
             "io_pub_dirsync_error": ("dirsync", (("native_fsync", "dirsync"),)),
             "io_extra_write_error": ("write", (("native_write", "write"), ("native_close", "close"))),
             "io_extra_close_error": ("close", (("native_close", "close"), ("native_close", "close")))}
FD_EVENTS = ("native_write", "native_fsync", "native_close", "native_read", "closed_number_unallocated_before_source_call",
             "source_created_descriptor", "stimulus_number_reallocated", "fixture_closes_source_owned_fd", "fixture_source_fd_close_error")
# Source-owned process/descriptor blockers are established failures; every other unresolved kind is HOLD.
SOURCE_BLOCKERS = ("source_owned_process", "source_sink_thread", "source_fds", "fd_identity_changed")
START = time.monotonic()
DEADLINE = START + 60
FAILURES = []
MISSING = []    # Required proof unavailable or fixture inconclusive: HOLD.
BOUNDARY = []   # Validated case-specific missed real boundary only: NOT_EXERCISED.


def check():
    if time.monotonic() >= DEADLINE:
        raise OSError("ORACLE_COOPERATIVE_DEADLINE")


def need(condition, name):
    if not condition:
        FAILURES.append(name)


def exact(condition, name):
    if not condition:
        raise ValueError(name)


def integer(value):
    return type(value) is int


def number(value):
    return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value)


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return set(a) == set(b) and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def created_continuity(wanted, facts):
    exact(isinstance(wanted, dict) and set(wanted) == {"path", "inode", "sha256", "bytes", "nlink", "creation_ordinal"} and
          integer(wanted["creation_ordinal"]) and wanted["creation_ordinal"] >= 0 and
          integer(wanted["nlink"]) and wanted["nlink"] == 1 and
          all(typed_equal(wanted[k], facts[k]) for k in ("path", "inode", "sha256", "bytes", "nlink")),
          "original approved exclusive creation inode/content continuity")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def decode(raw):
    def finite(text):
        result = float(text)
        if not math.isfinite(result):
            raise ValueError("nonfinite JSON")
        return result
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_float=finite,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


def packed(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def directory(path):
    exact(isinstance(path, str) and path.startswith("/") and os.path.normpath(path) == path, "canonical directory")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    if path == "/":
        return fd  # No empty component traversal for the canonical root directory.
    try:
        for part in path.split("/")[1:]:
            check()
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def inode(fd):
    value = os.fstat(fd)
    return [value.st_dev, value.st_ino]


def regular(path, cap=16 << 20):
    parent = directory(os.path.dirname(path))
    fd = None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
        before = os.fstat(fd)
        exact(stat.S_ISREG(before.st_mode) and 0 <= before.st_size <= cap, "bounded regular")
        result = bytearray()
        while len(result) < before.st_size:
            check()
            raw = os.read(fd, min(65536, before.st_size - len(result)))
            exact(bool(raw), "short regular read")
            result.extend(raw)
        after = os.fstat(fd)
        exact(not os.read(fd, 1) and (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns) ==
              (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns), "regular changed")
        named = os.stat(os.path.basename(path), dir_fd=parent, follow_symlinks=False)
        exact((named.st_dev, named.st_ino, named.st_size, named.st_mtime_ns, named.st_ctime_ns) ==
              (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns), "original regular pathname replaced during read")
        return {"path": path, "inode": [before.st_dev, before.st_ino], "sha256": sha(result),
                "bytes": len(result), "nlink": before.st_nlink}, bytes(result)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def error_text(value):
    exact(isinstance(value, dict) and set(value) == {"type", "errno", "UTF8_HEX", "utf8_bytes", "text_scope"}, "error raw schema")
    exact(value["text_scope"] == "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "error date scope")
    raw = bytes.fromhex(value["UTF8_HEX"])
    exact(integer(value["utf8_bytes"]) and value["utf8_bytes"] == len(raw), "complete, not truncated, error text evidence")
    return raw.decode("utf-8", "surrogateescape")


def pick(events, operation):
    return [v for v in events if v["operation"] == operation]


def only(events, operation):
    values = pick(events, operation)
    exact(len(values) == 1, "exact one raw event: " + operation)
    return values[0]


def resources(value):
    return isinstance(value, dict) and set(value) == {"charged_bytes", "lane_bytes", "free"} and all(integer(v) and v >= 0 for v in value.values())


def case_design(case, run, request, cfg, go):
    """Independent fixed-input reconstruction, not a driver's asserted pass."""
    name = "mutate_pin" if case in MUTATION and "_pin_" in case else "mutate_evidence"
    channel = {}
    if case in PREPARATION:
        channel = {"kind": "qualification-creation-v1", "scenario": name,
                   "preparation_path": run + "/preparation.json", "preparation_sha256": request["preparation"]["sha256"],
                   "target_path": run + ("/pinned-scratch.txt" if name == "mutate_pin" else "/out/launch.json")}
        if case == "io_channel_wrong_scenario":
            channel["scenario"] = "fixed-invalid-scenario"
        elif case == "io_channel_wrong_target":
            channel["target_path"] = run + "/fixed-forbidden-target.txt"
        elif case == "io_channel_missing_schema":
            del channel["kind"]
        elif case == "io_channel_extra_schema":
            channel["extra"] = True
        elif case == "io_channel_malformed":
            channel = []
        elif case == "io_channel_preparation_digest":
            channel["preparation_sha256"] = "0" * 64
    exact(typed_equal(cfg["creation_channel"], channel), "exact declared channel, no arbitrary target")
    negative = {"scenario": name, "kind": "mutation", "creation_channel": True} if case in PREPARATION else \
               {"scenario": case, "kind": "matrix_io", "creation_channel": False}
    if case == "io_channel_wrong_negative":
        negative["scenario"] = "fixed-wrong-scenario"
    elif case == "io_channel_numeric_boolean":
        negative["creation_channel"] = 1
    elif case == "io_channel_negative_missing_key":
        del negative["kind"]
    elif case == "io_channel_negative_extra_key":
        negative["extra"] = True
    elif case == "io_channel_negative_false":
        negative["creation_channel"] = False
    go_keys = {"decision", "item", "configs", "not_after_epoch", "stability_receipt_sha256"}
    if case not in ("io_channel_ordinary", "io_channel_missing_negative"):
        go_keys.add("qualification_negative")
        exact(typed_equal(go["qualification_negative"], negative), "exact negative GO key/type defect")
    exact(set(go) == go_keys, "exact original GO keys")
    exact(cfg["purpose"] == ("ordinary" if case == "io_channel_wrong_purpose" else "guard-qualification"), "fixed config purpose")
    exact(typed_equal(cfg["cpu_slots"], request["allocation"]["cpu_slots"]) and cfg["busy_limit"] in (1, 2) and
          cfg["max_wall_s"] <= 60 and cfg["settle_s"] <= 30 and cfg["max_chunk_seconds"] <= 300 and
          cfg["rss_trip_bytes"] <= 256 << 20 and cfg["lane_roots"] == [LANE] and cfg["fault_injection"] == {}, "fixed resources/source fault scope")
    names = {"GO": "GO.json", "go_original": "GO.original.json", "config": "config.json", "stability": "stability.json",
             "preparation": "preparation.json", "pin": "pinned-scratch.txt", "replacement": "scratch/replacement.bin"}
    exact(set(request["created_facts"]) == set(names), "complete created-input role set")
    ordinals = []
    for role in names:
        fact = request["created_facts"][role]
        required = role not in ("preparation", "pin", "replacement") or role == "preparation" and case in PREPARATION or \
                   role == "pin" and case in MUTATION and "_pin_" in case or role == "replacement" and case in MUTATION
        exact((fact is not None) is required, "exact created input presence")
        if fact is not None:
            exact(fact["path"] == run + "/" + names[role] and integer(fact["creation_ordinal"]), "fixed original-created path/order")
            ordinals.append(fact["creation_ordinal"])
    approval = decode(regular(run + "/parent-authorization.json", 1 << 20)[1])
    exact(len(ordinals) == len(set(ordinals)) and all(n < approval["request_created"]["creation_ordinal"] for n in ordinals), "approved creation ordering")
    exact(request["created_facts"]["GO"]["inode"] != request["created_facts"]["go_original"]["inode"], "GO original/copy distinct original inodes")
    if case in PREPARATION:
        prep = decode(regular(run + "/preparation.json", 1 << 20)[1])
        pins = {"supervisor": {"path": PATHS["supervisor"], "sha256": SUP_SHA},
                "child": {"path": PATHS["base_child"], "sha256": BASE_SHA}}
        for role, file in (("writer", "guard_qual_configs_v12.py"), ("checker", "guard_qual_check_v11.py")):
            path = LANE + "/code/" + file
            pins[role] = {"path": path, "sha256": regular(path, 2 << 20)[0]["sha256"]}
        allocation = dict(request["allocation"])
        if case in TYPE_PREP:
            field = "cpu_slots" if "cpu_slots" in case else "lane_outstanding_reservations_bytes" if "lane_outstanding" in case else "outstanding_reservations_bytes"
            exact(typed_equal(allocation[field], 1 if field == "cpu_slots" else 0), "prep typed alias integer prerequisite")
            allocation[field] = field == "cpu_slots"
        pin = request["created_facts"]["pin"]
        fixture = {k: pin[k] for k in ("path", "inode", "sha256", "bytes", "nlink")} if name == "mutate_pin" else None
        expected = {"kind": "qualification-creation-preparation-v1", "scenario": name,
                    "run": request["anchors"]["run"], "output_root": request["anchors"]["out"], "fixture": fixture,
                    "source_pins": pins, "python": {"path": cfg["argv"][0], "sha256": regular(cfg["argv"][0], 64 << 20)[0]["sha256"]},
                    "allocation": allocation, "negative_control": True}
        exact(typed_equal(prep, expected), "original preparation semantics/current actual source pins/declared defect")
    if case == "io_extra_go_age":
        exact(cfg["max_wall_s"] == 10 and cfg["sample_s"] == 10 and request["parameters"]["child_life_s"] >= 15, "fixed real age settings")
    if case == "io_extra_deadline":
        exact(cfg["max_wall_s"] == 40 and cfg["sample_s"] == 10 and cfg["settle_s"] <= 5 and request["parameters"]["child_life_s"] >= 50,
              "original IO_S30 deadline remains before main40/child50 cutoffs")
    if case == "io_extra_expiry":
        exact(cfg["sample_s"] == 10, "unchanged original expiry census-freshness setting")


def frozen_case(raw, case):
    """Exact frozen expected outcomes; no oracle-added exception or conditional outcome."""
    spec = decode(raw)
    exact(isinstance(spec, dict) and spec.get("case_count") == 72 and isinstance(spec.get("cases"), list) and
          [c.get("case") if isinstance(c, dict) else None for c in spec["cases"]] == list(CASES), "frozen 72-case specification order")
    frozen = spec["cases"][CASES.index(case)]
    exact(type(frozen.get("expected_actual_exit")) is int and frozen["expected_actual_exit"] == expected_exit(case), "oracle exit equals frozen case")
    declared = case in EXPECTED_FAILURES
    exact(("expected_failure_codes" in frozen) is declared and
          (not declared or isinstance(frozen["expected_failure_codes"], list) and sorted(frozen["expected_failure_codes"]) == sorted(EXPECTED_FAILURES[case])) and
          ("conditional_failure" in frozen) is (case in CONDITIONAL_OUTPUT), "oracle failure set equals frozen case; no added conditional")
    signalled = case.startswith("io_extra_signal_")
    exact(("expected_trip_codes" in frozen) is signalled and (not signalled or frozen["expected_trip_codes"] == ["SUPERVISOR_CANCEL"]),
          "oracle trip set equals frozen case")
    child = case in EXPECTED_CHILD and not signalled
    exact(("expected_child_return_from_source_wait" in frozen) is child and
          (not child or typed_equal(frozen["expected_child_return_from_source_wait"], EXPECTED_CHILD[case])), "oracle child status equals frozen case")
    return frozen


def authority(case, approval_sha, capture_sha):
    exact(case in CASES and len(approval_sha) == 64 and len(capture_sha) == 64, "fixed invocation arguments")
    run = ROOT + "/" + case
    af, ar = regular(run + "/parent-authorization.json", 1 << 20)
    rf, rr = regular(run + "/request.json", 1 << 20)
    exact(af["sha256"] == approval_sha, "external approval SHA")
    approval, request = decode(ar), decode(rr)
    keys = {"kind", "case", "scope", "sources", "anchors", "allocation", "not_after_epoch", "negative_control", "hook_set",
            "config", "go", "go_original", "stability", "preparation", "mutable", "parameters", "limits", "different_device", "created_facts"}
    exact(set(request) == keys and set(approval) == keys | {"request_sha256", "request_created"}, "exact authority schemas")
    exact(approval["kind"] == "rqls10-guard-matrix-invocation-v1" and request["kind"] == "rqls10-guard-matrix-request-v1" and
          approval["request_sha256"] == rf["sha256"], "authority kinds/request digest")
    exact(all(typed_equal(request[k], approval[k]) for k in keys - {"kind"}), "strictly typed authority fields joined")
    created_continuity(approval["request_created"], rf)
    exact(af["nlink"] == 1, "single-link parent approval")
    exact(request["case"] == case and request["scope"] == "MODIFIED_QUALIFICATION_FIXTURE" and request["hook_set"] == [case], "exact case/scope/hooks")
    exact(request["negative_control"] is (case != "io_channel_ordinary"), "literal negative scope")
    exact(request["limits"] == {"max_wall_s": 300, "rss_bytes": 256 << 20, "output_bytes": 16 << 20,
                                "busy_ceiling": 2, "max_loops": 2}, "fixed resource limits")
    allocation = request["allocation"]
    exact(set(allocation) == {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} and
          all(integer(v) and v >= 0 for v in allocation.values()) and allocation["bytes"] == 20 << 20 and
          1 <= allocation["cpu_slots"] <= 2, "actual serialized allocation")
    exact(set(request["sources"]) == set(PATHS), "fixed source set")
    for role, path in PATHS.items():
        pin = request["sources"][role]
        exact(isinstance(pin, dict) and set(pin) == {"path", "sha256"} and pin["path"] == path, "source path/schema")
        facts, raw = regular(path, 2 << 20)
        exact(pin["sha256"] == facts["sha256"], "actual source bytes: " + role)
        expected = {"supervisor": SUP_SHA, "base_child": BASE_SHA, "held_consumer": HELD_SHA}.get(role)
        exact(expected is None or facts["sha256"] == expected, "immutable source: " + role)
        if role == "case_specs":
            frozen_case(raw, case)  # Oracle expectation tables must equal the pinned frozen case object.
    expected_anchors = {"run": run, "charge": run + "/fixture-root" if case in ANCHOR else run,
                        "scratch": run + "/scratch"}
    expected_anchors["out"] = expected_anchors["charge"] + "/out"
    expected_anchors["tmp"] = expected_anchors["charge"] + "/tmp"
    exact(set(request["anchors"]) == set(expected_anchors), "anchor set")
    for key, path in expected_anchors.items():
        anchor = request["anchors"][key]
        exact(set(anchor) == {"path", "inode"} and anchor["path"] == path and isinstance(anchor["inode"], list) and
              len(anchor["inode"]) == 2 and all(integer(v) and v >= 0 for v in anchor["inode"]), "original anchor schema")
        if case in ("io_root_swap", "io_subtree_swap") and key in ("charge", "out", "tmp"):
            continue  # The case-specific native archived-original checks follow.
        fd = directory(path)
        try:
            exact(inode(fd) == anchor["inode"], "current unchanged anchor: " + key)
        finally:
            os.close(fd)
    for role, name in (("config", "config.json"), ("go_original", "GO.original.json"), ("stability", "stability.json"), ("preparation", "preparation.json")):
        pin = request[role]
        if pin is None and role == "preparation":
            continue
        exact(set(pin) == {"path", "sha256"} and pin["path"] == run + "/" + name, "fixed input path")
        facts = regular(pin["path"], 1 << 20)[0]
        exact(facts["sha256"] == pin["sha256"], "actual immutable input digest")
        created_continuity(request["created_facts"][role], facts)
    exact(request["go"] == {"path": run + "/GO.json", "sha256": request["go_original"]["sha256"]}, "original GO copy pin")
    cfg = decode(regular(run + "/config.json", 1 << 20)[1])
    go = decode(regular(run + "/GO.original.json", 1 << 20)[1])
    admission = cfg.get("admission")
    exact(isinstance(admission, dict) and typed_equal(admission.get("reservation_bytes"), allocation["bytes"]) and
          typed_equal(admission.get("outstanding_reservations_bytes"), allocation["outstanding_reservations_bytes"]) and
          typed_equal(admission.get("lane_outstanding_reservations_bytes"), allocation["lane_outstanding_reservations_bytes"]),
          "approved serialized allocation equals the effective config admission reservation accounting")
    bound = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
    bound.update({k: cfg["admission"][k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
    if case in TYPE_GO:
        field = "cpu_slots" if "cpu_slots" in case else "lane_outstanding_reservations_bytes" if "lane_outstanding" in case else "outstanding_reservations_bytes"
        exact(typed_equal(bound[field], 1 if field == "cpu_slots" else 0), "typed alias actual integer prerequisite")
        bound[field] = field == "cpu_slots"
    exact(typed_equal(go.get("configs"), {request["config"]["sha256"]: bound}) and go.get("decision") == "GO" and go.get("item") == case and
          go.get("stability_receipt_sha256") == request["stability"]["sha256"], "exact original GO bindings")
    mode = "mutation" if case in MUTATION else "channel" if case in EXTRA else "wire"
    exact(isinstance(cfg.get("argv"), list) and len(cfg["argv"]) == 4 and cfg["argv"][1:] == [PATHS["child"], mode, case], "no arbitrary target argv")
    exact(cfg.get("env") == {"PATH": "/usr/bin:/bin", "TMPDIR": expected_anchors["tmp"], "PYTHONDONTWRITEBYTECODE": "1"}, "fixed child environment")
    exact(cfg.get("lane_disk_root") == expected_anchors["charge"] and cfg.get("output_roots") == [expected_anchors["out"]] and
          cfg.get("lane") == LANE and cfg.get("item") == case, "config anchors/item")
    exact(number(request["not_after_epoch"]) and number(go.get("not_after_epoch")) and go["not_after_epoch"] <= request["not_after_epoch"], "real expiry bindings")
    case_design(case, run, request, cfg, go)
    go_facts = regular(run + ("/GO.archived.json" if case in AUTH else "/GO.json"))[0]
    go_facts["path"] = run + "/GO.json"
    created_continuity(request["created_facts"]["GO"], go_facts)
    cf, cr = regular(run + "/parent-capture.json", 1 << 20)
    exact(cf["sha256"] == capture_sha, "external parent capture SHA")
    capture = decode(cr)
    capture_keys = {"kind", "case", "approval_sha256", "driver_source_sha256", "pid", "pgid", "mono_begin", "mono_end", "actual_exit",
                    "stdout", "stderr", "outcome_sha256", "wait_status"}
    exact(set(capture) == capture_keys and capture["kind"] == "rqls10-guard-matrix-parent-capture-v1" and capture["case"] == case and
          capture["approval_sha256"] == approval_sha and capture["driver_source_sha256"] == request["sources"]["driver"]["sha256"], "parent capture binding/schema")
    exact(integer(capture["pid"]) and integer(capture["pgid"]) and capture["pid"] > 1 and capture["pgid"] > 1 and
          number(capture["mono_begin"]) and number(capture["mono_end"]) and
          0 <= capture["mono_end"] - capture["mono_begin"] <= 300, "actual invocation native identity/time")
    wait = capture["wait_status"]
    exact(set(wait) == {"native_wait_status", "waitpid_pid", "reaped"} and wait["reaped"] is True and
          integer(wait["waitpid_pid"]) and typed_equal(wait["waitpid_pid"], capture["pid"]) and
          integer(wait["native_wait_status"]) and integer(capture["actual_exit"]) and
          os.waitstatus_to_exitcode(wait["native_wait_status"]) == capture["actual_exit"], "actual wait status not selected source status")
    streams = {}
    for name in ("stdout", "stderr"):
        record = capture[name]
        exact(set(record) == {"path", "sha256", "bytes", "inode", "eof"} and record["path"] == run + "/driver." + name and
              record["eof"] is True and integer(record["bytes"]) and record["bytes"] >= 0 and
              isinstance(record["inode"], list) and len(record["inode"]) == 2 and
              all(integer(value) and value >= 0 for value in record["inode"]),
              "exact complete parent stream schema with externally pinned ORIGINAL created-descriptor inode")
        facts, raw = regular(record["path"])
        exact(facts["sha256"] == record["sha256"] and facts["bytes"] == record["bytes"] and
              typed_equal(facts["inode"], record["inode"]), "actual no-follow capture bytes/inode match parent's ORIGINAL creation binding, not current-only substitution")
        streams[name] = raw
    exact(len(streams["stdout"]) + len(streams["stderr"]) <= 16 << 20, "actual capture output cap")
    of, obr = regular(run + "/fixture-outcome.json", 8 << 20)
    exact(of["sha256"] == capture["outcome_sha256"], "actual outcome/capture binding")
    outcome = decode(obr)
    exact(outcome.get("evidence_complete") is True and not (outcome.get("source_state") or {}).get("evidence_truncated"),
          "incomplete/truncated/oversized source evidence is HOLD")
    return run, request, cfg, go, capture, streams, outcome


def common(run, request, cfg, capture, streams, outcome):
    exact(outcome.get("kind") == "rqls10-guard-matrix-outcome-v1" and outcome.get("case") == request["case"] and
          outcome.get("scope") == "MODIFIED_QUALIFICATION_FIXTURE", "outcome kind/case/scope")
    expected = {"approval_sha256": capture["approval_sha256"], "request_sha256": regular(run + "/request.json", 1 << 20)[0]["sha256"],
                "request_created": decode(regular(run + "/parent-authorization.json", 1 << 20)[1])["request_created"],
                "sources": request["sources"], "config": request["config"], "go_original": request["go_original"], "go": request["go"],
                "stability": request["stability"], "preparation": request["preparation"], "anchors": request["anchors"],
                "allocation": request["allocation"], "hook_set": request["hook_set"], "negative_control": request["negative_control"]}
    exact(typed_equal(outcome.get("bindings"), expected), "outcome exact typed authority/source/request bindings")
    owner = outcome["owner"]
    exact(set(owner) == {"pid", "pgid", "mono_begin", "mono_end"} and owner["pid"] == capture["pid"] and owner["pgid"] == capture["pgid"] and
          capture["mono_begin"] <= owner["mono_begin"] <= owner["mono_end"] <= capture["mono_end"] and
          owner["mono_end"] - owner["mono_begin"] <= 300, "actual owner/time join")
    exact(outcome.get("limits") == request["limits"] and number(outcome.get("observed_maxrss_bytes")) and
          outcome["observed_maxrss_bytes"] <= 256 << 20, "observed owned resource envelope")
    events = outcome["observations"]
    exact(isinstance(events, list) and 1 <= len(events) <= 4096, "bounded raw event trace")
    previous = owner["mono_begin"]
    for index, value in enumerate(events):
        exact(isinstance(value, dict) and value.get("seq") == index and isinstance(value.get("operation"), str) and
              isinstance(value.get("scope"), str) and number(value.get("mono")) and previous <= value["mono"] <= owner["mono_end"], "event raw order/scope")
        previous = value["mono"]
        if "mono_before" in value:
            exact(number(value["mono_before"]) and number(value.get("mono_after")) and value["mono_before"] <= value["mono_after"] <= value["mono"], "native call raw interval")
        if "error" in value:
            error_text(value["error"])
    authority_event = only(events, "authority_checked")
    exact(authority_event["approval_sha256"] == capture["approval_sha256"] and authority_event["sources"] == request["sources"] and
          authority_event["original_run_inode"] == request["anchors"]["run"]["inode"], "actual authority event")
    load = only(events, "source_loaded")
    exact(load["source_sha256"] == SUP_SHA and load["wrapper_sha256"] == request["sources"]["driver"]["sha256"] and
          load["config_sha256"] == request["config"]["sha256"] and load["hook_set"] == [request["case"]] and load["seq"] > authority_event["seq"], "authorized immutable load and visible hook pins")
    terminal = outcome["terminal"]
    exact(terminal.get("source_sha256") == SUP_SHA and terminal.get("ast_lines") == [2688, 2692] and terminal.get("unchanged") is True,
          "original source terminal identity")
    stdout_lines = streams["stdout"].splitlines(keepends=True)
    exact(bool(stdout_lines) and all(v.endswith(b"\n") for v in stdout_lines), "full stdout framing")
    first = decode(stdout_lines[0])
    exact(set(first) == {"kind", "pid", "pgid", "mono_begin", "scope"} and first["kind"] == "rqls10-matrix-owner-v1" and
          first["pid"] == owner["pid"] and first["pgid"] == owner["pgid"] and first["mono_begin"] == owner["mono_begin"], "first native owner framing record")
    summaries = [decode(line) for line in stdout_lines[1:]]
    method_only = request["case"] in METHOD
    exact(outcome["original_main_called"] is (not method_only), "method-only vs full-main scope")
    exact(len(summaries) == (0 if method_only else 1), "exact stdout summary count; no contradictory second summary")
    summary = summaries[0] if summaries else None
    if summary is not None:
        exact(summary.get("supervisor") == "owned_supervisor_v19" and ("config_sha256" not in summary or summary["config_sha256"] == request["config"]["sha256"]), "captured actual source19 summary/config if exported")
        writes = pick(events, "source_stdout_write")
        exact(len(writes) == 1 and writes[0]["caller_bytes"] == len(stdout_lines[1]) and writes[0]["text_sha256"] == sha(stdout_lines[1]), "actual full stdout/source-write byte join")
        exact(all(integer(v) and v > 0 for v in writes[0]["native_write_counts"]) and
              sum(writes[0]["native_write_counts"]) == len(stdout_lines[1]), "actual bounded native stdout full-write counts")
        final = outcome["source_state"]["rec"].get("final_census")
        need(isinstance(final, dict) and final.get("complete") is True and final.get("incomplete_n") == 0 and
             final.get("owned_live") == [] and final.get("unproved_live") == [] and final.get("group_live") == [],
             "native final source coverage/endedness cannot be excused by an expected I/O refusal code")
    # Independently reopen all retained artifacts; no evidence bool substitutes.
    artifacts = outcome["artifacts"]
    exact(isinstance(artifacts, list) and len(artifacts) <= 1024, "bounded artifact inventory")
    by_path = {}
    for value in artifacts:
        path = value["path"]
        exact(path.startswith(run + "/") and os.path.normpath(path) == path and "/../" not in path, "current-run artifact path")
        exact(path not in by_path, "one artifact fact per current name")
        by_path[path] = value
        if value.get("missing") is True:
            exact(not os.path.lexists(path), "missing artifact really missing")
        elif "directory_inode" in value:
            fd = directory(path)
            try:
                exact(inode(fd) == value["directory_inode"], "actual directory inode")
            finally:
                os.close(fd)
        elif "sha256" in value:
            facts, raw = regular(path)
            exact(all(facts[k] == value[k] for k in ("path", "inode", "sha256", "bytes", "nlink")), "actual artifact inode/digest/size/links")
        else:
            exact(False, "unsupported/ambiguous artifact type")
    unresolved = outcome.get("unresolved")
    exact(isinstance(unresolved, list), "unresolved list")
    for value in unresolved:
        kind = value.get("kind") if isinstance(value, dict) else None
        if kind == "event_trace_truncated":
            MISSING.append("RAW_EVENT_TRACE_TRUNCATED")  # Missing raw evidence: HOLD, never MET or NOT_EXERCISED.
        elif kind in SOURCE_BLOCKERS:
            FAILURES.append("unresolved source ownership/coverage evidence prevents closure: " + kind)
        else:
            # Fixture/wrapper failure, truncation or unavailable ownership-window evidence: inconclusive HOLD.
            MISSING.append("UNRESOLVED_REQUIRED_EVIDENCE_OR_FIXTURE_FAILURE:" + str(kind))
    # Raw child-spawn registration is after original immediate registration, never
    # a manufactured guardian verdict. The original helper remains /bin/date.
    for value in pick(events, "native_spawn_registered"):
        exact(value["source_ledger_registered"] is True and integer(value["pid"]) and value["pid"] > 1, "native source PID registered before work")
        if value["role"] == "helper":
            exact(value["argv"] == ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"] and value["child_external_sha_overlay"] is None, "unchanged real metadata helper")
        else:
            exact(value["role"] == "child" and value["argv"] == cfg["argv"] and value["child_external_sha_overlay"] == capture["approval_sha256"], "fixed child-only external SHA overlay")
        if value["native_pgid"] is not None:
            exact(value["native_pgid"] == value["pid"], "actual fresh native process group")
    helper_pids = [v["pid"] for v in pick(events, "native_spawn_registered") if v["role"] == "helper"]
    state = outcome.get("source_state")
    exact(state is None and not pick(events, "native_spawn_registered") or
          isinstance(state, dict) and isinstance(state.get("reconciliation"), dict) and
          isinstance(state["reconciliation"].get("helpers"), list) and
          [h.get("pid") if isinstance(h, dict) else None for h in state["reconciliation"]["helpers"]] == helper_pids,
          "every natively registered helper has exactly one retained source helper record, in spawn order")
    expected_paths = set()
    def inventory_paths(path, depth=0):
        exact(depth <= 12 and len(expected_paths) < 1024, "actual artifact inventory bounds")
        expected_paths.add(path)
        fd = directory(path)
        try:
            for name in os.listdir(fd):
                check()
                full = path + "/" + name
                value = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if stat.S_ISDIR(value.st_mode):
                    inventory_paths(full, depth + 1)
                else:
                    exact(stat.S_ISREG(value.st_mode), "actual unlisted nonregular artifact")
                    expected_paths.add(full)
        finally:
            os.close(fd)
    roots = [request["anchors"]["charge"]["path"], run + "/scratch"] if request["case"] in ANCHOR else \
            [request["anchors"]["out"]["path"], request["anchors"]["tmp"]["path"], run + "/scratch"]
    for path in roots:
        inventory_paths(path)
    expected_paths.update(run + "/" + name for name in
                          ("GO.json", "GO.archived.json", "pinned-scratch.txt", "child-ready.json", "child-open-release.json"))
    exact(set(by_path) == expected_paths, "independent complete current-name artifact correspondence, not a listed subset")
    return events, summary, by_path


def expected_exit(case):
    if case in AUTH or case in POST or case in ("io_account_pre_end", "io_account_post_end", "io_extra_expiry"):
        return 14
    if case in ("io_account_pre_payload", "io_account_pre_b", "io_staged_same_content", "io_pub_dirsync_error", "io_pub_dirsync_late"):
        return 13
    if case in PUB and case != "io_pub_short_write":
        return 12
    if case in MUTATION:
        return 0 if case == "io_mutation_pin_before_child_open" else 11
    if case in EXTRA:
        return 0 if case == "io_extra_write_short" else 11
    return 0


def accounting(run, case, cfg, outcome, events, summary):
    value = outcome["accounting"]
    keys = {"publication_payload_bytes", "publication_resources", "ack_resources", "last_accounting_observation",
            "accounting_observations", "min_free_witness", "min_free", "last_native_free"}
    exact(set(value) == keys, "source19 raw/null/accounting-event schema")
    payload, b, end = (value[k] for k in ("publication_payload_bytes", "publication_resources", "ack_resources"))
    observations, last = value["accounting_observations"], value["last_accounting_observation"]
    native = pick(events, "native_fstatvfs")
    exact(isinstance(observations, list) and len(observations) == len(native), "every native accounting acquisition joined, no fresh substitute")
    event_keys = {"id", "phase", "inside_helper", "mono_begin", "mono_observed", "resources", "retained", "returned"}
    for index, (observation, actual) in enumerate(zip(observations, native)):
        exact(set(observation) == event_keys and type(observation["id"]) is int and observation["id"] == index + 1 and
              type(observation["inside_helper"]) is bool and type(observation["retained"]) is bool and type(observation["returned"]) is bool and
              resources(observation["resources"]) and (observation["mono_begin"] is None or number(observation["mono_begin"])) and
              (observation["mono_observed"] is None or number(observation["mono_observed"])), "exact typed historical accounting event with honest null timing")
        raw = actual["raw"]
        need(set(raw) == {"f_bavail", "f_frsize", "free"} and all(integer(x) and x >= 0 for x in raw.values()) and
             raw["free"] == raw["f_bavail"] * raw["f_frsize"] == observation["resources"]["free"],
             "actual native free blocks*unit retained before source completion check")
        if number(observation["mono_observed"]):
            need(observation["mono_begin"] <= actual["mono_before"] <= actual["mono_after"] <= observation["mono_observed"],
                 "actual accounting acquisition interval, not a fresh clock substitute")
    need(last is None if not observations else typed_equal(last, observations[-1]), "actual final accounting event retained")
    if observations:
        minimum = min(observations, key=lambda row: row["resources"]["free"])
        need(typed_equal(value["min_free_witness"], minimum) and value["min_free"] == minimum["resources"]["free"],
             "independently reconstructed first establishing historical minimum witness")
        need(typed_equal(value["last_native_free"], native[-1]["raw"]), "actual last rawfree, never a fresh observation")
    if summary is not None:
        recon = summary.get("reconciliation", {})
        need(all(typed_equal(recon.get(k), value[k]) for k in keys), "captured original reconciliation exact raw/null/accounting join")
    if case not in ACCOUNT:
        return
    stage = case.removeprefix("io_account_")
    need(summary.get("acknowledged") is False and typed_equal(summary.get("exit_code"), expected_exit(case)),
         "exact unacknowledged accounting refusal summary/status")
    delayed = only(events, "accounting_late_response")
    need(delayed["stage"] == stage and delayed["scope"] == "API_RESPONSE_INJECTION" and
         delayed["injection_start"] < delayed["deadline_mono"] < delayed["injection_end"], "measured real crossing, not requested delay")
    if stage != "post_end":
        failed = only(events, "actual_accounting_exception")
        need(typed_equal(failed["observation"], last) and last["retained"] is True and last["returned"] is False and
             last["mono_observed"] > delayed["deadline_mono"] and error_text(failed["error"]) == "DEADLINE_EXCEEDED after accounting",
             "ORIGINAL source accounting completion failed, actual resource acquisition retained before the failure")
        need(typed_equal(delayed["raw_free"], value["last_native_free"]), "actual late native resource return retained")
    else:
        need(last["retained"] is True and last["returned"] is True and typed_equal(last["resources"], end), "successful original end not erased by later failure")
    finals = [row for row in observations if row["phase"] == "FINAL" and not row["inside_helper"]]
    expected_count = {"pre_payload": 1, "pre_b": 2, "pre_end": 3, "post_end": 3}[stage]
    need(len(finals) == expected_count, "exact final accounting stage count")
    if stage in ("pre_payload", "pre_b"):
        need(b is None and end is None and (payload is None if stage == "pre_payload" else integer(payload)), "honest unavailable payload/b/end stages")
        need(summary.get("reason") == "FINALIZATION_FAILED" and summary.get("error_code") == "DEADLINE_EXCEEDED",
             "exact original finalization refusal")
        need(not os.path.lexists(cfg["receipt"]) and not os.path.lexists(cfg["settlement_record"]), "no fabricated publications")
        if stage == "pre_b":
            captured = only(events, "pre_b_record_artifact")
            facts, raw = regular(run + "/scratch/pre-b-record.json", 3 << 20)
            need(typed_equal(facts, {k: captured["artifact"][k] for k in facts}), "actual exclusive pre-b source record capture")
            rec = decode(raw)
            rb = (json.dumps(rec, sort_keys=True, indent=1, allow_nan=False) + "\n").encode()
            sb = (json.dumps({"supervisor": "owned_supervisor_v19", "config_sha256": outcome["bindings"]["config"]["sha256"],
                             "settlement": rec["settlement"], "receipt": cfg["receipt"], "receipt_sha256": sha(rb),
                             "child_returncode": rec["child_returncode"], "failure_codes": sorted(outcome["source_state"]["failure_codes"]),
                             "trips": list(outcome["source_state"]["trips"]), "authority": "only independent parent commit releases reservations"},
                            sort_keys=True, indent=1, allow_nan=False) + "\n").encode()
            need(len(rb) + len(sb) == payload and typed_equal(rec, outcome["source_state"]["rec"]), "independent exact source19 serialized buffers, no post-capture rewrite")
    else:
        need(resources(b) and (end is None if stage == "pre_end" else resources(end)) and integer(payload), "actual b/end stage availability")
        need(typed_equal(b, finals[1]["resources"]) and finals[1]["returned"] is True, "b is actual successful historical second final observation")
        if stage == "post_end":
            post = only(events, "post_end_accounting_state")
            need(typed_equal(post["accounting"]["ack_resources"], end) and typed_equal(end, finals[2]["resources"]), "actual successful historical end retained")
        need(summary.get("reason") == "ACK_REFUSED" and summary.get("error_code") == "DEADLINE_EXCEEDED", "exact source19 ACK refusal")
        rf, rr = regular(cfg["receipt"])
        sf, sr = regular(cfg["settlement_record"])
        staged = regular(cfg["settlement_record"] + ".staged")[0]
        receipt, settlement = decode(rr), decode(sr)
        need(receipt["supervisor"] == "owned_supervisor_v19" and receipt["supervisor_sha256"] == SUP_SHA and
             receipt["config_sha256"] == outcome["bindings"]["config"]["sha256"] and settlement["receipt_sha256"] == rf["sha256"],
             "actual original source19 receipt/settlement body")
        need(rf["bytes"] + sf["bytes"] == payload and sf["inode"] == staged["inode"] and sf["nlink"] == 2 and
             summary.get("receipt_sha256") == rf["sha256"] and summary.get("settlement_record_sha256") == sf["sha256"],
             "actual exact publication bytes and original linked identity")


def fd_window(case, request, cfg, events):
    """Reconstruct the complete native closed-number ownership window, never a producer success label."""
    target, chain = FD_CHAINS[case]
    opened, stimulus, closed, end = (only(events, name) for name in
                                     ("descriptor_fault_window_begin", "descriptor_fault_stimulus", "native_owned_fd_close_stimulus", "descriptor_fault_window_end"))
    fd, old = stimulus["fd"], stimulus["original"]
    exact(integer(fd) and fd >= 3 and isinstance(old, dict) and set(old) == {"path", "inode", "mode"} and
          isinstance(old["inode"], list) and len(old["inode"]) == 2 and all(integer(n) and n >= 0 for n in old["inode"]) and
          integer(old["mode"]), "complete original source descriptor identity")
    need(stimulus["operation_target"] == target and stimulus["allocation_lock_held"] is True and
         integer(stimulus["source_close_observations_required"]) and
         stimulus["source_close_observations_required"] == sum(op == "native_close" for op, label in chain),
         "fixed source-close count and original allocation-lock ownership")
    need(opened.get("fd") == fd and opened.get("operation_target") == target and typed_equal(opened.get("original"), old) and
         typed_equal(opened.get("observed_inode"), old["inode"]) and typed_equal(opened.get("observed_mode"), old["mode"]) and
         opened["mono_before"] <= opened["mono_after"] <= opened["mono"] and
         opened.get("allocation_lock_held") is True and opened.get("output_lock_held") is True and
         typed_equal(opened.get("source_close_observations_required"), stimulus["source_close_observations_required"]) and
         opened["seq"] < closed["seq"] and opened["mono"] <= closed["mono_before"],
         "allocation/output locks enclose the actual native stimulus close and all subsequent original source calls")
    need(closed.get("fd") == fd and typed_equal(closed.get("original"), old) and closed.get("path") == old["path"] and
         "error" not in closed and closed.get("result") is None and closed["seq"] < stimulus["seq"] and
         closed["mono_after"] <= stimulus["mono"], "actual successful native stimulus close of the original descriptor")
    exact(end.get("fd") == fd and end.get("reason") == "all_expected_native_calls_completed" and
          type(end.get("closes_left")) is int and end["closes_left"] == 0 and end["seq"] > stimulus["seq"],
          "complete same-fd allocation-lock window through every required source close (missing/incomplete => HOLD)")
    rows = [v for v in events if stimulus["seq"] < v["seq"] < end["seq"] and v.get("fd") == fd and v["operation"] in FD_EVENTS]
    expected_ops = [op for native, label in chain for op in ("closed_number_unallocated_before_source_call", native)]
    exact([v["operation"] for v in rows] == expected_ops, "complete exact native/unallocated chain with no descriptor reuse inside window")
    for (native, label), observed, call in zip(chain, rows[::2], rows[1::2]):
        need(observed["operation_target"] == label and type(observed["native_errno"]) is int and observed["native_errno"] == 9 and
             type(call.get("error", {}).get("errno")) is int and call["error"]["errno"] == 9 and call["scope"] == "NATIVE_OBSERVATION" and
             stimulus["mono"] <= observed["mono"] <= call["mono_before"] <= call["mono_after"] <= call["mono"] <= end["mono"],
             "every selected native errno9 call has its own preceding same-fd unallocated fstat observation inside the lock window")
    if case.startswith("io_extra_"):
        begin = only(events, "extra_line_write_begin")
        spawns = [v for v in pick(events, "native_spawn_registered") if v["role"] == "child"]
        exact(len(spawns) == 1, "native child spawn for stdin descriptor ownership")
        pipes = [v for v in pick(events, "native_pipe") if v["spawn_role"] == "child" and v["seq"] < spawns[0]["seq"]]
        exact(len(pipes) == 3, "source19 child stdout/stdin/stderr pipe allocation inventory")
        need(begin["fd"] == fd and pipes[1]["fds"][1] == fd and pipes[1]["seq"] < begin["seq"] < closed["seq"] and
             old["path"] is None and stat.S_ISFIFO(old["mode"]) and
             not any(v.get("fd") == fd and v["seq"] > pipes[1]["seq"] and v["seq"] < closed["seq"] for v in pick(events, "native_close")),
             "fault closes the exact natively allocated child stdin write end used for this original extra line")
    elif target == "dirsync":
        need(old["path"] == cfg["output_roots"][0] == request["anchors"]["out"]["path"] and
             typed_equal(old["inode"], request["anchors"]["out"]["inode"]) and stat.S_ISDIR(old["mode"]),
             "dirsync fault owns the approved original output-directory descriptor; source19 has no later original root-FD close")
    else:
        created = [v for v in pick(events, "source_created_descriptor") if v["path"] == cfg["receipt"]]
        exact(len(created) == 1, "source's exclusive original receipt descriptor evidence")
        need(old["path"] == cfg["receipt"] and old["inode"] == created[0]["inode"] and stat.S_ISREG(old["mode"]) and
             created[0]["seq"] < closed["seq"] and (target == "readback" or created[0]["fd"] == fd),
             "publication fault descriptor belongs to the original source-created current-run receipt inode")
    # After the completed window a later proxied allocation may legitimately reuse the number.
    # A later source operation without such a fresh allocation exposes a missed original close/use => HOLD.
    allocated = False
    for row in events[end["seq"] + 1:]:
        if row.get("fd") != fd:
            continue
        if row["operation"] == "stimulus_number_reallocated":
            exact(row.get("window_closed") is True, "no allocation before the complete original close window")
            allocated = True
        elif row["operation"] in ("native_write", "native_fsync", "native_close", "native_read", "fixture_closes_source_owned_fd"):
            exact(allocated, "later source use/close of closed number without a fresh allocation => incomplete ownership window HOLD")
            if row["operation"] == "fixture_closes_source_owned_fd" or row["operation"] == "native_close" and "error" not in row:
                allocated = False
    return stimulus


def publication(case, request, cfg, events, summary, outcome):
    if case in PUB:
        if case != "io_pub_short_write":
            need(summary.get("acknowledged") is False and typed_equal(summary.get("exit_code"), expected_exit(case)),
                 "exact original unacknowledged publication refusal summary/status")
        if case.endswith("_error"):
            operation = case[len("io_pub_"):-len("_error")]
            stimulus = fd_window(case, request, cfg, events)
            native = {"readback": "native_read", "dirsync": "native_fsync"}.get(operation, "native_" + operation)
            errors = [v for v in pick(events, native) if v.get("fd") == stimulus["fd"] and v.get("error", {}).get("errno") == 9 and
                      stimulus["seq"] < v["seq"] < only(events, "descriptor_fault_window_end")["seq"]]
            need(bool(errors), "actual selected same-fd native EBADF return, not injected exception metadata")
            need(summary.get("error_code") == "OS_ERROR_9", "exact original native-error branch code")
            expected_reason = "SETTLEMENT_OR_DIRECTORY_SYNC_FAILED" if operation == "dirsync" else "RECEIPT_PUBLICATION_FAILED"
            need(summary.get("reason") == expected_reason, "exact publication refusal stage")
        elif case.endswith("_late"):
            operation = case[len("io_pub_"):-len("_late")]
            delayed = only(events, "declared_response_delay")
            armed = only(events, "late_boundary_armed")
            need(armed["operation_target"] == operation and armed["seq"] < delayed["seq"] and
                 armed["deadline_mono"] == delayed["deadline_mono"] and armed["mono"] <= delayed["native_before"],
                 "original shared deadline armed immediately before the selected native call")
            need(delayed["scope"] == "API_RESPONSE_INJECTION" and delayed["operation_target"] == operation and
                 delayed["native_before"] <= delayed["native_after"] <= delayed["injection_start"] < delayed["deadline_mono"] < delayed["injection_end"],
                 "real measured native call plus declared response crossing; not native-latency coverage")
            need(summary.get("error_code") == "DEADLINE_EXCEEDED", "late native/API completion rejected by original deadline check")
            need(summary.get("reason") == ("SETTLEMENT_OR_DIRECTORY_SYNC_FAILED" if operation == "dirsync" else "RECEIPT_PUBLICATION_FAILED"), "exact late publication refusal stage")
        elif case == "io_pub_readback_mismatch":
            changed = only(events, "native_readback_bytes_mutated")
            need(changed["native_pwrite_return"] == 1 and changed["offset"] == 0 and summary.get("reason") == "RECEIPT_PUBLICATION_FAILED" and
                 summary.get("error_code") == "PUBLICATION_READBACK_MISMATCH", "native same-length changed bytes caught by original readback")
            facts, raw = regular(cfg["receipt"])
            need(facts["inode"] == changed["target_inode"] and facts["bytes"] == changed["original"]["bytes"] and
                 facts["sha256"] != changed["original"]["sha256"] and raw[:1].hex() == changed["replacement_byte_hex"], "actual mutated owned artifact")
        else:
            short = only(events, "short_write_response")
            need(short["scope"] == "API_RESPONSE_INJECTION" and 0 < short["native_return"] == short["native_argument_bytes"] < short["caller_bytes"], "honest shorter-argument response, not native spontaneous short-write claim")
            need(summary.get("acknowledged") is True and typed_equal(summary.get("exit_code"), 0) and summary.get("settlement") == "SETTLED" and
                 "reason" not in summary and "error" not in summary and "error_code" not in summary and summary.get("failure_codes") == [] and
                 typed_equal(summary.get("child_returncode"), 0),
                 "original write_all completed all bytes with the exact clean SETTLED ACK0 summary and no source error")
            facts, raw = regular(cfg["receipt"])
            need(facts["sha256"] == summary.get("receipt_sha256") and facts["bytes"] == summary.get("receipt_bytes"), "complete real short-response publication")
    if case == "io_staged_same_content":
        replacement = only(events, "archive_replace")
        old, new, archive = replacement["original"], replacement["replacement"], replacement["archive"]
        staged_return = only(events, "original_staged_publish_return")
        need(staged_return["inode"] == old["inode"] == archive["inode"] and staged_return["sha256"] == old["sha256"] and
             staged_return["path"] == cfg["settlement_record"] + ".staged" and staged_return["seq"] < replacement["seq"],
             "archived staged object is the source's own publish-returned original inode")
        need(old["sha256"] == new["sha256"] == archive["sha256"] and old["inode"] == archive["inode"] != new["inode"], "same-content staged replacement retains original inode")
        actual_archive, _ = regular(ROOT + "/" + case + "/scratch/staged.original")
        need(archive["path"] == actual_archive["path"] and all(typed_equal(actual_archive[k], archive[k]) for k in ("path", "inode", "sha256", "bytes", "nlink")) and
             actual_archive["inode"] == staged_return["inode"] and actual_archive["sha256"] == staged_return["sha256"] and
             actual_archive["bytes"] == staged_return["bytes"] == old["bytes"] and actual_archive["nlink"] == 1,
             "independently reopened fixed fresh archive is the source's preserved publish-returned original inode/content/link count")
        staged, _ = regular(cfg["settlement_record"] + ".staged")
        final, _ = regular(cfg["settlement_record"])
        need(staged["inode"] == final["inode"] == new["inode"] and final["nlink"] == 2 and archive["nlink"] == 1, "actual linked replacement not original staged inode")
        need(summary.get("acknowledged") is False and typed_equal(summary.get("exit_code"), 13) and
             summary.get("reason") == "SETTLEMENT_OR_DIRECTORY_SYNC_FAILED" and summary.get("error_code") == "SETTLEMENT_LINK_MISMATCH", "original staged identity guard refuses same bytes")


def authorization_case(case, events, summary, request, cfg, outcome):
    changed = only(events, "authorization_copy_mutated")
    phase = case.rsplit("_", 1)[1]
    action = "revoke" if "_revoke_" in case else "replace"
    need(changed["phase"] == phase and changed["action"] == action, "exact preceding-preparation mutation phase and declared action")
    archive = only(events, "archive_replace")
    wanted = request["created_facts"]["GO"]
    need(all(archive["original"][k] == wanted[k] for k in ("path", "inode", "sha256", "bytes", "nlink")) and
         archive["archive"]["inode"] == wanted["inode"] and archive["archive"]["sha256"] == wanted["sha256"] and
         archive["seq"] < changed["seq"], "only approved fresh GO copy archived before its mutation event; original approval untouched")
    # Independently derive the one exact replacement/revocation, not a reported mutation-success label.
    run = ROOT + "/" + case
    old_facts, old_raw = regular(run + "/GO.archived.json")
    new_facts, new_raw = regular(run + "/GO.json")
    expected_go = dict(decode(old_raw))
    if action == "revoke":
        expected_go["decision"] = "HOLD"
    else:
        expected_go["fixture_binding_revision"] = "fixed-replacement-not-parent-approval"
    need(typed_equal(decode(new_raw), expected_go) and new_raw == packed(expected_go) and
         all(typed_equal(old_facts[k], wanted[k]) for k in ("inode", "sha256", "bytes", "nlink")) and
         all(typed_equal(new_facts[k], archive["replacement"][k]) for k in ("path", "inode", "sha256", "bytes", "nlink")) and
         new_facts["inode"] != old_facts["inode"] and new_facts["nlink"] == 1,
         "actual original/replacement bytes and inodes implement only the frozen revoke or binding replacement")
    reads = [v for v in events if v["seq"] > changed["seq"] and v["operation"] in
             ("final_binding_read_begin", "final_binding_read_return", "final_binding_read_exception")]
    exact(len(reads) >= 2, "actual original final authorization reread after mutation")
    begin, refusal = reads[:2]
    expected = "GO_NOT_FOR_ITEM" if action == "revoke" else "AUTHORIZATION_CHANGED"
    need(begin["operation"] == "final_binding_read_begin" and refusal["operation"] == "final_binding_read_exception" and
         begin["after_mutation"] is True and refusal["after_mutation"] is True and
         begin["phase"] == refusal["phase"] and begin["inside_helper"] is refusal["inside_helper"] and
         refusal["error"]["type"] == "GuardError" and error_text(refusal["error"]) == expected,
         "first post-mutation original binding reread is the exact phase-matching refusal; no later refusal substitutes")
    # The trigger is the last relevant preparation event before archive, not merely changed.phase="main".
    gates = [v for v in events if v["seq"] < archive["seq"] and v["operation"] in
             ("native_pipe", "actual_accounting_return", "final_binding_read_begin", "final_binding_read_return",
              "final_binding_read_exception", "source_commit_return", "native_spawn_registered")]
    exact(bool(gates), "selected original preparation completion before mutation")
    prep = gates[-1]
    children = [v for v in pick(events, "native_spawn_registered") if v["role"] == "child"]
    if phase in ("helper", "main"):
        role = "helper" if phase == "helper" else "child"
        need(prep["operation"] == "native_pipe" and prep["spawn_role"] == role and
             number(prep["mono_before"]) and number(prep["mono_after"]) and prep["mono_after"] <= archive["mono"] and
             isinstance(prep["fds"], list) and len(prep["fds"]) == 2 and all(integer(fd) and fd >= 3 for fd in prep["fds"]) and
             begin["inside_helper"] is (phase == "helper") and (phase == "helper" or begin["phase"] == "PRE_GO"),
             "exact native helper/main preparation pipe completed before mutation and phase-specific protected reread")
        following = [v for v in pick(events, "native_pipe") if changed["seq"] < v["seq"] < begin["seq"]]
        need(len(following) == (0 if phase == "helper" else 2) and all(v["spawn_role"] == "child" for v in following) and
             not any(v["seq"] < begin["seq"] for v in children), "helper versus main source pipe inventory and no prior child launch")
    elif phase == "go":
        native = [v for v in pick(events, "native_fstatvfs") if v["seq"] < prep["seq"]]
        exact(bool(native), "pre-GO native accounting acquisition")
        actual = native[-1]
        need(len(children) == 1 and children[0]["seq"] < actual["seq"] < prep["seq"] < archive["seq"] and
             prep["operation"] == "actual_accounting_return" and prep["stage"] is None and
             actual["phase"] == "PRE_GO" and actual["accounting_stage"] is None and
             prep["resources"]["free"] == actual["raw"]["free"] and
             prep["last_accounting_observation"]["phase"] == "PRE_GO" and prep["last_accounting_observation"]["returned"] is True and
             outcome["source_state"]["rec"]["pre_go_census"]["mono_complete"] <= actual["mono_before"] and
             begin["phase"] == "PRE_GO" and begin["inside_helper"] is False,
             "GO mutation after actual post-spawn pre-GO census/accounting return and before its final authorization reread")
    else:
        state = outcome["source_state"]
        censuses = [c for c in state["reconciliation"]["census_observations"] if c["phase"] == "FINAL" and c["inside_helper"] is False and
                    number(c["mono_start"]) and number(c["mono_complete"]) and prep["mono"] <= c["mono_start"] <= c["mono_complete"] <= archive["mono"]]
        need(prep["operation"] == "actual_accounting_return" and prep["stage"] == "pre_end" and resources(state["accounting"]["ack_resources"]) and
             typed_equal(prep["resources"], state["accounting"]["ack_resources"]) and bool(censuses) and
             censuses[-1]["complete"] is True and censuses[-1]["incomplete_n"] == 0 and
             begin["phase"] == "FINAL" and begin["inside_helper"] is False,
             "ACK mutation follows the original completed native ACK census after successful end accounting, before its FINAL reread")
    need(prep["seq"] < archive["seq"] < changed["seq"] < begin["seq"] < refusal["seq"],
         "selected original preparation completion < archive/mutation < matching final reread/refusal")
    forbidden_commit = {"helper": "HELPER", "main": "LAUNCH", "go": "GO", "ack": "ACK"}[phase]
    need(not any(v["seq"] > changed["seq"] and v["phase"] == forbidden_commit for v in pick(events, "source_commit_return")), "superseded binding never committed")
    if phase in ("helper", "main"):
        role = "helper" if phase == "helper" else "child"
        need(not any(v["seq"] > changed["seq"] and v["role"] == role for v in pick(events, "native_spawn_registered")), "no spawn under superseded authority")
    need(summary.get("acknowledged") is False and typed_equal(summary.get("exit_code"), 14) and
         summary.get("reason") == "ACK_REFUSED" and summary.get("error_code") == expected,
         "exact final source ACK refusal, no success under replaced/revoked binding")
    state = outcome["source_state"]
    expected_failures = set(EXPECTED_FAILURES[case])
    if case in CONDITIONAL_OUTPUT and state["rec"]["artifacts"].get(cfg["outputs"][0]["path"]) is None:
        expected_failures.add("REQUIRED_OUTPUT_MISSING")  # Only the explicitly frozen conditional, from ORIGINAL source map.
    need(set(state["failure_codes"]) == expected_failures and state["trips"] == {}, "exact causally derived authorization failure set, no unrelated extras")
    if phase != "ack":
        need(state["go_delivered"] is not True and state["rec"].get("go_write_attempted") is not True,
             "refused helper/main/GO boundary never attempted or delivered GO")
    else:
        healthy_native_baseline(cfg, request, outcome, events)


def method_cases(case, cfg, request, outcome, events):
    result = outcome["source_outcome"]
    exact(result.get("mode") == "ORIGINAL_METHOD_ONLY" and result.get("original_main_called") is False, "method-only raw source scope")
    if case == "io_channel_certificate_extra":
        value = only(events, "held_exact_parser_observation")
        raw = regular(PATHS["held_consumer"], 2 << 20)[1]
        need(value["source_sha256"] == HELD_SHA and value["ast_lines"] == [84, 85] and
             value["ast_source_utf8_hex"] == b"".join(raw.splitlines(keepends=True)[83:85]).hex() and
             value["input_wire_hex"] == b"GO\nEXTRA\n".hex(), "exact held original parser AST and controlled native pipe input")
        need(value["actual_parser_outcome"] == "fallthrough" and value["actual_parser_systemexit"] is None and
             value["unread_suffix_hex"] == b"EXTRA\n".hex(), "known held consumer defect reproduced without NumPy/assay import")
        # REQUIRED strict rejection is false. This can NEVER become fixture MET
        # for this held SHA merely because fallthrough matched an observation.
        MISSING.append("HELD_CONSUMER_STRICT_EOF_REJECTION_FALSE_REQUIRES_ACTUALLY_ADMITTED_SUCCESSOR")
        return
    if case == "io_different_device":
        if request["different_device"] is None:
            MISSING.append("INDEPENDENTLY_APPROVED_EXISTING_GENUINELY_DIFFERENT_DEVICE_DIRECTORY")
            need(result["exception"] is None, "no fabricated different-device failure without prerequisite")
            return
        value = only(events, "different_device_readonly_preflight")
        fd = directory(request["different_device"]["path"])
        try:
            actual = inode(fd)
        finally:
            os.close(fd)
        need(value["actual_inode"] == actual == request["different_device"]["inode"], "actual approved readonly directory identity")
        if actual[0] == request["anchors"]["charge"]["inode"][0]:
            MISSING.append("SUPPLIED_DIRECTORY_NOT_GENUINELY_DIFFERENT_DEVICE")
            return
        need(error_text(result["exception"]) == "LANE_CWD_DIFFERENT_VOLUME", "actual original readonly native method different-volume refusal")
        return
    error = result.get("exception")
    exact(error is not None, "original method must actually refuse")
    message = error_text(error)
    if case in ("io_root_swap", "io_subtree_swap"):
        swap = only(events, "native_directory_replacement")
        anchor = "charge" if case == "io_root_swap" else "out"
        need(swap["original_inode"] == request["anchors"][anchor]["inode"] and swap["replacement_inode"] != swap["original_inode"], "approved original native directory actually replaced")
        fd = directory(swap["archive"])
        try:
            need(inode(fd) == swap["original_inode"], "only own original archived, not deleted")
        finally:
            os.close(fd)
        original_marker = regular(swap["archive"] + "/fixture-marker.txt")[0]
        replacement_marker = regular(swap["target"] + "/fixture-marker.txt")[0]
        need(original_marker["sha256"] == replacement_marker["sha256"] and original_marker["inode"] != replacement_marker["inode"], "same-content fresh directory marker identities")
        need(message == ("LANE_ANCHOR_CHANGED" if case == "io_root_swap" else "CHARGED_ANCHOR_CHANGED " + cfg["output_roots"][0]), "exact original anchor guard exception")
        return
    if case in TYPE_GO + TYPE_PREP + NEGATIVE_KEYS:
        expected = "GO_BINDING_MISMATCH" if case in TYPE_GO else "CREATION_PREPARATION_ALLOCATION_OR_INTERPRETER" if case in TYPE_PREP else "MUTATION_NEGATIVE_GO_NOT_EXPLICIT"
        need(error["type"] == "GuardError" and message == expected, "exact source19 typed authority/negative-key refusal")
        if case in TYPE_PREP:
            need(bool(pick(events, "final_binding_read_return")) and bool(pick(events, "original_manifest_exception")),
                 "valid GO first, ORIGINAL creation manifest then rejects typed preparation allocation")
        return
    expected = {"io_channel_wrong_purpose": "creation channel is restricted to declared mutation qualification negatives",
                "io_channel_wrong_scenario": "creation channel is restricted to declared mutation qualification negatives",
                "io_channel_wrong_target": "creation channel target/preparation is not the fixed current-run fixture",
                "io_channel_missing_schema": "creation channel is restricted to declared mutation qualification negatives",
                "io_channel_extra_schema": "creation channel is restricted to declared mutation qualification negatives",
                "io_channel_malformed": "invalid config type: creation_channel",
                "io_channel_missing_negative": "MUTATION_NEGATIVE_GO_NOT_EXPLICIT",
                "io_channel_wrong_negative": "MUTATION_NEGATIVE_GO_NOT_EXPLICIT",
                "io_channel_numeric_boolean": "MUTATION_NEGATIVE_GO_NOT_EXPLICIT",
                "io_channel_preparation_digest": "CREATION_PREPARATION_BINDING_CHANGED"}[case]
    need(message == expected and error["type"] == ("GuardError" if expected.isupper() else "ValueError"), "exact pinned source schema/authorization refusal")
    channel = cfg["creation_channel"]
    if case == "io_channel_wrong_target":
        need(channel.get("target_path") == ROOT + "/" + case + "/fixed-forbidden-target.txt" and
             not os.path.lexists(channel["target_path"]), "fixed wrong target never opened/created")
    elif case == "io_channel_numeric_boolean":
        go = decode(regular(request["go_original"]["path"])[1])
        need(type(go["qualification_negative"]["creation_channel"]) is int and go["qualification_negative"]["creation_channel"] == 1,
             "numeric1 not bool true, exact defect retained")


def child_report(cfg, request, outcome, events, mode):
    facts, raw = regular(cfg["outputs"][0]["path"], 1 << 20)
    value = decode(raw)
    keys = {"kind", "case", "mode", "scope", "approval_sha256", "owner", "base_source_sha256", "base_pin_fixture_sha256",
            "protocol", "manifest", "method_return", "method_exception", "ordinary_extra_probe", "observations", "unresolved",
            "selected_status_not_actual_exit", "observed_maxrss_bytes"}
    exact(isinstance(value, dict) and set(value) == keys and value["kind"] == "rqls10-matrix-io-child-outcome-v1" and
          value["base_source_sha256"] == BASE_SHA, "complete actual fixed child report schema (absent/partial => HOLD)")
    state = outcome["source_state"]
    spawns = [v for v in pick(events, "native_spawn_registered") if v["role"] == "child"]
    exact(len(spawns) == 1, "exact native registered child for report")
    spawn = spawns[0]
    owner = value["owner"]
    exact(isinstance(owner, dict) and set(owner) == {"pid", "pgid", "mono_entry", "mono_end"} and
          all(integer(owner[k]) and owner[k] > 1 for k in ("pid", "pgid")) and number(owner["mono_entry"]) and number(owner["mono_end"]),
          "complete child owner identity and invocation interval")
    need(value["case"] == request["case"] and value["mode"] == mode and value["scope"] == request["scope"] and
         value["approval_sha256"] == outcome["bindings"]["approval_sha256"] == spawn["child_external_sha_overlay"] and
         owner["pid"] == owner["pgid"] == spawn["pid"] == state["pid"] == state["group"],
         "report belongs to the intended case/approval/mode and native registered child owner, never another invocation")
    source_artifact = state["rec"]["artifacts"].get(cfg["outputs"][0]["path"])
    exact(isinstance(source_artifact, dict) and all(k in source_artifact for k in ("inode", "sha256", "bytes", "nlink")),
          "required child report present in ORIGINAL source artifact map (no oracle-added REQUIRED_OUTPUT_MISSING)")
    need(all(typed_equal(facts[k], source_artifact[k]) for k in ("inode", "sha256", "bytes", "nlink")) and facts["nlink"] == 1,
         "actual reopened child report digest/bytes/inode/links equals original source artifact observation")
    stdout = regular(cfg["stdout"], 1 << 20)[1].splitlines(keepends=True)
    exact(len(stdout) == 2 and all(v.endswith(b"\n") for v in stdout), "complete exact child owner+record stdout framing")
    first, record = (decode(row) for row in stdout)
    need(set(first) == {"kind", "pid", "pgid", "mono_begin", "scope"} and first.get("kind") == "rqls10-matrix-child-owner-v1" and
         typed_equal(first.get("pid"), owner["pid"]) and typed_equal(first.get("pgid"), owner["pgid"]) and
         first.get("mono_begin") == owner["mono_entry"] and first.get("scope") == "NATIVE_OWNER_RECORD",
         "child stdout original owner record joins intended native owner and module-entry time")
    need(set(record) == {"kind", "case", "selected_status_not_actual_exit", "report_sha256"} and
         record.get("kind") == "rqls10-matrix-io-child-record-v1" and record.get("case") == request["case"] and
         record.get("report_sha256") == facts["sha256"] and
         typed_equal(record.get("selected_status_not_actual_exit"), value["selected_status_not_actual_exit"]),
         "actual child stdout record binds this complete report digest and selected status, not another artifact")
    wait = state["reconciliation"].get("main_wait")
    exact(isinstance(wait, dict) and set(wait) == {"pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "mono_reaped", "epoch_reaped"} and
          integer(wait["pid"]) and integer(wait["raw_wait_status"]) and integer(wait["rc"]) and integer(state["rc"]) and
          integer(value["selected_status_not_actual_exit"]) and wait["leader_reaped"] is True and
          isinstance(wait["native_wait_result"], list) and len(wait["native_wait_result"]) == 2 and
          all(integer(x) for x in wait["native_wait_result"]) and number(wait["mono_reaped"]), "complete retained source native child wait observation")
    need(wait["pid"] == owner["pid"] and wait["native_wait_result"] == [owner["pid"], wait["raw_wait_status"]] and
         (os.WIFEXITED(wait["raw_wait_status"]) or os.WIFSIGNALED(wait["raw_wait_status"])) and
         os.waitstatus_to_exitcode(wait["raw_wait_status"]) == wait["rc"] == state["rc"] == value["selected_status_not_actual_exit"] and
         spawn["mono_before"] <= owner["mono_entry"] <= owner["mono_end"] <= wait["mono_reaped"] <= outcome["owner"]["mono_end"],
         "report status and owner bound to intended child's destructive native wait result; selected label alone never proves status")
    need(value["unresolved"] == [] and number(value["observed_maxrss_bytes"]) and value["observed_maxrss_bytes"] <= 256 << 20,
         "child finite ownership/resources")
    return value


def retained_source_telemetry(cfg, outcome):
    recon = outcome["source_state"]["reconciliation"]
    exact(recon["timing_failed"] is False and recon["raw_acquisitions"] == [], "healthy source timing has no unavailable raw acquisitions")
    tape, history = recon["identity_events"], recon["identity_history"]
    exact(isinstance(tape, list) and isinstance(history, list), "complete original identity tape/history")
    entries = {row["first_identity"]["uniqueid"]: row for row in history}
    exact(len(entries) == len(history), "unique identity-history entries")
    counts, positions = {}, {}
    for ref, row in enumerate(tape, 1):
        exact(isinstance(row, list) and len(row) == 6 and all(integer(row[k]) for k in (0, 1, 2)) and
              number(row[3]) and number(row[4]) and row[3] <= row[4] and type(row[5]) is bool and row[0] in entries,
              "source19 identity event types/acquisition interval")
        exact(0 <= row[1] < len(entries[row[0]]["variants"]), "actual variant reference")
        uid = row[0]
        counts[uid] = counts.get(uid, 0) + 1
        if uid not in positions:
            positions[uid] = {"first": ref, "last": ref}
        else:
            # Same sequential rule as source19: first strict smaller end; last greater-or-equal end.
            if row[4] < tape[positions[uid]["first"] - 1][4]:
                positions[uid]["first"] = ref
            if row[4] >= tape[positions[uid]["last"] - 1][4]:
                positions[uid]["last"] = ref
    def reference(identity, ref):
        exact(integer(ref) and 1 <= ref <= len(tape), "canonical identity reference")
        row = tape[ref - 1]
        need(row[0] == identity["uniqueid"] and typed_equal(dict(entries[row[0]]["variants"][row[1]], status=row[2]), identity),
             "full original identity/status matches canonical event")
        return row
    for uid, entry in entries.items():
        need(integer(entry["observations"]) and entry["observations"] == counts.get(uid, 0), "identity event count independently reconstructed")
        for role in ("first", "last"):
            row = reference(entry[role + "_identity"], entry[role + "_event_ref"])
            need(entry[role + "_event_ref"] == positions.get(uid, {}).get(role) and
                 entry["mono_" + role + "_begin"] == row[3] and entry["mono_" + role + "_seen"] == row[4],
                 "independently reconstructed actual first/last tape positions and acquisition intervals; reversed endpoints never pass")
    for owned in recon["owned_identities"]:
        reference(owned["identity"], owned["identity_event_ref"])
    for helper in recon["helpers"]:
        exact(helper["identity"] is not None and helper["identity_event_ref"] is not None,
              "mandatory actual helper retained identity and canonical reference")
        reference(helper["identity"], helper["identity_event_ref"])
    for census in recon["census_observations"]:
        for identities, refs in (("owned_live", "owned_event_refs"), ("unproved_live", "unproved_event_refs")):
            exact(len(census[identities]) == len(census[refs]), "complete census event references")
            for identity, ref in zip(census[identities], census[refs]):
                reference(identity, ref)
        for measurement in census["measurements"]:
            measured = measurement["identity"]
            reference(measured, measurement["identity_event_ref"])
            ref = measurement["before_task_event_ref"]
            exact(integer(ref) and 1 <= ref <= len(tape), "canonical strict 1-based before-task reference; zero/negative indexing forbidden")
            before = tape[ref - 1]
            before_identity = dict(entries[before[0]]["variants"][before[1]], status=before[2])
            after = reference(measurement["identity_after"], measurement["identity_after_event_ref"])
            need(before[0] == measured["uniqueid"] == measurement["identity_after"]["uniqueid"] and
                 all(typed_equal(before_identity[k], measured[k]) and typed_equal(measured[k], measurement["identity_after"][k]) for k in FINGERPRINT) and
                 ref < measurement["identity_after_event_ref"] and
                 before[4] <= measurement["mono_task_begin"] <= measurement["mono_task_end"] <= after[3] <= after[4] <= measurement["mono_observed"] and
                 measurement["identity_after_interval"] == after[3:5], "same measured incarnation at canonical before/task/after references and compatible native brackets")
    fields = {"bytes_seen", "bytes_written", "cap_bytes", "overflow", "write_inflight", "pending_bytes", "closed", "error",
              "sha256_prefix", "prefix_bytes", "hash_pending", "sha256_written", "mono_created", "mono_last_update",
              "mono_last_read", "mono_last_write", "mono_eof", "mono_close_completed", "eof_seen", "fsync_returned", "out_closed", "pipe_closed"}
    exact(isinstance(recon["streams"], dict) and set(recon["streams"]) == {"stdout", "stderr"},
          "mandatory exact stdout/stderr stream proof inventory; empty/omitted rows are required-proof HOLD")
    for name, row in recon["streams"].items():
        facts, raw = regular(cfg[name], 1 << 20)
        exact(name in ("stdout", "stderr") and set(row) == fields, "source19 stream schema")
        exact(all(integer(row[k]) and row[k] >= 0 for k in ("bytes_seen", "bytes_written", "cap_bytes", "pending_bytes", "prefix_bytes")) and
              all(type(row[k]) is bool for k in ("overflow", "write_inflight", "closed", "hash_pending", "eof_seen", "fsync_returned", "out_closed", "pipe_closed")), "strict stream scalar types")
        need(row["bytes_seen"] == row["bytes_written"] == row["prefix_bytes"] == facts["bytes"] and row["pending_bytes"] == 0 and
             row["sha256_prefix"] == row["sha256_written"] == facts["sha256"] and row["closed"] is True and row["error"] is None and
             row["overflow"] is False and row["write_inflight"] is False and row["hash_pending"] is False and
             row["eof_seen"] is True and row["fsync_returned"] is True and row["out_closed"] is True and row["pipe_closed"] is True,
             "actual sink byte/hash/EOF/fsync/close facts; no null normalization")


def healthy_native_baseline(cfg, request, outcome, events):
    retained_source_telemetry(cfg, outcome)
    state = outcome["source_state"]
    need(state["failure_codes"] == [] and state["trips"] == {} and state["rc"] == 0,
         "no unrelated failure/trip/nonzero-child outcome excused by an expected publication status")
    report = child_report(cfg, request, outcome, events, "wire")
    need(report["case"] == request["case"] and report["mode"] == "wire" and
         report["approval_sha256"] == outcome["bindings"]["approval_sha256"] and
         report["owner"]["pid"] == state["pid"] and report["owner"]["pgid"] == state["group"] and
         report["method_exception"] is None and report["selected_status_not_actual_exit"] == 0,
         "actual fixed wire child report/identity/source WNOHANG status")
    protocol = report["protocol"]
    need(protocol["bytes"] == 3 and protocol["sha256"] == sha(b"GO\n") and protocol["eof"] is True and
         protocol["error"] is None and protocol["creation_line_bytes"] is None and report["manifest"] is None,
         "all healthy baseline cases retain actual original ordinary GO+EOF")
    completion = state["rec"]["go_delivery_completion"]
    spawn = state["rec"]["mono_spawn"]
    need(state["go_delivered"] is True and completion["spawn_age_s"] == completion["mono"] - spawn and
         completion["spawn_age_bound_s"] == min(60.0, cfg["max_wall_s"] / 2.0) and
         completion["spawn_age_s"] <= completion["spawn_age_bound_s"] and
         completion["remaining_main_runtime_s"] == spawn + cfg["max_wall_s"] - completion["mono"] > 0,
         "actual original delivered-GO completion age and runtime, not requested delay")
    final = state["rec"]["final_census"]
    need(final["complete"] is True and final["incomplete_n"] == 0 and final["owned_live"] == [] and
         final["unproved_live"] == [] and final["group_live"] == [],
         "no unresolved native source final coverage/blocker excused")
    helpers, log = state["reconciliation"]["helpers"], state["reconciliation"]["helper_log"]
    spawns = [row for row in pick(events, "native_spawn_registered") if row["role"] == "helper"]
    exact(isinstance(log, list) and len(helpers) >= 3 and len(log) >= 3 and len(spawns) >= 3,
          "mandatory actual admission/start/end /bin/date helper proof inventory, not an empty collection")
    need(len(helpers) == len(log) == len(spawns) == 3 and [row.get("purpose") for row in log] == ["admission", "start", "end"] and
         all(row.get("outcome") == "OK" and row.get("pid") == helper["pid"] == spawn["pid"] and
             typed_equal(helper["mono_pid_registered"], spawn["mono_pid_registered"]) and
             number(helper["mono_spawn"]) and spawn["mono_before"] <= helper["mono_spawn"] <= helper["mono_pid_registered"] <= spawn["mono_after"]
             for row, helper, spawn in zip(log, helpers, spawns)), "exact three successful real metadata helpers joined to native spawn registration and retained identity")
    for helper in helpers:
        need(helper["leader_reaped"] is True and helper["rc"] == 0 and helper["wait_lost"] is False and
             helper["identity"] is not None and helper["identity"]["pid"] == helper["pid"] == helper["identity"]["pgid"] and
             helper["stdout_closed"] is True and helper["eof_proved"] is True and helper["group_clear"] is True and
             helper["descendants_clear"] is True and helper["proof"]["complete"] is True and
             helper["proof"]["owned_live"] == [] and helper["proof"]["unproved_live"] == [] and
             helper["capture_hex"] == (helper["date"] + "\n").encode("ascii").hex(),
             "actual retained owned /bin/date status/identity/EOF/native capture and closure")
    return report


def mutation(case, request, cfg, outcome, events, summary):
    replaced = only(events, "target_replaced_before_mutation")
    original, archive, replacement = (replaced[k] for k in ("original", "archive", "replacement"))
    need(original["inode"] == archive["inode"] != replacement["inode"] and
         original["sha256"] == archive["sha256"] == replacement["sha256"] and original["bytes"] == archive["bytes"] == replacement["bytes"],
         "actual same-content replacement and immutable own original archive")
    need(replacement["inode"] == request["created_facts"]["replacement"]["inode"] and request["created_facts"]["replacement"]["bytes"] == 0 and
         ("_pin_" not in case or request["created_facts"]["replacement"]["creation_ordinal"] < request["created_facts"]["pin"]["creation_ordinal"]),
         "approved older freshly created current-run replacement inode, never prior evidence")
    actual_old = regular(archive["path"])[0]
    actual_new = regular(replacement["path"])[0]
    need(all(actual_old[k] == original[k] for k in ("inode", "sha256", "bytes", "nlink")) and
         all(actual_new[k] == replacement[k] for k in ("inode", "sha256", "bytes", "nlink")), "refused BEFORE either inode append/mutation")
    if "_pin_" in case:
        need(all(original[k] == request["created_facts"]["pin"][k] for k in ("inode", "sha256", "bytes", "nlink")), "approved created pin descriptor facts")
    else:
        published = only(events, "original_launch_publish_return")
        need(original["inode"] == published["inode"] and original["sha256"] == published["sha256"] and original["bytes"] == published["bytes"], "source original launch publication-returned identity")
    if case.endswith("before_manifest"):
        refusal = only(events, "original_manifest_exception")
        need(refusal["seq"] > replaced["seq"] and error_text(refusal["error"]) == "ORIGINAL_CREATION_IDENTITY_CHANGED_BEFORE_GO", "actual source manifest refuses original-creation mismatch")
        state = outcome["source_state"]
        need(state["go_delivered"] is not True and state["rec"].get("go_write_attempted") is not True and
             "POST_SPAWN_FAILURE" in state["failure_codes"] and "GO_NOT_DELIVERED" in state["failure_codes"], "no GO commit under replaced original identity")
    else:
        manifest = only(events, "original_manifest_return")
        ready = only(events, "native_child_ready")
        barrier = only(events, "fixture_open_barrier_released")
        completed = only(events, "barrier_after_verified_go_completion")
        source_go = [v for v in pick(events, "original_completion_return") if v["phase"] == "GO"]
        need(len(source_go) == 1 and source_go[0]["seq"] < completed["seq"] < ready["seq"] and
             completed["completion"]["spawn_age_s"] <= completed["completion"]["spawn_age_bound_s"] and
             completed["completion"]["remaining_main_runtime_s"] > 0 and
             source_go[0]["mono_after"] - completed["pre_go_census_mono"] <= max(1, cfg["sample_s"]),
             "barrier AFTER actual original GO-age/completion and census freshness; no source threshold bypass")
        need(manifest["seq"] < ready["seq"] < replaced["seq"] < barrier["seq"] and 1 <= manifest["bytes"] <= 4096,
             "actual manifest delivery then replacement before separately controlled child open")
        report = child_report(cfg, request, outcome, events, "mutation")
        need(report["protocol"]["creation_manifest_sha256"] == manifest["sha256"] and report["protocol"]["eof"] is True,
             "actual received exact original manifest and EOF")
        need(report["method_return"] is None and error_text(report["method_exception"]) == "ORIGINAL_CREATION_INODE_HASH_SIZE_LINK_MISMATCH",
             "actual immutable child method rejected before write")
        opens = pick(report["observations"], "original_target_open")
        need(len(opens) == 1 and opens[0]["inode"] == replacement["inode"] and
             not pick(report["observations"], "original_target_write_return") and not pick(report["observations"], "original_target_write_error"),
             "native replacement descriptor opened, no mutation syscall attempted")
        need(report["selected_status_not_actual_exit"] == 3 and outcome["source_state"]["rc"] == 3, "source actual WNOHANG child exit3 joined to refusal")
    need(summary.get("acknowledged") is True and typed_equal(summary.get("exit_code"), expected_exit(case)) and
         summary.get("settlement") == ("SETTLED" if expected_exit(case) == 0 else "UNSETTLED") and
         "reason" not in summary and "error_code" not in summary,
         "exact source outcome/settlement, no accepted broad status set or contradictory source error")
    state = outcome["source_state"]
    if not case.endswith("before_manifest"):
        need(state["go_delivered"] is True and state["rec"].get("go_write_attempted") is True,
             "before-child-open mutation is bound to actual attempted/delivered source GO")
    expected_failures = set(EXPECTED_FAILURES[case])
    if case in CONDITIONAL_OUTPUT and state["rec"]["artifacts"].get(cfg["outputs"][0]["path"]) is None:
        expected_failures.add("REQUIRED_OUTPUT_MISSING")
    need(set(state["failure_codes"]) == expected_failures and state["trips"] == {}, "exact mutation refusal failure set, no unrelated failures/trips excused")


def post_ack(case, request, go, events, summary, capture, outcome, streams):
    crossing = only(events, "ack_flush_real_expiry_crossing")
    need(summary.get("acknowledged") is True and typed_equal(summary.get("exit_code"), 0) and summary.get("settlement") == "SETTLED" and
         summary.get("failure_codes") == [] and typed_equal(summary.get("child_returncode"), 0) and
         "reason" not in summary and "error" not in summary and "error_code" not in summary,
         "one actual clean SETTLED ACK0 without contradictory error/failure before terminal refusal")
    need(capture["actual_exit"] == 14 and outcome["source_outcome"].get("selected_source_return") == 14, "actual14 remains14, NEVER120")
    need(crossing["injection_start_epoch_raw"] < crossing["approved_expiry_epoch_raw"] == go["not_after_epoch"] < crossing["injection_end_epoch_raw"] and
         crossing["native_flush_before"] <= crossing["native_flush_after"] <= crossing["injection_start"] < crossing["injection_end"],
         "measured real approved expiry crossing, not requested flag")
    failures = pick(events, "stderr_native_error")
    exact(bool(failures), "source native stderr failure evidence")
    for value in failures:
        need(value["error"]["errno"] == 32 and value["native_argument_bytes"] == value["pending_bytes"] > 0 and
             value.get("native_argument_sha256") == value["pending_sha256"] and
             value["broken_fixture"] is True, "actual owned broken-pipe EPIPE native argument equals original pending bytes/digest")
    need(failures[0]["label"] == ("source_write" if case.endswith("write") else "source_or_interpreter_flush"), "exact write/flush failure boundary")
    retained = only(events, "stderr_owned_writer_retained_until_original_terminal")
    need(retained["stream_closed"] is False and retained["owner_pid"] == capture["pid"] and retained["native_inode"] is not None,
         "owned writer remains live until unchanged terminal; never mask shutdown by preclosing/restoring")
    if "persistent" in case:
        probes = [v for v in failures if v["label"].startswith("FIXTURE_POST_MAIN_PROBE_")]
        need(len(probes) == 2 and len(failures) == 3 and len({v["pending_sha256"] for v in failures}) == 1 and
             len({v["pending_bytes"] for v in failures}) == 1 and retained["pending_bytes"] > 0,
             "native fault and buffered bytes persist through all attempts to the original non-flushing terminal")
        attempted = only(events, "attempted_stderr_artifact")
        af, ar = regular(attempted["artifact"]["path"], 8 << 20)
        need(af["sha256"] == retained["pending_sha256"] == attempted["artifact"]["sha256"] and
             af["bytes"] == retained["pending_bytes"] and streams["stderr"] == b"" and
             all(v["pending_bytes"] == v["native_argument_bytes"] == af["bytes"] and
                 v["pending_sha256"] == v.get("native_argument_sha256") == af["sha256"] for v in failures) and
             failures[-1]["seq"] < retained["seq"] < attempted["seq"],
             "each actual EPIPE's pending/native argument is the exact terminal retained buffer and attempted artifact; never delivered stderr => parent release HOLD")
    else:
        need(len(failures) == 1 and len(pick(events, "stderr_one_shot_fault_consumed")) == 1, "exact one-shot native fault")
        recovery = only(events, "stderr_native_return")
        need(recovery["label"] == "FIXTURE_ONE_SHOT_RECOVERY_PROBE" and recovery["working_parent_sink"] is True and
             recovery["returned"] == failures[0]["pending_bytes"] and recovery["data_sha256"] == failures[0]["pending_sha256"] and
             sha(streams["stderr"]) == recovery["data_sha256"] and len(streams["stderr"]) == recovery["returned"] and retained["pending_bytes"] == 0,
             "fixed working sink after first fault; actual parent capture independently proves recovery")
        ar = streams["stderr"]
    diagnostic = decode(ar)
    need(diagnostic.get("kind") == "POST_ACK_REFUSAL_EVIDENCE" and diagnostic.get("exit_code") == 14 and
         diagnostic.get("error_code") == "AUTHORIZATION_EXPIRED_DURING_ACK" and outcome["source_state"]["ack_output_started"] is True,
         "exact actual source diagnostic; fixture recovery/attempt artifact never alters actual status or ACK count")


def extra_cases(case, request, cfg, go, outcome, events, summary):
    state = outcome["source_state"]
    begin, manifest = only(events, "extra_line_write_begin"), only(events, "original_manifest_return")
    line = bytes.fromhex(begin["raw_hex"])
    spawn = [v for v in pick(events, "native_spawn_registered") if v["role"] == "child"]
    exact(len(spawn) == 1 and number(state["rec"].get("mono_spawn")), "retained actual native child spawn time")
    need(begin["mono_spawn"] == state["rec"]["mono_spawn"] and
         spawn[0]["mono_before"] <= begin["mono_spawn"] <= spawn[0]["mono_after"] <= begin["mono"] and
         begin["age_bound"] == min(60.0, cfg["max_wall_s"] / 2.0),
         "initial second-line age uses retained native spawn and independently reconstructed original age bound")
    need(line == bytes.fromhex(manifest["raw_hex"]) and len(line) == begin["bytes"] == manifest["bytes"] <= 4096 and
         sha(line) == begin["sha256"] == manifest["sha256"] and begin["mono"] < begin["deadline_mono"] and
         begin["mono"] - begin["mono_spawn"] <= begin["age_bound"] and
         begin["mono"] - begin["pre_go_census_mono"] <= max(1, cfg["sample_s"]), "actual canonical second-line digest/bytes and valid original pre-write gates")
    decoded = decode(line)
    published = only(events, "original_launch_publish_return")
    expected_manifest = {"kind": "qualification-creation-manifest-v1", "scenario": "mutate_evidence",
                         "preparation_sha256": request["preparation"]["sha256"],
                         "run": request["anchors"]["run"], "output_root": request["anchors"]["out"],
                         "target": {"path": cfg["launch_record"], "inode": published["inode"], "sha256": published["sha256"],
                                    "bytes": published["bytes"], "nlink": 1}}
    need(typed_equal(decoded, expected_manifest) and packed(decoded) == line, "independently reconstructed ORIGINAL launch-creation manifest and canonical newline bytes")
    # All15 require the declared child parser outcome. A missing report cannot broaden the failure set.
    need(set(state["failure_codes"]) == set(EXPECTED_FAILURES[case]), "exact frozen source19 second-line failure set; no REQUIRED_OUTPUT_MISSING exception")
    need(set(state["trips"]) == ({"SUPERVISOR_CANCEL"} if case.startswith("io_extra_signal_") else set()), "exact source19 cancellation/trip set")
    delivered = case in DELIVERED
    need(state["rec"].get("go_write_attempted") is True and
         (state["go_delivered"] is True if delivered else state["go_delivered"] is None) and
         typed_equal(state["go_delivered"], state["rec"].get("go_delivered")),
         "exact actual source GO attempted/delivered flag, never inferred from GO_NOT_DELIVERED failure-code presence")
    write_errors, write_returns = pick(events, "extra_line_write_exception"), pick(events, "extra_line_write_return")
    failed_write = case in ("io_extra_write_zero", "io_extra_write_error", "io_extra_write_late", "io_extra_deadline")
    exact(len(write_errors) == int(failed_write) and len(write_returns) == int(not failed_write) and
          all(row.get("fd") == begin["fd"] for row in write_errors + write_returns), "complete exact selected extra-line write outcome on intended stdin fd")
    completions = [v for v in pick(events, "original_completion_return") if v["phase"] == "GO"]
    completion_errors = [v for v in pick(events, "original_completion_exception") if v["phase"] == "GO"]
    exact(len(completions) == int(case == "io_extra_write_short") and
          len(completion_errors) == int(delivered and case != "io_extra_write_short"),
          "exact GO completion invocation/outcome follows actual delivery, not a producer success label")
    if delivered:
        completion = state["rec"].get("go_delivery_completion")
        exact(isinstance(completion, dict) and set(completion) == {"mono", "spawn_age_s", "spawn_age_bound_s", "remaining_main_runtime_s"} and
              all(number(v) for v in completion.values()), "complete original actual GO-completion clock arithmetic")
        need(completion["spawn_age_s"] == completion["mono"] - begin["mono_spawn"] and
             completion["spawn_age_bound_s"] == begin["age_bound"] and
             completion["remaining_main_runtime_s"] == begin["mono_spawn"] + cfg["max_wall_s"] - completion["mono"] > 0 and
             (completion["spawn_age_s"] > begin["age_bound"] if case == "io_extra_go_age" else completion["spawn_age_s"] <= begin["age_bound"]),
             "original actual GO completion age/runtime and exact dominant age versus other source operation refusal")
    if case in ("io_extra_write_error", "io_extra_close_error"):
        fd_window(case, request, cfg, events)
        for code in ("POST_SPAWN_FAILURE", "STDIN_CLOSE_FAILED"):
            rows = [v for v in state["failures"] if v["code"] == code]
            need(len(rows) == 1 and isinstance(rows[0]["detail"], str) and rows[0]["detail"].startswith("OSError(9, "),
                 "original source failure detail retains actual selected native errno9 exception: " + code)
    native_writes = [v for v in pick(events, "native_write") if v.get("fd") == begin["fd"] and v.get("extra_line") is True and v["seq"] > begin["seq"]]
    if case == "io_extra_write_zero":
        need(native_writes == [], "explicit zero response made no native extra-line write")
    elif case == "io_extra_write_error":
        need(len(native_writes) == 1 and native_writes[0].get("error", {}).get("errno") == 9 and
             write_errors[0]["error"]["type"] == "OSError" and write_errors[0]["error"]["errno"] == 9,
             "actual selected source write exception is the retained native errno9, not a compatible category")
    else:
        need(bool(native_writes) and all("error" not in v and integer(v.get("result")) and 0 < v["result"] <= v["native_argument_bytes"] for v in native_writes) and
             all(begin["mono"] <= v["mono_before"] <= v["mono_after"] <= v["mono"] for v in native_writes) and
             sum(v.get("result", 0) for v in native_writes) == len(line), "actual native extra-line write counts/intervals total the complete original manifest after its source begin")
    if case == "io_extra_expiry":
        need(summary.get("acknowledged") is False and typed_equal(summary.get("exit_code"), 14) and
             summary.get("reason") == "ACK_REFUSED" and summary.get("error_code") == "GO_EXPIRED_AT_ACK", "actual expiry dominates final ACK")
    else:
        need(summary.get("acknowledged") is True and summary.get("exit_code") == expected_exit(case) and
             summary.get("settlement") == ("SETTLED" if case == "io_extra_write_short" else "UNSETTLED"), "exact source19 acknowledged fixture outcome")
    if case == "io_extra_write_zero":
        zero = only(events, "extra_zero_response")
        need(zero["fd"] == begin["fd"] and zero["result"] == 0 and zero["native_call_made"] is False and zero["scope"] == "API_RESPONSE_INJECTION" and
             write_errors[0]["error"]["type"] == "GuardError" and error_text(write_errors[0]["error"]) == "ZERO_PROGRESS_WRITE", "explicit API zero, exact original write_all exception")
    if case == "io_extra_write_short":
        short = only(events, "short_write_response")
        need(short["fd"] == begin["fd"] and short["extra_line"] is True and 0 < short["native_return"] == short["native_argument_bytes"] < short["caller_bytes"] and
             short["scope"] == "API_RESPONSE_INJECTION" and "error_code" not in summary and "error" not in summary and "reason" not in summary,
             "fixed short native argument, exact absence of source error; not spontaneous OS short write")
    if case in ("io_extra_write_late", "io_extra_deadline", "io_extra_close_late"):
        crossing = only(events, "accounting_late_response")
        need(crossing["fd"] == begin["fd"] and crossing["scope"] == "API_RESPONSE_INJECTION" and
             crossing["stage"] == ("extra_close" if case.endswith("close_late") else "extra_write") and
             crossing["native_before"] <= crossing["native_after"] <= crossing["injection_start"] < crossing["deadline_mono"] < crossing["injection_end"] <= crossing["mono"],
             "selected native stdin operation retained, measured API response crossing before its observation")
        error = completion_errors[0]["error"] if case == "io_extra_close_late" else write_errors[0]["error"]
        need(error["type"] == "GuardError" and error_text(error) ==
             ("DEADLINE_EXCEEDED after GO completion" if case == "io_extra_close_late" else "DEADLINE_EXCEEDED after write"),
             "declared exact DEADLINE_EXCEEDED source exception at selected write/close completion, not crossing plus broad failure code")
        if case == "io_extra_deadline":
            need(crossing["deadline_clamped"] is False and crossing["deadline_mono"] == crossing["original_deadline_mono"] == begin["deadline_mono"],
                 "original unmodified source GO deadline crossed, not the clamped response control")
    if case in ("io_extra_go_age", "io_extra_expiry"):
        crossing = only(events, "extra_real_crossing")
        age = case == "io_extra_go_age"
        expected_cutoff = begin["mono_spawn"] + min(60.0, cfg["max_wall_s"] / 2.0) if age else go["not_after_epoch"]
        exact(all(number(crossing.get(k)) for k in ("clock_begin_raw", "cutoff_value_raw", "clock_end_raw", "injection_start", "injection_end", "original_go_deadline")),
              "complete finite raw crossing interval/cutoff evidence")
        need(crossing["scope"] == "API_RESPONSE_INJECTION" and crossing["fd"] == begin["fd"] and
             crossing["cutoff"] == ("GO_AGE" if age else "AUTHORIZATION_EXPIRY") and
             typed_equal(crossing["cutoff_value_raw"], expected_cutoff) and
             crossing["clock_begin_raw"] < expected_cutoff < crossing["clock_end_raw"] and
             crossing["original_go_deadline"] == begin["deadline_mono"] and
             native_writes[-1]["mono_after"] <= crossing["injection_start"] <= crossing["injection_end"] <= crossing["mono"] < begin["deadline_mono"] and
             begin["seq"] < native_writes[-1]["seq"] < crossing["seq"] < write_returns[0]["seq"],
             "real crossing bound to actual source stdin operation and original spawn-age/approved expiry cutoff within invocation, before observation")
        if age:
            need(begin["mono"] <= crossing["clock_begin_raw"] <= crossing["injection_start"] and
                 crossing["clock_end_raw"] <= crossing["injection_end"] and expected_cutoff - crossing["clock_begin_raw"] <= 6.0,
                 "original real spawn+age boundary, measured mono endpoints and fixed six-second limit")
        else:
            need(typed_equal(state["reconciliation"]["authorization"]["not_after_epoch"], go["not_after_epoch"]) and
                 number(begin["epoch_raw"]) and number(crossing["epoch_raw"]) and
                 begin["epoch_raw"] <= crossing["clock_begin_raw"] < expected_cutoff < crossing["clock_end_raw"] <= crossing["epoch_raw"] and
                 expected_cutoff - crossing["clock_begin_raw"] <= request["parameters"]["max_flush_delay_s"],
                 "exact approved GO expiry (never an unrelated reported cutoff), within raw invocation epoch interval and declared maximum")
        closes = [v for v in pick(events, "native_close") if v.get("fd") == begin["fd"] and v["seq"] > write_returns[0]["seq"]]
        need(bool(closes) and "error" not in closes[0] and closes[0]["seq"] < completion_errors[0]["seq"] and
             completion_errors[0]["error"]["type"] == "GuardError" and error_text(completion_errors[0]["error"]) ==
             ("LATE_ACTUAL_GO_DELIVERY_OWNED_STOP" if age else "AUTHORIZATION_EXPIRED_DURING_GO"),
             "actual full-line write/real crossing/close then exact dominating original GO completion refusal")
    if case.startswith("io_extra_signal_"):
        sent = only(events, "extra_native_signal")
        name, boundary = case.split("_")[3:5]
        signum = SIGNALS[name]
        identities = (sent["identity_before"], sent["identity_checked"])
        exact(all(isinstance(p, dict) and set(p) == IDENTITY_KEYS and
                  all(integer(p[k]) and (k == "idversion" or p[k] >= 0) for k in IDENTITY_KEYS - {"traced", "comm"}) and
                  type(p["traced"]) is bool and isinstance(p["comm"], str) and bool(p["comm"]) and p["uniqueid"] > 0
                  for p in identities), "complete native self incarnation (empty identity never qualifies)")
        exact(all(number(sent.get(k)) for k in ("mono_check_begin", "mono_identity_checked", "mono_mask_observed", "mono_pending_before_observed",
                                               "mono_before", "mono_after", "mono_pending_observed")) and
              all(isinstance(sent.get(k), list) and all(integer(n) for n in sent[k]) and sent[k] == sorted(set(sent[k]))
                  for k in ("blocked_mask", "pending_before", "pending")), "ordered typed native mask/pending/send observations")
        need(type(sent["signum"]) is int and sent["signum"] == signum and sent["boundary"] == boundary and sent["fd"] == begin["fd"] and
             integer(sent["self_pid"]) and integer(sent["self_pgid"]) and
             sent["native_kill_returned"] is True and sent["self_pid"] == outcome["owner"]["pid"] == identities[0]["pid"] == identities[1]["pid"] and
             sent["self_pgid"] == outcome["owner"]["pgid"] == identities[0]["pgid"] == identities[1]["pgid"] and
             typed_equal(identities[0], identities[1]) and set(CANCEL_SIGNALS) <= set(sent["blocked_mask"]) and
             not set(CANCEL_SIGNALS) & set(sent["pending_before"]) and signum in sent["pending"] and
             begin["mono"] <= sent["mono_check_begin"] <= sent["mono_identity_checked"] <= sent["mono_mask_observed"] <=
             sent["mono_pending_before_observed"] <= sent["mono_before"] <= sent["mono_after"] <= sent["mono_pending_observed"] <= sent["mono"] and
             sent["native_syscall_overlap_claim"] is False,
             "case-prescribed signal/operation and complete owner incarnation, native kill interval and ordered blocked/pending evidence; NO kernel syscall-overlap claim")
        calls = native_writes if boundary == "write" else [v for v in pick(events, "native_close") if v.get("fd") == begin["fd"] and v["seq"] > begin["seq"]]
        need(bool(calls) and sent["seq"] < calls[0]["seq"] and sent["mono"] <= calls[0]["mono_before"] and
             (sent["seq"] < write_returns[0]["seq"] if boundary == "write" else write_returns[0]["seq"] < sent["seq"]) and
             "error" not in calls[0] and completion_errors[0]["seq"] > calls[0]["seq"] and
             completion_errors[0]["error"]["type"] == "GuardError" and error_text(completion_errors[0]["error"]) == "CANCEL_DURING_GO_COMPLETION",
             "prescribed native signal at the exact original protected second-write/close boundary then actual original completion cancellation")
    report = child_report(cfg, request, outcome, events, "channel")
    rc = EXPECTED_CHILD[case]
    need(report["mode"] == "channel" and report["selected_status_not_actual_exit"] == state["rc"] == rc, "actual child parser exit/source native wait join")
    if case != "io_extra_expiry":
        need(typed_equal(summary.get("child_returncode"), state["rc"]) and summary.get("failure_codes") == sorted(EXPECTED_FAILURES[case]) and
             "reason" not in summary and "error" not in summary and "error_code" not in summary,
             "exact acknowledged summary child status/failure list and absent contradictory source error")
    if rc == 0:
        protocol = report["protocol"]
        need(protocol["eof"] is True and protocol["error"] is None and protocol["creation_manifest_sha256"] == sha(line) and
             protocol["creation_line_bytes"] == len(line) and protocol["raw_hex"] == (b"GO\n" + line).hex() and
             typed_equal(report["manifest"], decoded) and report["method_return"] is None and report["method_exception"] is None and
             not pick(report["observations"], "original_target_open"), "actual original extra-line parser+EOF and identical parsed manifest, no target mutation or method exception")
    else:
        need(report["protocol"] is None and report["method_exception"]["type"] == "ValueError", "actual refused incomplete creation wire")
        text = error_text(report["method_exception"])
        prefix = "MUTATION_GO_NOT_EXACT "
        exact(text.startswith(prefix), "original mutation wire parser exact refusal")
        proof = decode(text[len(prefix):].encode())
        need(proof["raw_hex"] == b"GO\n".hex() and proof["bytes"] == 3 and proof["sha256"] == sha(b"GO\n") and
             proof["eof"] is True and proof["error"] is None and proof["creation_line_bytes"] is None,
             "independently decoded actual GO-only/EOF transport failure evidence")


def prerequisites(case, request, cfg, go, events, outcome):
    """A producer flag is not status authority. Only a case-specific retained missed real-boundary event is NOT_EXERCISED.
    Required-proof gaps, unclassified prerequisites and fixture failures are HOLD; common integrity failures remain retained."""
    values = outcome.get("missing_prerequisites")
    exact(isinstance(values, list) and all(isinstance(v, str) and bool(v) for v in values), "complete typed prerequisite inventory")
    def missed_response(row):
        if not all(number(row.get(k)) for k in ("injection_start", "deadline_mono", "injection_end")):
            return False
        start, cutoff, end = (row[k] for k in ("injection_start", "deadline_mono", "injection_end"))
        return outcome["owner"]["mono_begin"] <= start <= end <= row["mono"] and not start < cutoff < end and (
            "native_before" not in row or number(row.get("native_before")) and number(row.get("native_after")) and
            row["native_before"] <= row["native_after"] <= start)
    def missed_ack(row):
        if not all(number(row.get(k)) for k in ("start_epoch_raw", "expiry_epoch_raw", "end_epoch_raw", "max_delay_s")):
            return False
        start, cutoff, end = (row[k] for k in ("start_epoch_raw", "expiry_epoch_raw", "end_epoch_raw"))
        return typed_equal(cutoff, go["not_after_epoch"]) and row["max_delay_s"] == request["parameters"]["max_flush_delay_s"] and start <= end <= row["epoch_raw"] and (
            cutoff <= start or cutoff > start + row["max_delay_s"] or end <= cutoff)
    def missed_extra(row, cutoff_name):
        begin = pick(events, "extra_line_write_begin")
        if len(begin) != 1 or not all(number(row.get(k)) for k in ("clock_begin_raw", "cutoff_value_raw", "clock_end_raw", "injection_start", "injection_end")):
            return False
        start, cutoff, end = (row[k] for k in ("clock_begin_raw", "cutoff_value_raw", "clock_end_raw"))
        expected = outcome["source_state"]["rec"]["mono_spawn"] + min(60.0, cfg["max_wall_s"] / 2.0) if cutoff_name == "GO_AGE" else go["not_after_epoch"]
        return (row.get("fd") == begin[0]["fd"] and typed_equal(cutoff, expected) and start <= end and not start < cutoff < end and
                begin[0]["mono"] <= row["injection_start"] <= row["injection_end"] <= row["mono"] and
                end <= row["mono" if cutoff_name == "GO_AGE" else "epoch_raw"])
    for value in values:
        valid = False
        if case in POST and value == "real approved GO expiry not crossed within max_flush_delay_s during ACK flush":
            rows = pick(events, "ack_flush_boundary_missed")
            valid = len(rows) == 1 and missed_ack(rows[0]) and not pick(events, "ack_flush_real_expiry_crossing")
        elif case in PUB and case.endswith("_late"):
            op = case[len("io_pub_"):-len("_late")]
            valid = value == "declared " + op + " crossing not observed" and not pick(events, "declared_response_delay") and any(
                v.get("operation_target") == op and v["scope"] == "API_RESPONSE_INJECTION" and missed_response(v) for v in pick(events, "response_delay_boundary_missed"))
        elif case in ACCOUNT + ("io_extra_write_late", "io_extra_close_late"):
            stage = case.removeprefix("io_account_") if case in ACCOUNT else "extra_write" if case == "io_extra_write_late" else "extra_close"
            valid = value == "declared real response crossing not exercised: " + stage and not pick(events, "accounting_late_response") and any(
                v.get("stage") == stage and v["scope"] == "API_RESPONSE_INJECTION" and missed_response(v) for v in pick(events, "accounting_late_boundary_missed"))
        elif case == "io_extra_deadline":
            valid = value == "original unchanged IO_S30 extra-write deadline crossing not exercised" and not pick(events, "accounting_late_response") and any(
                v.get("stage") == "extra_write" and v.get("deadline_clamped") is False and missed_response(v) for v in pick(events, "accounting_late_boundary_missed"))
        elif case in ("io_extra_go_age", "io_extra_expiry"):
            cutoff = "GO_AGE" if case == "io_extra_go_age" else "AUTHORIZATION_EXPIRY"
            valid = value == "extra-line real age/expiry crossing not exercised" and not pick(events, "extra_real_crossing") and any(
                v.get("cutoff") == cutoff and v["scope"] == "API_RESPONSE_INJECTION" and missed_extra(v, cutoff) for v in pick(events, "extra_real_crossing_missed"))
        if valid:
            BOUNDARY.append("DRIVER_RETAINED_VALIDATED_UNEXERCISED_BOUNDARY:" + value)
        else:
            MISSING.append("DRIVER_RETAINED_REQUIRED_PREREQUISITE_UNAVAILABLE_OR_UNVALIDATED:" + value)
    if case in POST and not pick(events, "ack_flush_real_expiry_crossing") and not BOUNDARY:
        MISSING.append("REAL_APPROVED_EXPIRY_CROSSING_NOT_ESTABLISHED_AND_NO_VALIDATED_MISS_EVIDENCE")
    return values


def verify(case, approval_sha, capture_sha):
    run, request, cfg, go, capture, streams, outcome = authority(case, approval_sha, capture_sha)
    events, summary, artifacts = common(run, request, cfg, capture, streams, outcome)
    missing = prerequisites(case, request, cfg, go, events, outcome)
    if BOUNDARY and not FAILURES and not MISSING:
        # Pure validated missed boundary only: preserve the existing early-result keyset and actual status.
        return {"kind": "rqls10-guard-matrix-oracle-v1", "case": case, "status": "NOT_EXERCISED",
                "scope": request["scope"], "approval_sha256": approval_sha, "parent_capture_sha256": capture_sha,
                "actual_exit_from_parent": capture["actual_exit"], "expected_exact_exit_if_exercised": expected_exit(case),
                "missing_prerequisites_or_boundaries": missing,
                "authority": "NO_GO_NO_RELEASE_NO_SCIENCE; actual status is retained, not widened into an exercised case"}
    if not missing and not MISSING and not BOUNDARY:
        need(capture["actual_exit"] == expected_exit(case), "exact separately captured actual exit (no broadened status set)")
        if case in METHOD:
            method_cases(case, cfg, request, outcome, events)
        else:
            need(outcome["source_outcome"].get("mode") == "ORIGINAL_FULL_MAIN_WITH_FIXED_OVERLAY", "actual original full main completed existing finalization/diagnostic attempts")
            if case in AUTH:
                authorization_case(case, events, summary, request, cfg, outcome)
            if case in PUB or case == "io_staged_same_content":
                publication(case, request, cfg, events, summary, outcome)
            accounting(run, case, cfg, outcome, events, summary)
            if case in POST:
                post_ack(case, request, go, events, summary, capture, outcome, streams)
            if case in MUTATION:
                mutation(case, request, cfg, outcome, events, summary)
            if case in EXTRA:
                extra_cases(case, request, cfg, go, outcome, events, summary)
            healthy_report = None
            if case in PUB + ACCOUNT + POST + ("io_staged_same_content", "io_channel_ordinary"):
                healthy_report = healthy_native_baseline(cfg, request, outcome, events)
            if case == "io_channel_ordinary":
                report = healthy_report
                protocol = report["protocol"]
                need(protocol["bytes"] == 3 and protocol["sha256"] == sha(b"GO\n") and protocol["eof"] is True and
                     protocol["creation_line_bytes"] is None and report["manifest"] is None, "actual ordinary GO newline and EOF, no hidden extra line")
                probe = report["ordinary_extra_probe"]
                need(probe["input_utf8_hex"] == b"GO\nEXTRA\n".hex() and probe["source_sha256"] == BASE_SHA and
                     probe["return"] is None and probe["exception"]["type"] == "ValueError" and
                     error_text(probe["exception"]).startswith("GO_READ_REFUSED "), "actual original ordinary parser rejects extra native-pipe bytes")
                need(summary.get("acknowledged") is True and typed_equal(summary.get("exit_code"), 0) and summary.get("settlement") == "SETTLED" and
                     summary.get("failure_codes") == [] and typed_equal(summary.get("child_returncode"), 0) and
                     "reason" not in summary and "error" not in summary and "error_code" not in summary and outcome["source_state"]["rc"] == 0,
                     "exact clean ordinary native full-main SETTLED ACK0 outcome with no source error")
    # Prerequisite-first dependent checks never discard independent integrity failures from common().
    if MISSING:
        status = "HOLD"
    elif FAILURES:
        status = "NOT_MET"
    elif BOUNDARY:
        status = "NOT_EXERCISED"
    else:
        status = "FIXTURE_PREDICATES_MET"
    return {"kind": "rqls10-guard-matrix-oracle-v1", "case": case, "status": status,
            "scope": request["scope"], "approval_sha256": approval_sha, "parent_capture_sha256": capture_sha,
            "actual_exit_from_parent": capture["actual_exit"], "expected_exact_exit": expected_exit(case),
            "failures": FAILURES, "missing_prerequisites_or_boundaries": MISSING + BOUNDARY,
            "strict_certificate_eof_rejection": False if case == "io_channel_certificate_extra" else None,
            "parent_release_gate": "HOLD_REFUSAL_EVIDENCE_NOT_DELIVERED" if case in POST and "persistent" in case else "NO_RELEASE_AUTHORITY",
            "native_limits": "declared API-return delays/short slices are not native syscall-latency/short-write coverage; no universal latency proof",
            "authority": "NO_GO_NO_SCIENCE_ACCEPTANCE_NO_RESERVATION_RELEASE; parent five-part transaction remains separate"}


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("CASE APPROVAL_SHA CAPTURE_SHA required")
        result = verify(sys.argv[1], sys.argv[2], sys.argv[3])
    except BaseException as exc:
        result = {"kind": "rqls10-guard-matrix-oracle-v1", "status": "HOLD", "case": sys.argv[1] if len(sys.argv) > 1 else None,
                  "error_type": type(exc).__name__, "error_utf8_hex": str(exc).encode("utf-8", "surrogateescape").hex(),
                  "error_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "failures": FAILURES,
                  "missing_prerequisites_or_boundaries": MISSING + BOUNDARY,
                  "authority": "NO_GO_NO_RELEASE_NO_SCIENCE_ACCEPTANCE"}
    raw = packed(result)
    # Bounded local result only. Parent owns its exclusive capture/disposition.
    if len(raw) > 1 << 20:
        sys.exit(2)
    sys.stdout.buffer.write(raw)
    sys.stdout.buffer.flush()
    sys.exit(0 if result["status"] == "FIXTURE_PREDICATES_MET" else 2)
