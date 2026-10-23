import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
import gates as g
rng=np.random.default_rng(3)
def test(A):
    W,s,Vh=np.linalg.svd(A); rk=int((s>1e-8).sum())
    out={}
    for side,K in (('right',Vh[rk:].conj().T),('left',W[:,rk:])):
        Pi=K@K.conj().T  # projector on C^3 (x) C^3
        T=Pi.reshape(3,3,3,3)
        trB=np.einsum('ajbj->ab',T); trA=np.einsum('jajb->ab',T)
        sv=[]
        for _ in range(4):
            w=K@(rng.standard_normal(K.shape[1])+1j*rng.standard_normal(K.shape[1])); w/=np.linalg.norm(w)
            sv.append(np.round(np.linalg.svd(w.reshape(3,3),compute_uv=False),4).tolist())
        out[side]=dict(rank=rk, trB_eigs=np.round(np.linalg.eigvalsh(trB),4).tolist(), trA_eigs=np.round(np.linalg.eigvalsh(trA),4).tolist(), schmidt=sv)
    return out
S=np.array(g.swap(),complex); U0=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
print('U_s', test(nc.G(U0)))
for r in range(5):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    print(r, round(nc.ep(U),4), test(nc.G(U)))
