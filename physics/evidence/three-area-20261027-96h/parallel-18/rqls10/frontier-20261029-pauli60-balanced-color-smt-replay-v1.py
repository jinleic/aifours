#!/usr/bin/env python3
"""Independent SMT replay of balanced tripartition uniqueness."""
import datetime,hashlib,itertools,json,z3
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';D=json.loads(raw)
# Independently reconstruct 4D adjacency from the three original shared-ray matrices.
G=set();groups=D['groups']
for z in D['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if x:G.add(tuple(sorted((groups[a][i],groups[b][j]))))
x=[z3.Int('c%d'%i)for i in range(15)];S=z3.Solver();S.add(*[z3.And(t>=0,t<3)for t in x],x[0]==0)
for i,j in G:S.add(x[i]!=x[j])
for c in range(3):S.add(z3.PbEq([(x[i]==c,1)for i in range(15)],5))
Q=[]
while S.check()==z3.sat:
 m=S.model();q=tuple(m.eval(v).as_long()for v in x);Q.append(q);S.add(z3.Or(*[x[i]!=q[i]for i in range(15)]))
assert len(Q)==2
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'solver':'Z3 '+z3.get_version_string(),
 'balanced_colorings_fixing_vertex0':len(Q),'colorings':Q,'scope':'SMT exhaustion corroborates independent direct-DFS proof.','status':'PASS'}
(P/'frontier-20261029-pauli60-balanced-color-smt-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='colorings'},indent=2))
