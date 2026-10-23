import sys, json, collections, itertools
sys.path.insert(0,'.')
from km2 import KM2
from lkts_core import closure
from g513_groups import *
man = json.load(open("runs/bpool1/manifest.json"))
bases = [(P27, []), (F57, [gamma(1,1)])]
M = KM2(N, G_GENS, bases, names=["S0","B"])
R = closure([mu, gamma(1,1)], N)
# point orbits under R
porb = {}
for p in range(N):
    o = min(g[p] for g in R)
    porb.setdefault(o, set()).add(p)
orbs = sorted(porb.values(), key=lambda s:(len(s), min(s)))
print("point orbit sizes", [len(o) for o in orbs])
pid = {p:k for k,o in enumerate(orbs) for p in o}
for mt in man["meta"][:8]:
    sel = mt["rows"]
    blocks = sorted(tuple(int(x) for x in M.trip[t]) for i in sel for t in M.rows[i][1])
    bset=set(blocks)
    seen=set(); W=[]
    for b in blocks:
        if b in seen: continue
        orb={tuple(sorted(g[p] for p in b)) for g in R}
        seen|=orb; W.append((b,len(orb)))
    sizes=collections.Counter(s for _,s in W)
    # t-vectors of regular orbits
    tv=collections.Counter()
    for b,s in W:
        if s==9:
            v=[0]*len(orbs)
            for p in b: v[pid[p]]+=1
            tv[tuple(v)]+=1
    # layer types
    lay=collections.Counter()
    for b in blocks:
        ls=sorted(p//19 for p in b); lay[tuple(ls) if len(set(ls))<3 else 'ABC']+=0
    e=sum(1 for b in blocks if len({p//19 for p in b})==1)
    print("cand",mt["cand"],"orbit sizes",dict(sizes),"AAA",e, "distinct t-vectors",len(tv))
    print("   ", sorted(tv.items()))
