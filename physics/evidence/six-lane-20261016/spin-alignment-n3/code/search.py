"""Song-Chen arXiv:2603.25410v1 Conjecture 2 at n=3, d=2: numerical violation search (exploratory).

X = sum_I mu_I rho_I (x) Q^{(x)I^c},  Y = sum_I mu_I |0><0|^{(x)I} (x) Q^{(x)I^c},  Q = diag(q, 1-q), q >= 1/2.
Ky Fan sums K_k are convex and X is affine in rho, so pure global states suffice. Objective: max_k (K_k(X) - K_k(Y)).
A positive value is only a CANDIDATE; exact rational certification is separate (certify.py).
Controls: strong-conjecture counterexample (independent pair states) gives K_3 = 0.83440 > 5/6; Prop. 3 setting
(Q = I/2, mu on pairs) must give no violation.
"""
import itertools
import json
import sys

import numpy as np
from scipy.optimize import minimize

SUBSETS = [tuple(s) for r in range(4) for s in itertools.combinations(range(3), r)]  # 8 subsets of {0,1,2}


def embed(op_I, I, Q):
    """Operator on 3 qubits (qubit 0 = A most significant): op_I on positions I (in increasing order), Q elsewhere."""
    rest = [l for l in range(3) if l not in I]
    full = np.kron(op_I, np.kron(np.kron(Q, Q) if len(rest) == 2 else (Q if len(rest) == 1 else np.eye(1)), np.eye(1))) \
        if False else None
    # build by permuting tensor factors: start with op_I (x) Q^{(x)|rest|} in order I + rest, then permute to A,B,C
    T = op_I
    for _ in rest:
        T = np.kron(T, Q)
    order = list(I) + rest
    T = T.reshape([2] * 6)
    perm = [order.index(l) for l in range(3)]
    T = T.transpose(perm + [p + 3 for p in perm])
    return T.reshape(8, 8)


def marginal(psi, I):
    T = psi.reshape(2, 2, 2)
    rest = [l for l in range(3) if l not in I]
    M = np.tensordot(T, T.conj(), axes=(rest, rest))  # indices: I (ket), I (bra)
    d = 2 ** len(I)
    return M.reshape(d, d)


def XY(psi, mu, q):
    Q = np.diag([q, 1 - q])
    P0 = np.diag([1.0, 0.0])
    X = np.zeros((8, 8), dtype=complex)
    Y = np.zeros((8, 8))
    for m, I in zip(mu, SUBSETS):
        rI = marginal(psi, I) if len(I) else np.eye(1)
        X += m * embed(rI, I, Q)
        PI = np.eye(1)
        for _ in I:
            PI = np.kron(PI, P0)
        Y += m * embed(PI, I, Q).real
    return X, Y


def kyfan_gap(X, Y):
    ex = np.sort(np.linalg.eigvalsh((X + X.conj().T) / 2))[::-1]
    ey = np.sort(np.diag(Y))[::-1]
    return np.cumsum(ex)[:7] - np.cumsum(ey)[:7]


def unpack(z, fix_q=None, support=None):
    psi = z[:8] + 1j * z[8:16]
    psi = psi / np.linalg.norm(psi)
    w = np.exp(z[16:24] - z[16:24].max())
    if support is not None:
        w = w * support
    mu = w / w.sum()
    q = fix_q if fix_q is not None else 0.5 + 0.5 / (1 + np.exp(-z[24]))
    return psi, mu, q


def run(n_starts, seed, fix_q=None, support=None):
    rng = np.random.default_rng(seed)
    best = (-np.inf, None)
    for s in range(n_starts):
        z0 = rng.normal(size=25)
        f = lambda z: -np.max(kyfan_gap(*XY(*unpack(z, fix_q, support))))
        r = minimize(f, z0, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-13})
        r = minimize(f, r.x, method="BFGS")
        if -r.fun > best[0]:
            best = (-r.fun, r.x)
    psi, mu, q = unpack(best[1], fix_q, support)
    gaps = kyfan_gap(*XY(psi, mu, q))
    return best[0], psi, mu, q, gaps


def control_strong():
    """Independent pair states (Conjecture 1): must reproduce K_3 = 0.83440 > 5/6."""
    ab = np.array([0, 6, -9, -10]) / np.sqrt(217)
    ac = np.array([-2, -4, -1, 5]) / np.sqrt(46)
    bc = np.array([-6, -1, -4, 0]) / np.sqrt(53)
    Q = np.eye(2) / 2
    H = (embed(np.outer(ab, ab), (0, 1), Q) + embed(np.outer(ac, ac), (0, 2), Q) + embed(np.outer(bc, bc), (1, 2), Q)) / 3
    ev = np.sort(np.linalg.eigvalsh(H))[::-1]
    return float(ev[:3].sum())


if __name__ == "__main__":
    mode = sys.argv[1]
    n, seed = int(sys.argv[2]), int(sys.argv[3])
    if mode == "control":
        print(json.dumps({"strong_counterexample_K3": control_strong(), "target_K3": 5 / 6}))
        pairs = np.array([1.0 if len(I) == 2 else 0.0 for I in SUBSETS])
        v = run(n, seed, fix_q=0.5, support=pairs)
        print(json.dumps({"prop3_setting_max_gap": v[0], "gaps": v[4].tolist()}))
    elif mode == "interior":
        # interior (mu, q): mu ~ Dirichlet(1) on all 8 subsets, q ~ U[0.5, 1); maximize over psi only, each Ky Fan
        # index k separately (avoids drifting to trivial equality vertices)
        rng = np.random.default_rng(seed)
        best = {"gap": -np.inf}
        for s in range(n):
            alpha = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
            mu = rng.dirichlet(np.ones(8) * alpha)
            q = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != "rand" else 0.5 + 0.5 * rng.random()
            for k in range(7):
                f = lambda z: -kyfan_gap(*XY((z[:8] + 1j * z[8:]) / np.linalg.norm(z[:8] + 1j * z[8:]), mu, q))[k]
                for _ in range(2):
                    r = minimize(f, rng.normal(size=16), method="BFGS")
                    if -r.fun > best["gap"]:
                        best = {"gap": -r.fun, "k": k + 1, "mu": mu.tolist(), "q": q, "z": r.x.tolist()}
        print(json.dumps({"mode": mode, "seed": seed, "samples": n, **best}))
    else:
        v = run(n, seed)
        print(json.dumps({"mode": mode, "seed": seed, "starts": n, "max_gap": v[0], "gaps": v[4].tolist(),
                          "q": v[3], "mu": v[2].tolist(),
                          "psi_re": v[1].real.tolist(), "psi_im": v[1].imag.tolist()}))
