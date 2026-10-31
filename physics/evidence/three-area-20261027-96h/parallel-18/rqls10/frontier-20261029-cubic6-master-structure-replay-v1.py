#!/usr/bin/env python3
"""Independent support/phase generator and Z[omega] Bron–Kerbosch replay."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
# Generate phase patterns separately for each support, rather than projectively
# deduplicating 3^6 source vectors.
V=set()
for k in range(1,7):
 for supp in itertools.combinations(range(6),k):
  for phase in (1,2):
   for bits in itertools.product((0,1),repeat=k-1):
    v=[-1]*6;v[supp[0]]=0
    for j,b in zip(supp[1:],bits):v[j]=phase*b
    V.add(tuple(v))
V=sorted(V);assert len(V)==665
R=[(1,0),(0,1),(-1,-1)]
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x):return(x[0]-x[1],-x[1])
def orth(a,b):
 q=(0,0)
 for x,y in zip(a,b):
  if x>=0 and y>=0:q=add(q,mul(conj(R[x]),R[y]))
 return q==(0,0)
ad=[0]*len(V)
for i,j in itertools.combinations(range(len(V)),2):
 if orth(V[i],V[j]):ad[i]|=1<<j;ad[j]|=1<<i
B=[];nodes=0
def bk(sel,can,ex,depth):
 global nodes
 nodes+=1
 if depth+can.bit_count()<6:return
 if depth==6:B.append(tuple(i for i in range(len(V))if sel>>i&1));return
 U=can|ex;best=-1;pivot=-1
 while U:
  bit=U&-U;U-=bit;i=bit.bit_length()-1;q=(can&ad[i]).bit_count()
  if q>best:best=q;pivot=i
 todo=can if pivot<0 else can&~ad[pivot]
 while todo:
  bit=todo&-todo;todo-=bit;i=bit.bit_length()-1;bk(sel|bit,can&ad[i],ex&ad[i],depth+1);can&=~bit;ex|=bit
bk(0,(1<<len(V))-1,0,0);B.sort();assert len(B)==153
source=P/'frontier-20261029-cubic6-master-structure-v1.json';raw=source.read_bytes();D=json.loads(raw)
assert [list(x)for x in V]==D['rays'] and [list(x)for x in B]==D['bases']
sing={i for i,x in enumerate(V)if sum(q>=0 for q in x)==1};prof=collections.Counter(sum(i in sing for i in q)for q in B);assert prof=={0:40,1:72,3:40,6:1}
Z=[j for j,q in enumerate(B)if not(set(q)&sing)];degrees=[sum(len(set(q)&set(w))==1 for w in B)for q in B]
assert degrees==D['single_intersection_degrees'] and all(degrees[j]==0 for j in Z)
A=next(j for j,q in enumerate(B)if len(set(q)&sing)==6);assert all(j in Z for j,q in enumerate(B)if j!=A and not(set(q)&set(B[A])))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rays':len(V),'bases':len(B),'BK_nodes':nodes,
 'literal_rays_bases_degrees_match':True,'singleton_histogram':dict(prof),'zero_singleton_degree0':True,'status':'PASS'}
(P/'frontier-20261029-cubic6-master-structure-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
