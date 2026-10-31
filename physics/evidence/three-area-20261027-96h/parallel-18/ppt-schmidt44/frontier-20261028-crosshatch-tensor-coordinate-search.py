#!/usr/bin/env python3
"""Bounded FLOATING two-copy crosshatch coordinate-filter witness screen."""
from itertools import combinations,product
import json,numpy as np
# 3x3 crosshatch, arXiv:2402.12966v1 Figure 1. All four unnormalized edge kets.
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
vs=[]
for left,right in product(edges,repeat=2):
 q=np.zeros(81,dtype=np.complex128)
 for (a,b),(c,d) in product(left,right):q[(3*a+c)*9+(3*b+d)]+=1
 vs.append(q)
rho=sum((np.outer(v,v.conj()) for v in vs),np.zeros((81,81),complex))
def scores(x):
 x=x/np.trace(x).real;v=x.reshape(4,4,4,4)
 r=v.transpose(0,2,1,3).reshape(16,16)
 rc=float(np.linalg.svd(r,compute_uv=False).sum())
 A=np.trace(v,axis1=1,axis2=3);B=np.trace(v,axis1=0,axis2=2)
 pa=np.trace(A@A).real;pb=np.trace(B@B).real
 C=(x-np.kron(A,B)).reshape(4,4,4,4).transpose(0,2,1,3).reshape(16,16)
 cov=float(np.linalg.svd(C,compute_uv=False).sum()-1-np.sqrt(max(0,1-pa)*max(0,1-pb)))
 return rc,cov
vals=[];nonzero=0
for a,b in product(combinations(range(9),4),repeat=2):
 ix=[9*x+y for x in a for y in b];out=rho[np.ix_(ix,ix)];tr=np.trace(out).real
 if tr<=0:continue
 nonzero+=1;rc,cov=scores(out)
 vals.append({'alice':list(a),'bob':list(b),'trace':float(tr),'realignment_float':rc,'covariance_gap_float':cov})
valsR=sorted(vals,key=lambda x:-x['realignment_float']);valsC=sorted(vals,key=lambda x:-x['covariance_gap_float'])
print(json.dumps({'source':'two copies of 3x3 crosshatch, arXiv:2402.12966v1 Figure 1',
 'source_trace_float':float(np.trace(rho).real),'coordinate_pairs':126**2,'nonzero_outputs':nonzero,
 'top_realignment':valsR[:5],'top_covariance':valsC[:5],
 'limits':'Only finite coordinate filters and floating SVD. Violations require exact witness/PPT certificates; absence of a violation says nothing about arbitrary maps or SN.'},indent=2))
