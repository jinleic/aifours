#!/usr/bin/env python3
"""Independently replay univariate minor factors and fixed-root rejections.

Exact zeta8 integer-basis determinants at x=0,+1,-1 interpolate degree<=2.
Fixed roots are tested first mod97, with mod65521 fallback if needed.
"""
import datetime,hashlib,itertools,json,time
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
sources=[('onefree',P/'frontier-20261028-n8-dita-rank2-resultant-survivors-v1.jsonl',P/'frontier-20261028-n8-dita-rank2-root-certificates-v1.jsonl',8192),('ff',P/'frontier-20261028-n8-dita-freefree-specializations-survivors-v1.jsonl',P/'frontier-20261028-n8-dita-ff-specialized-root-certificates-v1.jsonl',7168)]
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]];Z=(0,0,0,0);ONE=(1,0,0,0)
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,n):return tuple(x*n for x in a)
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b;return (a0*b0-a1*b3-a2*b2-a3*b1,a0*b1+a1*b0-a2*b3-a3*b2,a0*b2+a1*b1+a2*b0-a3*b3,a0*b3+a1*b2+a2*b1+a3*b0)
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
perms=[(q,-1 if sum(q[i]>q[j]for i in range(4)for j in range(i+1,4))%2 else 1)for q in itertools.permutations(range(4))]
def det(A):
 out=Z
 for q,s in perms:
  v=ONE
  for i,j in enumerate(q):v=mul(v,A[i][j])
  out=add(out,scale(v,s))
 return out
def exactmat(row,a,b):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[sub(rt((R1[c]-R0[x])*loc[0][t]+h(M[t],c,b)-h(t,x,a)),rt((R1[c]-R0[x])*loc[1][t]+h(M[t],c,b)-h(t,x,a)))for t in range(4)]for x in range(4)for c in range(4)]
def factors(poly):
 poly=poly[:];out=[]
 while len(poly)>1 and poly[-1]==Z:poly.pop()
 if poly==[Z]:return None
 for k in [-1]+list(range(8)):
  x=Z if k==-1 else rt(k)
  while len(poly)>1:
   q=[Z]*(len(poly)-1);q[-1]=poly[-1]
   for i in range(len(q)-2,-1,-1):q[i]=add(poly[i+1],mul(x,q[i+1]))
   if add(poly[0],mul(x,q[0]))!=Z:break
   out.append(k);poly=q
   while len(poly)>1 and poly[-1]==Z:poly.pop()
 return out if len(poly)==1 and poly[0]!=Z else None
def rank_ids(A,p):
 B=[];ids=[]
 for i,row in enumerate(A):
  v=row[:]
  for j,z in B:
   k=v[j];v=[(x-k*y)%p for x,y in zip(v,z)]
  j=next((j for j,x in enumerate(v)if x),None)
  if j is None:continue
  u=pow(v[j],-1,p);B.append((j,[x*u%p for x in v]));ids.append(i)
  if len(ids)==4:break
 return ids
def det3(a,p):return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
def cof(A,ids,p):
 out=[]
 for k in range(4):
  cols=[j for j in range(4)if j!=k];v=det3([[A[i][j]for j in cols]for i in ids],p);out.append(v if k%2==0 else -v%p)
 return out
def fixed_gate(E,p,w):
 vals=[pow(w,i,p)for i in range(4)];valsbar=[pow(pow(w,-1,p),i,p)for i in range(4)]
 A=[[sum(q[i]*vals[i]for i in range(4))%p for q in row]for row in E];ids=rank_ids(A,p)
 if len(ids)==4:return 'rank4'
 if len(ids)<3:return None
 B=[[sum(q[i]*valsbar[i]for i in range(4))%p for q in row]for row in E];u=cof(A,ids,p);v=cof(B,ids,p)
 return 'unequal_norm' if len({x*y%p for x,y in zip(u,v)})>1 else None
assert all(97%d for d in range(2,10));w97=next(pow(g,12,97)for g in range(2,97)if pow(pow(g,12,97),4,97)==96)
assert pow(57852,4,65521)==65520
cnt=Counter();start=time.monotonic()
for name,src,cert,n in sources:
 T=[json.loads(x)for x in src.read_text().splitlines()];Q=[json.loads(x)for x in cert.read_text().splitlines()];assert len(T)==len(Q)==n
 for row,q in zip(T,Q):
  assert q is not None;a,b=row['alpha'],row['beta'];assert (a==-1)!=(b==-1)
  plus=exactmat(row,0 if a==-1 else a,0 if b==-1 else b);minus=exactmat(row,4 if a==-1 else a,4 if b==-1 else b);ids=q['minor_rows']
  A0=[[add(x,y)for x,y in zip(plus[r],minus[r])]for r in ids];A1=[[scale(x,2)for x in plus[r]]for r in ids];Am=[[scale(x,2)for x in minus[r]]for r in ids]
  d0,d1,dm=det(A0),det(A1),det(Am);pol=[scale(d0,2),sub(d1,dm),sub(add(d1,dm),scale(d0,2))];F=factors(pol);assert F is not None
  assert sorted(set(k for k in F if k>=0))==q['allowed_8th_root_exponents'];cnt[name+'_polynomials']+=1
  for k in q['allowed_8th_root_exponents']:
   aa=(-k)%8 if a==-1 else a;bb=k if b==-1 else b;E=exactmat(row,aa,bb)
   result=fixed_gate(E,97,w97)
   if result is None:cnt['fallback_65521']+=1;result=fixed_gate(E,65521,57852)
   assert result is not None;cnt[name+'_'+result]+=1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.monotonic()-start,6),
 'prime97_root':w97,'counts':dict(cnt),'status':'PASS'}
(P/'frontier-20261028-n8-dita-univariate-cert-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
