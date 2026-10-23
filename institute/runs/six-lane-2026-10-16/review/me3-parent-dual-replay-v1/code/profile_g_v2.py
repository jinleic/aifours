#!/usr/bin/env python3
"""profile_g_v2.py -- PROFILE ONLY (not the certificate run): dualcheck_v2's G evaluator on every leaf of a spread of
G cells (every STEP-th cell plus the r13 diagnostic cells), with the production certify() (extra depth 12).
Reports per-cell leaf counts, direct/subdivided/unproved counts, method histogram and seconds per leaf, to size the
sharded full run.  Writes OUT (exclusive).  Usage: python -I -B profile_g_v2.py PIN.json OUT.json STEP
"""
import sys
import os
import json
import gzip
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dualcheck_v2 as D  # noqa: E402
from flint import fmpq  # noqa: E402

PIN, OUT, STEP = sys.argv[1], sys.argv[2], int(sys.argv[3])
pin = json.load(open(PIN))
ent = pin["charts"]["G"]
sh, _ = D.sha256_file(ent["leaves"]["path"])
assert sh == ent["leaves"]["sha256"], "G leaf hash mismatch"
spec = json.load(open(ent["spec"]["path"]))
kind, cells, wts, maxdepth, problems = D.load_chart(spec, "G")
C = D.Ctx(fmpq(11, 50))
sel = set(range(0, len(cells), STEP)) | {178, 228, 282, 300}
per = {}
fails = []
t_all = time.time()
with gzip.open(ent["leaves"]["path"], "rt") as fh:
    cur, dims, t0 = None, None, None
    for ln in fh:
        ci_s, path, tag = ln.split()
        ci = int(ci_s)
        if ci not in sel:
            continue
        if ci != cur:
            if cur is not None:
                per[cur]["seconds"] = round(time.time() - t0, 3)
            cur, t0 = ci, time.time()
            dims = D.split_dims(cells[ci], wts, maxdepth + 13)
            per[ci] = {"leaves": 0, "skip_ok": 0, "direct": 0, "subdivided": 0, "subleaves": 0, "unproved": 0,
                       "methods": {}, "cell": [[str(a), str(b)] for a, b in cells[ci]]}
        p = "" if path == "-" else path
        box = D.leaf_box(cells[ci], dims, p)
        e = per[ci]
        e["leaves"] += 1
        if tag.startswith("SKIP"):
            e["skip_ok"] += int(D.skip_G(box, tag))
            continue
        r = D.certify(D.ev_G, C, box, len(p), dims, 12)
        if r is None:
            e["unproved"] += 1
            if len(fails) < 50:
                fails.append([ci, path, tag])
            continue
        if r[0] == 1:
            e["direct"] += 1
        else:
            e["subdivided"] += 1
            e["subleaves"] += r[0]
        for k, v in r[1].items():
            e["methods"][k] = e["methods"].get(k, 0) + v
    if cur is not None:
        per[cur]["seconds"] = round(time.time() - t0, 3)
tot = {k: sum(v[k] for v in per.values()) for k in ("leaves", "skip_ok", "direct", "subdivided", "subleaves", "unproved", "seconds")}
res = {"tool": "profile_g_v2.py", "step": STEP, "cells_profiled": len(per), "totals": tot,
       "sec_per_leaf": (tot["seconds"] / tot["leaves"]) if tot["leaves"] else None, "per_cell": per,
       "unproved_first": fails, "wall_seconds": round(time.time() - t_all, 1)}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"cells": len(per), "totals": tot, "sec_per_leaf": res["sec_per_leaf"], "wall": res["wall_seconds"]}))
