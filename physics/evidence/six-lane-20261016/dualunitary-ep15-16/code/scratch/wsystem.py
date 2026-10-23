import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
import gates as g
rng=np.random.default_rng(12)
def slices(U):
    # psi(a,b,c,d)=U[(c,d),(a,b)]/3 ; Z_bc[a,d] = 3 psi(a,b,c,d) = U[3c+d, 3a+b]
    T=U.reshape(3,3,3,3) # T[c,d,a,b]
    return [[T[c,:,:,b].T for c in range(3)] for b in range(3)]  # Z[b][c][a,d]=T[c,d,a,b]
def wspace(U):
    Z=slices(U)
    rows=[]
    # unknown w (9 complex) ; equation: (wZ - Z^T w^T) antisym entries
    for b in range(3):
        for c in range(3):
            M=Z[b][c]
            for (i,j) in [(0,1),(0,2),(1,2)]:
                # (wM)_{ij} - (wM)_{ji} = sum_k w_ik M_kj - w_jk M_ki
                r=np.zeros(9,complex)
                for k in range(3):
                    r[3*i+k]+=M[k,j]; r[3*j+k]-=M[k,i]
                rows.append(r)
    A=np.array(rows); s=np.linalg.svd(A,compute_uv=False); null=int((s<1e-9*s[0]).sum())
    Vh=np.linalg.svd(A)[2]; w=Vh[-1].conj().reshape(3,3)
    return null, s[-4:], w
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
n,s,w=wspace(Us); print('U_s nulldim',n, np.round(s,6)); print(np.round(w/w[np.unravel_index(np.argmax(abs(w)),w.shape)],4))
for r in range(8):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    n,s,w=wspace(U)
    sv=np.linalg.svd(w,compute_uv=False)
    rk=int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum())
    print(r,'rankUG',rk,'ep',round(nc.ep(U),4),'nulldim',n,'smallest sv of system',np.round(s,8),'w singular values (normalized)',np.round(sv/sv[0],6))
# also left-side twist: Z w symmetric? and P9
P=np.array(g.P9(),complex); n,s,w=wspace(P); print('P9 nulldim',n,np.round(s,6))
