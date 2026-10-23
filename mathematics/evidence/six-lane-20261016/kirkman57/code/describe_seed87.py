"""Orbit description of the pinned G903 LKTS(87) seed (exposition only; verifies reps)."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lkts_core import closure
from g87_groups import *
seed = json.load(open(sys.argv[1]))
def pt(p): return "∞" if p == INF else f"({p%43},{p//43})"
def img(g,b): return tuple(sorted(g[p] for p in b))
Ks = [closure([m21],N), closure([tau],N), closure([tau],N)]
out={"bases":[]}; md=[]
for base, K in zip(seed["bases"], Ks):
    classes=[[tuple(b) for b in C] for C in base["classes"]]
    blocks=sorted({b for C in classes for b in C})
    seen=set(); reps=[]
    for b in blocks:
        if b in seen: continue
        o={img(g,b) for g in K}; seen|=o; reps.append((b,len(o)))
    assert seen==set(blocks)
    cset=[frozenset(C) for C in classes]; cseen=set(); creps=[]
    for C in cset:
        if C in cseen: continue
        o={frozenset(img(g,b) for b in C) for g in K}; cseen|=o; creps.append((sorted(C),len(o)))
    assert cseen==set(cset)
    out["bases"].append({"name":base["name"],"K_order":len(K),"block_orbit_reps":[{"rep":list(b),"orbit":s} for b,s in reps],
                         "class_orbit_reps":[{"rep":[list(b) for b in C],"orbit":s} for C,s in creps]})
    md.append(f"### {base['name']}: |K|={len(K)}, {len(reps)} block orbits (sizes {dict(collections.Counter(s for _,s in reps))}); class orbits {[s for _,s in creps]}")
    md.append("Block orbit representatives ((x,j) means 43j+x): " + "; ".join("{"+",".join(pt(p) for p in b)+"}" for b,_ in reps))
json.dump(out, open(sys.argv[2],"w"), indent=1)
open(sys.argv[3],"w").write("\n\n".join(md)+"\n")
print("\n".join(m[:400] for m in md))
