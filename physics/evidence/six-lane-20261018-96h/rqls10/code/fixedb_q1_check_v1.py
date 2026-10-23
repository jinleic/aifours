#!/usr/bin/env python3
"""fixedb_q1_check_v1: standard-library checker of the Q1 behaviour-qualification criteria for rqls_fixedb_lm_v4
(review/rqls10-fixedb-GO-request-v2.md section 3 as corrected by review/rqls10-fixedb-GO-request-v2-erratum-1.md).
Reads ONLY the Q1 outputs (prefix evidence/rqls_fixedb_lm_v4.q1.sv2.*) and the frozen config; computes nothing else.
Usage: fixedb_q1_check_v1.py PREFIX CONFIG OUT.json
Verdict: PASS (all criteria), FAIL (a criterion failed), INCONCLUSIVE (a gate failed before W, or a candidate / defect
stop occurred - the latter are reported for the candidate / defect path, not judged here).
"""
import hashlib, json, os, sys

PREFIX, CONFIG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


res = {"checker": "fixedb_q1_check_v1", "prefix": PREFIX, "config": {"path": CONFIG, "sha256": sha(CONFIG)}, "criteria": {}}
files = {k: PREFIX + k for k in (".result.jsonl", ".stdout.txt", ".stderr.txt", ".stop-receipt.json", ".launch.json",
                                 ".samples.jsonl", ".supervisor-receipt.json")}
res["files"] = {k: ({"bytes": os.path.getsize(p), "sha256": sha(p)} if os.path.exists(p) else None) for k, p in files.items()}
C = res["criteria"]
cfg = load_json(CONFIG)
sv = load_json(files[".supervisor-receipt.json"])
recs = []
with open(files[".result.jsonl"], "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            recs.append(json.loads(line))
stop = load_json(files[".stop-receipt.json"]) if os.path.exists(files[".stop-receipt.json"]) else None
res["supervisor"] = {k: sv.get(k) for k in ("status", "returncode", "trips", "sigterm_sent", "identity_ok_at_signal",
                                            "settlement", "group_members_after", "go_sent", "wall_s", "max_rss_bytes",
                                            "min_free_bytes", "error", "pid", "pgid")}
res["stop_receipt"] = stop
gates = {r["GATE"]: r["pass"] for r in recs if "GATE" in r}
res["gates"] = gates
rc = sv.get("returncode")
if rc in (7, 8):
    res["verdict"] = "INCONCLUSIVE"
    res["note"] = "candidate (7) or model-defect (8) stop: follow the request's candidate / defect path"
elif rc == 3 or any(v is False for v in gates.values()):
    res["verdict"] = "INCONCLUSIVE"
    res["note"] = "a gate failed before the target stages; scenarios (a)/(b) not exercised"
else:
    head = recs[0] if recs else {}
    C["assay_v4"] = head.get("assay") == "rqls_fixedb_lm_v4"
    C["argv_matches_config"] = sv.get("go_sent") is True and head.get("argv") == cfg["argv"][4:]
    C["gates_pass"] = all(gates.get(g) is True for g in ("S_input_pins", "S_jacobian", "S_anchors", "KP_near_anchor"))
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
    # (b) supervisor DEADLINE trip -> SIGTERM inside WD
    trips = sv.get("trips") or []
    C["b_supervisor"] = (sv.get("status") == "EXITED" and rc == 5 and bool(trips) and trips[0].get("trip") == "DEADLINE"
                         and sv.get("sigterm_sent") is True and sv.get("identity_ok_at_signal") is True
                         and sv.get("settlement") == "SETTLED" and sv.get("group_members_after") == [])
    C["b_latency"] = bool(trips) and isinstance(sv.get("wall_s"), (int, float)) and sv["wall_s"] - trips[0]["t"] <= 7.0
    C["b_stop_receipt"] = stop is not None and stop.get("status") == "TERMINATED_UNKNOWN" and stop.get("stage") == "WD"
    wd_runs = [r for r in runs if r["tag"] == "WD_target_d5"]
    last = recs[-1] if recs else {}
    C["b_last_record"] = (last.get("tag") == "WD_target_d5" and last.get("st") == "TERMINATED") or \
        (last.get("summary") is None and last.get("tag") == "WD_target_d5")
    C["b_no_wd_summary"] = not any(r.get("summary") == "WD_target_d5" for r in recs)
    C["b_no_end_record"] = not any(r.get("end") for r in recs)
    res["counts"] = {"W_runs": len(w_runs), "WD_runs": len(wd_runs),
                     "W_mean_s": (round(sum(r["s"] for r in w_runs) / len(w_runs), 3) if w_runs else None),
                     "WD_mean_s": (round(sum(r["s"] for r in wd_runs) / len(wd_runs), 3) if wd_runs else None),
                     "W_verified": sum(1 for r in w_runs if r.get("ok")), "WD_verified": sum(1 for r in wd_runs if r.get("ok")),
                     "W_status": {s: sum(1 for r in w_runs if r["st"] == s) for s in {r["st"] for r in w_runs}},
                     "WD_status": {s: sum(1 for r in wd_runs if r["st"] == s) for s in {r["st"] for r in wd_runs}}}
    res["verdict"] = "PASS" if all(C.values()) else "FAIL"
with open(OUT, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1)
print(json.dumps({"verdict": res["verdict"], "criteria": C, "counts": res.get("counts"), "gates": gates}))
