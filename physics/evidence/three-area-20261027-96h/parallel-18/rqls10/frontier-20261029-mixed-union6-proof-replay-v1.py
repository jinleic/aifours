#!/usr/bin/env python3
"""Independent mixed-source Z[omega] and Hall proof replay."""
import collections,datetime,gzip,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;proof=P/'frontier-20261029-mixed-union6-complement-proof-v1.json.gz';raw=proof.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='0128ff598bdc0cba1323fad9508f8c5be9e40eaaf1820afe8f611abc7a33eeaa'
with gzip.open(proof,'rt',encoding='utf8')as f:D=json.load(f)
# Generate independently by support and relative phases, in sixth-root exponents.
V=set()
for phaseset in ((0,2,4),(0,3)):
 for n in range(1,7):
  for support in itertools.combinations(range(6),n):
   for phase in itertools.product(phaseset,repeat=n-1):
    q=[-1]*6;q[support[0]]=0
    for j,k in zip(support[1:],phase):q[j]=k
    V.add(tuple(q))
V=sorted(V);assert len(V)==1666 and [list(v)for v in V]==D['rays'];vi={v:i for i,v in enumerate(V)}
# An independent basis of Z[omega], omega²+omega+1=0, rather than producer's Z[zeta_6].
R=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return(a[0]-a[1],-a[1])
def orth(a,b):
 x=y=0
 for u,v in zip(a,b):
  if u>=0 and v>=0:c,d=mul(conj(R[u]),R[v]);x+=c;y+=d
 return x==y==0
ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 if orth(V[i],V[j]):ad[i]|=1<<j;ad[j]|=1<<i
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
bk(0,(1<<len(V))-1,0,0);B.sort();assert len(B)==3386 and [list(b)for b in B]==D['bases'];bi={b:i for i,b in enumerate(B)}
def norm(v):
 a=next(x for x in v if x>=0);return tuple((x-a)%6 if x>=0 else -1 for x in v)
gens=[]
# Star transpositions generate S6 but differ from the producer's adjacent generators.
for j in range(1,6):
 p=list(range(6));p[0],p[j]=p[j],p[0];gens.append([vi[norm(tuple(v[k]for k in p))]for v in V])
gens.append([vi[norm(tuple(-x%6 if x>=0 else -1 for x in v))]for v in V])
left=set(range(len(B)));orbits=[]
while left:
 i=min(left);seen={i};stack=[i]
 while stack:
  j=stack.pop()
  for gen in gens:
   k=bi[tuple(sorted(gen[x]for x in B[j]))]
   if k not in seen:seen.add(k);stack.append(k)
 left-=seen;orbits.append(sorted(seen))
assert orbits==D['orbits']
# Basis-neighbor masks, computed by incidence rather than pairwise intersections.
inc=[0]*len(V)
for i,q in enumerate(B):
 for r in q:inc[r]|=1<<i
full=(1<<len(B))-1;A0=[];A1=[];RM=[]
for q in B:
 seen=multi=0
 for r in q:multi|=seen&inc[r];seen|=inc[r]
 A0.append(full&~seen);A1.append(seen&~multi);RM.append(sum(1<<r for r in q))
domain=sum(1<<j for j in range(len(B))if A1[j].bit_count()>=6)
reps=[x[0]for x in orbits if domain>>x[0]&1];assert reps==[x['root']for x in D['proofs']]
core=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';corebytes=core.read_bytes();assert hashlib.sha256(corebytes).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';G=[set()for _ in range(15)]
for z in json.loads(corebytes)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
assert all(len(g)==6 for g in G)
counts=collections.Counter()
def check(tree,ass,used,once,twice):
 kind,v=tree[:2];counts[kind]+=1;assert len(ass)<15
 domains={}
 for x in range(15):
  if x in ass:continue
  q=domain&~used
  for y,k in ass.items():q&=A1[k]if y in G[x]else A0[k]
  domains[x]=q
 if kind=='empty':assert v not in ass and domains[v]==0;return
 if kind=='hall':
  assert v in ass;k=ass[v];need=sorted(x for x in G[v]if x not in ass);taken=0
  for x in G[v]:
   if x in ass:taken|=RM[k]&RM[ass[x]]
  missing={r for r in B[k]if not(taken>>r&1)};sub=tree[2];assert sub and len(sub)==len(set(sub)) and set(sub)<=missing
  reachable={w for w in need if any(domains[w]&inc[r]for r in sub)};assert len(reachable)<len(sub);return
 assert kind=='branch' and v not in ass;opts=domains[v];valid=[]
 while opts:
  bit=opts&-opts;opts-=bit;k=bit.bit_length()-1
  if not(RM[k]&twice):valid.append(k)
 children=tree[2];assert [k for k,ch in children]==valid
 for k,ch in children:
  bit=1<<k;q=RM[k];ass[v]=k;check(ch,ass,used|bit,once|q,twice|(once&q));del ass[v]
for q in D['proofs']:
 root=q['root'];before=sum(counts.values());check(q['tree'],{0:root},1<<root,RM[root],0);assert sum(counts.values())-before==q['nodes']
assert sum(counts.values())==D['nodes'] and dict(counts)==D['node_types']
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'core_sha256':hashlib.sha256(corebytes).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source_rays':len(V),'source_bases':len(B),'basis_orbits':len(orbits),'proof_nodes':sum(counts.values()),'node_types':dict(counts),
 'all_source_rays_bases_orbits_and_tree_children_replayed':True,'status':'PASS'}
(P/'frontier-20261029-mixed-union6-proof-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
