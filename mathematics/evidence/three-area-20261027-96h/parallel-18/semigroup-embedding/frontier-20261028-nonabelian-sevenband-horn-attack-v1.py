from itertools import permutations,product,combinations
from collections import deque,Counter
import time
G=list(permutations(range(3)));gid={g:i for i,g in enumerate(G)};one=gid[(0,1,2)];tau=gid[(1,0,2)]
def comp(a,b):return tuple(a[b[i]] for i in range(3))
GM=[[gid[comp(a,b)] for b in G] for a in G]
P=((one,one),(one,tau));D=list(product(range(2),range(6),range(2)))
def dm(x,y):
 i,g,l=x;j,h,m=y;return i,GM[GM[g][P[l][j]]][h],m
def bm(a,b):
 if b==0:return 0
 if a==0:return b+3 if b<=3 else b
 if a<=3:return a if b<=3 else b
 return a if b<=3 else b
def act(g,b):return 0 if b==0 else 1+G[g][b-1] if b<=3 else 4+G[g][b-4]
H=list(product(range(7),D));idx={x:i for i,x in enumerate(H)};N=len(H)
def hm(x,y):
 a,(i,g,l)=x;b,(j,h,m)=y;w=GM[g][P[l][j]]
 return bm(a,act(w,b)),dm(x[1],y[1])
M=[[idx[hm(x,y)] for y in H] for x in H]
def quotient(a,b):
 p=list(range(N));todo=deque([(a,b)])
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 while todo:
  x,y=todo.popleft();i=root(x);j=root(y)
  if i==j:continue
  p[j]=i
  for z in range(N):todo.append((M[x][z],M[y][z]));todo.append((M[z][x],M[z][y]))
 labels={};c=tuple(labels.setdefault(root(i),len(labels)) for i in range(N));k=len(labels);reps=[c.index(i) for i in range(k)]
 Q=[[c[M[i][j]] for j in reps] for i in reps];A=[H[i][1] for i in reps]
 assert all(A[c[i]]==H[i][1] for i in range(N))
 return c,Q,A

def horn(Q,A):
 n=len(Q);E=[i for i in range(n) if Q[i][i]==i];pairs=[(e,f) for e,f in product(E,repeat=2) if e!=f and A[e]==A[f] and Q[e][f]==Q[f][e]==e]
 if not pairs:return None,len(pairs)
 unary=[set() for _ in range(6*n)];binary=[[] for _ in range(6*n)]
 for u,s,t in product(range(6),range(n),range(n)):
  w=GM[A[s][1]][P[A[s][2]][A[t][0]]];z=u*n+Q[s][t];x=u*n+s;y=GM[u][w]*n+t
  unary[z].update((x,y));binary[x].append((y,z));binary[y].append((x,z))
 cache={}
 for e,f in pairs:
  if f not in cache:
   seen={one*n+f};todo=deque(seen)
   while todo:
    x=todo.popleft()
    for y in unary[x]:
     if y not in seen:seen.add(y);todo.append(y)
    for y,z in binary[x]:
     if y in seen and z not in seen:seen.add(z);todo.append(z)
   cache[f]=seen
  if one*n+e in cache[f]:return (e,f),len(pairs)
 return None,len(pairs)
start=time.monotonic();seen=set();counts=Counter();failure=None;stopped=None
for d in [d for d in D if dm(d,d)==d]:
 for a,b in combinations(range(7),2):
  if time.monotonic()-start>20:stopped='observed20-second discovery bound';break
  c,Q,A=quotient(idx[(a,d)],idx[(b,d)])
  if c in seen:continue
  seen.add(c);f,np=horn(Q,A);counts[(len(Q),np)]+=1
  if f:failure={'seed':[a,b,d],'source':Q,'actor':A,'pair':f};print('FAILURE',failure);break
 if failure or stopped:break
print('RESULT original host168; distinct quotients=',len(seen),'size/comparable counts=',dict(counts),'collapse=',failure is not None,'stop=',stopped,'elapsed=',round(time.monotonic()-start,3),sep='')
print('LIMIT S3 action on seven-element SN band; finite bounded quotient family only')
