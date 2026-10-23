#!/usr/bin/env python3
"""Independent fixed STATE_ONLY oracle; no driver import/execution and no release.
CLI: CASE_ID APPROVAL_SHA256 PARENT_CAPTURE_SHA256
Reads exact external parent capture + full driver.stdout/stderr + actual outcome.
Only FIXTURE_PREDICATES_MET / NOT_MET / NOT_EXERCISED / HOLD are conclusions.
Native terminal14 and every native integration obligation remain NOT_EXERCISED.
"""
import ast
import datetime
import hashlib
import json
import math
import os
import resource
import signal
import stat
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ROOT = LANE + "/qual-matrix-v1-v19"
# Successor install paths (parent-pinned at integration; originals stay frozen at their v1 paths).
DRIVER = LANE + "/code/guard_matrix_state_v2.py"
ORACLE = LANE + "/code/guard_matrix_state_check_v2.py"
SPECS = LANE + "/review/rqls10-matrix-state-v2-cases.json"
# Review candidate; exact freeze pins are external and source-ready confers no runtime authority.
SUPERVISOR = LANE + "/code/owned_supervisor_v19.py"
SUPERVISOR_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
SCOPE = "STATE_ONLY"
HOOK_SET = "rqls10-state-model-v1"
LIMIT = 16 << 20
CASES = (
    "st_runtime_999", "st_runtime_1000", "st_runtime_1026",
    "st_go_w10_lt", "st_go_w10_eq", "st_go_w10_gt", "st_go_w200_lt", "st_go_w200_eq", "st_go_w200_gt",
    "st_age_lt", "st_age_eq", "st_age_gt", "st_date_missing", "st_date_malformed", "st_date_naive", "st_date_future",
    "st_stability_rollback", "st_stability_refresh", "st_stability_tighten",
    "st_ack_age_lt", "st_ack_age_eq", "st_ack_age_gt", "st_retry_unproved", "st_retry_busy", "st_retry_rss",
    "st_abort_identity", "st_abort_resource", "st_cap_bytes_lt", "st_cap_bytes_eq", "st_cap_bytes_gt",
    "st_cap_identity_lt", "st_cap_identity_eq", "st_cap_identity_gt", "st_cap_unproved_lt", "st_cap_unproved_eq", "st_cap_unproved_gt",
    "st_cap_coverage_lt", "st_cap_coverage_eq", "st_cap_coverage_gt", "st_cap_attempt_lt", "st_cap_attempt_eq", "st_cap_attempt_gt",
    "st_cap_census_lt", "st_cap_census_eq", "st_cap_census_gt", "st_cap_variants_lt", "st_cap_variants_eq", "st_cap_variants_gt",
    "st_cap_final_rss", "st_cap_initial_main", "st_cap_helper_term",
    "st_budget_output_lt", "st_budget_output_eq", "st_budget_output_gt",
    "st_budget_reservation_lt", "st_budget_reservation_eq", "st_budget_reservation_gt",
    "st_budget_free_lt", "st_budget_free_eq", "st_budget_free_gt", "st_budget_lane_lt", "st_budget_lane_eq", "st_budget_lane_gt",
    "st_cutoff_census_lt", "st_cutoff_census_eq", "st_cutoff_census_gt",
    "st_cutoff_helper_lt", "st_cutoff_helper_eq", "st_cutoff_helper_gt",
    "st_cutoff_stop_grace_lt", "st_cutoff_stop_grace_eq", "st_cutoff_stop_grace_gt",
    "st_cutoff_exit_grace_lt", "st_cutoff_exit_grace_eq", "st_cutoff_exit_grace_gt",
    "st_cutoff_finalize_lt", "st_cutoff_finalize_eq", "st_cutoff_finalize_gt",
    "st_write_short", "st_write_zero", "st_write_late", "st_manifest_4095", "st_manifest_4096", "st_manifest_4097",
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


def canon(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


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
            raise Invalid("nonfinite JSON")
        return value
    def constant(text):
        raise Invalid("nonfinite JSON constant")
    return json.loads(raw.decode(), object_pairs_hook=pairs, parse_float=floating, parse_constant=constant)


def integer(value, minimum=0):
    return type(value) is int and value >= minimum


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def hex64(value):
    return type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def same(a, b):
    return canon(a) == canon(b)


def near(a, b):
    return number(a) and number(b) and abs(a - b) <= 1e-8


class Budget:
    def __init__(self):
        self.begin = time.monotonic()

    def check(self):
        if time.monotonic() - self.begin > 280 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 256 << 20:
            raise Invalid("oracle cooperative resource budget")


def directory(path):
    if not path.startswith("/") or os.path.normpath(path) != path:
        raise Invalid("directory path")
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


def signature(s):
    return (s.st_dev, s.st_ino, s.st_mode, s.st_size, s.st_nlink, s.st_mtime_ns, s.st_ctime_ns)


def snapshot(fdroot, name, budget, cap=LIMIT):
    budget.check()
    st = os.stat(name, dir_fd=fdroot, follow_symlinks=False)
    if not stat.S_ISREG(st.st_mode) or not 0 <= st.st_size <= cap or st.st_nlink != 1:
        raise Invalid("bounded one-link regular file required")
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fdroot)
    try:
        if signature(os.fstat(fd)) != signature(st):
            raise Invalid("changed open")
        parts, size = [], 0
        while size < st.st_size:
            budget.check()
            part = os.read(fd, min(65536, st.st_size - size))
            if not part:
                raise Invalid("short read")
            parts.append(part)
            size += len(part)
        if os.read(fd, 1) or signature(os.fstat(fd)) != signature(st) or \
                signature(os.stat(name, dir_fd=fdroot, follow_symlinks=False)) != signature(st):
            raise Invalid("changed read")
    finally:
        os.close(fd)
    raw = b"".join(parts)
    budget.check()
    return {"raw": raw, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
            "inode": [st.st_dev, st.st_ino], "nlink": st.st_nlink, "mode": stat.S_IMODE(st.st_mode)}


def absolute(path, budget):
    fd = directory(os.path.dirname(path))
    try:
        return snapshot(fd, os.path.basename(path), budget)
    finally:
        os.close(fd)


def facts(value):
    return {k: value[k] for k in ("sha256", "bytes", "inode", "nlink", "mode")}


def unhex(value, encoding="UTF8_HEX"):
    if type(value) is not dict or value.get("encoding") != encoding or \
            value.get("scope") not in ("MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "MODEL_INPUT"):
        raise Invalid("explicit model hex encoding required")
    raw = bytes.fromhex(value["hex"])
    if len(raw) != value.get("bytes") or hashlib.sha256(raw).hexdigest() != value.get("sha256"):
        raise Invalid("hex length/digest")
    return raw


def restore(value):
    if type(value) is dict:
        if value.get("encoding") == "UTF8_HEX":
            return unhex(value).decode("utf-8", "surrogatepass")
        if value.get("encoding") == "BYTES_HEX":
            return unhex(value, "BYTES_HEX")
        return {k: restore(v) for k, v in value.items()}
    if type(value) is list:
        return [restore(v) for v in value]
    return value


def exact_authority(case, approval_sha, capture_sha, runfd, budget):
    apf, rqf, cpf, of = (snapshot(runfd, name, budget) for name in
                         ("parent-authorization.json", "request.json", "parent-capture.json", "fixture-outcome.json"))
    if apf["sha256"] != approval_sha or cpf["sha256"] != capture_sha:
        raise Invalid("external approval/capture SHA trust roots")
    ap, rq, cp, outcome = (decode(v["raw"]) for v in (apf, rqf, cpf, of))
    run = {"path": ROOT + "/" + case, "inode": [os.fstat(runfd).st_dev, os.fstat(runfd).st_ino]}
    aq = {"kind", "case", "scope", "request_sha256", "run", "sources", "hook_set", "negative_control", "allocation",
          "not_after_epoch", "authority", "ownership_negative", "mutation_negative", "native_config"}
    rqkeys = {"kind", "case", "scope", "run", "hook_set", "negative_control", "allocation", "not_after_epoch", "model_inputs_sha256"}
    if type(ap) is not dict or set(ap) != aq or type(rq) is not dict or set(rq) != rqkeys or \
            ap["kind"] != "rqls10-guard-matrix-invocation-v1" or rq["kind"] != "rqls10-guard-matrix-request-v1":
        raise Invalid("request/approval exact schema")
    negative = {"kind": "MODEL_STATE", "case": case, "native_process": False, "native_mutation": False}
    for obj in (ap, rq):
        if obj["case"] != case or obj["scope"] != SCOPE or not same(obj["run"], run) or \
                obj["hook_set"] != HOOK_SET or not same(obj["negative_control"], negative):
            raise Invalid("case/scope/run/negative/hook binding")
    if ap["request_sha256"] != rqf["sha256"] or ap["authority"] != "PARENT_INDIVIDUAL_INVOCATION_NO_RELEASE" or \
            ap["ownership_negative"] is not False or ap["mutation_negative"] is not False or ap["native_config"] is not None or \
            not same(ap["allocation"], rq["allocation"]) or not same(ap["not_after_epoch"], rq["not_after_epoch"]):
        raise Invalid("authority cross-binding")
    allocation = rq["allocation"]
    fixed = {"bytes": LIMIT, "cpu_slots": 1, "max_wall_s": 300.0, "rss_bytes": 256 << 20,
             "output_bytes": LIMIT, "busy_limit": 2, "no_three_loops": True}
    if type(allocation) is not dict or set(allocation) != set(fixed) | {"outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"} or \
            any(not same(allocation[k], v) for k, v in fixed.items()) or any(not integer(allocation[k]) for k in
                ("outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")):
        raise Invalid("exact bounded allocation")
    paths = {"supervisor": SUPERVISOR, "driver": DRIVER, "oracle": ORACLE, "case_specs": SPECS}
    if type(ap["sources"]) is not dict or set(ap["sources"]) != set(paths):
        raise Invalid("all source bindings")
    actual_sources = {}
    for key, path in paths.items():
        pin = ap["sources"][key]
        actual = absolute(path, budget)
        if type(pin) is not dict or set(pin) != {"path", "sha256"} or pin["path"] != path or \
                actual["sha256"] != pin["sha256"] or actual["mode"] != 0o444:
            raise Invalid("actual frozen source pin")
        actual_sources[key] = actual
    if actual_sources["supervisor"]["sha256"] != SUPERVISOR_SHA:
        raise Invalid("original source pin")
    specs = decode(actual_sources["case_specs"]["raw"])
    if set(specs.get("cases", {})) != set(CASES) or specs.get("kind") != "rqls10-matrix-state-v1-cases" or \
            specs.get("supervisor") != {"path": SUPERVISOR, "sha256": SUPERVISOR_SHA} or \
            rq["model_inputs_sha256"] != hashlib.sha256(canon(specs["cases"][case])).hexdigest():
        raise Invalid("exact fixed-case source/inputs spec binding")
    capture_keys = {"kind", "case", "approval_sha256", "driver_source_sha256", "pid", "pgid", "mono_begin", "mono_end",
                    "actual_exit", "stdout", "stderr", "outcome_sha256", "wait_status"}
    if type(cp) is not dict or set(cp) != capture_keys or cp["kind"] != "rqls10-guard-matrix-parent-capture-v1" or \
            cp["case"] != case or cp["approval_sha256"] != approval_sha or \
            cp["driver_source_sha256"] != actual_sources["driver"]["sha256"] or cp["outcome_sha256"] != of["sha256"]:
        raise Invalid("external capture exact binding")
    if not integer(cp["pid"], 1) or not integer(cp["pgid"], 1) or not number(cp["mono_begin"]) or \
            not number(cp["mono_end"]) or not 0 <= cp["mono_end"] - cp["mono_begin"] <= 300:
        raise Invalid("capture owner/budget")
    wait = cp["wait_status"]
    if type(wait) is not dict or set(wait) != {"native_wait_status", "waitpid_pid", "reaped"} or \
            not integer(wait["waitpid_pid"], 1) or wait["waitpid_pid"] != cp["pid"] or wait["reaped"] is not True or \
            not integer(wait["native_wait_status"]) or type(cp["actual_exit"]) is not int or \
            os.waitstatus_to_exitcode(wait["native_wait_status"]) != cp["actual_exit"]:
        raise Invalid("native parent wait status join")
    captures = {}
    for stream in ("stdout", "stderr"):
        entry = cp[stream]
        path = run["path"] + "/driver." + stream
        if type(entry) is not dict or set(entry) != {"path", "sha256", "bytes", "inode", "eof"} or \
                entry["path"] != path or entry["eof"] is not True or not hex64(entry["sha256"]) or \
                not integer(entry["bytes"], 0) or type(entry["inode"]) is not list or len(entry["inode"]) != 2 or \
                not all(integer(v, 0) for v in entry["inode"]):
            raise Invalid("complete capture original-created-inode/EOF exact schema")
        actual = snapshot(runfd, "driver." + stream, budget)
        if actual["sha256"] != entry["sha256"] or actual["bytes"] != entry["bytes"] or not same(actual["inode"], entry["inode"]):
            raise Invalid("actual complete capture digest/size/original-created-inode")
        captures[stream] = actual
    out_lines = captures["stdout"]["raw"].splitlines(keepends=True)
    if len(out_lines) != 2 or any(not row.endswith(b"\n") for row in out_lines):
        raise Invalid("exact owner + outcome stdout framing")
    first, last = (decode(row) for row in out_lines)
    if type(first) is not dict or set(first) != {"kind", "pid", "pgid", "mono_begin", "scope"} or \
            first["kind"] != "rqls10-matrix-owner-v1" or first["scope"] != SCOPE or \
            not integer(first["pid"], 1) or not integer(first["pgid"], 1) or not number(first["mono_begin"]) or \
            not same([first["pid"], first["pgid"]], [cp["pid"], cp["pgid"]]):
        raise Invalid("first native owner record")
    owner = outcome.get("owner")
    if type(owner) is not dict or set(owner) != {"pid", "pgid", "mono_begin", "mono_end"} or \
            not integer(owner["pid"], 1) or not integer(owner["pgid"], 1) or \
            not number(owner["mono_begin"]) or not number(owner["mono_end"]) or \
            not same([owner["pid"], owner["pgid"], owner["mono_begin"]], [cp["pid"], cp["pgid"], first["mono_begin"]]) or \
            not cp["mono_begin"] <= owner["mono_begin"] <= owner["mono_end"] <= cp["mono_end"]:
        raise Invalid("owner/capture monotonic ordering")
    # The marker carries the ORIGINAL O_EXCL-created descriptor inode, bound by externally captured stdout.
    # This is a driver-reported origin assertion, not self-authentication; the external J18 adapter remains mandatory.
    if type(last) is not dict or set(last) != {"kind", "case", "scope", "outcome_sha256", "bytes", "outcome_inode"} or \
            not integer(last["bytes"]) or type(last["outcome_inode"]) is not list or len(last["outcome_inode"]) != 2 or \
            not all(integer(v) for v in last["outcome_inode"]) or \
            not same(last, {"kind": "rqls10-state-outcome-written-v1", "case": case, "scope": SCOPE,
                            "outcome_sha256": of["sha256"], "bytes": of["bytes"], "outcome_inode": of["inode"]}):
        raise Invalid("exclusive original-created outcome inode/capture/reopen join")
    if outcome.get("kind") != "rqls10-guard-matrix-outcome-v1" or outcome.get("case") != case or outcome.get("scope") != SCOPE:
        raise Invalid("outcome kind/case/scope")
    binding = {"approval_sha256": approval_sha, "request_sha256": rqf["sha256"], "run": run, "sources": ap["sources"],
               "hook_set": HOOK_SET, "allocation": rq["allocation"], "negative_control": negative,
               "model_inputs_sha256": rq["model_inputs_sha256"], "not_after_epoch": rq["not_after_epoch"], "native_config": None}
    if not same(outcome.get("bindings"), binding):
        raise Invalid("outcome actual authority binding")
    for key, entry in (("request", rqf), ("approval", apf)):
        record = outcome["artifacts"][key]
        if not same(record, {"original": facts(entry), "current": facts(entry)}):
            raise Invalid("authority original/current inode+digest")
    if not same(outcome["artifacts"]["sources"], {k: facts(v) for k, v in actual_sources.items()}):
        raise Invalid("source original facts")
    return outcome, cp, captures, actual_sources, specs, of


def verify_source(model, source):
    raw = source["raw"]
    tree = ast.parse(raw.decode(), filename=SUPERVISOR)  # Parse only; never execute driver/original code.
    lines = raw.splitlines(keepends=True)
    assignments = {"VERSION", "CANCEL_SIGNALS", "CANCEL", "CANCEL_FAILURE_TARGET", "POLICY", "SMALL", "PIN_CAP",
                   "PUBLICATION_CAP", "IO_S", "CENSUS_S", "FINALIZE_S", "WALK_ENTRIES", "ROOT_ENTRIES", "CONFIG",
                   "HELPER", "HELPER_FAULTS", "ADMISSION", "BOUND_KEYS", "MY_PID", "MY_UID", "SELF", "SZOMB"}
    expected = []
    for node in tree.body:
        label = None
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and node.name not in {"main", "sink"}:
            label = node.name
        elif isinstance(node, ast.Assign):
            names = {n.id for target in node.targets for n in ast.walk(target) if isinstance(n, ast.Name)}
            if names and names <= assignments:
                label = ",".join(sorted(names))
        if label is not None:
            start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
            expected.append({"symbol": label, "line_begin": start, "line_end": node.end_lineno,
                             "sha256": hashlib.sha256(b"".join(lines[start - 1:node.end_lineno])).hexdigest()})
    if model["symbols"] != expected:
        raise Invalid("complete exact original v19 AST allowlist/provenance")
    values = {"bytes": ("reserve_history", "self.history_charge + charge >", 4 << 20, "Gt"),
              "identity": ("retain_identity", "len(self.identity_history) >=", 8192, "GtE"),
              "unproved": ("retain_identity", "len(self.unproved_history) >=", 8192, "GtE"),
              "coverage": ("retain_coverage", "len(self.coverage_history) >=", 16384, "GtE"),
              "attempt": ("observation_attempt", "len(self.attempt_history) >=", 4096, "GtE"),
              "census": ("census", "len(self.census_history) >=", 4096, "GtE"),
              "variants": ("retain_identity", "len(variants) >=", 64, "GtE"),
              "raw": ("raw_acquisition", "len(self.raw_acquisitions) >=", 128, "GtE"),
              "clockless": ("helper_clockless_once", "if count >=", 3, "GtE")}
    def literal(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.LShift):
            return literal(node.left) << literal(node.right)
        raise Invalid("nonliteral source cap")
    for family, (symbol, fragment, cap, operator) in values.items():
        functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == symbol]
        if len(functions) != 1:
            raise Invalid("unique original cap method")
        fn = functions[0]
        hits = [line for line in range(fn.lineno, fn.end_lineno + 1) if fragment in lines[line - 1].decode()]
        if len(hits) != 1:
            raise Invalid("original cap anchor")
        comparisons = [n for n in ast.walk(fn) if isinstance(n, ast.Compare) and n.lineno == hits[0]]
        if len(comparisons) != 1 or literal(comparisons[0].comparators[0]) != cap or type(comparisons[0].ops[0]).__name__ != operator or \
                model["caps"][family] != {"value": cap, "symbol": symbol, "line": hits[0], "operator": operator}:
            raise Invalid("independently recomputed original cap")
    for rule in model["clock_rules"]:
        line = rule["line"]
        if not integer(line, 1) or rule["snippet"] not in lines[line - 1].decode():
            raise Invalid("clock dependency input source site")
        for parent in rule["within"]:
            functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == parent["function"]]
            if len(functions) != 1 or (parent["line"] is not None and
                    (not functions[0].lineno <= parent["line"] <= functions[0].end_lineno or
                     parent["snippet"] not in lines[parent["line"] - 1].decode())):
                raise Invalid("clock dependency enclosing source site")
        if rule["clock"] not in ("time", "monotonic") or rule["action"] not in ("set", "epoch", "raise", "observe"):
            raise Invalid("fixed clock-response hook kind")
    constants = {}
    for name in ("IO_S", "CENSUS_S", "FINALIZE_S"):
        found = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1 and
                 isinstance(n.targets[0], ast.Name) and n.targets[0].id == name]
        if len(found) != 1 or not isinstance(found[0].value, ast.Constant) or not number(found[0].value.value):
            raise Invalid("original literal cutoff constant")
        constants[name] = found[0].value.value
    return {"caps": values, "constants": constants}


def succeeded(step):
    """Success is ONLY a null exception; an encoded or caught exception object never implies completion."""
    return step["exception"] is None


def raised(step, expected):
    """Exact permitted failure with exclusive null return: GuardError code, or ValueError only for the parser ValueError."""
    error, kind = step["exception"], "ValueError" if expected == "ValueError" else "GuardError"
    return type(expected) is str and type(error) is dict and set(error) == {"type", "code", "text"} and \
        error["type"] == kind and error["code"] == expected and type(error["text"]) is str and \
        error["text"].startswith(kind + "(") and step["return"] is None


def outcome_is(step, expected):
    return succeeded(step) if expected is None else raised(step, expected)


def fingerprint(p):
    return tuple(p[k] for k in ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced"))


def relation(value, boundary):
    """Exact side of a declared MODEL boundary: equality is exact, never approximate."""
    if not number(value) or not number(boundary):
        raise Invalid("nonnumeric boundary relation")
    return "eq" if value == boundary else "lt" if value < boundary else "gt"


def table(mapping, key):
    """Prose expectations are interpreted only through exact fixed tables; anything else is unenforceable (HOLD)."""
    if type(key) is not str or key not in mapping:
        raise Invalid("uninterpretable selected expectation")
    return mapping[key]


def expectation(spec, case):
    """The selected SHA-bound immutable case object is the only source of discriminators and expected results."""
    if type(spec) is not dict or spec.get("id") != case or spec.get("scope") != SCOPE or type(spec.get("fixed_inputs")) is not dict:
        raise Invalid("selected case identity")
    if spec.get("contract_ref") == "added_case_common":
        expected = spec.get("expected")
    else:
        outer = spec.get("expected")
        if type(outer) is not dict or set(outer) != {"driver_actual_exit", "source", "oracle"}:
            raise Invalid("selected case expected envelope")
        expected = outer["source"]
    if type(expected) is not dict:
        raise Invalid("selected case expected outcome")
    return spec["fixed_inputs"], expected


FINAL_STATE_KEYS = {
    "phase", "pid", "ident", "group", "rc", "lost_wait", "mono_spawn", "epoch_spawn", "exit_mono",
    "exit_epoch", "stop", "signal", "clear", "loop_status", "failures", "trips", "runtime_observations",
    "history_charge", "history_halted", "history_overflow", "stability_expiry_mono", "clock_observation",
    "authorization", "maxima", "min_free", "publication_resources", "ack_resources",
    "publication_payload_bytes", "last_accounting_observation", "accounting_observations",
    "min_free_witness", "identity_events", "helper_calls", "helper_log", "ack_output_started",
    "cancel_handled", "rec", "timing_failed", "last_native_free", "streams", "raw_sequence", "histories",
    "helpers", "cancel", "pending_signals", "failure_codes", "owned", "baseline_uniqueids",
    "raw_acquisitions", "main_wait", "cancellation_target_installed", "anchor_fds"}
HELPER_KEYS = {
    "pid", "identity", "identity_event_ref", "leader_reaped", "rc", "wait_lost", "term_attempted",
    "settled", "initial_identity_valid", "stdout_closed", "eof_proved", "group_clear", "descendants_clear",
    "coverage_complete", "clock_failed", "date", "signal", "proof", "spawn_error", "launch_commit",
    "mono_spawn", "epoch_spawn", "mono_pid_registered", "call_deadline", "cleanup_deadline",
    "native_wait_result", "raw_wait_status", "epoch_reaped", "raw_identity_ref", "clockless_probe_done",
    "clockless_probe_count", "endpoint_errors", "mono_call_start", "mono_call_deadline",
    "mono_cleanup_start", "mono_cleanup_deadline", "mono_proof_complete", "mono_reaped",
    "mono_injection_start", "mono_injection_end", "stability_expiry_before", "stability_expiry_candidate",
    "stability_expiry_effective", "capture_hex"}
MAIN_WAIT_KEYS = {"pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "wait_lost", "mono_reaped",
                  "epoch_reaped", "mono_reaped_error", "epoch_reaped_error"}
LEDGER_KEYS = {"first_identity", "last_identity", "mono_first_begin", "mono_first_seen", "mono_last_begin", "mono_last_seen",
               "first_event_ref", "last_event_ref", "source", "observations", "variants"}
UNPROVED_KEYS = LEDGER_KEYS - {"source", "observations", "variants"}
OP_FIELDS = {"waitpid": {"pid", "flags", "mono_before", "mono_after", "returned"}, "killpg": {"pgid", "signal"},
             "write": {"fd", "requested", "returned", "mono_before", "mono_after", "sha256", "response_scope"},
             "close": {"fd"}, "pipe": {"read_fd", "write_fd"}, "open": {"fd", "path", "inode", "flags"},
             "read": {"fd", "requested", "returned", "sha256"}, "fsync": {"fd"}, "set_blocking": {"fd", "value"},
             "link": {"source", "target", "inode"}, "posix_spawn": {"pid", "pgid", "argv", "setsid", "setsigmask", "helper"},
             "proc_listallpids": {"pids", "capacity_bytes"}, "sleep": {"requested_s", "model_quantum_s"},
             "sigpending": {"signals"}, "sigmask": {"how", "signals"}, "stream_write": {"stream", "bytes", "sha256"},
             "stream_flush": {"stream"}}
OP_INTS = {"waitpid": ("pid", "flags"), "killpg": ("pgid", "signal"), "write": ("fd", "requested", "returned"),
           "close": ("fd",), "pipe": ("read_fd", "write_fd"), "proc_pidinfo": ("pid", "flavor", "returned")}


def validate_model(encoded, m, schemas):
    """Required MODEL/step/operation/state fields must exist exactly before any predicate; unavailable evidence is HOLD."""
    if type(encoded) is not dict or set(encoded) != set(schemas["model_fields"]) or set(m) != set(encoded):
        raise Invalid("exact model field set")
    if any(type(encoded.get(k)) is not dict or encoded[k].get("encoding") != "UTF8_HEX" for k in ("stdout", "stderr")):
        raise Invalid("model stdout/stderr require their explicit UTF8_HEX encodings")
    for item in encoded["steps"] if type(encoded["steps"]) is list else [None]:
        error = item.get("exception") if type(item) is dict else None
        if error is not None and (type(error) is not dict or type(error.get("text")) is not dict or
                                  error["text"].get("encoding") != "UTF8_HEX"):
            raise Invalid("exception text must be explicit UTF8_HEX model text")
    if type(m["stdout"]) is not str or type(m["stderr"]) is not str or type(m["disclosures"]) is not list or \
            type(m["open_model_fds"]) is not list or not all(integer(fd) for fd in m["open_model_fds"]) or \
            m["open_model_fds"] != sorted(set(m["open_model_fds"])) or type(m["artifacts"]) is not dict or \
            type(m["inputs"]) is not dict or type(m["config"]) is not dict or type(m["clock_rules"]) is not list or \
            type(m["metadata_transitions"]) is not list:
        raise Invalid("model capture/descriptor/input field types")
    ops = m["operations"]
    if type(ops) is not list or not integer(m["operation_count"]):
        raise Invalid("operation tape type")
    previous = 0
    for op in ops:
        # One model call may retain several records (checkpoint/transition/response), so indices never decrease.
        if type(op) is not dict or not integer(op.get("index"), 1) or op["index"] < previous or \
                type(op.get("operation")) is not str or type(op.get("scope")) is not str:
            raise Invalid("operation index/kind/scope")
        previous, name = op["index"], op["operation"]
        expected_scope = {"posix_spawn": "MODEL_PROCESS_NOT_NATIVE", "killpg": "MODEL_SIGNAL_NOT_NATIVE"}.get(name, "MODEL_INPUT")
        if op["scope"] != expected_scope:
            raise Invalid("operation model scope")
        shape = {"pid", "flavor", "returned", "identity" if op.get("returned") else "model_errno"} if name == "proc_pidinfo" \
            else OP_FIELDS.get(name)
        if shape is None:
            if name not in ("clock_rule", "metadata_transition", "history_checkpoint"):
                raise Invalid("unknown model operation")
        elif set(op) != {"index", "operation", "scope"} | shape:
            raise Invalid("exact operation schema " + name)
        if any(type(op[key]) is not int for key in OP_INTS.get(name, ())) or \
                (name == "waitpid" and (type(op["returned"]) is not list or len(op["returned"]) != 2 or
                                        not all(type(v) is int for v in op["returned"]))) or \
                (name in ("waitpid", "write") and not (number(op["mono_before"]) and number(op["mono_after"]))) or \
                (name == "write" and not hex64(op["sha256"])) or \
                (name == "proc_pidinfo" and op["returned"] and (type(op["identity"]) is not dict or
                                                               len(op["identity"]) != 10)):
            raise Invalid("strict operation field types " + name)
    if previous > m["operation_count"]:
        raise Invalid("operation index beyond model call counter")
    steps = m["steps"]
    if type(steps) is not list or not steps:
        raise Invalid("recorded original steps")
    end, calls = 0, 0
    for item in steps:
        if type(item) is not dict or set(item) != set(schemas["step_fields"]):
            raise Invalid("exact step field set")
        begin, finish, before, after = item["event_begin"], item["event_end"], item["before"], item["after"]
        if not integer(begin) or not integer(finish) or not end <= begin <= finish <= len(ops) or \
                type(before) is not dict or set(before) != {"mono", "history_charge", "calls"} or \
                type(after) is not dict or set(after) != set(before) or not integer(before["calls"]) or \
                not integer(after["calls"]) or not calls <= before["calls"] <= after["calls"] <= m["operation_count"] or \
                not number(before["mono"]) or not number(after["mono"]) or type(item["args"]) is not list:
            raise Invalid("step event range/call window/types")
        # The slice must be exactly the operations recorded during this step; an empty slice is evidence only if valid.
        if any(not before["calls"] < op["index"] <= after["calls"] for op in ops[begin:finish]) or \
                (begin > 0 and ops[begin - 1]["index"] > before["calls"]) or \
                (finish < len(ops) and ops[finish]["index"] <= after["calls"]):
            raise Invalid("step slice is not its complete retained call window")
        count_keys = {"identity_history", "unproved_history", "coverage_history", "attempt_history", "census_history"}
        if any(type(item[k]) is not dict or set(item[k]) != count_keys or
               any(v is not None and not integer(v) for v in item[k].values()) for k in ("counts_before", "counts_after")):
            raise Invalid("exact step retained-history counts")
        error = item["exception"]
        if error is not None and (type(error) is not dict or set(error) != {"type", "code", "text"} or
                                  type(error["type"]) is not str or type(error["code"]) is not str or
                                  type(error["text"]) is not str or item["return"] is not None):
            raise Invalid("exact exception structure")
        end, calls = finish, after["calls"]
    # No hidden post-step work may escape the final negative-work predicates. Only the declared write pipe closes follow.
    tail = ops[steps[-1]["event_end"]:]
    writing = steps[-1]["label"] in ("write_all", "write_progress_before_completion_refusal")
    if (not writing and (tail or steps[-1]["after"]["calls"] != m["operation_count"])) or             (writing and (len(tail) != 2 or any(op["operation"] != "close" for op in tail) or
                          m["operation_count"] != steps[-1]["after"]["calls"] + 2)):
        raise Invalid("work after the final declared step")
    state = m["final_state"]
    if type(state) is not dict or set(state) != FINAL_STATE_KEYS or type(state["helpers"]) is not list or \
            any(type(h) is not dict or set(h) != HELPER_KEYS for h in state["helpers"]) or \
            (state["main_wait"] is not None and (type(state["main_wait"]) is not dict or set(state["main_wait"]) != MAIN_WAIT_KEYS)) or \
            type(state["anchor_fds"]) is not dict or set(state["anchor_fds"]) != {"lane", "tmp", "roots"} or \
            type(state["anchor_fds"]["roots"]) is not list or type(state["failures"]) is not list or \
            type(state["trips"]) is not dict or type(state["raw_acquisitions"]) is not list:
        raise Invalid("exact final_state field set")


def signal_joins(ops, s, require):
    """Decode and join every terminal wait; join every killpg one-to-one to a fresh fingerprint-checked witness."""
    main = s["main_wait"]
    helpers = {h["pid"]: h for h in s["helpers"]}
    for wait in (x for x in ops if x["operation"] == "waitpid"):
        got = wait["returned"]
        if got[0] == 0:
            require("nonterminal_wait_%d_carries_no_status" % wait["index"], got[1] == 0)
            continue
        status = got[1]
        terminal = os.WIFEXITED(status) or os.WIFSIGNALED(status)
        rc = os.waitstatus_to_exitcode(status) if terminal else None
        record = main if main is not None and wait["pid"] == main["pid"] else helpers.get(wait["pid"])
        require("terminal_wait_%d_decoded_and_joined_to_retained_state" % wait["index"], terminal and got[0] == wait["pid"] and
                record is not None and same(record["native_wait_result"], got) and record["raw_wait_status"] == status and
                record["leader_reaped"] is True and record["rc"] == rc and (record is not main or s["rc"] == rc))
    witnesses = []
    if s["signal"] is not None:
        witnesses.append((s["signal"], s["ident"], s["pid"], s["group"]))
    for h in s["helpers"]:
        if h["signal"] is not None:
            witnesses.append((h["signal"], h["identity"], h["pid"], None if h["identity"] is None else h["identity"]["pgid"]))
    for n, (sig, original, _, _) in enumerate(witnesses):
        observed = sig.get("identity_observed")
        if "identity_ok" in sig and observed is not None and original is not None:
            require("signal_witness_%d_identity_ok_recomputed_not_trusted" % n,
                    sig["identity_ok"] is (fingerprint(observed) == fingerprint(original)))
    sent = [w for w in witnesses if w[0].get("sent") is True]
    kills = [x for x in ops if x["operation"] == "killpg"]
    require("killpg_one_to_one_with_sent_signal_witnesses", len(kills) == len(sent) and len({k["pgid"] for k in kills}) == len(kills))
    for kill in kills:
        match = [w for w in sent if w[3] == kill["pgid"]]
        ok = len(match) == 1
        if ok:
            sig, original, pid, group = match[0]
            observed = sig.get("identity_observed")
            fresh = [x for x in ops if x["operation"] == "proc_pidinfo" and x["index"] < kill["index"]][-5:]
            timing = [sig.get("mono_check"), sig.get("mono_identity_begin"), sig.get("mono_identity_observed"), sig.get("mono_sent")]
            reaped = [x for x in ops if x["operation"] == "waitpid" and x["pid"] == pid and x["returned"][0] != 0 and
                      fresh and fresh[0]["index"] <= x["index"] < kill["index"]]
            ok = type(original) is dict and type(observed) is dict and fingerprint(observed) == fingerprint(original) and \
                sig.get("identity_ok") is True and group == original["pgid"] == observed["pgid"] == kill["pgid"] and \
                len(fresh) == 5 and [x["flavor"] for x in fresh] == [17, 13, 17, 13, 17] and \
                [x["returned"] for x in fresh] == [56, 64, 56, 64, 56] and \
                all(x["pid"] == pid and fingerprint(x["identity"]) == fingerprint(observed) for x in fresh) and not reaped and \
                (all(number(t) for t in timing) and timing == sorted(timing) or s["timing_failed"] is True)
        require("killpg_%d_joined_to_fresh_checked_identity_group_and_send_chronology" % kill["index"], ok)


def overflow_proof(s, kind, witness, completed=None):
    """A cap refusal needs its substantive retained witness and exactly one matching failure latch."""
    overflow = s["history_overflow"]
    if type(overflow) is not dict or not {"kind", "mono", "witness"} <= set(overflow) or overflow["witness"] is None or             (completed is not None and "completed_identity_observation" not in overflow):
        raise Invalid("required substantive cap-overflow evidence unavailable")
    rows = [row for row in s["failures"] if row["code"] == kind]
    return s["history_halted"] is True and type(overflow) is dict and overflow.get("kind") == kind and \
        same(overflow.get("witness"), witness) and number(overflow.get("mono")) and len(rows) == 1 and \
        type(rows[0]["detail"]) is str and kind in s["failure_codes"] and \
        (completed is None or same(overflow.get("completed_identity_observation"), completed))


def attempted_witness(family, last, s):
    """Exact attempted observation of the selected count-cap step, joined to its recorded original call arguments."""
    args = last["args"]
    if family in ("identity", "unproved", "variants"):
        if last["label"] != "retain_identity" or len(args) != 4 or args[1] != "MODEL_TARGET" or type(args[0]) is not dict or \
                type(args[3]) is not list or len(args[3]) != 2:
            raise Invalid("count-cap identity attempt arguments")
        observed = {"identity": args[0], "mono_begin": args[3][0], "mono_end": args[3][1], "source": args[1]}
        return observed, observed
    if family == "coverage":
        if last["label"] != "retain_coverage" or len(args) != 2 or type(args[0]) is not list or len(args[0]) != 1:
            raise Invalid("count-cap coverage attempt arguments")
        return {"observation": args[0][0]}, None
    if family == "attempt":
        if last["label"] != "observation_attempt" or args != []:
            raise Invalid("count-cap attempt arguments")
        return {"kind": "MODEL_TARGET"}, None
    if family == "census":
        if last["label"] != "census" or len(args) != 1:
            raise Invalid("count-cap census arguments")
        return {"phase": s["phase"]}, None
    raise Invalid("fixed count-cap family")


def settled_proof(h, m, s):
    """Independently join identity, reap, census group/descendant closure and the stdout byte/EOF/close tape."""
    proof, ident, ops = h["proof"], h["identity"], m["operations"]
    if type(proof) is not dict or type(ident) is not dict:
        raise Invalid("required helper identity/settlement proof unavailable")
    censuses = [c for c in entries(s, "census_history") if same(proof, {key: c[key] for key in
                ("complete", "incomplete_n", "owned_live", "unproved_live", "mono_complete")})]
    spawns = [x for x in ops if x["operation"] == "posix_spawn" and x["pid"] == h["pid"] and x["helper"] is True]
    pipes = [x for x in ops if x["operation"] == "pipe" and len(spawns) == 1 and x["index"] < spawns[0]["index"]]
    if not censuses or len(spawns) != 1 or not pipes:
        raise Invalid("required helper census/spawn/stdout descriptor proof unavailable")
    pipe = pipes[-1]
    reads = [x for x in ops if x["operation"] == "read" and x["fd"] == pipe["read_fd"] and x["index"] > spawns[0]["index"]]
    closes = [x for x in ops if x["operation"] == "close" and x["fd"] == pipe["read_fd"]]
    if not reads or not closes:
        raise Invalid("required helper stdout EOF/close evidence unavailable")
    raw, offset = bytes.fromhex(h["capture_hex"]), 0
    for read in reads:
        n = read["returned"]
        if not integer(n) or not integer(read["requested"]) or n > read["requested"] or offset + n > len(raw) or \
                read["sha256"] != hashlib.sha256(raw[offset:offset + n]).hexdigest():
            return False
        offset += n
    owned = {row["identity"]["uniqueid"]: row for row in s["owned"]}
    group_clear = not any(p["pgid"] == ident["pgid"] for p in proof["owned_live"])
    descendants_clear = not any(p["uniqueid"] not in owned or owned[p["uniqueid"]]["root"] == ident["uniqueid"]
                                for p in proof["owned_live"])
    stdout_closed = len(reads) >= 1 and reads[-1]["returned"] == 0 and offset == len(raw) and len(closes) == 1 and \
        closes[0]["index"] > reads[-1]["index"] and pipe["read_fd"] not in m["open_model_fds"]
    return h["settled"] is True and s["timing_failed"] is False and h["initial_identity_valid"] is True and \
        ident["pid"] == h["pid"] == ident["pgid"] and ident["euid"] == ident["ruid"] == 501 and \
        integer(h["identity_event_ref"], 1) and h["leader_reaped"] is True and h["rc"] == 0 and h["wait_lost"] is False and \
        h["group_clear"] is group_clear is True and h["descendants_clear"] is descendants_clear is True and \
        h["coverage_complete"] is True and proof["complete"] is True and proof["incomplete_n"] == 0 and \
        proof["owned_live"] == [] and proof["unproved_live"] == [] and h["eof_proved"] is True and \
        h["stdout_closed"] is stdout_closed is True and h["clock_failed"] is False


def write_prefix(writes, data, fd):
    """Independent byte-prefix conservation over API-response writes; returns the conserved length or None."""
    offset = 0
    for write in writes:
        count = write["returned"]
        if write["fd"] != fd or type(count) is not int or type(write["requested"]) is not int or \
                not 0 <= count <= write["requested"] or write["requested"] != len(data) - offset or \
                write["sha256"] != hashlib.sha256(data[offset:offset + count]).hexdigest() or \
                write["response_scope"] != "API_RESPONSE_INJECTION":
            return None
        offset += count
    return offset


def entries(state, name):
    value = state["histories"][name]
    if value["omitted"] != 0:
        raise Invalid("full observations required outside count prestate isolation")
    return value["entries"]


def observation_state(model):
    state = model["final_state"]
    if state["history_halted"] and state["history_overflow"] is None:
        raise Invalid("halted history without raw overflow")
    if sorted(state["failure_codes"]) != sorted(x["code"] for x in state["failures"]):
        raise Invalid("failure latch correspondence")
    return state


def verify_model_telemetry(case, model, state, cfg):
    """Reconstruct v19 canonical events and pending failure evidence; never replay source/driver."""
    isolated = case.startswith(("st_cap_identity_", "st_cap_unproved_", "st_cap_coverage_",
                                "st_cap_attempt_", "st_cap_census_", "st_cap_variants_"))
    if isolated:
        if not model["disclosures"] and not case.startswith("st_cap_variants_"):
            raise Invalid("count-isolation reachability declaration missing")
        # Canonical event rows remain available even when large MODEL ledgers are count-only snapshots.
        counts = {}
        for row in state["identity_events"]:
            if type(row) is not list or len(row) != 6 or not all(integer(v) for v in row[:3]) or \
                    not number(row[3]) or not number(row[4]) or row[3] > row[4] or type(row[5]) is not bool:
                raise Invalid("count-isolation event row type/interval")
            counts[row[0]] = counts.get(row[0], 0) + 1
        for ledger in state["histories"]["identity_history"]["entries"]:
            if ledger["observations"] != counts.get(ledger["first_identity"]["uniqueid"], 0):
                raise Invalid("visible isolated ledger observations/event-count mismatch")
        return {"event_replay_scope": "COUNT_PRESTATE_ISOLATION_NOT_PHYSICAL_COVERAGE",
                "event_rows_counted": len(state["identity_events"]),
                "unverified": "Omitted ledger entries and deliberately reset cross-ledger references; no complete physical history claim"}
    ledgers = entries(state, "identity_history")
    by_uid = {entry["first_identity"]["uniqueid"]: entry for entry in ledgers}
    if len(by_uid) != len(ledgers) or any(type(row) is not dict or set(row) != LEDGER_KEYS for row in ledgers):
        raise Invalid("duplicate or malformed identity ledger")
    tape = state["identity_events"]
    acquired, per_uid = {}, {}
    for ref, row in enumerate(tape, 1):
        if type(row) is not list or len(row) != 6:
            raise Invalid("identity event row")
        uid, variant, status, begin, end, unproved = row
        if not integer(uid) or not integer(variant) or not integer(status) or type(unproved) is not bool or \
                not number(begin) or not number(end) or begin > end or uid not in by_uid or variant >= len(by_uid[uid]["variants"]):
            raise Invalid("identity event type/interval/variant")
        identity = dict(by_uid[uid]["variants"][variant], status=status)
        if identity["uniqueid"] != uid:
            raise Invalid("identity event UID binding")
        acquired[ref] = identity
        per_uid.setdefault(uid, []).append((ref, begin, end, identity, unproved))
    for uid, ledger in by_uid.items():
        rows = per_uid.get(uid, [])
        if not rows or ledger["observations"] != len(rows):
            raise Invalid("observations must equal committed acquisition-event count")
        first = min(rows, key=lambda r: r[2])
        last = max(rows, key=lambda r: (r[2], r[0]))
        if (ledger["first_event_ref"], ledger["last_event_ref"]) != (first[0], last[0]) or \
                ledger["first_identity"] != first[3] or ledger["last_identity"] != last[3] or \
                (ledger["mono_first_begin"], ledger["mono_first_seen"]) != (first[1], first[2]) or \
                (ledger["mono_last_begin"], ledger["mono_last_seen"]) != (last[1], last[2]):
            raise Invalid("ledger first/last actual interval reconstruction")
    unknowns = entries(state, "unproved_history")
    if any(type(row) is not dict or set(row) != UNPROVED_KEYS for row in unknowns):
        raise Invalid("exact original v19 unproved ledger fields (no invented count field)")
    unknown_by_uid = {row["first_identity"]["uniqueid"]: row for row in unknowns}
    marked = {uid: [row for row in rows if row[4]] for uid, rows in per_uid.items() if any(row[4] for row in rows)}
    # v19 unproved ledgers have no observations field: counts are the exact marked-row multiplicities.
    if len(unknown_by_uid) != len(unknowns) or set(unknown_by_uid) != set(marked):
        raise Invalid("bidirectional unproved event/ledger correspondence")
    for uid, ledger in unknown_by_uid.items():
        rows = marked[uid]
        first = min(rows, key=lambda r: r[2])
        last = max(rows, key=lambda r: (r[2], r[0]))
        if (ledger["first_event_ref"], ledger["last_event_ref"]) != (first[0], last[0]) or \
                not same(ledger["first_identity"], first[3]) or not same(ledger["last_identity"], last[3]) or \
                (ledger["mono_first_begin"], ledger["mono_first_seen"]) != (first[1], first[2]) or \
                (ledger["mono_last_begin"], ledger["mono_last_seen"]) != (last[1], last[2]):
            raise Invalid("complete unproved count/ref/identity/interval reconstruction")
    for owned in state["owned"]:
        if acquired.get(owned["identity_event_ref"]) != owned["identity"]:
            raise Invalid("rooted owned identity acquisition binding")
    for census in entries(state, "census_history"):
        for role in ("owned", "unproved"):
            identities, refs = census[role + "_live"], census[role + "_event_refs"]
            if len(identities) != len(refs) or any(acquired.get(ref) != identity for ref, identity in zip(refs, identities)):
                raise Invalid("census full identity/reference join")
        for measured in census["measurements"]:
            before = acquired.get(measured["before_task_event_ref"])
            if acquired.get(measured["identity_event_ref"]) != measured["identity"] or before is None:
                raise Invalid("measurement pre-bracket actual identity reference")
            fields = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
            if any(before[k] != measured["identity"][k] or before[k] != measured["identity_after"][k] for k in fields):
                raise Invalid("measurement complete applicable fingerprint")
            after_begin, after_end = measured["identity_after_interval"]
            before_event = tape[measured["before_task_event_ref"] - 1]
            times = [before_event[4], measured["mono_task_begin"], measured["mono_task_end"],
                     after_begin, after_end, measured["mono_observed"]]
            if any(value is None for value in times):
                if not state["timing_failed"] or measured["busy"] is not None:
                    raise Invalid("missing interval cannot qualify BUSY or healthy timing")
            elif times != sorted(times):
                raise Invalid("measurement actual acquisition/task interval ordering")
            after_ref = measured["identity_after_event_ref"]
            if after_ref is None:
                if state["history_halted"]:
                    overflow = state["history_overflow"]
                    if overflow["completed_measurement"] != measured:
                        raise Invalid("null cap reference requires completed bounded composite")
                    observed = overflow["completed_identity_observation"]
                    if observed["identity"] != measured["identity_after"] or \
                            [observed["mono_begin"], observed["mono_end"]] != measured["identity_after_interval"]:
                        raise Invalid("completed cap observation interval/identity loss")
                elif not state["timing_failed"] or not any(raw.get("identity") == measured["identity_after"] and
                        [raw["mono_begin"], raw["mono_end"]] == measured["identity_after_interval"]
                        for raw in state["raw_acquisitions"] if raw["kind"] == "identity" and raw["native_returned"]):
                    raise Invalid("null timing reference requires retained original raw acquisition")
            elif acquired.get(after_ref) != measured["identity_after"] or \
                    tape[after_ref - 1][3:5] != measured["identity_after_interval"]:
                raise Invalid("measurement actual final acquisition reference")
    for helper in state["helpers"]:
        if helper["identity"] is not None and acquired.get(helper["identity_event_ref"]) != helper["identity"]:
            if not (state["timing_failed"] or state["history_halted"]) or not any(
                    raw["kind"] == "identity" and raw["native_returned"] and raw["identity"] == helper["identity"]
                    for raw in state["raw_acquisitions"]):
                raise Invalid("helper actual initial acquisition")
        deadline = helper["call_deadline"]
        end = deadline["mono_created"] + deadline["seconds"]
        if deadline["until"] is not None:
            end = min(end, deadline["until"])
        if end != deadline["end"] or end != helper["mono_call_deadline"] or \
                deadline["seconds"] != cfg["helper_budget"]["call_budget_s"] or \
                not helper["mono_call_start"] <= deadline["mono_created"] <= helper["mono_spawn"] <= helper["mono_pid_registered"]:
            raise Invalid("helper call deadline/spawn/registration provenance")
    signals = [state["signal"]] + [h.get("signal") for h in state["helpers"]]
    for record in signals:
        if record is None or "identity_observed" not in record:
            continue
        timing = [record["mono_check"], record.get("mono_identity_begin"), record.get("mono_identity_observed")]
        if any(value is None for value in timing):
            if not state["timing_failed"]:
                raise Invalid("raw signal null timing without sticky failure")
        elif timing != sorted(timing):
            raise Invalid("raw signal acquisition interval")
        if record["sent"] and record.get("mono_sent") is not None and record.get("mono_identity_observed") is not None and \
                record["mono_sent"] < record["mono_identity_observed"]:
            raise Invalid("signal before fresh acquisition")
        ref = record["identity_event_ref"]
        if ref is None:
            if not (state["history_halted"] or state["timing_failed"]):
                raise Invalid("signal event loss without incomplete/HOLD boundary")
        elif acquired.get(ref) != record["identity_observed"]:
            raise Invalid("signal full acquired identity ref")
    accounting = state["accounting_observations"]
    for index, event in enumerate(accounting, 1):
        if event["id"] != index or event["retained"] is not True or type(event["returned"]) is not bool or \
                set(event["resources"]) != {"charged_bytes", "lane_bytes", "free"}:
            raise Invalid("actual complete accounting event schema")
        if event["mono_observed"] is None:
            if not state["timing_failed"] or event["returned"] is not False:
                raise Invalid("missing accounting time cannot qualify caller return")
        elif event["mono_begin"] > event["mono_observed"]:
            raise Invalid("actual accounting chronology")
    if accounting:
        minimum = min(event["resources"]["free"] for event in accounting)
        witness = next(event for event in accounting if event["resources"]["free"] == minimum)
        if state["min_free"] != minimum or state["min_free_witness"] != witness or \
                state["last_accounting_observation"] != accounting[-1]:
            raise Invalid("minimum/last accounting actual witness")
    elif state["min_free"] is not None or state["min_free_witness"] is not None:
        raise Invalid("invented accounting witness")
    raw_ids = [raw["id"] for raw in state["raw_acquisitions"]]
    if len(raw_ids) != len(set(raw_ids)) or len(raw_ids) > 128:
        raise Invalid("pending raw acquisition bounded identity")
    for raw in state["raw_acquisitions"]:
        if raw["kind"] not in ("identity", "task") or type(raw["native_returned"]) is not bool:
            raise Invalid("raw acquisition exact kind/return state")
        if raw["native_returned"] and raw["kind"] == "identity" and raw["identity"] is None:
            raise Invalid("returned native identity discarded")
    initial = state["rec"]["initial_fit"]
    chunk = initial["start_epoch"] + cfg["max_chunk_seconds"] - 120
    owned = cfg["owned_compute_settled_by_epoch"] - 180
    fit = min(chunk, owned)
    if initial["chunk_epoch_bound"] != chunk or initial["owned_epoch_bound"] != owned or initial["fit_epoch"] != fit or \
            initial["fit_mono"] != initial["start_mono"] + fit - initial["start_epoch"]:
        raise Invalid("original initial-fit formula")
    return {"event_replay_scope": "FULL_RETAINED_MODEL_TAPE", "events": len(tape), "accounting": len(accounting)}


def evaluate_added(case, m, s, cfg, require, spec):
    """Separate raw predicates bound to the selected compact case; no driver import, source execution, pass bit or release."""
    i, steps, ops = m["inputs"], m["steps"], m["operations"]
    fix, exp = expectation(spec, case)
    if spec.get("contract_ref") != "added_case_common" or type(exp.get("predicate")) is not str:
        raise Invalid("compact selected case contract")
    last = steps[-1]
    waits = [x for x in ops if x["operation"] == "waitpid"]
    main_waits = [x for x in waits if x["pid"] == 700000010]
    kills = [x for x in ops if x["operation"] == "killpg"]
    fingerprints = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
    raw = s["raw_acquisitions"]
    handled = {"predicate"}  # Prose predicate is enforced only through the branch predicates below.

    def expect(key, condition):
        handled.add(key)
        require("selected_expected_" + key, condition)
    generic = {
        "exception": lambda v: outcome_is(last, v),
        "first_exception": lambda v: outcome_is(steps[0], v),
        "second_exception": lambda v: len(steps) > 1 and outcome_is(steps[1], v),
        "step_codes": lambda v: type(v) is list and len(v) == len(steps) and all(outcome_is(x, c) for x, c in zip(steps, v)),
        "failure_codes": lambda v: type(v) is list and sorted(s["failure_codes"]) == sorted(v),
        "failures": lambda v: same(s["failures"], v),
        "TERM": lambda v: integer(v) and len(kills) == v,
        "source_return": lambda v: succeeded(last) and type(last["return"]) is int and last["return"] == v,
        "rc": lambda v: same(s["rc"], v),
        "main_wait_count": lambda v: integer(v) and len(main_waits) == v,
        "main_wait_results": lambda v: same([x["returned"] for x in main_waits], v),
        "waits": lambda v: integer(v) and len(waits) == v,
        "ident": lambda v: same(s["ident"], v),
        "exit_mono": lambda v: same(s["exit_mono"], v),
        "history_halted": lambda v: s["history_halted"] is v,
        "publication_resources": lambda v: same(s["publication_resources"], v),
        "ack_resources": lambda v: same(s["ack_resources"], v)}
    for key, check in generic.items():
        if key in exp:
            expect(key, check(exp[key]))
    if case.startswith("st_complete_"):
        phase = fix["phase"]
        boundary = table({"authorization.not_after_epoch": "auth", "fit": "fit", "stability_expiry_mono": "stability"}, fix["boundary"])
        delta = fix["delta_s"]
        _, _, named_phase, named_boundary, _ = case.split("_")
        require("case_binds_exact_phase_and_cutoff", phase == named_phase.upper() == i["phase"] and boundary == named_boundary == i["boundary"] and
                i["delta"] == delta and last["label"] == "protected_" + phase + "_completion" and last["args"][0] == phase and
                (boundary != "fit" or fix["owned_compute_settled_by_epoch"] == cfg["owned_compute_settled_by_epoch"]))
        rules = m["clock_rules"]
        epoch = next(r["returned"] for r in rules if r["clock"] == "time")
        mono = next(r["returned"] for r in rules if r["clock"] == "monotonic")
        auth, obs = i["authorization"], i["observation"]
        base = obs["epoch_date_floor"] - auth["stability_epoch"]
        upper = max(base + 1.0 + max(0.0, mono - obs["mono_before_read"]),
                    i["max_age"] + mono - i["stability_expiry"])
        expected = ("AUTHORIZATION_EXPIRED_DURING_" + phase if epoch > auth["not_after_epoch"] else
                    "FIT_EXPIRED_DURING_" + phase if epoch > i["fit_epoch"] or mono > i["fit_mono"] else
                    "STABILITY_STALE" if upper > i["max_age"] else None)
        required = {"auth": "AUTHORIZATION_EXPIRED_DURING_" + phase,
                    "fit": "FIT_EXPIRED_DURING_" + phase, "stability": "STABILITY_STALE"}[boundary] if delta > 0 else None
        observed = epoch if boundary == "auth" else mono
        cutoff = auth["not_after_epoch"] if boundary == "auth" else i["fit_mono"] if boundary == "fit" else i["stability_expiry"]
        require("protected_completion_exact_source_predicate", expected == required == exp["exception"] and last["return"] is None)
        require("declared_cutoff_not_requested_delay", observed == i["target"] and
                near(observed - cutoff, delta) and (delta != 0 or observed == cutoff))
        if delta == 0 and boundary == "stability":
            require("stability_equality_exact_upper_not_approximate", upper == i["max_age"] == 300.0)
        if boundary == "fit":
            require("fit_epoch_and_mono_both_reached", near(epoch - i["fit_epoch"], delta) and
                    near(mono - i["fit_mono"], delta) and (delta != 0 or epoch == i["fit_epoch"] and mono == i["fit_mono"]))
        require("completion_bound_to_retained_authority_and_initial_fit", auth == s["authorization"] and
                obs == s["clock_observation"] and i["stability_expiry"] == s["stability_expiry_mono"] and
                i["fit_epoch"] == s["rec"]["initial_fit"]["fit_epoch"] and i["fit_mono"] == s["rec"]["initial_fit"]["fit_mono"])
        require("protected_signal_mask_and_exact_paired_read", len(rules) == 2 and
                [r["clock"] for r in rules] == ["time", "monotonic"] and len([x for x in ops if x["operation"] == "sigmask"]) == 2)
        require("predicate_not_caller_or_native_commit_claim", not kills and s["failure_codes"] == [] and s["trips"] == {} and
                s["ack_output_started"] is False and s["rec"].get("go_delivered") is not True)
        if phase == "GO":
            go = s["rec"]["go_delivery_completion"]
            require("GO_age_gate_before_final_clock_pair", go["mono"] == i["initial_mono"] and
                    go["spawn_age_s"] <= go["spawn_age_bound_s"] and go["remaining_main_runtime_s"] > 0)
    elif case.startswith("st_ident_signal_"):
        before, after, field, sig = i["before"], i["after"], fix["field"], s["signal"]
        require("fixed_identity_transition_from_selected_case", field == case.rsplit("_", 1)[1] == i["field"] and
                same(i["value"], fix["new_value"]) and same(after[field], fix["new_value"]) and before["pid"] == 700000010 and
                same(before, s["ident"]))
        require("changed_full_fingerprint_refuses_TERM", [k for k in fingerprints if before[k] != after[k]] == [field] and
                same(sig["identity_observed"], after) and sig["identity_ok"] is False and sig["sent"] is False and not kills)
        require("fresh_signal_witness_and_conservative_failure", integer(sig["identity_event_ref"], 1) and
                s["stop"]["reason"] == "MODEL_STOP_REQUEST" and "identity mismatch" in sig["error"])
    elif case.startswith("st_ident_read_"):
        transitions = m["metadata_transitions"]
        transition = transitions[0] if len(transitions) == 1 else {}
        cs = [c for c in entries(s, "census_history") if not c["inside_helper"] and c["phase"] == "RUNNING"]
        field, value = fix["field"], fix["new_value"]
        require("fixed_read_transition_from_selected_case", field == case.rsplit("_", 1)[1] == i["field"] and
                same(i["value"], value) and transition.get("source") == fix["source"] == "pid_scan" and
                transition.get("pid") == 700000010 and transition.get("after_reads") == fix["after_pidinfo_reads"])
        require("mid_read_full_fingerprint_change_observed", transition.get("field") == field and
                transition.get("fired") is True and same(transition["after"][field], value))
        require("read_inconsistency_is_failed_coverage_not_absence", len(cs) == 2 and
                not cs[0]["complete"] and cs[0]["incomplete_n"] == 1 and cs[1]["complete"])
        error = exp.get("first_coverage_error")
        expect("first_coverage_error", error == ("IDENTITY_CHANGED" if field in ("uniqueid", "idversion") else "IDENTITY_METADATA_CHANGED") and
               any(row["observation"][0] == 700000010 and error in row["observation"][2] for row in entries(s, "coverage_history")))
        require("persistent_changed_identity_not_restored", not kills)
        if field == "uniqueid":
            require("reused_PID_incarnation_history_survives", any(row["last_identity"]["uniqueid"] == value
                    for row in entries(s, "unproved_history")) and any(row["identity"]["uniqueid"] == value and
                    row["via"] == "owned_group" for row in s["owned"]))
    elif case == "st_ident_bracket_changed":
        c = entries(s, "census_history")[-1]
        measured = c["raw_measurements"][-1]
        transition = m["metadata_transitions"][0] if len(m["metadata_transitions"]) == 1 else {}
        require("fixed_bracket_transition_from_selected_case", fix["field"] == i["field"] == "ppid" and same(i["value"], fix["new_value"]) and
                transition.get("source") == fix["source"] == "measurement_final_bracket" and transition.get("fired") is True and
                transition.get("field") == "ppid")
        require("changed_final_bracket_cannot_qualify_RSS", c["aborted"] and not c["complete"] and
                c["measurements"] == [] and measured["bracket_verified"] is False and
                same(measured["identity_after"]["ppid"], fix["new_value"]) and measured["identity"]["ppid"] == 700000001 and
                measured["busy"] is None)
        expect("lane_rss", c["lane_rss"] == exp["lane_rss"])
        require("returned_task_and_changed_identity_retained", any(r["kind"] == "task" and r["native_returned"] for r in raw) and
                any(r["kind"] == "identity" and r["native_returned"] and r["identity"] == measured["identity_after"] for r in raw) and not kills)
    elif case == "st_ident_mixed_uid_unreadable":
        p = i["mixed_identity"]
        cs = [c for c in entries(s, "census_history") if c["phase"] == "RUNNING"]
        require("mixed_identity_from_selected_case", p["pid"] == fix["pid"] and p["euid"] == fix["euid"] and p["ruid"] == fix["ruid"] and
                i["unreadable_flavor"] == fix["task_flavor"] and i["model_errno"] == fix["errno"])
        require("same_real_UID_attempted_despite_foreign_effective_UID", len([x for x in ops if x["operation"] == "proc_pidinfo" and
                x["pid"] == p["pid"] and x["flavor"] == fix["task_flavor"] and x["returned"] == 0 and
                x["model_errno"] == fix["errno"]]) == 3)
        expect("coverage_complete", exp["coverage_complete"] is False and len(cs) == 3 and
               all(not c["complete"] and c["incomplete_n"] == 1 and p in c["unproved_live"] and
                   all(row["identity"]["pid"] != p["pid"] for row in c["measurements"]) for c in cs) and
               len(entries(s, "coverage_history")) == 3 and not kills)
    elif case == "st_ident_main_initial_invalid":
        require("invalid_initial_credentials_from_selected_case", same(i["spawn_overrides"], {"child": {"euid": fix["MODEL_spawn_euid"]}}) and
                s["rec"]["main_initial_identity_observed"]["euid"] == fix["MODEL_spawn_euid"])
        require("invalid_initial_credentials_cannot_authorize_TERM_or_GO", s["group"] is None and not kills and
                s["signal"]["why_not"] == "NO_IDENTITY" and s["rec"].get("go_delivered") is not True)
        require("invalid_main_remains_explicitly_unsettled", s["loop_status"] == "GRACE_EXPIRED_AFTER_STOP_REQUEST" and
                any(p["pid"] == 700000010 for p in m["live_model_processes"]))
    elif case == "st_ident_helper_signal_changed":
        h = s["helpers"][-1]
        require("helper_change_from_selected_case", fix["helper"] == "fixed MODEL /bin/date held" and
                fix["change"] == "pgid+1 after initial original identity registration" and
                same(i["after"], dict(i["before"], pgid=i["before"]["pgid"] + 1)) and same(h["identity"], i["before"]))
        require("helper_mismatch_refuses_once_only_TERM", all(succeeded(x) for x in steps) and
                h["signal"]["identity_ok"] is False and h["signal"]["sent"] is False and not kills and
                same(h["signal"]["identity_observed"], i["after"]))
        expect("term_attempted", h["term_attempted"] is exp["term_attempted"] is True)
        expect("signal_reason", type(exp["signal_reason"]) is str and exp["signal_reason"] in h["signal"]["reason"])
        expect("settled", h["settled"] is exp["settled"] is False and h["clockless_probe_count"] == 1 and
               not h["leader_reaped"] and len([x for x in waits if x["pid"] == h["pid"]]) == 1)
    elif case.startswith("st_clock_") or case in ("st_acq_main_identity_end_clock", "st_acq_reap_mono_clock"):
        summaries = [decode(line.encode()) for line in m["stdout"].splitlines()]
        require("sticky_clock_failure_never_ACKs_SETTLED_or_exit0", s["timing_failed"] is True and
                last["label"] == "finalize_sticky_timing_HOLD" and len(summaries) == 1 and summaries[0]["acknowledged"] is False and
                summaries[0]["exit_code"] == 13 and summaries[0]["reason"] == "TIMING_EVIDENCE_UNAVAILABLE" and
                s["publication_payload_bytes"] is None and s["publication_resources"] is None and s["ack_resources"] is None and
                not m["artifacts"])
        require("clock_exception_type_not_broadened", any(r["exception_type"] == "ModelClockUnavailable" and
                r["returned"] is None and r["action"] == "raise" for r in m["clock_rules"]) and s["cancellation_target_installed"] is True)
        if case.startswith("st_clock_cancel_"):
            require("cancel_contained_without_unrelated_step_exceptions", all(succeeded(x) for x in steps))
            require("cancel_latched_before_failed_timing", s["cancel"]["mono"] is None and s["cancel"]["signal"] == fix["signal"] and
                    fix["cancel_clock"] == "ModelClockUnavailable" == s["cancel"]["clock_error"])
            if case.endswith("before_target"):
                require("early_cancel_propagates_after_target_installation", fix["target_at_handler"] is None and
                        i["target_at_handler"] is None and steps[0]["label"] == "cancel_before_target")
            else:
                require("installed_cancel_target_immediately_sticky", i["immediate_handler_timing_failed"] is True and
                        fix["cancel_handled_prestate"] is True and s["cancel_handled"] is True)
        elif case == "st_acq_main_identity_end_clock":
            require("main_identity_recovery_returns_true_before_finalize", len(steps) == 2 and succeeded(steps[0]) and steps[0]["return"] is True)
            initial = next((r for r in raw if r["source"] == "main_recovery"), None)
            require("identity_installed_before_failed_end_clock", fix["raise_site"] == "acquire_identity aux_clock mono_end within main recovery" and
                    initial is not None and initial["native_returned"] is True and same(initial["identity"], s["ident"]) and
                    initial["mono_end"] is None and initial["mono_end_error"] == "ModelClockUnavailable" and
                    same(s["rec"]["main_initial_identity_interval"], [initial["mono_begin"], None]) and
                    s["signal"]["sent"] is True and s["signal"]["identity_ok"] is True)
        elif case == "st_acq_reap_mono_clock":
            require("reap_steps_are_contained_null_returns", len(steps) == 4 and all(succeeded(x) and x["return"] is None for x in steps[:2]))
            w = s["main_wait"]
            require("destructive_reap_survives_null_auxiliary_exit_clock", fix["raise_site"] == "reap_record mono_reaped" and
                    len(main_waits) == 1 and near(main_waits[0]["mono_after"], fix["wait_return_mono"]) and
                    w["leader_reaped"] is True and same(w["native_wait_result"], [700000010, 0]) and w["raw_wait_status"] == 0 and
                    w["mono_reaped_error"] == "ModelClockUnavailable" and s["exit_epoch"] is not None and len(steps) == 4 and
                    steps[2]["label"] == "missing_exit_clock_denies_deadline")
            expect("deadline_exception", len(steps) == 4 and raised(steps[2], exp["deadline_exception"]))
        else:
            recovery = case == "st_clock_recovery_post_wait"
            require("runtime_clock_failure_contained_in_original_methods", len(steps) == 3 and all(succeeded(x) for x in steps) and
                    steps[0]["return"] is (True if recovery else None) and steps[1]["return"] is None)
            before = table({"enforce_runtime before_waitpid": True, "after_waitpid_including_success": False}, fix["raise_site"])
            prior = fix.get("prior_stop", False) not in (False, None)
            require("runtime_clock_stimulus_from_selected_case", i["runtime_check"] == ("before_waitpid" if before else "after_waitpid_including_success") and
                    i["recovery"] is recovery and ("registered_record" in fix) is recovery and not s["lost_wait"] and
                    (same(s["stop"], i["prior_stop"]) and s["stop"]["reason"] == fix["prior_stop"] if prior else
                     i["prior_stop"] is None and s["stop"]["reason"] == "FAILURE") and
                    ("wait_return_mono" not in fix or len(main_waits) == 1 and near(main_waits[0]["mono_after"], fix["wait_return_mono"])))
            require("postwait_containment_never_rewaits_consumed_status",
                    all(x["returned"] == [0, 0] for x in main_waits) if s["rc"] is None else
                    s["main_wait"]["leader_reaped"] is True and s["main_wait"]["rc"] == s["rc"])
            row = next((row for row in s["failures"] if row["code"] == "MAIN_RUNTIME_CLOCK_UNAVAILABLE"), None)
            require("runtime_failure_location_retained", row is not None and type(row["detail"]) is str and
                    ("after_waitpid_including_success" in row["detail"]) is (not before) and "ModelClockUnavailable" in row["detail"])
    elif case in ("st_acq_task_end_clock_rss", "st_acq_final_bracket_end_clock_rss"):
        cs = entries(s, "census_history")
        c = cs[-2] if len(cs) >= 2 else None
        measured = c["measurements"][-1] if c is not None and c["measurements"] else None
        require("rss_timing_stimulus_from_selected_case", measured is not None and fix["rss"] == cfg["rss_trip_bytes"] + 1 and
                measured["rss"] == fix["rss"] and s["stop"]["reason"] == fix["prior_stop"] and
                fix["raise_site"] == ("census task mono_end" if case == "st_acq_task_end_clock_rss" else "final-bracket acquisition mono_end"))
        if measured is not None:
            require("completed_RSS_composite_precedes_failed_timing", s["timing_failed"] is True and measured["bracket_verified"] is True and
                    same(measured["identity_after"], measured["identity"]) and measured["rss"] > cfg["rss_trip_bytes"] and
                    measured["identity_after_event_ref"] is None and c["lane_rss"] == sum(row["rss"] for row in c["measurements"]) and
                    "RSS" in s["trips"] and s["maxima"]["lane_rss"] >= c["lane_rss"])
            expect("busy", measured["busy"] is exp["busy"] is None)
            if case == "st_acq_task_end_clock_rss":
                expect("mono_task_end", measured["mono_task_end"] is exp["mono_task_end"] is None)
            else:
                expect("identity_after_interval_end", measured["identity_after_interval"][1] is exp["identity_after_interval_end"] is None)
            require("returned_raw_task_retained", any(r["kind"] == "task" and r["native_returned"] and
                    r["native_result"][0] == measured["rss"] for r in raw))
            require("abort_records_and_sticky_no_scan_resume", c["aborted"] and not c["complete"] and c["mono_end"] is not None and
                    len(steps) == 2 and not any(x["operation"].startswith("proc_") for x in ops[steps[1]["event_begin"]:steps[1]["event_end"]]) and
                    not kills)
    elif case in ("st_acq_accounting_late_return", "st_acq_accounting_observed_clock"):
        events, clock = s["accounting_observations"], case.endswith("_clock")
        event = events[-1] if len(events) == 1 else None
        require("accounting_stimulus_from_selected_case", i["free"] == fix["free"] and
                (fix["raise_site"] == "accounting event mono_observed" if clock else
                 fix["deadline_s"] == 1.0 and near(i["deadline"] + 0.01, fix["clock_at_after_accounting"])))
        require("native_free_retained_before_completion_refusal", event is not None and
                event["resources"]["free"] == i["free"] == s["last_native_free"]["free"] and
                s["min_free"] == i["free"] and same(s["min_free_witness"], event) and same(event, s["last_accounting_observation"]))
        require("exact_accounting_failure_not_success_by_exception", event is not None and
                raised(steps[0], "ACCOUNTING_COMPLETION_TIME_UNAVAILABLE" if clock else "DEADLINE_EXCEEDED") and
                (event["mono_observed"] is None if clock else event["mono_begin"] <= event["mono_observed"] <= i["deadline"] < steps[0]["after"]["mono"]))
        require("accounting_clock_failure_sticky_no_retry", (s["timing_failed"] is True and
                s["failure_codes"] == ["TIMING_EVIDENCE_UNAVAILABLE"] and len(steps) == 2 and
                steps[1]["event_begin"] == steps[1]["event_end"]) if clock else
                (s["timing_failed"] is False and s["failure_codes"] == [] and len(steps) == 1))
        if "retained" in exp:
            expect("retained", event is not None and event["retained"] is exp["retained"] is True)
        expect("returned", event is not None and event["returned"] is exp["returned"] is False)
        if "mono_observed" in exp:
            expect("mono_observed", exp["mono_observed"] is None and event is not None and event["mono_observed"] is None)
    elif case == "st_write_progress_late":
        writes = [x for x in ops if x["operation"] == "write"]
        pipes = [x for x in ops if x["operation"] == "pipe"]
        data = bytes.fromhex(i["data_hex"])
        require("progress_stimulus_from_selected_case", fix["data"] == "fixed MODEL byte string" and fix["deadline_s"] == 1.0 and
                fix["write_response"] == "all bytes, mono_after deadline+0.01" and len(pipes) == 1 and len(writes) == 1 and
                writes[0]["mono_after"] == i["deadline"] + 0.01)
        require("returned_prefix_callback_precedes_deadline_check", len(writes) == 1 and len(pipes) == 1 and
                write_prefix(writes, data, pipes[0]["write_fd"]) == len(data) and
                writes[0]["mono_before"] < i["deadline"] < writes[0]["mono_after"] and
                i["data_hex"] == i["progress_hex"] == i["result_data_hex"])
    elif case.startswith("st_cap_raw_"):
        cap = m["caps"]["raw"]
        desired, pre = i["requested_post_count"], i["pre_count"]
        overflow = pre >= cap["value"]  # Original GtE refusal before another acquisition.
        require("raw_cap_binds_selected_case_and_verified_source_cap", same(i["cap"], cap) and cap["operator"] == "GtE" and
                cap["value"] == fix["cap"] and desired == fix["requested_after"] and pre == fix["pending_before"] == desired - 1 and
                (exp["exception"] == "RAW_ACQUISITION_CAP") is overflow)
        expect("raw_count", exp["raw_count"] == len(raw) == min(desired, cap["value"]) and
               all(r["native_returned"] and r["identity"] is not None for r in raw))
        require("raw_cap_latch_independent_of_history", not s["history_halted"] and (overflow or s["failure_codes"] == []))
        if overflow:
            require("raw_cap_refuses_before_additional_native_model_acquisition",
                    not any(x["operation"].startswith("proc_") for x in ops[last["event_begin"]:last["event_end"]]))
    elif case.startswith("st_cap_clockless_"):
        h, cap, calls = s["helpers"][-1], m["caps"]["clockless"], fix["calls"]
        require("clockless_cap_binds_selected_case_and_verified_source_cap", same(i["cap"], cap) and cap["operator"] == "GtE" and
                cap["value"] == fix["cap"] and i["requested_post_count"] == calls and fix["helper"] == "held MODEL /bin/date" and
                len(steps) == calls and all(succeeded(x) for x in steps))
        expect("probe_count", exp["probe_count"] == h["clockless_probe_count"] == min(calls, cap["value"]))
        expect("wait_count", exp["wait_count"] == len([x for x in waits if x["pid"] == h["pid"]]))
        expect("settled", h["settled"] is exp["settled"] is False and h["leader_reaped"] is False and not kills)
        if calls > cap["value"]:
            require("clockless_cap_no_extra_raw_work", last["event_begin"] == last["event_end"])
    else:
        raise Invalid("added independent raw-state predicate absent")
    if set(exp) != handled:
        raise Invalid("selected compact expectation field not independently enforced")


def evaluate(case, outcome, capture, captures, sources, specs):
    checks = {}

    def require(label, condition):
        checks[label] = bool(condition)
    spec = specs["cases"][case]
    common = specs["added_case_common"]
    exit_expected = common.get("expected_driver_actual_exit") if spec.get("contract_ref") == "added_case_common" else \
        spec["expected"].get("driver_actual_exit") if type(spec.get("expected")) is dict else None
    require("external_actual_driver_exit_exactly_0_never_120", type(exit_expected) is int and type(capture["actual_exit"]) is int and
            capture["actual_exit"] == exit_expected == 0)
    require("full_native_driver_stderr_empty", captures["stderr"]["bytes"] == 0)
    require("driver_does_not_claim_actualexit_or_terminal14", outcome["source_outcome"]["actual_exit"] is None and
            outcome["source_outcome"]["native_supervisor_terminal14_exercised"] is False and
            outcome["source_outcome"]["fixture_identity"] == "MODIFIED_QUALIFICATION_FIXTURE")
    require("native_obligations_remain_open", outcome["unresolved"]["native_coverage"] == "NOT_EXERCISED" and
            outcome["unresolved"]["native_children_created"] == [] and outcome["unresolved"]["release"] is None and
            outcome["unresolved"]["science_acceptance"] is None and outcome["accounting"]["native_payload"] is None)
    observations = outcome["observations"]
    clocks = ("raw_epoch_begin", "authority_validation_epoch", "raw_epoch_end", "runtime_s")
    if type(observations) is not list or len(observations) != 1 or type(observations[0]) is not dict or \
            set(observations[0]) != {"scope", "kind", "rss_peak_bytes", "budget_checks"} | set(clocks) or \
            observations[0]["scope"] != "NATIVE_OBSERVATION" or observations[0]["kind"] != "owner_runtime" or \
            not integer(observations[0]["rss_peak_bytes"]) or not integer(observations[0]["budget_checks"]) or \
            not all(number(observations[0][k]) for k in clocks) or not number(outcome["bindings"]["not_after_epoch"]):
        raise Invalid("exact strict-typed native owner observation")
    native = observations[0]
    if outcome["source_outcome"]["status"] != "RECORDED" or outcome.get("model") is None:
        return checks, "NOT_EXERCISED" if outcome["source_outcome"]["status"] == "NOT_EXERCISED" else "HOLD"
    encoded = outcome["model"]
    original = verify_source(encoded, sources["supervisor"])
    m = restore(encoded)
    validate_model(encoded, m, specs["schemas"]["outcome"])
    i, s, steps, ops = m["inputs"], observation_state(m), m["steps"], m["operations"]
    cfg = m["config"]
    constants = original["constants"]
    require("declared_model_scope_no_backend_escape", m["scope"] == "MODEL_INPUT_NOT_NATIVE" and m["violations"] == [])
    require("native_cooperative_budget", outcome["owner"]["mono_end"] - outcome["owner"]["mono_begin"] <= 280 and
            native["rss_peak_bytes"] <= 256 << 20)
    require("native_authority_actual_validation_epoch", native["raw_epoch_begin"] <= native["authority_validation_epoch"] <=
            native["raw_epoch_end"] <= outcome["bindings"]["not_after_epoch"] and
            0 <= outcome["bindings"]["not_after_epoch"] - native["authority_validation_epoch"] <= 300)
    require("fixed_case_model_config", cfg["max_wall_s"] == (200.0 if case.startswith("st_go_w200_") else 10.0) and
            cfg["sample_s"] == 0.2 and cfg["settle_s"] == 0.5 and cfg["rss_trip_bytes"] == 1048576 and
            cfg["busy_limit"] == 1 and cfg["cpu_slots"] == 1 and cfg["admission"]["stability_max_age_s"] == 300.0 and
            cfg["output_trip_bytes"] == 1048576 and cfg["free_trip_bytes"] == 12000000000)
    require("original_fit_config_not_a_scalar_override", cfg["owned_compute_settled_by_epoch"] ==
            1700000000.0 + (220.0 if case.startswith(("st_complete_go_fit_", "st_complete_ack_fit_")) else 20000))
    virtual = m["virtual_authority"]
    digest = hashlib.sha256(canon(cfg)).hexdigest()
    bound_keys = ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel", "reservation_bytes",
                  "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")
    expected_go_entry = {key: cfg[key] for key in bound_keys[:5]}
    expected_go_entry.update({key: cfg["admission"][key] for key in bound_keys[5:]})
    require("virtual_auth_is_only_bound_MODEL_bytes", virtual["scope"] == "MODEL_AUTHORIZATION_BYTES_NOT_AUTHORITY" and
            virtual["config_sha256"] == digest and same(virtual["config"], cfg) and
            same(virtual["go"]["configs"], {digest: expected_go_entry}) and
            virtual["go"]["stability_receipt_sha256"] == hashlib.sha256(canon(virtual["stability"])).hexdigest())
    replay = verify_model_telemetry(case, m, s, cfg)
    require("original_raw_telemetry_reconstructed", replay["event_replay_scope"] in
            ("FULL_RETAINED_MODEL_TAPE", "COUNT_PRESTATE_ISOLATION_NOT_PHYSICAL_COVERAGE"))
    require("model_process_signal_whitelist", all(x["signal"] == int(signal.SIGTERM) and x["scope"] == "MODEL_SIGNAL_NOT_NATIVE"
                                                  for x in ops if x["operation"] == "killpg"))
    require("model_wait_is_WNOHANG", all(x["flags"] == os.WNOHANG for x in ops if x["operation"] == "waitpid"))
    require("all_clock_rules_hit_exact_declared_site", all(r["fired"] is True for r in m["clock_rules"]))
    if any(r["fired"] is not True for r in m["clock_rules"] + m["metadata_transitions"]):
        return checks, "NOT_EXERCISED"
    waits, kills = [x for x in ops if x["operation"] == "waitpid"], [x for x in ops if x["operation"] == "killpg"]
    consumed = set()
    for wait in waits:
        require("wait_once_after_terminal_%d" % wait["index"], wait["pid"] not in consumed)
        if wait["returned"][0] and (os.WIFEXITED(wait["returned"][1]) or os.WIFSIGNALED(wait["returned"][1])):
            consumed.add(wait["pid"])
    require("once_only_TERM_per_model_group", len([x["pgid"] for x in kills]) == len(set(x["pgid"] for x in kills)))
    signal_joins(ops, s, require)
    require("model_stderr_empty_no_finalization_or_post_ack_diagnostic", m["stderr"] == "")
    require("model_artifact_bytes_explicitly_not_actual_date", all(
            a["scope"] == "MODEL_INPUT_NOT_ACTUAL_BIN_DATE" and a["artifact_scope"] == "MODEL_ARTIFACT_NOT_NATIVE" and
            hashlib.sha256(bytes.fromhex(a["data_hex"])).hexdigest() == a["sha256"]
            for a in m["artifacts"].values()))
    if case.startswith(("st_complete_", "st_ident_", "st_clock_", "st_acq_", "st_cap_raw_", "st_cap_clockless_")) or case == "st_write_progress_late":
        evaluate_added(case, m, s, cfg, require, spec)
        return checks, None
    fix, exp = expectation(spec, case)
    handled = set()

    def expect(key, condition):
        handled.add(key)
        require("selected_expected_" + key, condition)
    last = steps[-1]
    if case.startswith("st_runtime_"):
        mains = [x for x in waits if x["pid"] == s["pid"]]
        require("runtime_inputs_bind_selected_case_and_model_state", s["pid"] == 700000010 and
                i["mono_spawn"] == s["mono_spawn"] == fix["mono_spawn"] and i["max_wall_s"] == cfg["max_wall_s"] == fix["max_wall_s"] and
                i["sample_s"] == cfg["sample_s"] == fix["sample_s"] and i["wait_status"] == fix["wait_status"] and
                near(i["wait_enter_mono"], fix["model_wait_enter"]) and near(i["wait_return_mono"], fix["model_wait_return"]))
        require("single_successful_model_wait_raw_order", len(mains) == 1 and same(mains[0]["returned"], [s["pid"], fix["wait_status"]]) and
                mains[0]["mono_before"] == i["wait_enter_mono"] and mains[0]["mono_after"] == i["wait_return_mono"] and
                last["label"] == "reap" and len(steps) == 1)
        if len(mains) == 1:
            reaped = mains[0]["mono_after"]  # Every runtime decision derives from this recorded wait completion.
            deadline = s["mono_spawn"] + cfg["max_wall_s"]
            trip = reaped >= deadline
            late = reaped > deadline + cfg["sample_s"] + 0.05
            require("recorded_wait_completion_joined_to_exit_and_reap_state", s["exit_mono"] == reaped and
                    s["main_wait"]["mono_reaped"] == reaped and mains[0]["mono_before"] < deadline and not s["lost_wait"])
            require("runtime_observation_is_the_recorded_wait_completion", same(s["runtime_observations"],
                    [{"where": "after_waitpid_including_success", "mono": reaped, "mono_deadline": deadline}] if trip else []))
            expect("trips", type(exp["trips"]) is list and sorted(s["trips"]) == sorted(exp["trips"]) and ("DEADLINE" in exp["trips"]) is trip)
            expect("failure_codes", type(exp["failure_codes"]) is list and sorted(s["failure_codes"]) == sorted(exp["failure_codes"]) and
                   ("MAIN_DEADLINE_ENFORCEMENT_LATE" in exp["failure_codes"]) is late)
        expect("rc", same(s["rc"], exp["rc"]) and same(s["main_wait"]["rc"], exp["rc"]))
        expect("signal", (s["signal"] is None and not kills) if exp["signal"] is None else
               (type(s["signal"]) is dict and s["signal"].get("why_not") == exp["signal"] and s["signal"]["sent"] is False and not kills))
        expect("exception", outcome_is(last, exp["exception"]))
    elif case.startswith("st_go_"):
        completion = s["rec"]["go_delivery_completion"]
        bound = min(60.0, cfg["max_wall_s"] / 2.0)
        observed = completion["mono"]
        age = observed - s["mono_spawn"]  # Original expression order: exact, never approximate.
        remaining = s["mono_spawn"] + cfg["max_wall_s"] - observed
        want = relation(fix["observed_mono"] - fix["mono_spawn"], fix["bound"])
        require("GO_inputs_bind_selected_case_and_model_state", i["mono_spawn"] == s["mono_spawn"] == fix["mono_spawn"] and
                i["max_wall_s"] == cfg["max_wall_s"] == fix["wall"] and bound == fix["bound"] == i["bound"] and
                observed == i["observed_mono"] == last["before"]["mono"] and near(observed, fix["observed_mono"]) and
                last["label"] == "completion_check_GO" and same(last["args"][0], "GO"))
        require("actual_original_completion_fields_exact", completion["spawn_age_s"] == age and
                completion["spawn_age_bound_s"] == bound and completion["remaining_main_runtime_s"] == remaining)
        require("GO_age_on_declared_side_exact_equality", relation(age, bound) == want)
        expect("remaining", near(remaining, exp["remaining"]) and (want != "eq" or remaining == exp["remaining"]))
        expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] is not None) is (want == "gt"))
        expect("failure_codes", type(exp["failure_codes"]) is list and sorted(s["failure_codes"]) == sorted(exp["failure_codes"]))
        expect("stop_requested", (s["stop"] is not None and s["stop"]["reason"] == "FAILURE" and type(s["signal"]) is dict and
                                  s["signal"]["sent"] is True and len(kills) == 1) if exp["stop_requested"] is True else
               (exp["stop_requested"] is False and s["stop"] is None and s["signal"] is None and not kills))
    elif case.startswith("st_age_"):
        obs = i["observation"]
        mono = last["args"][0] if len(last["args"]) == 1 else None
        want = relation(fix["requested_upper"], fix["max_age"])
        require("stability_inputs_bind_selected_case_and_retained_state", same(obs, s["clock_observation"]) and number(mono) and
                i["stability_epoch"] == s["authorization"]["stability_epoch"] and i["expiry"] == s["stability_expiry_mono"] and
                i["max_age"] == cfg["admission"]["stability_max_age_s"] == fix["max_age"] and mono == i["mono"] and
                near(i["requested_age"], fix["requested_upper"]) and last["label"] == "stability_age" and len(steps) == 1)
        if number(mono):
            base = obs["epoch_date_floor"] - i["stability_epoch"]
            upper = max(base + 1.0 + max(0.0, mono - obs["mono_before_read"]), i["max_age"] + mono - i["expiry"])
            require("conservative_upper_on_declared_side_exact_equality", relation(upper, i["max_age"]) == want and
                    (want == "eq" or near(upper, fix["requested_upper"])))
            expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] == "STABILITY_STALE") is (want == "gt"))
            expect("upper", (exp["upper"] is None and last["return"] is None) if want == "gt" else
                   (number(exp["upper"]) and last["return"] == upper and near(upper, exp["upper"]) and
                    (want != "eq" or upper == exp["upper"])))
    elif case in ("st_date_missing", "st_date_malformed", "st_date_naive"):
        stimulus = fix["parser_input"]
        if type(stimulus) is dict:
            if set(stimulus) != {"encoding", "scope", "hex"} or stimulus["encoding"] != "UTF8_HEX" or \
                    stimulus["scope"] != "MODEL_INPUT_NOT_ACTUAL_BIN_DATE":
                raise Invalid("selected parser stimulus encoding")
            stimulus = bytes.fromhex(stimulus["hex"]).decode("utf-8")
        elif stimulus is not None and type(stimulus) is not str:
            raise Invalid("selected parser stimulus type")
        require("parser_stimulus_is_the_selected_case_input", last["label"] == "parse_date_epoch" and len(steps) == 1 and
                same(i["parser_input"], stimulus) and same(last["args"], [stimulus]))
        expect("exception", raised(last, exp["exception"]))
        require("synthetic_parser_text_not_actual_bin_date", encoded["steps"][-1]["exception"]["text"]["encoding"] == "UTF8_HEX")
    elif case == "st_date_future":
        helper = s["helpers"][-1]
        text = bytes.fromhex(helper["capture_hex"]).decode("ascii").strip()
        parsed = datetime.datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
        require("future_branch_binds_selected_case_and_raw_MODEL_capture", parsed.timestamp() == i["model_epoch_floor"] ==
                fix["model_helper_epoch_floor"] and helper["date"] == text and
                i["receipt_stability_epoch"] == s["authorization"]["stability_epoch"] == fix["receipt_epoch"] and
                last["label"] == "date_now" and len(steps) == 1)
        require("declared_civil_shift_realized_in_raw_capture", number(helper["mono_spawn"]) and
                math.floor(1700000000.0 + helper["mono_spawn"] - 1000.0 + fix["model_civil_shift"]) == i["model_epoch_floor"])
        require("future_input_really_future", i["model_epoch_floor"] < i["receipt_stability_epoch"])
        expect("return", exp["return"] is None and succeeded(last) and last["return"] is None)
        expect("failure_codes", type(exp["failure_codes"]) is list and sorted(s["failure_codes"]) == sorted(exp["failure_codes"]))
        expect("error_contains", type(exp["error_contains"]) is str and s["helper_log"][-1]["outcome"] == "FAILED" and
               exp["error_contains"] in s["helper_log"][-1]["error"])
        expect("clock_observation", exp["clock_observation"] is None and s["clock_observation"] is None)
        expect("stability_expiry_mono", exp["stability_expiry_mono"] is None and s["stability_expiry_mono"] is None)
    elif case.startswith("st_stability_"):
        first, second = i["first"], i["second"]
        obs, prior = second["observation"], first["observation"]
        helper = s["helpers"][-1]
        candidate = obs["mono_before_read"] + i["max_age"] - (obs["epoch_date_floor"] - i["stability_epoch"] + 1.0)
        effective = min(first["expiry"], candidate)
        require("stability_inputs_bind_selected_case", i["max_age"] == cfg["admission"]["stability_max_age_s"] and
                i["stability_epoch"] == s["authorization"]["stability_epoch"] and fix["later_check"] == "effective_expiry+0.01" and
                obs["epoch_date_floor"] - prior["epoch_date_floor"] == fix["second_mono_delta"] + fix["civil_shift"] and
                same(obs, s["clock_observation"]) and len(steps) == 2)
        require("nonrenewing_min_recomputed_exact", second["expiry"] == effective == s["stability_expiry_mono"] and
                helper["stability_expiry_before"] == first["expiry"] and helper["stability_expiry_candidate"] == candidate and
                helper["stability_expiry_effective"] == effective)
        expect("candidate_relation", table({"> previous": candidate > first["expiry"], "< previous": candidate < first["expiry"]},
                                           exp["candidate_relation"]))
        expect("effective", table({"previous": effective == first["expiry"], "candidate": effective == candidate}, exp["effective"]))
        expect("second_helper_exception", exp["second_helper_exception"] is None and succeeded(steps[0]) and
               type(steps[0]["return"]) is str and steps[0]["return"] == helper["date"])
        expect("later_exception", i["later_check_mono"] == effective + 0.01 and same(last["args"], [i["later_check_mono"]]) and
               raised(last, exp["later_exception"]) and s["failure_codes"] == [])
    elif case.startswith("st_ack_age_"):
        census = entries(s, "census_history")[-1]
        observed = last["before"]["mono"]
        age = observed - census["mono_complete"]  # Original expression order: exact.
        limit = max(1.0, cfg["sample_s"])
        want = relation(fix["census_age"], limit)
        require("ACK_age_binds_selected_case_and_real_retained_census", same(i["census"], census) and census["complete"] is True and
                i["sample_s"] == cfg["sample_s"] == fix["sample_s"] and observed == last["after"]["mono"] == i["mono"] and
                last["label"] == "resource_age" and len(steps) == 1)
        require("ACK_census_age_on_declared_side_exact_equality", relation(age, limit) == want and near(age, fix["census_age"]))
        expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] is not None) is (want == "gt"))
    elif case.startswith("st_retry_"):
        mode = fix["mode"]
        preserved = table({"unproved": "transient U history", "busy": "BUSY trip and maximum", "rss": "RSS trip and maximum"}, mode)
        censuses = [c for c in entries(s, "census_history") if not c["inside_helper"] and c["phase"] == "RUNNING"]
        require("retry_inputs_bind_selected_case", i["mode"] == mode == case.split("_")[2] and fix["phase"] == "RUNNING" == s["phase"] and
                type(s["stop"]) is dict and s["stop"]["reason"] == fix["prior_stop"] and same(s["stop"], i["previous_stop"]) and
                i["busy_limit"] == cfg["busy_limit"] == fix["busy_limit"] and i["rss_limit"] == cfg["rss_trip_bytes"] == fix["rss_trip_bytes"] and
                i["transient_unproved_uid"] == fix["transient_unproved_uid"] and not kills)
        expect("first_complete", len(censuses) == 2 and censuses[0]["complete"] is exp["first_complete"] is False and
               censuses[0]["incomplete_n"] > 0)
        expect("second_complete", len(censuses) == 2 and censuses[1]["complete"] is exp["second_complete"] is True and
               censuses[1]["incomplete_n"] == 0)
        expect("exception", outcome_is(last, exp["exception"]))
        require("aborted_coverage_retained", len(entries(s, "coverage_history")) >= 1)
        previous = {}
        for index, census in enumerate(censuses):
            current, expected_busy = {}, []
            for measured in census["measurements"]:
                p = measured["identity"]
                key = (p["uniqueid"], p["idversion"])
                now, ticks = measured["mono_observed"], measured["cpu_ticks"]
                if key not in previous:
                    seconds = measured["epoch_observed"] - 1699999900.0
                    busy = seconds <= 0.05 or ticks >= seconds * 1e9 * cfg["busy_cpu_fraction"]
                else:
                    seconds = now - previous[key][0]
                    busy = seconds <= 0 or ticks - previous[key][1] >= seconds * 1e9 * cfg["busy_cpu_fraction"]
                require("retry_CPU_predicate_%d_%d" % (index, p["pid"]), type(measured["busy"]) is bool and measured["busy"] is busy)
                if busy:
                    expected_busy.append(p["pid"])
                current[key] = (now, ticks)
            require("retry_totals_from_raw_measurements_%d" % index,
                    census["lane_rss"] == sum(x["rss"] for x in census["measurements"]) and
                    census["lane_busy"] == len(expected_busy) and census["lane_busy_pids"] == sorted(expected_busy))
            previous = current
        if mode == "unproved":
            unknown = [p["uniqueid"] for p in censuses[0]["unproved_live"]] if len(censuses) == 2 else []
            history = entries(s, "unproved_history")
            expect("preserved", exp["preserved"] == preserved and i["transient_unproved_uid"] in unknown and
                   not censuses[1]["unproved_live"] and any(p["last_identity"]["uniqueid"] == i["transient_unproved_uid"] for p in history))
        elif mode == "busy":
            expect("preserved", exp["preserved"] == preserved and len(censuses) == 2 and censuses[0]["lane_busy"] > i["busy_limit"] and
                   censuses[1]["lane_busy"] <= i["busy_limit"] and "BUSY" in s["trips"] and s["maxima"]["lane_busy"] >= censuses[0]["lane_busy"])
        else:
            expect("preserved", exp["preserved"] == preserved and len(censuses) == 2 and censuses[0]["lane_rss"] > i["rss_limit"] and
                   censuses[1]["lane_rss"] <= i["rss_limit"] and "RSS" in s["trips"] and s["maxima"]["lane_rss"] >= censuses[0]["lane_rss"])
    elif case.startswith("st_abort_"):
        attempts = entries(s, "attempt_history")
        kind = "identity_scan" if case.endswith("identity") else "resource_scan"
        aborted = [a for a in attempts if a["kind"] == kind and a["aborted"]]
        rule = m["clock_rules"][0] if len(m["clock_rules"]) == 1 else {}
        require("abort_boundary_binds_selected_case", rule.get("fired") is True and number(rule.get("returned")) and
                rule["returned"] == i["deadline"] + 0.01 and near(rule["returned"], fix["completion_mono"]) and
                same(i["rule"], rule) and fix["deadline_s"] == 10)
        expect("exception", raised(last, exp["exception"]))
        expect("aborted", exp["aborted"] is True and len(aborted) == 1 and aborted[0]["error"] is not None)
        expect("mono_end", exp["mono_end"] == "not null" and len(aborted) == 1 and number(aborted[0]["mono_end"]) and
               aborted[0]["mono_end"] >= aborted[0]["mono_start"])
        if exp["partial_resources"] is None:
            expect("partial_resources", case == "st_abort_identity" and
                   last["counts_after"]["census_history"] == last["counts_before"]["census_history"])
        else:
            record = entries(s, "census_history")[-1]
            expect("partial_resources", exp["partial_resources"] == "retained/enforced" and case == "st_abort_resource" and
                   record["aborted"] and not record["complete"] and record["mono_end"] is not None and record["measurements"] and
                   record["lane_rss"] == sum(x["rss"] for x in record["measurements"]) and s["maxima"]["lane_rss"] >= record["lane_rss"])
    elif case.startswith("st_cap_bytes_"):
        cap = m["caps"]["bytes"]  # Independently recomputed from the original source by verify_source.
        item = i["entry"]["observation"]
        expected_charge = 2 * len(json.dumps(i["entry"], sort_keys=True, separators=(",", ":"), allow_nan=False).encode()) + 64
        attempted = i["precharge"] + expected_charge
        overflow = attempted > cap["value"]  # Original operator Gt.
        before, after = last["counts_before"]["coverage_history"], last["counts_after"]["coverage_history"]
        require("byte_cap_binds_selected_case_and_verified_source_cap", fix["family"] == "bytes" and same(i["cap"], cap) and
                cap["operator"] == "Gt" and cap["value"] == fix["cap_from_original_source"] and attempted == fix["boundary"] ==
                i["attempted_charge"] and expected_charge == i["charge"] and last["label"] == "retain_coverage" and
                same(last["args"], [[item], i["entry"]["mono"]]))
        expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] == "HISTORY_BYTE_CAP") is overflow)
        expect("history_halted", s["history_halted"] is exp["history_halted"] is overflow)
        expect("accepted_boundary", exp["accepted_boundary"] is (not overflow) and
               ((after == before and s["history_charge"] == i["precharge"]) if overflow else
                (after == before + 1 and s["history_charge"] == attempted)))
        expect("overflow_witness", (exp["overflow_witness"] == "full bounded raw witness" and
                                    overflow_proof(s, "HISTORY_BYTE_CAP", {"observation": item}) and
                                    s["failure_codes"] == ["HISTORY_BYTE_CAP"]) if overflow else
               (exp["overflow_witness"] is None and s["history_overflow"] is None and s["failure_codes"] == []))
    elif case in ("st_cap_final_rss", "st_cap_initial_main", "st_cap_helper_term"):
        mode = table({"retain_identity source=measurement_final_bracket": "final_rss", "retain_identity source=main_initial": "initial_main",
                      "first helper census mono_start": "helper_term"}, fix["checkpoint"])
        overflow = s["history_overflow"]
        require("selected_checkpoint_bound", case == "st_cap_" + mode and i["critical_mode"] == mode and
                type(m["checkpoint"]) is dict and m["checkpoint"]["mode"] == mode and same(i["cap"], m["caps"]["bytes"]))
        require("real_cap_branch_not_overflowflag_only", s["history_halted"] is True and type(overflow) is dict and
                overflow["kind"] == "HISTORY_BYTE_CAP" and "HISTORY_BYTE_CAP" in s["failure_codes"])
        expect("failure_codes_exact", type(exp["failure_codes_exact"]) is list and sorted(s["failure_codes"]) == sorted(exp["failure_codes_exact"]))
        require("calibration_only_selects_initial_state", i["declared_precharge"] + i["calibration"]["target"]["history_charge_before"] -
                i["calibration"]["baseline_charge"] == i["cap"]["value"] and m["checkpoint"]["history_charge_before"] == i["cap"]["value"])
        if mode == "final_rss":
            c = entries(s, "census_history")[-1]
            measured = overflow["completed_measurement"] if type(overflow) is dict else None
            attempts = [a for a in entries(s, "attempt_history") if a["kind"] == "resource_scan"]
            require("final_rss_stimulus_from_selected_case", fix["rss"] == cfg["rss_trip_bytes"] + 1 and fix["rss_limit"] == cfg["rss_trip_bytes"] and
                    s["stop"]["reason"] == fix["prior_stop"] and len(steps) == 2)
            expect("first_exception", raised(steps[0], exp["first_exception"]))
            expect("second_exception", len(steps) == 2 and raised(steps[1], exp["second_exception"]))
            expect("must_preserve", exp["must_preserve"] == ["complete identity/identity_after/rss/cpu/busy/mono composite",
                                                             "partial totals/RSS trip/maxima", "completed_measurement overflow witness",
                                                             "aborted/end attempt", "no resumed scan"] and
                   type(measured) is dict and measured in c["measurements"] and same(measured["identity_after"], measured["identity"]) and
                   measured["rss"] == fix["rss"] and type(measured["cpu_ticks"]) is int and type(measured["busy"]) is bool and
                   number(measured["mono_observed"]) and c["lane_rss"] >= measured["rss"] and "RSS" in s["trips"] and
                   s["maxima"]["lane_rss"] >= c["lane_rss"] and c["aborted"] and not c["complete"] and c["mono_end"] is not None and
                   bool(attempts) and attempts[-1]["aborted"] is True and number(attempts[-1]["mono_end"]) and
                   steps[1]["counts_before"] == steps[1]["counts_after"] and
                   not any(x["operation"].startswith("proc_") for x in ops[steps[1]["event_begin"]:steps[1]["event_end"]]))
        elif mode == "initial_main":
            require("initial_main_contained_failure_returns_without_exception", succeeded(last) and last["return"] is None)
            ident = s["rec"]["main_initial_identity_observed"]
            completed = overflow.get("completed_identity_observation") if type(overflow) is dict else None
            signals = [x for x in kills if x["pgid"] == ident["pgid"]]
            require("initial_main_stimulus_from_selected_case", fix["max_wall_s"] == cfg["max_wall_s"] and fix["settle_s"] == cfg["settle_s"])
            expect("history_error", exp["history_error"] == overflow["kind"] == "HISTORY_BYTE_CAP")
            expect("raw_initial_identity", exp["raw_initial_identity"] == "preserved in rec and s.ident/group" and
                   same(s["ident"], ident) and s["group"] == ident["pgid"] == s["pid"] and same(overflow["witness"]["identity"], ident) and
                   type(completed) is dict and same(completed["identity"], ident) and
                   same(s["rec"]["main_initial_identity_interval"], [completed["mono_begin"], completed["mono_end"]]))
            expect("signal", exp["signal"] == "one MODEL freshly fingerprint-checked TERM" and same(s["signal"]["identity_observed"], ident) and
                   s["signal"]["identity_ok"] is True and s["signal"]["sent"] is True and len(signals) == len(kills) == 1)
            expect("main_rc", same(s["rc"], exp["main_rc"]))
            expect("go_delivered", exp["go_delivered"] is False and s["rec"].get("go_delivered") is not True and
                   {"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED", "OBSERVATION_FAILED"} <= set(s["failure_codes"]))
        else:
            require("helper_cap_failure_is_a_null_date_return_not_an_unrelated_exception", succeeded(last) and last["return"] is None)
            h = s["helpers"][-1]
            sig = h["signal"]
            signals = [x for x in kills if x["pgid"] == h["identity"]["pgid"]]
            require("helper_term_stimulus_from_selected_case", fix["term_grace_s"] == cfg["helper_budget"]["term_grace_s"] and
                    fix["helper_wait"] == "running until MODEL TERM")
            expect("history_error", exp["history_error"] == overflow["kind"] == "HISTORY_BYTE_CAP")
            expect("helper_failure", exp["helper_failure"] == "HELPER_CALL_FAILED" and exp["helper_failure"] in s["failure_codes"])
            expect("ownership_failure", exp["ownership_failure"] == "HELPER_OWNERSHIP_UNSETTLED" and exp["ownership_failure"] in s["failure_codes"])
            expect("signal_count", h["term_attempted"] is True and len(signals) == len(kills) == exp["signal_count"] == 1 and
                   sig["sent"] is True and sig["identity_ok"] is True and same(sig["identity_observed"], h["identity"]) and
                   sig["mono_check"] <= sig["mono_identity_observed"] <= sig["mono_sent"])
            expect("helper_rc", h["leader_reaped"] is True and same(h["rc"], exp["helper_rc"]))
            expect("settled", h["settled"] is exp["settled"] is False)
    elif case.startswith("st_cap_"):
        family = fix["family"]
        codes = {"identity": "IDENTITY_HISTORY_CAP", "unproved": "UNPROVED_HISTORY_CAP", "coverage": "COVERAGE_HISTORY_CAP",
                 "attempt": "ATTEMPT_HISTORY_CAP", "census": "CENSUS_HISTORY_CAP", "variants": "IDENTITY_VARIANT_CAP"}
        names = {"identity": "identity_history", "unproved": "unproved_history", "coverage": "coverage_history",
                 "attempt": "attempt_history", "census": "census_history"}
        kind = table(codes, family)
        cap = m["caps"][family]
        desired, pre = i["requested_post_count"], i["pre_count"]
        overflow = pre >= cap["value"]  # Original GtE refusal before the attempted append.
        witness, completed = attempted_witness(family, last, s)
        require("count_cap_binds_selected_case_and_verified_source_cap", i["family"] == family == case.split("_")[2] and
                same(i["cap"], cap) and cap["operator"] == "GtE" and cap["value"] == fix["cap_from_original_source"] and
                desired == fix["boundary"] and pre == desired - 1)
        if family == "variants":
            records = entries(s, "identity_history")
            count = len(records[-1]["variants"]) if records and records[-1]["first_identity"]["uniqueid"] == witness["identity"]["uniqueid"] else None
            appended = True
        else:
            count = s["histories"][names[family]]["count"]
            appended = last["counts_before"][names[family]] == pre and last["counts_after"][names[family]] == count
        require("original_count_cap_exact_attempted_count", count == (pre if overflow else desired) and appended)
        expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] == codes[family]) is overflow)
        expect("history_halted", s["history_halted"] is exp["history_halted"] is overflow)
        expect("accepted_boundary", exp["accepted_boundary"] is (not overflow))
        expect("overflow_witness", (exp["overflow_witness"] == "full bounded raw witness" and
                                    overflow_proof(s, codes[family], witness, completed) and s["failure_codes"] == [codes[family]]) if overflow else
               (exp["overflow_witness"] is None and s["history_overflow"] is None and s["failure_codes"] == []))
        require("count_state_reachability_honestly_disclosed", family == "variants" or i["prestate_byte_charge_reset"] is True and
                any("NOT physical/native coverage" in text for text in m["disclosures"]))
    elif case.startswith("st_budget_output_"):
        payload = s["publication_payload_bytes"]
        b, end = s["publication_resources"], s["ack_resources"]
        events = s["accounting_observations"]
        summaries = [decode(line.encode()) for line in m["stdout"].splitlines()]
        summary = summaries[0] if len(summaries) == 1 else {}
        require("output_boundary_binds_selected_case", i["delta"] == fix["delta"] and cfg["output_trip_bytes"] == fix["output_trip_bytes"] and
                fix["total"] == "actual original serialized payload + MODEL accounting charge" and
                0 < len(i["calibration"]) <= fix["calibration_rounds_max"] and type(payload) is int and payload == i["payload_bytes"] and
                type(b) is dict and b["charged_bytes"] + payload == cfg["output_trip_bytes"] + fix["delta"] and len(summaries) == 1 and
                last["label"] == "finalize" and len(steps) == 1)
        fits = type(b) is dict and b["charged_bytes"] + payload <= cfg["output_trip_bytes"]
        expect("return", succeeded(last) and type(last["return"]) is int and last["return"] == exp["return"] and (exp["return"] == 10) is fits)
        returned = [e for e in events if e["returned"] is True and e["retained"] is True and number(e["mono_observed"])]
        if exp["summary"] == "acknowledged NOT_LAUNCHED":
            if end is None or len(events) != 3 or any(e["returned"] is not True for e in events):
                raise Invalid("required successful end accounting unavailable")
            artifacts = m["artifacts"]
            rb = bytes.fromhex(artifacts[cfg["receipt"]]["data_hex"]) if cfg["receipt"] in artifacts else b""
            sb = bytes.fromhex(artifacts[cfg["settlement_record"]]["data_hex"]) if cfg["settlement_record"] in artifacts else b""
            receipt = decode(rb) if rb else {}
            settled = decode(sb) if sb else {}
            ack_keys = {"supervisor", "acknowledged", "exit_code", "settlement", "config_sha256", "receipt_sha256",
                        "settlement_record_sha256", "receipt_bytes", "settlement_bytes", "post_publish_mono", "ack_commit",
                        "publication_resources", "ack_resources", "publication_payload_bytes", "child_returncode", "failure_codes",
                        "owned_live", "unproved_live", "ack_census", "contract_violations", "unproved_history", "coverage_history",
                        "census_observations", "reconciliation"}
            settlement_keys = {"supervisor", "config_sha256", "settlement", "receipt", "receipt_sha256", "child_returncode",
                               "failure_codes", "trips", "authority"}
            expect("summary", set(summary) == ack_keys and set(settled) == settlement_keys and
                   summary.get("acknowledged") is True and summary.get("exit_code") == 10 and
                   summary.get("settlement") == "NOT_LAUNCHED" and summary.get("config_sha256") == digest and
                   summary.get("receipt_sha256") == hashlib.sha256(rb).hexdigest() and
                   summary.get("settlement_record_sha256") == hashlib.sha256(sb).hexdigest() and
                   summary.get("receipt_bytes") == len(rb) and summary.get("settlement_bytes") == len(sb) and
                   summary.get("publication_payload_bytes") == payload and same(summary.get("publication_resources"), b) and
                   summary.get("failure_codes") == sorted(s["failure_codes"]) and
                   receipt.get("settlement") == "NOT_LAUNCHED" and receipt.get("config_sha256") == digest and
                   len(events) == 3 and same(receipt.get("publication_precheck"), events[0]["resources"]) and
                   receipt.get("publication_precheck_ref") == events[0]["id"] and
                   same(receipt.get("accounting_observations"), events[:1]) and
                   same(receipt.get("min_free_witness"), events[0]) and
                   settled.get("settlement") == "NOT_LAUNCHED" and settled.get("receipt_sha256") == hashlib.sha256(rb).hexdigest() and
                   settled.get("config_sha256") == digest and settled.get("receipt") == cfg["receipt"] and
                   "child_returncode" in settled and settled["child_returncode"] is None and
                   settled.get("failure_codes") == summary.get("failure_codes") and
                   type(receipt.get("trips")) is list and settled.get("trips") == [row.get("trip") for row in receipt["trips"]] and
                   sorted(settled["trips"]) == sorted(s["trips"]) and
                   artifacts[cfg["settlement_record"]]["inode"] == artifacts[cfg["settlement_record"] + ".staged"]["inode"])
            expect("ack_resources", exp["ack_resources"] == "actual MODEL returned end" and type(end) is dict and len(events) == 3 and
                   len(returned) == 3 and same(end, events[2]["resources"]) and same(summary.get("ack_resources"), end) and
                   same(b, events[1]["resources"]) and same(s["last_accounting_observation"], events[2]))
            expect("actual_payload", exp["actual_payload"] == "not a requested estimate" and len(rb) + len(sb) == payload and
                   i["calibration"][-1]["payload"] == payload)
        elif exp["summary"] == "PUBLICATION_REFUSED":
            refusal_keys = {"supervisor", "acknowledged", "exit_code", "reason", "clock_note", "reconciliation", "config_sha256",
                            "payload_bytes", "resources", "reservation_bytes"}
            expect("summary", set(summary) == refusal_keys and summary.get("acknowledged") is False and summary.get("exit_code") == 12 and
                   summary.get("reason") == "PUBLICATION_REFUSED" and summary.get("config_sha256") == digest and
                   summary.get("payload_bytes") == payload and same(summary.get("resources"), b) and not m["artifacts"])
            expect("ack_resources", exp["ack_resources"] is None and end is None and len(events) == 2 and len(returned) == 2 and
                   same(b, events[1]["resources"]))
            expect("actual_payload", exp["actual_payload"] == "not a requested estimate" and i["calibration"][-1]["payload"] == payload)
        else:
            raise Invalid("uninterpretable selected publication disposition")
    elif case.startswith("st_budget_"):
        family = fix["family"]
        a, adm, payload = i["resources"], i["admission"], i["payload"]
        require("budget_inputs_bind_selected_case_and_fixed_model_config", i["family"] == family == case.split("_")[2] and
                same(adm, cfg["admission"]) and payload == fix["payload"] and i["delta"] == fix["delta"] and
                adm["reservation_bytes"] == fix["reservation"] and i["free_trip_bytes"] == cfg["free_trip_bytes"] == fix["free_trip_bytes"] and
                i["lane_ceiling"] == cfg["lane_disk_ceiling_bytes"] == fix["lane_ceiling"] and last["label"] == "reservation_fits" and
                same(last["args"], [a, payload]) and len(steps) == 1)
        remaining = max(0, adm["reservation_bytes"] - a["charged_bytes"] - payload)
        slack = {"reservation": adm["reservation_bytes"] - (a["charged_bytes"] + payload),
                 "free": a["free"] - payload - adm["outstanding_reservations_bytes"] - remaining - i["free_trip_bytes"],
                 "lane": i["lane_ceiling"] - (a["lane_bytes"] + payload + adm["lane_outstanding_reservations_bytes"] + remaining)}
        target = table({"reservation": -slack["reservation"], "free": slack["free"], "lane": -slack["lane"]}, family)
        require("exact_isolated_budget_boundary", target == fix["delta"])
        require("non_target_budget_predicates_nonbinding", all(value > 0 for name, value in slack.items() if name != family))
        expect("return", succeeded(last) and type(exp["return"]) is bool and last["return"] is exp["return"] and
               last["return"] is all(value >= 0 for value in slack.values()))
    elif case.startswith("st_cutoff_census_"):
        rule = m["clock_rules"][0] if len(m["clock_rules"]) == 1 else {}
        c = entries(s, "census_history")[-1]
        observed = rule.get("returned")
        want = relation(fix["offset_s"], 0)
        require("census_cutoff_binds_selected_case_and_source_constant", fix["family"] == "census" and
                fix["source_constant"] == constants["CENSUS_S"] and rule.get("function") == "aux_clock" and number(observed) and
                observed == i["deadline"] + fix["offset_s"] and any(x["mono_observed"] == observed for x in c["measurements"]) and
                last["label"] == "census" and len(steps) == 1)
        require("census_completion_on_declared_side_exact_equality", number(observed) and relation(observed, i["deadline"]) == want)
        expect("equality_allowed", exp["equality_allowed"] is True)
        expect("late", exp["late"] == "DEADLINE_EXCEEDED" and (want != "gt" or raised(last, "DEADLINE_EXCEEDED") and
                                                                c["aborted"] is True and not c["complete"] and c["mono_end"] is not None))
        expect("before_or_equal", exp["before_or_equal"] == "original completion accepted under declared MODEL dependencies" and
               (want == "gt" or succeeded(last) and c["complete"] is True and c["aborted"] is False and c["mono_end"] is not None))
    elif case.startswith("st_cutoff_helper_"):
        h = s["helpers"][-1]
        rule = m["clock_rules"][0] if len(m["clock_rules"]) == 1 else {}
        observed = rule.get("returned")
        want = relation(fix["offset_s"], 0)
        terminal = [x for x in waits if x["pid"] == h["pid"] and x["returned"][0] != 0]
        require("helper_cutoff_binds_selected_case", fix["family"] == "helper" and
                fix["source_constant"] == cfg["helper_budget"]["call_budget_s"] and number(observed) and
                observed == i["deadline"] + fix["offset_s"] and
                i["deadline"] == i["call_start"] + cfg["helper_budget"]["call_budget_s"] == h["mono_call_deadline"] == h["call_deadline"]["end"] and
                h["mono_call_start"] == i["call_start"] and last["label"] == "date_now" and len(steps) == 1)
        require("helper_completion_observation_on_declared_side_every_arm", number(observed) and relation(observed, i["deadline"]) == want)
        require("helper_successful_terminal_reap_retained", h["leader_reaped"] is True and h["rc"] == 0 and h["wait_lost"] is False and
                len(terminal) == 1 and same(terminal[0]["returned"], [h["pid"], 0]))
        expect("equality_allowed", exp["equality_allowed"] is True)
        expect("before_or_equal", exp["before_or_equal"] == "original completion accepted under declared MODEL dependencies" and
               (want == "gt" or succeeded(last) and type(last["return"]) is str and last["return"] == h["date"] ==
                bytes.fromhex(h["capture_hex"]).decode("ascii").strip() and settled_proof(h, m, s) and
                h["mono_proof_complete"] == observed and s["failure_codes"] == []))
        expect("late", exp["late"] == "date_now returns null + HELPER_CALL_FAILED" and
               (want != "gt" or succeeded(last) and last["return"] is None and h["date"] is None and h["clock_failed"] is True and
                s["failure_codes"] == ["HELPER_CALL_FAILED"] and
                any(row["code"] == "HELPER_CALL_FAILED" and "DEADLINE_EXCEEDED" in row["detail"] for row in s["failures"]) and
                s["helper_log"][-1]["outcome"] == "FAILED" and "DEADLINE_EXCEEDED" in s["helper_log"][-1]["error"]))
    elif case.startswith("st_cutoff_stop_grace_") or case.startswith("st_cutoff_exit_grace_"):
        name = table({"stop_grace": "GRACE_EXPIRED_AFTER_STOP_REQUEST", "exit_grace": "GRACE_EXPIRED_AFTER_CHILD_EXIT"}, fix["family"])
        rules = [r for r in m["clock_rules"] if r["function"] == "clearance"]
        observed = rules[0].get("returned") if len(rules) == 1 == len(m["clock_rules"]) else None
        want = relation(fix["offset_s"], 0)
        if not number(observed):
            raise Invalid("required final grace-completion observation unavailable")
        cuts = []  # Applicable PRE-clearance cutoffs, independently reconstructed from the declared retained evidence.
        if fix["family"] == "stop_grace":
            require("preexisting_MODEL_stop_is_the_stop_grace_stimulus", type(s["stop"]) is dict and
                    s["stop"]["reason"] == "MODEL_STOP" and number(s["stop"]["mono"]))
            if type(s["stop"]) is dict and number(s["stop"]["mono"]):
                cuts.append(["GRACE_EXPIRED_AFTER_STOP_REQUEST", s["stop"]["mono"] + cfg["settle_s"]])
        else:
            # clearance.fail(exit-grace) creates a NEW stop after the late observation; it is not a renewed grace right.
            require("exit_grace_has_no_preexisting_stop_or_renewed_grace", s["stop"] is None or want == "gt" and
                    s["stop"]["reason"] == "FAILURE" and s["stop"]["mono"] == observed)
        if s["exit_mono"] is not None:
            cuts.append(["GRACE_EXPIRED_AFTER_CHILD_EXIT", s["exit_mono"] + cfg["settle_s"]])
        require("grace_cutoff_recomputed_from_retained_stop_exit", bool(cuts) and cuts[0][0] == name and same(i["cutoffs"], cuts) and
                i["deadline"] == min(value for _, value in cuts) == cuts[0][1] and fix["source_constant"] == cfg["settle_s"] and
                fix["family"] == "_".join(case.split("_")[2:4]))
        require("recorded_final_completion_observation_on_declared_side", number(observed) and rules[0]["fired"] is True and
                observed == i["deadline"] + fix["offset_s"] and relation(observed, i["deadline"]) == want)
        require("clearance_returns_after_all_predicates", succeeded(last) and last["return"] is True and last["label"] == "clearance" and
                len(steps) == 1)
        expect("equality_allowed", exp["equality_allowed"] is True)
        expect("late", exp["late"] == "clearance returns true with matching GRACE_EXPIRED latch, no clear timestamp" and
               (want != "gt" or s["clear"] is None and s["loop_status"] == name and name in s["failure_codes"] and
                any(row["code"] == name and row["detail"] == "all-clear verified after cutoff" and row["mono"] == observed
                    for row in s["failures"])))
        expect("before_or_equal", exp["before_or_equal"] == "original completion accepted under declared MODEL dependencies" and
               (want == "gt" or type(s["clear"]) is dict and s["clear"]["mono_all_predicates_verified"] == observed and
                s["clear"]["mono_all_predicates_verified"] >= s["clear"]["census"]["mono_complete"] and s["loop_status"] == "EXITED" and
                s["failure_codes"] == []))
    elif case.startswith("st_cutoff_finalize_"):
        want = relation(fix["offset_s"], 0)
        require("finalization_constant_from_source_and_selected_case", fix["family"] == "finalize" and
                i["seconds"] == constants["FINALIZE_S"] == fix["source_constant"] and
                last["before"]["mono"] == i["observed_mono"] == i["deadline"] + fix["offset_s"] and
                last["label"] == "completion_check_ACK" and same(last["args"][0], "ACK") and len(steps) == 1)
        require("finalization_completion_on_declared_side_exact_equality", relation(i["observed_mono"], i["deadline"]) == want)
        expect("equality_allowed", exp["equality_allowed"] is True)
        expect("late", exp["late"] == "DEADLINE_EXCEEDED" and (want != "gt" or raised(last, "DEADLINE_EXCEEDED")))
        expect("before_or_equal", exp["before_or_equal"] == "original completion accepted under declared MODEL dependencies" and
               (want == "gt" or succeeded(last) and last["return"] is None))
    elif case.startswith("st_write_"):
        data = bytes.fromhex(fix["payload_hex"])
        pipes = [x for x in ops if x["operation"] == "pipe"]
        writes = [x for x in ops if x["operation"] == "write"]
        result = bytes.fromhex(i["result_data_hex"])
        mode = fix["mode"]
        fds = [pipes[0]["read_fd"], pipes[0]["write_fd"]] if len(pipes) == 1 else []
        prefix = write_prefix(writes, data, fds[1]) if fds else None
        closes = [x for x in ops if x["operation"] == "close" and x["index"] > last["after"]["calls"]]
        anchors = s["anchor_fds"]
        permitted = sorted([anchors["lane"], anchors["tmp"]] + anchors["roots"]) if \
            all(integer(v) for v in [anchors["lane"], anchors["tmp"]] + anchors["roots"]) else None
        require("write_inputs_bind_selected_case", i["data_hex"] == fix["payload_hex"] and i["mode"] == mode == case.rsplit("_", 1)[1] and
                i["bytes"] == len(data) and len(pipes) == 1 and last["label"] == "write_all" and len(steps) == 1 and
                len(last["args"]) == 3 and last["args"][0] == fds[1] and last["args"][1] == data and fix["deadline_s"] == 1)
        require("independent_write_prefix_reconstruction", bool(writes) and prefix is not None and result == data[:prefix])
        require("write_descriptors_closed_and_exact_remaining_set", len(fds) == 2 and [x["fd"] for x in closes] == fds and
                permitted is not None and len(anchors["roots"]) == len(cfg["output_roots"]) == 1 and
                len(permitted) == len(set(permitted)) == 3 and m["open_model_fds"] == permitted and
                not set(fds) & set(m["open_model_fds"]))
        expect("exception", outcome_is(last, exp["exception"]))
        expect("bytes_preserved", (result == data and prefix == len(data)) if exp["bytes_preserved"] == "entire fixed payload" else
               (exp["bytes_preserved"] == 0 and result == b"" and prefix == 0))
        if mode == "short":
            require("real_write_all_retries_remaining_buffer", len(writes) > 1 and writes[0]["returned"] < writes[0]["requested"])
        elif mode == "zero":
            require("zero_progress_not_accepted", len(writes) == 1 and writes[0]["returned"] == 0)
        else:
            require("successful_late_write_rejected_after_return", mode == "late" and len(writes) == 1 and
                    writes[0]["mono_before"] < i["deadline"] < writes[0]["mono_after"] == i["deadline"] + 0.01 and
                    writes[0]["returned"] == len(data))
    elif case.startswith("st_manifest_"):
        prep = i["preparation"]
        target = fix["canonical_line_bytes"]
        manifest = {"kind": "qualification-creation-manifest-v1", "scenario": "mutate_pin",
                    "preparation_sha256": cfg["creation_channel"]["preparation_sha256"], "run": prep["run"],
                    "output_root": prep["output_root"], "target": i["actual_original_target"]}
        line = canon(manifest)
        require("manifest_inputs_bind_selected_case", target == int(case.rsplit("_", 1)[1]) == i["target_length"] and
                fix["model_run_path_padding"] is True and fix["model_inode_digit_residue"] is True and
                last["label"] == "creation_manifest" and len(steps) == 1)
        require("exact_canonical_manifest_length_recomputed", len(line) == target)
        over = target > 4096
        expect("exception", outcome_is(last, exp["exception"]) and (exp["exception"] == "CREATION_MANIFEST_BYTE_CAP") is over)
        expect("returned_bytes", (exp["returned_bytes"] is None and last["return"] is None) if over else
               (exp["returned_bytes"] == target and last["return"] == line))
        expect("rec_manifest", table({"absent": over and "go_creation_manifest" not in s["rec"],
                                      "exact canonical bytes + SHA": not over and same(s["rec"].get("go_creation_manifest"), manifest) and
                                      s["rec"].get("go_creation_manifest_sha256") == hashlib.sha256(line).hexdigest()},
                                     exp["rec_manifest"]))
    elif case == "st_cancel_pending_after_handled":
        require("cancel_inputs_bind_selected_case", i["handled_signal"] == fix["handled_signal"] and
                i["new_pending_signal"] == fix["new_pending_signal"] and fix["phase"] == "ACK" and len(steps) == 2 and
                all(same(x["args"][0], "ACK") for x in steps))
        expect("first_exception", outcome_is(steps[0], exp["first_exception"]))
        expect("second_exception", outcome_is(steps[1], exp["second_exception"]))
        expect("cancel_handled", s["cancel_handled"] is exp["cancel_handled"] is True and i["new_pending_signal"] in s["pending_signals"] and
               s["cancel"]["signal"] == i["handled_signal"])
    else:
        raise Invalid("independent case predicate dispatch absent")
    if set(exp) != handled:
        raise Invalid("selected expected outcome field not independently enforced")
    return checks, None


def main():
    if sys.platform != "darwin" or os.path.abspath(__file__) != ORACLE or os.path.realpath(__file__) != ORACLE or \
            len(sys.argv) != 4 or sys.argv[1] not in CASES or not hex64(sys.argv[2]) or not hex64(sys.argv[3]):
        raise Invalid("fixed oracle CASE_ID APPROVAL_SHA PARENT_CAPTURE_SHA interface")
    case, approval, capture = sys.argv[1:]
    budget = Budget()
    runfd = directory(ROOT + "/" + case)
    try:
        outcome, cp, captures, sources, specs, outcome_file = exact_authority(case, approval, capture, runfd, budget)
        checks, forced = evaluate(case, outcome, cp, captures, sources, specs)
        verdict = forced or ("FIXTURE_PREDICATES_MET" if all(checks.values()) else "NOT_MET")
        if any(not checks[k] for k in checks if k.startswith("external_") or k.startswith("full_native_")):
            verdict = "NOT_MET"
        result = {"kind": "rqls10-state-oracle-v1", "case": case, "scope": SCOPE, "verdict": verdict,
                  "approval_sha256": approval, "capture_sha256": capture, "outcome_sha256": outcome_file["sha256"],
                  "criteria": checks, "native_coverage": "NOT_EXERCISED", "release": None, "science_acceptance": None,
                  "verification_boundary": {"event_counts": "Canonical retained tape replay except explicit count-isolation prestates",
                      "not_independently_recomputed_scalars": ["aggregate history_charge outside byte-cap case", "whole operation-trace hash with suppressed prefill"],
                      "pending_raw": "Incomplete evidence only, never substitute for a healthy interval, BUSY proof or settlement",
                      "outcome_identity": "Driver-reported original O_EXCL fstat inode bound through external parent stdout capture, independently no-follow reopened; origin authentication/replacement detection remains J18 parent-external"},
                  "status14_note": "Actual supervisor terminal14 is separate native IO integration;120 never accepted.",
                  "authority": "No allocation, GO, admission, automatic case chain, science verdict or reservation release."}
        budget.check()
        os.write(1, canon(result))
        return 0 if verdict == "FIXTURE_PREDICATES_MET" else 1
    finally:
        os.close(runfd)


if __name__ == "__main__":
    try:
        status = main()
    except BaseException as failure:
        raw = repr(failure).encode("utf-8", "surrogatepass")
        os.write(1, canon({"kind": "rqls10-state-oracle-v1", "verdict": "HOLD", "scope": SCOPE,
                           "error": {"encoding": "UTF8_HEX", "scope": "MODEL_INPUT_NOT_ACTUAL_BIN_DATE", "hex": raw[:4096].hex()},
                           "release": None, "science_acceptance": None}))
        status = 2
    sys.exit(status)
