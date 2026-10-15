"""Exact finite isotropic array decision and independently checked counterexamples.

No floating-point arithmetic is used. See proof.md for completeness and input encoding.
The default suite is bounded and single-threaded; --input runs the general procedure.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import hashlib
from itertools import combinations, product
import json
from math import prod
from pathlib import Path

import sympy as sp
from sympy.polys.polyclasses import ANP

HERE = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


class RealField:
    """Exact ordered Q(alpha), using rational root isolation rather than numerics."""

    def __init__(self, specification=None):
        self.t = sp.Symbol("t")
        if specification is None:
            self.poly = sp.Poly(self.t, self.t, domain=sp.QQ)
            self.interval = None
        else:
            coefficients = [self.rational(v) for v in specification["minimal_polynomial"]]
            self.poly = sp.Poly.from_list(coefficients, self.t, domain=sp.QQ).monic()
            require(self.poly.degree() >= 2 and self.poly.is_irreducible is True,
                    "The primitive polynomial must be irreducible of degree at least two")
            lo, hi = map(self.rational, specification["isolating_interval"])
            require(lo < hi and self.poly.eval(lo) != 0 and self.poly.eval(hi) != 0,
                    "Root isolation requires ordered nonroot rational endpoints")
            require(self.poly.count_roots(lo, hi) == 1, "Interval must isolate exactly one real root")
            self.interval = [lo, hi]
        self.modulus = self.poly.rep.to_list()
        self.zero = self.scalar(0)
        self.one = self.scalar(1)

    @staticmethod
    def rational(value):
        require(type(value) in (str, int), "Use exact rational strings/integers, not floats")
        return sp.Rational(value)

    def scalar(self, value):
        if isinstance(value, list):
            require(self.interval is not None, "Polynomial coordinates require an algebraic field")
            require(bool(value), "A coefficient list cannot be empty")
            coefficients = [self.rational(v) for v in reversed(value)]
            residue = sp.Poly.from_list(coefficients, self.t, domain=sp.QQ).rem(self.poly)
            return ANP(residue.rep.to_list(), self.modulus, sp.QQ)
        return ANP([sp.QQ.convert(self.rational(value))], self.modulus, sp.QQ)

    def encode(self, value):
        coefficients = value.to_sympy_list()
        if len(coefficients) <= 1:
            return str(coefficients[0] if coefficients else 0)
        return [str(v) for v in reversed(coefficients)]

    def sign(self, value):
        coefficients = value.to_sympy_list()
        if not coefficients:
            return 0
        if len(coefficients) == 1:
            return 1 if coefficients[0] > 0 else -1
        while True:
            a, b = self.interval
            lo = hi = sp.Rational(0)
            for coefficient in coefficients:
                products = (lo * a, lo * b, hi * a, hi * b)
                lo, hi = min(products) + coefficient, max(products) + coefficient
            if lo > 0:
                return 1
            if hi < 0:
                return -1
            mid = (a + b) / 2
            # An irreducible polynomial of degree >=2 has no rational root.
            require(self.poly.eval(mid) != 0, "Unexpected rational root of primitive polynomial")
            count = self.poly.count_roots(a, mid)
            require(count in (0, 1), "Root isolation invariant was lost")
            self.interval = [a, mid] if count == 1 else [mid, b]

    def integer(self, value):
        coefficients = value.to_sympy_list()
        if not coefficients:
            return 0
        if len(coefficients) == 1 and coefficients[0].q == 1:
            return int(coefficients[0])
        return None

    def floor_sqrt(self, value):
        require(self.sign(value) >= 0, "Cannot bound the square root of a negative value")
        lo, hi = 0, 1
        while self.sign(value - self.scalar(hi * hi)) >= 0:
            lo, hi = hi, 2 * hi
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.sign(value - self.scalar(mid * mid)) >= 0:
                lo = mid
            else:
                hi = mid
        return lo


def dot(a, b, zero):
    return sum((x * y for x, y in zip(a, b)), zero)


def rref(matrix, field, columns):
    rows = [list(row) for row in matrix]
    original = list(range(len(rows)))
    pivots, selected = [], []
    for col in range(columns):
        pivot = next((j for j in range(len(pivots), len(rows)) if rows[j][col]), None)
        if pivot is None:
            continue
        i = len(pivots)
        rows[i], rows[pivot] = rows[pivot], rows[i]
        original[i], original[pivot] = original[pivot], original[i]
        selected.append(original[i])
        scale = rows[i][col]
        rows[i] = [v / scale for v in rows[i]]
        for j in range(len(rows)):
            if j != i and rows[j][col]:
                scale = rows[j][col]
                rows[j] = [v - scale * w for v, w in zip(rows[j], rows[i])]
        pivots.append(col)
    return rows, pivots, selected


def inverse(matrix, field):
    n = len(matrix)
    augmented = [row + [field.one if i == j else field.zero for j in range(n)]
                 for i, row in enumerate(matrix)]
    reduced, pivots, _ = rref(augmented, field, n)
    require(len(pivots) == n, "Matrix is singular")
    return [row[n:] for row in reduced]


def decide(instance, max_candidates=None):
    field = RealField(instance.get("field"))
    raw = instance["positions"]
    require(bool(raw) and bool(raw[0]), "At least one sensor and one coordinate are required")
    d = len(raw[0])
    require(all(len(row) == d for row in raw), "Sensor coordinates must be rectangular")
    domain = instance.get("domain", "ball")
    require(domain in ("ball", "sphere"), "Domain must be closed unit ball or sphere")
    require(domain != "sphere" or d >= 2, "S^0 does not have the radius-two difference ball")
    positions = [[field.scalar(v) for v in row] for row in raw]
    differences = [[x - y for x, y in zip(row, positions[0])] for row in positions[1:]]
    reduced, pivots, selected = rref(differences, field, d)
    result = {"domain": domain, "dimension": d, "sensor_count": len(raw),
              "rank": len(pivots), "independent_rows": selected}

    def witness(delta):
        wraps = [field.integer(dot(row, delta, field.zero) / field.scalar(2))
                 for row in differences]
        require(any(delta) and all(v is not None for v in wraps), "Invalid alias witness")
        norm = dot(delta, delta, field.zero)
        require(field.sign(norm - field.scalar(4)) <= 0, "Alias witness outside difference domain")
        return {"verdict": "ALIASED", "delta": [field.encode(v) for v in delta],
                "delta_norm_squared": field.encode(norm), "wrapping_integers": wraps}

    if len(pivots) < d:
        free = next(j for j in range(d) if j not in pivots)
        delta = [field.zero for _ in range(d)]
        delta[free] = field.one
        for row, pivot in zip(reduced, pivots):
            delta[pivot] = -row[free]
        scale = field.scalar(field.floor_sqrt(dot(delta, delta, field.zero)) + 1)
        delta = [v / scale for v in delta]
        result.update({"method": "kernel", "candidates_examined": 0, **witness(delta)})
        return result

    basis_rows = [differences[j] for j in selected]
    inv = inverse(basis_rows, field)
    bounds = [field.floor_sqrt(dot(row, row, field.zero)) for row in basis_rows]
    count = prod(2 * bound + 1 for bound in bounds) - 1
    if max_candidates is not None and count > max_candidates:
        raise ValueError(f"Complete search requires {count} candidates, exceeding explicit cap; no verdict")
    result.update({"method": "bounded_integer_wrapping", "wrapping_bounds": bounds,
                   "complete_box_nonzero_count": count})
    examined = 0
    for integers in product(*(range(-bound, bound + 1) for bound in bounds)):
        if not any(integers):
            continue
        examined += 1
        k = [field.scalar(v) for v in integers]
        delta = [field.scalar(2) * dot(row, k, field.zero) for row in inv]
        if field.sign(dot(delta, delta, field.zero) - field.scalar(4)) > 0:
            continue
        if all(field.integer(dot(row, delta, field.zero) / field.scalar(2)) is not None
               for row in differences):
            result.update({"candidates_examined": examined, **witness(delta)})
            return result
    result.update({"verdict": "ALIAS_FREE", "candidates_examined": examined})
    require(examined == count, "Incomplete search cannot certify alias-free")
    return result


# Independent certificate arithmetic below uses Fraction, not the ordered ANP solver.
def fmatrix(rows):
    return [[F(v) for v in row] for row in rows]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, b):
    return [sum(x * y for x, y in zip(row, b)) for row in a]


def norm2(v):
    return sum(x * x for x in v)


def inv2(v):
    a, b = v[0]
    c, d = v[1]
    determinant = a * d - b * c
    require(determinant != 0, "Singular two-dimensional basis")
    return [[d / determinant, -b / determinant], [-c / determinant, a / determinant]]


def encode_fraction(value):
    if isinstance(value, (list, tuple)):
        return [encode_fraction(v) for v in value]
    if isinstance(value, dict):
        return {key: encode_fraction(v) for key, v in value.items()}
    return str(value) if isinstance(value, F) else value


def certify(certificate):
    v = fmatrix(certificate["basis"])
    positions = fmatrix(certificate["positions"])
    delta = list(map(F, certificate["delta"]))
    left = list(map(F, certificate["u"]))
    right = list(map(F, certificate["v"]))
    coefficients = certificate["integer_coefficients"]
    require(all(type(k) is int for k in coefficients), "Witness coefficients must be integers")
    differences = [[x - y for x, y in zip(row, positions[0])] for row in positions[1:]]
    derived = [[2 * x for x in row] for row in inv2(v)]
    require(differences == derived, "Sensor geometry is not the independently derived 2V^-1")
    require(mm(differences, v) == [[F(2), F(0)], [F(0), F(2)]], "DV is not 2I")
    require(mv(v, coefficients) == delta, "Wrong lattice witness")
    require([x - y for x, y in zip(left, right)] == delta, "Directions have wrong difference")
    require(any(delta) and norm2(left) <= 1 and norm2(right) <= 1, "Invalid physical directions")
    phases_left, phases_right = mv(positions, left), mv(positions, right)
    relative = [x - y for x, y in zip(phases_left, phases_right)]
    require(all(((x - relative[0]) / 2).denominator == 1 for x in relative),
            "Original-data steering vectors are not projectively equal")
    binary = [mv(v, c) for c in product((0, 1), repeat=2) if any(c)]
    vertices = [[F(0), F(0)], *binary]
    pair_norms = [norm2([x - y for x, y in zip(a, b)]) for a, b in combinations(vertices, 2)]
    return encode_fraction({"binary_norm_squares": [norm2(x) for x in binary],
                            "pairwise_vertex_norm_squares": pair_norms,
                            "equation_11_passes": all(norm2(x) > 4 for x in binary),
                            "corollary_5_passes": all(q > 4 for q in pair_norms),
                            "phase_over_pi_u": phases_left, "phase_over_pi_v": phases_right,
                            "phase_difference_over_two_pi": [x / 2 for x in relative],
                            "delta_norm_squared": norm2(delta)})


def gauss_reduce(raw):
    original = fmatrix(raw)
    columns = [list(col) for col in zip(*original)]
    transform = [[1, 0], [0, 1]]  # columns, matching columns above
    while True:
        if norm2(columns[0]) > norm2(columns[1]):
            columns.reverse()
            transform.reverse()
        a = norm2(columns[0])
        c = sum(x * y for x, y in zip(*columns))
        if 2 * abs(c) <= a:
            break
        q = (c / a + F(1, 2)).__floor__()
        require(q != 0, "Nonterminal Gauss reduction must change the basis")
        columns[1] = [y - q * x for x, y in zip(*columns)]
        transform[1] = [y - q * x for x, y in zip(*transform)]
    reduced = list(map(list, zip(*columns)))
    u = list(map(list, zip(*transform)))
    require(abs(u[0][0] * u[1][1] - u[0][1] * u[1][0]) == 1, "Not unimodular")
    require(mm(original, u) == reduced, "Reduction changed the lattice")
    require(norm2(columns[0]) <= norm2(columns[1]) and
            2 * abs(sum(x * y for x, y in zip(*columns))) <= norm2(columns[0]),
            "Basis is not Gauss reduced")
    return encode_fraction({"basis": reduced, "unimodular_transform": u,
                            "shortest_norm_squared_by_lemma": norm2(columns[0])})


def classify_responses(left, right):
    left_nonzero, right_nonzero = any(left), any(right)
    if not left_nonzero or not right_nonzero:
        return "both_blind" if not left_nonzero and not right_nonzero else "one_blind"
    return "projective" if all(sp.expand(x * w - y * z) == 0
                               for (x, y), (z, w) in combinations(zip(left, right), 2)) else "distinct"


def suite(max_candidates):
    cases = json.loads((HERE / "sources/exact-instances.json").read_text())
    result = {"counterexamples": {}, "decision_cases": {}, "controls": {}}
    for name, certificate in cases["counterexamples"].items():
        certification = certify(certificate)
        decision = decide({"positions": certificate["positions"]}, max_candidates)
        reduction = gauss_reduce(certificate["basis"])
        require(decision["verdict"] == "ALIASED", "Counterexample was not detected")
        require(certification["equation_11_passes"], "Equation (11) no longer passes witness")
        require(certification["corollary_5_passes"] == (name == "C"), "Conflated shortcut tests")
        require(reduction["shortest_norm_squared_by_lemma"] ==
                ("1/10" if name == "E" else "9/100"), "Wrong reduced shortest norm")
        result["counterexamples"][name] = {"certificate": certification,
                                          "bounded_decision": decision, "gauss_reduction": reduction}
    for name, case in cases["decisions"].items():
        decision = decide(case, max_candidates)
        require(decision["verdict"] == case["expected"], f"Wrong verdict for {name}")
        result["decision_cases"][name] = decision
    extension = fmatrix([["3", "30", "0"], ["0", "3/10", "0"], ["0", "0", "3"]])
    vertices = [mv(extension, c) for c in product((0, 1), repeat=3)]
    pair_squares = [norm2([x - y for x, y in zip(a, b)])
                    for a, b in combinations(vertices, 2)]
    require(min(pair_squares) == 9 and
            result["decision_cases"]["sphere_counterexample_C_extension"]["verdict"] == "ALIASED",
            "Three-dimensional all-pairs shortcut refutation failed")
    result["controls"]["three_dimensional_vertex_shortcut_refuted"] = {
        "passed": True, "minimum_vertex_pair_squared_distance": "9",
        "short_alias_squared_norm": "9/100"}
    translated_phase_difference = [F(2, 3), F(8, 3)]
    require(all((q / 2).denominator != 1 for q in translated_phase_difference) and
            ((translated_phase_difference[1] - translated_phase_difference[0]) / 2).denominator == 1,
            "Common-phase projective control failed")
    result["controls"]["unknown_common_phase_not_literal_equality"] = {"passed": True}

    def rejection(name, action):
        try:
            action()
        except ValueError as error:
            result["controls"][name] = {"rejected": True, "reason": str(error)}
        else:
            raise ValueError(f"Tamper control {name} was accepted")

    original = cases["counterexamples"]["E"]
    changed = deepcopy(original)
    changed["delta"][0] = "-9/100"
    rejection("changed_witness", lambda: certify(changed))
    changed = deepcopy(original)
    changed["positions"][1][0] = "203/300"
    rejection("changed_sensor", lambda: certify(changed))
    changed = deepcopy(original)
    changed["basis"][0][0] = "31/10"
    rejection("changed_basis", lambda: certify(changed))
    changed = deepcopy(original)
    changed["u"] = ["2", "2"]
    rejection("changed_direction", lambda: certify(changed))
    rejection("false_alias_free_boundary_claim", lambda: require(
        result["decision_cases"]["half_wave_closed_boundary"]["verdict"] == "ALIAS_FREE",
        "Closed-domain boundary alias refutes the claimed verdict"))
    rejection("false_equation_11_sufficiency", lambda: require(
        not result["counterexamples"]["E"]["certificate"]["equation_11_passes"] or
        result["counterexamples"]["E"]["bounded_decision"]["verdict"] == "ALIAS_FREE",
        "Positive binary test is contradicted by exact original-data alias"))
    rejection("false_corollary_5_sufficiency", lambda: require(
        not result["counterexamples"]["C"]["certificate"]["corollary_5_passes"] or
        result["counterexamples"]["C"]["bounded_decision"]["verdict"] == "ALIAS_FREE",
        "All-pairs vertex test is contradicted by exact original-data alias"))
    rejection("truncated_search_has_no_verdict", lambda: decide(
        {"positions": cases["counterexamples"]["C"]["positions"]}, 1))
    rejection("floating_coordinate", lambda: decide({"positions": [[0], [0.5]]}))
    rejection("sphere_dimension_one", lambda: decide({"positions": [[0], [1]], "domain": "sphere"}))
    rejection("reducible_primitive_polynomial", lambda: RealField(
        {"minimal_polynomial": [1, 0, -1], "isolating_interval": [0, 2]}))
    rejection("unisolated_primitive_root", lambda: RealField(
        {"minimal_polynomial": [1, 0, -2], "isolating_interval": [-2, 2]}))
    field = RealField({"minimal_polynomial": [1, 0, -2], "isolating_interval": [1, 2]})
    alpha = field.scalar([0, 1])
    require(field.sign(alpha * alpha - field.scalar(2)) == 0, "Exact algebraic identity failed")
    require(field.sign(alpha - field.scalar("7/5")) == 1, "Positive algebraic sign failed")
    rejection("false_algebraic_identity", lambda: require(
        field.sign(alpha - field.scalar("7/5")) == 0, "sqrt(2) is not 7/5"))
    result["controls"]["exact_algebraic_identity_and_sign"] = {"passed": True}
    response_cases = {
        "complex_projective": ([1, sp.I, 0], [sp.I, -1, 0], "projective"),
        "same_support_not_proportional": ([1, 1], [1, 2], "distinct"),
        "different_support": ([1, 0], [1, 1], "distinct"),
        "one_blind": ([0, 0], [1, 0], "one_blind"),
        "two_blind": ([0, 0], [0, 0], "both_blind"),
    }
    for name, (left, right, expected) in response_cases.items():
        actual = classify_responses(left, right)
        require(actual == expected, f"Wrong projective/zero response handling: {name}")
        result["controls"][name] = {"passed": True, "classification": actual}
    # A one-sensor active taper gives constant magnitude although the full array is injective.
    require(result["decision_cases"]["strict_half_wave"]["verdict"] == "ALIAS_FREE",
            "Positive full-array control failed")
    require(classify_responses([1], [-1]) == "projective", "Single active sensor must alias")
    result["controls"]["single_sensor_weighting_counterexample"] = {"passed": True}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Exact array JSON; omit to run the fixed certificate suite")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-candidates", type=int, help="Fail without a verdict if complete box exceeds this cap")
    args = parser.parse_args()
    if args.input:
        payload = {"decision": decide(json.loads(args.input.read_text()), args.max_candidates)}
        files = [args.input, Path(__file__)]
    else:
        payload = suite(args.max_candidates)
        files = [Path(__file__), HERE / "proof.md", *sorted((HERE / "sources").iterdir())]
    payload["verification"] = {"arithmetic": "exact rational / algebraic residues with rational root isolation",
                               "sympy_version": sp.__version__, "threads": 1,
                               "source_sha256": {str(p.relative_to(HERE)) if p.is_relative_to(HERE) else str(p):
                                                 hashlib.sha256(p.read_bytes()).hexdigest()
                                                 for p in files if p.is_file()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "status": "VERIFIED",
                      "counterexamples": len(payload.get("counterexamples", {})),
                      "decision_cases": len(payload.get("decision_cases", {})),
                      "controls": len(payload.get("controls", {}))}))


if __name__ == "__main__":
    main()
