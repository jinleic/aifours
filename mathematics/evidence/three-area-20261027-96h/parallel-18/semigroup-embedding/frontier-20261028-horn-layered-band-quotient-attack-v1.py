from collections import deque, Counter
from itertools import product, combinations
BT=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
flip=(0,3,4,1,2)
B=list(product(range(5),range(2)))
D=list(product(range(2),repeat=3))
H=list(product(B,D));N=len(H);hi={x:i for i,x in enumerate(H)}
def dm(x,y):
 i,g,l=x;j,h,m=y;return i,g^(l&j)^h,m
def hm(x,y):
 (a,k),(i,g,l)=x;(b,r),(j,h,m)=y
 return (BT[a][flip[b] if g^(l&j) else b],k&r),dm(x[1],y[1])
M=[[hi[hm(x,y)] for y in H] for x in H]

def quotient(a,b):
 parent=list(range(N));todo=deque([(a,b)])
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 while todo:
  x,y=todo.popleft();i=root(x);j=root(y)
  if i==j:continue
  parent[j]=i
  for k in range(N):todo.append((M[x][k],M[y][k]));todo.append((M[k][x],M[k][y]))
 roots=[root(i) for i in range(N)];labels={};cls=[labels.setdefault(r,len(labels)) for r in roots];n=len(labels)
 reps=[next(i for i,c in enumerate(cls) if c==k) for k in range(n)]
 Q=[[cls[M[i][j]] for j in reps] for i in reps];actor=[H[i][1] for i in reps]
 assert all(actor[cls[i]]==H[i][1] for i in range(N))
 assert all(Q[cls[i]][cls[j]]==cls[M[i][j]] for i,j in product(range(N),repeat=2))
 return Q,actor,tuple(cls)

def analyse(Q,actor):
 n=len(Q);E=[i for i in range(n) if Q[i][i]==i];ES=set(E)
 assert all((actor[i][1]==(actor[i][0]&actor[i][2]))==(i in ES) for i in range(n))
 assert all(any(Q[Q[x][y]][x]==x and Q[Q[y][x]][y]==y for y in range(n)) for x in range(n))
 assert all(not(Q[e][s]==e and Q[s][e]==e) or s in ES for e,s in product(E,range(n)))
 orthodox=all(Q[x][y] in ES for x,y in product(E,repeat=2));li=True
 for e in E:
  corner={Q[Q[e][x]][e] for x in range(n)};ce=[x for x in corner if x in ES];cs=set(ce)
  assert all(Q[x][y] in cs for x,y in product(ce,repeat=2))
  assert all(Q[Q[Q[Q[x][y]][x]][z]][x]==Q[Q[Q[x][y]][z]][x] for x,y,z in product(ce,repeat=3))
  if any(Q[x][y]!=Q[y][x] for x,y in product(ce,repeat=2)):li=False
 unary=[set() for _ in range(2*n)];pairs=[[] for _ in range(2*n)]
 def v(u,s):return u*n+s
 for u,s,t in product(range(2),range(n),range(n)):
  i,g,l=actor[s];j,h,mu=actor[t];z=v(u,Q[s][t]);x=v(u,s);y=v(u^g^(l&j),t)
  unary[z].update((x,y));pairs[x].append((y,z));pairs[y].append((x,z))
 def close(start):
  seen={start};todo=deque([start])
  while todo:
   a=todo.popleft()
   for b in unary[a]:
    if b not in seen:seen.add(b);todo.append(b)
   for b,c in pairs[a]:
    if b in seen and c not in seen:seen.add(c);todo.append(c)
  return seen
 cache={};comps=[(x,y) for x,y in product(E,repeat=2) if x!=y and actor[x]==actor[y] and Q[x][y]==x and Q[y][x]==x];fails=[]
 for x,y in comps:
  if y not in cache:cache[y]=close(v(0,y))
  if v(0,x) in cache[y]:fails.append((x,y))
 return len(E),len(comps),tuple(fails),orthodox,li

patterns=[((a,k),(b,k)) for k in range(2) for a,b in [(0,1),(0,2),(1,2),(1,3),(2,4)]]+[((a,0),(a,1)) for a in range(5)]
candidates=[(hi[(a,d)],hi[(b,d)]) for d in D for a,b in patterns]
seen={}
for a,b in candidates:
 Q,actor,part=quotient(a,b)
 if part not in seen:seen[part]=(len(Q),analyse(Q,actor),(H[a],H[b]))
counts=Counter((size,ne,nc,len(fails),orth,li) for size,(ne,nc,fails,orth,li),pair in seen.values())
print('H=80; selected actor-compatible generators=',len(candidates),' distinct quotient congruences=',len(seen),sep='')
for key,n in sorted(counts.items()):print('size,E,comparables,collapsed,orthodox,locally_inverse=',key,' quotient count=',n,sep='')
failures=[(size,detail,pair) for size,detail,pair in seen.values() if detail[2]]
print('TOTAL quotient classes with comparable collapse=',len(failures),'; no universal conclusion',sep='')
if failures:print('FIRST FAILURE',failures[0])
