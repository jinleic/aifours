import time
START = time.monotonic()

import sys
from fractions import Fraction as F
from math import comb

LIMIT_SECONDS = 55
ZERO = (F(0),)


class BudgetExhausted(Exception):
    pass


class VerificationError(Exception):
    pass


def tick():
    if time.monotonic() - START >= LIMIT_SECONDS:
        raise BudgetExhausted("cooperative 55-second limit reached")


def need(condition, message):
    if not condition:
        raise VerificationError(message)


def poly(values):
    values = [F(x) for x in values]
    if not values:
        return ZERO
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def add(a, b):
    tick()
    out = [F(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += x
    return poly(out)


def scale(a, c):
    tick()
    return poly(x * c for x in a)


def shift(a, k):
    return poly([F(0)] * k + list(a))


def mul(a, b):
    tick()
    out = [F(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return poly(out)


def derivative(a):
    return poly(j * a[j] for j in range(1, len(a)))


def value(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def divide(a, b):
    tick()
    a = list(poly(a))
    b = poly(b)
    need(b != ZERO, "polynomial division by zero")
    out = [F(0)] * max(1, len(a) - len(b) + 1)
    while poly(a) != ZERO and len(a) >= len(b):
        tick()
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        out[k] += c
        for j in range(len(b)):
            a[k + j] -= c * b[j]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return poly(out), poly(a)


def gcd_poly(a, b):
    a, b = poly(a), poly(b)
    while b != ZERO:
        tick()
        a, b = b, divide(a, b)[1]
    need(a != ZERO, "undefined zero/zero gcd")
    return scale(a, F(1) / a[-1])


def positive_normalize(a):
    need(a != ZERO, "cannot normalize zero polynomial")
    return scale(a, F(1) / abs(a[-1]))


def sturm(a):
    tick()
    a = poly(a)
    g = gcd_poly(a, derivative(a))
    squarefree, remainder = divide(a, g)
    need(remainder == ZERO, "square-free division has remainder")
    sequence = [positive_normalize(squarefree)]
    d = derivative(sequence[0])
    if d == ZERO:
        return g, tuple(sequence)
    sequence.append(positive_normalize(d))
    while True:
        tick()
        remainder = divide(sequence[-2], sequence[-1])[1]
        if remainder == ZERO:
            break
        sequence.append(positive_normalize(scale(remainder, -1)))
    return g, tuple(sequence)


def variations(sequence, x):
    signs = []
    for p in sequence:
        y = value(p, x)
        if y != 0:
            signs.append(1 if y > 0 else -1)
    return sum(signs[j] != signs[j - 1]
               for j in range(1, len(signs)))


def analyze_positive(a):
    tick()
    endpoints = (value(a, F(0)), value(a, F(1)))
    if endpoints[0] <= 0 or endpoints[1] <= 0:
        return False, endpoints, None, None, None, ()
    g, sequence = sturm(a)
    v0 = variations(sequence, F(0))
    v1 = variations(sequence, F(1))
    need(v0 >= v1, "negative Sturm root count")
    return v0 == v1, endpoints, v0, v1, g, sequence


def compact(a, degree=7):
    tick()
    a = poly(a)
    need(len(a) <= degree + 1, "compactification degree overflow")
    out = [F(0)] * (degree + 1)
    for k, c in enumerate(a):
        for r in range(degree - k + 1):
            out[k + r] += c * comb(degree - k, r) * ((-1) ** r)
    return poly(out)


def parity(a):
    need(len(a) == 8, "expected degree-seven coefficient array")
    even = poly((a[0], -a[2], a[4], -a[6]))
    odd = poly((a[1], -a[3], a[5], -a[7]))
    return even, odd


def physical(q, a, conjugate=True):
    tick()
    out = [F(0)] * 8
    for j, x in enumerate(q):
        for k, y in enumerate(a):
            phase = (j - k if conjugate else j + k) % 4
            if phase == 0:
                out[(j + k) // 2] += x * y
            elif phase == 2:
                out[(j + k) // 2] -= x * y
    return poly(out)


def parity_pair(q, a):
    f, g = parity(q)
    e, o = parity(a)
    return add(mul(f, e), shift(mul(g, o), 1))


def raw_columns(a):
    e, o = parity(a)
    columns = []
    for j in range(8):
        k = j // 2
        base = shift(e, k) if j % 2 == 0 else shift(o, k + 1)
        columns.append(scale(base, (-1) ** k))
    return tuple(columns)


def contract(q, columns):
    out = ZERO
    for c, column in zip(q, columns):
        out = add(out, scale(column, c))
    return out


def routh(a):
    tick()
    need(len(a) == 8 and a[7] == 1,
         "Routh input is not a monic septic")
    u = [a[7], a[5], a[3], a[1]]
    v = [a[6], a[4], a[2], a[0]]
    first_column = [u[0], v[0]]
    need(u[0] > 0 and v[0] > 0, "nonpositive initial Routh pivot")
    for row in range(2, 8):
        tick()
        need(v[0] > 0, "nonpositive Routh pivot")
        current = [
            (v[0] * u[j + 1] - u[0] * v[j + 1]) / v[0]
            for j in range(3)
        ] + [F(0)]
        need(current[0] > 0, "Routh stability failure")
        first_column.append(current[0])
        u, v = v, current
    return tuple(first_column)


def make_grid(lo, hi):
    varying = [j for j in range(7) if lo[j] != hi[j]]
    out = []
    for mask in range(1 << len(varying)):
        a = list(lo) + [F(1)]
        for bit, j in enumerate(varying):
            a[j] = hi[j] if (mask >> bit) & 1 else lo[j]
        out.append(tuple(a))
    return tuple(out)


def complete_grid(corners, lo, hi):
    if len(lo) != 7 or len(hi) != 7:
        return False
    if any(lo[j] > hi[j] for j in range(7)):
        return False
    count = 1 << sum(lo[j] != hi[j] for j in range(7))
    if len(corners) != count or len(set(corners)) != count:
        return False
    for a in corners:
        if len(a) != 8 or a[7] != 1:
            return False
        if any(a[j] not in (lo[j], hi[j]) for j in range(7)):
            return False
    return True


def fmt(a):
    return "(" + ", ".join(str(x) for x in a) + ")"


def certify_box(name, q, lo, hi, margin):
    tick()
    corners = make_grid(lo, hi)
    need(complete_grid(corners, lo, hi), name + ": incomplete grid")
    need(q[7] == 1, name + ": nonmonic numerator")
    print("BOX", name, "COUNT", len(corners), "MARGIN", margin)
    print("NUMERATOR_ASCENDING", fmt(q))
    print("NUMERATOR_ROUTH_FIRST_COLUMN", fmt(routh(q)))
    for mask, a in enumerate(corners):
        tick()
        p = physical(q, a)
        need(p == parity_pair(q, a), name + ": physical/parity mismatch")
        need(p == contract(q, raw_columns(a)),
             name + ": physical/raw-row mismatch")
        need(len(p) == 8 and p[7] == 1,
             name + ": wrong physical leading term")
        u = compact(p)
        need(value(u, F(0)) == q[0] * a[0],
             name + ": wrong zero-frequency endpoint")
        need(value(u, F(1)) == 1,
             name + ": wrong infinity endpoint")
        margin_polynomial = add(u, (-margin,))
        ok, endpoints, v0, v1, g, sequence = analyze_positive(
            margin_polynomial)
        need(ok, name + ": strict all-frequency margin failed")
        first_column = routh(a)
        print("CERTIFICATE", name, mask)
        print("DENOMINATOR_ASCENDING", fmt(a))
        print("PHYSICAL_PAIRING_ASCENDING", fmt(p))
        print("COMPACT_MARGIN_ASCENDING", fmt(margin_polynomial))
        print("ENDPOINTS", fmt(endpoints))
        print("SQUAREFREE_GCD_ASCENDING", fmt(g))
        print("STURM_VARIATIONS", v0, v1, "INTERIOR_ROOTS", v0 - v1)
        for index, row in enumerate(sequence):
            print("STURM_CHAIN", index, fmt(row))
        print("CORNER_ROUTH_FIRST_COLUMN", fmt(first_column))
    return len(corners)


def mutation(name, detected, discriminator, positivity_tested):
    tick()
    need(detected, "mutation was not discriminated: " + name)
    print("MUTATION", name, "DETECTED_BY", discriminator,
          "POSITIVITY_DISCRIMINATION",
          "TESTED" if positivity_tested else "NOTTESTED")


def main():
    tick()
    base = tuple(F(comb(7, j)) for j in range(8))
    eps = F(3, 4)
    delta = F(1, 2)
    c = sum((F(1, comb(7, j)) for j in range(7)), F(0))
    need(c == F(151, 105), "wrong reciprocal-binomial constant")
    need(F(36, 25) - c == F(1, 525), "wrong 6/5 comparison")
    slack = F(81, 100) - eps * eps * c
    need(slack == F(3, 2800), "wrong squared-norm slack")
    strengthened_margin = F(1, 10) + slack / F(9, 5)
    need(strengthened_margin == F(169, 1680),
         "wrong strengthened binomial margin")
    need(compact(base) == (F(1),),
         "compactification of (1+t)^7 is not one")

    qdelta = tuple(
        base[j] * (delta if j % 2 == 0 else F(1))
        for j in range(8))
    eta = delta / 10
    qnorm = sum(abs(x) for x in qdelta)
    rho = eta / (14 * qnorm)
    need(eta == F(1, 20), "wrong fixed-parity margin")
    need(qnorm == 96, "wrong numerator coefficient norm")
    need(rho == F(1, 26880), "wrong thickening radius")

    full_lo = tuple(base[j] - eps for j in range(7))
    full_hi = tuple(base[j] + eps for j in range(7))
    core_lo = tuple(
        base[j] - eps if j % 2 == 0 else base[j]
        for j in range(7))
    core_hi = tuple(
        base[j] + eps if j % 2 == 0 else base[j]
        for j in range(7))
    thick_lo = tuple(x - rho for x in core_lo)
    thick_hi = tuple(x + rho for x in core_hi)

    print("EXACT_CONSTANTS", c, slack, strengthened_margin,
          eta, qnorm, rho)
    count = certify_box(
        "binomial-128", base, full_lo, full_hi, F(1, 10))
    count += certify_box(
        "fixed-odd-16", qdelta, core_lo, core_hi, eta)
    count += certify_box(
        "thickened-128", qdelta, thick_lo, thick_hi, eta / 2)
    need(count == 272, "wrong total number of corner obligations")

    correct = physical(base, base)
    wrong_conjugate = physical(base, base, conjugate=False)
    mutation(
        "wrong-conjugation",
        wrong_conjugate != correct
        and value(compact(wrong_conjugate), F(1)) == -1,
        "negative-compact-infinity", True)

    e, o = parity(base)
    omitted_t = add(mul(e, e), mul(o, o))
    mutation(
        "omitted-t",
        omitted_t != correct
        and value(compact(omitted_t), F(1)) == 0,
        "zero-compact-infinity", True)

    extra_t = add(mul(e, e), shift(mul(o, o), 2))
    mutation(
        "extra-t",
        len(extra_t) == 9,
        "degree-eight-instead-of-seven", False)

    wrong_parity = tuple(
        base[j] * (delta if j % 2 == 1 else F(1))
        for j in range(8))
    mutation(
        "scaled-leading-odd-coefficient",
        wrong_parity[7] != 1
        and value(compact(physical(wrong_parity, base)), F(1)) == delta,
        "monicity-and-infinity-contract", False)

    zero_delta = tuple(
        F(0) if j % 2 == 0 else base[j]
        for j in range(8))
    zero_pair = compact(physical(zero_delta, base))
    mutation(
        "zero-delta",
        value(zero_pair, F(0)) == 0
        and not analyze_positive(zero_pair)[0],
        "zero-frequency-strictness", True)

    tangent = (F(1, 4), F(-1), F(1))
    tangent_result = analyze_positive(tangent)
    mutation(
        "tangential-interior-zero",
        not tangent_result[0]
        and tangent_result[1][0] > 0
        and tangent_result[1][1] > 0
        and tangent_result[2] - tangent_result[3] == 1,
        "one-distinct-interior-Sturm-root", True)

    columns = list(raw_columns(base))
    missing_column = list(columns)
    missing_column[6] = ZERO
    mutation(
        "omitted-raw-coefficient",
        contract(base, missing_column) != correct,
        "physical-versus-raw-identity", False)

    swapped_columns = list(columns)
    swapped_columns[0], swapped_columns[1] = (
        swapped_columns[1], swapped_columns[0])
    mutation(
        "wrong-raw-row-order",
        contract(base, swapped_columns) != correct,
        "physical-versus-raw-identity", False)

    full_grid = make_grid(full_lo, full_hi)
    omitted_coordinate_grid = tuple(
        tuple(a[j] if j != 6 else full_lo[6] for j in range(8))
        for a in full_grid)
    mutation(
        "omitted-corner-coordinate",
        not complete_grid(omitted_coordinate_grid, full_lo, full_hi)
        and len(set(omitted_coordinate_grid)) == 64,
        "incomplete-Cartesian-grid", False)

    tick()
    print("PASS: 272 exact full-frequency corner margin certificates.")
    print("PASS: physical/parity/raw identities and corner Routh checks.")
    print("PASS: nine controls discriminated their stated invariants.")
    print("No arbitrary-box, novelty, human, family, or kernel claim.")


if __name__ == "__main__":
    try:
        main()
    except BudgetExhausted as exc:
        print("NOT_CERTIFIED_BUDGET:", str(exc), file=sys.stderr)
        sys.exit(2)
    except VerificationError as exc:
        print("NOT_CERTIFIED_FAILURE:", str(exc), file=sys.stderr)
        sys.exit(1)

