#!/usr/bin/env python3
"""Search a nonuniform Fourier × arbitrary phase-column actual-vector ansatz.

Columns of the QLS are ONBs automatically; rows and all supplied transversal
blocks are optimized on the SAME 100 vectors. Floating results are not proof.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('uniform',ROOT/'frontier-20261028-uniform-physical-search-v1.py')
uniform=importlib.util.module_from_spec(spec);spec.loader.exec_module(uniform)
n=10
F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)


def vectors(theta):
    P=np.exp(1j*theta)
    return (F[:,:,None]*P[:,None,:]/np.sqrt(n)).reshape(n,n*n)


def blocks(L):
    out=[tuple(n*r+c for c in range(n)) for r in range(n)]
    out += [tuple(n*r+c for r in range(n)) for c in range(n)]
    out += [tuple(n*r+c for r in range(n) for c in range(n) if L[r][c]==t) for t in range(n)]
    assert len(out)==30 and all(len(b)==n for b in out)
    return out


def objective(theta,bs,repel,threshold):
    V=vectors(theta); g=np.zeros_like(V); cost=0.
    for block in bs:
        idx=list(block); B=V[:,idx]; E=B.conj().T@B-np.eye(n)
        cost+=float(np.sum(np.abs(E)**2));g[:,idx]+=4*B@E
    gram=V.conj().T@V
    excess=np.maximum(np.abs(gram)**2-threshold**2,0);np.fill_diagonal(excess,0)
    cost+=float(repel*np.sum(excess**2)/2);g+=4*repel*V@(excess*gram)
    dtheta=np.imag(np.conj(V)*g).reshape(n,n,n).sum(axis=1)
    return cost,dtheta,V,gram


def score(V,gram,bs):
    worst=max(float(np.max(np.abs(gram[np.ix_(b,b)]-np.eye(n)))) for b in bs)
    off=np.abs(gram.copy());np.fill_diagonal(off,0)
    return {'max_block_gram_error':worst,'max_distinct_overlap':float(np.max(off)),
            'near_parallel_pairs':int(np.count_nonzero(np.triu(off>=1-1e-8,1)))}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--incidence',choices=('parker','weisner'),default='parker')
    p.add_argument('--restarts',type=int,default=12)
    p.add_argument('--steps',type=int,default=4000)
    p.add_argument('--seconds',type=float,default=60)
    p.add_argument('--seed',type=int,default=9271)
    p.add_argument('--repel',type=float,default=.3)
    p.add_argument('--threshold',type=float,default=.97)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0:raise ValueError('positive bounds required')
    L,_,_=uniform.make(args.incidence);bs=blocks(L)
    rng=np.random.default_rng(args.seed)
    theta=rng.uniform(-np.pi,np.pi,size=(n,n));d=rng.normal(size=(n,n));d/=np.linalg.norm(d)
    loss,g,_,_=objective(theta,bs,args.repel,args.threshold);h=1e-5
    fd=(objective(theta+h*d,bs,args.repel,args.threshold)[0]-objective(theta-h*d,bs,args.repel,args.threshold)[0])/(2*h)
    analytic=float(np.sum(g*d));print('gradient check',analytic,fd,'absolute_error',abs(analytic-fd),flush=True)
    if abs(analytic-fd)>1e-6:raise AssertionError('gradient mismatch')
    start=time.monotonic();best=None;runs=[]
    for run in range(args.restarts):
        theta=rng.uniform(-np.pi,np.pi,size=(n,n));m=np.zeros_like(theta);v=np.zeros_like(theta)
        for step in range(1,args.steps+1):
            loss,g,V,G=objective(theta,bs,args.repel,args.threshold)
            m=.9*m+.1*g;v=.999*v+.001*g*g
            rate=.04*max(.1,1-step/args.steps)
            theta-=rate*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8)
            if step==1 or step%100==0 or step==args.steps:
                loss,_,V,G=objective(theta,bs,args.repel,args.threshold)
                metrics=score(V,G,bs)
                if best is None or loss<best[0]:best=(loss,V.copy(),run,step,metrics)
                if metrics['max_block_gram_error']<1e-10 and metrics['max_distinct_overlap']<1-1e-8:
                    print('NUMERIC_CANDIDATE_REQUIRES_INDEPENDENT_CERTIFICATION',run,step,metrics,flush=True);break
            if time.monotonic()-start>=args.seconds:break
        runs.append({'restart':run,'steps':step,'loss':loss,**metrics})
        print('restart',run,'steps',step,'loss',loss,'metrics',metrics,flush=True)
        if time.monotonic()-start>=args.seconds:break
    stem='frontier-20261028-hadamard-product-'+args.incidence
    np.save(ROOT/(stem+'-best-v1.npy'),best[1],allow_pickle=False)
    rec={'parameters':vars(args),'runs':runs,'best_loss':best[0],'best_restart':best[2],
         'best_step':best[3],'best_metrics':best[4],'elapsed_seconds':time.monotonic()-start,
         'caveat':'floating fixed-L product ansatz; not a complete QLS search or rigorous certificate'}
    (ROOT/(stem+'-result-v1.json')).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print('best',best[2],best[3],best[0],best[4],flush=True)
    print('wrote',stem+'-{best,result}-v1',flush=True)


if __name__=='__main__':main()
