#!/usr/bin/env python3
"""Regenerate generic Diţă branch coverage from independently matching H4 tables.

For h1 transform O by mu and translate R1 to put its first entry at zero;
lookup the exact independently matching all-h0 table. Regenerate all
same-group branches, modular rank/norm gates, and explicit residual lists.
Terminal algebraic gates are separate and must be replayed separately.
"""
import datetime,hashlib,itertools,json,time
from collections import Counter
from functools import lru_cache
from pathlib import Path
P=Path(__file__).resolve().parent;table=P/'frontier-20261028-n8-dita-generic-h0-table-py-v1.txt';raw=table.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='5abdc4aebf774d3491215ac68dd71ae4d158d9c72ccaabda63cc5905e10a10c5'
rec=[];lookup={}
for line in raw.decode().splitlines():
 o,r,k=line.split();key=(tuple(map(int,o)),tuple(map(int,r)));lookup[key]=int(k);rec.append((key[0],key[1],int(k)))
assert len(rec)==len(lookup)==14592
p=65521;w=57852;wi=8031;W=[pow(w,i,p)for i in range(8)];WB=[pow(wi,i,p)for i in range(8)]
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
@lru_cache(maxsize=65521)
def inv(x):return pow(x,-1,p)
def cross(O,R0,R1,M,a,b,W,mask):
 loc=[[0]*4 for _ in range(2)]
 for t,j in enumerate(O):loc[j//4][j%4]=t
 out=[]
 for x in range(4):
  for y in range(4):
   if (mask==1 and x%2) or (mask==2 and y%2):out.append([0]*4);continue
   de=R1[y]-R0[x];v=[]
   for t in range(4):
    h0=(de*loc[0][t]+h(M[t],y,b)-h(t,x,a))%8;h1=(de*loc[1][t]+h(M[t],y,b)-h(t,x,a))%8
    v.append((W[h0]-W[h1])%p)
   out.append(v)
 return out
def pivot(A):
 basis=[];ids=[]
 for i,row in enumerate(A):
  v=row[:]
  for k,b in basis:
   t=v[k]
   if t:v=[(x-t*y)%p for x,y in zip(v,b)]
  k=next((j for j,x in enumerate(v)if x),None)
  if k is None:continue
  q=inv(v[k]);v=[x*q%p for x in v];basis.append((k,v));ids.append(i)
  if len(ids)==4:break
 return ids
def det3(a):return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
def cof(A,ids):
 out=[]
 for omit in range(4):
  cols=[j for j in range(4)if j!=omit];d=det3([[A[r][j]for j in cols]for r in ids]);out.append(d if omit%2==0 else -d%p)
 return out
cnt=Counter();residual=[];FF=[];start=time.monotonic();muall=[(0,)+m for m in itertools.permutations((1,2,3))]
for O,R0,a in rec:
 rest=[x for x in range(1,8)if x not in R0[1:]]
 for R1 in itertools.permutations(rest):
  R1p=tuple((r-R1[0])%8 for r in R1)
  for M in muall:
   Op=tuple(4*(x//4)+M[x%4] for x in O);b=lookup.get((Op,R1p))
   if b is None:continue
   cnt['both']+=1;row={'O':O,'R0':R0,'R1':R1,'mu':M}
   if a<0 and b<0:cnt['free_free']+=1;FF.append(row);continue
   mode=1 if a<0 else 2 if b<0 else 0
   cnt['free_fixed' if mode==1 else 'fixed_free' if mode==2 else 'fixed_fixed']+=1
   aa=0 if a<0 else a;bb=0 if b<0 else b
   C=cross(O,R0,R1,M,aa,bb,W,mode);ids=pivot(C);r=len(ids)
   if r==4:cnt['rank4']+=1;cnt['free_rank4']+=(mode!=0);continue
   reject=False
   if r==3:
    v=cof(C,ids);vb=cof(cross(O,R0,R1,M,aa,bb,WB,mode),ids)
    reject=len({x*y%p for x,y in zip(v,vb)})>1
   if reject:cnt['unequal_norm']+=1;cnt['free_unequal_norm']+=(mode!=0);continue
   cnt['unresolved']+=1;cnt['free_unresolved']+=(mode!=0)
   residual.append({**row,'alpha':a,'beta':b,'modrank':r})
(P/'frontier-20261028-n8-dita-generic-full-replay-unresolved-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in residual))
(P/'frontier-20261028-n8-dita-generic-full-replay-freefree-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in FF))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'table_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'elapsed_seconds':round(time.monotonic()-start,6),'counts':dict(cnt),'residual':len(residual),'freefree':len(FF)}
(P/'frontier-20261028-n8-dita-generic-full-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
