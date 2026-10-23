#!/usr/bin/env python3
"""fixedb_q1_check_v2: standard-library checker of the Q1 behaviour-qualification criteria for rqls_fixedb_lm_v4
(review/rqls10-fixedb-GO-request-v2.md section 3, corrected by the MANDATORY erratum
review/rqls10-fixedb-GO-request-v2-erratum-1.md). Supersedes fixedb_q1_check_v1 (never run).
v2 change (parent instruction 05:4x): the INTENDED supervisor DEADLINE trip (the test trip) is distinguished from every
other guard trip, from supervisor cancellation and from supervisor errors; a PASS never admits Phase 1 or any broader
search (field "admission").
Reads ONLY the Q1 outputs (prefix evidence/rqls_fixedb_lm_v4.q1.sv2.*) and the frozen config; computes nothing else.
Usage: fixedb_q1_check_v2.py PREFIX CONFIG OUT.json
Verdicts:
  PASS                     rc 5 after the intended DEADLINE trip, SETTLED, and every criterion (a), (b) holds.
  FAIL_GUARD_TRIP          any trip other than one DEADLINE at >= max_wall_s (RSS, FREE, OUTPUT, *_UNREADABLE,
                           SUPERVISOR_CANCEL_*, FINALLY_SETTLE*), any non-DEADLINE trip value in the samples, a
                           supervisor error or cancel signal - regardless of the child's outcome.
  FAIL_UNSETTLED           supervisor settlement != SETTLED (with no other guard trip).
  INCONCLUSIVE_GATE_FAIL   child exit 3 (a gate failed before W): honest inconclusive, scenarios (a)/(b) not exercised.
  CANDIDATE_STOP           child exit 7: follow the candidate path of request v1 section 4 / v2; not judged here.
  FAIL_MODEL_DEFECT        child exit 8.
  FAIL                     any other outcome (exit 0, 2, 4, 6, missing files) or a failed criterion.
"""
import hashlib, json, os, sys

PREFIX, CONFIG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(p):
    out = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out


res = {"checker": "fixedb_q1_check_v2", "prefix": PREFIX, "config": {"path": CONFIG, "sha256": sha(CONFIG)},
       "criteria": {}, "admission": "none: a PASS qualifies stop/deadline behaviour only; Phase 1 and any broader search "
                                    "need a separate parent GO"}
files = {k: PREFIX + k for k in (".result.jsonl", ".stdout.txt", ".stderr.txt", ".stop-receipt.json", ".launch.json",
                                 ".samples.jsonl", ".supervisor-receipt.json")}
res["files"] = {k: ({"bytes": os.path.getsize(p), "sha256": sha(p)} if os.path.exists(p) else None) for k, p in files.items()}
C = res["criteria"]
cfg = load_json(CONFIG)
missing = [k for k in (".result.jsonl", ".samples.jsonl", ".supervisor-receipt.json") if res["files"][k] is None]
if missing:
    res["verdict"] = "FAIL"
    res["note"] = "missing outputs: " + ", ".join(missing)
else:
    sv = load_json(files[".supervisor-receipt.json"])
    recs = load_jsonl(files[".result.jsonl"])
    samples = load_jsonl(files[".samples.jsonl"])
    stop = load_json(files[".stop-receipt.json"]) if res["files"][".stop-receipt.json"] else None
    res["supervisor"] = {k: sv.get(k) for k in ("status", "returncode", "trips", "sigterm_sent", "identity_ok_at_signal",
                                                "settlement", "group_members_after", "go_sent", "wall_s", "max_rss_bytes",
                                                "min_free_bytes", "error", "cancel_signal", "pid", "pgid")}
    res["stop_receipt"] = stop
    gates = {r["GATE"]: r["pass"] for r in recs if "GATE" in r}
    res["gates"] = gates
    rc = sv.get("returncode")
    # guard-trip classification (applies to every outcome)
    mw, sp = float(cfg["max_wall_s"]), float(cfg["sample_s"])
    trips = sv.get("trips") or []
    strips = [(s.get("t"), s.get("trip")) for s in samples if s.get("trip") is not None]
    intended = (len(trips) == 1 and trips[0].get("trip") == "DEADLINE" and isinstance(trips[0].get("t"), (int, float))
                and mw <= trips[0]["t"] <= mw + sp + 1.0)
    other = [t for t in trips if t.get("trip") != "DEADLINE"] + [{"t": t, "trip": v} for t, v in strips if v != "DEADLINE"]
    early = [t for t, v in strips if v == "DEADLINE" and t < mw]
    guard_fail = bool(other) or bool(early) or len(trips) > 1 or sv.get("cancel_signal") is not None or \
        sv.get("error") is not None
    res["guard"] = {"intended_deadline_trip": intended, "other_trips": other, "early_deadline_samples": early,
                    "n_trip_samples": len(strips), "cancel_signal": sv.get("cancel_signal"), "error": sv.get("error"),
                    "max_rss_below_trip": isinstance(sv.get("max_rss_bytes"), int) and sv["max_rss_bytes"] < cfg["rss_trip_bytes"],
                    "min_free_above_trip": isinstance(sv.get("min_free_bytes"), int) and sv["min_free_bytes"] >= cfg["free_trip_bytes"]}
    if guard_fail:
        res["verdict"] = "FAIL_GUARD_TRIP"
        res["note"] = "a guard trip other than the intended DEADLINE, a cancel or a supervisor error occurred"
    elif sv.get("settlement") != "SETTLED":
        res["verdict"] = "FAIL_UNSETTLED"
    elif rc == 7:
        res["verdict"] = "CANDIDATE_STOP"
        res["note"] = "candidate stop: follow the candidate path; nothing is claimed"
    elif rc == 8:
        res["verdict"] = "FAIL_MODEL_DEFECT"
    elif rc == 3 or any(v is False for v in gates.values()):
        res["verdict"] = "INCONCLUSIVE_GATE_FAIL"
        res["note"] = "a gate failed before the target stages; scenarios (a)/(b) not exercised"
    elif rc != 5:
        res["verdict"] = "FAIL"
        res["note"] = "unexpected child return code %r" % (rc,)
    else:
        head = recs[0] if recs else {}
        C["assay_v4"] = head.get("assay") == "rqls_fixedb_lm_v4"
        C["argv_matches_config"] = sv.get("go_sent") is True and head.get("argv") == cfg["argv"][4:]
        C["gates_pass"] = all(gates.get(g) is True for g in ("S_input_pins", "S_jacobian", "S_anchors", "KP_near_anchor"))
        C["resources_within_trips"] = res["guard"]["max_rss_below_trip"] and res["guard"]["min_free_above_trip"]
        runs = [r for r in recs if "tag" in r and "st" in r]
        C["no_defects_or_candidates"] = not any(r.get("model_defect") or r.get("maximal_candidate") for r in runs)
        # (a) child-side DEADLINE at the W stage end
        w_runs = [r for r in runs if r["tag"] == "W_target_cyc10"]
        w_dead = [k for k, r in enumerate(w_runs) if r["st"] == "DEADLINE"]
        w_sum = [r for r in recs if r.get("summary") == "W_target_cyc10"]
        w_skip = [r for r in recs if r.get("tag") == "W_target_cyc10" and r.get("status") == "SKIPPED_TIME"]
        C["a_one_deadline_run_last"] = len(w_dead) == 1 and w_dead[0] == len(w_runs) - 1
        C["a_skipped_record"] = len(w_skip) == 1
        C["a_summary_time"] = len(w_sum) == 1 and 612.0 <= w_sum[0]["elapsed_s"] <= 614.0
        C["a_deadline_endpoint_finite"] = bool(w_dead) and w_runs[w_dead[0]].get("md", 1e9) < 1e9
        # (b) intended supervisor DEADLINE trip -> SIGTERM inside WD
        C["b_intended_deadline_trip"] = intended
        C["b_supervisor"] = (sv.get("status") == "EXITED" and sv.get("sigterm_sent") is True
                             and sv.get("identity_ok_at_signal") is True and sv.get("group_members_after") == [])
        C["b_latency"] = intended and isinstance(sv.get("wall_s"), (int, float)) and sv["wall_s"] - trips[0]["t"] <= 7.0
        C["b_stop_receipt"] = stop is not None and stop.get("status") == "TERMINATED_UNKNOWN" and stop.get("stage") == "WD"
        wd_runs = [r for r in runs if r["tag"] == "WD_target_d5"]
        last = recs[-1] if recs else {}
        C["b_last_record_is_wd_run"] = last.get("tag") == "WD_target_d5" and "st" in last
        C["b_no_wd_summary"] = not any(r.get("summary") == "WD_target_d5" for r in recs)
        C["b_no_end_record"] = not any(r.get("end") for r in recs)
        res["counts"] = {"W_runs": len(w_runs), "WD_runs": len(wd_runs),
                         "W_mean_s": (round(sum(r["s"] for r in w_runs) / len(w_runs), 3) if w_runs else None),
                         "WD_mean_s": (round(sum(r["s"] for r in wd_runs) / len(wd_runs), 3) if wd_runs else None),
                         "W_verified": sum(1 for r in w_runs if r.get("ok")),
                         "WD_verified": sum(1 for r in wd_runs if r.get("ok")),
                         "W_status": {s: sum(1 for r in w_runs if r["st"] == s) for s in {r["st"] for r in w_runs}},
                         "WD_status": {s: sum(1 for r in wd_runs if r["st"] == s) for s in {r["st"] for r in wd_runs}},
                         "WD_last_status": last.get("st")}
        res["verdict"] = "PASS" if all(C.values()) else "FAIL"
with open(OUT, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1)
print(json.dumps({"verdict": res["verdict"], "criteria": C, "guard": res.get("guard"), "counts": res.get("counts"),
                  "gates": res.get("gates"), "admission": res["admission"]}))
