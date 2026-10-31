from fractions import Fraction as R
from math import comb
from time import monotonic

started = monotonic()
deadline = started + 50

class CheckFailure(Exception):
    pass

def tick():
    if monotonic() > deadline:
        raise CheckFailure("calculation budget exhausted; no completed receipt")

NAMES = ("a", "c", "m", "L", "y", "ell", "q", "z", "r", "t")
INDEX = {name: i for i, name in enumerate(NAMES)}
ZERO = (0,) * len(NAMES)

class P:
    def __init__(self, value=0):
        tick()
        if isinstance(value, P):
            self.c = value.c.copy()
        elif isinstance(value, dict):
            self.c = {e: R(v) for e, v in value.items() if v}
        else:
            self.c = {} if not value else {ZERO: R(value)}

    def __add__(self, other):
        out = self.c.copy()
        for e, v in P(other).c.items():
            out[e] = out.get(e, R(0)) + v
            if not out[e]:
                del out[e]
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -v for e, v in self.c.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        out = {}
        other = P(other)
        for e, v in self.c.items():
            tick()
            for f, w in other.c.items():
                g = tuple(x + y for x, y in zip(e, f))
                out[g] = out.get(g, R(0)) + v * w
        return P(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = R(scalar)
        if not scalar:
            raise CheckFailure("division by zero")
        return P({e: v / scalar for e, v in self.c.items()})

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise CheckFailure("non-polynomial exponent")
        out = P(1)
        for unused in range(exponent):
            out = out * self
        return out

    def d(self, name):
        j = INDEX[name]
        out = {}
        for e, v in self.c.items():
            if e[j]:
                f = list(e)
                f[j] -= 1
                out[tuple(f)] = v * e[j]
        return P(out)

    def anti(self, name):
        j = INDEX[name]
        out = {}
        for e, v in self.c.items():
            f = list(e)
            f[j] += 1
            out[tuple(f)] = v / f[j]
        return P(out)

    def sub(self, name, replacement):
        j = INDEX[name]
        replacement = P(replacement)
        out = P()
        for e, v in self.c.items():
            f = list(e)
            power = f[j]
            f[j] = 0
            out = out + P({tuple(f): v}) * replacement ** power
        return out

    def scalar(self):
        if any(e != ZERO for e in self.c):
            raise CheckFailure("nonconstant used as rational number")
        return self.c.get(ZERO, R(0))

def variable(name):
    e = list(ZERO)
    e[INDEX[name]] = 1
    return P({tuple(e): R(1)})

a, c, m, L, y, ell, q, z, r, t = [variable(n) for n in NAMES]
checks = 0
mutations = 0

def need(name, condition):
    global checks
    tick()
    if not condition:
        raise CheckFailure(name)
    checks += 1

def eq(name, left, right=0):
    need(name, P(left).c == P(right).c)

def reject_eq(name, mutated, reference, reason):
    global mutations
    need("mutation survived: " + name, P(mutated).c != P(reference).c)
    mutations += 1
    print("MUTANT_REJECT", name, reason)

def reject_accept(name, mutated_accepts, correct_accepts, reason):
    global mutations
    need("mutation not discriminated: " + name,
         mutated_accepts and not correct_accepts)
    mutations += 1
    print("MUTANT_REJECT", name, reason)

def I(f, lo, hi):
    primitive = P(f).anti("y")
    return primitive.sub("y", hi) - primitive.sub("y", lo)

def positive_coefficients(f):
    f = P(f)
    return bool(f.c) and all(v > 0 for v in f.c.values())

T = [P(1)]
for n in range(1, 5):
    T.append(m * sum((comb(n, j) * T[j] for j in range(n)), P()))
T2, T3, T4 = T[2], T[3], T[4]
v = m * (1 + m)
kappa = R(1, 3) + 2 * v
eq("derived T2", T2, m + 2 * m ** 2)
eq("derived T3", T3, m + 6 * m ** 2 + 6 * m ** 3)
eq("derived T4", T4, m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4)

def area_density(x):
    return x - y

def moment_density(x):
    return x ** 3 / 3 + y ** 2 * x - 4 * y ** 3 / 3

def boundary_density(x):
    return x ** 2 + y ** 2

def psi0(x):
    return moment_density(x) - L * area_density(x)

def psi1(x):
    return psi0(x) + m * boundary_density(x) + T2 * x

C = (8 * c ** 2 * T2 + 16 * c * T3 / 3 + 2 * T4 / 3
     - L * (8 * c * m + 2 * T2) - 8 * T2 * I(y, 0, c))
eq("deterministic constant from raw functional", C,
   4 * c ** 2 * T2 + 16 * c * T3 / 3 + 2 * T4 / 3
   - L * (8 * c * m + 2 * T2))

dz = psi1(z).d("z")
def dcoord(x):
    return dz.sub("z", x)

eq("coordinate derivative from densities", dz,
   (z + m) ** 2 + v + y ** 2 - L)
eq("active core pooling", psi0(z) + m * psi1(z + 1),
   (1 + m) * psi1(z) + m * (kappa - L))
eq("first-core diagonal endpoint", psi0(a).sub("y", a))

def geometric_integrals(f, lo, hi):
    return (8 * I(area_density(f), lo, hi),
            8 * I(moment_density(f), lo, hi),
            8 * I(boundary_density(f), lo, hi))

def raw_parts(f0, tails):
    A0, Q0, unused = geometric_integrals(f0, 0, a)
    A1, Q1, B1 = geometric_integrals(f0 + 1, 0, a)
    for f, lo, hi in tails:
        aa, qq, bb = geometric_integrals(f, lo, hi)
        A1, Q1, B1 = A1 + aa, Q1 + qq, B1 + bb
    first = Q0 - L * A0
    tail = (Q1 + m * B1 + (A1 + 8 * c ** 2) * T2
            + 16 * c * T3 / 3 + 2 * T4 / 3
            - L * (A1 + 8 * c * m + 2 * T2))
    return first, tail

def raw_value(f0, tails):
    first, tail = raw_parts(f0, tails)
    return first + m * tail

def signed_value(f0, tails):
    tail_integral = I(psi1(f0 + 1), 0, a)
    for f, lo, hi in tails:
        tail_integral = tail_integral + I(psi1(f), lo, hi)
    return 8 * I(psi0(f0), 0, a) + 8 * m * tail_integral + m * C

U = 2 * a - y
k = 2 * a + 1 - y
s = 2 * a + 1 - c
u = a + R(1, 2)
tails = [(k, a, s), (c, s, c)]
endpoint = psi1(c).sub("y", c)
D0 = endpoint + C.d("c") / 8
eq("moving diagonal endpoint", endpoint, 2 * m * c ** 2 + T2 * c)
eq("complete D0", D0,
   2 * c * T2 + 2 * m * c ** 2 + 2 * T3 / 3 - m * L)
eq("tail interface joins", k.sub("y", s), c)

affine = {}
for label, f0 in (("lower", a), ("upper", U)):
    H = raw_value(f0, tails)
    affine[label] = H
    eq(label + " complete functional", H, signed_value(f0, tails))
    da_shape = (8 * (1 + m) * I(dcoord(f0) * f0.d("a"), 0, a)
                + 16 * m * I(dcoord(k), a, s))
    dc_shape = 8 * m * (D0 + I(dcoord(c), s, c))
    eq(label + " raw a derivative", H.d("a"), da_shape)
    eq(label + " raw c derivative", H.d("c"), dc_shape)

def edge_value(f0):
    return raw_value(f0, [(k, a, c)]).sub("c", u)

Eupper = edge_value(U)
Elower = edge_value(a)
Aupper = -I(dcoord(U), 0, a)
Llower = I(dcoord(a), 0, a)
W = a ** 2 + (1 + 2 * m) * a + kappa - L / 2
eq("edge endpoint-and-corner simplification",
   I(dcoord(k), a, u) + D0.sub("c", u) / 2, (1 + m) * W)
eq("upper edge derivative from complete raw value",
   Eupper.d("a"), 16 * (1 + m) * (m * W - Aupper))
eq("lower edge derivative from complete raw value",
   Elower.d("a"), 16 * (1 + m) * (m * W + Llower / 2))
eq("all-upper A", Aupper,
   a * (L - T2) - 3 * m * a ** 2 - 8 * a ** 3 / 3)
G = 8 * a ** 3 / 3 + 4 * m * a ** 2 + (2 * T2 - L) * a
G = G + m * (kappa - L / 2)
eq("upper F from raw derivative", m * W - Aupper, G)
eq("upper F first derivative", G.d("a"),
   8 * a ** 2 + 8 * m * a + 2 * T2 - L)
eq("upper F second derivative", G.d("a").d("a"), 16 * a + 8 * m)

def D(x):
    return 2 * x ** 2 + 2 * m * x + T2

def Rfront(x):
    return 4 * x ** 2 + 4 * m * x + T2

Braw = I(dcoord(k), a, a + ell)
lambda_ell = dcoord(k).sub("y", a + ell) + L
Broot = Braw.sub("L", lambda_ell)
eq("corner B after implicit root constraint", Broot,
   (1 + m) * ell ** 2 - 4 * ell ** 3 / 3)
Ba = Braw.d("a").sub("L", lambda_ell)
eq("corner B_a from unsimplified integral", Ba, 2 * (2 * a + 1 + m) * ell)
eq("corner implicit derivative consistency",
   Broot.d("ell") * (2 * a + 1 + m),
   (1 + m - 2 * ell) * Ba)
curvature = -(1 + m) * Aupper.d("a") + m * Ba
eq("normalized h_aa algebra", curvature,
   (1 + m) * (-L + T2 + 6 * m * a + 8 * a ** 2)
   + 2 * m * (2 * a + 1 + m) * ell)
bound = curvature.sub("L", D(u)).sub("ell", R(1, 2))
eq("curvature bound after strict endpoint replacements", bound,
   (1 + m) * (6 * a ** 2 + (4 * m - 2) * a - R(1, 2))
   + 2 * m * a)
need("negative curvature rational bound",
     R(6, 64) + R(1, 12) - R(1, 2) == -R(31, 96))

lambda_q = D(a) + 2 * m * q + 2 * q ** 2
Aq = (-I(dcoord(U), a - q, a)).sub("L", lambda_q)
eq("free-branch A from integration", Aq, m * q ** 2 + 4 * q ** 3 / 3)
Ffree = m * W - Aq
Fa_free = m * (2 * a + 1 + 2 * m) + 2 * q * (2 * a + m)
eq("free F derivative under fixed-lambda implicit constraint",
   (2 * q + m) * Ffree.d("a") - (2 * a + m) * Ffree.d("q"),
   (2 * q + m) * Fa_free)
need("free F_a positive for positive a,m,q", positive_coefficients(Fa_free))
eq("branch values match",
   Ffree.sub("q", a).sub("L", Rfront(a)), G.sub("L", Rfront(a)))
eq("free derivative at branch frontier", Fa_free.sub("q", a), Rfront(a))
eq("upper derivative at branch frontier",
   G.d("a").sub("L", Rfront(a)), Rfront(a))
missing_branch_gap = (Ffree - G).sub("L", lambda_q)
eq("exact missing-free-branch error", missing_branch_gap,
   -(a - q) ** 2 * (m + 2 * a / 3 + 4 * q / 3))

eq("full rounded-core cubic identity",
   psi1(z) - psi1(r),
   (z - r) * dcoord(r) + (z - r) ** 2 * ((z + 2 * r) / 3 + m))

def M(n, shift):
    return sum((comb(n, j) * P(shift) ** (n - j) * T[j]
                for j in range(n + 1)), P())

for n in range(5):
    eq("memoryless shifted moment " + str(n),
       (1 + m) * M(n, t), t ** n + m * M(n, t + 1))
eq("complete diamond value from raw area and moments", Eupper,
   (1 + m) * (2 * M(4, 2 * a) / 3 - 2 * L * M(2, 2 * a)))

m0 = R(1, 10)
MM = [M(n, t).sub("m", m0) for n in range(5)]
Pexpr = 2 * MM[3] * MM[2] - MM[4] * MM[1]
p = 250 * Pexpr
eq("prescribed quintic derived from moment products", p,
   250 * t ** 5 + 125 * t ** 4 + 80 * t ** 3 - 47 * t ** 2 - 48 * t + 3)

def value(f, at):
    return P(f).sub("t", at).scalar()

lo, hi, half = R(11, 20), R(3, 5), R(1, 2)
need("quintic lower endpoint", value(p, lo) == -R(147, 512))
need("quintic upper endpoint", value(p, hi) == R(51, 5))
need("quintic derivative at half", value(p.d("t"), half) == R(845, 8))
shifted_second = p.d("t").d("t").sub("t", half + t)
eq("shifted second derivative", shifted_second,
   1146 + 5730 * t + 9000 * t ** 2 + 5000 * t ** 3)
need("second derivative positive at and above half",
     positive_coefficients(shifted_second))
need("third derivative positive on nonnegative axis",
     positive_coefficients(p.d("t").d("t").d("t")))
need("initial signs for unique positive turning point",
     value(p, 0) > 0 and value(p.d("t"), 0) < 0
     and value(p.d("t").d("t"), 0) < 0)

Ht = Eupper.sub("a", t / 2).sub("m", m0)
St = Eupper.d("a").sub("a", t / 2).sub("m", m0)
eq("diamond value is affine in lambda", Ht.d("L").d("L"))
eq("exact full value zero after cross multiplication",
   3 * MM[2] * Ht.sub("L", 0) + MM[4] * Ht.d("L"))
eq("stationarity numerator is precisely elimination polynomial",
   3 * MM[2] * St.sub("L", 0) + MM[4] * St.d("L"),
   8 * (1 + m0) * Pexpr)
eq("root-orientation curvature identity", p.d("t"),
   250 * (6 * MM[2] ** 2 - MM[4]))
need("positive moment denominators", positive_coefficients(MM[1])
     and positive_coefficients(MM[2]))

lower_value = value(MM[4], lo) / (3 * value(MM[2], hi))
upper_value = value(MM[4], hi) / (3 * value(MM[2], lo))
need("exact lower value bound",
     lower_value == R(54371, 96000) and lower_value > R(5, 9))
need("exact upper value bound",
     upper_value == R(256, 355) and upper_value < R(3, 4))
branch_gap = 2 * MM[3] - 3 * MM[1] * MM[2]
eq("diamond clipping inequality numerator", branch_gap,
   -t ** 3 - 3 * t ** 2 / 10 + 3 * t / 10 + R(37, 125))
need("clipping numerator decreases on assigned interval",
     positive_coefficients(-branch_gap.d("t").sub("t", lo + t)))
need("clipping numerator stays strictly positive",
     value(branch_gap, hi) == R(19, 125))
need("positive candidate edge curvature bound",
     2 * lo ** 2 + R(2, 5) * lo + R(6, 25) == R(213, 200)
     and R(213, 200) - R(3, 4) == R(63, 200))
need("strict candidate normal separation",
     2 * R(31, 40) ** 2 == R(961, 800) and R(961, 800) > 1
     and upper_value < 1)
v0 = m0 * (1 + m0)
w0 = v0 * (1 + 2 * m0)
need("assigned lower value exceeds stronger necessary threshold",
     R(5, 9) - 2 * v0 > 0
     and (R(5, 9) - 2 * v0) ** 3 - 2 * w0 ** 2
     == R(267427, 91125000))

def udict(f):
    out = {}
    for e, coef in P(f).c.items():
        if any(power for j, power in enumerate(e) if j != INDEX["t"]):
            raise CheckFailure("Sturm input is not univariate in t")
        out[e[INDEX["t"]]] = coef
    return out

def upoly(coefficients):
    return sum((coef * t ** degree for degree, coef in coefficients.items()), P())

def remainder(numerator, denominator):
    work = udict(numerator)
    den = udict(denominator)
    if not den:
        raise CheckFailure("zero Sturm divisor")
    degree_den = max(den)
    while work and max(work) >= degree_den:
        tick()
        degree_work = max(work)
        shift = degree_work - degree_den
        factor = work[degree_work] / den[degree_den]
        for degree, coef in den.items():
            key = degree + shift
            new_value = work.get(key, R(0)) - factor * coef
            if new_value:
                work[key] = new_value
            else:
                work.pop(key, None)
    return upoly(work)

def sturm_chain(f):
    chain = [f, f.d("t")]
    while chain[-1].c:
        rem = remainder(chain[-2], chain[-1])
        if not rem.c:
            break
        chain.append(-rem)
    return chain

def sign(number):
    return (number > 0) - (number < 0)

def variations(signs):
    signs = [s for s in signs if s]
    return sum(left * right < 0 for left, right in zip(signs, signs[1:]))

chain = sturm_chain(p)
need("quintic squarefree", max(udict(chain[-1])) == 0)

def variation_at(at):
    return variations([sign(value(f, at)) for f in chain])

def roots_between(left, right):
    return variation_at(left) - variation_at(right)

def root_only_accepts(left, right):
    return roots_between(left, right) == 1

def minimum_root_accepts(left, right):
    return (root_only_accepts(left, right)
            and value(p, left) < 0 < value(p, right))

variation_infinity = variations([
    sign(udict(f)[max(udict(f))]) for f in chain
])
need("exactly two positive quintic roots",
     variation_at(0) - variation_infinity == 2)
need("one earlier decreasing root", roots_between(0, lo) == 1)
need("one assigned increasing root", roots_between(lo, hi) == 1)
need("assigned root passes orientation gate", minimum_root_accepts(lo, hi))

H = affine["upper"]
first, tail = raw_parts(U, tails)
reject_eq("omit-b", first + (1 + m) * tail, H,
          "geometric mixture coefficient becomes 1 rather than b")
reject_eq("omit-tail-constant", H - m * C, H,
          "complete deterministic geometric-tail contribution is lost")
reject_eq("omit-moving-endpoint", H.d("c") - 8 * m * endpoint, H.d("c"),
          "terminal-height derivative 8*m*psi1(c,c) is missing")
reject_eq("omit-active-core-offset", H - 8 * m * a * (kappa - L), H,
          "required active-core pooling offset is missing")
normal = H.d("c").sub("c", u)
eq("edge normal on positive-gradient affine stratum", normal,
   8 * m * D0.sub("c", u))
reject_eq("flip-normal", -normal, normal,
          "right derivative has the opposite normal orientation")
reject_eq("omit-free-branch",
          Ffree.sub("L", lambda_q), G.sub("L", lambda_q),
          "nonzero -(a-q)^2*(m+2*a/3+4*q/3) discrepancy")
reject_accept("decreasing-root-as-minimum",
              root_only_accepts(0, lo), minimum_root_accepts(0, lo),
              "full value and stationarity do not replace positive curvature")

need("all seven intended mutation classes discriminated", mutations == 7)
need("finite execution bound", monotonic() - started < 55)
print("ENDPOINTS", value(p, lo), value(p, hi))
print("VALUE_BOUNDS", lower_value, upper_value)
print("ASSERTIONS", checks, "INTENDED_MUTATION_CLASSES", mutations)
print("SCOPE exact finite algebra; assigned synthetic candidate only")
print("LIMIT not a continuum proof, actual-regime existence, or adoption")
print("ELAPSED_SECONDS", monotonic() - started)
