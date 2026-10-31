#!/usr/bin/env python3
"""Find exact separable minor gates for both-free n8 Diţă branches.

A nonzero 4x4 minor P(x,y), x=alpha^-1,y=beta, with rank-one 3x3
coefficient table P=f(x)g(y)/a and factors only x,y or 8th roots forces
at least one free phase to be an eighth root. This is a reduction only:
such specializations require their OWN cross-equation checks.
"""
import datetime,hashlib,itertools,json,os,time
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n8-dita-freefree-survivors-v1.jsonl';p=65521;w=57852
sg=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
Z=(0,0,0,0);ONE=(1,0,0,0)
def rt(k):
 k%=8;a=[0]*4;a[k%4]=1 if k<4 else -1;return tuple(a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b3-a2*b2-a3*b1,a0*b1+a1*b0-a2*b3-a3*b2,a0*b2+a1*b1+a2*b0-a3*b3,a0*b3+a1*b2+a2*b1+a3*b0)
def evalmod(a):return sum(a[i]*pow(w,i,p)for i in range(4))%p
def facmod(a):
 a=a[:]
 while len(a)>1 and not a[-1]:a.pop()
 if a==[0]:return None
 roots=[]
 for k in [-1]+list(range(8)):
  v=0 if k==-1 else pow(w,k,p)
  while len(a)>1:
   q=[0]*(len(a)-1);q[-1]=a[-1]
   for i in range(len(q)-2,-1,-1):q[i]=(a[i+1]+v*q[i+1])%p
   if (a[0]+v*q[0])%p:break
   roots.append(k);a=q
   while len(a)>1 and not a[-1]:a.pop()
 return roots if len(a)==1 and a[0] else None
def facexact(a):
 a=a[:]
 while len(a)>1 and a[-1]==Z:a.pop()
 if a==[Z]:return None
 roots=[]
 for k in [-1]+list(range(8)):
  v=Z if k==-1 else rt(k)
  while len(a)>1:
   q=[Z]*(len(a)-1);q[-1]=a[-1]
   for i in range(len(q)-2,-1,-1):q[i]=add(a[i+1],mul(v,q[i+1]))
   if add(a[0],mul(v,q[0]))!=Z:break
   roots.append(k);a=q
   while len(a)>1 and a[-1]==Z:a.pop()
 return roots if len(a)==1 and a[0]!=Z else None
allrows=list(itertools.combinations(range(16),4))
rows=[(1,3,4,10)]+[q for q in allrows if q!=(1,3,4,10) and sorted(Counter(i//4 for i in q).values())==[2,2]]
perms=[]
for q in itertools.permutations(range(4)):
 sign=-1 if sum(q[i]>q[j]for i in range(4)for j in range(i+1,4))%2 else 1;perms.append((q,sign))
# Exponent combinatorics depend only on mu and selected rows.
termcache={}
def terms(M,ids):
 key=(tuple(M),ids)
 if key not in termcache:
  T=[]
  for q,sign in perms:
   X=Y=0
   for i,t in enumerate(q):b,c=divmod(ids[i],4);X+=(b%2)*(t%2);Y+=(c%2)*(M[t]%2)
   T.append((q,sign,3*X+Y))
  termcache[key]=T
 return termcache[key]
def base(row):
 O,R0,R1,M=(row[k]for k in ('O','R0','R1','mu'));loc=[[0]*4 for _ in range(2)]
 for tau,j in enumerate(O):loc[j//4][j%4]=tau
 return [[tuple(sg[t][b]*sg[M[t]][c]*v for v in sub(rt((R1[c]-R0[b])*loc[0][t]),rt((R1[c]-R0[b])*loc[1][t])))for t in range(4)]for b in range(4)for c in range(4)]
def pmul(A,B):return A*B%p
def poly_mod(C,M,ids):
 out=[0]*9
 for q,s,j in terms(M,ids):
  v=s
  for i,t in enumerate(q):v=v*C[ids[i]][t]%p
  out[j]=(out[j]+v)%p
 return out
def poly_exact(C,M,ids):
 out=[Z]*9
 for q,s,j in terms(M,ids):
  v=ONE
  for i,t in enumerate(q):v=mul(v,C[ids[i]][t])
  if s<0:v=tuple(-x for x in v)
  out[j]=add(out[j],v)
 return out
def rank1_mod(poly):
 pivot=next((k for k,v in enumerate(poly)if v),None)
 if pivot is None:return None
 i,j=divmod(pivot,3);a=poly[pivot];f=[poly[3*x+j]for x in range(3)];g=[poly[3*i+y]for y in range(3)]
 if any((poly[3*x+y]*a-f[x]*g[y])%p for x in range(3)for y in range(3)):return None
 fx,fy=facmod(f),facmod(g)
 return (i,j) if fx is not None and fy is not None else None
def rank1_exact(poly,i,j):
 a=poly[3*i+j];f=[poly[3*x+j]for x in range(3)];g=[poly[3*i+y]for y in range(3)]
 if a==Z or any(mul(poly[3*x+y],a)!=mul(f[x],g[y])for x in range(3)for y in range(3)):return None
 fx,fy=facexact(f),facexact(g)
 return (fx,fy) if fx is not None and fy is not None else None
limit=int(os.environ.get('LIMIT','0'));suffix='sample' if limit else 'full';cnt=Counter();cert=[];sur=[];start=time.monotonic()
for ix,line in enumerate(src.read_text().splitlines()):
 if limit and ix>=limit:break
 row=json.loads(line);C=base(row);M=row['mu'];Cm=[[evalmod(v)for v in r]for r in C];found=False
 for ids in rows:
  q=rank1_mod(poly_mod(Cm,M,ids))
  if q is None:continue
  e=rank1_exact(poly_exact(C,M,ids),*q)
  if e is None:continue
  fx,fy=e;cert.append({'rows':ids,'x_roots':sorted(set(k for k in fx if k>=0)),'y_roots':sorted(set(k for k in fy if k>=0))});cnt['separable_root_gate']+=1;found=True;break
 if not found:cnt['unresolved']+=1;cert.append(None);sur.append(row)
(P/f'frontier-20261028-n8-dita-freefree-separable-{suffix}-certs-v1.jsonl').write_text(''.join(json.dumps(c,separators=(',',':'))+'\n'for c in cert))
(P/f'frontier-20261028-n8-dita-freefree-separable-{suffix}-survivors-v1.jsonl').write_text(''.join(json.dumps(c,separators=(',',':'))+'\n'for c in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'seconds':round(time.monotonic()-start,6),'limit':limit,'minors_tried_max':len(rows),'counts':dict(cnt),'unresolved':len(sur)}
(P/f'frontier-20261028-n8-dita-freefree-separable-{suffix}-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
