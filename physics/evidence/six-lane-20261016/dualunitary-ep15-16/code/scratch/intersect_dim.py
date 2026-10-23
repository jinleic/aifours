import sys; sys.path.insert(0,"."); sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
from ascent import gn_project
src=open('nf_survey2.py').read().split("U,k=nc.mr_map")[0]; exec(src)
exec(open('generic_case_check2.py').read().split("for trial in range(3):")[0].split("src=open")[0])
def right_twist(mats):
    rows=[]
    for M in mats:
        r=np.zeros(4,complex)
        for k in range(2):
            r[2*k+1]+=M[0,k]; r[2*k+0]-=M[1,k]
        rows.append(r)
    A=np.array(rows); u,s,vh=np.linalg.svd(A); w=vh[-1].conj().reshape(2,2)
    return w/np.sqrt(abs(np.linalg.det(w)))
rng=np.random.default_rng(55)
def null(A,tol=1e-9):
    u,s,vh=np.linalg.svd(A); r=int((s>tol).sum()); return vh[r:].conj().T
for trial in range(3):
    U,k=nc.mr_map(nc.haar(9,rng),iters=3000,tol=1e-10); U,res,_=gn_project(U)
    for U1,s1 in normal_forms(U,tries=40)[:2]:
        phi=U1.reshape(3,3,3,3).transpose(2,3,0,1)
        R=[phi[1:,0,c,1:] for c in range(3)]
        wp=right_twist(R); G4=np.eye(3,dtype=complex); G4[1:,1:]=wp
        U2=np.kron(np.eye(3),G4.T)@U1     # gauge C=Sym (acts on d)
        phi=U2.reshape(3,3,3,3).transpose(2,3,0,1)
        N=[phi[0,1:,1:,d] for d in range(3)]; Q=[phi[a,1:,1:,0] for a in range(3)]
        R=[phi[1:,0,c,1:] for c in range(3)]; T=[phi[1:,b,0,1:] for b in range(3)]
        # Rcal rows a: vector over (c,d) ; Tcal rows a: vector over (b,d)
        Rcal=np.array([[R[c+1][a,d] for c in range(2) for d in range(2)] for a in range(2)])
        Tcal=np.array([[T[b+1][a,d] for b in range(2) for d in range(2)] for a in range(2)])
        # tensor X[b,c,d] (8-dim) constraints: for each b: X[b,.,.] orth to conj? relation sum_{c,d} X[b,c,d] conj(R_c[a,d]) = 0
        rows=[]
        for b in range(2):
            for a in range(2):
                r=np.zeros(8,complex)
                for c in range(2):
                    for d in range(2): r[4*b+2*c+d]=np.conj(R[c+1][a,d])
                rows.append(r)
        for c in range(2):
            for a in range(2):
                r=np.zeros(8,complex)
                for b in range(2):
                    for d in range(2): r[4*b+2*c+d]=np.conj(T[b+1][a,d])
                rows.append(r)
        I=null(np.array(rows))
        Nt=np.array([N[d+1][b,c] for b in range(2) for c in range(2) for d in range(2)])
        Qt=np.array([Q[d+1][b,c] for b in range(2) for c in range(2) for d in range(2)])
        P=I@np.linalg.pinv(I) if I.shape[1]>0 else np.zeros((8,8))
        print('dim I',I.shape[1],'| N in I resid',round(np.linalg.norm(Nt-P@Nt),12),'Q in I resid',round(np.linalg.norm(Qt-P@Qt),12), '| sym check R',max(np.linalg.norm(x-x.T) for x in R+T))
