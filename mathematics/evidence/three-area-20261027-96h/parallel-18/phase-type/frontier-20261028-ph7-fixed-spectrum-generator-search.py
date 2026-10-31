#!/usr/bin/env python3
"""Try actual row-generator inverse spectrum at critical z=8/9,p=8,q=15.

All 42 nonnegative offdiagonal entries are variables, normalized to sum12.
Five full characteristic coefficients are matched. This explores whether the
all-orders moment counterpoint is itself Metzler-realizable; numerical fits
and failures are never witnesses or nonexistence proofs.
"""
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20261115);I,J=np.where(~np.eye(7,dtype=bool));start=time.monotonic();WALL=95
z=8/9;target=np.convolve([1.,4.,6+2*z,4+4*z,(1+z)**2,0.],[1.,8.,15.])

def char(G):
 B=np.eye(7);out=[1.]
 for k in range(1,8):
  A=G@B;c=-np.trace(A)/k;out.append(c);B=A+c*np.eye(7)
 return np.array(out)

def mat(x):
 a=12*x/x.sum();G=np.zeros((7,7));G[I,J]=a;G[np.arange(7),np.arange(7)]=-G.sum(axis=1);return G

def fun(x):
 a=char(mat(x));return (a[2:7]-target[2:7])/(1+np.abs(target[2:7]))

rows=[];best=None
for j in range(16):
 if time.monotonic()-start>WALL:break
 if j<8:
  # Broad mixtures of a directed Hamilton cycle and a sparse second cycle.
  x=rng.exponential(.03,42)
  for i in range(7):x[np.where((I==i)&(J==(i+1)%7))[0][0]]=rng.uniform(.3,1.5)
  for _ in range(4):x[rng.integers(42)]+=rng.uniform(.05,1.5)
 else:x=rng.exponential(.4,42)
 fit=least_squares(fun,x,bounds=(np.full(42,1e-14),np.full(42,10.)),max_nfev=1600,
                    ftol=1e-12,xtol=1e-12,gtol=1e-12)
 err=float(np.linalg.norm(fun(fit.x),np.inf));item={'start':j,'max_scaled_residual':err,'nfev':int(fit.nfev)}
 rows.append(item);print('run',item,flush=True)
 if best is None or err<best[0]:best=(err,fit.x.copy())
 if err<1e-10:break
out=ROOT/'frontier-20261028-ph7-fixed-spectrum-generator-search-result.json'
out.write_text(json.dumps({'z':'8/9','p':'8','q':'15','runs':rows,'best_scaled_residual':best[0]if best else None,
 'best_rates_7x7':mat(best[1]).tolist()if best else None,'elapsed_seconds':time.monotonic()-start,
 'scope':'actual Markov-generator spectral search, floating proposal only; no rational PH witness or exclusion'},indent=2)+'\n')
print('saved:',out)
