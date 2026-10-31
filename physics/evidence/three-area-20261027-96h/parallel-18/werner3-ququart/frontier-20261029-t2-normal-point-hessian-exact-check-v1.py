#!/usr/bin/env python3
"""Exact second-order test of the T2 dual at the normal equality point
X1 = diag(3,-1,-1,-1)(x)I + I(x)diag(1,1,-1,-1), where sigma1^2+sigma2^2 = 16+16 = 32 = ||X1||^2/2.
X1 is diagonal, its top eigenvalue 16 of X1^dag X1 is double and isolated (next 4), so
  c2(Y) = sum_{v top} ||Yv||^2 + sum_{v top} sum_{w not top} |<w|H1|v>|^2/(16-mu_w) - ||Y||^2/2,
  H1 = X1^dag Y + Y^dag X1, over ALL 60 real directions of sl4+sl4 (non-normal ones included).
Exact Fraction arithmetic, exact inertia; fault controls overestimate the second-order term.
Authorized by Main as an exact counterexample search; no held input.
"""
from fractions import Fraction as Fr
from pathlib import Path
import hashlib
import json

D, N = 4, 16
a = [3, -1, -1, -1]
b = [1, 1, -1, -1]
x = [Fr(a[i] + b[j]) for i in range(D) for j in range(D)]  # diagonal of X1, index 4i+j
lam = [v * v for v in x]
top = max(lam)
top_idx = [k for k in range(N) if lam[k] == top]
assert len(top_idx) == 2 and sorted(lam)[-3] < top


def small(entries):
    return {k: v for k, v in entries.items()}


def Y_entry(S, R, r, c):
    """(S(x)I + I(x)R)[r][c] as complex pair, S,R dicts {(i,j):(re,im)}."""
    i1, j1 = divmod(r, 4)
    i2, j2 = divmod(c, 4)
    re = im = Fr(0)
    if j1 == j2 and (i1, i2) in S:
        re += S[(i1, i2)][0]
        im += S[(i1, i2)][1]
    if i1 == i2 and (j1, j2) in R:
        re += R[(j1, j2)][0]
        im += R[(j1, j2)][1]
    return re, im


def c2(S, R, scale=(Fr(1), Fr(1))):
    Y = [[Y_entry(S, R, r, c) for c in range(N)] for r in range(N)]
    normY = sum(p * p + q * q for row in Y for (p, q) in row)
    total = Fr(0)
    for v in top_idx:
        total += sum(Y[r][v][0] ** 2 + Y[r][v][1] ** 2 for r in range(N))
        for w in range(N):
            if w in top_idx:
                continue
            # <w|H1|v> = conj(x_w) Y[w][v] + conj(Y[v][w]) x_v   (X1 real diagonal)
            re = x[w] * Y[w][v][0] + x[v] * Y[v][w][0]
            im = x[w] * Y[w][v][1] - x[v] * Y[v][w][1]
            gap = top - lam[w]
            weight = scale[0] if lam[w] > 0 else scale[1]
            total += weight * (re * re + im * im) / gap
    return total - normY / 2


def sl4_basis():
    out = []
    for i in range(D):
        for j in range(D):
            if i != j:
                out.append({(i, j): (Fr(1), Fr(0))})
                out.append({(i, j): (Fr(0), Fr(1))})
    for k in range(1, D):
        out.append({(0, 0): (Fr(1), Fr(0)), (k, k): (Fr(-1), Fr(0))})
        out.append({(0, 0): (Fr(0), Fr(1)), (k, k): (Fr(0), Fr(-1))})
    return out


def addd(P, Q):
    out = dict(P)
    for k, v in Q.items():
        if k in out:
            out[k] = (out[k][0] + v[0], out[k][1] + v[1])
        else:
            out[k] = v
    return out


sl = sl4_basis()
dirs = [(B, {}) for B in sl] + [({}, B) for B in sl]


def form(scale):
    n = len(dirs)
    dg = [c2(*d, scale=scale) for d in dirs]
    M = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = dg[i]
        for j in range(i + 1, n):
            M[i][j] = M[j][i] = (c2(addd(dirs[i][0], dirs[j][0]), addd(dirs[i][1], dirs[j][1]), scale=scale) - dg[i] - dg[j]) / 2
    return M


def inertia(M):
    A = [row[:] for row in M]
    alive = list(range(len(A)))
    pos = neg = 0
    while alive:
        piv = next((i for i in alive if A[i][i] != 0), None)
        if piv is not None:
            p = A[piv][piv]
            pos += p > 0
            neg += p < 0
            rest = [i for i in alive if i != piv]
            for i in rest:
                if A[i][piv] != 0:
                    f = A[i][piv] / p
                    for j in rest:
                        A[i][j] -= f * A[piv][j]
            alive = rest
            continue
        pair = next(((i, j) for i in alive for j in alive if i < j and A[i][j] != 0), None)
        if pair is None:
            break
        i, j = pair
        pos += 1
        neg += 1
        rest = [k for k in alive if k not in (i, j)]
        bb = A[i][j]
        for k in rest:
            for l in rest:
                A[k][l] -= (A[k][i] * A[j][l] + A[k][j] * A[i][l]) / bb
        alive = rest
    return pos, neg, len(A) - pos - neg


p, n_, z = inertia(form((Fr(1), Fr(1))))
fault1 = inertia(form((Fr(2), Fr(1))))
fault2 = inertia(form((Fr(1), Fr(3))))
null_ok = c2({(0, 0): (Fr(3), Fr(0)), (1, 1): (Fr(-1), Fr(0)), (2, 2): (Fr(-1), Fr(0)), (3, 3): (Fr(-1), Fr(0))},
             {(0, 0): (Fr(1), Fr(0)), (1, 1): (Fr(1), Fr(0)), (2, 2): (Fr(-1), Fr(0)), (3, 3): (Fr(-1), Fr(0))}) == 0
status = null_ok and p == 0 and (fault1[0] > 0 or fault2[0] > 0)
rec = {
    'status': 'PASS' if status else ('INDEFINITE-CANDIDATE' if p > 0 else 'FAIL'),
    'equality_point': 'X1 = diag(3,-1,-1,-1)(x)I + I(x)diag(1,1,-1,-1); sigma1^2+sigma2^2=32=||X1||^2/2',
    'second_order_form_inertia': {'positive': p, 'negative': n_, 'zero': z},
    'null_check_c2_along_X1_is_0': null_ok,
    'fault_controls': {'gap_weights_doubled_for_nonzero_lower_eigenvalues': fault1, 'gap_weights_tripled_for_zero_eigenvalues': fault2},
    'arithmetic': 'fractions.Fraction only; exact symmetric elimination; no floats',
    'scope': 'Second-order necessary-condition test at one normal equality point, over all (including non-normal) traceless directions; not a proof of T2.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).resolve().parent.joinpath('frontier-20261029-t2-normal-point-hessian-exact-check-results-v1.json').write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
print(json.dumps(rec, sort_keys=True))
