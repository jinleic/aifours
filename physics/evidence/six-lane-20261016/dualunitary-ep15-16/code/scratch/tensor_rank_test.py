import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(0)
# S[s,c,a,d], s,c,a,d in {0,1}, symmetric in (a,d): params for (a,d) in {(0,0),(0,1),(1,1)}
def build(x):
    z=x[:12]+1j*x[12:]
    S=np.zeros((2,2,2,2),complex); k=0
    for s in range(2):
        for c in range(2):
            for (a,d) in [(0,0),(0,1),(1,1)]:
                S[s,c,a,d]=z[k]; S[s,c,d,a]=z[k]; k+=1
    return S
def F1(S): return S.transpose(0,2,1,3).reshape(4,4)   # rows (s,a), cols (c,d)
def F2(S): return S.reshape(4,4)                       # rows (s,c), cols (a,d)
def res(x):
    S=build(x); s=np.linalg.svd(F1(S),compute_uv=False)
    return np.array([s[2],s[3],np.linalg.norm(x)-1])
cnt={}
for t in range(200):
    sol=least_squares(res,rng.standard_normal(24),xtol=1e-15,ftol=1e-15,gtol=1e-15)
    S=build(sol.x); s1=np.linalg.svd(F1(S),compute_uv=False); s2=np.linalg.svd(F2(S),compute_uv=False)
    if s1[2]<1e-9:
        r2=int((s2>1e-7*s2[0]).sum()); cnt[r2]=cnt.get(r2,0)+1
        if r2>=3 and cnt[r2]<=2: print('found rank F2 =',r2,'sv F1',np.round(s1,9),'sv F2',np.round(s2,6))
print('distribution of rank F2 given rank F1<=2 (symmetric in (a,d)):',cnt)
