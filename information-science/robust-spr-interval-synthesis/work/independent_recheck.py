"""Independent re-verification of a random subset of the sub-agent's exact spot-check certificates.

Usage: python independent_recheck.py CASES.jsonl K SEED
Different code path from exact_verify.py: endpoints rebuilt from lo/hi with Fractions, pairing
polynomials built with sympy, positivity on [0, inf) via sympy real-root isolation
(Poly.real_roots) plus P(0) > 0 and leading coefficient > 0, robust stability via Hurwitz
determinants (sympy Matrix.det) of the four Kharitonov polynomials (Lienard-Chipart is not used).
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction

import sympy as sp

t = sp.symbols("t")


def endpoints(lo, hi):
    n = len(lo) - 1
    Em, Ep, Om, Op = [], [], [], []
    for k in range(n + 1):
        sgn = (-1) ** (k // 2)
        mn, mx = (lo[k], hi[k]) if sgn > 0 else (-hi[k], -lo[k])
        (Em if k % 2 == 0 else Om).append(mn)
        (Ep if k % 2 == 0 else Op).append(mx)
    return Em, Ep, Om, Op


def corner_coeffs(E, O, n):
    c = [Fraction(0)] * (n + 1)
    for l, e in enumerate(E):
        c[2 * l] = (-1) ** l * e
    for l, o in enumerate(O):
        c[2 * l + 1] = (-1) ** l * o
    return c


def hurwitz_dets_positive(c):
    """c ascending, c[-1] > 0. Hurwitz matrix of a_0 s^n + ... + a_n with a_i = c[n-i]."""
    n = len(c) - 1
    a = [c[n - i] for i in range(n + 1)]
    if a[0] <= 0:
        return False
    H = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            idx = 2 * (j + 1) - (i + 1)
            H[i, j] = sp.Rational(a[idx]) if 0 <= idx <= n else 0
    return all(H[:k, :k].det() > 0 for k in range(1, n + 1))


def evenodd(beta):
    F = sum(sp.Rational((-1) ** (k // 2)) * sp.Rational(beta[k]) * t ** (k // 2)
            for k in range(0, len(beta), 2))
    G = sum(sp.Rational((-1) ** (k // 2)) * sp.Rational(beta[k]) * t ** (k // 2)
            for k in range(1, len(beta), 2))
    return F, G


def main():
    path, K, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    recs = [json.loads(l) for l in open(path)]
    pick = random.Random(seed).sample(recs, min(K, len(recs)))
    ok_all = 0
    for r in pick:
        lo = [Fraction(x) for x in r["lo"]]
        hi = [Fraction(x) for x in r["hi"]]
        n = len(lo) - 1
        raw = r["construction"]["beta"] if "construction" in r else r["synthesis"]["beta"]
        beta = [Fraction(x) for x in raw]
        Em, Ep, Om, Op = endpoints(lo, hi)
        stable = all(hurwitz_dets_positive(corner_coeffs(E, O, n))
                     for E in (Em, Ep) for O in (Om, Op))
        F, G = evenodd(beta)
        pos = True
        for E in (Em, Ep):
            for O in (Om, Op):
                Ept = sum(sp.Rational(e) * t ** l for l, e in enumerate(E))
                Opt = sum(sp.Rational(o) * t ** l for l, o in enumerate(O))
                Pp = sp.Poly(sp.expand(F * Ept + t * G * Opt), t)
                roots = [x for x in Pp.real_roots() if x > 0]
                pos &= (Pp.eval(0) > 0) and (Pp.LC() > 0) and not roots
        deg_ok = beta[-1] != 0
        ok = stable and pos and deg_ok
        ok_all += ok
        print(r["id"], "stable", stable, "positive", pos, "deg", deg_ok)
    print(f"independently confirmed {ok_all}/{len(pick)}")


if __name__ == "__main__":
    main()
