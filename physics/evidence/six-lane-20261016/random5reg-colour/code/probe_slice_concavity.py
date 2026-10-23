"""Probe: slice concavity of psi <=> max_{u perp m} u^T S2 u / u^T diag(m) u < 2 (exact equivalence, see README log)."""
import sys, math
import numpy as np
from scipy.linalg import eigh, null_space
sys.path.insert(0, 'code')
from model import Model

def ratio(mod, theta):
    d = np.exp(mod.logw + mod.Sarr @ theta)
    m = mod.Sarr.T @ d
    S2 = (mod.Sarr.T * d) @ mod.Sarr
    B = null_space(m[None, :])  # basis of m-perp
    A = B.T @ S2 @ B
    C = B.T @ np.diag(m) @ B
    ev = eigh(A, C, eigvals_only=True)
    # also direct Hessian check on 1-perp
    Hs = 0.5 * np.diag(1 / m) - np.linalg.inv(S2)
    B1 = null_space(np.ones((1, 4)))
    hev = np.linalg.eigvalsh(B1.T @ Hs @ B1)
    return ev.max(), hev.max(), m

rainbow = (sys.argv[1] != 'plain') if len(sys.argv) > 1 else True
mod = Model(5, rainbow)
rng = np.random.default_rng(20261016)
worst = (0, None)
for scale in [0.5, 1, 2, 4, 8, 16]:
    for _ in range(20000):
        th = rng.normal(0, scale, 4)
        r, h, m = ratio(mod, th)
        if (r < 2) != (h < 0):
            print('MISMATCH', th, r, h)
        if r > worst[0]:
            worst = (r, th.copy(), m / m.sum())
    print(f'scale {scale}: worst ratio so far {worst[0]:.6f} at theta-theta.mean {worst[1]-worst[1].mean()} mhat {worst[2]}')
r, h, m = ratio(mod, np.zeros(4))
print('centre ratio', r, 'centre slice-hessian max eig', h)
