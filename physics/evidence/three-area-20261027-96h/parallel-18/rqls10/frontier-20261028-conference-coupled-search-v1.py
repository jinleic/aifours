#!/usr/bin/env python3
"""Couple ten actual GF(9) conference columns through shared phase parameters.

Each column is an ONB to numerical precision throughout. Optimize the full
uniform Gram across rows/transversals and nonsharing pairs. No physical
solution is certified without independent exact/rigorous verification.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('uniform',ROOT/'frontier-20261028-uniform-physical-search-v1.py')
uniform=importlib.util.module_from_spec(spec); spec.loader.exec_module(uniform)
n=10; N=100
source=json.loads((ROOT/'frontier-20261028-gf9-conference-result-v1.json').read_text())
# Source stores exactly checked scaled integer pairs (a,b)/8 for Q(i sqrt 7).
C=np.array([[(source['basis2'][j+1][i+1][0]+1j*np.sqrt(7)*source['basis2'][j+1][i+1][1])/8
             for j in range(9)] for i in range(9)],complex)
assert np.max(np.abs(C.conj().T@C-np.eye(9)))<1e-12


def makebase(L,rng):
    inv={L[0][c]:c for c in range(n)}
    base=np.zeros((n,N),complex)
    base[:,:n]=np.eye(n)
    for c in range(n):
        coords=[k for k in range(n) if k!=c]
        perm=rng.permutation(9)
        index={k:int(perm[idx]) for idx,k in enumerate(coords)}
        for r in range(1,n):
            missing=inv[L[r][c]]
            assert missing!=c
            for k in coords:
                base[k,n*r+c]=C[index[k],index[missing]]
    return base


def obj(theta,base,target):
    v=base.copy()
    for c in range(n):
        indices=[n*r+c for r in range(1,n)]
        v[:,indices]*=np.exp(1j*theta[:,c])[:,None]
    G=v.conj().T@v; E=np.abs(G)**2-target
    cost=float(np.sum(E**2)/2)
    W=v@(E*G)
    raw=4*np.imag(np.conj(v)*W)
    grad=np.zeros((n,n))
    for c in range(n):
        grad[:,c]=np.sum(raw[:,[n*r+c for r in range(1,n)]],axis=1)
    for c in range(n): grad[c,c]=0
    return cost,grad,v,G


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--incidence',choices=('parker','weisner'),default='parker')
    p.add_argument('--restarts',type=int,default=20)
    p.add_argument('--steps',type=int,default=2000)
    p.add_argument('--seconds',type=float,default=60)
    p.add_argument('--seed',type=int,default=51511)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0: raise ValueError('positive bounds')
    L,_,target=uniform.make(args.incidence)
    rng=np.random.default_rng(args.seed)
    base=makebase(L,rng)
    theta=rng.uniform(-np.pi,np.pi,size=(n,n))
    direction=rng.normal(size=(n,n)); np.fill_diagonal(direction,0); direction/=np.linalg.norm(direction)
    cost,grad,_,_=obj(theta,base,target); h=1e-5
    numeric=(obj(theta+h*direction,base,target)[0]-obj(theta-h*direction,base,target)[0])/(2*h)
    analytic=float(np.sum(grad*direction))
    print('gradient check',analytic,numeric,'absolute_error',abs(analytic-numeric),flush=True)
    if abs(analytic-numeric)>1e-6: raise AssertionError('gradient mismatch')
    start=time.monotonic(); best=None; runs=[]
    for run in range(args.restarts):
        base=makebase(L,rng); theta=rng.uniform(-np.pi,np.pi,size=(n,n))
        m=np.zeros_like(theta); v=np.zeros_like(theta)
        for step in range(1,args.steps+1):
            cost,g,_,_=obj(theta,base,target)
            m=.9*m+.1*g; v=.999*v+.001*g*g
            rate=.06*max(.15,1-step/args.steps)
            theta-=rate*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8)
            if step==1 or step%50==0 or step==args.steps:
                cost,_,array,G=obj(theta,base,target)
                err=np.abs(np.abs(G)**2-target)
                colmax=max(float(np.max(np.abs(G[np.ix_([n*r+c for r in range(n)],
                                                          [n*r+c for r in range(n)])]-np.eye(n))))
                           for c in range(n))
                metrics={'objective':cost,'max_squared_gram_error':float(np.max(err)),
                         'max_forced_inner_product':float(np.max(np.abs(G[target==0]))),
                         'max_column_gram_error':colmax}
                if best is None or cost<best[0]: best=(cost,array.copy(),run,step,metrics)
                if metrics['max_squared_gram_error']<1e-10:
                    print('NUMERIC_CANDIDATE_REQUIRES_CERTIFICATION',run,step,metrics,flush=True); break
            if time.monotonic()-start>=args.seconds: break
        runs.append({'restart':run,'steps':step,**metrics})
        print('restart',run,'steps',step,'metrics',metrics,flush=True)
        if time.monotonic()-start>=args.seconds: break
    stem=f'frontier-20261028-conference-coupled-{args.incidence}'
    np.save(ROOT/(stem+'-best-v1.npy'),best[1],allow_pickle=False)
    record={'parameters':vars(args),'runs':runs,'best_restart':best[2],'best_step':best[3],
            'best_metrics':best[4],'elapsed_seconds':time.monotonic()-start,
            'source':'exact GF9 conference block; independent random per-column labels/phases',
            'caveat':'floating point fixed-L fixed-conference-orbit heuristic, not a proof or certified witness'}
    (ROOT/(stem+'-result-v1.json')).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('best',best[2],best[3],best[4],flush=True)
    print('wrote',stem+'-{best,result}-v1',flush=True)


if __name__=='__main__':main()
