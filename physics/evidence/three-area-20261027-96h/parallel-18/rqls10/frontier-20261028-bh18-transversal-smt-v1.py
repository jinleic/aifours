#!/usr/bin/env python3
"""Full BH(10,18) Fourier-transversal exact SMT, not a Max-QLS solver.

Column-permute the putative transversal to cells (r,r), dephase K[0,*]
and K[*,0] by 18th roots. All root sums are over integer power bases:
Phi18=x^6-x^3+1, and zeta10=-zeta5^3 with Q(zeta18)∩Q(zeta5)=Q.
A timeout/unknown is not an exclusion. SAT is independently checked on
original 24-dimensional Q(zeta18) tensor Q(zeta5) Gram vectors and rays.
"""
import datetime, hashlib, itertools, json, time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent
out=P/'frontier-20261028-bh18-transversal-smt-v1.json'
start=datetime.datetime.now().astimezone().isoformat()
v18=[];v=[1,0,0,0,0,0]
for k in range(18):
    v18.append(v);v=[-v[5],v[0],v[1],v[2]+v[5],v[3],v[4]]
assert v==[1,0,0,0,0,0]
v5=[[int(i==j) for j in range(4)] for i in range(4)]+[[-1]*4]
assert len(v18)==18 and all(sum(abs(z) for z in a)<=2 for a in v18)
S=z3.Solver(); S.set(timeout=120000,random_seed=8)
X=[[z3.Int('x_%d_%d'%(t,c)) for c in range(10)]for t in range(10)]
for t in range(10):
 for c in range(10):
  S.add(X[t][c]>=0,X[t][c]<18)
  if t==0 or c==0:S.add(X[t][c]==0)
root={}
def V(t,r,s,j):
 key=(t,r,s,j)
 if key not in root:
  e=(X[t][s]-X[t][r])%18
  plus=[e==k for k in range(18) if v18[k][j]==1]
  minus=[e==k for k in range(18) if v18[k][j]==-1]
  root[key]=z3.If(z3.Or(*plus),1,0)-z3.If(z3.Or(*minus),1,0)
 return root[key]
for r in range(10):
 for s in range(r+1,10):
  for j in range(6):S.add(z3.Sum(*[V(t,r,s,j) for t in range(10)])==0)
  d=s-r
  if d==5:
   for j in range(6):S.add(z3.Sum(*[V(t,r,s,j) for t in range(0,10,2)])==0)
  else:
   # For d mod5 nonzero, the five Q(zeta18)-coefficients of powers
   # zeta5^(3*d*u) must all be equal.
   for u in range(1,5):
    for j in range(6):
     D0=V(0,r,s,j)+((-1)**d)*V(5,r,s,j)
     Du=((-1)**(d*u))*(V(u,r,s,j)+((-1)**d)*V(u+5,r,s,j))
     S.add(Du==D0)
print('constraints',len(S.assertions()),'exact root components',len(root),flush=True)
t0=time.monotonic();res=S.check();elapsed=time.monotonic()-t0
obj={'method':'exact Z3 over Phi18 and disjoint Q(zeta5); no rank/ray assumption',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_start':start,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver_timeout_ms':120000,'solver_elapsed_seconds':round(elapsed,6),
 'z3_version':z3.get_version_string(),'status':str(res),'assertion_count':len(S.assertions()),
 'unknown_reason':S.reason_unknown() if res==z3.unknown else None}
if res==z3.sat:
 m=S.model();E=[[m.eval(X[t][c]).as_long() for c in range(10)]for t in range(10)]
 obj['exponents']=E
 def phase(r,c,t):return (9*r*t+5*E[t][c])%90
 def gram(a,b):
  ans=[0]*24
  for t in range(10):
   k=(phase(*b,t)-phase(*a,t))%90
   A=v18[(11*k)%18];B=v5[(2*k)%5]
   for i in range(6):
    for j in range(4):ans[4*i+j]+=A[i]*B[j]
  return ans
 zero=[0]*24
 rowchecks=colchecks=transchecks=0
 for r in range(10):
  for c,d in itertools.combinations(range(10),2):assert gram((r,c),(r,d))==zero;rowchecks+=1
 for c in range(10):
  for r,s in itertools.combinations(range(10),2):assert gram((r,c),(s,c))==zero;colchecks+=1
 for r,s in itertools.combinations(range(10),2):assert gram((r,r),(s,s))==zero;transchecks+=1
 cells=list(itertools.product(range(10),repeat=2));dups=[]
 for a,b in itertools.combinations(cells,2):
  ds=[(phase(*b,t)-phase(*a,t))%90 for t in range(10)]
  if len(set(ds))==1:dups.append([a,b])
 obj['original_vector_check']={'row_grams':rowchecks,'column_grams':colchecks,'transversal_grams':transchecks,'ray_pairs':4950,'duplicates':dups}
out.write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2),flush=True)
