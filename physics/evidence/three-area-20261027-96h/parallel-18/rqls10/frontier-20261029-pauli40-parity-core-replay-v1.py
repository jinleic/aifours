#!/usr/bin/env python3
"""Independent Pauli40 basis enumeration, SMT parity and independent-set coloring replay."""
import datetime,hashlib,itertools,json
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli40-source-vectors-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='a4f6cfedaa499442551a664599a8fbd9c8529388abc9c040f39ec57d9ddd5d10'
d=json.loads(raw);V=[d['vectors'][str(i)]for i in range(1,41)]
def zero(u,v):
 a=sum(x[0]*y[0]+x[1]*y[1]for x,y in zip(u,v));b=sum(x[0]*y[1]-x[1]*y[0]for x,y in zip(u,v));return a==0 and b==0
adj=[set()for _ in range(40)]
for a,b in itertools.combinations(range(40),2):
 if zero(V[a],V[b]):adj[a].add(b);adj[b].add(a)
# Build 4-bases as triangles in shared orthogonality-neighbor sets.
B=[]
for a in range(40):
 for b in sorted(x for x in adj[a]if x>a):
  for c in sorted(x for x in adj[a]&adj[b]if x>b):
   for e in sorted(x for x in adj[a]&adj[b]&adj[c]if x>c):B.append((a,b,c,e))
assert len(B)==40 and len(set(B))==40
X=[z3.Bool('b%d'%i)for i in range(40)];S=z3.Solver();S.set(timeout=30000);S.add(z3.PbEq([(x,1)for x in X],15))
for v in range(40):
 ids=[X[i]for i,b in enumerate(B)if v in b];assert len(ids)==4
 S.add(z3.Or(z3.PbEq([(x,1)for x in ids],0),z3.PbEq([(x,1)for x in ids],2)))
sets=[]
while True:
 q=S.check()
 if q==z3.unsat:break
 if q!=z3.sat:raise RuntimeError('SMT unknown '+S.reason_unknown())
 model=S.model();ss=tuple(i for i,x in enumerate(X)if z3.is_true(model.eval(x)));sets.append(ss);S.add(z3.Or(*[z3.Not(X[i])for i in ss]))
producer=P/'frontier-20261029-pauli40-parity-core-census-v1.json';pr=producer.read_bytes();D=json.loads(pr)
assert [list(b)for b in B]==D['bases'];assert sorted(sets)==[tuple(x['basis_indices'])for x in D['records']]
records=[]
for ss in sorted(sets):
 bases=[set(B[i])for i in ss];adj2=[set()for _ in range(15)]
 for i,j in itertools.combinations(range(15),2):
  if bases[i]&bases[j]:adj2[i].add(j);adj2[j].add(i)
 independent=[]
 for q in itertools.combinations(range(15),5):
  if all(j not in adj2[i]for i,j in itertools.combinations(q,2)):independent.append(sum(1<<i for i in q))
 full=(1<<15)-1;found=False
 for i,u in enumerate(independent):
  for v in independent[i+1:]:
   if u&v:continue
   if full^(u|v) in independent:found=True;break
  if found:break
 records.append({'basis_indices':ss,'independent_5sets':len(independent),'balanced_3colorable':found})
 assert not found
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'producer_sha256':hashlib.sha256(pr).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver':'Z3 '+z3.get_version_string(),'orthogonal_4bases':len(B),'parity_sets':len(sets),'matched_producer_keys':True,
 'balanced_3colorable':sum(x['balanced_3colorable']for x in records),'records':records,
 'scope':'SMT exhaustion is corroboration, not a formal proof log; coloring search is complete independent-set enumeration.'}
(P/'frontier-20261029-pauli40-parity-core-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='records'},indent=2))
