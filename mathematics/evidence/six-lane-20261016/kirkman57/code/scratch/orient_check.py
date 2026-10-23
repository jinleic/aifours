import sys, json, collections
sys.path.insert(0,'.')
from km2 import KM2
from g513_groups import *
def orient(b):
    ls=[p//19 for p in b]; c=collections.Counter(ls)
    if len(c)!=2: return None
    two=[l for l,k in c.items() if k==2][0]; one=[l for l,k in c.items() if k==1][0]
    return '+' if one==(two+1)%3 else '-'
man = json.load(open("runs/bpool1/manifest.json"))
M = KM2(N, G_GENS, [(P27, []), (F57, [gamma(1,1)])], names=["S0","B"])
for mt in man["meta"]:
    blocks=[tuple(int(x) for x in M.trip[t]) for i in mt["rows"] for t in M.rows[i][1]]
    c=collections.Counter(orient(b) for b in blocks)
    Np=c['+']//3; Nm=c['-']//3
    print("gamma cand",mt["cand"],dict(c),"N+",Np,"N+ mod 9",Np%9,"plus-orbits(9)",c['+']/9)
man3=json.load(open("runs/exp3/manifest.json"))
M3 = KM2(N, G_GENS, [(P27, []), (F57, [])], names=["S0","B"])
for mt in man3["meta"]:
    blocks=[tuple(int(x) for x in M3.trip[t]) for i in mt["rows"] for t in M3.rows[i][1]]
    c=collections.Counter(orient(b) for b in blocks)
    print("plain cand",mt["cand"],dict(c))
