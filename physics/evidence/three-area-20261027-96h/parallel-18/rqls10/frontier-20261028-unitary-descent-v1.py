#!/usr/bin/env python3
"""Search actual vectors on product of row-unitary manifolds.

Uses Weisner Fig.1's fixed transversal incidence. The row constraints are
maintained by polar retraction; column/transversal constraints are optimized.
This floating point heuristic does not certify any solution or no-go.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('adam',HERE/'frontier-20261028-coupled-adam-v1.py')
adam=importlib.util.module_from_spec(spec)
spec.loader.exec_module(adam)
base=adam.base
N=10
ROWS=base.BLOCKS[:N]


def row_retract(v):
    w=np.empty_like(v)
    for block in ROWS:
        idx=list(block)
        w[:,idx]=base.polar(v[:,idx])
    return w


def tangent_gradient(v,grad):
    result=np.empty_like(grad)
    for block in ROWS:
        idx=list(block)
        b=v[:,idx]
        g=grad[:,idx]
        s=b.conj().T@g
        result[:,idx]=g-b@((s+s.conj().T)/2)
    return result


def run():
    p=argparse.ArgumentParser()
    p.add_argument('--restarts',type=int,default=4)
    p.add_argument('--steps',type=int,default=5000)
    p.add_argument('--seconds',type=float,default=90)
    p.add_argument('--repel',type=float,default=0.05)
    p.add_argument('--threshold',type=float,default=0.98)
    p.add_argument('--start-seed',type=int,default=301)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0:
        raise ValueError('positive run bounds required')
    start=time.monotonic()
    best=None
    runs=[]
    for seed in range(args.start_seed,args.start_seed+args.restarts):
        if seed==args.start_seed:
            v=np.load(HERE/'frontier-20261028-coupled-adam-best-v1.npy',allow_pickle=False)
        else:
            rng=np.random.default_rng(seed)
            v=rng.normal(size=(N,N*N))+1j*rng.normal(size=(N,N*N))
        v=row_retract(v)
        loss,gradient=adam.objective_gradient(v,args.repel,args.threshold)
        for step in range(1,args.steps+1):
            tangent=tangent_gradient(v,gradient)
            norm2=float(np.real(np.vdot(tangent,tangent)))
            if norm2 < 1e-20:
                reason='stationary_threshold'
                break
            eta=0.25
            accepted=False
            for _ in range(24):
                trial=row_retract(v-eta*tangent)
                newloss,newgrad=adam.objective_gradient(trial,args.repel,args.threshold)
                if newloss <= loss-1e-4*eta*norm2:
                    v,loss,gradient=trial,newloss,newgrad
                    accepted=True
                    break
                eta*=0.5
            if not accepted:
                reason='line_search_stalled'
                break
            if step==1 or step%50==0 or step==args.steps:
                metrics=base.score(v)
                if best is None or metrics['max_block_gram_error']<best[0]:
                    best=(metrics['max_block_gram_error'],v.copy(),seed,step,loss,metrics)
                if metrics['max_block_gram_error']<1e-10 and metrics['max_distinct_pair_overlap']<1-1e-8:
                    print('NUMERIC_CANDIDATE_REQUIRES_INDEPENDENT_CERTIFICATION',seed,step,metrics,flush=True)
                    reason='numeric_candidate'
                    break
            if time.monotonic()-start>=args.seconds:
                reason='time_limit'
                break
        else:
            reason='step_limit'
        result=base.score(v)
        runs.append({'seed':seed,'steps':step,'reason':reason,'loss':loss,**result})
        print('restart',seed,'steps',step,'reason',reason,'loss',loss,'metrics',result,flush=True)
        if time.monotonic()-start>=args.seconds or reason=='numeric_candidate':
            break
    if best is None:
        best=(base.score(v)['max_block_gram_error'],v.copy(),seed,step,loss,base.score(v))
    artifact=HERE/'frontier-20261028-unitary-descent-best-v1.npy'
    np.save(artifact,best[1],allow_pickle=False)
    record={'method':'row-unitary Riemannian gradient and Armijo polar retraction',
            'fixed_incidence':'Weisner 1963 Fig.1 second digit','parameters':vars(args),
            'runs':runs,'elapsed_seconds':time.monotonic()-start,
            'best_seed':best[2],'best_step':best[3],'best_loss':best[4],
            'best_metrics':best[5],'candidate_file':artifact.name,
            'caveat':'floating point heuristic; not exhaustive or a rigorous certificate'}
    output=HERE/'frontier-20261028-unitary-descent-result-v1.json'
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('best',best[2],best[3],best[4],best[5],flush=True)
    print('wrote',output.name,artifact.name,flush=True)


if __name__=='__main__':
    run()
