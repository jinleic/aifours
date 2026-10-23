#!/usr/bin/env python3
"""REVIEW CANDIDATE / WRITTEN ONLY. Separate source19 native-fixture oracle.

CHECK CASE APPROVAL_SHA PARENT_CAPTURE_SHA. Reads actual pinned files/captures;
imports no driver, child or supervisor, accepts no pass flag, never grants GO,
science, empirical closure or release. Equality/model counts are not native
coverage. Negative verifier copies are fresh, explicitly oracle-input only.
v2 (guard-v10 native repair): expected exits/failures/signals/exception families are read
from the frozen v2 case object; required prerequisites, measured sides and crossings are
established BEFORE dependent outcome predicates; precedence HOLD > NOT_MET > NOT_EXERCISED
> FIXTURE_PREDICATES_MET. Missing, contradictory or dropped evidence is HOLD.
"""
import ctypes
import errno
import hashlib
import json
import math
import os
import re
import resource
import stat
import struct
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
SUP_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
PATHS = {"supervisor": LANE + "/code/owned_supervisor_v19.py", "driver": LANE + "/code/guard_matrix_native_v2.py",
         "child": LANE + "/code/guard_matrix_native_child_v2.py", "oracle": LANE + "/code/guard_matrix_native_check_v2.py",
         "case_specs": LANE + "/review/rqls10-matrix-native-v2-cases.json"}
SPEC_KIND = "rqls10-matrix-native-v2-cases"
OUTCOME_KIND = "rqls10-guard-matrix-native-outcome-v2"
OUTCOME_KEYS = {"kind", "case", "scope", "bindings", "owner", "observations", "source_outcome", "source_state", "artifacts",
                "fixture_processes", "missing_prerequisites", "unresolved", "native_wait_ledger", "observation_failures",
                "original_main_called", "selected_status_not_actual_exit", "terminal", "observed_maxrss_bytes", "limits",
                "no_empirical_closure", "science_acceptance", "authority"}
SAMPLE_KEYS = {"mono", "epoch", "rc", "census", "resources", "accounting_ref", "streams", "stop", "failure_codes", "trips"}
DATE_ARGV = ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"]
ABI = {"sdk": {"path": "/Library/Developer/CommandLineTools/SDKs/MacOSX26.0.sdk/usr/include/sys/proc_info.h",
               "sha256": "e427fa96b348537b21552b9de71e01039410bcad2cedee5584c5e5fddafd70fc"},
       "private": {"path": LANE + "/tmp/xnu_proc_info_private.h", "sha256": "ccc01e88d5bf47bc9c3f5ba3a25c3e6202bbcd7b86aa967af31d714657571c3b"},
       "implementation": {"path": LANE + "/tmp/xnu_proc_info.c", "sha256": "557092f14fbad3341100f59e0391d2e812c54b79a7404c89b2af97471ad67082"}}
CLEAN = [["admission", "OK"], ["start", "OK"], ["end", "OK"]]
OSERRORS = {"OSError", "GuardError", "ChildProcessError", "ProcessLookupError", "FileNotFoundError", "PermissionError",
            "BlockingIOError", "InterruptedError", "FileExistsError", "IsADirectoryError", "NotADirectoryError",
            "BrokenPipeError", "ConnectionError", "TimeoutError"}
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
LIMITS = {"max_wall_s": 300, "rss_bytes": 256 << 20, "output_bytes": 16 << 20, "busy_ceiling": 2, "max_loops": 2}
IDENTITY = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
START = time.monotonic()
DEADLINE = START + 60.0


class Hold(Exception):
    pass


def exact(condition, reason):
    if not condition:
        raise Hold(reason)


def check():
    if time.monotonic() >= DEADLINE or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 256 << 20:
        raise Hold("oracle cooperative envelope")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def packed(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def same(a, b):
    return packed(a) == packed(b)


def pairs(items):
    out = {}
    for key, value in items:
        exact(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def finite(text):
    value = float(text)
    exact(math.isfinite(value), "nonfinite JSON")
    return value


def nonfinite(text):
    raise Hold("nonfinite JSON")


def decode(raw):
    return json.loads(raw.decode(), object_pairs_hook=pairs, parse_float=finite, parse_constant=nonfinite)


def number(x):
    return type(x) in (int, float) and math.isfinite(x)


def integer(x):
    return type(x) is int


def hex64(x):
    return type(x) is str and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def error_text(obj):
    exact(type(obj) is dict and set(obj) == {"type", "errno", "UTF8_HEX", "utf8_bytes", "text_scope"}, "complete raw error schema")
    exact(type(obj["type"]) is str and (obj["errno"] is None or integer(obj["errno"])) and type(obj["UTF8_HEX"]) is str and
          integer(obj["utf8_bytes"]), "typed raw error schema")
    raw = bytes.fromhex(obj["UTF8_HEX"])
    exact(obj["text_scope"] == "MODEL_INPUT_NOT_ACTUAL_BIN_DATE" and len(raw) == obj["utf8_bytes"], "raw error not truncated/date scoped")
    return raw.decode("utf-8", "surrogateescape")


def exception_code(obj):
    # Independent re-statement of source19 exception_code (L2375-2381) over the retained raw error record.
    text = error_text(obj)
    if obj["type"] == "GuardError" and obj["errno"] is None:
        return text.split(" ", 1)[0]
    if obj["type"] in OSERRORS:
        return "OS_ERROR_%s" % obj["errno"]
    return obj["type"]


def directory(path):
    exact(type(path) is str and path.startswith("/") and os.path.normpath(path) == path, "canonical directory")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.split("/")[1:]:
            check()
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


def regular(path, cap=16 << 20):
    pfd, fd = directory(os.path.dirname(path)), None
    try:
        fd = os.open(os.path.basename(path), os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=pfd)
        before = os.fstat(fd)
        exact(stat.S_ISREG(before.st_mode) and 0 <= before.st_size <= cap, "bounded regular")
        raw = bytearray()
        while len(raw) < before.st_size:
            check()
            b = os.read(fd, min(65536, before.st_size - len(raw)))
            exact(bool(b), "regular short read")
            raw.extend(b)
        after = os.fstat(fd)
        exact(not os.read(fd, 1) and all(getattr(before, k) == getattr(after, k) for k in
              ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")), "regular changed")
        return {"path": path, "inode": inode(fd), "bytes": len(raw), "sha256": sha(raw), "nlink": before.st_nlink}, bytes(raw)
    finally:
        if fd is not None:
            os.close(fd)
        os.close(pfd)


def inventory(root):
    out, seen, total = {}, set(), 0
    def walk(path, depth):
        nonlocal total
        exact(depth <= 12 and len(out) < 1024, "inventory cap")
        fd = directory(path)
        try:
            out[path] = {"path": path, "directory_inode": inode(fd)}
            for name in sorted(os.listdir(fd)):
                check()
                st = os.stat(name, dir_fd=fd, follow_symlinks=False)
                full = path + "/" + name
                if stat.S_ISDIR(st.st_mode):
                    walk(full, depth + 1)
                else:
                    exact(stat.S_ISREG(st.st_mode), "unlisted nonregular artifact")
                    facts, _ = regular(full)
                    out[full] = facts
                    key = tuple(facts["inode"])
                    if key not in seen:
                        seen.add(key)
                        total += facts["bytes"]
        finally:
            os.close(fd)
    walk(root, 0)
    return out, total


def fingerprint(p):
    exact(type(p) is dict and all(k in p for k in IDENTITY), "full raw identity")
    exact(type(p["traced"]) is bool and all(integer(p[k]) for k in IDENTITY if k != "traced"), "typed raw identity")
    return tuple(p[k] for k in IDENTITY)


class Oracle:
    def __init__(self, case, approval_sha, capture_sha):
        self.case, self.approval_sha, self.capture_sha = case, approval_sha, capture_sha
        self.run = ROOT + "/" + case
        self.failures, self.missing = [], []
        self.outcome, self.request, self.capture, self.cfg = None, None, None, None
        self.spec, self.frozen, self.summary, self.child, self.ledger = None, None, None, None, []
    def need(self, condition, reason):
        if not condition:
            self.failures.append(reason)
    def absent(self, reason):
        self.missing.append(reason)
    def events(self, name):
        return [e for e in self.outcome["observations"] if e["operation"] == name]
    def only(self, name):
        rows = self.events(name)
        exact(len(rows) == 1, "exact raw event required: " + name)
        return rows[0]
    def state(self):
        exact(type(self.outcome.get("source_state")) is dict, "actual source state required")
        return self.outcome["source_state"]
    def expected_config(self, py, alloc, wall):
        # Independent re-derivation of the complete frozen native config (spec fixed_config), exact JSON types.
        run, case = self.run, self.case
        cfg = {"item": case, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE,
               "argv": [py["path"], "-I", "-B", PATHS["child"], "main", case],
               "env": {"PATH": "/usr/bin:/bin", "TMPDIR": run + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"},
               "output_roots": [run + "/out"], "lane_disk_root": run, "lane_roots": [LANE], "pins": [],
               "outputs": [{"path": run + "/out/child-result.json", "required": True}], "max_wall_s": wall,
               "settle_s": 20.0, "sample_s": 0.2, "max_chunk_seconds": 10800.0, "rss_projection_bytes": 16 << 20,
               "rss_trip_bytes": (128 << 20) if case == "nat_cap_final_rss" else 256 << 20,
               "free_trip_bytes": 12000000000, "launch_free_min_bytes": 12200000000, "output_trip_bytes": 12 << 20,
               "lane_disk_ceiling_bytes": 64 << 20, "lane_walk_s": 5.0, "busy_limit": 2, "busy_cpu_fraction": 0.5,
               "cpu_slots": alloc["cpu_slots"], "fault_injection": {}, "creation_channel": {},
               "stdout_cap_bytes": 128 << 10, "stderr_cap_bytes": 128 << 10, "samples_cap_bytes": 1 << 20,
               "helper_budget": {"max_calls": 8, "call_budget_s": 2.0, "term_grace_s": 1.0},
               "admission": {"go_path": run + "/GO.json", "stability_receipt_path": run + "/stability.json",
                             "reservation_bytes": alloc["bytes"], "outstanding_reservations_bytes": alloc["outstanding_reservations_bytes"],
                             "lane_outstanding_reservations_bytes": alloc["lane_outstanding_reservations_bytes"],
                             "stability_max_age_s": 45.0 if case.endswith("_stability") else 300.0}}
        for key, name in (("stdout", "child.stdout"), ("stderr", "child.stderr"), ("samples", "samples.jsonl"),
                          ("launch_record", "launch.json"), ("receipt", "receipt.json"), ("settlement_record", "settlement.json")):
            cfg[key] = run + "/out/" + name
        return cfg
    def auth(self):
        case, run = self.case, self.run
        exact(case in CASES and hex64(self.approval_sha) and hex64(self.capture_sha), "fixed oracle arguments")
        af, ar = regular(run + "/parent-authorization.json", 1 << 20)
        rf, rr = regular(run + "/request.json", 1 << 20)
        exact(af["sha256"] == self.approval_sha, "external approval SHA")
        ap, rq = decode(ar), decode(rr)
        keys = {"kind", "case", "scope", "sources", "anchors", "allocation", "not_after_epoch", "negative_control", "ownership_negative",
                "hook_set", "config", "go", "stability", "python", "created_facts", "case_spec_sha256", "derived_base", "limits"}
        exact(type(rq) is dict and type(ap) is dict and set(rq) == keys and set(ap) == keys | {"request_sha256"} and
              ap["request_sha256"] == rf["sha256"] and ap["kind"] == "rqls10-guard-matrix-invocation-v1" and
              rq["kind"] == "rqls10-guard-matrix-request-v1" and all(same(ap[k], rq[k]) for k in keys - {"kind"}), "exact authority/request schema and typed join")
        exact(rq["case"] == case and rq["scope"] == "MODIFIED_QUALIFICATION_FIXTURE" and rq["hook_set"] == [case] and
              rq["negative_control"] is (case not in POSITIVE) and rq["ownership_negative"] is (case in OWNERSHIP), "case scope negative hooks")
        exact(same(rq["limits"], LIMITS) and number(rq["not_after_epoch"]), "fixed declared resource envelope and typed expiry")
        alloc = rq["allocation"]
        exact(type(alloc) is dict and set(alloc) == {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} and
              all(integer(v) and v >= 0 for v in alloc.values()) and alloc["bytes"] == 20 << 20 and alloc["cpu_slots"] == (2 if case in OWNERSHIP else 1), "serialized allocation")
        exact(type(rq["sources"]) is dict and set(rq["sources"]) == set(PATHS), "fixed source set")
        for role, path in PATHS.items():
            pin = rq["sources"][role]
            exact(type(pin) is dict and set(pin) == {"path", "sha256"} and pin["path"] == path and hex64(pin["sha256"]), "source pin schema")
            exact(regular(path, 2 << 20)[0]["sha256"] == pin["sha256"], "actual exact source: " + role)
        exact(rq["sources"]["supervisor"]["sha256"] == SUP_SHA, "immutable source19")
        specs = decode(regular(PATHS["case_specs"], 2 << 20)[1])
        exact(specs["kind"] == SPEC_KIND and set(specs["cases"]) == set(CASES) and
              specs["supervisor"] == {"path": PATHS["supervisor"], "sha256": SUP_SHA}, "complete exact finite v2 catalog")
        exact(sha(packed(specs["cases"][case])) == rq["case_spec_sha256"], "exact case definition binding")
        self.spec = specs["cases"][case]
        frozen = self.spec["strict_outcome"]
        exact(type(frozen) is dict and integer(frozen.get("parent_actual_driver_exit")) and type(frozen.get("source")) is dict,
              "frozen strict outcome schema")
        self.frozen = frozen
        if case in DERIVED:
            base = rq["derived_base"]
            exact(type(base) is dict and set(base) == {"case", "approval_sha256", "capture_sha256"} and base["case"] == "nat_integration_normal_exit" and
                  hex64(base["approval_sha256"]) and hex64(base["capture_sha256"]), "exact externally pinned normal-exit base")
        else:
            exact(rq["derived_base"] is None, "no undeclared derived base")
        exact(type(rq["anchors"]) is dict and set(rq["anchors"]) == {"run", "out", "tmp", "scratch"}, "anchor schema")
        for key, suffix in (("run", ""), ("out", "/out"), ("tmp", "/tmp"), ("scratch", "/scratch")):
            fd = directory(run + suffix)
            try:
                exact(same(rq["anchors"][key], {"path": run + suffix, "inode": inode(fd)}), "original/current anchor " + key)
            finally:
                os.close(fd)
        exact(type(rq["created_facts"]) is dict and set(rq["created_facts"]) == {"config", "go", "stability"}, "created-descriptor schema")
        for key, name in (("config", "config.json"), ("go", "GO.json"), ("stability", "stability.json")):
            facts, _ = regular(run + "/" + name, 1 << 20)
            exact(same(rq[key], {"path": facts["path"], "sha256": facts["sha256"]}) and same(rq["created_facts"][key], facts) and
                  facts["nlink"] == 1, "actual original parent-created input " + key)
        py = rq["python"]
        exact(type(py) is dict and set(py) == {"path", "sha256"} and os.path.realpath(py["path"]) == py["path"] and
              regular(py["path"], 64 << 20)[0]["sha256"] == py["sha256"], "actual interpreter bytes")
        cfg = decode(regular(run + "/config.json", 1 << 20)[1])
        go = decode(regular(run + "/GO.json", 1 << 20)[1])
        wall = 200.0 if case in GO and "w200" in case else 10.0
        expected = self.expected_config(py, alloc, wall)
        exact(type(cfg) is dict and set(cfg) == set(expected) | {"owned_compute_settled_by_epoch"}, "complete fixed native config key set")
        for key, wanted in expected.items():
            exact(same(cfg[key], wanted), "fixed typed native config/allocation join: " + key)
        exact(number(cfg["owned_compute_settled_by_epoch"]) and cfg["owned_compute_settled_by_epoch"] >= rq["not_after_epoch"] + 1000,
              "fixed fit headroom")
        bound = {k: expected[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
        bound.update({"reservation_bytes": alloc["bytes"], "outstanding_reservations_bytes": alloc["outstanding_reservations_bytes"],
                      "lane_outstanding_reservations_bytes": alloc["lane_outstanding_reservations_bytes"]})
        expected_go = {"decision": "GO", "item": case, "configs": {rq["config"]["sha256"]: bound},
                       "not_after_epoch": go.get("not_after_epoch") if type(go) is dict else None, "stability_receipt_sha256": rq["stability"]["sha256"]}
        if rq["negative_control"]:
            expected_go["qualification_negative"] = {"scenario": case, "kind": "matrix_native", "creation_channel": False}
        exact(same(go, expected_go) and number(go["not_after_epoch"]) and go["not_after_epoch"] <= rq["not_after_epoch"], "fixed GO exact typed binding to allocation")
        cf, cr = regular(run + "/parent-capture.json", 1 << 20)
        exact(cf["sha256"] == self.capture_sha, "external capture SHA")
        cap = decode(cr)
        ck = {"kind", "case", "approval_sha256", "driver_source_sha256", "pid", "pgid", "mono_begin", "mono_end", "actual_exit", "stdout", "stderr", "outcome_sha256", "wait_status"}
        exact(type(cap) is dict and set(cap) == ck and cap["kind"] == "rqls10-guard-matrix-parent-capture-v1" and cap["case"] == case and
              cap["approval_sha256"] == self.approval_sha and cap["driver_source_sha256"] == rq["sources"]["driver"]["sha256"] and
              hex64(cap["outcome_sha256"]), "parent actual capture binding")
        exact(integer(cap["pid"]) and integer(cap["pgid"]) and min(cap["pid"], cap["pgid"]) > 1 and integer(cap["actual_exit"]) and
              number(cap["mono_begin"]) and number(cap["mono_end"]) and 0 <= cap["mono_end"] - cap["mono_begin"] <= 300, "native parent owner/time exact types")
        ws = cap["wait_status"]
        exact(type(ws) is dict and set(ws) == {"native_wait_status", "waitpid_pid", "reaped"} and ws["reaped"] is True and
              integer(ws["waitpid_pid"]) and ws["waitpid_pid"] == cap["pid"] and integer(ws["native_wait_status"]) and ws["native_wait_status"] >= 0 and
              (os.WIFEXITED(ws["native_wait_status"]) or os.WIFSIGNALED(ws["native_wait_status"])) and
              os.waitstatus_to_exitcode(ws["native_wait_status"]) == cap["actual_exit"], "parent native destructive status exact types, not selected return")
        self.streams = {}
        for name in ("stdout", "stderr"):
            rec = cap[name]
            exact(type(rec) is dict and set(rec) == {"path", "sha256", "bytes", "inode", "eof"} and rec["path"] == run + "/driver." + name and
                  rec["eof"] is True and hex64(rec["sha256"]) and integer(rec["bytes"]) and rec["bytes"] >= 0 and type(rec["inode"]) is list and
                  len(rec["inode"]) == 2 and all(integer(x) and x >= 0 for x in rec["inode"]), "complete exact-typed original-inode parent streams required")
            facts, raw = regular(rec["path"], 4 << 20)
            exact(facts["sha256"] == rec["sha256"] and facts["bytes"] == rec["bytes"] and facts["inode"] == rec["inode"], "actual parent stream bytes and original created inode")
            self.streams[name] = raw
        of, raw = regular(run + "/fixture-outcome.json", 8 << 20)
        exact(of["sha256"] == cap["outcome_sha256"], "actual outcome digest joined")
        self.request, self.capture, self.cfg, self.go, self.outcome = rq, cap, cfg, go, decode(raw)
    def common(self):
        rq, cap, out = self.request, self.capture, self.outcome
        exact(type(out) is dict and set(out) == OUTCOME_KEYS and out["kind"] == OUTCOME_KIND and out["case"] == self.case and
              out["scope"] == rq["scope"], "outcome exact v2 kind/keys/case/scope")
        expected = {"approval_sha256": self.approval_sha, "request_sha256": regular(self.run + "/request.json")[0]["sha256"],
                    **{k: rq[k] for k in ("sources", "anchors", "allocation", "config", "go", "stability", "python", "created_facts", "hook_set", "negative_control", "ownership_negative", "case_spec_sha256", "derived_base")}}
        exact(same(out["bindings"], expected), "outcome exact authority binding")
        owner = out["owner"]
        exact(type(owner) is dict and set(owner) == {"pid", "pgid", "mono_begin", "mono_end"} and integer(owner["pid"]) and integer(owner["pgid"]) and
              owner["pid"] == cap["pid"] and owner["pgid"] == cap["pgid"] and
              number(owner["mono_begin"]) and number(owner["mono_end"]) and
              cap["mono_begin"] <= owner["mono_begin"] <= owner["mono_end"] <= cap["mono_end"], "owner/capture chronology")
        exact(out["no_empirical_closure"] is True and out["science_acceptance"] is False and same(out["limits"], LIMITS) and
              number(out["observed_maxrss_bytes"]) and out["observed_maxrss_bytes"] <= 256 << 20, "honest scope/resource envelope")
        exact(out["observation_failures"] == [], "contained native observation failures leave the evidence incomplete")
        lines = self.streams["stdout"].splitlines(keepends=True)
        exact(lines and all(line.endswith(b"\n") for line in lines), "complete stdout framing")
        first = decode(lines[0])
        exact(first["kind"] == "rqls10-matrix-owner-v1" and all(first[k] == owner[k] for k in ("pid", "pgid", "mono_begin")), "first native owner before work")
        full = self.case not in METHOD + DERIVED
        exact(out["original_main_called"] is full and len(lines) == (2 if full else 1), "full main vs native-method output framing")
        self.summary = decode(lines[1]) if full else None
        self.need(cap["actual_exit"] != 120, "actual14 can never be replaced by120")
        events = out["observations"]
        exact(type(events) is list and 1 <= len(events) <= 4096, "bounded complete raw trace")
        last = owner["mono_begin"]
        for index, row in enumerate(events):
            exact(type(row) is dict and integer(row.get("seq")) and row["seq"] == index and number(row.get("mono")) and last <= row["mono"] <= owner["mono_end"] and
                  type(row.get("operation")) is str and type(row.get("scope")) is str, "raw event sequence/scope/time")
            last = row["mono"]
            if "mono_before" in row:
                exact(number(row["mono_before"]) and number(row.get("mono_after")) and row["mono_before"] <= row["mono_after"] <= row["mono"], "native call interval")
            if row.get("error") is not None:
                error_text(row["error"])
        for row in out["unresolved"]:
            if type(row) is not dict or row.get("kind") == "raw_event_trace_dropped":
                raise Hold("raw event trace incomplete")
        checked, loaded = self.only("authority_checked"), self.only("source_loaded")
        exact(checked["approval_sha256"] == self.approval_sha and checked["sources"] == rq["sources"] and checked["anchors"] == rq["anchors"] and
              loaded["supervisor_sha256"] == SUP_SHA and loaded["wrapper_sha256"] == rq["sources"]["driver"]["sha256"] and
              loaded["hook_set"] == [self.case] and loaded["seq"] > checked["seq"], "actual authorized source/hook load")
        exact(out["terminal"] == {"source_sha256": SUP_SHA, "ast_lines": [2688, 2692], "unchanged": full}, "source19 terminal framing")
        if full:
            # ACK_REFUSED's original unsuccessful() summary has no config_sha256 field (source19 L2389/L2638).
            # The original state record always carries it; when summary exports it the duplicate must agree.
            exact(type(self.summary) is dict and self.summary.get("supervisor") == "owned_supervisor_v19" and
                  self.state()["rec"].get("config_sha256") == rq["config"]["sha256"] and
                  ("config_sha256" not in self.summary or self.summary["config_sha256"] == rq["config"]["sha256"]), "actual source summary/state config identity")
            writes = self.events("native_source_stdout_write")
            exact(len(writes) == 1 and writes[0]["bytes"] == len(lines[1]) and writes[0]["sha256"] == sha(lines[1]) and
                  sum(writes[0]["native_counts"]) == len(lines[1]) and all(integer(n) and n > 0 for n in writes[0]["native_counts"]), "actual native stdout bytes/counts")
        actual = {}
        for root in (self.run + "/out", self.run + "/tmp", self.run + "/scratch"):
            actual.update(inventory(root)[0])
        reported = out["artifacts"]
        exact(len({r["path"] for r in reported}) == len(reported) and set(actual) == {r["path"] for r in reported}, "complete independent artifact path correspondence")
        for row in reported:
            exact(same(actual[row["path"]], row), "actual artifact original/current inode/hash/size/nlink")
        self.artifacts = actual
        _, total = inventory(self.run)
        self.need(total <= 16 << 20, "whole RUN distinct-inode output bound")
        if out["missing_prerequisites"]:
            self.missing.extend("DRIVER_RETAINED:" + str(x) for x in out["missing_prerequisites"])
        if out["source_state"] is not None:
            state = self.state()
            recon = state["reconciliation"]
            exact(recon.get("timing_failed") is False, "source timing evidence unavailable")
            fit = recon["initial_fit"]
            exact(type(fit) is dict and same(fit, state["rec"]["initial_fit"]) and all(number(v) for v in fit.values()), "original initial fit object and raw clocks")
            self.need(fit["chunk_epoch_bound"] == fit["start_epoch"] + self.cfg["max_chunk_seconds"] - 120 and
                      fit["owned_epoch_bound"] == self.cfg["owned_compute_settled_by_epoch"] - 180 and
                      fit["fit_epoch"] == min(fit["chunk_epoch_bound"], fit["owned_epoch_bound"]) and
                      fit["fit_mono"] == fit["start_mono"] + fit["fit_epoch"] - fit["start_epoch"], "deadline fit provenance from fixed config and original startup clocks")
        self.ledger = self.wait_ledger()
        self.census_history_join()
        if out["source_state"] is not None:
            state = self.state()
            main = state["reconciliation"].get("main_wait")
            if type(main) is dict and main.get("leader_reaped") is True:
                self.main_wait_join()  # Integrity join is independent of any quiet-host/window prerequisite.
            for helper in state["reconciliation"]["helpers"]:
                if helper.get("date") is not None:
                    self.helper_proof(helper, True)  # A claimed actual date requires complete native proof even when a different prerequisite is absent.
                elif helper.get("leader_reaped") is True:
                    raw = helper.get("native_wait_result")
                    exact(type(raw) is list and len(raw) == 2 and all(integer(v) for v in raw) and integer(helper.get("raw_wait_status")) and
                          integer(helper.get("rc")), "helper destructive status proof available independently of the case window")
                    self.need(raw == [helper["pid"], helper["raw_wait_status"]] and (os.WIFEXITED(raw[1]) or os.WIFSIGNALED(raw[1])) and
                              os.waitstatus_to_exitcode(raw[1]) == helper["rc"], "independent helper native tuple/raw-status/rc consistency")
        for row in self.events("native_spawn_registered"):
            self.need(row["source_ledger_registered"] is True and integer(row["pid"]) and row["pid"] > 1 and row["pgid"] == row["pid"] and
                      row["setsid"] is True and row["setsigmask"] == [], "real registered native PID/fresh group/empty mask")
            if row["role"] == "helper" and not self.events("declared_native_method_helper"):
                self.need(row["argv"] == DATE_ARGV, "sole actual production clock helper is /bin/date")
        self.probe_join()
        self.unresolved_join()
        self.term_join()
        if full and self.frozen["parent_actual_driver_exit"] in (0, 10, 11, 14):
            self.publication()
    def wait_ledger(self):
        ledger = self.outcome["native_wait_ledger"]
        exact(type(ledger) is list, "native destructive wait ledger")
        seen = set()
        for row in ledger:
            exact(type(row) is list and len(row) == 4 and row[0] in ("source_waitpid", "fixture_probe", "competing_fixture_reaper") and
                  integer(row[1]) and row[1] > 1 and integer(row[2]) and row[2] == row[1] and integer(row[3]) and row[3] >= 0, "typed destructive wait ledger row")
            exact(row[1] not in seen, "one destructive native result per PID")
            seen.add(row[1])
        for e in self.events("native_waitpid"):
            exact(integer(e.get("pid")) and e.get("options") == os.WNOHANG and (("native_result" in e) != ("error" in e)), "native wait event schema")
            if "native_result" in e:
                exact(type(e["native_result"]) is list and len(e["native_result"]) == 2 and all(integer(x) for x in e["native_result"]) and
                      e["native_result"][0] in (0, e["pid"]), "native wait tuple schema")
        success = sorted([e["pid"], e["native_result"][1]] for e in self.events("native_waitpid") if "native_result" in e and e["native_result"][0])
        exact(success == sorted([r[1], r[3]] for r in ledger if r[0] == "source_waitpid"), "every successful source wait event equals its ledgered destructive tuple")
        reaper = sorted([e["pid"], e["native_result"][1]] for e in self.events("native_competing_reaper"))
        exact(reaper == sorted([r[1], r[3]] for r in ledger if r[0] == "competing_fixture_reaper"), "competing reaper tuple ledgered")
        destroyed = {}
        for e in self.outcome["observations"]:
            if e["operation"] == "native_waitpid":
                if e["pid"] in destroyed:
                    allowed = (self.case == "nat_helper_lost_wait" and destroyed[e["pid"]] == "competing" and
                               "error" in e and e["error"]["type"] == "ChildProcessError")
                    self.need(allowed, "native wait call after a destructive result for the same PID")
                elif "native_result" in e and e["native_result"][0]:
                    destroyed[e["pid"]] = "source"
            elif e["operation"] == "native_competing_reaper":
                destroyed[e["pid"]] = "competing"
        return ledger
    def census_history_join(self):
        s = self.outcome["source_state"]
        if s is None:
            return
        recon = s["reconciliation"]
        history, attempts = recon["census_observations"], recon["observation_attempts"]
        exact(type(history) is list and type(attempts) is list, "complete original census/attempt histories")
        returns = self.events("original_census_return")
        aborted = [e for e in self.events("original_census_exception") if e.get("census_mono_start") is not None]
        exact(len(returns) + len(aborted) == len(history), "every original census call with a retained record joins one history row")
        by_start = {c["mono_start"]: c for c in history}
        exact(len(by_start) == len(history), "distinct original census history starts")
        for e in returns:
            exact(e["mono_start"] in by_start, "successful census native return present in complete history")
            c = by_start[e["mono_start"]]
            self.need(c["complete"] is e["complete"] and c["mono_complete"] == e["mono_complete"] and same(c["incomplete"], e["incomplete"]) and
                      sorted(p["uniqueid"] for p in c["owned_live"]) == e["owned_uniqueids"] and
                      sorted(p["uniqueid"] for p in c["unproved_live"]) == e["unproved_uniqueids"], "original census return equals its retained source history")
        for e in aborted:
            exact(e["census_mono_start"] in by_start and by_start[e["census_mono_start"]]["aborted"] is True,
                  "aborted original census exception present in complete history")
        for c in history:
            exact(number(c.get("mono_start")) and number(c.get("mono_end")), "every retained census has start/end evidence")
            matched = [a for a in attempts if a["kind"] == "resource_scan" and a["mono_end"] == c["mono_end"] and c["mono_start"] <= a["mono_start"] <= c["mono_end"]]
            exact(len(matched) == 1 and matched[0]["aborted"] is c["aborted"], "every census joins its complete resource-scan attempt (no empty-history vacuity)")
    def probe_join(self):
        for p in self.outcome["fixture_processes"]:
            exact(type(p) is dict and integer(p.get("pid")) and type(p.get("identity")) is dict, "registered probe record")
            fingerprint(p["identity"])
            regs = [e for e in self.events("native_fixture_probe_registered") if e["pid"] == p["pid"]]
            caps = [e for e in self.events("native_probe_owner_capture") if e["pid"] == p["pid"]]
            reaps = [e for e in self.events("native_probe_reaped") if e["pid"] == p["pid"]]
            exact(len(regs) == len(caps) == 1 and fingerprint(regs[0]["identity"]) == fingerprint(p["identity"]) and
                  regs[0]["role"] == caps[0]["role"] == p["role"] and caps[0]["raw_hex"] == p["owner_raw_hex"],
                  "probe record joins original registration and original captured owner bytes")
            self.need(p.get("reaped") is True and type(p.get("native_wait_result")) is list and p["native_wait_result"][0] == p["pid"] and
                      p.get("stdin_fd") is None and p.get("stdout_fd") is None, "driver-owned probe settled by its original sole native wait")
            rows = [r for r in self.ledger if r[1] == p["pid"]]
            if p.get("reaped") is True:
                self.need(len(rows) == 1 and rows[0][0] == "fixture_probe" and rows[0][3] == p["native_wait_result"][1] and len(reaps) == 1 and
                          reaps[0]["native_wait_result"] == p["native_wait_result"] and regs[0]["seq"] < caps[0]["seq"] < reaps[0]["seq"] and
                          p["mono_reaped"] == reaps[0]["mono_after"] <= p["cleanup_deadline"] and p["wait_lost"] is False and p["cleanup_exhausted"] is False and
                          os.waitstatus_to_exitcode(rows[0][3]) == p["rc"] == 0, "probe sole destructive native result/rc/chronology retained within its one cleanup deadline")
            exact(number(p.get("cleanup_deadline")) and number(p.get("mono_cleanup_first_entry")), "original single probe cleanup interval retained")
            self.need(0 <= p["cleanup_deadline"] - p["mono_cleanup_first_entry"] <= 5.0 and
                      p["mono_cleanup_first_entry"] <= p["mono_reaped"] <= p["cleanup_deadline"], "probe cleanup never exceeds its one absolute original interval")
            sig = p.get("signal")
            terms = [e for e in self.events("native_probe_TERM") if e["pid"] == p["pid"]]
            self.need(len(terms) == (0 if sig is None else 1) and (sig is None) is (p.get("term_attempted") is False) and
                      all(t["signum"] == 15 and same(t["signal"], sig) for t in terms), "at most one retained named SIGTERM probe attempt")
            if type(sig) is dict and sig.get("sent") is True:
                self.need(sig.get("identity_ok") is True and fingerprint(sig["identity_observed"]) == fingerprint(p["identity"]) and
                          all(number(sig.get(k)) for k in ("mono_check", "mono_identity_begin", "mono_identity_observed", "mono_sent")) and
                          sig["mono_check"] <= sig["mono_identity_begin"] <= sig["mono_identity_observed"] <= sig["mono_sent"],
                          "probe TERM only after a fresh full-fingerprint check, chronology retained")
            raw = bytes.fromhex(p["owner_raw_hex"])
            exact(raw.endswith(b"\n") and raw.count(b"\n") == 1, "probe owner complete capture")
            frame = decode(raw)
            self.need(caps[0]["bytes"] == len(raw) and caps[0]["sha256"] == sha(raw), "probe owner capture bytes/digest independently recomputed")
            self.need(frame["pid"] == p["pid"] and frame["pgid"] == p["identity"]["pgid"], "probe actual owner record")
    def method_helper(self):
        so = self.outcome["source_outcome"]
        return so.get("helper") if type(so) is dict else None
    def unresolved_join(self):
        rows = self.outcome["unresolved"]
        expected = []
        if self.case in ("nat_helper_unverified_identity", "nat_helper_lost_wait", "nat_helper_grace_exhaustion"):
            h = self.method_helper()
            if type(h) is dict:
                expected = [{"kind": "source_owned_process", "pid": h["pid"], "role": "helper", "identity": h["identity"],
                             "wait_lost": self.case == "nat_helper_lost_wait"}]
        # Only the exact intended helper incarnation may remain blocking; every other row is refused.
        self.need(same(rows, expected), "unresolved rows equal exactly the intended blocking incarnation set")
    def term_join(self):
        events = self.events("native_source_TERM")
        s = self.outcome["source_state"]
        if s is None:
            self.need(not events, "no source TERM without a source state")
            return
        helpers = {h["pid"]: h for h in s["reconciliation"]["helpers"]}
        grouped = {}
        for e in events:
            t = e.get("target")
            exact(type(t) is dict and t.get("role") in ("main", "helper") and integer(t.get("pid")) and integer(e.get("pgid")) and
                  e.get("signal") == 15 and number(e.get("mono_before")) and number(e.get("mono_after")), "native TERM event schema/target")
            exact(("native_return" in e) != ("error" in e) and ("native_return" not in e or e["native_return"] is None), "native TERM result/error schema")
            grouped.setdefault((t["role"], t["pid"]), []).append(e)
        for (role, pid), rows in grouped.items():
            if role == "main":
                self.need(pid == s["pid"] and type(s["identity"]) is dict and all(r["pgid"] == s["group"] == s["identity"]["pgid"] and r["target"]["uniqueid"] == s["identity"]["uniqueid"] for r in rows),
                          "main TERM targets only the installed main group")
            else:
                self.need(pid in helpers and type(helpers[pid]["identity"]) is dict and all(r["pgid"] == helpers[pid]["identity"]["pgid"] and r["target"]["uniqueid"] == helpers[pid]["identity"]["uniqueid"] for r in rows),
                          "helper TERM targets only a registered helper group")
            self.need(len(rows) <= 1, "at most one native TERM attempt per target incarnation, failed attempts included")
        def check(sig, identity, rows, what):
            if type(sig) is dict and type(sig.get("identity_observed")) is dict:
                if sig.get("identity_event_ref") is None:
                    raw = [r for r in s["reconciliation"]["raw_acquisitions"] if r.get("id") == sig.get("raw_identity_ref")]
                    self.need(len(raw) == 1 and raw[0].get("native_returned") is True and same(raw[0].get("identity"), sig["identity_observed"]) and
                              raw[0].get("mono_begin") == sig.get("mono_identity_begin") and raw[0].get("mono_end") == sig.get("mono_identity_observed"),
                              what + ": raw signal acquisition survives a missing canonical event")
                else:
                    self.need(self.canonical_identity(sig["identity_observed"], sig["identity_event_ref"]), what + ": signal canonical acquisition/event/history join")
            if rows:
                self.need(type(sig) is dict and type(identity) is dict and sig.get("identity_ok") is True and
                          fingerprint(sig["identity_observed"]) == fingerprint(identity) and
                          all(number(sig.get(k)) for k in ("mono_check", "mono_identity_begin", "mono_identity_observed")) and
                          sig["mono_check"] <= sig["mono_identity_begin"] <= sig["mono_identity_observed"] <= rows[0]["mono_before"],
                          what + ": every native attempt (including failed) has its authorized fresh full-fingerprint check and bounded chronology")
            if type(sig) is dict and sig.get("sent") is True:
                self.need(len(rows) == 1 and "error" not in rows[0] and sig.get("identity_ok") is True and type(identity) is dict and
                          fingerprint(sig["identity_observed"]) == fingerprint(identity) and
                          all(number(sig.get(k)) for k in ("mono_check", "mono_identity_begin", "mono_identity_observed")) and
                          sig["mono_check"] <= sig["mono_identity_begin"] <= sig["mono_identity_observed"] <= rows[0]["mono_before"] and
                          (sig.get("mono_sent") is None or rows[0]["mono_after"] <= sig["mono_sent"]),
                          what + ": sent flag requires exactly one successful native TERM after a fresh full-fingerprint check")
            else:
                self.need(all("error" in r for r in rows) and (not rows or (type(sig) is dict and sig.get("identity_ok") is True)),
                          what + ": an unsent signal record admits only one failed native attempt after a passed fresh check")
        check(s.get("signal"), s.get("identity"), grouped.get(("main", s["pid"]), []), "main")
        for pid, h in helpers.items():
            check(h.get("signal"), h.get("identity"), grouped.get(("helper", pid), []), "helper %d" % pid)
    def publication(self):
        # Frozen exits 0/10/11/14 of full-main cases are all post-publication outcomes: the receipt, staged
        # settlement pair and every source-created artifact must exist with original identities and exact sizes.
        s, summ, arts = self.state(), self.summary, self.artifacts
        receipt, final, staged = self.cfg["receipt"], self.cfg["settlement_record"], self.cfg["settlement_record"] + ".staged"
        exact(hex64(summ.get("receipt_sha256")) and hex64(summ.get("settlement_record_sha256")), "summary publication digests required")
        self.need(receipt in arts and final in arts and staged in arts, "receipt and staged settlement publications exist")
        if receipt in arts and final in arts and staged in arts:
            self.need(arts[receipt]["sha256"] == summ["receipt_sha256"] and arts[final]["sha256"] == summ["settlement_record_sha256"] and
                      arts[final]["inode"] == arts[staged]["inode"] and arts[final]["nlink"] == arts[staged]["nlink"] == 2 and arts[receipt]["nlink"] == 1,
                      "actual receipt digest and sole staged-pair inode/digest publication")
            pubs = self.events("native_original_publication")
            self.need(sorted(p["role"] for p in pubs) == ["receipt", "staged"] and
                      all(p["path"] in arts and all(arts[p["path"]][k] == p[k] for k in ("inode", "sha256", "bytes")) for p in pubs),
                      "exactly one original native publication return per role, equal to the current artifact")
            sizes = arts[receipt]["bytes"] + arts[final]["bytes"]
            if summ.get("acknowledged") is True:
                exact(integer(summ.get("receipt_bytes")) and integer(summ.get("settlement_bytes")), "exported actual publication sizes required")
                self.need(summ["receipt_bytes"] == arts[receipt]["bytes"] and summ["settlement_bytes"] == arts[final]["bytes"],
                          "exported receipt/settlement sizes equal the actual independently read artifacts")
            exact(integer(summ.get("publication_payload_bytes")) and type(summ.get("ack_resources")) is dict and
                  type(summ.get("publication_resources")) is dict, "actual payload and publication/end accounting evidence required")
            self.need(summ["publication_payload_bytes"] == sizes, "exported payload total equals actual publication bytes")
            charged = inventory(self.run + "/out")[1] + inventory(self.run + "/tmp")[1]
            self.need(summ["ack_resources"]["charged_bytes"] == charged, "end accounting equals independent distinct-inode out+tmp total")
            self.need(summ["publication_resources"]["charged_bytes"] == charged - sizes, "pre-payload accounting equals actual total minus publication bytes")
            recon = s["reconciliation"]
            self.need(recon["publication_payload_bytes"] == sizes and same(recon["publication_resources"], summ["publication_resources"]) and
                      same(recon["ack_resources"], summ["ack_resources"]) and
                      all(any(a["retained"] is True and a["returned"] is True and same(a["resources"], r) for a in recon["accounting_observations"])
                          for r in (summ["publication_resources"], summ["ack_resources"])), "publication/end accounting joins complete retained returned source observations")
            history = decode(regular(receipt, 4 << 20)[1])
            current = s["reconciliation"]["helpers"]
            extra = 1 if self.case == "nat_post_publication_stop_helper" else 0
            self.need(type(history.get("helpers")) is list and same(current[:len(history["helpers"])], history["helpers"]) and
                      len(current) == len(history["helpers"]) + extra, "immutable historical helper prefix joins current helpers")
        for path, original in s["created"].items():
            self.need(path in arts and arts[path]["inode"] == original, "every source-created artifact present with its original inode")
    def canonical_identity(self, identity, ref):
        recon = self.state()["reconciliation"]
        if not integer(ref) or not 1 <= ref <= len(recon["identity_events"]):
            return False
        event = recon["identity_events"][ref - 1]
        histories = [h for h in recon["identity_history"] if h["first_identity"]["uniqueid"] == identity["uniqueid"]]
        return (len(event) == 6 and event[0] == identity["uniqueid"] and integer(event[1]) and len(histories) == 1 and
                0 <= event[1] < len(histories[0]["variants"]) and fingerprint(histories[0]["variants"][event[1]]) == fingerprint(identity) and
                event[2] == identity["status"] and number(event[3]) and number(event[4]) and event[3] <= event[4])
    def helper_proof(self, h, valid_clock=False):
        exact(type(h) is dict and integer(h.get("pid")) and h["pid"] > 1, "helper report")
        self.need(type(h["identity"]) is dict and h["identity"]["pid"] == h["pid"] == h["identity"]["pgid"] and h["initial_identity_valid"] is True,
                  "helper acquired original full native identity")
        if type(h["identity"]) is dict:
            fingerprint(h["identity"])
            self.need(self.canonical_identity(h["identity"], h.get("identity_event_ref")), "helper initial identity joins its original canonical acquisition event/history")
        if type(h.get("proof")) is dict:
            self.need(any(all(same(c.get(k), h["proof"].get(k)) for k in ("complete", "incomplete_n", "owned_live", "unproved_live", "mono_complete"))
                          for c in self.state()["reconciliation"]["census_observations"]), "helper ownership proof joins an actual retained census observation")
        rows = [r for r in self.ledger if r[1] == h["pid"]]
        if h["leader_reaped"]:
            raw = h["native_wait_result"]
            exact(type(raw) is list and len(raw) == 2 and integer(raw[0]) and integer(raw[1]) and raw[1] >= 0 and
                  integer(h["raw_wait_status"]) and integer(h["rc"]), "helper exact-typed destructive tuple/status retained")
            self.need(raw[0] == h["pid"] and raw[1] == h["raw_wait_status"] and (os.WIFEXITED(raw[1]) or os.WIFSIGNALED(raw[1])) and
                      os.waitstatus_to_exitcode(raw[1]) == h["rc"] and len(rows) == 1 and rows[0][0] == "source_waitpid" and rows[0][3] == raw[1],
                      "helper real destructive status retained once and ledgered")
        if h["settled"]:
            self.need(h["wait_lost"] is False and h["leader_reaped"] is True and h["group_clear"] is True and h["descendants_clear"] is True and
                      h["coverage_complete"] is True and h["stdout_closed"] is True and h["eof_proved"] is True and type(h["proof"]) is dict and
                      h["proof"]["complete"] is True and h["proof"]["owned_live"] == [] and h["proof"]["unproved_live"] == [], "helper settlement conjunction not reap-only")
        if valid_clock:
            exact(type(h.get("identity")) is dict and type(h.get("proof")) is dict and type(h.get("native_wait_result")) is list and
                  integer(h.get("raw_wait_status")) and integer(h.get("rc")) and type(h.get("date")) is str and type(h.get("capture_hex")) is str and
                  all(type(h.get(k)) is bool for k in ("leader_reaped", "wait_lost", "settled", "initial_identity_valid", "stdout_closed", "eof_proved", "group_clear", "descendants_clear", "coverage_complete")),
                  "complete required owned /bin/date identity/wait/closure/EOF/capture proof is available")
            exact(all(number(h.get(k)) for k in ("mono_call_start", "mono_call_deadline", "mono_spawn", "mono_reaped", "mono_proof_complete")) and
                  type(h.get("call_deadline")) is dict and set(h["call_deadline"]) == {"mono_created", "seconds", "until", "end"} and
                  number(h["call_deadline"]["mono_created"]) and number(h["call_deadline"]["seconds"]) and number(h["call_deadline"]["end"]) and
                  (h["call_deadline"]["until"] is None or number(h["call_deadline"]["until"])), "required owned /bin/date timing and deadline proof available")
            cd = h["call_deadline"]
            end = cd["mono_created"] + cd["seconds"] if cd["until"] is None else min(cd["mono_created"] + cd["seconds"], cd["until"])
            s = self.state()
            cuts = [s["reconciliation"]["initial_fit"]["fit_mono"]]
            if type(s.get("stop")) is dict and number(s["stop"].get("mono")) and s["stop"]["mono"] <= cd["mono_created"]:
                cuts.append(s["stop"]["mono"] + self.cfg["settle_s"])
            mw = s["reconciliation"].get("main_wait")
            if type(mw) is dict and number(mw.get("mono_reaped")) and mw["mono_reaped"] <= cd["mono_created"]:
                cuts.append(mw["mono_reaped"] + self.cfg["settle_s"])
            self.need(same(cd["seconds"], self.cfg["helper_budget"]["call_budget_s"]) and cd["until"] == min(cuts) and
                      cd["end"] == end and h["mono_call_deadline"] == cd["end"],
                      "helper call deadline provenance from fixed budget, original fit, and original stop/exit cutoffs")
            self.need(h["settled"] is True and h["rc"] == 0 and type(h["date"]) is str and bytes.fromhex(h["capture_hex"]) == (h["date"] + "\n").encode("ascii") and
                      h["term_attempted"] is False and h["signal"] is None and h["wait_lost"] is False and
                      h["mono_call_start"] <= h["mono_spawn"] <= h["mono_reaped"] <= h["mono_call_deadline"] and h["mono_proof_complete"] <= h["mono_call_deadline"],
                      "only timely settled owned /bin/date bytes constitute actual metadata")
    def required_helpers(self):
        # Exact original date_now call outcomes for every full-main case. Non-clock refusals are retained
        # log entries with no PID/date; they never substitute for a missing required native clock helper.
        refused = "REFUSED_FAILURE_CANCEL_OR_REENTRANCY"
        before_main = [["admission", "OK"], ["start", "OK"], ["end", refused]]
        failed_start = [["admission", "OK"], ["start", "FAILED"], ["end", refused]]
        stopped = [["admission", "OK"], ["start", "OK"], ["stop", refused], ["end", refused]]
        case = self.case
        if case == "nat_runtime_1000":
            return [["admission", "OK"], ["start", "OK"], ["stop", "OK"], ["end", "OK"]]
        if case == "nat_runtime_1026":
            return [["admission", "OK"], ["start", "OK"], ["stop", "OK"], ["end", refused]]
        if case in ("nat_ack_existing_blocker_subset", "nat_ack_additional_blocker"):
            return [["admission", "OK"], ["start", "OK"], ["end", "OK"], ["stop", refused]]
        if case == "nat_post_publication_stop_helper":
            return [["admission", "OK"], ["start", "OK"], ["end", "OK"], ["stop", "OK"]]
        if case.endswith("before_helper") or case in ("nat_helper_late_successful_reap", "nat_helper_pre_spawn_allocation_failure", "nat_helper_registered_pid_setup_failure"):
            return failed_start
        if case.endswith("before_main"):
            return before_main
        if ((case in GO and not case.endswith("_lt")) or case.endswith("go_write") or case == "nat_pending_after_handled" or
                case in ("nat_protected_go_expiry", "nat_protected_go_stability", "nat_completion_go_deadline", "nat_cap_final_rss", "nat_cap_initial_main",
                         "nat_platform_startup_reexec", "nat_platform_fast_exit_zombie")):
            return stopped
        return CLEAN
    def helper_population(self, required=None):
        required = self.required_helpers() if required is None else required
        s = self.state()
        recon = s["reconciliation"]
        helpers, log = recon["helpers"], recon["helper_log"]
        exact(type(helpers) is list and type(log) is list and all(type(e) is dict and type(e.get("purpose")) is str and type(e.get("outcome")) is str for e in log),
              "helper report/log histories")
        spawned = [e for e in self.events("native_spawn_registered") if e["role"] == "helper"]
        logged = [e for e in log if e.get("pid") is not None]
        exact(sorted(e["pid"] for e in logged) == sorted(h["pid"] for h in helpers) == sorted(e["pid"] for e in spawned) and
              len({h["pid"] for h in helpers}) == len(helpers), "one-to-one helper log/report/native registration join")
        by_pid = {h["pid"]: h for h in helpers}
        dates = {}
        for entry in logged:
            h = by_pid[entry["pid"]]
            reg = next(e for e in spawned if e["pid"] == entry["pid"])
            self.need(reg["purpose"] == entry["purpose"] and reg["argv"] == DATE_ARGV, "native helper registration purpose/argv joins its source call")
            if entry["outcome"] == "OK":
                self.helper_proof(h, True)
                dates[entry["purpose"]] = h["date"]
            else:
                self.need(h["date"] is None, "failed/refused helper call never supplies a date")
        admission = s["rec"].get("admission")
        self.need(type(admission) is dict and admission.get("date") == dates.get("admission") and type(dates.get("admission")) is str and
                  bool(log) and [log[0]["purpose"], log[0]["outcome"]] == ["admission", "OK"], "genuine owned /bin/date admission precedes every full-main outcome")
        for purpose, value in (("start", s["rec"].get("start_date")), ("end", s["rec"].get("end_date")), ("stop", (s["stop"] or {}).get("date"))):
            self.need(value == dates.get(purpose), "source %s date equals its owned /bin/date helper bytes or null" % purpose)
        if required is not None:
            self.need([[e["purpose"], e["outcome"]] for e in log] == required, "exact case-specific owned /bin/date helper population")
    def quiet_host(self):
        # Prerequisite, evaluated BEFORE dependent outcome predicates: no foreign post-baseline identity,
        # foreign coverage gap or foreign busy lane member in any retained source census.
        s = self.state()
        recon = s["reconciliation"]
        admission = s["rec"].get("admission")
        if self.outcome["original_main_called"] is True and (type(admission) is not dict or admission.get("reasons") != []):
            self.absent("original native admission prerequisites unavailable; observed admission reasons retained: " + str(admission))
            return False
        probes = self.outcome["fixture_processes"]
        allowed = {p["identity"]["uniqueid"] for p in probes if type(p.get("identity")) is dict}
        member = self.run + "/scratch/helper-member-owner.json"
        if member in self.artifacts:
            allowed.add(decode(regular(member)[1])["identity"]["uniqueid"])
        own_pids = {p["pid"] for p in probes} | {h["pid"] for h in recon["helpers"]} | {self.capture["pid"]}
        if s["pid"] is not None:
            own_pids.add(s["pid"])
        owned = {o["identity"]["uniqueid"] for o in recon["owned_identities"]}
        censuses = list(recon["census_observations"]) + [e["census"] for e in self.events("native_ACK_census_return")]
        foreign = []
        for c in censuses:
            foreign += [["unproved", p["pid"], p["uniqueid"]] for p in c.get("unproved_live", []) if p["uniqueid"] not in allowed]
            foreign += [["coverage", item[0]] for item in c.get("incomplete", []) if item[0] not in own_pids]
            foreign += [["busy_lane_member", m["identity"]["pid"]] for m in c.get("measurements", [])
                        if m.get("busy") is True and m["identity"]["pid"] not in own_pids and m["identity"]["uniqueid"] not in owned]
        if foreign:
            self.absent("quiet-host prerequisite not established; dependent outcome predicates not exercised; foreign=%s; observed actual_exit=%r failures=%r trips=%r" %
                        (json.dumps(foreign[:20]), self.capture["actual_exit"], s["failure_codes"], sorted(s["trips"])))
            return False
        return True
    def main_wait_join(self):
        s = self.state()
        mw, pid = s["reconciliation"]["main_wait"], s["pid"]
        exact(integer(pid) and type(mw) is dict and integer(mw.get("pid")) and mw["pid"] == pid and integer(mw.get("raw_wait_status")) and
              integer(mw.get("rc")) and integer(s.get("rc")) and type(mw.get("native_wait_result")) is list and
              len(mw["native_wait_result"]) == 2 and all(integer(v) for v in mw["native_wait_result"]), "installed main exact-typed wait/status record")
        waits = [e for e in self.events("native_waitpid") if e["pid"] == pid]
        success = [e for e in waits if "native_result" in e and e["native_result"][0]]
        rows = [r for r in self.ledger if r[1] == pid]
        exact(len(success) == 1 and len(rows) == 1 and rows[0][0] == "source_waitpid", "one destructive native main wait, ledgered")
        e = success[0]
        status = e["native_result"][1]
        self.need(e["native_result"] == [pid, status] and rows[0][3] == status and mw["native_wait_result"] == [pid, status] and
                  mw["raw_wait_status"] == status and mw["leader_reaped"] is True and (os.WIFEXITED(status) or os.WIFSIGNALED(status)),
                  "one destructive main result: native tuple, ledger, retained tuple and raw status agree")
        if os.WIFEXITED(status) or os.WIFSIGNALED(status):
            rc = os.waitstatus_to_exitcode(status)
            self.need(mw["rc"] == rc == s["rc"] and (self.summary is None or "child_returncode" not in self.summary or self.summary["child_returncode"] == rc),
                      "decoded native status equals source rc, wait record and summary child status")
        exact(number(mw["mono_reaped"]), "main reap time retained")
        self.need(waits[-1] is e and e["mono_after"] <= mw["mono_reaped"], "no wait after the destructive result; return precedes retained reap time")
        return e
    def clean_full(self, child=True, closure=True, population=None):
        s = self.state()
        final = s["rec"].get("final_census")
        if type(final) is not dict:
            self.need(False, "original final census missing")
            return
        if closure:
            self.need(final["complete"] is True and final["incomplete_n"] == 0 and final["owned_live"] == [] and final["group_live"] == [] and
                      final["unproved_live"] == [], "complete native final closure")
        self.helper_population(population)
        if s["pid"] is not None:
            e = self.main_wait_join()
        if child and s["pid"] is not None:
            path = self.cfg["outputs"][0]["path"]
            exact(path in self.artifacts, "actual child report prerequisite")
            facts, raw = regular(path, 256 << 10)
            report = decode(raw)
            self.need(report["kind"] == "rqls10-native-child-outcome-v1" and report["case"] == self.case and
                      report["approval_sha256"] == self.approval_sha and report["owner"]["pid"] == s["pid"] and report["owner"]["pgid"] == s["group"] and
                      report["science_acceptance"] is False and report["observed_maxrss_bytes"] <= 256 << 20, "native fixed child/report/source identity join")
            if type(s["rc"]) is int and s["rc"] >= 0:
                self.need(integer(report["selected_status_not_actual_exit"]) and report["selected_status_not_actual_exit"] == s["rc"], "child selected status equals its decoded native exit")
            self.child = report
            cstdout = regular(self.cfg["stdout"], 128 << 10)[1].splitlines(keepends=True)
            exact(cstdout and all(x.endswith(b"\n") for x in cstdout), "complete child stdout capture")
            owner = decode(cstdout[0])
            self.need(owner["pid"] == s["pid"] and owner["pgid"] == s["group"], "actual first child owner frame")
            record = decode(cstdout[-1])
            self.need(record.get("kind") == "rqls10-native-child-record-v1" and record.get("report_sha256") == facts["sha256"] and
                      same(record.get("artifact"), facts), "child actual created-descriptor artifact inode/hash joined through captured stdout")
    def exit(self, code=None):
        frozen = self.frozen["parent_actual_driver_exit"]
        exact(code is None or code == frozen, "oracle expectation contradicts the frozen case exit")
        self.need(self.capture["actual_exit"] == frozen, "exact parent actual exit=%d" % frozen)
    def source_errors(self):
        return [error_text(e["error"]) for e in self.events("original_completion_exception")]
    def strict_failures(self, expected, trips=()):
        s = self.state()
        src = self.frozen["source"]
        exact(("failures" not in src or set(src["failures"]) == set(expected)) and ("trips" not in src or set(src["trips"]) == set(trips)),
              "oracle failure/trip expectation contradicts the frozen case")
        # Frozen set only: no causal-exception broadening (REQUIRED_OUTPUT_MISSING is never added).
        self.need(set(s["failure_codes"]) == set(expected) and set(s["trips"]) == set(trips), "exact frozen source failures/trips")
    def runtime(self):
        s = self.state()
        marks = self.events("native_successful_wait_target")
        if not marks:
            self.absent("actual SZOMB-delayed original main wait not reached")
            return
        exact(len(marks) == 1, "one fixed runtime scheduling hook")
        mark = marks[0]
        e = self.main_wait_join()
        spawn = s["rec"]["mono_spawn"]
        exact(number(spawn) and number(e["mono_before"]) and number(e["mono_after"]), "native main wait interval")
        target = {RUNTIME[0]: 9.99, RUNTIME[1]: 10.0, RUNTIME[2]: 10.26}[self.case]
        upper = 10.0 if self.case == RUNTIME[0] else 10.01 if self.case == RUNTIME[1] else 10.27
        if not target <= e["mono_before"] - spawn <= e["mono_after"] - spawn < upper:
            self.absent("native successful-wait target window missed; no exact-equality substitution")
            return
        obs = s["rec"]["runtime_observations"]
        exact(type(obs) is list, "original runtime observations retained")
        if self.case == RUNTIME[0]:
            checks = [r for r in self.events("original_enforce_runtime") if r["where"] == "after_waitpid_including_success" and r["seq"] > e["seq"]]
            exact(bool(checks) and number(checks[0]["mono_after"]), "original post-success runtime decision interval observed")
            if not checks[0]["mono_after"] - spawn < 10.0:
                self.absent("original post-success runtime decision not entirely below the 10.00 cutoff; side missed")
                return
        elif len(obs) == 1 and number(obs[0].get("mono")):
            # Source19 L857-858: late iff now > cutoff + sample_s + 0.05, cutoff = spawn + max_wall_s.
            late = obs[0]["mono"] > (spawn + 10.0) + 0.2 + 0.05
            if late is not (self.case == RUNTIME[2]):
                self.absent("original runtime decision landed on the other late-enforcement side; not exercised")
                return
        if not self.quiet_host():
            return
        src = self.frozen["source"]
        self.need(type(mark["status_observed"]) is dict and mark["status_observed"]["status"] == 5 and number(mark["hook_begin"]) and
                  mark["hook_begin"] < spawn + 10.0 and mark["target_mono"] == spawn + target, "genuine zombie and pre-cutoff original call entry before native return")
        self.need(s["rc"] == src["child_rc"] == 0, "late native wait actually successful child0")
        self.exit()
        self.strict_failures(set(src["failures"]), tuple(src["trips"]))
        if self.case == RUNTIME[0]:
            self.need(obs == [], "before deadline no trip")
        else:
            self.need(len(obs) == 1 and obs[0]["where"] == "after_waitpid_including_success" and obs[0]["mono"] >= e["mono_after"] and
                      obs[0]["mono_deadline"] == spawn + 10.0, "original post-success runtime enforcement observation")
        stop = [["admission", "OK"], ["start", "OK"], ["stop", "OK"], ["end", "OK"]]
        self.clean_full(population=CLEAN if self.case == RUNTIME[0] else stop if self.case == RUNTIME[1] else None)
    def go_case(self):
        s = self.state()
        rec = s["rec"]
        c = rec.get("go_delivery_completion")
        if c is None:
            self.absent("valid prewrite gate and actual GO completion not reached")
            return
        exact(type(c) is dict and number(c.get("spawn_age_s")) and number(c.get("mono")), "original GO completion record")
        bound = min(60.0, self.cfg["max_wall_s"] / 2)
        label = self.case.rsplit("_", 1)[1]
        age = c["spawn_age_s"]
        if age == bound:
            self.absent("exact equality age==bound is source-accepted and STATE-only; never native eq coverage")
            return
        inside = {"lt": bound - 0.01 <= age < bound, "eq": bound < age < bound + 0.01, "gt": bound + 0.01 <= age < bound + 0.02}[label]
        if not inside:
            self.absent("actual original GO completion age outside the labelled side/window")
            return
        lead, delay, write = self.only("fixed_pre_GO_census_lead"), self.only("GO_native_delivery_delay"), self.only("native_GO_write")
        gd = delay["original_deadline"]
        exact(type(gd) is dict and number(gd.get("mono_created")) and number(gd.get("end")) and number(lead.get("mono_end")) and
              same(gd, delay["original_deadline_start"]), "GO deadline provenance retained")
        if not (gd["mono_created"] >= lead["mono_end"] and c["mono"] <= gd["end"]):
            self.absent("fresh original pre-GO deadline did not begin after the fixed lead, or dominated completion")
            return
        if not self.quiet_host():
            return
        late = age > bound
        src = self.frozen["source"]
        exact(late is bool(src["failures"]), "frozen GO side/outcome coherence")
        commit, census = rec["go_commit"], rec["pre_go_census"]
        self.need(s["go_delivered"] is True and c["spawn_age_bound_s"] == bound and c["spawn_age_s"] == c["mono"] - rec["mono_spawn"] and
                  c["remaining_main_runtime_s"] == rec["mono_spawn"] + self.cfg["max_wall_s"] - c["mono"] > 0,
                  "actual original GO completion age/remaining runtime")
        self.need(census["complete"] is True and census["unproved_live"] == [] and len(census["owned_live"]) == 1 and
                  fingerprint(census["owned_live"][0]) == fingerprint(s["identity"]) and
                  commit["mono"] < delay["injection_end"] <= write["mono_before"] <= write["mono_after"] <= c["mono"] and
                  c["mono"] - census["mono_complete"] <= 1.0 and commit["mono"] - rec["mono_spawn"] <= bound,
                  "valid fresh original prewrite gates then actual delayed native write/close/completion")
        self.exit(11 if late else 0)
        self.strict_failures(set(src["failures"]))
        if late:
            self.need("LATE_ACTUAL_GO_DELIVERY_OWNED_STOP" in self.source_errors() and s["signal"]["sent"] is True and
                      fingerprint(s["signal"]["identity_observed"]) == fingerprint(s["identity"]), "original late-GO owned stop and identity-checked TERM")
        self.clean_full(population=None if late else CLEAN)
    def ack_case(self):
        s, case = self.state(), self.case
        if not self.events("native_ACK_census_return"):
            self.absent("actual post-publication ACK census not reached")
            return
        if not self.quiet_host():
            return
        e = self.only("native_ACK_census_return")
        ack, final = e["census"], s["rec"].get("final_census")
        exact(type(ack) is dict and type(final) is dict, "final and ACK censuses retained")
        probes = {p["role"]: p for p in self.outcome["fixture_processes"]}
        roles = {"nat_ack_clean": set(), "nat_ack_new_unproved": {"ack"}, "nat_ack_incomplete": {"retry1", "retry2", "retry3"},
                 "nat_ack_disappearing_retry": {"ack"}, "nat_ack_existing_blocker_subset": {"final"}, "nat_ack_additional_blocker": {"final", "ack"}}[case]
        exact(len(probes) == len(self.outcome["fixture_processes"]) and set(probes) == roles, "fixed probe population")
        def uid(role):
            return probes[role]["identity"]["uniqueid"]
        finalids = {p["uniqueid"] for p in final["owned_live"] + final["unproved_live"]}
        ackids = {p["uniqueid"] for p in ack["owned_live"] + ack["unproved_live"]}
        self.need(final["owned_live"] == [] and ack["owned_live"] == [], "ACK blockers are unproved-class probes only")
        by_uid = {p["identity"]["uniqueid"]: p["identity"] for p in probes.values()}
        self.need(all(p["uniqueid"] in by_uid and fingerprint(p) == fingerprint(by_uid[p["uniqueid"]]) for p in final["unproved_live"] + ack["unproved_live"]),
                  "every final/ACK blocker is the exact original full probe incarnation, not a selected uniqueid")
        if case == "nat_ack_clean":
            self.need(finalids == ackids == set() and ack["complete"] is True and self.summary["acknowledged"] is True, "unchanged clean ACK coverage")
        elif case == "nat_ack_new_unproved":
            self.need(finalids == set() and ackids == {uid("ack")} and ack["complete"] is True and
                      any(fingerprint(p) == fingerprint(probes["ack"]["identity"]) for p in ack["unproved_live"]), "exactly the new probe identity after publication")
            self.need(self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING" and self.summary["acknowledged"] is False, "new U refuses ACK")
        elif case == "nat_ack_incomplete":
            vanished = self.events("native_probe_disappeared_before_identification")
            attempts = {}
            for row in self.events("original_census_return") + self.events("original_census_exception"):
                if row.get("ack_attempt") is not None:
                    attempts.setdefault(row["ack_attempt"], []).append(row)
            self.need(e["attempt_count"] == 3 and sorted(attempts) == [1, 2, 3] and all(len(v) == 1 for v in attempts.values()), "exactly three original ACK census attempts")
            for k in (1, 2, 3):
                p = probes["retry%d" % k]
                v = [r for r in vanished if r["attempt"] == k]
                rows = [r for r in self.ledger if r[1] == p["pid"]]
                att = attempts.get(k, [None])[0]
                self.need(len(v) == 1 and v[0]["pid"] == p["pid"] and v[0]["role"] == p["role"] and len(rows) == 1 and rows[0][0] == "fixture_probe" and
                          v[0]["native_wait_result"] == [p["pid"], rows[0][3]] == p["native_wait_result"], "retry probe reaped by its one ledgered driver wait before identification")
                ident = [r for r in self.events("original_observed_identity_exception") if r["pid"] == p["pid"] and r["source"] == "pid_scan" and r["ack_attempt"] == k]
                reaps = [r for r in self.events("native_probe_reaped") if r["pid"] == p["pid"]]
                self.need(len(ident) == 1 and ident[0]["error"]["type"] == "GuardError" and ident[0]["error"]["errno"] == errno.ESRCH and
                          re.fullmatch(r"\[Errno 3\] PIDINFO %d flavor 17 bytes -?\d+" % p["pid"], error_text(ident[0]["error"])) is not None and
                          len(reaps) == 1 and len(v) == 1 and reaps[0]["seq"] < v[0]["seq"] < ident[0]["seq"],
                          "actual original identify ESRCH after the probe's destructive reap, same ACK attempt")
                self.need(att is not None and att["operation"] == "original_census_return" and att["complete"] is False and len(ident) == 1 and
                          ident[0]["seq"] < att["seq"] and any(type(item) is list and item[:2] == [p["pid"], "identify"] and "[Errno 3]" in item[2] for item in att["incomplete"]),
                          "corresponding source identify ESRCH retained in the same ACK census incomplete history")
            self.need(ack["complete"] is False and ack["incomplete_n"] > 0 and not ackids and
                      self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING", "three disappearance retries leave incomplete ACK with no live blocker")
        elif case == "nat_ack_disappearing_retry":
            v = self.only("native_probe_disappeared_after_identity")
            p = probes["ack"]
            rows = [r for r in self.ledger if r[1] == p["pid"]]
            hist = s["reconciliation"]["census_observations"]
            self.need(v["pid"] == p["pid"] and fingerprint(v["identity_before"]) == fingerprint(p["identity"]) and len(rows) == 1 and
                      rows[0][0] == "fixture_probe" and v["native_wait_result"] == [p["pid"], rows[0][3]], "vanished identity is the probe reaped by its ledgered driver wait")
            self.need(ack["complete"] is True and not ackids and e["attempt_count"] >= 2 and
                      any(c["complete"] is False and any(q["uniqueid"] == uid("ack") for q in c["unproved_live"]) for c in hist) and
                      any(q["first_identity"]["uniqueid"] == uid("ack") for q in s["reconciliation"]["unproved_history"]),
                      "disappearing retry identity/coverage history retained, only final complete ACK empty")
        else:
            subset = case == "nat_ack_existing_blocker_subset"
            self.need(finalids == {uid("final")} and ackids == ({uid("final")} if subset else {uid("final"), uid("ack")}) and ack["complete"] is True,
                      "exact final/ACK blocker identities and cardinalities")
            self.need(self.summary["acknowledged"] is subset and (self.summary.get("settlement") == "UNSETTLED" if subset else
                      self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING"), "exact subset ACK11/additional refusal14")
        blocked = case in ("nat_ack_existing_blocker_subset", "nat_ack_additional_blocker")
        self.exit()
        self.strict_failures({"UNPROVED_LIVE"} if blocked else set())
        clean = case in ("nat_ack_clean", "nat_ack_disappearing_retry")
        self.clean_full(closure=not blocked, population=CLEAN if clean else None)
    def ack_age(self):
        if not self.events("ACK_native_output_delay"):
            self.absent("protected ACK output target not reached")
            return
        e, flush = self.only("ACK_native_output_delay"), self.only("native_ACK_flush_return")
        exact(number(flush["mono_after"]) and number(e["census_mono"]), "ACK timing evidence")
        target = {ACK_AGE[0]: 0.99, ACK_AGE[1]: 1.0, ACK_AGE[2]: 1.01}[self.case]
        measured = flush["mono_after"] - e["census_mono"]
        if not target <= measured < target + 0.01:
            self.absent("measured completion census-age window missed; no native equality claim")
            return
        late = self.case != ACK_AGE[0]
        rows = [r for r in self.events("original_resource_age_return") + self.events("original_resource_age_exception")
                if r["census_mono"] == e["census_mono"] and number(r["mono_before"]) and r["mono_before"] >= flush["mono_after"]]
        if not rows:
            self.absent("original post-completion fresh-age decision not reached")
            return
        exact(len(rows) == 1, "one original post-completion fresh-age decision")
        r = rows[0]
        side = r["mono_before"] - e["census_mono"] > 1.0 if late else r["mono_after"] - e["census_mono"] <= 1.0
        if not side:
            self.absent("original post-completion age decision interval not entirely on the labelled side")
            return
        if not self.quiet_host():
            return
        self.exit(14 if late else 0)
        self.strict_failures(set())
        self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0, "one printed ACK0 precedes actual completion decision")
        self.need((r["operation"] == "original_resource_age_exception") is late, "original decision kind matches the measured side")
        if late and r["operation"] == "original_resource_age_exception":
            self.need(error_text(r["error"]) == "RESOURCE_CENSUS_STALE_AT_COMMIT", "strict native age>1 refusal")
            self.post_ack_error(self.frozen["source"]["post_ACK_error"])
        self.clean_full(population=None if late else CLEAN)
    def post_ack_error(self, code):
        rows = self.streams["stderr"].splitlines(keepends=True)
        exact(len(rows) == 1 and rows[0].endswith(b"\n"), "complete single post-ACK diagnostic capture")
        diag = decode(rows[0])
        self.need(diag["kind"] == "POST_ACK_REFUSAL_EVIDENCE" and diag["exit_code"] == 14 and diag["error_code"] == code, "actual captured refusal cause after printed ACK")
    def signals(self):
        case, s = self.case, self.state()
        rows = self.events("native_self_signal")
        if case == "nat_pending_after_handled":
            expected = [(15, "go_write"), (1, "ACK_after_handled_TERM")]
        elif case == "nat_integration_printed_ack_actual14":
            expected = [(15, "ack_flush")]
        else:
            src = self.frozen["source"]
            exact(src.get("point") in ("before_helper", "before_main", "go_write", "ack_flush") and case.endswith(src["point"]) and
                  src.get("signal") == {"term": 15, "int": 2, "hup": 1}[case.split("_")[2]], "frozen exact named signal/point")
            expected = [(src["signal"], src["point"])]
        got = [(r.get("signum"), r.get("point")) for r in rows]
        if len(got) < len(expected) and got == expected[:len(got)]:
            self.absent("fixed own-signal point not reached")
            return
        self.need(got == expected, "exact named own signals at their fixed points; no TERM/INT/HUP substitution")
        for row in rows:
            exact(integer(row.get("signum")) and integer(row.get("pid")) and integer(row.get("pgid")), "native own-signal exact integer fields")
            fingerprint(row["identity"])
            self.need(row["pid"] == self.capture["pid"] and row["pgid"] == row["identity"]["pgid"] == self.capture["pgid"] and row["identity"]["pid"] == row["pid"] and
                      row["identity"]["euid"] == row["identity"]["ruid"] == s["rec"]["uid"], "only the approved freshly full-identified own process signalled")
            if row.get("point") in ("go_write", "ack_flush", "ACK_after_handled_TERM"):
                prior = 15 if row["point"] == "ACK_after_handled_TERM" else None
                self.need(row["signum"] in row["pending"] and row["source_cancel"]["signal"] == prior,
                          "named signal genuinely pending inside the protected operation, original source cancel latch preserved")
            else:
                self.need(row["source_cancel"]["signal"] == row["signum"], "unmasked named signal reached the original source cancellation handler")
        cancel = s["rec"].get("cancel")
        exact(type(cancel) is dict, "source cancellation latch retained")
        self.need(cancel.get("signal") == expected[0][0], "source cancellation latch is the first named signal")
        if not self.quiet_host():
            return
        if case.endswith("before_helper"):
            self.exit(10)
            self.strict_failures({"HELPER_CALL_FAILED"})
            self.need(s["pid"] is None and not any(e["purpose"] == "start" for e in self.events("native_spawn_registered")), "pending cancellation prevents helper creation")
        elif case.endswith("before_main"):
            self.exit(10)
            self.strict_failures(set())
            self.need(s["pid"] is None and not any(e["role"] == "child" for e in self.events("native_spawn_registered")), "pending cancellation prevents main creation")
        elif case.endswith("ack_flush") or case == "nat_integration_printed_ack_actual14":
            self.exit(14)
            self.strict_failures(set())
            self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0, "real pending masked ACK cancellation after printed ACK")
            self.post_ack_error("CANCEL_DURING_ACK_COMPLETION")
        else:
            self.strict_failures({"POST_SPAWN_FAILURE"}, {"SUPERVISOR_CANCEL"})
            self.need(s["go_delivered"] is True and s["signal"]["sent"] is True and "CANCEL_DURING_GO_COMPLETION" in self.source_errors() and
                      s["cancel_handled"] is True, "masked GO signal causes original owned stop with one verified TERM")
            if case == "nat_pending_after_handled":
                self.exit(14)
                self.need(self.summary.get("error_code") == "CANCEL_AT_ACK" and self.summary["acknowledged"] is False,
                          "new pending signal cannot inherit earlier handled-cancel authority")
            else:
                self.exit(11)
                self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 11, "owned cancelled result acknowledged UNSETTLED11 only")
        self.clean_full(child=s["pid"] is not None, closure=True, population=None)
    def protected(self):
        case, s = self.case, self.state()
        phase = "GO" if "_go_" in case else "ACK"
        rows = self.events("GO_native_delivery_delay" if phase == "GO" else "ACK_native_output_delay")
        if not rows:
            self.absent("actual protected native completion crossing not reached")
            return
        exact(len(rows) == 1, "one fixed protected delay")
        e = rows[0]
        recon = s["reconciliation"]
        if case in ("nat_completion_go_deadline", "nat_completion_ack_deadline"):
            clamp = self.only("fixed_original_deadline_clamp")
            exact(clamp["scope"] == "API_RESPONSE_INJECTION" and clamp["phase"] == phase and same(e["original_deadline"], clamp["deadline"]) and
                  same(e["original_deadline_start"], clamp["deadline"]) and number(e["injection_start"]) and number(e["injection_end"]),
                  "crossing joined to the exact clamped original deadline object")
            cutoff = clamp["deadline"]["end"]
            crossed = e["injection_start"] < cutoff < e["injection_end"]
            code = "DEADLINE_EXCEEDED"
        else:
            src = self.frozen["source"]
            exact(src.get("phase") == phase and src.get("cutoff_family") in ("AUTHORIZATION_EXPIRY", "STABILITY_EXPIRY") and
                  e.get("cutoff_family") == src["cutoff_family"], "frozen single cutoff family and phase")
            code = src["completion_error"]
            if src["cutoff_family"] == "AUTHORIZATION_EXPIRY":
                # No fallback epoch: the actual recorded injection start is mandatory.
                exact(number(e.get("injection_start_epoch_raw")) and number(e.get("epoch_end_raw")) and type(e.get("authorization_start")) is dict and
                      type(e.get("authorization")) is dict and type(recon.get("authorization")) is dict, "authorization cutoff provenance and recorded start")
                cutoff = self.go["not_after_epoch"]
                exact(e["authorization_start"]["not_after_epoch"] == e["authorization"]["not_after_epoch"] == recon["authorization"]["not_after_epoch"] == cutoff,
                      "cutoff joined to GO.json, source authorization and delay snapshots")
                crossed = e["injection_start_epoch_raw"] < cutoff < e["epoch_end_raw"]
            else:
                exact(number(e.get("injection_start")) and number(e.get("injection_end")) and number(e.get("stability_expiry_mono_start")) and
                      e["stability_expiry_mono_start"] == e["stability_expiry_mono"] == recon["stability_expiry_mono"], "stability cutoff provenance and recorded start")
                cutoff = e["stability_expiry_mono"]
                crossed = e["injection_start"] < cutoff < e["injection_end"]
        if not crossed:
            self.absent("recorded start < actual cutoff < end not established; already-late stimulus never qualifies")
            return
        completion = [v for v in self.events("original_GO_write_all_exception" if case == "nat_completion_go_deadline" else "original_completion_exception")
                      if v.get("phase", "GO") == phase]
        exact(len(completion) == 1, "one original protected completion refusal observed")
        comp = completion[0]
        if case in ("nat_protected_go_expiry", "nat_protected_ack_expiry"):
            exact(number(comp.get("mono_after")) and number(recon.get("stability_expiry_mono")), "completion-check interval and stability cutoff")
            if not recon["stability_expiry_mono"] > comp["mono_after"]:
                self.absent("stability cutoff also crossed by the completion check; other family dominated, not this case")
                return
        if case in ("nat_protected_go_stability", "nat_protected_ack_stability"):
            exact(number(comp.get("epoch_after")), "completion-check epoch interval")
            if not comp["epoch_after"] <= recon["authorization"]["not_after_epoch"]:
                self.absent("authorization cutoff also crossed by the completion check; other family dominated, not this case")
                return
            if phase == "GO" and self.summary.get("error_code") == "GO_EXPIRED_AT_ACK":
                self.absent("authorization expiry dominated the later ACK refusal; not a stability-only case")
                return
        if not self.quiet_host():
            return
        self.need(error_text(comp["error"]).split(" ", 1)[0] == code, "exact original protected completion error for the named cutoff")
        if phase == "GO" and case != "nat_completion_go_deadline":
            commit = s["rec"]["go_commit"]
            self.need(type(commit) is dict and commit["mono"] < e["injection_start"] and
                      (commit["epoch"] <= cutoff if case.endswith("_expiry") else commit["mono"] < cutoff), "original GO commit precedes the named cutoff")
        if phase == "ACK":
            commit = self.summary.get("ack_commit")
            self.need(type(commit) is dict and commit["mono"] < e["injection_start"] and
                      (case == "nat_completion_ack_deadline" or (commit["epoch"] <= cutoff if case.endswith("_expiry") else commit["mono"] < cutoff)),
                      "original ACK commit precedes the named cutoff")
        self.exit(11 if case == "nat_completion_go_deadline" else 14)
        if phase == "ACK":
            self.strict_failures(set())
            self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0, "post-ACK native crossing retains printed0/actual14")
            self.post_ack_error(code)
        elif case == "nat_completion_go_deadline":
            self.strict_failures({"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
            self.need(s["go_delivered"] is not True and s["signal"]["sent"] is True and self.summary["acknowledged"] is True and self.summary["exit_code"] == 11,
                      "native bytes returned late but original write_all guard prevents delivery commit; owned stop and ACK11")
        else:
            self.strict_failures({"POST_SPAWN_FAILURE"})
            self.need(s["go_delivered"] is True and s["signal"]["sent"] is True, "actual delivered GO followed by owned verified stop")
            self.need(self.summary.get("error_code") == self.frozen["source"]["later_refusal"] and self.summary["acknowledged"] is False,
                      "named cutoff family also refuses the later ACK")
        self.clean_full(population=None)
    def helper_full(self):
        case, s = self.case, self.state()
        recon = s["reconciliation"]
        helpers, log = recon["helpers"], recon["helper_log"]
        if case == "nat_helper_timely_success":
            if not self.quiet_host():
                return
            self.exit(0)
            self.strict_failures(set())
            self.clean_full(population=CLEAN)
            return
        start = [x for x in log if x.get("purpose") == "start"]
        exact(len(start) == 1, "one original start helper call")
        if case == "nat_helper_pre_spawn_allocation_failure":
            fault = self.events("fixed_allocation_fault")
            if not fault:
                self.absent("fixed pre-spawn allocation point not reached")
                return
        else:
            name = "native_helper_call_crossing" if case == "nat_helper_late_successful_reap" else "registered_PID_setup_crossing"
            if not self.events(name):
                self.absent("fixed helper crossing point not reached")
                return
            e = self.only(name)
            exact(integer(e.get("pid")) and number(e.get("injection_start")) and number(e.get("injection_end")) and number(e.get("call_deadline")),
                  "recorded helper injection interval and cutoff")
            h = next((x for x in helpers if x["pid"] == e["pid"]), None)
            exact(type(h) is dict and h["mono_call_deadline"] == e["call_deadline"] and type(h.get("call_deadline")) is dict and
                  h["call_deadline"]["end"] == e["call_deadline"] and same(e.get("call_deadline_telemetry"), h["call_deadline"]),
                  "crossing joined to the exact original helper call deadline object")
            if not e["injection_start"] < h["mono_call_deadline"] < e["injection_end"]:
                self.absent("helper injection began after its own call deadline or missed the real crossing")
                return
        if not self.quiet_host():
            return
        self.exit(10)
        self.strict_failures({"HELPER_CALL_FAILED"})
        self.need(s["pid"] is None and self.summary["settlement"] == "NOT_LAUNCHED" and self.summary["acknowledged"] is True and
                  start[0]["outcome"] == "FAILED" and s["rec"].get("start_date") is None, "start-helper failure cannot launch compute")
        error = start[0].get("error")
        if case == "nat_helper_pre_spawn_allocation_failure":
            fault = self.only("fixed_allocation_fault")
            self.need(fault["scope"] == "API_RESPONSE_INJECTION" and fault["native_call_made"] is False and fault["errno"] == errno.EMFILE and
                      not any(r["purpose"] == "start" for r in self.events("native_spawn_registered")) and start[0].get("pid") is None and
                      error == "OSError(24, 'fixed API allocation failure, no native exhaustion')", "exact fixed pre-spawn API allocation failure with no PID")
            pipes = [r for r in self.events("native_source_pipe") if r["purpose"] == "start"]
            closed = {r["fd"] for r in self.events("native_source_close")}
            self.need(len(pipes) == 1 and set(pipes[0]["fds"]) <= closed, "all actual pre-spawn allocated descriptors closed")
        else:
            h = next(x for x in helpers if x["pid"] == start[0].get("pid"))
            self.helper_proof(h)
            self.need(h["date"] is None and h["leader_reaped"] is True and h["settled"] is True, "late/setup-failed clock call never supplies a date but original cleanup settles")
            if case == "nat_helper_late_successful_reap":
                self.need(h["rc"] == 0 and number(h["mono_reaped"]) and h["mono_reaped"] > h["mono_call_deadline"] and
                          error == "GuardError('DEADLINE_EXCEEDED after helper reap, including a successful reap')",
                          "actual native successful late reap rejected by the original post-reap deadline check")
            else:
                self.need(h["spawn_error"] == "GuardError('DEADLINE_EXCEEDED fixed registered-PID setup completion')" and
                          error == "GuardError(%r)" % h["spawn_error"] and self.only("registered_PID_setup_crossing")["native_PID_registered"] is True,
                          "returned PID retained through the exact original setup deadline exception")
        self.clean_full(child=False, population=None)
    def method_population(self, h):
        recon = self.state()["reconciliation"]
        helpers, log = recon["helpers"], recon["helper_log"]
        regs = [r for r in self.events("native_spawn_registered") if r["role"] == "helper"]
        exact(type(log) is list and len(log) == 1 and log[0]["purpose"] == "admission" and log[0]["outcome"] == "OK" and
              len(helpers) == len(regs) == 2 and {r["pid"] for r in regs} == {x["pid"] for x in helpers} == {log[0]["pid"], h["pid"]},
              "method helper population is exactly the actual admission clock plus the declared negative helper")
        self.helper_proof(next(x for x in helpers if x["pid"] == log[0]["pid"]), True)
        self.need(same(next(x for x in helpers if x["pid"] == h["pid"]), h), "negative method report equals its complete current helper row")
        expected = self.spec["negative_authority"]["separate_helper_or_probe_argv"]
        exact(type(expected) is list, "frozen method helper argv")
        argv = [self.request["python"]["path"] if x == "ACTUAL_PINNED_PYTHON" else x for x in expected]
        admission = next(r for r in regs if r["pid"] == log[0]["pid"])
        self.need(admission["purpose"] == "admission" and admission["argv"] == DATE_ARGV, "method prestate admission is the actual original owned /bin/date, not the negative helper")
        negative = next(r for r in regs if r["pid"] == h["pid"])
        self.need(negative["purpose"] is None and negative["argv"] == argv and
                  self.outcome["source_outcome"]["negative_argv"] == argv, "declared fixed separate helper argv, never an actual clock substitution")
    def helper_method(self):
        out, case = self.outcome["source_outcome"], self.case
        exact(type(out) is dict and out.get("mode") == "ORIGINAL_HELPER_METHODS", "original native helper methods mode")
        h = out.get("helper")
        if h is None:
            self.absent("method-negative native helper not acquired (genuine /bin/date admission or helper spawn prerequisite)")
            return
        exact(out["source_date_now_not_replaced"] is True, "original native helper methods, not production clock substitution")
        s = self.state()
        recon = s["reconciliation"]
        if recon["history_halted"]:
            self.absent("unrelated original history cap prevented the named helper lifecycle boundary")
            return
        declaration = self.only("declared_native_method_helper")
        frozen = self.frozen["source"]
        exact(type(frozen.get("error_family")) is str and type(frozen.get("settled")) is bool and frozen.get("output_clock_date") is None,
              "frozen helper-method exceptional outcome")
        exc = out["exception"]
        exact(exc is not None, "original method exception record retained")
        text, family = error_text(exc), exception_code(exc)
        x = self.only("original_helper_method_exception")
        exact(same(x["error"], exc) and x["helper_pid"] == h["pid"] and number(x["mono_call_deadline"]) and
              x["mono_call_deadline"] == h["mono_call_deadline"] == declaration["call_deadline"]["end"], "exception event joined to the method call deadline object")
        if family == "DEADLINE_EXCEEDED" and frozen["error_family"] != "DEADLINE_EXCEEDED":
            self.absent("original call deadline expired before the named method boundary was reached")
            return
        self.method_population(h)
        if not self.quiet_host():
            return
        self.exit(0)
        expected = {"HELPER_CALL_FAILED"} | (set() if frozen["settled"] else {"HELPER_OWNERSHIP_UNSETTLED"})
        if "latched_failure_family" in frozen:
            expected.add(frozen["latched_failure_family"])
        self.strict_failures(expected)
        self.need(declaration["date_assignment_forbidden"] is True and declaration["source_phase"] == "RUNNING" and
                  declaration["phase_scope"] == "DECLARED_METHOD_PRESTATE_NOT_PRODUCTION_LAUNCH" and h["date"] is None, "declared running-phase native methods, never clock substitution")
        self.need(family == frozen["error_family"], "exact original exceptional family for this method case")
        site = {"HELPER_BAD_DATE_OUTPUT": exc["type"] == "GuardError" and exc["errno"] is None and text == "HELPER_BAD_DATE_OUTPUT",
                "HELPER_EXEC_OR_CREDENTIAL_CHANGE": exc["type"] == "GuardError" and exc["errno"] is None and text == "HELPER_EXEC_OR_CREDENTIAL_CHANGE",
                "OS_ERROR_5": exc["type"] == "OSError" and exc["errno"] == 5 and text == "[Errno 5] fixed API close error; owned descriptor remains open",
                "OS_ERROR_3": exc["type"] == "GuardError" and exc["errno"] == errno.ESRCH and
                              re.fullmatch(r"\[Errno 3\] PIDINFO %d flavor 17 bytes -?\d+" % h["pid"], text) is not None,
                "DEADLINE_EXCEEDED": exc["type"] == "GuardError" and exc["errno"] is None and text.startswith("DEADLINE_EXCEEDED ") and
                                     x["mono"] > h["mono_call_deadline"]}.get(frozen["error_family"], False)
        self.need(site, "exact original exception site/type/errno for the frozen family; other errno or a missing original path is never accepted")
        self.need(h["settled"] is frozen["settled"], "frozen settlement evidence")
        self.helper_proof(h)
        if case in ("nat_helper_bad_output", "nat_helper_nonzero_exit"):
            self.need(h["rc"] == (3 if case == "nat_helper_nonzero_exit" else 0) and b"20" not in bytes.fromhex(h["capture_hex"])[:4],
                      "exact original output-check AST refuses native invalid/nonzero fixture output, never a date")
        elif case == "nat_helper_lost_wait":
            reaper = self.only("native_competing_reaper")
            rows = [r for r in self.ledger if r[1] == h["pid"]]
            echild = [w for w in self.events("native_waitpid") if w["pid"] == h["pid"] and "error" in w]
            recheck = [w for w in self.events("original_observed_identity_exception") if w["pid"] == h["pid"] and w["source"] == "measurement_bracket"]
            exact(len(recheck) == 1 and same(recheck[0]["error"], exc) and recheck[0]["seq"] < x["seq"],
                  "native ESRCH at the original same-helper identity re-check site is present, not a selected family")
            self.need(reaper["pid"] == h["pid"] and len(rows) == 1 and rows[0][0] == "competing_fixture_reaper" and rows[0][3] == reaper["native_result"][1] and
                      len(echild) == 1 and echild[0]["error"]["type"] == "ChildProcessError" and echild[0]["error"]["errno"] == errno.ECHILD and
                      reaper["seq"] < echild[0]["seq"] < recheck[0]["seq"] < x["seq"] and h["wait_lost"] is True and h["leader_reaped"] is False and
                      h["term_attempted"] is False and h["signal"] is None,
                      "competing destructive reap, then original ECHILD latch, then the ESRCH re-check; no recovered wait/signal right")
        elif case == "nat_helper_unverified_identity":
            owner = decode(regular(self.run + "/scratch/helper-owner.json")[1])
            post = decode(regular(self.run + "/scratch/helper-postexec.json")[1])
            self.need(owner["pid"] == post["identity"]["pid"] == h["pid"] and fingerprint(owner["identity"]) == fingerprint(h["identity"]) and
                      post["identity"]["uniqueid"] == h["identity"]["uniqueid"] and post["identity"]["idversion"] != h["identity"]["idversion"] and
                      h["settled"] is False and not (h.get("signal") or {}).get("sent"), "native reexec of the same incarnation; no TERM under a stale fingerprint")
        elif case in ("nat_helper_live_group", "nat_helper_live_descendant_unproved"):
            member = decode(regular(self.run + "/scratch/helper-member-owner.json")[1])
            registration = decode(regular(self.run + "/scratch/helper-fork-registration.json")[1])
            gate = decode(regular(self.run + "/scratch/helper-member-gate.json")[1])
            self.need(registration["pid"] == member["pid"] == gate["pid"] and registration["parent_pid"] == h["pid"] and
                      fingerprint(registration["parent_identity"]) == fingerprint(h["identity"]) and
                      member["identity"]["pid"] == member["pid"] and gate["raw_hex"] == b"R".hex() and gate["eof"] is True and
                      registration["mono_registered"] <= gate["mono_end"] and member["mono_begin"] <= gate["mono_end"],
                      "native descendant owner and parent fork registration precede fixed gate release and bounded work")
            proof = h["proof"]
            listed = proof["owned_live"] + proof["unproved_live"]
            self.need(any(p["pid"] == member["pid"] for p in listed) and h["settled"] is False and h["leader_reaped"] is True and
                      (h["group_clear"] is False if case.endswith("live_group") else h["descendants_clear"] is False or h["coverage_complete"] is False),
                      "genuine live helper group/descendant/unproved member prevents settlement")
        elif case == "nat_helper_missing_eof":
            held, closed = self.only("native_extra_pipe_writer_held"), self.only("native_extra_pipe_writer_closed")
            self.need(held["fd"] == closed["fd"] and held["mono"] < closed["mono"] and h["leader_reaped"] is True and h["rc"] == 0 and
                      h["stdout_closed"] is False and h["eof_proved"] is False and h["settled"] is False, "real held writer prevents EOF despite native date reap, bounded own close afterward")
        elif case == "nat_helper_close_error":
            fault = self.only("fixed_close_fault")
            self.need(fault["scope"] == "API_RESPONSE_INJECTION" and fault["native_close_made"] is False and fault["descriptor_retained"] is True and
                      h["settled"] is True and h["stdout_closed"] is True, "API close error retains the real descriptor until bounded native retry closes")
        elif case == "nat_helper_grace_exhaustion":
            self.need(type(h["signal"]) is dict and h["signal"]["sent"] is True and h["settled"] is False and h["leader_reaped"] is False and
                      number(h["mono_cleanup_deadline"]) and h["mono_cleanup_deadline"] <= self.only("native_helper_method_end")["mono"],
                      "one actual TERM ignored; original grace exhaustion remains blocking")
    def caps(self):
        case, s = self.case, self.state()
        if not self.events("fixed_history_cap_precharge"):
            self.absent("fixed cap reservation point not reached")
            return
        cap = self.only("fixed_history_cap_precharge")
        recon = s["reconciliation"]
        overflow = recon["history_overflow"]
        exact(type(overflow) is dict and number(overflow.get("mono")) and type(recon["raw_acquisitions"]) is list, "original history overflow record retained")
        if not self.quiet_host():
            return
        raws = recon["raw_acquisitions"]
        end = overflow["mono"]
        self.need(cap["scope"] == "API_CAP_STATE_INJECTION_NOT_NATIVE_COUNT" and cap["injected_charge"] == 4 << 20 and cap["native_cap_attainment_claim"] is False and
                  integer(cap["before_charge"]) and 0 <= cap["before_charge"] < 4 << 20, "fixed API cap pressure distinct from model/native-count claims")
        self.need(recon["history_halted"] is True and overflow["kind"] == "HISTORY_BYTE_CAP" and end >= cap["mono"] and same(overflow["witness"], cap["witness"]),
                  "original cap latch from the precharged original reservation witness")
        after = [r for r in self.events("original_census_return") if number(r.get("mono_entry")) and r["mono_entry"] > end]
        refused = [r for r in self.events("original_census_exception") if number(r.get("mono_entry")) and r["mono_entry"] > end]
        self.need(not after and all(error_text(r["error"]).startswith("HISTORY_ALREADY_HALTED") for r in refused) and
                  all(c["mono_start"] <= end for c in recon["census_observations"]) and all(a["mono_start"] <= end for a in recon["observation_attempts"]),
                  "complete call trace: every census after the halt refused, no resumed scan or attempt")
        def raw_signal(sig, source):
            return any(r.get("id") == sig.get("raw_identity_ref") and r.get("source") == source and r.get("native_returned") is True and
                       same(r.get("identity"), sig.get("identity_observed")) for r in raws)
        if case in ("nat_cap_final_rss", "nat_cap_initial_main"):
            self.helper_population()
            sig = s["signal"]
            self.need(type(sig) is dict and sig["sent"] is True and sig["identity_event_ref"] is None and raw_signal(sig, "main_signal") and
                      number(sig.get("mono_sent")) and sig["mono_sent"] > cap["mono"], "surviving raw main signal witness after the cap, no invented canonical event")
            self.main_wait_join()
            self.need(s["go_delivered"] is not True if case == "nat_cap_initial_main" else True, "no GO after the initial cap")
            self.exit(13)
            self.need(self.summary["reason"] == "FINALIZATION_FAILED" and self.summary["error_code"] == "HISTORY_ALREADY_HALTED", "exact cap finalization refusal13")
        if case == "nat_cap_final_rss":
            m, w = overflow.get("completed_measurement"), overflow.get("witness")
            exact(type(m) is dict and type(w) is dict, "retained completed resource bracket and witness after cap")
            self.need(w.get("source") == "measurement_final_bracket" and same(overflow.get("completed_identity_observation"), w) and
                      fingerprint(w["identity"]) == fingerprint(m["identity_after"]) and w["identity"]["pid"] == s["pid"], "final bracket witness is the completed main acquisition")
            self.need(m["bracket_verified"] is True and m["identity"]["pid"] == s["pid"] and fingerprint(m["identity"]) == fingerprint(m["identity_after"]) == fingerprint(s["identity"]) and
                      m["rss"] > self.cfg["rss_trip_bytes"] and m["rss"] <= 256 << 20, "actual final identity bracket and native RSS excess")
            task = [r for r in raws if r.get("kind") == "task" and same(r.get("measurement"), m)]
            bracket = [r for r in raws if r.get("kind") == "identity" and r.get("source") == "measurement_final_bracket" and r.get("native_returned") is True and
                       same(r.get("identity"), m["identity_after"])]
            self.need(len(task) == 1 and task[0]["native_returned"] is True and task[0]["native_result"] == [m["rss"], m["cpu_ticks"]] and len(bracket) == 1,
                      "retained raw task and final-bracket acquisition composites")
            aborted = [c for c in recon["census_observations"] if c["aborted"] is True]
            exact(len(aborted) == 1, "one aborted partial census retained")
            c = aborted[0]
            total, crossed = 0, None
            for meas in c["measurements"]:
                total += meas["rss"]
                if crossed is None and total > self.cfg["rss_trip_bytes"]:
                    crossed = total
            trip = s["trips"].get("RSS")
            self.need(type(trip) is dict and crossed is not None and trip["detail"] == crossed and c["lane_rss"] == total and any(same(meas, m) for meas in c["measurements"]),
                      "partial total and RSS latch equal the retained measurement prefix; completed measurement inside the aborted census")
            attempts = [a for a in recon["observation_attempts"] if a["kind"] == "resource_scan" and a["aborted"] is True]
            self.need(number(c.get("mono_aborted")) and number(c.get("mono_end")) and c["mono_aborted"] <= c["mono_end"] and "HISTORY_BYTE_CAP" in (c.get("abort_error") or "") and
                      len(attempts) == 1 and number(attempts[0]["mono_end"]) and "HISTORY_BYTE_CAP" in (attempts[0]["error"] or ""), "aborted census/attempt retain abort and end records")
        elif case == "nat_cap_initial_main":
            w, p = overflow.get("witness"), s["rec"].get("main_initial_identity_observed")
            exact(type(w) is dict and type(p) is dict, "initial acquisition witness retained")
            self.need(w.get("source") == "main_initial" and same(overflow.get("completed_identity_observation"), w) and
                      fingerprint(w["identity"]) == fingerprint(p) == fingerprint(s["identity"]) and s["group"] == s["pid"], "actual initial identity installed before the auxiliary cap")
            raw = [r for r in raws if r.get("kind") == "identity" and r.get("source") == "main_initial" and r.get("native_returned") is True and same(r.get("identity"), w["identity"])]
            self.need(len(raw) == 1 and number(raw[0]["mono_begin"]) and number(raw[0]["mono_end"]) and raw[0]["event_ref"] is None and
                      fingerprint(s["signal"]["identity_observed"]) == fingerprint(p), "retained raw initial acquisition composite and signal identity")
        elif case == "nat_cap_helper_term":
            self.exit(0)
            h = self.method_helper()
            exact(type(h) is dict, "method cap helper retained")
            self.method_population(h)
            self.need(cap["source_kind"] == "resource_attempt" and cap["witness"] is None and overflow["witness"] is None and cap["helper_pid"] == h["pid"],
                      "cap at the helper's first original proof census reservation")
            self.helper_proof(h)
            sig = h["signal"]
            self.need(type(sig) is dict and sig["sent"] is True and h["leader_reaped"] is True and h["rc"] == -15 and h["settled"] is False and
                      sig["identity_event_ref"] is None and number(sig.get("mono_sent")) and cap["mono"] < sig["mono_sent"] and raw_signal(sig, "helper_signal"),
                      "native cleanup TERM after cap; raw fingerprint/send/reap survives unavailable proof")
    def platform(self):
        case = self.case
        if case in PLATFORM_METHOD:
            self.exit(0)
        if case == "nat_platform_abi_layout":
            e = self.only("native_ABI_layout")
            exact(set(e["pinned_files"]) == set(ABI), "complete fixed ABI input set")
            contents = {}
            for role, pin in ABI.items():
                facts, raw = regular(pin["path"])
                exact(facts["sha256"] == pin["sha256"] and same(facts, e["pinned_files"][role]), "actual original/current pinned ABI input: " + role)
                contents[role] = raw
            sdk, private = contents["sdk"], contents["private"]
            self.need(sha(sdk) == "e427fa96b348537b21552b9de71e01039410bcad2cedee5584c5e5fddafd70fc" and
                      sha(private) == "ccc01e88d5bf47bc9c3f5ba3a25c3e6202bbcd7b86aa967af31d714657571c3b", "exact pinned public/private ABI headers")
            # Independent flat-struct layout computation from actual pinned C
            # declarations (not driver/source offsets). Darwin arm64 primitive ABI.
            def layout(raw, name):
                text = raw.decode()
                body = re.search(r"struct\s+" + name + r"\s*\{(.*?)\};", text, re.S)
                exact(body is not None, "pinned ABI struct declaration")
                body = re.sub(r"/\*.*?\*/", "", body.group(1), flags=re.S)
                sizes = {"uint8_t": (1, 1), "char": (1, 1), "uint32_t": (4, 4), "int32_t": (4, 4), "uid_t": (4, 4), "gid_t": (4, 4), "uint64_t": (8, 8)}
                pos, maximum, fields = 0, 1, {}
                for decl in body.split(";"):
                    if not decl.strip():
                        continue
                    m = re.fullmatch(r"\s*(\w+)\s+(\w+)\s*(?:\[([^]]+)\])?\s*", decl)
                    exact(m is not None and m.group(1) in sizes, "flat pinned ABI field")
                    size, align = sizes[m.group(1)]
                    count = {"MAXCOMLEN": 16, "2 * MAXCOMLEN": 32}.get(m.group(3), int(m.group(3)) if m.group(3) and m.group(3).isdigit() else 1)
                    pos = (pos + align - 1) // align * align
                    fields[m.group(2)] = pos
                    pos += size * count
                    maximum = max(maximum, align)
                return (pos + maximum - 1) // maximum * maximum, fields
            us, u = layout(private, "proc_uniqidentifierinfo")
            ss, short = layout(sdk, "proc_bsdshortinfo")
            ts, task = layout(sdk, "proc_taskinfo")
            bs, bsd = layout(sdk, "proc_bsdinfo")
            self.need((us, ss, ts, bs) == (56, 64, 96, 136) and (u["p_uniqueid"], u["p_idversion"]) == (16, 32) and
                      (short["pbsi_pid"], short["pbsi_ppid"], short["pbsi_pgid"], short["pbsi_status"], short["pbsi_comm"], short["pbsi_flags"], short["pbsi_uid"], short["pbsi_ruid"]) == (0, 4, 8, 12, 16, 32, 36, 44) and
                      (task["pti_resident_size"], task["pti_total_user"], task["pti_total_system"]) == (8, 16, 24) and bsd["pbi_start_tvsec"] == 120, "independent C-layout offsets and native-return lengths")
            raws = {int(k): bytes.fromhex(v) for k, v in e["raw_by_flavor"].items()}
            self.need({k: len(v) for k, v in raws.items()} == {17: 56, 13: 64, 4: 96, 3: 136, 9: 2352}, "actual native ABI return sizes")
            ref, identity = e["native_reference"], e["original_identity"]
            fingerprint(identity)
            consumed = e["consumed_by_original"]
            exact(type(consumed) is list and [c["flavor"] for c in consumed] == [17, 13, 17, 13, 17, 4, 3, 9] and all(c["pid"] == ref["pid"] for c in consumed),
                  "exact native buffers consumed by original identify/task_of/start_of/cwd_of")
            bufs = [bytes.fromhex(c["raw_hex"]) for c in consumed]
            self.need(same(e["raw_by_flavor"], {str(c["flavor"]): c["raw_hex"] for c in consumed}),
                      "retained flavor buffers are exactly those decoded by the original methods, not contradictory separate samples")
            self.need([len(b) for b in bufs] == [56, 64, 56, 64, 56, 96, 136, 2352] and all(c["size"] == len(b) for c, b in zip(consumed, bufs)) and
                      [c["zombies"] for c in consumed] == [True, True, True, True, True, False, True, False], "consumed native buffer sizes/flags")
            if [len(b) for b in bufs] == [56, 64, 56, 64, 56, 96, 136, 2352]:
                ids = [(struct.unpack_from("=Q", bufs[i], u["p_uniqueid"])[0], struct.unpack_from("=i", bufs[i], u["p_idversion"])[0]) for i in (0, 2, 4)]
                self.need(ids[0] == ids[1] == ids[2] == (identity["uniqueid"], identity["idversion"]), "independent flavor17 decode equals original uniqueid/idversion")
                sh = bufs[3]
                flags = struct.unpack_from("=I", sh, short["pbsi_flags"])[0]
                decoded = {"pid": struct.unpack_from("=I", sh, short["pbsi_pid"])[0], "ppid": struct.unpack_from("=I", sh, short["pbsi_ppid"])[0],
                           "pgid": struct.unpack_from("=I", sh, short["pbsi_pgid"])[0], "status": struct.unpack_from("=I", sh, short["pbsi_status"])[0],
                           "euid": struct.unpack_from("=I", sh, short["pbsi_uid"])[0], "ruid": struct.unpack_from("=I", sh, short["pbsi_ruid"])[0],
                           "traced": bool(flags & 2),
                           "comm": sh[short["pbsi_comm"]:short["pbsi_comm"] + 16].split(b"\0")[0].decode("utf-8", "replace")}
                self.need(all(decoded[k] == identity[k] for k in decoded), "independent flavor13 decode equals original pid/ppid/pgid/status/UIDs/trace/comm")
                first_short = bufs[1]
                prior = {k: struct.unpack_from("=I", first_short, short[f])[0] for k, f in
                         (("pid", "pbsi_pid"), ("ppid", "pbsi_ppid"), ("pgid", "pbsi_pgid"), ("euid", "pbsi_uid"), ("ruid", "pbsi_ruid"))}
                prior["traced"] = bool(struct.unpack_from("=I", first_short, short["pbsi_flags"])[0] & 2)
                self.need(all(prior[k] == identity[k] for k in prior), "both original short-info buffers agree on every fingerprint component")
                self.need(all(decoded[k] == ref[k] for k in ("pid", "ppid", "pgid", "euid", "ruid")), "decoded identity equals independent getpid/getppid/getpgrp/geteuid/getuid")
                rss = struct.unpack_from("=Q", bufs[5], task["pti_resident_size"])[0]
                ticks = struct.unpack_from("=Q", bufs[5], task["pti_total_user"])[0] + struct.unpack_from("=Q", bufs[5], task["pti_total_system"])[0]
                self.need([rss, ticks] == e["original_task"] and 0 < rss <= 256 << 20, "independent flavor4 decode equals original task result")
                start = struct.unpack_from("=Q", bufs[6], bsd["pbi_start_tvsec"])[0] + struct.unpack_from("=Q", bufs[6], bsd["pbi_start_tvusec"])[0] / 1e6
                self.need(start == e["original_start_epoch_raw"] and 0 < start <= ref["epoch"] and ref["epoch"] - start <= 330, "independent flavor3 decode equals original start and owner lifetime")
                field = bufs[7][152:1176]
                cut = field.find(b"\0")
                self.need(cut > 0 and field[:cut].decode("utf-8", "surrogateescape") == e["original_cwd"], "independent flavor9 decode equals original cwd")
            for key in ("pid", "ppid", "pgid", "euid", "ruid"):
                self.need(identity[key] == ref[key], "native decoded identity independently agrees " + key)
            self.need(e["original_cwd"] == ref["cwd"] == LANE and ref["pid"] == self.capture["pid"] and
                      struct.unpack_from("=IIII", raws[13])[:3] == (ref["pid"], ref["ppid"], ref["pgid"]) and
                      raws[9][152:1176].split(b"\0")[0].decode() == ref["cwd"] and e["timebase"] > 0 and e["argmax"] > 0,
                      "native layout/cwd behavior independently tied to real owner")
            self.need(e["original_argv"][1:] == ref["argv"] and 0 < e["original_task"][0] <= 256 << 20 and
                      e["original_start_epoch_raw"] > 0, "native argv/task/start evidence, not model ABI response")
            return
        if case in PLATFORM_METHOD:
            scan = self.only("native_readonly_prerequisite_scan")
            exact(scan["distinct_pids"] > 0 and scan["no_spawn_no_credentials_no_trace_no_PID_pressure"] is True and type(scan["matches"]) is list, "actual bounded readonly prerequisite search")
            if not scan["matches"]:
                self.absent("genuine existing platform prerequisite absent; no forced credential/trace/PID reuse")
                return
            if case == "nat_platform_pid_reuse":
                rows = self.events("native_real_PID_reuse")
                keys = ("prior", "current", "prior_mono_observed", "current_mono_begin", "current_mono_observed")
                self.need(same([{k: r[k] for k in keys} for r in rows], scan["matches"]), "every PID-reuse match is exactly one retained native observation")
                for r in rows:
                    self.need(r["prior"]["pid"] == r["current"]["pid"] and r["prior"]["uniqueid"] != r["current"]["uniqueid"] and
                              number(r["prior_mono_observed"]) and number(r["current_mono_begin"]) and r["prior_mono_observed"] < r["current_mono_begin"],
                              "actual PID reuse observed later in time, distinct incarnation not PID-only ownership")
            elif case in ("nat_platform_uid_change_observation", "nat_platform_trace_change_observation"):
                rows = self.events("native_existing_metadata_change")
                keys = ("prior", "current", "prior_mono_observed", "current_mono_begin", "current_mono_observed", "changed_keys")
                changed = ["euid", "ruid"] if case == "nat_platform_uid_change_observation" else ["traced"]
                self.need(same([{k: r[k] for k in keys} for r in rows], scan["matches"]), "every metadata-change match is exactly one retained native observation")
                for r in rows:
                    self.need(r["prior"]["pid"] == r["current"]["pid"] and r["prior"]["uniqueid"] == r["current"]["uniqueid"] and r["changed_keys"] == changed and
                              any(r["prior"][k] != r["current"][k] for k in changed) and number(r["prior_mono_observed"]) and number(r["current_mono_begin"]) and
                              r["prior_mono_observed"] < r["current_mono_begin"] and r["no_credential_or_trace_change"] is True,
                              "genuine temporal change within one native incarnation; a stable mixed state is never a change")
            elif case == "nat_platform_trace_observation":
                rows = [r for r in self.events("native_existing_trace_observation") if r.get("stable_full_fingerprint") is True]
                exact(bool(rows), "required native traced-process observation proof is absent")
                self.need(same([{"before": r["before"], "after": r["after"]} for r in rows], scan["matches"]),
                          "every traced match is exactly one retained stable observation; no vacuous success")
                for r in rows:
                    self.need(r["before"]["traced"] is True and r["after"]["traced"] is True and fingerprint(r["before"]) == fingerprint(r["after"]) and
                              r["no_trace_change"] is True, "stable existing trace metadata from two actual full observations")
            else:
                rows = [e for e in self.events("native_existing_mixed_UID_read") if e["error"] is not None and e["after"] is not None and
                        e["error"]["errno"] in (errno.EPERM, errno.EACCES) and fingerprint(e["before"]) == fingerprint(e["after"])]
                self.need(bool(rows) and same([{"before": e["before"], "after": e["after"], "error": e["error"], "operation_target": e["operation_target"]} for e in rows], scan["matches"]),
                          "every mixed-UID match is exactly one retained native unreadability observation")
                for e in rows:
                    self.need(e["before"]["ruid"] != e["before"]["euid"] and e["no_credential_or_trace_change"] is True, "actual stable mixed UID permission failure")
            return
        s = self.state()
        if case == "nat_platform_fast_exit_zombie":
            if not self.events("native_fast_exit_status_before_initial"):
                self.absent("fast-exit zombie before initial identification not reached")
                return
            if not self.quiet_host():
                return
            e = self.only("native_fast_exit_status_before_initial")
            self.exit(11)
            self.need(e["identity"]["status"] == 5 and s["rec"]["main_initial_identity_observed"]["status"] == 5 and
                      s["go_delivered"] is not True and s["rc"] == 0, "native successful zombie identity acquisition before main install; actual EPIPE/owned failure retained")
            self.strict_failures({"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
            self.clean_full(population=None)
        elif case == "nat_platform_startup_reexec":
            barrier = self.events("native_startup_reexec_barrier")
            if not barrier:
                self.absent("actual postexec barrier not observed before the original pre-GO census")
                return
            if not self.quiet_host():
                return
            self.exit(11)
            bf, braw = regular(self.run + "/scratch/preexec.json")
            af, araw = regular(self.run + "/scratch/postexec.json")
            before, after = decode(braw), decode(araw)
            ident = s["identity"]
            exact(type(ident) is dict, "installed original main identity")
            pre, post = before["identity"], after["identity"]
            self.need(before["pid"] == after["pid"] == pre["pid"] == post["pid"] == s["pid"] and pre["uniqueid"] == post["uniqueid"] == ident["uniqueid"] and
                      fingerprint(pre) == fingerprint(ident) and pre["idversion"] != post["idversion"] and
                      all(pre[k] == post[k] for k in ("pid", "uniqueid", "euid", "ruid", "ppid", "pgid", "traced")),
                      "pre/post exec belong to the installed main incarnation; only the declared idversion transition")
            self.need(same(barrier[0]["artifact"], af) and same(barrier[0]["value"], after), "barrier is the actual postexec artifact")
            sig = s["signal"]
            mains = [t for t in self.events("native_source_TERM") if t["target"]["role"] == "main"]
            self.need(type(sig) is dict and sig["sent"] is False and sig.get("identity_ok") is False and fingerprint(sig["identity_observed"]) == fingerprint(post) and
                      not mains and s["go_delivered"] is not True and s["rc"] == 6, "stale fingerprint refuses TERM on the re-executed main; no GO; honest child6")
            self.strict_failures({"CHILD_IDENTITY_CHANGED", "IDENTITY_UNVERIFIED", "POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
            self.clean_full(population=None)
        else:
            if not self.quiet_host():
                return
            self.exit(0)
            self.strict_failures(set())
            self.clean_full(population=CLEAN)
            owner = self.child["owner"] if self.child else {}
            self.need(owner.get("mask") == [] and owner.get("pid") == owner.get("pgid") == owner.get("sid") == s["pid"], "native child empty inherited mask/fresh process session")
            waits = [e for e in self.events("native_waitpid") if e["pid"] == s["pid"]]
            self.need(len(waits) >= 1 and all(e["options"] == os.WNOHANG for e in waits), "original sole nonblocking native wait ownership")
    def hardlink(self):
        self.exit(0)
        e = self.only("native_hardlink_charge")
        tmp = self.run + "/tmp"
        a, alias, distinct = e["original"], e["alias"], e["distinct"]
        exact(a["path"] == tmp + "/a.bin" and alias["path"] == tmp + "/alias.bin" and distinct["path"] == tmp + "/distinct.bin" and
              e["created_original"]["path"] == tmp + "/a.bin", "fixed hardlink fixture paths")
        actual, total = inventory(tmp)
        files = {p: f for p, f in actual.items() if "sha256" in f}
        self.need(set(files) == {tmp + "/a.bin", tmp + "/alias.bin", tmp + "/distinct.bin"}, "exact tmp artifact set")
        self.need(all(same(files.get(x["path"]), x) for x in (a, alias, distinct)), "event facts equal the independent reopen of the actual files")
        self.need(len({f["sha256"] for f in files.values()}) == 1 and all(f["bytes"] == e["payload_bytes"] for f in files.values()) and
                  e["payload_sha256"] == a["sha256"], "identical bytes established by actual digest and size")
        self.need(a["inode"] == alias["inode"] != distinct["inode"] and a["nlink"] == alias["nlink"] == 2 and distinct["nlink"] == 1,
                  "actual aliases same dev/inode; identical bytes on a different inode")
        self.need(e["created_original"]["inode"] == a["inode"] and e["created_original"]["sha256"] == a["sha256"] and
                  e["created_original"]["nlink"] == 1, "hardlink original exclusive-created descriptor survives alias creation")
        self.need(total == e["source_walk_total"] == 2 * e["payload_bytes"] and sum(f["bytes"] for f in files.values()) == e["raw_path_sum"] == 3 * e["payload_bytes"],
                  "original native walk charges same-inode aliases once and byte-identical distinct inode separately; method only")
    def sample_records(self, raw):
        text = raw.decode("utf-8")
        decoder = json.JSONDecoder(object_pairs_hook=pairs, parse_float=finite, parse_constant=nonfinite)
        pos, rows = 0, []
        while pos < len(text):
            obj, end = decoder.raw_decode(text, pos)
            exact(type(obj) is dict and set(obj) == SAMPLE_KEYS and number(obj["mono"]) and number(obj["epoch"]) and
                  (obj["rc"] is None or integer(obj["rc"])) and type(obj["census"]) is dict and type(obj["resources"]) is dict and
                  integer(obj["accounting_ref"]) and type(obj["streams"]) is dict and (obj["stop"] is None or type(obj["stop"]) is str) and
                  type(obj["failure_codes"]) is list and type(obj["trips"]) is list and
                  all(type(x) is str for x in obj["failure_codes"] + obj["trips"]) and set(obj["resources"]) == {"charged_bytes", "lane_bytes", "free"} and
                  all(integer(v) and v >= 0 for v in obj["resources"].values()), "typed native sample record")
            exact(text[pos:end + 1] == json.dumps(obj, sort_keys=True, indent=1, allow_nan=False) + "\n", "exact source sample framing")
            rows.append(obj)
            pos = end + 1
        return rows
    def integration(self):
        if self.case == "nat_integration_printed_ack_actual14":
            self.signals()
            return
        if not self.quiet_host():
            return
        s = self.state()
        src = self.frozen["source"]
        self.exit(src["driver_exit"])
        self.strict_failures(set())
        self.clean_full(population=CLEAN)
        self.need(s["rc"] == src["child_rc"] and self.summary["acknowledged"] is True and self.summary["exit_code"] == 0 and
                  self.summary["child_returncode"] == s["rc"], "SETTLED transport never scientific acceptance, including native child7")
        facts, raw = regular(self.cfg["samples"], 1 << 20)
        rows = self.sample_records(raw)
        recon = s["reconciliation"]
        accounting = {a["id"]: a for a in recon["accounting_observations"]}
        censuses = {c["mono_start"]: c for c in recon["census_observations"]}
        self.need(len(rows) == s["rec"]["samples_written"] >= 1 and facts["bytes"] == s["rec"]["samples_bytes"] and
                  facts["sha256"] == s["rec"]["evidence_expected_sha256"][self.cfg["samples"]], "normal/immediate-GO exits retain actual nonempty hashed complete samples")
        self.need(all(r["accounting_ref"] in accounting and same(r["resources"], accounting[r["accounting_ref"]]["resources"]) and
                      r["census"].get("mono_start") in censuses and same(r["census"], censuses[r["census"]["mono_start"]]) for r in rows) and
                  all(a["mono"] <= b["mono"] for a, b in zip(rows, rows[1:])), "every sample joins retained source census/accounting evidence in time order")
        protocol = self.child["protocol"] if self.child else None
        self.need(type(protocol) is dict and protocol["bytes"] == 3 and protocol["raw_hex"] == b"GO\n".hex() and protocol["eof"] is True, "ordinary exact GO+EOF still actual")
    def derived(self):
        self.exit(0)
        out = self.outcome["source_outcome"]
        exact(type(out) is dict and out.get("mode") == "FIXED_ORACLE_NEGATIVE_FRESH_COPY" and out.get("negative_scope") == "ORACLE_INPUT_NOT_NATIVE_SOURCE_OUTCOME",
              "derived scope not native evidence")
        base = self.request["derived_base"]
        exact(base == out["base"] and base["case"] == "nat_integration_normal_exit", "fixed base join")
        source = Oracle(base["case"], base["approval_sha256"], base["capture_sha256"])
        if source.verify()["status"] != "FIXTURE_PREDICATES_MET":
            self.absent("independent actual base native normal-exit evidence not met")
            return
        broot, objects, rejected = source.run, out["objects"], None
        if self.case == "nat_integration_incomplete_capture":
            original, raw = regular(objects["original"]["path"], 4 << 20)
            copied, bad = regular(objects["copy"]["path"], 4 << 20)
            bcap = source.capture["stdout"]
            self.need(objects["original"]["path"] == broot + "/driver.stdout" and same(objects["original_capture"], bcap) and same(original, objects["original"]) and
                      original["sha256"] == bcap["sha256"] and original["bytes"] == bcap["bytes"] and original["inode"] == bcap["inode"],
                      "original is exactly the independently verified base captured stdout stream")
            self.need(objects["copy"]["path"] == self.run + "/scratch/incomplete.stdout" and same(copied, objects["copy"]) and copied["inode"] != original["inode"] and
                      bad == raw[:-1] and not bad.endswith(b"\n"), "fresh copy is exactly the base stream minus its final byte")
            if sha(bad) != bcap["sha256"] or len(bad) != bcap["bytes"] or not bad.endswith(b"\n"):
                rejected = "CAPTURE_BYTES_OR_COMPLETENESS"
        elif self.case == "nat_integration_digest_inode_mismatch":
            original, raw = regular(objects["original"]["path"], 4 << 20)
            copied, other = regular(objects["copy"]["path"], 4 << 20)
            bart = source.artifacts.get(broot + "/out/receipt.json")
            self.need(objects["original"]["path"] == broot + "/out/receipt.json" and type(bart) is dict and same(original, bart) and same(original, objects["original"]) and
                      source.summary.get("receipt_sha256") == original["sha256"], "original is the independently verified base receipt artifact")
            self.need(objects["copy"]["path"] == self.run + "/scratch/same-content-receipt.json" and same(copied, objects["copy"]) and raw == other and
                      copied["inode"] != original["inode"] and objects["expected_original_inode"] == original["inode"], "fresh equal-digest copy on a different native inode")
            if type(bart) is dict and copied["inode"] != bart["inode"]:
                rejected = "ORIGINAL_ARTIFACT_INODE"
        elif self.case == "nat_integration_unresolved_identity":
            original, oraw = regular(objects["original"]["path"], 8 << 20)
            copied, raw = regular(objects["copy"]["path"], 8 << 20)
            prior, obj = decode(oraw), decode(raw)
            self.need(objects["original"]["path"] == broot + "/fixture-outcome.json" and original["sha256"] == source.capture["outcome_sha256"] and
                      same(original, objects["original"]) and same(copied, objects["copy"]) and objects["replaced_keys"] == ["unresolved"],
                      "original is the independently verified base outcome")
            stripped = {k: v for k, v in obj.items() if k != "unresolved"}
            self.need(same(stripped, {k: v for k, v in prior.items() if k != "unresolved"}) and prior["unresolved"] == [] and
                      obj["unresolved"] == [{"kind": "ORACLE_NEGATIVE_ACTUAL_LIVE_OWNER", "identity": objects["actual_identity"]}] and
                      objects["actual_identity"]["pid"] == self.capture["pid"] and objects["actual_identity"]["pgid"] == self.capture["pgid"],
                      "fresh copy differs from the verified base outcome only by the inserted actual live owner")
            if obj["unresolved"]:
                rejected = "UNRESOLVED_IDENTITY"
        else:
            facts, raw = regular(objects["late_artifact"]["path"])
            pfd = directory(self.run + "/scratch")
            try:
                names = sorted(os.listdir(pfd))
                scratch = inode(pfd)
            finally:
                os.close(pfd)
            self.need(objects["late_artifact"]["path"] == self.run + "/scratch/late.bin" and same(facts, objects["late_artifact"]) and
                      raw == b"fixed late artifact after empty captured inventory\n" and objects["before_names"] == [] and
                      objects["scratch_directory_inode"] == scratch == self.request["anchors"]["scratch"]["inode"] and number(objects["before_mono"]) and
                      objects["before_mono"] > self.only("authority_checked")["mono"], "fresh late artifact relative to the anchor-verified empty scratch inventory captured after authority")
            if names != objects["before_names"]:
                rejected = "LATE_ARTIFACT_INVENTORY"
        self.need(rejected == {DERIVED[0]: "CAPTURE_BYTES_OR_COMPLETENESS", DERIVED[1]: "ORIGINAL_ARTIFACT_INODE",
                               DERIVED[2]: "UNRESOLVED_IDENTITY", DERIVED[3]: "LATE_ARTIFACT_INVENTORY"}[self.case], "independently recomputed strict rejection, never flag-only acceptance")
    def post_publication(self):
        if not self.events("post_publication_API_entry"):
            self.absent("clean post-publication request_stop entry not reached")
            return
        if not self.quiet_host():
            return
        self.exit(0)
        self.strict_failures(set())
        before = self.only("post_publication_API_entry")
        after = self.only("post_publication_native_helper_activity")
        s = self.state()
        self.need(before["scope"] == "API_ENTRY_STIMULUS" and before["trips_before"] == {} and before["failures_before"] == [] and before["stop_before"] is None and
                  after["scope"] == "NATIVE_HELPER_ACTIVITY" and after["no_resource_excess_claim"] is True and s["stop"]["reason"] == "FIXED_POST_PUBLICATION_API_ENTRY" and
                  s["signal"]["why_not"] == "CHILD_ALREADY_REAPED", "one clean explicit postpublication original request_stop entry, no invented trip/excess")
        receipt = decode(regular(self.cfg["receipt"], 4 << 20)[1])
        current = s["reconciliation"]["helpers"]
        self.need(same(receipt["helpers"], before["helper_prefix"]) and same(current[:-1], receipt["helpers"]) and len(current) == len(receipt["helpers"]) + 1 and
                  current[-1]["date"] == s["stop"]["date"] and current[-1]["mono_spawn"] > self.summary["post_publish_mono"],
                  "historical receipt prefix vs new actual owned /bin/date helper after publication")
        self.helper_proof(current[-1], True)
        self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0 and same(self.summary["ack_resources"], before["accounting"]) and
                  same(self.summary["reconciliation"]["helpers"], current), "dominant source19 ACK0/current helper/accounting join without backediting historical receipt")
        self.clean_full(population=[["admission", "OK"], ["start", "OK"], ["end", "OK"], ["stop", "OK"]])
    def verify(self):
        self.auth()
        self.common()
        case = self.case
        if self.missing:
            # Driver-retained missing prerequisite: dependent case predicates are not evaluated (prerequisite-first);
            # prerequisite-independent integrity failures from common() are preserved.
            pass
        elif case in RUNTIME:
            self.runtime()
        elif case in GO:
            self.go_case()
        elif case in ACK:
            self.ack_case()
        elif case in ACK_AGE:
            self.ack_age()
        elif case in SIGNALS:
            self.signals()
        elif case in PROTECTED:
            self.protected()
        elif case in HELPER_FULL:
            self.helper_full()
        elif case in HELPER_METHOD:
            self.helper_method()
        elif case in CAPS:
            self.caps()
        elif case in PLATFORM_METHOD + PLATFORM_FULL:
            self.platform()
        elif case == "nat_hardlink_distinct_inode":
            self.hardlink()
        elif case in INTEGRATION:
            self.integration()
        elif case in DERIVED:
            self.derived()
        elif case == "nat_post_publication_stop_helper":
            self.post_publication()
        else:
            raise Hold("no fixed dispatch")
        status = "NOT_MET" if self.failures else "NOT_EXERCISED" if self.missing else "FIXTURE_PREDICATES_MET"
        return {"kind": "rqls10-guard-matrix-oracle-v1", "case": case, "status": status, "scope": self.request["scope"],
                "approval_sha256": self.approval_sha, "parent_capture_sha256": self.capture_sha, "actual_exit_from_parent": self.capture["actual_exit"],
                "failures": self.failures, "missing_prerequisites_or_boundaries": self.missing,
                "native_equality_claim": False, "native_history_count_cap_claim": False, "empirical_matrix_closed": False,
                "science_acceptance": False, "reservation_release": False, "authority": "FIXTURE_ONLY_NO_GO_NO_RELEASE_NO_SCIENCE"}


if __name__ == "__main__":
    try:
        exact(len(sys.argv) == 4, "CASE APPROVAL_SHA CAPTURE_SHA required")
        result = Oracle(*sys.argv[1:]).verify()
    except BaseException as exc:
        result = {"kind": "rqls10-guard-matrix-oracle-v1", "case": sys.argv[1] if len(sys.argv) > 1 else None, "status": "HOLD",
                  "error_type": type(exc).__name__, "error_UTF8_HEX": str(exc).encode("utf-8", "surrogateescape").hex(),
                  "error_scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "empirical_matrix_closed": False,
                  "science_acceptance": False, "reservation_release": False, "authority": "NO_GO_NO_RELEASE_NO_SCIENCE"}
    raw = packed(result)
    if len(raw) > 1 << 20:
        sys.exit(2)
    sys.stdout.buffer.write(raw)
    sys.stdout.buffer.flush()
    sys.exit(0 if result["status"] == "FIXTURE_PREDICATES_MET" else 2)
