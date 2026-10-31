#!/usr/bin/env python3
"""Bounded numerical scan of actual PPT grid projections.

Approximate sampled-rank and nonnegative fits are heuristics, never a proof of
SN<=2, SN>=3, or nonexistence. Every input is an actual local map of a PPT
source; no mixed-state relaxation is substituted for a physical state.
"""
from pathlib import Path
import json
import runpy
import numpy as np

HELP=runpy.run_path(str(Path(__file__).with_name('frontier-20261028-grid-generic-numerical-exploration.py')))
source_matrix=HELP['source_matrix']; feature=HELP['feature']
CASES=((.25,.25,.25,.25),(1,1,1,1),(.5,2,.5,1),(2,0,2,1),
       (2j,1,1j,1),(5,.5,1j,2),(0,2,0,.1),(1+1j,-1j,2j,-1))


def run_case(theta,seed):
    v0,v1,v2,lam=theta
    K=np.array([[1,0,0,v0,0],[0,1,0,v1,0],[0,0,1,v2,0],
                [0,0,0,lam,1]],dtype=np.complex128)
    T=np.column_stack([(source_matrix(np.eye(9)[j])@K.T).reshape(16) for j in range(9)])
    rank=int(np.linalg.matrix_rank(T))
    if rank!=9:return {'theta':[str(x) for x in theta],'range_rank':rank,'status':'rank-deficient chart not sampled'}
    Q,_=np.linalg.qr(T);pinv=np.linalg.pinv(T);rng=np.random.default_rng(seed)
    atoms=[];errors=[]
    for j in range(1,9):
        x=np.zeros(9,dtype=np.complex128);x[j]=1;atoms.append(x);errors.append(0.)
    for _ in range(160):
        xi=rng.normal(size=9)+1j*rng.normal(size=9)
        M=(T@xi).reshape(4,4);M/=np.linalg.norm(M)
        for it in range(400):
            U,s,Vh=np.linalg.svd(M,full_matrices=False)
            low=(U[:,:2]*s[:2])@Vh[:2,:]
            M=(Q@(Q.conj().T@low.reshape(16))).reshape(4,4)
            norm=np.linalg.norm(M)
            if norm==0:break
            M/=norm
            if it%10==9 and np.linalg.svd(M,compute_uv=False)[2]<1e-8:break
        s=np.linalg.svd(M,compute_uv=False);err=float(s[2]/s[0])
        if err<1e-8:
            xi=pinv@M.reshape(16);xi/=np.linalg.norm(xi)
            if abs(xi[0])>1e-4:atoms.append(xi);errors.append(err)
    target=feature(np.diag([1,1,3,1,3,3,3,3,3]).astype(np.complex128))
    P=np.column_stack([feature(np.outer(x,x.conj())) for x in atoms])
    L=np.linalg.norm(P,ord=2)**2;x=np.zeros(len(atoms));y=x.copy();t=1.
    for _ in range(4000):
        new=np.maximum(0,y-(P.T@(P@y-target))/L)
        tn=(1+np.sqrt(1+4*t*t))/2;y=new+((t-1)/tn)*(new-x);x=new;t=tn
    res=np.linalg.norm(P@x-target)/np.linalg.norm(target)
    return {'theta':[str(x) for x in theta],'range_rank':rank,'approx_sr2_atoms':len(atoms)-8,
            'max_relative_singular3':max(errors),'positive_fit_weights':int(np.sum(x>1e-7)),
            'relative_feature_residual':float(res)}

print(json.dumps({'seed_base':880,'samples_per_case':160,'cases':[run_case(t,880+j) for j,t in enumerate(CASES)],
                  'limits':'finite FLOATING exploratory samples; no SN proof or nonexistence inference'},indent=2))
