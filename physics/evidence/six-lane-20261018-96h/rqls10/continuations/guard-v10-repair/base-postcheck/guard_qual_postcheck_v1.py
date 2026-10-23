#!/usr/bin/env python3
"""V19 evidence-bound qualification checker, source-only. Retains owned bounded /bin/date and explicit negative controls.
Parent correction fabe57ab...4155a2 withdraws v10's narrowing; all earlier files remain immutable/unrun.
Usage: guard_qual_postcheck_v1.py SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT
Fixed no-follow root, independent actual source/config/GO/stability/preparation/evidence hashes and trusted parent
approval digest. Exact outcome sets plus complete helper settlement predicates, all unproved/owned identity evidence,
PID-specific intended cause proofs, same-inode publication and whole-sample decoding. No PASS releases reservations.
Helper overrun/group/EOF branches are reviewed injections, not evidence of a real corrupted /bin/date or kernel.
Ownership workloads require their OWN negative-control GO, are not science and never weaken global busy<=2.
Exit0 PASS,1 FAIL,2 infrastructure error. No execution authorized by this source.
"""
import bisect
import hashlib
import json
import math
import os
import datetime
import stat
import sys
import time

VERSION = "guard_qual_postcheck_v1"
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v9-v19"
ITEM = "owned_supervisor_v19 rebound creation-identity qualification"
CHILD = LANE + "/code/guard_qual_child_v12.py"
SUPERVISOR = LANE + "/code/owned_supervisor_v19.py"
WRITER = LANE + "/code/guard_qual_configs_v12.py"
CHECKER = LANE + "/code/guard_qual_check_v11.py"  # Immutable workload-provenance source, not this oracle.
VERIFIER = LANE + "/code/guard_qual_postcheck_v1.py"
SUPERVISOR_SHA = "cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93"
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
    if not isinstance(p, dict) or set(p) != {"pid", "ppid", "pgid", "uniqueid", "idversion", "euid", "ruid", "status", "traced", "comm"} or not all(integer(p.get(k), 0) for k in
        ("pid", "ppid", "pgid", "uniqueid", "euid", "ruid", "status")) or not integer(p.get("idversion")) or \
            not -(1 << 31) <= p["idversion"] < 1 << 31 or \
            not all(p[k] > 0 for k in ("pid", "uniqueid")) or not isinstance(p.get("traced"), bool) or \
            not isinstance(p.get("comm"), str):
        raise Invalid("full process incarnation missing")
    return tuple(p[k] for k in ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced"))


def identity_form(p):
    return identity(p) + (p["comm"],)


def histories(view, baseuids):
    required = ("identity_history", "identity_events", "unproved_history", "coverage_history", "census_observations", "observation_attempts")
    if any(not isinstance(view.get(k), list) for k in required):
        raise Invalid("complete current/retained identity-event history missing")
    ih, events, uh, ch, cs, ats = (view[k] for k in required)
    if len(ih) > 8192 or len(uh) > 8192 or len(ch) > 16384 or len(cs) > 4096 or len(ats) > 4096:
        raise Invalid("history entry cap")
    if not integer(view.get("history_charge_bytes"), 0) or view["history_charge_bytes"] > 4 << 20 or \
            view.get("history_overflow") is not None or view.get("history_halted", False) is not False:
        raise Invalid("history cap/overflow or missing charged bytes")
    cutoff = view.get("mono_decision", view.get("mono_snapshot"))
    start = view.get("initial_fit", {}).get("start_mono")
    if not finite(cutoff) or not finite(start) or start > cutoff:
        raise Invalid("actual identity-event observation window missing")
    imap, by_uid, unknown_refs = {}, {}, {}
    for e in ih:
        first, last, variants = e.get("first_identity"), e.get("last_identity"), e.get("variants")
        identity(first)
        identity(last)
        uid = first["uniqueid"]
        if uid in imap or last["uniqueid"] != uid or first["pid"] != last["pid"] or \
                not integer(e.get("observations"), 1) or not isinstance(e.get("source"), str) or \
                not isinstance(variants, list) or not 1 <= len(variants) <= 64:
            raise Invalid("identity ledger malformed")
        forms = [identity_form(p) for p in variants]
        if len(set(forms)) != len(forms) or any(p["uniqueid"] != uid or p["pid"] != first["pid"] for p in variants):
            raise Invalid("duplicate/inconsistent full metadata variants")
        imap[uid] = e
        by_uid[uid], unknown_refs[uid] = [], []
    introduced = {uid: set() for uid in imap}
    for index, row in enumerate(events, 1):
        if not isinstance(row, list) or len(row) != 6:
            raise Invalid("identity event row schema")
        uid, variant, status, begin, end, unproved = row
        if not integer(uid, 1) or uid not in imap or not integer(variant, 0) or \
                variant >= len(imap[uid]["variants"]) or not integer(status, 0) or \
                not finite(begin) or not finite(end) or not start <= begin <= end <= cutoff or \
                not isinstance(unproved, bool):
            raise Invalid("unbound identity event or impossible actual acquisition interval")
        if variant not in introduced[uid]:
            if variant != len(introduced[uid]) or imap[uid]["variants"][variant]["status"] != status:
                raise Invalid("variant lacks its actual first acquisition")
            introduced[uid].add(variant)
        by_uid[uid].append(index)
        if unproved:
            unknown_refs[uid].append(index)
    decoded = {}
    def event_at(ref):
        if not integer(ref, 1) or ref > len(events):
            raise Invalid("missing completed native identity reference")
        if ref not in decoded:
            uid, variant, status, begin, end, unknown = events[ref - 1]
            p = imap[uid]["variants"][variant]
            p = p if p["status"] == status else dict(p, status=status)
            decoded[ref] = {"identity": p, "mono_begin": begin, "mono_end": end, "unproved": unknown}
        return decoded[ref]
    def first_last(e, refs):
        if not refs:
            raise Invalid("identity history has no completed native event")
        first_ref = min(refs, key=lambda r: (events[r - 1][4], r))
        last_ref = max(refs, key=lambda r: (events[r - 1][4], r))
        first, last = event_at(first_ref), event_at(last_ref)
        if not integer(e.get("first_event_ref"), 1) or not integer(e.get("last_event_ref"), 1) or \
                e["first_event_ref"] != first_ref or e["last_event_ref"] != last_ref or \
                not same(e.get("first_identity"), first["identity"]) or not same(e.get("last_identity"), last["identity"]) or \
                e.get("mono_first_begin") != first["mono_begin"] or e.get("mono_first_seen") != first["mono_end"] or \
                e.get("mono_last_begin") != last["mono_begin"] or e.get("mono_last_seen") != last["mono_end"]:
            raise Invalid("count/first/last/identity interval not reconstructible from actual events")
    for uid, e in imap.items():
        if e["observations"] != len(by_uid[uid]) or introduced[uid] != set(range(len(e["variants"]))):
            raise Invalid("unsupported observation scalar or unused variant")
        first_last(e, by_uid[uid])
    def retained(p, interval=None, ref=None):
        identity(p)
        uid = p["uniqueid"]
        refs = by_uid.get(uid, [])
        if ref is not None:
            refs = [ref]
        matches = [event_at(r) for r in refs if same(event_at(r)["identity"], p)]
        if interval is not None:
            begin, end = interval
            matches = [e for e in matches if begin <= e["mono_begin"] <= e["mono_end"] <= end]
        if not matches:
            raise Invalid("full identity not joined to a compatible completed native interval")
    umap = {}
    for e in uh:
        p = e.get("first_identity")
        identity(p)
        uid = p["uniqueid"]
        if uid in umap or uid in baseuids or uid not in imap or not unknown_refs[uid]:
            raise Invalid("unproved first evidence missing/duplicated/exempted")
        first_last(e, unknown_refs[uid])
        umap[uid] = e
    if {uid for uid, refs in unknown_refs.items() if refs} != set(umap):
        raise Invalid("a completed unproved acquisition disappeared from history")
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
                    ("owned_live", "unproved_live", "owned_event_refs", "unproved_event_refs",
                     "group_live", "owned_zombies", "lane_pids", "lane_busy_pids", "measurements")):
            raise Invalid("resource/history hard policy or schema")
        if not same(c.get("raw_measurements", []), []):
            raise Invalid("pending/nullable native resource composite cannot qualify an original22 control")
        for row in c["incomplete"]:
            if not any(same(e["observation"], row) and c["mono_start"] <= e["mono"] <= c["mono_end"] for e in ch):
                raise Invalid("missing-read coverage omitted")
        for label in ("owned", "unproved"):
            if len(c[label + "_live"]) != len(c[label + "_event_refs"]):
                raise Invalid("current identity/ref arrays disagree")
            for p, ref in zip(c[label + "_live"], c[label + "_event_refs"]):
                if not integer(ref, 1):
                    raise Invalid("completed census acquisition ref absent")
                retained(p, (c["mono_start"], c["mono_end"]), ref)
                if label == "unproved" and p["uniqueid"] not in umap:
                    raise Invalid("current unproved incarnation missing historical evidence")
        measurements, mpids, bpids, total, last = c["measurements"], [], [], 0, None
        for m in measurements:
            expected_measurement = {"identity", "identity_event_ref", "before_task_event_ref", "identity_after",
                "identity_after_event_ref", "identity_after_interval", "mono_task_begin", "mono_task_end",
                "rss", "cpu_ticks", "busy", "mono_observed", "bracket_verified", "epoch_observed"}
            if not isinstance(m, dict) or set(m) != expected_measurement or m["bracket_verified"] is not True or \
                    not finite(m["epoch_observed"]):
                raise Invalid("complete verified native task composite/schema/epoch unavailable")
            p, after = m.get("identity"), m.get("identity_after")
            retained(p, (c["mono_start"], c["mono_end"]), m.get("identity_event_ref"))
            retained(after, (c["mono_start"], c["mono_end"]), m.get("identity_after_event_ref"))
            initial_event = event_at(m.get("identity_event_ref"))
            before_event = event_at(m.get("before_task_event_ref"))
            after_event = event_at(m.get("identity_after_event_ref"))
            # The pre-task acquisition belongs to THIS census and the initial acquisition precedes the task.
            if identity(before_event["identity"]) != identity(p) or identity(after) != identity(p) or \
                    not same(m.get("identity_after_interval"), [after_event["mono_begin"], after_event["mono_end"]]) or \
                    not all(finite(m.get(k)) for k in ("mono_task_begin", "mono_task_end", "mono_observed")) or \
                    not c["mono_start"] <= before_event["mono_begin"] or initial_event["mono_end"] > m["mono_task_begin"] or \
                    not before_event["mono_end"] <= m["mono_task_begin"] <= m["mono_task_end"] <= after_event["mono_begin"] <= after_event["mono_end"] <= m["mono_observed"]:
                raise Invalid("actual task/identity brackets do not causally enclose the measurement")
            if not integer(m.get("rss"), 0) or not integer(m.get("cpu_ticks"), 0) or not isinstance(m.get("busy"), bool) or \
                    not c["mono_start"] <= m["mono_observed"] <= c["mono_end"] or \
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
            raise Invalid("partial counters disagree with completed measurements")
    if attempt_by_end:
        raise Invalid("resource attempt omitted from history")
    return imap, umap, retained, event_at


def history_extensions(old, new):
    for key in ("coverage_history", "census_observations", "observation_attempts", "identity_events", "accounting_observations"):
        a, b = old[key], new[key]
        if len(b) < len(a) or not same(b[:len(a)], a):
            raise Invalid("postpublication history prefix changed: " + key)
    if any(row[3] < old["mono_decision"] for row in new["identity_events"][len(old["identity_events"]):]):
        raise Invalid("new current acquisition falsely predates frozen producer decision")
    for key in ("identity_history", "unproved_history"):
        before = {e["first_identity"]["uniqueid"]: e for e in old[key]}
        after = {e["first_identity"]["uniqueid"]: e for e in new[key]}
        if not set(before) <= set(after):
            raise Invalid("historical incarnation vanished")
        for uid, first in before.items():
            last = after[uid]
            for k in ("first_identity", "mono_first_begin", "mono_first_seen", "first_event_ref"):
                if not same(first[k], last[k]):
                    raise Invalid("immutable first actual acquisition changed")
            if last["mono_last_seen"] < first["mono_last_seen"]:
                raise Invalid("last physical observation rewound")
            advanced = any(not same(first[k], last[k]) for k in
                           ("last_identity", "mono_last_begin", "mono_last_seen", "last_event_ref"))
            if last["last_event_ref"] == first["last_event_ref"] and advanced:
                raise Invalid("same event reference claims changed native acquisition")
            if key == "identity_history":
                if last["source"] != first["source"] or last["observations"] < first["observations"] or \
                        not same(last["variants"][:len(first["variants"])], first["variants"]) or \
                        ((advanced or not same(last["variants"], first["variants"])) and last["observations"] <= first["observations"]):
                    raise Invalid("history advances without additional actual acquisition references")
    if new["history_charge_bytes"] < old["history_charge_bytes"]:
        raise Invalid("history accounting rewound")


def census_join(c, observations, subset=False):
    if not isinstance(c, dict):
        raise Invalid("embedded census missing")
    matches = [r for r in observations if (all(k in r and same(v, r[k]) for k, v in c.items()) if subset else same(c, r))]
    if len(matches) != 1:
        raise Invalid("embedded census does not join a unique retained observation")
    return matches[0]


def main_stream_evidence(receipt, summary, cfg, files, samples):
    if receipt["child_pid"] is None:
        if not same(receipt.get("streams"), {}) or not same(summary["reconciliation"].get("streams"), {}):
            raise Invalid("admission-negative MAIN stream map is not empty")
        return
    names = {"stdout", "stderr"}
    integer_keys = ("bytes_seen", "bytes_written", "cap_bytes", "pending_bytes", "prefix_bytes")
    bool_keys = ("overflow", "write_inflight", "closed", "hash_pending", "eof_seen",
                 "fsync_returned", "out_closed", "pipe_closed")
    time_keys = ("mono_created", "mono_last_update", "mono_last_read", "mono_last_write", "mono_eof", "mono_close_completed")
    keys = set(integer_keys + bool_keys + time_keys) | {"error", "sha256_prefix", "sha256_written"}
    cache = {}
    def prefix(name, count):
        if (name, count) not in cache:
            raw = files[name + ".txt"]["raw"]
            if count > len(raw):
                raise Invalid("stream claims writes beyond actual retained bytes")
            cache[(name, count)] = hashlib.sha256(memoryview(raw)[:count]).hexdigest()
        return cache[(name, count)]
    def row(name, value, observed):
        if not isinstance(value, dict) or set(value) != keys or not finite(observed) or \
                not all(integer(value[k], 0) for k in integer_keys) or not all(type(value[k]) is bool for k in bool_keys) or \
                value["cap_bytes"] != cfg[name + "_cap_bytes"] or value["error"] is not None:
            raise Invalid("complete typed healthy MAIN stream schema missing")
        seen, written, cap, pending, hashed = (value[k] for k in integer_keys)
        if not 0 <= hashed <= written <= min(seen, cap) or pending != min(seen, cap) - written or \
                value["write_inflight"] is not (pending > 0) or value["hash_pending"] is not (hashed < written) or \
                value["overflow"] is not (seen > cap) or value["sha256_prefix"] != prefix(name, hashed):
            raise Invalid("actual stream prefix/count/cap/overflow/pending relationships contradictory")
        created = value["mono_created"]
        if not finite(created) or not receipt["mono_spawn"] <= created <= observed or \
                not finite(value["mono_last_update"]) or not created <= value["mono_last_update"] <= observed:
            raise Invalid("stream actual creation/update provenance missing")
        for k in time_keys[2:]:
            t = value[k]
            if t is not None and (not finite(t) or not created <= t <= observed):
                raise Invalid("stream timestamp after containing observation")
        if seen > 0 and value["mono_last_read"] is None:
            raise Invalid("returned MAIN read has no usable producer timing")
        if written > 0 and value["mono_last_write"] is None:
            raise Invalid("returned MAIN write has no usable producer timing")
        if value["eof_seen"]:
            if value["mono_eof"] is None:
                raise Invalid("native EOF missing its healthy timing")
            if any(value[k] is not None and value[k] > value["mono_eof"] for k in ("mono_last_read", "mono_last_write")):
                raise Invalid("EOF precedes included read/write")
        elif value["mono_eof"] is not None:
            raise Invalid("EOF timestamp without native EOF")
        close = value["mono_close_completed"]
        if close is not None and any(value[k] is not None and value[k] > close for k in ("mono_last_read", "mono_last_write", "mono_eof")):
            raise Invalid("read/write/EOF transition after the stream's completed closure")
        final_hash = value["sha256_written"]
        if final_hash is not None:
            if final_hash != value["sha256_prefix"] or hashed != written or value["hash_pending"] or \
                    pending != 0 or not all(value[k] for k in ("eof_seen", "fsync_returned", "out_closed", "pipe_closed")):
                raise Invalid("final stream hash contradicts physical closure/prefix")
        if value["closed"]:
            if value["mono_close_completed"] is None or value["mono_last_update"] != value["mono_close_completed"] or \
                    final_hash is None or written != files[name + ".txt"]["bytes"] or \
                    final_hash != files[name + ".txt"]["sha256"]:
                raise Invalid("closed stream not exactly actual artifact bytes/digest")
        return value
    snapshots = [(s.get("streams"), s.get("mono")) for s in samples]
    snapshots += [(receipt.get("streams"), receipt.get("stream_snapshot_mono")),
                  (summary["reconciliation"].get("streams"), summary["reconciliation"].get("mono_snapshot"))]
    prior = {}
    overflow_seen = False
    for values, observed in snapshots:
        if not isinstance(values, dict) or set(values) != names:
            raise Invalid("complete MAIN stdout/stderr snapshot missing")
        for name in sorted(names):
            current = row(name, values[name], observed)
            before = prior.get(name)
            if before is not None:
                if current["mono_created"] != before["mono_created"] or any(current[k] < before[k] for k in
                        ("bytes_seen", "bytes_written", "prefix_bytes")) or \
                        (before["closed"] and not same(before, current)) or \
                        any(before[k] and not current[k] for k in ("overflow", "eof_seen", "fsync_returned", "out_closed", "pipe_closed")):
                    raise Invalid("MAIN stream counters/closure rewind across snapshots")
                for k in time_keys[1:]:
                    if before[k] is not None and (current[k] is None or current[k] < before[k]):
                        raise Invalid("MAIN stream observation time rewound/disappeared")
            prior[name] = current
            overflow_seen = overflow_seen or current["overflow"]
    if overflow_seen != ("STREAM_CAP" in [t["trip"] for t in receipt["trips"]]):
        raise Invalid("observed stream overflow and exact required STREAM_CAP consequence disagree")
    expected = receipt["evidence_expected_sha256"]
    for name, value in receipt["streams"].items():
        path = cfg[name]
        if value["sha256_written"] is None:
            if path in expected:
                raise Invalid("unfinished MAIN stream invented final expected digest")
        elif expected.get(path) != value["sha256_written"] or files[name + ".txt"]["sha256"] != value["sha256_written"]:
            raise Invalid("final MAIN stream hash not bound to expected map and actual artifact")


def authorization_fit_evidence(receipt, summary, cfg, go, stability, name, go_sha, stability_sha):
    fit = receipt.get("initial_fit")
    keys = {"start_epoch", "start_mono", "chunk_epoch_bound", "owned_epoch_bound", "fit_epoch", "fit_mono"}
    if not isinstance(fit, dict) or set(fit) != keys or not all(type(fit[k]) is float and finite(fit[k]) for k in keys):
        raise Invalid("actual complete initial epoch/monotonic fit telemetry absent")
    chunk = fit["start_epoch"] + cfg["max_chunk_seconds"] - 120
    owned = cfg["owned_compute_settled_by_epoch"] - 180
    end = min(chunk, owned)
    expected_fit = {"start_epoch": fit["start_epoch"], "start_mono": fit["start_mono"],
                    "chunk_epoch_bound": chunk, "owned_epoch_bound": owned,
                    "fit_epoch": end, "fit_mono": fit["start_mono"] + end - fit["start_epoch"]}
    current = summary.get("reconciliation")
    if not same(fit, expected_fit) or not isinstance(current, dict) or not same(current.get("initial_fit"), fit):
        raise Invalid("both fit bounds/monotonic mapping contradict actual initial telemetry")
    expected = None if name == "go_unlisted" else {
        "go_sha256": go_sha, "stability_receipt_sha256": stability_sha, "not_after_epoch": go["not_after_epoch"],
        "stability_epoch": date_epoch(stability["now_date"]), "stability_date": stability["now_date"]}
    if "authorization" not in receipt or "authorization" not in current or \
            not same(receipt["authorization"], expected) or not same(current["authorization"], expected):
        raise Invalid("complete actual producer authorization absent/contradictory")
    admission = receipt.get("admission")
    if not isinstance(admission, dict):
        raise Invalid("admission authorization record missing")
    if name == "go_unlisted":
        if "authorization" in admission:
            raise Invalid("deliberate unlisted GO invented an authorization")
    elif "authorization" not in admission or not same(admission["authorization"], expected):
        raise Invalid("applicable admission authorization missing before early return")
    return fit, expected


def rooted_registry(view, event_at):
    owned = view.get("owned_identities")
    helpers = view.get("helpers")
    if not isinstance(owned, list) or not isinstance(helpers, list):
        raise Invalid("complete rooted ownership registry missing")
    root_objects = {h["identity"]["uniqueid"]: (h["identity"], "helper", h.get("identity_event_ref")) for h in helpers}
    main = view.get("child_identity", view.get("main_identity"))
    if main is not None:
        identity(main)
        root_objects[main["uniqueid"]] = (main, "child", None)
    limit = view.get("mono_decision", view.get("mono_snapshot"))
    registry = {}
    keys = {"identity", "identity_event_ref", "via", "root", "first_seen_mono", "proof"}
    for entry in owned:
        if not isinstance(entry, dict) or set(entry) != keys:
            raise Invalid("typed owned registration schema missing")
        p = entry["identity"]
        identity(p)
        uid = p["uniqueid"]
        observation = event_at(entry.get("identity_event_ref"))
        if uid in registry or not same(observation["identity"], p) or not integer(entry.get("root"), 1) or \
                entry["root"] not in root_objects or not isinstance(entry.get("via"), str) or \
                not finite(entry.get("first_seen_mono")) or not observation["mono_end"] <= entry["first_seen_mono"] <= limit:
            raise Invalid("owned incarnation/reference/registration/root chronology invalid")
        registry[uid] = entry
    for uid, (p, role, ref) in root_objects.items():
        entry = registry.get(uid)
        if entry is None or entry["root"] != uid or entry["via"] != role or entry["proof"] is not None or \
                not same(entry["identity"], p) or (ref is not None and entry["identity_event_ref"] != ref):
            raise Invalid("actual mandatory main/helper root registration missing")
    for uid, entry in registry.items():
        p, via, root, proof = entry["identity"], entry["via"], entry["root"], entry["proof"]
        if uid in root_objects:
            continue
        if via == "owned_group":
            if proof is not None or p["pgid"] != root_objects[root][0]["pgid"] or \
                    registry[root]["first_seen_mono"] > entry["first_seen_mono"]:
                raise Invalid("owned-group registration not rooted in the actual known group")
        elif via.startswith("current_parent:"):
            suffix = via[len("current_parent:"):]
            if not suffix.isdigit() or suffix != str(int(suffix)):
                raise Invalid("noncanonical current-parent registration")
            parent_uid = int(suffix)
            parent = registry.get(parent_uid)
            if parent is None or parent["root"] != root or parent["first_seen_mono"] > entry["first_seen_mono"] or \
                    not isinstance(proof, dict) or set(proof) != {"parent_before_ref", "child_ref", "parent_after_ref"}:
                raise Invalid("current-parent root/actual bracket references missing")
            a, b, c = [event_at(proof[k]) for k in ("parent_before_ref", "child_ref", "parent_after_ref")]
            if a["identity"]["uniqueid"] != parent_uid or c["identity"]["uniqueid"] != parent_uid or \
                    identity(a["identity"]) != identity(c["identity"]) or identity(b["identity"]) != identity(p) or \
                    b["identity"]["ppid"] != a["identity"]["pid"] or p["ppid"] != parent["identity"]["pid"] or \
                    not a["mono_end"] <= b["mono_begin"] <= b["mono_end"] <= c["mono_begin"] <= c["mono_end"] <= entry["first_seen_mono"]:
                raise Invalid("current-parent edge is not the actual complete ordered native proof")
        else:
            raise Invalid("unknown ownership provenance")
        seen, current = set(), uid
        while current not in root_objects:
            if current in seen:
                raise Invalid("cyclic rooted ownership registry")
            seen.add(current)
            node = registry[current]
            current = node["root"] if node["via"] == "owned_group" else int(node["via"].split(":", 1)[1])
    # Every historical identity, not merely final or reported_uids, has a validated root.
    for census in view["census_observations"]:
        for p in census["owned_live"]:
            entry = registry.get(p["uniqueid"])
            if entry is None or entry["first_seen_mono"] > census["mono_end"]:
                raise Invalid("historical owned incarnation omitted from rooted registry")
    for h in helpers:
        for p in h["proof"]["owned_live"]:
            if p["uniqueid"] not in registry:
                raise Invalid("helper proof loses a historical owned registration")
    return registry


def unresolved_coverage(view, complete, baseuids, registry):
    """Classification is recomputed from baseline/registration chronology, never trusted from the event boolean.
    Acquisitions are single-threaded: one retained after the baseline completed for an incarnation outside the
    baseline and not yet rooted MUST be unproved, except the known MAIN/helper registration acquisition itself."""
    events = view["identity_events"]
    for ref, row in enumerate(events, 1):
        uid, end, unproved = row[0], row[4], row[5]
        if uid in baseuids or end <= complete or unproved:
            continue
        entry = registry.get(uid)
        if entry is None or (end < entry["first_seen_mono"] and not
                (entry["via"] in ("child", "helper") and entry["identity_event_ref"] == ref)):
            raise Invalid("post-baseline unrooted acquisition omitted from unproved coverage")
    # Every census that was not aborted classifies each non-baseline incarnation it acquired as owned or unproved.
    order = sorted(range(len(events)), key=lambda i: (events[i][3], i))
    begins = [events[i][3] for i in order]
    for c in view["census_observations"]:
        if c["aborted"]:
            continue
        covered = {p["uniqueid"] for p in c["owned_live"] + c["unproved_live"]}
        for i in order[bisect.bisect_left(begins, c["mono_start"]):bisect.bisect_right(begins, c["mono_end"])]:
            uid, end = events[i][0], events[i][4]
            if end <= c["mono_end"] and uid not in baseuids and uid not in covered:
                raise Invalid("census omits an acquired non-baseline incarnation from owned/unproved coverage")


def signal_witness(record, intended, stop, event_at):
    if not isinstance(record, dict) or record.get("sent") is not True or record.get("identity_ok") is not True or \
            record.get("error") is not None or not isinstance(stop, dict) or \
            not all(finite(record.get(k)) for k in ("mono_check", "mono_identity_begin", "mono_identity_observed", "mono_sent")):
        raise Invalid("full actual MAIN signal check/send evidence missing")
    p = record.get("identity_observed")
    if identity(p) != identity(intended) or not finite(stop.get("mono")) or \
            not stop["mono"] <= record["mono_check"] <= record["mono_identity_begin"] <= record["mono_identity_observed"] <= record["mono_sent"]:
        raise Invalid("MAIN signal fingerprint or native check/send chronology contradictory")
    event = event_at(record.get("identity_event_ref"))
    if not same(event["identity"], p) or event["mono_begin"] != record["mono_identity_begin"] or event["mono_end"] != record["mono_identity_observed"]:
        raise Invalid("MAIN signal assertion not joined to actual complete acquisition")


def helper_deadline_evidence(receipt, cfg, event_at):
    fit = receipt["initial_fit"]
    stop, exited = receipt.get("stop_request"), receipt.get("child_exit_mono")
    for h in receipt["helpers"]:
        for key, seconds in (("call_deadline", cfg["helper_budget"]["call_budget_s"]),
                             ("cleanup_deadline", cfg["helper_budget"]["term_grace_s"])):
            value = h.get(key)
            if value is None:
                if key == "call_deadline" or h.get("mono_cleanup_start") is not None or h.get("mono_cleanup_deadline") is not None:
                    raise Invalid("applicable actual helper deadline telemetry missing")
                continue
            if not isinstance(value, dict) or set(value) != {"mono_created", "seconds", "until", "end"} or \
                    not all(finite(value.get(k)) for k in value) or value["seconds"] != seconds:
                raise Invalid("actual helper deadline schema/duration invalid")
            created = value["mono_created"]
            bounds = [fit["fit_mono"]]
            if isinstance(stop, dict) and finite(stop.get("mono")) and stop["mono"] <= created:
                bounds.append(stop["mono"] + cfg["settle_s"])
            if finite(exited) and exited <= created:
                bounds.append(exited + cfg["settle_s"])
            until = min(bounds)
            if value["until"] != until or value["end"] != min(created + seconds, until):
                raise Invalid("helper deadline detached from its real creation/then-applicable fit/grace")
            if key == "call_deadline":
                commit = h["launch_commit"]
                if not all(finite(h.get(k)) for k in ("mono_call_start", "mono_spawn", "mono_pid_registered")) or \
                        h.get("mono_call_deadline") != value["end"] or \
                        not h["mono_call_start"] <= created <= commit["mono"] <= h["mono_spawn"] <= h["mono_pid_registered"]:
                    raise Invalid("helper actual call/spawn/registration chronology contradictory")
                first = event_at(h.get("identity_event_ref"))
                if not same(first["identity"], h["identity"]) or first["mono_begin"] < h["mono_pid_registered"] or \
                        not finite(h.get("mono_reaped")) or first["mono_end"] > h["mono_reaped"]:
                    raise Invalid("helper initial acquisition not bound to its native spawn/reap")
            elif not finite(h.get("mono_cleanup_start")) or h.get("mono_cleanup_deadline") != value["end"] or \
                    h["mono_cleanup_start"] > created:
                raise Invalid("helper cleanup deadline not its actual cleanup interval")
        sig = h.get("signal")
        if isinstance(sig, dict) and sig.get("sent") is True:
            if sig.get("identity_ok") is not True or identity(sig.get("identity_observed")) != identity(h["identity"]) or \
                    not all(finite(sig.get(k)) for k in ("mono_check", "mono_identity_begin", "mono_identity_observed", "mono_sent")) or \
                    not h["mono_cleanup_start"] <= sig["mono_check"] <= sig["mono_identity_begin"] <= sig["mono_identity_observed"] <= sig["mono_sent"] <= h["cleanup_deadline"]["end"]:
                raise Invalid("helper actual TERM fingerprint/check/send/grace proof missing")
            event = event_at(sig.get("identity_event_ref"))
            if not same(event["identity"], sig["identity_observed"]) or \
                    event["mono_begin"] != sig["mono_identity_begin"] or event["mono_end"] != sig["mono_identity_observed"]:
                raise Invalid("helper TERM not the referenced complete native acquisition")


def native_result_evidence(view):
    if view.get("timing_failed") is not False or not same(view.get("raw_acquisitions"), []):
        raise Invalid("nullable/pending native timing evidence cannot qualify an original22 control")
    free = view.get("last_native_free")
    last = view.get("last_accounting_observation")
    if last is None:
        rows = view.get("accounting_observations", [])
        last = rows[-1] if rows else None
    if not isinstance(free, dict) or set(free) != {"f_bavail", "f_frsize", "free"} or \
            not all(integer(v, 0) for v in free.values()) or free["free"] != free["f_bavail"] * free["f_frsize"] or \
            last is None or free["free"] != last["resources"]["free"]:
        raise Invalid("actual native free result not joined to the latest actual accounting")
    main = view.get("child_identity", view.get("main_identity"))
    wait = view.get("main_wait")
    if main is None:
        if wait is not None:
            raise Invalid("no MAIN incarnation but native MAIN wait invented")
    else:
        keys = {"pid", "native_wait_result", "raw_wait_status", "leader_reaped", "rc", "mono_reaped", "epoch_reaped"}
        if not isinstance(wait, dict) or set(wait) != keys or wait["pid"] != main["pid"] or type(wait["leader_reaped"]) is not bool:
            raise Invalid("complete native MAIN wait latch missing")
        result = wait["native_wait_result"]
        if not isinstance(result, list) or len(result) != 2 or not all(integer(v, 0) for v in result):
            raise Invalid("raw destructive MAIN wait result missing")
        if wait["leader_reaped"]:
            status = wait["raw_wait_status"]
            if not integer(status, 0) or result != [main["pid"], status] or \
                    not (os.WIFEXITED(status) or os.WIFSIGNALED(status)) or not integer(wait["rc"]) or \
                    wait["rc"] != os.waitstatus_to_exitcode(status) or not all(finite(wait[k]) for k in ("mono_reaped", "epoch_reaped")):
                raise Invalid("known MAIN terminal status/time contradiction")
        elif result != [0, 0] or any(wait[k] is not None for k in ("raw_wait_status", "rc", "mono_reaped", "epoch_reaped")):
            raise Invalid("unreaped MAIN incorrectly claims a destructive terminal result")
        if "child_returncode" in view and (not same(wait["rc"], view["child_returncode"]) or \
                not same(wait["mono_reaped"], view.get("child_exit_mono")) or \
                not same(wait["epoch_reaped"], view.get("child_exit_epoch"))):
            raise Invalid("MAIN wait latch contradicts duplicated receipt exit fields")
    for h in view["helpers"]:
        status = h.get("raw_wait_status")
        if not integer(status, 0) or not same(h.get("native_wait_result"), [h["pid"], status]) or \
                not (os.WIFEXITED(status) or os.WIFSIGNALED(status)) or not integer(h.get("rc")) or \
                h["rc"] != os.waitstatus_to_exitcode(status) or not finite(h.get("epoch_reaped")) or \
                not integer(h.get("raw_identity_ref"), 1) or h.get("clockless_probe_done") is not False or \
                not integer(h.get("clockless_probe_count"), 0) or h["clockless_probe_count"] != 0 or \
                not same(h.get("endpoint_errors"), []):
            raise Invalid("helper raw wait/identity/clockless/endpoint telemetry missing or not a healthy original22 path")


def integrated_v19_evidence(receipt, summary, stability, cfg, go, name, samples):
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
    imap, umap, retained, event_at = histories(receipt, baseuids)
    current = summary.get("reconciliation")
    current_keys = {"owned_identities", "unproved_history", "identity_history", "coverage_history", "census_observations",
                    "observation_attempts", "helpers", "helper_log", "failures", "main_identity", "main_signal", "main_stop",
                    "baseline_uniqueids", "stability_expiry_mono", "history_charge_bytes", "history_cap_bytes", "history_halted",
                    "history_overflow", "publication_resources", "ack_resources", "publication_payload_bytes",
                    "last_accounting_observation", "maxima", "min_free", "identity_events", "accounting_observations",
                    "min_free_witness", "authorization", "initial_fit", "streams", "mono_snapshot",
                    "timing_failed", "raw_acquisitions", "last_native_free", "main_wait"}
    if not isinstance(current, dict) or set(current) != current_keys or current["history_halted"] is not False or \
            not integer(current["history_cap_bytes"], 0) or current["history_cap_bytes"] != 4 << 20:
        raise Invalid("mandatory complete current refusal/ACK reconciliation schema missing")
    current_imap, current_umap, current_retained, current_event_at = histories(current, baseuids)
    native_result_evidence(receipt)
    native_result_evidence(current)
    registry = rooted_registry(receipt, event_at)
    current_registry = rooted_registry(current, current_event_at)
    history_extensions(receipt, current)
    unresolved_coverage(receipt, baseline["mono_complete"], baseuids, registry)
    unresolved_coverage(current, baseline["mono_complete"], baseuids, current_registry)
    refs = baseline.get("event_refs")
    if not isinstance(refs, list) or len(refs) != len(baseline["identities"]):
        raise Invalid("baseline actual acquisition references missing")
    # The baseline is the LAST completed identity scan before its own completion clock, inside the observation window.
    complete = baseline["mono_complete"]
    scans = [a for a in receipt["observation_attempts"] if a["kind"] == "identity_scan" and a["mono_end"] <= complete]
    scan = scans[-1] if scans else None
    if scan is None or scan["aborted"] is not False or scan["phase"] != "ADMISSION" or scan["inside_helper"] is not False or \
            not receipt["initial_fit"]["start_mono"] <= scan["mono_start"] or not complete <= receipt["mono_decision"]:
        raise Invalid("baseline not completed by its actual pre-spawn identity scan inside the observation window")
    for p, ref in zip(baseline["identities"], refs):
        if not integer(ref, 1):
            raise Invalid("baseline acquisition ref not an integer")
        retained(p, (scan["mono_start"], scan["mono_end"]), ref)
    creations = [e.get("mono_start") if isinstance(e, dict) else None for e in receipt["helper_log"]]
    creations += [h.get("mono_call_start") for h in receipt["helpers"]]
    if receipt["child_pid"] is not None:
        creations += [receipt.get("mono_spawn"),
                      receipt["launch_commit"].get("mono") if isinstance(receipt.get("launch_commit"), dict) else None]
    if any(not finite(t) or t < complete for t in creations):
        raise Invalid("pre-spawn baseline completed after a helper or MAIN creation")
    if not same(current.get("baseline_uniqueids"), sorted(baseuids)):
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
    if not same(current.get("main_wait"), receipt.get("main_wait")):
        raise Invalid("current MAIN wait result contradicts the original22 frozen outcome")
    embedded = [receipt.get("final_census")]
    embedded += receipt.get("admission", {}).get("censuses", [])
    embedded += [receipt[k] for k in ("launch_census", "pre_go_census") if k in receipt]
    if receipt.get("clear") is not None:
        embedded.append(receipt["clear"]["census"])
    embedded += [s.get("census") for s in samples]
    for c in embedded:
        census_join(c, obs)
    for h in receipt["helpers"]:
        proof_census = census_join(h["proof"], obs, subset=True)
        if h.get("settled") is True:
            # Settlement completes only after the leader reap and the retained ownership census, inside its deadline.
            deadline = h.get("call_deadline") if h.get("clock_failed") is False else h.get("cleanup_deadline")
            if not isinstance(deadline, dict) or not all(finite(v) for v in (
                    h.get("mono_reaped"), proof_census.get("mono_start"), proof_census.get("mono_complete"),
                    h.get("mono_proof_complete"), deadline.get("end"))) or \
                    not h["mono_reaped"] <= proof_census["mono_start"] <= proof_census["mono_complete"] <= \
                        h["mono_proof_complete"] <= deadline["end"]:
                raise Invalid("settled helper completion precedes its reap/ownership census or exceeds its deadline")
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
    helper_deadline_evidence(receipt, cfg, event_at)
    if isinstance(receipt.get("signal"), dict) and receipt["signal"].get("sent") is True:
        signal_witness(receipt["signal"], receipt["child_identity"], receipt["stop_request"], event_at)
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
                commit["epoch"] + commit["required_s"] > receipt["initial_fit"]["fit_epoch"] or \
                commit["mono"] + commit["required_s"] > receipt["initial_fit"]["fit_mono"] or \
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


def accounting_history(view):
    rows = view.get("accounting_observations")
    cutoff = view.get("mono_decision", view.get("mono_snapshot"))
    start = view["initial_fit"]["start_mono"]
    if not isinstance(rows, list) or not rows or not finite(cutoff):
        raise Invalid("actual complete accounting history missing")
    keys = {"id", "phase", "inside_helper", "mono_begin", "mono_observed", "resources", "retained", "returned"}
    prior = start
    for index, event in enumerate(rows, 1):
        resources = event.get("resources") if isinstance(event, dict) else None
        if not isinstance(event, dict) or set(event) != keys or not integer(event.get("id"), 1) or event["id"] != index or \
                event.get("phase") not in ("ADMISSION", "PRE_GO", "RUNNING", "FINAL") or not isinstance(event.get("inside_helper"), bool) or \
                event.get("retained") is not True or event.get("returned") is not True or \
                not all(finite(event.get(k)) for k in ("mono_begin", "mono_observed")) or \
                not prior <= event["mono_begin"] <= event["mono_observed"] <= cutoff or \
                not isinstance(resources, dict) or set(resources) != {"charged_bytes", "lane_bytes", "free"} or \
                not all(integer(resources[k], 0) for k in resources):
            raise Invalid("accounting native values/chronology/type/return provenance invalid")
        prior = event["mono_observed"]
    witness = min(rows, key=lambda event: (event["resources"]["free"], event["id"]))
    if not integer(view.get("min_free"), 0) or view["min_free"] != witness["resources"]["free"] or \
            not same(view.get("min_free_witness"), witness):
        raise Invalid("minimum FREE not exactly its retained actual establishing observation")
    return rows


def accounting_join(resources, ref, rows, phase, after, before):
    """A stage's resources join ITS actual non-helper accounting call inside the stage's causal window."""
    if not integer(ref, 1) or ref > len(rows) or not same(resources, rows[ref - 1]["resources"]):
        raise Invalid("resource dictionary does not join its actual accounting observation")
    event = rows[ref - 1]
    if event["phase"] != phase or event["inside_helper"] is not False or not finite(after) or not finite(before) or \
            not after <= event["mono_begin"] or not event["mono_observed"] <= before:
        raise Invalid("accounting observation not from its stage phase, non-helper context and causal window")


def common_final_evidence(receipt, summary, cfg, files, late, runfd, require, samples):
    """Run for EVERY scenario, including all admission negatives; no early-return exemption."""
    final = receipt.get("final_census")
    if not isinstance(final, dict) or final.get("complete") is not True:
        raise Invalid("complete final census required for every scenario")
    if receipt.get("child_pid") is None:
        main_fields = {"child_pid", "child_identity", "child_returncode", "child_exit_mono", "child_exit_epoch",
                       "wait_status_lost", "stop_request", "signal", "streams", "samples_written", "samples_bytes",
                       "artifacts", "evidence_expected_sha256"}
        main_paths = [cfg[k] for k in ("stdout", "stderr", "samples", "launch_record")] + [o["path"] for o in cfg["outputs"]]
        if not main_fields <= set(receipt) or not same(receipt["artifacts"], {p: None for p in main_paths}) or \
                not same(receipt["evidence_expected_sha256"], {}) or not same(receipt["streams"], {}) or \
                not all(integer(receipt.get(k), 0) and receipt[k] == 0 for k in ("samples_written", "samples_bytes")) or \
                any(receipt[k] is not None for k in ("child_pid", "child_identity", "child_returncode", "child_exit_mono",
                                                     "child_exit_epoch", "stop_request", "signal")) or receipt["wait_status_lost"] is not False:
            raise Invalid("not-launched MAIN artifact/digest/stream/counter/wait manifest missing or contradictory")
        # This says nothing is launched for MAIN. Actual helper/date/ownership histories above remain mandatory and untouched.
        require("admission_negative_MAIN_manifest_and_zero_counters", True)
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
    accounting = accounting_history(receipt)
    current_accounting = accounting_history(summary["reconciliation"])
    if len(current_accounting) != len(accounting) + 2 or not same(current_accounting[:len(accounting)], accounting):
        raise Invalid("original22 exact pre-publication/b/end accounting stages not joined")
    if maxima["charged_bytes"] != max(event["resources"]["charged_bytes"] for event in accounting):
        raise Invalid("frozen charged maximum not reconstructed from its complete accounting history")
    accounting_join(receipt["publication_precheck"], receipt.get("publication_precheck_ref"), accounting,
                    "FINAL", final.get("mono_end"), receipt.get("mono_decision"))
    if receipt["publication_precheck_ref"] != len(accounting):
        raise Invalid("precheck is not the final frozen accounting observation")
    if receipt["child_pid"] is None:
        if len(accounting) != 1 or receipt["min_free"] != receipt["publication_precheck"]["free"]:
            raise Invalid("admission-negative FREE minimum contradicts its actual sole accounting")
    else:
        admission = receipt["admission"]
        dates = [e for e in receipt["helper_log"] if isinstance(e, dict) and e.get("purpose") == "admission"]
        censuses = admission.get("censuses") or []
        accounting_join(admission.get("resources"), admission.get("accounting_ref"), accounting, "ADMISSION",
                        dates[0].get("mono_end") if len(dates) == 1 else None,
                        min([admission["checked"]["mono"]] + [c["mono_start"] for c in censuses[:1]]))
        accounting_join(receipt.get("launch_resources"), receipt.get("launch_accounting_ref"), accounting, "PRE_GO",
                        receipt["launch_census"]["mono_end"], receipt["launch_commit"]["mono"])
        accounting_join(receipt.get("pre_go_resources"), receipt.get("pre_go_accounting_ref"), accounting, "PRE_GO",
                        receipt["pre_go_census"]["mono_end"], receipt["go_commit"]["mono"])
        for sample in samples:
            accounting_join(sample.get("resources"), sample.get("accounting_ref"), accounting, "RUNNING",
                            sample["census"]["mono_end"], sample["mono"])
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
    if not same(observation, current_accounting[-1]) or not same(br, current_accounting[-2]["resources"]) or \
            not same(ar, current_accounting[-1]["resources"]) or not finite(summary.get("post_publish_mono")) or \
            observation["mono_observed"] < summary["post_publish_mono"]:
        raise Invalid("actual historical b/end and last accounting observation not exactly joined")
    accounting_join(br, len(current_accounting) - 1, current_accounting, "FINAL",
                    receipt.get("mono_decision"), summary["post_publish_mono"])
    accounting_join(ar, len(current_accounting), current_accounting, "FINAL",
                    summary["post_publish_mono"], current.get("mono_snapshot"))
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
            current_max["charged_bytes"] != max(event["resources"]["charged_bytes"] for event in current_accounting) or \
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


def private_transport(value, coop, role, entry, report_mono, expected=None, extra=None, cap=32768, *, kind):
    """Validate the retained ORIGINAL bytes and their actual fixed-role read/write completion evidence.
    The caller names the producer interface: a read must prove literal EOF, a write must prove its return."""
    common = {"mono_start", "deadline_mono", "deadline_role", "bytes", "sha256", "raw_hex", "error", "mono_end"}
    extras = set(extra or ())
    if not isinstance(value, dict) or not integer(value.get("bytes"), 0) or value["bytes"] > cap or \
            not isinstance(value.get("raw_hex"), str) or len(value["raw_hex"]) != 2 * value["bytes"] or \
            any(c not in "0123456789abcdef" for c in value["raw_hex"]) or value.get("error") is not None or \
            value.get("deadline_role") != role or not same(value.get("deadline_mono"), coop[role]) or \
            not all(finite(value.get(k)) for k in ("mono_start", "mono_end")) or \
            not entry <= value["mono_start"] <= value["mono_end"] <= report_mono:
        raise Invalid("private transport bytes/error/original role/deadline/containing chronology")
    raw = bytes.fromhex(value["raw_hex"])
    if value["sha256"] != hashlib.sha256(raw).hexdigest() or (expected is not None and raw != expected):
        raise Invalid("private transport original content/digest")
    if kind == "read":
        if set(value) != common | {"eof", "mono_eof"} | extras or value["eof"] is not True or \
                not finite(value.get("mono_eof")) or \
                not value["mono_start"] <= value["mono_eof"] < coop[role] or \
                not value["mono_eof"] <= value["mono_end"]:
            raise Invalid("private read did not prove actual EOF before original cutoff")
    elif kind == "write":
        if set(value) != common | {"returned"} | extras or value.get("returned") is not True or \
                not value["mono_end"] < coop[role]:
            raise Invalid("private write incomplete/late or wrong exact schema")
    else:
        raise Invalid("private transport interface kind unknown")
    return raw


def private_join(j, source_observations, coop, entry, report_mono, allowed):
    bindings = {"busy_spinner": ("main_join", "main", ["main", "post_go"], ["busy_spinner", "pre_spin"]),
        "intermediate": ("main_join", "main", ["main", "post_go"], ["intermediate", "self_post_setup"]),
        "zombie": ("inner_zombie_join", "intermediate", ["intermediate", "self_post_setup"],
                   ["zombie", "zombie_hold_start"])}
    fields = {"role", "join_role", "observer_role", "observer", "pid", "deadline_role", "deadline_mono",
        "mono_life_deadline", "expected_observer_source", "expected_observer_identity", "intended_source",
        "intended_identity", "mono_start", "mono_end", "precheck", "precheck_ok", "wait_options",
        "wait_options_value", "calls", "interruptions", "first_call", "last_call", "resolved", "wait_status",
        "exit_code", "mono_reaped", "error", "unresolved_observation", "unresolved_observation_error"}
    if not isinstance(j, dict) or set(j) != fields or j.get("role") not in bindings:
        raise Invalid("private join exact schema/declared role")
    join_role, observer_role, observer_source, intended_source = bindings[j["role"]]
    deadline_role = "mono_inner_deadline" if join_role == "inner_zombie_join" else "mono_join_deadline"
    if j["join_role"] != join_role or j["observer_role"] != observer_role or \
            not same(j["expected_observer_source"], observer_source) or not same(j["intended_source"], intended_source) or \
            j["deadline_role"] != deadline_role or not same(j["deadline_mono"], coop[deadline_role]) or \
            not same(j["mono_life_deadline"], coop["mono_life_deadline"]) or \
            not integer(j["observer"], 1) or j["observer"] not in allowed or not integer(j["pid"], 1) or j["pid"] not in allowed:
        raise Invalid("private join changed canonical role/observer/source/deadline")
    sources = []
    for source in (observer_source, intended_source):
        matches = [o for o in source_observations if o.get("role") == source[0] and o.get("phase") == source[1]]
        if len(matches) != 1 or matches[0].get("identity") is None:
            raise Invalid("private join lacks unique original intended observer/target source")
        sources.append(matches[0])
    observer, intended = [o["identity"] for o in sources]
    if not same(j["expected_observer_identity"], observer) or not same(j["intended_identity"], intended) or \
            observer["pid"] != j["observer"] or intended["pid"] != j["pid"] or \
            not all(finite(j.get(k)) for k in ("mono_start", "mono_end", "mono_reaped")) or \
            not entry <= j["mono_start"] <= j["mono_reaped"] <= j["mono_end"] <= report_mono or \
            not j["mono_reaped"] < coop[deadline_role] or j["precheck_ok"] is not True or \
            j["resolved"] is not True or j["error"] is not None or j["unresolved_observation"] is not None or \
            j["unresolved_observation_error"] is not None or not same(j["wait_options"], ["WNOHANG"]) or \
            not integer(j["wait_options_value"], 0) or j["wait_options_value"] != os.WNOHANG or \
            not integer(j["calls"], 1) or not integer(j["interruptions"], 0) or j["interruptions"] >= j["calls"] or \
            not integer(j["wait_status"], 0) or not integer(j["exit_code"]) or \
            os.waitstatus_to_exitcode(j["wait_status"]) != j["exit_code"] or j["exit_code"] != 0:
        raise Invalid("private join unresolved/nonzero/late/unbound or invalid native wait status")
    p = j["precheck"]
    if not isinstance(p, dict) or set(p) != {"phase", "mono_start", "parent_before", "target", "parent_after", "error", "mono_end"} or \
            p["phase"] != join_role + "_precheck" or p["error"] is not None or \
            not all(finite(p.get(k)) for k in ("mono_start", "mono_end")) or \
            not j["mono_start"] <= p["mono_start"] <= p["mono_end"] <= j["mono_reaped"]:
        raise Invalid("private join original pre-wait bracket missing/late")
    observations = [p[k] for k in ("parent_before", "target", "parent_after")]
    identities = [child_observation(o, coop[deadline_role], allowed) for o in observations]
    if any(v is None for v in identities) or identity(identities[0]) != identity(observer) or \
            identity(identities[2]) != identity(observer) or identity(identities[1]) != identity(intended) or \
            identities[1]["ppid"] != observer["pid"] or any(o["observer"] != observer["pid"] for o in observations) or \
            any(o["role"] != role for o, role in zip(observations, (observer_role, j["role"], observer_role))) or \
            [o["phase"] for o in observations] != [p["phase"] + "_parent_before", p["phase"], p["phase"] + "_parent_after"] or \
            not p["mono_start"] <= observations[0]["mono_start"] <= observations[0]["observed_mono"] <= \
                observations[1]["mono_start"] <= observations[1]["observed_mono"] <= observations[2]["mono_start"] <= \
                observations[2]["observed_mono"] <= p["mono_end"] or \
            any(o["observed_mono"] > j["mono_start"] for o in sources):
        raise Invalid("private join full observer/child incarnation/current-parent/chronology mismatch")
    call_fields = {"index", "pid", "options", "mono_call", "mono_return", "returned_pid", "returned_status", "error"}
    for call in (j["first_call"], j["last_call"]):
        if not isinstance(call, dict) or set(call) != call_fields or not integer(call["index"], 1) or \
                not integer(call["pid"], 1) or call["pid"] != intended["pid"] or \
                not integer(call["options"], 0) or call["options"] != os.WNOHANG or \
                not all(finite(call[k]) for k in ("mono_call", "mono_return")) or \
                not p["mono_end"] <= call["mono_call"] <= call["mono_return"] <= j["mono_end"] or \
                not call["mono_call"] < coop[deadline_role]:
            raise Invalid("private join actual native wait call/deadline evidence")
        if call["error"] is None:
            if not integer(call["returned_pid"], 0) or call["returned_pid"] not in (0, intended["pid"]) or \
                    not integer(call["returned_status"], 0) or \
                    (call["returned_pid"] == 0 and call["returned_status"] != 0):
                raise Invalid("private join raw native wait result")
        elif not isinstance(call["error"], str) or call["returned_pid"] is not None or call["returned_status"] is not None or \
                j["interruptions"] < 1:
            raise Invalid("private join raw interruption evidence")
    first, last = j["first_call"], j["last_call"]
    if first["index"] != 1 or last["index"] != j["calls"] or \
            (j["calls"] == 1 and not same(first, last)) or \
            (j["calls"] > 1 and (first["returned_pid"] not in (None, 0) or first["mono_return"] > last["mono_call"])) or \
            last["error"] is not None or last["returned_pid"] != intended["pid"] or \
            last["returned_status"] != j["wait_status"] or not same(last["mono_return"], j["mono_reaped"]):
        raise Invalid("private join first/final actual call/reaped-result join")
    return observations


def private_members(container, source_observations, coop, entry, report_mono, allowed):
    """All included native acquisition/edge/poll/join evidence finishes before THIS original containing report."""
    observations = []
    for o in container["descendants"]:
        # Refusal is derived from the included record itself, never from an independently empty failure list.
        if child_observation(o, coop["mono_life_deadline"], allowed) is None:
            raise Invalid("included private acquisition failed although the report claims no evidence failure")
        observations.append(o)
    for edge in container["ownership_edges"]:
        if not isinstance(edge, dict) or set(edge) != {"phase", "parent_before", "child", "parent_after",
                "current_parent_verified", "same_group_verified", "error"}:
            raise Invalid("private current-parent edge exact schema")
        items = [edge[k] for k in ("parent_before", "child", "parent_after")]
        ps = [child_observation(o, coop["mono_life_deadline"], allowed) for o in items]
        observations.extend(items)
        target_role = "descendant" if edge["phase"] in ("post_setup", "hold_end") else \
            "exec_descendant" if edge["phase"] in ("pre_exec", "post_exec_current_parent") else None
        parent_role = "main" if target_role == "descendant" else "intermediate"
        if target_role is None or [o["role"] for o in items] != [parent_role, target_role, parent_role] or \
                [o["phase"] for o in items] != [edge["phase"] + "_parent_before", edge["phase"], edge["phase"] + "_parent_after"]:
            raise Invalid("private current-parent edge changed its declared role/phase")
        if edge["error"] is not None:
            raise Invalid("included private ownership edge failed although the report claims no evidence failure")
        a, b, c = ps
        if any(p is None for p in ps) or identity(a) != identity(c) or b["ppid"] != a["pid"] or \
                any(o["observer"] != a["pid"] for o in items) or \
                edge["current_parent_verified"] is not True or edge["same_group_verified"] is not (b["pgid"] == a["pgid"]) or \
                not items[0]["observed_mono"] <= items[1]["mono_start"] <= \
                    items[1]["observed_mono"] <= items[2]["mono_start"]:
            raise Invalid("private asserted current-parent edge without actual full ordered brackets")
    for j in container["joins"]:
        observations.extend(private_join(j, source_observations, coop, entry, report_mono, allowed))
    wait_fields = {"role", "pid", "phase", "observer", "deadline_mono", "deadline_role", "mono_start", "mono_end",
                   "attempts", "first_observation", "last_observation", "errors", "matched"}
    for w in container["identity_waits"]:
        if not isinstance(w, dict) or set(w) != wait_fields or not integer(w["pid"], 1) or w["pid"] not in allowed or \
                not integer(w["observer"], 1) or w["observer"] not in allowed or w["matched"] is not True or \
                not integer(w["attempts"], 1) or w["errors"] != [] or \
                w["deadline_role"] != "mono_inner_deadline" or not same(w["deadline_mono"], coop["mono_inner_deadline"]) or \
                (w["role"], w["phase"]) not in (("zombie", "zombie_hold_start"), ("exec_descendant", "post_exec_pre_reparent")) or \
                not all(finite(w.get(k)) for k in ("mono_start", "mono_end")) or \
                not entry <= w["mono_start"] <= w["mono_end"] <= report_mono or w["mono_end"] >= coop["mono_inner_deadline"]:
            raise Invalid("private identity polling original deadline/role/report/error evidence")
        for key in ("first_observation", "last_observation"):
            o = w[key]
            child_observation(o, coop["mono_inner_deadline"], allowed)
            if o["observer"] != w["observer"] or o["pid"] != w["pid"] or o["role"] != w["role"] or o["phase"] != w["phase"] or \
                    o["error"] is not None or not w["mono_start"] <= o["mono_start"] <= o["observed_mono"] <= w["mono_end"]:
                raise Invalid("private identity polling actual observation role/observer/interval")
            observations.append(o)
        if (w["attempts"] == 1 and not same(w["first_observation"], w["last_observation"])) or \
                w["first_observation"]["observed_mono"] > w["last_observation"]["observed_mono"] or \
                w["last_observation"]["identity"] is None:
            raise Invalid("private identity polling first/last/matched evidence")
        target = w["last_observation"]["identity"]
        if w["pid"] != container.get("grandchild") or w["observer"] != container.get("intermediate") or \
                target["ppid"] != w["observer"] or not any(same(o, w["last_observation"]) for o in container["descendants"]):
            raise Invalid("private polling target/parent/retained actual matched observation")
        if w["role"] == "zombie":
            joins = [j for j in container["joins"] if j["role"] == "zombie"]
            if target["status"] != 5 or len(joins) != 1 or not same(joins[0]["intended_identity"], target) or \
                    w["mono_end"] > joins[0]["mono_start"]:
                raise Invalid("zombie join is not bound to actual final matched held-zombie incarnation")
        elif target["comm"] != "sleep" or target["status"] == 5:
            raise Invalid("exec polling matched flag contradicts actual post-exec native metadata")
    if any(not entry <= o["mono_start"] <= o["observed_mono"] <= report_mono for o in observations):
        raise Invalid("native observation outside its original containing lifetime/report")
    return observations


def child_envelope(report, name, main, receipt, cfg, has_output, late_output):
    """Validate original private evidence and report every acquired incarnation for the separate parent endedness audit."""
    base = {"child", "scenario", "pid", "pgid", "ppid", "negative_control", "mono_module_entry", "epoch_module_entry",
        "mono_life_deadline", "stdin_protocol", "main_identity", "main_identity_observed_mono", "main_identity_observation",
        "cooperative", "descendants", "joins", "identity_waits", "ownership_edges", "transports", "evidence_failures", "mono_output"}
    extra = {"main_identity_at_output"} if has_output else set()
    if name in ("mutate_pin", "mutate_evidence"):
        extra |= {"creation", "target_inode", "size_before"}
    elif name == "rss":
        extra |= {"rss_pid", "allocated", "touched_bytes", "touch_stride", "touch_writes", "touch_write_bytes", "page_size",
            "rss_before_bytes", "rss_after_bytes", "rss_delta_bytes", "rss_before", "rss_after",
            "mono_before_allocation", "mono_after_touch", "term_masked_for_evidence"}
    elif name == "busy2":
        extra |= {"grandchild", "busy_pids"} if has_output else {"busy_pids", "mono_before_work", "mono_work_end", "busy_gate"}
    elif name in ("ownership_group", "ownership_slow", "ownership_fast"):
        extra |= {"grandchild", "ownership_hold", "required_ownership_class"}
    elif name in ("ownership_double", "zombie_hold"):
        extra |= {"intermediate", "grandchild", "intermediate_status", "intermediate_merge", "required_ownership_class"}
        if name == "zombie_hold":
            extra.add("zombie_hold")
    elif name in ("deadline", "ignore", "identity"):
        extra.add("term_arrivals")
    if not isinstance(report, dict) or set(report) != base | extra or report.get("child") != "guard_qual_child_v12" or \
            report.get("scenario") != name or not integer(report.get("pid"), 1) or report["pid"] != main["pid"] or \
            not integer(report.get("pgid"), 1) or report["pgid"] != main["pgid"] or not integer(report.get("ppid"), 1) or \
            report.get("negative_control") is not (name not in ("ok", "rc_nonzero")) or report.get("evidence_failures") != []:
        raise Invalid("child exact report schema/identity/negative declaration/failure evidence")
    entry, life, output = report["mono_module_entry"], report["mono_life_deadline"], report["mono_output"]
    if not all(finite(report.get(k)) for k in ("mono_module_entry", "epoch_module_entry", "mono_life_deadline", "mono_output")) or \
            abs(life - entry - SC[name][0]) > 1e-6 or not receipt["mono_spawn"] <= entry <= output < life:
        raise Invalid("shared original module-entry child life not proved")
    coop, reserve = report["cooperative"], min(0.25, SC[name][0] / 8.0)
    expected_coop = {"mono_life_deadline": life, "mono_work_end": life - 2 * reserve,
        "mono_join_deadline": life - reserve, "mono_inner_deadline": life - 3 * reserve,
        "poll_interval_s": 0.01, "deadline_extended": False}
    if not same(coop, expected_coop) or any(not isinstance(report[k], list) for k in
            ("descendants", "joins", "identity_waits", "ownership_edges")) or not isinstance(report["transports"], dict):
        raise Invalid("cooperative bounds/full included child evidence lists missing")
    line = b""
    if name in ("mutate_pin", "mutate_evidence"):
        line = (json.dumps(receipt.get("go_creation_manifest"), sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
        if len(line) > 4096 or hashlib.sha256(line).hexdigest() != receipt.get("go_creation_manifest_sha256"):
            raise Invalid("actual bounded creation line digest missing")
    proto = report["stdin_protocol"]
    private_transport(proto, coop, "mono_join_deadline", entry, output, b"GO\n" + line,
                      {"creation_line_bytes", "creation_manifest_sha256"}, 4099, kind="read")
    if proto["mono_eof"] < receipt["go_written_mono"] or \
            not same(proto["creation_line_bytes"], len(line) if line else None) or \
            not same(proto["creation_manifest_sha256"], hashlib.sha256(line).hexdigest() if line else None):
        raise Invalid("exact token/declared creation line/actual EOF after actual GO write")
    allowed = {main["pid"]}
    allowed.update(x["pid"] for x in report["descendants"] if isinstance(x, dict) and integer(x.get("pid"), 1))
    allowed.update(x for x in (report.get("intermediate"), report.get("grandchild")) if integer(x, 1))
    main_o = report["main_identity_observation"]
    p = child_observation(main_o, life, allowed)
    if p is None or identity(p) != identity(main) or not same(p, report["main_identity"]) or \
            main_o["role"] != "main" or main_o["phase"] != "post_go" or main_o["observer"] != main["pid"] or \
            not same(report["main_identity_observed_mono"], main_o["observed_mono"]) or \
            not proto["mono_end"] <= main_o["mono_start"] <= main_o["observed_mono"] <= output:
        raise Invalid("original full main incarnation/actual GO/report chronology mismatch")
    source_observations = [main_o] + report["descendants"]
    observations = [main_o] + private_members(report, source_observations, coop, entry, output, allowed)
    edges = report["ownership_edges"]
    required_edges = {"ownership_group": ["post_setup", "hold_end"], "ownership_slow": ["post_setup", "hold_end"],
                      "ownership_fast": ["post_setup"], "ownership_double": ["pre_exec", "post_exec_current_parent"]}
    if [e["phase"] for e in edges] != required_edges.get(name, []) or \
            (name == "ownership_group" and any(e["same_group_verified"] is not True for e in edges)) or \
            (name in ("ownership_slow", "ownership_fast") and edges[0]["child"]["identity"]["pgid"] != report["grandchild"]):
        raise Invalid("scenario-required private ownership edges missing, extra or not proved")
    if has_output:
        o = report["main_identity_at_output"]
        p = child_observation(o, life, allowed)
        if p is None or o["observer"] != main["pid"] or o["pid"] != main["pid"] or \
                o["role"] != "main" or o["phase"] != "output" or o["observed_mono"] > output:
            raise Invalid("main output incarnation not acquired before containing report")
        # The output acquisition is the SAME launched incarnation. Only a verified late report may observe the
        # launchd reparent after the supervisor ended; every other safety field stays invariant.
        if identity(p) != identity(main) and not (late_output and p["ppid"] == 1 and
                identity(dict(p, ppid=main["ppid"])) == identity(main)):
            raise Invalid("main output observation is not the launched main incarnation")
        observations.append(o)
    transports = report["transports"]
    if name in ("ownership_group", "ownership_slow", "ownership_fast"):
        if set(transports) != {"descendant_ready"}:
            raise Invalid("ownership readiness transport exact set")
        private_transport(transports["descendant_ready"], coop, "mono_join_deadline", entry, output, b"R", cap=1, kind="read")
        starts = [o["mono_start"] for o in report["descendants"] if o["phase"] == "post_setup"]
        if len(starts) != 1 or transports["descendant_ready"]["mono_end"] > starts[0]:
            raise Invalid("readiness completed after its intended setup acquisition")
    elif name == "busy2" and has_output:
        if set(transports) != {"busy_start_gate"}:
            raise Invalid("busy actual start transport exact set")
        private_transport(transports["busy_start_gate"], coop, "mono_join_deadline", entry, output, b"S", cap=1, kind="write")
    elif name in ("ownership_double", "zombie_hold"):
        if set(transports) != {"intermediate_report", "intermediate_internal"}:
            raise Invalid("original intermediate transports exact set")
        raw = private_transport(transports["intermediate_report"], coop, "mono_join_deadline", entry, output, cap=32768, kind="read")
        if not raw.endswith(b"\n") or raw.count(b"\n") != 1:
            raise Invalid("original intermediate report incomplete/non-single-line")
        original = decode(raw)
        canonical = (json.dumps(original, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()
        fields = {"kind", "scenario", "intermediate", "mono_module_entry", "mono_life_deadline", "cooperative", "grandchild",
            "descendants", "joins", "identity_waits", "ownership_edges", "transports", "evidence_failures", "error", "mono_output"}
        if name == "zombie_hold":
            fields.add("zombie_hold")
        if raw != canonical or not isinstance(original, dict) or set(original) != fields or \
                original["kind"] != "qualification-intermediate-report-v2" or original["scenario"] != name or \
                not integer(original["intermediate"], 1) or original["intermediate"] != report["intermediate"] or \
                not integer(original["grandchild"], 1) or original["grandchild"] != report["grandchild"] or \
                not same(original["mono_module_entry"], entry) or not same(original["mono_life_deadline"], life) or \
                not same(original["cooperative"], coop) or original["evidence_failures"] != [] or original["error"] is not None or \
                not finite(original["mono_output"]) or \
                not entry <= original["mono_output"] <= transports["intermediate_report"]["mono_eof"] <= output:
            raise Invalid("retained original intermediate bytes identity/life/report/schema")
        lists = ("descendants", "joins", "identity_waits", "ownership_edges", "evidence_failures")
        merge = report["intermediate_merge"]
        if not isinstance(merge, dict) or set(merge) != set(lists):
            raise Invalid("original intermediate list merge schema")
        for key in lists:
            if not isinstance(original[key], list) or not same(merge[key], [0, len(original[key])]) or \
                    not same(report[key][:len(original[key])], original[key]):
                raise Invalid("original intermediate observations/joins/failures changed during merge")
        if not same(transports["intermediate_internal"], original["transports"]):
            raise Invalid("original intermediate transport object changed during merge")
        observations += private_members(original, source_observations, coop, entry, original["mono_output"], allowed)
        main_joins = [j for j in report["joins"] if j["role"] == "intermediate"]
        if len(main_joins) != 1 or main_joins[0]["observer"] != main["pid"] or \
                main_joins[0]["pid"] != report["intermediate"] or not integer(report["intermediate_status"], 0) or \
                report["intermediate_status"] != main_joins[0]["wait_status"] or \
                transports["intermediate_report"]["mono_end"] > main_joins[0]["mono_start"]:
            raise Invalid("original intermediate actual parent join/status/read-before-join")
        internal = original["transports"]
        if name == "ownership_double":
            if set(internal) != {"exec_start_gate", "exec_status"}:
                raise Invalid("double-fork original internal exec transports exact set")
            private_transport(internal["exec_start_gate"], coop, "mono_inner_deadline", entry, original["mono_output"], b"S", cap=1, kind="write")
            private_transport(internal["exec_status"], coop, "mono_inner_deadline", entry, original["mono_output"], b"", cap=2048, kind="read")
            post = [w for w in original["identity_waits"] if w["phase"] == "post_exec_pre_reparent"]
            if len(post) != 1 or internal["exec_start_gate"]["mono_end"] > internal["exec_status"]["mono_start"] or \
                    internal["exec_status"]["mono_end"] > post[0]["mono_start"]:
                raise Invalid("double-fork actual close-on-exec EOF before native post-exec identity")
            matched = post[0]["last_observation"]["identity"]
            indexes = [i for i, o in enumerate(report["descendants"]) if o["role"] == "exec_descendant" and
                       o["phase"] == "post_exec_post_reparent"]
            moved = report["descendants"][indexes[0]] if len(indexes) == 1 else None
            if moved is None or indexes[0] < len(original["descendants"]) or moved["observer"] != main["pid"] or \
                    moved["pid"] != report["grandchild"] or moved["identity"] is None or \
                    any(not same(moved["identity"][k], matched[k]) for k in
                        ("pid", "uniqueid", "idversion", "euid", "ruid", "pgid", "traced")) or \
                    moved["identity"]["comm"] != "sleep" or moved["identity"]["status"] == 5 or \
                    moved["identity"]["ppid"] == report["intermediate"] or moved["mono_start"] < main_joins[0]["mono_end"]:
                raise Invalid("double-fork post-reparent record is not the matched post-exec incarnation observed by main after the intermediate join")
        else:
            hold = original["zombie_hold"]
            waited = [w for w in original["identity_waits"] if w["role"] == "zombie"]
            ends = [o for o in original["descendants"] if o["role"] == "zombie" and o["phase"] == "zombie_hold_end"]
            joins = [j for j in original["joins"] if j["role"] == "zombie"]
            if internal or not same(report["zombie_hold"], hold) or not isinstance(hold, dict) or \
                    set(hold) != {"mono_start", "mono_hold_until", "mono_end"} or \
                    not all(finite(v) for v in hold.values()) or len(waited) != 1 or len(ends) != 1 or len(joins) != 1:
                raise Invalid("zombie original internal transports/hold/wait/end/join schema")
            start, end = waited[0]["last_observation"], ends[0]
            if start["identity"]["status"] != 5 or end["identity"] is None or end["identity"]["status"] != 5 or \
                    identity(start["identity"]) != identity(end["identity"]) or \
                    hold["mono_hold_until"] != min(hold["mono_start"] + 3.0, coop["mono_inner_deadline"] - reserve) or \
                    not waited[0]["mono_end"] <= hold["mono_start"] <= hold["mono_hold_until"] <= \
                        end["mono_start"] <= end["observed_mono"] <= hold["mono_end"] <= joins[0]["mono_start"]:
                raise Invalid("actual held-zombie full fingerprint and measured original hold window")
    elif transports:
        raise Invalid("undeclared private transport evidence")
    unique = {}
    for o in observations:
        if o.get("identity") is not None:
            unique[identity(o["identity"])] = o["identity"]
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
    observations, reported = child_envelope(report, name, main, receipt, cfg, childout is not None, "child-out.json" in late)
    imap = {e["first_identity"]["uniqueid"]: e for e in receipt["identity_history"]}
    registry = {e["identity"]["uniqueid"]: e for e in receipt["owned_identities"]}
    roots = {h["identity"]["uniqueid"] for h in receipt["helpers"]} | {main["uniqueid"]}
    extra = {uid: e for uid, e in registry.items() if uid not in roots}
    acquired = {}
    for row in receipt["identity_events"]:
        p = imap[row[0]]["variants"][row[1]]
        acquired.setdefault(identity(p), []).append((row[3], row[4]))
    def compatible(actual, reported, interval):
        if identity(actual) == identity(reported):
            return True
        if identity(actual)[:5] != identity(reported)[:5] or actual["traced"] is not reported["traced"] or interval is None:
            return False
        originals = [o for o in observations if o.get("identity") is not None and identity(o["identity"]) == identity(reported)]
        # Only these source-declared setsid transitions change a known incarnation's original group.
        session = (report["intermediate"], "intermediate", "self_post_setup") if name == "ownership_double" else \
            (report["grandchild"], "descendant", "post_setup") if name in ("ownership_slow", "ownership_fast") else None
        if session is not None and actual["pid"] == session[0] and actual["ppid"] == reported["ppid"] == main["pid"] and \
                actual["pgid"] == main["pgid"] and reported["pgid"] == actual["pid"]:
            return any(o["role"] == session[1] and o["phase"] == session[2] and
                       interval[1] <= o["mono_start"] for o in originals)
        # Single descendants are reported BEFORE their main parent exits. Reparenting is the only omitted
        # private observation, not permission to ignore group/trace/UID/version or an unknown live parent.
        if name not in ("ownership_group", "ownership_slow", "ownership_fast") or \
                actual["pid"] != report["grandchild"] or actual["pgid"] != reported["pgid"] or \
                reported["ppid"] != main["pid"] or actual["ppid"] == main["pid"] or \
                receipt["child_returncode"] != 0 or not finite(receipt.get("child_exit_mono")):
            return False
        exit_mono = receipt["child_exit_mono"]
        return exit_mono <= interval[0] and any(o["observed_mono"] <= exit_mono for o in originals)
    def reported_match(p, interval):
        return any(compatible(p, q, interval) for q in reported)
    for entry in extra.values():
        event = receipt["identity_events"][entry["identity_event_ref"] - 1]
        if not reported_match(entry["identity"], (event[3], event[4])):
            raise Invalid("owned registry incarnation lacks reported full fingerprint or its exact declared transition")
    for p in receipt["contract_violations"]:
        entry = registry.get(p["uniqueid"])
        event = receipt["identity_events"][entry["identity_event_ref"] - 1] if entry is not None else None
        if event is None or not reported_match(p, (event[3], event[4])):
            raise Invalid("unreported full contract-violating incarnation")
    def in_ledger(p, full=False):
        e = imap.get(p["uniqueid"])
        return e is not None and any(identity(v) == identity(p) or (not full and any(
            compatible(v, p, interval) for interval in acquired.get(identity(v), []))) for v in e["variants"])
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
        if len(blockers) != 1 or not compatible(blockers[0], target, (final["mono_begin"], final["mono_end"])) or \
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
        pair = {identity(main), identity(kid)}
        witnessed = False
        for c in receipt["census_observations"]:
            busy = [m for m in c["measurements"] if m["busy"]]
            if {identity(m["identity"]) for m in busy} == pair and len(busy) == 2 and \
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
            if not isinstance(r, dict) or set(r) != {"pid", "identity_before", "identity_after", "rss_bytes", "mono_start", "mono_end", "error"} or \
                    not integer(r.get("pid"), 1) or r["pid"] != main["pid"] or r["error"] is not None or \
                    not integer(r["rss_bytes"], 0) or not finite(r["mono_start"]) or not finite(r["mono_end"]):
                raise Invalid("PID-specific child RSS bracket missing")
            before, after = r["identity_before"], r["identity_after"]
            a = child_observation(before, report["mono_life_deadline"], {main["pid"]})
            b = child_observation(after, report["mono_life_deadline"], {main["pid"]})
            if a is None or b is None or identity(a) != identity(b) or identity(a) != identity(main) or \
                    before["observer"] != main["pid"] or after["observer"] != main["pid"] or \
                    before["role"] != "main" or after["role"] != "main" or \
                    before["phase"] != "rss_measurement_before" or after["phase"] != "rss_measurement_after" or \
                    not before["observed_mono"] <= r["mono_start"] <= after["mono_start"] <= \
                        after["observed_mono"] <= r["mono_end"] <= report["mono_output"]:
                raise Invalid("RSS task read lacks intended full fingerprint/native bracket/report chronology")
        if not report["main_identity_observation"]["observed_mono"] <= report["rss_before"]["identity_before"]["mono_start"]:
            raise Invalid("RSS stimulus/task evidence precedes the post-GO main observation")
        if not all(integer(report.get(k), 0) for k in ("rss_before_bytes", "rss_after_bytes", "rss_delta_bytes")) or \
                report["rss_before_bytes"] != report["rss_before"]["rss_bytes"] or \
                report["rss_after_bytes"] != report["rss_after"]["rss_bytes"] or \
                report["rss_delta_bytes"] != report["rss_after_bytes"] - report["rss_before_bytes"] or \
                not all(finite(report.get(k)) for k in ("mono_before_allocation", "mono_after_touch")) or \
                not report["rss_before"]["mono_end"] <= report["mono_before_allocation"] <= \
                    report["rss_after"]["identity_before"]["mono_start"] <= report["rss_after"]["mono_end"] <= \
                    report["mono_after_touch"] <= report["mono_output"] or report["rss_after_bytes"] <= cfg["rss_trip_bytes"]:
            raise Invalid("RSS reported counters contradict actual bracketed task records")
        trip, witnessed = receipt["trips"][0], False
        for c in receipt["census_observations"]:
            partial = 0
            for index, m in enumerate(c["measurements"]):
                partial += m["rss"]
                following = c["measurements"][index + 1]["mono_observed"] if index + 1 < len(c["measurements"]) else c["mono_end"]
                if identity(m["identity"]) == identity(main) and m["rss"] > cfg["rss_trip_bytes"] and \
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
                not same(creation.get("manifest_line_bytes"), len(manifest_line)) or \
                creation.get("preparation_sha256") != preparation["sha256"] or \
                not same(creation.get("run"), prep["run"]) or not same(creation.get("output_root"), prep["output_root"]) or \
                not same(creation.get("original"), original) or not same(creation.get("after"), after) or \
                not same(manifest.get("target"), original) or not same(manifest.get("run"), prep["run"]) or \
                not same(manifest.get("output_root"), prep["output_root"]) or \
                manifest.get("preparation_sha256") != preparation["sha256"] or \
                not same(creation.get("preparation_facts"), {"path": QROOT + "/" + name + "/preparation.json", **hash_entry(preparation)}) or \
                not same(creation.get("name_inode_before"), original["inode"]) or not same(creation.get("name_inode_after"), original["inode"]) or \
                not same(creation.get("append_bytes"), 1) or actual["raw"] != raw_original + b"x" or \
                not all(finite(creation.get(k)) for k in ("mono_verified", "mono_append", "mono_fsync_completed", "mono_after_verified")) or \
                not creation["mono_verified"] <= creation["mono_append"] <= creation["mono_fsync_completed"] <= creation["mono_after_verified"] < report["mono_life_deadline"] or \
                not report["main_identity_observation"]["observed_mono"] <= creation["mono_verified"] or \
                not creation["mono_after_verified"] <= report["main_identity_at_output"]["mono_start"]:
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
    if not isinstance(approval, dict) or approval.get("kind") != "v19-qualification-invocation-v1" or approval.get("scenario") != name:
        raise Invalid("approval kind/scenario")
    cp, gp, sp, pp = (snapshot(runfd, f, 1 << 20) for f in ("config.json", "go.json", "stability.json", "preparation.json"))
    require("approval_artifact_bindings", all(approval.get(k) == v["sha256"] for k, v in (
        ("config_sha256", cp), ("go_sha256", gp), ("stability_receipt_sha256", sp), ("preparation_sha256", pp))))
    verifier = absolute_snapshot(VERIFIER, 1 << 20)
    verifier_pin = approval.get("verifier")
    if not isinstance(verifier_pin, dict) or set(verifier_pin) != {"path", "sha256"} or \
            verifier_pin["path"] != VERIFIER or verifier_pin["sha256"] != verifier["sha256"]:
        raise Invalid("approval must independently pin this postchecker source")
    require("independent_postchecker_source_matches_actual_bytes", True)
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
            same(go["configs"], {} if name == "go_unlisted" else {cp["sha256"]: expected_entry}))
    expected_root = {"kind": "v19-qualification-root", "package": "v9", "qroot": QROOT, "source_pins": package}
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
            summary.get("supervisor") == "owned_supervisor_v19")
    rsha, ssha = files["supervisor-receipt.json"]["sha256"], files["settlement.json"]["sha256"]
    require("receipt_source_config_binding", receipt.get("supervisor") == "owned_supervisor_v19" and
            receipt.get("supervisor_sha256") == SUPERVISOR_SHA and receipt.get("config_sha256") == cp["sha256"])
    require("settlement_receipt_binding", settlement.get("receipt_sha256") == rsha and settlement.get("receipt") == cfg["receipt"] and
            settlement.get("config_sha256") == cp["sha256"] and settlement.get("supervisor") == "owned_supervisor_v19")
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
    authorization_fit_evidence(receipt, summary, cfg, go, stability, name, gp["sha256"], sp["sha256"])
    C.update(integrated_v19_evidence(receipt, summary, stability, cfg, go, name, samples))
    common_final_evidence(receipt, summary, cfg, files, late, runfd, require, samples)
    main_stream_evidence(receipt, summary, cfg, files, samples)
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
    identity(ident)
    require("full_child_identity", same(ident, receipt.get("child_identity")) and
            ident["pid"] == ident["pgid"] == receipt.get("child_pid"))
    owned = receipt.get("owned_identities")
    helper_ids = {h["identity"]["uniqueid"] for h in receipt.get("helpers", []) if isinstance(h.get("identity"), dict)}
    known_uids = helper_ids | {ident["uniqueid"]}
    known_extra = [o for o in owned if o.get("identity", {}).get("uniqueid") not in known_uids] if isinstance(owned, list) else []
    require("known_owned_registry_retained", isinstance(owned, list) and all(
        any(o.get("identity", {}).get("uniqueid") == u for o in owned) for u in known_uids) and
        (name in NEGATIVE_PROCESS or (not known_extra and receipt.get("contract_violations") == [])))
    expected_launch = {"supervisor": SUPERVISOR.rsplit("/", 1)[1][:-3], "supervisor_sha256": SUPERVISOR_SHA,
        "config_sha256": cp["sha256"], "supervisor_pid": receipt["supervisor_pid"],
        "identity": receipt["child_identity"], "argv": cfg["argv"], "cwd": cfg["lane"], "env": cfg["env"],
        "mono_spawn": receipt["mono_spawn"], "epoch_spawn": receipt["epoch_spawn"],
        "start_date": receipt["start_date"], "baseline_count": len(receipt["baseline"]["identities"]),
        "authorization": receipt["authorization"], "launch_commit": receipt["launch_commit"],
        "cpu_slots": cfg["cpu_slots"], "reservation_bytes": cfg["admission"]["reservation_bytes"]}
    require("exact_launch_clock_authority_and_config_binding", same(launch, expected_launch))
    require("authorization_cross_binding", same(launch["authorization"], receipt["admission"]["authorization"]))
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
                same(childout.get("target_inode"), fixture["inode"]) and same(childout.get("size_before"), len(FIXTURE)))
    if name == "mutate_evidence":
        require("launch_mutation_same_inode", same(childout.get("target_inode"), files["launch.json"]["inode"]) and
                integer(childout.get("size_before"), 0) and childout["size_before"] + 1 == files["launch.json"]["bytes"])
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
    if os.path.abspath(__file__) != VERIFIER or os.path.realpath(__file__) != VERIFIER:
        raise Invalid("postchecker must execute at the exact approved fixed source path")
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
