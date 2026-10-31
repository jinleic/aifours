#!/usr/bin/env python3
"""Repair 800 modular-only rank3 findings with exact Q(zeta10) determinants."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/'frontier-20261028-n10-dita-allorders-rank-scan-v1.jsonl';aux=P/'frontier-20261028-n10-dita-lowrank-modulus-v1.jsonl'
Q=[json.loads(x)for x in src.read_text().splitlines()];C=[json.loads(x)for x in aux.read_text().splitlines()];assert len(Q)==len(C)==4000
Z=(0,0,0,0);ONE=(1,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 v=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 for i in range(6,3,-1):
  x=v[i];v[i-4]-=x;v[i-3]+=x;v[i-2]-=x;v[i-1]+=x
 return tuple(v[:4])
def det(A):
 n=len(A);z=Z
 for order in itertools.permutations(range(n)):
  x=ONE
  for i,j in enumerate(order):x=mul(x,A[i][j])
  inv=sum(order[i]>order[j]for i in range(n)for j in range(i+1,n))
  z=add(z,neg(x) if inv%2 else x)
 return z
R=[ONE]
for _ in range(9):
 a,b,c,d=R[-1];R.append((-d,a+d,b-d,c+d))
def val(a,p=31,z=15):return sum(v*pow(z,k,p)for k,v in enumerate(a))%p
def matrix(q):
 out=[]
 for b in range(5):
  for c in range(5):
   d=(q['g'][c]-q['f'][b])%10;k=(c-b)%5
   out.append([add(R[(d*a+2*t*k)%10],neg(R[(d*aa+2*t*k)%10])) for t,(a,aa) in enumerate(q['pairs'])])
 return out
out=P/'frontier-20261028-n10-dita-rank3-exact-zero-v1.jsonl';witnesses=0;unresolved=[];hist=collections.Counter()
with out.open('w') as f:
 for x in C:
  if x['status']!='linear_inconsistent':continue
  ix=x['branch'];q=Q[ix];cert=x['certificate'];rows=cert['rows'];cols=cert['pivot_columns'];free=cert['free_columns'];assert len(rows)==len(cols)==3 and len(free)==2
  M=matrix(q);A=[[M[r][c]for c in cols]for r in rows];pivot=det(A);assert val(pivot)!=0
  found=[]
  for j,col in enumerate(cols):
   ds=[]
   for qcol in free:
    B=[row.copy()for row in A]
    for a,r in enumerate(rows):B[a][j]=M[r][qcol]
    ds.append(det(B))
   if ds==[Z,Z]:found.append(col)
  if found:witnesses+=1;hist[str(found[0])]+=1
  else:unresolved.append(ix)
  f.write(json.dumps({'branch':ix,'rows':rows,'pivot_columns':cols,'pivot_determinant':pivot,'pivot_nonzero_mod31':val(pivot),'forced_zero_columns':found},separators=(',',':'))+'\n')
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scan_stream_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'modulus_stream_sha256':hashlib.sha256(aux.read_bytes()).hexdigest(),'certificate_stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rank3_cases':witnesses+len(unresolved),'exact_zero_coordinate_witnesses':witnesses,'witness_histogram':dict(hist),'unresolved_indices':unresolved}
(P/'frontier-20261028-n10-dita-rank3-exact-zero-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
