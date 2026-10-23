#!/usr/bin/env python3
"""pin_inputs_v2.py -- bind one chart's exact worker inputs (generic version of pin_inputs_v1.py, for reruns).

Usage: python -I -B pin_inputs_v2.py M_ROOT CHART RUN CANDIDATE_PIN_REL EXPECTED_CANDIDATE_PIN_SHA OUT.json
Computes every hash here and cross-checks: post receipt binds leaves.txt.gz and dual.json and the pre receipt; the
pre-receipt argv names CHART and the spec; the candidate pin (given relative path and expected sha) binds the spec
and, if it lists them, the post receipt / leaves / dual / index; the index row for CHART (if the candidate pin binds an
index) names RUN and the same hashes.  Writes OUT (exclusive), in the same per-chart layout as inputs-pin-v1.json.
"""
import sys
import json
import hashlib
import os
import time

M, CHART, RUN, CAND_REL, CAND_SHA, OUT = sys.argv[1:7]


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
out = {"event": "ME3ParentDual input pin (generic v2)", "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "M": M,
       "charts": {}, "candidate_pin": {"path": P(CAND_REL)}}
cs_, _ = sha(P(CAND_REL))
out["candidate_pin"]["sha256"] = cs_
if cs_ != CAND_SHA:
    problems.append("candidate pin sha %s != expected" % cs_)
cand = json.load(open(P(CAND_REL)))
kf = cand.get("key_files", {})
post_rel, pre_rel = "receipts/%s-post.json" % RUN, "receipts/%s-pre.json" % RUN
post_sha, _ = sha(P(post_rel))
pre_sha, _ = sha(P(pre_rel))
post = json.load(open(P(post_rel)))
pre = json.load(open(P(pre_rel)))
argv = pre["argv"].split()
spec_rel = argv[1]
if argv[2] != CHART:
    problems.append("pre argv chart %s" % argv[2])
if post.get("pre_receipt_sha256") != pre_sha:
    problems.append("post does not bind pre")
if post.get("exit_code") != 0:
    problems.append("exit code %r" % post.get("exit_code"))
e = {"run": RUN, "argv": pre["argv"], "interpreter": pre.get("interpreter"),
     "interpreter_version": pre.get("interpreter_version"), "code_sha256_at_launch": pre.get("code_sha256"),
     "pre_receipt": {"path": P(pre_rel), "sha256": pre_sha}, "post_receipt": {"path": P(post_rel), "sha256": post_sha}}
s_, _ = sha(P(spec_rel))
e["spec"] = {"path": P(spec_rel), "sha256": s_}
if spec_rel in kf and kf[spec_rel] != s_:
    problems.append("candidate pin mismatch for spec %s" % spec_rel)
for key, fname in (("leaves", "leaves.txt.gz"), ("dual", "dual.json")):
    rel = "runs/%s/%s" % (RUN, fname)
    s_, n_ = sha(P(rel))
    e[key] = {"path": P(rel), "sha256": s_, "bytes": n_}
    rec = post["outputs_sha256"].get("./" + rel)
    if rec is None or rec["sha256"] != s_ or rec["bytes"] != n_:
        problems.append("post receipt does not bind %s" % rel)
    if rel in kf and kf[rel] != s_:
        problems.append("candidate pin mismatch for %s" % rel)
for rel, s_ in ((post_rel, post_sha), (pre_rel, pre_sha)):
    if rel in kf and kf[rel] != s_:
        problems.append("candidate pin mismatch for %s" % rel)
dual = json.load(open(e["dual"]["path"]))
e["claimed"] = {"counts": dual["counts"], "leaf_lines_sha256": dual["leaf_lines_sha256"],
                "certificate_ok": dual["certificate_ok"], "eval_cap_hit": dual["eval_cap_hit"], "cells": dual["cells"],
                "total_leaves": sum(dual["counts"].values())}
idx_rel = [k for k in kf if k.endswith("certificate_index.json")]
if idx_rel:
    isha, _ = sha(P(idx_rel[0]))
    out["index"] = {"path": P(idx_rel[0]), "sha256": isha, "pinned": kf[idx_rel[0]]}
    if isha != kf[idx_rel[0]]:
        problems.append("index sha mismatch")
    rows = {r["chart"]: r for r in json.load(open(P(idx_rel[0])))["rows"]}
    row = rows.get(CHART)
    if row is None:
        problems.append("no index row for %s" % CHART)
    else:
        chk = {"index_run": row["run"] == RUN, "index_spec": row["spec_sha256"] == e["spec"]["sha256"],
               "index_leaves": row["leaves_gz_sha256"] == e["leaves"]["sha256"],
               "index_post": row["post_receipt_sha256"] == post_sha, "index_pre": row["pre_receipt_sha256"] == pre_sha,
               "index_counts_eq_dual": row["counts"] == dual["counts"],
               "index_leaf_lines_eq_dual": row["leaf_lines_sha256"] == dual["leaf_lines_sha256"]}
        e["index_checks"] = chk
        problems.extend("%s false" % k for k, v in chk.items() if not v)
out["charts"][CHART] = e
out["problems"] = problems
out["ok"] = not problems
with open(OUT, "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"ok": out["ok"], "problems": problems, "claimed": e["claimed"]}))
