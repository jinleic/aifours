"""Twirled PPT relaxation of sup_{sigma, Pi} Tr[Pi N(sigma)]  (N: LU-covariant map on 4 qubits; sigma a state;
0 <= Pi <= 1, Tr Pi = k) -> an LP in 16 variables c_S (S subset of qubits).

Write Tr[Pi N(sigma^T)] = Tr[(sigma (x) Pi) J], J = sum_ij |i><j| (x) N(|i><j|). Covariance N(U.U^dag) = U N(.) U^dag
(U a product of local unitaries) gives J commuting with conj(U) (x) U, whose commutant per site (sigma_l, Pi_l) is
span{Phi+, 1 - Phi+}. Twirling the relaxation variable omega (relaxing sigma (x) Pi) over the group therefore gives
omega = sum_S c_S E_S, E_S = (x)_l (Phi+ if l in S else 1 - Phi+), with valid constraints
  omega >= 0, sigma_tw (x) 1 - omega >= 0 (sigma_tw = 1/16), Tr omega = k, Tr_sigma omega <= 1,
  PPT: omega^{T_Pi} >= 0, (sigma_tw (x) 1 - omega)^{T_Pi} >= 0.
The LP optimum upper-bounds K_k(N(sigma)) over all states sigma. If it equals K_k(N(|0000><0000|)) for every k the
majorization is PROVED (after exact rational re-verification of the LP certificate).
Usage: python twirl_ppt_lp.py dep <p> | U <s>
"""
import itertools
import sys

import numpy as np
from scipy.optimize import linprog

from n4 import apply_Dp, kf, marginal_op, proj_op

n = 4
subsets = [S for r in range(n + 1) for S in itertools.combinations(range(n), r)]


def site_pair_ops():
    phi = np.zeros(4); phi[0] = phi[3] = 1 / np.sqrt(2)
    P = np.outer(phi, phi)
    return P, np.eye(4) - P


def reorder(M):
    """operators built as (x)_l (sigma_l, Pi_l) -> order (sigma_1..4, Pi_1..4)."""
    T = M.reshape([2] * 16)
    order = [0, 2, 4, 6, 1, 3, 5, 7]        # positions of sigma_l,Pi_l in pair ordering
    T = T.transpose(order + [o + 8 for o in order])
    return T.reshape(256, 256)


def basis():
    P, Q = site_pair_ops()
    out = []
    for S in subsets:
        M = np.ones((1, 1))
        for l in range(n):
            M = np.kron(M, P if l in S else Q)
        out.append(reorder(M))
    return out


def choi(N):
    J = np.zeros((256, 256), dtype=complex)
    for i in range(16):
        for j in range(16):
            E = np.zeros((16, 16)); E[i, j] = 1
            J += np.kron(E, N(E))
    return J


def g(inS, tau):
    return (0.5 if tau == 0 else -0.5) if inS else (0.5 if tau == 0 else 1.5)


def solve(N, target_kf):
    J = choi(N)
    E = basis()
    obj = np.array([np.trace(J @ e).real for e in E])
    trE = np.array([np.trace(e).real for e in E])
    trsig = np.array([(0.5) ** len(S) * 1.5 ** (n - len(S)) for S in subsets])
    ppt = np.array([[np.prod([g(l in S, tau[l]) for l in range(n)]) for S in subsets]
                    for tau in itertools.product((0, 1), repeat=n)])
    res = []
    for k in range(1, 16):
        A_ub = np.vstack([trsig[None, :], -ppt, ppt])
        b_ub = np.concatenate([[1.0], np.zeros(16), np.full(16, 1 / 16)])
        r = linprog(-obj, A_ub=A_ub, b_ub=b_ub, A_eq=trE[None, :], b_eq=[k],
                    bounds=[(0, 1 / 16)] * 16, method="highs")
        res.append((k, -r.fun, target_kf[k - 1], -r.fun - target_kf[k - 1]))
    return res


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "dep":
        p = float(sys.argv[2])
        N = lambda X: apply_Dp(X, p)
        e0 = np.zeros((16, 16)); e0[0, 0] = 1
        tk = kf(apply_Dp(e0, p))
    else:
        s = int(sys.argv[2])
        subs = list(itertools.combinations(range(n), s))

        def N(X):
            # Phi_s(X) = sum_{|I|=s} Tr_{I^c}(X) (x) 1_{I^c}
            out = np.zeros((16, 16), dtype=complex)
            T = X.reshape([2] * 8)
            for I in subs:
                rest = [l for l in range(n) if l not in I]
                R = T
                for cnt, l in enumerate(sorted(rest, reverse=True)):
                    R = np.trace(R, axis1=l, axis2=l + R.ndim // 2)
                k = len(I)
                op = R.reshape(2 ** k, 2 ** k)
                big = op
                for _ in rest:
                    big = np.kron(big, np.eye(2))
                order = list(I) + rest
                Tb = big.reshape([2] * 8)
                perm = [order.index(l) for l in range(n)]
                out += Tb.transpose(perm + [x + n for x in perm]).reshape(16, 16)
            return out
        tk = kf(sum(proj_op(I) for I in subs))
    for k, lp, t, gap in solve(N, tk):
        print(f"k={k:2d} LP={lp:.10f} target={t:.10f} gap={gap:+.3e}")
