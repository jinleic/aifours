#!/usr/bin/env python3
"""Classify 3-partite 30-15 Pauli cores under an exact unitary subgroup.
SAT/UNSAT is solver-scoped; if incomplete no all-core statement follows.
"""
import collections,datetime,hashlib,itertools,json,time
from fractions import Fraction
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-search-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='40baaa1a7d25e32c12aa9117707422bb3159a697da1d076dcba9f36ec7cd3561'
g={'__file__':str(src)};exec(compile(raw.decode().split('t0=time.monotonic();res=S.check()',1)[0],str(src),'exec'),g)
S=g['S'];S.set(timeout=30000,random_seed=52);X=g['X'];B=g['B'];V=[tuple(tuple(y)for y in x)for x in g['V']]
def key(v):
 a,b=next(x for x in v if x!=(0,0));d=a*a+b*b
 return tuple((Fraction(c*a+e*b,d),Fraction(e*a-c*b,d))for c,e in v)
lookup={key(v):i for i,v in enumerate(V)};assert len(lookup)==60

def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def ii(a):return(-a[1],a[0])
def H(v):return(plus(v[0],v[2]),plus(v[1],v[3]),minus(v[0],v[2]),minus(v[1],v[3]))
def Sg(v):return(v[0],v[1],ii(v[2]),ii(v[3]))
def swap(v):return(v[0],v[2],v[1],v[3])
def cx(v):return(v[0],v[1],v[3],v[2])
index={b:i for i,b in enumerate(B)};generators=[]
for fun in (H,Sg,swap,cx):
 r=[lookup[key(fun(v))]for v in V];assert len(set(r))==60
 q=[index[tuple(sorted(r[i]for i in b))]for b in B];assert len(set(q))==105;generators.append(q)
ref0=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';ref=json.loads(ref0.read_bytes());R=[[set()for _ in range(15)]][0]
for z in ref['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,q in enumerate(row):
   if q:u=5*a+i;v=5*b+j;R[u].add(v);R[v].add(u)

def partitions(Q):
 G=[set()for _ in range(15)]
 for i,j in itertools.combinations(range(15),2):
  if set(B[Q[i]])&set(B[Q[j]]):G[i].add(j);G[j].add(i)
 color=[-1]*15;color[0]=0;cnt=[1,0,0];ans=set()
 def rec(todo):
  if not todo:
   ans.add(tuple(sorted(tuple(i for i,v in enumerate(color)if v==c)for c in range(3))));return
  v=min(todo,key=lambda x:sum(cnt[c]<5 and all(color[y]!=c for y in G[x])for c in range(3)))
  for c in range(3):
   if cnt[c]<5 and all(color[y]!=c for y in G[v]):color[v]=c;cnt[c]+=1;rec(todo-{v});cnt[c]-=1;color[v]=-1
 rec(set(range(1,15)));return G,sorted(ans)

def isomorphic(G,parts):
 for perm in itertools.permutations(range(3)):
  f={};used=set()
  def rec():
   if len(f)==15:return f.copy()
   dom={v:[w for w in parts[perm[v//5]] if w not in used and all((u in R[v])==(f[u] in G[w])for u in f)]for v in range(15)if v not in f}
   v=min(dom,key=lambda k:len(dom[k]))
   for w in dom[v]:
    f[v]=w;used.add(w);q=rec()
    if q:return q
    used.remove(w);del f[v]
   return None
  q=rec()
  if q:return q
 return None

def orbit(seed):
 seen={seed};todo=[seed]
 while todo:
  q=todo.pop()
  for h in generators:
   a=tuple(sorted(h[i]for i in q))
   if a not in seen:seen.add(a);todo.append(a)
 return seen
start=time.monotonic();records=[];total=0;status='wall_limit'
while time.monotonic()-start<100:
 status0=S.check()
 if status0!=z3.sat:status=str(status0)+((':'+S.reason_unknown())if status0==z3.unknown else '');break
 m=S.model();Q=tuple(i for i,x in enumerate(X)if z3.is_true(m.eval(x)));G,parts=partitions(Q);assert parts
 maps=[isomorphic(G,x)for x in parts];O=orbit(Q);total+=len(O)
 records.append({'representative':Q,'orbit_size':len(O),'balanced_partitions':parts,'all_same_colored_graph':all(x is not None for x in maps),
  'graph_isomorphisms':maps})
 print('orbit',len(records),'size',len(O),'partitions',len(parts),'same',all(x is not None for x in maps),flush=True)
 if any(x is None for x in maps):status='DIFFERENT_COLORED_GRAPH';break
 for o in O:S.add(z3.Or(*[z3.Not(X[i])for i in o]))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_setup_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'solver':'Z3 '+z3.get_version_string(),'status':status,
 'orbits_tested':len(records),'core_sets_blocked':total,'records':records,
 'scope':'Complete only on solver UNSAT; unitary generators H1,S1,SWAP,CNOT, no reliance on full Clifford group.'}
(P/'frontier-20261029-pauli60-tripartite-orbit-scan-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='records'},indent=2))
