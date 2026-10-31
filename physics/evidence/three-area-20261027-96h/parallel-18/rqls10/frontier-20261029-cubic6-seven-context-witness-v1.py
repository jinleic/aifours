#!/usr/bin/env python3
"""Exact original-vector verification of a 21-ray, seven-basis cubic master core."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cubic6-master-structure-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='54ed33497b845b6123eaa39e5f295e5d3bd9a2f4db158341b3dc614b1e1502c1';D=json.loads(raw);V=D['rays'];B=D['bases'];ids=[0,31,50,65,87,113,116];Q=[B[i]for i in ids]
# In Z[omega], w²=-w-1; compute original Gram coefficient pairs.
R=[(1,0),(0,1),(-1,-1)]
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def cj(x):return(x[0]-x[1],-x[1])
def dot(a,b):
 x=y=0
 for i,j in zip(a,b):
  if i>=0 and j>=0:u,v=mul(cj(R[i]),R[j]);x+=u;y+=v
 return(x,y)
for q in Q:
 for a,b in itertools.combinations(q,2):assert dot(V[a],V[b])==(0,0)
occ=collections.Counter(a for q in Q for a in q);assert len(occ)==21 and set(occ.values())=={2}
assert all(len(set(a)&set(b))==1 for a,b in itertools.combinations(Q,2))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'master_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'basis_indices':ids,'rays':21,'bases':7,'original_orthogonality_checks':105,
 'ray_incidence':2,'context_graph':'K7','status':'PASS'}
(P/'frontier-20261029-cubic6-seven-context-witness-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
