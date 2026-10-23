"""Probe (floating point) of the local dual concavity (LDC) argument near n*.

U(eta) = sum_u [ n^u Psi*(C_u Y eta) + 1.5 n^u ln n^u ],  n^u = 1/9 + (A eta)_u,  eta = n4 - n*4.
Weak duality gives ln F(n) <= U(eta) for every eta; U(0) = ln F(n*), grad U(0) = 0.
Y is the exact optimal linear dual response at n* (rational, from R(0)).  Report the Hessian of U
at 0 and its maximal eigenvalue over random eta in boxes |eta|_inf <= r0.
"""
import sys, math
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, 'code')
from dual import inner, C
from model import nine_from_four

A = np.array([nine_from_four(e) - nine_from_four(np.zeros(4)) for e in np.eye(4)]).T  # 9x4
one = np.ones(4)
gv0, mh0, th0, R0 = inner(np.zeros(4))
G = sum(C[u].T @ R0 @ C[u] for u in range(9))
b = sum(np.outer(C[u].T @ one, A[u]) for u in range(9))  # 18x4
Y = -(45 / 4) * np.linalg.solve(G, b)


def U_and_H(eta):
    n9v = 1 / 9 + A @ eta
    H = np.zeros((4, 4)); val = 0.0
    for u in range(9):
        K = C[u] @ Y
        z = K @ eta
        gv, mh, th, R = inner(z)
        a = A[u]
        val += n9v[u] * gv + 1.5 * n9v[u] * math.log(n9v[u])
        H += 1.5 * np.outer(a, a) / n9v[u] + np.outer(a, K.T @ mh) + np.outer(K.T @ mh, a) + n9v[u] * K.T @ R @ K
    return val, H


v0, H0 = U_and_H(np.zeros(4))
print('U(0) =', v0, ' L* =', 2.5 * math.log(5) + math.log(25 / 24))
print('eig H_U(0):', np.linalg.eigvalsh(H0))
print('eig of Frobenius Gram A^T A:', np.linalg.eigvalsh(A.T @ A))
print('generalised eig H_U(0) vs A^T A:', np.linalg.eigvals(np.linalg.solve(A.T @ A, H0)).real)
rng = np.random.default_rng(7)
for r0 in [0.005, 0.01, 0.015, 0.02, 0.025]:
    worst = -1e9
    for _ in range(200):
        eta = rng.uniform(-r0, r0, 4)
        if rng.random() < 0.3:
            eta = r0 * rng.choice([-1, 1], 4)
        worst = max(worst, np.linalg.eigvalsh(U_and_H(eta)[1]).max())
    print(f'r0={r0}: max eigenvalue of H_U over samples = {worst:.4f}')
# finite-difference check of the Hessian formula
eta = rng.uniform(-0.01, 0.01, 4); h = 1e-4
Hfd = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        ei, ej = np.eye(4)[i] * h, np.eye(4)[j] * h
        Hfd[i, j] = (U_and_H(eta + ei + ej)[0] - U_and_H(eta + ei - ej)[0] - U_and_H(eta - ei + ej)[0] + U_and_H(eta - ei - ej)[0]) / (4 * h * h)
print('FD check max|H - Hfd| =', np.max(np.abs(U_and_H(eta)[1] - Hfd)))
