from functools import lru_cache
from itertools import product,permutations
from collections import deque
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
assert all(B[B[a][b]][c]==B[a][B[b][c]] for a,b,c in product(range(5),repeat=3))
assert all(B[B[a][b]][c]==B[B[B[B[a][c]][a]][b]][c] for a,b,c in product(range(5),repeat=3))
@lru_cache(None)
def sig(w):
 if not w:return None
 last={a:i for i,a in enumerate(w)};c=min(last,key=last.get)
 return w[0],c,sig(w[last[c]+1:])
@lru_cache(None)
def C(a):return frozenset() if a is None else C(a[2])|{a[1]}
@lru_cache(None)
def mul(a,b):
 if a is None:return b
 if b is None:return a
 missing=C(a)-C(b)
 if not missing:return a[0],b[1],b[2]
 x=a
 while x[1] not in missing:x=x[2]
 return a[0],x[1],mul(x[2],b)
@lru_cache(None)
def word(a):
 if a is None:return ()
 w=(a[0],a[1])+word(a[2]);return tuple(x for i,x in enumerate(w) if i==0 or x!=w[i-1])
def evaluate(w,assignment):
 a=assignment[w[0]]
 for c in w[1:]:a=B[a][assignment[c]]
 return a
for n in range(1,5):
 coords=[]
 for a in range(n):coords.append(tuple(2 if i==a else 1 for i in range(n)))
 for a,b in permutations(range(n),2):coords.append(tuple(2 if i==a else 4 if i==b else 1 for i in range(n)))
 for mask in range(1<<n):
  for h in range(n):
   if mask&(1<<h):continue
   coords.append(tuple(0 if mask&(1<<i) else 1 if i==h else 3 for i in range(n)))
 assert len(coords)==n*n+n*(1<<(n-1))
 coordset=set(coords);gens=[sig((i,)) for i in range(n)];states=set();todo=deque(gens)
 while todo:
  a=todo.popleft()
  if a in states:continue
  states.add(a)
  for b in gens:todo.append(mul(a,b))
 vectors={tuple(evaluate(word(a),v) for v in coords) for a in states}
 assert len(vectors)==len(states)
 for p in permutations(range(n)):
  assert all(tuple(v[p[i]] for i in range(n)) in coordset for v in coords)
 print('n=',n,' free rightSNstates=',len(states),' coordinate bound=',len(coords),' all distinct and symmetric-group stable',sep='')
print('PASS finite five-band separator family; universal signature-separation argument is written separately')
