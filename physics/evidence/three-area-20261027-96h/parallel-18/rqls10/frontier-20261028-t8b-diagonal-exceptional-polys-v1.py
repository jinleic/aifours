#!/usr/bin/env python3
"""Exact adjacency-polynomial census for T8B(z,z,z), arbitrary row orders.

P(z)=z^3*N(z)*D(z)*sum_t zeta8^t conj(K[O_t,c])*K[O_t,d],
N=1+3z², D=3z+z³, after |z|=|d|=1. Coefficients are in Z[zeta8].
Identity adjacency graph cannot contain a Hamiltonian cycle by field theorem;
this program independently checks all normalized source orders and bounds.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
rows=[['1','1','1','1','1','1','1','1'],['1','-1','-d','-c','d','c','cd','-cd'],['1','-a','-1','c','a','-ac','-c','ac'],['1','a','d','-1','ad','-a','-d','-ad'],['1','b','-b','-bc','-1','-c','c','bc'],['1','-b','bd','b','-d','-1','d','-bd'],['1','-ab','b','-b','-a','a','-1','ab'],['1','ab','-bd','bc','-ad','ac','-cd','-abcd']]
def token(s):
 sign=-1 if s.startswith('-')else 1;s=s.lstrip('-');return sign,sum(s.count(x)for x in 'abc'),s.count('d')
K=[[token(s)for s in row]for row in rows]
# N²,ND,D²; a monomial z^3 clears the largest negative exponent.
F={1:{0:1,2:6,4:9},0:{1:3,3:10,5:3},-1:{2:9,4:6,6:1}}
def root(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return v
# Precompute exact coefficient contributions [physical coordinate][source row][c][d].
T={}
for t in range(8):
 for s in range(8):
  for c,d in itertools.permutations(range(8),2):
   sc,kc,dc=K[s][c];sd,kd,dd=K[s][d];shift=kd-kc+3;assert 0<=shift<=6
   v=root(t);P0=[[0]*4 for _ in range(13)]
   for e,q in F[dd-dc].items():
    for j in range(4):P0[e+shift][j]+=sc*sd*q*v[j]
   T[t,s,c,d]=P0
identities=nonzero=totaldeg=0;maxdeg=0;maxedges=0;bad=[]
for perm in itertools.permutations(range(1,8)):
 O=(0,)+perm;adj=[0]*8
 for c,d in itertools.permutations(range(8),2):
  A=[[0]*4 for _ in range(13)]
  for t in range(8):
   B=T[t,O[t],c,d]
   for e in range(13):
    for j in range(4):A[e][j]+=B[e][j]
  non=[e for e in range(13)if any(A[e])]
  if not non:identities+=1;adj[c]|=1<<d
  else:nonzero+=1;degree=max(non);maxdeg=max(maxdeg,degree);totaldeg+=degree
 maxedges=max(maxedges,sum(x.bit_count()for x in adj))
 def cycle(v,mask):
  if mask==255:return bool(adj[v]&1)
  opts=adj[v]&~mask
  while opts:
   q=(opts&-opts).bit_length()-1;opts&=opts-1
   if cycle(q,mask|(1<<q)):return True
  return False
 if cycle(0,1):bad.append(O)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source':'https://arxiv.org/html/2505.22947v1 Proposition3.2 T8B',
 'normalized_source_orders':5040,'directed_adjacencies_per_order':56,
 'identically_zero_polynomials':identities,'nonzero_polynomials':nonzero,
 'maximum_degree':maxdeg,'sum_degrees_with_multiplicity':totaldeg,
 'max_identity_graph_edges':maxedges,'identity_hamiltonian_cycles_found':len(bad),'first_bad_order':bad[:1]}
(P/'frontier-20261028-t8b-diagonal-exceptional-polys-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
