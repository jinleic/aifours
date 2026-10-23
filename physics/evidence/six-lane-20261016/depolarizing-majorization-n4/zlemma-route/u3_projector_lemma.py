"""Structural route to U_3 (k <= 4) via a convex decomposition (exploration, floating point).

For pure psi, rho_{~l} = mu_l |alpha_l><alpha_l| + (1-mu_l) |beta_l><beta_l| (mu_l >= 1/2), so with t_l = 2mu_l - 1:
   rho_{~l} (x) 1_l = t_l P_{A_l} + (1 - t_l) Q_l / 2,   P_{A_l} = |alpha_l><alpha_l| (x) 1_l,  Q_l = (P_alpha + P_beta) (x) 1_l.
X_3 is then a convex combination of the 16 "pattern" operators  O_L = sum_{l in L} P_{A_l} + sum_{l not in L} Q_l / 2,
so K_k(X_3) <= max_L K_k(O_L).  Lemma candidates (target 3 + k, k = 1..4):
  (arb)  for ARBITRARY unit alpha_l and 2-dim subspaces S_l of the three other qubits;
  (psi)  for alpha_l, S_l derived from one 4-qubit pure psi (Schmidt data).
Mode arb|psi, pattern size |L| in 0..4, starts, seed.
"""
import itertools
import sys

import numpy as np
from scipy.optimize import minimize


def embed3(M3, l):
    """M3 on the three qubits other than l (in increasing order) (x) 1 on qubit l -> 16x16."""
    T = np.kron(M3, np.eye(2)).reshape([2] * 8)
    order = [m for m in range(4) if m != l] + [l]
    perm = [order.index(q) for q in range(4)]
    return T.transpose(perm + [p + 4 for p in perm]).reshape(16, 16)


def ky(M, k):
    return np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))[::-1][:k].sum()


def pattern_op_arb(z, L):
    ops = 0
    off = 0
    for l in range(4):
        if l in L:
            a = z[off:off + 8] + 1j * z[off + 8:off + 16]; off += 16
            a /= np.linalg.norm(a)
            ops = ops + embed3(np.outer(a, a.conj()), l)
        else:
            Z = (z[off:off + 16] + 1j * z[off + 16:off + 32]).reshape(8, 2); off += 32
            q, _ = np.linalg.qr(Z)
            ops = ops + embed3(q @ q.conj().T, l) / 2
    return ops


def pattern_op_psi(z, L):
    psi = z[:16] + 1j * z[16:]
    psi /= np.linalg.norm(psi)
    T = psi.reshape([2] * 4)
    ops = 0
    for l in range(4):
        M = np.moveaxis(T, l, 0).reshape(2, 8)            # qubit l vs others (in increasing order)
        u, s, vh = np.linalg.svd(M)                        # psi = sum_i s_i u_i (x) vh[i]  (vh rows, unconjugated)
        alpha, beta = vh[0], vh[1]
        if l in L:
            ops = ops + embed3(np.outer(alpha, alpha.conj()), l)
        else:
            ops = ops + embed3(np.outer(alpha, alpha.conj()) + np.outer(beta, beta.conj()), l) / 2
    return ops


if __name__ == "__main__":
    mode, size, starts, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = np.random.default_rng(seed)
    L = tuple(range(size))
    f_op = pattern_op_arb if mode == "arb" else pattern_op_psi
    dim = (16 * size + 32 * (4 - size)) if mode == "arb" else 32
    for k in range(1, 5):
        best = -np.inf
        for _ in range(starts):
            r = minimize(lambda z: -(ky(f_op(z, L), k) - (3 + k)), rng.normal(size=dim), method="BFGS")
            best = max(best, -r.fun)
        print(f"mode={mode} |L|={size} k={k} max K_k(O_L) - (3+k) = {best:+.3e}", flush=True)
