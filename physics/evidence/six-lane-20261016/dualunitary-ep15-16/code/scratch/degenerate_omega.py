import sys; sys.path.insert(0,"."); import numpy as np
exec(open('omega_system.py').read().split("N0=np.diag")[0])
rng=np.random.default_rng(7)
def unital_diag_completion(N0diag, s):
    # N0 = diag(n1,n2); need N1,N2 diagonal with |n0^(i)|^2+... =1 : choose N1=diag(x1,y1), N2=diag(x2,y2)
    n1,n2=N0diag
    t=rng.uniform(0,np.pi/2,2); ph=np.exp(2j*np.pi*rng.random(4))
    r1=np.sqrt(1-abs(n1)**2); r2=np.sqrt(1-abs(n2)**2)
    return [np.diag([r1*np.cos(t[0])*ph[0], r2*np.cos(t[1])*ph[1]]), np.diag([r1*np.sin(t[0])*ph[2], r2*np.sin(t[1])*ph[3]])]
for s in (0.0, 0.3, 0.6, 0.9):
    N0=s*np.eye(2,dtype=complex)
    Nd=unital_diag_completion((s,s),s)
    V=np.linalg.qr(rng.standard_normal((2,2))+1j*rng.standard_normal((2,2)))[0]
    Qd=[V@q@V.conj().T for q in unital_diag_completion((s,s),s)]
    # check unital
    chkN=np.linalg.norm(N0@N0.conj().T+sum(x@x.conj().T for x in Nd)-np.eye(2)); chkQ=np.linalg.norm(N0@N0.conj().T+sum(x@x.conj().T for x in Qd)-np.eye(2))
    res,rk=omega_system(N0,Nd,Qd)
    print(f"s={s}: unital chk {chkN:.1e},{chkQ:.1e}; Omega-system residual {res:.3e} rank {rk}")
