#!/usr/bin/env python3
"""pin_inputs_v3.py -- bind the exact worker inputs of several dual charts under a given candidate pin.

Generalises pin_inputs_v1.py (which hard-coded candidate pin v1 and run d02-SWC).  Usage:
  python -I -B pin_inputs_v3.py M_ROOT CANDIDATE_PIN_REL EXPECTED_SHA OUT.json CHART=RUN [CHART=RUN ...]
For each chart: hashes of post/pre receipts, the spec named in the pre-receipt argv, leaves.txt.gz and dual.json;
cross-checks: post binds leaves/dual/pre and exit 0; pre argv names the chart; the candidate pin binds the leaf file,
dual.json and spec (required) and the index it lists (required) has a row with the same run, spec, leaves, pre, post,
counts and leaf-line hash.  Optional --compare OLD_PIN.json reports whether each chart's leaves/dual/spec hashes are
byte-identical to an earlier desk pin.  Writes OUT (exclusive), layout as inputs-pin-v1.json.
"""
import sys
import json
import hashlib
import os
import time

args = sys.argv[1:]
compare = None
if "--compare" in args:
    i = args.index("--compare")
    compare = json.load(open(args[i + 1]))
    args = args[:i] + args[i + 2:]
M, CAND_REL, CAND_SHA, OUT = args[:4]
RUNS = dict(a.split("=", 1) for a in args[4:])


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
out = {"event": "ME3ParentDual input pin (v3 script)", "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "M": M,
       "candidate_pin": {"rel": CAND_REL}, "charts": {}}
cs_, _ = sha(P(CAND_REL))
out["candidate_pin"]["sha256"] = cs_
if cs_ != CAND_SHA:
    problems.append("candidate pin sha %s != expected %s" % (cs_, CAND_SHA))
cand = json.load(open(P(CAND_REL)))
kf = cand["key_files"]
idx_rel = [k for k in kf if k.endswith("certificate_index.json")]
if len(idx_rel) != 1:
    problems.append("candidate pin lists %d indexes" % len(idx_rel))
    rows = {}
else:
    isha, _ = sha(P(idx_rel[0]))
    out["index"] = {"rel": idx_rel[0], "sha256": isha, "pinned": kf[idx_rel[0]]}
    if isha != kf[idx_rel[0]]:
        problems.append("index sha mismatch")
    rows = {r["chart"]: r for r in json.load(open(P(idx_rel[0])))["rows"]}
for chart, run in RUNS.items():
    post_rel, pre_rel = "receipts/%s-post.json" % run, "receipts/%s-pre.json" % run
    post_sha, _ = sha(P(post_rel))
    pre_sha, _ = sha(P(pre_rel))
    post, pre = json.load(open(P(post_rel))), json.load(open(P(pre_rel)))
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
         "pre_receipt": {"path": P(pre_rel), "sha256": pre_sha}, "post_receipt": {"path": P(post_rel), "sha256": post_sha}}
    s_, _ = sha(P(spec_rel))
    e["spec"] = {"path": P(spec_rel), "sha256": s_, "candidate_pin_binds": kf.get(spec_rel) == s_}
    if kf.get(spec_rel) != s_:
        problems.append("%s: candidate pin does not bind spec %s" % (chart, spec_rel))
    for key, fname in (("leaves", "leaves.txt.gz"), ("dual", "dual.json")):
        rel = "runs/%s/%s" % (run, fname)
        s_, n_ = sha(P(rel))
        e[key] = {"path": P(rel), "sha256": s_, "bytes": n_, "candidate_pin_binds": kf.get(rel) == s_}
        rec = post["outputs_sha256"].get("./" + rel)
        if rec is None or rec["sha256"] != s_ or rec["bytes"] != n_:
            problems.append("%s: post receipt does not bind %s" % (chart, rel))
        if kf.get(rel) != s_:
            problems.append("%s: candidate pin does not bind %s" % (chart, rel))
    dual = json.load(open(e["dual"]["path"]))
    e["claimed"] = {"counts": dual["counts"], "leaf_lines_sha256": dual["leaf_lines_sha256"],
                    "certificate_ok": dual["certificate_ok"], "eval_cap_hit": dual["eval_cap_hit"], "cells": dual["cells"],
                    "total_leaves": sum(dual["counts"].values())}
    row = rows.get(chart)
    if row is None:
        problems.append("%s: no index row" % chart)
    else:
        chk = {"index_run": row["run"] == run, "index_spec": row["spec_sha256"] == e["spec"]["sha256"],
               "index_leaves": row["leaves_gz_sha256"] == e["leaves"]["sha256"],
               "index_post": row["post_receipt_sha256"] == post_sha, "index_pre": row["pre_receipt_sha256"] == pre_sha,
               "index_counts_eq_dual": row["counts"] == dual["counts"],
               "index_leaf_lines_eq_dual": row["leaf_lines_sha256"] == dual["leaf_lines_sha256"],
               "index_certificate_ok": row.get("certificate_ok") is True}
        e["index_checks"] = chk
        problems.extend("%s: %s false" % (chart, k) for k, v in chk.items() if not v)
    if compare is not None and chart in compare["charts"]:
        old = compare["charts"][chart]
        e["identical_to_compared_pin"] = {k: old[k]["sha256"] == e[k]["sha256"] for k in ("leaves", "dual", "spec")}
        e["compared_pin_run"] = old.get("run")
    out["charts"][chart] = e
out["problems"] = problems
out["ok"] = not problems
with open(OUT, "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"ok": out["ok"], "problems": problems,
                  "identical": {c: out["charts"][c].get("identical_to_compared_pin") for c in RUNS},
                  "totals": {c: out["charts"][c]["claimed"]["total_leaves"] for c in RUNS}}))
