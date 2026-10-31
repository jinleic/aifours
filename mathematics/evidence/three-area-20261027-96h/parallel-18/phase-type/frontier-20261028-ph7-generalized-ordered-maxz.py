#!/usr/bin/env python3
"""Numerical maximum-z continuation in the full ordered 3+1+3 graph.

This contains the proven v4 two-cycle point and prior generalized ordered
search: it has all 15 center/cross feedbacks and seven outer-block arcs.
No numerical result is an existence/optimality claim. Any reported point
above the old interval must pass direct exact Fraction PH verification.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import minimize
from numpy.polynomial.polynomial import polymul,polypow
G=SourceFileLoader('genmax',str(ROOT/'frontier-20261028-ph7-generalized-ordered-search.py')).load_module()
rng=np.random.default_rng(20261112);start=time.monotonic();WALL=100
U=1.33878790715898607629;V=1.0420296911339997153;z0=.82042044078412600605
p=5*U+2*V-4;q=10*U**2+10*U*V-20*U+V**2-8*V-2*z0+10
B=p-2*U;C=q-U*p+U**2
poly0=polymul(polypow([U,1.],5),polypow([V,1.],2))
dz=polymul([0.,1.],polypow([1+z0,2.,1.],2));poly1=polymul(dz,[q,p,1.]);R=poly0-poly1
D1=R[2];D3=R[0]-V*V*D1
fb=np.zeros(15);fb[6]=D1;fb[12]=D3
seed=np.r_[[U,U,U,U,V,V],np.zeros(7),[C,B],fb,z0]
lo=np.array([.1]*6+[0.]*7+[0.]*2+[0.]*15+[.5])
hi=np.array([6.]*6+[5.]*7+[15.]*2+[50.]*15+[8/9])
bounds=list(zip(lo,hi))

def equal(x):
    M,b,w,p,q,Q=G.data(x[-1],x[:6],x[6:13],x[13:15]);M=np.asarray(M,float).T;b=np.asarray(b,float);fb=x[15:30]
    return (b-M@fb)/(1+np.abs(b)+np.abs(M)@fb)

def positive(x):
    M,b,w,p,q,Q=G.data(x[-1],x[:6],x[6:13],x[13:15]);return np.array([w-.001,p-.001,q-.001])

assert np.linalg.norm(equal(seed),np.inf)<1e-10 and min(positive(seed))>0
runs=[];best=None;exact=None
for j in range(5):
    if time.monotonic()-start>WALL:break
    if j==0:x=seed.copy()
    else:
        x=seed+ rng.normal(0,.002,31)*np.maximum(.05,np.abs(seed));x[-1]=seed[-1]
        x=np.maximum(lo+1e-12,np.minimum(hi-1e-12,x))
    fit=minimize(lambda x:-x[-1],x,method='SLSQP',bounds=bounds,
      constraints=[{'type':'eq','fun':equal},{'type':'ineq','fun':positive}],
      options={'maxiter':1000,'ftol':1e-12,'disp':False})
    err=float(np.linalg.norm(equal(fit.x),np.inf));item={'start':j,'z':float(fit.x[-1]),'residual_inf':err,
      'min_physical_inequality':float(min(positive(fit.x))),'success':bool(fit.success),'message':str(fit.message),'iterations':int(fit.nit)}
    runs.append(item);print('run',j,item,flush=True)
    if err<1e-8 and min(positive(fit.x))>=0 and (best is None or fit.x[-1]>best[0]):best=(fit.x[-1],fit.x.copy())
    if err<1e-8 and fit.x[-1]>.82043:
        z=F(int(fit.x[-1]*1000000)-1,1000000);G.Z=z
        exact=G.exact_project(fit.x[:30])
        if exact:break
out=ROOT/'frontier-20261028-ph7-generalized-ordered-maxz-result.json'
out.write_text(json.dumps({'runs':runs,'best_feasible_numeric_z':float(best[0]) if best else None,
 'best_parameters':best[1].tolist() if best else None,'exact_witness':exact,'elapsed_seconds':time.monotonic()-start,
 'scope':'larger ordered topology, numerical proposals only unless separately exact verified; no global optimum or exclusion'},indent=2)+'\n')
print('saved:',out)
