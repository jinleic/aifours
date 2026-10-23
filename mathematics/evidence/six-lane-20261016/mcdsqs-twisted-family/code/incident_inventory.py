#!/usr/bin/env python3
"""Read-only inventory for the 2026-10-17 CNF/mutation-file deletion incident (standard library).
For every pipeline run directory given, compares the files the old producer wrote (from its
summary.json) with the files present now; records sha256 from summary.json for files that are
gone and the current sha256 for files still present.  Writes nothing except OUT.json.
Usage: incident_inventory.py OUT.json RUNDIR [RUNDIR ...]"""
import hashlib
import json
import os
import sys


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    out, dirs = sys.argv[1], sys.argv[2:]
    report = []
    for d in dirs:
        s = json.load(open(os.path.join(d, "summary.json")))
        rec = {"run_dir": d, "samples_recorded": len(s["samples"]), "files": []}
        for r in s["samples"]:
            i = r["sample"]
            km = os.path.join(d, f"km_{i}.cnf")
            rec["files"].append({"file": km, "kind": "KM CNF", "recorded_sha256": r["km_cnf_sha256"],
                                 "present": os.path.exists(km),
                                 "present_sha256": sha(km) if os.path.exists(km) else None,
                                 "km_status": r["km_status"]})
            if "col_cnf_sha256" in r:
                col = os.path.join(d, f"col_{i}.cnf")
                rec["files"].append({"file": col, "kind": "colouring CNF", "recorded_sha256": r["col_cnf_sha256"],
                                     "present": os.path.exists(col),
                                     "present_sha256": sha(col) if os.path.exists(col) else None,
                                     "col_status": r.get("col_status", "not finished / not recorded")})
        rec["missing"] = [f["file"] for f in rec["files"] if not f["present"]]
        rec["present_sha_matches_record"] = all(f["present_sha256"] == f["recorded_sha256"]
                                                for f in rec["files"] if f["present"])
        report.append(rec)
    json.dump(report, open(out, "w"), indent=1)
    for rec in report:
        print(rec["run_dir"], "samples", rec["samples_recorded"], "files", len(rec["files"]),
              "missing", len(rec["missing"]), "present-match", rec["present_sha_matches_record"])


if __name__ == "__main__":
    main()
