from fractions import Fraction as F
from math import comb, factorial
from time import monotonic

START = monotonic()
CHECKS = 0
NV = 7
ZERO = (0,) * NV

class Failure(Exception):
    pass

def deadline():
    if monotonic() - START > 55:
        raise Failure("cooperative 55-second deadline exceeded")

def check(label, condition):
    global CHECKS
    deadline()
    if not condition:
        raise Failure(label)
    CHECKS += 1

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.d = dict(value.d)
        elif isinstance(value, dict):
            self.d = {tuple(k): F(v) for k, v in value.items() if v}
        else:
            value = F(value)
            self.d = {} if not value else {ZERO: value}

    def __add__(self, other):
        out = dict(self.d)
        for monomial, coefficient in P(other).d.items():
            value = out.get(monomial, F(0)) + coefficient
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) + (-self)

    def __mul__(self, other):
        deadline()
        out = {}
        for left, lc in self.d.items():
            for right, rc in P(other).d.items():
                monomial = tuple(x + y for x, y in zip(left, right))
                out[monomial] = out.get(monomial, F(0)) + lc * rc
        return P(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (F(1) / F(scalar))

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise Failure("invalid polynomial exponent")
        result, base = P(1), self
        while exponent:
            deadline()
            if exponent & 1:
                result = result * base
            exponent //= 2
            if exponent:
                base = base * base
        return result

    def __eq__(self, other):
        return self.d == P(other).d

    def diff(self, index):
        out = {}
        for monomial, coefficient in self.d.items():
            exponent = monomial[index]
            if exponent:
                key = list(monomial)
                key[index] -= 1
                out[tuple(key)] = coefficient * exponent
        return P(out)

    def sub(self, replacements):
        deadline()
        targets = {i: P(v) for i, v in replacements.items()}
        out = P(0)
        for monomial, coefficient in self.d.items():
            term = P(coefficient)
            for i, exponent in enumerate(monomial):
                if exponent:
                    term = term * targets.get(i, X[i]) ** exponent
            out = out + term
        return out

    def scalar(self):
        if any(key != ZERO for key in self.d):
            raise Failure("scalar requested with unsubstituted variables")
        return self.d.get(ZERO, F(0))

    def coefficients(self, index):
        for monomial in self.d:
            if any(e for i, e in enumerate(monomial) if i != index):
                raise Failure("univariate coefficients requested for multivariate input")
        degree = max((key[index] for key in self.d), default=0)
        out = [F(0)] * (degree + 1)
        for monomial, coefficient in self.d.items():
            out[monomial[index]] = coefficient
        return out

X = []
for index in range(NV):
    key = [0] * NV
    key[index] = 1
    X.append(P({tuple(key): F(1)}))
M, T, U, A, Q, Y, R = range(NV)
m, t, u, a, q, y, r = X

def same(label, left, right):
    check(label, P(left) == P(right))

def value(poly, replacements):
    return P(poly).sub(replacements).scalar()

def orthant_positive(poly):
    poly = P(poly)
    return poly.d.get(ZERO, F(0)) > 0 and all(c >= 0 for c in poly.d.values())

def bernstein(poly, index, left, right):
    transformed = P(poly).sub({index: F(left) + (F(right) - F(left)) * X[index]})
    coefficients = transformed.coefficients(index)
    degree = len(coefficients) - 1
    return tuple(
        sum((coefficients[j] * F(comb(k, j), comb(degree, j))
             for j in range(k + 1)), F(0))
        for k in range(degree + 1)
    )

def interval_nonnegative(label, poly, index, left, right, strict=False):
    coefficients = bernstein(poly, index, left, right)
    check(label, all(c > 0 if strict else c >= 0 for c in coefficients))
    print("BERNSTEIN", label, tuple(str(c) for c in coefficients))
    return coefficients

def raw_moment(n):
    # Stirling conversion of factorial moments j! m^j.
    stirling = [0] * (n + 1)
    stirling[0] = 1
    for unused in range(n):
        stirling = [0] + [
            stirling[k - 1] + k * stirling[k] for k in range(1, n + 1)
        ]
    return sum((stirling[k] * factorial(k) * m ** k
                for k in range(n + 1)), P(0))

def moment(n, shift):
    shift = P(shift)
    return sum((comb(n, j) * raw_moment(j) * shift ** (n - j)
                for j in range(n + 1)), P(0))

def reject(name, wrong, reference):
    check("intended mutant differs: " + name, wrong != reference)
    print("REJECTED_MUTANT", name)

def main():
    # H(z)=1/(1+m(1-z)); its denominator at z=1 is one.
    pgf_denominator = 1 + m - m * t
    same("normalized PGF", pgf_denominator.sub({T: 1}), 1)
    for order in range(1, 5):
        previous_numerator = factorial(order - 1) * m ** (order - 1)
        same("PGF factorial derivative " + str(order),
             -order * previous_numerator * pgf_denominator.diff(T),
             factorial(order) * m ** order)

    T2 = m + 2 * m ** 2
    T3 = m + 6 * m ** 2 + 6 * m ** 3
    T4 = m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4
    same("raw moment zero", raw_moment(0), 1)
    same("raw moment one", raw_moment(1), m)
    same("raw moment two", raw_moment(2), T2)
    same("raw moment three", raw_moment(3), T3)
    same("raw moment four", raw_moment(4), T4)
    M2, M4 = moment(2, t), moment(4, t)
    same("shifted second moment", M2, t ** 2 + 2 * m * t + T2)
    same("shifted fourth moment", M4,
         t ** 4 + 4 * m * t ** 3 + 6 * T2 * t ** 2 + 4 * T3 * t + T4)
    Z, N = 2 * M2, F(2, 3) * M4
    L = 384 * m ** 4 + 768 * m ** 3 + 416 * m ** 2 + 32 * m - 5
    same("half-radius lower certificate",
         (M4 - F(3, 2) * M2).sub({T: F(1, 2)}), L / 16)
    check("L strictly increasing for nonnegative m", orthant_positive(L.diff(M)))
    same("L lower sign", value(L, {M: F(7, 100)}), F(-350747, 781250))
    same("L upper sign", value(L, {M: F(3, 40)}), F(1523, 20000))

    quartic = (t ** 4 + 4 * m * t ** 3 + (6 * m + 12 * m ** 2 - 6) * t ** 2
               + (-8 * m + 24 * m ** 2 + 24 * m ** 3) * t
               + 24 * m ** 4 + 36 * m ** 3 + 2 * m ** 2 - 5 * m)
    same("P=M4-6M2", quartic, M4 - 6 * M2)
    same("complete signed all-diamond objective", N - 2 * Z, F(2, 3) * quartic)
    dp, ddp = quartic.diff(T), quartic.diff(T).diff(T)
    same("critical cubic", dp / 4,
         t ** 3 + 3 * m * t ** 2 + (3 * m + 6 * m ** 2 - 3) * t
         - 2 * m + 6 * m ** 2 + 6 * m ** 3)
    same("second t derivative", ddp, 12 * t ** 2 + 24 * m * t + 12 * (T2 - 1))
    lo, hi = F(3, 10), F(1, 3)
    interval_nonnegative("Pprime(0) lower bound",
                         dp.sub({T: 0}) - F(51, 125), M, lo, hi)
    interval_nonnegative("Pprime(1/2) upper bound",
                         -F(5, 18) - dp.sub({T: F(1, 2)}), M, lo, hi)
    interval_nonnegative("Pprime(1) lower bound",
                         dp.sub({T: 1}) - F(221, 125), M, lo, hi)
    interval_nonnegative("T2<1 on critical interval", 1 - T2, M, lo, hi, True)
    check("Psecond strictly increases on t>=0",
          orthant_positive(ddp.diff(T).sub({M: lo + m})))

    dm = quartic.diff(M)
    same("parameter derivative at 3/10", dm.sub({M: lo}),
         4 * t ** 3 + F(66, 5) * t ** 2 + F(322, 25) * t + F(1064, 125))
    same("second parameter derivative", dm.diff(M),
         24 * t ** 2 + (48 + 144 * m) * t + 4 + 216 * m + 288 * m ** 2)
    check("parameter derivative positive at 3/10",
          orthant_positive(dm.sub({M: lo})))
    check("parameter derivative increases for m>=3/10",
          orthant_positive(dm.diff(M).sub({M: lo + m})))

    W = 27 * t ** 4 + 36 * t ** 3 - 72 * t ** 2 + 24 * t + 5
    J = 4 * t ** 3 + 14 * t ** 2 + 16 * t + F(107, 9)
    B = 12 * t ** 2 + 48 * t + 54
    C = 24 * t + 68
    same("expansion about 1/3", quartic.sub({M: F(1, 3) + u}),
         W / 27 + u * J + u ** 2 * B + u ** 3 * C + 24 * u ** 4)
    check("first W Bernstein table",
          bernstein(W, T, 0, F(1, 2)) ==
          (F(5), F(8), F(8), F(49, 8), F(83, 16)))
    check("second W Bernstein table",
          bernstein(W, T, F(1, 2), 1) ==
          (F(83, 16), F(17, 4), F(17, 4), F(8), F(20)))
    interval_nonnegative("J upper bound", F(413, 9) - J, T, 0, 1)
    interval_nonnegative("C upper bound", 92 - C, T, 0, 1)
    check("B nonnegative on nonnegative t", all(c >= 0 for c in B.d.values()))
    upper_margin = F(17, 108) - F(413, 2700) - F(92, 27000000)
    same("upper bracket margin", upper_margin, F(29977, 6750000))
    check("upper bracket margin positive", upper_margin > 0)
    beta_lo, beta_hi = F(13, 40), F(33, 100)
    same("upper bracket displacement", beta_hi - F(1, 3), F(-1, 300))
    same("lower bracket negative witness",
         value(quartic, {M: beta_lo, T: F(2, 3)}), F(-1508857, 25920000))
    same("lower bracket origin positive",
         value(quartic, {M: beta_lo, T: 0}), F(28743, 320000))
    same("lower bracket other endpoint positive",
         value(quartic, {M: beta_lo, T: 1}), F(117183, 320000))

    v = m * (1 + m)
    kappa = F(1, 3) + 2 * v
    Da = 2 * a ** 2 + 2 * m * a + T2
    Ra = 4 * a ** 2 + 4 * m * a + T2
    Qstar = 1 + 3 * m + 2 * m ** 2
    K = Da + 2 * m * q + 2 * q ** 2 - 2
    cap = 2 * a - y
    droot = r ** 2 + 2 * m * r + T2 + y ** 2 - 2
    same("free radical root equation", droot, (r + m) ** 2 + v + y ** 2 - 2)
    def psi(x):
        return x ** 3 / 3 + m * x ** 2 + (T2 + y ** 2 - 2) * x
    gain = (cap - r) ** 2 * ((cap + 2 * r) / 3 + m)
    same("cubic improvement identity", psi(cap) - psi(r) - gain, (cap - r) * droot)
    same("free-to-upper root relation", droot.sub({R: a + q, Y: a - q}), K)
    same("moving endpoint gain vanishes", gain.sub({R: a + q, Y: a - q}), 0)

    dcap = cap ** 2 + 2 * m * cap + T2 + y ** 2 - 2
    primitive = ((4 * a ** 2 + 4 * m * a + T2 - 2) * y
                 - (2 * a + m) * y ** 2 + F(2, 3) * y ** 3)
    same("polynomial integral primitive", primitive.diff(Y), dcap)
    I = primitive.sub({Y: a - q})
    Itotal = F(8, 3) * a ** 3 + 3 * m * a ** 2 + (T2 - 2) * a
    same("rounded positive integral reduction",
         I - Itotal - m * q ** 2 - F(4, 3) * q ** 3, -q * K)
    FR = (m * (a ** 2 + (1 + 2 * m) * a + kappa - 1)
          - m * q ** 2 - F(4, 3) * q ** 3)
    same("complete rounded derivative modulo K",
         dp.sub({T: 2 * a}) / 12 - I - FR, q * K)
    same("implicit q numerator", K.diff(A), 2 * (2 * a + m))
    same("implicit q denominator", K.diff(Q), 2 * (m + 2 * q))
    check("q derivative denominator positive",
          orthant_positive((m + 2 * q).sub({M: lo + m})))
    FRprime = m * (2 * a + 1 + 2 * m) + 2 * q * (2 * a + m)
    same("total FR derivative cross multiplication",
         (m + 2 * q) * (FR.diff(A) - FRprime) - (2 * a + m) * FR.diff(Q), 0)
    check("total FR derivative positive",
          orthant_positive(FRprime.sub({M: lo + m})))

    FRjoin = FR.sub({Q: a})
    join_form = (m * (F(1, 3) + F(3, 2) * m + m ** 2)
                 + m * a - 2 * m * a ** 2 - F(4, 3) * a ** 3)
    same("correct joining condition", K.sub({Q: a}), Ra - 2)
    same("join formula modulo R=2", FRjoin - join_form, m * (Ra - 2) / 2)
    same("all-diamond derivative matching",
         dp.sub({T: 2 * a}) - 12 * FRjoin, 12 * a * (Ra - 2))
    base_bound = m * (F(1, 3) + F(3, 2) * m + m ** 2)
    same("join nonnegative remainder", join_form - base_bound,
         m * a * (1 - 2 * a) - F(4, 3) * a ** 3)
    same("join parameter bound", value(base_bound, {M: lo}), F(131, 500))
    check("join base increases",
          orthant_positive(base_bound.diff(M).sub({M: lo + m})))
    same("join positive margin", F(131, 500) - F(1, 6), F(143, 1500))
    same("R-D", Ra - Da, 2 * a * (a + m))
    same("R(1/2)=Qstar", Ra.sub({A: F(1, 2)}), Qstar)
    interval_nonnegative("Qstar>2", Qstar - 2, M, lo, F(1, 2), True)
    interval_nonnegative("R(1/4)<2", 2 - Ra.sub({A: F(1, 4)}),
                         M, lo, F(1, 2), True)
    t2_certificate = interval_nonnegative("T2<=1 up to 1/2", 1 - T2,
                                         M, lo, F(1, 2))
    check("T2 strictly below one before endpoint", t2_certificate[0] > 0)

    physical = {M: F(2, 5), A: F(68, 125), Q: F(26, 125)}
    same("declared rounded K", value(K, physical), 0)
    same("declared rounded D", value(Da, physical), F(27298, 15625))
    same("declared rounded R", value(Ra, physical), F(43346, 15625))
    check("declared rounded branch",
          value(Da, physical) < 2 < value(Ra, physical)
          and 0 < physical[Q] < physical[A]
          and value(Qstar, {M: physical[M]}) > 2)
    same("declared q derivative",
         -value(2 * a + m, physical) / value(m + 2 * q, physical), F(-31, 17))
    same("declared FR", value(FR, physical), F(1293132, 1953125))
    same("declared FRprime", value(FRprime, physical), F(27722, 15625))
    root_point = {M: F(2, 5), Y: F(42, 125), R: F(94, 125)}
    same("declared joining root", value(droot, root_point), 0)
    check("declared free slope admissible",
          F(42, 125) / (F(94, 125) + F(2, 5)) == F(7, 24))
    join_point = {M: F(2, 5), A: F(2, 5), Q: F(2, 5)}
    same("declared R join", value(Ra, join_point), 2)
    same("declared D at R join", value(Da, join_point), F(34, 25))
    same("declared FR at join", value(FR, join_point), F(48, 125))

    # These are identity/logical mutants, not actual-regime existence checks.
    fixed = {M: F(2, 5), T: F(1, 2)}
    zfixed = value(Z, fixed)
    same("normalized sample area", zfixed, F(137, 50))
    reject("extra-1-minus-b-factor", F(5, 7) * zfixed, zfixed)
    C0 = F(2, 3) * t ** 4 - 4 * t ** 2
    same("telescoping deterministic baseline", value(C0, {T: F(1, 2)}), F(-23, 24))
    reject("drop-deterministic-baseline", N - 2 * Z - C0, N - 2 * Z)
    reject("reverse-penalty-sign", N + 2 * Z, N - 2 * Z)
    endpoints_positive = (
        value(quartic, {M: beta_lo, T: 0}) > 0
        and value(quartic, {M: beta_lo, T: 1}) > 0
    )
    witness_nonnegative = value(quartic, {M: beta_lo, T: F(2, 3)}) >= 0
    check("local-global mutant has positive endpoint trigger", endpoints_positive)
    reject("endpoint-or-local-check-is-global", endpoints_positive, witness_nonnegative)
    reject("use-D-equals-two-at-R-join", value(Da, join_point), F(2))
    zero_lower_residual = F(0)
    reject("include-lower-equality", zero_lower_residual >= 0, zero_lower_residual > 0)
    h2_at_v2 = -(F(2) - F(2)) * zfixed
    reject("force-strict-H2-at-V-equals-two", h2_at_v2 < 0, h2_at_v2 <= 0)
    reject("omit-rounded-improvement-derivative",
           value(dp.sub({T: 2 * a}) / 12, physical), value(FR, physical))
    deadline()
    print("ALL_LISTED_EXACT_PREDICATES_HOLD", CHECKS)
    print("NO_NUMERIC_BETA_COMPUTED")
    print("NOT_CERTIFIED: actual V, regime existence, radical integral evaluation, novelty")
    print("elapsed_seconds", monotonic() - START)

if __name__ == "__main__":
    main()
