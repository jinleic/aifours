#!/usr/bin/env python3
"""profile_g_v3.py -- PROFILE ONLY (not the certificate run): run a desk checker module's G evaluator (production
certify, extra depth 12) on the first K leaves of each listed G cell; report direct/subdivided/unproved counts,
sub-leaves and seconds per leaf.  Usage: python -I -B profile_g_v3.py PIN.json OUT.json MODULE K CELL [CELL ...]
MODULE is dualcheck_v2 or dualcheck_v3 (desk code).  Writes OUT (exclusive).
"""
import sys
import os
import json
import gzip
import time
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PIN, OUT, MOD, K = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
CELLS = [int(c) for c in sys.argv[5:]]
assert MOD in ("dualcheck_v2", "dualcheck_v3")
D = importlib.import_module(MOD)
from flint import fmpq  # noqa: E402

pin = json.load(open(PIN))
ent = pin["charts"]["G"]
assert D.sha256_file(ent["leaves"]["path"])[0] == ent["leaves"]["sha256"]
kind, cells, wts, maxdepth, problems = D.load_chart(json.load(open(ent["spec"]["path"])), "G")
C = D.Ctx(fmpq(11, 50))
want = {c: [] for c in CELLS}
with gzip.open(ent["leaves"]["path"], "rt") as fh:
    for ln in fh:
        c = int(ln.split(" ", 1)[0])
        if c in want and len(want[c]) < K:
            want[c].append(ln.split())
        if c > max(CELLS):
            break
per = {}
for c in CELLS:
    dims = D.split_dims(cells[c], wts, maxdepth + 13)
    e = {"leaves": 0, "direct": 0, "subdivided": 0, "subleaves": 0, "unproved": 0, "methods": {}}
    t0 = time.time()
    for ci, path, tag in want[c]:
        if not tag.startswith("CERT"):
            continue
        p = "" if path == "-" else path
        r = D.certify(D.ev_G, C, D.leaf_box(cells[c], dims, p), len(p), dims, 12)
        e["leaves"] += 1
        if r is None:
            e["unproved"] += 1
            continue
        if r[0] == 1:
            e["direct"] += 1
        else:
            e["subdivided"] += 1
            e["subleaves"] += r[0]
        for k_, v_ in r[1].items():
            e["methods"][k_] = e["methods"].get(k_, 0) + v_
    e["seconds"] = round(time.time() - t0, 3)
    e["ms_per_leaf"] = round(1000 * e["seconds"] / max(1, e["leaves"]), 3)
    per[c] = e
tot = {k: sum(v[k] for v in per.values()) for k in ("leaves", "direct", "subdivided", "subleaves", "unproved", "seconds")}
res = {"tool": "profile_g_v3.py", "module": MOD, "module_sha256": D.sha256_file(D.__file__)[0], "K": K,
       "per_cell": per, "totals": tot}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"module": MOD, "totals": tot,
                  "ms_per_leaf": round(1000 * tot["seconds"] / max(1, tot["leaves"]), 3)}))
