#!/usr/bin/env python3
"""summary_v1.py -- aggregate the desk's per-chart replay results into one record (no evaluation).

Usage: python -I -B summary_v1.py OUT.json CHART=RESULT.json [CHART=RESULT.json ...] [--controls CONTROLS.json]
A chart counts as PASS only if its result file says verdict PASS with scope_full_chart, zero failures, no tiling
errors, matching leaf-line and leaf-file hashes, and a post receipt that binds leaves and dual.json.  The aggregate
is PASS only if all six charts LW, LD1, LD2, G, SWB, SWC are PASS (a missing chart makes it INCOMPLETE) and the
controls (if given) all pass.  Writes OUT (exclusive).
"""
import sys
import json
import hashlib
import time

OUT = sys.argv[1]
args = sys.argv[2:]
controls = None
if "--controls" in args:
    i = args.index("--controls")
    controls = args[i + 1]
    args = args[:i] + args[i + 2:]
REQUIRED = ["LW", "LD1", "LD2", "G", "SWB", "SWC"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


charts = {}
for a in args:
    name, path = a.split("=", 1)
    r = json.load(open(path))
    b = r["binding"]
    ok = (r.get("verdict") == "PASS" and r.get("scope_full_chart") and r["n_failures"] == 0 and not r["tiling_errors"]
          and not r["spec_problems"] and r["leaf_lines_match"] and r["claimed_counts_match_dual"]
          and r["leaves_rehash_after"]["unchanged"] and b["post_receipt_binds_leaves"] and b["post_receipt_binds_dual"]
          and b["post_receipt_exit_code"] == 0 and r["chart"] == name)
    charts[name] = {
        "result_file": path, "result_sha256": sha(path), "verdict": r.get("verdict"), "accepted": bool(ok),
        "inputs": {k: {"path": b[k]["path"], "sha256": b[k]["sha256"], "bytes": b[k]["bytes"]}
                   for k in ("spec", "leaves", "dual", "post_receipt")},
        "leaf_lines_sha256": r["leaf_lines_sha256"], "lines": r["lines"], "cells": r["cells"],
        "max_depth_seen": r["max_depth_seen"], "claimed_counts": r["claimed_counts"],
        "verification_table": r["verification_table"], "skip_rule_ok": r["skip_rule_ok"],
        "subdivision": r["subdivision"], "n_failures": r["n_failures"], "tiling_errors": r["tiling_errors"][:5],
        "tool_sha256": r["tool_sha256"], "T": r["T"], "prec": r["prec"], "wall_seconds": r["wall_seconds"]}
missing = [c for c in REQUIRED if c not in charts]
ctl = None
if controls:
    cj = json.load(open(controls))
    ctl = {"file": controls, "sha256": sha(controls), "all_pass": cj["all_pass"], "not_applicable": cj["not_applicable"],
           "failed": [k for k, v in cj["controls"].items() if v["pass"] is False]}
all_ok = all(charts[c]["accepted"] for c in charts)
if missing:
    agg = "INCOMPLETE"
elif all_ok and (ctl is None or ctl["all_pass"]):
    agg = "PASS"
else:
    agg = "FAIL"
res = {"event": "ME3ParentDual aggregate", "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "charts": charts,
       "missing_charts": missing, "controls": ctl, "aggregate": agg,
       "rule": "aggregate PASS requires all six dual charts accepted (full replay) and all applicable controls passing"}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"aggregate": agg, "missing": missing, "accepted": {c: charts[c]["accepted"] for c in charts}}))
