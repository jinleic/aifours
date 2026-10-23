"""U2(n=4) via a new spin-flip decomposition (generalizing Song-Chen's eq. (31) argument from n=3 to n=4).

Identity (any 4-qubit pure psi, rho = |psi><psi|, psi~ = s_y^{(x)4} conj(psi), rho~ = |psi~><psi~|):
    X_2 = (2 X_1 - 3*1) + rho + (X_3(psi~) - rho~),      X_3(psi~) - rho~ >= rho~ >= 0,
with X_s = sum_{|I|=s} rho_I (x) 1. Hence (Weyl) lambda_i(X_2) >= h_i, h = spectrum of the Kronecker sum
2 X_1 - 3 = 2 sum_l rho_l (x) 1 - 3, explicit in the local spectra (1-r_l, r_l), and lambda_i(X_2) >= 0, so
    K_k(X_2) <= 24 - sum_{i>k} max(h_i, 0).
Mode `identity`: numerical check of the identity on random states.
Mode `bound`: worst value of [bound - K_k(T_2)] over a grid of r in [0,1/2]^4, with/without polygon inequalities.
"""
import itertools
import sys

import numpy as np

from n4 import marginal_op, kf, proj_op

SY = np.array([[0, -1j], [1j, 0]])
S4 = np.kron(np.kron(SY, SY), np.kron(SY, SY))


def Xs(psi, s):
    return sum(marginal_op(psi, I) for I in itertools.combinations(range(4), s))


def T2_ky():
    T = sum(proj_op(I) for I in itertools.combinations(range(4), 2))
    return kf(T)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "identity":
        rng = np.random.default_rng(5)
        for t in range(5):
            psi = rng.normal(size=16) + 1j * rng.normal(size=16)
            psi /= np.linalg.norm(psi)
            pt = S4 @ psi.conj()
            rho, rt = np.outer(psi, psi.conj()), np.outer(pt, pt.conj())
            rhs = 2 * Xs(psi, 1) - 3 * np.eye(16) + rho + Xs(pt, 3) - rt
            print("identity err", np.abs(Xs(psi, 2) - rhs).max(),
                  "min eig(X3(psi~)-rho~)", np.linalg.eigvalsh(Xs(pt, 3) - rt).min())
    else:
        grid = int(sys.argv[2])
        Ky = T2_ky()
        rs = np.linspace(0, 0.5, grid + 1)
        worst = {"poly": (-np.inf, None), "all": (-np.inf, None)}
        perk = {k: (-np.inf, None) for k in range(1, 16)}
        xs = list(itertools.product((0, 1), repeat=4))
        for r in itertools.product(rs, repeat=4):
            if not (r[0] <= r[1] <= r[2] <= r[3]):
                continue                     # symmetric in permutations of qubits
            poly = all(r[l] <= sum(r) - r[l] + 1e-12 for l in range(4))
            h = np.sort([2 * sum((r[l] if x[l] else 1 - r[l]) for l in range(4)) - 3 for x in xs])[::-1]
            for k in range(1, 16):
                ub = 24 - np.maximum(h[k:], 0).sum()
                g = ub - Ky[k - 1]
                if poly and g > perk[k][0]:
                    perk[k] = (g, r)
                for key in (["poly", "all"] if poly else ["all"]):
                    if g > worst[key][0]:
                        worst[key] = (g, (k, r))
        print({k: (float(v[0]), v[1][0], [float(x) for x in v[1][1]]) for k, v in worst.items()})
        for k in range(1, 16):
            print("k", k, "worst (bound - K_k(T2)) under polygon:", round(float(perk[k][0]), 6),
                  "at r", [float(x) for x in perk[k][1]])
