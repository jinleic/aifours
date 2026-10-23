import sys, time, json
sys.path.insert(0, '.')
from km_model import KMModel, exact_cover
from g513_groups import *
t0 = time.time()
M = KMModel(N, G_GENS, [P27, F57, F57, F57P, F57P], names=["S0","B1","B2","B3","B4"])
print(json.dumps(M.summary(), indent=1, default=str))
print("build s", round(time.time()-t0,2))
rows = [r[3] for r in M.rows]
t1 = time.time()
try:
    for sol in exact_cover(rows, M.cols, limit=1, time_limit=120):
        print("SOLUTION rows", len(sol), "time", round(time.time()-t1,2))
        bs = M.base_blocks(sol)
        print([len(b) for b in bs])
        json.dump({"rows": sol}, open("scratch/g513_first_solution.json","w"))
        break
    else:
        print("NO SOLUTION (exhausted)", round(time.time()-t1,2))
except TimeoutError:
    print("TIMEOUT", round(time.time()-t1,2))
