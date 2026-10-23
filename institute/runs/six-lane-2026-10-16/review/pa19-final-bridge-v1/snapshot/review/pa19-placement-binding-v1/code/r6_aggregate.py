#!/usr/bin/env python3
"""R6 aggregate: write placement-binding-result.json from pin-v1.json, cases/*.json, run logs and
mutation controls. Read-only on S and L (it re-hashes the live stored lists at aggregation time to
bind lists that appeared after their case was processed, by exact SHA-256 against the parent
regeneration). Writes OUT/<name> with mode x.
Usage (research venv): python -B r6_aggregate.py placement-binding-result.json [mutation-controls-v1.json]
"""
import glob
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from r6_replay import S, L, VENV_PY, SRC_USED  # noqa: E402

PROD_CALLS = {
    "m1_ms01": "run_hard4.py:91  [VENV_PY, src/extend_p1.py, cases19skel/specs/<tag>.json, cycle2/a3/<tag>/ext.json]",
    "m1_ms09": "run_hard5.py:97, run_hard6.py:67, run_hard7.py:69, run_hard8.py:99  "
               "[VENV_PY, src/extend_p1q.py, cases19skel/specs/<tag>.json, cycle2/part/<tag>/ext.json, '1']",
    "m2": "run_m2partbatch5.py:53  [sys.executable, src/extend_b.py, LANE/cycle2/skel-b/skeletons-b-msXX.json, <b>, "
          "cycle2/m2part_drat/msXX_bNNNNN/ext.json]  (the runner's interpreter is not recorded by the lane)",
}
WORKER_CHECK_COPIES = {
    "cycle2/part/check-extb-ms01_b1554.json": ("ms01_s01260", "m2"),
    "cycle2/part/check2-extb-ms01_b1554.json": ("ms01_s01260", "m2"),
    "cycle2/part/check-extb-ms09_b9.json": ("ms09_s00001", "m2"),
    "cycle2/part/check2-extb-ms09_b9.json": ("ms09_s00001", "m2"),
    "cycle2/part/check-ms09_s00001-ext.json": ("ms09_s00001", "m1"),
}


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def fsha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    name = sys.argv[1]
    mut_name = sys.argv[2] if len(sys.argv) > 2 else None
    pin = json.load(open(os.path.join(OUT, "pin-v1.json")))
    cases = {}
    for p in sorted(glob.glob(os.path.join(OUT, "cases", "ms*_s*.json"))):
        b = os.path.basename(p)
        if b.count(".") == 1:
            cases[b[:-5]] = json.load(open(p))
    runs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(OUT, "logs", "run-*-end.json")))]
    rows, mismatches, incremental_m1, incremental_m2, late = [], [], [], [], []
    missing_cases = []
    for c in pin["cases"]:
        tag = c["tag"]
        r = cases.get(tag)
        if r is None:
            missing_cases.append(tag)
            continue
        ind = r["independent"]
        row = {"tag": tag, "multiset": r["multiset"], "skel_index": r["skel_index"], "b_index": r["b_index"],
               "status": r["status"], "m1_binding": r["m1_binding"], "m2_binding": r["m2_binding"],
               "counts": r["counts"], "row_level_labeled": ind["row_level_control"]["labeled"],
               "row_level_control_ok": ind["row_level_control"]["ok"],
               "isomorphisms_a_to_b": ind["isomorphisms"], "iso_first": ind["iso_first"],
               "orbits_burnside_a": ind["orbits_a_burnside"],
               "transport_matching_sha256": (ind["m1_to_m2_transport"] or {}).get("matching_sha256"),
               "shas": r["shas"],
               "m1_regen": {k: r["m1_regen"].get(k) for k in ("elapsed_s", "ru_maxrss_bytes", "limit_reason",
                                                              "returncode", "out_bytes")},
               "m2_regen": {k: r["m2_regen"].get(k) for k in ("elapsed_s", "ru_maxrss_bytes", "limit_reason",
                                                              "returncode", "out_bytes")},
               "m1_stored_read": {k: r["m1_stored"].get(k) for k in ("status", "read_at", "mtime", "size")},
               "m2_stored_read": {k: r["m2_stored"].get(k) for k in ("status", "read_at", "mtime", "size")},
               "live_source_drift": r["live_source_drift"], "run_id": r["run_id"], "finished": r["finished"]}
        bad = [k for k, v in r["checks"].items() if not v]
        if bad or r["status"] != "REPLAYED_MATCH":
            mismatches.append({"tag": tag, "status": r["status"], "failed_checks": bad,
                               "m1_diff_vs_stored": r["m1_regen"].get("diff_vs_stored"),
                               "m2_diff_vs_stored": r["m2_regen"].get("diff_vs_stored"),
                               "lists": ind["lists"], "spec_binding": r["spec_binding"],
                               "m1_regen_stderr": r["m1_regen"].get("stderr_tail"),
                               "m2_regen_stderr": r["m2_regen"].get("stderr_tail")})
        # live re-hash at aggregation time (lists that appeared or changed after the case was read)
        mi, bi = r["multiset"], r["b_index"]
        m1p = os.path.join(L, "cycle2", "a3" if mi == 1 else "part", tag, "ext.json")
        m2p = os.path.join(L, "cycle2", "m2part_drat", "ms%02d_b%05d" % (mi, bi), "ext.json")
        now_m1 = fsha(m1p) if os.path.isfile(m1p) else None
        now_m2 = fsha(m2p) if os.path.isfile(m2p) else None
        row["aggregate_rehash"] = {"m1": now_m1, "m2": now_m2}
        if r["m1_stored"]["status"] == "read" and now_m1 != r["m1_stored"]["sha256"]:
            late.append({"tag": tag, "list": "m1", "event": "changed_after_read", "read_sha256": r["m1_stored"]["sha256"],
                         "now_sha256": now_m1})
        if r["m1_stored"]["status"] != "read":
            ev = {"tag": tag, "list": "m1", "predicted_sha256": r["shas"]["m1_regen"],
                  "predicted_raw": r["counts"]["m1_raw"], "predicted_num_full": r["counts"]["m1_num_full"],
                  "now_sha256": now_m1}
            ev["now_equals_predicted"] = now_m1 is not None and now_m1 == r["shas"]["m1_regen"]
            incremental_m1.append(ev)
            if now_m1 is not None:
                late.append(dict(ev, event="appeared_after_processing"))
        if r["m2_stored"]["status"] == "read" and now_m2 != r["m2_stored"]["sha256"]:
            late.append({"tag": tag, "list": "m2", "event": "changed_after_read", "read_sha256": r["m2_stored"]["sha256"],
                         "now_sha256": now_m2})
        if r["m2_stored"]["status"] != "read":
            ev = {"tag": tag, "b_index": bi, "list": "m2",
                  "predicted_sha256_with_production_source": r["shas"]["m2_regen_normalized_production_source"],
                  "parent_generated_raw": r["counts"]["m2_raw"], "parent_generated_aut": r["counts"]["m2_aut"],
                  "parent_generated_num_placements": r["counts"]["m2_num"], "now_sha256": now_m2}
            ev["now_equals_predicted"] = now_m2 is not None and now_m2 == r["shas"]["m2_regen_normalized_production_source"]
            incremental_m2.append(ev)
            if now_m2 is not None:
                late.append(dict(ev, event="appeared_after_processing"))
        rows.append(row)
    # worker check copies vs R6 regeneration payloads
    wcc = []
    for rel, (tag, kind) in WORKER_CHECK_COPIES.items():
        p = os.path.join(L, rel)
        if not os.path.isfile(p) or tag not in cases:
            wcc.append({"path": rel, "present": os.path.isfile(p)})
            continue
        obj = json.load(open(p))
        lists = cases[tag]["independent"]["lists"]
        if kind == "m2":
            mine = lists["m2_regen"]["ordered_payload_sha256"]
            theirs = hashlib.sha256(json.dumps(obj["placements"]).encode()).hexdigest()
        else:
            mine = lists["m1_stored"]["ordered_payload_sha256"]
            theirs = hashlib.sha256(json.dumps(obj["full"]).encode()).hexdigest()
        wcc.append({"path": rel, "sha256": fsha(p), "payload_sha256": theirs, "r6_payload_sha256": mine,
                    "payload_equal": mine == theirs, "note": "worker check copy, not a production list"})
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    m1b, m2b = {}, {}
    for r in rows:
        m1b[r["m1_binding"]] = m1b.get(r["m1_binding"], 0) + 1
        m2b[r["m2_binding"]] = m2b.get(r["m2_binding"], 0) + 1
    mut = None
    if mut_name and os.path.isfile(os.path.join(OUT, mut_name)):
        M = json.load(open(os.path.join(OUT, mut_name)))
        mut = {"file": mut_name, "sha256": fsha(os.path.join(OUT, mut_name)), "baselines": len(M["baselines"]),
               "all_baselines_accepted": M["all_baselines_accepted"], "controls": len(M["controls"]),
               "all_rejected_for_intended_reason": M["all_rejected_for_intended_reason"],
               "not_applicable": M["not_applicable"],
               "per_control": [[c["case"], c["control"], c["rejected_for_intended_reason"]] for c in M["controls"]]}
    code = {os.path.basename(p): fsha(p) for p in sorted(glob.glob(os.path.join(HERE, "*.py")))}
    ms01 = [r for r in rows if r["multiset"] == 1]
    ms09 = [r for r in rows if r["multiset"] == 9]
    res = {
        "recorded_at": now(),
        "scope": ("R6 placement-split binding replay for PA(19,8,6): parent regeneration of the lane enumerators "
                  "extend_p1 (ms01 A3), extend_p1q m=1 (ms09 A3') and extend_b (M2) from pinned code and specs, "
                  "byte/semantic comparison with the stored lists, and parent-owned independent orbit semantics. "
                  "No SAT solver, proof checker or CNF was run or stored. This is not a mathematical completeness "
                  "claim and not a PA(19,8,6) acceptance: the target remains UNKNOWN."),
        "result_summary": {
            "cases_expected": len(pin["cases"]), "cases_processed": len(rows), "cases_not_processed": missing_cases,
            "status_counts": st, "m1_binding_counts": m1b, "m2_binding_counts": m2b,
            "ms01_a3": {"expected": 31, "processed": len(ms01),
                        "stored_present_and_byte_equal": sum(1 for r in ms01 if r["m1_binding"] == "STORED_REPLAYED_BYTE_EQUAL")},
            "ms09_a3prime": {"expected": 43, "processed": len(ms09),
                             "stored_present_and_byte_equal": sum(1 for r in ms09 if r["m1_binding"] == "STORED_REPLAYED_BYTE_EQUAL"),
                             "stored_absent_at_read": [r["tag"] for r in ms09 if r["m1_stored_read"]["status"] != "read"]},
            "m2": {"expected": 74, "stored_present_and_byte_equal_after_source_path":
                   sum(1 for r in rows if r["m2_binding"] == "STORED_REPLAYED_BYTE_EQUAL_AFTER_SOURCE_PATH"),
                   "stored_absent_parent_generated_counts": sum(1 for r in rows if r["m2_binding"].startswith("STORED_ABSENT"))},
            "all_cases_all_checks_true": not mismatches and not missing_cases,
            "m1_m2_raw_and_orbit_counts_equal_all": all(
                r["counts"]["m1_raw"] == r["counts"]["m2_raw"] == r["counts"]["indep_X"] and
                r["counts"]["m1_num_full"] == r["counts"]["m2_num"] == r["counts"]["indep_orbits"] for r in rows),
            "late_events": len(late),
            "b_indices_distinct_per_multiset": all(
                len({c["b_index"] for c in pin["cases"] if c["multiset"] == m}) ==
                sum(1 for c in pin["cases"] if c["multiset"] == m) for m in (1, 9)),
            "a_to_b_isomorphism_explicit_all": all(r["isomorphisms_a_to_b"] > 0 for r in rows),
        },
        "pin": {"file": "pin-v1.json", "sha256": fsha(os.path.join(OUT, "pin-v1.json")), "recorded_at": pin["recorded_at"],
                "summary": pin["summary"], "parent_pin": pin["parent_pin"], "networkx": pin["networkx"],
                "python": pin["python"], "venv_python": pin["venv_python"],
                "sources_used": {f: pin["sources"][f] for f in SRC_USED},
                "src_delta_file": pin["src_delta_file"],
                "m2_jobs_equal_a_to_b_of_hard_tags": pin["m2_jobs_equal_a_to_b_of_hard_tags"],
                "compare_map_flags": pin["compare_map_flags"]},
        "code_sha256": code,
        "commands": {
            "pin": "%s -B code/r6_pin.py pin-v1.json" % VENV_PY,
            "replay": "%s -B code/r6_replay.py <run_id> <max_wall_s>  (runs: %s)" % (VENV_PY, [x["run_id"] for x in runs]),
            "mutations": "%s -B code/r6_mutations.py mutation-controls-v1.json" % VENV_PY,
            "aggregate": "%s -B code/r6_aggregate.py %s %s" % (VENV_PY, name, mut_name or ""),
            "m1_ms01_regen": "/usr/bin/nice -n 10 %s -B %s/src/extend_p1.py %s/cases19skel/specs/<tag>.json /dev/fd/<pipe>" % (VENV_PY, S, S),
            "m1_ms09_regen": "/usr/bin/nice -n 10 %s -B %s/src/extend_p1q.py %s/cases19skel/specs/<tag>.json /dev/fd/<pipe> 1" % (VENV_PY, S, S),
            "m2_regen": "/usr/bin/nice -n 10 %s -B %s/src/extend_b.py %s/cycle2/skel-b/skeletons-b-msXX.json <b> /dev/fd/<pipe>" % (VENV_PY, S, S),
            "production_calls_replayed": PROD_CALLS,
            "regenerated_output_handling": ("written by the child to an anonymous pipe, hashed and parsed in memory by the "
                                            "driver, then discarded; M2 bytes compared after replacing the `source` field "
                                            "(S path) by the production path string, after checking that json.dumps "
                                            "re-serialization of the regenerated object is byte-exact"),
        },
        "cases": rows,
        "mismatches": mismatches,
        "incremental_binding": {
            "m1_lists_absent_at_read": incremental_m1,
            "m2_lists_absent_at_read": incremental_m2,
            "rule": ("a later production list binds to this replay iff its SHA-256 equals the predicted SHA "
                     "(M1: exact regenerated bytes; M2: regenerated bytes with the production source path)"),
        },
        "late_events": late,
        "runs": [{k: x[k] for k in ("run_id", "started", "ended", "stop_requested", "free_bytes")} |
                 {"processed": len(x["processed"])} for x in runs],
        "worker_check_copies": wcc,
        "mutation_controls": mut,
        "independence_and_limits": [
            "Byte replays rerun the lane's own enumerator code (pinned S copies, equal to live L at every case); they show "
            "determinism and binding of each stored list to its pinned spec/skeleton and code, not correctness.",
            "The independent semantics (code/r6_indep.py) is parent-written, stdlib only, and shares no code with "
            "extend_p1/extend_p1q/extend_b; it does not import networkx or nauty. It restates the same placement conditions "
            "(block sizes 4/4/2, no common P0 quad inside a block, row budget with `left` free P1 columns) from the lane "
            "README A3; those formulas are therefore shared with all three enumerators and were re-derived by hand, not "
            "machine-checked.",
            "Orbit counts: extend_p1/extend_p1q use networkx weisfeiler_lehman_graph_hash + is_isomorphic (imported, "
            "networkx %s pinned by tree digest); extend_b uses canonical minima over a brute-force automorphism group; "
            "r6_indep uses union-find over generators of a brute-force automorphism group and Burnside's lemma. All three "
            "agree on every processed case." % pin["networkx"]["version"],
            "The count-vector reduction (rows with equal P0 set are interchangeable) is shared by extend_b and r6_indep. "
            "It is checked without that reduction by row-level labeled enumeration: full labeled orbit counts (union-find "
            "over row generators) for all 31 ms01 cases; for ms09 only the labeled count equals the multinomial weight sum "
            "of the count vectors (labeled sets are 1e7+), which with realizability forces the count-vector set but does "
            "not by itself recount ms09 orbits at row level.",
            "The A->B map (compare-map a_to_b, made with networkx in compare_skel.py) is validated per case by explicit "
            "P0-column isomorphisms found by brute force over c0! permutations; transported count-vector sets equal the M2 "
            "sets and every M1 list maps bijectively onto the M2 orbits.",
            "The interpreter used by the production M2 runner is not recorded by the lane; extend_b is stdlib-only and "
            "the stored M2 lists that exist are byte-identical to the venv-python regeneration after the source-path "
            "substitution.",
            "Placement completeness is relative to the stated necessary conditions and to the skeleton list (R3/R4); "
            "it says nothing about the solved status of any subcase.",
        ],
    }
    with open(os.path.join(OUT, name), "x") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res["result_summary"], indent=1))
    print("mismatches", len(mismatches), "late_events", len(late))


if __name__ == "__main__":
    main()
