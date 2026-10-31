#!/usr/bin/env python3
"""Floating regression (diagnostic, not a proof) for the coefficient
inequalities used by the symmetrization route, on random 7x7 Metzler matrices.

For G Metzler with geometric symmetrization S (S_ii=G_ii, S_ij=sqrt(G_ij G_ji))
and v_1<=...<=v_7 the eigenvalues of -S, let c_k be the coefficient of y^(7-k)
in det(yI-G) and d_k = e_k(v) - c_k. The written lemmas imply
  d_1 = d_2 = 0,  W := d_3 >= 0,  d_4 >= W*S4,
  d_5 >= W*m2 + S3*max(0, d_4 - W*L4)       (Lemma 5),
with S3, S4 the sums of the 3, 4 smallest v's, m2=e2(v_1..v_4), L4 the sum of
the four largest. No irreducibility or spectral assumption is needed for these.
"""
import itertools
import numpy as np

def esym(vals, k):
    return sum(np.prod(c) for c in itertools.combinations(vals, k)) if k else 1.0

rng = np.random.default_rng(20261029)
worst = {'d1': 0.0, 'd2': 0.0, 'W': np.inf, 'K': np.inf, 'Y2': np.inf}
trials = 0; nontrivial = 0; y2_active = 0
for density in (0.25, 0.4, 0.6, 0.85):
    for _ in range(500):
        G = np.where(rng.random((7, 7)) < density, rng.exponential(1.0, (7, 7)), 0.0)
        # sometimes force many bidirected pairs, sometimes many one-way edges
        if rng.random() < 0.3:
            G = np.where((G > 0) & (G.T > 0), G, 0.0) + np.triu(G, 1) * (rng.random() < 0.5)
        if rng.random() < 0.5:      # add heavy one-way 3-, 4- or 5-cycles so that W, C4, C5 are substantial
            for _c in range(rng.integers(1, 4)):
                cyc = rng.permutation(7)[:rng.integers(3, 6)]
                for a_, b_ in zip(cyc, np.roll(cyc, -1)):
                    G[a_, b_] += rng.exponential(3.0); G[b_, a_] = 0.0
        np.fill_diagonal(G, 0.0)
        np.fill_diagonal(G, -(G.sum(axis=1) + rng.exponential(1.0, 7)))
        S = np.sqrt(G * G.T); np.fill_diagonal(S, np.diag(G))
        v = np.sort(np.linalg.eigvalsh(-S))
        c = np.poly(G)            # det(yI-G) coefficients, c[0]=1
        e = [esym(v, k) for k in range(8)]
        d = [e[k] - c[k] for k in range(8)]
        scale = 1.0 + max(abs(t) for t in e)
        W = d[3]; S3 = v[:3].sum(); S4 = v[:4].sum(); L4 = v[3:].sum(); m2 = esym(v[:4], 2)
        worst['d1'] = max(worst['d1'], abs(d[1]) / scale); worst['d2'] = max(worst['d2'], abs(d[2]) / scale)
        worst['W'] = min(worst['W'], W / scale)
        worst['K'] = min(worst['K'], (d[4] - W * S4) / scale)
        worst['Y2'] = min(worst['Y2'], (d[5] - W * m2 - S3 * max(0.0, d[4] - W * L4)) / scale)
        nontrivial += W / scale > 1e-3; y2_active += (d[4] - W * L4) / scale > 1e-3
        trials += 1
print('trials', trials, 'with W/scale>1e-3:', nontrivial, 'with (d4-W*L4)/scale>1e-3:', y2_active, {k: float(f'{val:.3e}') for k, val in worst.items()})
tol = 1e-9
assert worst['d1'] < tol and worst['d2'] < tol and worst['W'] > -tol and worst['K'] > -tol and worst['Y2'] > -tol
print('PASS (floating regression): d1=d2=0, W>=0, d4>=W*S4, Lemma 5 inequality on all trials')
