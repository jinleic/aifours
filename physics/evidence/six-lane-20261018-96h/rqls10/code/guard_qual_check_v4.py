#!/usr/bin/env python3
"""guard_qual_check_v4: check one guard-qualification scenario of code/owned_supervisor_v7.py against its preregistered
expectation (plan evidence/owned_supervisor_v7-guard-qualification-plan-v4.md). Supersedes guard_qual_check_v3.py (never
run) after the parent's pre-review: the busy scenario uses busy2 with busy_limit 1, and EVERY scenario must show that the
lane never exceeded 2 busy processes (every sample's census lane_busy <= 2 and the receipt's max lane_busy <= 2).
v7 receipt fields (failure latch, lineage census, deadline timeliness, staged settlement link) and the scenarios
go_unlisted, stray_file, zombie_hold and double_fork_escape. Every trip name must belong to the scenario's allowed set;
SETTLED scenarios also need an empty failure latch, a clear final census, GO delivered and four matching evidence
digests. Reads only RUN/out (settlement.json, settlement.json.staged, supervisor-receipt.json, samples.jsonl,
stdout.txt) with bounded regular-file reads; exclusive output. Exit 0 only for verdict PASS, 1 for FAIL.
Usage: guard_qual_check_v4.py SCENARIO RUN_DIR OUT.json
"""
import hashlib, json, os, stat, sys

LAUNCHED_UNSETTLED_ESCAPE = {"settlement": "UNSETTLED", "rc": 0, "allowed": [], "signal_sent": False,
                             "failures_all": ["GRACE_EXPIRED_AFTER_CHILD_EXIT", "BLOCKING_LIVE"],
                             "loop_status": "GRACE_EXPIRED_AFTER_CHILD_EXIT"}
EXPECT = {
    "date_fault": {"settlement": "NOT_LAUNCHED", "rc": None, "allowed": [], "admission_reasons_any": ["DATE_HELPER_UNAVAILABLE"]},
    "go_unlisted": {"settlement": "NOT_LAUNCHED", "rc": None, "allowed": [],
                    "admission_reasons_any": ["GO_DOES_NOT_NAME_THIS_CONFIG"], "failures_n": 0},
    "ok": {"settlement": "SETTLED", "rc": 0, "allowed": [], "signal_sent": False},
    "rc_nonzero": {"settlement": "SETTLED", "rc": 3, "allowed": [], "signal_sent": False},
    "missing_output": {"settlement": "UNSETTLED", "rc": 0, "allowed": [], "signal_sent": False,
                       "failures_all": ["REQUIRED_OUTPUT_MISSING"]},
    "mutate_pin": {"settlement": "UNSETTLED", "rc": 0, "allowed": [], "signal_sent": False,
                   "failures_all": ["PIN_CHANGED_OR_UNREADABLE"]},
    "mutate_evidence": {"settlement": "UNSETTLED", "rc": 0, "allowed": [], "signal_sent": False,
                        "failures_all": ["EVIDENCE_MUTATED"]},
    "stray_file": {"settlement": "UNSETTLED", "rc": 0, "allowed": [], "signal_sent": False,
                   "failures_all": ["UNDECLARED_ENTRIES"]},
    "deadline": {"settlement": "SETTLED", "rc": -15, "allowed": ["DEADLINE"], "first_trip": "DEADLINE", "signal_sent": True},
    "flood": {"settlement": "SETTLED", "rc": -15, "allowed": ["STREAM_CAP"], "first_trip": "STREAM_CAP", "signal_sent": True,
              "stdout_bytes": 1048576},
    "busy": {"settlement": "SETTLED", "rc": -15, "allowed": ["BUSY"], "first_trip": "BUSY", "signal_sent": True},
    "rss": {"settlement": "SETTLED", "rc": -15, "allowed": ["RSS"], "first_trip": "RSS", "signal_sent": True},
    "zombie_hold": {"settlement": "SETTLED", "rc": 0, "allowed": [], "signal_sent": False, "zombie_seen": True},
    "escape_slow": dict(LAUNCHED_UNSETTLED_ESCAPE),
    "escape_fast": dict(LAUNCHED_UNSETTLED_ESCAPE),
    "double_fork_escape": dict(LAUNCHED_UNSETTLED_ESCAPE, final_blocking_nonempty=True),
    "ignore": {"settlement": "UNSETTLED", "rc": None, "allowed": ["DEADLINE"], "first_trip": "DEADLINE", "signal_sent": True,
               "failures_all": ["GRACE_EXPIRED_AFTER_STOP_REQUEST", "CHILD_NOT_REAPED"],
               "loop_status": "GRACE_EXPIRED_AFTER_STOP_REQUEST"},
    "identity": {"settlement": "UNSETTLED", "rc": None, "allowed": ["DEADLINE"], "first_trip": "DEADLINE",
                 "signal_sent": False,
                 "failures_all": ["IDENTITY_UNVERIFIED", "GRACE_EXPIRED_AFTER_STOP_REQUEST", "CHILD_NOT_REAPED"],
                 "loop_status": "GRACE_EXPIRED_AFTER_STOP_REQUEST"},
}
MAX_BYTES = 8 << 20


def read_regular(p, max_bytes=MAX_BYTES):
    st = os.lstat(p)
    if not stat.S_ISREG(st.st_mode) or st.st_size > max_bytes:
        raise OSError("not a bounded regular file: %s" % p)
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        st2 = os.fstat(fd)
        if (st2.st_dev, st2.st_ino, st2.st_size) != (st.st_dev, st.st_ino, st.st_size):
            raise OSError("changed while opening: %s" % p)
        parts, got = [], 0
        while got < st.st_size:
            chunk = os.read(fd, st.st_size - got)
            if not chunk:
                raise OSError("short read: %s" % p)
            parts.append(chunk)
            got += len(chunk)
        if os.read(fd, 1):
            raise OSError("grew while read: %s" % p)
    finally:
        os.close(fd)
    return b"".join(parts)


def _no_dup(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError("duplicate key %r" % k)
        out[k] = v
    return out


def _no_const(name):
    raise ValueError("non-finite constant %s" % name)


def load(p):
    raw = read_regular(p)
    return json.loads(raw.decode("utf-8"), object_pairs_hook=_no_dup, parse_constant=_no_const), \
        hashlib.sha256(raw).hexdigest()


def main():
    name, run, out = sys.argv[1], sys.argv[2], sys.argv[3]
    exp = EXPECT[name]
    od = os.path.join(run, "out")
    res = {"checker": "guard_qual_check_v3", "scenario": name, "run_dir": run, "expected": exp, "failed": []}
    F = res["failed"]
    try:
        st, st_sha = load(os.path.join(od, "settlement.json"))
        _, staged_sha = load(os.path.join(od, "settlement.json.staged"))
        rc_, rc_sha = load(os.path.join(od, "supervisor-receipt.json"))
    except (OSError, ValueError) as ex:
        F.append("UNREADABLE %r" % ex)
        st, rc_, st_sha, staged_sha, rc_sha = {}, {}, None, None, None
    res["settlement_sha256"], res["receipt_sha256"] = st_sha, rc_sha
    if not isinstance(st, dict) or not isinstance(rc_, dict):
        F.append("NOT_OBJECTS")
        st, rc_ = {}, {}
    if st_sha is not None and staged_sha != st_sha:
        F.append("STAGED_SETTLEMENT_DIFFERS")
    if st and st.get("receipt_sha256") != rc_sha:
        F.append("SETTLEMENT_RECEIPT_SHA_MISMATCH")
    if st.get("settlement") != exp["settlement"] or rc_.get("settlement") != exp["settlement"]:
        F.append("SETTLEMENT %r/%r != %r" % (st.get("settlement"), rc_.get("settlement"), exp["settlement"]))
    if rc_.get("child_returncode") != exp["rc"] or st.get("child_returncode") != exp["rc"]:
        F.append("RC %r != %r" % (rc_.get("child_returncode"), exp["rc"]))
    trips = [t.get("trip") for t in rc_.get("trips") or [] if isinstance(t, dict)]
    res["trips"] = trips
    bad = sorted(set(trips) - set(exp["allowed"]))
    if bad:
        F.append("UNEXPECTED_TRIPS %r" % bad)
    if "first_trip" in exp and (not trips or trips[0] != exp["first_trip"]):
        F.append("FIRST_TRIP %r != %r" % (trips[:1], exp["first_trip"]))
    sig = rc_.get("signal") or {}
    res["signal"] = sig
    if "signal_sent" in exp and (sig.get("sent") is True) != exp["signal_sent"]:
        F.append("SIGNAL_SENT %r != %r" % (sig.get("sent"), exp["signal_sent"]))
    failures = [f.get("reason", "") for f in rc_.get("failures") or [] if isinstance(f, dict)]
    res["failures"] = failures
    if not isinstance(rc_.get("failures_n"), int) or rc_["failures_n"] < len(failures):
        F.append("FAILURES_N_INVALID")
    for r in exp.get("failures_all", []):
        if not any(x.startswith(r) for x in failures):
            F.append("MISSING_FAILURE %s" % r)
    if "failures_n" in exp and rc_.get("failures_n") != exp["failures_n"]:
        F.append("FAILURES_N %r != %r" % (rc_.get("failures_n"), exp["failures_n"]))
    if "loop_status" in exp and rc_.get("loop_status") != exp["loop_status"]:
        F.append("LOOP_STATUS %r != %r" % (rc_.get("loop_status"), exp["loop_status"]))
    if "admission_reasons_any" in exp:
        ar = (rc_.get("admission") or {}).get("reasons") or []
        if not any(any(str(x).startswith(r) for x in ar) for r in exp["admission_reasons_any"]):
            F.append("ADMISSION_REASON_MISSING %r" % exp["admission_reasons_any"])
    if "stdout_bytes" in exp:
        try:
            n = os.lstat(os.path.join(od, "stdout.txt")).st_size
        except OSError:
            n = None
        if n != exp["stdout_bytes"]:
            F.append("STDOUT_BYTES %r != %r" % (n, exp["stdout_bytes"]))
    fc = rc_.get("final_census") or {}
    if exp.get("final_blocking_nonempty") and not (fc.get("owned_live") or fc.get("unresolved_live")):
        F.append("FINAL_BLOCKING_EMPTY")
    if exp["settlement"] == "SETTLED":
        if fc.get("blocking_live") != [] or rc_.get("go_delivered") is not True or rc_.get("failures_n") != 0:
            F.append("SETTLED_PRECONDITIONS")
        ev = rc_.get("evidence_expected_sha256") or {}
        arts = rc_.get("artifacts") or {}
        if len(ev) != 4 or any((arts.get(p) or {}).get("sha256") != h for p, h in ev.items()):
            F.append("EVIDENCE_DIGESTS")
        dt = rc_.get("deadline_timeliness")
        if not isinstance(dt, dict):
            F.append("DEADLINE_TIMELINESS_MISSING")
    zombie_seen, busy_max = False, 0
    if exp["settlement"] != "NOT_LAUNCHED":
        try:
            n_s = 0
            for line in read_regular(os.path.join(od, "samples.jsonl")).decode("utf-8").splitlines():
                if line.strip():
                    s = json.loads(line, object_pairs_hook=_no_dup, parse_constant=_no_const)
                    n_s += 1
                    c = s.get("census") or {}
                    if c.get("blocking_zombies"):
                        zombie_seen = True
                    if isinstance(c.get("lane_busy"), int):
                        busy_max = max(busy_max, c["lane_busy"])
            res["samples"] = n_s
        except (OSError, ValueError) as ex:
            F.append("SAMPLES_UNREADABLE %r" % ex)
        rmax = (rc_.get("max") or {}).get("lane_busy")
        res["lane_busy_max"] = [busy_max, rmax]
        if busy_max > 2 or not isinstance(rmax, int) or rmax > 2:
            F.append("LANE_BUSY_ABOVE_2 %r" % res["lane_busy_max"])
    res["zombie_seen"] = zombie_seen
    if exp.get("zombie_seen") and not zombie_seen:
        F.append("ZOMBIE_NOT_SEEN")
    if sig.get("sent") and isinstance(sig.get("mono_sent"), (int, float)) and isinstance(rc_.get("mono_end"), (int, float)):
        res["signal_to_receipt_s"] = rc_["mono_end"] - sig["mono_sent"]
    res["verdict"] = "PASS" if not F else "FAIL"
    data = (json.dumps(res, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(out, "xb") as fh:
        fh.write(data)
    print(json.dumps({"scenario": name, "verdict": res["verdict"], "failed": F}))
    return 0 if res["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
