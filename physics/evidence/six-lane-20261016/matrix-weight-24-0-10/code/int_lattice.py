"""Exact integer-point structure of the 8-parameter genus-2 family: all s in Z^8 such that every pair count
x = c + V s is an integer form a coset s0 + B Z^8. Computed by successive solution of linear congruences
(extended-gcd column reduction) with exact Python integers, followed by exact LLL reduction of B.
"""
import json
from fractions import Fraction
from math import gcd

from g2_polytope import load_space


def lcm(a, b):
    return a // gcd(a, b) * b


def ext_gcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x, y = ext_gcd(b, a % b)
    return (g, y, x - (a // b) * y)


def row_kernel_unimodular(row):
    """For integer row r (length k), return (g, U) with U unimodular k x k such that r U = (g, 0, ..., 0)."""
    k = len(row)
    U = [[int(i == j) for j in range(k)] for i in range(k)]
    r = list(row)
    for j in range(1, k):
        if r[j] == 0:
            continue
        g, x, y = ext_gcd(r[0], r[j])
        a0, aj = r[0] // g, r[j] // g
        # new col0 = x*col0 + y*colj ; new colj = -aj*col0 + a0*colj  (det = x*a0 + y*aj = 1)
        for i in range(k):
            c0, cj = U[i][0], U[i][j]
            U[i][0], U[i][j] = x * c0 + y * cj, -aj * c0 + a0 * cj
        r[0], r[j] = g, 0
    if r[0] < 0:
        for i in range(k):
            U[i][0] = -U[i][0]
        r[0] = -r[0]
    return r[0], U


def solve_congruence(alpha, rho, D):
    """All y in Z^k with alpha.y == rho (mod D): returns (y0, basis list of k vectors) or None."""
    k = len(alpha)
    row = [a % D for a in alpha] + [-D]
    g, U = row_kernel_unimodular(row)
    if rho % g:
        return None
    # particular: (y,kk) = (rho/g) * U[:,0]
    t = rho // g
    y0 = [t * U[i][0] for i in range(k)]
    basis = [[U[i][j] for i in range(k)] for j in range(1, k + 1)]
    return y0, basis


def lll(B, delta=Fraction(3, 4)):
    """Exact LLL on list of integer vectors (rows)."""
    B = [list(b) for b in B]
    n = len(B)

    def dot(u, v):
        return sum(a * b for a, b in zip(u, v))

    def gs(B):
        Bs, mu = [], [[Fraction(0)] * n for _ in range(n)]
        for i in range(n):
            v = [Fraction(x) for x in B[i]]
            for j in range(i):
                mu[i][j] = Fraction(dot(B[i], Bs[j])) / dot(Bs[j], Bs[j]) if dot(Bs[j], Bs[j]) else Fraction(0)
                v = [a - mu[i][j] * b for a, b in zip(v, Bs[j])]
            Bs.append(v)
        return Bs, mu

    Bs, mu = gs(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            q = round(mu[k][j])
            if q:
                B[k] = [a - q * b for a, b in zip(B[k], B[j])]
                Bs, mu = gs(B)
        if dot(Bs[k], Bs[k]) >= (delta - mu[k][k - 1] ** 2) * dot(Bs[k - 1], Bs[k - 1]):
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            Bs, mu = gs(B)
            k = max(k - 1, 1)
    return B


def subspace_multiplier(key):
    """For a pair type with u, v, u+v all nonzero, lambda must be divisible by |Stab_S3(n0x,nx0,nxx)|:
    each 2-dim subspace {0,u,v,u+v} contributes exactly m ordered pairs to every type of its S3-orbit."""
    (a, b, cc), d = key
    n0x, nx0, nxx, nxy = a, b, cc, d
    i, j, k = nx0 + nxx + nxy, n0x + nxx + nxy, nx0 + n0x + nxy
    if min(i, j, k) == 0:
        return 1
    distinct = len({a, b, cc})
    return {1: 6, 2: 2, 3: 1}[distinct]


if __name__ == "__main__":
    import sys
    use_sub = "--subspace" in sys.argv
    keys, piv, free, c, V = load_space()
    nf = len(free)
    s0 = [0] * nf
    B = [[int(i == j) for j in range(nf)] for i in range(nf)]  # rows = basis vectors
    ncong = 0
    for i in range(len(keys)):
        mult = subspace_multiplier((tuple(keys[i][0]), keys[i][1])) if use_sub else 1
        D = c[i].denominator
        for f in range(nf):
            D = lcm(D, V[i][f].denominator)
        if D * mult == 1:
            continue
        a = [int(V[i][f] * D) for f in range(nf)]
        r = int(-c[i] * D)
        D = D * mult
        # substitute s = s0 + sum_j y_j B[j]
        alpha = [sum(a[f] * B[j][f] for f in range(nf)) for j in range(nf)]
        rho = r - sum(a[f] * s0[f] for f in range(nf))
        sol = solve_congruence(alpha, rho, D)
        if sol is None:
            print("NO INTEGER POINTS: congruence unsolvable at row", i, keys[i])
            raise SystemExit(1)
        y0, Ybasis = sol
        s0 = [s0[f] + sum(y0[j] * B[j][f] for j in range(nf)) for f in range(nf)]
        B = [[sum(Yb[j] * B[j][f] for j in range(nf)) for f in range(nf)] for Yb in Ybasis]
        B = lll(B)
        ncong += 1
    import sympy
    detB = abs(sympy.Matrix(B).det())
    print("subspace divisibility:", use_sub, " congruences used:", ncong, " lattice index [Z^8 : L] =", detB)
    outname = "../evidence/int_lattice_subspace.json" if use_sub else "../evidence/int_lattice.json"
    json.dump({"s0": [str(v) for v in s0], "B": [[str(v) for v in row] for row in B], "index": str(detB),
               "subspace_divisibility": use_sub}, open(outname, "w"), indent=1)
    # verify: s0 and s0 + each basis vector give integer counts (and divisibility if requested)
    for test in [s0] + [[s0[f] + B[j][f] for f in range(nf)] for j in range(nf)]:
        xs = [c[i] + sum(V[i][f] * test[f] for f in range(nf)) for i in range(len(keys))]
        assert all(x.denominator == 1 for x in xs), "integrality check failed"
        if use_sub:
            assert all(int(xs[i]) % subspace_multiplier((tuple(keys[i][0]), keys[i][1])) == 0
                       for i in range(len(keys))), "divisibility check failed"
    print("integrality (and divisibility) verified for s0 and all s0 + basis vectors")
    print("basis row lengths (log10):", [round(float(sympy.log(sum(v * v for v in b), 10) / 2), 2) for b in B])
