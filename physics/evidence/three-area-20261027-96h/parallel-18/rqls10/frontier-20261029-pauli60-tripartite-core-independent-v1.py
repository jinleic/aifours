#!/usr/bin/env python3
"""Independent literal Gaussian-integer original-vector check of one 30–15 core."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-search-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8fb98404025a8fcd521554cd0b9eced293bb9b84488ba970797b6a9174fcbeca';data=json.loads(raw);assert data['status']=='sat'
# Independently transcribed from Waegell-Aravind Table1 (not the producer vector file).
S={5:'1 1 1 1',6:'1 -1 1 -1',7:'1 1 -1 -1',8:'1 -1 -1 1',13:'1 1 0 0',14:'1 -1 0 0',15:'0 0 1 1',16:'0 0 1 -1',
33:'1 1 i i',34:'1 -1 i -i',35:'1 1 -i -i',36:'1 -1 -i i',38:'1 1 -1 1',39:'1 -1 1 1',40:'1 -1 -1 -1',
41:'1 0 0 i',43:'0 1 i 0',44:'1 0 0 -i',45:'1 i i 1',47:'1 i -i -1',48:'1 -i -i 1',
50:'1 0 0 -1',51:'0 1 1 0',52:'0 1 -1 0',53:'1 1 -i i',54:'1 1 i -i',55:'1 -1 i i',57:'1 i 1 -i',59:'1 -i 1 i',60:'1 -i -1 -i'}
M={'0':(0,0),'1':(1,0),'-1':(-1,0),'i':(0,1),'-i':(0,-1)};V={k:tuple(M[x]for x in s.split())for k,s in S.items()}
def dot(a,b):return (sum(x*u+y*v for (x,y),(u,v)in zip(a,b)),sum(x*v-y*u for (x,y),(u,v)in zip(a,b)))
def norm(a):return sum(x*x+y*y for x,y in a)
assert all(norm(v)>0 for v in V.values())
for a,b in itertools.combinations(sorted(V),2):
 x,y=dot(V[a],V[b]);assert x*x+y*y!=norm(V[a])*norm(V[b])
B=data['bases_1indexed'];color=data['colors'];assert len(B)==15 and sorted(collections.Counter(color).values())==[5,5,5]
occ=collections.Counter(r for q in B for r in q);assert set(occ)==set(V) and set(occ.values())=={2}
for q in B:
 assert len(set(q))==4
 for a,b in itertools.combinations(q,2):assert dot(V[a],V[b])==(0,0)
groups=[[i for i in range(15)if color[i]==j]for j in range(3)];assert all(len(q)==5 for q in groups)
for i,j in itertools.combinations(range(15),2):
 shared=set(B[i])&set(B[j]);assert len(shared)<=1
 if shared:assert color[i]!=color[j]
G=[]
for a,b in ((0,1),(0,2),(1,2)):
 E=[]
 for i in groups[a]:E.append([next(iter(set(B[i])&set(B[j])),0)for j in groups[b]])
 G.append({'groups':[a,b],'shared_H4_ray_matrix':E})
for i in range(15):assert sum(bool(set(B[i])&set(B[j]))for j in range(15)if j!=i)==4
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'candidate_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'source':'https://arxiv.org/html/1109.1299v2#S2.T1',
 'rays':len(V),'pairwise_distinct_checks':435,'contexts':len(B),'orthogonality_checks':90,'incidence_per_ray':2,
 'context_group_sizes':[5,5,5],'context_graph_degree':4,'groups':groups,'cross_group_incidence':G,
 'scope':'Exact 4D partial parity core only. No 6D complement, no full 100-ray 1RQLS10.','status':'PASS'}
(P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
