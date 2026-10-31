#!/usr/bin/env python3
"""Exact 252 half-graphs for each published BH(10,q) representative."""
from collections import Counter
from functools import lru_cache
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent

def divide(a,b):
 a=a[:];out=[0]*(len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);v=a[-1];out[k]=v
  for j,u in enumerate(b):a[j+k]-=v*u
  while a and a[-1]==0:a.pop()
 assert not a
 return out
@lru_cache(None)
def phi(n):
 a=[-1]+[0]*(n-1)+[1]
 for d in range(1,n):
  if n%d==0:a=divide(a,phi(d))
 return a

def tables(q):
 f=phi(q);deg=len(f)-1
 def red(poly):
  a=poly[:]
  for i in range(len(a)-1,deg-1,-1):
   v=a[i]
   for j,c in enumerate(f):a[i-deg+j]-=v*c
  return tuple((a+[0]*deg)[:deg])
 powers=[red([0]*k+[1]) for k in range(q)]
 def iszero(seq):return all(sum(powers[x][j] for x in seq)==0 for j in range(deg))
 zero5={s for s in combinations_with_replacement(range(q),5) if iszero(s)}
 return iszero,zero5

def perfect(adj):
 @lru_cache(None)
 def rec(mask):
  if not mask:return ()
  b=mask&-mask;i=b.bit_length()-1;rest=mask^b;can=adj[i]&rest
  while can:
   c=can&-can;can-=c
   got=rec(rest^c)
   if got is not None:return ((i,c.bit_length()-1),)+got
  return None
 return rec((1<<10)-1)

allout=[];start=time.monotonic()
for q,expected in ((6,34),(10,51),(12,577),(15,1)):
 path=P/f'frontier-20261028-aalto-bh10-{q}-catalog-v1.txt'
 lines=path.read_text().splitlines();assert len(lines)==expected
 iszero,zero5=tables(q);subsets=list(combinations(range(10),5));summary=[];total=0
 for no,line in enumerate(lines,1):
  assert len(line)==106 and line[:3]=='BH1' and [ord(x)-48 for x in line[3:6]]==[10,10,q]
  a=[[ord(line[6+10*r+c])-48 for c in range(10)] for r in range(10)]
  assert all(0<=x<q for row in a for x in row)
  for c,d in combinations(range(10),2):assert iszero([(a[t][d]-a[t][c])%q for t in range(10)])
  diff=[[[(a[t][d]-a[t][c])%q for t in range(10)] for d in range(10)] for c in range(10)]
  good=[];hist=Counter()
  for E in subsets:
   adj=[0]*10
   for c,d in combinations(range(10),2):
    if tuple(sorted(diff[c][d][t] for t in E)) in zero5:
     adj[c]|=1<<d;adj[d]|=1<<c
   edges=sum(x.bit_count() for x in adj)//2;mat=perfect(adj)
   hist[edges]+=1
   if mat is not None:good.append({'even_half':list(E),'matching':[list(x) for x in mat]})
  total+=len(good)
  summary.append({'catalog_index_1based':no,'half_matching_count':len(good),
                  'first_matching':good[0] if good else None,'edge_count_histogram':dict(hist)})
  if no%100==0:print('q',q,'processed',no,'half_matchings_so_far',total,flush=True)
 print('q',q,'matrices',len(lines),'valid_BH_all',True,'matching_halves',total,flush=True)
 allout.append({'q':q,'matrix_count':len(lines),'total_matching_halves':total,'matrices':summary})
out={'source':'https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence',
     'scope':'exact finite catalog scan; matching is necessary, not sufficient for a transversal',
     'elapsed_seconds':time.monotonic()-start,'catalogs':allout}
(P/'frontier-20261028-aalto-halfgraph-census-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
