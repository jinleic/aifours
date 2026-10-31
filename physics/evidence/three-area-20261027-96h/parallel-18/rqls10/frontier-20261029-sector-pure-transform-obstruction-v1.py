#!/usr/bin/env python3
"""Exact cyclotomic obstruction for a natural sector-mixing transversal."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
# Z[zeta5], primitive 5th root, in polynomial basis 1,z,z²,z³.
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def mul(x,y):
 v=[0]*7
 for i,a in enumerate(x):
  for j,b in enumerate(y):v[i+j]+=a*b
 for k in range(6,3,-1):
  a=v[k]
  for j in range(1,5):v[k-j]-=a
 return tuple(v[:4])
def rt(k):
 k%=5
 return (-1,-1,-1,-1)if k==4 else tuple(int(i==k)for i in range(4))
def sm(v):
 x=(0,0,0,0)
 for y in v:x=add(x,y)
 return x
sig=(0,1,3,2,4)
# H=DFT*zeta-permuted columns, all scalings 1/5 omitted.
num=[[sm(rt(t*(k-r)+c*sig[t])for t in range(5))for c in range(5)]for r in range(5)for k in range(5)]
# Demonstrate an EXACT nonzero off-diagonal M_0^* M_0 element for sector lift.
# M_r=F^* diag(zeta^(r t)) H. Need M_0^*M_s=0 for r!=s,
# which is impossible already because these are unitary; row-vector Gram across
# sector-coupled states simplifies to M_r^* M_s.
# More directly, eliminate output t by Fourier orthogonality: for two states
# (r,c) and (s,d), cross-sector Gram numerator = 5 sum_t zeta^((s-r)t+(d-c)sigma[t]).
examples=[]
for (r,c),(s,d) in itertools.combinations(list(itertools.product(range(5),repeat=2)),2):
 q=sm(rt((s-r)*t+(d-c)*sig[t])for t in range(5))
 if q!=(0,0,0,0):examples.append([r,c,s,d,q])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'distinct_cross_sector_pair_obstructions':len(examples),'first_obstruction':examples[0],
 'scope':'Fixed naive diagonal Bell-like row/column mixing, all 25 candidate states; not arbitrary vector/measurement coupling.'}
(P/'frontier-20261029-sector-pure-transform-obstruction-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
