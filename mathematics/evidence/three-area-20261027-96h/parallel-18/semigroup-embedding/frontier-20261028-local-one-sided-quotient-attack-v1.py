from collections import deque,Counter
from itertools import product,combinations
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
S=list(product(range(5),repeat=2));idx={x:i for i,x in enumerate(S)}
T=[[idx[(B[x[0]][y[0]],B[y[1]][x[1]])] for y in S] for x in S]
def cong(T,seeds):
 n=len(T);p=list(range(n));todo=deque(seeds)
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 while todo:
  a,b=todo.popleft();i=root(a);j=root(b)
  if i==j:continue
  p[j]=i
  for x in range(n):todo.append((T[a][x],T[b][x]));todo.append((T[x][a],T[x][b]))
 lab={};return tuple(lab.setdefault(root(i),len(lab)) for i in range(n))
def analyse(U):
 n=len(U);left=set();right=set()
 for e in range(n):
  corner={U[U[e][x]][e] for x in range(n)}
  assert all(U[U[U[U[x][y]][x]][z]][x]==U[U[U[x][y]][z]][x] for x,y,z in product(corner,repeat=3))
  for x,y in product(corner,repeat=2):
   xyx=U[U[x][y]][x]
   if xyx!=U[x][y]:left.add((xyx,U[x][y]))
   if xyx!=U[y][x]:right.add((xyx,U[y][x]))
 L=cong(U,left);R=cong(U,right)
 return [(i,j) for i in range(n) for j in range(i) if L[i]==L[j] and R[i]==R[j]],L,R
seen={};witness=None
for i,j in combinations(range(25),2):
 c=cong(T,[(i,j)])
 if c in seen:continue
 n=max(c)+1;reps=[c.index(a) for a in range(n)];U=[[c[T[a][b]] for b in reps] for a in reps]
 common,L,R=analyse(U);seen[c]=(n,len(common))
 if common:
  witness={'seed':[i,j],'source_pairs':[S[i],S[j]],'partition':list(c),'table':U,'left':list(L),'right':list(R),'common':common}
  print('COUNTERMODEL',witness);break
print('tested distinct quotient partitions=',len(seen),'size/count=',dict(Counter(seen.values())),'no-universal-inference',sep='')
