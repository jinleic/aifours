import sys, time, json
sys.path.insert(0, '.')
from km2 import KM2
from lkts_core import closure
from resolve import resolve_symmetric, resolve_group, check_resolution
from g513_groups import *
bases = [(P27, []), (F57, [gamma(1,1)]), (F57, [gamma(2,1)]), (F57P, [gamma(1,-1)]), (F57P, [gamma(2,-1)])]
M = KM2(N, G_GENS, bases, names=["S0","B1","B2","B3","B4"])
sel = json.load(open("scratch/g513_km2_solution.json"))["rows"]
bs = M.bases_from(sel)
which = sys.argv[1:] or ["0","1","2","3","4"]
gens = {1:(mu, gamma(1,1)), 2:(mu, gamma(2,1)), 3:(mup, gamma(1,-1)), 4:(mup, gamma(2,-1))}
for js in which:
    j = int(js)
    blocks = [tuple(int(x) for x in M.trip[t]) for t in bs[j]]
    if j == 0:
        info, classes = resolve_symmetric(blocks, N, nu, [1,9,9,9], f"scratch/g513_km2_res_{j}.cnf", timeout=300)
    else:
        R = closure(list(gens[j]), N)
        ident = tuple(range(N))
        info, classes = resolve_group(blocks, N, R, [R, [ident], [ident], [ident]], f"scratch/g513_km2_res_{j}.cnf", timeout=300)
    print(M.names[j], info, flush=True)
    if classes:
        check_resolution(blocks, N, classes)
        json.dump(classes, open(f"scratch/g513_km2_classes_{j}.json","w"))
        print("  verified", flush=True)
