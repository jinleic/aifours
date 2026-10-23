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
DRIVER = LANE + "/code/guard_matrix_state_v1.py"
ORACLE = LANE + "/code/guard_matrix_state_check_v1.py"
SPECS = LANE + "/review/rqls10-matrix-state-v1-cases.json"
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
            wait["waitpid_pid"] != cp["pid"] or wait["reaped"] is not True or \
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
    if set(first) != {"kind", "pid", "pgid", "mono_begin", "scope"} or first["kind"] != "rqls10-matrix-owner-v1" or \
            first["scope"] != SCOPE or (first["pid"], first["pgid"]) != (cp["pid"], cp["pgid"]):
        raise Invalid("first native owner record")
    owner = outcome.get("owner")
    if type(owner) is not dict or set(owner) != {"pid", "pgid", "mono_begin", "mono_end"} or \
            owner["pid"] != cp["pid"] or owner["pgid"] != cp["pgid"] or owner["mono_begin"] != first["mono_begin"] or \
            not cp["mono_begin"] <= owner["mono_begin"] <= owner["mono_end"] <= cp["mono_end"]:
        raise Invalid("owner/capture monotonic ordering")
    if set(last) != {"kind", "case", "scope", "outcome_sha256", "bytes"} or \
            last != {"kind": "rqls10-state-outcome-written-v1", "case": case, "scope": SCOPE,
                     "outcome_sha256": of["sha256"], "bytes": of["bytes"]}:
        raise Invalid("exclusive outcome/capture join")
    if outcome.get("kind") != "rqls10-guard-matrix-outcome-v1" or outcome.get("case") != case or outcome.get("scope") != SCOPE:
        raise Invalid("outcome kind/case/scope")
    binding = {"approval_sha256": approval_sha, "request_sha256": rqf["sha256"], "run": run, "sources": ap["sources"],
               "hook_set": HOOK_SET, "allocation": rq["allocation"], "negative_control": negative,
               "model_inputs_sha256": rq["model_inputs_sha256"], "not_after_epoch": rq["not_after_epoch"], "native_config": None}
    if not same(outcome.get("bindings"), binding):
        raise Invalid("outcome actual authority binding")
    for key, entry in (("request", rqf), ("approval", apf)):
        record = outcome["artifacts"][key]
        if record != {"original": facts(entry), "current": facts(entry)}:
            raise Invalid("authority original/current inode+digest")
    if outcome["artifacts"]["sources"] != {k: facts(v) for k, v in actual_sources.items()}:
        raise Invalid("source original facts")
    return outcome, cp, captures, actual_sources, specs["cases"][case], of


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
    return values


def code(step):
    return None if step["exception"] is None else step["exception"]["code"]


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
    if len(by_uid) != len(ledgers):
        raise Invalid("duplicate identity ledger")
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
    for ledger in entries(state, "unproved_history"):
        uid = ledger["first_identity"]["uniqueid"]
        rows = [row for row in per_uid[uid] if row[4]]
        first = min(rows, key=lambda r: r[2])
        last = max(rows, key=lambda r: (r[2], r[0]))
        if (ledger["first_event_ref"], ledger["last_event_ref"]) != (first[0], last[0]) or \
                ledger["first_identity"] != first[3] or ledger["last_identity"] != last[3]:
            raise Invalid("unproved historical acquisition reconstruction")
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


def evaluate_added(case, m, s, cfg, require):
    """Separate raw predicates; no driver import, source execution, pass bit or release verdict."""
    i, steps, ops = m["inputs"], m["steps"], m["operations"]
    last = steps[-1]
    waits = [x for x in ops if x["operation"] == "waitpid"]
    main_waits = [x for x in waits if x["pid"] == 700000010]
    kills = [x for x in ops if x["operation"] == "killpg"]
    fingerprints = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
    raw = s["raw_acquisitions"]
    if case.startswith("st_complete_"):
        phase, boundary = i["phase"], i["boundary"]
        _, _, named_phase, named_boundary, _ = case.split("_")
        require("case_binds_exact_phase_and_cutoff", phase == named_phase.upper() and boundary == named_boundary and
                last["label"] == "protected_" + phase + "_completion" and last["args"][0] == phase)
        delta = {"lt": -0.01, "eq": 0.0, "gt": 0.01}[case.rsplit("_", 1)[-1]]
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
        require("protected_completion_exact_source_predicate", code(last) == expected == required and last["return"] is None)
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
        before, after, field, sig = i["before"], i["after"], i["field"], s["signal"]
        values = {"uniqueid": 2700000010, "euid": 0, "ruid": 0, "idversion": 2, "ppid": 1, "pgid": 700000099, "traced": True}
        require("fixed_identity_transition_not_arbitrary_input", field == case.rsplit("_", 1)[1] and
                same(i["value"], values[field]) and same(after[field], values[field]) and before["pid"] == 700000010)
        require("changed_full_fingerprint_refuses_TERM", [k for k in fingerprints if before[k] != after[k]] == [field] and
                sig["identity_observed"] == after and sig["identity_ok"] is False and sig["sent"] is False and not kills)
        require("fresh_signal_witness_and_conservative_failure", code(last) is None and
                s["failure_codes"] == ["IDENTITY_UNVERIFIED"] and sig["identity_event_ref"] is not None and
                s["stop"]["reason"] == "MODEL_STOP_REQUEST" and "identity mismatch" in sig["error"])
    elif case.startswith("st_ident_read_"):
        transition = m["metadata_transitions"][0]
        cs = [c for c in entries(s, "census_history") if not c["inside_helper"] and c["phase"] == "RUNNING"]
        values = {"uniqueid": 2700000010, "euid": 0, "ruid": 0, "idversion": 2, "ppid": 1, "pgid": 700000099, "traced": True}
        require("fixed_read_transition_not_arbitrary_input", i["field"] == case.rsplit("_", 1)[1] and
                same(i["value"], values[i["field"]]) and transition["source"] == "pid_scan" and transition["pid"] == 700000010)
        error = "IDENTITY_CHANGED" if i["field"] in ("uniqueid", "idversion") else "IDENTITY_METADATA_CHANGED"
        require("mid_read_full_fingerprint_change_observed", transition["field"] == i["field"] and
                transition["after_reads"] == 2 and transition["fired"] is True and transition["after"][i["field"]] == i["value"])
        require("read_inconsistency_is_failed_coverage_not_absence", len(cs) == 2 and
                not cs[0]["complete"] and cs[0]["incomplete_n"] == 1 and cs[1]["complete"] and
                any(row["observation"][0] == 700000010 and error in row["observation"][2] for row in entries(s, "coverage_history")))
        require("persistent_changed_identity_not_restored", code(last) is None and not kills and
                (s["failure_codes"] == [] if i["field"] == "uniqueid" else s["failure_codes"] == ["CHILD_IDENTITY_CHANGED"]))
        if i["field"] == "uniqueid":
            require("reused_PID_incarnation_history_survives", any(row["last_identity"]["uniqueid"] == i["value"]
                    for row in entries(s, "unproved_history")) and any(row["identity"]["uniqueid"] == i["value"] and
                    row["via"] == "owned_group" for row in s["owned"]))
    elif case == "st_ident_bracket_changed":
        c = entries(s, "census_history")[-1]
        measured = c["raw_measurements"][-1]
        require("changed_final_bracket_cannot_qualify_RSS", code(last) == "TASK_IDENTITY_CHANGED" and
                s["failure_codes"] == ["RESOURCE_ACQUISITION_INCOMPLETE"] and c["aborted"] and not c["complete"] and
                c["measurements"] == [] and c["lane_rss"] == 0 and measured["bracket_verified"] is False and
                measured["identity_after"]["ppid"] == 1 and measured["identity"]["ppid"] == 700000001 and measured["busy"] is None)
        require("returned_task_and_changed_identity_retained", any(r["kind"] == "task" and r["native_returned"] for r in raw) and
                any(r["kind"] == "identity" and r["native_returned"] and r["identity"] == measured["identity_after"] for r in raw) and not kills)
    elif case == "st_ident_mixed_uid_unreadable":
        p = i["mixed_identity"]
        cs = [c for c in entries(s, "census_history") if c["phase"] == "RUNNING"]
        require("same_real_UID_attempted_despite_foreign_effective_UID", p["euid"] == 0 and p["ruid"] == 501 and
                len([x for x in ops if x["operation"] == "proc_pidinfo" and x["pid"] == p["pid"] and x["flavor"] == 4 and
                     x["returned"] == 0 and x["model_errno"] == 13]) == 3)
        require("unreadable_retries_never_prove_clean_coverage", code(last) is None and len(cs) == 3 and
                all(not c["complete"] and c["incomplete_n"] == 1 and p in c["unproved_live"] and
                    all(row["identity"]["pid"] != p["pid"] for row in c["measurements"]) for c in cs) and
                len(entries(s, "coverage_history")) == 3 and not kills)
    elif case == "st_ident_main_initial_invalid":
        require("invalid_initial_credentials_cannot_authorize_TERM_or_GO", code(last) is None and s["ident"] is None and
                s["group"] is None and s["rec"]["main_initial_identity_observed"]["euid"] == 0 and not kills and
                s["signal"]["why_not"] == "NO_IDENTITY" and s["rec"].get("go_delivered") is not True and s["rc"] is None)
        require("invalid_main_remains_explicitly_unsettled", set(s["failure_codes"]) ==
                {"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED", "GRACE_EXPIRED_AFTER_STOP_REQUEST"} and
                s["loop_status"] == "GRACE_EXPIRED_AFTER_STOP_REQUEST" and any(p["pid"] == 700000010 for p in m["live_model_processes"]))
    elif case == "st_ident_helper_signal_changed":
        h = s["helpers"][-1]
        require("helper_mismatch_refuses_once_only_TERM", all(code(x) is None for x in steps) and h["term_attempted"] is True and
                h["signal"]["identity_ok"] is False and h["signal"]["sent"] is False and not kills and
                "HELPER_SIGNAL_IDENTITY_CHANGED" in h["signal"]["reason"] and
                h["signal"]["identity_observed"] == i["after"] and h["identity"] == i["before"])
        require("raw_helper_cleanup_is_not_settlement", h["clockless_probe_count"] == 1 and not h["settled"] and
                not h["leader_reaped"] and len([x for x in waits if x["pid"] == h["pid"]]) == 1)
    elif case.startswith("st_clock_") or case in ("st_acq_main_identity_end_clock", "st_acq_reap_mono_clock"):
        summaries = [decode(line.encode()) for line in m["stdout"].splitlines()]
        require("sticky_clock_failure_never_ACKs_SETTLED_or_exit0", s["timing_failed"] is True and code(last) is None and
                last["return"] == 13 and len(summaries) == 1 and summaries[0]["acknowledged"] is False and
                summaries[0]["exit_code"] == 13 and summaries[0]["reason"] == "TIMING_EVIDENCE_UNAVAILABLE" and
                s["publication_payload_bytes"] is None and s["publication_resources"] is None and s["ack_resources"] is None and not m["artifacts"])
        require("clock_exception_type_not_broadened", any(r["exception_type"] == "ModelClockUnavailable" and
                r["returned"] is None and r["action"] == "raise" for r in m["clock_rules"]) and s["cancellation_target_installed"] is True)
        if case.startswith("st_clock_cancel_"):
            require("cancel_latched_before_failed_timing", s["cancel"]["mono"] is None and
                    s["cancel"]["clock_error"] == "ModelClockUnavailable" and s["failure_codes"] == ["TIMING_EVIDENCE_UNAVAILABLE"])
            if case.endswith("before_target"):
                require("early_cancel_propagates_after_target_installation", s["cancel"]["signal"] == int(signal.SIGHUP) and
                        i["target_at_handler"] is None and code(steps[1]) == "TIMING_EVIDENCE_UNAVAILABLE_NO_SCAN_RETRY" and
                        code(steps[2]) == "TIMING_EVIDENCE_UNAVAILABLE" and not waits and not kills)
            else:
                require("installed_cancel_target_immediately_sticky", i["immediate_handler_timing_failed"] is True and
                        s["cancel"]["signal"] == int(signal.SIGTERM) and s["cancel_handled"] is True and
                        [x["returned"] for x in main_waits] == [[0, 0], [700000010, 15]] and len(kills) == 1)
        elif case == "st_acq_main_identity_end_clock":
            initial = next(r for r in raw if r["source"] == "main_recovery")
            require("identity_installed_before_failed_end_clock", initial["native_returned"] is True and initial["identity"] == s["ident"] and
                    initial["mono_end"] is None and initial["mono_end_error"] == "ModelClockUnavailable" and
                    s["rec"]["main_initial_identity_interval"] == [initial["mono_begin"], None] and set(s["failure_codes"]) ==
                    {"TIMING_EVIDENCE_UNAVAILABLE", "IDENTITY_TIMING_UNAVAILABLE", "POST_SPAWN_FAILURE"} and
                    s["signal"]["sent"] is True and s["signal"]["identity_ok"] is True and len(kills) == len(main_waits) == 1 and s["rc"] == -15)
        elif case == "st_acq_reap_mono_clock":
            w = s["main_wait"]
            require("destructive_reap_survives_null_auxiliary_exit_clock", s["failure_codes"] == ["TIMING_EVIDENCE_UNAVAILABLE"] and
                    s["rc"] == 0 and w["leader_reaped"] is True and w["native_wait_result"] == [700000010, 0] and
                    w["raw_wait_status"] == 0 and s["exit_mono"] is None and w["mono_reaped_error"] == "ModelClockUnavailable" and
                    s["exit_epoch"] is not None and len(main_waits) == 1 and not kills and code(steps[2]) == "CLEANUP_DEADLINE_UNVERIFIABLE")
        else:
            recovery, before, prior = case == "st_clock_recovery_post_wait", "before_wait" in case, case.endswith("_prior_stop")
            expected_codes = {"MAIN_RUNTIME_CLOCK_UNAVAILABLE"} | ({"POST_SPAWN_FAILURE"} if recovery else set())
            expected_rc = None if before and prior else -15 if before or recovery else 0
            require("exact_runtime_clock_failure_and_retained_wait", set(s["failure_codes"]) == expected_codes and
                    s["rc"] == expected_rc and not s["lost_wait"] and
                    (s["stop"] == i["prior_stop"] if prior else s["stop"]["reason"] == "FAILURE"))
            require("postwait_containment_never_rewaits_consumed_status", len(main_waits) == (3 if before and prior else 1) and
                    (all(x["returned"] == [0, 0] for x in main_waits) if expected_rc is None else
                     s["main_wait"]["leader_reaped"] is True and s["main_wait"]["rc"] == expected_rc))
            require("no_extra_TERM_or_renewed_stop", len(kills) == (1 if recovery or before and not prior else 0))
            row = next(row for row in s["failures"] if row["code"] == "MAIN_RUNTIME_CLOCK_UNAVAILABLE")
            require("runtime_failure_location_retained", ("after_waitpid_including_success" in row["detail"]) is (not before) and
                    "ModelClockUnavailable" in row["detail"])
    elif case in ("st_acq_task_end_clock_rss", "st_acq_final_bracket_end_clock_rss"):
        cs = entries(s, "census_history")
        c, measured = cs[-2], cs[-2]["measurements"][-1]
        require("completed_RSS_composite_precedes_failed_timing", code(steps[0]) == "RESOURCE_TIMING_UNAVAILABLE" and
                s["timing_failed"] is True and measured["bracket_verified"] is True and measured["identity_after"] == measured["identity"] and
                measured["rss"] > cfg["rss_trip_bytes"] and measured["busy"] is None and measured["identity_after_event_ref"] is None and
                c["lane_rss"] == sum(row["rss"] for row in c["measurements"]) and "RSS" in s["trips"] and s["maxima"]["lane_rss"] >= c["lane_rss"])
        require("missing_clock_honest_null_and_exact_failures", set(s["failure_codes"]) ==
                {"TIMING_EVIDENCE_UNAVAILABLE", "RESOURCE_TIMING_UNAVAILABLE", "RESOURCE_ACQUISITION_INCOMPLETE"} and
                (measured["mono_task_end"] is None if case == "st_acq_task_end_clock_rss" else measured["identity_after_interval"][1] is None) and
                any(r["kind"] == "task" and r["native_returned"] and r["native_result"][0] == measured["rss"] for r in raw))
        require("abort_records_and_sticky_no_scan_resume", c["aborted"] and not c["complete"] and c["mono_end"] is not None and
                code(steps[1]) == "TIMING_EVIDENCE_UNAVAILABLE_NO_SCAN_RETRY" and
                not any(x["operation"].startswith("proc_") for x in ops[steps[1]["event_begin"]:steps[1]["event_end"]]) and not kills)
    elif case in ("st_acq_accounting_late_return", "st_acq_accounting_observed_clock"):
        event, clock = s["accounting_observations"][-1], case.endswith("_clock")
        require("native_free_retained_before_completion_refusal", len(s["accounting_observations"]) == 1 and
                event["resources"]["free"] == i["free"] == s["last_native_free"]["free"] and event["retained"] is True and
                event["returned"] is False and s["min_free"] == i["free"] and s["min_free_witness"] == event == s["last_accounting_observation"] and
                s["publication_resources"] is None and s["ack_resources"] is None)
        require("exact_accounting_failure_not_success_by_exception", code(steps[0]) ==
                ("ACCOUNTING_COMPLETION_TIME_UNAVAILABLE" if clock else "DEADLINE_EXCEEDED") and steps[0]["return"] is None and
                (event["mono_observed"] is None if clock else event["mono_begin"] <= event["mono_observed"] <= i["deadline"] < steps[0]["after"]["mono"]))
        require("accounting_clock_failure_sticky_no_retry", (s["timing_failed"] is True and
                s["failure_codes"] == ["TIMING_EVIDENCE_UNAVAILABLE"] and code(steps[1]) == "TIMING_EVIDENCE_UNAVAILABLE_NO_ACCOUNTING_RETRY" and
                steps[1]["event_begin"] == steps[1]["event_end"]) if clock else (s["timing_failed"] is False and s["failure_codes"] == []))
    elif case == "st_write_progress_late":
        writes = [x for x in ops if x["operation"] == "write"]
        require("returned_prefix_callback_precedes_deadline_check", code(last) == "DEADLINE_EXCEEDED" and len(writes) == 1 and
                writes[0]["mono_before"] < i["deadline"] < writes[0]["mono_after"] and writes[0]["returned"] == len(bytes.fromhex(i["data_hex"])) and
                i["data_hex"] == i["progress_hex"] == i["result_data_hex"] and writes[0]["response_scope"] == "API_RESPONSE_INJECTION")
    elif case.startswith("st_cap_raw_"):
        desired, cap = i["requested_post_count"], i["cap"]["value"]
        require("raw_cap_case_delta_bound", desired == 128 + {"lt": -1, "eq": 0, "gt": 1}[case.rsplit("_", 1)[1]])
        overflow = desired > cap
        require("raw_acquisition_limit_minus_one_equal_plus_one", cap == 128 and len(raw) == min(desired, cap) and
                all(r["native_returned"] and r["identity"] is not None for r in raw) and code(last) == ("RAW_ACQUISITION_CAP" if overflow else None) and
                s["failure_codes"] == (["RAW_ACQUISITION_CAP"] if overflow else []) and not s["history_halted"])
        if overflow:
            require("raw_cap_refuses_before_additional_native_model_acquisition",
                    not any(x["operation"].startswith("proc_") for x in ops[last["event_begin"]:last["event_end"]]))
    elif case.startswith("st_cap_clockless_"):
        h, expected = s["helpers"][-1], min(i["requested_post_count"], 3)
        require("clockless_cap_case_delta_bound", i["requested_post_count"] == 3 + {"lt": -1, "eq": 0, "gt": 1}[case.rsplit("_", 1)[1]])
        require("clockless_cleanup_finite_raw_pass_limit", i["cap"]["value"] == 3 and h["clockless_probe_count"] == expected and
                h["settled"] is False and h["leader_reaped"] is False and not kills and
                len([x for x in waits if x["pid"] == h["pid"]]) == expected and all(code(x) is None for x in steps))
        if i["requested_post_count"] > 3:
            require("clockless_cap_no_extra_raw_work", last["event_begin"] == last["event_end"])
    else:
        raise Invalid("added independent raw-state predicate absent")


def evaluate(case, outcome, capture, captures, sources):
    checks = {}
    def require(label, condition):
        checks[label] = bool(condition)
    require("external_actual_driver_exit_exactly_0_never_120", capture["actual_exit"] == 0)
    require("full_native_driver_stderr_empty", captures["stderr"]["bytes"] == 0)
    require("driver_does_not_claim_actualexit_or_terminal14", outcome["source_outcome"]["actual_exit"] is None and
            outcome["source_outcome"]["native_supervisor_terminal14_exercised"] is False and
            outcome["source_outcome"]["fixture_identity"] == "MODIFIED_QUALIFICATION_FIXTURE")
    require("native_obligations_remain_open", outcome["unresolved"]["native_coverage"] == "NOT_EXERCISED" and
            outcome["unresolved"]["native_children_created"] == [] and outcome["unresolved"]["release"] is None and
            outcome["unresolved"]["science_acceptance"] is None and outcome["accounting"]["native_payload"] is None)
    if outcome["source_outcome"]["status"] != "RECORDED" or outcome.get("model") is None:
        return checks, "NOT_EXERCISED" if outcome["source_outcome"]["status"] == "NOT_EXERCISED" else "HOLD"
    encoded = outcome["model"]
    verify_source(encoded, sources["supervisor"])
    m = restore(encoded)
    i, s, steps, ops = m["inputs"], observation_state(m), m["steps"], m["operations"]
    cfg = m["config"]
    require("declared_model_scope_no_backend_escape", m["scope"] == "MODEL_INPUT_NOT_NATIVE" and m["violations"] == [])
    require("native_cooperative_budget", outcome["owner"]["mono_end"] - outcome["owner"]["mono_begin"] <= 280 and
            all(x["rss_peak_bytes"] <= 256 << 20 for x in outcome["observations"] if x.get("kind") == "owner_runtime"))
    native = next(x for x in outcome["observations"] if x.get("kind") == "owner_runtime")
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
    require("model_artifact_bytes_explicitly_not_actual_date", all(
            a["scope"] == "MODEL_INPUT_NOT_ACTUAL_BIN_DATE" and a["artifact_scope"] == "MODEL_ARTIFACT_NOT_NATIVE" and
            hashlib.sha256(bytes.fromhex(a["data_hex"])).hexdigest() == a["sha256"]
            for a in m["artifacts"].values()))
    if case.startswith(("st_complete_", "st_ident_", "st_clock_", "st_acq_", "st_cap_raw_", "st_cap_clockless_")) or case == "st_write_progress_late":
        evaluate_added(case, m, s, cfg, require)
        return checks, None
    last = steps[-1]
    delta = {"lt": -0.01, "eq": 0.0, "gt": 0.01}.get(case.rsplit("_", 1)[-1])
    if case.startswith("st_runtime_"):
        target = {"st_runtime_999": 9.99, "st_runtime_1000": 10.0, "st_runtime_1026": 10.26}[case]
        deadline = i["mono_spawn"] + i["max_wall_s"]
        waits = [x for x in ops if x["operation"] == "waitpid" and x["pid"] == s["pid"]]
        trip = i["wait_return_mono"] >= deadline
        late = i["wait_return_mono"] > deadline + i["sample_s"] + 0.05
        require("runtime_inputs_bind_actual_model_state", i["mono_spawn"] == s["mono_spawn"] == 1000.0 and
                i["max_wall_s"] == cfg["max_wall_s"] and i["sample_s"] == cfg["sample_s"])
        require("successful_late_return_model_wait_raw_order", len(waits) == 1 and waits[0]["returned"] == [s["pid"], 0] and
                waits[0]["mono_before"] < deadline and near(waits[0]["mono_after"] - i["mono_spawn"], target))
        require("reaped_state_not_erased", s["rc"] == 0 and near(s["exit_mono"], i["wait_return_mono"]) and not s["lost_wait"])
        require("runtime_exact_threshold_and_lateness", set(s["trips"]) == ({"DEADLINE"} if trip else set()) and
                set(s["failure_codes"]) == ({"MAIN_DEADLINE_ENFORCEMENT_LATE"} if late else set()))
        require("deadline_after_successful_reap_retained", not trip or len(s["runtime_observations"]) == 1 and
                s["runtime_observations"][0]["where"] == "after_waitpid_including_success" and
                s["runtime_observations"][0]["mono_deadline"] == deadline)
        require("reaped_main_never_signalled", not [x for x in ops if x["operation"] == "killpg"] and
                (not trip or s["signal"]["why_not"] == "CHILD_ALREADY_REAPED"))
        require("original_reap_returns", code(last) is None)
    elif case.startswith("st_go_"):
        completion = s["rec"]["go_delivery_completion"]
        bound = min(60.0, i["max_wall_s"] / 2.0)
        age = i["observed_mono"] - i["mono_spawn"]
        remaining = i["mono_spawn"] + i["max_wall_s"] - i["observed_mono"]
        require("GO_inputs_bind_actual_model_state", i["mono_spawn"] == s["mono_spawn"] == 1000.0 and
                i["max_wall_s"] == cfg["max_wall_s"])
        bad = age > bound or remaining <= 0
        require("actual_original_completion_fields", near(age, bound + delta) and completion["mono"] == i["observed_mono"] and
                near(completion["spawn_age_s"], age) and completion["spawn_age_bound_s"] == bound and
                near(completion["remaining_main_runtime_s"], remaining))
        require("GO_boundary_exception", code(last) == ("LATE_ACTUAL_GO_DELIVERY_OWNED_STOP" if bad else None))
        require("GO_age_latch_and_stop", set(s["failure_codes"]) == ({"GO_COMPLETION_AGE_EXCEEDED"} if bad else set()) and
                ((s["stop"] is not None and s["signal"]["sent"] and len([x for x in ops if x["operation"] == "killpg"]) == 1) if bad else s["stop"] is None))
    elif case.startswith("st_age_"):
        base = i["observation"]["epoch_date_floor"] - i["stability_epoch"]
        upper = max(base + 1.0 + max(0.0, i["mono"] - i["observation"]["mono_before_read"]), i["max_age"] + i["mono"] - i["expiry"])
        require("stability_inputs_bind_retained_state", i["observation"] == s["clock_observation"] and
                i["stability_epoch"] == s["authorization"]["stability_epoch"] and i["expiry"] == s["stability_expiry_mono"] and
                i["max_age"] == cfg["admission"]["stability_max_age_s"])
        require("conservative_upper_independently_recomputed", near(upper, 300.0 + delta))
        require("stability_exact_strict_greater", code(last) == ("STABILITY_STALE" if upper > i["max_age"] else None) and
                (upper > i["max_age"] or near(last["return"], upper)))
    elif case in ("st_date_missing", "st_date_malformed", "st_date_naive"):
        expected = "STABILITY_TIMESTAMP_MISSING" if case == "st_date_missing" else "ValueError"
        require("original_parser_refuses_exact_exception", code(last) == expected and last["return"] is None)
        require("synthetic_parser_text_not_actual_bin_date", encoded["steps"][-1]["exception"]["text"]["encoding"] == "UTF8_HEX")
    elif case == "st_date_future":
        helper = s["helpers"][-1]
        text = bytes.fromhex(helper["capture_hex"]).decode("ascii").strip()
        parsed = datetime.datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
        require("future_branch_binds_raw_MODEL_capture", parsed.timestamp() == i["model_epoch_floor"] and
                helper["date"] == text and i["receipt_stability_epoch"] == s["authorization"]["stability_epoch"])
        require("future_input_really_future", i["model_epoch_floor"] < i["receipt_stability_epoch"])
        require("original_future_branch_latches_failure", last["return"] is None and s["failure_codes"] == ["HELPER_CALL_FAILED"] and
                "STABILITY_TIMESTAMP_IN_FUTURE" in s["helper_log"][-1]["error"])
        require("future_does_not_install_fresh_clock", s["clock_observation"] is None and s["stability_expiry_mono"] is None)
    elif case.startswith("st_stability_"):
        first, second = i["first"], i["second"]
        obs = second["observation"]
        candidate = obs["mono_before_read"] + i["max_age"] - (obs["epoch_date_floor"] - i["stability_epoch"] + 1.0)
        effective = min(first["expiry"], candidate)
        require("nonrenewing_min_recomputed", near(second["expiry"], effective) and near(s["stability_expiry_mono"], effective))
        require("declared_rollback_refresh_or_tighten_hit", candidate < first["expiry"] if case.endswith("tighten") else candidate > first["expiry"])
        require("later_observation_cannot_restore_expired_freshness", i["later_check_mono"] > effective and code(last) == "STABILITY_STALE" and
                steps[0]["exception"] is None and s["failure_codes"] == [])
    elif case.startswith("st_ack_age_"):
        age = i["mono"] - i["census"]["mono_complete"]
        limit = max(1.0, i["sample_s"])
        require("ACK_age_binds_real_retained_census", i["census"] == entries(s, "census_history")[-1] and
                i["sample_s"] == cfg["sample_s"])
        require("ACK_census_actual_model_age", near(age, limit + delta) and i["census"]["complete"] is True)
        require("ACK_census_strict_staleness", code(last) == ("RESOURCE_CENSUS_STALE_AT_COMMIT" if age > limit else None))
    elif case.startswith("st_retry_"):
        censuses = [c for c in entries(s, "census_history") if not c["inside_helper"] and c["phase"] == "RUNNING"]
        require("incomplete_then_clean_actual_original_retries", len(censuses) == 2 and not censuses[0]["complete"] and
                censuses[0]["incomplete_n"] > 0 and censuses[1]["complete"] and censuses[1]["incomplete_n"] == 0 and code(last) is None)
        require("aborted_coverage_retained", len(entries(s, "coverage_history")) >= 1 and s["stop"] == i["previous_stop"])
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
        if i["mode"] == "unproved":
            unknown = [p["uniqueid"] for p in censuses[0]["unproved_live"]]
            history = entries(s, "unproved_history")
            require("transient_U_survives_clean_retry", i["transient_unproved_uid"] in unknown and not censuses[1]["unproved_live"] and
                    any(p["last_identity"]["uniqueid"] == i["transient_unproved_uid"] for p in history))
        elif i["mode"] == "busy":
            require("transient_BUSY_excess_latched", censuses[0]["lane_busy"] > i["busy_limit"] and censuses[1]["lane_busy"] <= i["busy_limit"] and
                    "BUSY" in s["trips"] and s["maxima"]["lane_busy"] >= censuses[0]["lane_busy"])
        else:
            require("transient_RSS_excess_latched", censuses[0]["lane_rss"] > i["rss_limit"] and censuses[1]["lane_rss"] <= i["rss_limit"] and
                    "RSS" in s["trips"] and s["maxima"]["lane_rss"] >= censuses[0]["lane_rss"])
    elif case.startswith("st_abort_"):
        attempts = entries(s, "attempt_history")
        kind = "identity_scan" if case.endswith("identity") else "resource_scan"
        aborted = [a for a in attempts if a["kind"] == kind and a["aborted"]]
        require("abort_and_end_not_discarded", len(aborted) == 1 and aborted[0]["mono_end"] >= aborted[0]["mono_start"] and
                aborted[0]["error"] is not None and code(last) == "DEADLINE_EXCEEDED")
        if case.endswith("resource"):
            record = entries(s, "census_history")[-1]
            require("resource_partial_composite_survives_abort", record["aborted"] and not record["complete"] and record["mono_end"] is not None and
                    record["measurements"] and record["lane_rss"] == sum(x["rss"] for x in record["measurements"]))
    elif case.startswith("st_cap_bytes_"):
        expected_charge = 2 * len(json.dumps(i["entry"], sort_keys=True, separators=(",", ":"), allow_nan=False).encode()) + 64
        attempted = i["precharge"] + expected_charge
        overflow = attempted > i["cap"]["value"]
        require("byte_charge_formula_recomputed", expected_charge == i["charge"] and attempted == i["attempted_charge"] and
                attempted == i["cap"]["value"] + int(delta * 100))
        require("strict_byte_cap_branch", code(last) == ("HISTORY_BYTE_CAP" if overflow else None) and s["history_halted"] is overflow and
                s["history_charge"] == (i["precharge"] if overflow else attempted))
        require("byte_overflow_witness_not_truncated", not overflow or s["history_overflow"]["witness"] == {"observation": i["entry"]["observation"]})
    elif case in ("st_cap_final_rss", "st_cap_initial_main", "st_cap_helper_term"):
        overflow = s["history_overflow"]
        require("real_cap_branch_not_overflowflag_only", s["history_halted"] is True and overflow["kind"] == "HISTORY_BYTE_CAP" and
                "HISTORY_BYTE_CAP" in s["failure_codes"] and m["checkpoint"] is not None)
        exact_codes = {
            "st_cap_final_rss": {"HISTORY_BYTE_CAP", "RESOURCE_ACQUISITION_INCOMPLETE"},
            "st_cap_initial_main": {"HISTORY_BYTE_CAP", "POST_SPAWN_FAILURE", "GO_NOT_DELIVERED", "OBSERVATION_FAILED",
                                    "GRACE_EXPIRED_AFTER_STOP_REQUEST"},
            "st_cap_helper_term": {"HISTORY_BYTE_CAP", "HELPER_CALL_FAILED", "HELPER_OWNERSHIP_UNSETTLED"}}
        require("critical_cap_exact_v19_failure_set", set(s["failure_codes"]) == exact_codes[case])
        require("calibration_only_selects_initial_state", i["declared_precharge"] + i["calibration"]["target"]["history_charge_before"] -
                i["calibration"]["baseline_charge"] == i["cap"]["value"] and m["checkpoint"]["history_charge_before"] == i["cap"]["value"])
        if case == "st_cap_final_rss":
            c = entries(s, "census_history")[-1]
            measured = overflow["completed_measurement"]
            require("completed_RSS_identity_composite_survives", measured in c["measurements"] and measured["identity_after"] == measured["identity"] and
                    measured["rss"] > cfg["rss_trip_bytes"] and c["lane_rss"] >= measured["rss"] and "RSS" in s["trips"] and
                    s["maxima"]["lane_rss"] >= c["lane_rss"])
            require("cap_abort_end_and_no_resumed_scan", c["aborted"] and not c["complete"] and c["mono_end"] is not None and
                    code(steps[0]) == "HISTORY_BYTE_CAP" and code(steps[1]) == "HISTORY_ALREADY_HALTED" and
                    steps[1]["counts_before"] == steps[1]["counts_after"] and
                    not any(x["operation"].startswith("proc_") for x in ops[steps[1]["event_begin"]:steps[1]["event_end"]]))
        elif case == "st_cap_initial_main":
            ident = s["rec"]["main_initial_identity_observed"]
            signals = [x for x in ops if x["operation"] == "killpg" and x["pgid"] == ident["pgid"]]
            require("cleanup_identity_installed_before_retention_failure", s["ident"] == ident and s["group"] == ident["pgid"] == s["pid"] and
                    overflow["witness"]["identity"] == ident and overflow["completed_identity_observation"]["identity"] == ident and
                    s["rec"]["main_initial_identity_interval"] ==
                    [overflow["completed_identity_observation"]["mono_begin"], overflow["completed_identity_observation"]["mono_end"]] and
                    s["signal"]["identity_observed"] == ident and s["signal"]["identity_ok"] is True and
                    s["signal"]["sent"] is True and len(signals) == 1 and s["rc"] == -int(signal.SIGTERM))
            require("initial_cap_no_GO_or_hidden_launch_success", s["rec"].get("go_delivered") is not True and
                    {"POST_SPAWN_FAILURE", "GO_NOT_DELIVERED", "OBSERVATION_FAILED"} <= set(s["failure_codes"]))
        else:
            h = s["helpers"][-1]
            sig = h["signal"]
            signals = [x for x in ops if x["operation"] == "killpg" and x["pgid"] == h["identity"]["pgid"]]
            require("helper_TERM_witness_survives_success_update", h["term_attempted"] is True and len(signals) == 1 and
                    sig["sent"] is True and sig["identity_ok"] is True and sig["identity_observed"] == h["identity"] and
                    sig["mono_check"] <= sig["mono_identity_observed"] <= sig["mono_sent"])
            require("helper_reap_does_not_fake_settlement_after_cap", h["leader_reaped"] is True and h["rc"] == -int(signal.SIGTERM) and
                    h["settled"] is False and "HELPER_OWNERSHIP_UNSETTLED" in s["failure_codes"])
    elif case.startswith("st_cap_"):
        family, cap, desired, pre = i["family"], i["cap"]["value"], i["requested_post_count"], i["pre_count"]
        overflow = pre >= cap
        codes = {"identity": "IDENTITY_HISTORY_CAP", "unproved": "UNPROVED_HISTORY_CAP", "coverage": "COVERAGE_HISTORY_CAP",
                 "attempt": "ATTEMPT_HISTORY_CAP", "census": "CENSUS_HISTORY_CAP", "variants": "IDENTITY_VARIANT_CAP"}
        if family == "variants":
            records = entries(s, "identity_history")
            count = len(records[-1]["variants"])
        else:
            name = {"identity": "identity_history", "unproved": "unproved_history", "coverage": "coverage_history",
                    "attempt": "attempt_history", "census": "census_history"}[family]
            count = s["histories"][name]["count"]
        require("original_count_cap_exact_attempted_count", desired == cap + int(delta * 100) and pre == desired - 1 and
                count == (pre if overflow else desired))
        require("count_cap_exception_and_halt", code(last) == (codes[family] if overflow else None) and s["history_halted"] is overflow)
        require("count_state_reachability_honestly_disclosed", family == "variants" or i["prestate_byte_charge_reset"] is True and
                any("NOT physical/native coverage" in text for text in m["disclosures"]))
    elif case.startswith("st_budget_output_"):
        payload = s["publication_payload_bytes"]
        b = s["publication_resources"]
        total = b["charged_bytes"] + payload
        expected_code = 10 if total <= cfg["output_trip_bytes"] else 12
        require("exact_actual_serialized_payload_total_boundary", total == cfg["output_trip_bytes"] + i["delta"] and payload == i["payload_bytes"])
        summaries = [decode(line.encode()) for line in m["stdout"].splitlines()]
        require("original_final_body_exact_status_not_blanket_success", code(last) is None and last["return"] == expected_code and
                len(summaries) == 1 and summaries[0]["exit_code"] == expected_code and
                (summaries[0]["acknowledged"] is True if expected_code == 10 else summaries[0]["reason"] == "PUBLICATION_REFUSED"))
        if expected_code == 10:
            summary = summaries[0]
            artifacts = m["artifacts"]
            rb = bytes.fromhex(artifacts[cfg["receipt"]]["data_hex"])
            sb = bytes.fromhex(artifacts[cfg["settlement_record"]]["data_hex"])
            require("independent_exact_payload_and_inode_artifacts", len(rb) + len(sb) == payload and
                    hashlib.sha256(rb).hexdigest() == summary["receipt_sha256"] and
                    hashlib.sha256(sb).hexdigest() == summary["settlement_record_sha256"] and
                    artifacts[cfg["settlement_record"]]["inode"] == artifacts[cfg["settlement_record"] + ".staged"]["inode"])
        else:
            require("publication_refusal_has_no_fabricated_end", s["ack_resources"] is None and not m["artifacts"])
    elif case.startswith("st_budget_"):
        a, adm, payload = i["resources"], i["admission"], i["payload"]
        require("budget_inputs_bind_fixed_model_config", adm == cfg["admission"] and payload == 100 and
                i["free_trip_bytes"] == cfg["free_trip_bytes"] and i["lane_ceiling"] == cfg["lane_disk_ceiling_bytes"])
        remaining = max(0, adm["reservation_bytes"] - a["charged_bytes"] - payload)
        predicates = [a["charged_bytes"] + payload <= adm["reservation_bytes"],
                      a["free"] - payload - adm["outstanding_reservations_bytes"] - remaining >= i["free_trip_bytes"],
                      a["lane_bytes"] + payload + adm["lane_outstanding_reservations_bytes"] + remaining <= i["lane_ceiling"]]
        require("reservation_FREE_LANE_predicates_recomputed", code(last) is None and last["return"] is all(predicates))
        family = i["family"]
        relation = {"reservation": a["charged_bytes"] + payload - adm["reservation_bytes"],
                    "free": a["free"] - payload - adm["outstanding_reservations_bytes"] - remaining - i["free_trip_bytes"],
                    "lane": a["lane_bytes"] + payload + adm["lane_outstanding_reservations_bytes"] + remaining - i["lane_ceiling"]}[family]
        require("exact_isolated_budget_boundary", relation == i["delta"])
    elif case.startswith("st_cutoff_census_"):
        c = entries(s, "census_history")[-1]
        require("census_completion_boundary_measured_in_model", near(c["measurements"][-1]["mono_observed"], i["deadline"] + delta))
        require("census_deadline_equality_allowed_late_aborts", code(last) == ("DEADLINE_EXCEEDED" if delta > 0 else None) and
                c["complete"] is (delta <= 0) and c["aborted"] is (delta > 0) and c["mono_end"] is not None)
    elif case.startswith("st_cutoff_helper_"):
        h = s["helpers"][-1]
        require("helper_successful_reap_observed_but_completion_timed", h["leader_reaped"] is True and h["rc"] == 0 and
                near(h["mono_proof_complete"], i["deadline"] + delta) and h["mono_call_deadline"] == i["deadline"])
        require("helper_late_success_not_accepted", (last["return"] is None and "HELPER_CALL_FAILED" in s["failure_codes"]) if delta > 0 else
                (type(last["return"]) is str and s["failure_codes"] == []))
    elif case.startswith("st_cutoff_stop_grace_") or case.startswith("st_cutoff_exit_grace_"):
        expected = "GRACE_EXPIRED_AFTER_STOP_REQUEST" if "stop_grace" in case else "GRACE_EXPIRED_AFTER_CHILD_EXIT"
        require("fresh_all_predicate_timestamp_not_census_backdate", last["return"] is True and code(last) is None and
                ((s["clear"] is None and expected in s["failure_codes"] and s["loop_status"] == expected) if delta > 0 else
                 (s["clear"] is not None and near(s["clear"]["mono_all_predicates_verified"], i["deadline"] + delta) and
                  s["clear"]["mono_all_predicates_verified"] >= s["clear"]["census"]["mono_complete"] and s["loop_status"] == "EXITED")))
    elif case.startswith("st_cutoff_finalize_"):
        require("finalization_constant_and_exact_completion_cutoff", i["seconds"] == 120.0 and
                near(i["observed_mono"], i["deadline"] + delta) and code(last) == ("DEADLINE_EXCEEDED" if delta > 0 else None))
    elif case.startswith("st_write_"):
        writes = [x for x in ops if x["operation"] == "write"]
        data = bytes.fromhex(i["data_hex"])
        returned = bytes.fromhex(i["result_data_hex"])
        require("all_write_returns_explicit_API_response_model", writes and all(x["response_scope"] == "API_RESPONSE_INJECTION" for x in writes))
        if case == "st_write_short":
            require("real_write_all_retries_remaining_buffer", len(writes) > 1 and code(last) is None and returned == data and
                    sum(x["returned"] for x in writes) == len(data) and writes[0]["returned"] < writes[0]["requested"] and
                    all(writes[n + 1]["requested"] == writes[n]["requested"] - writes[n]["returned"] for n in range(len(writes) - 1)))
        elif case == "st_write_zero":
            require("zero_progress_not_accepted", len(writes) == 1 and writes[0]["returned"] == 0 and returned == b"" and code(last) == "ZERO_PROGRESS_WRITE")
        else:
            require("successful_late_write_rejected_after_return", len(writes) == 1 and writes[0]["mono_before"] < i["deadline"] < writes[0]["mono_after"] and
                    writes[0]["returned"] == len(data) and returned == data and code(last) == "DEADLINE_EXCEEDED")
    elif case.startswith("st_manifest_"):
        prep = i["preparation"]
        manifest = {"kind": "qualification-creation-manifest-v1", "scenario": "mutate_pin",
                    "preparation_sha256": cfg["creation_channel"]["preparation_sha256"], "run": prep["run"],
                    "output_root": prep["output_root"], "target": i["actual_original_target"]}
        line = canon(manifest)
        target = int(case.rsplit("_", 1)[1])
        require("exact_canonical_manifest_length_recomputed", len(line) == target and i["target_length"] == target)
        require("manifest_exact_4096_cap_not_native_path_claim", code(last) == ("CREATION_MANIFEST_BYTE_CAP" if target > 4096 else None) and
                (("go_creation_manifest" not in s["rec"]) if target > 4096 else
                 (last["return"] == line and s["rec"]["go_creation_manifest"] == manifest and
                  s["rec"]["go_creation_manifest_sha256"] == hashlib.sha256(line).hexdigest())))
    elif case == "st_cancel_pending_after_handled":
        require("earlier_handled_cancel_does_not_hide_new_pending", len(steps) == 2 and code(steps[0]) is None and
                code(steps[1]) == "CANCEL_DURING_ACK_COMPLETION" and s["cancel_handled"] is True and
                i["new_pending_signal"] in s["pending_signals"] and s["cancel"]["signal"] == i["handled_signal"])
    else:
        raise Invalid("independent case predicate dispatch absent")
    return checks, None


def main():
    if sys.platform != "darwin" or os.path.abspath(__file__) != ORACLE or os.path.realpath(__file__) != ORACLE or \
            len(sys.argv) != 4 or sys.argv[1] not in CASES or not hex64(sys.argv[2]) or not hex64(sys.argv[3]):
        raise Invalid("fixed oracle CASE_ID APPROVAL_SHA PARENT_CAPTURE_SHA interface")
    case, approval, capture = sys.argv[1:]
    budget = Budget()
    runfd = directory(ROOT + "/" + case)
    try:
        outcome, cp, captures, sources, spec, outcome_file = exact_authority(case, approval, capture, runfd, budget)
        checks, forced = evaluate(case, outcome, cp, captures, sources)
        verdict = forced or ("FIXTURE_PREDICATES_MET" if all(checks.values()) else "NOT_MET")
        if any(not checks[k] for k in checks if k.startswith("external_") or k.startswith("full_native_")):
            verdict = "NOT_MET"
        result = {"kind": "rqls10-state-oracle-v1", "case": case, "scope": SCOPE, "verdict": verdict,
                  "approval_sha256": approval, "capture_sha256": capture, "outcome_sha256": outcome_file["sha256"],
                  "criteria": checks, "native_coverage": "NOT_EXERCISED", "release": None, "science_acceptance": None,
                  "verification_boundary": {"event_counts": "Canonical retained tape replay except explicit count-isolation prestates",
                      "not_independently_recomputed_scalars": ["aggregate history_charge outside byte-cap case", "whole operation-trace hash with suppressed prefill"],
                      "pending_raw": "Incomplete evidence only, never substitute for a healthy interval, BUSY proof or settlement"},
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
