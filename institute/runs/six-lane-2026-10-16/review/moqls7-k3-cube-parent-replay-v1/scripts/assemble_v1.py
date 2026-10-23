#!/usr/bin/env python3
"""Assemble RESULT.json for the parent K3 cube replay desk review/moqls7-k3-cube-parent-replay-v1.

Usage: assemble_v1.py TAG:CUBE [TAG:CUBE ...]     e.g. assemble_v1.py v1:C321 v1:C411

Reads the desk's exclusive receipts (never modifies them), re-hashes every referenced receipt and log, checks the
hash bindings recorded at run time (pre and launch receipt SHA-256 in the final receipt, solver and checker log
SHA-256), and writes RESULT.json exclusively. No native or subprocess launch.
"""
import hashlib
import json
import os
import sys

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
K2_RESULT = os.path.join(REVIEW, "moqls7-k2-parent-v1", "RESULT.r2.json")
LANE_CERT = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/cert_r2"
DEVIATIONS = os.path.join(DESK, "deviations-v1.json")
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
READ_ONLY_INPUTS = [os.path.join(LANE, "code", "k3_cubes.py"), os.path.join(LANE, "code", "gram_enc.py"),
                    os.path.join(LANE, "review", "AMENDMENT-2.r1.md"),
                    os.path.join(REVIEW, "moqls7-parent-proofcheck-v1", "drat-trim"),
                    "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical"]


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(rel):
    p = os.path.join(DESK, rel)
    with open(p, "rb") as f:
        b = f.read()
    return json.loads(b), hashlib.sha256(b).hexdigest()


def instance(tag, cube):
    label = "%s-A_%s" % (tag, cube)
    final, final_sha = load("receipts/%s.json" % label)
    pre_sha = sha_file(os.path.join(DESK, "receipts", label + ".pre.json"))
    launch_path = os.path.join(DESK, "receipts", label + ".launch.json")
    launch_sha = sha_file(launch_path) if os.path.exists(launch_path) else None
    rec = final.get("pipeline") or {}
    logs = {}
    for key in ("solver_log", "checker_log"):
        if rec.get(key):
            p = os.path.join(DESK, rec[key])
            now_sha = sha_file(p)
            logs[rec[key]] = {"sha256": now_sha, "bytes": os.path.getsize(p),
                              "equals_receipt": now_sha == rec.get(key + "_sha256")}
    ch = rec.get("children", {})
    regen = final.get("regen") or {}
    bins = final.get("binaries_at_spawn") or {}
    after = final.get("binaries_after") or {}
    return {
        "label": label, "verdict": final.get("verdict"),
        "receipt": "receipts/%s.json" % label, "receipt_sha256": final_sha,
        "pre_receipt": "receipts/%s.pre.json" % label, "pre_receipt_sha256": pre_sha,
        "pre_receipt_bound": pre_sha == final.get("pre_receipt_sha256"),
        "launch_receipt": "receipts/%s.launch.json" % label if launch_sha else None,
        "launch_receipt_sha256": launch_sha,
        "launch_receipt_bound": launch_sha == final.get("launch_receipt_sha256"),
        "expected_cnf_sha256": final.get("expected_cnf_sha256"),
        "regenerated_cnf_sha256": regen.get("cnf_sha256"), "cnf_hash_match": regen.get("cnf_hash_match"),
        "cnf_bytes": regen.get("cnf_bytes"), "cnf_header": regen.get("cnf_header"),
        "base_cnf_sha256": regen.get("base_cnf_sha256"), "base_cnf_equals_brief": regen.get("base_cnf_equals_brief"),
        "meta_agreement": regen.get("meta_agreement"),
        "solver_rc": ch.get("solver", {}).get("rc"), "checker_rc": ch.get("checker", {}).get("rc"),
        "checker_status_lines": (rec.get("checker_flags") or {}).get("status_lines"),
        "checker_flags": rec.get("checker_flags"), "solver_status_lines": rec.get("solver_status_lines"),
        "solver_log_equals_producer": final.get("solver_log_equals_producer"),
        "safety_stop_reason": rec.get("safety_stop_reason"), "deferred": rec.get("deferred"),
        "grace_exceeded": rec.get("grace_exceeded"),
        "times": {"driver_started_at": final.get("started_at"), "pipeline_started_at": rec.get("started_at"),
                  "pipeline_finished_at": rec.get("finished_at"), "pipeline_seconds": rec.get("pipeline_seconds"),
                  "solver": {k: ch.get("solver", {}).get(k) for k in ("wall_seconds", "user_seconds", "sys_seconds",
                                                                      "ended_at")},
                  "checker": {k: ch.get("checker", {}).get(k) for k in ("wall_seconds", "user_seconds",
                                                                        "sys_seconds", "ended_at")},
                  "driver_finished_at": final.get("finished_at"), "driver_seconds": final.get("driver_seconds"),
                  "regeneration_seconds": (regen.get("regen_run") or {}).get("seconds")},
        "rss": {"peak_sampled_aggregate_bytes": rec.get("peak_sampled_aggregate_rss_bytes"),
                "samples": rec.get("rss_samples"), "solver_maxrss_bytes": ch.get("solver", {}).get("maxrss_bytes"),
                "checker_maxrss_bytes": ch.get("checker", {}).get("maxrss_bytes")},
        "free_bytes": {"gates": rec.get("gates"), "at_pipeline_start": rec.get("free_bytes_start"),
                       "min_sampled_in_flight": rec.get("min_sampled_free_bytes"), "at_end": rec.get("free_bytes_end")},
        "logs": logs, "logs_unchanged": all(v["equals_receipt"] for v in logs.values()) if logs else None,
        "binaries_at_spawn": {k: v.get("sha256") for k, v in bins.items()},
        "binaries_after": {k: v.get("sha256") for k, v in after.items()},
        "binaries_unchanged": ({k: v.get("sha256") for k, v in bins.items()}
                               == {k: v.get("sha256") for k, v in after.items()}) if bins and after else None,
        "pins_unchanged": final.get("pins_unchanged"),
        "solver_argv": rec.get("solver_argv"), "checker_argv": rec.get("checker_argv"),
    }


def compare_with_producer_log(row, cube):
    """Line-by-line comparison of the parent checker log with the producer's lane checker log (read-only)."""
    lane_log = os.path.join(LANE_CERT, "A_%s.checker.log" % cube)
    mine_rel = [k for k in row["logs"] if k.endswith(".checker.log")]
    if not mine_rel:
        return None
    with open(os.path.join(DESK, mine_rel[0]), "rb") as f:
        mine = f.read().split(b"\n")
    with open(lane_log, "rb") as f:
        lb = f.read()
    prod = lb.split(b"\n")
    diff = [{"line": i + 1, "parent": a.decode("ascii", "replace"), "producer": b.decode("ascii", "replace")}
            for i, (a, b) in enumerate(zip(mine, prod)) if a != b]
    return {"producer_log": lane_log, "producer_log_sha256": hashlib.sha256(lb).hexdigest(),
            "producer_log_sha256_equals_producer_receipt": (hashlib.sha256(lb).hexdigest()
                                                            == row["producer_receipt"].get("checker_log_sha256")),
            "line_counts": [len(mine), len(prod)], "differing_lines": diff}


def main():
    specs = [s.split(":") for s in sys.argv[1:]]
    out_path = os.path.join(DESK, "RESULT.json")
    if os.path.lexists(out_path):
        raise SystemExit("exists: " + out_path)
    inst = {}
    for tag, cube in specs:
        row = instance(tag, cube)
        pre, _ = load("receipts/%s.pre.json" % row["label"])
        pr = pre["producer"]["receipt_fields"]
        row["producer_receipt"] = {"path": pre["producer"]["receipt"]["path"],
                                   "sha256": pre["producer"]["receipt"]["sha256"],
                                   "meta_path": pre["producer"]["meta"]["path"],
                                   "meta_sha256": pre["producer"]["meta"]["sha256"],
                                   "seconds": pr.get("seconds"), "solver_rc": pr.get("solver_rc"),
                                   "checker_rc": pr.get("checker_rc"),
                                   "checker_status_lines": pr.get("checker_status_lines"),
                                   "peak_sampled_aggregate_rss_bytes": pr.get("peak_sampled_aggregate_rss_bytes"),
                                   "solver_binary_sha256": pr.get("solver_binary_sha256"),
                                   "checker_binary_sha256": pr.get("checker_binary_sha256"),
                                   "solver_log_sha256": pr.get("solver_log_sha256"),
                                   "checker_log_sha256": pr.get("checker_log_sha256"),
                                   "consistency_checks": pre["producer"]["checks"]}
        row["lane_cnf_copy"] = pre["producer"]["lane_cnf_copy"]
        row["scripts_sha256_at_pre"] = pre["scripts_sha256"]
        row["interpreter"] = pre["interpreter_binary"]
        row["gate_rule"] = pre["gate_rule"]
        row["checker_log_vs_producer"] = compare_with_producer_log(row, cube)
        recheck = {}
        for key in ("receipt", "meta", "lane_cnf_copy"):
            ent = pre["producer"][key]
            now_sha = sha_file(ent["path"])
            recheck[key] = {"path": ent["path"], "sha256_at_pre": ent["sha256"], "sha256_at_assembly": now_sha,
                            "unchanged": now_sha == ent["sha256"]}
        row["lane_inputs_recheck"] = recheck
        inst["A_" + cube] = row
    regen = {}
    for cube in ("C321", "C411"):
        p = "receipts/v1-regen-A_%s.json" % cube
        if os.path.exists(os.path.join(DESK, p)):
            r, h = load(p)
            regen["A_" + cube] = {"receipt": p, "sha256": h, "result": r.get("result"),
                                  "cnf_sha256": (r.get("regen") or {}).get("cnf_sha256")}
    sc, sc_sha = load("receipts/v1-selfcheck-summary.json")
    selfcheck = {"summary": "receipts/v1-selfcheck-summary.json", "summary_sha256": sc_sha,
                 "pre_receipt_sha256": sha_file(os.path.join(DESK, "receipts", "v1-selfcheck.pre.json")),
                 "all_match": sc["all_match"], "parser_all_ok": sc["parser_all_ok"],
                 "verdict_logic_ok": sc["verdict_logic_ok"],
                 "rows": [{k: r[k] for k in ("label", "expect", "verdict", "solver_rc", "checker_rc",
                                             "checker_status_lines", "receipt_sha256")} for r in sc["rows"]],
                 "receipts_rehashed_equal": all(sha_file(os.path.join(DESK, "receipts", r["label"] + ".json"))
                                                == r["receipt_sha256"] for r in sc["rows"])}
    k2 = {"path": K2_RESULT, "sha256": sha_file(K2_RESULT)}
    with open(K2_RESULT) as f:
        ctrls = json.load(f).get("controls", {})
    k2["controls"] = {n: {"outcome": c.get("outcome"), "matches_expectation": c.get("matches_expectation")}
                      for n, c in ctrls.items()}
    verdicts = {k: v["verdict"] for k, v in inst.items()}
    with open(DEVIATIONS) as f:
        dev = json.load(f)
    result = {
        "desk": "review/moqls7-k3-cube-parent-replay-v1",
        "scope": ("Per-instance verification evidence only: for each listed K3 covering cube CNF (encoder A), the "
                  "parent regenerated the CNF from the pinned lane code, matched the brief's SHA-256, and checked a "
                  "freshly streamed CaDiCaL binary DRAT refutation with the parent-built drat-trim. No K3, M(7), "
                  "coverage, bridge or theorem verdict. C311 is not part of this desk."),
        "verdicts": verdicts,
        "instances": inst,
        "regeneration_precheck": regen,
        "transport_selfcheck": selfcheck,
        "parent_checker_controls_cited": k2,
        "deviations": {"path": "deviations-v1.json", "sha256": sha_file(DEVIATIONS), "items": dev},
        "read_only_inputs_at_assembly": {p: sha_file(p) for p in READ_ONLY_INPUTS},
        "scripts_sha256_now": {n: sha_file(os.path.join(DESK, "scripts", n))
                               for n in sorted(os.listdir(os.path.join(DESK, "scripts"))) if n.endswith(".py")},
    }
    with open(out_path, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({"RESULT.json": sha_file(out_path), "verdicts": verdicts}))


if __name__ == "__main__":
    main()
