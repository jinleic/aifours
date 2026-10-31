from functools import lru_cache
from collections import deque
from math import comb,factorial

@lru_cache(None)
def content(a):return frozenset() if a is None else content(a[2])|{a[1]}
@lru_cache(None)
def sig(w):
 if not w:return None
 pos={x:i for i,x in enumerate(w)};c=min(pos,key=pos.get)
 return w[0],c,sig(w[pos[c]+1:])
@lru_cache(None)
def mul(a,b):
 if a is None:return b
 if b is None:return a
 missing=content(a)-content(b)
 if not missing:return a[0],b[1],b[2]
 x=a
 while x[1] not in missing:x=x[2]
 return a[0],x[1],mul(x[2],b)
@lru_cache(None)
def word(a):
 if a is None:return ()
 w=(a[0],a[1])+word(a[2]);return tuple(x for i,x in enumerate(w) if i==0 or x!=w[i-1])
def pmul(a,b):return mul(a[0],b[0]),mul(b[1],a[1])
def pair_count(n):return sum(comb(n,k)*(1 if k==1 else k*k*factorial(k-1)**4) for k in range(1,n+1))
for n in range(1,5):
 gens=[(sig((i,)),sig((i,))) for i in range(n)];seen=set();todo=deque(gens)
 while todo:
  a=todo.popleft()
  if a in seen:continue
  seen.add(a)
  for b in gens:todo.append(pmul(a,b))
 assert len(seen)==pair_count(n)
 for a,b in seen:
  k=len(content(a));assert content(a)==content(b)
  if k==1:normal=(a[1],)
  else:normal=tuple(reversed(word(b[2])))+(b[1],a[1])+word(a[2])
  assert sig(normal)==a and sig(normal[::-1])==b
  assert len(normal)<=max(1,4*k-4)
 full=sum(len(content(a))==n for a,b in seen)
 assert full==(1 if n==1 else n*n*factorial(n-1)**4)
 print('n=',n,' correlated states=',len(seen),' full-content=',full,' all short normal representatives checked',sep='')
print('formula-only larger counts n5=',pair_count(5),' n6=',pair_count(6),' (NOT enumerated)',sep='')
print('LIMIT universal count/freeness proof is written separately; no source-injectivity conclusion')
