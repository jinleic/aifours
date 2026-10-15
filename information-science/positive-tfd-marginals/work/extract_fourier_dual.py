#!/usr/bin/env python3
"""Generate a rational globally nonnegative dual candidate; integrals numerical here."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack, hstack, csr_matrix
from scipy.integrate import quad
from screen_fourier import data


def density(t):
    p=4*t**4-12*t*t+3
    return (196+p*p)*np.exp(-t*t)/(220*np.sqrt(np.pi))


def current(t):
    return 14*(16*t**3-24*t)*np.exp(-t*t)/(220*np.sqrt(np.pi))


def run(n, limit):
    edges=np.linspace(-limit,limit,n+1)
    x,mass,moments,*_=data({0:1,4:1j*np.sqrt(6)/7},edges,order=40)
    row=[]; col=[]; val=[]
    for i in range(n):
        for j in range(n):
            for r,v in ((i,1),(n+j,1),(2*n+i,x[j]),(3*n+j,x[i])):
                row.append(r);col.append(i*n+j);val.append(v)
    a=coo_matrix((val,(row,col)),shape=(4*n,n*n)).tocsr()
    am=a[2*n:]
    mm=np.r_[moments,-moments]
    pp=np.r_[mass,mass]
    delta=limit/n
    upper=hstack((vstack((am,-am)),csr_matrix(-np.concatenate((pp,pp))[:,None])))
    # The shared slack multiplies each row's mass.
    equal=hstack((a[:2*n],csr_matrix((2*n,1))))
    objective=np.zeros(n*n+1);objective[-1]=1
    result=linprog(objective,A_eq=equal,b_eq=pp,A_ub=upper,
                   b_ub=np.r_[mm+delta*pp,-mm+delta*pp],method='highs',
                   options={'time_limit':60,'primal_feasibility_tolerance':1e-9,
                            'dual_feasibility_tolerance':1e-9})
    if result.status!=0:
        return {'n':n,'limit':limit,'status':int(result.status),'message':result.message}
    y=result.eqlin.marginals; z=result.ineqlin.marginals
    aa=-y[:n];bb=-y[n:]
    hh=-(z[:n]-z[2*n:3*n]);kk=-(z[n:2*n]-z[3*n:])
    aa+=delta*abs(hh);bb+=delta*abs(kk)
    scale=max(np.max(abs(q)) for q in (aa,bb,hh,kk))
    if scale==0: return {'n':n,'limit':limit,'status':0,'slack':float(result.fun)}
    denom=10**6
    rat=lambda arr:[F(int(round(v/scale*denom)),denom) for v in arr]
    aa,bb,hh,kk=map(rat,(aa,bb,hh,kk))
    ed=[F(-limit)+F(2*limit*i,n) for i in range(n+1)]
    minimum=min(aa[i]+bb[j]+hh[i]*w+kk[j]*t
                for i in range(n) for j in range(n)
                for t in (ed[i],ed[i+1]) for w in (ed[j],ed[j+1]))
    correction=max(F(0),-minimum)+F(1,denom)
    aa=[v+correction for v in aa]
    minimum+=correction
    H=max(abs(v) for v in hh);K=max(abs(v) for v in kk)
    A=max(abs(v) for v in aa);B=max(abs(v) for v in bb)
    interior=sum(float(aa[i]+bb[i])*quad(density,float(ed[i]),float(ed[i+1]),epsabs=1e-13)[0]
                 +float(hh[i]-kk[i])*quad(current,float(ed[i]),float(ed[i+1]),epsabs=1e-13)[0]
                 for i in range(n))
    tail=2*quad(lambda t:float(H+K)*t*density(t)+float(A+B)*density(t),limit,np.inf,epsabs=1e-13)[0]
    return {'n':n,'limit':limit,'status':0,'slack':float(result.fun),
            'normalization_scale':float(scale),'edges':ed,'a':aa,'b':bb,'h':hh,'k':kk,
            'minimum_corner_value':minimum,'tail_coefficients':{'H':H,'K':K,'A':A,'B':B},
            'numerical_interior_integral':interior,'numerical_tail_bound':tail,
            'numerical_total':interior+tail,
            'warning':'Only global corner inequality is exact here. Integrals and convex order still need certification.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();results=[]
    for n,lim in ((24,4),(32,4),(40,5)):
        result=run(n,lim);results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k not in ('a','b','h','k','edges')},default=str),flush=True)
        args.output.write_text(json.dumps({'results':results},indent=2,default=str)+'\n')
