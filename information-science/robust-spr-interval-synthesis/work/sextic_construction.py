"""50-digit transcription of arXiv:2609.26541v2, Sections 3--4.

Root calculations and Proposition 4.1 diagnostics are numerical, NOT formal
proofs.  Every returned successful numerator is rounded to QQ and certified
on the entire rational box by exact_verify.  No LP substitutes for this
construction.  Fixed even parts use the paper's separate Lemma 2.3.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math

import mpmath as mp

from exact_verify import (CORNERS, box_stable_exact, endpoints_exact, rational,
                          verify_numerator)


def _mp(x):
    x = rational(x)
    return mp.mpf(x.numerator) / x.denominator


def _add(*polys):
    out = [mp.mpf(0)] * max(map(len, polys))
    for poly in polys:
        for j, value in enumerate(poly):
            out[j] += value
    return out


def _scale(poly, factor):
    return [factor * x for x in poly]


def _mul(p, q):
    out = [mp.mpf(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def _eval(poly, x):
    result = mp.mpf(0)
    for c in reversed(poly):
        result = result * x + c
    return result


def _derivative(poly):
    return [j * poly[j] for j in range(1, len(poly))]


def _relative_residual(poly, x):
    scale = _eval(list(map(abs, poly)), abs(x))
    return abs(_eval(poly, x)) / max(mp.mpf(1), scale)


def _real_positive_roots(poly):
    """Degree 2/3 roots, bracketed by derivative roots (no numpy seed)."""
    if len(poly) == 3:
        c, b, a = poly
        discriminant = b*b - 4*a*c
        if discriminant <= 0:
            raise ArithmeticError("Expected two simple real quadratic roots")
        q = -(b + (1 if b >= 0 else -1) * mp.sqrt(discriminant)) / 2
        roots = sorted([q / a, c / q])
        if roots[0] <= 0:
            raise ArithmeticError("Expected positive quadratic roots")
        return roots
    if len(poly) != 4:
        raise ValueError("Only quadratics and cubics are required")
    critical = _real_positive_roots(_derivative(poly))
    bound = 2 + max(abs(c / poly[-1]) for c in poly[:-1])
    edges = [mp.mpf(0), *critical, bound]
    roots = []
    for left, right in zip(edges[:-1], edges[1:]):
        fl, fr = _eval(poly, left), _eval(poly, right)
        if fl * fr >= 0:
            raise ArithmeticError("Cubic does not have three separated positive roots")
        for _ in range(5 * mp.mp.dps + 64):
            mid = (left + right) / 2
            if mid == left or mid == right:
                break
            fm = _eval(poly, mid)
            if fm == 0:
                left = right = mid
                break
            if fm * fl > 0:
                left, fl = mid, fm
            else:
                right = mid
        roots.append((left + right) / 2)
    return roots


def _strings(values):
    if isinstance(values, dict):
        return {key: _strings(value) for key, value in values.items()}
    if isinstance(values, (list, tuple)):
        return [_strings(value) for value in values]
    if isinstance(values, mp.mpf):
        return mp.nstr(values, mp.mp.dps)
    return values


def _formula(lo, hi, dps):
    em, ep, om, op = [[_mp(x) for x in row] for row in endpoints_exact(lo, hi)]
    a, b, c = _real_positive_roots(em)
    A, B, C = _real_positive_roots(ep)
    if not 0 < a < A < B < b < c < C:
        raise ArithmeticError("Even-root order (3.2) failed at working precision")
    # (3.6): om = [ell_5, -u_3, ell_1], op = [u_5, -ell_3, u_1].
    h = mp.sqrt(om[1]**2 - 4*om[2]*om[0]) / (c - A)
    k = mp.sqrt(op[1]**2 - 4*op[2]*op[0]) / (b - B)
    m = k / h
    M = (c - A) / (b - B)
    U, V = _mul([-A, 1], [-c, 1]), _mul([-B, 1], [-b, 1])
    D1, D2 = (b - a)*(c - a), (C - A)*(C - B)
    la1, la2 = (b - a)*(c - b), (C - B)*(B - A)
    lg1, lg2 = (c - a)*(c - b), (C - A)*(B - A)
    L_alpha = [B*b*(1/la1 + 1/la2), -(b/la1 + B/la2)]
    L_gamma = [-A*c*(1/lg1 + 1/lg2), c/lg1 + A/lg2]
    F0 = _add(_mul(U, L_alpha), _mul(V, L_gamma))
    f2 = 1 + a*(A + B + b + c - a)/D1 + (A*B + C*(b + c))/D2
    w_A = (C - A)/((b - A)*(c - A)**2)
    w_B = (C - B)/(m*(b - B)**2*(c - B))
    w_b = (b - a)/(m*(b - A)*(b - B)**2)
    w_c = (c - a)/((c - A)**2*(c - B))
    rho = (A*w_A + B*w_B + b*w_b + c*w_c)/(w_A + w_B + w_b + w_c)
    F_z = [mp.mpf(0), -rho, mp.mpf(1)]
    v_A = (A - rho)*(A - B)*(A - C)/(A - c)
    v_B = (B - rho)*(B - A)*(B - C)/(m*(B - b))
    v_b = (b - rho)*(b - a)*(b - c)/(m*(b - B))
    G_z = _add(_scale(_mul([-B, 1], [-b, 1]), v_A/((A - B)*(A - b))),
               _scale(_mul([-A, 1], [-b, 1]), v_B/((B - A)*(B - b))),
               _scale(_mul([-A, 1], [-B, 1]), v_b/((b - A)*(b - B))))
    F = _scale(_add(F0, _scale(F_z, f2)), m)
    G = _add(U, _scale(V, m), _scale(G_z, m*f2))
    beta = [mp.mpf(0)] * 7
    for j, value in enumerate(F):
        beta[2*j] = h * (-1)**j * value
    for j, value in enumerate(G):
        beta[2*j + 1] = (-1)**j * value
    monic_beta = [value / beta[-1] for value in beta]
    tolerance = mp.power(10, -(dps // 2))
    close = lambda x, y: abs(x-y) <= tolerance * max(1, abs(x), abs(y))
    contacts = []
    for (i, j), node in zip(CORNERS, (c, b, A, B)):
        pairing = _add(_mul(F, (em, ep)[i]),
                       [mp.mpf(0)] + _mul(G, (U, _scale(V, m))[j]))
        value_error = _relative_residual(pairing, node)
        derivative_error = _relative_residual(_derivative(pairing), node)
        contacts.append({"corner": [i, j], "node": node,
                         "relative_value_residual": value_error,
                         "relative_derivative_residual": derivative_error,
                         "ok": bool(value_error < tolerance and derivative_error < tolerance)})
    # Numerical global quadratic separation in (3.7), by the vertex minimum.
    def positive_quadratic(q):
        return bool(q[2] > 0 and q[0] - q[1]**2/(4*q[2]) > 0)
    lower_gap = _add(om, _scale(U, -h))
    upper_gap = _add(_scale(V, k), _scale(op, -1))
    checks = {
        "root_order_3_2": bool(0 < a < A < B < b < c < C),
        "scales_3_8": bool(h > 0 and 1 < m and (m <= M or close(m, M))),
        "strict_odd_bounds_3_7": positive_quadratic(lower_gap) and positive_quadratic(upper_gap),
        "F0_constant_4_4": close(F0[0], A*B*b*c*(1/D1 + 1/D2)),
        "f2_coefficient_4_5": close(F0[2], f2),
        "F0_leading_4_6": close(F0[3], -(a/D1 + C/D2)),
        "rho_bounds_4_9": bool(B < rho < b),
        "double_contacts_4_16": all(row["ok"] for row in contacts),
        "coefficient_signs_prop_4_1": bool(F[0] > 0 and F[3] < 0 and G[2] > 0),
        "last_root_test_4_22": bool(_eval(F0, C) + f2*C*(C - b) > 0),
    }
    roots_F, roots_G, root_error = None, None, None
    try:
        roots_F, roots_G = _real_positive_roots(F), _real_positive_roots(G)
        r1, r2, r3 = roots_F
        u, v = roots_G
        checks["G_roots_4_17"] = bool(A < u < B < b < v < c)
        checks["F_roots_4_18"] = bool(0 < r1 < A and B < r2 < b and C < r3)
    except ArithmeticError as exc:
        root_error = str(exc)
        checks["G_roots_4_17"] = checks["F_roots_4_18"] = False
    data = {"dps": dps, "roots": {"a": a, "A": A, "B": B, "b": b, "c": c, "C": C},
            "h": h, "k": k, "m": m, "M": M, "D1": D1, "D2": D2,
            "U": U, "V": V, "L_alpha": L_alpha, "L_gamma": L_gamma, "F0": F0,
            "f2": f2, "weights": [w_A, w_B, w_b, w_c], "rho": rho,
            "F_z": F_z, "G_z": G_z, "F": F, "G": G,
            "roots_F": roots_F, "roots_G": roots_G, "root_diagnostic_error": root_error,
            "beta_unscaled": beta, "beta_monic": monic_beta,
            "contacts": contacts, "checks": checks,
            "audit_ok": all(checks.values()), "audit_tolerance": tolerance}
    return monic_beta, _strings(data)


def construct_sextic(lo, hi, dps=50):
    """Return a rational numerator, exact certificate, and construction diagnostics.

    On failed rational rounding the denominator bound is increased.  A failed
    formula diagnostic is retained, not silently replaced by a different
    construction.  The caller must distinguish exact SPR from formula claims.
    """
    lo, hi = list(map(rational, lo)), list(map(rational, hi))
    if len(lo) != 7 or not box_stable_exact(lo, hi):
        raise ValueError("Construction requires an exactly stable monic sextic box")
    em, ep, _, _ = endpoints_exact(lo, hi)
    if em == ep:
        epsilon = Fraction(1)
        trials = []
        for attempt in range(512):
            beta = [Fraction(0)] * 7
            for j, value in enumerate(em):
                beta[2*j] = (-1)**j * value
            for j in range(3):
                beta[2*j + 1] = -epsilon * (-1)**j * (j+1) * em[j+1]
            verification = verify_numerator(lo, hi, beta)
            trials.append({"epsilon": str(epsilon), "ok": verification["ok"]})
            if verification["ok"]:
                return {"beta": beta, "verification": verification,
                        "method": "Lemma 2.3 fixed even part", "audit_ok": True,
                        "details": {"epsilon": str(epsilon), "trials": trials}}
            epsilon /= 2
        return {"beta": beta, "verification": verification,
                "method": "Lemma 2.3 fixed even part", "audit_ok": False,
                "details": {"trials": trials, "error": "No certified epsilon in 512 halvings"}}
    with mp.workdps(dps):
        values, details = _formula(lo, hi, dps)
        rounding = []
        for digits in (12, 18, 24, 36):
            beta = [Fraction(mp.nstr(x, dps - 5)).limit_denominator(10**digits) for x in values]
            beta[-1] = Fraction(1)
            verification = verify_numerator(lo, hi, beta)
            rounding.append({"max_den": str(10**digits), "ok": verification["ok"]})
            if verification["ok"]:
                break
        details["rounding_attempts"] = rounding
        return {"beta": beta, "verification": verification,
                "method": "Equations (3.6), (4.1)--(4.14)",
                "audit_ok": details["audit_ok"], "details": details}


def example_check():
    center = [Fraction(math.comb(6, k)) for k in range(7)]
    lo = [x - Fraction(1, 100) for x in center[:-1]] + [Fraction(1)]
    hi = [x + Fraction(1, 100) for x in center[:-1]] + [Fraction(1)]
    result = construct_sextic(lo, hi)
    return {"example": "arXiv:2609.26541v2 equation (7.1)",
            "lo": list(map(str, lo)), "hi": list(map(str, hi)),
            "paper_simple_numerator_certificate": verify_numerator(lo, hi, center),
            "construction": {**result, "beta": list(map(str, result["beta"]))}}


if __name__ == "__main__":
    result = example_check()
    print(json.dumps(result, indent=2))
    if not (result["paper_simple_numerator_certificate"]["ok"]
            and result["construction"]["verification"]["ok"]
            and result["construction"]["audit_ok"]):
        raise SystemExit(1)
