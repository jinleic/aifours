#!/usr/bin/env python3
"""Exact modular consistency gate for one FREE H4 block parameter.

A phase-independent subset has rank 3, so any solution's delta is the
cofactor kernel v. The remaining equations are A_i+x B_i=0 with x=alpha^-1
or beta. A nonzero 2x2 determinant of (A,B) mod p rules out every x over C.
Unrejected branches remain OPEN; no completeness inference is made.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-generic-rank-unresolved-v2.jsonl';p=65521;w=57852
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
def mat(row,a,b):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[(pow(w,(R1[c]-R0[x])*loc[0][t]+h(M[t],c,b)-h(t,x,a),p)-pow(w,(R1[c]-R0[x])*loc[1][t]+h(M[t],c,b)-h(t,x,a),p))%p for t in range(4)] for x in range(4)for c in range(4)]
def pivots(A):
 basis=[];ids=[]
 for i,row in enumerate(A):
  v=row[:]
  for k,z in basis:
   f=v[k];v=[(x-f*y)%p for x,y in zip(v,z)]
  k=next((j for j,x in enumerate(v)if x),None)
  if k is None:continue
  v=[x*pow(v[k],-1,p)%p for x in v];basis.append((k,v));ids.append(i)
  if len(ids)==3:break
 return ids
def det3(a):return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
def cof(A,ids):
 z=[]
 for k in range(4):
  cols=[j for j in range(4)if j!=k];d=det3([[A[i][j]for j in cols]for i in ids]);z.append(d if k%2==0 else -d%p)
 return z
counts=Counter();sur=[]
for line in src.read_text().splitlines():
 row=json.loads(line);a,b=row['alpha'],row['beta'];assert (a==-1) != (b==-1)
 plus=mat(row,0 if a==-1 else a,0 if b==-1 else b)
 minus=mat(row,4 if a==-1 else a,4 if b==-1 else b)
 keep=[r for r in range(16)if ((r//4)%2==0 if a==-1 else r%2==0)]
 subset=[plus[r]for r in keep];ids0=pivots(subset)
 if len(ids0)<3:counts['subset_rank_below3_unresolved']+=1;sur.append(row);continue
 ids=[keep[i]for i in ids0];v=cof(plus,ids);assert any(v)
 assert all(sum(x*y for x,y in zip(plus[r],v))%p==0 for r in keep)
 U=[sum(x*y for x,y in zip(q,v))%p for q in plus];V=[sum(x*y for x,y in zip(q,v))%p for q in minus]
 A=[(x+y)%p for x,y in zip(U,V)];B=[(x-y)%p for x,y in zip(U,V)]
 if any(A[i]*B[j]%p!=A[j]*B[i]%p for i in range(16)for j in range(i+1,16)):
  counts['inconsistent_linear_phase']+=1;continue
 if not any(B) and any(A):counts['nonzero_constant']+=1;continue
 counts['unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-freeblock-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'prime':p,'root':w,'counts':dict(counts),'unresolved':len(sur)}
(P/'frontier-20261028-n8-dita-freeblock-gate-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
