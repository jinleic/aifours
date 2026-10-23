"""Recompute, for the 8 runs/bpool1 candidates, the premises of Corollary 5a:
R=<mu,gamma_1> orbit sizes on blocks, which blocks lie in non-regular R-orbits,
layer types, and orientation of K-orbits.  Output JSON to argv[1]."""
import sys, os, json, collections, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from lkts_core import closure
from g513_groups import *
def orient(b):
    ls=[p//19 for p in b]; c=collections.Counter(ls)
    if len(c)==1: return "AAA"
    if len(c)==3: return "ABC"
    two=[l for l,k in c.items() if k==2][0]; one=[l for l,k in c.items() if k==1][0]
    return "+" if one==(two+1)%3 else "-"
man = json.load(open("runs/bpool1/manifest.json"))
M = KM2(N, G_GENS, [(P27, []), (F57, [gamma(1,1)])], names=["S0","B"])
R = closure([mu, gamma(1,1)], N); K = M.K[1]
gcyc = {tuple(sorted(((x)%19, ((x+1)%19)+19, ((x+1+7)%19)+38))) for x in range(19)}  # gamma_1-cycles
gcyc = set()
g = gamma(1,1)
for p in range(19):
    gcyc.add(tuple(sorted((p, g[p], g[g[p]]))))
out = []
for mt in man["meta"]:
    blocks = sorted(tuple(int(x) for x in M.trip[t]) for i in mt["rows"] for t in M.rows[i][1])
    bset = set(blocks); seen=set(); orbs=[]
    for b in blocks:
        if b in seen: continue
        o = {tuple(sorted(h[p] for p in b)) for h in R}; seen |= o; orbs.append(o)
    nonreg = set().union(*[o for o in orbs if len(o) < 9])
    kseen=set(); korb_orient=[]
    for b in blocks:
        if b in kseen or orient(b) not in "+-": continue
        o = {tuple(sorted(h[p] for p in b)) for h in K}; kseen |= o
        korb_orient.append((len(o), sorted({orient(x) for x in o})))
    out.append({"cand": mt["cand"], "blocks": len(blocks),
                "R_orbit_sizes": dict(collections.Counter(len(o) for o in orbs)),
                "nonregular_blocks_are_exactly_gamma_cycles": nonreg == gcyc and gcyc <= bset,
                "layer_types": dict(collections.Counter(orient(b) for b in blocks)),
                "K_orbits_of_two_layer_blocks": korb_orient,
                "positive_regular_R_orbits": sum(1 for o in orbs if len(o)==9 and orient(next(iter(o)))=="+")})
rec = {"R_order": len(R), "K_order": len(K), "candidates": out,
       "manifest_sha256": hashlib.sha256(open("runs/bpool1/manifest.json","rb").read()).hexdigest()}
json.dump(rec, open(sys.argv[1], "w"), indent=1)
for c in out: print(c["cand"], c["R_orbit_sizes"], c["nonregular_blocks_are_exactly_gamma_cycles"], c["layer_types"], c["positive_regular_R_orbits"], c["K_orbits_of_two_layer_blocks"])
