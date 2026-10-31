#!/usr/bin/env python3
"""Independent exact Q(sqrt(5)) replay of the 15-context 4D witness."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;w=P/'frontier-20261029-600cell-circulant4d-core-v1.json';raw=w.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='665517cf4f42ad2ddc1b9f83893449e4cb26d0c5802c0a46476cafd9e2c8073c';D=json.loads(raw)
V=[tuple(tuple(c)for c in v)for v in D['rays']];C=[tuple(x)for x in D['contexts']]
def neg(v):return tuple((-a,-b)for a,b in v)
def inn(v,w):return(sum(a*c+5*b*d for(a,b),(c,d)in zip(v,w)),sum(a*d+b*c for(a,b),(c,d)in zip(v,w)))
assert len(V)==60 and len(set(V))==60 and all(v==min(v,neg(v)) and inn(v,v)==(16,0)for v in V)
# Regenerate conventional equal-norm 600-cell coordinates, independently of the stored labels.
source=set()
for i in range(4):
 v=tuple((4,0)if j==i else(0,0)for j in range(4));source.add(min(v,neg(v)))
for signs in itertools.product((1,-1),repeat=4):
 v=tuple((2*x,0)for x in signs);source.add(min(v,neg(v)))
for p in itertools.permutations(range(4)):
 if sum(p[i]>p[j]for i in range(4)for j in range(i+1,4))%2:continue
 for x,y,z in itertools.product((1,-1),repeat=3):
  b=((0,0),(2*x,0),(y,y),(-z,z));v=tuple(b[j]for j in p);source.add(min(v,neg(v)))
assert source==set(V)
assert len(C)==15 and len(set(C))==15 and all(len(set(q))==4 and all(0<=r<60 for r in q)for q in C)
ids=sorted({j for q in C for j in q});assert len(ids)==30 and set(collections.Counter(j for q in C for j in q).values())=={2}
# Compute all 435 original selected-vector inner products, not merely the displayed bases.
Gm={(i,j):inn(V[i],V[j])for i,j in itertools.combinations(ids,2)}
for q in C:
 assert all(Gm[tuple(sorted((a,b)))]==(0,0)for a,b in itertools.combinations(q,2))
H=[set()for _ in range(15)]
for i,j in itertools.combinations(range(15),2):
 common=set(C[i])&set(C[j]);assert len(common)<=1
 if common:H[i].add(j);H[j].add(i)
assert all(H[i]=={j for j in range(15)if(j-i)%15 in(1,4,11,14)}for i in range(15))
assert D['families']==[[i for i in range(15)if i%3==k]for k in range(3)]
assert all(not(H[i]&set(f))for f in D['families']for i in f)
J=[{j for j in range(15)if i%3!=j%3 and j not in H[i]}for i in range(15)]
assert all(J[i]=={j for j in range(15)if(j-i)%15 in(2,5,7,8,10,13)}for i in range(15))
def triangles(g):return sum(j in g[i] and k in g[i] and k in g[j]for i,j,k in itertools.combinations(range(15),3))
old=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';oldraw=old.read_bytes();assert hashlib.sha256(oldraw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';K=[set()for _ in range(15)]
for z in json.loads(oldraw)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;K[u].add(v);K[v].add(u)
assert triangles(J)==35 and triangles(K)==29
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'witness_sha256':hashlib.sha256(raw).hexdigest(),
 'old_core_sha256':hashlib.sha256(oldraw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source_rays':len(V),'selected_rays':len(ids),'original_vector_inner_products_checked':len(Gm),'bases':len(C),
 'each_selected_ray_in_exactly_two_bases':True,'H4_degree':4,'H6_degree':6,
 'new_H6_triangles':triangles(J),'old_H6_triangles':triangles(K),'nonisomorphic_by_triangle_count':True,'status':'PASS'}
(P/'frontier-20261029-600cell-circulant4d-core-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
