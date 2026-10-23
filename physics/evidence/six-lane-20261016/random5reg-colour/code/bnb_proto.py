"""Floating-point prototype of the outer branch-and-bound (NOT a certificate).

Cells: 4-simplices in n-space (coordinates n00, n01, n10, n11).  Delta = cone from n* over its 9
tetrahedral facets {n^u = 0}; by the order-72 symmetry one facet cone suffices (u0 below).
Per cell: y = optimal pairing multipliers at the centroid; bound U_y(n) = sum_u [n^u Psi*(C_u y)
+ 1.5 n^u ln n^u] is convex in n, so its max over the simplex is at a vertex.
Cells inside the central ball |n - n*|_F <= r0 are left to the local argument.
Usage: bnb_proto.py FACET_I FACET_J R0 [MAXCELLS] [OUTJSON]
"""
import sys, math, time, json, itertools
import numpy as np
sys.path.insert(0, 'code')
from dual import solve_dual, inner, C
from model import nine_from_four

fi, fj, r0 = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
maxcells = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
outjson = sys.argv[5] if len(sys.argv) > 5 else None
LSTAR = 2.5 * math.log(5) + math.log(25 / 24)
NSTAR = np.full(4, 1 / 9)


def perm_point(sig):
    return np.array([sig[0] == 0, sig[0] == 1, sig[1] == 0, sig[1] == 1], float) / 3


verts = [perm_point(s) for s in itertools.permutations(range(3)) if s[fi] != fj]
assert len(verts) == 4
root = np.array([NSTAR] + verts)


def n9(p):
    v = nine_from_four(p)
    v[np.abs(v) < 1e-15] = 0.0
    return np.maximum(v, 0.0)


def dist_centre(p):
    return np.linalg.norm(n9(p) - 1 / 9)


def bound(cell, y0):
    cen = cell.mean(axis=0)
    val, y, gres, ths, mhs = solve_dual(n9(cen), y0)
    psis = np.array([inner(C[u] @ y)[0] for u in range(9)])
    ub = -1e9
    for p in cell:
        nn = n9(p)
        U = sum(nn[u] * psis[u] + (1.5 * nn[u] * math.log(nn[u]) if nn[u] > 0 else 0.0) for u in range(9))
        ub = max(ub, U)
    return ub, val, y


t0 = time.time()
stack = [(root, None, 0)]
stats = {'accepted': 0, 'central': 0, 'evaluated': 0, 'maxdepth': 0, 'min_margin_accepted': 1e9}
hist, acc_log = {}, []
while stack:
    cell, y0, depth = stack.pop()
    if all(dist_centre(p) <= r0 for p in cell):
        stats['central'] += 1
        continue
    ub, val, y = bound(cell, y0)
    stats['evaluated'] += 1
    stats['maxdepth'] = max(stats['maxdepth'], depth)
    if ub < LSTAR - 1e-9:
        stats['accepted'] += 1
        stats['min_margin_accepted'] = min(stats['min_margin_accepted'], LSTAR - ub)
        hist[depth] = hist.get(depth, 0) + 1
        dc = min(dist_centre(p) for p in cell)
        diam = max(np.linalg.norm(n9(a) - n9(b)) for a in cell for b in cell)
        acc_log.append((round(dc, 5), round(float(min(n9(cell.mean(axis=0)))), 6), round(diam, 6), depth,
                        round(LSTAR - val, 6), round(LSTAR - ub, 7)))
        continue
    if stats['evaluated'] > maxcells:
        stats['aborted'] = True
        break
    # longest edge bisection (Frobenius metric on the nine overlap values)
    best, bi, bj = -1, 0, 0
    for i in range(5):
        for j in range(i + 1, 5):
            dd = np.linalg.norm(n9(cell[i]) - n9(cell[j]))
            if dd > best:
                best, bi, bj = dd, i, j
    mid = 0.5 * (cell[bi] + cell[bj])
    c1 = cell.copy(); c1[bi] = mid
    c2 = cell.copy(); c2[bj] = mid
    stack.append((c1, y, depth + 1))
    stack.append((c2, y, depth + 1))
stats['runtime_s'] = time.time() - t0
stats['depth_hist'] = hist
stats['open_cells'] = len(stack)
print(json.dumps(stats))
if outjson:
    with open(outjson, 'w') as f:
        json.dump({'stats': stats, 'r0': r0, 'facet': [fi, fj],
                   'accepted_cells(dist_centre_min, centroid_nmin, diam, depth, centroid_gap, bound_margin)': acc_log}, f)
