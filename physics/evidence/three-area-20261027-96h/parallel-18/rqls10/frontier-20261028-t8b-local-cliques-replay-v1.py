#!/usr/bin/env python3
"""Independent Q(zeta24) Gram + pivoted Bron–Kerbosch 8-clique replay."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-t8b-original-vector-replay-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f3a8a629b868105a2080001095a2800a4ba8471f8f816d85ea1e2ca8fc3daba7'
exec(compile(raw.decode().split('dup=[];orth={}',1)[0],str(src),'exec'),globals())
local=list(itertools.product(range(8),repeat=2));adj=[0]*64
for i,j in itertools.combinations(range(64),2):
 if gram(local[i],local[j])==Z:adj[i]|=1<<j;adj[j]|=1<<i
cliques=[];nodes=0
def BK(R,C,X):
 global nodes
 nodes+=1
 if len(R)+C.bit_count()<8:return
 if len(R)==8:cliques.append(tuple(sorted(R)));return
 u=C|X
 pivot=max((v for v in range(64)if u>>v&1),key=lambda v:(C&adj[v]).bit_count(),default=None)
 cand=C if pivot is None else C&~adj[pivot]
 while cand:
  bit=cand&-cand;v=bit.bit_length()-1;cand-=bit;BK(R+[v],C&adj[v],X&adj[v]);C&=~bit;X|=bit
BK([],(1<<64)-1,0);cliques=sorted(set(cliques));expected=json.loads((P/'frontier-20261028-t8b-local-cliques-v1.json').read_bytes())['cliques'];assert cliques==[tuple(q)for q in expected]
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'original_vector_checker_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'method':'Q(zeta24) exact Gram, pivoted Bron-Kerbosch','degree_histogram':dict(collections.Counter(x.bit_count()for x in adj)),
 'nodes':nodes,'clique_count':len(cliques),'matches_producer':True,'status':'PASS'}
(P/'frontier-20261028-t8b-local-cliques-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
