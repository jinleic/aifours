"""Self-tests of the exact engine (operator algebra, adjointness, CG formula).

Run: $PY code/selftest.py   (PY = scratch/ai4s-venvs/phys-fractional-parentage-coefficients/bin/python)
"""
import random

from flint import fmpq
from sympy import Rational, sign
from sympy.physics.wigner import clebsch_gordan

import fpc_core
from fpc_core import SpinBosons, cg_stretched, clean


def sub(p, q, c=1):
    out = dict(p)
    for a, x in q.items():
        fpc_core._add(out, a, -c * x)
    return clean(out)


def main():
    random.seed(20261014)
    checks = 0
    for f in (1, 2, 3):
        B = SpinBosons(f)
        D = B.D
        for n in (3, 4, 5, 6):
            for M in (0, 1, 2):
                p = clean({a: fmpq(random.randint(-5, 5)) for a in B.monomials(n, M)})
                # [P, P+] = 4N + 2D
                lhs = sub(B.pair_ann(B.pair_cre(p)), B.pair_cre(B.pair_ann(p)))
                assert not sub(lhs, p, 4 * n + 2 * D), (f, n, M)
                # S+ commutes with P and P+
                assert not sub(B.splus(B.pair_ann(p)), B.pair_ann(B.splus(p)))
                assert not sub(B.splus(B.pair_cre(p)), B.pair_cre(B.splus(p)))
                # harmonic projection lands in ker P and is idempotent / orthogonal
                h = B.harm_proj(p, n)
                assert not clean(B.pair_ann(h)), (f, n, M)
                assert not sub(B.harm_proj(h, n), h)
                if n >= 2:
                    q = clean({a: fmpq(random.randint(-5, 5)) for a in B.monomials(n - 2, M)})
                    assert B.inner(B.pair_cre(q), p) == B.inner(q, B.pair_ann(p))
                    assert B.inner(B.pair_cre(q), h) == 0
                r = clean({a: fmpq(random.randint(-5, 5)) for a in B.monomials(n, M + 1)})
                assert B.inner(B.splus(p), r) == B.inner(p, B.sminus(r))
                # [S+, S-] = 2 S_z
                comm = sub(B.splus(B.sminus(p)), B.sminus(B.splus(p)))
                assert not sub(comm, p, 2 * M)
                checks += 7
    for j1 in range(0, 4):
        for j2 in range(0, 6):
            for J in range(abs(j1 - j2), j1 + j2 + 1):
                for m1 in range(-j1, j1 + 1):
                    m2 = J - m1
                    if abs(m2) > j2:
                        continue
                    s, sq = cg_stretched(j1, m1, j2, m2, J)
                    ref = clebsch_gordan(j1, j2, J, m1, m2, J)
                    assert Rational(int(sq.p), int(sq.q)) == ref ** 2, (j1, m1, j2, m2, J)
                    assert s == sign(ref)
                    checks += 1
    print(f"selftest OK: {checks} exact checks passed")


if __name__ == "__main__":
    main()
