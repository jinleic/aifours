"""Unrun exact finite controls for F743; parent full-read and fresh GO required.

No eligible zero dual is supplied.  The physical fixtures live in a single
explicit, all-member-Hurwitz, full-width box.  The separate endpoint-moment
fixtures are algebraic sign controls only, not physical row representations.
The six band pairs are actual members/frequencies but are not zero duals.

Stdlib Fraction arithmetic; no input, output, files, network, subprocesses,
solver, randomization, or deletion.  A clean exit means every named guard ran;
a CheckFailure names the first failed guard.  The parent must impose a separate
at-most-55-second external deadline.  The cooperative deadline is 45 seconds.
"""

from fractions import Fraction as Q
from math import comb
from time import monotonic

DEADLINE = monotonic() + 45.0


class CheckFailure(Exception):
    pass


def checkpoint():
    if monotonic() >= DEADLINE:
        raise CheckFailure("cooperative_deadline")


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def expect_failure(action, reason):
    try:
        action()
    except CheckFailure as exc:
        require(str(exc) == reason, "wrong_rejection:" + reason + ":" + str(exc))
        return
    raise CheckFailure("mutant_not_rejected:" + reason)


def value(coefficients, x):
    result = Q(0)
    for c in reversed(coefficients):
        result = result * x + c
    return result


def parity_poly(a, parity):
    if parity == 0:
        return (a[0], -a[2], a[4], -a[6])
    require(parity == 1, "bad_parity")
    return (a[1], -a[3], a[5], -a[7])


def actual_row(a, t):
    """Direct definition, independent of compact-polynomial construction."""
    e = a[0] - a[2] * t + a[4] * t**2 - a[6] * t**3
    o = a[1] - a[3] * t + a[5] * t**2 - a[7] * t**3
    return (e, t * o, -t * e, -t**2 * o,
            t**2 * e, t**3 * o, -t**3 * e, -t**4 * o)


def aggregate(members, nodes, weights):
    require(len(members) == len(nodes) == len(weights), "aggregate_lengths")
    out = [Q(0)] * 8
    for a, t, w in zip(members, nodes, weights):
        checkpoint()
        r = actual_row(a, t)
        for j in range(8):
            out[j] += w * r[j]
    return tuple(out)


def in_box(a, center, halfwidths):
    return (len(a) == 8 and a[7] == 1 and
            all(abs(a[j] - center[j]) <= halfwidths[j] for j in range(7)))


def lagrange_at_minus_one(nodes, i):
    answer = Q(1)
    for j, other in enumerate(nodes):
        if j != i:
            answer *= (-Q(1) - other) / (nodes[i] - other)
    return answer


def steer(center, u, w, lvalue, eps, mutation=None):
    denominator = Q(1) if mutation == "drop_weight" else w
    linear_u = Q(1) if mutation == "drop_u" else u
    d0 = -eps * lvalue / denominator
    d1 = -eps * lvalue / (denominator * linear_u)
    if mutation == "wrong_sign":
        d1 = -d1
    a = list(center)
    a[0] += d0
    a[1] += d1
    return tuple(a)


def check_steering_difference(before, after, nodes, weights, eps):
    old = aggregate(before, nodes, weights)
    new = aggregate(after, nodes, weights)
    for j in range(8):
        require(new[j] - old[j] == -eps, "steering_coordinate_" + str(j))


def check_all_strict_negative(vector):
    require(len(vector) == 8, "strict_vector_length")
    require(all(x < 0 for x in vector), "strict_negative")


def shifted(poly, power, scale=Q(1)):
    return [Q(0)] * power + [scale * c for c in poly]


def row_polynomials(a):
    e = parity_poly(a, 0)
    o = parity_poly(a, 1)
    return (shifted(e, 0), shifted(o, 1), shifted(e, 1, -Q(1)),
            shifted(o, 2, -Q(1)), shifted(e, 2), shifted(o, 3),
            shifted(e, 3, -Q(1)), shifted(o, 4, -Q(1)))


def compact_poly(poly):
    """Coefficients of (1-x)^7 p(x/(1-x)), including x=1."""
    require(len(poly) <= 8, "compact_degree")
    out = [Q(0)] * 8
    for k, c in enumerate(poly):
        for j in range(8 - k):
            out[k + j] += c * comb(7 - k, j) * ((-1) ** j)
    return tuple(out)


def check_endpoints(origin, infinity, a0):
    require(origin == (a0,) + (Q(0),) * 7, "compact_origin")
    require(infinity == (Q(0),) * 7 + (Q(1),), "compact_infinity")


def check_compactification(a):
    compact = tuple(compact_poly(p) for p in row_polynomials(a))
    origin = tuple(value(p, Q(0)) for p in compact)
    infinity = tuple(value(p, Q(1)) for p in compact)
    check_endpoints(origin, infinity, a[0])
    for x in (Q(1, 4), Q(1, 2), Q(3, 4)):
        checkpoint()
        t = x / (1 - x)
        r = actual_row(a, t)
        for j in range(8):
            require(value(compact[j], x) == (1 - x)**7 * r[j],
                    "compact_interior_" + str(j))
    return origin, infinity


def check_moments(nodes, x, y, lam, mu):
    require(len(nodes) == len(x) == len(y), "moment_lengths")
    require(all(t > 0 for t in nodes), "moment_node")
    require(lam >= 0 and mu >= 0, "moment_endpoint_sign")
    require(sum(x, Q(0)) + lam == 0, "even_zeroth_endpoint")
    for k in (1, 2, 3):
        require(sum((xi * u**k for xi, u in zip(x, nodes)), Q(0)) == 0,
                "even_moment_" + str(k))
    for k in (0, 1, 2):
        require(sum((yi * u**k for yi, u in zip(y, nodes)), Q(0)) == 0,
                "odd_moment_" + str(k))
    require(sum((yi * u**3 for yi, u in zip(y, nodes)), Q(0)) - mu == 0,
            "odd_third_endpoint")


def sign_condition(values, endpoint):
    require(endpoint >= 0, "sign_endpoint_negative")
    signs = [1 if v > 0 else -1 for v in values if v != 0]
    require(bool(signs), "sign_empty")
    changes = sum(a != b for a, b in zip(signs, signs[1:]))
    require(changes >= 3, "sign_below_three")
    if changes == 3:
        require(endpoint > 0, "three_changes_endpoint")
        require(signs[-1] > 0, "three_changes_last")
    return changes


def barycentric_weight(nodes, i):
    denominator = Q(1)
    for j, other in enumerate(nodes):
        if i != j:
            denominator *= nodes[i] - other
    require(denominator != 0, "barycentric_duplicate")
    return Q(1) / denominator


def envelope_member(center, halfwidths, parity, direction):
    require(direction in (-1, 1), "envelope_direction")
    a = list(center)
    indices = (0, 2, 4, 6) if parity == 0 else (1, 3, 5)
    for k, j in enumerate(indices):
        a[j] += direction * ((-1)**k) * halfwidths[j]
    return tuple(a)


def bisect_center_root(poly, left, right):
    fl = value(poly, left)
    fr = value(poly, right)
    require(fl * fr < 0, "root_bracket")
    for _ in range(32):
        checkpoint()
        mid = (left + right) / 2
        fm = value(poly, mid)
        if fm == 0:
            return mid
        if fm * fl > 0:
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return (left + right) / 2


def physical_value(a, u, parity):
    r = actual_row(a, u)
    if parity == 0:
        return r[0]
    require(parity == 1 and u > 0, "physical_odd_node")
    return r[1] / u


def check_reverse(band, left, right, vleft, vright):
    require(0 <= band <= 2 and left < right, "reverse_order")
    if band == 1:
        require(vleft > 0 and vright < 0, "reverse_direction")
    else:
        require(vleft < 0 and vright > 0, "reverse_direction")


def check_physical_bands(center, halfwidths):
    even = ((Q(0), Q(1, 10)), (Q(1, 2), Q(1)), (Q(4), Q(5)))
    odd = ((Q(1, 5), Q(3, 10)), (Q(3, 2), Q(2)), (Q(19), Q(20)))
    ordered = (even[0], odd[0], even[1], odd[1], even[2], odd[2])
    require(all(a[1] < b[0] for a, b in zip(ordered, ordered[1:])),
            "band_brackets_not_disjoint")
    for parity, brackets in ((0, even), (1, odd)):
        minus = envelope_member(center, halfwidths, parity, -1)
        plus = envelope_member(center, halfwidths, parity, 1)
        require(in_box(minus, center, halfwidths), "minus_not_actual")
        require(in_box(plus, center, halfwidths), "plus_not_actual")
        p = parity_poly(center, parity)
        pminus = parity_poly(minus, parity)
        pplus = parity_poly(plus, parity)
        hs = ((halfwidths[0], halfwidths[2], halfwidths[4], halfwidths[6])
              if parity == 0 else
              (halfwidths[1], halfwidths[3], halfwidths[5], Q(0)))
        require(all(h > 0 for h in hs[:3]), "nonpositive_envelope_width")
        require(all(pminus[k] == p[k] - hs[k] and
                    pplus[k] == p[k] + hs[k] for k in range(4)),
                "envelope_polynomial")
        for env in (pminus, pplus):
            require(env[3] < 0 and value(env, Q(0)) > 0,
                    "envelope_cubic_orientation")
            for band, (left, right) in enumerate(brackets):
                checkpoint()
                initial = 1 if band != 1 else -1
                require(initial * value(env, left) > 0 and
                        initial * value(env, right) < 0,
                        "envelope_bracket_" + str(parity) + "_" + str(band))
        # Each cubic has three distinct sign-changing positive roots, one per
        # bracket, and hence no others. Both envelopes have the same signs in
        # every outside gap. Their actual uncertainty bands lie strictly inside
        # these six mutually disjoint rational brackets.
        for band, (left, right) in enumerate(brackets):
            checkpoint()
            middle = bisect_center_root(p, left, right)
            delta = Q(1, 2**24)
            u, v = middle - delta, middle + delta
            require(left < u < v < right, "band_pair_outside_bracket")
            for t in (u, v):
                require(value(pminus, t) < 0 < value(pplus, t),
                        "band_pair_not_inside_actual_band")
            lmember, rmember = ((plus, minus) if band == 1 else (minus, plus))
            lv = physical_value(lmember, u, parity)
            rv = physical_value(rmember, v, parity)
            check_reverse(band, u, v, lv, rv)
            # The opposite, baseline crossing is a specific rejected mutant.
            wrong_l = physical_value(rmember, u, parity)
            wrong_r = physical_value(lmember, v, parity)
            expect_failure(lambda: check_reverse(band, u, v, wrong_l, wrong_r),
                           "reverse_direction")


def main():
    checkpoint()
    center = tuple(Q(comb(7, j)) for j in range(8))
    inner = (Q(1, 10000),) * 7
    outer = (Q(1, 1000),) * 7
    require(center == (1, 7, 21, 35, 35, 21, 7, 1), "binomial_center")
    require(all(0 < inner[j] < outer[j] for j in range(7)), "box_buffer")
    require(center[0] - outer[0] > 0, "box_constant")

    # Whole-frequency proof encoded by coefficient inequalities:
    # (1+t)^7 >= t^j, 0 <= j <= 6, t >= 0.  Thus for every
    # |a_j-center_j| <= outer_j and every 0 <= theta <= 1,
    # |a_theta(iw)-center(iw)| <= (7/1000)|center(iw)|.
    # Monic root continuity and nonvanishing on the imaginary axis show that
    # every actual member is strictly Hurwitz; this is not corner stability.
    # Also Re(center(iw)*conj(a_theta(iw))) >= (993/1000)(1+t)^7.
    for j in range(7):
        for k in range(8):
            require(comb(7, k) - (1 if k == j else 0) >= 0,
                    "global_monomial_bound")
    margin = Q(1) - sum(outer, Q(0))
    require(margin == Q(993, 1000) and margin > 0, "homotopy_margin")

    nodes = (Q(1, 2), Q(1), Q(2), Q(3))
    weights = (Q(1), Q(2), Q(3), Q(4))
    require(all(t > 0 for t in nodes) and len(set(nodes)) == 4,
            "steering_nodes")
    require(all(w > 0 for w in weights) and len(set(weights)) > 1,
            "steering_weights")
    lagrange = tuple(lagrange_at_minus_one(nodes, i) for i in range(4))
    require(lagrange == (Q(64, 5), Q(-18), Q(8), Q(-9, 5)),
            "lagrange_values")
    for k in range(4):
        require(sum((lagrange[i] * nodes[i]**k for i in range(4)), Q(0))
                == (-1)**k, "lagrange_moment_" + str(k))
    maxscale = max(max(abs(lagrange[i] / weights[i]),
                       abs(lagrange[i] / (weights[i] * nodes[i])))
                   for i in range(4))
    eps = outer[0] / (2 * maxscale)
    require(maxscale == Q(128, 5) and eps == Q(1, 51200) and eps > 0,
            "epsilon")
    before = (center,) * 4
    after = tuple(steer(center, nodes[i], weights[i], lagrange[i], eps)
                  for i in range(4))
    require(all(in_box(a, center, inner) for a in before), "before_inner")
    require(all(in_box(a, center, outer) for a in before + after), "outer_member")
    require(any(not in_box(a, center, inner) for a in after), "buffer_not_used")
    check_steering_difference(before, after, nodes, weights, eps)

    # Independently check the actual P=center dot r at the selected physical
    # rows.  The continuum conclusion comes from the preceding analytic bound.
    for family in (before, after):
        for a, t in zip(family, nodes):
            row = actual_row(a, t)
            pairing = sum((center[j] * row[j] for j in range(8)), Q(0))
            require(pairing >= margin * (1 + t)**7, "selected_pairing_margin")
        ag = aggregate(family, nodes, weights)
        require(sum((center[j] * ag[j] for j in range(8)), Q(0)) > 0,
                "physical_aggregate_not_zero")

    for mutation, reason in (("drop_u", "steering_coordinate_1"),
                             ("wrong_sign", "steering_coordinate_1"),
                             ("drop_weight", "steering_coordinate_0")):
        mutant = tuple(steer(center, nodes[i], weights[i], lagrange[i], eps, mutation)
                       for i in range(4))
        expect_failure(lambda: check_steering_difference(before, mutant, nodes, weights, eps),
                       reason)

    for a in before + after:
        origin, infinity = check_compactification(a)
    expect_failure(lambda: check_endpoints(origin, (Q(0),) * 8, a[0]),
                   "compact_infinity")

    # Algebraic endpoint/moment fixtures ONLY: no claim these X,Y arise from
    # the physical box, the selected physical members, or any zero dual.
    mnodes = (Q(1), Q(2), Q(3), Q(4))
    x = (Q(-4), Q(6), Q(-4), Q(1))
    y = (Q(-1, 6), Q(1, 2), Q(-1, 2), Q(1, 6))
    check_moments(mnodes, x, y, Q(1), Q(1))
    require(sign_condition(x, Q(1)) == 3 and sign_condition(y, Q(1)) == 3,
            "three_change_fixture")
    expect_failure(lambda: check_moments(mnodes, x, y, Q(0), Q(1)),
                   "even_zeroth_endpoint")
    expect_failure(lambda: check_moments(mnodes, x, y, Q(1), Q(0)),
                   "odd_third_endpoint")
    expect_failure(lambda: sign_condition(x, Q(0)), "three_changes_endpoint")
    expect_failure(lambda: sign_condition(tuple(-v for v in x), Q(1)),
                   "three_changes_last")
    expect_failure(lambda: sign_condition((Q(1), Q(-1), Q(1)), Q(1)),
                   "sign_below_three")

    five = (Q(1), Q(2), Q(3), Q(4), Q(5))
    bweights = tuple(barycentric_weight(five, i) for i in range(5))
    with_zero_nodes = (five[0], five[1], Q(5, 2), five[2], five[3], five[4])
    with_zero = (bweights[0], bweights[1], Q(0), bweights[2], bweights[3], bweights[4])
    check_moments(with_zero_nodes, with_zero, with_zero, Q(0), Q(0))
    require(sign_condition(with_zero, Q(0)) == 4, "four_change_zero_endpoint")

    weak_only = (-Q(1),) * 7 + (Q(0),)
    require(all(v <= 0 for v in weak_only), "weak_control_setup")
    expect_failure(lambda: check_all_strict_negative(weak_only), "strict_negative")
    check_physical_bands(center, outer)
    checkpoint()


if __name__ == "__main__":
    main()
