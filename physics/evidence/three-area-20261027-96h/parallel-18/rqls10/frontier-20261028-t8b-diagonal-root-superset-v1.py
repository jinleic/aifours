#!/usr/bin/env python3
"""Exact finite candidate polynomial superset for T8B(z,z,z) Fourier T.

Fix source row0 at coordinate0 by coordinate rotation and T cell (0,0) by
physical row shift. Its next physical row must choose c=1..7. Form the
seven adjacent Gram polynomials for every 7! ordering. Normalize by a
nonzero z power, integer gcd and zeta8 unit scalar; zero roots are excluded.
"""
import datetime,hashlib,itertools,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
rows=[['1','1','1','1','1','1','1','1'],['1','-1','-d','-c','d','c','cd','-cd'],['1','-a','-1','c','a','-ac','-c','ac'],['1','a','d','-1','ad','-a','-d','-ad'],['1','b','-b','-bc','-1','-c','c','bc'],['1','-b','bd','b','-d','-1','d','-bd'],['1','-ab','b','-b','-a','a','-1','ab'],['1','ab','-bd','bc','-ad','ac','-cd','-abcd']]
def tok(s):
 q=-1 if s.startswith('-')else 1;s=s.lstrip('-');return q,sum(s.count(x)for x in 'abc'),s.count('d')
K=[[tok(s)for s in row]for row in rows]
F={1:{0:1,2:6,4:9},0:{1:3,3:10,5:3},-1:{2:9,4:6,6:1}}
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def mulroot(v,k):
 out=[0]*4
 for i,x in enumerate(v):
  r=rt(i+k)
  for j in range(4):out[j]+=x*r[j]
 return tuple(out)
T={}
for t in range(8):
 for s in range(8):
  for d in range(1,8):
   sc,kc,dc=K[s][0];sd,kd,dd=K[s][d];shift=kd-kc+3;A=[[0]*4 for _ in range(13)];v=rt(t)
   for e,q in F[dd-dc].items():
    for j in range(4):A[e+shift][j]+=sc*sd*q*v[j]
   T[t,s,d]=A
unique=set();zero=0;orders=0;maxdegree=0
for perm in itertools.permutations(range(1,8)):
 O=(0,)+perm;orders+=1
 for d in range(1,8):
  A=[[0]*4 for _ in range(13)]
  for t in range(8):
   q=T[t,O[t],d]
   for e in range(13):
    for j in range(4):A[e][j]+=q[e][j]
  nz=[i for i,v in enumerate(A)if any(v)]
  if not nz:zero+=1;continue
  low,high=min(nz),max(nz);maxdegree=max(maxdegree,high);A=A[low:high+1]
  g=math.gcd(*(abs(x)for v in A for x in v));A=[tuple(x//g for x in v)for v in A]
  # Multiplication by any eighth root is a nonzero scalar in Q(zeta8).
  canonical=min(tuple(mulroot(v,k)for v in A)for k in range(8));unique.add(canonical)
polys=sorted(unique);totaldeg=sum(len(q)-1 for q in polys)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source':'https://arxiv.org/html/2505.22947v1 Proposition3.2 T8B',
 'orders':orders,'next_columns_per_order':7,'identity_polynomials':zero,'max_raw_degree':maxdegree,
 'distinct_normalized_polynomials':len(polys),'sum_normalized_degrees':totaldeg,'polynomials':polys}
(P/'frontier-20261028-t8b-diagonal-root-superset-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({k:v for k,v in obj.items()if k!='polynomials'},indent=2))
