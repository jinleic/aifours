import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
def tr1(Y): return np.einsum('iaib->ab',Y.reshape(3,3,3,3))
def tr2(Y): return np.einsum('iaja->ij',Y.reshape(3,3,3,3))
ks=[]
for i in range(3):
    for j in range(i+1,3):
        A=np.zeros((3,3),complex); A[i,j]=A[j,i]=1; ks.append(A)
        B=np.zeros((3,3),complex); B[i,j]=1j; B[j,i]=-1j; ks.append(B)
ks.append(np.diag([1,-1,0]).astype(complex)); ks.append(np.diag([0,1,-1]).astype(complex))
I3=np.eye(3)
Hs=[np.kron(I3,k)-Us@np.kron(k.T,I3)@Us.T for k in ks]
print('max |(HU)^R + HU|', max(np.abs(nc.R(H@Us)+H@Us).max() for H in Hs))
M=np.array([[np.trace(ki@tr1(H))-np.trace(ki.T@tr2(Us.T@H@Us)) for H in Hs] for ki in ks])
print('M imag max',np.abs(M.imag).max(),'det M',np.linalg.det(M.real),'3^17/4=',3**17/4)
# B4: rank (R - I) on LU tangent
T=nc.lu_tangent(Us)
cols=[nc.to_vec(nc.R(nc.from_vec(T[:,i]))-nc.from_vec(T[:,i])) for i in range(T.shape[1])]
s=np.linalg.svd(np.array(cols).T,compute_uv=False); print('rank (R-I)|T_LU',int((s>1e-9*s[0]).sum()))
# A1 numeric: random self-dual X
rng=np.random.default_rng(0); X=rng.standard_normal((9,9))+1j*rng.standard_normal((9,9)); U=(X+nc.R(X))/2
print('A1 numeric residual', np.abs(tr1(U@U.conj().T)-tr2(U.conj().T@U).T).max())
