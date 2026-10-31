import json
from pathlib import Path
from itertools import product
from collections import deque
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
Q=J['source_multiplication'];n=len(Q);E=[i for i in range(n) if Q[i][i]==i];p=list(range(n));seeds=set()
for z in E:
 ce={Q[Q[z][x]][z] for x in range(n)}&set(E)
 seeds.update((Q[Q[e][f]][e],Q[e][f]) for e,f in product(ce,repeat=2) if Q[Q[e][f]][e]!=Q[e][f])
todo=deque(seeds)
def root(x):
 while p[x]!=x:p[x]=p[p[x]];x=p[x]
 return x
while todo:
 a,b=todo.popleft();i=root(a);j=root(b)
 if i==j:continue
 p[j]=i
 for x in range(n):todo.append((Q[a][x],Q[b][x]));todo.append((Q[x][a],Q[x][b]))
lab={};c=[lab.setdefault(root(i),len(lab)) for i in range(n)];m=len(lab);reps=[c.index(i) for i in range(m)];T=[[c[Q[i][j]] for j in reps] for i in reps]
assert m==60 and all((Q[i][i]==i)==(T[c[i]][c[i]]==c[i]) for i in range(n))
RS=[frozenset([i]+Q[i]) for i in range(n)];LS=[frozenset([i]+[Q[j][i] for j in range(n)]) for i in range(n)]
LT=[frozenset([i]+[T[j][i] for j in range(m)]) for i in range(m)]
assert all(c[i]!=c[j] or RS[i]==RS[j] for i,j in product(range(n),repeat=2))
for e in E:
 source=[i for i in range(n) if LS[i]==LS[e]];target=[i for i in range(m) if LT[i]==LT[c[e]]]
 assert {c[i] for i in source}==set(target) and len(source)==len(target)
assert c[37]==c[61] and Q[37]!=Q[61]
leftdiff=[i for i in range(n) if Q[37][i]!=Q[61][i]]
assert leftdiff==list(range(24,32))+list(range(52,60))
print('PASS S68→T60 localLRB quotient is pure, kernel⊂R, all34 idempotent L-class restrictions bijective')
print('source distinct L-classes=',len(set(LS)),' target L-classes=',len(set(LT)),sep='')
print('CONTROL ordinary quotient action fails: π37=π61 but 16 left-translation disagreements')
