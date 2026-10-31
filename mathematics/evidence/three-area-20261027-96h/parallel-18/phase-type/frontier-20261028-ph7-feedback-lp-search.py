#!/usr/bin/env python3
"""Bounded LP-guided search for same-matrix ordered PH7 feedback.

For each proposed outer tuple, optimize all 15 nonnegative feedback variables
against the FULL six-coefficient characteristic identity. This removes the
previous nonlinear least-squares feedback bottleneck. A numeric LP fit is not
a witness: every prospective fit must pass exact rational matrix checks.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import linprog, minimize
nu=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
gen=SourceFileLoader('go',str(ROOT/'frontier-20261028-ph7-generalized-ordered-search.py')).load_module()
seed_rates=list(map(F,['669/500','1339/1000','671/500','669/500','1043/1000','1041/1000']))
nu.Z=F(820409,1000000);v=nu.rational_family(seed_rates)
seed=np.array([float(x) for x in seed_rates]+[0.]*7+[float(v['C0']),float(v['B'])])
BOUNDS=[(.5,3.)]*6+[(0.,2.)]*7+[(0.,8.)]*2
RATIOS=[F(33,40),F(83,100),F(17,20),F(8,9)]
RNG=np.random.default_rng(20261107);MAX_STARTS=3;MAX_EVAL=3000;WALL=100
start=time.monotonic();rows=[]


def solve_outer(x,z):
    M,b,w,p,q,_=gen.data(float(z),x[:6],x[6:13],x[13:15]);M=np.asarray(M,float).T;b=np.asarray(b,float)
    if not (np.isfinite(M).all() and np.isfinite(b).all() and w>0 and q>0):
        return 10.+abs(min(w,0.))+abs(min(q,0.)),None
    scale=1+np.abs(b); A=np.c_[M,-scale];B=np.c_[-M,-scale]
    result=linprog(np.r_[np.zeros(15),1.],A_ub=np.vstack((A,B)),b_ub=np.r_[b,-b],
                   bounds=[(0,1000)]*15+[(0,None)],method='highs')
    if not result.success:return 100.,None
    return float(result.x[-1]),result.x[:15]

for z in RATIOS:
    gen.Z=z;best=None;exact=None;attempts=[]
    for j in range(MAX_STARTS):
        if time.monotonic()-start>WALL:break
        if j==0:x=seed.copy()
        else:x=np.clip(seed+RNG.normal(0,.08,15)*np.maximum(.1,np.abs(seed)),
                       [v[0] for v in BOUNDS],[v[1] for v in BOUNDS])
        fit=minimize(lambda y:solve_outer(y,z)[0],x,method='Powell',bounds=BOUNDS,
                     options={'maxfev':MAX_EVAL,'xtol':1e-7,'ftol':1e-10})
        err,fb=solve_outer(fit.x,z);attempts.append({'start':j,'objective':err,'nfev':int(fit.nfev),'solver_message':str(fit.message)})
        if best is None or err<best[0]:best=(err,fit.x.copy(),fb)
        if err<1e-8 and fb is not None:
            exact=gen.exact_project(np.r_[fit.x,fb])
            if exact:seed=fit.x.copy();break
    rows.append({'z':str(z),'attempts':attempts,'best_objective':best[0] if best else None,
                 'best_outer':best[1].tolist() if best else None,
                 'best_feedback':best[2].tolist() if best and best[2] is not None else None,'exact_witness':exact})
    print('z',z,'starts',len(attempts),'best',rows[-1]['best_objective'],'exact',bool(exact),flush=True)
    if time.monotonic()-start>WALL:break
out=ROOT/'frontier-20261028-ph7-feedback-lp-search-result.json'
out.write_text(json.dumps({'seed':20261107,'elapsed_seconds':time.monotonic()-start,'rows':rows,
 'scope':'specified enlarged ordered graph only; LP/optimizer misses never prove nonexistence'},indent=2)+'\n')
print('saved:',out)
