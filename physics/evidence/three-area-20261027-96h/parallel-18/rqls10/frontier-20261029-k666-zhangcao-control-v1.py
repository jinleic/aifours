#!/usr/bin/env python3
"""Exact cyclotomic check: Zhang-Cao Construction 3.3 (v=12) contains a K6,6,6 ONB edge representation."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
k=3;m=2*k;G=[(a,b)for a in range(2)for b in range(m)]
mu={}
for x in range(m):
 mu[(0,x)]=(1,0)if x==0 else (0,x)if x<=k-1 else (1,(x+1)%m)if x<=2*k-2 else (0,0)
 mu[(1,x)]=(1,(x+1)%m)if x<=k-2 else (0,k)if x==k-1 else (1,k)if x==k else (0,x)
assert sorted(mu.values())==G and sorted(((t[0]+mu[t][0])%2,(t[1]+mu[t][1])%m)for t in G)==G
# vectors as exponent tuples of zeta_12 (sign -1 = zeta^6, omega_6 = zeta^2); entries all unit, norm factor 1/12 squared.
def ex(g,t):return (6*g[0]*t[0]+2*g[1]*t[1])%12
def cell(i,j):return tuple((ex(i,mu[t])+ex(j,t))%12 for t in G)
def add(a,b):return((a[0]+b[0])%2,(a[1]+b[1])%m)
def sub(a,b):return((a[0]-b[0])%2,(a[1]-b[1])%m)
# inner product of two such vectors is (1/12) sum zeta^(b-a); exact zero test via Z[zeta12] with Phi12=x^4-x^2+1
def is_zero(diffs):
 c=[0]*12
 for d in diffs:c[d%12]+=1
 # reduce modulo x^12-1 to polynomial, then mod Phi12 = x^4 - x^2 + 1
 p=c[:]
 for deg in range(11,3,-1):
  q=p[deg]
  if q:p[deg]=0;p[deg-2]+=q;p[deg-4]-=q
 return all(x==0 for x in p[:4])
R=[g for g in G if g[0]==1];C=[g for g in G if g[0]==1];T=[g for g in G if g[0]==1]
edges=[]
for i in R:
 for j in C:edges.append((('r',i),('c',j),cell(i,j)))
for i in R:
 for t in T:j=add(i,t);assert j[0]==0;edges.append((('r',i),('t',t),cell(i,j)))
for j in C:
 for t in T:i=sub(j,t);assert i[0]==0;edges.append((('c',j),('t',t),cell(i,j)))
inc=collections.defaultdict(list)
for x,y,v in edges:inc[x].append(v);inc[y].append(v)
assert len(edges)==108 and len(inc)==18 and all(len(v)==12 for v in inc.values())
for vs in inc.values():
 for a,b in itertools.combinations(vs,2):assert is_zero([y-x for x,y in zip(a,b)])
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'construction':'Zhang-Cao Construction 3.3, v=12, G=Z2xZ6, Lemma 3.5 complete mapping k=3','vertices':len(inc),'edges':len(edges),
 'all_vertex_pairs_exactly_orthogonal_in_Q(zeta12)':True,'status':'PASS'}
(P/'frontier-20261029-k666-zhangcao-control-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
