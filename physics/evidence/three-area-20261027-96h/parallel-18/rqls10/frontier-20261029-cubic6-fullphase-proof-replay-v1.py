#!/usr/bin/env python3
"""Independent Z[omega]/BK source generation + exact 51246-node proof replay."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cubic6-fullphase-complement-proof-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='246ceea122d922db1882023772d9dd99274d3def1f91ad2c30bf3223d71004f7';D=json.loads(raw)
# Generate source rays directly by support and arbitrary relative cubic phases.
V=[]
for n in range(1,7):
 for S in itertools.combinations(range(6),n):
  for phases in itertools.product(range(3),repeat=n-1):
   v=[-1]*6;v[S[0]]=0
   for i,x in zip(S[1:],phases):v[i]=x
   V.append(tuple(v))
V.sort();assert len(V)==len(set(V))==1365;vi={v:i for i,v in enumerate(V)}
R=[(1,0),(0,1),(-1,-1)]
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return(a[0]-a[1],-a[1])
def ortho(a,b):
 x=y=0
 for u,v in zip(a,b):
  if u>=0 and v>=0:c,d=mul(conj(R[u]),R[v]);x+=c;y+=d
 return x==0 and y==0
ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 if ortho(V[i],V[j]):ad[i]|=1<<j;ad[j]|=1<<i
B=[]
def bk(sel,can,ex,n):
 if n+can.bit_count()<6:return
 if n==6:B.append(tuple(i for i in range(len(V))if sel>>i&1));return
 U=can|ex;best=-1;pivot=-1
 while U:
  bit=U&-U;U-=bit;i=bit.bit_length()-1;k=(can&ad[i]).bit_count()
  if k>best:best=k;pivot=i
 todo=can if pivot<0 else can&~ad[pivot]
 while todo:
  bit=todo&-todo;todo-=bit;i=bit.bit_length()-1;bk(sel|bit,can&ad[i],ex&ad[i],n+1);can&=~bit;ex|=bit
bk(0,(1<<len(V))-1,0,0);B.sort();assert len(B)==1609
assert [list(v)for v in V]==D['rays'] and [list(b)for b in B]==D['bases']
Rm=[sum(1<<x for x in b)for b in B];A0=[0]*len(B);A1=[0]*len(B)
for i,j in itertools.combinations(range(len(B)),2):
 k=(Rm[i]&Rm[j]).bit_count()
 if k==0:A0[i]|=1<<j;A0[j]|=1<<i
 elif k==1:A1[i]|=1<<j;A1[j]|=1<<i
viable=[i for i in range(len(B))if A1[i].bit_count()>=6];domain=sum(1<<i for i in viable)
# Reconstruct subgroup orbits independently, including all six local phase generators.
def norm(v):
 a=next(x for x in v if x>=0);return tuple((x-a)%3 if x>=0 else -1 for x in v)
gens=[]
for j in range(5):
 p=list(range(6));p[j],p[j+1]=p[j+1],p[j];gens.append([vi[norm(tuple(v[k]for k in p))]for v in V])
for j in range(6):gens.append([vi[norm(tuple((v[k]+int(k==j))%3 if v[k]>=0 else -1 for k in range(6)))]for v in V])
gens.append([vi[norm(tuple(-x%3 if x>=0 else -1 for x in v))]for v in V]);bi={b:i for i,b in enumerate(B)}
remaining=set(range(len(B)));orbits=[]
while remaining:
 a=min(remaining);seen={a};stack=[a]
 while stack:
  i=stack.pop()
  for gen in gens:
   j=bi[tuple(sorted(gen[r]for r in B[i]))]
   if j not in seen:seen.add(j);stack.append(j)
 remaining-=seen;orbits.append(sorted(seen))
assert orbits==D['orbits'];reps=[q[0]for q in orbits if q[0]in viable];assert reps==[q['root_basis']for q in D['proofs']]
# Rebuild target graph directly from the independently checked 4D core.
core=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';corebytes=core.read_bytes()
assert hashlib.sha256(corebytes).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';G=[set()for _ in range(15)]
for z in json.loads(corebytes)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
assert all(len(z)==6 for z in G)
nodes=0
def check(tree,ass,used,once,twice):
 global nodes
 nodes+=1;assert len(ass)<15 and isinstance(tree,list) and len(tree)==2
 v,children=tree;assert v not in ass
 options=domain&~used
 for w,k in ass.items():options&=A1[k] if w in G[v] else A0[k]
 valid=[]
 while options:
  bit=options&-options;options-=bit;i=bit.bit_length()-1
  if not(Rm[i]&twice):valid.append(i)
 assert [i for i,ch in children]==valid
 for i,ch in children:
  bit=1<<i;Q=Rm[i];ass[v]=i;check(ch,ass,used|bit,once|Q,twice|(once&Q));del ass[v]
for q in D['proofs']:
 root=q['root_basis'];before=nodes;check(q['tree'],{0:root},1<<root,Rm[root],0);assert nodes-before==q['nodes']
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(raw).hexdigest(),
 'core_sha256':hashlib.sha256(corebytes).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'rays':len(V),'bases':len(B),'orbits':len(orbits),'root_representatives':reps,'literal_proof_nodes_replayed':nodes,
 'all_branches_rejected':True,'status':'PASS'}
(P/'frontier-20261029-cubic6-fullphase-proof-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
