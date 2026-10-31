#!/usr/bin/env python3
"""Bounded exact Z3 search for one circulant BH(10,10) Hadamard pair."""
from pathlib import Path
import json,time,z3
n=10;sol=z3.Solver();sol.set(timeout=30000,random_seed=23847)
x=[z3.Int(f'x_{i}') for i in range(n)]
sol.add(*[z3.And(v>=0,v<10) for v in x]);sol.add(x[0]==0,x[1]==0)

def add_zero(exponents):
    counts=[z3.Sum([z3.If(e%10==j,1,0) for e in exponents]) for j in range(10)]
    v=[counts[j]-counts[j+5] for j in range(5)]
    sol.add(v[0]==-v[1],v[0]==v[2],v[0]==-v[3],v[0]==v[4])
for k in range(1,6):
    dif=[x[t]-x[(t-k)%10] for t in range(10)]
    add_zero(dif)
    add_zero([dif[t]+k*t for t in range(10)])
# Circulant K columns character-related iff a shifted autocorrelation ratio
# is exactly one of ten Fourier characters. Forbid such pairs.
for k in range(1,10):
    for m in range(10):
        ref=(x[0]-x[-k])%10
        sol.add(z3.Or(*[((x[t]-x[(t-k)%10]-m*t)%10)!=ref for t in range(1,10)]))
start=time.monotonic();answer=sol.check();elapsed=time.monotonic()-start
rec={'verdict':str(answer),'elapsed':elapsed,'timeout_ms':30000,
     'reason_unknown':sol.reason_unknown() if answer==z3.unknown else None,
     'scope':'one circulant q10 phase ansatz; no generic no-go or proof certificate'}
if answer==z3.sat:
    model=sol.model();rec['sequence']=[model.eval(v).as_long() for v in x]
    rec['requires_independent_original_vector_check']=True
out=Path(__file__).resolve().parent/'frontier-20261028-circulant-bh10-pair-smt-result-v1.json'
out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print(json.dumps(rec,sort_keys=True),flush=True)
