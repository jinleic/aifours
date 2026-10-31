#!/usr/bin/env python3
"""Exact possible unit-root halfedges for 104 literal q6 rectangle families."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();data=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())
six=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1));Z=(0,0)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]
def conj(x):return x[0]+x[1],-x[1]
def norm(x):
 y=mul(x,conj(x));assert y[1]==0;return y[0]
@lru_cache(None)
def classify(coeff):
 c,b,a=coeff
 if a==b==c==Z:return 'identity'
 A=norm(a)-norm(c);B=sub(mul(a,conj(b)),mul(b,conj(c)));res=A*A-norm(B)
 if res!=0:return 'no_unit'
 if B!=Z:
  nb=norm(B);num=mul((-A,0),conj(B))
  if any(num==(q[0]*nb,q[1]*nb) for q in six):return 'mu6'
  return 'other_field_unit'
 assert A==0
 if a==c==Z:return 'no_unit'
 assert norm(a)>0
 if norm(b)>4*norm(a):return 'no_unit'
 roots=[]
 for r in six:
  if add(add(mul(a,mul(r,r)),mul(b,r)),c)==Z:roots.append(r)
 disc=sub(mul(b,b),mul((4,0),mul(a,c)))
 if len(roots)==2 or (len(roots)==1 and disc==Z):return 'mu6'
 return 'selfinverse_extra'
def perfect(adj):
 @lru_cache(None)
 def rec(mask):
  if not mask:return True
  bit=mask&-mask;i=bit.bit_length()-1;rem=mask^bit;can=adj[i]&rem
  while can:
   b=can&-can;can-=b
   if rec(rem^b):return True
  return False
 return rec(1023)
res=[];summary=Counter()
for item in data['records']:
 idx=item['class'];line=lines[idx-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 for fam in item['families']:
  R=set(fam['rows']);C=set(fam['columns']);mask=[[int(t in R and c in C) for c in range(10)] for t in range(10)]
  counts=Counter();generic=0;firstextra=None
  for E in combinations(range(10),5):
   adj=[0]*10
   for c,d in combinations(range(10),2):
    co=[Z,Z,Z]
    for t in E:
     j=mask[t][d]-mask[t][c]+1;co[j]=add(co[j],six[(H[t][d]-H[t][c])%6])
    typ=classify(tuple(co));counts[typ]+=1
    if typ=='identity':adj[c]|=1<<d;adj[d]|=1<<c
    elif typ in ('other_field_unit','selfinverse_extra') and firstextra is None:firstextra={'E':list(E),'columns':[c,d],'coefficients':[list(x) for x in co],'type':typ}
   if perfect(adj):generic+=1
  status='mu6-only-no-generic' if not generic and not counts['other_field_unit'] and not counts['selfinverse_extra'] else 'unresolved'
  summary[status]+=1;res.append({'class':idx,'rows':sorted(R),'columns':sorted(C),'type_counts':dict(counts),'generic_matching_halves':generic,'first_extra':firstextra,'status':status})
print('families',len(res),'summary',dict(summary),'unique raw polynomial patterns',classify.cache_info().currsize,flush=True)
(P/'frontier-20261028-bh6-rectangle-unitroots-result-v1.json').write_text(json.dumps({'families':res,'summary':dict(summary),
 'scope':'exact halfedge possibility; mu6 base no-T requires separate q6 theorem; unresolved not exclusion'},indent=2,sort_keys=True)+'\n')
