#!/usr/bin/env python3
"""Exact finite-field certificates for the low-rank Diţă branches.

Choose independent constraint rows whose pivot minor is invertible at both
zeta and conjugate-zeta embeddings. For rank4, the 1d kernel must have
coordinate norms equal. For rank3, normalize two free unit coordinates as
1,z, set w=conj(z); the other three equal-norm equations are linear in z,w,
and z*w=1. A witnessed nonzero rational-function numerator is rigorous;
finite-field absence of points is NOT used as a proof.
"""
import collections,datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/'frontier-20261028-n10-dita-allorders-rank-scan-v1.jsonl'
records=[json.loads(x)for x in src.read_text().splitlines()]
assert len(records)==4000

def rref(A,p):
 A=[[(v%p)for v in row] for row in A];piv=[];row=0
 for col in range(len(A[0])):
  j=next((j for j in range(row,len(A))if A[j][col]),None)
  if j is None:continue
  A[row],A[j]=A[j],A[row];a=pow(A[row][col],-1,p);A[row]=[(x*a)%p for x in A[row]]
  for k in range(len(A)):
   if k!=row and A[k][col]:
    a=A[k][col];A[k]=[(x-a*y)%p for x,y in zip(A[k],A[row])]
  piv.append(col);row+=1
  if row==len(A):break
 return A,piv

def solve(A,b,p):
 n=len(A);R,piv=rref([row+[v]for row,v in zip(A,b)],p)
 assert piv[:n]==list(range(n))
 return [R[i][-1]for i in range(n)]

def basis_rows(M,p):
 selected=[];rank=0
 for i,row in enumerate(M):
  _,piv=rref([M[j]for j in selected]+[row],p)
  if len(piv)>rank:selected.append(i);rank+=1
  if rank==5:break
 _,cols=rref([M[j]for j in selected],p)
 return selected,cols

def matrix(q,z,p):
 powers=[pow(z,i,p)for i in range(10)];out=[]
 for b in range(5):
  for c in range(5):
   d=(q['g'][c]-q['f'][b])%10;k=(c-b)%5
   out.append([(powers[(d*a+2*t*k)%10]-powers[(d*aa+2*t*k)%10])%p for t,(a,aa) in enumerate(q['pairs'])])
 return out

def system(q,p,z):
 M=matrix(q,z,p);Mb=matrix(q,pow(z,-1,p),p)
 rows,cols=basis_rows(M,p);k=len(cols)
 if k==5:return 'rank5',{'p':p}
 free=[j for j in range(5)if j not in cols]
 A=[[M[i][j] for j in cols]for i in rows];Ab=[[Mb[i][j]for j in cols]for i in rows]
 if len(rref(Ab,p)[1])!=k:return None,None
 basis=[];basisb=[]
 for qcol in free:
  vals=solve(A,[(-M[i][qcol])%p for i in rows],p)
  valsb=solve(Ab,[(-Mb[i][qcol])%p for i in rows],p)
  v=[int(j==qcol)for j in range(5)];w=v.copy()
  for j,x,y in zip(cols,vals,valsb):v[j]=x;w[j]=y
  basis.append(v);basisb.append(w)
 cert={'p':p,'rows':rows,'pivot_columns':cols,'free_columns':free}
 if k==4:
  v=basis[0];vb=basisb[0];norm=[v[i]*vb[i]%p for i in range(5)];cert['norm_ratios_mod_p']=norm
  return ('unequal_norm' if len(set(norm))>1 else 'unresolved4'),cert
 if k!=3:return 'unresolved_lower',cert
 v,w=basis;vb,wb=basisb
 # a*z+b*zbar=c, with the free coordinates fixed to 1,z and |z|=1
 equations=[]
 for i in range(5):
  a=vb[i]*w[i]%p;b=v[i]*wb[i]%p;c=(1-v[i]*vb[i]-w[i]*wb[i])%p
  equations.append([a,b,c])
 R,piv=rref(equations,p);rc=len(rref([x[:2]for x in equations],p)[1]);ra=len(piv)
 cert.update(equations_mod_p=equations,linear_rank=rc,augmented_rank=ra)
 if ra>rc:return 'linear_inconsistent',cert
 if rc==2:
  x=R[0][2];y=R[1][2];cert['z_zbar_mod_p']=[x,y]
  return ('wrong_product' if x*y%p!=1 else 'unresolved3'),cert
 return 'unresolved3',cert

counts=collections.Counter();unresolved=[];out=P/'frontier-20261028-n10-dita-lowrank-modulus-v1.jsonl'
with out.open('w') as fp:
 for ix,q in enumerate(records):
  best=None
  for p,z in [(31,15),(41,4),(61,3),(71,14),(101,6)]:
   status,cert=system(q,p,z)
   if status is not None:
    best=(status,cert)
    if not status.startswith('unresolved'):break
  if best is None:best=('no_common_pivot',{})
  status,cert=best;counts[status]+=1
  entry={'branch':ix,'status':status,'certificate':cert};fp.write(json.dumps(entry,separators=(',',':'))+'\n')
  if status.startswith('unresolved') or status=='no_common_pivot':unresolved.append(ix)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'certificate_stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'branches':len(records),'counts':dict(counts),'unresolved_indices':unresolved}
(P/'frontier-20261028-n10-dita-lowrank-modulus-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='unresolved_indices'},indent=2));print('first unresolved:',unresolved[:10])
