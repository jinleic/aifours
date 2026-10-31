from collections import deque
from itertools import permutations

letters='abuvpq'
words=[w for k in range(1,7) for w in permutations(letters,k)]
ids={w:i for i,w in enumerate(words)}
def mul(x,y):
 sy=set(y)
 return tuple(a for a in x if a not in sy)+y
def W(s):
 w=()
 for c in s:w=mul(w,(c,))
 return ids[w]
assert len(words)==1956
E=W('vpq');F=W('vq')
seeds=[(mul(words[E],words[F]),words[F]),(mul(words[F],words[E]),words[E]),(mul(words[E],('b',)),words[E]),(mul(words[F],('b',)),words[F]),(mul(('a',),words[E]),mul(('a',),words[F])),(words[F],words[W('upq')])]
parent=list(range(len(words)));edges=[];todo=deque((ids[x],ids[y],('seed',k)) for k,(x,y) in enumerate(seeds))
def find(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
while todo and find(E)!=find(F):
 x,y,reason=todo.popleft();i=find(x);j=find(y)
 if i==j:continue
 parent[j]=i;edge=len(edges);edges.append((x,y,reason))
 for c in letters:
  todo.append((ids[mul((c,),words[x])],ids[mul((c,),words[y])],('left',c,edge)))
  todo.append((ids[mul(words[x],(c,))],ids[mul(words[y],(c,))],('right',c,edge)))
print('free RRB words=',len(words),'accepted congruence steps=',len(edges),'e=f?',find(E)==find(F),sep='')
if find(E)==find(F):
 adj=[[] for _ in words]
 for k,(x,y,reason) in enumerate(edges):adj[x].append((y,k));adj[y].append((x,k))
 back={E:None};q=deque([E])
 while q and F not in back:
  x=q.popleft()
  for y,k in adj[x]:
   if y not in back:back[y]=(x,k);q.append(y)
 assert F in back
 path=[];x=F
 while x!=E:
  x,k=back[x];path.append(k)
 used=set(path);stack=list(used)
 while stack:
  k=stack.pop();reason=edges[k][2]
  if reason[0]!='seed':
   p=reason[2]
   if p not in used:used.add(p);stack.append(p)
 print('proof edges=',len(used),'transitivity path length=',len(path),'largest id=',max(used),sep='')
 print('RESULT: source hypotheses entail e=f in every right-regular band')
else:
 print('COUNTERMODEL: completed finite free-RRB congruence keeps e,f distinct')
