import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
from collections import Counter
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]; exec(src)
rng=np.random.default_rng(321)
def rk(vs,tol=1e-8): return int((np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)>tol).sum())
def info(U1):
    phi=U1.reshape(3,3,3,3).transpose(2,3,0,1)
    N=[phi[0,1:,1:,d] for d in range(3)]; Q=[phi[a,1:,1:,0] for a in range(3)]
    R=[phi[1:,0,c,1:] for c in range(3)]; T=[phi[1:,b,0,1:] for b in range(3)]
    M=phi.transpose(0,3,1,2).reshape(9,9); rM=int((np.linalg.svd(M,compute_uv=False)>1e-7).sum())
    return (rk(N),rk(Q),rk(R),rk(T), round(np.linalg.norm(N[0],2),3)>0.9999, round(np.linalg.norm(R[0],2),3)>0.9999, np.linalg.norm(N[0])<1e-9, np.linalg.norm(R[0])<1e-9, rk([N[1],N[2],Q[1],Q[2]]), rk([R[1],R[2],T[1],T[2]]), rM)
pts=[]
while len(pts)<6:
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    rk_=int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum())
    if rk_ in (4,) : pts.append((U,rk_))
S=np.array(g.swap(),complex)
for t in range(2):
    C=np.zeros((9,9),complex)
    for a in range(3): C[3*a:3*a+3,3*a:3*a+3]=nc.haar(3,rng)
    pts.append((S@C,3))
for t in range(2):
    D=np.diag(np.exp(2j*np.pi*rng.random(9))); pts.append((S@D,'S*diag'))
print("key: (dimA,dimB,dimC,dimD, ||N0||op=1, ||R0||op=1, N0=0, R0=0, rP, rB, rankM)")
for U,lab in pts:
    nfs=normal_forms(U,tries=120)
    c=Counter(info(U1) for U1,s1 in nfs if s1<1e-11)
    print('stratum',lab,'#nf',len(nfs))
    for k,v in c.most_common(10): print('   ',v,k)
