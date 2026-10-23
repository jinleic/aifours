import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
rng=np.random.default_rng(3)
def Xarr(U):
    T=U.reshape(3,3,3,3)   # T[c,d,a,b] = U[(c,d),(a,b)] = 3 psi(a,b,c,d)
    return [[T[:,d,a,:].T for d in range(3)] for a in range(3)]   # X_ad[b,c]
def S_components(row):
    n=row[0].shape[0]
    cols=[]
    for k in range(3):
        for idx in range(n*n):
            Y=[np.zeros((n,n),complex) for _ in range(3)]; Y[k].flat[idx]=1
            r1=sum(Y[d]@row[d].conj().T for d in range(3)); r2=sum(row[d].conj().T@Y[d] for d in range(3))
            cols.append(np.concatenate([r1.ravel(),r2.ravel()]))
    L=np.array(cols).T; u,s,vh=np.linalg.svd(L); r=int((s>1e-9*s[0]).sum()); null=vh[r:].conj().T
    comps=np.hstack([null[k*n*n:(k+1)*n*n,:] for k in range(3)])
    return r, null.shape[1], np.linalg.matrix_rank(comps,1e-8), comps
def span_dim(ms): return np.linalg.matrix_rank(np.array([m.ravel() for m in ms]),1e-8)
for trial in range(4):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    X=Xarr(U)
    allX=[X[a][d] for a in range(3) for d in range(3)]
    r,dimS,dimcomp,comps=S_components(X[0])
    # is span(all X_ad) inside comp span?
    C=comps; P=C@np.linalg.pinv(C)
    inside=max(np.linalg.norm(m.ravel()-P@m.ravel()) for m in allX)
    print('rank UG',int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum()),'dim span X_ad',span_dim(allX),'| rank conds',r,'dim S',dimS,'dim comp-span',dimcomp,'X_ad inside comp-span:',round(inside,10), 'dim span row0',span_dim(X[0]))
# random unital 3x3 Kraus triple (non-dual context)
from scipy.stats import unitary_group
for trial in range(2):
    W=unitary_group.rvs(9,random_state=trial)
    row=[W[3*0:3, 3*d:3*d+3] for d in range(3)]  # rows of a unitary: sum_d K_d K_d^dag = I, but not nec. sum K^dag K = I
    # make doubly stochastic via MR-like alternating projections on the 3x9 / 9x3 arrangements
    K=np.hstack(row)
    for it in range(2000):
        K=nc.polar(K) if False else K
        Wp=np.linalg.svd(K,full_matrices=False); K=Wp[0]@Wp[2]          # co-isometry 3x9
        V=np.vstack([K[:,3*d:3*d+3] for d in range(3)]); Wv=np.linalg.svd(V,full_matrices=False); V=Wv[0]@Wv[2]   # isometry 9x3
        K=np.hstack([V[3*d:3*d+3,:] for d in range(3)])
    row=[K[:,3*d:3*d+3] for d in range(3)]
    print('random unital: check',np.linalg.norm(sum(x@x.conj().T for x in row)-np.eye(3)),np.linalg.norm(sum(x.conj().T@x for x in row)-np.eye(3)))
    r,dimS,dimcomp,comps=S_components(row)
    print('   rank conds',r,'dim S',dimS,'dim comp-span',dimcomp,'dim span row',span_dim(row))
