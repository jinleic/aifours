"""Experiment 4: gamma-B candidates with orientation-feasible class structures.
 struct g61 = [R] + [<gamma>]*6 + [1]   (C0 + 6 gamma-stabilized 3-orbits + 1 regular 9-orbit)
 struct g32 = [R] + [<gamma>]*3 + [1]*2"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from lkts_core import closure
from resolve import build_group
from pool import run_pool
from g513_groups import *
out = sys.argv[1]; tmo = int(sys.argv[2])
os.makedirs(out, exist_ok=True)
man = json.load(open("runs/bpool1/manifest.json"))
M = KM2(N, G_GENS, [(P27, []), (F57, [gamma(1, 1)])], names=["S0", "B"])
R = closure([mu, gamma(1, 1)], N)
gsub = closure([gamma(1, 1)], N)
ident = [tuple(range(N))]
structs = {"g61": [R] + [gsub] * 6 + [ident], "g32": [R] + [gsub] * 3 + [ident] * 2}
specs = [(1, "g61"), (3, "g61"), (1, "g32"), (3, "g32")]
jobs, meta = [], []
for ci, st in specs:
    sel = man["meta"][ci]["rows"]
    blocks = sorted(tuple(int(x) for x in M.trip[t]) for i in sel for t in M.rows[i][1])
    cnf, orbits, choice, cosets, stb = build_group(blocks, N, R, structs[st])
    p = os.path.join(out, f"c{ci}_{st}.cnf"); sha = cnf.write(p)
    jobs.append({"cmd": ["kissat", "-q", f"--time={tmo}", "--seed=7", p], "log": os.path.join(out, f"c{ci}_{st}.log")})
    meta.append({"cand": ci, "struct": st, "cnf_sha256": sha, "vars": cnf.nv, "clauses": len(cnf.clauses), "orbits": len(orbits)})
json.dump(meta, open(os.path.join(out, "manifest.json"), "w"), indent=1)
res = run_pool(jobs, workers=4)
summ = []
for (job, rc, so, dt), mt in zip(res, meta):
    status = "SAT" if "s SATISFIABLE" in so else ("UNSAT" if "s UNSATISFIABLE" in so else "UNKNOWN")
    summ.append(dict(mt, status=status, seconds=round(dt, 2)))
    print(mt["cand"], mt["struct"], status, round(dt, 2), flush=True)
json.dump(summ, open(os.path.join(out, "summary.json"), "w"), indent=1)
