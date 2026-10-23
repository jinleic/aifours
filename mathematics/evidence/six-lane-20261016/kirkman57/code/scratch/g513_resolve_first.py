import sys, time, json
sys.path.insert(0, '.')
from km_model import KMModel
from resolve import resolve_symmetric, check_resolution
from g513_groups import *
M = KMModel(N, G_GENS, [P27, F57, F57, F57P, F57P], names=["S0","B1","B2","B3","B4"])
sol = json.load(open("scratch/g513_km_sat_solution.json"))["rows"]
bs = M.base_blocks(sol)
syms = [(nu, [1,9,9,9]), (mu, [1]+[3]*9), (mu, [1]+[3]*9), (mup, [1]+[3]*9), (mup, [1]+[3]*9)]
for j, (S, (r, sizes)) in enumerate(zip(bs, syms)):
    blocks = [tuple(int(x) for x in M.trip[t]) for t in S]
    info, classes = resolve_symmetric(blocks, N, r, sizes, f"scratch/g513_res_{j}.cnf", timeout=120)
    print(M.names[j], info)
    if classes:
        check_resolution(blocks, N, classes)
        print("  resolution verified")
