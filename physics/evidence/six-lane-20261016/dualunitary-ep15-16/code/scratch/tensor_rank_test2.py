import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(1)
def build(x):
    z=x[:16]+1j*x[16:]; U=z[:8].reshape(4,2); V=z[8:].reshape(4,2)
    F1=U@V.T   # rows (s,a), cols (c,d)
    S=F1.reshape(2,2,2,2).transpose(0,2,1,3)  # S[s,c,a,d]
    return S
def res(x):
    S=build(x); r=[]
    for s in range(2):
        for c in range(2):
            r.append(S[s,c,0,1]-S[s,c,1,0])
    r=np.array(r); return np.concatenate([r.real,r.imag,[np.linalg.norm(S)-1]])
cnt={}
for t in range(300):
    sol=least_squares(res,rng.standard_normal(32),xtol=1e-15,ftol=1e-15,gtol=1e-15)
    if np.linalg.norm(res(sol.x))>1e-12: continue
    S=build(sol.x)
    F2=S.reshape(4,4); s2=np.linalg.svd(F2,compute_uv=False); r2=int((s2>1e-8*s2[0]).sum())
    cnt[r2]=cnt.get(r2,0)+1
print('rank F2 distribution given rank F1<=2 & (a,d)-symmetry:',cnt)
