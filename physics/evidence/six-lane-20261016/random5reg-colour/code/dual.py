"""Lagrangian (pairing-dual) evaluation of F(n).

For edge multipliers y (18) put z^u = C_u y (4-vector per class u).  Weak duality, valid for
every y and every n (no concavity needed):
    ln F(n) <= D(y, n) = sum_u [ n^u Psi*(z^u) + (3/2) n^u ln n^u ],
    Psi*(z) = max_{mhat in M0(1)} psi(mhat) + <z, mhat>     (M0(1): 2x2 cone slice, entry sum 5).
Slice concavity (proved exactly, evidence/slice_poly.json) + Slater give equality at the optimal y.
Inner problem solved by Newton in the exponential-family parameter theta (unconstrained).
"""
import sys, math
import numpy as np
sys.path.insert(0, 'code')
from model import Model

MOD = Model(5, True)
S = MOD.Sarr
LW = MOD.logw
B3 = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]], float)  # basis of 1-perp
C = np.zeros((9, 4, 18))
for e, (u, k, v, kv) in enumerate(MOD.edges):
    C[u, k, e] += 1.0
    C[v, kv, e] -= 1.0


def family(theta):
    z = LW + S @ theta
    zm = z.max()
    ez = np.exp(z - zm)
    Z = ez.sum()
    p = ez / Z
    logZ = zm + math.log(Z)
    mh = S.T @ p
    V = (S.T * p) @ S - np.outer(mh, mh)
    return p, logZ, mh, V


def g_val(theta, z):
    p, logZ, mh, V = family(theta)
    return 0.5 * mh @ np.log(mh) - theta @ mh + logZ + z @ mh, mh


def inner(z, theta0=None, tol=1e-13, maxit=200):
    """Psi*(z) and maximiser.  Returns (value, mhat, theta, R) with R = d mhat / d z (4x4 PSD)."""
    th = np.zeros(4) if theta0 is None else np.array(theta0, float)
    th -= th.mean()
    gv, _ = g_val(th, z)
    for it in range(maxit):
        p, logZ, mh, V = family(th)
        F = 0.5 * np.log(mh) - th + z
        Fp = B3.T @ F
        if np.max(np.abs(F - F.mean())) < tol:
            break
        J = B3.T @ (0.5 * (V / mh[:, None]) - np.eye(4)) @ B3
        a = np.linalg.solve(J, -Fp)
        step = B3 @ a
        lam = 1.0
        while lam > 1e-12:
            tn = th + lam * step
            gn, _ = g_val(tn, z)
            if gn >= gv - 1e-15 * abs(gv):
                break
            lam *= 0.5
        th, gv = tn, gn
    p, logZ, mh, V = family(th)
    # R = d mhat/dz:  from P(0.5 ln m - theta + z) = 0 with dm = V dtheta:
    #   (0.5 D^{-1} V - I) dtheta = -dz (mod 1)  ->  dm = V dtheta
    Jfull = B3.T @ (0.5 * (V / mh[:, None]) - np.eye(4)) @ B3
    R = -V @ B3 @ np.linalg.solve(Jfull, B3.T)
    R = 0.5 * (R + R.T)
    return gv, mh, th, R


def D_and_derivs(y, n9, thetas=None):
    val = 1.5 * sum(nu * math.log(nu) for nu in n9 if nu > 0)
    grad = np.zeros(18)
    hess = np.zeros((18, 18))
    th_out, mh_out = [], []
    for u in range(9):
        z = C[u] @ y
        gv, mh, th, R = inner(z, None if thetas is None else thetas[u])
        th_out.append(th); mh_out.append(mh)
        if n9[u] <= 0:
            continue
        val += n9[u] * gv
        grad += n9[u] * (C[u].T @ mh)
        hess += n9[u] * (C[u].T @ R @ C[u])
    return val, grad, hess, th_out, mh_out


def solve_dual(n9, y0=None, tol=1e-12, maxit=100, verbose=False):
    y = np.zeros(18) if y0 is None else np.array(y0, float)
    val, grad, hess, ths, mhs = D_and_derivs(y, n9)
    for it in range(maxit):
        if np.max(np.abs(grad)) < tol:
            break
        step = -np.linalg.lstsq(hess + 1e-14 * np.eye(18), grad, rcond=None)[0]
        lam = 1.0
        while lam > 1e-10:
            yn = y + lam * step
            vn, gn, hn, tn, mn = D_and_derivs(yn, n9, ths)
            if vn <= val + 1e-4 * lam * (grad @ step):
                break
            lam *= 0.5
        y, val, grad, hess, ths, mhs = yn, vn, gn, hn, tn, mn
        if verbose:
            print(it, val, np.max(np.abs(grad)), lam)
    return val, y, np.max(np.abs(grad)), ths, mhs


if __name__ == '__main__':
    Lstar = 2.5 * math.log(5) + math.log(25 / 24)
    I3 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]) / 3
    Cn = np.full(9, 1 / 9)
    y = None
    for t in [0.0, 0.2, 0.5, 0.8, 0.9, 0.95, 0.97, 0.98, 0.985, 0.99, 0.995, 0.999]:
        n9 = (1 - t) * Cn + t * I3
        val, y, gres, ths, mhs = solve_dual(n9, y)
        print(f't={t:6.3f} n_off={n9[1]:.5f} lnF={val:.10f} gap={Lstar - val:.6f} |grad|={gres:.1e}')
