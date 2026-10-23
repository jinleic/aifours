#!/usr/bin/env python3
"""V15 rebound qualification checker, source-only. Retains owned bounded /bin/date and explicit negative controls.
Parent correction fabe57ab...4155a2 withdraws v10's narrowing; all earlier files remain immutable/unrun.
Usage: guard_qual_check_v9.py SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT
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

VERSION = "guard_qual_check_v9"
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v8-v15"
ITEM = "owned_supervisor_v15 rebound creation-identity qualification"
CHILD = LANE + "/code/guard_qual_child_v10.py"
SUPERVISOR = LANE + "/code/owned_supervisor_v15.py"
WRITER = LANE + "/code/guard_qual_configs_v10.py"
CHECKER = LANE + "/code/guard_qual_check_v9.py"
SUPERVISOR_SHA = "0a22bbc56a929bf674a579314ef0eeefd7f8e71ed5b3e39cb44db7921f5f34f9"
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

def config_for(name, python, pysha, outstanding, lane_outstanding, source_pins, preparation_sha256, creation_channel):
    life, wall, required, rss = SC[name]
    run, out = QROOT + "/" + name, QROOT + "/" + name + "/out"
    pins = [dict(source_pins[k]) for k in ("supervisor", "child", "writer", "checker")]
    pins += [{"path": python, "sha256": pysha},
             {"path": run + "/preparation.json", "sha256": preparation_sha256}]
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
            "fault_injection": {FAULTS[name]: True} if name in FAULTS else {},
            "creation_channel": creation_channel}


class Invalid(Exception):
    pass


def integer(x, lower=None):
    return isinstance(x, int) and not isinstance(x, bool) and (lower is None or x >= lower)


def finite(x):
    try:
        return isinstance(x, (float, int)) and not isinstance(x, bool) and math.isfinite(x)
    except OverflowError:
        return False


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
    def signature(s):
        return (s.st_dev, s.st_ino, s.st_mode, s.st_size, s.st_nlink, s.st_mtime_ns, s.st_ctime_ns)
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
        if signature(s1) != signature(st):
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
        named_end = os.stat(name, dir_fd=fdroot, follow_symlinks=False)
        if tail or signature(s2) != signature(st) or signature(named_end) != signature(st):
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
    if receipt["helper_calls"] != len(hs) or len(hs) > cfg["helper_budget"]["max_calls"] or any(
            not isinstance(e, dict) or not finite(e.get("mono_start")) or not finite(e.get("mono_end")) or
            e["mono_end"] < e["mono_start"] for e in log):
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
    if len({h.get("pid") for h in hs}) != len(hs) or (injected and len(hs) != 1):
        return False
    for h in hs:
        ident, proof = h.get("identity"), h.get("proof")
        if not isinstance(ident, dict) or not isinstance(proof, dict):
            return False
        if not (integer(h.get("pid"), 1) and ident.get("pid") == ident.get("pgid") == h["pid"] and
                integer(ident.get("uniqueid"), 1) and integer(ident.get("idversion")) and
                ident.get("euid") == ident.get("ruid") == receipt.get("uid") and
                h.get("initial_identity_valid") is True and h.get("leader_reaped") is True and
                h.get("wait_lost") is False and integer(h.get("rc")) and h.get("stdout_closed") is True and
                proof.get("complete") is True and proof.get("unproved_live") == [] and
                h.get("coverage_complete") is True and h.get("descendants_clear") is True and finite(h.get("mono_reaped")) and
                finite(h.get("mono_call_start")) and finite(h.get("mono_call_deadline")) and
                h["mono_call_start"] <= h["mono_reaped"] and h.get("spawn_error") is None and
                isinstance(h.get("term_attempted"), bool) and isinstance(h.get("launch_commit"), dict)):
            return False
        root_uid = ident["uniqueid"]
        roots = {o.get("identity", {}).get("uniqueid"): o.get("root") for o in receipt.get("owned_identities", [])}
        if any(roots.get(p.get("uniqueid")) == root_uid for p in proof.get("owned_live", [])):
            return False
        if name in ("helper_group", "helper_eof"):
            if not (h.get("settled") is False and h.get("clock_failed") is True and h.get("date") is None and h["rc"] == 0):
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
            if not (h["rc"] in (0, -15) and finite(h.get("mono_injection_start")) and finite(h.get("mono_injection_end")) and
                    h["mono_call_start"] <= h["mono_injection_start"] < h["mono_call_deadline"] < h["mono_injection_end"] <= h["mono_cleanup_start"]):
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
        identity(ident)
        linked = [e for e in log if e.get("pid") == h["pid"]]
        if len(linked) != 1 or linked[0].get("outcome") != ("FAILED" if injected else "OK"):
            return False
        sig = h.get("signal")
        if sig is not None:
            if not isinstance(sig, dict) or not isinstance(sig.get("sent"), bool):
                return False
            if "identity_observed" in sig:
                identity(sig["identity_observed"])
                if not finite(sig.get("mono_identity_observed")) or not finite(sig.get("mono_check")) or \
                        sig["mono_identity_observed"] < sig["mono_check"]:
                    return False
            if sig["sent"] and (sig.get("identity_ok") is not True or not finite(sig.get("mono_sent")) or
                    "identity_observed" not in sig or identity(sig["identity_observed"]) != identity(ident) or
                    not sig["mono_identity_observed"] <= sig["mono_sent"]):
                return False
        if h["rc"] == -15 and (sig is None or sig.get("sent") is not True):
            return False
    return True


def date_epoch(text):
    if not isinstance(text, str):
        raise Invalid("date is not an actual helper string")
    parsed = datetime.datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
    if parsed.strftime("%Y-%m-%dT%H:%M:%S%z") != text:
        raise Invalid("noncanonical actual date")
    return parsed.timestamp()


def same(a, b):
    return json.dumps(a, sort_keys=True, separators=(",", ":"), allow_nan=False) == \
        json.dumps(b, sort_keys=True, separators=(",", ":"), allow_nan=False)


def identity(p):
    if not isinstance(p, dict) or not all(integer(p.get(k), 0) for k in
        ("pid", "ppid", "pgid", "uniqueid", "euid", "ruid", "status")) or not integer(p.get("idversion")) or \
            not -(1 << 31) <= p["idversion"] < 1 << 31 or \
            not all(p[k] > 0 for k in ("pid", "uniqueid")) or not isinstance(p.get("traced"), bool) or \
            not isinstance(p.get("comm"), str):
        raise Invalid("full process incarnation missing")
    return tuple(p[k] for k in ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced"))


def histories(view, baseuids):
    required = ("identity_history", "unproved_history", "coverage_history", "census_observations", "observation_attempts")
    if any(not isinstance(view.get(k), list) for k in required):
        raise Invalid("complete current/retained history schema missing")
    ih, uh, ch, cs, ats = (view[k] for k in required)
    if len(ih) > 8192 or len(uh) > 8192 or len(ch) > 16384 or len(cs) > 4096 or len(ats) > 4096:
        raise Invalid("history entry cap")
    if not integer(view.get("history_charge_bytes"), 0) or view["history_charge_bytes"] > 4 << 20 or \
            view.get("history_overflow") is not None or view.get("history_halted", False) is not False:
        raise Invalid("history cap/overflow or missing charged bytes")
    imap = {}
    for e in ih:
        first, last, variants = e.get("first_identity"), e.get("last_identity"), e.get("variants")
        f, l = identity(first), identity(last)
        uid = first["uniqueid"]
        if uid in imap or first["uniqueid"] != last["uniqueid"] or first["pid"] != last["pid"] or \
                not finite(e.get("mono_first_seen")) or not finite(e.get("mono_last_seen")) or \
                e["mono_first_seen"] > e["mono_last_seen"] or not integer(e.get("observations"), 1) or \
                not isinstance(e.get("source"), str) or not isinstance(variants, list) or not 1 <= len(variants) <= 64:
            raise Invalid("identity ledger malformed")
        fps = [identity(p) for p in variants]
        if len(set(fps)) != len(fps) or f not in fps or l not in fps or any(
                p["uniqueid"] != uid or p["pid"] != first["pid"] for p in variants):
            raise Invalid("identity variants changed/disappeared incarnation")
        imap[uid] = e
    def retained(p, stamp=None):
        fp, uid = identity(p), p["uniqueid"]
        e = imap.get(uid)
        if e is None or fp not in {identity(v) for v in e["variants"]}:
            raise Invalid("observed incarnation omitted from retained ledger")
        if stamp is not None and not e["mono_first_seen"] <= stamp <= e["mono_last_seen"] + 1e-6:
            raise Invalid("retained incarnation time does not enclose observation")
    umap = {}
    for e in uh:
        first, last = e.get("first_identity"), e.get("last_identity")
        retained(first)
        retained(last)
        uid = first["uniqueid"]
        if uid in umap or uid in baseuids or uid != last["uniqueid"] or not finite(e.get("mono_first_seen")) or \
                not finite(e.get("mono_last_seen")) or e["mono_first_seen"] > e["mono_last_seen"] or \
                not imap[uid]["mono_first_seen"] <= e["mono_first_seen"] <= e["mono_last_seen"] <= imap[uid]["mono_last_seen"]:
            raise Invalid("unproved immutable first/last history invalid")
        umap[uid] = e
    prior = None
    for e in ch:
        row = e.get("observation")
        if not finite(e.get("mono")) or (prior is not None and e["mono"] < prior) or not isinstance(row, list) or \
                len(row) != 3 or not integer(row[0], 1) or not all(isinstance(x, str) for x in row[1:]):
            raise Invalid("coverage evidence malformed/reordered")
        prior = e["mono"]
    attempt_by_end = {}
    for e in ats:
        if e.get("kind") not in ("identity_scan", "resource_scan") or e.get("phase") not in ("ADMISSION", "PRE_GO", "RUNNING", "FINAL") or \
                not isinstance(e.get("inside_helper"), bool) or not isinstance(e.get("aborted"), bool) or \
                not finite(e.get("mono_start")) or not finite(e.get("mono_end")) or e["mono_end"] < e["mono_start"] or \
                (e["aborted"] and not isinstance(e.get("error"), str)) or (not e["aborted"] and e.get("error") is not None):
            raise Invalid("completed/aborted attempt missing")
        if e["kind"] == "resource_scan":
            if e["mono_end"] in attempt_by_end:
                raise Invalid("duplicate resource attempt")
            attempt_by_end[e["mono_end"]] = e
    prior_start = None
    for c in cs:
        a = attempt_by_end.pop(c.get("mono_end"), None)
        if a is None or not finite(c.get("mono_start")) or a["mono_start"] < c["mono_start"] or \
                (prior_start is not None and c["mono_start"] <= prior_start) or c.get("phase") != a["phase"] or \
                c.get("inside_helper") != a["inside_helper"] or c.get("aborted") != a["aborted"] or \
                not isinstance(c.get("complete"), bool) or not integer(c.get("incomplete_n"), 0) or \
                not isinstance(c.get("incomplete"), list) or len(c["incomplete"]) != min(c["incomplete_n"], 30):
            raise Invalid("resource observation/attempt binding invalid")
        prior_start = c["mono_start"]
        if c["aborted"]:
            if c["complete"] is not False or c.get("mono_complete") is not None or not finite(c.get("mono_aborted")) or \
                    not c["mono_start"] <= c["mono_aborted"] <= c["mono_end"] or c.get("abort_error") != a["error"]:
                raise Invalid("aborted observation presented as complete")
        elif not finite(c.get("mono_complete")) or not c["mono_start"] <= c["mono_complete"] <= c["mono_end"] or \
                c["complete"] != (c["incomplete_n"] == 0):
            raise Invalid("completed resource observation missing")
        if not all(integer(c.get(k), 0) for k in ("pids", "lane_busy", "lane_rss")) or c["lane_busy"] > 2 or \
                not all(isinstance(c.get(k), list) for k in
                    ("owned_live", "unproved_live", "group_live", "owned_zombies", "lane_pids", "lane_busy_pids", "measurements")):
            raise Invalid("resource/history hard policy or schema")
        for row in c["incomplete"]:
            if not any(same(e["observation"], row) and c["mono_start"] <= e["mono"] <= c["mono_end"] for e in ch):
                raise Invalid("missing-read coverage omitted")
        for p in c["owned_live"] + c["unproved_live"]:
            retained(p)
        if any(p["uniqueid"] not in umap for p in c["unproved_live"]):
            raise Invalid("current unproved incarnation missing historical first evidence")
        measurements, mpids, bpids, total, last = c["measurements"], [], [], 0, None
        for m in measurements:
            p = m.get("identity")
            retained(p)
            after = m.get("identity_after")
            retained(after)
            if identity(after) != identity(p):
                raise Invalid("final resource identity bracket changed")
            if not integer(m.get("rss"), 0) or not integer(m.get("cpu_ticks"), 0) or not isinstance(m.get("busy"), bool) or \
                    not finite(m.get("mono_observed")) or not c["mono_start"] <= m["mono_observed"] <= c["mono_end"] or \
                    (last is not None and m["mono_observed"] <= last) or p["pid"] in mpids:
                raise Invalid("bracketed PID-specific measurement missing")
            mpids.append(p["pid"])
            total += m["rss"]
            if m["busy"]:
                bpids.append(p["pid"])
            last = m["mono_observed"]
        if c["lane_rss"] != total or sorted(c["lane_pids"]) != sorted(mpids) or \
                sorted(c["lane_busy_pids"]) != sorted(bpids) or c["lane_busy"] != len(bpids) or \
                (last is not None and c.get("mono_last_observation") != last):
            raise Invalid("partial resource counters disagree with retained individual measurements")
    if attempt_by_end:
        raise Invalid("resource attempt omitted from observation history")
    return imap, umap, retained


def history_extensions(old, new):
    for key in ("coverage_history", "census_observations", "observation_attempts"):
        a, b = old[key], new[key]
        if len(b) < len(a) or not same(b[:len(a)], a):
            raise Invalid("postpublication history prefix changed: " + key)
    for key in ("identity_history", "unproved_history"):
        before = {e["first_identity"]["uniqueid"]: e for e in old[key]}
        after = {e["first_identity"]["uniqueid"]: e for e in new[key]}
        if not set(before) <= set(after):
            raise Invalid("historical incarnation vanished")
        for uid, first in before.items():
            last = after[uid]
            for k in ("first_identity", "mono_first_seen"):
                if not same(first[k], last[k]):
                    raise Invalid("immutable first incarnation/observation changed")
            if last["mono_last_seen"] < first["mono_last_seen"]:
                raise Invalid("last observation rewound")
            if last["mono_last_seen"] == first["mono_last_seen"] and not same(first["last_identity"], last["last_identity"]):
                raise Invalid("last incarnation changed without a new observation")
            if key == "identity_history" and (last["source"] != first["source"] or last["observations"] < first["observations"] or
                    not same(last["variants"][:len(first["variants"])], first["variants"])):
                raise Invalid("incarnation variant/count prefix changed")
    if new["history_charge_bytes"] < old["history_charge_bytes"]:
        raise Invalid("history accounting rewound")


def census_join(c, observations, subset=False):
    if not isinstance(c, dict):
        raise Invalid("embedded census missing")
    matches = [r for r in observations if (all(k in r and same(v, r[k]) for k, v in c.items()) if subset else same(c, r))]
    if len(matches) != 1:
        raise Invalid("embedded census does not join a unique retained observation")
    return matches[0]


def integrated_v15_evidence(receipt, summary, stability, cfg, go, name, samples):
    checks = {}
    baseline = receipt.get("baseline")
    if not isinstance(baseline, dict) or not finite(baseline.get("mono_complete")) or not isinstance(baseline.get("identities"), list):
        raise Invalid("complete pre-spawn baseline missing")
    baseuids = set()
    for p in baseline["identities"]:
        identity(p)
        if p["uniqueid"] in baseuids:
            raise Invalid("duplicate baseline incarnation")
        baseuids.add(p["uniqueid"])
    imap, umap, retained = histories(receipt, baseuids)
    current = summary.get("reconciliation")
    if not isinstance(current, dict):
        raise Invalid("current refusal/ACK reconciliation evidence missing")
    current_imap, current_umap, current_retained = histories(current, baseuids)
    history_extensions(receipt, current)
    if current.get("baseline_uniqueids") != sorted(baseuids):
        raise Invalid("current reconciliation baseline changed")
    owned = current.get("owned_identities")
    if not isinstance(owned, list) or not same(owned[:len(receipt["owned_identities"])], receipt["owned_identities"]):
        raise Invalid("owned registry prefix changed")
    for o in owned:
        current_retained(o["identity"])
    if not same(current.get("helpers"), receipt["helpers"]) or not same(current.get("helper_log"), receipt["helper_log"]) or \
            not same(current.get("failures"), receipt["failures"]) or not same(current.get("main_identity"), receipt["child_identity"]) or \
            not same(current.get("main_signal"), receipt["signal"]) or not same(current.get("main_stop"), receipt["stop_request"]):
        raise Invalid("current reconciliation contradicts frozen outcome/helper/stop evidence")
    obs = receipt["census_observations"]
    later = current["census_observations"]
    embedded = [receipt.get("final_census")]
    embedded += receipt.get("admission", {}).get("censuses", [])
    embedded += [receipt[k] for k in ("launch_census", "pre_go_census") if k in receipt]
    if receipt.get("clear") is not None:
        embedded.append(receipt["clear"]["census"])
    embedded += [s.get("census") for s in samples]
    for c in embedded:
        census_join(c, obs)
    for h in receipt["helpers"]:
        census_join(h["proof"], obs, subset=True)
    if summary.get("acknowledged") is True:
        for k in ("unproved_history", "coverage_history", "census_observations"):
            if not same(summary.get(k), current[k]):
                raise Invalid("duplicated current history contradicts reconciliation")
        ack = summary.get("ack_census")
        census_join(ack, later)
        final = receipt["final_census"]
        if ack.get("complete") is not True:
            raise Invalid("ACK coverage incomplete")
        fids = {p["uniqueid"] for p in final["owned_live"] + final["unproved_live"]}
        aids = {p["uniqueid"] for p in ack["owned_live"] + ack["unproved_live"]}
        if not aids <= fids or (receipt["settlement"] != "UNSETTLED" and aids) or not \
                summary["post_publish_mono"] <= ack["mono_complete"] <= summary["ack_commit"]["mono"] or \
                summary["ack_commit"]["mono"] - ack["mono_complete"] > max(1, cfg["sample_s"]):
            raise Invalid("ACK census not fresh or current blockers changed")
        if not same(summary.get("owned_live"), ack["owned_live"]) or not same(summary.get("unproved_live"), ack["unproved_live"]) or \
                not same(summary.get("contract_violations"), receipt["contract_violations"]) or \
                not same(summary.get("failure_codes"), sorted(f["code"] for f in receipt["failures"])) or \
                not same(summary.get("child_returncode"), receipt["child_returncode"]):
            raise Invalid("duplicated outcome/current blocker fields contradict receipt")
        if not same(later[-1], ack):
            raise Invalid("ACK is not the final retained resource observation")
    checks["full_history_prefix_tail_and_embedded_joins"] = True
    stable_epoch = date_epoch(stability.get("now_date"))
    good = []
    expiry = None
    helper_by_pid = {h["pid"]: h for h in receipt["helpers"]}
    purposes = {}
    for e in receipt["helper_log"]:
        purpose = e.get("purpose")
        if purpose not in ("admission", "start", "stop", "end") or purpose in purposes:
            raise Invalid("helper purpose missing/duplicated")
        purposes[purpose] = e
        if e.get("outcome") == "OK":
            h = helper_by_pid.get(e.get("pid"))
            if h is None or h.get("clock_failed") is not False or h.get("date") is None or \
                    h["mono_call_start"] != e["mono_start"] or not h["mono_proof_complete"] <= e["mono_end"]:
                raise Invalid("actual date purpose/PID/proof not joined")
            raw = bytes.fromhex(h["capture_hex"])
            if raw != (h["date"] + "\n").encode("ascii"):
                raise Invalid("actual /bin/date capture does not match exact canonical date line")
            floor = date_epoch(h["date"])
            if floor < stable_epoch:
                raise Invalid("actual date floor precedes canonical stability receipt")
            candidate = h["mono_call_start"] + cfg["admission"]["stability_max_age_s"] - (floor - stable_epoch + 1.0)
            effective = candidate if expiry is None else min(expiry, candidate)
            if not same(h.get("stability_expiry_before"), expiry) or not finite(h.get("stability_expiry_candidate")) or \
                    abs(h["stability_expiry_candidate"] - candidate) > 1e-6 or not finite(h.get("stability_expiry_effective")) or \
                    abs(h["stability_expiry_effective"] - effective) > 1e-6:
                raise Invalid("monotonic stability expiry was renewed/omitted")
            expiry = effective
            good.append((h, effective))
    for purpose, value in (("admission", receipt.get("admission", {}).get("date")),
                           ("start", receipt.get("start_date")), ("end", receipt.get("end_date"))):
        e = purposes.get(purpose)
        if e is None:
            if purpose == "admission" and name == "go_unlisted" and value is None:
                continue
            if purpose == "start" and receipt["child_pid"] is None and value is None:
                continue
            raise Invalid("mandatory actual-date purpose missing: " + purpose)
        expected = helper_by_pid[e["pid"]]["date"] if e["outcome"] == "OK" else None
        if not same(value, expected):
            raise Invalid("date field contradicts purpose/PID/capture")
    stop = receipt.get("stop_request")
    if stop is not None:
        e = purposes.get("stop")
        if e is None or not same(stop.get("date"), helper_by_pid[e["pid"]]["date"] if e["outcome"] == "OK" else None):
            raise Invalid("stop date provenance missing")
    if not same(receipt.get("stability_expiry_mono"), expiry) or not same(current.get("stability_expiry_mono"), expiry):
        raise Invalid("frozen/current stability cutoff mismatch")
    if good:
        h, _ = good[-1]
        observation = receipt.get("clock_observation")
        if not isinstance(observation, dict) or observation.get("date") != h["date"] or \
                observation.get("mono_before_read") != h["mono_call_start"] or \
                observation.get("epoch_date_floor") != date_epoch(h["date"]) or \
                not finite(observation.get("mono_after_read")) or not h["mono_proof_complete"] <= observation["mono_after_read"]:
            raise Invalid("latest actual clock observation omitted/contradictory")
    elif receipt.get("clock_observation") is not None or expiry is not None:
        raise Invalid("invented clock on deliberate helper/admission failure")
    commits = []
    for index, h in enumerate(receipt["helpers"]):
        commits.append((h.get("launch_commit"), "HELPER", index == 0,
                        cfg["helper_budget"]["call_budget_s"] + cfg["helper_budget"]["term_grace_s"]))
    launched = receipt["child_pid"] is not None
    if launched:
        commits += [(receipt.get("admission", {}).get("checked"), "ADMISSION", False, cfg["max_wall_s"] + cfg["settle_s"] + 120),
                    (receipt.get("launch_commit"), "LAUNCH", False, cfg["max_wall_s"] + cfg["settle_s"] + 120),
                    (receipt.get("go_commit"), "GO", False, None)]
    elif any(k in receipt for k in ("launch_commit", "go_commit", "go_delivery_completion")) or \
            receipt.get("admission", {}).get("checked") is not None:
        raise Invalid("unexpected child/clock commit on admission refusal")
    if summary.get("acknowledged") is True:
        commits.append((summary.get("ack_commit"), "ACK", False, 0))
    for commit, phase, first_clock_exception, required in commits:
        if not isinstance(commit, dict) or commit.get("phase") != phase or \
                not all(finite(commit.get(k)) for k in ("mono", "epoch", "required_s")) or commit["required_s"] < 0 or \
                commit["epoch"] > go["not_after_epoch"] or \
                commit["epoch"] + commit["required_s"] > cfg["owned_compute_settled_by_epoch"] - 180 or \
                (required is not None and commit["required_s"] != required):
            raise Invalid("mandatory exact-phase commit missing/late/contradictory")
        prior = [(h, cut) for h, cut in good if h["mono_proof_complete"] <= commit["mono"]]
        if not prior:
            if not (phase == "HELPER" and first_clock_exception and commit.get("stability_age_upper_s") is None):
                raise Invalid("only first actual clock helper may lack prior actual clock")
        else:
            h, cut = prior[-1]
            base = date_epoch(h["date"]) - stable_epoch
            if base < 0:
                raise Invalid("future stability receipt")
            upper = max(base + 1.0 + max(0.0, commit["mono"] - h["mono_call_start"]),
                        cfg["admission"]["stability_max_age_s"] + commit["mono"] - cut)
            if not finite(commit.get("stability_age_upper_s")) or abs(commit["stability_age_upper_s"] - upper) > 1e-6 or \
                    not 0 <= upper <= cfg["admission"]["stability_max_age_s"]:
                raise Invalid("actual date plus immutable monotonic expiry age replay failed")
    if launched:
        delivery = receipt.get("go_delivery_completion")
        if not isinstance(delivery, dict) or not all(finite(delivery.get(k)) for k in
                ("mono", "spawn_age_s", "spawn_age_bound_s", "remaining_main_runtime_s")):
            raise Invalid("actual post-write/close GO completion omitted")
        age, remaining = delivery["mono"] - receipt["mono_spawn"], receipt["mono_child_deadline"] - delivery["mono"]
        bound = min(60.0, cfg["max_wall_s"] / 2.0)
        if not (0 <= age <= bound and remaining > 0 and delivery["spawn_age_bound_s"] == bound and
                abs(delivery["spawn_age_s"] - age) <= 1e-6 and abs(delivery["remaining_main_runtime_s"] - remaining) <= 1e-6 and
                receipt["go_commit"]["mono"] <= receipt["go_written_mono"] <= delivery["mono"] and
                receipt["mono_child_deadline"] == receipt["mono_spawn"] + cfg["max_wall_s"] and
                receipt["go_commit"]["required_s"] >= max(0, receipt["mono_child_deadline"] - receipt["go_commit"]["mono"]) + cfg["settle_s"] + 120):
            raise Invalid("spawn-to-actual-GO upper age or remaining main runtime violated")
    if summary.get("acknowledged") is False:
        cause = "GO_DOES_NOT_NAME_THIS_CONFIG" if name == "go_unlisted" else "STABILITY_AGE_UNVERIFIABLE"
        if summary.get("error_code") != cause:
            raise Invalid("ACK refusal exact machine cause mismatch")
    checks["mandatory_clock_commits_provenance_cutoff_and_actual_GO_age"] = True
    if not isinstance(receipt.get("runtime_observations"), list):
        raise Invalid("runtime-obligation evidence missing")
    return checks


def common_final_evidence(receipt, summary, cfg, files, late, runfd, require):
    """Run for EVERY scenario, including all admission negatives; no early-return exemption."""
    final = receipt.get("final_census")
    if not isinstance(final, dict) or final.get("complete") is not True:
        raise Invalid("complete final census required for every scenario")
    owned, helpers = receipt.get("owned_identities"), receipt.get("helpers")
    if not isinstance(owned, list) or not isinstance(helpers, list):
        raise Invalid("complete owned/helper registry required")
    roots = {}
    for h in helpers:
        identity(h["identity"])
        if not integer(h.get("rc")) or h.get("leader_reaped") is not True or h.get("wait_lost") is not False:
            raise Invalid("integer known helper wait status missing")
        roots[h["identity"]["uniqueid"]] = (h["identity"], "helper")
    if receipt.get("child_identity") is not None:
        roots[receipt["child_identity"]["uniqueid"]] = (receipt["child_identity"], "child")
    registry = {}
    for e in owned:
        p = e.get("identity")
        identity(p)
        uid = p["uniqueid"]
        if uid in registry or not integer(e.get("root"), 1) or e["root"] not in roots or \
                not isinstance(e.get("via"), str) or not finite(e.get("first_seen_mono")):
            raise Invalid("owned registry malformed/duplicated/unrooted")
        registry[uid] = e
    for uid, (p, via) in roots.items():
        if uid not in registry or identity(registry[uid]["identity"]) != identity(p) or \
                registry[uid]["root"] != uid or registry[uid]["via"] != via:
            raise Invalid("mandatory main/helper root absent from registry")
    for p in final["owned_live"]:
        if p["uniqueid"] not in registry:
            raise Invalid("current owned incarnation omitted from registry")
    retained = receipt.get("census_observations")
    if not isinstance(retained, list) or not retained:
        raise Invalid("all resource observations required before every early return")
    enforced = [c for c in retained if c["phase"] not in ("ADMISSION", "PRE_GO")]
    maxima = receipt.get("maxima")
    if not isinstance(maxima, dict) or not enforced or not all(integer(maxima.get(k), 0) for k in
            ("lane_busy", "lane_rss", "owned_live", "charged_bytes")):
        raise Invalid("complete explicit extrema missing")
    require("common_all_partial_retry_resource_maxima", maxima["lane_busy"] == max(c["lane_busy"] for c in enforced) and
            maxima["lane_rss"] == max(c["lane_rss"] for c in enforced) and
            maxima["owned_live"] == max(len(c["owned_live"]) for c in enforced))
    require("common_min_free_explicit", integer(receipt.get("min_free"), 0) and receipt["min_free"] >= cfg["free_trip_bytes"])
    require("common_wait_registry_and_final_census", True)
    published = {"supervisor-receipt.json", "settlement.json", "settlement.json.staged"}
    before = sum(v["bytes"] for n, v in files.items() if v is not None and n not in published and n not in late)
    if any(v["nlink"] != 1 for n, v in files.items() if v is not None and n not in published):
        raise Invalid("nonpublication artifact has an undeclared hard link")
    payload = files["supervisor-receipt.json"]["bytes"] + files["settlement.json"]["bytes"]
    before_resources, br, ar = receipt.get("publication_precheck"), summary.get("publication_resources"), summary.get("ack_resources")
    current = summary["reconciliation"]
    for r in (before_resources, br, ar, current.get("publication_resources"), current.get("ack_resources")):
        if not isinstance(r, dict) or set(r) != {"charged_bytes", "lane_bytes", "free"} or \
                not all(integer(r[k], 0) for k in r):
            raise Invalid("actual historical publication/ACK accounting missing, including refused paths")
    if not same(br, current["publication_resources"]) or not same(ar, current["ack_resources"]) or \
            summary.get("publication_payload_bytes") != payload or current.get("publication_payload_bytes") != payload:
        raise Invalid("historical b/end/payload contradict current reconciliation")
    observation = current.get("last_accounting_observation")
    if not isinstance(observation, dict) or set(observation) != {"resources", "mono_observed"} or \
            not same(observation["resources"], ar) or not finite(observation.get("mono_observed")) or \
            not finite(summary.get("post_publish_mono")) or observation["mono_observed"] < summary["post_publish_mono"]:
        raise Invalid("latest actual disk accounting provenance missing")
    require("common_exact_payload_and_distinct_inode_charge", before_resources["charged_bytes"] == br["charged_bytes"] == before and
            ar["charged_bytes"] == before + payload and payload <= 4 << 20 and
            before + payload <= cfg["output_trip_bytes"] and before + payload <= RESERVATION and
            maxima["charged_bytes"] == before)
    adm = cfg["admission"]
    remaining = max(0, RESERVATION - before - payload)
    require("common_publication_reservation_free_lane_bounds", all(
            r["free"] - added - adm["outstanding_reservations_bytes"] - remaining >= cfg["free_trip_bytes"] and
            r["lane_bytes"] + added + adm["lane_outstanding_reservations_bytes"] + remaining <= cfg["lane_disk_ceiling_bytes"]
            for r, added in ((before_resources, payload), (br, payload), (ar, 0))))
    current_max = current.get("maxima")
    if not isinstance(current_max, dict) or not all(integer(current_max.get(k), 0) for k in maxima) or \
            any(current_max[k] < maxima[k] for k in maxima) or current_max["charged_bytes"] != before + payload or \
            not integer(current.get("min_free"), 0) or current["min_free"] > receipt["min_free"] or \
            current["min_free"] > min(br["free"], ar["free"]) or current["min_free"] < cfg["free_trip_bytes"]:
        raise Invalid("current extrema/free minimum absent or contradictory")
    later = current["census_observations"]
    later_enforced = [c for c in later if c["phase"] not in ("ADMISSION", "PRE_GO")]
    require("common_current_extrema_reconciled", current_max["lane_busy"] == max(c["lane_busy"] for c in later_enforced) and
            current_max["lane_rss"] == max(c["lane_rss"] for c in later_enforced) and
            current_max["owned_live"] == max(len(c["owned_live"]) for c in later_enforced))
    tfd = os.open("tmp", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=runfd)
    try:
        require("common_test_tmp_empty", os.listdir(tfd) == [])
    finally:
        os.close(tfd)


def child_observation(o, deadline, allowed_observers):
    if not isinstance(o, dict) or not integer(o.get("observer"), 1) or o["observer"] not in allowed_observers or \
            not integer(o.get("pid"), 1) or not isinstance(o.get("role"), str) or not isinstance(o.get("phase"), str) or \
            not finite(o.get("mono_start")) or not finite(o.get("observed_mono")) or \
            not o["mono_start"] <= o["observed_mono"] < deadline or not isinstance(o.get("bracket"), dict):
        raise Invalid("reported actual child observation schema/deadline")
    if o.get("error") is not None:
        if not isinstance(o["error"], str) or o.get("identity") is not None:
            raise Invalid("failed child read invented an identity")
        return None
    p, b = o.get("identity"), o["bracket"]
    identity(p)
    if set(b) != {"unique_before", "short_before", "unique_middle", "short_after", "unique_after"} or \
            not same(b["unique_before"], [p["uniqueid"], p["idversion"]]) or \
            not same(b["unique_before"], b["unique_middle"]) or not same(b["unique_before"], b["unique_after"]):
        raise Invalid("reported incarnation lacks the three equal actual unique/version reads")
    before, after = dict(b["short_before"]), dict(b["short_after"])
    for s in (before, after):
        s.update(uniqueid=p["uniqueid"], idversion=p["idversion"])
    if identity(before) != identity(after) or not same(after, p) or p["pid"] != o["pid"]:
        raise Invalid("reported current parent/group/UID/version/trace bracket changed")
    return p


def child_envelope(report, name, main, receipt, cfg, has_output):
    """Validate actual reported incarnations/private joins; report all variants for independent parent ended-identity audit."""
    if not isinstance(report, dict) or report.get("child") != "guard_qual_child_v10" or report.get("scenario") != name or \
            report.get("pid") != main["pid"] or report.get("pgid") != main["pgid"] or \
            report.get("negative_control") is not (name not in ("ok", "rc_nonzero")) or \
            report.get("evidence_failures") != []:
        raise Invalid("child report identity/negative declaration/failure evidence")
    entry, life = report.get("mono_module_entry"), report.get("mono_life_deadline")
    if not all(finite(report.get(k)) for k in ("mono_module_entry", "epoch_module_entry", "mono_life_deadline", "mono_output")) or \
            abs(life - entry - SC[name][0]) > 1e-6 or not receipt["mono_spawn"] <= entry <= report["mono_output"] < life:
        raise Invalid("shared module-entry child life not proved")
    coop = report.get("cooperative")
    reserve = min(0.25, SC[name][0] / 8.0)
    expected_coop = {"mono_life_deadline": life, "mono_work_end": life - 2 * reserve,
                     "mono_join_deadline": life - reserve, "mono_inner_deadline": life - 3 * reserve,
                     "poll_interval_s": 0.01, "deadline_extended": False}
    if not same(coop, expected_coop) or any(not isinstance(report.get(k), list) for k in
            ("descendants", "joins", "identity_waits", "ownership_edges")) or not isinstance(report.get("transports"), dict):
        raise Invalid("cooperative bounds or full child evidence lists missing")
    proto = report.get("stdin_protocol")
    line = b""
    if name in ("mutate_pin", "mutate_evidence"):
        manifest = receipt.get("go_creation_manifest")
        line = (json.dumps(manifest, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
        if len(line) > 4096 or hashlib.sha256(line).hexdigest() != receipt.get("go_creation_manifest_sha256"):
            raise Invalid("actual bounded creation line digest missing")
    if not isinstance(proto, dict) or proto.get("eof") is not True or proto.get("error") is not None or \
            proto.get("bytes") != len(b"GO\n" + line) or proto.get("sha256") != hashlib.sha256(b"GO\n" + line).hexdigest() or \
            not all(finite(proto.get(k)) for k in ("mono_start", "mono_eof", "mono_end", "deadline_mono")) or \
            not entry <= proto["mono_start"] <= proto["mono_eof"] <= proto["mono_end"] < proto["deadline_mono"] < life or \
            proto["mono_eof"] < receipt["go_written_mono"] or \
            proto.get("creation_line_bytes") != (len(line) if line else None) or \
            proto.get("creation_manifest_sha256") != (hashlib.sha256(line).hexdigest() if line else None):
        raise Invalid("exact token/optional declared line/EOF/absolute child startup evidence")
    allowed = {main["pid"]}
    allowed.update(x["pid"] for x in report["descendants"] if isinstance(x, dict) and integer(x.get("pid"), 1))
    allowed.update(x for x in (report.get("intermediate"), report.get("grandchild")) if integer(x, 1))
    observations = []
    p = child_observation(report.get("main_identity_observation"), life, allowed)
    if p is None or identity(p) != identity(main) or not same(p, report.get("main_identity")) or \
            report.get("main_identity_observed_mono") != report["main_identity_observation"]["observed_mono"]:
        raise Invalid("main reported full incarnation does not join actual launch")
    observations.append(report["main_identity_observation"])
    if has_output:
        child_observation(report.get("main_identity_at_output"), life, allowed)
        observations.append(report["main_identity_at_output"])
    for o in report["descendants"]:
        child_observation(o, life, allowed)
        observations.append(o)
    for edge in report["ownership_edges"]:
        if not isinstance(edge, dict):
            raise Invalid("child current-parent edge missing")
        ps = [child_observation(edge.get(k), life, allowed) for k in ("parent_before", "child", "parent_after")]
        observations += [edge[k] for k in ("parent_before", "child", "parent_after")]
        if edge.get("error") is None:
            a, b, c = ps
            if any(p is None for p in ps) or identity(a) != identity(c) or b["ppid"] != a["pid"] or \
                    edge.get("current_parent_verified") is not True or edge.get("same_group_verified") is not (b["pgid"] == a["pgid"]):
                raise Invalid("child asserted ownership edge without actual full parent/child brackets")
        elif not isinstance(edge.get("error"), str):
            raise Invalid("edge uncertainty missing")
    for j in report["joins"]:
        if not isinstance(j, dict) or not integer(j.get("pid"), 1) or j["pid"] not in allowed or \
                not integer(j.get("observer"), 1) or j["observer"] not in allowed or j.get("wait_options") != ["WNOHANG"] or \
                j.get("mono_life_deadline") != life or not all(finite(j.get(k)) for k in
                    ("mono_start", "mono_end", "deadline_mono", "mono_reaped")) or \
                not entry <= j["mono_start"] <= j["mono_reaped"] <= j["mono_end"] < j["deadline_mono"] < life or \
                j.get("resolved") is not True or j.get("error") is not None or j.get("unresolved_observation") is not None or \
                not integer(j.get("polls"), 1) or not integer(j.get("interruptions"), 0) or \
                not integer(j.get("wait_status"), 0) or j.get("exit_code") != os.waitstatus_to_exitcode(j["wait_status"]) or j["exit_code"] != 0:
            raise Invalid("private child join unresolved/late/nonzero/not-WNOHANG")
    for w in report["identity_waits"]:
        if not isinstance(w, dict) or not integer(w.get("pid"), 1) or w["pid"] not in allowed or \
                w.get("matched") is not True or not integer(w.get("attempts"), 1) or \
                not isinstance(w.get("errors"), list) or len(w["errors"]) >= 8 or not all(finite(w.get(k)) for k in
                    ("mono_start", "mono_end", "deadline_mono")) or not entry <= w["mono_start"] <= w["mono_end"] < w["deadline_mono"] < life:
            raise Invalid("identity polling escaped shared absolute lifetime")
        for k in ("first_observation", "last_observation"):
            child_observation(w.get(k), life, allowed)
            observations.append(w[k])
        for o in w["errors"]:
            child_observation(o, life, allowed)
            observations.append(o)
    if name in ("ownership_double", "zombie_hold"):
        mid = report.get("intermediate")
        t = report["transports"].get("intermediate_report")
        if not integer(mid, 1) or report.get("intermediate_status") != 0 or not any(
                j["pid"] == mid and j["observer"] == main["pid"] for j in report["joins"]) or \
                not isinstance(t, dict) or t.get("eof") is not True or t.get("error") is not None or \
                not integer(t.get("bytes"), 1) or t["bytes"] > 32768:
            raise Invalid("complete private intermediate transport and actual join required")
    unique = {}
    for o in observations:
        if o.get("identity") is not None:
            p = o["identity"]
            unique[identity(p)] = p
    return observations, list(unique.values())


def intended_case_evidence(name, childout, stdout, receipt, cfg, prep, preparation, files, main, late, require):
    report = childout
    if name in ("busy2", "rss"):
        lines = stdout.splitlines()
        if len(lines) != 1 or not lines[0].startswith(b"IDS "):
            raise Invalid("one complete actual IDS report required")
        report = decode(lines[0][4:])
    if report is None:
        if name in ("ok", "rc_nonzero", "mutate_pin", "mutate_evidence", "stray_file", "zombie_hold") or name.startswith("ownership_"):
            raise Invalid("mandatory intended-child report missing")
        return []
    observations, reported = child_envelope(report, name, main, receipt, cfg, childout is not None)
    imap = {e["first_identity"]["uniqueid"]: e for e in receipt["identity_history"]}
    registry = {e["identity"]["uniqueid"]: e for e in receipt["owned_identities"]}
    roots = {h["identity"]["uniqueid"] for h in receipt["helpers"]} | {main["uniqueid"]}
    extra = {uid: e for uid, e in registry.items() if uid not in roots}
    reported_core = {identity(p)[:5] for p in reported}
    reported_uids = {p["uniqueid"] for p in reported}
    if any(identity(e["identity"])[:5] not in reported_core for e in extra.values()) or any(
            identity(p)[:5] not in reported_core for p in receipt["contract_violations"]):
        raise Invalid("unreported owned incarnation or deleted reported registry entry")
    for c in receipt["census_observations"]:
        for p in c["owned_live"]:
            if p["uniqueid"] in reported_uids and p["uniqueid"] not in registry:
                raise Invalid("observed reported owned identity disappeared from the registry")
    def in_ledger(p, full=False):
        e = imap.get(p["uniqueid"])
        return e is not None and any((identity(v) == identity(p) if full else identity(v)[:5] == identity(p)[:5]) for v in e["variants"])
    def selected(role, phase=None):
        matches = {identity(o["identity"]): o["identity"] for o in observations if o.get("role") == role and
                   (phase is None or o.get("phase") == phase) and o.get("identity") is not None}
        return list(matches.values())
    if name.startswith("ownership_"):
        role, phase = ("exec_descendant", "post_exec_post_reparent") if name == "ownership_double" else ("descendant", "post_setup")
        targets = selected(role, phase)
        if len(targets) != 1 or targets[0]["pid"] != report.get("grandchild"):
            raise Invalid("full intended descendant incarnation missing")
        target = targets[0]
        final = receipt["final_census"]
        blockers = final["owned_live"] + final["unproved_live"]
        if len(blockers) != 1 or identity(blockers[0])[:5] != identity(target)[:5] or \
                blockers[0]["pgid"] != target["pgid"] or blockers[0]["traced"] != target["traced"] or \
                blockers[0]["status"] == 5 or not in_ledger(blockers[0], True):
            raise Invalid("intended full incarnation is not the sole retained live blocker")
        uid, classification = blockers[0]["uniqueid"], report.get("required_ownership_class")
        if name in ("ownership_group", "ownership_slow"):
            owned = registry.get(uid)
            if owned is None or owned["root"] != main["uniqueid"] or not in_ledger(target, True) or \
                    final["unproved_live"] != [] or len(final["owned_live"]) != 1:
                raise Invalid("group/slow requires known ownership, never an unproved alternative")
            if name == "ownership_group" and (classification != "known_group" or owned["via"] != "owned_group" or
                    owned["identity"]["pgid"] != main["pgid"]):
                raise Invalid("known same-group root proof missing")
            if name == "ownership_slow" and (classification != "known_current_parent" or
                    owned["via"] != "current_parent:%d" % main["uniqueid"] or owned["identity"]["ppid"] != main["pid"]):
                raise Invalid("slow control lacks observed current-parent ownership")
        elif classification != "known_or_unproved" or not in_ledger(target) or \
                (uid not in registry and uid not in {e["first_identity"]["uniqueid"] for e in receipt["unproved_history"]}):
            raise Invalid("fast/double permitted branch not retained as known or unproved")
        require("intended_full_descendant_and_exact_ownership_root", True)
    if name == "zombie_hold":
        targets = selected("zombie", "zombie_hold_start")
        if len(targets) != 1:
            raise Invalid("actual held-zombie incarnation missing")
        z = targets[0]
        if z["status"] != 5 or z["pid"] != report.get("grandchild") or z["uniqueid"] not in extra or \
                extra[z["uniqueid"]]["root"] != main["uniqueid"] or not in_ledger(z, True) or not any(
                    z["pid"] in c["owned_zombies"] and any(identity(p) == identity(z) and p["status"] == 5 for p in c["owned_live"])
                    for c in receipt["census_observations"]) or not any(j["pid"] == z["pid"] for j in report["joins"]):
            raise Invalid("reported full zombie/parent-root/wait evidence not observed and retained")
        require("intended_full_zombie_retained_and_reaped", True)
    if name == "busy2":
        targets = selected("busy_spinner", "pre_spin")
        if len(targets) != 1 or not in_ledger(targets[0], True):
            raise Invalid("intended pre-spin full descendant not retained")
        kid = targets[0]
        if kid["uniqueid"] not in extra or extra[kid["uniqueid"]]["root"] != main["uniqueid"] or \
                extra[kid["uniqueid"]]["via"] != "owned_group" or kid["pgid"] != main["pgid"] or \
                report.get("busy_pids") != [main["pid"], kid["pid"]] or \
                report.get("busy_gate") != "not_released_before_identity_and_IDS" or cfg["cpu_slots"] != 2:
            raise Invalid("two-slot intended busy ownership/gate proof missing")
        trip = receipt["trips"][0]
        d = trip.get("detail")
        if not isinstance(d, dict) or d.get("count") != 2 or set(d.get("pids", [])) != {main["pid"], kid["pid"]}:
            raise Invalid("BUSY cause not the exact two intended PIDs")
        pair = {identity(main)[:5], identity(kid)[:5]}
        witnessed = False
        for c in receipt["census_observations"]:
            busy = [m for m in c["measurements"] if m["busy"]]
            if {identity(m["identity"])[:5] for m in busy} == pair and len(busy) == 2 and \
                    max(m["mono_observed"] for m in busy) <= trip["mono"] <= c["mono_end"]:
                witnessed = True
        require("two_full_intended_busy_measurements_cause_first_excess", witnessed)
    if name == "rss":
        if report.get("rss_pid") != main["pid"] or report.get("allocated") != 320 * 1024 * 1024 or \
                report.get("touched_bytes") != report["allocated"] or report.get("touch_stride") != 4096 or \
                report.get("touch_writes") != 81920 or report.get("touch_write_bytes") != 81920 or \
                not integer(report.get("page_size"), 1) or report.get("term_masked_for_evidence") is not True:
            raise Invalid("actual bounded intended RSS allocation/touch evidence missing")
        for key in ("rss_before", "rss_after"):
            r = report.get(key)
            if not isinstance(r, dict) or r.get("pid") != main["pid"] or r.get("error") is not None or \
                    not integer(r.get("rss_bytes"), 0) or not finite(r.get("mono_start")) or not finite(r.get("mono_end")):
                raise Invalid("PID-specific child RSS bracket missing")
            a = child_observation(r.get("identity_before"), report["mono_life_deadline"], {main["pid"]})
            b = child_observation(r.get("identity_after"), report["mono_life_deadline"], {main["pid"]})
            if a is None or b is None or identity(a) != identity(b) or identity(a)[:5] != identity(main)[:5]:
                raise Invalid("RSS task read not bracketed by the intended incarnation")
        if report.get("rss_before_bytes") != report["rss_before"]["rss_bytes"] or \
                report.get("rss_after_bytes") != report["rss_after"]["rss_bytes"] or \
                report.get("rss_delta_bytes") != report["rss_after_bytes"] - report["rss_before_bytes"]:
            raise Invalid("RSS reported counters contradict actual bracketed task records")
        trip, witnessed = receipt["trips"][0], False
        for c in receipt["census_observations"]:
            partial = 0
            for index, m in enumerate(c["measurements"]):
                partial += m["rss"]
                following = c["measurements"][index + 1]["mono_observed"] if index + 1 < len(c["measurements"]) else c["mono_end"]
                if identity(m["identity"])[:5] == identity(main)[:5] and m["rss"] > cfg["rss_trip_bytes"] and \
                        partial == trip.get("detail") and m["mono_observed"] <= trip["mono"] <= following:
                    witnessed = True
        require("intended_PID_alone_exceeds_RSS_and_is_in_exact_first_trip_prefix", witnessed)
    if name in ("mutate_pin", "mutate_evidence"):
        creation = report.get("creation")
        manifest = receipt["go_creation_manifest"]
        path = cfg["creation_channel"]["target_path"]
        actual = files["launch.json"] if name == "mutate_evidence" else absolute_snapshot(path, 1 << 20)
        raw_original = actual["raw"][:-1]
        original = {"path": path, "inode": actual["inode"], "sha256": hashlib.sha256(raw_original).hexdigest(),
                    "bytes": len(raw_original), "nlink": 1}
        after = {"path": path, **hash_entry(actual)}
        expected_manifest = {"kind": "qualification-creation-manifest-v1", "scenario": name,
                             "preparation_sha256": preparation["sha256"], "run": prep["run"],
                             "output_root": prep["output_root"], "target": original}
        manifest_line = (json.dumps(expected_manifest, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
        if not same(manifest, expected_manifest) or len(manifest_line) > 4096:
            raise Invalid("creation manifest semantic schema/original publication binding")
        if not isinstance(creation, dict) or not same(creation.get("manifest"), manifest) or \
                creation.get("manifest_sha256") != receipt["go_creation_manifest_sha256"] or \
                creation.get("manifest_line_bytes") != len(manifest_line) or \
                creation.get("preparation_sha256") != preparation["sha256"] or \
                not same(creation.get("run"), prep["run"]) or not same(creation.get("output_root"), prep["output_root"]) or \
                not same(creation.get("original"), original) or not same(creation.get("after"), after) or \
                not same(manifest.get("target"), original) or not same(manifest.get("run"), prep["run"]) or \
                not same(manifest.get("output_root"), prep["output_root"]) or \
                manifest.get("preparation_sha256") != preparation["sha256"] or \
                not same(creation.get("preparation_facts"), {"path": QROOT + "/" + name + "/preparation.json", **hash_entry(preparation)}) or \
                creation.get("name_inode_before") != original["inode"] or creation.get("name_inode_after") != original["inode"] or \
                creation.get("append_bytes") != 1 or actual["raw"] != raw_original + b"x" or \
                not all(finite(creation.get(k)) for k in ("mono_verified", "mono_append", "mono_fsync_completed", "mono_after_verified")) or \
                not creation["mono_verified"] <= creation["mono_append"] <= creation["mono_fsync_completed"] <= creation["mono_after_verified"] < report["mono_life_deadline"]:
            raise Invalid("original approved creation identity not continuously verified BEFORE mutation")
        if name == "mutate_pin" and (not same(original, prep["fixture"]) or raw_original != FIXTURE):
            raise Invalid("mutated inode not original CREATED approved fresh fixture")
        if name == "mutate_evidence" and original["sha256"] != receipt["launch_record_sha256"]:
            raise Invalid("launch mutation not bound to original publication digest/inode")
        require("approved_original_creation_inode_and_before_append_checks", True)
    return reported


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
    if not isinstance(approval, dict) or approval.get("kind") != "v15-qualification-invocation-v1" or approval.get("scenario") != name:
        raise Invalid("approval kind/scenario")
    cp, gp, sp, pp = (snapshot(runfd, f, 1 << 20) for f in ("config.json", "go.json", "stability.json", "preparation.json"))
    require("approval_artifact_bindings", all(approval.get(k) == v["sha256"] for k, v in (
        ("config_sha256", cp), ("go_sha256", gp), ("stability_receipt_sha256", sp), ("preparation_sha256", pp))))
    package = approval.get("sources")
    if not isinstance(package, dict) or set(package) != {"supervisor", "child", "writer", "checker"}:
        raise Invalid("approval must pin the entire four-source package")
    expected_sources = {"supervisor": (SUPERVISOR, SUPERVISOR_SHA), "child": (CHILD, None),
                        "writer": (WRITER, None), "checker": (CHECKER, None)}
    source_ok = True
    for key, (path, h) in expected_sources.items():
        src = absolute_snapshot(path, 1 << 20)
        pinned = package[key]
        source_ok = source_ok and isinstance(pinned, dict) and set(pinned) == {"path", "sha256"} and \
            pinned["path"] == path and pinned["sha256"] == src["sha256"] and (h is None or h == src["sha256"])
    require("approved_sources_match_actual_bytes", source_ok)
    py = approval.get("python")
    if not isinstance(py, dict) or not isinstance(py.get("path"), str) or not py["path"].endswith("/Resources/Python.app/Contents/MacOS/Python") or os.path.realpath(py["path"]) != py["path"]:
        raise Invalid("approval interpreter must be the actual Python.app executable, not its launcher")
    require("actual_interpreter_digest", absolute_snapshot(py["path"])["sha256"] == py.get("sha256"))
    cfg, go, stability, prep = (decode(p["raw"]) for p in (cp, gp, sp, pp))
    adm = cfg["admission"]
    channel = {} if name not in ("mutate_pin", "mutate_evidence") else {
        "kind": "qualification-creation-v1", "scenario": name,
        "preparation_path": QROOT + "/" + name + "/preparation.json", "preparation_sha256": pp["sha256"],
        "target_path": QROOT + "/" + name + ("/pinned-scratch.txt" if name == "mutate_pin" else "/out/launch.json")}
    expected_cfg = config_for(name, py["path"], py["sha256"], adm["outstanding_reservations_bytes"],
                              adm["lane_outstanding_reservations_bytes"], package, pp["sha256"], channel)
    require("exact_scenario_config", same(cfg, expected_cfg))
    reservation = {"bytes": RESERVATION, "cpu_slots": cfg["cpu_slots"],
                   "outstanding_reservations_bytes": adm["outstanding_reservations_bytes"],
                   "lane_outstanding_reservations_bytes": adm["lane_outstanding_reservations_bytes"]}
    require("current_parent_allocation", same(approval.get("allocation"), reservation) and
            all(integer(adm[k], 0) for k in ("outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")))
    expected_prep = {"kind": "qualification-creation-preparation-v1", "scenario": name,
                     "run": {"path": QROOT + "/" + name, "inode": [os.fstat(runfd).st_dev, os.fstat(runfd).st_ino]},
                     "output_root": {"path": QROOT + "/" + name + "/out", "inode": [os.fstat(outfd).st_dev, os.fstat(outfd).st_ino]},
                     "fixture": None, "source_pins": package, "python": py, "allocation": reservation,
                     "negative_control": name not in ("ok", "rc_nonzero")}
    if name == "mutate_pin":
        original = prep.get("fixture") if isinstance(prep, dict) else None
        if not isinstance(original, dict) or not isinstance(original.get("inode"), list) or len(original["inode"]) != 2 or \
                not all(integer(v, 0) for v in original["inode"]):
            raise Invalid("original CREATED fixture descriptor identity missing")
        expected_prep["fixture"] = {"path": QROOT + "/" + name + "/pinned-scratch.txt", "inode": original["inode"],
                                    "bytes": len(FIXTURE), "nlink": 1, "sha256": hashlib.sha256(FIXTURE).hexdigest()}
        require("created_fixture_original_identity_retained", snapshot(runfd, "pinned-scratch.txt", 1 << 20)["inode"] == original["inode"])
    require("preparation_complete_semantics_and_approved_creation", same(prep, expected_prep))
    negative = None
    if name in NEGATIVE_PROCESS:
        negative = {"scenario": name, "kind": "ownership", "creation_channel": False}
        require("all_forking_negative_approval", approval.get("ownership_negative") is True)
    elif name in ("mutate_pin", "mutate_evidence"):
        negative = {"scenario": name, "kind": "mutation", "creation_channel": True}
        require("mutation_negative_approval", approval.get("mutation_negative") is True)
    elif name in ("date_fault", "helper_overrun", "helper_group", "helper_eof"):
        negative = {"scenario": name, "kind": "helper_injection", "creation_channel": False}
        require("helper_injection_approval", approval.get("helper_injection") is True)
    require("exact_individual_negative_GO", same(go.get("qualification_negative"), negative))
    expected_entry = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots", "creation_channel")}
    expected_entry.update({k: adm[k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
    require("go_envelope", go.get("decision") == "GO" and go.get("item") == ITEM and finite(go.get("not_after_epoch")) and
            go.get("stability_receipt_sha256") == sp["sha256"] and stability.get("verdict") == "PASS")
    require("go_exact_listing", isinstance(go.get("configs"), dict) and
            (go["configs"] == {} if name == "go_unlisted" else go["configs"] == {cp["sha256"]: expected_entry}))
    expected_root = {"kind": "v15-qualification-root", "package": "v8", "qroot": QROOT, "source_pins": package}
    qfd = directory(QROOT)
    try:
        require("fresh_package_root_marker", same(decode(snapshot(qfd, "package-root.json", 1 << 20)["raw"]), expected_root))
    finally:
        os.close(qfd)
    files = {n: snapshot(outfd, n, optional=True) for n in ("supervisor-receipt.json", "settlement.json",
              "settlement.json.staged", "launch.json", "samples.jsonl", "stdout.txt", "stderr.txt", "child-out.json", "stray.txt")}
    if any(files[n] is None for n in ("supervisor-receipt.json", "settlement.json", "settlement.json.staged")):
        raise Invalid("missing receipt or settlement publication")
    receipt = decode(files["supervisor-receipt.json"]["raw"])
    settlement = decode(files["settlement.json"]["raw"])
    summaries = sequence(snapshot(runfd, "supervisor-summary.txt", 16 << 20)["raw"])
    if len(summaries) != 1:
        raise Invalid("exactly one captured supervisor summary required")
    summary = summaries[0]
    require("complete_parent_stderr_capture", snapshot(runfd, "supervisor-stderr.txt", 16 << 20)["raw"] == b"")
    common_summary_keys = {"supervisor", "acknowledged", "exit_code", "receipt_sha256", "settlement_record_sha256",
                           "post_publish_mono", "publication_resources", "ack_resources", "publication_payload_bytes", "reconciliation"}
    expected_summary_keys = common_summary_keys | ({"reason", "clock_note", "error", "error_code"} if
        name in ("go_unlisted", "date_fault", "helper_overrun", "helper_group", "helper_eof") else
        {"settlement", "config_sha256", "receipt_bytes", "settlement_bytes", "ack_commit", "child_returncode", "failure_codes",
         "owned_live", "unproved_live", "ack_census", "contract_violations", "unproved_history", "coverage_history", "census_observations"})
    require("exact_summary_schema_no_hidden_contradictory_outcomes", set(summary) == expected_summary_keys and
            summary.get("supervisor") == "owned_supervisor_v15")
    rsha, ssha = files["supervisor-receipt.json"]["sha256"], files["settlement.json"]["sha256"]
    require("receipt_source_config_binding", receipt.get("supervisor") == "owned_supervisor_v15" and
            receipt.get("supervisor_sha256") == SUPERVISOR_SHA and receipt.get("config_sha256") == cp["sha256"])
    require("settlement_receipt_binding", settlement.get("receipt_sha256") == rsha and settlement.get("receipt") == cfg["receipt"] and
            settlement.get("config_sha256") == cp["sha256"] and settlement.get("supervisor") == "owned_supervisor_v15")
    a, b = files["settlement.json"], files["settlement.json.staged"]
    require("same_inode_staged_link", a["sha256"] == b["sha256"] and a["inode"] == b["inode"] and a["nlink"] == b["nlink"] == 2)
    require("summary_and_actual_exit", integer(actual_exit) and integer(summary.get("exit_code")) and
            actual_exit == exp["exit"] == summary["exit_code"] and
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
            same(rc, exp["rc"]) and (rc is None or integer(rc)) and same(settlement.get("child_returncode"), rc) and
            receipt.get("loop_status") == exp["loop"])
    require("mandatory_owned_date_helpers", helper_evidence(receipt, cfg, name))
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
    samples = sequence(files["samples.jsonl"]["raw"]) if files["samples.jsonl"] is not None else []
    C.update(integrated_v15_evidence(receipt, summary, stability, cfg, go, name, samples))
    common_final_evidence(receipt, summary, cfg, files, late, runfd, require)
    result["artifact_hashes"] = {n: hash_entry(v) for n, v in files.items() if v is not None}
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
    stdout = files["stdout.txt"]["raw"]
    childout = decode(files["child-out.json"]["raw"]) if files["child-out.json"] is not None else None
    if childout is not None:
        require("child_output_identity", childout.get("scenario") == name and childout.get("pid") == ident["pid"] and
                childout.get("pgid") == ident["pgid"] and
                ("child-out.json" in late or childout.get("ppid") == receipt.get("supervisor_pid")))
    result["child_reported_identities"] = intended_case_evidence(name, childout, stdout, receipt, cfg, prep, pp, files, ident, late, require)
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
    result["verdict"] = "PASS" if all(C.values()) else "FAIL"
    return result


def main():
    if os.path.abspath(__file__) != CHECKER or os.path.realpath(__file__) != CHECKER:
        raise Invalid("checker must execute at the exact approved fixed source path")
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
        except (Invalid, OSError, ValueError, KeyError, TypeError, AttributeError, IndexError, UnicodeDecodeError, OverflowError, RecursionError) as e:
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
