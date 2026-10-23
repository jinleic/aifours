import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
from scipy.optimize import minimize, least_squares
rng=np.random.default_rng(78)
def unpack(x):
    a=x[0:3]+1j*x[3:6]; b=x[6:9]+1j*x[9:12]; return a,b
def ent(x,U):
    a,b=unpack(x); a=a/np.linalg.norm(a); b=b/np.linalg.norm(b)
    s=np.linalg.svd((U@np.kron(a,b)).reshape(3,3),compute_uv=False); return 1-s[0]**2
def minors(x,U):
    a,b=unpack(x); o=(U@np.kron(a,b)).reshape(3,3); r=[]
    for (i,j) in [(0,1),(0,2),(1,2)]:
        for (k,l) in [(0,1),(0,2),(1,2)]:
            m=o[i,k]*o[j,l]-o[i,l]*o[j,k]; r+= [m.real,m.imag]
    r+=[np.linalg.norm(a)**2-1, np.linalg.norm(b)**2-1, a[0].imag, b[0].imag]
    return np.array(r)
def complete(v):
    M=np.eye(3,dtype=complex); M[:,0]=v; Q,R=np.linalg.qr(M); ph=np.vdot(Q[:,0],v); Q[:,0]*=ph; return Q
def normal_forms(U, tries=120):
    out=[]; seen=[]
    for t in range(tries):
        r=minimize(ent,rng.standard_normal(12),args=(U,),method='BFGS',options={'gtol':1e-12})
        if r.fun>1e-9: continue
        a,b=unpack(r.x); a=a/np.linalg.norm(a)*np.exp(-1j*np.angle(a[0])); b=b/np.linalg.norm(b)*np.exp(-1j*np.angle(b[0]))
        x0=np.concatenate([a.real,a.imag,b.real,b.imag])
        ls=least_squares(minors,x0,args=(U,),xtol=1e-15,ftol=1e-15,gtol=1e-15,method='lm')
        a,b=unpack(ls.x); a/=np.linalg.norm(a); b/=np.linalg.norm(b)
        v=np.kron(a,b)
        if any(abs(abs(np.vdot(v,w))-1)<1e-6 for w in seen): continue
        seen.append(v)
        o=(U@v).reshape(3,3); W,s,Vh=np.linalg.svd(o)
        U1=np.kron(complete(W[:,0]),complete(Vh[0])).conj().T@U@np.kron(complete(a),complete(b))
        out.append((U1, s[1]))
    return out
def stats(U1):
    psi=U1.reshape(3,3,3,3).transpose(2,3,0,1)/3
    n=[3*psi[0,1:,1:,d] for d in range(3)]; q=[3*psi[a,1:,1:,0] for a in range(3)]
    rr=[3*psi[1:,0,c,1:] for c in range(3)]; t=[3*psi[1:,b,0,1:] for b in range(3)]
    sv=lambda vs:np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)
    M=psi.transpose(0,3,1,2).reshape(9,9)
    zc=max(abs(psi[0,0,0,1:]).max(),abs(psi[0,0,1:,0]).max(),abs(psi[0,1:,0,0]).max(),abs(psi[1:,0,0,0]).max())
    return dict(zero_check=float(zc), n0=round(np.linalg.norm(n[0]),3), r0=round(np.linalg.norm(rr[0]),3),
                svAB=np.round(sv(n+q),8).tolist(), svN=np.round(sv(n[1:]+q[1:]),8).tolist(), svL=np.round(sv(rr[1:]+t[1:]),8).tolist(),
                svM=np.round(np.linalg.svd(M,compute_uv=False),8).tolist())
U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
print('rank', int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum()), 'ep', nc.ep(U))
nfs=normal_forms(U)
print('#nf',len(nfs))
for U1,s1 in nfs[:8]:
    st=stats(U1); print('s1',f"{s1:.1e}",'zc',f"{st['zero_check']:.1e}",'n0',st['n0'],'r0',st['r0']); print('   svAB',st['svAB']); print('   svN',st['svN'],' svL',st['svL']); print('   svM',st['svM'])
