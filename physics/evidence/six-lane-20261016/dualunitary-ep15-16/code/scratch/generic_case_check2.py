import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]; exec(src)
rng=np.random.default_rng(124)
def rk(vs,tol=1e-9): return int((np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)>tol).sum())
def right_twist(mats):
    # find w (2x2) with M w symmetric for all M; return unitary w
    rows=[]
    for M in mats:
        r=np.zeros(4,complex)
        # (M w)_{01} - (M w)_{10} = sum_k M[0,k] w[k,1] - M[1,k] w[k,0]
        for k in range(2):
            r[2*k+1]+=M[0,k]; r[2*k+0]-=M[1,k]
        rows.append(r)
    A=np.array(rows); u,s,vh=np.linalg.svd(A); w=vh[-1].conj().reshape(2,2)
    return w/np.sqrt(abs(np.linalg.det(w))), s
def sectors(U1):
    phi=U1.reshape(3,3,3,3).transpose(2,3,0,1)
    N=[phi[0,1:,1:,d] for d in range(3)]; Q=[phi[a,1:,1:,0] for a in range(3)]
    R=[phi[1:,0,c,1:] for c in range(3)]; T=[phi[1:,b,0,1:] for b in range(3)]
    return phi,N,Q,R,T
for trial in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    for U1,s1 in normal_forms(U,tries=60)[:3]:
        phi,N,Q,R,T=sectors(U1)
        w,sw=right_twist(N); wp,swp=right_twist(R)
        G3=np.eye(3,dtype=complex); G3[1:,1:]=w     # acts on output factor 1 (index c)
        G4=np.eye(3,dtype=complex); G4[1:,1:]=wp    # acts on output factor 2 (index d)
        U2=np.kron(G3.T,G4.T)@U1
        phi,N,Q,R,T=sectors(U2)
        symN=max(np.linalg.norm(x-x.T) for x in N+Q); symR=max(np.linalg.norm(x-x.T) for x in R+T)
        W=[]
        for S in (R,T):
            for a in range(2):
                W.append(np.array([[S[c+1][a,d] for d in range(2)] for c in range(2)]))
        print(f"twist sv N {np.round(sw,4)} R {np.round(swp,4)} | gauge: N,Q sym err {symN:.1e}, R,T sym err {symR:.1e} | F1 {rk(W)} rB {rk([R[1],R[2],T[1],T[2]])} rP {rk([N[1],N[2],Q[1],Q[2]])} | dual res {nc.dual_residual(U2):.1e}")
