"""Probe (floating point): Hessian of L on the 13-dim tangent space T at m*, and its variation."""
import sys, math
import numpy as np
from scipy.linalg import null_space
sys.path.insert(0, 'code')
from model import Model
mod = Model(5, True)
# tangent constraints in x (18): row/col sums of n^u = (1/5) sum_{e in u} x_e
A = []
for i in range(3):
    row = np.zeros(36)
    for j in range(3): row[4*(3*i+j):4*(3*i+j)+4] = 1
    A.append(row @ mod.E)
for j in range(3):
    row = np.zeros(36)
    for i in range(3): row[4*(3*i+j):4*(3*i+j)+4] = 1
    A.append(row @ mod.E)
A = np.array(A)
Q = null_space(A)
print('dim T =', Q.shape[1])
def HL(x):
    M = mod.m_from_x(x)
    blocks = np.zeros((36, 36))
    for u in range(9):
        blocks[4*u:4*u+4, 4*u:4*u+4] = mod.psi_hess(M[u])
    return mod.E.T @ blocks @ mod.E
xs = np.full(18, 5/36)
H = Q.T @ HL(xs) @ Q
ev = np.linalg.eigvalsh(H)
print('eigs of H|T at m*:', np.round(ev, 5))
# single-vertex psi Hessian at m*
h0 = mod.psi_hess(np.full(4, 5/36))
print('psi hess at m*:\n', h0)
# variation: random perturbations within box delta
rng = np.random.default_rng(5)
for delta in [0.005, 0.01, 0.02, 0.04]:
    worst = -1e9; worst_dev = 0
    for _ in range(300):
        x = xs + rng.uniform(-delta, delta, 18)
        Hx = Q.T @ HL(x) @ Q
        worst = max(worst, np.linalg.eigvalsh(Hx).max())
        worst_dev = max(worst_dev, max(np.linalg.norm(mod.psi_hess(mod.m_from_x(x)[u]) - h0, 2) for u in range(9)))
    print(f'delta={delta}: max eig over samples {worst:.4f}; max ||psi hess dev||_2 {worst_dev:.3f}')
# 4x4 Hessian of ln F at n* via finite differences of the dual value
from dual import solve_dual
I3 = np.array([1,0,0,0,1,0,0,0,1])/3; Cn = np.full(9, 1/9)
for t in [1e-3, 2e-3, 4e-3]:
    v1 = solve_dual(Cn + t*(I3 - Cn))[0]; v0 = solve_dual(Cn)[0]; vm = solve_dual(Cn - t*(I3-Cn))[0]
    eta2 = t*t*np.sum((I3-Cn)**2)
    print('t', t, 'second diff coefficient c =', -(v1 + vm - 2*v0)/(2*eta2))
