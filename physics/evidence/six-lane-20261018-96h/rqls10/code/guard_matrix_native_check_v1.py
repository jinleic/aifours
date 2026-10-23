#!/usr/bin/env python3
"""REVIEW CANDIDATE / WRITTEN ONLY. Separate source19 native-fixture oracle.

CHECK CASE APPROVAL_SHA PARENT_CAPTURE_SHA. Reads actual pinned files/captures;
imports no driver, child or supervisor, accepts no pass flag, never grants GO,
science, empirical closure or release. Equality/model counts are not native
coverage. Negative verifier copies are fresh, explicitly oracle-input only.
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
PATHS = {"supervisor": LANE + "/code/owned_supervisor_v19.py", "driver": LANE + "/code/guard_matrix_native_v1.py",
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


def decode(raw):
    def finite(text):
        value = float(text)
        exact(math.isfinite(value), "nonfinite JSON")
        return value
    return json.loads(raw.decode(), object_pairs_hook=pairs, parse_float=finite,
                      parse_constant=lambda x: (_ for _ in ()).throw(Hold("nonfinite JSON")))


def number(x):
    return type(x) in (int, float) and math.isfinite(x)


def integer(x):
    return type(x) is int


def hex64(x):
    return type(x) is str and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def error_text(obj):
    exact(type(obj) is dict and set(obj) == {"type", "errno", "UTF8_HEX", "utf8_bytes", "text_scope"}, "complete raw error schema")
    raw = bytes.fromhex(obj["UTF8_HEX"])
    exact(obj["text_scope"] == "MODEL_INPUT_NOT_ACTUAL_BIN_DATE" and len(raw) == obj["utf8_bytes"], "raw error not truncated/date scoped")
    return raw.decode("utf-8", "surrogateescape")


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
    def auth(self):
        case, run = self.case, self.run
        exact(case in CASES and hex64(self.approval_sha) and hex64(self.capture_sha), "fixed oracle arguments")
        af, ar = regular(run + "/parent-authorization.json", 1 << 20)
        rf, rr = regular(run + "/request.json", 1 << 20)
        exact(af["sha256"] == self.approval_sha, "external approval SHA")
        ap, rq = decode(ar), decode(rr)
        keys = {"kind", "case", "scope", "sources", "anchors", "allocation", "not_after_epoch", "negative_control", "ownership_negative",
                "hook_set", "config", "go", "stability", "python", "created_facts", "case_spec_sha256", "derived_base", "limits"}
        exact(set(rq) == keys and set(ap) == keys | {"request_sha256"} and ap["request_sha256"] == rf["sha256"] and
              ap["kind"] == "rqls10-guard-matrix-invocation-v1" and rq["kind"] == "rqls10-guard-matrix-request-v1" and
              all(same(ap[k], rq[k]) for k in keys - {"kind"}), "exact authority/request schema and typed join")
        exact(rq["case"] == case and rq["scope"] == "MODIFIED_QUALIFICATION_FIXTURE" and rq["hook_set"] == [case] and
              rq["negative_control"] is (case not in POSITIVE) and rq["ownership_negative"] is (case in OWNERSHIP), "case scope negative hooks")
        exact(same(rq["limits"], LIMITS), "fixed declared resource envelope")
        alloc = rq["allocation"]
        exact(set(alloc) == {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} and
              all(integer(v) and v >= 0 for v in alloc.values()) and alloc["bytes"] == 20 << 20 and alloc["cpu_slots"] == (2 if case in OWNERSHIP else 1), "serialized allocation")
        exact(set(rq["sources"]) == set(PATHS), "fixed source set")
        for role, path in PATHS.items():
            pin = rq["sources"][role]
            exact(type(pin) is dict and set(pin) == {"path", "sha256"} and pin["path"] == path and hex64(pin["sha256"]), "source pin schema")
            exact(regular(path, 2 << 20)[0]["sha256"] == pin["sha256"], "actual exact source: " + role)
        exact(rq["sources"]["supervisor"]["sha256"] == SUP_SHA, "immutable source19")
        specs = decode(regular(PATHS["case_specs"], 2 << 20)[1])
        exact(specs["kind"] == "rqls10-matrix-native-v1-cases" and set(specs["cases"]) == set(CASES) and
              specs["supervisor"] == {"path": PATHS["supervisor"], "sha256": SUP_SHA}, "complete exact finite catalog")
        exact(sha(packed(specs["cases"][case])) == rq["case_spec_sha256"], "exact case definition binding")
        self.spec = specs["cases"][case]
        exact(set(rq["anchors"]) == {"run", "out", "tmp", "scratch"}, "anchor schema")
        for key, suffix in (("run", ""), ("out", "/out"), ("tmp", "/tmp"), ("scratch", "/scratch")):
            fd = directory(run + suffix)
            try:
                exact(same(rq["anchors"][key], {"path": run + suffix, "inode": inode(fd)}), "original/current anchor " + key)
            finally:
                os.close(fd)
        exact(set(rq["created_facts"]) == {"config", "go", "stability"}, "created-descriptor schema")
        for key, name in (("config", "config.json"), ("go", "GO.json"), ("stability", "stability.json")):
            facts, _ = regular(run + "/" + name, 1 << 20)
            exact(same(rq[key], {"path": facts["path"], "sha256": facts["sha256"]}) and same(rq["created_facts"][key], facts) and
                  facts["nlink"] == 1, "actual original parent-created input " + key)
        py = rq["python"]
        exact(set(py) == {"path", "sha256"} and os.path.realpath(py["path"]) == py["path"] and
              regular(py["path"], 64 << 20)[0]["sha256"] == py["sha256"], "actual interpreter bytes")
        cfg = decode(regular(run + "/config.json", 1 << 20)[1])
        go = decode(regular(run + "/GO.json", 1 << 20)[1])
        wall = 200.0 if case in GO and "w200" in case else 10.0
        exact(same(cfg["max_wall_s"], wall) and same(cfg["sample_s"], 0.2) and same(cfg["settle_s"], 20.0) and
              cfg["argv"] == [py["path"], "-I", "-B", PATHS["child"], "main", case] and cfg["lane"] == LANE and
              cfg["purpose"] == "guard-qualification" and cfg["item"] == case and cfg["creation_channel"] == {} and cfg["fault_injection"] == {}, "fixed native config design")
        exact(cfg["lane_disk_root"] == run and cfg["lane_roots"] == [LANE] and cfg["output_roots"] == [run + "/out"] and
              cfg["env"] == {"PATH": "/usr/bin:/bin", "TMPDIR": run + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"} and cfg["pins"] == [], "fixed isolation/readonly lane")
        exact(cfg["cpu_slots"] == alloc["cpu_slots"] and cfg["busy_limit"] == 2 and cfg["rss_trip_bytes"] == ((128 << 20) if case == "nat_cap_final_rss" else 256 << 20), "fixed resource thresholds")
        bound = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
        bound.update({k: cfg["admission"][k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
        expected_go = {"decision": "GO", "item": case, "configs": {rq["config"]["sha256"]: bound},
                       "not_after_epoch": go.get("not_after_epoch"), "stability_receipt_sha256": rq["stability"]["sha256"]}
        if rq["negative_control"]:
            expected_go["qualification_negative"] = {"scenario": case, "kind": "matrix_native", "creation_channel": False}
        exact(same(go, expected_go) and number(go["not_after_epoch"]) and number(rq["not_after_epoch"]) and go["not_after_epoch"] <= rq["not_after_epoch"], "fixed GO exact typed binding")
        for key, name in (("stdout", "child.stdout"), ("stderr", "child.stderr"), ("samples", "samples.jsonl"),
                          ("launch_record", "launch.json"), ("receipt", "receipt.json"), ("settlement_record", "settlement.json")):
            exact(cfg[key] == run + "/out/" + name, "fixed output names")
        cf, cr = regular(run + "/parent-capture.json", 1 << 20)
        exact(cf["sha256"] == self.capture_sha, "external capture SHA")
        cap = decode(cr)
        ck = {"kind", "case", "approval_sha256", "driver_source_sha256", "pid", "pgid", "mono_begin", "mono_end", "actual_exit", "stdout", "stderr", "outcome_sha256", "wait_status"}
        exact(set(cap) == ck and cap["kind"] == "rqls10-guard-matrix-parent-capture-v1" and cap["case"] == case and
              cap["approval_sha256"] == self.approval_sha and cap["driver_source_sha256"] == rq["sources"]["driver"]["sha256"], "parent actual capture binding")
        exact(integer(cap["pid"]) and integer(cap["pgid"]) and min(cap["pid"], cap["pgid"]) > 1 and
              number(cap["mono_begin"]) and number(cap["mono_end"]) and 0 <= cap["mono_end"] - cap["mono_begin"] <= 300, "native parent owner/time")
        ws = cap["wait_status"]
        exact(set(ws) == {"native_wait_status", "waitpid_pid", "reaped"} and ws["reaped"] is True and ws["waitpid_pid"] == cap["pid"] and
              integer(ws["native_wait_status"]) and (os.WIFEXITED(ws["native_wait_status"]) or os.WIFSIGNALED(ws["native_wait_status"])) and
              os.waitstatus_to_exitcode(ws["native_wait_status"]) == cap["actual_exit"], "parent native destructive status, not selected return")
        self.streams = {}
        for name in ("stdout", "stderr"):
            rec = cap[name]
            exact(set(rec) == {"path", "sha256", "bytes", "inode", "eof"} and rec["path"] == run + "/driver." + name and rec["eof"] is True, "complete original-inode parent streams required")
            facts, raw = regular(rec["path"], 4 << 20)
            exact(facts["sha256"] == rec["sha256"] and facts["bytes"] == rec["bytes"] and facts["inode"] == rec["inode"], "actual parent stream bytes and original created inode")
            self.streams[name] = raw
        of, raw = regular(run + "/fixture-outcome.json", 8 << 20)
        exact(of["sha256"] == cap["outcome_sha256"], "actual outcome digest joined")
        self.request, self.capture, self.cfg, self.go, self.outcome = rq, cap, cfg, go, decode(raw)
    def common(self):
        rq, cap, out = self.request, self.capture, self.outcome
        exact(out.get("kind") == "rqls10-guard-matrix-outcome-v1" and out.get("case") == self.case and out.get("scope") == rq["scope"], "outcome kind/case/scope")
        expected = {"approval_sha256": self.approval_sha, "request_sha256": regular(self.run + "/request.json")[0]["sha256"],
                    **{k: rq[k] for k in ("sources", "anchors", "allocation", "config", "go", "stability", "python", "created_facts", "hook_set", "negative_control", "ownership_negative", "case_spec_sha256", "derived_base")}}
        exact(same(out["bindings"], expected), "outcome exact authority binding")
        owner = out["owner"]
        exact(set(owner) == {"pid", "pgid", "mono_begin", "mono_end"} and owner["pid"] == cap["pid"] and owner["pgid"] == cap["pgid"] and
              cap["mono_begin"] <= owner["mono_begin"] <= owner["mono_end"] <= cap["mono_end"], "owner/capture chronology")
        exact(out["no_empirical_closure"] is True and out["science_acceptance"] is False and same(out["limits"], LIMITS) and
              number(out["observed_maxrss_bytes"]) and out["observed_maxrss_bytes"] <= 256 << 20, "honest scope/resource envelope")
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
            exact(type(row) is dict and row.get("seq") == index and number(row.get("mono")) and last <= row["mono"] <= owner["mono_end"] and
                  type(row.get("operation")) is str and type(row.get("scope")) is str, "raw event sequence/scope/time")
            last = row["mono"]
            if "mono_before" in row:
                exact(number(row["mono_before"]) and number(row.get("mono_after")) and row["mono_before"] <= row["mono_after"] <= row["mono"], "native call interval")
            if row.get("error") is not None:
                error_text(row["error"])
        checked, loaded = self.only("authority_checked"), self.only("source_loaded")
        exact(checked["approval_sha256"] == self.approval_sha and checked["sources"] == rq["sources"] and checked["anchors"] == rq["anchors"] and
              loaded["supervisor_sha256"] == SUP_SHA and loaded["wrapper_sha256"] == rq["sources"]["driver"]["sha256"] and
              loaded["hook_set"] == [self.case] and loaded["seq"] > checked["seq"], "actual authorized source/hook load")
        exact(out["terminal"] == {"source_sha256": SUP_SHA, "ast_lines": [2688, 2692], "unchanged": full}, "source19 terminal framing")
        if full:
            exact(self.summary["supervisor"] == "owned_supervisor_v19" and self.summary["config_sha256"] == rq["config"]["sha256"], "actual source summary identity")
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
        expected_unresolved = self.case in ("nat_helper_unverified_identity", "nat_helper_lost_wait", "nat_helper_live_group", "nat_helper_live_descendant_unproved", "nat_helper_grace_exhaustion")
        for row in out["unresolved"]:
            if row.get("kind") == "raw_event_trace_dropped":
                raise Hold("raw event trace incomplete")
            if expected_unresolved and row.get("kind") == "source_owned_process":
                continue  # Expected continued blocking, NOT endedness or release.
            self.need(False, "unresolved ownership/FD/thread/raw fixture evidence: " + row.get("kind", "unknown"))
        for row in self.events("native_spawn_registered"):
            self.need(row["source_ledger_registered"] is True and integer(row["pid"]) and row["pid"] > 1 and row["pgid"] == row["pid"] and
                      row["setsid"] is True and row["setsigmask"] == [], "real registered native PID/fresh group/empty mask")
            if row["role"] == "helper" and not self.events("declared_native_method_helper"):
                self.need(row["argv"] == ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], "sole actual production clock helper is /bin/date")
        for p in out["fixture_processes"]:
            self.need(p.get("reaped") is True and p.get("native_wait_result", [None])[0] == p.get("pid") and p.get("stdin_fd") is None and p.get("stdout_fd") is None,
                      "driver-owned probe settled by its original sole native wait")
            raw = bytes.fromhex(p["owner_raw_hex"])
            exact(raw.endswith(b"\n") and raw.count(b"\n") == 1, "probe owner complete capture")
            frame = decode(raw)
            self.need(frame["pid"] == p["pid"] and frame["pgid"] == p["identity"]["pgid"], "probe actual owner record")
        if full:
            s = self.state()
            for path, original in s["created"].items():
                if path in self.artifacts:
                    self.need(self.artifacts[path].get("inode") == original, "original source-created artifact inode continuity")
            for pub in self.events("native_original_publication"):
                actual = self.artifacts[pub["path"]]
                self.need(all(actual[k] == pub[k] for k in ("inode", "sha256", "bytes")), "original native publication return matches current artifact")
            if self.summary.get("receipt_sha256") is not None:
                self.need(self.artifacts[self.cfg["receipt"]]["sha256"] == self.summary["receipt_sha256"], "actual original receipt digest joined")
            if self.summary.get("settlement_record_sha256") is not None:
                final = self.artifacts[self.cfg["settlement_record"]]
                staged = self.artifacts[self.cfg["settlement_record"] + ".staged"]
                self.need(final["sha256"] == self.summary["settlement_record_sha256"] and final["inode"] == staged["inode"] and
                          final["nlink"] == staged["nlink"] == 2, "actual sole staged-pair inode/digest publication")
    def exit(self, code):
        self.need(self.capture["actual_exit"] == code, "exact parent actual exit=%d" % code)
    def source_errors(self):
        return [error_text(e["error"]) for e in self.events("original_completion_exception")]
    def strict_failures(self, expected, trips=()):
        s = self.state()
        expected = set(expected)
        # Only an actually absent required report after early owned stop permits
        # this one causally derived extra. No unrelated outcome set broadening.
        if s["pid"] is not None and not os.path.lexists(self.cfg["outputs"][0]["path"]):
            expected.add("REQUIRED_OUTPUT_MISSING")
        self.need(set(s["failure_codes"]) == expected and set(s["trips"]) == set(trips), "exact causally derived source failures/trips")
    def helper_proof(self, h, valid_clock=False):
        self.need(h["identity"] is not None and h["identity"]["pid"] == h["pid"] == h["identity"]["pgid"] and h["initial_identity_valid"] is True,
                  "helper acquired original full native identity")
        if (h.get("signal") or {}).get("sent"):
            sig = h["signal"]
            self.need(sig["identity_ok"] is True and fingerprint(sig["identity_observed"]) == fingerprint(h["identity"]) and
                      sig["mono_check"] <= sig["mono_identity_begin"] <= sig["mono_identity_observed"] <= sig["mono_sent"], "helper actual TERM fingerprint/check/send chronology")
            native = [e for e in self.events("native_source_TERM") if e["pgid"] == h["identity"]["pgid"] and "error" not in e]
            self.need(len(native) == 1, "at most one original helper verified TERM success")
        if h["leader_reaped"]:
            raw = h["native_wait_result"]
            self.need(raw[0] == h["pid"] and raw[1] == h["raw_wait_status"] and os.waitstatus_to_exitcode(raw[1]) == h["rc"], "helper real destructive status retained")
        if h["settled"]:
            self.need(h["wait_lost"] is False and h["leader_reaped"] is True and h["group_clear"] is True and h["descendants_clear"] is True and
                      h["coverage_complete"] is True and h["stdout_closed"] is True and h["eof_proved"] is True and
                      h["proof"]["complete"] is True and h["proof"]["owned_live"] == [] and h["proof"]["unproved_live"] == [], "helper settlement conjunction not reap-only")
        if valid_clock:
            self.need(h["settled"] is True and h["rc"] == 0 and type(h["date"]) is str and
                      bytes.fromhex(h["capture_hex"]) == (h["date"] + "\n").encode("ascii") and
                      h["mono_proof_complete"] <= h["mono_call_deadline"] and h["mono_reaped"] <= h["mono_call_deadline"], "only timely owned /bin/date bytes constitute actual metadata")
    def clean_full(self, child=True):
        s = self.state()
        final = s["rec"].get("final_census")
        if final is None:
            self.absent("original full main did not reach final census; actual prerequisite/outcome retained")
            return
        foreign = [p for p in final["unproved_live"] if p["uniqueid"] not in {p["identity"]["uniqueid"] for p in self.outcome["fixture_processes"] if p.get("identity")}]
        if foreign:
            self.absent("native unrelated post-baseline identities prevent quiet-host coverage prerequisite")
        self.need(final["complete"] is True and final["incomplete_n"] == 0 and final["owned_live"] == [] and final["group_live"] == [] and final["unproved_live"] == [], "complete native final closure")
        for h in s["reconciliation"]["helpers"]:
            if h["date"] is not None:
                self.helper_proof(h, True)
        if child and s["pid"] is not None:
            path = self.cfg["outputs"][0]["path"]
            exact(os.path.lexists(path), "actual child report prerequisite")
            facts, raw = regular(path, 256 << 10)
            report = decode(raw)
            self.need(report["kind"] == "rqls10-native-child-outcome-v1" and report["case"] == self.case and
                      report["approval_sha256"] == self.approval_sha and report["owner"]["pid"] == s["pid"] and report["owner"]["pgid"] == s["group"] and
                      report["science_acceptance"] is False and report["observed_maxrss_bytes"] <= 256 << 20, "native fixed child/report/source identity join")
            self.child = report
            cstdout = regular(self.cfg["stdout"], 128 << 10)[1].splitlines(keepends=True)
            exact(cstdout and all(x.endswith(b"\n") for x in cstdout), "complete child stdout capture")
            owner = decode(cstdout[0])
            self.need(owner["pid"] == s["pid"] and owner["pgid"] == s["group"], "actual first child owner frame")
            record = decode(cstdout[-1])
            self.need(record.get("kind") == "rqls10-native-child-record-v1" and record.get("report_sha256") == facts["sha256"] and
                      same(record.get("artifact"), facts), "child actual created-descriptor artifact inode/hash joined through captured stdout")
            mw = s["reconciliation"]["main_wait"]
            self.need(mw["leader_reaped"] is True and mw["native_wait_result"][0] == s["pid"] and
                      os.waitstatus_to_exitcode(mw["raw_wait_status"]) == s["rc"] == mw["rc"], "actual source WNOHANG child status")
    def runtime(self):
        s = self.state()
        rows = [e for e in self.events("native_waitpid") if e["pid"] == s["pid"] and e.get("native_result", [0])[0]]
        exact(len(rows) == 1, "one successful original native main wait")
        e, mark = rows[0], self.only("native_successful_wait_target")
        spawn = s["rec"]["mono_spawn"]
        target = {RUNTIME[0]: 9.99, RUNTIME[1]: 10.0, RUNTIME[2]: 10.26}[self.case]
        measured = e["mono_after"] - spawn
        upper = 10.0 if self.case == RUNTIME[0] else 10.01 if self.case == RUNTIME[1] else 10.27
        if not target <= e["mono_before"] - spawn <= measured < upper:
            self.absent("native successful-wait target window missed; no exact-equality substitution")
            return
        self.need(mark["status_observed"]["status"] == 5 and mark["hook_begin"] < spawn + 10.0 and mark["target_mono"] == spawn + target,
                  "genuine zombie and pre-cutoff original call entry before native return")
        self.need(e["native_result"][0] == s["pid"] and s["rc"] == 0, "late native wait actually successful, no API zero-return fixture")
        if self.case == RUNTIME[0]:
            self.exit(0)
            self.strict_failures(set())
            self.need(s["rec"]["runtime_observations"] == [], "before deadline no trip")
        else:
            late = self.case == RUNTIME[2]
            self.exit(11 if late else 0)
            self.strict_failures({"MAIN_DEADLINE_ENFORCEMENT_LATE"} if late else set(), {"DEADLINE"})
            obs = s["rec"]["runtime_observations"]
            self.need(len(obs) == 1 and obs[0]["where"] == "after_waitpid_including_success" and
                      obs[0]["mono"] >= e["mono_after"] and (obs[0]["mono"] > spawn + 10.25) is late,
                      "original post-success runtime enforcement/late boundary")
        self.clean_full()
    def go_case(self):
        s, c = self.state(), self.state()["rec"].get("go_delivery_completion")
        if c is None:
            self.absent("valid prewrite gate and actual GO completion not reached")
            return
        bound = min(60.0, self.cfg["max_wall_s"] / 2)
        delta = {"lt": -0.01, "eq": 0.0, "gt": 0.01}[self.case.rsplit("_", 1)[1]]
        target = bound + delta
        if not target <= c["spawn_age_s"] < target + 0.01:
            self.absent("actual GO target-relative completion window missed")
            return
        commit = s["rec"]["go_commit"]
        census = s["rec"]["pre_go_census"]
        delay = self.only("GO_native_delivery_delay")
        write = self.only("native_GO_write")
        self.need(s["go_delivered"] is True and c["spawn_age_bound_s"] == bound and
                  c["spawn_age_s"] == c["mono"] - s["rec"]["mono_spawn"] and
                  c["remaining_main_runtime_s"] == s["rec"]["mono_spawn"] + self.cfg["max_wall_s"] - c["mono"] > 0,
                  "actual original GO completion age/remaining runtime")
        self.need(census["complete"] is True and census["unproved_live"] == [] and len(census["owned_live"]) == 1 and
                  fingerprint(census["owned_live"][0]) == fingerprint(s["identity"]) and
                  commit["mono"] < delay["injection_end"] <= write["mono_before"] <= write["mono_after"] <= c["mono"] and
                  c["mono"] - census["mono_complete"] <= 1.0 and commit["mono"] - s["rec"]["mono_spawn"] <= bound,
                  "valid fresh original prewrite gates then actual delayed native write/close/completion")
        late = c["spawn_age_s"] > bound
        self.exit(11 if late else 0)
        self.strict_failures({"GO_COMPLETION_AGE_EXCEEDED", "POST_SPAWN_FAILURE"} if late else set())
        if late:
            self.need("LATE_ACTUAL_GO_DELIVERY_OWNED_STOP" in self.source_errors() and s["signal"]["sent"] is True and
                      fingerprint(s["signal"]["identity_observed"]) == fingerprint(s["identity"]), "original late-GO owned stop and identity-checked TERM")
        self.clean_full()
    def ack_case(self):
        s, case = self.state(), self.case
        if not self.events("native_ACK_census_return"):
            self.absent("actual post-publication ACK census not reached")
            return
        e = self.only("native_ACK_census_return")
        ack, final = e["census"], s["rec"]["final_census"]
        finalids = {p["uniqueid"] for p in final["owned_live"] + final["unproved_live"]}
        ackids = {p["uniqueid"] for p in ack["owned_live"] + ack["unproved_live"]}
        if case == "nat_ack_clean":
            self.exit(0)
            self.strict_failures(set())
            self.need(finalids == ackids == set() and ack["complete"] is True and self.summary["acknowledged"] is True, "unchanged clean ACK coverage")
            self.clean_full()
        elif case == "nat_ack_new_unproved":
            self.exit(14)
            self.strict_failures(set())
            self.need(not finalids and len(ackids) == 1 and ack["complete"] is True and not ackids <= finalids, "new actual unproved identity after publication")
            self.need(self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING" and self.summary["acknowledged"] is False, "new U refuses ACK")
        elif case == "nat_ack_incomplete":
            self.exit(14)
            self.strict_failures(set())
            vanished = self.events("native_probe_disappeared_before_identification")
            self.need(len(vanished) == 3 and {e["attempt"] for e in vanished} == {1, 2, 3} and ack["complete"] is False and
                      ack["incomplete_n"] > 0 and not ackids and self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING", "three genuine disappearance retries leave incomplete ACK with no additional live blocker")
        elif case == "nat_ack_disappearing_retry":
            self.exit(0)
            self.strict_failures(set())
            v = self.only("native_probe_disappeared_after_identity")
            uid = v["identity_before"]["uniqueid"]
            hist = s["reconciliation"]["census_observations"]
            self.need(ack["complete"] is True and not ackids and e["attempt_count"] >= 2 and
                      any(c["complete"] is False and any(p["uniqueid"] == uid for p in c["unproved_live"]) for c in hist) and
                      any(p["first_identity"]["uniqueid"] == uid for p in s["reconciliation"]["unproved_history"]), "disappearing retry identity/coverage history retained, only final complete ACK empty")
        else:
            self.strict_failures({"UNPROVED_LIVE"})
            subset = case == "nat_ack_existing_blocker_subset"
            self.exit(11 if subset else 14)
            self.need(len(finalids) == 1 and ack["complete"] is True and ((ackids <= finalids and bool(ackids)) if subset else (ackids > finalids)), "existing UNSETTLED blocker subset vs additional blocker")
            self.need(self.summary["acknowledged"] is subset and (self.summary.get("settlement") == "UNSETTLED" if subset else
                      self.summary.get("error_code") == "ACK_PROCESS_COVERAGE_CHANGED_OR_BLOCKING"), "exact subset ACK11/additional refusal14")
    def ack_age(self):
        if not self.events("ACK_native_output_delay"):
            self.absent("protected ACK output target not reached")
            return
        e, flush = self.only("ACK_native_output_delay"), self.only("native_ACK_flush_return")
        target = {ACK_AGE[0]: 0.99, ACK_AGE[1]: 1.0, ACK_AGE[2]: 1.01}[self.case]
        measured = flush["mono_after"] - e["census_mono"]
        if not target <= measured < target + 0.01:
            self.absent("measured completion census-age window missed; no native equality claim")
            return
        late = self.case != ACK_AGE[0]
        self.exit(14 if late else 0)
        self.strict_failures(set())
        self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0, "one printed ACK0 precedes actual completion decision")
        rows = self.events("original_resource_age_exception" if late else "original_resource_age_return")
        matching = [r for r in rows if r["census_mono"] == e["census_mono"] and r["mono_before"] >= flush["mono_after"]]
        self.need(len(matching) == 1, "original post-completion fresh-age decision actually observed")
        if late:
            self.need(error_text(matching[0]["error"]) == "RESOURCE_CENSUS_STALE_AT_COMMIT", "strict native age>1 refusal")
            self.post_ack_error("RESOURCE_CENSUS_STALE_AT_COMMIT")
        self.clean_full()
    def post_ack_error(self, code):
        rows = self.streams["stderr"].splitlines(keepends=True)
        exact(len(rows) == 1 and rows[0].endswith(b"\n"), "complete single post-ACK diagnostic capture")
        diag = decode(rows[0])
        self.need(diag["kind"] == "POST_ACK_REFUSAL_EVIDENCE" and diag["exit_code"] == 14 and diag["error_code"] == code, "actual captured refusal cause after printed ACK")
    def signals(self):
        case, s = self.case, self.state()
        rows = self.events("native_self_signal")
        expected_count = 2 if case == "nat_pending_after_handled" else 1
        exact(len(rows) == expected_count, "actual own signal count")
        for row in rows:
            self.need(row["pid"] == self.capture["pid"] and row["pgid"] == self.capture["pgid"] and
                      row["identity"]["pid"] == row["pid"] and row["signum"] in (1, 2, 15), "only approved identified own process signalled")
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
            self.need(rows[0]["signum"] in rows[0]["pending"] and self.summary["acknowledged"] is True and self.summary["exit_code"] == 0,
                      "real pending masked ACK cancellation after printed ACK")
            self.post_ack_error("CANCEL_DURING_ACK_COMPLETION")
        else:
            self.strict_failures({"POST_SPAWN_FAILURE"}, {"SUPERVISOR_CANCEL"})
            self.need(s["go_delivered"] is True and s["signal"]["sent"] is True and rows[0]["signum"] in rows[0]["pending"] and
                      "CANCEL_DURING_GO_COMPLETION" in self.source_errors() and s["cancel_handled"] is True, "masked GO signal causes original owned stop")
            if case == "nat_pending_after_handled":
                self.exit(14)
                self.need(rows[0]["signum"] == 15 and rows[1]["signum"] == 1 and 1 in rows[1]["pending"] and
                          self.summary.get("error_code") == "CANCEL_AT_ACK" and self.summary["acknowledged"] is False, "new pending signal cannot inherit earlier handled-cancel authority")
            else:
                self.exit(11)
                self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 11, "owned cancelled result acknowledged UNSETTLED11 only")
        self.clean_full(child=s["pid"] is not None)
    def protected(self):
        case, s = self.case, self.state()
        phase = "GO" if "_go_" in case else "ACK"
        rows = self.events("GO_native_delivery_delay" if phase == "GO" else "ACK_native_output_delay")
        if not rows:
            self.absent("actual protected native completion crossing not reached")
            return
        e = rows[0]
        if case in ("nat_completion_go_deadline", "nat_completion_ack_deadline"):
            clamp = self.only("fixed_original_deadline_clamp")
            cutoff = clamp["deadline"]["end"]
            crossed = e["injection_start"] < cutoff < e["injection_end"]
            code = "DEADLINE_EXCEEDED"
            self.need(clamp["scope"] == "API_RESPONSE_INJECTION", "deadline fixture clamp explicitly API, not hostclock/production fit change")
        elif case.endswith("_expiry"):
            cutoff = self.go["not_after_epoch"]
            begin_epoch = e.get("injection_start_epoch_raw")
            if begin_epoch is None:
                # Commit is a real earlier epoch, not a synthetic timestamp.
                begin_epoch = s["rec"]["go_commit"]["epoch"]
            crossed = begin_epoch < cutoff < e["epoch_end_raw"]
            code = "AUTHORIZATION_EXPIRED_DURING_" + phase
        else:
            cutoff = e["stability_expiry_mono"]
            crossed = e["injection_start"] < cutoff < e["injection_end"]
            code = "STABILITY_STALE"
        if not crossed:
            self.absent("recorded start < actual cutoff < end not established; already-late stimulus never qualifies")
            return
        completion = self.events("original_GO_write_all_exception" if case == "nat_completion_go_deadline" else "original_completion_exception")
        matching = [v for v in completion if (v.get("phase", "GO") == phase) and error_text(v["error"]).split(" ", 1)[0] == code]
        self.need(len(matching) == 1, "exact original protected completion dominant error, including earlier write_all guard")
        self.exit(11 if case == "nat_completion_go_deadline" else 14)
        if phase == "ACK":
            self.strict_failures(set())
            self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0, "post-ACK native crossing retains printed0/actual14")
            self.post_ack_error(code)
        elif case == "nat_completion_go_deadline":
            self.strict_failures({"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
            self.need(s["go_delivered"] is not True and s["signal"]["sent"] is True and
                      self.summary["acknowledged"] is True and self.summary["exit_code"] == 11,
                      "native bytes returned late but original write_all guard prevents delivery commit; owned stop and ACK11")
        else:
            self.strict_failures({"POST_SPAWN_FAILURE"})
            self.need(s["go_delivered"] is True and s["signal"]["sent"] is True, "actual delivered GO followed by owned stop")
            expected = "STABILITY_STALE" if case.endswith("_stability") else "GO_EXPIRED_AT_ACK"
            self.need(self.summary.get("error_code") == expected and self.summary["acknowledged"] is False,
                      "expired/stale authority also refuses later ACK")
        self.clean_full()
    def helper_full(self):
        case, s = self.case, self.state()
        helpers = s["reconciliation"]["helpers"]
        if case == "nat_helper_timely_success":
            self.exit(0)
            self.strict_failures(set())
            exact(len(helpers) >= 3, "actual admission/start/end clock helpers")
            for h in helpers:
                self.helper_proof(h, True)
            self.clean_full()
            return
        self.exit(10)
        self.strict_failures({"HELPER_CALL_FAILED"})
        self.need(s["pid"] is None and self.summary["settlement"] == "NOT_LAUNCHED" and self.summary["acknowledged"] is True,
                  "start-helper failure cannot launch compute")
        if case == "nat_helper_pre_spawn_allocation_failure":
            e = self.only("fixed_allocation_fault")
            self.need(e["scope"] == "API_RESPONSE_INJECTION" and e["native_call_made"] is False and e["errno"] == errno.EMFILE and
                      not any(r["purpose"] == "start" for r in self.events("native_spawn_registered")), "fixed pre-spawn API allocation failure with no PID")
            pipes = [r for r in self.events("native_source_pipe") if r["purpose"] == "start"]
            closed = {r["fd"] for r in self.events("native_source_close")}
            self.need(len(pipes) == 1 and set(pipes[0]["fds"]) <= closed, "all actual pre-spawn allocated descriptors closed")
        else:
            h = helpers[-1]
            self.helper_proof(h)
            self.need(h["date"] is None and h["leader_reaped"] is True and h["settled"] is True, "late/setup-failed clock call never supplies date but original cleanup settles")
            name = "native_helper_call_crossing" if case == "nat_helper_late_successful_reap" else "registered_PID_setup_crossing"
            e = self.only(name)
            if not e["injection_start"] < e["call_deadline"] < e["injection_end"]:
                self.absent("helper injection began after call deadline or missed real crossing")
            if case == "nat_helper_late_successful_reap":
                self.need(h["rc"] == 0 and h["mono_reaped"] > h["mono_call_deadline"], "actual native successful late reap rejected")
            else:
                self.need(h["spawn_error"] is not None and e["native_PID_registered"] is True, "returned PID retained through setup exception")
        self.clean_full(False)
    def helper_method(self):
        self.exit(0)
        out, case = self.outcome["source_outcome"], self.case
        exact(out["mode"] == "ORIGINAL_HELPER_METHODS" and out["source_date_now_not_replaced"] is True, "original native helper methods, not production clock substitution")
        declaration = self.only("declared_native_method_helper")
        h = out["helper"]
        if h is None:
            self.absent("method-negative native helper not acquired")
            return
        if self.state()["reconciliation"]["history_halted"]:
            self.absent("unrelated original history cap prevented the named helper lifecycle boundary")
            return
        expected = {"HELPER_CALL_FAILED"}
        if case not in ("nat_helper_bad_output", "nat_helper_nonzero_exit", "nat_helper_close_error"):
            expected.add("HELPER_OWNERSHIP_UNSETTLED")
        if case == "nat_helper_lost_wait":
            expected.add("HELPER_WAIT_STATUS_LOST")
        self.strict_failures(expected)
        self.need(declaration["date_assignment_forbidden"] is True and declaration["source_phase"] == "RUNNING" and
                  declaration["phase_scope"] == "DECLARED_METHOD_PRESTATE_NOT_PRODUCTION_LAUNCH" and h["date"] is None and
                  out["exception"] is not None, "declared running-phase native methods, not admission/launch or clock substitution")
        self.helper_proof(h)
        self.need("HELPER_CALL_FAILED" in self.state()["failure_codes"], "method helper failure retained")
        if case in ("nat_helper_bad_output", "nat_helper_nonzero_exit"):
            self.need(error_text(out["exception"]) == "HELPER_BAD_DATE_OUTPUT" and h["settled"] is True and
                      h["rc"] == (3 if case == "nat_helper_nonzero_exit" else 0), "exact original output-check AST refuses native invalid/nonzero fixture")
            self.need(b"20" not in bytes.fromhex(h["capture_hex"])[:4], "negative output not a substituted actual date")
        elif case == "nat_helper_lost_wait":
            e = self.only("native_competing_reaper")
            self.need(e["native_result"][0] == h["pid"] and h["wait_lost"] is True and h["leader_reaped"] is False and h["settled"] is False and
                      not (h.get("signal") or {}).get("sent") and any((e.get("error") or {}).get("type") == "ChildProcessError" for e in self.events("native_waitpid")),
                      "real competing destructive reap yields ECHILD, permanently no recovered signal/wait rights")
        elif case == "nat_helper_unverified_identity":
            post = decode(regular(self.run + "/scratch/helper-postexec.json")[1])
            self.need(post["identity"]["uniqueid"] == h["identity"]["uniqueid"] and post["identity"]["idversion"] != h["identity"]["idversion"] and
                      h["settled"] is False and not (h.get("signal") or {}).get("sent") and "HELPER_OWNERSHIP_UNSETTLED" in self.state()["failure_codes"],
                      "native reexec changes version; no TERM under stale fingerprint; continued blocking")
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
            self.need(any(p["pid"] == member["pid"] for p in listed) and h["settled"] is False and
                      (h["group_clear"] is False if case.endswith("live_group") else h["descendants_clear"] is False or h["coverage_complete"] is False),
                      "genuine live helper group/descendant/unproved member prevents settlement")
        elif case == "nat_helper_missing_eof":
            held, closed = self.only("native_extra_pipe_writer_held"), self.only("native_extra_pipe_writer_closed")
            self.need(held["fd"] == closed["fd"] and held["mono"] < closed["mono"] and h["leader_reaped"] is True and h["rc"] == 0 and
                      h["stdout_closed"] is False and h["eof_proved"] is False and h["settled"] is False, "real held writer prevents EOF despite native date reap, bounded own close afterward")
        elif case == "nat_helper_close_error":
            e = self.only("fixed_close_fault")
            self.need(e["scope"] == "API_RESPONSE_INJECTION" and e["native_close_made"] is False and e["descriptor_retained"] is True and
                      error_text(out["exception"]).startswith("[Errno 5]") and h["settled"] is True and h["stdout_closed"] is True, "API close error retains real descriptor until bounded native retry closes")
        elif case == "nat_helper_grace_exhaustion":
            self.need(h["signal"]["sent"] is True and h["settled"] is False and h["leader_reaped"] is False and
                      h["mono_cleanup_deadline"] <= self.only("native_helper_method_end")["mono"] and
                      "HELPER_OWNERSHIP_UNSETTLED" in self.state()["failure_codes"], "one actual TERM ignored; original grace exhaustion remains blocking")
    def caps(self):
        case, s = self.case, self.state()
        cap = self.only("fixed_history_cap_precharge")
        self.need(cap["scope"] == "API_CAP_STATE_INJECTION_NOT_NATIVE_COUNT" and cap["injected_charge"] == 4 << 20 and
                  cap["native_cap_attainment_claim"] is False, "fixed API cap pressure distinct from model/native-count claims")
        rec = s["reconciliation"]
        self.need(rec["history_halted"] is True and rec["history_overflow"]["kind"] == "HISTORY_BYTE_CAP", "original cap and permanent no-resumed-scan latch")
        snap = rec["history_overflow"]
        if case == "nat_cap_final_rss":
            self.exit(13)
            m = snap.get("completed_measurement")
            exact(type(m) is dict, "retained actual completed resource bracket after cap")
            self.need(m["bracket_verified"] is True and m["identity"]["pid"] == s["pid"] and fingerprint(m["identity"]) == fingerprint(m["identity_after"]) and
                      m["rss"] > self.cfg["rss_trip_bytes"] and m["rss"] <= 256 << 20 and "RSS" in s["trips"] and
                      s["signal"]["sent"] is True and s["rc"] is not None, "actual final identity bracket+native RSS excess and original owned TERM/reap survive cap")
            self.need(any(c["aborted"] is True and c.get("mono_aborted") is not None and c.get("mono_end") is not None for c in rec["census_observations"]), "aborted partial census retains end and extrema")
            self.need(self.summary["reason"] == "FINALIZATION_FAILED" and self.summary["error_code"] == "HISTORY_ALREADY_HALTED", "exact cap finalization refusal13")
        elif case == "nat_cap_initial_main":
            self.exit(13)
            p = s["rec"].get("main_initial_identity_observed")
            self.need(p is not None and fingerprint(p) == fingerprint(s["identity"]) and s["group"] == s["pid"] and
                      s["signal"]["sent"] is True and fingerprint(s["signal"]["identity_observed"]) == fingerprint(p) and
                      s["go_delivered"] is not True and s["rc"] is not None, "actual initial identity installed before auxiliary cap, original one TERM and raw wait retained")
            self.need(s["signal"]["identity_event_ref"] is None and s["signal"]["identity_observed"] is not None, "raw signal survives history halt without invented canonical event")
        else:
            self.exit(0)
            h = self.outcome["source_outcome"]["helper"]
            self.helper_proof(h)
            self.need(h["signal"]["sent"] is True and h["leader_reaped"] is True and h["rc"] == -15 and h["settled"] is False and
                      h["signal"]["identity_event_ref"] is None and cap["mono"] < h["signal"]["mono_sent"], "native cleanup TERM after cap, raw fingerprint/send/reap survives unavailable proof")
        end = rec["history_overflow"]["mono"]
        self.need(all(c["mono_start"] <= end for c in rec["census_observations"]) and
                  all(a["mono_start"] <= end for a in rec["observation_attempts"]), "no resumed scans or reservation acceptance after history halt")
    def platform(self):
        case = self.case
        if case in PLATFORM_METHOD:
            self.exit(0)
        if case == "nat_platform_abi_layout":
            e = self.only("native_ABI_layout")
            sdk = regular(e["pinned_files"]["sdk"]["path"])[1]
            private = regular(e["pinned_files"]["private"]["path"])[1]
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
            exact(scan["distinct_pids"] > 0 and scan["no_spawn_no_credentials_no_trace_no_PID_pressure"] is True, "actual bounded readonly prerequisite search")
            if not scan["matches"]:
                self.absent("genuine existing platform prerequisite absent; no forced credential/trace/PID reuse")
                return
            if case == "nat_platform_pid_reuse":
                e = self.only("native_real_PID_reuse")
                self.need(e["prior"]["pid"] == e["current"]["pid"] and e["prior"]["uniqueid"] != e["current"]["uniqueid"], "actual PID reuse, distinct incarnation not PID-only ownership")
            elif case in ("nat_platform_uid_change_observation", "nat_platform_trace_change_observation"):
                e = self.only("native_existing_metadata_change")
                keys = ("euid", "ruid") if case == "nat_platform_uid_change_observation" else ("traced",)
                self.need(e["prior"]["pid"] == e["current"]["pid"] and e["prior"]["uniqueid"] == e["current"]["uniqueid"] and
                          any(e["prior"][k] != e["current"][k] for k in keys) and e["no_credential_or_trace_change"] is True,
                          "genuine already-existing metadata change; no forced credentials or tracing")
            elif case == "nat_platform_trace_observation":
                for e in self.events("native_existing_trace_observation"):
                    self.need(e["before"]["traced"] is True and fingerprint(e["before"]) == fingerprint(e["after"]), "stable existing trace metadata, no trace changes forced")
            else:
                rows = [e for e in self.events("native_existing_mixed_UID_read") if e["error"] is not None]
                self.need(bool(rows), "actual native unreadability, never model EPERM")
                for e in rows:
                    self.need(e["before"]["ruid"] != e["before"]["euid"] and fingerprint(e["before"]) == fingerprint(e["after"]) and
                              e["error"]["errno"] in (errno.EPERM, errno.EACCES), "actual stable mixed UID permission failure")
            return
        s = self.state()
        if case == "nat_platform_fast_exit_zombie":
            e = self.only("native_fast_exit_status_before_initial")
            self.exit(11)
            self.need(e["identity"]["status"] == 5 and s["rec"]["main_initial_identity_observed"]["status"] == 5 and
                      s["go_delivered"] is not True and s["rc"] == 0, "native successful zombie identity acquisition before main install; actual EPIPE/owned failure retained")
            self.strict_failures({"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
        elif case == "nat_platform_startup_reexec":
            self.exit(11)
            before = decode(regular(self.run + "/scratch/preexec.json")[1])
            after = decode(regular(self.run + "/scratch/postexec.json")[1])
            self.need(before["identity"]["uniqueid"] == after["identity"]["uniqueid"] and before["identity"]["idversion"] != after["identity"]["idversion"] and
                      before["identity"]["idversion"] == s["identity"]["idversion"] and self.only("native_startup_reexec_barrier")["value"] == after and
                      s["signal"]["sent"] is False and s["go_delivered"] is not True and s["rc"] == 6, "genuine startup exec after installed original identity; no stale TERM or GO")
            self.strict_failures({"CHILD_IDENTITY_CHANGED", "IDENTITY_UNVERIFIED", "POST_SPAWN_FAILURE", "GO_NOT_DELIVERED"})
        else:
            self.exit(0)
            self.strict_failures(set())
            self.clean_full()
            owner = self.child["owner"]
            self.need(owner["mask"] == [] and owner["pid"] == owner["pgid"] == owner["sid"] == s["pid"], "native child empty inherited mask/fresh process session")
            waits = [e for e in self.events("native_waitpid") if e["pid"] == s["pid"]]
            success = [e for e in waits if e.get("native_result", [0])[0]]
            self.need(len(success) == 1 and waits[-1] == success[0] and all(e["options"] == os.WNOHANG for e in waits), "original sole native wait ownership; no wait after destructive result")
    def hardlink(self):
        self.exit(0)
        e = self.only("native_hardlink_charge")
        a, alias, distinct = e["original"], e["alias"], e["distinct"]
        self.need(a["inode"] == alias["inode"] != distinct["inode"] and a["sha256"] == alias["sha256"] == distinct["sha256"] and
                  a["bytes"] == alias["bytes"] == distinct["bytes"] == e["payload_bytes"] and a["nlink"] == alias["nlink"] == 2 and distinct["nlink"] == 1,
                  "actual aliases same dev/inode, identical bytes on a different inode")
        self.need(e["created_original"]["inode"] == a["inode"] and e["created_original"]["sha256"] == a["sha256"] and
                  e["created_original"]["nlink"] == 1, "hardlink original exclusive-created descriptor survives alias creation")
        actual, total = inventory(self.run + "/tmp")
        self.need(total == e["source_walk_total"] == 2 * e["payload_bytes"] and
                  sum(r.get("bytes", 0) for r in actual.values()) == e["raw_path_sum"] == 3 * e["payload_bytes"],
                  "original native walk charges same-inode aliases once and byte-identical distinct inode separately; method only")
    def integration(self):
        if self.case == "nat_integration_printed_ack_actual14":
            self.signals()
            return
        self.exit(0)
        self.strict_failures(set())
        self.clean_full()
        s = self.state()
        self.need(s["rc"] == (7 if self.case == "nat_integration_rc7" else 0) and self.summary["acknowledged"] is True and
                  self.summary["exit_code"] == 0 and self.summary["child_returncode"] == s["rc"], "SETTLED transport never scientific acceptance, including native child7")
        facts, samples = regular(self.cfg["samples"], 1 << 20)
        decoder = json.JSONDecoder(object_pairs_hook=pairs)
        text, pos, rows = samples.decode(), 0, []
        while pos < len(text):
            while pos < len(text) and text[pos].isspace():
                pos += 1
            if pos == len(text):
                break
            row, pos = decoder.raw_decode(text, pos)
            rows.append(row)
        self.need(len(rows) == s["rec"]["samples_written"] >= 1 and facts["bytes"] == s["rec"]["samples_bytes"] and
                  facts["sha256"] == s["rec"]["evidence_expected_sha256"][self.cfg["samples"]], "normal/immediate-GO exits retain actual nonempty hashed complete samples")
        protocol = self.child["protocol"]
        self.need(protocol["bytes"] == 3 and protocol["raw_hex"] == b"GO\n".hex() and protocol["eof"] is True, "ordinary exact GO+EOF still actual")
    def derived(self):
        self.exit(0)
        out = self.outcome["source_outcome"]
        exact(out["mode"] == "FIXED_ORACLE_NEGATIVE_FRESH_COPY" and out["negative_scope"] == "ORACLE_INPUT_NOT_NATIVE_SOURCE_OUTCOME", "derived scope not native evidence")
        base = self.request["derived_base"]
        exact(base == out["base"] and base["case"] == "nat_integration_normal_exit", "fixed base join")
        verdict = Oracle(base["case"], base["approval_sha256"], base["capture_sha256"]).verify()
        if verdict["status"] != "FIXTURE_PREDICATES_MET":
            self.absent("independent actual base native normal-exit evidence not met")
            return
        objects = out["objects"]
        rejected = None
        if self.case == "nat_integration_incomplete_capture":
            original, raw = regular(objects["original"]["path"])
            copied, bad = regular(objects["copy"]["path"])
            self.need(same(original, objects["original"]) and same(copied, objects["copy"]) and original["inode"] != copied["inode"] and
                      bad == raw[:-1] and not bad.endswith(b"\n"), "fresh actual truncated capture bytes, original untouched")
            if bad != raw or sha(bad) != objects["original_capture"]["sha256"] or len(bad) != objects["original_capture"]["bytes"]:
                rejected = "CAPTURE_BYTES_OR_COMPLETENESS"
        elif self.case == "nat_integration_digest_inode_mismatch":
            original, raw = regular(objects["original"]["path"])
            copied, other = regular(objects["copy"]["path"])
            self.need(same(original, objects["original"]) and same(copied, objects["copy"]) and raw == other and
                      original["inode"] != copied["inode"] and objects["expected_original_inode"] == original["inode"], "fresh equal-digest different native inode, not an old mutation")
            if copied["inode"] != objects["expected_original_inode"]:
                rejected = "ORIGINAL_ARTIFACT_INODE"
        elif self.case == "nat_integration_unresolved_identity":
            copied, raw = regular(objects["copy"]["path"], 8 << 20)
            obj = decode(raw)
            self.need(same(copied, objects["copy"]) and obj["unresolved"] == [{"kind": "ORACLE_NEGATIVE_ACTUAL_LIVE_OWNER", "identity": objects["actual_identity"]}] and
                      objects["actual_identity"]["pid"] == self.capture["pid"], "fresh input contains actual live fixture owner, explicitly not producer discovery")
            if obj["unresolved"]:
                rejected = "UNRESOLVED_IDENTITY"
        else:
            facts, raw = regular(objects["late_artifact"]["path"])
            pfd = directory(self.run + "/scratch")
            try:
                names = sorted(os.listdir(pfd))
            finally:
                os.close(pfd)
            self.need(same(facts, objects["late_artifact"]) and raw == b"fixed late artifact after empty captured inventory\n" and objects["before_names"] == [],
                      "fresh actual late bytes/inode relative to original empty fixture inventory")
            if names != objects["before_names"]:
                rejected = "LATE_ARTIFACT_INVENTORY"
        self.need(rejected == {DERIVED[0]: "CAPTURE_BYTES_OR_COMPLETENESS", DERIVED[1]: "ORIGINAL_ARTIFACT_INODE",
                              DERIVED[2]: "UNRESOLVED_IDENTITY", DERIVED[3]: "LATE_ARTIFACT_INVENTORY"}[self.case], "independently recomputed strict rejection, never flag-only acceptance")
    def post_publication(self):
        self.exit(0)
        self.strict_failures(set())
        self.clean_full()
        before = self.only("post_publication_API_entry")
        after = self.only("post_publication_native_helper_activity")
        s = self.state()
        self.need(before["scope"] == "API_ENTRY_STIMULUS" and before["trips_before"] == {} and before["failures_before"] == [] and before["stop_before"] is None and
                  after["scope"] == "NATIVE_HELPER_ACTIVITY" and after["no_resource_excess_claim"] is True and
                  s["stop"]["reason"] == "FIXED_POST_PUBLICATION_API_ENTRY" and s["signal"]["why_not"] == "CHILD_ALREADY_REAPED", "one clean explicit postpublication original request_stop entry, no invented trip/excess")
        _, receipt_raw = regular(self.cfg["receipt"], 4 << 20)
        receipt = decode(receipt_raw)
        current = s["reconciliation"]["helpers"]
        self.need(receipt["helpers"] == before["helper_prefix"] and current[:-1] == receipt["helpers"] and len(current) == len(receipt["helpers"]) + 1 and
                  current[-1]["date"] == s["stop"]["date"] and current[-1]["mono_spawn"] > self.summary["post_publish_mono"], "historical receipt prefix vs new actual owned /bin/date helper after publication")
        self.helper_proof(current[-1], True)
        self.need(self.summary["acknowledged"] is True and self.summary["exit_code"] == 0 and self.summary["ack_resources"] == before["accounting"] and
                  self.summary["reconciliation"]["helpers"] == current and self.summary["publication_payload_bytes"] == self.summary["receipt_bytes"] + self.summary["settlement_bytes"],
                  "dominant source19 ACK0/current helper/accounting join without backediting historical receipt")
    def verify(self):
        self.auth()
        self.common()
        case = self.case
        if case in RUNTIME:
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
