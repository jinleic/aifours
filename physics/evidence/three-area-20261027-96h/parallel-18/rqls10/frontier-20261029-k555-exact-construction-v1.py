#!/usr/bin/env python3
"""Exact Z[zeta20] verification of an orthonormal representation of L(K5,5,5) in C^10.

Vectors are flat: v_q(x)_j = zeta20^(4<c_j,x> + 2*Phi[q][j]) / sqrt(10), x in Z5^2, j=0..9.
Quadrant q=0 ('AB'), q=1 ('AC'), q=2 ('BC').  Edge/cell incidence:
  q=0, x=(s,t): A_s -- B_t ;  q=1, x=(s,t): A_s -- C_(s+t) ;  q=2, x=(s,t): B_t -- C_(s+t).
Each of the 15 vertices gets 10 vectors; every pair inside a vertex is checked exactly orthogonal.
Also checks 75 pairwise non-parallel rays exactly.  This is a finite exact certificate for this one object only.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
T=[(0,0),(0,1),(1,0),(1,3),(2,2),(2,4),(3,1),(3,4),(4,2),(4,3)]
# phases in units of pi/10 (=2*Phi with Phi in units pi/5), from the exact integer/rational phase solve
PHI2=[[-35,-25,-25,-15,-20,-10,-15,-5,-10,0],
      [-10,-10,-10,-5,0,5,-10,0,0,0],
      [0]*10]
N=20
def vec(q,x):
    return tuple((4*((c[0]*x[0]+c[1]*x[1])%5)+PHI2[q][j])%N for j,c in enumerate(T))
# exact arithmetic in Z[zeta20]: reduce sum of zeta^e mod Phi20(x)=x^8-x^6+x^4-x^2+1
def reduce20(coef):
    p=coef[:]  # length 20, x^20=1 already applied
    for d in range(19,7,-1):
        q=p[d]
        if q:
            p[d]=0;p[d-2]+=q;p[d-4]-=q;p[d-6]+=q;p[d-8]-=q
    return p[:8]
def inner_is_zero(a,b):
    c=[0]*N
    for x,y in zip(a,b):c[(y-x)%N]+=1
    return all(v==0 for v in reduce20(c))
def parallel(a,b):
    # a,b flat; parallel iff b_j - a_j constant mod N
    d={(y-x)%N for x,y in zip(a,b)};return len(d)==1
cells=[]
for q in range(3):
    for x in itertools.product(range(5),repeat=2):
        s,t=x;u=(s+t)%5
        ends=[('A',s),('B',t)] if q==0 else ([('A',s),('C',u)] if q==1 else [('B',t),('C',u)])
        cells.append((q,x,tuple(ends),vec(q,x)))
inc={}
for q,x,ends,v in cells:
    for e in ends:inc.setdefault(e,[]).append(v)
assert len(cells)==75 and len(inc)==15 and all(len(v)==10 for v in inc.values())
pairs=0
for e,vs in inc.items():
    for a,b in itertools.combinations(vs,2):
        assert inner_is_zero(a,b),e;pairs+=1
nonpar=all(not parallel(a[3],b[3]) for a,b in itertools.combinations(cells,2))
assert nonpar
extra=sum(1 for a,b in itertools.combinations(cells,2) if inner_is_zero(a[3],b[3]))
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'object':'orthonormal representation of the line graph of K5,5,5 in C^10 (15 ONB contexts, 75 rays)',
 'field':'Q(zeta20); flat vectors 1/sqrt10 * zeta20^e',
 'context_pairs_checked_exactly_orthogonal':pairs,
 'all_75_rays_pairwise_nonparallel':nonpar,
 'total_exactly_orthogonal_pairs':extra,'status':'PASS'}
(P/'frontier-20261029-k555-exact-construction-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
