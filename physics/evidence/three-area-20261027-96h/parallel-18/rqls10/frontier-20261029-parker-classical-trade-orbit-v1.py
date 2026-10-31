#!/usr/bin/env python3
"""Find compatible independent two-color switches by exact classical trade BFS.
Outputs any 1RQLS candidate explicitly; separate original-vector replay needed.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-exact-switch-grow-result-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2023d098dc9c81b437b698601ed8709161794b7434934f83abc2f4219a6dcb6e'
w=json.loads(raw)['partial_witness'];L=w['labels'];V=w['array'];D=w['denominator'];N=10
def canon(v):
 v=tuple(v);return v if next(x for x in v if x)>0 else tuple(-x for x in v)
local=sorted({canon(V[r][c])for r in range(7,10)for c in range(7,10)});assert len(local)==3
A=[]
for r in range(10):
 row=[]
 for c in range(10):
  q=canon(V[r][c]);nz=[i for i,x in enumerate(q)if x]
  row.append(nz[0] if len(nz)==1 else 7+local.index(q))
 A.append(row)
def check(A):
 assert all(set(row)==set(range(N))for row in A)
 assert all({A[r][c]for r in range(N)}==set(range(N))for c in range(N))
 assert len({(A[r][c],L[r][c])for r,c in itertools.product(range(N),repeat=2)})==100
check(A)
def normalize(A):
 d={x:i for i,x in enumerate(A[0])};return tuple(d[x]for row in A for x in row)
def unflatten(A):return [list(A[10*r:10*r+10])for r in range(10)]
def comps(A,a,b):
 cells={10*r+c for r,c in itertools.product(range(10),repeat=2)if A[r][c] in (a,b)};adj={x:set()for x in cells}
 for B in ([[10*r+c for c in range(10)]for r in range(10)]+[[10*r+c for r in range(10)]for c in range(10)]+[[10*r+c for r,c in itertools.product(range(10),repeat=2)if L[r][c]==t]for t in range(10)]):
  vals=[x for x in B if x in cells];assert len(vals)==2;x,y=vals;adj[x].add(y);adj[y].add(x)
 out=[]
 while cells:
  todo=[min(cells)];C=set()
  while todo:
   x=todo.pop()
   if x in C:continue
   C.add(x);todo.extend(adj[x]-C)
  cells-=C;out.append(tuple(sorted(C)))
 return out

def options(A):
 out=[]
 for a,b in itertools.combinations(range(10),2):
  C=comps(A,a,b)
  if len(C)>1:out.extend((a,b,x)for x in C)
 return out
queue=collections.deque([(normalize(A),0)]);seen={queue[0][0]};tested=0;depthmax=0;count_hist=collections.Counter();best=None;first_multi=None;cap=5000
while queue and tested<cap:
 rawA,depth=queue.popleft();M=unflatten(rawA);tested+=1;depthmax=max(depthmax,depth);op=options(M);pairs=sorted(set((a,b)for a,b,C in op));count_hist[len(pairs)]+=1
 for i,pair in enumerate(pairs):
  for other in pairs[i+1:]:
   if set(pair).isdisjoint(other):
    opts=[next(q for q in op if q[:2]==pair),next(q for q in op if q[:2]==other)];first_multi={'A':M,'depth':depth,'switches':opts};break
  if first_multi:break
 if first_multi:break
 for a,b,C in op:
  T=[row[:]for row in M]
  for x in C:
   r,c=divmod(x,10);T[r][c]=b if T[r][c]==a else a
  H=normalize(T)
  if H not in seen:seen.add(H);queue.append((H,depth+1))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'tested':tested,'states_seen':len(seen),'frontier':len(queue),'depthmax':depthmax,
 'switchable_pair_histogram':dict(count_hist),'first_disjoint_color_pair_switches':first_multi,
 'boundary':'BFS is complete only if frontier is empty; all attainable classical mates for this fixed L are not implied unless trade connectivity is known.'}
(P/'frontier-20261029-parker-classical-trade-orbit-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
