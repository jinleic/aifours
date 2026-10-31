from functools import lru_cache
from itertools import product
from math import factorial,comb
from collections import deque
import time

@lru_cache(None)
def content(s):return frozenset() if s is None else content(s[2])|{s[1]}
@lru_cache(None)
def sig(w):
 if not w:return None
 last={c:i for i,c in enumerate(w)};crit=min(last,key=last.get)
 return w[0],crit,sig(w[last[crit]+1:])
@lru_cache(None)
def mul(a,b):
 if a is None:return b
 if b is None:return a
 missing=content(a)-content(b)
 if not missing:return a[0],b[1],b[2]
 cursor=a
 while cursor[1] not in missing:cursor=cursor[2]
 return a[0],cursor[1],mul(cursor[2],b)
@lru_cache(None)
def word(s):
 if s is None:return ()
 h,c,t=s;w=(h,c)+word(t)
 return tuple(x for i,x in enumerate(w) if i==0 or x!=w[i-1])
def right_states(n):
 gens=[sig((i,)) for i in range(n)];seen=set();q=deque(gens)
 while q:
  a=q.popleft()
  if a in seen:continue
  seen.add(a)
  for b in gens:q.append(mul(a,b))
 return sorted(seen,key=repr)
for n in (1,2,3,4):
 R=right_states(n);expected=sum(comb(n,k)*factorial(k)**2 for k in range(1,n+1))
 assert len(R)==expected and all(sig(word(a))==a and mul(a,a)==a for a in R)
 assert all(len(word(a))<=2*n-1 for a in R)
 assert all(mul(a,b)==sig(word(a)+word(b)) for a,b in product(R,repeat=2))
 if n<=3:
  assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(R,repeat=3))
  assert all(mul(mul(a,b),c)==mul(mul(mul(mul(a,c),a),b),c) for a,b,c in product(R,repeat=3))
 print('right-SN free signatures n=',n,' size=',len(R),' maximal representative length=',max(map(lambda a:len(word(a)),R)),sep='')

def pair_product(a,b):return mul(a[0],b[0]),mul(b[1],a[1])
for n in (1,2,3,4):
 gs=[(sig((i,)),sig((i,))) for i in range(n)];seen=set();q=deque(gs);start=time.monotonic();stop=None
 while q:
  a=q.popleft()
  if a in seen:continue
  seen.add(a)
  if len(seen)>30000 or time.monotonic()-start>10:stop='discovery cap';break
  for b in gs:q.append(pair_product(a,b))
 print('paired-SN signatures n=',n,' size=',len(seen),' complete=',stop is None,' elapsed=',round(time.monotonic()-start,3),sep='')
print('LIMIT interpreting signatures as free objects requires the written universal normal-form proof')
