#!/usr/bin/env python3
"""Float diagnostic: is the best two-atom law p delta_a+(1-p) delta_1 KKT-optimal?

For nu=p delta_a+(1-p)delta_1, Y=p B_a^2+(1-p)B_1^2.  KKT on (a,1) reduces to
Gamma<=2F with Gamma=2E[B_a B_1/sqrt Y]+(1-a)E[Y^(-1/2)].  Diagnostic only.
"""
import json
import numpy as np


def gl(m=3000):
    x, w = np.polynomial.legendre.leggauss(m)
    th = (x + 1) * np.pi / 4
    return np.tan(th), w * np.pi / 4 / np.cos(th) ** 2


U, WU = gl()


def moments(p, a):
    # Sigma=[[a,a],[a,1]], D=diag(p,1-p); vectorized 2x2 algebra over nodes U
    s2 = 2 * U * U
    q, r = p, 1 - p
    # M = I + s2*Sigma*D = [[1+s2*a*q, s2*a*r],[s2*a*q, 1+s2*r]]
    det = (1 + s2 * a * q) * (1 + s2 * r) - (s2 * a * r) * (s2 * a * q)
    vals = det ** -0.5
    # Cov_u = (Sigma^-1 + s2*D)^-1 ; Sigma^-1 = (1/(a(1-a)))[[1,-a],[-a,a]]
    k = 1.0 / (a * (1 - a))
    m11 = k + s2 * q
    m12 = -k * a
    m22 = k * a + s2 * r
    dm = m11 * m22 - m12 * m12
    c11, c22, c12 = m22 / dm, m11 / dm, -m12 / dm
    out = {}
    integ = np.where(U < 1e-8, p * a + (1 - p), (1 - vals) / np.maximum(U, 1e-300) ** 2)
    out['F'] = float(np.sum(integ * WU) / np.sqrt(np.pi))
    c = 2 / np.sqrt(np.pi)
    out['E_inv'] = float(c * np.sum(vals * WU))
    out['f_a'] = float(c * np.sum(vals * c11 * WU))
    out['f_1'] = float(c * np.sum(vals * c22 * WU))
    out['E_xy'] = float(c * np.sum(vals * c12 * WU))
    out['Gamma'] = 2 * out['E_xy'] + (1 - a) * out['E_inv']
    return out


def main():
    best = None
    for p in np.linspace(0.05, 0.6, 56):
        for a in np.linspace(0.3, 0.98, 69):
            F = moments(p, a)['F']
            if best is None or F > best[0]:
                best = (F, p, a)
    F0, p0, a0 = best
    # local refinement
    step_p, step_a = 0.005, 0.005
    for _ in range(60):
        improved = False
        for dp, da in [(step_p, 0), (-step_p, 0), (0, step_a), (0, -step_a)]:
            p1, a1 = p0 + dp, a0 + da
            if 0 < p1 < 1 and 0 < a1 < 1:
                F1 = moments(p1, a1)['F']
                if F1 > F0:
                    F0, p0, a0, improved = F1, p1, a1, True
        if not improved:
            step_p /= 2
            step_a /= 2
    m = moments(p0, a0)
    lam = np.linspace(0, 1, 11)
    f_interior = [float(m['F'] - l * (1 - l) * (2 * m['F'] - m['Gamma'])) for l in lam]
    print(json.dumps({'best_two_atom': {'p_at_a': float(p0), 'a': float(a0), **m},
                      'KKT_interior_requires_Gamma_le_2F': bool(m['Gamma'] <= 2 * m['F']),
                      'f_on_[a,1]_at_lambda_0..1_using_F_for_endpoints': f_interior,
                      'limits': 'Float quadrature/grid search diagnostic only; not a proof.'}, indent=1))


if __name__ == '__main__':
    main()
