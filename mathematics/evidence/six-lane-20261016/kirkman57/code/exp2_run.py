"""Experiment 2: calibrate resolution difficulty. Jobs (600 s each, 4 workers):
 a0,a1: B candidates 0,1 of runs/bpool1 with cyclic R=<mu>, classes [1]+[3]*9
 b0   : B candidate 0 with cyclic R=<gamma_1>, classes [1]+[3]*9
 s0   : S0 of the full KM2 (gamma) solution scratch/g513_km2_solution.json, R=<nu>, [1,9,9,9]
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from resolve import build
from pool import run_pool
from g513_groups import *
out = sys.argv[1]; tmo = int(sys.argv[2])
os.makedirs(out, exist_ok=True)
man = json.load(open("runs/bpool1/manifest.json"))
MB = KM2(N, G_GENS, [(P27, []), (F57, [gamma(1, 1)])], names=["S0", "B"])
def bblocks(ci):
    sel = man["meta"][ci]["rows"]
    return sorted(tuple(int(x) for x in MB.trip[t]) for i in sel for t in MB.rows[i][1])
M5 = KM2(N, G_GENS, [(P27, []), (F57, [gamma(1,1)]), (F57, [gamma(2,1)]), (F57P, [gamma(1,-1)]), (F57P, [gamma(2,-1)])])
sel5 = json.load(open("scratch/g513_km2_solution.json"))["rows"]
s0 = sorted(tuple(int(x) for x in M5.trip[t]) for t in M5.bases_from(sel5)[0])
specs = [("a0", bblocks(0), mu, [1]+[3]*9), ("a1", bblocks(1), mu, [1]+[3]*9),
         ("b0", bblocks(0), gamma(1,1), [1]+[3]*9), ("s0", s0, nu, [1,9,9,9])]
jobs, meta = [], []
for tag, blocks, r, sizes in specs:
    cnf, orbits, choice = build(blocks, N, r, sizes)
    p = os.path.join(out, f"{tag}.cnf"); sha = cnf.write(p)
    jobs.append({"cmd": ["kissat", "-q", f"--time={tmo}", "--seed=3", p], "log": os.path.join(out, f"{tag}.log")})
    meta.append({"tag": tag, "cnf_sha256": sha, "vars": cnf.nv, "clauses": len(cnf.clauses), "orbits": len(orbits)})
json.dump(meta, open(os.path.join(out, "manifest.json"), "w"), indent=1)
res = run_pool(jobs, workers=4)
summ = []
for (job, rc, so, dt), mt in zip(res, meta):
    status = "SAT" if "s SATISFIABLE" in so else ("UNSAT" if "s UNSATISFIABLE" in so else "UNKNOWN")
    summ.append(dict(mt, status=status, seconds=round(dt, 2)))
    print(mt["tag"], status, round(dt, 2), mt["orbits"], flush=True)
json.dump(summ, open(os.path.join(out, "summary.json"), "w"), indent=1)
