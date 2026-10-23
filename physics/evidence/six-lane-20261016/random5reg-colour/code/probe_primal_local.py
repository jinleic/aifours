"""Probe (float): constants for the primal local argument (X2 + X3)."""
import sys, itertools
import numpy as np
from scipy.linalg import null_space
sys.path.insert(0, 'code')
from model import Model, nine_from_four
mod = Model(5, True)
A = np.array([nine_from_four(e) - nine_from_four(np.zeros(4)) for e in np.eye(4)]).T
Vx = np.zeros((9, 18))
for e, (u, k, v, kv) in enumerate(mod.edges):
    Vx[u, e] += 1; Vx[v, e] += 1
xs = np.full(18, 5/36)
h0 = mod.psi_hess(np.full(4, 5/36))
Hx = mod.E.T @ np.kron(np.eye(9), h0) @ mod.E
Pf = null_space(Vx)
print('dim fibre tangent', Pf.shape[1], ' fibre Hessian eigs', np.round(np.linalg.eigvalsh(Pf.T @ Hx @ Pf), 4))
# optimal lift: L eta with Vx L eta = 5 A eta and Pf^T Hx L eta = 0
Mbig = np.vstack([Vx, Pf.T @ Hx])
rhs = np.vstack([5 * A, np.zeros((Pf.shape[1], 4))])
L = np.linalg.lstsq(Mbig, rhs, rcond=None)[0]
print('residual', np.abs(Mbig @ L - rhs).max())
cn = max(np.linalg.norm(L @ np.array(s)) for s in itertools.product([-1, 1], repeat=4))
ci = max(np.abs(L @ np.array(s)).max() for s in itertools.product([-1, 1], repeat=4))
print('||L||_{inf->2} =', cn, ' ||L||_{inf->inf} =', ci)
# Hessian variation over m-box radius delta (sampled; the certificate uses enclosures)
rng = np.random.default_rng(1)
for delta in [0.002, 0.003, 0.004]:
    dev = 0
    for _ in range(3000):
        m = 5/36 + rng.uniform(-delta, delta, 4)
        if rng.random() < 0.5: m = 5/36 + delta * rng.choice([-1, 1], 4)
        dev = max(dev, np.linalg.norm(mod.psi_hess(m) - h0, 2))
    Q = null_space(np.vstack([np.ones(9) @ np.zeros((9, 18)) + 0, ]))
    print(f'delta={delta}: sampled sup ||H(m)-H(m*)||_2 = {dev:.4f}')
