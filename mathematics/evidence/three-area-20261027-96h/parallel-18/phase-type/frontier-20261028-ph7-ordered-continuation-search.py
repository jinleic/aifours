#!/usr/bin/env python3
"""Continue a verified PH7 point by constrained same-matrix optimization.

The 3+3 blocks are nontriangular, feedback is fully coupled, and all six
characteristic coefficients are equality constraints. SLSQP output is not a
witness: an exact Fraction full-matrix checker is required for every claim.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import minimize
nu=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
gen=SourceFileLoader('go',str(ROOT/'frontier-20261028-ph7-generalized-ordered-search.py')).load_module()
rates=list(map(F,['669/500','1339/1000','671/500','669/500','1043/1000','1041/1000']))
nu.Z=F(820409,1000000);v=nu.rational_family(rates)
x0=np.array([float(q)for q in rates]+[0.]*7+[float(v['C0']),float(v['B'])]
 +[0.]*3+[0.,0.,float(v['phi'])]
 +[float(v['D1']),0.,0.,float(v['D2']),0.,0.,float(v['D3']),0.,0.]+[float(nu.Z)])
assert len(x0)==31
bounds=[(.05,8.)]*6+[(0.,8.)]*7+[(0.,25.)]*2+[(0.,40.)]*15+[(.8,1.)]

def conditions(x):
    M,b,w,p,q,_=gen.data(x[-1],x[:6],x[6:13],x[13:15]);M=np.asarray(M,float).T;b=np.asarray(b,float)
    return M@x[15:30]-b,w,p,q

def eq(x):
    r,_,_,_=conditions(x)
    return r/np.array([10.,10.,20.,20.,20.,10.])
def inequ(x):
    _,w,p,q=conditions(x);return np.array([w,p,q])

start=time.monotonic();runs=[];best=None;exact=None;rng=np.random.default_rng(20261109)
for i in range(4):
    if time.monotonic()-start>100:break
    if i==0:startx=x0.copy()
    else:
        startx=x0+rng.normal(0,.015,len(x0))*np.maximum(.001,np.abs(x0));startx[-1]=x0[-1]
        startx=np.array([min(max(a,lo+1e-12),hi-1e-12)for a,(lo,hi)in zip(startx,bounds)])
    result=minimize(lambda x:-x[-1],startx,method='SLSQP',bounds=bounds,
                    constraints=[{'type':'eq','fun':eq},{'type':'ineq','fun':inequ}],
                    options={'maxiter':1200,'ftol':1e-12})
    er=float(np.linalg.norm(eq(result.x),ord=np.inf));val=float(result.x[-1])
    runs.append({'start':i,'success':bool(result.success),'message':str(result.message),'iterations':int(result.nit),
                 'z':val,'normalized_equality_residual':er,'min_constraints':float(min(inequ(result.x)))})
    if best is None or val>best[0]:best=(val,result.x.copy(),er)
    print('start',i,'z',val,'eq',er,'success',result.success,flush=True)
    if er<1e-9 and val>.821:
        for den in (10000,100000,1000000):
            zz=F(int((val-1e-5)*den),den)
            if zz<=F(82041,100000):continue
            gen.Z=zz;candidate=gen.exact_project(result.x[:30])
            if candidate:exact={'z':str(zz),'witness':candidate};break
        if exact:break
out=ROOT/'frontier-20261028-ph7-ordered-continuation-search-result.json'
out.write_text(json.dumps({'runs':runs,'best_numeric_z':best[0]if best else None,
 'best_parameters':best[1].tolist()if best else None,'best_residual':best[2]if best else None,
 'exact_witness':exact,'elapsed_seconds':time.monotonic()-start,
 'scope':'one enlarged 3+3 graph, no optimality/exclusion from local optimizer'},indent=2)+'\n')
print('saved:',out,'exact',bool(exact))
