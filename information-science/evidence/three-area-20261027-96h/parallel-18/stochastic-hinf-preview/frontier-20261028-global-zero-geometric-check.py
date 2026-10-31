#!/usr/bin/env python3
"""Bounded numerical diagnostics for a written stochastic geometric zero test."""
import json
import numpy as np

TOL=1e-10


def orth(A):
    if not A.size:return np.zeros((A.shape[0],0))
    U,s,_=np.linalg.svd(A,full_matrices=False)
    rank=int(np.sum(s>TOL*max(A.shape)*max(1.0,s[0] if len(s) else 0)))
    return U[:,:rank]


def null(A):
    rows,cols=A.shape
    if cols==0:return np.zeros((0,0))
    if rows==0:return np.eye(cols)
    _,s,Vh=np.linalg.svd(A,full_matrices=True)
    rank=int(np.sum(s>TOL*max(A.shape)*max(1.0,s[0] if len(s) else 0)))
    return Vh[rank:,:].T


def solve(A,A0,B,B0,C,D0,D1):
    n=A.shape[0]; V=np.eye(n); dims=[n]
    for _ in range(n+1):
        R=null(V.T)
        Cj=np.vstack((R.T@A,R.T@A0,D0))
        Dj=np.vstack((R.T@B,R.T@B0,D1))
        residual=(np.eye(Dj.shape[0])-Dj@np.linalg.pinv(Dj,rcond=TOL))@Cj@V
        Vnext=orth(V@null(residual)); dims.append(Vnext.shape[1])
        if Vnext.shape[1]==V.shape[1]:V=Vnext; break
        V=Vnext
    else:raise RuntimeError('subspace iteration did not stabilize')
    R=null(V.T)
    Dstack=np.vstack((R.T@B,R.T@B0,D1))
    Cstack=np.vstack((R.T@A,R.T@A0,D0))
    Fstack=np.vstack((R.T@C,np.zeros((R.shape[1],C.shape[1])),np.zeros((D0.shape[0],C.shape[1]))))
    pseudo=np.linalg.pinv(Dstack,rcond=TOL)
    K=-pseudo@Cstack@V@V.T
    L=-pseudo@Fstack
    fit=np.linalg.norm(Dstack@L+Fstack)
    projector=np.eye(n)-V@V.T
    checks={'drift_invariance':float(np.linalg.norm(projector@(A+B@K)@V)),
            'diffusion_invariance':float(np.linalg.norm(projector@(A0+B0@K)@V)),
            'output_on_hidden':float(np.linalg.norm((D0+D1@K)@V)),
            'feedthrough':float(np.linalg.norm(D1@L)),
            'forced_drift':float(np.linalg.norm(projector@(B@L+C))),
            'forced_diffusion':float(np.linalg.norm(projector@B0@L))}
    return {'dimensions':dims,'hidden_dimension':V.shape[1],'matching_residual':float(fit),
            'K':K.tolist(),'L':L.tolist(),'residuals':checks}


def arr(x):return np.array(x,dtype=float)


def main():
    hidden=solve(arr([[-1,0],[1,-2]]),arr([[.5,0],[1,1/3]]),arr([[1],[0]]),arr([[0],[1]]),arr([[2],[3]]),arr([[1,0]]),arr([[0]]))
    obstruction=solve(arr([[0]]),arr([[0]]),arr([[1]]),arr([[1]]),arr([[1]]),arr([[1]]),arr([[0]]))
    conversion=solve(arr([[0,1],[0,0]]),arr([[0,0],[0,0]]),arr([[0,0],[1,0]]),arr([[0,0],[0,0]]),arr([[1],[0]]),arr([[1,0]]),arr([[0,1]]))
    print(json.dumps({'hidden_noise_case':hidden,'diffusion_obstruction_case':obstruction,
      'distributed_to_feedback_case':conversion,'tolerance':TOL,
      'limits':'Floating SVD/pseudoinverse diagnostics only. No exact rank, theorem proof or positive-gain decision.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
