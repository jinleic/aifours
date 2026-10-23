import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]; exec(src)
rng=np.random.default_rng(123)
def proj_resid(vs, basis):
    B=np.array([b.ravel() for b in basis]).T; P=B@np.linalg.pinv(B)
    return max(np.linalg.norm(v.ravel()-P@v.ravel()) for v in vs)
def rk(vs,tol=1e-9): return int((np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)>tol).sum())
for trial in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    nfs=normal_forms(U,tries=80)
    for U1,s1 in nfs[:4]:
        phi=U1.reshape(3,3,3,3).transpose(2,3,0,1)   # phi[a,b,c,d] = 3 psi
        K=[1,2]
        N=[phi[0,1:,1:,d] for d in range(3)]; Q=[phi[a,1:,1:,0] for a in range(3)]
        Om={(a,d):phi[a,1:,1:,d] for a in K for d in K}
        R=[phi[1:,0,c,1:] for c in range(3)]; T=[phi[1:,b,0,1:] for b in range(3)]
        Omp={(b,c):phi[1:,b,c,1:] for b in K for c in K}
        dA,dC=rk(N),rk(R)
        n0=np.linalg.norm(N[0],2)
        lemN1=proj_resid([Q[1],Q[2]]+list(Om.values()),N); lemN1p=proj_resid([T[1],T[2]]+list(Omp.values()),R)
        Nmat=np.hstack([N[1],N[2]])   # 2x4 : [b,(d,c)]? arrange as [b,(c,d)]
        Nbcd=np.zeros((2,4),complex)
        for b in range(2):
            for c in range(2):
                for d in range(2): Nbcd[b,2*c+d]=N[d+1][b,c]
        rkN=int((np.linalg.svd(Nbcd,compute_uv=False)>1e-9).sum())
        W=[]
        for S in (R,T):
            for a in range(2):
                W.append(np.array([[S[c+1][a,d] for d in range(2)] for c in range(2)]))
        F1=rk(W); rB=rk([R[1],R[2],T[1],T[2]]); rP=rk([N[1],N[2],Q[1],Q[2]])
        M=phi.transpose(0,3,1,2).reshape(9,9); rM=int((np.linalg.svd(M,compute_uv=False)>1e-8).sum())
        print(f"dimA {dA} dimC {dC} ||N0||op {n0:.3f} | N1: Q,Om in A resid {lemN1:.1e} | N1': T,Om' in C resid {lemN1p:.1e} | rank Nbcd {rkN} F1 {F1} rB {rB} rP {rP} rankM {rM}")
