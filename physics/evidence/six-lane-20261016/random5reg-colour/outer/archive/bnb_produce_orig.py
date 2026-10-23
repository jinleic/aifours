"""Producer of the outer cell certificate (floating point search; the certificate is checked
independently by cert_cells.py (arb) and cert_cells_iv.py (mpmath.iv)).

Tree in preorder: ['S', i, j] bisect edge (i,j) (first child replaces vertex i by the midpoint);
['C'] central leaf (all vertices in the box |n_k - 1/9| <= r0); ['D', y_hex[18], mu0_hex[9][4]].
Usage: bnb_produce.py FI FJ R0_FRACTION OUT.json [SAFETY]
"""
import sys, math, json, time, itertools
from fractions import Fraction
import numpy as np
sys.path.insert(0, 'code')
from dual import solve_dual, inner, C
from model import Model, nine_from_four

sys.setrecursionlimit(100000)
fi, fj = int(sys.argv[1]), int(sys.argv[2])
r0 = Fraction(sys.argv[3])
out = sys.argv[4]
safety = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-9
MOD = Model(5, True)
SARR = MOD.Sarr
LSTAR = 2.5 * math.log(5) + math.log(25 / 24)


def a_float(z, theta):
    mu = np.exp(theta)
    d = MOD.w * np.prod(mu[None, :] ** SARR, axis=1)
    Z = d.sum()
    m0 = SARR.T @ d / Z
    psi0 = 0.5 * m0 @ np.log(m0) + math.log(Z) - np.log(mu) @ m0
    g = 0.5 * np.log(m0) - np.log(mu) + z
    T = np.max((SARR - m0) @ g)
    return psi0 + z @ m0 + T, mu


def n9(p):
    v = nine_from_four(p)
    v[np.abs(v) < 1e-15] = 0.0
    return np.maximum(v, 0.0)


def central(cell):
    rf = float(r0)
    return all(abs(p[k] - 1 / 9) <= rf * (1 - 1e-12) for p in cell for k in range(4))


tree = []
stats = {'dual': 0, 'central': 0, 'splits': 0, 'min_margin': 1e9, 'maxdepth': 0}


def rec(cell, y0, depth):
    stats['maxdepth'] = max(stats['maxdepth'], depth)
    if central(cell):
        tree.append(['C']); stats['central'] += 1
        return
    cen = cell.mean(axis=0)
    val, y, gres, ths, mhs = solve_dual(n9(cen), y0)
    # quantise y to hex floats (exactly what the checker will read)
    yq = np.array([float.fromhex(float(v).hex()) for v in y])
    a, mus = [], []
    for u in range(9):
        z = C[u] @ yq
        gv, mh, th, R = inner(z, ths[u] if ths is not None else None)
        au, mu = a_float(z, th)
        a.append(au); mus.append(mu)
    ub = -1e18
    for p in cell:
        nn = n9(p)
        ub = max(ub, sum(nn[u] * a[u] + (1.5 * nn[u] * math.log(nn[u]) if nn[u] > 0 else 0.0) for u in range(9)))
    if ub < LSTAR - safety:
        tree.append(['D', [float(v).hex() for v in yq], [[float(x).hex() for x in mu] for mu in mus]])
        stats['dual'] += 1
        stats['min_margin'] = min(stats['min_margin'], LSTAR - ub)
        return
    best, bi, bj = -1, 0, 0
    for i in range(5):
        for j in range(i + 1, 5):
            dd = np.linalg.norm(n9(cell[i]) - n9(cell[j]))
            if dd > best:
                best, bi, bj = dd, i, j
    tree.append(['S', bi, bj]); stats['splits'] += 1
    mid = 0.5 * (cell[bi] + cell[bj])
    c1 = cell.copy(); c1[bi] = mid
    c2 = cell.copy(); c2[bj] = mid
    rec(c1, y, depth + 1)
    rec(c2, y, depth + 1)


def perm_point(sig):
    return np.array([sig[0] == 0, sig[0] == 1, sig[1] == 0, sig[1] == 1], float) / 3


root = np.array([np.full(4, 1 / 9)] + [perm_point(s) for s in itertools.permutations(range(3)) if s[fi] != fj])
t0 = time.time()
rec(root, None, 0)
stats['runtime_s'] = round(time.time() - t0, 1)
json.dump({'facet': [fi, fj], 'r0': str(r0), 'safety': safety, 'stats': stats, 'tree': tree}, open(out, 'w'))
print(json.dumps(stats))
