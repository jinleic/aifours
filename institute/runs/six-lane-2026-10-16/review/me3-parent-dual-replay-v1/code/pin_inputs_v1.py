#!/usr/bin/env python3
"""pin_inputs_v1.py -- bind the exact worker inputs of the six dual charts before any replay (read-only on M).

For each chart: run directory from the frozen certificate index, post- and pre-receipts, the spec named in the
pre-receipt argv, leaves.txt.gz and dual.json.  Every hash is computed here and cross-checked against the post
receipt, the pre receipt (via the post receipt's pre_receipt_sha256), the certificate index row and the candidate pin.
Writes OUT (exclusive create).  Usage: python -I -B pin_inputs_v1.py M_ROOT OUT.json
"""
import sys
import json
import hashlib
import os
import time

M = sys.argv[1]
OUT = sys.argv[2]
RUNS = {"LW": "d01-LW", "LD1": "d01-LD1", "LD2": "d01-LD2", "SWB": "d01-SWB", "G": "d01-G", "SWC": "d02-SWC"}
EXPECT_CANDIDATE_PIN = "8bd1b39e89b55b8dec394e5e3dfe2dddd1108913a4a972e39262731b9514a859"
EXPECT_INDEX = "edb78933bec26ac04ecfd5f5574eef8e33dcfaa65ecb4423811f7d28f0ba7b0e"


def sha(p):
    h = hashlib.sha256()
    n = 0
    with open(p, "rb") as fh:
        while True:
            b = fh.read(1 << 20)
            if not b:
                break
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def P(rel):
    return os.path.join(M, rel)


problems = []
out = {"event": "ME3ParentDual input pin v1", "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "M": M, "charts": {},
       "docs": {}}
cand_sha, _ = sha(P("receipts/me3-candidate-pin-v1.json"))
if cand_sha != EXPECT_CANDIDATE_PIN:
    problems.append("candidate pin sha %s" % cand_sha)
cand = json.load(open(P("receipts/me3-candidate-pin-v1.json")))
idx_sha, _ = sha(P("runs/i01-index/certificate_index.json"))
if idx_sha != EXPECT_INDEX:
    problems.append("index sha %s" % idx_sha)
if cand["key_files"].get("runs/i01-index/certificate_index.json") != idx_sha:
    problems.append("candidate pin does not bind index")
index = json.load(open(P("runs/i01-index/certificate_index.json")))
rows = {r["chart"]: r for r in index["rows"]}
for rel in ["proof/me3-theorem-v1.md", "proof/me3-theorem-v2.md", "proof/me3-theorem-v3.md", "proof/charts-spec-v1.md",
            "code/spec_dual_v1.json", "code/spec_dual_v2.json", "code/spec_primal_P_v1.json",
            "receipts/spec-dual-freeze-v1.json", "receipts/spec-dual-freeze-v2.json",
            "reductions/proof/reductions-v1.md", "reductions/proof/vcos-lower-bound-v1.md", "reductions/STATUS.md",
            "receipts/me3-candidate-pin-v1.json", "runs/p01-pin/manifest.json", "runs/i01-index/certificate_index.json"]:
    s_, n_ = sha(P(rel))
    out["docs"][rel] = {"sha256": s_, "bytes": n_, "candidate_pin_sha256": cand["key_files"].get(rel)}
    if rel in cand["key_files"] and cand["key_files"][rel] != s_:
        problems.append("candidate pin mismatch for %s" % rel)
for chart, run in RUNS.items():
    post_rel = "receipts/%s-post.json" % run
    pre_rel = "receipts/%s-pre.json" % run
    post_sha, _ = sha(P(post_rel))
    pre_sha, _ = sha(P(pre_rel))
    post = json.load(open(P(post_rel)))
    pre = json.load(open(P(pre_rel)))
    argv = pre["argv"].split()
    spec_rel = argv[1]
    if argv[2] != chart:
        problems.append("%s: pre argv chart %s" % (chart, argv[2]))
    if post.get("pre_receipt_sha256") != pre_sha:
        problems.append("%s: post does not bind pre" % chart)
    if post.get("exit_code") != 0:
        problems.append("%s: exit code %r" % (chart, post.get("exit_code")))
    e = {"run": run, "argv": pre["argv"], "interpreter": pre.get("interpreter"),
         "interpreter_version": pre.get("interpreter_version"),
         "pre_receipt": {"path": P(pre_rel), "sha256": pre_sha},
         "post_receipt": {"path": P(post_rel), "sha256": post_sha}}
    s_, n_ = sha(P(spec_rel))
    e["spec"] = {"path": P(spec_rel), "sha256": s_}
    for key, fname in (("leaves", "leaves.txt.gz"), ("dual", "dual.json")):
        rel = "runs/%s/%s" % (run, fname)
        s_, n_ = sha(P(rel))
        e[key] = {"path": P(rel), "sha256": s_, "bytes": n_}
        rec = post["outputs_sha256"].get("./" + rel)
        if rec is None or rec["sha256"] != s_ or rec["bytes"] != n_:
            problems.append("%s: post receipt does not bind %s" % (chart, rel))
    row = rows.get(chart)
    if row is None:
        problems.append("%s: no index row" % chart)
    else:
        chk = {"index_run": row["run"] == run, "index_spec": row["spec_sha256"] == e["spec"]["sha256"],
               "index_leaves": row["leaves_gz_sha256"] == e["leaves"]["sha256"],
               "index_post": row["post_receipt_sha256"] == post_sha,
               "index_pre": row["pre_receipt_sha256"] == pre_sha,
               "index_certificate_ok": row["certificate_ok"] is True}
        dual = json.load(open(e["dual"]["path"]))
        chk["index_counts_eq_dual"] = row["counts"] == dual["counts"]
        chk["index_leaf_lines_eq_dual"] = row["leaf_lines_sha256"] == dual["leaf_lines_sha256"]
        e["index_checks"] = chk
        e["claimed"] = {"counts": dual["counts"], "leaf_lines_sha256": dual["leaf_lines_sha256"],
                        "certificate_ok": dual["certificate_ok"], "eval_cap_hit": dual["eval_cap_hit"],
                        "cells": dual["cells"], "total_leaves": sum(dual["counts"].values())}
        for k_, v_ in chk.items():
            if not v_:
                problems.append("%s: %s false" % (chart, k_))
    out["charts"][chart] = e
out["problems"] = problems
out["ok"] = not problems
with open(OUT, "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"ok": out["ok"], "problems": problems,
                  "totals": {c: out["charts"][c].get("claimed", {}).get("total_leaves") for c in RUNS}}))
