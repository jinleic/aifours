import sys, json; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import F_dual, gn_project
recs=[]
for s in (201,202,203,204):
    for line in open(f'../../evidence/search/rank9seeds_{s}.jsonl'):
        r=json.loads(line)
        if 'U_re' in r: recs.append(r)
for r in recs:
    U=np.array(r['U_re'])+1j*np.array(r['U_im']); U0=U.copy()
    for it in range(300):
        A=nc.G(U); W,s,Vh=np.linalg.svd(A); s[4:]=0; A=(W*s)@Vh; U=nc.G(A)
        U,res,_=gn_project(U,tol=1e-15,maxit=20)
    sv=np.linalg.svd(nc.G(U),compute_uv=False)
    print(r['seed'],r['t'],'res',f"{np.linalg.norm(F_dual(U)):.2e}",'sv',np.round(sv,15)[:6],'dist to original',f"{np.linalg.norm(U-U0):.2e}",'ep',nc.ep(U))
