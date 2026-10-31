#!/usr/bin/env python3
"""Exact exceptional-variety caller for T8B Fourier transversals.

For every normalized coordinate half and every column matching, substitute
source d=N/D into the exact Laurent half-Gram sums. On the unit domain
D!=0 implies N!=0. Identically zero edges impose nothing; every other
polynomial must vanish. Inclusion-minimize the 35*105 matching branches.
"""
import collections,datetime,hashlib,itertools,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
rows=[['1','1','1','1','1','1','1','1'],['1','-1','-d','-c','d','c','cd','-cd'],['1','-a','-1','c','a','-ac','-c','ac'],['1','a','d','-1','ad','-a','-d','-ad'],['1','b','-b','-bc','-1','-c','c','bc'],['1','-b','bd','b','-d','-1','d','-bd'],['1','-ab','b','-b','-a','a','-1','ab'],['1','ab','-bd','bc','-ad','ac','-cd','-abcd']]
def token(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('-');return sign,tuple(s.count(v)for v in 'abcd')
K=[[token(s)for s in row]for row in rows]
def poly(terms):return {e:c for e,c in terms.items() if c}
def prod(a,b):
 z=collections.Counter()
 for x,u in a.items():
  for y,v in b.items():z[tuple(i+j for i,j in zip(x,y))]+=u*v
 return poly(z)
N={(0,0,0):1,(1,1,0):1,(1,0,1):1,(0,1,1):1};D={(1,0,0):1,(0,1,0):1,(0,0,1):1,(1,1,1):1}
F={-1:prod(D,D),0:prod(N,D),1:prod(N,N)}
def normalize(z):
 z=poly(z)
 if not z:return None
 low=tuple(min(e[i]for e in z)for i in range(3));out={tuple(e[i]-low[i]for i in range(3)):v for e,v in z.items()}
 g=math.gcd(*map(abs,out.values()));out={e:v//g for e,v in out.items()}
 if out[min(out)]<0:out={e:-v for e,v in out.items()}
 return tuple(sorted(out.items()))
def edge(E,c,d):
 z=collections.Counter()
 for t in E:
  s,x=K[t][c];u,y=K[t][d];diff=tuple(y[i]-x[i] for i in range(4));assert diff[3] in (-1,0,1)
  for mon,coef in F[diff[3]].items():z[tuple(mon[i]+diff[i]+1 for i in range(3))]+=s*u*coef
 return normalize(z)
def matchings(vertices):
 if not vertices:yield ();return
 c=vertices[0]
 for i in range(1,len(vertices)):
  d=vertices[i]
  for M in matchings(vertices[1:i]+vertices[i+1:]):yield ((c,d),)+M
allM=list(matchings(tuple(range(8))));assert len(allM)==105
polys=[];index={};branches=set();empty=[];halfdata=[]
for E0 in itertools.combinations(range(1,8),3):
 E=(0,)+E0;lookup={}
 for c,d in itertools.combinations(range(8),2):
  f=edge(E,c,d)
  if f is None:lookup[c,d]=-1
  else:
   if f not in index:index[f]=len(polys);polys.append(f)
   lookup[c,d]=index[f]
 local=[]
 for M in allM:
  req=frozenset(lookup[e] for e in M if lookup[e]>=0);local.append(req);branches.add(req)
  if not req:empty.append((E,M))
 halfdata.append({'half':E,'identity_edges':[list(e)for e,x in lookup.items()if x<0],
                  'min_nonidentity_edges':min(map(len,local))})
# Global inclusion-minimal conjunctions imply the same union of varieties.
minimal=[]
for s in sorted(branches,key=lambda x:(len(x),tuple(sorted(x)))):
 if not any(q<=s for q in minimal):minimal.append(s)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source':'https://arxiv.org/html/2505.22947v1 Proposition3.2 T8B',
 'normalized_halves':len(halfdata),'matchings_per_half':len(allM),'distinct_nonzero_polynomials':len(polys),
 'distinct_requirement_sets':len(branches),'minimal_requirement_sets':len(minimal),
 'requirement_size_histogram':dict(collections.Counter(len(s)for s in minimal)),
 'identically_matched_halves':len(empty),'polynomials':polys,
 'minimal_requirements':[sorted(s)for s in minimal],'halfdata':halfdata}
(P/'frontier-20261028-t8b-halfgraph-variety-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({k:v for k,v in obj.items()if k not in ('polynomials','minimal_requirements','halfdata')},indent=2))
