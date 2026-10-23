"""Scan many local symmetries γ (R3γ) for KM satisfiability only. Usage: r3g_scan.py m seed0 count"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from itertools import combinations
from r3_pipeline import Field
from r3g_pipeline import make_gamma, Q, V, I0, I1
from rdsqs_lib import SQSKM, closure, comp, kissat, rank
m, s0, cnt = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
F = Field(Q); w = F.subgroup_gen(3)
lift = lambda f: tuple([f(x) for x in range(Q)] + [f(x) + Q for x in range(Q)] + [I0, I1])
trans = [lift(lambda x, b=b: F.add(x, b)) for b in F.addgens]
mult = lift(lambda x: F.mul(w, x))
swap = tuple([x + Q for x in range(Q)] + [x for x in range(Q)] + [I1, I0])
M = SQSKM(V, trans + [mult, swap])
rowidx = {lab: i for i, (lab, _) in enumerate(M.rows)}
trip = np.array(list(combinations(range(1, V), 3)), dtype=np.int64)
quads = np.concatenate([np.zeros((len(trip), 1), dtype=np.int64), trip], axis=1)
lab1 = M.LQ[rank(quads)]
os.makedirs("runs/r3g_scan", exist_ok=True)
res = []
for seed in range(s0, s0 + cnt):
    gamma, desc = make_gamma(F, w, seed, m)
    R = closure([mult, gamma], V)
    fix = sorted({sum(1 for p in range(1, V) if g[p] == p) for g in R if g != tuple(range(V))})
    lab2 = M.LQ[rank(np.asarray(gamma)[quads])]
    cnf, rv = M.cnf()
    for l1, l2 in zip(lab1.tolist(), lab2.tolist()):
        r1, r2 = rowidx.get(l1), rowidx.get(l2)
        if r1 == r2: continue
        if r1 is None: cnf.add([-rv[r2]])
        elif r2 is None: cnf.add([-rv[r1]])
        else: cnf.add([-rv[r1], rv[r2]]); cnf.add([rv[r1], -rv[r2]])
    p = f"runs/r3g_scan/km_m{m}.cnf"; cnf.write(p)
    st, model, dt = kissat(p, 60, seed=0)
    res.append({"seed": seed, "m": m, "fix": fix, "status": st, "seconds": round(dt, 3)})
    if st != "UNSAT": print(json.dumps(res[-1]), flush=True)
json.dump(res, open(f"runs/r3g_scan/scan_m{m}_{s0}_{cnt}.json", "w"))
import collections
print("m", m, collections.Counter(r["status"] for r in res))
