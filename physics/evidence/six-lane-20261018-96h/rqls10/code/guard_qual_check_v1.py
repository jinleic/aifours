#!/usr/bin/env python3
"""guard_qual_check_v1: check one guard-qualification scenario of code/owned_supervisor_v5.py against its preregistered
expectation (plan evidence/owned_supervisor_v5-guard-qualification-plan-v1.md). Reads only the scenario directory
(settlement.json, supervisor-receipt.json, launch.json, samples.jsonl, stdout.txt, config.json); computes nothing else.
Usage: guard_qual_check_v1.py SCENARIO RUN_DIR OUT.json   (OUT exclusive create)
Verdict PASS only if every expectation holds; otherwise FAIL with the failed items. Raw values are copied.
"""
import hashlib, json, os, sys

EXPECT = {
    "ok": {"settlement": "SETTLED", "rc": 0, "trips": [], "signal_sent": False},
    "flood": {"settlement": "SETTLED", "rc": -15, "first_trip": "STREAM_CAP", "signal_sent": True,
              "stdout_bytes": 1048576},
    "deadline": {"settlement": "SETTLED", "rc": -15, "first_trip": "DEADLINE", "signal_sent": True},
    "ignore": {"settlement": "UNSETTLED", "rc": None, "first_trip": "DEADLINE", "signal_sent": True,
               "reasons_any": ["CHILD_NOT_REAPED"], "loop_status": "GRACE_EXPIRED_AFTER_STOP_REQUEST"},
    "identity": {"settlement": "UNSETTLED", "rc": None, "first_trip": "DEADLINE", "signal_sent": False,
                 "reasons_all": ["CHILD_NOT_REAPED", "FLAG_IDENTITY_UNVERIFIED"],
                 "loop_status": "GRACE_EXPIRED_AFTER_STOP_REQUEST"},
    "escape_slow": {"settlement": "UNSETTLED", "rc": 0, "trips": [], "reasons_any": ["OWNED_LIVE"],
                    "loop_status": "GRACE_EXPIRED_AFTER_CHILD_EXIT"},
    "escape_fast": {"settlement": "UNSETTLED", "rc": 0, "trips": [],
                    "reasons_any": ["OWNED_LIVE", "UNATTRIBUTED_NEW_LANE_PROCESSES"],
                    "loop_status": "GRACE_EXPIRED_AFTER_CHILD_EXIT"},
    "busy": {"settlement": "SETTLED", "rc": -15, "first_trip": "BUSY", "signal_sent": True},
    "rss": {"settlement": "SETTLED", "rc": -15, "first_trip": "RSS", "signal_sent": True},
    "date_fault": {"settlement": "NOT_LAUNCHED", "rc": None, "admission_reasons_any": ["DATE_HELPER_UNAVAILABLE"]},
}


def load(p):
    with open(p, "rb") as fh:
        raw = fh.read()
    return json.loads(raw.decode("utf-8")), hashlib.sha256(raw).hexdigest()


def main():
    name, run, out = sys.argv[1], sys.argv[2], sys.argv[3]
    exp = EXPECT[name]
    res = {"checker": "guard_qual_check_v1", "scenario": name, "run_dir": run, "expected": exp, "failed": []}
    F = res["failed"]
    try:
        st, st_sha = load(os.path.join(run, "settlement.json"))
        rc_, rc_sha = load(os.path.join(run, "supervisor-receipt.json"))
    except (OSError, ValueError) as ex:
        res["failed"].append("UNREADABLE %r" % ex)
        st, rc_, st_sha, rc_sha = {}, {}, None, None
    res["settlement_sha256"], res["receipt_sha256"] = st_sha, rc_sha
    if st and st.get("receipt_sha256") != rc_sha:
        F.append("SETTLEMENT_RECEIPT_SHA_MISMATCH")
    if st.get("settlement") != exp["settlement"]:
        F.append("SETTLEMENT %r != %r" % (st.get("settlement"), exp["settlement"]))
    if rc_.get("child_returncode") != exp["rc"]:
        F.append("RC %r != %r" % (rc_.get("child_returncode"), exp["rc"]))
    trips = [t.get("trip") for t in rc_.get("trips") or []]
    res["trips"] = trips
    if "trips" in exp and trips != exp["trips"]:
        F.append("TRIPS %r != %r" % (trips, exp["trips"]))
    if "first_trip" in exp and (not trips or trips[0] != exp["first_trip"]):
        F.append("FIRST_TRIP %r != %r" % (trips[:1], exp["first_trip"]))
    sig = rc_.get("signal") or {}
    res["signal"] = sig
    if "signal_sent" in exp and bool(sig.get("sent")) != exp["signal_sent"]:
        F.append("SIGNAL_SENT %r != %r" % (sig.get("sent"), exp["signal_sent"]))
    reasons = rc_.get("settlement_reasons") or []
    res["reasons"] = reasons
    for r in exp.get("reasons_all", []):
        if not any(x.startswith(r) for x in reasons):
            F.append("MISSING_REASON %s" % r)
    if exp.get("reasons_any") and not any(any(x.startswith(r) for x in reasons) for r in exp["reasons_any"]):
        F.append("NONE_OF_REASONS %r" % exp["reasons_any"])
    if "loop_status" in exp and rc_.get("loop_status") != exp["loop_status"]:
        F.append("LOOP_STATUS %r != %r" % (rc_.get("loop_status"), exp["loop_status"]))
    if "admission_reasons_any" in exp:
        ar = (rc_.get("admission") or {}).get("reasons") or []
        if not any(any(x.startswith(r) for x in ar) for r in exp["admission_reasons_any"]):
            F.append("ADMISSION_REASON_MISSING %r" % exp["admission_reasons_any"])
    if "stdout_bytes" in exp:
        p = os.path.join(run, "stdout.txt")
        n = os.path.getsize(p) if os.path.exists(p) else None
        if n != exp["stdout_bytes"]:
            F.append("STDOUT_BYTES %r != %r" % (n, exp["stdout_bytes"]))
    if exp["settlement"] == "SETTLED":
        fc = rc_.get("final_census") or {}
        if fc.get("owned_live") or fc.get("group_live") or fc.get("new_lane_live"):
            F.append("FINAL_CENSUS_NOT_CLEAR")
        if not rc_.get("go_sent"):
            F.append("GO_NOT_SENT")
    if sig.get("sent") and isinstance(sig.get("mono_sent"), (int, float)) and isinstance(rc_.get("mono_end"), (int, float)):
        res["signal_to_receipt_s"] = rc_["mono_end"] - sig["mono_sent"]
    try:
        n_s = 0
        other = []
        with open(os.path.join(run, "samples.jsonl"), "r", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    n_s += 1
                    json.loads(line)
        res["samples"] = n_s
    except (OSError, ValueError) as ex:
        if exp["settlement"] != "NOT_LAUNCHED":
            F.append("SAMPLES_UNREADABLE %r" % ex)
    res["verdict"] = "PASS" if not F else "FAIL"
    data = (json.dumps(res, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(out, "xb") as fh:
        fh.write(data)
    print(json.dumps({"scenario": name, "verdict": res["verdict"], "failed": F}))


if __name__ == "__main__":
    main()
