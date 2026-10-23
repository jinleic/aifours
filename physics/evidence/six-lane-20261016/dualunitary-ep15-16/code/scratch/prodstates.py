import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import gn_project
import gates as g
from scipy.optimize import minimize
rng=np.random.default_rng(8)
def ent(x,U):
    a=x[0:3]+1j*x[3:6]; b=x[6:9]+1j*x[9:12]
    a=a/np.linalg.norm(a); b=b/np.linalg.norm(b)
    out=(U@np.kron(a,b)).reshape(3,3)
    s=np.linalg.svd(out,compute_uv=False)
    return 1-s[0]**2
def find(U, tries=300):
    sols=[]
    for t in range(tries):
        x0=rng.standard_normal(12)
        r=minimize(ent,x0,args=(U,),method='BFGS',options={'gtol':1e-12,'maxiter':2000})
        if r.fun<1e-10:
            a=r.x[0:3]+1j*r.x[3:6]; b=r.x[6:9]+1j*r.x[9:12]; a/=np.linalg.norm(a); b/=np.linalg.norm(b)
            # canonical phase
            a=a*np.exp(-1j*np.angle(a[np.argmax(abs(a))])); b=b*np.exp(-1j*np.angle(b[np.argmax(abs(b))]))
            v=np.kron(a,b)
            if not any(abs(abs(np.vdot(v,w))-1)<1e-6 for w in sols): sols.append(v)
    return sols
S=np.array(g.swap(),complex); Us=S@np.array(g.U36(-0.5,np.sqrt(3)/2),complex)
print('U_s: #product->product found', len(find(Us)))
for r in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    print('random dual',r,'ep',round(nc.ep(U),4),'#found',len(find(U)))
for r in range(2):
    U=nc.haar(9,rng); print('haar',r,'#found',len(find(U)))
