#!/usr/bin/env python3
"""Eliminate 2-free-phase n8 branches using parity-block kernel invariants.

Each 2x2 parity block of cross equations is C0 diag(x^(bp*t%2)
 y^(cp*mu(t)%2)). Rank4 or unequal cofactor norms forbids unit delta.
Rank3 block-pair ratios and balanced quartic products yield x,y-independent
necessary identities. A nonzero mod-p residue is an exact rejection.
"""
import datetime,hashlib,itertools,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-freefree-branches-v1.jsonl';p=65521;w=57852;wi=pow(w,-1,p)
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
def mat(row,bp,cp,w):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[(sg[t][b]*sg[M[t]][c]*(pow(w,(R1[c]-R0[b])*loc[0][t],p)-pow(w,(R1[c]-R0[b])*loc[1][t],p)))%p for t in range(4)] for b in range(bp,4,2)for c in range(cp,4,2)]
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
counts=Counter();sur=[]
for line in src.read_text().splitlines():
 row=json.loads(line);mu=row['mu'];blocks=[];reject=None
 for bp,cp in itertools.product(range(2),repeat=2):
  C=mat(row,bp,cp,w);ids=pivots(C)
  if len(ids)==4:reject='block_rank4';break
  if len(ids)==3:
   v=cof(C,ids);Cb=mat(row,bp,cp,wi);vb=cof(Cb,ids)
   if len({a*b%p for a,b in zip(v,vb)})>1:reject='unequal_unit_norms';break
   blocks.append((bp,cp,v))
 if reject:counts[reject]+=1;continue
 for A,B in itertools.combinations(blocks,2):
  bp,cp,v=A;bq,cq,u=B;db=bp-bq;dc=cp-cq
  for i,j in itertools.combinations(range(4),2):
   if (not db or i%2==j%2) and (not dc or mu[i]%2==mu[j]%2):
    if (v[i]*u[j]-v[j]*u[i])%p:reject='phase_invariant_pair';break
  if reject:break
  pairs=list(itertools.combinations(range(4),2))
  for (i,j),(k,l) in itertools.combinations(pairs,2):
   if (not db or i%2+j%2==k%2+l%2) and (not dc or mu[i]%2+mu[j]%2==mu[k]%2+mu[l]%2):
    if (v[i]*v[j]*u[k]*u[l]-v[k]*v[l]*u[i]*u[j])%p:reject='phase_invariant_quartic';break
  if reject:break
 if reject:counts[reject]+=1
 else:counts['unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-freefree-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'prime':p,'counts':dict(counts),'unresolved':len(sur)}
(P/'frontier-20261028-n8-dita-freefree-gate-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
