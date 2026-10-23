"""Four-qubit depolarizing-output majorization (SWTF Eq. (2), d=2, n=4): exploration tools (floating point).

D_p(X) = (1-p) X + p Tr(X) I/2 applied to each qubit. Target spectrum (1-p/2, p/2)^{(x)4}.
Modes:
  calib   : Ky Fan gaps K_k(D(psi)) - K_k(D(0000)) for product, Bell(x)Bell, GHZ, W, linear cluster at p=1/2
  search  : multistart BFGS over pure psi (16 complex amplitudes), each k separately, given p
  blocks  : uniform size-s families X_s = sum_{|I|=s} rho_I (x) 1 vs T_s = sum_{|I|=s} |0..0><0..0|_I (x) 1 (Q=I/2);
            D_p^{(x)4} = sum_s (1-p)^s p^{4-s} 2^{-(4-s)} X_s, and the T_s are aligned by Hamming weight, so
            X_s <= T_s for s=2,3 (s=1: Kronecker-sum lemma; s=0,4 trivial) would prove all p in [0,1].
"""
import itertools
import json
import sys

import numpy as np
from scipy.optimize import minimize

N = 4


def apply_Dp(R, p, n=N):
    T = R.reshape([2] * (2 * n))
    for q in range(n):
        tr = np.trace(T, axis1=q, axis2=q + n)
        shape = [1] * (2 * n)
        shape[q] = 2
        shape[q + n] = 2
        full = np.expand_dims(np.expand_dims(tr, q), q + n) * np.eye(2).reshape(shape) / 2
        T = (1 - p) * T + p * full
    return T.reshape(2 ** n, 2 ** n)


def marginal_op(psi, I, n=N):
    """rho_I (x) 1_{I^c} as a 2^n x 2^n operator (qubit 0 most significant)."""
    T = psi.reshape([2] * n)
    rest = [l for l in range(n) if l not in I]
    M = np.tensordot(T, T.conj(), axes=(rest, rest))           # axes: I (ket), I (bra)
    k = len(I)
    # build operator: rho_I on positions I, identity elsewhere
    op = M.reshape(2 ** k, 2 ** k)
    big = op
    for _ in rest:
        big = np.kron(big, np.eye(2))
    order = list(I) + rest
    Tb = big.reshape([2] * (2 * n))
    perm = [order.index(l) for l in range(n)]
    Tb = Tb.transpose(perm + [x + n for x in perm])
    return Tb.reshape(2 ** n, 2 ** n)


def proj_op(I, n=N):
    P = np.ones(1)
    diag = []
    for x in itertools.product((0, 1), repeat=n):
        diag.append(1.0 if all(x[l] == 0 for l in I) else 0.0)
    return np.diag(diag)


def kf(M):
    e = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))[::-1]
    return np.cumsum(e)


def gap_dep(psi, p):
    R = np.outer(psi, psi.conj())
    e0 = np.zeros(2 ** N); e0[0] = 1
    return kf(apply_Dp(R, p)) - kf(apply_Dp(np.outer(e0, e0), p))


def gap_block(psi, s):
    subs = list(itertools.combinations(range(N), s))
    X = sum(marginal_op(psi, I) for I in subs)
    T = sum(proj_op(I) for I in subs)
    return kf(X) - kf(T)


def states():
    z = np.zeros(16, dtype=complex)
    out = {}
    s = z.copy(); s[0] = 1; out["product_0000"] = s
    bell = np.array([1, 0, 0, 1]) / np.sqrt(2)
    out["bell_x_bell"] = np.kron(bell, bell).astype(complex)
    g = z.copy(); g[0] = g[15] = 1 / np.sqrt(2); out["GHZ4"] = g
    w = z.copy()
    for q in range(4):
        w[1 << (3 - q)] = 0.5
    out["W4"] = w
    # linear cluster: CZ on (0,1),(1,2),(2,3) applied to |+>^4
    c = np.ones(16, dtype=complex) / 4
    for idx in range(16):
        bits = [(idx >> (3 - q)) & 1 for q in range(4)]
        sgn = (-1) ** (bits[0] * bits[1] + bits[1] * bits[2] + bits[2] * bits[3])
        c[idx] *= sgn
    out["linear_cluster4"] = c
    return out


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "calib":
        res = {}
        for name, psi in states().items():
            g = gap_dep(psi, 0.5)
            res[name] = {"max_gap_k1..15": float(g[:15].max()), "argmax_k": int(np.argmax(g[:15]) + 1),
                         "gaps": np.round(g[:15], 6).tolist()}
            print(name, res[name]["max_gap_k1..15"], res[name]["argmax_k"])
        e0 = np.zeros(16); e0[0] = 1
        print("target spectrum x256:", np.round(np.sort(np.linalg.eigvalsh(apply_Dp(np.outer(e0, e0), 0.5)))[::-1] * 256, 6))
        json.dump(res, open("../evidence/calibration_p_half.json", "w"), indent=1)
    elif mode in ("search", "blocks"):
        param = float(sys.argv[2])
        nst, seed = int(sys.argv[3]), int(sys.argv[4])
        rng = np.random.default_rng(seed)
        best = {"gap": -np.inf}
        for k in range(15):
            for _ in range(nst):
                if mode == "search":
                    f = lambda z: -gap_dep((z[:16] + 1j * z[16:]) / np.linalg.norm(z[:16] + 1j * z[16:]), param)[k]
                else:
                    f = lambda z: -gap_block((z[:16] + 1j * z[16:]) / np.linalg.norm(z[:16] + 1j * z[16:]), int(param))[k]
                r = minimize(f, rng.normal(size=32), method="BFGS")
                if -r.fun > best["gap"]:
                    best = {"gap": -r.fun, "k": k + 1, "z": r.x.tolist()}
        print(json.dumps({"mode": mode, "param": param, "starts_per_k": nst, "seed": seed,
                          "best_gap": best["gap"], "k": best["k"]}))
        json.dump(best, open(f"../evidence/{mode}_{param}_seed{seed}.json", "w"))
