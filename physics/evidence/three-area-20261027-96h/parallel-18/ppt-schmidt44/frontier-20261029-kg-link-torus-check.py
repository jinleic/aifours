#!/usr/bin/env python3
"""Exact Gaussian-integer checks for KG source torus weights and coordinate cuts."""
import itertools
import json
from collections import defaultdict

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scal(v,z): return [mul(x,z) for x in v]
def gsum(*v):
    return [(sum(x[i][0] for x in v),sum(x[i][1] for x in v)) for i in range(len(v[0]))]
def ket(*terms):
    v=[(0,0) for _ in range(20)]
    for a,b,c in terms:v[5*a+b]=add(v[5*a+b],(c,0))
    return v

e0=ket((0,0,1),(1,1,1),(2,2,1));e1=ket((0,1,1),(1,2,1));e2=ket((1,0,1),(2,1,-1))
C=ket((0,2,1),(3,4,1));E=ket((2,0,1),(3,3,1));F=ket((2,3,1));G=ket((3,0,1));I=ket((3,2,1));H=ket((0,4,1))
source=[(1,e0),(1,e1),(1,e2),(3,C),(3,E),(3,F),(3,G),(3,I),(3,H)]
fa=((0,0),(1,0),(2,0),(0,1));gb=((0,0),(-1,0),(-2,0),(2,-1),(-2,-1))
char=[(fa[a][0]+gb[b][0],fa[a][1]+gb[b][1]) for a in range(4) for b in range(5)]
for _,v in source:
    assert len({char[i] for i,x in enumerate(v) if x!=(0,0)})==1
blocks=defaultdict(list)
for idx,c in enumerate(char):blocks[c].append(idx)
assert sorted(map(len,blocks.values()))==[1]*9+[2]*4+[3]
sectors=defaultdict(list)
for i,j in itertools.product(range(5),repeat=2):
    sectors[(gb[i][0]-gb[j][0],gb[i][1]-gb[j][1])].append((i,j))
assert len(sectors[(0,0)])==5 and sorted(len(v) for k,v in sectors.items() if k!=(0,0))==[1]*16+[2]*2
assert sectors[(1,0)]==[(0,1),(1,2)] and sectors[(-1,0)]==[(1,0),(2,1)]

def pt_cut(v,j): return [x if idx%5!=j else (0,0) for idx,x in enumerate(v)]
def outer(v): return [[mul(v[i],conj(v[j])) for j in range(20)] for i in range(20)]
def matadd(dest,src,m=1):
    for i in range(20):
        for j in range(20):dest[i][j]=add(dest[i][j],(m*src[i][j][0],m*src[i][j][1]))
def det3(v,rows,cols):
    out=(0,0)
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        t=(1,0)
        for i in range(3):t=mul(t,v[5*rows[i]+cols[p[i]]])
        out=add(out,neg(t) if inv%2 else t)
    return out

def cut_identity(j):
    rho=[[(0,0) for _ in range(20)] for _ in range(20)]
    for w,v in source:matadd(rho,outer(pt_cut(v,j)),4*w)
    rec=[[(0,0) for _ in range(20)] for _ in range(20)]
    roots=((1,0),(0,1),(-1,0),(0,-1))
    for z in roots:
        z2=mul(z,z);z3=mul(z2,z)
        if j==3:q=gsum(scal(e0,z),e1,scal(e2,neg(z2)),scal(ket((2,0,1)),neg(z3)))
        else:q=gsum(scal(e0,z),scal(e1,z2),scal(e2,(-1,0)),scal(ket((0,2,1)),z3))
        q=pt_cut(q,j)
        assert all(det3(q,rows,cols)==(0,0) for rows in itertools.combinations(range(4),3) for cols in itertools.combinations(range(5),3))
        matadd(rec,outer(q))
    if j==3:
        rest=[(2,ket((2,0,1))),(3,C),(3,G),(3,I),(3,H)]
    else:
        rest=[(2,ket((0,2,1))),(3,E),(3,F),(3,G),(3,I)]
    for w,v in rest:matadd(rec,outer(pt_cut(v,j)),4*w)
    assert rho==rec
    return 4*len(list(itertools.combinations(range(4),3)))*len(list(itertools.combinations(range(5),3)))
checks=cut_identity(3)+cut_identity(4)
print(json.dumps({'source_blocks':sorted(map(len,blocks.values())),'source_invariant_hermitian_parameters':sum(len(v)**2 for v in blocks.values()),
 'link_zero_sector':5,'link_nonzero_sector_sizes':sorted(len(v) for k,v in sectors.items() if k!=(0,0)),
 'nonzero_sector_all_matrix_ranks_at_most':2,'cut_3_4_exact_decompositions':True,'3x3_minor_checks':checks,
 'projector_entries_per_cut':400,'scope':'Exact integer/Gaussian arithmetic; index theorem is a written proof, not this finite check.'},indent=2))
