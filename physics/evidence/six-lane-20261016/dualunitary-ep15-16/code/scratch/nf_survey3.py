import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
import importlib.util
spec=importlib.util.spec_from_file_location('s2','nf_survey2.py')
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]
exec(src)
rng=np.random.default_rng(91)
pts=[]
while len([p for p in pts if p[1]==4])<2 or len([p for p in pts if p[1]==6])<1:
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    rk=int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum())
    if rk in (4,6) and len([p for p in pts if p[1]==rk])<(2 if rk==4 else 1): pts.append((U,rk))
S=np.array(g.swap(),complex); C=np.zeros((9,9),complex)
for a in range(3): C[3*a:3*a+3,3*a:3*a+3]=nc.haar(3,rng)
pts.append((S@C,3))
def dims(U1):
    psi=U1.reshape(3,3,3,3).transpose(2,3,0,1)/3
    n=[3*psi[0,1:,1:,d] for d in range(3)]; q=[3*psi[a,1:,1:,0] for a in range(3)]
    rk=lambda vs:int((np.linalg.svd(np.array([v.ravel() for v in vs]),compute_uv=False)>1e-9).sum())
    return (rk(n), rk(q), rk(n+q), rk(n[1:]), rk(q[1:]), rk(n[1:]+q[1:]), round(np.linalg.norm(n[0]),3))
from collections import Counter
for U,rk in pts:
    nfs=normal_forms(U, tries=150)
    c=Counter(dims(U1) for U1,s1 in nfs if s1<1e-12)
    print('rank',rk,'ep',round(nc.ep(U),4),'#nf',len(nfs),'(dimA,dimB,dimA+B, dim N12, dim Q12, dim N12+Q12, |N0|):')
    for k,v in c.most_common(8): print('   ',v,k)
