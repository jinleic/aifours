from itertools import product
from collections import deque
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
S=list(product(range(5),repeat=2));idx={s:i for i,s in enumerate(S)}
T=[[idx[(B[x[0]][y[0]],B[y[1]][x[1]])] for y in S] for x in S];n=25

def cong(seeds):
 p=list(range(n));todo=deque(seeds)
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 while todo:
  a,b=todo.popleft();i=root(a);j=root(b)
  if i==j:continue
  p[j]=i
  for x in range(n):todo.append((T[a][x],T[b][x]));todo.append((T[x][a],T[x][b]))
 lab={};return [lab.setdefault(root(i),len(lab)) for i in range(n)]
left=set();right=set()
for z in range(n):
 corner={T[T[z][x]][z] for x in range(n)}
 for e,f in product(corner,repeat=2):
  efe=T[T[e][f]][e]
  left.add((efe,T[e][f]));right.add((efe,T[f][e]))
L=cong(left);R=cong(right);C=cong(left|right)
assert len(set(L))==len(set(R))==20 and len(set(C))==16
assert all(i==j or (L[i],R[i])!=(L[j],R[j]) for i,j in product(range(n),repeat=2))
mapL={L[s]:C[s] for s in range(n)};mapR={R[s]:C[s] for s in range(n)}
pullback={(a,b) for a,b in product(set(L),set(R)) if mapL[a]==mapR[b]}
assert len(pullback)==25 and pullback=={(L[s],R[s]) for s in range(n)}
for s,t in product(range(n),repeat=2):
 if C[s]==C[t]:
  u=s;v=T[T[s][u]][t]
  assert L[v]==L[s] and R[v]==R[t]
  assert any(L[s]==L[x] and R[x]==R[t] for x in range(n))
  assert any(R[s]==R[x] and L[x]==L[t] for x in range(n))
print('PASS nondegenerate SN band source25: quotient sizes20,20 overLI16, fibre product exactly25')
print('PASS every compatible source pair filler sut withu=s; congruences commute and intersect in equality')
