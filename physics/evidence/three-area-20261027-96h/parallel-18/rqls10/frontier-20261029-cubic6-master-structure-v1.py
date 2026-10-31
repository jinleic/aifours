#!/usr/bin/env python3
"""All 6D bases from alphabet {0,1,zeta3}: exact support/intersection census."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
def canon(x):
 a=next(z for z in x if z>=0);return tuple((z-a)%3 if z>=0 else -1 for z in x)
V=sorted({canon(x)for x in itertools.product((-1,0,1),repeat=6)if max(x)>=0});assert len(V)==665
def orth(a,b):
 q=[0,0,0]
 for x,y in zip(a,b):
  if x>=0 and y>=0:q[(y-x)%3]+=1
 return q[0]==q[1]==q[2]
ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 if orth(V[i],V[j]):ad[i]|=1<<j;ad[j]|=1<<i
B=[];nodes=0
def dfs(q,can):
 global nodes
 nodes+=1
 if len(q)==6:B.append(tuple(q));return
 if len(q)+can.bit_count()<6:return
 while can:
  x=can&-can;can-=x;i=x.bit_length()-1;dfs(q+[i],can&ad[i])
dfs([], (1<<len(V))-1);B.sort();assert len(B)==153
singles={i for i,v in enumerate(V)if sum(x>=0 for x in v)==1};profiles=collections.Counter();Z=[];A=[];odd=[]
for j,q in enumerate(B):
 n=sum(x in singles for x in q);profiles[n]+=1
 if n==0:Z.append(j)
 elif n==6:A.append(j)
 else:odd.append(j)
assert profiles=={0:40,1:72,3:40,6:1}
deg=[]
for q in B:deg.append(sum(len(set(q)&set(w))==1 for w in B))
assert all(deg[j]==0 for j in Z)
assert len(A)==1 and all(j in Z for j,q in enumerate(B)if j!=A[0] and not(set(q)&set(B[A[0]])))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'alphabet':'{0,1,zeta3}, projective normalization','ray_count':len(V),'basis_count':len(B),'DFS_nodes':nodes,
 'singleton_histogram':dict(profiles),'zero_singleton_have_no_single_intersection':True,'standard_disjoint_bases_all_zero_singleton':True,
 'rays':V,'bases':B,'single_intersection_degrees':deg,'scope':'Full alphabet, not only one parity core; exact integer root-count arithmetic.'}
(P/'frontier-20261029-cubic6-master-structure-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('rays','bases','single_intersection_degrees')},indent=2))
