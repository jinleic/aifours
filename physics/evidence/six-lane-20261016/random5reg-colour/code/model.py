"""Core objects for the Diaz-Kaporis-Kemkes-Kirousis-Perez-Wormald Maximum Hypothesis.

Conventions (preprint sections 4, 5.1, 7):
  * a 2x2 matrix is stored as a 4-vector in the order (-1,-1), (-1,1), (1,-1), (1,1),
    i.e. (x, y, z, w) in Phi(x y; z w);
  * vertex u = (i, j) in Z3 x Z3 has index 3*i + j;
  * m^{ij}_{r,t} is the scaled number of points of class (i,j) matched into class (i+r, j+t);
    pairing (4.3): m^{ij}_{r,t} = m^{i+r,j+t}_{-r,-t}.  The 36 matching variables therefore
    collapse to 18 edge weights x_e on the tensor product K3 x K3.
"""
from __future__ import annotations

import itertools
import math

import numpy as np

OFFSETS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # entry order of a 2x2 matrix


def spectra(deg: int = 5, rainbow: bool = True):
    """All 2x2 nonnegative integer matrices with entry sum deg (row/col sums >= 1 if rainbow)."""
    out = []
    for a, b, c in itertools.product(range(deg + 1), repeat=3):
        d = deg - a - b - c
        if d < 0:
            continue
        s = (a, b, c, d)
        if rainbow:
            rows = (a + b, c + d)
            cols = (a + c, b + d)
            if min(rows) < 1 or min(cols) < 1:
                continue
        out.append(s)
    return out


def multinomial(s):
    n = sum(s)
    r = math.factorial(n)
    for k in s:
        r //= math.factorial(k)
    return r


class Model:
    def __init__(self, deg: int = 5, rainbow: bool = True):
        self.deg = deg
        self.rainbow = rainbow
        self.S = spectra(deg, rainbow)
        self.Sarr = np.array(self.S, dtype=float)  # (|S|, 4)
        self.w = np.array([multinomial(s) for s in self.S], dtype=float)
        self.logw = np.log(self.w)
        # K3 x K3 structure
        self.vertices = [(i, j) for i in range(3) for j in range(3)]
        self.edges = []  # (u, k_u, v, k_v): m^u[k_u] = m^v[k_v] = x_e
        seen = {}
        for u, (i, j) in enumerate(self.vertices):
            for k, (r, t) in enumerate(OFFSETS):
                v = 3 * ((i + r) % 3) + ((j + t) % 3)
                kv = OFFSETS.index((-r, -t))
                key = (min(u, v), max(u, v), (k, kv) if u < v else (kv, k))
                if (u, k) in seen:
                    continue
                e = len(self.edges)
                self.edges.append((u, k, v, kv))
                seen[(u, k)] = e
                seen[(v, kv)] = e
        assert len(self.edges) == 18
        # incidence: m (9x4 flattened, index 4u+k) = E @ x
        self.E = np.zeros((36, 18))
        for e, (u, k, v, kv) in enumerate(self.edges):
            self.E[4 * u + k, e] = 1.0
            self.E[4 * v + kv, e] = 1.0
        assert np.all(self.E.sum(axis=1) == 1)

    # ---------- per-vertex function psi via the mu-system (evaluator B) ----------
    def theta_from_m(self, m, theta0=None, tol=1e-14, maxit=500):
        """Solve sum_s s w_s exp(<s,theta>) = m for theta = ln mu (m in the open cone).

        Works on the normalised slice (exponential family p_s ~ w_s e^{<s,th>}, E_p s = m/c,
        c = sum m / deg) with a log-sum-exp stabilised damped Newton method, then rescales by
        homogeneity (sum_rt s_rt = deg for every spectrum)."""
        S, lw, deg = self.Sarr, self.logw, self.deg
        m = np.asarray(m, float)
        c = m.sum() / deg
        mh = m / c
        th = np.zeros(4) if theta0 is None else np.array(theta0, float) - np.mean(theta0)

        def logZ(t):
            z = lw + S @ t
            zm = z.max()
            return zm + math.log(np.exp(z - zm).sum()), z

        f = logZ(th)[0] - mh @ th
        for it in range(maxit):
            lz, z = logZ(th)
            p = np.exp(z - lz)
            mean = S.T @ p
            g = mean - mh
            if np.max(np.abs(g) / mh) < tol:
                break
            Cov = (S.T * p) @ S - np.outer(mean, mean)
            # Cov is singular along the all-ones direction; regularise that direction only
            try:
                step = np.linalg.solve(Cov + np.ones((4, 4)), -g)
            except np.linalg.LinAlgError:
                step = np.linalg.lstsq(Cov + np.ones((4, 4)), -g, rcond=None)[0]
            step -= step.mean()
            lam = 1.0
            while True:
                tn = th + lam * step
                fn = logZ(tn)[0] - mh @ tn
                if fn <= f + 1e-4 * lam * (g @ step) or lam < 1e-14:
                    break
                lam *= 0.5
            if fn > f:
                break
            th, f = tn, fn
        lz, _ = logZ(th)
        return th + (math.log(c) - lz) / deg

    def psi(self, m, theta0=None):
        """psi(m) = sum m (ln m / 2 - ln mu); returns (psi, grad, theta).  m in the open cone."""
        m = np.asarray(m, float)
        th = self.theta_from_m(m, theta0)
        val = float(m @ (0.5 * np.log(m) - th))
        grad = 0.5 * np.log(m) - th + (0.5 - 1.0 / self.deg)
        return val, grad, th

    def psi_hess(self, m, theta=None):
        m = np.asarray(m, float)
        if theta is None:
            theta = self.theta_from_m(m)
        d = np.exp(self.logw + self.Sarr @ theta)
        S2 = (self.Sarr.T * d) @ self.Sarr
        return 0.5 * np.diag(1.0 / m) - np.linalg.inv(S2)

    # ---------- per-vertex primal evaluation (evaluator A, no mu-system) ----------
    def H_primal_gis(self, m, iters=20000, tol=1e-15):
        """max sum_s d_s ln(w_s/d_s) s.t. sum_s d_s s = m via generalized iterative scaling."""
        S, w = self.Sarr, self.w
        m = np.asarray(m, float)
        tot = m.sum() / self.deg
        d = w / w.sum() * tot
        for it in range(iters):
            mm = S.T @ d
            ratio = m / mm
            d = d * np.exp((S @ np.log(ratio)) / self.deg)
            if np.max(np.abs(ratio - 1)) < tol:
                break
        mm = S.T @ d
        val = float(np.sum(d * (np.log(w) - np.log(d))))
        return val, d, float(np.max(np.abs(mm - m) / m))

    # ---------- whole-configuration objective ----------
    def m_from_x(self, x):
        return (self.E @ x).reshape(9, 4)

    def L(self, x, thetas=None):
        """Objective L(x) = sum_u psi(m^u) (cold-started mu-solver unless thetas given; a global
        warm-start cache was tried and removed: it corrupted runs after infeasible SLSQP iterates)."""
        M = self.m_from_x(x)
        tot, g = 0.0, np.zeros(36)
        th_out = []
        for u in range(9):
            v, gr, th = self.psi(M[u], None if thetas is None else thetas[u])
            tot += v
            g[4 * u:4 * u + 4] = gr
            th_out.append(th)
        return tot, self.E.T @ g, th_out

    def n_from_x(self, x):
        return self.m_from_x(x).sum(axis=1) / self.deg


def nine_from_four(n4):
    n1, n2, n3, n4_ = n4
    return np.array([
        n1, n2, 1 / 3 - n1 - n2,
        n3, n4_, 1 / 3 - n3 - n4_,
        1 / 3 - n1 - n3, 1 / 3 - n2 - n4_, n1 + n2 + n3 + n4_ - 1 / 3,
    ])


def cone_rows(model: Model):
    """Linear inequalities G m^u >= 0 describing the cone (5.4) for one vertex (4-vector)."""
    q = model.deg - 1
    rows = []
    # row sums: R_-1 = m0+m1, R_1 = m2+m3 ; need R_a <= q R_b
    rows.append([q, q, -1, -1])   # q*R_-1 - R_1 >= 0
    rows.append([-1, -1, q, q])   # q*R_1 - R_-1 >= 0
    rows.append([q, -1, q, -1])   # q*C_-1 - C_1 >= 0 (C_-1 = m0+m2)
    rows.append([-1, q, -1, q])
    for k in range(4):
        e = [0, 0, 0, 0]
        e[k] = 1
        rows.append(e)
    return np.array(rows, float)


if __name__ == "__main__":
    mod = Model()
    print("|S| =", len(mod.S), " sum w =", mod.w.sum(), " prod w =", math.prod(int(x) for x in mod.w))
    # centre anchors
    mstar = np.full(4, 5 / 36)
    v, g, th = mod.psi(mstar)
    mu = np.exp(th)
    print("mu* =", mu, " (1/8100)^(1/5) =", (1 / 8100) ** 0.2)
    Lc = 9 * v
    print("ln F(n*) =", Lc, " expected", 2.5 * math.log(5) + math.log(25 / 24), " F =", math.exp(Lc))
    hv, d, err = mod.H_primal_gis(mstar)
    print("GIS H(m*) =", hv, " mu-system H =", -float(mstar @ th), " gis resid", err)
