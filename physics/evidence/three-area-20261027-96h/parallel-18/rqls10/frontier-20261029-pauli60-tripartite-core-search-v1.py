#!/usr/bin/env python3
"""Search entire published two-qubit 60-ray set for a 3-partite 30–15 core.
SAT is an explicit 4D partial configuration, not a QLS10; independent original
ray replay and a 6D complement plus full 100-ray extension are mandatory.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-source-vectors-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8edccd50a66289a669b30fa5ec40b6b215147af3e9731545cc4ffe3bf8b33294';d=json.loads(raw);V=[d['vectors'][str(i)]for i in range(1,61)]
def dot(a,b):return(sum(x[0]*y[0]+x[1]*y[1]for x,y in zip(a,b)),sum(x[0]*y[1]-x[1]*y[0]for x,y in zip(a,b)))
def norm(a):return sum(x*x+y*y for x,y in a)
for i,j in itertools.combinations(range(60),2):
 x,y=dot(V[i],V[j]);assert x*x+y*y!=norm(V[i])*norm(V[j])
adj=[set()for _ in range(60)]
for i,j in itertools.combinations(range(60),2):
 if dot(V[i],V[j])==(0,0):adj[i].add(j);adj[j].add(i)
B=[]
for a in range(60):
 for b in sorted(x for x in adj[a]if x>a):
  for c in sorted(x for x in adj[a]&adj[b]if x>b):
   for e in sorted(x for x in adj[a]&adj[b]&adj[c]if x>c):B.append((a,b,c,e))
assert len(B)==105
X=[z3.Bool('selected%d'%i)for i in range(len(B))];C=[z3.Int('color%d'%i)for i in range(len(B))];S=z3.Solver();S.set(timeout=90000,random_seed=20)
S.add(z3.PbEq([(x,1)for x in X],15))
for c in C:S.add(c>=0,c<3)
for v in range(60):
 q=[X[i]for i,b in enumerate(B)if v in b];S.add(z3.Or(z3.PbEq([(x,1)for x in q],0),z3.PbEq([(x,1)for x in q],2)))
for k in range(3):S.add(z3.PbEq([(z3.And(X[i],C[i]==k),1)for i in range(len(B))],5))
for i,j in itertools.combinations(range(len(B)),2):
 size=len(set(B[i])&set(B[j]))
 if size>=2:S.add(z3.Or(z3.Not(X[i]),z3.Not(X[j])))
 elif size==1:S.add(z3.Implies(z3.And(X[i],X[j]),C[i]!=C[j]))
t0=time.monotonic();res=S.check();elapsed=time.monotonic()-t0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rays':60,'orthogonal_bases':len(B),'solver':'Z3 '+z3.get_version_string(),
 'timeout_ms':90000,'elapsed_seconds':round(elapsed,6),'status':str(res),'unknown_reason':S.reason_unknown()if res==z3.unknown else None,
 'scope':'Only the published 60 two-qubit rays. SAT is a 4D partial parity configuration, not a 1RQLS10 witness; UNSAT is solver-scoped.'}
if res==z3.sat:
 m=S.model();ids=[i for i,x in enumerate(X)if z3.is_true(m.eval(x))];chosen=[B[i]for i in ids];colors=[m.eval(C[i]).as_long()for i in ids]
 assert len(chosen)==15 and all(colors.count(k)==5 for k in range(3))
 R=[sum(v in b for b in chosen)for v in range(60)];assert all(x in(0,2)for x in R) and sum(x==2 for x in R)==30
 for i,j in itertools.combinations(range(15),2):
  q=len(set(chosen[i])&set(chosen[j]));assert q<=1 and (q==0 or colors[i]!=colors[j])
 obj['bases_1indexed']=[[j+1 for j in b]for b in chosen];obj['colors']=colors;obj['used_rays_1indexed']=[i+1 for i,x in enumerate(R)if x==2]
(P/'frontier-20261029-pauli60-tripartite-core-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
