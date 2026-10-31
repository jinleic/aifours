from itertools import product
from collections import deque

def sig(w):
 if not w:return ()
 C=set(w)
 if len(C)==1:return ('a',w[0])
 for i in range(len(w)):
  if set(w[:i+1])==C:pre=w[:i];last=w[i];break
 for i in range(len(w)-1,-1,-1):
  if set(w[i:])==C:suf=w[i+1:];first=w[i];break
 return last,sig(pre),first,sig(suf)
words=[];ids={};todo=deque(['a','b','c'])
while todo:
 w=todo.popleft();s=sig(w)
 if s in ids:continue
 ids[s]=len(words);words.append(w)
 for c in 'abc':todo.append(w+c)
assert len(words)==159
T=[[ids[sig(x+y)] for y in words] for x in words]

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
 labels={};return [labels.setdefault(root(i),len(labels)) for i in range(n)]
seeds=set()
for e in range(159):
 corner={T[T[e][x]][e] for x in range(159)}
 for x,y,z in product(corner,repeat=3):
  a=T[T[T[T[x][y]][x]][z]][x];b=T[T[T[x][y]][z]][x]
  if a!=b:seeds.add((a,b))
c=cong(T,seeds);n=max(c)+1;reps=[c.index(i) for i in range(n)];U=[[c[T[i][j]] for j in reps] for i in reps]
print('free band3=159; local-regular seed pairs=',len(seeds),' quotient size=',n,sep='')
left=set();right=set()
for e in range(n):
 corner={U[U[e][x]][e] for x in range(n)}
 assert all(U[U[U[U[x][y]][x]][z]][x]==U[U[U[x][y]][z]][x] for x,y,z in product(corner,repeat=3))
 for x,y in product(corner,repeat=2):
  xyx=U[U[x][y]][x]
  if xyx!=U[x][y]:left.add((xyx,U[x][y]))
  if xyx!=U[y][x]:right.add((xyx,U[y][x]))
l=cong(U,left);r=cong(U,right)
coll=[(i,j) for i in range(n) for j in range(i) if l[i]==l[j] and r[i]==r[j]]
print('localLRB quotient=',len(set(l)),' localRRB quotient=',len(set(r)),' common collapsed pairs=',len(coll),sep='')
if coll:print('FIRST',coll[0],'words',words[reps[coll[0][0]]],words[reps[coll[0][1]]])
print('LIMIT finite free-three-generator case; no all-band subdirect theorem')
