"""One-command scientific replay; exact rational/symbolic arithmetic only."""
from fractions import Fraction as Q
from functools import cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

import sympy as sp

from cartesian_oracle import compute as cartesian_compute
from crw_formula import admissible, dimension, square_pi
from prior_art_identity import main as verify_prior_art

ROOT = Path(__file__).resolve().parents[1]
MAX_V = 12


def multiply(p, q):
    result = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def legendre(n):
    polynomials = [[Q(1)], [Q(0), Q(1)]]
    for k in range(1, n):
        next_p = [Q(0)] * (k + 2)
        for i, coefficient in enumerate(polynomials[k]):
            next_p[i + 1] += Q(2 * k + 1, k + 1) * coefficient
        for i, coefficient in enumerate(polynomials[k - 1]):
            next_p[i] -= Q(k, k + 1) * coefficient
        polynomials.append(next_p)
    return polynomials[n]


C = [tuple(i * coefficient for i, coefficient in enumerate(legendre(v + 1)) if i) for v in range(MAX_V + 1)]


def integrate_weighted(p):
    return sum((coefficient * (Q(2, k + 1) - Q(2, k + 3)) for k, coefficient in enumerate(p) if k % 2 == 0), Q(0))


@cache
def triple_integral(sorted_triple):
    p = [Q(1)]
    for v in sorted_triple:
        p = multiply(p, C[v])
    return integrate_weighted(p)


def integral_value(v1, v2, v3):
    integral = triple_integral(tuple(sorted((v1, v2, v3))))
    return Q((2 * v1 + 3) * (2 * v2 + 3), 32 * (v3 + 1) * (v3 + 2)) * integral


def symbolic_checks():
    a, b, c = sp.symbols("a b c", integer=True, nonnegative=True)
    s = a + b + c
    p = a + b
    f = sp.factorial
    half = lambda q: f(2 * q + 1) / (4 ** q * f(q))
    # DLMF 18.18.22 with m=b+c, n=a+c, k=c, lambda=3/2.
    rogers = ((p + sp.Rational(3, 2)) * f(p) / ((s + sp.Rational(3, 2)) * f(c) * f(b) * f(a))
              * half(c) * half(b) * half(a) * (f(s + 2) / 2)
              / (half(s) * (f(p + 2) / 2)))
    norm = 2 * (p + 1) * (p + 2) / (2 * p + 3)
    factored_integral = (4 * f(s + 1) * f(s + 2) / f(2 * s + 3)
                        * sp.prod(f(2 * j + 1) / f(j) ** 2 for j in (a, b, c)))
    ratio_integral = sp.combsimp(rogers * norm / factored_integral)
    v1, v2, v3 = b + c, a + c, a + b
    bridge = sp.Rational(1, 32) * (2 * v1 + 3) * (2 * v2 + 3) / ((v3 + 1) * (v3 + 2)) * factored_integral
    conjecture = (sp.Rational(1, 16) * (f(s + 1) / (f(a) * f(b) * f(c))) ** 2
                  * (2 * v1 + 3) * (2 * v2 + 3) / ((v3 + 1) * (v3 + 2))
                  * (2 * s + 4) * f(2 * a + 1) * f(2 * b + 1) * f(2 * c + 1) / f(2 * s + 3))
    ratio_formula = sp.combsimp(bridge / conjecture)
    assert ratio_integral == ratio_formula == 1
    return {"rogers_to_factorial_ratio": str(ratio_integral), "factorial_to_crw_ratio": str(ratio_formula)}


def main():
    symbolic = symbolic_checks()
    counts = {"admissible": 0, "forbidden": 0}
    for triple in product(range(MAX_V + 1), repeat=3):
        expected = square_pi(*triple)
        actual = integral_value(*triple)
        assert actual == expected, (triple, actual, expected)
        counts["admissible" if admissible(*triple) else "forbidden"] += 1
        assert dimension(triple[2]) * expected == dimension(triple[0]) * square_pi(triple[2], triple[1], triple[0])
    for v in range(MAX_V + 1):
        assert square_pi(v, 0, v) == Q(3, 16)
        assert square_pi(v, v, 0) == Q(3 * dimension(v), 16)
        assert square_pi(v, 1, v + 1) == Q(15 * (v + 1), 16 * (2 * v + 5))
        if v:
            assert square_pi(v, 1, v - 1) == Q(15 * (v + 2), 16 * (2 * v + 1))
    dimensions, overlaps, cartesian = cartesian_compute()
    for triple, value in cartesian.items():
        assert value == square_pi(*triple), (triple, value, square_pi(*triple))
    # Arithmetic illustrations, not an independently injected-mutation campaign.
    controls = {
        "standard_sphere_area_instead_of_bohr_measure": 2 * cartesian[(0, 0, 0)] != square_pi(0, 0, 0),
        "missing_output_dimension_division": dimension(2) * cartesian[(1, 1, 2)] != square_pi(1, 1, 2),
        "legendre_instead_of_gegenbauer": Q(25, 64) * integrate_weighted(multiply(legendre(1), legendre(1))) != square_pi(1, 1, 0),
        "nonzero_odd_parity_candidate": Q(1, 16) != integral_value(1, 1, 1),
        "nonzero_triangle_violating_candidate": Q(1, 16) != integral_value(0, 0, 2),
    }
    assert all(controls.values())
    report = {
        "verdict": "PASS", "arithmetic": "fractions.Fraction and exact SymPy; no floating-point comparisons",
        "python": sys.version.split()[0], "sympy": sp.__version__,
        "symbolic": symbolic,
        "univariate": {"maximum_each_seniority": MAX_V, "ordered_triples": (MAX_V + 1) ** 3, **counts},
        "cartesian": {"degrees": [0, 1, 2, 3], "dimensions": dimensions, "triple_overlaps_evaluated": overlaps, "ordered_triples": len(cartesian)},
        "arithmetic_illustrations": controls,
        "controls_pi_squared_R_squared": {"0,0,0": str(square_pi(0, 0, 0)), "1,1,0": str(square_pi(1, 1, 0)), "2,2,2": str(square_pi(2, 2, 2))},
        "cartesian_values_pi_squared_R_squared": {",".join(map(str, t)): str(v) for t, v in sorted(cartesian.items())},
        "scope": "Finite checks are controls, not the universal proof. See RESULTS.md, Theorem 1.",
    }
    source_hashes = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT / "source").iterdir()) if p.is_file()}
    code_hashes = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT / "code").glob("*.py"))}
    report["code_sha256"] = code_hashes
    (ROOT / "results" / "exact-checks.json").write_text(json.dumps(report, indent=2) + "\n")
    (ROOT / "results" / "source-sha256.json").write_text(json.dumps(source_hashes, indent=2) + "\n")
    print("PASS: symbolic ratios 1,1; exact univariate triples", (MAX_V + 1) ** 3, counts)
    print("PASS: Cartesian dimensions", dimensions, "; ordered triples", len(cartesian), "; overlaps", overlaps)
    print("PASS: arithmetic illustrations", sum(controls.values()), "; pi^2 R(2;2,2)^2 =", square_pi(2, 2, 2))
    verify_prior_art()


if __name__ == "__main__":
    main()
