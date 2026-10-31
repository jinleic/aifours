from itertools import product
from collections import Counter

def parts(n):
 out=[]
 def go(seq):
  if len(seq)==n:out.append(tuple(seq));return
  for v in range(max(seq)+2):go(seq+[v])
 go([0]);return out

def mono_classes(T,side):
 n=len(T);p=list(range(n))
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 for i,j in product(range(n),repeat=2):
  a=root(i if side=='row' else j);b=root(T[i][j]);p[b]=a
 lab={};return tuple(lab.setdefault(root(i),len(lab)) for i in range(n))

def green_classes(T,side):
 n=len(T)
 ideals=[frozenset([i]+([T[i][j] for j in range(n)] if side=='row' else [T[j][i] for j in range(n)])) for i in range(n)]
 lab={};return tuple(lab.setdefault(x,len(lab)) for x in ideals)

def quotient(T,classes):
 n=len(T);k=max(classes)+1
 reps=[next(i for i,c in enumerate(classes) if c==j) for j in range(k)]
 return [[classes[T[i][j]] for j in reps] for i in reps]

def is_congruence(T,c):
 n=len(T)
 return all(c[i]!=c[j] or (c[T[i][k]]==c[T[j][k]] and c[T[k][i]]==c[T[k][j]]) for i,j,k in product(range(n),repeat=3))

def is_cs(T):
 n=len(T); idem=[i for i in range(n) if T[i][i]==i]
 for x in range(n):
  ideal={x}|{T[a][x] for a in range(n)}|{T[x][b] for b in range(n)}|{T[T[a][x]][b] for a,b in product(range(n),repeat=2)}
  if len(ideal)!=n:return False
 return bool(idem) and all(e==f or T[e][f]!=e or T[f][e]!=e for e,f in product(idem,repeat=2))

def contexts(T):
 n=len(T);ctx=[None]+list(range(n));out=[]
 for s in range(n):
  sig=[]
  for x,y in product(ctx,repeat=2):
   t=s if x is None else T[x][s]
   if y is not None:t=T[t][y]
   sig.append(T[t][t]==t)
  out.append(tuple(sig))
 lab={};return tuple(lab.setdefault(v,len(lab)) for v in out)

def pure(T,c,U):return all((T[s][s]==s)==(U[c[s]][c[s]]==c[s]) for s in range(len(T)))
counts=Counter();bell={1:1,2:2,3:5}
for n in (1,2,3):
 for flat in product(range(n),repeat=n*n):
  T=[flat[i*n:(i+1)*n] for i in range(n)]
  if not all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(n),repeat=3)):continue
  counts['associative']+=1
  if not all(any(T[T[i][j]][i]==i for j in range(n)) for i in range(n)):continue
  counts['regular']+=1
  q=contexts(T);assert is_congruence(T,q);D=quotient(T,q)
  if not pure(T,q,D) or not is_cs(D):continue
  counts['q_pure_cs']+=1
  rf=mono_classes(T,'row');cf=mono_classes(T,'col');dr=green_classes(D,'row');dc=green_classes(D,'col')
  rowfib={};colfib={}
  for s in range(n):
   if rf[s] in rowfib:assert rowfib[rf[s]]==dr[q[s]]
   if cf[s] in colfib:assert colfib[cf[s]]==dc[q[s]]
   rowfib[rf[s]]=dr[q[s]];colfib[cf[s]]=dc[q[s]]
  sizesR=Counter(rowfib.values());sizesC=Counter(colfib.values());expected=1
  for v in list(sizesR.values())+list(sizesC.values()):expected*=bell[v]
  purekernels=[]
  for c in parts(n):
   if is_congruence(T,c):
    U=quotient(T,c)
    if pure(T,c,U) and is_cs(U):purekernels.append(c)
  assert len(purekernels)==expected
  lab={};finest=tuple(lab.setdefault((rf[s],cf[s],q[s]),len(lab)) for s in range(n))
  assert is_congruence(T,finest) and finest in purekernels
  assert all(all(finest[i]!=finest[j] or c[i]==c[j] for i,j in product(range(n),repeat=2)) for c in purekernels)
  groupsize=len(D)//(len(set(dr))*len(set(dc)))
  assert len(set(finest))==len(set(rf))*len(set(cf))*groupsize
  counts['quotient_lattice_checked']+=1
 print('n=',n,' cumulative=',dict(counts),sep='')
print('PASS all labelled semigroups of orders 1-3 at the exact filtered hypothesis; finite check only')
