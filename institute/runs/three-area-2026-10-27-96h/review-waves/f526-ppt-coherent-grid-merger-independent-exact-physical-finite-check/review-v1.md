# author-candidate-v1.md — f526 independent exact physical check

**Status: written algebra checked; executable verification NOT RUN.**

The frozen manuscript’s coherent-merger claim is supported by the written checks below. I found no mathematical defect in its stated family. This return includes a complete, independent standard-library checker and eight targeted mutation controls, but **none was executed**: the runtime expressly prohibits scientific execution and file edits. There is no claimed stdout, elapsed runtime, machine-verified PSD result, or passed mutation control.

## 1. Input binding and chronology

Before opening the mathematical body, I read:

- Complete manifest, LF 1–97.
- Complete freeze receipt, LF 1–34.
- All ten listed permission/status controls, including every ending.
- Parent metadata supply and dispatch receipt.

I then sent the direct pre-body ACK and read the **entire literal packet, LF 1–591, consecutively in raw chunks of at most 20 LF**, including the ending. That packet contains the complete S1 manuscript, source lines 1–589.

Parent-supplied bindings:

- Manifest: `9501732fbabe5b5717068f782a56f3dad56a63377d798dfadfe715e7db1b13ed`
- Receipt: `4127792e82e5d540a3339607ab800689b39cebad2297666ead1027fa63ccf86d`
- Packet: `9336603d419f2efbceaae9904444d01856563112825a029e7fb84fcb3388575b`
- S1 manuscript: `85d63cbec7a7115066565abba8b789e4873667fac7a247950f6b26accc4049cd`

These are **parent observations, not hashes recomputed by this reviewer**.

No held mathematical payload or consumer, sibling return, additional scientific source, or author implementation was opened. The manuscript’s public citation was not followed. A permitted, path-scoped `git diff` returned no output; this is therefore a review of the frozen manuscript, not an assertion about a nonempty Git patch.

## 2. Independent written checks

### Physical operator, filter and normalization

Writing \(d=s|v|^2+r|u|^2\), summing projector traces gives

\[
\operatorname{Tr}R=7+2(s+r)+2d.
\]

Directly applying the declared Bob map to each projector in \(Q\) gives exactly \(R\). In particular, the two extension coherences become those in \(E_u\) and \(F_v\); the core terms are retained, not discarded.

Furthermore,

\[
KK^\dagger=\operatorname{diag}(1,1,1,|u|^2+|v|^2).
\]

Thus \(K/\sqrt m\) is a contraction for

\[
m=\max(1,|u|^2+|v|^2),
\]

and its success probability on normalized \(Q\) is

\[
p=\frac{7+2(s+r)+2d}{m\,[7+4(s+r)]}.
\]

The normalized output remains \(R/\operatorname{Tr}R\).

The stated marginals follow by tracing the projector entries:

\[
R_A=\operatorname{diag}
(2+s+s|v|^2,\ 3,\ 2+r+r|u|^2,\ s+r+d),
\]

\[
R_B=\operatorname{diag}(2+2r,\ 3,\ 2+2s,\ 2d).
\]

Consequently both local supports are four-dimensional exactly when \((u,v)\ne(0,0)\); when both vanish, Bob’s fourth marginal entry is zero.

### Bob partial transpose and exact PPT region

The extension off-diagonal entry from \(E_u\) becomes

\[
r\bar u\,|23\rangle\langle30|,
\]

so its block is \(r[\bar u\,23+30]\), with the conjugate on the indicated coefficient. The \(v\) block behaves identically.

All other nontrivial signs reduce to the displayed central block

\[
M=
\begin{pmatrix}s&1&1\\1&1&-1\\1&-1&r\end{pmatrix}.
\]

Eliminating its middle entry gives

\[
\begin{pmatrix}s-1&2\\2&r-1\end{pmatrix}.
\]

Its PSD condition is exactly

\[
s>1,\qquad r>1,\qquad (s-1)(r-1)\ge4,
\]

including equality. The manuscript’s rank-one expansion of \(M\) reproduces all six off-diagonal entries and all three diagonal entries.

### Rank-two vectors and root averaging

For the manuscript’s \(4\times4\) coefficient matrix, the relations

\[
C_2=z^{-1}C_1,\qquad
C_3=\alpha w C_0+\alpha zw C_1
\]

hold entry by entry, including the complex \(v\) entry. They establish rank at most two without restricting vectors to be real.

The seven character classes in \(C_4\times C_3\) are

\[
(1,0),(0,0),(2,0),(3,0),(1,1),(3,1),(3,2).
\]

They are pairwise distinct. Character averaging therefore retains precisely the four original projector bundles and the three stated filler projectors. In particular, the third-root factor cannot simply be replaced by a second-root factor: the \(|23\rangle\) and \(|30\rangle\) characters would then coincide.

The reflected construction has the stated signs: \(L F_{-u}=-E_u\), while projector signs disappear. It therefore yields the stated \(H\) identity and preserves Schmidt rank.

### Exhaustive remainder signs

The split must be squared consistently:

\[
|v|\le r|u|
\quad\Longleftrightarrow\quad
|v|^2\le r^2|u|^2.
\]

- For \(v=0\), the four-root core average and the displayed remainder are valid.
- In Case 2, \(\alpha^2=|v|^2/r\) cancels the \([30]\) coefficient. The remaining nontrivial coefficients are
  \[
  |v|^2(s-4/r),\qquad r|u|^2-|v|^2/r,
  \]
  both nonnegative under the PPT and case hypotheses.
- In Case 3, \(\alpha^2=1/(sr^2)\) gives exactly the manuscript’s four filler coefficients. The case inequality handles \([03]\); \(sr\ge9\) and \(r>1\) handle the remaining signs.

These cases exhaust all complex \(u,v\), including both zero cases.

### Entanglement and the parent’s Schmidt number

The compressed core’s two indicated rank-one minors imply \(2a^2=0\), hence \(a=0\) over \(\mathbb C\). The range-support argument for positive decompositions is valid, and the nonzero \(|00\rangle\) diagonal supplies the contradiction to separability.

For the parent \(Q\), the five stated minors have the stated index sets and signs. Their combination satisfies

\[
g_5-g_3-g_4=a^3+ace,\qquad
\frac12(cg_1+eg_2)=a^2ce,
\]

hence

\[
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
\]

Rank at most two therefore forces \(a=0\). The same positive-range argument excludes any Schmidt-rank-at-most-two decomposition of \(Q\), while its defining projector decomposition has maximum rank three.

These are **written logical arguments**, not conclusions established by selected numerical matrices.

### Assigned physical example

For the manuscript-assigned \(s=r=3,\ u=v=1\):

\[
\operatorname{Tr}R=\operatorname{Tr}Q=31,
\qquad
R_A=R_B=\operatorname{diag}(8,3,8,12).
\]

The central PPT residual vanishes, and the stated remainder coefficients are \(2,3,5/3,8/3,3\). Since \(KK^\dagger=\operatorname{diag}(1,1,1,2)\), the whole contraction is \(K/\sqrt2\); its success probability is exactly \(1/2\).

## 3. Complete prospective checker — NOT RUN

The following source uses only Gaussian rationals, exact sparse polynomial/character algebra, direct matrix operations and exact LDL decompositions. No floating-point roots or approximate PSD tests are used.

Its declared positive cases cover the assigned boundary example, complex coefficients with both coherences active, Cases 2 and 3, either coefficient zero, both zero, another PPT boundary and an interior PPT point. It also includes positive-parameter points outside the PPT region.

Eight intended-reason mutation controls cover:

1. Wrong partial-transpose leg.
2. Missing conjugation in the extension blocks.
3. Wrong rank-two phase.
4. Wrong root order.
5. \(r\) versus \(r^2\) in the case split.
6. Negative filler weight.
7. A false SN3-detector claim.
8. Dropping the core of the whole physical filter.

**All finite cases and all mutation outcomes remain NOT RUN.** The source has a 54-second cooperative computation deadline; actual runtime has not been measured.

Exact prospective argv:

- argv[0]: `python3`
- argv[1]: `-B`
- argv[2]: `-c`
- argv[3]: the complete literal source between SOURCE BEGIN and SOURCE END.

SOURCE BEGIN
from fractions import Fraction as F
from itertools import combinations, permutations
from time import monotonic

START = monotonic()
DEADLINE = START + 54.0

class CheckFailure(Exception):
    pass

def guard():
    if monotonic() >= DEADLINE:
        raise TimeoutError("cooperative deadline")

def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)

class C:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, other):
        other = cc(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-cc(other))

    def __rsub__(self, other):
        return cc(other) - self

    def __mul__(self, other):
        other = cc(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = cc(other)
        denominator = other.re * other.re + other.im * other.im
        if denominator == 0:
            raise ZeroDivisionError("Gaussian rational division")
        return C((self.re * other.re + self.im * other.im) / denominator,
                 (self.im * other.re - self.re * other.im) / denominator)

    def __rtruediv__(self, other):
        return cc(other) / self

    def conj(self):
        return C(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __eq__(self, other):
        if not isinstance(other, (C, int, F)):
            return False
        other = cc(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return "C(%s,%s)" % (self.re, self.im)

def cc(value):
    return value if isinstance(value, C) else C(value)

ZERO = C()
ONE = C(1)

def norm2(value):
    value = cc(value)
    return value.re * value.re + value.im * value.im

def zero_matrix(n, m=None):
    if m is None:
        m = n
    return [[ZERO] * m for _ in range(n)]

def diagonal(values):
    out = zero_matrix(len(values))
    for i, value in enumerate(values):
        out[i][i] = cc(value)
    return out

def madd(a, b):
    return [[x + y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]

def msub(a, b):
    return [[x - y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]

def mscale(a, value):
    value = cc(value)
    return [[x * value for x in row] for row in a]

def dagger(a):
    return [[a[j][i].conj() for j in range(len(a))]
            for i in range(len(a[0]))]

def mm(a, b):
    need(len(a[0]) == len(b), "matrix dimensions")
    out = zero_matrix(len(a), len(b[0]))
    for i, row in enumerate(a):
        guard()
        for k, value in enumerate(row):
            if value:
                for j, right in enumerate(b[k]):
                    if right:
                        out[i][j] = out[i][j] + value * right
    return out

def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)

def sum_projectors(n, terms):
    out = zero_matrix(n)
    for weight, vector in terms:
        guard()
        need(len(vector) == n, "projector dimensions")
        weight = cc(weight)
        for i, left in enumerate(vector):
            if left:
                for j, right in enumerate(vector):
                    if right:
                        out[i][j] = (out[i][j]
                                     + weight * left * right.conj())
    return out

def entries(b, specifications):
    out = [ZERO] * (4 * b)
    for i, j, value in specifications:
        out[i * b + j] = out[i * b + j] + cc(value)
    return out

def unit(i, j, b=4):
    return entries(b, [(i, j, 1)])

def av(b=4):
    return entries(b, [(0, 0, 1), (1, 1, 1), (2, 2, 1)])

def bv(b=4):
    return entries(b, [(0, 1, 1), (1, 2, 1)])

def dv(b=4):
    return entries(b, [(1, 0, 1), (2, 1, -1)])

def fv(v):
    return entries(4, [(0, 2, 1), (3, 3, v)])

def ev(u):
    return entries(4, [(2, 0, 1), (3, 3, u)])

def make_r(s, r, u, v):
    return sum_projectors(16, [
        (1, av()), (1, bv()), (1, dv()),
        (s, fv(v)), (r, ev(u)),
        (s * norm2(v), unit(0, 3)),
        (r * norm2(u), unit(2, 3)),
        (r, unit(3, 0)), (s, unit(3, 2))
    ])

def make_q(s, r):
    return sum_projectors(20, [
        (1, av(5)), (1, bv(5)), (1, dv(5)),
        (s, entries(5, [(0, 2, 1), (3, 4, 1)])),
        (s, unit(3, 2, 5)), (s, unit(0, 4, 5)),
        (r, entries(5, [(2, 0, 1), (3, 3, 1)])),
        (r, unit(2, 3, 5)), (r, unit(3, 0, 5))
    ])

def gamma(a, b, leg="B"):
    need(leg in ("A", "B"), "partial transpose leg")
    out = zero_matrix(4 * b)
    for i in range(4):
        guard()
        for j in range(b):
            for k in range(4):
                for ell in range(b):
                    if leg == "B":
                        out[i * b + ell][k * b + j] = a[i * b + j][k * b + ell]
                    else:
                        out[k * b + j][i * b + ell] = a[i * b + j][k * b + ell]
    return out

def pt_claim(s, r, u, v, b=4, wrong_conjugates=False):
    terms = [
        (1, entries(b, [(0, 1, 1), (1, 0, 1)])),
        (1, entries(b, [(1, 2, 1), (2, 1, 1)])),
        (1, unit(0, 0, b)), (1, unit(2, 2, b))
    ]
    if b == 4:
        cu = u if wrong_conjugates else u.conj()
        cv = v if wrong_conjugates else v.conj()
        terms += [
            (r, entries(4, [(2, 3, cu), (3, 0, 1)])),
            (s, entries(4, [(0, 3, cv), (3, 2, 1)])),
            (r * norm2(u) + s * norm2(v), unit(3, 3))
        ]
    else:
        need(b == 5, "parent dimension")
        terms += [
            (r, entries(5, [(2, 3, 1), (3, 0, 1)])),
            (s, entries(5, [(0, 4, 1), (3, 2, 1)])),
            (r, unit(3, 3, 5)), (s, unit(3, 4, 5))
        ]
    out = sum_projectors(4 * b, terms)
    locations = [(0, 2), (1, 1), (2, 0)]
    central = [[s, 1, 1], [1, 1, -1], [1, -1, r]]
    for i, (ai, bi) in enumerate(locations):
        for j, (aj, bj) in enumerate(locations):
            out[ai * b + bi][aj * b + bj] += cc(central[i][j])
    return out

def partial_traces(a, b):
    alice = zero_matrix(4)
    bob = zero_matrix(b)
    for i in range(4):
        for k in range(4):
            alice[i][k] = sum((a[i * b + j][k * b + j]
                               for j in range(b)), ZERO)
    for j in range(b):
        for ell in range(b):
            bob[j][ell] = sum((a[i * b + j][i * b + ell]
                               for i in range(4)), ZERO)
    return alice, bob

def make_k(u, v, core=1):
    out = zero_matrix(4, 5)
    for j in range(3):
        out[j][j] = cc(core)
    out[3][3] = u
    out[3][4] = v
    return out

def filter_b(q, k):
    lifted = zero_matrix(16, 20)
    for i in range(4):
        for j in range(4):
            for old in range(5):
                lifted[i * 4 + j][i * 5 + old] = k[j][old]
    return mm(mm(lifted, q), dagger(lifted))

def ldl_psd(a):
    n = len(a)
    if any(a[i][j] != a[j][i].conj()
           for i in range(n) for j in range(n)):
        return None
    work = [row[:] for row in a]
    certificate = []
    for k in range(n):
        guard()
        pivot = work[k][k]
        if pivot.im or pivot.re < 0:
            return None
        if not pivot:
            if any(work[i][k] or work[k][i] for i in range(k + 1, n)):
                return None
            continue
        d = pivot.re
        vector = [ZERO] * n
        vector[k] = ONE
        for i in range(k + 1, n):
            vector[i] = work[i][k] / d
        certificate.append((d, vector))
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                work[i][j] = (work[i][j]
                              - vector[i] * vector[j].conj() * d)
    need(sum_projectors(n, certificate) == a, "LDL reconstruction")
    return certificate

def determinant(a):
    n = len(a)
    answer = 0
    for perm in permutations(range(n)):
        guard()
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        term = 1
        for i in range(n):
            term = term * a[i][perm[i]]
        answer = answer + (-term if inversions % 2 else term)
    return answer

def minor(a, rows, cols):
    return determinant([[a[i][j] for j in cols] for i in rows])

def rank_le_two(a):
    for rows in combinations(range(len(a)), 3):
        for cols in combinations(range(len(a[0])), 3):
            guard()
            need(minor(a, rows, cols) == 0, "rank exceeds two")

def reshape4(vector):
    return [vector[4 * i:4 * i + 4] for i in range(4)]

class P:
    # Sparse Laurent polynomials. A positive modulus imposes a root character;
    # modulus zero leaves that variable formal and unrestricted.
    __slots__ = ("ring", "terms")

    def __init__(self, ring, terms=None):
        self.ring = tuple(ring)
        combined = {}
        for exponent, coefficient in (terms or {}).items():
            need(len(exponent) == len(self.ring), "polynomial dimension")
            key = tuple(e % m if m else e
                        for e, m in zip(exponent, self.ring))
            combined[key] = combined.get(key, ZERO) + cc(coefficient)
        self.terms = {e: c for e, c in combined.items() if c}

    def lift(self, other):
        if isinstance(other, P):
            need(self.ring == other.ring, "polynomial ring mismatch")
            return other
        return P(self.ring, {(0,) * len(self.ring): cc(other)})

    def __add__(self, other):
        other = self.lift(other)
        terms = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            terms[exponent] = terms.get(exponent, ZERO) + coefficient
        return P(self.ring, terms)

    __radd__ = __add__

    def __neg__(self):
        return P(self.ring, {e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        guard()
        other = self.lift(other)
        terms = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                exponent = tuple(x + y for x, y in zip(left, right))
                exponent = tuple(e % m if m else e
                                 for e, m in zip(exponent, self.ring))
                terms[exponent] = terms.get(exponent, ZERO) + a * b
        return P(self.ring, terms)

    __rmul__ = __mul__

    def __pow__(self, power):
        need(isinstance(power, int) and power >= 0, "polynomial power")
        answer = self.lift(1)
        base = self
        while power:
            guard()
            if power % 2:
                answer = answer * base
            base = base * base
            power //= 2
        return answer

    def __eq__(self, other):
        if not isinstance(other, (P, C, int, F)):
            return False
        other = self.lift(other)
        return self.terms == other.terms

    def star(self):
        return P(self.ring, {
            tuple(-e if m else e for e, m in zip(exponent, self.ring)):
            coefficient.conj()
            for exponent, coefficient in self.terms.items()
        })

def monomial(ring, exponent):
    return P(ring, {tuple(exponent): ONE})

def root_matrix(v, modw=3, phase=-1):
    ring = (0, 4, modw)
    def m(t, z, w):
        return monomial(ring, (t, z, w))
    zero = P(ring)
    one = m(0, 0, 0)
    return [
        [m(0, 1, 0), one, m(0, -1, 0), m(1, 1, 1) * 2],
        [m(0, 2, 0) * phase, m(0, 1, 0), one, zero],
        [zero, m(0, 2, 0) * (-phase), m(0, 1, 0), m(1, 3, 1)],
        [m(-1, -1, -1) * v, zero, zero, m(0, -1, 0) * v]
    ]

def check_columns(a):
    ring = a[0][0].ring
    zi = monomial(ring, (0, -1, 0))
    tw = monomial(ring, (1, 0, 1))
    tzw = monomial(ring, (1, 1, 1))
    for i in range(4):
        need(a[i][2] == zi * a[i][1], "first column relation")
        need(a[i][3] == tw * a[i][0] + tzw * a[i][1],
             "second column relation")

def average_value(poly, alpha_squared):
    answer = ZERO
    for exponent, coefficient in poly.terms.items():
        t, z, w = exponent
        if z == 0 and w == 0:
            need(t % 2 == 0, "uncancelled odd alpha power")
            answer += coefficient * (alpha_squared ** (t // 2))
    return answer

def average_projector(a, alpha_squared):
    need(alpha_squared > 0, "positive alpha squared")
    vector = [entry for row in a for entry in row]
    out = zero_matrix(16)
    for i, left in enumerate(vector):
        guard()
        for j, right in enumerate(vector):
            out[i][j] = average_value(left * right.star(), alpha_squared)
    return out

def reflect(a):
    signs = [1, 1, -1, 1]
    return [[a[j][i] * (signs[i] * signs[j]) for j in range(4)]
            for i in range(4)]

def expected_g(v, a):
    return sum_projectors(16, [
        (1, av()), (1, bv()), (1, dv()), (1, fv(v)),
        (4 * a, unit(0, 3)), (a, unit(2, 3)),
        (norm2(v) / a, unit(3, 0))
    ])

def expected_h(u, a):
    return sum_projectors(16, [
        (1, av()), (1, bv()), (1, dv()), (1, ev(u)),
        (4 * a, unit(3, 0)), (a, unit(3, 2)),
        (norm2(u) / a, unit(0, 3))
    ])

def check_roots(u, v, a):
    gm = root_matrix(v)
    check_columns(gm)
    rank_le_two(gm)
    g = average_projector(gm, a)
    need(g == expected_g(v, a), "G root average")

    hm = reflect(root_matrix(-u))
    rank_le_two(hm)
    h = average_projector(hm, a)
    need(h == expected_h(u, a), "H root average")
    return g, h

def core_average():
    a = root_matrix(ZERO)
    ring = a[0][0].ring
    for i in range(4):
        for j in range(4):
            if i == 3 or j == 3:
                a[i][j] = P(ring)
    rank_le_two(a)
    out = average_projector(a, F(1))
    expected = sum_projectors(16, [
        (1, av()), (1, bv()), (1, dv()), (1, unit(0, 2))
    ])
    need(out == expected, "four-root core average")
    return out

def decomposition(s, r, u, v, forced=None):
    uu, vv = norm2(u), norm2(v)
    case = (1 if not v else 2 if vv <= r * r * uu else 3)
    if forced is not None:
        case = forced
    if case == 1:
        base = core_average()
        terms = [
            (s - 1, unit(0, 2)), (r, ev(u)),
            (r * uu, unit(2, 3)), (r, unit(3, 0)),
            (s, unit(3, 2))
        ]
        return case, None, base, terms
    a = vv / r if case == 2 else F(1) / (s * r * r)
    g, h = check_roots(u, v, a)
    if case == 2:
        terms = [
            (s - 1, fv(v)), (r, ev(u)),
            (vv * (s - F(4) / r), unit(0, 3)),
            (r * uu - vv / r, unit(2, 3)),
            (s, unit(3, 2))
        ]
        return case, a, g, terms
    terms = [
        (s, fv(v)), (r - 1, ev(u)),
        (s * (vv - r * r * uu), unit(0, 3)),
        (r * uu, unit(2, 3)),
        (r - F(4) / (s * r * r), unit(3, 0)),
        (s - F(1) / (s * r * r), unit(3, 2))
    ]
    return case, a, h, terms

def validate_remainder(terms):
    for coefficient, vector in terms:
        need(coefficient >= 0, "negative remainder coefficient")
        rank_le_two(reshape4(vector))

def check_primary_minors():
    ring = (0,) * 9
    variables = []
    for i in range(9):
        exponent = [0] * 9
        exponent[i] = 1
        variables.append(monomial(ring, exponent))
    a, b, c, d, e, f, g, h, k = variables
    z = P(ring)
    y = [
        [a, b, c, z, h],
        [d, a, b, z, z],
        [e, -d, a, k, z],
        [f, z, g, e, c]
    ]
    locations = [
        ((0, 1, 3), (0, 1, 3)),
        ((1, 2, 3), (1, 2, 4)),
        ((0, 1, 3), (1, 2, 3)),
        ((1, 2, 3), (0, 1, 4)),
        ((0, 1, 2), (0, 1, 2))
    ]
    calculated = [minor(y, rows, cols) for rows, cols in locations]
    expected = [
        e * (a * a - b * d),
        c * (a * a + b * d),
        e * (b * b - a * c),
        -c * (d * d + a * e),
        a ** 3 + b * b * e - d * d * c - a * c * e
    ]
    for i, (left, right) in enumerate(zip(calculated, expected), 1):
        need(left == right, "primary minor %d" % i)
    g1, g2, g3, g4, g5 = calculated
    need(a * (g5 - g3 - g4)
         - (c * g1 + e * g2) * F(1, 2) == a ** 4,
         "a-fourth identity")
    print("PASS", "five formal minors and a-fourth identity")

def ppt_region(s, r):
    return s > 1 and r > 1 and (s - 1) * (r - 1) >= 4

def check_central(s, r):
    central = [
        [C(s), ONE, ONE],
        [ONE, ONE, C(-1)],
        [ONE, C(-1), C(r)]
    ]
    residual = r - 1 - F(4) / (s - 1)
    need(residual >= 0, "central residual sign")
    expansion = sum_projectors(3, [
        (1, [ONE, ONE, C(-1)]),
        (s - 1, [ONE, ZERO, C(F(2) / (s - 1))]),
        (residual, [ZERO, ZERO, ONE])
    ])
    need(central == expansion, "central expansion")
    need(ldl_psd(central) is not None, "central LDL")

def check_case(name, s, r, u, v):
    guard()
    need(ppt_region(s, r), "positive fixture region")
    rr, qq = make_r(s, r, u, v), make_q(s, r)
    uu, vv = norm2(u), norm2(v)
    z = 7 + 2 * (s + r) + 2 * (s * vv + r * uu)
    tq = 7 + 4 * (s + r)
    need(trace(rr) == z and trace(qq) == tq, "trace formulas")
    need(ldl_psd(rr) is not None, "R PSD")
    need(ldl_psd(qq) is not None, "Q PSD")
    rpt, qpt = gamma(rr, 4), gamma(qq, 5)
    need(rpt == pt_claim(s, r, u, v), "R Bob Gamma identity")
    need(qpt == pt_claim(s, r, u, v, 5), "Q Bob Gamma identity")
    rcert, qcert = ldl_psd(rpt), ldl_psd(qpt)
    need(rcert is not None and qcert is not None, "PPT LDL")
    check_central(s, r)

    ra, rb = partial_traces(rr, 4)
    need(ra == diagonal([
        2 + s + s * vv, 3, 2 + r + r * uu,
        s + r + s * vv + r * uu
    ]), "R Alice marginal")
    need(rb == diagonal([
        2 + 2 * r, 3, 2 + 2 * s, 2 * (s * vv + r * uu)
    ]), "R Bob marginal")
    qa, qb = partial_traces(qq, 5)
    need(qa == diagonal([2 + 2 * s, 3, 2 + 2 * r, 2 * (s + r)]),
         "Q Alice marginal")
    need(qb == diagonal([2 + 2 * r, 3, 2 + 2 * s, 2 * r, 2 * s]),
         "Q Bob marginal")

    k = make_k(u, v)
    need(filter_b(qq, k) == rr, "whole filter identity")
    need(mm(k, dagger(k)) == diagonal([1, 1, 1, uu + vv]),
         "K row Gram")
    m = max(F(1), uu + vv)
    effect_slack = msub(diagonal([m] * 5), mm(dagger(k), k))
    need(ldl_psd(effect_slack) is not None, "K contraction bound")
    unnormalized = mscale(filter_b(qq, k), F(1) / (m * tq))
    probability = z / (m * tq)
    need(trace(unnormalized) == probability, "success probability")
    need(mscale(unnormalized, F(1) / probability)
         == mscale(rr, F(1) / z), "normalized output")

    case, a, base, terms = decomposition(s, r, u, v)
    validate_remainder(terms)
    need(madd(base, sum_projectors(16, terms)) == rr,
         "complete SN2 decomposition identity")
    print("PASS CASE", name, "s", s, "r", r, "u", u, "v", v,
          "case", case, "alpha_squared", a, "trace", z,
          "probability", probability,
          "PT_ranks", len(rcert), len(qcert))

def must_reject(name, expected_reason, operation):
    guard()
    try:
        operation()
    except CheckFailure as error:
        need(str(error) == expected_reason,
             "wrong mutation rejection: " + name + ": " + str(error))
    else:
        raise CheckFailure("mutation accepted: " + name)
    print("MUTANT_REJECTED", name, expected_reason)

def require_equal(left, right, reason):
    need(left == right, reason)

def detector_necessary_condition(w, psi):
    # This can reject a detector claim; it cannot certify universal
    # two-block-positivity from a finite test.
    rank_le_two(reshape4(psi))
    value = ZERO
    for i, left in enumerate(psi):
        for j, right in enumerate(psi):
            value += left.conj() * w[i][j] * right
    need(value.im == 0 and value.re >= 0,
         "negative expectation on rank-at-most-two vector")

def check_mutations():
    s = r = F(3)
    u, v = C(1, 1), C(1, -1)
    rr = make_r(s, r, u, v)
    correct_pt = pt_claim(s, r, u, v)

    must_reject(
        "wrong Gamma leg", "wrong Gamma leg",
        lambda: require_equal(gamma(rr, 4, "A"), correct_pt,
                              "wrong Gamma leg"))
    must_reject(
        "missing conjugation", "missing conjugation",
        lambda: require_equal(pt_claim(s, r, u, v, wrong_conjugates=True),
                              correct_pt, "missing conjugation"))
    must_reject(
        "wrong rank-two phase", "rank exceeds two",
        lambda: rank_le_two(root_matrix(v, phase=1)))
    a = F(1, 3)
    must_reject(
        "C4 times C2 instead of C4 times C3", "wrong root order",
        lambda: require_equal(
            average_projector(root_matrix(v, modw=2), a),
            expected_g(v, a), "wrong root order"))

    def wrong_split():
        su, sv = C(1), C(0, 2)
        uu, vv = norm2(su), norm2(sv)
        wrong_case = 2 if vv <= r * uu else 3
        need(wrong_case != (2 if vv <= r * r * uu else 3),
             "split mutation fixture")
        _, _, _, terms = decomposition(s, r, su, sv, forced=wrong_case)
        validate_remainder(terms)

    must_reject("r versus r-squared split", "negative remainder coefficient",
                wrong_split)

    def negative_filler():
        _, _, _, terms = decomposition(s, r, C(1), C(1))
        coefficient, vector = terms[0]
        changed = [(-coefficient, vector)] + terms[1:]
        validate_remainder(changed)

    must_reject("negative filler", "negative remainder coefficient",
                negative_filler)

    must_reject(
        "false SN3 detector", "negative expectation on rank-at-most-two vector",
        lambda: detector_necessary_condition(diagonal([-1] * 16), unit(0, 3)))

    qq = make_q(s, r)
    assigned_r = make_r(s, r, C(1), C(1))
    must_reject(
        "extension-only map substituted for whole filter", "whole filter mismatch",
        lambda: require_equal(
            filter_b(qq, make_k(C(1), C(1), core=0)),
            assigned_r, "whole filter mismatch"))

def check_assigned_example():
    s = r = F(3)
    u = v = C(1)
    rr, qq = make_r(s, r, u, v), make_q(s, r)
    need(trace(rr) == 31 and trace(qq) == 31, "assigned trace 31")
    ra, rb = partial_traces(rr, 4)
    expected = diagonal([8, 3, 8, 12])
    need(ra == expected and rb == expected, "assigned marginals")
    g, _ = check_roots(u, v, F(1, 3))
    remainder = sum_projectors(16, [
        (2, fv(v)), (3, ev(u)),
        (F(5, 3), unit(0, 3)),
        (F(8, 3), unit(2, 3)), (3, unit(3, 2))
    ])
    need(msub(rr, g) == remainder, "assigned SN2 remainder")
    explicit_pt = sum_projectors(16, [
        (1, entries(4, [(0, 1, 1), (1, 0, 1)])),
        (1, entries(4, [(1, 2, 1), (2, 1, 1)])),
        (1, entries(4, [(0, 2, 1), (1, 1, 1), (2, 0, -1)])),
        (2, entries(4, [(0, 2, 1), (2, 0, 1)])),
        (3, entries(4, [(2, 3, 1), (3, 0, 1)])),
        (3, entries(4, [(0, 3, 1), (3, 2, 1)])),
        (1, unit(0, 0)), (1, unit(2, 2)), (6, unit(3, 3))
    ])
    need(gamma(rr, 4) == explicit_pt, "assigned PPT expansion")
    filtered = mscale(filter_b(qq, make_k(u, v)), F(1, 62))
    need(trace(filtered) == F(1, 2), "assigned success one-half")
    need(mscale(filtered, 2) == mscale(rr, F(1, 31)),
         "assigned normalized output")
    print("PASS", "assigned trace, marginals, PPT, remainder and success")

def main():
    check_primary_minors()
    cases = [
        ("assigned-boundary", F(3), F(3), C(1), C(1)),
        ("complex-boundary", F(3), F(3), C(1, 1), C(1, -1)),
        ("complex-interior", F(2), F(6), C(1, 1), C(1, 2)),
        ("case-two-split-control", F(3), F(3), C(1), C(0, 2)),
        ("case-three-both-active", F(3), F(3), C(1), C(0, 4)),
        ("v-zero", F(3), F(3), C(1, 2), C(0)),
        ("u-zero-other-boundary", F(5), F(2), C(0), C(1, 1)),
        ("both-zero", F(3), F(3), C(0), C(0))
    ]
    for fixture in cases:
        check_case(*fixture)
    for s, r in [
        (F(1), F(3)), (F(3), F(1)), (F(2), F(2)),
        (F(2), F(4)), (F(1, 2), F(3))
    ]:
        guard()
        need(s > 0 and r > 0 and not ppt_region(s, r),
             "outside fixture region")
        u, v = C(1, 1), C(1, -1)
        rr, qq = make_r(s, r, u, v), make_q(s, r)
        need(ldl_psd(rr) is not None and ldl_psd(qq) is not None,
             "outside fixtures remain physical")
        need(ldl_psd(gamma(rr, 4)) is None, "outside R not PPT")
        need(ldl_psd(gamma(qq, 5)) is None, "outside Q not PPT")
        print("PASS OUTSIDE REGION", s, r)
    check_assigned_example()
    check_mutations()
    guard()
    print("COMPLETE", "all declared exact checks and eight intended-reason controls",
          "elapsed_seconds", monotonic() - START)

try:
    main()
except CheckFailure as error:
    print("FAIL", str(error))
    raise SystemExit(1)
except TimeoutError:
    print("INCOMPLETE", "54-second cooperative computation deadline")
    raise SystemExit(2)
SOURCE END

## 4. Exact scope and remaining ceiling

The written result concerns **only** the specified weighted grid family and Bob maps that preserve the three core coordinates and coherently merge the two extension coordinates. Within that family, its proof supports:

- The exact PPT parameter region, including its boundary.
- Arbitrary complex \(u,v\), including either or both zero.
- Schmidt number exactly two for every PPT output.
- Full \(4\times4\) local support when \((u,v)\ne(0,0)\).
- Impossibility of a valid, fully complex rank-two-block-positive detector having negative expectation on one of those outputs.

The finite checker, even if subsequently completed successfully, would not by selected cases alone establish these universal claims. Their universal support is the written decomposition, character identities, polynomial identity and range argument.

**Not established:** unrestricted \(4\times4\) PPT/SN3 existence or nonexistence; arbitrary \(5\to4\) filters mixing core and extension coordinates; other grid/filler families; novelty or priority; human, kernel, cross-vendor or independent-model-family acceptance. The detector mutation only rejects an invalid proposed detector; it does not certify universal block positivity through finite sampling.

No file was written. Main can materialize this complete body and, in an execution-authorized context, run the exact prospective argv above and retain its actual results. Until then, the computational gate remains **NOT RUN**, not passed.

**Findings:** None meeting the evidence-backed mathematical-defect criteria in the frozen manuscript.

**overall_correctness:** correct

**explanation:** The frozen coherent-merger manuscript’s physical identities, PPT region, rank-two decomposition and range arguments are consistent under independent written checking. This verdict is confined to that stated family; the executable gate remains NOT RUN and there is no original-target, novelty or automatic-adoption claim.

**confidence:** 0.95