import sys; sys.path.insert(0,"."); import numpy as np
exec(open('omega_system.py').read().split("N0=np.diag")[0])
rng=np.random.default_rng(11)
def S0(N):
    # basis of S = {Y in (M2)^3 : sum_d Y_d N_d^dag = 0, sum_d N_d^dag Y_d = 0}, complex-linear
    cols=[]
    for k in range(3):
        for idx in range(4):
            Y=[np.zeros((2,2),complex) for _ in range(3)]; Y[k].flat[idx]=1
            r1=sum(Y[d]@N[d].conj().T for d in range(3)); r2=sum(N[d].conj().T@Y[d] for d in range(3))
            cols.append(np.concatenate([r1.ravel(),r2.ravel()]))
    L=np.array(cols).T   # 8 x 12
    u,s,vh=np.linalg.svd(L); r=int((s>1e-10).sum()); null=vh[r:].conj().T  # 12 x (12-r)
    Y0=null[:4,:]   # first block coords
    return r, null.shape[1], np.linalg.matrix_rank(Y0,1e-10), Y0
for trial in range(3):
    N0=rng.standard_normal((2,2))+1j*rng.standard_normal((2,2)); N0=0.8*N0/np.linalg.norm(N0,2)
    K,e=unital_completion(N0,trial+10); N=[N0,K[0],K[1]]
    r,dimS,dimS0,Y0=S0(N)
    A=np.array([m.ravel() for m in N]).T
    # is span(Y0) inside span(A)?
    PA=A@np.linalg.pinv(A); inside=np.linalg.norm(Y0-PA@Y0)
    print('rank conds',r,'dim S',dimS,'dim S0',dimS0,'dist of S0 from A',round(inside,10),'dim A',np.linalg.matrix_rank(A,1e-10))
