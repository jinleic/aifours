#!/usr/bin/env python3
"""Float Frank-Wolfe diagnostic for F(nu)=E sqrt(int B_s^2 nu(ds)) on a time grid.

Diagnostic only: floating quadrature and a finite grid; it proves nothing about the
continuum optimizer nu*, its atom at 1, or kappa.
"""
import json
import numpy as np

N_GRID = 60
THETA = None
WEIGHTS = None


def nodes(m=1600):
    x, w = np.polynomial.legendre.leggauss(m)
    th = (x + 1) * np.pi / 4.0          # (0, pi/2)
    return np.tan(th), w * np.pi / 4.0 / np.cos(th) ** 2


def setup(n):
    s = np.arange(1, n + 1) / n
    sig = np.minimum.outer(s, s)
    return s, sig


def value_and_kkt(p, sig, u, wu):
    n = len(p)
    sq = np.sqrt(p)
    m = sq[:, None] * sig * sq[None, :]
    lam = np.clip(np.linalg.eigvalsh(m), 0.0, None)
    # F = (1/sqrt(pi)) int_0^inf (1-prod(1+2u^2 lam)^(-1/2))/u^2 du
    prod = np.prod(1.0 / np.sqrt(1.0 + 2.0 * np.outer(u ** 2, lam)), axis=1)
    small = u < 1e-6
    integrand = np.where(small, lam.sum(), (1.0 - prod) / np.where(small, 1.0, u ** 2))
    val = float(np.sum(integrand * wu) / np.sqrt(np.pi))
    # f_j = (2/sqrt(pi)) int_0^inf det(I+2u^2 Sig D)^(-1/2) [ (Sig^-1+2u^2 D)^-1 ]_jj du
    siginv = np.linalg.inv(sig)
    f = np.zeros(n)
    for uk, wk, pk in zip(u, wu, prod):
        cov = np.linalg.inv(siginv + 2.0 * uk ** 2 * np.diag(p))
        f += wk * pk * np.diag(cov)
    f *= 2.0 / np.sqrt(np.pi)
    return val, f


def main():
    u, wu = nodes()
    s, sig = setup(N_GRID)
    p = np.zeros(N_GRID)
    p[-1] = 0.99
    p[N_GRID // 2 - 1] = 0.01
    history = []
    for it in range(120):
        val, f = value_and_kkt(p, sig, u, wu)
        j = int(np.argmax(f))
        direction = -p.copy()
        direction[j] += 1.0
        best = (val, 0.0)
        for g in [0.25 * 0.7 ** k for k in range(40)]:
            q = p + g * direction
            sq = np.sqrt(np.clip(q, 0, None))
            m = sq[:, None] * sig * sq[None, :]
            lam = np.clip(np.linalg.eigvalsh(m), 0.0, None)
            prod = np.prod(1.0 / np.sqrt(1.0 + 2.0 * np.outer(u ** 2, lam)), axis=1)
            small = u < 1e-6
            integ = np.where(small, lam.sum(), (1.0 - prod) / np.where(small, 1.0, u ** 2))
            vq = float(np.sum(integ * wu) / np.sqrt(np.pi))
            if vq > best[0]:
                best = (vq, g)
        if best[1] == 0.0:
            break
        p = p + best[1] * direction
        if it % 10 == 0:
            history.append({'iter': it, 'F': val, 'max_f_grid': float(f.max()),
                            'tangent_upper_on_grid': (val + float(f.max())) / 2,
                            'mass_at_1': float(p[-1])})
    val, f = value_and_kkt(p, sig, u, wu)
    support = [(float(s[i]), float(p[i])) for i in range(N_GRID) if p[i] > 1e-4]
    print(json.dumps({'grid_n': N_GRID, 'F_final': val, 'max_f_grid': float(f.max()),
                      'grid_tangent_upper': (val + float(f.max())) / 2,
                      'mass_at_1': float(p[-1]), 'support_mass_gt_1e-4': support,
                      'kkt_f_at_support': [float(f[i]) for i in range(N_GRID) if p[i] > 1e-4],
                      'history': history,
                      'limits': 'Float quadrature on a 60-point grid; diagnostic only, not a proof about nu* or kappa.'},
                     indent=1))


if __name__ == '__main__':
    main()
