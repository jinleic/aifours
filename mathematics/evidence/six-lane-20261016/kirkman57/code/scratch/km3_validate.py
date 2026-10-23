import sys, time, json
sys.path.insert(0, '.')
from km3 import KM3
from km2 import KM2
from g87_groups import *
t0 = time.time()
M3 = KM3(N, G_GENS, [(Z21, []), (Z43, []), (Z43, [])], names=["S0", "B1", "B2"])
t1 = time.time()
M2 = KM2(N, G_GENS, [(Z21, []), (Z43, []), (Z43, [])], names=["S0", "B1", "B2"])
t2 = time.time()
print("km3", json.dumps(M3.summary()), round(t1 - t0, 1))
print("km2", json.dumps(M2.summary()), round(t2 - t1, 1))
# compare row sets as sets of block-sets per base
def rowsets(M, trip):
    return sorted((j, tuple(sorted(tuple(int(x) for x in trip[t]) for t in U))) for j, U, c in M.rows)
r3 = rowsets(M3, M3.trip); r2 = rowsets(M2, M2.trip)
print("identical row block-sets:", r3 == r2, len(r3), len(r2))
