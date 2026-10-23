"""Vectorised float numerics for the outer producer (search guidance only; never trusted).

Same objects as code/dual.py (pairing-dual D(y,n) = sum_u n^u Psi*(C_u y) + (3/2) sum_u n^u ln n^u)
and code/cert_cells.py (a_u from a rational mu0), batched over the nine classes.
"""
import itertools
import math

import numpy as np

FACT = [1, 1, 2, 6, 24, 120]


def _spectra():
    out = []
    for a, b, c in itertools.product(range(6), repeat=3):
        d = 5 - a - b - c
        if d < 0:
            continue
        if min(a + b, c + d) >= 1 and min(a + c, b + d) >= 1:
            out.append((a, b, c, d))
    return out


S_LIST = _spectra()
assert len(S_LIST) == 36
S = np.array(S_LIST, float)                      # (36, 4)
W = np.array([120 // (FACT[a] * FACT[b] * FACT[c] * FACT[d]) for (a, b, c, d) in S_LIST], float)
LW = np.log(W)
SS = (S[:, :, None] * S[:, None, :]).reshape(36, 16)
OFF = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
VERT = [(i, j) for i in range(3) for j in range(3)]
EDGES, _seen = [], set()
for _u, (_i, _j) in enumerate(VERT):          # identical construction/order to cert_cells.py
    for _k, (_r, _t) in enumerate(OFF):
        _v = 3 * ((_i + _r) % 3) + (_j + _t) % 3
        _kv = OFF.index((-_r, -_t))
        if (_u, _k) in _seen:
            continue
        _seen.add((_u, _k)); _seen.add((_v, _kv))
        EDGES.append((_u, _k, _v, _kv))
assert len(EDGES) == 18
C = np.zeros((9, 4, 18))
for _e, (_u, _k, _v, _kv) in enumerate(EDGES):
    C[_u, _k, _e] += 1.0
    C[_v, _kv, _e] -= 1.0
C36 = C.reshape(36, 18)
# scatter matrix: hess_flat(324) = (n^u R^u_{kl})_(u,k,l) (144) @ PH (144, 324)
PH = np.einsum('uki,ulj->uklij', C, C).reshape(144, 324)
B3 = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]], float)
I4 = np.eye(4)
LSTAR = 2.5 * math.log(5) + math.log(25 / 24)


def family(th):
    """th (9,4) -> p (9,36), logZ (9,), mh (9,4), V (9,4,4)."""
    zl = LW[None, :] + th @ S.T
    zm = zl.max(axis=1, keepdims=True)
    ez = np.exp(zl - zm)
    Z = ez.sum(axis=1, keepdims=True)
    p = ez / Z
    logZ = zm[:, 0] + np.log(Z[:, 0])
    mh = p @ S
    V = (p @ SS).reshape(-1, 4, 4) - mh[:, :, None] * mh[:, None, :]
    return p, logZ, mh, V


def gval(th, z, logZ, mh):
    return 0.5 * np.sum(mh * np.log(mh), axis=1) - np.sum(th * mh, axis=1) + logZ + np.sum(z * mh, axis=1)


def inner_batch(z, th0=None, tol=1e-14, maxit=200):
    """Psi*(z^u) for the nine rows of z (9,4). Returns (val (9,), mh (9,4), th (9,4), R (9,4,4), resid)."""
    nb = z.shape[0]
    th = np.zeros((nb, 4)) if th0 is None else np.array(th0, float)
    th = th - th.mean(axis=1, keepdims=True)
    p, logZ, mh, V = family(th)
    G = gval(th, z, logZ, mh)
    res = None
    for it in range(maxit):
        F = 0.5 * np.log(mh) - th + z
        Fc = F - F.mean(axis=1, keepdims=True)
        res = np.abs(Fc).max(axis=1)
        act = res >= tol
        if not act.any():
            break
        J = np.einsum('ki,ukl,lj->uij', B3, 0.5 * V / mh[:, :, None] - I4, B3)
        rhs = -(F @ B3)
        a = np.linalg.solve(J, rhs[:, :, None])[:, :, 0]
        step = a @ B3.T
        step[~act] = 0.0
        lam = np.ones(nb)
        for _ in range(60):
            tn = th + lam[:, None] * step
            pn, lzn, mhn, Vn = family(tn)
            Gn = gval(tn, z, lzn, mhn)
            ok = (Gn >= G - 1e-15 * np.abs(G)) | (lam < 1e-12) | ~act
            if ok.all():
                break
            lam = np.where(ok, lam, 0.5 * lam)
        th, mh, V, logZ, G = tn, mhn, Vn, lzn, Gn
    th = th - th.mean(axis=1, keepdims=True)
    p, logZ, mh, V = family(th)
    G = gval(th, z, logZ, mh)
    J = np.einsum('ki,ukl,lj->uij', B3, 0.5 * V / mh[:, :, None] - I4, B3)
    R = -np.einsum('ukl,lm,umn,pn->ukp', V, B3, np.linalg.inv(J), B3)
    R = 0.5 * (R + np.transpose(R, (0, 2, 1)))
    return G, mh, th, R, res


def ent(n9):
    """(3/2) sum_u n^u ln n^u for rows of n9 (..., 9), with 0 ln 0 = 0."""
    n9 = np.asarray(n9, float)
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(n9 > 0, n9 * np.log(np.where(n9 > 0, n9, 1.0)), 0.0)
    return 1.5 * t.sum(axis=-1)


def zmat(y):
    return (C36 @ y).reshape(9, 4)


def dual_eval(y, n9, th0=None):
    z = zmat(y)
    val, mh, th, R, res = inner_batch(z, th0)
    D = float(n9 @ val) + float(ent(n9))
    grad = (n9[:, None] * mh).reshape(36) @ C36
    hess = ((n9[:, None, None] * R).reshape(144) @ PH).reshape(18, 18)
    return D, grad, hess, th, mh, R, val


def solve_dual(n9, y0=None, th0=None, tol=1e-11, maxit=80):
    """Newton for min_y D(y, n9). Returns (D, y, |grad|, th, mh, R, val, iterations)."""
    y = np.zeros(18) if y0 is None else np.array(y0, float)
    D, g, H, th, mh, R, val = dual_eval(y, n9, th0)
    it = 0
    for it in range(maxit):
        if np.max(np.abs(g)) < tol:
            break
        try:
            step = -np.linalg.solve(H + 1e-13 * np.eye(18), g)
        except np.linalg.LinAlgError:
            step = -np.linalg.lstsq(H + 1e-13 * np.eye(18), g, rcond=None)[0]
        lam = 1.0
        while True:
            yn = y + lam * step
            Dn, gn, Hn, thn, mhn, Rn, valn = dual_eval(yn, n9, th)
            if Dn <= D + 1e-4 * lam * (g @ step) or lam < 1e-10:
                break
            lam *= 0.5
        y, D, g, H, th, mh, R, val = yn, Dn, gn, Hn, thn, mhn, Rn, valn
    return D, y, float(np.max(np.abs(g))), th, mh, R, val, it


def a_from_mu(z, mu):
    """Float replica of cert_cells.a_bound for the nine classes: z (9,4), mu (9,4) > 0."""
    lmu = np.log(mu)
    zl = LW[None, :] + lmu @ S.T
    zm = zl.max(axis=1, keepdims=True)
    d = np.exp(zl - zm)
    Zs = d.sum(axis=1)
    m0 = (d @ S) / Zs[:, None]
    lnZ = zm[:, 0] + np.log(Zs)
    lm0 = np.log(m0)
    psi0 = 0.5 * np.sum(m0 * lm0, axis=1) + lnZ - np.sum(lmu * m0, axis=1)
    g = 0.5 * lm0 - lmu + z
    T = np.max(g @ S.T - np.sum(g * m0, axis=1)[:, None], axis=1)
    return psi0 + np.sum(z * m0, axis=1) + T


def to_hex(a):
    return [float(v).hex() for v in np.ravel(a)]
