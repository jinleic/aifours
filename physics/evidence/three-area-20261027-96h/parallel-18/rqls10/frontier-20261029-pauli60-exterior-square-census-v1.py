#!/usr/bin/env python3
"""Exact shared Lambda² basis-ray census for all 105 Pauli60 bases."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-source-vectors-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8edccd50a66289a669b30fa5ec40b6b215147af3e9731545cc4ffe3bf8b33294';d=json.loads(raw);V=[tuple(tuple(x)for x in d['vectors'][str(i)])for i in range(1,61)]
def dot(a,b):return(sum(x*u+y*v for (x,y),(u,v)in zip(a,b)),sum(x*v-y*u for (x,y),(u,v)in zip(a,b)))
def gm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def wedge(a,b):return tuple(sub(gm(a[i],b[j]),gm(a[j],b[i]))for i,j in itertools.combinations(range(4),2))
def key(v):
 a,b=next(x for x in v if x!=(0,0));d=a*a+b*b
 return tuple((F(x*a+y*b,d),F(y*a-x*b,d))for x,y in v)
B=[q for q in itertools.combinations(range(60),4)if all(dot(V[i],V[j])==(0,0)for i,j in itertools.combinations(q,2))];assert len(B)==105
planes=[{key(wedge(V[i],V[j]))for i,j in itertools.combinations(q,2)}for q in B];assert all(len(x)==6 for x in planes)
deg=[0]*105;patterns=collections.Counter();pairs=[]
for i,j in itertools.combinations(range(105),2):
 shared=len(set(B[i])&set(B[j]));w=len(planes[i]&planes[j]);patterns[(shared,w)]+=1
 if shared==0 and w:
  deg[i]+=1;deg[j]+=1;pairs.append([i,j,w])
hist=collections.Counter(deg);assert hist=={4:90,12:15};high=[i for i,x in enumerate(deg)if x>=6]
assert len({x for i in high for x in B[i]})==60 and all(not(set(B[i])&set(B[j]))for i,j in itertools.combinations(high,2))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'bases':B,'disjoint_shared_plane_pairs':pairs,'compatible_degrees':deg,
 'pair_overlap_histogram':{str(k):v for k,v in patterns.items()},'degree_histogram':dict(hist),'high_degree_basis_indices':high,
 'high_degree_bases_disjoint':True,'scope':'One fixed exterior-square bivector frame per context; arbitrary 6D bases not constrained.'}
(P/'frontier-20261029-pauli60-exterior-square-census-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('bases','disjoint_shared_plane_pairs','compatible_degrees','high_degree_basis_indices')},indent=2))
