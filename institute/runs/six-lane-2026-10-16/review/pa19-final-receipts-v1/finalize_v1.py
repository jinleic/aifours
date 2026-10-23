#!/usr/bin/env python3
"""Assemble RESULT.json and the compact per-case manifest from run-v1 + controls-v1 (own outputs only; reads no lane
record). Also checks the drat-trim binary hash recorded by run-v1 against the parent's earlier tool-hash receipt.
Usage: finalize_v1.py   (writes RESULT.json, M1-manifest-compact.tsv with mode 'x')"""
import gzip
import hashlib
import json
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.dirname(HERE)


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    core = json.load(open(os.path.join(HERE, "run-v1", "RESULT-core.json")))
    ctl = json.load(open(os.path.join(HERE, "controls-v1.json")))
    rows = [json.loads(l) for l in open(os.path.join(HERE, "run-v1", "cases-A2.jsonl"))]
    th = open(os.path.join(REVIEW, "pa19-lratcheck-smoke-v1", "tool-hashes.txt")).read().split("\n")
    parent_dt = [l.split()[0] for l in th if l.strip().endswith("/tools/drat-trim/drat-trim")]
    now_dt = core["side_checks"]["drat_trim_binary"]["now"]
    with open(os.path.join(HERE, "M1-manifest-compact.tsv"), "x") as f:
        f.write("tag\tstate\troute\ttier\trev\tsolver\tchosen_path_or_dir\tchosen_record_sha256_or_ext_sha256\t"
                "num_full\trecords_chosen\tindex_map_digest\text_binding\tbase_cnf_sha256\tparent_snapshot_equal\n")
        for r in rows:
            c = r.get("chosen") or {}
            rt = c.get("route")
            if rt in ("a", "b", "c5"):
                f.write("\t".join(map(str, [r["tag"], r["state"], rt, c["tier"], c.get("rev"), c.get("solver"), c["path"],
                                            c["sha256"], "", "", "", "", r.get("base_cnf_sha256"),
                                            int(bool(c.get("parent_snapshot_hash_equal")))])) + "\n")
            elif rt in ("d", "e"):
                f.write("\t".join(map(str, [r["tag"], r["state"], rt, c["tier"], ",".join(sorted(c["chosen_tiers"])),
                                            "", c["dir"], c["ext"]["sha256"], c["num_full"], c["records_chosen"],
                                            c["index_map_digest"], c["ext"]["binding"], r.get("base_cnf_sha256"),
                                            "%d/%d" % (c["chosen_parent_snapshot_hash_equal"], c["records_chosen"])])) + "\n")
            elif rt == "cell":
                f.write("\t".join(map(str, [r["tag"], r["state"], rt, c["tier"], "13,14", "kissat", c["dir"],
                                            ",".join(x["sha256"] for x in c["records"]), 6, 6, "",
                                            "six-unit cover, unit CNFs recomputed by auditor", r.get("base_cnf_sha256"),
                                            "0/6"])) + "\n")
            else:
                f.write("\t".join(map(str, [r["tag"], r["state"], "", "", "", "", "", "", "", "", "", "", r.get("base_cnf_sha256"), ""])) + "\n")
    outs = {}
    for rel in ("run-v1/RESULT-core.json", "run-v1/cases-A2.jsonl", "run-v1/cases-E0.jsonl", "run-v1/split-index-map.jsonl.gz",
                "run-v1/consumed-manifest.tsv.gz", "controls-v1.json", "M1-manifest-compact.tsv", "m1_receipts_v1.py",
                "controls_v1.py", "token_ro.py", "census_v1.py", "census-v1.json", "finalize_v1.py"):
        p = os.path.join(HERE, rel)
        outs[rel] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
    res = {
        "title": "PA19FinalReceiptAudit RESULT v1: independent M1 receipt coverage (metadata only)",
        "recorded_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "disposition": core["reader_verdict"],
        "not_claimed": "No native proof replay, no encoder/cover soundness verdict, no parent acceptance, no PA(19,8,6) "
                       "nonexistence claim. M2 is NOT complete and out of scope (producer pin 5411/5577 at 01:25 is "
                       "historical; the ms09 b3 empty-list structural route is M2 and separate).",
        "pins_consumed": {"m1_complete_candidate": core["side_checks"]["candidate"],
                          "STATUS15_now_vs_task_pin": {k: core["side_checks"]["STATUS15"][k] for k in ("sha256", "pinned", "match")},
                          "parent_reference_receipts": core["parent_reference_pins"],
                          "lane_inputs": core["lane_input_pins"]},
        "counts": {"A2_cases": core["A2"]["cases"], "A2_COVERED": core["A2"]["COVERED"], "A2_UNKNOWN": core["A2"]["UNKNOWN"],
                   "A2_SAT_CLAIM": core["A2"]["SAT_CLAIM"], "A2_EMPTY_COVER_NOT_ACCEPTED": len(core["A2"]["EMPTY_COVER_NOT_ACCEPTED_cases"]),
                   "E0_graphs": core["E0"]["graphs"], "E0_COVERED": core["E0"]["COVERED"], "E0_SAT_CLAIM": core["E0"]["SAT_CLAIM"],
                   "A2_holes": core["A2"]["not_covered"], "E0_holes": core["E0"]["not_covered"]},
        "per_multiset": core["A2"]["per_multiset"],
        "chosen_tier_counts": core["A2"]["chosen_tier_counts"],
        "qualifying_route_sets": core["A2"]["qualifying_route_sets"],
        "binding_provenance": core["binding_provenance"],
        "bridge_census": core["bridge_census"],
        "sat_claims": {"consumed_records": core["sat_claims_in_consumed_records"], "archive": core["sat_claims_in_archive"]},
        "archive_rev10_records_never_counted": core["archive_rev10_records"],
        "orphan_or_unindexed_files": core["orphan_or_unindexed_files"],
        "point_in_time_inventory": core["drift"], "parent_snapshot_drift": core["parent_snapshot_drift"],
        "drat_trim_binary": {"now": now_dt, "parent_tool_hash_receipt": "review/pa19-lratcheck-smoke-v1/tool-hashes.txt",
                             "parent_recorded": parent_dt, "match": parent_dt == [now_dt],
                             "source_commit": core["side_checks"]["drat_trim_binary"]["source_commit"]},
        "side_checks": {k: v for k, v in core["side_checks"].items() if k not in ("drat_trim_binary",)},
        "controls": {"file": "controls-v1.json", "count": ctl["count"], "passed": ctl["passed"], "all_pass": ctl["all_pass"],
                     "started": ctl["started"], "finished": ctl["finished"], "reader_sha256": ctl["reader_sha256"],
                     "controls_sha256": ctl["controls_sha256"], "fixtures": ctl["fixtures"],
                     "results": [{k: c[k] for k in ("id", "what", "case", "route", "expected_state", "expected_reason_substring",
                                                    "observed_state", "observed_holes", "pass", "started", "ended")}
                                 for c in ctl["controls"]]},
        "run": {k: core[k] for k in ("started", "evaluated", "finished", "reader", "token", "consumed_files")},
        "outputs": outs,
    }
    with open(os.path.join(HERE, "RESULT.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({"disposition": res["disposition"], "controls": [ctl["count"], ctl["passed"]],
                      "drat_trim_match_parent": res["drat_trim_binary"]["match"], "result_sha256": sha(os.path.join(HERE, "RESULT.json"))}))


if __name__ == "__main__":
    main()
