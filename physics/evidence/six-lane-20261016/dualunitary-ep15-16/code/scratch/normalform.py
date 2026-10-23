import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
from scipy.optimize import minimize
rng=np.random.default_rng(21)
def ent(x,U):
    a=x[0:3]+1j*x[3:6]; b=x[6:9]+1j*x[9:12]; a=a/np.linalg.norm(a); b=b/np.linalg.norm(b)
    s=np.linalg.svd((U@np.kron(a,b)).reshape(3,3),compute_uv=False); return 1-s[0]**2
def complete(v):
    # unitary with first column v
    M=np.eye(3,dtype=complex); M[:,0]=v
    Q,R=np.linalg.qr(M); Q=Q*(np.conj(np.diag(R))/abs(np.diag(R))) if False else Q
    # fix phase so that Q[:,0] = v
    ph=np.vdot(Q[:,0],v); Q[:,0]*=ph
    return Q
def normal_form(U):
    for t in range(200):
        r=minimize(ent,rng.standard_normal(12),args=(U,),method='BFGS',options={'gtol':1e-13})
        if r.fun<1e-12: break
    a=r.x[0:3]+1j*r.x[3:6]; b=r.x[6:9]+1j*r.x[9:12]; a/=np.linalg.norm(a); b/=np.linalg.norm(b)
    out=(U@np.kron(a,b)).reshape(3,3); W,s,Vh=np.linalg.svd(out); g=W[:,0]; h=Vh[0]
    v3=complete(a); v4=complete(b); u1=complete(g); u2=complete(h)
    U1=np.kron(u1,u2).conj().T@U@np.kron(v3,v4)
    return U1
def blocks(U1):
    psi=np.zeros((3,3,3,3),complex)
    T=U1.reshape(3,3,3,3) # T[c,d,a,b]
    psi=T.transpose(2,3,0,1)/3  # psi[a,b,c,d]
    K=[1,2]
    out={}
    out['0000']=psi[0,0,0,0]
    out['y(psi14)']=np.linalg.norm(psi[0][np.ix_(K,K)][:, :, 0]) if False else np.linalg.norm(psi[0,1:,1:,0])
    out['z(psi23)']=np.linalg.norm(psi[1:,0,0,1:])
    M=psi.transpose(0,3,1,2).reshape(9,9)  # rows (a,d), cols (b,c)
    # sector index lists
    idx=lambda i,j:3*i+j
    S00=[idx(0,0)]; S0K=[idx(0,1),idx(0,2)]; SK0=[idx(1,0),idx(2,0)]; SKK=[idx(1,1),idx(1,2),idx(2,1),idx(2,2)]
    N=M[np.ix_(S0K+SK0,SKK)]; L=M[np.ix_(SKK,S0K+SK0)]
    zero_checks=[np.linalg.norm(M[np.ix_(S0K+SK0,S00+S0K+SK0)]), np.linalg.norm(M[np.ix_(S00,S0K+SK0)]), np.linalg.norm(M[np.ix_(S0K+SK0,S00)])]
    rk=lambda A:int((np.linalg.svd(A,compute_uv=False)>1e-8).sum())
    out.update(rankM=rk(M), rankN=rk(N), rankL=rk(L), zero_checks=np.round(zero_checks,10).tolist())
    return out
for r in range(6):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    U1=normal_form(U)
    print(r, 'ep',round(nc.ep(U),4), 'U1[0,0]',np.round(abs(U1[0,0]),8), blocks(U1))
