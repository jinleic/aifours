#!/usr/bin/env python3
"""Independent MRV-transversal / 20-vertex DSU trade census for Parker L."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-parker-13ray-result-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5'
L=json.loads(raw)['partial_witness']['labels'];T=[];nodes=0

def rec(remaining,columns,labels,cur):
 global nodes
 nodes+=1
 if not remaining:T.append(tuple(cur));return
 best=min(remaining,key=lambda r:sum(c not in columns and L[r][c]not in labels for c in range(10)))
 for c in range(10):
  v=L[best][c]
  if c in columns or v in labels:continue
  cur[best]=c;rec(remaining-{best},columns|{c},labels|{v},cur);cur[best]=-1
rec(set(range(10)),set(),set(),[-1]*10);T.sort();assert len(set(T))==len(T)
masks=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T]
def comps(a,b):
 x,y=T[a],T[b];parent=list(range(20))
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 def union(i,j):
  i=find(i);j=find(j)
  if i!=j:parent[j]=i
 C={y[r]:r for r in range(10)};D={L[r][y[r]]:r for r in range(10)}
 for r in range(10):union(r,10+r);union(r,10+C[x[r]]);union(r,10+D[L[r][x[r]]])
 ans=collections.defaultdict(list)
 for r in range(10):ans[find(r)].append(r)
 return tuple(sorted((tuple(a)for a in ans.values()),key=lambda x:(len(x),x)))
trades=[];compatible=0
for a,b in itertools.combinations(range(len(T)),2):
 if masks[a]&masks[b]:continue
 compatible+=1;C=comps(a,b)
 if len(C)>1:trades.append((a,b,C))
tri=set();pair_count=collections.Counter()
for x,y in itertools.combinations(trades,2):
 I=tuple(sorted(set(x[:2]+y[:2])))
 if any(masks[a]&masks[b]for a,b in itertools.combinations(I,2)):continue
 pair_count[str(len(I))]+=1
 if len(I)==3:tri.add(I)
assert pair_count['4']==0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'search_nodes':nodes,'transversals':len(T),'compatible_transversal_pairs':compatible,
 'disconnected_color_pairs':len(trades),'compatible_trade_pair_vertex_count':dict(pair_count),'compatible_trade_triangles':len(tri),
 'T':T,'trades':[{'a':a,'b':b,'components':c}for a,b,c in trades],
 'scope':'Independent original L; dynamic MRV and 20-vertex DSU, no assumption of extension of partial trade sets.'}
(P/'frontier-20261029-parker-trade-dsu-replay-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('T','trades')},indent=2))
