#!/usr/bin/env python3
"""Exact search for an n=8 even-Fourier-product transversal in a 2x4 Diţă family.

K[(a,t),(0,b)]=i^(t*b), K[(a,t),(1,b)]=(-1)^a*zeta8^d_t*i^(mu(t)*b).
O permutes all eight source rows, R assigns distinct physical rows to columns.
mu is any S4 permutation, d any four 8th-root phases. No max-ray assumption.
Normalizations O[0]=0, R[0]=0, mu[0]=0, d[0]=0 are via coordinate/physical
cyclic shifts and harmless column gauges. UNKNOWN is not a no-go.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;start=datetime.datetime.now().astimezone().isoformat()
S=z3.Solver();S.set(timeout=120000,random_seed=31)
O=[z3.BitVec(f'o{t}',3) for t in range(8)];R=[z3.BitVec(f'r{c}',3) for c in range(8)]
M=[z3.BitVec(f'm{t}',2) for t in range(4)];D=[z3.BitVec(f'd{t}',3) for t in range(4)]
S.add(z3.Distinct(*O),z3.Distinct(*R),z3.Distinct(*M),O[0]==0,R[0]==0,M[0]==0,D[0]==0)
def rootexpr(o,c):
 h,b=divmod(c,4);vals=[]
 for j in range(8):
  a,t=divmod(j,4)
  if h==0:v=z3.BitVecVal((2*t*b)%8,3)
  else:v=z3.BitVecVal((4*a)%8,3)+D[t]+z3.ZeroExt(1,M[t])*z3.BitVecVal((2*b)%8,3)
  vals.append(v)
 x=vals[-1]
 for j in range(6,-1,-1):x=z3.If(o==j,vals[j],x)
 return x
K=[[rootexpr(O[t],c) for c in range(8)]for t in range(8)]
for c,d in itertools.combinations(range(8),2):
 e=[K[t][d]-K[t][c]+(R[d]-R[c])*z3.BitVecVal(t,3) for t in range(8)]
 for j in range(4):S.add(z3.Sum(*[z3.If(v==j,1,z3.If(v==j+4,-1,0)) for v in e])==0)
print('assertions',len(S.assertions()),flush=True);t0=time.monotonic();res=S.check();dt=time.monotonic()-t0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_start':start,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'status':str(res),'solver_seconds':round(dt,6),'timeout_ms':120000,
 'unknown_reason':S.reason_unknown() if res==z3.unknown else None,'z3':z3.get_version_string()}
if res==z3.sat:
 m=S.model();O0=[m.eval(x).as_long()for x in O];R0=[m.eval(x).as_long()for x in R];M0=[m.eval(x).as_long()for x in M];D0=[m.eval(x).as_long()for x in D]
 E=[]
 for tau in range(8):
  a,t=divmod(O0[tau],4);E.append([(2*t*b)%8 for b in range(4)]+[(4*a+D0[t]+2*M0[t]*b)%8 for b in range(4)])
 def phase(r,c,t):return (r*t+E[t][c])%8
 def gram(a,b):
  v=[0]*4
  for t in range(8):
   k=(phase(*b,t)-phase(*a,t))%8;v[k%4]+=1 if k<4 else -1
  return v
 zero=[0]*4
 for r in range(8):
  for c,d in itertools.combinations(range(8),2):assert gram((r,c),(r,d))==zero
 for c in range(8):
  for r,s in itertools.combinations(range(8),2):assert gram((r,c),(s,c))==zero
 for c,d in itertools.combinations(range(8),2):assert gram((R0[c],c),(R0[d],d))==zero
 cells=list(itertools.product(range(8),repeat=2));dups=[]
 for a,b in itertools.combinations(cells,2):
  if len({(phase(*b,t)-phase(*a,t))%8 for t in range(8)})==1:dups.append([a,b])
 obj.update(source_order=O0,transversal_rows=R0,mu=M0,delta_exponents=D0,hadamard_exponents=E,
            original_checks={'norms':64,'row_grams':224,'column_grams':224,'T_grams':28,'ray_pairs':2016,'duplicate_pairs':dups})
(P/'frontier-20261028-n8-dita-bh8-counterexample-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2),flush=True)
