#!/usr/bin/env python3
"""Unrestricted BH(10,30) Fourier-transversal exact finite SMT encoding.

A transversal is column-normalized to (r,r); K[0,*],K[*,0] are dephased.
Q(zeta30)=Q(zeta6)Q(zeta5) has tensor basis (1,zeta6)*(1,zeta5,..,zeta5^3),
zeta30=zeta6^5*zeta5 and zeta10=zeta30^3. Unknown is NOT an exclusion.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent; out=P/'frontier-20261028-bh30-transversal-smt-v1.json'
start=datetime.datetime.now().astimezone().isoformat()
v6=[[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]]
v5=[[int(i==j) for j in range(4)] for i in range(4)]+[[-1]*4]
v30=[[a*b for a in v6[(5*k)%6] for b in v5[k%5]] for k in range(30)]
S=z3.Solver(); S.set(timeout=120000,random_seed=9)
X=[[z3.Int('x_%d_%d'%(t,c)) for c in range(10)]for t in range(10)]
for t in range(10):
 for c in range(10):
  S.add(X[t][c]>=0,X[t][c]<30)
  if t==0 or c==0:S.add(X[t][c]==0)
root={}
def V(t,r,s,shift,j):
 key=(t,r,s,shift,j)
 if key not in root:
  e=(X[t][s]-X[t][r]+shift)%30
  plus=[e==k for k in range(30) if v30[k][j]==1]
  minus=[e==k for k in range(30) if v30[k][j]==-1]
  root[key]=z3.If(z3.Or(*plus),1,0)-z3.If(z3.Or(*minus),1,0)
 return root[key]
for r in range(10):
 for s in range(r+1,10):
  d=s-r
  for j in range(8):
   S.add(z3.Sum(*[V(t,r,s,0,j) for t in range(10)])==0)
   S.add(z3.Sum(*[V(t,r,s,(3*d*t)%30,j) for t in range(10)])==0)
print('constraints',len(S.assertions()),'exact root components',len(root),flush=True)
t0=time.monotonic();res=S.check();elapsed=time.monotonic()-t0
obj={'method':'exact Z3 over Q(zeta6) tensor Q(zeta5); no rank/ray assumption',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_start':start,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver_timeout_ms':120000,'solver_elapsed_seconds':round(elapsed,6),
 'z3_version':z3.get_version_string(),'status':str(res),'assertion_count':len(S.assertions()),
 'unknown_reason':S.reason_unknown() if res==z3.unknown else None}
if res==z3.sat:
 m=S.model();E=[[m.eval(X[t][c]).as_long() for c in range(10)]for t in range(10)]
 obj['exponents']=E
 def phase(r,c,t):return (3*r*t+E[t][c])%30
 def gram(a,b):
  ans=[0]*8
  for t in range(10):
   k=(phase(*b,t)-phase(*a,t))%30
   for j,x in enumerate(v30[k]):ans[j]+=x
  return ans
 zero=[0]*8
 rowchecks=colchecks=transchecks=0
 for r in range(10):
  for c,d in itertools.combinations(range(10),2):assert gram((r,c),(r,d))==zero;rowchecks+=1
 for c in range(10):
  for r,s in itertools.combinations(range(10),2):assert gram((r,c),(s,c))==zero;colchecks+=1
 for r,s in itertools.combinations(range(10),2):assert gram((r,r),(s,s))==zero;transchecks+=1
 cells=list(itertools.product(range(10),repeat=2));dups=[]
 for a,b in itertools.combinations(cells,2):
  ds=[(phase(*b,t)-phase(*a,t))%30 for t in range(10)]
  if len(set(ds))==1:dups.append([a,b])
 obj['original_vector_check']={'row_grams':rowchecks,'column_grams':colchecks,'transversal_grams':transchecks,'ray_pairs':4950,'duplicates':dups}
out.write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2),flush=True)
