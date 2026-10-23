import sys, time, json
sys.path.insert(0, '.')
from km_model import KMModel, km_cnf
from satlib import solve
from g513_groups import *
M = KMModel(N, G_GENS, [P27, F57, F57, F57P, F57P], names=["S0","B1","B2","B3","B4"])
cnf, rv = km_cnf(M)
h = cnf.write("scratch/g513_km.cnf")
print("vars", cnf.nv, "clauses", len(cnf.clauses), "sha", h)
st, model, dt = solve("scratch/g513_km.cnf", "kissat", timeout=250, log="scratch/g513_km.kissat.log")
print(st, round(dt,2))
if st == "SAT":
    sol = [i for i, v in enumerate(rv) if v in model]
    json.dump({"rows": sol}, open("scratch/g513_km_sat_solution.json","w"))
    bs = M.base_blocks(sol)
    print([len(b) for b in bs])
