#!/usr/bin/env python3
"""Exact bounded 6D complement search over union of full cubic and real-sign source rays."""
import collections,datetime,hashlib,itertools,json,time
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
inc=[0]*len(V)
for j,b in enumerate(B):
 bit=1<<j
 for x in b:inc[x]|=bit
import gzip
nodes=0;types=collections.Counter()
def prove(assign,used,once,twice):
 global nodes
 nodes+=1
 if len(assign)==15:raise RuntimeError('SAT branch; stop no-go claim')
 domains={}
 for v in range(15):
  if v in assign:continue
  q=domain&~used
  for w,k in assign.items():q&=adj1[k] if w in target[v] else adj0[k]
  if not q:types['empty']+=1;return ['empty',v]
  domains[v]=q
 for v,k in assign.items():
  need=sorted(w for w in target[v]if w not in assign)
  if not need:continue
  taken=0
  for w in target[v]:
   if w in assign:taken|=rays[k]&rays[assign[w]]
  missing=[r for r in B[k]if not(taken>>r&1)];assert len(missing)==len(need)
  allowed=[sum(1<<j for j,w in enumerate(need)if domains[w]&inc[r])for r in missing]
  order=sorted(allowed,key=int.bit_count)
  def match(j,used2):
   if j==len(order):return True
   opts=order[j]&~used2
   while opts:
    bit=opts&-opts;opts-=bit
    if match(j+1,used2|bit):return True
   return False
  if not match(0,0):
   for mask in range(1,1<<len(missing)):
    union=0
    for j in range(len(missing)):
     if mask>>j&1:union|=allowed[j]
    if union.bit_count()<mask.bit_count():
     types['hall']+=1;return ['hall',v,[missing[j]for j in range(len(missing))if mask>>j&1]]
   raise AssertionError('Hall witness missing')
 v=min(domains,key=lambda v:domains[v].bit_count());opts=domains[v];children=[]
 while opts:
  bit=opts&-opts;opts-=bit;k=bit.bit_length()-1;r=rays[k]
  if r&twice:continue
  assign[v]=k;children.append([k,prove(assign,used|bit,once|r,twice|(once&r))]);del assign[v]
 types['branch']+=1;return ['branch',v,children]
proofs=[];start=time.monotonic()
for orbit in orbits:
 root=orbit[0]
 if not(domain>>root&1):continue
 before=nodes;tree=prove({0:root},1<<root,rays[root],0);proofs.append({'root':root,'nodes':nodes-before,'tree':tree})
 print('root',root,'nodes',nodes-before,flush=True)
record={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rays':V,'bases':B,'orbits':orbits,'proofs':proofs,
 'nodes':nodes,'node_types':dict(types),'scope':'full cubic plus real-sign union source; one 6D target; Hall-pruned exhaustive branch forest.'}
out=P/'frontier-20261029-mixed-union6-complement-proof-v1.json.gz'
with gzip.open(out,'wt',encoding='utf8')as f:json.dump(record,f,separators=(',',':'))
summary={'source_sha256':record['source_sha256'],'core_sha256':record['core_sha256'],'clock_finish':record['clock_finish'],
 'ray_count':len(V),'basis_count':len(B),'basis_orbits':len(orbits),'nodes':nodes,'node_types':dict(types),
 'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,4),'status':'EXHAUSTED'}
(P/'frontier-20261029-mixed-union6-complement-proof-v1.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
