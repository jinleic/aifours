#!/usr/bin/env python3
"""Bounded float search: arbitrary-phase circulant H and H∘F10."""
from pathlib import Path
import json,time,numpy as np
n=10;coord=(np.arange(n)[:,None]-np.arange(n)[None,:])%n
F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n);I=np.eye(n)
def obj(theta):
    H=np.exp(1j*theta[coord])/np.sqrt(n);J=H*F
    G=H.conj().T@H-I;Q=J.conj().T@J-I
    loss=float(np.sum(np.abs(G)**2)+np.sum(np.abs(Q)**2))
    A=np.imag(np.conj(H)*(4*H@G+4*np.conj(F)*(J@Q)))
    grad=np.bincount(coord.ravel(),weights=A.ravel(),minlength=n);grad[0]=0
    return loss,grad,H,G,Q
rng=np.random.default_rng(80287);theta=rng.uniform(-np.pi,np.pi,n);theta[0]=0
v=rng.normal(size=n);v[0]=0;v/=np.linalg.norm(v);eps=1e-6
f,g,_,_,_=obj(theta);fd=(obj(theta+eps*v)[0]-obj(theta-eps*v)[0])/(2*eps)
assert abs(np.dot(g,v)-fd)<1e-6
print('finite-difference gradient error',abs(np.dot(g,v)-fd),flush=True)
start=time.monotonic();best=None;results=[]
for run in range(200):
    th=rng.uniform(-np.pi,np.pi,n);th[0]=0;m=np.zeros(n);v=np.zeros(n)
    for step in range(1,4001):
        loss,g,H,G,Q=obj(th);m=.9*m+.1*g;v=.999*v+.001*g*g
        th-=.035*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8);th[0]=0
        if step%100==0 or step==1:
            loss,g,H,G,Q=obj(th)
            if best is None or loss<best[0]:best=(loss,th.copy(),run,step,float(np.max(np.abs(G))),float(np.max(np.abs(Q))))
            if max(np.max(np.abs(G)),np.max(np.abs(Q)))<1e-10:
                print('FLOAT_PAIR_REQUIRES_EXACT_VECTOR_VERIFICATION',run,step,loss,th.tolist(),flush=True);break
        if time.monotonic()-start>=75:break
    results.append({'run':run,'steps':step,'loss':loss})
    if run%10==0:print('run',run,'loss',loss,'best',best[0],flush=True)
    if time.monotonic()-start>=75:break
p=Path(__file__).resolve().parent
out={'scope':'bounded floating arbitrary-phase circulant H, not exact proof or no-go',
     'seed':80287,'elapsed':time.monotonic()-start,'runs':results,'best_loss':best[0],
     'best_theta':best[1].tolist(),'best_run':best[2],'best_step':best[3],
     'max_H_error':best[4],'max_HF_error':best[5]}
(p/'frontier-20261028-circulant-hadamard-pair-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best[0],best[4],best[5],flush=True)
