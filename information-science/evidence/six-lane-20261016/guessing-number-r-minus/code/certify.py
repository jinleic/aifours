"""Exact rational certificates for entropy-LP upper bounds h(V) <= B.

A certificate is: nonnegative rationals y_r for '>= 0' rows (elemental Shannon / extra valid rows),
rationals z_e for game equalities h(N[v]) - h(N(v)) = 0, nonnegative u_v for singleton bounds h({v}) <= 1,
such that for EVERY polymatroid-coordinate mask S:
    [S == V] + sum_r y_r * row_r[S] + sum_e z_e * eq_e[S] - u_{v}[S=={v}] == 0
i.e.  h(V) = - sum y_r row_r(h) - sum z_e eq_e(h) + sum u_v h({v})  <=  sum u_v  =: B.
check() verifies this identity with Fractions only (no floats).  rationalize() turns HiGHS duals into
candidate rationals by limit_denominator and then repairs/validates exactly.
"""
from fractions import Fraction as Fr
import numpy as np

def check(n, ge_rows, eq_rows, y, z, u):
    full = (1 << n) - 1
    acc = {}
    def add(m, c):
        if c: acc[m] = acc.get(m, 0) + c
    add(full, Fr(1))
    for r, yr in zip(ge_rows, y):
        if yr:
            assert yr >= 0, "negative multiplier on >= row"
            for m, c in r.items(): add(m, yr * c)
    for r, ze in zip(eq_rows, z):
        if ze:
            for m, c in r.items(): add(m, ze * c)
    for v in range(n):
        if u[v]:
            assert u[v] >= 0
            add(1 << v, -u[v])
    bad = {m: c for m, c in acc.items() if c != 0}
    return (len(bad) == 0), bad, sum(u)

def rationalize(vals, maxden):
    return [Fr(float(x)).limit_denominator(maxden) if abs(x) > 1e-12 else Fr(0) for x in vals]
