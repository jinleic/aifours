#!/usr/bin/env python3
"""Direct float check of all original QLS and uniform pairs, independent of optimizer."""
import argparse
import importlib.util
from pathlib import Path
from itertools import combinations
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
p=argparse.ArgumentParser()
p.add_argument('array')
p.add_argument('--incidence',choices=('parker','weisner'),required=True)
args=p.parse_args()
n=10
L=([[int(oa.PARKER_B[r][c]) for c in range(n)] for r in range(n)] if args.incidence=='parker'
   else [[oa.w1.TABLE[r][c][1] for c in range(n)] for r in range(n)])
assert all(set(row)==set(range(n)) for row in L)
assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
v=np.load(args.array,allow_pickle=False)
assert v.shape==(10,100) and np.isfinite(v).all()
blocks=[[(r,c) for c in range(n)] for r in range(n)]
blocks += [[(r,c) for r in range(n)] for c in range(n)]
blocks += [[(r,c) for r in range(n) for c in range(n) if L[r][c]==t] for t in range(n)]
assert all(len(b)==10 for b in blocks)
maxnorm=max(float(abs(np.vdot(v[:,i],v[:,i])-1)) for i in range(100))
worst=(0.0,None)
for blockidx,block in enumerate(blocks):
    for x,y in combinations(block,2):
        ix=n*x[0]+x[1]; iy=n*y[0]+y[1]
        value=float(abs(np.vdot(v[:,ix],v[:,iy])))
        if value>worst[0]: worst=(value,(blockidx,x,y))
nonforced=[]; near=0
for x,y in combinations(range(100),2):
    r,c=divmod(x,n); s,d=divmod(y,n)
    val=np.vdot(v[:,x],v[:,y])
    denom=np.linalg.norm(v[:,x])*np.linalg.norm(v[:,y])
    if abs(val)/denom>=1-1e-8: near+=1
    if r!=s and c!=d and L[r][c]!=L[s][d]:
        nonforced.append(float(abs(abs(val)**2-1/8)))
assert len(nonforced)==3600
print('incidence',args.incidence,'file',args.array)
print('all100 norm max_error',maxnorm)
print('all30 original ONBs worst offdiagonal',worst)
print('all3600 nonforced pairs max squared-overlap error',max(nonforced))
print('all4950 pairs near-parallel tolerance1e-8',near)
print('numerical uniform feasibility 1e-10',maxnorm<1e-10 and worst[0]<1e-10 and max(nonforced)<1e-10 and near==0)
print('floating point only; no rigorous exact certificate')
