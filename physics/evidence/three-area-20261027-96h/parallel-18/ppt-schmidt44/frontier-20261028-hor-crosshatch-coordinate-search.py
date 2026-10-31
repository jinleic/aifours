#!/usr/bin/env python3
"""Bounded FLOATING 4x4 cuts of the published 4x12 Horodecki-crosshatch state."""
from itertools import combinations,product
import json,numpy as np
H=(((0,0,1),),((0,1,1),(1,0,1)),((0,3,1),(1,2,1)),
   ((0,2,1),(1,1,1)),((1,3,2**.5),(1,0,1)))
C=(((1,0,1),(0,2,1)),((2,0,1),(1,2,1)),((0,0,1),(2,1,1)),((0,1,1),(2,2,1)))
A=((0,0),(0,1),(0,2),(1,1));vs=[]
for x,y in product(H,C):
 v=np.zeros(48,dtype=np.complex128)
 for (a,b,u),(c,d,w) in product(x,y):
  if (a,c) in A:v[12*A.index((a,c))+3*b+d]+=u*w
 vs.append(v)
rho=sum((np.outer(v,v.conj()) for v in vs),np.zeros((48,48),complex))
def scores(x):
 x=x/np.trace(x).real;v=x.reshape(4,4,4,4)
 mat=v.transpose(0,2,1,3).reshape(16,16)
 rc=float(np.linalg.svd(mat,compute_uv=False).sum())
 a=np.trace(v,axis1=1,axis2=3);b=np.trace(v,axis1=0,axis2=2)
 pa=np.trace(a@a).real;pb=np.trace(b@b).real
 cent=(x-np.kron(a,b)).reshape(4,4,4,4).transpose(0,2,1,3).reshape(16,16)
 cov=float(np.linalg.svd(cent,compute_uv=False).sum()-1-np.sqrt(max(0,1-pa)*max(0,1-pb)))
 return rc,cov
results=[]
for BB in combinations(range(12),4):
 ix=[12*a+b for a in range(4) for b in BB];out=rho[np.ix_(ix,ix)];tr=np.trace(out).real
 if tr<=0:continue
 rc,cov=scores(out)
 ranks=[]
 for v in vs:
  M=v[ix].reshape(4,4);ranks.append(int(np.linalg.matrix_rank(M,tol=1e-9)))
 results.append({'bob':list(BB),'trace_float':float(tr),'realignment_float':rc,'covariance_gap_float':cov,
                 'high_rank_source_vectors':sum(k>=3 for k in ranks),'source_output_rank_float':int(np.linalg.matrix_rank(out,tol=1e-9))})
print(json.dumps({'source':'arXiv:2402.12966v1 Eq.8 and Appendix E; Horodecki plus crosshatch',
 'source_trace_float':float(np.trace(rho).real),'bob_coordinate_cuts':len(results),
 'top_realignment':sorted(results,key=lambda x:-x['realignment_float'])[:5],
 'top_covariance':sorted(results,key=lambda x:-x['covariance_gap_float'])[:5],
 'most_high_rank_kets':sorted(results,key=lambda x:-x['high_rank_source_vectors'])[:5],
 'limits':'Floating finite exploration; no exact witness, PPT, rank or SN claim. No violation excludes nothing.'},indent=2))
