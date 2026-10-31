from fractions import Fraction as F
from math import comb, factorial

NVAR = 9
ZERO = (0,) * NVAR
PREDICATES = 0

class CheckFailure(Exception):
    pass

class MutationRejected(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason

def cp(value):
    if isinstance(value, dict):
        return value
    value = F(value)
    return {} if value == 0 else {ZERO: value}

def variable(index):
    exponent = list(ZERO)
    exponent[index] = 1
    return {tuple(exponent): F(1)}

X = [variable(i) for i in range(NVAR)]
m, t, a, q, y, c, U, r, lam = X

def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in cp(polynomial).items():
            result[exponent] = result.get(exponent, F(0)) + coefficient
    return {e: coefficient for e, coefficient in result.items() if coefficient}

def mul(*polynomials):
    result = cp(1)
    for polynomial in polynomials:
        product = {}
        for left, x in result.items():
            for right, z in cp(polynomial).items():
                exponent = tuple(i + j for i, j in zip(left, right))
                product[exponent] = product.get(exponent, F(0)) + x * z
        result = {e: coefficient for e, coefficient in product.items() if coefficient}
    return result

def neg(polynomial):
    return mul(-1, polynomial)

def power(polynomial, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise CheckFailure("invalid polynomial exponent")
    result = cp(1)
    for unused in range(exponent):
        result = mul(result, polynomial)
    return result

def derivative(polynomial, index):
    result = {}
    for exponent, coefficient in cp(polynomial).items():
        degree = exponent[index]
        if degree:
            reduced = list(exponent)
            reduced[index] -= 1
            reduced = tuple(reduced)
            result[reduced] = result.get(reduced, F(0)) + degree * coefficient
    return {e: coefficient for e, coefficient in result.items() if coefficient}

def substitute(polynomial, replacements):
    result = {}
    for exponent, coefficient in cp(polynomial).items():
        term = cp(coefficient)
        for index, degree in enumerate(exponent):
            if degree:
                term = mul(term, power(replacements.get(index, X[index]), degree))
        result = add(result, term)
    return result

def value(polynomial, assignments):
    result = substitute(polynomial, {i: cp(x) for i, x in assignments.items()})
    if any(exponent != ZERO for exponent in result):
        raise CheckFailure("value called with an unassigned active variable")
    return result.get(ZERO, F(0))

def check(label, condition):
    global PREDICATES
    if not condition:
        raise CheckFailure(label)
    PREDICATES += 1

def equal(label, left, right):
    check(label, cp(left) == cp(right))

def coefficient_positive_constant(label, polynomial):
    polynomial = cp(polynomial)
    check(label, polynomial.get(ZERO, F(0)) > 0 and all(x >= 0 for x in polynomial.values()))

def bernstein_two_variables(polynomial, indices, lower, width):
    replacements = {i: add(lo, mul(w, X[i])) for i, lo, w in zip(indices, lower, width)}
    shifted = substitute(polynomial, replacements)
    allowed = set(indices)
    check("Bernstein variables", all(all(not degree or i in allowed for i, degree in enumerate(e)) for e in shifted))
    first, second = indices
    degree_first = max((e[first] for e in shifted), default=0)
    degree_second = max((e[second] for e in shifted), default=0)
    coefficients = []
    for i in range(degree_first + 1):
        row = []
        for j in range(degree_second + 1):
            total = F(0)
            for exponent, coefficient in shifted.items():
                k, ell = exponent[first], exponent[second]
                if k <= i and ell <= j:
                    total += coefficient * F(comb(i, k), comb(degree_first, k)) * F(comb(j, ell), comb(degree_second, ell))
            row.append(total)
        coefficients.append(row)
    return coefficients

def guard(reason, condition):
    if not condition:
        raise MutationRejected(reason)

def polynomial_guard(reason, observed, expected):
    guard(reason, cp(observed) == cp(expected))

def reject_mutant(label, expected_reason, operation):
    try:
        operation()
    except MutationRejected as error:
        if error.reason != expected_reason:
            raise CheckFailure(label + ": wrong rejection reason " + error.reason)
        print("CONTROL_REJECTED", label, error.reason)
    else:
        raise CheckFailure(label + ": mutant was accepted")

REQUIRED_BOUNDARIES = frozenset(("all_upper", "rounded", "lower_face", "a0", "q_a", "q0", "T2_equal_half"))

def boundary_guard(covered):
    guard("BOUNDARY_A0", "a0" in covered)
    guard("BOUNDARY_Q0", "q0" in covered)
    guard("BOUNDARY_COVERAGE", REQUIRED_BOUNDARIES <= set(covered))

def strip_admission(flags):
    guard("STRIP_ADMISSIBILITY", len(flags) == 7 and all(flags))

def original_cutoff_prerequisites(reduction, attainment, localization_without_cutoff):
    guard("UNPAID_GLOBAL_ATTAINMENT_LOCALIZATION", reduction and attainment and localization_without_cutoff)

def main():
    # Variables: m,t,a,q,y,c,U,r,lambda. No candidate code is imported.
    stirling = [[0] * 5 for unused in range(5)]
    stirling[0][0] = 1
    for n in range(1, 5):
        for k in range(1, n + 1):
            stirling[n][k] = stirling[n - 1][k - 1] + k * stirling[n - 1][k]
    raw = [add(*(mul(stirling[n][k] * factorial(k), power(m, k)) for k in range(n + 1))) for n in range(5)]
    moments = [add(*(mul(comb(n, j), power(t, n - j), raw[j]) for j in range(n + 1))) for n in range(5)]
    T2, T3, T4 = raw[2], raw[3], raw[4]
    v = add(m, power(m, 2))
    kappa = add(F(1, 3), mul(2, v))
    equal("T2", T2, add(m, mul(2, power(m, 2))))
    equal("T3", T3, add(m, mul(6, power(m, 2)), mul(6, power(m, 3))))
    equal("T4", T4, add(m, mul(14, power(m, 2)), mul(36, power(m, 3)), mul(24, power(m, 4))))
    # PGF derivative recurrence after clearing rational denominators. U is z here.
    denominator = add(1, m, mul(-1, m, U))
    equal("PGF denominator at one", substitute(denominator, {6: cp(1)}), 1)
    for j in range(4):
        numerator = mul(factorial(j), power(m, j))
        cleared_derivative = add(mul(denominator, derivative(numerator, 6)), mul(-(j + 1), numerator, derivative(denominator, 6)))
        equal("PGF derivative recurrence " + str(j), cleared_derivative, mul(factorial(j + 1), power(m, j + 1)))
    M2, M4 = moments[2], moments[4]
    numerator = mul(F(2, 3), M4)
    normalizer = mul(2, M2)
    signed = add(numerator, mul(-1, lam, normalizer))
    equal("signed scalar coefficient", signed, mul(F(2, 3), add(M4, mul(-3, lam, M2))))
    K = add(M4, mul(F(-3, 2), M2))
    upper = add(M4, mul(-6, M2))
    expected_K = add(power(t, 4), mul(4, m, power(t, 3)), mul(add(mul(6, m), mul(12, power(m, 2)), F(-3, 2)), power(t, 2)), mul(add(m, mul(24, power(m, 2)), mul(24, power(m, 3))), t), mul(24, power(m, 4)), mul(36, power(m, 3)), mul(11, power(m, 2)), mul(F(-1, 2), m))
    expected_upper = add(power(t, 4), mul(4, m, power(t, 3)), mul(add(mul(6, m), mul(12, power(m, 2)), -6), power(t, 2)), mul(add(mul(-8, m), mul(24, power(m, 2)), mul(24, power(m, 3))), t), mul(24, power(m, 4)), mul(36, power(m, 3)), mul(2, power(m, 2)), mul(-5, m))
    equal("independent K coefficient array", K, expected_K)
    equal("independent upper coefficient array", upper, expected_upper)
    equal("half scalar signed objective", substitute(signed, {8: cp(F(1, 2))}), mul(F(2, 3), K))
    equal("two scalar signed objective", substitute(signed, {8: cp(2)}), mul(F(2, 3), upper))
    L = add(mul(384, power(m, 4)), mul(768, power(m, 3)), mul(416, power(m, 2)), mul(32, m), -5)
    equal("K half equals L over sixteen", substitute(K, {1: cp(F(1, 2))}), mul(F(1, 16), L))
    equal("L derivative", derivative(L, 0), add(mul(1536, power(m, 3)), mul(2304, power(m, 2)), mul(832, m), 32))
    coefficient_positive_constant("L strictly increasing", derivative(L, 0))
    Kp = derivative(K, 1)
    Kpp = derivative(Kp, 1)
    equal("K second derivative", Kpp, add(mul(12, power(t, 2)), mul(24, m, t), mul(12, T2), -3))
    equal("K third derivative", derivative(Kpp, 1), add(mul(24, t), mul(24, m)))
    lo, hi = F(7, 100), F(3, 40)
    minus, plus, t0 = F(223, 3000), F(119, 1600), F(21, 40)
    half, three_fifths = F(1, 2), F(3, 5)
    check("ordered source intervals", lo < minus < plus < hi)
    source_values = (
        ("K minus t0", K, {0: minus, 1: t0}, F(-23195458191, 81000000000000)),
        ("K plus t0", K, {0: plus, 1: t0}, F(63277144, 6553600000000)),
        ("Kprime plus t0", Kp, {0: plus, 1: t0}, F(20796776, 4096000000)),
        ("Ksecond plus half", Kpp, {0: plus, 1: half}, F(4909464, 2560000)),
        ("Kprime high half", Kp, {0: hi, 1: half}, F(-299, 8000)),
        ("Kprime low three fifths", Kp, {0: lo, 1: three_fifths}, F(17099, 125000)),
        ("L minus", L, {0: minus}, F(357360169344, 81000000000000)),
        ("L low", L, {0: lo}, F(-44895616, 100000000)),
        ("L high", L, {0: hi}, F(1523, 20000)),
    )
    for label, polynomial, assignments, expected in source_values:
        observed = value(polynomial, assignments)
        equal(label, observed, expected)
        print("EXACT", label, str(observed))
    check("lower negative", value(K, {0: minus, 1: t0}) < 0)
    check("upper value bound", value(K, {0: plus, 1: t0}) > F(19, 2000000))
    check("upper derivative bound", 0 < value(Kp, {0: plus, 1: t0}) < F(13, 2500))
    check("upper curvature bound", value(Kpp, {0: plus, 1: half}) > F(19, 10))
    strong_lower = F(19, 2000000) - F(13, 2500) ** 2 / (2 * F(19, 10))
    equal("strong convexity lower value", strong_lower, F(453, 190000000))
    check("strong convexity lower positive", strong_lower > 0)
    equal("second derivative at zero upper m", value(Kpp, {0: hi, 1: F(0)}), F(-393, 200))
    coefficient_positive_constant("Kprime increasing in m", derivative(Kp, 0))
    shifted_parameter_derivative = substitute(derivative(K, 0), {0: add(lo, m)})
    coefficient_positive_constant("uniform parameter derivative positive", shifted_parameter_derivative)
    check("uniform parameter derivative margin", shifted_parameter_derivative.get(ZERO, F(0)) >= F(26, 25))
    Kzero = substitute(K, {1: cp(0)})
    coefficient_positive_constant("endpoint K positive above low m", substitute(Kzero, {0: add(lo, m)}))
    bernstein = bernstein_two_variables(Kpp, (0, 1), (lo, half), (hi - lo, three_fifths - half))
    expected_bernstein = [[F(2247, 1250), F(1551, 625), F(4107, 1250)], [F(933, 500), F(2553, 1000), F(84, 25)], [F(387, 200), F(21, 8), F(687, 200)]]
    check("exact Bernstein curvature matrix", bernstein == expected_bernstein)
    check("all Bernstein curvature coefficients positive", all(x > 0 for row in bernstein for x in row))
    for row in bernstein:
        print("BERNSTEIN_ROW", " ".join(str(x) for x in row))
    equal("explicit lower b map", minus / (1 + minus), F(223, 3223))
    equal("explicit upper b map", F(33, 100) / (1 + F(33, 100)), F(33, 133))
    # Cleared identity for monotonicity of x/(1+x); t is a second parameter.
    equal("b map difference numerator", add(mul(m, add(1, t)), mul(-1, t, add(1, m))), add(m, neg(t)))
    def D(x):
        return add(mul(2, power(x, 2)), mul(2, m, x), T2)
    def d(z, yy):
        return add(power(add(z, m), 2), v, power(yy, 2), neg(lam))
    Qstar = add(1, mul(3, m), mul(2, power(m, 2)))
    coefficient_positive_constant("fixed scalar tail slack", add(Qstar, F(-1, 2)))
    D0 = add(mul(2, c, T2), mul(2, m, power(c, 2)), mul(F(2, 3), T3), mul(-1, m, lam))
    equal("D0 decomposition", D0, add(mul(m, add(D(c), neg(lam))), mul(2, c, v), mul(F(2, 3), m), mul(3, power(m, 2)), mul(2, power(m, 3))))
    equal("D at half", substitute(D(c), {5: cp(half)}), add(half, mul(2, v)))
    equal("D increasing from half", add(D(c), neg(substitute(D(c), {5: cp(half)}))), mul(add(c, F(-1, 2)), add(mul(2, c), 1, mul(2, m))))
    cgap = add(c, neg(y))
    equal("clipped negative-part gap", add(d(add(mul(2, c), neg(y)), y), neg(d(c, c))), add(mul(2, power(cgap, 2)), mul(2, m, cgap)))
    equal("clipped integrand y derivative", derivative(d(add(mul(2, c), neg(y)), y), 4), add(mul(4, y), mul(-4, c), mul(-2, m)))
    equal("projected F1 lower margin", add(U, 1, neg(c)), add(U, neg(a), a, 1, neg(c)))
    equal("projected F1 upper margin", add(mul(2, a), 1, neg(y), neg(add(U, 1))), add(mul(2, a), neg(y), neg(U)))
    s = add(mul(2, a), 1, neg(c))
    equal("strip integral orientation", add(c, neg(s)), mul(2, add(c, neg(a), F(-1, 2))))
    R = add(mul(4, power(a, 2)), mul(4, m, a), T2)
    lamq = add(D(a), mul(2, m, q), mul(2, power(q, 2)))
    gain = mul(power(add(U, neg(r)), 2), add(mul(F(1, 3), add(U, mul(2, r))), m))
    equal("gain derivative in U", derivative(gain, 6), add(power(add(U, m), 2), neg(power(add(r, m), 2))))
    equal("gain zero at U equals r", substitute(gain, {6: r}), 0)
    endpoint_identity = add(lam, neg(v), neg(power(add(a, neg(q)), 2)), neg(power(add(a, q, m), 2)))
    equal("principal radical endpoint square", substitute(endpoint_identity, {8: lamq}), 0)
    primitive = add(mul(add(R, neg(lam)), y), mul(-1, add(mul(2, a), m), power(y, 2)), mul(F(2, 3), power(y, 3)))
    equal("quadratic integrand primitive", derivative(primitive, 4), d(add(mul(2, a), neg(y)), y))
    integral = substitute(primitive, {4: add(a, neg(q))})
    pre_F = add(mul(F(1, 3), substitute(moments[3], {1: mul(2, a)})), mul(F(-1, 2), lam, substitute(moments[1], {1: mul(2, a)})), neg(integral))
    FR = add(mul(m, add(power(a, 2), mul(add(1, mul(2, m)), a), kappa, mul(F(-1, 2), lam))), mul(-1, m, power(q, 2)), mul(F(-4, 3), power(q, 3)))
    equal("rounded derivative after joining constraint", substitute(pre_F, {8: lamq}), substitute(FR, {8: lamq}))
    FRprime = add(mul(m, add(mul(2, a), 1, mul(2, m))), mul(2, q, add(mul(2, a), m)))
    equal("implicit rounded derivative cleared denominator", add(mul(add(m, mul(2, q)), derivative(FR, 2)), mul(-1, add(mul(2, a), m), derivative(FR, 3))), mul(add(m, mul(2, q)), FRprime))
    check("FRprime has nonnegative coefficients", all(x >= 0 for x in FRprime.values()))
    J = add(mul(m, add(mul(add(1, mul(2, m)), a), F(1, 12), mul(2, v))), mul(F(-4, 3), power(a, 3)))
    FRhalf = substitute(FR, {8: cp(half)})
    equal("q equals a join", substitute(FRhalf, {3: a}), J)
    equal("all upper join derivative matching", add(substitute(Kp, {1: mul(2, a)}), mul(-12, J)), mul(12, a, add(R, F(-1, 2))))
    equal("J parameter derivative", derivative(J, 0), add(mul(add(1, mul(4, m)), a), F(1, 12), mul(4, m), mul(6, power(m, 2))))
    coefficient_positive_constant("J parameter derivative positive", derivative(J, 0))
    equal("J concavity", derivative(derivative(J, 2), 2), mul(-8, a))
    join_values = (
        ("R low at three tenths", R, {0: lo, 2: F(3, 10)}, F(2619, 5000)),
        ("R high at one quarter", R, {0: hi, 2: F(1, 4)}, F(329, 800)),
        ("J low at zero", J, {0: lo, 2: F(0)}, F(24479, 1500000)),
        ("J low at three tenths", J, {0: lo, 2: F(3, 10)}, F(6389, 1500000)),
    )
    for label, polynomial, assignments, expected in join_values:
        observed = value(polynomial, assignments)
        equal(label, observed, expected)
        print("EXACT", label, str(observed))
    equal("q zero endpoint derivative", substitute(FRhalf, {3: cp(0)}), mul(m, add(power(a, 2), mul(add(1, mul(2, m)), a), F(1, 12), mul(2, v))))
    equal("a zero empty core expression", substitute(mul(F(2, 3), substitute(K, {1: mul(2, a)})), {2: cp(0)}), mul(F(2, 3), Kzero))
    # Positive controls for scope bookkeeping are NOT proofs of their premises.
    boundary_guard(REQUIRED_BOUNDARIES)
    strip_admission((True, True, True, True, True, True, True))
    original_cutoff_prerequisites(True, True, True)
    # Algebraic mutants: require the intended reason, not an arbitrary exception.
    reject_mutant("unnormalized geometric mass", "GEOMETRIC_MASS_NORMALIZATION", lambda: polynomial_guard("GEOMETRIC_MASS_NORMALIZATION", add(1, m), 1))
    reject_mutant("geometric tail omitted", "COMPLETE_GEOMETRIC_M2", lambda: polynomial_guard("COMPLETE_GEOMETRIC_M2", power(t, 2), M2))
    wrong_signed = mul(F(2, 3), add(M4, mul(-1, lam, M2)))
    reject_mutant("wrong lambda factor", "SIGNED_LAMBDA_FACTOR", lambda: polynomial_guard("SIGNED_LAMBDA_FACTOR", wrong_signed, signed))
    # Delta is a formal nonnegative comparison gap, not a chosen optimizer.
    delta = U
    reject_mutant("minimum comparison reversed", "MINIMUM_COMPARATOR_DIRECTION", lambda: polynomial_guard("MINIMUM_COMPARATOR_DIRECTION", delta, neg(delta)))
    reject_mutant("equality called strict improvement", "GAMMA_EQUALITY_IS_NOT_STRICT", lambda: guard("GAMMA_EQUALITY_IS_NOT_STRICT", F(0) < 0))
    reject_mutant("wrong lower b mapping", "B_LOWER_MAPPING", lambda: polynomial_guard("B_LOWER_MAPPING", minus / (1 - minus), minus / (1 + minus)))
    # Logical endpoint/coverage/admission mutants, not numerical experiments.
    reject_mutant("closed lower threshold", "STRICT_LOWER_ENDPOINT", lambda: guard("STRICT_LOWER_ENDPOINT", ">=" == ">"))
    reject_mutant("a zero omitted", "BOUNDARY_A0", lambda: boundary_guard(REQUIRED_BOUNDARIES - {"a0"}))
    reject_mutant("q zero join omitted", "BOUNDARY_Q0", lambda: boundary_guard(REQUIRED_BOUNDARIES - {"q0"}))
    reject_mutant("core admissibility absent", "STRIP_ADMISSIBILITY", lambda: strip_admission((True, True, True, False, True, True, True)))
    reject_mutant("strip promoted to global existence", "UNPAID_GLOBAL_ATTAINMENT_LOCALIZATION", lambda: original_cutoff_prerequisites(True, False, False))
    print("EXACT_PREDICATE_COUNT", PREDICATES)
    print("RESULT: EXACT_ALGEBRA_AND_GUARD_CHECKS_COMPLETE")
    print("LIMIT: NO_ACTUAL_OPTIMIZER_OR_ORIGINAL_EXISTENCE_CERTIFICATE")
    print("LIMIT: NO_RADICAL_QUADRATURE_OR_NEW_SOURCE_EQUIVALENCE")
    print("LIMIT: RETAINED_CLIPPED_VALUE_IDENTITIES_REMAIN_ANALYTIC_IMPORTS")

if __name__ == "__main__":
    main()
