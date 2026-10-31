#!/usr/bin/env python3
"""Bounded numerical exploration of one full-support grid projection.

Alternating low-rank/range projections followed by a nonnegative least-squares
fit. Floating results are heuristics only: no PPT/SN/entanglement certificate
or nonexistence conclusion follows from a fit, miss, or finite sample.
"""
import json
import numpy as np


SEED=20261028
NSAMPLES=384
MAXITER=500
TOL=1e-8
FITITER=4000


def source_matrix(t):
    a,b,c,d,e,f,g,i,h=t
    return np.array([[a,b,c,0,h],[d,a,b,0,0],
                     [e,-d,a,f,0],[g,0,i,e,c]],dtype=np.complex128)


def feature(h):
    d=list(h.diagonal().real)
    for i in range(9):
        for j in range(i+1,9): d.extend((h[i,j].real,h[i,j].imag))
    return np.array(d)


def main():
    # Kernel line (-1,-1,-1,4,-1) has support on all five coordinates.
    K=np.array([[1,0,0,0.25,0],[0,1,0,0.25,0],[0,0,1,0.25,0],
                [0,0,0,0.25,1]],dtype=np.complex128)
    basis=[]
    for j in range(9):
        e=np.zeros(9,dtype=np.complex128); e[j]=1
        basis.append((source_matrix(e)@K.T).reshape(16))
    T=np.column_stack(basis)
    Q,_=np.linalg.qr(T)
    if np.linalg.matrix_rank(T)!=9: raise AssertionError('source range not injective')
    pinv=np.linalg.pinv(T)
    rng=np.random.default_rng(SEED)
    atoms=[]; errors=[]; attempts=0
    # The eight non-A source generators are exactly SR<=2 under any local map.
    for j in range(1,9):
        x=np.zeros(9,dtype=np.complex128);x[j]=1
        atoms.append(x);errors.append(0.0)
    for _ in range(NSAMPLES):
        attempts+=1
        x=rng.normal(size=9)+1j*rng.normal(size=9)
        M=(T@x).reshape(4,4); M/=np.linalg.norm(M)
        for it in range(MAXITER):
            U,s,Vh=np.linalg.svd(M,full_matrices=False)
            low=(U[:,:2]*s[:2])@Vh[:2,:]
            M=(Q@(Q.conj().T@low.reshape(16))).reshape(4,4)
            n=np.linalg.norm(M)
            if n==0: break
            M/=n
            if it%10==9:
                s=np.linalg.svd(M,compute_uv=False)
                if s[2]/s[0]<TOL: break
        s=np.linalg.svd(M,compute_uv=False)
        error=float(s[2]/s[0])
        if error<TOL:
            xi=pinv@M.reshape(16)
            xi/=np.linalg.norm(xi)
            if abs(xi[0])>1e-4:
                atoms.append(xi);errors.append(error)
    D=np.diag([1,1,3,1,3,3,3,3,3]).astype(np.complex128)
    target=feature(D)
    P=np.column_stack([feature(np.outer(x,x.conj())) for x in atoms])
    L=np.linalg.norm(P,ord=2)**2
    x=np.zeros(len(atoms)); y=x.copy(); t=1.0
    for _ in range(FITITER):
        new=np.maximum(0,y-(P.T@(P@y-target))/L)
        tn=(1+np.sqrt(1+4*t*t))/2
        y=new+((t-1)/tn)*(new-x)
        x=new;t=tn
    fit=P@x-target
    result={'seed':SEED,'K':K.real.tolist(),'attempts':attempts,
            'range_dimension':9,'accepted_atoms':len(atoms),
            'accepted_nontrivial_atoms':len(atoms)-8,
            'max_accepted_relative_singular3':max(errors),
            'fit_iterations':FITITER,'feature_residual_l2':float(np.linalg.norm(fit)),
            'relative_feature_residual':float(np.linalg.norm(fit)/np.linalg.norm(target)),
            'positive_weights':int(np.count_nonzero(x>1e-7)),
            'limits':'floating heuristic on one local projection and sampled approximate atoms only; no proof of a decomposition, separator, or nonexistence'}
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
