#!/usr/bin/env python3
"""Exact minor-polynomial root gates for one-free-block n8 branches.

Rank-drop requires every 4x4 minor of C(x)=C0+x C1 to vanish. Here x is
alpha^-1 or beta, and C1 has at most2 nonzero columns: degree <=2. For a
selected minor, certify its exact Q(zeta8) polynomial has roots ONLY 0 or
8th roots; x cannot be0 and fixed 8th-root branches are handled separately.
Mod-p arithmetic is only a prescreen. Unfound gates remain OPEN.
"""
import datetime,hashlib,itertools,json,time
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-freefree-specializations-survivors-v1.jsonl';p=65521;w=57852;half=pow(2,-1,p)
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];ex=[[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,1]]
Z=(0,0,0,0);ONE=(1,0,0,0)
def h(t,b,k):return ((4 if sg[t][b]<0 else 0)+k*ex[t][b])%8
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,k):return tuple(x*k for x in a)
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b3-a2*b2-a3*b1,a0*b1+a1*b0-a2*b3-a3*b2,a0*b2+a1*b1+a2*b0-a3*b3,a0*b3+a1*b2+a2*b1+a3*b0)
def matrices(row):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));a,b=row['alpha'],row['beta'];loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 def mat(x):
  aa=x if a==-1 else a;bb=x if b==-1 else b
  return [[sub(rt((R1[c]-R0[k])*loc[0][t]+h(M[t],c,bb)-h(t,k,aa)),rt((R1[c]-R0[k])*loc[1][t]+h(M[t],c,bb)-h(t,k,aa)))for t in range(4)]for k in range(4)for c in range(4)]
 return mat(0),mat(4)
def detmod(A):
 A=[r[:]for r in A];v=1
 for k in range(4):
  j=next((i for i in range(k,4)if A[i][k]),None)
  if j is None:return 0
  if j!=k:A[k],A[j]=A[j],A[k];v=-v
  x=A[k][k];v=v*x%p;inv=pow(x,-1,p)
  for i in range(k+1,4):
   f=A[i][k]*inv%p
   for j in range(k+1,4):A[i][j]=(A[i][j]-f*A[k][j])%p
 return v%p
perms=[]
for q in itertools.permutations(range(4)):
 sign=-1 if sum(q[i]>q[j]for i in range(4)for j in range(i+1,4))%2 else 1;perms.append((q,sign))
def detexact(A):
 out=Z
 for q,s in perms:
  v=ONE
  for i in range(4):v=mul(v,A[i][q[i]])
  out=add(out,scale(v,s))
 return out
def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def factors_mod(a):
 a=trim(a[:]);facts=[]
 if a==[0]:return None
 for k in [-1]+list(range(8)):
  r=0 if k==-1 else pow(w,k,p)
  while len(a)>1:
   q=[0]*(len(a)-1);q[-1]=a[-1]
   for j in range(len(q)-2,-1,-1):q[j]=(a[j+1]+r*q[j+1])%p
   if (a[0]+r*q[0])%p:break
   a=trim(q);facts.append(k)
 return facts if len(a)==1 and a[0] else None
def trimexact(a):
 while len(a)>1 and a[-1]==Z:a.pop()
 return a
def factors_exact(a):
 a=trimexact(a[:]);facts=[]
 if a==[Z]:return None
 for k in [-1]+list(range(8)):
  r=Z if k==-1 else rt(k)
  while len(a)>1:
   q=[Z]*(len(a)-1);q[-1]=a[-1]
   for j in range(len(q)-2,-1,-1):q[j]=add(a[j+1],mul(r,q[j+1]))
   if add(a[0],mul(r,q[0]))!=Z:break
   a=trimexact(q);facts.append(k)
 return facts if len(a)==1 and a[0]!=Z else None
allrows=list(itertools.combinations(range(16),4))
rows=[(1,2,4,7)]+[q for q in allrows if q!=(1,2,4,7) and sorted(Counter(i//4 for i in q).values())==[2,2]]
cnt=Counter();sur=[];cert=[];start=time.monotonic()
for line in src.read_text().splitlines():
 row=json.loads(line);plus,minus=matrices(row)
 # C0=(Cplus+Cminus)/2; exact determinant evaluations of 2*C(x) avoid fractions.
 a0=[[add(x,y)for x,y in zip(r,s)]for r,s in zip(plus,minus)]
 a1=[[scale(x,2)for x in r]for r in plus];am=[[scale(x,2)for x in r]for r in minus]
 def modmat(A):return [[sum(v[k]*pow(w,k,p)for k in range(4))%p for v in r]for r in A]
 m0,m1,mm=modmat(a0),modmat(a1),modmat(am);ok=False
 for ids in rows:
  d0=detmod([m0[i]for i in ids]);d1=detmod([m1[i]for i in ids]);dm=detmod([mm[i]for i in ids])
  poly=[2*d0%p,(d1-dm)%p,(d1+dm-2*d0)%p]
  if factors_mod(poly) is None:continue
  e0=detexact([a0[i]for i in ids]);e1=detexact([a1[i]for i in ids]);em=detexact([am[i]for i in ids])
  epoly=[scale(e0,2),sub(e1,em),sub(add(e1,em),scale(e0,2))]
  factors=factors_exact(epoly)
  if factors is None:continue
  cert.append({'minor_rows':ids,'allowed_8th_root_exponents':sorted(set(k for k in factors if k>=0))});cnt['root_only']+=1;ok=True;break
 if not ok:cnt['unresolved']+=1;sur.append(row);cert.append(None)
(P/'frontier-20261028-n8-dita-ff-specialized-root-certificates-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in cert))
(P/'frontier-20261028-n8-dita-ff-specialized-root-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'seconds':round(time.monotonic()-start,6),'counts':dict(cnt),'unresolved':len(sur),'minors_per_branch_max':len(rows)}
(P/'frontier-20261028-n8-dita-ff-specialized-root-gate-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
