"""Human-readable orbit description of the pinned G513 seed (exposition only).
For each base: block-orbit representatives under its required symmetry group K
(S0: P27; B_k: F57 or F57' with gamma), and class-orbit representatives of its
chosen resolution under R (S0: <nu>; B_k: <mu or mu', gamma>).  Verifies that the
representatives regenerate exactly the seed's block set and class set."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lkts_core import closure
from g513_groups import *
seed = json.load(open(sys.argv[1]))
def pt(p): return f"({p%19},{p//19})"
def img(g,b): return tuple(sorted(g[p] for p in b))
Ks = [closure(P27,N), closure(F57+[gamma(1,1)],N), closure(F57+[gamma(2,1)],N), closure(F57P+[gamma(1,-1)],N), closure(F57P+[gamma(2,-1)],N)]
Rs = [closure([nu],N), closure([mu,gamma(1,1)],N), closure([mu,gamma(2,1)],N), closure([mup,gamma(1,-1)],N), closure([mup,gamma(2,-1)],N)]
out = {"bases": []}; md = []
for base, K, R in zip(seed["bases"], Ks, Rs):
    classes = [[tuple(b) for b in C] for C in base["classes"]]
    blocks = sorted({b for C in classes for b in C})
    seen=set(); reps=[]
    for b in blocks:
        if b in seen: continue
        o={img(g,b) for g in K}; seen|=o; reps.append((b,len(o)))
    assert seen == set(blocks)
    cset=[frozenset(C) for C in classes]; cseen=set(); creps=[]
    for C in cset:
        if C in cseen: continue
        o={frozenset(img(g,b) for b in C) for g in R}; cseen|=o; creps.append((sorted(C),len(o)))
    assert cseen == set(cset)
    out["bases"].append({"name": base["name"], "K_order": len(K), "R_order": len(R),
        "block_orbit_reps": [{"rep": list(b), "orbit": s} for b,s in reps],
        "class_orbit_reps": [{"rep": [list(b) for b in C], "orbit": s} for C,s in creps]})
    md.append(f"### {base['name']}: |K|={len(K)}, {len(reps)} block orbits (sizes {dict(collections.Counter(s for _,s in reps))}); |R|={len(R)}, class orbits {[s for _,s in creps]}")
    md.append("Block orbit representatives ((x,i) means 19i+x): " + "; ".join("{"+",".join(pt(p) for p in b)+"}" for b,_ in reps))
json.dump(out, open(sys.argv[2],"w"), indent=1)
open(sys.argv[3],"w").write("\n\n".join(md)+"\n")
print("\n".join(m[:200] for m in md))
