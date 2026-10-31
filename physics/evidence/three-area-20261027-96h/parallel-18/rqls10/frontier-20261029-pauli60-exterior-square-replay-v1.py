#!/usr/bin/env python3
"""Independent common-plane replay using 2x2 Gram determinants, no wedge arrays."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-source-vectors-v1.json';raw=src.read_bytes();d=json.loads(raw);V=[d['vectors'][str(i)]for i in range(1,61)]
def dot(a,b):return(sum(x[0]*y[0]+x[1]*y[1]for x,y in zip(a,b)),sum(x[0]*y[1]-x[1]*y[0]for x,y in zip(a,b)))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm(a):return sum(x*x+y*y for x,y in a)
def area(a,b,c,d):
 x=mul(dot(V[a],V[c]),dot(V[b],V[d]));y=mul(dot(V[a],V[d]),dot(V[b],V[c]));return(x[0]-y[0],x[1]-y[1])
def sameplane(a,b,c,d):
 x,y=area(a,b,c,d);return x*x+y*y==norm(V[a])*norm(V[b])*norm(V[c])*norm(V[d])
ad=[set()for _ in range(60)]
for i,j in itertools.combinations(range(60),2):
 if dot(V[i],V[j])==(0,0):ad[i].add(j);ad[j].add(i)
B=[]
for a in range(60):
 for b in sorted(x for x in ad[a]if x>a):
  for c in sorted(x for x in ad[a]&ad[b]if x>b):
   for d0 in sorted(x for x in ad[a]&ad[b]&ad[c]if x>c):B.append((a,b,c,d0))
assert len(B)==105
pairs=[];deg=[0]*105;hist=collections.Counter()
for i,j in itertools.combinations(range(105),2):
 n=sum(sameplane(a,b,c,d)for a,b in itertools.combinations(B[i],2)for c,d in itertools.combinations(B[j],2));r=len(set(B[i])&set(B[j]));hist[(r,n)]+=1
 if r==0 and n:
  deg[i]+=1;deg[j]+=1;pairs.append([i,j,n])
base=P/'frontier-20261029-pauli60-exterior-square-census-v1.json';basebytes=base.read_bytes();D=json.loads(basebytes)
assert [list(q)for q in B]==D['bases'] and pairs==D['disjoint_shared_plane_pairs'] and deg==D['compatible_degrees']
high=[i for i,x in enumerate(deg)if x>=6];assert len(high)==15 and len({r for i in high for r in B[i]})==60
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_vectors_sha256':hashlib.sha256(raw).hexdigest(),
 'producer_sha256':hashlib.sha256(basebytes).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'bases':len(B),'disjoint_compatible_pairs':len(pairs),'degree_histogram':dict(collections.Counter(deg)),
 'all_literal_pairs_and_degrees_match':True,'high_degree_bases_mutually_disjoint':True,'status':'PASS'}
(P/'frontier-20261029-pauli60-exterior-square-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
