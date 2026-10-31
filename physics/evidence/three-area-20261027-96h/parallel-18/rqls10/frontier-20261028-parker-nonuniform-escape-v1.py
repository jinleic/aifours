#!/usr/bin/env python3
"""Bounded nonuniform actual-vector search near and away from Parker13.

All30 original blocks share the same vectors; near-parallel penalty only
steers this heuristic and is not a WLOG assumption or exact certification.
"""
import argparse
import json
from pathlib import Path
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
source=json.loads((ROOT/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']
L=source['labels']; den=source['denominator']; n=10
V0=np.array(source['array'],dtype=float).reshape(100,10).T.astype(complex)/den
assert V0.shape==(10,100)
BLOCKS=[tuple(10*r+c for c in range(n)) for r in range(n)]
BLOCKS += [tuple(10*r+c for r in range(n)) for c in range(n)]
BLOCKS += [tuple(10*r+c for r in range(n) for c in range(n) if L[r][c]==t) for t in range(n)]
assert len(BLOCKS)==30 and all(len(b)==n for b in BLOCKS)


def objective(v,penalty,threshold):
    g=np.zeros_like(v); loss=0.0
    for block in BLOCKS:
        idx=list(block); b=v[:,idx]; e=b.conj().T@b-np.eye(n)
        loss+=float(np.sum(np.abs(e)**2)); g[:,idx]+=4*b@e
    gram=v.conj().T@v
    excess=np.maximum(np.abs(gram)**2-threshold**2,0)
    np.fill_diagonal(excess,0)
    loss+=float(penalty*np.sum(excess**2)/2)
    g+=4*penalty*v@(excess*gram)
    return loss,g


def score(v):
    gram=v.conj().T@v
    err=max(float(np.max(np.abs(gram[np.ix_(b,b)]-np.eye(n)))) for b in BLOCKS)
    off=np.abs(gram.copy());np.fill_diagonal(off,0)
    return {'max_block_gram_error':err,'max_norm_error':float(np.max(np.abs(np.diag(gram)-1))),
            'max_distinct_overlap':float(np.max(off)),
            'near_parallel_pairs':int(np.count_nonzero(np.triu(off>=1-1e-8,1)))}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--restarts',type=int,default=8)
    p.add_argument('--steps',type=int,default=6000)
    p.add_argument('--seconds',type=float,default=60)
    p.add_argument('--seed',type=int,default=71421)
    p.add_argument('--penalty',type=float,default=0.4)
    p.add_argument('--threshold',type=float,default=0.97)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0:raise ValueError('positive bounds required')
    rng=np.random.default_rng(args.seed)
    base=V0+0.2*(rng.normal(size=V0.shape)+1j*rng.normal(size=V0.shape))
    direction=rng.normal(size=V0.shape)+1j*rng.normal(size=V0.shape);direction/=np.linalg.norm(direction)
    loss,g=objective(base,args.penalty,args.threshold);h=1e-5
    d=(objective(base+h*direction,args.penalty,args.threshold)[0]-objective(base-h*direction,args.penalty,args.threshold)[0])/(2*h)
    analytic=float(np.real(np.vdot(g,direction)))
    print('gradient check analytic',analytic,'central',d,'error',abs(analytic-d),flush=True)
    if abs(analytic-d)>1e-5:raise AssertionError('gradient mismatch')
    start=time.monotonic();runs=[];best=None
    widths=(0.02,0.05,0.1,0.2,0.4,0.8,1.2,2.0)
    for run in range(args.restarts):
        sigma=widths[run%len(widths)]
        v=V0+sigma*(rng.normal(size=V0.shape)+1j*rng.normal(size=V0.shape))
        v/=np.linalg.norm(v,axis=0)
        m=np.zeros_like(v);h2=np.zeros(v.shape)
        for step in range(1,args.steps+1):
            loss,g=objective(v,args.penalty,args.threshold)
            m=.9*m+.1*g;h2=.999*h2+.001*np.abs(g)**2
            rate=.025*max(.08,1-step/args.steps)
            v-=rate*(m/(1-.9**step))/(np.sqrt(h2/(1-.999**step))+1e-8)
            v/=np.linalg.norm(v,axis=0)
            if step==1 or step%100==0 or step==args.steps:
                metrics=score(v)
                score_value=metrics['max_block_gram_error']+max(0,metrics['max_distinct_overlap']-.999)
                if best is None or score_value<best[0]:best=(score_value,v.copy(),run,step,sigma,metrics)
                if metrics['max_block_gram_error']<1e-10 and metrics['max_distinct_overlap']<1-1e-8:
                    print('NUMERIC_CANDIDATE_REQUIRES_CERTIFICATION',run,step,metrics,flush=True);break
            if time.monotonic()-start>=args.seconds:break
        metrics=score(v);runs.append({'restart':run,'steps':step,'sigma':sigma,'last_preupdate_loss':loss,**metrics})
        print('restart',run,'sigma',sigma,'steps',step,'metrics',metrics,flush=True)
        if time.monotonic()-start>=args.seconds:break
    stem='frontier-20261028-parker-nonuniform-escape'
    np.save(ROOT/(stem+'-best-v1.npy'),best[1],allow_pickle=False)
    result={'parameters':vars(args),'runs':runs,'best_restart':best[2],'best_step':best[3],
            'best_sigma':best[4],'best_metrics':best[5],'elapsed_seconds':time.monotonic()-start,
            'incidence':'Parker13 certificate labels',
            'caveat':'floating point nonuniform heuristic, no exact certificate or global no-go'}
    (ROOT/(stem+'-result-v1.json')).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('best',best[2],best[3],best[4],best[5],flush=True)
    print('wrote',stem+'-{best,result}-v1',flush=True)


if __name__=='__main__':main()
