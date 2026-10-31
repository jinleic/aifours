from itertools import product,combinations
from collections import Counter
X=list(product(range(3),repeat=3))
def comp(f,g):return tuple(f[g[i]] for i in range(3))
def generated(seed):
 S=set(seed);todo=list(S)
 while todo:
  x=todo.pop()
  for y in list(S):
   for z in (comp(x,y),comp(y,x)):
    if z not in S:S.add(z);todo.append(z)
 return tuple(sorted(S))
def table(S):
 idx={x:i for i,x in enumerate(S)};return [[idx[comp(x,y)] for y in S] for x in S]
seen=set();count=Counter();examples=[]
for m in (1,2,3):
 for seed in combinations(X,m):
  S=generated(seed)
  if S in seen:continue
  seen.add(S);T=table(S);n=len(S)
  if not all(any(T[T[x][y]][x]==x for y in range(n)) for x in range(n)):continue
  count['regular']+=1;E={x for x in range(n) if T[x][x]==x}
  if any(({T[e][s] for e in E}&{T[s][f] for f in E}&E) and s not in E for s in range(n)):continue
  count['weakE']+=1;localr=True;localinverse=True
  for e in E:
   corner={T[T[e][x]][e] for x in range(n)};ce=corner&E
   if any(T[x][y] not in ce for x,y in product(ce,repeat=2)):localr=False;break
   if any(T[T[T[T[x][y]][x]][z]][x]!=T[T[T[x][y]][z]][x] for x,y,z in product(ce,repeat=3)):localr=False;break
   if any(T[x][y]!=T[y][x] for x,y in product(ce,repeat=2)):localinverse=False
  if not localr:continue
  count['original']+=1;orth=all(T[e][f] in E for e,f in product(E,repeat=2))
  count['orthodox']+=orth;count['locally_inverse']+=localinverse
  if not orth and not localinverse:count['neither']+=1;examples.append((S,seed))
print('unique',len(seen),'counts',dict(count),'neither examples',len(examples))
if examples:print('first neither source size',len(examples[0][0]),'seed',examples[0][1])
