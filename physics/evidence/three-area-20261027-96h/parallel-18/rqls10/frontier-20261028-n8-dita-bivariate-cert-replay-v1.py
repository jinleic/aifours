#!/usr/bin/env python3
"""Independent exact replay of all bivariate separable/binomial certificates.

Recover each (<=2,<=2) determinant by exact interpolation on {0,1,-1}²,
not producer monomial expansion. Check cofactor identities by ten-point
exact evaluation (degree<=9), not producer symbolic expansion.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/'frontier-20261028-n8-dita-freefree-replay-survivors-v1.jsonl'
sep=P/'frontier-20261028-n8-dita-freefree-separable-full-certs-v1.jsonl'
bsrc=P/'frontier-20261028-n8-dita-freefree-separable-full-survivors-v1.jsonl'
bin=P/'frontier-20261028-n8-dita-freefree-binomial-full-certs-v1.jsonl'
T=[json.loads(s)for s in src.read_text().splitlines()];Q=[json.loads(s)for s in sep.read_text().splitlines()];B=[json.loads(s)for s in bin.read_text().splitlines()]
assert len(T)==len(Q)==30720 and len(B)==2048
assert hashlib.sha256(src.read_bytes()).hexdigest()=='65a3bacaf8c2feaae3e0d72b00d80b9f51a227130369d09a7e56ec4beb4dfe93'
extract=''.join(json.dumps(t,separators=(',',':'))+'\n' for t,q in zip(T,Q) if q is None).encode();assert extract==bsrc.read_bytes()
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];Z=(0,0,0,0);ONE=(1,0,0,0)
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,k):return tuple(x*k for x in a)
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b3-a2*b2-a3*b1,a0*b1+a1*b0-a2*b3-a3*b2,a0*b2+a1*b1+a2*b0-a3*b3,a0*b3+a1*b2+a2*b1+a3*b0)
per4=[(q,-1 if sum(q[i]>q[j]for i in range(4)for j in range(i+1,4))%2 else 1)for q in itertools.permutations(range(4))]
per3=[(q,-1 if sum(q[i]>q[j]for i in range(3)for j in range(i+1,3))%2 else 1)for q in itertools.permutations(range(3))]
def base(row):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[scale(sub(rt((R1[c]-R0[b])*loc[0][t]),rt((R1[c]-R0[b])*loc[1][t])),sg[t][b]*sg[M[t]][c])for t in range(4)]for b in range(4)for c in range(4)]
def det(A,per):
 out=Z
 for q,sign in per:
  v=ONE
  for i,t in enumerate(q):v=mul(v,A[i][t])
  out=add(out,scale(v,sign))
 return out
def minorval(C,M,ids,x,y):
 A=[]
 for r in ids:
  b,c=divmod(r,4);A.append([scale(C[r][t],x**((b%2)*(t%2))*y**((c%2)*(M[t]%2)))for t in range(4)])
 return det(A,per4)
def interp(vals):
 d0,d1,dm=vals;return [scale(d0,2),sub(d1,dm),sub(add(d1,dm),scale(d0,2))]
def poly(C,M,ids):
 # First interpolate x (factor2), then y (another factor2).
 a=[interp([minorval(C,M,ids,x,y)for x in (0,1,-1)])for y in (0,1,-1)]
 byx=[interp([a[j][i]for j in range(3)])for i in range(3)]
 return [byx[i][j]for i in range(3)for j in range(3)]
def factors(a):
 a=a[:];out=[]
 while len(a)>1 and a[-1]==Z:a.pop()
 if a==[Z]:return None
 for k in [-1]+list(range(8)):
  r=Z if k==-1 else rt(k)
  while len(a)>1:
   q=[Z]*(len(a)-1);q[-1]=a[-1]
   for i in range(len(q)-2,-1,-1):q[i]=add(a[i+1],mul(r,q[i+1]))
   if add(a[0],mul(r,q[0]))!=Z:break
   out.append(k);a=q
   while len(a)>1 and a[-1]==Z:a.pop()
 return out if len(a)==1 and a[0]!=Z else None
def cofactval(C,M,ids,omit,k,eps,y):
 cols=[t for t in range(4)if t!=omit];A=[]
 for r in ids:
  b,c=divmod(r,4);rr=[]
  for t in cols:
   ax=(b%2)*(t%2);by=(c%2)*(M[t]%2);deg=eps*ax+by+(1 if eps==-1 else 0)
   rr.append(scale(mul(C[r][t],rt(k*ax)),y**deg))
  A.append(rr)
 return det(A,per3)
start=time.monotonic();nsep=nbin=0;bi=0
for row,q in zip(T,Q):
 C=base(row);M=row['mu']
 if q is not None:
  z=poly(C,M,q['rows']);pivot=next(i for i,v in enumerate(z)if v!=Z);i,j=divmod(pivot,3);a=z[pivot];f=[z[3*t+j]for t in range(3)];g=[z[3*i+t]for t in range(3)]
  assert all(mul(z[3*t+u],a)==mul(f[t],g[u])for t in range(3)for u in range(3))
  fx,fy=factors(f),factors(g);assert fx is not None and fy is not None
  assert sorted(set(k for k in fx if k>=0))==q['x_roots'] and sorted(set(k for k in fy if k>=0))==q['y_roots'];nsep+=1;continue
 q=B[bi];bi+=1;assert q is not None
 z=poly(C,M,q['minor_rows']);nz=[(divmod(i,3),v)for i,v in enumerate(z)if v!=Z];assert len(nz)==2
 (i,j),a=nz[0];(k,l),b=nz[1]
 if i<k:(i,j),a,(k,l),b=(k,l),b,(i,j),a
 d=i-k;assert d in (1,2) and abs(j-l)==d;eps=1 if j-l==-d else -1;assert eps==q['relation_y_power']
 ks=[k for k in range(8)if add(mul(a,rt(k*d)),b)==Z];assert len(ks)==d and ks==[v['k']for v in q['branches']]
 for v in q['branches']:
  ids=v['rows'];zidx=v['zero_coordinate'];midx=v['nonzero_cofactor'];deg=v['monomial_degree'];assert 0<=deg<=9
  c=cofactval(C,M,ids,midx,v['k'],eps,1);assert c!=Z
  for y in range(10):
   assert cofactval(C,M,ids,zidx,v['k'],eps,y)==Z
   assert cofactval(C,M,ids,midx,v['k'],eps,y)==scale(c,y**deg)
 nbin+=1
assert bi==nbin==2048 and nsep==28672
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_cases_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'separable_certs_sha256':hashlib.sha256(sep.read_bytes()).hexdigest(),
 'binomial_certs_sha256':hashlib.sha256(bin.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.monotonic()-start,6),
 'separable_checked':nsep,'binomial_checked':nbin,'cofactor_test_points':10,'status':'PASS'}
(P/'frontier-20261028-n8-dita-bivariate-cert-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
