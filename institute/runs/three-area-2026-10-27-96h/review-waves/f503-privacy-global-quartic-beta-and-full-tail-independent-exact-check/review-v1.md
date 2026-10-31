F503 FINITE — complete independent exact-check return

Execution status: NOTRUN.
Findings: none identified in the assigned algebraic scope.
Overall_correctness: correct.
Confidence: 0.90.

Explanation: The written reconstruction supports the stated necessary bounds and their different endpoint conventions, conditional on the named attainment and canonical-reduction imports. No computational verification was executed, so this return does not close the FINITE execution gate or authorize parent adoption.

1. Input and method receipt

Before opening the scientific body, I completely read:

• manifest-v1.json, LF 1–104.
• freeze-receipt-v1.json, LF 1–47.
• parent-dispatch-receipt-v1.json through its ending.
• parent-live-metadata-supply-v1.json through its ending.
• All ten listed permission/status controls, including their endings.

I then sent Main a direct pre-body ACK. Only afterward did I read literal-packet-v1.md in the ordered raw windows 1–20, 21–40, …, 501–520, 521–534. This included S1’s complete logical lines 1–471 and S2’s complete lines 1–61.

The following are supplied parent observations, not child-executed hashes, byte counts, or native start-time observations:

• Manifest SHA256: a22566919bf3fc37aa93e3c982c0744ad522ac7579aae6710c36d89ec860a35d.
• Receipt SHA256: 6cef666e3a8c719b8a19a1cc7e163ad39d65d0035ceab0ce61a4748bb6c8a446.
• Packet SHA256: 1f3cc8c4d9acb2b5e19bde4ae75193d619067452f7da08cd1f64d0ef870d4b7d.
• S1 SHA256: fc4423b5a7cb6fb9a1ba19ae35cf70145b9fab9034daf9da78af4e26aa3c1b11.
• S2 SHA256: 4179e3691a8050e64432044bfb928c273086537a3755fbd5b5d4f9c790af3330.
• Parent-supplied observation clock: 2026-10-30T12:27:04-0700 PDT.

I opened no linked author program, sibling scientific return, additional scientific source, or held payload. All held episodes and their consumers remain NONINPUT, including the privacy auxiliary episode and f439/f444/f448. The historical penalty-sign MAJOR remains permanent.

The higher-priority runtime restricts executable review activity. I therefore ran no scientific code, CAS, solver, build, test, numerical integration, or checksum command, and attempted no filesystem-write bypass. The exact-check program below is newly written source, not an executed result.

2. Written reconstruction of the finite algebra

2.1 Normalized geometric moments and lower bound

For the normalized geometric distribution, its probability-generating function is

\(H(z)=1/[1+m(1-z)]\).

Thus \(H(1)=1\) and the factorial moments are \(H^{(j)}(1)=j!m^j\). Conversion from factorial to ordinary moments gives exactly

\(T_2=m+2m^2\),

\(T_3=m+6m^2+6m^3\),

\(T_4=m+14m^2+36m^3+24m^4\).

Consequently, the supplied \(M_2(t)\) and \(M_4(t)\) formulas agree with the normalized law; another factor \(1-b\) outside these expectations would be erroneous.

At \(t=1/2\),

\(M_4(1/2)-\frac32M_2(1/2)=L(m)/16\).

The supplied rational signs are consistent:

\(L(7/100)=-350747/781250<0\),

\(L(3/40)=1523/20000>0\).

Since \(L'\) has strictly positive coefficients and positive constant term, the positive zero is unique. At \(m=\alpha\), the competitor quotient is exactly \(1/2\), which still contradicts the imported strict condition \(V>1/2\). The lower endpoint must therefore remain excluded.

2.2 Quartic and parameter certificate

Direct coefficient reconstruction gives \(P_m=M_4-6M_2\), with the stated first and second \(t\)-derivatives and the stated expansion around \(m=1/3\).

The critical-point bounds are consistent:

\(P'_m(0)\ge51/125>0\),

\(P'_m(1/2)\le-5/18<0\),

\(P'_m(1)\ge221/125>0\),

for \(3/10\le m\le1/3\). Together with \(P''_m(0)<0\) and strictly increasing \(P''_m(t)\) on \(t\ge0\), these establish the two-positive-critical-point classification used in S1.

At \(m=3/10\), all coefficients of \(\partial_mP_m(t)\) are strictly positive. The displayed \(\partial_m^2P_m(t)\) is also positive for \(m\ge3/10,\ t\ge0\). This is sufficient for strict parameter monotonicity on the whole half-line, not merely at a selected root.

The two Bernstein tables for \(W\) agree with affine power-to-Bernstein conversion. They yield \(W\ge17/4\) on \([0,1]\). The remaining upper-bracket bounds give exactly

\(P_{33/100}(t)\ge29977/6750000>0\), for \(0\le t\le1\).

At the lower bracket,

\(P_{13/40}(2/3)=-1508857/25920000<0\),

while

\(P_{13/40}(0)=28743/320000>0\).

Thus the implicit definition of \(\beta\), its prescribed bracket, and the global certificate follow from the written critical-point and monotonicity argument. No numerical approximation of \(\beta\) is supplied or needed.

An important distinction is preserved: positivity at endpoints alone is insufficient. In fact, at this same lower bracket,

\(P_{13/40}(1)=117183/320000>0\),

although \(P_{13/40}(2/3)<0\).

2.3 Complete rounded-core differentiation

Let

\(K=D(a)+2mq+2q^2-2\),

and let \(I=\int_0^{a-q}d(U,y)\,dy\), where \(U=2a-y\).

The following polynomial identities reconstruct the rounded derivative:

\(\psi(U,y)-\psi(r,y)- (U-r)^2[(U+2r)/3+m]=(U-r)d(r,y)\).

Hence the improvement formula is exact on the free-root equation \(d(r,y)=0\).

Also,

\(I=\frac83a^3+3ma^2+(T_2-2)a+mq^2+\frac43q^3-qK\).

The moving-endpoint term vanishes because the improvement is zero at the join. Differentiating the integral analytically therefore gives

\(e'_2(a)/16=P'_m(2a)/12-I=F_R(a)+qK\),

and hence the stated \(F_R\) on \(K=0\).

Implicit differentiation gives

\(q_a=-(2a+m)/(m+2q)\).

Substitution into the derivative of \(F_R\) gives precisely

\(F'_R=m(2a+1+2m)+2q(2a+m)>0\).

At \(q=a\), the correct joining equation is \(R(a)=2\), not \(D(a)=2\). The matching identities are

\(P'_m(2a)-12F_R(a,q=a)=12a(R(a)-2)\),

and

\(F_R(a,q=a)-[m(1/3+3m/2+m^2)+ma-2ma^2-4a^3/3]
=\frac m2(R(a)-2)\).

The endpoint lower bound is exactly

\(131/500-1/6=143/1500>0\).

These are polynomial and implicit-differentiation checks. The justification for differentiating the radical integral is analytical, using the smooth free-root branch and vanishing moving-endpoint term; it is not an exact numerical integration.

2.4 Declared rational rounded-branch instance

For the finite program’s explicit non-actual-\(V\) check, the declared inputs are

\(m=2/5,\quad a=68/125,\quad q=26/125,\quad\lambda=2\).

Written rational substitution gives

\(D(a)=27298/15625<2\),

\(R(a)=43346/15625>2\),

\(K=0,\quad0<q<a\).

The joining coordinates are \(y=42/125,\ r=94/125\), and \(d(r,y)=0\). The free-profile slope magnitude there is \(7/24<1\).

The corresponding algebraic values are

\(q_a=-31/17\),

\(F_R=1293132/1953125>0\),

\(F'_R=27722/15625>0\).

These are written substitutions, not observed program output. This parameter lies outside the necessary actual-attainment band; it is used only as a feasible fixed-scalar rounded-profile check, never as an actual cutoff-two optimizer.

3. Exact-check program — NOTRUN

The program uses only the Python standard library, exact Fraction coefficients, and sparse polynomial arithmetic. It reads and writes no files, uses no network or subprocesses, and has a cooperative 55-second deadline. It imports no author implementation.

Its deterministic-baseline mutation concerns the complete folded all-diamond functional’s exact telescoping baseline \(C_0(t)=2t^4/3-4t^2\). It does not claim to reconstruct a separately named upstream \(C(c;\lambda)\) formula absent from this packet.

The endpoint mutations are logical checks of the strict/non-strict implications, not existence tests at algebraic endpoints.

Complete argv:
argv[0]: python3
argv[1]: -B
argv[2]: -c
argv[3]: SOURCE, recovered exactly as described next.

SOURCE consists of every following line beginning “SRC|”, with precisely that four-character prefix removed, joined in order with LF and one final LF. The prefix is a transport label, not Python source.

SRC|from fractions import Fraction as F
SRC|from math import comb, factorial
SRC|from time import monotonic
SRC|
SRC|START = monotonic()
SRC|CHECKS = 0
SRC|NV = 7
SRC|ZERO = (0,) * NV
SRC|
SRC|class Failure(Exception):
SRC|    pass
SRC|
SRC|def deadline():
SRC|    if monotonic() - START > 55:
SRC|        raise Failure("cooperative 55-second deadline exceeded")
SRC|
SRC|def check(label, condition):
SRC|    global CHECKS
SRC|    deadline()
SRC|    if not condition:
SRC|        raise Failure(label)
SRC|    CHECKS += 1
SRC|
SRC|class P:
SRC|    def __init__(self, value=0):
SRC|        if isinstance(value, P):
SRC|            self.d = dict(value.d)
SRC|        elif isinstance(value, dict):
SRC|            self.d = {tuple(k): F(v) for k, v in value.items() if v}
SRC|        else:
SRC|            value = F(value)
SRC|            self.d = {} if not value else {ZERO: value}
SRC|
SRC|    def __add__(self, other):
SRC|        out = dict(self.d)
SRC|        for monomial, coefficient in P(other).d.items():
SRC|            value = out.get(monomial, F(0)) + coefficient
SRC|            if value:
SRC|                out[monomial] = value
SRC|            else:
SRC|                out.pop(monomial, None)
SRC|        return P(out)
SRC|
SRC|    __radd__ = __add__
SRC|
SRC|    def __neg__(self):
SRC|        return P({k: -v for k, v in self.d.items()})
SRC|
SRC|    def __sub__(self, other):
SRC|        return self + (-P(other))
SRC|
SRC|    def __rsub__(self, other):
SRC|        return P(other) + (-self)
SRC|
SRC|    def __mul__(self, other):
SRC|        deadline()
SRC|        out = {}
SRC|        for left, lc in self.d.items():
SRC|            for right, rc in P(other).d.items():
SRC|                monomial = tuple(x + y for x, y in zip(left, right))
SRC|                out[monomial] = out.get(monomial, F(0)) + lc * rc
SRC|        return P(out)
SRC|
SRC|    __rmul__ = __mul__
SRC|
SRC|    def __truediv__(self, scalar):
SRC|        return self * (F(1) / F(scalar))
SRC|
SRC|    def __pow__(self, exponent):
SRC|        if not isinstance(exponent, int) or exponent < 0:
SRC|            raise Failure("invalid polynomial exponent")
SRC|        result, base = P(1), self
SRC|        while exponent:
SRC|            deadline()
SRC|            if exponent & 1:
SRC|                result = result * base
SRC|            exponent //= 2
SRC|            if exponent:
SRC|                base = base * base
SRC|        return result
SRC|
SRC|    def __eq__(self, other):
SRC|        return self.d == P(other).d
SRC|
SRC|    def diff(self, index):
SRC|        out = {}
SRC|        for monomial, coefficient in self.d.items():
SRC|            exponent = monomial[index]
SRC|            if exponent:
SRC|                key = list(monomial)
SRC|                key[index] -= 1
SRC|                out[tuple(key)] = coefficient * exponent
SRC|        return P(out)
SRC|
SRC|    def sub(self, replacements):
SRC|        deadline()
SRC|        targets = {i: P(v) for i, v in replacements.items()}
SRC|        out = P(0)
SRC|        for monomial, coefficient in self.d.items():
SRC|            term = P(coefficient)
SRC|            for i, exponent in enumerate(monomial):
SRC|                if exponent:
SRC|                    term = term * targets.get(i, X[i]) ** exponent
SRC|            out = out + term
SRC|        return out
SRC|
SRC|    def scalar(self):
SRC|        if any(key != ZERO for key in self.d):
SRC|            raise Failure("scalar requested with unsubstituted variables")
SRC|        return self.d.get(ZERO, F(0))
SRC|
SRC|    def coefficients(self, index):
SRC|        for monomial in self.d:
SRC|            if any(e for i, e in enumerate(monomial) if i != index):
SRC|                raise Failure("univariate coefficients requested for multivariate input")
SRC|        degree = max((key[index] for key in self.d), default=0)
SRC|        out = [F(0)] * (degree + 1)
SRC|        for monomial, coefficient in self.d.items():
SRC|            out[monomial[index]] = coefficient
SRC|        return out
SRC|
SRC|X = []
SRC|for index in range(NV):
SRC|    key = [0] * NV
SRC|    key[index] = 1
SRC|    X.append(P({tuple(key): F(1)}))
SRC|M, T, U, A, Q, Y, R = range(NV)
SRC|m, t, u, a, q, y, r = X
SRC|
SRC|def same(label, left, right):
SRC|    check(label, P(left) == P(right))
SRC|
SRC|def value(poly, replacements):
SRC|    return P(poly).sub(replacements).scalar()
SRC|
SRC|def orthant_positive(poly):
SRC|    poly = P(poly)
SRC|    return poly.d.get(ZERO, F(0)) > 0 and all(c >= 0 for c in poly.d.values())
SRC|
SRC|def bernstein(poly, index, left, right):
SRC|    transformed = P(poly).sub({index: F(left) + (F(right) - F(left)) * X[index]})
SRC|    coefficients = transformed.coefficients(index)
SRC|    degree = len(coefficients) - 1
SRC|    return tuple(
SRC|        sum((coefficients[j] * F(comb(k, j), comb(degree, j))
SRC|             for j in range(k + 1)), F(0))
SRC|        for k in range(degree + 1)
SRC|    )
SRC|
SRC|def interval_nonnegative(label, poly, index, left, right, strict=False):
SRC|    coefficients = bernstein(poly, index, left, right)
SRC|    check(label, all(c > 0 if strict else c >= 0 for c in coefficients))
SRC|    print("BERNSTEIN", label, tuple(str(c) for c in coefficients))
SRC|    return coefficients
SRC|
SRC|def raw_moment(n):
SRC|    # Stirling conversion of factorial moments j! m^j.
SRC|    stirling = [0] * (n + 1)
SRC|    stirling[0] = 1
SRC|    for unused in range(n):
SRC|        stirling = [0] + [
SRC|            stirling[k - 1] + k * stirling[k] for k in range(1, n + 1)
SRC|        ]
SRC|    return sum((stirling[k] * factorial(k) * m ** k
SRC|                for k in range(n + 1)), P(0))
SRC|
SRC|def moment(n, shift):
SRC|    shift = P(shift)
SRC|    return sum((comb(n, j) * raw_moment(j) * shift ** (n - j)
SRC|                for j in range(n + 1)), P(0))
SRC|
SRC|def reject(name, wrong, reference):
SRC|    check("intended mutant differs: " + name, wrong != reference)
SRC|    print("REJECTED_MUTANT", name)
SRC|
SRC|def main():
SRC|    # H(z)=1/(1+m(1-z)); its denominator at z=1 is one.
SRC|    pgf_denominator = 1 + m - m * t
SRC|    same("normalized PGF", pgf_denominator.sub({T: 1}), 1)
SRC|    for order in range(1, 5):
SRC|        previous_numerator = factorial(order - 1) * m ** (order - 1)
SRC|        same("PGF factorial derivative " + str(order),
SRC|             -order * previous_numerator * pgf_denominator.diff(T),
SRC|             factorial(order) * m ** order)
SRC|
SRC|    T2 = m + 2 * m ** 2
SRC|    T3 = m + 6 * m ** 2 + 6 * m ** 3
SRC|    T4 = m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4
SRC|    same("raw moment zero", raw_moment(0), 1)
SRC|    same("raw moment one", raw_moment(1), m)
SRC|    same("raw moment two", raw_moment(2), T2)
SRC|    same("raw moment three", raw_moment(3), T3)
SRC|    same("raw moment four", raw_moment(4), T4)
SRC|    M2, M4 = moment(2, t), moment(4, t)
SRC|    same("shifted second moment", M2, t ** 2 + 2 * m * t + T2)
SRC|    same("shifted fourth moment", M4,
SRC|         t ** 4 + 4 * m * t ** 3 + 6 * T2 * t ** 2 + 4 * T3 * t + T4)
SRC|    Z, N = 2 * M2, F(2, 3) * M4
SRC|    L = 384 * m ** 4 + 768 * m ** 3 + 416 * m ** 2 + 32 * m - 5
SRC|    same("half-radius lower certificate",
SRC|         (M4 - F(3, 2) * M2).sub({T: F(1, 2)}), L / 16)
SRC|    check("L strictly increasing for nonnegative m", orthant_positive(L.diff(M)))
SRC|    same("L lower sign", value(L, {M: F(7, 100)}), F(-350747, 781250))
SRC|    same("L upper sign", value(L, {M: F(3, 40)}), F(1523, 20000))
SRC|
SRC|    quartic = (t ** 4 + 4 * m * t ** 3 + (6 * m + 12 * m ** 2 - 6) * t ** 2
SRC|               + (-8 * m + 24 * m ** 2 + 24 * m ** 3) * t
SRC|               + 24 * m ** 4 + 36 * m ** 3 + 2 * m ** 2 - 5 * m)
SRC|    same("P=M4-6M2", quartic, M4 - 6 * M2)
SRC|    same("complete signed all-diamond objective", N - 2 * Z, F(2, 3) * quartic)
SRC|    dp, ddp = quartic.diff(T), quartic.diff(T).diff(T)
SRC|    same("critical cubic", dp / 4,
SRC|         t ** 3 + 3 * m * t ** 2 + (3 * m + 6 * m ** 2 - 3) * t
SRC|         - 2 * m + 6 * m ** 2 + 6 * m ** 3)
SRC|    same("second t derivative", ddp, 12 * t ** 2 + 24 * m * t + 12 * (T2 - 1))
SRC|    lo, hi = F(3, 10), F(1, 3)
SRC|    interval_nonnegative("Pprime(0) lower bound",
SRC|                         dp.sub({T: 0}) - F(51, 125), M, lo, hi)
SRC|    interval_nonnegative("Pprime(1/2) upper bound",
SRC|                         -F(5, 18) - dp.sub({T: F(1, 2)}), M, lo, hi)
SRC|    interval_nonnegative("Pprime(1) lower bound",
SRC|                         dp.sub({T: 1}) - F(221, 125), M, lo, hi)
SRC|    interval_nonnegative("T2<1 on critical interval", 1 - T2, M, lo, hi, True)
SRC|    check("Psecond strictly increases on t>=0",
SRC|          orthant_positive(ddp.diff(T).sub({M: lo + m})))
SRC|
SRC|    dm = quartic.diff(M)
SRC|    same("parameter derivative at 3/10", dm.sub({M: lo}),
SRC|         4 * t ** 3 + F(66, 5) * t ** 2 + F(322, 25) * t + F(1064, 125))
SRC|    same("second parameter derivative", dm.diff(M),
SRC|         24 * t ** 2 + (48 + 144 * m) * t + 4 + 216 * m + 288 * m ** 2)
SRC|    check("parameter derivative positive at 3/10",
SRC|          orthant_positive(dm.sub({M: lo})))
SRC|    check("parameter derivative increases for m>=3/10",
SRC|          orthant_positive(dm.diff(M).sub({M: lo + m})))
SRC|
SRC|    W = 27 * t ** 4 + 36 * t ** 3 - 72 * t ** 2 + 24 * t + 5
SRC|    J = 4 * t ** 3 + 14 * t ** 2 + 16 * t + F(107, 9)
SRC|    B = 12 * t ** 2 + 48 * t + 54
SRC|    C = 24 * t + 68
SRC|    same("expansion about 1/3", quartic.sub({M: F(1, 3) + u}),
SRC|         W / 27 + u * J + u ** 2 * B + u ** 3 * C + 24 * u ** 4)
SRC|    check("first W Bernstein table",
SRC|          bernstein(W, T, 0, F(1, 2)) ==
SRC|          (F(5), F(8), F(8), F(49, 8), F(83, 16)))
SRC|    check("second W Bernstein table",
SRC|          bernstein(W, T, F(1, 2), 1) ==
SRC|          (F(83, 16), F(17, 4), F(17, 4), F(8), F(20)))
SRC|    interval_nonnegative("J upper bound", F(413, 9) - J, T, 0, 1)
SRC|    interval_nonnegative("C upper bound", 92 - C, T, 0, 1)
SRC|    check("B nonnegative on nonnegative t", all(c >= 0 for c in B.d.values()))
SRC|    upper_margin = F(17, 108) - F(413, 2700) - F(92, 27000000)
SRC|    same("upper bracket margin", upper_margin, F(29977, 6750000))
SRC|    check("upper bracket margin positive", upper_margin > 0)
SRC|    beta_lo, beta_hi = F(13, 40), F(33, 100)
SRC|    same("upper bracket displacement", beta_hi - F(1, 3), F(-1, 300))
SRC|    same("lower bracket negative witness",
SRC|         value(quartic, {M: beta_lo, T: F(2, 3)}), F(-1508857, 25920000))
SRC|    same("lower bracket origin positive",
SRC|         value(quartic, {M: beta_lo, T: 0}), F(28743, 320000))
SRC|    same("lower bracket other endpoint positive",
SRC|         value(quartic, {M: beta_lo, T: 1}), F(117183, 320000))
SRC|
SRC|    v = m * (1 + m)
SRC|    kappa = F(1, 3) + 2 * v
SRC|    Da = 2 * a ** 2 + 2 * m * a + T2
SRC|    Ra = 4 * a ** 2 + 4 * m * a + T2
SRC|    Qstar = 1 + 3 * m + 2 * m ** 2
SRC|    K = Da + 2 * m * q + 2 * q ** 2 - 2
SRC|    cap = 2 * a - y
SRC|    droot = r ** 2 + 2 * m * r + T2 + y ** 2 - 2
SRC|    same("free radical root equation", droot, (r + m) ** 2 + v + y ** 2 - 2)
SRC|    def psi(x):
SRC|        return x ** 3 / 3 + m * x ** 2 + (T2 + y ** 2 - 2) * x
SRC|    gain = (cap - r) ** 2 * ((cap + 2 * r) / 3 + m)
SRC|    same("cubic improvement identity", psi(cap) - psi(r) - gain, (cap - r) * droot)
SRC|    same("free-to-upper root relation", droot.sub({R: a + q, Y: a - q}), K)
SRC|    same("moving endpoint gain vanishes", gain.sub({R: a + q, Y: a - q}), 0)
SRC|
SRC|    dcap = cap ** 2 + 2 * m * cap + T2 + y ** 2 - 2
SRC|    primitive = ((4 * a ** 2 + 4 * m * a + T2 - 2) * y
SRC|                 - (2 * a + m) * y ** 2 + F(2, 3) * y ** 3)
SRC|    same("polynomial integral primitive", primitive.diff(Y), dcap)
SRC|    I = primitive.sub({Y: a - q})
SRC|    Itotal = F(8, 3) * a ** 3 + 3 * m * a ** 2 + (T2 - 2) * a
SRC|    same("rounded positive integral reduction",
SRC|         I - Itotal - m * q ** 2 - F(4, 3) * q ** 3, -q * K)
SRC|    FR = (m * (a ** 2 + (1 + 2 * m) * a + kappa - 1)
SRC|          - m * q ** 2 - F(4, 3) * q ** 3)
SRC|    same("complete rounded derivative modulo K",
SRC|         dp.sub({T: 2 * a}) / 12 - I - FR, q * K)
SRC|    same("implicit q numerator", K.diff(A), 2 * (2 * a + m))
SRC|    same("implicit q denominator", K.diff(Q), 2 * (m + 2 * q))
SRC|    check("q derivative denominator positive",
SRC|          orthant_positive((m + 2 * q).sub({M: lo + m})))
SRC|    FRprime = m * (2 * a + 1 + 2 * m) + 2 * q * (2 * a + m)
SRC|    same("total FR derivative cross multiplication",
SRC|         (m + 2 * q) * (FR.diff(A) - FRprime) - (2 * a + m) * FR.diff(Q), 0)
SRC|    check("total FR derivative positive",
SRC|          orthant_positive(FRprime.sub({M: lo + m})))
SRC|
SRC|    FRjoin = FR.sub({Q: a})
SRC|    join_form = (m * (F(1, 3) + F(3, 2) * m + m ** 2)
SRC|                 + m * a - 2 * m * a ** 2 - F(4, 3) * a ** 3)
SRC|    same("correct joining condition", K.sub({Q: a}), Ra - 2)
SRC|    same("join formula modulo R=2", FRjoin - join_form, m * (Ra - 2) / 2)
SRC|    same("all-diamond derivative matching",
SRC|         dp.sub({T: 2 * a}) - 12 * FRjoin, 12 * a * (Ra - 2))
SRC|    base_bound = m * (F(1, 3) + F(3, 2) * m + m ** 2)
SRC|    same("join nonnegative remainder", join_form - base_bound,
SRC|         m * a * (1 - 2 * a) - F(4, 3) * a ** 3)
SRC|    same("join parameter bound", value(base_bound, {M: lo}), F(131, 500))
SRC|    check("join base increases",
SRC|          orthant_positive(base_bound.diff(M).sub({M: lo + m})))
SRC|    same("join positive margin", F(131, 500) - F(1, 6), F(143, 1500))
SRC|    same("R-D", Ra - Da, 2 * a * (a + m))
SRC|    same("R(1/2)=Qstar", Ra.sub({A: F(1, 2)}), Qstar)
SRC|    interval_nonnegative("Qstar>2", Qstar - 2, M, lo, F(1, 2), True)
SRC|    interval_nonnegative("R(1/4)<2", 2 - Ra.sub({A: F(1, 4)}),
SRC|                         M, lo, F(1, 2), True)
SRC|    t2_certificate = interval_nonnegative("T2<=1 up to 1/2", 1 - T2,
SRC|                                         M, lo, F(1, 2))
SRC|    check("T2 strictly below one before endpoint", t2_certificate[0] > 0)
SRC|
SRC|    physical = {M: F(2, 5), A: F(68, 125), Q: F(26, 125)}
SRC|    same("declared rounded K", value(K, physical), 0)
SRC|    same("declared rounded D", value(Da, physical), F(27298, 15625))
SRC|    same("declared rounded R", value(Ra, physical), F(43346, 15625))
SRC|    check("declared rounded branch",
SRC|          value(Da, physical) < 2 < value(Ra, physical)
SRC|          and 0 < physical[Q] < physical[A]
SRC|          and value(Qstar, {M: physical[M]}) > 2)
SRC|    same("declared q derivative",
SRC|         -value(2 * a + m, physical) / value(m + 2 * q, physical), F(-31, 17))
SRC|    same("declared FR", value(FR, physical), F(1293132, 1953125))
SRC|    same("declared FRprime", value(FRprime, physical), F(27722, 15625))
SRC|    root_point = {M: F(2, 5), Y: F(42, 125), R: F(94, 125)}
SRC|    same("declared joining root", value(droot, root_point), 0)
SRC|    check("declared free slope admissible",
SRC|          F(42, 125) / (F(94, 125) + F(2, 5)) == F(7, 24))
SRC|    join_point = {M: F(2, 5), A: F(2, 5), Q: F(2, 5)}
SRC|    same("declared R join", value(Ra, join_point), 2)
SRC|    same("declared D at R join", value(Da, join_point), F(34, 25))
SRC|    same("declared FR at join", value(FR, join_point), F(48, 125))
SRC|
SRC|    # These are identity/logical mutants, not actual-regime existence checks.
SRC|    fixed = {M: F(2, 5), T: F(1, 2)}
SRC|    zfixed = value(Z, fixed)
SRC|    same("normalized sample area", zfixed, F(137, 50))
SRC|    reject("extra-1-minus-b-factor", F(5, 7) * zfixed, zfixed)
SRC|    C0 = F(2, 3) * t ** 4 - 4 * t ** 2
SRC|    same("telescoping deterministic baseline", value(C0, {T: F(1, 2)}), F(-23, 24))
SRC|    reject("drop-deterministic-baseline", N - 2 * Z - C0, N - 2 * Z)
SRC|    reject("reverse-penalty-sign", N + 2 * Z, N - 2 * Z)
SRC|    endpoints_positive = (
SRC|        value(quartic, {M: beta_lo, T: 0}) > 0
SRC|        and value(quartic, {M: beta_lo, T: 1}) > 0
SRC|    )
SRC|    witness_nonnegative = value(quartic, {M: beta_lo, T: F(2, 3)}) >= 0
SRC|    check("local-global mutant has positive endpoint trigger", endpoints_positive)
SRC|    reject("endpoint-or-local-check-is-global", endpoints_positive, witness_nonnegative)
SRC|    reject("use-D-equals-two-at-R-join", value(Da, join_point), F(2))
SRC|    zero_lower_residual = F(0)
SRC|    reject("include-lower-equality", zero_lower_residual >= 0, zero_lower_residual > 0)
SRC|    h2_at_v2 = -(F(2) - F(2)) * zfixed
SRC|    reject("force-strict-H2-at-V-equals-two", h2_at_v2 < 0, h2_at_v2 <= 0)
SRC|    reject("omit-rounded-improvement-derivative",
SRC|           value(dp.sub({T: 2 * a}) / 12, physical), value(FR, physical))
SRC|    deadline()
SRC|    print("ALL_LISTED_EXACT_PREDICATES_HOLD", CHECKS)
SRC|    print("NO_NUMERIC_BETA_COMPUTED")
SRC|    print("NOT_CERTIFIED: actual V, regime existence, radical integral evaluation, novelty")
SRC|    print("elapsed_seconds", monotonic() - START)
SRC|
SRC|if __name__ == "__main__":
SRC|    main()

4. Execution results and disposition limits

Observed execution results: none. The program has not been run. There is no observed exit code, predicate count, elapsed time, mutation-rejection output, or source-file hash to report.

The exact rational results in section 2 are written reconstruction, explicitly distinguished from execution. The source’s prospective output strings are not evidence that those outputs occurred.

The assigned finite algebra is consistent with the candidate’s conclusion:

\(\alpha<m\le\beta\),

with lower equality excluded by the feasible competitor and upper equality not excluded by \(H_2=-(2-V)Z\le0\). Conditional upper-endpoint attainment would require \(V=2\) and the stated strictly all-upper core; no such attainment is established here.

Remaining boundaries are unchanged: this return does not prove actual cutoff-two existence anywhere, sufficiency of the necessary band, the actual global value, an all-parameter integral theorem, original-source equivalence, novelty, independent-family review, human verification, or formal-kernel acceptance. Parent execution of the complete source and the separate written gates remain necessary before any FINITE-verified disposition.