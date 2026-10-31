#!/usr/bin/env python3
"""Bounded exact 6D complement embedding over {0,1,omega,omega²}.
SAT is partial 6D incidence, not a full QLS10; timeout makes no no-go claim.
"""
import collections,datetime,hashlib,itertools,json,time
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-parity-core-6d-projection-v1.json';raw=src.read_bytes();data=json.loads(raw);target=[set()for _ in range(15)]
for a,b in data['edges']:target[a].add(b);target[b].add(a)
assert all(len(q)==6 for q in target)
def canon(x):
 z=next(a for a in x if a>=0);return tuple((a-z)%3 if a>=0 else -1 for a in x)
V=sorted({canon(x)for x in itertools.product((-1,0,1,2),repeat=6)if max(x)>=0});vi={v:i for i,v in enumerate(V)};assert len(V)==1365
ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 count=[0,0,0]
 for a,b in zip(V[i],V[j]):
  if a>=0 and b>=0:count[(b-a)%3]+=1
 if count[0]==count[1]==count[2]:ad[i]|=1<<j;ad[j]|=1<<i
B=[]
def basis_dfs(path,can):
 if len(path)==6:B.append(tuple(path));return
 if len(path)+can.bit_count()<6:return
 while can:
  bit=can&-can;can-=bit;i=bit.bit_length()-1;basis_dfs(path+[i],can&ad[i])
basis_dfs([],(1<<len(V))-1);B.sort();assert len(B)==1609
bi={q:i for i,q in enumerate(B)};rays=[sum(1<<i for i in q)for q in B];adj0=[0]*len(B);adj1=[0]*len(B)
for i,j in itertools.combinations(range(len(B)),2):
 n=(rays[i]&rays[j]).bit_count()
 if n==0:adj0[i]|=1<<j;adj0[j]|=1<<i
 elif n==1:adj1[i]|=1<<j;adj1[j]|=1<<i
# Exact source automorphisms: adjacent coordinate swaps, each coordinate phase,
# and conjugation; enumerate their basis orbits before picking a root.
gens=[]
for k in range(5):
 s=list(range(6));s[k],s[k+1]=s[k+1],s[k];gens.append([vi[canon(tuple(v[j]for j in s))]for v in V])
for k in range(5):gens.append([vi[canon(tuple((x+int(j==k))%3 if x>=0 else -1 for j,x in enumerate(v)))]for v in V])
gens.append([vi[canon(tuple(-x%3 if x>=0 else -1 for x in v))]for v in V])
remaining=set(range(len(B)));orbits=[]
while remaining:
 start=min(remaining);orbit={start};stack=[start]
 while stack:
  i=stack.pop()
  for gen in gens:
   j=bi[tuple(sorted(gen[x]for x in B[i]))]
   if j not in orbit:orbit.add(j);stack.append(j)
 remaining-=orbit;orbits.append(sorted(orbit))
viable=[i for i in range(len(B))if adj1[i].bit_count()>=6];domain=sum(1<<i for i in viable);reps=[o[0]for o in orbits if o[0]in viable]
nodes=0

def prove(ass,used,once,twice):
 global nodes
 nodes+=1
 if len(ass)==15:raise RuntimeError('SAT branch contradicts expected no-go')
 pick=None;options=None
 for v in range(15):
  if v in ass:continue
  q=domain&~used
  for w,k in ass.items():q&=adj1[k] if w in target[v] else adj0[k]
  if options is None or q.bit_count()<options.bit_count():pick=v;options=q
  if not options:break
 children=[]
 while options:
  bit=options&-options;options-=bit;k=bit.bit_length()-1;R=rays[k]
  if R&twice:continue
  ass[pick]=k;child=prove(ass,used|bit,once|R,twice|(once&R));del ass[pick]
  children.append([k,child])
 return [pick,children]
proofs=[]
for root in reps:
 before=nodes;tree=prove({0:root},1<<root,rays[root],0);proofs.append({'root_basis':root,'nodes':nodes-before,'tree':tree})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'target_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'ray_count':len(V),'basis_count':len(B),'nodes':nodes,
 'orbits':orbits,'rays':V,'bases':B,'proofs':proofs,'scope':'One fixed H6 graph, source {0,1,omega,omega²}; exact exhaustive proof trees.'}
(P/'frontier-20261029-cubic6-fullphase-complement-proof-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('orbits','rays','bases','proofs')},indent=2))
