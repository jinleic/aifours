#!/usr/bin/env python3
"""rv163 reviewer-authored NUMERICAL sanity control for Theorem A (not evidence of non-existence).

Searches for orthonormal representations of L(K_{m,m,m}) in C^{2m}: 3m^2 unit vectors, every vertex
star an orthonormal basis.  Objective F = sum_v || Psi_v^* Psi_v - I ||_F^2 (zero iff representation).
Analytic gradient dF/dRe = 4 Re(Psi M), dF/dIm = 4 Im(Psi M), M = Psi^* Psi - I (checked by finite
differences).  L-BFGS-B from seeded random complex Gaussian starts.
  positive controls: m = 2 (C^4), m = 4 (C^8) must reach F ~ 0; m = 5 from the exact certificate
                     (+ small noise) must reach F ~ 0.
  target:            m = 3 (C^6) -- Theorem A predicts every run stalls at F > 0.
For the best m = 3 run, the finite-difference Hessian is diagonalised: the gauge group (global U(6):
36 real directions, one phase per vector: 27) predicts a 63-dimensional null space; the remaining
spectrum being positive means a strict local minimum modulo gauge, i.e. no slow creep to F = 0.
Also: float cross-check of the exact K555 object (basis error, commutant dimension via SVD).
Run: /usr/bin/python3 -B rv163-thmA-numeric-v1.py  (writes rv163-thmA-numeric-v1.json)
"""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy
import scipy.optimize as so

SELF = Path(__file__).resolve()
OUT = SELF.parent / 'rv163-thmA-numeric-v1.json'


def native_clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], capture_output=True,
                          text=True, check=True).stdout.strip()


CLOCK_START = native_clock()


def kmmm(m):
    A = [('A', i) for i in range(m)]
    B = [('B', i) for i in range(m)]
    C = [('C', i) for i in range(m)]
    edges = [(a, b) for a in A for b in B] + [(a, c) for a in A for c in C] + [(b, c) for b in B for c in C]
    ctx = [np.array([k for k, e in enumerate(edges) if v in e]) for v in A + B + C]
    return edges, ctx


def make_fg(m, ctx):
    n = 2 * m
    E = 3 * m * m
    I = np.eye(n)

    def fg(x):
        Z = (x[:E * n] + 1j * x[E * n:]).reshape(E, n)
        F = 0.0
        G = np.zeros((E, n), dtype=complex)
        for c in ctx:
            Psi = Z[c].T
            M = Psi.conj().T @ Psi - I
            F += float(np.sum(np.abs(M) ** 2))
            G[c] += (Psi @ M).T
        g = 4.0 * np.concatenate([G.real.ravel(), G.imag.ravel()])
        return F, g
    return fg, 2 * E * n


def run(m, starts, seed, x0s=None, maxiter=20000):
    edges, ctx = kmmm(m)
    fg, dim = make_fg(m, ctx)
    rng = np.random.default_rng(seed)
    vals, best = [], (np.inf, None)
    inits = x0s if x0s is not None else [None] * starts
    for x0 in inits:
        if x0 is None:
            Z = rng.normal(size=(len(edges), 2 * m)) + 1j * rng.normal(size=(len(edges), 2 * m))
            Z /= np.linalg.norm(Z, axis=1, keepdims=True)
            x0 = np.concatenate([Z.real.ravel(), Z.imag.ravel()])
        r = so.minimize(fg, x0, jac=True, method='L-BFGS-B',
                        options={'maxiter': maxiter, 'maxfun': 4 * maxiter, 'maxcor': 30, 'ftol': 1e-30,
                                 'gtol': 1e-14})
        vals.append(float(r.fun))
        if r.fun < best[0]:
            best = (float(r.fun), r.x.copy())
    return np.array(vals), best, fg, dim


res = {'interpreter': sys.version.split()[0], 'numpy': np.__version__, 'scipy': scipy.__version__}
# gradient check
fg3, dim3 = make_fg(3, kmmm(3)[1])
rng = np.random.default_rng(7)
x = rng.normal(size=dim3)
F0, g0 = fg3(x)
d = rng.normal(size=dim3)
h = 1e-6
fd = (fg3(x + h * d)[0] - fg3(x - h * d)[0]) / (2 * h)
res['gradient_check_rel_err'] = abs(fd - g0 @ d) / abs(fd)

summary = {}
t0 = time.time()
for m, starts, seed in ((2, 40, 1632), (3, 300, 1633), (4, 30, 1634)):
    vals, best, fg, dim = run(m, starts, seed)
    summary[f'm{m}'] = {'dimension': 2 * m, 'starts': starts, 'min_F': float(vals.min()),
                        'quantiles_F_0_10_50_90_100': [float(np.quantile(vals, q)) for q in (0, .1, .5, .9, 1)],
                        'runs_with_F_below_1e-12': int((vals < 1e-12).sum()),
                        'runs_with_F_below_1e-6': int((vals < 1e-6).sum())}
    if m == 3:
        best3 = best
        fg_best = fg
summary['seconds_random_runs'] = time.time() - t0

# m = 5: from the exact certificate, plus 6 random starts
T5 = [(0, 0), (0, 1), (1, 0), (1, 3), (2, 2), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)]
PH5 = [[-35, -25, -25, -15, -20, -10, -15, -5, -10, 0], [-10, -10, -10, -5, 0, 5, -10, 0, 0, 0], [0] * 10]
edges5, ctx5 = kmmm(5)
z20 = np.exp(2j * np.pi / 20)
cellvec = {}
for q in range(3):
    for s in range(5):
        for t in range(5):
            e = [(4 * ((c[0] * s + c[1] * t) % 5) + PH5[q][j]) % 20 for j, c in enumerate(T5)]
            u = (s + t) % 5
            key = [(('A', s), ('B', t)), (('A', s), ('C', u)), (('B', t), ('C', u))][q]
            cellvec[key] = z20 ** np.array(e) / np.sqrt(10)
Z5 = np.array([cellvec[e] for e in edges5])
x5 = np.concatenate([Z5.real.ravel(), Z5.imag.ravel()])
fg5, dim5 = make_fg(5, ctx5)
res['K555_exact_object_F'] = fg5(x5)[0]
res['K555_exact_object_max_basis_error'] = max(float(np.abs(Z5[c].conj() @ Z5[c].T - np.eye(10)).max())
                                                for c in ctx5)
Ls = []
for v in Z5:
    Q = np.outer(v, v.conj())
    Ls.append(np.kron(np.eye(10), Q.T) - np.kron(Q, np.eye(10)))
sv = np.linalg.svd(np.vstack(Ls), compute_uv=False)
res['K555_float_commutant_singular_values_smallest3'] = [float(s) for s in sv[-3:]]
res['K555_float_commutant_dim_tol1e-9'] = int((sv < 1e-9).sum())
rng5 = np.random.default_rng(1635)
x0s = [x5 + 1e-2 * rng5.normal(size=dim5)]
for _ in range(6):
    Zr = rng5.normal(size=(75, 10)) + 1j * rng5.normal(size=(75, 10))
    Zr /= np.linalg.norm(Zr, axis=1, keepdims=True)
    x0s.append(np.concatenate([Zr.real.ravel(), Zr.imag.ravel()]))
vals5, _, _, _ = run(5, None, 0, x0s=x0s, maxiter=40000)
summary['m5'] = {'dimension': 10, 'F_from_exact_plus_1e-2_noise': float(vals5[0]),
                 'F_random_starts': [float(v) for v in vals5[1:]]}
res['searches'] = summary

# Hessian at the best m = 3 minimum
Fb, xb = best3
_, gb = fg_best(xb)
H = np.zeros((dim3, dim3))
eps = 1e-6
for i in range(dim3):
    e = np.zeros(dim3)
    e[i] = eps
    H[:, i] = (fg_best(xb + e)[1] - fg_best(xb - e)[1]) / (2 * eps)
H = (H + H.T) / 2
ev = np.linalg.eigvalsh(H)
res['m3_best'] = {'F': Fb, 'grad_norm': float(np.linalg.norm(gb)),
                  'hessian_min_eig': float(ev[0]), 'hessian_eigs_abs_below_1e-6': int((np.abs(ev) < 1e-6).sum()),
                  'hessian_smallest_eig_above_gauge_gap': float(ev[np.abs(ev) >= 1e-6].min()) if (np.abs(ev) >= 1e-6).any() else None,
                  'hessian_eigs_below_-1e-6': int((ev < -1e-6).sum()), 'gauge_dimension_predicted': 36 + 27,
                  'hessian_eigs_sorted_first_70': [float(v) for v in ev[:70]]}
out = {'script': SELF.name, 'script_sha256': hashlib.sha256(SELF.read_bytes()).hexdigest(),
       'native_clock_start': CLOCK_START, 'native_clock_finish': native_clock(), 'results': res}
OUT.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: res[k] for k in ('gradient_check_rel_err', 'K555_exact_object_F',
                                       'K555_exact_object_max_basis_error', 'K555_float_commutant_dim_tol1e-9')},
                 indent=1))
print(json.dumps(summary, indent=1))
print(json.dumps({k: v for k, v in res['m3_best'].items() if k != 'hessian_eigs_sorted_first_70'}, indent=1))
