#!/usr/bin/env python3
"""Full q30 100-ray Fourier 1-RQLS search using QF_BV, exact phase sums.

Difference modulo30 is conditional subtraction, not integer modulo. Component
sums use BV5: each signed integer sum lies in [-10,10], so zero modulo32 iff
zero as an integer. A diagonal T and first-row/column dephasing are WLOG.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;start=datetime.datetime.now().astimezone().isoformat()
v6=[[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]];v5=[[int(i==j)for j in range(4)]for i in range(4)]+[[-1]*4]
v30=[[a*b for a in v6[(5*k)%6]for b in v5[k%5]]for k in range(30)]
S=z3.SolverFor('QF_BV');S.set(timeout=120000,random_seed=41)
X=[[z3.BitVec('x%d_%d'%(t,c),5)for c in range(10)]for t in range(10)]
for t in range(10):
 for c in range(10):
  S.add(z3.ULT(X[t][c],z3.BitVecVal(30,5)))
  if t==0 or c==0:S.add(X[t][c]==0)
def diff(t,r,s):
 v=z3.ZeroExt(1,X[t][s])+z3.BitVecVal(30,6)-z3.ZeroExt(1,X[t][r]);return z3.If(z3.UGE(v,z3.BitVecVal(30,6)),v-z3.BitVecVal(30,6),v)
D={(t,r,s):diff(t,r,s)for t in range(10)for r in range(10)for s in range(r+1,10)}
def shifted(v,k):
 if k==0:return v
 x=v+z3.BitVecVal(k,6);return z3.If(z3.UGE(x,z3.BitVecVal(30,6)),x-z3.BitVecVal(30,6),x)
def component(e,j):
 pos=z3.Or(*[e==k for k in range(30)if v30[k][j]==1]);neg=z3.Or(*[e==k for k in range(30)if v30[k][j]==-1])
 return z3.If(pos,z3.BitVecVal(1,5),z3.If(neg,z3.BitVecVal(31,5),z3.BitVecVal(0,5)))
for r in range(10):
 for s in range(r+1,10):
  for typ in range(2):
   es=[shifted(D[t,r,s],(3*(s-r)*t)%30 if typ else 0)for t in range(10)]
   for j in range(8):S.add(sum((component(e,j)for e in es),z3.BitVecVal(0,5))==0)
  # Exactly excludes all parallel cells using first-coordinate dephasing.
  for k in range(1,10):S.add(z3.Or(*[D[t,r,s]!=((3*k*t)%30) for t in range(1,10)]))
print('BV assertions',len(S.assertions()),flush=True);t0=time.monotonic();res=S.check();elapsed=time.monotonic()-t0
obj={'method':'QF_BV exact Q(zeta6) tensor Q(zeta5); all 405 100-ray character exclusions',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_start':start,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'timeout_ms':120000,'seconds':round(elapsed,6),'z3_version':z3.get_version_string(),
 'status':str(res),'unknown_reason':S.reason_unknown() if res==z3.unknown else None}
if res==z3.sat:
 model=S.model();E=[[model.eval(X[t][c]).as_long()for c in range(10)]for t in range(10)]
 def ph(r,c,t):return (3*r*t+E[t][c])%30
 def gram(a,b):
  z=[0]*8
  for t in range(10):
   e=(ph(*b,t)-ph(*a,t))%30
   for j,v in enumerate(v30[e]):z[j]+=v
  return z
 Z=[0]*8
 assert all(gram((r,c),(r,d))==Z for r in range(10)for c,d in itertools.combinations(range(10),2))
 assert all(gram((r,c),(s,c))==Z for c in range(10)for r,s in itertools.combinations(range(10),2))
 assert all(gram((r,r),(s,s))==Z for r,s in itertools.combinations(range(10),2))
 cells=list(itertools.product(range(10),repeat=2));dup=[]
 for a,b in itertools.combinations(cells,2):
  if len({(ph(*b,t)-ph(*a,t))%30 for t in range(10)})==1:dup.append((a,b))
 assert not dup
 obj.update(exponents=E,original_checks={'norms':100,'row_gram_pairs':450,'column_gram_pairs':450,'T_gram_pairs':45,'ray_pairs':4950,'duplicates':len(dup)})
(P/'frontier-20261028-bh30-maximal-bv-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2),flush=True)
