"""Strict re-classification of the §8 root-cube WORKER records (Codex audit fix 1; README §8.2). Reads the old
RESULTS.jsonl files (never modified) and evaluates, per record, every condition of the strict conjunction from what was
recorded: solver exit 20, solver line "s UNSATISFIABLE", no cap stop, proof compression exit 0, proof decompression
exit 0, complete CNF feeds, checker exit 0, checker line "s VERIFIED" (\\r stripped; read from the recorded drat-trim
log) and no "s NOT VERIFIED". A condition is True/False/ABSENT; the strict verdict is CERTIFIED only if all are True,
otherwise UNKNOWN (reasons listed). Output: a new JSON file (exclusive create).
python -B k5_root_reclassify.py --results ../evidence/k5_split_v1/pilot/RESULTS.jsonl,../evidence/k5_split_v1/all/RESULTS.jsonl \\
       --out ../evidence/k5_split_v1/ROOT_RECLASSIFY_v1.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def classify(r, logdir):
    c = {}
    c["solver_exit_20"] = (r["solver_returncode"] == 20) if "solver_returncode" in r else "ABSENT"
    c["solver_line_unsat"] = (r["solver_status"] == "UNSAT") if "solver_status" in r else "ABSENT"
    c["not_stopped_by_cap"] = (r["stopped_by_cap"] is False) if "stopped_by_cap" in r else "ABSENT"
    c["compress_exit_0"] = (r["zstd_compress_returncode"] == 0) if "zstd_compress_returncode" in r else "ABSENT"
    c["decompress_exit_0"] = (r["zstd_decompress_returncode"] == 0) if "zstd_decompress_returncode" in r else "ABSENT"
    c["cnf_feeds_complete"] = (not r["feed_errors"]) if "feed_errors" in r else "ABSENT"
    c["checker_exit_0"] = (r["check_exit"] == 0) if r.get("check_exit") is not None else "ABSENT"
    log = os.path.join(logdir, "cube%03d.drat-trim.log" % r["cube"])
    if os.path.exists(log):
        lines = [l.replace("\r", "").strip() for l in open(log, errors="replace").read().split("\n")]
        c["checker_line_verified"] = "s VERIFIED" in lines
        c["no_not_verified"] = "s NOT VERIFIED" not in lines
    else:
        c["checker_line_verified"] = "ABSENT"
        c["no_not_verified"] = "ABSENT"
    bad = [k for k, v in c.items() if v is not True]
    return c, ("CERTIFIED" if not bad else "UNKNOWN"), bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = {"argv": sys.argv, "script_sha256": sha_bytes(open(__file__, "rb").read()), "inputs": {}, "records": []}
    for path in a.results.split(","):
        raw = open(path, "rb").read()
        out["inputs"][path] = sha_bytes(raw)
        for line in raw.split(b"\n"):
            if not line.strip():
                continue
            r = json.loads(line)
            c, verdict, bad = classify(r, os.path.dirname(path))
            out["records"].append({"file": path, "line_sha256": sha_bytes(line), "cube": r["cube"],
                                   "worker_verdict": "POSITIVE" if r.get("verified") else "NOT-POSITIVE",
                                   "worker_solver_status": r.get("solver_status"), "conditions": c,
                                   "strict_verdict": verdict, "failed_or_absent": bad})
    cubes = [x["cube"] for x in out["records"]]
    out["summary"] = {"records": len(cubes), "distinct_cubes": len(set(cubes)),
                      "duplicate_cubes": sorted({b for b in cubes if cubes.count(b) > 1}),
                      "missing_cubes": sorted(set(range(128)) - set(cubes)),
                      "strict_certified": sum(x["strict_verdict"] == "CERTIFIED" for x in out["records"]),
                      "worker_positive": sorted(x["cube"] for x in out["records"] if x["worker_verdict"] == "POSITIVE"),
                      "worker_not_positive": sorted(x["cube"] for x in out["records"]
                                                    if x["worker_verdict"] != "POSITIVE")}
    with open(a.out, "x") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out["summary"]))


if __name__ == "__main__":
    main()
