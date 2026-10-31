#!/usr/bin/env python3
"""Exploratory modular gcd of two necessary adjacent Gram polynomials.

For a putative T normalized to row0/column0, row1 uses c and row7 uses d,
c!=d. Their +1/-1 Gram equations give P_c(z)=0 and sigma(P_d)(z)=0,
where sigma conjugates zeta8 coefficients, not the variable z. Modular gcd
is only a screen: zero/nonzero findings need exact resultant/replay.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-t8b-diagonal-root-superset-v1.py';helper_raw=helper.read_bytes()
assert hashlib.sha256(helper_raw).hexdigest()=='17e28e2f6c8d437f2d6b420e3bec07422a65ec6f225bb2b6f8ae233b36be098a'
exec(compile(helper_raw.decode().split('unique=set();zero=0;',1)[0],str(helper),'exec'),globals())
p=65521;w=57852;wi=pow(w,-1,p)
def trim(v):
 while len(v)>1 and not v[-1]:v.pop()
 return v
def rem(a,b):
 a=trim(a[:]);b=trim(b[:]);inv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  d=len(a)-len(b);k=a[-1]*inv%p
  for i,x in enumerate(b):a[d+i]=(a[d+i]-k*x)%p
  trim(a)
 return a
def gcd(a,b):
 a=trim(a[:]);b=trim(b[:])
 while b!=[0]:a,b=b,rem(a,b)
 return a
cnt=Counter();records=[];orders=0
for perm in itertools.permutations(range(1,8)):
 O=(0,)+perm;orders+=1;polys=[]
 for d in range(1,8):
  A=[[0]*4 for _ in range(13)]
  for t in range(8):
   B=T[t,O[t],d]
   for e in range(13):
    for j in range(4):A[e][j]+=B[e][j]
  nz=[i for i,v in enumerate(A)if any(v)];assert nz
  A=A[min(nz):max(nz)+1]
  plus=[sum(v[j]*pow(w,j,p)for j in range(4))%p for v in A]
  minus=[sum(v[j]*pow(wi,j,p)for j in range(4))%p for v in A]
  polys.append((plus,minus))
 for c in range(7):
  for d in range(7):
   if c==d:continue
   A,B=polys[c][0],polys[d][1]
   if not A[-1] or not B[-1]:cnt['leading_drop']+=1;records.append({'O':O,'c':c+1,'d':d+1,'kind':'leading_drop'});continue
   g=gcd(A,B);degree=len(g)-1;cnt['gcd_degree_'+str(degree)]+=1
   if degree:records.append({'O':O,'c':c+1,'d':d+1,'kind':'common_mod','degree':degree})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(helper_raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'prime':p,'orders':orders,'ordered_pairs_per_order':42,'counts':dict(cnt),'retained':len(records),
 'warning':'modular gcd screen only; no exact no-go inferred'}
(P/'frontier-20261028-t8b-diagonal-adjacent-gcd-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
(P/'frontier-20261028-t8b-diagonal-adjacent-gcd-retained-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in records))
print(json.dumps(obj,indent=2))
