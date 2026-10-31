#!/usr/bin/env python3
"""Bounded exact 6D complement search in a qubit-qutrit contextual alphabet.
Source: product MUB rays and equal-amplitude pair-entangled rays with relative
12th phases, all generated exactly in Z[zeta12]. SAT is only a partial core.
"""
import collections,datetime,hashlib,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;source=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';D0=json.loads(raw);G=[set()for _ in range(15)]
for z in D0['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
assert all(len(g)==6 for g in G)
Z=(0,0,0,0);ONE=(1,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 q=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):q[i+j]+=x*y
 for k in range(6,3,-1):q[k-4]-=q[k];q[k-2]+=q[k]
 return tuple(q[:4])
R=[ONE]
for _ in range(11):a,b,c,d=R[-1];R.append((-d,a,b+d,c))
def cj(a):
 q=Z
 for i,x in enumerate(a):q=add(q,tuple(x*y for y in R[-i%12]))
 return q
cache={}
def inv(a):
 if a in cache:return cache[a]
 M=[[F(mul(a,tuple(int(j==i)for j in range(4)))[k])for i in range(4)]+[F(int(k==0))]for k in range(4)]
 for j in range(4):
  k=next(i for i in range(j,4)if M[i][j]);M[j],M[k]=M[k],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for k in range(4):
   if k!=j:
    q=M[k][j];M[k]=[x-q*y for x,y in zip(M[k],M[j])]
 cache[a]=tuple(M[k][4]for k in range(4));return cache[a]
def key(v):
 a=inv(next(x for x in v if x!=Z));return tuple(mul(x,a)for x in v)
def tensor(a,b):return tuple(mul(x,y)for x in a for y in b)
def vadd(a,b):return tuple(add(x,y)for x,y in zip(a,b))
def scale(a,z):return tuple(mul(x,z)for x in a)
i=R[3];Q=[((ONE,Z),(Z,ONE)),((ONE,ONE),(ONE,neg(ONE))),((ONE,i),(ONE,neg(i)))]
T=[[tuple(ONE if j==k else Z for j in range(3))for k in range(3)]]
for a in range(3):T.append([tuple(R[4*((a*k*k+b*k)%3)]for k in range(3))for b in range(3)])
D={}
for qb in Q:
 for u in qb:
  for tb in T:
   for v in tb:
    x=tensor(u,v);D.setdefault(key(x),x)
for qb in Q:
 for tb in T:
  for a,b in itertools.permutations(range(3),2):
   for k in range(12):
    x=vadd(tensor(qb[0],tb[a]),scale(tensor(qb[1],tb[b]),R[k]));D.setdefault(key(x),x)
K=list(D);V=list(D.values());vi={k:i for i,k in enumerate(K)};assert len(V)==936
scalar={x for v in V for x in v};prod={(x,y):mul(cj(x),y)for x in scalar for y in scalar};adj=[0]*len(V)
for a,b in itertools.combinations(range(len(V)),2):
 q=[0,0,0,0]
 for x,y in zip(V[a],V[b]):
  v=prod[x,y]
  for k in range(4):q[k]+=v[k]
 if not any(q):adj[a]|=1<<b;adj[b]|=1<<a
B=[]
def dfs(path,can):
 if len(path)==6:B.append(tuple(path));return
 if len(path)+can.bit_count()<6:return
 while can:
  bit=can&-can;can-=bit;j=bit.bit_length()-1;dfs(path+[j],can&adj[j])
dfs([], (1<<len(V))-1);B.sort();assert len(B)==16560;bi={b:i for i,b in enumerate(B)}
def qh(v):return tuple(add(v[t],v[t+3])for t in range(3))+tuple(add(v[t],neg(v[t+3]))for t in range(3))
def qs(v):return v[:3]+tuple(mul(i,x)for x in v[3:])
def shift(v):return tuple(v[3*a+(t-1)%3]for a in range(2)for t in range(3))
def clock(v):return tuple(mul(R[4*t],v[3*a+t])for a in range(2)for t in range(3))
def chirp(v):return tuple(mul(R[4*t*t%12],v[3*a+t])for a in range(2)for t in range(3))
def fourier(v):
 return tuple(tuple(sum(mul(R[4*t*j%12],v[3*a+j])[k]for j in range(3))for k in range(4))for a in range(2)for t in range(3))
def conjugate(v):return tuple(cj(x)for x in v)
gens=[]
for f in (qh,qs,shift,clock,chirp,fourier,conjugate):
 perm=[vi[key(f(v))]for v in V];assert len(set(perm))==len(V);gens.append(perm)
left=set(range(len(B)));orbits=[]
while left:
 s=min(left);O={s};todo=[s]
 while todo:
  j=todo.pop()
  for gen in gens:
   k=bi[tuple(sorted(gen[x]for x in B[j]))]
   if k not in O:O.add(k);todo.append(k)
 left-=O;orbits.append(sorted(O))
assert len(orbits)==30
inc=[0]*len(V)
for j,b in enumerate(B):
 bit=1<<j
 for x in b:inc[x]|=bit
full=(1<<len(B))-1;A0=[];A1=[]
for b in B:
 seen=multi=0
 for x in b:multi|=seen&inc[x];seen|=inc[x]
 A1.append(seen&~multi);A0.append(full&~seen)
Rays=[sum(1<<x for x in b)for b in B];domain=sum(1<<j for j in range(len(B))if A1[j].bit_count()>=6)
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
  for w,k in assign.items():q&=A1[k] if w in G[v] else A0[k]
  if not q:types['empty']+=1;return ['empty',v]
  domains[v]=q
 for v,k in assign.items():
  need=sorted(w for w in G[v]if w not in assign)
  if not need:continue
  taken=0
  for w in G[v]:
   if w in assign:taken|=Rays[k]&Rays[assign[w]]
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
  bit=opts&-opts;opts-=bit;k=bit.bit_length()-1;r=Rays[k]
  if r&twice:continue
  assign[v]=k;children.append([k,prove(assign,used|bit,once|r,twice|(once&r))]);del assign[v]
 types['branch']+=1;return ['branch',v,children]
proofs=[];start=time.monotonic()
for orbit in orbits:
 root=orbit[0]
 if not(domain>>root&1):continue
 before=nodes;tree=prove({0:root},1<<root,Rays[root],0);proofs.append({'root':root,'nodes':nodes-before,'tree':tree})
 print('root',root,'nodes',nodes-before,flush=True)
record={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rays':V,'bases':B,'orbits':orbits,'proofs':proofs,
 'nodes':nodes,'node_types':dict(types),'scope':'936 product/entangled MUB source; one 6D target; Hall-pruned exhaustive branch forest.'}
out=P/'frontier-20261029-qubit-qutrit-6d-complement-proof-v1.json.gz'
with gzip.open(out,'wt',encoding='utf8')as f:json.dump(record,f,separators=(',',':'))
summary={'source_sha256':record['source_sha256'],'core_sha256':record['core_sha256'],'clock_finish':record['clock_finish'],
 'ray_count':len(V),'basis_count':len(B),'basis_orbits':len(orbits),'nodes':nodes,'node_types':dict(types),
 'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,4),'status':'EXHAUSTED'}
(P/'frontier-20261029-qubit-qutrit-6d-complement-proof-v1.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
