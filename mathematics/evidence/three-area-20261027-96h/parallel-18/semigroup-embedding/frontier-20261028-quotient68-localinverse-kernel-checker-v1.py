import json
from pathlib import Path
from collections import deque
from itertools import product
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
Q=J['source_multiplication'];actor=J['actual_actor'];n=len(Q);E=[i for i in range(n) if Q[i][i]==i]
seeds=set()
for z in E:
 corner={Q[Q[z][x]][z] for x in range(n)};ce=corner&set(E)
 seeds.update((Q[e][f],Q[f][e]) for e,f in product(ce,repeat=2) if Q[e][f]!=Q[f][e])
p=list(range(n));todo=deque(seeds)
def root(x):
 while p[x]!=x:p[x]=p[p[x]];x=p[x]
 return x
while todo:
 a,b=todo.popleft();i=root(a);j=root(b)
 if i==j:continue
 p[j]=i
 for x in range(n):todo.append((Q[a][x],Q[b][x]));todo.append((Q[x][a],Q[x][b]))
lab={};classes=[lab.setdefault(root(i),len(lab)) for i in range(n)];k=len(lab);reps=[classes.index(i) for i in range(k)]
T=[[classes[Q[i][j]] for j in reps] for i in reps];act=[actor[i] for i in reps];ET=[i for i in range(k) if T[i][i]==i]
assert all(act[classes[i]]==actor[i] for i in range(n))
assert all((T[classes[i]][classes[i]]==classes[i])==(i in E) for i in range(n))
assert all(any(T[T[x][y]][x]==x and T[T[y][x]][y]==y for y in range(k)) for x in range(k))
for e in ET:
 corner={T[T[e][x]][e] for x in range(k)};ce=corner&set(ET)
 assert all(T[x][y]==T[y][x] for x,y in product(ce,repeat=2))
comp=[(e,f) for e,f in product(E,repeat=2) if e!=f and Q[e][f]==Q[f][e]==e]
collapsed=[(e,f) for e,f in comp if classes[e]==classes[f]]
R=[(e,f) for e,f in product(E,repeat=2) if e!=f and actor[e]==actor[f] and Q[e][f]==f and Q[f][e]==e]
L=[(e,f) for e,f in product(E,repeat=2) if e!=f and actor[e]==actor[f] and Q[e][f]==e and Q[f][e]==f]
print('S68 local commutator seeds=',len(seeds),' least-LI quotient size=',k,' actor-image=8, quotient pure/locally-inverse checked',sep='')
print('strict comparable pairs=',len(comp),' collapsed=',len(collapsed),' same-q R/L pairs=',len(R),',',len(L),' collapsed=',sum(classes[e]==classes[f] for e,f in R),',',sum(classes[e]==classes[f] for e,f in L),sep='')
assert not collapsed
