#!/usr/bin/env python3
"""assemble_g_v1.py -- assemble the G shard results of dualcheck_v2.py (--cells LO:HI) into one chart result.

No evaluation.  Accepts the chart iff:
  * every shard ran the same checker (tool sha), the same pin (pin sha), on the same pinned inputs (binding match,
    post receipt binds leaves and dual.json, exit 0), saw the full file (same line count and leaf-line sha, equal to
    dual.json's claim; claimed counts equal dual.json; leaf file unchanged after the run), with no spec problems,
    no tiling errors, no failures, verdict CHUNK-PASS or PASS;
  * the shards' evaluated cell ranges, sorted, tile [0, n_cells) exactly (no gap, no overlap);
  * the evaluated leaves sum to the line count, and per-outcome sums of the verification tables equal the claimed
    counts (every claimed leaf was evaluated exactly once).
Writes OUT (exclusive).  Usage: python -I -B assemble_g_v1.py OUT.json SHARD.json [SHARD.json ...]
"""
import sys
import json
import hashlib
import time

OUT, paths = sys.argv[1], sys.argv[2:]
sh = [json.load(open(p)) for p in paths]
problems = []


def same(key_fn, label):
    vals = {json.dumps(key_fn(s), sort_keys=True) for s in sh}
    if len(vals) != 1:
        problems.append("shards disagree on %s" % label)


same(lambda s: s["tool_sha256"], "tool sha")
same(lambda s: s["pin"]["sha256"], "pin sha")
same(lambda s: {k: s["binding"][k]["sha256"] for k in ("spec", "leaves", "dual", "post_receipt")}, "input hashes")
same(lambda s: s["lines"], "line count")
same(lambda s: s["leaf_lines_sha256"], "leaf-line sha")
same(lambda s: s["claimed_counts"], "claimed counts")
same(lambda s: s["cells"], "cell count")
same(lambda s: s["T"], "T")
for p, s in zip(paths, sh):
    b = s["binding"]
    if s["chart"] != "G":
        problems.append("%s: chart %s" % (p, s["chart"]))
    if not all(b[k]["match"] for k in ("spec", "leaves", "dual", "post_receipt")):
        problems.append("%s: input binding mismatch" % p)
    if not (b["post_receipt_binds_leaves"] and b["post_receipt_binds_dual"] and b["post_receipt_exit_code"] == 0):
        problems.append("%s: post receipt binding" % p)
    if s["spec_problems"] or s["tiling_errors"] or s["n_failures"] != 0:
        problems.append("%s: spec/tiling/failures %r %r %d" % (p, s["spec_problems"], s["tiling_errors"][:2], s["n_failures"]))
    if not (s["leaf_lines_match"] and s["claimed_counts_match_dual"] and s["leaves_rehash_after"]["unchanged"]):
        problems.append("%s: hash/count claim mismatch" % p)
    if s["verdict"] not in ("CHUNK-PASS", "PASS"):
        problems.append("%s: verdict %s" % (p, s["verdict"]))
ranges = sorted((s["evaluated_cells"][0], s["evaluated_cells"][1], p) for p, s in zip(paths, sh))
ncell = sh[0]["cells"]
pos = 0
for lo, hi, p in ranges:
    if lo != pos:
        problems.append("cell range gap/overlap at %d (shard %s starts at %d)" % (pos, p, lo))
    if not hi > lo:
        problems.append("empty or reversed range in %s" % p)
    pos = max(pos, hi)
if pos != ncell:
    problems.append("ranges end at %d != %d cells" % (pos, ncell))
evaluated = sum(s["evaluated_leaves"] for s in sh)
if evaluated != sh[0]["lines"]:
    problems.append("evaluated leaves %d != lines %d" % (evaluated, sh[0]["lines"]))
table, sub = {}, {"leaves": 0, "subleaves": 0, "max_extra_depth": 0, "methods": {}}
for s in sh:
    for k, v in s["verification_table"].items():
        table[k] = table.get(k, 0) + v
    sub["leaves"] += s["subdivision"]["leaves"]
    sub["subleaves"] += s["subdivision"]["subleaves"]
    sub["max_extra_depth"] = max(sub["max_extra_depth"], s["subdivision"]["max_extra_depth"])
    for k, v in s["subdivision"]["methods"].items():
        sub["methods"][k] = sub["methods"].get(k, 0) + v
per_outcome = {}
for k, v in table.items():
    oc = k.split(" -> ")[0]
    per_outcome[oc] = per_outcome.get(oc, 0) + v
if per_outcome != sh[0]["claimed_counts"]:
    problems.append("per-outcome evaluated counts %r != claimed %r" % (per_outcome, sh[0]["claimed_counts"]))
bad_keys = [k for k in table if k.endswith("UNPROVED") or k.endswith("INVALID-SKIP") or k.endswith("FAIL-LABEL")]
if bad_keys:
    problems.append("bad verification keys %r" % bad_keys)
res = {"event": "ME3ParentDual G shard assembly", "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
       "shards": [{"file": p, "sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(), "cells": s["evaluated_cells"],
                   "evaluated_leaves": s["evaluated_leaves"], "subdivision": s["subdivision"], "wall_seconds": s["wall_seconds"]}
                  for p, s in zip(paths, sh)],
       "inputs": {k: sh[0]["binding"][k]["sha256"] for k in ("spec", "leaves", "dual", "post_receipt")},
       "tool_sha256": sh[0]["tool_sha256"], "pin_sha256": sh[0]["pin"]["sha256"], "lines": sh[0]["lines"],
       "cells": ncell, "leaf_lines_sha256": sh[0]["leaf_lines_sha256"], "claimed_counts": sh[0]["claimed_counts"],
       "verification_table": table, "subdivision": sub, "evaluated_leaves": evaluated,
       "skip_rule_ok": sum(s["skip_rule_ok"] for s in sh), "max_depth_seen": max(s["max_depth_seen"] for s in sh),
       "problems": problems, "verdict": "PASS" if not problems else "FAIL"}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"verdict": res["verdict"], "problems": problems[:5], "evaluated": evaluated, "subdivision": sub}))
