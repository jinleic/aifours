"""Exact certificates for monic real interval-polynomial SPR synthesis.

All coefficient arrays are ascending.  Verification rejects floating-point
inputs; only ``to_fraction_box`` performs an explicitly numerical conversion.
Corners are (--), (-+), (+-), (++), matching sprlib.CORNERS.  A certificate
concerns the rationalized box, not automatically the original floating box.
"""
from __future__ import annotations

from fractions import Fraction
import json
from numbers import Integral

import sympy as sp

T = sp.Symbol("t")
CORNERS = ((0, 0), (0, 1), (1, 0), (1, 1))


def rational(value):
    """Convert exact scalar types, refusing floats even when integral."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Integral):
        return Fraction(int(value))
    if isinstance(value, sp.Rational):
        return Fraction(int(value.p), int(value.q))
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"Expected an exact rational, got {type(value).__name__}")


def _box(lo, hi):
    lo, hi = tuple(map(rational, lo)), tuple(map(rational, hi))
    if len(lo) != len(hi) or len(lo) < 2:
        raise ValueError("A box requires equal arrays and positive degree")
    if lo[-1] != 1 or hi[-1] != 1:
        raise ValueError("The denominator box must be monic")
    if any(a > b for a, b in zip(lo, hi)):
        raise ValueError("Inverted coefficient interval")
    return lo, hi


def to_fraction_box(lo, hi, max_den=10**6):
    """Nearest bounded-denominator rational endpoints, preserving order/monicity.

    Exact rational inputs are also rounded to ``max_den``.  Invalid order or
    nonmonic inputs are rejected rather than silently changing their meaning.
    The output is not claimed to enclose the original box; recheck stability.
    """
    if max_den < 1 or int(max_den) != max_den:
        raise ValueError("max_den must be a positive integer")
    if len(lo) != len(hi) or len(lo) < 2:
        raise ValueError("Incompatible coefficient arrays")
    if lo[-1] != 1 or hi[-1] != 1 or any(a > b for a, b in zip(lo, hi)):
        raise ValueError("Input must be an ordered monic box")
    convert = lambda x: Fraction(str(x)).limit_denominator(max_den)
    lower, upper = [convert(x) for x in lo], [convert(x) for x in hi]
    for j, (a, b) in enumerate(zip(lower, upper)):
        if a > b:
            lower[j], upper[j] = b, a
    lower[-1] = upper[-1] = Fraction(1)
    return lower, upper


def endpoints_exact(lo, hi):
    lo, hi = _box(lo, hi)
    parts = [[], [], [], []]
    for k, (lower, upper) in enumerate(zip(lo, hi)):
        sign = (-1) ** (k // 2)
        mn, mx = (lower, upper) if sign == 1 else (-upper, -lower)
        offset = 2 * (k % 2)
        parts[offset].append(mn)
        parts[offset + 1].append(mx)
    return tuple(parts)


def kharitonov_exact(lo, hi):
    em, ep, om, op = endpoints_exact(lo, hi)
    result = []
    for i, j in CORNERS:
        e, o = (em, ep)[i], (om, op)[j]
        c = [Fraction(0)] * len(lo)
        for k, value in enumerate(e):
            c[2 * k] = (-1) ** k * value
        for k, value in enumerate(o):
            c[2 * k + 1] = (-1) ** k * value
        result.append(c)
    return result


def is_hurwitz_exact(coeffs):
    """Strict rational Routh test, after normalizing the leading coefficient.

    Zero pivots and zero rows are rejections: a strictly Hurwitz polynomial
    has all strictly positive first-column entries, so no epsilon rule is used.
    Nonzero constants are vacuously Hurwitz; the zero polynomial is not.
    """
    c = list(map(rational, coeffs))
    while c and c[-1] == 0:
        c.pop()
    if not c:
        return False
    if len(c) == 1:
        return True
    leading = c[-1]
    descending = [v / leading for v in reversed(c)]
    if any(v <= 0 for v in descending):
        return False
    n = len(c) - 1
    width = (n + 2) // 2
    upper, lower = descending[::2], descending[1::2]
    upper += [Fraction(0)] * (width - len(upper))
    lower += [Fraction(0)] * (width - len(lower))
    for _ in range(n - 1):
        if lower[0] <= 0:
            return False
        row = [(lower[0] * upper[j + 1] - upper[0] * lower[j + 1])
               / lower[0] for j in range(width - 1)] + [Fraction(0)]
        upper, lower = lower, row
    return lower[0] > 0


def box_stable_exact(lo, hi):
    """Kharitonov's exact four-polynomial criterion."""
    return all(is_hurwitz_exact(c) for c in kharitonov_exact(lo, hi))


def _poly(coeffs):
    return sp.Poly.from_list(list(reversed(coeffs)), T, domain=sp.QQ)


def pairing_polys(lo, hi, beta):
    """Four exact P_c(t) = F(t)E_c(t) + tG(t)O_c(t), over QQ."""
    lo, hi = _box(lo, hi)
    beta = list(map(rational, beta))
    if len(beta) > len(lo):
        raise ValueError("Numerator degree exceeds denominator degree")
    beta += [Fraction(0)] * (len(lo) - len(beta))
    f = _poly([(-1)**j * x for j, x in enumerate(beta[::2])])
    g = _poly([(-1)**j * x for j, x in enumerate(beta[1::2])])
    em, ep, om, op = map(_poly, endpoints_exact(lo, hi))
    t = sp.Poly(T, T, domain=sp.QQ)
    return [f * (em, ep)[i] + t * g * (om, op)[j] for i, j in CORNERS]


def positivity_certificate(poly):
    """Exact endpoint signs plus a Sturm root count on a strict Cauchy bound.

    For degree > 0 every complex root has modulus < B, where
    B = 2 + max_{j<degree}|a_j/a_degree|.  Since P(0)>0 and P(B)!=0,
    count_roots(0, B) is precisely the number of positive real roots.  This
    also rejects even-multiplicity tangencies, unlike a sign-change grid.
    """
    if not isinstance(poly, sp.Poly):
        expression = sp.sympify(poly)
        if expression.atoms(sp.Float):
            raise TypeError("Floating-point polynomial is not an exact input")
        poly = sp.Poly(expression, T, domain=sp.QQ)
    if poly.domain not in (sp.QQ, sp.ZZ):
        raise TypeError("Polynomial must have exact rational coefficients")
    if len(poly.gens) != 1:
        raise ValueError("Polynomial must be univariate")
    if poly.is_zero:
        return {"ok": False, "degree": None, "reason": "zero polynomial"}
    degree = int(poly.degree())
    c0, leading = poly.eval(0), poly.LC()
    result = {"ok": False, "degree": degree, "at_zero": str(c0),
              "leading": str(leading), "positive_roots": None}
    if c0 <= 0 or leading <= 0:
        result["reason"] = "nonpositive endpoint sign"
        return result
    if degree == 0:
        result.update(ok=True, positive_roots=0, root_bound=None)
        return result
    bound = 2 + max(abs(a / leading) for a in poly.all_coeffs()[1:])
    count = int(poly.count_roots(0, bound))
    result.update(ok=count == 0, positive_roots=count, root_bound=str(bound))
    return result


def positive_on_halfline(poly):
    return positivity_certificate(poly)["ok"]


def verify_numerator(lo, hi, beta):
    """Certify the complete rational box, actual degree, and all frequencies."""
    lo, hi = _box(lo, hi)
    beta = list(map(rational, beta))
    n = len(lo) - 1
    actual_degree = next((i for i in range(len(beta)-1, -1, -1) if beta[i]), -1)
    degree_ok = actual_degree == n
    stability = [is_hurwitz_exact(c) for c in kharitonov_exact(lo, hi)]
    result = {"ok": False, "denominator_degree": n, "numerator_degree": actual_degree,
              "degree_ok": degree_ok, "stable_corners": stability,
              "box_stable": all(stability), "corners": []}
    if actual_degree > n:
        return result
    beta = beta[:n + 1]
    certificates = [positivity_certificate(p) for p in pairing_polys(lo, hi, beta)]
    for i, certificate in enumerate(certificates):
        certificate["corner"] = i
    result["corners"] = certificates
    result["ok"] = degree_ok and all(stability) and all(c["ok"] for c in certificates)
    return result


def verify_gordan(lo, hi, points, w_inf=0):
    """Check a rational nonnegative dependence of frequency functionals.

    ``points`` is [(t, corner_index, weight), ...].  Alternatively pass
    {"points": [...], "w_inf": rational}.  The optional infinity functional
    is b_n (not a sampled large frequency).  At least one FINITE weight must
    be positive.  Denominator stability is not assumed by this algebraic test.
    A successful certificate rules out strictly positive finite pairings
    together with b_n >= 0; it does not itself establish a stable counterexample.
    """
    lo, hi = _box(lo, hi)
    if isinstance(points, dict):
        if rational(w_inf) != 0:
            raise ValueError("Specify w_inf in only one place")
        w_inf = points.get("w_inf", 0)
        points = points["points"]
    w_inf = rational(w_inf)
    coefficients = [Fraction(0)] * len(lo)
    coefficients[-1] = w_inf
    em, ep, om, op = endpoints_exact(lo, hi)
    valid_weights, finite_positive = w_inf >= 0, False
    valid_points = True
    for t, ci, weight in points:
        t, weight = rational(t), rational(weight)
        valid_weights &= weight >= 0
        finite_positive |= weight > 0
        if t < 0 or not isinstance(ci, Integral) or not 0 <= ci < 4:
            valid_points = False
            continue
        i, j = CORNERS[ci]
        e = sum(v * t**k for k, v in enumerate((em, ep)[i]))
        o = sum(v * t**k for k, v in enumerate((om, op)[j]))
        for k in range(len(lo)):
            ell = k // 2
            row = (-1)**ell * t**ell * (e if k % 2 == 0 else t * o)
            coefficients[k] += weight * row
    zero_form = all(x == 0 for x in coefficients)
    return {"ok": bool(valid_weights and valid_points and finite_positive and zero_form),
            "weights_nonnegative": bool(valid_weights), "points_valid": valid_points,
            "finite_positive_weight": bool(finite_positive), "zero_linear_form": zero_form,
            "linear_coefficients": [str(x) for x in coefficients]}


def self_test():
    """Positive controls and adversarial negative controls; no numerical oracle."""
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    for n in (1, 2, 5, 6):
        c = [int(sp.binomial(n, k)) for k in range(n + 1)]
        check(f"hurwitz_binomial_{n}", is_hurwitz_exact(c))
        check(f"identity_spr_{n}", verify_numerator(c, c, c)["ok"])
    check("negative_leading_hurwitz", is_hurwitz_exact([-1, -2, -1]))
    check("imaginary_axis_rejected", not is_hurwitz_exact([1, 0, 1]))
    check("zero_root_rejected", not is_hurwitz_exact([0, 1]))
    check("nonzero_constant_hurwitz", is_hurwitz_exact([2]))
    check("zero_polynomial_rejected", not is_hurwitz_exact([0]))
    check("negative_numerator_rejected", not verify_numerator([1, 2, 1], [1, 2, 1], [-1, -2, -1])["ok"])
    check("lower_degree_rejected", not verify_numerator([1, 2, 1], [1, 2, 1], [1, 2])["ok"])
    # Three corner indices stable, one unstable (no repeated-corner shortcut).
    unstable_lo, unstable_hi = [1, 1, 1, 1], [Fraction(3, 2), 2, 2, 1]
    flags = [is_hurwitz_exact(c) for c in kharitonov_exact(unstable_lo, unstable_hi)]
    check("unstable_corner_detected", not box_stable_exact(unstable_lo, unstable_hi) and sum(flags) == 3)
    check("bogus_gordan_rejected", not verify_gordan([1, 1], [1, 1], [(0, 0, 1)])["ok"])
    check("negative_weight_rejected", not verify_gordan([-1, 1], [1, 1], [(0, 0, -1), (0, 2, -1)])["ok"])
    check("valid_gordan_control", verify_gordan([-1, 1], [1, 1], [(0, 0, 1), (0, 2, 1)])["ok"])
    check("infinity_weight_included", not verify_gordan([-1, 1], [1, 1], {"points": [(0, 0, 1), (0, 2, 1)], "w_inf": 1})["ok"])
    check("all_zero_certificate_rejected", not verify_gordan([1, 1], [1, 1], [])["ok"])
    check("negative_frequency_rejected", not verify_gordan([-1, 1], [1, 1], [(-1, 0, 1)])["ok"])
    check("constant_positive", positive_on_halfline(sp.Poly(3, T)))
    check("positive_no_roots", positive_on_halfline(sp.Poly(T*T + 1, T)))
    check("negative_roots_allowed", positive_on_halfline(sp.Poly((T + 1)*(T + 2), T)))
    check("double_positive_root_rejected", not positive_on_halfline(sp.Poly((T - 1)**2, T)))
    check("zero_endpoint_rejected", not positive_on_halfline(sp.Poly(T, T)))
    check("tiny_negative_pocket_rejected", not positive_on_halfline(sp.Poly((T - 1)**2 - sp.Rational(1, 10**80), T)))
    check("infinite_bound_semantics", sp.Poly((T - 1)**2 * (T + 2), T).count_roots(0, sp.oo) == 1)
    lo, hi = to_fraction_box([0.1, 1.0], [0.100001, 1.0])
    check("rationalization_order", lo[0] <= hi[0] and lo[-1] == hi[-1] == 1)
    try:
        is_hurwitz_exact([1.0, 1.0])
    except TypeError:
        checks["verification_rejects_floats"] = True
    else:
        check("verification_rejects_floats", False)
    return {"ok": all(checks.values()), "checks": checks, "count": len(checks),
            "sympy_version": sp.__version__}


if __name__ == "__main__":
    print(json.dumps(self_test(), indent=2))
