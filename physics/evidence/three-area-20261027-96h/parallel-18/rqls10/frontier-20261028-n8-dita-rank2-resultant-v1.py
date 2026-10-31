#!/usr/bin/env python3
"""Reject one-free-block branches using fixed-degree determinant resultants.

4x4 cross minors have degree <=2 in x=alpha^-1 or beta because variable
entries occupy only two columns. A nonzero 4x4 Sylvester determinant mod p
certifies two exact minors have no common complex root. Unrejected=OPEN.
"""
import datetime,hashlib,itertools,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-freeblock-survivors-v1.jsonl';p=65521;w=57852
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
def mat(row,a,b):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[(pow(w,(R1[c]-R0[x])*loc[0][t]+h(M[t],c,b)-h(t,x,a),p)-pow(w,(R1[c]-R0[x])*loc[1][t]+h(M[t],c,b)-h(t,x,a),p))%p for t in range(4)] for x in range(4)for c in range(4)]
def det4(A):
 A=[r[:] for r in A];v=1
 for k in range(4):
  j=next((i for i in range(k,4) if A[i][k]),None)
  if j is None:return 0
  if j!=k:A[k],A[j]=A[j],A[k];v=-v
  x=A[k][k];v=v*x%p;inv=pow(x,-1,p)
  for i in range(k+1,4):
   f=A[i][k]*inv%p
   for j in range(k+1,4):A[i][j]=(A[i][j]-f*A[k][j])%p
 return v%p
def syl(a,b):
 a0,a1,a2=a;b0,b1,b2=b
 return det4([[a2,a1,a0,0],[0,a2,a1,a0],[b2,b1,b0,0],[0,b2,b1,b0]])
rows=list(itertools.combinations(range(16),4))[::23];half=pow(2,-1,p);counts=Counter();sur=[]
for line in src.read_text().splitlines():
 row=json.loads(line);a,b=row['alpha'],row['beta'];assert (a==-1)!=(b==-1)
 plus=mat(row,0 if a==-1 else a,0 if b==-1 else b);minus=mat(row,4 if a==-1 else a,4 if b==-1 else b)
 C0=[[(x+y)*half%p for x,y in zip(u,v)]for u,v in zip(plus,minus)]
 C1=[[(x-y)*half%p for x,y in zip(u,v)]for u,v in zip(plus,minus)]
 pool=[];cert=False
 for ids in rows:
  d0=det4([C0[i]for i in ids]);d1=det4([plus[i]for i in ids]);dm=det4([minus[i]for i in ids])
  poly=(d0,(d1-dm)*half%p,(d1+dm-2*d0)*half%p)
  if poly==(0,0,0):continue
  if any(syl(poly,q) for q in pool):cert=True;break
  if poly not in pool:pool.append(poly)
 if cert:counts['nonzero_sylvester']+=1
 else:counts['unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-rank2-resultant-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'prime':p,'counts':dict(counts),'unresolved':len(sur),'selected_minors':len(rows),'method':'fixed-degree quadratic Sylvester mod p'}
(P/'frontier-20261028-n8-dita-rank2-resultant-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
