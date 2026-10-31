#!/usr/bin/env python3
"""Full q8/ordering/transversal search: candidate even-order counterexample.

Exact bitvector arithmetic: Phi8=x^4+1; K and K∘F8 Gram equations.
A diagonal transversal is WLOG by K-column permutation; K is dephased.
No maximum-ray assumption. Unknown/uncertified unsat is not an all-K no-go.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;start=datetime.datetime.now().astimezone().isoformat()
S=z3.Solver();S.set(timeout=120000,random_seed=22)
X=[[z3.BitVec('x_%d_%d'%(t,c),3) for c in range(8)]for t in range(8)]
for t in range(8):
 for c in range(8):
  if not t or not c:S.add(X[t][c]==0)
for r in range(8):
 for s in range(r+1,8):
  for d in [0,s-r]:
   e=[X[t][s]-X[t][r]+z3.BitVecVal((d*t)%8,3) for t in range(8)]
   for j in range(4):S.add(z3.Sum(*[z3.If(v==j,1,z3.If(v==j+4,-1,0)) for v in e])==0)
print('initial assertions',len(S.assertions()),flush=True)
t0=time.monotonic();res=S.check();dt=time.monotonic()-t0
obj={'method':'exact BV3 Gram constraints in Q(zeta8), no ray assumption',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_start':start,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'timeout_ms':120000,'seconds':round(dt,6),'z3_version':z3.get_version_string(),
 'status':str(res),'unknown_reason':S.reason_unknown() if res==z3.unknown else None}
if res==z3.sat:
 m=S.model();A=[[m.eval(X[t][c]).as_long() for c in range(8)]for t in range(8)]
 def phase(r,c,t):return (r*t+A[t][c])%8
 def gram(a,b):
  v=[0]*4
  for t in range(8):
   k=(phase(*b,t)-phase(*a,t))%8;v[k%4]+=1 if k<4 else -1
  return v
 zero=[0]*4;counts=[0,0,0]
 for r in range(8):
  for c,d in itertools.combinations(range(8),2):assert gram((r,c),(r,d))==zero;counts[0]+=1
 for c in range(8):
  for r,s in itertools.combinations(range(8),2):assert gram((r,c),(s,c))==zero;counts[1]+=1
 for r,s in itertools.combinations(range(8),2):assert gram((r,r),(s,s))==zero;counts[2]+=1
 cells=list(itertools.product(range(8),repeat=2));dups=[]
 for a,b in itertools.combinations(cells,2):
  if len({(phase(*b,t)-phase(*a,t))%8 for t in range(8)})==1:dups.append([a,b])
 obj['exponents']=A;obj['original_vector_checks']={'row_grams':counts[0],'column_grams':counts[1],'transversal_grams':counts[2],'ray_pairs':len(cells)*(len(cells)-1)//2,'duplicates':dups}
(P/'frontier-20261028-n8-bh8-transversal-smt-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2),flush=True)
