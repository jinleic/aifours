#!/usr/bin/env python3
"""reviewer-f173-witt-sanity-v1.py -- modelling sanity for reviewer-f173-controls-v1.py.

Checks that the toy realisation of L_n(M) used by the controls (span of right-nested
commutators inside M^(tensor n), computed with the same reviewer-authored routines)
has the multigraded Witt (free Lie) dimension at every root degree, for the sl2 toy
(levels 1..6) and the sl3-adjoint toy (levels 1..4).  This only confirms the classical
embedding of the free Lie algebra in the tensor algebra for the toy pieces used; it
computes no quotient, rank or actual-problem quantity.
"""
import importlib.util
import os
import sys
from itertools import product
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ctl", os.path.join(HERE, "reviewer-f173-controls-v1.py"))
ctl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctl)


def mobius(n):
    res, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    return -res if m > 1 else res


def witt_dims(model, n_max):
    """T_m(D) by counting letter sequences; l_n(D) = (1/n) sum_{d|gcd(n,D)} mu(d) T_{n/d}(D/d)."""
    T = {m: {} for m in range(1, n_max + 1)}
    for m in range(1, n_max + 1):
        for s in product(range(model.N), repeat=m):
            D = model.wdeg(s)
            T[m][D] = T[m].get(D, 0) + 1
    out = {}
    for n in range(1, n_max + 1):
        for D in T[n]:
            g = n
            for x in D:
                g = gcd(g, x)
            tot = 0
            for d in range(1, g + 1):
                if g % d == 0:
                    tot += mobius(d) * T[n // d].get(tuple(x // d for x in D), 0)
            assert tot % n == 0
            out[(n, D)] = tot // n
    return out


def run(model, n_max):
    W = witt_dims(model, n_max)
    bad, total = [], {}
    for (n, D), w in sorted(W.items()):
        got = model.L(n, D).dim()
        total[n] = total.get(n, 0) + got
        if got != w:
            bad.append((n, D, got, w))
    ok = not bad
    print(f"POS {'PASS' if ok else 'FAIL'} | {model.name}: dim span(nested commutators) == Witt l_n(D) at all "
          f"{len(W)} root degrees, levels 1..{n_max} | level totals {total} | mismatches {bad[:5]}", flush=True)
    return ok


def main():
    ok = run(ctl.build_sl2(), 6) and run(ctl.build_sl3(), 4)
    print(f"SUMMARY | witt sanity {'PASS' if ok else 'FAIL'}", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
