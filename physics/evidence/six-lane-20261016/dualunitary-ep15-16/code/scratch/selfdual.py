import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
import gates as g
rng=np.random.default_rng(4)
# (a) tangent dimension of SD = {U unitary, U^R = U} at U_s
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
print('Us^R==Us', np.allclose(nc.R(Us),Us))
def sd_dim(U):
    cols=[]
    for X in nc.BASIS:
        A=X@U.conj().T+U@X.conj().T
        B=nc.R(X)-X
        cols.append(np.concatenate([nc.herm_vec(A), B.real.ravel(), B.imag.ravel()]))
    J=np.array(cols).T
    s=np.linalg.svd(J,compute_uv=False); r=int((s>1e-9*s[0]).sum())
    return 162-r
print('tangent dim of SD at U_s:', sd_dim(Us))
# (b) random MR point -> find u1,u4 mapping kernel to Lambda^2 and test self-duality
def to_selfdual(U):
    A=nc.G(U)   # columns indexed (a,d) parties 1,4 ; rows (c,b)
    W,s,Vh=np.linalg.svd(A); K=Vh[6:].conj().T  # 9x3 kernel in C^3_a (x) C^3_d
    # kernel vectors as 3x3 matrices M_k[a,d]; for (u x v)Lambda^2: M = u E v^T with E antisymmetric
    # find u,v: the space {u E v^T}. Use: for skew space, M_k v^{-T}... solve via generic approach:
    # every M in K has rank 2; kernel vector of M (right) ranges over v^{-T}-image... use optimisation-free method:
    Ms=[K[:,k].reshape(3,3) for k in range(3)]
    # right null vectors n_k of M_k: for M = u E v^T, null(M) = v^{-T} null(E). Collect n_k for basis -> matrix N = v^{-T} [e-dual]
    Nr=np.array([np.linalg.svd(M)[2][-1].conj() for M in Ms]).T
    Nl=np.array([np.linalg.svd(M)[0][:,-1].conj() for M in Ms]).T
    return Ms, Nr, Nl
for r in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    Ms,Nr,Nl=to_selfdual(U)
    print(r,'ep',round(nc.ep(U),4),'Nr singular values',np.round(np.linalg.svd(Nr,compute_uv=False),4),'Nl',np.round(np.linalg.svd(Nl,compute_uv=False),4))
