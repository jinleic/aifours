import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, itertools, collections
rng=np.random.default_rng(0)
cnt=collections.Counter(); ex={}
for p in itertools.permutations(range(9)):
    P=np.zeros((9,9)); P[list(p),range(9)]=1   # P|col>=|p(col)>
    PR=nc.R(P)
    if not (PR.sum(0)==1).all() or not (PR.sum(1)==1).all(): continue
    PG=nc.G(P)
    r0=np.linalg.matrix_rank(PG)
    ph=np.exp(2j*np.pi*rng.random(9)); Pt=np.zeros((9,9),complex); Pt[list(p),range(9)]=ph
    r1=np.linalg.matrix_rank(nc.G(Pt),1e-9)
    td=(PG.sum(0)==1).all() and (PG.sum(1)==1).all()
    key=(r0,r1,bool(td), round(float(nc.ep(P)),6))
    cnt[key]+=1
    ex.setdefault(key,p)
for k in sorted(cnt): print(k, cnt[k], ex[k])
