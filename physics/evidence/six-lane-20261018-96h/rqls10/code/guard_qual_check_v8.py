#!/usr/bin/env python3
"""V12 qualification successor. Restores owned bounded /bin/date and explicit ownership-negative controls.
Parent correction fabe57ab...4155a2 withdraws v10's narrowing; all earlier files remain immutable/unrun.
Usage: guard_qual_check_v8.py SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT
Fixed no-follow root, independent actual source/config/GO/stability/preparation/evidence hashes and trusted parent
approval digest. Exact outcome sets plus complete helper settlement predicates, all unproved/owned identity evidence,
PID-specific intended cause proofs, same-inode publication and whole-sample decoding. No PASS releases reservations.
Helper overrun/group/EOF branches are reviewed injections, not evidence of a real corrupted /bin/date or kernel.
Ownership workloads require their OWN negative-control GO, are not science and never weaken global busy<=2.
Exit0 PASS,1 FAIL,2 infrastructure error. No execution authorized by this source.
"""
import hashlib
import json
import math
import os
import datetime
import stat
import sys
import time

VERSION = "guard_qual_check_v8"
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v7-v12"
ITEM = "owned_supervisor_v12 restored ownership qualification"
CHILD = LANE + "/code/guard_qual_child_v9.py"
SUPERVISOR = LANE + "/code/owned_supervisor_v12.py"
WRITER = LANE + "/code/guard_qual_configs_v8.py"
CHILD_SHA = "6018262187adee7faab5891a16e33e78c1c9a4e4537f100b409260f78e8f51d8"
SUPERVISOR_SHA = "304748cc494a71b379094fa964c6ef41d2c3d59e31b19ad969a0ec8ae45ab9b4"
WRITER_SHA = "2a538618e811bcfede1658f9576ef8f4b0bdb449b52a7d79b4196b1c9b2be8e3"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
RESERVATION = 20971520

SC = {"go_unlisted": (60, 60, True, 2147483648), "ok": (60, 60, True, 2147483648),
      "rc_nonzero": (60, 60, True, 2147483648), "missing_output": (60, 60, True, 2147483648),
      "mutate_pin": (60, 60, True, 2147483648), "mutate_evidence": (60, 60, True, 2147483648),
      "stray_file": (60, 60, True, 2147483648), "deadline": (120, 10, False, 2147483648),
      "flood": (60, 60, False, 2147483648), "busy2": (60, 60, False, 2147483648),
      "rss": (60, 60, False, 268435456), "ignore": (60, 10, False, 2147483648),
      "identity": (60, 10, False, 2147483648), "date_fault": (60, 60, True, 2147483648),
      "helper_overrun": (60, 60, True, 2147483648), "helper_group": (60, 60, True, 2147483648),
      "helper_eof": (60, 60, True, 2147483648), "ownership_group": (40, 60, True, 2147483648),
      "ownership_slow": (40, 60, True, 2147483648), "ownership_fast": (40, 60, True, 2147483648),
      "ownership_double": (40, 60, True, 2147483648), "zombie_hold": (10, 60, True, 2147483648)}
FAULTS = {"identity": "identity_check_fails", "date_fault": "date_helper_fails",
          "helper_overrun": "helper_observation_overrun", "helper_group": "helper_group_unproved",
          "helper_eof": "helper_eof_unproved"}
NEGATIVE_PROCESS = {"busy2", "ownership_group", "ownership_slow", "ownership_fast", "ownership_double", "zombie_hold"}

def config_for(name, python, pysha, outstanding, lane_outstanding):
    life, wall, required, rss = SC[name]
    run, out = QROOT + "/" + name, QROOT + "/" + name + "/out"
    pins = [{"path": CHILD, "sha256": CHILD_SHA}, {"path": SUPERVISOR, "sha256": SUPERVISOR_SHA},
            {"path": python, "sha256": pysha}]
    if name == "mutate_pin":
        pins.append({"path": run + "/pinned-scratch.txt", "sha256": hashlib.sha256(FIXTURE).hexdigest()})
    call = 0.01 if name == "helper_overrun" else 0.2 if name in ("helper_group", "helper_eof") else 5.0
    return {"item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE,
            "argv": [python, "-I", "-B", CHILD, name, str(life)],
            "env": {"TMPDIR": run + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"},
            "stdout": out + "/stdout.txt", "stderr": out + "/stderr.txt", "stdout_cap_bytes": 1048576,
            "stderr_cap_bytes": 1048576, "samples": out + "/samples.jsonl", "samples_cap_bytes": 2097152,
            "launch_record": out + "/launch.json", "receipt": out + "/supervisor-receipt.json",
            "settlement_record": out + "/settlement.json", "outputs": [{"path": out + "/child-out.json", "required": required}],
            "output_roots": [out], "pins": pins, "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0,
            "max_chunk_seconds": 10800, "owned_compute_settled_by_epoch": 1792731393.0,
            "rss_trip_bytes": rss, "rss_projection_bytes": 67108864, "free_trip_bytes": 12200000000,
            "launch_free_min_bytes": 12200000000, "output_trip_bytes": 9437184, "lane_roots": [LANE],
            "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 5.0,
            "busy_limit": 1 if name == "busy2" else 2, "busy_cpu_fraction": 0.5,
            "cpu_slots": 2 if name == "busy2" else 1,
            "admission": {"go_path": run + "/go.json", "stability_receipt_path": run + "/stability.json",
                          "reservation_bytes": RESERVATION, "outstanding_reservations_bytes": outstanding,
                          "lane_outstanding_reservations_bytes": lane_outstanding, "stability_max_age_s": 300},
            "helper_budget": {"max_calls": 8, "call_budget_s": call,
                              "term_grace_s": 0.5 if name in ("helper_group", "helper_eof") else 5.0},
            "fault_injection": {FAULTS[name]: True} if name in FAULTS else {}}


class Invalid(Exception):
    pass


def integer(x, lower=None):
    return isinstance(x, int) and not isinstance(x, bool) and (lower is None or x >= lower)


def finite(x):
    return isinstance(x, (float, int)) and not isinstance(x, bool) and math.isfinite(x)


def pairs(kv):
    out = {}
    for k, v in kv:
        if k in out:
            raise Invalid("duplicate JSON key")
        out[k] = v
    return out


def floating(s):
    n = float(s)
    if not math.isfinite(n):
        raise Invalid("nonfinite numeric literal")
    return n


def constant(s):
    raise Invalid("nonfinite JSON constant")


DECODER = json.JSONDecoder(object_pairs_hook=pairs, parse_float=floating, parse_constant=constant)


def decode(raw):
    return DECODER.decode(raw.decode())


def sequence(raw):
    text, at, objects = raw.decode(), 0, []
    while at < len(text):
        while at < len(text) and text[at].isspace():
            at += 1
        if at == len(text):
            break
        obj, at = DECODER.raw_decode(text, at)
        if not isinstance(obj, dict):
            raise Invalid("sample is not an object")
        objects.append(obj)
    return objects


def directory(path):
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for c in path.lstrip("/").split("/"):
            if c in ("", ".", ".."):
                raise Invalid("invalid directory component")
            nxt = os.open(c, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def snapshot(fdroot, name, cap=64 << 20, optional=False):
    deadline = time.monotonic() + 30
    try:
        st = os.stat(name, dir_fd=fdroot, follow_symlinks=False)
    except FileNotFoundError:
        if optional:
            return None
        raise
    if not stat.S_ISREG(st.st_mode) or not 0 <= st.st_size <= cap:
        raise Invalid("not a bounded regular file: " + name)
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fdroot)
    try:
        s1 = os.fstat(fd)
        if (s1.st_dev, s1.st_ino, s1.st_size) != (st.st_dev, st.st_ino, st.st_size):
            raise Invalid("file changed at open")
        parts, n = [], 0
        while n < st.st_size:
            b = os.read(fd, min(1 << 20, st.st_size - n))
            if not b:
                raise Invalid("short read")
            parts.append(b)
            n += len(b)
            if time.monotonic() > deadline:
                raise Invalid("read deadline")
        tail, s2 = os.read(fd, 1), os.fstat(fd)
        if tail or (s2.st_size, s2.st_mtime_ns) != (st.st_size, st.st_mtime_ns):
            raise Invalid("file changed during read")
    finally:
        os.close(fd)
    if time.monotonic() > deadline:
        raise Invalid("read completion deadline")
    raw = b"".join(parts)
    return {"raw": raw, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
            "inode": [st.st_dev, st.st_ino], "nlink": st.st_nlink, "birth_epoch": st.st_birthtime}


def absolute_snapshot(path, cap=64 << 20):
    fd = directory(os.path.dirname(path))
    try:
        return snapshot(fd, os.path.basename(path), cap)
    finally:
        os.close(fd)


def expectations(name):
    if name == "go_unlisted":
        return {"state": "NOT_LAUNCHED", "exit": 14, "rc": None, "loop": "NOT_STARTED", "failures": set(), "trips": [], "signal": None}
    if name in ("date_fault", "helper_overrun", "helper_group", "helper_eof"):
        unresolved = name in ("helper_group", "helper_eof")
        codes = {"HELPER_FAULT_INJECTED"} if name == "date_fault" else {"HELPER_CALL_FAILED"}
        if unresolved:
            codes.add("HELPER_OWNERSHIP_UNSETTLED")
        return {"state": "UNSETTLED" if unresolved else "NOT_LAUNCHED", "exit": 14,
                "rc": None, "loop": "NOT_STARTED", "failures": codes, "trips": [], "signal": None}
    if name in ("ok", "rc_nonzero", "zombie_hold"):
        return {"state": "SETTLED", "exit": 0, "rc": 3 if name == "rc_nonzero" else 0,
                "loop": "EXITED", "failures": set(), "trips": [], "signal": None}
    if name.startswith("ownership_"):
        codes = {"GRACE_EXPIRED_AFTER_CHILD_EXIT"}
        if name != "ownership_double":
            codes.add("STREAMS_OR_THREADS_NOT_CLOSED")
        return {"state": "UNSETTLED", "exit": 11, "rc": 0, "loop": "GRACE_EXPIRED_AFTER_CHILD_EXIT",
                "failures": codes, "trips": [], "signal": "reaped", "derive_exact_blocker_code": True}
    codes = {"missing_output": "REQUIRED_OUTPUT_MISSING", "mutate_pin": "PIN_CHANGED_OR_UNREADABLE",
             "mutate_evidence": "EVIDENCE_MUTATED", "stray_file": "UNDECLARED_ENTRIES"}
    if name in codes:
        return {"state": "UNSETTLED", "exit": 11, "rc": 0, "loop": "EXITED", "failures": {codes[name]}, "trips": [], "signal": "reaped"}
    if name in ("deadline", "flood", "busy2", "rss"):
        return {"state": "SETTLED", "exit": 0, "rc": -15, "loop": "EXITED", "failures": set(),
                "trips": [{"deadline": "DEADLINE", "flood": "STREAM_CAP", "busy2": "BUSY", "rss": "RSS"}[name]], "signal": "sent"}
    failures = {"GRACE_EXPIRED_AFTER_STOP_REQUEST", "CHILD_NOT_REAPED", "OWNED_LIVE", "STREAMS_OR_THREADS_NOT_CLOSED"}
    if name == "identity":
        failures.add("IDENTITY_UNVERIFIED")
    return {"state": "UNSETTLED", "exit": 11, "rc": None, "loop": "GRACE_EXPIRED_AFTER_STOP_REQUEST",
            "failures": failures, "trips": ["DEADLINE"], "signal": "injected" if name == "identity" else "sent"}


def hash_entry(s):
    return {k: s[k] for k in ("sha256", "bytes", "inode", "nlink")}


def helper_evidence(receipt, cfg, name):
    hs, log = receipt.get("helpers"), receipt.get("helper_log")
    if not isinstance(hs, list) or not isinstance(log, list) or not integer(receipt.get("helper_calls"), 0):
        return False
    if receipt["helper_calls"] != len(hs) or any(not isinstance(e, dict) or not finite(e.get("mono_start")) or not finite(e.get("mono_end")) for e in log):
        return False
    allowed = {"OK", "REFUSED_FAILURE_CANCEL_OR_REENTRANCY"}
    if name == "go_unlisted":
        return hs == [] and receipt["helper_calls"] == 0 and receipt.get("end_date") is None and \
            log and all(e.get("outcome") == "REFUSED_NO_AUTHORIZATION" for e in log)
    if name == "date_fault":
        return hs == [] and receipt["helper_calls"] == 0 and receipt.get("admission", {}).get("date") is None and \
            receipt.get("end_date") is None and any(e.get("outcome") == "FAULT_BEFORE_SPAWN" for e in log) and \
            all(e.get("outcome") in allowed | {"FAULT_BEFORE_SPAWN"} for e in log)
    injected = name in ("helper_overrun", "helper_group", "helper_eof")
    if not hs or any(e.get("outcome") not in allowed | ({"FAILED"} if injected else set()) for e in log):
        return False
    if len({h.get("pid") for h in hs}) != len(hs):
        return False
    for h in hs:
        ident, proof = h.get("identity"), h.get("proof")
        if not isinstance(ident, dict) or not isinstance(proof, dict):
            return False
        if not (integer(h.get("pid"), 1) and ident.get("pid") == ident.get("pgid") == h["pid"] and
                integer(ident.get("uniqueid"), 1) and integer(ident.get("idversion")) and
                ident.get("euid") == ident.get("ruid") == receipt.get("uid") and
                h.get("initial_identity_valid") is True and h.get("leader_reaped") is True and
                h.get("wait_lost") is False and h.get("stdout_closed") is True and
                proof.get("complete") is True and proof.get("unproved_live") == [] and
                h.get("descendants_clear") is True and finite(h.get("mono_reaped")) and
                finite(h.get("mono_call_start")) and finite(h.get("mono_call_deadline")) and
                h["mono_call_start"] <= h["mono_reaped"]):
            return False
        root_uid = ident["uniqueid"]
        roots = {o.get("identity", {}).get("uniqueid"): o.get("root") for o in receipt.get("owned_identities", [])}
        if any(roots.get(p.get("uniqueid")) == root_uid for p in proof.get("owned_live", [])):
            return False
        if name in ("helper_group", "helper_eof"):
            if not (h.get("settled") is False and h.get("clock_failed") is True and h.get("date") is None):
                return False
            if name == "helper_group" and not (h.get("group_clear") is False and h.get("eof_proved") is True):
                return False
            if name == "helper_eof" and not (h.get("group_clear") is True and h.get("eof_proved") is False):
                return False
        elif name == "helper_overrun":
            if not (h.get("clock_failed") is True and h.get("date") is None and h.get("settled") is True and
                    h.get("group_clear") is True and h.get("eof_proved") is True and
                    finite(h.get("mono_cleanup_start")) and h["mono_cleanup_start"] > h["mono_call_deadline"] and
                    finite(h.get("mono_cleanup_deadline")) and finite(h.get("mono_proof_complete")) and
                    h["mono_proof_complete"] <= h["mono_cleanup_deadline"]):
                return False
            if not (finite(h.get("mono_injection_start")) and finite(h.get("mono_injection_end")) and
                    h["mono_injection_end"] > h["mono_call_deadline"] and
                    h["mono_injection_start"] <= h["mono_injection_end"] <= h["mono_cleanup_start"]):
                return False
        else:
            try:
                raw = bytes.fromhex(h["capture_hex"])
                text = raw.decode("ascii").strip()
            except (ValueError, KeyError, UnicodeDecodeError):
                return False
            digits = text[:4] + text[5:7] + text[8:10] + text[11:13] + text[14:16] + text[17:19] + text[20:24]
            if not (h.get("settled") is True and h.get("clock_failed") is False and h.get("rc") == 0 and
                    h.get("group_clear") is True and h.get("eof_proved") is True and h.get("date") == text and
                    len(text) == 24 and len(raw) <= 256 and text[4] == text[7] == "-" and text[10] == "T" and
                    text[13] == text[16] == ":" and text[19] in "+-" and digits.isdigit() and
                    finite(h.get("mono_proof_complete")) and h["mono_proof_complete"] <= h["mono_call_deadline"]):
                return False
        sig = h.get("signal")
        if sig is not None and (not isinstance(sig, dict) or not isinstance(sig.get("sent"), bool) or
                                (sig.get("sent") and (sig.get("identity_ok") is not True or not finite(sig.get("mono_sent"))))):
            return False
    return True


def date_epoch(text):
    return datetime.datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z").timestamp()


def integrated_v12_evidence(receipt, summary, stability, cfg, name):
    checks = {}
    baseline = receipt.get("baseline")
    if not isinstance(baseline, dict) or not finite(baseline.get("mono_complete")) or not isinstance(baseline.get("identities"), list):
        raise Invalid("complete pre-spawn baseline evidence missing")
    baseuids = {p.get("uniqueid") for p in baseline["identities"]}
    hist, coverage, observations = (receipt.get(k) for k in ("unproved_history", "coverage_history", "census_observations"))
    if not all(isinstance(x, list) for x in (hist, coverage, observations)):
        raise Invalid("retained unproved/coverage/retry histories missing")
    seen = set()
    for entry in hist:
        first, last = entry.get("first_identity"), entry.get("last_identity")
        if not isinstance(first, dict) or not isinstance(last, dict):
            raise Invalid("unproved identity history malformed")
        uid = first.get("uniqueid")
        if not integer(uid, 1) or uid in baseuids or uid in seen or last.get("uniqueid") != uid or not (
            finite(entry.get("mono_first_seen")) and finite(entry.get("mono_last_seen")) and entry["mono_first_seen"] <= entry["mono_last_seen"]):
            raise Invalid("unproved history changed/duplicated/exempted identity")
        seen.add(uid)
    if any(not isinstance(x, dict) or not finite(x.get("mono")) or not isinstance(x.get("observation"), list) for x in coverage):
        raise Invalid("coverage history malformed")
    complete_history = True
    missing_total = 0
    prior = None
    for c in observations:
        if not (isinstance(c, dict) and isinstance(c.get("complete"), bool) and integer(c.get("incomplete_n"), 0) and
                integer(c.get("lane_busy"), 0) and integer(c.get("lane_rss"), 0) and finite(c.get("mono_complete"))):
            raise Invalid("resource observation history malformed")
        missing_total += c["incomplete_n"]
        complete_history = complete_history and c["lane_busy"] <= 2 and (
            prior is None or c["mono_complete"] > prior) and all(p.get("uniqueid") in seen for p in c.get("unproved_live", []))
        prior = c["mono_complete"]
    checks["all_unproved_and_retry_evidence_retained"] = complete_history and len(coverage) >= missing_total
    checks["stability_receipt_has_actual_timestamp"] = isinstance(stability.get("now_date"), str)
    stable_epoch = date_epoch(stability["now_date"])
    good_clocks = [h for h in receipt.get("helpers", []) if h.get("date") is not None and h.get("clock_failed") is False]
    commits = [h.get("launch_commit") for h in receipt.get("helpers", [])]
    commits += [receipt.get("admission", {}).get("checked"), receipt.get("launch_commit"), receipt.get("go_commit")]
    if summary.get("acknowledged") is True:
        commits.append(summary.get("ack_commit"))
    age_ok = True
    for commit in (c for c in commits if c is not None):
        if not isinstance(commit, dict) or not finite(commit.get("mono")):
            raise Invalid("commit clock schema missing")
        previous = [h for h in good_clocks if finite(h.get("mono_proof_complete")) and h["mono_proof_complete"] <= commit["mono"]]
        if not previous:
            age_ok = age_ok and commit.get("phase") == "HELPER" and commit.get("stability_age_upper_s") is None
            continue
        clock = max(previous, key=lambda h: h["mono_proof_complete"])
        upper = date_epoch(clock["date"]) - stable_epoch + 1.0 + max(0, commit["mono"] - clock["mono_call_start"])
        age_ok = age_ok and finite(commit.get("stability_age_upper_s")) and abs(commit["stability_age_upper_s"] - upper) <= 1e-6 and (
            0 <= upper <= cfg["admission"]["stability_max_age_s"])
    checks["actual_bin_date_stability_upper_age_replayed"] = age_ok
    checks["runtime_obligation_evidence_present"] = isinstance(receipt.get("runtime_observations"), list)
    if summary.get("acknowledged") is True:
        ack = summary.get("ack_census")
        if not isinstance(ack, dict) or ack.get("complete") is not True:
            raise Invalid("fresh complete ACK census missing")
        final = receipt.get("final_census") or {}
        finalids = {p.get("uniqueid") for p in final.get("owned_live", []) + final.get("unproved_live", [])}
        ackids = {p.get("uniqueid") for p in ack.get("owned_live", []) + ack.get("unproved_live", [])}
        checks["fresh_ack_census_and_current_blockers"] = ackids <= finalids and (
            receipt.get("settlement") == "UNSETTLED" or not ackids) and finite(ack.get("mono_complete")) and (
            summary["post_publish_mono"] <= ack["mono_complete"] <= summary["ack_commit"]["mono"]) and (
            summary["ack_commit"]["mono"] - ack["mono_complete"] <= max(1, cfg["sample_s"]))
        later = summary.get("census_observations")
        checks["postpublication_retry_history_preserved"] = isinstance(later, list) and later[:len(observations)] == observations and (
            later and later[-1].get("mono_complete") == ack["mono_complete"])
        sh = summary.get("unproved_history")
        checks["postpublication_unproved_history_preserved"] = isinstance(sh, list) and seen <= {
            e.get("first_identity", {}).get("uniqueid") for e in sh}
    elif name in ("date_fault", "helper_overrun", "helper_group", "helper_eof"):
        checks["helper_negative_refuses_without_invented_clock"] = "STABILITY_AGE_UNVERIFIABLE" in summary.get("error", "") and (
            receipt.get("clock_observation") is None)
    elif name == "go_unlisted":
        checks["isolated_refusal_has_no_end_helper_contamination"] = "GO_DOES_NOT_NAME_THIS_CONFIG" in summary.get("error", "") and (
            receipt.get("helpers") == [] and receipt.get("failures") == [])
    return checks


def verify(name, approval_digest, actual_exit, runfd, outfd):
    exp, C = expectations(name), {}
    result = {"checker": VERSION, "scenario": name, "criteria": C,
              "parent_release": "not granted; separate ended-owned and late-artifact disposition mandatory"}
    def require(key, ok):
        C[key] = bool(ok)
    ap = snapshot(runfd, "parent-authorization.json", 1 << 20)
    if ap["sha256"] != approval_digest:
        raise Invalid("approval digest differs from the parent-supplied trusted digest")
    approval = decode(ap["raw"])
    if not isinstance(approval, dict) or approval.get("kind") != "v12-qualification-invocation-v1" or approval.get("scenario") != name:
        raise Invalid("approval kind/scenario")
    cp, gp, sp, pp = (snapshot(runfd, f, 1 << 20) for f in ("config.json", "go.json", "stability.json", "preparation.json"))
    require("approval_artifact_bindings", all(approval.get(k) == v["sha256"] for k, v in (
        ("config_sha256", cp), ("go_sha256", gp), ("stability_receipt_sha256", sp), ("preparation_sha256", pp))))
    package = approval.get("sources")
    if not isinstance(package, dict) or set(package) != {"supervisor", "child", "writer", "checker"}:
        raise Invalid("approval must pin the entire four-source package")
    expected_sources = {"supervisor": (SUPERVISOR, SUPERVISOR_SHA), "child": (CHILD, CHILD_SHA),
                        "writer": (WRITER, WRITER_SHA), "checker": (os.path.realpath(__file__), None)}
    source_ok = True
    for key, (path, h) in expected_sources.items():
        src = absolute_snapshot(path, 1 << 20)
        pinned = package[key]
        source_ok = source_ok and isinstance(pinned, dict) and pinned.get("path") == path and pinned.get("sha256") == src["sha256"] and (h is None or h == src["sha256"])
    require("approved_sources_match_actual_bytes", source_ok)
    py = approval.get("python")
    if not isinstance(py, dict) or not isinstance(py.get("path"), str) or not py["path"].endswith("/Resources/Python.app/Contents/MacOS/Python") or os.path.realpath(py["path"]) != py["path"]:
        raise Invalid("approval interpreter must be the actual Python.app executable, not its launcher")
    require("actual_interpreter_digest", absolute_snapshot(py["path"])["sha256"] == py.get("sha256"))
    cfg, go, stability = decode(cp["raw"]), decode(gp["raw"]), decode(sp["raw"])
    adm = cfg["admission"]
    expected_cfg = config_for(name, py["path"], py["sha256"], adm["outstanding_reservations_bytes"], adm["lane_outstanding_reservations_bytes"])
    require("exact_scenario_config", cfg == expected_cfg)
    reservation = {"bytes": RESERVATION, "cpu_slots": cfg["cpu_slots"],
                   "outstanding_reservations_bytes": adm["outstanding_reservations_bytes"],
                   "lane_outstanding_reservations_bytes": adm["lane_outstanding_reservations_bytes"]}
    require("current_parent_allocation", approval.get("allocation") == reservation and
            all(integer(adm[k], 0) for k in ("outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")))
    expected_entry = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots")}
    expected_entry.update({k: adm[k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
    require("go_envelope", go.get("decision") == "GO" and go.get("item") == ITEM and finite(go.get("not_after_epoch")) and
            go.get("stability_receipt_sha256") == sp["sha256"] and stability.get("verdict") == "PASS")
    require("go_exact_listing", isinstance(go.get("configs"), dict) and
            (go["configs"] == {} if name == "go_unlisted" else go["configs"] == {cp["sha256"]: expected_entry}))
    expected_root = (json.dumps({"kind": "v12-qualification-root", "supervisor_sha256": SUPERVISOR_SHA,
                                 "child_sha256": CHILD_SHA}, sort_keys=True) + "\n").encode()
    qfd = directory(QROOT)
    try:
        require("fresh_package_root_marker", snapshot(qfd, "package-root.json", 1 << 20)["raw"] == expected_root)
    finally:
        os.close(qfd)
    files = {n: snapshot(outfd, n, optional=True) for n in ("supervisor-receipt.json", "settlement.json",
              "settlement.json.staged", "launch.json", "samples.jsonl", "stdout.txt", "stderr.txt", "child-out.json", "stray.txt")}
    if any(files[n] is None for n in ("supervisor-receipt.json", "settlement.json", "settlement.json.staged")):
        raise Invalid("missing receipt or settlement publication")
    receipt = decode(files["supervisor-receipt.json"]["raw"])
    settlement = decode(files["settlement.json"]["raw"])
    summaries = sequence(snapshot(runfd, "supervisor-summary.txt", 1 << 20)["raw"])
    if len(summaries) != 1:
        raise Invalid("exactly one captured supervisor summary required")
    summary = summaries[0]
    rsha, ssha = files["supervisor-receipt.json"]["sha256"], files["settlement.json"]["sha256"]
    require("receipt_source_config_binding", receipt.get("supervisor") == "owned_supervisor_v12" and
            receipt.get("supervisor_sha256") == SUPERVISOR_SHA and receipt.get("config_sha256") == cp["sha256"])
    require("settlement_receipt_binding", settlement.get("receipt_sha256") == rsha and settlement.get("receipt") == cfg["receipt"] and
            settlement.get("config_sha256") == cp["sha256"] and settlement.get("supervisor") == "owned_supervisor_v12")
    a, b = files["settlement.json"], files["settlement.json.staged"]
    require("same_inode_staged_link", a["sha256"] == b["sha256"] and a["inode"] == b["inode"] and a["nlink"] == b["nlink"] == 2)
    require("summary_and_actual_exit", integer(actual_exit) and actual_exit == exp["exit"] == summary.get("exit_code") and
            summary.get("receipt_sha256") == rsha and summary.get("settlement_record_sha256") == ssha)
    if name in ("go_unlisted", "date_fault", "helper_overrun", "helper_group", "helper_eof"):
        require("intended_ack_refusal", summary.get("acknowledged") is False and summary.get("reason") == "ACK_REFUSED")
    else:
        require("publication_acknowledged", summary.get("acknowledged") is True and summary.get("settlement") == exp["state"] and
                summary.get("config_sha256") == cp["sha256"] and summary.get("receipt_bytes") == files["supervisor-receipt.json"]["bytes"] and
                summary.get("settlement_bytes") == files["settlement.json"]["bytes"] and finite(summary.get("post_publish_mono")))
    failures, trips = receipt.get("failures"), receipt.get("trips")
    if not isinstance(failures, list) or not all(isinstance(f, dict) and isinstance(f.get("code"), str) and finite(f.get("mono")) for f in failures):
        raise Invalid("malformed failure entries")
    if not isinstance(trips, list) or not all(isinstance(t, dict) and isinstance(t.get("trip"), str) and finite(t.get("mono")) and finite(t.get("epoch")) for t in trips):
        raise Invalid("malformed trip entries")
    codes, tripcodes = [f["code"] for f in failures], [t["trip"] for t in trips]
    if exp.get("derive_exact_blocker_code"):
        fc_early = receipt.get("final_census") or {}
        if fc_early.get("owned_live"):
            exp["failures"].add("OWNED_LIVE")
        if fc_early.get("unproved_live"):
            exp["failures"].add("UNPROVED_LIVE")
    require("failure_sets_exact", len(codes) == len(set(codes)) and set(codes) == exp["failures"] and settlement.get("failure_codes") == sorted(codes))
    require("trip_sets_exact", tripcodes == exp["trips"] == settlement.get("trips"))
    rc = receipt.get("child_returncode")
    require("state_rc_loop_exact", receipt.get("settlement") == settlement.get("settlement") == exp["state"] and
            rc == exp["rc"] and (rc is None or integer(rc)) and settlement.get("child_returncode") == rc and
            receipt.get("loop_status") == exp["loop"])
    require("mandatory_owned_date_helpers", helper_evidence(receipt, cfg, name))
    C.update(integrated_v12_evidence(receipt, summary, stability, cfg, name))
    require("no_hidden_cancellation_or_lost_wait", receipt.get("cancel") == {"signal": None, "mono": None} and
            receipt.get("wait_status_lost") is False)
    expected_pin_end = [[p["path"], not (name == "mutate_pin" and p["path"].endswith("/pinned-scratch.txt"))] for p in cfg["pins"]]
    require("pin_end_results_exact", receipt.get("pins_at_end") == expected_pin_end)
    sig, stop = receipt.get("signal"), receipt.get("stop_request")
    if exp["signal"] is None:
        require("signal_exact", sig is None and stop is None)
    elif exp["signal"] == "sent":
        require("signal_exact", isinstance(sig, dict) and sig.get("sent") is True and sig.get("identity_ok") is True and finite(sig.get("mono_sent")))
    elif exp["signal"] == "reaped":
        require("signal_exact", isinstance(sig, dict) and sig.get("sent") is False and sig.get("why_not") == "CHILD_ALREADY_REAPED" and stop.get("reason") == "FAILURE")
    else:
        require("signal_exact", isinstance(sig, dict) and sig.get("sent") is False and sig.get("why_not") == "FAULT_INJECTED" and
                any(f["code"] == "IDENTITY_UNVERIFIED" and f.get("detail") == "fault injected" for f in failures))
    if exp["trips"]:
        require("stop_matches_intended_trip", isinstance(stop, dict) and stop.get("reason") == exp["trips"][0])
    if name == "go_unlisted":
        require("only_intended_admission_refusal", receipt.get("admission", {}).get("reasons") == ["GO_DOES_NOT_NAME_THIS_CONFIG"] and
                receipt.get("child_pid") is None and receipt.get("contract_violations") == [])
    elif name in ("date_fault", "helper_overrun", "helper_group", "helper_eof"):
        require("only_intended_helper_admission_refusal", receipt.get("admission", {}).get("reasons") == ["DATE_HELPER_UNAVAILABLE"] and
                receipt.get("child_pid") is None and receipt.get("clear") is None)
    else:
        require("healthy_admission", receipt.get("admission", {}).get("reasons") == [] and receipt.get("go_delivered") is True)
    inventory = receipt.get("output_root_inventory")
    if not isinstance(inventory, dict) or set(inventory) != {QROOT + "/" + name + "/out"}:
        raise Invalid("per-root inventory missing")
    actual = set(os.listdir(outfd))
    published = {"supervisor-receipt.json", "settlement.json", "settlement.json.staged"}
    expected_names = set(published)
    launched = name not in ("go_unlisted", "date_fault", "helper_overrun", "helper_group", "helper_eof")
    if launched:
        expected_names |= {"launch.json", "samples.jsonl", "stdout.txt", "stderr.txt"}
    if name in ("ok", "rc_nonzero", "mutate_pin", "mutate_evidence", "stray_file", "zombie_hold") or name.startswith("ownership_"):
        expected_names.add("child-out.json")
    if name == "stray_file":
        expected_names.add("stray.txt")
    late = set()
    if name in ("ignore", "identity") and files["child-out.json"] is not None:
        if not finite(receipt.get("epoch_decision")) or files["child-out.json"]["birth_epoch"] <= receipt["epoch_decision"]:
            raise Invalid("unexpected non-late child output")
        late.add("child-out.json")
        expected_names.add("child-out.json")
    require("exact_directory_manifest", actual == expected_names and
            set(inventory[next(iter(inventory))]) == expected_names - published - late)
    result["late_artifacts"] = {n: hash_entry(files[n]) for n in late}
    if not launched:
        require("no_launched_artifacts", all(files[n] is None for n in ("launch.json", "samples.jsonl", "stdout.txt", "stderr.txt", "child-out.json")))
        result["verdict"] = "PASS" if all(C.values()) else "FAIL"
        return result
    lraw = files["launch.json"]["raw"]
    if name == "mutate_evidence":
        require("one_byte_launch_mutation", lraw[-1:] == b"x" and hashlib.sha256(lraw[:-1]).hexdigest() == receipt.get("launch_record_sha256"))
        lraw = lraw[:-1]
    launch = decode(lraw)
    ident = launch.get("identity")
    if not isinstance(ident, dict):
        raise Invalid("launch identity missing")
    require("full_child_identity", all(integer(ident.get(k), 1) for k in ("pid", "uniqueid", "pgid")) and
            integer(ident.get("idversion")) and integer(ident.get("euid"), 0) and integer(ident.get("ruid"), 0) and
            ident["pid"] == ident["pgid"] == receipt.get("child_pid") and receipt.get("child_identity") == ident and
            launch.get("supervisor_pid") == receipt.get("supervisor_pid") and launch.get("argv") == cfg["argv"] and
            launch.get("supervisor_sha256") == SUPERVISOR_SHA and launch.get("config_sha256") == cp["sha256"])
    owned = receipt.get("owned_identities")
    helper_ids = {h["identity"]["uniqueid"] for h in receipt.get("helpers", []) if isinstance(h.get("identity"), dict)}
    known_uids = helper_ids | {ident["uniqueid"]}
    known_extra = [o for o in owned if o.get("identity", {}).get("uniqueid") not in known_uids] if isinstance(owned, list) else []
    require("known_owned_registry_retained", isinstance(owned, list) and all(
        any(o.get("identity", {}).get("uniqueid") == u for o in owned) for u in known_uids) and
        (name in NEGATIVE_PROCESS or (not known_extra and receipt.get("contract_violations") == [])))
    require("authorization_cross_binding", launch.get("authorization") == receipt.get("admission", {}).get("authorization") and
            launch.get("authorization", {}).get("go_sha256") == gp["sha256"] and
            launch.get("authorization", {}).get("stability_receipt_sha256") == sp["sha256"])
    arts, ev = receipt.get("artifacts"), receipt.get("evidence_expected_sha256")
    if not isinstance(arts, dict) or not isinstance(ev, dict):
        raise Invalid("artifact/evidence manifest missing")
    amap = {cfg["stdout"]: "stdout.txt", cfg["stderr"]: "stderr.txt", cfg["samples"]: "samples.jsonl",
            cfg["launch_record"]: "launch.json", cfg["outputs"][0]["path"]: "child-out.json"}
    require("artifact_keys_complete", set(arts) == set(amap))
    hashes_ok = True
    for path, filename in amap.items():
        current, stated = files[filename], arts.get(path)
        if filename in late:
            hashes_ok = hashes_ok and stated is None
        elif current is None:
            hashes_ok = hashes_ok and stated is None
        else:
            hashes_ok = hashes_ok and isinstance(stated, dict) and all(stated.get(k) == current[k] for k in ("sha256", "bytes", "inode", "nlink"))
    require("actual_artifact_hashes", hashes_ok)
    expected_ev = {cfg["samples"], cfg["launch_record"]}
    if name not in ("ignore", "identity", "ownership_group", "ownership_slow", "ownership_fast"):
        expected_ev |= {cfg["stdout"], cfg["stderr"]}
    require("supervisor_expected_digests_exact", set(ev) == expected_ev and all(
        ev[p] == (hashlib.sha256(files[amap[p]]["raw"][:-1]).hexdigest() if name == "mutate_evidence" and p == cfg["launch_record"] else files[amap[p]]["sha256"])
        for p in expected_ev))
    require("stderr_empty", files["stderr.txt"]["raw"] == b"")
    samplefile = files["samples.jsonl"]
    samples = sequence(samplefile["raw"])
    require("sample_counts_and_bytes", bool(samples) and integer(receipt.get("samples_written"), 1) and
            len(samples) == receipt["samples_written"] and samplefile["bytes"] == receipt.get("samples_bytes"))
    previous, observed = None, []
    sample_ok = True
    for s in samples:
        c, r = s.get("census"), s.get("resources")
        sample_ok = (sample_ok and isinstance(c, dict) and c.get("complete") is True and integer(c.get("lane_busy"), 0) and
                     0 <= c["lane_busy"] <= 2 and integer(c.get("lane_rss"), 0) and isinstance(c.get("lane_busy_pids"), list) and
                     c["lane_busy"] == len(c["lane_busy_pids"]) and finite(s.get("mono")) and (previous is None or s["mono"] > previous) and
                     isinstance(r, dict) and integer(r.get("charged_bytes"), 0) and r["charged_bytes"] <= cfg["output_trip_bytes"] and
                     integer(r.get("free"), 0) and r["free"] >= cfg["free_trip_bytes"] and set(s.get("failure_codes", [])) <= exp["failures"] and
                     s.get("trips") in ([], exp["trips"]))
        if not sample_ok:
            break
        previous = s["mono"]
        observed.append(c)
    require("complete_uncontaminated_samples", sample_ok)
    final_c = receipt.get("final_census")
    if not isinstance(final_c, dict) or final_c.get("complete") is not True:
        raise Invalid("complete final census required")
    observed.append(final_c)
    clear = receipt.get("clear")
    if exp["loop"] == "EXITED":
        require("timely_all_predicate_clearance", isinstance(clear, dict) and finite(clear.get("mono_all_predicates_verified")) and
                isinstance(clear.get("census"), dict) and clear["census"].get("complete") is True and clear["census"].get("owned_live") == [] and
                clear["census"].get("unproved_live") == [] and clear["census"].get("group_live") == [] and
                clear["mono_all_predicates_verified"] >= clear["census"].get("mono_complete", math.inf))
        if isinstance(clear, dict) and isinstance(clear.get("census"), dict):
            observed.append(clear["census"])
        if isinstance(stop, dict):
            require("clear_before_stop_grace", clear["mono_all_predicates_verified"] <= stop["mono"] + cfg["settle_s"])
        require("final_owned_clear", final_c.get("owned_live") == [] and final_c.get("unproved_live") == [] and final_c.get("group_live") == [])
    else:
        blockers = final_c.get("owned_live", []) + final_c.get("unproved_live", [])
        if name.startswith("ownership_"):
            require("ownership_blockers_retained", bool(blockers) and clear is None)
        else:
            require("owned_child_still_blocking", isinstance(final_c.get("owned_live"), list) and len(final_c["owned_live"]) == 1 and
                    final_c["owned_live"][0].get("uniqueid") == ident["uniqueid"] and final_c.get("unproved_live") == [] and clear is None)
        result["owned_or_unproved_not_ended"] = blockers
    mx = receipt.get("maxima") or {}
    retained = receipt.get("census_observations")
    if not isinstance(retained, list) or not retained or any(not isinstance(x, dict) or not integer(x.get("lane_busy"), 0) or
        not integer(x.get("lane_rss"), 0) or not finite(x.get("mono_complete")) for x in retained):
        raise Invalid("all helper/retry resource observations must be retained")
    enforced = [x for x in retained if x.get("phase") not in ("ADMISSION", "PRE_GO")]
    require("census_maxima_reconciled", bool(enforced) and integer(mx.get("lane_busy"), 0) and integer(mx.get("lane_rss"), 0) and
            mx["lane_busy"] == max(x["lane_busy"] for x in enforced) and mx["lane_rss"] == max(x["lane_rss"] for x in enforced))
    require("free_minimum_explicit", integer(receipt.get("min_free"), 0) and receipt["min_free"] >= cfg["free_trip_bytes"])
    stdout = files["stdout.txt"]["raw"]
    childout = decode(files["child-out.json"]["raw"]) if files["child-out.json"] is not None else None
    if childout is not None:
        require("child_output_identity", childout.get("scenario") == name and childout.get("pid") == ident["pid"] and
                childout.get("pgid") == ident["pgid"] and
                ("child-out.json" in late or childout.get("ppid") == receipt.get("supervisor_pid")))
    if name.startswith("ownership_"):
        target = childout.get("grandchild") if isinstance(childout, dict) else None
        blockers = final_c.get("owned_live", []) + final_c.get("unproved_live", [])
        require("intended_descendant_is_only_blocker", integer(target, 1) and len(blockers) == 1 and
                blockers[0].get("pid") == target and integer(blockers[0].get("uniqueid"), 1) and clear is None)
        require("ownership_negative_explicitly_authorized", approval.get("ownership_negative") is True and
                childout.get("negative_control") is True)
        if name == "ownership_double":
            require("double_fork_transport_reported", integer(childout.get("intermediate"), 1) and childout.get("intermediate_status") == 0)
    if name == "zombie_hold":
        target = childout.get("grandchild") if isinstance(childout, dict) else None
        require("reported_zombie_identity_observed", integer(target, 1) and any(target in c.get("owned_zombies", []) for c in observed) and
                childout.get("intermediate_status") == 0 and approval.get("ownership_negative") is True)
    if name in NEGATIVE_PROCESS:
        reported = {childout.get("grandchild"), childout.get("intermediate")} if isinstance(childout, dict) else set()
        if name == "busy2":
            ids_lines = [x for x in stdout.decode().splitlines() if x.startswith("IDS ")]
            ids_obj = decode(ids_lines[0][4:].encode()) if len(ids_lines) == 1 else {}
            reported = set(ids_obj.get("busy_pids", [])) - {ident["pid"]}
        reported.discard(None)
        require("no_unreported_owned_identity", all(o.get("identity", {}).get("pid") in reported for o in known_extra) and
                all(p.get("pid") in reported for p in receipt.get("contract_violations", [])))
    if name == "ok":
        require("stdout_exact", stdout == b"line 1\nline 2\nline 3\n")
    if name in ("rc_nonzero", "mutate_pin", "mutate_evidence", "stray_file", "ignore", "identity", "deadline"):
        require("stdout_empty", stdout == b"")
    if name == "missing_output":
        require("missing_output_intended", files["child-out.json"] is None and stdout == b"no output written\n")
    if name == "mutate_pin":
        fixture = snapshot(runfd, "pinned-scratch.txt", 1 << 20)
        require("fixture_one_byte_append", fixture["raw"] == FIXTURE + b"x" and fixture["nlink"] == 1 and
                childout.get("target_inode") == fixture["inode"] and childout.get("size_before") == len(FIXTURE))
    if name == "mutate_evidence":
        require("launch_mutation_same_inode", childout.get("target_inode") == files["launch.json"]["inode"] and
                childout.get("size_before") + 1 == files["launch.json"]["bytes"])
    if name == "stray_file":
        require("stray_actual_bytes", files["stray.txt"]["raw"] == b"undeclared file\n" and files["stray.txt"]["nlink"] == 1)
    if exp["trips"]:
        t = trips[0]
        require("trip_stop_signal_order", finite(stop.get("mono")) and t["mono"] <= stop["mono"] and
                (exp["signal"] != "sent" or stop["mono"] <= sig["mono_sent"]))
    if name in ("deadline", "ignore", "identity"):
        require("deadline_after_wall_limit", trips[0]["mono"] >= receipt["mono_child_deadline"] == receipt["mono_spawn"] + cfg["max_wall_s"])
    if name in ("deadline", "flood", "busy2", "rss"):
        require("signal_to_persistence_le_7s", 0 <= summary["post_publish_mono"] - sig["mono_sent"] <= 7 and
                0 <= summary["post_publish_mono"] - trips[0]["mono"] <= 7)
    if name == "flood":
        st = receipt.get("streams", {}).get("stdout") or {}
        require("flood_trigger_proved", st.get("overflow") is True and st.get("bytes_written") == len(stdout) == cfg["stdout_cap_bytes"] and
                integer(st.get("bytes_seen"), 0) and st["bytes_seen"] > st["bytes_written"] and
                any(s.get("streams", {}).get("stdout", {}).get("overflow") is True for s in samples))
    if name in ("busy2", "rss"):
        lines = [x for x in stdout.decode().splitlines() if x]
        ids = decode(lines[0][4:].encode()) if len(lines) == 1 and lines[0].startswith("IDS ") else {}
        if name == "busy2":
            d = trips[0].get("detail") or {}
            pids = ids.get("busy_pids")
            require("two_reserved_busy_identities_proved", isinstance(pids, list) and len(pids) == 2 and pids[0] == ident["pid"] and
                    all(integer(p, 1) for p in pids) and len(set(pids)) == 2 and d.get("count") == 2 and set(d.get("pids", [])) == set(pids) and
                    any(set(c["lane_busy_pids"]) == set(pids) and c["lane_busy"] == 2 for c in observed) and cfg["cpu_slots"] == 2)
        else:
            d = trips[0].get("detail")
            require("rss_intended_crossing", ids.get("rss_pid") == ident["pid"] and ids.get("allocated") == 320 * 1024 * 1024 and
                    integer(d, 0) and d > cfg["rss_trip_bytes"] and any(c["lane_rss"] == d for c in observed))
    streams = receipt.get("streams")
    require("stream_schema", isinstance(streams, dict) and set(streams) == {"stdout", "stderr"} and all(
        isinstance(v.get("closed"), bool) and v.get("error") is None and integer(v.get("bytes_written"), 0) and
        v["bytes_written"] == files[k + ".txt"]["bytes"] for k, v in streams.items()))
    if exp["loop"] == "EXITED":
        require("streams_closed", all(v["closed"] is True for v in streams.values()))
        require("clearance_after_stream_and_reap", finite(receipt.get("child_exit_mono")) and
                receipt["child_exit_mono"] <= clear["mono_all_predicates_verified"] and all(
                    finite(v.get("mono_close_completed")) and v["mono_close_completed"] <= clear["mono_all_predicates_verified"]
                    for v in streams.values()))
    if name != "go_unlisted":
        commits = [receipt.get("launch_commit"), receipt.get("go_commit"), summary.get("ack_commit")]
        require("commit_order_and_expiry", all(isinstance(c, dict) and finite(c.get("mono")) and finite(c.get("epoch")) and c["epoch"] <= go["not_after_epoch"] for c in commits) and
                commits[0]["mono"] <= receipt["mono_spawn"] <= commits[1]["mono"] <= summary["post_publish_mono"] <= commits[2]["mono"])
        payload = files["supervisor-receipt.json"]["bytes"] + files["settlement.json"]["bytes"]
        br, ar = summary.get("publication_resources"), summary.get("ack_resources")
        if not isinstance(br, dict) or not isinstance(ar, dict):
            raise Invalid("publication/ack resource evidence missing")
        charged_before = sum(v["bytes"] for n, v in files.items() if v is not None and n not in published and n not in late)
        tfd = os.open("tmp", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=runfd)
        try:
            require("test_tmp_empty", os.listdir(tfd) == [])
        finally:
            os.close(tfd)
        require("all_launch_evidence_bytes_charged", br.get("charged_bytes") == charged_before and
                ar.get("charged_bytes") == charged_before + payload)
        remain_before = max(0, RESERVATION - charged_before - payload)
        require("exact_payload_budget", charged_before + payload <= RESERVATION and payload <= 4 << 20 and
                charged_before + payload <= cfg["output_trip_bytes"] and ar["charged_bytes"] <= cfg["output_trip_bytes"] and
                all(integer(r.get(k), 0) for r in (br, ar) for k in ("free", "charged_bytes", "lane_bytes")) and
                br["free"] - payload - adm["outstanding_reservations_bytes"] - remain_before >= cfg["free_trip_bytes"] and
                br["lane_bytes"] + payload + adm["lane_outstanding_reservations_bytes"] + remain_before <= cfg["lane_disk_ceiling_bytes"] and
                ar["free"] - adm["outstanding_reservations_bytes"] - remain_before >= cfg["free_trip_bytes"] and
                ar["lane_bytes"] + adm["lane_outstanding_reservations_bytes"] + remain_before <= cfg["lane_disk_ceiling_bytes"])
    result["artifact_hashes"] = {n: hash_entry(v) for n, v in files.items() if v is not None}
    result["verdict"] = "PASS" if all(C.values()) else "FAIL"
    return result


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in SC:
        raise Invalid("usage: SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT")
    name, approval_digest, exit_text = sys.argv[1:4]
    if len(approval_digest) != 64 or any(c not in "0123456789abcdef" for c in approval_digest):
        raise Invalid("parent approval digest format")
    actual_exit = int(exit_text)
    runfd = directory(QROOT + "/" + name)
    outfd = os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=runfd)
    try:
        try:
            result = verify(name, approval_digest, actual_exit, runfd, outfd)
        except (Invalid, OSError, ValueError, KeyError, TypeError, AttributeError, IndexError, UnicodeDecodeError) as e:
            result = {"checker": VERSION, "scenario": name, "verdict": "FAIL", "criteria": {}, "error": repr(e)}
        data = (json.dumps(result, sort_keys=True, indent=1, allow_nan=False) + "\n").encode()
        fd = os.open("check.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=runfd)
        try:
            view = memoryview(data)
            while view:
                n = os.write(fd, view)
                if n <= 0:
                    raise Invalid("zero-progress checker write")
                view = view[n:]
            os.fsync(fd)
        finally:
            os.close(fd)
        os.fsync(runfd)
        print(json.dumps({"scenario": name, "verdict": result["verdict"], "failed": [k for k, v in result["criteria"].items() if not v]}))
        return 0 if result["verdict"] == "PASS" else 1
    finally:
        os.close(outfd)
        os.close(runfd)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        sys.stderr.write("CHECKER_ERROR %r\n" % e)
        sys.exit(2)
