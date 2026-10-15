"""Verify the normalization dictionary to Alisauskas PDF Eq. (26a).

The n=3 control uses an independently implemented SymPy Wigner 3j symbol.
The n=5 comparison includes all ordered triples with degrees 0..12.
"""
from fractions import Fraction as Q
from itertools import product
import json
from math import factorial
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import wigner_3j

from crw_formula import admissible, dimension, square_pi

ROOT = Path(__file__).resolve().parents[1]


def half_gamma(q):
    """Gamma(q+1/2)/sqrt(pi), exactly for nonnegative integer q."""
    return Q(factorial(2 * q), 4 ** q * factorial(q))


def class_one_dimension(n, v):
    return (2 * v + n - 2) * factorial(v + n - 3) // (factorial(v) * factorial(n - 2))


def three_j_squared(n, triple):
    """Literal square of Alisauskas (26a), n=3 or 5; pi cancels."""
    if n not in (3, 5):
        raise ValueError("this replay specializes only n=3 and n=5")
    if not admissible(*triple):
        return Q(0)
    s = sum(triple) // 2
    q = (n - 1) // 2
    value = Q(factorial(s + n - 3), factorial(n - 3)) / (half_gamma(q) ** 2 * half_gamma(s + q))
    for v in triple:
        j = s - v
        value *= Q(2 * v + n - 2, 2) * half_gamma(j + q - 1) / (class_one_dimension(n, v) * factorial(j))
    return value


def symbolic_ratio():
    a, b, c = sp.symbols("a b c", integer=True, nonnegative=True)
    s = a + b + c
    vs = (b + c, a + c, a + b)
    js = (a, b, c)
    f = sp.factorial
    H = lambda q: f(2 * q) / (4 ** q * f(q))
    d = lambda v: (v + 1) * (v + 2) * (2 * v + 3) / 6
    prior = f(s + 2) / (2 * H(2) ** 2 * H(s + 2))
    prior *= sp.prod((v + sp.Rational(3, 2)) * H(j + 1) / (d(v) * f(j)) for v, j in zip(vs, js))
    factored = (24 * f(s + 1) * f(s + 2) / f(2 * s + 3)
                * sp.prod(f(2 * j + 1) / f(j) ** 2 for j in js)
                / sp.prod((v + 1) * (v + 2) for v in vs))
    ratio = sp.combsimp(prior / factored)
    assert ratio == 1
    return str(ratio)


def main():
    ratio = symbolic_ratio()
    for triple in product(range(5), repeat=3):
        assert sp.Rational(three_j_squared(3, triple)) == wigner_3j(*triple, 0, 0, 0) ** 2
    for triple in product(range(13), repeat=3):
        mapped = Q(3, 16) * dimension(triple[0]) * dimension(triple[1]) * three_j_squared(5, triple)
        assert mapped == square_pi(*triple), (triple, mapped)
    # Direct fixed-L3=4 stretched CRW Eq. (28) calibration, not a trace sum.
    q2_fourth_moment = Q(1, 4) * (Q(3, 35) + 2 * Q(1, 35) + Q(3, 35))
    direct_stretched = Q(225, 256) * Q(16, 3) * q2_fourth_moment
    assert direct_stretched == square_pi(1, 1, 2) == Q(15, 56)
    report = {"verdict": "PASS", "source": "Alisauskas math-ph/0509035v1 PDF Eq.(26a), visually checked on p.11",
              "symbolic_factorial_ratio": ratio, "so3_wigner_control_triples": 125,
              "so5_crw_dictionary_triples": 2197,
              "dictionary": "pi^2 R(v3;v2,v1)^2 = (3/16) d(v1)d(v2) (v1 v2 v3;0 0 0)_5^2",
              "three_j_squared_222": str(three_j_squared(5, (2, 2, 2))),
              "direct_crw_stretched_112_pi_squared_R_squared": str(direct_stretched),
              "meaning": "Equivalent closed-form literature predates CRW. No new-discovery priority is claimed."}
    (ROOT / "results/prior-art-identity.json").write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: prior-art symbolic ratio", ratio, "; SO(3) controls 125; SO(5)-CRW dictionaries 2197")
    print("PASS: SO(5) 3j(2,2,2;0,0,0)^2 =", three_j_squared(5, (2, 2, 2)), "; direct CRW stretched pi^2 R^2 =", direct_stretched)


if __name__ == "__main__":
    main()
