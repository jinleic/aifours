from itertools import product,combinations
from collections import Counter
X=list(product(range(3),repeat=3))
def compose(f,g):return tuple(f[g[i]] for i in range(3))
def generated(seed):
 S=set(seed);todo=list(S)
 while todo:
  x=todo.pop()
  for y in list(S):
   for z in (compose(x,y),compose(y,x)):
    if z not in S:S.add(z);todo.append(z)
 return tuple(sorted(S))
def table(S):
 lookup={x:i for i,x in enumerate(S)}
 return [[lookup[compose(x,y)] for y in S] for x in S]
def context_classes(T):
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
 reps=[c.index(i) for i in range(max(c)+1)]
 return [[c[T[i][j]] for j in reps] for i in reps]
def iscs(T):
 n=len(T);E=[e for e in range(n) if T[e][e]==e]
 for x in range(n):
  ideal={x}|{T[a][x] for a in range(n)}|{T[x][b] for b in range(n)}|{T[T[a][x]][b] for a,b in product(range(n),repeat=2)}
  if len(ideal)!=n:return False
 return bool(E) and all(e==f or T[e][f]!=e or T[f][e]!=e for e,f in product(E,repeat=2))
seen=set();counts=Counter();witness=None
for k in (1,2,3):
 for seed in combinations(X,k):
  S=generated(seed)
  if S in seen:continue
  seen.add(S);counts['unique']+=1;T=table(S);n=len(S)
  if not all(any(T[T[i][j]][i]==i for j in range(n)) for i in range(n)):continue
  counts['regular']+=1;E=[e for e in range(n) if T[e][e]==e]
  if any(({T[e][s] for e in E}&{T[s][f] for f in E}&set(E)) and s not in E for s in range(n)):continue
  counts['weakE']+=1;q=context_classes(T);D=quotient(T,q)
  assert all((T[i][i]==i)==(D[q[i]][q[i]]==q[i]) for i in range(n))
  if not iscs(D):
   counts['weakE_not_qCS']+=1;witness=(S,T,q,D);print('COUNTEREXAMPLE',witness);break
 if witness:break
print('RESULT',dict(counts),'no-universal-inference; generators at most3 on 3 points')
