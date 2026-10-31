#!/usr/bin/env python3
"""Exact check of non-one-per-t and unique three-term half edge in q30 sample."""
import json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parent/'frontier-20261028-dita-q30-maximal-result-v1.json').read_text())
E=D['row_source_pairs'][::2];delta=D['delta_exponents']
assert len(E)==5
x=[sum(a==0 and t==j for a,t in E) for j in range(5)]
y=[sum(a==1 and t==j for a,t in E) for j in range(5)]
assert sum(x[t]!=y[t] for t in range(5))==3
# Phi_30 = X^8 + X^7 - X^5 - X^4 - X^3 + X + 1.
phi=[1,1,0,-1,-1,-1,0,1,1]
def zero(c):
    c=c[:]
    for k in range(len(c)-1,7,-1):
        v=c[k]
        for j in range(9):c[k-8+j]-=v*phi[j]
    return all(v==0 for v in c[:8])
good=[]
for d in range(5):
    c=[0]*30
    for t in range(5):c[(delta[t]+6*d*t)%30]+=x[t]-y[t]
    if zero(c):good.append(d)
assert good==[0]
print('E',E,'x-y',[x[t]-y[t] for t in range(5)])
print('PASS exactly three single t values, q30 cross-half zero shifts',good)
