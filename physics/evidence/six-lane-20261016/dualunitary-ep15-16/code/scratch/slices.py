import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
rng=np.random.default_rng(31)
def X_of(U):
    T=U.reshape(3,3,3,3) # T[c,d,a,b] = U[(c,d),(a,b)]
    psi=T.transpose(2,3,0,1)  # psi[a,b,c,d]*3
    return [[psi[a,:,:,d] for d in range(3)] for a in range(3)]  # X_ad[b,c]
def show(U,label):
    X=X_of(U)
    rk=[[int((np.linalg.svd(X[a][d],compute_uv=False)>1e-8).sum()) for d in range(3)] for a in range(3)]
    sv=[[np.round(np.linalg.svd(X[a][d],compute_uv=False),3).tolist() for d in range(3)] for a in range(3)]
    print(label,'ep',round(nc.ep(U),4),'ranks',rk)
    for a in range(3): print('   ',sv[a])
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
show(Us,'U_s'); show(np.array(g.P9(),complex),'P9')
for r in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U); show(U,f'rand{r}')
