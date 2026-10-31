#!/usr/bin/env python3
"""Exact Z[zeta28] verification of an orthonormal representation of L(K7,7,7) in C^14 (flat-diagonal Z7^2 type).

v_q(x)_j = zeta28^(4<c_j,x> + PHI2[q][j]) / sqrt(14), x in Z7^2; q=0 (A_s--B_t), q=1 (A_s--C_(s+t)), q=2 (B_t--C_(s+t)).
Checks all 21 contexts exactly orthonormal (all pairs) and 147 rays pairwise non-parallel.  Scope: this object only.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
m=7;N=28
T=[(0,0),(0,1),(1,0),(1,1),(2,3),(2,5),(3,5),(3,6),(4,2),(4,6),(5,2),(5,4),(6,3),(6,4)]
PHI2=[[-63,-49,-14,0,-84,-70,-56,-42,-42,-28,-28,-14,-14,0],
      [-49,-70,-14,-35,-56,-14,-14,0,-14,0,-14,0,0,0],
      [0]*14]
def vec(q,x):return tuple((4*((c[0]*x[0]+c[1]*x[1])%m)+PHI2[q][j])%N for j,c in enumerate(T))
def reduce28(c):
    # Phi28 = x^12 - x^10 + x^8 - x^6 + x^4 - x^2 + 1 ; x^12 = x^10 - x^8 + x^6 - x^4 + x^2 - 1
    p=c[:]
    for d in range(27,11,-1):
        q=p[d]
        if q:p[d]=0;p[d-2]+=q;p[d-4]-=q;p[d-6]+=q;p[d-8]-=q;p[d-10]+=q;p[d-12]-=q
    return p[:12]
def orth(a,b):
    c=[0]*N
    for x,y in zip(a,b):c[(y-x)%N]+=1
    return all(v==0 for v in reduce28(c))
def parallel(a,b):return len({(y-x)%N for x,y in zip(a,b)})==1
cells=[]
for q in range(3):
    for x in itertools.product(range(m),repeat=2):
        s,t=x;u=(s+t)%m
        ends=[('A',s),('B',t)] if q==0 else ([('A',s),('C',u)] if q==1 else [('B',t),('C',u)])
        cells.append((q,x,tuple(ends),vec(q,x)))
inc={}
for q,x,ends,v in cells:
    for e in ends:inc.setdefault(e,[]).append(v)
assert len(cells)==147 and len(inc)==21 and all(len(v)==14 for v in inc.values())
pairs=0
for e,vs in inc.items():
    for a,b in itertools.combinations(vs,2):
        assert orth(a,b),e;pairs+=1
nonpar=all(not parallel(a[3],b[3]) for a,b in itertools.combinations(cells,2))
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'object':'orthonormal representation of L(K7,7,7) in C^14','field':'Q(zeta28)','context_pairs_exactly_orthogonal':pairs,
 'rays_pairwise_nonparallel':nonpar,'status':'PASS' if nonpar else 'FAIL'}
(P/'frontier-20261029-k777-exact-construction-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
