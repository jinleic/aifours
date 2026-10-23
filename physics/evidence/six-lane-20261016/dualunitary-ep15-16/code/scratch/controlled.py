import sys; sys.path.insert(0,".."); import numpy as np, numcore as nc, gates as g
rng=np.random.default_rng(2)
S=np.array(g.swap(),complex)
for t in range(3):
    C=np.zeros((9,9),complex)
    for a in range(3):
        C[3*a:3*a+3,3*a:3*a+3]=nc.haar(3,rng)
    U=S@C
    J=nc.jac_dual(U); s=np.linalg.svd(J,compute_uv=False); r=int((s>1e-8*s[0]).sum())
    sv=np.linalg.svd(nc.G(U),compute_uv=False)
    print('S*controlled: dual res',f"{nc.dual_residual(U):.1e}",'tangent',162-r,'rank U^G',int((sv>1e-8).sum()),'ep',round(nc.ep(U),4))
