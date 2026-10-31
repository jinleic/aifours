#!/usr/bin/env python3
"""Complete transversals and compatible 2-color trade pairs for Parker L."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-exact-switch-grow-result-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2023d098dc9c81b437b698601ed8709161794b7434934f83abc2f4219a6dcb6e'
L=json.loads(raw)['partial_witness']['labels'];N=10;T=[];nodes=0
def rec(r,usedc,usedl,path):
 global nodes
 nodes+=1
 if r==10:T.append(tuple(path));return
 for c in range(10):
  x=L[r][c]
  if not(usedc>>c&1)and not(usedl>>x&1):path.append(c);rec(r+1,usedc|1<<c,usedl|1<<x,path);path.pop()
rec(0,0,0,[]);assert T==sorted(T)
masks=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T];ic=[];il=[]
for t in T:
 a=[0]*10;b=[0]*10
 for r,c in enumerate(t):a[c]=r;b[L[r][c]]=r
 ic.append(a);il.append(b)
def components(i,j):
 x=T[i];pc=[ic[j][x[r]]for r in range(10)];pl=[il[j][L[r][x[r]]]for r in range(10)];remaining=set(range(10));out=[]
 while remaining:
  x=min(remaining);stack=[x];seen={x}
  while stack:
   a=stack.pop()
   for b in (pc[a],pl[a]):
    if b not in seen:seen.add(b);stack.append(b)
  remaining-=seen;out.append(tuple(sorted(seen)))
 return tuple(sorted(out,key=lambda z:(len(z),z)))
trades=[];compatible=0
for a in range(len(T)):
 for b in range(a+1,len(T)):
  if masks[a]&masks[b]:continue
  compatible+=1;C=components(a,b)
  if len(C)>1:trades.append((a,b,C))
pairs=collections.Counter();triangles=set()
for x,y in itertools.combinations(trades,2):
 ids=set(x[:2]+y[:2]);ids=tuple(sorted(ids))
 if any(masks[a]&masks[b]for a,b in itertools.combinations(ids,2)):continue
 pairs[str(len(ids))]+=1
 if len(ids)==3:triangles.add(ids)
assert pairs['4']==0 and len(trades)==162 and len(triangles)==24
for tr in triangles:
 C=[components(a,b)for a,b in itertools.combinations(tr,2)]
 assert all(tuple(map(len,x))==(3,7) and x[0]==(7,8,9)for x in C)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'search_nodes':nodes,'transversals':len(T),'compatible_transversal_pairs':compatible,
 'disconnected_color_pairs':len(trades),'trade_pair_component_profiles':dict(collections.Counter(str(tuple(map(len,c)))for a,b,c in trades)),
 'compatible_trade_pair_vertex_count':dict(pairs),'compatible_trade_triangles':len(triangles),'all_triangle_short_rows':[7,8,9],
 'T':T,'trades':[{'a':a,'b':b,'components':c}for a,b,c in trades],
 'scope':'Exact census for this one Parker resolution L; compatible sets need not themselves extend to a full orthogonal mate. Not an arbitrary-L theorem.'}
(P/'frontier-20261029-parker-all-mates-trade-census-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('T','trades')},indent=2))
