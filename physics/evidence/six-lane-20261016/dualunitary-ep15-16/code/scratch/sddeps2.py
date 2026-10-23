import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
# left null space: Hermitian H with (H U)^R = - H U
basisH=[]
for i in range(9):
    E=np.zeros((9,9),complex); E[i,i]=1; basisH.append(E)
for i in range(9):
    for j in range(i+1,9):
        E=np.zeros((9,9),complex); E[i,j]=E[j,i]=1; basisH.append(E)
        E=np.zeros((9,9),complex); E[i,j]=1j; E[j,i]=-1j; basisH.append(E)
cols=[]
for H in basisH:
    Y=H@Us; Z=nc.R(Y)+Y
    cols.append(np.concatenate([Z.real.ravel(),Z.imag.ravel()]))
A=np.array(cols).T
_,s,Vh=np.linalg.svd(A); null=Vh[-8:]
print('smallest sv',np.round(s[-10:],8))
Hs=[sum(c*B for c,B in zip(v,basisH)) for v in null]
# test structure: is each H of form h(x)I + I(x)k ?  project onto that subspace
def local_proj(H):
    T=H.reshape(3,3,3,3)
    h=np.einsum('ijkj->ik',T)/3; k=np.einsum('jijk->ik',T)/3; t=np.trace(H)/9
    L=np.kron(h,np.eye(3))+np.kron(np.eye(3),k)-t*np.eye(9)
    return np.linalg.norm(H-L)/np.linalg.norm(H)
for H in Hs: print('rel dist from local-sum form', round(local_proj(H),6))
# check if span of null H's equals {h(x)I - ...}: compute partial traces
for H in Hs[:3]:
    T=H.reshape(3,3,3,3); print(np.round(np.einsum('ijkj->ik',T),3)); print(np.round(np.einsum('jijk->ik',T),3)); print('---')
