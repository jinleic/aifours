#!/usr/bin/env python3
"""Enumerate all first-row-normalized classical mates of Weisner L."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-weisner-all-mates-trade-census-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='995796c616d4b48aec948f638234bdd2ac764267b66429a7321edd6de5bd4fb9'
d=json.loads(raw);T=d['T'];masks=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T];groups={c:[i for i,t in enumerate(T)if t[0]==c]for c in range(10)};nodes=0;solutions=[]
def search(rem,used,chosen):
 global nodes
 nodes+=1
 if not rem:solutions.append(tuple(chosen));return
 c=min(rem,key=lambda x:(sum(not(masks[i]&used)for i in groups[x]),x))
 for i in groups[c]:
  if not masks[i]&used:search(rem-{c},used|masks[i],chosen+[i])
search(set(range(10)),0,[])
def square(ids):
 A=[[-1]*10 for _ in range(10)]
 for i in ids:
  c0=T[i][0]
  for r,c in enumerate(T[i]):assert A[r][c]<0;A[r][c]=c0
 assert A[0]==list(range(10)) and all(sorted(row)==list(range(10))for row in A)
 assert all(sorted(A[r][c]for r in range(10))==list(range(10))for c in range(10));return A
mates=sorted(square(ids)for ids in solutions)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'transversal_input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'exact_cover_nodes':nodes,'normalized_classical_mates':len(mates),'mates':mates,
 'normalization':'A[0,c]=c, quotient only by global A-symbol relabeling','scope':'One fixed literal Weisner L; no restriction on mate A beyond Latin and orthogonal to L.'}
(P/'frontier-20261029-weisner-all-classical-mates-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='mates'},indent=2))
