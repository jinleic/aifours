#!/usr/bin/env python3
"""Bounded float search for H and H∘F10 Hadamard; never a proof or exact witness."""
import json,time
from pathlib import Path
import numpy as np
n=10
F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)
I=np.eye(n);mask=np.ones((n,n));mask[0,:]=mask[:,0]=0

def evaluate(theta):
    H=np.exp(1j*theta)/np.sqrt(n);J=H*F
    G=H.conj().T@H-I;Q=J.conj().T@J-I
    loss=float(np.sum(np.abs(G)**2)+np.sum(np.abs(Q)**2))
    grad=np.imag(np.conj(H)*(4*H@G+4*np.conj(F)*(J@Q)))*mask
    return loss,grad,H,G,Q

def detail(H,G,Q):
    V=(F[:,:,None]*H[:,None,:]).reshape(10,100)
    P=np.abs(V.conj().T@V);np.fill_diagonal(P,0)
    return {'max_H_error':float(np.max(np.abs(G))),
            'max_HF_error':float(np.max(np.abs(Q))),
            'max_pair_overlap':float(np.max(P)),
            'near_parallel_pairs':int(np.count_nonzero(np.triu(P>1-1e-8,1)))}

rng=np.random.default_rng(23847)
th=rng.uniform(-np.pi,np.pi,(n,n))*mask
d=rng.normal(size=(n,n))*mask;d/=np.linalg.norm(d)
f,g,_,_,_=evaluate(th);eps=1e-6
fd=(evaluate(th+eps*d)[0]-evaluate(th-eps*d)[0])/(2*eps)
print('gradient analytic',float((g*d).sum()),'finite_difference',fd,flush=True)
assert abs((g*d).sum()-fd)<1e-6
best=None;runs=[];start=time.monotonic()
for run in range(24):
    th=rng.uniform(-np.pi,np.pi,(n,n))*mask;m=np.zeros_like(th);v=np.zeros_like(th)
    for step in range(1,3501):
        f,g,H,G,Q=evaluate(th);m=.9*m+.1*g;v=.999*v+.001*g*g
        th-=.035*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8)*mask
        if step%200==0 or step==1:
            f,g,H,G,Q=evaluate(th);met=detail(H,G,Q)
            if best is None or f<best[0]:best=(f,H.copy(),run,step,met)
            if met['max_H_error']<1e-10 and met['max_HF_error']<1e-10 and met['max_pair_overlap']<1-1e-8:
                print('NUMERIC_CANDIDATE_REQUIRES_EXACT_CHECK',run,step,met,flush=True);break
        if time.monotonic()-start>90:break
    runs.append({'restart':run,'steps':step,'loss':f,**met})
    print('run',run,'step',step,'loss',f,'metrics',met,flush=True)
    if time.monotonic()-start>90:break
p=Path(__file__).resolve().parent
np.save(p/'frontier-20261028-general-hadamard-pair-best-v1.npy',best[1],allow_pickle=False)
out={'seed':23847,'requested_restarts':24,'step_limit':3500,'wall_limit_seconds':90,
     'elapsed':time.monotonic()-start,'runs':runs,'best_loss':best[0],
     'best_run':best[2],'best_step':best[3],'best_metrics':best[4],
     'scope':'floating one-transversal Fourier product only; not exact or no-go'}
(p/'frontier-20261028-general-hadamard-pair-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best[0],best[4],flush=True)
