#!/usr/bin/env python3
"""Reject n8 Diţă rank-3 branches by exact modular cofactor norm inequalities.

Cofactors of the same selected 3 rows at zeta8=w and conjugate zeta8=w^-1
are reductions of one algebraic kernel vector and its conjugate. Unequal
cofactor norm reductions prove the required unit-phase vector cannot exist.
Equal reductions are retained, not claimed feasible. Source census is required.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-allphase-singular-v1.jsonl';prime=65521;w=57852
assert pow(w,4,prime)==prime-1;wi=pow(w,-1,prime)
def matrix(row,w):
 O,R0,R1,M=row['O'],row['R0'],row['R1'],row['mu'];loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[(pow(w,(R1[c]-R0[b])*loc[0][t]+2*(M[t]*c-t*b),prime)-pow(w,(R1[c]-R0[b])*loc[1][t]+2*(M[t]*c-t*b),prime))%prime for t in range(4)]for b in range(4)for c in range(4)]
def pivots(A):
 B=[];ix=[]
 for i,row in enumerate(A):
  v=row[:]
  for k,b in B:
   h=v[k];v=[(a-h*c)%prime for a,c in zip(v,b)]
  p=next((j for j,x in enumerate(v)if x),None)
  if p is None:continue
  inv=pow(v[p],-1,prime);v=[x*inv%prime for x in v];B.append((p,v));ix.append(i)
  if len(ix)==3:return ix
 raise AssertionError('unexpected rank')
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%prime
def cof(M,ix):
 out=[]
 for k in range(4):
  cols=[j for j in range(4)if j!=k];a=[[M[i][j]for j in cols]for i in ix]
  x=det3(a);out.append(x if k%2==0 else (-x)%prime)
 return out
cnt=Counter();sample=[];sur=[]
for line in src.read_text().splitlines():
 row=json.loads(line);A=matrix(row,w);B=matrix(row,wi);ix=pivots(A);u=cof(A,ix);v=cof(B,ix)
 assert any(u) and all(sum(a*b for a,b in zip(R,u))%prime==0 for R in A)
 norms=[a*b%prime for a,b in zip(u,v)]
 if len(set(norms))>1:cnt['unequal_norms_excluded']+=1
 elif not norms[0]:cnt['all_zero_reduction_unresolved']+=1;sur.append(row)
 else:cnt['equal_nonzero_unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-unit-kernel-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'prime':prime,'root':w,'conjugate_root':wi,
 'counts':dict(cnt),'retained':len(sur)}
(P/'frontier-20261028-n8-dita-unit-kernel-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
