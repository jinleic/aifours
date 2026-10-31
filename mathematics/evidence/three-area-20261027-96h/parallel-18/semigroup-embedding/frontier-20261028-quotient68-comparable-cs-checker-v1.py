import json
from pathlib import Path
from itertools import product
from collections import deque
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];n=len(Q);E=[e for e in range(n) if Q[e][e]==e]
seeds=[(e,f) for e,f in product(E,repeat=2) if e!=f and Q[e][f]==Q[f][e]==e]
p=list(range(n));todo=deque(seeds);merges=0

def root(x):
 while p[x]!=x:p[x]=p[p[x]];x=p[x]
 return x
while todo:
 a,b=todo.popleft();i=root(a);j=root(b)
 if i==j:continue
 p[j]=i;merges+=1
 for x in range(n):todo.append((Q[a][x],Q[b][x]));todo.append((Q[x][a],Q[x][b]))
assert merges==56 and len(set(root(i) for i in range(n)))==12
assert all((root(i)==root(j))==(K['actor'][i]==K['actor'][j]) for i,j in product(range(n),repeat=2))
assert len(seeds)==52
print('PASS S68: 52 strict comparable-idempotent seeds generate 56 congruence merges and refined D12 kernel exactly')
print('LIMIT universality of comparable-generated congruence is the accompanying written proof')
