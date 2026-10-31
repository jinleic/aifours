#!/usr/bin/env python3
"""Exact Z[zeta20] certificate: a maximal-cardinality QLS(10) built on the K5,5,5 parity core.

Four 5x5 quadrants Q00,Q01,Q10,Q11, each indexed by x=(x1,x2) in Z5^2, flat vectors
v_q(x)_j = zeta20^(4<c_j,x> + PHI2[q][j]) / sqrt(10).
Grid: Q00 x -> (row x1, col x2); Q01 x -> (row x1, col 5+x2); Q10 x -> (row 5+x1, col x2);
Q11 y -> (row 5+y1, col 5+y2) (offsets dR=dC=0).  Label class T1(u) = Q01 cells and Q10 cells with x1+x2=u.
Checks exactly: all 10 rows and 10 columns are ONBs, the 5 classes T1(u) are ONBs, the 100 rays are pairwise
non-parallel; then computes the exact orthogonality graph and enumerates ALL orthogonal transversals
(one cell per row and column, pairwise orthogonal).  Scope: this one explicit array only.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
T=[(0,0),(0,1),(1,0),(1,3),(2,2),(2,4),(3,1),(3,4),(4,2),(4,3)]
PHI2=[[-65,-40,-40,-25,-25,-15,-20,-10,-10,0],
      [-40,-30,-25,-15,-15,-5,-20,-10,-10,0],
      [-25,-10,-15,-10,-10,-10,0,0,0,0],
      [0]*10]
N=20
def vec(q,x):return tuple((4*((c[0]*x[0]+c[1]*x[1])%5)+PHI2[q][j])%N for j,c in enumerate(T))
def reduce20(c):
    p=c[:]
    for d in range(19,7,-1):
        q=p[d]
        if q:p[d]=0;p[d-2]+=q;p[d-4]-=q;p[d-6]+=q;p[d-8]-=q
    return p[:8]
def orth(a,b):
    c=[0]*N
    for x,y in zip(a,b):c[(y-x)%N]+=1
    return all(v==0 for v in reduce20(c))
def parallel(a,b):return len({(y-x)%N for x,y in zip(a,b)})==1
grid={}
for x in itertools.product(range(5),repeat=2):
    grid[(x[0],x[1])]=vec(0,x);grid[(x[0],5+x[1])]=vec(1,x);grid[(5+x[0],x[1])]=vec(2,x);grid[(5+x[0],5+x[1])]=vec(3,x)
assert len(grid)==100
def onb(cells):return all(orth(grid[a],grid[b]) for a,b in itertools.combinations(cells,2))
rows_ok=all(onb([(r,c) for c in range(10)]) for r in range(10))
cols_ok=all(onb([(r,c) for r in range(10)]) for c in range(10))
T1=[[(x[0],5+x[1]) for x in itertools.product(range(5),repeat=2) if (x[0]+x[1])%5==u]+
    [(5+x[0],x[1]) for x in itertools.product(range(5),repeat=2) if (x[0]+x[1])%5==u] for u in range(5)]
t1_ok=all(len(cl)==10 and onb(cl) for cl in T1)
cells=sorted(grid);nonpar=all(not parallel(grid[a],grid[b]) for a,b in itertools.combinations(cells,2))
O={(a,b):orth(grid[a],grid[b]) for a,b in itertools.combinations(cells,2)}
def isorth(a,b):return O[(a,b)] if (a,b) in O else O[(b,a)]
trans=[]
def rec(r,used,chosen):
    if r==10:trans.append(tuple(chosen));return
    for c in range(10):
        if c in used:continue
        if all(isorth((r,c),z) for z in chosen):rec(r+1,used|{c},chosen+[(r,c)])
rec(0,frozenset(),[])
t1_sets=sorted(tuple(sorted(cl)) for cl in T1)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'rows_onb':rows_ok,'columns_onb':cols_ok,'T1_label_classes_onb':t1_ok,'rays_pairwise_nonparallel':nonpar,
 'exactly_orthogonal_pairs':sum(O.values()),'orthogonal_transversals':len(trans),
 'orthogonal_transversals_equal_T1_classes':sorted(tuple(sorted(t)) for t in trans)==t1_sets,
 'one_resolvable':False if len(trans)<10 else 'needs exact cover','status':'PASS' if rows_ok and cols_ok and t1_ok and nonpar else 'FAIL'}
(P/'frontier-20261029-half-resolved-maximal-qls10-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
