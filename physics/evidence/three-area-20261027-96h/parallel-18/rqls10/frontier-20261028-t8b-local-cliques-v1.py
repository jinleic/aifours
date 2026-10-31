#!/usr/bin/env python3
"""All exact 8-ray ONBs in the explicit non-Butson T8B Fourier QLS8."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-t8b-nonbutson-explicit-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='6ce6e5df6b6a7901d8822971dffdc1d05c17cc05dbb5f2687664cf568701b0cd'
exec(compile(raw.decode().split('nodes=0;found=None',1)[0],str(src),'exec'),globals())
local=list(itertools.product(range(8),repeat=2));adj=[]
for a in local:
 m=0
 for j,b in enumerate(local):
  if a!=b and O(a,b):m|=1<<j
 adj.append(m)
cliques=[];nodes=0
def dfs(path,candidates):
 global nodes
 nodes+=1
 if len(path)==8:cliques.append(tuple(path));return
 if len(path)+candidates.bit_count()<8:return
 while candidates:
  b=candidates&-candidates;i=b.bit_length()-1;candidates-=b;dfs(path+[i],candidates&adj[i])
dfs([],(1<<64)-1);assert len(cliques)==24
rectcols={(0,4),(1,2),(3,7),(5,6)};kind=collections.Counter()
for q in cliques:
 rc=[local[i]for i in q];rs={r for r,c in rc};cs={c for r,c in rc}
 if len(rs)==1:kind['row']+=1
 elif len(cs)==1:kind['column']+=1
 else:
  assert tuple(sorted(cs)) in rectcols and (rs=={0,2,4,6}or rs=={1,3,5,7}) and len(rc)==8
  kind['parity_rectangle']+=1
assert kind=={'row':8,'column':8,'parity_rectangle':8}
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'local_checker_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'degree_histogram':dict(collections.Counter(x.bit_count()for x in adj)),
 'DFS_nodes':nodes,'clique_count':len(cliques),'kind_counts':dict(kind),'cliques':[list(q)for q in sorted(cliques)]}
(P/'frontier-20261028-t8b-local-cliques-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='cliques'},indent=2))
