import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
sys.path.insert(0,'.')
from ascent import gn_project
import gates as g
rng=np.random.default_rng(3)
def kinfo(A, side):
    W,s,Vh=np.linalg.svd(A); rk=int((s>1e-8).sum())
    if side=='right': K=Vh[rk:].conj().T
    else: K=W[:,rk:]
    Ms=[K[:,i].reshape(3,3) for i in range(K.shape[1])]
    # common right null vector: stack vertically -> (3m x 3) rank<3
    st=np.vstack(Ms); r1=np.linalg.matrix_rank(st,1e-8)
    st2=np.hstack(Ms); r2=np.linalg.matrix_rank(st2,1e-8)
    # skew-type test: exists P,Q with P M Q skew for all M? test via: for skew space, the map is 'rank exactly 2 generically'
    rks=[np.linalg.matrix_rank(sum((rng.standard_normal()+1j*rng.standard_normal())*M for M in Ms),1e-8) for _ in range(3)]
    return dict(rank=rk, kdim=len(Ms), vstack_rank=r1, hstack_rank=r2, generic_rank=rks)
S=np.array(g.swap(),complex); U0=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
print('U_s', kinfo(nc.G(U0),'right'), kinfo(nc.G(U0),'left'))
for r in range(8):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    print(r, round(nc.ep(U),4), kinfo(nc.G(U),'right'), kinfo(nc.G(U),'left'))
