#!/usr/bin/env python3
"""Exact all-mates pair-graph rigidity certificate for Weisner Figure1 L."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-ols10-switch-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='394c59221d0526ca623d46925d4d82e68d13ddb55b6c45f5bdada1ee622ff172'
G={'__file__':str(src)};exec(compile(raw.decode().split("if __name__",1)[0],str(src),'exec'),G);G['check_table']();L=[[G['TABLE'][r][c][1]for c in range(10)]for r in range(10)]
T=[];nodes=0
def rec(r,usedc,usedl,path):
 global nodes
 nodes+=1
 if r==10:T.append(tuple(path));return
 for c in range(10):
  a=L[r][c]
  if not(usedc>>c&1)and not(usedl>>a&1):path.append(c);rec(r+1,usedc|1<<c,usedl|1<<a,path);path.pop()
rec(0,0,0,[]);assert T==sorted(T)
masks=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T];ic=[];il=[]
for t in T:
 a=[0]*10;b=[0]*10
 for r,c in enumerate(t):a[c]=r;b[L[r][c]]=r
 ic.append(a);il.append(b)
def comps(a,b):
 x=T[a];pc=[ic[b][x[r]]for r in range(10)];pl=[il[b][L[r][x[r]]]for r in range(10)];rem=set(range(10));out=[]
 while rem:
  v=min(rem);todo=[v];seen={v}
  while todo:
   v=todo.pop()
   for w in(pc[v],pl[v]):
    if w not in seen:seen.add(w);todo.append(w)
  rem-=seen;out.append(tuple(sorted(seen)))
 return tuple(sorted(out,key=lambda x:(len(x),x)))
trades=[];compat=0
for a,b in itertools.combinations(range(len(T)),2):
 if masks[a]&masks[b]:continue
 compat+=1;C=comps(a,b)
 if len(C)>1:trades.append((a,b,C))
groups={c:[i for i,t in enumerate(T)if t[0]==c]for c in range(10)}
def proof(rem,used):
 if not rem:return {'SAT':True}
 opts={c:[i for i in groups[c]if not(masks[i]&used)]for c in rem};c=min(rem,key=lambda j:(len(opts[j]),j))
 return {'column':c,'branches':[[i,proof(rem-{c},used|masks[i])]for i in opts[c]]}
cert=[];trees=0
for a,b,C in trades:
 rem=set(range(10))-{T[a][0],T[b][0]};q=proof(rem,masks[a]|masks[b]);cert.append({'a':a,'b':b,'components':C,'proof':q})
 def count(x):return 1+sum(count(y)for i,y in x.get('branches',[]))
 def sat(x):return x.get('SAT',False)or any(sat(y)for i,y in x.get('branches',[]))
 trees+=count(q);assert not sat(q)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'source':'Weisner1963 Figure1 second Latin coordinate','T':T,'transversals':len(T),'DFS_nodes':nodes,
 'compatible_pairs':compat,'disconnected_pairs':len(trades),'proof_nodes':trees,'trade_certificates':cert,
 'scope':'All classical mates of this literal L; certificate trees exclude extending any disconnected pair.'}
(P/'frontier-20261029-weisner-all-mates-trade-census-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('T','trade_certificates')},indent=2))
