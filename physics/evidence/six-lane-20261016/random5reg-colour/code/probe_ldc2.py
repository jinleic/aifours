"""Probe (float): quadratic-majorant variant of the local dual concavity argument (LDC')."""
import sys, math
import numpy as np
sys.path.insert(0, 'code')
from dual import inner, C
from model import nine_from_four
A = np.array([nine_from_four(e) - nine_from_four(np.zeros(4)) for e in np.eye(4)]).T
one = np.ones(4)
gv0, mh0, th0, R0 = inner(np.zeros(4))
G = sum(C[u].T @ R0 @ C[u] for u in range(9))
b = sum(np.outer(C[u].T @ one, A[u]) for u in range(9))
Y = -(45 / 4) * np.linalg.solve(G, b)
K = [C[u] @ Y for u in range(9)]
P = np.eye(4) - np.ones((4, 4)) / 4
print('max row-abs-sum of K_u:', max(np.abs(Ku).sum(axis=1).max() for Ku in K))
Hsens = sum(Ku.T @ P @ Ku for Ku in K) / 9
AtA = A.T @ A
print('gen. eig of (1/9) sum K^T P K vs A^T A:', np.sort(np.linalg.eigvals(np.linalg.solve(AtA, Hsens)).real))
rng = np.random.default_rng(3)
for zr in [0.005, 0.01, 0.02, 0.04, 0.06]:
    worst = 0
    for _ in range(400):
        z = rng.uniform(-zr, zr, 4)
        if rng.random() < 0.5: z = zr * rng.choice([-1, 1], 4)
        R = inner(z)[3]
        worst = max(worst, np.linalg.eigvalsh(P @ (R - R0) @ P).max())
    print(f'z-box radius {zr}: sup lambda_max(R(z)-R(0)) ~ {worst:.4f}')
def HUbar(eta, eps):
    H = np.zeros((4, 4))
    for u in range(9):
        a = A[u]; n = 1/9 + a @ eta
        l = 1.25 * K[u].T @ one; Q = K[u].T @ (R0 + eps * P) @ K[u]
        g = l + Q @ eta
        H += np.outer(a, g) + np.outer(g, a) + n * Q + 1.5 * np.outer(a, a) / n
    return H
for r0 in [0.001, 0.002, 0.003, 0.005]:
    zr = r0 * max(np.abs(Ku).sum(axis=1).max() for Ku in K)
    for eps in [0.01, 0.03, 0.05, 0.1]:
        worst = -1e9
        for c in range(16):
            eta = r0 * np.array([1 if (c >> k) & 1 else -1 for k in range(4)])
            worst = max(worst, np.linalg.eigvalsh(HUbar(eta, eps)).max())
        print(f'r0={r0} (z radius {zr:.4f}) eps={eps}: max eig H_Ubar at box corners {worst:.4f}; at 0 {np.linalg.eigvalsh(HUbar(np.zeros(4), eps)).max():.4f}')
