import sys, time, json
sys.path.insert(0, '.')
from km2 import KM2
from satlib import solve
from g513_groups import *
t0=time.time()
bases = [(P27, []), (F57, [gamma(1,1)]), (F57, [gamma(2,1)]), (F57P, [gamma(1,-1)]), (F57P, [gamma(2,-1)])]
M = KM2(N, G_GENS, bases, names=["S0","B1","B2","B3","B4"])
print(json.dumps(M.summary()), round(time.time()-t0,2))
cnf, rv = M.cnf()
h = cnf.write("scratch/g513_km2.cnf")
st, model, dt = solve("scratch/g513_km2.cnf", "kissat", timeout=250)
print(st, round(dt,2), h)
if st == "SAT":
    sel = [i for i, v in enumerate(rv) if v in model]
    json.dump({"rows": sel}, open("scratch/g513_km2_solution.json","w"))
    bs = M.bases_from(sel)
    print([len(b) for b in bs])
