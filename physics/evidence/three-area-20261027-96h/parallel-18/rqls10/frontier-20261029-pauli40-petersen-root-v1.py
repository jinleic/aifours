#!/usr/bin/env python3
"""Verify each parity-context graph is the line graph of Petersen."""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli40-parity-core-census-v2.json';raw=src.read_bytes();D=json.loads(raw);B=D['bases']
assert len(D['records'])==64
p=[set()for _ in range(10)]
def add(a,b):p[a].add(b);p[b].add(a)
for i in range(5):add(i,(i+1)%5);add(i+5,(i+2)%5+5);add(i,i+5)
assert all(len(x)==3 for x in p)
def find_iso(G):
 mapping={};used=set();nodes=0
 def rec():
  nonlocal nodes
  nodes+=1
  if len(mapping)==10:return mapping.copy()
  candidates={v:[w for w in range(10)if w not in used and all((u in G[v])==(mapping[u] in p[w])for u in mapping)]for v in range(10)if v not in mapping}
  v=min(candidates,key=lambda z:(len(candidates[z]),-sum(u in mapping for u in G[z]),z))
  for w in candidates[v]:
   mapping[v]=w;used.add(w);q=rec()
   if q is not None:return q
   used.remove(w);del mapping[v]
  return None
 return rec(),lambda:nodes
records=[]
for item in D['records']:
 Q=[set(B[i])for i in item['basis_indices']];adj=[set()for _ in range(15)]
 for i,j in itertools.combinations(range(15),2):
  if Q[i]&Q[j]:adj[i].add(j);adj[j].add(i)
 tri=[q for q in itertools.combinations(range(15),3)if all(j in adj[i]for i,j in itertools.combinations(q,2))];assert len(tri)==10
 owners=[[i for i,t in enumerate(tri)if v in t]for v in range(15)];assert all(len(q)==2 for q in owners)
 E={tuple(sorted(q))for q in owners};assert len(E)==15
 G=[set()for _ in range(10)]
 for a,b in E:G[a].add(b);G[b].add(a)
 assert all(len(q)==3 for q in G)
 assert all((j in adj[i])==bool(set(owners[i])&set(owners[j]))for i,j in itertools.combinations(range(15),2))
 phi,nn=find_iso(G);assert phi is not None and all((j in G[i])==(phi[j]in p[phi[i]])for i,j in itertools.combinations(range(10),2))
 records.append({'basis_indices':item['basis_indices'],'triangle_to_petersen':phi,'isomorphism_nodes':nn()})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'cases':len(records),'all_context_graphs_line_Petersen':True,
 'records':records,'status':'PASS'}
(P/'frontier-20261029-pauli40-petersen-root-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='records'},indent=2))
