#!/usr/bin/env python3
"""Fixed deficit-five closed matrices and exact checks, not a second CFP core.

The only general CFP/occupation engine is imported read-only from the sibling.
Our formula consists of fixed integer coefficient matrices and diagonal rational
weights; it has no recursion in particle number and performs no fitted search.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
from math import comb, factorial
from pathlib import Path
import platform
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT.parent / "phys-fractional-parentage-coefficients" / "code"
sys.path.insert(0, str(SHARED))
import sympy as sp
from sympy.physics.wigner import clebsch_gordan
from flint import fmpq
import flint
from fpc_core import SpinBosons
from top_family_symbolic import Deficit

f, v = sp.symbols("f v", positive=True, integer=True)
PARTS = {
    0: [()],
    2: [(2,), (1, 1)],
    3: [(3,), (2, 1), (1, 1, 1)],
    4: [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)],
    5: [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)],
}
C = {
    0: sp.Matrix([[1]]),
    2: sp.Matrix([[1], [-1]]),
    3: sp.Matrix([[1], [-3], [2]]),
    4: sp.Matrix([[1, 0], [-4, 0], [3, 1], [0, -2], [0, 1]]),
    5: sp.Matrix([[1, 0], [-5, 0], [2, 1], [8, -1], [-6, -3], [0, 5], [0, -2]]),
}
MIN_DEGREE = {0: [0], 2: [2], 3: [3], 4: [2, 4], 5: [3, 5]}
# Multiplication of each daughter covariant by z_(5-k), in the fixed parent rows.
INSERT = {
    0: sp.Matrix([[1], [0], [0], [0], [0], [0], [0]]),
    2: sp.Matrix([[0], [0], [1], [-1], [0], [0], [0]]),
    3: sp.Matrix([[0], [0], [1], [0], [-3], [2], [0]]),
    4: sp.Matrix([[0, 0], [1, 0], [0, 0], [-4, 0], [3, 1], [0, -2], [0, 1]]),
    5: C[5],
}


def factored(matrix):
    return matrix.applyfunc(lambda x: sp.factor(sp.cancel(x)))


def orbital_weight(spin, j):
    return sp.factorial(j) / sp.ff(2 * spin, j)


def active(k, degree):
    return [i for i, minimum in enumerate(MIN_DEGREE[k])
            if not sp.sympify(degree).is_Integer or degree >= minimum]


def monomial_weight(partition, degree, spin):
    """Fock norm divided by degree!, explicitly rational for each fixed row."""
    counts = Counter(partition)
    return sp.prod(sp.factorial(count) * orbital_weight(spin, j) ** count
                   for j, count in counts.items()) / sp.ff(degree, len(partition))


def gram(k, degree, spin=f):
    cols = active(k, degree)
    rows = [i for i, part in enumerate(PARTS[k])
            if not sp.sympify(degree).is_Integer or len(part) <= degree]
    coefficients = C[k].extract(rows, cols)
    diagonal = sp.diag(*[monomial_weight(PARTS[k][i], degree, spin) for i in rows])
    return factored(coefficients.T * diagonal * coefficients)


def insertion(k, degree, spin=f):
    rows = [i for i, part in enumerate(PARTS[5])
            if not sp.sympify(degree).is_Integer or len(part) <= degree]
    parent = C[5].extract(rows, active(5, degree))
    daughter = INSERT[k].extract(rows, active(k, degree - 1))
    diagonal = sp.diag(*[monomial_weight(PARTS[5][i], degree, spin) for i in rows])
    return factored(parent.T * diagonal * daughter)


def cg_square(k, degree, spin=f):
    j = 5 - k
    L, Lp = spin * degree - 5, spin * (degree - 1) - k
    return sp.prod((2 * Lp - i) / (2 * L + 2 + i) for i in range(j))


def orthogonalizer(G):
    T = sp.eye(G.rows)
    if G.rows == 2:
        T[0, 1] = -G[0, 1] / G[0, 0]
    H = factored(T.T * G * T)
    assert H.is_diagonal()
    return factored(T), [H[i, i] for i in range(G.rows)]


def formulas(degree=v, spin=f):
    Gp = gram(5, degree, spin)
    Tp, hp = orthogonalizer(Gp)
    blocks = {}
    total = sp.zeros(Gp.rows)
    for k in PARTS:
        if not active(k, degree - 1):
            continue
        Gd = gram(k, degree - 1, spin)
        Td, hd = orthogonalizer(Gd)
        X = insertion(k, degree, spin)
        cg = sp.factor(cg_square(k, degree, spin))
        denominator = orbital_weight(spin, 5 - k) * cg
        Y = factored(Tp.T * X * Td)
        squares = sp.Matrix(Gp.rows, Gd.rows, lambda i, j:
                            sp.factor(sp.cancel(Y[i, j] ** 2 / (denominator * hp[i] * hd[j]))))
        blocks[k] = {"X": X, "G_daughter": Gd, "Y": Y, "h_daughter": hd,
                     "cg_squared": cg, "denominator": sp.factor(denominator),
                     "squares": squares, "cg_sign": (-1) ** (5 - k)}
        total += X * Gd.inv() * X.T / denominator
    residual = factored(total - Gp)
    assert residual == sp.zeros(Gp.rows), (degree, residual)
    return Gp, hp, blocks


def deficit_polynomials(k, degree):
    polynomials = []
    for col in active(k, degree):
        p = {}
        for part, coefficient in zip(PARTS[k], C[k][:, col]):
            if coefficient:
                counts = Counter(part)
                p[tuple(counts.get(j, 0) for j in range(1, 6))] = coefficient
        polynomials.append(p)
    return polynomials


def symbolic_controls(Gp, blocks):
    D = Deficit(f, 5)
    parents = deficit_polynomials(5, v)
    for k in PARTS:
        ps = deficit_polynomials(k, v)
        for p in ps:
            assert D.splus(p) == {}
        # Formula weights use n!; shared Deficit uses (n-k)!.
        other = sp.Matrix(len(ps), len(ps), lambda i, j:
                          D.inner(ps[i], ps[j], v, k) / sp.ff(v, k))
        assert factored(other - gram(k, v)) == sp.zeros(len(ps))
        ds = deficit_polynomials(k, v - 1)
        other_x = sp.Matrix(2, len(ds), lambda i, j:
                            D.inner(parents[i], D.mul_z(ds[j], 5 - k), v, 5) / sp.ff(v, 5))
        assert factored(other_x - blocks[k]["X"]) == sp.zeros(2, len(ds))
    bad = dict(parents[0])
    bad[(0, 0, 0, 0, 1)] = 2
    assert D.splus(bad), "highest-weight negative control not detected"
    missing = factored(blocks[4]["X"] * blocks[4]["G_daughter"].inv() *
                       blocks[4]["X"].T / blocks[4]["denominator"])
    assert missing.subs({f: 3, v: 6}) != sp.zeros(2), "missing-block negative control not detected"


def as_rational(x):
    return sp.Rational(int(x.p), int(x.q))


def occupation_basis(k, degree, B):
    output = []
    for col in active(k, degree):
        poly = {}
        for part, coefficient in zip(PARTS[k], C[k][:, col]):
            if not coefficient:
                continue
            exponents = [0] * B.D
            exponents[2 * B.f] = degree - len(part)
            assert exponents[2 * B.f] >= 0
            for j in part:
                exponents[2 * B.f - j] += 1
            poly[tuple(exponents)] = fmpq(int(coefficient))
        for previous in output:
            ratio = B.inner(previous, poly) / B.norm2(previous)
            for key, coefficient in previous.items():
                poly[key] = poly.get(key, fmpq(0)) - ratio * coefficient
            poly = {key: coefficient for key, coefficient in poly.items() if coefficient}
        assert B.norm2(poly) > 0 and not B.splus(poly) and not B.pair_ann(poly)
        output.append(poly)
    return output


def numeric_controls(stable, exceptions):
    checks = 0
    blocks_checked = 0
    for spin in range(3, 8):
        B = SpinBosons(spin)
        for degree in range(3, 11):
            data = stable if degree >= 6 else exceptions[degree]
            _, _, blocks = data
            parent = occupation_basis(5, degree, B)
            assert len(B.hw_harmonic_basis(degree, spin * degree - 5)) == len(parent)
            all_squares = [[] for _ in parent]
            for k, block in blocks.items():
                daughters = occupation_basis(k, degree - 1, B)
                assert len(B.hw_harmonic_basis(degree - 1, spin * (degree - 1) - k)) == len(daughters)
                for i, p in enumerate(parent):
                    for j, d in enumerate(daughters):
                        actual, sign = B.cfp_sq_sign(p, degree, spin * degree - 5, d, spin * (degree - 1) - k)
                        expected = block["squares"][i, j].subs({f: spin, v: degree})
                        y = block["Y"][i, j].subs({f: spin, v: degree})
                        expected_sign = int(sp.sign(y)) * block["cg_sign"]
                        assert expected == as_rational(actual), (spin, degree, k, i, j)
                        assert sign == expected_sign, ("phase", spin, degree, k, i, j)
                        all_squares[i].append(expected)
                        checks += 1
                blocks_checked += 1
            assert all(sum(row) == 1 for row in all_squares)
        for degree in (1, 2):
            L = spin * degree - 5
            if L >= 0:
                assert not B.hw_harmonic_basis(degree, L)
    return checks, blocks_checked


def tensor_amplitudes(poly, degree, spin):
    """Ordered first-quantized tensor, independently normalized by direct sum."""
    amplitudes = {}
    for values in product(range(-spin, spin + 1), repeat=degree):
        counts = tuple(values.count(m) for m in range(-spin, spin + 1))
        coefficient = poly.get(counts)
        if coefficient:
            weight = sp.prod(sp.Rational(1, comb(2 * spin, spin + m)) ** a
                             for m, a in zip(range(-spin, spin + 1), counts))
            amplitudes[values] = as_rational(coefficient) * sp.prod(factorial(a) for a in counts) * sp.sqrt(weight)
    norm = sp.sqrt(sum(a * a for a in amplitudes.values()))
    return {key: sp.simplify(value / norm) for key, value in amplitudes.items()}


def first_quantized_control():
    spin, degree = 3, 3
    B = SpinBosons(spin)
    (p,) = occupation_basis(5, degree, B)
    parent = tensor_amplitudes(p, degree, spin)
    L = spin * degree - 5
    signs_checked = 0
    for k in (0, 2, 4):
        (daughter,) = occupation_basis(k, degree - 1, B)
        Lp = spin * (degree - 1) - k
        overlap = 0
        lowered = dict(daughter)
        for M in range(Lp, -Lp - 1, -1):
            m = L - M
            if -spin <= m <= spin:
                tensor = tensor_amplitudes(lowered, degree - 1, spin)
                cg = clebsch_gordan(spin, Lp, L, m, M, L)
                overlap += cg * sum(parent.get((m,) + key, 0) * value for key, value in tensor.items())
            lowered = B.sminus(lowered)
        overlap = sp.simplify(overlap)
        square, sign = B.cfp_sq_sign(p, degree, L, daughter, Lp)
        assert sp.simplify(overlap ** 2 - as_rational(square)) == 0
        assert int(sp.sign(overlap)) == sign
        expected_signed = sign * sp.sqrt(as_rational(square))
        wrong_phase = -overlap
        assert sp.simplify(wrong_phase - expected_signed) != 0, "odd-phase mutation was accepted"
        signs_checked += 1
    return signs_checked


def serial(data):
    if isinstance(data, sp.MatrixBase):
        return [[str(x) for x in row] for row in data.tolist()]
    if isinstance(data, dict):
        return {str(key): serial(value) for key, value in data.items()}
    if isinstance(data, (list, tuple)):
        return [serial(value) for value in data]
    return str(data) if isinstance(data, sp.Basic) else data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    stable = formulas()
    symbolic_controls(stable[0], stable[2])
    exceptions = {degree: formulas(sp.Integer(degree)) for degree in (3, 4, 5)}
    checks, block_checks = numeric_controls(stable, exceptions)
    tensor_checks = first_quantized_control()
    output = {
        "scope": "integer f>=3; parent L=f*v-5; reduced v->v-1 branch only",
        "basis_order": "C5 first, H2*T3 second; Q4 first, H2^2 second in deficit four",
        "formula": "r_ij=(-1)^(5-k)*Y_ij/sqrt(denominator*h_parent_i*h_daughter_j)",
        "stable_domain": "v>=6",
        "stable": {"G_parent": stable[0], "h_parent": stable[1], "blocks": stable[2]},
        "exceptions": {degree: {"G_parent": data[0], "h_parent": data[1], "blocks": data[2]}
                       for degree, data in exceptions.items()},
        "absence": "No parent deficit-five state at v=0,1,2",
    }
    receipt = {
        "status": "PASS", "python": platform.python_version(), "sympy": sp.__version__,
        "python_flint": flint.__version__, "symbolic_completeness_domains": ["Q(f,v), v>=6", "Q(f), v=3", "Q(f), v=4", "Q(f), v=5"],
        "signed_numeric_CFP_checks": checks, "daughter_block_checks": block_checks,
        "numeric_domain": "f=3..7, v=3..10", "first_quantized_signed_checks": tensor_checks,
        "negative_controls": ["perturbed C5 highest-weight coefficient", "omitted deficit-four daughter block", "reversed odd-j phase in first-quantized comparison"],
        "shared_core": str(SHARED / "fpc_core.py"), "shared_core_usage": "read-only import, bytecode writes disabled",
        "proof_boundary": "Universal statement follows from fixed matrices and algebra in RESULTS.md, not finite sampling or model review.",
    }
    if args.write:
        (ROOT / "results" / "closed-form.json").write_text(json.dumps(serial(output), indent=2) + "\n")
        (ROOT / "results" / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: stable Q(f,v) identity and all three low-v Q(f) identities")
    print(f"PASS: {checks} signed CFP comparisons; {block_checks} daughter blocks; f=3..7, v=3..10")
    print(f"PASS: {tensor_checks} independent first-quantized signed overlaps; 3 negative controls")


if __name__ == "__main__":
    main()
