import json,time
from pathlib import Path
from collections import deque,Counter
from itertools import product,combinations
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-10band-host-data-v1.json').read_text())
BT=J['band_table'];flip=J['band_action'];D=list(product(range(2),repeat=3));H=list(product(range(10),D));idx={x:i for i,x in enumerate(H)};N=len(H)
def dm(x,y):
 i,g,l=x;j,h,m=y;return i,g^(l&j)^h,m
def hm(x,y):
 a,(i,g,l)=x;b,(j,h,m)=y;w=g^(l&j)
 return BT[a][flip[b] if w else b],dm(x[1],y[1])
M=[[idx[hm(x,y)] for y in H] for x in H]
def quotient(a,b):
 p=list(range(N));todo=deque([(a,b)])
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 while todo:
  x,y=todo.popleft();i=root(x);j=root(y)
  if i==j:continue
  p[j]=i
  for k in range(N):todo.append((M[x][k],M[y][k]));todo.append((M[k][x],M[k][y]))
 labels={};c=tuple(labels.setdefault(root(i),len(labels)) for i in range(N));n=len(labels);rep=[c.index(k) for k in range(n)]
 Q=[[c[M[i][j]] for j in rep] for i in rep];A=[H[i][1] for i in rep]
 assert all(A[c[i]]==H[i][1] for i in range(N))
 return c,Q,A

def horn_fail(Q,A):
 n=len(Q);E=[i for i in range(n) if Q[i][i]==i];unary=[set() for _ in range(2*n)];binary=[[] for _ in range(2*n)]
 def v(u,i):return u*n+i
 for u,s,t in product(range(2),range(n),range(n)):
  z=v(u,Q[s][t]);x=v(u,s);y=v(u^A[s][1]^(A[s][2]&A[t][0]),t)
  unary[z].update((x,y));binary[x].append((y,z));binary[y].append((x,z))
 comp=[(e,f) for e,f in product(E,repeat=2) if e!=f and A[e]==A[f] and Q[e][f]==Q[f][e]==e];cache={}
 for e,f in comp:
  if f not in cache:
   seen={v(0,f)};todo=deque(seen)
   while todo:
    x=todo.popleft()
    for y in unary[x]:
     if y not in seen:seen.add(y);todo.append(y)
    for y,z in binary[x]:
     if y in seen and z not in seen:seen.add(z);todo.append(z)
   cache[f]=seen
  if v(0,e) in cache[f]:return e,f
 return None
seen=set();count=Counter();failure=None;started=time.monotonic()
for d in D:
 for a,b in combinations(range(10),2):
  c,Q,A=quotient(idx[(a,d)],idx[(b,d)])
  if c in seen:continue
  seen.add(c);count[len(Q)]+=1;f=horn_fail(Q,A)
  if f:
   failure={'seed':[a,b,d],'partition':list(c),'source_table':Q,'actor':A,'collapsed_pair':f};print('FAILURE',failure);break
 if failure:break
print('RESULT distinct actor-compatible quotients=',len(seen),' size counts=',dict(count),' comparable-collapse=',failure is not None,' elapsed_seconds=',round(time.monotonic()-started,3),sep='')
print('LIMIT bounded exact quotient family, not universal original-class result')
