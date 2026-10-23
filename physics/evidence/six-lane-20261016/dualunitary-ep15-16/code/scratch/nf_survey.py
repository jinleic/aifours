import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
from scipy.optimize import minimize
rng=np.random.default_rng(77)
def ent(x,U):
    a=x[0:3]+1j*x[3:6]; b=x[6:9]+1j*x[9:12]; a=a/np.linalg.norm(a); b=b/np.linalg.norm(b)
    s=np.linalg.svd((U@np.kron(a,b)).reshape(3,3),compute_uv=False); return 1-s[0]**2
def complete(v):
    M=np.eye(3,dtype=complex); M[:,0]=v; Q,R=np.linalg.qr(M); ph=np.vdot(Q[:,0],v); Q[:,0]*=ph; return Q
def normal_forms(U, tries=150):
    out=[]; seen=[]
    for t in range(tries):
        r=minimize(ent,rng.standard_normal(12),args=(U,),method='BFGS',options={'gtol':1e-13})
        if r.fun>1e-12: continue
        a=r.x[0:3]+1j*r.x[3:6]; b=r.x[6:9]+1j*r.x[9:12]; a/=np.linalg.norm(a); b/=np.linalg.norm(b)
        v=np.kron(a,b)
        if any(abs(abs(np.vdot(v,w))-1)<1e-5 for w in seen): continue
        seen.append(v)
        o=(U@v).reshape(3,3); W,s,Vh=np.linalg.svd(o)
        U1=np.kron(complete(W[:,0]),complete(Vh[0])).conj().T@U@np.kron(complete(a),complete(b))
        U1,res,_=gn_project(U1); out.append(U1)
    return out
def stats(U1):
    psi=U1.reshape(3,3,3,3).transpose(2,3,0,1)/3
    n=[3*psi[0,1:,1:,d] for d in range(3)]; q=[3*psi[a,1:,1:,0] for a in range(3)]
    rr=[3*psi[1:,0,c,1:] for c in range(3)]; t=[3*psi[1:,b,0,1:] for b in range(3)]
    rk=lambda vs:int((np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)>1e-6).sum())
    M=psi.transpose(0,3,1,2).reshape(9,9); rM=int((np.linalg.svd(M,compute_uv=False)>1e-6).sum())
    return dict(n0=round(np.linalg.norm(n[0]),3), r0=round(np.linalg.norm(rr[0]),3), dimAB=rk(n+q), rN=rk(n[1:]+q[1:]), dimCD=rk(rr+t), rL=rk(rr[1:]+t[1:]), rM=rM)
pts=[]
for r in range(40):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    rk=int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum())
    if rk in (6,4) and len([p for p in pts if p[1]==rk])<3: pts.append((U,rk))
    if len(pts)>=6: break
S=np.array(g.swap(),complex); C=np.zeros((9,9),complex)
for a in range(3): C[3*a:3*a+3,3*a:3*a+3]=nc.haar(3,rng)
pts.append((S@C,3)); pts.append((np.array(g.P9(),complex),9))
for U,rk in pts:
    nfs=normal_forms(U)
    print('rank',rk,'ep',round(nc.ep(U),4),'#normal forms found',len(nfs))
    from collections import Counter
    c=Counter(tuple(sorted(stats(U1).items())) for U1 in nfs)
    for k,v in c.most_common(6): print('   ',v,dict(k))
