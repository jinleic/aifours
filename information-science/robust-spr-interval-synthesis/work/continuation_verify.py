"""Exact finite controls for the all-order written proofs in theory.md, I--M.

This is not a proof assistant or a general SPR decision theorem. It checks the
moment signs, sign-definite minor formula, a degree-seven contact countercontrol,
the necessary phase filter, and closed-to-strict perturbations. All arithmetic is rational.
Run from any directory; --output allows a parent replay without replacing evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from enumerate_configs import PAT, QUAD, region_ok
from exact_verify import (
    CORNERS, T, box_stable_exact, is_hurwitz_exact, pairing_polys,
    positivity_certificate, verify_numerator,
)

S = sp.Symbol("s")


def ascending(poly):
    return [poly.nth(k) for k in range(poly.degree() + 1)]


def components(coefficients):
    return tuple(sp.Poly(sum((-1)**k * c * T**k for k, c in enumerate(coefficients[p::2])), T)
                 for p in (0, 1))


def moment_checks():
    records = []
    for n in range(3, 13):
        for infinity in (False, True):
            m = n if infinity else n + 1
            for degree in ((n - 1,) if infinity else (n - 1, n)):
                for origin in (False, True):
                    for zero_node in ((False, True) if origin else (False,)):
                        if infinity and zero_node and n % 2 == 0:
                            continue
                        b = sp.Poly(S**int(origin) * (S + 1)**(degree - int(origin)), S)
                        eb, ob = components(ascending(b))
                        nodes = list(map(sp.Integer, range(int(not zero_node), m + int(not zero_node))))
                        kappa = sp.Integer((-1)**(m - 1) if zero_node and not infinity else 1)
                        eta = [1 / sp.prod(x - y for y in nodes if y != x) for x in nodes]
                        z = [kappa * e * ob.eval(x) for x, e in zip(nodes, eta)]
                        y = [-kappa * e * eb.eval(x) for x, e in zip(nodes, eta)]
                        mu_inf = b.nth(n - 1) if infinity else sp.Integer(0)
                        moments = [sp.factor((-1)**(k // 2) * sum(
                            x**(k // 2) * v for x, v in zip(nodes, y if k % 2 else z)))
                            for k in range(n + 1)]
                        moments[n] += mu_inf
                        assert all(value == 0 for value in moments)
                        assert all(eb.eval(x) * zz + ob.eval(x) * yy == 0
                                   for x, zz, yy in zip(nodes, z, y))
                        if zero_node:
                            assert y[0] == 0 and z[0] > 0
                        records.append({"n": n, "degree": degree, "infinity": infinity,
                                        "origin_zero": origin, "zero_node": zero_node,
                                        "nodes": m, "all_moments_zero": True})
    return {"scope": "Interpolation identities only; no stable denominators are manufactured.",
            "count": len(records), "cases": records}


def vandermonde(nodes):
    return sp.prod(nodes[j] - nodes[i] for i in range(len(nodes)) for j in range(i + 1, len(nodes)))


def determinant_checks():
    records = []
    for n in range(3, 13):
        m = n - 2
        nodes = list(map(sp.Integer, range(1, m + 1)))
        ratios = [(-1)**(j + 1) * sp.Rational(j + 2, j + 3) for j in range(1, m + 1)]
        for p in range(min(m, n // 2 + 1) + 1):
            q = m - p
            if q > (n - 1) // 2 + 1:
                continue
            matrix = sp.Matrix([[x**k for k in range(p)] + [r * x**k for k in range(q)]
                                for x, r in zip(nodes, ratios)])
            expansion = sp.Integer(0)
            expected_sign = (-1)**(q + sum(range(p + 1, m + 1)))
            for selected in itertools.combinations(range(m), q):
                complement = [i for i in range(m) if i not in selected]
                laplace_sign = (-1)**(sum(i + 1 for i in selected) + sum(range(p + 1, m + 1)))
                term = (laplace_sign * sp.prod(ratios[i] for i in selected)
                        * vandermonde([nodes[i] for i in complement])
                        * vandermonde([nodes[i] for i in selected]))
                assert sp.sign(term) == expected_sign
                expansion += term
            determinant = matrix.det()
            assert determinant == expansion and sp.sign(determinant) == expected_sign
            records.append({"n": n, "P": p, "Q": q, "determinant": str(determinant),
                            "all_laplace_terms_same_sign": True})
    return {"scope": "Finite exact controls of the universal determinant identity, not its proof.",
            "count": len(records), "cases": records}


def hypothesis_controls():
    cases = [
        ("fixed_linear", [1, 2, 2, 1], [3, 2, 2, 1], [0, 2, 0, 1], T * (2 - T)**2),
        ("fixed_constant", [1, 1, 2, 1], [1, 2, 2, 1], [1, 0, 2], (1 - 2*T)**2),
    ]
    results = []
    for name, lo, hi, b, expected in cases:
        assert box_stable_exact(lo, hi)
        pairings = pairing_polys(lo, hi, b)
        assert all(poly == sp.Poly(expected, T, domain=sp.QQ) for poly in pairings)
        eb, ob = components(b)
        assert eb.is_zero or ob.is_zero
        results.append({"case": name, "box_hurwitz": True, "lower_ascending": lo,
                        "upper_ascending": hi, "b_ascending": b,
                        "all_four_pairings": str(expected), "has_imaginary_zeros": True})
    assert box_stable_exact([1, 1, 1], [2, 2, 1])
    assert components([0, 1])[0].is_zero
    results.append({"case": "degree_two", "box_hurwitz": True,
                    "lower_ascending": [1, 1, 1], "upper_ascending": [2, 2, 1],
                    "b_ascending": [0, 1], "pairing": "a_1*t >= 0", "E_b_zero": True})
    return results


def boundary_control():
    nodes = list(map(sp.Integer, (1, 11, 12, 134, 137, 1505, 1508)))
    ep = [sp.Poly(-2240 * (T - 1) * (T - 134) * (T - 137), T),
          sp.Poly(-400 * (T - 11) * (T - 12) * (T - 1505), T),
          sp.Poly(-(T - 11) * (T - 137) * (T - 1505), T),
          sp.Poly(-(T - 12) * (T - 134) * (T - 1508), T)]
    widths = [ep[1] - ep[0], ep[3] - ep[2]]
    assert all(c > 0 for p in widths for c in p.all_coeffs())
    lo, hi = [], []
    for k in range(8):
        offset = 2 * (k % 2)
        sign = (-1)**(k // 2)
        values = [sign * ep[offset + j].nth(k // 2) for j in range(2)]
        lo.append(min(values))
        hi.append(max(values))
    assert lo[-1] == hi[-1] == 1
    assert all(a < b for a, b in zip(lo[:-1], hi[:-1]))

    rows, labels = [], []
    for x in nodes[1:-1]:
        ei = next(i for i in range(2) if ep[i].eval(x) == 0)
        oi = next(i for i in range(2) if ep[2 + i].eval(x) == 0)
        de, do = ep[ei].diff().eval(x), ep[2 + oi].diff().eval(x)
        rows.append([(-1)**(k // 2) * x**(k // 2 + k % 2) * (do if k % 2 else de)
                     for k in range(8)])
        labels.append((ei, oi))
    matrix = sp.Matrix(rows)
    assert matrix.rank() == 5
    unknown = sp.symbols("b1:6")

    def numerator(constant):
        b = sp.Matrix([constant, *unknown, 1, 1])
        solution = sp.solve(list(matrix * b), unknown)
        assert set(solution) == set(unknown)
        result = list(b.subs(solution))
        assert all(value.is_Rational and value > 0 for value in result)
        assert matrix * sp.Matrix(result) == sp.zeros(5, 1)
        assert is_hurwitz_exact(result)
        return result

    good, bad = numerator(1), numerator(1000000)
    bad_pairs = pairing_polys(lo, hi, bad)
    bad_pairing = bad_pairs[0].eval(2)
    assert bad_pairing == -sp.Rational(139916915046677619005320581891582600,
                                     6256410274897111573321)
    bad_e, bad_o = components(bad)
    local_checks = []
    for index, (x, (ei, oi)) in enumerate(zip(nodes[1:-1], labels), 1):
        pairing = bad_pairs[CORNERS.index((ei, oi))]
        curvature = pairing.diff().diff().eval(x)
        re, remainder_e = sp.div(ep[ei], sp.Poly(x - T, T))
        ro, remainder_o = sp.div(ep[2 + oi], sp.Poly(x - T, T))
        assert remainder_e.is_zero and remainder_o.is_zero
        orientation = bad_o.eval(x) * re.eval(x) - bad_e.eval(x) * ro.eval(x)
        q_b = int(bad_e.count_roots(0, x) + bad_o.count_roots(0, x))
        q_rho = int(re.count_roots(0, x) + ro.count_roots(0, x))
        minimizing = (0 if bad_e.eval(x) > 0 else 1, 0 if bad_o.eval(x) > 0 else 1)
        assert curvature > 0 and orientation > 0
        assert minimizing == (ei, oi) and q_b == index and q_rho == index - 1
        values = [poly.eval(x) for poly in bad_pairs]
        assert all(v >= 0 for v in values) and sum(v == 0 for v in values) == 1
        local_checks.append({"t": str(x), "corner": [ei, oi], "second_derivative": str(curvature),
                             "orientation_without_positive_sqrt_t": str(orientation),
                             "numerator_quadrant": q_b, "cofactor_quadrant": q_rho,
                             "minimizing_corner": list(minimizing),
                             "four_pairing_values": list(map(str, values))})
    good_pairs = pairing_polys(lo, hi, good)
    residuals, corner_factors = [], []
    for (ei, oi), pairing in zip(CORNERS, good_pairs):
        roots = [x for x, label in zip(nodes[1:-1], labels) if label == (ei, oi)]
        square = sp.Poly(sp.prod((T - x)**2 for x in roots), T)
        quotient, remainder = sp.div(pairing, square)
        assert remainder.is_zero
        certificate = positivity_certificate(quotient)
        assert certificate["ok"]
        residuals.append({"corner": [ei, oi], "contacts": list(map(str, roots)),
                          "residual_coefficients_ascending": list(map(str, ascending(quotient))),
                          "sturm": certificate})
        a = sp.Poly(ep[ei].as_expr().subs(T, -S**2)
                    + S * ep[2 + oi].as_expr().subs(T, -S**2), S)
        marginal_factor = sp.Poly(sp.prod(S**2 + x for x in roots), S)
        reduced, remainder = sp.div(a, marginal_factor)
        assert remainder.is_zero and is_hurwitz_exact(ascending(reduced))
        corner_factors.append({"corner": [ei, oi], "imaginary_factors": list(map(str, roots)),
                               "remaining_hurwitz_coefficients_ascending": list(map(str, ascending(reduced))),
                               "remaining_routh_positive": True})

    inner_lo = [(3 * a + b) / 4 for a, b in zip(lo, hi)]
    inner_hi = [(a + 3 * b) / 4 for a, b in zip(lo, hi)]
    assert box_stable_exact(inner_lo, inner_hi)
    inner = verify_numerator(inner_lo, inner_hi, good)
    assert inner["ok"]
    return {"scope": "A marginal box in the stable closure, NOT a book counterexample.",
            "nodes": list(map(str, nodes)), "lower_ascending": list(map(str, lo)),
            "upper_ascending": list(map(str, hi)),
            "widths_ascending": [list(map(str, ascending(p))) for p in widths],
            "contact_matrix": [[str(value) for value in row] for row in rows],
            "contact_rank": 5, "contact_nullity": 3,
            "corner_factor_certificates": corner_factors,
            "bad_numerator_ascending": list(map(str, bad)), "bad_is_hurwitz": True,
            "bad_contact_residuals": ["0"] * 5, "bad_all_coefficients_positive": True,
            "negative_pairing": {"corner": [0, 0], "t": "2", "value": str(bad_pairing)},
            "bad_local_contact_checks": local_checks,
            "good_numerator_ascending": list(map(str, good)), "good_is_hurwitz": True,
            "good_residual_certificates": residuals,
            "half_width_contraction": {"lower_ascending": list(map(str, inner_lo)),
                                       "upper_ascending": list(map(str, inner_hi)),
                                       "exact_spr": inner}}


def transfer_controls():
    n = 7
    center = ascending(sp.Poly((S + 1)**n, S))
    radius, perturbation = sp.Rational(1, 100), sp.Rational(1, 100)
    lo = [c - radius if k < n else c for k, c in enumerate(center)]
    hi = [c + radius if k < n else c for k, c in enumerate(center)]
    inner_lo = [(3*a+b)/4 for a, b in zip(lo, hi)]
    inner_hi = [(a+3*b)/4 for a, b in zip(lo, hi)]
    assert box_stable_exact(lo, hi)
    records = []
    for degree in (n - 1, n):
        beta = ascending(sp.Poly(S * (S + 1)**(degree - 1), S))
        weak_residuals = []
        for pairing in pairing_polys(lo, hi, beta):
            quotient, remainder = sp.div(pairing, sp.Poly(T, T))
            assert remainder.is_zero
            certificate = positivity_certificate(quotient)
            assert certificate["ok"]
            weak_residuals.append(certificate)
        strict = beta + [sp.Integer(0)] * (n + 1 - len(beta))
        strict[0] += perturbation
        strict[n] += perturbation
        certificate = verify_numerator(inner_lo, inner_hi, strict)
        assert certificate["ok"]
        records.append({"weak_degree": degree, "weak_numerator": list(map(str, beta)),
                        "weak_pairings_divided_by_t": weak_residuals,
                        "perturbation": str(perturbation), "strict_numerator": list(map(str, strict)),
                        "strict_certificate": certificate})
    return {"scope": "Two exact controls of M, including simultaneous origin zero and degree loss.",
            "outer_lower": list(map(str, lo)), "outer_upper": list(map(str, hi)),
            "inner_lower": list(map(str, inner_lo)), "inner_upper": list(map(str, inner_hi)),
            "cases": records}


def lifted_regions(indices, n):
    r, regions = 0, []
    for index in indices:
        if not 0 <= index < n:
            return None
        while r <= 2 * (n - 1):
            allowed = {r // 2} if r % 2 == 0 else {(r - 1) // 2, (r + 1) // 2}
            if index in allowed:
                break
            r += 1
        if r > 2 * (n - 1):
            return None
        regions.append(r)
    return regions


def phase_checks():
    records = []
    for n in (5, 6, 7, 8):
        by_sign = {}
        for sign in (-1, 1):
            old, lifted = 0, 0
            for seq in itertools.combinations_with_replacement(range(n), n + 1):
                if max(sum(q % 4 == v for q in seq) for v in range(4)) > n // 2:
                    continue
                actual = [q - sign * (-1)**(n + 1 - i) for i, q in enumerate(seq, 1)]
                quads = []
                for i, q in enumerate(seq, 1):
                    sigma = sign * (-1)**(n + 1 - i)
                    e, o = PAT[q % 4]
                    quads.append(QUAD[(sigma * o, -sigma * e)])
                old_ok = region_ok(quads, n)
                new_ok = lifted_regions(actual, n) is not None
                assert not new_ok or old_ok
                old += int(old_ok)
                lifted += int(new_ok)
            by_sign[str(sign)] = {"old_mod_four": old, "unwrapped": lifted}
        records.append({"n": n, "by_kappa_sign": by_sign})
    n7 = next(row for row in records if row["n"] == 7)["by_kappa_sign"]
    assert sum(row["old_mod_four"] for row in n7.values()) == 207
    assert sum(row["unwrapped"] for row in n7.values()) == 43
    seq = (1, 2, 2, 3, 3, 4)
    actual = [q - (-1)**(7 - i) for i, q in enumerate(seq, 2)]
    regions = lifted_regions(actual, 7)
    assert actual == [2, 1, 3, 2, 4, 3] and regions == [3, 3, 5, 5, 7, 7]
    corner_names = ("--", "+-", "++", "-+")
    corner_counts = {name: sum(q % 4 == v for q in seq) for v, name in enumerate(corner_names)}
    assert corner_counts == {"--": 1, "+-": 1, "++": 2, "-+": 2}
    wrap_q = [0, 1, 1, 2, 2, 3, 3, 4]
    wrap_actual = [q + (-1)**(8-i) for i, q in enumerate(wrap_q, 1)]
    assert region_ok([k % 4 for k in wrap_actual], 7)
    assert lifted_regions(wrap_actual, 7) is None and wrap_actual[0] == -1
    return {"scope": "Necessary sign/phase/multiplicity filters; not realizability or an exclusion theorem.",
            "regular_census": records,
            "strict_filter_witness": {"n": 7, "m": 8, "kappa_sign": -1, "q": wrap_q,
                                     "demanded_k": wrap_actual, "old_passes": True, "new_passes": False},
            "both_endpoints_survivor": {"n": 7, "degree_b": 6, "b_at_zero": "0",
                                        "m_finite": 7, "positive_infinity_mass": True,
                                        "zero_finite_node": True, "kappa_sign": 1,
                                        "positive_node_numerator_indices": list(seq),
                                        "denominator_indices": actual, "regions": regions,
                                        "positive_contact_counts": corner_counts}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {"status": "PASS", "arithmetic": "exact rational (SymPy)",
               "sympy_version": sp.__version__, "proof_status": "written/model-reviewed, not kernel checked",
               "original_question_resolved": False,
               "moment_identities": moment_checks(), "contact_determinants": determinant_checks(),
               "hypothesis_countercontrols": hypothesis_controls(),
               "degree_seven_control": boundary_control(), "phase_filter": phase_checks(),
               "closed_to_strict_controls": transfer_controls()}
    inputs = [Path(__file__), Path(__file__).with_name("theory.md"),
              Path(__file__).with_name("exact_verify.py"), Path(__file__).with_name("enumerate_configs.py")]
    payload["input_sha256"] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "moment_cases": payload["moment_identities"]["count"],
                      "determinant_cases": payload["contact_determinants"]["count"],
                      "degree_seven_contact_rank": 5, "stable_bad_numerator_rejected": True,
                      "closed_good_numerator_certified": True, "inner_box_exact_spr": True,
                      "n7_regular_configurations": "207 -> 43", "transfer_controls": 2,
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
