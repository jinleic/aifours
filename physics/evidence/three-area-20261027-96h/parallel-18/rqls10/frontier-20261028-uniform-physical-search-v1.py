#!/usr/bin/env python3
"""Bounded actual-vector search in the uniform-overlap branch.

The first row is a fixed ONB; each other vector has the exact two forced zero
coordinates and equal nonzero magnitudes. All remaining squared Gram entries
are optimized simultaneously. Floating output is NOT a witness certificate.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
n=10; N=n*n


def make(incidence):
    L=([[oa.w1.TABLE[r][c][1] for c in range(n)] for r in range(n)] if incidence=='weisner'
       else [[int(oa.PARKER_B[r][c]) for c in range(n)] for r in range(n)])
    assert all(set(row)==set(range(n)) for row in L)
    assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
    inv={L[0][c]:c for c in range(n)}
    mask=np.zeros((n,N),dtype=bool)
    for r in range(1,n):
        for c in range(n):
            j=inv[L[r][c]]
            assert j!=c
            mask[:,n*r+c]=True
            mask[c,n*r+c]=False; mask[j,n*r+c]=False
    target=np.empty((N,N))
    for x in range(N):
        r,c=divmod(x,n)
        for y in range(N):
            s,d=divmod(y,n)
            target[x,y]=1.0 if x==y else (0.0 if r==s or c==d or L[r][c]==L[s][d] else 1/8)
    return L,mask,target


def vectors(theta,mask):
    V=np.zeros((n,N),complex)
    V[:,:n]=np.eye(n)
    V[mask]=np.exp(1j*theta[mask])/np.sqrt(8)
    return V


def objective(theta,mask,target):
    V=vectors(theta,mask)
    G=V.conj().T@V
    E=np.abs(G)**2-target
    cost=float(np.sum(E**2)/2)
    W=V@(E*G)
    grad=4*np.imag(np.conj(V)*W)
    grad[~mask]=0
    return cost,grad,V,G


def run():
    p=argparse.ArgumentParser()
    p.add_argument('--incidence',choices=('weisner','parker'),default='parker')
    p.add_argument('--restarts',type=int,default=4)
    p.add_argument('--steps',type=int,default=4000)
    p.add_argument('--seconds',type=float,default=50)
    p.add_argument('--seed',type=int,default=3201)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0: raise ValueError('positive limits')
    L,mask,target=make(args.incidence)
    rng=np.random.default_rng(args.seed)
    theta=rng.uniform(-np.pi,np.pi,size=(n,N))
    direction=rng.normal(size=(n,N)); direction[~mask]=0
    direction/=np.linalg.norm(direction)
    cost,grad,_,_=objective(theta,mask,target)
    h=1e-5
    numeric=(objective(theta+h*direction,mask,target)[0]-objective(theta-h*direction,mask,target)[0])/(2*h)
    analytic=float(np.sum(grad*direction))
    print('gradient check analytic',analytic,'central_difference',numeric,'absolute_error',abs(analytic-numeric),flush=True)
    if abs(analytic-numeric)>1e-6: raise AssertionError('gradient check failed')
    start=time.monotonic(); best=None; records=[]
    for run in range(args.restarts):
        theta=rng.uniform(-np.pi,np.pi,size=(n,N))
        m=np.zeros_like(theta); v=np.zeros_like(theta)
        for step in range(1,args.steps+1):
            cost,grad,V,G=objective(theta,mask,target)
            m=0.9*m+0.1*grad; v=0.999*v+0.001*grad**2
            rate=0.04*max(0.15,1-step/args.steps)
            theta-=rate*(m/(1-0.9**step))/(np.sqrt(v/(1-0.999**step))+1e-8)
            if step==1 or step%100==0 or step==args.steps:
                cost,_,V,G=objective(theta,mask,target)
                err=np.abs(np.abs(G)**2-target)
                result={'objective':cost,'max_squared_gram_error':float(np.max(err)),
                        'max_forced_inner_product':float(np.max(np.abs(G[(target==0)]))),
                        'min_nonforced_squared_overlap':float(np.min(np.abs(G[target==0.125])**2)),
                        'max_nonforced_squared_overlap':float(np.max(np.abs(G[target==0.125])**2))}
                if best is None or cost<best[0]: best=(cost,V.copy(),run,step,result)
                if result['max_squared_gram_error']<1e-10:
                    print('NUMERIC_CANDIDATE_REQUIRES_CERTIFICATION',run,step,result,flush=True)
                    break
            if time.monotonic()-start>=args.seconds: break
        records.append({'restart':run,'steps':step,**result})
        print('restart',run,'steps',step,'metrics',result,flush=True)
        if time.monotonic()-start>=args.seconds: break
    stem=f'frontier-20261028-uniform-physical-{args.incidence}'
    np.save(ROOT/(stem+'-best-v1.npy'),best[1],allow_pickle=False)
    data={'incidence':args.incidence,'parameters':vars(args),'elapsed_seconds':time.monotonic()-start,
          'runs':records,'best_restart':best[2],'best_step':best[3],'best_metrics':best[4],
          'best_file':stem+'-best-v1.npy',
          'caveat':'floating point, fixed L and uniform branch, not a proof/certificate'}
    (ROOT/(stem+'-result-v1.json')).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print('best',best[2],best[3],best[4],flush=True)
    print('wrote',stem+'-{best,result}-v1',flush=True)


if __name__=='__main__': run()
