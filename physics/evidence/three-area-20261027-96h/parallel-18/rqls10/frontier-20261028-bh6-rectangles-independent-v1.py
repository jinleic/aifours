#!/usr/bin/env python3
"""Independent complete rectangle extraction and Q(zeta6) polynomial-gcd replay."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();assert len(lines)==34
claimed=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())
expected={(r['class'],tuple(f['rows']),tuple(f['columns'])) for r in claimed['records'] for f in r['families']}
assert len(expected)==104
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)];Z=(Q(0),Q(0));mu={tuple(map(Q,a)) for a in six}
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def conj(a):return a[0]+a[1],-a[1]
def norm(a):v=mul(a,conj(a));assert v[1]==0 and v[0]>=0;return v[0]
def div(a,b):
 n=norm(b);assert n>0;v=mul(a,conj(b));return v[0]/n,v[1]/n
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def trim(a):
 a=list(a)
 while a and a[-1]==Z:a.pop()
 return a
def rem(a,b):
 a=trim(a);b=trim(b)
 while a and len(a)>=len(b):
  k=len(a)-len(b);v=div(a[-1],b[-1])
  for j,x in enumerate(b):a[j+k]=sub(a[j+k],mul(v,x))
  a=trim(a)
 return a
def gcd(a,b):
 a,b=trim(a),trim(b)
 while b:a,b=b,rem(a,b)
 if not a:return []
 return [div(v,a[-1]) for v in a]
@lru_cache(None)
def roots_kind(coeff):
 p=list(coeff);star=[conj(p[2]),conj(p[1]),conj(p[0])]
 if all(v==Z for v in p):return 'identity'
 g=gcd(p,star)
 if len(g)<=1:return 'no_unit'
 if len(g)==2:
  root=neg(g[0])
  if norm(root)!=1:return 'no_unit'
  assert root in mu
  return 'mu6'
 assert len(g)==3 and p[2]!=Z
 if norm(p[1])>4*norm(p[2]):return 'no_unit'
 roots=[r for r in mu if add(add(mul(p[2],mul(r,r)),mul(p[1],r)),p[0])==Z]
 disc=sub(mul(p[1],p[1]),mul((Q(4),Q(0)),mul(p[2],p[0])))
 assert len(roots)==2 or (len(roots)==1 and disc==Z)
 return 'mu6'
def matching(adj):
 @lru_cache(None)
 def rec(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and rec(left-{a,b}) for b in left-{a})
 return rec(frozenset(range(10)))
actual=set();matrices=[]
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1::6'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 for r,s in combinations(range(10),2):assert zero6([H[r][c]-H[s][c] for c in range(10)])
 matrices.append(H)
 for cmask in range(1,1023,2):
  C=tuple(c for c in range(10) if cmask>>c&1)
  bad=[0]*10
  for r,s in combinations(range(10),2):
   if not zero6([H[r][c]-H[s][c] for c in C]):bad[r]|=1<<s;bad[s]|=1<<r
  for rmask in range(1,1023,2):
   if all(not (bad[r]&(~rmask&1023)) for r in range(10) if rmask>>r&1):
    actual.add((idx,tuple(r for r in range(10) if rmask>>r&1),C))
assert actual==expected and len(actual)==104
print('PASS 34 validated BH, independently enumerated exactly104 normalized rectangles',flush=True)
hist=Counter();families=[]
for idx,R,C in sorted(actual):
 H=matrices[idx-1];rs=set(R);cs=set(C);generic=0;counts=Counter()
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   co=[Z,Z,Z]
   for t in E:
    k=int(t in rs and d in cs)-int(t in rs and c in cs)+1
    co[k]=add(co[k],tuple(map(Q,six[(H[t][d]-H[t][c])%6])))
   kind=roots_kind(tuple(co));counts[kind]+=1;hist[kind]+=1
   if kind=='identity':adj[c].add(d);adj[d].add(c)
  if matching(adj):generic+=1
 assert generic==0
 families.append({'class':idx,'rows':R,'columns':C,'counts':dict(counts),'generic_matching_halves':generic})
print('PASS all104 families; identity-edge graphs have no perfect matching; all other unit roots belong to mu6',flush=True)
print('half-polynomial category totals',dict(hist),'unique patterns',roots_kind.cache_info().currsize,flush=True)
(P/'frontier-20261028-bh6-rectangles-independent-result-v1.json').write_text(json.dumps({'families':families,'category_totals':dict(hist),
 'scope':'exact finite family/cyclotomic replay; endpoint mu6 exclusion uses prior q6 theorem'},indent=2,sort_keys=True)+'\n')
