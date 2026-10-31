#!/usr/bin/env python3
"""Turn numerical range/rank intersections into exact Gaussian-rational atoms.

Every atom has exact row-relation certificates. The nonnegative fit uses
floating arithmetic only and is NOT a decomposition until weights are certified.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import runpy
import numpy as np


HERE=Path(__file__).parent
exact=runpy.run_path(str(HERE/'frontier-20261028-grid-generic-gaussian-atoms.py'))
num=runpy.run_path(str(HERE/'frontier-20261028-grid-generic-numerical-exploration.py'))
atom=exact['atom']; source_matrix=num['source_matrix']; feature=num['feature']
Z=(F(0),F(0)); O=(F(1),F(0)); SEED=301028; N=768; DENOM=32
OUT=HERE/'frontier-20261028-grid-rationalized-atoms-run-v1.json'


def rat(x):
    return (F(float(x.real)).limit_denominator(DENOM),
            F(float(x.imag)).limit_denominator(DENOM))


def main():
    K=np.array([[1,0,0,.25,0],[0,1,0,.25,0],[0,0,1,.25,0],
                [0,0,0,.25,1]],dtype=np.complex128)
    T=np.column_stack([(source_matrix(np.eye(9)[j])@K.T).reshape(16) for j in range(9)])
    Q,_=np.linalg.qr(T);pinv=np.linalg.pinv(T)
    if np.linalg.matrix_rank(T)!=9:raise AssertionError('range rank')
    rng=np.random.default_rng(SEED)
    exact_atoms=[];params=[];singular=[];rejected=0
    for j in range(1,9):
        exact_atoms.append(tuple(O if k==j else Z for k in range(9)));params.append(('basis',j))
    for _ in range(N):
        xi=rng.normal(size=9)+1j*rng.normal(size=9)
        M=(T@xi).reshape(4,4);M/=np.linalg.norm(M)
        for step in range(500):
            U,s,Vh=np.linalg.svd(M,full_matrices=False)
            low=(U[:,:2]*s[:2])@Vh[:2,:]
            M=(Q@(Q.conj().T@low.reshape(16))).reshape(4,4)
            norm=np.linalg.norm(M)
            if norm==0:break
            M/=norm
            if step%10==9 and np.linalg.svd(M,compute_uv=False)[2]<1e-9:break
        vals=np.linalg.svd(M,compute_uv=False)
        if vals[2]>=1e-8:rejected+=1;continue
        xi=pinv@M.reshape(16)
        if abs(xi[0])<.01:rejected+=1;continue
        xi/=xi[0]; raw=(source_matrix(xi)@K.T)
        ab,_,_,_=np.linalg.lstsq(raw[:2,:].T,raw[2,:],rcond=None)
        vals=(rat(ab[0]),rat(ab[1]),rat(xi[1]),rat(xi[5]))
        if vals[0]==Z or vals[3]==Z:rejected+=1;continue
        exact_atoms.append(atom(*vals));params.append(vals)
        singular.append(float(np.linalg.svd(raw,compute_uv=False)[2]))
    P=[];norms=[]
    for xi in exact_atoms:
        x=np.array([complex(float(a),float(b)) for a,b in xi]);n2=np.vdot(x,x).real
        norms.append(n2);x/=np.sqrt(n2)
        P.append(feature(np.outer(x,x.conj())))
    P=np.column_stack(P);target=feature(np.diag([1,1,3,1,3,3,3,3,3]))
    L=np.linalg.norm(P,ord=2)**2
    x=np.zeros(len(exact_atoms));y=x.copy();t=1.0
    for _ in range(12000):
        new=np.maximum(0,y-(P.T@(P@y-target))/L)
        tn=(1+np.sqrt(1+4*t*t))/2;y=new+((t-1)/tn)*(new-x);x=new;t=tn
    residual=P@x-target; active=[]
    for j,w in enumerate(x):
        if w>1e-10:
            active.append({'parameters':str(params[j]),
                           'atom':[[str(a),str(b)] for a,b in exact_atoms[j]],
                           'coefficient_float':float(w/norms[j]),
                           'normalized_weight_float':float(w)})
    result={'seed':SEED,'requested':N,'rational_denominator_cap':DENOM,
            'exact_atoms':len(exact_atoms),'rejected':rejected,
            'numerical_pre_rationalization_max_singular3':max(singular,default=None),
            'fit_iterations':12000,'positive_weights':len(active),
            'float_feature_residual_l2':float(np.linalg.norm(residual)),
            'float_relative_residual':float(np.linalg.norm(residual)/np.linalg.norm(target)),
            'active_atoms':active,'limits':'exact atoms, FLOAT weights; not yet exact decomposition'}
    with open(OUT,'x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='active_atoms'},indent=2))


if __name__=='__main__':main()
