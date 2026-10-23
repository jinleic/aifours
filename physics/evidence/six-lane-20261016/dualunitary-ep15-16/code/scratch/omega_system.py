import sys; sys.path.insert(0,".."); import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(5)
def unital_completion(N0, seed):
    r=np.random.default_rng(seed)
    def res(x):
        K=(x[:8]+1j*x[8:]).reshape(2,2,2)
        A=N0@N0.conj().T+sum(k@k.conj().T for k in K)-np.eye(2)
        B=N0.conj().T@N0+sum(k.conj().T@k for k in K)-np.eye(2)
        v=np.concatenate([A.ravel(),B.ravel()]); return np.concatenate([v.real,v.imag])
    s=least_squares(res,r.standard_normal(16)*0.5,xtol=1e-15,ftol=1e-15,gtol=1e-15)
    K=(s.x[:8]+1j*s.x[8:]).reshape(2,2,2); return K, np.linalg.norm(res(s.x))
def omega_system(N0,Ns,Qs):
    # unknown Omega_ad (a,d in {1,2}) 2x2 complex -> 16 complex unknowns; build linear map (real-linear because of daggers)
    def F(om):   # om: 4 2x2 matrices indexed (a,d) -> residuals of (alpha),(delta),(beta),(gamma)
        O={(a,d):om[2*a+d] for a in range(2) for d in range(2)}
        r=[]
        for a in range(2):   # alpha: N0 Qa^dag + sum_d Nd Omega_ad^dag
            r.append(N0@Qs[a].conj().T+sum(Ns[d]@O[(a,d)].conj().T for d in range(2)))
            r.append(N0.conj().T@Qs[a]+sum(Ns[d].conj().T@O[(a,d)] for d in range(2)))   # gamma
        for d in range(2):   # beta/delta
            r.append(N0@Ns[d].conj().T+sum(Qs[a]@O[(a,d)].conj().T for a in range(2)))
            r.append(N0.conj().T@Ns[d]+sum(Qs[a].conj().T@O[(a,d)] for a in range(2)))
        v=np.concatenate([x.ravel() for x in r]); return np.concatenate([v.real,v.imag])
    # affine real-linear: F(om)=b + L om ; build L via basis
    zero=[np.zeros((2,2),complex) for _ in range(4)]
    b=F(zero); cols=[]
    for k in range(4):
        for idx in range(4):
            for ph in (1,1j):
                om=[np.zeros((2,2),complex) for _ in range(4)]; om[k].flat[idx]=ph; cols.append(F(om)-b)
    L=np.array(cols).T
    sol,res,rk,sv=np.linalg.lstsq(L,-b,rcond=None)
    return np.linalg.norm(L@sol+b), rk
N0=np.diag([0.6,0.35]).astype(complex)
U=np.linalg.qr(rng.standard_normal((2,2))+1j*rng.standard_normal((2,2)))[0]; N0=U@N0@np.linalg.qr(rng.standard_normal((2,2))+1j*rng.standard_normal((2,2)))[0]
K,e1=unital_completion(N0,1); L,e2=unital_completion(N0,2)
print('completion residuals',e1,e2)
def dimspan(ms): return np.linalg.matrix_rank(np.array([m.ravel() for m in ms]),1e-9)
print('dim A',dimspan([N0,*K]),'dim B',dimspan([N0,*L]),'dim A+B',dimspan([N0,*K,*L]))
print('system with independent completions (A != B): residual, rank', omega_system(N0,K,L))
u=np.linalg.qr(rng.standard_normal((2,2))+1j*rng.standard_normal((2,2)))[0]
Lr=[u[0,0]*K[0]+u[0,1]*K[1], u[1,0]*K[0]+u[1,1]*K[1]]
print('system with B = A (rotated completion): residual, rank', omega_system(N0,K,Lr))
print('system with Q = N exactly: residual, rank', omega_system(N0,K,list(K)))
