#!/usr/bin/env python3
"""Boolean-PB alternative to rooted Pauli-core SMT orbit exhaustion."""
import datetime,hashlib,itertools,json,time,z3
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-core-pure-hybrid-orbit-v1.py';raw=src.read_bytes()
# Build exact source bases and unitary generators without executing either original SMT query.
g={'__file__':str(src)};exec(compile(raw.decode().split('S.push();S.add(z3.Or',1)[0],str(src),'exec'),g)
B=g['B'];gens=g['gens'];pure=g['pure'];index=g['index'];P0=P/'frontier-20261029-pauli60-tripartite-core-search-v1.json';seed=json.loads(P0.read_bytes());core=tuple(sorted(index[tuple(x-1 for x in q)]for q in seed['bases_1indexed']));root=core[0];orbit={core};stack=[core]
while stack:
 q=stack.pop()
 for h in gens:
  z=tuple(sorted(h[i]for i in q))
  if z not in orbit:orbit.add(z);stack.append(z)
rooted=[q for q in orbit if root in q];assert len(orbit)==1920 and len(rooted)==320
hybrid=[i for i in range(len(B))if i not in pure];Y={(i,c):z3.Bool('b%d_%d'%(i,c))for i in hybrid for c in range(3)};X={i:z3.Or(*[Y[i,c]for c in range(3)])for i in hybrid};S=z3.Solver();S.set(timeout=45000,random_seed=29)
for i in hybrid:S.add(z3.PbLe([(Y[i,c],1)for c in range(3)],1))
for c in range(3):S.add(z3.PbEq([(Y[i,c],1)for i in hybrid],5))
for r in range(60):
 contains=[i for i in hybrid if r in B[i]]
 S.add(z3.Or(z3.PbEq([(X[i],1)for i in contains],0),z3.PbEq([(X[i],1)for i in contains],2)))
 for c in range(3):S.add(z3.PbLe([(Y[i,c],1)for i in contains],1))
for i,j in itertools.combinations(hybrid,2):
 if len(set(B[i])&set(B[j]))>=2:S.add(z3.Or(z3.Not(X[i]),z3.Not(X[j])))
S.add(Y[root,0]);S.add(*[z3.Or(*[z3.Not(X[i])for i in q if i!=root])for q in rooted])
begin=time.monotonic();v=S.check();seconds=time.monotonic()-begin
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'setup_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'solver':'Z3 '+z3.get_version_string(),'root':root,'blocked_rooted_cores':len(rooted),
 'elapsed_seconds':round(seconds,6),'status':str(v),'unknown_reason':S.reason_unknown()if v==z3.unknown else None,
 'scope':'Pure bases excluded by independent degree0 census; SAT is an additional orbit, UNSAT solver-scoped, UNKNOWN no conclusion.'}
if v==z3.sat:
 m=S.model();obj['different_core']=[i for i in hybrid if z3.is_true(m.eval(X[i]))];obj['colors']={str(i):next(c for c in range(3)if z3.is_true(m.eval(Y[i,c])))for i in obj['different_core']}
(P/'frontier-20261029-pauli60-boolean-orbit-test-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
