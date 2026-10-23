"""R1 sweep: KM satisfiability of SQS(52) under Z52 ⋊ M for all subgroups M of U(52) (by generators)."""
import sys, json, itertools
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure
v=52
from math import gcd
U=[m for m in range(1,v) if gcd(m,v)==1]
mp=lambda m: tuple((m*x)%v for x in range(v))
subgroups={}
for a in U:
    for b in U:
        H=frozenset(g[1] for g in closure([mp(a),mp(b)],v))
        subgroups.setdefault(H,(a,b))
res=[]
for H,(a,b) in sorted(subgroups.items(), key=lambda kv: len(kv[0])):
    if len(H)==1: continue
    gens=[tuple((x+1)%v for x in range(v)), mp(a), mp(b)]
    M=SQSKM(v,gens)
    cnf,rv=M.cnf(); p='runs/e0_km52/sweep.cnf'; cnf.write(p)
    st,model,dt=kissat(p,60,seed=0)
    res.append({"M":sorted(H),"order":len(H),"gens":[a,b],"rows":len(M.rows),"status":st,"seconds":round(dt,3)})
    print(len(H), sorted(H), st, round(dt,3), flush=True)
json.dump(res, open('runs/e0_km52/mult_sweep.json','w'), indent=1)
