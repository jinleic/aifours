"""Experiment 3: plain F57 B-bases (no gamma) with exactly one AAA F57-orbit (u_B=3),
mu-invariant resolution [1]+[3]*9; 4 candidates x TIMEOUT s on 4 workers."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from pool import single_base_cnf, run_pool
from resolve import build
from satlib import solve
from g513_groups import *
out = sys.argv[1]; tmo = int(sys.argv[2]); ncand = int(sys.argv[3]); typ = sys.argv[4] if len(sys.argv) > 4 else "F57"
os.makedirs(out, exist_ok=True)
H, r = (F57, mu) if typ == "F57" else (F57P, mup)
M = KM2(N, G_GENS, [(P27, []), (H, [])], names=["S0", "B"])
cnf, rv = single_base_cnf(M, 1)
aaa = [rv[i] for i, (j, U, c) in enumerate(M.rows) if j == 1 and len({int(p)//19 for p in M.trip[U[0]]}) == 1]
cnf.exactly_one(aaa)
cands = []
for it in range(ncand):
    p = os.path.join(out, "single.cnf"); cnf.write(p)
    st, model, dt = solve(p, "kissat", timeout=120, seed=5 + it)
    if st != "SAT":
        print("single-base", st); break
    sel = sorted(i for i, v in rv.items() if v in model)
    cands.append(sel)
    cnf.add([-rv[i] for i in sel])
jobs, meta = [], []
for ci, sel in enumerate(cands):
    blocks = sorted(tuple(int(x) for x in M.trip[t]) for i in sel for t in M.rows[i][1])
    e = sum(1 for b in blocks if len({p // 19 for p in b}) == 1)
    c3, orbits, choice = build(blocks, N, r, [1] + [3] * 9)
    p = os.path.join(out, f"res_{ci}.cnf"); sha = c3.write(p)
    jobs.append({"cmd": ["kissat", "-q", f"--time={tmo}", f"--seed={ci}", p], "log": os.path.join(out, f"res_{ci}.log")})
    meta.append({"cand": ci, "rows": sel, "AAA_triples": e, "cnf_sha256": sha, "orbits": len(orbits)})
json.dump({"type": typ, "meta": meta}, open(os.path.join(out, "manifest.json"), "w"), indent=1)
res = run_pool(jobs, workers=4)
summ = []
for (job, rc, so, dt), mt in zip(res, meta):
    status = "SAT" if "s SATISFIABLE" in so else ("UNSAT" if "s UNSATISFIABLE" in so else "UNKNOWN")
    summ.append({"cand": mt["cand"], "AAA": mt["AAA_triples"], "status": status, "seconds": round(dt, 2)})
    print(mt["cand"], mt["AAA_triples"], status, round(dt, 2), flush=True)
json.dump(summ, open(os.path.join(out, "summary.json"), "w"), indent=1)
