#!/usr/bin/env python3
"""Bounded exact SAT search for a 4-sparse real 100-ray Parker 1-RQLS."""
from itertools import combinations
from pathlib import Path
import json,time,z3
P=Path(__file__).resolve().parent
L=json.loads((P/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']['labels']
assert all(set(row)==set(range(10))for row in L) and all({L[r][c] for r in range(10)}==set(range(10))for c in range(10))
inv={L[0][c]:c for c in range(10)};S=z3.Solver();S.set(timeout=30000,random_seed=411)
p={};m={};cells=[(r,c)for r in range(1,10)for c in range(10)]
for r,c in cells:
 for t in range(10):
  p[r,c,t]=z3.Bool(f'p_{r}_{c}_{t}');m[r,c,t]=z3.Bool(f'm_{r}_{c}_{t}')
  S.add(z3.Not(z3.And(p[r,c,t],m[r,c,t])))
  if t==c or t==inv[L[r][c]]:S.add(z3.Not(p[r,c,t]),z3.Not(m[r,c,t]))
 S.add(z3.Sum([z3.If(z3.Or(p[r,c,t],m[r,c,t]),1,0)for t in range(10)])==4)
blocks=[[ (r,c)for c in range(10)]for r in range(1,10)]
blocks += [[(r,c)for r in range(1,10)]for c in range(10)]
blocks += [[(r,c)for r in range(1,10)for c in range(10)if L[r][c]==label]for label in range(10)]
edge=set()
for B in blocks:
 for a,b in combinations(B,2):edge.add(tuple(sorted((a,b))))
for (r,c),(s,d) in edge:
 terms=[]
 for t in range(10):
  positive=z3.Or(z3.And(p[r,c,t],p[s,d,t]),z3.And(m[r,c,t],m[s,d,t]))
  negative=z3.Or(z3.And(p[r,c,t],m[s,d,t]),z3.And(m[r,c,t],p[s,d,t]))
  terms.append(z3.If(positive,1,z3.If(negative,-1,0)))
 S.add(z3.Sum(terms)==0)
# Orthogonal pairs are already nonparallel. Only nonedges need both sign exclusions.
for a,b in combinations(cells,2):
 if tuple(sorted((a,b))) in edge:continue
 r,c=a;s,d=b
 S.add(z3.Or(*[z3.Or(p[r,c,t]!=p[s,d,t],m[r,c,t]!=m[s,d,t])for t in range(10)]))
 S.add(z3.Or(*[z3.Or(p[r,c,t]!=m[s,d,t],m[r,c,t]!=p[s,d,t])for t in range(10)]))
start=time.monotonic();answer=S.check();elapsed=time.monotonic()-start
out={'verdict':str(answer),'elapsed_seconds':elapsed,'timeout_ms':30000,'edge_count':len(edge),
 'reason_unknown':S.reason_unknown() if answer==z3.unknown else None,
 'scope':'one fixed Parker L, nonfirst vectors real flat4; solver result not an unrestricted no-go'}
if answer==z3.sat:
 model=S.model();array=[]
 for r in range(10):
  row=[]
  for c in range(10):
   if r==0:row.append([2*int(t==c)for t in range(10)])
   else:row.append([int(z3.is_true(model.eval(p[r,c,t])))-int(z3.is_true(model.eval(m[r,c,t])))for t in range(10)])
  array.append(row)
 out['candidate']={'array':array,'denominator':2,'labels':L,'requires_independent_original_vector_verification':True}
(P/'frontier-20261028-sparse4-sign-smt-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print({k:v for k,v in out.items()if k!='candidate'},flush=True)
