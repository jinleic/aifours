#!/usr/bin/env python3
"""Exploratory third-inner-product gcd screen for the T8B(z,z,z) slice.

For normalized T, rows 0,1,7 use columns 0,c,d. In addition to the two
adjacent Gram polynomials, row1/row7 gives a third polynomial with Delta6.
All modular N,D peeling is screening only; exact resultant replay is needed.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-t8b-diagonal-adjacent-gcd-v2.py';raw0=helper.read_bytes()
assert hashlib.sha256(raw0).hexdigest()=='3ce4c3c92c041f9699de9635b1529d75fc63ed903609853fa4ad53ffd15ca9d7'
exec(compile(raw0.decode().split('cnt=Counter();records=[];orders=0',1)[0],str(helper),'exec'),globals())
src=P/'frontier-20261028-t8b-diagonal-adjacent-gcd-retained-v2.jsonl';items=[json.loads(x)for x in src.read_text().splitlines()];assert len(items)==5856
cache={};cnt=Counter();ret=[]
def c0polys(O):
 if O in cache:return cache[O]
 out=[]
 for d in range(1,8):
  A=[[0]*4 for _ in range(13)]
  for t in range(8):
   B=T[t,O[t],d]
   for e in range(13):
    for j in range(4):A[e][j]+=B[e][j]
  nz=[i for i,v in enumerate(A)if any(v)];assert nz;A=A[min(nz):max(nz)+1]
  out.append((peel([sum(v[j]*pow(w,j,p)for j in range(4))%p for v in A]),peel([sum(v[j]*pow(wi,j,p)for j in range(4))%p for v in A])))
 cache[O]=out;return out
def third(O,c,d):
 v=[0]*13
 for tau in range(8):
  sc,kc,dc=K[O[tau]][c];sd,kd,dd=K[O[tau]][d];shift=kd-kc+3;z=pow(w,(6*tau)%8,p)
  for e,k in F[dd-dc].items():v[e+shift]=(v[e+shift]+sc*sd*k*z)%p
 while len(v)>1 and not v[0]:v=v[1:]
 return peel(v)
for row in items:
 O=tuple(row['O']);c,d=row['c'],row['d'];A,B=c0polys(O)[c-1][0],c0polys(O)[d-1][1];C=third(O,c,d)
 if not A[-1] or not B[-1] or C==[0] or not C[-1]:cnt['degenerate_mod']+=1;ret.append(row);continue
 g=gcd(gcd(A,B),C);degree=len(g)-1;cnt['gcd_degree_'+str(degree)]+=1
 if degree:ret.append(row)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(raw0).hexdigest(),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'input_pairs':len(items),'counts':dict(cnt),'retained':len(ret),
 'warning':'modular screen only; no exact no-go inferred'}
(P/'frontier-20261028-t8b-diagonal-third-gcd-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
(P/'frontier-20261028-t8b-diagonal-third-gcd-retained-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in ret))
print(json.dumps(obj,indent=2))
