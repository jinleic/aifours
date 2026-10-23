#!/usr/bin/env python3
"""fixedb_q1_check_v3: standard-library checker for the bounded Q1 behaviour qualification of code/rqls_fixedb_lm_v6.py
run under code/owned_supervisor_v6.py. Supersedes fixedb_q1_check_v1/v2 (never run). Implements the raw checks listed
in RUN/review/rqls10-fixedB-v4-source-codex-v1.prompt.stdout.txt. Reads only the run directory and the frozen config;
computes nothing numerical. Strict JSON (duplicate keys and NaN/Infinity rejected).
Usage: fixedb_q1_check_v3.py RUN_DIR CONFIG OUT.json
Expected Q1 setting (config): child argv "... OUT WITNESS STOP 1100 q1 NN NC NKR NKR10 N8 1000 1000 NS", supervisor
max_wall_s 820, settle_s 120 (the parent may freeze other values; the checker reads them from the config).
Verdicts (first applicable): FAIL_BINDING, FAIL_SAFETY (any guard trip other than the single intended DEADLINE, cancel,
supervisor error, UNSETTLED, resource limit), CANDIDATE_STOP (exit 7), FAIL_MODEL_DEFECT (exit 8), INCONCLUSIVE_GATE
(exit 3 or any gate not passed), UNEXERCISED (a scenario precondition not met, e.g. W finished its runs before the
deadline or the signal did not land inside a WD LM interval), FAIL (any other criterion), PASS. A PASS establishes only
the observed bounded cancellation scenarios; it admits no Phase 1 or broader search.
"""
import hashlib, json, math, os, sys

GATES = ("S_runtime", "S_single_thread", "S_input_pins", "S_jacobian", "S_anchors", "N_negative_controls",
         "C_classical_only_v5", "KP_near_anchor", "KR_known_class_recovery")


def _pairs(kv):
    d = {}
    for k, v in kv:
        if k in d:
            raise ValueError("duplicate key %r" % k)
        d[k] = v
    return d


def _const(name):
    raise ValueError("non-finite constant %s" % name)


def jload(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_const)


def read(p):
    with open(p, "rb") as fh:
        raw = fh.read()
    return raw, hashlib.sha256(raw).hexdigest()


def isfin(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def main():
    run, cfg_path, outp = sys.argv[1], sys.argv[2], sys.argv[3]
    res = {"checker": "fixedb_q1_check_v3", "run_dir": run, "criteria": {}, "notes": [],
           "admission": "none: PASS qualifies only the observed bounded cancellation scenarios"}
    C = res["criteria"]
    verdict = None
    cfg_raw, cfg_sha = read(cfg_path)
    cfg = jload(cfg_raw)
    res["config_sha256"] = cfg_sha
    paths = {"receipt": cfg["receipt"], "settlement": cfg["settlement_record"], "launch": cfg["launch_record"],
             "samples": cfg["samples"], "out": cfg["argv"][4], "witness": cfg["argv"][5], "stop": cfg["argv"][6]}
    raw = {}
    for k, p in paths.items():
        try:
            raw[k] = read(p)
        except OSError:
            raw[k] = None
    res["files"] = {k: (None if v is None else {"path": paths[k], "bytes": len(v[0]), "sha256": v[1]}) for k, v in raw.items()}
    try:
        rc_ = jload(raw["receipt"][0])
        st = jload(raw["settlement"][0])
        launch = jload(raw["launch"][0])
        recs = [jload(x.encode("utf-8")) for x in raw["out"][0].decode("utf-8").splitlines() if x.strip()]
        samples = [jload(x.encode("utf-8")) for x in raw["samples"][0].decode("utf-8").splitlines() if x.strip()]
        stop = jload(raw["stop"][0]) if raw["stop"] is not None else None
    except Exception as ex:
        res["verdict"] = "FAIL_BINDING"
        res["notes"].append("unreadable or non-strict record: %r" % ex)
        return finish(res, outp)
    # binding
        # (settlement names the receipt; receipt binds config and supervisor; artifact hashes match current files)
    C["settlement_names_receipt"] = st.get("receipt_sha256") == raw["receipt"][1]
    C["receipt_binds_config"] = rc_.get("config_sha256") == cfg_sha
    C["receipt_supervisor_v6"] = rc_.get("supervisor") == "owned_supervisor_v6"
    arts = rc_.get("artifacts") or {}
    C["artifact_hashes_current"] = all((arts.get(paths[k]) or {}).get("sha256") == raw[k][1]
                                       for k in ("launch", "samples", "out") if raw[k] is not None) and \
        (raw["stop"] is None or (arts.get(paths["stop"]) or {}).get("sha256") == raw["stop"][1])
    C["identity_recorded"] = isinstance(launch.get("identity"), dict) and launch["identity"].get("pid") == rc_.get(
        "child_pid", launch.get("child_pid")) and launch["identity"].get("pgid") == launch["identity"].get("pid")
    head = recs[0] if recs else {}
    C["assay_v6"] = head.get("assay") == "rqls_fixedb_lm_v6" and head.get("argv") == cfg["argv"][4:] and \
        head.get("mode") == "q1"
    C["child_pid_matches"] = head.get("pid") == (launch.get("identity") or {}).get("pid")
    if not all(C[k] for k in ("settlement_names_receipt", "receipt_binds_config", "receipt_supervisor_v6",
                              "artifact_hashes_current", "identity_recorded", "assay_v6", "child_pid_matches")):
        res["verdict"] = "FAIL_BINDING"
        return finish(res, outp)
    # safety (supervisor)
    trips = rc_.get("trips") or []
    sig = rc_.get("signal") or {}
    sample_trips = [s for s in samples if s.get("stop") not in (None, "DEADLINE")]
    S = {"single_deadline_trip": len(trips) == 1 and trips[0].get("trip") == "DEADLINE",
         "samples_only_deadline_stop": not sample_trips,
         "settled": st.get("settlement") == "SETTLED" and rc_.get("settlement_before_publication") == "SETTLED",
         "no_flags": not rc_.get("flags"),
         "signal_identity_checked": sig.get("sent") is True and sig.get("identity_ok") is True,
         "no_cancel": not any(str(t.get("trip", "")).startswith("SUPERVISOR_CANCEL") for t in trips),
         "rss_within": (rc_.get("max") or {}).get("lane_rss", 0) <= cfg["rss_trip_bytes"],
         "free_within": rc_.get("min_free") is not None and rc_["min_free"] >= cfg["free_trip_bytes"],
         "output_within": (rc_.get("max") or {}).get("output_bytes", 0) <= cfg["output_trip_bytes"]}
    C.update({"safety_" + k: v for k, v in S.items()})
    if not all(S.values()):
        res["verdict"] = "FAIL_SAFETY"
        return finish(res, outp)
    crc = rc_.get("child_returncode")
    if crc == 7:
        res["verdict"] = "CANDIDATE_STOP"
        return finish(res, outp)
    if crc == 8:
        res["verdict"] = "FAIL_MODEL_DEFECT"
        return finish(res, outp)
    gates = [r for r in recs if "GATE" in r]
    gnames = [g["GATE"] for g in gates]
    first_w = next((k for k, r in enumerate(recs) if r.get("tag") == "W_target_cyc10"), None)
    gate_ok = crc != 3 and all(gnames.count(g) == 1 for g in GATES) and all(g["pass"] is True for g in gates) and \
        first_w is not None and all(recs.index(g) < first_w for g in gates if g["GATE"] in GATES)
    C["gates_once_pass_before_W"] = gate_ok
    if not gate_ok:
        res["verdict"] = "INCONCLUSIVE_GATE"
        return finish(res, outp)
    kp = [r for r in recs if str(r.get("tag", "")).startswith("KP_") and "st" in r]
    C["kp_eight_small_per_anchor"] = all(sum(1 for r in kp if r["tag"] == t and r["amp"] <= 1e-2) == 8
                                         for t in ("KP_anchor7", "KP_anchor8", "KP_parker10")) and \
        not any(r.get("status") == "SKIPPED_TIME" and str(r.get("tag", "")).startswith("KP_") and r.get("amp", 1) <= 1e-2
                for r in recs)
    # W: child-side deadline
    w_runs = [(k, r) for k, r in enumerate(recs) if r.get("tag") == "W_target_cyc10" and "st" in r]
    w_dead = [k for k, r in w_runs if r["st"] == "DEADLINE"]
    w_skip = [(k, r) for k, r in enumerate(recs) if r.get("tag") == "W_target_cyc10" and r.get("status") == "SKIPPED_TIME"]
    w_sum = [(k, r) for k, r in enumerate(recs) if r.get("summary") == "W_target_cyc10"]
    w_plan = (head.get("plan_end_mono") or {}).get("W")
    if not w_dead:
        res["verdict"] = "UNEXERCISED"
        res["notes"].append("no W run ended with DEADLINE (W may have finished its runs early)")
        return finish(res, outp)
    kd, rd = w_dead[0], recs[w_dead[0]]
    C["w_one_deadline_last"] = len(w_dead) == 1 and w_runs[-1][0] == kd
    C["w_halt_reason_deadline"] = (rd.get("halt") or {}).get("reason") == "DEADLINE"
    C["w_deadline_endpoint_finite"] = rd.get("res_finite") is True and isfin(rd.get("res")) and rd["res"] >= 0 and \
        rd.get("md_finite") is True and all(isfin(x) for x in (rd.get("mdf") or [None]))
    C["w_skip_count"] = len(w_skip) == 1 and w_skip[0][1].get("count") == 1000 - len(w_runs) and \
        w_skip[0][1]["count"] > 0
    C["w_order"] = len(w_sum) == 1 and kd < w_skip[0][0] < w_sum[0][0] if w_skip and w_sum else False
    C["w_summary_within_2s_of_plan_end"] = bool(w_sum) and isfin(w_plan) and 0 <= w_sum[0][1]["mono"] - w_plan <= 2.0
    # WD: supervisor signal inside an LM interval
    wd_runs = [(k, r) for k, r in enumerate(recs) if r.get("tag") == "WD_target_d5" and "st" in r]
    sent = sig.get("mono_sent")
    term = [r for k, r in wd_runs if r["st"] == "TERMINATED"]
    if not (isfin(sent) and len(term) == 1 and isfin(term[0].get("mono_lm_start")) and
            isfin(term[0].get("mono_lm_end")) and term[0]["mono_lm_start"] <= sent <= term[0]["mono_lm_end"]):
        res["verdict"] = "UNEXERCISED"
        res["notes"].append("the supervisor signal did not land inside exactly one WD LM interval")
        return finish(res, outp)
    rt = term[0]
    C["wd_terminated_is_final_record"] = recs[-1] is rt
    C["wd_halt_inside_lm_after_signal"] = (rt.get("halt") or {}).get("reason") == "TERMINATED" and \
        isfin((rt.get("halt") or {}).get("mono")) and sent <= rt["halt"]["mono"] <= rt["mono_lm_end"]
    C["wd_iteration_work_before_signal"] = isfin(rt.get("last_iter_start_mono")) and rt["last_iter_start_mono"] <= sent \
        and rt.get("it", 0) >= 1
    C["wd_no_summary_ws_end"] = not any(r.get("summary") == "WD_target_d5" or r.get("tag") == "WS_target_seeded" or
                                        r.get("end") for r in recs)
    # latency and stop receipt
    rec_end = rc_.get("mono_end")
    C["latency_signal_to_receipt_le_7s"] = isfin(rec_end) and 0 <= rec_end - sent <= 7.0
    C["latency_trip_to_receipt_le_7s"] = isfin(rec_end) and isfin(trips[0].get("mono")) and \
        0 <= rec_end - trips[0]["mono"] <= 7.0
    C["child_rc_5"] = crc == 5
    C["stop_receipt"] = stop is not None and stop.get("status") == "TERMINATED_UNKNOWN" and stop.get("stage") == "WD" and \
        stop.get("terminated") is True and stop.get("jsonl_records") == len(recs) and \
        stop.get("jsonl_bytes") == len(raw["out"][0])
    C["no_witness"] = raw["witness"] is None
    res["raw"] = {"signal_mono_sent": sent, "receipt_mono_end": rec_end, "w_plan_end": w_plan,
                  "w_summary_mono": w_sum[0][1]["mono"] if w_sum else None, "wd_lm": [rt["mono_lm_start"], rt["mono_lm_end"]],
                  "wd_halt": rt.get("halt"), "w_runs": len(w_runs), "wd_runs": len(wd_runs)}
    res["verdict"] = "PASS" if all(C.values()) else "FAIL"
    return finish(res, outp)


def finish(res, outp):
    data = (json.dumps(res, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(outp, "xb") as fh:
        fh.write(data)
    print(json.dumps({"verdict": res["verdict"], "failed": sorted(k for k, v in res["criteria"].items() if not v),
                      "notes": res["notes"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
