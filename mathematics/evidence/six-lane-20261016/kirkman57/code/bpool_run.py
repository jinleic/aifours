"""Experiment: enumerate B-type candidates (F57 + gamma_c) and test symmetric
resolutions in a parallel pool.  Usage: bpool_run.py OUTDIR TYPE C NCAND TIMEOUT STRUCT
TYPE in {F57,F57P}; STRUCT in {r3 (fixed+3 regular), g31 (fixed + 3 <gamma>-orbits + 2 regular)}"""
import sys, json, time, hashlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from lkts_core import closure
from pool import single_base_candidates, run_pool
from resolve import build_group
from g513_groups import *

out, typ, c, ncand, tmo, struct = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
os.makedirs(out, exist_ok=True)
e = 1 if typ == "F57" else -1
H = F57 if e == 1 else F57P
m = mu if e == 1 else mup
g = gamma(c, e)
bases = [(P27, []), (H, [g])]
M = KM2(N, G_GENS, bases, names=["S0", "B"])
t0 = time.time()
cands, st = single_base_candidates(M, 1, ncand, os.path.join(out, "single.cnf"), timeout=120, seed=17)
print("candidates", len(cands), st, round(time.time() - t0, 2), flush=True)
R = closure([m, g], N)
ident = tuple(range(N))
gsub = closure([g], N)
if struct == "r3":
    stabs = [R, [ident], [ident], [ident]]
elif struct == "g31":
    stabs = [R, gsub, gsub, gsub, [ident], [ident]]
else:
    raise SystemExit("bad struct")
jobs = []
meta = []
for ci, sel in enumerate(cands):
    blocks = sorted(tuple(int(x) for x in M.trip[t]) for i in sel for t in M.rows[i][1])
    cnf, orbits, choice, cosets, stb = build_group(blocks, N, R, stabs)
    p = os.path.join(out, f"res_{ci}.cnf")
    sha = cnf.write(p)
    jobs.append({"cmd": ["kissat", "-q", f"--time={tmo}", f"--seed={ci}", p], "log": os.path.join(out, f"res_{ci}.log")})
    meta.append({"cand": ci, "rows": sel, "cnf": p, "cnf_sha256": sha, "vars": cnf.nv, "clauses": len(cnf.clauses),
                 "block_orbits": len(orbits)})
json.dump({"type": typ, "c": c, "struct": struct, "timeout": tmo, "meta": meta}, open(os.path.join(out, "manifest.json"), "w"), indent=1)
res = run_pool(jobs, workers=4)
summary = []
for (job, rc, so, dt), mt in zip(res, meta):
    status = "SAT" if "s SATISFIABLE" in so else ("UNSAT" if "s UNSATISFIABLE" in so else "UNKNOWN")
    summary.append({"cand": mt["cand"], "status": status, "seconds": round(dt, 2)})
    print(mt["cand"], status, round(dt, 2), flush=True)
json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1)
