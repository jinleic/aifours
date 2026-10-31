#!/usr/bin/env python3
"""All column/transversal difference constraints on reference-row phases.

Variables s[t,i,j] are for ordered distinct zeros i,j and t not in {i,j}.
This finite-field check supports but does not replace the general abelian-
group gauge proof; no physical array or phase samples are generated.
"""
from itertools import combinations
from pathlib import Path

n=10
keys=[(t,i,j) for i in range(n) for j in range(n) if j!=i
      for t in range(n) if t not in (i,j)]
index={key:k for k,key in enumerate(keys)}
assert len(keys)==720
rows=[]
for i in range(n):
    for j,k in combinations([a for a in range(n) if a!=i],2):
        coords=[t for t in range(n) if t not in (i,j,k)]
        base=coords[0]
        for t in coords[1:]:
            rows.append([(index[t,i,j],1),(index[t,i,k],-1),
                         (index[base,i,j],-1),(index[base,i,k],1)])
colrows=len(rows)
for j in range(n):
    for i,k in combinations([a for a in range(n) if a!=j],2):
        coords=[t for t in range(n) if t not in (i,j,k)]
        base=coords[0]
        for t in coords[1:]:
            rows.append([(index[t,i,j],1),(index[t,k,j],-1),
                         (index[base,i,j],-1),(index[base,k,j],1)])
assert colrows==2160 and len(rows)==4320
out=Path(__file__).resolve().parent/'frontier-20261028-phase-gauge-constraints-v1.txt'
with out.open('w') as f:
    f.write(f'{len(rows)} {len(keys)}\n')
    for row in rows:
        f.write(str(len(row))+''.join(f' {i} {v}' for i,v in row)+'\n')
print('variables',len(keys),'column rows',colrows,'transversal rows',len(rows)-colrows,'output',out.name)
print('predicted gauge kernel dimension = 10 coordinate + 90 cell - 1 global = 99')
