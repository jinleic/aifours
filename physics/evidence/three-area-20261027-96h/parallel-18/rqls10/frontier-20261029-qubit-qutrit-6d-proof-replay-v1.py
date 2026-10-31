#!/usr/bin/env python3
"""Independent Q(i,omega), BK, symmetry and Hall-certificate replay."""
import collections,datetime,gzip,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;proof=P/'frontier-20261029-qubit-qutrit-6d-complement-proof-v1.json.gz';raw=proof.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='3e50b31d20466bea87e6e2f981f0a5964d36699706132a198e420c519505efe8'
with gzip.open(proof,'rt',encoding='utf8')as f:D=json.load(f)
# Q(i,omega), basis 1,omega,i,i omega, omega²=-1-omega.
Z=(0,0,0,0);O=(1,0,0,0);W=(0,1,0,0);I=(0,0,1,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def m2(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def mul(a,b):
 x=m2(a[:2],b[:2]);y=m2(a[2:],b[2:]);u=m2(a[:2],b[2:]);v=m2(a[2:],b[:2])
 return(x[0]-y[0],x[1]-y[1],u[0]+v[0],u[1]+v[1])
def cj(a):return(a[0]-a[1],-a[1],-a[2]+a[3],a[3])
zeta=neg(mul(I,W));R=[O]
for _ in range(11):R.append(mul(R[-1],zeta))
assert R[3]==I and R[4]==W and mul(R[-1],zeta)==O
cache={}
def inv(a):
 if a in cache:return cache[a]
 A=[[F(mul(a,tuple(int(k==j)for k in range(4)))[i])for j in range(4)]+[F(int(i==0))]for i in range(4)]
 for i in range(4):
  j=next(j for j in range(i,4)if A[j][i]);A[i],A[j]=A[j],A[i];q=A[i][i];A[i]=[x/q for x in A[i]]
  for j in range(4):
   if j!=i:q=A[j][i];A[j]=[x-q*y for x,y in zip(A[j],A[i])]
 cache[a]=tuple(A[i][4]for i in range(4));return cache[a]
def key(v):
 q=inv(next(x for x in v if x!=Z));return tuple(mul(x,q)for x in v)
def tensor(a,b):return tuple(mul(x,y)for x in a for y in b)
def combine(a,b,z):return tuple(add(x,mul(z,y))for x,y in zip(a,b))
# Independently generate the advertised three qubit MUBs and four qutrit MUBs.
QB=[((O,Z),(Z,O)),((O,O),(O,neg(O))),((O,I),(O,neg(I)))]
TB=[[tuple(O if i==j else Z for i in range(3))for j in range(3)]]
for a in range(3):TB.append([tuple(R[4*((a*j*j+b*j)%3)]for j in range(3))for b in range(3)])
source=set()
for q in QB:
 for x in q:
  for b in TB:
   for y in b:source.add(key(tensor(x,y)))
for q in QB:
 for b in TB:
  for i,j in itertools.permutations(range(3),2):
   for k in range(12):source.add(key(combine(tensor(q[0],b[i]),tensor(q[1],b[j]),R[k])))
assert len(source)==936
# Convert producer's 1,zeta,zeta²,zeta³ basis to 1,omega,i,i omega.
def convert(q):a,b,c,d=q;return(a+c,c,d,-b)
V=[tuple(convert(x)for x in v)for v in D['rays']];keys=[key(v)for v in V];assert len(set(keys))==len(V)==936 and set(keys)==source;vi={x:i for i,x in enumerate(keys)}
sc={x for v in V for x in v};products={(a,b):mul(cj(a),b)for a in sc for b in sc};adj=[0]*len(V)
for a,b in itertools.combinations(range(len(V)),2):
 q=[0,0,0,0]
 for x,y in zip(V[a],V[b]):
  t=products[x,y]
  for j in range(4):q[j]+=t[j]
 if not any(q):adj[a]|=1<<b;adj[b]|=1<<a
B=[]
def bk(sel,can,ex,depth):
 if depth+can.bit_count()<6:return
 if depth==6:B.append(tuple(i for i in range(len(V))if sel>>i&1));return
 both=can|ex;pivot=-1;best=-1
 while both:
  bit=both&-both;both-=bit;x=bit.bit_length()-1;k=(can&adj[x]).bit_count()
  if k>best:best=k;pivot=x
 choices=can if pivot<0 else can&~adj[pivot]
 while choices:
  bit=choices&-choices;choices-=bit;x=bit.bit_length()-1;bk(sel|bit,can&adj[x],ex&adj[x],depth+1);can&=~bit;ex|=bit
bk(0,(1<<len(V))-1,0,0);B.sort();assert len(B)==16560 and [list(q)for q in B]==D['bases'];bi={b:i for i,b in enumerate(B)}
# Independent exact actions of local unitary generators and conjugation.
def qh(v):return tuple(add(v[t],v[t+3])for t in range(3))+tuple(add(v[t],neg(v[t+3]))for t in range(3))
def qs(v):return v[:3]+tuple(mul(I,x)for x in v[3:])
def sh(v):return tuple(v[3*a+(t-1)%3]for a in range(2)for t in range(3))
def cl(v):return tuple(mul(R[4*t],v[3*a+t])for a in range(2)for t in range(3))
def ch(v):return tuple(mul(R[4*t*t%12],v[3*a+t])for a in range(2)for t in range(3))
def fo(v):return tuple(tuple(sum(mul(R[4*t*j%12],v[3*a+j])[k]for j in range(3))for k in range(4))for a in range(2)for t in range(3))
def co(v):return tuple(cj(x)for x in v)
gens=[]
for f in(qh,qs,sh,cl,ch,fo,co):
 perm=[vi[key(f(v))]for v in V];assert len(set(perm))==len(V);gens.append(perm)
left=set(range(len(B)));orbits=[]
while left:
 i=min(left);Oset={i};stack=[i]
 while stack:
  j=stack.pop()
  for gen in gens:
   k=bi[tuple(sorted(gen[x]for x in B[j]))]
   if k not in Oset:Oset.add(k);stack.append(k)
 left-=Oset;orbits.append(sorted(Oset))
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
(P/'frontier-20261029-qubit-qutrit-6d-proof-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
