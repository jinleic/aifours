#!/usr/bin/env python3
"""KM satisfiability probe for SQS(v) under Z_v ⋊ <multipliers>. Usage: km_probe.py v mults(comma) timeout seed outdir"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rdsqs_lib import SQSKM, kissat
v = int(sys.argv[1]); mults = [int(m) for m in sys.argv[2].split(",") if m and m != "none"]; tmo = int(sys.argv[3]); seed = int(sys.argv[4]); out = sys.argv[5]
os.makedirs(out, exist_ok=True)
gens = [tuple((x + 1) % v for x in range(v))] + [tuple((m * x) % v for x in range(v)) for m in mults]
t0 = time.time()
M = SQSKM(v, gens)
cnf, rv = M.cnf()
tag = f"v{v}_m{'-'.join(map(str, mults)) or 'none'}_s{seed}"
p = os.path.join(out, f"km_{tag}.cnf"); sha = cnf.write(p)
st, model, dt = kissat(p, tmo, seed=seed)
rec = {"v": v, "mult": mults, "seed": seed, **M.summary(), "cnf_sha256": sha, "status": st, "seconds": round(dt, 3)}
if st == "SAT":
    rec["rows"] = [j for j, x in enumerate(rv) if x in model]
json.dump(rec, open(os.path.join(out, f"{tag}.json"), "w"))
print(json.dumps({k: rec[k] for k in ("v", "mult", "triple_orbits", "valid_rows", "status", "seconds")}))
