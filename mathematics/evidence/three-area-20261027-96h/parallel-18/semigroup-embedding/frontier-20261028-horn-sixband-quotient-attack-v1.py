from collections import deque,Counter
from itertools import product,combinations
T=((0,1,0,0,4,5),(0,1,1,1,4,5),(0,1,2,2,4,5),(0,1,3,3,4,5),(4,4,4,4,4,4),(0,1,0,1,4,5));flip=(1,0,3,2,4,5)
B=range(6);D=list(product(range(2),repeat=3));H=list(product(B,D));N=len(H);hi={x:i for i,x in enumerate(H)}
def dm(x,y):
 i,g,l=x;j,h,m=y;return i,g^(l&j)^h,m
def hm(x,y):
 a,(i,g,l)=x;b,(j,h,m)=y
 return T[a][flip[b] if g^(l&j) else b],dm(x[1],y[1])
M=[[hi[hm(x,y)] for y in H] for x in H]
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
 labels={};cls=[labels.setdefault(root(i),len(labels)) for i in range(N)];n=len(labels)
 reps=[next(i for i,c in enumerate(cls) if c==j) for j in range(n)]
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
seeds=[(hi[(a,d)],hi[(b,d)]) for d in D for a,b in combinations(B,2)]
seen={}
for a,b in seeds:
 Q,actor,part=quotient(a,b)
 if part not in seen:seen[part]=(len(Q),analyse(Q,actor),(H[a],H[b]))
counts=Counter((n,ne,nc,len(fails),orth,li) for n,(ne,nc,fails,orth,li),seed in seen.values())
print('H=48, actor=8; pair seeds=',len(seeds),' distinct quotient congruences=',len(seen),sep='')
for key,count in sorted(counts.items()):print('size,E,comparable,collapsed,orthodox,locally_inverse=',key,' count=',count,sep='')
fails=[v for v in seen.values() if v[1][2]]
print('TOTAL quotient classes with comparable collapse=',len(fails),'; no universal conclusion',sep='')
if fails:print('FIRST FAILURE',fails[0])
