#!/usr/bin/env python3
"""Exact one-block screen for arbitrary H4(alpha), all normalized n8 orders.

No h1/cross phase equations are tested; passing branches are not transversals.
Same-group equations are linear in alpha or its inverse, with |alpha|=1.
"""
import datetime,hashlib,itertools,json,time
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
zero=(0,0,0,0);one=(1,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,b):
 v=[0]*4
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[(i+j)%4]+=(1 if i+j<4 else -1)*x*y
 return tuple(v)
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def conj(a):
 out=zero
 for i,x in enumerate(a):out=add(out,tuple(x*y for y in rt(-i)))
 return out
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
pairs=[(b,c)for b in range(4)for c in range(b+1,4)];Rs=list(itertools.permutations(range(1,8),3));cnt=Counter();samples={};start=time.monotonic()
for Otail in itertools.permutations(range(1,8)):
 O=(0,)+Otail;table={}
 for b,c in pairs:
  for d in range(1,8):
   part={-1:zero,0:zero,1:zero}
   for tau in range(8):
    t=O[tau]%4;v=rt(d*tau);v=tuple(sg[t][b]*sg[t][c]*x for x in v)
    e=ex[t][c]-ex[t][b];part[e]=add(part[e],v)
   assert part[-1]==zero or part[1]==zero
   if part[-1]!=zero:X,Y=part[-1],part[0] # multiply alpha
   else:X,Y=part[0],part[1]
   table[b,c,d]=(X,Y)
 for r in Rs:
  R=(0,)+r;num=den=None;valid=True
  for b,c in pairs:
   X,Y=table[b,c,(R[c]-R[b])%8]
   if X==zero and Y==zero:continue
   if X==zero or Y==zero:valid=False;break
   n=tuple(-x for x in X);d=Y
   if mul(n,conj(n))!=mul(d,conj(d)):valid=False;break
   if num is None:num,den=n,d
   elif mul(num,d)!=mul(n,den):valid=False;break
  if not valid:continue
  if num is None:key='free'
  else:
   roots=[k for k in range(8)if num==mul(rt(k),den)]
   key='root8_'+str(roots[0]) if roots else 'unit_nonroot8'
  cnt[key]+=1
  if key not in samples:samples[key]={'O':O,'R0':R,'numerator':num,'denominator':den}
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'elapsed_seconds':round(time.monotonic()-start,6),
 'orderings':5040,'R0_per_ordering':210,'feasible_h0_types':dict(cnt),'samples':samples,
 'scope':'only h0 equations; not a proof about h1/cross or transversals'}
(P/'frontier-20261028-n8-dita-generic-block-h0-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
