from itertools import product
from random import Random
from collections import Counter
X=list(product(range(4),repeat=4));rng=Random(20261028)
def comp(f,g):return tuple(f[g[i]] for i in range(4))
def generated(seed,limit):
 S=set(seed);todo=list(S)
 while todo:
  x=todo.pop()
  for y in list(S):
   for z in (comp(x,y),comp(y,x)):
    if z not in S:
     S.add(z);todo.append(z)
     if len(S)>limit:return None
 return tuple(sorted(S))
def table(S):
 idx={x:i for i,x in enumerate(S)};return [[idx[comp(x,y)] for y in S] for x in S]
def contexts(T):
 n=len(T);ctx=[None]+list(range(n));lab={};out=[]
 for s in range(n):
  sig=[]
  for a,b in product(ctx,repeat=2):
   t=s if a is None else T[a][s]
   if b is not None:t=T[t][b]
   sig.append(T[t][t]==t)
  out.append(lab.setdefault(tuple(sig),len(lab)))
 return out
def quotient(T,c):
 reps=[c.index(i) for i in range(max(c)+1)];return [[c[T[i][j]] for j in reps] for i in reps]
def iscs(T):
 n=len(T);E=[e for e in range(n) if T[e][e]==e]
 for x in range(n):
  ideal={x}|{T[a][x] for a in range(n)}|{T[x][b] for b in range(n)}|{T[T[a][x]][b] for a,b in product(range(n),repeat=2)}
  if len(ideal)!=n:return False
 return bool(E) and all(e==f or T[e][f]!=e or T[f][e]!=e for e,f in product(E,repeat=2))
counts=Counter();seen=set();witness=None
for k in range(500):
 seed=rng.sample(X,3);S=generated(seed,40)
 if S is None:counts['over40_skipped']+=1;continue
 if S in seen:continue
 seen.add(S);counts['unique_under40']+=1;T=table(S);n=len(T)
 if not all(any(T[T[x][y]][x]==x for y in range(n)) for x in range(n)):continue
 counts['regular']+=1;E={x for x in range(n) if T[x][x]==x}
 if any(({T[e][s] for e in E}&{T[s][f] for f in E}&E) and s not in E for s in range(n)):continue
 counts['weakE']+=1
 if all(T[e][f] in E for e,f in product(E,repeat=2)):continue
 counts['nonorthogonal_weakE']+=1;q=contexts(T);D=quotient(T,q)
 if not iscs(D):witness=(seed,S,T,q,D);counts['weakE_q_not_cs']+=1;print('WITNESS',witness);break
print('RESULT',dict(counts),'seed=20261028; bounded sample, no universal inference')
