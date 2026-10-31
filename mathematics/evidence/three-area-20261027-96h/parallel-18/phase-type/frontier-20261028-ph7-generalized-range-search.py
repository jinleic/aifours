#!/usr/bin/env python3
"""Continue the actual PH7 matrix toward 8/9 with nontriangular blocks.

Warm-start at an exact positive 7-state candidate. Additional allowed arcs,
center feedback and full 3x3 return matrix enlarge that construction. Numeric
optimization is proposal-only; exact rational full-matrix verification is
required before any witness claim. Failure excludes no continuum or topology.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json, sys, time, numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
nu=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
gen=SourceFileLoader('ordered',str(ROOT/'frontier-20261028-ph7-generalized-ordered-search.py')).load_module()
seed_rates=list(map(F,['669/500','1339/1000','671/500','669/500','1043/1000','1041/1000']))
nu.Z=F(820409,1000000);v=nu.rational_family(seed_rates)
base=np.array([float(t)for t in seed_rates]+[0.]*7+[float(v['C0']),float(v['B'])]
              +[0.]*3+[0.,0.,float(v['phi'])]
              +[float(v['D1']),0.,0.,float(v['D2']),0.,0.,float(v['D3']),0.,0.])
assert len(base)==30
RATIOS=[F(33,40),F(83,100),F(5,6),F(17,20),F(8,9)]
STARTS=4;MAX_NFEV=2500;WALL_LIMIT=110;RNG=np.random.default_rng(20261105)
lower=np.array([.05]*6+[0.]*24);upper=np.array([7.]*6+[10.]*7+[25.]*2+[40.]*15)

def fun(x,z):
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        A,b,w,p,q,_=gen.data(float(z),x[:6],x[6:13],x[13:15]); M=np.asarray(A,float).T;b=np.asarray(b,float);fb=x[15:]
        result=np.r_[(M@fb-b)/(1+np.abs(b)+np.abs(M)@fb),min(w,0.),min(q,0.)]
    return result if np.all(np.isfinite(result)) else np.full(8,1e8)

start=time.monotonic();rows=[]
for z in RATIOS:
    best=None;exact=None;attempts=[];gen.Z=z
    for j in range(STARTS):
        if time.monotonic()-start>WALL_LIMIT:break
        if j==0:x0=base.copy()
        else:
            scale=np.maximum(np.abs(base),.05)
            x0=base+RNG.normal(0,.1,len(base))*scale
        x0=np.maximum(lower+1e-10,np.minimum(upper-1e-10,x0))
        try:
            fit=least_squares(lambda x:fun(x,z),x0,bounds=(lower,upper),max_nfev=MAX_NFEV,
                              ftol=1e-12,xtol=1e-12,gtol=1e-12)
        except (np.linalg.LinAlgError, ValueError) as exc:
            attempts.append({'start':j,'optimizer_error':str(exc)})
            continue
        err=float(np.linalg.norm(fun(fit.x,z),ord=np.inf));attempts.append({'start':j,'residual_inf':err,'nfev':int(fit.nfev)})
        if best is None or err<best[0]:best=(err,fit.x.copy())
        if err<1e-8:
            exact=gen.exact_project(fit.x)
            if exact:base=fit.x.copy();break
    row={'z':str(z),'attempts':attempts,'best_residual_inf':best[0] if best else None,
         'best_parameters':best[1].tolist() if best else None,'exact_witness':exact};rows.append(row)
    print('z',z,'starts',len(attempts),'best',row['best_residual_inf'],'exact',bool(exact),flush=True)
    if time.monotonic()-start>WALL_LIMIT:break
out=ROOT/'frontier-20261028-ph7-generalized-range-search-result.json'
out.write_text(json.dumps({'seed':20261105,'elapsed_seconds':time.monotonic()-start,'rows':rows,
 'scope':'one enlarged ordered graph, numerical failure not universal exclusion'},indent=2)+'\n')
print('saved:',out)
