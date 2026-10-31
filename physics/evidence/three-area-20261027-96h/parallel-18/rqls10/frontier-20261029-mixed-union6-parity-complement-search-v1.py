#!/usr/bin/env python3
"""Exact bounded 6D complement search over union of full cubic and real-sign source rays."""
import datetime,hashlib,itertools,json,time
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=src.read_bytes();data=json.loads(raw);target=[set()for _ in range(15)]
for z in data['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;target[u].add(v);target[v].add(u)
assert all(len(q)==6 for q in target)
def canon(x):
 z=next(a for a in x if a>=0);return tuple((a-z)%6 if a>=0 else -1 for a in x)
V=sorted({canon(x)for alphabet in [(-1,0,2,4),(-1,0,3)]for x in itertools.product(alphabet,repeat=6)if max(x)>=0});assert len(V)==1666;vi={v:i for i,v in enumerate(V)}
roots=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)];ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 a=b=0
 for x,y in zip(V[i],V[j]):
  if x>=0 and y>=0:u,v=roots[(y-x)%6];a+=u;b+=v
 if a==b==0:ad[i]|=1<<j;ad[j]|=1<<i
B=[]
def dfs(q,can):
 if len(q)==6:B.append(tuple(q));return
 if len(q)+can.bit_count()<6:return
 while can:
  bit=can&-can;can-=bit;i=bit.bit_length()-1;dfs(q+[i],can&ad[i])
dfs([], (1<<len(V))-1);B.sort();assert len(B)==3386
bi={q:i for i,q in enumerate(B)};rays=[sum(1<<r for r in q)for q in B];adj0=[0]*len(B);adj1=[0]*len(B)
for i,j in itertools.combinations(range(len(B)),2):
 x=(rays[i]&rays[j]).bit_count()
 if x==0:adj0[i]|=1<<j;adj0[j]|=1<<i
 elif x==1:adj1[i]|=1<<j;adj1[j]|=1<<i
gens=[]
for k in range(5):
 t=list(range(6));t[k],t[k+1]=t[k+1],t[k];gens.append([vi[canon(tuple(v[j]for j in t))]for v in V])
gens.append([vi[canon(tuple(-x%6 if x>=0 else -1 for x in v))]for v in V])
left=set(range(len(B)));orbits=[]
while left:
 k=min(left);orb={k};stack=[k]
 while stack:
  i=stack.pop()
  for g in gens:
   j=bi[tuple(sorted(g[x]for x in B[i]))]
   if j not in orb:orb.add(j);stack.append(j)
 left-=orb;orbits.append(sorted(orb))
viable=[i for i in range(len(B))if adj1[i].bit_count()>=6];domain=sum(1<<i for i in viable);reps=[x[0]for x in orbits if x[0]in viable]
start=time.monotonic();deadline=start+75;nodes=0;found=None;timeout=False;trials=[]
def search(ass,used,once,twice):
 global nodes,found,timeout
 nodes+=1
 if nodes%512==0 and time.monotonic()>deadline:timeout=True;return
 if len(ass)==15:found=ass.copy();return
 v0=None;best=None
 for v in range(15):
  if v in ass:continue
  q=domain&~used
  for w,k in ass.items():q&=adj1[k] if w in target[v] else adj0[k]
  if best is None or q.bit_count()<best.bit_count():v0=v;best=q
  if not best:return
 while best and found is None and not timeout:
  bit=best&-best;best-=bit;k=bit.bit_length()-1;R=rays[k]
  if R&twice:continue
  ass[v0]=k;search(ass,used|bit,once|R,twice|(once&R));del ass[v0]
for r in reps:
 before=nodes;search({0:r},1<<r,rays[r],0);trials.append({'root_basis':r,'nodes':nodes-before,'complete':not timeout and found is None,'found':found is not None})
 if found is not None or timeout:break
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'ray_count':len(V),'basis_count':len(B),'participating_rays':len({r for q in B for r in q}),
 'orbits':[{'representative':o[0],'size':len(o),'degree':adj1[o[0]].bit_count()}for o in orbits],
 'nodes':nodes,'elapsed_seconds':round(time.monotonic()-start,6),'trials':trials,'status':'SAT' if found is not None else 'UNKNOWN_TIMEOUT' if timeout else 'EXHAUSTED',
 'scope':'One fixed 6D complement graph and union of full cubic and real-sign source only; SAT requires exact independent replay and 10D extension.'}
if found is not None:
 Q=[B[found[i]]for i in range(15)];edge={}
 for a,b in itertools.combinations(range(15),2):
  x=set(Q[a])&set(Q[b]);assert len(x)==(1 if b in target[a] else 0)
  if x:edge[f'{a},{b}']=V[next(iter(x))]
 assert len(edge)==45 and len(set(edge.values()))==45
 obj.update(contexts=[[V[i]for i in q]for q in Q],edge_vectors=edge)
(P/'frontier-20261029-mixed-union6-parity-complement-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('contexts','edge_vectors')},indent=2))
