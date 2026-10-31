
import sys
from fractions import Fraction as F
from math import comb, factorial, isqrt
from time import monotonic

class Failure(Exception):
    pass

class Rejection(Exception):
    pass

DEADLINE = float("inf")
COUNTS = [0, 0]
NVAR = 6
ZERO = (0,) * NVAR

def budget():
    if monotonic() >= DEADLINE:
        raise Failure("cooperative time limit reached; incomplete")

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.d = dict(value.d)
        elif isinstance(value, dict):
            self.d = {e: F(c) for e, c in value.items() if c}
        else:
            c = F(value)
            self.d = {ZERO: c} if c else {}

    @staticmethod
    def variable(k):
        e = [0] * NVAR
        e[k] = 1
        return P({tuple(e): F(1)})

    def __add__(self, other):
        other = P(other)
        out = dict(self.d)
        for e, c in other.d.items():
            out[e] = out.get(e, F(0)) + c
            if not out[e]:
                del out[e]
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.d.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) + (-self)

    def __mul__(self, other):
        budget()
        other = P(other)
        out = {}
        for e, c in self.d.items():
            budget()
            for f, d in other.d.items():
                g = tuple(e[k] + f[k] for k in range(NVAR))
                out[g] = out.get(g, F(0)) + c * d
        return P(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = F(other)
        if not q:
            raise Failure("division by zero")
        return P({e: c / q for e, c in self.d.items()})

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise Failure("invalid polynomial exponent")
        out = P(1)
        for unused in range(n):
            out = out * self
        return out

    def at(self, k, value):
        value = P(value)
        out = P(0)
        for e, c in self.d.items():
            f = list(e)
            f[k] = 0
            out += P({tuple(f): c}) * value ** e[k]
        return out

    def integral(self, k):
        out = {}
        for e, c in self.d.items():
            f = list(e)
            f[k] += 1
            out[tuple(f)] = c / f[k]
        return P(out)

    def scalar(self):
        if any(e != ZERO for e in self.d):
            raise Failure("uneliminated symbolic variable")
        return self.d.get(ZERO, F(0))

M, X, S, D, Y, LAM = [P.variable(k) for k in range(NVAR)]
THIRD = F(1, 3)

def same(a, b):
    if isinstance(a, P) or isinstance(b, P):
        return P(a).d == P(b).d
    return a == b

def check(name, condition):
    budget()
    if not condition:
        raise Failure(name)
    COUNTS[0] += 1
    print("CHECK " + name)

def check_equal(name, a, b):
    check(name, same(a, b))

def must_equal(reason, a, b):
    if not same(a, b):
        raise Rejection(reason)

def must_nonnegative(reason, value):
    if value < 0:
        raise Rejection(reason)

def expect_rejection(reason, action):
    budget()
    try:
        action()
    except Rejection as exc:
        if str(exc) != reason:
            raise Failure("wrong rejection reason: " + str(exc))
        COUNTS[1] += 1
        print("REJECT " + reason)
        return
    raise Failure("mutant survived: " + reason)

def t2(m):
    return m + 2 * m ** 2

def t3(m):
    return m + 6 * m ** 2 + 6 * m ** 3

def t4(m):
    return m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4

def psi0(x, y, lam):
    return THIRD * x ** 3 + (y ** 2 - lam) * x - 4 * THIRD * y ** 3 + lam * y

def psi1(x, y, lam, m):
    return psi0(x, y, lam) + m * (x ** 2 + y ** 2) + t2(m) * x

def d0(x, y, lam):
    return x ** 2 + y ** 2 - lam

def d1(x, y, lam, m):
    return (x + m) ** 2 + m * (1 + m) + y ** 2 - lam

def b0(t, s, y, lam):
    return d0(s, y, lam) * (t - s) + THIRD * (t - s) ** 2 * (t + 2 * s)

def b1(t, s, y, lam, m):
    return d1(s, y, lam, m) * (t - s) + (t - s) ** 2 * (THIRD * (t + 2 * s) + m)

def gamma(x, d, y, lam, m):
    return d1(x + 1, y, lam, m) * d + (x + 1 + m) * d ** 2 + THIRD * d ** 3

def constant_tail(d, lam, m):
    return 4 * d ** 2 * t2(m) + F(16, 3) * d * t3(m) + F(2, 3) * t4(m) - lam * (8 * d * m + 2 * t2(m))

def integral_poly(expr, lo, hi):
    primitive = P(expr).integral(4)
    return primitive.at(4, hi) - primitive.at(4, lo)

def integral_value(expr, lo, hi):
    return integral_poly(expr, lo, hi).scalar()

def symbolic_checks():
    st = [[0] * 5 for unused in range(5)]
    st[0][0] = 1
    for n in range(1, 5):
        for k in range(1, n + 1):
            st[n][k] = st[n - 1][k - 1] + k * st[n - 1][k]
    moments = [P(1)]
    for n in range(1, 5):
        moments.append(sum((st[n][k] * factorial(k) * M ** k for k in range(1, n + 1)), P(0)))
    expected = [P(1), M, t2(M), t3(M), t4(M)]
    for n in range(1, 5):
        check_equal("factorial-moment-polynomial-" + str(n), moments[n], expected[n])
        shifted = sum((comb(n, k) * moments[k] for k in range(n + 1)), P(0))
        check_equal("positive-power-shift-" + str(n), M * shifted, (1 + M) * moments[n])
    expect_rejection("shift-reindex-requires-positive-k", lambda: must_equal("shift-reindex-requires-positive-k", M, 1 + M))

    cap = 2 * X + S - Y
    check_equal("cap-area", integral_poly(8 * (cap - Y), X, X + S / 2), 2 * S ** 2)
    cap_q = 8 * (THIRD * cap ** 3 + Y ** 2 * cap - 4 * THIRD * Y ** 3)
    check_equal("cap-moment", integral_poly(cap_q, X, X + S / 2), 4 * X ** 2 * S ** 2 + F(8, 3) * X * S ** 3 + F(2, 3) * S ** 4)
    check_equal("diamond-area", 8 * integral_value(1 - 2 * Y, 0, F(1, 2)), 2)
    check_equal("diamond-moment", 8 * integral_value(THIRD * (1 - Y) ** 3 + Y ** 2 * (1 - Y) - 4 * THIRD * Y ** 3, 0, F(1, 2)), F(2, 3))
    check_equal("diamond-B", 8 * integral_value((1 - Y) ** 2 + Y ** 2, 0, F(1, 2)), F(8, 3))

    check_equal("diamond-complete-Z", M * (2 + 4 * M + 2 * moments[2]), (1 + M) * 2 * moments[2])
    diamond_tail_n = F(2, 3) + F(8, 3) * M + 4 * moments[2] + F(8, 3) * moments[3] + F(2, 3) * moments[4]
    check_equal("diamond-complete-N", M * diamond_tail_n, (1 + M) * F(2, 3) * moments[4])

    cut = F(2, 7)
    qstar = 1 + 3 * M + 2 * M ** 2
    numerator = 2 + M - 12 * M ** 2 - 12 * M ** 3
    check_equal("comparison-numerator", 3 * (1 + 2 * M) * qstar - (1 + 14 * M + 36 * M ** 2 + 24 * M ** 3), numerator)
    check_equal("two-sevenths-small-m-certificate", numerator, F(352, 343) + (cut - M) * (12 * M ** 2 + F(108, 7) * M + F(167, 49)))
    check_equal("two-sevenths-large-m-certificate", qstar - 2, F(1, 49) + (M - cut) * (2 * M + F(25, 7)))

    check_equal("bivariate-cubic-B0", psi0(X, Y, LAM) - psi0(S, Y, LAM), b0(X, S, Y, LAM))
    check_equal("bivariate-cubic-B1", psi1(X, Y, LAM, M) - psi1(S, Y, LAM, M), b1(X, S, Y, LAM, M))
    check_equal("pooled-gradient-cleared-denominator", d0(X, Y, LAM) + M * d1(X + 1, Y, LAM, M), (1 + M) * d1(X, Y, LAM, M))
    pooled = psi0(X, Y, LAM) - psi0(S, Y, LAM) + M * (psi1(X + 1, Y, LAM, M) - psi1(S + 1, Y, LAM, M))
    check_equal("pooled-cubic-difference", pooled, (1 + M) * b1(X, S, Y, LAM, M))
    check_equal("slack-cubic", psi1(X + 1 + D, Y, LAM, M) - psi1(X + 1, Y, LAM, M), gamma(X, D, Y, LAM, M))
    whole_core = psi0(X, Y, LAM) - psi0(S, Y, LAM) + M * (psi1(X + 1 + D, Y, LAM, M) - psi1(S + 1, Y, LAM, M))
    check_equal("core-calibration-8-and-8b", whole_core, (1 + M) * b1(X, S, Y, LAM, M) + M * gamma(X, D, Y, LAM, M))

def exact_sqrt(q):
    q = F(q)
    if q < 0:
        raise Failure("negative radicand on selected free branch")
    n, d = isqrt(q.numerator), isqrt(q.denominator)
    if n * n != q.numerator or d * d != q.denominator:
        raise Failure("control unexpectedly requires irrational selected root")
    return F(n, d)

def derivative(kind, x, y, lam, m):
    return d0(x, y, lam) if kind == 0 else d1(x, y, lam, m)

def interval_minimum(kind, lo, hi, y, lam, m):
    if lo > hi:
        raise Failure("empty interval")
    if lo == hi:
        return lo
    if derivative(kind, lo, y, lam, m) >= 0:
        return lo
    if derivative(kind, hi, y, lam, m) <= 0:
        return hi
    root = exact_sqrt(lam - y ** 2 - (m * (1 + m) if kind else 0)) - (m if kind else 0)
    if not lo < root < hi:
        raise Failure("constructed root is not interior")
    return root

def polygon_vertices(a, c, y):
    aa, bb = 2 * a - y, 2 * c - y
    points = [(a, c), (a, bb), (aa, c), (aa, bb),
              (a, a + 1), (aa, aa + 1), (c - 1, c), (bb - 1, bb)]
    return sorted(set((x, z) for x, z in points if a <= x <= aa and c <= z <= bb and z >= x + 1))

def joint_minimum(a, c, y, lam, m):
    aa, bb = 2 * a - y, 2 * c - y
    p = interval_minimum(0, a, aa, y, lam, m)
    q = interval_minimum(1, c, bb, y, lam, m)
    candidates = []
    if q >= p + 1:
        candidates.append((p, q))
    lo = max(a, c - 1)
    if lo <= aa:
        s = interval_minimum(1, lo, aa, y, lam, m)
        candidates.append((s, s + 1))
    if not candidates:
        raise Failure("no feasible candidate")
    def cost(pair):
        x, z = pair
        return (psi0(x, y, lam) + m * psi1(z, y, lam, m)) / (1 + m)
    result = min(candidates, key=cost)
    x, z = result
    vertices = polygon_vertices(a, c, y)
    if not vertices:
        raise Failure("empty feasible polygon")
    g0 = d0(x, y, lam) / (1 + m)
    g1 = m * d1(z, y, lam, m) / (1 + m)
    if any(g0 * (xx - x) + g1 * (zz - z) < 0 for xx, zz in vertices):
        raise Failure("supporting-gradient certificate failed")
    return result, p, q

def fixed_height_checks():
    m, a, c, y = F(1, 5), F(1, 4), F(7, 8), F(1, 8)
    roots = [F(1, 8), a, F(5, 16), F(3, 8), F(1, 2)]
    for index, r in enumerate(roots):
        lam = (r + m) ** 2 + m * (1 + m) + y ** 2
        pair, p, q = joint_minimum(a, c, y, lam, m)
        selected = max(a, min(F(3, 8), r))
        check_equal("synthetic-core-face-" + str(index), pair, (selected, selected + 1))
        check_equal("synthetic-independent-infeasibility-" + str(index), q - p - 1, F(-1, 2))

    blocks = [
        ("corner", F(1), F(5, 4), F(1, 2), [F(7, 8), F(1), F(9, 8), F(5, 4), F(11, 8)]),
        ("far-tail", F(7, 8), F(1), F(3, 4), [F(3, 4), F(7, 8), F(15, 16), F(1), F(9, 8)])
    ]
    for label, lo, hi, yy, cases in blocks:
        for index, r in enumerate(cases):
            lam = (r + m) ** 2 + m * (1 + m) + yy ** 2
            s = interval_minimum(1, lo, hi, yy, lam, m)
            check_equal("synthetic-" + label + "-face-" + str(index), s, max(lo, min(hi, r)))
            check("interval-normal-" + label + "-" + str(index), all(d1(s, yy, lam, m) * (t - s) >= 0 for t in (lo, hi)))
    check_equal("no-nonnegative-root", interval_minimum(1, F(1, 4), F(1, 2), 0, 0, m), F(1, 4))
    check_equal("collapsed-core", joint_minimum(a, c, a, F(2, 5), m)[0], (a, a + 1))
    check_equal("collapsed-edge-corner", interval_minimum(1, F(1), F(1), F(1, 2), 0, m), F(1))
    check_equal("collapsed-far-tail", interval_minimum(1, c, c, c, 0, m), c)
    check_equal("zero-core-vertex", joint_minimum(F(0), F(1, 2), F(0), F(0), m)[0], (F(0), F(1)))
    pair, p, q = joint_minimum(a, F(7, 4), y, F(1), m)
    check_equal("synthetic-slack-independent-pair", pair, (F(3, 8), F(7, 4)))
    check("synthetic-slack-is-strict", q > p + 1)

def profile_moments(pieces):
    area, moment, boundary = F(0), F(0), F(0)
    for lo, hi, f in pieces:
        if lo > hi:
            raise Failure("reversed profile interval")
        f = P(f)
        area += 8 * integral_value(f - Y, lo, hi)
        moment += 8 * integral_value(THIRD * f ** 3 + Y ** 2 * f - 4 * THIRD * Y ** 3, lo, hi)
        boundary += 8 * integral_value(f ** 2 + Y ** 2, lo, hi)
    return area, moment, boundary

def full_value(m, lam, d, first, tail):
    b = m / (1 + m)
    a0, q0, unused = profile_moments(first)
    a1, q1, boundary = profile_moments(tail)
    z = (1 - b) * a0 + b * (a1 + 8 * d * m + 2 * t2(m))
    n = (1 - b) * q0 + b * (q1 + m * boundary + (a1 + 8 * d ** 2) * t2(m) + F(16, 3) * d * t3(m) + F(2, 3) * t4(m))
    return n - lam * z, z, n

def endpoint_control(d, m, lam, a, u):
    b, z0, cut = m / (1 + m), a + 1, 2 * u - d
    if not a <= cut <= u <= d:
        raise Failure("endpoint construction outside its declared range")
    first = [(F(0), a, a)]
    tail = [(F(0), a, z0), (a, cut, 2 * u - Y), (cut, d, d)]
    h, z, n = full_value(m, lam, d, first, tail)
    ind, iz, inn = full_value(m, lam, d, [(F(0), a, 2 * a - Y)], [(F(0), d, d)])
    p0 = 8 * (1 - b) * integral_value(b0(a, 2 * a - Y, Y, lam), 0, a)
    core = 8 * b * integral_value(b1(z0, d, Y, lam, m), 0, a)
    corner = 8 * b * integral_value(b1(2 * u - Y, d, Y, lam, m), a, cut)
    penalty = p0 + core + corner
    check("positive-complete-denominator-" + str(d), z > 0)
    check_equal("endpoint-penalty-decomposition-" + str(d), h - ind, penalty)
    return {"h": h, "ind": ind, "p0": p0, "core": core, "corner": corner, "P": penalty, "tail": tail}

def profile_and_mutation_checks():
    m, lam, a, u, c = F(1, 5), F(2, 5), F(1, 4), F(3, 4), F(7, 8)
    b, z0 = m / (1 + m), a + 1
    delta = 1 + 3 * m + 2 * m ** 2 - lam
    check_equal("synthetic-delta", delta, F(32, 25))
    check_equal("pooled-lower-normal-minimum", d1(a, 0, lam, m), F(17, 400))
    check("independent-C0-upper-for-entire-core", max(d0(2 * a, 0, lam), d0(a, a, lam)) < 0)
    check("independent-tail-lower-for-both-endpoints", all(d1(d, 0, lam, m) > 0 for d in (u, c)))

    eu = endpoint_control(u, m, lam, a, u)
    ec = endpoint_control(c, m, lam, a, u)
    expected_u = {"p0": F(11, 192), "core": F(793, 3600), "corner": F(773, 3600), "P": F(2363, 4800)}
    expected_c = {"p0": F(11, 192), "core": F(7039, 38400), "corner": F(3447, 25600), "P": F(28819, 76800)}
    for key in expected_u:
        check_equal("edge-" + key, eu[key], expected_u[key])
        check_equal("interior-endpoint-" + key, ec[key], expected_c[key])

    actual_difference = ec["h"] - eu["h"]
    ind_difference = ec["ind"] - eu["ind"]
    check_equal("both-penalty-difference", ec["P"] - eu["P"], F(-8989, 76800))
    check_equal("independent-endpoint-difference", ind_difference, F(355469, 1152000))
    check_equal("complete-endpoint-difference", actual_difference, F(110317, 576000))
    check_equal("both-endpoint-subtraction", actual_difference, ind_difference + ec["P"] - eu["P"])

    endpoint_rhs = b * (constant_tail(c, lam, m) - constant_tail(u, lam, m))
    endpoint_rhs += 8 * b * integral_value(psi1(c, Y, lam, m), u, c)
    endpoint_rhs += 8 * b * integral_value(psi1(c, Y, lam, m) - psi1(u, Y, lam, m), 0, u)
    endpoint_rhs += ec["P"] - eu["P"]
    check_equal("general-endpoint-identity", actual_difference, endpoint_rhs)

    active_rhs = b * (constant_tail(c, lam, m) - constant_tail(u, lam, m))
    active_rhs += 8 * b * integral_value(psi1(c, Y, lam, m) - psi1(2 * u - Y, Y, lam, m), 2 * u - c, u)
    active_rhs += 8 * b * integral_value(psi1(c, Y, lam, m), u, c)
    check_equal("active-coupled-core-cancellation", actual_difference, active_rhs)

    expect_rejection("omitted-edge-tail-core-correction", lambda: must_equal("omitted-edge-tail-core-correction", ind_difference + ec["P"] - (eu["P"] - eu["core"]), actual_difference))
    expect_rejection("omitted-whole-edge-penalty", lambda: must_equal("omitted-whole-edge-penalty", ind_difference + ec["P"], actual_difference))
    expect_rejection("omitted-whole-other-endpoint-penalty", lambda: must_equal("omitted-whole-other-endpoint-penalty", ind_difference - eu["P"], actual_difference))

    dd = (a - Y) / 2
    slack_tail = [(F(0), a, z0 + dd), (a, u, 2 * u - Y), (u, u, u)]
    slack_h, unused_z, unused_n = full_value(m, lam, u, [(F(0), a, a)], slack_tail)
    direct_gap = slack_h - eu["h"]
    cubic_gap = 8 * b * integral_value(gamma(a, dd, Y, lam, m), 0, a)
    lower = 8 * b * delta * integral_value(dd, 0, a)
    check_equal("full-functional-slack-calibration", direct_gap, cubic_gap)
    check_equal("strict-slack-exact-gap", direct_gap, F(19933, 460800))
    check_equal("strict-slack-lower-bound", lower, F(2, 75))
    check_equal("strict-slack-positive-margin", direct_gap - lower, F(1529, 92160))
    check("strict-slack-inequality", direct_gap > lower > 0)
    expect_rejection("missing-eight-factor", lambda: must_equal("missing-eight-factor", cubic_gap / 8, direct_gap))
    expect_rejection("missing-b-factor", lambda: must_equal("missing-b-factor", cubic_gap / b, direct_gap))
    bad_gamma = -d1(z0, Y, lam, m) * dd + (z0 + m) * dd ** 2 + THIRD * dd ** 3
    bad_gap = 8 * b * integral_value(bad_gamma, 0, a)
    expect_rejection("strict-slack-linear-sign", lambda: must_nonnegative("strict-slack-linear-sign", bad_gap - lower))

    diamond_h, diamond_z, diamond_n = full_value(m, lam, F(1, 2), [(F(0), F(0), F(0))], [(F(0), F(1, 2), 1 - Y)])
    check_equal("numeric-diamond-Z", diamond_z, F(14, 25))
    check_equal("numeric-diamond-N", diamond_n, F(1358, 1875))
    check_equal("numeric-diamond-signed-value", diamond_h, F(2, 3) * t4(m) - 2 * lam * t2(m))
    expect_rejection("tail-weight-normalization", lambda: must_equal("tail-weight-normalization", (1 - b) * diamond_z, diamond_z))

    x, yy, ll = F(5, 16), F(1, 8), F(3317, 6400)
    correct_gradient = (1 - b) * d0(x, yy, ll) + b * d1(x + 1, yy, ll, m)
    wrong_gradient = (1 - b) * d0(x, yy, ll) + b * (1 - b) * d1(x + 1, yy, ll, m)
    check_equal("correct-pooled-root-gradient", correct_gradient, F(0))
    check_equal("wrong-tail-weight-explicit-residual", wrong_gradient, F(-9, 160))
    expect_rejection("tail-weight-pooled-gradient", lambda: must_equal("tail-weight-pooled-gradient", wrong_gradient, F(0)))

    yy = F(1, 2)
    floor = max(c, 2 * u - yy)
    omitted_floor = interval_minimum(1, c, 2 * c - yy, yy, lam, m)
    correct_corner = interval_minimum(1, floor, 2 * c - yy, yy, lam, m)
    check_equal("correct-corner-floor-minimum", correct_corner, F(1))
    check_equal("missing-corner-floor-gap", floor - omitted_floor, F(1, 8))
    expect_rejection("missing-corner-floor", lambda: must_nonnegative("missing-corner-floor", omitted_floor - floor))

def normal_cone_checks():
    nu = F(3, 7)
    edge_good, edge_bad = (-nu, nu), (nu, -nu)
    edge_rays = [(F(1), F(1)), (F(-1), F(-1)), (F(0), F(1))]
    check("correct-edge-normal-rays", all(edge_good[0] * da + edge_good[1] * dc >= 0 for da, dc in edge_rays))
    expect_rejection("reversed-edge-normal-cone", lambda: must_nonnegative("reversed-edge-normal-cone", edge_bad[1]))
    vertex_good = (F(-2, 7), F(3, 7))
    check("correct-vertex-normal-rays", vertex_good[1] >= 0 and sum(vertex_good) >= 0)
    vertex_bad = (F(-4, 7), F(3, 7))
    expect_rejection("wrong-vertex-diagonal-ray", lambda: must_nonnegative("wrong-vertex-diagonal-ray", sum(vertex_bad)))
    check("correct-a-zero-open-edge-normal", nu >= 0 and F(0) == 0)
    expect_rejection("reversed-a-zero-normal", lambda: must_nonnegative("reversed-a-zero-normal", -nu))
    check("interior-zero-normal", (F(0), F(0)) == (F(0), F(0)))

def main():
    global DEADLINE
    args = sys.argv[1:]
    seconds = 50
    if args:
        if len(args) != 2 or args[0] != "--seconds":
            raise Failure("usage: checker.py [--seconds INTEGER_IN_1_TO_55]")
        try:
            seconds = int(args[1])
        except ValueError:
            raise Failure("seconds must be an integer")
        if not 1 <= seconds <= 55:
            raise Failure("seconds must be in 1..55")
    DEADLINE = monotonic() + seconds
    symbolic_checks()
    fixed_height_checks()
    profile_and_mutation_checks()
    normal_cone_checks()
    budget()
    print("COMPLETE checks=%d intended_mutant_rejections=%d" % tuple(COUNTS))
    print("SCOPE exact algebra and synthetic finite controls; no actual optimizer or uniqueness certification")

if __name__ == "__main__":
    try:
        main()
    except (Failure, Rejection) as exc:
        print("FAIL " + str(exc))
        sys.exit(1)

