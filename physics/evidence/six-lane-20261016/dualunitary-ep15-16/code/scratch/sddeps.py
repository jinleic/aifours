import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
# basis of self-dual subspace V = {X: X^R = X}
B=[]
for X in nc.BASIS:
    Y=(X+nc.R(X))/2
    B.append(nc.to_vec(Y))
B=np.array(B).T
Ub,s,_=np.linalg.svd(B,full_matrices=False); k=int((s>1e-9).sum()); Vb=Ub[:,:k]; print('dim V (real)',k)
def dG(U,Xv):
    X=nc.from_vec(Xv); return nc.herm_vec(X@U.conj().T+U@X.conj().T)
def analyze(U,label):
    J=np.array([dG(U,Vb[:,i]) for i in range(k)]).T  # 81 x 108
    W,s,Vh=np.linalg.svd(J); r=int((s>1e-9*s[0]).sum())
    L=W[:,r:]   # left null space (81 x (81-r))
    print(label,'rank dG|V',r,'left null dim',81-r)
    return L
L0=analyze(Us,'U_s')
# interpret left null vectors as Hermitian matrices H with tr(H dG)=0
def vec_to_herm(v):
    H=np.zeros((9,9),complex); iu=np.triu_indices(9,1); n=len(iu[0])
    H[np.diag_indices(9)]=v[:9]; H[iu]=(v[9:9+n]+1j*v[9+n:])/2; H=H+np.triu(H,1).conj().T
    return H
for j in range(L0.shape[1]):
    H=vec_to_herm(L0[:,j]); T=H.reshape(3,3,3,3)
    # check structure: is H = A (x) I - I (x) A^T-like ? compute partial traces
    print(j, 'tr', np.round(np.trace(H),6), 'tr1-part', np.round(np.linalg.norm(np.einsum('ijik->jk',T)),4),'tr2-part',np.round(np.linalg.norm(np.einsum('jiki->jk',T)),4))
# check constancy at a nearby self-dual point: project a perturbation of U_s onto SD by alternating (U+U^R)/2 & polar
rng=np.random.default_rng(1)
U=Us+0.05*(rng.standard_normal((9,9))+1j*rng.standard_normal((9,9)))
for it in range(5000):
    U=(U+nc.R(U))/2; U=nc.polar(U)
print('SD point residual', np.linalg.norm(nc.R(U)-U), np.linalg.norm(U@U.conj().T-np.eye(9)), 'ep', nc.ep(U), 'rankUG', int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum()))
analyze(U,'nearby SD point')
# global identity test
rng=np.random.default_rng(5)
for j in range(L0.shape[1]):
    H=vec_to_herm(L0[:,j]); vals=[]
    for t in range(5):
        X=nc.from_vec(Vb@rng.standard_normal(k))
        vals.append(abs(np.trace(H@X@X.conj().T)))
    print('null vec',j,'max |tr(H X X^dag)| over random X in V:', max(vals))
