#!/usr/bin/env python3
"""Discharge root-specializations forced by exact separable bivariate minors.

A rank4 or unequal-norm 3-minor or inconsistent remaining linear phase
system mod p is exact no-solution. Other branches are retained. Root lists
are 0 excluded: x=alpha^-1, y=beta. Does not rerun original census.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/'frontier-20261028-n8-dita-freefree-survivors-v1.jsonl';cert=P/'frontier-20261028-n8-dita-freefree-separable-full-certs-v1.jsonl';p=65521;w=57852;wi=pow(w,-1,p)
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
def mat(row,a,b,w):
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
  if len(ids)==4:break
 return ids
def det3(a):return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
def cof(A,ids):
 z=[]
 for k in range(4):
  cols=[j for j in range(4)if j!=k];d=det3([[A[i][j]for j in cols]for i in ids]);z.append(d if k%2==0 else -d%p)
 return z
T=[json.loads(x)for x in src.read_text().splitlines()];Q=[json.loads(x)for x in cert.read_text().splitlines()];assert len(T)==len(Q)==30720
cnt=Counter();sur=[];special=0
for ix,(original,gate) in enumerate(zip(T,Q)):
 if gate is None:cnt['no_separable_gate']+=1;continue
 if not gate['x_roots'] and not gate['y_roots']:cnt['nonzero_monomial']+=1;continue
 cases=[((-k)%8,-1)for k in gate['x_roots']]+[(-1,k)for k in gate['y_roots']]
 for a,b in cases:
  special+=1;row={**original,'alpha':a,'beta':b,'parent_index':ix}
  keep=[r for r in range(16)if ((r//4)%2==0 if a==-1 else r%2==0)]
  C=mat(row,0 if a==-1 else a,0 if b==-1 else b,w);Cb=mat(row,0 if a==-1 else a,0 if b==-1 else b,wi)
  ids0=pivots([C[r]for r in keep]);rank=len(ids0)
  if rank==4:cnt['rank4']+=1;continue
  if rank<3:cnt['rank_below3_unresolved']+=1;sur.append(row);continue
  ids=[keep[i]for i in ids0];v=cof(C,ids);vb=cof(Cb,ids)
  if len({x*y%p for x,y in zip(v,vb)})>1:cnt['unequal_norm']+=1;continue
  minus=mat(row,4 if a==-1 else a,4 if b==-1 else b,w)
  U=[sum(x*y for x,y in zip(q,v))%p for q in C];V=[sum(x*y for x,y in zip(q,v))%p for q in minus]
  A=[(x+y)%p for x,y in zip(U,V)];B=[(x-y)%p for x,y in zip(U,V)]
  if any(A[i]*B[j]%p!=A[j]*B[i]%p for i in range(16)for j in range(i+1,16)):
   cnt['inconsistent_linear']+=1;continue
  if not any(B) and any(A):cnt['nonzero_constant']+=1;continue
  cnt['linear_unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-freefree-specializations-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'gate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'specializations':special,'counts':dict(cnt),'unresolved':len(sur)}
(P/'frontier-20261028-n8-dita-freefree-specializations-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
