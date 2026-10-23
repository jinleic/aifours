"""Non-rigorous moment-based evaluator and gradient for candidate EXPLORATION.

Not a premise of any certified inequality. Uses the identities (proved in
notes/PROOF.md, Section 9) that Psi_T depends on rho only through the moments
c_h = E R^h:

    nu_i  = sum_h (-1)^h binom(i,h) c_h^(k-1),
    M_i   = exp(lambda (nu_i - 1)),  lambda = k alpha / 2,
    mu_j  = sum_i (-1)^i binom(j,i) M_i,
    -d_oo = sum_{h>=1} c_h^k / h,
    Psi_T = -sum_{j<=T} mu_j^2/j + (k-1) alpha sum_{h>=1} c_h^k/h.

Alternating sums are evaluated as forward-difference tables in fixed-point
integers with 2T+guard bits (nearest rounding, not directed). The reverse
(adjoint) pass gives d Psi / d c_h, hence gradients in atom locations and
weights. Floating optimisation then proposes candidate laws.
"""
import math

import mpmath
import numpy as np


class MomentEvaluator:
    def __init__(self, k, T, H=None, guard=192):
        self.k, self.T = k, T
        self.H = max(T, H or 0)
        self.P = 2 * T + guard
        self.ONE = 1 << self.P
        mpmath.mp.prec = self.P + 64

    # ---- helpers -------------------------------------------------------
    def to_fx(self, x):
        return int(mpmath.nint(mpmath.mpf(x) * self.ONE))

    def moments_fx(self, rates, weights):
        """c_h for h=0..H as fixed-point ints from float atoms."""
        P, ONE, H = self.P, self.ONE, self.H
        rs = [self.to_fx(r) for r in rates]
        ws = [self.to_fx(w) for w in weights]
        c = [0] * (H + 1)
        for r, w in zip(rs, ws):
            p = w
            for h in range(H + 1):
                c[h] += p
                p = (p * r) >> P
        return c

    @staticmethod
    def forward_diff(seq, n):
        """Return [(Delta^j seq)_0 for j=0..n] with Delta u_i = u_i - u_{i+1}."""
        row = list(seq[: n + 1])
        out = [row[0]]
        for _ in range(n):
            row = [row[i] - row[i + 1] for i in range(len(row) - 1)]
            out.append(row[0])
        return out

    @staticmethod
    def adjoint_diff(g, n):
        """Given g_j (j=0..n), return a_i = sum_j g_j (-1)^i binom(j,i)."""
        # Horner: v = g_n e0; for j=n-1..0: v = (1-S) v + g_j e0
        v = [g[n]]
        for j in range(n - 1, -1, -1):
            w = [0] * (len(v) + 1)
            for i, x in enumerate(v):
                w[i] += x
                w[i + 1] -= x
            w[0] += g[j]
            v = w
        return v  # length n+1

    # ---- evaluation ----------------------------------------------------
    def evaluate(self, rates, weights, alpha, grad=False):
        k, T, P, ONE, H = self.k, self.T, self.P, self.ONE, self.H
        c = self.moments_fx(rates, weights)
        # e_h = c_h^(k-1)
        e = []
        for x in c[: T + 1]:
            y = ONE
            for _ in range(k - 1):
                y = (y * x) >> P
            e.append(y)
        nu = self.forward_diff(e, T)
        lam = mpmath.mpf(k) * mpmath.mpf(alpha) / 2
        M = []
        for i in range(T + 1):
            M.append(int(mpmath.nint(mpmath.exp(lam * (mpmath.mpf(nu[i]) / ONE - 1)) * ONE)))
        mu = self.forward_diff(M, T)
        site = mpmath.mpf(0)
        for j in range(1, T + 1):
            site += mpmath.mpf(mu[j]) ** 2 / j
        site /= mpmath.mpf(ONE) ** 2
        dval, d_gr, d_gw = clause_enum(rates, weights, k)
        clause = -(k - 1) * alpha * dval
        psi = float(-site) + clause
        if not grad:
            return psi, dict(site=float(site), clause=clause,
                             mu=[m / ONE for m in mu])
        # ---- adjoint pass: dPsi/dc_h -----------------------------------
        # dPsi/dmu_j = -2 mu_j / j   (fixed point)
        g_mu = [0] + [-(2 * mu[j]) // j for j in range(1, T + 1)]
        g_M = self.adjoint_diff(g_mu, T)          # dPsi/dM_i, fixed point
        lam_fx = self.to_fx(lam)
        g_nu = [((((g_M[i] * M[i]) >> P) * lam_fx) >> P) for i in range(T + 1)]
        g_e = self.adjoint_diff(g_nu, T)          # dPsi/de_h
        # dPsi/dc_h (site part only) as fixed-point integers
        G = []
        for h in range(T + 1):
            pw = ONE
            for _ in range(k - 2):
                pw = (pw * c[h]) >> P
            G.append((g_e[h] * pw * (k - 1)) >> P)
        g_r = np.zeros(len(rates))
        g_w = np.zeros(len(rates))
        for t, (r, w) in enumerate(zip(rates, weights)):
            rf = self.to_fx(r)
            acc_w, acc_r = 0, 0
            pw = ONE          # r^h
            prevpow = 0       # r^(h-1)
            for h in range(T + 1):
                acc_w += G[h] * pw
                acc_r += G[h] * h * prevpow
                prevpow = pw
                pw = (pw * rf) >> P
            g_w[t] = acc_w / (ONE * ONE)
            g_r[t] = float(w) * (acc_r / (ONE * ONE))
        g_w += -(k - 1) * alpha * d_gw
        g_r += -(k - 1) * alpha * d_gr
        return psi, g_r, g_w


def clause_enum(rates, weights, k):
    """d = E log(1 - R_1...R_k) and its gradient (float64, ordered tuples).

    Returns (d, dd/dr_t, dd/dw_t) treating weights as free (unnormalised)."""
    r = np.asarray(rates, float)
    w = np.asarray(weights, float)
    m = len(r)
    if m ** k > 2_000_000:
        # d = -sum_h c_h^k / h with c_h = E R^h (all terms of one sign)
        rmax = float(r.max())
        H = int(min(200000, max(50, np.ceil(np.log(1e-19) / (k * np.log(rmax))))))
        hs = np.arange(1, H + 1)
        logr = np.log(r)
        P = np.exp(np.outer(hs, logr))            # H x m, r_t^h
        c = P @ w                                   # c_h
        d = -float(np.sum(c ** k / hs))
        coef = k * c ** (k - 1) / hs                # dd/dc_h = -coef
        gw = -(coef @ P)
        gr = -w * ((coef * hs) @ (P / r))
        return d, gr, gw
    # law of Q = R_2...R_k over ordered (k-1)-tuples
    qv = np.ones(1)
    qw = np.ones(1)
    for _ in range(k - 1):
        qv = np.outer(qv, r).ravel()
        qw = np.outer(qw, w).ravel()
    z = np.outer(r, qv)                 # m x m^(k-1)
    L = np.log1p(-z)
    d = float(np.dot(w, L @ qw))
    gw = k * (L @ qw)                    # dd/dw_t = k E log(1 - r_t Q)
    gr = k * w * ((-qv / (1.0 - z)) @ qw)
    return d, gr, gw


def unpack(theta, m):
    a, b = theta[:m], theta[m:]
    rates = 1.0 / (1.0 + np.exp(-a))
    bb = b - b.max()
    ex = np.exp(bb)
    weights = ex / ex.sum()
    return rates, weights


def pack(rates, weights):
    rates = np.asarray(rates, float)
    weights = np.asarray(weights, float)
    return np.concatenate([np.log(rates / (1 - rates)), np.log(weights)])


def objective(ev, theta, m, alpha):
    rates, weights = unpack(theta, m)
    psi, g_r, g_w = ev.evaluate(list(rates), list(weights), alpha, grad=True)
    # chain rule
    da = g_r * rates * (1 - rates)
    gw_mean = float(np.dot(g_w, weights))
    db = weights * (g_w - gw_mean)
    return psi, np.concatenate([da, db])


def bfgs(ev, theta0, m, alpha, iters=200, gtol=1e-10, verbose=False):
    theta = np.array(theta0, float)
    f, g = objective(ev, theta, m, alpha)
    n = len(theta)
    Hinv = np.eye(n) * 0.1
    for it in range(iters):
        p = -Hinv @ g
        if np.dot(p, g) >= 0:
            Hinv = np.eye(n) * 0.1
            p = -Hinv @ g
        step = 1.0
        while True:
            th2 = theta + step * p
            f2, g2 = objective(ev, th2, m, alpha)
            if f2 <= f + 1e-4 * step * np.dot(g, p) or step < 1e-8:
                break
            step *= 0.5
        s = th2 - theta
        yv = g2 - g
        sy = float(np.dot(s, yv))
        theta, fold, f, g = th2, f, f2, g2
        if sy > 1e-30:
            rho = 1.0 / sy
            I = np.eye(n)
            Hinv = (I - rho * np.outer(s, yv)) @ Hinv @ (I - rho * np.outer(yv, s)) + rho * np.outer(s, s)
        gn = float(np.max(np.abs(g)))
        if verbose and it % 10 == 0:
            print(it, f, gn, step, flush=True)
        if gn < gtol or abs(fold - f) < 1e-16:
            break
    return theta, f, g
