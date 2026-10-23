import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]; exec(src)
rng=np.random.default_rng(999)
def check(U1):
    phi=U1.reshape(3,3,3,3).transpose(2,3,0,1)
    K=[1,2]
    N=[phi[0,1:,1:,d] for d in range(3)]; Q=[phi[a,1:,1:,0] for a in range(3)]
    R=[phi[1:,0,c,1:] for c in range(3)]; T=[phi[1:,b,0,1:] for b in range(3)]
    Om={(a,d):phi[a,1:,1:,d] for a in K for d in K}; Omp={(b,c):phi[1:,b,c,1:] for b in K for c in K}
    I2=np.eye(2); e=[]
    e.append(np.linalg.norm(sum(x@x.conj().T for x in N)-I2)); e.append(np.linalg.norm(sum(x.conj().T@x for x in N)-I2))
    e.append(np.linalg.norm(sum(x@x.conj().T for x in Q)-I2)); e.append(np.linalg.norm(sum(x.conj().T@x for x in Q)-I2))
    e.append(np.linalg.norm(sum(x@x.conj().T for x in R)-I2)); e.append(np.linalg.norm(sum(x.conj().T@x for x in R)-I2))
    e.append(np.linalg.norm(sum(x@x.conj().T for x in T)-I2)); e.append(np.linalg.norm(sum(x.conj().T@x for x in T)-I2))
    for a in K:
        e.append(np.linalg.norm(N[0]@Q[a].conj().T+sum(N[d]@Om[(a,d)].conj().T for d in K)))    # alpha
        e.append(np.linalg.norm(N[0].conj().T@Q[a]+sum(N[d].conj().T@Om[(a,d)] for d in K)))    # gamma
    for d in K:
        e.append(np.linalg.norm(N[d]@N[0].conj().T+sum(Om[(a,d)]@Q[a].conj().T for a in K)))    # beta
        e.append(np.linalg.norm(N[0].conj().T@N[d]+sum(Q[a].conj().T@Om[(a,d)] for a in K)))    # delta
    for b in K:   # (a,d)-sector analogues
        e.append(np.linalg.norm(T[b]@R[0].conj().T+sum(Omp[(b,c)]@R[c].conj().T for c in K)))
        e.append(np.linalg.norm(R[0].conj().T@T[b]+sum(R[c].conj().T@Omp[(b,c)] for c in K)))
    for c in K:
        e.append(np.linalg.norm(R[c]@R[0].conj().T+sum(Omp[(b,c)]@T[b].conj().T for b in K)))
        e.append(np.linalg.norm(R[0].conj().T@R[c]+sum(T[b].conj().T@Omp[(b,c)] for b in K)))
    # O1..O4 (indices: N_d[b,c], R_c[a,d], T_b[a,d], Q_a[b,c]) with 0-based K indices
    O1=max(abs(sum(N[d+1][b,c]*np.conj(R[c+1][a,d]) for c in range(2) for d in range(2))) for a in range(2) for b in range(2))
    O3=max(abs(sum(N[d+1][b,c]*np.conj(T[b+1][a,d]) for b in range(2) for d in range(2))) for a in range(2) for c in range(2))
    O4=max(abs(sum(Q[a+1][b,c]*np.conj(R[c+1][a,d]) for a in range(2) for c in range(2))) for b in range(2) for d in range(2))
    O2=max(abs(sum(Q[a+1][b,c]*np.conj(T[b+1][a,d]) for a in range(2) for b in range(2))) for c in range(2) for d in range(2))
    return max(e), O1,O2,O3,O4
for kind in ('main','rank4','controlled','P9'):
    if kind=='main':
        U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    elif kind=='rank4':
        while True:
            U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
            if int((np.linalg.svd(nc.G(U),compute_uv=False)>1e-7).sum())==4: break
    elif kind=='controlled':
        C=np.zeros((9,9),complex)
        for a in range(3): C[3*a:3*a+3,3*a:3*a+3]=nc.haar(3,rng)
        U=np.array(g.swap(),complex)@C
    else:
        v=[nc.haar(3,rng) for _ in range(4)]; U=np.kron(v[0],v[1])@np.array(g.P9(),complex)@np.kron(v[2],v[3])
    for U1,s1 in normal_forms(U,tries=30)[:3]:
        print(kind, 'max |unital/alpha-delta/(a,d)-analog| %.1e  O1 %.1e O2 %.1e O3 %.1e O4 %.1e'%check(U1))
