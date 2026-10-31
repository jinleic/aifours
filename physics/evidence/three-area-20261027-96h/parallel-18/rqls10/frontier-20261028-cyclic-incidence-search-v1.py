#!/usr/bin/env python3
"""Bounded coupled-vector search with cyclic resolution; no uniformity assumption."""
from pathlib import Path
import json,time,numpy as np
n=10;N=100;L=[[(r-c)%n for c in range(n)] for r in range(n)]
blocks=[tuple(10*r+c for c in range(n)) for r in range(n)]
blocks += [tuple(10*r+c for r in range(n)) for c in range(n)]
blocks += [tuple(10*r+c for r in range(n) for c in range(n) if L[r][c]==t) for t in range(n)]
assert all(len(x)==10 for x in blocks)
mask=np.zeros((n,N),bool)
for r in range(1,n):
 for c in range(n):
  mask[:,10*r+c]=True;mask[c,10*r+c]=False;mask[(c-r)%n,10*r+c]=False
assert all(mask[:,i].sum()==8 for i in range(10,100))
def project(v):
    v[~mask]=0;v[:,:10]=np.eye(n)
    v[:,10:]/=np.linalg.norm(v[:,10:],axis=0)
    return v
def objective(v,penalty=.3,threshold=.97):
    g=np.zeros_like(v);loss=0.
    for bb in blocks:
        idx=list(bb);B=v[:,idx];e=B.conj().T@B-np.eye(n)
        loss+=float(np.sum(np.abs(e)**2));g[:,idx]+=4*B@e
    gram=v.conj().T@v;ex=np.maximum(np.abs(gram)**2-threshold**2,0.);np.fill_diagonal(ex,0)
    loss+=float(penalty*np.sum(ex**2)/2);g+=4*penalty*v@(ex*gram);g[~mask]=0
    return loss,g
def metrics(v):
    G=v.conj().T@v;err=max(float(np.max(np.abs(G[np.ix_(b,b)]-np.eye(n)))) for b in blocks)
    off=np.abs(G.copy());np.fill_diagonal(off,0)
    return {'max_block_gram_error':err,'max_overlap':float(np.max(off)),
            'near_parallel_pairs':int(np.count_nonzero(np.triu(off>1-1e-8,1)))}
rng=np.random.default_rng(193414);start=time.monotonic();best=None;runs=[]
for run in range(30):
    v=project(rng.normal(size=(n,N))+1j*rng.normal(size=(n,N)));m=np.zeros_like(v);h=np.zeros(v.shape)
    for step in range(1,3501):
        loss,g=objective(v);m=.9*m+.1*g;h=.999*h+.001*np.abs(g)**2
        v-=.025*(m/(1-.9**step))/(np.sqrt(h/(1-.999**step))+1e-8);project(v)
        if step%100==0 or step==1:
            met=metrics(v);value=met['max_block_gram_error']+max(0,met['max_overlap']-.999)
            if best is None or value<best[0]:best=(value,v.copy(),run,step,met)
            if met['max_block_gram_error']<1e-10 and met['max_overlap']<1-1e-8:
                print('NUMERIC_CANDIDATE_NEEDS_EXACT_CHECK',run,step,met,flush=True);break
        if time.monotonic()-start>50:break
    runs.append({'run':run,'steps':step,'loss_before_last_update':loss,**met})
    print('run',run,'steps',step,'metrics',met,flush=True)
    if time.monotonic()-start>50:break
p=Path(__file__).resolve().parent
np.save(p/'frontier-20261028-cyclic-incidence-best-v1.npy',best[1],allow_pickle=False)
out={'scope':'nonuniform physical vectors, fixed cyclic Latin L, numeric heuristic only',
     'seed':193414,'elapsed':time.monotonic()-start,'runs':runs,
     'best_run':best[2],'best_step':best[3],'best_metrics':best[4]}
(p/'frontier-20261028-cyclic-incidence-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best[4],flush=True)
