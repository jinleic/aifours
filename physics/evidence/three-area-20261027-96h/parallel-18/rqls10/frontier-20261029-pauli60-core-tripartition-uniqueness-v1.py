#!/usr/bin/env python3
"""Exhaustive colorings of the explicit 4D parity-core context graph."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-search-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8fb98404025a8fcd521554cd0b9eced293bb9b84488ba970797b6a9174fcbeca';D=json.loads(raw);B=[set(x)for x in D['bases_1indexed']];adj=[set()for _ in B]
for i,j in itertools.combinations(range(15),2):
 if B[i]&B[j]:adj[i].add(j);adj[j].add(i)
colors=[-1]*15;colors[0]=0;solutions=[];nodes=0
def rec(unassigned):
 global nodes
 nodes+=1
 if not unassigned:solutions.append(tuple(colors));return
 v=min(unassigned,key=lambda j:(sum(all(colors[x]!=c for x in adj[j])for c in range(3)),-len(adj[j]),j))
 for c in range(3):
  if all(colors[x]!=c for x in adj[v]):colors[v]=c;rec(unassigned-{v});colors[v]=-1
rec(set(range(1,15)))
balanced=[q for q in solutions if sorted(collections.Counter(q).values())==[5,5,5]]
partitions={tuple(sorted(tuple(i for i,x in enumerate(q)if x==c)for c in range(3)))for q in balanced}
assert len(solutions)==30 and len(balanced)==2 and len(partitions)==1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'DFS_nodes':nodes,'all_colorings_fixing_vertex0':len(solutions),
 'balanced_colorings_fixing_vertex0':len(balanced),'balanced_unlabeled_partitions':len(partitions),
 'group_sizes':[5,5,5],'balanced_partitions':[list(x)for x in partitions],
 'development_note':'Initial unchecked assertion mistakenly assumed all 3-colorings balanced; corrected after inspecting 30 solutions.','status':'PASS'}
(P/'frontier-20261029-pauli60-core-tripartition-uniqueness-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
