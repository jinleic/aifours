#!/usr/bin/env python3
"""Search the exact scalar equations of every 7-vertex 8-edge SCC shape.

A strongly connected n-vertex digraph with n+1 distinct directed edges is
one directed theta graph or a figure-eight. The shared segment has k edges,
the two branches l,m edges and k+l+m=8 (k=0 means a shared vertex).
Condition 0 is Perron-normalized by theta+(1-theta)=1. Solve for a double
visible nonreal eigenvalue at z=8/9. This is spectral exploration ONLY, not a
PH transfer, not a rational proof and not a global exclusion on any miss.
"""
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20261113);z=8/9;lam=-1+1j*np.sqrt(z);start=time.monotonic();WALL=95
patterns=[]
for k in range(6):
 for l in range(1,8-k):
  m=8-k-l
  if l>m or m<1 or (k==0 and l<2) or (l==m==1):continue
  patterns.append((k,l,m))

def indices(k,l,m):
 common=list(range(k+1));left=list(range(k+1,k+l));right=list(range(k+l,7))
 assert len(common)+len(left)+len(right)==7
 return common+left,common+right

def fun(x,k,l,m):
 a,b=indices(k,l,m);u=x[:7];t=x[7];
 f1=np.prod(u[a]/(u[a]+lam));f2=np.prod(u[b]/(u[b]+lam))
 f=t*f1+(1-t)*f2-1
 derivative=t*f1*np.sum(1/(u[a]+lam))+(1-t)*f2*np.sum(1/(u[b]+lam))
 return np.array([f.real,f.imag,derivative.real,derivative.imag])

rows=[];hits=[]
for pat in patterns:
 best=None;runs=[]
 for j in range(4):
  if time.monotonic()-start>WALL:break
  x=np.r_[rng.uniform(.5,3.,7),rng.uniform(.1,.9)]
  if pat==(4,1,3) and j==0:
   U=1.338787907158986;V=1.042029691134;D1=2.79968191053
   x=np.r_[np.repeat(U,5),np.repeat(V,2),D1/U**5]
  fit=least_squares(fun,x,args=pat,bounds=(np.r_[[.05]*7,1e-5],np.r_[[10.]*7,1-1e-5]),
    max_nfev=1300,ftol=1e-12,xtol=1e-12,gtol=1e-12)
  err=float(np.linalg.norm(fun(fit.x,*pat),np.inf));runs.append({'start':j,'residual_inf':err,'nfev':int(fit.nfev)})
  if best is None or err<best[0]:best=(err,fit.x.copy())
 row={'k_l_m':list(pat),'runs':runs,'best_residual_inf':best[0]if best else None,
      'best_parameters':best[1].tolist()if best else None}
 rows.append(row)
 if best and best[0]<1e-8:hits.append(row)
 print('shape',pat,'best',row['best_residual_inf'],flush=True)
 if time.monotonic()-start>WALL:break
out=ROOT/'frontier-20261028-ph7-eight-edge-spectral-search-result.json'
out.write_text(json.dumps({'z':'8/9','patterns_enumerated':len(patterns),'patterns_attempted':len(rows),
 'shapes':rows,'numerical_hits_under_1e-8':hits,'elapsed_seconds':time.monotonic()-start,
 'scope':'all abstract theta/figure-eight cycle lengths, finite box and multistart; only double-eigenvalue conditions; no PH claim or exclusion'},indent=2)+'\n')
print('saved:',out)
