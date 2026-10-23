import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
import normalform as NF
rng=np.random.default_rng(41)
def rk(vs,tol=1e-7):
    A=np.array([v.ravel() for v in vs]); return int((np.linalg.svd(A,compute_uv=False)>tol).sum())
for r in range(6):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    U1=NF.normal_form(U); U1,res,_=gn_project(U1)
    T=U1.reshape(3,3,3,3); psi=T.transpose(2,3,0,1)/3
    K=[1,2]
    n=[psi[0][np.ix_(K,K)][:,:,d] if False else psi[0,1:,1:,d] for d in range(3)]
    q=[psi[a,1:,1:,0] for a in range(3)]
    rr=[psi[1:,0,c,1:] for c in range(3)]   # r_c[a,d]
    t=[psi[1:,b,0,1:] for b in range(3)]    # t_b[a,d]
    chk=lambda L: np.round(np.linalg.norm(sum(9*x@x.conj().T for x in L)-np.eye(2)),6)
    print(r,'ep',round(nc.ep(U),4),'unital checks',chk(n),chk(q),chk(rr),chk(t),
          '| dim A',rk(n),'dim B',rk(q),'dim A+B',rk(n+q),'rank N',rk(n[1:]+q[1:]),
          '| dim C',rk(rr),'dim D',rk(t),'dim C+D',rk(rr+t),'rank L',rk(rr[1:]+t[1:]),
          '| |n0|',round(np.linalg.norm(n[0]),4),'|r0|',round(np.linalg.norm(rr[0]),4))
