import sys, json; sys.path.insert(0,".."); import numpy as np, numcore as nc
from ascent import F_dual
import mpmath as mp
recs=[]
for s in (201,202,203,204):
    for line in open(f'../../evidence/search/rank9seeds_{s}.jsonl'):
        r=json.loads(line)
        if 'U_re' in r: recs.append(r)
print(len(recs),'saved suspicious points')
for r in recs:
    U=np.array(r['U_re'])+1j*np.array(r['U_im'])
    # damped GN with fixed small truncation threshold, many iterations, track sv of U^G
    for it in range(400):
        f=F_dual(U); J=nc.jac_dual(U)
        W,s,Vh=np.linalg.svd(J,full_matrices=False)
        k=int((s>1e-6*s[0]).sum())
        U=U+nc.from_vec(-(Vh[:k].T@((W[:,:k].T@f)/s[:k])))
        if it%100==99:
            sv=np.linalg.svd(nc.G(U),compute_uv=False)
            print(r['seed'],r['t'],'it',it+1,'res',f"{np.linalg.norm(F_dual(U)):.2e}",'sv',np.round(sv,9))
