#!/usr/bin/env python3
"""Search for an EVEN Fourier T via the 24=8*3 CRT tensor lift.

K24=K8⊗F3, K8 is the exact non-Butson T8B point. The product QLS's
3-dimensional factor is classical with ray label r3+c3. 576 cell booleans,
exactly one per global row/column, and within each of three labels every
chosen local-8 ray must be orthogonal. Exact local Grams are imported from
the pinned original-vector checker. No maximal-24 ray premise.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;source=P/'frontier-20261028-t8b-nonbutson-explicit-v1.py';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='6ce6e5df6b6a7901d8822971dffdc1d05c17cc05dbb5f2687664cf568701b0cd'
exec(compile(raw.decode().split('nodes=0;found=None',1)[0],str(source),'exec'),globals())
S=z3.Solver();S.set(timeout=120000,random_seed=62)
X={(r,u,c,v):z3.Bool(f'x{r}_{u}_{c}_{v}') for r in range(8)for u in range(3)for c in range(8)for v in range(3)}
for r in range(8):
 for u in range(3):S.add(z3.PbEq([(X[r,u,c,v],1)for c in range(8)for v in range(3)],1))
for c in range(8):
 for v in range(3):S.add(z3.PbEq([(X[r,u,c,v],1)for r in range(8)for u in range(3)],1))
Y={(t,r,c):z3.Bool(f'y{t}_{r}_{c}')for t in range(3)for r in range(8)for c in range(8)}
for t in range(3):
 for r in range(8):
  for c in range(8):
   cells3=[X[r,u,c,(t-u)%3]for u in range(3)];S.add(Y[t,r,c]==z3.Or(*cells3),z3.PbLe([(v,1)for v in cells3],1))
 S.add(z3.PbEq([(Y[t,r,c],1)for r in range(8)for c in range(8)],8))
 local=list(itertools.product(range(8),repeat=2))
 for i,j in itertools.combinations(local,2):
  if not O(i,j):S.add(z3.Or(z3.Not(Y[t,*i]),z3.Not(Y[t,*j])))
S.add(X[0,0,0,0]);print('assertions',len(S.assertions()),flush=True);t0=time.monotonic();v=S.check();elapsed=time.monotonic()-t0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'local_checker_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver':'Z3 '+z3.get_version_string(),'timeout_ms':120000,'elapsed_seconds':round(elapsed,6),
 'status':str(v),'unknown_reason':S.reason_unknown() if v==z3.unknown else None}
if v==z3.sat:
 m=S.model();chosen=[key for key,x in X.items()if z3.is_true(m.eval(x))];assert len(chosen)==24
 assert len({(r,u)for r,u,c,v in chosen})==24 and len({(c,v)for r,u,c,v in chosen})==24
 assert all(((u+v)-(up+vp))%3!=0 or O((r,c),(rp,cp)) for (r,u,c,v),(rp,up,cp,vp) in itertools.combinations(chosen,2))
 obj.update(transversal=chosen,checked={'T_pairs_via_exact_local_gram':276,'row_column_incidence':True},tensor_inferred={'unit_vectors':576,'row_bases':24,'column_bases':24,'factor8_rays':64,'factor3_rays':3,'total_rays':192},warning='independent original 24-dimensional vector replay REQUIRED')
(P/'frontier-20261028-n24-t8b-f3-lift-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2),flush=True)
